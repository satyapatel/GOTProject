import MySQLdb
import logging

log = logging.getLogger(__name__)

class MySqlHandler:

    def __init__(self):
        self.db = MySQLdb.connect("satyapatel.mysql.pythonanywhere-services.com","satyapatel","June@@2016","satyapatel$SatyaPatelDatabase" )
        self.cursor = self.db.cursor()

    def execute_query(self, query):
        try :
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except Exception as e:
            log.exception(e)
            return []

    def close(self):
        self.db.close()
