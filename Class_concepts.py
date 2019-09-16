
class Computer:
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("Configuration is ", self.cpu, self.ram)


comp1 = Computer('i4','8gb')
comp2 = Computer('i5','16gb')
comp1.config()
comp2.config()


