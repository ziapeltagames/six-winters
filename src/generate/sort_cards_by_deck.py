from shutil import move

import glob
import os


for subloc in ["tts", "game_crafter"]:

    indices =  [1, 200]

    for subpath in ["obstacles", "events", "text_obstacles", "assets", "abilities", "locations", "scenes", "conflicts", "stats", "agents", "scenes", "suits"]:

        # full_path = '..\\Cards\\'+subloc+'\\'+subpath+'\\'

        # WM
        full_path = '..\\..\\Six Winters\\cards\\'+subloc+'\\'+subpath+'\\'
        print(full_path)

        for i in range(indices[0], indices[1], 2):
            if i == 1:
                files = glob.glob(full_path+'*-1.png')
            else:
                files = glob.glob(full_path+'*-1'+str(i)+'.png')
            if files:
                base, cardnum = os.path.basename(files[0]).split('-')
                if i == 1:
                    cardnum = '2'
                else:
                    cardnum = str(int(cardnum[1:-4]) + 1)
                print(full_path+'front\\'+base[:-3]+'-1'+cardnum+'[face].png')
                move(files[0], full_path+'front\\'+base[:-3]+'-1'+cardnum+'[face].png')

            files = glob.glob(full_path+'*-1'+str(i+1)+'.png')
            if files:
                base, cardnum = os.path.basename(files[0]).split('-')
                print(full_path+'back\\'+base[:-3]+'-'+cardnum[:-4]+'[back].png')
                move(files[0], full_path+'back\\'+base[:-3]+'-'+cardnum[:-4]+'[back].png')
                # move(files[0], full_path+'back\\'+os.path.basename(files[0])[:-4]+'[back].png')


# chars =  [1, 99]

# charpath = '..\\Characters\\tts\\sheets\\'

# for i in range(chars[0], chars[1], 2):
#     if i == 1:
#         obs = glob.glob(charpath+'*-1.png')
#     else:
#         obs = glob.glob(charpath+'*-1'+str(i)+'.png')
#     if obs:
#         base, cardnum = os.path.basename(obs[0]).split('-')
#         if i == 1:
#             cardnum = '2'
#         else:
#             cardnum = str(int(cardnum[1:-4]) + 1)
#         move(obs[0], charpath+'front\\'+base+'-1'+cardnum+'[face].png')

#     obs = glob.glob(charpath+'*-1'+str(i+1)+'.png')
#     if obs:
#         move(obs[0], charpath+'back\\'+os.path.basename(obs[0])[:-4]+'[back].png')

rulepath = '..\\Rules\\game_crafter\\'

pages = glob.glob(rulepath + '*.png')
for page in pages:
    base, pagenum = os.path.basename(page).split('05')
    if pagenum == '.png':
        pagenum = '1.png'

    move(page, rulepath+'front\\'+base + '[' + pagenum[:-4] + '].png')
