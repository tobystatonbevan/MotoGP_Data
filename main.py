from modules import insertContent,createConnection,displayContents

dbConnection = createConnection()

# Open a cursor to perform database operations
cur = dbConnection.cursor()

try:
    insertContent(cur,"motogp_riders",["rider_num","rider_name","bike_manufacturer","current_track"],[11,'Jolly Rodger','Lexmoto','Brown Lid'])
except Exception as e:
    print(e)

# Make the changes to the database persistent
dbConnection.commit()

rows = displayContents(cur)
dbConnection.commit()
# Close cursor and communication with the database
cur.close()
dbConnection.close()

for row in rows:
    print(row)