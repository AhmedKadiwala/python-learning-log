# st = "\nHey ahmed you are fantastic." # string creation
# f = open("writefile.txt" , "a")      # "a" is used to open or create file in append mode  
# f.write(st)                          # write the given string "st" in f.
# f.close()                            # close the file.


#using with statement 
st = "\nAhmed you suck."
with open("writefile.txt", "a") as f:
    f.write(st)
