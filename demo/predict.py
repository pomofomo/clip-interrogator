from PIL import Image
from clip_interrogator import Config, Interrogator

import time

# caption_model_name = 'blip-base' / 'blip-large' (default)
ci = Interrogator(Config(clip_model_name="ViT-B-32-quickgelu/openai"))
# ci = Interrogator(Config(clip_model_name="ViT-L-14/openai"))


print("starting interrogation")

start = time.time()
# Make them both 256x256 (not sure if pre-processing is important)
image1 = Image.open("./images/sd-girl-night.png").convert('RGB')
image2 = Image.open("./images/girl-dancing.jpg").convert('RGB')
duration = time.time() - start
print(f"Loaded images in {duration} s")

start = time.time()
# prompt1 = ci.interrogate(image1)
# prompt2 = ci.interrogate(image2)
prompt1 = ci.interrogate_classic(image1) # (or _fast)
prompt2 = ci.interrogate_classic(image2)
duration = time.time() - start
print(f"Interrogated classic in {duration/2} s")

start = time.time()
neg1 = ci.interrogate_negative(image1)
neg2 = ci.interrogate_negative(image2)
duration = time.time() - start
print(f"Interrogated negative in {duration/2} s")


print(f"Image 1: {prompt1}")
print(f"Image 2: {prompt2}")

print(f"Neg 1: {neg1}")
print(f"Neg 2: {neg2}")
