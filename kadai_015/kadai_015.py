class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def printonfo(self):
        print("名前:", self.name)
        print("年齢:", self.age)
   
#　インスタンス化する
user = Human("侍太郎", 36,)
    
    
#　属性にアクセスし、値を出力する
print(user.name)
print(user.age)
