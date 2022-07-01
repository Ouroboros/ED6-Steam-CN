import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T4151_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4151   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '王都格兰赛尔·北街区'),
    TXT(0x02, '王都格兰赛尔·南街区'),
    TXT(0x03, '王都格兰赛尔·空港'),
    TXT(0x04, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4151.x'
    header.mapIndex       = 1
    header.bgm            = 34
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x2E8
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
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

# id: 0x10001 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
    ]

# id: 0x10002 offset: 0xA8
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 17760,
            z                   = 0,
            y                   = 63880,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x00FF,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 29270,
            z                   = 0,
            y                   = -950,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x00FF,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 51010,
            z                   = 0,
            y                   = 102170,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x00FF,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x108
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x108
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 109720,
            y           = 1000,
            z           = 32980,
            range       = 2000,
            dword_10    = 0x00000FA0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000003,
        ),
        ScenaEventData(
            x           = 76740,
            y           = 1000,
            z           = 23010,
            range       = 2000,
            dword_10    = 0x000009C4,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000004,
        ),
        ScenaEventData(
            x           = 69950,
            y           = 1000,
            z           = 14290,
            range       = 2000,
            dword_10    = 0x000009C4,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000004,
        ),
        ScenaEventData(
            x           = 63260,
            y           = 1000,
            z           = 22960,
            range       = 2000,
            dword_10    = 0x000009C4,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000004,
        ),
        ScenaEventData(
            x           = 69910,
            y           = 1000,
            z           = 31710,
            range       = 2000,
            dword_10    = 0x000009C4,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000004,
        ),
        ScenaEventData(
            x           = 42920,
            y           = 0,
            z           = 81110,
            range       = 2000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000005,
        ),
        ScenaEventData(
            x           = 70940,
            y           = 0,
            z           = -9490,
            range       = 2000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000006,
        ),
        ScenaEventData(
            x           = 75010,
            y           = 0,
            z           = 71300,
            range       = 2000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000007,
        ),
    )

# id: 0x10005 offset: 0x208
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 38820,
            triggerZ            = 1250,
            triggerY            = 36920,
            triggerRange        = 800,
            actorX              = 38820,
            actorZ              = 2250,
            actorY              = 36920,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x22C
@scena.Code('PreInit')
def PreInit():
    Return()

# id: 0x0001 offset: 0x22D
@scena.Code('Init')
def Init():
    OP_16(0x02, 0x00000FA0, 0xFFFF4C50, 0xFFFEA070, 0x0023005C)
    OP_72(0x0009, 0x0010)
    OP_72(0x000A, 0x0010)
    OP_71(0x0000, 0x0010)
    OP_71(0x0001, 0x0010)
    OP_71(0x0002, 0x0010)
    OP_71(0x0003, 0x0010)

    Return()

# id: 0x0002 offset: 0x25E
@scena.Code('ReInit')
def ReInit():
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '『导力式时钟２号机』\n',
            '　七耀历１１６３年·由蔡斯技术工房制造',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Return()

# id: 0x0003 offset: 0x2C4
@scena.Code('func_03_2C4')
def func_03_2C4():
    SetPlaceName(0x00BA)

    Return()

# id: 0x0004 offset: 0x2C8
@scena.Code('func_04_2C8')
def func_04_2C8():
    SetPlaceName(0x00B1)

    Return()

# id: 0x0005 offset: 0x2CC
@scena.Code('func_05_2CC')
def func_05_2CC():
    SetPlaceName(0x00BB)

    Return()

# id: 0x0006 offset: 0x2D0
@scena.Code('func_06_2D0')
def func_06_2D0():
    SetPlaceName(0x00BC)

    Return()

# id: 0x0007 offset: 0x2D4
@scena.Code('func_07_2D4')
def func_07_2D4():
    SetPlaceName(0x00BD)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
