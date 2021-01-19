import pandas as pd 

class ParseData():
    def pulseDataAvg(self, data):
        pulse = data[["Data","Średnie tętno (bpm)"]]
        pulse.iloc[:,1] = pulse.iloc[:,1].fillna(0)
        return pulse
    
    def caloriesData(self, data):
        calories = data[["Data","Kalorie (kcal)"]]
        calories.iloc[:,1] = calories.iloc[:,1].fillna(0)
        return calories

    def cardioPoints(self, data):
        cardio = data[["Data","Punkty kardio"]]
        cardio.iloc[:,1] = cardio.iloc[:,1].fillna(0)
        return cardio

    def pulseDataMax(self, data):
        pulseMax = data[["Data","Najwyższe tętno (bpm)"]]
        pulseMax.iloc[:,1] = pulseMax.iloc[:,1].fillna(0)
        return pulseMax

    def pulseDataMin(self,data):
        pulseMin = data[["Data", "Najniższe tętno (bpm)"]]
        pulseMin.iloc[:,1] = pulseMin.iloc[:,1].fillna(0)
        return pulseMin

    def stepCount(self, data):
        count = data[["Data","Liczba kroków"]]
        count.iloc[:,1] = count.iloc[:,1].fillna(0)
        return count

    def minutesMoving(self, data):
        movingTime = data[["Data", "Liczba minut ruchu"]]
        movingTime.iloc[:,1] = movingTime.iloc[:,1].fillna(0)
        return movingTime

    def movingDistance(self,data):
        distance = data[["Data","Odległość (m)"]]
        distance.iloc[:,1] = distance.iloc[:,1].fillna(0)
        return distance