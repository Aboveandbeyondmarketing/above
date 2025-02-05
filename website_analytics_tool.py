import os

# Debugging
print("Current Directory:", os.getcwd())  
print("Templates Folder Exists:", os.path.exists("templates"))
print("Templates Directory Contents:", os.listdir("templates") if os.path.exists("templates") else "Not Found")
