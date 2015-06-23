# This is the file for the deciphering partner.

alphabet = "abcdefghijklmnopqrstuvwxyz "

alphabet_list = list(alphabet)

# Copy and paste the cipher list from your partner below,
# instead of the empty list.
cipher_list = ['p', 'a', 'y', 'o', 'u', 'l', 'n', 'b', 'i', 't', 'z', 'd', 'g', ' ', 'c', 'w', 'j', 'e', 'r', 'q', 'k', 'v', 'f', 'x', 's', 'm', 'h']


# copy and paste the cipher_text from your partner in slack
# and assign it to the variable new_cipher_text
new_cipher_text = "fbshirhrixhplepiohclhruvu"

decrypt_text = ""

for y in new_cipher_text:
    index = cipher_list.index(y)
    decrypt_char = alphabet_list[index]
    decrypt_text += decrypt_char

print(decrypt_text)
