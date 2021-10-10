import xml.etree.ElementTree as ET
import pandas as pd
import os
import logging
from datetime import datetime

dataProject = []

file = './buildn/phpmetrics.xml'

def parse():

    tree = ET.parse(file)
    root = tree.getroot()

    root.attrib['namespace'] = 'Project'
    root.attrib['tag'] = root.tag
    dataProject.append(root.attrib)

def get_metrics():

	for line in dataProject:
        
		cc = line.get('cyclomaticComplexity')
		lcom = line.get('lcom')
		instability = line.get('instability')
		documentation = round(int(line.get('lloc')) / int(line.get('loc')) * 100)
		noc = line.get('noc')
	
	df = pd.read_csv('indicators.csv', delimiter = ',')
	df['Instability'] = df['Instability'].fillna(instability)
	df['Complexity'] = df['Complexity'].fillna(cc)
	df['Cohesion'] = df['Cohesion'].fillna(lcom)
	df['Documentation'] = df['Documentation'].fillna(documentation)
	df['noc'] = df['noc'].fillna(noc)
	df.to_csv('indicators.csv', index = False)

	print('Complexity: ', cc)
	print('LCOM: ', lcom)
	print('Instability: ', instability)
	print('Documentation: ', documentation, "%")

if __name__ == '__main__':

	logging.basicConfig(filename="actions.log", level=logging.INFO)
	logging.info('phpqa_phpmetrics.py initiated @ {0}.'.format(datetime.now()))

	df_read = pd.read_csv('input_metrics.csv', delimiter = ',')
	url = df_read['url'].iloc[0]
	tag = df_read['tag'].iloc[0]
	os.system('git clone {0} --branch {1}'.format(url, tag))

	a_r = df_read['repo_author'].iloc[0]
	pos = a_r.find('/')
	repo_name = a_r[pos+1:]
	os.system('phpqa --analyzedDirs ./{0} --buildDir ./buildn --tools phpmetrics'.format(repo_name))
	
	parse()
	get_metrics()

	logging.info('phpqa_phpmetrics.py complete @ {0}.'.format(datetime.now()))
