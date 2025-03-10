
def encrypt(plain_text):

    encrypt=input("do you want to encrypt the text")
    try:
         if encrypt == "yes":
            encrypt_text={"a":"h", "b":"y","c":"p","d":"j"}
            encrypt_result=""
            for char in plain_text:#loop in each letter in plain text
                if char in encrypt_text:
                    encrypt_result+=encrypt_text[char]#replace the letter if it is in the dictionary
                else:
                     encrypt_result += char#stays the same if not found in the dictionary
            print(encrypt_result)
         else:
            print(plain_text)
    except:
      print("error")

def decrypt(encrypted_text):
    decrypt = input("Do you want to decrypt the text? (yes/no): ").lower()
    try:
        if decrypt == "yes":
            decrypt_text = {"h": "a", "y": "b", "p": "c", "j": "d"}  # Reverse the mapping of encrypt_text
            decrypt_result = ""
            for char in encrypted_text:  # Loop through each character in the encrypted text
                if char in decrypt_text:
                    decrypt_result += decrypt_text[char]  # Replace the letter if it is in the dictionary
                else:
                    decrypt_result += char  # Keep the letter as is if not found in the dictionary
            print("Decrypted text:", decrypt_result)  # Print the decrypted text
        else:
            print("Encrypted text:", encrypted_text)  # Print the encrypted text if no decryption
    except :
        print("Error")

text_ms=input("enter a text")
encryption = encrypt(text_ms)
decrypt(encryption)