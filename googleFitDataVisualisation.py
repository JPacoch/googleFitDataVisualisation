import pandas as pd 
from readData import ReadData
from parseData import ParseData
import seaborn as sns
import matplotlib.pyplot as plt
#fit = pd.read_csv('data/fit.csv')
#fit = pd.DataFrame(fit)

read = ReadData()
dane = read.gfitDF()

googleFit = ParseData()
a = googleFit.movingDistance(dane)
print(a)
sns.set_theme(style="darkgrid")
sns.relplot(x="Data", y="Odległość (m)",
             data=a, kind = "line")
plt.show()  

