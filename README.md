# project_peanutsandcrackerjack
A series of projects exploring the Chadwick Baseball Databank

This repo contains code that analyzes the Chadwick Baseball Databank which can be found here:
https://github.com/chadwickbureau/baseballdatabank 

## Folder:  Top_Hitters_OPS
This folder contains the R markdown code for the analysis that supports my blog published in Towards Data Science.
[https://c-k.com/stats-for-baseball-fans-the-single-metric-for-offense-is-ops/ ](https://towardsdatascience.com/stats-for-baseball-fans-the-single-metric-for-offense-is-ops-fc568af5e87b)
To perform this analysis, I set up a Postgres database on my local machine that contains all of the Chadwick Baseball Databank files as tables.  I also created a view of the players hitting stats - details can be found in the Data_ETL folder in this repo.
https://github.com/agentdanger/project_peanutsandcrackerjack/tree/master/data_ETL

## Folder:  Data_ETL
This folder contains the python script that automates the transfer and load into my local Postgres database.
