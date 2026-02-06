print ('Welcome to Nirmala horse riding'.title())

name = input('Enter your name:')
age = int(input('Enter your age:'))
bill = 0
if age<5:
          print(f'Sorry {name} you will not allow into Hose Riding')
elif age>=5 and age<=10:
    bill += 100
elif age>=11 and age<=15:
    bill += 120
elif age>=16 and age<=20:
    bill += 150
else:
    bill += 200
print(f'Hello {name.upper()} Welcome to Horse Riding')
photos = input('Do you want to take photos while riding(y/n):')
if photos == 'y':
    bill = bill+20
    
print('Your total bill is:', float(bill))
print('Thank you, Visit again')
  

          
