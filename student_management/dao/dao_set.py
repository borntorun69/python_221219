import sqlite3

class DaoSet:
  def conn_db(self):
    self.conn = sqlite3.connect(
      'd:/classPython/workspace/python_221219/db.sqlite'
      , isolation_level=None)
    return self.conn


def conn_close(self):
  try:
    if self.conn != None:
      self.conn.close()
  except Exception as e:
    print(e)
