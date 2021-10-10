from github import Github
from datetime import datetime
import pandas as pd
import logging

ACCESS_TOKEN = '350a99b4631e71168b17bc6f2acee45785472305'
g = Github(ACCESS_TOKEN)

def get_devs(d_start, d_end, g_repo):
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

    devs_attracted = round((new_devs_counter / all_time_devs) * 100)
    active_devs = round((active_devs_counter / all_time_active_devs) * 100)

    df = pd.read_csv('indicators.csv', delimiter = ',')
    df['Developers Attracted'] = df['Developers Attracted'].fillna(devs_attracted)
    df['Active Developers'] = df['Active Developers'].fillna(active_devs)
    df.to_csv('indicators.csv', index = False)
    
    print("Developers Attracted: ", devs_attracted, "%")
    print("Active Developers: ", active_devs, "%")


def get_issues(d_start, d_end, g_repo):
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

    no_of_open_issues = round((1 - (open_issues_version_counter / opened_issues_beginningToVersion_counter)) * 100)
    open_closed_issues = round((closed_issues_version_counter / open_issues_version_counter) * 100)
    issue_tracking_activity = round((open_issues_version_counter / opened_issues_beginningToVersion_counter) * 100)

    df = pd.read_csv('indicators.csv', delimiter = ',')
    df['Number of open issues'] = df['Number of open issues'].fillna(no_of_open_issues)
    df['Open / Closed issues'] = df['Open / Closed issues'].fillna(open_closed_issues)
    df['Issue tracking activity'] = df['Issue tracking activity'].fillna(issue_tracking_activity)
    df.to_csv('indicators.csv', index = False)
    
    print("Number of Open Issues: ", no_of_open_issues, "%")
    print("Open/Closed Issues: ", open_closed_issues, "%")
    print("Issue Tracking Activity: ", issue_tracking_activity, "%")


if __name__ == '__main__':

    logging.basicConfig(filename="actions.log", level=logging.INFO)

    logging.info('github_APIInfo.py initiated @ {0}.'.format(datetime.now()))

    df_read = pd.read_csv('input_metrics.csv', delimiter = ',')

    starting_date = df_read['s_date'].iloc[0]
    s_date = datetime.strptime(starting_date, '%Y-%m-%d')

    ending_date = df_read['e_date'].iloc[0]
    e_date = datetime.strptime(ending_date, '%Y-%m-%d')
    
    g_repo = df_read['repo_author'].iloc[0]
    
    get_devs(s_date, e_date, g_repo)
    get_issues(s_date, e_date, g_repo)

    logging.info('github_APIInfo.py complete @ {0}.'.format(datetime.now()))
