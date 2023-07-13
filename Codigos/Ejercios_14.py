def modify_file(file_name, content, overwrite=False):

    mode = "w" if overwrite else "a"
    
    file = open(file_name, mode)
    file.write(content)
    file.close
    
    
modify_file("benji1.txt", "Contenido nuevo",  overwrite=True )
