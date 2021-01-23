"""

Copyright 2021 Supriyo

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""



# Core of the app
import random

# Available moves
moves = ['rock', 'paper', 'scissors']

# Move by client 
client_move = random.choice(moves)

# Scores


def result(move: str) -> str:
    '''Takes the move and returns the result'''
    user_score, client_score = 0, 0
    if move.lower() not in moves:
        response = {
            'status': 404,
            'reason': 'Move not found.'
        }
        return response
    else:
            # Rock statements
        if move.lower() == 'rock' and client_move == 'scissors':
            user_score = user_score + 1
            client_score = client_score - 1
            data = {
                'status': 200,
                'move': client_move,
                'user_score': user_score,
                'client_score': client_score,
                'result': 'win'
            }
            return data

        if move.lower() == 'rock' and client_move == 'paper':
            user_score = user_score - 1
            client_score = client_score + 1
            data = {
                'status': 200,
                'move': client_move,
                'user_score': user_score,
                'client_score': client_score,
                'result': 'lose'
            }
            return data

        if move.lower() == 'rock' and client_move == 'rock':
            data = {
                'status': 200,
                'move': client_move,
                'user_score': user_score,
                'client_score': client_score,
                'result': 'draw'
            }
            return data

        # Paper statements
        if move.lower() == 'paper' and client_move == 'rock':
            user_score = user_score + 1
            client_score = client_score - 1
            data = {
                'status': 200,
                'move': client_move,
                'user_score': user_score,
                'client_score': client_score,
                'result': 'winner'
            }
            return data

        if move.lower() == 'paper' and client_move == 'scissors':
            user_score = user_score - 1
            client_score = client_score + 1
            data = {
                'status': 200,
                'move': client_move,
                'user_score': user_score,
                'client_score': client_score,
                'result': 'lose'
            }
            return data

        if move.lower() == 'paper' and client_move == 'paper':
            data = {
                'status': 200,
                'move': client_move,
                'user_score': user_score,
                'client_score': client_score,
                'result': 'draw'
            }
            return data

        # Scissors statements
        if move.lower() == 'scissors' and client_move == 'paper':
            user_score = user_score + 1
            client_score = client_score - 1
            data = {
                'status': 200,
                'move': client_move,
                'user_score': user_score,
                'client_score': client_score,
                'result': 'win'
            }
            return data

        if move.lower() == 'scissors' and client_move == 'rock':
            user_score = user_score - 1
            client_score = client_score + 1
            data = {
                'status': 200,
                'move': client_move,
                'user_score': user_score,
                'client_score': client_score,
                'result': 'lose'
            }
            return data

        if move.lower() == 'scissors' and client_move == 'scissors':
            data = {
                'status': 200,
                'move': client_move,
                'user_score': user_score,
                'client_score': client_score,
                'result': 'draw'
            }
            return data
            
            


# print(result('rock'))
        
