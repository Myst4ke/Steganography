# Steganography
### Pré-requis :
Installation des librairies
* `PIL` Pour gérer les Images : `pip3 install Pillow`
* `numpy` Pour convertir les données de l'image en tableau : `pip3 install numpy`

### Compilation :
Le fichier pris en entrée **doit être dans le dossier** `/inputs`. 
L'image qui en résulte, elle, se trouve dans le dossier `/outputs`.

L'image que l'on veut lire doit rester dans `/outputs`.

On peut compiler grace à `python3 main.py` suivit d'une des commandes.

**Les différentes commandes :**
* `enc-message` : Ecrit les données du message qui suit dans l'image fournie.
* **Ex :** `enc-message "coucou !" image.png`

* `enc-file` Ecrit les données du fichier qui suit dans l'image fournie.
* **Ex :** `enc-file test.txt image.png`

* `dec-message` Lit les données contenues dans l'image et les affiche.
* **Ex :** `dec-message image_enc.png`

* `dec-file` Lit les données contenues dans l'image et les écrit dans un fichier.
* **Ex :** `dec-file image_enc.png`

* `help` liste les différentes commandes et comment les utiliser

Toutes les commandes supportent le `-o` pour spécifier le nom de fichier de sortie. (seul `dec-message` ne l'utilise pas)

---

### Road Map
- [x] Ecriture de message 
- [x] Lecture de message
- [x] Arguments en ligne de commande
- [x] Ecriture de fichiers
- [x] Lecture de fichiers
- [ ] Lecture & Ecriture dans une vidéo

---

### Fonctions :
Chiffrement
* `from_str_to_bin(message)` : Convertit une string en binaire caractère par caractère (grâce au code ascii).
* `change_img_data(msg, data)` : Ecrit les données du message bit par bit dans le RGBA de chaque pixel (4bits par pixel).

Déchiffrement
* `get_msg_size(data)` : Récupère les 24 premiers bits encodé dans l'image (taille max du message).
* `delete_start(data)` : Enlève les 24 premiers bits dans le message (taille max de la clé)
* `get_img_data(data, size)` : Récupère le message bit a bit encodé dans l'image grâce à la taille.
* `from_bin_to_str(message)` : Convertit un binaire en string

---
### Sources :
* Vidéo explicative de la Stéganographie [Dissimuler de l'information grâce à la stéganographie](https://www.youtube.com/watch?v=uGmQcJAI0g0).
* [Python Command Line Arguments](https://realpython.com/python-command-line-arguments/) : Permet d'afficher tous les arguments dans la ligne de commande.
```py
import sys

if __name__ == "__main__":
    print(f"Arguments count: {len(sys.argv)}")
    for i, arg in enumerate(sys.argv):
        print(f"Argument {i:>6}: {arg}")
```
* [Basic Markdown Syntax](https://www.markdownguide.org/basic-syntax/).
* [Python String join() Method](https://www.w3schools.com/python/ref_string_join.asp).

 



