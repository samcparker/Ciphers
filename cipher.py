import abc

class Cipher(metaclass=abc.ABCMeta):
    """Cipher super class, contains abstract methods for encrypting and decrypting
    and methods to set and retrieve keys."""

    def __init__(self):
        self._lower = "abcdefghijklmnopqrstuvwxyz"
        self._upper = list(self._lower.upper())
        self._lower = list(self._lower)

    @property
    def k(self):
        return self._k

    @k.setter
    def k(self, k):
        self._k = k


    @abc.abstractmethod
    def encrypt(self, plaintext):
        """Encrypt plaintext"""
        

    @abc.abstractmethod
    def decrypt(self, cipher):
        """Decrypt cipher"""

class Vigenere(Cipher):
    """Vigenere cipher class.
    
    The Vigenere cipher is similar to the Caeser cipher, however uses different
    values for the key at each letter based on a repeating key phrase.
    """

    def __init__(self):
        super().__init__()
        self._k = "KEY"
    

    def encrypt(self, plaintext):
        key = self._k.lower()

        k_sequence = []
        for i in range(0, len(key)):
            k_sequence.append(self._lower.index(key[i]))
        
        cipher = ""
        for i in range(0, len(plaintext)):
            letter = plaintext[i]

            if letter in self._lower:
                alphabet = self._lower
            elif letter in self._upper:
                alphabet = self._upper
            else:
                cipher += letter
                continue

            p = alphabet.index(letter)


            c = (p + k_sequence[i % len(k_sequence)]) % 26
            cipher += alphabet[c]

        return cipher

    def decrypt(self, cipher):
        key = self._k.lower()

        k_sequence = []
        for i in range(0, len(key)):
            k_sequence.append(self._lower.index(key[i]))
        
        plaintext = ""
        for i in range(0, len(cipher)):
            letter = cipher[i]

            if letter in self._lower:
                alphabet = self._lower
            elif letter in self._upper:
                alphabet = self._upper
            else:
                plaintext += letter
                continue

            p = alphabet.index(letter)


            c = (p - k_sequence[i % len(k_sequence)]) % 26
            plaintext += alphabet[c]

        return plaintext

class Caeser(Cipher):
    """Caeser cipher class.

    Shifts each character to the right by the key and same in reverse to decrypt.
    """

    def __init__(self):
        super().__init__()
        self._k = 3

      
    def encrypt(self, plaintext):
        cipher = ""
        for i in range(0, len(plaintext)):
            letter = plaintext[i]

            if letter in self._lower:
                alphabet = self._lower
            elif letter in self._upper:
                alphabet = self._upper
            else:
                cipher += letter
                continue

            p = alphabet.index(letter)


            c = (p + self._k) % 26
            cipher += alphabet[c]

        return cipher


    def decrypt(self, cipher):
        self._k = -self._k
        plaintext = self.encrypt(cipher)
        self._k = -self._k

        return plaintext