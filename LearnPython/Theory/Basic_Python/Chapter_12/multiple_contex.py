# Using multiple context managers to open two files at once
with open('file1.txt', 'r') as file1, open('file2.txt', 'w') as file2:
    content = file1.read()
    file2.write(content)
