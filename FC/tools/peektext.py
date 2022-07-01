from ml import *

def main():
    fs = fileio.FileStream(r"D:\Game\Steam\steamapps\common\Trails in the Sky FC\ed6_win_dump")

    lines = []
    xml = OrderedDict()
    root   = OrderedDict()
    xml['ed6fc'] = root
    root['text'] = lines
    for l in fileio.readLines(r'ed6_fc_text2.txt'):
        if not l:
            continue

        addr, text = l.split(' ', 1)
        # addr, *_, length = addr.split(' ')
        addr = int(addr, 16)

        # addr -= 0x400000
        fs.Position = addr

        original = fs.ReadMultiByte('shiftjis')

        lines.append(OrderedDict([
            ('rva', '%08X' % addr),
            ('original', original),
            ('translation', original),

            # ('original', {'#text': '%s' % fs.ReadMultiByte('shiftjis')}),
            # ('translation', {'#text': ''}),
        ]))

    # lines[:] = sorted(lines, key = lambda e: int(e['rva'], 16))

    # open('ed6_fc_text.xml', 'wb').write(xmltodict.unparse(xml, pretty = True, indent = '  ').encode('utf_8_sig'))
    open('ed6_fc_text2.json', 'wb').write(json.dumps(lines, ensure_ascii = False, indent = '  ').encode('utf_8_sig'))

    console.pause('done')

if __name__ == '__main__':
    Try(main)
