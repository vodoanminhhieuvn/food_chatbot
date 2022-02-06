from typing import Text, Dict, Any, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from base_models.rasa_model.message_tracker_model import MessageTracker, Entity
from base_models.rasa_model.slot_model import slot


class ActionSetIngredient(Action):
    def name(self) -> Text:
        return "action_set_ingredients"

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        list_ingredient: List[str] = []
        tracker.latest_message['entities'] = sorted(tracker.latest_message['entities'], key=lambda i: i['start'])
        message_tracker: MessageTracker = MessageTracker(**tracker.latest_message)

        current_index: int = 0
        entity: Entity
        for entity in message_tracker.entities:
            if entity.type == 'or' and list_ingredient[current_index]:
                current_index += 1

            if entity.type == 'ingredient':
                try:
                    list_ingredient[current_index] += f"{entity.value} "
                except IndexError:
                    list_ingredient.append(entity.value)

        slot.set_list_ingredient(list_ingredient)

        print(slot.list_ingredients)

        return []
