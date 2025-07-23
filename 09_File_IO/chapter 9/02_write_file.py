st = "Hey ahmed you are fantastic." # string creation
f = open("writefile.txt" , "w")     # "w" is used to open or create file in write mode 
f.write(st)                         # write the given string "st" in f.
f.close()                           # close the file.