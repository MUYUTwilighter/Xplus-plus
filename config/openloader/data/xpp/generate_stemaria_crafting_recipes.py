from os import listdir, chdir

def extractElement(raw:str) -> str:
    return raw[:-10]

def generateRecipe(element:str) -> str:
    return f'''
{"{"}
    "type": "minecraft:crafting_shapeless",
    "category": "misc",
    "ingredients": [
        {"{"}
            "item": "stemaria:{element}_melon"
        {"}"}
    ],
    "result": {"{"}
      "item": "techreborn:{element}_storage_block",
      "count": 1
    {"}"}
{"}"}
'''

# chdir("E:/Program Files/Minecraft/.minecraft/versions/[1.20.1][Fabric]Xplus 2.0/config/openloader/data/jsm")
resourceDir = "xpp/resources/stemaria_ct_loot-tables"
resources = listdir(resourceDir)
for resource in resources:
    if "attached" in resource:
        continue
    else:
        element = extractElement(resource)
        recipe = generateRecipe(element)
        print(element)
        with open("xpp/data/stemaria/recipes/crafting_table/" + element + ".json", "w") as file:
            file.write(recipe)
            file.close()