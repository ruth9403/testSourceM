import mysql.connector

class Connection():

    def __init__(self, user, password, database, host):
        self.connection = mysql.connector.connect(user=user, password=password,
                                                database=database, host=host)
        
        self.connection.autocommit = False
        print('conection successfull')

    def executeQuery(self, query, params): #para cada registro
        """ Para ejecutar las sentencias en la BD """
        cursor = self.connection.cursor()
        cursor.execute(query, params)

    def executeQueryArray(self, query, paramsArray):
        """ Para ejecutar las sentencias con arrays en la BD """
        cursor = self.connection.cursor()
        cursor.executemany(query, paramsArray)

    def commit(self):
        """ Para confirmar los inserts al la BD """
        self.connection.commit()

    def executeQuerySimple(self,query):
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        self.connection.commit()



    

