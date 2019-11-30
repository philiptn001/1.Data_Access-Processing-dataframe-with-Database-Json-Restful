# Data_Access: Processing dataframe with Database, Json, Restful
Project to read data from  CSV, Relational Databases, NoSQL databases and RESTful APIs.

## Project 1:
Project to read data from  CSV and save it back to another CSV
Steps:
* Read the CSV file as pandas dataframe.
* Print the columns / rows of the dataframe
* Save the dataframe as a CSV file 

## Project 2:
Project to read data from  CSV and save it to Relational Databases (sqlite)
Steps:
* Load the CSV file as pandas dataframe
* Store the dataframe in sqlite database
* Query the database and load the data into a new dataframe again

## Project 3:
Project to store a dataframe in MongoDB and how query the database and create a dataframe
Steps:
* Load the CSV file as pandas dataframe
* Install mongodb on your local machine
* Create a database named demographic with a collection named Demographic_Statistics
* Write the dataframe in mongodb
* Query the database and load the data into a new dataframe again

## Project 4:
Project to create a RESTful request, and process JSON objects into dataframes
Steps:
* Using the below url, create a get request and fetch the JSON programmatically
* GET https://data.cityofnewyork.us/api/views/kku6-nxdu/rows.json
* Create a dataframe out of the JSON object created in the previous step
