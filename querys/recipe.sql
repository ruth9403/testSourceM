CREATE DATABASE mytest;

CREATE TABLE recipes(
	id INT PRIMARY key,
	name VARCHAR(100), 
	minutes INT,
	contributor_id INT, 
	submited DATE, 
	n_ingredients INT,
	n_steps INT,
	description VARCHAR(10000)
);
	
CREATE TABLE IF NOT EXISTS recipes_tags(
	id INT AUTO_INCREMENT PRIMARY key,
	tag_name VARCHAR(100),
	recipe_id INT NOT null
);
	
CREATE TABLE IF NOT EXISTS recipes_steps(
	id INT AUTO_INCREMENT PRIMARY key,
	step_name VARCHAR(100) UNIQUE,
	recipe_id INT UNIQUE NOT null
);
	
CREATE TABLE IF NOT EXISTS  recipes_ingredients(
	id INT AUTO_INCREMENT PRIMARY key,
	ingredient_name VARCHAR(100) UNIQUE,
	recipe_id INT UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS  interactions(
	id INT AUTO_INCREMENT PRIMARY key,
	userId INT NOT NULL,
	recipe_id INT NOT NULL,
	published DATE, 
	rating INT,
	review TEXT
);

ALTER TABLE recipes_tags
ADD CONSTRAINT FK_recipeId_tags
FOREIGN KEY (recipe_id) REFERENCES recipes(id);

ALTER TABLE recipes_steps
ADD CONSTRAINT FK_recipeId_steps
FOREIGN KEY (recipe_id) REFERENCES recipes(id);

ALTER TABLE recipes_ingredients
ADD CONSTRAINT FK_recipeId_ingredients
FOREIGN KEY (recipe_id) REFERENCES recipes(id);

ALTER TABLE interactions
ADD CONSTRAINT FK_recipeId_interactions
FOREIGN KEY (recipe_id) REFERENCES recipes(id);

ALTER TABLE mytest.recipes CONVERT TO CHARACTER SET utf8