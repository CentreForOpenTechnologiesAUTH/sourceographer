import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import logging
from math import pi
from datetime import datetime


logging.basicConfig(filename="actions.log", level=logging.INFO)

logging.info('Generating output data @ {0}.'.format(datetime.now()))

df = pd.read_csv('indicators.csv', delimiter = ',')


#Source Code Dimension
#Architecture Goal

robustness = df['Robustness'].iloc[0] / 5
scalability = df['Scalability'].iloc[0] / 5
usability = df['Usability'].iloc[0] / 5
effectiveness = df['Effectiveness'].iloc[0] / 100

architecture = round(np.average([robustness, scalability, usability, effectiveness]), 2)

#Maintainability Goal

corrections = df['Corrections'].iloc[0] / 5
improvements = df['Improvements'].iloc[0] / 5

maintainability = round(np.average([corrections, improvements]), 2)

#Security & Testing Goal

security = df['Security'].iloc[0] / 5
testing_process = df['Testing process'].iloc[0]
coverage = df['Coverage'].iloc[0] / 100

security_testing = round(np.average([security, testing_process, coverage]), 2)

#Dimension calc
D_source_code = round(np.average([architecture, maintainability, security_testing]), 2)


#Business & Legal Dimension
#License Goal

license_of_code = df['License type'].iloc[0] / 5

license_goal = license_of_code

#Market Goal

dual_license = df['Dual licensing'].iloc[0]
commercial_resources = df['Commercial resources'].iloc[0]
commercial_training = df['Commercial training'].iloc[0]
industry_adoption = df['Industry adoption'].iloc[0]

market = round(np.average([dual_license, commercial_resources, commercial_training, industry_adoption]), 2)

#Support Goal

non_profit = df['Non profit / Foundation support'].iloc[0]
for_profit = df['For profit company support'].iloc[0]
donations = df['Donations'].iloc[0]

support = round(np.average([non_profit, for_profit, donations]), 2)

#Dimension calc
D_business_legal = round(np.average([license_goal, market, support]), 2)


#Integration & Reuse Dimension
#Initialization Goal

installability = df['Installability'].iloc[0] / 5
configurability = df['Configurability'].iloc[0] / 5

initialization = round(np.average([installability, configurability]), 2)

#Dependencies Goal

dependability = df['Dependability'].iloc[0] / 5
resource_util = df['Resource Utilization'].iloc[0] / 5

dependencies = round(np.average([dependability, resource_util]), 2)

#Reuse Goal

if df['Complexity'].iloc[0] <= 10:
    complexity = 1
elif df['Complexity'].iloc[0] <= 15:
    complexity = 0.8
elif df['Complexity'].iloc[0] <= 20:
    complexity = 0.6
elif df['Complexity'].iloc[0] <= 50:
    complexity = 0.4
else:
    complexity = 0.2

modularity = df['Modularity'].iloc[0] / 5
instability = 1 - df['Instability'].iloc[0]

if df['noc'].iloc[0] <= 100:
    if df['Cohesion'].iloc[0] < 1:
        cohesion = 1
    elif df['Cohesion'].iloc[0] <= 25:
        cohesion = 0.67
    else:
        cohesion = 0.33
elif df['noc'].iloc[0] > 100:
    if df['Cohesion'].iloc[0] < 1:
        cohesion = 1
    elif df['Cohesion'].iloc[0] <= 20:
        cohesion = 0.67
    else:
        cohesion = 0.33

reuse = round(np.average([complexity, modularity, instability, cohesion]), 2)

#Dimension calc
D_integration_reuse = round(np.average([initialization, dependencies, reuse]), 2)


#Social (Community) Dimension
#Development Process & Governance Goal

governance_model = df['Governance model'].iloc[0]
roadmap = df['Project road-map'].iloc[0]
code_of_conduct = df['Code of conduct'].iloc[0]
coding_standards = df['Coding standards'].iloc[0]
documentation_standards = df['Documentation standards'].iloc[0]

development_governance = round(np.average([governance_model, roadmap, code_of_conduct,
    coding_standards, documentation_standards]), 2)

#Developer Base Goal

devs_attracted = df['Developers Attracted'].iloc[0] / 100
active_devs = df['Active Developers'].iloc[0] / 100
num_of_open_issues = 1 - (df['Number of open issues'].iloc[0] / 100)
open_closed_issues = df['Open / Closed issues'].iloc[0] / 100
documentation = df['Documentation'].iloc[0] / 100

developer_base = round(np.average([devs_attracted, active_devs, num_of_open_issues,
    open_closed_issues, documentation]), 2)

#User Base Goal

localization = df['Localization process'].iloc[0]
issue_tracking_activity = df['Issue tracking activity'].iloc[0] / 100
user_guide = df['User guide'].iloc[0] / 5

user_base = round(np.average([localization, issue_tracking_activity, user_guide]), 2)

#Dimension calc
D_social = round(np.average([development_governance, developer_base, user_base]), 2)


#Writing the results to .txt file
out_filename = "./output/output.txt"
f = open(out_filename, 'w+')
f.write("RFOSS Scores:")
f.write("\n")
f.write("\n")
f.write("D1. Source Code: " + str(D_source_code * 100) + "%")
f.write("\n")
f.write("\n")
f.write("G01. Architecture: " + str(architecture * 100) + "%")
f.write("\nG02. Maintainability: " + str(maintainability * 100) + "%")
f.write("\nG03. Security & Testing: " + str(security_testing * 100) + "%")
f.write("\n")
f.write("\n")
f.write("D2. Business & Legal: " + str(D_business_legal * 100) + "%")
f.write("\n")
f.write("\n")
f.write("G04. License: " + str(license_goal * 100) + "%")
f.write("\nG05. Market: " + str(market * 100) + "%")
f.write("\nG06. Support: " + str(support * 100) + "%")
f.write("\n")
f.write("\n")
f.write("D3. Integration & Reuse: " + str(D_integration_reuse * 100) + "%")
f.write("\n")
f.write("\n")
f.write("G07. Initialization: " + str(initialization * 100) + "%")
f.write("\nG08. Dependencies: " + str(dependencies * 100) + "%")
f.write("\nG09. Reuse: " + str(reuse * 100) + "%")
f.write("\n")
f.write("\n")
f.write("D4. Social (Community): " + str(D_social * 100) + "%")
f.write("\n")
f.write("\n")
f.write("G10. Development process & Governance: " + str(development_governance * 100) + "%")
f.write("\nG11. Developer Base: " + str(developer_base * 100) + "%")
f.write("\nG12. User Base: " + str(user_base * 100) + "%")
f.close()


#Visualizations

#Spider chart
rfoss_goals = {
    'Architecture': architecture*100,
    'Maintainability': maintainability*100,
    'Security & Testing': security_testing*100,
    'License': license_goal*100,
    'Market': market*100,
    'Support': support*100,
    'Initialization': initialization*100,
    'Dependencies': dependencies*100,
    'Reuse': reuse*100,
    'Development process & Governance': development_governance*100,
    'Developer Base': developer_base*100,
    'User Base': user_base*100
}

spdr_df = pd.DataFrame([rfoss_goals])

skills = list(spdr_df)
num_skills = len(skills)

angles = [i / float(num_skills) * 2 * pi for i in range(num_skills)]
angles += angles[:1]  # repeat the first value to close the circle

GRAY = '#999999'

# Clear the plot to start with a blank canvas.
plt.clf()

# Create subplots for each data series
series_1 = plt.subplot(1, 1, 1, polar=True)

# Draw one x-axis per variable and add labels
plt.xticks(angles, skills, color=GRAY, size=8)

# Draw the y-axis labels. To keep the graph uncluttered,
# include lines and labels at only a few values.
plt.yticks(
    [20, 40, 60, 80],
    ['20', '40', '60', '80'],
    color=GRAY,
    size=7
)

# Constrain y axis to range 0-100
plt.ylim(0,100)

series_1_values = spdr_df.loc[0] \
                    .values \
                    .flatten() \
                    .tolist()
series_1_values += series_1_values[:1]  # duplicate first element to close the circle

# Set up colors
ORANGE = '#FD7120'
BLUE = '#00BFFF'

# Plot the first series
series_1.set_rlabel_position(0)
series_1.plot(
    angles,
    series_1_values,
    color=ORANGE,
    linestyle='solid',
    linewidth=1,
)
series_1.fill(
    angles,
    series_1_values,
    color=ORANGE,
    alpha=0.6
)

# Save the image
out_radar = "./output/output_radar.png"
plt.savefig(out_radar)


# Bar chart
# Clear the plot to start with a blank canvas.
plt.clf()

N = 1
d1_bar = D_source_code
d2_bar = D_business_legal
d3_bar = D_integration_reuse
d4_bar = D_social

ind = np.arange(N) 
width = 0.15       
plt.bar(ind, d1_bar, width, label='Source Code')
plt.bar(ind + width, d2_bar, width, label='Business & Legal')
plt.bar(ind + 2*width, d3_bar, width, label='Integration & Reuse')
plt.bar(ind + 3*width, d4_bar, width, label='Social')

plt.ylabel('Scores')
plt.title('Dimensions')

plt.legend(loc='best')

# Save the image
out_bar = "./output/output_bar.png"
plt.savefig(out_bar)

logging.info('Generating output data complete @ {0}.'.format(datetime.now()))
