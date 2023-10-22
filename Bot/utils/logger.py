import logging, os
from typing import Union
from datetime import datetime

def get_logger(name: Union[str, None] = "GLOBAL", level: Union[logging.INFO, logging.WARNING, logging.DEBUG] = logging.DEBUG):
    logger = logging.getLogger(name)
    log_file_path = os.path.join(os.getcwd(), "Bot", "log")
    log_file_name = f"log {datetime.now().strftime('%Y-%m-%d %H-%M')}.log"
    if not os.path.exists(log_file_path):
        os.makedirs(log_file_path)
    if os.path.isdir(log_file_path):
        log_file = os.path.join(log_file_path, log_file_name)
    logging.basicConfig(
        filename=log_file,
        filemode= "a",
        level=level,
        format='%(asctime)s - %(levelname)s - %(name)s -   %(message)s',
        datefmt='%m/%d/%Y %H:%M:%S'
    )
    return logger

    
