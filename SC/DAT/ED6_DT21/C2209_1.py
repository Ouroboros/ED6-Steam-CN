import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C2209_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C2209_1 ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'C0403.x'
    header.mapIndex       = 1
    header.bgm            = 15
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0x00000000,
            dword_04        = 0x00000000,
            dword_08        = 0x00001770,
            word_0C         = 0x0004,
            word_0E         = 0x0000,
            dword_10        = 0,
            dword_14        = 9500,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2800,
            dword_2C        = 262,
            word_30         = 45,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 0,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
    )

# id: 0x10000 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
    ]

# id: 0x10001 offset: 0xA8
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10002 offset: 0xA8
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0xA8
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0xA8
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0xA8
@scena.Code('Init')
def Init():
    FadeOut(0, 0, -1)
    EventBegin(0x00)
    OP_72(0x0004, 0x0004)
    OP_71(0x0002, 0x0020)
    OP_71(0x0004, 0x0020)
    OP_71(0x0002, 0x0008)
    OP_71(0x0004, 0x0008)
    CameraMove(3340, 13200, 3070, 0)
    OP_67(0, 10720, -10000, 0)
    CameraSetDistance(4800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    FadeIn(2000, 0)
    CreateThread(0x0101, 0x00, 0x01, 0x0001)
    CreateThread(0x0101, 0x01, 0x01, 0x0002)
    CreateThread(0x0101, 0x02, 0x01, 0x0003)
    CreateThread(0x0101, 0x03, 0x01, 0x0004)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(4000)

    OP_56(0x00)
    FadeOut(2000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/C2219._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0001 offset: 0x154
@scena.Code('func_01_154')
def func_01_154():
    CameraMove(90, 28750, 5270, 12000)

    Return()

# id: 0x0002 offset: 0x166
@scena.Code('func_02_166')
def func_02_166():
    OP_67(0, 7310, -10000, 12000)

    Return()

# id: 0x0003 offset: 0x178
@scena.Code('func_03_178')
def func_03_178():
    CameraSetDistance(3560, 12000)

    Return()

# id: 0x0004 offset: 0x182
@scena.Code('func_04_182')
def func_04_182():
    OP_6C(338000, 12000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
