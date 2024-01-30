from os import listdir, chdir
from json import loads, dumps

chdir("E:/Program Files/Minecraft/.minecraft/versions/[1.20.1][Fabric]Xplus 2.0/config/openloader/data/jsm")
resourceDir = "resources/botanypots"
resources = listdir(resourceDir)
for resource in resources:
    recipe = ""
    with open(resourceDir + "/" + resource, "r") as file:
        recipe = file.read()
        file.close()
    recipe = loads(recipe)
    if recipe["type"] == "minecraft:crafting_shapeless":
        continue
    recipe["pattern"][-1] = recipe["pattern"][-1].replace(" ", "F")
    recipe["key"]["F"] = {"tag": "c:steel_blocks"}
    with open("data/botanypots/recipes/botanypots/crafting/" + resource, "w") as file:
        file.write(dumps(recipe, indent="    "))
        file.close()