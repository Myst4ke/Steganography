import sys
from enc_file import dec_file, enc_file
from enc_message import enc_msg, dec_msg


def print_args():
    print("Arguments supplied : ")
    for i, arg in enumerate(sys.argv):
        print(f"Argument {i:>6}: {arg}")


# Vérifie que seul 3 arguments sont fournis et renvoie les 2 derniers
def args_check():
    if len(sys.argv) == 4:
        return(sys.argv[1], sys.argv[2], sys.argv[3])
    elif len(sys.argv) == 3:
        return(sys.argv[1], sys.argv[2])
    elif len(sys.argv) == 5 and sys.argv[3] == "-o":
        return(sys.argv[1], sys.argv[2], sys.argv[4])
    elif len(sys.argv) == 6 and sys.argv[4] == "-o":
        return(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[5])
    elif len(sys.argv) == 2 and sys.argv[1] == "help":
        print("Help :\n")
        print("The functions are :\n")
        print("<enc-message> to encrypt the following message")
        print("<enc-file> to encrypt the file at following location")
        print("<dec-message> to decrypt the following image and print the result")
        print("<dec-file> to decrypt the following image and write the result in a file")
        sys.exit(0)
    else:
        print("Error : the numbers of arguments is either too low or too high !")
        print("Usage : python3 enc_image.py <function> <\"message\" or filename> <imagename>")
        print("You can use the 'help' command for more information")
        print_args()
        exit(0)


def main():
    args = args_check()
    match args[0]:
        case "enc-message":
            if len(args)==4:
                print("Message encryption ...")
                enc_msg(args[1], args[2], args[3])
            else:
                print("Message encryption ...")
                enc_msg(args[1], args[2], "image_enc.png")
        case "enc-file":
            if len(args)==4:
                print("File encryption ...")
                enc_file(args[1], args[2], args[3])
            else:
                print("File encryption ...")
                enc_file(args[1], args[2], "image_enc.png")
        case "dec-message":
            print("Message decryption ...")
            print("Message is :",dec_msg(args[1]))
        case "dec-file":
            if len(args)==3:
                print("File decryption ...")
                dec_file(args[1], args[2])
            else:
                print("File decryption ...")
                dec_file(args[1], "result.txt")
        case _ :
            print("The function that you supplied is either misswritten or doesn't exit")
            return 0

if __name__ == "__main__":
    main()
