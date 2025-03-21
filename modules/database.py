import configu
import psycopg2

dbConnection = psycopg2.connect(database = "motogp_test", 
                        user = configu.dbUser, 
                        password = configu.dbPassword,
                        host= 'localhost',
                        port = 5432)

# Open a cursor to perform database operations
cur = dbConnection.cursor()
# Execute a command: create motogp_riders table
cur.execute("""CREATE TABLE motogp_riders(
            id SERIAL PRIMARY KEY,
            rider_num SERIAL UNIQUE NOT NULL,
            rider_name VARCHAR (50) UNIQUE NOT NULL,
            bike_manufacturer VARCHAR (50) NOT NULL,
            current_track VARCHAR (50) NOT NULL);
            """)


cur.execute("INSERT INTO motogp_riders(rider_num,rider_name,bike_manufacturer,current_track) VALUES(93,'Marc Maquez','Ducati','Brands Hatch')")

# Make the changes to the database persistent
dbConnection.commit()

cur.execute('SELECT * FROM motogp_riders;')
rows = cur.fetchall()
dbConnection.commit()
# Close cursor and communication with the database
cur.close()
dbConnection.close()

for row in rows:
    print(row)


#separate out table creation, population, viewing