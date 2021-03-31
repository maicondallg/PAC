from ...utils.rule import Rule
from ...utils.validation import checks_data


class Apriori(object):
    def __init__(self, min_sup, min_conf, absolute=False):
        self.min_sup = min_sup
        self.min_conf = min_conf
        self.min_sup_absolute = min_sup
        self.min_conf_absolute = min_conf
        self.absolute = absolute

    def __add_rule(self, rule: Rule):
        pass

    def __def_sup_conf(self, X):
        # Convert absolute sup and conf in relative
        if self.absolute:
            self.min_sup = self.absolute / X.shape[0]
            self.min_conf = self.absolute / X.shape[0]

        else:
            self.min_sup_absolute = self.min_sup * X.shape[0]
            self.min_conf_absolute = self.min_conf * X.shape[0]

    def fit(self, X, y):
        checks_data(X, y)
        self.__def_sup_conf(X)








