# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk("dataset"):
    for filename in filenames:
        print(os.path.join(dirname, filename))

import plotly.graph_objects as go
from plotly.offline import iplot
import folium
from  folium  import  plugins

# Loading the datas
resultsDF = pd.read_csv("dataset\results.csv")
circuitsDF = pd.read_csv("dataset\\circuits.csv")
driversDF = pd.read_csv("dataset\drivers.csv")
racesDF = pd.read_csv("dataset\races.csv")
constructorDF = pd.read_csv("dataset\constructors.csv")

resultsDF.head()

