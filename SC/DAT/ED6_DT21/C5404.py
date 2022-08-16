import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C5404_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C5404   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'C5404.x'
    header.mapIndex       = 1
    header.bgm            = 28
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
        ('ED6_DT29/CH12570._CH', 'ED6_DT29/CH12570P._CP'),
        ('ED6_DT29/CH12571._CH', 'ED6_DT29/CH12571P._CP'),
        ('ED6_DT29/CH12350._CH', 'ED6_DT29/CH12350P._CP'),
        ('ED6_DT29/CH12351._CH', 'ED6_DT29/CH12351P._CP'),
        ('ED6_DT29/CH12580._CH', 'ED6_DT29/CH12580P._CP'),
        ('ED6_DT29/CH12581._CH', 'ED6_DT29/CH12581P._CP'),
        ('ED6_DT29/CH12310._CH', 'ED6_DT29/CH12310P._CP'),
        ('ED6_DT29/CH12310._CH', 'ED6_DT29/CH12310P._CP'),
        ('ED6_DT29/CH12320._CH', 'ED6_DT29/CH12320P._CP'),
        ('ED6_DT29/CH12321._CH', 'ED6_DT29/CH12321P._CP'),
    ]

# id: 0x10001 offset: 0xFA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '',
            x                   = 73000,
            z                   = 2000,
            y                   = -98360,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x11A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '亡命守护者',
            x           = -1000,
            z           = 0,
            y           = 78200,
            word_0C     = 0x0000,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0425,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '目标探索者',
            x           = -13970,
            z           = 0,
            y           = 79920,
            word_0C     = 0x0000,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0428,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '目标探索者',
            x           = 12740,
            z           = 0,
            y           = 79820,
            word_0C     = 0x0000,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0428,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '哨兵570（蓝）',
            x           = 69850,
            z           = 1000,
            y           = 58110,
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
            name        = '目标探索者',
            x           = 40980,
            z           = 0,
            y           = 3640,
            word_0C     = 0x0000,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0428,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '目标探索者',
            x           = 124900,
            z           = 0,
            y           = -50190,
            word_0C     = 0x0000,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0428,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '哨兵235（红）',
            x           = -62040,
            z           = 1000,
            y           = -113250,
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
            name        = '亡命守护者',
            x           = -1140,
            z           = 0,
            y           = -75510,
            word_0C     = 0x0000,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0425,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '据点武装者',
            x           = -980,
            z           = 0,
            y           = -7880,
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
            name        = '据点武装者',
            x           = -1440,
            z           = 0,
            y           = -31230,
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
            name        = '据点武装者',
            x           = -900,
            z           = 0,
            y           = -49020,
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
            name        = '亡命守护者',
            x           = -1000,
            z           = 0,
            y           = 78200,
            word_0C     = 0x0000,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x042E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '目标探索者',
            x           = -13970,
            z           = 0,
            y           = 79920,
            word_0C     = 0x0000,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0431,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '目标探索者',
            x           = 12740,
            z           = 0,
            y           = 79820,
            word_0C     = 0x0000,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0431,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '哨兵570（蓝）',
            x           = 69850,
            z           = 1000,
            y           = 58110,
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
            name        = '目标探索者',
            x           = 40980,
            z           = 0,
            y           = 3640,
            word_0C     = 0x0000,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0431,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '目标探索者',
            x           = 124900,
            z           = 0,
            y           = -50190,
            word_0C     = 0x0000,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0431,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '哨兵235（红）',
            x           = -62040,
            z           = 1000,
            y           = -113250,
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
            name        = '亡命守护者',
            x           = -1140,
            z           = 0,
            y           = -75510,
            word_0C     = 0x0000,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x042E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '据点武装者',
            x           = -770,
            z           = 0,
            y           = -80,
            word_0C     = 0x0000,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x042F,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '据点武装者',
            x           = -4030,
            z           = 0,
            y           = -25880,
            word_0C     = 0x0000,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x042F,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '据点武装者',
            x           = -640,
            z           = 0,
            y           = -43460,
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

# id: 0x10003 offset: 0x382
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -1030,
            y           = -1000,
            z           = 133840,
            range       = 3000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000010,
        ),
        ScenaEventData(
            x           = 1980,
            y           = -1000,
            z           = -119660,
            range       = 3000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000011,
        ),
        ScenaEventData(
            x           = -28000,
            y           = -3000,
            z           = 76300,
            range       = -26800,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00014758,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000018,
        ),
        ScenaEventData(
            x           = -6500,
            y           = 0,
            z           = -2500,
            range       = 5500,
            dword_10    = 0x000007D0,
            dword_14    = 0x000009C4,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000001A,
        ),
        ScenaEventData(
            x           = -6500,
            y           = 0,
            z           = -60500,
            range       = 5500,
            dword_10    = 0x000007D0,
            dword_14    = 0xFFFF2734,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000001B,
        ),
        ScenaEventData(
            x           = 38000,
            y           = 0,
            z           = -6000,
            range       = 45000,
            dword_10    = 0x000007D0,
            dword_14    = 0xFFFFFA24,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000001C,
        ),
        ScenaEventData(
            x           = 131500,
            y           = 0,
            z           = -192000,
            range       = 136500,
            dword_10    = 0x000007D0,
            dword_14    = 0xFFFD3140,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000001D,
        ),
    )

# id: 0x10004 offset: 0x462
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 75730,
            triggerZ            = 0,
            triggerY            = -20940,
            triggerRange        = 1000,
            actorX              = 75070,
            actorZ              = 0,
            actorY              = -20990,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -1000,
            triggerZ            = 0,
            triggerY            = 134330,
            triggerRange        = 1000,
            actorX              = -1000,
            actorZ              = 1000,
            actorY              = 134330,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0017,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 67030,
            triggerZ            = 0,
            triggerY            = -90240,
            triggerRange        = 1000,
            actorX              = 66960,
            actorZ              = 0,
            actorY              = -89540,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 69990,
            triggerZ            = 0,
            triggerY            = -90250,
            triggerRange        = 1000,
            actorX              = 70020,
            actorZ              = 0,
            actorY              = -89630,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 73000,
            triggerZ            = 0,
            triggerY            = -90250,
            triggerRange        = 1000,
            actorX              = 72970,
            actorZ              = 0,
            actorY              = -89680,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 72970,
            triggerZ            = 0,
            triggerY            = -97700,
            triggerRange        = 1000,
            actorX              = 73000,
            actorZ              = 0,
            actorY              = -98360,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 69940,
            triggerZ            = 0,
            triggerY            = -97700,
            triggerRange        = 1000,
            actorX              = 69980,
            actorZ              = 0,
            actorY              = -98310,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 66990,
            triggerZ            = 0,
            triggerY            = -97700,
            triggerRange        = 1000,
            actorX              = 67020,
            actorZ              = 0,
            actorY              = -98360,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0009,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 68510,
            triggerZ            = 0,
            triggerY            = -132200,
            triggerRange        = 1000,
            actorX              = 68480,
            actorZ              = 0,
            actorY              = -131590,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000A,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 72000,
            triggerZ            = 0,
            triggerY            = -132200,
            triggerRange        = 1000,
            actorX              = 71970,
            actorZ              = 0,
            actorY              = -131630,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000B,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 75450,
            triggerZ            = 0,
            triggerY            = -132200,
            triggerRange        = 1000,
            actorX              = 75410,
            actorZ              = 0,
            actorY              = -131590,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000C,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 75480,
            triggerZ            = 0,
            triggerY            = -139800,
            triggerRange        = 1000,
            actorX              = 75510,
            actorZ              = 0,
            actorY              = -140420,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000D,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 72040,
            triggerZ            = 0,
            triggerY            = -139790,
            triggerRange        = 1000,
            actorX              = 71980,
            actorZ              = 0,
            actorY              = -140460,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000E,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 68470,
            triggerZ            = 0,
            triggerY            = -139800,
            triggerRange        = 1000,
            actorX              = 68510,
            actorZ              = 0,
            actorY              = -140460,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000F,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 5910,
            triggerZ            = 0,
            triggerY            = 88840,
            triggerRange        = 1000,
            actorX              = 5910,
            actorZ              = 1000,
            actorY              = 88840,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0020,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 14960,
            triggerZ            = 0,
            triggerY            = -120950,
            triggerRange        = 1000,
            actorX              = 14960,
            actorZ              = 1000,
            actorY              = -120950,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0021,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x6A2
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_6B2',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    OP_B5(0x00)
    Event(0, func_12_1904)

    def _loc_6B2(): pass

    label('loc_6B2')

    Return()

# id: 0x0001 offset: 0x6B3
@scena.Code('func_01_6B3')
def func_01_6B3():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6D1',
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

    def _loc_6D1(): pass

    label('loc_6D1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A7, 1, 0x1D39)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6E3',
    )

    OP_6F(0x0000, 0)

    Jump('loc_6EA')

    def _loc_6E3(): pass

    label('loc_6E3')

    OP_6F(0x0000, 60)

    def _loc_6EA(): pass

    label('loc_6EA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0466, 0, 0x2330)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6FC',
    )

    OP_6F(0x0021, 0)

    Jump('loc_703')

    def _loc_6FC(): pass

    label('loc_6FC')

    OP_6F(0x0021, 60)

    def _loc_703(): pass

    label('loc_703')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0466, 1, 0x2331)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_715',
    )

    OP_6F(0x0022, 0)

    Jump('loc_71C')

    def _loc_715(): pass

    label('loc_715')

    OP_6F(0x0022, 60)

    def _loc_71C(): pass

    label('loc_71C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0466, 3, 0x2333)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_72E',
    )

    OP_6F(0x0023, 0)

    Jump('loc_735')

    def _loc_72E(): pass

    label('loc_72E')

    OP_6F(0x0023, 60)

    def _loc_735(): pass

    label('loc_735')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0466, 4, 0x2334)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_747',
    )

    OP_6F(0x0024, 0)

    Jump('loc_74E')

    def _loc_747(): pass

    label('loc_747')

    OP_6F(0x0024, 60)

    def _loc_74E(): pass

    label('loc_74E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0466, 6, 0x2336)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_760',
    )

    OP_6F(0x0025, 0)

    Jump('loc_767')

    def _loc_760(): pass

    label('loc_760')

    OP_6F(0x0025, 60)

    def _loc_767(): pass

    label('loc_767')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0466, 7, 0x2337)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_779',
    )

    OP_6F(0x0026, 0)

    Jump('loc_780')

    def _loc_779(): pass

    label('loc_779')

    OP_6F(0x0026, 60)

    def _loc_780(): pass

    label('loc_780')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0467, 0, 0x2338)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_792',
    )

    OP_6F(0x0027, 0)

    Jump('loc_799')

    def _loc_792(): pass

    label('loc_792')

    OP_6F(0x0027, 60)

    def _loc_799(): pass

    label('loc_799')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0467, 1, 0x2339)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7AB',
    )

    OP_6F(0x0028, 0)

    Jump('loc_7B2')

    def _loc_7AB(): pass

    label('loc_7AB')

    OP_6F(0x0028, 60)

    def _loc_7B2(): pass

    label('loc_7B2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0467, 2, 0x233A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7C4',
    )

    OP_6F(0x0029, 0)

    Jump('loc_7CB')

    def _loc_7C4(): pass

    label('loc_7C4')

    OP_6F(0x0029, 60)

    def _loc_7CB(): pass

    label('loc_7CB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0467, 4, 0x233C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7DD',
    )

    OP_6F(0x002A, 0)

    Jump('loc_7E4')

    def _loc_7DD(): pass

    label('loc_7DD')

    OP_6F(0x002A, 60)

    def _loc_7E4(): pass

    label('loc_7E4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0467, 5, 0x233D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7F6',
    )

    OP_6F(0x002B, 0)

    Jump('loc_7FD')

    def _loc_7F6(): pass

    label('loc_7F6')

    OP_6F(0x002B, 60)

    def _loc_7FD(): pass

    label('loc_7FD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0467, 6, 0x233E)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_80F',
    )

    OP_6F(0x002C, 0)

    Jump('loc_816')

    def _loc_80F(): pass

    label('loc_80F')

    OP_6F(0x002C, 60)

    def _loc_816(): pass

    label('loc_816')

    ExecExpressionWithValue(
        0x0009,
        0x24,
        (
            (Expr.PushLong, 0xEF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0010,
        0x24,
        (
            (Expr.PushLong, 0xEF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0011,
        0x24,
        (
            (Expr.PushLong, 0xEF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0012,
        0x24,
        (
            (Expr.PushLong, 0xEF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0013,
        0x24,
        (
            (Expr.PushLong, 0xEF),
            Expr.Nop,
            Expr.Return,
        ),
    )

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
        0x001B,
        0x24,
        (
            (Expr.PushLong, 0xEF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001C,
        0x24,
        (
            (Expr.PushLong, 0xEF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001D,
        0x24,
        (
            (Expr.PushLong, 0xEF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001E,
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
        'loc_8CA',
    )

    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000D, 0x0080)
    ChrSetFlags(0x000E, 0x0080)
    ChrSetFlags(0x000F, 0x0080)
    ChrSetFlags(0x0010, 0x0080)
    ChrSetFlags(0x0011, 0x0080)
    ChrSetFlags(0x0012, 0x0080)
    ChrSetFlags(0x0013, 0x0080)

    Jump('loc_901')

    def _loc_8CA(): pass

    label('loc_8CA')

    ChrSetFlags(0x0014, 0x0080)
    ChrSetFlags(0x0015, 0x0080)
    ChrSetFlags(0x0016, 0x0080)
    ChrSetFlags(0x0017, 0x0080)
    ChrSetFlags(0x0018, 0x0080)
    ChrSetFlags(0x0019, 0x0080)
    ChrSetFlags(0x001A, 0x0080)
    ChrSetFlags(0x001B, 0x0080)
    ChrSetFlags(0x001C, 0x0080)
    ChrSetFlags(0x001D, 0x0080)
    ChrSetFlags(0x001E, 0x0080)

    def _loc_901(): pass

    label('loc_901')

    OP_64(0x01, 0x0001)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0444, 2, 0x2222)),
            (Expr.TestScenaFlags, ScenaFlag(0x0444, 3, 0x2223)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_91A',
    )

    OP_72(0x0007, 0x0010)
    OP_65(0x01, 0x0001)

    def _loc_91A(): pass

    label('loc_91A')

    Call(0, 0x0019)

    Return()

# id: 0x0002 offset: 0x91F
@scena.Code('func_02_91F')
def func_02_91F():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_934',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_91F')

    def _loc_934(): pass

    label('loc_934')

    Return()

# id: 0x0003 offset: 0x935
@scena.Code('func_03_935')
def func_03_935():
    UnlockAchievement(0x02, 0x0171, 0x00)
    MapSetFlags(0x08000000)
    FadeOut(300, 0, 100)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A7, 1, 0x1D39)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A61',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0000, 30)
    OP_73(0x0000)
    OP_6F(0x0000, 30)
    AddSepith(0x00, 100)
    AddSepith(0x01, 100)
    AddSepith(0x02, 100)
    AddSepith(0x03, 100)
    AddSepith(0x04, 100)
    AddSepith(0x05, 100)
    AddSepith(0x06, 100)
    PlaySE(17, 0x00, 0x64)
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
    SetScenaFlags(ScenaFlag(0x03A7, 1, 0x1D39))

    Jump('loc_A7B')

    def _loc_A61(): pass

    label('loc_A61')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_A7B(): pass

    label('loc_A7B')

    FadeIn(300, 0)
    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0xA8D
@scena.Code('func_04_A8D')
def func_04_A8D():
    UnlockAchievement(0x02, 0x0172, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0466, 0, 0x2330)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B6A',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0021, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['全回复药'], 1)"),
            Expr.Return,
        ),
        'loc_B01',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['全回复药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0466, 0, 0x2330))

    Jump('loc_B67')

    def _loc_B01(): pass

    label('loc_B01')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['全回复药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['全回复药']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0021, 60)
    OP_70(0x0021, 0)

    def _loc_B67(): pass

    label('loc_B67')

    Jump('loc_B9B')

    def _loc_B6A(): pass

    label('loc_B6A')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

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
    def _loc_B9B(): pass

    label('loc_B9B')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0xBA9
@scena.Code('func_05_BA9')
def func_05_BA9():
    UnlockAchievement(0x02, 0x0173, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0466, 1, 0x2331)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C86',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0022, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['殂击神'], 1)"),
            Expr.Return,
        ),
        'loc_C1D',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['殂击神']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0466, 1, 0x2331))

    Jump('loc_C83')

    def _loc_C1D(): pass

    label('loc_C1D')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['殂击神']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['殂击神']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0022, 60)
    OP_70(0x0022, 0)

    def _loc_C83(): pass

    label('loc_C83')

    Jump('loc_CB7')

    def _loc_C86(): pass

    label('loc_C86')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

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
    def _loc_CB7(): pass

    label('loc_CB7')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0006 offset: 0xCC5
@scena.Code('func_06_CC5')
def func_06_CC5():
    UnlockAchievement(0x02, 0x0174, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0466, 3, 0x2333)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_DA2',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0023, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['EP填充剂Ⅱ'], 1)"),
            Expr.Return,
        ),
        'loc_D39',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

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
    SetScenaFlags(ScenaFlag(0x0466, 3, 0x2333))

    Jump('loc_D9F')

    def _loc_D39(): pass

    label('loc_D39')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

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
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0023, 60)
    OP_70(0x0023, 0)

    def _loc_D9F(): pass

    label('loc_D9F')

    Jump('loc_DD3')

    def _loc_DA2(): pass

    label('loc_DA2')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

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
    def _loc_DD3(): pass

    label('loc_DD3')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0007 offset: 0xDE1
@scena.Code('func_07_DE1')
def func_07_DE1():
    UnlockAchievement(0x02, 0x0175, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0466, 4, 0x2334)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_F79',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0024, 60)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0466, 5, 0x2335)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_EC5',
    )

    ChrSetRGBAMask(0x0008, 255, 255, 255, 0, 0)
    ChrTurnDirection(0x0008, 0x0000, 0)
    ChrMoveToRelativeAsync(0x0008, 0, 1000, 0, 0, 0x00)

    @scena.Lambda('lambda_0E38')
    def lambda_0E38():
        ChrMoveToRelativeAsync(0x00FE, 0, -1000, 0, 600, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0E38)

    @scena.Lambda('lambda_0E53')
    def lambda_0E53():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 600)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_0E53)

    ChrClearFlags(0x0008, 0x0080)

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
    Battle(0x00000432, 0x00000000, 0x00, 0x0000, 0xFF)
    ChrSetFlags(0x0008, 0x0080)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_EA0'),
        (0x00000002, 'loc_EB2'),
        (0x00000001, 'loc_EC2'),
        (-1, 'loc_EC5'),
    )

    def _loc_EA0(): pass

    label('loc_EA0')

    SetScenaFlags(ScenaFlag(0x0466, 5, 0x2335))
    OP_6F(0x0024, 60)
    Sleep(500)

    Jump('loc_EC5')

    def _loc_EB2(): pass

    label('loc_EB2')

    OP_6F(0x0024, 0)
    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

    def _loc_EC2(): pass

    label('loc_EC2')

    OP_B4(0x00)

    Return()

    def _loc_EC5(): pass

    label('loc_EC5')

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['神圣挂链'], 1)"),
            Expr.Return,
        ),
        'loc_F14',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['神圣挂链']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0466, 4, 0x2334))

    Jump('loc_F76')

    def _loc_F14(): pass

    label('loc_F14')

    FadeOut(300, 0, 100)

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['神圣挂链']),
            (TxtCtl.SetColor, 0x0),
            '。 \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['神圣挂链']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0024, 60)
    OP_70(0x0024, 0)

    def _loc_F76(): pass

    label('loc_F76')

    Jump('loc_FA8')

    def _loc_F79(): pass

    label('loc_F79')

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
    def _loc_FA8(): pass

    label('loc_FA8')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0008 offset: 0xFB6
@scena.Code('func_08_FB6')
def func_08_FB6():
    UnlockAchievement(0x02, 0x0176, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0466, 6, 0x2336)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1093',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0025, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['全回复药'], 1)"),
            Expr.Return,
        ),
        'loc_102A',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['全回复药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0466, 6, 0x2336))

    Jump('loc_1090')

    def _loc_102A(): pass

    label('loc_102A')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['全回复药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['全回复药']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0025, 60)
    OP_70(0x0025, 0)

    def _loc_1090(): pass

    label('loc_1090')

    Jump('loc_10C4')

    def _loc_1093(): pass

    label('loc_1093')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

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
    def _loc_10C4(): pass

    label('loc_10C4')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0009 offset: 0x10D2
@scena.Code('func_09_10D2')
def func_09_10D2():
    UnlockAchievement(0x02, 0x0177, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0466, 7, 0x2337)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_11AF',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0026, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['大回复药'], 1)"),
            Expr.Return,
        ),
        'loc_1146',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

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
    SetScenaFlags(ScenaFlag(0x0466, 7, 0x2337))

    Jump('loc_11AC')

    def _loc_1146(): pass

    label('loc_1146')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

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
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0026, 60)
    OP_70(0x0026, 0)

    def _loc_11AC(): pass

    label('loc_11AC')

    Jump('loc_11E0')

    def _loc_11AF(): pass

    label('loc_11AF')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

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
    def _loc_11E0(): pass

    label('loc_11E0')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x000A offset: 0x11EE
@scena.Code('func_0A_11EE')
def func_0A_11EE():
    UnlockAchievement(0x02, 0x0178, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0467, 0, 0x2338)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_12CB',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0027, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['回复药'], 1)"),
            Expr.Return,
        ),
        'loc_1262',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['回复药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0467, 0, 0x2338))

    Jump('loc_12C8')

    def _loc_1262(): pass

    label('loc_1262')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['回复药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['回复药']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0027, 60)
    OP_70(0x0027, 0)

    def _loc_12C8(): pass

    label('loc_12C8')

    Jump('loc_12FC')

    def _loc_12CB(): pass

    label('loc_12CB')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

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
    def _loc_12FC(): pass

    label('loc_12FC')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x000B offset: 0x130A
@scena.Code('func_0B_130A')
def func_0B_130A():
    UnlockAchievement(0x02, 0x017A, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0467, 1, 0x2339)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_13E7',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0028, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['清醒之药'], 1)"),
            Expr.Return,
        ),
        'loc_137E',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['清醒之药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0467, 1, 0x2339))

    Jump('loc_13E4')

    def _loc_137E(): pass

    label('loc_137E')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['清醒之药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['清醒之药']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0028, 60)
    OP_70(0x0028, 0)

    def _loc_13E4(): pass

    label('loc_13E4')

    Jump('loc_1418')

    def _loc_13E7(): pass

    label('loc_13E7')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

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
    def _loc_1418(): pass

    label('loc_1418')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x000C offset: 0x1426
@scena.Code('func_0C_1426')
def func_0C_1426():
    UnlockAchievement(0x02, 0x017B, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0467, 2, 0x233A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1503',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0029, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['七星剑'], 1)"),
            Expr.Return,
        ),
        'loc_149A',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['七星剑']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0467, 2, 0x233A))

    Jump('loc_1500')

    def _loc_149A(): pass

    label('loc_149A')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['七星剑']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['七星剑']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0029, 60)
    OP_70(0x0029, 0)

    def _loc_1500(): pass

    label('loc_1500')

    Jump('loc_1534')

    def _loc_1503(): pass

    label('loc_1503')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

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
    def _loc_1534(): pass

    label('loc_1534')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x000D offset: 0x1542
@scena.Code('func_0D_1542')
def func_0D_1542():
    UnlockAchievement(0x02, 0x017C, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0467, 4, 0x233C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_161F',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x002A, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['圣灵药'], 1)"),
            Expr.Return,
        ),
        'loc_15B6',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

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
    SetScenaFlags(ScenaFlag(0x0467, 4, 0x233C))

    Jump('loc_161C')

    def _loc_15B6(): pass

    label('loc_15B6')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

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
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x002A, 60)
    OP_70(0x002A, 0)

    def _loc_161C(): pass

    label('loc_161C')

    Jump('loc_1650')

    def _loc_161F(): pass

    label('loc_161F')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

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
    def _loc_1650(): pass

    label('loc_1650')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x000E offset: 0x165E
@scena.Code('func_0E_165E')
def func_0E_165E():
    UnlockAchievement(0x02, 0x017D, 0x00)
    MapSetFlags(0x08000000)
    FadeOut(300, 0, 100)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0467, 5, 0x233D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_178A',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x002B, 30)
    OP_73(0x002B)
    OP_6F(0x002B, 30)
    AddSepith(0x00, 100)
    AddSepith(0x01, 100)
    AddSepith(0x02, 100)
    AddSepith(0x03, 100)
    AddSepith(0x04, 100)
    AddSepith(0x05, 100)
    AddSepith(0x06, 100)
    PlaySE(17, 0x00, 0x64)
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
    SetScenaFlags(ScenaFlag(0x0467, 5, 0x233D))

    Jump('loc_17A4')

    def _loc_178A(): pass

    label('loc_178A')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_17A4(): pass

    label('loc_17A4')

    FadeIn(300, 0)
    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x000F offset: 0x17B6
@scena.Code('func_0F_17B6')
def func_0F_17B6():
    UnlockAchievement(0x02, 0x017E, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0467, 6, 0x233E)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1893',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x002C, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['EP填充剂Ⅱ'], 1)"),
            Expr.Return,
        ),
        'loc_182A',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

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
    SetScenaFlags(ScenaFlag(0x0467, 6, 0x233E))

    Jump('loc_1890')

    def _loc_182A(): pass

    label('loc_182A')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

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
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x002C, 60)
    OP_70(0x002C, 0)

    def _loc_1890(): pass

    label('loc_1890')

    Jump('loc_18C4')

    def _loc_1893(): pass

    label('loc_1893')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

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
    def _loc_18C4(): pass

    label('loc_18C4')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0010 offset: 0x18D2
@scena.Code('func_10_18D2')
def func_10_18D2():
    ClearScenaFlags(ScenaFlag(0x0390, 1, 0x1C81))
    ClearScenaFlags(ScenaFlag(0x0390, 2, 0x1C82))
    ClearScenaFlags(ScenaFlag(0x0390, 3, 0x1C83))
    ClearScenaFlags(ScenaFlag(0x0390, 4, 0x1C84))
    ClearScenaFlags(ScenaFlag(0x0390, 5, 0x1C85))
    SetScenaFlags(ScenaFlag(0x0390, 6, 0x1C86))
    ClearScenaFlags(ScenaFlag(0x0390, 7, 0x1C87))
    ClearScenaFlags(ScenaFlag(0x0391, 0, 0x1C88))

    Return()

# id: 0x0011 offset: 0x18EB
@scena.Code('func_11_18EB')
def func_11_18EB():
    ClearScenaFlags(ScenaFlag(0x0390, 1, 0x1C81))
    ClearScenaFlags(ScenaFlag(0x0390, 2, 0x1C82))
    ClearScenaFlags(ScenaFlag(0x0390, 3, 0x1C83))
    ClearScenaFlags(ScenaFlag(0x0390, 4, 0x1C84))
    ClearScenaFlags(ScenaFlag(0x0390, 5, 0x1C85))
    ClearScenaFlags(ScenaFlag(0x0390, 6, 0x1C86))
    SetScenaFlags(ScenaFlag(0x0390, 7, 0x1C87))
    ClearScenaFlags(ScenaFlag(0x0391, 0, 0x1C88))

    Return()

# id: 0x0012 offset: 0x1904
@scena.Code('func_12_1904')
def func_12_1904():
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
        'loc_191B',
    )

    Call(0, 0x001E)
    Call(0, 0x001F)

    def _loc_191B(): pass

    label('loc_191B')

    LoadChip('ED6_DT27/CH04000._CH', 'ED6_DT27/CH04000P._CP', 10)
    LoadChip('ED6_DT27/CH04001._CH', 'ED6_DT27/CH04001P._CP', 11)
    LoadChip('ED6_DT27/CH04010._CH', 'ED6_DT27/CH04010P._CP', 12)
    LoadChip('ED6_DT27/CH04011._CH', 'ED6_DT27/CH04011P._CP', 13)
    LoadChip('ED6_DT07/CH00310._CH', 'ED6_DT07/CH00310P._CP', 14)
    LoadChip('ED6_DT07/CH00311._CH', 'ED6_DT07/CH00311P._CP', 15)

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_197C'),
        (0x00000003, 'loc_1993'),
        (0x00000004, 'loc_19AA'),
        (0x00000005, 'loc_19C1'),
        (0x00000006, 'loc_19D8'),
        (0x00000007, 'loc_19EF'),
        (0x00000008, 'loc_1A06'),
        (-1, 'loc_1A1D'),
    )

    def _loc_197C(): pass

    label('loc_197C')

    LoadChip('ED6_DT07/CH00120._CH', 'ED6_DT07/CH00120P._CP', 16)
    LoadChip('ED6_DT07/CH00121._CH', 'ED6_DT07/CH00121P._CP', 17)

    Jump('loc_1A1D')

    def _loc_1993(): pass

    label('loc_1993')

    LoadChip('ED6_DT07/CH00130._CH', 'ED6_DT07/CH00130P._CP', 16)
    LoadChip('ED6_DT07/CH00131._CH', 'ED6_DT07/CH00131P._CP', 17)

    Jump('loc_1A1D')

    def _loc_19AA(): pass

    label('loc_19AA')

    LoadChip('ED6_DT27/CH04210._CH', 'ED6_DT27/CH04210P._CP', 16)
    LoadChip('ED6_DT27/CH04211._CH', 'ED6_DT27/CH04211P._CP', 17)

    Jump('loc_1A1D')

    def _loc_19C1(): pass

    label('loc_19C1')

    LoadChip('ED6_DT07/CH00150._CH', 'ED6_DT07/CH00150P._CP', 16)
    LoadChip('ED6_DT07/CH00151._CH', 'ED6_DT07/CH00151P._CP', 17)

    Jump('loc_1A1D')

    def _loc_19D8(): pass

    label('loc_19D8')

    LoadChip('ED6_DT07/CH00160._CH', 'ED6_DT07/CH00160P._CP', 16)
    LoadChip('ED6_DT07/CH00161._CH', 'ED6_DT07/CH00161P._CP', 17)

    Jump('loc_1A1D')

    def _loc_19EF(): pass

    label('loc_19EF')

    LoadChip('ED6_DT07/CH00170._CH', 'ED6_DT07/CH00170P._CP', 16)
    LoadChip('ED6_DT07/CH00171._CH', 'ED6_DT07/CH00171P._CP', 17)

    Jump('loc_1A1D')

    def _loc_1A06(): pass

    label('loc_1A06')

    LoadChip('ED6_DT27/CH04080._CH', 'ED6_DT27/CH04080P._CP', 16)
    LoadChip('ED6_DT27/CH04081._CH', 'ED6_DT27/CH04081P._CP', 17)

    Jump('loc_1A1D')

    def _loc_1A1D(): pass

    label('loc_1A1D')

    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x0015, 0x0080)
    ChrSetChipByIndex(0x0101, 10)
    ChrSetChipByIndex(0x0102, 12)
    ChrSetChipByIndex(0x010B, 14)
    ChrSetChipByIndex(0x00F9, 16)
    CameraMove(-25490, 100, 79270, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(4000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    CameraMove(-20610, 0, 81250, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(2210, 0)
    OP_6C(45000, 0)
    OP_6E(502, 0)
    FadeIn(1000, 0)

    @scena.Lambda('lambda_1AD8')
    def lambda_1AD8():
        CameraMove(-4780, 0, 80680, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1AD8)

    @scena.Lambda('lambda_1AF0')
    def lambda_1AF0():
        OP_67(0, 5000, -10000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1AF0)

    @scena.Lambda('lambda_1B08')
    def lambda_1B08():
        CameraSetDistance(2830, 5000)

        ExitThread()

    DispatchAsync(0x0102, 0x0000, lambda_1B08)

    @scena.Lambda('lambda_1B18')
    def lambda_1B18():
        OP_6C(56000, 5000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_1B18)

    CreateThread(0x0102, 0x01, 0x00, func_14_24F6)
    Sleep(100)

    CreateThread(0x0101, 0x01, 0x00, func_13_24AE)
    Sleep(300)

    CreateThread(0x010B, 0x01, 0x00, func_15_253E)
    Sleep(100)

    CreateThread(0x00F9, 0x01, 0x00, func_16_2586)
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x010B, 0x0001)
    WaitForThreadExit(0x00F9, 0x0001)
    Fade(500)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0102, 65535)
    ChrSetChipByIndex(0x010B, 65535)
    ChrSetChipByIndex(0x00F9, 65535)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x010B,
        (
            '#0090400187V#216F#6P这、这就是『古罗力亚斯』的内部……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1C02',
    )

    ChrTalk(
        0x0107,
        (
            '#0070400188V#065F好、好厉害……！\n',
            '竟然如此宽阔……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1DF7')

    def _loc_1C02(): pass

    label('loc_1C02')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1C4E',
    )

    ChrTalk(
        0x0105,
        (
            '#0060400189V#1163F……完全不像是在\n',
            '飞船里的宽度啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1DF7')

    def _loc_1C4E(): pass

    label('loc_1C4E')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1C98',
    )

    ChrTalk(
        0x0109,
        (
            '#0180400190V#1068F啊～完全不像是在\n',
            '飞船里的宽度呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1DF7')

    def _loc_1C98(): pass

    label('loc_1C98')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1CEF',
    )

    ChrTalk(
        0x0103,
        (
            '#0030400191V#022F原来如此，和外观一样，\n',
            '里面也是很夸张的宽度啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1DF7')

    def _loc_1CEF(): pass

    label('loc_1CEF')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1D68',
    )

    ChrTalk(
        0x0104,
        (
            '#0040400192V#033F这……\n',
            '这就是宽阔的舰内啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040400193V#031F感觉都快可以开\n',
            '我的演奏会了不是吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1DF7')

    def _loc_1D68(): pass

    label('loc_1D68')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1DB3',
    )

    ChrTalk(
        0x0106,
        (
            '#0050400194V#555F咦……完全不像是在\n',
            '飞船里的宽度啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1DF7')

    def _loc_1DB3(): pass

    label('loc_1DB3')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1DF7',
    )

    ChrTalk(
        0x0108,
        (
            '#0080400195V#072F嗯……\n',
            '很合乎飞船外观的宽度嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1DF7(): pass

    label('loc_1DF7')

    Sleep(100)

    Fade(500)
    CameraMove(-10600, 0, 80800, 0)
    OP_67(0, 6980, -10000, 0)
    CameraSetDistance(3470, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    ChrSetDirection(0x0101, 225, 400)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010400196V#1007F#5P呼～\n',
            '宽阔得简直令人头晕呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010400197V#1002F而且结社的人形兵器\n',
            '又放得到处都是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0090400198V#215F#6P…………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090400199V#212F你们曾经从这艘舰艇\n',
            '逃出过吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090400200V大哥他们所在的地方有线索吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1F4C')
    def lambda_1F4C():
        ChrTurnDirection(0x00FE, 0x010B, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1F4C)

    Sleep(50)

    @scena.Lambda('lambda_1F5F')
    def lambda_1F5F():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1F5F)

    Sleep(50)

    @scena.Lambda('lambda_1F72')
    def lambda_1F72():
        ChrTurnDirection(0x00FE, 0x010B, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_1F72)

    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010400201V#1004F#5P啊，嗯……这个啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010400202V#1015F说不定在一开始\n',
            '关我的客舱附近……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020400203V#1035F#2P不……\n',
            '因为那里怎么说都是客房。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020400204V#1042F多半是被关在\n',
            '监禁用的牢房里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x010B, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_208A')
    def lambda_208A():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_208A)

    Sleep(50)

    @scena.Lambda('lambda_209D')
    def lambda_209D():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_209D)

    Sleep(50)

    @scena.Lambda('lambda_20B0')
    def lambda_20B0():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_20B0)

    WaitForThreadExit(0x010B, 0x0001)

    ChrTalk(
        0x010B,
        (
            '#0090400205V#216F#6P监、监禁用的牢房里～！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010400206V#1002F#5P还、还有这种房间啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010400207V之前逃脱的时候，\n',
            '印象中倒是没看过……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0102, 0, 400)
    Sleep(300)

    ChrTalk(
        0x0102,
        (
            '#0020400208V#1035F#4P那个时候，防止脱逃用的\n',
            '电磁栅栏都是展开着的，\n',
            '所以能前往的地方很有限。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020400209V#1042F但是现在电磁栅栏\n',
            '似乎都没有展开……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020400210V说不定这正是帮助\n',
            '多伦先生他们的好机会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0090400211V#212F#6P那、那么……\n',
            '那个牢房在哪里！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2269')
    def lambda_2269():
        ChrTurnDirection(0x00FE, 0x0102, 400)
        Yield()

        Jump('lambda_2269')

    DispatchAsync2(0x0101, 0x0002, lambda_2269)

    @scena.Lambda('lambda_227A')
    def lambda_227A():
        ChrTurnDirection(0x00FE, 0x0102, 400)
        Yield()

        Jump('lambda_227A')

    DispatchAsync2(0x010B, 0x0002, lambda_227A)

    @scena.Lambda('lambda_228B')
    def lambda_228B():
        ChrTurnDirection(0x00FE, 0x0102, 400)
        Yield()

        Jump('lambda_228B')

    DispatchAsync2(0x00F9, 0x0002, lambda_228B)

    ChrSetDirection(0x0102, 90, 400)
    Sleep(300)

    @scena.Lambda('lambda_22A8')
    def lambda_22A8():
        CameraMove(-3990, 0, 77560, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_22A8)

    ChrWalkTo(0x0102, -4560, 0, 77140, 3000, 0x00)
    WaitForThreadExit(0x0101, 0x0000)
    ChrSetDirection(0x0102, 180, 400)
    CameraMove(-1740, 0, 73860, 1500)

    ChrTalk(
        0x0102,
        (
            '#0020400212V#1042F#5P……这前面的通道\n',
            '有接连到下层的小楼梯。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020400213V从那里下去应该就是牢房了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(500)
    CameraMove(-9270, 0, 80720, 0)
    OP_67(0, 6260, -10000, 0)
    CameraSetDistance(3680, 0)
    OP_6C(57000, 0)
    OP_6E(262, 0)
    ChrSetDirection(0x0102, 270, 400)
    TerminateThread(0x0101, 0x02)
    TerminateThread(0x010B, 0x02)
    TerminateThread(0x00F9, 0x02)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010400214V#1006F#6P向下通往牢房的小楼梯啊……\n',
            '好～先试着调查看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    CameraMove(-10420, 0, 79270, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(4000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0000, -10420, 0, 79270, 90)
    ChrSetPos(0x0001, -10420, 0, 79270, 90)
    ChrSetPos(0x0002, -10420, 0, 79270, 90)
    ChrSetPos(0x0003, -10420, 0, 79270, 90)
    OP_69(0x0000, 0)
    SetScenaFlags(ScenaFlag(0x0444, 2, 0x2222))
    OP_28(0x009E, 0x01, 0x0010)
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x0013 offset: 0x24AE
@scena.Code('func_13_24AE')
def func_13_24AE():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetPos(0x00FE, -32830, -200, 80800, 90)

    @scena.Lambda('lambda_24D5')
    def lambda_24D5():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_24D5)

    ChrWalkTo(0x00FE, -10600, 0, 80800, 6000, 0x00)

    Return()

# id: 0x0014 offset: 0x24F6
@scena.Code('func_14_24F6')
def func_14_24F6():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetPos(0x00FE, -32830, -200, 79270, 90)

    @scena.Lambda('lambda_251D')
    def lambda_251D():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_251D)

    ChrWalkTo(0x00FE, -10720, 0, 79100, 6000, 0x00)

    Return()

# id: 0x0015 offset: 0x253E
@scena.Code('func_15_253E')
def func_15_253E():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetPos(0x00FE, -32830, -200, 81200, 90)

    @scena.Lambda('lambda_2565')
    def lambda_2565():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2565)

    ChrWalkTo(0x00FE, -12180, 0, 80830, 6000, 0x00)

    Return()

# id: 0x0016 offset: 0x2586
@scena.Code('func_16_2586')
def func_16_2586():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetPos(0x00FE, -32830, -200, 79180, 90)

    @scena.Lambda('lambda_25AD')
    def lambda_25AD():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_25AD)

    ChrWalkTo(0x00FE, -12550, 0, 79030, 6000, 0x00)

    Return()

# id: 0x0017 offset: 0x25CE
@scena.Code('func_17_25CE')
def func_17_25CE():
    Switch(
        (
            (Expr.PushValueByIndex, 0xA),
            Expr.Return,
        ),
        (0x00000000, 'loc_25FE'),
        (0x00000001, 'loc_2660'),
        (0x0000000A, 'loc_26C4'),
        (0x00000006, 'loc_2729'),
        (0x00000004, 'loc_278A'),
        (0x00000008, 'loc_27EE'),
        (0x00000002, 'loc_2854'),
        (0x00000003, 'loc_28B5'),
        (0x00000005, 'loc_291C'),
        (0x00000007, 'loc_297F'),
        (-1, 'loc_29E6'),
    )

    def _loc_25FE(): pass

    label('loc_25FE')

    ChrTalk(
        0x0101,
        (
            '#0010400215V#1002F（监禁用的牢房\n',
            '  是在通道的反方向吧……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010400216V（得先去那边。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_29E6')

    def _loc_2660(): pass

    label('loc_2660')

    ChrTalk(
        0x0102,
        (
            '#0020400217V#1042F（监禁用的牢房\n',
            '  是在通道的反方向……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020400218V（这边待会儿再来。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_29E6')

    def _loc_26C4(): pass

    label('loc_26C4')

    ChrTalk(
        0x010B,
        (
            '#0090400219V#212F（……监禁用的牢房\n',
            '  是在通道的反方向吧。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090400220V（得先去那边……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_29E6')

    def _loc_2729(): pass

    label('loc_2729')

    ChrTalk(
        0x0107,
        (
            '#0070400221V#062F（嗯，记得牢房\n',
            '  是在通道的反方向吧……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070400222V（得先去那边。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_29E6')

    def _loc_278A(): pass

    label('loc_278A')

    ChrTalk(
        0x0105,
        (
            '#0060400223V#1162F（监禁用的牢房\n',
            '  应该是在通道的反方向……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060400224V（得先去那边。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_29E6')

    def _loc_27EE(): pass

    label('loc_27EE')

    ChrTalk(
        0x0109,
        (
            '#0180400225V#1063F（监禁用的牢房\n',
            '  是在通道的反方向吧……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180400226V（这边待会儿再来。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_29E6')

    def _loc_2854(): pass

    label('loc_2854')

    ChrTalk(
        0x0103,
        (
            '#0030400227V#022F（监禁用的牢房\n',
            '  是在通道的反方向吧……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030400228V（先去那边吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_29E6')

    def _loc_28B5(): pass

    label('loc_28B5')

    ChrTalk(
        0x0104,
        (
            '#0040400229V#030F（唔，监禁用的牢房\n',
            '  好像是在通道的反方向……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040400230V（先去那边吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_29E6')

    def _loc_291C(): pass

    label('loc_291C')

    ChrTalk(
        0x0106,
        (
            '#0050400231V#050F（监禁用的牢房\n',
            '  好像是在通道的反方向……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050400232V（得先去那边。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_29E6')

    def _loc_297F(): pass

    label('loc_297F')

    ChrTalk(
        0x0108,
        (
            '#0080400233V#072F（监禁用的牢房\n',
            '  好像是在通道的反方向。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080400234V（这边待会儿再来吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_29E6')

    def _loc_29E6(): pass

    label('loc_29E6')

    TalkEnd(0x00FF)

    Return()

# id: 0x0018 offset: 0x29EA
@scena.Code('func_18_29EA')
def func_18_29EA():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0384, 7, 0x1C27)),
            (Expr.TestScenaFlags, ScenaFlag(0x0444, 2, 0x2222)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2A53',
    )

    EventBegin(0x01)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门牢牢地关着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    ChrMoveToRelative(0x0000, 1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Jump('loc_2EEC')

    def _loc_2A53(): pass

    label('loc_2A53')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0444, 2, 0x2222)),
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 4, 0x222C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2EEC',
    )

    EventBegin(0x02)

    Switch(
        (
            (Expr.PushValueByIndex, 0xA),
            Expr.Return,
        ),
        (0x00000000, 'loc_2A91'),
        (0x00000001, 'loc_2AF5'),
        (0x0000000A, 'loc_2B69'),
        (0x00000006, 'loc_2BC4'),
        (0x00000004, 'loc_2C38'),
        (0x00000008, 'loc_2CAB'),
        (0x00000002, 'loc_2D1B'),
        (0x00000003, 'loc_2D7A'),
        (0x00000005, 'loc_2DF7'),
        (0x00000007, 'loc_2E5F'),
        (-1, 'loc_2ED1'),
    )

    def _loc_2A91(): pass

    label('loc_2A91')

    ChrTalk(
        0x0101,
        (
            '#0010400473V#1002F（还没救出\n',
            '  乔丝特的哥哥们……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010400474V（逃出的事待会儿再说吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2ED1')

    def _loc_2AF5(): pass

    label('loc_2AF5')

    ChrTalk(
        0x0102,
        (
            '#0020400475V#1043F（在救出吉尔先生他们之前\n',
            '  还是不要随便逃出比较好……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020400476V（回到舰内搜索吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2ED1')

    def _loc_2B69(): pass

    label('loc_2B69')

    ChrTalk(
        0x010B,
        (
            '#0090400477V#215F（不行……\n',
            '  还不能逃出去。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090400478V（必须救出大哥们……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2ED1')

    def _loc_2BC4(): pass

    label('loc_2BC4')

    ChrTalk(
        0x0107,
        (
            '#0070400479V#062F（还不能从『古罗力亚斯』\n',
            '  里面出去吧……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070400480V（必须尽快救出\n',
            '  空贼那些人……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2ED1')

    def _loc_2C38(): pass

    label('loc_2C38')

    ChrTalk(
        0x0105,
        (
            '#0060400481V#1163F（还不能从『古罗力亚斯』\n',
            '  里面出去……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060400482V  必须救出\n',
            '  乔丝特的哥哥们……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2ED1')

    def _loc_2CAB(): pass

    label('loc_2CAB')

    ChrTalk(
        0x0109,
        (
            '#0180400483V#1063F（哦，逃出的事待会儿再说。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180400484V（不管怎样得先救出\n',
            '  空贼的小哥们才行……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2ED1')

    def _loc_2D1B(): pass

    label('loc_2D1B')

    ChrTalk(
        0x0103,
        (
            '#0030400485V#022F（还没救出\n',
            '  空贼的成员……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030400486V（逃出的事待会儿再说吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2ED1')

    def _loc_2D7A(): pass

    label('loc_2D7A')

    ChrTalk(
        0x0104,
        (
            '#0040400487V#033F（哎呀……\n',
            '  现在逃跑可太不华丽。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040400488V#035F（必须大胆且华丽地救出\n',
            '  诸位空贼之后再说。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2ED1')

    def _loc_2DF7(): pass

    label('loc_2DF7')

    ChrTalk(
        0x0106,
        (
            '#0050400489V#052F（哦，不行不行……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050400490V#053F（要开溜也得等\n',
            '  救出了空贼之后再说。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2ED1')

    def _loc_2E5F(): pass

    label('loc_2E5F')

    ChrTalk(
        0x0108,
        (
            '#0080400491V#074F（在救出空贼们之前\n',
            '  还是不要随便逃出比较好……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080400492V#072F（回到舰内搜索吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2ED1')

    def _loc_2ED1(): pass

    label('loc_2ED1')

    ChrMoveToRelative(0x0000, 1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_2EEC(): pass

    label('loc_2EEC')

    Return()

# id: 0x0019 offset: 0x2EED
@scena.Code('func_19_2EED')
def func_19_2EED():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x9),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_2EFA',
    )

    Return()

    def _loc_2EFA(): pass

    label('loc_2EFA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0394, 1, 0x1CA1)),
            Expr.Return,
        ),
        'loc_2F2F',
    )

    OP_6F(0x0001, 100)
    OP_72(0x0001, 0x0002)
    OP_BE(0x00, 0x01, 0x0002, 0x0064, 0x0000, 0x02, -5600, -1000, -1500, 3600, 2000, 1500)

    def _loc_2F2F(): pass

    label('loc_2F2F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0394, 2, 0x1CA2)),
            Expr.Return,
        ),
        'loc_2F64',
    )

    OP_6F(0x0002, 100)
    OP_72(0x0002, 0x0002)
    OP_BE(0x01, 0x01, 0x0002, 0x0064, 0x0000, 0x02, -5600, -1000, -59500, 3600, 2000, -56500)

    def _loc_2F64(): pass

    label('loc_2F64')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0394, 3, 0x1CA3)),
            Expr.Return,
        ),
        'loc_2F99',
    )

    OP_6F(0x0003, 100)
    OP_72(0x0003, 0x0002)
    OP_BE(0x02, 0x01, 0x0002, 0x0064, 0x0000, 0x02, 38000, -1000, -5300, 45000, 2000, -2500)

    def _loc_2F99(): pass

    label('loc_2F99')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0394, 4, 0x1CA4)),
            Expr.Return,
        ),
        'loc_2FCE',
    )

    OP_6F(0x0004, 100)
    OP_72(0x0004, 0x0002)
    OP_BE(0x03, 0x01, 0x0002, 0x0064, 0x0000, 0x02, 132500, -1000, -191000, 135500, 2000, -185000)

    def _loc_2FCE(): pass

    label('loc_2FCE')

    Return()

# id: 0x001A offset: 0x2FCF
@scena.Code('func_1A_2FCF')
def func_1A_2FCF():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x9),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_2FDC',
    )

    Return()

    def _loc_2FDC(): pass

    label('loc_2FDC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0394, 1, 0x1CA1)),
            Expr.Return,
        ),
        'loc_2FE4',
    )

    Return()

    def _loc_2FE4(): pass

    label('loc_2FE4')

    EventBegin(0x02)
    PlaySE(107, 0x00, 0x64)
    OP_6F(0x0001, 0)
    OP_70(0x0001, 100)
    Sleep(1500)

    PlaySE(157, 0x00, 0x64)
    OP_73(0x0001)
    SetScenaFlags(ScenaFlag(0x0394, 1, 0x1CA1))
    Call(0, 0x0019)
    EventEnd(0x03)

    Return()

# id: 0x001B offset: 0x3010
@scena.Code('func_1B_3010')
def func_1B_3010():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x9),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_301D',
    )

    Return()

    def _loc_301D(): pass

    label('loc_301D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0394, 2, 0x1CA2)),
            Expr.Return,
        ),
        'loc_3025',
    )

    Return()

    def _loc_3025(): pass

    label('loc_3025')

    EventBegin(0x02)
    PlaySE(107, 0x00, 0x64)
    OP_6F(0x0002, 0)
    OP_70(0x0002, 100)
    Sleep(1500)

    PlaySE(157, 0x00, 0x64)
    OP_73(0x0002)
    SetScenaFlags(ScenaFlag(0x0394, 2, 0x1CA2))
    Call(0, 0x0019)
    EventEnd(0x03)

    Return()

# id: 0x001C offset: 0x3051
@scena.Code('func_1C_3051')
def func_1C_3051():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x9),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_305E',
    )

    Return()

    def _loc_305E(): pass

    label('loc_305E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0394, 3, 0x1CA3)),
            Expr.Return,
        ),
        'loc_3066',
    )

    Return()

    def _loc_3066(): pass

    label('loc_3066')

    EventBegin(0x02)
    PlaySE(107, 0x00, 0x64)
    OP_6F(0x0003, 0)
    OP_70(0x0003, 100)
    Sleep(1500)

    PlaySE(157, 0x00, 0x64)
    OP_73(0x0003)
    SetScenaFlags(ScenaFlag(0x0394, 3, 0x1CA3))
    Call(0, 0x0019)
    EventEnd(0x03)

    Return()

# id: 0x001D offset: 0x3092
@scena.Code('func_1D_3092')
def func_1D_3092():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x9),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_309F',
    )

    Return()

    def _loc_309F(): pass

    label('loc_309F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0394, 4, 0x1CA4)),
            Expr.Return,
        ),
        'loc_30A7',
    )

    Return()

    def _loc_30A7(): pass

    label('loc_30A7')

    EventBegin(0x02)
    PlaySE(107, 0x00, 0x64)
    OP_6F(0x0004, 0)
    OP_70(0x0004, 100)
    Sleep(1500)

    PlaySE(157, 0x00, 0x64)
    OP_73(0x0004)
    SetScenaFlags(ScenaFlag(0x0394, 4, 0x1CA4))
    Call(0, 0x0019)
    EventEnd(0x03)

    Return()

# id: 0x001E offset: 0x30D3
@scena.Code('func_1E_30D3')
def func_1E_30D3():
    FadeOut(0, 0, -1)
    ClearScenaFlags(ScenaFlag(0x0240, 0, 0x1200))
    ClearScenaFlags(ScenaFlag(0x0240, 1, 0x1201))
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
        (0x00000000, 'loc_314D'),
        (0x00000001, 'loc_3153'),
        (-1, 'loc_3159'),
    )

    def _loc_314D(): pass

    label('loc_314D')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_3159')

    def _loc_3153(): pass

    label('loc_3153')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_3159')

    def _loc_3159(): pass

    label('loc_3159')

    Return()

# id: 0x001F offset: 0x315A
@scena.Code('func_1F_315A')
def func_1F_315A():
    FadeOut(0, 0, -1)
    CameraMove(-78410, -8000, -230560, 0)
    OP_67(0, 6500, -10000, 0)
    CameraSetDistance(4500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    Sleep(200)

    FadeIn(0, 0)
    OP_0D()

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['约修亚'],
            ChrTable['乔丝特'],
            0x00FF,
        ),
        (
            ChrTable['阿加特'],
            ChrTable['雪拉扎德'],
            ChrTable['科洛丝'],
            ChrTable['奥利维尔'],
            ChrTable['提妲'],
            ChrTable['金'],
            ChrTable['凯文神父'],
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
    OP_69(0x0000, 0)

    Return()

# id: 0x0020 offset: 0x31EB
@scena.Code('func_20_31EB')
def func_20_31EB():
    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_AD('ED6_DT24/C_VIS255._CH', 0x0000, 0x0000, 0x000001F4)
    Sleep(500)

    OP_56(0x03)
    OP_AE(0x000001F4)
    TalkEnd(0x00FF)

    Return()

# id: 0x0021 offset: 0x3211
@scena.Code('func_21_3211')
def func_21_3211():
    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_AD('ED6_DT24/C_VIS256._CH', 0x0000, 0x0000, 0x000001F4)
    Sleep(500)

    OP_56(0x03)
    OP_AE(0x000001F4)
    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
