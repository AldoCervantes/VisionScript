number i = 0
number n = 0 
number cont = 0
number temp = 0
container a = [0,1]

print("Cual es el numero que desea encontrar:")
read(n)
 
repeat until i >= n - 1 
begin
    temp = a.get(i) + a.get(i + 1)
    a.insert_back(temp)
    i = i + 1
end

print("Respuesta:")
print(a.get_back())

print(" ")

print("Contenedor:")
print(a)