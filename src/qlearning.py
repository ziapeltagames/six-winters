# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 11:13:34 2019

@author: zia
"""

import gym
import swenv
from tqdm import tqdm
import numpy as np
import matplotlib.pyplot as plt
from hyperopt import hp, tpe, fmin, pyll, STATUS_OK, Trials

env = gym.make('SixWinters-v0')

def indices(env_tuple):
    return env_tuple[0], env_tuple[1], env_tuple[2]

# Return both action probabilities for this state
def qactions(qtable, cstate):
    sa, sb, sc = indices(cstate)
    return qtable[sa, sb, sc, :]

# Return the single entry for this state and action
def qaction(qtable, cstate, caction):
    return qactions(qtable, cstate)[caction]

# Run through one game, returning number of turns
def play_game(qt, env, lr, y, training = True, logging = False):
    if logging:
        print("(Stage, Current Timers, Total Timers, Current Reward)")
        print("[Bank Progress / Draw] --> Action (0 = Bank, 1 = Draw) Reward")        

    s = env.reset()
    turns = 0
    reward = 0
    done = False
    while done == False:
        turns = turns + 1
        if training:
            act = np.argmax(qactions(qt, s) + (np.random.randn(env.action_space.n)))
        else:
            act = np.argmax(qactions(qt, s))
        if logging:
            print(s, qactions(qt, s),"-->",act,reward) 
        s1, reward, done, _ = env.step(act)
        if training:
            #Update Q-Table with new knowledge
            sa, sb, sc = indices(s)
            qt[sa, sb, sc, act] = qaction(qt, s, act) + lr*(reward + y*np.max(qactions(qt, s1)) - qaction(qt, s, act))
        
        s = s1
        
    if logging:
        print("Turns ", turns, "Reward ", reward)
            
    return turns, reward, qt

def train_qlearn(param_space = {}):
    
    #Initialize table with all zeros
    Q = np.zeros([env.observation_space.spaces[0].n,
                  env.observation_space.spaces[1].n,
                  env.observation_space.spaces[2].n,
                  env.action_space.n])
    
    # Set learning parameters
    lr = .00001
    if 'lr' in param_space:
        lr = param_space['lr']
    
    y = .9
    if 'y' in param_space:
        y = param_space['y']
        
    num_episodes = 100000
    if 'num_episodes' in param_space:
        num_episodes = int(param_space['num_episodes'])
    
    # Train the network
    for i in range(num_episodes):
        turns, r, Q = play_game(Q, env, lr, y, training = True)
    
    # Calculate a batch score after training
    rList = []
    turnList = []
    for i in range(100000):
        turns, r, Q = play_game(Q, env, lr, y, training = False)
        turnList.append(turns)
        rList.append(r)
            
    # print("lr ",lr," y ",y," episodes ",num_episodes)
    # print("Testing score: " + str(np.average(rList)))
    # print("Testing turns: " + str(np.average(turnList)))
    
    # Log a single playthrough
    # play_game(Q, env, lr, y, training = False, logging = True)
    
    # For minimization problems, this must be lowered, so subtract from
    # some known very high score(this is higher than the avg max of 21)
    avg_r = np.average(rList)
    cost = 25.0 - avg_r
    print('Reward',' ',avg_r,' ',param_space)
    return {'loss': cost, 'status': STATUS_OK}

# Search the hyperparameter space using tpe
def bayes_optimization():

    param_space = {
            'lr': hp.loguniform('lr', np.log(0.0000001), np.log(0.1)),
            'num_episodes': hp.quniform('num_episodes', 10000, 500000, 10000),
            'y': hp.uniform('y', 0.1, 1.0)
            }
    
#    print(pyll.stochastic.sample(param_space))
    
    trials = Trials()
    best_result = fmin(fn = train_qlearn, space = param_space, 
                       algo = tpe.suggest, max_evals = 500, trials = trials)
    
    f, ax = plt.subplots(1)
    xs = [t['misc']['vals']['y'] for t in trials.trials]
    ys = [t['result']['loss'] for t in trials.trials]
    
    # Undo the minimization
    ys = [25.0 - y for y in ys]
    ax.scatter(xs, ys, s=20, linewidth=0.01, alpha=0.75)
    ax.set_title('$score$ $vs$ $y$ ', fontsize=18)
    ax.set_xlabel('$y$', fontsize=16)
    ax.set_ylabel('$score$', fontsize=16)   
    
    f, ax = plt.subplots(1)
    xs = [t['misc']['vals']['lr'] for t in trials.trials]
    ax.scatter(xs, ys, s=20, linewidth=0.01, alpha=0.75)
    ax.set_title('$score$ $vs$ $lr$ ', fontsize=18)
    ax.set_xlabel('$lr$', fontsize=16)
    ax.set_xscale('log')
    ax.set_ylabel('$score$', fontsize=16)

    f, ax = plt.subplots(1)
    xs = [t['misc']['vals']['num_episodes'] for t in trials.trials]
    ax.scatter(xs, ys, s=20, linewidth=0.01, alpha=0.75)
    ax.set_title('$score$ $vs$ $episodes$ ', fontsize=18)
    ax.set_xlabel('$episodes$', fontsize=16)
    ax.set_ylabel('$score$', fontsize=16)    
    
    print("Best Score: ", np.max(ys)," ", best_result)
    
if __name__ == "__main__":
    bayes_optimization()