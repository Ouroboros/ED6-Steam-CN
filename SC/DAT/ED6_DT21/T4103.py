import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T4103_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4103   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '诺雅尔'),
    TXT(0x02, '维基奥'),
    TXT(0x03, '巴鲁托'),
    TXT(0x04, '王国军士兵'),
    TXT(0x05, '王国军士兵'),
    TXT(0x06, '巡逻兵'),
    TXT(0x07, '吉赛尔'),
    TXT(0x08, '杜南公爵'),
    TXT(0x09, '凯诺娜'),
    TXT(0x0A, '特务兵'),
    TXT(0x0B, '特务兵'),
    TXT(0x0C, '士兵'),
    TXT(0x0D, '士兵'),
    TXT(0x0E, '士兵'),
    TXT(0x0F, '士兵'),
    TXT(0x10, '士兵'),
    TXT(0x11, '士兵'),
    TXT(0x12, '士兵'),
    TXT(0x13, '士兵'),
    TXT(0x14, '士兵'),
    TXT(0x15, '士兵'),
    TXT(0x16, '士兵'),
    TXT(0x17, '士兵'),
    TXT(0x18, '士兵'),
    TXT(0x19, '士兵'),
    TXT(0x1A, '士兵'),
    TXT(0x1B, '士兵'),
    TXT(0x1C, '王都格兰赛尔·西街区'),
    TXT(0x1D, '格兰赛尔城'),
    TXT(0x1E, '王都格兰赛尔·东街区'),
    TXT(0x1F, '王都格兰赛尔·南街区'),
    TXT(0x20, ''),
    TXT(0x21, ''),
    TXT(0x22, ''),
    TXT(0x23, ''),
    TXT(0x24, ''),
    TXT(0x25, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4103.x'
    header.mapIndex       = 1
    header.bgm            = 14
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x33B6
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
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
        ('ED6_DT07/CH02140._CH', 'ED6_DT07/CH02140P._CP'),
        ('ED6_DT27/CH03120._CH', 'ED6_DT27/CH03120P._CP'),
        ('ED6_DT07/CH01610._CH', 'ED6_DT07/CH01610P._CP'),
        ('ED6_DT06/CH20043._CH', 'ED6_DT06/CH20043P._CP'),
        ('ED6_DT07/CH01130._CH', 'ED6_DT07/CH01130P._CP'),
        ('ED6_DT07/CH01290._CH', 'ED6_DT07/CH01290P._CP'),
        ('ED6_DT07/CH01200._CH', 'ED6_DT07/CH01200P._CP'),
        ('ED6_DT27/CH04610._CH', 'ED6_DT27/CH04610P._CP'),
        ('ED6_DT27/CH04611._CH', 'ED6_DT27/CH04611P._CP'),
        ('ED6_DT27/CH04620._CH', 'ED6_DT27/CH04620P._CP'),
        ('ED6_DT27/CH04621._CH', 'ED6_DT27/CH04621P._CP'),
        ('ED6_DT29/CH12570._CH', 'ED6_DT29/CH12570P._CP'),
        ('ED6_DT29/CH12571._CH', 'ED6_DT29/CH12571P._CP'),
        ('ED6_DT29/CH12350._CH', 'ED6_DT29/CH12350P._CP'),
        ('ED6_DT29/CH12351._CH', 'ED6_DT29/CH12351P._CP'),
        ('ED6_DT29/CH12320._CH', 'ED6_DT29/CH12320P._CP'),
        ('ED6_DT29/CH12321._CH', 'ED6_DT29/CH12321P._CP'),
        ('ED6_DT07/CH01230._CH', 'ED6_DT07/CH01230P._CP'),
    ]

# id: 0x10002 offset: 0x142
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0005,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            x                   = -2950,
            z                   = 0,
            y                   = 63820,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0006,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            x                   = -7440,
            z                   = 0,
            y                   = 49400,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0007,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            x                   = 7690,
            z                   = 0,
            y                   = 41560,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 18,
            chipIndex           = 18,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0008,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
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
            dword_10            = 3,
            chipIndex           = 3,
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
            dword_10            = 3,
            chipIndex           = 3,
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
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x01A0,
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
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x01A0,
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
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x01A0,
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
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x01A0,
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
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x01A0,
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
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x01A0,
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
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x01A0,
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
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x01A0,
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
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x01A0,
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
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x01A0,
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
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x01A0,
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
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x01A0,
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
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x01A0,
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
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x01A0,
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
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x01A0,
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
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x01A0,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -40080,
            z                   = 0,
            y                   = 17660,
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
            x                   = 100,
            z                   = 0,
            y                   = 104130,
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
            x                   = 40430,
            z                   = 0,
            y                   = 64060,
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
            x                   = 20,
            z                   = 0,
            y                   = -3500,
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

# id: 0x10003 offset: 0x522
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = 170,
            z           = 0,
            y           = 39490,
            word_0C     = 0x00B4,
            word_0E     = 0x0010,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x054A,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 16030,
            z           = 0,
            y           = 63610,
            word_0C     = 0x00B4,
            word_0E     = 0x000C,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0548,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -40070,
            z           = 0,
            y           = 49910,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0547,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -14730,
            z           = 0,
            y           = 50220,
            word_0C     = 0x00B4,
            word_0E     = 0x000E,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0549,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 9080,
            z           = 250,
            y           = 58390,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0546,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x5AE
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 18520,
            y           = 0,
            z           = 44050,
            range       = 1500,
            dword_10    = 0x000009C4,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000001A,
        ),
    )

# id: 0x10005 offset: 0x5CE
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 19260,
            triggerZ            = 750,
            triggerY            = 44000,
            triggerRange        = 800,
            actorX              = 19260,
            actorZ              = 1750,
            actorY              = 44000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0015,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -23040,
            triggerZ            = 500,
            triggerY            = 63200,
            triggerRange        = 800,
            actorX              = -23040,
            actorZ              = 1500,
            actorY              = 63200,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0015,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -22160,
            triggerZ            = 500,
            triggerY            = 29050,
            triggerRange        = 800,
            actorX              = -22160,
            actorZ              = 1500,
            actorY              = 29050,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0015,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x63A
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 2, 0x203A)),
            Expr.Return,
        ),
        'loc_645',
    )

    Call(0, 0x0014)

    def _loc_645(): pass

    label('loc_645')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 3, 0x203B)),
            Expr.Return,
        ),
        'loc_663',
    )

    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000E, 0x0080)

    Jump('loc_6C3')

    def _loc_663(): pass

    label('loc_663')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_67C',
    )

    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    SetChrFlags(0x000E, 0x0080)

    Jump('loc_6C3')

    def _loc_67C(): pass

    label('loc_67C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_690',
    )

    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)

    Jump('loc_6C3')

    def _loc_690(): pass

    label('loc_690')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_6A4',
    )

    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)

    Jump('loc_6C3')

    def _loc_6A4(): pass

    label('loc_6A4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_6B2',
    )

    Jump('loc_6C3')

    def _loc_6B2(): pass

    label('loc_6B2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_6BC',
    )

    Jump('loc_6C3')

    def _loc_6BC(): pass

    label('loc_6BC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_6C3',
    )

    def _loc_6C3(): pass

    label('loc_6C3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_6D9',
    )

    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 0x0012)

    Jump('loc_6EA')

    def _loc_6D9(): pass

    label('loc_6D9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 3, 0x1003)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6EA',
    )

    SetMapFlags(0x10000000)
    Event(0, 0x000F)

    def _loc_6EA(): pass

    label('loc_6EA')

    Return()

# id: 0x0001 offset: 0x6EB
@scena.Code('Init')
def Init():
    OP_16(0x02, 0x00000FA0, 0xFFFDE4F0, 0xFFFECF50, 0x0023005E)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 2, 0x1002)),
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 4, 0x1004)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_712',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x1A),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_712(): pass

    label('loc_712')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 5, 0x1625)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 6, 0x1626)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 4, 0x162C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_732',
    )

    OP_B1('t4103_y')

    Jump('loc_753')

    def _loc_732(): pass

    label('loc_732')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C6, 6, 0x1636)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 0, 0x1638)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_74A',
    )

    OP_B1('t4103_y')

    Jump('loc_753')

    def _loc_74A(): pass

    label('loc_74A')

    OP_B1('t4103_n')

    def _loc_753(): pass

    label('loc_753')

    ExecExpressionWithValue(
        0x0027,
        0x24,
        (
            (Expr.PushLong, 0xE7),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 2, 0x203A)),
            Expr.Return,
        ),
        'loc_79C',
    )

    OP_72(0x0002, 0x0010)
    OP_72(0x0003, 0x0010)
    OP_72(0x0004, 0x0010)
    OP_1B(0x04, 0x00, 0x0017)
    OP_1B(0x05, 0x00, 0x0016)
    OP_77(0xFF, 0xBD, 0xA7, 0x00, 0x00000000)
    Call(0, 0x0013)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x2E),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetMapFlags(0x02000000)

    Jump('loc_7AA')

    def _loc_79C(): pass

    label('loc_79C')

    OP_64(0x00, 0x0001)
    OP_64(0x01, 0x0001)
    OP_64(0x02, 0x0001)
    OP_B5(0x00)

    def _loc_7AA(): pass

    label('loc_7AA')

    Return()

# id: 0x0002 offset: 0x7AB
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_7C0',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('ReInit')

    def _loc_7C0(): pass

    label('loc_7C0')

    Return()

# id: 0x0003 offset: 0x7C1
@scena.Code('func_03_7C1')
def func_03_7C1():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_806',
    )

    SetChrPos(0x00FE, 31870, 0, 62980, 270)
    OP_8E(0x00FE, 3180, 0, 62980, 2000, 0x00)
    OP_8E(0x00FE, 3180, 0, 16590, 2000, 0x00)

    Jump('func_03_7C1')

    def _loc_806(): pass

    label('loc_806')

    Return()

# id: 0x0004 offset: 0x807
@scena.Code('func_04_807')
def func_04_807():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_A17',
    )

    SetChrPos(0x00FE, -40860, 0, 28340, 0)
    OP_8E(0x00FE, -40860, 0, 47840, 9000, 0x00)
    OP_8E(0x00FE, -40370, 0, 50210, 9000, 0x00)
    OP_8E(0x00FE, -23750, 0, 50680, 9000, 0x00)
    OP_8C(0x00FE, 0, 800)
    Sleep(300)

    OP_8E(0x00FE, -23750, 250, 59870, 9000, 0x00)
    OP_8E(0x00FE, -24760, 250, 61940, 9000, 0x00)
    OP_8C(0x00FE, 0, 800)
    Sleep(400)

    OP_8E(0x00FE, -23750, 250, 59870, 9000, 0x00)
    OP_8E(0x00FE, -23750, 0, 50680, 9000, 0x00)
    OP_8E(0x00FE, -6540, 0, 50680, 9000, 0x00)
    OP_62(0x0009, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    OP_8E(0x00FE, -4900, 0, 52950, 9000, 0x00)
    OP_8E(0x00FE, -4900, 0, 62070, 9000, 0x00)
    OP_8E(0x00FE, -3730, 0, 64900, 9000, 0x00)
    OP_8E(0x00FE, 39820, 0, 64900, 9000, 0x00)
    Sleep(2000)

    SetChrPos(0x00FE, 39650, 0, 62210, 90)
    OP_8E(0x00FE, 26530, 0, 62210, 9000, 0x00)
    OP_8E(0x00FE, 22200, 250, 58890, 9000, 0x00)
    OP_8E(0x00FE, 10910, 250, 58890, 9000, 0x00)
    OP_8E(0x00FE, 8840, 250, 56320, 9000, 0x00)
    OP_8E(0x00FE, 8840, 250, 49200, 9000, 0x00)
    OP_8E(0x00FE, 11240, 250, 46800, 9000, 0x00)
    OP_8E(0x00FE, 16430, 250, 46800, 9000, 0x00)
    Sleep(400)

    OP_8E(0x00FE, 7920, 250, 36370, 9000, 0x00)
    OP_8E(0x00FE, 7920, 250, 7940, 9000, 0x00)
    Sleep(2000)

    Jump('func_04_807')

    def _loc_A17(): pass

    label('loc_A17')

    Return()

# id: 0x0005 offset: 0xA18
@scena.Code('func_05_A18')
def func_05_A18():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_A71',
    )

    SetChrPos(0x00FE, -4340, 0, 16160, 0)
    OP_8E(0x00FE, -4340, 0, 48500, 2500, 0x00)
    OP_8E(0x00FE, -38810, 0, 48500, 2500, 0x00)
    OP_8E(0x00FE, -38810, 0, 27480, 2500, 0x00)

    Jump('func_05_A18')

    def _loc_A71(): pass

    label('loc_A71')

    Return()

# id: 0x0006 offset: 0xA72
@scena.Code('func_06_A72')
def func_06_A72():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_B08',
    )

    OP_8E(0x00FE, -2950, 0, 49920, 2500, 0x00)
    OP_8C(0x00FE, 270, 400)
    Sleep(2000)

    OP_8E(0x00FE, -2950, 0, 21800, 2500, 0x00)
    Sleep(2000)

    OP_8C(0x00FE, 270, 400)
    Sleep(2000)

    OP_8E(0x00FE, -2950, 0, 49920, 2500, 0x00)
    OP_8C(0x00FE, 270, 400)
    Sleep(2000)

    OP_8E(0x00FE, -2950, 0, 63820, 2500, 0x00)
    Sleep(2000)

    OP_8C(0x00FE, 90, 400)
    Sleep(2000)

    Jump('func_06_A72')

    def _loc_B08(): pass

    label('loc_B08')

    Return()

# id: 0x0007 offset: 0xB09
@scena.Code('func_07_B09')
def func_07_B09():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_C0F',
    )

    OP_8E(0x00FE, -22900, 0, 49400, 2500, 0x00)
    OP_8C(0x00FE, 90, 400)
    Sleep(2000)

    OP_8E(0x00FE, -22900, 0, 49400, 2500, 0x00)
    OP_8E(0x00FE, -39450, 0, 48100, 2500, 0x00)
    OP_8E(0x00FE, -39750, 0, 46660, 2500, 0x00)
    OP_8E(0x00FE, -39750, 0, 38290, 2500, 0x00)
    Sleep(2000)

    OP_8E(0x00FE, -39750, 0, 46660, 2500, 0x00)
    OP_8E(0x00FE, -39060, 0, 49640, 2500, 0x00)
    OP_8E(0x00FE, -22900, 0, 49400, 2500, 0x00)
    OP_8C(0x00FE, 90, 400)
    Sleep(2000)

    OP_8E(0x00FE, -7440, 0, 49400, 2500, 0x00)
    Sleep(2000)

    OP_8C(0x00FE, 0, 400)
    Sleep(2000)

    OP_8C(0x00FE, 180, 400)
    Sleep(2000)

    OP_8C(0x00FE, 90, 400)
    Sleep(2000)

    Jump('func_07_B09')

    def _loc_C0F(): pass

    label('loc_C0F')

    Return()

# id: 0x0008 offset: 0xC10
@scena.Code('func_08_C10')
def func_08_C10():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_C33',
    )

    OP_8D(0x00FE, 8130, 41700, 5710, 43100, 2000)

    Jump('func_08_C10')

    def _loc_C33(): pass

    label('loc_C33')

    Return()

# id: 0x0009 offset: 0xC34
@scena.Code('func_09_C34')
def func_09_C34():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_C9F',
    )

    ChrTalk(
        0x00FE,
        (
            '大家都认为女王陛下\n',
            '会想办法的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '导力停止的原因\n',
            '还不明吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我非常非常不安……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FE9')

    def _loc_C9F(): pass

    label('loc_C9F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_D14',
    )

    ChrTalk(
        0x00FE,
        (
            '西街区的事你们听说了吗？\n',
            '真是了不得。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过情报部的余党\n',
            '也因此不复存在了，\n',
            '生活得能稍微安心点了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FE9')

    def _loc_D14(): pass

    label('loc_D14')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_D8E',
    )

    ChrTalk(
        0x00FE,
        (
            '我和以前在附近看到的\n',
            '旅行者的孩子擦肩而过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然那孩子平时\n',
            '都和父母在一起。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不知道要不要紧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FE9')

    def _loc_D8E(): pass

    label('loc_D8E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_DEA',
    )

    ChrTalk(
        0x00FE,
        (
            '哎呀，讨厌。\n',
            '已经这么晚了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在百货商店关门之前\n',
            '要买好晚饭的原料。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FE9')

    def _loc_DEA(): pass

    label('loc_DEA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_E9A',
    )

    ChrTalk(
        0x00FE,
        (
            '可能是签字仪式近了的缘故……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最近，帝国和共和国的大使馆的人\n',
            '好像频繁出入着到城堡。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '互不侵犯条约虽然像梦一样，不过现在\n',
            '我开始感受到它的真实存在感了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FE9')

    def _loc_E9A(): pass

    label('loc_E9A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_FE9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_F6A',
    )

    ChrTalk(
        0x00FE,
        (
            '向普通人开放的\n',
            '城堡游览项目因政变被中止,但是现在恢复了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我自然要推荐空中庭园。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '从瓦雷利亚湖吹来的清爽的风\n',
            '和庭园的草木的香味儿真的很舒服。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1003F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    Jump('loc_FE9')

    def _loc_F6A(): pass

    label('loc_F6A')

    ChrTalk(
        0x00FE,
        (
            '向普通人开放的\n',
            '城堡游览项目因政变被中止,但是现在恢复了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '从瓦雷利亚湖吹来的清爽的风\n',
            '和庭园的草木的香味儿真的很舒服。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_FE9(): pass

    label('loc_FE9')

    TalkEnd(0x00FE)

    Return()

# id: 0x000A offset: 0xFED
@scena.Code('func_0A_FED')
def func_0A_FED():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1052',
    )

    ChrTalk(
        0x00FE,
        (
            '在港口能看见那个\n',
            '形状古怪的物体。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '从王城的女王宫应该\n',
            '能看清那个方向的东西……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11FB')

    def _loc_1052(): pass

    label('loc_1052')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_10DA',
    )

    ChrTalk(
        0x00FE,
        (
            '港湾区出现了巨大的\n',
            '人形兵器吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '传闻说拉赛尔博士\n',
            '制造的新兵器失控了，\n',
            '真的假的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没有官方消息，\n',
            '所以传闻很多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11FB')

    def _loc_10DA(): pass

    label('loc_10DA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_112A',
    )

    ChrTalk(
        0x00FE,
        (
            '说起来，我刚才\n',
            '在飞船坪听说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '卢安的新市长\n',
            '终于产生了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11FB')

    def _loc_112A(): pass

    label('loc_112A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1198',
    )

    ChrTalk(
        0x00FE,
        (
            '说起来，卢安现在\n',
            '正在选举市长呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那个戴尔蒙的后任啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真希望他能\n',
            '重振卢安啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11FB')

    def _loc_1198(): pass

    label('loc_1198')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_11D6',
    )

    ChrTalk(
        0x00FE,
        (
            '啊，忙死了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '下一个投送地点在东街区……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11FB')

    def _loc_11D6(): pass

    label('loc_11D6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_11FB',
    )

    ChrTalk(
        0x00FE,
        (
            '让开让开，快递公司来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_11FB(): pass

    label('loc_11FB')

    TalkEnd(0x00FE)

    Return()

# id: 0x000B offset: 0x11FF
@scena.Code('func_0B_11FF')
def func_0B_11FF():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_12A7',
    )

    ChrTalk(
        0x00FE,
        (
            '我正在遵照女王陛下的\n',
            '指示挨家挨户地说明情况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大家似乎还没能完全接受，\n',
            '虽然这也是理所当然的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样下去的话稍有风吹草动\n',
            '就有可能引发恐慌……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_156D')

    def _loc_12A7(): pass

    label('loc_12A7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_1356',
    )

    ChrTalk(
        0x00FE,
        (
            '情报部的预算有很多\n',
            '被操纵过的痕迹……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '仅据我所了解的情况，\n',
            '就有不少去向不明的资金。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '恐怕就是这次的\n',
            '坦克的开发费用吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '通过这次的事件都连成线了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_156D')

    def _loc_1356(): pass

    label('loc_1356')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_1424',
    )

    ChrTalk(
        0x00FE,
        (
            '以准将身份回归军队的\n',
            '卡西乌斯先生真了不起。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不仅军事策略，连财政方面也\n',
            '能做出正确的指示。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不愧是击退了帝国军、\n',
            '曾被誉为智将的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在城里和他碰见的话\n',
            '连我也会不自觉地紧张起来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_156D')

    def _loc_1424(): pass

    label('loc_1424')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1459',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，该回城一次向\n',
            '女王陛下报告……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_156D')

    def _loc_1459(): pass

    label('loc_1459')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_1504',
    )

    ChrTalk(
        0x00FE,
        (
            '传言生病了的女王陛下\n',
            '其实很健康哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过她还要收拾政变之后的局势，\n',
            '还有签字仪式的准备工作一定很忙吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我倒是觉得签字仪式\n',
            '稍微推迟一点也没关系……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_156D')

    def _loc_1504(): pass

    label('loc_1504')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_156D',
    )

    ChrTalk(
        0x00FE,
        (
            '我是在王城工作的，\n',
            '正在调查政变事件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然恢复了和平，不过\n',
            '那件事的不良影响还是很深的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_156D(): pass

    label('loc_156D')

    TalkEnd(0x00FE)

    Return()

# id: 0x000C offset: 0x1571
@scena.Code('func_0C_1571')
def func_0C_1571():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_15B3',
    )

    ChrTalk(
        0x00FE,
        (
            '为了不让市民们动摇，\n',
            '我们得保持泰然自若的姿态。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_16B0')

    def _loc_15B3(): pass

    label('loc_15B3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_166A',
    )

    ChrTalk(
        0x00FE,
        (
            '从某种意义上说凯诺娜上尉\n',
            '是个很厉害的女人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '正因为她有能力，\n',
            '才能实行那个作战方案。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是那些无能的士官\n',
            '怎么可能有这种计划。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '和她为敌真是吃不了兜着走。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_16B0')

    def _loc_166A(): pass

    label('loc_166A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_16B0',
    )

    ChrTalk(
        0x00FE,
        (
            '签字仪式虽然在离宫进行，\n',
            '不过上面吩咐也要加强王都的警戒。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_16B0(): pass

    label('loc_16B0')

    TalkEnd(0x00FE)

    Return()

# id: 0x000D offset: 0x16B4
@scena.Code('func_0D_16B4')
def func_0D_16B4():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_16FA',
    )

    ChrTalk(
        0x00FE,
        (
            '没事儿，就算不能使用导力，\n',
            '我也会用刺刀保护大家的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17A2')

    def _loc_16FA(): pass

    label('loc_16FA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_1780',
    )

    ChrTalk(
        0x00FE,
        (
            '如果坦克侵入市区的话\n',
            '受害情况就绝不止这样了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果做错一步的话\n',
            '王都就有可能陷入火海了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……想想都觉得可怕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17A2')

    def _loc_1780(): pass

    label('loc_1780')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_17A2',
    )

    ChrTalk(
        0x00FE,
        (
            '好，现在没\n',
            '任何异常。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_17A2(): pass

    label('loc_17A2')

    TalkEnd(0x00FE)

    Return()

# id: 0x000E offset: 0x17A6
@scena.Code('func_0E_17A6')
def func_0E_17A6():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_17CB',
    )

    ChrTalk(
        0x00FE,
        (
            '吉赛尔　临时消息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_18D6')

    def _loc_17CB(): pass

    label('loc_17CB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_17FA',
    )

    ChrTalk(
        0x00FE,
        (
            '坦克竟然出现在城里，\n',
            '真可怕……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_18D6')

    def _loc_17FA(): pass

    label('loc_17FA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_1849',
    )

    ChrTalk(
        0x00FE,
        (
            '……穿白衣服的女孩子？\n',
            '那孩子迷路了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没看见她出现在附近。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_18D6')

    def _loc_1849(): pass

    label('loc_1849')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1880',
    )

    ChrTalk(
        0x00FE,
        (
            '那么，差不多该\n',
            '要不要回宾馆房间呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_18D6')

    def _loc_1880(): pass

    label('loc_1880')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_18A4',
    )

    ChrTalk(
        0x00FE,
        (
            '好，去城堡参观参观。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_18D6')

    def _loc_18A4(): pass

    label('loc_18A4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_18D6',
    )

    ChrTalk(
        0x00FE,
        (
            '我一直憧憬有一天能\n',
            '住在这家酒店里啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_18D6(): pass

    label('loc_18D6')

    TalkEnd(0x00FE)

    Return()

# id: 0x000F offset: 0x18DA
@scena.Code('func_0F_18DA')
def func_0F_18DA():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    ClearMapFlags(0x02000000)
    OP_77(0xC8, 0xC8, 0xC8, 0x00, 0x00000000)
    OP_11(0x00, 0x00, 0x00, 0x00009470, 0x0001FBD0, 0x00000000)
    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000B, 0x0080)
    SetChrFlags(0x000C, 0x0080)
    SetChrFlags(0x000E, 0x0080)
    OP_4A(0x0009, 255)
    OP_4A(0x000A, 255)
    OP_4A(0x0008, 255)
    OP_4A(0x000B, 255)
    OP_4A(0x000C, 255)
    OP_4A(0x000E, 255)
    LoadEffect(0x00, 'map\\\\mp014_00.eff')
    PlayEffect(0x00, 0xFF, 0x00FF, -2650, 0, 50890, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_6D(-3300, 0, 71820, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, -2540, 0, 73310, 180)
    SetChrPos(0x000D, -2180, 0, 41910, 0)
    ClearChrFlags(0x000D, 0x0080)
    CreateThread(0x000D, 0x03, 0x00, 0x0010)
    Sleep(600)

    FadeIn(1000, 0)

    @scena.Lambda('lambda_1A02')
    def lambda_1A02():
        OP_6D(-2650, 0, 50890, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1A02)

    OP_8E(0x0101, -2590, 0, 51080, 7000, 0x00)

    ChrTalk(
        0x0101,
        (
            '#0010190125V#584F#5P呼、呼……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190126V……………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190127V#588F不可能……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190128V约修亚怎么可能走掉……\n',
            '这……不可能……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#2440190129V#1P哎呀，小姐。\n',
            '你在这里干什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_92(0x000D, 0x0101, 0x000007D0, 0x00000BB8, 0x00)

    ChrTalk(
        0x000D,
        (
            '#2440190130V在被淋湿之前\n',
            '赶紧回家吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190131V#004F#5P啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190132V………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190133V#586F……对，是的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190134V约修亚不可能走掉……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190135V他一定是……先回家了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#2440190136V咦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190137V#006F#5P谢谢你，士兵先生！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190138V我马上回家！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1C3E')
    def lambda_1C3E():
        OP_6D(-1170, 0, 52220, 1000)

        ExitThread()

    DispatchAsync(0x000D, 0x0000, lambda_1C3E)

    @scena.Lambda('lambda_1C56')
    def lambda_1C56():
        OP_67(0, 9500, -10000, 1000)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_1C56)

    OP_8C(0x0101, 45, 800)

    @scena.Lambda('lambda_1C75')
    def lambda_1C75():
        OP_8E(0x0101, 1880, 0, 54600, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1C75)

    WaitForThreadExit(0x0101, 0x0001)

    @scena.Lambda('lambda_1C95')
    def lambda_1C95():
        OP_8E(0x0101, 2360, 0, 60220, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1C95)

    Sleep(1500)

    @scena.Lambda('lambda_1CB5')
    def lambda_1CB5():
        OP_6D(-2550, 0, 49300, 1500)

        ExitThread()

    DispatchAsync(0x000D, 0x0002, lambda_1CB5)

    @scena.Lambda('lambda_1CCD')
    def lambda_1CCD():
        OP_67(0, 9500, -10000, 1500)

        ExitThread()

    DispatchAsync(0x000D, 0x0003, lambda_1CCD)

    Sleep(1500)

    ChrTalk(
        0x000D,
        (
            '#2440190139V怎、怎么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#2440190140V说起来刚才那女孩子……\n',
            '我好像在哪儿见过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000D, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000D,
        (
            '#2440190141V对了！\n',
            '她是帮忙阻止政变的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(3000, 0, -1)
    OP_24(0x01C9, 0x5A)
    OP_0D()
    OP_AD(0x002400B6, 0x0000, 0x0000, 0x00000096)
    Sleep(1000)

    OP_56(0x02)
    OP_20(0x00000FA0)
    CreateThread(0x000D, 0x03, 0x00, 0x0011)
    OP_AE(0x000000C8)
    OP_21()
    WaitForThreadExit(0x000D, 0x0003)
    OP_77(0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    ClearMapFlags(0x10000000)
    NewScene('ED6_DT21/E0001._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0010 offset: 0x1DD8
@scena.Code('func_10_1DD8')
def func_10_1DD8():
    OP_22(0x01C9, 0x01, 0x1E)
    Sleep(300)

    OP_24(0x01C9, 0x28)
    Sleep(300)

    OP_24(0x01C9, 0x32)
    Sleep(300)

    OP_24(0x01C9, 0x3C)
    Sleep(300)

    OP_24(0x01C9, 0x46)
    Sleep(300)

    OP_24(0x01C9, 0x50)
    Sleep(300)

    OP_24(0x01C9, 0x5A)
    Sleep(300)

    OP_24(0x01C9, 0x64)

    Return()

# id: 0x0011 offset: 0x1E1D
@scena.Code('func_11_1E1D')
def func_11_1E1D():
    OP_24(0x01C9, 0x5F)
    Sleep(200)

    OP_24(0x01C9, 0x5A)
    Sleep(200)

    OP_24(0x01C9, 0x55)
    Sleep(200)

    OP_24(0x01C9, 0x50)
    Sleep(200)

    OP_24(0x01C9, 0x4B)
    Sleep(200)

    OP_24(0x01C9, 0x46)
    Sleep(200)

    OP_24(0x01C9, 0x41)
    Sleep(200)

    OP_24(0x01C9, 0x3C)
    Sleep(200)

    OP_24(0x01C9, 0x37)
    Sleep(200)

    OP_24(0x01C9, 0x32)
    Sleep(200)

    OP_24(0x01C9, 0x2D)
    Sleep(200)

    OP_24(0x01C9, 0x28)
    Sleep(200)

    OP_24(0x01C9, 0x23)
    Sleep(200)

    OP_24(0x01C9, 0x1E)
    Sleep(200)

    OP_23(0x01C9)

    Return()

# id: 0x0012 offset: 0x1E9F
@scena.Code('func_12_1E9F')
def func_12_1E9F():
    EventBegin(0x00)
    SetChrFlags(0x0000, 0x0080)
    SetChrFlags(0x0001, 0x0080)
    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000B, 0x0080)
    SetChrFlags(0x000C, 0x0080)
    SetChrFlags(0x000E, 0x0080)
    OP_4A(0x0009, 255)
    OP_4A(0x000A, 255)
    OP_4A(0x0008, 255)
    OP_4A(0x000B, 255)
    OP_4A(0x000C, 255)
    OP_4A(0x000E, 255)
    ClearChrFlags(0x000F, 0x0080)
    SetChrPos(0x000F, -40420, 0, 33150, 360)
    OP_6D(-40710, 0, 35630, 0)
    OP_67(0, 6910, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(120000, 0)
    OP_6E(262, 0)
    OP_69(0x000F, 0x00000000)
    OP_C4(0x00, 0x00000040)
    OP_6A(0x000F)
    FadeIn(2000, 0)
    OP_8F(0x000F, -40220, 0, 33750, 600, 0x00)
    Sleep(100)

    OP_8F(0x000F, -40420, 0, 34550, 1000, 0x00)
    Sleep(50)

    OP_8F(0x000F, -40620, 0, 35630, 600, 0x00)
    Sleep(50)

    ChrTalk(
        0x000F,
        (
            '#0640260975V#480F嗝……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640260976V菲利普那家伙\n',
            '总是对我说三道四……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640260977V他以为\n',
            '我是谁啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640260978V我可是有着第一顺位王位继承权的……\n',
            '杜南·冯·奥赛雷丝……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8F(0x000F, -40320, 0, 36450, 1000, 0x00)
    Sleep(100)

    OP_8F(0x000F, -40120, 0, 37390, 600, 0x00)
    Sleep(50)

    ChrTalk(
        0x000F,
        (
            '#0640260979V#483F唔……\n',
            '好像有点喝多了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640260980V可是那个咖喱饭\n',
            '味道相当不错……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640260981V偶尔尝尝平民的味道也不坏……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8F(0x000F, -40020, 0, 37890, 1000, 0x00)
    Sleep(100)

    OP_8F(0x000F, -39730, 0, 38790, 800, 0x00)
    Sleep(50)

    OP_6A(0x00FF)
    OP_C4(0x01, 0x00000040)

    ChrTalk(
        0x000F,
        (
            '#0640260982V#480F……可恶……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640260983V科洛蒂娅……\n',
            '还有那个游击士小丫头……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640260984V为什么我……\n',
            '……会因为那些小丫头们……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640260985V因为那些小丫头们的话……\n',
            '而心烦意乱……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearChrFlags(0x0010, 0x0080)
    OP_9F(0x0010, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    SetChrPos(0x0010, -39770, 0, 46180, 180)

    NpcTalk(
        0x0010,
        '女人的声音',
        (
            '#0610260986V#2P我了解公爵阁下的\n',
            '痛苦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_9F(0x0010, 0xFF, 0xFF, 0xFF, 0xFF, 0x000003E8)
    OP_62(0x000F, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    OP_20(0x000007D0)
    OP_6D(-39770, 0, 42350, 2000)

    ChrTalk(
        0x000F,
        (
            '#0640260987V#481F#4P什……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640260988V你是理查德的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_1D(0x51)
    Sleep(500)

    ChrTalk(
        0x0010,
        (
            '#0610260989V#1180F#5P嗯，我是他的副官凯诺娜。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610260990V公爵阁下你这么\n',
            '精神真是太好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610260991V#1183F呵呵，不过您的\n',
            '情绪看来不佳……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_91(0x000F, 0, 0, -500, 1000, 0x00)

    ChrTalk(
        0x000F,
        (
            '#0640260992V#484F#4P你、你有什么事……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640260993V我记得你们\n',
            '正受到通缉吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_23D7')
    def lambda_23D7():
        OP_6D(-39600, 0, 41260, 1200)

        ExitThread()

    DispatchAsync(0x000F, 0x0000, lambda_23D7)

    ClearChrFlags(0x0011, 0x0080)
    ClearChrFlags(0x0012, 0x0080)
    SetChrPos(0x0011, -39000, 0, 33000, 0)
    SetChrPos(0x0012, -40500, 0, 33000, 0)

    @scena.Lambda('lambda_241B')
    def lambda_241B():
        OP_8E(0x00FE, -39000, 0, 36500, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_241B)

    Sleep(50)

    @scena.Lambda('lambda_243B')
    def lambda_243B():
        OP_8E(0x00FE, -40500, 0, 36500, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_243B)

    WaitForThreadExit(0x0011, 0x0001)
    WaitForThreadExit(0x0012, 0x0001)
    OP_62(0x000F, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    OP_8C(0x000F, 180, 600)
    OP_62(0x000F, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_91(0x000F, 0, 0, 500, 2000, 0x00)

    ChrTalk(
        0x000F,
        (
            '#0640260994V#484F#6P呀……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_24CD')
    def lambda_24CD():
        OP_6D(-39600, 0, 38790, 2500)

        ExitThread()

    DispatchAsync(0x0010, 0x0002, lambda_24CD)

    @scena.Lambda('lambda_24E5')
    def lambda_24E5():
        OP_92(0x00FE, 0x000F, 0x000007D0, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_24E5)

    Sleep(2000)

    OP_8C(0x000F, 360, 400)
    OP_62(0x000F, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    WaitForThreadExit(0x0010, 0x0002)
    WaitForThreadExit(0x0010, 0x0001)
    Sleep(500)

    ChrTalk(
        0x0010,
        (
            '#0610260995V#1180F呵呵，您这么警惕的话\n',
            '可要受伤的哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610260996V我们只是……\n',
            '想要帮助公爵阁下而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610260997V#1181F好了，请跟我们来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x02000000)
    OP_A2(0x10F0)
    NewScene('ED6_DT21/T0601._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0013 offset: 0x25D0
@scena.Code('func_13_25D0')
def func_13_25D0():
    LoadEffect(0x00, 'map\\\\mpsmk0.eff')
    LoadEffect(0x01, 'map\\\\mpfire2.eff')
    LoadEffect(0x02, 'map\\\\mpkaji0.eff')
    OP_22(0x0087, 0x01, 0x50)
    OP_22(0x00AE, 0x01, 0x50)
    PlayEffect(0x02, 0xFF, 0x00FF, -150, 250, 42190, 0, 0, 0, 2000, 2000, 2000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x00FF, 6610, 1800, -55210, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x00FF, 18680, 5000, 41990, 0, 0, 0, 1500, 1800, 1500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x00FF, -410, 3500, 33390, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x00FF, -16160, 4400, 33500, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x00FF, -610, 3600, 25270, 0, 0, 0, 1300, 1500, 1300, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x00FF, 10660, 5000, 27200, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x00FF, -21520, 5000, 26000, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x00FF, -22010, 5000, 62980, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x00FF, 760, 4200, 58600, 0, 0, 0, 1500, 1700, 1500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x00FF, -46780, 3000, 52260, 0, 0, 0, 1600, 1800, 1600, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x00FF, -610, 3300, 25270, 0, 0, 0, 2200, 2200, 2200, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x00FF, -22010, 4800, 62980, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x00FF, 760, 3800, 58600, 0, 0, 0, 1700, 1700, 1700, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x00FF, 10660, 4800, 27200, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x00FF, -21520, 4700, 26000, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x00FF, -46780, 2480, 52260, 0, 0, 0, 2500, 2500, 2500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x00FF, 16740, 4200, 51970, 0, 0, 0, 1300, 1300, 1300, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x00FF, -410, 3400, 33390, 0, 0, 0, 1100, 1300, 1100, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x00FF, -16160, 3900, 33500, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x00FF, 18680, 4800, 41990, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)

    Return()

# id: 0x0014 offset: 0x2A6C
@scena.Code('func_14_2A6C')
def func_14_2A6C():
    SetChrPos(0x0013, -37620, 0, 37330, 45)
    SetChrPos(0x0014, -41800, 0, 37210, 135)
    SetChrPos(0x0015, 9070, 0, 30110, 315)
    SetChrPos(0x0016, 8300, 0, 66830, 225)
    SetChrPos(0x0017, -6670, 0, 58620, 135)
    SetChrPos(0x0018, -2340, 0, 34710, 180)
    SetChrPos(0x0019, -9060, 250, 28940, 90)
    SetChrPos(0x001A, 13690, 250, 44060, 270)
    SetChrPos(0x001B, 4640, 0, 44330, 225)
    SetChrPos(0x001C, -11050, 0, 50470, 90)
    SetChrPos(0x001D, -30670, 0, 47940, 180)
    SetChrPos(0x001E, 8950, 250, 58550, 225)
    SetChrPos(0x001F, 3900, 0, 60990, 315)
    SetChrPos(0x0020, -7260, 0, 48580, 270)
    SetChrPos(0x0021, -6530, 250, 36470, 315)
    SetChrPos(0x0022, 5150, 10, 30490, 135)
    ClearChrFlags(0x0013, 0x0080)
    ClearChrFlags(0x0015, 0x0080)
    ClearChrFlags(0x0016, 0x0080)
    ClearChrFlags(0x0017, 0x0080)
    ClearChrFlags(0x0018, 0x0080)
    ClearChrFlags(0x001B, 0x0080)
    ClearChrFlags(0x001C, 0x0080)
    ClearChrFlags(0x001D, 0x0080)
    ClearChrFlags(0x0013, 0x0001)
    ClearChrFlags(0x0014, 0x0001)
    ClearChrFlags(0x0015, 0x0001)
    ClearChrFlags(0x0016, 0x0001)
    ClearChrFlags(0x0017, 0x0001)
    ClearChrFlags(0x0018, 0x0001)
    ClearChrFlags(0x0019, 0x0001)
    ClearChrFlags(0x001A, 0x0001)
    ClearChrFlags(0x001B, 0x0001)
    ClearChrFlags(0x001C, 0x0001)
    ClearChrFlags(0x001D, 0x0001)
    ClearChrFlags(0x001E, 0x0001)
    ClearChrFlags(0x001F, 0x0001)
    ClearChrFlags(0x0020, 0x0001)
    ClearChrFlags(0x0021, 0x0001)
    ClearChrFlags(0x0022, 0x0001)
    SetChrFlags(0x0013, 0x0020)
    SetChrFlags(0x0014, 0x0020)
    SetChrFlags(0x0015, 0x0020)
    SetChrFlags(0x0016, 0x0020)
    SetChrFlags(0x0017, 0x0020)
    SetChrFlags(0x0018, 0x0020)
    SetChrFlags(0x0019, 0x0020)
    SetChrFlags(0x001A, 0x0020)
    SetChrFlags(0x001B, 0x0020)
    SetChrFlags(0x001C, 0x0020)
    SetChrFlags(0x001D, 0x0020)
    SetChrFlags(0x001E, 0x0020)
    SetChrFlags(0x001F, 0x0020)
    SetChrFlags(0x0020, 0x0020)
    SetChrFlags(0x0021, 0x0020)
    SetChrFlags(0x0022, 0x0020)

    Return()

# id: 0x0015 offset: 0x2C45
@scena.Code('func_15_2C45')
def func_15_2C45():
    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门上着锁。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    TalkEnd(0x00FF)
    SetMapFlags(0x02000000)

    Return()

# id: 0x0016 offset: 0x2C7E
@scena.Code('func_16_2C7E')
def func_16_2C7E():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 3, 0x203B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2C87',
    )

    Return()

    def _loc_2C87(): pass

    label('loc_2C87')

    EventBegin(0x02)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2CA7',
    )

    Call(0, 0x0018)
    Call(0, 0x0019)
    FadeIn(0, 0)

    def _loc_2CA7(): pass

    label('loc_2CA7')

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '东街区断断续续地\n',
            '传来枪声和剑戟的声音。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2D67',
    )

    ChrTalk(
        0x0101,
        (
            '#0010380161V#1002F（看来是军队在\n',
            '和猎兵作战……)',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010380162V(我们得赶快\n',
            '赶往城堡！)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F6C')

    def _loc_2D67(): pass

    label('loc_2D67')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2DCE',
    )

    ChrTalk(
        0x0102,
        (
            '#0020380163V#1042F（这边布置了\n',
            '军队……)',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020380164V(就交给他们吧，我们去城堡。)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F6C')

    def _loc_2DCE(): pass

    label('loc_2DCE')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2E32',
    )

    ChrTalk(
        0x0103,
        (
            '#0030380165V#022F（这边应该\n',
            '有军队在作战……)',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030380166V(我们还是去城堡吧。)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F6C')

    def _loc_2E32(): pass

    label('loc_2E32')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2EA9',
    )

    ChrTalk(
        0x0107,
        (
            '#0070380167V#062F（军队的失败们看来\n',
            '正在结社的人作战……)',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070380168V(我们得赶快\n',
            '赶往城堡……！)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F6C')

    def _loc_2EA9(): pass

    label('loc_2EA9')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2F11',
    )

    ChrTalk(
        0x0106,
        (
            '#0050380169V#057F（看来军队住在\n',
            '和猎兵们作战……)',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050380170V(我们还是去城堡吧。)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F6C')

    def _loc_2F11(): pass

    label('loc_2F11')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2F6C',
    )

    ChrTalk(
        0x0108,
        (
            '#0080380171V#072F（这边有军队\n',
            '在守护……)',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080250453V(我们赶紧去王城吧)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2F6C(): pass

    label('loc_2F6C')

    OP_90(0x0000, -1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)
    SetMapFlags(0x02000000)

    Return()

# id: 0x0017 offset: 0x2F8D
@scena.Code('func_17_2F8D')
def func_17_2F8D():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 3, 0x203B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2F96',
    )

    Return()

    def _loc_2F96(): pass

    label('loc_2F96')

    EventBegin(0x02)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2FB6',
    )

    Call(0, 0x0018)
    Call(0, 0x0019)
    FadeIn(0, 0)

    def _loc_2FB6(): pass

    label('loc_2FB6')

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '西街区断断续续地\n',
            '传来枪声和剑戟的声音。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3076',
    )

    ChrTalk(
        0x0101,
        (
            '#0010380161V#1002F（看来是军队在\n',
            '和猎兵作战……)',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010380162V(我们得赶快\n',
            '赶往城堡！)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_327B')

    def _loc_3076(): pass

    label('loc_3076')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_30DD',
    )

    ChrTalk(
        0x0102,
        (
            '#0020380163V#1042F（这边布置了\n',
            '军队……)',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020380164V(就交给他们吧，我们去城堡。)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_327B')

    def _loc_30DD(): pass

    label('loc_30DD')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3141',
    )

    ChrTalk(
        0x0103,
        (
            '#0030380165V#022F（这边应该\n',
            '有军队在作战……)',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030380166V(我们还是去城堡吧。)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_327B')

    def _loc_3141(): pass

    label('loc_3141')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_31B8',
    )

    ChrTalk(
        0x0107,
        (
            '#0070380167V#062F（军队的失败们看来\n',
            '正在结社的人作战……)',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070380168V(我们得赶快\n',
            '赶往城堡……！)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_327B')

    def _loc_31B8(): pass

    label('loc_31B8')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3220',
    )

    ChrTalk(
        0x0106,
        (
            '#0050380169V#057F（看来军队住在\n',
            '和猎兵们作战……)',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050380170V(我们还是去城堡吧。)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_327B')

    def _loc_3220(): pass

    label('loc_3220')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_327B',
    )

    ChrTalk(
        0x0108,
        (
            '#0080380171V#072F（这边有军队\n',
            '在守护……)',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080250453V(我们赶紧去王城吧)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_327B(): pass

    label('loc_327B')

    OP_90(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)
    SetMapFlags(0x02000000)

    Return()

# id: 0x0018 offset: 0x329C
@scena.Code('func_18_329C')
def func_18_329C():
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
        (0x00000000, 'loc_3316'),
        (0x00000001, 'loc_331C'),
        (-1, 'loc_3322'),
    )

    def _loc_3316(): pass

    label('loc_3316')

    OP_A2(0x1200)

    Jump('loc_3322')

    def _loc_331C(): pass

    label('loc_331C')

    OP_A2(0x1201)

    Jump('loc_3322')

    def _loc_3322(): pass

    label('loc_3322')

    Return()

# id: 0x0019 offset: 0x3323
@scena.Code('func_19_3323')
def func_19_3323():
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

# id: 0x001A offset: 0x337C
@scena.Code('func_1A_337C')
def func_1A_337C():
    SetPlaceName(0x00B4)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
