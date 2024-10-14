
import json

# Run this script on the overworld_all_biomes.json and overwrite data/minecraft/dimension/overworld.json with it

# If for some reason this .json is missing or modified then generate a new one from:
# https://misode.github.io/dimension/?version=1.19 (preset: overworld)

# if any biomes contain this name, then they are removed also
# eg. "swamp" includes "mangrove_swamp"
unwanted_biomes_partnames = [
    "deep_", # oceans
    "swamp",
    "slopes",
    "badlands",
    "peaks",
    "jungle",
    "ice_spikes",
    "warm_",
    "plateau",
    "frozen",
    "cold",
    "snowy"
]

unwanted_biomes_wholenames = [
    "warm_ocean"
]

leftover_biomes = []
untrimmed_biomes = []


with open("overworld_all_biomes.json", "r+") as json_file:

    json_data = json.load(json_file)

    starting_biomes = json_data["generator"]["biome_source"]["biomes"]

    for biome in starting_biomes:
        unwanted = False
        for unwanted_biome in unwanted_biomes_partnames:
            if unwanted_biome in biome["biome"]:
                unwanted = True
                break
        for unwanted_biome in unwanted_biomes_wholenames:
            if unwanted_biome == biome["biome"]:
                unwanted = True
                break
        if not unwanted:
            leftover_biomes.append(biome)

    json_data["generator"]["biome_source"]["biomes"] = leftover_biomes
    json_file.seek(0)
    json.dump(json_data, json_file, indent=4)
    json_file.truncate()

    
print(leftover_biomes)

print("starting_biomes: " + str(len(starting_biomes)))
print("leftover_biomes: " + str(len(leftover_biomes)))