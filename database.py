import psycopg2

# here we implement PostgreSql database connection and functionality


class MyDatabase():
    def __init__(self, host: str = 'localhost', db: str = 'first', user: str = 'postgres', password: str = 'admin'):
        self.connection = psycopg2.connect(
            host=host, database=db, user=user, password=password)
        self.cur = self.connection.cursor()

    # basic query function from a database
    def query(self, query: str):
        self.cur.execute(query)
