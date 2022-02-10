import json
from typing import TextIO

from pydantic import BaseModel


class SpoonApiConfigModel(BaseModel):
    key: str
    searchUrl: str
    generateMealUrl: str


class EdamamApiConfigModel(BaseModel):
    id: str
    key: str
    searchUrl: str


class GlobalConfiguration:
    edamam_api_config: EdamamApiConfigModel
    spooncular_api_config: SpoonApiConfigModel

    @classmethod
    def set_config(cls):
        file: TextIO
        with open('assets/api/edamam.json') as file:
            edamam_config = json.load(file)
            cls.edamam_api_config = EdamamApiConfigModel(**edamam_config)

        with open('assets/api/spooncular.json') as file:
            spooncular_config = json.load(file)
            cls.spooncular_api_config = SpoonApiConfigModel(**spooncular_config)
