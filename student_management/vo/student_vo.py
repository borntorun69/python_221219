class student:

  #id
  @property
  def id(self):   return self.__id
  @id.setter
  def set_id(self, id): self.__id = id
  @id.getter
  def get_id(self):  return self.__id
  #name
  @property
  def name(self):   return self.__name
  @name.setter
  def set_name(self, name): self.__name = name
  @name.getter
  def get_name(self):  return self.__name
  #pw
  @property
  def pw(self):   return self.__pw
  @pw.setter
  def set_pw(self, pw): self.__pw = pw
  @pw.getter
  def get_pw(self):  return self.__pw

  def __init__(self, id, name, pw):
    self.__id = id
    self.__name = name
    self.__pw = pw
