from ml import *

def main():
    text = json.loads(open('ed6_fc_text.json', 'rb').read().decode('utf-8-sig'))
    dump = open(r"D:\Game\Steam\steamapps\common\Trails in the Sky FC\memory_dump", 'rb').read()

    for t in text:
        original = t['original']
        if original:
            original = original.encode('shiftjis')
            original += (4 - (len(original) % 4)) * b'\x00'

            start = 0
            while start < len(dump):
                newrva = dump.find(original, start)
                if newrva == -1:
                    start = len(dump)
                    continue

                if newrva % 4 != 0:
                    start = newrva + len(original)
                    if start == 7: ibp()
                    continue

                t['rva'] = '%08X' % newrva
                break

            else:
                print('missing %s' % original)
                # ibp()

    open('ed6_fc_text_update.json', 'wb').write(json.dumps(text, ensure_ascii = False, indent = '  ').encode('utf_8_sig'))

if __name__ == '__main__':
    Try(main)
