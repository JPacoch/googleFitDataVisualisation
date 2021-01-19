import os
from matplotlib import pyplot as plt

class PlotWriter():
    def writePlot(self, plot):
        #for plot in plots:
        plt.savefig('%s.png' % plot)