#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 13:00:32 2023
@author: Najia Ahmadi
"""

from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

# Database connection parameters

db_host = "your database host"
db_port = "your database port"
db_name = "your database name"
db_user = "your admin user name"
db_password = "your admin password"

# list og tables and columns to be updated
updates = [
    {
     # tbale: person
        "table_name": "cds_cdm.person",
        "column_name": "month_of_birth",
        "new_value": 'none'  # Replace with the desired new value or 'None' for null
    },
    {
        "table_name": "cds_cdm.person",
        "column_name": "day_of_birth",
        "new_value": 'none'  # Replace with the desired new value or 'None' for null
    },
    {
        "table_name": "cds_cdm.person",
        "column_name": "person_source_value",
        "new_value": 'none'  # Replace with the desired new value or 'None' for null
    },
    
    # tbale: visit_occurrence
    {
        "table_name": "cds_cdm.visit_occurrence",
        "column_name": "visit_source_value",
        "new_value": 'none'
    },
    
    # tbale: drug_exposure
    {
        "table_name": "cds_cdm.drug_exposure",
        "column_name": "provider_id",
        "new_value": 'none'
        },
    # tbale: observation
    {
        "table_name": "cds_cdm.observation",
        "column_name": "observation_date",
        "new_value": 'none'
        }
    # Add more table and column updates as needed
]

# Create the database connection
db_url = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

try:
    engine = create_engine(db_url)
    connection = engine.connect()

    for update in updates:
        table_name = update["table_name"]
        column_name = update["column_name"]
        new_value = update["new_value"]

        # SQL script to update the column in the specified table
        sql_script = f"""
            UPDATE {table_name}
            SET {column_name} = {new_value};
        """
            # if the column should entirely be deleted instead of update with new value
            # the following two commonds can be used instead of UPDATE and SET commonds.
            # ALTER TABLE {table_name} 
            # DROP COLUMN {column_name};
            
        # Execute the SQL script
        connection.execute(sql_script)

        print(f"Column '{column_name}' in table '{table_name}' updated successfully!")


except SQLAlchemyError as error:
    print("Error while connecting to PostgreSQL:", error)
    
finally:
    if connection:
        connection.close()

