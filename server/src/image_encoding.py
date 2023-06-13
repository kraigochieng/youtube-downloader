import base64

def encode_image_to_base_64(image_url):
    encoded_bytes =  base64.b64encode(image_url)
    print(encoded_bytes)
    return encoded_bytes.decode("utf-8")