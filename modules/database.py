import configu
import psycopg2

def createConnection(dbName = "motogp_test",uName = configu.dbUser,pWord = configu.dbPassword, hName = "localhost", portNo = 5432):

    dbConn = psycopg2.connect(database = dbName, 
                            user = uName, 
                            password = pWord,
                            host= hName,
                            port = portNo)
    return dbConn

dbConnection = createConnection()

# Open a cursor to perform database operations
cur = dbConnection.cursor()

def createTable(q = "CREATE TABLE motogp_riders(id SERIAL PRIMARY KEY,rider_num SERIAL UNIQUE NOT NULL,rider_name VARCHAR (50) UNIQUE NOT NULL,bike_manufacturer VARCHAR (50) NOT NULL,current_track VARCHAR (50) NOT NULL);"):
    # Execute a command: create motogp_riders table
    cur.execute(q)
    return

#def insertContent(q = "INSERT INTO motogp_riders(rider_num,rider_name,bike_manufacturer,current_track) VALUES(93,'Marc Maquez','Ducati','Brands Hatch')"):
def insertContent(tName, cols, vals):
    stringCols = ",".join(cols)
    stringVals = str(vals)[1:-1]
    cur.execute(f"INSERT INTO {tName}({stringCols}) VALUES({stringVals})")
    return

insertContent("motogp_riders",["rider_num","rider_name","bike_manufacturer","current_track"],[11,'Jolly Rodger','Lexmoto','Brown Lid'])

# Make the changes to the database persistent
dbConnection.commit()

def displayContents(q = 'SELECT * FROM motogp_riders;'):
    cur.execute(q)
    r = cur.fetchall()
    return r

rows = displayContents()
dbConnection.commit()
# Close cursor and communication with the database
cur.close()
dbConnection.close()

for row in rows:
    print(row)


#separate out table creation, population, viewing