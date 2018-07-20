class Ninja:
# underscore hoa_is_handsome
# cammel case HoaIsHandsome
    
    #  ham tao - constructor
    def __init__(self,name,strength,defense,hp):
        self.name = name
        self.strength = strength 
        self.defense = defense
        self.hp = hp
    def print(self):
        print(self.name)
        print(self.strength)
        print(self.defense)
        print(self.hp)
    def attack(self, other):
        hp_loss = self.strength - other.defense/2
        if hp_loss >= 0 :
            other.hp = other.hp - hp_loss


ninja1 = Ninja("Kakashi", 7, 9, 10) # n : object 
# thiet ke - design = class 
# khoi cong xay dung = object 
ninja2 = Ninja("Itachi", 4, 10, 10) 


print("**********")


print("{0} is attacking {1}".format(n.name,m.name))
n.attack(m)
m.print()


