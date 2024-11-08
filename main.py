import os
import sys
import random


while True:
    print("""
 ▄▄· ▄▄▄   ▄· ▄▌.▄▄ · ▄▄▄▄▄ ▄▄▄· ▄▄▌   ▄▄▄·      ▪    ▐ ▄ ▄▄▄▄▄
▐█ ▌▪▀▄ █·▐█▪██▌▐█ ▀. •██  ▐█ ▀█ ██•  ▐█ ▄█▪     ██  •█▌▐█•██  
██ ▄▄▐▀▀▄ ▐█▌▐█▪▄▀▀▀█▄ ▐█.▪▄█▀▀█ ██▪   ██▀· ▄█▀▄ ▐█· ▐█▐▐▌ ▐█.▪
▐███▌▐█•█▌ ▐█▀·.▐█▄▪▐█ ▐█▌·▐█ ▪▐▌▐█▌▐▌▐█▪·•▐█▌.▐▌▐█▌ ██▐█▌ ▐█▌·
·▀▀▀ .▀  ▀  ▀ •  ▀▀▀▀  ▀▀▀  ▀  ▀ .▀▀▀ .▀    ▀█▄▀▪▀▀▀ ▀▀ █▪ ▀▀▀                    
""")
    from User import User

    # prints the basic introduction
    print("Hello Adventurer, Welcome to CrystalPoint: Where you can choose your fate." + "\n")
    name = input("What is your name: ")
    print("\n" + "Hello " + str(
        name) + ". Welcome to the game! You will be given choices that will determine life or death." + "\n" + "Every decision matters. This is you!")
    print("""
        *     *      ☺|                *        
   *                /|   *     *
  _________________ / \ _________________
""")
    print("Ready? Let's get started. Happy Adventures!" + "\n")
    user_friend = input(
        "Just so you're not completely alone, enter the first name of your friend: ")
    # choose number to determine how much money they have
    money_number = input("Pick a number between 1-3: ")

    while not money_number.isnumeric() or int(money_number) < 1 or int(money_number) > 3:
        print("Please enter a number between 1-3")
        money_number = input("Pick a number between 1-3: ")

    # Initializing money and health values and a list of all items in your pocket
    money = 0
    health = 300
    pocket = []

    if int(money_number) == 1:
        money = 300
    elif int(money_number) == 2:
        money = 500
    elif int(money_number) == 3:
        money = 400

    user = User(name, money, health)


    # defines functions for when user wins or loses
    def lose():
        print("""
  _______      ___      .___  ___.  _______      ______   ____    ____  _______ .______      
 /  _____|    /   \     |   \/   | |   ____|    /  __  \  \   \  /   / |   ____||   _  \     
|  |  __     /  ^  \    |  \  /  | |  |__      |  |  |  |  \   \/   /  |  |__   |  |_)  |    
|  | |_ |   /  /_\  \   |  |\/|  | |   __|     |  |  |  |   \      /   |   __|  |      /     
|  |__| |  /  _____  \  |  |  |  | |  |____    |  `--'  |    \    /    |  |____ |  |\  \----.
 \______| /__/     \__\ |__|  |__| |_______|    \______/      \__/     |_______|| _| `._____|




    """)

        game_over = input("Would you like to try again? (Y or N): ")
        while not game_over.isalpha or game_over.upper() != "Y" or game_over.upper() != "N":
            if game_over.upper() == "Y" or game_over.upper() == "N":
                break
            print("Please enter Y or N.")
            game_over = input("Would you like to try again? (Y or N): ")
            if game_over.upper() == "Y" or game_over.upper() == "N":
                break
        if game_over.upper() == "N":
            print("""
*           *      *
     *         *               *
 *     Thanks for Playing!  *         *
      *           *
   *                     *         *
      """)
            quit()
        elif game_over.upper() == "Y":
            os.execl(sys.executable, sys.executable, *sys.argv)


    def win():
        print("""
____    ____  ______    __    __     ____    __    ____  __  .__   __.  __  
\   \  /   / /  __  \  |  |  |  |    \   \  /  \  /   / |  | |  \ |  | |  | 
 \   \/   / |  |  |  | |  |  |  |     \   \/    \/   /  |  | |   \|  | |  | 
  \_    _/  |  |  |  | |  |  |  |      \            /   |  | |  . `  | |  | 
    |  |    |  `--'  | |  `--'  |       \    /\    /    |  | |  |\   | |__| 
    |__|     \______/   \______/         \__/  \__/     |__| |__| \__| (__) 


    """)
        game_over = input("Would you like to play again? (Y or N): ")
        while not game_over.isalpha or game_over.upper() != "Y" or game_over.upper() != "N":
            if game_over.upper() == "Y" or game_over.upper() == "N":
                break
            print("Please enter Y or N.")
            game_over = input("Would you like to play again? (Y or N): ")
            if game_over.upper() == "Y" or game_over.upper() == "N":
                break
        if game_over.upper() == "N":
            print("""
*           *      *
     *         *               *
 *     Thanks for Playing!  *         *
      *           *
   *                     *         *
      """)
            quit()
        elif game_over.upper() == "Y":
            os.execl(sys.executable, sys.executable, *sys.argv)


    print("\n" + "Congratulations you chose number " + str(money_number) + ", and you won " + str(
        user.money) + "!" + "\n" + "\n" + "You will use this money in the game to buy supplies at any shops you may come across. Make sure you spend your money well." + "\n" + "\n" + "Also... Small detail, you only have 300 health. If you lose it all, you die ... I also won't be telling you your health so maybe try to remember it?" + "\n")

    print("You begin your journey and are immediately greeted with a fork in the road. Do you go right or left?")
    print("""

\     \      /     /
 \     \    /     /
  \     \  /     /
   \     \/     /
    \          /
     \        /
      |   O   |
      |  /|\  |
      |  / \  |

""")

    # First decision choosing right or left
    crossroad = input("Choose your direction (R or L): ")
    while crossroad.upper() != "R" or crossroad.upper() != "L":
        if crossroad.upper() == "R" or crossroad.upper() == "L":
            break
        print("Please input R or L.")
        crossroad = input("Choose your direction (R or L): ")
        if crossroad.upper() == "R" or crossroad.upper() == "L":
            break

    # choose to go right
    if crossroad.upper() == "R":
        print(
            "\n" + "You have chosen to proceed right." + "\n" + "You walk for a bit down the path and see something just past the trees...")

        print("""

              ********
            ****************
          *******************
          ********************   
          ********************** 
        *****\\   //  ********  
          *** \\\\//  *******    
              \\\////   
           O   |||//    
         /|\   |||||     
         / \  //||||\    


  """)
        print(
            "At last! you've found some sort of shop! The salseman shows you his inventory and there are three things to choose from. (If you do not wish to purchase anything, input the number 4.)")

        print("""
  **********************

    1- 1x Knife  $30
    2- 1xApple   $20
    3- 1xShield  $100

  **********************
  """)

        print()
        # validates and colects user choice for item purchase
        weapon_choose = input("Input the item number of the one you wish to buy: ")
        while not weapon_choose.isnumeric() or int(weapon_choose) < 1 or int(weapon_choose) > 4:
            print("Please enter a number between 1-4")
            weapon_choose = input("Input the item number of the one you wish to buy: ")

        # chose knife
        if int(weapon_choose) == 1:
            pocket.append("knife")
            user.money -= 30
            print("\n" + "You have bought the knife" + "\n")
        # chose apple
        elif int(weapon_choose) == 2:
            pocket.append("apple")
            user.money -= 20
            print("\n" + "You have bought the apple" + "\n")
        # chose shield
        elif int(weapon_choose) == 3:
            pocket.append("shield")
            user.money -= 100
            print("\n" + "You have bought the shield" + "\n")
        # didnt buy anything (option 4)
        else:
            print("\n" + "You did not buy anything" + "\n")
            pocket.append("none")

        print(
            "You thank the kind man for helping you out and continue along your journey. It's getting dark and cold... ")

        print("""
  *                 *    *
   *       *      *                  *   
     *          *       *         *      
          *     O
    *         /|\    *         * 
              / \\
  """)

        print(
            "Just then you hear a noise. You spot a tree with a glimmer of light coming from inside it. Impossible... What could be.....")

        print("""
     ___       __    __   __    __   __    __   __    __   __    __   __    __   __    __   __    __  
    /   \     |  |  |  | |  |  |  | |  |  |  | |  |  |  | |  |  |  | |  |  |  | |  |  |  | |  |  |  | 
   /  ^  \    |  |__|  | |  |__|  | |  |__|  | |  |__|  | |  |__|  | |  |__|  | |  |__|  | |  |__|  | 
  /  /_\  \   |   __   | |   __   | |   __   | |   __   | |   __   | |   __   | |   __   | |   __   | 
 /  _____  \  |  |  |  | |  |  |  | |  |  |  | |  |  |  | |  |  |  | |  |  |  | |  |  |  | |  |  |  | 
/__/     \__\ |__|  |__| |__|  |__| |__|  |__| |__|  |__| |__|  |__| |__|  |__| |__|  |__| |__|  |__| 


  """)
        print("You are confronted with the most terrifying creatures. Quick! What can you use to help yourself?" + "\n")
        # checks through list "pocket" for which item user bought
        # user bouht knife
        if "knife" in pocket:
            print(
                "Thankfully you bought that kniife! You use it against the goblins, but you got too close and one of them bit you! You lose 20 health." + "\n")
            user.health -= 20
        # user bought apple
        elif "apple" in pocket:
            print(
                "Thankfully you bought that apple! You pull it out of your bag and they seem to like it. You give them your apple and they go back into their little tree." + "\n")
        # user bought shield
        elif "shield" in pocket:
            print(
                "Thankfully you bought that shield! But wait, it looks like you got scammed! The shield is practically falling a part and it only took some of the hit. You lose 50 health." + "\n")
            user.health -= 50
        # user didnt buy anything which causes loss
        elif "none" in pocket:
            print(
                "You should have bought something... The goblins attack you from everywhere. There are just too many and you become overwhelmed.")
            lose()

        # after goblin attack
        print("Wow! That was scary! What's that?... It looks like one of the goblins left something behind.")
        print("""
            _____________
           /     __      /|
          /   __/ /_    / /
         /   /_  __/   / //
        /     /_/     / //
       /_____________/ //
       |______&______|//
       |_____________|/

    """)
        print("It seems to be a health kit...")
        # open health kit? validates and collects input
        open_health = input("Would you like to open it? (Y or N): ")
        while not open_health.isalpha() or open_health.upper() != "Y" or open_health.upper() != "N":
            if open_health.upper() == "Y" or open_health.upper() == "N":
                break
            print("Please enter Y or N.")
            open_health = input("Would you like to open it? (Y or N): ")
            if open_health.upper() == "Y" or open_health.upper() == "N":
                break
        # chose to open health pack
        if open_health.upper() == "Y":
            print("\n" + "You have been granted 10 health. Nice!" + "\n")
            user.health += 10
        # chose to not open health pack
        elif open_health.upper() == "N":
            print("I wonder what would have happened if you opened that... Oh Well! Lets continue on.")
            print("""

              ********
            ****************
          *******************
          ********************   
          ********************** 
        *****\\   //  ********  
          ***  \\\//  *******    
              \\\////   
               |||//          O
               |||||        /|\
              //||||\       / \


      """)
        print(
            "You continue on your treck. The birds are chirping, the sun is shining, theres a whining noise... There's a whining noise?" + "\n")
        print(
            "You hurry through the forest to find the noise and see a fairy that appears hurt. You can help her out by donating 10 health." + "\n")
        # user choice to help or leave fairy
        # collects and validates decision input
        help_fairy = input("Would you like to donate 10 health to help her? (Y or N): ")
        while not help_fairy.isalpha() or help_fairy.upper() != "Y" or help_fairy.upper() != "N":
            if help_fairy.upper() == "Y" or help_fairy.upper() == "N":
                break
            print("Please enter Y or N.")
            help_fairy = input("Would you like to donate 10 health to help her? (Y or N): ")
            if help_fairy.upper() == "Y" or help_fairy.upper() == "N":
                break
        # chose to help fairy
        if help_fairy.upper() == "Y":
            print("\n" + "The fairy thanks you for your help. She promises to help you on your last hurdle!")
            pocket.append("fairy")
            user.health -= 10
        # chose to leave fairy
        elif help_fairy == "N":
            print(
                "\n" + "You have chosen to ignore the fairy and you walk the other way, keeping your health. The fairy will remember that.")

        print(
            "\n" + "You continue your walk through the forest and it begins to get dark. You get a bit disoriented and see a wall of lights.")
        print("""
              _,-'|
           ,-'._  |
 .||,      |####\\ |
\\.`',/     \\####| |
= ,. =      |###| |
/ || \\    ,-'\\#/,'`.
  ||     ,'   `,,. `.
  ,|____,' , ,;' \\| |
 (3|\\    _/|/'   _| |
  ||/,-''  | >-'' _,
  ||'      ==\\ ,-'  ,'
  ||       |  V \\ ,|
  ||       |    |` |
  ||       |    |   \\
  ||       |    \\    \\
  ||       |     |    \\
  ||       |      \\_,-'
  ||       |___,,--")_\\
  ||         |_|   ccc/
  ||        ccc/
  ||                    


    """)
        print("A wizard emerges from the light and will let you pass... If you answer his question correctly." + "\n")
        # answer trivia and collects input to validate
        print(
            "Which one of these foods is poisonous?" + "\n" + "1. Elderberries" + "\n" + "2. Macadamia Nuts" + "\n" + "3. Durian" + "\n" + "4. Lutefisk" + "\n")
        poison = input("Enter the number that corresponds with the correct answer: ")
        while not poison.isnumeric() or int(poison) < 1 or int(poison) > 4:
            print("Please enter a number from 1-4.")
            poison = input("Enter the number that corresponds with the correct answer: ")
        # while wrong is inputted, takes health each time
        while not poison.isnumeric() or int(poison) != 1:
            while not poison.isnumeric() or int(poison) < 1 or int(poison) > 4:
                print("Please enter a number from 1-4.")
                poison = input("Enter the number that corresponds with the correct answer: ")
            if user.health <= 0:
                print("The wizard has taken all your health.")
                lose()

            print("\n" + "Incorrect answer. You lose 20 health." +"\n")
            user.health -= 20
            print(
                "Which one of these foods is poisonous?" + "\n" + "1. Elderberries" + "\n" + "2. Macadamia Nuts" + "\n" + "3. Durian" + "\n" + "4. Lutefisk" + "\n")
            poison = input("Enter the number that corresponds with the correct answer: ")

        print("\n" + "Good job! You look into the distance and see the end... It's so close.")
        print(
            "\n" + "You look forward and see a body of water blocking your way. This should be easy. Even easier if you could swim! (You can't btw)")
        print("""

    O
   /|\ 
___/ \______ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~___________

    """)
        print(
            "Alright, you have 2 options. You could try to swim across, or you could ask the nice man with the canoe beside you for a ride across the water for 30 health." + "\n")
        cross_river = input("Do you want to swim or ask the man (C=Canoe, S=Swim): ")
        while not cross_river.isalpha() or cross_river.upper() != "C" or cross_river != "S":
            if cross_river.upper() == "C" or cross_river.upper() == "S":
                break
            print("Please enter either C for Canoe or S for swim.")
            cross_river = input("Do you want to swim or ask the man (C=Canoe, S=Swim): ")
        if cross_river.upper() == "S":
            print(
                "\n" + "Well that went better than expected." + "\n" + "You entered the water and realized it was knee height. You walked across no problem!" + "\n")
        elif cross_river.upper() == "C":
            user.health = 0
            if user.health <= 0:
                print(
                    "\n" + "You get into the canoe and are immediately being dragged by the current. Oh look, a cliff! Oh no....")
                lose()

        print(
            "You see the end but it's at the bottom of a hill. You've been through so much already, this should be easy." + "\n")
        print("There's three ways down this hill.")
        print("Do you want to:" + "\n" + "1. Run down" + "\n" + "2. Slide down" + "\n" + "3. Roll down" + "\n")
        hill = input("Enter the number that corresponds with your choice: ")
        while not hill.isnumeric() or int(hill) < 1 or int(hill) > 3:
            print("Please enter a number from 1-3.")
            print("Do you want to:" + "\n" + "1. Run down" + "\n" + "2. Slide down" + "\n" + "3. Roll down" + "\n")
            hill = input("Enter the number that corresponds with your choice: ")
        if int(hill) != 2:
            print("You try getting down the hill, but get impaled by a large stick on your way down.")
            lose()

        print("You get down the hill safely and now you're even closer... There it is!")
        print("""
                    |>>>                        |>>>
                    |                           |
                _  _|_  _                   _  _|_  _
               | |_| |_| |                 | |_| |_| |
               \  .      /                 \ .    .  /
                \    ,  /                   \    .  /
                 | .   |_   _   _   _   _   _| ,   |
                 |    .| |_| |_| |_| |_| |_| |  .  |
                 | ,   | .    .     .      . |    .|
                 |   . |  .     . .   .  ,   |.    |
     ___----_____| .   |.   ,  _______   .   |   , |---~_____
_---~            |     |  .   /+++++++\    . | .   |         ~---_
                 |.    | .    |+++++++| .    |   . |              ~-_
              __ |   . |   ,  |+++++++|.  . _|__   |                 ~-_
     ____--`~    '--~~__ .    |++++ __|----~    ~`---,              ___^~-__
-~--~                   ~---__|,--~'                  ~~----_____-~'   `~----~    

    """)
        print(
            "You see the guardian at the entrance and freeze. The guardian is the marker of the end. A man of legends, the guardian decides who gets to pass. Let's hope he likes you!" + "\n")
        print("He needs you to make a decision.")
        print("From the shadows a person emerges. It is " + str(
            user_friend) + "! They went the wrong way and made a deal with the guardian..." + "\n")
        print("You must get this question right or else your friend dies.")
        print("**Please note that any wrong input will be taken as an answer"+ "\n")
        guardian_question = input("What can fill a room but takes up no space? ")
        while guardian_question.isspace() or guardian_question == "":
            print("Please enter a valid answer.")
            guardian_question = input("What can fill a room but takes up no space? ")

        if guardian_question.lower() == "light":
            print("\n" + "Light that's it. You are blinded by a bright white light.")
            win()

        elif "fairy" in pocket:
            print("\n" + "Oh no. That wasn't right...")
            print(
                "Just before you die, you see a small light. The fairy! She sees you in need and takes you and your friend out into the bright white light.")
            win()

        else:
            print(
                "\n" + "The guardian considers giving you another chance, but before that, he looks back at your life.")
            print(
                "One glance and he decides he doesn't like you very much. Looks like you should have helped that fairy after all!")
            lose()



    # choose to go left
    elif crossroad.upper() == "L":
        print("You have chosen to proceed left." + "\n")
        print(
            "You're so excited for the journey and start skipping along. The forest is so pretty this afternoon. Ah your first obstacle. What is it?" + "\n")
        print("There seems to be a bridge with an ugly man standing on it. Weird...")
        print("As you get closer he gets scarier. Sharp teeth, really large.. ")
        print("""
      .----.__
     /---.__  \\
    /       `\ |
    | o     o  \\|
  ./| .vvvvv.  |\\
 / /| |     |  | \\
//' | `^vvvv'  |/\\
~   \\          |  \\
    |          |   ~
     7        /
    /    .    |
    |_/\\/ `--.|


    """)
        talk_troll = input("Do you want to talk to the troll? (Y or N): ")
        while not talk_troll.isalpha() or talk_troll.upper() != "Y" or talk_troll.upper() != "N":
            if talk_troll.upper() == "Y" or talk_troll.upper() == "N":
                break
            print("Please enter Y or N")
            talk_troll = input("Do you want to talk to the troll? (Y or N): ")
            if talk_troll.upper() == "Y" or talk_troll.upper() == "N":
                break

        # talk to troll
        if talk_troll.upper() == "Y":
            print("\n" + "You have chosen to talk to the troll.")
            print("You approach him and he gets less intimidating.")
            print("To get over the bridge, you must answer the troll's trivia question." + "\n")

            print(
                "What is the fear of trolls called?" + "\n" + "a. Triskaidekaphobia" + "\n" + "b. Chronomentrophobia" + "\n" + "c. Pteridophobia" + "\n" + "d. Barophobia" + "\n")
            troll_trivia = input("Choose the letter that matches the answer: ")
            while not troll_trivia.isalpha() or troll_trivia.lower() not in ["a", "b", "c", "d"]:
                if troll_trivia.lower() in ["a", "b", "c", "d"]:
                    break
                print(
                    "What is the fear of trolls called?" + "\n" + "a. Triskaidekaphobia" + "\n" + "b. Chronomentrophobia" + "\n" + "c. Pteridophobia" + "\n" + "d. Barophobia" + "\n")
                troll_trivia = input("Choose the letter that matches the answer: ")
                if troll_trivia.lower() in ["a", "b", "c", "d"]:
                    break

            while troll_trivia.lower() != "a":
                while troll_trivia.lower() not in ["a", "b", "c", "d"] or not troll_trivia.isalpha():
                    print("\n" + "Please choose a,b,c or d." + "\n")
                    print(
                        "What is the fear of trolls called?" + "\n" + "a. Triskaidekaphobia" + "\n" + "b. Chronomentrophobia" + "\n" + "c. Pteridophobia" + "\n" + "d. Barophobia" + "\n")
                    troll_trivia = input("Choose the letter that matches the answer: ")

                print("\n" + "Sorry, that is the wrong answer. You lose 40 health." + "\n")
                user.health -= 40
                print(
                    "What is the fear of trolls called?" + "\n" + "a. Triskaidekaphobia" + "\n" + "b. Chronomentrophobia" + "\n" + "c. Pteridophobia" + "\n" + "d. Barophobia" + "\n")
                troll_trivia = input("Choose the letter that matches the answer: ")
                if user.health <= 0:
                    print("The troll has taken all of your health.")
                    lose()

            print("\n" + "Congratulations, you answered the riddle correctly.")
            print("Perfect, you've crossed the bridge at last! But wait... ")
            print("""

        O
       /|\\
       / \ 
--------------                               ----------------
             /                              /
            /                              /
            |                              |
            \\                              \\
            /                               \\
           /                                 \\
          /                                  |
      """)
            print("You begin to look around for materials, something, anything to help you cross.")
            print("After searching for a bit, you come across a small whimsical looking shop." + "\n")
            print(
                "The salseman shows you his inventory and there are three things to choose from. (If you do not wish to purchase anything, input the number 4.)")

            print("""
  *********************************

    1- 1x Rope               $30
    2- 1x Large Wood Plank   $20
    3- 1x Fairy Wings        $100

  *********************************
      """)
            item_choose = input("Input the item number of the one you wish to buy: ")
            while not item_choose.isnumeric() or int(item_choose) < 1 or int(item_choose) > 4:
                print("Please enter a number between 1-4.")
                item_choose = input("Input the item number of the one you wish to buy: ")

            # chose rope
            if int(item_choose) == 1:
                pocket.append("rope")
                user.money -= 30
                print("\n" + "You have bought the rope")
            # chose wood plank
            elif int(item_choose) == 2:
                pocket.append("wood")
                user.money -= 20
                print("\n" + "You have bought the large wood plank")
            elif int(item_choose) == 3:
                pocket.append("wings")
                user.money -= 100
                print("\n" + "You have bought the fairy wings")
            else:
                print("\n" + "You did not buy anything")
                pocket.append("none")

            print("Alright, time to try that again. You set up to cross the cliff and..." + "\n")

            if "rope" in pocket:
                print(
                    "You attach the rope to a tree branch and swing safely across. Good thinking! Not even a scratch!")
            elif "wood" in pocket:
                print(
                    "You set up the wood plank and it fits perfectly across the cliff! You begin to walk across, but you hear some cracking. Oh no!")
                print("""
________________
                \\
                |
                /              \O_
               /            ,/\/
              |               /
              /               \\
            /                `


        """)
                lose()

            elif "wings" in pocket:
                print(
                    "You attach the wings to your back and jump off the cliff. You close your eyes hoping for the wings to work... They never did.")
                lose()

            elif "none" in pocket:
                print(
                    "You can't do anything. You have no way to cross the cliff. You go back to the shop to buy something, but get mauled by a bear on your way.")
                lose()

            print(
                "\n" + "You've finally made it over the cliff. Thank god that's over. It looks like your journey is almost over!")
            print(
                "You look forward and see a body of water blocking your way. This should be easy. Even easier if you could swim! (You can't btw)")
            print("""

    O
   /|\ 
___/ \______ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~___________

      """)
            # breaks here prints infinite y or n message
            print(
                "Alright, you have 2 options. You could try to swim across, or you could ask the nice man with the canoe beside you for a ride across the water for 30 health." + "\n")
            cross_river = input("Do you want to swim or ask the man (C=Canoe, S=Swim): ")
            while not cross_river.isalpha() or cross_river.upper() != "C" and cross_river.upper() != "S":
                # if cross_river.upper()=="C" or cross_river.upper()=="S":

                # break
                print("\n" + "Please enter either C for Canoe or S for swim." + "\n")
                cross_river = input("Do you want to swim or ask the man (C=Canoe, S=Swim): ")
            if cross_river.upper() == "S":
                print(
                    "\n" + "Well that went better than expected. You entered the water and realized it was knee height. You walked across no problem!")

            elif cross_river.upper() == "C":
                user.health = 0
                if user.health <= 0:
                    print(
                        "\n" + "You get into the canoe and are immediately being dragged by the current. Oh look, a cliff! Oh no....")
                    lose()

            print("\n" + "Oh look! It's your friend " + str(user_friend) + ". You decide to continue together.")
            print(
                "You guys end up talking on your hike, and apparently your friend turned the other way at the beginning! So that's where they were! Oh well, at least you're together now.")
            print("You guys hike farther and begin to get hungry.")
            print("""
        ,,,                      ,,,
       {{{}}    ,,,             {{{}}    ,,,
    ,,, ~Y~    {{{}},,,      ,,, ~Y~    {{{}},,,
   {{}}} |/,,,  ~Y~{{}}}    {{}}} |/,,,  ~Y~{{}}}
    ~Y~ \|{{}}}/\|/ ~Y~  ,,, ~Y~ \|{{}}}/\|/ ~Y~  ,,,
    \|/ \|/~Y~  \|,,,|/ {{}}}\|/ \|/~Y~  \|,,,|/ {{}}}
    \|/ \|/\|/  \{{{}}/  ~Y~ \|/ \|/\|/  \{{{}}/  ~Y~
    \|/\\|/\|/ \\|~Y~//  \|/ \|/\\|/\|/ \\|~Y~//  \|/
    \|//\|/\|/,\\|/|/|// \|/ \|//\|/\|/,\\|/|/|// \|/
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

      """)
            print(
                "You come across a patch of berry plants and decide to pick them. They're red and look like little cranberries!")

            eat_berries = input("Do you want to eat them? (Y or N): ")
            while not eat_berries.isalpha() or eat_berries.upper() != "Y" and eat_berries.upper() != "N":
                print("Please enter Y or N.")
                eat_berries = input("Do you want to eat them? (Y or N): ")
            if eat_berries.upper() == "N":
                print("You starve to death.")
                lose()

            elif eat_berries.upper() == "Y":
                print(
                    "\n" + "You decide to eat them but your friend volounteers. I mean... Alright then. You don't try to stop them and they eat them all.")
                print("\n" + "What's happening? " + str(
                    user_friend) + " looks dizzy. They begin to clutch their stomach.. This can't be good. They hold their shoulder and begin looking pale.")
                print("""
  ______    __    __     .__   __.   ______    __  
 /  __  \  |  |  |  |    |  \ |  |  /  __  \  |  | 
|  |  |  | |  |__|  |    |   \|  | |  |  |  | |  | 
|  |  |  | |   __   |    |  . `  | |  |  |  | |  | 
|  `--'  | |  |  |  |    |  |\   | |  `--'  | |__| 
 \______/  |__|  |__|    |__| \__|  \______/  (__) 


        """)
                print("It looks like " + str(user_friend) + " is having a heart attack!")
                cpr = input("Quick! Do you know CPR? (Y or N): ")
                while not cpr.isalpha() or cpr.upper() != "Y" or cpr.upper() != "N":
                    if cpr.upper() == "Y" or cpr.upper() == "N":
                        break
                    print("Please enter Y or N.")
                    cpr = input("Quick! Do you know CPR? (Y or N): ")
                if cpr.upper() == "Y":
                    print("\n" + "Perfect! You get down and begin to perform CPR." + "\n")
                    breaths = input("How many breaths do you give? (Enter the number): ")
                    while not breaths.isnumeric():
                        print("Please enter a valid number.")
                        breaths = input("How many breaths do you give? (Enter the number): ")
                    print()
                    compressions = input(
                        "How many compressions do you give? (Enter the number): ")
                    while not compressions.isnumeric():
                        print("Please enter a valid number.")
                        compressions = input(
                            "How many compressions do you give? (Enter the number): ")
                    if int(breaths) == 2 and int(compressions) == 30:
                        print("\n" + "Well done! You have successfully saved your friend!")
                        user.health -= 50
                        print("However, you lost 50 health for almost killing them.")
                        if user.health <= 0:
                            print("\n" + "That took the last of your health.")
                            lose()

                    else:
                        print(
                            "\n" + "You tried to perform CPR but you didn't get it right. 2 breaths and 30 compressions was the correct way. Oh well...")
                        print("For murdering your friend, you get struck by lightning as karma.")
                        lose()

                elif cpr.upper() == "N":
                    print(
                        "\n" + "You don't know CPR and your friend dies. Moments later you get struck by lightning as karma.")
                    lose()

            print("\n" + "You can see the end... It's so close.")
            print("You see a treehouse marked \"EXIT\". That's convenient!")
            print("""
                         vv
                     vvv^^^^vvvvv
                 vvvvvvvvv^^vvvvvv^^vvvvv
        vvvvvvvvvvv^^^^^^^^^^^^^vvvvv^^^vvvvv
    vvvvvvv^^^^^^^^^vvv^^^^^^^vvvvvvvvvvv^^^vvv
  vvvv^^^^^^vvvvv^^^^^^^vv^^^^^^^vvvv^^^vvvvvv
 vv^^^^^^^^vvv^^^^^vv^^^^vvvvvvvvvvvv^^^^^^vv^
 vvv^^^^^vvvv^^^^^^vvvvv^^vvvvvvvvv^^^^^^vvvvv^
  vvvvvvvvvv^^^v^^^vvvvvv^^vvvvvvvvvv^^^vvvvvvvvv
   ^vv^^^vvvvvvv^^vvvvv^^^^^^^^vvvvvvvvv^^^^^^vvvvvv
     ^vvvvvvvvv^^^^vvvvvv^^^^^^vvvvvvvv^^^vvvvvvvvvv^v
        ^^^^^^vvvv^^vvvvv^vvvv^^^v^^^^^^vvvvvv^^^^vvvvv
 vvvv^^vvv^^^vvvvvvvvvv^vvvvv^vvvvvv^^^vvvvvvv^^vvvvv^
vvv^vvvvv^^vvvvvvv^^vvvvvvv^^vvvvv^v##vvv^vvvv^^vvvvv^v
 ^vvvvvv^^vvvvvvvv^vv^vvv^^^^^^_____##^^^vvvvvvvv^^^^
    ^^vvvvvvv^^vvvvvvvvvv^^^^/\@@@@@@\#vvvv^^^
         ^^vvvvvv^^^^^^vvvvv/__\@@@@@@\^vvvv^v
             ;^^vvvvvvvvvvv/____\@@@@@@\vvvvvvv
             ;      \_  ^\|[  -:] ||--| | _/^^
             ;        \   |[   :] ||_/| |/
             ;         \\ ||___:]______/
             ;          \   ;=; /
             ;           |  ;=;|
             ;          ()  ;=;|
            (()          || ;=;|
                        / / \;=;\      



      """)
            print(
                "You climb up the ladder but there is a passcode that protects the door. Lucky for you, there seems to be a hint as to what the combination is." + "\n")
            print("You see a list of jumbled numbers and at the top it says \"Ordered\".")
            print("""
****************
    Ordered  

  [10,87,23,51]

****************    

      """)
            print(
                "With some deductive reasoning, it's determined that you must type these numbers into the keypad in numerical order." + "\n")

            comp_keypad = ["10", "87", "23", "51"]
            user_keypad = []
            keypad = input(
                "Enter the numbers in numerical order as a singular number (Ex. 23875110): ")
            user_keypad.append(keypad)
            while not keypad.isnumeric() or len(keypad) != 8:
                print("Please enter a valid number.")
                keypad = input(
                    "Enter the numbers in numerical order as a singular number (Ex. 23875110): ")

            split = lambda s: (len(s) & 1 and [s[0]] or []) + [s[i - 1] + s[i] for i in range(len(s) - 1, 0, -2)][::-1]
            user_in_format = split(user_keypad[0])

            if user_in_format == sorted(comp_keypad):
                print("\n" + "Perfect, you got the combination correct!")
            else:
                print("\n" + "Really? C'mon, I can't let you continue after messing up that bad.")
                lose()

            print(
                "\n" + "You enter the treehouse and you are faced with the guardian. A man only heard of in legends, the guardian is the gatekeeper to the end.")
            print("\n" + "Easy enough, all he wants you to do is guess his random number from 1-10.")
            guardian_num = random.randint(1, 10)
            guardian_guess = input("Enter a number from 1-10: ")
            while not guardian_guess.isnumeric() or int(guardian_guess) < 1 or int(guardian_guess) > 10:
                print("Please enter a number from 1-10.")
                guardian_guess = input("Enter a number from 1-10: ")
            while int(guardian_guess) != int(guardian_num):
                while not guardian_guess.isnumeric() or int(guardian_guess) < 1 or int(guardian_guess) > 10:
                    print("Please enter a number from 1-10.")
                    guardian_guess = input("Enter a number from 1-10: ")
                print("Incorrect guess. You have lost 10 health.")
                user.health -= 10
                if user.health <= 0:
                    print("\n" + "You have lost all your health.")
                    lose()

                guardian_guess = input("Enter a number from 1-10: ")
                while not guardian_guess.isnumeric():
                    print("Please enter a number from 1-10")
                    guardian_guess = input("Enter a number from 1-10: ")

            print(
                "\n" + "Well done! You have guessed the number correctly. The guardian opens the back door and you are greeted with a bright light.")
            win()

        # find way wround troll
        elif talk_troll.upper() == "N":
            print("\n" + "You chose to avoid the troll and turn to find another way past.")
            print("You don't look where you're going... Its scary in this forest after all.")
            print("You walk deeper into the woods and you aren't looking at the ground...")
            print("""
     _______..__   __.      ___      .______    __  
    /       ||  \ |  |     /   \     |   _  \  |  | 
   |   (----`|   \|  |    /  ^  \    |  |_)  | |  | 
    \   \    |  . `  |   /  /_\  \   |   ___/  |  | 
.----)   |   |  |\   |  /  _____  \  |  |      |__| 
|_______/    |__| \__| /__/     \__\ | _|      (__) 


      """)
            print("Your foot gets caught in a bear trap and you are left to die...")
            lose()
