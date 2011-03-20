#!/usr/bin/python3.1
# -*- coding: UTF-8 -*-

def python_3_tukee_unicodemerkkejä_varsin_laajasti(ភាសាខ្មែរ="khemrin kieli khmeriksi"):
	print("Hei vaan ja hellurei!", ភាសាខ្មែរ)
	
	epävalidia_python_koodia='kuitenkin_esim_€_merkki_ei_ole_sallittu = "epic fai"'
	try:
		exec(epävalidia_python_koodia)
	except SyntaxError as se:
		print("€-merkki ei ollut sallittu muuttujan nimessä :'(", se)
	
	validia_python_koodia = epävalidia_python_koodia.replace("€", "e")
	exec(validia_python_koodia)
	print("Hyvin pyyhkii. No problemo, kun €-merkit vaihdettiin e-kirjaimiksi")

if __name__ == "__main__":
	python_3_tukee_unicodemerkkejä_varsin_laajasti()