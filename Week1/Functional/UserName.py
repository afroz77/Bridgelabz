template = "Hello <<UserName>> How Are You !"
print(template)
Username = input("Enter User Name : ")
while len(Username) <= 2:
    Username = input("Enter Valid User Name : ")
print(template.replace("<<UserName>>", Username))