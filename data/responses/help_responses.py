from typing import List


class GlobalHelp:

    @staticmethod
    def help_introduction() -> List[str]:
        utter_help_intro1 = "Hello this is food chatbot which help you to find recipe information and  " \
                            "create meal plan for " \
                            "you "
        utter_help_intro2 = "There are 2 helping option that may can help you to get recipe or nutrient  " \
                            "you can typing these 2 below "
        utter_help_intro3 = "'How to get recipe ?'"
        utter_help_intro4 = "'How to set nutrient setting ?'"

        return [utter_help_intro1, utter_help_intro2, utter_help_intro3, utter_help_intro4]
