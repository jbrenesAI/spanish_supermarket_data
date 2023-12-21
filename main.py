import yaml
from dotenv import load_dotenv
import os
import logging
import json
from src.supermarket import Supermarket

logger = logging.getLogger()
sh = logging.StreamHandler()
logger.addHandler(sh)
logger.setLevel(logging.DEBUG)


def get_config_path() -> str:
    try:
        config_path = os.getenv("CONFIG_PATH")
    except Exception as e:
        logger.error("Error reading config path")
        logger.error(str(e))
        return None

    logger.info(config_path)
    return config_path


def read_supermarkets_config(config_path: str) -> dict or None:
    try:
        with open(config_path, 'r') as config_stream:
            config = yaml.safe_load(config_stream)
            logger.info(json.dumps(config, indent=2))
    except Exception as e:
        logger.error("Error reading supermarkets configuration")
        logger.error(str(e))
        return None

    return config


if __name__ == "__main__":
    load_dotenv()
    config_path = get_config_path()

    config: dict = read_supermarkets_config(config_path)

    supermarkets = config.get("supermarkets")
    for element in supermarkets:
        supermarket = Supermarket(element)
        # TODO: Implement logic to obtain all supermarket products
        #   Try to implement the max number of tables like products... categories... etc



