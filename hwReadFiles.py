import os
from pprint import pprint

FILE = "recipes.txt"
FILE_DIR = "recipes"
ROOT_PATH = os.getcwd()
full_path = os.path.join(ROOT_PATH, FILE_DIR, FILE)

with open(full_path, encoding="utf-8") as file:
    cook_book = {}
    for line in file:
        dish = line.strip()
        ingr_quantity = file.readline().strip()
        ingredients = []
        for ingr in range (int(ingr_quantity)):
            ingr_line = []
            ingr_line.append(file.readline().strip().split(" | "))        
            ingredients.append({
                "ingredient_name" : ingr_line[0][0],
                "quantity" : ingr_line[0][1],
                "measure" : ingr_line[0][2]
                })    
        file.readline()
        cook_book[dish] = ingredients
            

def get_shop_list_by_dishes(dishes, pers_quantity):
    products = {}
    for dish in dishes:
        if dish in cook_book:
            for ingr in cook_book.get(dish):
                quantity = {}
                if ingr.get("ingredient_name") in products.keys():
                    products[ingr.get("ingredient_name")] = quantity
                    quantity["measure"] = ingr.get("measure") 
                    quantity["quantity"] = (int(ingr.get("quantity")) + int(ingr.get("quantity"))) * pers_quantity
                else:
                    products[ingr.get("ingredient_name")] = quantity
                    quantity["measure"] = ingr.get("measure") 
                    quantity["quantity"] = int(ingr.get("quantity")) * pers_quantity
    return products                
                        
             
pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))


