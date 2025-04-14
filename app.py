import random

def generador_password(longitud):

    password = "" 


    contra_usuario =("+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")

    for i in range (longitud):
        password += random.choice(contra_usuario)
    return password

























