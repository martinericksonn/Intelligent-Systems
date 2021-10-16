import requests
import json
import locale
import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

import const as const
locale.setlocale(locale.LC_ALL, '')

COUNTRY = 'india'

MILLION = 1000000
SAFE = 'safe'
PRECAUTION_NEEDED = 'precaution_needed'
BAD = 'bad'
DANGEROUS = 'dangerous'
GREAT = 'great'
GOOD = 'good'
WORSE = 'worse'
VERY_SLOW = 'very_slow'
SLOW = 'slow'
FAST = 'fast'
VERY_FAST = 'very_fast'
LINE_WIDTH = 1.5
ZERO = 0

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

plot_covid_growth = np.arange(0, 11, 1)
plot_recovered_percent = np.arange(0, 11, 1)
plot_of_safety = np.arange(0, 11, 1)

graph_covid_growth = {
    VERY_SLOW: fuzz.trimf(plot_covid_growth, [0, 0, 2]),
    SLOW: fuzz.trimf(plot_covid_growth, [1, 2, 4]),
    FAST: fuzz.trimf(plot_covid_growth, [3, 5, 6]),
    VERY_FAST: fuzz.trimf(plot_covid_growth, [5, 10, 10])
}

graph_recovered_percent = {
    GREAT: fuzz.trimf(plot_recovered_percent, [0, 0, 3]),
    GOOD: fuzz.trimf(plot_recovered_percent, [1, 3, 5]),
    BAD: fuzz.trimf(plot_recovered_percent, [3, 6, 7]),
    WORSE: fuzz.trimf(plot_recovered_percent, [5, 10, 10])
}

graph_safeness = {
    SAFE: fuzz.trapmf(plot_of_safety, [0, 0, 0, 2]),
    PRECAUTION_NEEDED: fuzz.trapmf(plot_of_safety, [1, 3, 4, 5]),
    BAD: fuzz.trapmf(plot_of_safety, [3, 5, 6, 7]),
    DANGEROUS: fuzz.trapmf(plot_of_safety, [6, 8, 10, 10])
}

fig, (graph1, graph2, graph3) = plt.subplots(nrows=3, figsize=(10, 10))

graph1.plot(plot_covid_growth,
            graph_covid_growth[VERY_SLOW], 'blue', linewidth=LINE_WIDTH, label=VERY_SLOW)
graph1.plot(plot_covid_growth,
            graph_covid_growth[SLOW], 'green', linewidth=LINE_WIDTH, label=SLOW)
graph1.plot(plot_covid_growth,
            graph_covid_growth[FAST], 'violet', linewidth=LINE_WIDTH, label=FAST)
graph1.plot(plot_covid_growth,
            graph_covid_growth[VERY_FAST], 'red', linewidth=LINE_WIDTH, label=VERY_FAST)
graph1.set_title('Covid Growth')


graph2.plot(plot_recovered_percent,
            graph_recovered_percent[GREAT], 'blue', linewidth=LINE_WIDTH, label=GREAT)
graph2.plot(plot_recovered_percent,
            graph_recovered_percent[GOOD], 'green', linewidth=LINE_WIDTH, label=GOOD)
graph2.plot(plot_recovered_percent,
            graph_recovered_percent[BAD], 'violet', linewidth=LINE_WIDTH, label=BAD)
graph2.plot(plot_recovered_percent,
            graph_recovered_percent[WORSE], 'red', linewidth=LINE_WIDTH, label=WORSE)
graph2.set_title('Recovery Gwroth')


graph3.plot(plot_recovered_percent,
            graph_safeness[SAFE], 'blue', linewidth=LINE_WIDTH, label=SAFE)
graph3.plot(plot_recovered_percent,
            graph_safeness[PRECAUTION_NEEDED], 'green', linewidth=LINE_WIDTH, label=PRECAUTION_NEEDED)
graph3.plot(plot_recovered_percent,
            graph_safeness[BAD], 'violet', linewidth=LINE_WIDTH, label=BAD)
graph3.plot(plot_recovered_percent,
            graph_safeness[DANGEROUS], 'red', linewidth=LINE_WIDTH, label=DANGEROUS)
graph3.set_title('Safeness To Visit')

graph1.legend()
graph2.legend()
graph3.legend()


# FUZZYFICATION

fuzzificaton_covid_growth = {
    VERY_SLOW: fuzz.interp_membership(plot_covid_growth,
                                      graph_covid_growth[VERY_SLOW], covid_growth),
    SLOW: fuzz.interp_membership(plot_covid_growth,
                                 graph_covid_growth[SLOW], covid_growth),
    FAST: fuzz.interp_membership(plot_covid_growth,
                                 graph_covid_growth[FAST], covid_growth),
    VERY_FAST: fuzz.interp_membership(plot_covid_growth,
                                      graph_covid_growth[VERY_FAST], covid_growth),
}

fuzzification_recovered_percenth = {
    GREAT: fuzz.interp_membership(plot_recovered_percent,
                                  graph_recovered_percent[GREAT], recovered_percent),
    GOOD: fuzz.interp_membership(plot_covid_growth,
                                 graph_recovered_percent[GOOD], recovered_percent),
    BAD: fuzz.interp_membership(plot_covid_growth,
                                graph_recovered_percent[BAD], recovered_percent),
    WORSE: fuzz.interp_membership(plot_covid_growth,
                                  graph_recovered_percent[WORSE], recovered_percent),
}

# RULES
# 1 if covid Growth is VERY_SLOW slow or recovery VERY_SLOW then safe to visit
# 2 if covi d Growth is  SLOW or recovery SLOW slow then NOT SAFE to visit
# 3 if covid Growth is FAST or recovery growth BAD then BAD to visit
# 4 if covid Growth is very VERY_FAST or recovery growth WORSE then DANGEROUS to visit

rule = {
    1: np.fmax(fuzzificaton_covid_growth[VERY_SLOW], fuzzification_recovered_percenth[GREAT]),
    2: np.fmax(fuzzificaton_covid_growth[SLOW], fuzzification_recovered_percenth[GOOD]),
    3: np.fmax(fuzzificaton_covid_growth[FAST], fuzzification_recovered_percenth[BAD]),
    4: np.fmax(fuzzificaton_covid_growth[VERY_FAST], fuzzification_recovered_percenth[WORSE])
}

rule_activation = {
    ZERO: np.zeros_like(plot_of_safety),
    SAFE: np.fmin(rule[1], graph_safeness[SAFE]),
    PRECAUTION_NEEDED: np.fmin(rule[2], graph_safeness[PRECAUTION_NEEDED]),
    BAD: np.fmin(rule[3], graph_safeness[BAD]),
    DANGEROUS: np.fmin(rule[4], graph_safeness[DANGEROUS]),
}

# Visualize this
fig, graph4 = plt.subplots(figsize=(8, 4))

graph4.fill_between(
    plot_of_safety, rule_activation[ZERO], rule_activation[SAFE], facecolor='b', alpha=0.7)
graph4.plot(plot_of_safety, graph_safeness[SAFE],
            'b', linewidth=0.5, linestyle='--', label=SAFE)
graph4.fill_between(
    plot_of_safety, rule_activation[ZERO], rule_activation[PRECAUTION_NEEDED], facecolor='g', alpha=0.7)
graph4.plot(plot_of_safety,
            graph_safeness[PRECAUTION_NEEDED], 'g', linewidth=0.5, linestyle='--', label=PRECAUTION_NEEDED)
graph4.fill_between(
    plot_of_safety, rule_activation[ZERO], rule_activation[BAD], facecolor='r', alpha=0.7)
graph4.plot(plot_of_safety, graph_safeness[BAD],
            'violet', linewidth=0.5, linestyle='--', label=BAD)
graph4.fill_between(plot_of_safety, rule_activation[ZERO],
                    rule_activation[DANGEROUS], facecolor='violet', alpha=0.7)
graph4.plot(plot_of_safety,
            graph_safeness[DANGEROUS], 'r', linewidth=0.5, linestyle='--', label=DANGEROUS)
graph4.set_title(f'Safeness of Visit to {COUNTRY.upper()}')
graph4.legend()

# Turn off top/right axes
for ax in (graph4,):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()


aggregated = np.fmax(rule_activation[SAFE], np.fmax(
    rule_activation[PRECAUTION_NEEDED], np.fmax(rule_activation[BAD], rule_activation[DANGEROUS])))

safeness = fuzz.defuzz(plot_of_safety, aggregated, 'centroid')
safeness_activation = fuzz.interp_membership(
    plot_of_safety, aggregated, safeness)  # for plot
print(safeness)
print(safeness_activation)
fig, graph5 = plt.subplots(figsize=(8, 3))

graph5.plot(plot_of_safety,
            graph_safeness[SAFE], 'b', linewidth=0.5, linestyle='--', )
graph5.plot(plot_of_safety,
            graph_safeness[PRECAUTION_NEEDED], 'g', linewidth=0.5, linestyle='--')
graph5.plot(plot_of_safety,
            graph_safeness[BAD], 'violet', linewidth=0.5, linestyle='--')
graph5.plot(plot_of_safety,
            graph_safeness[DANGEROUS], 'r', linewidth=0.5, linestyle='--')
graph5.fill_between(
    plot_of_safety, rule_activation[ZERO], aggregated, facecolor='Orange', alpha=0.7)
graph5.plot([safeness, safeness], [0, safeness_activation],
            'k', linewidth=1.5, alpha=0.9)
graph5.set_title('Aggregated membership and result (line)')

# Turn off top/right axes
for ax in (graph5,):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

plt.tight_layout()
plt.show()
