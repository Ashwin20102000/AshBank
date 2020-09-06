'''
we are going to create the bank app
1. Balance
2. withdrawl
3. deposit 
4 . quit
'''
print('''
Welcome To AshBank : 
1. Balance
2. Withdrawl
3. Deposit 
4. Statement
5. Quit
''')
a=0
Amount = 10000 #intializing Money

while a<=4: #going for applicable process
  a=int(input()) #input for operation
  if a==1:
    print(f"Your Amount in the Bank is : $.{Amount}")
    # break
  if a==2:
    withDrawl = float(input("Enter the with drawl Amount : $")) #withdrawl
    if withDrawl < Amount:
      Amount-=withDrawl
      print(Amount)
      # break
    else:
      print("Not Efficient Money")
  if a==3:
    deposit = float(input("Enter the Deposit Amount : $")) #deposit
    if deposit <= 30000:
      Amount+=deposit
      print(Amount)
      # break
    else:
      print("Dont go over 30000")  
  if a==4:
    print(f'''
    Amount = {Amount}
    WithDrawl = -{withDrawl}
    Deposit = +{deposit}
    ''')
  if a==5:
    break
