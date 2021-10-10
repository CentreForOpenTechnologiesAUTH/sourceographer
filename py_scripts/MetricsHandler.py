import GrimoireProject
import PHPQAProject

class MetricsHandler:

    Grimoire_Data = []
    Grimoire_setOfFields = {}

    PHPQA_Data = []
    PHPQA_setOfFields = {}

    def __init__(self):
        print("Collecting data.")


    def collectGrimoire_Data(self):

        grprj = GrimoireProject.GrimoireProject()
        grprj.getData()
        self.Grimoire_Data = list(grprj.projectData)

        grprj.projectData.clear()


    def collectPHPQA_Data(self):

        phpqaprj = PHPQAProject.PHPQAProject()
        phpqaprj.getData()
        self.PHPQA_Data = list(phpqaprj.projectData)

        phpqaprj.projectData.clear()


    def collectAll_Data(self):

        grprj = GrimoireProject.GrimoireProject()
        grprj.getData()
        self.Grimoire_Data = list(grprj.projectData)

        grprj.projectData.clear()

        phpqaprj = PHPQAProject.PHPQAProject()
        phpqaprj.getData()
        self.PHPQA_Data = list(phpqaprj.projectData)

        phpqaprj.projectData.clear()


    def collect_setOfFields(self):

        grprj = GrimoireProject.GrimoireProject()
        self.Grimoire_setOfFields = list(grprj.setOfFields)

        phpqaprj = PHPQAProject.PHPQAProject()
        self.PHPQA_setOfFields = list(phpqaprj.setOfFields)
