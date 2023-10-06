# idf-test
Database dump is loaded into MySQL docker container, Adminer is used for DB UI.
File [test-queries.sql](test-queries.sql) contains all 6 queries from the 2 task.

Report for task 3 was created using Plotly Dashboard library.
Report opens localy on port 8050 and requires connection to DB. You can use either database from docker-compose or your own compatible database. In second case change configuration settings in [requirements.txt](requirements.txt).
