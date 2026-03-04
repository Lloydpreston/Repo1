#  *if/elif/else age verification test*

#   This code will determine wether a user is allowed to enter using "if/else" with the criteria being 18 or 16 with adult supervision.

user_age = 20
required_age = 18
adult_supervision = 16

if user_age >= required_age:
    print("Allowed to enter")

elif user_age >= 16:
    print("Adult supervision required")

else:
    print("Denied access")
