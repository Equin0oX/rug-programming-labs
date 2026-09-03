"""
File:   helloworld.py
Author: Sebastian Ševčík (s.sevcik@student,rug.nl)

Description:
    This program takes in two imputs of player move decisions, then prints out which player has won.
"""

player1choice = input()
player2choice = input()

if player1choice == player2choice:
    print("It is a draw.")
elif player1choice == "rock" and player2choice == "scissors" or player1choice == "scissors" and player2choice == "paper" or player1choice == "paper" and player2choice == "rock" :
    print("Player one wins.")
else :
    print("Player two wins.")
