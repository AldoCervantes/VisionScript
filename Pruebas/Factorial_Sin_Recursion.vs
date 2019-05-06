number i = 1
number fact = 1
number numero = 0

print("ingresa un numero: ")
read(numero)

if numero < 0
begin
  fact = 0
else
  if numero equal 0 
  begin
    fact = 1
  else
    repeat until i > numero
    begin
        fact = fact * i
        i = i + 1
    end
  end
end

print("Factorial:" )
print(fact)