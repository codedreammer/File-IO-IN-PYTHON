
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
