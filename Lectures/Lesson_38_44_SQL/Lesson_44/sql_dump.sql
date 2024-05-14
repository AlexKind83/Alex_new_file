BEGIN TRANSACTION;CREATE TABLE cars(
        car_id INTEGER PRIMARY KEY AUTOINCREMENT,
        model TEXT,
        price INTEGER
    );INSERT INTO "cars" VALUES(1,'Renault',22300);INSERT INTO "cars" VALUES(2,'Volvo',29300);INSERT INTO "cars" VALUES(3,'Mercedes',57300);INSERT INTO "cars" VALUES(5,'Audi',52300);INSERT INTO "cars" VALUES(7,'Chevrolet',46300);INSERT INTO "cars" VALUES(8,'Daewoo',46300);INSERT INTO "cars" VALUES(9,'Citroen',29300);INSERT INTO "cars" VALUES(10,'Honda',33300);INSERT INTO "cars" VALUES(17,'Chevrolet',46300);INSERT INTO "cars" VALUES(18,'Daewoo',46300);INSERT INTO "cars" VALUES(19,'Citroen',29300);INSERT INTO "cars" VALUES(20,'Honda',33300);INSERT INTO "cars" VALUES(21,'Renault',22200);INSERT INTO "cars" VALUES(23,'Запорожец',1000);CREATE TABLE cost(
        name TEXT, tr_in INTEGER, buy INTEGER
    );INSERT INTO "cost" VALUES('Илья',23,2);CREATE TABLE users(
        name TEXT, ava BLOB, score INTEGER
    );DELETE FROM "sqlite_sequence";INSERT INTO "sqlite_sequence" VALUES('cars',23);COMMIT;