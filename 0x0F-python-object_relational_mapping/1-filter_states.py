#!/usr/bin/python3
'''
    Filter states
'''
if __name__ == "__main__":
    import sys
    import MySQLdb

    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    c = db.cursor()
    c.execute("""SELECT * FROM states
                WHERE name LIKE BINARY 'N%'""")
    for row in c.fetchall():
        print(row)

    c.close()
    db.close()
