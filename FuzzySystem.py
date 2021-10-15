import requests
import json
import locale
import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

import const as const
locale.setlocale(locale.LC_ALL, '')

COUNTRY = 'philippines'
MILLION = 1000000
SAFE = 'safe'
NOT_SAFE = 'not_safe'
BAD = 'bad'
DANGEROUS = 'dangerous'
GREAT = 'great'
GOOD = 'good'
WORSE = 'worse'
VERY_SLOW = 'very_slow'
SLOW = 'slow'
FAST = 'fast'
VERY_FAST = 'very_fast'

url = f"https://covid-193.p.rapidapi.com/statistics?country={COUNTRY}"

headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "a40d7aa2f4msh6a00fe6828f23d5p171ae9jsna21e56f053e1"
}


response = requests.request("GET", url, headers=headers)
data = json.loads(response.text)
active_cases = int(data['response'][0]['cases']['active'])
total_cases = int(data['response'][0]['cases']['total'])
recovered_cases = int(data['response'][0]['cases']['recovered'])
M1_pop = int(data['response'][0]['cases']['1M_pop'])

covid_growth = ((active_cases/total_cases) + (M1_pop/MILLION))*100
recovered_percent = 100 - (recovered_cases/total_cases*100)

if(covid_growth > 10):
    covid_growth = 10

if(recovered_percent > 10):
    recovered_percent = 10

print(f'{COUNTRY} Covid Growth: {covid_growth:n}')
print(f'{COUNTRY} Recovered : {recovered_percent:n}')


degree_covid_growth = np.arange(0, 11, 1)
degree_recovered_percent = np.arange(0, 11, 1)
degree_of_safety = np.arange(0, 11, 1)

fuzzification_covid_growth = {
    VERY_SLOW: fuzz.trimf(degree_covid_growth, [0, 0, 2]),
    SLOW: fuzz.trimf(degree_covid_growth, [1, 2, 4]),
    FAST: fuzz.trimf(degree_covid_growth, [3, 5, 6]),
    VERY_FAST: fuzz.trimf(degree_covid_growth, [5, 10, 10])
}

fuzzification_recovered_percent = {
    GREAT: fuzz.trimf(degree_recovered_percent, [0, 0, 3]),
    GOOD: fuzz.trimf(degree_recovered_percent, [1, 3, 5]),
    BAD: fuzz.trimf(degree_recovered_percent, [3, 6, 7]),
    WORSE: fuzz.trimf(degree_recovered_percent, [5, 10, 10])
}


fuzzification_safeness = {
    SAFE: fuzz.trapmf(degree_of_safety, [0, 0, 0, 2]),
    NOT_SAFE: fuzz.trapmf(degree_of_safety, [1, 3, 4, 5]),
    BAD: fuzz.trapmf(degree_of_safety, [3, 5, 6, 7]),
    DANGEROUS: fuzz.trapmf(degree_of_safety, [6, 8, 10, 10]),
}

fig, (graph1, graph2, graph3) = plt.subplots(nrows=3, figsize=(10, 10))

graph1.plot(degree_covid_growth,
            fuzzification_covid_growth[VERY_SLOW], 'b', linewidth=1.5, label=VERY_SLOW)
graph1.plot(degree_covid_growth,
            fuzzification_covid_growth[SLOW], 'g', linewidth=1.5, label=SLOW)
graph1.plot(degree_covid_growth,
            fuzzification_covid_growth[FAST], 'violet', linewidth=1.5, label=FAST)
graph1.plot(degree_covid_growth,
            fuzzification_covid_growth[VERY_FAST], 'r', linewidth=1.5, label=VERY_FAST)
graph1.set_title('Covid Growth')
graph1.legend()

graph2.plot(degree_recovered_percent,
            fuzzification_recovered_percent[GREAT], 'b', linewidth=1.5, label=GREAT)
graph2.plot(degree_recovered_percent,
            fuzzification_recovered_percent[GOOD], 'g', linewidth=1.5, label=GOOD)
graph2.plot(degree_recovered_percent,
            fuzzification_recovered_percent[BAD], 'violet', linewidth=1.5, label=BAD)
graph2.plot(degree_recovered_percent,
            fuzzification_recovered_percent[WORSE], 'r', linewidth=1.5, label=WORSE)
graph2.set_title('Recovery Gwroth')
graph2.legend()

graph3.plot(degree_recovered_percent,
            fuzzification_safeness[SAFE], 'b', linewidth=1.5, label=SAFE)
graph3.plot(degree_recovered_percent,
            fuzzification_safeness[NOT_SAFE], 'g', linewidth=1.5, label=NOT_SAFE)
graph3.plot(degree_recovered_percent,
            fuzzification_safeness[BAD], 'violet', linewidth=1.5, label=BAD)
graph3.plot(degree_recovered_percent,
            fuzzification_safeness[DANGEROUS], 'r', linewidth=1.5, label=DANGEROUS)
graph3.set_title('Safe To Visit')
graph3.legend()


plt.show()
