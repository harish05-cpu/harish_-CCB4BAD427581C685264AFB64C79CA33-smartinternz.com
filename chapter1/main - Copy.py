year=int(input('enter year:'))
if(year%4==0andyear%100!=0)or(year%400==0):
    print(year,"is a leap year.")
else:
    print(year,"is not a leap year.")
