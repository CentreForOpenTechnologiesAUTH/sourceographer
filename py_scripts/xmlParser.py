import xml.etree.ElementTree as ET

class xmlParser:

    dataProject = []

    file = './outputs/phpmetrics.xml' ##To do: optimizations in the file reading


    def __init__(self,file):
        self.file = file


    def parse(self):

        tree = ET.parse(self.file)
        root = tree.getroot()

        root.attrib['namespace'] = 'Project'
        root.attrib['tag'] = root.tag
        #root.attrib['Project_ID']=""
        self.dataProject.append(root.attrib)


        for child in root:
            modules = child


        for module in modules:
            module.attrib['tag'] = module.tag
            self.dataProject.append(module.attrib)

