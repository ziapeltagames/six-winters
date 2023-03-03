# Used for prototype art

import random
import torch

from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler

artists = ["wayne reynolds", "john stanko", "kieran yanner", "artgerm", "greg rukowski", "alphonse mucha",
"clyde caldwell", "john blanche", "russ nicholson", "larry elmore", "jeff easley", "erol otus", 
"brom", "ian miller", "keith parkinson", "frank frazetta", "daniel horne", "doug kovacs",
"ned rogers", "nixeu", "william-adolphe bouguereau", "greg hildebrandt",
"mahmud asrar", "tuomas korpi", "titian", "charlie bowater", "n. c. wyeth", "arthur rackham"]

# Less appropriate artist prompts
# gustave dore: usually black and white, detailed etchings
# edmund dulac: muted tones
# michael garmash: heavy brush strokes, more abstract

loc_prompts = []
    
old_loc_prompts = ["painting of fantasy persian city on the sea, with many houses and markets, boats are in the harbor, sun is setting, the beaches are crimson, for dungeons and dragons, in the style of  ",
"painting of a cloaked fantasy figure, walking through the snow, between tall rocky mountains, setting sun, stars coming out above, in the style of ",
"painting of four seasons, swirled together in a circle, mixing, in the style of ",
"painting of travelers in the distance, walking through a snowy mountain pass, tall mountains surround them, in the style of ",
"painting of fantasy persian city on the sea, boats are in the harbor, sun is setting, the beaches are crimson, for dungeons and dragons, in the style of  ",
"painting of will o wisps in a swamp, the water is glowing orange and blue, vines hang above the water, for dungeons and dragons, in the style of ",
"painting of a fantasy throne room, for dungeons and dragons, with pale lavender lighting, high brass arches, in the style of ",
"painting of ghosts floating through dense forest, with purple clouds floating overhead, for dungeons and dragons, in the style of ",
"painting of a magical forest, with translucent purple ghost trees and dark gray rivers, for dungeons and dragons, in the style of ",
"painting of byzantine throne room, with brass throne, and red carpets, pale lavender lighting, in the style of ",
"painting of a ruined fantasy city, crumbling walls, crows flying overhead, the sun is setting, for dungeons and dragons, in the style of ",
"painting of magical wizard's tower, rising above celtic village, with stars in the sky, in the style of ",
"painting of wizard's tower, rising above celtic village, with hills in the background, in the style of ",
"painting of long persian hall, with brass doors, and brass statues on either side of a lavender carpet, in the style of ",
"painting of long hall in persian castle, with brass doors both sides, in the style of ",
"painting of desolate plains in mongolia, with rain clouds overhead, in the style of ",
"painting of an alley in a fantasy city for dungeons and dragons, rain clouds are overhead, the houses are dreary, in the style of ",
"painting of a slavic village, with a stream running through it, deep in the forest, in the style of",
"painting of a large wooden fantasy building, long and narrow, in a mountain valley, in the style of",
"painting of a long fantasy hall, full of mirrors, and sunlight coming through windows high in the ceiling, in the style of ",
"painting of a fantasy cottage, built into the top of a large tree, in a dense forest, in the style of ",
"painting of a fantasy persian house, built into a large forest, with a stream running past, in the style of ",
"painting of fantasy tavern, with lavender smoke swirling around the customers, in the style of ",
"painting of a fantasy opium den, with lavender pillows and a large brass hookah, with lavender smoke swirling around, in the style of ",
"painting of rocky columns forming an eldritch helix, standing on a hill, in the style of ",
"painting of fields of wheat and barley in an ancient valley, with farm houses in the distance, in the style of ",
"painting of ancient roman farms, with hills in the backgrounds, in the style of ",
"painting of small valley with a narrow stream running through it, trees on both sides of the stream, leaves are over the stream in the style of ",
"painting of a green field with rocky monuments for dungeons and dragons, in the style of ",
"painting of fantasy female roman peasent standing next to cart filled with squid and octopus, in the style of ",
"painting of fantasy fish merchant stall, selling squid and octopus, in the style of ",
"painting of dark forest with white and gray trees, colorful mushrooms grow on the ground, in the style of ",
"painting of fantasy fishmonger, with cart carrying squid and octopus, for dungeons and dragons, in the style of ",
"painting of fantasy persian village with trading carts and amaranth, for dungeons and dragons, in the style of ",
"painting of fantasy military fort with white walls in the hills for dungeons and dragons, in the style of ",
"painting of fantasy dungeon hall with many jail cells, dim lighting from torches, for dungeons and dragons, in the style of ",
"painting of fantasy prison with many jail cells, for dungeons and dragons, in the style of ",
"painting of medieval torture devices, for dungeons and dragons, in the style of ",
"painting of roman fort in the hills, for dungeons and dragons, in the style of ",
"painting of dimly lit, crowded fantasy tavern, for dungeons and dragons, in the style of ",
"painting of persian castle made of brass in the distance with a field of amaranth, for dungeons and dragons, in the style of ",
"painting of glowing blue forest, dense trees, ghosts, for dungeons and dragons, in the style of ",
"painting of stone statues of skulls and tentacles on a rocky mountain, for dungeons and dragons, in the style of ",
"painting of the inside of a fantasy roman fort, in a mountain pass, for dungeons and dragons, in the style of ",
"painting of roman fort with an open portcullis, sitting in a mountain valley, for dungeons and dragons, in the style of "
"painting of roman generals walking in dimly lit hall with marble columns, for dungeons and dragons, in the style of ",
"painting of roman generals standing around table with maps on it, dimly lit room, for dungeons and dragons, in the style of ",
"painting of dungeons and dragons fighters walking down hall with torches in the walls, for dungeons and dragons, in the style of ",
"painting of fantasy castle wall with catapults in front of it, for dungeons and dragons, in the style of ",
"painting of mongolian trading house, in wide open field, for dungeons and dragons, in the style of ",
"painting of fantasy spooky dark forest, for dungeons and dragons, in the style of ",
"painting of roman military hall, with battle maps, for dungeons and dragons, in the style of ",
"painting of fantasy tavern, with lavender smoke filling the air, for dungeons and dragons, in the style of ",
"painting of fantasy dungeon with torture chamber, for dungeons and dragons, in the style of ",
"painting of roman fantasy dungeon with cell doors, for dungeons and dragons, in the style of ",
"painting of fantasy roman castle in the mountains, for dungeons and dragons, in the style of ",
"painting of fantasy roman city bustling with trade, for dungeons and dragons, in the style of ",
"painting of old keep, stone walls, in mountain valley, for dungeons and dragons, in the style of ",
"painting of fantasy keep in the desert, for dungeons and dragons, in the style of ",
"painting of fantasy persian brass palace in the desert, for dungeons and dragons, in the style of ",
"painting of fantasy byzantine port city with boats and brass buildings, for dungeons and dragons, in the style of ",
"painting of fantasy persian market square, with trading carts, for dungones and dragons, in the style of ",
"painting of smoke filled room with brass statues, for dungeons and dragons, in the style of ",
"painting of gloomy caves, glowing with energy, for dungeons and dragons, in the style of ",
"painting of fantasy library, filled with old books, dimly lit, for dungeons and dragons, in the style of ",
"painting of wide open green field with mountains in the background, for dungeons and dragons, in the style of ",
"painting of tall forbidding mountains, for dungeons and dragons, in the style of "
]

obs_prompts = ["painting of a fantasy guard wearing a red cloak, standing in an alley, for dungeons and dragons, in the style of ",
"painting of roman legionary, standing in a field, in the style of "]

old_obs_prompts = [
"painting of dimly lit, crowded fantasy tavern, for dungeons and dragons, in the style of ",
"painting of a fat mongolian merchant in fine clothes standing next to a tavern, for dungeons and dragons, in the style of ",
"painting of a colorful magical tome, glowing with magical energy, for dungeons and dragons, in the style of ",
"painting of a female rogue wearing a cloak, sneaking into a dark vault with a torch on the wall and a table with books on it, for dungeons and dragons, in the style of ",
"painting of glowing blue magical energy swirling above a persian village, for dungeons and dragons, in the style of "
]

negative_prompt = "poorly drawn, ugly, tiling, out of frame, mutation, mutated, extra limbs, extra legs, extra arms, disfigured, deformed, cross-eye, body out of frame, blurry, bad art, bad anatomy, blurred, text, watermark, grainy, writing, calligraphy, sign, cut off, cartoon, vector art, clipart, distorted, amateur, split"

prompts = obs_prompts

# Standard: 768px x 768px

# Generating imagery for 240dpi, a little lower than the normal 300dpi, but still looks okay

# Trade board at 240dpi: 18.25in x 18.25in (4380px x 4380px)
#height = 768
#width = 768

# Obstacle imagery at 300dpi: 2.25in x 2.093in (675px x 628px)
height = 624
width = 672

# Location imagery at 240dpi: 3.83in x 2.154in (920px x 520px)
#height = 520
#width = 920


for i in range(1000):

    prompt = random.choice(obs_prompts)

    # Randomly sample 1-3 artists for style matching
    artist_string = ""

    artist_list = random.sample(artists, random.randint(1,3))
    for next_artist in artist_list:
        if artist_string == "":
            artist_string = next_artist
        else:
            artist_string = artist_string + " and " + next_artist

    artist_prompt = prompt + artist_string

    seed = random.randint(1, 200000)
    steps = random.randint(50, 150)

    guidance_scale = round(random.uniform(5.0, 10.0), 2)

    model_id="stabilityai/stable-diffusion-2-1"

    pipe = StableDiffusionPipeline.from_pretrained(model_id)

    # pipe.scheduler = EulerDiscreteScheduler.from_config(pipe.scheduler.config)
    pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)

    pipe = pipe.to("cuda")
    pipe.enable_attention_slicing()

    generator = torch.Generator("cuda").manual_seed(seed)

    print('Generating ', artist_prompt, i)

    image = pipe(artist_prompt, negative_prompt=negative_prompt, height=height, width=width, guidance_scale = guidance_scale, num_inference_steps=steps, generator=generator).images[0]

    guidance_str = str(guidance_scale).replace('.', '_')

    try:
        image.save("images\\ai_in_progress\\" + artist_prompt[-150:] + " " + guidance_str + " " + str(steps) + " " + str(seed) + ".png")
    except Exception as e:
        print(e)