from shuffler import Shuffle


# from AlgorithmProject import shuffler


class Encoding:
    cipher = {}
    charSize = 2

    def __init__(self):
        # Assuming less than 100 characters, to always take 2 digit values for encoded letters
        self.asciitoNum(32, 127)

    def asciitoNum(self, start, end, count=100):
        count = 10 ** self.charSize
        for i in range(start, end):
            key = str(count)
            key = key[1:]
            self.cipher[key] = chr(i)
            count += 1

        # Include newline
        key = str(count)
        key = key[1:]
        self.cipher[key] = chr(10)

    def decode(self, c, combination):
        l = len(c)
        i = 0
        r = ""
        while i < l:
            d = c[i:i + self.charSize]
            r += combination[d]
            i += self.charSize

        return r

    def encode(self, message, combination):
        r = ""
        for c in message:
            for x in combination:
                if combination[x] == c:
                    r += x
        return r


class Encrypting:
    key = "29100107563126386110270218232633044045320933080956364007560849105921553322275604"

    # Message -> encode (to numbers) -> encrypt (to scrambled string)
    def demo(self, message, cipher, newCipher):
        trans = Encoding()
        encodedMessage = trans.encode(message, cipher)
        print("Default encoded Message = ", encodedMessage)

        encodedMessage = trans.encode(message, newCipher)
        print("New encoded = ", encodedMessage)

        encryptedMessage = trans.decode(encodedMessage, cipher)
        print("Encrypted Message = ", encryptedMessage)

        decryptedMessage = trans.decode(encodedMessage, newCipher)
        print("Decrypted Message = ", decryptedMessage)

    def askCredentials(self):
        message = input("Enter your message")
        pw = input("Password: ")

        return message, pw

    def passwordDemo(self, message, pw):
        # Need a sample key because most user keys will be too short
        key = self.key
        trans = Encoding()
        deck = Shuffle()
        print(trans.cipher)
        pwe = trans.encode(pw, trans.cipher)
        secretKey = pwe + key
        newCipher = deck.fixShuffle(trans.cipher, secretKey, trans.charSize)

        print(newCipher)

        self.demo(message, trans.cipher, newCipher)

    def caesarDemo(self, message, pw):
        trans = Encoding()
        deck = Shuffle()
        print(trans.cipher)

        pw = int(pw)

        newCipher = deck.slide(trans.cipher, pw)
        print(newCipher)

        self.demo(message, trans.cipher, newCipher)

    def hybridDemo(self, message, pw):
        key = self.key

        trans = Encoding()
        deck = Shuffle()
        print(trans.cipher)

        pwi = int(pw) % len(trans.cipher)
        newCipher = deck.slide(trans.cipher, pwi)
        pwe = trans.encode(pw, trans.cipher)
        secretKey = pwe + key
        newCipher = deck.fixShuffle(newCipher, secretKey, trans.charSize)
        print(newCipher)

        self.demo(message, trans.cipher, newCipher)

    def passwordEncrypt(self, message, pw):
        key = self.key
        trans = Encoding()
        deck = Shuffle()

        pwe = trans.encode(pw, trans.cipher)
        secretKey = pwe + key
        newCipher = deck.fixShuffle(trans.cipher, secretKey, trans.charSize)

        encodedMessage = trans.encode(message, newCipher)
        encryptedMessage = trans.decode(encodedMessage, trans.cipher)

        return encryptedMessage

    def passwordDecrypt(self, message, pw):
        key = self.key
        trans = Encoding()
        deck = Shuffle()

        pwe = trans.encode(pw, trans.cipher)
        secretKey = pwe + key
        newCipher = deck.fixShuffle(trans.cipher, secretKey, trans.charSize)

        encodedMessage = trans.encode(message, trans.cipher)
        decryptedMessage = trans.decode(encodedMessage, newCipher)

        return decryptedMessage

    def caesarEncrypt(self, message, pw):
        trans = Encoding()
        deck = Shuffle()

        pw = int(pw)

        newCipher = deck.slide(trans.cipher, pw)

        encodedMessage = trans.encode(message, newCipher)
        encryptedMessage = trans.decode(encodedMessage, trans.cipher)

        return encryptedMessage

    def caesarDecrypt(self, message, pw):
        trans = Encoding()
        deck = Shuffle()

        pw = int(pw)

        newCipher = deck.slide(trans.cipher, pw)

        encodedMessage = trans.encode(message, trans.cipher)
        decryptedMessage = trans.decode(encodedMessage, newCipher)

        return decryptedMessage

    def hybridEncrypt(self, message, pw):
        key = self.key

        trans = Encoding()
        deck = Shuffle()

        pwe = trans.encode(pw, trans.cipher)
        pwi = int(pwe)
        newCipher = deck.slide(trans.cipher, pwi)
        secretKey = pwe + key
        newCipher = deck.fixShuffle(newCipher, secretKey, trans.charSize)

        encodedMessage = trans.encode(message, newCipher)
        encryptedMessage = trans.decode(encodedMessage, trans.cipher)

        return encryptedMessage

    def hybridDecrypt(self, message, pw):
        key = self.key

        trans = Encoding()
        deck = Shuffle()

        pwe = trans.encode(pw, trans.cipher)
        pwi = int(pwe) % len(trans.cipher)
        newCipher = deck.slide(trans.cipher, pwi)

        secretKey = pwe + key
        newCipher = deck.fixShuffle(newCipher, secretKey, trans.charSize)

        encodedMessage = trans.encode(message, trans.cipher)
        decryptedMessage = trans.decode(encodedMessage, newCipher)

        return decryptedMessage


if __name__ == "__main__":
    encrypt = Encrypting()
    while True:
        print("1. Caesar Chipher \n 2. Password Cipher \n 3. Hybrid Cipher")
        choice = input()
        if choice == '1':
            msg, pw = encrypt.askCredentials()
            encrypt.caesaDemo(msg, pw)

        elif choice == '2':
            msg, pw = encrypt.askCredentials()
            encrypt.passwordDemo(msg, pw)

        elif choice == '3':
            msg, pw = encrypt.askCredentials()
            encrypt.hybridDemo(msg, pw)
