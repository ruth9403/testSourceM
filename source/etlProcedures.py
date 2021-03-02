# from Connection import Connection
# import os
# import numpy as np
# import pandas as pd

# con = Connection(user='DB_USER', password='DB_PASSWORD', database='DB_DATABASE')
# con = con.connect()
# con.close() #no Cierra TT_TT
#print('conection closed')

# with open('files/RAW_recipes.csv','r', newline='') as csvfile:
    #          recipe = csv.reader(csvfile, delimiter=',', quotechar='|')
    #          for row in recipe:
    #             print(', '.join(row))
    


###Trying Ingredients
#Subsetting the Dataframe into the columns needed
# recipes_ingredients= recipes[['id','ingredients']]
# print(recipes_ingredients.head())

# #Reading PP recipies.csv
# pprecipes = pd.read_csv('files/PP_recipes.csv')

# #Subsetting the Dataframe into the columns needed
# pprecipes_sub = pprecipes[['id','ingredient_ids']]
# print(pprecipes_sub.head())

# #Merging Dataframes
# result = pd.merge(recipes_ingredients,
#                  pprecipes_sub,
#                  on='id')
# print(result.head())
# print(result.info())

# #Converting column ingredients from str  to array
# for index, row in result.iterrows():
#     row['ingredients'] = row['ingredients'].replace(row['ingredients'], ast.literal_eval(row['ingredients']))

# result_testing = result.iloc[:5,:]
# print(type(result_testing['ingredients'][0]))
# #
# #separated = pd.DataFrame(data, columns = ['Name', 'Age'])
# separated = []
# for index, row in result_testing.iterrows():
#     for ingredient in row['ingredients']:
#         separated.append([row['id'],ingredient,row['ingredient_ids']])
# print(separated)
