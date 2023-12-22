# Tamagotchi.py
from random import randrange

class Pet:
    excitment_reduce = 3
    excitment_max = 10
    excitment_warning = 3
    food_reduce = 2
    food_max = 10
    food_warning = 3
    vocab = ['"Grrrr..."']

    def __init__(self, name, animal_type):
        self.name = name
        self.animal_type = animal_type
        self.food = randrange(self.food_max)
        self.isHappy = randrange(self.excitment_max)
        self.vocab = self.vocab[:]

    def __clock__tick(self):
        #by this function we can decrease their excitment and fullness by time
        self.isHappy -= 1
        self.food -=1

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
        self.__clock__tick() #it should be reduced because while we teach smth it costs

    def speak(self):
        print("I am: " + self.animal_type + " but my person calls me: " + self.name + ". " + "Also I feel " + self.mood())

        print(self.vocab[randrange(len(self.vocab))])
        self.__clock__tick()


    def feed(self):
        print("Mmmm...Thank you!")
        meal = randrange(self.food, self.food_max) #here we take the amount of food between current food and the max amount of the food
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
