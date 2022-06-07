print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
name3=name1+name2
name3=name3.lower()
count1=0
count2=0
for i in name3:
    if (i=='t' or i=='r' or i=='u' or i=='e'):
        count1+=1
    if (i=='l') or (i=='o') or (i=='v') or (i=='e'):
        count2+=1
score=str(count1)+str(count2)
#print(score)
if (int(score)<10 or int(score)>90):
    print("Your score is " +(score)+", you go together like coke and mentos.")
elif (int(score)>=40 and int(score)<=50):
    print("Your score is " +(score)+", you are alright together.")
else:
    print("Your score is " +(score)+".")
