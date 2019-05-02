/*
    Datenbank für Rohdaten
*/
CREATE DATABASE wminbound;
/*
    Tabellen    
*/
CREATE TABLE 'sessions' (
    sessionID INT UNSIGNED NOT NULL AUTO_INCREMENT,
    start DATETIME(),
    end DATETIME(),
    setupID INT NOT NULL,
    PRIMARY KEY(sessionID)

)

CREATE TABLE 'data' (
    dataID INT UNSIGNED NOT NULL AUTO_INCREMENT,
    sigStrength FLOAT NOT NULL,
    sourceMAC VARCHAR(17),
    apID INT NOT NULL,
    time DATETIME(),
    sessionID,
    PRIMARY KEY(dataID)
)

CREATE TABLE 'location' (
   locationID INT UNSIGNED NOT NULL AUTO_INCREMENT,
   name VARCHAR(32) NOT NULL,
   PRIMARY KEY(locationID)
)

CREATE TABLE 'ap' (
   apID INT UNSIGNED NOT NULL AUTO_INCREMENT,
   apName VARCHAR(32) NOT NULL,
   apPlatform VARCHAR(255),
   apNetworkdev VARCHAR(255),
   apComment VARCHAR(255),
   PRIMARY KEY(apID)
)

CREATE TABLE 'ap_to_setup' (
    ap_to_setupID INT UNSIGNED NOT NULL AUTO_INCREMENT,
    apID INT UNSIGNED NOT NULL,
    setupID IN UNSIGNED NOT NULL,
    PRIMARY KEY(ap_to_setupID)
)

CREATE TABLE 'setup' (
    setupID INT UNSIGNED NOT NULL AUTO_INCREMENT,
    locationID INT UNSIGNED NOT NULL,
    PRIMARY KEY(setupID)
)

CREATE TABLE 'distance' (
   distanceID INT UNSIGNED NOT NULL AUTO_INCREMENT,
   fromApID INT NOT NULL,
   toApID INT NOT NULL,
   distance FLOAT NOT NULL,
   sessionID INT NOT NULL,
   PRIMARY KEY(distanceID)
)
