#!/usr/bin/python3
"""Exercise
"""

if __name__ == '__main__':
    
    import MySQLdb
    from sys import argv
    """COnect
    """
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()

    cur.execute('SELECT * FROM states ORDER BY id ASC')
    for row in cur.fetchall():
        print(row)

    db.close()
