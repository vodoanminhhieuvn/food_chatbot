from typing import List

from base_models.food_model.nutrient_model import NutrientModel


class Slot:
    target_calory: int = 2000
    diet: str = ""
    nutrient_slots = NutrientModel()
    list_ingredients: List[str]

    def set_nutrient_attr(self, name: str, value: int):
        self.nutrient_slots.__setattr__(name, value)

    def set_list_ingredient(self, list_ingredient: List[str]):
        self.list_ingredients = list_ingredient


slot = Slot()
