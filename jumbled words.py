# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 06:15:28 2022

@author: SAI VISHWA B
"""

#Jumbled words
import random
def choose():
    words = ["science","world","coding","computer","water","earth","winter","summer","enjoy","football"]
    pick = random.choice(words)
    return pick

def jumble(words):
    jumbled_word = "".join(random.sample(words,len(words)))
    return jumbled_word
    
def play():
    p1 = input("Player 1 : Enter your name : ")
    p2 = input("Player 2 : Enter your name : ")
    print()
    p1p = 0
    p2p = 0
    turn = 0 
    c = 0
    while(1):
        if turn % 2 == 0:
            picked_word = choose()
            qn = jumble(picked_word)
            print(p1," its your turn...")
            print("Rearrange this word : ",qn)
            ans = input()
            print()
            if (ans == picked_word):
                print("Wonderful, your are right.")
                p1p += 1
                print("Your point is ",p1p)
            else:
                print("Sorry, better luck next time ",p1)
                print("Your point is ",p1p)
                
        else:
            picked_word = choose()
            qn = jumble(picked_word)
            print(p2," its your turn...")
            print("Rearrange this word : ",qn)
            print()
            ans = input()
            if (ans == picked_word):
                print("Wonderful, your are right.")
                p2p += 1
                print("Your point is ",p2p)
            else:
                print("Sorry, better luck next time ")
                print("Your point is ",p2p)
                
        turn += 1
        c = int(input("Do you want to continue the game, enter 1 to continue or 0 to exit : "))
        print()
        if(c == 0):
            print("Okay bye bye...")
            break
        
play()
        
        
                
                
                