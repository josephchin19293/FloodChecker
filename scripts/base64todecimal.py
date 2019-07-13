import base64
def base64todecimal(encoded_data):
    # encoded_data = b'BZM='
    decoded_data = base64.b64decode(encoded_data)
    # print repr(decoded_data)
    normalHex= decoded_data.encode('hex').upper()
    result = int(normalHex, 16)
    return result

# print (base64todecimal('BZM='))
