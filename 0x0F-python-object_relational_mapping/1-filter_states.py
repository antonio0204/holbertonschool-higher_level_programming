#!/usr/bin/python3
"""filter_states."""
if __name__ == '__main__':

    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    cur.execute("""SELECT * FROM states WHERE name
                 LIKE BINARY 'N%' ORDER BY states.id ASC""")
    lines = cur.fetchall()
    for line in lines:
        print(line)
