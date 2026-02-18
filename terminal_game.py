import random

print("Welcome to the Terminal RPG...")

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
    proceed = int(input('\nEnter 1 if this is correct, 2 to re-enter'))

    if proceed == 1:
        confirm = True




