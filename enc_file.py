from enc_message import enc_msg, dec_msg


def enc_file(filename, image_name, enc_img_path):
    file=open("inputs/"+filename,"rb")
    byte = file.read()
    file.close
    rst = ""
    for char in byte: 
        rst += (chr(char))
    enc_msg(rst, image_name, enc_img_path)

def dec_file(image_name, outputfile):
    msg = dec_msg(image_name)
    file=open("outputs/"+outputfile, "w+")
    print("New decypted file created, can be found at : outputs/"+outputfile)
    file.write(msg)

