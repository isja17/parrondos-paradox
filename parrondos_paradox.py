#!/usr/bin/env python
# coding: utf-8

# This is a program that lets you test three different Parrondos Paradox strategies. Parrondos Paradox is a game theory paradox that states that there exists two losing games 
#such that, if you play them in alternating orders, you will end up with a winning record. The two games are as follows. In game a, you have a .5 - epsilon chance to win. 
#In the second game, if the amount of money you have is divisible by three, you have a .1-epsilon chance to win; otherwise, you have a .75-epsilon chance to win. 
#If you were to play only one of these games, you would end up losing.
# 
# I include two other strategies beyond alternating games. The second strategy picks a random game to play. The third plays game a twice, then game b twice, etc. 
#In all of these strategies, we expect to have a winning rate by the end, provided we play enough games. 
# 
# Parrondos Paradox: https://en.wikipedia.org/wiki/Parrondo%27s_paradox#The_coin-tossing_example

# In[1]:


import random as rn
import matplotlib.pyplot as plt


# In[43]:


class letsPlay():
    money = []
    games = []
    outcomes = []
    init_money = 5
    
    def game_a(self):
        '''
        game a gives you a ~50% chance to win. (.5-epsilon)
        '''
        self.games.append('a')
        if rn.random() <= .4999999999999999999999999999:
            self.money.append(self.money[len(self.money)-1] + 1) 
            self.outcomes.append('win')
        else:
            self.money.append(self.money[len(self.money)-1] - 1)
            self.outcomes.append('lose')
            
    def game_b(self):
        '''
        if money is divisible by 3, you have a 10-epsilon% chance to win. Otherwise, you have a 75-epsilon% chance
        to win.
        '''
        self.games.append('b')
        
        if self.money[len(self.money)-1] % 3 == 0:
            if rn.random() <= .1:
                self.money.append(self.money[len(self.money)-1] + 1) 
                self.outcomes.append('win')
                
            else:
                self.money.append(self.money[len(self.money)-1] - 1)
                self.outcomes.append('lose')
            
                
        else:
            if rn.random() <= .7499999999999999999999:
                self.money.append(self.money[len(self.money)-1] + 1) 
                self.outcomes.append('win')
                
            else:
                self.money.append(self.money[len(self.money)-1] - 1)
                self.outcomes.append('lose')
    
    def alternate_switching(self, num_games):
        '''
        this strategy plays game a, then game b until num_games is reached. This is the main strategy proposed
        in the original Parrondos Paradox paper. 
        '''
        self.money.append(self.init_money)
        for game in range(num_games):
            if game == 0:
                self.game_a()
            if game % 2 == True:
                self.game_a()
            else:
                self.game_b()
                
        return self.money, self.games, self.outcomes   
                
    def random_strategy(self, num_games):
        'This strategy picks game a or b randomly (50% chance of either)'
        self.money.append(self.init_money)
        for game in range(num_games):
            if rn.random() <= .5:
                self.game_a()
            else:
                self.game_b()
                
        return self.money, self.games, self.outcomes
    
    def double_alternate_switching(self, num_games):
        '''
        This strategy plays game_a twice then game_b twice, etc
        '''
        self.money.append(self.init_money)
        for games in range(num_games//4): #need to / by four since we play four games per loop.
            for _ in range(2):
                self.game_a()
            for _ in range(2):
                self.game_b()
                
        return self.money, self.games, self.outcomes
    
gamble = letsPlay().double_alternate_switching(10000)


# In[44]:


plt.plot(gamble[0])
plt.title('Money over time')
plt.xlabel('Game')
plt.ylabel('Money')

