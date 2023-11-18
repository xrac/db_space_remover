import sqlite3
con = sqlite3.connect("../../Descargas/bdLUZ.dmn.sqlite")
cur = con.cursor()
cur2 = con.cursor()
cur3 = con.cursor()
res = cur.execute("SELECT name FROM sqlite_schema WHERE type ='table' AND name NOT LIKE 'sqlite_%';")
#print(res.fetchall())
for name in res:
  table = ''.join(name)
  newname = ''
  print(f'------------Table: {table}-----------')
  if(' ' in table): newname = table.replace(' ', '')
  if('ó' in table): newname = table.replace('ó', 'o')
  if(newname!=''):
    print(table + newname)
    cur.execute(f'ALTER TABLE \'{table}\' RENAME TO {newname};')  

  res1 = cur2.execute(f'SELECT name FROM PRAGMA_TABLE_INFO(\'{table}\')')
  for name1 in res1:
    column = ''.join(name1)
    newcolname = ''
    print(column)
    if(' ' in column): newcolname = column.replace(' ','')
    if('ñ' in column): newcolname = column.replace('ñ','n')
    if('ú' in column): newcolname = column.replace('ú','u')
    if('ó' in column): newcolname = column.replace('ó','o')
    if('í' in column): newcolname = column.replace('í','i')
    if('é' in column): newcolname = column.replace('é','e')
    if('á' in column): newcolname = column.replace('á','a')
    if(newcolname!=''):
      print(f'Rename {column} >>>>> {newcolname} ')
      cur3.execute(f'ALTER TABLE \'{table}\' RENAME COLUMN \'{column}\' TO \'{newcolname}\';');
