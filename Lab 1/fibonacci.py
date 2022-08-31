#Programa para generar la Sucesión de Fibonacci hasta n
n=int(input("Enter the value of 'n': "))
#los dos primeros términos son primero y segundo
first=0
second=1
sum=0
count=1
print("Fibonacci Sequence: ")
# El conteo no debe ser mayor que n.
while(count<=n):    
  print(sum)
  count+=1
  first=second
  second=sum
  sum=first+second	
