## Database creation and data migration

This script creates the database schema for the project and thereafter migrates information
from excel to SQL. 

A local PostgreSQL database was created for this project under the credentials:
db name 	: environ
db user 	: ilumone
db password : ilumone

### Schema
The following tables and fields are represented below:

```
Table countries
(
	code 	varchar(5) 		NOT NULL,
	name 	varchar(100) 	NOT NULL,
	region 	varchar(50) 	NOT NULL,
	inc_grp varchar(50),
	notes 	varchar(40000),
	PRIMARY KEY(code)
);

Table indicators
(
	code 	varchar(20)		NOT NULL,
	name 	varchar(1000) 	NOT NULL,
	notes 	varchar(40000),
	PRIMARY KEY(code)
);

Table historical_data
(
	country_code 	varchar(5)		NOT NULL,
	indicator_code 	varchar(20) 	NOT NULL,
	y_1960 			float			NOT NULL,
	y_1961 			float 			NOT NULL, 
	... 
	y_2015 			float			NOT NULL,

	FOREIGN KEY(country_code) REFERENCES Countries(code),
	FOREIGN KEY(indicator_code) REFERENCES Indicators(code)
);

```

### Execution
First generate the database schema and tables using the command
``` python
python GenEnvironDb.py
```

Thereafter, migrate the data in excel over to the relevant tables using
``` python
python Migrate.py
```

Note: **GenEnvironDb** does not rebuild the table one it has been established in the database.
However, Migrate.py will cause data replication or may throw a primary key duplication error. 

### Table deletion
To delete a table in case of a mistake or changes done to the table, we need to manually
access the database through admin privileges. 

Thereafter, run the **GenEnvironDb.py** script to rebuilt the tables and **Migrate.py** to
export excel data into SQL format. 