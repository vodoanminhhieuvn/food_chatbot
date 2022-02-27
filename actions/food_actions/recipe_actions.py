from typing import Text, Dict, Any, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from requests import Response

from api.get_api import GetApi, EdamamMethod, get_food_recipe
from base_models.rasa_model.slot_model import slot
from data.responses.food_reponses.recipe_responses import RecipeResponses


class ActionGetRecipe(Action):
    def name(self) -> Text:
        return "action_get_recipe"

    def run(
            self,
            dispatcher: "CollectingDispatcher",
            tracker: Tracker,
            domain: DomainDict,
    ) -> List[Dict[Text, Any]]:
        response: Response = GetApi.request_edamam(EdamamMethod.GET_RECIPES,
                                                   params=get_food_recipe("Chicken", nutrient_info=slot.nutrient_slots))

        print(response)
        return []


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
