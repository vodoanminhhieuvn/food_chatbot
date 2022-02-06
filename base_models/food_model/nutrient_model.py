from typing import Optional

from pydantic import BaseModel, root_validator


class NutrientModel(BaseModel):
    minCalories: Optional[int] = 50
    maxCalories: Optional[int] = 800
    minFat: Optional[int] = 10
    maxFat: Optional[int] = 200

    class Config:
        validate_assignment = True

    @classmethod
    @root_validator()
    def validate_valid_min_max(cls, values):
        min_calories = values["minCalories"] = values["minCalories"] or 50
        max_calories = values["maxCalories"] = values["maxCalories"] or 800
        min_fat = values["minFat"] = values["minFat"] or 10
        max_fat = values["maxFat"] = values["maxFat"] or 200

        if min_calories > max_calories:
            values["minCalories"], values["maxCalories"] = (max_calories, min_calories)

        if min_fat > max_fat:
            values["minFat"], values["maxFat"] = max_fat, min_fat

        return values
