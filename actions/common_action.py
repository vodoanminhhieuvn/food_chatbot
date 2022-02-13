from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

# ? Global helping

"Utter for global helping"

utter_intro1 = "Hello this is food chatbot which help you to find recipe infomation and create meal plan for you"
utter_intro2 = "There are 2 helping option that may can help you to get recipe or nutrient you can typing these 2 below"
utter_intro3 = "'How to get recipe ?'"
utter_intro4 = "'How to set nutrient setting ?'"

# ? Recipe helping
"Utter for recipe helping"

utter_help_recipe1 = (
    "First you need type ingredient you want to be in recipe \nI want to cook chicken"
)
utter_help_recipe2 = "Then you an type 'Get me recipe' to get 5 examples recipe"
utter_help_recipe3 = "I will give option you can choose to know more about these recipe and ingredient that in recipe"

# ? Nutrient helping
"Utter for Nutrient helping"

utter_help_nutrient1 = (
    "There will be default value for nutrient \nYou can see this below"
)
utter_help_nutrient2 = "You can type: 'current calory or any nutrient setting'  to view your current nutrient setting"
utter_help_nutrient3 = "Example: current calory setting"
utter_help_nutrient4 = "To reset nutrient setting you can type"
utter_help_nutrient5 = "reset all nutrient to reset all value to default \nOr"
utter_help_nutrient6 = "reset calory setting to reset calory value to default"


class ActionHelpCommon(Action):
    def name(self) -> Text:
        return "action_help"

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        return []

    def _show_utter_message(self, dispatcher, arg1, arg2, arg3):
        dispatcher.utter_message(arg1)
        dispatcher.utter_message(arg2)
        dispatcher.utter_message(arg3)

    def _extract_help_utter(self, dispatcher, arg1, arg2, arg3):
        self._show_utter_message(dispatcher, arg1, arg2, arg3)