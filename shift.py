ukr_alphabet = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя,. -!?"
uk_alphabet = "abcdefghijklmnopqrstuvwxyz"


def shift(message: str, shift: int, A: str) -> str:

    encrypted_message = ""
    for s in message:
        encrypted_message += A[(A.index(s) + shift) % (len(A))]
    return encrypted_message


def decrypt_shift(message: str, shift: int, A: str) -> str:
    decrypted_message = ""
    for s in message:
        decrypted_message += A[(A.index(s) - shift) % (len(A))]
    return decrypted_message


for i in range(len(ukr_alphabet)):
    print(decrypt_shift("a'-оі,о!яіфубо!у'ршд", i, ukr_alphabet))
