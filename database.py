import psycopg2

# here we implement PostgreSql database connection and functionality


class MyDatabase():
    def __init__(self, host: str = 'localhost', db: str = 'first', user: str = 'postgres', password: str = 'admin'):  # port is deault = 5432
        self.connection = psycopg2.connect(
            host=host, database=db, user=user, password=password)
        self.cur = self.connection.cursor()

 ################# DB functionality for islaidu_tipai screen ########################################

    # main query from islaidu_tipai table
    # table is ordered by active/inactive and then alphabetically

    def islaidos_query(self) -> list:
        try:
            self.cur.execute(
                'SELECT * FROM islaidu_tipai ORDER BY aktyvus DESC, tipai ASC')
            data = self.cur.fetchall()
            return data
        except (Exception, psycopg2.Error) as err:
            # TODO# show dialog box if connection problem/failed to execute
            pass

    # add values to islaidu_tipai table

    def add_islaidos(self, tipai: str, aktyvus: bool):
        try:
            self.cur.execute(
                "INSERT INTO islaidu_tipai(tipai, aktyvus) VALUES (%s, %s)", (tipai, aktyvus))
            self.connection.commit()
        except (Exception, psycopg2.Error) as err:
            # TODO# show dialog box if connection problem/failed to execute
            print('Failed to execute', err)

#######################################################################################################

################################## Dialog box' functionality ##########################################

### chnage type (active/inactive) on islaidu_tipai table
def change_active_status(self, type_name: str, curr_type: bool):
       try:
            self.cur.execute(
                "UPDATE islaidu_tipai SET aktyvus = %s WHERE tipai = '%s'", (curr_type, type_name))
            self.connection.commit()
       except (Exception, psycopg2.Error) as err:
            # TODO# show dialog box if connection problem/failed to execute
            print('Failed to execute', err)
########################################################################################################



