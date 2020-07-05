# anonymous function
f=lambda a:a%2==0

nums = [1,2,3,4,5,56,7]
evens = list(filter(f,nums))
print(evens)