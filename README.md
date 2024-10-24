# Pipeline 38

This is a follow- up to Pipeline 37. The aim is to create a serialisation format of a data pipeline. There is one key change from Pipeline 37: <br />

Data will be manipulated using PostgreSQL commands rather than in a Pandas Dataframe format. <br />

**Technologies used:**
PostgreSQL 17.0, <br />
Python 3.13.0, <br />
Pandas, <br />
SQLAlchemy 2.0.36, <br />
psycopg 2 2.9.10, <br />


pgAdmin 4 <br />
PyCharm <br />

**Objectives:**
 1. Create tools for automated data process including cleaning, transformation, and processing.
 2. The application can generate a working serialisation format of a pipeline.
 3. Improve performance for large datasets with use of PostgreSQL queries.

**Goal:**
Improve my workflow for large datasets to create useful analysis for Tableau.

**Architecture**
The basic structure of this project has a few simple elements. There is a connection to a PostgreSQL database that uses LocalSettings (this file is not on Github). The user can enter commands, the args are passed to the relevant function in SQLFunctions, and the query is constructed there and passed back to 'Connection' to be executed. These commands will include both changes to the data being examined and the creation of new tables. Every time a command is successfully executed, a row is also added to a DF called <ins>Query DF</ins> that is recording the completed instructions. 

This DF is a record of the data processing. It can then be saved, loaded, or exported so that the user can automate the steps for another file. 

There is a second dataframe (<ins>Derived DF</ins>) that stores the results of user commands, IE derived values that are not added to the original dataset. In this way the user is able to create a table of derived data and perform different operations on it directly.
