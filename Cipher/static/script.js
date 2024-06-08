function switchSection() {
    var encryptSection = document.getElementById('encrypt-section');
    var decryptSection = document.getElementById('decrypt-section');
    
    if (encryptSection.style.display === 'none') {
        encryptSection.style.display = 'block';
        decryptSection.style.display = 'none';
        document.getElementById('ciphertext').value = '';
        document.getElementById('plaintext').value = '';
    } else {
        encryptSection.style.display = 'none';
        decryptSection.style.display = 'block';
        document.getElementById('ciphertext-dec').value = '';
        document.getElementById('plaintext-dec').value = '';
    }
}

function encrypt() {
    var plaintext = document.getElementById('plaintext').value;
    
    fetch('/encrypt', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: 'plaintext=' + encodeURIComponent(plaintext)
    })
    .then(response => response.text())
    .then(ciphertext => {
        document.getElementById('ciphertext').value = ciphertext;
    })
    .catch(error => console.error('Error:', error));
}

function decrypt() {
    var ciphertext = document.getElementById('ciphertext-dec').value;
    
    fetch('/decrypt', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: 'ciphertext=' + encodeURIComponent(ciphertext)
    })
    .then(response => response.text())
    .then(plaintext => {
        document.getElementById('plaintext-dec').value = plaintext;
    })
    .catch(error => console.error('Error:', error));
}