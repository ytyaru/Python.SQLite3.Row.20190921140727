import sqlite3

con = sqlite3.connect(":memory:")
con.row_factory = sqlite3.Row
cur = con.cursor()
cur.execute('create table T(i integer, r real, t text, b blob);')
sql = 'insert into T values(?, ?, ?, ?)'
datas = [(0, 0.1, 'A', 'A'.encode('utf-8')),(1, 1.1, 'B', 'B'.encode('utf-8')),]
cur.executemany(sql, datas)
rows = cur.execute("select rowid,* from T;")
for i,row in enumerate(rows):
    print(str(i) + '----------------')
    print('rowid: {}'.format(row['rowid']))
    print('i:     {}'.format(row['i']))
    print('r:     {}'.format(row['r']))
    print('t:     {}'.format(row['t']))
    print('b:     {}'.format(row['b']))

