with open ("test2.txt","a+")as file:
    file.write("hey/n howareyou?/nletshangout")
    file.close()
    
with open ("test2.txt","r+")as file:
    print(file.read())


with open ("test3.txt","w+")as file1:
    file1.write("hey/n howareyou?/nletshangout")
    file1.close()
with open ("test3.txt","r+")as file1:
    print(file1.read())

with open ("test3.txt","r+")as file2:
    print(file2.read()) 
with open ("test3.txt","w+")as file2:
    file2.write("hey/n howareyou?/nletshangout")   
    
    
