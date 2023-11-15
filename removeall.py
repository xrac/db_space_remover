import sqlite3
con = sqlite3.connect("../../Downloads/bdLUZ.dmn.sqlite")
cur = con.cursor()
cur2 = con.cursor()
cur3 = con.cursor()
res = cur.execute("SELECT name FROM sqlite_schema WHERE type ='table' AND name NOT LIKE 'sqlite_%';")
#print(res.fetchall())
for name in res:
  table = ''.join(name)
  print(f'------------Table: {table}-----------')
  if(' ' in table):
    newname = table.replace(' ', '')
    print(table + newname)
    cur.execute(f'ALTER TABLE \'{table}\' RENAME TO {newname};')  
  res1 = cur2.execute(f'SELECT name FROM PRAGMA_TABLE_INFO(\'{table}\')')
  for name1 in res1:
    column = ''.join(name1)
    print(column)
    if(' ' in column):
      newcolname = column.replace(' ','')
      print(f'Rename {column} >>>>> {newcolname} ')
      cur3.execute(f'ALTER TABLE \'{table}\' RENAME COLUMN \'{column}\' TO \'{newcolname}\';');

    
