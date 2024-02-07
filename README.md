# OMOP CDM Content deletion
This script is used to delete the content of certain columns in certan tables of OMOP CDM. 

## Required packages
- sqlalchemy
- psycopg2

### Fill in the database information in the scrip: 

- db_host = "Your database host"
- db_port = "Your port"
- db_name = "Your database name"
- db_user = "You admin name"
- db_password = "Your admin password"

### Run the scrip in Terminal using the following commond: 

- python omop-deletion-scrip.py

