username_passwords= {
"Ahmed":"1394",
"Ali":"6078",
"Amr":"9345"
}
username=input("please,enter your username :")
password=input("please,enter the password : ")

if username in username_passwords :
    if(username_passwords[username]==password):
       print("Welcome {}".format(username))
    else:
       print("Wrong Password")
else:
   print("wrong username")
