from os import listdir, chdir

def extractElement(raw:str) -> str:
    return raw[:-10]

def generateRecipe(element:str) -> str:
    return f'''
{"{"}
    "bookshelf:load_conditions": [
        {"{"}
            "type": "bookshelf:item_exists",
            "values": [
                "stemaria:seed_stem_{element}",
                "stemaria:{element}_melon"
            ]
        {"}"}
    ],
    "type": "botanypots:crop",
    "seed": {"{"}
        "item": "stemaria:seed_stem_{element}"
    {"}"},
    "categories": [
        "dirt",
        "farmland"
    ],
    "growthTicks": 2400,
    "display": {"{"}
        "type": "botanypots:aging",
        "block": "croparia:block_crop_{element}"
    {"}"},
    "drops": [
        {"{"}
            "chance": 1.00,
            "output": {"{"}
                "item": "stemaria:{element}_melon"
            {"}"}
        {"}"},
        {"{"}
            "chance": 0.01,
            "output": {"{"}
                "item": "stemaria:seed_stem_{element}"
            {"}"}
        {"}"}
    ]
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
        with open("xpp/data/stemaria/recipes/botanypots/" + element + ".json", "w") as file:
            file.write(recipe)
            file.close()