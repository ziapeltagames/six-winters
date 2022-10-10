from shutil import move

import glob
import os

ob_threats =  [1, 125]
ob_locs =  [125, 183]

obpath = 'D:\\\\Dropbox\\Ziapelta Games\\Games\\Six Winters\\Cards\\tts\\obstacles\\'

for i in range(ob_threats[0], ob_threats[1], 2):
    if i == 1:
        obs = glob.glob(obpath+'*-1.png')
    else:
        obs = glob.glob(obpath+'*-1'+str(i)+'.png')
    if obs:
        move(obs[0], obpath+'threat_fronts\\'+os.path.basename(obs[0]))

    obs = glob.glob(obpath+'*-1'+str(i+1)+'.png')
    if obs:
        move(obs[0], obpath+'threat_backs\\'+os.path.basename(obs[0]))

for i in range(ob_locs[0], ob_locs[1], 2):
    obs = glob.glob(obpath+'*-1'+str(i)+'.png')
    if obs:
        move(obs[0], obpath+'loc_fronts\\'+os.path.basename(obs[0]))
    obs = glob.glob(obpath+'*-1'+str(i+1)+'.png')
    if obs:
        move(obs[0], obpath+'loc_backs\\'+os.path.basename(obs[0]))

progs =  [1, 115]

progpath = 'D:\\\\Dropbox\\Ziapelta Games\\Games\\Six Winters\\Cards\\tts\\progress\\'

for i in range(progs[0], progs[1], 2):
    if i == 1:
        obs = glob.glob(progpath+'*-1.png')
    else:
        obs = glob.glob(progpath+'*-1'+str(i)+'.png')
    if obs:
        move(obs[0], progpath+'front\\'+os.path.basename(obs[0]))

    obs = glob.glob(progpath+'*-1'+str(i+1)+'.png')
    if obs:
        move(obs[0], progpath+'back\\'+os.path.basename(obs[0]))

locs =  [1, 99]

locpath = 'D:\\\\Dropbox\\Ziapelta Games\\Games\\Six Winters\\Cards\\tts\\locations\\'

for i in range(locs[0], locs[1], 2):
    if i == 1:
        obs = glob.glob(locpath+'*-1.png')
    else:
        obs = glob.glob(locpath+'*-1'+str(i)+'.png')
    if obs:
        move(obs[0], locpath+'front\\'+os.path.basename(obs[0]))

    obs = glob.glob(locpath+'*-1'+str(i+1)+'.png')
    if obs:
        move(obs[0], locpath+'back\\'+os.path.basename(obs[0]))

events =  [1, 99]

eventpath = 'D:\\\\Dropbox\\Ziapelta Games\\Games\\Six Winters\\Cards\\tts\\events\\'

for i in range(events[0], events[1], 2):
    if i == 1:
        obs = glob.glob(eventpath+'*-1.png')
    else:
        obs = glob.glob(eventpath+'*-1'+str(i)+'.png')
    if obs:
        move(obs[0], eventpath+'front\\'+os.path.basename(obs[0]))

    obs = glob.glob(eventpath+'*-1'+str(i+1)+'.png')
    if obs:
        move(obs[0], eventpath+'back\\'+os.path.basename(obs[0]))
