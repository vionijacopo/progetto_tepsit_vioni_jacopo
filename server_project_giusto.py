import socket
import mysql.connector

# Password autorizzata
PASSWORD = "tepsit"

def db_get_dipendenti(parametri):
    conn = mysql.connector.connect(
        host="10.10.0.10",
        user="jacopo_vioni",
        password="vioni1234",
        database="5BTepsit",
        port=3306
    )

    cur = conn.cursor()

    clausole = ""
    for key, value in parametri.items():
        clausole += f"and {key} = '{value}' "

    query = f"SELECT * FROM dipendenti_jacopo_vioni where 1=1 {clausole}"
    cur.execute(query)
    dati = cur.fetchall()
    return dati

def db_get_zone(parametri):
    conn = mysql.connector.connect(
        host="10.10.0.10",
        user="jacopo_vioni",
        password="vioni1234",
        database="5BTepsit",
        port=3306
    )

    cur = conn.cursor()

    clausole = ""
    for key, value in parametri.items():
        clausole += f"and {key} = '{value}' "

    query = f"SELECT * FROM zona_di_lavoro_jacopo_vioni where 1=1 {clausole}"
    cur.execute(query)
    dati = cur.fetchall()
    return dati

def db_elimina_dipendente(parametri):
    conn=mysql.connector.connect(
        host="10.10.0.10",
        user="jacopo_vioni",
        password="vioni1234",
        database="5BTepsit",
        port=3306
    )
    
    cur = conn.cursor()
    
    clausole = ""
    for key, value in parametri.items():
        clausole += f"and {key} = '{value}' "
    
    query = f"DELETE FROM dipendenti_jacopo_vioni where 1=1 {clausole}"
    cur.execute(query)
    conn.commit()

def db_elimina_zona(parametri):
    conn=mysql.connector.connect(
        host="10.10.0.10",
        user="jacopo_vioni",
        password="vioni1234",
        database="5BTepsit",
        port=3306
    )
    
    cur = conn.cursor()
    
    clausole = ""
    for key, value in parametri.items():
        clausole += f"and {key} = '{value}' "
    
    query = f"DELETE FROM zona_di_lavoro_jacopo_vioni where 1=1 {clausole}"
    cur.execute(query)
    conn.commit()

def db_inserisci(parametri):
    conn=mysql.connector.connect(
        host="10.10.0.10",
        user="jacopo_vioni",
        password="vioni1234",
        database="5BTepsit",
        port=3306
    )
    
    cur = conn.cursor()
    
    query = f"INSERT INTO dipendenti_jacopo_vioni (nome, cognome, posizionelavorativa, dataassunzione, eta, stipendioxmese) VALUES ('{nome}','{cognome}','{posizione_lavoro}','{data_assunzione}','{eta}','{stipendio}')"
    cur.execute(query)
    conn.commit()

def db_modifica(par):
    
    conn=mysql.connector.connect(
        host="10.10.0.10",
        user="jacopo_vioni",
        password="vioni1234",
        database="5BTepsit",
        port=3306
    )
    cur = conn.cursor()
    query = f"UPDATE dipendenti_jacopo_vioni SET nome = '{nome}', cognome = '{cognome}', posizionelavorativa = '{posizione_lavoro}', dataassunzione = '{data_assunzione}', eta = '{eta}', stipendioxmese = '{stipendio}' WHERE id= '{id_modifica}'"
    cur.execute(query)
    conn.commit()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost", 50007))
s.listen()

print("In attesa di connessioni...")

conn, addr = s.accept()
print('Connected by', addr)

i = 0
while i < 3:
    password = conn.recv(1024).decode()
    if password == PASSWORD:
        conn.send("Password corretta. Inizia la comunicazione".encode())
        break
    else:
        i += 1
        tentativi_rimasti = 3 - i
        if i < 3:
            conn.send(f"Errore: Password sbagliata. Tentativi rimasti: {tentativi_rimasti}".encode())
        else:
            conn.send("Tentativi massimi raggiunti. Chiudo la connessione".encode())
            conn.close()
            exit()

while True:
    data = conn.recv(1024).decode()
    if not data:
        break  # Connessione chiusa dal client
    if data == "5":
        break  # Termina il server

    if data == "1":
        
        scelta = conn.recv(1024).decode()
        if scelta == "1":
            nome = conn.recv(1024).decode()
            par = {"nome": nome}
            result = db_get_dipendenti(par)
            conn.send(str(result).encode())
        
        else:
            nome = conn.recv(1024).decode()
            par = {"nome": nome}
            result = db_get_zone(par)
            conn.send(str(result).encode())
    
    elif data == "2":

        scelta = conn.recv(1024).decode()
        if scelta == "1":
            id_elimina = conn.recv(1024).decode()
            par = {"id": id_elimina}
            db_elimina_dipendente(par)
        
        else:
            id_elimina = conn.recv(1024).decode()
            par = {"idzona": id_elimina}
            db_elimina_zona(par)
        
    
    elif data == "3":
        nome = conn.recv(1024).decode()
        cognome = conn.recv(1024).decode()
        posizione_lavoro = conn.recv(1024).decode()
        data_assunzione = conn.recv(1024).decode()
        stipendio = conn.recv(1024).decode()
        eta = conn.recv(1024).decode()
        
        par = {"nome": nome, "cognome": cognome, "posizionelavorativa": posizione_lavoro, "dataassunzione": data_assunzione, "eta": eta, "stipendioxmese": stipendio}
        
        db_inserisci(par)

    elif data == "4":
        id_modifica = conn.recv(1024).decode()
        nome = conn.recv(1024).decode()
        cognome = conn.recv(1024).decode()
        posizione_lavoro = conn.recv(1024).decode()
        data_assunzione = conn.recv(1024).decode()
        stipendio = conn.recv(1024).decode()
        eta = conn.recv(1024).decode()
        par = {"id": id_modifica, "nome": nome, "cognome": cognome, "posizionelavorativa": posizione_lavoro, "dataassunzione": data_assunzione, "eta": eta, "stipendioxmese": stipendio}
        db_modifica(par)

conn.close()
