class Computer: 
    def __init__(self, CPU, RAM):
        print("Inilitallizing...")
        self.cpu = CPU
        self.ram = RAM
    
    def config(self):
        print(f"{self.cpu} || {self.ram}")


comp1 = Computer("i5", 8)
comp1.config()

print("\n")

comp2 = Computer("i7", 9 )
comp2.config()


