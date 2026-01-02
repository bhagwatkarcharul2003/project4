#file = open ("demofile.txt","x")
file = open ("demofile.txt","r")

print(file.readlines())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())

file.close