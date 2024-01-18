import socket
import math

HOST = "challenge01.root-me.org"  # L'addresse du serveur
PORT = 52002  # Le port utilisé par le serveur


def recevoir_challenge(connection: socket.socket) -> str:
    connection.connect((HOST, PORT))
    # retourne le défi en chaine de charactère (`str`)
    return connection.recv(1024).decode()


def envoyer_resultat(connection: socket.socket, resultat: float) -> str:
    """
    Envoie le résultat et retourne la réponse du serveur.
    Si la réponse est bonne, elle contient un mot de passe
    pour valider le challenge.
    """
    connection.send(f"{resultat}\n".encode())
    return connection.recv(1024).decode()


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as connection:
    text = recevoir_challenge(connection)
    mot_de_passe = envoyer_resultat(connection, 1.0)
    print(mot_de_passe)
