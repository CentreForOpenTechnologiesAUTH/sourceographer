import xmlParser
from pprint import pprint

class PHPQAProject:

    setOfFields = {"loc", 
		   "lloc", 
		   "cyclomaticComplexity", 
		   "maintainabilityIndex", 
		   "volume", 
		   "vocabulary", 
		   "difficulty",
           "effort",
		   "bugs", 
		   "time", 
		   "intelligentContent", 
		   "commentWeight", 
	       "length",
		   "lcom", 
	       "instability",
           "efferentCoupling",
		   "afferentCoupling", 
		   "sysc", 
		   "rsysc", 
		   "dc",
		   "rdc", 
		   "sc", 
	  	   "rsc", 
		   "noc", 
		   "noca",
           "nocc",
		   "noi", 
		   "nom", 
		   "namespace"}

    projectData = []


    def __init__(self):
        print('PHPQA project initialized')


    def getData(self):

        parser = xmlParser.xmlParser('phpmetrics.xml')
        parser.parse()

        self.projectData = list(parser.dataProject)


    def printProjectData(self):
        for field in self.setOfFields:
            print(field)
            for line in self.projectData:
                pprint(line)



