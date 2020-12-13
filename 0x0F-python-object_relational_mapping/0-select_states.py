#!/usr/bin/python3
"""Exercise
"""

if __name__ == '__main__':

    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host='localhost', argv[1], argv[2], argv[3], port=3306)
    cur = db.cursor()

    cur.execute('SELECT * FROM states ORDER BY id ASC')
    for row in cur.fetchall():
        print(row)

    db.close()
