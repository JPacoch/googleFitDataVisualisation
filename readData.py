import pandas as pd

#for col in fit.columns: 
#    print(col) 

class ReadData():
    def gfitDF():
        fit = pd.read_csv('datasets/fit.csv')
        fit = pd.DataFrame(fit)

print(ReadData.gfitDF())