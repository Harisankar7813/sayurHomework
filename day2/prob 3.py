'''Problem #3
Its is a single player game where the user starts with 0 points. User keeps rolling the 
dice.If the rolled number is 0, game ends. If the rolled number is even, then 2 points are
 added. If the number is odd, then if the number is 1,3 then the user has to jump. 
 If the number is 5, then 3 points are added. The game ends when the user has 50 points.'''

def dice_game():
    player_score=0
    end_point=50
    even_numbers=[2,4,6,8]
    while(player_score <= end_point):
        user_rolled=int(input("Rolled number you get:"))
        if user_rolled in even_numbers:
            player_score+=2
        elif user_rolled == 1 or user_rolled ==3:
            print("User jumps")
        elif user_rolled == 5:
            player_score+=3

        print(f"Current Score : {player_score}")
        if player_score>=50:
            print("Congratulations you have win the game")
            break
        elif user_rolled==0:
            print("Game Ends")
            break
dice_game()

'''
output
Rolled number you get:3
User jumps
Current Score : 0
Rolled number you get:2
Current Score : 2
Rolled number you get:5
Current Score : 5
Rolled number you get:5
Current Score : 8
Rolled number you get:5
Current Score : 11
Rolled number you get:5
Current Score : 14
Rolled number you get:2
Current Score : 16
Rolled number you get:5
Current Score : 19
Rolled number you get:4
Current Score : 21
Rolled number you get:6
Current Score : 23
Rolled number you get:8
Current Score : 25
Rolled number you get:5
Current Score : 28
Rolled number you get:5
Current Score : 31
Rolled number you get:5
Current Score : 34
Rolled number you get:5
Current Score : 37
Rolled number you get:5
Current Score : 40
Rolled number you get:5
Current Score : 43
Rolled number you get:5
Current Score : 46
Rolled number you get:5
Current Score : 49
Rolled number you get:5
Current Score : 52
Congratulations you have win the game
'''       

