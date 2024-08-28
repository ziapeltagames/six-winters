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

negative_prompt = "picture frame, poorly drawn, ugly, tiling, out of frame, mutation, mutated, extra limbs, extra legs, extra arms, disfigured, deformed, cross-eye, body out of frame, blurry, bad art, bad anatomy, blurred, text, watermark, grainy, writing, calligraphy, sign, cut off, cartoon, vector art, clipart, distorted, amateur, split"

loc_prompts = ["painting of golden hills with small stream and magical forest for dungeons and dragons",
               "painting of golden hills with large mountains behind them for dungeons and dragons"]

obs_prompts = ["fantasy painting of twisted tree roots oozing a black deathly substance",
               "fantasy painting of twisted bloody roots an evil ball",
               "fantasy painting of a white dragon staring coldly ahead",
               "fantasy painting of a tawny dragon with a laughing expression",
               "fantasy painting for dungeons and dragons of fantasy merchants yelling at each other"]

ast_prompts = ["a corporate icon of an ankylosaurus with a 20 sided die for a tail",
               "a graphic design of an ankylosaurus with a d20 on its tail",
               "a corporate logo featuring a brown ankylosaurus dinosaur",
               "a dinosaur logo with a d20 for a body",
               "a fantasy dinosaur logo with a 20 sided die for a body"]

back_prompts = ["byzantine mosaic of lavender and crimson",
                "byzantine mosaic",
                "persian pattern from sasanian empire",
                "persian pattern"]

prompts = ast_prompts

# Generating imagery for 240dpi, a little lower than the normal 300dpi, but still looks okay

# Obstacle imagery at 300dpi: 2.25in x 2.093in (675px x 628px)
# height = 624
# width = 672

# Location imagery at 240dpi: 5.75 x 3.0583
# width = 1384
# height = 736

# Changed asset to 2.75 in x 1.76 in (825px x 528px)
width = 832
height = 528

# Card backgrounds 2.75 in x 3.75 in
# width = 832
# height = 1128

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