import pandas as pd
file = pd.read_csv(r"C:\Users\vishn\Desktop\DATA SCIENCE PROJECTS\Main project ideas\Ford dataset\X_train.csv")

print(file.head(5))

print(file.isnull().sum())

print(file.describe())

file.info()


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.barplot(X='transmission')
