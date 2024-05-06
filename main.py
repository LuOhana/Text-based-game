"""class Employee:

 def __init__(self, fname, lname):
   self.fname = fname
   self.lname = lname

 def get_name(self):
   return self.fname + " " + self.lname


class Programmer(Employee):
  def __init__(self, fname, lname, role, salary):
   super().__init__(fname, lname)
   self.role = role
   self._salary = salary

  def details(self):
   print(f"{self.fname},{self.lname},{self.role}")

  @property
  def salary(self):
    return ", salary: ", self._salary

  @salary.setter
  def salary(self, new_salary):
    self._salary = new_salary

person = Programmer("John", "Doe", "Software Engineer", "100000")
person.salary("200000")
person.details
person.salary_value"""

from room import Room
from chest import Chest

kitchen = Room("kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies")
ballroom = Room("ballroom")
ballroom.set_description("A vast room with a shiny wooden floor")
dining_hall = Room("dining hall")
dining_hall.set_description("A large room with ornate golden decorations")

#the room you're linking FROM is the object you call the method on, 
#and the room you are linking TO is the object you pass into the method
kitchen.link_room(dining_hall, "south")  
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom,"west")
ballroom.link_room(dining_hall,"east")

current_room = kitchen


#setting up my chests
wooden_chest = Chest("wooden chest")
wooden_chest.set_chestinfo("A falling-appart wooden chest. It doesn't seem valuable. Type 'open' to check it")
kitchen.set_items(wooden_chest)


silver_chest = Chest("silver chest")
silver_chest.set_chestinfo("A dusty chest ornated in silver. Type 'open' to check it")
ballroom.set_items(silver_chest)

golden_chest = Chest("gold chest")
golden_chest.set_chestinfo("A beautiful golden chest covered in spider webs. Type 'open' to check it")
dining_hall.set_items(golden_chest)

#chests contents
wooden_chest.set_treasure("10 coins")
silver_chest.set_treasure("2 rubies and a black key")
golden_chest.set_treasure("1 diamond and 50 coins")


while True: #unconditional iteration or infinite loop
    print("\n")
    current_room.get_details()
    current_room.get_items()
    command = input("> ")
    current_room = current_room.move(command)






