import hashlib
import os

print('Hashing Algorithms: \n1. MD5\n2. SHA1 \n3. SHA224\n4. SHA256\n5. SHA384\n6. SHA512')
hashtype = str(input('Enter The Name Of Hashing Algorithm Of Your Choice: '))
hashtype = hashtype.lower()
# print(hashtype)

filepath = str(input('Enter Path Of File To BRUTE Force With: '))
hash_to_decrypt = str(input('Enter Hash Value To Brute Force: '))

if os.path.exists(filepath) == False:
    print('[!!] File/Path Does Not Exist!')
    exit(1)

with open(filepath, 'r', encoding="utf8") as file:
    for line in file.readlines():
        if hashtype == 'md5':
            hash_obj = hashlib.md5(line.strip().encode())
            hashed_word = hash_obj.hexdigest()
            if hashed_word == hash_to_decrypt:
                print('Found MD5 Password: '+line.strip())
                exit(0)
        elif hashtype == 'sha1':
            hash_obj = hashlib.sha1(line.strip().encode())
            hashed_word = hash_obj.hexdigest()
            if hashed_word == hash_to_decrypt:
                print('Found SHA1 Password: '+line.strip())
                exit(0)
        elif hashtype == 'sha224':
            hash_obj = hashlib.sha224(line.strip().encode())
            hashed_word = hash_obj.hexdigest()
            if hashed_word == hash_to_decrypt:
                print('Found SHA224 Password: '+line.strip())
                exit(0)
        elif hashtype == 'sha256':
            hash_obj = hashlib.md5(line.strip().encode())
            hashed_word = hash_obj.hexdigest()
            if hashed_word == hash_to_decrypt:
                print('Found SHA256 Password: '+line.strip())
                exit(0)
        elif hashtype == 'sha384':
            hash_obj = hashlib.sha384(line.strip().encode())
            hashed_word = hash_obj.hexdigest()
            if hashed_word == hash_to_decrypt:
                print('Found SHA384 Password: '+line.strip())
                exit(0)
        elif hashtype == 'sha512':
            hash_obj = hashlib.sha512(line.strip().encode())
            hashed_word = hash_obj.hexdigest()
            if hashed_word == hash_to_decrypt:
                print('Found SHA512 Password: '+line.strip())
                exit(0)
        else:
            print('[!!] Hash Type Incorrect.')
            exit(1)

    print('Password Is Not In File.')

# BRUTE FORCE ATTACK
# - Provide The Hash Value Of The Password To Crack
# - Input The Password Dictionary To Brute Force With