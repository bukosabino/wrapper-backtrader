from datetime import datetime

from strategies import (Aberration,
                        AberrationSideway)


CONFIG = {
    'init_date': datetime(2011, 1, 1),
    'end_date': datetime(2013, 12, 31),
    'asset': 'MSFT',
    'data_freq': 'daily',
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
    'strategy': Aberration
}

# TODO: "slippage_allowed": 0.01,
