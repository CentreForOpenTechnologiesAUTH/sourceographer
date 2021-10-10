import jsonParser

from pprint import pprint


class GrimoireProject:


    setOfFields = {"assignee_email", 
		   "assignee_geolocation",
		   "assignee_location", 
		   "assignee_login", 
		   "assignee_name",
           "assignee_org",
		   "author_name", 
      	   "closed_at",
		   "created_at", 
		   "github_repo",
		   "grimoire_creation_date",
           "id",
		   "id_in_repo",
		   "is_github_issue", 
		   "item_type", 
		   "labels", 
		   "metadata__enriched_on",
           "metadata__gelk_backend_name",
		   "metadata__gelk_version", 
		   "metadata__timestamp", 
		   "metadata__updated_on",
           "origin",
		   "offset",
		   "pull_request", 
		   "repository", 
		   "state", 
		   "tag", 
		   "time_open_days", 
		   "time_to_close_days", 
		   "title",
           "title_analyzed",
	       "updated_at",
		   "url", 
		   "url_id",
		   "user_email", 
		   "user_geolocation", 
		   "user_location",
           "user_login",
		   "user_name", 
		   "user_org", 
		   "uuid"}

    projectData = []


    def __init__(self):
        print("Grimoire Project initialized")


    def getData(self):

        parser = jsonParser.jsonParser('myindex.json')
        parser.parse()

        self.projectData = list(parser.dataUser)


    def printProjectData(self):
        for field in self.setOfFields:
            print(field)
            for line in self.projectData:
                pprint(line[field])




