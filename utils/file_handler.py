import os
import json


class FileHandler:

	# class atribútumok:
	poster_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), "poster")
	print(poster_folder)
	metadata_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), "metadata")
	print(metadata_folder)
	movie_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), "movies")
	print(movie_folder)

	def __init__(self):

		self.value = 0
		self.__create_necessary_folders()

	def __create_necessary_folders(self):
		if not os.path.exists(self.poster_folder):
			os.mkdir(self.poster_folder)
		# poster-metadata
		if not os.path.exists(self.metadata_folder):
			os.mkdir(self.metadata_folder)

	def get_data_from_folder(self):
		if not os.path.exists(self.movie_folder):
			raise FileNotFoundError(f"File not exists -:)")
		temp = []
		for item in os.listdir(self.movie_folder):
			if item[-4:] == ".mkv":
				temp.append(item)
		print(temp)

	def get_jason_path(self):
		return os.path.join(self.metadata_folder, f'{self.movies}')

	# def write_json(self.movie_name, data):


if __name__ == '__main__':
	test = FileHandler()
	test.get_jason("Alien")
	test.get_data_from_folder()
