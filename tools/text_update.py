from ml import *

def main():
    text = json.loads(open('ed6_fc_text.json', 'rb').read().decode('utf-8-sig'))
    dump = open(r"D:\Game\Steam\steamapps\common\Trails in the Sky FC\memory_dump", 'rb').read()

    for t in text:
        original = t['original']
        if original:
            original = original.encode('shiftjis') + b'\x00'
            newrva = dump.find(original)
            t['rva'] = '%08X' % newrva

    open('ed6_fc_text_update.json', 'wb').write(json.dumps(text, ensure_ascii = False, indent = '  ').encode('utf_8_sig'))

if __name__ == '__main__':
    Try(main)
