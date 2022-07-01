import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C5403_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C5403   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
    TXT(0x02, '基尔巴特'),
    TXT(0x03, '暴动钢臂（白）'),
    TXT(0x04, '暴动钢臂（白）'),
    TXT(0x05, '目标探索者'),
    TXT(0x06, '哨兵570（蓝）'),
    TXT(0x07, '哨兵235（红）'),
    TXT(0x08, '目标探索者'),
    TXT(0x09, '目标探索者'),
    TXT(0x0A, '哨兵570（蓝）'),
    TXT(0x0B, '哨兵235（红）'),
    TXT(0x0C, '目标探索者'),
    TXT(0x0D, '据点武装者'),
    TXT(0x0E, '据点武装者'),
    TXT(0x0F, '据点武装者'),
    TXT(0x10, '据点武装者'),
    TXT(0x11, '目标探索者'),
    TXT(0x12, '哨兵570（蓝）'),
    TXT(0x13, '哨兵235（红）'),
    TXT(0x14, '目标探索者'),
    TXT(0x15, '目标探索者'),
    TXT(0x16, '哨兵570（蓝）'),
    TXT(0x17, '哨兵235（红）'),
    TXT(0x18, '目标探索者'),
    TXT(0x19, '据点武装者'),
    TXT(0x1A, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'C5403.x'
    header.mapIndex       = 1
    header.bgm            = 28
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x4261
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
        ('ED6_DT29/CH12570._CH', 'ED6_DT29/CH12570P._CP'),
        ('ED6_DT29/CH12571._CH', 'ED6_DT29/CH12571P._CP'),
        ('ED6_DT29/CH12350._CH', 'ED6_DT29/CH12350P._CP'),
        ('ED6_DT29/CH12351._CH', 'ED6_DT29/CH12351P._CP'),
        ('ED6_DT26/CH20255._CH', 'ED6_DT26/CH20255P._CP'),
        ('ED6_DT26/CH20255._CH', 'ED6_DT26/CH20255P._CP'),
        ('ED6_DT29/CH12310._CH', 'ED6_DT29/CH12310P._CP'),
        ('ED6_DT29/CH12310._CH', 'ED6_DT29/CH12310P._CP'),
        ('ED6_DT29/CH12320._CH', 'ED6_DT29/CH12320P._CP'),
        ('ED6_DT29/CH12321._CH', 'ED6_DT29/CH12321P._CP'),
        ('ED6_DT27/CH03750._CH', 'ED6_DT27/CH03750P._CP'),
        ('ED6_DT29/CH12530._CH', 'ED6_DT29/CH12530P._CP'),
        ('ED6_DT29/CH12531._CH', 'ED6_DT29/CH12531P._CP'),
        ('ED6_DT26/CH20501._CH', 'ED6_DT26/CH20501P._CP'),
    ]

# id: 0x10002 offset: 0x11A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 35060,
            z                   = 2000,
            y                   = -35010,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
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
            dword_10            = 11,
            chipIndex           = 11,
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
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x19A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = 34000,
            z           = 1000,
            y           = -76880,
            word_0C     = 0x0000,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0427,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 82050,
            z           = 0,
            y           = -27100,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0424,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 82050,
            z           = 0,
            y           = 27210,
            word_0C     = 0x0000,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0427,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 32040,
            z           = 1000,
            y           = 116120,
            word_0C     = 0x0000,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0427,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -34140,
            z           = 1000,
            y           = 116640,
            word_0C     = 0x0000,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0427,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -87240,
            z           = 0,
            y           = 27500,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0424,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -86970,
            z           = 0,
            y           = -24730,
            word_0C     = 0x0000,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0427,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -33900,
            z           = 1000,
            y           = -75690,
            word_0C     = 0x0000,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0427,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -830,
            z           = 0,
            y           = -16890,
            word_0C     = 0x0000,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0426,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -940,
            z           = 0,
            y           = 8910,
            word_0C     = 0x0000,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0426,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -1050,
            z           = 0,
            y           = 23020,
            word_0C     = 0x0000,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0426,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -910,
            z           = 0,
            y           = -28570,
            word_0C     = 0x0000,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0426,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 34000,
            z           = 1000,
            y           = -76880,
            word_0C     = 0x0000,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0430,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 82050,
            z           = 0,
            y           = -27100,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x042D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 82050,
            z           = 0,
            y           = 27210,
            word_0C     = 0x0000,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0430,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 32040,
            z           = 1000,
            y           = 116120,
            word_0C     = 0x0000,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0430,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -34140,
            z           = 1000,
            y           = 116640,
            word_0C     = 0x0000,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0430,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -87240,
            z           = 0,
            y           = 27500,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x042D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -86970,
            z           = 0,
            y           = -24730,
            word_0C     = 0x0000,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0430,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -33900,
            z           = 1000,
            y           = -75690,
            word_0C     = 0x0000,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0430,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -1050,
            z           = 0,
            y           = 23020,
            word_0C     = 0x0000,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x042F,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x3E6
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 0,
            y           = -1000,
            z           = 82020,
            range       = 3000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000011,
        ),
        ScenaEventData(
            x           = -6200,
            y           = -1000,
            z           = -27740,
            range       = 4700,
            dword_10    = 0x00000BB8,
            dword_14    = 0xFFFF978C,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000012,
        ),
        ScenaEventData(
            x           = -5910,
            y           = -1000,
            z           = 31010,
            range       = 3950,
            dword_10    = 0x000007D0,
            dword_14    = 0x0000695A,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000001D,
        ),
        ScenaEventData(
            x           = -5690,
            y           = -1000,
            z           = -32460,
            range       = 4110,
            dword_10    = 0x000007D0,
            dword_14    = 0xFFFF6E2E,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000001E,
        ),
        ScenaEventData(
            x           = 80120,
            y           = -1000,
            z           = -36990,
            range       = 84020,
            dword_10    = 0x000007D0,
            dword_14    = 0xFFFF6000,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000001F,
        ),
        ScenaEventData(
            x           = 80070,
            y           = -1000,
            z           = 8600,
            range       = 83680,
            dword_10    = 0x000007D0,
            dword_14    = 0x000012AC,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000020,
        ),
        ScenaEventData(
            x           = -127880,
            y           = -1000,
            z           = 10750,
            range       = -124230,
            dword_10    = 0x000007D0,
            dword_14    = 0x00001AFE,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000021,
        ),
        ScenaEventData(
            x           = -88820,
            y           = -1000,
            z           = 10590,
            range       = -84910,
            dword_10    = 0x000007D0,
            dword_14    = 0x00001B6C,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000022,
        ),
    )

# id: 0x10005 offset: 0x4E6
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -42690,
            triggerZ            = 0,
            triggerY            = -31970,
            triggerRange        = 1000,
            actorX              = -42030,
            actorZ              = 0,
            actorY              = -31970,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 35680,
            triggerZ            = 0,
            triggerY            = -35010,
            triggerRange        = 1000,
            actorX              = 35060,
            actorZ              = 0,
            actorY              = -35010,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 3580,
            triggerZ            = 0,
            triggerY            = 79630,
            triggerRange        = 1000,
            actorX              = 3580,
            actorZ              = 1000,
            actorY              = 79630,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x001B,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 41170,
            triggerZ            = 0,
            triggerY            = 60740,
            triggerRange        = 1000,
            actorX              = 41740,
            actorZ              = 1000,
            actorY              = 60890,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 41200,
            triggerZ            = 0,
            triggerY            = 59640,
            triggerRange        = 1000,
            actorX              = 41740,
            actorZ              = 1000,
            actorY              = 59710,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 41220,
            triggerZ            = 0,
            triggerY            = 58190,
            triggerRange        = 1000,
            actorX              = 41930,
            actorZ              = 1000,
            actorY              = 58370,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 41190,
            triggerZ            = 0,
            triggerY            = 56900,
            triggerRange        = 1000,
            actorX              = 42060,
            actorZ              = 1000,
            actorY              = 57120,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 38140,
            triggerZ            = 0,
            triggerY            = 62850,
            triggerRange        = 1000,
            actorX              = 38130,
            actorZ              = 1000,
            actorY              = 63510,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0009,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 38390,
            triggerZ            = 0,
            triggerY            = 55260,
            triggerRange        = 1000,
            actorX              = 38380,
            actorZ              = 1000,
            actorY              = 54650,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000A,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 41600,
            triggerZ            = 0,
            triggerY            = 15510,
            triggerRange        = 1000,
            actorX              = 42260,
            actorZ              = 0,
            actorY              = 15480,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000B,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 41600,
            triggerZ            = 0,
            triggerY            = 12030,
            triggerRange        = 1000,
            actorX              = 42210,
            actorZ              = 0,
            actorY              = 11950,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000C,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 41590,
            triggerZ            = 0,
            triggerY            = 8540,
            triggerRange        = 1000,
            actorX              = 42300,
            actorZ              = 0,
            actorY              = 8510,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000D,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -43620,
            triggerZ            = 0,
            triggerY            = 17790,
            triggerRange        = 1000,
            actorX              = -43660,
            actorZ              = 0,
            actorY              = 18410,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000E,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -39950,
            triggerZ            = 0,
            triggerY            = 17800,
            triggerRange        = 1000,
            actorX              = -39990,
            actorZ              = 0,
            actorY              = 18410,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000F,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -36240,
            triggerZ            = 0,
            triggerY            = 17800,
            triggerRange        = 1000,
            actorX              = -36280,
            actorZ              = 0,
            actorY              = 18510,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0010,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 4960,
            triggerZ            = 0,
            triggerY            = 77000,
            triggerRange        = 1000,
            actorX              = 4960,
            actorZ              = 1000,
            actorY              = 77000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0024,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x726
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0444, 7, 0x2227)),
            Expr.Return,
        ),
        'loc_757',
    )

    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x0009, -1950, 0, -22900, 180)
    ClearChrFlags(0x0009, 0x0001)
    SetChrFlags(0x0009, 0x0002)
    SetChrChipByIndex(0x0009, 13)
    SetChrSubChip(0x0009, 5)

    def _loc_757(): pass

    label('loc_757')

    Return()

# id: 0x0001 offset: 0x758
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_776',
    )

    ExecExpressionWithVar(
        0x3B,
        (
            (Expr.PushLong, 0x227),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x3C,
        (
            (Expr.PushLong, 0x10A),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_776(): pass

    label('loc_776')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A6, 6, 0x1D36)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_788',
    )

    OP_6F(0x0024, 0)

    Jump('loc_78F')

    def _loc_788(): pass

    label('loc_788')

    OP_6F(0x0024, 60)

    def _loc_78F(): pass

    label('loc_78F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A6, 7, 0x1D37)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7A1',
    )

    OP_6F(0x0025, 0)

    Jump('loc_7A8')

    def _loc_7A1(): pass

    label('loc_7A1')

    OP_6F(0x0025, 60)

    def _loc_7A8(): pass

    label('loc_7A8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A7, 5, 0x1D3D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7BA',
    )

    OP_6F(0x0029, 0)

    Jump('loc_7C1')

    def _loc_7BA(): pass

    label('loc_7BA')

    OP_6F(0x0029, 60)

    def _loc_7C1(): pass

    label('loc_7C1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A7, 6, 0x1D3E)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7D3',
    )

    OP_6F(0x002A, 0)

    Jump('loc_7DA')

    def _loc_7D3(): pass

    label('loc_7D3')

    OP_6F(0x002A, 60)

    def _loc_7DA(): pass

    label('loc_7DA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A7, 7, 0x1D3F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7EC',
    )

    OP_6F(0x002B, 0)

    Jump('loc_7F3')

    def _loc_7EC(): pass

    label('loc_7EC')

    OP_6F(0x002B, 60)

    def _loc_7F3(): pass

    label('loc_7F3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A8, 0, 0x1D40)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_805',
    )

    OP_6F(0x002C, 0)

    Jump('loc_80C')

    def _loc_805(): pass

    label('loc_805')

    OP_6F(0x002C, 60)

    def _loc_80C(): pass

    label('loc_80C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A8, 1, 0x1D41)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_81E',
    )

    OP_6F(0x002D, 0)

    Jump('loc_825')

    def _loc_81E(): pass

    label('loc_81E')

    OP_6F(0x002D, 60)

    def _loc_825(): pass

    label('loc_825')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A8, 2, 0x1D42)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_837',
    )

    OP_6F(0x002E, 0)

    Jump('loc_83E')

    def _loc_837(): pass

    label('loc_837')

    OP_6F(0x002E, 60)

    def _loc_83E(): pass

    label('loc_83E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A8, 3, 0x1D43)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_850',
    )

    OP_6F(0x002F, 0)

    Jump('loc_857')

    def _loc_850(): pass

    label('loc_850')

    OP_6F(0x002F, 60)

    def _loc_857(): pass

    label('loc_857')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A8, 4, 0x1D44)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_869',
    )

    OP_6F(0x0030, 0)

    Jump('loc_870')

    def _loc_869(): pass

    label('loc_869')

    OP_6F(0x0030, 60)

    def _loc_870(): pass

    label('loc_870')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A8, 6, 0x1D46)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_882',
    )

    OP_6F(0x0031, 0)

    Jump('loc_889')

    def _loc_882(): pass

    label('loc_882')

    OP_6F(0x0031, 60)

    def _loc_889(): pass

    label('loc_889')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A8, 7, 0x1D47)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_89B',
    )

    OP_6F(0x0032, 0)

    Jump('loc_8A2')

    def _loc_89B(): pass

    label('loc_89B')

    OP_6F(0x0032, 60)

    def _loc_8A2(): pass

    label('loc_8A2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A9, 0, 0x1D48)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8B4',
    )

    OP_6F(0x0033, 0)

    Jump('loc_8BB')

    def _loc_8B4(): pass

    label('loc_8B4')

    OP_6F(0x0033, 60)

    def _loc_8BB(): pass

    label('loc_8BB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A9, 1, 0x1D49)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8CD',
    )

    OP_6F(0x0034, 0)

    Jump('loc_8D4')

    def _loc_8CD(): pass

    label('loc_8CD')

    OP_6F(0x0034, 60)

    def _loc_8D4(): pass

    label('loc_8D4')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_929',
    )

    LoadEffect(0x00, 'map\\\\mp027_00.eff')
    PlayEffect(0x00, 0x00, 0x00FF, 3580, 1200, 79630, 0, 0, 0, 1300, 1300, 1300, 0x00FF, 0, 0, 0, 0)

    def _loc_929(): pass

    label('loc_929')

    ExecExpressionWithValue(
        0x0014,
        0x24,
        (
            (Expr.PushLong, 0xEF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0015,
        0x24,
        (
            (Expr.PushLong, 0xEF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0016,
        0x24,
        (
            (Expr.PushLong, 0xEF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0017,
        0x24,
        (
            (Expr.PushLong, 0xEF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0020,
        0x24,
        (
            (Expr.PushLong, 0xEF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_9AB',
    )

    SetChrFlags(0x000C, 0x0080)
    SetChrFlags(0x000D, 0x0080)
    SetChrFlags(0x000E, 0x0080)
    SetChrFlags(0x000F, 0x0080)
    SetChrFlags(0x0010, 0x0080)
    SetChrFlags(0x0011, 0x0080)
    SetChrFlags(0x0012, 0x0080)
    SetChrFlags(0x0013, 0x0080)
    SetChrFlags(0x0014, 0x0080)
    SetChrFlags(0x0015, 0x0080)
    SetChrFlags(0x0016, 0x0080)
    SetChrFlags(0x0017, 0x0080)

    Jump('loc_9D8')

    def _loc_9AB(): pass

    label('loc_9AB')

    SetChrFlags(0x0018, 0x0080)
    SetChrFlags(0x0019, 0x0080)
    SetChrFlags(0x001A, 0x0080)
    SetChrFlags(0x001B, 0x0080)
    SetChrFlags(0x001C, 0x0080)
    SetChrFlags(0x001D, 0x0080)
    SetChrFlags(0x001E, 0x0080)
    SetChrFlags(0x001F, 0x0080)
    SetChrFlags(0x0020, 0x0080)

    def _loc_9D8(): pass

    label('loc_9D8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0444, 5, 0x2225)),
            (Expr.TestScenaFlags, ScenaFlag(0x0444, 7, 0x2227)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_A6C',
    )

    OP_72(0x0017, 0x0010)
    OP_6F(0x0002, 100)
    OP_6F(0x0004, 100)
    OP_6F(0x0005, 100)
    OP_BE(0x02, 0x01, 0x0002, 0x0064, 0x0000, 0x02, 80500, -1000, -37650, 84000, 2000, -40350)
    OP_BE(0x04, 0x01, 0x0002, 0x0064, 0x0000, 0x02, -128000, -1000, 7600, -123800, 2000, 10360)
    OP_BE(0x05, 0x01, 0x0002, 0x0064, 0x0000, 0x02, -88290, 0, 10370, -85540, 2000, 7640)
    SetChrFlags(0x0017, 0x0080)

    Jump('loc_A6C')

    def _loc_A6C(): pass

    label('loc_A6C')

    Call(0, 0x001C)

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
            (Expr.PushValueByIndex, 0x29),
            (Expr.PushLong, 0x434),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B5D',
    )

    OP_D2(0x002703A8, 0x002703B2, 0x0E)
    OP_D2(0x002703AC, 0x002703B6, 0x0F)
    OP_D2(0x002703AE, 0x002703B8, 0x10)
    OP_D2(0x0026020B, 0x00260210, 0x11)
    OP_D2(0x00290216, 0x0029021A, 0x12)
    OP_D2(0x00270110, 0x00270120, 0x13)
    OP_D2(0x00270130, 0x00270140, 0x14)
    OP_D2(0x000702B4, 0x000702BB, 0x15)

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_B02'),
        (0x00000003, 'loc_B0F'),
        (0x00000004, 'loc_B1C'),
        (0x00000005, 'loc_B29'),
        (0x00000006, 'loc_B36'),
        (0x00000007, 'loc_B43'),
        (0x00000008, 'loc_B50'),
        (-1, 'loc_B5D'),
    )

    def _loc_B02(): pass

    label('loc_B02')

    OP_D2(0x000701D0, 0x000701DC, 0x16)

    Jump('loc_B5D')

    def _loc_B0F(): pass

    label('loc_B0F')

    OP_D2(0x000701E8, 0x000701F4, 0x16)

    Jump('loc_B5D')

    def _loc_B1C(): pass

    label('loc_B1C')

    OP_D2(0x0027036E, 0x0027037B, 0x16)

    Jump('loc_B5D')

    def _loc_B29(): pass

    label('loc_B29')

    OP_D2(0x00070218, 0x00070224, 0x16)

    Jump('loc_B5D')

    def _loc_B36(): pass

    label('loc_B36')

    OP_D2(0x00070230, 0x0007023C, 0x16)

    Jump('loc_B5D')

    def _loc_B43(): pass

    label('loc_B43')

    OP_D2(0x00070248, 0x00070254, 0x16)

    Jump('loc_B5D')

    def _loc_B50(): pass

    label('loc_B50')

    OP_D2(0x00270176, 0x00270183, 0x16)

    Jump('loc_B5D')

    def _loc_B5D(): pass

    label('loc_B5D')

    Return()

# id: 0x0002 offset: 0xB5E
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_B73',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('ReInit')

    def _loc_B73(): pass

    label('loc_B73')

    Return()

# id: 0x0003 offset: 0xB74
@scena.Code('func_03_B74')
def func_03_B74():
    UnlockAchievement(0x02, 0x63, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A6, 6, 0x1D36)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C51',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0024, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['兔跃靴'], 1)"),
            Expr.Return,
        ),
        'loc_BE8',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['兔跃靴']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1D36)

    Jump('loc_C4E')

    def _loc_BE8(): pass

    label('loc_BE8')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['兔跃靴']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['兔跃靴']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0024, 60)
    OP_70(0x0024, 0x00000000)

    def _loc_C4E(): pass

    label('loc_C4E')

    Jump('loc_C82')

    def _loc_C51(): pass

    label('loc_C51')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_C82(): pass

    label('loc_C82')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0xC90
@scena.Code('func_04_C90')
def func_04_C90():
    UnlockAchievement(0x02, 0x64, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A6, 7, 0x1D37)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_E28',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0025, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A7, 0, 0x1D38)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_D74',
    )

    OP_9F(0x0008, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    ChrTurnDirection(0x0008, 0x0000, 0)
    OP_91(0x0008, 0, 1000, 0, 0, 0x00)

    @scena.Lambda('lambda_0CE7')
    def lambda_0CE7():
        OP_91(0x00FE, 0, -1000, 0, 600, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0CE7)

    @scena.Lambda('lambda_0D02')
    def lambda_0D02():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000258)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_0D02)

    ClearChrFlags(0x0008, 0x0080)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '魔兽出现了！',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Battle(0x0000042C, 0x00000000, 0x00, 0x0000, 0xFF)
    SetChrFlags(0x0008, 0x0080)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_D4F'),
        (0x00000002, 'loc_D61'),
        (0x00000001, 'loc_D71'),
        (-1, 'loc_D74'),
    )

    def _loc_D4F(): pass

    label('loc_D4F')

    OP_A2(0x1D38)
    OP_6F(0x0025, 60)
    Sleep(500)

    Jump('loc_D74')

    def _loc_D61(): pass

    label('loc_D61')

    OP_6F(0x0025, 0)
    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

    def _loc_D71(): pass

    label('loc_D71')

    OP_B4(0x00)

    Return()

    def _loc_D74(): pass

    label('loc_D74')

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['七轮棍'], 1)"),
            Expr.Return,
        ),
        'loc_DC3',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['七轮棍']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1D37)

    Jump('loc_E25')

    def _loc_DC3(): pass

    label('loc_DC3')

    FadeOut(300, 0, 100)

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['七轮棍']),
            (TxtCtl.SetColor, 0x0),
            '。 \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['七轮棍']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0025, 60)
    OP_70(0x0025, 0x00000000)

    def _loc_E25(): pass

    label('loc_E25')

    Jump('loc_E57')

    def _loc_E28(): pass

    label('loc_E28')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_E57(): pass

    label('loc_E57')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0xE65
@scena.Code('func_05_E65')
def func_05_E65():
    UnlockAchievement(0x02, 0x65, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A7, 5, 0x1D3D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_F42',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0029, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['大回复药'], 1)"),
            Expr.Return,
        ),
        'loc_ED9',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['大回复药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1D3D)

    Jump('loc_F3F')

    def _loc_ED9(): pass

    label('loc_ED9')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['大回复药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['大回复药']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0029, 60)
    OP_70(0x0029, 0x00000000)

    def _loc_F3F(): pass

    label('loc_F3F')

    Jump('loc_F73')

    def _loc_F42(): pass

    label('loc_F42')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_F73(): pass

    label('loc_F73')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0006 offset: 0xF81
@scena.Code('func_06_F81')
def func_06_F81():
    UnlockAchievement(0x02, 0x66, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A7, 6, 0x1D3E)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_105E',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x002A, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['漆黑弥赛亚'], 1)"),
            Expr.Return,
        ),
        'loc_FF5',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['漆黑弥赛亚']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1D3E)

    Jump('loc_105B')

    def _loc_FF5(): pass

    label('loc_FF5')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['漆黑弥赛亚']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['漆黑弥赛亚']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x002A, 60)
    OP_70(0x002A, 0x00000000)

    def _loc_105B(): pass

    label('loc_105B')

    Jump('loc_108F')

    def _loc_105E(): pass

    label('loc_105E')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_108F(): pass

    label('loc_108F')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0007 offset: 0x109D
@scena.Code('func_07_109D')
def func_07_109D():
    UnlockAchievement(0x02, 0x67, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A7, 7, 0x1D3F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_117A',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x002B, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['EP填充剂Ⅱ'], 1)"),
            Expr.Return,
        ),
        'loc_1111',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅱ']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1D3F)

    Jump('loc_1177')

    def _loc_1111(): pass

    label('loc_1111')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅱ']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅱ']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x002B, 60)
    OP_70(0x002B, 0x00000000)

    def _loc_1177(): pass

    label('loc_1177')

    Jump('loc_11AB')

    def _loc_117A(): pass

    label('loc_117A')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_11AB(): pass

    label('loc_11AB')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0008 offset: 0x11B9
@scena.Code('func_08_11B9')
def func_08_11B9():
    UnlockAchievement(0x02, 0x68, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A8, 0, 0x1D40)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1296',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x002C, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['大回复药'], 1)"),
            Expr.Return,
        ),
        'loc_122D',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['大回复药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1D40)

    Jump('loc_1293')

    def _loc_122D(): pass

    label('loc_122D')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['大回复药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['大回复药']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x002C, 60)
    OP_70(0x002C, 0x00000000)

    def _loc_1293(): pass

    label('loc_1293')

    Jump('loc_12C7')

    def _loc_1296(): pass

    label('loc_1296')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_12C7(): pass

    label('loc_12C7')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0009 offset: 0x12D5
@scena.Code('func_09_12D5')
def func_09_12D5():
    UnlockAchievement(0x02, 0x69, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A8, 1, 0x1D41)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_13B2',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x002D, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['圣灵药'], 1)"),
            Expr.Return,
        ),
        'loc_1349',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['圣灵药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1D41)

    Jump('loc_13AF')

    def _loc_1349(): pass

    label('loc_1349')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['圣灵药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['圣灵药']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x002D, 60)
    OP_70(0x002D, 0x00000000)

    def _loc_13AF(): pass

    label('loc_13AF')

    Jump('loc_13E3')

    def _loc_13B2(): pass

    label('loc_13B2')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_13E3(): pass

    label('loc_13E3')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x000A offset: 0x13F1
@scena.Code('func_0A_13F1')
def func_0A_13F1():
    UnlockAchievement(0x02, 0x6A, 0x01, 0x00)
    SetMapFlags(0x08000000)
    FadeOut(300, 0, 100)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A8, 2, 0x1D42)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_151D',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x002E, 0x0000001E)
    OP_73(0x002E)
    OP_6F(0x002E, 30)
    AddSepith(0x00, 0x0064)
    AddSepith(0x01, 0x0064)
    AddSepith(0x02, 0x0064)
    AddSepith(0x03, 0x0064)
    AddSepith(0x04, 0x0064)
    AddSepith(0x05, 0x0064)
    AddSepith(0x06, 0x0064)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '#56I地之耀晶片×１００\n',
            (TxtCtl.SetColor, 0x2),
            '#57I水之耀晶片×１００\n',
            (TxtCtl.SetColor, 0x2),
            '#58I火之耀晶片×１００\n',
            (TxtCtl.SetColor, 0x2),
            '#59I风之耀晶片×１００\n',
            (TxtCtl.SetColor, 0x2),
            '#62I时之耀晶片×１００\n',
            (TxtCtl.SetColor, 0x2),
            '#60I空之耀晶片×１００\n',
            (TxtCtl.SetColor, 0x2),
            '#61I幻之耀晶片×１００\n',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x1D42)

    Jump('loc_1537')

    def _loc_151D(): pass

    label('loc_151D')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_1537(): pass

    label('loc_1537')

    FadeIn(300, 0)
    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x000B offset: 0x1549
@scena.Code('func_0B_1549')
def func_0B_1549():
    UnlockAchievement(0x02, 0x6B, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A8, 3, 0x1D43)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1626',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x002F, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['圣灵药'], 1)"),
            Expr.Return,
        ),
        'loc_15BD',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['圣灵药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1D43)

    Jump('loc_1623')

    def _loc_15BD(): pass

    label('loc_15BD')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['圣灵药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['圣灵药']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x002F, 60)
    OP_70(0x002F, 0x00000000)

    def _loc_1623(): pass

    label('loc_1623')

    Jump('loc_1657')

    def _loc_1626(): pass

    label('loc_1626')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_1657(): pass

    label('loc_1657')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x000C offset: 0x1665
@scena.Code('func_0C_1665')
def func_0C_1665():
    UnlockAchievement(0x02, 0x6C, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A8, 4, 0x1D44)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1742',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0030, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['金色女伯爵'], 1)"),
            Expr.Return,
        ),
        'loc_16D9',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['金色女伯爵']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1D44)

    Jump('loc_173F')

    def _loc_16D9(): pass

    label('loc_16D9')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['金色女伯爵']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['金色女伯爵']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0030, 60)
    OP_70(0x0030, 0x00000000)

    def _loc_173F(): pass

    label('loc_173F')

    Jump('loc_1773')

    def _loc_1742(): pass

    label('loc_1742')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_1773(): pass

    label('loc_1773')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x000D offset: 0x1781
@scena.Code('func_0D_1781')
def func_0D_1781():
    UnlockAchievement(0x02, 0x6D, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A8, 6, 0x1D46)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_185E',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0031, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['大回复药'], 1)"),
            Expr.Return,
        ),
        'loc_17F5',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['大回复药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1D46)

    Jump('loc_185B')

    def _loc_17F5(): pass

    label('loc_17F5')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['大回复药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['大回复药']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0031, 60)
    OP_70(0x0031, 0x00000000)

    def _loc_185B(): pass

    label('loc_185B')

    Jump('loc_188F')

    def _loc_185E(): pass

    label('loc_185E')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_188F(): pass

    label('loc_188F')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x000E offset: 0x189D
@scena.Code('func_0E_189D')
def func_0E_189D():
    UnlockAchievement(0x02, 0x6E, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A8, 7, 0x1D47)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_197A',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0032, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['Ｓ－药片'], 1)"),
            Expr.Return,
        ),
        'loc_1911',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['Ｓ－药片']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1D47)

    Jump('loc_1977')

    def _loc_1911(): pass

    label('loc_1911')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['Ｓ－药片']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['Ｓ－药片']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0032, 60)
    OP_70(0x0032, 0x00000000)

    def _loc_1977(): pass

    label('loc_1977')

    Jump('loc_19AB')

    def _loc_197A(): pass

    label('loc_197A')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_19AB(): pass

    label('loc_19AB')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x000F offset: 0x19B9
@scena.Code('func_0F_19B9')
def func_0F_19B9():
    UnlockAchievement(0x02, 0x6F, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A9, 0, 0x1D48)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1A96',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0033, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['EP填充剂Ⅱ'], 1)"),
            Expr.Return,
        ),
        'loc_1A2D',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅱ']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1D48)

    Jump('loc_1A93')

    def _loc_1A2D(): pass

    label('loc_1A2D')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅱ']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅱ']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0033, 60)
    OP_70(0x0033, 0x00000000)

    def _loc_1A93(): pass

    label('loc_1A93')

    Jump('loc_1AC7')

    def _loc_1A96(): pass

    label('loc_1A96')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_1AC7(): pass

    label('loc_1AC7')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0010 offset: 0x1AD5
@scena.Code('func_10_1AD5')
def func_10_1AD5():
    UnlockAchievement(0x02, 0x70, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A9, 1, 0x1D49)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1BB2',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0034, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['还魂粉'], 1)"),
            Expr.Return,
        ),
        'loc_1B49',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['还魂粉']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1D49)

    Jump('loc_1BAF')

    def _loc_1B49(): pass

    label('loc_1B49')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['还魂粉']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['还魂粉']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0034, 60)
    OP_70(0x0034, 0x00000000)

    def _loc_1BAF(): pass

    label('loc_1BAF')

    Jump('loc_1BE3')

    def _loc_1BB2(): pass

    label('loc_1BB2')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_1BE3(): pass

    label('loc_1BE3')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0011 offset: 0x1BF1
@scena.Code('func_11_1BF1')
def func_11_1BF1():
    OP_A3(0x1C81)
    OP_A3(0x1C82)
    OP_A3(0x1C83)
    OP_A3(0x1C84)
    OP_A2(0x1C85)
    OP_A3(0x1C86)
    OP_A3(0x1C87)
    OP_A3(0x1C88)

    Return()

# id: 0x0012 offset: 0x1C0A
@scena.Code('func_12_1C0A')
def func_12_1C0A():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0444, 5, 0x2225)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0444, 7, 0x2227)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_1C17',
    )

    Return()

    def _loc_1C17(): pass

    label('loc_1C17')

    Call(0, 0x0013)
    Call(0, 0x0014)

    Return()

# id: 0x0013 offset: 0x1C20
@scena.Code('func_13_1C20')
def func_13_1C20():
    EventBegin(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1C45',
    )

    Call(0, 0x001A)
    Call(0, 0x0023)
    FadeIn(0, 0)
    Sleep(100)

    def _loc_1C45(): pass

    label('loc_1C45')

    CreateThread(0x00F9, 0x03, 0x00, 0x0025)
    OP_22(0x006B, 0x00, 0x64)
    OP_6F(0x0001, 0)
    OP_70(0x0001, 0x00000064)
    Sleep(1500)

    OP_22(0x009D, 0x00, 0x64)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x010B, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1CE4',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_1D22')

    def _loc_1CE4(): pass

    label('loc_1CE4')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1D0B',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_1D22')

    def _loc_1D0B(): pass

    label('loc_1D0B')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    def _loc_1D22(): pass

    label('loc_1D22')

    Sleep(1000)

    @scena.Lambda('lambda_1D2D')
    def lambda_1D2D():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1D2D)

    Sleep(50)

    @scena.Lambda('lambda_1D40')
    def lambda_1D40():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1D40)

    Sleep(50)

    @scena.Lambda('lambda_1D53')
    def lambda_1D53():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x010B, 0x0001, lambda_1D53)

    Sleep(50)

    OP_8C(0x00F9, 180, 400)
    SetChrFlags(0x0020, 0x0080)
    Fade(500)
    OP_6D(150, 0, -28510, 0)
    OP_67(0, 6420, -10000, 0)
    OP_6B(3380, 0)
    OP_6C(45000, 0)
    OP_6E(303, 0)
    SetChrPos(0x0101, -1540, 0, -27810, 180)
    SetChrPos(0x0102, -120, 0, -27830, 180)
    SetChrPos(0x010B, -1860, 0, -29380, 180)
    SetChrPos(0x00F9, -350, 0, -29430, 180)
    SetChrPos(0x0009, -950, 0, -12970, 180)
    OP_E5(0x09, 0x00, 0x00)
    OP_0D()

    ChrTalk(
        0x010B,
        (
            '#0090400391V#216F#5P什…什么…！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010400392V#1020F#5P怎、怎么回事！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0009,
        '青年的声音',
        (
            '#0480400393V#4P呼呼……\n',
            '终于抓到你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x010B, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1F0F',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_1F4D')

    def _loc_1F0F(): pass

    label('loc_1F0F')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1F36',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_1F4D')

    def _loc_1F36(): pass

    label('loc_1F36')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    def _loc_1F4D(): pass

    label('loc_1F4D')

    Sleep(1000)

    @scena.Lambda('lambda_1F58')
    def lambda_1F58():
        OP_6D(-10, 0, -23700, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1F58)

    @scena.Lambda('lambda_1F70')
    def lambda_1F70():
        OP_67(0, 4680, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1F70)

    @scena.Lambda('lambda_1F88')
    def lambda_1F88():
        OP_6B(2880, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_1F88)

    @scena.Lambda('lambda_1F98')
    def lambda_1F98():
        OP_6C(45000, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_1F98)

    @scena.Lambda('lambda_1FA8')
    def lambda_1FA8():
        OP_6E(357, 3000)

        ExitThread()

    DispatchAsync(0x010B, 0x0002, lambda_1FA8)

    WaitForThreadExit(0x00F9, 0x0003)
    ClearChrFlags(0x0009, 0x0080)

    @scena.Lambda('lambda_1FC2')
    def lambda_1FC2():
        OP_8E(0x00FE, -950, 0, -19550, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1FC2)

    @scena.Lambda('lambda_1FDD')
    def lambda_1FDD():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1FDD)

    Sleep(50)

    @scena.Lambda('lambda_1FF0')
    def lambda_1FF0():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1FF0)

    Sleep(80)

    @scena.Lambda('lambda_2003')
    def lambda_2003():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x010B, 0x0001, lambda_2003)

    Sleep(70)

    @scena.Lambda('lambda_2016')
    def lambda_2016():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_2016)

    WaitForThreadExit(0x0009, 0x0001)
    Fade(250)
    OP_22(0x00D8, 0x00, 0x64)
    SetChrChipByIndex(0x0009, 14)
    SetChrSubChip(0x0009, 0)
    OP_0D()
    Sleep(500)

    OP_E5(0x09, 0x00, 0x01)

    ChrTalk(
        0x0101,
        (
            '#0010400394V#1005F#6P基、基尔巴特！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_20A1',
    )

    ChrTalk(
        0x0105,
        (
            '#0060400395V#1164F#4P呀……前辈？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_20A1(): pass

    label('loc_20A1')

    ChrTalk(
        0x0102,
        (
            '#0020400396V#1042F#2P……你在舰内啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0480400397V#1226F#5P哎呀哎呀……\n',
            '听说有人侵入舰艇，\n',
            '我还在想是怎样的蠢货……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480400398V#1221F果然是你们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0090400399V#213F#6P咦……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090400400V……我说这家伙，\n',
            '是你们认识的人吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_236C',
    )

    ChrTalk(
        0x0105,
        (
            '#0060400401V#1163F#2P嗯嗯……\n',
            '是王立学院的前辈……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_228E',
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
            TXT(0x00, '【◇做了王立学院解放任务（８章）】\n'),
            TXT(0x01, '【◇没做王立学院解放任务（８章）】\n'),
            TXT(0x02, '【◇什么也没有变更】\n'),
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
        (0x00000000, 'loc_2282'),
        (0x00000001, 'loc_2288'),
        (-1, 'loc_228E'),
    )

    def _loc_2282(): pass

    label('loc_2282')

    OP_A2(0x202F)

    Jump('loc_228E')

    def _loc_2288(): pass

    label('loc_2288')

    OP_A3(0x202F)

    Jump('loc_228E')

    def _loc_228E(): pass

    label('loc_228E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_2321',
    )

    ChrTalk(
        0x0101,
        (
            '#0010400402V#1007F#5P当他袭击学院的时候，\n',
            '就已经失去前辈的资格啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010400403V#1019F他是渎职市长的前党羽，\n',
            '以前曾经被我们抓住……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2369')

    def _loc_2321(): pass

    label('loc_2321')

    ChrTalk(
        0x0101,
        (
            '#0010400404V#1019F#5P他是渎职市长的前党羽，\n',
            '以前曾经被我们抓住……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2369(): pass

    label('loc_2369')

    Jump('loc_23D4')

    def _loc_236C(): pass

    label('loc_236C')

    ChrTalk(
        0x0101,
        (
            '#0010400405V#1007F#5P嗯，算是吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010400403V#1019F他是渎职市长的前党羽，\n',
            '以前曾经被我们抓住……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_23D4(): pass

    label('loc_23D4')

    ChrTalk(
        0x0102,
        (
            '#0020400407V#1035F#5P后来在政变时趁乱逃走，\n',
            '似乎已经投靠结社了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0090400408V#211F#6P啊哈哈，果然是这样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090400409V#210F是和我们一样\n',
            '被关在雷斯顿要塞地下\n',
            '的市长秘书对吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090400410V不断哭喊着『我是无辜的！』，\n',
            '所以我一直记得很清楚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#0480400411V#1224F#5P什……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2536',
    )

    ChrTalk(
        0x0105,
        (
            '#0060400412V#1164F嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2536(): pass

    label('loc_2536')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2569',
    )

    ChrTalk(
        0x0107,
        (
            '#0070400413V#067F啊，啊哈哈……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2569(): pass

    label('loc_2569')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_25AD',
    )

    ChrTalk(
        0x0104,
        (
            '#0040400414V#031F哈哈哈。\n',
            '冲击性的事实曝光了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_25AD(): pass

    label('loc_25AD')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_25DC',
    )

    ChrTalk(
        0x0103,
        (
            '#0030400415V#025F真丢脸……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_25DC(): pass

    label('loc_25DC')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_260F',
    )

    ChrTalk(
        0x0106,
        (
            '#0050400416V#053F……太没用了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_260F(): pass

    label('loc_260F')

    If(
        (
            (Expr.Eval, "OP_42(0x08)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2681',
    )

    ChrTalk(
        0x0109,
        (
            '#0180400417V#1068F#2P我说小姑娘……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180400418V#1066F这种时候\n',
            '装作互不相识\n',
            '是人之常情吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_26ED')

    def _loc_2681(): pass

    label('loc_2681')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_26ED',
    )

    ChrTalk(
        0x0108,
        (
            '#0080400419V#075F#2P喂喂，小姑娘。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080400420V#070F这种时候装作\n',
            '互不相识是人之常情吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_26ED(): pass

    label('loc_26ED')

    ChrTalk(
        0x0101,
        (
            '#0010400421V#1025F#6P唔、嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010400422V#1016F算了，没必要\n',
            '这么在意了吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010400423V只有积累这样可耻的经验，\n',
            '人才会不断成长……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010400424V#1013F……不过看你现在这副狼狈样，\n',
            '似乎完全都没有累积什么经验嘛……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0102,
        (
            '#0020400425V#1048F#2P……艾丝蒂尔。\n',
            '你也太不给人家留面子了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_9E(0x0009, 0x0000000F, 0x00000000, 0x0000012C, 0x00000FA0)
    Sleep(300)

    ChrTalk(
        0x0009,
        (
            '#0480400426V#1222F#5P你、你、你们，\n',
            '到底要把我戏耍到何种地步……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480400427V#1226F好吧……\n',
            '我再也不会手下留情了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480400428V#1225F我新·基尔巴特的力量，\n',
            '你们就好好见识一下吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x0009, 16)

    ExecExpressionWithValue(
        0x0009,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    ExecExpressionWithValue(
        0x0009,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(240)

    OP_9F(0x000A, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    SetChrPos(0x000A, -990, 800, 49890, 180)
    CreateThread(0x000A, 0x00, 0x00, 0x0015)
    ClearChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000A, 0x0040)

    @scena.Lambda('lambda_2957')
    def lambda_2957():
        OP_69(0x000A, 0x00001388)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2957)

    @scena.Lambda('lambda_2965')
    def lambda_2965():
        OP_67(0, 2000, -10000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2965)

    @scena.Lambda('lambda_297D')
    def lambda_297D():
        OP_6B(3000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_297D)

    @scena.Lambda('lambda_298D')
    def lambda_298D():
        OP_6C(0, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_298D)

    @scena.Lambda('lambda_299D')
    def lambda_299D():
        OP_6E(380, 5000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_299D)

    WaitForThreadExit(0x0101, 0x0000)
    SetChrPos(0x0009, -10, 0, -19000, 180)
    SetChrChipByIndex(0x0009, 14)
    SetChrSubChip(0x0009, 0)
    SetChrPos(0x0101, -7820, 0, -30050, 0)
    Sleep(500)

    OP_22(0x0193, 0x00, 0x64)
    Sleep(900)

    CreateThread(0x0009, 0x03, 0x00, 0x0018)
    Sleep(300)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x000A, 12)

    @scena.Lambda('lambda_2A07')
    def lambda_2A07():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000000C8)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_2A07)

    @scena.Lambda('lambda_2A19')
    def lambda_2A19():
        OP_8F(0x00FE, -2150, 800, -30, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_2A19)

    Sleep(1200)

    Fade(500)
    OP_69(0x000A, 0x00000000)
    OP_6A(0x000A)
    OP_67(0, 2500, -10000, 0)
    OP_6B(2300, 0)
    OP_6C(24000, 0)
    OP_6E(380, 0)

    @scena.Lambda('lambda_2A74')
    def lambda_2A74():
        OP_67(0, 3000, -10000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2A74)

    @scena.Lambda('lambda_2A8C')
    def lambda_2A8C():
        OP_6B(2500, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2A8C)

    @scena.Lambda('lambda_2A9C')
    def lambda_2A9C():
        OP_6C(45000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2A9C)

    WaitForThreadExit(0x000A, 0x0001)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0101, 0x02)
    TerminateThread(0x0101, 0x03)
    OP_6A(0x00FF)
    TerminateThread(0x0009, 0x03)
    OP_23(0x013F)
    OP_22(0x023B, 0x00, 0x64)

    @scena.Lambda('lambda_2ACC')
    def lambda_2ACC():
        OP_96(0x00FE, 0xFFFFF79A, 0x00000FA0, 0xFFFFD9A4, 0x00001388, 0x00001F40)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_2ACC)

    Sleep(100)

    Fade(1000)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_6D(-2150, 800, -19000, 0)
    OP_67(0, 3590, -10000, 0)
    OP_6B(2060, 0)
    OP_6C(45000, 0)
    OP_6E(380, 0)
    WaitForThreadExit(0x000A, 0x0001)
    OP_22(0x00C8, 0x00, 0x64)
    OP_22(0x023B, 0x00, 0x64)

    @scena.Lambda('lambda_2B49')
    def lambda_2B49():
        OP_96(0x00FE, 0xFFFFF79A, 0x00000320, 0xFFFFB5C8, 0x000007D0, 0x00001F40)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_2B49)

    WaitForThreadExit(0x000A, 0x0001)
    SetChrChipByIndex(0x000A, 11)
    TerminateThread(0x000A, 0x00)
    OP_22(0x00F5, 0x00, 0x64)
    OP_7C(0x00000000, 0x000001F4, 0x00001388, 0x000001F4)
    Sleep(500)

    CreateThread(0x000A, 0x00, 0x00, 0x0002)
    OP_22(0x0193, 0x00, 0x64)
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010400429V#1020F#1P！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(500)
    OP_6D(400, 0, -22850, 0)
    OP_67(0, 4840, -10000, 0)
    OP_6B(2760, 0)
    OP_6C(44000, 0)
    OP_6E(380, 0)
    SetChrPos(0x0101, -1540, 0, -27810, 0)
    OP_0D()
    Sleep(500)

    Fade(250)
    OP_22(0x00D5, 0x00, 0x64)
    SetChrChipByIndex(0x0101, 19)
    SetChrSubChip(0x0101, 0)
    SetChrChipByIndex(0x0102, 20)
    SetChrSubChip(0x0102, 0)
    Sleep(100)

    OP_22(0x00D8, 0x00, 0x64)
    SetChrChipByIndex(0x010B, 21)
    SetChrSubChip(0x010B, 0)
    SetChrChipByIndex(0x00F9, 22)
    SetChrSubChip(0x00F9, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x010B,
        (
            '#0090400430V#216F#6P什、什什什什！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010400431V#1020F#6P机、机械装置的狮子！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020400432V#1042F#2P『十三工房』的新型吗……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0480400433V#1221F#5P哈哈哈，这是狮子型人形兵器，\n',
            '『暴动钢臂』！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480400434V面对它惊人的性能，\n',
            '你们就尽情地颤抖吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_22(0x0193, 0x00, 0x64)
    Sleep(1200)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_2D85')
    def lambda_2D85():
        OP_6D(-210, 0, -25930, 700)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2D85)

    @scena.Lambda('lambda_2D9D')
    def lambda_2D9D():
        OP_67(0, 6180, -10000, 700)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2D9D)

    @scena.Lambda('lambda_2DB5')
    def lambda_2DB5():
        OP_6B(2020, 700)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2DB5)

    SetChrFlags(0x000A, 0x0020)
    SetChrChipByIndex(0x000A, 12)
    CreateThread(0x000A, 0x00, 0x00, 0x0015)
    CreateThread(0x000A, 0x03, 0x00, 0x0019)
    OP_8F(0x000A, -1020, 800, -22630, 10000, 0x00)
    OP_22(0x023B, 0x00, 0x64)

    @scena.Lambda('lambda_2DF6')
    def lambda_2DF6():
        OP_96(0x00FE, 0xFFFFFCA4, 0x00000000, 0xFFFF92A0, 0x000005DC, 0x00001770)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_2DF6)

    TerminateThread(0x000A, 0x00)
    SetChrChipByIndex(0x000A, 18)

    @scena.Lambda('lambda_2E1D')
    def lambda_2E1D():
        OP_99(0x00FE, 0x00, 0x05, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_2E1D)

    WaitForThreadExit(0x0101, 0x0001)
    TerminateThread(0x000A, 0xFF)
    Battle(0x00000434, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_2E49'),
        (-1, 'loc_2E4E'),
    )

    def _loc_2E49(): pass

    label('loc_2E49')

    OP_B4(0x00)

    Jump('loc_2E4E')

    def _loc_2E4E(): pass

    label('loc_2E4E')

    Return()

# id: 0x0014 offset: 0x2E4F
@scena.Code('func_14_2E4F')
def func_14_2E4F():
    UnlockAchievement(0x0B, 0x00, 0x00, 0x00)
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    TerminateThread(0x000A, 0x00)
    TerminateThread(0x000A, 0x01)
    TerminateThread(0x000A, 0x02)
    SetChrFlags(0x000A, 0x0080)
    OP_6D(-480, 0, -22740, 0)
    OP_67(0, 5070, -10000, 0)
    OP_6B(3480, 0)
    OP_6C(44000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, -2170, 0, -25140, 0)
    SetChrPos(0x0102, -910, 0, -25200, 0)
    SetChrPos(0x010B, -2630, 0, -26440, 0)
    SetChrPos(0x00F9, -1200, 0, -26530, 0)
    ClearChrFlags(0x0020, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x0009, -1620, 0, -22000, 180)
    SetChrChipByIndex(0x0009, 15)
    SetChrSubChip(0x0009, 3)
    SetChrChipByIndex(0x0101, 65535)
    SetChrChipByIndex(0x0102, 65535)
    SetChrChipByIndex(0x010B, 65535)
    SetChrChipByIndex(0x00F9, 65535)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#0480400435V#1224F#5P不、不可能……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480400436V我居然……\n',
            '我新·基尔巴特居然会……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010400437V#1015F#6P那、那个～打扰一下？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010400438V那东西…确实比以前的人形兵器\n',
            '要强上许多……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0090400439V#413F#6P不过，这并不代表\n',
            '你本身变强了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0480400440V#1224F#5P咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_30AE',
    )

    ChrTalk(
        0x0105,
        (
            '#0060400441V#1165F确实啊，加个『新』字，\n',
            '结果一点变化都没有……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_336C')

    def _loc_30AE(): pass

    label('loc_30AE')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3107',
    )

    ChrTalk(
        0x0107,
        (
            '#0070400442V#067F确、确实，只是加个『新』字，\n',
            '但一点进步都没有……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_336C')

    def _loc_3107(): pass

    label('loc_3107')

    If(
        (
            (Expr.Eval, "OP_42(0x08)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3191',
    )

    ChrTalk(
        0x0109,
        (
            '#0180400443V#1068F确实啊，只是加个『新』字而已，\n',
            '根本就没有一点进步嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180400444V#1060F这就是所谓的虚张声势吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_336C')

    def _loc_3191(): pass

    label('loc_3191')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_320D',
    )

    ChrTalk(
        0x0103,
        (
            '#0030400445V#025F确实，加个『新』字，\n',
            '结果一点进步都没有。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030400446V#524F男人的虚荣心真是可悲啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_336C')

    def _loc_320D(): pass

    label('loc_320D')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_327C',
    )

    ChrTalk(
        0x0104,
        (
            '#0040400447V#035F呼，这么没用还敢加个『新』字。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040400448V#037F这就是所谓的虚荣心吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_336C')

    def _loc_327C(): pass

    label('loc_327C')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_32E9',
    )

    ChrTalk(
        0x0106,
        (
            '#0050400449V#551F切……\n',
            '什么『新』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050400450V#555F是男人就靠\n',
            '自己的双手来战斗吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_336C')

    def _loc_32E9(): pass

    label('loc_32E9')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_336C',
    )

    ChrTalk(
        0x0108,
        (
            '#0080400451V#074F唔，确实，虽然加了个『新』字，\n',
            '但一点长进都没有啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080400452V#070F这就是年轻人的虚荣心吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_336C(): pass

    label('loc_336C')

    ChrTalk(
        0x0009,
        (
            '#0480400453V#1228F#5P……（语塞）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(500)
    OP_22(0x020C, 0x00, 0x64)
    SetChrPos(0x0009, -1950, 0, -22900, 180)
    ClearChrFlags(0x0009, 0x0001)
    SetChrFlags(0x0009, 0x0002)
    SetChrChipByIndex(0x0009, 13)
    SetChrSubChip(0x0009, 5)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010400454V#1004F#6P啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0090400455V#213F#6P咦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3439',
    )

    ChrTalk(
        0x0105,
        (
            '#0060400412V#1164F嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3553')

    def _loc_3439(): pass

    label('loc_3439')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_346B',
    )

    ChrTalk(
        0x0107,
        (
            '#0070290840V#065F啊哇哇……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3553')

    def _loc_346B(): pass

    label('loc_346B')

    If(
        (
            (Expr.Eval, "OP_42(0x08)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_349C',
    )

    ChrTalk(
        0x0109,
        (
            '#0180400458V#1064F哎呀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3553')

    def _loc_349C(): pass

    label('loc_349C')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_34CA',
    )

    ChrTalk(
        0x0103,
        (
            '#0030400459V#023F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3553')

    def _loc_34CA(): pass

    label('loc_34CA')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_34FA',
    )

    ChrTalk(
        0x0104,
        (
            '#0040400460V#033F哎呀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3553')

    def _loc_34FA(): pass

    label('loc_34FA')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3528',
    )

    ChrTalk(
        0x0106,
        (
            '#0050400461V#052F喔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3553')

    def _loc_3528(): pass

    label('loc_3528')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3553',
    )

    ChrTalk(
        0x0108,
        (
            '#0080400462V#073F喂……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3553(): pass

    label('loc_3553')

    OP_62(0x0101, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(50)

    OP_62(0x0102, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(50)

    OP_62(0x010B, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_35BA',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x18, 0x1B, 0x000000FA, 0x00)

    Jump('loc_35EE')

    def _loc_35BA(): pass

    label('loc_35BA')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_35DC',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x18, 0x1B, 0x000000FA, 0x00)

    Jump('loc_35EE')

    def _loc_35DC(): pass

    label('loc_35DC')

    OP_62(0x00F9, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)

    def _loc_35EE(): pass

    label('loc_35EE')

    Sleep(1500)

    OP_63(0x0101)
    OP_63(0x0102)
    OP_63(0x010B)
    OP_63(0x00F9)
    Sleep(500)

    @scena.Lambda('lambda_360A')
    def lambda_360A():
        OP_6D(-1450, 0, -25300, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_360A)

    @scena.Lambda('lambda_3622')
    def lambda_3622():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3622)

    Sleep(50)

    @scena.Lambda('lambda_3635')
    def lambda_3635():
        OP_8C(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_3635)

    Sleep(50)

    @scena.Lambda('lambda_3648')
    def lambda_3648():
        OP_8C(0x00FE, 45, 400)

        ExitThread()

    DispatchAsync(0x010B, 0x0002, lambda_3648)

    Sleep(50)

    @scena.Lambda('lambda_365B')
    def lambda_365B():
        OP_8C(0x00FE, 225, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_365B)

    WaitForThreadExit(0x0101, 0x0001)
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x0101,
        (
            '#0010400463V#1016F#5P好，好～了。\n',
            '赶快返回牢房吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_36E7',
    )

    ChrTalk(
        0x0105,
        (
            '#0060400464V#1165F是、是啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3817')

    def _loc_36E7(): pass

    label('loc_36E7')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3719',
    )

    ChrTalk(
        0x0107,
        (
            '#0070400465V#067F是，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3817')

    def _loc_3719(): pass

    label('loc_3719')

    If(
        (
            (Expr.Eval, "OP_42(0x08)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3750',
    )

    ChrTalk(
        0x0109,
        (
            '#0180400466V#1066F啊哈哈，是呀～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3817')

    def _loc_3750(): pass

    label('loc_3750')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3784',
    )

    ChrTalk(
        0x0103,
        (
            '#0030400467V#021F是，是啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3817')

    def _loc_3784(): pass

    label('loc_3784')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_37B6',
    )

    ChrTalk(
        0x0104,
        (
            '#0040400468V#031F呼，赞成。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3817')

    def _loc_37B6(): pass

    label('loc_37B6')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_37E8',
    )

    ChrTalk(
        0x0106,
        (
            '#0050400469V#551F……是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3817')

    def _loc_37E8(): pass

    label('loc_37E8')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3817',
    )

    ChrTalk(
        0x0108,
        (
            '#0080400470V#070F嗯，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3817(): pass

    label('loc_3817')

    ChrTalk(
        0x010B,
        (
            '#0090400471V#211F#6P嗯嗯。\n',
            '得赶快去救大哥他们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020400472V#1052F#5P（真是个可怜的家伙呢……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_6D(-1410, 0, -25050, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0000, -1410, 0, -25050, 0)
    SetChrPos(0x0001, -1410, 0, -25050, 0)
    SetChrPos(0x0002, -1410, 0, -25050, 0)
    SetChrPos(0x0003, -1410, 0, -25050, 0)
    Sleep(500)

    FadeIn(1000, 0)
    OP_71(0x0017, 0x0010)
    OP_6F(0x0002, 0)
    OP_6F(0x0004, 0)
    OP_6F(0x0005, 0)
    OP_BE(0x02, 0x01, 0x0000, 0x0000, 0x0000, 0x02, 0, 0, 0, 0, 0, 0)
    OP_BE(0x04, 0x01, 0x0000, 0x0000, 0x0000, 0x02, 0, 0, 0, 0, 0, 0)
    OP_BE(0x05, 0x01, 0x0000, 0x0000, 0x0000, 0x02, 0, 0, 0, 0, 0, 0)
    OP_A2(0x2227)
    EventEnd(0x00)

    Return()

# id: 0x0015 offset: 0x39A1
@scena.Code('func_15_39A1')
def func_15_39A1():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_39B6',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000BB8)

    Jump('func_15_39A1')

    def _loc_39B6(): pass

    label('loc_39B6')

    Return()

# id: 0x0016 offset: 0x39B7
@scena.Code('func_16_39B7')
def func_16_39B7():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_39CC',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000007D0)

    Jump('func_16_39B7')

    def _loc_39CC(): pass

    label('loc_39CC')

    Return()

# id: 0x0017 offset: 0x39CD
@scena.Code('func_17_39CD')
def func_17_39CD():
    SetChrChipByIndex(0x00FE, 18)
    OP_22(0x0195, 0x00, 0x64)
    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)
    SetChrChipByIndex(0x00FE, 11)
    SetChrSubChip(0x00FE, 0)

    Return()

# id: 0x0018 offset: 0x39EB
@scena.Code('func_18_39EB')
def func_18_39EB():
    OP_22(0x013F, 0x00, 0x46)
    Sleep(400)

    OP_22(0x013F, 0x00, 0x50)
    Sleep(400)

    OP_22(0x013F, 0x00, 0x5A)
    Sleep(400)

    def _loc_3A09(): pass

    label('loc_3A09')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3A1F',
    )

    OP_22(0x013F, 0x00, 0x64)
    Sleep(400)

    Jump('loc_3A09')

    def _loc_3A1F(): pass

    label('loc_3A1F')

    Return()

# id: 0x0019 offset: 0x3A20
@scena.Code('func_19_3A20')
def func_19_3A20():
    OP_22(0x013F, 0x00, 0x64)
    Sleep(400)

    OP_22(0x013F, 0x00, 0x64)
    Sleep(400)

    Return()

# id: 0x001A offset: 0x3A35
@scena.Code('func_1A_3A35')
def func_1A_3A35():
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
        (0x00000000, 'loc_3AAF'),
        (0x00000001, 'loc_3AB5'),
        (-1, 'loc_3ABB'),
    )

    def _loc_3AAF(): pass

    label('loc_3AAF')

    OP_A2(0x1200)

    Jump('loc_3ABB')

    def _loc_3AB5(): pass

    label('loc_3AB5')

    OP_A2(0x1201)

    Jump('loc_3ABB')

    def _loc_3ABB(): pass

    label('loc_3ABB')

    Return()

# id: 0x001B offset: 0x3ABC
@scena.Code('func_1B_3ABC')
def func_1B_3ABC():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3B0D',
    )

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '导力好像停止了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Jump('loc_3CC8')

    def _loc_3B0D(): pass

    label('loc_3B0D')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '这是一台可供旅行者回复体力的导力器装置。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
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

    Menu(
        0,
        10,
        32,
        1,
        (
            TXT(0x00, '在这里休息\n'),
            TXT(0x01, '离开\n'),
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

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3CAD',
    )

    FadeIn(100, 0)
    Sleep(500)

    OP_26(13)
    OP_82(0x00, 0x02)
    PlayEffect(0x00, 0x00, 0x00FF, 3580, 1000, 79630, 0, 0, 0, 700, 700, 700, 0x00FF, 0, 0, 0, 0)
    OP_6F(0x0028, 0)
    OP_70(0x0028, 0x00000032)
    OP_73(0x0028)
    OP_20(0x00000BB8)
    OP_22(0x000C, 0x00, 0x64)
    OP_82(0x00, 0x02)
    LoadEffect(0x01, 'map\\\\mp027_01.eff')
    PlayEffect(0x01, 0x01, 0x00FF, 3580, 1000, 79630, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    FadeOut(1000, 0, -1)
    Sleep(700)

    OP_22(0x000D, 0x00, 0x64)
    OP_0D()
    SetChrStatus(0x00FF, 0xFE, 0)
    OP_69(0x0000, 0x00000000)
    OP_30(0x01)
    Sleep(3500)

    OP_82(0x01, 0x02)
    PlayEffect(0x00, 0x00, 0x00FF, 3580, 1000, 79630, 0, 0, 0, 1300, 1300, 1300, 0x00FF, 0, 0, 0, 0)
    OP_6F(0x0028, 0)
    OP_1E()
    FadeIn(1000, 0)
    OP_56(0x00)
    TalkEnd(0x00FF)

    Return()

    def _loc_3CAD(): pass

    label('loc_3CAD')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3CC7',
    )

    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Return()

    def _loc_3CC7(): pass

    label('loc_3CC7')

    Return()

    def _loc_3CC8(): pass

    label('loc_3CC8')

    Return()

# id: 0x001C offset: 0x3CC9
@scena.Code('func_1C_3CC9')
def func_1C_3CC9():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x9),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_3DFA',
    )

    OP_72(0x0000, 0x0020)
    OP_72(0x0000, 0x0008)
    OP_6F(0x0000, 0)
    OP_71(0x0000, 0x0002)
    OP_72(0x0001, 0x0020)
    OP_72(0x0001, 0x0008)
    OP_6F(0x0001, 0)
    OP_71(0x0001, 0x0002)
    OP_72(0x0002, 0x0020)
    OP_72(0x0002, 0x0008)
    OP_6F(0x0002, 0)
    OP_71(0x0002, 0x0002)
    OP_72(0x0003, 0x0020)
    OP_72(0x0003, 0x0008)
    OP_6F(0x0003, 0)
    OP_71(0x0003, 0x0002)
    OP_72(0x0004, 0x0020)
    OP_72(0x0004, 0x0008)
    OP_6F(0x0004, 0)
    OP_71(0x0004, 0x0002)
    OP_72(0x0005, 0x0020)
    OP_72(0x0005, 0x0008)
    OP_6F(0x0005, 0)
    OP_71(0x0005, 0x0002)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0444, 5, 0x2225)),
            (Expr.TestScenaFlags, ScenaFlag(0x0444, 7, 0x2227)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3DF9',
    )

    OP_72(0x0017, 0x0010)
    OP_6F(0x0002, 100)
    OP_6F(0x0004, 100)
    OP_6F(0x0005, 100)
    OP_72(0x0002, 0x0002)
    OP_72(0x0004, 0x0002)
    OP_72(0x0005, 0x0002)
    OP_BE(0x02, 0x01, 0x0002, 0x0064, 0x0000, 0x02, 80500, -1000, -37650, 84000, 2000, -40350)
    OP_BE(0x04, 0x01, 0x0002, 0x0064, 0x0000, 0x02, -128000, -1000, 7600, -123800, 2000, 10360)
    OP_BE(0x05, 0x01, 0x0002, 0x0064, 0x0000, 0x02, -88290, 0, 10370, -85540, 2000, 7640)
    SetChrFlags(0x0017, 0x0080)

    def _loc_3DF9(): pass

    label('loc_3DF9')

    Return()

    def _loc_3DFA(): pass

    label('loc_3DFA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0392, 4, 0x1C94)),
            Expr.Return,
        ),
        'loc_3E2A',
    )

    OP_6F(0x0000, 100)
    OP_BE(0x00, 0x01, 0x0002, 0x0064, 0x0000, 0x02, -5310, -1000, 30410, 3470, 2000, 27560)

    def _loc_3E2A(): pass

    label('loc_3E2A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0392, 5, 0x1C95)),
            Expr.Return,
        ),
        'loc_3E5A',
    )

    OP_6F(0x0001, 100)
    OP_BE(0x01, 0x01, 0x0002, 0x0064, 0x0000, 0x02, -5210, -1000, -36500, 3470, 2000, -33500)

    def _loc_3E5A(): pass

    label('loc_3E5A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0392, 6, 0x1C96)),
            Expr.Return,
        ),
        'loc_3E8A',
    )

    OP_6F(0x0002, 100)
    OP_BE(0x02, 0x01, 0x0002, 0x0064, 0x0000, 0x02, 80500, -1000, -37650, 84000, 2000, -40350)

    def _loc_3E8A(): pass

    label('loc_3E8A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0392, 7, 0x1C97)),
            Expr.Return,
        ),
        'loc_3EBA',
    )

    OP_6F(0x0003, 100)
    OP_BE(0x03, 0x01, 0x0002, 0x0064, 0x0000, 0x02, 80690, -1000, 8260, 83470, 2000, 5400)

    def _loc_3EBA(): pass

    label('loc_3EBA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0393, 0, 0x1C98)),
            Expr.Return,
        ),
        'loc_3EEA',
    )

    OP_6F(0x0004, 100)
    OP_BE(0x04, 0x01, 0x0002, 0x0064, 0x0000, 0x02, -128000, -1000, 7600, -123800, 2000, 10360)

    def _loc_3EEA(): pass

    label('loc_3EEA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0393, 1, 0x1C99)),
            Expr.Return,
        ),
        'loc_3F1A',
    )

    OP_6F(0x0005, 100)
    OP_BE(0x05, 0x01, 0x0002, 0x0064, 0x0000, 0x02, -88290, 0, 10370, -85540, 2000, 7640)

    def _loc_3F1A(): pass

    label('loc_3F1A')

    Return()

# id: 0x001D offset: 0x3F1B
@scena.Code('func_1D_3F1B')
def func_1D_3F1B():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x9),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_3F28',
    )

    Return()

    def _loc_3F28(): pass

    label('loc_3F28')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0392, 4, 0x1C94)),
            Expr.Return,
        ),
        'loc_3F30',
    )

    Return()

    def _loc_3F30(): pass

    label('loc_3F30')

    EventBegin(0x02)
    OP_22(0x006B, 0x00, 0x64)
    OP_6F(0x0000, 0)
    OP_70(0x0000, 0x00000064)
    Sleep(1500)

    OP_22(0x009D, 0x00, 0x64)
    OP_73(0x0000)
    OP_A2(0x1C94)
    Call(0, 0x001C)
    EventEnd(0x03)

    Return()

# id: 0x001E offset: 0x3F5C
@scena.Code('func_1E_3F5C')
def func_1E_3F5C():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x9),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_3F69',
    )

    Return()

    def _loc_3F69(): pass

    label('loc_3F69')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0392, 5, 0x1C95)),
            Expr.Return,
        ),
        'loc_3F71',
    )

    Return()

    def _loc_3F71(): pass

    label('loc_3F71')

    EventBegin(0x02)
    OP_22(0x006B, 0x00, 0x64)
    OP_6F(0x0001, 0)
    OP_70(0x0001, 0x00000064)
    Sleep(1500)

    OP_22(0x009D, 0x00, 0x64)
    OP_73(0x0001)
    OP_A2(0x1C95)
    Call(0, 0x001C)
    EventEnd(0x03)

    Return()

# id: 0x001F offset: 0x3F9D
@scena.Code('func_1F_3F9D')
def func_1F_3F9D():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x9),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_3FAA',
    )

    Return()

    def _loc_3FAA(): pass

    label('loc_3FAA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0392, 6, 0x1C96)),
            Expr.Return,
        ),
        'loc_3FB2',
    )

    Return()

    def _loc_3FB2(): pass

    label('loc_3FB2')

    EventBegin(0x02)
    OP_22(0x006B, 0x00, 0x64)
    OP_6F(0x0002, 0)
    OP_70(0x0002, 0x00000064)
    Sleep(1500)

    OP_22(0x009D, 0x00, 0x64)
    OP_73(0x0002)
    OP_A2(0x1C96)
    Call(0, 0x001C)
    EventEnd(0x03)

    Return()

# id: 0x0020 offset: 0x3FDE
@scena.Code('func_20_3FDE')
def func_20_3FDE():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x9),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_3FEB',
    )

    Return()

    def _loc_3FEB(): pass

    label('loc_3FEB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0392, 7, 0x1C97)),
            Expr.Return,
        ),
        'loc_3FF3',
    )

    Return()

    def _loc_3FF3(): pass

    label('loc_3FF3')

    EventBegin(0x02)
    OP_22(0x006B, 0x00, 0x64)
    OP_6F(0x0003, 0)
    OP_70(0x0003, 0x00000064)
    Sleep(1500)

    OP_22(0x009D, 0x00, 0x64)
    OP_73(0x0003)
    OP_A2(0x1C97)
    Call(0, 0x001C)
    EventEnd(0x03)

    Return()

# id: 0x0021 offset: 0x401F
@scena.Code('func_21_401F')
def func_21_401F():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x9),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_402C',
    )

    Return()

    def _loc_402C(): pass

    label('loc_402C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0393, 0, 0x1C98)),
            Expr.Return,
        ),
        'loc_4034',
    )

    Return()

    def _loc_4034(): pass

    label('loc_4034')

    EventBegin(0x02)
    OP_22(0x006B, 0x00, 0x64)
    OP_6F(0x0004, 0)
    OP_70(0x0004, 0x00000064)
    Sleep(1500)

    OP_22(0x009D, 0x00, 0x64)
    OP_73(0x0004)
    OP_A2(0x1C98)
    Call(0, 0x001C)
    EventEnd(0x03)

    Return()

# id: 0x0022 offset: 0x4060
@scena.Code('func_22_4060')
def func_22_4060():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x9),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_406D',
    )

    Return()

    def _loc_406D(): pass

    label('loc_406D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0393, 1, 0x1C99)),
            Expr.Return,
        ),
        'loc_4075',
    )

    Return()

    def _loc_4075(): pass

    label('loc_4075')

    EventBegin(0x02)
    OP_22(0x006B, 0x00, 0x64)
    OP_6F(0x0005, 0)
    OP_70(0x0005, 0x00000064)
    Sleep(1500)

    OP_22(0x009D, 0x00, 0x64)
    OP_73(0x0005)
    OP_A2(0x1C99)
    Call(0, 0x001C)
    EventEnd(0x03)

    Return()

# id: 0x0023 offset: 0x40A1
@scena.Code('func_23_40A1')
def func_23_40A1():
    FadeOut(0, 0, -1)
    OP_6D(-27650, 0, -3680, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(200)

    FadeIn(0, 0)
    OP_0D()

    OP_C9(
        0x00,
        (
            0x0000,
            0x0001,
            0x000A,
            0x00FF,
        ),
        (
            0x0005,
            0x0002,
            0x0004,
            0x0003,
            0x0006,
            0x0007,
            0x0008,
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

    Sleep(100)

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0x00000000)

    Return()

# id: 0x0024 offset: 0x4132
@scena.Code('func_24_4132')
def func_24_4132():
    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_AD(0x00240131, 0x0000, 0x0000, 0x000001F4)
    Sleep(500)

    OP_56(0x03)
    OP_AE(0x000001F4)
    TalkEnd(0x00FF)

    Return()

# id: 0x0025 offset: 0x4158
@scena.Code('func_25_4158')
def func_25_4158():
    OP_D2(0x002703A8, 0x002703B2, 0x0E)
    OP_D2(0x002703AE, 0x002703B8, 0x10)
    OP_D2(0x00290216, 0x0029021A, 0x12)
    OP_D2(0x00270110, 0x00270120, 0x13)
    OP_D2(0x00270130, 0x00270140, 0x14)
    OP_D2(0x000702B4, 0x000702BB, 0x15)

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_41B9'),
        (0x00000003, 'loc_41C6'),
        (0x00000004, 'loc_41D3'),
        (0x00000005, 'loc_41E0'),
        (0x00000006, 'loc_41ED'),
        (0x00000007, 'loc_41FA'),
        (0x00000008, 'loc_4207'),
        (-1, 'loc_4214'),
    )

    def _loc_41B9(): pass

    label('loc_41B9')

    OP_D2(0x000701D0, 0x000701DC, 0x16)

    Jump('loc_4214')

    def _loc_41C6(): pass

    label('loc_41C6')

    OP_D2(0x000701E8, 0x000701F4, 0x16)

    Jump('loc_4214')

    def _loc_41D3(): pass

    label('loc_41D3')

    OP_D2(0x0027036E, 0x0027037B, 0x16)

    Jump('loc_4214')

    def _loc_41E0(): pass

    label('loc_41E0')

    OP_D2(0x00070218, 0x00070224, 0x16)

    Jump('loc_4214')

    def _loc_41ED(): pass

    label('loc_41ED')

    OP_D2(0x00070230, 0x0007023C, 0x16)

    Jump('loc_4214')

    def _loc_41FA(): pass

    label('loc_41FA')

    OP_D2(0x00070248, 0x00070254, 0x16)

    Jump('loc_4214')

    def _loc_4207(): pass

    label('loc_4207')

    OP_D2(0x00270176, 0x00270183, 0x16)

    Jump('loc_4214')

    def _loc_4214(): pass

    label('loc_4214')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
