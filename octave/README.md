## Database query and insights

This folder consists of a collection of .m scripts that queries the database for insights.

The insights chosen here would be to provide a historical plot of the data across the years, given the information
supplied by the excel sheets for the project. 

Add NULL columns in the excel sheets are automatically changed to 0 via pre-processing of the data. 


### Execution
Run the script under **octave/Qeury.m**. This script will connect to the database, extract useful information and 
plot a graph of the histroical data against years, with relevant contextual information for the X, Y axis and title. 

In order to select plots, we can call the API under function Analyse.m. The following parameters are specified:
conn 				: Connection instance to the database after a call to pg_conn
country_code 		: Country code such as "ABW"
indicator_code 		: Indicator code 
start_yr 			: Starting year of the data reading 

### Sample images
Please refer to **/pics** folder for sample images
