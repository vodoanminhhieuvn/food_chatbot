import enum
from typing import Dict

from requests import Response

from api.network_util import NetworkUtil, NetworkMethod
from utils.global_configuration import GlobalConfiguration


class EdamamMethod(enum.Enum):
    GET_RECIPES = 1
    NEXT_RECIPES = 2

