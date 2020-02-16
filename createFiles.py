import os

f1 = open('C:\\Senthil\\py\\1.txt' ,'r')
out1 = f1.read()
# print(out1)
f2 = open('C:\\Senthil\\py\\2.txt' ,'r')
out2 = f2.read()

output = out1 +" " + out2

f3 = open('C:\\Senthil\\py\\3.txt' ,'w')
f3.write(output)
f3.close()
f4 = open('C:\\Senthil\\py\\3.txt' ,'r')
f5 = f4.read()
print(f5)

f1.close()
f2.close()
f3.close()

