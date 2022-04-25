import os
import datetime
import pymysql

# Get username from Gitpod workspace
username = os.getenv("C9_USER")

# Connect to database
connection = pymysql.connect(host="localhost",
                             user=username,
                             password="",
                             db="Chinook")


# try:
#     # Run a query
#     with connection.cursor() as cursor:
#         sql = "SELECT * FROM Artist;"
#         cursor.execute(sql)
#         result = cursor.fetchall()
#         print(result)

# try:
#     # Run a query - make the list a tuple
#     with connection.cursor() as cursor:
#         sql = "SELECT * FROM Genre;"
#         cursor.execute(sql)
#         for row in cursor:
#             print(row)

# try:
#     # Run a query - make the list a dictionary
#     with connection.cursor(pymysql.cursors.DictCursor) as cursor:
#         sql = "SELECT * FROM Genre;"
#         cursor.execute(sql)
#         for row in cursor:
#             print(row)

# try:
#     # Run a query - create a new table if it doesn't exist
#     with connection.cursor() as cursor:
#         cursor.execute("""CREATE TABLE IF NOT EXIST
#                         Friends(name char(20), age int, DOB datetime);""")

# try:
#     # Run a query - insert value into table
#     with connection.cursor() as cursor:
#         row = ("Bob", 21, "1990-02-06 23:04:56")
#         cursor.execute("INSERT INTO Friends VALUES(%s, %s, %s);", row)
#         connection.commit()

# try:
#     # Run a query - insert multiple rows with values into table
#     with connection.cursor() as cursor:
#         rows = [("Bob", 21, "1990-02-06 23:04:56"),
#                 ("Jim", 56, "1955-05-09 13:12:45"),
#                 ("Fred", 100, "1911-09-12 01:01:01")]
#         cursor.executemany("INSERT INTO Friends VALUES(%s, %s, %s);", rows)
#         connection.commit()

# try:
#     # Run a query - update a row
#     with connection.cursor() as cursor:
#         cursor.execute("UPDATE Friends SET age=22 WHERE name='Bob';")
#         connection.commit()

# try:
#     # Run a query - update a row using a tuple
#     with connection.cursor() as cursor:
#         cursor.execute("UPDATE Friends SET age=%s WHERE name=%s;", (23, "Bob"))
#         connection.commit()

# try:
#     # Run a query - update multiple rows using tuple list
#     with connection.cursor() as cursor:
#         rows = [(23, "Bob"),
#                 (24, "Jim"),
#                 (25, "Fred")]
#         cursor.executemany("UPDATE Friends SET age=%s WHERE name=%s;", rows)
#         connection.commit()
# try:
#     # Run a query - delete a row
#     with connection.cursor() as cursor:
#         cursor.execute("DELETE FROM Friends WHERE name='Bob';")
#         connection.commit()
# try:
#     # Run a query - delete a row using tuple
#     with connection.cursor() as cursor:
#         rows = cursor.execute("DELETE FROM Friends WHERE name=%s;", 'Bob')
#         connection.commit()
# try:
#     # Run a query - delete multiple rows using tuple
#     with connection.cursor() as cursor:
#         cursor.executemany("DELETE FROM Friends WHERE name=%s;", ['Bob', 'Jim'])
#         connection.commit()

# try:
#     # Run a query - delete multiple rows using tuple
#     with connection.cursor() as cursor:
#         cursor.executemany("DELETE FROM Friends WHERE name in ('Bob', 'Jim')")
#         connection.commit()

# try:
#     # Run a query - delete multiple rows using tuple
#     with connection.cursor() as cursor:
#         names = ['Jim', 'Bob']
#         cursor.execute("DELETE FROM Friends WHERE name in (%s, %s)", names)
#         connection.commit()

try:
    # Run a query - delete multiple rows using tuple
    with connection.cursor() as cursor:
        list_of_names = ['Jim', 'Bob']
        # Prepare the string with tha same number of placeholders as in list_of_names
        format_strings = ','.join(['%s']*len(List_of_names))
        cursor.execute("DELETE FROM Friends WHERE name in ({});"
                       .format(format_strings), list_of_names)
        connection.commit()
finally:
    # Close the connection, regardless of whether the above was successful
    connection.close()
    