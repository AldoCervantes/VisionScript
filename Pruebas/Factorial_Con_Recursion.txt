text again = "yes"

number function factorial(number n)
begin
    number fact = 0
    if n equal 0
    begin
        return(1)
    else
        return (n * factorial(n-1))
    end
end 

number n = 0

repeat until again equal "no" or again equal "n" or again equal "N" or again equal "NO" or again equal "No"
begin
    print("Introduzca numero: ")
    read(n)

    print("factorial: ")
    print(factorial(n))
   
    print(" ")

    print("Quieres hacer otro calculo?")
    read(again)
    print(" ")
end