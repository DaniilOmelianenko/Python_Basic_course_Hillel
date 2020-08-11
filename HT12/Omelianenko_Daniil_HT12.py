import string
import random
import zipfile

PASSWORD_LENGTH = 4


def extract_archive(file_to_open, password):
    try:
        file_to_open.extractall(pwd=password.encode())
        return True
    except Exception as e:
        print(e)
        return False


def hack_archive(file_name):
    file_to_open = zipfile.ZipFile(file_name)
    wrong_passwords = []
    tries = 0

    while True:
        password = "".join(random.choices(string.digits, k=PASSWORD_LENGTH))
        if password in wrong_passwords:
            continue
        elif extract_archive(file_to_open, password) is True:
            print(f'Archive {file_name} is hacked. Password - {password}')
            print(f'Password was found after {tries} tries')
            break
        print(f"{password} - False")
        wrong_passwords.append(password)
        tries += 1


filename = 'archive.zip'
hack_archive(filename)
