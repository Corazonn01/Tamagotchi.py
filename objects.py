def main():
    pet_name = input("What is the name of your pet? ")
    pet_type = input("What kind of pet do you want to have? ")

    #creating a pet
    my_pet = Pet(pet_name, pet_type)
    input("Hello human! My name is " + my_pet.name +  ". Please, press enter to start the game!")

    choice = None
    while choice != 0:
        print("""
            *** Please choose an action ***

            1: Feed your pet 
            2: Talk with your pet 
            3: Teach your pet 
            4: Play with your pet
            0: Exit the game
            
        """)
        break

    choice = input("What is your choice? ")
    if choice == '0':
        print("Good bye!")
    elif choice == '1':
        my_pet.feed()
    elif choice == '2':
        my_pet.speak()
    elif choice == '3':
        new_word = input("What do you want to teach me? ")
        my_pet.teach(new_word)
    elif choice == '4':
        my_pet.play()
    else:
        print("Sorry that is not a valid option")
main()
