# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 16:53:11 2022

@author: Suleman_Sahib
"""

import chess
import chess.pgn
import chess.engine
import gym
import gym_chess
from gym_chess.alphazero import BoardEncoding
from gym_chess.alphazero import MoveEncoding
import numpy as np
#import numpy as np
env = gym.make('Chess-v0')
env = BoardEncoding(env, history_length=4)
env = MoveEncoding(env)
env.reset()
import random
import time
from math import log,sqrt,e,inf


class node():
    def __init__(self):
        self.state = chess.Board()
        self.action = ''
        self.children = set()
        self.parent = None
        self.parent_visit = 0
        self.child_visit = 0
        self.winning_score = 0


def expand(curr_node):
    if(len(curr_node.children)==0):
        return curr_node
    max_ucb = -inf
    
    idx = -1
    max_ucb = -inf
    sel_child = None
    for i in curr_node.children:
        tmp = ucb1(i)
        if(tmp>max_ucb):
            idx = i
            max_ucb = tmp
            sel_child = i

    return(expand(sel_child))

def simulate(curr_node):
    if(curr_node.state.is_game_over()):
        board = curr_node.state
        if(board.result()=='1-0'):
            #print("h1")
            return (1,curr_node)
        elif(board.result()=='0-1'):
            #print("h2")
            return (-1,curr_node)
        else:
            return (0.5,curr_node)
    
    all_moves = [curr_node.state.san(i) for i in list(curr_node.state.legal_moves)]
    
    for i in all_moves:
        tmp_state = chess.Board(curr_node.state.fen())
        tmp_state.push_san(i)
        #child = node()
        #child.state = tmp_state
        #child.parent = curr_node
        #curr_node.children.add(child)
    rnd_state = random.choice(list(curr_node.children))

    return simulate(rnd_state)

def backpropagate(reward , current_node):
    while(current_node.parent != None):
        current_node.parent_visit += 1
    return current_node
    
def add_child_under_root(parent_root):
    all_moves = [curr_node.state.san(i) for i in list(curr_node.state.legal_moves)]
    
    for i in all_moves:
        tmp_state = chess.Board(curr_node.state.fen())
        tmp_state.push_san(i)
        child = node()
        child.state = tmp_state
        child.parent = curr_node
        curr_node.children.add(child)
    return curr_node
def get_reward(env):
    if(env.is_game_over()):
        board = curr_node.state
        if(board.result()=='1-0'):
            #print("h1")
            return (1,curr_node)
        elif(board.result()=='0-1'):
            #print("h2")
            return (-1,curr_node)
        else:
            return (0.5,curr_node)
def give_reward(result):
    if (result == "1/2-1/2"):
        return 0.5
    if (result == "0-1"):
        return -1
    if (result == "1-0"):
        return 1.0


board = chess.Board()
engine = chess.engine.SimpleEngine.popen_uci(r'E:\stockfish_win_x64\stockfish_ex.exe')

white = 1
moves = 0
pgn = []
game = chess.pgn.Game()
evaluations = []
sm = 0
cnt = 0
#root = node()
#root.state = board
#ideal_tree = root
#curr_node = root
#root_expanded = add_child_under_root(curr_node)
#state = chess.Board(curr_node.state.fen())
#print(state)
#print(root_expanded.state)
#if (state ==  root_expanded.state):
#    print ("Allah Khair")

Q_table = dict()
#act_val = dict()
#for i in range(20):
    #while not (board.is_game_over()):
state = board.fen()
all_moves = [board.san(i) for i in list(board.legal_moves)]
#for action in all_moves:
    
    #board = chess.Board(state)
action = np.random.choice(all_moves)
#print(board)
board.push_san(action)
print(board)
next_state = board.fen()
limit = chess.engine.Limit(time=2.0)
engin_play = engine.play(board, limit)
import chess.svg

chess.svg.board(board, size=350)   
print(board)
"""
key = state
if key not in Q_table:
    Q_table[key]= {}
else:
    print("Np APPEBNDoih")
if action not in Q_table[key]:
    Q_table[key][action] = 0
if next_state not in Q_table:
    Q_table[key]= {}           
"""        
    #result = board.result()
    #board.reset()
    #game.headers["Result"] = board.result()
    #game.headers["Result"]
    #print(game)

#result = board.result()
#reward = give_reward(result)
#print(Q_table[state])

#for state in Q_table:
#    print(len(Q_table[state]))
    #print(len(Q_table[state].keys()))
        
         
"""
state_list = [a for a in Q_table.keys()]
print(board)
board = chess.Board(str(state_list[0][0]))
print(board)
all_moves = [board.san(i) for i in list(board.legal_moves)]
action = np.random.choice(all_moves)
board.push_san(action)
print(board)
"""
    
#    my_board = chess.Board(a[0])
    
#    break

    #Q_table[a] += reward

#print(state)
#print(next_state)
#for i in all_moves:
#    
#
#for i in all_moves:
#    value = Q_table[((state),i)] 
#    print(value)

"""
for i in range(10):
    
    all_moves = [curr_node.state.san(i) for i in list(curr_node.state.legal_moves)]
    
    for i in all_moves:
        tmp_state = chess.Board(curr_node.state.fen())
        tmp_state.push_san(i)

"""
#saving[(state)] = 0
#child_new = expand(curr_node)
#reward, last_node = simulate(child_new)
#actual = backpropagate(reward, last_node)

"""        
def exploratrion(current_node):
        if(curr_node.state.is_game_over()):
            board = curr_node.state
            reward = 0
            if(board.result()=='1-0'):
                reward = 1
                return (reward ,curr_node)
            elif(board.result()=='0-1'):
                reward = -1
                return (reward ,curr_node)
            else:
                reward = 0.5
                return (reward ,curr_node)
    all_moves = [curr_node.state.san(i) for i in list(curr_node.state.legal_moves)]
    for i in all_moves:
        tmp_state = chess.Board(curr_node.state.fen())
        tmp_state.push_san(i)
        child = node()
        child.state = tmp_state
        child.parent = curr_node
        curr_node.children.add(child)
    rnd_state = random.choice(list(curr_node.children))

    return rollout(rnd_state)

"""