import configu
import psycopg2

dbConnection = psycopg2.connect(database = "motogp_test", 
                        user = configu.dbUser, 
                        password = configu.dbPassword,
                        host= 'localhost',
                        port = 5432)

# Open a cursor to perform database operations
cur = dbConnection.cursor()
# Execute a command: create datacamp_courses table
cur.execute("""CREATE TABLE motogp_riders(
            rider_num SERIAL PRIMARY KEY,
            rider_name VARCHAR (50) UNIQUE NOT NULL,
            bike_manufacturer VARCHAR (50) NOT NULL,
            current_track VARCHAR (50) NOT NULL);
            """)
# Make the changes to the database persistent
dbConnection.commit()
# Close cursor and communication with the database
cur.close()
dbConnection.close()

#select from database