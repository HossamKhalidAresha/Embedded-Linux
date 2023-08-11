vowel="eaiou"
letter=input("please,enter a letter : ")
if(vowel.find(letter.lower())!=-1):
    print("{} is a vowel".format(letter))
else:
     print("{} is not a vowel".format(letter))
