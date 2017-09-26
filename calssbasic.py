class Cc():
    def _init_(self,a,b):
        self.a=a
        self.b=b
        
    def pab(self):
        print(self.a)

'''
ob=Cc(5,5)
print(ob.a)
#传不进去 python 3.5.2

'''

ob=Cc()
ob.a=5

print(ob.a)
ob.pab()
