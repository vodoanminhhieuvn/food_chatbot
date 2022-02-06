from pydantic import BaseModel


class ButtonMessageModel(BaseModel):
    title: str
    payload: str
