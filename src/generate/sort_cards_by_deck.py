from shutil import move

import glob
import os

ob_threats =  [1, 127]
ob_locs =  [127, 185]

obpath = '..\\Cards\\tts\\obstacles\\'

for i in range(ob_threats[0], ob_threats[1], 2):
    if i == 1:
        obs = glob.glob(obpath+'*-1.png')
    else:
        obs = glob.glob(obpath+'*-1'+str(i)+'.png')
    if obs:
        base, cardnum = os.path.basename(obs[0]).split('-')
        if i == 1:
            cardnum = '2'
        else:
            cardnum = str(int(cardnum[1:-4]) + 1)
        move(obs[0], obpath+'threat_fronts\\'+base+'-1'+cardnum+'[face].png')

    obs = glob.glob(obpath+'*-1'+str(i+1)+'.png')
    if obs:
        move(obs[0], obpath+'threat_backs\\'+os.path.basename(obs[0])[:-4]+'[back].png')

for i in range(ob_locs[0], ob_locs[1], 2):
    obs = glob.glob(obpath+'*-1'+str(i)+'.png')
    if obs:
        base, cardnum = os.path.basename(obs[0]).split('-')
        cardnum = str(int(cardnum[1:-4]) + 1)
        move(obs[0], obpath+'loc_fronts\\'+base+'-1'+cardnum+'[face].png')
    obs = glob.glob(obpath+'*-1'+str(i+1)+'.png')
    if obs:
        move(obs[0], obpath+'loc_backs\\'+os.path.basename(obs[0][:-4]+'[back].png'))

progs =  [1, 150]

progpath = '..\\Cards\\tts\\progress\\'

for i in range(progs[0], progs[1], 2):
    if i == 1:
        obs = glob.glob(progpath+'*-1.png')
    else:
        obs = glob.glob(progpath+'*-1'+str(i)+'.png')
    if obs:
        base, cardnum = os.path.basename(obs[0]).split('-')
        if i == 1:
            cardnum = '2'
        else:
            cardnum = str(int(cardnum[1:-4]) + 1)
        move(obs[0], progpath+'front\\'+base+'-1'+cardnum+'[face].png')

    obs = glob.glob(progpath+'*-1'+str(i+1)+'.png')
    if obs:
        move(obs[0], progpath+'back\\'+os.path.basename(obs[0])[:-4]+'[back].png')

locs =  [1, 99]

locpath = '..\\Cards\\tts\\locations\\'

for i in range(locs[0], locs[1], 2):
    if i == 1:
        obs = glob.glob(locpath+'*-1.png')
    else:
        obs = glob.glob(locpath+'*-1'+str(i)+'.png')
    if obs:
        base, cardnum = os.path.basename(obs[0]).split('-')
        if i == 1:
            cardnum = '2'
        else:
            cardnum = str(int(cardnum[1:-4]) + 1)
        move(obs[0], locpath+'front\\'+base+'-1'+cardnum+'[face].png')

    obs = glob.glob(locpath+'*-1'+str(i+1)+'.png')
    if obs:
        move(obs[0], locpath+'back\\'+os.path.basename(obs[0])[:-4]+'[back].png')

chars =  [1, 99]

charpath = '..\\Characters\\tts\\'

for i in range(chars[0], chars[1], 2):
    if i == 1:
        obs = glob.glob(charpath+'*-1.png')
    else:
        obs = glob.glob(charpath+'*-1'+str(i)+'.png')
    if obs:
        base, cardnum = os.path.basename(obs[0]).split('-')
        if i == 1:
            cardnum = '2'
        else:
            cardnum = str(int(cardnum[1:-4]) + 1)
        move(obs[0], charpath+'front\\'+base+'-1'+cardnum+'[face].png')

    obs = glob.glob(charpath+'*-1'+str(i+1)+'.png')
    if obs:
        move(obs[0], charpath+'back\\'+os.path.basename(obs[0])[:-4]+'[back].png')

charpath = '..\\Characters\\sheets_tts\\'

for i in range(chars[0], chars[1], 2):
    if i == 1:
        obs = glob.glob(charpath+'*-1.png')
    else:
        obs = glob.glob(charpath+'*-1'+str(i)+'.png')
    if obs:
        base, cardnum = os.path.basename(obs[0]).split('-')
        if i == 1:
            cardnum = '2'
        else:
            cardnum = str(int(cardnum[1:-4]) + 1)
        move(obs[0], charpath+'front\\'+base+'-1'+cardnum+'[face].png')

    obs = glob.glob(charpath+'*-1'+str(i+1)+'.png')
    if obs:
        move(obs[0], charpath+'back\\'+os.path.basename(obs[0])[:-4]+'[back].png')

rulepath = '..\\Rules\\game_crafter\\'

pages = glob.glob(rulepath + '*.png')
for page in pages:
    base, pagenum = os.path.basename(page).split('05')
    if pagenum == '.png':
        pagenum = '1.png'

    move(page, rulepath+'front\\'+base + '[' + pagenum[:-4] + '].png')

# events =  [1, 99]

# eventpath = '..\\Cards\\tts\\events\\'

# for i in range(events[0], events[1], 2):
#     if i == 1:
#         obs = glob.glob(eventpath+'*-1.png')
#     else:
#         obs = glob.glob(eventpath+'*-1'+str(i)+'.png')
#     if obs:
#         move(obs[0], eventpath+'front\\'+os.path.basename(obs[0]))

#     obs = glob.glob(eventpath+'*-1'+str(i+1)+'.png')
#     if obs:
#         move(obs[0], eventpath+'back\\'+os.path.basename(obs[0]))
