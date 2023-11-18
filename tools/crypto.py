from cryptography.fernet import Fernet

def crypting_pass(contra):
    """Esta es una funcion que permite generar la encriptacion de los pass
    resibe la contra y devuelve la encriptacion
    """
    #Generar una clave de encriptacion
    f= Fernet(b'ZdBDHMopkW1IOg9LXL3MHdx4Thw30kTnW3KsFnV4jJ4=')
    #convertir a bytes
    b_pass= bytes(contra,'ascii')
    #Encriptar la contra
    encrip_contra=f.encrypt(b_pass)
    #Devolver la encriptacion en ascii
    return encrip_contra.decode('ascii')

def uncrypting_pass(contra):
    f= Fernet(b'ZdBDHMopkW1IOg9LXL3MHdx4Thw30kTnW3KsFnV4jJ4=')
    #convertir a bytes
    b_pass= bytes(contra,'ascii')
    #Desencriptar la contra
    encrip_contra=f.decrypt(b_pass)
    #Devolver la encriptacion en ascii,porque devuelve en binario
    return encrip_contra.decode('ascii')