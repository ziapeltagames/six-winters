# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 11:15:38 2019

@author: zia
"""

from gym.envs.registration import register

register(
        id = 'SixWinters-v0',
        entry_point = 'swenv.sixwinters:SixWinters',
        )