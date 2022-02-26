import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.tsa.api as smt
import pandas as pd
import os
from config import *


def tsplot(y, flag, filename=""):
    """
    This method plot time series (frame wise), AutoCorrelation, as well as apply Dickey–Fuller test
    y - time-series values after image processing
    lags - how many lags to include in AutoCorrelation calculation
    """
    if not isinstance(y, pd.Series):
        y = pd.Series(y)

    with plt.style.context(STYLE):
        plt.figure(figsize=FIGSIZE)
        layout = (2, 2)
        ts_ax = plt.subplot2grid(layout, (0, 0), colspan=2)
        acf_ax = plt.subplot2grid(layout, (1, 0))
        pacf_ax = plt.subplot2grid(layout, (1, 1))

        y.plot(ax=ts_ax)
        p_value = sm.tsa.stattools.adfuller(y)[1]
        ts_ax.set_title('Noise of Gauge Plots\n Dickey-Fuller: p={0:.5f}'.format(p_value))
        smt.graphics.plot_acf(y, ax=acf_ax)
        smt.graphics.plot_pacf(y, ax=pacf_ax)
        plt.tight_layout()
        if flag:
            plt.savefig(os.path.join(ARTIFACT_DIR, filename + '_noise_plot.png'))
