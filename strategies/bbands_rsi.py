import backtrader as bt

from strategy import Strategy


class Aberration_RSI(Strategy):
    """Bollinger Bands Strategy
    """

    params = (
        ('period', 20),
        ('devfactor', 2),
    )

    def __init__(self):
        # Add a BBand indicator
        self.bband = bt.indicators.BBands(self.datas[0],
                                          period=self.params.period,
                                          devfactor=self.params.devfactor)
        self.rsi = bt.indicators.RSI_SMA(self.data.close, period=self.params.period)
        super(Aberration_RSI, self).__init__()

    def next(self):
        super(Aberration_RSI, self).next()

        # Check if an order is pending ... if yes, we cannot send a 2nd one
        if self.order:
            return

        if self.orefs:
            return

        if self.dataclose < self.bband.lines.bot and not self.position and self.rsi < 30:
            self.buy()

        if self.dataclose > self.bband.lines.top and self.position and self.rsi > 70:
            self.sell()

    def stop(self):
        from settings import CONFIG
        pnl = round(self.broker.getvalue() - CONFIG['capital_base'], 2)
        print('Aberration Period: {} Final PnL: {}'.format(
            self.params.period, pnl))
