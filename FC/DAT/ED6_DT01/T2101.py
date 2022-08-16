import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T2101_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2101   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'T2101.x'
    header.mapIndex       = 1
    header.bgm            = 12
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT01/T2101._SN', 'ED6_DT01/T2101_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
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
        ('ED6_DT07/CH01390._CH', 'ED6_DT07/CH01390P._CP'),
        ('ED6_DT07/CH02410._CH', 'ED6_DT07/CH02410P._CP'),
        ('ED6_DT07/CH02420._CH', 'ED6_DT07/CH02420P._CP'),
        ('ED6_DT07/CH02320._CH', 'ED6_DT07/CH02320P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH02063._CH', 'ED6_DT07/CH02063P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT07/CH01680._CH', 'ED6_DT07/CH01680P._CP'),
        ('ED6_DT07/CH01500._CH', 'ED6_DT07/CH01500P._CP'),
        ('ED6_DT07/CH01460._CH', 'ED6_DT07/CH01460P._CP'),
        ('ED6_DT07/CH01110._CH', 'ED6_DT07/CH01110P._CP'),
        ('ED6_DT07/CH02510._CH', 'ED6_DT07/CH02510P._CP'),
        ('ED6_DT07/CH02520._CH', 'ED6_DT07/CH02520P._CP'),
        ('ED6_DT07/CH02530._CH', 'ED6_DT07/CH02530P._CP'),
        ('ED6_DT06/CH20051._CH', 'ED6_DT06/CH20051P._CP'),
        ('ED6_DT06/CH20161._CH', 'ED6_DT06/CH20161P._CP'),
    ]

# id: 0x10001 offset: 0x12A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '迪恩',
            x                   = 1200,
            z                   = 4000,
            y                   = 16700,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '雷斯',
            x                   = 1200,
            z                   = 4000,
            y                   = 16700,
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
            name                = '洛克',
            x                   = 1200,
            z                   = 4000,
            y                   = 16700,
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
            name                = '皮卡罗',
            x                   = 49950,
            z                   = 1000,
            y                   = 2460,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            name                = '戴尔蒙市长',
            x                   = 1200,
            z                   = 4000,
            y                   = 16700,
            direction           = 180,
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
            name                = '秘书基尔巴特',
            x                   = 1200,
            z                   = 4000,
            y                   = 16700,
            direction           = 180,
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
            name                = '基库',
            x                   = 800,
            z                   = 6000,
            y                   = -13810,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '哈古',
            x                   = 4620,
            z                   = -1800,
            y                   = 22750,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0000,
        ),
        ScenaNpcData(
            name                = '照相机',
            x                   = 800,
            z                   = 6000,
            y                   = -13810,
            direction           = 180,
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
            name                = '布诺安',
            x                   = 15900,
            z                   = -1800,
            y                   = 25200,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '奈尔',
            x                   = 65090,
            z                   = -1700,
            y                   = 32900,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x01D5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '西蒙',
            x                   = 24700,
            z                   = 0,
            y                   = 24500,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '波尔多斯',
            x                   = 20070,
            z                   = 0,
            y                   = 26530,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '昆茨',
            x                   = 7100,
            z                   = 0,
            y                   = 28900,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '布兰塔婆婆',
            x                   = 58900,
            z                   = 0,
            y                   = 29500,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '船',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0080,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '波尔多斯',
            x                   = 23560,
            z                   = 1000,
            y                   = 1760,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '阿伊纳街道方向',
            x                   = 73210,
            z                   = 0,
            y                   = -16650,
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
            name                = '卢安市·北街区',
            x                   = 50980,
            z                   = 400,
            y                   = 77990,
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
    )

# id: 0x10003 offset: 0x38A
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 32790,
            y           = 2000,
            z           = 13300,
            range       = 26260,
            dword_10    = 0xFFFFFC18,
            dword_14    = 0x00002ADA,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000000B,
        ),
        ScenaEventData(
            x           = 49000,
            y           = 2000,
            z           = 26550,
            range       = 46940,
            dword_10    = 0xFFFFFC18,
            dword_14    = 0x00004B82,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000000C,
        ),
        ScenaEventData(
            x           = 76190,
            y           = 0,
            z           = 0,
            range       = 70000,
            dword_10    = 0x000007D0,
            dword_14    = 0xFFFFF830,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000000E,
        ),
        ScenaEventData(
            x           = 31200,
            y           = 0,
            z           = 25340,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000011,
        ),
        ScenaEventData(
            x           = 77280,
            y           = 0,
            z           = 22060,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000012,
        ),
    )

# id: 0x10004 offset: 0x42A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 41040,
            triggerZ            = -1650,
            triggerY            = 32140,
            triggerRange        = 1400,
            actorX              = 41040,
            actorZ              = -6350,
            actorY              = 32140,
            flags               = 0x007C,
            talkScenaIndex      = 0x0001,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 17000,
            triggerZ            = 0,
            triggerY            = 29200,
            triggerRange        = 3500,
            actorX              = 17050,
            actorZ              = 3500,
            actorY              = 29200,
            flags               = 0x007C,
            talkScenaIndex      = 0x0001,
            talkFunctionIndex   = 0x0009,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 50320,
            triggerZ            = 1000,
            triggerY            = 2450,
            triggerRange        = 800,
            actorX              = 50320,
            actorZ              = 2000,
            actorY              = 2450,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000F,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 50320,
            triggerZ            = 1000,
            triggerY            = 9400,
            triggerRange        = 800,
            actorX              = 50320,
            actorZ              = 2000,
            actorY              = 9400,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000F,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 31960,
            triggerZ            = 1000,
            triggerY            = 3430,
            triggerRange        = 800,
            actorX              = 31960,
            actorZ              = 2000,
            actorY              = 3430,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000F,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 23540,
            triggerZ            = 1000,
            triggerY            = 3430,
            triggerRange        = 800,
            actorX              = 23540,
            actorZ              = 2000,
            actorY              = 3430,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000F,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x502
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_516',
    )

    ChrSetFlags(0x0013, 0x0080)
    ChrSetFlags(0x0013, 0x0008)

    Jump('loc_579')

    def _loc_516(): pass

    label('loc_516')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_53B',
    )

    ChrSetPos(0x0015, 19270, 0, 30790, 225)
    ChrSetFlags(0x0013, 0x0080)
    ChrSetFlags(0x0013, 0x0008)

    Jump('loc_579')

    def _loc_53B(): pass

    label('loc_53B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_559',
    )

    ChrSetFlags(0x0013, 0x0080)
    ChrSetFlags(0x0013, 0x0008)
    ChrSetFlags(0x000F, 0x0080)
    ChrSetFlags(0x000F, 0x0008)

    Jump('loc_579')

    def _loc_559(): pass

    label('loc_559')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_568',
    )

    ChrClearFlags(0x0012, 0x0080)

    Jump('loc_579')

    def _loc_568(): pass

    label('loc_568')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 4, 0x414)),
            Expr.Return,
        ),
        'loc_579',
    )

    ChrSetFlags(0x0014, 0x0080)
    ChrSetFlags(0x0014, 0x0008)

    def _loc_579(): pass

    label('loc_579')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_587',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, func_0D_4D94)

    def _loc_587(): pass

    label('loc_587')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 7, 0x417)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_594',
    )

    ChrClearFlags(0x000B, 0x0080)

    def _loc_594(): pass

    label('loc_594')

    ExecExpressionWithValue(
        0x000E,
        0x28,
        (
            (Expr.PushLong, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0001 offset: 0x5A6
@scena.Code('func_01_5A6')
def func_01_5A6():
    OP_16(0x02, 4000, -88000, -100000, 196680)
    OP_72(0x0016, 0x0010)
    OP_6F(0x0016, 60)
    OP_71(0x0018, 0x0004)
    OP_71(0x0019, 0x0004)
    OP_71(0x001A, 0x0004)
    OP_71(0x001B, 0x0004)
    OP_71(0x001C, 0x0004)
    OP_71(0x001D, 0x0004)
    OP_71(0x001E, 0x0004)
    OP_71(0x001F, 0x0004)
    OP_72(0x0014, 0x0010)
    OP_72(0x0015, 0x0010)
    OP_64(0x02, 0x0001)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 7, 0x417)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_60E',
    )

    OP_72(0x0013, 0x0010)
    OP_65(0x02, 0x0001)

    Jump('loc_613')

    def _loc_60E(): pass

    label('loc_60E')

    OP_1C(0x13, 0x00, 0x0010)

    def _loc_613(): pass

    label('loc_613')

    If(
        (
            (Expr.Eval, "OP_29(0x0021, 0x00, 0x04)"),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x0021, 0x01, 0x0010)"),
            Expr.Or,
            (Expr.Eval, "OP_29(0x0021, 0x00, 0x40)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_631',
    )

    OP_64(0x00, 0x0001)

    def _loc_631(): pass

    label('loc_631')

    If(
        (
            (Expr.Eval, "OP_29(0x0020, 0x01, 0x0010)"),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x0020, 0x00, 0x40)"),
            Expr.Or,
            (Expr.Eval, "OP_29(0x0020, 0x01, 0x8000)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_650',
    )

    OP_64(0x01, 0x0001)

    def _loc_650(): pass

    label('loc_650')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 4, 0x43C)),
            Expr.Return,
        ),
        'loc_65A',
    )

    Jump('loc_6E3')

    def _loc_65A(): pass

    label('loc_65A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            Expr.Return,
        ),
        'loc_670',
    )

    OP_6F(0x0011, 1020)
    OP_72(0x0021, 0x0002)

    Jump('loc_6E3')

    def _loc_670(): pass

    label('loc_670')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_67A',
    )

    Jump('loc_6E3')

    def _loc_67A(): pass

    label('loc_67A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 4, 0x42C)),
            Expr.Return,
        ),
        'loc_690',
    )

    OP_6F(0x0011, 1020)
    OP_72(0x0021, 0x0002)

    Jump('loc_6E3')

    def _loc_690(): pass

    label('loc_690')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 2, 0x42A)),
            Expr.Return,
        ),
        'loc_6A6',
    )

    OP_6F(0x0011, 1020)
    OP_72(0x0021, 0x0002)

    Jump('loc_6E3')

    def _loc_6A6(): pass

    label('loc_6A6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 6, 0x41E)),
            Expr.Return,
        ),
        'loc_6B0',
    )

    Jump('loc_6E3')

    def _loc_6B0(): pass

    label('loc_6B0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_6BA',
    )

    Jump('loc_6E3')

    def _loc_6BA(): pass

    label('loc_6BA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 1, 0x419)),
            Expr.Return,
        ),
        'loc_6D0',
    )

    OP_6F(0x0011, 1020)
    OP_72(0x0021, 0x0002)

    Jump('loc_6E3')

    def _loc_6D0(): pass

    label('loc_6D0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 0, 0x418)),
            Expr.Return,
        ),
        'loc_6E3',
    )

    OP_6F(0x0011, 1020)
    OP_72(0x0021, 0x0002)

    def _loc_6E3(): pass

    label('loc_6E3')

    If(
        (
            (Expr.Eval, "OP_29(0x0021, 0x00, 0x04)"),
            (Expr.Eval, "OP_29(0x0021, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0021, 0x01, 0x0010)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_747',
    )

    LoadEffect(0x00, 'map\\\\mp022_00.eff')
    PlayEffect(0x00, 0xFF, 0x00FF, 41040, -6550, 32140, 0, 0, 0, 2500, 2500, 2500, 0x00FF, 0, 0, 0, 0)

    def _loc_747(): pass

    label('loc_747')

    PlaySE(453, 0x01, 0x64)

    Return()

# id: 0x0002 offset: 0x74D
@scena.Code('func_02_74D')
def func_02_74D():
    ExecExpressionWithReg(
        0x0000,
        (
            Expr.Rand,
            (Expr.PushLong, 0xE),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_772',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_8B4')

    def _loc_772(): pass

    label('loc_772')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_78B',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_8B4')

    def _loc_78B(): pass

    label('loc_78B')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7A4',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_8B4')

    def _loc_7A4(): pass

    label('loc_7A4')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7BD',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_8B4')

    def _loc_7BD(): pass

    label('loc_7BD')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7D6',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_8B4')

    def _loc_7D6(): pass

    label('loc_7D6')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7EF',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_8B4')

    def _loc_7EF(): pass

    label('loc_7EF')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_808',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_8B4')

    def _loc_808(): pass

    label('loc_808')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_821',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_8B4')

    def _loc_821(): pass

    label('loc_821')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_83A',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_8B4')

    def _loc_83A(): pass

    label('loc_83A')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_853',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_8B4')

    def _loc_853(): pass

    label('loc_853')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_86C',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_8B4')

    def _loc_86C(): pass

    label('loc_86C')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_885',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_8B4')

    def _loc_885(): pass

    label('loc_885')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_89E',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_8B4')

    def _loc_89E(): pass

    label('loc_89E')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8B4',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_8B4(): pass

    label('loc_8B4')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_8C9',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_8B4')

    def _loc_8C9(): pass

    label('loc_8C9')

    Return()

# id: 0x0003 offset: 0x8CA
@scena.Code('func_03_8CA')
def func_03_8CA():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B37',
    )

    EventBegin(0x00)
    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '#1480040996V……为、为什么在这种地方\n',
            '会有年轻的女孩子……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1480040997V不行不行，你们不许进入！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1480040998V这、这可不是你们\n',
            '这些小鬼可以来的地方！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040999V#004F你误会了吧，\n',
            '我们可没说要进去啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010041000V#000F这位大哥，\n',
            '你为什么这么紧张呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1480041001V果、果然\n',
            '能看得出我很紧张吗……？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1480041002V……不对，\n',
            '总之这里不许进入！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1480041003V赶快去别的地方吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020041004V#015F（呼……\n',
            '　我觉得还是不要去管他比较好……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010041005V#009F（嗯，这人穿得这么奇怪，\n',
            '　到底是什么人呢？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0136,
        (
            '#0060041006V#043F（…………………………）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0088, 7, 0x447))
    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))
    EventEnd(0x01)

    Jump('loc_B7C')

    def _loc_B37(): pass

    label('loc_B37')

    ChrTalk(
        0x00FE,
        (
            '总、总之这里不许进入！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '这、这可不是\n',
            '你们这些小鬼可以来的地方！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B7C(): pass

    label('loc_B7C')

    TalkEnd(0x000B)

    Return()

# id: 0x0004 offset: 0xB80
@scena.Code('func_04_B80')
def func_04_B80():
    TalkBegin(0x0011)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_CB5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C3A',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '戴尔蒙市长\n',
            '只重视观光业。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他从来不会考虑\n',
            '为港口更换新的设备。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '主任也应该明白。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '干脆让波尔多斯主任\n',
            '来当市长更好啦，\n',
            '那样我们也能够安心地工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CB2')

    def _loc_C3A(): pass

    label('loc_C3A')

    ChrTalk(
        0x00FE,
        (
            '戴尔蒙市长\n',
            '从来都不会考虑\n',
            '为港口更换新的设备。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '干脆让波尔多斯主任\n',
            '来当市长更好啦，\n',
            '那样我们也能够安心地工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_CB2(): pass

    label('loc_CB2')

    Jump('loc_F1F')

    def _loc_CB5(): pass

    label('loc_CB5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_D15',
    )

    ChrTalk(
        0x00FE,
        (
            '最近这几天，\n',
            '完全看不到那些不良青年的身影。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '难道说他们已经\n',
            '被市长赶出去了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F1F')

    def _loc_D15(): pass

    label('loc_D15')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_D84',
    )

    ChrTalk(
        0x00FE,
        (
            '仓库那帮人正当年青，\n',
            '却不好好干活。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最终还是要靠别人养活，\n',
            '那副狼狈相，\n',
            '父母哭都哭不出来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F1F')

    def _loc_D84(): pass

    label('loc_D84')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_DE6',
    )

    ChrTalk(
        0x00FE,
        (
            '刚才，渡鸦帮那些家伙\n',
            '不知为什么在吵吵闹闹的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '反正又干了些\n',
            '不入流的事情吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F1F')

    def _loc_DE6(): pass

    label('loc_DE6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_E50',
    )

    ChrTalk(
        0x00FE,
        (
            '市长为什么放任\n',
            '渡鸦帮那些家伙们不管啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样让他们任意妄为，\n',
            '只会让他们更加得意忘形。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F1F')

    def _loc_E50(): pass

    label('loc_E50')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 4, 0x414)),
            Expr.Return,
        ),
        'loc_F1F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_ECD',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '你们是旅游者吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我话说在前面，\n',
            '你们可千万别靠近仓库那里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那一带集中了\n',
            '不少不良青年哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F1F')

    def _loc_ECD(): pass

    label('loc_ECD')

    ChrTalk(
        0x00FE,
        (
            '我话说在前面，\n',
            '你们可千万别靠近仓库那里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那一带集中了\n',
            '不少不良青年哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F1F(): pass

    label('loc_F1F')

    TalkEnd(0x0011)

    Return()

# id: 0x0005 offset: 0xF23
@scena.Code('func_05_F23')
def func_05_F23():
    TalkBegin(0x0015)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_102B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_FCC',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '渡鸦帮的那些家伙\n',
            '好像都回到城里来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '也许是心理作用，\n',
            '看起来他们好像无精打采的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这种时候只要活动一下身体，\n',
            '就会感觉心情舒畅了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1028')

    def _loc_FCC(): pass

    label('loc_FCC')

    ChrTalk(
        0x00FE,
        (
            '渡鸦帮的那些家伙\n',
            '好像都回到城里来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '也许是心理作用，\n',
            '看起来他们好像无精打采的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1028(): pass

    label('loc_1028')

    Jump('loc_11FD')

    def _loc_102B(): pass

    label('loc_102B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_10A6',
    )

    ChrTalk(
        0x00FE,
        (
            '波尔多斯主任\n',
            '又在为什么事情烦恼了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有时不要有太多烦恼，\n',
            '偶尔也运动一下，\n',
            '说不定会想出什么好点子来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11FD')

    def _loc_10A6(): pass

    label('loc_10A6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_10FB',
    )

    ChrTalk(
        0x00FE,
        (
            '最近机器的情况不太好啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还是请蔡斯的技术人员\n',
            '过来检查一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11FD')

    def _loc_10FB(): pass

    label('loc_10FB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_1139',
    )

    ChrTalk(
        0x00FE,
        (
            '哦，开合桥吊起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '差不多到吃饭时间了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11FD')

    def _loc_1139(): pass

    label('loc_1139')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_1185',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，\n',
            '今天过得真是很充实啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我果然适合\n',
            '做这些体力活呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11FD')

    def _loc_1185(): pass

    label('loc_1185')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 4, 0x414)),
            Expr.Return,
        ),
        'loc_11FD',
    )

    ChrTalk(
        0x00FE,
        (
            '这里是将从国外运来的物资\n',
            '卸下船的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '进口的货物\n',
            '在这里办理好通关手续之后，\n',
            '就可以运往利贝尔各地了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_11FD(): pass

    label('loc_11FD')

    TalkEnd(0x0015)

    Return()

# id: 0x0006 offset: 0x1201
@scena.Code('func_06_1201')
def func_06_1201():
    TalkBegin(0x000F)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_13AC',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0021, 0x00, 0x10)"),
            (Expr.Eval, "OP_29(0x0021, 0x01, 0x8000)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1272',
    )

    OP_28(0x0021, 0x01, 0x8000)

    ChrTalk(
        0x00FE,
        (
            '哦，之前真是谢谢你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果再遇到什么困难，\n',
            '还是要拜托你们哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_13A9')

    def _loc_1272(): pass

    label('loc_1272')

    If(
        (
            (Expr.Eval, "OP_29(0x0020, 0x00, 0x10)"),
            (Expr.Eval, "OP_29(0x0021, 0x01, 0x4000)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_132A',
    )

    OP_28(0x0021, 0x01, 0x4000)

    ChrTalk(
        0x00FE,
        (
            '呼，\n',
            '我还是觉得那个假扮的主任\n',
            '和真的波尔多斯主任一模一样呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不只是外形，\n',
            '连说话的方式和态度也都完全一样呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这个世上还有\n',
            '这么厉害的家伙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_13A9')

    def _loc_132A(): pass

    label('loc_132A')

    ChrTalk(
        0x00FE,
        (
            '看到波尔多斯主任那么辛苦，\n',
            '真是十分过意不去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但要是发生什么问题的话，\n',
            '能解决问题的人也还是\n',
            '只有波尔多斯主任一个啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_13A9(): pass

    label('loc_13A9')

    Jump('loc_1981')

    def _loc_13AC(): pass

    label('loc_13AC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_15D7',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0021, 0x00, 0x10)"),
            (Expr.Eval, "OP_29(0x0021, 0x01, 0x8000)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_141A',
    )

    OP_28(0x0021, 0x01, 0x8000)

    ChrTalk(
        0x00FE,
        (
            '哦，之前真是谢谢你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果再遇到什么困难，\n',
            '还是要拜托你们哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15D4')

    def _loc_141A(): pass

    label('loc_141A')

    If(
        (
            (Expr.Eval, "OP_29(0x0020, 0x00, 0x10)"),
            (Expr.Eval, "OP_29(0x0021, 0x01, 0x4000)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_14D2',
    )

    OP_28(0x0021, 0x01, 0x4000)

    ChrTalk(
        0x00FE,
        (
            '呼，\n',
            '我还是觉得那个假扮的主任\n',
            '和真的波尔多斯主任一模一样呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不只是外形，\n',
            '连说话的方式和态度也都完全一样呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这个世上还有\n',
            '这么厉害的家伙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15D4')

    def _loc_14D2(): pass

    label('loc_14D2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1582',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '波尔多斯主任\n',
            '虽然外表看上去有点呆呆的，\n',
            '但实际上他头脑很灵活，而且很负责任。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '无论哪个方面\n',
            '他都非常为我们着想。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不管怎么说，\n',
            '我们对主任都十分敬仰。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15D4')

    def _loc_1582(): pass

    label('loc_1582')

    ChrTalk(
        0x00FE,
        (
            '波尔多斯主任\n',
            '虽然外表看上去有点呆呆的，\n',
            '但实际上他头脑很灵活，而且很负责任。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_15D4(): pass

    label('loc_15D4')

    Jump('loc_1981')

    def _loc_15D7(): pass

    label('loc_15D7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_1801',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0021, 0x00, 0x10)"),
            (Expr.Eval, "OP_29(0x0021, 0x01, 0x8000)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1645',
    )

    OP_28(0x0021, 0x01, 0x8000)

    ChrTalk(
        0x00FE,
        (
            '哦，之前真是谢谢你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果再遇到什么困难，\n',
            '还是要拜托你们哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17FE')

    def _loc_1645(): pass

    label('loc_1645')

    If(
        (
            (Expr.Eval, "OP_29(0x0020, 0x00, 0x10)"),
            (Expr.Eval, "OP_29(0x0021, 0x01, 0x4000)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_16FD',
    )

    OP_28(0x0021, 0x01, 0x4000)

    ChrTalk(
        0x00FE,
        (
            '呼，\n',
            '我还是觉得那个假扮的主任\n',
            '和真的波尔多斯主任一模一样呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不只是外形，\n',
            '连说话的方式和态度也都完全一样呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这个世上还有\n',
            '这么厉害的家伙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17FE')

    def _loc_16FD(): pass

    label('loc_16FD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1798',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '唔～\n',
            '下一艘要到达的是共和国的船只吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果被近海的渔船干扰了进港，\n',
            '就是波尔多斯主任的责任了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果海港能\n',
            '再扩大一些就好了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17FE')

    def _loc_1798(): pass

    label('loc_1798')

    ChrTalk(
        0x00FE,
        (
            '唔～\n',
            '下一艘要到达的是共和国的船只。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果被近海的渔船干扰了进港，\n',
            '就是波尔多斯主任的责任了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_17FE(): pass

    label('loc_17FE')

    Jump('loc_1981')

    def _loc_1801(): pass

    label('loc_1801')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_1832',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯～\n',
            '先赶快把这边的货物处理好吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1981')

    def _loc_1832(): pass

    label('loc_1832')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_18D2',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0021, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_1885',
    )

    ChrTalk(
        0x00FE,
        (
            '谢谢你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果再遇到什么困难，\n',
            '还是要拜托你们哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_18CF')

    def _loc_1885(): pass

    label('loc_1885')

    ChrTalk(
        0x00FE,
        (
            '伤脑筋了。\n',
            '掉在哪里了呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在被他发现之前，\n',
            '要赶快找到才行……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_18CF(): pass

    label('loc_18CF')

    Jump('loc_1981')

    def _loc_18D2(): pass

    label('loc_18D2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 4, 0x414)),
            Expr.Return,
        ),
        'loc_192E',
    )

    ChrTalk(
        0x00FE,
        (
            '今天该轮到\n',
            '我来保管仓库的钥匙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '必须去波尔多斯主任那里\n',
            '把钥匙拿过来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1981')

    def _loc_192E(): pass

    label('loc_192E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_1981',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯～\n',
            '这些是从帝国运来的集装箱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要把它们装载到\n',
            '去蔡斯的定期船上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1981(): pass

    label('loc_1981')

    TalkEnd(0x000F)

    Return()

# id: 0x0007 offset: 0x1985
@scena.Code('func_07_1985')
def func_07_1985():
    TalkBegin(0x0016)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_1AFA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1A77',
    )

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x00FE,
        (
            '市长竟然会\n',
            '犯下这么多的罪行，\n',
            '看来戴尔蒙家族也没落了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样的话，\n',
            '选举下任市长就要注意点了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '相比之下，\n',
            '我更加担心那些孩子们啊。\n',
            '孤儿院被烧掉之后该怎么办呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '像我这样的老太婆\n',
            '什么忙也帮不上啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AF7')

    def _loc_1A77(): pass

    label('loc_1A77')

    ChrTalk(
        0x00FE,
        (
            '市长竟然会\n',
            '犯下这么多的罪行，\n',
            '看来戴尔蒙家族也没落了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说起来我更加\n',
            '担心那些孩子们啊。\n',
            '孤儿院被烧掉之后该怎么办呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1AF7(): pass

    label('loc_1AF7')

    Jump('loc_1F69')

    def _loc_1AFA(): pass

    label('loc_1AFA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_1BD2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1B7F',
    )

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x00FE,
        (
            '有一个穿着气派却带有低级趣味的男人\n',
            '进入了市长官邸。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……说起来，\n',
            '听说有位某地的达官贵人会在卢安停留。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1BCF')

    def _loc_1B7F(): pass

    label('loc_1B7F')

    ChrTalk(
        0x00FE,
        (
            '就在刚才，\n',
            '有个虽看上去很有气派但穿着却\n',
            '带有低级趣味的男人进入了市长官邸。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1BCF(): pass

    label('loc_1BCF')

    Jump('loc_1F69')

    def _loc_1BD2(): pass

    label('loc_1BD2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_1CC8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1C7F',
    )

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x00FE,
        (
            '今天的天气也很好啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我小时候总是在这里\n',
            '看着外国的船进进出出，\n',
            '从来都不会觉得看腻了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '港口的周围\n',
            '有很多市场和摊贩，\n',
            '那才叫充满活力啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1CC5')

    def _loc_1C7F(): pass

    label('loc_1C7F')

    ChrTalk(
        0x00FE,
        (
            '我小时候总是在这里\n',
            '看着外国的船进进出出，\n',
            '从来都不会觉得看腻了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1CC5(): pass

    label('loc_1CC5')

    Jump('loc_1F69')

    def _loc_1CC8(): pass

    label('loc_1CC8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_1DE9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1D79',
    )

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x00FE,
        (
            '戴尔蒙市长非常积极地\n',
            '发展卢安的观光业。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他好像准备以此带动\n',
            '全市各项事业的发展呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这里原本是\n',
            '以港口城市而繁荣起来的，\n',
            '这就是时代的变迁吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1DE6')

    def _loc_1D79(): pass

    label('loc_1D79')

    ChrTalk(
        0x00FE,
        (
            '戴尔蒙市长非常积极地\n',
            '发展卢安的观光业。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这里原本是\n',
            '以港口城市而繁荣起来的，\n',
            '这就是时代的变迁吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1DE6(): pass

    label('loc_1DE6')

    Jump('loc_1F69')

    def _loc_1DE9(): pass

    label('loc_1DE9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_1EDF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1E8C',
    )

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x00FE,
        (
            '河川的这边\n',
            '不是有座非常漂亮的住宅吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那是卢安市长\n',
            '戴尔蒙先生的官邸。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '卢安的市长一职\n',
            '是由曾为贵族的\n',
            '戴尔蒙家的主人代代相传的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1EDC')

    def _loc_1E8C(): pass

    label('loc_1E8C')

    ChrTalk(
        0x00FE,
        (
            '河川的这边\n',
            '不是有座非常漂亮的住宅吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那是卢安市长\n',
            '戴尔蒙先生的官邸。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1EDC(): pass

    label('loc_1EDC')

    Jump('loc_1F69')

    def _loc_1EDF(): pass

    label('loc_1EDF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 4, 0x414)),
            Expr.Return,
        ),
        'loc_1F69',
    )

    ChrTalk(
        0x00FE,
        (
            '在河的对岸那边\n',
            '集中了本市的商业和观光设施，\n',
            '那些都是最近才发展起来的产业。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '河岸这边则在很早以前\n',
            '就是港湾设施和住宅区了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1F69(): pass

    label('loc_1F69')

    TalkEnd(0x0016)

    Return()

# id: 0x0008 offset: 0x1F6D
@scena.Code('func_08_1F6D')
def func_08_1F6D():
    TalkBegin(0x0012)

    ChrTalk(
        0x00FE,
        (
            '#0270050061V#140F……接下来，\n',
            '该怎样继续调查比较好呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270050062V还是要靠这双脚\n',
            '去现场调查才行吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0012)

    Return()

# id: 0x0009 offset: 0x1FDF
@scena.Code('func_09_1FDF')
def func_09_1FDF():
    TalkBegin(0x0013)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_2119',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_20A2',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '以前一提起卢安，\n',
            '就是贸易与渔业发达的城市。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最繁荣的是这个港口，\n',
            '可不是如今那么兴盛的观光业。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '自从戴尔蒙市长就任以来，\n',
            '这里给人的印象就完全成了旅游城市了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2116')

    def _loc_20A2(): pass

    label('loc_20A2')

    ChrTalk(
        0x00FE,
        (
            '以前一提起卢安，\n',
            '就是贸易与渔业发达的城市。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '自从戴尔蒙市长就任以来，\n',
            '这里给人的印象就完全成了旅游城市了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2116(): pass

    label('loc_2116')

    Jump('loc_222D')

    def _loc_2119(): pass

    label('loc_2119')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 0, 0x418)),
            Expr.Return,
        ),
        'loc_21B4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_217D',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '嗯……\n',
            '货物没有问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '必须要赶快\n',
            '办好通关手续，\n',
            '把集装箱送到柏斯去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_21B1')

    def _loc_217D(): pass

    label('loc_217D')

    ChrTalk(
        0x00FE,
        (
            '必须要赶快\n',
            '办好通关手续，\n',
            '把集装箱送到柏斯去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_21B1(): pass

    label('loc_21B1')

    Jump('loc_222D')

    def _loc_21B4(): pass

    label('loc_21B4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_222D',
    )

    ChrTalk(
        0x00FE,
        (
            '虽说飞艇可以运送大量的商品，\n',
            '但是所需经费也是大量的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果不是什么急需的商品，\n',
            '我还是会采用海运的方式。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_222D(): pass

    label('loc_222D')

    TalkEnd(0x0013)

    Return()

# id: 0x000A offset: 0x2231
@scena.Code('func_0A_2231')
def func_0A_2231():
    TalkBegin(0x0014)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_241F',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0020, 0x00, 0x10)"),
            (Expr.Eval, "OP_29(0x0020, 0x01, 0x4000)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_233F',
    )

    OP_28(0x0020, 0x01, 0x4000)

    ChrTalk(
        0x00FE,
        (
            '哟，是你们啊，\n',
            '我不知道仓库的事，\n',
            '随便向你们发火实在对不起。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看来那个冒牌货\n',
            '就像扎古所说的那样，\n',
            '无论哪个方面都和我一模一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔，真可惜。\n',
            '要是你们能把他捉起来的话，\n',
            '一定能得到许多赏金……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈哈哈，我是开玩笑的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_241C')

    def _loc_233F(): pass

    label('loc_233F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_23C4',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '真没想到市长\n',
            '会落得那样的下场。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '本来还想和他商量一下，\n',
            '重新评估港口设备呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔，\n',
            '现在要怎么办才好呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_241C')

    def _loc_23C4(): pass

    label('loc_23C4')

    ChrTalk(
        0x00FE,
        (
            '真没想到市长\n',
            '会落得那样的下场。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '本来还想和他商量一下，\n',
            '重新评估港口设备呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_241C(): pass

    label('loc_241C')

    Jump('loc_2952')

    def _loc_241F(): pass

    label('loc_241F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_262E',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0020, 0x00, 0x10)"),
            (Expr.Eval, "OP_29(0x0020, 0x01, 0x4000)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_252A',
    )

    OP_28(0x0020, 0x01, 0x4000)

    ChrTalk(
        0x00FE,
        (
            '哟，是你们啊，\n',
            '我不知道仓库的事，\n',
            '随便向你们发火实在对不起。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看来那个冒牌货\n',
            '就像扎古所说的那样，\n',
            '无论哪个方面都和我一模一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔，真可惜。\n',
            '要是你们能把他捉起来的话，\n',
            '一定能得到许多赏金……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈哈哈，我是开玩笑的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_262B')

    def _loc_252A(): pass

    label('loc_252A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_25C7',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '这台起重机也很旧了，\n',
            '也该是换一台新机器的时候了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '果然，还是要和市长谈谈\n',
            '港湾设施的问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎呀哎呀，\n',
            '事情变得越来越麻烦了呀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_262B')

    def _loc_25C7(): pass

    label('loc_25C7')

    ChrTalk(
        0x00FE,
        (
            '这台起重机也很旧了，\n',
            '也该是换一台新机器的时候了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '果然，还是要和市长谈谈\n',
            '港湾设施的问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_262B(): pass

    label('loc_262B')

    Jump('loc_2952')

    def _loc_262E(): pass

    label('loc_262E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_278B',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0020, 0x00, 0x10)"),
            (Expr.Eval, "OP_29(0x0020, 0x01, 0x4000)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2739',
    )

    OP_28(0x0020, 0x01, 0x4000)

    ChrTalk(
        0x00FE,
        (
            '哟，是你们啊，\n',
            '我不知道仓库的事，\n',
            '随便向你们发火实在对不起。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看来那个冒牌货\n',
            '就像扎古所说的那样，\n',
            '无论哪个方面都和我一模一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔，真可惜。\n',
            '要是你们能把他捉起来的话，\n',
            '一定能得到许多赏金……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈哈哈，我是开玩笑的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2788')

    def _loc_2739(): pass

    label('loc_2739')

    ChrTalk(
        0x00FE,
        (
            '这里的设施也开始\n',
            '慢慢变得老化了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎呀哎呀，有太多事情让我烦恼了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2788(): pass

    label('loc_2788')

    Jump('loc_2952')

    def _loc_278B(): pass

    label('loc_278B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_2850',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_280F',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '我以前拜托过市长，\n',
            '恳请他处理一下\n',
            '盘踞在仓库的那些人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在一点音讯都没有。\n',
            '哎呀哎呀，真是麻烦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_284D')

    def _loc_280F(): pass

    label('loc_280F')

    ChrTalk(
        0x00FE,
        (
            '我以前拜托过市长，\n',
            '恳请他处理一下\n',
            '盘踞在仓库的那些人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_284D(): pass

    label('loc_284D')

    Jump('loc_2952')

    def _loc_2850(): pass

    label('loc_2850')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_2952',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_28F2',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '这里有许多即将\n',
            '装运上外国船只的货物……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如今这个年代，\n',
            '出口最多的果然是导力制品啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说起利贝尔制的导力器，\n',
            '可是世界闻名的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2952')

    def _loc_28F2(): pass

    label('loc_28F2')

    ChrTalk(
        0x00FE,
        (
            '外国船只运走的货物\n',
            '果然要数导力制品最多啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说起利贝尔制的导力器，\n',
            '可是世界闻名的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2952(): pass

    label('loc_2952')

    TalkEnd(0x0014)

    Return()

# id: 0x000B offset: 0x2956
@scena.Code('func_0B_2956')
def func_0B_2956():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 6, 0x416)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2BCC',
    )

    SetScenaFlags(ScenaFlag(0x0082, 6, 0x416))
    EventBegin(0x00)

    ExecExpressionWithValue(
        0x0136,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0136,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_297F')
    def lambda_297F():
        OP_6C(156000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_297F)

    @scena.Lambda('lambda_298F')
    def lambda_298F():
        CameraSetDistance(4100, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_298F)

    @scena.Lambda('lambda_299F')
    def lambda_299F():
        CameraMove(28940, 0, 430, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_299F)

    Sleep(5000)

    Fade(1000)
    OP_6C(135000, 0)
    CameraSetDistance(2800, 0)
    CameraMove(29580, 0, 8940, 0)
    ChrSetPos(0x0101, 29440, 0, 8189, 180)
    ChrSetPos(0x0102, 30100, 0, 9570, 180)
    ChrSetPos(0x0136, 28520, 0, 9990, 180)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010040988V#004F这里好像\n',
            '尽是些大型的建筑物啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0136,
        (
            '#0060040989V#040F这里是仓库区域哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060040990V从外国运来的货物\n',
            '和其他物品都是保管在这里的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040991V#000F嗯……\n',
            '不过，这里有点冷清呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0136,
        (
            '#0060040992V#040F因为自从飞艇普及之后，\n',
            '只能在水面上行走的轮船\n',
            '就用得越来越少了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060040993V听说和过去相比，\n',
            '这里的卸货量减少了很多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040994V#000F这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040995V#010F果然， \n',
            '好像还有很多仓库闲置着呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    def _loc_2BCC(): pass

    label('loc_2BCC')

    Return()

# id: 0x000C offset: 0x2BCD
@scena.Code('func_0C_2BCD')
def func_0C_2BCD():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0088, 7, 0x447)),
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 7, 0x417)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4D93',
    )

    SetScenaFlags(ScenaFlag(0x0082, 7, 0x417))
    EventBegin(0x00)

    ExecExpressionWithValue(
        0x0136,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0136,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetFlags(0x0008, 0x0040)
    ChrSetFlags(0x0009, 0x0040)
    ChrSetFlags(0x000A, 0x0040)
    ChrSetFlags(0x000C, 0x0040)
    ChrSetFlags(0x000D, 0x0040)
    ChrSetPos(0x000C, 50970, 0, 35000, 0)
    ChrSetPos(0x000D, 50970, 0, 34260, 0)
    ChrSetPos(0x0008, 37400, 0, 23790, 0)
    ChrSetPos(0x0009, 37400, 0, 21720, 0)
    ChrSetPos(0x000A, 37400, 0, 22740, 0)

    NpcTalk(
        0x0008,
        '年轻人的声音',
        (
            '#0450041009V慢着，小姑娘。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(1000)
    CameraMove(48730, 0, 23120, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(315000, 0)
    OP_6E(261, 0)
    ChrSetPos(0x0101, 50170, 0, 23370, 270)
    ChrSetPos(0x0102, 50380, 0, 22120, 270)
    ChrSetPos(0x0136, 51330, 0, 22810, 270)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)

    @scena.Lambda('lambda_2D1E')
    def lambda_2D1E():
        ChrWalkTo(0x00FE, 48280, 0, 23780, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2D1E)

    Sleep(200)

    @scena.Lambda('lambda_2D3E')
    def lambda_2D3E():
        ChrWalkTo(0x00FE, 48040, 0, 21720, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_2D3E)

    Sleep(200)

    @scena.Lambda('lambda_2D5E')
    def lambda_2D5E():
        ChrWalkTo(0x00FE, 47750, 0, 22740, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_2D5E)

    WaitForThreadExit(0x0008, 0x0001)
    WaitForThreadExit(0x0009, 0x0001)
    WaitForThreadExit(0x000A, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010041010V#004F哎？是叫我们吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0450041011V#2P呦～瞧瞧，\n',
            '看来真的猜对了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0460041012V嘿嘿，难得听到女人的声音，\n',
            '就走过来看看，果然……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0136,
        (
            '#0060041013V#040F请问，有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0450041014V#2P嘿嘿，\n',
            '我看你们从刚才起就在这里闲逛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0450041015V#2P既然那么有空，\n',
            '不如陪我们来玩～玩吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0136,
        (
            '#0060041016V#043F哎？这个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010041017V#007F什么呀，原来是几个流氓啊～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010041018V#006F不好意思，\n',
            '我们正在游览这城市呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010041019V要玩的话，你们还是去找别人陪吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0470041020V呦，态度好强硬。\n',
            '我就喜欢这种类型～㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010041021V#004F啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0460041022V想游览的话，\n',
            '我们来做导游不就搞定了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0460041023V别理这个毛头小子了， \n',
            '跟我们去开心开心吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020041024V#014F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010041025V#009F等、等等！\n',
            '什么叫毛头小子！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010041026V像你们这种门外汉，\n',
            '就算一起上也不是约修亚的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0102, 0, 400)

    ChrTalk(
        0x0102,
        (
            '#0020041027V#010F算了，艾丝蒂尔。\n',
            '我根本就没有介意。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020041028V所以你也不用替我生气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 180, 400)

    ChrTalk(
        0x0101,
        (
            '#0010041029V#003F但、但是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0102, 400)

    ChrTalk(
        0x0008,
        (
            '#0450041030V#2P什么，这小子……\n',
            '竟然在我们面前耍酷。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0460041031V真是气人的小鬼……\n',
            '居然跟两个美人卿卿我我的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0470041032V嘿嘿……\n',
            '看来要教教你什么叫做社会的严酷了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_323E')
    def lambda_323E():
        OP_92(0x00FE, 0x0102, 1600, 500, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_323E)

    Sleep(100)

    @scena.Lambda('lambda_3258')
    def lambda_3258():
        OP_92(0x00FE, 0x0102, 1600, 500, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_3258)

    Sleep(100)

    @scena.Lambda('lambda_3272')
    def lambda_3272():
        OP_92(0x00FE, 0x0102, 1700, 500, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_3272)

    Sleep(400)

    ChrSetDirection(0x0101, 225, 400)

    ChrTalk(
        0x0101,
        (
            '#0010041033V#005F等、等等……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0136,
        (
            '#0060041034V#043F请、请不要这样……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1200)

    OP_63(0x0102)

    ChrTalk(
        0x0102,
        (
            '#0020041035V#015F……如果我的态度令你们不舒服，\n',
            '我可以道歉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0102, 270, 400)
    Sleep(500)

    OP_92(0x0102, 0x000A, 1000, 2000, 0x00)

    ChrTalk(
        0x0102,
        (
            '#0020041036V#012F#4P但如果你们要打她们的主意，\n',
            '……我可是不会手下留情的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x000A, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x0008, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    @scena.Lambda('lambda_33DE')
    def lambda_33DE():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000001F4, 0x00000BB8, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_33DE)

    Sleep(100)

    @scena.Lambda('lambda_33F9')
    def lambda_33F9():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000001F4, 0x00000BB8, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_33F9)

    Sleep(100)

    @scena.Lambda('lambda_3414')
    def lambda_3414():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000002BC, 0x00000BB8, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_3414)

    WaitForThreadExit(0x000A, 0x0001)

    ChrTalk(
        0x0009,
        (
            '#0470041037V什……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0460041038V这、这小子搞什么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0450041039V#2P装、装什么腔作什么势！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0450041040V#2P嘿嘿，想在小姑娘面前\n',
            '耍帅的心情我是可以理解。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0450041041V#2P不过太逞强的话，\n',
            '可是会很受伤的哦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000D,
        '青年的声音',
        (
            '#0480041042V#3P你们几个，在干什么！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_354A')
    def lambda_354A():
        CameraMove(50290, 0, 24500, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_354A)

    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000D, 0x0080)

    @scena.Lambda('lambda_356C')
    def lambda_356C():
        ChrTurnDirection(0x00FE, 0x000D, 400)
        Yield()

        Jump('lambda_356C')

    DispatchAsync2(0x0101, 0x0001, lambda_356C)

    @scena.Lambda('lambda_357D')
    def lambda_357D():
        ChrTurnDirection(0x00FE, 0x000D, 400)
        Yield()

        Jump('lambda_357D')

    DispatchAsync2(0x0102, 0x0001, lambda_357D)

    @scena.Lambda('lambda_358E')
    def lambda_358E():
        ChrTurnDirection(0x00FE, 0x000D, 400)
        Yield()

        Jump('lambda_358E')

    DispatchAsync2(0x0136, 0x0001, lambda_358E)

    @scena.Lambda('lambda_359F')
    def lambda_359F():
        ChrTurnDirection(0x00FE, 0x000D, 400)
        Yield()

        Jump('lambda_359F')

    DispatchAsync2(0x0008, 0x0001, lambda_359F)

    @scena.Lambda('lambda_35B0')
    def lambda_35B0():
        ChrTurnDirection(0x00FE, 0x000D, 400)
        Yield()

        Jump('lambda_35B0')

    DispatchAsync2(0x0009, 0x0001, lambda_35B0)

    @scena.Lambda('lambda_35C1')
    def lambda_35C1():
        ChrTurnDirection(0x00FE, 0x000D, 400)
        Yield()

        Jump('lambda_35C1')

    DispatchAsync2(0x000A, 0x0001, lambda_35C1)

    ChrWalkTo(0x000D, 50700, 0, 26480, 3000, 0x00)

    ChrTalk(
        0x0009,
        (
            '#0470041043V嘁……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0460041044V来了个烦人的家伙……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0480041045V#674F你们几个不知悔改的家伙，\n',
            '又在惹是生非……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480041046V年纪也不小了，\n',
            '一点都不觉得羞耻吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0450041047V#2P啰、啰嗦！\n',
            '你这家伙懂什么！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0450041048V#2P不过是市长的跟班罢了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0480041049V#671F你说什么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000C,
        '男性的声音',
        (
            '#0490041050V#3P……哦？有人叫我吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0136, 0xFF)
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)

    @scena.Lambda('lambda_3763')
    def lambda_3763():
        ChrTurnDirection(0x00FE, 0x000C, 400)
        Yield()

        Jump('lambda_3763')

    DispatchAsync2(0x0101, 0x0001, lambda_3763)

    @scena.Lambda('lambda_3774')
    def lambda_3774():
        ChrTurnDirection(0x00FE, 0x000C, 400)
        Yield()

        Jump('lambda_3774')

    DispatchAsync2(0x0102, 0x0001, lambda_3774)

    @scena.Lambda('lambda_3785')
    def lambda_3785():
        ChrTurnDirection(0x00FE, 0x000C, 400)
        Yield()

        Jump('lambda_3785')

    DispatchAsync2(0x0136, 0x0001, lambda_3785)

    @scena.Lambda('lambda_3796')
    def lambda_3796():
        ChrTurnDirection(0x00FE, 0x000C, 400)
        Yield()

        Jump('lambda_3796')

    DispatchAsync2(0x0008, 0x0001, lambda_3796)

    @scena.Lambda('lambda_37A7')
    def lambda_37A7():
        ChrTurnDirection(0x00FE, 0x000C, 400)
        Yield()

        Jump('lambda_37A7')

    DispatchAsync2(0x0009, 0x0001, lambda_37A7)

    @scena.Lambda('lambda_37B8')
    def lambda_37B8():
        ChrTurnDirection(0x00FE, 0x000C, 400)
        Yield()

        Jump('lambda_37B8')

    DispatchAsync2(0x000A, 0x0001, lambda_37B8)

    @scena.Lambda('lambda_37C9')
    def lambda_37C9():
        ChrWalkTo(0x00FE, 50700, 0, 26480, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_37C9)

    ChrTurnDirection(0x000D, 0x000C, 400)
    Sleep(500)

    ChrWalkTo(0x000D, 52200, 0, 25190, 2000, 0x00)
    ChrSetDirection(0x000D, 270, 400)
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    WaitForThreadExit(0x000C, 0x0001)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0136, 0xFF)
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)

    ChrTalk(
        0x0009,
        (
            '#0470041051V戴、戴尔蒙！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0460041052V嘁……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010041053V#002F（这、这是谁啊……\n',
            '　看起来好有威严的样子。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0136,
        (
            '#0060041054V#040F（是卢安的市长戴尔蒙先生。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060041055V（年轻的那个，应该是\n',
            '　担任秘书的基尔巴特先生……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0490041056V#664F卢安是座自由而传统的城市。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490041057V对于你们的衣着和言行，\n',
            '我承认的确没有权力干涉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490041058V#662F但如果你们敢给他人带来麻烦， \n',
            '尤其是旅客，就要另当别论了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0450041059V#2P哼，啰嗦什么呀。\n',
            '这个没落贵族的大款市长。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0450041060V#2P我可不记得我有义务听你说教。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000D, 0x0008, 400)

    ChrTalk(
        0x000D,
        (
            '#0480041061V#674F你、你们太放肆了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480041062V再不适可而止的话，\n',
            '是不是又想让我去协会通报！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0470041063V哼……\n',
            '说来说去又是游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0470041064V难道你就不会\n',
            '靠自己的本事干点什么吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0460041065V就算你去向协会求救，\n',
            '他们赶过来也要花时间的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0460041066V教训了你们之后我们就溜之大吉，\n',
            '我看你们还拿我们有什么办法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3BF5')
    def lambda_3BF5():
        CameraMove(49220, 0, 23720, 1000)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_3BF5)

    Sleep(500)

    @scena.Lambda('lambda_3C12')
    def lambda_3C12():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3C12)

    Sleep(200)

    @scena.Lambda('lambda_3C25')
    def lambda_3C25():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_3C25)

    Sleep(200)

    @scena.Lambda('lambda_3C38')
    def lambda_3C38():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0136, 0x0001, lambda_3C38)

    WaitForThreadExit(0x000C, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010041067V#007F真不好意思……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010041068V根本就用不着去通知，\n',
            '因为游击士已经在这里了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3CAB')
    def lambda_3CAB():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_3CAB)

    @scena.Lambda('lambda_3CB9')
    def lambda_3CB9():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_3CB9)

    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#0450041069V#2P什、什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010041070V#006F哈～居然到现在\n',
            '还没注意到这徽章啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010041071V你们几个，眼神也太不好使了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔指了指\n',
            '自己左边胸前的准游击士徽章。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0009,
        (
            '#0470041072V这、这是……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0460041073V游击士的徽章！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0460041074V那么，那个小子也……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020041075V#010F没错，正是如此。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x000A, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x0008, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrSetDirection(0x0009, 0, 400)

    ChrTalk(
        0x0009,
        (
            '#0470041076V（怎、怎么办？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0470041077V（想不到这样的小鬼\n',
            '　居然会是游击士……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0460041078V（什么呀？管他的！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0460041079V（就算是游击士，也只不过是\n',
            '　两个女人和一个毛头小子罢了！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0008, 180, 400)

    ChrTalk(
        0x0008,
        (
            '#0450041080V#2P（蠢、蠢货！\n',
            '　别光凭外表判断！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0450041081V#2P（你忘了吗！？\n',
            '　前不久我们跟一个女游击士动手，\n',
            '　结果三人联手还是被她修理了一顿。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0450041082V#2P（而、而且不管怎么说……\n',
            '　他们和『那个人』是一样的！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x000A, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0008, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1500)

    ChrSetDirection(0x0008, 90, 400)

    ChrTalk(
        0x0008,
        (
            '#0450041083V#2P今、今天就放你们一马！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0009, 90, 400)

    ChrTalk(
        0x0009,
        (
            '#0470041084V咱们就走着瞧吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0460041085V哼，算你们好样的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_4156')
    def lambda_4156():
        ChrTurnDirection(0x00FE, 0x000A, 400)
        Yield()

        Jump('lambda_4156')

    DispatchAsync2(0x0101, 0x0001, lambda_4156)

    @scena.Lambda('lambda_4167')
    def lambda_4167():
        ChrTurnDirection(0x00FE, 0x000A, 400)
        Yield()

        Jump('lambda_4167')

    DispatchAsync2(0x0102, 0x0001, lambda_4167)

    @scena.Lambda('lambda_4178')
    def lambda_4178():
        ChrTurnDirection(0x00FE, 0x000A, 400)
        Yield()

        Jump('lambda_4178')

    DispatchAsync2(0x0136, 0x0001, lambda_4178)

    @scena.Lambda('lambda_4189')
    def lambda_4189():
        ChrTurnDirection(0x00FE, 0x000A, 400)
        Yield()

        Jump('lambda_4189')

    DispatchAsync2(0x000C, 0x0001, lambda_4189)

    @scena.Lambda('lambda_419A')
    def lambda_419A():
        ChrTurnDirection(0x00FE, 0x000A, 400)
        Yield()

        Jump('lambda_419A')

    DispatchAsync2(0x000D, 0x0001, lambda_419A)

    ChrSetDirection(0x000A, 270, 400)

    @scena.Lambda('lambda_41B2')
    def lambda_41B2():
        CameraMove(48000, 0, 24000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_41B2)

    @scena.Lambda('lambda_41CA')
    def lambda_41CA():
        ChrWalkTo(0x00FE, 37000, 0, 22740, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_41CA)

    ChrSetDirection(0x0008, 270, 400)

    @scena.Lambda('lambda_41EC')
    def lambda_41EC():
        ChrWalkTo(0x00FE, 37000, 0, 23790, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_41EC)

    ChrSetDirection(0x0009, 270, 400)

    @scena.Lambda('lambda_420E')
    def lambda_420E():
        ChrWalkTo(0x00FE, 37000, 0, 21720, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_420E)

    WaitForThreadExit(0x0009, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010041086V#007F该说什么好呢……\n',
            '还真是老套的退场词啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020041087V#010F不过算了，\n',
            '我想他们应该不会再过来惹事吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0136, 0xFF)
    TerminateThread(0x000D, 0xFF)
    TerminateThread(0x000C, 0xFF)
    ChrSetDirection(0x000C, 180, 400)

    ChrTalk(
        0x000C,
        (
            '#0490041088V#660F#2P真是十分抱歉，各位。\n',
            '那些人刚才给你们添麻烦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_4310')
    def lambda_4310():
        CameraMove(50450, 0, 24070, 1500)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_4310)

    @scena.Lambda('lambda_4328')
    def lambda_4328():
        ChrTurnDirection(0x00FE, 0x0136, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_4328)

    ChrWalkTo(0x000C, 50700, 0, 25560, 2000, 0x00)

    @scena.Lambda('lambda_434A')
    def lambda_434A():
        ChrTurnDirection(0x00FE, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_434A)

    @scena.Lambda('lambda_4358')
    def lambda_4358():
        ChrTurnDirection(0x00FE, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x0136, 0x0001, lambda_4358)

    ChrTurnDirection(0x0101, 0x000C, 400)
    WaitForThreadExit(0x000C, 0x0002)

    ChrTalk(
        0x000C,
        (
            '#0490041089V#660F还没做自我介绍，\n',
            '我是卢安的市长戴尔蒙。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490041090V#660F而这位就是\n',
            '我的秘书基尔巴特。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0480041091V#670F请多指教。\n',
            '你们是游击士吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010041092V#000F嗯，我们是从洛连特来的。\n',
            '我是准游击士艾丝蒂尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020041093V#010F我是准游击士约修亚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0490041094V#660F说起来，\n',
            '卢安支部的嘉恩说过\n',
            '会有两个很有前途的新人过来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490041095V莫非就是指二位吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010041096V#008F嘿嘿……\n',
            '是不是有前途还不敢说呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020041097V#010F接下来的一段时间，\n',
            '我们会在卢安地区工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0490041098V#661F呀，那可是帮了我们大忙啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490041099V现在正处于非常时期。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490041100V说不定我也会有\n',
            '需要你们协助的地方，\n',
            '到时候就请二位多多关照了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020041101V#014F非常时期……吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0490041102V#660F嗯，详细的情况\n',
            '二位可以向嘉恩询问。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490041103V对了，这位小姐\n',
            '好像是王立学院的学生啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0136,
        (
            '#0060041104V#040F是的，我是王立学院二年级的\n',
            '科洛丝·琳希。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060041105V初次见面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0490041106V#660F原来如此， \n',
            '科林兹校长和我可是老交情了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490041107V说起来，\n',
            '基尔巴特也是王立学院毕业的对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0480041108V#670F嗯，是的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480041109V你叫科洛丝是吧？\n',
            '我可是久仰你的大名了哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480041110V听说你正和学生会长乔儿\n',
            '一起争夺学生会主席的位置。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480041111V有你们这样优秀的后辈，\n',
            '我这个前辈也是脸上沾光啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0136,
        (
            '#0060041112V#045F这……太过奖了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0490041113V#661F哈哈哈， \n',
            '这次的学园祭我也是非常期待啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490041114V还请多多加油了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0136,
        (
            '#0060041115V#040F是，我一定会尽力的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0490041116V#661F嗯，那么各位。\n',
            '我们这就告辞了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490041117V要是刚才那些人再来找麻烦，\n',
            '尽管来通知我就行了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490041118V就让我这个卢安市长\n',
            '好好地履行管教他们的职责吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_49A8')
    def lambda_49A8():
        CameraMove(52270, 0, 23490, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_49A8)

    @scena.Lambda('lambda_49C0')
    def lambda_49C0():
        ChrTurnDirection(0x00FE, 0x000C, 400)
        Yield()

        Jump('lambda_49C0')

    DispatchAsync2(0x0101, 0x0001, lambda_49C0)

    @scena.Lambda('lambda_49D1')
    def lambda_49D1():
        ChrTurnDirection(0x00FE, 0x000C, 400)
        Yield()

        Jump('lambda_49D1')

    DispatchAsync2(0x0102, 0x0001, lambda_49D1)

    @scena.Lambda('lambda_49E2')
    def lambda_49E2():
        ChrTurnDirection(0x00FE, 0x000C, 400)
        Yield()

        Jump('lambda_49E2')

    DispatchAsync2(0x0136, 0x0001, lambda_49E2)

    ChrWalkTo(0x000C, 52590, 0, 23260, 3000, 0x00)

    @scena.Lambda('lambda_4A07')
    def lambda_4A07():
        ChrWalkTo(0x00FE, 64340, 0, 21300, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_4A07)

    Sleep(500)

    ChrWalkTo(0x000D, 53590, 0, 22860, 3000, 0x00)

    @scena.Lambda('lambda_4A3B')
    def lambda_4A3B():
        ChrWalkTo(0x00FE, 64340, 0, 21300, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_4A3B)

    WaitForThreadExit(0x000D, 0x0001)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0136, 0xFF)

    ChrTalk(
        0x0101,
        (
            '#0010041119V#000F嗯，这个戴尔蒙先生\n',
            '真是个好有气量和威严的人呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020041120V#010F是啊，他的言行举止\n',
            '的确很有作为市长的风范。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_4AEF')
    def lambda_4AEF():
        CameraMove(50520, 0, 23090, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_4AEF)

    Sleep(500)

    ChrSetDirection(0x0136, 270, 400)
    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0136,
        (
            '#0060041121V#040F因为戴尔蒙家\n',
            '以前是一个豪门贵族。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060041122V虽说贵族制已经被废除了，\n',
            '但是这家族的人至今仍被视为\n',
            '上流阶级的代表者。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 135, 400)

    ChrTalk(
        0x0101,
        (
            '#0010041123V#501F哦～……\n',
            '好像跟我们不是一个世界的呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010041124V#007F不过呢，话说回来，\n',
            '这城市怎么会有流氓存在啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0136,
        (
            '#0060041125V#043F是啊。\n',
            '吓了我一跳呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060041126V真对不起，\n',
            '把你们带到不安全的地方来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020041127V#010F你用不着道歉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020041128V而且，\n',
            '我们也没必要特意去招惹他们。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020041129V看来他们经常聚集在\n',
            '仓库区域最里面那一带，\n',
            '所以我们就尽量不要靠近那里吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010041130V#009F嗯……\n',
            '虽然有点气愤，但也没办法啦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000D, 0x0080)
    ChrSetFlags(0x000B, 0x0080)
    OP_64(0x02, 0x0001)
    OP_71(0x0013, 0x0010)
    EventEnd(0x00)

    def _loc_4D93(): pass

    label('loc_4D93')

    Return()

# id: 0x000D offset: 0x4D94
@scena.Code('func_0D_4D94')
def func_0D_4D94():
    EventBegin(0x00)
    FadeIn(2000, 0)
    PlaySE(212, 0x00, 0x64)
    LoadEffect(0x04, 'map\\\\mp013_00.eff')
    LoadEffect(0x05, 'map\\\\mp013_01.eff')
    PlayEffect(0x04, 0x00, 0x0017, 0, 0, 2200, 180, 0, 0, 1000, 100, 3000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x05, 0x01, 0x0017, 0, 0, -1800, 180, 0, 0, 700, 700, 700, 0x00FF, 0, 0, 0, 0)
    ChrSetPos(0x0017, -1310, -2900, 14370, 270)
    ChrSetFlags(0x0017, 0x0040)
    OP_A1(0x0017, 0x0020)
    OP_72(0x0020, 0x0004)
    OP_72(0x0020, 0x0002)
    OP_71(0x0020, 0x0400)
    OP_71(0x0020, 0x0040)
    Yield()
    ChrClearFlags(0x0000, 0x0004)
    ChrClearFlags(0x0001, 0x0004)
    ChrClearFlags(0x0002, 0x0004)
    ChrSetPos(0x0102, -2350, -2870, 14350, 270)
    ChrSetPos(0x0101, -1030, -2800, 14700, 90)
    ChrSetPos(0x0136, -910, -2840, 13890, 90)
    ChrSetFlags(0x0000, 0x0020)
    ChrSetFlags(0x0001, 0x0020)
    ChrSetFlags(0x0002, 0x0020)
    CameraMove(8670, -1800, 15130, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(158000, 0)
    OP_6E(262, 0)
    Sleep(1000)

    @scena.Lambda('lambda_4EFF')
    def lambda_4EFF():
        CameraMove(18890, -1800, 11040, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4EFF)

    @scena.Lambda('lambda_4F17')
    def lambda_4F17():
        OP_6C(134000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_4F17)

    ChrSetFlags(0x0017, 0x0040)
    ChrSetFlags(0x0017, 0x0004)
    WaitForThreadExit(0x0017, 0x0001)

    @scena.Lambda('lambda_4F36')
    def lambda_4F36():
        ChrMoveTo(0x00FE, 18170, -2900, 13370, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0017, 0x0001, lambda_4F36)

    Sleep(500)

    StopEffect(0x00, 0x02)
    PlayEffect(0x04, 0x02, 0x0017, 0, 0, 2200, 180, 0, 0, 600, 100, 3000, 0x00FF, 0, 0, 0, 0)
    StopEffect(0x01, 0x02)

    @scena.Lambda('lambda_4F91')
    def lambda_4F91():
        ChrMoveTo(0x00FE, 18170, -2900, 13370, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0017, 0x0001, lambda_4F91)

    Sleep(500)

    @scena.Lambda('lambda_4FB1')
    def lambda_4FB1():
        ChrMoveTo(0x00FE, 18170, -2900, 13370, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0017, 0x0001, lambda_4FB1)

    WaitForThreadExit(0x0017, 0x0001)
    StopEffect(0x02, 0x02)
    ChrClearFlags(0x0000, 0x0020)
    ChrClearFlags(0x0001, 0x0020)
    ChrClearFlags(0x0002, 0x0020)

    @scena.Lambda('lambda_4FE3')
    def lambda_4FE3():
        ChrTurnDirection(0x00FE, 0x0136, 400)
        Yield()

        Jump('lambda_4FE3')

    DispatchAsync2(0x0101, 0x0001, lambda_4FE3)

    @scena.Lambda('lambda_4FF4')
    def lambda_4FF4():
        ChrTurnDirection(0x00FE, 0x0136, 400)
        Yield()

        Jump('lambda_4FF4')

    DispatchAsync2(0x0102, 0x0001, lambda_4FF4)

    ChrSetDirection(0x0136, 180, 400)

    ExecExpressionWithValue(
        0x0136,
        0x0B,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetFlags(0x0136, 0x1000)
    ChrSetSubChip(0x0136, 4)

    @scena.Lambda('lambda_5021')
    def lambda_5021():
        OP_99(0x00FE, 0x04, 0x06, 2000)

        ExitThread()

    DispatchAsync(0x0136, 0x0003, lambda_5021)

    ChrSetFlags(0x0136, 0x0004)
    ChrJumpTo(0x0136, 18350, -1800, 11970, 1500, 8000)

    ExecExpressionWithValue(
        0x0136,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrClearFlags(0x0136, 0x1000)
    ChrClearFlags(0x0136, 0x0004)
    ChrWalkTo(0x0136, 19300, -1800, 11350, 3000, 0x00)
    ChrTurnDirection(0x0136, 0x0101, 400)

    @scena.Lambda('lambda_507D')
    def lambda_507D():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_507D')

    DispatchAsync2(0x0136, 0x0001, lambda_507D)

    TerminateThread(0x0101, 0xFF)
    ChrSetFlags(0x0101, 0x0004)
    ChrWalkTo(0x0101, 18280, -2800, 12950, 3000, 0x00)

    ExecExpressionWithValue(
        0x0101,
        0x0B,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetFlags(0x0101, 0x1000)
    ChrSetSubChip(0x0101, 0)

    @scena.Lambda('lambda_50C0')
    def lambda_50C0():
        OP_99(0x00FE, 0x00, 0x02, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_50C0)

    ChrSetFlags(0x0101, 0x0004)
    ChrJumpTo(0x0101, 18350, -1800, 11970, 1500, 8000)

    ExecExpressionWithValue(
        0x0101,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrClearFlags(0x0101, 0x1000)
    ChrClearFlags(0x0101, 0x0004)
    ChrWalkTo(0x0101, 18220, -1800, 10840, 3000, 0x00)
    ChrTurnDirection(0x0101, 0x0102, 400)

    @scena.Lambda('lambda_511C')
    def lambda_511C():
        ChrTurnDirection(0x00FE, 0x0102, 400)
        Yield()

        Jump('lambda_511C')

    DispatchAsync2(0x0136, 0x0001, lambda_511C)

    @scena.Lambda('lambda_512D')
    def lambda_512D():
        ChrTurnDirection(0x00FE, 0x0102, 400)
        Yield()

        Jump('lambda_512D')

    DispatchAsync2(0x0101, 0x0001, lambda_512D)

    TerminateThread(0x0102, 0xFF)
    ChrWalkTo(0x0102, 17070, -2750, 12950, 3000, 0x00)

    ExecExpressionWithValue(
        0x0102,
        0x0B,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetFlags(0x0102, 0x1000)
    ChrSetSubChip(0x0102, 0)
    ChrSetFlags(0x0102, 0x0004)

    @scena.Lambda('lambda_5170')
    def lambda_5170():
        OP_99(0x00FE, 0x00, 0x02, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_5170)

    ChrJumpTo(0x0102, 17230, -1800, 11590, 1500, 8000)

    ExecExpressionWithValue(
        0x0102,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrClearFlags(0x0102, 0x1000)
    ChrSetSubChip(0x0102, 0)
    ChrClearFlags(0x0102, 0x0004)
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0101,
        (
            '#0010050624V#002F这里就是……\n',
            '仓库区域的最南面吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(407, 0x00, 0x64)
    ChrClearFlags(0x000E, 0x0080)
    ChrSetFlags(0x000E, 0x0004)
    ChrSetFlags(0x000E, 0x0040)
    ChrSetPos(0x000E, 31110, 6000, 15480, 0)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0136, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0136, 0xFF)

    @scena.Lambda('lambda_526B')
    def lambda_526B():
        ChrTurnDirection(0x00FE, 0x000E, 400)
        Yield()

        Jump('lambda_526B')

    DispatchAsync2(0x0101, 0x0002, lambda_526B)

    @scena.Lambda('lambda_527C')
    def lambda_527C():
        ChrTurnDirection(0x00FE, 0x000E, 400)
        Yield()

        Jump('lambda_527C')

    DispatchAsync2(0x0102, 0x0002, lambda_527C)

    @scena.Lambda('lambda_528D')
    def lambda_528D():
        ChrTurnDirection(0x00FE, 0x000E, 400)
        Yield()

        Jump('lambda_528D')

    DispatchAsync2(0x0136, 0x0002, lambda_528D)

    @scena.Lambda('lambda_529E')
    def lambda_529E():
        CameraMove(20890, -1800, 11040, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_529E)

    PlaySE(140, 0x00, 0x64)
    OP_92(0x000E, 0x0136, 5000, 8000, 0x00)
    OP_92(0x000E, 0x0136, 4000, 6000, 0x00)
    OP_92(0x000E, 0x0136, 3000, 4000, 0x00)
    OP_92(0x000E, 0x0136, 2000, 2000, 0x00)
    ChrWalkTo(0x000E, 19800, -800, 11500, 1500, 0x00)
    TerminateThread(0x0136, 0xFF)
    ChrSetFlags(0x0136, 0x0020)

    @scena.Lambda('lambda_5310')
    def lambda_5310():
        ChrSetDirection(0x00FE, 315, 200)

        ExitThread()

    DispatchAsync(0x0136, 0x0003, lambda_5310)

    ChrSetChipByIndex(0x0136, 14)
    ChrSetSubChip(0x0136, 2)
    ChrMoveTo(0x000E, 19500, -1600, 11450, 1000, 0x00)
    WaitForThreadExit(0x000E, 0x0003)
    Sleep(100)

    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    Fade(250)
    ChrSetFlags(0x000E, 0x0080)
    ChrSetSubChip(0x0136, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010050625V#004F啊，基库！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0440050626V#310F啾。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0440050627V#310F叽啾，啾～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0136,
        (
            '#0060050628V#049F#2P是吗……我知道了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060050629V#042F#2P……那孩子果然\n',
            '跑到仓库最里面去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    ChrClearFlags(0x000E, 0x0080)
    ChrSetSubChip(0x0136, 2)
    OP_0D()

    @scena.Lambda('lambda_5430')
    def lambda_5430():
        ChrTurnDirection(0x00FE, 0x000E, 400)
        Yield()

        Jump('lambda_5430')

    DispatchAsync2(0x0101, 0x0002, lambda_5430)

    @scena.Lambda('lambda_5441')
    def lambda_5441():
        ChrTurnDirection(0x00FE, 0x000E, 400)
        Yield()

        Jump('lambda_5441')

    DispatchAsync2(0x0102, 0x0002, lambda_5441)

    @scena.Lambda('lambda_5452')
    def lambda_5452():
        ChrTurnDirection(0x00FE, 0x000E, 400)
        Yield()

        Jump('lambda_5452')

    DispatchAsync2(0x0136, 0x0002, lambda_5452)

    @scena.Lambda('lambda_5463')
    def lambda_5463():
        CameraMove(18890, -1800, 11040, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5463)

    PlaySE(140, 0x00, 0x64)

    @scena.Lambda('lambda_5480')
    def lambda_5480():
        ChrWalkTo(0x00FE, 51110, 6000, 15480, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_5480)

    Sleep(400)

    @scena.Lambda('lambda_54A0')
    def lambda_54A0():
        ChrWalkTo(0x00FE, 51110, 6000, 15480, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_54A0)

    Sleep(400)

    ChrSetChipByIndex(0x0136, 65535)
    ChrClearFlags(0x0136, 0x0020)
    ChrSetSubChip(0x0136, 0)

    @scena.Lambda('lambda_54CF')
    def lambda_54CF():
        ChrWalkTo(0x00FE, 51110, 6000, 15480, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_54CF)

    WaitForThreadExit(0x000E, 0x0001)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0136, 0xFF)
    ChrTurnDirection(0x0102, 0x0136, 400)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0102,
        (
            '#0020050630V#012F我们赶快过去吧。\n',
            '那帮家伙的地盘就在最里面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_5549')
    def lambda_5549():
        ChrTurnDirection(0x0136, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x0136, 0x0001, lambda_5549)

    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010050631V#005F#2P明白！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0136,
        (
            '#0060050632V#042F是……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x000E, 0x0080)
    EventEnd(0x00)

    Return()

# id: 0x000E offset: 0x559F
@scena.Code('func_0E_559F')
def func_0E_559F():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0088, 2, 0x442)),
            (Expr.Eval, "OP_40(0x0334)"),
            (Expr.Eval, "OP_40(0x0332)"),
            Expr.Or,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_55B7',
    )

    Call(1, 0x000A)

    Jump('loc_59E6')

    def _loc_55B7(): pass

    label('loc_55B7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            (Expr.TestScenaFlags, ScenaFlag(0x0088, 2, 0x442)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_56D4',
    )

    EventBegin(0x02)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5645',
    )

    ChrTurnDirection(0x0102, 0x0001, 400)

    ChrTalk(
        0x0102,
        (
            '#0020061363V#012F往这边走就出城了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020061364V现在我们要去市长家，\n',
            '在王国军到来之前尽量拖延时间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_56B6')

    def _loc_5645(): pass

    label('loc_5645')

    ChrTurnDirection(0x0102, 0x0000, 400)

    ChrTalk(
        0x0102,
        (
            '#0020061365V#012F往这边走就出城了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020061366V现在我们要去市长家，\n',
            '在王国军到来之前尽量拖延时间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_56B6(): pass

    label('loc_56B6')

    ChrMoveToRelative(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Jump('loc_59E6')

    def _loc_56D4(): pass

    label('loc_56D4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 1, 0x429)),
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_575B',
    )

    EventBegin(0x02)
    ChrTurnDirection(0x0136, 0x0000, 400)

    ChrTalk(
        0x0105,
        (
            '#0060050563V#042F往这边走就出城了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060050564V赶快去仓库区找找克拉姆吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveToRelative(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Jump('loc_59E6')

    def _loc_575B(): pass

    label('loc_575B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 6, 0x41E)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5964',
    )

    EventBegin(0x02)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_58D8',
    )

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_581B',
    )

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020050052V#010F在去城外之前先到协会报到吧。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020050053V嘉恩先生不是说\n',
            '要给我们分配工作吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010050054V#000F啊，是这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_58D5')

    def _loc_581B(): pass

    label('loc_581B')

    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010050055V#000F哎……\n',
            '要到城外去吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020050056V#010F不了，\n',
            '还是先去协会吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020050057V嘉恩先生不是说\n',
            '要给我们分配工作吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010050058V#006F嗯，好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_58D5(): pass

    label('loc_58D5')

    Jump('loc_5946')

    def _loc_58D8(): pass

    label('loc_58D8')

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020050059V#010F在去城外之前先到协会报到吧。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020050060V嘉恩先生不是说\n',
            '要给我们分配工作吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_5946(): pass

    label('loc_5946')

    ChrMoveToRelative(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Jump('loc_59E6')

    def _loc_5964(): pass

    label('loc_5964')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 0, 0x418)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_59E6',
    )

    EventBegin(0x02)
    ChrTurnDirection(0x0136, 0x0000, 400)

    ChrTalk(
        0x0136,
        (
            '#0060040971V#040F再往前走就到阿伊纳街道了。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060040972V我们还是回城里去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveToRelative(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_59E6(): pass

    label('loc_59E6')

    Return()

# id: 0x000F offset: 0x59E7
@scena.Code('func_0F_59E7')
def func_0F_59E7():
    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门上着锁，无法打开。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0010 offset: 0x5A37
@scena.Code('func_10_5A37')
def func_10_5A37():
    TalkBegin(0x00FF)
    TalkEnd(0x00FF)

    Return()

# id: 0x0011 offset: 0x5A3E
@scena.Code('func_11_5A3E')
def func_11_5A3E():
    OP_13(0x0069)

    Return()

# id: 0x0012 offset: 0x5A42
@scena.Code('func_12_5A42')
def func_12_5A42():
    OP_13(0x0052)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
