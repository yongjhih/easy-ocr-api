from ocrmac import ocrmac
from flask import Flask, render_template, request
from flask_cors import cross_origin
from PIL import Image
import io, base64

app = Flask(__name__)

@app.route('/ocr', methods=['GET'])
@cross_origin()
def ocr_api():
    args = request.args
    imgBase64 = args.get('img')
    img = Image.open(io.BytesIO(base64.decodebytes(bytes(imgBase64, "utf-8"))))

    res = ocrmac.OCR(img).recognize()
    print(res)
    return res[0][0]
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8089)
