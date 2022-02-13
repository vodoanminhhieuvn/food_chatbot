from typing import Text, Dict, Any, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from data.responses.food_reponses.recipe_responses import RecipeResponses


class ActionHelpGetRecipe(Action):
    def name(self) -> Text:
        return "action_help_get_recipe"

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        for messages in RecipeResponses.help_get_recipe():
            dispatcher.utter_message(messages)

        return []
