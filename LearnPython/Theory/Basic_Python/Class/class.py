class communicate: 
    def greet(self): 
        print("Hello Someone")



hello_1 = communicate()
hello_2 = communicate()

communicate.greet(hello_1)
communicate.greet(hello_2)

hello_1.greet()
hello_2.greet()