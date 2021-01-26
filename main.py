import unittest
import cipher

class TestCipherMethods(unittest.TestCase):

    def test_caeser(self):
        c = cipher.Caeser()


        for i in range(0, 100):
            c.k = i

            original = "Hello, world!"
            encrypted = c.encrypt(original)

            self.assertEqual(original, c.decrypt(encrypted))

    def test_vigenere(self):
        c = cipher.Vigenere()

        c.k = "PASSPHRASE"

        original = "Hello, world!"
        encrypted = c.encrypt(original)

        self.assertEqual(original, c.decrypt(encrypted))

unittest.main()