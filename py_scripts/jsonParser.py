import json
import codecs


from pprint import pprint


class jsonParser:

    data = []
    dataUser = []
    dataLoc = []
    file = './outputs/myindex.json' ##To do: optimizations in the file reading

    def __init__(self, file):

        self.file = file


    def parse(self):

        with codecs.open(self.file, 'rU', 'utf-8') as infile:
         for line in infile:
            self.data.append(json.loads(line))

        infile.close()

        for line in self.data:
            if 'lon' in line and 'location' in line and 'lat' in line:
                self.dataLoc.append(line)
            else:
                self.dataUser.append(line)

        self.data.clear()



    def printField(self, field):

        for line in self.dataUser:
            pprint(line[field])





