import time
from random import randint
wins  = 0
loses = 0
 
 
def game(wins, loses):
        print "Rock, Paper or Scissors"
        user_choice = raw_input()
        comp_choice = randint(0,2)
        print "Rock"
        time.sleep(0.5)
        print "Paper"
        time.sleep(0.5)
        print "Scissors"
        time.sleep(0.5)
       
        if user_choice == "Rock":
                if comp_choice == 0:
                        print "Its a draw"
                        end(wins, loses)
                elif comp_choice == 1:
                        print "Paper beats Rock you lost"
                        loses += 1
                        end(wins, loses)
                elif comp_choice == 2:
                        print "Rock beats Scissors you won"
                        wins += 1
                        end(wins, loses)
 
        if user_choice == "Paper":
                if comp_choice == 0:
                        print "Paper beats Rock you won"
                        wins += 1
                        end(wins, loses)
                elif comp_choice == 1:
                        print "Its a draw"
                        end(wins, loses)
                elif comp_choice == 2:
                        print "Scissors beats Paper you lost"
                        loses += 1
                        end(wins, loses)
 
        if user_choice == "Scissors":
                if comp_choice == 0:
                        print "Rock beats Scissors you lost"
                        loses += 1
                        end(wins, loses)
                elif comp_choice == 1:
                        print "Scissors beats Paper you won"
                        wins += 1
                        end(wins, loses)
                elif comp_choice == 2:
                        print "Its a draw"
                        end(wins, loses)
 
def end(wins, loses):
        print "Wins: " + str(wins) + " Loses: " + str(loses)
        print "Do you want to play again?"
        user_input = raw_input()
        if user_input == "Yes":
                game(wins, loses)
 
print "Want to play Rock Paper Scissors?"
user_input = raw_input()
if user_input == "Yes":
        game(wins, loses)
