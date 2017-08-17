pkg load database;

clear;
clc;

db_name   = "environ";
db_user   = "ilumone";
db_pass   = "ilumone";

conn      = pq_connect(setdbopts( "host", "localhost", 
                                  "dbname", db_name, 
                                  "user", db_user, 
                                  "password", db_pass));

Analyse(conn, "ABW", "AG.LND.EL5M.ZS", 1960);
pq_close(conn);