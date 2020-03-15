import pandas
from pandas.io.json import json_normalize
import time
import pyspark as spark
import pyspark.sql.functions as F
import json


from src.validator.validate_csv import validate_csv_data


def getRecipes(recipes_path):
    try:
        df = pandas.read_json(recipes_path, orient='records')
    except:
        print("Can't read recipes.")
    
    # print(validate_csv_data(ingredients))
    recipes_exploded = df.explode('ingredients')
    recipes_exploded_expanded = recipes_exploded.ingredients.apply(pandas.Series)
    recipes=recipes_exploded.join(recipes_exploded_expanded)
    recipes=recipes.drop('ingredients',1)
    return (recipes.drop_duplicates(keep='first',inplace=False))

def getIngredients(ingredients_path):
    try:
        ingredients = pandas.read_csv(ingredients_path)
    except:
        print("Can't read ingredients from CSV file.")
    try:
        ingredients_validated = validate_csv_data(ingredients)
    except e:
        print(e)
    return ingredients_validated


if __name__== "__main__":
    
    ingredients_path="./source_files/my-fridge.csv"
    recipes_path="./source_files/my-recipes.json"
    
    ingredients=getIngredients(ingredients_path)
    recipes=getRecipes(recipes_path)

    

    print(ingredients)
    print("================")
    print(recipes)
    print("================")
    # result=pandas.merge()