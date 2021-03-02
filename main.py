import os
from source.connection import Connection
import numpy as np
import pandas as pd
import csv
import ast

if __name__ == "__main__":
    con = Connection(user=os.environ['DB_USER'], 
                    password=os.environ['DB_PASSWORD'], 
                    database=os.environ['DB_DATABASE'], 
                    host=os.environ['DB_HOST'])

    
    ###Inserting Data into RECIPES TABLE*-------------------------------------------------------------*
    
    #Reading csv
    recipes = pd.read_csv('files/RAW_recipes.csv')
    #print(recipes.info())
    #Subsetting the Dataframe into the columns needed
    recipes_table = recipes[['name', 'id','minutes','contributor_id','submitted','n_ingredients','n_steps', 'description']]
    
    #Taking care of nan Values
    #print(recipes_table.isnull().any())
    recipes_table['name'] = recipes_table['name'].fillna(0)
    recipes_table['description'] = recipes_table['description'].fillna(0)
    #print(recipes_table.isnull().any())#verifying filled nans OK
    
    #Testing with smaller data
    #recipes_testing = recipes_table.iloc[:5,:]
    #print(recipes_testing)

    #Inseting the Df rows to BD, recipes Table 
    for index,row in recipes_table.iterrows():
        sql_insert = """INSERT IGNORE INTO recipes (id, name, minutes, contributor_id, submited, n_ingredients, n_steps, description) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
        params = (row["id"], 
                row['name'], 
                row['minutes'], 
                row['contributor_id'], 
                row['submitted'], 
                row['n_ingredients'], 
                row['n_steps'], 
                row['description'])
        con.executeQuery(query=sql_insert, params=params)
        print(f'index {index} - {row["id"]}')
    con.commit()
        #print(f'{row["name"]}, {row["minutes"]} ')


###Inserting Data into RECIPE_TAGS TABLE//////////////////////////////////////////////////////////////////////

#Subsetting the Dataframe into the columns needed
recipes_tags_table = recipes[['id','tags']]
#print(recipes_tags_table.head())

#Testing with smaller data
# recipes_tags_table_testing = recipes_tags_table.iloc[:5,:]
# print(recipes_tags_table_testing)

#Inseting the Df rows to BD, recipes_tags Table 
for index,row in recipes_tags_table.iterrows():
    sql_insert = """INSERT IGNORE INTO recipes_tags (tag_name, recipe_id) VALUES (%s, %s)"""
    params = (row["tags"], 
            row['id'])
    con.executeQuery(query=sql_insert, params=params)
    print(f'index {index} - {row["id"]}')
con.commit()


###Inserting Data into INTERACTIONS TABLE++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#Reading csv
interactions = pd.read_csv('files/RAW_interactions.csv')
# print(interactions.head())
# print(interactions.info())

#Taking care of nan Values
#print(interactions.isnull().any())
interactions['review'] = interactions['review'].fillna(0)
#print(interactions.isnull().any())#verifying filled nans OK

#Testing with smaller data
# interactions_testing = interactions.iloc[:5,:]
# print(interactions_testing)

#Inseting the Df rows to BD, interactions Table 

for index,row in interactions.iterrows():
    sql_insert = """INSERT IGNORE INTO interactions (userId, recipe_id, published, rating, review) VALUES (%s, %s, %s, %s, %s)"""
    params = (row['user_id'], 
            row['recipe_id'], 
            row['date'], 
            row['rating'], 
            row['review'])
    con.executeQuery(query=sql_insert, params=params)
    print(f'index {index} - {row["user_id"]}')
con.commit()
    # print(f'{row["user_id"]}, {row["rating"]} ')



