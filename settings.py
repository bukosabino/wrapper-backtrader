from datetime import datetime

from strategies import (Aberration,
                        AberrationSideway,
                        RSI)


CONFIG = {
    'mode': 'optimization', # 'backtest', 'optimization', 'walk_forward'
    'plot': True,
    'init_date': datetime(2011, 1, 1),
    'end_date': datetime(2013, 12, 31),
    'asset': 'MSFT', # TODO: cryptocurrencies
    # TODO: 'data_freq': 'daily',
    'capital_base': 100000.0,
    'commission': 0.002,
    'size': 500,
    'log': False,
    'take_profit': {
        'enabled': True,
        'value': 0.01,
    },
    'stop_loss': {
        'enabled': True,
        'value': 0.02,
    },
    'strategies': [ # One or more strategies to run
        #Aberration,
        #AberrationSideway,
        RSI
    ],
}

# TODO: "slippage_allowed": 0.01,
