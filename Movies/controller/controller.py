from model.model import Model 
from view.view import View 


class Controller:
	"""
	********************************
	* A controller for a movies DB *
	********************************
	"""
	def __init__(self):
		self.model = Model()
		self.view = View()

	def start(self):
		self.view.start()
		self.main_menu()

	"""
	***********************
	* General controllers *
	***********************
	"""
	def main_menu(self):
		o = '0'
		while o != '5':
			self.view.main_menu()
			self.view.option('5')
			o = input()
			if o == '1':
				self.directors_menu()
			elif o == '2':
				self.actors_menu()
			elif o == '3':
				self.genres_menu()
			elif o == '4':
				self.movies_menu()
			elif o == '5':
				self.view.end()
			else:
				self.view.not_valid_option()
		return

	def update_lists(self, fs, vs):
		fields = []
		vals = []
		for f,v in zip(fs,vs):
			if v!= '':
				fields.append(f+' = %s')
				vals.append(v)
		return fields,vals

	"""
	*****************************
	* Controllers for directors *
	*****************************
	"""
	def directors_menu(self):
		o = '0'
		while o != '7':
			self.view.directors_menu()
			self.view.option('7')
			o = input()
			if o == '1':
				self.create_director()
			elif o == '2':
				self.read_a_director()
			elif o == '3':
				self.read_all_directors()
			elif o == '4':
				self.read_directors_nationality()
			elif o == '5':
				self.update_director()
			elif o == '6':
				self.delete_director()
			elif o == '7':
				return
			else:
				self.view.not_valid_option()
		return

	def ask_director(self):
		self.view.ask('Nombre: ')
		name = input()
		self.view.ask('A.Paterno: ')
		sname1 = input()
		self.view.ask('A.Materno: ')
		sname2 = input()
		self.view.ask('Nacionalidad: ')
		nationality = input()
		return[name, sname1, sname2, nationality]

	def create_director(self):
		name, sname1, sname2, nationality = self.ask_director()
		out = self.model.create_director(name, sname1, sname2, nationality)
		if out == True:
			self.view.ok(name+' '+sname1, 'agrego')
		else:
			self.view.error('No se pudo agregar Director. REVISA')
		return

	def read_a_director(self):
		self.view.ask('ID_Director: ')
		id_director = input()
		director = self.model.read_a_director(id_director)
		if type(director) == tuple:
			self.view.show_director_header('  Datos del Director '+id_director+' ')
			self.view.show_a_director(director)
			self.view.show_director_midder()
			self.view.show_director_footer()
		else:
			if director == None:
				self.view.error('EL DIRECTOR NO EXISTE')
			else:
				self.view.error('PROBLEMA AL LEER DIRECTOR. REVISA.')
		return

	def read_all_directors(self):
		directors = self.model.read_all_directors()
		if type(directors) == list:
			self.view.show_director_header('  Todos los Directores  ')
			for director in directors:
				self.view.show_a_director(director)
			self.view.show_director_midder()
			self.view.show_director_footer()
		else:
			self.view.error('PROBLEMA AL LEER LOS DIRECTORES. REVISA.')
		return

	def read_directors_nationality(self):
		self.view.ask('Nacionalidad:')
		nationality = input()
		directors = self.model.read_directors_nationality(nationality)
		if type(directors) == list:
			self.view.show_director_header(' Directores para la Nacionalidad de '+nationality+' ')
			for director in directors:
				self.view.show_a_director(director)
			self.view.show_director_midder()
			self.view.show_director_footer()
		else:
			self.view.error('PROBLEMA al LEER LOS DIRECTORES. REVISA.')
		return

	def update_director(self):
		self.view.ask('ID del Director a modificar: ')
		id_director = input()
		director = self.model.read_a_director(id_director)
		if type(director) == tuple:
			self.view.show_director_header('Datos del Director'+id_director+' ')
			self.view.show_a_director(director)
			self.view.show_director_midder()
			self.view.show_director_footer()
		else:
			if director == None:
				self.view.error('El Director no existe')
			else:
				self.view.error('Problemas al leer el Director, REVISA')
			return
		self.view.msg('Ingresa los valores a modificar:(vacio para dejarlo igual)')
		whole_vals = self.ask_director()
		fields, vals = self.update_lists(['d_fname','d_sname1','d_sname2','d_nationality'], whole_vals)
		vals.append(id_director)
		vals = tuple(vals)
		out = self.model.update_director(fields, vals)
		if out == True:
			self.view.ok(id_director, 'actualizo')
		else:
			self.view.error('No se pudo actualizar el DIRECTOR. REVISA')
		return

	def delete_director(self):
		self.view.ask('ID_Director a borrar: ')
		id_director = input()
		count = self.model.delete_director(id_director)
		if count !=0:
			self.view.ok(id_director, 'borro')
		else:
			if count == 0:
				self.view.error('El Director no existe')
			else:
				self.view.error('Problemas al leer el Director. REVISA')
		return

	"""
	*****************************
	* Controllers for actors *
	*****************************
	"""
	def actors_menu(self):
		o = '0'
		while o != '7':
			self.view.actors_menu()
			self.view.option('7')
			o = input()
			if o == '1':
				self.create_actor()
			elif o == '2':
				self.read_a_actor()
			elif o == '3':
				self.read_all_actors()
			elif o == '4':
				self.read_actors_nationality()
			elif o == '5':
				self.update_actor()
			elif o == '6':
				self.delete_actor()
			elif o == '7':
				return
			else:
				self.view.not_valid_option()
		return

	def ask_actor(self):
		self.view.ask('Nombre: ')
		name = input()
		self.view.ask('A.Paterno: ')
		sname1 = input()
		self.view.ask('A.Materno: ')
		sname2 = input()
		self.view.ask('Nacionalidad: ')
		nationality = input()
		return[name, sname1, sname2, nationality]

	def create_actor(self):
		name, sname1, sname2, nationality = self.ask_actor()
		out = self.model.create_actor(name, sname1, sname2, nationality)
		if out == True:
			self.view.ok(name+' '+sname1, 'agrego')
		else:
			self.view.error('No se pudo agregar Actor. REVISA')
		return

	def read_a_actor(self):
		self.view.ask('ID_Actor: ')
		id_actor = input()
		actor = self.model.read_a_actor(id_actor)
		if type(actor) == tuple:
			self.view.show_actor_header('  Datos del Director '+id_actor+' ')
			self.view.show_a_actor(actor)
			self.view.show_actor_midder()
			self.view.show_actor_footer()
		else:
			if actor == None:
				self.view.error('EL ACTOR NO EXISTE')
			else:
				self.view.error('PROBLEMA AL LEER ACTOR. REVISA.')
		return

	def read_all_actors(self):
		actors = self.model.read_all_actors()
		if type(actors) == list:
			self.view.show_actor_header('  Todos los Actores  ')
			for actor in actors:
				self.view.show_a_actor(actor)
			self.view.show_actor_midder()
			self.view.show_actor_footer()
		else:
			self.view.error('PROBLEMA AL LEER LOS ACTORES. REVISA.')
		return

	def read_actors_nationality(self):
		self.view.ask('Nacionalidad:')
		nationality = input()
		actors = self.model.read_actors_nationality(nationality)
		if type(actors) == list:
			self.view.show_actor_header(' Actores para la Nacionalidad de '+nationality+' ')
			for actor in actors:
				self.view.show_a_actor(actor)
			self.view.show_actor_midder()
			self.view.show_actor_footer()
		else:
			self.view.error('PROBLEMA al LEER LOS ACTORES. REVISA.')
		return

	def update_actor(self):
		self.view.ask('ID del Actor a modificar: ')
		id_actor = input()
		actor = self.model.read_a_actor(id_actor)
		if type(actor) == tuple:
			self.view.show_actor_header('Datos del Actor'+id_actor+' ')
			self.view.show_a_actor(actor)
			self.view.show_actor_midder()
			self.view.show_actor_footer()
		else:
			if actor == None:
				self.view.error('El Actor no existe')
			else:
				self.view.error('Problemas al leer el Actor, REVISA')
			return
		self.view.msg('Ingresa los valores a modificar:(vacio para dejarlo igual)')
		whole_vals = self.ask_actor()
		fields, vals = self.update_lists(['a_fname','a_sname1','a_sname2','c_nationality'], whole_vals)
		vals.append(id_actor)
		vals = tuple(vals)
		out = self.model.update_actor(fields, vals)
		if out == True:
			self.view.ok(id_actor, 'actualizo')
		else:
			self.view.error('No se pudo actualizar el Actor. REVISA')
		return

	def delete_actor(self):
		self.view.ask('ID_Actor a borrar: ')
		id_actor = input()
		count = self.model.delete_actor(id_actor)
		if count !=0:
			self.view.ok(id_actor, 'borro')
		else:
			if count == 0:
				self.view.error('El Actor no existe')
			else:
				self.view.error('Problemas al leer el Actor. REVISA')
		return

	"""
	*****************************
	* Controllers for genres *
	*****************************
	"""
	def genres_menu(self):
		o = '0'
		while o != '7':
			self.view.genres_menu()
			self.view.option('7')
			o = input()
			if o == '1':
				self.create_genre()
			elif o == '2':
				self.read_a_genre()
			elif o == '3':
				self.read_all_genres()
			elif o == '4':
				self.read_genres_name()
			elif o == '5':
				self.update_genre()
			elif o == '6':
				self.delete_genre()
			elif o == '7':
				return
			else:
				self.view.not_valid_option()
		return

	def ask_genre(self):
		self.view.ask('Nombre: ')
		name = input()
		self.view.ask('Descripcion: ')
		descrip = input()
		return[name, descrip]

	def create_genre(self):
		name, descrip = self.ask_genre()
		out = self.model.create_genre(name, descrip)
		if out == True:
			self.view.ok(name+' '+descrip, 'agrego')
		else:
			self.view.error('No se pudo agregar el Genero. REVISA')
		return

	def read_a_genre(self):
		self.view.ask('ID_Genero: ')
		id_genre = input()
		genre = self.model.read_a_genre(id_genre)
		if type(genre) == tuple:
			self.view.show_genre_header('  Datos del Genero '+id_genre+' ')
			self.view.show_a_genre(genre)
			self.view.show_genre_midder()
			self.view.show_genre_footer()
		else:
			if genre == None:
				self.view.error('EL Genero NO EXISTE')
			else:
				self.view.error('PROBLEMA AL LEER Genero. REVISA.')
		return

	def read_all_genres(self):
		genres = self.model.read_all_genres()
		if type(genres) == list:
			self.view.show_genre_header('  Todos los Generos  ')
			for genre in genres:
				self.view.show_a_genre(genre)
			self.view.show_genre_midder()
			self.view.show_genre_footer()
		else:
			self.view.error('PROBLEMA AL LEER LOS Generos. REVISA.')
		return

	def read_genres_name(self):
		self.view.ask('Nombre:')
		name = input()
		genres = self.model.read_genres_name(name)
		if type(genres) == list:
			self.view.show_genre_header(' Genero llamado de '+name+' ')
			for genre in genres:
				self.view.show_a_genre(genre)
			self.view.show_genre_midder()
			self.view.show_genre_footer()
		else:
			self.view.error('PROBLEMA al LEER LOS Generos. REVISA.')
		return

	def update_genre(self):
		self.view.ask('ID del Genero a modificar: ')
		id_genre = input()
		genre = self.model.read_a_genre(id_genre)
		if type(genre) == tuple:
			self.view.show_genre_header('Datos del Genero'+id_genre+' ')
			self.view.show_a_genre(genre)
			self.view.show_genre_midder()
			self.view.show_genre_footer()
		else:
			if genre == None:
				self.view.error('El Genero no existe')
			else:
				self.view.error('Problemas al leer el Genero, REVISA')
			return
		self.view.msg('Ingresa los valores a modificar:(vacio para dejarlo igual)')
		whole_vals = self.ask_genre()
		fields, vals = self.update_lists(['g_name','p_descrip'], whole_vals)
		vals.append(id_genre)
		vals = tuple(vals)
		out = self.model.update_genre(fields, vals)
		if out == True:
			self.view.ok(id_genre, 'actualizo')
		else:
			self.view.error('No se pudo actualizar el Genero. REVISA')
		return

	def delete_genre(self):
		self.view.ask('ID_Genero a borrar: ')
		id_genre = input()
		count = self.model.delete_genre(id_genre)
		if count !=0:
			self.view.ok(id_genre, 'borro')
		else:
			if count == 0:
				self.view.error('El Genero no existe')
			else:
				self.view.error('Problemas al leer el Genero. REVISA')
		return

	"""
	**************************
	* Controllers for Movies *
	**************************
	"""
	def movies_menu(self):
		o = '0'
		while o != '9':
			self.view.movies_menu()
			self.view.option('9')
			o = input()
			if o == '1':
				self.create_movie()
			elif o == '2':
				self.read_a_movie()
			elif o == '3':
				self.read_all_movies()
			elif o == '4':
				self.read_movies_year()
			elif o == '5':
				self.update_movie()
			elif o == '6':
				self.delete_movie()
			elif o == '7':
				self.create_movie_actors()
			elif o == '8':
				self.create_movie_genre()
			elif o == '9':
				return
			else:
				self.view.not_valid_option()
		return

	def ask_movie(self):
		self.view.ask('Nombre: ')
		name = input()
		self.view.ask('Año: ')
		year = input()
		self.view.ask('Sinopsis: ')
		sinopsis = input()
		self.view.ask('Director: ')
		director = input()
		return[name, year, sinopsis, director]

	def create_movie(self):
		name, year, sinopsis, director = self.ask_movie()
		out = self.model.create_movie(name, year,sinopsis, director)
		if out == True:
			self.view.ok(name+' '+year, 'agrego')
		else:
			self.view.error('No se pudo agregar la pelicula. REVISA')
		return

	def read_a_movie(self):
		self.view.ask('ID_movie: ')
		id_movie = input()
		movie = self.model.read_a_movie(id_movie)
		if type(movie) == tuple:
			self.view.show_movie_header('  Datos de la Pelicula '+id_movie+' ')
			self.view.show_a_movie(movie)
			self.view.show_movie_midder()
			self.view.show_movie_footer()
		else:
			if movie == None:
				self.view.error('LA PELICULA NO EXISTE')
			else:
				self.view.error('PROBLEMA AL LEER LA PELICULA. REVISA.')
		return

	def read_all_movies(self):
		movies = self.model.read_all_movies()
		if type(movies) == list:
			self.view.show_movie_header('  Todos los Generos  ')
			for movie in movies:
				self.view.show_a_movie(movie)
			self.view.show_movie_midder()
			self.view.show_movie_footer()
		else:
			self.view.error('PROBLEMA AL LEER LAS PELICULAS. REVISA.')
		return

	def read_movies_year(self):
		self.view.ask('Año:')
		year = input()
		movies = self.model.read_movies_name(year)
		if type(movies) == list:
			self.view.show_movie_header(' PELICULA llamada de '+year+' ')
			for movie in movies:
				self.view.show_a_movie(movie)
			self.view.show_movie_midder()
			self.view.show_movie_footer()
		else:
			self.view.error('PROBLEMA al LEER LAS PELICULAS. REVISA.')
		return

	def update_movie(self):
		self.view.ask('ID de la pelucula a modificar: ')
		id_movie = input()
		movie = self.model.read_a_movie(id_movie)
		if type(movie) == tuple:
			self.view.show_movie_header('Datos de la pelicula'+id_movie+' ')
			self.view.show_a_movie(movie)
			self.view.show_movie_midder()
			self.view.show_movie_footer()
		else:
			if movie == None:
				self.view.error('La pelicula no existe')
			else:
				self.view.error('Problemas al leer la pelicula, REVISA')
			return
		self.view.msg('Ingresa los valores a modificar:(vacio para dejarlo igual)')
		whole_vals = self.ask_movie()
		fields, vals = self.update_lists(['m_name','m_year','m_sinopsis','id_director'], whole_vals)
		vals.append(id_movie)
		vals = tuple(vals)
		out = self.model.update_movie(fields, vals)
		if out == True:
			self.view.ok(id_movie, 'actualizo')
		else:
			self.view.error('No se pudo actualizar la pelucula. REVISA')
		return

	def delete_movie(self):
		self.view.ask('ID Pelicula a borrar: ')
		id_movie = input()
		count = self.model.delete_movie(id_movie)
		if count !=0:
			self.view.ok(id_movie, 'borro')
		else:
			if count == 0:
				self.view.error('La pelicula no existe')
			else:
				self.view.error('Problemas al leer la pelicula. REVISA')
		return

	def create_movie_actors(self):
		self.view.ask('ID actor: ')
		id_actor = input()
		self.view.ask('ID pelicula: ')
		id_movie = input()
		self.view.ask('salario: ')
		salario = input()
		if id_actor != '':
			actor = self.model.read_a_actor(id_actor) 
			if type(actor) == tuple:
				self.view.show_actor_header(' Datos del actor '+id_actor+' ')
				self.view.show_a_actor(actor)
				self.view.show_actor_footer()
				self.view.ask('Salario: ')
				out = self.model.create_movie_actors(id_movie, id_actor, salario)
				if out == True:
					self.view.ok( 'Agrego a la pelicula')
				else:
					if out.errno == 1062:
						self.view.error('el actor ya esta en la pelicula')
					else:
						self.view.error('No se pudo agregar el producto. REVISA.')
					
			else:
				if product == None:
					self.view.error('El producto no existe')
				else:
					self.view.error('Problemas al leer el producto. REVISA.')
		return id_movie, salario

	def create_movie_genre(self):
		self.view.ask('ID pelicula: ')
		id_movie = input()
		self.view.ask('ID genero: ')
		id_genre = input()
		
		if id_genre != '':
			genre = self.model.read_a_genre(id_genre) 
			if type(genre) == tuple:
				self.view.show_genre_header(' Datos del movie '+id_genre+' ')
				self.view.show_a_genre(genre)
				self.view.show_genre_footer()
				
				out = self.model.create_movie_genre(id_movie, id_genre)
				if out == True:
					self.view.ok( 'Agrego a la genero')
				else:
					if out.errno == 1062:
						self.view.error('el genero ya esta en la pelicula')
					else:
						self.view.error('No se pudo agregar el genero. REVISA.')
					
			else:
				if product == None:
					self.view.error('El genro no existe')
				else:
					self.view.error('Problemas al leer el genero. REVISA.')
		return id_movie