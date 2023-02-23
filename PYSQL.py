import sqlite3
# All the SQL functions you could ever want
# These functions make the object oriented interface to SQLite
def print_data( data):
    for row in data:
        print(row)

# This will show the schema of the table
def table_schema(table_name):
    sql_query = """SELECT sql FROM sqlite_master
                WHERE name = '{}';""".format(table_name)
    c.execute(sql_query)
    for i in c.fetchall():
        for j in i:
            print(j)

# This will show the schema of the database
def database_schema():
    sql_query = """SELECT sql FROM sqlite_master
                WHERE type = 'table';"""
    c.execute(sql_query)
    for i in c.fetchall():
        for j in i:
            print(j)


class PSQL:
    # Initialize the database
    # This will create a connection to the database
    # This will also create a cursor to the database
    # This will create a object that can be used to run queries
    def __init__(self, db):
        self.db = db
        self.conn = sqlite3.connect(self.db)
        self.c = self.conn.cursor()

    # Commit changes to the database
    # This will save the changes to the database
    def commit(self):
        self.conn.commit()
    
    # Close the connection to the database
    def close(self):
        self.conn.close()

    # Run a query
    # This will run a query but doesn't return the results
    # This is most basic function
    def run(self, query):
        self.c.execute(query)

    # Create a table        
    def create_table(self, table, columns):
        self.c.execute("CREATE TABLE IF NOT EXISTS {} ({})".format(table, columns))
    
    # Insert a row into a table
    def insert(self, table, values):
        self.c.execute("INSERT INTO {} VALUES ({})".format(table, values))
    
    # Select rows from a table
    # This will return the results of the query
    def select(self, table, columns = "*", where=None):
        if where:
            self.c.execute("SELECT {} FROM {} WHERE {}".format(columns, table, where))
        else:
            self.c.execute("SELECT {} FROM {}".format(columns, table))
        return self.c.fetchall()
    
    # Delete rows from a table    
    def delete(self, table, where):
        self.c.execute("DELETE FROM {} WHERE {}".format(table, where))
    
    # Update rows in a table
    def update(self, table, set, where):
        self.c.execute("UPDATE {} SET {} WHERE {}".format(table, set, where))
    
    # Drop a table
    # This will delete the table from the database
    def drop(self, table):
        self.c.execute("DROP TABLE {}".format(table))
    
    # Show all tables in the database
    def show_tables(self):
        self.c.execute("SELECT name FROM sqlite_master WHERE type='table'")
        return self.c.fetchall()

    # Show all views in the database        
    def show_columns(self, table):
        self.c.execute("PRAGMA table_info({})".format(table))
        return self.c.fetchall()
    
    # Show all views in the table 
    def show_create_table(self, table):
        self.c.execute("SELECT sql FROM sqlite_master WHERE name='{}'".format(table))
        return self.c.fetchall()
    
    def show_indexes(self, table):
        self.c.execute("PRAGMA index_list({})".format(table))
        return self.c.fetchall()
        
    def show_index_info(self, index):
        self.c.execute("PRAGMA index_info({})".format(index))
        return self.c.fetchall()
    
    def show_triggers(self, table):
        self.c.execute("PRAGMA trigger_list({})".format(table))
        return self.c.fetchall()
    
    # This will show all the foreign keys in the database
    def show_foreign_keys(self, table):
        self.c.execute("PRAGMA foreign_key_list({})".format(table))
        return self.c.fetchall()
    
    # This will show all the foreign keys and their info in the database
    def show_foreign_key_info(self, table):
        self.c.execute("PRAGMA foreign_key_info({})".format(table))
        return self.c.fetchall()
        
    def show_collations(self):
        self.c.execute("SELECT name FROM sqlite_master WHERE type='collation'")
        return self.c.fetchall()
        
    def show_collation_info(self, collation):
        self.c.execute("PRAGMA collation_list({})".format(collation))
        return self.c.fetchall()

    # Show table schema of complete database
    def show_schema(self, database):
        self.c.execute("SELECT sql FROM sqlite_master WHERE type='table'")
        return self.c.fetchall()
    
    # Show table schema of a table
    def show_table_schema(self, table):
        self.c.execute("SELECT sql FROM sqlite_master WHERE name='{}'".format(table))
        return self.c.fetchall()
        
