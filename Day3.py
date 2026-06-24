print("Welcome to the treasure Island!")
turn = input("The road you were walking on now diverges into two turns, the left one looks scary and mysterious and the right one seems out of the ordinary, very silent and calm. Which path do you want to go? 'Left' or 'Right'")
turn0 = turn.lower()
if turn0 == "right":
    print("You got eaten by a monster hiding on a tree. Game Over.")
elif turn == "left":
        turn2 = input("You found an Abondened Castle. Would to go into the castle or turn back? type 'castle' or 'turn back' ")
        turn1 = turn2.lower()
        if turn1 == "castle":
              print("Congrats! you found the Treasure.")
        else:
            print("You got stuck in an infinity loop inside while returning and died out of hunger. Game Over.")
else:
      print("Wrong input. Game Over.")