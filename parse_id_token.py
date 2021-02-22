#!/usr/bin/env python3
import os
import errno
import base64
import ast
import json

def decode_jwt():
    
    file_path = None
    while file_path == None:
        file_path = input("Enter JWT file location: ")
        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
            with open(file_path, 'r') as file:
                raw_jwt = file.read().rstrip()
                decoded_jwt = {}
                split_raw_jwt = raw_jwt.split('.')
                encoded_jwt_header = split_raw_jwt[0]
                encoded_jwt_payload = split_raw_jwt[1]
                encoded_jwt_signature = split_raw_jwt[2]

                try:
                    decoded_jwt['header'] = ast.literal_eval(base64.standard_b64decode(encoded_jwt_header + "====").decode(encoding="utf-8"))
                    decoded_jwt['payload'] = ast.literal_eval(base64.standard_b64decode(encoded_jwt_payload + "====").decode(encoding="utf-8"))
                    decoded_jwt['signature'] = encoded_jwt_signature
                except Exception as err:
                    print(err)
            
            return decoded_jwt

        else:
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), file_path)
    
if __name__ == "__main__":
    decoded_jwt = decode_jwt()
    print(F"JWT Header: {decoded_jwt['header']}")
    print(F"JWT Payload: {decoded_jwt['payload']}")
    print(F"Full JWT: {decoded_jwt}")