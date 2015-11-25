from ml import *

def main():
    jsonlines = []
    lines = []
    original = set()
    scan = set()
    for e in json.loads(open('ed6_fc_text.json', 'rb').read().decode('utf_8_sig')):
        original.add(e['original'])

    fs = fileio.FileStream(r"D:\Game\Steam\steamapps\common\Trails in the Sky FC\ed6_win_dump")

    base = 0x149000
    end = 0x173060
    fs.Position = base

    buffer = fs.Read(end - base)
    fs = fileio.FileStream(buffer)

    while fs.Position < fs.Length:
        pos = fs.Position + base

        ch = fs.ReadByte()
        ch2 = fs.ReadByte()
        fs.Position -= 2

        if any([
            chr(ch) in ['#', '%', ' '],
            (0x81 <= ch <= 0x9F or 0xE0 <= ch <= 0xEF) and (0x40 <= ch2 <= 0xFC),
            ]):

            if fs.Remaining >= 4:
                ptr = fs.ReadULong()

                if ptr & 0xFF000000 == 0 and (0x400000 <= ptr <= 0x600000 or (ptr >> 16) == 0x16):
                    continue

                fs.Position -= 4

            text = fs.ReadMultiByte('932')
            fs.Position = (fs.Position + 3) & ~3

            try:
                text.encode('932').decode('ASCII')
                continue
            except:
                pass

            scan.add(text)

            text = repr(text)

            jsonlines.append(OrderedDict([
                ('rva', '%08X' % pos),
                ('original', text),
                ('translation', ''),
            ]))

            lines.append('%08X %s' % (pos, text))

            # print('%08X: ' % pos, end = '')

            # try:
            #     print(text)
            # except UnicodeEncodeError:
            #     print(text.encode('932'))

            continue

        fs.Position += 4

    open('ed6_fc_text2.json', 'wb').write(json.dumps(jsonlines, ensure_ascii = False, indent = '  ').encode('utf_8_sig'))
    open('ed6_fc_text2.txt', 'wb').write('\n'.join(lines).encode('utf_8_sig'))

    for o in original:
        if o not in scan:
            try:
                print(o)
            except UnicodeEncodeError:
                print(o.encode('932'))

    print(len(lines))
    console.pause('done')

if __name__ == '__main__':
    Try(main)
