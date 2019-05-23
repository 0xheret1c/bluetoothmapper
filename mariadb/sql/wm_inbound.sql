/*
    Datenbank für Rohdaten
*/
CREATE DATABASE IF NOT EXISTS wminbound;
USE wminbound;
/*
    Tabellen    
*/

CREATE TABLE IF NOT EXISTS location (
   locationID INT UNSIGNED NOT NULL AUTO_INCREMENT,
   name VARCHAR(32) NOT NULL,
   PRIMARY KEY(locationID)
);

CREATE TABLE IF NOT EXISTS ap (
   apID INT UNSIGNED NOT NULL AUTO_INCREMENT,
   apName                   VARCHAR(32) NOT NULL,
   apPlatform               VARCHAR(255),
   
   apNetworkdevIntern       VARCHAR(255),
   apNetworkdevInternMAC    VARCHAR(17),
   
   apNetworkdevExtern       VARCHAR(255),
   apNetworkdevExternMAC    VARCHAR(17),
   
   apComment                VARCHAR(255),
   PRIMARY KEY(apID)
);

CREATE TABLE IF NOT EXISTS setup (
    setupID     INT UNSIGNED NOT NULL AUTO_INCREMENT,
    locationID  INT UNSIGNED NOT NULL,
    PRIMARY KEY(setupID),
    FOREIGN KEY(locationID) REFERENCES location(locationID)
);

CREATE TABLE ap_to_setup (
    apID    INT UNSIGNED NOT NULL,
    setupID INT UNSIGNED NOT NULL,
    PRIMARY KEY(apID,setupID),
    FOREIGN KEY(apID) REFERENCES ap(apID),
    FOREIGN KEY(setupID) REFERENCES setup(setupID)
);

CREATE TABLE IF NOT EXISTS sessions (
    sessionID   INT UNSIGNED NOT NULL AUTO_INCREMENT,
    setupID     INT UNSIGNED NOT NULL,
    start       DATETIME,
    end         DATETIME,
    PRIMARY KEY(sessionID),
    FOREIGN KEY(setupID) REFERENCES setup(setupID)
);

CREATE TABLE IF NOT EXISTS data (
    dataID      INT UNSIGNED    NOT NULL AUTO_INCREMENT,
    apID        INT UNSIGNED    NOT NULL,
    sessionID   INT UNSIGNED    NOT NULL,
    sigStrength FLOAT           NOT NULL,
    sourceMAC   VARCHAR(17),
    time        DATETIME,
    PRIMARY KEY(dataID),
    FOREIGN KEY(sessionID) REFERENCES sessions(sessionID),
    FOREIGN KEY(apID) REFERENCES ap(apID)
);

CREATE TABLE IF NOT EXISTS distance (
   distanceID   INT UNSIGNED NOT NULL AUTO_INCREMENT,
   fromApID     INT UNSIGNED NOT NULL,
   toApID       INT UNSIGNED NOT NULL,
   sessionID    INT UNSIGNED NOT NULL,
   distance     FLOAT NOT NULL,
   PRIMARY KEY(distanceID),
   FOREIGN KEY(fromApID) REFERENCES ap(apID),
   FOREIGN KEY(toApID) REFERENCES ap(apID),
   FOREIGN KEY(sessionID) REFERENCES sessions(sessionID)
);
