# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 04:24:10 2019

@author: Gaoxiang
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

q_table = pd.read_pickle('q_table.pickle')
agent = pd.read_pickle('agent.pickle')
obs = pd.read_pickle('observer.pickle')

def show(table):    
    df = pd.DataFrame(np.zeros((9,9)), index = range(9), columns = range(9), dtype = np.float64)

    for state in table.index:
        x = int(list(state)[1])
        y = int(list(state)[4])
        df.loc[x][y] = table.loc['[{0}, {1}]'.format(x, y)].max()
    
    Z = np.zeros((9,9))
    for x in range(9):
        for y in range(9):
            Z[x][y] = df.loc[x, y]

    plt.imshow(Z, interpolation='none', cmap='hot', origin='lower')
    plt.show()
    
show(q_table)
show(agent)
show(obs)