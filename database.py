import psycopg2

# here we implement PostgreSql database connection and functionality


class MyDatabase():
    def __init__(self, host: str = 'localhost', db: str = 'first', user: str = 'postgres', password: str = 'admin'): ### port is deault = 5432
        self.connection = psycopg2.connect(
            host=host, database=db, user=user, password=password)
        self.cur = self.connection.cursor()

    # basic query function from a database
    def query(self, query: str):
        pass
        #self.cur.execute(query)

    # main query for islaidu_tipai
    #first, table is ordered by active/inactive and then alphabetically 
    def islaidos_query(self) -> List:
        self.cur.execute('SELECT * FROM islaidu_tipai ORDER BY aktyvus DESC, tipai ASC') 
        data = self.cur.fetchall()
        return data
    
    # add values to islaidu_tipai table
    def add_islaidos(self,tipai:str,aktyvus:bool):
        self.cur.execute('INSERT INTO islaidu_tipai (tipai, aktyvus) VALUES ({},{})'.format(tipai,aktyvus))
