import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T0024_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0024   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'map24'
    header.mapModel       = 'map.x'
    header.mapIndex       = 1
    header.bgm            = 10
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x2DE
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0xFFFFC950,
            dword_04        = 0x00000000,
            dword_08        = 0xFFFFD508,
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
        ScenaEntryPoint(
            dword_00        = 0x00002A94,
            dword_04        = 0xFFFFFF38,
            dword_08        = 0xFFFFC7C0,
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
            word_30         = 180,
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
        ScenaEntryPoint(
            dword_00        = 0x00002AF8,
            dword_04        = 0xFFFFFF38,
            dword_08        = 0xFFFFAC68,
            word_0C         = 0x0004,
            word_0E         = 0x00B4,
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
        ScenaEntryPoint(
            dword_00        = 0x00001B58,
            dword_04        = 0xFFFFFF38,
            dword_08        = 0xFFFFB9B0,
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
            word_30         = 270,
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
        ScenaEntryPoint(
            dword_00        = 0x00002AF8,
            dword_04        = 0x00000000,
            dword_08        = 0x0000CF08,
            word_0C         = 0x0004,
            word_0E         = 0x00B4,
            dword_10        = 0,
            dword_14        = 9500,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2800,
            dword_2C        = 262,
            word_30         = 315,
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
        ScenaEntryPoint(
            dword_00        = 0xFFFF8D8C,
            dword_04        = 0xFFFFFF9C,
            dword_08        = 0xFFFF9A70,
            word_0C         = 0x0004,
            word_0E         = 0x002D,
            dword_10        = 0,
            dword_14        = 9500,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2800,
            dword_2C        = 262,
            word_30         = 270,
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

# id: 0x10001 offset: 0x1FC
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
    ]

# id: 0x10002 offset: 0x1FC
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10003 offset: 0x1FC
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x1FC
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x1FC
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x1FC
@scena.Code('PreInit')
def PreInit():
    Return()

# id: 0x0001 offset: 0x1FD
@scena.Code('Init')
def Init():
    Return()

# id: 0x0002 offset: 0x1FE
@scena.Code('ReInit')
def ReInit():
    Fade(500)
    SetChrPos(0x0000, -13500, 0, 47000, 270)
    OP_0D()

    Return()

# id: 0x0003 offset: 0x216
@scena.Code('func_03_216')
def func_03_216():
    Fade(500)
    SetChrPos(0x0000, 53000, 0, 50200, 90)
    OP_0D()

    Return()

# id: 0x0004 offset: 0x22E
@scena.Code('func_04_22E')
def func_04_22E():
    Fade(500)
    SetChrPos(0x0000, 12000, -250, 45600, 0)
    OP_0D()

    Return()

# id: 0x0005 offset: 0x246
@scena.Code('func_05_246')
def func_05_246():
    Fade(500)
    SetChrPos(0x0000, -18000, 2850, 46600, 0)
    OP_0D()

    Return()

# id: 0x0006 offset: 0x25E
@scena.Code('func_06_25E')
def func_06_25E():
    Fade(500)
    SetChrPos(0x0000, 52000, 5000, 50500, 7)
    OP_0D()

    Return()

# id: 0x0007 offset: 0x276
@scena.Code('func_07_276')
def func_07_276():
    Fade(500)
    SetChrPos(0x0000, 17000, 0, 47000, 0)
    OP_0D()

    Return()

# id: 0x0008 offset: 0x28E
@scena.Code('func_08_28E')
def func_08_28E():
    NewScene('ED6_DT01/T0100._SN', 1, 0, 0)
    IdleLoop()

    Return()

# id: 0x0009 offset: 0x298
@scena.Code('func_09_298')
def func_09_298():
    NewScene('ED6_DT01/T0100._SN', 2, 0, 0)
    IdleLoop()

    Return()

# id: 0x000A offset: 0x2A2
@scena.Code('func_0A_2A2')
def func_0A_2A2():
    NewScene('ED6_DT01/T0100._SN', 3, 0, 0)
    IdleLoop()

    Return()

# id: 0x000B offset: 0x2AC
@scena.Code('func_0B_2AC')
def func_0B_2AC():
    EventBegin(0x00)
    NewScene('ED6_DT01/T0020._SN', 1, 0, 0)
    IdleLoop()

    Return()

# id: 0x000C offset: 0x2B8
@scena.Code('func_0C_2B8')
def func_0C_2B8():
    EventBegin(0x00)
    NewScene('ED6_DT01/T0022._SN', 1, 0, 0)
    IdleLoop()

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
