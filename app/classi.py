#classi.py


class Pianta:
    """
    Classe base che rappresenta una pianta generica del giardino.
    Gestisce crescita, irrigazione , raccolta e informazioni generali comuni a tutte le piante.
    """
    def __init__(self, nome, terriccio, diametro_vaso, freq_acqua, vel_crescita, altezza=0, num_frutti=0):
        """
        Inizializza una nuova pianta.
        Args:
            nome(str):nome della pianta.
            terriccio(str): tipo di terriccio richiesto.
            diametro_vaso(float): diametro del vaso in cm.
            freq_acqua (int): giorni massimi senza acqua.
            vel_crescita (float): crescita giornaliera in mm.
            altezza (float, optional): altezza iniziale.
            num_frutti (float, optional): quantità iniziale di frutti.
        """
        self.nome=nome
        self.terriccio=terriccio
        self.diametro_vaso=diametro_vaso
        self.freq_acqua=freq_acqua
        self.vel_crescita= vel_crescita
        self.giorni_senza_acqua=0
        self.altezza=altezza
        self.num_frutti=num_frutti
    def annaffia(self):
        """
        Annaffia la pianta azzerando il contatore dei giorni
        trascorsi dall'ultima irrigazione.
        """
        self.giorni_senza_acqua = 0
    def bisogna_annaffiare(self):
        """
        Verifica se la pianta necessita di essere annaffiata.

        Returns:
            bool: True se deve essere annaffiata.
        """
        if self.giorni_senza_acqua>=self.freq_acqua:
            return True
        else:
            return False
    def bisogna_travasare(self):
        """
        Verifica se il vaso è diventato troppo piccolo.

        Returns:
            bool: True se la pianta dovrebbe essere travasata.
        """
        diametro_mm=self.diametro_vaso*10
        if self.altezza>=diametro_mm*2:
            return True
        else:
            return False
    def cresce(self):
        """
        Simula la crescita della pianta per un giorno.
        """
        self.altezza+=self.vel_crescita/10
    def pota(self, quanto:float):
        """
        Riduce l'altezza della pianta.

        Args:
            quanto (float): quantità da rimuovere.
        """
        self.altezza-=quanto
    def cogli(self, quanti:int):
        """
        Raccoglie un certo numero di frutti.
        Args:
            quanti (int): numero di frutti da raccogliere.
        Raises:
            ValueError: se i frutti richiesti superano quelli disponibili.
        """
        if quanti>self.num_frutti:
            raise ValueError(f"Impossibile cogliere {quanti} frutti, ce ne sono solo {self.num_frutti}. ")
        self.num_frutti-=quanti
        return f"Hai raccolti {quanti} frutti."
    
    def __str__(self):
        """
        Restituisce una descrizione completa della pianta.

        Returns:
            str: descrizione della pianta.
        """
        return f"""{self.nome}: è un {self.__class__.__name__} quindi vuole un terriccio {self.terriccio},
        il vaso ha un diametro di {self.diametro_vaso}cm,
        vuole l'acqua ogni {self.freq_acqua} giorni e sono {self.giorni_senza_acqua} giorni che non beve,
        è alto {self.altezza:.2f}cm e cresce {self.vel_crescita}mm/giorno
        adesso ha {self.num_frutti} frutti/foglie pronti per essere raccolti """

class Agrume(Pianta):
    def __init__(self, nome, diametro_vaso,altezza=0, num_frutti=0):
        super().__init__(
            nome=nome,
            terriccio='Specifico per agrumi',
            diametro_vaso=diametro_vaso,
            freq_acqua=7,
            vel_crescita=2,
            altezza=altezza,
            num_frutti=num_frutti
        )
    def cresce_frutti(self): #forse non ha senso
        """
        Simula la crescita di nuovi frutti.
        """
        if self.giorni_senza_acqua==6:
            self.num_frutti+=1
class Cactus(Pianta):
    def __init__(self, nome, diametro_vaso, altezza=0, num_frutti=0):
        super().__init__(
            nome=nome,
            terriccio='Sabbioso e drenante',
            diametro_vaso=diametro_vaso,
            freq_acqua=21,
            vel_crescita=0.2,
            altezza=altezza,
            num_frutti=num_frutti
        )
class Pomodoro(Pianta):
    def __init__(self, nome, diametro_vaso, altezza=0, num_frutti=0):
        super().__init__(
            nome=nome,
            terriccio='Universale',
            diametro_vaso=diametro_vaso,
            freq_acqua=2,
            vel_crescita=5,
            altezza=altezza,
            num_frutti=num_frutti
        )
    def cresce_frutti(self):  #forse non ha senso
        """
        Simula la crescita di nuovi frutti.
        """
        if self.giorni_senza_acqua==1:
            self.num_frutti+=0.1
            
class Basilico(Pianta):
    def __init__(self, nome, diametro_vaso, altezza=0, num_foglie=20):
        super().__init__(
            nome=nome,
            terriccio='Universale',
            diametro_vaso=diametro_vaso,
            freq_acqua=2,
            vel_crescita=5,
            altezza=altezza
        )
        self.num_foglie=num_foglie
    def cresce_foglie(self): #forse non ha senso
        """
        Simula la crescita di nuove foglie.
        """
        if self.giorni_senza_acqua==1:
            self.num_foglie+=1
    def cogli(self, quanti): #da vedere come estendere il metodo coglie della classe pianta 
        """
        Raccoglie foglie di basilico.
        Args:
            quanti (int): numero di foglie da raccogliere.
        Raises:
            ValueError: se le foglie richieste non sono disponibili.
        """
        if quanti>self.num_foglie:
            raise ValueError(f"Impossibile cogliere {quanti} foglie, ce ne sono solo {self.num_foglie}. ")
        self.num_foglie-=quanti
        return f"Raccolte {quanti} foglie di basilico."

class Aloe(Pianta):
    def __init__(self, nome, diametro_vaso, altezza=0, num_frutti=0):
        super().__init__(
            nome=nome,
            terriccio='Drenante',
            diametro_vaso=diametro_vaso,
            freq_acqua=15,
            vel_crescita=0.3,
            altezza=altezza,
            num_frutti=num_frutti
        )
    def cogli(self, quanti):
        return f"Gel di aloe estratto da {quanti} foglie."

class Rosmarino(Pianta):
    def __init__(self, nome, diametro_vaso, altezza=0, num_frutti=0):
        super().__init__(
            nome=nome,
            terriccio='Roccioso',
            diametro_vaso=diametro_vaso,
            freq_acqua=10,
            vel_crescita=1,
            altezza=altezza,
            num_frutti=num_frutti
        )
    def cogli(self, quanti):
        return f"{quanti} rametti di rosmarino raccolti."

class Altro(Pianta):
    """
    Permette di definire una pianta personalizzata.
    """
    def __init__(self, nome, terriccio, diametro_vaso, freq_acqua, vel_crescita, altezza=0, num_frutti=0):
        super().__init__(
            nome=nome,
            terriccio=terriccio,
            diametro_vaso=diametro_vaso,
            freq_acqua=freq_acqua,
            vel_crescita=vel_crescita,
            altezza=altezza,
            num_frutti=num_frutti
        )
    def __str__(self):
        return f"""{self.nome}: vuole un terriccio {self.terriccio},
        il vaso ha un diametro di {self.diametro_vaso}cm,
        vuole l'acqua ogni {self.freq_acqua} giorni e sono {self.giorni_senza_acqua} giorni che non beve,
        è alto {self.altezza}cm e cresce {self.vel_crescita}mm/giorno
        adesso ha {self.num_frutti} frutti/foglie pronti per essere raccolti """

