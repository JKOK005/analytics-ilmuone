## Ilmuone Data environment set analytics
Done by 	: Johan Kok Zhi Kang
Date 		: 18-08-2017
dataset 	: data/environ.xlsx

### Description
This repository contains and automated document generator that generates graphical plots from a test set provided
by Ilmuone Data. The test set contains data which is highly unstructured and inconsistent. 

My approach is to first perform initial filtering of the dataset based on observations of the general pattern within the data. 
After filtering, the data is then migrated into a PostgreSQL database for robust querying. I then developed an API that allows
users to generate graphical interfaces given a **country_code** and **indicator_code**. This graph contains histroical information 
provided by the dataset and also gives added information based on notes in the meta data sheet.

### Execution
Please refer to folders:
- scripts 
- octave

for a detailed desription on how to execute the programme. 