# Steganography
### Pré-requis :
Installation des librairies
* `PIL` Pour gérer les Images : `pip3 install Pillow`
* `numpy` Pour convertir les données de l'image en tableau : `pip3 install numpy`

### Fonctions :
Chiffrement
* `from_str_to_bin(message)` : Convertit une string en binaire caractère par caractère (grâce au code ascii).
* `change_img_data(msg, data)` : Ecrit les données du message bit par bit dans le RGBA de chaque pixel (4bits par pixel).

Déchiffrement
* `get_msg_size(data)` : Récupère les 24 premiers bits encodé dans l'image (taille max du message).
* `get_img_data(data, size)` : Récupère le message bit a bit encodé dans l'image grâce à la taille.
* `delete_start(data)` : Enlève les 24 premiers bits dans le message (taille max de la clé)



