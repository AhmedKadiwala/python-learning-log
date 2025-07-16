post = input("Enter message here:")
word = "Harry"
if(word.lower() in post.lower()):
    print("Post contains harry.")
else:
    print("Harry is not mentioned in post.")