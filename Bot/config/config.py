from Bot.utils.logger import get_logger
import configparser, os


conf = configparser.ConfigParser()
config_file = os.getcwd()
if not os.path.isdir(config_file):
    os.makedirs(config_file)
config_file = os.path.join(os.getcwd(), 'config.ini')


def create_config():
    conf["Server"] = {}
    conf["Server"]["Name"] = "Your Server Name"
    conf["Server"]["Member_role"] = "ID/Name of Member's Role that will be assigned to new members"

    with open(config_file, "w") as f:
        conf.write(f)


class Config():
    bot_logger = get_logger("BOT")
    try:
        conf.read(config_file)
    except FileNotFoundError:
        create_config()
    
    try:
        server  = conf['Server']
    except KeyError:
        pass
    


    

