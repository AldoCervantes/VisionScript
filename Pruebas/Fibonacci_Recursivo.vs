number function funcionFibonacci(number num)
begin
    if num equal 0 or num equal 1
    begin
        return(num)
    else
        return(funcionFibonacci(num - 1) + funcionFibonacci(num -2))
    end
end

number cont = 0

print("Cual es el numero que desea encontrar:")
read(cont)
print(funcionFibonacci(cont))


