import random

print("Welcome to the Terminal RPG...")
health = 100
confirm = False

while confirm != True:
    player_name = input("\nEnter your player name: ")
    print(f"\nYour chosen name is {player_name}...")
    proceed = int(input('Enter 1 if this is correct, 2 to re-enter: '))

    if proceed == 1:
        confirm = True

print("\nPlease pick a weapon from the following -")
print("\n1. Sword (Consistent damage, 15 per hit)")
print("\n2. Staff (Variable damage, 10 to 30 per hit)")

confirm = False

while confirm != True:
    weapon = int(input("\nWhat's your weapon of choice? "))
    print(f"\nYour chosen name is Option {weapon}...")
    proceed = int(input('\nEnter 1 if this is correct, 2 to re-enter: '))

    if proceed == 1:
        confirm = True


print("\nAnd so, {player_name} embarks on their journey in the terminal with just a {weapon} in hand...")
print("Oh...and $100")


print("------------------------------------------------------------------------------------------------")

print("As you are navigating through the unknown domain, you encounter a strange stone. ")
print("\n'It looks like a rock', you think to yourself. But you are a curious being after all...")

print("\nChoose an action: ")
print("1. Investigate the rock.")
print("2. Break the rock.")
print("3. Ignore the rock and continue.")

choice = int(input("\nWhat will you do? "))

while choice > 3 or choice < 0:
    print("Invalid option.")
    choice = int(input("What will you do? "))


if choice == 1:
    print("You choose to investigate the rock...")
    print("To your surprise, the rock is sentient! It turns around and tells you it needs help!")
    print("Strange Rock : I need you to give me all of your money, or I will fight you.")

    print("Option 1: Fight the rock. ")
    print("\nOption 2. Give the rock all of your money.")
    choice = int(input("What will you do? "))

if choice == 2:
    print("You try to break the rock, but it dodges your move. ")
    print("The rock then morphs into a human-like figure, and takes a fighting stance.")
    rock_health = 30

    while health > 0 and rock_health > 0:
        rock_attack = random.randint(1,10)
        if weapon == 1:
            player_attack = 15
        else:
            player_attack = random.randint(10,30)
