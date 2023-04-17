import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class Parent_lib:
    def __init__(self):
        pass

    class Numpy:
        def find_min(self, arr):
            """
            Finds the minimum value in a numpy array.
            """
            return np.min(arr)

        def find_max(self, arr):
            """
            Finds the maximum value in a numpy array.
            """
            return np.max(arr)

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
    
# Example usage with dataset
df = pd.read_csv('example_data.csv')
arr = df['column_name'].values
child_instance = Child()
print("Minimum value:", child_instance.find_min(arr))
print("Maximum value:", child_instance.find_max(arr))
print("Plotting histogram...")
Parent_lib.Matplotlib().plot_histogram(arr)
print("Plotting line graph...")
Parent_lib.Matplotlib().plot_line(arr, arr**2)




