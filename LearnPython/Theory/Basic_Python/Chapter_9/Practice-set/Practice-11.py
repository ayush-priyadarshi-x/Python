import os

def removeFile(fileName):
    os.remove(fileName)
    print(f"File deleted successfully: {fileName}")

# Open and read the content of "this.txt" before deleting it
with open("this.txt", "r") as f:
    content = f.read()

# Delete the original file
removeFile("this.txt")

# Create a new file and write the content into it
with open("renamed_by_python.txt", "w") as w:
    w.write(content)
