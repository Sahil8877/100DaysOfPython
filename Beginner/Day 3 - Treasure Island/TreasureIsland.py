print(r'''
                  
                               _ooOoo_
                              o8888888o
                              88" . "88
                              (| -_- |)
                              O\  =  /O
                           ____/`---'\____
                         .'  \\|     |//  `.
                        /  \\|||  :  |||//  \
                       /  _||||| -:- |||||_  \
                       |   | \\\  -  /'| |   |
                       | \_|  `\`---'//  |_/ |
                       \  .-\__ `-. -'__/-.  /
                     ___`. .'  /--.--\  `. .'___
                  ."" '<  `.___\_<|>_/___.' _> \"".
                 | | :  `- \`. ;`. _/; .'/ /  .' ; |
                 \  \ `-.   \_\_`. _.'_/_/  -' _.' /
       ===========`-.`___`-.__\ \___  /__.-'_.'_.-'================
                               `=--=-'                    
      ''')
print("Welcome to Treasure Island\nYour mission is to find the treasure.")
ready = input("Are you ready? y/n :\n").lower()
if ready == "y":
    direction = input("You are at a crossroad.\nDo you want to go right or left ? r/l :\n").lower()
    if direction == "r":
        print("You were attacked by the pirates. Game Over.")
    elif direction == 'l':
        mode = input("You are at the bank of a river.\nDo you want to swim to other side or wait ? s/w :\n").lower()
        if mode == "s":
            print("You were attacked by an Alligator. Game Over.")
        elif mode == "w":
            door = input("Your standing in front of Red, Blue and Yellow coloured gates.\nWhich door you want to open ? r/b/y :\n").lower()
            if door == 'r':
                print("A huge fire erupted. Game Over.")
            elif door == 'b':
                print("You were eaten by a beast. Game Over.")
            elif door == 'y':
                print("Congratulation! You found the treasure.")
            else:
                print("Sorry wrong input!")
        else:
               print("Sorry wrong input!")
    else:
        print("Sorry wrong input!")
else:
    print("Its alright, Thanks.")
            