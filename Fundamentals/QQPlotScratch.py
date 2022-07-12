import numpy as np
import pandas as pd
from scipy.special import ndtri # Used to calculate theoretical z values.
import matplotlib.pyplot as plt

def QQPlotScratch():
    data_points = np.random.uniform(0, 1, 50)
    df = pd.DataFrame(data_points, columns=["Points"])
    df = df.sort_values(by=["Points"], ascending=True).reset_index(drop=True)
    df["count"] = df.index + 1
    n_rows = df.shape[0]
    df["percentile_area"] = (df["count"]) / n_rows
    df["z_theortical"] = ndtri(df["percentile_area"])
    df["z_actual"] = (df["Points"] - df["Points"].mean()) / df["Points"].std()
    plt.scatter(df['z_theortical'],df['z_actual'])
    plt.plot([-2,-1,0,1,2],[-2,-1,0,1,2])
    plt.show()
QQPlotScratch()