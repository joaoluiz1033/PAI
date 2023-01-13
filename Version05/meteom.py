from datetime import datetime, timedelta
import json


DB_PATH = 'S:\PAI\database'

class Measure:
    def __init__(self, date, temperature, rain):
        self.date = date
        self.temperature = temperature
        self.rain = rain

    def __repr__(self):
        return f"{self.date}: T={self.temperature} ; R={self.rain}"

def str2date(datestr, format):
    try:
        date = datetime.strptime(datestr, format)
    except ValueError:
        return None
    return date

def readsynopfile(filename):
    measures = []
    # path = f"{DB_PATH}/{filename}"
    # with open(path) as file:
    #     header = file.readline()
    #     for line in file:
    #         data = line.strip().split(";")
    #         date = str2date(data[1], "%Y%m%d%H%M%S")
    #         temperature = float(data[7]) if data[7] != "mq" else 0.0
    #         rain = float(data[39]) if data[39] != "mq" else 0.0
    #         measure = Measure(date, temperature, rain)
    #         measures.append(measure)
    return measures


    
    
    
def loadlistoftowns():
    towns = dict()
    # path = f"{DB_PATH}/postesSynop.json"
    # with open(path) as file:
    #     data = json.load(file)
    #     for line in data["features"]:
    #         townid = line["properties"]["ID"]
    #         name = line["properties"]["Nom"]
    #         towns[name] = townid
    return towns


def finddogdays(data: list[Measure]):
    dogdays = []
    dogday = []
    current_date = data[0].date.date()
    for measure in data:
        if measure.date.date() == current_date:
            dogday.append(measure)
        else:
            tmin = min([measure.temperature for measure in dogday])
            tmax = max([measure.temperature for measure in dogday])
            if tmin >= 293 and tmax >= 303:
                dogdays.append(dogday)
            dogday = []
            dogday.append(measure)
            current_date = measure.date.date()
    return dogdays


def findheatwaves(data):
    dogdays = finddogdays(data)
    heatwaves = []
    heatwave = [dogdays[0]]
    for dogday in dogdays[1:]:
        if dogday[-1].date - heatwave[-1][-1].date <= timedelta(days=1):
            heatwave.append(dogday)
        else:
            if len(heatwave) >= 3:
                heatwaves.append(heatwave)
            heatwave = [dogday]
    return heatwaves


def printdogdays(dogdays):
    for dogday in dogdays:
        date = dogday[0].date.date() 
        temperarures = [measure.temperature for measure in dogday]
        print(date, ":", min(temperarures), max(temperarures))

def printheatwaves(heatwaves):
    for heatwave in heatwaves:
        print(f"{len(heatwave)} jours du {heatwave[0][0].date.date()} au {heatwave[-1][-1].date.date()}")


if __name__ == "__main__":
    date = str2date("19960416060000", "%Y%m%d%H%M%S")
    print(date, date.year, date.month, date.day)
    data = readsynopfile("07149.csv")   # ORLY
    print(len(data))
    print(data[0])
    print(data[-1])
    towns = loadlistoftowns()
    print(towns)
    dogdays = finddogdays(data)
    printdogdays(dogdays)
    heatwaves = findheatwaves(data)
    printheatwaves(heatwaves)
    data = readsynopfile("07110.csv")  # BREST
    dogdays = finddogdays(data)
    printdogdays(dogdays)