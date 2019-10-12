email = input("enter your e-mail id\n").strip()

name = email[:email.index('@')]
domain = email[(email.index('@')+1):]

op = "User name is {} and domain is {}".format(name, domain)
print(op)
