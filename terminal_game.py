import random

print("Welcome to the Terminal RPG...")
health = 100
money = 100.0
exp = 0.0
confirm = False

while confirm != True:
    player_name = input("\nEnter your player name: ")
    print(f"\nYour chosen name is {player_name}...")
    proceed = int(input('Enter 1 if this is correct, 2 to re-enter: '))

    if proceed == 1:
        confirm = True

print("\nPlease pick a weapon from the following -")
print("\n1. Global Sword (Consistent damage, 15 per hit)")
print("\n2. Local Staff (Variable damage, 10 to 30 per hit)")

confirm = False

while confirm != True:
    weapon = int(input("\nWhat's your weapon of choice? "))
    print(f"\nYour chosen name is Option {weapon}...")
    proceed = int(input('\nEnter 1 if this is correct, 2 to re-enter: '))

    if proceed == 1:
        confirm = True

print("\nAnd so, {player_name} embarks on their journey in the terminal with just a {weapon} in hand...")
print("Oh...and $100")
print("Goal - Try to finish with as much money and health as possible.")
print("And of course, stay alive.")


print("------------------------------------------------------------------------------------------------")
game_in_progress = True
while health > 0 and game_in_progress == True:

    print("As you are navigating through the unknown domain, you encounter a strange stone that looks like a series of boxes. ")
    print("\n'It looks harmless!', you think to yourself. But you are a curious being after all...")

    print("\nChoose an action: ")
    print("1. Investigate the stone.")
    print("2. Break the stone.")
    print("3. Ignore the stone and continue.")

    choice = int(input("\nWhat will you do? "))

    while choice > 3 or choice < 0: 
        print("Invalid option.")
        choice = int(input("What will you do? "))


    if choice == 1:
        print("You choose to investigate the stone...")
        print("To your surprise, the stone is sentient! It turns around and tells you it needs help!")
        print("Strange Rock : I need you to give me all of your money, or I will fight you.")

        print("\nOption 1. Give the stone all of your money.")
        print("Option 2: Fight the stone. ")
        choice = int(input("What will you do? "))

    if choice == 2:
        print("\nYou try to break the stone, but it dodges your move. ")
        print("The stone then morphs into a human-like figure, and takes a fighting stance.")
        rock_health = 30

        while health > 0 and rock_health > 0:
            rock_attack = random.randint(1,10)
            if weapon == 1:
                player_attack = 15
            else:
                player_attack = random.randint(10,30)

            print("\nOption 1: Attack!")
            print("Option 2. Defend!")
            attack = int(input("Choose action: "))
            if attack == 1:
                rock_health -= player_attack
                print(f"\nYou have dealt {player_attack} damage to the enemy!")
                health -= rock_attack
                print(f"Enemy has dealt {rock_attack} damage to you!")
            if attack == 2:
                print(f"\nThe rock tried to deal {rock_attack} damage and failed!")

    if health <= 0:
        print("You have been defeated. Game over!")
        break
    if health > 0 and choice == 2:
        print("\nYou have successfully defeated the strange rock!")
        money_gained = random.randint(10,30)
        print(f"You gained ${money_gained}!")
        money += money_gained
        print(f"You have {health} hp and ${money} remaining...\n")

    if choice == 3:
        print("You evaded the stone, which turned out to be a strange sentient creature.\n")

    print("You continue moving forward through the terminal domain. There is a door in front of you...")
    print("'Pay $50 to proceed.' reads the sign. \n")
    print("You have two options:")
    print("\nOption 1: Pay the cost and proceed.")
    print("Option 2: Look for an alternative method.\n")

    choice = int(input("Pick an option: "))
    while choice != 1 and choice != 2:
        print("Invalid option, try again.")
        choice = int(input("Pick an option: "))

    if choice == 1:
        print(f"\nYou pay the cost. Now you have ${money-50} left.")
        money -= 50
    elif choice == 2:
        print("\nYou look around you and see a window. You also see a being that looks like they should have been guarding the door, but they are asleep.")
        print("\nOption 1: Break through the window.")
        print("Option 2: Search the guard.")

        choice = int(input("\nPick an option: "))
        while choice != 1 and choice != 2:
            print("Invalid option, try again.")
            choice = int(input("Pick an option: "))
    
        if choice == 1:
            print(f"\nYou break through the window but hurt yourself in the process. You now have {health-50} health.")
            print(f"$50 is also missing from your pocket...You have ${money-50} left.")
        if choice == 2:
            print("You search the guard for a key...\n")
            print("Suddenly, the guard jolts awake, and pulls out a gun.")
            guard_health = 80
            while health > 0 and guard_health > 0:
                guard_attack = random.randint(10,30)
                if weapon == 1:
                    player_attack = 15
                else:
                    player_attack = random.randint(10,30)

                print("\nOption 1: Attack!")
                print("Option 2. Dodge!")
                attack = int(input("Choose action: "))
                if attack == 1:
                    guard_health -= player_attack
                    print(f"You have dealt {player_attack} damage to the enemy!")
                    print(f"The guard has {guard_health} hp left.")
                    health -= guard_attack
                    print(f"Enemy has dealt {guard_attack} damage to you!")
                    print(f"You have {health} hp left.")
                if attack == 2:
                    print(f"The guard tried to deal {guard_attack} damage and failed!")
            if health <= 0:
                print("You have been defeated. Game over!")
                break
            if health > 0 and choice == 2:
                print("\nYou have successfully defeated the guard!")
                money_gained = random.randint(10,30)
                print(f"You gained ${money_gained}!")
                money += money_gained
                print(f"You have {health} hp and ${money} remaining...\n")
    
    print("\nYou have reached the end of the domain...")
    print("In front of you, there is a portal back to the real universe.")
    print("However, it takes a great toll on your health in order to go through it.")
    print("It takes 75 hp to get through the portal, but you can also purchase 0.5 hp for every $1")
    print(f"You currently have {health} hp and ${money}.")
    print("\nOption 1. Go through the portal.")
    print("Option 2: Purchase HP.")
    choice = int(input("Pick an option: "))

    if choice == 2:
        hp_available = 0.5 * money
        print(f"\nYou have purchased {hp_available} hp with ${money}")
        money = 0
        health += hp_available
    
    health -= 75
    game_in_progress = False
    

if health > 0:
    print("\nYou have successfully made it out of the domain and back to the real world. Congratulations.\n")
else:
    print("\nYour soul remains stuck in the domain forever...\n")
            

    

