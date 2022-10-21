from numpy import asarray
from PIL import Image

def from_str_to_bin(message):
    bin_msg = ""
    for char in message:
        bin_char = ord(char)
        bin_char = bin(bin_char)[2:]
        while len(bin_char) < 8:
            bin_char = "0" + bin_char
        bin_msg+=bin_char
    return bin_msg


def change_img_data(msg, data):
    it = 0
    #li = ligne, col = colones, rgb = [r, g ,b ,a]
    for li in range(len(data)):
        for col in range (len(data[li])):
            for rgb in range(len(data[li][col])):
                #Arret quand l'itérateur dépace la taille de notre message
                if it >= len(msg):
                    return data
                    
                bin_rgb = bin(data[li][col][rgb])[2:]
                list_bin = list(bin_rgb)
                #On écrit sur le dernier bit de la couleur le bit de notre msg
                list_bin[-1] = msg[it]
                rst = int("".join(list_bin),2)
                data[li][col][rgb] = rst
                it += 1


def enc(msg, img_path):
    #Récupération des données de l'image
    image = Image.open(img_path)
    img_data = asarray(image).copy()
    

    # Test de la longueur du message (en binaire donc *8).
    # Si elle excède la taille de l'image divisée par 4
    # 4bits du message sont codé sur 1pixel (un bit par couleur +1 alpha)
    # Alors le message ne peut être encodé dans l'image
    if len(msg)*8 > len(img_data)*len(img_data[0])/4:
        print("msg too long")
        return
    

    # Convertion du message en binaire
    bin_msg = from_str_to_bin(msg)
    print("message bin = ", bin_msg)


    # Ecriture de la taille du message sur 3 octet pour la décription
    # La taille sur 3octet permet une taille max de 16 millions de bits
    # Soit une image de 16M/3 = 5.5M pixels
    msg_taille = bin(len(bin_msg))[2:]
    while len(msg_taille) < 24:
        msg_taille = "0" + msg_taille
    print("message size = ",msg_taille)


    # Creation du message complet à écrire 
    enc_msg = msg_taille + bin_msg
    print("final message = ",enc_msg)



    #Ecriture du message & de la taille dans l'image
    change_img_data(enc_msg, img_data)

    #Sauvegarde de limage dans le dossier outputs
    new_image = Image.fromarray(img_data)
    new_image.save("outputs/image_enc.png")


            
#MAIN
enc("coucou", "inputs/image.png")