# Šis file yra vykdomas, kai veikia check50 komanda (užduoties tikrinimas)
# Kodas yra rašomas Python kalba.
# Štai yra pavyzdinis kodas, kuris patikrina ar egzistuoja visi failai, ar duomenų failas yra surašytas teisingai,
# ar rezultatų faile yra išvesta teisinga informacija ir patikrinimas, ar gaunamas teisingas atsakymas pagal du pavyzdžius.

import check50 # importuojama check50 aplinka.

# funkcijos iki test0 veikia visuose uždaviniuose, tik reikia pakeisti uzduotis.cpp į savo užduoties failo pavadinimą.

@check50.check() # vykdoma check funkcija
def egzistuoja(): # egzistuoja yra funkcijos pavadinimas, jį galima keisti
  """balsavimas.cpp egzistuoja.""" # šis tekstas bus išvedamas jeigu nebus klaidų
  check50.exists("balsavimas.cpp") # Vykdoma funkcija, kuri patikrina, ar failas uzduotis.cpp egzistuoja
  # jeigu egzistuoja, tada išvedamas tekstas, kuris yra parašytas funkcijos pradžioje (uzduotis.cpp egzistuoja)

@check50.check(egzistuoja) # ši funkcija veikia tik tada jeigu funkcija pavadinimu egzistuoja veikia.
def kompiliuojasi(): # kompiliuojasi yra funkcijos pavadinimas, jį galima keisti
    """balsavimas.cpp kompiliuojasi be klaidų.""" # šis tekstas bus išvedamas jeigu programa kompiliuosis be klaidų
    check50.run("g++     balsavimas.cpp  -lcrypt -lcs50 -lm -o balsavimas").exit(0) # tikrina, ar pasileidžia programa (tas pats kaip
    # per code blocks paspausti F9).
   
@check50.check(kompiliuojasi) # funkcija veikia tik tada, jeigu failas kompiliuojasi.
def egzistuoja_Duomenys(): # egzistuoja_Duomenys yra funkcijos pavadinimas, jį galima keisti
    """Duomenys.txt egzistuoja.""" # ši funkcija veikia tik tada jeigu Duomenų failas egzistuoja.
    check50.exists("Duomenys.txt") # tikrinama, ar egzistuoja Duomenys.txt failas sistemoje.
   
@check50.check(kompiliuojasi) # funkcija veikia tik tada, jeigu failas kompiliuojasi.
def egzistuoja_Rezultatai(): # egzistuoja_Rezultatai yra funkcijos pavadinimas, jį galima keisti
    """Rezultatai.txt egzistuoja.""" # ši funkcija veikia tik tada jeigu Rezultatų failas egzistuoja.
    check50.exists("Rezultatai.txt") # tikrinama, ar egzistuoja Rezultatai.txt failas sistemoje.
