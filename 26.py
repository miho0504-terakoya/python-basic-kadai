#　継承
class SushiShop:
    feature_val = ""
    mc_val = ""
    
    
    def __init__(self, name):
        #コントラクタ
        self.name = name
        
    def feature(self):
        print(self.feature_val)
        
    def main_character(self):
        print(self.mc_val)


class Kura(SushiShop):
    feature_val = "びっくらポン"
    mc_val = "元はダウンタウン"
    

class Hama(SushiShop):
    feature_val = "5種の全国厳選醤油"
    mc_val = "川口春奈"
        



# 回転寿司

class Kura:
    def __init__(self, name):
        self.name = name
        
    def feature(self):
        print("びっくらポン")
        
    def main_character(self):
        print("元はダウンタウン")
        

class Hama:
    def __init__(self, name):
        self.name = name
        
    def feature(self):
        print("5種の全国厳選醤油")
        
    def main_character(self):
        print("川口春奈")

        
shops =  []
   
kura_umeda = Kura("梅田店")
kura_nanba = Kura("難波店")
hama_shinagawa = Hama("品川店")

shops.append(kura_umeda)
shops.append(kura_nanba)
shops.append(hama_shinagawa)

for shop in shops:
    print(shop.name)
    shop.feature()
    shop.main_character()
    