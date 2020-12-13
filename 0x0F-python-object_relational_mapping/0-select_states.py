#!/usr/bin/python3
'''
    MySQLdb
'''
if __name__ == "__main__":

    import sys
    import MySQLdb

    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("""SELECT * FROM states
                ORDER BY states.id ASC""")
    for row in c.fetchall():
        print(row)
    c.close()
    db.close()
