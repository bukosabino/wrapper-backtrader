import datetime

import backtrader as bt


class Strategy(bt.Strategy):

    def __init__(self):
        # Keep a reference to the "close" line in the data[0] dataseries
        self.dataclose = self.datas[0].close

        # To keep track of pending orders and buy price/commission
        self.order = None
        self.buyprice = None
        self.buycomm = None

        self.orefs = None

    def log(self, txt, dt=None):
        ''' Logging function fot this strategy'''
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))

    def next(self):
        from settings import CONFIG

        # Simply log the closing price of the series from the reference
        if CONFIG['log']:
            self.log('Close, %.2f' % self.dataclose[0])

    def buy(self):
        from settings import CONFIG
        close = self.dataclose[0]

        if CONFIG['take_profit']['enabled'] or CONFIG['stop_loss']['enabled']:

            aux_orefs = []
            limit = 0.005 # TODO: settings
            p1 = close * (1.0 - limit)
            p2 = p1 - CONFIG['stop_loss']['value'] * close
            p3 = p1 + CONFIG['take_profit']['value'] * close

            limdays = 3 # TODO: settings
            limdays2 = 1000 # TODO: settings
            valid1 = datetime.timedelta(limdays)
            valid2 = valid3 = datetime.timedelta(limdays2)

            o1 = super(Strategy, self).buy(exectype=bt.Order.Limit,
                                           price=p1,
                                           valid=valid1,
                                           transmit=False,
                                           size=CONFIG['size'])
            self.log('BUY CREATE, %.2f' % p1)
            aux_orefs.append(o1.ref)

            if CONFIG['stop_loss']['enabled']:
                o2 = super(Strategy, self).sell(exectype=bt.Order.Stop,
                                                price=p2,
                                                valid=valid2,
                                                parent=o1,
                                                transmit=False,
                                                size=CONFIG['size'])
                self.log('STOP LOSS CREATED, %.2f' % p2)
                aux_orefs.append(o2.ref)

            if CONFIG['take_profit']['enabled']:
                o3 = super(Strategy, self).sell(exectype=bt.Order.Limit,
                                                price=p3,
                                                valid=valid3,
                                                parent=o1,
                                                transmit=True,
                                                size=CONFIG['size'])
                self.log('TAKE PROFIT CREATED, %.2f' % p3)
                aux_orefs.append(o3.ref)

            self.orefs = aux_orefs

        else:
            self.log('BUY CREATE, %.2f' % self.dataclose[0])
            self.order = super(Strategy, self).buy(size=CONFIG['size'])

    def sell(self):
        from settings import CONFIG

        if not CONFIG['take_profit']['enabled'] and not CONFIG['stop_loss']['enabled']:
            self.log('SELL CREATE, %.2f' % self.dataclose[0])
            self.order = super(Strategy, self).sell(size=CONFIG['size'])

    def notify_order(self, order):
        from settings import CONFIG

        if order.status in [order.Submitted, order.Accepted]:
            # Buy/Sell order submitted/accepted to/by broker - Nothing to do
            return

        # Check if an order has been completed
        # Attention: broker could reject order if not enougth cash
        if order.status in [order.Completed, order.Canceled, order.Margin]:
            if order.isbuy():
                self.log(
                    'BUY EXECUTED, Price: %.2f, Cost: %.2f, Comm %.2f' %
                    (order.executed.price,
                     order.executed.value,
                     order.executed.comm))

                self.buyprice = order.executed.price
                self.buycomm = order.executed.comm
            else:  # Sell
                self.log('SELL EXECUTED, Price: %.2f, Cost: %.2f, Comm %.2f' %
                         (order.executed.price,
                          order.executed.value,
                          order.executed.comm))

            self.bar_executed = len(self)

        if CONFIG['stop_loss']['enabled'] or CONFIG['take_profit']['enabled']:
            if not order.alive() and order.ref in self.orefs:
                self.orefs = []
        else:
            # Write down: no pending order
            self.order = None

    def notify_trade(self, trade):
        if not trade.isclosed:
            return

        self.log('OPERATION PROFIT, GROSS %.2f, NET %.2f' %
                 (trade.pnl, trade.pnlcomm))
