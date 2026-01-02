
with open ("test1.txt","w")as file:
    file.write("hey\n how are you?\n lets hang out")

with open ("test1.txt","r")as file:
    print(file.read())
with open ("test1.txt","r")as file:
    file.truncate(5)  
      

