# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 11:13:34 2019

@author: zia
"""

import gym
import swenv
import numpy as np

env = gym.make('SixWinters-v0')

def indices(env_tuple):
    return env_tuple[0], env_tuple[1], env_tuple[2], env_tuple[3]

#Initialize table with all zeros
total_obs = 0

Q = np.zeros([env.observation_space.spaces[0].n,
              env.observation_space.spaces[1].n,
              env.observation_space.spaces[2].n,
              env.observation_space.spaces[3].n,
              env.action_space.n])

# Set learning parameters
lr = .0001
y = .95
num_episodes = 1000000

#create lists to contain total rewards and steps per episode
rList = []
for i in range(num_episodes):
    
    #Reset environment and get first new observation
    s = env.reset()
    d = False
    
    #The Q-Table learning algorithm
    while d == False:
        
        sa, sb, sc, sd = indices(s)        
        
        #Choose an action by greedily (with noise) picking from Q table
        a = np.argmax(Q[sa, sb, sc, sd, :] + (np.random.randn(env.action_space.n) + [0.0, 1.0]) * (1./(i+1)))
        
        #Get new state and reward from environment
        s1, r, d, _ = env.step(a)
        if i == (num_episodes - 1):
            print(s,Q[sa, sb, sc, sd, :],"-->",a,r)

        s1a, s1b, s1c, s1d = indices(s1)
        
        #Update Q-Table with new knowledge
        Q[sa, sb, sc, sd, a] = Q[sa, sb, sc, sd, a] + lr*(r + y*np.max(Q[s1a, s1b, s1c, s1d, :]) - Q[sa, sb, sc, sd, a])
        s = s1

    rList.append(r)
    
print("Score over time: " +  str(sum(rList)/num_episodes))