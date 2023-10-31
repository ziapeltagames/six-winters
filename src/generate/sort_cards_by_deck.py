from shutil import move

import glob
import os


for subloc in ["tts", "game_crafter"]:

    ob_mission =  [1, 200]

    obpath = '..\\Cards\\'+subloc+'\\obstacles\\'

    for i in range(ob_mission[0], ob_mission[1], 2):
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
            move(obs[0], obpath+'front\\'+base+'-1'+cardnum+'[face].png')

        obs = glob.glob(obpath+'*-1'+str(i+1)+'.png')
        if obs:
            move(obs[0], obpath+'back\\'+os.path.basename(obs[0])[:-4]+'[back].png')


for subloc in ["tts", "game_crafter"]:

    square_progs =  [1, 200]
    square_progpath = '..\\Cards\\'+subloc+'\\assets\\'

    for i in range(square_progs[0], square_progs[1], 2):
        if i == 1:
            obs = glob.glob(square_progpath+'*-1.png')
        else:
            obs = glob.glob(square_progpath+'*-1'+str(i)+'.png')
        if obs:
            base, cardnum = os.path.basename(obs[0]).split('-')
            if i == 1:
                cardnum = '2'
            else:
                cardnum = str(int(cardnum[1:-4]) + 1)
            move(obs[0], square_progpath+'front\\'+base+'-1'+cardnum+'[face].png')

        obs = glob.glob(square_progpath+'*-1'+str(i+1)+'.png')
        if obs:
            move(obs[0], square_progpath+'back\\'+os.path.basename(obs[0])[:-4]+'[back].png')

for subloc in ["tts", "game_crafter"]:

    locs =  [1, 120]

    locpath = '..\\Cards\\'+subloc+'\\locations\\'

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


for subloc in ["tts", "game_crafter"]:

    miss =  [1, 99]

    misspath = '..\\Cards\\'+subloc+'\\missions\\'

    for i in range(miss[0], miss[1], 2):
        if i == 1:
            obs = glob.glob(misspath+'*-1.png')
        else:
            obs = glob.glob(misspath+'*-1'+str(i)+'.png')
        if obs:
            base, cardnum = os.path.basename(obs[0]).split('-')
            if i == 1:
                cardnum = '2'
            else:
                cardnum = str(int(cardnum[1:-4]) + 1)
            move(obs[0], misspath+'front\\'+base+'-1'+cardnum+'[face].png')

        obs = glob.glob(misspath+'*-1'+str(i+1)+'.png')
        if obs:
            move(obs[0], misspath+'back\\'+os.path.basename(obs[0])[:-4]+'[back].png')

for subloc in ["tts", "game_crafter"]:

    scene =  [1, 99]

    scenepath = '..\\Cards\\'+subloc+'\\scenes\\'

    for i in range(scene[0], scene[1], 2):
        if i == 1:
            obs = glob.glob(scenepath+'*-1.png')
        else:
            obs = glob.glob(scenepath+'*-1'+str(i)+'.png')
        if obs:
            base, cardnum = os.path.basename(obs[0]).split('-')
            if i == 1:
                cardnum = '2'
            else:
                cardnum = str(int(cardnum[1:-4]) + 1)
            move(obs[0], scenepath+'front\\'+base+'-1'+cardnum+'[face].png')

        obs = glob.glob(scenepath+'*-1'+str(i+1)+'.png')
        if obs:
            move(obs[0], scenepath+'back\\'+os.path.basename(obs[0])[:-4]+'[back].png')

chars =  [1, 99]

charpath = '..\\Characters\\tts\\sheets\\'

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

charpath = '..\\Characters\\tts\\mats\\'

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
