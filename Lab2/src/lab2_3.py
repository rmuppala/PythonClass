
class Flight(object): #class 1

  def __init__(self, no, frm, tol ,date , dep, arr):
      self.flightNo = no
      self.source = frm
      self.destination = tol
      self.flightDate = date
      self.departure = dep
      self.arrival = arr



class Person(object): #class 2

    def __init__(self,name, age, contact):
        self.name  = name
        self.age = age
        self.phno = contact

class Employee(Person): # class 3 single inheritance

    def __init__(self,per, salary, title):
        Person.__init__(self,per.name, per.age, per.phno)
        self.salary = salary
        self.title = title

class Food(object): #class 4
    def __init__(self, meal, type, price):
        self.meal = meal
        self.type = type
        self.price = price

class Passenger(Person, Flight): #class 5 multiple inheritance Person, Flight
    def __init__(self,person, flight): #constructor passing person flight object
        Person.__init__(self,person.name, person.age, person.phno)
        Flight.__init__(self, flight.flightNo, flight.source, flight.destination ,flight.flightDate , flight.departure, flight.arrival)


    def foodOrdered(self, food): # setting food object
        self.food = food

    def passengerDetails(self):
        print("\nPassenger Name : " + self.name + ", Age : " + self.age + ", Contact : " + self.phno )
        print("Traveling in flight : " + self.flightNo + " From :" + self.source + " To: " + self.destination +  " Date : " + self.flightDate + " Dep : " + self.departure + " Arr : " + self.arrival)
        print("FoodOrdered : ", self.food.meal + ", " + self.food.type + ", price " + str(self.food.price))

def main():
        person1 = Person("Tina", "32", "5673891730") #instance of Person class
        person2 = Person("Robert" , "45" , "9234567890")
        person3 = Person("Bill", "29", "9765478908")

        flight1 = Flight("AI120", "Denver", "Kansas" ,"02/15/2018" , "12:30 AM", "4:30 PM") #instance of Flight class

        food1 = Food("Breakfast", "snack", 3) #instance of Food class
        food2 =  Food("Lunch", "Veg", 0)

        employee1 = Employee(person1,50000,"Crew") #instance of Employee class
        employee2 = Employee(person2,75000,"Pilot")

        passenger1 = Passenger(person3,flight1) #instance of Passenger class

        passenger1.foodOrdered(food2)
        passenger1.passengerDetails()


if __name__ == "__main__":
    main()