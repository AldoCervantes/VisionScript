number function partition(container arr, number low, number high)
begin 
  number i = low - 1
  number pivot = arr.get(high)
  number j = low
  number temp = 0

  repeat until j >= high
  begin
    if arr.get(j) <= pivot
    begin
        i = i + 1
        temp = arr.get(j)
        arr.replace(j , arr.get(i))
        arr.replace(i,temp)
    else
    end
    j = j + 1
  end

  temp = arr.get(high)
  arr.replace(high, arr.get(i + 1 ))
  arr.replace(i + 1 , temp)
  
  return(i+1)
end  

void function quickSort(container arr, number low, number high)
begin
  number pi = 0
  if low < high
  begin
    pi = partition( arr, low, high)
    quickSort (arr,low, pi - 1 )
    quickSort (arr,pi + 1,high)
  else
  end
end


container arr = [10,0,7,6,3,2,1,9,8,5,4]
number low = 0
number high = arr.length() - 1 
  
quickSort(arr,low,high) 
print(arr)