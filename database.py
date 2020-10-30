import psycopg2

# here we implement PostgreSql database connection and functionality


class MyDatabase():
    def __init__(self, host: str = 'localhost', db: str = 'first', user: str = 'postgres', password: str = 'admin'):  # default port number = 5432
        self.connection = psycopg2.connect(
            host=host, database=db, user=user, password=password)
        self.cur = self.connection.cursor()

 ################# DB functionality for islaidu_tipai screen ########################################

    # main query from islaidu_tipai table
    # table is ordered by active/inactive and then alphabetically

    def islaidos_tipai_query(self) -> list:
        try:
            self.cur.execute(
                'SELECT * FROM islaidu_tipai ORDER BY aktyvus DESC, tipai ASC')
            _data = self.cur.fetchall()
            return _data
        except (Exception, psycopg2.Error) as err:
            # TODO# show dialog box if connection problem/failed to execute
            pass

    # add values to islaidu_tipai table

    def add_islaidos_tipai(self, tipai: str, aktyvus: bool):
        try:
            self.cur.execute(
                "INSERT INTO islaidu_tipai(tipai, aktyvus) VALUES (%s, %s)", (tipai, aktyvus))
            self.connection.commit()
        except (Exception, psycopg2.Error) as err:
            # TODO# show dialog box if connection problem/failed to execute
            print('Failed to execute', err)

#######################################################################################################

################# DB functionality for islaidos screen ################################################
    def islaidos_query(self) -> list:
        try:
            self.cur.execute(
                'SELECT * FROM islaidos ORDER BY data DESC')
            _data = self.cur.fetchall()
            print(_data)
            return _data
        except (Exception, psycopg2.Error) as err:
            # TODO# show dialog box if connection problem/failed to execute
            pass

     # add values to islaidos table

    def add_islaidos(self, data: str, tipas: str, tiekejas: str, dok_nr: str, suma: float):
        try:
            self.cur.execute(
                "INSERT INTO islaidos(data,tipas,tiekejas,dok_nr,suma) VALUES (%s, %s,%s,%s,%s)", (data, tipas, tiekejas, dok_nr, suma))
            self.connection.commit()
        except (Exception, psycopg2.Error) as err:
            # TODO# show dialog box if connection problem/failed to execute
            print('Failed to execute', err)
    
    # getting all types from islaidu_tipai for box selection on add_new_islaidos widget
    def get_box_info(self) -> list:
        try:
            self.cur.execute(
                'SELECT tipai FROM islaidu_tipai WHERE aktyvus = True ORDER BY tipai ASC')
            _data = self.cur.fetchall()
            return [el[0] for el in _data] ## returning sorted data from db : list of tuples -> list
        except (Exception, psycopg2.Error) as err:
            # TODO# show dialog box if connection problem/failed to execute
            print(err)



#######################################################################################################

################################## Dialog box' functionality ##########################################

    # change type (active/inactive) on islaidu_tipai table and/or type itself


    def change_active_status(self, type_name: str, new_type: str, curr_type: bool):
        try:
            self.cur.execute(
                "UPDATE islaidu_tipai SET aktyvus = %s, tipai = %s WHERE tipai = %s", (curr_type, new_type, type_name))
            self.connection.commit()
        except (Exception, psycopg2.Error) as err:
            # TODO# show dialog box if connection problem/failed to execute
            print('Failed to execute', err)

    
    ######################################################################################################
