class animal:

    alive = True

    def eat(self):
        print("this animal is eating")

    def sleep(self):
        print("this animal is sleeping")

class Rabbit(animal):
    
    def run(self):
        print("this rabbit is runing")
class Fish(animal):
    
    def swim(self):
        print("this fish is swiming")
class Hawk(animal):
    
    def flying(self):
        print("this hawk is flying")

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

#print(rabbit.alive)
#fish.eat()
#hawk.sleep()

rabbit.run()
fish.swim()
hawk.flying()