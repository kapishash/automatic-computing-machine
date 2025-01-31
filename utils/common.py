import base64


def encodeImage(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())
    

def decodeImage(imageString, fileName):
    imagedata = base64.b64decode(imageString)
    with open(fileName, "wb") as f:
        f.write(imagedata)
        f.close()

        