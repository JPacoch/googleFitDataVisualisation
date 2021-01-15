import pandas as pd

#for col in fit.columns: 
#    print(col) 

class ReadData():
    def gfitDF(self):
        fit = pd.read_csv('data/fit.csv')
        fit = pd.DataFrame(fit)
        return fit