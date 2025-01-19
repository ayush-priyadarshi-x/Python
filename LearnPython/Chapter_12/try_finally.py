def main(): 
    try:
        file = open('example.txt', 'r')
        content = file.read()
        print(content)
        return
    except FileNotFoundError:
        print("File not found!")
        return
    finally:
        file.close()  # Ensures the file is closed no matter what
        print("File has been closed.")

main()