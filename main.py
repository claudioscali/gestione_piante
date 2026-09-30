#main.py
import logging
import datetime
import math

from app.dati import giardino
from app.funzioni import (
    pulisci_schermo, 
    aggiungi_pianta, 
    passa_un_giorno, 
    raccogli_frutti_foglie, 
    annaffia_una_pianta, 
    rimuovi_pianta
)

logging.basicConfig(
    filename='gestionale.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

while True:
    pulisci_schermo()
    print('#'*60)
    inizio=datetime.datetime.now()
    for pianta in giardino:
        if pianta.bisogna_annaffiare():
            print(f"DEVI ANNAFFIARE {pianta.nome.upper()}!!!!!")
    azione=input("""Che cosa vuoi fare? 
    1.aggiungi una pianta
    2.visualizza la descrizione del giardino
    3.fai passare un giorno
    4.raccogli frutti/foglie
    5.annaffia una pianta
    6.annaffia tutte le piante
    7.togli una pianta
    0.uscire
    >>> """)
    if azione =='1':
        aggiungi_pianta()
    elif azione=='2':
        for pianta in giardino:
            print(pianta)
        invio=input()
    elif azione=='3':
        passa_un_giorno()
    elif azione=='4':
        raccogli_frutti_foglie()
    elif azione=='5':
        annaffia_una_pianta() 
    elif azione=='6':
        for pianta in giardino:
            pianta.annaffia()      
    elif azione=='7':
        rimuovi_pianta()   
    elif azione=='0':
        print('Ciao.')
        break
    else:
        print("Devi scegliere una tra le cose che ti ho proposto, riprova")

    adesso=datetime.datetime.now()
    intervallo=(adesso-inizio).seconds
    for i in range(math.floor(intervallo/86400)):
        passa_un_giorno()
    print(f'Sono passati {math.floor(intervallo/86400)} giorni')#ogni 86400 secondi passa un giorno 


