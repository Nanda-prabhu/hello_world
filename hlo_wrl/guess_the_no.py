import random
print("Ready to guess the number ?? \n Enter a range...")
small=int(input("Enter a samller no."))
large=int(input("Enter a larger no."))
mynum=random.randint(small,large)
cnt=0
while True:
    cnt+=1
    user_no=int(input("Enter the number u've guessed :"))
    if(user_no > mynum):
        print("Too Large")
    elif(user_no < mynum):
        print("Too Small") 
    else:
        print("you've got it in ",cnt,"tries!!!")
        break   