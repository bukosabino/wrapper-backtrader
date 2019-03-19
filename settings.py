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
    'strategy': Aberration
}

"""
"slippage_allowed": 0.01,
"take_profit": 0.04,
"stop_loss": 0.02
"""
