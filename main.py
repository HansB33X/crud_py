#project CRUD dengan Python
#code by hans@root
#sab 22/01/22
#run on linux/termux

import os
import time as waktu
import pyfiglet as figlet

try:
	def main():
		os.system('clear')
		create_file()


	def create_file():
		if os.path.isfile('data.txt') == True:
			login()
			pass
		else:
			create_file = open('data.txt', 'x')
			if os.path.isfile('data.txt') == True:
				print("file database berhasil dibuat...")
				waktu.sleep(1)
				os.system('clear')
				login()
			else:
				print("gagal membuat file...")


	def read_file():
		create_file()
		readfile = open('data.txt', 'r')
		print(readfile.read())
		readfile.close()
		welcome()


	def delete_data():
		open('data.txt', 'r')
		os.system('rm data.txt')
		if  os.path.isfile('data.txt') == False:
			print("data berhasil dihapus...")
			waktu.sleep(0.5)
			welcome()
		else:
			print('data gagal dihapus...')
			waktu.sleep(0.5)
			welcome()


	def upload_data():
		create_file()
		nimkar = input("Masukan nama karyawan> ")
		agekar = input("Masukan umur karyawan> ")
		addrkar = input("Masukan alamat karyawan> ")
		updat = open('data.txt')
		write = "Nama: {}, Umur: {}, Alamat: {}\n".format(nimkar, agekar, addrkar)
		open_file = open('data.txt', 'w')
		open_file.write(write)
		print("data berhasil di upload")
		open_file.close()
		waktu.sleep(3)
		os.system('clear')
		welcome()


	def login():
		user = None
		user = input("login> ")
		os.system('clear')
		print("hai",user,"selamat datang di program CRUD")
		input("[press any key to continue...]")
		waktu.sleep(1)
		os.system('clear')
		welcome()	


	def welcome():
		print(figlet.figlet_format("CRUD"))
		print('by hans\n')
		menu()


	def help():
		print("1 > upload data")
		print("2 > read data")
		print("3 > delete all data")
		print("4 > exit\n")
		welcome()


	def menu():
		input_menu = input("crud> ")
		if input_menu == "help()":
			help()
		if input_menu == "1":
			upload_data()
		if input_menu == "2":
			read_file()
		if input_menu == "3":
			delete_data()
		if input_menu == "4":
			print("logout...")
			waktu.sleep(3)
			os.system('clear')
			print("logout berhasil!")
			waktu.sleep(1)
			os.system('clear')
		else:
			print("perintah yang anda masukan salah, ketik help() untuk bantuan")
			welcome()

	if __name__ == '__main__':
		main()
except:
	print("\nSintaks yang anda masukan salah...\nsilahkan jalankan ulang program\njika masih terjadi kendala harap hubungi\nHans(developer) : 087850013150")