#funzioni.py
import os
import logging
from app.classi import Agrume, Cactus, Pomodoro, Basilico, Aloe, Rosmarino, Altro
from app.dati import giardino

def pulisci_schermo():
    if os.name == "nt":      # Windows
        os.system("cls")
    else:                    # Linux/macOS
        os.system("clear")


def esegui_raccolto(pianta, quantita):
    """
    Esegue la raccolta di frutti o foglie da una pianta.
    Gestisce eventuali errori e li registra nel log.
    """
    try:
        print(pianta.cogli(quantita))
        logging.info(f"Raccolta completata: {quantita} da {pianta}")
    except ValueError as errore:
        print(f"ERRORE: {errore}")
        logging.warning(f"Raccolta fallita di {quantita} da {pianta}, {errore}")

def aggiungi_pianta():
    """
    Permette all'utente di registrare una nuova pianta
    nel giardino.
    """
    tipo=input('''Che tipo di pianta vuoi aggiungere al giardino?
    Agrume, Cactus, Pomodoro, Basilico, Aloe, Rosmarino, Altro
    >>> ''').capitalize()
    mappa_classi={
        "Agrume": Agrume,
        "Cactus": Cactus,
        "Pomodoro": Pomodoro,
        "Basilico": Basilico,
        "Aloe":Aloe,
        "Rosmarino": Rosmarino,
        "Altro": Altro
    }
    if tipo not in mappa_classi:
        logging.warning(f'Tipo di pianta da aggiungere non riconosciuta: {tipo}')
        altro=input("Forse intendevi 'Altro'? (si/no) ")
        if altro=='si':
            classe=mappa_classi['Altro']
        elif altro=='no':
            print('Allora non voglio questa pianta.')
            return
    else:
        classe=mappa_classi[tipo]
    nome=input(f'Come si chiama questo {tipo}? ').lower()
    diam_vaso=chiedi_float_positivo(f"Quanto è grande il vaso? (il diametro in cm) ")
    altezza=chiedi_float_positivo(f"Quanto è alta la pianta ora? (in cm) ")
    num_frutti=chiedi_float_positivo('Quanti frutti ci sono su questa pianta ora? ')

    if classe!=mappa_classi['Altro']:
        giardino.append(classe(nome, diam_vaso, altezza, num_frutti))
        print(f'{nome.capitalize()} registrata con successo!')
        logging.info(f"Nuova pianta registrata: {nome} (Tipo: {tipo})")
    else:
        terra=input('Che tipo di terriccio ha? ')
        freq=chiedi_intero_positivo('Ogni quanti giorni va annaffiata? ')
        vel=chiedi_float_positivo('Quanti millimetri cresce al giorno? ')
        giardino.append(classe(nome, terra, diam_vaso, freq, vel, altezza, num_frutti))
        print(f'{nome.capitalize()} registrata con successo!')
        logging.info(f"Nuova tipo di pianta registrato: {nome} (Tipo: {tipo})")

def trova_pianta(giardino, nome):
    """Trova una pianta nel giardino partendo dal nome"""
    for pianta in giardino:
        if pianta.nome == nome:
            return pianta
    return None

def rimuovi_pianta():
    """
    Permette all'utente di rimuovere una pianta dal giardino.
    """
    nome=input('Quale pianta vuoi togliere dal giardino? ')
    pianta=trova_pianta(giardino, nome)
    if pianta:
        giardino.remove(pianta)

def passa_un_giorno():
    """
    Simula il passaggio di un giorno per tutte le piante.
    """
    logging.info('è passato un giorno')
    for pianta in giardino:
        pianta.cresce()
        pianta.giorni_senza_acqua+=1



def chiedi_intero_positivo(messaggio):
    """
    Richiede un numero intero positivo all'utente.
    Args:
        messaggio (str): messaggio mostrato all'utente.
    Returns:
        int: valore inserito.
    """
    while True:
        valore=input(messaggio)
        try:
            numero = int(valore)
            if numero < 0:
                print('Non può essere negativo, riprova')
                logging.warning(f'Numero negativo bloccato: {numero}')
                continue
            return numero
        
        except ValueError:
            print("Devi inserire un numero intero valido, riprova")
            logging.error(f"Input bloccato: '{valore}' invece di un intero")

def chiedi_float_positivo(messaggio):
    """
    Richiede un numero decimale positivo all'utente.

    Args:
        messaggio (str): messaggio mostrato all'utente.

    Returns:
        float: valore inserito.
    """
    while True:
        valore=input(messaggio)
        try:
            numero = float(valore)
            if numero < 0:
                print('Non può essere negativo, riprova')
                logging.warning(f'Numero negativo bloccato: {numero}')
                continue
            return numero
        except ValueError:
            print("Devi inserire un numero valido, riprova")
            logging.error(f"Input bloccato: '{valore}' invece di un float")


def annaffia_una_pianta():
    nome=input('Quale pianta vuoi annaffiare? ')
    pianta=trova_pianta(giardino, nome)
    if pianta:
        pianta.annaffia()
    else:
        print(f"Non c'è nessuna pianta chiamata {nome}.")  

def raccogli_frutti_foglie():
    nome=input('Di quale pianta vuoi raccogliere i frutti o le foglie? ')
    pianta=trova_pianta(giardino,nome)
    if pianta:
        quanti=chiedi_intero_positivo('Quanti ne vuoi raccogliere? ')
        esegui_raccolto(pianta, quanti)
    else:
        print(f"Non c'è nessuna pianta chiamata {nome}.")


