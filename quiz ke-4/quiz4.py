a = [ [1, 1, 1, 1 ],  
    [ 1, 2, 3, 4 ],  
    [ 1, 3, 6, 10 ],  
    [ 1, 4, 10, 20 ] ]  
          
for i in range(len(a)) :  
    for j in range(len(a[i])) :  
        print(a[i][j], end=" ") 
    print()     