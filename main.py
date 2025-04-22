from modules import insertContent,createConnection,displayContents,createTable,getRiderNameNumbers
from psycopg2 import OperationalError, errorcodes, errors

dbConnection = createConnection()

# Open a cursor to perform database operations
cur = dbConnection.cursor()

try:
    createTable(cur,"CREATE TABLE motogp_riders(id SERIAL PRIMARY KEY,rider_num SERIAL NOT NULL,rider_name VARCHAR (50) NOT NULL,UNIQUE (rider_num,rider_name));")
    # Make the changes to the database persistent
    dbConnection.commit()

except Exception as e:
    dbConnection.commit()
    print(e)

riderNameNumList = getRiderNameNumbers()

for i in riderNameNumList:
        try:
            # Open a cursor to perform database operations
            cur = dbConnection.cursor()
            insertContent(cur,"motogp_riders",["rider_num","rider_name"],[i['Number'],i['Name']])
            # Make the changes to the database persistent
            dbConnection.commit()
            #print(i)
        except Exception as e:
            dbConnection.commit()
            #print([i['Number'],i['Name']])
            #strips out unique violation errors so duplicates just get skipped without errors
            if type(e).__name__ != "UniqueViolation":
                print(f"{i} throws error: {type(e).__name__}")


cur = dbConnection.cursor()
rows = displayContents(cur)
dbConnection.commit()
# Close cursor and communication with the database
cur.close()
dbConnection.close()

for row in rows:
    print(row)

#motogp/2/3/e label somehow