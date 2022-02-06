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


class RequestApiConfigModel(BaseModel):
    spoonApi: SpoonApiConfigModel
    edamamApi: EdamamApiConfigModel


class GlobalConfiguration:
    request_api_config: RequestApiConfigModel

    def set_config(self):
        file: TextIO
        with open('assets/api_key/api_key.json') as file:
            data = json.load(file)
            self.request_api_config = RequestApiConfigModel(**data)
