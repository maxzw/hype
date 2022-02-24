from datetime import datetime
import logging

def create_logger(config):
    if config.log:
        dt = datetime.now().strftime("%m-%d-%Y_%H-%M-%S")
        filename = f"./logs/{dt}.txt"
        open(filename, "x").close()
        logging.basicConfig(
                    level=logging.INFO,
                    format='%(asctime)s | %(name)5s | %(levelname)5s | %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S',
                    handlers=[
                        logging.FileHandler(filename),
                        logging.StreamHandler()
                    ])
    else:
        logging.basicConfig(
                    level=logging.INFO,
                    format='%(asctime)s | %(name)5s | %(levelname)8s | %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S'
                    )
    return logging
