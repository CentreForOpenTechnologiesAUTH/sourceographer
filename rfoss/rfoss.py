####
###
##
# Resilience Framework for OSS (RFOSS)
# Author: Apostolos Kritikos <akritiko@csd.auth.gr>
# Version: 1.0
#
# This source code is part of my PhD thesis, entitled "Open 
# Source Software Engineering" in cooperation with the School of 
# Informatics, Aristotle University of Thessaloniki.
#
# The PhD is happening under the supervision of Prof. Ioannis Stamelos.
#
# This research is co-financed by Greece and the European Union 
# (European Social Fund- ESF) through the Operational Programme 
# "Human Resources Development, Education and Lifelong Learning" 
# in the context of the project "Strengthening Human Resources 
# Research Potential via Doctorate Research" (MIS-5000432), 
# implemented by the State Scholarships Foundation (ΙΚY), Greece.
#
##
###
####

import os
import csv
import pandas as pd
from math import pi
import matplotlib.pyplot as plt
import numpy as np

# Directory of csv files
directory = "./data/"

# Initialize indicators array
indicators = {}

# Iterate over csv files (select only csv files)
for filename in os.listdir(directory):
    if filename.endswith(".csv"): 
        # Directory + filename
        finalfilename = directory+filename
        # Open single csv file for read
        with open(finalfilename, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                key = row[1]
                if key in indicators:
                    # implement your duplicate row handling here
                    pass
                if row[2] != 'Score':
                    indicators[key] = float(row[2])
            # Get project name from filename
            temp = csvfile.name
            temp1 = temp.split("/")
            temp2 = temp1[2].split(".")
            project_name = temp2[0]

            # Calculate Goals       
            g1 = ( indicators[ 'I01' ] + indicators[ 'I02' ] + indicators[ 'I03' ] + indicators[ 'I04' ] ) / 4
            g1_str = str( int( round( g1 * 100 ) ) ) + "%"

            g2 = ( indicators[ 'I05' ] + indicators[ 'I06' ] ) / 2
            g2_str = str( int( round( g2 * 100 ) ) ) + "%"

            g3 = ( indicators[ 'I07' ] + indicators[ 'I08' ] + indicators[ 'I09' ]) / 3
            g3_str = str( int( round( g3 * 100 ) ) ) + "%"

            g4 = indicators[ 'I10' ]
            g4_str = str( int( round( g4 * 100 ) ) ) + "%"

            g5 = ( indicators[ 'I11' ] + indicators[ 'I12' ] + indicators[ 'I13' ] + indicators[ 'I14' ] ) / 4
            g5_str = str( int( round( g5 * 100 ) ) ) + "%"

            g6 = ( indicators[ 'I15' ] + indicators[ 'I16' ] + indicators[ 'I17' ] ) / 3
            g6_str = str( int( round( g6 * 100 ) ) ) + "%"

            g7 = ( indicators[ 'I18' ] + indicators[ 'I19' ] ) / 2
            g7_str = str( int( round( g7 * 100 ) ) ) + "%"

            g8 = ( indicators[ 'I20' ] + indicators[ 'I21' ] ) / 2
            g8_str = str( int( round( g8 * 100 ) ) ) + "%"

            g9 = ( indicators[ 'I22' ] + indicators[ 'I23' ] + indicators[ 'I24' ] + indicators[ 'I25' ] ) / 4
            g9_str = str( int( round( g9 * 100 ) ) ) + "%"

            g10 = ( indicators[ 'I26' ] + indicators[ 'I27' ] + indicators[ 'I28' ] + indicators[ 'I29' ] + indicators[ 'I30' ] ) / 5
            g10_str = str( int( round( g10 * 100 ) ) ) + "%"

            g11 = ( indicators[ 'I31' ] + indicators[ 'I32' ] + indicators[ 'I33' ] + indicators[ 'I34' ] + indicators[ 'I35' ] ) / 5
            g11_str = str( int( round( g11 * 100 ) ) ) + "%"

            g12 = ( indicators[ 'I36' ] + indicators[ 'I37' ] + indicators[ 'I38' ] ) / 3
            g12_str = str( int( round( g12 * 100 ) ) ) + "%"

            # Calculate Dimensions
            d1 = ( g1 + g2 + g3 ) / 3
            d1_str = str( int( round( d1 * 100 ) ) ) + "%"

            d2 = ( g4 + g5 + g6 ) / 3
            d2_str = str( int( round( d2 * 100 ) ) ) + "%"

            d3 = ( g7 + g8 + g9 ) / 3
            d3_str = str( int( round( d3 * 100 ) ) ) + "%"

            d4 = ( g10 + g11 + g12 ) / 3
            d4_str = str( int( round( d4 * 100 ) ) ) + "%"

            # Results

            # Write results to file
            out_filename = "./output/" + project_name + ".txt"
            f = open(out_filename, 'w+')
            f.write("RFOSS Scores:")
            f.write("\n")
            f.write("\n")
            f.write("D1. Source Code: " + d1_str)
            f.write("\n")
            f.write("\n")
            f.write("G01. Architecture: " + g1_str)
            f.write("\nG02. Maintainability: " + g2_str)
            f.write("\nG03. Security & Testing: " + g3_str)
            f.write("\n")
            f.write("\n")
            f.write("D2. Business & Legal: " + d2_str)
            f.write("\n")
            f.write("\n")
            f.write("G04. License: " + g4_str)
            f.write("\nG05. Market: " + g5_str)
            f.write("\nG06. Support: " + g6_str)
            f.write("\n")
            f.write("\n")
            f.write("D3. Integration & Reuse: " + d3_str)
            f.write("\n")
            f.write("\n")
            f.write("G07. Initialization: " + g7_str)
            f.write("\nG08. Dependencies: " + g8_str)
            f.write("\nG09. Reuse: " + g9_str)
            f.write("\n")
            f.write("\n")
            f.write("D4. Social (Community): " + d4_str)
            f.write("\n")
            f.write("\n")
            f.write("G10. Development process & Governance: " + g10_str)
            f.write("\nG11. Developer Base: " + g11_str)
            f.write("\nG12. User Base: " + g12_str)
            f.close()

            # Visualizations

            # Spider chart based on: https://williamhuster.com/radar-chart-in-python/
            rfoss_goals = {
              'Architecture': g1*100,
              'Maintainability': g2*100,
              'Security & Testing': g3*100,
              'License': g4*100,
              'Market': g5*100,
              'Support': g6*100,
              'Initialization': g7*100,
              'Dependencies': g8*100,
              'Reuse': g9*100,
              'Development process & Governance': g10*100,
              'Developer Base': g11*100,
              'User Base': g12*100
            }

            df = pd.DataFrame([rfoss_goals])

            skills = list(df)
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

            series_1_values = df.loc[0] \
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
            out_radar = "./output/" + project_name + "_radar.png"
            plt.savefig(out_radar)
            # Show plot
            #plt.show()


            # Bar chart
            # Clear the plot to start with a blank canvas.
            plt.clf()

            N = 1
            d1_bar = d1
            d2_bar = d2
            d3_bar = d3
            d4_bar = d4

            ind = np.arange(N) 
            width = 0.15       
            plt.bar(ind, d1_bar, width, label='Source Code')
            plt.bar(ind + width, d2_bar, width, label='Business & Legal')
            plt.bar(ind + 2*width, d3_bar, width, label='Integration & Reuse')
            plt.bar(ind + 3*width, d4_bar, width, label='Social')

            plt.ylabel('Scores')
            plt.title('Dimensions')

            #plt.xticks(ind + width / 2, ('D1', 'D2', 'D3', 'D4'))
            plt.legend(loc='best')

            # Save the image
            out_bar = "./output/" + project_name + "_bar.png"
            plt.savefig(out_bar)
            # Show plot
            #plt.show()
    else:
        continue


