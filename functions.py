import json
import tkinter
from random import randrange
from tkinter import messagebox

import easygui

root = tkinter.Tk()
root.withdraw()
messagebox.showinfo("Alert", "You dont have a pet yet! Lets create it!")
messagebox.showinfo("Default version", "Hello human! My name is Thomas! I am a medium orange cat!")

# default version
default_characteristics = {"name": "Thomas", "color": "orange", "size": "medium", "type": "cat"}

response = easygui.buttonbox("Would you like to change these characteristics?", choices=["Yes", "No"])
if response == "Yes":
    new_name = easygui.enterbox("Choose name: ", default=default_characteristics["name"])
    new_type = easygui.enterbox("Choose new type: ", default=default_characteristics["type"])
    new_color = easygui.enterbox("Choose a color: ", default=default_characteristics["color"])
    new_size = easygui.enterbox("Choose size: ", default=default_characteristics["size"])

    characteristics = {'name': new_name, "color": new_color, "size": new_size}
else:
    characteristics = default_characteristics

easygui.msgbox(f"'Pet's characreristics': {characteristics}")


class Pet:
    excitment_reduce = 3
    excitment_max = 10
    excitment_warning = 3
    food_reduce = 2
    food_max = 10
    food_warning = 3
    vocab = ['"Grrrr..."']

    def __init__(self, name, pet_type):
        self.pet_type = pet_type
        self.name = name
        self.food = randrange(self.food_max)
        self.isHappy = randrange(self.excitment_max)
        self.vocab = self.vocab[:]

    def __clock__tick(self):
        # by this function we can decrease their excitment and fullness by time
        self.isHappy -= 1
        self.food -= 1

    def mood(self):
        if self.food > self.food_warning > self.excitment_warning:
            return "Happy"
        elif self.food < self.food_warning:
            return "Hungry"
        else:
            return "Boring"

    def __str__(self):
        return self.name + "feels" + self.mood() + "."

    def teach(self, word):
        self.vocab.append(word)
        self.__clock__tick()

    def speak(self):
        print("I am: " + self.pet_type + " but my person calls me: " + self.name + ". " + "Also I feel " + self.mood())

        print(self.vocab[randrange(len(self.vocab))])
        self.__clock__tick()

    def feed(self):
        print("Mmmm...Thank you!")
        meal = randrange(self.food,
                         self.food_max)  # here we take the amount of food between current food and the max amount of
        # the food
        self.food += meal

        if self.food < 0:
            self.food = 0
            print("I am dying of hunger")
        elif self.food > self.food_max:
            self.food_max = self.food
            print("I am full")
            self.__clock__tick()

    def play(self):
        print("Let's play!")
        game = randrange(self.isHappy, self.excitment_max)
        self.isHappy += game

        if self.isHappy < 0:
            self.isHappy = 0
            print("I am soooo boreed!")
        elif self.isHappy > self.excitment_max:
            self.isHappy = self.excitment_max
            print("I am happy!")
            self.__clock__tick()


print("Keys in characteristics:", characteristics.keys())
my_pet = Pet(name=characteristics['name'], pet_type=characteristics.get('type'))


with open("tamago.json", "w") as file:
    pet_data = {
        "name": my_pet.name,
        "pet_type": my_pet.pet_type,
        "food": my_pet.food,
        "isHappy": my_pet.isHappy,
        "vocab": my_pet.vocab
    }
    json.dump(pet_data, file)
