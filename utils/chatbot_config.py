# ? This file will contain config and will execute in actions to add config to chatbot
from utils.global_configuration import GlobalConfiguration


class AppConfig:
    global_configuration: GlobalConfiguration = GlobalConfiguration()

    # @param ClassMethod
    # ? được dùng để định nghĩa class này là class constants
    # ? dùng cho mấy hàm constants khi muốn truy cập vào biến của class

    @classmethod
    def load_config(cls):
        cls.global_configuration.set_config()
