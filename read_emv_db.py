import sqlite3
from sqlite3 import Error
from texttable import Texttable

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def select_all(conn):
    cur = conn.cursor()
    cur.execute("SELECT a.model, b.region_name, c.tag_name, c.version_xpath, c.tag_name_xpath FROM emv_ver_xpath AS c LEFT JOIN device AS a ON a.id = c.device_id LEFT JOIN device_region AS b ON b.id = device_region_id")

    rows = cur.fetchall()

    rows.insert(0, ['DEVICE', 'REGION', 'TAG NAME', 'VERSION XPATH', 'TAG NAME XPATH'])

    table = Texttable()
    table.set_deco(Texttable.HEADER)
    table.set_cols_dtype(['t', 't', 't', 't', 't'])  # text
    table.set_cols_width([10, 10, 50, 85, 85])

    table.set_cols_align(["l", "l", "l", "l", "l"])
    table.add_rows(rows)
    print(table.draw())

def main():
    database = r"emv_ver_xpath.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        select_all(conn)

if __name__ == '__main__':
    main()