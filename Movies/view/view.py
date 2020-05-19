class View:
	"""
	*************************
	* A view for a store DB *
	*************************
	"""
	def start(self):
		print('================================================')
		print('= ¡Bienvenido a nuestro Catalogo de peliculas! =')
		print('================================================')

	def end(self):
		print('=================================')
		print('=       ¡Vuelve pronto!         =')
		print('=================================')

	def main_menu(self):
		print('************************')
		print('* -- Menu Principal -- *')
		print('************************')
		print('1. Directors')
		print('2. Actors')
		print('3. Generos')
		print('4. Peliculas')
		print('5. Salir')

	def option(self, last):
		print('Seleciona una opcion (1-'+last+'):', end = '')

	def not_valid_option(self):
		print('¡Opcion no valida!\nIntenta de nuevo')

	def ask(self, output):
		print(output, end = '')

	def msg(self, output):
		print(output)

	def ok(self, id, op):
		print('+'*(len(str(id))+len(op)+24))
		print('+ ¡'+str(id)+' se '+op+' correctamente! +')
		print('+'*(len(str(id))+len(op)+24))

	def error(self, err):
		print('  ¡ERROR!  '.center(len(err)+4,'-'))
		print('- '+err+' -')
		print('-'*(len(err)+4))

	"""
	***********************
	* Views for directors *
	***********************
	"""
	def directors_menu(self):
		print('****************************')
		print('* -- Submenu Directores -- *')
		print('****************************')
		print('1. Agregar Director')
		print('2. Mostrar a un Director')
		print('3. Mostrar todos los Directores')
		print('4. Mostrar Directores de una nacionalidad')
		print('5. Actualizar Director')
		print('6. Borrar Director')
		print('7. Regresar')

	def show_a_director(self, record):
		print('ID:', record[0])
		print('Nombre:', record[1])
		print('A.Paterno:', record[2])
		print('A.Marterno:', record[3])
		print('Nacionalidad:', record[4])

	def show_director_header(self, header):
		print(header.center(48,'*'))
		print('-'*48)

	def show_director_midder(self):
		print('-'*78)

	def show_director_footer(self):
		print('*'*78)

	"""
	********************
	* Views for Actors *
	********************
	"""
	def actors_menu(self):
		print('*************************')
		print('* -- Submenu Actores -- *')
		print('*************************')
		print('1. Agregar Actor')
		print('2. Mostrar a un Actor')
		print('3. Mostrar todos los Actores')
		print('4. Mostrar Actores de una nacionalidad')
		print('5. Actualizar Actor')
		print('6. Borrar Actor')
		print('7. Regresar')

	def show_a_actor(self, record):
		print('ID:', record[0])
		print('Nombre:', record[1])
		print('A.Paterno:', record[2])
		print('A.Marterno:', record[3])
		print('Nacionalidad:', record[4])

	def show_actor_header(self, header):
		print(header.center(48,'*'))
		print('-'*48)

	def show_actor_midder(self):
		print('-'*78)

	def show_actor_footer(self):
		print('*'*78)

	"""
	********************
	* Views for Genres *
	********************
	"""
	def genres_menu(self):
		print('*************************')
		print('* -- Submenu Generos -- *')
		print('*************************')
		print('1. Agregar Genero')
		print('2. buscar a un Genero por ID')
		print('3. Mostrar todos los Generos')
		print('4. Buscar Generos por Nombre')
		print('5. Actualizar Genero')
		print('6. Borrar Genero')
		print('7. Regresar')

	def show_a_genre(self, record):
		print('ID:', record[0])
		print('Nombre:', record[1])
		print('Descripcion:', record[2])
		

	def show_genre_header(self, header):
		print(header.center(48,'*'))
		print('-'*48)

	def show_genre_midder(self):
		print('-'*78)

	def show_genre_footer(self):
		print('*'*78)

	"""
	********************
	* Views for movies *
	********************
	"""
	def movies_menu(self):
		print('*************************')
		print('* -- Submenu Peliculas -- *')
		print('*************************')
		print('1. Agregar Pelicula')
		print('2. Leer una Pelicula')
		print('3. Leer Todas las peliculas')
		print('4. Buscar peliculas por año')
		print('5. Actualizar Pelicula')
		print('6. Borrar Pelicula')
		print('7. Crear pelicula actor')
		print('8. Crear pelicula genero')
		print('9. Regresar')

	def show_a_movie(self, record):
		print('ID:', record[0])
		print('Nombre:', record[1])
		print('Año:', record[2])
		print('Sipnosis:', record[3])
		print('Director:', record[4])
		

	def show_movie_header(self, header):
		print(header.center(48,'*'))
		print('-'*48)

	def show_movie_midder(self):
		print('-'*78)

	def show_movie_footer(self):
		print('*'*78)
