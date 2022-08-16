import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C5402_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C5402   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'C5402.x'
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
        ('ED6_DT27/CH04002._CH', 'ED6_DT27/CH04002P._CP'),
        ('ED6_DT27/CH04004._CH', 'ED6_DT27/CH04004P._CP'),
        ('ED6_DT29/CH12570._CH', 'ED6_DT29/CH12570P._CP'),
        ('ED6_DT29/CH12571._CH', 'ED6_DT29/CH12571P._CP'),
        ('ED6_DT29/CH12350._CH', 'ED6_DT29/CH12350P._CP'),
        ('ED6_DT29/CH12351._CH', 'ED6_DT29/CH12351P._CP'),
        ('ED6_DT29/CH12580._CH', 'ED6_DT29/CH12580P._CP'),
        ('ED6_DT29/CH12581._CH', 'ED6_DT29/CH12581P._CP'),
        ('ED6_DT29/CH12310._CH', 'ED6_DT29/CH12310P._CP'),
        ('ED6_DT29/CH12310._CH', 'ED6_DT29/CH12310P._CP'),
    ]

# id: 0x10001 offset: 0xFA
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10002 offset: 0xFA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '目标探索者',
            x           = 92240,
            z           = 0,
            y           = 25900,
            word_0C     = 0x0000,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0428,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '目标探索者',
            x           = -90960,
            z           = 0,
            y           = -210,
            word_0C     = 0x0000,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0428,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '哨兵570（蓝）',
            x           = 40060,
            z           = 1000,
            y           = -76560,
            word_0C     = 0x0000,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0424,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '哨兵235（红）',
            x           = 38010,
            z           = 1000,
            y           = 80150,
            word_0C     = 0x0000,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0427,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '哨兵570（蓝）',
            x           = -40030,
            z           = 1000,
            y           = 79100,
            word_0C     = 0x0000,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0424,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '哨兵235（红）',
            x           = -40020,
            z           = 1000,
            y           = -76980,
            word_0C     = 0x0000,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0427,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '据点武装者',
            x           = -830,
            z           = 0,
            y           = -16890,
            word_0C     = 0x0000,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0426,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '据点武装者',
            x           = -940,
            z           = 0,
            y           = 8910,
            word_0C     = 0x0000,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0426,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '据点武装者',
            x           = -1050,
            z           = 0,
            y           = 23020,
            word_0C     = 0x0000,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0426,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '目标探索者',
            x           = 92240,
            z           = 0,
            y           = 25900,
            word_0C     = 0x0000,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0431,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '目标探索者',
            x           = -90960,
            z           = 0,
            y           = -210,
            word_0C     = 0x0000,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0431,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '哨兵570（蓝）',
            x           = 40060,
            z           = 1000,
            y           = -76560,
            word_0C     = 0x0000,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x042D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '哨兵235（红）',
            x           = 38010,
            z           = 1000,
            y           = 80150,
            word_0C     = 0x0000,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0430,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '哨兵570（蓝）',
            x           = -40030,
            z           = 1000,
            y           = 79100,
            word_0C     = 0x0000,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x042D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '哨兵235（红）',
            x           = -40020,
            z           = 1000,
            y           = -76980,
            word_0C     = 0x0000,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0430,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '据点武装者',
            x           = -830,
            z           = 0,
            y           = -16890,
            word_0C     = 0x0000,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x042F,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '据点武装者',
            x           = -940,
            z           = 0,
            y           = 8910,
            word_0C     = 0x0000,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x042F,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '据点武装者',
            x           = -1050,
            z           = 0,
            y           = 23020,
            word_0C     = 0x0000,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x042F,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x2F2
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 110,
            y           = -1000,
            z           = 82080,
            range       = 3000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000015,
        ),
        ScenaEventData(
            x           = -6460,
            y           = 0,
            z           = 25940,
            range       = 5290,
            dword_10    = 0x000007D0,
            dword_14    = 0x00006E50,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000000D,
        ),
        ScenaEventData(
            x           = -6460,
            y           = 0,
            z           = -28270,
            range       = 5290,
            dword_10    = 0x000007D0,
            dword_14    = 0xFFFF9A2A,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000000E,
        ),
        ScenaEventData(
            x           = 89640,
            y           = 0,
            z           = -6980,
            range       = 95290,
            dword_10    = 0x000007D0,
            dword_14    = 0xFFFFE9D0,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000000F,
        ),
        ScenaEventData(
            x           = 89640,
            y           = 0,
            z           = -8440,
            range       = 95290,
            dword_10    = 0x000007D0,
            dword_14    = 0xFFFFE44E,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000010,
        ),
        ScenaEventData(
            x           = -93460,
            y           = 0,
            z           = 16000,
            range       = -87810,
            dword_10    = 0x000007D0,
            dword_14    = 0x00004682,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000011,
        ),
        ScenaEventData(
            x           = -93460,
            y           = 0,
            z           = 13990,
            range       = -87810,
            dword_10    = 0x000007D0,
            dword_14    = 0x00003DEA,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000012,
        ),
        ScenaEventData(
            x           = -93460,
            y           = 0,
            z           = -16200,
            range       = -87810,
            dword_10    = 0x000007D0,
            dword_14    = 0xFFFFC75C,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000013,
        ),
        ScenaEventData(
            x           = -93460,
            y           = 0,
            z           = -16200,
            range       = -87810,
            dword_10    = 0x000007D0,
            dword_14    = 0xFFFFB9B0,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000014,
        ),
    )

# id: 0x10004 offset: 0x412
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -49300,
            triggerZ            = 0,
            triggerY            = 17980,
            triggerRange        = 1000,
            actorX              = -49910,
            actorZ              = 0,
            actorY              = 18010,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -49300,
            triggerZ            = 0,
            triggerY            = 14500,
            triggerRange        = 1000,
            actorX              = -49920,
            actorZ              = 0,
            actorY              = 14540,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -49300,
            triggerZ            = 0,
            triggerY            = 21480,
            triggerRange        = 1000,
            actorX              = -49960,
            actorZ              = 0,
            actorY              = 21520,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 41020,
            triggerZ            = 0,
            triggerY            = -23700,
            triggerRange        = 1000,
            actorX              = 41020,
            actorZ              = 0,
            actorY              = -23040,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 38540,
            triggerZ            = 0,
            triggerY            = -23700,
            triggerRange        = 1000,
            actorX              = 38540,
            actorZ              = 0,
            actorY              = -23040,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 43460,
            triggerZ            = 0,
            triggerY            = -23700,
            triggerRange        = 1000,
            actorX              = 43550,
            actorZ              = 0,
            actorY              = -23000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -48700,
            triggerZ            = 0,
            triggerY            = -27980,
            triggerRange        = 1000,
            actorX              = -48040,
            actorZ              = 0,
            actorY              = -27980,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 47800,
            triggerZ            = 0,
            triggerY            = 23490,
            triggerRange        = 1000,
            actorX              = 48450,
            actorZ              = 0,
            actorY              = 23510,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0009,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 47790,
            triggerZ            = 0,
            triggerY            = 19970,
            triggerRange        = 1000,
            actorX              = 48410,
            actorZ              = 0,
            actorY              = 19980,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000A,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 47800,
            triggerZ            = 0,
            triggerY            = 16490,
            triggerRange        = 1000,
            actorX              = 48460,
            actorZ              = 0,
            actorY              = 16460,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000B,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 5030,
            triggerZ            = 0,
            triggerY            = 76990,
            triggerRange        = 1000,
            actorX              = 5030,
            actorZ              = 1000,
            actorY              = 76990,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0016,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x59E
@scena.Code('Init')
def Init():
    Return()

# id: 0x0001 offset: 0x59F
@scena.Code('func_01_59F')
def func_01_59F():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5BD',
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

    def _loc_5BD(): pass

    label('loc_5BD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A9, 4, 0x1D4C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5CF',
    )

    OP_6F(0x001A, 0)

    Jump('loc_5D6')

    def _loc_5CF(): pass

    label('loc_5CF')

    OP_6F(0x001A, 60)

    def _loc_5D6(): pass

    label('loc_5D6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A9, 5, 0x1D4D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5E8',
    )

    OP_6F(0x001B, 0)

    Jump('loc_5EF')

    def _loc_5E8(): pass

    label('loc_5E8')

    OP_6F(0x001B, 60)

    def _loc_5EF(): pass

    label('loc_5EF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A9, 6, 0x1D4E)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_601',
    )

    OP_6F(0x001C, 0)

    Jump('loc_608')

    def _loc_601(): pass

    label('loc_601')

    OP_6F(0x001C, 60)

    def _loc_608(): pass

    label('loc_608')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A6, 2, 0x1D32)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_61A',
    )

    OP_6F(0x001D, 0)

    Jump('loc_621')

    def _loc_61A(): pass

    label('loc_61A')

    OP_6F(0x001D, 60)

    def _loc_621(): pass

    label('loc_621')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A6, 3, 0x1D33)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_633',
    )

    OP_6F(0x001E, 0)

    Jump('loc_63A')

    def _loc_633(): pass

    label('loc_633')

    OP_6F(0x001E, 60)

    def _loc_63A(): pass

    label('loc_63A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A6, 4, 0x1D34)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_64C',
    )

    OP_6F(0x001F, 0)

    Jump('loc_653')

    def _loc_64C(): pass

    label('loc_64C')

    OP_6F(0x001F, 60)

    def _loc_653(): pass

    label('loc_653')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A6, 5, 0x1D35)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_665',
    )

    OP_6F(0x0020, 0)

    Jump('loc_66C')

    def _loc_665(): pass

    label('loc_665')

    OP_6F(0x0020, 60)

    def _loc_66C(): pass

    label('loc_66C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A9, 7, 0x1D4F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_67E',
    )

    OP_6F(0x0027, 0)

    Jump('loc_685')

    def _loc_67E(): pass

    label('loc_67E')

    OP_6F(0x0027, 60)

    def _loc_685(): pass

    label('loc_685')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03AA, 0, 0x1D50)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_697',
    )

    OP_6F(0x0028, 0)

    Jump('loc_69E')

    def _loc_697(): pass

    label('loc_697')

    OP_6F(0x0028, 60)

    def _loc_69E(): pass

    label('loc_69E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03AA, 1, 0x1D51)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6B0',
    )

    OP_6F(0x0029, 0)

    Jump('loc_6B7')

    def _loc_6B0(): pass

    label('loc_6B0')

    OP_6F(0x0029, 60)

    def _loc_6B7(): pass

    label('loc_6B7')

    ExecExpressionWithValue(
        0x000E,
        0x24,
        (
            (Expr.PushLong, 0xEF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000F,
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
        0x0017,
        0x24,
        (
            (Expr.PushLong, 0xEF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0018,
        0x24,
        (
            (Expr.PushLong, 0xEF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0019,
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
        'loc_735',
    )

    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000D, 0x0080)
    ChrSetFlags(0x000E, 0x0080)
    ChrSetFlags(0x000F, 0x0080)
    ChrSetFlags(0x0010, 0x0080)

    Jump('loc_762')

    def _loc_735(): pass

    label('loc_735')

    ChrSetFlags(0x0011, 0x0080)
    ChrSetFlags(0x0012, 0x0080)
    ChrSetFlags(0x0013, 0x0080)
    ChrSetFlags(0x0014, 0x0080)
    ChrSetFlags(0x0015, 0x0080)
    ChrSetFlags(0x0016, 0x0080)
    ChrSetFlags(0x0017, 0x0080)
    ChrSetFlags(0x0018, 0x0080)
    ChrSetFlags(0x0019, 0x0080)

    def _loc_762(): pass

    label('loc_762')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_777',
    )

    OP_10(0x2C, 0x01)
    OP_10(0x23, 0x00)

    Jump('loc_77D')

    def _loc_777(): pass

    label('loc_777')

    OP_10(0x2C, 0x00)
    OP_10(0x23, 0x01)

    def _loc_77D(): pass

    label('loc_77D')

    Call(0, 0x000C)

    Return()

# id: 0x0002 offset: 0x782
@scena.Code('func_02_782')
def func_02_782():
    UnlockAchievement(0x02, 0x0159, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A9, 4, 0x1D4C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_85F',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x001A, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['超重装甲服'], 1)"),
            Expr.Return,
        ),
        'loc_7F6',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['超重装甲服']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x03A9, 4, 0x1D4C))

    Jump('loc_85C')

    def _loc_7F6(): pass

    label('loc_7F6')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['超重装甲服']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['超重装甲服']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x001A, 60)
    OP_70(0x001A, 0)

    def _loc_85C(): pass

    label('loc_85C')

    Jump('loc_890')

    def _loc_85F(): pass

    label('loc_85F')

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
    def _loc_890(): pass

    label('loc_890')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0003 offset: 0x89E
@scena.Code('func_03_89E')
def func_03_89E():
    UnlockAchievement(0x02, 0x015A, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A9, 5, 0x1D4D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_97B',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x001B, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['中回复药'], 1)"),
            Expr.Return,
        ),
        'loc_912',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['中回复药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x03A9, 5, 0x1D4D))

    Jump('loc_978')

    def _loc_912(): pass

    label('loc_912')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['中回复药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['中回复药']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x001B, 60)
    OP_70(0x001B, 0)

    def _loc_978(): pass

    label('loc_978')

    Jump('loc_9AC')

    def _loc_97B(): pass

    label('loc_97B')

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
    def _loc_9AC(): pass

    label('loc_9AC')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x9BA
@scena.Code('func_04_9BA')
def func_04_9BA():
    UnlockAchievement(0x02, 0x015B, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A9, 6, 0x1D4E)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A97',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x001C, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['全回复药'], 1)"),
            Expr.Return,
        ),
        'loc_A2E',
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
    SetScenaFlags(ScenaFlag(0x03A9, 6, 0x1D4E))

    Jump('loc_A94')

    def _loc_A2E(): pass

    label('loc_A2E')

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
    OP_6F(0x001C, 60)
    OP_70(0x001C, 0)

    def _loc_A94(): pass

    label('loc_A94')

    Jump('loc_AC8')

    def _loc_A97(): pass

    label('loc_A97')

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
    def _loc_AC8(): pass

    label('loc_AC8')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0xAD6
@scena.Code('func_05_AD6')
def func_05_AD6():
    UnlockAchievement(0x02, 0x015C, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A6, 2, 0x1D32)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_BB3',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x001D, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['侏罗'], 1)"),
            Expr.Return,
        ),
        'loc_B4A',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['侏罗']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x03A6, 2, 0x1D32))

    Jump('loc_BB0')

    def _loc_B4A(): pass

    label('loc_B4A')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['侏罗']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['侏罗']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x001D, 60)
    OP_70(0x001D, 0)

    def _loc_BB0(): pass

    label('loc_BB0')

    Jump('loc_BE4')

    def _loc_BB3(): pass

    label('loc_BB3')

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
    def _loc_BE4(): pass

    label('loc_BE4')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0006 offset: 0xBF2
@scena.Code('func_06_BF2')
def func_06_BF2():
    UnlockAchievement(0x02, 0x015D, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A6, 3, 0x1D33)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_CCF',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x001E, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['EP填充剂Ⅰ'], 1)"),
            Expr.Return,
        ),
        'loc_C66',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅰ']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x03A6, 3, 0x1D33))

    Jump('loc_CCC')

    def _loc_C66(): pass

    label('loc_C66')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅰ']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅰ']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x001E, 60)
    OP_70(0x001E, 0)

    def _loc_CCC(): pass

    label('loc_CCC')

    Jump('loc_D00')

    def _loc_CCF(): pass

    label('loc_CCF')

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
    def _loc_D00(): pass

    label('loc_D00')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0007 offset: 0xD0E
@scena.Code('func_07_D0E')
def func_07_D0E():
    UnlockAchievement(0x02, 0x015E, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A6, 4, 0x1D34)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_DEB',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x001F, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['痊愈之药'], 1)"),
            Expr.Return,
        ),
        'loc_D82',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['痊愈之药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x03A6, 4, 0x1D34))

    Jump('loc_DE8')

    def _loc_D82(): pass

    label('loc_D82')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['痊愈之药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['痊愈之药']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x001F, 60)
    OP_70(0x001F, 0)

    def _loc_DE8(): pass

    label('loc_DE8')

    Jump('loc_E1C')

    def _loc_DEB(): pass

    label('loc_DEB')

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
    def _loc_E1C(): pass

    label('loc_E1C')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0008 offset: 0xE2A
@scena.Code('func_08_E2A')
def func_08_E2A():
    UnlockAchievement(0x02, 0x015F, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A6, 5, 0x1D35)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_F07',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0020, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['金耀晚礼服'], 1)"),
            Expr.Return,
        ),
        'loc_E9E',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['金耀晚礼服']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x03A6, 5, 0x1D35))

    Jump('loc_F04')

    def _loc_E9E(): pass

    label('loc_E9E')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['金耀晚礼服']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['金耀晚礼服']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0020, 60)
    OP_70(0x0020, 0)

    def _loc_F04(): pass

    label('loc_F04')

    Jump('loc_F38')

    def _loc_F07(): pass

    label('loc_F07')

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
    def _loc_F38(): pass

    label('loc_F38')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0009 offset: 0xF46
@scena.Code('func_09_F46')
def func_09_F46():
    UnlockAchievement(0x02, 0x0160, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A9, 7, 0x1D4F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1023',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0027, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['复苏药'], 1)"),
            Expr.Return,
        ),
        'loc_FBA',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['复苏药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x03A9, 7, 0x1D4F))

    Jump('loc_1020')

    def _loc_FBA(): pass

    label('loc_FBA')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['复苏药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['复苏药']),
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

    def _loc_1020(): pass

    label('loc_1020')

    Jump('loc_1054')

    def _loc_1023(): pass

    label('loc_1023')

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
    def _loc_1054(): pass

    label('loc_1054')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x000A offset: 0x1062
@scena.Code('func_0A_1062')
def func_0A_1062():
    UnlockAchievement(0x02, 0x0161, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03AA, 0, 0x1D50)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_113F',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0028, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['赤蔷薇'], 1)"),
            Expr.Return,
        ),
        'loc_10D6',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['赤蔷薇']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x03AA, 0, 0x1D50))

    Jump('loc_113C')

    def _loc_10D6(): pass

    label('loc_10D6')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['赤蔷薇']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['赤蔷薇']),
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

    def _loc_113C(): pass

    label('loc_113C')

    Jump('loc_1170')

    def _loc_113F(): pass

    label('loc_113F')

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
    def _loc_1170(): pass

    label('loc_1170')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x000B offset: 0x117E
@scena.Code('func_0B_117E')
def func_0B_117E():
    UnlockAchievement(0x02, 0x0162, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03AA, 1, 0x1D51)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_125B',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0029, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['大回复药'], 1)"),
            Expr.Return,
        ),
        'loc_11F2',
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
    SetScenaFlags(ScenaFlag(0x03AA, 1, 0x1D51))

    Jump('loc_1258')

    def _loc_11F2(): pass

    label('loc_11F2')

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
    OP_6F(0x0029, 60)
    OP_70(0x0029, 0)

    def _loc_1258(): pass

    label('loc_1258')

    Jump('loc_128C')

    def _loc_125B(): pass

    label('loc_125B')

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
    def _loc_128C(): pass

    label('loc_128C')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x000C offset: 0x129A
@scena.Code('func_0C_129A')
def func_0C_129A():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0444, 2, 0x2222)),
            Expr.Return,
        ),
        'loc_12BA',
    )

    OP_72(0x0000, 0x0020)
    OP_72(0x0000, 0x0008)
    OP_6F(0x0000, 0)
    OP_71(0x0000, 0x0002)

    Jump('loc_1312')

    def _loc_12BA(): pass

    label('loc_12BA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0384, 2, 0x1C22)),
            Expr.Return,
        ),
        'loc_12FC',
    )

    OP_72(0x0000, 0x0020)
    OP_72(0x0000, 0x0008)
    OP_6F(0x0000, 100)
    OP_72(0x0000, 0x0002)
    OP_BE(0x00, 0x01, 0x0002, 0x0064, 0x0000, 0x02, -5600, -1000, 24500, 3600, 2000, 27500)

    Jump('loc_1312')

    def _loc_12FC(): pass

    label('loc_12FC')

    OP_72(0x0000, 0x0020)
    OP_72(0x0000, 0x0008)
    OP_6F(0x0000, 0)
    OP_71(0x0000, 0x0002)

    def _loc_1312(): pass

    label('loc_1312')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0444, 2, 0x2222)),
            Expr.Return,
        ),
        'loc_1332',
    )

    OP_72(0x0001, 0x0020)
    OP_72(0x0001, 0x0008)
    OP_6F(0x0001, 0)
    OP_71(0x0001, 0x0002)

    Jump('loc_138A')

    def _loc_1332(): pass

    label('loc_1332')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0384, 3, 0x1C23)),
            Expr.Return,
        ),
        'loc_1374',
    )

    OP_72(0x0001, 0x0020)
    OP_72(0x0001, 0x0008)
    OP_6F(0x0001, 100)
    OP_72(0x0001, 0x0002)
    OP_BE(0x01, 0x01, 0x0002, 0x0064, 0x0000, 0x02, -5600, -1000, -27500, 3600, 2000, -24500)

    Jump('loc_138A')

    def _loc_1374(): pass

    label('loc_1374')

    OP_72(0x0001, 0x0020)
    OP_72(0x0001, 0x0008)
    OP_6F(0x0001, 0)
    OP_71(0x0001, 0x0002)

    def _loc_138A(): pass

    label('loc_138A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0444, 2, 0x2222)),
            Expr.Return,
        ),
        'loc_13AA',
    )

    OP_72(0x0002, 0x0020)
    OP_72(0x0002, 0x0008)
    OP_6F(0x0002, 0)
    OP_71(0x0002, 0x0002)

    Jump('loc_1402')

    def _loc_13AA(): pass

    label('loc_13AA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0384, 4, 0x1C24)),
            Expr.Return,
        ),
        'loc_13EC',
    )

    OP_72(0x0002, 0x0020)
    OP_72(0x0002, 0x0008)
    OP_6F(0x0002, 100)
    OP_72(0x0002, 0x0002)
    OP_BE(0x02, 0x01, 0x0002, 0x0064, 0x0000, 0x02, 90400, -1000, -8600, 93600, 2000, -5500)

    Jump('loc_1402')

    def _loc_13EC(): pass

    label('loc_13EC')

    OP_72(0x0002, 0x0020)
    OP_72(0x0002, 0x0008)
    OP_6F(0x0002, 0)
    OP_71(0x0002, 0x0002)

    def _loc_1402(): pass

    label('loc_1402')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0444, 2, 0x2222)),
            Expr.Return,
        ),
        'loc_1422',
    )

    OP_72(0x0003, 0x0020)
    OP_72(0x0003, 0x0008)
    OP_6F(0x0003, 0)
    OP_71(0x0003, 0x0002)

    Jump('loc_147A')

    def _loc_1422(): pass

    label('loc_1422')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0384, 5, 0x1C25)),
            Expr.Return,
        ),
        'loc_1464',
    )

    OP_72(0x0003, 0x0020)
    OP_72(0x0003, 0x0008)
    OP_6F(0x0003, 100)
    OP_72(0x0003, 0x0002)
    OP_BE(0x03, 0x01, 0x0002, 0x0064, 0x0000, 0x02, -92500, -1000, 14600, -89600, 2000, 17450)

    Jump('loc_147A')

    def _loc_1464(): pass

    label('loc_1464')

    OP_72(0x0003, 0x0020)
    OP_72(0x0003, 0x0008)
    OP_6F(0x0003, 0)
    OP_71(0x0003, 0x0002)

    def _loc_147A(): pass

    label('loc_147A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0444, 2, 0x2222)),
            Expr.Return,
        ),
        'loc_149A',
    )

    OP_72(0x0004, 0x0020)
    OP_72(0x0004, 0x0008)
    OP_6F(0x0004, 0)
    OP_71(0x0004, 0x0002)

    Jump('loc_14F2')

    def _loc_149A(): pass

    label('loc_149A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0392, 2, 0x1C92)),
            Expr.Return,
        ),
        'loc_14DC',
    )

    OP_72(0x0004, 0x0020)
    OP_72(0x0004, 0x0008)
    OP_6F(0x0004, 100)
    OP_72(0x0004, 0x0002)
    OP_BE(0x04, 0x01, 0x0002, 0x0064, 0x0000, 0x02, -92500, -1000, -17400, -89600, 2000, -14650)

    Jump('loc_14F2')

    def _loc_14DC(): pass

    label('loc_14DC')

    OP_72(0x0004, 0x0020)
    OP_72(0x0004, 0x0008)
    OP_6F(0x0004, 0)
    OP_71(0x0004, 0x0002)

    def _loc_14F2(): pass

    label('loc_14F2')

    Return()

# id: 0x000D offset: 0x14F3
@scena.Code('func_0D_14F3')
def func_0D_14F3():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0384, 2, 0x1C22)),
            (Expr.TestScenaFlags, ScenaFlag(0x0444, 2, 0x2222)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_14FF',
    )

    Return()

    def _loc_14FF(): pass

    label('loc_14FF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0384, 2, 0x1C22)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0384, 7, 0x1C27)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_157F',
    )

    EventBegin(0x00)
    PlaySE(107, 0x00, 0x64)
    OP_6F(0x0000, 0)
    OP_70(0x0000, 100)
    OP_72(0x0000, 0x0002)
    ChrSetDirection(0x0000, 180, 400)
    Sleep(300)

    ChrJumpToRelative(0x0000, 0, 0, 2000, 1000, 5000)
    Sleep(900)

    PlaySE(157, 0x00, 0x64)
    SetScenaFlags(ScenaFlag(0x0384, 2, 0x1C22))
    OP_BE(0x00, 0x01, 0x0002, 0x0064, 0x0000, 0x02, -5600, -1000, 24500, 3600, 2000, 27500)
    OP_73(0x0000)
    EventEnd(0x00)

    Jump('loc_19B7')

    def _loc_157F(): pass

    label('loc_157F')

    EventBegin(0x00)
    PlaySE(107, 0x00, 0x64)
    OP_6F(0x0000, 0)
    OP_70(0x0000, 100)
    OP_72(0x0000, 0x0002)
    SetScenaFlags(ScenaFlag(0x0384, 2, 0x1C22))
    OP_BE(0x00, 0x01, 0x0002, 0x0064, 0x0000, 0x02, -5600, -1000, 24500, 3600, 2000, 27500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0383, 6, 0x1C1E)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1629',
    )

    ChrSetDirection(0x0101, 180, 400)
    Sleep(300)

    ChrJumpToRelative(0x0101, 0, 0, 2000, 1000, 5000)
    Sleep(900)

    PlaySE(157, 0x00, 0x64)

    ChrTalk(
        0x0101,
        (
            '#0010330469V#1020F这、这是什么啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0383, 6, 0x1C1E))
    OP_28(0x0099, 0x01, 0x0002)

    Jump('loc_19B2')

    def _loc_1629(): pass

    label('loc_1629')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0383, 7, 0x1C1F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1690',
    )

    ChrSetDirection(0x0101, 180, 400)
    Sleep(300)

    ChrJumpToRelative(0x0101, 0, 0, 2000, 1000, 5000)
    Sleep(900)

    PlaySE(157, 0x00, 0x64)

    ChrTalk(
        0x0101,
        (
            '#0010330470V#1005F又、又来了！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0383, 7, 0x1C1F))
    OP_28(0x0099, 0x01, 0x0004)

    Jump('loc_19B2')

    def _loc_1690(): pass

    label('loc_1690')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0384, 0, 0x1C20)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_16FB',
    )

    ChrSetDirection(0x0101, 180, 400)
    Sleep(300)

    ChrJumpToRelative(0x0101, 0, 0, 2000, 1000, 5000)
    Sleep(900)

    PlaySE(157, 0x00, 0x64)

    ChrTalk(
        0x0101,
        (
            '#0010330471V#1019F适、适可而止吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0384, 0, 0x1C20))
    OP_28(0x0099, 0x01, 0x0008)

    Jump('loc_19B2')

    def _loc_16FB(): pass

    label('loc_16FB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0384, 1, 0x1C21)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1985',
    )

    ChrSetDirection(0x0101, 180, 400)
    Sleep(300)

    ChrJumpToRelative(0x0101, 0, 0, 2000, 1000, 5000)
    Sleep(900)

    PlaySE(157, 0x00, 0x64)
    Fade(1000)
    ChrSetPos(0x0101, -940, 0, 30200, 180)
    CameraMove(-450, 0, 27630, 0)
    OP_67(0, 9280, -10000, 0)
    CameraSetDistance(3530, 0)
    OP_6C(128000, 0)
    OP_6E(236, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010330472V#1019F………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330473V#1022F很好很好。\n',
            '就是不让我通过吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330474V#1005F既然这样的话……\n',
            '就强行突破了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x0101, 0)
    Sleep(500)

    @scena.Lambda('lambda_181C')
    def lambda_181C():
        ChrJumpTo(0x0101, -940, 0, 27380, 1000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_181C)

    OP_99(0x0101, 0x00, 0x07, 2000)
    WaitForThreadExit(0x0101, 0x0001)
    PlaySE(214, 0x00, 0x64)

    @scena.Lambda('lambda_184D')
    def lambda_184D():
        OP_69(0x0101, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_184D)

    @scena.Lambda('lambda_185B')
    def lambda_185B():
        ChrJumpToRelative(0x00FE, 0, 0, 2000, 1500, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_185B)

    ChrSetSubChip(0x0101, 3)
    ChrSetChipByIndex(0x0101, 1)
    WaitForThreadExit(0x0101, 0x0002)
    Sleep(1000)

    ChrSetSubChip(0x0101, 2)
    Sleep(100)

    ChrTalk(
        0x0101,
        (
            '#0010330475V#1007F呜呜……\n',
            '手麻掉了～……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330476V#1013F果然是太勉强了吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    Fade(500)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetSubChip(0x0101, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010330477V#1002F没办法……\n',
            '绕道前进吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    Fade(1000)
    CameraMove(-940, 0, 29380, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(4000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x0384, 1, 0x1C21))
    OP_28(0x0099, 0x01, 0x0010)

    Jump('loc_19B2')

    def _loc_1985(): pass

    label('loc_1985')

    ChrSetDirection(0x0101, 180, 400)
    Sleep(300)

    ChrJumpToRelative(0x0101, 0, 0, 2000, 1000, 5000)
    Sleep(900)

    PlaySE(157, 0x00, 0x64)

    def _loc_19B2(): pass

    label('loc_19B2')

    OP_73(0x0000)
    EventEnd(0x00)

    def _loc_19B7(): pass

    label('loc_19B7')

    Return()

# id: 0x000E offset: 0x19B8
@scena.Code('func_0E_19B8')
def func_0E_19B8():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0384, 3, 0x1C23)),
            (Expr.TestScenaFlags, ScenaFlag(0x0444, 2, 0x2222)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_19C4',
    )

    Return()

    def _loc_19C4(): pass

    label('loc_19C4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0384, 3, 0x1C23)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0384, 7, 0x1C27)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1A44',
    )

    EventBegin(0x00)
    PlaySE(107, 0x00, 0x64)
    OP_6F(0x0001, 0)
    OP_70(0x0001, 100)
    OP_72(0x0001, 0x0002)
    ChrSetDirection(0x0000, 0, 400)
    Sleep(300)

    ChrJumpToRelative(0x0000, 0, 0, -2000, 1000, 5000)
    Sleep(900)

    PlaySE(157, 0x00, 0x64)
    SetScenaFlags(ScenaFlag(0x0384, 3, 0x1C23))
    OP_BE(0x01, 0x01, 0x0002, 0x0064, 0x0000, 0x02, -5600, -1000, -27500, 3600, 2000, -24500)
    OP_73(0x0001)
    EventEnd(0x00)

    Jump('loc_1E66')

    def _loc_1A44(): pass

    label('loc_1A44')

    EventBegin(0x00)
    PlaySE(107, 0x00, 0x64)
    OP_6F(0x0001, 0)
    OP_70(0x0001, 100)
    OP_72(0x0001, 0x0002)
    SetScenaFlags(ScenaFlag(0x0384, 3, 0x1C23))
    OP_BE(0x01, 0x01, 0x0002, 0x0064, 0x0000, 0x02, -5600, -1000, -27500, 3600, 2000, -24500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0383, 6, 0x1C1E)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1AE8',
    )

    ChrSetDirection(0x0101, 0, 400)
    Sleep(300)

    ChrJumpToRelative(0x0101, 0, 0, -2000, 1000, 5000)
    Sleep(900)

    PlaySE(157, 0x00, 0x64)

    ChrTalk(
        0x0101,
        (
            '#0010330469V#1020F这、这是什么啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0383, 6, 0x1C1E))

    Jump('loc_1E61')

    def _loc_1AE8(): pass

    label('loc_1AE8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0383, 7, 0x1C1F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1B49',
    )

    ChrSetDirection(0x0101, 0, 400)
    Sleep(300)

    ChrJumpToRelative(0x0101, 0, 0, -2000, 1000, 5000)
    Sleep(900)

    PlaySE(157, 0x00, 0x64)

    ChrTalk(
        0x0101,
        (
            '#0010330470V#1005F又、又来了！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0383, 7, 0x1C1F))

    Jump('loc_1E61')

    def _loc_1B49(): pass

    label('loc_1B49')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0384, 0, 0x1C20)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1BAE',
    )

    ChrSetDirection(0x0101, 0, 400)
    Sleep(300)

    ChrJumpToRelative(0x0101, 0, 0, -2000, 1000, 5000)
    Sleep(900)

    PlaySE(157, 0x00, 0x64)

    ChrTalk(
        0x0101,
        (
            '#0010330471V#1019F适、适可而止吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0384, 0, 0x1C20))

    Jump('loc_1E61')

    def _loc_1BAE(): pass

    label('loc_1BAE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0384, 1, 0x1C21)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1E34',
    )

    ChrSetDirection(0x0101, 0, 400)
    Sleep(300)

    ChrJumpToRelative(0x0101, 0, 0, -2000, 1000, 5000)
    Sleep(900)

    PlaySE(157, 0x00, 0x64)
    Fade(1000)
    ChrSetPos(0x0101, -980, 0, -30230, 0)
    CameraMove(-980, 0, -30230, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(4000, 0)
    OP_6C(45000, 0)
    OP_6E(220, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010330481V#1019F………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330473V#1022F很好很好。\n',
            '就是不让我们通过吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330474V#1005F既然这样的话……\n',
            '就强行突破了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x0101, 0)
    Sleep(500)

    @scena.Lambda('lambda_1CD1')
    def lambda_1CD1():
        ChrJumpTo(0x0101, -980, 0, -27670, 1000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1CD1)

    OP_99(0x0101, 0x00, 0x07, 2000)
    WaitForThreadExit(0x0101, 0x0001)
    PlaySE(214, 0x00, 0x64)

    @scena.Lambda('lambda_1D02')
    def lambda_1D02():
        OP_69(0x0101, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1D02)

    @scena.Lambda('lambda_1D10')
    def lambda_1D10():
        ChrJumpToRelative(0x00FE, 0, 0, -2000, 1500, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1D10)

    ChrSetSubChip(0x0101, 3)
    ChrSetChipByIndex(0x0101, 1)
    WaitForThreadExit(0x0101, 0x0002)
    Sleep(1000)

    ChrSetSubChip(0x0101, 2)
    Sleep(100)

    ChrTalk(
        0x0101,
        (
            '#0010330484V#1007F呜呜……\n',
            '手麻掉了～……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330476V#1013F果然是太勉强了吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    Fade(500)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetSubChip(0x0101, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010330486V#1002F没办法……\n',
            '绕道前进吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    Fade(1000)
    CameraMove(-980, 0, -29670, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(4000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x0384, 1, 0x1C21))

    Jump('loc_1E61')

    def _loc_1E34(): pass

    label('loc_1E34')

    ChrSetDirection(0x0101, 0, 400)
    Sleep(300)

    ChrJumpToRelative(0x0101, 0, 0, -2000, 1000, 5000)
    Sleep(900)

    PlaySE(157, 0x00, 0x64)

    def _loc_1E61(): pass

    label('loc_1E61')

    OP_73(0x0001)
    EventEnd(0x00)

    def _loc_1E66(): pass

    label('loc_1E66')

    Return()

# id: 0x000F offset: 0x1E67
@scena.Code('func_0F_1E67')
def func_0F_1E67():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0384, 4, 0x1C24)),
            (Expr.TestScenaFlags, ScenaFlag(0x0444, 2, 0x2222)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_1E73',
    )

    Return()

    def _loc_1E73(): pass

    label('loc_1E73')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0384, 4, 0x1C24)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0384, 7, 0x1C27)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1EF3',
    )

    EventBegin(0x00)
    PlaySE(107, 0x00, 0x64)
    OP_6F(0x0002, 0)
    OP_70(0x0002, 100)
    OP_72(0x0002, 0x0002)
    ChrSetDirection(0x0000, 180, 400)
    Sleep(300)

    ChrJumpToRelative(0x0000, 0, 0, 2000, 1000, 5000)
    Sleep(900)

    PlaySE(157, 0x00, 0x64)
    SetScenaFlags(ScenaFlag(0x0384, 4, 0x1C24))
    OP_BE(0x02, 0x01, 0x0002, 0x0064, 0x0000, 0x02, 90400, -1000, -8600, 93600, 2000, -5500)
    OP_73(0x0002)
    EventEnd(0x00)

    Jump('loc_231A')

    def _loc_1EF3(): pass

    label('loc_1EF3')

    EventBegin(0x00)
    PlaySE(107, 0x00, 0x64)
    OP_6F(0x0002, 0)
    OP_70(0x0002, 100)
    OP_72(0x0002, 0x0002)
    SetScenaFlags(ScenaFlag(0x0384, 4, 0x1C24))
    OP_BE(0x02, 0x01, 0x0002, 0x0064, 0x0000, 0x02, 90400, -1000, -8600, 93600, 2000, -5500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0383, 6, 0x1C1E)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1F97',
    )

    ChrSetDirection(0x0101, 180, 400)
    Sleep(300)

    ChrJumpToRelative(0x0101, 0, 0, 2000, 1000, 5000)
    Sleep(900)

    PlaySE(157, 0x00, 0x64)

    ChrTalk(
        0x0101,
        (
            '#0010330469V#1020F这、这是什么啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0383, 6, 0x1C1E))

    Jump('loc_2315')

    def _loc_1F97(): pass

    label('loc_1F97')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0383, 7, 0x1C1F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1FF8',
    )

    ChrSetDirection(0x0101, 180, 400)
    Sleep(300)

    ChrJumpToRelative(0x0101, 0, 0, 2000, 1000, 5000)
    Sleep(900)

    PlaySE(157, 0x00, 0x64)

    ChrTalk(
        0x0101,
        (
            '#0010330470V#1005F又、又来了！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0383, 7, 0x1C1F))

    Jump('loc_2315')

    def _loc_1FF8(): pass

    label('loc_1FF8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0384, 0, 0x1C20)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_205D',
    )

    ChrSetDirection(0x0101, 180, 400)
    Sleep(300)

    ChrJumpToRelative(0x0101, 0, 0, 2000, 1000, 5000)
    Sleep(900)

    PlaySE(157, 0x00, 0x64)

    ChrTalk(
        0x0101,
        (
            '#0010330471V#1019F适、适可而止吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0384, 0, 0x1C20))

    Jump('loc_2315')

    def _loc_205D(): pass

    label('loc_205D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0384, 1, 0x1C21)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_22E8',
    )

    ChrSetDirection(0x0101, 180, 400)
    Sleep(300)

    ChrJumpToRelative(0x0101, 0, 0, 2000, 1000, 5000)
    Sleep(900)

    PlaySE(157, 0x00, 0x64)
    Fade(1000)
    ChrSetPos(0x0101, 92040, 0, -3780, 180)
    CameraMove(91880, 0, -4860, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(51000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010330490V#1019F………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330473V#1022F很好很好。\n',
            '就是不让我们通过吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330474V#1005F既然这样的话……\n',
            '就强行突破了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(213, 0x00, 0x64)
    ChrSetChipByIndex(0x0101, 0)
    Sleep(500)

    @scena.Lambda('lambda_2185')
    def lambda_2185():
        ChrJumpTo(0x0101, 92040, 0, -5720, 1000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2185)

    OP_99(0x0101, 0x00, 0x07, 2000)
    WaitForThreadExit(0x0101, 0x0001)
    PlaySE(214, 0x00, 0x64)

    @scena.Lambda('lambda_21B6')
    def lambda_21B6():
        OP_69(0x0101, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_21B6)

    @scena.Lambda('lambda_21C4')
    def lambda_21C4():
        ChrJumpToRelative(0x00FE, 0, 0, 2000, 1500, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_21C4)

    ChrSetSubChip(0x0101, 3)
    ChrSetChipByIndex(0x0101, 1)
    WaitForThreadExit(0x0101, 0x0002)
    Sleep(1000)

    ChrSetSubChip(0x0101, 2)
    Sleep(100)

    ChrTalk(
        0x0101,
        (
            '#0010330493V#1007F呜呜……\n',
            '手麻掉了～……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330476V#1013F果是是太勉强了吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    Fade(500)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetSubChip(0x0101, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010330495V#1002F没办法……\n',
            '绕道前进吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    Fade(1000)
    CameraMove(92040, 0, -3720, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x0384, 1, 0x1C21))

    Jump('loc_2315')

    def _loc_22E8(): pass

    label('loc_22E8')

    ChrSetDirection(0x0101, 180, 400)
    Sleep(300)

    ChrJumpToRelative(0x0101, 0, 0, 2000, 1000, 5000)
    Sleep(900)

    PlaySE(157, 0x00, 0x64)

    def _loc_2315(): pass

    label('loc_2315')

    OP_73(0x0002)
    EventEnd(0x00)

    def _loc_231A(): pass

    label('loc_231A')

    Return()

# id: 0x0010 offset: 0x231B
@scena.Code('func_10_231B')
def func_10_231B():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0384, 4, 0x1C24)),
            (Expr.TestScenaFlags, ScenaFlag(0x0444, 2, 0x2222)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_2327',
    )

    Return()

    def _loc_2327(): pass

    label('loc_2327')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0384, 4, 0x1C24)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0384, 7, 0x1C27)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_23A7',
    )

    EventBegin(0x00)
    PlaySE(107, 0x00, 0x64)
    OP_6F(0x0002, 0)
    OP_70(0x0002, 100)
    OP_72(0x0002, 0x0002)
    ChrSetDirection(0x0000, 0, 400)
    Sleep(300)

    ChrJumpToRelative(0x0000, 0, 0, -2000, 1000, 5000)
    Sleep(900)

    PlaySE(157, 0x00, 0x64)
    SetScenaFlags(ScenaFlag(0x0384, 4, 0x1C24))
    OP_BE(0x02, 0x01, 0x0002, 0x0064, 0x0000, 0x02, 90400, -1000, -8600, 93600, 2000, -5500)
    OP_73(0x0002)
    EventEnd(0x00)

    Jump('loc_2786')

    def _loc_23A7(): pass

    label('loc_23A7')

    EventBegin(0x00)
    PlaySE(107, 0x00, 0x64)
    OP_6F(0x0002, 0)
    OP_70(0x0002, 100)
    OP_72(0x0002, 0x0002)
    SetScenaFlags(ScenaFlag(0x0384, 4, 0x1C24))
    OP_BE(0x02, 0x01, 0x0002, 0x0064, 0x0000, 0x02, 90400, -1000, -8600, 93600, 2000, -5500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0383, 6, 0x1C1E)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_244B',
    )

    ChrSetDirection(0x0101, 0, 400)
    Sleep(300)

    ChrJumpToRelative(0x0101, 0, 0, -2000, 1000, 5000)
    Sleep(900)

    PlaySE(157, 0x00, 0x64)

    ChrTalk(
        0x0101,
        (
            '#0010330469V#1020F这、这是什么啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0383, 6, 0x1C1E))

    Jump('loc_2781')

    def _loc_244B(): pass

    label('loc_244B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0383, 7, 0x1C1F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_24AC',
    )

    ChrSetDirection(0x0101, 0, 400)
    Sleep(300)

    ChrJumpToRelative(0x0101, 0, 0, -2000, 1000, 5000)
    Sleep(900)

    PlaySE(157, 0x00, 0x64)

    ChrTalk(
        0x0101,
        (
            '#0010330470V#1005F又、又来了！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0383, 7, 0x1C1F))

    Jump('loc_2781')

    def _loc_24AC(): pass

    label('loc_24AC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0384, 0, 0x1C20)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2511',
    )

    ChrSetDirection(0x0101, 0, 400)
    Sleep(300)

    ChrJumpToRelative(0x0101, 0, 0, -2000, 1000, 5000)
    Sleep(900)

    PlaySE(157, 0x00, 0x64)

    ChrTalk(
        0x0101,
        (
            '#0010330471V#1019F适、适可而止吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0384, 0, 0x1C20))

    Jump('loc_2781')

    def _loc_2511(): pass

    label('loc_2511')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0384, 1, 0x1C21)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2754',
    )

    ChrSetDirection(0x0101, 0, 400)
    Sleep(300)

    ChrJumpToRelative(0x0101, 0, 0, -2000, 1000, 5000)
    Sleep(900)

    PlaySE(157, 0x00, 0x64)
    Fade(1000)
    ChrSetPos(0x0101, 92040, 0, -10450, 0)
    CameraMove(92040, 0, -10450, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010330499V#1019F………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330473V#1022F很好很好。\n',
            '就是不让我们通过吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330474V#1005F既然这样的话……\n',
            '就强行突破了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(213, 0x00, 0x64)
    ChrSetChipByIndex(0x0101, 0)
    Sleep(500)

    @scena.Lambda('lambda_2639')
    def lambda_2639():
        ChrJumpTo(0x0101, 92040, 0, -8360, 1000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2639)

    OP_99(0x0101, 0x00, 0x07, 2000)
    WaitForThreadExit(0x0101, 0x0001)
    PlaySE(214, 0x00, 0x64)

    @scena.Lambda('lambda_266A')
    def lambda_266A():
        OP_69(0x0101, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_266A)

    @scena.Lambda('lambda_2678')
    def lambda_2678():
        ChrJumpToRelative(0x00FE, 0, 0, -2000, 1500, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2678)

    ChrSetSubChip(0x0101, 3)
    ChrSetChipByIndex(0x0101, 1)
    WaitForThreadExit(0x0101, 0x0002)
    Sleep(1000)

    ChrSetSubChip(0x0101, 2)
    Sleep(100)

    ChrTalk(
        0x0101,
        (
            '#0010330484V#1007F呜呜……\n',
            '手麻掉了～……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330476V#1013F果然是太勉强了吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    Fade(500)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetSubChip(0x0101, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010330486V#1002F没办法……\n',
            '绕道前进吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0384, 1, 0x1C21))

    Jump('loc_2781')

    def _loc_2754(): pass

    label('loc_2754')

    ChrSetDirection(0x0101, 0, 400)
    Sleep(300)

    ChrJumpToRelative(0x0101, 0, 0, -2000, 1000, 5000)
    Sleep(900)

    PlaySE(157, 0x00, 0x64)

    def _loc_2781(): pass

    label('loc_2781')

    OP_73(0x0002)
    EventEnd(0x00)

    def _loc_2786(): pass

    label('loc_2786')

    Return()

# id: 0x0011 offset: 0x2787
@scena.Code('func_11_2787')
def func_11_2787():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0384, 5, 0x1C25)),
            (Expr.TestScenaFlags, ScenaFlag(0x0444, 2, 0x2222)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_2793',
    )

    Return()

    def _loc_2793(): pass

    label('loc_2793')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0384, 5, 0x1C25)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0384, 7, 0x1C27)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2813',
    )

    EventBegin(0x00)
    PlaySE(107, 0x00, 0x64)
    OP_6F(0x0003, 0)
    OP_70(0x0003, 100)
    OP_72(0x0003, 0x0002)
    ChrSetDirection(0x0000, 180, 400)
    Sleep(300)

    ChrJumpToRelative(0x0000, 0, 0, 2000, 1000, 5000)
    Sleep(9000)

    PlaySE(157, 0x00, 0x64)
    SetScenaFlags(ScenaFlag(0x0384, 5, 0x1C25))
    OP_BE(0x03, 0x01, 0x0002, 0x0064, 0x0000, 0x02, -92500, -1000, 14600, -89600, 2000, 17450)
    OP_73(0x0003)
    EventEnd(0x00)

    Jump('loc_2C3A')

    def _loc_2813(): pass

    label('loc_2813')

    EventBegin(0x00)
    PlaySE(107, 0x00, 0x64)
    OP_6F(0x0003, 0)
    OP_70(0x0003, 100)
    OP_72(0x0003, 0x0002)
    SetScenaFlags(ScenaFlag(0x0384, 5, 0x1C25))
    OP_BE(0x03, 0x01, 0x0002, 0x0064, 0x0000, 0x02, -92500, -1000, 14600, -89600, 2000, 17450)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0383, 6, 0x1C1E)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_28B7',
    )

    ChrSetDirection(0x0101, 180, 400)
    Sleep(300)

    ChrJumpToRelative(0x0101, 0, 0, 2000, 1000, 5000)
    Sleep(900)

    PlaySE(157, 0x00, 0x64)

    ChrTalk(
        0x0101,
        (
            '#0010330469V#1020F这、这是什么啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0383, 6, 0x1C1E))

    Jump('loc_2C35')

    def _loc_28B7(): pass

    label('loc_28B7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0383, 7, 0x1C1F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2918',
    )

    ChrSetDirection(0x0101, 180, 400)
    Sleep(300)

    ChrJumpToRelative(0x0101, 0, 0, 2000, 1000, 5000)
    Sleep(900)

    PlaySE(157, 0x00, 0x64)

    ChrTalk(
        0x0101,
        (
            '#0010330470V#1005F又、又来了！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0383, 7, 0x1C1F))

    Jump('loc_2C35')

    def _loc_2918(): pass

    label('loc_2918')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0384, 0, 0x1C20)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_297D',
    )

    ChrSetDirection(0x0101, 180, 400)
    Sleep(300)

    ChrJumpToRelative(0x0101, 0, 0, 2000, 1000, 5000)
    Sleep(900)

    PlaySE(157, 0x00, 0x64)

    ChrTalk(
        0x0101,
        (
            '#0010330471V#1019F适、适可而止吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0384, 0, 0x1C20))

    Jump('loc_2C35')

    def _loc_297D(): pass

    label('loc_297D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0384, 1, 0x1C21)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2C08',
    )

    ChrSetDirection(0x0101, 180, 400)
    Sleep(300)

    ChrJumpToRelative(0x0101, 0, 0, 2000, 1000, 5000)
    Sleep(900)

    PlaySE(157, 0x00, 0x64)
    Fade(1000)
    ChrSetPos(0x0101, -90980, 0, 20100, 180)
    CameraMove(-90920, 0, 17750, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010330508V#1019F………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330473V#1022F很好很好。\n',
            '就是不让我们通过吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330474V#1005F既然这样的话……\n',
            '就强行突破了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(213, 0x00, 0x64)
    ChrSetChipByIndex(0x0101, 0)
    Sleep(500)

    @scena.Lambda('lambda_2AA5')
    def lambda_2AA5():
        ChrJumpTo(0x0101, -90980, 0, 17450, 1000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2AA5)

    OP_99(0x0101, 0x00, 0x07, 2000)
    WaitForThreadExit(0x0101, 0x0001)
    PlaySE(214, 0x00, 0x64)

    @scena.Lambda('lambda_2AD6')
    def lambda_2AD6():
        OP_69(0x0101, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2AD6)

    @scena.Lambda('lambda_2AE4')
    def lambda_2AE4():
        ChrJumpToRelative(0x00FE, 0, 0, 2000, 1500, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2AE4)

    ChrSetSubChip(0x0101, 3)
    ChrSetChipByIndex(0x0101, 1)
    WaitForThreadExit(0x0101, 0x0002)
    Sleep(1000)

    ChrSetSubChip(0x0101, 2)
    Sleep(100)

    ChrTalk(
        0x0101,
        (
            '#0010330475V#1007F呜呜……\n',
            '手麻掉了～……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330476V#1013F果然是太勉强了吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    Fade(500)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetSubChip(0x0101, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010330477V#1002F没办法……\n',
            '绕道前进吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    Fade(1000)
    CameraMove(-90980, 0, 19450, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x0384, 1, 0x1C21))

    Jump('loc_2C35')

    def _loc_2C08(): pass

    label('loc_2C08')

    ChrSetDirection(0x0101, 180, 400)
    Sleep(300)

    ChrJumpToRelative(0x0101, 0, 0, 2000, 1000, 5000)
    Sleep(900)

    PlaySE(157, 0x00, 0x64)

    def _loc_2C35(): pass

    label('loc_2C35')

    OP_73(0x0003)
    EventEnd(0x00)

    def _loc_2C3A(): pass

    label('loc_2C3A')

    Return()

# id: 0x0012 offset: 0x2C3B
@scena.Code('func_12_2C3B')
def func_12_2C3B():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0384, 5, 0x1C25)),
            (Expr.TestScenaFlags, ScenaFlag(0x0444, 2, 0x2222)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_2C47',
    )

    Return()

    def _loc_2C47(): pass

    label('loc_2C47')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0384, 5, 0x1C25)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0384, 7, 0x1C27)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2CC7',
    )

    EventBegin(0x00)
    PlaySE(107, 0x00, 0x64)
    OP_6F(0x0003, 0)
    OP_70(0x0003, 100)
    OP_72(0x0003, 0x0002)
    ChrSetDirection(0x0000, 0, 400)
    Sleep(300)

    ChrJumpToRelative(0x0000, 0, 0, -2000, 1000, 5000)
    Sleep(900)

    PlaySE(157, 0x00, 0x64)
    SetScenaFlags(ScenaFlag(0x0384, 5, 0x1C25))
    OP_BE(0x03, 0x01, 0x0002, 0x0064, 0x0000, 0x02, -92500, -1000, 14600, -89600, 2000, 17450)
    OP_73(0x0003)
    EventEnd(0x00)

    Jump('loc_309C')

    def _loc_2CC7(): pass

    label('loc_2CC7')

    EventBegin(0x00)
    PlaySE(107, 0x00, 0x64)
    OP_6F(0x0003, 0)
    OP_70(0x0003, 100)
    OP_72(0x0003, 0x0002)
    SetScenaFlags(ScenaFlag(0x0384, 5, 0x1C25))
    OP_BE(0x03, 0x01, 0x0002, 0x0064, 0x0000, 0x02, -92500, -1000, 14600, -89600, 2000, 17450)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0383, 6, 0x1C1E)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2D6B',
    )

    ChrSetDirection(0x0101, 0, 400)
    Sleep(300)

    ChrJumpToRelative(0x0101, 0, 0, -2000, 1000, 5000)
    Sleep(900)

    PlaySE(157, 0x00, 0x64)

    ChrTalk(
        0x0101,
        (
            '#0010330469V#1020F这、这是什么啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0383, 6, 0x1C1E))

    Jump('loc_3097')

    def _loc_2D6B(): pass

    label('loc_2D6B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0383, 7, 0x1C1F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2DCC',
    )

    ChrSetDirection(0x0101, 0, 400)
    Sleep(300)

    ChrJumpToRelative(0x0101, 0, 0, -2000, 1000, 5000)
    Sleep(900)

    PlaySE(157, 0x00, 0x64)

    ChrTalk(
        0x0101,
        (
            '#0010330470V#1005F又、又来了！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0383, 7, 0x1C1F))

    Jump('loc_3097')

    def _loc_2DCC(): pass

    label('loc_2DCC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0384, 0, 0x1C20)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2E31',
    )

    ChrSetDirection(0x0101, 0, 400)
    Sleep(300)

    ChrJumpToRelative(0x0101, 0, 0, -2000, 1000, 5000)
    Sleep(900)

    PlaySE(157, 0x00, 0x64)

    ChrTalk(
        0x0101,
        (
            '#0010330471V#1019F适、适可而止吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0384, 0, 0x1C20))

    Jump('loc_3097')

    def _loc_2E31(): pass

    label('loc_2E31')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0384, 1, 0x1C21)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_306A',
    )

    ChrSetDirection(0x0101, 0, 400)
    Sleep(300)

    ChrJumpToRelative(0x0101, 0, 0, -2000, 1000, 5000)
    Sleep(900)

    PlaySE(157, 0x00, 0x64)
    Fade(1000)
    ChrSetPos(0x0101, -91000, 0, 12100, 0)
    CameraMove(-91000, 0, 12100, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010330517V#1019F………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330473V#1022F很好很好。\n',
            '就是不让我们通过吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330474V#1005F既然这样的话……\n',
            '就强行突破了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(213, 0x00, 0x64)
    ChrSetChipByIndex(0x0101, 0)
    Sleep(500)

    @scena.Lambda('lambda_2F59')
    def lambda_2F59():
        ChrJumpTo(0x0101, -91000, 0, 14360, 1000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2F59)

    OP_99(0x0101, 0x00, 0x07, 2000)
    WaitForThreadExit(0x0101, 0x0001)
    PlaySE(214, 0x00, 0x64)

    @scena.Lambda('lambda_2F8A')
    def lambda_2F8A():
        OP_69(0x0101, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2F8A)

    @scena.Lambda('lambda_2F98')
    def lambda_2F98():
        ChrJumpToRelative(0x00FE, 0, 0, -2000, 1500, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2F98)

    ChrSetSubChip(0x0101, 3)
    ChrSetChipByIndex(0x0101, 1)
    WaitForThreadExit(0x0101, 0x0002)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010330484V#1007F呜呜……\n',
            '手麻掉了～……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330476V#1013F果然是太勉强了吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    Fade(500)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetSubChip(0x0101, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010330486V#1002F没办法……\n',
            '绕道前进吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0384, 1, 0x1C21))

    Jump('loc_3097')

    def _loc_306A(): pass

    label('loc_306A')

    ChrSetDirection(0x0101, 0, 400)
    Sleep(300)

    ChrJumpToRelative(0x0101, 0, 0, -2000, 1000, 5000)
    Sleep(900)

    PlaySE(157, 0x00, 0x64)

    def _loc_3097(): pass

    label('loc_3097')

    OP_73(0x0003)
    EventEnd(0x00)

    def _loc_309C(): pass

    label('loc_309C')

    Return()

# id: 0x0013 offset: 0x309D
@scena.Code('func_13_309D')
def func_13_309D():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0392, 2, 0x1C92)),
            (Expr.TestScenaFlags, ScenaFlag(0x0444, 2, 0x2222)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_30A9',
    )

    Return()

    def _loc_30A9(): pass

    label('loc_30A9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0392, 2, 0x1C92)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0384, 7, 0x1C27)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3129',
    )

    EventBegin(0x00)
    PlaySE(107, 0x00, 0x64)
    OP_6F(0x0004, 0)
    OP_70(0x0004, 100)
    OP_72(0x0004, 0x0002)
    ChrSetDirection(0x0000, 180, 400)
    Sleep(300)

    ChrJumpToRelative(0x0000, 0, 0, 2000, 1000, 5000)
    Sleep(900)

    PlaySE(157, 0x00, 0x64)
    SetScenaFlags(ScenaFlag(0x0392, 2, 0x1C92))
    OP_BE(0x04, 0x01, 0x0002, 0x0064, 0x0000, 0x02, -92500, -1000, -17400, -89600, 2000, -14650)
    OP_73(0x0004)
    EventEnd(0x00)

    Jump('loc_3550')

    def _loc_3129(): pass

    label('loc_3129')

    EventBegin(0x00)
    PlaySE(107, 0x00, 0x64)
    OP_6F(0x0004, 0)
    OP_70(0x0004, 100)
    OP_72(0x0004, 0x0002)
    SetScenaFlags(ScenaFlag(0x0392, 2, 0x1C92))
    OP_BE(0x04, 0x01, 0x0002, 0x0064, 0x0000, 0x02, -92500, -1000, -17400, -89600, 2000, -14650)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0383, 6, 0x1C1E)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_31CD',
    )

    ChrSetDirection(0x0101, 180, 400)
    Sleep(300)

    ChrJumpToRelative(0x0101, 0, 0, 2000, 1000, 5000)
    Sleep(900)

    PlaySE(157, 0x00, 0x64)

    ChrTalk(
        0x0101,
        (
            '#0010330469V#1020F这、这是什么啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0383, 6, 0x1C1E))

    Jump('loc_354B')

    def _loc_31CD(): pass

    label('loc_31CD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0383, 7, 0x1C1F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_322E',
    )

    ChrSetDirection(0x0101, 180, 400)
    Sleep(300)

    ChrJumpToRelative(0x0101, 0, 0, 2000, 1000, 5000)
    Sleep(900)

    PlaySE(157, 0x00, 0x64)

    ChrTalk(
        0x0101,
        (
            '#0010330470V#1005F又、又来了！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0383, 7, 0x1C1F))

    Jump('loc_354B')

    def _loc_322E(): pass

    label('loc_322E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0384, 0, 0x1C20)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3293',
    )

    ChrSetDirection(0x0101, 180, 400)
    Sleep(300)

    ChrJumpToRelative(0x0101, 0, 0, 2000, 1000, 5000)
    Sleep(900)

    PlaySE(157, 0x00, 0x64)

    ChrTalk(
        0x0101,
        (
            '#0010330471V#1019F适、适可而止吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0384, 0, 0x1C20))

    Jump('loc_354B')

    def _loc_3293(): pass

    label('loc_3293')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0384, 1, 0x1C21)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_351E',
    )

    ChrSetDirection(0x0101, 180, 400)
    Sleep(300)

    ChrJumpToRelative(0x0101, 0, 0, 2000, 1000, 5000)
    Sleep(900)

    PlaySE(157, 0x00, 0x64)
    Fade(1000)
    ChrSetPos(0x0101, -91140, 0, -12020, 180)
    CameraMove(-90820, 0, -13710, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010330526V#1019F………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330473V#1022F很好很好。\n',
            '就是不让我们通过吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330474V#1005F既然这样的话……\n',
            '就强行突破了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(213, 0x00, 0x64)
    ChrSetChipByIndex(0x0101, 0)
    Sleep(500)

    @scena.Lambda('lambda_33BB')
    def lambda_33BB():
        ChrJumpTo(0x0101, -91000, 0, -14480, 1000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_33BB)

    OP_99(0x0101, 0x00, 0x07, 2000)
    WaitForThreadExit(0x0101, 0x0001)
    PlaySE(214, 0x00, 0x64)

    @scena.Lambda('lambda_33EC')
    def lambda_33EC():
        OP_69(0x0101, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_33EC)

    @scena.Lambda('lambda_33FA')
    def lambda_33FA():
        ChrJumpToRelative(0x00FE, 0, 0, 2000, 1500, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_33FA)

    ChrSetSubChip(0x0101, 3)
    ChrSetChipByIndex(0x0101, 1)
    WaitForThreadExit(0x0101, 0x0002)
    Sleep(1000)

    ChrSetSubChip(0x0101, 2)
    Sleep(100)

    ChrTalk(
        0x0101,
        (
            '#0010330529V#1007F呜呜……\n',
            '手麻掉了～……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330476V#1013F果然是太勉强了吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    Fade(500)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetSubChip(0x0101, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010330531V#1002F没办法……\n',
            '绕道前进吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    Fade(1000)
    CameraMove(-91000, 0, -12480, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x0384, 1, 0x1C21))

    Jump('loc_354B')

    def _loc_351E(): pass

    label('loc_351E')

    ChrSetDirection(0x0101, 180, 400)
    Sleep(300)

    ChrJumpToRelative(0x0101, 0, 0, 2000, 1000, 5000)
    Sleep(900)

    PlaySE(157, 0x00, 0x64)

    def _loc_354B(): pass

    label('loc_354B')

    OP_73(0x0004)
    EventEnd(0x00)

    def _loc_3550(): pass

    label('loc_3550')

    Return()

# id: 0x0014 offset: 0x3551
@scena.Code('func_14_3551')
def func_14_3551():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0392, 2, 0x1C92)),
            (Expr.TestScenaFlags, ScenaFlag(0x0444, 2, 0x2222)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_355D',
    )

    Return()

    def _loc_355D(): pass

    label('loc_355D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0392, 2, 0x1C92)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0384, 7, 0x1C27)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_35DD',
    )

    EventBegin(0x00)
    PlaySE(107, 0x00, 0x64)
    OP_6F(0x0004, 0)
    OP_70(0x0004, 100)
    OP_72(0x0004, 0x0002)
    ChrSetDirection(0x0000, 0, 400)
    Sleep(300)

    ChrJumpToRelative(0x0000, 0, 0, -2000, 1000, 5000)
    Sleep(900)

    PlaySE(157, 0x00, 0x64)
    SetScenaFlags(ScenaFlag(0x0392, 2, 0x1C92))
    OP_BE(0x04, 0x01, 0x0002, 0x0064, 0x0000, 0x02, -92500, -1000, -17400, -89600, 2000, -14650)
    OP_73(0x0004)
    EventEnd(0x00)

    Jump('loc_39C8')

    def _loc_35DD(): pass

    label('loc_35DD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0392, 2, 0x1C92)),
            (Expr.TestScenaFlags, ScenaFlag(0x0444, 2, 0x2222)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_35E9',
    )

    Return()

    def _loc_35E9(): pass

    label('loc_35E9')

    EventBegin(0x00)
    PlaySE(107, 0x00, 0x64)
    OP_6F(0x0004, 0)
    OP_70(0x0004, 100)
    OP_72(0x0004, 0x0002)
    SetScenaFlags(ScenaFlag(0x0392, 2, 0x1C92))
    OP_BE(0x04, 0x01, 0x0002, 0x0064, 0x0000, 0x02, -92500, -1000, -17400, -89600, 2000, -14650)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0383, 6, 0x1C1E)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_368D',
    )

    ChrSetDirection(0x0101, 0, 400)
    Sleep(300)

    ChrJumpToRelative(0x0101, 0, 0, -2000, 1000, 5000)
    Sleep(900)

    PlaySE(157, 0x00, 0x64)

    ChrTalk(
        0x0101,
        (
            '#0010330469V#1020F这、这是什么啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0383, 6, 0x1C1E))

    Jump('loc_39C3')

    def _loc_368D(): pass

    label('loc_368D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0383, 7, 0x1C1F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_36EE',
    )

    ChrSetDirection(0x0101, 0, 400)
    Sleep(300)

    ChrJumpToRelative(0x0101, 0, 0, -2000, 1000, 5000)
    Sleep(900)

    PlaySE(157, 0x00, 0x64)

    ChrTalk(
        0x0101,
        (
            '#0010330470V#1005F又、又来了！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0383, 7, 0x1C1F))

    Jump('loc_39C3')

    def _loc_36EE(): pass

    label('loc_36EE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0384, 0, 0x1C20)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3753',
    )

    ChrSetDirection(0x0101, 0, 400)
    Sleep(300)

    ChrJumpToRelative(0x0101, 0, 0, -2000, 1000, 5000)
    Sleep(900)

    PlaySE(157, 0x00, 0x64)

    ChrTalk(
        0x0101,
        (
            '#0010330471V#1019F适、适可而止吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0384, 0, 0x1C20))

    Jump('loc_39C3')

    def _loc_3753(): pass

    label('loc_3753')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0384, 1, 0x1C21)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3996',
    )

    ChrSetDirection(0x0101, 0, 400)
    Sleep(300)

    ChrJumpToRelative(0x0101, 0, 0, -2000, 1000, 5000)
    Sleep(900)

    PlaySE(157, 0x00, 0x64)
    Fade(1000)
    ChrSetPos(0x0101, -91080, 0, -19830, 0)
    CameraMove(-91000, 0, -17270, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010330535V#1019F………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330473V#1022F很好很好。\n',
            '就是不让我们通过吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330474V#1005F既然这样的话……\n',
            '就强行突破了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(213, 0x00, 0x64)
    ChrSetChipByIndex(0x0101, 0)
    Sleep(500)

    @scena.Lambda('lambda_387B')
    def lambda_387B():
        ChrJumpTo(0x0101, -91190, 0, -17360, 1000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_387B)

    OP_99(0x0101, 0x00, 0x07, 2000)
    WaitForThreadExit(0x0101, 0x0001)
    PlaySE(214, 0x00, 0x64)

    @scena.Lambda('lambda_38AC')
    def lambda_38AC():
        OP_69(0x0101, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_38AC)

    @scena.Lambda('lambda_38BA')
    def lambda_38BA():
        ChrJumpToRelative(0x00FE, 0, 0, -2000, 1500, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_38BA)

    ChrSetSubChip(0x0101, 3)
    ChrSetChipByIndex(0x0101, 1)
    WaitForThreadExit(0x0101, 0x0002)
    Sleep(1000)

    ChrSetSubChip(0x0101, 2)
    Sleep(100)

    ChrTalk(
        0x0101,
        (
            '#0010330484V#1007F呜呜……\n',
            '手麻掉了～……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330476V#1013F果然是太勉强了吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    Fade(500)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetSubChip(0x0101, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010330486V#1002F没办法……\n',
            '绕道前进吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0384, 1, 0x1C21))

    Jump('loc_39C3')

    def _loc_3996(): pass

    label('loc_3996')

    ChrSetDirection(0x0101, 0, 400)
    Sleep(300)

    ChrJumpToRelative(0x0101, 0, 0, -2000, 1000, 5000)
    Sleep(900)

    PlaySE(157, 0x00, 0x64)

    def _loc_39C3(): pass

    label('loc_39C3')

    OP_73(0x0004)
    EventEnd(0x00)

    def _loc_39C8(): pass

    label('loc_39C8')

    Return()

# id: 0x0015 offset: 0x39C9
@scena.Code('func_15_39C9')
def func_15_39C9():
    SetScenaFlags(ScenaFlag(0x0390, 1, 0x1C81))
    ClearScenaFlags(ScenaFlag(0x0390, 2, 0x1C82))
    ClearScenaFlags(ScenaFlag(0x0390, 3, 0x1C83))
    ClearScenaFlags(ScenaFlag(0x0390, 4, 0x1C84))
    ClearScenaFlags(ScenaFlag(0x0390, 5, 0x1C85))
    ClearScenaFlags(ScenaFlag(0x0390, 6, 0x1C86))
    ClearScenaFlags(ScenaFlag(0x0390, 7, 0x1C87))
    ClearScenaFlags(ScenaFlag(0x0391, 0, 0x1C88))

    Return()

# id: 0x0016 offset: 0x39E2
@scena.Code('func_16_39E2')
def func_16_39E2():
    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_AD('ED6_DT24/C_VIS250._CH', 0x0000, 0x0000, 0x000001F4)
    Sleep(500)

    OP_56(0x03)
    OP_AE(0x000001F4)
    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
