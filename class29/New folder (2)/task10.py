f=open("newfile1.txt","a")
f.write("hey everyone ")#in write we can only use string a-z
f.writelines(["/n95116113"])#in writeline only int and float allowed
f.close()

f=open("newfile1.txt","r")
f.seek(5)
print(f.read())
f.close()
