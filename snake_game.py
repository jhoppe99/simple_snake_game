#!/usr/bin/python3.8

from typing import List
import os
import time
import click
import threading


printable = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

board_height = 20
board_width = 20
snake_width = 3
empty_space = '.'
snake_body = '*'
speed_sec = 1


"""Initial informations about snake's position and direction"""

snake_segments = [[7,9], [8,9], [9,9], [10,9], [11,9]]
number_of_snake_segments = len(snake_segments)
current_movement_direction = "up"

class Snake_game:
    def __init__(self, width: int, height: int, fill: str, snake_segments: list, direction: str ):
        self.width = width
        self.height = height
        self.fill = fill
        self.snake_segments = snake_segments
        self.direction = direction
        
    def get_empty_board(self):
        empty_board = [[self.fill for _ in range(self.width)] for _ in range(self.height)]
        return empty_board


    def display_board(self):
        '''Displays game board with the snake in initial position'''


        board = Snake_game(board_width, board_height, empty_space, snake_segments, current_movement_direction)
        board2 = board.get_empty_board() 
        # get_empty_board(width=board_width, height=board_height, fill=empty_space)
        for x, y in snake_segments:
            board2[y][x] = snake_body
        for x in board2:
            print(*x, '\r')

    def update_snake(self):
        """Updates snakes coordinates based on the moving direction."""
 
        if self.direction == "down":
            movement = snake_segments[-1].copy()
            movement[1] = movement[1] + 1
            snake_segments.append(movement)
            del snake_segments[0]
        elif self.direction == "up":
            movement = snake_segments[-1].copy()
            movement[1] = movement[1] - 1
            snake_segments.append(movement)
            del snake_segments[0]
        elif self.direction == "right":
            movement = snake_segments[-1].copy()
            movement[0] = movement[0] + 1
            snake_segments.append(movement)
            del snake_segments[0]
        elif self.direction == "left":
            movement = snake_segments[0].copy()
            movement[0] = movement[0] - 1
            snake_segments.insert(0, movement)
            del snake_segments[-1]



   



    def check_colision(self):
        '''Checks if snake don't touches walls'''


        if snake_segments[0][0] == 0:
            os.system('clear')
            print("---YOU LOSE!---YOUR SCORE WAS: " + str(score)+ "---")
            exit()
        if snake_segments[0][1] == 0:
            os.system('clear')
            print("---YOU LOSE!---YOUR SCORE WAS: " + str(score)+ "---")
            exit()
        if snake_segments[number_of_snake_segments - 1][0] == board_height - 1:
            os.system('clear')
            print("---YOU LOSE!---YOUR SCORE WAS: " + str(score)+ "---")
            exit()
        if snake_segments[number_of_snake_segments - 1][1] == board_width - 1:
            os.system('clear')
            print("---YOU LOSE!---YOUR SCORE WAS: " + str(score)+ "---")
            exit()   

if __name__ == '__main__':
    
    game = Snake_game(board_width, board_height, empty_space, snake_segments, current_movement_direction)

    '''Shows basic informations about the game'''
    
    os.system('clear')
    print("This is a little snake game. You can control the snake by your keybord arrows. Be careful! Don't touch the walls!")
    time.sleep(5)
    
    
    
    def moves():
        '''Changes arrows input to change in snake movement direction'''


        while True:
            key_input = click.getchar()
            global current_movement_direction 
            if key_input == '\x1b[D':
                current_movement_direction = "left"
                print(current_movement_direction)  
            elif key_input == '\x1b[C':
                current_movement_direction = "right"
            elif key_input == '\x1b[A':
                current_movement_direction = "up"
            elif key_input == '\x1b[B':
                current_movement_direction = "down"

    

    thre1 = threading.Thread(target=moves, daemon=True)
    thre1.start()
    


    '''Puting together whole functions defining game and creates output'''

    score = 5
    while True:
        game.check_colision()
        game.update_snake()
        game.display_board()
        
        print("YOUR SCORE: " + str(score))
        score = score + 2
        time.sleep(speed_sec)
        os.system('clear')



