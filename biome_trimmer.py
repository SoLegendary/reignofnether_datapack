
import json

# if any biomes contain this name, then they are removed also
# eg. "swamp" includes "mangrove_swamp"
unwanted_biomes = [
    "deep_", # oceans
    "swamp",
    "slopes",
    "badlands",
    "peaks",
    "jungle",
    "ice_spikes",
    "desert",
    "plateau",
    "frozen",
    "cold",
    "snowy"
]

trimmed_biomes = []
untrimmed_biomes = []


with open("overworld_dimension.json", "r+") as json_file:

    json_data = json.load(json_file)

    untrimmed_biomes = json_data["generator"]["biome_source"]["biomes"]

    for biome in untrimmed_biomes:
        unwanted = False
        for unwanted_biome in unwanted_biomes:
            if unwanted_biome in biome["biome"]:
                unwanted = True
                break
        if not unwanted:
            trimmed_biomes.append(biome)

    json_data["generator"]["biome_source"]["biomes"] = trimmed_biomes
    json_file.seek(0)
    json.dump(json_data, json_file, indent=4)
    json_file.truncate()

    
print(trimmed_biomes)

print("untrimmed_biomes: " + str(len(untrimmed_biomes)))
print("trimmed_biomes: " + str(len(trimmed_biomes)))