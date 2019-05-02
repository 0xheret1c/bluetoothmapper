/*
    Datenbank für Rohdaten
*/
CREATE DATABASE wminbound;
/*
    Tabellen    
*/
CREATE TABLE 'sessions' (
    sessionID INT UNSIGNED NOT NULL AUTO_INCREMENT,
    locID INT NOT NULL,
    start DATETIME(),
    end DATETIME(),
    PRIMARY KEY(sessionID)

)

CREATE TABLE 'data' (
    dataID INT UNSIGNED NOT NULL AUTO_INCREMENT,
    sigStrength FLOAT NOT NULL,
    sourceMAC VARCHAR(17),
    apID INT NOT NULL,
    time DATETIME(),
    PRIMARY KEY(dataID)
)

CREATE TABLE 'location' (
   locationID INT UNSIGNED NOT NULL AUTO_INCREMENT,
   sigStrength FLOAT NOT NULL,
   name VARCHAR(32) NOT NULL,
   PRIMARY KEY(locationID)
)

CREATE TABLE 'ap' (
   apID INT UNSIGNED NOT NULL AUTO_INCREMENT,
   locationID INT NOT NULL, 
   PRIMARY KEY(apID)
)

CREATE TABLE 'distance' (
   distanceID INT UNSIGNED NOT NULL AUTO_INCREMENT,
   fromApID INT NOT NULL,
   toApID INT NOT NULL,
   distance FLOAT NOT NULL,
   PRIMARY KEY(distanceID)
)