

import pyodbc

# cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
# cursor = cnxn.cursor()


class Table_create:
    def __init__(self, table_name, column_info):
        self.server = 'localhost,1433'
        self.database = 'Northwind'
        self.username = 'SA'
        self.password = 'Passw0rd2018'
        self.table_name = table_name
        self.columns_info = column_info
        self.column_strings = []


    def set_column_strings(self):
        for column in self.column_info.keys():
            column_string = column
            column_string += ' '
            column_string += column['Type']
            if 'Primary_Key' in column.keys():
                column_string+= ' IDENTITY'








