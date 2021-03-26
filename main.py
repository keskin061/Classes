class Dog:
    def __init__(self, name):
        self.name = name

    def sit(self):
        print(self.name + "is sitting")


class SARDog(Dog):
    def __init__(self, name):
        super().__init__(name)

    def search(self):
        print(self.name + "is searching")


snoop = Dog("Snoop")
sniffy = SARDog("Sniffy")

print(f"{snoop.name} & {sniffy.name} are both great dogs")
sniffy.sit()
sniffy.search()
