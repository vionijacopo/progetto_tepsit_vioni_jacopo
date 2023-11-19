import socket

HOST = 'localhost'  # Indirizzo IP del server
PORT = 50007  # Porta su cui il server sta ascoltando

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

def funz_password():
    for _ in range(3):
        password = input("Inserisci la password: ")
        s.send(password.encode())
        response = s.recv(1024).decode()
        if response == "Password corretta. Inizia la comunicazione":
            return True
        else:
            print(response)
    return False

if funz_password():
    print("Autenticazione riuscita. Puoi iniziare a effettuare le operazioni.")
    while True:
        print("Scegli un'operazione:")
        print("1. Leggi dati di una tabella")
        print("2. Elimina un'istanza di una tabella")
        print("3. Inserisci un'istanza nella tabella")
        print("4. Modifica un dato di una tabella")
        print("5. Esci")

        scelta = input("Operazione: ")
        s.send(scelta.encode())

        if scelta == "5":
            print("Uscito")
            break

        if scelta == "1":

            scelta2 = 0
            while(scelta2 != "1" and scelta2 != "2"):
                scelta2=input("Inserisci 1 per leggere dipendenti o 2 per le zone: ")

            s.send(str(scelta2).encode())

            if scelta2 == "1":
                nome_d = input("Inserisci il nome del dipendente: ")
                s.send(nome_d.encode())
                response = s.recv(1024).decode()
                print(response)

            else:
                nome = input("Inserisci il nome della zona: ")
                s.send(nome.encode())
                response = s.recv(1024).decode()
                print(response)

            
        
        if scelta == "2":

            scelta2 = 0
            while(scelta2 != "1" and scelta2 != "2"):
                scelta2=input("Inserisci 1 per eliminare dipendenti o 2 per eliminare zone: ")

            s.send(str(scelta2).encode())

            if scelta2 == "1":
                id_elimina = input("Inserisci l'id del dipendente per eliminare la sua istanza dalla tabella del database: ")
                s.send(id_elimina.encode())

            else:
                id_elimina = input("Inserisci l'id della zona per eliminare la sua istanza dalla tabella del database: ")
                s.send(id_elimina.encode())

        if scelta == "3":

            scelta2 = 0
            while(scelta2 != "1" and scelta2 != "2"):
                scelta2=input("Inserisci 1 per eliminare dipendenti o 2 per eliminare zone: ")

            s.send(str(scelta2).encode())

            if scelta2 == "1":
                nome = input("Inserisci il nome del dipendente da inserire: ")
                s.send(nome.encode())
                cognome = input("Inserisci il cognome del dipendente da inserire: ")
                s.send(cognome.encode())
                posizione_lavoro = input("Inserisci dove lavora il dipendente da inserire: ")
                s.send(posizione_lavoro.encode())
                data_assunzione = input("Inserisci la data di assunzione del dipendente da inserire: ")
                s.send(data_assunzione.encode())
                stipendio = input("Inserisci lo stipendio del dipendente da inserire: ")
                s.send(stipendio.encode())
                eta = input("Inserisci l'eta del dipendente da inserire: ")
                s.send(eta.encode())

            else:
                #stesso codice del dipendente ma con le variabili delle zone
                print("")

        if scelta == "4":
            id_modifica = input("Inserisci l'id del dipendente di cui vuoi modificare i dati: ")
            s.send(id_modifica.encode())
            nome = input("Inserisci il nuovo nome del dipendente oppure lo stesso nome se non cambia: ")
            s.send(nome.encode())
            cognome = input("Inserisci il nuovo cognome del dipendente oppure lo stesso se non cambia: ")
            s.send(cognome.encode())
            posizione_lavoro = input("Inserisci il nuovo luogo dove lavora il dipendente oppure lo stesso se non cambia: ")
            s.send(posizione_lavoro.encode())
            data_assunzione = input("Inserisci la nuova data di assunzione del dipendente oppure la stessa se non cambia: ")
            s.send(data_assunzione.encode())
            stipendio = input("Inserisci il nuovo stipendio del dipendente oppure lo stesso se non cambia: ")
            s.send(stipendio.encode())
            eta = input("Inserisci l'eta del dipendente oppure la stessa se non cambia: ")
            s.send(eta.encode())
        
else:
    print("Tentativi massimi raggiunti. Chiudo la connessione.")

s.close()
