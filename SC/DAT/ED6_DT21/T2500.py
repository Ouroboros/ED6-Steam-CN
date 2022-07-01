import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T2500_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2500   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '乔儿'),
    TXT(0x02, '汉斯'),
    TXT(0x03, '基库'),
    TXT(0x04, '米克'),
    TXT(0x05, '芙拉瑟'),
    TXT(0x06, '蕾娜'),
    TXT(0x07, '坎诺'),
    TXT(0x08, '帕布尔'),
    TXT(0x09, '艾福托老师'),
    TXT(0x0A, '巴克斯'),
    TXT(0x0B, '奥利维尔'),
    TXT(0x0C, '布卢布兰的亡灵'),
    TXT(0x0D, '强化猎兵'),
    TXT(0x0E, '强化猎兵'),
    TXT(0x0F, '强化猎兵'),
    TXT(0x10, '强化猎兵'),
    TXT(0x11, '装甲猎豹'),
    TXT(0x12, '装甲猎豹'),
    TXT(0x13, '哨兵'),
    TXT(0x14, '哨兵'),
    TXT(0x15, '王国军士兵'),
    TXT(0x16, '王国军士兵'),
    TXT(0x17, '卡露娜'),
    TXT(0x18, '库拉茨'),
    TXT(0x19, '罗迪'),
    TXT(0x1A, '巴托姆'),
    TXT(0x1B, '王立学院·小道'),
    TXT(0x1C, '街景林道方向'),
    TXT(0x1D, ''),
    TXT(0x1E, ''),
    TXT(0x1F, ''),
    TXT(0x20, ''),
    TXT(0x21, ''),
    TXT(0x22, ''),
    TXT(0x23, ''),
    TXT(0x24, ''),
    TXT(0x25, ''),
    TXT(0x26, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'T2500.x'
    header.mapIndex       = 1
    header.bgm            = 14
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0xB8BD
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
        ('ED6_DT07/CH02390._CH', 'ED6_DT07/CH02390P._CP'),
        ('ED6_DT07/CH02550._CH', 'ED6_DT07/CH02550P._CP'),
        ('ED6_DT07/CH02320._CH', 'ED6_DT07/CH02320P._CP'),
        ('ED6_DT26/CH20238._CH', 'ED6_DT26/CH20238P._CP'),
        ('ED6_DT07/CH02323._CH', 'ED6_DT07/CH02323P._CP'),
        ('ED6_DT07/CH01080._CH', 'ED6_DT07/CH01080P._CP'),
        ('ED6_DT07/CH01090._CH', 'ED6_DT07/CH01090P._CP'),
        ('ED6_DT07/CH01370._CH', 'ED6_DT07/CH01370P._CP'),
        ('ED6_DT07/CH01580._CH', 'ED6_DT07/CH01580P._CP'),
        ('ED6_DT07/CH01093._CH', 'ED6_DT07/CH01093P._CP'),
        ('ED6_DT07/CH01460._CH', 'ED6_DT07/CH01460P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT06/CH20045._CH', 'ED6_DT06/CH20045P._CP'),
        ('ED6_DT26/CH20270._CH', 'ED6_DT26/CH20270P._CP'),
        ('ED6_DT26/CH20422._CH', 'ED6_DT26/CH20422P._CP'),
        ('ED6_DT26/CH20424._CH', 'ED6_DT26/CH20424P._CP'),
        ('ED6_DT29/CH12320._CH', 'ED6_DT29/CH12320P._CP'),
        ('ED6_DT29/CH12321._CH', 'ED6_DT29/CH12321P._CP'),
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
        ('ED6_DT07/CH01240._CH', 'ED6_DT07/CH01240P._CP'),
        ('ED6_DT07/CH01260._CH', 'ED6_DT07/CH01260P._CP'),
        ('ED6_DT26/CH20423._CH', 'ED6_DT26/CH20423P._CP'),
        ('ED6_DT07/CH01360._CH', 'ED6_DT07/CH01360P._CP'),
        ('ED6_DT29/CH12330._CH', 'ED6_DT29/CH12330P._CP'),
        ('ED6_DT29/CH12331._CH', 'ED6_DT29/CH12331P._CP'),
        ('ED6_DT29/CH12350._CH', 'ED6_DT29/CH12350P._CP'),
        ('ED6_DT29/CH12351._CH', 'ED6_DT29/CH12351P._CP'),
        ('ED6_DT29/CH12570._CH', 'ED6_DT29/CH12570P._CP'),
        ('ED6_DT29/CH12571._CH', 'ED6_DT29/CH12571P._CP'),
    ]

# id: 0x10002 offset: 0x192
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 58530,
            z                   = 0,
            y                   = 49540,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0012,
        ),
        ScenaNpcData(
            x                   = 32450,
            z                   = 0,
            y                   = 63980,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0006,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            x                   = 32530,
            z                   = 0,
            y                   = 66280,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            x                   = 29910,
            z                   = -2000,
            y                   = 47650,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            x                   = 35640,
            z                   = 0,
            y                   = 77750,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0007,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            x                   = 60000,
            z                   = 0,
            y                   = 50000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            x                   = 39000,
            z                   = -2000,
            y                   = 46000,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0005,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            x                   = 38010,
            z                   = 0,
            y                   = 21120,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 16,
            chipIndex           = 16,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 16,
            chipIndex           = 16,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 16,
            chipIndex           = 16,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 16,
            chipIndex           = 16,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 23,
            chipIndex           = 23,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 23,
            chipIndex           = 23,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 25,
            chipIndex           = 25,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 25,
            chipIndex           = 25,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 12860,
            z                   = 0,
            y                   = 47520,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 18,
            chipIndex           = 18,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            x                   = 12860,
            z                   = 0,
            y                   = 44370,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 18,
            chipIndex           = 18,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0014,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 19,
            chipIndex           = 19,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 20,
            chipIndex           = 20,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 29380,
            z                   = -2000,
            y                   = 35460,
            direction           = 318,
            word_0E             = 0,
            dword_10            = 22,
            chipIndex           = 22,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0008,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            x                   = 37390,
            z                   = -2000,
            y                   = 58930,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0015,
        ),
        ScenaNpcData(
            x                   = 84080,
            z                   = 0,
            y                   = 28010,
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
            x                   = -3490,
            z                   = 0,
            y                   = 46180,
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

# id: 0x10003 offset: 0x512
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = 52160,
            z           = 0,
            y           = 12900,
            word_0C     = 0x00B4,
            word_0E     = 0x0019,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0F3D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 31950,
            z           = 0,
            y           = 19680,
            word_0C     = 0x00B4,
            word_0E     = 0x0017,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0F3C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 15470,
            z           = 0,
            y           = 14340,
            word_0C     = 0x00B4,
            word_0E     = 0x001B,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0F3E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 21240,
            z           = 0,
            y           = 45950,
            word_0C     = 0x00B4,
            word_0E     = 0x0017,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0F3C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 15510,
            z           = 0,
            y           = 81080,
            word_0C     = 0x00B4,
            word_0E     = 0x0019,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0F3D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 34060,
            z           = -2000,
            y           = 46430,
            word_0C     = 0x00B4,
            word_0E     = 0x0019,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0F3D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 33470,
            z           = 0,
            y           = 66230,
            word_0C     = 0x00B4,
            word_0E     = 0x0010,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0F3F,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 62710,
            z           = 0,
            y           = 50010,
            word_0C     = 0x00B4,
            word_0E     = 0x0017,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0F3C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 63430,
            z           = 0,
            y           = 79810,
            word_0C     = 0x00B4,
            word_0E     = 0x001B,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0F3E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x60E
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 12290,
            y           = -1000,
            z           = 47300,
            range       = 14900,
            dword_10    = 0x000007D0,
            dword_14    = 0x0000AE38,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000055,
        ),
        ScenaEventData(
            x           = 12600,
            y           = -2000,
            z           = 44600,
            range       = 14000,
            dword_10    = 0x000007D0,
            dword_14    = 0x0000B98C,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000016,
        ),
        ScenaEventData(
            x           = 13400,
            y           = -1000,
            z           = 24000,
            range       = 18060,
            dword_10    = 0x000007D0,
            dword_14    = 0x0000625C,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000032,
        ),
        ScenaEventData(
            x           = 26000,
            y           = -1000,
            z           = 11270,
            range       = 26800,
            dword_10    = 0x000007D0,
            dword_14    = 0x000036F6,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000033,
        ),
        ScenaEventData(
            x           = 47400,
            y           = -1000,
            z           = 11070,
            range       = 49000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00003A48,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000034,
        ),
        ScenaEventData(
            x           = 52060,
            y           = -1000,
            z           = 26000,
            range       = 54200,
            dword_10    = 0x000007D0,
            dword_14    = 0x00007918,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000037,
        ),
        ScenaEventData(
            x           = 52060,
            y           = -1000,
            z           = 61000,
            range       = 54200,
            dword_10    = 0x000007D0,
            dword_14    = 0x000101D0,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000038,
        ),
        ScenaEventData(
            x           = 43200,
            y           = -1000,
            z           = 82000,
            range       = 41450,
            dword_10    = 0x000007D0,
            dword_14    = 0x000136F0,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000045,
        ),
        ScenaEventData(
            x           = 27430,
            y           = -1000,
            z           = 82000,
            range       = 26100,
            dword_10    = 0x000007D0,
            dword_14    = 0x00013880,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000046,
        ),
        ScenaEventData(
            x           = 13400,
            y           = -1000,
            z           = 68000,
            range       = 18060,
            dword_10    = 0x000007D0,
            dword_14    = 0x00010E3C,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000004B,
        ),
        ScenaEventData(
            x           = 41180,
            y           = 0,
            z           = 74060,
            range       = 1000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000056,
        ),
        ScenaEventData(
            x           = 53030,
            y           = 0,
            z           = 67260,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000056,
        ),
        ScenaEventData(
            x           = 53150,
            y           = 0,
            z           = 59630,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000057,
        ),
        ScenaEventData(
            x           = 48380,
            y           = 0,
            z           = 45960,
            range       = 1000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000057,
        ),
        ScenaEventData(
            x           = 52870,
            y           = 0,
            z           = 32110,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000057,
        ),
        ScenaEventData(
            x           = 53030,
            y           = 0,
            z           = 24850,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000058,
        ),
        ScenaEventData(
            x           = 47120,
            y           = 0,
            z           = 19010,
            range       = 1000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000058,
        ),
        ScenaEventData(
            x           = 22030,
            y           = 0,
            z           = 25660,
            range       = 1000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000059,
        ),
        ScenaEventData(
            x           = 22010,
            y           = 0,
            z           = 67170,
            range       = 1000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000005A,
        ),
    )

# id: 0x10005 offset: 0x86E
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 13480,
            triggerZ            = 0,
            triggerY            = 45900,
            triggerRange        = 700,
            actorX              = 13480,
            actorZ              = 1500,
            actorY              = 46000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0017,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 66600,
            triggerZ            = 0,
            triggerY            = 27910,
            triggerRange        = 700,
            actorX              = 66600,
            actorZ              = 1500,
            actorY              = 27910,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0018,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 17020,
            triggerZ            = 0,
            triggerY            = 22130,
            triggerRange        = 700,
            actorX              = 17000,
            actorZ              = 1500,
            actorY              = 22000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x002E,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 16940,
            triggerZ            = 0,
            triggerY            = 16040,
            triggerRange        = 700,
            actorX              = 17000,
            actorZ              = 1500,
            actorY              = 16000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0030,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 57010,
            triggerZ            = 0,
            triggerY            = 14090,
            triggerRange        = 700,
            actorX              = 56980,
            actorZ              = 1500,
            actorY              = 14000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0035,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 57730,
            triggerZ            = 0,
            triggerY            = 36050,
            triggerRange        = 700,
            actorX              = 58000,
            actorZ              = 1500,
            actorY              = 36000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0039,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 58000,
            triggerZ            = 0,
            triggerY            = 39920,
            triggerRange        = 700,
            actorX              = 58000,
            actorZ              = 1500,
            actorY              = 40110,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x003B,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 59010,
            triggerZ            = 0,
            triggerY            = 45880,
            triggerRange        = 700,
            actorX              = 59000,
            actorZ              = 1500,
            actorY              = 46040,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x003D,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 57910,
            triggerZ            = 0,
            triggerY            = 51930,
            triggerRange        = 700,
            actorX              = 58000,
            actorZ              = 1500,
            actorY              = 51970,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x003F,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 49150,
            triggerZ            = 0,
            triggerY            = 79920,
            triggerRange        = 700,
            actorX              = 48980,
            actorZ              = 1500,
            actorY              = 79890,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0043,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 17000,
            triggerZ            = 0,
            triggerY            = 77050,
            triggerRange        = 700,
            actorX              = 17000,
            actorZ              = 1500,
            actorY              = 76930,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0047,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 16960,
            triggerZ            = 0,
            triggerY            = 71100,
            triggerRange        = 700,
            actorX              = 17000,
            actorZ              = 1500,
            actorY              = 71000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0049,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0xA1E
@scena.Code('PreInit')
def PreInit():
    ExecExpressionWithValue(
        0x000A,
        0x28,
        (
            (Expr.PushLong, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_A3D',
    )

    OP_B5(0x00)

    def _loc_A3D(): pass

    label('loc_A3D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_AB9',
    )

    ClearChrFlags(0x001C, 0x0080)
    ClearChrFlags(0x001D, 0x0080)
    SetChrFlags(0x000E, 0x0080)
    SetChrFlags(0x000F, 0x0080)
    SetChrFlags(0x0011, 0x0080)
    SetChrPos(0x0010, 45800, 0, 46000, 0)
    CreateThread(0x0010, 0x00, 0x00, 0x0004)
    ClearChrFlags(0x0021, 0x0080)
    SetChrPos(0x000C, 36500, 0, 70920, 225)
    ClearChrFlags(0x000C, 0x0080)
    CreateThread(0x000C, 0x00, 0x06, 0x0002)
    SetChrPos(0x000D, 35500, 0, 69860, 45)
    ClearChrFlags(0x000D, 0x0080)
    CreateThread(0x000D, 0x00, 0x06, 0x0002)
    OP_B5(0x00)

    Jump('loc_BC4')

    def _loc_AB9(): pass

    label('loc_AB9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 1, 0x2001)),
            Expr.Return,
        ),
        'loc_AD7',
    )

    SetChrFlags(0x000E, 0x0080)
    SetChrFlags(0x000F, 0x0080)
    SetChrFlags(0x0010, 0x0080)
    SetChrFlags(0x0011, 0x0080)

    Jump('loc_BC4')

    def _loc_AD7(): pass

    label('loc_AD7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_AF7',
    )

    SetChrFlags(0x000E, 0x0080)
    SetChrFlags(0x000F, 0x0080)
    SetChrFlags(0x0010, 0x0080)
    SetChrFlags(0x0011, 0x0080)
    OP_B5(0x00)

    Jump('loc_BC4')

    def _loc_AF7(): pass

    label('loc_AF7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_B37',
    )

    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    SetChrFlags(0x000F, 0x0080)
    SetChrPos(0x0011, 46910, 0, 52960, 180)
    SetChrPos(0x0010, 22070, 0, 28390, 0)

    Jump('loc_BC4')

    def _loc_B37(): pass

    label('loc_B37')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0244, 1, 0x1221)),
            Expr.Return,
        ),
        'loc_B97',
    )

    SetChrPos(0x0010, 20410, 0, 28400, 53)
    TerminateThread(0x0011, 0xFF)
    SetChrPos(0x0011, 40830, -2000, 42670, 270)
    CreateThread(0x0011, 0x00, 0x06, 0x0002)
    TerminateThread(0x000F, 0xFF)
    SetChrFlags(0x000F, 0x0010)
    SetChrFlags(0x000F, 0x0004)
    SetChrChipByIndex(0x000F, 9)
    SetChrPos(0x000F, 33280, 200, 79020, 180)
    ClearChrFlags(0x0020, 0x0080)

    Jump('loc_BC4')

    def _loc_B97(): pass

    label('loc_B97')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 6, 0x121E)),
            Expr.Return,
        ),
        'loc_BB0',
    )

    OP_26(190)
    ClearChrFlags(0x0012, 0x0080)
    CreateThread(0x0010, 0x00, 0x00, 0x0003)

    Jump('loc_BC4')

    def _loc_BB0(): pass

    label('loc_BB0')

    SetChrFlags(0x000E, 0x0080)
    SetChrFlags(0x000F, 0x0080)
    SetChrFlags(0x0010, 0x0080)
    SetChrFlags(0x0011, 0x0080)

    def _loc_BC4(): pass

    label('loc_BC4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021F, 6, 0x10FE)),
            Expr.Return,
        ),
        'loc_CD7',
    )

    OP_A3(0x10FE)
    SetMapFlags(0x10000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_BEF',
    )

    OP_A3(0x10F0)
    OP_B5(0x00)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x6E),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, 0x002A)

    Jump('loc_CD4')

    def _loc_BEF(): pass

    label('loc_BEF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_C0B',
    )

    OP_A3(0x10F1)
    OP_B5(0x00)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x6E),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, 0x002D)

    Jump('loc_CD4')

    def _loc_C0B(): pass

    label('loc_C0B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 2, 0x10F2)),
            Expr.Return,
        ),
        'loc_C1C',
    )

    OP_A3(0x10F2)
    Event(0, 0x002F)

    Jump('loc_CD4')

    def _loc_C1C(): pass

    label('loc_C1C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 3, 0x10F3)),
            Expr.Return,
        ),
        'loc_C2D',
    )

    OP_A3(0x10F3)
    Event(0, 0x0031)

    Jump('loc_CD4')

    def _loc_C2D(): pass

    label('loc_C2D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 4, 0x10F4)),
            Expr.Return,
        ),
        'loc_C3E',
    )

    OP_A3(0x10F4)
    Event(0, 0x0036)

    Jump('loc_CD4')

    def _loc_C3E(): pass

    label('loc_C3E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 5, 0x10F5)),
            Expr.Return,
        ),
        'loc_C4F',
    )

    OP_A3(0x10F5)
    Event(0, 0x003A)

    Jump('loc_CD4')

    def _loc_C4F(): pass

    label('loc_C4F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 6, 0x10F6)),
            Expr.Return,
        ),
        'loc_C60',
    )

    OP_A3(0x10F6)
    Event(0, 0x003C)

    Jump('loc_CD4')

    def _loc_C60(): pass

    label('loc_C60')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 7, 0x10F7)),
            Expr.Return,
        ),
        'loc_C71',
    )

    OP_A3(0x10F7)
    Event(0, 0x003E)

    Jump('loc_CD4')

    def _loc_C71(): pass

    label('loc_C71')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021F, 0, 0x10F8)),
            Expr.Return,
        ),
        'loc_C82',
    )

    OP_A3(0x10F8)
    Event(0, 0x0040)

    Jump('loc_CD4')

    def _loc_C82(): pass

    label('loc_C82')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021F, 1, 0x10F9)),
            Expr.Return,
        ),
        'loc_C93',
    )

    OP_A3(0x10F9)
    Event(0, 0x0041)

    Jump('loc_CD4')

    def _loc_C93(): pass

    label('loc_C93')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021F, 2, 0x10FA)),
            Expr.Return,
        ),
        'loc_CA4',
    )

    OP_A3(0x10FA)
    Event(0, 0x0042)

    Jump('loc_CD4')

    def _loc_CA4(): pass

    label('loc_CA4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021F, 3, 0x10FB)),
            Expr.Return,
        ),
        'loc_CB5',
    )

    OP_A3(0x10FB)
    Event(0, 0x0044)

    Jump('loc_CD4')

    def _loc_CB5(): pass

    label('loc_CB5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021F, 4, 0x10FC)),
            Expr.Return,
        ),
        'loc_CC6',
    )

    OP_A3(0x10FC)
    Event(0, 0x0048)

    Jump('loc_CD4')

    def _loc_CC6(): pass

    label('loc_CC6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021F, 5, 0x10FD)),
            Expr.Return,
        ),
        'loc_CD4',
    )

    OP_A3(0x10FD)
    Event(0, 0x004A)

    def _loc_CD4(): pass

    label('loc_CD4')

    Jump('loc_E8E')

    def _loc_CD7(): pass

    label('loc_CD7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_CF6',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x51),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 0x001F)

    Jump('loc_E8E')

    def _loc_CF6(): pass

    label('loc_CF6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_D15',
    )

    OP_A3(0x10F1)
    SetMapFlags(0x10000000)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x6E),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, 0x0021)

    Jump('loc_E8E')

    def _loc_D15(): pass

    label('loc_D15')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 2, 0x10F2)),
            Expr.Return,
        ),
        'loc_D2B',
    )

    OP_A3(0x10F2)
    SetMapFlags(0x10000000)
    Event(0, 0x004D)

    Jump('loc_E8E')

    def _loc_D2B(): pass

    label('loc_D2B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 3, 0x10F3)),
            Expr.Return,
        ),
        'loc_D4A',
    )

    OP_A3(0x10F3)
    SetMapFlags(0x10000000)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x59),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, 0x004E)

    Jump('loc_E8E')

    def _loc_D4A(): pass

    label('loc_D4A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 4, 0x10F4)),
            Expr.Return,
        ),
        'loc_D62',
    )

    OP_A3(0x10F4)
    OP_B5(0x00)
    SetMapFlags(0x10000000)
    Event(0, 0x0052)

    Jump('loc_E8E')

    def _loc_D62(): pass

    label('loc_D62')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 6, 0x202E)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0404, 2, 0x2022)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0404, 3, 0x2023)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0404, 5, 0x2025)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0404, 6, 0x2026)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 0, 0x2028)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 1, 0x2029)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 3, 0x202B)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 5, 0x202D)),
            Expr.Nez64,
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x66),
            Expr.Equ,
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x65),
            Expr.Equ,
            Expr.Or,
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x69),
            Expr.Equ,
            Expr.Or,
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x67),
            Expr.Equ,
            Expr.Or,
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x6C),
            Expr.Equ,
            Expr.Or,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_DC3',
    )

    SetMapFlags(0x10000000)
    Event(0, 0x0051)

    Jump('loc_E8E')

    def _loc_DC3(): pass

    label('loc_DC3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0244, 0, 0x1220)),
            (Expr.TestScenaFlags, ScenaFlag(0x0246, 2, 0x1232)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0246, 3, 0x1233)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0246, 4, 0x1234)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0244, 1, 0x1221)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_E8E',
    )

    TerminateThread(0x0010, 0xFF)
    SetChrPos(0x0010, 20410, 0, 28400, 53)
    CreateThread(0x0010, 0x00, 0x06, 0x0002)
    TerminateThread(0x0011, 0xFF)
    SetChrPos(0x0011, 40830, -2000, 42670, 270)
    CreateThread(0x0011, 0x00, 0x06, 0x0002)
    TerminateThread(0x000F, 0xFF)
    SetChrFlags(0x000F, 0x0010)
    SetChrFlags(0x000F, 0x0004)
    SetChrChipByIndex(0x000F, 9)
    SetChrPos(0x000F, 33280, 200, 79020, 180)
    SetChrFlags(0x0012, 0x0080)
    ClearChrFlags(0x0020, 0x0080)
    OP_A2(0x1221)

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000065, 'loc_E64'),
        (0x00000067, 'loc_E6B'),
        (0x00000068, 'loc_E72'),
        (0x00000069, 'loc_E79'),
        (0x0000006A, 'loc_E80'),
        (0x0000006B, 'loc_E87'),
        (-1, 'loc_E8E'),
    )

    def _loc_E64(): pass

    label('loc_E64')

    Event(0, 0x0019)

    Jump('loc_E8E')

    def _loc_E6B(): pass

    label('loc_E6B')

    Event(0, 0x001A)

    Jump('loc_E8E')

    def _loc_E72(): pass

    label('loc_E72')

    Event(0, 0x001B)

    Jump('loc_E8E')

    def _loc_E79(): pass

    label('loc_E79')

    Event(0, 0x001D)

    Jump('loc_E8E')

    def _loc_E80(): pass

    label('loc_E80')

    Event(0, 0x001C)

    Jump('loc_E8E')

    def _loc_E87(): pass

    label('loc_E87')

    Event(0, 0x001E)

    Jump('loc_E8E')

    def _loc_E8E(): pass

    label('loc_E8E')

    Return()

# id: 0x0001 offset: 0xE8F
@scena.Code('Init')
def Init():
    OP_16(0x02, 0x00000FA0, 0xFFFEA840, 0xFFFEBFB0, 0x0023004C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0244, 1, 0x1221)),
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_EB9',
    )

    OP_B1('t2500_y')

    Jump('loc_EC2')

    def _loc_EB9(): pass

    label('loc_EB9')

    OP_B1('t2500_n')

    def _loc_EC2(): pass

    label('loc_EC2')

    OP_64(0x02, 0x0001)
    OP_64(0x03, 0x0001)
    OP_64(0x04, 0x0001)
    OP_64(0x05, 0x0001)
    OP_64(0x06, 0x0001)
    OP_64(0x07, 0x0001)
    OP_64(0x08, 0x0001)
    OP_64(0x09, 0x0001)
    OP_64(0x0A, 0x0001)
    OP_64(0x0B, 0x0001)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1005',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_F22',
    )

    OP_B5(0x00)
    OP_6F(0x0021, 60)
    OP_72(0x0021, 0x0010)
    OP_64(0x00, 0x0001)
    OP_6F(0x0022, 60)
    OP_72(0x0022, 0x0010)
    OP_64(0x01, 0x0001)

    Jump('loc_1002')

    def _loc_F22(): pass

    label('loc_F22')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0403, 7, 0x201F)),
            Expr.Return,
        ),
        'loc_F71',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x59),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetMapFlags(0x02000000)
    OP_6F(0x0021, 60)
    OP_72(0x0021, 0x0010)
    OP_64(0x00, 0x0001)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0404, 0, 0x2020)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_F5E',
    )

    OP_6F(0x0022, 0)
    OP_72(0x0022, 0x0010)

    Jump('loc_F6E')

    def _loc_F5E(): pass

    label('loc_F5E')

    OP_6F(0x0022, 60)
    OP_72(0x0022, 0x0010)
    OP_64(0x01, 0x0001)

    def _loc_F6E(): pass

    label('loc_F6E')

    Jump('loc_1002')

    def _loc_F71(): pass

    label('loc_F71')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 3, 0x2013)),
            Expr.Return,
        ),
        'loc_FF2',
    )

    OP_B5(0x00)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x6E),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetMapFlags(0x02000000)
    OP_6F(0x0021, 0)
    OP_72(0x0021, 0x0010)
    OP_64(0x00, 0x0001)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0404, 0, 0x2020)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_FAF',
    )

    OP_6F(0x0022, 0)
    OP_72(0x0022, 0x0010)

    Jump('loc_FBF')

    def _loc_FAF(): pass

    label('loc_FAF')

    OP_6F(0x0022, 60)
    OP_72(0x0022, 0x0010)
    OP_64(0x01, 0x0001)

    def _loc_FBF(): pass

    label('loc_FBF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0403, 7, 0x201F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_FEF',
    )

    OP_65(0x02, 0x0001)
    OP_65(0x03, 0x0001)
    OP_65(0x04, 0x0001)
    OP_65(0x05, 0x0001)
    OP_65(0x06, 0x0001)
    OP_65(0x07, 0x0001)
    OP_65(0x08, 0x0001)
    OP_65(0x09, 0x0001)
    OP_65(0x0A, 0x0001)
    OP_65(0x0B, 0x0001)

    def _loc_FEF(): pass

    label('loc_FEF')

    Jump('loc_1002')

    def _loc_FF2(): pass

    label('loc_FF2')

    OP_6F(0x0021, 0)
    OP_72(0x0021, 0x0010)
    OP_64(0x00, 0x0001)

    def _loc_1002(): pass

    label('loc_1002')

    Jump('loc_1053')

    def _loc_1005(): pass

    label('loc_1005')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 6, 0x121E)),
            Expr.Return,
        ),
        'loc_101F',
    )

    OP_64(0x00, 0x0001)
    OP_72(0x0021, 0x0010)
    OP_6F(0x0021, 60)

    Jump('loc_1037')

    def _loc_101F(): pass

    label('loc_101F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_102D',
    )

    OP_64(0x00, 0x0001)

    Jump('loc_1037')

    def _loc_102D(): pass

    label('loc_102D')

    OP_72(0x0021, 0x0010)
    OP_72(0x002D, 0x0004)

    def _loc_1037(): pass

    label('loc_1037')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0244, 3, 0x1223)),
            Expr.Return,
        ),
        'loc_104C',
    )

    OP_64(0x01, 0x0001)
    OP_6F(0x0022, 60)

    Jump('loc_1053')

    def _loc_104C(): pass

    label('loc_104C')

    OP_6F(0x0022, 0)

    def _loc_1053(): pass

    label('loc_1053')

    OP_71(0x0009, 0x0004)
    OP_71(0x000A, 0x0004)
    OP_71(0x000B, 0x0004)
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
    OP_71(0x0023, 0x0004)
    OP_71(0x0024, 0x0004)
    OP_71(0x0025, 0x0004)
    OP_71(0x0026, 0x0004)
    OP_71(0x0027, 0x0004)
    OP_71(0x0028, 0x0004)
    OP_71(0x0029, 0x0004)
    OP_71(0x002A, 0x0004)
    OP_71(0x002B, 0x0004)
    OP_71(0x002C, 0x0004)

    ExecExpressionWithValue(
        0x0025,
        0x24,
        (
            (Expr.PushLong, 0xC3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0027,
        0x24,
        (
            (Expr.PushLong, 0xC3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x002A,
        0x24,
        (
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x002B,
        0x24,
        (
            (Expr.PushLong, 0xC3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0002 offset: 0x112A
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_113F',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('ReInit')

    def _loc_113F(): pass

    label('loc_113F')

    Return()

# id: 0x0003 offset: 0x1140
@scena.Code('func_03_1140')
def func_03_1140():
    OP_8E(0x00FE, 60000, 0, 60800, 5000, 0x00)
    OP_8E(0x00FE, 59500, 0, 61600, 5000, 0x00)
    OP_8E(0x00FE, 59000, 0, 62400, 5000, 0x00)
    OP_8E(0x00FE, 58500, 0, 62800, 5000, 0x00)
    OP_8E(0x00FE, 58000, 0, 63000, 5000, 0x00)
    def _loc_11A4(): pass

    label('loc_11A4')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1376',
    )

    OP_8E(0x00FE, 48000, 0, 63000, 5000, 0x00)
    OP_8E(0x00FE, 47500, 0, 62800, 5000, 0x00)
    OP_8E(0x00FE, 47000, 0, 62400, 5000, 0x00)
    OP_8E(0x00FE, 46500, 0, 61600, 5000, 0x00)
    OP_8E(0x00FE, 46000, 0, 60800, 5000, 0x00)
    OP_62(0x00FE, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_8E(0x00FE, 46000, 0, 31000, 5000, 0x00)
    OP_8E(0x00FE, 46500, 0, 30200, 5000, 0x00)
    OP_8E(0x00FE, 47000, 0, 29400, 5000, 0x00)
    OP_8E(0x00FE, 47500, 0, 29000, 5000, 0x00)
    OP_8E(0x00FE, 48000, 0, 28800, 5000, 0x00)
    OP_8E(0x00FE, 58000, 0, 28800, 5000, 0x00)
    OP_62(0x00FE, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_8E(0x00FE, 58500, 0, 29000, 5000, 0x00)
    OP_8E(0x00FE, 59000, 0, 29400, 5000, 0x00)
    OP_8E(0x00FE, 59500, 0, 30200, 5000, 0x00)
    OP_8E(0x00FE, 60000, 0, 31000, 5000, 0x00)
    OP_8E(0x00FE, 60000, 0, 60800, 5000, 0x00)
    OP_62(0x00FE, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_8E(0x00FE, 59500, 0, 61600, 5000, 0x00)
    OP_8E(0x00FE, 59000, 0, 62400, 5000, 0x00)
    OP_8E(0x00FE, 58500, 0, 62800, 5000, 0x00)
    OP_8E(0x00FE, 58000, 0, 63000, 5000, 0x00)

    Jump('loc_11A4')

    def _loc_1376(): pass

    label('loc_1376')

    Return()

# id: 0x0004 offset: 0x1377
@scena.Code('func_04_1377')
def func_04_1377():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_13D3',
    )

    OP_8E(0x00FE, 46000, 0, 63950, 2000, 0x00)
    OP_8E(0x00FE, 22140, 0, 63950, 2000, 0x00)
    OP_8E(0x00FE, 22140, 0, 27950, 2000, 0x00)
    OP_8E(0x00FE, 46000, 0, 27950, 2000, 0x00)

    Jump('func_04_1377')

    def _loc_13D3(): pass

    label('loc_13D3')

    Return()

# id: 0x0005 offset: 0x13D4
@scena.Code('func_05_13D4')
def func_05_13D4():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_1401',
    )

    def _loc_13DB(): pass

    label('loc_13DB')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_13FE',
    )

    OP_8D(0x00FE, 48790, 55520, 45390, 51020, 1000)

    Jump('loc_13DB')

    def _loc_13FE(): pass

    label('loc_13FE')

    Jump('loc_16DD')

    def _loc_1401(): pass

    label('loc_1401')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_16DD',
    )

    Sleep(1500)

    OP_8B(0x00FE, 0x00009858, 0x0000DAC0, 0x0190)
    OP_8E(0x00FE, 39000, -2000, 56000, 2000, 0x00)
    OP_8E(0x00FE, 39000, -2000, 56000, 2000, 0x00)
    OP_8E(0x00FE, 38000, -2000, 57000, 2000, 0x00)
    OP_8E(0x00FE, 35000, -2000, 57000, 2000, 0x00)
    OP_8E(0x00FE, 34000, -2000, 58000, 2000, 0x00)
    OP_8E(0x00FE, 34000, 0, 63000, 2000, 0x00)
    OP_8E(0x00FE, 33000, 0, 64000, 2000, 0x00)
    OP_8E(0x00FE, 24000, 0, 64000, 2000, 0x00)
    OP_8E(0x00FE, 23000, 0, 63000, 2000, 0x00)
    OP_8E(0x00FE, 23000, 0, 46000, 2000, 0x00)
    OP_8B(0x00FE, 0x00004B64, 0x0000B3B0, 0x0190)
    Sleep(500)

    OP_8B(0x00FE, 0x00007080, 0x0000A3AC, 0x0190)
    Sleep(200)

    OP_8B(0x00FE, 0x00007080, 0x0000C3B4, 0x0190)
    Sleep(1500)

    OP_8B(0x00FE, 0x000071AC, 0x0000B3B0, 0x0190)
    OP_8E(0x00FE, 28000, -2000, 46000, 2000, 0x00)
    OP_8E(0x00FE, 29000, -2000, 45000, 2000, 0x00)
    OP_8E(0x00FE, 29000, -2000, 36000, 2000, 0x00)
    OP_8E(0x00FE, 30000, -2000, 35000, 2000, 0x00)
    OP_8E(0x00FE, 33000, -2000, 35000, 2000, 0x00)
    OP_8E(0x00FE, 34000, -2000, 34000, 2000, 0x00)
    OP_8E(0x00FE, 34000, 0, 29000, 2000, 0x00)
    OP_8B(0x00FE, 0x00008CA0, 0x00007148, 0x0190)
    Sleep(500)

    OP_8B(0x00FE, 0x00007D00, 0x00007148, 0x0190)
    Sleep(800)

    OP_8B(0x00FE, 0x00009470, 0x000061A8, 0x0190)
    Sleep(1000)

    OP_8E(0x00FE, 38000, 0, 25000, 2000, 0x00)
    Sleep(500)

    OP_8B(0x00FE, 0x0000884A, 0x00005096, 0x0190)
    Sleep(500)

    OP_8B(0x00FE, 0x0000A028, 0x000055F0, 0x0190)
    Sleep(1000)

    OP_8B(0x00FE, 0x0000A028, 0x00006D60, 0x0190)
    OP_8E(0x00FE, 41000, 0, 28000, 2000, 0x00)
    OP_8E(0x00FE, 44000, 0, 28000, 2000, 0x00)
    OP_8E(0x00FE, 45000, 0, 29000, 2000, 0x00)
    OP_8E(0x00FE, 45000, 0, 46000, 2000, 0x00)
    OP_8B(0x00FE, 0x00004B64, 0x0000B3B0, 0x0190)
    Sleep(500)

    OP_8B(0x00FE, 0x00007080, 0x0000A3AC, 0x0190)
    Sleep(200)

    OP_8B(0x00FE, 0x00007080, 0x0000C3B4, 0x0190)
    Sleep(1500)

    OP_8B(0x00FE, 0x000071AC, 0x0000B3B0, 0x0190)
    OP_8E(0x00FE, 39000, -2000, 46000, 2000, 0x00)

    Jump('loc_1401')

    def _loc_16DD(): pass

    label('loc_16DD')

    Return()

# id: 0x0006 offset: 0x16DE
@scena.Code('func_06_16DE')
def func_06_16DE():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1701',
    )

    OP_8D(0x00FE, 27793, 65500, 35900, 62530, 2000)

    Jump('func_06_16DE')

    def _loc_1701(): pass

    label('loc_1701')

    Return()

# id: 0x0007 offset: 0x1702
@scena.Code('func_07_1702')
def func_07_1702():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1725',
    )

    OP_8D(0x00FE, 34220, 72290, 36840, 78320, 2000)

    Jump('func_07_1702')

    def _loc_1725(): pass

    label('loc_1725')

    Return()

# id: 0x0008 offset: 0x1726
@scena.Code('func_08_1726')
def func_08_1726():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1749',
    )

    OP_8D(0x00FE, 27610, 33720, 30640, 36510, 2000)

    Jump('func_08_1726')

    def _loc_1749(): pass

    label('loc_1749')

    Return()

# id: 0x0009 offset: 0x174A
@scena.Code('func_09_174A')
def func_09_174A():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0244, 1, 0x1221)),
            Expr.Return,
        ),
        'loc_17FF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_17AD',
    )

    ChrTalk(
        0x00FE,
        (
            '哈，学院祭真开心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，等到学院祭到来之前\n',
            '就先享受一下社团活动吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17FF')

    def _loc_17AD(): pass

    label('loc_17AD')

    OP_A2(0x0008)

    ChrTalk(
        0x00FE,
        (
            '哈，学院祭真开心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '能再那样和大家一起热闹\n',
            '不知要等到什么时候了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_17FF(): pass

    label('loc_17FF')

    TalkEnd(0x00FE)

    Return()

# id: 0x000A offset: 0x1803
@scena.Code('func_0A_1803')
def func_0A_1803():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x024C, 2, 0x1262)),
            Expr.Return,
        ),
        'loc_18E3',
    )

    ChrTalk(
        0x00FE,
        (
            '#0040210976V#035F呵，王立学院的女子宿舍啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040210977V可爱的花蕾们\n',
            '一定等不及了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040210978V#035F呵呵……呵呵呵呵…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010210979V#1019F（……绝对不带你去。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D38')

    def _loc_18E3(): pass

    label('loc_18E3')

    OP_22(0x00BE, 0x00, 0x64)
    OP_99(0x00FE, 0x00, 0x04, 0x00000578)
    OP_99(0x00FE, 0x04, 0x00, 0x000001F4)
    Sleep(1000)

    OP_A2(0x1262)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_197C',
    )

    ChrTalk(
        0x00FE,
        (
            '#0040210980V#035F呵，这不是艾丝蒂尔吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010210981V#1018F怎样？奥利维尔。\n',
            '打听有进展吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    Jump('loc_19D7')

    def _loc_197C(): pass

    label('loc_197C')

    ChrTalk(
        0x00FE,
        (
            '#0040210982V#035F呼，这不是公主殿下吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060210983V#040F辛苦了。\n',
            '打听有进展吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_19D7(): pass

    label('loc_19D7')

    ChrTalk(
        0x00FE,
        (
            '#0040210984V#035F哈哈，这件事\n',
            '委托给朵洛希了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040210985V话说回来，我碰巧听说\n',
            '这里有女学生的宿舍呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040210986V我正急着\n',
            '找那个呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060210987V#044F啊，找女子宿舍……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010210988V#1004F找那个干什么啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210989V#1015F不过，总觉～得\n',
            '能猜到理由……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#0040210990V#031F呵，这还用说吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040210991V为了守护少女的卧室，\n',
            '我要立即赶去才行啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010210992V#1007F唉，果然来这套。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060210993V#045F意、意料之中的行动啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0040210994V#035F若等危险至极的魔掌\n',
            '伸长之后就为时已晚了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x22, 0x24, 0x000000FA, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '#0040210995V#031F对了。\n',
            '我说，艾丝蒂尔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040210996V你以前，好像在这个学院\n',
            '里待过吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040210997V可以的话，能不能\n',
            '带我去宿舍？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010210998V#1016F唔、唔～………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210999V#1016F现、现在有点忙，\n',
            '稍后再说吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211000V#1019F（被、被这家伙知道\n',
            '宿舍在哪就更危险了。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1D38(): pass

    label('loc_1D38')

    TalkEnd(0x00FE)

    Return()

# id: 0x000B offset: 0x1D3C
@scena.Code('func_0B_1D3C')
def func_0B_1D3C():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_1DCF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_1D73',
    )

    ChrTalk(
        0x00FE,
        (
            '这所学校真是\n',
            '什么学生都有啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1DCC')

    def _loc_1D73(): pass

    label('loc_1D73')

    OP_A2(0x0006)

    ChrTalk(
        0x00FE,
        (
            '昨天夜晚，我在校舍巡逻\n',
            '竟然发现有男生藏在教室。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '突然跑出来\n',
            '真是把我吓死了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1DCC(): pass

    label('loc_1DCC')

    Jump('loc_1E70')

    def _loc_1DCF(): pass

    label('loc_1DCF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0244, 1, 0x1221)),
            Expr.Return,
        ),
        'loc_1E25',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，看来\n',
            '操场好像没问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好了，待会儿还要\n',
            '检查各社团的备用品呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E70')

    def _loc_1E25(): pass

    label('loc_1E25')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 6, 0x121E)),
            Expr.Return,
        ),
        'loc_1E70',
    )

    ChrTalk(
        0x00FE,
        (
            '明天起\n',
            '就要开始社团活动了嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '正在检查\n',
            '操场有没有异常呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1E70(): pass

    label('loc_1E70')

    TalkEnd(0x00FE)

    Return()

# id: 0x000C offset: 0x1E74
@scena.Code('func_0C_1E74')
def func_0C_1E74():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_1F3E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1EF4',
    )

    ChrTalk(
        0x00FE,
        (
            '啊，游击士们。\n',
            '真是辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们在这之后也要准备\n',
            '重新开课，开始变忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔，彼此加油啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0005)

    Jump('loc_1F3B')

    def _loc_1EF4(): pass

    label('loc_1EF4')

    ChrTalk(
        0x00FE,
        (
            '我们在这之后也要准备\n',
            '重新开课，开始变忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔，彼此加油啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1F3B(): pass

    label('loc_1F3B')

    Jump('loc_206F')

    def _loc_1F3E(): pass

    label('loc_1F3E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_1F90',
    )

    ChrTalk(
        0x00FE,
        (
            '好，今天起\n',
            '终于要重开社团了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '变迟钝的身体\n',
            '要努力重新锻炼啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_206F')

    def _loc_1F90(): pass

    label('loc_1F90')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0244, 2, 0x1222)),
            Expr.Return,
        ),
        'loc_1FA7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_1FA1',
    )

    Jump('loc_1FA4')

    def _loc_1FA1(): pass

    label('loc_1FA1')

    OP_A2(0x0005)

    def _loc_1FA4(): pass

    label('loc_1FA4')

    Jump('loc_206F')

    def _loc_1FA7(): pass

    label('loc_1FA7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0244, 1, 0x1221)),
            Expr.Return,
        ),
        'loc_1FFC',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，差不多要天黑了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为了明天开始的社团活动\n',
            '今天就早点休息吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_206F')

    def _loc_1FFC(): pass

    label('loc_1FFC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 6, 0x121E)),
            Expr.Return,
        ),
        'loc_206F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_2021',
    )

    ChrTalk(
        0x00FE,
        (
            '哎嘿、哎嘿……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_206F')

    def _loc_2021(): pass

    label('loc_2021')

    OP_A2(0x0005)
    SetChrFlags(0x00FE, 0x0010)

    ChrTalk(
        0x00FE,
        (
            '明天起是久违的\n',
            '社团活动嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要趁今天到处跑跑\n',
            '活动筋骨才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_206F(): pass

    label('loc_206F')

    TalkEnd(0x00FE)

    Return()

# id: 0x000D offset: 0x2073
@scena.Code('func_0D_2073')
def func_0D_2073():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_211C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_20C2',
    )

    ChrTalk(
        0x00FE,
        (
            '听说旧校舍\n',
            '潜伏着可疑的人物？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '像是小说成真一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2119')

    def _loc_20C2(): pass

    label('loc_20C2')

    OP_A2(0x0004)

    ChrTalk(
        0x00FE,
        (
            '刚才\n',
            '碰巧听说了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '听说旧校舍\n',
            '潜伏着可疑的人物？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '像是小说成真一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2119(): pass

    label('loc_2119')

    Jump('loc_22F5')

    def _loc_211C(): pass

    label('loc_211C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0244, 1, 0x1221)),
            Expr.Return,
        ),
        'loc_21F4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_217D',
    )

    ChrTalk(
        0x00FE,
        (
            '我想在休假中\n',
            '试着写写长篇小说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '打算以我们的学校\n',
            '这样的学院做为舞台。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_21F1')

    def _loc_217D(): pass

    label('loc_217D')

    OP_A2(0x0004)

    ChrTalk(
        0x00FE,
        (
            '我想在放假期间\n',
            '试着写写长篇小说呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '打算以我们的学校\n',
            '这样的学院做为舞台。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在正在考虑\n',
            '这个设定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_21F1(): pass

    label('loc_21F1')

    Jump('loc_22F5')

    def _loc_21F4(): pass

    label('loc_21F4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 6, 0x121E)),
            Expr.Return,
        ),
        'loc_22F5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_2263',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯～不过很有魅力呢。\n',
            '袭击学院的怪现象……之类的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在构思中的小说里\n',
            '说不定能用上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_22F5')

    def _loc_2263(): pass

    label('loc_2263')

    OP_A2(0x0004)

    ChrTalk(
        0x00FE,
        (
            '考试中的怪事……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不，没什么\n',
            '特别的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，很有魅力呢。\n',
            '袭击学院的怪现象……之类的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在构思中的小说里\n',
            '说不定能用上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_22F5(): pass

    label('loc_22F5')

    TalkEnd(0x00FE)

    Return()

# id: 0x000E offset: 0x22F9
@scena.Code('func_0E_22F9')
def func_0E_22F9():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_2395',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_2336',
    )

    ChrTalk(
        0x00FE,
        (
            '今天美术部的各位\n',
            '计划一起画素描哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2392')

    def _loc_2336(): pass

    label('loc_2336')

    OP_A2(0x0003)

    ChrTalk(
        0x00FE,
        (
            '今天美术部的各位\n',
            '计划一起画素描。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……不过还没人来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是不是来早了点呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2392(): pass

    label('loc_2392')

    Jump('loc_24D0')

    def _loc_2395(): pass

    label('loc_2395')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0244, 1, 0x1221)),
            Expr.Return,
        ),
        'loc_2448',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_23E2',
    )

    ChrTalk(
        0x00FE,
        (
            '好久没\n',
            '坐在画布前了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '感觉现在能\n',
            '画出漂亮的画呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2445')

    def _loc_23E2(): pass

    label('loc_23E2')

    OP_A2(0x0003)

    ChrTalk(
        0x00FE,
        (
            '哼哼哼～⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为了准备美术部的作品\n',
            '正在寻找题材呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哟，晚霞中的校舍\n',
            '说不定很不错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2445(): pass

    label('loc_2445')

    Jump('loc_24D0')

    def _loc_2448(): pass

    label('loc_2448')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 6, 0x121E)),
            Expr.Return,
        ),
        'loc_24D0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_248B',
    )

    ChrTalk(
        0x00FE,
        (
            '应该没什么特别的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我去问问其他人吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24D0')

    def _loc_248B(): pass

    label('loc_248B')

    OP_A2(0x0003)

    ChrTalk(
        0x00FE,
        (
            '考试期间中发生的\n',
            '怪事……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不，不知道。\n',
            '问问其它人吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_24D0(): pass

    label('loc_24D0')

    TalkEnd(0x00FE)

    Return()

# id: 0x000F offset: 0x24D4
@scena.Code('func_0F_24D4')
def func_0F_24D4():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_2A01',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0418, 5, 0x20C5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_24F0',
    )

    Call(0, 0x0011)
    OP_A2(0x20C5)

    Jump('loc_29FE')

    def _loc_24F0(): pass

    label('loc_24F0')

    If(
        (
            (Expr.Eval, "OP_29(0x007A, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_29B4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0418, 6, 0x20C6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2965',
    )

    ChrTalk(
        0x00FE,
        (
            '小姐要有\n',
            '广阔的视野才行……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '出身名门的人\n',
            '就有背负这名声的命运。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1015F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '哎呀，怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1008F嗯、嗯，基于职务上的理由\n',
            '有些事情想打听一下……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1015F（那个，结果……\n',
            '　相亲怎样了？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#1048F（慢着……\n',
            '　这哪算是职务上的话？)',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '（单纯是艾丝蒂尔\n',
            '　想知道吧。)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#1009F（有、有什么关系。\n',
            '　多少也和工作有点关联嘛。)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '（嗯，倒也无所谓……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '（……当然是大成功啦。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    ChrTurnDirection(0x0101, 0x00FE, 400)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#1004F（咦咦！？成功了！？）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1013F（那个，这么说来……\n',
            '　芙拉瑟，莫非……)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '（做事要循序渐进，\n',
            '　不可能一下子就订婚啦。)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '（单纯只是相互\n',
            '　都比较中意而已。)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1008F（这、这样啊……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1007F（呼～虽说是别人的事\n',
            '　还是禁不住着急起来了。)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_287A',
    )

    ChrTurnDirection(0x0103, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#027F（哎呀，为什么艾丝蒂尔\n',
            '　这么着急？)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#1013F（没、没什么深刻涵义啦。\n',
            '　只是因为我们同年……)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_290F')

    def _loc_287A(): pass

    label('loc_287A')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_290F',
    )

    ChrTurnDirection(0x0106, 0x0101, 400)

    ChrTalk(
        0x0106,
        (
            '#055F（啊？为什么你\n',
            '　看起来这么着急？)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrTurnDirection(0x0101, 0x0106, 400)

    ChrTalk(
        0x0101,
        (
            '#1013F（没、没什么深刻涵义，\n',
            '　只是因为我们同年……)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_290F(): pass

    label('loc_290F')

    ChrTalk(
        0x00FE,
        (
            '（暂时打算通过写信\n',
            '　来加深交流。)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '（所以说，订婚的话\n',
            '　还早得很吧。)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x20C6)

    Jump('loc_29B1')

    def _loc_2965(): pass

    label('loc_2965')

    ChrTalk(
        0x00FE,
        (
            '大小姐要有\n',
            '广阔的视野才行……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '出身名门的人\n',
            '就有背负这名声的命运。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_29B1(): pass

    label('loc_29B1')

    Jump('loc_29FE')

    def _loc_29B4(): pass

    label('loc_29B4')

    ChrTalk(
        0x00FE,
        (
            '小姐要有\n',
            '广阔的视野才行……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '出身名门的人\n',
            '就有背负这名声的命运。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_29FE(): pass

    label('loc_29FE')

    Jump('loc_2B6E')

    def _loc_2A01(): pass

    label('loc_2A01')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_2A77',
    )

    ChrTalk(
        0x00FE,
        (
            '（这次相亲的对象\n',
            '　帝国某贵族子弟……)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '（对方听说是王国留学中的才女，\n',
            '　马上就对小姐产生了兴趣。)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2B6E')

    def _loc_2A77(): pass

    label('loc_2A77')

    OP_A2(0x0002)

    ChrTalk(
        0x00FE,
        (
            '（芙拉瑟好像以为\n',
            '　得到了我国的许可……)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '（其实这次归国，一开始\n',
            '就预定到柏斯旅行的。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '（那边也有餐厅，\n',
            '　还有从帝国出发的定期船……)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '（作为跟帝国贵族的相亲会场，\n',
            '　确实是最理想的地方。)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '（…………不过这是秘密。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2B6E(): pass

    label('loc_2B6E')

    TalkEnd(0x00FE)

    Return()

# id: 0x0010 offset: 0x2B72
@scena.Code('func_10_2B72')
def func_10_2B72():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_2C4B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0418, 5, 0x20C5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2B8E',
    )

    Call(0, 0x0011)
    OP_A2(0x20C5)

    Jump('loc_2C48')

    def _loc_2B8E(): pass

    label('loc_2B8E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_2BF4',
    )

    ChrTalk(
        0x00FE,
        (
            '不、不管怎样……\n',
            '今天真是帮大忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '王国好像有危机，\n',
            '不过大家都决心坚守学院生活。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2C48')

    def _loc_2BF4(): pass

    label('loc_2BF4')

    ChrTalk(
        0x000C,
        (
            '自己的人生被人操纵，\n',
            '没人会感到高兴的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '我不可能像蕾娜那样\n',
            '想得那么乐观。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2C48(): pass

    label('loc_2C48')

    Jump('loc_2D20')

    def _loc_2C4B(): pass

    label('loc_2C4B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_2C95',
    )

    ChrTalk(
        0x00FE,
        (
            '归国前会在柏斯城里\n',
            '稍作停留。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵，蕾娜\n',
            '也有优点嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2D20')

    def _loc_2C95(): pass

    label('loc_2C95')

    OP_A2(0x0001)

    ChrTalk(
        0x00FE,
        (
            '嘿嘿……太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '归省前会在柏斯城里\n',
            '稍作停留。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然没几天,\n',
            '但足够享受市内旅游了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这也多亏蕾娜\n',
            '和国家进行了交涉呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2D20(): pass

    label('loc_2D20')

    TalkEnd(0x00FE)

    Return()

# id: 0x0011 offset: 0x2D24
@scena.Code('func_11_2D24')
def func_11_2D24():
    OP_4A(0x000C, 255)
    OP_4A(0x000D, 255)
    OP_62(0x000C, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x000C, 0x0101, 0)
    Sleep(400)

    ChrTalk(
        0x000C,
        (
            '啊，艾丝蒂尔\n',
            '和约修亚……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000D, 0x0101, 400)

    ChrTalk(
        0x000D,
        (
            '各位不是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '你们救了小姐，\n',
            '实在是感激不尽。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '我代表本家\n',
            '致以深切感谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1017F哪里，太客气了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1040F嗯嗯，我们只是尽了义务。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000C, 0x0102, 400)

    ChrTalk(
        0x000C,
        (
            '呵呵，游击士\n',
            '总是这么谦虚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '不过，真的\n',
            '非常感谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '多亏事件的解决，\n',
            '我们之间的鸿沟也被填埋了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x007A, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_30A6',
    )

    ChrTalk(
        0x0101,
        (
            '#1004F啊……\n',
            '这么说难道……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '……你们俩和好了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000C, 0x0101, 400)

    ChrTalk(
        0x000C,
        (
            '嗯嗯，就算是吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000D, 0x0101, 400)

    ChrTalk(
        0x000D,
        (
            '只是我的立场\n',
            '得到了理解。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '不过……\n',
            '好像还没完全接受。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000C, 0x000D, 400)

    ChrTalk(
        0x000C,
        (
            '哎呀，那是当然了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '随便给人家定什么相亲，\n',
            '怎么可能接受嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000D, 0x000C, 400)

    ChrTalk(
        0x000D,
        (
            '所以说，请别\n',
            '拘泥那些小事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '我是希望芙拉瑟\n',
            '拥有广阔的视野。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000C, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000C,
        (
            '这、这是我的亲事啊！？\n',
            '哪里算是小事了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1016F好、好了好了……\n',
            '两个人都冷静一下啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1052F（这算是和好了吗……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1015F（嗯～很微妙……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1016F（不过，算是恢复\n',
            '以前的状态了吧？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_326F')

    def _loc_30A6(): pass

    label('loc_30A6')

    ChrTurnDirection(0x000D, 0x000C, 400)

    ChrTalk(
        0x000D,
        (
            '嗯，确实我的立场\n',
            '好像得到了理解……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '可是，小姐\n',
            '还要具备不拘泥于\n',
            '小事的态度才行……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000C, 0x000D, 400)

    ChrTalk(
        0x000C,
        (
            '哎呀，拘泥也是当然的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '自己的人生被人操纵，\n',
            '没人会感到高兴的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '这种想法\n',
            '太狭隘了，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '呼，真没办法……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '看来，小姐的器量\n',
            '也就是这种程度而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000C, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000C,
        (
            '你，你说什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1052F（怎么吵起来了……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1016F（唔、嗯……\n',
            '这两人真是老样子啊。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '（不过，反正一直都是这样的\n',
            '　这也算是关系好的证据吧。)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_326F(): pass

    label('loc_326F')

    OP_A2(0x0001)
    OP_A2(0x0002)
    OP_4B(0x000C, 255)
    OP_4B(0x000D, 255)

    Return()

# id: 0x0012 offset: 0x327E
@scena.Code('func_12_327E')
def func_12_327E():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_32D1',
    )

    ChrTalk(
        0x00FE,
        (
            '结果，那个白影\n',
            '到底是什么呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '反正就是带着\n',
            '一副奇怪的面具。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3334')

    def _loc_32D1(): pass

    label('loc_32D1')

    OP_A2(0x0000)

    ChrTalk(
        0x00FE,
        (
            '哟，我听说啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '据说旧校舍\n',
            '有可疑的家伙潜伏啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我看到的白影\n',
            '也是那家伙搞的鬼吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3334(): pass

    label('loc_3334')

    TalkEnd(0x00FE)

    Return()

# id: 0x0013 offset: 0x3338
@scena.Code('func_13_3338')
def func_13_3338():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '辛苦了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '以后的警备\n',
            '请交给我们吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0014 offset: 0x336C
@scena.Code('func_14_336C')
def func_14_336C():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_33BE',
    )

    ChrTalk(
        0x00FE,
        (
            '非常抱歉来迟了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为警备艇不能使用\n',
            '行动起来很花时间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0009)

    Jump('loc_33E5')

    def _loc_33BE(): pass

    label('loc_33BE')

    ChrTalk(
        0x00FE,
        (
            '非常抱歉来迟了。\n',
            '警备由我们接手。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_33E5(): pass

    label('loc_33E5')

    TalkEnd(0x00FE)

    Return()

# id: 0x0015 offset: 0x33E9
@scena.Code('func_15_33E9')
def func_15_33E9():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3479',
    )

    ChrTalk(
        0x00FE,
        (
            '现在事件解决了\n',
            '突然有点疑问……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '犯人们有使用\n',
            '导力枪吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '导力器都停了，\n',
            '为何还能用枪呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔～不可思议……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000A)

    Jump('loc_34B4')

    def _loc_3479(): pass

    label('loc_3479')

    ChrTalk(
        0x00FE,
        (
            '导力器都停了，\n',
            '为何还能用枪呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔～不可思议……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_34B4(): pass

    label('loc_34B4')

    TalkEnd(0x00FE)

    Return()

# id: 0x0016 offset: 0x34B8
@scena.Code('func_16_34B8')
def func_16_34B8():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 6, 0x121E)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Ez,
            Expr.Or,
            Expr.Return,
        ),
        'loc_34C5',
    )

    Return()

    def _loc_34C5(): pass

    label('loc_34C5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_34D6',
    )

    Call(0, 0x0053)

    def _loc_34D6(): pass

    label('loc_34D6')

    EventBegin(0x00)
    OP_71(0x0002, 0x0010)
    OP_6F(0x0021, 0)
    OP_70(0x0021, 0x0000003C)
    Sleep(1000)

    Fade(1000)
    OP_C4(0x00, 0x00000002)
    OP_7E(0x044C, 0x07D0, 0x0064, 0x0A, 0x00000001)
    FormationAddMember(ChrTable['科洛丝'], 0xF9, 0xFF)
    SetChrStatus(ChrTable['科洛丝'], 0x00, 38)
    SetChrStatus(ChrTable['科洛丝'], 0xFE, 0)
    EquipCmd(ChrTable['科洛丝'], ItemTable['刺剑'], 0xFF)
    EquipCmd(ChrTable['科洛丝'], ItemTable['纤维护铠'], 0xFF)
    EquipCmd(ChrTable['科洛丝'], ItemTable['金属靴'], 0xFF)
    EquipCmd(ChrTable['科洛丝'], ItemTable['ＨＰ２'], 0x00)
    EquipCmd(ChrTable['科洛丝'], ItemTable['治愈'], 0x01)
    EquipCmd(ChrTable['科洛丝'], ItemTable['ＥＰ１'], 0x02)
    AddCraft(ChrTable['科洛丝'], 0x0000)
    AddCraft(ChrTable['科洛丝'], CraftTable['连锁战技１(２人协力)'])
    OP_BB(0x04, 0x06, 0x000000FA)
    SetChrFlags(0x000A, 0x0040)
    SetChrFlags(0x0008, 0x0040)
    SetChrFlags(0x0009, 0x0040)
    SetChrFlags(0x0105, 0x0008)
    SetChrPos(0x0101, 22270, 0, 46760, 91)
    SetChrPos(0x00F7, 21650, 0, 45420, 84)
    SetChrPos(0x0104, 20500, 0, 47120, 85)
    SetChrPos(0x0127, 20100, 0, 46000, 85)
    SetChrPos(0x0105, 22100, 0, 59170, 195)
    SetChrPos(0x0008, 20980, 0, 58890, 171)
    SetChrPos(0x0009, 22410, 0, 58760, 179)
    OP_6D(61060, 0, 55000, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(6110, 0)
    OP_6C(75000, 0)
    OP_6E(262, 0)
    OP_12(0x00009470, 0x0003D090, 0x00000000)
    OP_C8(0x0200, 0x0046, 'C_PLAC06._CH', 0x01, 0x03E8)
    ShowPlaceName('杰尼丝王立学院')

    @scena.Lambda('lambda_3642')
    def lambda_3642():
        OP_6D(21160, 0, 46450, 10000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_3642)

    @scena.Lambda('lambda_365A')
    def lambda_365A():
        OP_6C(315000, 10000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_365A)

    Sleep(2000)

    OP_12(0x00009470, 0x00014C08, 0x00001F40)

    @scena.Lambda('lambda_367C')
    def lambda_367C():
        OP_6B(3000, 8000)

        ExitThread()

    DispatchAsync(0x0001, 0x0003, lambda_367C)

    @scena.Lambda('lambda_368C')
    def lambda_368C():
        OP_67(0, 8350, -10000, 8000)

        ExitThread()

    DispatchAsync(0x0001, 0x0002, lambda_368C)

    Sleep(8000)

    ChrTalk(
        0x0104,
        (
            '#0040210767V#033F哦，这里就是王立学院吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040210768V#035F即将绽放的花蕾们\n',
            '洒下青春汗与泪的学舍……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040210769V呵呵……\n',
            '实在是太棒了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0127,
        (
            '#0280210770V#151F看来有很多\n',
            '值得拍摄的对象呢～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280210771V趁此机会要大拍特拍才行～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00F7, 0x0104, 400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_3800',
    )

    ChrTalk(
        0x0106,
        (
            '#0050210772V#551F#6P我说啊，我们只是\n',
            '来调查幽灵骚动的啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050210773V#552F明白吗，这件事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3864')

    def _loc_3800(): pass

    label('loc_3800')

    ChrTalk(
        0x0103,
        (
            '#0030210774V#025F#6P唉……\n',
            '完全忘记本来的目的了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030210775V#020F别忘了我们是来调查事件的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3864(): pass

    label('loc_3864')

    ChrTalk(
        0x0101,
        (
            '#0010210776V#1025F#5P不过，真是怀念啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210777V在这所学院\n',
            '虽然只度过一周左右……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x00F7, 0, 400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_3941',
    )

    ChrTalk(
        0x0106,
        (
            '#0050210778V#051F#6P不过，却是和朋友们\n',
            '一起度过的难忘时光呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050210779V不是还出演了\n',
            '学院祭的戏剧吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_39AF')

    def _loc_3941(): pass

    label('loc_3941')

    ChrTalk(
        0x0103,
        (
            '#0030210780V#027F#6P呵呵，却是和朋友们\n',
            '一起度过的难忘时光呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030210781V不是还出演了\n',
            '学院祭的戏剧吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_39AF(): pass

    label('loc_39AF')

    ChrTalk(
        0x0127,
        (
            '#0280210782V#151F啊，我听奈尔前辈说了～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280210783V小艾你们是骑士,\n',
            '约修亚是公主对吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280210784V#154F啊～啊，好想拍下照片啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0104, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0104,
        (
            '#0040210785V#036F什么……那是真的吗！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040210786V#034F哦哦，竟然如此！\n',
            '居然错过了约修亚的美态！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040210787V无论如何也要找到他\n',
            '让他再穿一次才行！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x0E, 0x0F, 0x000000FA, 0x02)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x0101, 0x0104, 600)

    ChrTalk(
        0x0101,
        (
            '#0010210788V#1007F#4P唉，沉浸于感伤，\n',
            '真是像傻瓜一样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210789V#1015F这么说来，特蕾莎老师\n',
            '说过现在是考试期间……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210790V还没结束吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_22(0x0197, 0x00, 0x64)
    Sleep(500)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0127, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x00F7, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0104, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_3C1D')
    def lambda_3C1D():
        OP_8C(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3C1D)

    @scena.Lambda('lambda_3C2B')
    def lambda_3C2B():
        OP_8C(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_3C2B)

    @scena.Lambda('lambda_3C39')
    def lambda_3C39():
        OP_8C(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_3C39)

    @scena.Lambda('lambda_3C47')
    def lambda_3C47():
        OP_8C(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0127, 0x0001, lambda_3C47)

    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010210791V#1004F#5P基库！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_6D(27230, 0, 48860, 1500)

    @scena.Lambda('lambda_3C8E')
    def lambda_3C8E():
        OP_6D(21160, 0, 46450, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_3C8E)

    OP_22(0x008C, 0x00, 0x64)
    SetChrPos(0x000A, 36940, 6000, 46020, 90)
    ClearChrFlags(0x000A, 0x0080)
    CreateThread(0x000A, 0x01, 0x00, 0x0002)
    OP_8E(0x000A, 22000, 2000, 48300, 6000, 0x00)
    OP_22(0x0197, 0x00, 0x64)
    TerminateThread(0x000A, 0x01)
    OP_97(0x000A, 0x000056FE, 0x0000B6A8, 0xFFFA81C0, 0x00001770, 0x0001)
    OP_97(0x000A, 0x000056FE, 0x0000B6A8, 0xFFFE2B40, 0x00001388, 0x0001)
    OP_97(0x000A, 0x000056FE, 0x0000B6A8, 0xFFFF15A0, 0x00000BB8, 0x0001)
    OP_8C(0x0101, 135, 0)
    CreateThread(0x000A, 0x01, 0x00, 0x0002)

    @scena.Lambda('lambda_3D32')
    def lambda_3D32():
        OP_8C(0x000A, 90, 100)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_3D32)

    OP_8F(0x000A, 22280, 700, 46140, 2000, 0x00)
    Fade(500)
    TerminateThread(0x000A, 0x01)
    SetChrFlags(0x000A, 0x0080)
    SetChrChipByIndex(0x0101, 3)
    SetChrSubChip(0x0101, 3)
    OP_0D()
    OP_8C(0x00F7, 0, 400)
    SetChrSubChip(0x0101, 5)
    OP_8C(0x0104, 135, 400)

    ChrTalk(
        0x000A,
        (
            '#0440210792V#311F#5P啾啾啾⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010210793V#1016F#2P啊哈哈……\n',
            '虽然不明白你说什么，\n',
            '不过好像在欢迎我们呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210794V#1006F好久不见，还好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0440210795V#311F#5P啾～～㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearChrFlags(0x0105, 0x0008)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)

    NpcTalk(
        0x0105,
        '女孩的声音',
        (
            '#0060210796V#6P……艾丝蒂尔………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    SetChrSubChip(0x0101, 3)
    SetChrFlags(0x0101, 0x0020)
    ChrTurnDirection(0x0101, 0x0105, 400)

    @scena.Lambda('lambda_3EA9')
    def lambda_3EA9():
        ChrTurnDirection(0x00F7, 0x0105, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_3EA9)

    @scena.Lambda('lambda_3EB7')
    def lambda_3EB7():
        ChrTurnDirection(0x0104, 0x0105, 400)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_3EB7)

    @scena.Lambda('lambda_3EC5')
    def lambda_3EC5():
        ChrTurnDirection(0x0127, 0x0105, 400)

        ExitThread()

    DispatchAsync(0x0127, 0x0001, lambda_3EC5)

    ClearChrFlags(0x0101, 0x0020)

    ChrTalk(
        0x0101,
        (
            '#0010210797V#1025F#5P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3EF9')
    def lambda_3EF9():
        OP_6D(21750, 0, 50070, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_3EF9)

    @scena.Lambda('lambda_3F11')
    def lambda_3F11():
        OP_67(0, 9280, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_3F11)

    @scena.Lambda('lambda_3F29')
    def lambda_3F29():
        OP_6C(328000, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_3F29)

    @scena.Lambda('lambda_3F39')
    def lambda_3F39():
        OP_6B(2840, 3000)

        ExitThread()

    DispatchAsync(0x0001, 0x0003, lambda_3F39)

    Fade(250)
    SetChrPos(0x000A, 22710, 0, 46900, 0)
    ClearChrFlags(0x000A, 0x0080)
    SetChrChipByIndex(0x0101, 65535)
    SetChrSubChip(0x0101, 0)
    OP_22(0x008C, 0x00, 0x64)

    @scena.Lambda('lambda_3F73')
    def lambda_3F73():
        OP_8F(0x000A, 25410, 3400, 51560, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0000, lambda_3F73)

    CreateThread(0x000A, 0x01, 0x00, 0x0002)

    @scena.Lambda('lambda_3F95')
    def lambda_3F95():
        OP_8E(0x00FE, 22610, 0, 52300, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_3F95)

    Sleep(1000)

    @scena.Lambda('lambda_3FB5')
    def lambda_3FB5():
        OP_8E(0x00FE, 21680, 0, 53190, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_3FB5)

    Sleep(300)

    @scena.Lambda('lambda_3FD5')
    def lambda_3FD5():
        OP_8E(0x00FE, 22810, 0, 53630, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_3FD5)

    WaitForThreadExit(0x000A, 0x0000)
    OP_8C(0x000A, 270, 180)
    OP_8C(0x000A, 180, 180)
    Sleep(250)

    TerminateThread(0x000A, 0x01)
    SetChrChipByIndex(0x000A, 4)
    SetChrSubChip(0x000A, 0)
    WaitForThreadExit(0x0009, 0x0001)
    WaitForThreadExit(0x0001, 0x0000)
    WaitForThreadExit(0x0001, 0x0001)
    WaitForThreadExit(0x0001, 0x0002)
    WaitForThreadExit(0x0001, 0x0003)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010210798V#1025F#6P科洛丝……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210799V#1016F嘿嘿……诞辰庆典以来好久不见呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060210800V#542F嗯……是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060210801V……那个……我……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060210802V#049F…………我………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_40F9')
    def lambda_40F9():
        ChrTurnDirection(0x00F7, 0x0105, 0)
        Yield()

        Jump('lambda_40F9')

    DispatchAsync2(0x00F7, 0x0002, lambda_40F9)

    @scena.Lambda('lambda_410A')
    def lambda_410A():
        ChrTurnDirection(0x0104, 0x0105, 0)
        Yield()

        Jump('lambda_410A')

    DispatchAsync2(0x0104, 0x0002, lambda_410A)

    @scena.Lambda('lambda_411B')
    def lambda_411B():
        ChrTurnDirection(0x0127, 0x0105, 0)
        Yield()

        Jump('lambda_411B')

    DispatchAsync2(0x0127, 0x0002, lambda_411B)

    @scena.Lambda('lambda_412C')
    def lambda_412C():
        OP_8E(0x0105, 22000, 0, 47120, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_412C)

    Sleep(300)

    Fade(500)
    OP_6D(22200, 0, 48130, 0)
    OP_67(0, 9280, -10000, 0)
    OP_6B(2840, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)

    @scena.Lambda('lambda_418E')
    def lambda_418E():
        OP_6D(22270, 0, 46760, 2000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_418E)

    @scena.Lambda('lambda_41A6')
    def lambda_41A6():
        OP_67(0, 9280, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_41A6)

    @scena.Lambda('lambda_41BE')
    def lambda_41BE():
        OP_8E(0x00FE, 21410, 0, 48870, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_41BE)

    Sleep(300)

    @scena.Lambda('lambda_41DE')
    def lambda_41DE():
        OP_8E(0x00FE, 22530, 0, 49180, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_41DE)

    WaitForThreadExit(0x0105, 0x0001)
    SetChrFlags(0x0101, 0x0002)
    SetChrChipByIndex(0x0101, 13)
    SetChrSubChip(0x0101, 0)
    SetChrFlags(0x0105, 0x0080)
    OP_99(0x0101, 0x00, 0x03, 0x000007D0)
    TerminateThread(0x00F7, 0x02)
    TerminateThread(0x0104, 0x02)
    TerminateThread(0x0127, 0x02)

    @scena.Lambda('lambda_4227')
    def lambda_4227():
        ChrTurnDirection(0x00F7, 0x0101, 0)
        Yield()

        Jump('lambda_4227')

    DispatchAsync2(0x00F7, 0x0002, lambda_4227)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010210803V#1025F哇哇……\n',
            '怎么了科洛丝？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060210804V#049F#6P对不起……\n',
            '……真是对不起……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060210805V艾丝蒂尔你们这么困难的时候，\n',
            '我……什么也做不到……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060210806V好讨厌自己力量不足……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010210807V#1025F真是的……\n',
            '别这么说嘛……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0101, 0x04, 0x06, 0x000005DC)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010210808V#1012F你这么为我们着想\n',
            '我就很高兴了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210809V约修亚\n',
            '也一定是这样……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210810V#1017F总之……\n',
            '能再见面就很开心了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060210811V#047F#6P嗯……我也是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060210812V#048F能这样再会\n',
            '就要感谢空之女神了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    SetChrFlags(0x0101, 0x0800)
    SetChrChipByIndex(0x0101, 13)
    SetChrSubChip(0x0101, 7)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0510210813V#649F#2P真是的～\n',
            '你们两个太夸张啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510210814V#648F好久不见呢、艾丝蒂尔。\n',
            '诞辰庆典见面以来都没见过了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010210815V#1017F嗯，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210816V汉斯也是……好久不见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0520210817V#730F#6P啊啊……是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520210818V虽然有很多话想说……\n',
            '现在还是先推迟一下吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520210819V你们是为游击士的工作来的吧？\n',
            '我带你们去校长那里吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(500)

    OP_A2(0x10F0)
    NewScene('ED6_DT21/T2510._SN', 114, 0, 0)
    IdleLoop()

    Return()

# id: 0x0017 offset: 0x45E1
@scena.Code('func_17_45E1')
def func_17_45E1():
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '现在是期末考试中，\n',
            '校外人员不允许进入。\n',
            '　　　　　　　　　　杰尼丝王立学院',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0018 offset: 0x465C
@scena.Code('func_18_465C')
def func_18_465C():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4872',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 7, 0x2017)),
            (Expr.TestScenaFlags, ScenaFlag(0x0404, 0, 0x2020)),
            Expr.Ez,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0403, 7, 0x201F)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_467F',
    )

    Call(0, 0x0050)

    Jump('loc_486C')

    def _loc_467F(): pass

    label('loc_467F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 7, 0x2017)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_47DE',
    )

    OP_A2(0x2017)
    EventBegin(0x00)
    Fade(500)
    OP_6D(65860, 0, 27990, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(122000, 0)
    OP_6E(262, 0)
    OP_6D(65860, 0, 27990, 0)
    SetChrPos(0x0102, 65860, 0, 27990, 90)
    SetChrSubChip(0x0102, 0)
    OP_0D()
    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '后门上了锁。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x0102,
        (
            '#0020360603V#1043F（这前面是旧校舍吗……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020360604V#1040F（……是啊，慎重起见……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '约修亚取出工具\n',
            '快速插入钥匙孔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x0073, 0x00, 0x50)
    Sleep(1000)

    Call(0, 0x004C)
    EventEnd(0x00)

    Jump('loc_486C')

    def _loc_47DE(): pass

    label('loc_47DE')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '后门的锁被打开了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x0102,
        (
            '#0020360605V#1035F（现在没必要往前……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020360606V#1042F（回学院内探索吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_486C(): pass

    label('loc_486C')

    TalkEnd(0x00FF)

    Jump('loc_48B9')

    def _loc_4872(): pass

    label('loc_4872')

    OP_22(0x0074, 0x00, 0x64)
    Sleep(300)

    OP_22(0x0074, 0x00, 0x64)
    Sleep(300)

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '后门上了锁。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)
    def _loc_48B9(): pass

    label('loc_48B9')

    Return()

# id: 0x0019 offset: 0x48BA
@scena.Code('func_19_48BA')
def func_19_48BA():
    EventBegin(0x00)
    FadeIn(1000, 0)
    SetChrPos(0x0101, 22990, 250, 66860, 176)
    SetChrPos(0x0105, 22040, 250, 66860, 175)
    OP_6D(22280, 480, 67450, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(44000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010211264V#1004F啊……\n',
            '已经这么晚了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0101, 400)

    ChrTalk(
        0x0105,
        (
            '#0060211265V#542F已经向学生们打听过了，\n',
            '暂时回学生会室吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0105, 400)

    ChrTalk(
        0x0101,
        (
            '#0010211266V#1006F嗯，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211267V核对大家的情报后\n',
            '能发现什么就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1221)
    OP_28(0x0083, 0x01, 0x0040)
    EventEnd(0x00)

    Return()

# id: 0x001A offset: 0x4A1B
@scena.Code('func_1A_4A1B')
def func_1A_4A1B():
    EventBegin(0x00)
    FadeIn(1000, 0)
    SetChrPos(0x0101, 40810, 250, 73170, 271)
    SetChrPos(0x0105, 40760, 250, 74250, 287)
    OP_6D(41600, 460, 73930, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(44000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010211264V#1004F啊……\n',
            '已经这么晚了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0101, 400)

    ChrTalk(
        0x0105,
        (
            '#0060211265V#542F已经向学生们打听过了，\n',
            '暂时回学生会室吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0105, 400)

    ChrTalk(
        0x0101,
        (
            '#0010220715V#1006F嗯，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211267V核对大家的情报后\n',
            '能发现什么就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1221)
    OP_28(0x0083, 0x01, 0x0040)
    EventEnd(0x00)

    Return()

# id: 0x001B offset: 0x4B7C
@scena.Code('func_1B_4B7C')
def func_1B_4B7C():
    EventBegin(0x00)
    FadeIn(1000, 0)
    SetChrPos(0x0101, 52040, 0, 65500, 258)
    SetChrPos(0x0105, 52280, 0, 64660, 252)
    OP_6D(52780, 0, 65680, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010211264V#1004F啊……\n',
            '已经这么晚了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0101, 400)

    ChrTalk(
        0x0105,
        (
            '#0060211265V#542F已经向学生们打听过了，\n',
            '暂时回学生会室吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0105, 400)

    ChrTalk(
        0x0101,
        (
            '#0010211266V#1006F嗯，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211267V核对大家的情报后\n',
            '能发现什么就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1221)
    OP_28(0x0083, 0x01, 0x0040)
    EventEnd(0x00)

    Return()

# id: 0x001C offset: 0x4CDD
@scena.Code('func_1C_4CDD')
def func_1C_4CDD():
    EventBegin(0x00)
    FadeIn(1000, 0)
    SetChrPos(0x0101, 51910, 0, 61530, 268)
    SetChrPos(0x0105, 52160, 0, 62400, 253)
    OP_6D(52910, 0, 61210, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(111000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010211264V#1004F啊……\n',
            '已经这么晚了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0101, 400)

    ChrTalk(
        0x0105,
        (
            '#0060211265V#542F已经向学生们打听过了，\n',
            '暂时回学生会室吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0105, 400)

    ChrTalk(
        0x0101,
        (
            '#0010220715V#1006F嗯，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211267V核对大家的情报后\n',
            '能发现什么就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1221)
    OP_28(0x0083, 0x01, 0x0040)
    EventEnd(0x00)

    Return()

# id: 0x001D offset: 0x4E3E
@scena.Code('func_1D_4E3E')
def func_1D_4E3E():
    EventBegin(0x00)
    FadeIn(1000, 0)
    SetChrPos(0x0101, 46730, 0, 45410, 277)
    SetChrPos(0x0105, 47060, 0, 46350, 262)
    OP_6D(47100, 0, 45890, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010211264V#1004F啊……\n',
            '已经这么晚了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0101, 400)

    ChrTalk(
        0x0105,
        (
            '#0060211265V#542F已经向学生们打听过了，\n',
            '暂时回学生会室吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0105, 400)

    ChrTalk(
        0x0101,
        (
            '#0010211266V#1006F嗯，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211267V核对大家的情报后\n',
            '能发现什么就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1221)
    OP_28(0x0083, 0x01, 0x0040)
    EventEnd(0x00)

    Return()

# id: 0x001E offset: 0x4F9F
@scena.Code('func_1E_4F9F')
def func_1E_4F9F():
    EventBegin(0x00)
    FadeIn(1000, 0)
    SetChrPos(0x0101, 51870, 0, 30080, 275)
    SetChrPos(0x0105, 52310, 0, 29300, 257)
    OP_6D(52390, 0, 30630, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(53000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010211264V#1004F啊……\n',
            '已经这么晚了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0101, 400)

    ChrTalk(
        0x0105,
        (
            '#0060211265V#542F已经向学生们打听过了，\n',
            '暂时回学生会室吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0105, 400)

    ChrTalk(
        0x0101,
        (
            '#0010211266V#1006F嗯，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211267V核对大家的情报后\n',
            '能发现什么就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1221)
    OP_28(0x0083, 0x01, 0x0040)
    EventEnd(0x00)

    Return()

# id: 0x001F offset: 0x5100
@scena.Code('func_1F_5100')
def func_1F_5100():
    EventBegin(0x00)
    ClearMapFlags(0x00000010)
    OP_DB()
    OP_6D(72780, 0, 23250, 0)
    OP_67(0, 6540, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(40000, 0)
    OP_6E(439, 0)
    SetChrFlags(0x0013, 0x0020)
    ClearChrFlags(0x0013, 0x0080)
    ClearChrFlags(0x0013, 0x0001)
    SetChrPos(0x0013, 71000, 7000, 17030, 180)
    SetChrChipByIndex(0x0013, 14)
    SetChrSubChip(0x0013, 0)

    @scena.Lambda('lambda_5175')
    def lambda_5175():
        OP_99(0x00FE, 0x00, 0x07, 0x000005DC)
        Yield()

        Jump('lambda_5175')

    DispatchAsync2(0x0013, 0x0001, lambda_5175)

    OP_9F(0x0013, 0xFF, 0xFF, 0xFF, 0xB4, 0x00000000)
    OP_A0(0x0013, 0xB4, 0xB4, 0xB4, 0x00000000)
    FadeIn(2000, 0)

    @scena.Lambda('lambda_51A6')
    def lambda_51A6():
        OP_6C(45000, 8000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_51A6)

    OP_97(0x0013, 0x00010D88, 0x00004286, 0xFFFA81C0, 0x00000BB8, 0x0001)
    OP_97(0x0013, 0x00010D88, 0x00004286, 0xFFFA81C0, 0x00000BB8, 0x0001)
    OP_97(0x0013, 0x00010D88, 0x00004286, 0xFFFEA070, 0x000007D0, 0x0001)
    Sleep(300)

    OP_8C(0x0013, 90, 1000)
    OP_8C(0x0013, 360, 1000)
    OP_8C(0x0013, 270, 1000)
    Sleep(300)

    TerminateThread(0x0000, 0x01)
    TerminateThread(0x0000, 0x02)

    @scena.Lambda('lambda_521C')
    def lambda_521C():
        OP_6D(71780, 0, 23250, 2000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_521C)

    @scena.Lambda('lambda_5234')
    def lambda_5234():
        OP_6B(2700, 2000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_5234)

    @scena.Lambda('lambda_5244')
    def lambda_5244():
        OP_96(0x0013, 0x000101C6, 0x00001388, 0x00004286, 0x000003E8, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x0013, 0x0002, lambda_5244)

    WaitForThreadExit(0x0013, 0x0002)
    SetChrChipByIndex(0x0013, 15)
    SetChrSubChip(0x0013, 0)
    WaitForThreadExit(0x0000, 0x0001)
    Sleep(500)

    TerminateThread(0x0013, 0x00)
    TerminateThread(0x0013, 0x01)
    TerminateThread(0x0013, 0x02)
    SetChrFlags(0x0013, 0x0002)
    SetChrChipByIndex(0x0013, 21)
    SetChrSubChip(0x0013, 0)
    Sleep(100)

    SetChrSubChip(0x0013, 8)
    Sleep(100)

    SetChrSubChip(0x0013, 16)
    Sleep(100)

    SetChrSubChip(0x0013, 24)
    Sleep(100)

    SetChrSubChip(0x0013, 32)
    Sleep(100)

    SetChrSubChip(0x0013, 40)
    Sleep(100)

    SetChrSubChip(0x0013, 48)
    Sleep(100)

    SetChrSubChip(0x0013, 56)
    Sleep(100)

    SetChrSubChip(0x0013, 64)
    Sleep(100)

    SetChrSubChip(0x0013, 72)
    Sleep(1000)

    SetChrChipByIndex(0x0013, 14)
    SetChrSubChip(0x0013, 0)
    ClearChrFlags(0x0013, 0x0002)
    OP_8C(0x0013, 90, 600)

    @scena.Lambda('lambda_530B')
    def lambda_530B():
        OP_6D(74780, 0, 23250, 1500)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_530B)

    @scena.Lambda('lambda_5323')
    def lambda_5323():
        OP_8E(0x00FE, 75000, 7000, 20300, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0013, 0x0002, lambda_5323)

    Sleep(1000)

    FadeOut(2000, 0, -1)
    OP_0D()
    OP_DC()
    OP_A2(0x10F1)
    SetMapFlags(0x02000000)
    NewScene('ED6_DT21/T2511._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0020 offset: 0x535B
@scena.Code('func_20_535B')
def func_20_535B():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5370',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000001F4)

    Jump('func_20_535B')

    def _loc_5370(): pass

    label('loc_5370')

    Return()

# id: 0x0021 offset: 0x5371
@scena.Code('func_21_5371')
def func_21_5371():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_DB()
    SetChrFlags(0x0000, 0x0080)
    SetChrFlags(0x0001, 0x0080)
    SetChrFlags(0x0002, 0x0080)
    SetChrFlags(0x0003, 0x0080)
    SetChrFlags(0x0024, 0x0080)
    SetChrFlags(0x0025, 0x0080)
    SetChrFlags(0x0026, 0x0080)
    SetChrFlags(0x0027, 0x0080)
    SetChrFlags(0x0028, 0x0080)
    SetChrFlags(0x0029, 0x0080)
    SetChrFlags(0x002A, 0x0080)
    SetChrFlags(0x002B, 0x0080)
    SetChrFlags(0x002C, 0x0080)
    OP_D2(0x0026000D, 0x00260012, 0x20)
    SetChrChipByIndex(0x0014, 32)
    SetChrChipByIndex(0x0015, 32)
    SetChrChipByIndex(0x0016, 32)
    SetChrChipByIndex(0x0017, 32)
    CreateThread(0x0014, 0x01, 0x00, 0x0022)
    CreateThread(0x0015, 0x01, 0x00, 0x0023)
    CreateThread(0x0016, 0x01, 0x00, 0x0024)
    CreateThread(0x0017, 0x01, 0x00, 0x0025)
    CreateThread(0x0018, 0x01, 0x00, 0x0026)
    CreateThread(0x0019, 0x01, 0x00, 0x0027)
    CreateThread(0x001A, 0x01, 0x00, 0x0028)
    CreateThread(0x001B, 0x01, 0x00, 0x0029)
    OP_6D(45900, 0, 46020, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2960, 0)
    OP_6C(45000, 0)
    OP_6E(315, 0)
    FadeIn(1000, 0)
    OP_0D()

    @scena.Lambda('lambda_5462')
    def lambda_5462():
        OP_6D(15710, 0, 46020, 10000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_5462)

    @scena.Lambda('lambda_547A')
    def lambda_547A():
        OP_6C(90000, 10000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_547A)

    Sleep(2000)

    Sleep(2000)

    Sleep(2000)

    Sleep(2000)

    Sleep(1000)

    SetMapFlags(0x02000000)
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_DC()
    OP_A2(0x10F0)
    NewScene('ED6_DT21/R2301._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0022 offset: 0x54BB
@scena.Code('func_22_54BB')
def func_22_54BB():
    SetChrPos(0x00FE, 46550, 0, 54620, 0)
    ClearChrFlags(0x00FE, 0x0080)
    def _loc_54D1(): pass

    label('loc_54D1')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5548',
    )

    OP_8C(0x00FE, 315, 400)
    Sleep(600)

    OP_8C(0x00FE, 45, 400)
    Sleep(500)

    OP_8C(0x00FE, 180, 400)
    OP_8E(0x00FE, 45900, 0, 49190, 2000, 0x00)
    Sleep(500)

    OP_8C(0x00FE, 270, 400)
    Sleep(600)

    OP_8C(0x00FE, 180, 400)
    Sleep(500)

    OP_8C(0x00FE, 0, 400)
    OP_8E(0x00FE, 46550, 0, 54620, 2000, 0x00)

    Jump('loc_54D1')

    def _loc_5548(): pass

    label('loc_5548')

    Return()

# id: 0x0023 offset: 0x5549
@scena.Code('func_23_5549')
def func_23_5549():
    SetChrPos(0x00FE, 45710, 0, 44810, 45)
    ClearChrFlags(0x00FE, 0x0080)
    Sleep(200)

    def _loc_5564(): pass

    label('loc_5564')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_55E0',
    )

    Sleep(600)

    OP_8C(0x00FE, 315, 400)
    Sleep(500)

    OP_8C(0x00FE, 45, 400)
    Sleep(600)

    OP_8C(0x00FE, 180, 400)
    OP_8E(0x00FE, 46600, 0, 31790, 2000, 0x00)
    Sleep(500)

    OP_8C(0x00FE, 135, 400)
    Sleep(600)

    OP_8C(0x00FE, 225, 400)
    Sleep(500)

    OP_8C(0x00FE, 0, 400)
    OP_8E(0x00FE, 45710, 0, 44810, 2000, 0x00)

    Jump('loc_5564')

    def _loc_55E0(): pass

    label('loc_55E0')

    Return()

# id: 0x0024 offset: 0x55E1
@scena.Code('func_24_55E1')
def func_24_55E1():
    SetChrPos(0x00FE, 21070, 0, 38420, 0)
    ClearChrFlags(0x00FE, 0x0080)
    def _loc_55F7(): pass

    label('loc_55F7')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5673',
    )

    OP_8E(0x00FE, 21070, 0, 53900, 2000, 0x00)
    Sleep(500)

    OP_8C(0x00FE, 90, 400)
    Sleep(500)

    OP_8C(0x00FE, 0, 400)
    Sleep(600)

    OP_8C(0x00FE, 180, 400)
    OP_8E(0x00FE, 21070, 0, 38420, 2000, 0x00)
    Sleep(500)

    OP_8C(0x00FE, 270, 400)
    Sleep(600)

    OP_8C(0x00FE, 90, 400)
    Sleep(500)

    OP_8C(0x00FE, 0, 400)

    Jump('loc_55F7')

    def _loc_5673(): pass

    label('loc_5673')

    Return()

# id: 0x0025 offset: 0x5674
@scena.Code('func_25_5674')
def func_25_5674():
    SetChrPos(0x00FE, 22990, 0, 54810, 180)
    ClearChrFlags(0x00FE, 0x0080)
    Sleep(200)

    def _loc_568F(): pass

    label('loc_568F')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_570B',
    )

    OP_8E(0x00FE, 22990, 0, 40680, 2000, 0x00)
    Sleep(500)

    OP_8C(0x00FE, 90, 400)
    Sleep(600)

    OP_8C(0x00FE, 180, 400)
    Sleep(600)

    OP_8C(0x00FE, 0, 400)
    OP_8E(0x00FE, 22990, 0, 54810, 2000, 0x00)
    Sleep(500)

    OP_8C(0x00FE, 90, 400)
    Sleep(500)

    OP_8C(0x00FE, 270, 400)
    Sleep(600)

    OP_8C(0x00FE, 180, 400)

    Jump('loc_568F')

    def _loc_570B(): pass

    label('loc_570B')

    Return()

# id: 0x0026 offset: 0x570C
@scena.Code('func_26_570C')
def func_26_570C():
    CreateThread(0x00FE, 0x00, 0x00, 0x0002)
    Sleep(200)

    SetChrPos(0x00FE, 31840, -1650, 57320, 0)
    ClearChrFlags(0x00FE, 0x0080)
    def _loc_572E(): pass

    label('loc_572E')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5840',
    )

    OP_8C(0x00FE, 270, 400)
    SetChrChipByIndex(0x00FE, 24)
    OP_8E(0x00FE, 30140, -1900, 56960, 2500, 0x00)
    SetChrPos(0x00FE, 30140, -1650, 56960, 270)
    SetChrChipByIndex(0x00FE, 23)
    Sleep(500)

    OP_8C(0x00FE, 180, 400)
    SetChrChipByIndex(0x00FE, 24)
    OP_8E(0x00FE, 30210, -1900, 50650, 2500, 0x00)
    SetChrPos(0x00FE, 30210, -1550, 50650, 180)
    SetChrChipByIndex(0x00FE, 23)
    OP_8C(0x00FE, 225, 400)
    Sleep(800)

    OP_8C(0x00FE, 135, 400)
    SetChrChipByIndex(0x00FE, 24)
    OP_8E(0x00FE, 33020, -1900, 48660, 2500, 0x00)
    SetChrPos(0x00FE, 33020, -1700, 48660, 135)
    SetChrChipByIndex(0x00FE, 23)
    Sleep(500)

    OP_8C(0x00FE, 0, 400)
    SetChrChipByIndex(0x00FE, 24)
    OP_8E(0x00FE, 31840, -1900, 57320, 2500, 0x00)
    SetChrPos(0x00FE, 31840, -1650, 57320, 0)
    SetChrChipByIndex(0x00FE, 23)
    Sleep(500)

    OP_8C(0x00FE, 225, 400)
    Sleep(800)

    OP_8C(0x00FE, 315, 400)

    Jump('loc_572E')

    def _loc_5840(): pass

    label('loc_5840')

    Return()

# id: 0x0027 offset: 0x5841
@scena.Code('func_27_5841')
def func_27_5841():
    CreateThread(0x00FE, 0x00, 0x00, 0x0002)
    SetChrPos(0x00FE, 33990, -1650, 34800, 135)
    ClearChrFlags(0x00FE, 0x0080)
    def _loc_585E(): pass

    label('loc_585E')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5981',
    )

    Sleep(500)

    OP_8C(0x00FE, 270, 400)
    SetChrChipByIndex(0x00FE, 24)
    OP_8E(0x00FE, 30930, -1900, 34630, 2500, 0x00)
    SetChrPos(0x00FE, 30930, -1650, 34630, 270)
    SetChrChipByIndex(0x00FE, 23)
    Sleep(800)

    OP_8C(0x00FE, 0, 400)
    SetChrChipByIndex(0x00FE, 24)
    OP_8E(0x00FE, 29820, -1900, 43990, 2500, 0x00)
    SetChrPos(0x00FE, 29820, -1650, 43990, 0)
    SetChrChipByIndex(0x00FE, 23)
    OP_8C(0x00FE, 315, 400)
    Sleep(500)

    OP_8C(0x00FE, 270, 400)
    Sleep(500)

    OP_8C(0x00FE, 90, 400)
    SetChrChipByIndex(0x00FE, 24)
    OP_8E(0x00FE, 34130, -1900, 43070, 2500, 0x00)
    SetChrPos(0x00FE, 34130, -1650, 43070, 90)
    SetChrChipByIndex(0x00FE, 23)
    Sleep(800)

    OP_8C(0x00FE, 180, 400)
    SetChrChipByIndex(0x00FE, 24)
    OP_8E(0x00FE, 33990, -1900, 34800, 2500, 0x00)
    SetChrPos(0x00FE, 33990, -1650, 34800, 180)
    SetChrChipByIndex(0x00FE, 23)
    Sleep(500)

    OP_8C(0x00FE, 315, 400)
    Sleep(800)

    OP_8C(0x00FE, 135, 400)

    Jump('loc_585E')

    def _loc_5981(): pass

    label('loc_5981')

    Return()

# id: 0x0028 offset: 0x5982
@scena.Code('func_28_5982')
def func_28_5982():
    CreateThread(0x00FE, 0x00, 0x00, 0x0002)
    SetChrPos(0x00FE, 40320, -2000, 48550, 90)
    ClearChrFlags(0x00FE, 0x0080)
    Sleep(800)

    def _loc_59A4(): pass

    label('loc_59A4')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5A9F',
    )

    OP_8C(0x00FE, 270, 400)
    SetChrChipByIndex(0x00FE, 26)
    OP_8E(0x00FE, 37690, -2000, 47200, 3000, 0x00)
    SetChrChipByIndex(0x00FE, 25)
    OP_8C(0x00FE, 0, 400)
    Sleep(500)

    SetChrChipByIndex(0x00FE, 26)
    OP_8E(0x00FE, 36920, -2000, 52930, 3000, 0x00)
    SetChrChipByIndex(0x00FE, 25)
    OP_8C(0x00FE, 45, 400)
    Sleep(800)

    OP_8C(0x00FE, 0, 400)
    SetChrChipByIndex(0x00FE, 26)
    OP_8E(0x00FE, 35960, -2000, 56400, 3000, 0x00)
    SetChrChipByIndex(0x00FE, 25)
    SetChrFlags(0x00FE, 0x0002)
    Sleep(1000)

    ClearChrFlags(0x00FE, 0x0002)
    OP_8C(0x00FE, 135, 400)
    SetChrChipByIndex(0x00FE, 26)
    OP_8E(0x00FE, 39490, -2000, 53840, 3000, 0x00)
    SetChrChipByIndex(0x00FE, 25)
    Sleep(800)

    OP_8C(0x00FE, 180, 400)
    SetChrChipByIndex(0x00FE, 26)
    OP_8E(0x00FE, 40320, -2000, 48550, 3000, 0x00)
    SetChrChipByIndex(0x00FE, 25)
    Sleep(500)

    OP_8C(0x00FE, 90, 400)
    Sleep(500)

    Jump('loc_59A4')

    def _loc_5A9F(): pass

    label('loc_5A9F')

    Return()

# id: 0x0029 offset: 0x5AA0
@scena.Code('func_29_5AA0')
def func_29_5AA0():
    CreateThread(0x00FE, 0x00, 0x00, 0x0002)
    SetChrPos(0x00FE, 36800, -2000, 41930, 315)
    ClearChrFlags(0x00FE, 0x0080)
    SetChrFlags(0x00FE, 0x0002)
    Sleep(1000)

    ClearChrFlags(0x00FE, 0x0002)
    def _loc_5ACC(): pass

    label('loc_5ACC')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5BD6',
    )

    OP_8C(0x00FE, 90, 400)
    SetChrChipByIndex(0x00FE, 26)
    OP_8E(0x00FE, 39740, -2000, 42890, 3000, 0x00)
    SetChrChipByIndex(0x00FE, 25)
    Sleep(500)

    OP_8C(0x00FE, 180, 400)
    SetChrChipByIndex(0x00FE, 26)
    SetChrFlags(0x00FE, 0x0002)
    Sleep(1000)

    ClearChrFlags(0x00FE, 0x0002)
    OP_8E(0x00FE, 39330, -2000, 36410, 3000, 0x00)
    SetChrChipByIndex(0x00FE, 25)
    OP_8C(0x00FE, 270, 400)
    Sleep(800)

    OP_8C(0x00FE, 215, 400)
    SetChrChipByIndex(0x00FE, 26)
    OP_8E(0x00FE, 36000, -2000, 34650, 3000, 0x00)
    SetChrChipByIndex(0x00FE, 25)
    SetChrFlags(0x00FE, 0x0002)
    Sleep(1000)

    ClearChrFlags(0x00FE, 0x0002)
    OP_8C(0x00FE, 90, 400)
    SetChrChipByIndex(0x00FE, 26)
    OP_8E(0x00FE, 38240, -2000, 34230, 3000, 0x00)
    SetChrChipByIndex(0x00FE, 25)
    Sleep(800)

    OP_8C(0x00FE, 180, 400)
    SetChrChipByIndex(0x00FE, 26)
    OP_8E(0x00FE, 36800, -2000, 41930, 3000, 0x00)
    SetChrChipByIndex(0x00FE, 25)
    Sleep(500)

    OP_8C(0x00FE, 315, 400)
    Sleep(500)

    Jump('loc_5ACC')

    def _loc_5BD6(): pass

    label('loc_5BD6')

    Return()

# id: 0x002A offset: 0x5BD7
@scena.Code('func_2A_5BD7')
def func_2A_5BD7():
    EventBegin(0x00)
    OP_6D(15700, 0, 45080, 0)
    OP_67(0, 11040, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(132000, 0)
    OP_6E(446, 0)
    SetChrPos(0x0102, 10480, 0, 580, 0)
    SetChrFlags(0x0024, 0x0080)
    SetChrFlags(0x0025, 0x0080)
    SetChrFlags(0x0026, 0x0080)
    SetChrFlags(0x0027, 0x0080)
    SetChrFlags(0x0028, 0x0080)
    SetChrFlags(0x0029, 0x0080)
    SetChrFlags(0x002A, 0x0080)
    SetChrFlags(0x002B, 0x0080)
    SetChrFlags(0x002C, 0x0080)
    OP_D2(0x00270019, 0x0027001D, 0x1D)
    OP_D2(0x002600FC, 0x00260101, 0x1E)
    OP_D2(0x0026000D, 0x00260012, 0x1F)
    SetChrChipByIndex(0x0014, 31)
    SetChrChipByIndex(0x0015, 31)
    SetChrChipByIndex(0x0016, 31)
    SetChrChipByIndex(0x0017, 31)
    CreateThread(0x0014, 0x01, 0x00, 0x0022)
    CreateThread(0x0015, 0x01, 0x00, 0x0023)
    CreateThread(0x0016, 0x01, 0x00, 0x0024)
    CreateThread(0x0017, 0x01, 0x00, 0x0025)
    CreateThread(0x0018, 0x01, 0x00, 0x0026)
    CreateThread(0x0019, 0x01, 0x00, 0x0027)
    CreateThread(0x001A, 0x01, 0x00, 0x0028)
    CreateThread(0x001B, 0x01, 0x00, 0x0029)
    OP_C8(0x0200, 0x0046, 'C_PLAC06._CH', 0x01, 0x03E8)
    ShowPlaceName('杰尼丝王立学院')
    FadeIn(1000, 0)

    @scena.Lambda('lambda_5CF2')
    def lambda_5CF2():
        OP_6D(13720, 0, 10560, 6000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_5CF2)

    @scena.Lambda('lambda_5D0A')
    def lambda_5D0A():
        OP_67(0, 10100, -10000, 6000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_5D0A)

    @scena.Lambda('lambda_5D22')
    def lambda_5D22():
        OP_6C(143000, 6000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_5D22)

    @scena.Lambda('lambda_5D32')
    def lambda_5D32():
        OP_6E(296, 6000)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_5D32)

    @scena.Lambda('lambda_5D42')
    def lambda_5D42():
        OP_6B(2570, 6000)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_5D42)

    Sleep(4500)

    SetChrFlags(0x0014, 0x0080)
    SetChrFlags(0x0015, 0x0080)
    SetChrFlags(0x0016, 0x0080)
    SetChrFlags(0x0017, 0x0080)
    SetChrFlags(0x0018, 0x0080)
    SetChrFlags(0x0019, 0x0080)
    SetChrFlags(0x001A, 0x0080)
    SetChrFlags(0x001B, 0x0080)
    OP_8F(0x0102, 12280, 0, 8870, 6000, 0x00)
    OP_8C(0x0102, 45, 400)
    SetChrChipByIndex(0x0102, 30)
    SetChrSubChip(0x0102, 1)
    WaitForThreadExit(0x0102, 0x0001)

    @scena.Lambda('lambda_5DA9')
    def lambda_5DA9():
        OP_6D(15230, 0, 13640, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_5DA9)

    @scena.Lambda('lambda_5DC1')
    def lambda_5DC1():
        OP_6C(179000, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_5DC1)

    SetChrSubChip(0x0102, 1)
    Sleep(300)

    SetChrSubChip(0x0102, 0)
    OP_22(0x023B, 0x00, 0x64)
    SetChrFlags(0x0102, 0x0004)
    OP_7D(0x00, 0x0102, 0x0028, 0x01F4)
    OP_96(0x0102, 0x000035DE, 0x00000D48, 0x00002C56, 0x00001194, 0x00001770)
    OP_22(0x00A4, 0x00, 0x64)
    SetChrSubChip(0x0102, 1)
    Sleep(100)

    SetChrSubChip(0x0102, 0)
    OP_22(0x023B, 0x00, 0x64)
    OP_96(0x0102, 0x00003C32, 0x00000000, 0x00003610, 0x000005DC, 0x00001770)
    SetChrSubChip(0x0102, 1)
    OP_22(0x00A4, 0x00, 0x64)
    OP_7D(0x01, 0x0102, 0x0000, 0x0000)
    ClearChrFlags(0x0102, 0x0004)
    WaitForThreadExit(0x0102, 0x0001)
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020360588V#1035F……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x0102, 65535)
    SetChrSubChip(0x0102, 0)
    OP_0D()

    @scena.Lambda('lambda_5E98')
    def lambda_5E98():
        OP_6D(16090, 0, 24680, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_5E98)

    OP_8E(0x0102, 16200, 0, 24520, 3000, 0x00)
    Fade(250)
    SetChrChipByIndex(0x0102, 29)
    OP_8C(0x0102, 45, 0)
    OP_0D()
    Sleep(1000)

    OP_D2(0x0026000D, 0x00260012, 0x20)
    SetChrChipByIndex(0x0014, 32)
    SetChrChipByIndex(0x0015, 32)
    CreateThread(0x0014, 0x01, 0x00, 0x002B)
    CreateThread(0x0015, 0x01, 0x00, 0x002C)

    @scena.Lambda('lambda_5EFD')
    def lambda_5EFD():
        OP_6D(21840, 0, 27280, 4000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_5EFD)

    @scena.Lambda('lambda_5F15')
    def lambda_5F15():
        OP_6B(2910, 4000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_5F15)

    @scena.Lambda('lambda_5F25')
    def lambda_5F25():
        OP_6C(153000, 4000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_5F25)

    OP_6E(301, 4000)
    Sleep(3000)

    Fade(500)
    OP_6D(16090, 0, 24680, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(166000, 0)
    OP_6E(288, 0)
    TerminateThread(0x0014, 0x01)
    TerminateThread(0x0015, 0x01)
    SetChrFlags(0x0014, 0x0080)
    SetChrFlags(0x0015, 0x0080)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x0102,
        (
            '#0020360589V#1043F（……看来移动到\n',
            '  建筑物背后比较好。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020360590V#1042F（之后只要掌握建筑物里的人质\n',
            '  和大体的敌方战力分布……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x0102, 65535)
    OP_8C(0x0102, 180, 0)
    OP_0D()

    @scena.Lambda('lambda_603B')
    def lambda_603B():
        OP_6D(16500, 0, 21880, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_603B)

    @scena.Lambda('lambda_6053')
    def lambda_6053():
        OP_6C(151000, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_6053)

    OP_8E(0x0102, 16480, 0, 21830, 2000, 0x00)
    OP_8C(0x0102, 90, 400)
    WaitForThreadExit(0x0102, 0x0001)

    @scena.Lambda('lambda_6083')
    def lambda_6083():
        OP_6E(241, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_6083)

    Sleep(1000)

    FadeOut(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x02000000)
    OP_A2(0x10F0)
    NewScene('ED6_DT21/T2512._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x002B offset: 0x60AF
@scena.Code('func_2B_60AF')
def func_2B_60AF():
    SetChrPos(0x00FE, 20980, 0, 38990, 180)
    ClearChrFlags(0x00FE, 0x0080)
    OP_8E(0x00FE, 20980, 0, 28160, 2000, 0x00)
    OP_8E(0x00FE, 33270, 0, 28160, 2000, 0x00)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x002C offset: 0x60F3
@scena.Code('func_2C_60F3')
def func_2C_60F3():
    SetChrPos(0x00FE, 30910, 0, 29060, 270)
    ClearChrFlags(0x00FE, 0x0080)
    OP_8E(0x00FE, 23020, 0, 29060, 2000, 0x00)
    OP_8E(0x00FE, 23020, 0, 40790, 2000, 0x00)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x002D offset: 0x6137
@scena.Code('func_2D_6137')
def func_2D_6137():
    EventBegin(0x00)
    OP_6D(16500, 0, 21880, 0)
    OP_6C(151000, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6E(288, 0)
    SetChrPos(0x0102, 16480, 0, 21830, 90)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020360591V#1035F（男子宿舍内敌兵两名……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020360592V#1040F（就这样先检查一次\n',
            '  全部建筑物吧……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_65(0x02, 0x0001)
    OP_65(0x03, 0x0001)
    OP_65(0x04, 0x0001)
    OP_65(0x05, 0x0001)
    OP_65(0x06, 0x0001)
    OP_65(0x07, 0x0001)
    OP_65(0x08, 0x0001)
    OP_65(0x09, 0x0001)
    OP_65(0x0A, 0x0001)
    OP_65(0x0B, 0x0001)
    EventEnd(0x00)
    SetMapFlags(0x02000000)

    Return()

# id: 0x002E offset: 0x6233
@scena.Code('func_2E_6233')
def func_2E_6233():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 3, 0x2013)),
            Expr.Return,
        ),
        'loc_6373',
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeOut(300, 0, 100)
    OP_57(0x00C8, 0x0014, 0x000C, '#5CLook inside again?')
    OP_CC(0x00, 0x00, 0x000A, 0x000A, 0x00)
    OP_CC(0x01, 0x00, '【是】')
    OP_CC(0x01, 0x00, '【否】')
    OP_CC(0x02, 0x00)
    MenuEnd(0x0000)
    FadeIn(300, 0)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_DA()

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_62BD'),
        (0x00000001, 'loc_6361'),
        (-1, 'loc_6370'),
    )

    def _loc_62BD(): pass

    label('loc_62BD')

    EventBegin(0x00)

    If(
        (
            (Expr.PushValueByIndex, 0x64),
            (Expr.PushLong, 0x5A),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_6302',
    )

    Fade(500)
    SetChrPos(0x0102, 16480, 0, 21830, 90)
    OP_6D(16480, 0, 21830, 0)
    OP_6C(150000, 0)
    OP_A3(0x2030)
    OP_0D()

    Jump('loc_632D')

    def _loc_6302(): pass

    label('loc_6302')

    Fade(500)
    SetChrPos(0x0102, 16480, 0, 21830, 90)
    OP_6D(16480, 0, 21830, 0)
    OP_A2(0x2030)
    OP_0D()

    def _loc_632D(): pass

    label('loc_632D')

    @scena.Lambda('lambda_6333')
    def lambda_6333():
        OP_6E(241, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_6333)

    Sleep(1000)

    FadeOut(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x02000000)
    OP_A2(0x10F1)
    NewScene('ED6_DT21/T2512._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_6370')

    def _loc_6361(): pass

    label('loc_6361')

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)

    Jump('loc_6370')

    def _loc_6370(): pass

    label('loc_6370')

    Jump('loc_641D')

    def _loc_6373(): pass

    label('loc_6373')

    EventBegin(0x00)

    If(
        (
            (Expr.PushValueByIndex, 0x64),
            (Expr.PushLong, 0x5A),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_63B8',
    )

    Fade(500)
    SetChrPos(0x0102, 16480, 0, 21830, 90)
    OP_6D(16480, 0, 21830, 0)
    OP_6C(150000, 0)
    OP_A3(0x2030)
    OP_0D()

    Jump('loc_63EC')

    def _loc_63B8(): pass

    label('loc_63B8')

    Fade(500)
    SetChrPos(0x0102, 16480, 0, 21830, 90)
    OP_6D(16480, 0, 21830, 0)
    OP_6C(30000, 0)
    OP_A2(0x2030)
    OP_0D()

    def _loc_63EC(): pass

    label('loc_63EC')

    @scena.Lambda('lambda_63F2')
    def lambda_63F2():
        OP_6E(241, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_63F2)

    Sleep(1000)

    FadeOut(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x02000000)
    OP_A2(0x10F1)
    NewScene('ED6_DT21/T2512._SN', 100, 0, 0)
    IdleLoop()
    def _loc_641D(): pass

    label('loc_641D')

    TalkEnd(0x00FF)

    Return()

# id: 0x002F offset: 0x6421
@scena.Code('func_2F_6421')
def func_2F_6421():
    EventBegin(0x00)
    OP_6D(16480, 0, 21830, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6E(262, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0406, 0, 0x2030)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_646B',
    )

    OP_6C(150000, 0)

    Jump('loc_6474')

    def _loc_646B(): pass

    label('loc_646B')

    OP_6C(30000, 0)

    def _loc_6474(): pass

    label('loc_6474')

    SetChrPos(0x0102, 16480, 0, 21830, 90)
    FadeIn(1000, 0)
    OP_0D()
    Call(0, 0x004C)
    EventEnd(0x00)
    SetMapFlags(0x02000000)

    Return()

# id: 0x0030 offset: 0x649B
@scena.Code('func_30_649B')
def func_30_649B():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 4, 0x2014)),
            Expr.Return,
        ),
        'loc_65E1',
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeOut(300, 0, 100)
    OP_57(0x00C8, 0x0014, 0x000C, '#5CLook inside again?')
    OP_CC(0x00, 0x00, 0x000A, 0x000A, 0x00)
    OP_CC(0x01, 0x00, '【是】')
    OP_CC(0x01, 0x00, '【否】')
    OP_CC(0x02, 0x00)
    MenuEnd(0x0000)
    FadeIn(300, 0)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_DA()

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_6525'),
        (0x00000001, 'loc_65CF'),
        (-1, 'loc_65DE'),
    )

    def _loc_6525(): pass

    label('loc_6525')

    EventBegin(0x00)

    If(
        (
            (Expr.PushValueByIndex, 0x64),
            (Expr.PushLong, 0x5A),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_656A',
    )

    Fade(500)
    SetChrPos(0x0102, 16490, 0, 16250, 90)
    OP_6D(16490, 0, 16250, 0)
    OP_6C(150000, 0)
    OP_A3(0x2030)
    OP_0D()

    Jump('loc_659E')

    def _loc_656A(): pass

    label('loc_656A')

    Fade(500)
    SetChrPos(0x0102, 16490, 0, 16250, 90)
    OP_6D(16490, 0, 16250, 0)
    OP_6C(30000, 0)
    OP_A2(0x2030)
    OP_0D()

    def _loc_659E(): pass

    label('loc_659E')

    @scena.Lambda('lambda_65A4')
    def lambda_65A4():
        OP_6E(241, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_65A4)

    Sleep(1000)

    FadeOut(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x02000000)
    OP_A2(0x10F2)
    NewScene('ED6_DT21/T2512._SN', 107, 0, 0)
    IdleLoop()

    def _loc_65CF(): pass

    label('loc_65CF')

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)

    Jump('loc_65DE')

    def _loc_65DE(): pass

    label('loc_65DE')

    Jump('loc_668B')

    def _loc_65E1(): pass

    label('loc_65E1')

    EventBegin(0x00)

    If(
        (
            (Expr.PushValueByIndex, 0x64),
            (Expr.PushLong, 0x5A),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_6626',
    )

    Fade(500)
    SetChrPos(0x0102, 16490, 0, 16250, 90)
    OP_6D(16490, 0, 16250, 0)
    OP_6C(150000, 0)
    OP_A3(0x2030)
    OP_0D()

    Jump('loc_665A')

    def _loc_6626(): pass

    label('loc_6626')

    Fade(500)
    SetChrPos(0x0102, 16490, 0, 16250, 90)
    OP_6D(16490, 0, 16250, 0)
    OP_6C(30000, 0)
    OP_A2(0x2030)
    OP_0D()

    def _loc_665A(): pass

    label('loc_665A')

    @scena.Lambda('lambda_6660')
    def lambda_6660():
        OP_6E(241, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_6660)

    Sleep(1000)

    FadeOut(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x02000000)
    OP_A2(0x10F2)
    NewScene('ED6_DT21/T2512._SN', 107, 0, 0)
    IdleLoop()
    def _loc_668B(): pass

    label('loc_668B')

    TalkEnd(0x00FF)

    Return()

# id: 0x0031 offset: 0x668F
@scena.Code('func_31_668F')
def func_31_668F():
    EventBegin(0x00)
    OP_6D(16490, 0, 16250, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6E(262, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0406, 0, 0x2030)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_66D9',
    )

    OP_6C(150000, 0)

    Jump('loc_66E2')

    def _loc_66D9(): pass

    label('loc_66D9')

    OP_6C(30000, 0)

    def _loc_66E2(): pass

    label('loc_66E2')

    SetChrPos(0x0102, 16490, 0, 16250, 90)
    FadeIn(1000, 0)
    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 4, 0x2014)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_67AB',
    )

    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020360593V#1043F（男学生两名\n',
            '  和被击伤的勤务员吗……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020360594V#1040F（那个情况看来……\n',
            '  似乎不是致命伤。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020360595V（总算放心一点吧……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x2014)

    def _loc_67AB(): pass

    label('loc_67AB')

    Call(0, 0x004C)
    EventEnd(0x00)
    SetMapFlags(0x02000000)

    Return()

# id: 0x0032 offset: 0x67B7
@scena.Code('func_32_67B7')
def func_32_67B7():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 3, 0x2013)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0403, 7, 0x201F)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_67C4',
    )

    Return()

    def _loc_67C4(): pass

    label('loc_67C4')

    EventBegin(0x01)
    Fade(500)
    OP_6D(16410, 0, 23210, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)
    OP_8E(0x0102, 16470, 0, 24650, 2000, 0x00)
    OP_8C(0x0102, 45, 400)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020360596V#1042F（……外面有巡逻。\n',
            '  从里面通过比较好。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    Fade(500)
    OP_6D(15550, 0, 23560, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(180000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0102, 15550, 0, 23560, 180)
    OP_0D()
    Sleep(50)

    EventEnd(0x04)
    SetMapFlags(0x02000000)

    Return()

# id: 0x0033 offset: 0x68D0
@scena.Code('func_33_68D0')
def func_33_68D0():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 3, 0x2013)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0403, 7, 0x201F)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_68DD',
    )

    Return()

    def _loc_68DD(): pass

    label('loc_68DD')

    EventBegin(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 5, 0x2015)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6A18',
    )

    @scena.Lambda('lambda_68ED')
    def lambda_68ED():
        OP_6D(35520, 0, 12770, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_68ED)

    @scena.Lambda('lambda_6905')
    def lambda_6905():
        OP_6B(2910, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_6905)

    @scena.Lambda('lambda_6915')
    def lambda_6915():
        OP_6C(225000, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_6915)

    OP_6E(310, 3000)
    Sleep(1000)

    Fade(500)
    OP_6D(26720, 0, 12520, 0)
    OP_67(0, 5470, -10000, 0)
    OP_6B(1580, 0)
    OP_6C(237000, 0)
    OP_6E(502, 0)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearMapFlags(0x00000010)
    SetChrPos(0x0102, 26720, 0, 12520, 45)
    OP_D2(0x00270019, 0x0027001D, 0x1D)
    OP_D2(0x002600FC, 0x00260101, 0x1E)
    OP_D2(0x00270011, 0x00270015, 0x1F)
    OP_0D()
    Sleep(250)

    ChrTalk(
        0x0102,
        (
            '#0020360597V#1042F（……没办法了。\n',
            '  一口气跑过去吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    OP_8C(0x0102, 90, 400)
    Sleep(500)

    Fade(250)
    SetChrChipByIndex(0x0102, 29)
    SetChrSubChip(0x0102, 0)
    OP_0D()
    Sleep(250)

    Jump('loc_6A9F')

    def _loc_6A18(): pass

    label('loc_6A18')

    Fade(500)
    OP_6D(26720, 0, 12520, 0)
    OP_67(0, 5470, -10000, 0)
    OP_6B(1580, 0)
    OP_6C(237000, 0)
    OP_6E(502, 0)
    SetChrPos(0x0102, 26720, 0, 12520, 90)
    OP_D2(0x00270019, 0x0027001D, 0x1D)
    OP_D2(0x002600FC, 0x00260101, 0x1E)
    OP_D2(0x00270011, 0x00270015, 0x1F)
    OP_0D()
    Fade(250)
    SetChrChipByIndex(0x0102, 29)
    SetChrSubChip(0x0102, 0)
    OP_0D()
    Sleep(250)

    def _loc_6A9F(): pass

    label('loc_6A9F')

    LoadEffect(0x00, 'craft\\\\cr162_02.eff')

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearMapFlags(0x00000010)
    OP_22(0x0099, 0x00, 0x64)
    OP_7D(0x00, 0x0102, 0x0078, 0x0FA0)
    SetChrFlags(0x0102, 0x1000)
    SetChrChipByIndex(0x0102, 31)
    SetChrSubChip(0x0102, 0)

    @scena.Lambda('lambda_6AE5')
    def lambda_6AE5():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000190)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_6AE5)

    @scena.Lambda('lambda_6AF7')
    def lambda_6AF7():
        OP_8E(0x00FE, 52830, 0, 12930, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_6AF7)

    @scena.Lambda('lambda_6B12')
    def lambda_6B12():
        OP_99(0x00FE, 0x03, 0x07, 0x00001194)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_6B12)

    @scena.Lambda('lambda_6B22')
    def lambda_6B22():
        OP_6C(225000, 300)

        ExitThread()

    DispatchAsync(0x001D, 0x0000, lambda_6B22)

    @scena.Lambda('lambda_6B32')
    def lambda_6B32():
        OP_67(0, 6300, -10000, 300)

        ExitThread()

    DispatchAsync(0x001D, 0x0001, lambda_6B32)

    OP_6D(34000, 0, 12820, 300)
    WaitForThreadExit(0x0102, 0x0002)
    TerminateThread(0x0102, 0x01)
    TerminateThread(0x0102, 0x03)
    SetChrFlags(0x0102, 0x0080)
    Fade(500)
    OP_6D(50030, 0, 12990, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(90000, 0)
    OP_6E(262, 0)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetMapFlags(0x00000010)
    OP_7D(0x00, 0x0102, 0x0028, 0x03E8)
    ClearChrFlags(0x0102, 0x0080)
    ClearChrFlags(0x0102, 0x0020)
    SetChrFlags(0x0102, 0x1000)
    SetChrPos(0x0102, 49830, 4000, 12930, 90)
    SetChrChipByIndex(0x0102, 30)
    SetChrFlags(0x0102, 0x0020)
    SetChrSubChip(0x0102, 1)

    @scena.Lambda('lambda_6BF4')
    def lambda_6BF4():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000001F4)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_6BF4)

    SetChrFlags(0x0102, 0x0004)

    @scena.Lambda('lambda_6C0B')
    def lambda_6C0B():
        OP_8F(0x00FE, 50030, 0, 12990, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_6C0B)

    WaitForThreadExit(0x0102, 0x0001)
    PlayEffect(0x00, 0xFF, 0x0102, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x00A4, 0x00, 0x64)
    OP_7D(0x01, 0x0102, 0x0000, 0x0000)
    WaitForThreadExit(0x0102, 0x0002)
    Sleep(500)

    ClearChrFlags(0x0102, 0x0020)
    SetChrChipByIndex(0x0102, 65535)
    SetChrSubChip(0x0102, 0)
    ClearChrFlags(0x0102, 0x1000)
    OP_D3(0x1D)
    OP_A2(0x2015)
    EventEnd(0x00)
    SetMapFlags(0x02000000)

    Return()

# id: 0x0034 offset: 0x6C92
@scena.Code('func_34_6C92')
def func_34_6C92():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 3, 0x2013)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0403, 7, 0x201F)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_6C9F',
    )

    Return()

    def _loc_6C9F(): pass

    label('loc_6C9F')

    EventBegin(0x00)
    Fade(500)
    OP_6D(48840, 0, 12980, 0)
    OP_67(0, 5740, -10000, 0)
    OP_6B(1620, 0)
    OP_6C(135000, 0)
    OP_6E(502, 0)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearMapFlags(0x00000010)
    SetChrPos(0x0102, 48840, 0, 12980, 270)
    OP_D2(0x00270019, 0x0027001D, 0x1D)
    OP_D2(0x002600FC, 0x00260101, 0x1E)
    OP_D2(0x00270011, 0x00270015, 0x1F)
    OP_0D()
    LoadEffect(0x00, 'craft\\\\cr162_02.eff')
    Fade(250)
    SetChrChipByIndex(0x0102, 29)
    SetChrSubChip(0x0102, 0)
    OP_0D()
    Sleep(250)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearMapFlags(0x00000010)
    OP_22(0x0099, 0x00, 0x64)
    OP_7D(0x00, 0x0102, 0x0078, 0x0FA0)
    SetChrFlags(0x0102, 0x1000)
    SetChrChipByIndex(0x0102, 31)

    @scena.Lambda('lambda_6D77')
    def lambda_6D77():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000190)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_6D77)

    @scena.Lambda('lambda_6D89')
    def lambda_6D89():
        OP_8E(0x00FE, 24990, 0, 12520, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_6D89)

    @scena.Lambda('lambda_6DA4')
    def lambda_6DA4():
        OP_6C(150000, 300)

        ExitThread()

    DispatchAsync(0x001D, 0x0000, lambda_6DA4)

    @scena.Lambda('lambda_6DB4')
    def lambda_6DB4():
        OP_67(0, 6300, -10000, 300)

        ExitThread()

    DispatchAsync(0x001D, 0x0001, lambda_6DB4)

    OP_6D(41000, 0, 12960, 300)
    WaitForThreadExit(0x0102, 0x0002)
    TerminateThread(0x0102, 0x01)
    TerminateThread(0x0102, 0x03)
    SetChrFlags(0x0102, 0x0080)
    Fade(500)
    OP_6D(24400, 0, 12550, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(270000, 0)
    OP_6E(262, 0)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetMapFlags(0x00000010)
    OP_7D(0x00, 0x0102, 0x0028, 0x03E8)
    ClearChrFlags(0x0102, 0x0080)
    SetChrFlags(0x0102, 0x1000)
    SetChrPos(0x0102, 24400, 4000, 12550, 270)
    SetChrChipByIndex(0x0102, 30)
    SetChrFlags(0x0102, 0x0020)
    SetChrSubChip(0x0102, 1)

    @scena.Lambda('lambda_6E71')
    def lambda_6E71():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000001F4)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_6E71)

    SetChrFlags(0x0102, 0x0004)

    @scena.Lambda('lambda_6E88')
    def lambda_6E88():
        OP_8F(0x00FE, 24400, 0, 12550, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_6E88)

    WaitForThreadExit(0x0102, 0x0001)
    PlayEffect(0x00, 0xFF, 0x0102, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x00A4, 0x00, 0x64)
    OP_7D(0x01, 0x0102, 0x0000, 0x0000)
    WaitForThreadExit(0x0102, 0x0002)
    Sleep(500)

    ClearChrFlags(0x0102, 0x0020)
    SetChrChipByIndex(0x0102, 65535)
    SetChrSubChip(0x0102, 0)
    ClearChrFlags(0x0102, 0x1000)
    OP_D3(0x1D)
    EventEnd(0x00)
    SetMapFlags(0x02000000)

    Return()

# id: 0x0035 offset: 0x6F0C
@scena.Code('func_35_6F0C')
def func_35_6F0C():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 6, 0x2016)),
            Expr.Return,
        ),
        'loc_7052',
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeOut(300, 0, 100)
    OP_57(0x00C8, 0x0014, 0x000C, '#5CLook inside again?')
    OP_CC(0x00, 0x00, 0x000A, 0x000A, 0x00)
    OP_CC(0x01, 0x00, '【是】')
    OP_CC(0x01, 0x00, '【否】')
    OP_CC(0x02, 0x00)
    MenuEnd(0x0000)
    FadeIn(300, 0)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_DA()

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_6F96'),
        (0x00000001, 'loc_7040'),
        (-1, 'loc_704F'),
    )

    def _loc_6F96(): pass

    label('loc_6F96')

    EventBegin(0x00)

    If(
        (
            (Expr.PushValueByIndex, 0x64),
            (Expr.PushLong, 0xB4),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_6FDB',
    )

    Fade(500)
    SetChrPos(0x0102, 56980, 0, 13500, 0)
    OP_6D(56980, 0, 13500, 0)
    OP_6C(285000, 0)
    OP_A3(0x2030)
    OP_0D()

    Jump('loc_700F')

    def _loc_6FDB(): pass

    label('loc_6FDB')

    Fade(500)
    SetChrPos(0x0102, 56980, 0, 13500, 0)
    OP_6D(56980, 0, 13500, 0)
    OP_6C(75000, 0)
    OP_A2(0x2030)
    OP_0D()

    def _loc_700F(): pass

    label('loc_700F')

    @scena.Lambda('lambda_7015')
    def lambda_7015():
        OP_6E(241, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_7015)

    Sleep(1000)

    FadeOut(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x02000000)
    OP_A2(0x10F2)
    NewScene('ED6_DT21/T2511._SN', 100, 0, 0)
    IdleLoop()

    def _loc_7040(): pass

    label('loc_7040')

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)

    Jump('loc_704F')

    def _loc_704F(): pass

    label('loc_704F')

    Jump('loc_70FC')

    def _loc_7052(): pass

    label('loc_7052')

    EventBegin(0x00)

    If(
        (
            (Expr.PushValueByIndex, 0x64),
            (Expr.PushLong, 0xB4),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_7097',
    )

    Fade(500)
    SetChrPos(0x0102, 56980, 0, 13500, 0)
    OP_6D(56980, 0, 13500, 0)
    OP_6C(285000, 0)
    OP_A3(0x2030)
    OP_0D()

    Jump('loc_70CB')

    def _loc_7097(): pass

    label('loc_7097')

    Fade(500)
    SetChrPos(0x0102, 56980, 0, 13500, 0)
    OP_6D(56980, 0, 13500, 0)
    OP_6C(75000, 0)
    OP_A2(0x2030)
    OP_0D()

    def _loc_70CB(): pass

    label('loc_70CB')

    @scena.Lambda('lambda_70D1')
    def lambda_70D1():
        OP_6E(241, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_70D1)

    Sleep(1000)

    FadeOut(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x02000000)
    OP_A2(0x10F2)
    NewScene('ED6_DT21/T2511._SN', 100, 0, 0)
    IdleLoop()
    def _loc_70FC(): pass

    label('loc_70FC')

    TalkEnd(0x00FF)

    Return()

# id: 0x0036 offset: 0x7100
@scena.Code('func_36_7100')
def func_36_7100():
    EventBegin(0x00)
    OP_6D(56980, 0, 13500, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6E(262, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0406, 0, 0x2030)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_714A',
    )

    OP_6C(285000, 0)

    Jump('loc_7153')

    def _loc_714A(): pass

    label('loc_714A')

    OP_6C(75000, 0)

    def _loc_7153(): pass

    label('loc_7153')

    SetChrPos(0x0102, 56980, 0, 13500, 0)
    FadeIn(1000, 0)
    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 6, 0x2016)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7208',
    )

    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020360598V#1043F（敌方士兵四名……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020360599V（以防万一的\n',
            '  待命人员吗。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020360600V#1042F（或许人质\n',
            '  在二楼也不一定。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x2016)

    def _loc_7208(): pass

    label('loc_7208')

    Call(0, 0x004C)
    EventEnd(0x00)
    SetMapFlags(0x02000000)

    Return()

# id: 0x0037 offset: 0x7214
@scena.Code('func_37_7214')
def func_37_7214():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 3, 0x2013)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0403, 7, 0x201F)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_7221',
    )

    Return()

    def _loc_7221(): pass

    label('loc_7221')

    EventBegin(0x01)
    Fade(500)
    SetChrPos(0x0018, 38350, 350, 27790, 315)
    ClearChrFlags(0x0018, 0x0080)
    SetChrChipByIndex(0x0018, 23)
    SetChrSubChip(0x0018, 0)
    CreateThread(0x0018, 0x00, 0x00, 0x0002)
    OP_6C(270000, 0)
    OP_8C(0x0102, 270, 0)
    OP_69(0x0102, 0x00000000)
    OP_0D()
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_7289')
    def lambda_7289():
        OP_6D(36580, 0, 27680, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0000, lambda_7289)

    @scena.Lambda('lambda_72A1')
    def lambda_72A1():
        OP_67(0, 7500, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_72A1)

    @scena.Lambda('lambda_72B9')
    def lambda_72B9():
        OP_6B(2300, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_72B9)

    @scena.Lambda('lambda_72C9')
    def lambda_72C9():
        OP_6C(270000, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_72C9)

    @scena.Lambda('lambda_72D9')
    def lambda_72D9():
        OP_6E(321, 3000)

        ExitThread()

    DispatchAsync(0x0018, 0x0003, lambda_72D9)

    If(
        (
            (Expr.GetChrWork, 0x102, 0x3),
            (Expr.PushLong, 0x6F36),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_731C',
    )

    OP_90(0x0102, 600, 0, 0, 5000, 0x00)
    OP_8E(0x0102, 54910, 0, 31450, 5000, 0x00)

    Jump('loc_7344')

    def _loc_731C(): pass

    label('loc_731C')

    OP_90(0x0102, 600, 0, 0, 5000, 0x00)
    OP_8E(0x0102, 54910, 0, 25490, 5000, 0x00)

    def _loc_7344(): pass

    label('loc_7344')

    OP_8C(0x0102, 90, 400)
    Sleep(700)

    WaitForThreadExit(0x0101, 0x0000)
    Sleep(500)

    Fade(500)
    OP_69(0x0102, 0x00000000)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(270000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x0018, 0x0080)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020360601V#1042F（……外面有巡逻。\n',
            '  从里面通过比较好。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(50)

    EventEnd(0x04)
    SetMapFlags(0x02000000)

    Return()

# id: 0x0038 offset: 0x73EB
@scena.Code('func_38_73EB')
def func_38_73EB():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 3, 0x2013)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0403, 7, 0x201F)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_73F8',
    )

    Return()

    def _loc_73F8(): pass

    label('loc_73F8')

    EventBegin(0x01)
    Fade(500)
    SetChrPos(0x0018, 36310, 350, 64080, 225)
    ClearChrFlags(0x0018, 0x0080)
    SetChrChipByIndex(0x0018, 23)
    SetChrSubChip(0x0018, 0)
    CreateThread(0x0018, 0x00, 0x00, 0x0002)
    OP_6C(270000, 0)
    OP_8C(0x0102, 270, 0)
    OP_69(0x0102, 0x00000000)
    OP_0D()
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_7460')
    def lambda_7460():
        OP_6D(34720, 0, 63840, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0000, lambda_7460)

    @scena.Lambda('lambda_7478')
    def lambda_7478():
        OP_67(0, 7500, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_7478)

    @scena.Lambda('lambda_7490')
    def lambda_7490():
        OP_6B(2300, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_7490)

    @scena.Lambda('lambda_74A0')
    def lambda_74A0():
        OP_6C(270000, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_74A0)

    @scena.Lambda('lambda_74B0')
    def lambda_74B0():
        OP_6E(321, 3000)

        ExitThread()

    DispatchAsync(0x0018, 0x0003, lambda_74B0)

    If(
        (
            (Expr.GetChrWork, 0x102, 0x3),
            (Expr.PushLong, 0xF816),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_74F3',
    )

    OP_90(0x0102, 600, 0, 0, 5000, 0x00)
    OP_8E(0x0102, 54910, 0, 66570, 5000, 0x00)

    Jump('loc_751B')

    def _loc_74F3(): pass

    label('loc_74F3')

    OP_90(0x0102, 600, 0, 0, 5000, 0x00)
    OP_8E(0x0102, 54910, 0, 60450, 5000, 0x00)

    def _loc_751B(): pass

    label('loc_751B')

    OP_8C(0x0102, 90, 400)
    Sleep(700)

    WaitForThreadExit(0x0101, 0x0000)
    Sleep(500)

    Fade(500)
    OP_69(0x0102, 0x00000000)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(270000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x0018, 0x0080)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020360602V#1042F（……外面有巡逻。\n',
            '  从里面通过比较好。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(50)

    EventEnd(0x04)
    SetMapFlags(0x02000000)

    Return()

# id: 0x0039 offset: 0x75C2
@scena.Code('func_39_75C2')
def func_39_75C2():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0403, 0, 0x2018)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_763A',
    )

    EventBegin(0x00)
    OP_A2(0x2018)
    OP_28(0x00C0, 0x01, 0x0002)
    Fade(500)
    SetChrPos(0x0102, 58500, 0, 36000, 270)
    OP_6D(58500, 0, 36000, 0)
    OP_6C(285000, 0)
    OP_0D()

    @scena.Lambda('lambda_760C')
    def lambda_760C():
        OP_6E(241, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_760C)

    Sleep(1000)

    FadeOut(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x02000000)
    OP_A2(0x10F1)
    NewScene('ED6_DT21/T2510._SN', 114, 0, 0)
    IdleLoop()

    Jump('loc_76A0')

    def _loc_763A(): pass

    label('loc_763A')

    ChrTalk(
        0x0102,
        (
            '#0020360635V#1043F（……好像还在\n',
            '  继续说话。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020360636V#1042F（去其它地方调查看看吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FF)

    def _loc_76A0(): pass

    label('loc_76A0')

    Return()

# id: 0x003A offset: 0x76A1
@scena.Code('func_3A_76A1')
def func_3A_76A1():
    EventBegin(0x00)
    SetChrPos(0x0102, 58500, 0, 36000, 270)
    OP_6D(58500, 0, 36000, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(285000, 0)
    OP_6E(262, 0)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020360633V#1035F（难道他就是这次的主谋吗……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020360634V#1043F（说起来的话，\n',
            '  记得他好像是这学院的毕业生啊。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(0, 0x004C)
    EventEnd(0x00)
    SetMapFlags(0x02000000)

    Return()

# id: 0x003B offset: 0x7787
@scena.Code('func_3B_7787')
def func_3B_7787():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0403, 1, 0x2019)),
            Expr.Return,
        ),
        'loc_7885',
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeOut(300, 0, 100)
    OP_57(0x00C8, 0x0014, 0x000C, '#5CLook inside again?')
    OP_CC(0x00, 0x00, 0x000A, 0x000A, 0x00)
    OP_CC(0x01, 0x00, '【是】')
    OP_CC(0x01, 0x00, '【否】')
    OP_CC(0x02, 0x00)
    MenuEnd(0x0000)
    FadeIn(300, 0)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_DA()

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_7811'),
        (0x00000001, 'loc_7873'),
        (-1, 'loc_7882'),
    )

    def _loc_7811(): pass

    label('loc_7811')

    Fade(500)
    SetChrPos(0x0102, 58510, 0, 40110, 270)
    OP_6D(58510, 0, 40110, 0)
    OP_6C(285000, 0)
    OP_0D()

    @scena.Lambda('lambda_7848')
    def lambda_7848():
        OP_6E(241, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_7848)

    Sleep(1000)

    FadeOut(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x02000000)
    OP_A2(0x10F2)
    NewScene('ED6_DT21/T2510._SN', 113, 0, 0)
    IdleLoop()

    def _loc_7873(): pass

    label('loc_7873')

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)

    Jump('loc_7882')

    def _loc_7882(): pass

    label('loc_7882')

    Jump('loc_78E7')

    def _loc_7885(): pass

    label('loc_7885')

    Fade(500)
    SetChrPos(0x0102, 58510, 0, 40110, 270)
    OP_6D(58510, 0, 40110, 0)
    OP_6C(285000, 0)
    OP_0D()

    @scena.Lambda('lambda_78BC')
    def lambda_78BC():
        OP_6E(241, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_78BC)

    Sleep(1000)

    FadeOut(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x02000000)
    OP_A2(0x10F2)
    NewScene('ED6_DT21/T2510._SN', 113, 0, 0)
    IdleLoop()
    def _loc_78E7(): pass

    label('loc_78E7')

    TalkEnd(0x00FF)

    Return()

# id: 0x003C offset: 0x78EB
@scena.Code('func_3C_78EB')
def func_3C_78EB():
    EventBegin(0x00)
    SetChrPos(0x0102, 58510, 0, 40110, 270)
    OP_6D(58510, 0, 40110, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(285000, 0)
    OP_6E(262, 0)
    FadeIn(1000, 0)
    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0403, 1, 0x2019)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_79B8',
    )

    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020360637V#1043F（没有发现教师……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020360638V#1035F（大概是被监禁\n',
            '  到其它地方了吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x2019)

    def _loc_79B8(): pass

    label('loc_79B8')

    Call(0, 0x004C)
    EventEnd(0x00)
    SetMapFlags(0x02000000)

    Return()

# id: 0x003D offset: 0x79C4
@scena.Code('func_3D_79C4')
def func_3D_79C4():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0403, 2, 0x201A)),
            Expr.Return,
        ),
        'loc_7B0A',
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeOut(300, 0, 100)
    OP_57(0x00C8, 0x0014, 0x000C, '#5CLook inside again?')
    OP_CC(0x00, 0x00, 0x000A, 0x000A, 0x00)
    OP_CC(0x01, 0x00, '【是】')
    OP_CC(0x01, 0x00, '【否】')
    OP_CC(0x02, 0x00)
    MenuEnd(0x0000)
    FadeIn(300, 0)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_DA()

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_7A4E'),
        (0x00000001, 'loc_7AF8'),
        (-1, 'loc_7B07'),
    )

    def _loc_7A4E(): pass

    label('loc_7A4E')

    EventBegin(0x00)

    If(
        (
            (Expr.PushValueByIndex, 0x64),
            (Expr.PushLong, 0x10E),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_7A93',
    )

    Fade(500)
    SetChrPos(0x0102, 59500, 0, 46040, 270)
    OP_6D(59500, 0, 46040, 0)
    OP_6C(315000, 0)
    OP_A3(0x2030)
    OP_0D()

    Jump('loc_7AC7')

    def _loc_7A93(): pass

    label('loc_7A93')

    Fade(500)
    SetChrPos(0x0102, 59500, 0, 46040, 270)
    OP_6D(59500, 0, 46040, 0)
    OP_6C(225000, 0)
    OP_A2(0x2030)
    OP_0D()

    def _loc_7AC7(): pass

    label('loc_7AC7')

    @scena.Lambda('lambda_7ACD')
    def lambda_7ACD():
        OP_6E(241, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_7ACD)

    Sleep(1000)

    FadeOut(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x02000000)
    OP_A2(0x10F3)
    NewScene('ED6_DT21/T2510._SN', 100, 0, 0)
    IdleLoop()

    def _loc_7AF8(): pass

    label('loc_7AF8')

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)

    Jump('loc_7B07')

    def _loc_7B07(): pass

    label('loc_7B07')

    Jump('loc_7BB4')

    def _loc_7B0A(): pass

    label('loc_7B0A')

    EventBegin(0x00)

    If(
        (
            (Expr.PushValueByIndex, 0x64),
            (Expr.PushLong, 0x10E),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_7B4F',
    )

    Fade(500)
    SetChrPos(0x0102, 59500, 0, 46040, 270)
    OP_6D(59500, 0, 46040, 0)
    OP_6C(315000, 0)
    OP_A3(0x2030)
    OP_0D()

    Jump('loc_7B83')

    def _loc_7B4F(): pass

    label('loc_7B4F')

    Fade(500)
    SetChrPos(0x0102, 59500, 0, 46040, 270)
    OP_6D(59500, 0, 46040, 0)
    OP_6C(225000, 0)
    OP_A2(0x2030)
    OP_0D()

    def _loc_7B83(): pass

    label('loc_7B83')

    @scena.Lambda('lambda_7B89')
    def lambda_7B89():
        OP_6E(241, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_7B89)

    Sleep(1000)

    FadeOut(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x02000000)
    OP_A2(0x10F3)
    NewScene('ED6_DT21/T2510._SN', 100, 0, 0)
    IdleLoop()
    def _loc_7BB4(): pass

    label('loc_7BB4')

    TalkEnd(0x00FF)

    Return()

# id: 0x003E offset: 0x7BB8
@scena.Code('func_3E_7BB8')
def func_3E_7BB8():
    EventBegin(0x00)
    OP_6D(59500, 0, 46040, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6E(262, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0406, 0, 0x2030)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7C02',
    )

    OP_6C(315000, 0)

    Jump('loc_7C0B')

    def _loc_7C02(): pass

    label('loc_7C02')

    OP_6C(225000, 0)

    def _loc_7C0B(): pass

    label('loc_7C0B')

    SetChrPos(0x0102, 59500, 0, 46040, 270)
    FadeIn(1000, 0)
    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0403, 2, 0x201A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7CA7',
    )

    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020360639V#1042F（虽然有死角看不到，\n',
            '  但可以感觉到走廊上有人……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020360640V（大概是看守的士兵吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x201A)

    def _loc_7CA7(): pass

    label('loc_7CA7')

    Call(0, 0x004C)
    EventEnd(0x00)
    SetMapFlags(0x02000000)

    Return()

# id: 0x003F offset: 0x7CB3
@scena.Code('func_3F_7CB3')
def func_3F_7CB3():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0403, 3, 0x201B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7D4E',
    )

    EventBegin(0x00)
    OP_A2(0x201B)
    Fade(500)
    OP_6D(58500, 0, 51970, 0)
    SetChrPos(0x0102, 58500, 0, 51970, 270)
    OP_6C(225000, 0)
    OP_0D()
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0102,
        (
            '#0020360641V#1044F（啊……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x02000000)
    OP_A2(0x10F4)
    NewScene('ED6_DT21/T2510._SN', 111, 0, 0)
    IdleLoop()

    Jump('loc_7DC4')

    def _loc_7D4E(): pass

    label('loc_7D4E')

    ChrTalk(
        0x0102,
        (
            '#0020360682V#1043F（……说太久的话\n',
            '  也许会被看守的士兵发现。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020360683V#1042F（去其它地方调查看看吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FF)

    def _loc_7DC4(): pass

    label('loc_7DC4')

    Return()

# id: 0x0040 offset: 0x7DC5
@scena.Code('func_40_7DC5')
def func_40_7DC5():
    EventBegin(0x00)
    SetChrPos(0x0102, 58500, 0, 51970, 270)
    OP_6D(58500, 0, 51970, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020360646V#1040F#6P（……安静些，汉斯。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020360647V（声音太大的话\n',
            '  会被看守的士兵发现啊。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(352, 0, -1, -1)
    SetChrName('汉斯')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0520360648V#732F（知、知道了……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520360649V#734F（……不过你啊，）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520360650V（在这种情况下突然冒出来，\n',
            '  让人怎么能不吃惊嘛。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(
        0x0102,
        (
            '#0020360651V#1054F#6P（哈哈……抱歉。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x10F5)
    NewScene('ED6_DT21/T2510._SN', 111, 0, 0)
    IdleLoop()

    Return()

# id: 0x0041 offset: 0x7F65
@scena.Code('func_41_7F65')
def func_41_7F65():
    EventBegin(0x00)
    SetChrPos(0x0102, 58500, 0, 51970, 270)
    OP_6D(58500, 0, 51970, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)
    Sleep(500)

    SetMessageWindowPos(360, 50, -1, -1)
    SetChrName('汉斯')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0520360658V#734F（总之一定切记\n',
            '  声音不要太大啊……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(300, 0, -1, -1)
    SetChrName('乔儿')

    Talk(
        (
            '#0510360659V#645F（太、太吃惊了！）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510360660V#644F（为什么约修亚\n',
            '  会在这里呢！？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(
        0x0102,
        (
            '#0020360661V#1040F#6P（好久不见了啊，乔儿。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020360662V#1035F（现在时间紧迫，\n',
            '  我只能长话短说……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '约修亚把至今为止发生的一切，以及从米克\n',
            '那里听说学院发生了异变等事情做了个说明。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x10F6)
    NewScene('ED6_DT21/T2510._SN', 111, 0, 0)
    IdleLoop()

    Return()

# id: 0x0042 offset: 0x8175
@scena.Code('func_42_8175')
def func_42_8175():
    EventBegin(0x00)
    SetChrPos(0x0102, 58500, 0, 51970, 270)
    OP_6D(58500, 0, 51970, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)
    FadeIn(1000, 0)
    OP_0D()
    Call(0, 0x004C)
    EventEnd(0x00)
    SetMapFlags(0x02000000)

    Return()

# id: 0x0043 offset: 0x81DB
@scena.Code('func_43_81DB')
def func_43_81DB():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0403, 4, 0x201C)),
            Expr.Return,
        ),
        'loc_8321',
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeOut(300, 0, 100)
    OP_57(0x00C8, 0x0014, 0x000C, '#5CLook inside again?')
    OP_CC(0x00, 0x00, 0x000A, 0x000A, 0x00)
    OP_CC(0x01, 0x00, '【是】')
    OP_CC(0x01, 0x00, '【否】')
    OP_CC(0x02, 0x00)
    MenuEnd(0x0000)
    FadeIn(300, 0)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_DA()

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_8265'),
        (0x00000001, 'loc_830F'),
        (-1, 'loc_831E'),
    )

    def _loc_8265(): pass

    label('loc_8265')

    EventBegin(0x00)

    If(
        (
            (Expr.PushValueByIndex, 0x64),
            (Expr.PushLong, 0xB4),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_82AA',
    )

    Fade(500)
    SetChrPos(0x0102, 48830, 0, 80500, 180)
    OP_6D(48830, 0, 80500, 0)
    OP_6C(105000, 0)
    OP_A3(0x2030)
    OP_0D()

    Jump('loc_82DE')

    def _loc_82AA(): pass

    label('loc_82AA')

    Fade(500)
    SetChrPos(0x0102, 48830, 0, 80500, 180)
    OP_6D(48830, 0, 80500, 0)
    OP_6C(255000, 0)
    OP_A2(0x2030)
    OP_0D()

    def _loc_82DE(): pass

    label('loc_82DE')

    @scena.Lambda('lambda_82E4')
    def lambda_82E4():
        OP_6E(241, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_82E4)

    Sleep(1000)

    FadeOut(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x02000000)
    OP_A2(0x10F0)
    NewScene('ED6_DT21/T2513._SN', 100, 0, 0)
    IdleLoop()

    def _loc_830F(): pass

    label('loc_830F')

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)

    Jump('loc_831E')

    def _loc_831E(): pass

    label('loc_831E')

    Jump('loc_83CB')

    def _loc_8321(): pass

    label('loc_8321')

    EventBegin(0x00)

    If(
        (
            (Expr.PushValueByIndex, 0x64),
            (Expr.PushLong, 0xB4),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_8366',
    )

    Fade(500)
    SetChrPos(0x0102, 48830, 0, 80500, 180)
    OP_6D(48830, 0, 80500, 0)
    OP_6C(105000, 0)
    OP_A3(0x2030)
    OP_0D()

    Jump('loc_839A')

    def _loc_8366(): pass

    label('loc_8366')

    Fade(500)
    SetChrPos(0x0102, 48830, 0, 80500, 180)
    OP_6D(48830, 0, 80500, 0)
    OP_6C(255000, 0)
    OP_A2(0x2030)
    OP_0D()

    def _loc_839A(): pass

    label('loc_839A')

    @scena.Lambda('lambda_83A0')
    def lambda_83A0():
        OP_6E(241, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_83A0)

    Sleep(1000)

    FadeOut(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x02000000)
    OP_A2(0x10F0)
    NewScene('ED6_DT21/T2513._SN', 100, 0, 0)
    IdleLoop()
    def _loc_83CB(): pass

    label('loc_83CB')

    TalkEnd(0x00FF)

    Return()

# id: 0x0044 offset: 0x83CF
@scena.Code('func_44_83CF')
def func_44_83CF():
    EventBegin(0x00)
    OP_6D(48830, 0, 80500, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6E(262, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0406, 0, 0x2030)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8419',
    )

    OP_6C(105000, 0)

    Jump('loc_8422')

    def _loc_8419(): pass

    label('loc_8419')

    OP_6C(255000, 0)

    def _loc_8422(): pass

    label('loc_8422')

    SetChrPos(0x0102, 48830, 0, 80500, 180)
    FadeIn(1000, 0)
    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0403, 4, 0x201C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_84B2',
    )

    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020360684V#1040F（休息室这里很安静，\n',
            '  不像有人的样子……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020360685V（这里应该没有人。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x201C)

    def _loc_84B2(): pass

    label('loc_84B2')

    Call(0, 0x004C)
    EventEnd(0x00)
    SetMapFlags(0x02000000)

    Return()

# id: 0x0045 offset: 0x84BE
@scena.Code('func_45_84BE')
def func_45_84BE():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 3, 0x2013)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0403, 7, 0x201F)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_84CB',
    )

    Return()

    def _loc_84CB(): pass

    label('loc_84CB')

    EventBegin(0x00)
    Fade(500)
    OP_6D(43190, 0, 81780, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(1600, 0)
    OP_6C(45000, 0)
    OP_6E(499, 0)
    SetChrPos(0x0102, 43040, 0, 81120, 270)
    OP_D2(0x00270019, 0x0027001D, 0x1D)
    OP_D2(0x002600FC, 0x00260101, 0x1E)
    OP_D2(0x00270011, 0x00270015, 0x1F)
    OP_0D()
    LoadEffect(0x00, 'craft\\\\cr162_02.eff')
    Fade(250)
    SetChrChipByIndex(0x0102, 29)
    SetChrSubChip(0x0102, 0)
    OP_0D()
    Sleep(250)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearMapFlags(0x00000010)
    OP_22(0x0099, 0x00, 0x64)
    OP_7D(0x00, 0x0102, 0x0078, 0x0FA0)
    SetChrFlags(0x0102, 0x1000)
    SetChrChipByIndex(0x0102, 31)
    SetChrSubChip(0x0102, 0)

    @scena.Lambda('lambda_859A')
    def lambda_859A():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000190)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_859A)

    @scena.Lambda('lambda_85AC')
    def lambda_85AC():
        OP_8E(0x00FE, 25680, 0, 80960, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_85AC)

    @scena.Lambda('lambda_85C7')
    def lambda_85C7():
        OP_99(0x00FE, 0x03, 0x07, 0x00001194)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_85C7)

    @scena.Lambda('lambda_85D7')
    def lambda_85D7():
        OP_6C(30000, 300)

        ExitThread()

    DispatchAsync(0x001D, 0x0000, lambda_85D7)

    @scena.Lambda('lambda_85E7')
    def lambda_85E7():
        OP_67(0, 6300, -10000, 300)

        ExitThread()

    DispatchAsync(0x001D, 0x0001, lambda_85E7)

    OP_6D(36000, 0, 81030, 300)
    WaitForThreadExit(0x0102, 0x0002)
    TerminateThread(0x0102, 0x01)
    TerminateThread(0x0102, 0x03)
    SetChrFlags(0x0102, 0x0080)
    Fade(500)
    OP_6D(25160, 0, 80940, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(270000, 0)
    OP_6E(262, 0)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetMapFlags(0x00000010)
    OP_7D(0x00, 0x0102, 0x0028, 0x03E8)
    ClearChrFlags(0x0102, 0x0080)
    SetChrFlags(0x0102, 0x1000)
    SetChrPos(0x0102, 25160, 4000, 80940, 270)
    SetChrChipByIndex(0x0102, 30)
    SetChrFlags(0x0102, 0x0020)
    SetChrSubChip(0x0102, 1)

    @scena.Lambda('lambda_86A4')
    def lambda_86A4():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000001F4)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_86A4)

    SetChrFlags(0x0102, 0x0004)

    @scena.Lambda('lambda_86BB')
    def lambda_86BB():
        OP_8F(0x00FE, 25160, 0, 80940, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_86BB)

    WaitForThreadExit(0x0102, 0x0001)
    PlayEffect(0x00, 0xFF, 0x0102, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x00A4, 0x00, 0x64)
    WaitForThreadExit(0x0102, 0x0002)
    OP_7D(0x01, 0x0102, 0x0000, 0x0000)
    Sleep(500)

    ClearChrFlags(0x0102, 0x0020)
    SetChrChipByIndex(0x0102, 65535)
    SetChrSubChip(0x0102, 0)
    ClearChrFlags(0x0102, 0x1000)
    OP_D3(0x1D)
    EventEnd(0x00)
    SetMapFlags(0x02000000)

    Return()

# id: 0x0046 offset: 0x873F
@scena.Code('func_46_873F')
def func_46_873F():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 3, 0x2013)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0403, 7, 0x201F)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_874C',
    )

    Return()

    def _loc_874C(): pass

    label('loc_874C')

    EventBegin(0x00)
    Fade(500)
    OP_6D(26220, 0, 80980, 0)
    OP_67(0, 5920, -10000, 0)
    OP_6B(1620, 0)
    OP_6C(312000, 0)
    OP_6E(499, 0)
    SetChrPos(0x0102, 26220, 0, 80980, 90)
    OP_D2(0x00270019, 0x0027001D, 0x1D)
    OP_D2(0x002600FC, 0x00260101, 0x1E)
    OP_D2(0x00270011, 0x00270015, 0x1F)
    OP_0D()
    LoadEffect(0x00, 'craft\\\\cr162_02.eff')
    Fade(250)
    SetChrChipByIndex(0x0102, 29)
    SetChrSubChip(0x0102, 0)
    OP_0D()
    Sleep(250)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearMapFlags(0x00000010)
    OP_22(0x0099, 0x00, 0x64)
    OP_7D(0x00, 0x0102, 0x0078, 0x0FA0)
    SetChrFlags(0x0102, 0x1000)
    SetChrChipByIndex(0x0102, 31)
    SetChrSubChip(0x0102, 0)

    @scena.Lambda('lambda_881B')
    def lambda_881B():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000190)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_881B)

    @scena.Lambda('lambda_882D')
    def lambda_882D():
        OP_8E(0x00FE, 43070, 0, 80970, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_882D)

    @scena.Lambda('lambda_8848')
    def lambda_8848():
        OP_99(0x00FE, 0x03, 0x07, 0x00001194)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_8848)

    @scena.Lambda('lambda_8858')
    def lambda_8858():
        OP_6C(330000, 300)

        ExitThread()

    DispatchAsync(0x001D, 0x0000, lambda_8858)

    @scena.Lambda('lambda_8868')
    def lambda_8868():
        OP_67(0, 6300, -10000, 300)

        ExitThread()

    DispatchAsync(0x001D, 0x0001, lambda_8868)

    OP_6D(34000, 0, 80920, 300)
    WaitForThreadExit(0x0102, 0x0002)
    TerminateThread(0x0102, 0x01)
    TerminateThread(0x0102, 0x03)
    SetChrFlags(0x0102, 0x0080)
    Fade(500)
    OP_6D(44120, 0, 80990, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(90000, 0)
    OP_6E(262, 0)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetMapFlags(0x00000010)
    OP_7D(0x00, 0x0102, 0x0028, 0x03E8)
    ClearChrFlags(0x0102, 0x0080)
    SetChrFlags(0x0102, 0x1000)
    SetChrPos(0x0102, 44120, 4000, 80990, 90)
    SetChrChipByIndex(0x0102, 30)
    SetChrFlags(0x0102, 0x0020)
    SetChrSubChip(0x0102, 1)

    @scena.Lambda('lambda_8925')
    def lambda_8925():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000001F4)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_8925)

    SetChrFlags(0x0102, 0x0004)

    @scena.Lambda('lambda_893C')
    def lambda_893C():
        OP_8F(0x00FE, 44120, 0, 80990, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_893C)

    WaitForThreadExit(0x0102, 0x0001)
    PlayEffect(0x00, 0xFF, 0x0102, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x00A4, 0x00, 0x64)
    WaitForThreadExit(0x0102, 0x0002)
    OP_7D(0x01, 0x0102, 0x0000, 0x0000)
    Sleep(500)

    ClearChrFlags(0x0102, 0x0020)
    SetChrChipByIndex(0x0102, 65535)
    SetChrSubChip(0x0102, 0)
    ClearChrFlags(0x0102, 0x1000)
    OP_D3(0x1D)
    EventEnd(0x00)
    SetMapFlags(0x02000000)

    Return()

# id: 0x0047 offset: 0x89C0
@scena.Code('func_47_89C0')
def func_47_89C0():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0403, 5, 0x201D)),
            Expr.Return,
        ),
        'loc_8B06',
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeOut(300, 0, 100)
    OP_57(0x00C8, 0x0014, 0x000C, '#5CLook inside again?')
    OP_CC(0x00, 0x00, 0x000A, 0x000A, 0x00)
    OP_CC(0x01, 0x00, '【是】')
    OP_CC(0x01, 0x00, '【否】')
    OP_CC(0x02, 0x00)
    MenuEnd(0x0000)
    FadeIn(300, 0)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_DA()

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_8A4A'),
        (0x00000001, 'loc_8AF4'),
        (-1, 'loc_8B03'),
    )

    def _loc_8A4A(): pass

    label('loc_8A4A')

    EventBegin(0x00)

    If(
        (
            (Expr.PushValueByIndex, 0x64),
            (Expr.PushLong, 0x5A),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_8A8F',
    )

    Fade(500)
    SetChrPos(0x0102, 16480, 0, 76930, 90)
    OP_6D(16480, 0, 76930, 0)
    OP_6C(150000, 0)
    OP_A3(0x2030)
    OP_0D()

    Jump('loc_8AC3')

    def _loc_8A8F(): pass

    label('loc_8A8F')

    Fade(500)
    SetChrPos(0x0102, 16480, 0, 76930, 90)
    OP_6D(16480, 0, 76930, 0)
    OP_6C(30000, 0)
    OP_A2(0x2030)
    OP_0D()

    def _loc_8AC3(): pass

    label('loc_8AC3')

    @scena.Lambda('lambda_8AC9')
    def lambda_8AC9():
        OP_6E(241, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_8AC9)

    Sleep(1000)

    FadeOut(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x02000000)
    OP_A2(0x10F3)
    NewScene('ED6_DT21/T2512._SN', 116, 0, 0)
    IdleLoop()

    def _loc_8AF4(): pass

    label('loc_8AF4')

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)

    Jump('loc_8B03')

    def _loc_8B03(): pass

    label('loc_8B03')

    Jump('loc_8BB0')

    def _loc_8B06(): pass

    label('loc_8B06')

    EventBegin(0x00)

    If(
        (
            (Expr.PushValueByIndex, 0x64),
            (Expr.PushLong, 0x5A),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_8B4B',
    )

    Fade(500)
    SetChrPos(0x0102, 16480, 0, 76930, 90)
    OP_6D(16480, 0, 76930, 0)
    OP_6C(150000, 0)
    OP_A3(0x2030)
    OP_0D()

    Jump('loc_8B7F')

    def _loc_8B4B(): pass

    label('loc_8B4B')

    Fade(500)
    SetChrPos(0x0102, 16480, 0, 76930, 90)
    OP_6D(16480, 0, 76930, 0)
    OP_6C(30000, 0)
    OP_A2(0x2030)
    OP_0D()

    def _loc_8B7F(): pass

    label('loc_8B7F')

    @scena.Lambda('lambda_8B85')
    def lambda_8B85():
        OP_6E(241, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_8B85)

    Sleep(1000)

    FadeOut(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x02000000)
    OP_A2(0x10F3)
    NewScene('ED6_DT21/T2512._SN', 116, 0, 0)
    IdleLoop()
    def _loc_8BB0(): pass

    label('loc_8BB0')

    TalkEnd(0x00FF)

    Return()

# id: 0x0048 offset: 0x8BB4
@scena.Code('func_48_8BB4')
def func_48_8BB4():
    EventBegin(0x00)
    OP_6D(16480, 0, 76930, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6E(262, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0406, 0, 0x2030)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8BFE',
    )

    OP_6C(150000, 0)

    Jump('loc_8C07')

    def _loc_8BFE(): pass

    label('loc_8BFE')

    OP_6C(30000, 0)

    def _loc_8C07(): pass

    label('loc_8C07')

    SetChrPos(0x0102, 16480, 0, 76930, 90)
    FadeIn(1000, 0)
    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0403, 5, 0x201D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8C8C',
    )

    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020360686V#1043F（三个女孩子吗……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020360687V#1042F（其它人大概在主校舍吧？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x201D)

    def _loc_8C8C(): pass

    label('loc_8C8C')

    Call(0, 0x004C)
    EventEnd(0x00)
    SetMapFlags(0x02000000)

    Return()

# id: 0x0049 offset: 0x8C98
@scena.Code('func_49_8C98')
def func_49_8C98():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0403, 6, 0x201E)),
            Expr.Return,
        ),
        'loc_8DDE',
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeOut(300, 0, 100)
    OP_57(0x00C8, 0x0014, 0x000C, '#5CLook inside again?')
    OP_CC(0x00, 0x00, 0x000A, 0x000A, 0x00)
    OP_CC(0x01, 0x00, '【是】')
    OP_CC(0x01, 0x00, '【否】')
    OP_CC(0x02, 0x00)
    MenuEnd(0x0000)
    FadeIn(300, 0)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_DA()

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_8D22'),
        (0x00000001, 'loc_8DCC'),
        (-1, 'loc_8DDB'),
    )

    def _loc_8D22(): pass

    label('loc_8D22')

    EventBegin(0x00)

    If(
        (
            (Expr.PushValueByIndex, 0x64),
            (Expr.PushLong, 0x5A),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_8D67',
    )

    Fade(500)
    SetChrPos(0x0102, 16480, 0, 71110, 90)
    OP_6D(16480, 0, 71110, 0)
    OP_6C(150000, 0)
    OP_A3(0x2030)
    OP_0D()

    Jump('loc_8D9B')

    def _loc_8D67(): pass

    label('loc_8D67')

    Fade(500)
    SetChrPos(0x0102, 16480, 0, 71110, 90)
    OP_6D(16480, 0, 71110, 0)
    OP_6C(30000, 0)
    OP_A2(0x2030)
    OP_0D()

    def _loc_8D9B(): pass

    label('loc_8D9B')

    @scena.Lambda('lambda_8DA1')
    def lambda_8DA1():
        OP_6E(241, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_8DA1)

    Sleep(1000)

    FadeOut(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x02000000)
    OP_A2(0x10F4)
    NewScene('ED6_DT21/T2512._SN', 109, 0, 0)
    IdleLoop()

    def _loc_8DCC(): pass

    label('loc_8DCC')

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)

    Jump('loc_8DDB')

    def _loc_8DDB(): pass

    label('loc_8DDB')

    Jump('loc_8E88')

    def _loc_8DDE(): pass

    label('loc_8DDE')

    EventBegin(0x00)

    If(
        (
            (Expr.PushValueByIndex, 0x64),
            (Expr.PushLong, 0x5A),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_8E23',
    )

    Fade(500)
    SetChrPos(0x0102, 16480, 0, 71110, 90)
    OP_6D(16480, 0, 71110, 0)
    OP_6C(150000, 0)
    OP_A3(0x2030)
    OP_0D()

    Jump('loc_8E57')

    def _loc_8E23(): pass

    label('loc_8E23')

    Fade(500)
    SetChrPos(0x0102, 16480, 0, 71110, 90)
    OP_6D(16480, 0, 71110, 0)
    OP_6C(30000, 0)
    OP_A2(0x2030)
    OP_0D()

    def _loc_8E57(): pass

    label('loc_8E57')

    @scena.Lambda('lambda_8E5D')
    def lambda_8E5D():
        OP_6E(241, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_8E5D)

    Sleep(1000)

    FadeOut(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x02000000)
    OP_A2(0x10F4)
    NewScene('ED6_DT21/T2512._SN', 109, 0, 0)
    IdleLoop()
    def _loc_8E88(): pass

    label('loc_8E88')

    TalkEnd(0x00FF)

    Return()

# id: 0x004A offset: 0x8E8C
@scena.Code('func_4A_8E8C')
def func_4A_8E8C():
    EventBegin(0x00)
    OP_6D(16480, 0, 71110, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6E(262, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0406, 0, 0x2030)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8ED6',
    )

    OP_6C(150000, 0)

    Jump('loc_8EDF')

    def _loc_8ED6(): pass

    label('loc_8ED6')

    OP_6C(30000, 0)

    def _loc_8EDF(): pass

    label('loc_8EDF')

    SetChrPos(0x0102, 16480, 0, 71110, 90)
    FadeIn(1000, 0)
    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0403, 6, 0x201E)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8F68',
    )

    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020360688V#1042F（巡逻的士兵两名……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020360689V#1035F（其它的房间应该没有人了。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x201E)

    def _loc_8F68(): pass

    label('loc_8F68')

    Call(0, 0x004C)
    EventEnd(0x00)
    SetMapFlags(0x02000000)

    Return()

# id: 0x004B offset: 0x8F74
@scena.Code('func_4B_8F74')
def func_4B_8F74():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 3, 0x2013)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0403, 7, 0x201F)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_8F81',
    )

    Return()

    def _loc_8F81(): pass

    label('loc_8F81')

    EventBegin(0x01)
    Fade(500)
    OP_6D(16260, 0, 70080, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_8E(0x0102, 16490, 0, 68460, 2000, 0x00)
    OP_8C(0x0102, 135, 400)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020360690V#1042F（……外面有巡逻。\n',
            '  从里面通过比较好。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    Fade(500)
    OP_6D(15560, 0, 69700, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    SetChrPos(0x0102, 15560, 0, 69700, 0)
    OP_0D()
    Sleep(50)

    EventEnd(0x04)
    SetMapFlags(0x02000000)

    Return()

# id: 0x004C offset: 0x908D
@scena.Code('func_4C_908D')
def func_4C_908D():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_9189',
    )

    FadeOut(300, 0, 100)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        100,
        0,
        (
            TXT(0x00, '【◇建筑物内部全部确认、后门的锁也已经打开】\n'),
            TXT(0x01, '【◇建筑物内部没有全部确认，后门的锁也没有打开】\n'),
            TXT(0x02, '【◇不变更】\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_56(0x00)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_9147'),
        (0x00000001, 'loc_9168'),
        (-1, 'loc_9189'),
    )

    def _loc_9147(): pass

    label('loc_9147')

    OP_A2(0x2017)
    OP_A2(0x2014)
    OP_A2(0x2016)
    OP_A2(0x2018)
    OP_A2(0x2019)
    OP_A2(0x201A)
    OP_A2(0x201B)
    OP_A2(0x201C)
    OP_A2(0x201D)
    OP_A2(0x201E)

    Jump('loc_9189')

    def _loc_9168(): pass

    label('loc_9168')

    OP_A3(0x2017)
    OP_A3(0x2014)
    OP_A3(0x2016)
    OP_A3(0x2018)
    OP_A3(0x2019)
    OP_A3(0x201A)
    OP_A3(0x201B)
    OP_A3(0x201C)
    OP_A3(0x201D)
    OP_A3(0x201E)

    Jump('loc_9189')

    def _loc_9189(): pass

    label('loc_9189')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 7, 0x2017)),
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 4, 0x2014)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 6, 0x2016)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0403, 0, 0x2018)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0403, 1, 0x2019)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0403, 2, 0x201A)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0403, 3, 0x201B)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0403, 4, 0x201C)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0403, 5, 0x201D)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0403, 6, 0x201E)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_92EE',
    )

    OP_62(0x0102, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1500)

    OP_63(0x0102)
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020360691V#1035F（这样就算全部调查完毕了吧。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020360692V#1042F（这种程度的敌人……\n',
            '  凭我一个人应该就可以……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020360693V（…………………………………）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020360694V#1043F（不……\n',
            '  现在不是最佳时机。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020360695V（还是赶快回到大家那里吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F1)
    NewScene('ED6_DT21/R2301._SN', 100, 0, 0)
    IdleLoop()

    def _loc_92EE(): pass

    label('loc_92EE')

    Return()

# id: 0x004D offset: 0x92EF
@scena.Code('func_4D_92EF')
def func_4D_92EF():
    EventBegin(0x00)
    OP_D2(0x0026000D, 0x00260012, 0x20)
    SetChrFlags(0x0000, 0x0080)
    SetChrFlags(0x0001, 0x0080)
    SetChrFlags(0x0002, 0x0080)
    SetChrFlags(0x0003, 0x0080)
    SetChrChipByIndex(0x0014, 32)
    SetChrChipByIndex(0x0015, 32)
    SetChrChipByIndex(0x0016, 32)
    SetChrChipByIndex(0x0017, 32)
    SetChrFlags(0x0024, 0x0080)
    SetChrFlags(0x0025, 0x0080)
    SetChrFlags(0x0026, 0x0080)
    SetChrFlags(0x0027, 0x0080)
    SetChrFlags(0x0028, 0x0080)
    SetChrFlags(0x0029, 0x0080)
    SetChrFlags(0x002A, 0x0080)
    SetChrFlags(0x002B, 0x0080)
    SetChrFlags(0x002C, 0x0080)
    CreateThread(0x0014, 0x01, 0x00, 0x0022)
    CreateThread(0x0015, 0x01, 0x00, 0x0023)
    CreateThread(0x0018, 0x01, 0x00, 0x0026)
    CreateThread(0x0019, 0x01, 0x00, 0x0027)
    CreateThread(0x001A, 0x01, 0x00, 0x0028)
    CreateThread(0x001B, 0x01, 0x00, 0x0029)
    SetChrPos(0x0016, 21540, 0, 46950, 180)
    SetChrPos(0x0017, 21540, 0, 45600, 0)
    ClearChrFlags(0x0016, 0x0080)
    ClearChrFlags(0x0017, 0x0080)
    OP_6D(53310, 0, 46050, 0)
    OP_67(0, 8390, -10000, 0)
    OP_6B(3210, 0)
    OP_6C(90000, 0)
    OP_6E(375, 0)

    @scena.Lambda('lambda_93E9')
    def lambda_93E9():
        OP_6D(23270, 0, 46150, 6000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_93E9)

    @scena.Lambda('lambda_9401')
    def lambda_9401():
        OP_67(0, 7570, -10000, 6000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_9401)

    @scena.Lambda('lambda_9419')
    def lambda_9419():
        OP_6B(3220, 6000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_9419)

    @scena.Lambda('lambda_9429')
    def lambda_9429():
        OP_6E(345, 6000)

        ExitThread()

    DispatchAsync(0x0001, 0x0002, lambda_9429)

    FadeIn(1000, 0)
    OP_0D()
    WaitForThreadExit(0x0000, 0x0001)
    Fade(1000)
    OP_6D(22660, 0, 46750, 0)
    OP_67(0, 7180, -10000, 0)
    OP_6B(2990, 0)
    OP_6C(65000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0016,
        (
            '#4230360787V#5P……基尔巴特那家伙的脑子里\n',
            '到底在想些什么啊？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#4230360788V费这么大力气占据了这里，\n',
            '难道就是为了吓唬吓唬这群毛头小子吗？\n',
            '真是无聊的行为啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '#4250360789V#6P确实，想要在王国内制造混乱的话，\n',
            '最好是在都市中下手……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#4250360790V不过在这所学院中可是\n',
            '聚集着很多名门家族的子女呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#4250360791V听传闻说，就连利贝尔王家的公主\n',
            '也都在这间学院中就读呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '#4230360792V#5P王家的公主……\n',
            '难道是科洛蒂娅公主吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '#4250360793V#6P哈哈，那不可能吧。\n',
            '听说她一直在王城中居住着。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#4250360794V只不过，『怪盗绅士』所迷恋的\n',
            '那个女孩就是这里的学生，\n',
            '而且好像确实就是王族的人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#4250360795V基尔巴特大概就是为了确认\n',
            '她的真实身份而攻占这里的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '#4230360796V#5P原来如此……这么一说的话\n',
            '我们辛苦这么久倒也不算是白费力气。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#4230360797V只是那样的话，军队和游击士协会\n',
            '肯定会来全力营救吧，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#4230360798V我们可不能放松警戒。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '#4250360799V#6P哈哈，我们才刚占据这里，\n',
            '他们不可能马上发现的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#4250360800V而且那帮家伙和咱们不同，\n',
            '现在连导力兵器都用不了，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#4250360801V硬拼的话也不用怕他们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '#4230360802V#5P嗯，的确如此……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_22(0x0235, 0x00, 0x3C)
    Sleep(600)

    OP_22(0x0235, 0x00, 0x46)
    OP_20(0x000007D0)
    OP_62(0x0016, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(100)

    OP_62(0x0017, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(600)

    OP_22(0x0235, 0x00, 0x50)
    Sleep(400)

    @scena.Lambda('lambda_98F4')
    def lambda_98F4():
        OP_8C(0x00FE, 270, 600)

        ExitThread()

    DispatchAsync(0x0016, 0x0001, lambda_98F4)

    Sleep(50)

    @scena.Lambda('lambda_9907')
    def lambda_9907():
        OP_8C(0x00FE, 270, 600)

        ExitThread()

    DispatchAsync(0x0017, 0x0001, lambda_9907)

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F2)
    NewScene('ED6_DT21/R2301._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x004E offset: 0x9927
@scena.Code('func_4E_9927')
def func_4E_9927():
    EventBegin(0x00)
    SetChrFlags(0x0000, 0x0080)
    SetChrFlags(0x0001, 0x0080)
    SetChrFlags(0x0002, 0x0080)
    SetChrFlags(0x0003, 0x0080)
    OP_D2(0x0026000D, 0x00260012, 0x20)
    SetChrFlags(0x0000, 0x0080)
    SetChrFlags(0x0001, 0x0080)
    SetChrFlags(0x0002, 0x0080)
    SetChrFlags(0x0003, 0x0080)
    SetChrFlags(0x0024, 0x0080)
    SetChrFlags(0x0025, 0x0080)
    SetChrFlags(0x0026, 0x0080)
    SetChrFlags(0x0027, 0x0080)
    SetChrFlags(0x0028, 0x0080)
    SetChrFlags(0x0029, 0x0080)
    SetChrFlags(0x002A, 0x0080)
    SetChrFlags(0x002B, 0x0080)
    SetChrFlags(0x002C, 0x0080)
    SetChrChipByIndex(0x0014, 32)
    SetChrChipByIndex(0x0015, 32)
    SetChrChipByIndex(0x0016, 32)
    SetChrChipByIndex(0x0017, 32)
    CreateThread(0x0014, 0x01, 0x00, 0x0022)
    CreateThread(0x0015, 0x01, 0x00, 0x0023)
    CreateThread(0x0018, 0x01, 0x00, 0x0026)
    CreateThread(0x0019, 0x01, 0x00, 0x0027)
    CreateThread(0x001A, 0x01, 0x00, 0x0028)
    CreateThread(0x001B, 0x01, 0x00, 0x0029)
    SetChrPos(0x0016, 21540, 0, 46950, 270)
    SetChrPos(0x0017, 21540, 0, 45600, 270)
    ClearChrFlags(0x0016, 0x0080)
    ClearChrFlags(0x0017, 0x0080)
    OP_6F(0x0021, 0)
    OP_72(0x0021, 0x0010)
    OP_6D(22660, 0, 46750, 0)
    OP_67(0, 7180, -10000, 0)
    OP_6B(2990, 0)
    OP_6C(65000, 0)
    OP_6E(262, 0)
    CreateThread(0x0016, 0x02, 0x00, 0x004F)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0016,
        (
            '#4230360803V#5P火、火药式的枪械！？\n',
            '竟然连这种古董货都拿出来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '#4250360804V#2P这样下去的话防线迟早要被他们攻破……\n',
            '快把待命中的同伴们叫来！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMapFlags(0x02000000)
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene('ED6_DT21/T2600._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x004F offset: 0x9B08
@scena.Code('func_4F_9B08')
def func_4F_9B08():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_9B5C',
    )

    OP_22(0x0235, 0x00, 0x50)
    Sleep(1500)

    OP_23(0x0235)
    Sleep(500)

    OP_22(0x0235, 0x00, 0x50)
    Sleep(1900)

    OP_23(0x0235)
    Sleep(700)

    OP_22(0x0235, 0x00, 0x50)
    Sleep(1700)

    OP_23(0x0235)
    Sleep(600)

    OP_22(0x0235, 0x00, 0x50)
    Sleep(2000)

    OP_23(0x0235)
    Sleep(800)

    Jump('func_4F_9B08')

    def _loc_9B5C(): pass

    label('loc_9B5C')

    Return()

# id: 0x0050 offset: 0x9B5D
@scena.Code('func_50_9B5D')
def func_50_9B5D():
    EventBegin(0x00)
    Fade(500)
    SetChrPos(0x0101, 67000, 0, 28000, 270)
    SetChrPos(0x0102, 69060, 0, 28020, 270)
    SetChrPos(0x010A, 68950, 0, 27000, 315)
    SetChrPos(0x010E, 68850, 0, 29110, 225)
    OP_6D(65590, 0, 28000, 0)
    OP_67(0, 7570, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(270000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_70(0x0022, 0x0000003C)
    OP_73(0x0022)
    Sleep(1000)

    OP_A2(0x2020)
    OP_64(0x01, 0x0001)
    EventEnd(0x00)
    SetMapFlags(0x02000000)

    Return()

# id: 0x0051 offset: 0x9C04
@scena.Code('func_51_9C04')
def func_51_9C04():
    EventBegin(0x00)

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000065, 'loc_9C2E'),
        (0x00000066, 'loc_9D00'),
        (0x00000067, 'loc_9DD2'),
        (0x00000069, 'loc_9EA4'),
        (0x0000006A, 'loc_9F76'),
        (0x0000006B, 'loc_A048'),
        (0x0000006C, 'loc_A11A'),
        (0x0000006D, 'loc_A1EC'),
        (-1, 'loc_A2BE'),
    )

    def _loc_9C2E(): pass

    label('loc_9C2E')

    OP_6D(21430, 250, 67190, 0)
    OP_67(0, 7530, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(314000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0014, 35940, -2000, 50640, 0)
    SetChrPos(0x0101, 21590, 250, 66630, 180)
    SetChrPos(0x0102, 22830, 250, 66650, 180)
    SetChrPos(0x010A, 21570, 500, 67710, 180)
    SetChrPos(0x010E, 22630, 500, 67660, 180)
    FadeIn(1000, 0)
    OP_0D()

    NpcTalk(
        0x0014,
        '女孩子的声音',
        (
            '#4030361027V#2P呀～～不要啊～～！',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_A2BE')

    def _loc_9D00(): pass

    label('loc_9D00')

    OP_6D(22360, 250, 25500, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(144000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0014, 40130, 250, 27260, 0)
    SetChrPos(0x0101, 22590, 250, 26500, 0)
    SetChrPos(0x0102, 21540, 250, 26340, 0)
    SetChrPos(0x010A, 22540, 500, 25460, 0)
    SetChrPos(0x010E, 21540, 500, 25390, 0)
    FadeIn(1000, 0)
    OP_0D()

    NpcTalk(
        0x0014,
        '女孩子的声音',
        (
            '#4030361028V#4P呀～～不要啊～～！',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_A2BE')

    def _loc_9DD2(): pass

    label('loc_9DD2')

    OP_6D(41330, 440, 73990, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0014, 48840, 0, 54680, 0)
    SetChrPos(0x0101, 40760, 250, 73540, 270)
    SetChrPos(0x0102, 40820, 250, 74500, 270)
    SetChrPos(0x010A, 41510, 500, 73600, 270)
    SetChrPos(0x010E, 41580, 500, 74500, 270)
    FadeIn(1000, 0)
    OP_0D()

    NpcTalk(
        0x0014,
        '女孩子的声音',
        (
            '#4030361029V#3P呀～～不要啊～～！',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_A2BE')

    def _loc_9EA4(): pass

    label('loc_9EA4')

    OP_6D(49030, 0, 45120, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(134000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0014, 65770, 0, 27850, 0)
    SetChrPos(0x0101, 47790, 250, 46520, 270)
    SetChrPos(0x0102, 47710, 250, 45530, 270)
    SetChrPos(0x010A, 48800, 500, 46520, 270)
    SetChrPos(0x010E, 48670, 500, 45520, 270)
    FadeIn(1000, 0)
    OP_0D()

    NpcTalk(
        0x0014,
        '女孩子的声音',
        (
            '#4030361029V#3P呀～～不要啊～～！',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_A2BE')

    def _loc_9F76(): pass

    label('loc_9F76')

    OP_6D(52890, 0, 62050, 0)
    OP_67(0, 8870, -10000, 0)
    OP_6B(2710, 0)
    OP_6C(99000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0014, 65770, 0, 27850, 0)
    SetChrPos(0x0101, 51310, 0, 62270, 315)
    SetChrPos(0x0102, 52320, 0, 62850, 315)
    SetChrPos(0x010A, 52190, 0, 61540, 315)
    SetChrPos(0x010E, 53310, 0, 61990, 315)
    FadeIn(1000, 0)
    OP_0D()

    NpcTalk(
        0x0014,
        '女孩子的声音',
        (
            '#4030361029V#3P呀～～不要啊～～！',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_A2BE')

    def _loc_A048(): pass

    label('loc_A048')

    OP_6D(52540, 0, 29710, 0)
    OP_67(0, 9140, -10000, 0)
    OP_6B(2650, 0)
    OP_6C(86000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0014, 65770, 0, 27850, 0)
    SetChrPos(0x0101, 51230, 0, 29590, 225)
    SetChrPos(0x0102, 52250, 0, 29160, 225)
    SetChrPos(0x010A, 51900, 0, 30380, 225)
    SetChrPos(0x010E, 52990, 0, 29970, 225)
    FadeIn(1000, 0)
    OP_0D()

    NpcTalk(
        0x0014,
        '女孩子的声音',
        (
            '#4030361029V#3P呀～～不要啊～～！',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_A2BE')

    def _loc_A11A(): pass

    label('loc_A11A')

    OP_6D(47860, 0, 19530, 0)
    OP_67(0, 9580, -10000, 0)
    OP_6B(2580, 0)
    OP_6C(44000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0014, 65770, 0, 27850, 0)
    SetChrPos(0x0101, 46810, 250, 19550, 270)
    SetChrPos(0x0102, 46800, 250, 18440, 270)
    SetChrPos(0x010A, 47820, 500, 19500, 270)
    SetChrPos(0x010E, 47810, 500, 18470, 270)
    FadeIn(1000, 0)
    OP_0D()

    NpcTalk(
        0x0014,
        '女孩子的声音',
        (
            '#4030361033V#6P呀～～不要啊～～！',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_A2BE')

    def _loc_A1EC(): pass

    label('loc_A1EC')

    OP_6D(52820, 0, 26990, 0)
    OP_67(0, 7310, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(105000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0014, 65770, 0, 27850, 0)
    SetChrPos(0x0101, 51270, 0, 27310, 315)
    SetChrPos(0x0102, 52020, 0, 27920, 315)
    SetChrPos(0x010A, 52120, 0, 26600, 315)
    SetChrPos(0x010E, 53070, 0, 27160, 315)
    FadeIn(1000, 0)
    OP_0D()

    NpcTalk(
        0x0014,
        '女孩子的声音',
        (
            '#4030361028V#4P呀～～不要啊～～！',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_A2BE')

    def _loc_A2BE(): pass

    label('loc_A2BE')

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x010A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x010E, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_A335')
    def lambda_A335():
        ChrTurnDirection(0x00FE, 0x0014, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_A335)

    Sleep(50)

    @scena.Lambda('lambda_A348')
    def lambda_A348():
        ChrTurnDirection(0x00FE, 0x0014, 400)

        ExitThread()

    DispatchAsync(0x010A, 0x0001, lambda_A348)

    Sleep(50)

    @scena.Lambda('lambda_A35B')
    def lambda_A35B():
        ChrTurnDirection(0x00FE, 0x0014, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_A35B)

    Sleep(50)

    @scena.Lambda('lambda_A36E')
    def lambda_A36E():
        ChrTurnDirection(0x00FE, 0x0014, 400)

        ExitThread()

    DispatchAsync(0x010E, 0x0001, lambda_A36E)

    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010361035V#1020F刚刚的声音是……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020361036V#1042F那个方向……\n',
            '是旧校舍那边！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010E,
        (
            '#0330361037V#842F手册上所差的最后１人……\n',
            '就是她吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120361038V#815F赶快追过去！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x202E)
    OP_28(0x00C0, 0x01, 0x4000)
    EventEnd(0x00)
    SetMapFlags(0x02000000)

    Return()

# id: 0x0052 offset: 0xA448
@scena.Code('func_52_A448')
def func_52_A448():
    EventBegin(0x00)
    OP_20(0x00000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_A4C1',
    )

    Call(0, 0x0053)
    Call(0, 0x0054)
    OP_A3(0x2031)
    OP_A3(0x2032)
    OP_A3(0x2033)
    OP_A3(0x2034)

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_A480',
    )

    OP_A2(0x2031)

    def _loc_A480(): pass

    label('loc_A480')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_A490',
    )

    OP_A2(0x2032)

    def _loc_A490(): pass

    label('loc_A490')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_A4A0',
    )

    OP_A2(0x2033)

    def _loc_A4A0(): pass

    label('loc_A4A0')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_A4B0',
    )

    OP_A2(0x2034)

    def _loc_A4B0(): pass

    label('loc_A4B0')

    FormationReset()
    FormationAddMember(ChrTable['艾丝蒂尔'], 0xF6, 0xFF)
    FormationAddMember(ChrTable['约修亚'], 0xF7, 0xFF)
    FormationAddMember(ChrTable['亚妮拉丝'], 0xF8, 0xFF)
    FormationAddMember(ChrTable['克鲁茨'], 0xF9, 0xFF)

    def _loc_A4C1(): pass

    label('loc_A4C1')

    FormationAddMember(ChrTable['雪拉扎德'], 0xFF, 0xFF)
    FormationAddMember(ChrTable['阿加特'], 0xFF, 0xFF)
    FormationAddMember(ChrTable['金'], 0xFF, 0xFF)
    FormationAddMember(ChrTable['提妲'], 0xFF, 0xFF)
    OP_D2(0x00260049, 0x0026004E, 0x1D)
    SetChrChipByIndex(0x0101, 29)
    SetChrSubChip(0x0101, 3)
    SetChrPos(0x0101, 20370, 0, 45200, 270)
    SetChrPos(0x0102, 20600, 0, 46260, 270)
    SetChrPos(0x0107, 21330, 0, 45740, 270)
    SetChrPos(0x0103, 21830, 0, 46650, 270)
    SetChrPos(0x0106, 21700, 0, 44370, 270)
    SetChrPos(0x0108, 22800, 0, 45100, 270)
    SetChrPos(0x010A, 18520, 0, 45400, 90)
    SetChrPos(0x001F, 17170, 0, 46730, 90)
    SetChrPos(0x001E, 17290, 0, 45450, 90)
    SetChrPos(0x010E, 18420, 0, 46630, 90)
    ClearChrFlags(0x001C, 0x0080)
    ClearChrFlags(0x001D, 0x0080)
    ClearChrFlags(0x001E, 0x0080)
    ClearChrFlags(0x001F, 0x0080)
    OP_6D(12000, 0, 46000, 0)
    OP_67(0, 7050, -10000, 0)
    OP_6B(1890, 0)
    OP_6C(90000, 0)
    OP_6E(469, 0)
    OP_1D(0x0E)

    @scena.Lambda('lambda_A5E8')
    def lambda_A5E8():
        OP_6D(21530, 0, 46000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_A5E8)

    @scena.Lambda('lambda_A600')
    def lambda_A600():
        OP_67(0, 8310, -10000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_A600)

    FadeIn(1000, 0)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0000)
    Fade(500)
    OP_6D(18910, 0, 46630, 0)
    OP_67(0, 6340, -10000, 0)
    OP_6B(2140, 0)
    OP_6C(315000, 0)
    OP_6E(397, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010361161V#1012F克鲁茨前辈、亚妮拉丝。\n',
            '还有卡露娜前辈和库拉兹前辈。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010361162V#1006F这次真是多谢\n',
            '你们的帮助了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120361163V#811F#5P啊哈哈哈……\n',
            '干嘛要说这么见外的话啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010E,
        (
            '#0330361164V#841F#5P是啊，同样身为游击士，\n',
            '这也是我们的义务。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001E,
        (
            '#0320361165V#835F#5P呵呵，在湖畔那里欠你们的人情\n',
            '总算是稍微还上了一点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001F,
        (
            '#0310361166V#821F#5P大家以后要是遇到什么困难的话，\n',
            '我们随时都可以帮忙的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030361167V#021F呵呵，那就期待下次见面吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020361168V#1040F你们接下来\n',
            '有什么打算呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010E,
        (
            '#0330361169V#840F#5P嗯，我们准备穿越古罗尼山道\n',
            '到柏斯那边去。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330361170V为了防止类似这次的事情再发生，\n',
            '还要到各地进行一次巡视。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080361171V#070F是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070361172V#560F#6P那个那个……\n',
            '那你们可要一路小心了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001F,
        (
            '#0310361173V#825F#5P哈哈，你们也是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001E,
        (
            '#0320361174V#831F#5P这种状况结束之前\n',
            '我们一刻都不能松懈。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050361175V#051F#6P嗯，说的没错，\n',
            '我们彼此加油吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x010A, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTalk(
        0x010A,
        (
            '#0120361176V#814F#5P对了……\n',
            '喂，艾丝蒂尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010361177V#1011F嗯？怎么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120361178V#816F#5P这次和你并肩作战，\n',
            '有些新的感觉……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120361179V从艾丝蒂尔的动作中\n',
            '已经感觉不到迷惑和迟疑了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120361180V#811F实在是成长了不少，\n',
            '真让我佩服啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010361181V#1016F讨、讨厌啦～\n',
            '就算夸奖我，也没有奖励可以拿哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010361182V#1008F而且亚妮拉丝你也\n',
            '进步了不少啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120361183V#1314F#5P这就是在不断的实战中得到的财富吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120361184V#817F不过我能感觉得到，\n',
            '艾丝蒂尔不只是武术进步了，\n',
            '连意志也比以前坚强了很多。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120361185V大概是在寻找\n',
            '约修亚的旅途中\n',
            '悟出了自己的『道』吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120361186V#816F真的……很了不起啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010361187V#1017F亚妮拉丝……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120361188V#819F#5P嘿嘿嘿，身为竞争对手，\n',
            '我可是不能输给你的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120361189V#1310F以后有机会的话\n',
            '再一起作战吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120361190V#811F下一次就该轮到我\n',
            '让艾丝蒂尔大吃一惊了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010361191V#1018F啊哈哈……嗯！\n',
            '那我就期待着那一天的到来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_B7(0x09)
    OP_B7(0x0D)
    OP_20(0x000007D0)
    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0406, 1, 0x2031)),
            (Expr.TestScenaFlags, ScenaFlag(0x0406, 3, 0x2033)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_AE6A',
    )

    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '之后，阿加特和提妲\n',
            '先一步返回了卢安支部，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '从王都飞来的基库\n',
            '也回到了科洛丝的身边。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔一行人在和学院中的大家\n',
            '道别后，也重新踏上了新的旅途。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_B212')

    def _loc_AE6A(): pass

    label('loc_AE6A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0406, 1, 0x2031)),
            (Expr.TestScenaFlags, ScenaFlag(0x0406, 2, 0x2032)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_AF2C',
    )

    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '之后，雪拉扎德和阿加特\n',
            '先一步返回了卢安支部，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '从王都飞来的基库\n',
            '也回到了科洛丝的身边。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔一行人在和学院中的大家\n',
            '道别后，也重新踏上了新的旅途。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_B212')

    def _loc_AF2C(): pass

    label('loc_AF2C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0406, 1, 0x2031)),
            (Expr.TestScenaFlags, ScenaFlag(0x0406, 4, 0x2034)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_AFE8',
    )

    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '之后，阿加特和金\n',
            '先一步返回了卢安支部，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '从王都飞来的基库\n',
            '也回到了科洛丝的身边。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔一行人在和学院中的大家\n',
            '道别后，也重新踏上了新的旅途。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_B212')

    def _loc_AFE8(): pass

    label('loc_AFE8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0406, 3, 0x2033)),
            (Expr.TestScenaFlags, ScenaFlag(0x0406, 2, 0x2032)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_B0A8',
    )

    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '之后，雪拉扎德和提妲\n',
            '先一步返回了卢安支部，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '从王都飞来的基库\n',
            '也回到了科洛丝的身边。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔一行人在和学院中的大家\n',
            '道别后，也重新踏上了新的旅途。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_B212')

    def _loc_B0A8(): pass

    label('loc_B0A8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0406, 3, 0x2033)),
            (Expr.TestScenaFlags, ScenaFlag(0x0406, 4, 0x2034)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_B162',
    )

    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '之后，提妲和金\n',
            '先一步返回了卢安支部，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '从王都飞来的基库\n',
            '也回到了科洛丝的身边。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔一行人在和学院中的大家\n',
            '道别后，也重新踏上了新的旅途。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_B212')

    def _loc_B162(): pass

    label('loc_B162')

    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '之后，雪拉扎德和金\n',
            '先一步返回了卢安支部，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '从王都飞来的基库\n',
            '也回到了科洛丝的身边。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔一行人在和学院中的大家\n',
            '道别后，也重新踏上了新的旅途。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_B212(): pass

    label('loc_B212')

    Sleep(500)

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    OP_22(0x0017, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【王立学院受袭事件】',
            (TxtCtl.SetColor, 0x0),
            '完成了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_28(0x00C0, 0x04, 0x10)
    OP_28(0x00C0, 0x01, 0x8000)
    OP_28(0x00C1, 0x03, 0x02)
    OP_28(0x00C1, 0x03, 0x08)
    OP_28(0x00C3, 0x04, 0x02)
    OP_28(0x00C3, 0x04, 0x08)
    OP_28(0x00C3, 0x04, 0x10)
    OP_28(0x00C3, 0x01, 0x0100)
    OP_28(0x00C3, 0x01, 0x0200)
    OP_28(0x00C3, 0x01, 0x0400)
    OP_28(0x00C3, 0x01, 0x0800)
    OP_28(0x00C3, 0x01, 0x1000)
    OP_28(0x00C3, 0x01, 0x2000)
    OP_28(0x00C3, 0x01, 0x4000)
    OP_28(0x00C3, 0x01, 0x8000)
    FormationReset()
    FormationAddMember(ChrTable['艾丝蒂尔'], 0xF6, 0xFF)
    FormationAddMember(ChrTable['约修亚'], 0xF7, 0xFF)

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0406, 1, 0x2031)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B2D7',
    )

    FormationAddMember(ChrTable['阿加特'], 0xF8, 0xFF)

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_B2D7(): pass

    label('loc_B2D7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0406, 2, 0x2032)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B301',
    )

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B2FD',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xF8, 0xFF)

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_B301')

    def _loc_B2FD(): pass

    label('loc_B2FD')

    FormationAddMember(ChrTable['雪拉扎德'], 0xF9, 0xFF)

    def _loc_B301(): pass

    label('loc_B301')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0406, 3, 0x2033)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B32B',
    )

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B327',
    )

    FormationAddMember(ChrTable['提妲'], 0xF8, 0xFF)

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_B32B')

    def _loc_B327(): pass

    label('loc_B327')

    FormationAddMember(ChrTable['提妲'], 0xF9, 0xFF)

    def _loc_B32B(): pass

    label('loc_B32B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0406, 4, 0x2034)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B355',
    )

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B351',
    )

    FormationAddMember(ChrTable['金'], 0xF8, 0xFF)

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_B355')

    def _loc_B351(): pass

    label('loc_B351')

    FormationAddMember(ChrTable['金'], 0xF9, 0xFF)

    def _loc_B355(): pass

    label('loc_B355')

    OP_6D(21410, 0, 45890, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0000, 21410, 0, 45890, 270)
    SetChrPos(0x0001, 21410, 0, 45890, 270)
    SetChrPos(0x0002, 21410, 0, 45890, 270)
    SetChrPos(0x0003, 21410, 0, 45890, 270)
    OP_69(0x0000, 0x00000000)
    SetChrChipByIndex(0x0101, 65535)
    SetChrFlags(0x001E, 0x0080)
    SetChrFlags(0x001F, 0x0080)
    OP_A2(0x202F)

    OP_CE(
        0x00,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrPos(0x0010, 45800, 0, 46000, 0)
    CreateThread(0x0010, 0x00, 0x00, 0x0004)
    SetChrPos(0x000C, 36500, 0, 70920, 225)
    CreateThread(0x000C, 0x00, 0x06, 0x0002)
    SetChrPos(0x000D, 35500, 0, 69860, 45)
    CreateThread(0x000D, 0x00, 0x06, 0x0002)
    ClearChrFlags(0x0010, 0x0080)
    ClearChrFlags(0x0021, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    SetChrFlags(0x000E, 0x0080)
    SetChrFlags(0x000F, 0x0080)
    SetChrFlags(0x0011, 0x0080)
    Sleep(100)

    OP_1D(0x1A)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x1A),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x0053 offset: 0xB47F
@scena.Code('func_53_B47F')
def func_53_B47F():
    FadeOut(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        100,
        0,
        (
            TXT(0x00, '【◇选择雪拉扎德为队友】\n'),
            TXT(0x01, '【◇选择阿加特为队友】\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_56(0x00)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_B4F9'),
        (0x00000001, 'loc_B4FF'),
        (-1, 'loc_B505'),
    )

    def _loc_B4F9(): pass

    label('loc_B4F9')

    OP_A2(0x1200)

    Jump('loc_B505')

    def _loc_B4FF(): pass

    label('loc_B4FF')

    OP_A2(0x1201)

    Jump('loc_B505')

    def _loc_B505(): pass

    label('loc_B505')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_B513',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    Jump('loc_B517')

    def _loc_B513(): pass

    label('loc_B513')

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    def _loc_B517(): pass

    label('loc_B517')

    Return()

# id: 0x0054 offset: 0xB518
@scena.Code('func_54_B518')
def func_54_B518():
    ClearMapFlags(0x00000001)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)

    FadeIn(0, 0)

    OP_C9(
        0x00,
        (
            0x0000,
            0x0001,
            0x00FF,
            0x00FF,
        ),
        (
            0x0005,
            0x0002,
            0x0006,
            0x0007,
            0xFFFF,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0x00000000)
    Sleep(1000)

    Return()

# id: 0x0055 offset: 0xB571
@scena.Code('func_55_B571')
def func_55_B571():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0403, 7, 0x201F)),
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_B70F',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B5DF',
    )

    ChrTalk(
        0x0101,
        (
            '#0010360818V#1002F（现在是吸引敌人注意力的好时机。\n',
            '　必须要尽快解救人质。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B6EC')

    def _loc_B5DF(): pass

    label('loc_B5DF')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B63B',
    )

    ChrTalk(
        0x0102,
        (
            '#0020360819V#1042F（现在敌人的注意力已经转移了。\n',
            '　赶快去解救人质吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B6EC')

    def _loc_B63B(): pass

    label('loc_B63B')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B696',
    )

    ChrTalk(
        0x010A,
        (
            '#0120360820V#816F（看来已经成功把敌人引开了。\n',
            '　我们快去解救人质吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B6EC')

    def _loc_B696(): pass

    label('loc_B696')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B6EC',
    )

    ChrTalk(
        0x010E,
        (
            '#0330360821V#842F（现在是吸引敌人的绝好时机。\n',
            '　赶快去解救人质吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B6EC(): pass

    label('loc_B6EC')

    OP_90(0x0000, 1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)
    SetMapFlags(0x02000000)

    Jump('loc_B7F2')

    def _loc_B70F(): pass

    label('loc_B70F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0244, 1, 0x1221)),
            (Expr.TestScenaFlags, ScenaFlag(0x0244, 2, 0x1222)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_B77C',
    )

    EventBegin(0x01)
    ChrTurnDirection(0x0105, 0x0101, 400)

    ChrTalk(
        0x0105,
        (
            '#0060211262V#040F天马上就要黑了啊。\n',
            '先回学生会室吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_90(0x0000, 1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Jump('loc_B7F2')

    def _loc_B77C(): pass

    label('loc_B77C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 6, 0x121E)),
            (Expr.TestScenaFlags, ScenaFlag(0x0244, 1, 0x1221)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_B7F2',
    )

    EventBegin(0x01)
    ChrTurnDirection(0x0105, 0x0101, 400)

    ChrTalk(
        0x0105,
        (
            '#0060211263V#040F学生们应该在教室和宿舍中。\n',
            '继续在学院内探听吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_90(0x0000, 1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_B7F2(): pass

    label('loc_B7F2')

    Return()

# id: 0x0056 offset: 0xB7F3
@scena.Code('func_56_B7F3')
def func_56_B7F3():
    SetPlaceName(0x005F)

    Return()

# id: 0x0057 offset: 0xB7F7
@scena.Code('func_57_B7F7')
def func_57_B7F7():
    SetPlaceName(0x005C)

    Return()

# id: 0x0058 offset: 0xB7FB
@scena.Code('func_58_B7FB')
def func_58_B7FB():
    SetPlaceName(0x005D)

    Return()

# id: 0x0059 offset: 0xB7FF
@scena.Code('func_59_B7FF')
def func_59_B7FF():
    SetPlaceName(0x006C)

    Return()

# id: 0x005A offset: 0xB803
@scena.Code('func_5A_B803')
def func_5A_B803():
    SetPlaceName(0x006D)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
