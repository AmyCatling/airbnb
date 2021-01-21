import pyodbc

# cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
# cursor = cnxn.cursor()


class Table_create:
    def __init__(self, table_name, column_info):
        self.server = 'localhost,1433'
        self.database = 'Airbnb'
        self.username = 'SA'
        self.password = 'Passw0rd2018'
        self.table_name = table_name
        self.columns_info = column_info
        self.column_strings = []
        self.set_column_strings()
        self.set_table_string()
        #self.create_table()

    def set_column_strings(self):
        for column in self.column_info.keys():
            column_string = column
            column_string += ' '
            column_string += column['Type']
            if 'Primary_Key' in column.keys():
                column_string+= ' IDENTITY PRIMARY KEY NOT NULL'
            elif 'Foreign_Key' in column.keys():
                column_string += ' FOREIGN KEY REFERENCES '
                column_string += column['Foreign_Key']
            elif 'Not_Null' in column.keys():
                column_string += ' NOT NULL'
            self.column_strings.append(column_string)

    def set_table_string(self):
        self.table_string = 'CREATE TABLE '
        self.table_string += self.table_name
        self.table_string += ' ('
        for column in self.column_strings[-1]:
            self.table_string += column
            self.table_string += ', '
        self.table_string += self.column_strings[-1]
        self.table_string += ')'

    def create_table(self):
        cnxn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
        cursor = cnxn.cursor()
        cursor.execute(self.table_string)










