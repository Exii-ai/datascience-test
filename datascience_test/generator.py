from datascience_test.data import Data


class Generator:

    def __init__(self):

        self.data = Data()

    def example(self):
        print("We have %s customers" % str(self.data.customers.shape[0]))

