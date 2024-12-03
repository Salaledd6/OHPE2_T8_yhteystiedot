import json

yhteystiedot = {
    "Aleksi": {
        "puhelin": "0404132963",
        "sahkoposti": "aleksi.salin@seamk.fi"
    },
    "Matti": {
        "puhelin": "0501234567",
        "sahkoposti": "matti.meikalainen@example.com"
    }
}

def hae_nimella(sanakirja: dict): 
    nimi = input("Hae henkilöä: ") 
    if nimi in sanakirja:
        print(f"Nimi: {nimi}, puhelinumero {sanakirja[nimi]['puhelin'],}, sahkoposti: {sanakirja[nimi]['sahkoposti']} ")
    else:
        print("Yritä uudelleen")

def lisaa_yhteystieto(sanakirja: dict):
    print("Syötä lisättävän henkilön tiedot")
    nimi = input("Nimi > ")
    numero = input("puhelinnumero > ")
    posti = input("posti > ")
    sanakirja[nimi] = {"puhelin": numero, "sahkoposti": posti}
    

def poista_yhteystieto(sanakirja: dict):
    nimi = input("Syötä poistettavan henkilön nimi")
    if nimi in sanakirja:
         sanakirja.pop(nimi)
    else:
        print("Yritä uudelleen")
    
f = open("yhteystiedot.json", "r") #tiedoston avaaminen
merkkijonona = f.read() # luetaan merkkijono tiedostosta
yhteystiedot = json.loads(merkkijonona) #merkkijonosta sanak
f.close #tiedoston sulkeminen  

'''Ohjelman suoritus alkaa tästä'''
while True:
    print("Valitse toiminto 1: Hae nimellä")
    print("Valitse toiminto 2: Lisää yhteystieto")
    print("Valitse toiminto 3: Poista yhteystieto")
    print("Valitse toiminto 4: Lopeta")


    valinta = input("> ")

    if valinta == "1":
        hae_nimella(yhteystiedot)
    elif valinta == "2":
        lisaa_yhteystieto(yhteystiedot)
    elif valinta == "3":
        poista_yhteystieto(yhteystiedot)
    else:
        break

    f = open("yhteystiedot.json", "w") #avataan tiedosto kirjoitustilassa
    merkkijonona = json.dumps(yhteystiedot) # muutetaan tiedosto json merkkijonoksi
    f.write(merkkijonona) # kirjoitetaan merkkijono json tiedostoon
    f.close() #tiedoston sulkeminen

