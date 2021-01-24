import pyodbc


server = 'localhost,1433'
database = 'Airbnb'
username = 'SA'
password = 'Passw0rd2018'

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()
a = cursor.execute("""
                                            SELECT pk_tab.name
                                            FROM sys.tables tab
                                                INNER JOIN sys.columns col
                                                    ON col.object_id = tab.object_id
                                                LEFT OUTER JOIN sys.foreign_key_columns fk_cols
                                                    ON fk_cols.parent_object_id = tab.object_id
                                                    AND fk_cols.parent_column_id = col.column_id
                                                LEFT OUTER JOIN sys.foreign_keys fk
                                                    ON fk.object_id = fk_cols.constraint_object_id
                                                LEFT OUTER JOIN sys.tables pk_tab
                                                    ON pk_tab.object_id = fk_cols.referenced_object_id
                                                LEFT OUTER JOIN sys.columns pk_col
                                                    ON pk_col.column_id = fk_cols.referenced_column_id
                                                    AND pk_col.object_id = fk_cols.referenced_object_id
                                            WHERE col.name = 'Location_ID' AND tab.name = 'Listings'
                                            """).fetchone()

print(a)