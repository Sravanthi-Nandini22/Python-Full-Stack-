#List of items using for loop

products = ['bread', 'butter', 'milk', 'sugar', 'salt']
for product in products:
    print(f'{product}_ Add to fav |Buy now |Add to cart')


# Tuple of items using for loop

sizes = ('xs', 's', 'm', 'l', 'xl', 'xxl', 'xxl')

for s in sizes:
    print(f'...|{s}|...')

# set of items using for loop

followers = {'Saaketh', 'Swapnil', 'Dileep', 'Varsha', 'Satwik'}
for i in followers:
    print(f'{i}- |follow back|remove|message|')

# Dict of items using for loop

data = {
    'Varsha': ['C', 'Python', 'Java'],
    'Abhi' : ['ML', 'AI', 'Python'],
    'saaketh' : ['Java', 'Linux', 'Python'],
    'sirisha' : ['Figma', 'UXUI', 'Python']
    }
for i in data:
    print(f'{i}: {data[i]}')

# String of items using for loop

 s = 'Python_programming'
 for i in s:
     print(i)

#range(start,stop+1,step) = range(0,n,1)
for i in range(1,11):
    print(i)

# To print only even numbers
for i in range(2,101,2):
    print(i)

#To print only odd numbers
for i in range(1,100,2):
    print(i)

#To print 3 multiples
for i in range(3, 100, 3):
    print(i)

#To print reverse of a number
for i in range(10, 1,-1):
    print(i)

#To print a table
n = int(input('Enter the number: '))
print(f'{n}_Table
for i in range(1,11):
      print(f'{n}*{i} ={n*i}')

#Break and Continue

for i in range(1,10):
    if(i==7):
      break
    print(i)

for i in range(1,10):
    if(i==7):
        continue
    print(i)

#Using while loop to print

i = 1
while i<=10:
    print(i)
    i = i+1
      
      
      
      
      


    

    
