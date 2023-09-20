CREATE DATABASE IF NOT EXISTS Test;
USE Test;

CREATE TABLE IF NOT EXISTS
users(
    id          INTEGER UNIQUE NOT NULL,
    login        TEXT NOT NULL,
    money_amount        INTEGER NOT NULL,
    card_number       TEXT NOT NULL,
    status       INTEGER
);

CREATE TABLE IF NOT EXISTS
passwords(
    id          INTEGER UNIQUE NOT NULL,
    password            TEXT NOT NULL
);

INSERT INTO users VALUES
        (1,     'admin',        110000,        '4024007141020197',      1),
        (2,     'Innil',        414300,          '4716145656322211',      0),
        (3,     'Rolen',        56800,          '4556177851649331',      0),
        (4,     'Tass',         183800,     '4024007145815501',      1),
        (5,     'Helly',        322010,   '5154013136862683',      1)
;
INSERT INTO passwords VALUES
    (1,   'qwerty'),
    (2,  'qwerty123'),
    (3, 'qwerty1234'),
    (4,   'qwerty12345'),
    (5, 'qwerty123456')
;