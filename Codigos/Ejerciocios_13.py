def create_file(file_name, content=None):
      
        
    if content:
       mode = "w"
    else:
       mode ="x"
       
    file = open(file_name, mode) 
    
    
    if content:
       file.write(content)
       
    file.close()
  



def modify_file(file_name, content, overwrite=False):

    mode = "w" if overwrite else "a"
    
    file = open(file_name, mode)
    file.write(content)
    file.close
    
    
modify_file("benji1.txt", "Contenido nuevo",  overwrite=True )
create_file("sample1:txt", "contenidi del archivo hola como estas")


#  mode = "w" if content else "x"  este es otra forma mas sencillo 

     
    
    
    #if content:
       #file = open(file_name, "w")
    #else:
       #file = open(file_name, "x")
    
    
    
    
    
# def modify_file(file_name, content, overwrite=False)