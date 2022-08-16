import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import R0203_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R0203   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'R0203.x'
    header.mapIndex       = 22
    header.bgm            = 29
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
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
        ('ED6_DT09/CH10020._CH', 'ED6_DT09/CH10020P._CP'),
        ('ED6_DT09/CH10021._CH', 'ED6_DT09/CH10021P._CP'),
        ('ED6_DT09/CH10180._CH', 'ED6_DT09/CH10180P._CP'),
        ('ED6_DT09/CH10181._CH', 'ED6_DT09/CH10181P._CP'),
        ('ED6_DT09/CH10260._CH', 'ED6_DT09/CH10260P._CP'),
        ('ED6_DT09/CH10261._CH', 'ED6_DT09/CH10261P._CP'),
        ('ED6_DT09/CH10210._CH', 'ED6_DT09/CH10210P._CP'),
        ('ED6_DT09/CH10211._CH', 'ED6_DT09/CH10211P._CP'),
        ('ED6_DT29/CH12090._CH', 'ED6_DT29/CH12090P._CP'),
        ('ED6_DT29/CH12091._CH', 'ED6_DT29/CH12091P._CP'),
        ('ED6_DT29/CH12130._CH', 'ED6_DT29/CH12130P._CP'),
        ('ED6_DT29/CH12131._CH', 'ED6_DT29/CH12131P._CP'),
        ('ED6_DT07/CH01310._CH', 'ED6_DT07/CH01310P._CP'),
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
        ('ED6_DT07/CH01600._CH', 'ED6_DT07/CH01600P._CP'),
        ('ED6_DT29/CH13050._CH', 'ED6_DT29/CH13050P._CP'),
    ]

# id: 0x10001 offset: 0x12A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '阿斯顿队长',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '王国军士官',
            x                   = -181690,
            z                   = -310,
            y                   = -45590,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0002,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = -181520,
            z                   = -400,
            y                   = -47440,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            name                = '',
            x                   = -159140,
            z                   = -60,
            y                   = 5400,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '洛连特方向',
            x                   = -131580,
            z                   = 0,
            y                   = -18130,
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
            name                = '威尔特桥·关所方向',
            x                   = -224350,
            z                   = 20,
            y                   = -16180,
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
            name                = '帕赛尔农场方向',
            x                   = -184980,
            z                   = 0,
            y                   = -81290,
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

# id: 0x10002 offset: 0x38A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '',
            x           = -160000,
            z           = 200,
            y           = -2000,
            word_0C     = 0x0000,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0079,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -161000,
            z           = 0,
            y           = -21000,
            word_0C     = 0x0000,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x007A,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -155000,
            z           = 0,
            y           = -44000,
            word_0C     = 0x0000,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x007B,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -178000,
            z           = 500,
            y           = -29000,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x007D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -190000,
            z           = 0,
            y           = -39000,
            word_0C     = 0x0000,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x007C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -205000,
            z           = 200,
            y           = -55000,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x007E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -193000,
            z           = 200,
            y           = -2000,
            word_0C     = 0x0000,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0079,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -207000,
            z           = 200,
            y           = -6000,
            word_0C     = 0x0000,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x007B,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -198000,
            z           = 300,
            y           = -47000,
            word_0C     = 0x0000,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x007A,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -180000,
            z           = -500,
            y           = -58000,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x007D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -159000,
            z           = 200,
            y           = -59000,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x007E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -180000,
            z           = 0,
            y           = -5000,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x007C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -172000,
            z           = 200,
            y           = -43000,
            word_0C     = 0x0000,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0079,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x4F6
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -159140,
            y           = -60,
            z           = 5400,
            range       = 2000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000007,
        ),
    )

# id: 0x10004 offset: 0x516
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -176080,
            triggerZ            = 50,
            triggerY            = 11940,
            triggerRange        = 1000,
            actorX              = -176140,
            actorZ              = 1050,
            actorY              = 12680,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -211720,
            triggerZ            = 20,
            triggerY            = -56010,
            triggerRange        = 1000,
            actorX              = -211660,
            actorZ              = 20,
            actorY              = -56570,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -145080,
            triggerZ            = 40,
            triggerY            = -50920,
            triggerRange        = 1000,
            actorX              = -144640,
            actorZ              = 40,
            actorY              = -51360,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -179550,
            triggerZ            = 0,
            triggerY            = -15360,
            triggerRange        = 1500,
            actorX              = -179550,
            actorZ              = 1500,
            actorY              = -15360,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000E,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x5A6
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_5D5',
    )

    ChrClearFlags(0x0015, 0x0080)
    ChrClearFlags(0x0016, 0x0080)
    ChrSetFlags(0x001B, 0x0080)
    ChrSetFlags(0x001C, 0x0080)
    ChrSetFlags(0x001D, 0x0080)
    ChrSetFlags(0x001E, 0x0080)
    ChrSetFlags(0x0024, 0x0080)
    ChrSetFlags(0x0027, 0x0080)

    def _loc_5D5(): pass

    label('loc_5D5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_5EE',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    OP_B5(0x00)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x73),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, func_08_FC3)

    def _loc_5EE(): pass

    label('loc_5EE')

    Return()

# id: 0x0001 offset: 0x5EF
@scena.Code('func_01_5EF')
def func_01_5EF():
    OP_16(0x02, 4000, -306000, -162000, 2293772)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0324, 2, 0x1922)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_613',
    )

    OP_6F(0x0000, 0)

    Jump('loc_61A')

    def _loc_613(): pass

    label('loc_613')

    OP_6F(0x0000, 60)

    def _loc_61A(): pass

    label('loc_61A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0324, 3, 0x1923)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_62C',
    )

    OP_6F(0x0001, 0)

    Jump('loc_633')

    def _loc_62C(): pass

    label('loc_62C')

    OP_6F(0x0001, 60)

    def _loc_633(): pass

    label('loc_633')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0324, 4, 0x1924)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_645',
    )

    OP_6F(0x0002, 0)

    Jump('loc_64C')

    def _loc_645(): pass

    label('loc_645')

    OP_6F(0x0002, 60)

    def _loc_64C(): pass

    label('loc_64C')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_674',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_674',
    )

    MapSetFlags(0x00000010)
    OP_11(0xE6, 0xF0, 0xFF, 0, 60000, 0)

    def _loc_674(): pass

    label('loc_674')

    ExecExpressionWithValue(
        0x001B,
        0x24,
        (
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001C,
        0x24,
        (
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001D,
        0x24,
        (
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001E,
        0x24,
        (
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001F,
        0x24,
        (
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0020,
        0x24,
        (
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0021,
        0x24,
        (
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0022,
        0x24,
        (
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0023,
        0x24,
        (
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0024,
        0x24,
        (
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0025,
        0x24,
        (
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0026,
        0x24,
        (
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0027,
        0x24,
        (
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0017,
        0x24,
        (
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_B2(0x00, 0x00, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            (Expr.TestScenaFlags, ScenaFlag(0x041F, 1, 0x20F9)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_729',
    )

    ChrClearFlags(0x0017, 0x0080)
    OP_B2(0x01, 0x00, 0x0080)

    def _loc_729(): pass

    label('loc_729')

    Return()

# id: 0x0002 offset: 0x72A
@scena.Code('func_02_72A')
def func_02_72A():
    TalkBegin(0x0015)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 5, 0x2085)),
            Expr.Return,
        ),
        'loc_841',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7E2',
    )

    ChrTalk(
        0x00FE,
        (
            '看来定期船\n',
            '好像也停开了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎呀呀，交通工具\n',
            '都闲下来了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只是不能使用导力器\n',
            '就成了这样的状况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是现在帝国攻进来\n',
            '可是片刻也支撑不了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Jump('loc_83E')

    def _loc_7E2(): pass

    label('loc_7E2')

    ChrTalk(
        0x00FE,
        (
            '只是不能使用导力器\n',
            '就成了这样的状况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是现在帝国攻进来\n',
            '可是片刻也支撑不了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_83E(): pass

    label('loc_83E')

    Jump('loc_977')

    def _loc_841(): pass

    label('loc_841')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_977',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_925',
    )

    ChrTalk(
        0x00FE,
        (
            '啊，那胸前的纹章，\n',
            '你们是游击士啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '让你们看见这副模样\n',
            '真是不好意思。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们在撤回基地途中，\n',
            '引擎的输出突然下降。\n',
            '于是慌忙着陆了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '救援要是能快点过来就好了，\n',
            '不过这种状况下应该会延迟吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Jump('loc_977')

    def _loc_925(): pass

    label('loc_925')

    ChrTalk(
        0x00FE,
        (
            '多亏附近有农场\n',
            '可是帮了大忙呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我和部下一起\n',
            '承蒙款待，在这里用了晚餐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_977(): pass

    label('loc_977')

    TalkEnd(0x0015)

    Return()

# id: 0x0003 offset: 0x97B
@scena.Code('func_03_97B')
def func_03_97B():
    TalkBegin(0x0016)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 5, 0x2085)),
            Expr.Return,
        ),
        'loc_A4D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A04',
    )

    ChrTalk(
        0x00FE,
        (
            '真是给这里的农场\n',
            '添了不少麻烦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '分给我们的奶酪\n',
            '实在是美味……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎，返回基地之前\n',
            '买一些作为礼物吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_A4A')

    def _loc_A04(): pass

    label('loc_A04')

    ChrTalk(
        0x00FE,
        (
            '这个农场的奶酪\n',
            '真是极品啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '到底是洛连特。\n',
            '食物真是美味啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A4A(): pass

    label('loc_A4A')

    Jump('loc_AB0')

    def _loc_A4D(): pass

    label('loc_A4D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_AB0',
    )

    ChrTalk(
        0x00FE,
        (
            '到处都没有异常，\n',
            '不过飞船就是动不了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，在救援部队到来前，\n',
            '只能在这里等下去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_AB0(): pass

    label('loc_AB0')

    TalkEnd(0x0016)

    Return()

# id: 0x0004 offset: 0xAB4
@scena.Code('func_04_AB4')
def func_04_AB4():
    UnlockAchievement(0x02, 0x01C2, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0324, 2, 0x1922)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B91',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0000, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['轰雷剑'], 1)"),
            Expr.Return,
        ),
        'loc_B28',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['轰雷剑']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0324, 2, 0x1922))

    Jump('loc_B8E')

    def _loc_B28(): pass

    label('loc_B28')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['轰雷剑']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['轰雷剑']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0000, 60)
    OP_70(0x0000, 0)

    def _loc_B8E(): pass

    label('loc_B8E')

    Jump('loc_BC2')

    def _loc_B91(): pass

    label('loc_B91')

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
    def _loc_BC2(): pass

    label('loc_BC2')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0xBD0
@scena.Code('func_05_BD0')
def func_05_BD0():
    UnlockAchievement(0x02, 0x01C3, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0324, 3, 0x1923)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_CAD',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0001, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['清醒之药'], 1)"),
            Expr.Return,
        ),
        'loc_C44',
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
    SetScenaFlags(ScenaFlag(0x0324, 3, 0x1923))

    Jump('loc_CAA')

    def _loc_C44(): pass

    label('loc_C44')

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
    OP_6F(0x0001, 60)
    OP_70(0x0001, 0)

    def _loc_CAA(): pass

    label('loc_CAA')

    Jump('loc_CDE')

    def _loc_CAD(): pass

    label('loc_CAD')

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
    def _loc_CDE(): pass

    label('loc_CDE')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0006 offset: 0xCEC
@scena.Code('func_06_CEC')
def func_06_CEC():
    UnlockAchievement(0x02, 0x01C4, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0324, 4, 0x1924)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_DC9',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0002, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['中回复药'], 1)"),
            Expr.Return,
        ),
        'loc_D60',
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
    SetScenaFlags(ScenaFlag(0x0324, 4, 0x1924))

    Jump('loc_DC6')

    def _loc_D60(): pass

    label('loc_D60')

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
    OP_6F(0x0002, 60)
    OP_70(0x0002, 0)

    def _loc_DC6(): pass

    label('loc_DC6')

    Jump('loc_DFA')

    def _loc_DC9(): pass

    label('loc_DC9')

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
    def _loc_DFA(): pass

    label('loc_DFA')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0007 offset: 0xE08
@scena.Code('func_07_E08')
def func_07_E08():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x041F, 1, 0x20F9)),
            Expr.Return,
        ),
        'loc_E10',
    )

    Return()

    def _loc_E10(): pass

    label('loc_E10')

    EventBegin(0x01)

    ExecExpressionWithValue(
        0x0000,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0001,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0002,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0003,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0004,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0005,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0006,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0007,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetSubChip(0x0000, 0)
    ChrSetSubChip(0x0001, 0)
    ChrSetSubChip(0x0002, 0)
    ChrSetSubChip(0x0003, 0)
    ChrSetSubChip(0x0004, 0)
    ChrSetSubChip(0x0005, 0)
    ChrSetSubChip(0x0006, 0)
    ChrSetSubChip(0x0007, 0)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '大型魔兽正在四处游荡中。',
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
        0,
        (
            TXT(0x00, '【消灭它】\n'),
            TXT(0x01, '【放弃】\n'),
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
        (0x00000001, 'loc_EF5'),
        (-1, 'loc_F18'),
    )

    def _loc_EF5(): pass

    label('loc_EF5')

    Fade(500)
    OP_89(0x0000, -160450, 230, -1320, 0)
    OP_69(0x0000, 0)
    OP_30(0x01)
    OP_0D()
    EventEnd(0x00)

    Return()

    def _loc_F18(): pass

    label('loc_F18')

    Battle(0x00000EF0, 0x00000000, 0x00, 0x0000, 0xFF)
    EventBegin(0x01)
    OP_89(0x0000, -160450, 230, -1320, 0)
    OP_69(0x0000, 0)
    OP_30(0x01)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000002, 'loc_F51'),
        (0x00000001, 'loc_F54'),
        (-1, 'loc_F57'),
    )

    def _loc_F51(): pass

    label('loc_F51')

    EventEnd(0x00)

    Return()

    def _loc_F54(): pass

    label('loc_F54')

    OP_B4(0x00)

    Return()

    def _loc_F57(): pass

    label('loc_F57')

    EventBegin(0x01)
    ChrSetFlags(0x0017, 0x0080)
    OP_B2(0x00, 0x00, 0x0080)
    OP_0D()
    Sleep(400)

    PlaySE(23, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '消灭了通缉魔兽！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetScenaFlags(ScenaFlag(0x041F, 1, 0x20F9))
    OP_28(0x00B8, 0x04, 0x10)
    OP_28(0x00B8, 0x04, 0x02)
    OP_28(0x00B8, 0x01, 0x0001)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x00)

    Return()

# id: 0x0008 offset: 0xFC3
@scena.Code('func_08_FC3')
def func_08_FC3():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_DB()
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    ChrSetPos(0x0009, -165970, -10, -34300, 180)
    ChrSetPos(0x000C, -161610, 50, -48590, 319)
    ChrSetPos(0x000D, -159300, 120, -45800, 315)
    ChrSetPos(0x000E, -157300, 10, -39940, 225)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    ChrSetChipByIndex(0x000E, 12)
    ChrSetSubChip(0x000E, 0)
    CameraMove(-163100, 100, -41390, 0)
    OP_67(0, 11240, -10000, 0)
    CameraSetDistance(7200, 0)
    OP_6C(78000, 0)
    OP_6E(295, 0)
    OP_12(0x00007D00, 0x0003F7A0, 0x00000000)
    CreateThread(0x0009, 0x01, 0x00, func_09_116D)
    CreateThread(0x000C, 0x01, 0x00, func_0A_11EB)
    CreateThread(0x000D, 0x01, 0x00, func_0B_1264)
    OP_62(0x000A, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x00)
    Sleep(50)

    OP_62(0x000B, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x00)
    OP_C8(0x0200, 0x0046, 'C_PLAC24._CH', 0x00, 0x03E8)
    FadeIn(1000, 0)
    OP_12(0x00007D00, 0x0001FBD0, 0x00001B58)

    @scena.Lambda('lambda_10FF')
    def lambda_10FF():
        OP_67(0, 13250, -10000, 7000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_10FF)

    @scena.Lambda('lambda_1117')
    def lambda_1117():
        CameraSetDistance(3200, 7000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_1117)

    @scena.Lambda('lambda_1127')
    def lambda_1127():
        OP_6C(45000, 7000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_1127)

    Sleep(1000)

    Sleep(1000)

    Sleep(1000)

    Sleep(1000)

    Sleep(1000)

    Sleep(1000)

    MapSetFlags(0x02000000)
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_DC()
    SetScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    NewScene('ED6_DT21/E0900._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0009 offset: 0x116D
@scena.Code('func_09_116D')
def func_09_116D():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_11EA',
    )

    Sleep(400)

    ChrSetDirection(0x00FE, 90, 400)
    Sleep(400)

    ChrSetDirection(0x00FE, 315, 400)
    Sleep(500)

    OP_62(0x00FE, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrSetDirection(0x00FE, 270, 400)
    Sleep(1000)

    ChrSetDirection(0x00FE, 90, 400)
    Sleep(400)

    ChrSetDirection(0x00FE, 315, 400)
    Sleep(800)

    ChrSetDirection(0x00FE, 270, 400)
    Sleep(600)

    OP_62(0x00FE, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    Jump('func_09_116D')

    def _loc_11EA(): pass

    label('loc_11EA')

    Return()

# id: 0x000A offset: 0x11EB
@scena.Code('func_0A_11EB')
def func_0A_11EB():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1263',
    )

    OP_62(0x00FE, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrSetDirection(0x00FE, 180, 400)
    Sleep(600)

    ChrSetDirection(0x00FE, 225, 400)
    Sleep(400)

    ChrSetDirection(0x00FE, 270, 400)
    Sleep(800)

    ChrSetDirection(0x00FE, 225, 400)
    OP_62(0x00FE, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(400)

    ChrSetDirection(0x00FE, 180, 400)
    Sleep(600)

    ChrSetDirection(0x00FE, 135, 400)
    Sleep(800)

    Jump('func_0A_11EB')

    def _loc_1263(): pass

    label('loc_1263')

    Return()

# id: 0x000B offset: 0x1264
@scena.Code('func_0B_1264')
def func_0B_1264():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_12FC',
    )

    OP_62(0x00FE, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrWalkTo(0x00FE, -158060, 110, -44990, 2000, 0x00)
    ChrWalkTo(0x00FE, -158420, 80, -43410, 2000, 0x00)
    ChrSetDirection(0x00FE, 272, 400)
    Sleep(500)

    ChrWalkTo(0x00FE, -158060, 110, -44990, 2000, 0x00)
    OP_62(0x00FE, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrWalkTo(0x00FE, -159300, 120, -45800, 2000, 0x00)
    ChrSetDirection(0x00FE, 315, 400)
    Sleep(500)

    Jump('func_0B_1264')

    def _loc_12FC(): pass

    label('loc_12FC')

    Return()

# id: 0x000C offset: 0x12FD
@scena.Code('func_0C_12FD')
def func_0C_12FD():
    FadeOut(0, 0, -1)
    ClearScenaFlags(ScenaFlag(0x0240, 0, 0x1200))
    ClearScenaFlags(ScenaFlag(0x0240, 1, 0x1201))
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x09, 0xFF)

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
        (0x00000000, 'loc_137A'),
        (0x00000001, 'loc_1380'),
        (-1, 'loc_1386'),
    )

    def _loc_137A(): pass

    label('loc_137A')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_1386')

    def _loc_1380(): pass

    label('loc_1380')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_1386')

    def _loc_1386(): pass

    label('loc_1386')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_1394',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    Jump('loc_1398')

    def _loc_1394(): pass

    label('loc_1394')

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    def _loc_1398(): pass

    label('loc_1398')

    Return()

# id: 0x000D offset: 0x1399
@scena.Code('func_0D_1399')
def func_0D_1399():
    MapClearFlags(0x00000001)
    CameraMove(106730, -1920, 53920, 0)
    Sleep(100)

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['雪拉扎德'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['阿加特'],
            ChrTable['奥利维尔'],
            ChrTable['科洛丝'],
            ChrTable['提妲'],
            ChrTable['金'],
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
    OP_69(0x0000, 0)
    Sleep(1000)

    Return()

# id: 0x000E offset: 0x13EB
@scena.Code('func_0E_13EB')
def func_0E_13EB():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '南　帕赛尔农场',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
