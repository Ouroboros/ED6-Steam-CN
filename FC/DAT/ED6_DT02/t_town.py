from init import *

class TownEntry:
    def __init__(self, fs, cp):
        self.name = fs.ReadMultiByte(cp)
        if not self.name:
            fs.Position -= 1

        self.type = fs.ReadByte()

def load(path, cp):
    fs = fileio.FileStream(path)

    count = fs.ReadUShort()
    offsets = [fs.ReadUShort() for _ in range(count)]

    data = []

    for offset in offsets:
        fs.Position = offset
        data.append(TownEntry(fs, cp))

    return data

def main():
    os.chdir(os.path.dirname(__file__))

    cn = load(os.path.join(GAME_CN_PATH, 'ED6_DT02\\T_TOWN  ._DT'), 'GBK')
    en = load(os.path.join(GAME_EN_PATH, 'ED6_DT02\\T_TOWN  ._DT'), 'SHIFTJIS')

    assert len(cn) == len(en)

    fs = fileio.FileStream('T_TOWN  ._DT', 'wb')

    fs.Position = len(en) * 2 + 2
    offsets = []

    for index, town in enumerate(en):
        offsets.append(fs.Position)

        if town.name and not cn[index].name:
            raise

        if town.name:
            name = cn[index].name.encode('GBK') + b'\x00'
            fs.Write(name)

        fs.WriteByte(town.type)

    fs.Position = 0
    fs.WriteUShort(len(en))

    for offset in offsets:
        fs.WriteUShort(offset)

    load('T_TOWN  ._DT', 'GBK')

if __name__ == '__main__':
    Try(main)
