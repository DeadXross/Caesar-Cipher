from flask import Flask, request, render_template
import base64
import hashlib

app = Flask(__name__)

KEY = b'My5up3rC0mpl3xK3y!@#$%^'
base64_chars = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890+/=']


def convert(string, type):
    hash = hashlib.sha512(KEY).hexdigest()

    cipher = base64_chars[:]

    for c in hash:
        char_int = int(c, 16)
        pos = 65 * (char_int / 15)

        cipher.insert(0, cipher.pop(int(pos) - 1))
        cipher = cipher[::-1]

    sbox = {}

    for i, c in enumerate(base64_chars):
        sbox[c] = cipher[i]

    if type == 'd':
        sbox = dict((v, k) for k, v in sbox.items())

    for i, c in enumerate(string):
        string[i] = sbox[c]

    return ''.join(string)


def encrypt(string):
    string = [c for c in base64.b64encode(string.encode()).decode()]

    return convert(string, 'e')


def decrypt(string):
    string = [c for c in string.strip()]

    return base64.b64decode(convert(string, 'd')).decode()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/encrypt', methods=['POST'])
def encrypt_route():
    plaintext = request.form['plaintext']
    ciphertext = encrypt(plaintext)
    return ciphertext


@app.route('/decrypt', methods=['POST'])
def decrypt_route():
    ciphertext = request.form['ciphertext']
    plaintext = decrypt(ciphertext)
    return plaintext


if __name__ == '__main__':
    app.run()