container a = [false,true,1,2,3,4,5,6,7,"Aldo","$"]

text find = ""

print("De que tipo es el elemento que quieres buscar: (T -> Text, N -> Number y B -> Bool) ")
read(find)

number num = 0
bool bo = false
number i = 0
bool encontrado = false
number pos = 0

if find equal "T"
begin
  print("Escribe qué texto quieres que busque:")
  read(find)
  repeat until i >= a.length()
  begin
    if a.get(i) equal find
    begin
      encontrado = true
      pos = i
      i = a.length()
    else
      i = i + 1
    end
  end
else
  if find equal "N"
  begin
    print("Escribe qué número quieres que busque:")
    read(num)
    repeat until i >= a.length()
    begin
      if a.get(i) equal num
      begin
        encontrado = true
        pos = i
        i = a.length()
      else
        i = i + 1
      end
    end
  else
    if find equal "B"
    begin
      print("Escribe que bool quieres que busque:")
      read(bo)
      repeat until i >= a.length()
      begin
        if a.get(i) equal bo
        begin
          encontrado = true
          pos = i
          i = a.length()
        else
          i = i + 1
        end
      end
    else
      print("Lo siento, el tipo de dato que solicitas no es válido")
    end
  end
end

if encontrado
begin
  print("Encontre tu elemento en la posición:")
  print(pos)
else
  print("El elemento no está dentro del contenedor")
end
