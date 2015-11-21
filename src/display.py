import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from IPython.display import display

class Dataframe(object): 
    def __init__(self, shots, columns):
        self.shots = shots
        self.columns = columns
        self.shot_df = pd.DataFrame(shots, columns = columns)

    def print_data(self):
        with pd.option_context('display.max_columns', None):
            display(self.shot_df.head())

    def shot_distribution(self):
        sns.set_style('white')
        sns.set_color_codes()
        fig = plt.figure(figsize = (12,11))
        plt.scatter(self.shot_df.LOC_X, self.shot_df.LOC_Y)
        plt.show()
        fig.savefig('shot_distribution.png', dpi = fig.dpi)
