# Auteur: Gertjan Leemans, 500895041
# Doel: Het omrekenen van buitenlandse valuta naar Euro's

# imports
import requests
import json

# variabelen
valuta = int(input("Valuta (1 = US Dollar, 2 = GB pounds, 3 = Yen): "))
hoeveel = int(input("Hoeveel wilt u wisselen? "))
# koers request USD
request_usd = requests.get("https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/usd/eur.min.json")
data_usd = request_usd.text
parsed_usd = json.loads(data_usd)
koers_usd = float(parsed_usd["eur"])
# koers reqest voor GBP
request_gbp = requests.get("https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/gbp/eur.min.json")
data_gbp = request_gbp.text
parsed_gbp = json.loads(data_gbp)
koers_gbp = float(parsed_gbp["eur"])
# koers request voor JPY
request_jpy = requests.get("https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/jpy/eur.min.json")
data_jpy = request_jpy.text
parsed_jpy = json.loads(data_jpy)
koers_jpy = float(parsed_jpy["eur"])
# transactie percentage
transactie = 0.015

# berekeningen voor USD
som_usd = hoeveel * koers_usd
trans_usd = som_usd * transactie
# transactie kosten USD min 2 max 15 euro
if trans_usd < 2:
    transactie_kosten_usd = 2
elif trans_usd > 15:
    transactie_kosten_usd = 15
else:
    transactie_kosten_usd = trans_usd
# Berekeningen voor GBP
som_gbp = hoeveel * koers_gbp
trans_gbp = som_gbp * transactie
# transactie kosten GBP min 2 max 15 euro
if trans_gbp < 2:
    transactie_kosten_gbp = 2
elif trans_gbp > 15:
    transactie_kosten_gbp = 15
else:
    transactie_kosten_gbp = trans_gbp
# Berekeningen voor Yen
som_jpy = hoeveel * koers_jpy
trans_jpy = som_jpy * transactie
# transactie kosten Yen min 2 max 15 euro
if trans_jpy < 2:
    transactie_kosten_jpy = 2
elif trans_jpy > 15:
    transactie_kosten_jpy = 15
else:
    transactie_kosten_jpy = trans_jpy

# uitvoering
if valuta == 1:
    print("Voor " + str(hoeveel) + " US Dollar krijgt u " + str(round(som_usd, 2)) + " Euro. "
          + "De transactie kosten bedraagt " + str(round(transactie_kosten_usd, 2)) + " Euro. U ontvangt "
          + str(round(som_usd - transactie_kosten_usd, 2)) + " Euro.")
elif valuta == 2:
    print("Voor " + str(hoeveel) + " Brites Ponden krijgt u " + str(round(som_gbp, 2)) + " Euro. "
          + "De transactie kosten bedraagt " + str(round(transactie_kosten_gbp, 2)) + " Euro. U ontvangt "
          + str(round(som_gbp - transactie_kosten_gbp, 2)) + " Euro.")
elif valuta == 3:
    print("Voor " + str(hoeveel) + " Japanse Yen krijgt u " + str(round(som_jpy, 2)) + " Euro. "
          + "De transactie kosten bedraagt " + str(round(transactie_kosten_jpy, 2)) + " Euro. U ontvangt "
          + str(round(som_jpy - transactie_kosten_jpy, 2)) + " Euro.")
else:
    print("Ongeldige invoer")
