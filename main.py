from numpy import asarray
from PIL import Image
maxMsgSize = 24

# Convertion d'un string vers un binaire
def from_str_to_bin(message):
    bin_msg = ""
    for char in message:
        bin_char = ord(char)
        bin_char = bin(bin_char)[2:]
        while len(bin_char) < 8:
            bin_char = "0" + bin_char
        bin_msg+=bin_char
    return bin_msg

# Modification des données de l'image pixel par pixel
def change_img_data(msg, data):
    it = 0
    for li in range(len(data)):
        for col in range (len(data[li])):
            for rgb in range(len(data[li][col])):
                if it >= len(msg):
                    return data
                bin_rgb = bin(data[li][col][rgb])[2:]
                list_bin = list(bin_rgb)
                list_bin[-1] = msg[it]
                rst = int("".join(list_bin),2)
                data[li][col][rgb] = rst
                it += 1

# Ecriture des données (msg) dans l'image -> création d'une nouvelle image
def enc_msg(msg, img_path):
    #Récupération des données de l'image
    image = Image.open(img_path)
    img_data = asarray(image).copy()

    # Test de la longueur du message 
    if len(msg)*8 > len(img_data)*len(img_data[0])*4:
        print("msg too long !")
        return
    
    # Convertion du message en binaire
    print("message to encrypt is :", msg)
    bin_msg = from_str_to_bin(msg)
    print("message in bin is :", bin_msg)

    # Ecriture de la taille du message
    print("message length is :",len(bin_msg),"bits")
    msg_taille = bin(len(bin_msg))[2:]
    while len(msg_taille) < maxMsgSize:
        msg_taille = "0" + msg_taille

    # Création du message complet à écrire 
    final_msg = msg_taille + bin_msg

    #Ecriture du message & de la taille dans l'image
    change_img_data(final_msg, img_data)

    #Sauvegarde de l'image dans le dossier outputs
    new_image = Image.fromarray(img_data)
    new_image.save("outputs/image_enc.png")



# Récupère les 24 premiers bits encodés dans l'image -> déduit la taille du message
def get_msg_size(data):
    it = 0
    size = []
    for li in range(len(data)):
        for col in range (len(data[li])):
            for rgb in range(len(data[li][col])):
                if it >= maxMsgSize:
                    rst = int("".join(size),2)
                    return rst
                bin_rgb = bin(data[li][col][rgb])[2:]
                list_bin = list(bin_rgb)
                size.append(list_bin[-1])
                it += 1

# Enlève les 24 premiers bits de l'entrée
def delete_start(data):
    del data[:maxMsgSize]
    return data

# Récupère les données dans l'image jusqu'à taille msg + maxMsgSize (24b)
def get_img_data(data, size):
    it = 0
    message = []
    size = size + maxMsgSize
    for li in range(len(data)):
        for col in range (len(data[li])):
            for rgb in range(len(data[li][col])):
                if it >= size:
                    message = delete_start(message)
                    message = "".join(message)
                    return message
                bin_rgb = bin(data[li][col][rgb])[2:]
                list_bin = list(bin_rgb)
                message.append(list_bin[-1])
                it += 1

# Convertion d'un binaire vers un string
def from_bin_to_str(message):
    rst = []
    for i in range(len(message)//8):
        rst.append(message[i*8:(i+1)*8])

    final_message = ""
    for i in range(len(rst)):
        final_message += chr(int(rst[i],2))
    return final_message

# Extraction des données dans l'image -> message final
def dec_msg(img_path):
    #Récupération des données de l'image
    image = Image.open(img_path)
    img_data = asarray(image).copy() 

    #Récupération de la taille du message
    msgSize = get_msg_size(img_data)
    print("Message size found : ",msgSize,"bits")

    #Lecture du message
    message = get_img_data(img_data, msgSize)

    final_message = from_bin_to_str(message)
    print("Message is : ",final_message,)



#MAIN
print("Encryption : ")
enc_msg("coucou", "inputs/image.png")

print("\nDécryption : ")
dec_msg("outputs/image_enc.png")