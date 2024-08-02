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

f = open('File-IO-IN-PYTHON/myFile3.txt', 'w')
f.write('Hello, world! ')
f.close()

with open('File-IO-IN-PYTHON/myFile3.txt', 'a') as f:
    f.write("Hey I as inside with")


f = open('File-IO-IN-PYTHON/work.txt', 'w')
f.write('56,45,67\n12,34,63\n13,64,56')
f.close()
'''
f = open('File-IO-IN-PYTHON/work.txt', 'r')
i = 0
while True:
    i += 1
    line = f.readline()
    if not line:
        break
    m1 = line.split(",")[0]
    m2 = line.split(",")[1]
    m3 = line.split(",")[2]
    print(f"marks of student {i} in maths is: {m1}")
    print(f"marks of student {i} in english is: {m2}")
    print(f"marks of student {i} in SST is: {m3}")
    print(line)

f.close()

