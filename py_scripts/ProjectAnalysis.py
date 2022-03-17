import MySQLdb
import MetricsHandler


class ProjectAnalysis:

    ##To do: optimization to hide personal fields, use as is for now
    db = MySQLdb.connect(host="localhost",
                         user="phpmyadminuser",
                         passwd="*******",
                         db="Sourceographer")

    mh = MetricsHandler.MetricsHandler()


    def __init__(self):

        self.mh.collectAll_Data()
        self.mh.collect_setOfFields()

        print("Project Analysis initialized")


    def insert_Data_Grimoire(self):

        cr = self.db.cursor()

        for line in self.mh.Grimoire_Data:
            del line['user_geolocation']
            del line['assignee_geolocation']

            for field in self.mh.Grimoire_setOfFields:
                if (field is not 'user_geolocation' and field is not 'assignee_geolocation'):
                    vals = str(line[field])
                    vals = str(vals).encode('utf8')
                    vals = str(vals).replace("'", "")
                    vals = str(vals).replace("b", "", 1)
                    line[field]=vals

            placeholder = ", ".join(["%s"] * len(line))
            stmt = "insert into `{table}` (`{columns}`) values ({values});".format(table="Grimoire", columns="`,`".join(line.keys()),
                                                                     values=placeholder)
            #print(stmt)

            cr.execute(stmt, line.values())

        cr.close()
        self.db.commit()


    def insert_Data_PHPQA(self):

        cr = self.db.cursor()

        for line in self.mh.PHPQA_Data:

            placeholder = ", ".join(["%s"] * len(line))
            stmt = "insert into `{table}` (`{columns}`) values ({values});".format(table="PHPQA",
                                                                                   columns="`,`".join(line.keys()),
                                                                                   values=placeholder)
            #print(stmt)

            cr.execute(stmt, line.values())

        cr.close()
        self.db.commit()


    def insert_Data(self):

        self.insert_Data_Grimoire()
        self.insert_Data_PHPQA()

        self.db.close()



PA = ProjectAnalysis()
PA.insert_Data()
