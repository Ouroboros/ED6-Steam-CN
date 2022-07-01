import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T3114_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3114   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'T3114.x'
    header.mapIndex       = 1
    header.bgm            = 13
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x2C3
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
    )

# id: 0x10003 offset: 0xA8
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0xA8
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -107140,
            y           = 0,
            z           = -340,
            range       = 1000,
            dword_10    = 0x000008CA,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000002,
        ),
        ScenaEventData(
            x           = -119480,
            y           = 0,
            z           = 6960,
            range       = 1000,
            dword_10    = 0x000008CA,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000003,
        ),
        ScenaEventData(
            x           = -107010,
            y           = 0,
            z           = 199500,
            range       = 1000,
            dword_10    = 0x000008CA,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000004,
        ),
        ScenaEventData(
            x           = -119590,
            y           = 0,
            z           = 206950,
            range       = 1000,
            dword_10    = 0x000008CA,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000005,
        ),
        ScenaEventData(
            x           = -106990,
            y           = 0,
            z           = 399440,
            range       = 1000,
            dword_10    = 0x000008CA,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000006,
        ),
        ScenaEventData(
            x           = -119440,
            y           = 0,
            z           = 406910,
            range       = 1000,
            dword_10    = 0x000008CA,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000007,
        ),
    )

# id: 0x10005 offset: 0x168
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x168
@scena.Code('PreInit')
def PreInit():
    Return()

# id: 0x0001 offset: 0x169
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_29A',
    )

    OP_6F(0x0003, 0)
    OP_72(0x0003, 0x0010)
    OP_6F(0x0007, 0)
    OP_72(0x0007, 0x0010)
    OP_6F(0x000B, 0)
    OP_72(0x000B, 0x0010)
    OP_6F(0x0000, 29)
    OP_72(0x0000, 0x0010)
    OP_6F(0x0001, 29)
    OP_72(0x0001, 0x0010)
    OP_6F(0x0002, 29)
    OP_72(0x0002, 0x0010)
    OP_6F(0x0004, 29)
    OP_72(0x0004, 0x0010)
    OP_6F(0x0005, 29)
    OP_72(0x0005, 0x0010)
    OP_6F(0x0006, 29)
    OP_72(0x0006, 0x0010)
    OP_6F(0x0008, 29)
    OP_72(0x0008, 0x0010)
    OP_6F(0x0009, 29)
    OP_72(0x0009, 0x0010)
    OP_6F(0x000A, 29)
    OP_72(0x000A, 0x0010)
    OP_71(0x000C, 0x0004)
    OP_71(0x000D, 0x0004)
    OP_71(0x000E, 0x0004)
    OP_71(0x000F, 0x0004)
    OP_71(0x0010, 0x0004)
    OP_71(0x0011, 0x0004)
    OP_71(0x0012, 0x0004)
    OP_71(0x0013, 0x0004)
    OP_71(0x0014, 0x0004)
    OP_71(0x0015, 0x0004)
    OP_71(0x0016, 0x0004)
    OP_71(0x0017, 0x0004)
    OP_71(0x0018, 0x0004)
    OP_71(0x0019, 0x0004)
    OP_71(0x001A, 0x0004)
    OP_71(0x001B, 0x0004)
    OP_71(0x001C, 0x0004)
    OP_71(0x001D, 0x0004)
    OP_71(0x001E, 0x0004)
    OP_71(0x001F, 0x0004)
    OP_71(0x0020, 0x0004)
    OP_71(0x0021, 0x0004)
    OP_71(0x0022, 0x0004)
    OP_71(0x0023, 0x0004)
    OP_71(0x0024, 0x0004)
    OP_71(0x0025, 0x0004)
    OP_71(0x0026, 0x0004)
    OP_79(0xFF, 0x0002)
    OP_7B()
    OP_10(0x00, 0x00)
    OP_10(0x06, 0x00)
    OP_10(0x0C, 0x00)

    def _loc_29A(): pass

    label('loc_29A')

    Return()

# id: 0x0002 offset: 0x29B
@scena.Code('ReInit')
def ReInit():
    SetPlaceName(0x0094)

    Return()

# id: 0x0003 offset: 0x29F
@scena.Code('func_03_29F')
def func_03_29F():
    SetPlaceName(0x0093)

    Return()

# id: 0x0004 offset: 0x2A3
@scena.Code('func_04_2A3')
def func_04_2A3():
    SetPlaceName(0x0096)

    Return()

# id: 0x0005 offset: 0x2A7
@scena.Code('func_05_2A7')
def func_05_2A7():
    SetPlaceName(0x0095)

    Return()

# id: 0x0006 offset: 0x2AB
@scena.Code('func_06_2AB')
def func_06_2AB():
    SetPlaceName(0x0098)

    Return()

# id: 0x0007 offset: 0x2AF
@scena.Code('func_07_2AF')
def func_07_2AF():
    SetPlaceName(0x0097)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
