from typing import List


class RecipeResponses:

    @staticmethod
    def help_get_recipe() -> List[str]:
        utter_help_get_recipe1 = (
            "First you need type ingredient you want to be in recipe \nI want to cook chicken"
        )
        utter_help_get_recipe2 = "Then you an type 'Get me recipe' to get 5 examples recipe"
        utter_help_get_recipe3 = "I will give option you can choose to know more about these recipe and ingredient " \
                                 "that " \
                                 "in recipe "

        return [utter_help_get_recipe1, utter_help_get_recipe2, utter_help_get_recipe3]
