import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class Parent_lib:
    def __init__(self):
        pass

    class Numpy:
        def find_min(self, df):
            """
            Finds the minimum value in a numpy array.
            """
            return np.min(df)

        def find_max(self, df):
            """
            Finds the maximum value in a numpy array.
            """
            return np.max(df)

    class Pandas:
        def __init__(self):
            print("from Pandas")

    class Sklearn:
        def __init__(self):
            print("from Sklearn")

    class Matplotlib:
        def plot_histogram(self, data):
            """
            Plots a histogram of the given data using Matplotlib.
            """
            plt.hist(data)
            plt.show()

        def plot_line(self, x, y):
            """
            Plots a line graph of the given x and y data using Matplotlib.
            """
            plt.plot(x, y)
            plt.show()


class Child(Parent_lib.Numpy):
    def __init__(self):
        pass
    

# now you can read the file
df = pd.read_csv(r'C:\Users\TOSHIBA\Documents\GitHub\100-Days-of-ML-Code-with-Python\Project\.ipynb_checkpoints\dataset.csv')
arr = df['writing_score'].values
child_instance = Child()
print("Minimum value:", child_instance.find_min(df))
print("Maximum value:", child_instance.find_max(df))
print("Plotting histogram...")
Parent_lib.Matplotlib().plot_histogram(df)
print("Plotting line graph...")
Parent_lib.Matplotlib().plot_line(df, df**2)



