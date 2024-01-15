from flask import Flask, render_template, request
import ddddocr
import base64

app = Flask(__name__)

@app.route('/ocr', methods=['GET'])
def ocr_api():
    args = request.args
    imgBase64 = args.get('img')
    img = base64.b64decode(f"{imgBase64}{'=' * (4 - len(imgBase64) % 4)}")
    ocr = ddddocr.DdddOcr()
    r = ocr.classification(imageData)
    return ''.join(r)
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8089)
