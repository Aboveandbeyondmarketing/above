import os

@app.route('/')
def home():
    print("Current Directory:", os.getcwd())  
    print("Templates Folder Exists:", os.path.exists("templates"))
    print("Templates Directory Contents:", os.listdir("templates") if os.path.exists("templates") else "Not Found")
    
    return render_template('index.html')
