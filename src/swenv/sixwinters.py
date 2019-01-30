import random
from random import shuffle

import gym
import numpy as np
from gym import spaces
from gym.utils import seeding

NUM_TIMERS = 10
NUM_NONTIMERS = 10

# 1s are timers
def build_deck(num_nontimers, num_timers):
    deck = []
    for i in range(num_nontimers):
        deck.append(0)
    for i in range(num_timers):
        deck.append(1)
    shuffle(deck)
    return deck

# Pull a card from the deck
def draw_card(deck):
    card = deck.pop(0)
    return card

# Add back in the 0s (non timers)
def advance_stage(deck):
    timers_remaining = np.sum(deck)
    return build_deck(NUM_NONTIMERS, timers_remaining)

class SixWinters(gym.Env):
    """
    A template to implement custom OpenAI Gym environments

    """

    metadata = {'render.modes': ['human']}
    def __init__(self):
        self.__version__ = "0"

        # Draw or keep what you have
        self.action_space = spaces.Discrete(2)
        
        # Current stage, current timers, total timers, current_reward
        self.observation_space = spaces.Tuple((
            spaces.Discrete(3),
            spaces.Discrete(3),
            spaces.Discrete(10)))
        self.seed()

        # Start the first game
        self.reset()

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]        

    def step(self, action):
        """
        Runs one time-step of the environment's dynamics. The reset() method is called at the end of every episode
        :param action: The action to be executed in the environment
        :return: (observation, reward, done, info)
            observation (object):
                Observation from the environment at the current time-step
            reward (float):
                Reward from the environment due to the previous action performed
            done (bool):
                a boolean, indicating whether the episode has ended
            info (dict):
                a dictionary containing additional information about the previous action
        """

        assert self.action_space.contains(action)
        done = False

        if action: # draw again
            self.current_reward += 1
            card = draw_card(self.deck)
            if card == 1: # card is a timer
                self.total_timers += 1
                if self.current_timers == 2:
                    self.current_reward = 0
                    self.current_timers = 0
                    if self.stage == 2:
                        done = True
                    else:
                        self.stage += 1
                        self.deck = advance_stage(self.deck)
                else:
                    self.current_timers += 1

        else:  # bank all progress
            self.reward = self.reward + self.current_reward
            self.current_reward = 0
            self.current_timers = 0
            self.deck = advance_stage(self.deck)
            if self.stage == 2:
                done = True
            else:
                self.stage += 1
                
        # Doesn't seem to work with many algorithms if there's a reward
        # before the end
        if done == True and self.reward <= 0:
            return self._get_obs(), -1, done, {}
        return self._get_obs(), self.current_reward + self.reward, done, {}

    def reset(self):
        """
        Reset the environment state and returns an initial observation

        Returns
        -------
        observation (object): The initial observation for the new episode after reset
        :return:
        """
        self.deck = build_deck(NUM_NONTIMERS, NUM_TIMERS)        
        self.stage = 0
        self.current_timers = 0
        self.total_timers = 0
        self.current_reward = 0
        self.reward = 0
        
        return self._get_obs()
        
    def _get_obs(self):
        return (self.stage, self.current_timers, self.total_timers)
    
if __name__ == "__main__":
    # Test out a random "push your luck" strategy
    env = SixWinters()
    obs = env.reset()
    done = False
    t = 0
    tot_re = 0.0
    while not done:
        action = random.randint(0,1)
        obs, r, done, info = env.step(action)
        print("Step", t, "Action", action, "Reward", round(r, 4), "Obs", obs)
        t = t+1
        