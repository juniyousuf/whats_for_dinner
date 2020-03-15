import sys
import pandas
import time
import pyspark as spark
import pyspark.sql.functions as F
import json


from src.validator.validate_csv import validate_csv_data


if __name__== "__main__":
    
    ingredients_path="./source_files/my-fridge.csv"
    recipes_path="./source_files/my-recipes.json"
    try: 
        ingredients = pandas.read_csv(ingredients_path)
        recipes = pandas.read_json(recipes_path, orient='records')
    except:
        print("Can't read Fridge ingredients csv.")
    
    # print(recipes.ingredients)
    print(validate_csv_data(ingredients))
    # print((recipes["ingredients"]))
    # print("======================")
    # recipes = recipes.join(recipes['ingredients'].apply(pandas.Series))
    # print(recipes)
    # print("======================")
    
    # print(d[0])
