CREATE SCHEMA if not exists project_two;

CREATE TABLE if not exists project_two.Global_Exchange_Universities (
    ID INT PRIMARY KEY,
    Name VARCHAR(255),
    Country VARCHAR(255),
    City VARCHAR(255),
    Overall_QS_Rank INT,
    Compsci_QS_Rank INT,
    Mathematics_QS_Rank INT,
    Website VARCHAR(255)
);

