# load-data-into-sql

This repository contains the source code of loading the CareerVillage dataset into a MySQL database. This dataset can be found [here](https://www.kaggle.com/competitions/data-science-for-good-careervillage/data)

## Pre-requisities to run this application
- Installed and running instance of MySQL server (tested on version 8.0.32)
- Python (tested on version 3.9.13)
- Python library: mysql-connector-python
- all csv files of the dataset in the same directory as this readme


## Code organization/ Directory structure
- `execute.sh` : Driver program - shell script used to run the application to load data into the dataset
- `createDB.py` : python script to create the required datbase
- `createTables.py` : python script to create the required tables
- `createDB.py` : python script to load csv file data into tables

## Running the application
Execute the following command

`./execute.sh`

The complete process of loading the data has been automated and progress updates are displayed on terminal

## Result
After successfully loading the daatset into MySQL the following databse will be created

![ER Diagram](https://user-images.githubusercontent.com/26086412/237060808-940d1ae2-9532-49a2-9b0b-73f8fc7d3a9e.png)

## Environment specifications
Following are the specifications of the environment on which this application was last executed/tested: 
- MacBook Air M1
- OS: Montery
- Memory: 16 GB
- MySQL version: Community Edition - 8.0.32
- Python version: 3.9.13

