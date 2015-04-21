import os
import pandas as pd
import pytest

from lifetimes import plotting
from lifetimes import BetaGeoFitter
from lifetimes.datasets import load_cdnow, load_transaction_data

bgf = BetaGeoFitter()
cd_data = load_cdnow()
bgf.fit(cd_data['frequency'], cd_data['recency'], cd_data['T'], iterative_fitting=0)

@pytest.mark.plottest
@pytest.mark.skipif("DISPLAY" not in os.environ, reason="requires display")
class TestPlotting():
    
    def test_plot_period_transactions(self):
        from matplotlib import pyplot as plt
        
        plotting.plot_period_transactions(bgf)
        
        plotting.plot_period_transactions(bgf, max_frequency=12)
        
        plotting.plot_period_transactions(bgf, label=['A', 'B'])
        plt.show()

    def test_plot_frequency_recency_matrix(self):
        from matplotlib import pyplot as plt

        plt.figure()
        plotting.plot_frequency_recency_matrix(bgf)

        plt.figure()
        plotting.plot_frequency_recency_matrix(bgf, max_recency=100, max_frequency=50)

        plt.show()

    def test_plot_expected_repeat_purchases(self):
        from matplotlib import pyplot as plt

        plt.figure()
        plotting.plot_expected_repeat_purchases(bgf)

        plt.figure()
        plotting.plot_expected_repeat_purchases(bgf, label='test label')

        plt.show()

    def test_plot_customer_alive_history(self):

        transaction_data = load_transaction_data()
        # yes I know this is using the wrong data, but I'm testing plotting here.
        id = 35
        days_since_birth = 200
        sp_trans = transaction_data.ix[transaction_data['id'] == id]
        plot.figure()
        plotting.plot_history_alive(bgf, days_since_birth, sp_trans, 'date')
        plot.show()


