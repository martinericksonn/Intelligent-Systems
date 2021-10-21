import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt
from constants import GRADES_SET, JOB_PERCENT


# New Antecedent/Consequent objects hold universe variables and membership


# PROGRAMMING
OOP = ctrl.Antecedent(GRADES_SET, 'Object_Oriented_Programming')
PROGRAMMING = ctrl.Antecedent(GRADES_SET, 'PROGRAMMING')
DATA_STRUCT = ctrl.Antecedent(GRADES_SET, 'DATA_STRUCT')
ALGO_ANALYSIS = ctrl.Antecedent(GRADES_SET, 'ALGO_ANALYSIS')

# NETWORK MANAGMENT
NETWORK = ctrl.Antecedent(GRADES_SET, 'NETWORKING')

# DATABASE MANAGEMENTS
IM = ctrl.Antecedent(GRADES_SET, 'INFORMATION_MANAGEMENT')

# COMPUTER ARCHITECTURE
DIGITAL = ctrl.Antecedent(GRADES_SET, 'DIGITAL_LOGIC_DESIGN')
OPERTATING_SYSTEMS = ctrl.Antecedent(GRADES_SET, 'OPERTATING_SYSTEMS')
COMP_ORG = ctrl.Antecedent(GRADES_SET, 'COMP_ORG')

# MATH
DISCRETE_MATH = ctrl.Antecedent(GRADES_SET, 'DISCRETE_MATH')
CALCULUS = ctrl.Antecedent(GRADES_SET, 'CALCULUS')
QM = ctrl.Antecedent(GRADES_SET, 'QUANTITATIVE_METHODS')
CMP = ctrl.Antecedent(GRADES_SET, 'COMPUTING_MATH_PREP')

# OTHERS
WEB_DEV = ctrl.Antecedent(GRADES_SET, 'WEB_DEV')
DVA = ctrl.Antecedent(GRADES_SET, 'DIGITAL_VISUAL_ARTS')
HCI = ctrl.Antecedent(GRADES_SET, 'HUMAN COMPUTER INTERACTION')

# JOBS
PROGRAMMER = ctrl.Consequent(
    JOB_PERCENT, 'SYSTEMS_AND_APPLICATIONS-PROGRAMMER')
SYSTEMS_ANALYST = ctrl.Consequent(JOB_PERCENT, 'SYSTEMS_ANALYST')
DATABASE_ADMIN = ctrl.Consequent(JOB_PERCENT, 'DATABASE_ADMIN')
SOFTWARE_ENGINEER = ctrl.Consequent(JOB_PERCENT, 'SOFTWARE_ENGINEER')
ALGO_ANALYST = ctrl.Consequent(JOB_PERCENT, 'ALGO_ANALYST')
SOFTWARE_SPECIALIST = ctrl.Consequent(JOB_PERCENT, 'SOFTWARE_SPECIALIST')
NETWORK_ADMIN = ctrl.Consequent(JOB_PERCENT, 'NETWORK_ADMIN')
SYSTEM_ADMIN = ctrl.Consequent(JOB_PERCENT, 'SYSTEM_ADMIN')
WEB_DEVELOPER = ctrl.Consequent(JOB_PERCENT, 'WEB_DEVELOPER')
UX_UI_DESIGNER = ctrl.Consequent(JOB_PERCENT, 'UX_UI_DESIGNER')


# Auto-membership function population is possible with .automf(3, 5, or 7)o
# operating_systems.automf(3)
# object_oriented_programming.automf(3)

OPERTATING_SYSTEMS['Best'] = fuzz.trimf(
    OPERTATING_SYSTEMS.universe, [1, 1.5, 1.8])
# operating_systems['Average'] = fuzz.trapmf(
#     operating_systems.universe, [1, 1.5, 1.8, 2.9])


# set = fuzz.interp_membership(
#     np.arange(1.0, 3.1, .1), operating_systems['poor'].mf, .50)
# fuzz.interp_membership(
#     np.arange(1.0, 3.1, .1), operating_systems['average'].mf, .50)
# fuzz.interp_membership(
#     np.arange(1.0, 3.1, .1), operating_systems['good'].mf, .50)


# Custom membership functions can be built interactively with a familiar,
# Pythonic API
PROGRAMMER['low'] = fuzz.trimf(PROGRAMMER.universe, [0, 20, 50])
PROGRAMMER['medium'] = fuzz.trimf(PROGRAMMER.universe, [20, 50, 75])
PROGRAMMER['high'] = fuzz.trimf(PROGRAMMER.universe, [60, 80, 100])

PROGRAMMING.automf(3)
fig, (ax0, ax1, ax2) = plt.subplots(nrows=3, figsize=(8, 9))

ax0.plot(PROGRAMMING, PROGRAMMING['poor'], 'b', linewidth=1.5, label='Bad')
ax0.plot(PROGRAMMING, PROGRAMMING['average'],
         'g', linewidth=1.5, label='Decent')
ax0.plot(PROGRAMMING, PROGRAMMING['good'], 'r', linewidth=1.5, label='Great')
ax0.set_title('Food quality')
ax0.legend()

ax1.plot(DATA_STRUCT,  DATA_STRUCT['poor'], 'b', linewidth=1.5, label='Poor')
ax1.plot(DATA_STRUCT,  DATA_STRUCT['average'],
         'g', linewidth=1.5, label='Acceptable')
ax1.plot(DATA_STRUCT,  DATA_STRUCT['good'],
         'r', linewidth=1.5, label='Amazing')
ax1.set_title('Service quality')
ax1.legend()

ax2.plot(PROGRAMMER, PROGRAMMER['low'], 'b', linewidth=1.5, label='Low')
ax2.plot(PROGRAMMER, PROGRAMMER['medium'], 'g', linewidth=1.5, label='Medium')
ax2.plot(PROGRAMMER, PROGRAMMER['high'], 'r', linewidth=1.5, label='High')
ax2.set_title('Tip amount')
ax2.legend()

for ax in (ax0, ax1, ax2):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

plt.tight_layout()

# Turn off top/right axes
for ax in (ax0, ax1, ax2):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

plt.tight_layout()
xlevel_lo = fuzz.interp_membership(PROGRAMMING, PROGRAMMING['poor'], 2.1)
xlevel_mid = fuzz.interp_membership(PROGRAMMING, PROGRAMMING['average'], 2.1)
xlevel_hi = fuzz.interp_membership(PROGRAMMING, PROGRAMMING['good'], 2.1)

ylevel_lo = fuzz.interp_membership(DATA_STRUCT, DATA_STRUCT['poor'], 1.3)
ylevel_mid = fuzz.interp_membership(DATA_STRUCT, DATA_STRUCT['average'], 1.3)
ylevel_hi = fuzz.interp_membership(DATA_STRUCT, DATA_STRUCT['good'], 1.3)

rule1 = np.fmax(xlevel_lo, ylevel_lo)
activation_lo = np.fmin(rule1, PROGRAMMER['low'])
activation_md = np.fmin(ylevel_mid, PROGRAMMER['medium'])

rule3 = np.fmax(PROGRAMMING['good'], DATA_STRUCT['good'])
activation_hi = np.fmin(rule3, PROGRAMMER['high'])
tip0 = np.zeros_like(PROGRAMMER)

fig, ax0 = plt.subplots(figsize=(8, 3))

ax0.fill_between(PROGRAMMER, tip0, activation_lo, facecolor='b', alpha=0.7)
ax0.plot(PROGRAMMER, PROGRAMMER['low'], 'b', linewidth=0.5, linestyle='--', )
ax0.fill_between(PROGRAMMER, tip0, activation_md, facecolor='g', alpha=0.7)
ax0.plot(PROGRAMMER, PROGRAMMER['medium'], 'g', linewidth=0.5, linestyle='--')
ax0.fill_between(PROGRAMMER, tip0, activation_hi, facecolor='r', alpha=0.7)
ax0.plot(PROGRAMMER, PROGRAMMER['high'], 'r', linewidth=0.5, linestyle='--')
ax0.set_title('Output membership activity')

plt.tight_layout()
# You can see how these look with .
# operating_systems.view()
# object_oriented_programming.view()
plt.show()
