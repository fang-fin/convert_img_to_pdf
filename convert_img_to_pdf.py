import sys
import os
import img2pdf    



def convert_image_from_file(files):
    # if len(files) == 0:
    #     return None
    
    pdf_file_name =  os.path.basename(files[0])
    
    with open("{name}.pdf".format(name=pdf_file_name),"wb") as pdf_file :
        pdf_file.write(img2pdf.convert(files))
    



if __name__ == "__main__" :
    if len(sys.argv) < 2:
        print("Usage: python convert_img_to_pdf <file1.jpg> <file2.jpg> <file3.jpg> ....")
        sys.exit(1)
    
    convert_image_from_file(sys.argv[1:])
    # print(len(sys.argv[1:])
    