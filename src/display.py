import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Arc
from IPython.display import display

class Dataframe(object): 
    def __init__(self, shots, columns):
        self.shots = shots
        self.columns = columns
        self.shot_df = pd.DataFrame(shots, columns = columns)

    def print_data(self):
        with pd.option_context('display.max_columns', None):
            display(self.shot_df.head())

    def basketball_court(self):
        fig = plt.figure(figsize=(12,11))
        self.draw_court(outer_lines=True)
        plt.xlim(-300, 300)
        plt.ylim(-100, 500)
        plt.show()
        fig.savefig('basketball_court.png', dpi=fig.dpi)

    def shot_distribution(self):
        sns.set_style('white')
        sns.set_color_codes()
        fig = plt.figure(figsize=(12,11))
        plt.scatter(self.shot_df.LOC_X, self.shot_df.LOC_Y)
        plt.show()
        fig.savefig('shot_distribution.png', dpi=fig.dpi)

    def draw_court(self, ax=None, color='black', lw=2, outer_lines=False):
        if ax is None:
            ax = plt.gca()

        hoop = Circle((0, 0), radius=7.5, linewidth=lw, color=color, fill=False)
        backboard = Rectangle((-30, -7.5), 60, -1, linewidth=lw, color=color)
        outer_box = Rectangle((-80, -47.5), 160, 190, linewidth=lw, color=color, fill=False)
        inner_box = Rectangle((-60, -47.5), 120, 190, linewidth=lw, color=color, fill=False)

        top_free_throw = Arc((0, 142.5), 120, 120, theta1=0, theta2=180, linewidth=lw, color=color, fill=False)
        bottom_free_throw = Arc((0, 142.5), 120, 120, theta1=180, theta2=0, linewidth=lw, color=color, linestyle='dashed')
        restricted = Arc((0, 0), 80, 80, theta1=0, theta2=180, linewidth=lw, color=color)

        corner_three_a = Rectangle((-220, -47.5), 0, 140, linewidth=lw, color=color)
        corner_three_b = Rectangle((220, -47.5), 0, 140, linewidth=lw, color=color)
        three_arc = Arc((0, 0), 475, 475, theta1=22, theta2=158, linewidth=lw, color=color)

        center_outer_arc = Arc((0, 422.5), 120, 120, theta1=180, theta2=0, linewidth=lw, color=color)
        center_inner_arc = Arc((0, 422.5), 40, 40, theta1=180, theta2=0, linewidth=lw, color=color)
        court_elements = [hoop, backboard, outer_box, inner_box, top_free_throw,
                          bottom_free_throw, restricted, corner_three_a,
                          corner_three_b, three_arc, center_outer_arc,
                          center_inner_arc]

        if outer_lines:
            outer_lines = Rectangle((-250, -47.5), 500, 470, linewidth=lw, color=color, fill=False)
            court_elements.append(outer_lines)

        for element in court_elements:
            ax.add_patch(element)

        return ax
