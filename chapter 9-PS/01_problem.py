f = open("poem.txt")
content = f.read()

if("Twinkle" in content):
    print("Twinkle is present in the content.")

f.close()
