import qrcode
import numpy

# 原文
text = "Well done! Correct answer.\nthank you for trying."
# シーザー暗号キー
KEY = 5

# 暗号文
e_text = ""

# シーザー暗号化
for t in text:
    if('a' <= t <= "z"):
        t = chr((ord(t) + KEY - 97) % 26 + 97)
    elif('A' <= t <= "Z"):
        t = chr((ord(t) + KEY - 65) % 26 + 65)
    e_text += t

# ヒント追加
e_text += "\nShift:"+str(KEY)

# QRコード設定
qr = qrcode.QRCode(box_size=1,border=0)

# QRコードデータ作成
qr.add_data(e_text)
qr.make()
img = qr.make_image()

# QRコード画像出力
#img.save("QR.png")

# 作成したQRコードをアスキーアート化
data = numpy.array(img.getdata()).reshape(*img.size)

qr_text = list()
for y in data:
    row = ""
    for x in y:
        if x==255: #空白
            row += "　"
        else: #黒
            row += "■"
    qr_text.append(row)

# HTML作成
with open("output.html","w") as f:
    f.write("""
    <div style="color:#000;font-size:16px;line-height:72%;letter-spacing:-5px;font-family:'ＭＳ ゴシック','Osaka－等幅',monospace;font-weight:bold;">
    """)
    for t in qr_text:
        f.write(t+"<br>\n")

    f.write("</div>")
