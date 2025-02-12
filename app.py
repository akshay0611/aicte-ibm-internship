from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import cv2
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encode', methods=['POST'])
def encode():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)
        msg = request.form['message'] + '\0'  
        img = cv2.imread(filename)
        d = {chr(i): i for i in range(255)}
        m, n, z = 0, 0, 0
        for i in range(len(msg)):
            img[n, m, z] = d[msg[i]]
            n, m = n + 1, m + 1
            z = (z + 1) % 3
        encrypted_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'encryptedImage.png')
        cv2.imwrite(encrypted_filename, img)
        return send_from_directory(app.config['UPLOAD_FOLDER'], 'encryptedImage.png', as_attachment=True)
    return redirect(request.url)

@app.route('/decode', methods=['POST'])
def decode():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)
        img = cv2.imread(filename)
        c = {i: chr(i) for i in range(255)}
        m, n, z = 0, 0, 0
        message = ""
        while True:
            try:
                char = c[img[n, m, z]]
                if char == '\0':  
                    break
                message += char
                n, m = n + 1, m + 1
                z = (z + 1) % 3
            except IndexError:
                break
        return f"Decryption message: {message}"
    return redirect(request.url)

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)