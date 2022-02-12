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

        tracker.latest_message['entities'] = sorted(tracker.latest_message['entities'], key=lambda i: i['start'])
        message_tracker: MessageTracker = MessageTracker(**tracker.latest_message)

        # Check should clear list entity
        if slot.recipe_parts_slots.check_should_clear(message_tracker.entities):
            slot.recipe_parts_slots.parts = []

        # Update recipe parts
        slot.recipe_parts_slots.append_list(message_tracker.entities)
        # Sort list
        slot.recipe_parts_slots.filter_parts()

        # Check for missing components => utter request
        if self.request_more_part(dispatcher, slot.recipe_parts_slots.parts):
            return []

        # Else
        # Run handle creating search keywords by rule
        print(slot.recipe_parts_slots.parts)
        slot.recipe_search_keyword_slots = (
            slot.recipe_parts_slots.create_search_keywords()
        )

        # result utter
        dispatcher.utter_message("Your search is:")
        for item in slot.recipe_search_keyword_slots:
            dispatcher.utter_message(item)
        return []

    @staticmethod
    def request_more_part(
            dispatcher: CollectingDispatcher, recipe_parts: list
    ) -> bool:
        if all(item.type != "ingredient" for item in recipe_parts):
            dispatcher.utter_message(text="Give me main ingredient")
            return True
        elif all(item.type != "cook_technique" for item in recipe_parts):
            dispatcher.utter_message(text="You can provide me a cook technique")
            return True
        else:
            return False
