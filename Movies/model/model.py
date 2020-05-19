from mysql import connector
class Model:
	"""
	*****************************************
	* A data model with MySQL for a movies DB*
	*****************************************
	"""
	def __init__(self, config_db_file='config.txt'):
		self.config_db_file = config_db_file
		self.config_db = self.read_config_db()
		self.connect_to_db()

	def read_config_db(self):
		d = {}
		with open(self.config_db_file) as f_r:
			for line in f_r:
				(key, val) = line.strip().split(':')
				d[key] = val
		return d 

	def connect_to_db(self):
		self.cnx = connector.connect(**self.config_db)
		self.cursor = self.cnx.cursor()

	def close_db(self):
		self.cnx.close()

	"""
	********************
	* director methods *
	********************
	"""

	def create_director(self, name, sname1, sname2, nationality):
		try:
			sql = 'INSERT INTO directors (`d_fname`, `d_sname1`, `d_sname2`, `d_nationality`) VALUES (%s, %s, %s, %s)'
			vals = (name, sname1, sname2, nationality)
			self.cursor.execute(sql, vals)
			self.cnx.commit()
			return True
		except connector.Error as err:
			self.cnx.rollback()
			return err

	def read_a_director(self, id_director):
	 	try:
	 		sql = 'SELECT * FROM directors WHERE id_director = %s'
	 		vals = (id_director,)
	 		self.cursor.execute(sql, vals)
	 		record = self.cursor.fetchone()
	 		return record
	 	except connector.Error as err:
	 		return err

	def read_all_directors(self):
	 	try:
	 		sql = 'SELECT * FROM directors'
	 		self.cursor.execute(sql)
	 		records = self.cursor.fetchall()
	 		return records
	 	except connector.Error as err:
	 		return err
	 	    	
	def read_directors_nationality(self, nationality):
		try:
			sql = ('SELECT * FROM directors WHERE d_nationality = %s')
			vals = (nationality,)
			self.cursor.execute(sql, vals)
			records = self.cursor.fetchall()
			return records
		except connector.Error as err:
			return err       

	def update_director(self, fields, vals):
		try:
			sql = 'UPDATE directors SET '+','.join(fields)+' WHERE id_director = %s'
			self.cursor.execute(sql, vals)
			self.cnx.commit()
			return True 
		except connector.Error as err:
			self.cnx.rollback()
			return err

	def delete_director(self, id_director):
		try:
			sql = 'DELETE FROM directors WHERE id_director = %s'
			vals = (id_director,)
			self.cursor.execute(sql, vals)
			self.cnx.commit()
			count = self.cursor.rowcount
			return count
		except connector.Error as err:
			self.cnx.rollback()
			return err

	"""
	******************
	* Actors methods *
	******************
	"""

	def create_actor(self, name, sname1, sname2, nationality):
		try:
			sql = 'INSERT INTO actors (`a_fname`, `a_sname1`, `a_sname2`, `c_nationality`) VALUES (%s, %s, %s, %s)'
			vals = (name, sname1, sname2, nationality)
			self.cursor.execute(sql, vals)
			self.cnx.commit()
			return True
		except connector.Error as err:
			self.cnx.rollback()
			return err

	def read_a_actor(self, id_actor):
	 	try:
	 		sql = 'SELECT * FROM actors WHERE id_actor = %s'
	 		vals = (id_actor,)
	 		self.cursor.execute(sql, vals)
	 		record = self.cursor.fetchone()
	 		return record
	 	except connector.Error as err:
	 		return err

	def read_all_actors(self):
	 	try:
	 		sql = 'SELECT * FROM actors'
	 		self.cursor.execute(sql)
	 		records = self.cursor.fetchall()
	 		return records
	 	except connector.Error as err:
	 		return err
	 	    	
	def read_actors_nationality(self, nationality):
		try:
			sql = ('SELECT * FROM actors WHERE c_nationality = %s')
			vals = (nationality,)
			self.cursor.execute(sql, vals)
			records = self.cursor.fetchall()
			return records
		except connector.Error as err:
			return err       

	def update_actor(self, fields, vals):
		try:
			sql = 'UPDATE actors SET '+','.join(fields)+' WHERE id_actor = %s'
			self.cursor.execute(sql, vals)
			self.cnx.commit()
			return True 
		except connector.Error as err:
			self.cnx.rollback()
			return err

	def delete_actor(self, id_actor):
		try:
			sql = 'DELETE FROM actors WHERE id_actor = %s'
			vals = (id_actor,)
			self.cursor.execute(sql, vals)
			self.cnx.commit()
			count = self.cursor.rowcount
			return count
		except connector.Error as err:
			self.cnx.rollback()
			return err

	"""
	******************
	* Genres Genre *
	******************
	"""

	def create_genre(self, name, descrip):
		try:
			sql = 'INSERT INTO genres (`g_name`, `p_descrip`) VALUES (%s, %s)'
			vals = (name, descrip)
			self.cursor.execute(sql, vals)
			self.cnx.commit()
			return True
		except connector.Error as err:
			self.cnx.rollback()
			return err

	def read_a_genre(self, id_genre):
	 	try:
	 		sql = 'SELECT * FROM genres WHERE id_genre = %s'
	 		vals = (id_genre,)
	 		self.cursor.execute(sql, vals)
	 		record = self.cursor.fetchone()
	 		return record
	 	except connector.Error as err:
	 		return err

	def read_all_genres(self):
	 	try:
	 		sql = 'SELECT * FROM genres'
	 		self.cursor.execute(sql)
	 		records = self.cursor.fetchall()
	 		return records
	 	except connector.Error as err:
	 		return err
	 	    	
	def read_genres_name(self, name):
		try:
			sql = ('SELECT * FROM genres WHERE g_name = %s')
			vals = (name,)
			self.cursor.execute(sql, vals)
			records = self.cursor.fetchall()
			return records
		except connector.Error as err:
			return err       

	def update_genre(self, fields, vals):
		try:
			sql = 'UPDATE genres SET '+','.join(fields)+' WHERE id_genre = %s'
			self.cursor.execute(sql, vals)
			self.cnx.commit()
			return True 
		except connector.Error as err:
			self.cnx.rollback()
			return err

	def delete_genre(self, id_genre):
		try:
			sql = 'DELETE FROM genres WHERE id_genre = %s'
			vals = (id_genre,)
			self.cursor.execute(sql, vals)
			self.cnx.commit()
			count = self.cursor.rowcount
			return count
		except connector.Error as err:
			self.cnx.rollback()
			return err

	"""
	********************
	* movies methodf    *
	********************
	"""
	def create_movie(self, name, year, sinopsis, director):
		try:
			sql = 'INSERT INTO movies (`m_name`, `m_year`, `m_sinopsis`, `id_director`) VALUES (%s, %s, %s, %s)'
			vals = (name, year, sinopsis, director)
			self.cursor.execute(sql, vals)
			self.cnx.commit()
			return True
		except connector.Error as err:
			self.cnx.rollback()
			return err

	def read_a_movie(self, id_movie):
	 	try:
	 		sql = 'SELECT * FROM movies WHERE id_movie = %s'
	 		vals = (id_movie,)
	 		self.cursor.execute(sql, vals)
	 		record = self.cursor.fetchone()
	 		return record
	 	except connector.Error as err:
	 		return err

	def read_all_movies(self):
	 	try:
	 		sql = 'SELECT * FROM movies'
	 		self.cursor.execute(sql)
	 		records = self.cursor.fetchall()
	 		return records
	 	except connector.Error as err:
	 		return err
	 	    	
	def read_movies_name(self, year):
		try:
			sql = ('SELECT * FROM movies WHERE m_year = %s')
			vals = (year,)
			self.cursor.execute(sql, vals)
			records = self.cursor.fetchall()
			return records
		except connector.Error as err:
			return err       

	def update_movie(self, fields, vals):
		try:
			sql = 'UPDATE movies SET '+','.join(fields)+' WHERE id_movie = %s'
			self.cursor.execute(sql, vals)
			self.cnx.commit()
			return True 
		except connector.Error as err:
			self.cnx.rollback()
			return err

	def delete_movie(self, id_movie):
		try:
			sql = 'DELETE FROM movies WHERE id_movie = %s'
			vals = (id_movie,)
			self.cursor.execute(sql, vals)
			self.cnx.commit()
			count = self.cursor.rowcount
			return count
		except connector.Error as err:
			self.cnx.rollback()
			return err

	def create_movie_actors(self, id_movie, id_actor, salario):
		try:
			sql = 'INSERT INTO movie_actors (`id_movie`, `id_actor`, `salario`) VALUES (%s, %s, %s)'
			vals = (id_movie, id_actor, salario)
			self.cursor.execute(sql, vals)
			self.cnx.commit()
			return True
		except connector.Error as err:
			self.cnx.rollback()
			return err

	def create_movie_genre(self, id_movie, id_genre):
		try:
			sql = 'INSERT INTO movie_genres (`id_movie`, `id_genre`) VALUES (%s, %s)'
			vals = (id_movie, id_genre)
			self.cursor.execute(sql, vals)
			self.cnx.commit()
			return True
		except connector.Error as err:
			self.cnx.rollback()
			return err

	