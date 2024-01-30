from os import listdir, chdir

mapping = {
    "minecraft:iron_block": "ad_astra:desh_block",
    "minecraft:diamond_block": "ad_astra:ostrum_block",
    "minecraft:netherite_block": "ad_astra:calorite_block"
}

chdir("E:/Program Files/Minecraft/.minecraft/versions/[1.20.1][Fabric]Xplus 2.0/config/openloader/data/jsm")
resourceDir = "resources/botanypotstiers"
resources = listdir(resourceDir)
for resource in resources:
    recipe = ""
    with open(resourceDir + "/" + resource, "r") as file:
        recipe = file.read()
        file.close()
    for (old, new) in mapping.items():
        recipe = recipe.replace(old, new, 100)
    with open("data/botanypotstiers/recipes/crafting/" + resource, "w") as file:
        file.write(recipe)
        file.close()