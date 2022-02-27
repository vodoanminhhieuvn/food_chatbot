from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from base_models.food_model.nutrient_model import NutrientModel
from base_models.rasa_model.message_tracker_model import MessageTracker
from base_models.rasa_model.slot_model import slot


class ActionGetNutrient(Action):
    def name(self) -> Text:
        return "action_set_nutrient"

    async def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        min_values = []
        max_values = []
        nutrient_type = []

        message_tracker = MessageTracker(**tracker.latest_message)

        for entity in message_tracker.entities:
            if entity.type == "min":

                min_values.append(entity.value)

            elif entity.type == "max":

                max_values.append(entity.value)

            elif entity.type == "nutrient":
                nutrient_type.append(entity.value)

        if not (self._check_valid_nutrient(dispatcher, nutrient_type)):
            return []

        if not (
                self._add_nutrient_to_slot(
                    dispatcher, min_values, max_values, nutrient_type[0]
                )
        ):
            return []

        min_display_value = slot.nutrient_slots.dict()[f"min_{nutrient_type[0]}"]
        max_display_value = slot.nutrient_slots.dict()[f"max_{nutrient_type[0]}"]

        dispatcher.utter_message(
            text=f"{nutrient_type[0]}\nMin: {min_display_value} - Max: {max_display_value}"
        )

        return []

    def _check_valid_nutrient(
            self, dispatcher: CollectingDispatcher, nutrient_type: list
    ):
        if len(nutrient_type) >= 2:
            return self._too_much_info(
                dispatcher, "You can't input 2 nutrient type values"
            )
        return True

    def _add_nutrient_to_slot(
            self,
            dispatcher: CollectingDispatcher,
            min_values: list,
            max_values: list,
            nutrient_type: str,
    ):
        if len(min_values) >= 2 or len(max_values) >= 2:
            return self._too_much_info(
                dispatcher, "You can't input 2 minimum or maximum type values"
            )

        slot.nutrient_slots = NutrientModel(
            **slot.nutrient_slots.copy(
                update={
                    f"min{nutrient_type}": min_values[0]
                    if 0 < len(min_values)
                    else slot.nutrient_slots.dict()[f"min_{nutrient_type}"],
                    f"max{nutrient_type}": max_values[0]
                    if 0 < len(max_values)
                    else slot.nutrient_slots.dict()[f"max_{nutrient_type}"],
                }
            ).dict()
        )

        return True

    @staticmethod
    def _too_much_info(dispatcher, text):
        dispatcher.utter_message(text=text)
        dispatcher.utter_message(text="Please input only 1 value of each type")

        return False
