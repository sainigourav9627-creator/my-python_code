#1 se 20 tak numbers print karo.
#Agar number Even ho to print karo:
#Agar number Odd ho to print karo:
#Aur saath me ye bhi batao ki number 3 se divisible hai ya nahi

for i in range(1,11):

    if i % 2 == 0:

        if i % 3 == 0:
            print(i,"Even Divisible by 3")

        else:
            print(i,"Even Not Divisible by 3")

    else:

        if i % 3 == 0:
            print(i,"Odd Divisible by 3")

        else:
            print(i,"Odd Not Divisible by 3")
