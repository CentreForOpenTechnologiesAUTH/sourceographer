####
###
##
#
# Open Source Software Resilience Framework (OSSRF)
# Authors: Apostolos Kritikos <akritiko@csd.auth.gr>, Prodromos Polychroniadis <propol@csd.auth.gr>
# Version: 2.0
#
# This source code is part of my PhD thesis, entitled "Open 
# Source Software Engineering" in cooperation with the Informatics 
# Department of the Aristotle University of Thessaloniki.
#
# The PhD is happening under the supervision of Prof. Ioannis Stamelos.
#
# This research is co-financed by Greece and the European Union 
# (European Social Fund- ESF) through the Operational Programme 
# «Human Resources Development, Education and Lifelong Learning» 
# in the context of the project “Strengthening Human Resources 
# Research Potential via Doctorate Research” (MIS-5000432), 
# implemented by the State Scholarships Foundation (ΙΚY).
#
##
###
####

import os
import re
import sys
import csv
import json
import pandas as pd
from math import pi
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import logging
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from github import Github

githubToken = '' # //XXX: Global variable. Should be changed to a non global variable logic

def callGUI(df, index):
    """ callGUI() calls GUI to get user generated variables (18 OSSRF indicators). """
    global githubToken
    
    logging.basicConfig(filename="actions.log", level=logging.INFO)
    logging.info('GUI initiated @ {0}.'.format(datetime.now()))

    window = Tk()
    window.title("Sourceographer")
    window.geometry('650x600')
    window.configure(background = "white")

    access_token = Label(window ,text = "Github Access Token").grid(row = 0,column = 0)
    access_token_text = Entry(window)
    access_token_text.grid(row = 0, column = 1)

    effectiveness = Label(window ,text = "Effectiveness").grid(row = 1,column = 0)
    effectiveness_text = Entry(window)
    effectiveness_text.grid(row = 1, column = 1)

    testing = Label(window ,text = "Testing process").grid(row = 2,column = 0)
    testing_var = IntVar()
    testing_R1 = Radiobutton(window, text="True", variable=testing_var, value=1).grid(row = 2, column = 1)
    testing_R2 = Radiobutton(window, text="False", variable=testing_var, value=0).grid(row = 2, column = 2)

    coverage = Label(window ,text = "Coverage").grid(row = 3,column = 0)
    coverage_text = Entry(window)
    coverage_text.grid(row = 3, column = 1)

    licensing = Label(window ,text = "Licensing").grid(row = 4,column = 0)
    licensing_var = IntVar()
    licensing_R1 = Radiobutton(window, text="1", variable=licensing_var, value=1).grid(row = 4, column = 1)
    licensing_R2 = Radiobutton(window, text="2", variable=licensing_var, value=2).grid(row = 4, column = 2)
    licensing_R3 = Radiobutton(window, text="3", variable=licensing_var, value=3).grid(row = 4, column = 3)
    licensing_R4 = Radiobutton(window, text="4", variable=licensing_var, value=4).grid(row = 4, column = 4)
    licensing_R5 = Radiobutton(window, text="5", variable=licensing_var, value=5).grid(row = 4, column = 5)

    dual_licensing = Label(window ,text = "Dual licensing").grid(row = 5,column = 0)
    dual_var = IntVar()
    dual_R1 = Radiobutton(window, text="True", variable=dual_var, value=1).grid(row = 5, column = 1)
    dual_R2 = Radiobutton(window, text="False", variable=dual_var, value=0).grid(row = 5, column = 2)

    comm_res = Label(window ,text = "Commercial resources").grid(row = 6,column = 0)
    res_var = IntVar()
    res_R1 = Radiobutton(window, text="True", variable=res_var, value=1).grid(row = 6, column = 1)
    res_R2 = Radiobutton(window, text="False", variable=res_var, value=0).grid(row = 6, column = 2)

    comm_training = Label(window ,text = "Commercial training").grid(row = 7,column = 0)
    training_var = IntVar()
    training_R1 = Radiobutton(window, text="True", variable=training_var, value=1).grid(row = 7, column = 1)
    training_R2 = Radiobutton(window, text="False", variable=training_var, value=0).grid(row = 7, column = 2)

    industry_adoption = Label(window ,text = "Industry adoption").grid(row = 8,column = 0)
    adoption_var = IntVar()
    adoption_R1 = Radiobutton(window, text="True", variable=adoption_var, value=1).grid(row = 8, column = 1)
    adoption_R2 = Radiobutton(window, text="False", variable=adoption_var, value=0).grid(row = 8, column = 2)

    non_profit = Label(window ,text = "Non profit support").grid(row = 9,column = 0)
    non_var = IntVar()
    non_R1 = Radiobutton(window, text="True", variable=non_var, value=1).grid(row = 9, column = 1)
    non_R2 = Radiobutton(window, text="False", variable=non_var, value=0).grid(row = 9, column = 2)

    for_profit = Label(window ,text = "For profit support").grid(row = 10,column = 0)
    for_var = IntVar()
    for_R1 = Radiobutton(window, text="True", variable=for_var, value=1).grid(row = 10, column = 1)
    for_R2 = Radiobutton(window, text="False", variable=for_var, value=0).grid(row = 10, column = 2)

    donations = Label(window ,text = "Donations").grid(row = 11,column = 0)
    donations_var = IntVar()
    donations_R1 = Radiobutton(window, text="True", variable=donations_var, value=1).grid(row = 11, column = 1)
    donations_R2 = Radiobutton(window, text="False", variable=donations_var, value=0).grid(row = 11, column = 2)

    governance = Label(window ,text = "Governance Model").grid(row = 12,column = 0)
    gov_var = IntVar()
    gov_R1 = Radiobutton(window, text="True", variable=gov_var, value=1).grid(row = 12, column = 1)
    gov_R2 = Radiobutton(window, text="False", variable=gov_var, value=0).grid(row = 12, column = 2)

    roadmap = Label(window ,text = "Project Road-map").grid(row = 13,column = 0)
    roadmap_var = IntVar()
    roadmap_R1 = Radiobutton(window, text="True", variable=roadmap_var, value=1).grid(row = 13, column = 1)
    roadmap_R2 = Radiobutton(window, text="False", variable=roadmap_var, value=0).grid(row = 13, column = 2)

    coc = Label(window ,text = "Code of Conduct").grid(row = 14,column = 0)
    coc_var = IntVar()
    coc_R1 = Radiobutton(window, text="True", variable=coc_var, value=1).grid(row = 14, column = 1)
    coc_R2 = Radiobutton(window, text="False", variable=coc_var, value=0).grid(row = 14, column = 2)

    coding_standards = Label(window ,text = "Coding standards").grid(row = 15,column = 0)
    coding_var = IntVar()
    coding_R1 = Radiobutton(window, text="True", variable=coding_var, value=1).grid(row = 15, column = 1)
    coding_R2 = Radiobutton(window, text="False", variable=coding_var, value=0).grid(row = 15, column = 2)

    documentation_standards = Label(window ,text = "Documentation standards").grid(row = 16,column = 0)
    doc_var = IntVar()
    doc_R1 = Radiobutton(window, text="True", variable=doc_var, value=1).grid(row = 16, column = 1)
    doc_R2 = Radiobutton(window, text="False", variable=doc_var, value=0).grid(row = 16, column = 2)

    localization = Label(window ,text = "Localization process").grid(row = 17,column = 0)
    loc_var = IntVar()
    loc_R1 = Radiobutton(window, text="True", variable=loc_var, value=1).grid(row = 17, column = 1)
    loc_R2 = Radiobutton(window, text="False", variable=loc_var, value=0).grid(row = 17, column = 2)

    user_guide = Label(window ,text = "User guide").grid(row = 18,column = 0)
    guide_var = IntVar()
    guide_R1 = Radiobutton(window, text="1", variable=guide_var, value=1).grid(row = 18, column = 1)
    guide_R2 = Radiobutton(window, text="2", variable=guide_var, value=2).grid(row = 18, column = 2)
    guide_R3 = Radiobutton(window, text="3", variable=guide_var, value=3).grid(row = 18, column = 3)
    guide_R4 = Radiobutton(window, text="4", variable=guide_var, value=4).grid(row = 18, column = 4)
    guide_R5 = Radiobutton(window, text="5", variable=guide_var, value=5).grid(row = 18, column = 5)

    repo_author = Label(window ,text = "Repository name in author/repo format").grid(row = 19,column = 0)
    repo_author_text = Entry(window)
    repo_author_text.grid(row = 19, column = 1)

    tag = Label(window ,text = "Version (repo specific tag name)").grid(row = 20,column = 0)
    tag_text = Entry(window)
    tag_text.grid(row = 20, column = 1)

    url = Label(window ,text = "Repository URL").grid(row = 21,column = 0)
    url_text = Entry(window)
    url_text.grid(row = 21, column = 1)

    start_d = Label(window ,text = "Version starting date (YYYY-MM-DD)").grid(row = 22,column = 0)
    start_d_text = Entry(window)
    start_d_text.grid(row = 22, column = 1)

    end_d = Label(window ,text = "Version ending date (YYYY-MM-DD)").grid(row = 23,column = 0)
    end_d_text = Entry(window)
    end_d_text.grid(row = 23, column = 1)

    def submit():
        """ submit function stores the GUI variables """
        global githubToken

        githubToken = access_token_text.get()
        df.at[index,'i4_effectiveness'] = float(effectiveness_text.get()) 
        df.at[index,'i8_testing_process'] = testing_var.get()
        df.at[index,'i9_coverage'] = float(coverage_text.get()) / 100
        df.at[index,'i10_license_type'] = float(licensing_var.get()) / 5
        df.at[index,'i11_dual_licensing'] = dual_var.get()
        df.at[index,'i12_commercial_resources'] = res_var.get()
        df.at[index,'i13_commercial_training'] = training_var.get()
        df.at[index,'i14_industry_adoption'] = adoption_var.get()
        df.at[index,'i15_ngo_support'] = non_var.get()
        df.at[index,'i16_corporate_support'] = for_var.get()
        df.at[index,'i17_donations'] = donations_var.get()
        df.at[index,'i26_governance_model'] = gov_var.get()
        df.at[index,'i27_project_road_map'] = roadmap_var.get()
        df.at[index,'i28_code_of_conduct'] = coc_var.get()
        df.at[index,'i29_coding_standards'] = coding_var.get()
        df.at[index,'i30_documentation_standards'] = doc_var.get()
        df.at[index,'i36_localization_process'] = loc_var.get()
        df.at[index,'i38_user_guide'] = float(guide_var.get()) / 5

        messagebox.showinfo('Message', 'Metrics submitted. Exiting to continue.')
        logging.info('GUI exit @ {0}.'.format(datetime.now()))
        window.destroy()

    btn = ttk.Button(window ,text="Submit", command=submit)
    btn.grid(row=23,column=2)    
    window.mainloop()


def get_devs(df, index, d_start, d_end, g_repo, g):
    """ Github function """
    rate_limit = g.get_rate_limit()
    rate = rate_limit.search
    if rate.remaining == 0:
        print(f'You have 0/{rate.limit} API calls remaining. Reset time: {rate.reset}')
    else:
        print(f'You have {rate.remaining}/{rate.limit} API calls remaining')

    repo = g.get_repo(g_repo)
    
    contributors = repo.get_contributors()

    pages = contributors.totalCount

    active_devs_counter = 0
    new_devs_counter = 0
    all_time_active_devs = 0
    all_time_devs = pages

    for i in range(0, pages):        
        overall_commits = repo.get_commits(until=d_end, author=contributors[i].login)

        overall_comms_pages = overall_commits.totalCount #overall contributions
        
        if overall_comms_pages >= 30:
            all_time_active_devs = all_time_active_devs + 1

        specific_commits = repo.get_commits(since=d_start, until=d_end, 
            author=contributors[i].login) #date specific contributions
        specific_comm_pages = specific_commits.totalCount

        if specific_comm_pages == 0:
            continue
        elif specific_comm_pages == overall_comms_pages and specific_comm_pages < 30:
            new_devs_counter = new_devs_counter + 1
        else:
            active_devs_counter = active_devs_counter + 1
    
    print("new devs: ", new_devs_counter)
    print("active devs:", active_devs_counter)
    print("all time devs: ", all_time_devs)
    print("all time active devs: ", all_time_active_devs)

    devs_attracted = round(new_devs_counter / all_time_devs) 
    active_devs = round(active_devs_counter / all_time_active_devs)

    df.at[index,'i31_devs_attracted'] = devs_attracted
    df.at[index,'i32_devs_active'] = active_devs
    
    print("Developers Attracted: ", devs_attracted, "%")
    print("Active Developers: ", active_devs, "%")


def get_issues(df, index, d_start, d_end, g_repo, g):
    """ Github function """
    rate_limit = g.get_rate_limit()
    rate = rate_limit.search
    if rate.remaining == 0:
        print(f'You have 0/{rate.limit} API calls remaining. Reset time: {rate.reset}')
    else:
        print(f'You have {rate.remaining}/{rate.limit} API calls remaining')

    repo = g.get_repo(g_repo)
    
    issues_all = repo.get_issues(state="all")
    pages = issues_all.totalCount
    
    open_issues_version_counter = 0
    opened_issues_beginningToVersion_counter = 0
    closed_issues_version_counter = 0

    for i in range(0, pages):
        if(issues_all[i].created_at >= d_start and issues_all[i].created_at <= d_end):
            open_issues_version_counter = open_issues_version_counter + 1
        
        if(issues_all[i].created_at <= d_end):
            opened_issues_beginningToVersion_counter = opened_issues_beginningToVersion_counter + 1
        
        if(issues_all[i].created_at >= d_start and issues_all[i].created_at <= d_end and 
         issues_all[i].state=='open'):
            closed_issues_version_counter = open_issues_version_counter - 1
    
    print("Opened issues(version): ", open_issues_version_counter)
    print("Opened issues(beginning-version): ", opened_issues_beginningToVersion_counter)
    print("Closed issues(version): ", closed_issues_version_counter)

    no_of_open_issues = round(1 - (open_issues_version_counter / opened_issues_beginningToVersion_counter))
    open_closed_issues = round(closed_issues_version_counter / open_issues_version_counter)
    issue_tracking_activity = round(open_issues_version_counter / opened_issues_beginningToVersion_counter)

    df.at[index,'i33_nof_open_issues'] = no_of_open_issues
    df.at[index,'i34_open_vs_closed_issues'] = open_closed_issues
    df.at[index,'i37_issue_tracking'] = issue_tracking_activity
    
    print("Number of Open Issues: ", no_of_open_issues, "%")
    print("Open/Closed Issues: ", open_closed_issues, "%")
    print("Issue Tracking Activity: ", issue_tracking_activity, "%")

def phpmetrics_export(df, index, filename):
    """ PHPMETRICS function """
    phpmetrics = [
        ["Lines of code", "LOC", ""],
        ["Logical lines of code", "LOC", ""],
        ["Comment lines of code", "LOC", ""],  
        ["Average volume", "LOC", ""],
        ["Average comment weight", "LOC", ""],
        ["Average intelligent content", "LOC", ""],
        ["Logical lines of code by class", "LOC", ""],
        ["Logical lines of code by method", "LOC", ""],
        ["Classes", "Object oriented programming", ""],
        ["Interface", "Object oriented programming", ""],
        ["Methods", "Object oriented programming", ""],
        ["Methods by class", "Object oriented programming", ""],
        ["Lack of cohesion of methods", "Object oriented programming", ""],
        ["Average afferent coupling", "Coupling", ""],
        ["Average efferent coupling",  "Coupling", ""], 
        ["Average instability", "Coupling", ""],
        ["Depth of Inheritance Tree",  "Coupling", ""],
        ["Packages", "Package", ""],
        ["Average classes per package", "Package", ""],
        ["Average distance", "Package", ""],
        ["Average incoming class dependencies", "Package", ""],
        ["Average outgoing class dependencies", "Package", ""],
        ["Average incoming package dependencies", "Package", ""],
        ["Average outgoing package dependencies", "Package", ""],
        ["Average Cyclomatic complexity by class", "Complexity", ""],
        ["Average Weighted method count by class", "Complexity", ""],
        ["Average Relative system complexity", "Complexity", ""],
        ["Average Difficulty", "Complexity", ""],
        ["Average bugs by class", "Bugs", ""],
        ["Average defects by class (Kan)", "Bugs", ""],
        ["Critical", "Violations", ""],
        ["Error", "Violations", ""],
        ["Warning", "Violations", ""],
        ["Information", "Violations", ""]
    ];
    df = pd.DataFrame(phpmetrics, columns=['Metric','Category', 'Value']) 
    with open('phpmetrics.txt') as f:
        lines = f.readlines() # list containing lines of file
        for line in lines:
            line = line.strip() # remove leading/trailing white spaces    
            for index, row in df.iterrows():
                if row['Metric'] == "Average defects by class (Kan)":
                    if re.search(r"\b"+"(Kan)"+r"\b",line) and row['Value'] == "": # add value only if there is not one yet.
                        s_nums = re.findall(r"[-+]?\d*\.\d+|\d+", str(line))
                        logging.info(row['Metric'] + ": " + s_nums[0]) # logging
                        row['Value'] = s_nums[0]
                else:
                    if re.search(r"\b"+row['Metric']+r"\b",line) and row['Value'] == "": # add value only if there is not one yet.
                        s_nums = re.findall(r"[-+]?\d*\.\d+|\d+", str(line))
                        logging.info(row['Metric'] + ": " + s_nums[0]) # logging
                        row['Value'] = s_nums[0]
    df.to_json (r'phpmetrics.json', orient='records') # export to JSON with each item to reflect a tuple [Metric, Category, Value]

def get_metrics(df, index):
    """ PHPMETRICS function """
    # read file
    with open('phpmetrics.json', 'r') as myfile:
        data=myfile.read()
    # parse file
    obj = json.loads(data)

    loc = 0
    lloc = 0
    cc = 0
    lcom = 0
    ins = 0
    doc = 0
    noc = 0

    for metric in obj:
        if metric['Metric'] == "Lines of code":
            loc = int(metric['Value'])
        elif metric['Metric'] == "Logical lines of code":
            lloc = int(metric['Value'])
        elif metric['Metric'] == "Classes":
            noc = int(metric['Value'])
        elif metric['Metric'] == "Average Cyclomatic complexity by class":
            cc = float(metric['Value'])
        elif metric['Metric'] == "Lack of cohesion of methods":
            lcom = float(metric['Value'])
        elif metric['Metric'] == "Average instability":
            ins = float(metric['Value'])

    cc_final = 0
    if(cc<11): 
        cc_final = 5
    elif(cc<16):
        cc_final = 4
    elif(cc<21):
        cc_final = 3
    elif(cc<50):
        cc_final = 2
    else:
        cc_final = 1

    df.at[index,'i22_complexity'] =  int(cc_final) / 5
    df.at[index,'i24_instability'] = ins

    coh = 0
    if(noc<102):
        if(lcom<1):
            coh = 3
        elif(lcom<26):
            coh = 2
        else:
            coh = 1
    elif(noc<1001):
        if(lcom<1):
            coh = 3
        elif(lcom<21):
            coh = 2
        else:
            coh = 1
    else:
        if(lcom<1):
            coh = 3
        elif(lcom<21):
            coh = 2
        else:
            coh = 1   

    df.at[index,'i25_cohesion'] = round(int(coh) / 3)
    df.at[index,'i35_documendation'] = round(int(lloc)/int(loc))

""" MAIN FUNCTION """
def main():
    global githubToken
    df = pd.read_csv("./data/input.csv", index_col=0) # Read CSV with input data
    
    # For every row (project / version)
    for index, row in df.iterrows():
        if row.analysis_complete != 1:
            
            # STEP 1: Initialize qualitative values with auto_expert_value field *** if not set by an expert *** // 11 indicators
            if not pd.isna(row.auto_expert_value):
                df.at[index,'i1_robustness'] = row.auto_expert_value  / 5
                df.at[index,'i2_scalability'] = row.auto_expert_value / 5
                df.at[index,'i3_usability'] = row.auto_expert_value / 5
                df.at[index,'i5_corrections'] = row.auto_expert_value / 5
                df.at[index,'i6_improvements'] = row.auto_expert_value / 5
                df.at[index,'i7_security'] = row.auto_expert_value / 5
                df.at[index,'i18_installability'] = row.auto_expert_value / 5
                df.at[index,'i19_configurability'] = row.auto_expert_value / 5
                df.at[index,'i20_self_contained'] = row.auto_expert_value / 5
                df.at[index,'i21_resource_utilization'] = row.auto_expert_value / 5
                df.at[index,'i23_modularity'] = row.auto_expert_value / 5

            # STEP 2: Get user input via GUI // 18 indicators
            callGUI(df, index) 
            print("out" + githubToken)
            g = Github(githubToken)

            # STEP 3:Get Github input // 5 indicators
            s_date = datetime.strptime(str(row.version_start_date), '%Y-%m-%d') # should be datetime objects or else PyGithub won't work
            e_date = datetime.strptime(str(row.version_end_date), '%Y-%m-%d') # should be datetime objects or else PyGithub won't work
            g_repo = row.repo_name    
            get_devs(df, index, s_date, e_date, g_repo, g)
            get_issues(df, index, s_date, e_date, g_repo, g)

            # STEP 4: Get language specific indicators // 4 indicators
            # PHP w/ PHPMETRICS Analyzer
            if row.language == 'PHP':    
                url = row.repo_url
                tag = row.version_github_tag
                os.system('git clone {0} --branch {1}'.format(url, tag))
                a_r = row.repo_name
                pos = a_r.find('/')
                repo_name = a_r[pos+1:]
                os.system('phpmetrics --report-html=myreport ./{0} >> phpmetrics.txt'.format(repo_name))
                phpmetrics_export(df, index, 'phpmetrics.txt')
                os.system('rm phpmetrics.txt')
                get_metrics(df, index)

                # Calculate OSSRF goals and dimensions output
                g1 = ( df.at[index,'i1_robustness'] + df.at[index,'i2_scalability'] + df.at[index,'i3_usability'] + df.at[index,'i4_effectiveness'] ) / 4
                df.at[index,'g1_architecture'] = round( g1 * 100 )
                g2 = ( df.at[index,'i5_corrections'] + df.at[index,'i6_improvements'] ) / 2
                df.at[index,'g2_maintenability'] = round( g2 * 100 )
                g3 = ( df.at[index,'i7_security'] + df.at[index,'i8_testing_process'] + df.at[index,'i9_coverage'] ) / 3
                df.at[index,'g3_security_testing'] = round( g3 * 100 )
                g4 = df.at[index,'i10_license_type']
                df.at[index,'g4_license'] = round( g4 * 100 )
                g5 = ( df.at[index,'i11_dual_licensing'] + df.at[index,'i12_commercial_resources'] + df.at[index,'i13_commercial_training'] + df.at[index,'i14_industry_adoption'] ) / 4
                df.at[index,'g5_market'] = round( g5 * 100 )
                g6 = ( df.at[index,'i15_ngo_support'] + df.at[index,'i16_corporate_support'] + df.at[index,'i17_donations'] ) / 3
                df.at[index,'g6_support'] = round( g6 * 100 )
                g7 = ( df.at[index,'i18_installability'] + df.at[index,'i19_configurability'] ) / 2
                df.at[index,'g7_initialization'] = round( g7 * 100 )
                g8 = ( df.at[index,'i20_self_contained'] + df.at[index,'i21_resource_utilization'] ) / 2
                df.at[index,'g8_dependencies'] = round( g8 * 100 )
                g9 = ( df.at[index,'i22_complexity'] + df.at[index,'i23_modularity'] + df.at[index,'i24_instability'] + df.at[index,'i25_cohesion'] ) / 4
                df.at[index,'g9_reuse'] = round( g9 * 100 )
                g10 = ( df.at[index,'i26_governance_model'] + df.at[index,'i27_project_road_map'] + df.at[index,'i28_code_of_conduct'] + df.at[index,'i29_coding_standards'] + df.at[index,'i30_documentation_standards'] ) / 5
                df.at[index,'g10_dev_process_governance'] = round( g10 * 100 )
                g11 = ( df.at[index,'i31_devs_attracted'] + df.at[index,'i32_devs_active'] + df.at[index,'i33_nof_open_issues'] + df.at[index,'i34_open_vs_closed_issues'] + df.at[index,'i35_documendation'] ) / 5
                df.at[index,'g11_developer_base'] = round( g11 * 100 )
                g12 = ( df.at[index,'i36_localization_process'] + df.at[index,'i37_issue_tracking'] + df.at[index,'i38_user_guide'] ) / 3
                df.at[index,'g12_user_base'] = round( g12 * 100 )
                
                d1 = ( g1 + g2 + g3 ) / 3
                df.at[index,'d1_source_code'] = round( d1 * 100 )
                d2 = ( g4 + g5 + g6 ) / 3
                df.at[index,'d2_business_legal'] = round( d2 * 100 )
                d3 = ( g7 + g8 + g9 ) / 3
                df.at[index,'d3_integration_reuse'] = round( d3 * 100 )
                d4 = ( g10 + g11 + g12 ) / 3
                df.at[index,'d4_social'] = round( d4 * 100 )

            # Update row when analysis is complete (analysis_complete = YES)
            df.at[index,'analysis_complete'] = 1

    # Write the updated dataframe to CSV
    df.to_csv("./data/input.csv")

if __name__ == "__main__":
    main()