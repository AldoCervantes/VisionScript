number function join(number x , number y, number z, number r)
begin
    return(x + y)
end

number function less(number x, number y)
begin
    return(join(5,5,x,y))
end

number function add(number x, text y, bool z, container o)
begin
    number a = 20
    less(x,1)
    print(a)
    a = a + x - 1
    print(a)
    return( less(1,2) + less(1,2) )
end


number a = add(16,"2",true,[])
print(a)
