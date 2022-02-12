from typing import List

from pydantic import BaseModel

# part == Entity
from base_models.rasa_model.message_tracker_model import Entity


def is_reg_extractor(entity: Entity) -> bool:
    return entity.extractor == "RegexEntityExtractor"


# sort list entity base on order in message
def sort(entities: List[Entity]):
    def compare_to(e):
        return e.start

    entities.sort(key=compare_to)
    return entities


class RecipePartsModel(BaseModel):
    parts: List[Entity] = []

    def check_should_clear(self, new_parts: List[Entity]):
        has_ingredient_in_old = any(item.type == "ingredient" for item in self.parts)
        has_technique_in_old = any(
            item.type == "cook_technique" for item in self.parts
        )
        has_ingredient_in_new = any(item.type == "ingredient" for item in new_parts)
        has_technique_in_new = any(
            item.type == "cook_technique" for item in new_parts
        )

        return (
                has_ingredient_in_new
                and has_ingredient_in_old
                or has_technique_in_new
                and has_technique_in_old
        )

    def append_list(self, entities: List[Entity]):
        # TODO: check should filter regex
        # entities_filtered = list(filter(is_reg_extractor, entities))
        # entities_sorted = sort(entities_filtered)
        entities_sorted = sort(entities)
        self.parts += entities_sorted

    def create_search_keywords(self) -> list:
        # ?     type |  or      and
        # ?     same |  x2       +
        # ?     diff |  split    +

        # branch will generate search key
        branch_list = []
        # index of list parts
        index = 0
        # index of complete branch
        check_first_index = 0

        while index < len(self.parts):
            item = self.parts[index]
            if item.type == "or":
                if self.parts[index - 1].type == self.parts[index + 1].type:
                    for _ in range(check_first_index, len(branch_list)):
                        branch = branch_list[check_first_index]
                        del branch[-1]
                        branch_list.append(branch + [self.parts[index - 1]])
                        branch_list.append(branch + [self.parts[index + 1]])
                        del branch
                    index += 1
                else:
                    check_first_index += 1

            elif len(branch_list) == 0:
                branch_list.append([item])
            else:
                for i in range(check_first_index, len(branch_list)):
                    branch_list[i].append(item)

            index += 1

        search_list = []
        for item in branch_list:
            search_list.append(item[0].value)
            for i in range(1, len(item)):
                search_list[-1] += " " + item[i].value

        return search_list

    # remove redundant parts
    def filter_parts(self):

        for index, val in enumerate(self.parts):
            if (val.type not in ["or", "cook_technique", "ingredient"]) or (val.type == "or" and (
                    index == 0
                    or index == len(self.parts) - 1
                    or self.parts[index + 1].type == "or"
            )):
                del self.parts[index]
