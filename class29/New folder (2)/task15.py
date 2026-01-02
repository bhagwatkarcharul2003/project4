#write
'''a=open("text.txt5","w")
a.write("my name is charul\ni love playing games")
a.writelines(["\n i love cooking","\n7559298"])
print(a.seekable())
print(a.writable())
a.close()'''
#read
a=open("text.txt5","r")
print(a.read())
a.seek(0)
print(a.readline())
a.seek(0)
print(a.readlines())
a.seek(0)
print(a.readable())
print(a.seekable())
print(a.tell())
#a.close()
