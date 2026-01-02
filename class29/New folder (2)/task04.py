myfile=open("text.txt","w")
myfile.write("hi my name is charul.\n i am in nagpur")
myfile.close()
myfile=open("text.txt","r")

print(myfile.read())
myfile.seek(0)
