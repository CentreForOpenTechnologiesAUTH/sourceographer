import os
import logging
from datetime import datetime


logging.basicConfig(filename="actions.log", level=logging.INFO)

with open('actions.log', 'w'):
    pass

logging.info('flowcontroller.py STARTS @ {0}'.format(datetime.now()))

os.system("python3 gui_init.py")
os.system("python3 github_APIInfo.py")
os.system("python3 phpqa_phpmetrics.py")

os.system("python3 other_metrics.py")
os.system("python3 csv_output.py")

logging.info('flowcontroller.py complete @ {0}.'.format(datetime.now()))
