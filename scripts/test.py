import base64

encoded_data = 'BZM='
decoded_data = base64.b64decode(encoded_data)
print('Decoded :', decoded_data)
