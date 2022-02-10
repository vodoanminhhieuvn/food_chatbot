import enum
from typing import Dict

from requests import Response

from api.network_util import NetworkUtil, NetworkMethod
from utils.global_configuration import GlobalConfiguration


class EdamamMethod(enum.Enum):
    GET_RECIPES = 1
    NEXT_RECIPES = 2


class SpooncularMethod(enum.Enum):
    GET_RECIPE = 1
    GENERATE_MEAL_PLAN = 2


class GetApi:
    @staticmethod
    def request_edamam(edamam_method: EdamamMethod):
        response: Response

        if edamam_method == EdamamMethod.GET_RECIPES:
            response = NetworkUtil.request(GlobalConfiguration.edamam_api_config.searchUrl, params=[],
                                           method=NetworkMethod.GET)
        else:
            response = NetworkUtil.request(GlobalConfiguration.spooncular_api_config.generateMealUrl, params=[],
                                           method=NetworkMethod.GET)

        return response

    @staticmethod
    def request_spooncular(spooncular_method: SpooncularMethod):
        response: Response

        if spooncular_method == SpooncularMethod.GENERATE_MEAL_PLAN:
            response = NetworkUtil.request(GlobalConfiguration.spooncular_api_config.generateMealUrl, params=[],
                                           method=NetworkMethod.GET)
        else:
            response = NetworkUtil.request(GlobalConfiguration.spooncular_api_config.generateMealUrl, params=[],
                                           method=NetworkMethod.GET)

        return response


def load_edamam_config() -> Dict[str, str]:
    return {
        "app_id": GlobalConfiguration.edamam_api_config.id,
        "app_key": GlobalConfiguration.edamam_api_config.key,
        "type": "public",
    }


def load_spooncular_config() -> Dict[str, str]:
    return {
        "apiKey": GlobalConfiguration.spooncular_api_config.key,
    }
