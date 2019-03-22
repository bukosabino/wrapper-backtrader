import backtrader.analyzers as btanalyzers

from settings import CONFIG


def run_strategy(cerebro):

    # Print out the starting conditions
    _show_backtest_init(cerebro.broker)

    # Run over everything
    strats = cerebro.run()

    _show_config_settings(CONFIG)

    if CONFIG['mode'] == 'backtest':
        # Print out the final result
        _show_backtest_end(cerebro.broker)
        _show_analyzers_end(strats[0])


def add_analyzers(cerebro):
    cerebro.addanalyzer(btanalyzers.SharpeRatio, _name='sharpe_ratio')
    cerebro.addanalyzer(btanalyzers.SharpeRatio_A, _name='sharpe_ratio_a') # sharpe ratio anualized
    cerebro.addanalyzer(btanalyzers.VWR, _name='vwr') # sharpe ratio with log returns
    cerebro.addanalyzer(btanalyzers.DrawDown, _name='draw_down')
    cerebro.addanalyzer(btanalyzers.Returns, _name='returns')
    cerebro.addanalyzer(btanalyzers.SQN, _name='sqn')
    cerebro.addanalyzer(btanalyzers.TimeDrawDown, _name='time_drawdown')
    cerebro.addanalyzer(btanalyzers.AnnualReturn, _name='annual_return')
    cerebro.addanalyzer(btanalyzers.TradeAnalyzer, _name='trade_analyzer')
    # cerebro.addanalyzer(btanalyzers.Calmar, _name='calmar')
    # cerebro.addanalyzer(btanalyzers.LogReturnsRolling, _name='log_returns_rolling')
    # cerebro.addanalyzer(btanalyzers.PeriodStats, _name='periods_stats')
    # cerebro.addanalyzer(btanalyzers.PyFolio, _name='pyfolio')
    # cerebro.addanalyzer(btanalyzers.Transactions, _name='transactions')
    # cerebro.addanalyzer(btanalyzers.TimeReturn, _name='time_return')
    return cerebro


def _show_config_settings(config):
    print(config)


def _show_backtest_init(broker):
    print('Initial Portfolio Value: %.2f' % broker.getvalue())


def _show_backtest_end(broker):
    print('Final portfolio value: %.2f' % broker.getvalue())
    print('Fund value: ' + str(broker.fundvalue))
    print('Number of orders executed: %.2f' % len(broker.orders))
    # print('Number of positions: %.2f' % len(broker.positions))


def _printTradeAnalysis(analyzer):
    '''
    Function to print the Technical Analysis results in a nice format.
    https://backtest-rookies.com/2017/06/11/using-analyzers-backtrader/
    '''
    # Get the results we are interested in
    total_open = analyzer.total.open
    total_closed = analyzer.total.closed
    total_won = analyzer.won.total
    total_lost = analyzer.lost.total

    # Designate the rows
    h1 = ['Total Open', 'Total Closed', 'Total Won', 'Total Lost']
    r1 = [total_open, total_closed,total_won,total_lost]

    header_length = len(h1)

    # Print the rows
    print_list = [h1, r1]
    row_format ="{:<15}" * (header_length + 1)
    print("Trade Analysis Results:")
    for row in print_list:
        print(row_format.format('', *row))


def _show_analyzers_end(strats):
    print('Sharpe Ratio: ' + str(strats.analyzers.sharpe_ratio.get_analysis()))
    print('Sharpe Ratio Annualized: ' + str(strats.analyzers.sharpe_ratio_a.get_analysis())) # sharpe ratio anualized
    #print('Sharpe Ratio Log Returns: ' + str(strats.analyzers.vwr.get_analysis())) # sharpe ratio with log returns
    print('Draw Down: ' + str(strats.analyzers.draw_down.get_analysis()))
    print('Returns: ' + str(strats.analyzers.returns.get_analysis()))
    print('SQN: ' + str(strats.analyzers.sqn.get_analysis()))
    print('Time Drawdown: ' + str(strats.analyzers.time_drawdown.get_analysis()))
    print('Annual Return: ' + str(strats.analyzers.annual_return.get_analysis()))
    # print('TradeAnalyzer: ' + str(strats.analyzers.trade_analyzer.get_analysis()))
    _printTradeAnalysis(strats.analyzers.trade_analyzer.get_analysis())

    # print('Calmar: ' + str(strats.analyzers.calmar.get_analysis()))
    # print('Log Returns Rolling: ' + str(strats.analyzers.log_returns_rolling.get_analysis()))
    # print('Periods Stats: ' + str(strats.analyzers.periods_stats.get_analysis()))
    # print('PyFolio: ' + str(strats.analyzers.pyfolio.get_analysis()))

    # print('Transactions: ' + str(strats.analyzers.transactions.get_analysis()))
    # print('Time Return: ' + str(strats.analyzers.time_return.get_analysis()))
