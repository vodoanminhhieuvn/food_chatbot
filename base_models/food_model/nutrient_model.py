from typing import Optional

from pydantic import BaseModel, root_validator


class NutrientModel(BaseModel):
    min_calories: Optional[int] = 50
    max_calories: Optional[int] = 800
    min_fat: Optional[int] = 10
    max_fat: Optional[int] = 200

    class Config:
        validate_assignment = True

    @classmethod
    @root_validator()
    def validate_valid_min_max(cls, values):
        min_calories = values["min_calories"] = values["min_calories"] or 50
        max_calories = values["max_calories"] = values["max_calories"] or 800
        min_fat = values["min_fat"] = values["min_fat"] or 10
        max_fat = values["max_fat"] = values["max_fat"] or 200

        if min_calories > max_calories:
            values["min_calories"], values["max_calories"] = (max_calories, min_calories)

        if min_fat > max_fat:
            values["min_fat"], values["max_fat"] = max_fat, min_fat

        return values
