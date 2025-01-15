import sys
import os
import img2pdf    



def convert_image_from_file(files):
    pdf_file_name =  os.path.basename(files[0])
    
    with open("{name}.pdf".format(name=pdf_file_name),"wb") as pdf_file :
        pdf_file.write(img2pdf.convert(files))
    return



if __name__ == "__main__" :
    if len(sys.argv)< 1:
        print("Usage: python convert_img_to_pdf <file1> <file2> <file3> ....")
    
    convert_image_from_file(sys.argv[1:])
    print(len(sys.argv[1:]))
    