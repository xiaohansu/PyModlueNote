from ZODB import FileStorage,DB
import transaction

class MyZODB(object):
    def __init__(self,path):
        self.storage = FileStorage.FileStorage(path)#存储数据库数据的方法
        self.db = DB(self.storage)#围绕存储并为存储提供实际数据库行为“db”包装
        self.connection = self.db.open()#启动与该数据库的特定会话的“connection”对象
        self.dbroot = self.connection.root()#允许我们访问包含在数据库中的对象层次结构的根的“dbroot”对象
    
    def close(self):
        self.connection.close()
        self.db.close()
        self.storage.close()


if __name__ == '__main__':
    db = MyZODB('./Data.fs')
    dbroot = db.dbroot
    dbroot['a_number'] = 3
    dbroot['a_string'] = 'gift'
    dbroot['a_list'] = [1, 2, 3, 5, 7, 12]
    dbroot['a_dictionary'] = { 1918: 'Red Sox', 1919: 'Reds' }
    dbroot['deeply_nested'] = {
    1918: [ ('Red Sox', 4), ('Cubs', 2) ],
    1919: [ ('Reds', 5), ('White Sox', 3) ],
    }
    transaction.commit()
    db.close()