import pandas as pd 
from readData import ReadData
from parseData import ParseData
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime
from writePlot import PlotWriter

read = ReadData()
dane = read.gfitDF()

googleFit = ParseData()
distance = googleFit.movingDistance(dane)
pulsemax = googleFit.pulseDataMax(dane)
pulsemin = googleFit.pulseDataMin(dane)
pulseavg = googleFit.pulseDataAvg(dane)
calories = googleFit.caloriesData(dane)
cardio = googleFit.cardioPoints(dane)
steps = googleFit.stepCount(dane)
minutes = googleFit.minutesMoving(dane)

sns.set_theme(style="dark")

class VisualiseData():
    def visualiseDistance(self, data):
        timeIndex = data["Data"]
        timeIndexMonth = timeIndex.index[::30]

        ax = sns.lineplot(x="Data", y="Odległość (m)",
             data=data)
        ax.set_title("Dzienna odległość w metrach.")
        plt.xticks(timeIndexMonth, rotation = 60) 
        #ax.savefig("distance.png")
        plt.show()
        
    def visualiseCalories(self, data):
        timeIndex = data["Data"]
        timeIndexMonth = timeIndex.index[::30]

        ax = sns.lineplot(x="Data", y="Kalorie (kcal)",
             data=data)
        ax.set_title("Dzienna ilość spalonych kalorii.")
        plt.xticks(timeIndexMonth, rotation = 60) 
        #ax.savefig("distance.png")
        plt.show()

    def visualiseCardioPoints(self, data):
        timeIndex = data["Data"]
        timeIndexMonth = timeIndex.index[::30]

        ax = sns.lineplot(x="Data", y="Punkty kardio",
             data=data)
        ax.set_title("Dzienna liczba punktów kardio")
        plt.xticks(timeIndexMonth, rotation = 60) 
        #ax.savefig("distance.png")
        plt.show()

    def visualiseSteps(self, data):
        timeIndex = data["Data"]
        timeIndexMonth = timeIndex.index[::30]

        ax = sns.lineplot(x="Data", y="Liczba kroków",
             data=data)
        ax.set_title("Dzienna liczba kroków.")
        plt.xticks(timeIndexMonth, rotation = 60) 
        #ax.savefig("distance.png")
        plt.show()

    def visualiseMinutesMoving(self, data):
        timeIndex = data["Data"]
        timeIndexMonth = timeIndex.index[::30]

        ax = sns.lineplot(x="Data", y="Liczba minut ruchu",
             data=data)
        ax.set_title("Minuty w ruchu dziennie.")
        plt.xticks(timeIndexMonth, rotation = 60) 
        #ax.savefig("distance.png")
        plt.show()

    def visualisePulse(self, pulseavg, pulsemax, pulsemin):
        timeIndex = pulseavg["Data"]
        timeIndexMonth = timeIndex.index[::30]

        fig, ax = plt.subplots()
        ax.plot(pulseavg.iloc[:,1], linewidth = 2, label = 'Średnia')
        ax.plot(pulsemax.iloc[:,1], linewidth = 1, label = 'Max')
        ax.plot(pulsemin.iloc[:,1], linewidth = 1, label = 'Min')
        plt.xticks(timeIndexMonth, rotation = 60)
        ax.legend()
        ax.set_title("Najwyższa, najniższa i średnia wartość tętna.")
        plt.xlim(left = 100)
        plt.show()

    def visualiseMovingCardio(self, movingTime, cardioPoints):
        timeIndex = pulseavg["Data"]
        timeIndexMonth = timeIndex.index[::30]

        fig, ax = plt.subplots()
        ax.plot(movingTime.iloc[:,1], linewidth = 1, label = 'Czas')
        ax.plot(cardioPoints.iloc[:,1], linewidth = 1, label = 'Punkty kardio')
        plt.xticks(timeIndexMonth, rotation = 60)
        ax.legend()
        ax.set_title("Stosunek zdobytych punktów kardio do minut ruchu dziennie.")
        plt.show()

plotter = VisualiseData()
pulsePlot = plotter.visualisePulse(pulseavg, pulsemax, pulsemin)
distancePlot = plotter.visualiseDistance(distance)
caloriesPlot = plotter.visualiseCalories(calories)
cpPlot = plotter.visualiseCardioPoints(cardio)
stepsPlot = plotter.visualiseSteps(steps)
minutesPlot = plotter.visualiseMinutesMoving(minutes)
cpmvPlot = plotter.visualiseMovingCardio(minutes, cardio)

#lista = (pulsePlot, distancePlot)
#print(lista)

#writer = PlotWriter()
#writer.writePlot(pulsePlot)
#writer.writePlot(distancePlot)
#writer.writePlot(caloriesPlot)
#writer.writePlot(cpPlot)
#writer.writePlot(stepsPlot)
#writer.writePlot(minutesPlot)
#writer.writePlot(cpmvPlot)