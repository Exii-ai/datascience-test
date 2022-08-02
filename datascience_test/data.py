import logging
import pandas as pd

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
logger.setLevel(logging.INFO)


class Data:

    BASE_PATH = "data_store/{file}.csv"
    FILES = ["orders", "customers"]

    orders = None
    customers = None

    def __init__(self):
        for file in self.FILES:
            logger.info("Reading %s" % file)
            data = pd.read_csv(self.BASE_PATH.format(file=file))
            setattr(self, file, data)


