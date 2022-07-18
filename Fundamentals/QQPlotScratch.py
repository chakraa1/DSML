import numpy as np
import pandas as pd
from scipy.special import ndtri # Used to calculate theoretical z values.
import matplotlib.pyplot as plt

"""
# Source - https://www.youtube.com/watch?v=JfnHsWhGRBk
#####################
When to use QQPlot
#####################
To verify if sample data follows Normal distribution
"""

def QQPlotScratchSimple(df,col_name):
    """
    Arranging the data in the sorted form
    """
    df_tmp = df.sort_values(by=[col_name], ascending=True).reset_index(drop=True)
    df_tmp["count"] = df_tmp.index + 1
    n_rows = df_tmp.shape[0]
    df_tmp["percentile_area"] = (df_tmp["count"]) / n_rows
    """
    Calculating theoretical z score
    """
    df_tmp["z_theoretical"] = ndtri(df_tmp["percentile_area"])
    """
    Calculating Actual z score
    """
    df_tmp["z_actual"] = (df_tmp[col_name] - df_tmp[col_name].mean()) / df_tmp[col_name].std()
    """
    Plot Theoretical vs Actual z score and set reference point 
    """
    plt.scatter(df_tmp['z_theoretical'],df_tmp['z_actual'])
    plt.plot([-2, -1, 0, 1, 2], [-2, -1, 0, 1, 2])
    plt.show()

df = pd.DataFrame(np.random.uniform(0, 1, 50), columns=["Points"])
QQPlotScratchSimple(df,"Points")

# https://towardsdatascience.com/understand-q-q-plot-using-simple-python-4f83d5b89f8f