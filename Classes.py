#creating a class based on animal -dog
class Dog:
    #next the atrributes pertaing to the dog-like its features
    #attributes:name,breed,colour
    #self is a key word
    #def __init__ is a function also known as a constrcuor 
    #2 underscoures next to init
    def __init__(self, name, breed, colour):
        self.name = name
        self.breed = breed
        self.colour = colour
     #getter   
    def getName(self):
        return self.name
    #setter
    def setname(self,name):
        self.name =name 
    
    def getbreed(self):
        return self.breed
    
    def setbreed(self,breed):
        self.breed =breed
    
    def getcolour(self):
        return self.colour
    
    def setcolour(self,colour):
        self.colour =colour
        
#creating an object of the above class,we calling the __init__ function now
myDog = Dog("Max","Pug","Black")

print('The dogs name is', myDog.getName())
#we used the setter to change the dogs name lol (setters allow us to change the atrributes )
myDog.setname("Pablo")

print('The dogs name has been changed to', myDog.getName())
#lets now chnage the breed and color of theu dog 
myDog.setbreed("Pitbull")
print('Dogs Breed: ' ,myDog.getbreed())

myDog.setcolour("Brown")
print('Dogs color: ', myDog.getcolour())

""" 
my_doggy = Dog("Alex", " ", "brown")
my_doggy.setbreed('Dalmation')

print(my_doggy.getbreed()) """