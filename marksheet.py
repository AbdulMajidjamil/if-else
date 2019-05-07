eng=int(input("Enter marks of English: "))
chem=int(input("Enter marks of Chemistry: "))
sin=int(input("Enter marks of Sindhi: "))
pst=int(input("Enter marks of Pakistan Studies: "))
comp=int(input("Enter marks of Computer: "))
total_eng= 75
total_chem=100
total_pst=75
total_sin=75
total_comp=100
total_marks=425
percent= (eng+chem+sin+pst+comp)*(100/425)
print("Your Percentage is :", percent)
if percent>=80:
    print("Your Grade is A1")
elif percent>=70:
    print("Your Grade is A")
elif percent>=60:
    print("Your Grade is B ")
elif percent>=50:
    print("Your Grade is C ")
else:
    print("You are fail") 




