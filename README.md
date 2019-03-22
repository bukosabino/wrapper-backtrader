# Backtrader Wrapper

It is a personal Backtrader wrapper to implement trading strategies.

Also, you can find some example strategies implemented.

# How to use (python 3.7)

```sh
$ git clone https://github.com/bukosabino/wrapper-backtrader.git
$ cd wrapper-backtrader
$ virtualenv -p python3.7 env
$ source env/bin/activate
$ pip install -r requirements.txt
$ python run.py
```

# Advanced use

You can modify the `settings.py` file to run strategies with different
configurations.

You can program your own strategy on a new file in `strategies` folder.
After, you would need import the name strategy on the parameter 'strategy' in
settings.CONFIG.


# TODO:

* Documentation for settings
* Improve 'optimization' mode: https://backtest-rookies.com/2017/06/26/optimize-strategies-backtrader/ (code 3)
* ML strategy utils
* 'walk_forward' mode utils
* Communication module with Darwinex: https://github.com/darwinex/dwx-zeromq-connector/
* Communication module with IB
* PyMC3 strategy utils
* Implement Sortino Ratio like a new analyzer on Backtrader: https://backtest-rookies.com/2017/11/08/backtrader-creating-analyzers/
* pep8 linter(flake8)
* codecov

# DONE:

* Abstract strategy/settings definition
* Output
* Mode Backtest / Optimization
* Some example strategies
