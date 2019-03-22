from datetime import datetime

from strategies import *


CONFIG = {
    'mode': 'backtest', # 'backtest', 'optimization', 'walk_forward', 'paper', 'live'
    'plot': True,
    'init_date': datetime(2017, 1, 1),
    'end_date': datetime(2019, 2, 28),
    'asset': 'BTC-USD',
    # TODO: 'data_freq': 'daily',
    'capital_base': 100000.0,
    'commission': 0.002,
    'size': 2,
    'log': False,
    'take_profit': {
        'enabled': False,
        'value': 0.01,
    },
    'stop_loss': {
        'enabled': False,
        'value': 0.02,
    },
    'strategies': [ # One or more strategies to run
        Aberration_RSI
        # Aberration,
        # AberrationSideway,
        # RSI,
    ],
}

# TODO: "slippage_allowed": 0.01,
