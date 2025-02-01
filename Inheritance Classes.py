class Automobile:
 # The _ _init_ _method accepts arguments for the make, model, mileage, and price. It initializes
 # the data attributes with these values.

    def __init__(self, make, model, mileage, price):
        self._make = make
        self._model = model
        self._mileage = mileage
        self._price = price

    # The following methods are mutators for the class's data attributes.

    def set_make(self, make):
        self._make = make

    def set_model(self, model):
        self._model = model

    def set_mileage(self, mileage):
        self._mileage = mileage

    def set_price(self, price):
        self. _price = price

    # The following methods are the accessors for the class's data attributes.
    def get_make(self):
        return self. _make

    def get_model(self):
        return self. _model

    def get_mileage(self):
        return self._mileage

    def get_price(self):
        return self._price

class Car(Automobile):
    # The _ _init_ _ method accepts arguments for the car's make, model, mileage, price, and doors.

    def __init__(self, make, model, mileage, price, doors):
        # Call the superclass's _ _init_ _ method and pass the required arguments. Note that we also have
        # to pass self as an argument.
        Automobile.__init__(self, make, model, mileage, price)
        # Initialize the _ _doors attribute.
        self.__doors = doors

    # The set_doors method is the mutator for the  _ _doors attribute.
    def set_doors(self, doors):
        self.__doors = doors

    # The get_doors method is the accessor for the _ _doors attribute.
    def get_doors(self):
        return self.__doors
    
    def set_price(self, price):
        self._price = price

    def get_price(self):
        return self._price

my_car = Car('Audi', 2007, 12500, 0 , 4)

# Display the car's data.
print('Make of car:', my_car.get_make() )
print('Model of car:', my_car.get_model(), 'km' )
print('Mileage:', my_car.get_mileage() )
print('Number of doors:', my_car.get_doors() )

#car_1 = Car('nissan', 'evo', '165km', 'R1.6 milliom', '4 doors')
my_car.set_price(20000)
print('The price of the car is R',my_car.get_price())





