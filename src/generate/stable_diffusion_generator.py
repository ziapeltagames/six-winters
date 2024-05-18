# Used for prototype art

import random
import torch

from diffusers import DiffusionPipeline, StableDiffusionXLImg2ImgPipeline, StableDiffusionXLPipeline

artists = ["wayne reynolds", "john stanko", "kieran yanner", "artgerm", "greg rukowski", "alphonse mucha",
"clyde caldwell", "john blanche", "russ nicholson", "larry elmore", "jeff easley", "erol otus", 
"brom", "ian miller", "keith parkinson", "frank frazetta", "daniel horne", "doug kovacs",
"ned rogers", "nixeu", "william-adolphe bouguereau", "greg hildebrandt",
"mahmud asrar", "tuomas korpi", "titian", "charlie bowater", "n. c. wyeth", "arthur rackham", "todd lockwood",
"ciruelo cabral", "danny flynn", "alan lee", "john jude palencar", "stephanie pui-mun law", "hannes bok", "tony diterlizzi",
"kinuko y. craft", "ted nasmith", "bob eggleton", "rowena morrill", "glenn fabry", "jim warren", "wayne barlow", "charles vess"]

# Less appropriate artist prompts
# gustave dore: usually black and white, detailed etchings
# edmund dulac: muted tones
# michael garmash: heavy brush strokes, more abstract

loc_prompts = []
    
old_loc_prompts = ["painting of fantasy persian city on the sea, with many houses and markets, boats are in the harbor, sun is setting, the beaches are crimson, for dungeons and dragons  ",
"painting of a cloaked fantasy figure, walking through the snow, between tall rocky mountains, setting sun, stars coming out above ",
"painting of four seasons, swirled together in a circle, mixing ",
"painting of travelers in the distance, walking through a snowy mountain pass, tall mountains surround them ",
"painting of fantasy persian city on the sea, boats are in the harbor, sun is setting, the beaches are crimson, for dungeons and dragons  ",
"painting of will o wisps in a swamp, the water is glowing orange and blue, vines hang above the water, for dungeons and dragons ",
"painting of a fantasy throne room, for dungeons and dragons, with pale lavender lighting, high brass arches ",
"painting of ghosts floating through dense forest, with purple clouds floating overhead, for dungeons and dragons ",
"painting of a magical forest, with translucent purple ghost trees and dark gray rivers, for dungeons and dragons ",
"painting of byzantine throne room, with brass throne, and red carpets, pale lavender lighting ",
"painting of a ruined fantasy city, crumbling walls, crows flying overhead, the sun is setting, for dungeons and dragons ",
"painting of magical wizard's tower, rising above celtic village, with stars in the sky ",
"painting of wizard's tower, rising above celtic village, with hills in the background ",
"painting of long persian hall, with brass doors, and brass statues on either side of a lavender carpet ",
"painting of long hall in persian castle, with brass doors both sides ",
"painting of desolate plains in mongolia, with rain clouds overhead ",
"painting of an alley in a fantasy city for dungeons and dragons, rain clouds are overhead, the houses are dreary ",
"painting of a slavic village, with a stream running through it, deep in the forest",
"painting of a large wooden fantasy building, long and narrow, in a mountain valley",
"painting of a long fantasy hall, full of mirrors, and sunlight coming through windows high in the ceiling ",
"painting of a fantasy cottage, built into the top of a large tree, in a dense forest ",
"painting of a fantasy persian house, built into a large forest, with a stream running past ",
"painting of fantasy tavern, with lavender smoke swirling around the customers ",
"painting of a fantasy opium den, with lavender pillows and a large brass hookah, with lavender smoke swirling around ",
"painting of rocky columns forming an eldritch helix, standing on a hill ",
"painting of fields of wheat and barley in an ancient valley, with farm houses in the distance ",
"painting of ancient roman farms, with hills in the backgrounds ",
"painting of small valley with a narrow stream running through it, trees on both sides of the stream, leaves are over the stream in the style of ",
"painting of a green field with rocky monuments for dungeons and dragons ",
"painting of fantasy female roman peasent standing next to cart filled with squid and octopus ",
"painting of fantasy fish merchant stall, selling squid and octopus ",
"painting of dark forest with white and gray trees, colorful mushrooms grow on the ground ",
"painting of fantasy fishmonger, with cart carrying squid and octopus, for dungeons and dragons ",
"painting of fantasy persian village with trading carts and amaranth, for dungeons and dragons ",
"painting of fantasy military fort with white walls in the hills for dungeons and dragons ",
"painting of fantasy dungeon hall with many jail cells, dim lighting from torches, for dungeons and dragons ",
"painting of fantasy prison with many jail cells, for dungeons and dragons ",
"painting of medieval torture devices, for dungeons and dragons ",
"painting of roman fort in the hills, for dungeons and dragons ",
"painting of dimly lit, crowded fantasy tavern, for dungeons and dragons ",
"painting of persian castle made of brass in the distance with a field of amaranth, for dungeons and dragons ",
"painting of glowing blue forest, dense trees, ghosts, for dungeons and dragons ",
"painting of stone statues of skulls and tentacles on a rocky mountain, for dungeons and dragons ",
"painting of the inside of a fantasy roman fort, in a mountain pass, for dungeons and dragons ",
"painting of roman fort with an open portcullis, sitting in a mountain valley, for dungeons and dragons "
"painting of roman generals walking in dimly lit hall with marble columns, for dungeons and dragons ",
"painting of roman generals standing around table with maps on it, dimly lit room, for dungeons and dragons ",
"painting of dungeons and dragons fighters walking down hall with torches in the walls, for dungeons and dragons ",
"painting of fantasy castle wall with catapults in front of it, for dungeons and dragons ",
"painting of mongolian trading house, in wide open field, for dungeons and dragons ",
"painting of fantasy spooky dark forest, for dungeons and dragons ",
"painting of roman military hall, with battle maps, for dungeons and dragons ",
"painting of fantasy tavern, with lavender smoke filling the air, for dungeons and dragons ",
"painting of fantasy dungeon with torture chamber, for dungeons and dragons ",
"painting of roman fantasy dungeon with cell doors, for dungeons and dragons ",
"painting of fantasy roman castle in the mountains, for dungeons and dragons ",
"painting of fantasy roman city bustling with trade, for dungeons and dragons ",
"painting of old keep, stone walls, in mountain valley, for dungeons and dragons ",
"painting of fantasy keep in the desert, for dungeons and dragons ",
"painting of fantasy persian brass palace in the desert, for dungeons and dragons ",
"painting of fantasy byzantine port city with boats and brass buildings, for dungeons and dragons ",
"painting of fantasy persian market square, with trading carts, for dungones and dragons ",
"painting of smoke filled room with brass statues, for dungeons and dragons ",
"painting of gloomy caves, glowing with energy, for dungeons and dragons ",
"painting of fantasy library, filled with old books, dimly lit, for dungeons and dragons ",
"painting of wide open green field with mountains in the background, for dungeons and dragons ",
"painting of tall forbidding mountains, for dungeons and dragons "
]

obs_prompts = ["painting of magical mist draining the life force from fantasy villagers",
               "painting of a magical grey glowing cloud in a fantasy persian village",
               "painting of a fantasy spell from dungeons and dragons",
               "magical spell dungeons and dragons blasting death magic",
               "eldritch spell energy dark red clouds swirling magic",
               "assassin wearing a blue cloak with a scar for dungeons and dragons",
               "a charming bard with an evil grin and a lute for dungeons and dragons",
               "fantasy assassin in a city for conan"]

old_obs_prompts = [
"painting of a fantasy ranger in a cloak sitting on a rock smoking a pipe with gray smoke rings coming out of it ",
"drawing of a pipe on a table, sitting next to a blue and white poweder ",
"drawing of a fantasy traveler, sitting in a dimly lit tavern, smoking a pipe with stars and moons flying out of it ",
"painting of dimly lit, crowded fantasy tavern, for dungeons and dragons ",
"painting of a fat mongolian merchant in fine clothes standing next to a tavern, for dungeons and dragons ",
"painting of a colorful magical tome, glowing with magical energy, for dungeons and dragons ",
"painting of a female rogue wearing a cloak, sneaking into a dark vault with a torch on the wall and a table with books on it, for dungeons and dragons ",
"painting of glowing blue magical energy swirling above a persian village, for dungeons and dragons "
]

negative_prompt = "picture frame, poorly drawn, ugly, tiling, out of frame, mutation, mutated, extra limbs, extra legs, extra arms, disfigured, deformed, cross-eye, body out of frame, blurry, bad art, bad anatomy, blurred, text, watermark, grainy, writing, calligraphy, sign, cut off, cartoon, vector art, clipart, distorted, amateur, split"

odl_ast_prompts = ["painting of bread in medieval tavern",
                    "painting of grapes in medieval tavern",
                    "painting of mug of ale in medieval tavern",
                    "painting of fantasy scarf with persian design",
                    "painting of fantasy spell turning lead into gold",
                    "painting of fantasy spell polymorph other for dungeons and dragons",
                    "painting of medieval cannons for dungeons and dragons",
                    "painting of fantasy war machine for dungeons and dragons",
                    "painting of fantasy medieval love letter",
                    "painting of mysterious message using magical ink",
                    "painting of scribe hireling for dugeons and dragons",
                    "painting of torchbearer hireling for dungeons and dragons",
                    "painting of sharp fantasy sword",
                    "painting of large fantasy crowssbow for dungeons and dragons",
                    "painting of massive fantasy crossbow firing magical bolt",
                    "painting of magical potion for dungeons and dragons",
                    "painting of fantasy costume ball mask for dungeons and dragons",
                    "painting of fantasy costume ball dress for dungeons and dragons",
                    "painting of fantasy armor for dungeons and dragons",
                    "painting of fantasy mongolian armor",
                    "painting of fantasy roman armor",
                    "painting of bubbling cauldron for dungeons and dragons",
                    "painting of wineskin for dungeons and dragons",
                    "painting of flint and steel for dungeons and dragons",
                    "painting of lyre sitting on table for dungeons and dragons",
                    "painting of fantasy drums",
                    "painting of rope for dungeons and dragons",
                    "painting of burlap sack for dungeons and dragons",
                    "painting of fantasy tent for dungeons and dragons",
                    "painting of crossbow sitting on table for dungeons and dragons",
                    "painting of scarf for dungeons and dragons",
                    "painting of cat familiar for dungeons and dragons",
                    "painting of turtle familiar for dungeons and dragons",
                    "painting of dog companion for dungeons and dragons",
                    "painting of fantasy dog",
                    "painting of fantasy dragonfly for dungeons and dragons",
                    "painting of arrows sitting on a medieval table",
                    "painting of a fantasy longbow sitting against a forest tree",
                    "painting of a fantasy grappling hook for dungeons and dragons",
                    "painting of fantasy climbing spikes for dungeons and dragons",
                    "painting of an apple on a medieval table",
                    "painting of a wizard walking into a portal for dungeons and dragons",
                    "painting of an arcane trickster walking to a magical portal for dungeons and dragons"]

ast_prompts = ["fantasy dungeons and dragons magical wand of mirrors",
               "fantasy dungeons and dragons magic item mirrors of heat",
               "painting of fantasy mirror weapon",
               "fantasy painting dungeons and dragons mirror artifact"]

back_prompts = ["byzantine mosaic of lavender and crimson",
                "byzantine mosaic",
                "persian pattern from sasanian empire",
                "persian pattern"]

prompts = back_prompts

# Standard: 768px x 768px

# Generating imagery for 240dpi, a little lower than the normal 300dpi, but still looks okay

# Trade board at 240dpi: 18.25in x 18.25in (4380px x 4380px)
# height = 768
# width = 768

# Obstacle imagery at 300dpi: 2.25in x 2.093in (675px x 628px)
# height = 624
# width = 672

# Location imagery at 240dpi: 3.83in x 2.154in (920px x 520px)
# height = 520
# width = 920

# Large location imagery at 300dpi: 5.75 x 3.06 (1725px x 920px)
# Large location imagery at 240dpi: 1380px x 734px
# Asset imagery at 300dpi: 2.75 in x 1.4 in (825px x 420px)
# width = 832
# height = 424

# Changed asset to 2.75 in x 1.76 in (825px x 528px)
# width = 832
# height = 528

# Card backgrounds 2.75 in x 3.75 in
width = 832
height = 1128

# Square asset, must be cropped
# height = 592
# width = 832

for i in range(200):

    prompt = random.choice(prompts)

    # Randomly sample 1-3 artists for style matching
    artist_string = ""

    artist_list = random.sample(artists, random.randint(1,3))
    for next_artist in artist_list:
        if artist_string == "":
            artist_string = next_artist
        else:
            artist_string = artist_string + " and " + next_artist

    artist_prompt = prompt + ", in the style of " + artist_string

    seed = random.randint(1, 200000)
    steps = random.randint(40, 90)
    high_noise_frac = 0.8

    guidance_scale = round(random.uniform(5.0, 10.0), 2)

    # load both base & refiner
    base = StableDiffusionXLPipeline.from_pretrained(
        "stabilityai/stable-diffusion-xl-base-1.0", torch_dtype=torch.float16, variant="fp16", use_safetensors=True
    )
    base.to("cuda")
    # base is StableDiffusionXLPipeline

    refiner = StableDiffusionXLImg2ImgPipeline.from_pretrained(
        "stabilityai/stable-diffusion-xl-refiner-1.0",
        text_encoder_2=base.text_encoder_2,
        vae=base.vae,
        torch_dtype=torch.float16,
        use_safetensors=True,
        variant="fp16",
    )
    refiner.to("cuda")
    # refiner is StableDiffusionXLImg2ImgPipeline

    image = base(prompt = artist_prompt,
                 negative_prompt = negative_prompt,
                 num_inference_steps = steps,
                 #denoising_end = high_noise_frac,
                 output_type = "latent",
                 height = height,
                 width = width
                 ).images
    
                #  output_type = "latent").images[0]
    
    refined_image = refiner(prompt = artist_prompt,
                            negative_prompt = negative_prompt,
                            # num_inference_steps = steps,
                            #denoising_end = high_noise_frac,
                            image=image).images[0]

    # guidance_str = str(guidance_scale).replace('.', '_')

    try:
        refined_image.save("images\\ai_in_progress\\" + artist_prompt[-150:] + " " + str(steps) + " " + str(seed) + ".png")
    except Exception as e:
        print(e)