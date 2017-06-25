from ml import *

def iterable(text):
    return text if isinstance(text, (list, tuple)) else [text]

def main():
    try:
        ed6_fc_text = json.loads(open('ed6_fc_text_update.json', 'rb').read().decode('utf-8-sig'))
    except:
        ed6_fc_text = json.loads(open('ed6_fc_text.json', 'rb').read().decode('utf-8-sig'))

    entries = []
    for text in ed6_fc_text:
        translation = text['translation']
        if not translation:
            continue

        rva = int(text['rva'], 16)

        if rva == 0:
            continue

        entries.append((rva, translation))

    fs = fileio.FileStream('ed6fc.text', 'wb')
    fs.WriteULong(len(entries))

    for rva, text in entries:
        text = text.replace('・・・', '…').replace('・', '·')
        # print('%X' % rva)
        text = text.encode('gbk') + b'\x00'
        fs.WriteULong(rva)
        fs.WriteULong(len(text))
        fs.Write(text)

        fs.Position = (fs.Position + 3) & ~3

if __name__ == '__main__':
    Try(main)
