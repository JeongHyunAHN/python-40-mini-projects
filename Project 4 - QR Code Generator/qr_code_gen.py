import qrcode

# qrData = "www.naver.com"
# qrImg = qrcode.make(qrData)

# qrImg.save(qrData + ".png")

filePath = r"qr_code_list.txt"
with open(filePath, 'rt', encoding="UTF8") as f:
    readLines = f.readlines()
    
    for line in readLines:
        line = line.strip()
        qrImg = qrcode.make(line)
        qrImg.save(line + ".png")
        