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
    hear("Introduce el número del que quieres saber su factorial: ")
    read(n)

    hear("la factorial de")
    hear(n)
    hear("es")
    hear(factorial(n))

    hear("¿Quiéres hacer otro cálculo?")
    read(again)
end