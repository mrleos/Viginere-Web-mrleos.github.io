from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Fungsi enkripsi Vigenere
def vigenere_encrypt(plaintext, key):
    ciphertext = ""
    key = key.upper()
    key_length = len(key)
    key_index = 0

    for char in plaintext:
        if char.isalpha():
            shift = ord(key[key_index]) - ord('A')
            if char.isupper():
                encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            ciphertext += encrypted_char
            key_index = (key_index + 1) % key_length
        else:
            ciphertext += char

    return ciphertext

# Fungsi dekripsi Vigenere
def vigenere_decrypt(ciphertext, key):
    plaintext = ""
    key = key.upper()
    key_length = len(key)
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index]) - ord('A')
            if char.isupper():
                decrypted_char = chr((ord(char) - ord('A') - shift + 26) % 26 + ord('A'))
            else:
                decrypted_char = chr((ord(char) - ord('a') - shift + 26) % 26 + ord('a'))
            plaintext += decrypted_char
            key_index = (key_index + 1) % key_length
        else:
            plaintext += char

    return plaintext

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    data = request.json
    plaintext = data['plaintext']
    key = data['key']
    ciphertext = vigenere_encrypt(plaintext, key)
    return jsonify({'ciphertext': ciphertext})

@app.route('/decrypt', methods=['POST'])
def decrypt():
    data = request.json
    ciphertext = data['ciphertext']
    key = data['key']
    decrypted_text = vigenere_decrypt(ciphertext, key)
    return jsonify({'decrypted_text': decrypted_text})

if __name__ == '__main__':
    app.run(debug=True)
