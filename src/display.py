import pandas
import seaborn
from IPython.display import display

class Dataframe(object): 
    def __init__(self, shots, columns):
        self.shots = shots
        self.columns = columns

    def display(self):
        shot_df = pandas.DataFrame(self.shots, columns = self.columns)
        with pandas.option_context('display.max_columns', None):
            display(shot_df.head())
