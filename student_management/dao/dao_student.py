from student_management.dao.dao_set import DaoSet as dao


class StudentDao(dao):
  def __init__(self):
    self.conn = self.conn_db()
    self.cursor = self.conn.cursor()

  def get_all(self):
    try:
      conn = self.conn_db()
      c = conn.cursor()
      rs = c.execute("select * from student ")
      return rs.fetchall()
    except Exception as e:
      print(e)
    finally:
      self.conn.close()


def insert_one(self, std):
  try:
    self.cursor.execute(f"insert into student (id, name, pass) "
                      f"values('{std.id}','{std.name}','{std.pw}') ")
    self.conn.commit()
    return self.cursor.lastrowid
  except Exception as e:
    print(e)
  finally:
    self.conn_close()

def login_check(self, std):
  try:
    rs = self.cursor.execute(f"insert into student "
                           f"where id={std.id}, and pass = {std.pw} ")
    return rs.fetchone()
  except Exception as e:
    print(e)
  finally:
    self.conn_close()
