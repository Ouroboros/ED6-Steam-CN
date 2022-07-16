import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C0401_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C0401   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '波波'),
    TXT(0x02, '波波'),
    TXT(0x03, '波波'),
    TXT(0x04, '岩溶捕猎手'),
    TXT(0x05, '竹刀飞鱼'),
    TXT(0x06, '食人鲨'),
    TXT(0x07, '食人鲨'),
    TXT(0x08, '食人鲨'),
    TXT(0x09, '波波'),
    TXT(0x0A, '波波'),
    TXT(0x0B, '食人鲨'),
    TXT(0x0C, '食人鲨'),
    TXT(0x0D, '竹刀飞鱼'),
    TXT(0x0E, '竹刀飞鱼'),
    TXT(0x0F, '竹刀飞鱼'),
    TXT(0x10, '竹刀飞鱼'),
    TXT(0x11, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'C0401.x'
    header.mapIndex       = 16
    header.bgm            = 33
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x358
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
            word_3A         = 16,
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
        ('ED6_DT09/CH10160._CH', 'ED6_DT09/CH10160P._CP'),
        ('ED6_DT09/CH10161._CH', 'ED6_DT09/CH10161P._CP'),
        ('ED6_DT09/CH10150._CH', 'ED6_DT09/CH10150P._CP'),
        ('ED6_DT09/CH10151._CH', 'ED6_DT09/CH10151P._CP'),
        ('ED6_DT09/CH10040._CH', 'ED6_DT09/CH10040P._CP'),
        ('ED6_DT09/CH10041._CH', 'ED6_DT09/CH10041P._CP'),
        ('ED6_DT09/CH10190._CH', 'ED6_DT09/CH10190P._CP'),
        ('ED6_DT09/CH10191._CH', 'ED6_DT09/CH10191P._CP'),
    ]

# id: 0x10002 offset: 0xEA
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10003 offset: 0xEA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = 0,
            z           = 0,
            y           = 11000,
            word_0C     = 0x0000,
            word_0E     = 0x0002,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0034,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 8000,
            z           = 0,
            y           = 19000,
            word_0C     = 0x0000,
            word_0E     = 0x0002,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0034,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -8000,
            z           = 0,
            y           = 19000,
            word_0C     = 0x0000,
            word_0E     = 0x0002,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0034,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 0,
            z           = 0,
            y           = 27000,
            word_0C     = 0x0000,
            word_0E     = 0x0006,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x003B,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 0,
            z           = 0,
            y           = 19000,
            word_0C     = 0x0000,
            word_0E     = 0x0004,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0036,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -8000,
            z           = 0,
            y           = 0,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0038,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -20000,
            z           = 0,
            y           = 27000,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0038,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 19000,
            z           = 0,
            y           = 13000,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0038,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 63000,
            z           = 0,
            y           = 7000,
            word_0C     = 0x0000,
            word_0E     = 0x0002,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0034,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 55000,
            z           = 0,
            y           = 7000,
            word_0C     = 0x0000,
            word_0E     = 0x0002,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0034,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 46000,
            z           = 0,
            y           = -10000,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0039,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 73000,
            z           = 0,
            y           = -9000,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0039,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 71000,
            z           = 0,
            y           = 7000,
            word_0C     = 0x0000,
            word_0E     = 0x0004,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0036,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 47000,
            z           = 0,
            y           = 2000,
            word_0C     = 0x0000,
            word_0E     = 0x0004,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0036,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 65000,
            z           = 0,
            y           = 18000,
            word_0C     = 0x0000,
            word_0E     = 0x0004,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x003A,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 52000,
            z           = 0,
            y           = 18000,
            word_0C     = 0x0000,
            word_0E     = 0x0004,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x003A,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x2AA
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 43000,
            y           = -200,
            z           = 11000,
            range       = 45000,
            dword_10    = 0x00000708,
            dword_14    = 0x000032C8,
            dword_18    = 0x00000010,
            dword_1C    = 0x00000002,
        ),
        ScenaEventData(
            x           = 43000,
            y           = -200,
            z           = 6000,
            range       = 45000,
            dword_10    = 0x00000708,
            dword_14    = 0x00001F40,
            dword_18    = 0x00000010,
            dword_1C    = 0x00000003,
        ),
        ScenaEventData(
            x           = 72800,
            y           = -200,
            z           = 11000,
            range       = 74800,
            dword_10    = 0x00000708,
            dword_14    = 0x000032C8,
            dword_18    = 0x00000010,
            dword_1C    = 0x00000004,
        ),
        ScenaEventData(
            x           = 72800,
            y           = -200,
            z           = 1000,
            range       = 74800,
            dword_10    = 0x00000708,
            dword_14    = 0x00000BB8,
            dword_18    = 0x00000010,
            dword_1C    = 0x00000005,
        ),
    )

# id: 0x10005 offset: 0x32A
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x32A
@scena.Code('PreInit')
def PreInit():
    Return()

# id: 0x0001 offset: 0x32B
@scena.Code('Init')
def Init():
    Return()

# id: 0x0002 offset: 0x32C
@scena.Code('ReInit')
def ReInit():
    OP_70(0x0004, 60)

    Return()

# id: 0x0003 offset: 0x334
@scena.Code('func_03_334')
def func_03_334():
    OP_70(0x0005, 60)

    Return()

# id: 0x0004 offset: 0x33C
@scena.Code('func_04_33C')
def func_04_33C():
    OP_70(0x0009, 60)

    Return()

# id: 0x0005 offset: 0x344
@scena.Code('func_05_344')
def func_05_344():
    OP_70(0x0007, 60)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
