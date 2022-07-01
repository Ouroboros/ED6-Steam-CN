import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T4203_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4203   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, 'Private Dan'),
    TXT(0x02, 'Private Aluts'),
    TXT(0x03, 'Grancel - North Block'),
    TXT(0x04, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4203.x'
    header.mapIndex       = 1
    header.bgm            = 84
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x164
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
        ('ED6_DT07/CH01300._CH', 'ED6_DT07/CH01300P._CP'),
        (None, 'ED6_DT07/CH02140P._CP'),
        (None, 'ED6_DT07/CH02470P._CP'),
        (None, 'ED6_DT07/CH01330P._CP'),
        (None, 'ED6_DT07/CH00401P._CP'),
        (None, 'ED6_DT07/CH00421P._CP'),
        (None, 'ED6_DT07/CH00391P._CP'),
        (None, 'ED6_DT07/CH00411P._CP'),
        (None, 'ED6_DT07/CH02090P._CP'),
        (None, 'ED6_DT07/CH00321P._CP'),
        (None, 'ED6_DT07/CH02000P._CP'),
    ]

# id: 0x10002 offset: 0xDA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = -790,
            z                   = 0,
            y                   = 41980,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0002,
        ),
        ScenaNpcData(
            x                   = 950,
            z                   = 0,
            y                   = 41980,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = -22550,
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

# id: 0x10003 offset: 0x13A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x13A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x13A
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x13A
@scena.Code('PreInit')
def PreInit():
    Return()

# id: 0x0001 offset: 0x13B
@scena.Code('Init')
def Init():
    OP_16(0x02, 0x00000FA0, 0xFFFE0C00, 0xFFFE4A80, 0x00230060)

    Return()

# id: 0x0002 offset: 0x14E
@scena.Code('ReInit')
def ReInit():
    TalkBegin(0x00FE)
    TalkEnd(0x00FE)

    Return()

# id: 0x0003 offset: 0x155
@scena.Code('func_03_155')
def func_03_155():
    TalkBegin(0x00FE)
    TalkEnd(0x00FE)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
