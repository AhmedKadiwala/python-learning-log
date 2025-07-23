f = open("file.txt")
data = f.read()
print(data)
f.close()




# import PyPDF2

# # Open the PDF in binary mode
# with open("C:/Users/Ahmed Kadiwala/Desktop/resume(2.0.2).pdf", "rb") as file:
#     reader = PyPDF2.PdfReader(file)
    
#     # Extract text from all pages
#     for i, page in enumerate(reader.pages):
#         text = page.extract_text()
#         print(f"Page {i + 1}:\n{text}\n")
