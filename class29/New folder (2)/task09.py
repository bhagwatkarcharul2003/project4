#write mode
f=open("newfile1.txt","w")
f.write("hey everone ")
f.writelines(["95116113"])
f.close()
f=open("newfile1.txt","r")
print(f.read())

