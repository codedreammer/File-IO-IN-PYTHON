'''
f = open('File-IO-IN-PYTHON/myFile.txt', 'r')

text = f.read()
print(text)
f.close()

f = open('File-IO-IN-PYTHON/myFile2.txt', 'r')

text = f.read()
print(text)
f.close()

f = open('File-IO-IN-PYTHON/myFile3.txt', 'w')

text = f.write()
print(text)
f.close()
'''
f = open('File-IO-IN-PYTHON/myFile3.txt', 'w')
f.write('Hello, world! ')
f.close()

with open('File-IO-IN-PYTHON/myFile3.txt', 'a') as f:
    f.write("Hey I as inside with")
