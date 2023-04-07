def any_duplicates(square):
    c= [i for x in square for i in x ]
    a = {1,2,3,4,5,6,7,8,9}
    return set(c)!= a  
        