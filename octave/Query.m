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

Analyse(conn, "BLZ", "EN.BIR.THRD.NO", 1960);
pq_close(conn);