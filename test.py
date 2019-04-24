myMap = {}
cont = 30000
def ConstDeclaration(myMap , VarType , value):
        if VarType == 'number':
            float(value) 
        if value not in myMap:
                myMap[value] = [VarType,cont]
        return myMap[value][1]


ConstDeclaration(myMap,'number','2.3')
cont = cont + 1
ConstDeclaration(myMap,'number','2')
cont = cont + 1
ConstDeclaration(myMap,'bool','false')
cont = cont + 1
ConstDeclaration(myMap,'bool','true')
cont = cont + 1
ConstDeclaration(myMap,'text','"Aldo"')
cont = cont + 1
ConstDeclaration(myMap,'text','"2.3"')
cont = cont + 1

for key , value in myMap.items():
    print(key,"=>",value)
    print("______________")



