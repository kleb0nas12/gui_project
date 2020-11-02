# gui_project - mini ERP application

## Required packages

'''bash
pip install PyQt5
pip install PyQtChart
pip install psycopg2-binary

'''

## Before start

Setup local postgreSql database with parameters: 
 - host = localhost
 - database-name = first #I know, stupid name for db :)
 - user = postgres
 - password = admin
 - port = 5432 # default port

 Then create two tables with schemas (colummn_name(type)):
 - 'islaidu_tipai' table (tipai(varchar[xx]), aktyvus(bool)))
 - 'islaidos' table (data(date), tipas(varchar[xx]), tiekejas(varchar[xx]), dok_nr(varchar[xx]), suma(double precision)) # but usig numeric or decimal type with precision of 2 in this case scenarion would be better idea.

 ## Launch Script
 '''bash
/.~ python main.py

'''
