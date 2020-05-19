#Definition of the schema fo the DB
#This is a DB for managing imformation about movies

#Create the DB
DROP DATABASE IF EXISTS movies_db;
CREATE DATABASE IF NOT EXISTS movies_db;

#Select the database to work with
USE movies_db;

#Create the kernel tables:director, actor and genres
CREATE TABLE IF NOT EXISTS directors(
id_director int NOT NULL AUTO_INCREMENT,
d_fname VARCHAR(35) NOT NULL,
d_sname1 VARCHAR(35) NOT NULL,
d_sname2 VARCHAR(35),
d_nationality VARCHAR(35),
PRIMARY KEY(id_director)
)ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS actors(
id_actor int NOT NULL AUTO_INCREMENT,
a_fname VARCHAR(35) NOT NULL,
a_sname1 VARCHAR(35) NOT NULL,
a_sname2 VARCHAR(35),
c_nationality VARCHAR(35) NOT NULL,
PRIMARY KEY(id_actor)
)ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS genres(
id_genre INT NOT NULL AUTO_INCREMENT,
g_name VARCHAR(35) NOT NULL,
p_descrip VARCHAR(250),
PRIMARY KEY(id_genre)
) ENGINE = InnoDB;

#CREATE the dependent tables: movies, movies-genres, movies-actors
CREATE TABLE IF NOT EXISTS movies(
id_movie INT NOT NULL AUTO_INCREMENT,
m_name VARCHAR(35) NOT NULL,
m_year int NOT NULL,
m_sinopsis VARCHAR(250),
id_director int,
PRIMARY KEY(id_movie),
CONSTRAINT fkdiector FOREIGN KEY(id_director)
	REFERENCES directors(id_director)
    ON DELETE CASCADE
    ON UPDATE CASCADE
)ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS movie_actors(
id_movie INT NOT NULL,
id_actor INT NOT NULL,
salario INT NOT NULL,
PRIMARY KEY(id_movie, id_actor),
CONSTRAINT fkmovie_act FOREIGN KEY(id_movie)
	REFERENCES movies(id_movie)
	ON DELETE CASCADE
	ON UPDATE CASCADE,
CONSTRAINT fkactor FOREIGN KEY(id_actor)
	REFERENCES actors(id_actor)
	ON DELETE CASCADE
    ON UPDATE CASCADE
)ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS movie_genres(
id_movie INT NOT NULL,
id_genre INT NOT NULL,
PRIMARY KEY(id_movie, id_genre),
CONSTRAINT fkmovie_gen FOREIGN KEY(id_movie)
	REFERENCES movies(id_movie)
	ON DELETE CASCADE
	ON UPDATE CASCADE,
CONSTRAINT fkgenre FOREIGN KEY(id_genre)
	REFERENCES genres(id_genre)
	ON DELETE CASCADE
    ON UPDATE CASCADE
)ENGINE = InnoDB;