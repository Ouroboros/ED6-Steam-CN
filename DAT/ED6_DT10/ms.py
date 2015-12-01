from init import *

class CraftInfo:
    def __init__(self, fs, cp):
        self.data = fs.Read(0x1C)
        self.name = fs.ReadMultiByte(cp)
        self.desc = fs.ReadMultiByte(cp)

    def __eq__(self, that):
        return self.data == that.data

class MSFile:
    def __init__(self, file, cp):
        fs = fileio.FileStream(file)

        self.fileName = os.path.basename(file)
        self.meta   = fs.Read(0xAC)
        self.arts   = [fs.Read(0x18) for _ in range(fs.ReadByte())]
        self.craft  = [fs.Read(0x18) for _ in range(fs.ReadByte())]
        self.scraft = [fs.Read(0x18) for _ in range(fs.ReadByte())]
        self.info   = [CraftInfo(fs, cp) for _ in range(fs.ReadByte())]

    def __eq__(self, that):
        return all([
            self.meta   == that.meta,
            self.arts   == that.arts,
            self.craft  == that.craft,
            self.scraft == that.scraft,
            self.info   == that.info,
        ])

def load(path, cp):
    ms = [MSFile(file, cp) for file in fileio.getDirectoryFiles(path, 'MS*._DT')]
    return ms

def main():
    os.chdir(os.path.dirname(__file__))

    cn = load(os.path.join(GAME_CN_PATH, 'ED6_DT10'), 'GBK')
    en = load(os.path.join(GAME_EN_PATH, 'ED6_DT10'), 'SHIFTJIS')

    assert len(cn) == len(en)
    print(len(cn), len(en))

    for index, ms in enumerate(en):
        print(ms.fileName, cn[index].fileName)
        if ms.fileName not in ['MS30100 ._DT', 'MS30110 ._DT', 'MS30120 ._DT']:
            assert ms == cn[index]

if __name__ == '__main__':
    Try(main)
