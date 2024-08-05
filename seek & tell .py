with open('File-IO-IN-PYTHON/file.txt', 'r') as f:
    print(type(f))

   # move the 10th byts in the file
    f.seek(10)

   #read the next 5 byts
    data = f.read(5)
    print(data)

    with open('File-IO-IN-PYTHON/sample.txt', 'w') as f:
        f.write('Hello World!')
        f.truncate(3)

with open('File-IO-IN-PYTHON/sample.txt', 'r') as f:
    print(f.read())