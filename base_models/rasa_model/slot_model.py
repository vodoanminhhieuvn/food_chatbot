from typing import List

from base_models.food_model.nutrient_model import NutrientModel
from base_models.food_model.recipe_part_model import RecipePartsModel


class Slot:
    target_calory: int = 2000
    diet: str = ""
    nutrient_slots = NutrientModel()
    recipe_parts_slots = RecipePartsModel()
    recipe_search_keyword_slots: list = []

    def set_nutrient_attr(self, name: str, value: int):
        self.nutrient_slots.__setattr__(name, value)


slot = Slot()
