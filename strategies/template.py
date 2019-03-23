import backtrader as bt

from strategy import Strategy

class StrategyTemplate(Strategy):
    # definición de parámetros necesarios para el indicador
    params = ()

    def __init__(self):
        # llamadas a algún indicador
        super(StrategyTemplate, self).__init__()

    def next(self):

        # lógica a seguir
        if something:
            pass
            # self.buy()
        else:
            pass
            # self.sell()
