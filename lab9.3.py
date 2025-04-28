def create_array(a,b,c,n):
    array=[]
    
    for i in range(a):
        layer=[]

        for j in range(b):
            row=[]
            
            for k in range(c):
                row.append(n)
                
            layer.append(row)


        array.append(layer)
    print(array )
      
    return array

create_array(3,4,5,7)
    
