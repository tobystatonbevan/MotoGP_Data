from modules import configu
import psycopg2

def createConnection(dbName = "motogp_test",uName = configu.dbUser,pWord = configu.dbPassword, hName = "localhost", portNo = 5432):

    dbConn = psycopg2.connect(database = dbName, 
                            user = uName, 
                            password = pWord,
                            host= hName,
                            port = portNo)
    return dbConn

def createTable(c,q = "CREATE TABLE motogp_riders(id SERIAL PRIMARY KEY,rider_num SERIAL NOT NULL,rider_name VARCHAR (50) NOT NULL;"):
    # Execute a command: create motogp_riders table
    c.execute(q)
    return

#def insertContent(q = "INSERT INTO motogp_riders(rider_num,rider_name,bike_manufacturer,current_track) VALUES(93,'Marc Maquez','Ducati','Brands Hatch')"):
def insertContent(c,tName, cols, vals):
    stringCols = ",".join(cols)
    stringVals = str(vals)[1:-1]
    c.execute(f"INSERT INTO {tName}({stringCols}) VALUES({stringVals})")
    return

def displayContents(c,q = 'SELECT * FROM motogp_riders;'):
    c.execute(q)
    r = c.fetchall()
    return r