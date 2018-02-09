CREATE DATABASE forum CHARACTER SET 'utf8';
SHOW WARNINGS;
USE forum

CREATE TABLE IF NOT EXISTS forum (
	id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
	sujet VARCHAR(100) NOT NULL,
	auteur VARCHAR(100) NOT NULL,
	date_sujet DATETIME,
	PRIMARY KEY (id)
) ENGINE=INNODB;

INSERT INTO forum (sujet, auteur, date_sujet)
VALUES ("Farcry 5", "Enzo", "2018-02-06");

INSERT INTO forum (sujet, auteur, date_sujet)
VALUES ("La neutralite du net", "Florian", "2018-07-30");

INSERT INTO forum (sujet, auteur, date_sujet)
VALUES ("Les Nouveaux Procos Intel", "Gregory", "2020-06-25");

INSERT INTO forum (sujet, auteur, date_sujet)
VALUES ("Lorem Ipsium: Utile?", "Enzo", "2018-09-17");

INSERT INTO forum (sujet, auteur, date_sujet)
VALUES ("My SQL Indispensable Pour les sites", "Jonahtan", "2019-09-09");

INSERT INTO forum (sujet, auteur, date_sujet)
VALUES ("Les jobs de demain", "Darkzorg28", "2018-02-27");

INSERT INTO forum (sujet, auteur, date_sujet)
VALUES ("Les imprimantes 3D", "Romain", "2018-09-28");

INSERT INTO forum (sujet, auteur, date_sujet)
VALUES ("Le Samsung A8", "Jerome", "2018-06-30");

INSERT INTO forum (sujet, auteur, date_sujet)
VALUES ("Le retro-gaming", "Julien", "2050-08-13");

INSERT INTO forum (sujet, auteur, date_sujet)
VALUES ("L'Iphone X", "Jean", "7856-08-23");

INSERT INTO forum (sujet, auteur, date_sujet)
VALUES ("Le Internet", "Julien", "2018-08-21");

INSERT INTO forum (sujet, auteur, date_sujet)
VALUES ("Le cassoulet", "Jonahtan", "2019-08-30");

INSERT INTO forum (sujet, auteur, date_sujet)
VALUES ("La batterie externe", "Enzo", "2018-09-17");

SELECT sujet, auteur, date_sujet  FROM forum WHERE date_sujet BETWEEN "2018-01-01" AND "2018-12-31";

SELECT DISTINCT auteur FROM forum ORDER BY auteu

SELECT COUNT(sujet) AS Nombre_de_sujets_par_les_auteurs FROM forum WHERE auteur LIKE "j%";

SELECT sujet FROM forum WHERE sujet LIKE "%Les%";

SELECT auteur, COUNT(sujet) FROM forum GROUP BY auteur;