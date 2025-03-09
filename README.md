# Cryptography

This repository contains implementations of various cryptographic algorithms and techniques.

## Caesar Cipher

The Caesar Cipher is a simple substitution cipher where each letter in the plaintext is shifted a certain number of positions down the alphabet. For example, with a shift of 3, 'A' would become 'D', 'B' would become 'E', and so on.

### How it works

1.  Choose a shift value (e.g., 3).
2.  For each letter in the plaintext, replace it with the letter that is the shift value positions down the alphabet.
3.  Wrap around the alphabet if necessary (e.g., if shifting 'X' by 3, it would become 'A').

### Example

*   Plaintext: `ATTACKATONCE`
*   Shift: 4
*   Ciphertext: `EXXEGOEXSRGI`

### Implementation

The Caesar Cipher is implemented in Python in the file `CeaserChipher.py`.  It includes both encryption and decryption functions.
