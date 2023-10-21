from Bot.utils.logger import get_logger
import configparser, os


conf = configparser.ConfigParser()
config_file = os.path.join(os.get.cwd(), 'config.ini')
if not os.path.isdir(config_file):
    os.makedirs(config_file)


class Config():
    bot_logger = get_logger("BOT")

    

