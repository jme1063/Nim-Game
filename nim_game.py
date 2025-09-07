"""
Nim Game implementation for lab assignment.

Author: Jacqueline
Date: 2025-09-07
Collaborators: GitHub Copilot

Implements a 2-player Nim game with a randomized stick count and two game modes; poison
and normal. 
"""
import random

class NimGame:
    """
    Class to represent the 21 Nim game logic.

    Attributes:
        total_sticks (int): The number of sticks remaining in the game.
        current_player (int): The player whose turn it is (1 or 2).
    """
    def __init__(self, total_sticks=21):
        """
        Starts NimGame with a certain amount of sticks.
        Args:
            total_sticks (int): The starting number of sticks. Default is 21.
        """
        self.total_sticks = total_sticks
        self.current_player = 1

    def take_sticks(self, count):
        """
        Current player removed sticks, then changes who's turn it is.

        Args:
            count (int): The number of sticks to take (must be 1, 2, or 3).
            
        """
        if count not in [1, 2, 3]:
            print("you can only take up to 3 sticks, and you have to take atelast 1!")
        elif count > self.total_sticks:
            print("Not enough sticks remain.")

        self.total_sticks -= count

        if self.current_player == 1:
            self.current_player = 2 
        else:
            self.current_player = 2

    def game_state(self):
        """
        Flag to check if game is over. if there are no more sticks, the game ends. otherwise, it
        continues.

        Returns:
            bool: True if no sticks remain, False otherwise.
        """
        if self.total_sticks == 0:
            return True
        else:
            return False

    def get_loser(self):
        """
        Returns the loser (defaults to normal ruleset, where the last person to pick up
        a stick wins. Posion game mode switches dialog for it's win-con).

        Returns:
            int: The losing player's number (1 or 2).
        """
        if self.current_player == 1:
            return 2
        else:
            return 1

    def __str__(self):
        """
        Returns a string representation of the game state.

        Returns:
            str: The current game state.
        """
        return f"Sticks remaining: {self.total_sticks} | Player {self.current_player}'s turn"


if __name__ == "__main__":

    starting_sticks = random.randint(15, 30)

    print(f"Welcome to Nim! Playing the game with {starting_sticks} sticks.")
    print("Choose ruleset:")
    print("1. Normal (last stick wins)")
    print("2. Poison (last stick loses)")

    ruleset = input("Enter 1 for Normal or 2 for Poison: ")

    while ruleset not in ["1", "2"]:

        ruleset = input("Please enter 1 or 2: ")

    poison = (ruleset == "2")

    game = NimGame(total_sticks=starting_sticks)

    while not game.game_state():

        print(game)
        move_input = input(f"Player {game.current_player}, how many sticks do you take (1-3)? ")
        
        if not move_input.isdigit():

            print("Please enter a number.")
        
        else:
            move = int(move_input)

            if move not in [1, 2, 3]:
                print("You can only take 1, 2, or 3 sticks.")

            elif move > game.total_sticks:
                print("Not enough sticks remain.")

            else:
                game.take_sticks(move)
    if poison:
        print(f"Player {game.get_loser()} took the last stick and loses! Player {game.current_player} wins!")
    
    else:
        print(f"Player {game.get_winner()} wins by taking the last stick!")
