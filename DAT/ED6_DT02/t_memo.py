from init import *

class MemoEntry:
    def __init__(self, index, fs):
        self.index = fs.ReadUShort()

        assert self.index == index

        self.unknown = fs.ReadUShort()
        self.offset = fs.ReadUShort()
        self.text = ''

def load(path, cp):
    fs = fileio.FileStream(path)

    minOffset = fs.ReadUShort()
    offsets = [minOffset]

    while fs.Position < minOffset:
        offsets.append(fs.ReadUShort())

    data = []

    for index, offset in enumerate(offsets):
        fs.Position = offset
        entry = MemoEntry(index, fs)

        fs.Position = entry.offset
        entry.text = fs.ReadMultiByte(cp)

        data.append(entry)

    return data

def main():
    os.chdir(os.path.dirname(__file__))

    cn = load(os.path.join(GAME_CN_PATH, 'ED6_DT02\\T_MEMO  ._DT'), 'GBK')
    en = load(os.path.join(GAME_EN_PATH, 'ED6_DT02\\T_MEMO  ._DT'), 'SHIFTJIS')

    assert len(cn) == len(en)

    fs = fileio.FileStream('T_MEMO  ._DT', 'wb')

    fs.Position = len(en) * 2
    offsets = []

    for index, entry in enumerate(en):
        offsets.append(fs.Position)

        if entry.text and not cn[index].text:
            raise

        text = cn[index].text.encode('GBK') + b'\x00'

        fs.WriteUShort(entry.index)
        fs.WriteUShort(entry.unknown)
        fs.WriteUShort(fs.Position + 2)
        fs.Write(text)

    fs.Position = 0
    for offset in offsets:
        fs.WriteUShort(offset)

    load('T_MEMO  ._DT', 'GBK')

if __name__ == '__main__':
    Try(main)
