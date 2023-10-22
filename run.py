from Bot.controller.main import Bot
from dotenv import load_dotenv
import os
env_path = os.getcwd()
load_dotenv(env_path)
if __name__ == '__main__':
    Bot.run(os.getenv("TOKEN"))