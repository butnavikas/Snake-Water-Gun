import random 

computer = random.choice([1, 2, 3])

print('''
        WELCOME TO SNAKE WATER GUN GAME
        CHOOSE FROM SNAKE(🐍), WATER(💧) & GUN(🔫)
        FOR SNAKE(🐍) TYPE s
        FOR WATER(💧) TYPE w
        FOR GUN(🔫) TYPE g
        ''')

user_input = input("enter your choice: ").lower()
youdict = {"s": 1, "g": 2, "w": 3}
reversedict = {1: "snake", 2: "gun", 3: "water"}


try:

    you = youdict[user_input] 
except KeyError:
 
    print("❌ Invalid input! You must type 's', 'w', or 'g'.")
    exit()

print(f"\nYOU CHOSE: {reversedict[you]}")
print(f"COMPUTER CHOSE: {reversedict[computer]}")

if computer == you:
    print("IT'S A DRAW 🤝")

elif (computer == 1 and you == 3) or \
     (computer == 3 and you == 2) or \
     (computer == 2 and you == 1):
    print("YOU LOSE! 😔")
else:
    print("YOU WON! 🥳")