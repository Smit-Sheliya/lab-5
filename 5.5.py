def upperCase_list(lst):
    
    for string in lst:
        newstring=""
        
        for ch in string:

            if "a"<=ch<="z":
                newstring+=chr(ord(ch)-32)
                
            else:
                newstring+=ch

        lst[lst.index(string)]=newstring        

            
lst=["smit","pravinbhai","sheliya"]
upperCase_list(lst)
print(lst)
