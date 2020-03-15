import sys
import pandas
import time
import pyspark as spark
import pyspark.sql.functions as F
import json
from pandas.io.json import json_normalize


from src.validator.validate_csv import validate_csv_data


if __name__== "__main__":
    
    ingredients_path="./source_files/my-fridge.csv"
    recipes_path="./source_files/my-recipes.json"
    try: 
        ingredients = pandas.read_csv(ingredients_path)
        recipes = pandas.read_json(recipes_path, orient='records')
    except:
        print("Can't read Fridge ingredients csv.")
    
    print(recipes)
    # test_json_normalize = 
    # print(validate_csv_data(ingredients))
    # print((recipes["ingredients"]))
    # print("======================")
    # recipes = recipes.join(recipes['ingredients'].apply(pandas.Series))
    # print(recipes)
    # print("======================")
    with open(recipes_path) as f:
        d = json.load(f)
    
    # print(d[0])
