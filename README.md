# gui_project - mini ERP application

## Required packages

```
pip install PyQt5
pip install PyQtChart
pip install psycopg2-binary
```

## Before start

Setup local postgreSql database with parameters: 
 - host = localhost
 - database-name = first  #I know, stupid name for db :)
 - user = postgres
 - password = admin
 - port = 5432  # default port

 Then create two tables with schemas (colummn_name(type)):
 - 'islaidu_tipai'  table (tipai(varchar[xx]), aktyvus(bool)))
 - 'islaidos'  table (data(date), tipas(varchar[xx]), tiekejas(varchar[xx]), dok_nr(varchar[xx]), suma(double precision))   # but usig numeric or decimal type with precision of 2 in this case scenarion would be better idea.

 ## Launch Script

```
/.~ python main.py
```

## Major drawbacks and problems
Due to time constraints , there were some problems left. The major one is that main data representation widgets does not update, redraw itself after the data has been submitted or executed. Possible sollution is: instead of QTableWIdget use QTableView widget with QsQL package provided by Pyqt5 itself.
So, as for example, if you add or change record ,you need to 'redraw that page manually' : example : if you add new type to islaidos_type, you need to prees 'Nustatymai' menu button to see changes to appear and so on. Due to this consistent problem some part of required task elements are not working. 