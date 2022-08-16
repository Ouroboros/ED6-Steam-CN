import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T2120_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2120   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'T2120.x'
    header.mapIndex       = 1
    header.bgm            = 12
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT01/T2120._SN', 'ED6_DT01/T2120_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
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
        ('ED6_DT07/CH01240._CH', 'ED6_DT07/CH01240P._CP'),
        ('ED6_DT07/CH02400._CH', 'ED6_DT07/CH02400P._CP'),
        ('ED6_DT06/CH20053._CH', 'ED6_DT06/CH20053P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH01190._CH', 'ED6_DT07/CH01190P._CP'),
        ('ED6_DT07/CH01460._CH', 'ED6_DT07/CH01460P._CP'),
        ('ED6_DT07/CH01210._CH', 'ED6_DT07/CH01210P._CP'),
        ('ED6_DT07/CH01590._CH', 'ED6_DT07/CH01590P._CP'),
        ('ED6_DT07/CH01760._CH', 'ED6_DT07/CH01760P._CP'),
        ('ED6_DT07/CH01100._CH', 'ED6_DT07/CH01100P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01210._CH', 'ED6_DT07/CH01210P._CP'),
        ('ED6_DT06/CH20021._CH', 'ED6_DT06/CH20021P._CP'),
        ('ED6_DT06/CH20034._CH', 'ED6_DT06/CH20034P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
    ]

# id: 0x10001 offset: 0x122
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '嘉恩',
            x                   = -5700,
            z                   = 0,
            y                   = 45100,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0105,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '卡露娜',
            x                   = -400,
            z                   = 0,
            y                   = 45400,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            name                = '阿加特',
            x                   = 0,
            z                   = 0,
            y                   = 33500,
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
            name                = '索姆茨',
            x                   = -30000,
            z                   = 0,
            y                   = 4910,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '加鲁诺',
            x                   = 3100,
            z                   = 4000,
            y                   = 8000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '扎古',
            x                   = -3700,
            z                   = 0,
            y                   = 42600,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '爱珐',
            x                   = 1200,
            z                   = 0,
            y                   = 5000,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '妮吉塔',
            x                   = 5360,
            z                   = 4000,
            y                   = 5510,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '梅尔茨',
            x                   = -38000,
            z                   = 0,
            y                   = 47490,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            name                = '欧尼尔',
            x                   = 29900,
            z                   = 0,
            y                   = 4500,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            name                = '西加罗',
            x                   = 31800,
            z                   = 0,
            y                   = 2500,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '艾德尔',
            x                   = 28500,
            z                   = 0,
            y                   = 700,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0011,
        ),
        ScenaNpcData(
            name                = '目标用摄像机',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0081,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '玻璃杯',
            x                   = 20,
            z                   = 700,
            y                   = 39430,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 917516,
            chipIndex           = 12,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '吉米',
            x                   = 28570,
            z                   = 0,
            y                   = 1980,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0012,
        ),
    )

# id: 0x10002 offset: 0x302
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x302
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x302
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 1070,
            triggerZ            = 0,
            triggerY            = 43260,
            triggerRange        = 1400,
            actorX              = 1070,
            actorZ              = 2000,
            actorY              = 43260,
            flags               = 0x007C,
            talkScenaIndex      = 0x0001,
            talkFunctionIndex   = 0x0000,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -30020,
            triggerZ            = 0,
            triggerY            = 3590,
            triggerRange        = 400,
            actorX              = -30000,
            actorZ              = 1500,
            actorY              = 4910,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 1020,
            triggerZ            = 0,
            triggerY            = 3000,
            triggerRange        = 400,
            actorX              = 1200,
            actorZ              = 1500,
            actorY              = 5000,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 29980,
            triggerZ            = 0,
            triggerY            = 3310,
            triggerRange        = 400,
            actorX              = 29900,
            actorZ              = 1500,
            actorY              = 4500,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000E,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -4420,
            triggerZ            = 0,
            triggerY            = 45090,
            triggerRange        = 600,
            actorX              = -5700,
            actorZ              = 1500,
            actorY              = 45100,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000A,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x3B6
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_3F1',
    )

    ChrSetFlags(0x000F, 0x0080)
    ChrSetFlags(0x000F, 0x0008)
    ChrClearFlags(0x0010, 0x0080)

    If(
        (
            (Expr.Eval, "OP_29(0x001E, 0x00, 0x04)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3E4',
    )

    ChrClearFlags(0x0016, 0x0080)
    ChrSetFlags(0x0016, 0x0010)

    Jump('loc_3EE')

    def _loc_3E4(): pass

    label('loc_3E4')

    If(
        (
            (Expr.Eval, "OP_29(0x001E, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_3EE',
    )

    def _loc_3EE(): pass

    label('loc_3EE')

    Jump('loc_523')

    def _loc_3F1(): pass

    label('loc_3F1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_436',
    )

    ChrSetFlags(0x000F, 0x0080)
    ChrSetFlags(0x000F, 0x0008)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x0009, 0x0008)
    ChrClearFlags(0x0010, 0x0080)

    If(
        (
            (Expr.Eval, "OP_29(0x001E, 0x00, 0x04)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_429',
    )

    ChrClearFlags(0x0016, 0x0080)
    ChrSetFlags(0x0016, 0x0010)

    Jump('loc_433')

    def _loc_429(): pass

    label('loc_429')

    If(
        (
            (Expr.Eval, "OP_29(0x001E, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_433',
    )

    def _loc_433(): pass

    label('loc_433')

    Jump('loc_523')

    def _loc_436(): pass

    label('loc_436')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            Expr.Return,
        ),
        'loc_47B',
    )

    ChrClearFlags(0x000D, 0x0080)
    ChrSetFlags(0x000F, 0x0080)
    ChrSetFlags(0x000F, 0x0008)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x0009, 0x0008)

    If(
        (
            (Expr.Eval, "OP_29(0x001E, 0x00, 0x04)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_46E',
    )

    ChrClearFlags(0x0016, 0x0080)
    ChrSetFlags(0x0016, 0x0010)

    Jump('loc_478')

    def _loc_46E(): pass

    label('loc_46E')

    If(
        (
            (Expr.Eval, "OP_29(0x001E, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_478',
    )

    def _loc_478(): pass

    label('loc_478')

    Jump('loc_523')

    def _loc_47B(): pass

    label('loc_47B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_4A5',
    )

    ChrSetFlags(0x000F, 0x0080)
    ChrSetFlags(0x000F, 0x0008)
    ChrSetPos(0x0009, -36210, 0, 41450, 270)
    ChrClearFlags(0x0010, 0x0080)

    Jump('loc_523')

    def _loc_4A5(): pass

    label('loc_4A5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_4CD',
    )

    ChrSetFlags(0x000F, 0x0080)
    ChrSetFlags(0x000F, 0x0008)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x0009, 0x0008)
    ChrClearFlags(0x0012, 0x0080)
    ChrClearFlags(0x0013, 0x0080)

    Jump('loc_523')

    def _loc_4CD(): pass

    label('loc_4CD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_4F2',
    )

    ChrSetFlags(0x000F, 0x0080)
    ChrSetFlags(0x000F, 0x0008)
    ChrSetPos(0x0009, -36210, 0, 41450, 270)

    Jump('loc_523')

    def _loc_4F2(): pass

    label('loc_4F2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 7, 0x417)),
            Expr.Return,
        ),
        'loc_512',
    )

    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0009, -36400, 0, 41270, 270)

    Jump('loc_523')

    def _loc_512(): pass

    label('loc_512')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_523',
    )

    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0008, 0x0008)

    def _loc_523(): pass

    label('loc_523')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_532',
    )

    ChrSetFlags(0x000C, 0x0080)

    Jump('loc_53F')

    def _loc_532(): pass

    label('loc_532')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 6, 0x41E)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_53F',
    )

    ChrSetFlags(0x000C, 0x0080)

    def _loc_53F(): pass

    label('loc_53F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_54D',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, func_17_8A92)

    def _loc_54D(): pass

    label('loc_54D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 3, 0x3FB)),
            Expr.Return,
        ),
        'loc_55B',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    Event(0, func_18_92A9)

    def _loc_55B(): pass

    label('loc_55B')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000069, 'loc_567'),
        (-1, 'loc_5AD'),
    )

    def _loc_567(): pass

    label('loc_567')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 4, 0x414)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_576',
    )

    SetScenaFlags(ScenaFlag(0x0082, 4, 0x414))
    Event(0, func_13_49E3)

    def _loc_576(): pass

    label('loc_576')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 0, 0x418)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 7, 0x417)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_597',
    )

    SetScenaFlags(ScenaFlag(0x0083, 0, 0x418))
    Event(0, func_14_5214)
    MapSetFlags(0x10000000)
    OP_B1('t2120_n')

    def _loc_597(): pass

    label('loc_597')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 4, 0x42C)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5AA',
    )

    SetScenaFlags(ScenaFlag(0x0085, 5, 0x42D))
    Event(0, func_16_6A76)

    def _loc_5AA(): pass

    label('loc_5AA')

    Jump('loc_5AD')

    def _loc_5AD(): pass

    label('loc_5AD')

    Return()

# id: 0x0001 offset: 0x5AE
@scena.Code('func_01_5AE')
def func_01_5AE():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0089, 3, 0x44B)),
            (Expr.TestScenaFlags, ScenaFlag(0x0089, 4, 0x44C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5C3',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_5C3(): pass

    label('loc_5C3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 0, 0x418)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 4, 0x43C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Or,
            Expr.Return,
        ),
        'loc_5E4',
    )

    OP_B1('t2120_y')

    Jump('loc_5ED')

    def _loc_5E4(): pass

    label('loc_5E4')

    OP_B1('t2120_n')

    def _loc_5ED(): pass

    label('loc_5ED')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 0, 0x418)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5FE',
    )

    OP_1B(0x06, 0x00, 0x0019)
    OP_64(0x04, 0x0001)

    def _loc_5FE(): pass

    label('loc_5FE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_60E',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x56),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_60E(): pass

    label('loc_60E')

    Return()

# id: 0x0002 offset: 0x60F
@scena.Code('func_02_60F')
def func_02_60F():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_624',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_60F')

    def _loc_624(): pass

    label('loc_624')

    Return()

# id: 0x0003 offset: 0x625
@scena.Code('func_03_625')
def func_03_625():
    Call(0, 0x0004)
    ChrSetDirection(0x000B, 180, 0)

    Return()

# id: 0x0004 offset: 0x631
@scena.Code('func_04_631')
def func_04_631():
    TalkBegin(0x000B)
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
        1,
        (
            TXT(0x00, '对话\n'),
            TXT(0x01, '改造·换钱\n'),
            TXT(0x02, '离开\n'),
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
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_693',
    )

    OP_0D()
    OP_A9(0x1E)
    OP_56(0x00)
    TalkEnd(0x000B)

    Return()

    def _loc_693(): pass

    label('loc_693')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6A4',
    )

    TalkEnd(0x000B)

    Return()

    def _loc_6A4(): pass

    label('loc_6A4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_6EB',
    )

    ChrTalk(
        0x000B,
        (
            '辛苦你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '那么，\n',
            '以后有什么事情还得拜托你们哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E01')

    def _loc_6EB(): pass

    label('loc_6EB')

    If(
        (
            (Expr.Eval, "OP_29(0x001D, 0x00, 0x02)"),
            (Expr.Eval, "OP_29(0x001D, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x001D, 0x01, 0x8000)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_70D',
    )

    Call(1, 0x0001)

    Jump('loc_E01')

    def _loc_70D(): pass

    label('loc_70D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_782',
    )

    ChrTalk(
        0x000B,
        (
            '市长被逮捕了，\n',
            '真让人松了一口气啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '戴尔蒙家族没有继承人，\n',
            '下一任的市长是不是\n',
            '必须要全民公选了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E01')

    def _loc_782(): pass

    label('loc_782')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_8B0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_831',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x000B,
        (
            '听说传闻中的公爵要到这一带来视察，\n',
            '我就去看了一下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '结果根本没有那样一个人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '倒是有一个穿着奇装异服的大叔\n',
            '一直在用奇怪的说话方式叫嚷着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8AD')

    def _loc_831(): pass

    label('loc_831')

    ChrTalk(
        0x000B,
        (
            '听说传闻中的公爵要到这一带来视察，\n',
            '我就去看了一下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '我没有看到公爵，\n',
            '倒是有一个穿着奇装异服的大叔在吵吵嚷嚷的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8AD(): pass

    label('loc_8AD')

    Jump('loc_E01')

    def _loc_8B0(): pass

    label('loc_8B0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            Expr.Return,
        ),
        'loc_A33',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_9BC',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x000B,
        (
            '戴尔蒙市长虽然\n',
            '极力推进旅游业……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '但是采取了强硬的措施，\n',
            '反对者也不少。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '希望他能够和本地居民\n',
            '相处得再融洽一点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '……在推动旅游事业之前，\n',
            '应该先对渡鸦帮采取些措施才对吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '有他们这些人在，\n',
            '不正是给作为旅游胜地的卢安抹黑吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A30')

    def _loc_9BC(): pass

    label('loc_9BC')

    ChrTalk(
        0x000B,
        (
            '在推动旅游事业之前，\n',
            '应该先对渡鸦帮采取些措施才对吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '有他们这些人在，\n',
            '不正是给作为旅游胜地的卢安抹黑吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A30(): pass

    label('loc_A30')

    Jump('loc_E01')

    def _loc_A33(): pass

    label('loc_A33')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_AA6',
    )

    ChrTalk(
        0x000B,
        (
            '最近，\n',
            '王立学院的学生们\n',
            '来买了不少照明和烹饪的器具。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '这么说的话……\n',
            '就快要到学园祭的时候了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E01')

    def _loc_AA6(): pass

    label('loc_AA6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_B5A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B36',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x000B,
        (
            '啊……\n',
            '快到吃午饭的时间了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '饿着肚子可没法做生意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '真想吃啊……\n',
            '卢安的孩子们最喜欢的\n',
            '加了许多虾的杂菜烩饭。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B57')

    def _loc_B36(): pass

    label('loc_B36')

    ChrTalk(
        0x000B,
        (
            '啊……\n',
            '快到吃午饭的时间了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B57(): pass

    label('loc_B57')

    Jump('loc_E01')

    def _loc_B5A(): pass

    label('loc_B5A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_C8C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C23',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x000B,
        (
            '我听嘉恩那小子说了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '昨天有一位王族出身的人物\n',
            '来到卢安了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '那位与艾莉茜雅女王\n',
            '拥有相同血统的人\n',
            '一定是位举止高雅的人吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '趁他在卢安的时候，\n',
            '我一定要去见见他。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C89')

    def _loc_C23(): pass

    label('loc_C23')

    ChrTalk(
        0x000B,
        (
            '昨天有一位王族出身的人物\n',
            '来到卢安了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '与艾莉茜雅女王拥有相同血统，\n',
            '一定是位举止高雅的人吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C89(): pass

    label('loc_C89')

    Jump('loc_E01')

    def _loc_C8C(): pass

    label('loc_C8C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 0, 0x418)),
            Expr.Return,
        ),
        'loc_CF4',
    )

    ChrTalk(
        0x000B,
        (
            '你们去看过伦格兰德大桥了吗？\n',
            '那里很值得一看哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '不管怎么说，\n',
            '它可是这座城市的标志。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E01')

    def _loc_CF4(): pass

    label('loc_CF4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_E01',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_DAA',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x000B,
        (
            '今天的观光客特别多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '听说如果没有向酒店预订房间，\n',
            '是没办法在酒店里住下来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '说起来在以前，\n',
            '那些没有地方住宿的客人，\n',
            '游击士协会会向他们提供住所。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E01')

    def _loc_DAA(): pass

    label('loc_DAA')

    ChrTalk(
        0x000B,
        (
            '今天的观光客特别多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '听说如果没有向酒店预订房间，\n',
            '是没办法在酒店里住下来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E01(): pass

    label('loc_E01')

    TalkEnd(0x000B)

    Return()

# id: 0x0005 offset: 0xE05
@scena.Code('func_05_E05')
def func_05_E05():
    TalkBegin(0x000C)

    If(
        (
            (Expr.Eval, "OP_40(0x0067)"),
            (Expr.Eval, "OP_29(0x0022, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_E1A',
    )

    EventBegin(0x00)

    def _loc_E1A(): pass

    label('loc_E1A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_E67',
    )

    ChrTalk(
        0x00FE,
        (
            '今天谢谢你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果再有什么事情的话，\n',
            '还得麻烦你们哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1906')

    def _loc_E67(): pass

    label('loc_E67')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_1214',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0022, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_EFA',
    )

    ChrTalk(
        0x00FE,
        (
            '呀，之前真是帮了我大忙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '后来我这边的工作\n',
            '也进行得很顺利。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，\n',
            '差不多该回蔡斯去了。\n',
            '要赶快把零碎的事情做完。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1211')

    def _loc_EFA(): pass

    label('loc_EFA')

    If(
        (
            (Expr.Eval, "OP_29(0x0022, 0x00, 0x04)"),
            Expr.Return,
        ),
        'loc_FC1',
    )

    ChrTalk(
        0x00FE,
        (
            '#1890170917V如果在阿伊纳街道周围\n',
            '找到导力枪的话，\n',
            '就拿过来给我看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890170918V那可能是我\n',
            '丢失的试制品也说不定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890170919V我打算马上就回蔡斯去。\n',
            '所以请尽量快一点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1211')

    def _loc_FC1(): pass

    label('loc_FC1')

    ChrTalk(
        0x00FE,
        (
            '#1890170907V为了对正在开发中的\n',
            '导力枪进行市场调查，\n',
            '我从蔡斯来到这里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890170908V途经阿伊纳街道的时候\n',
            '遭到凶暴魔兽的追击。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890170909V我丢下装有重要试制品的袋子，\n',
            '好不容易逃到了这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x0022, 0x00, 0x02)"),
            Expr.Return,
        ),
        'loc_1153',
    )

    OP_28(0x0022, 0x04, 0x08)
    OP_28(0x0022, 0x04, 0x04)
    OP_28(0x0022, 0x01, 0x0001)
    OP_28(0x0022, 0x01, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010170913V#000F啊，我们从公告板上看到了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170914V丢失的是试制的导力枪吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#1890170915V嗯，是的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890170916V拜托你们把它找回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1211')

    def _loc_1153(): pass

    label('loc_1153')

    OP_28(0x0022, 0x04, 0x08)
    OP_28(0x0022, 0x04, 0x04)
    OP_28(0x0022, 0x04, 0x02)
    OP_28(0x0022, 0x01, 0x0001)
    OP_28(0x0022, 0x01, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010170910V#002F和游击士协会联络了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#1890170911V是啊，而且很快就安排好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890170912V公告板上也应该出来了，\n',
            '一旦找到了请赶快来通知我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1211(): pass

    label('loc_1211')

    Jump('loc_1906')

    def _loc_1214(): pass

    label('loc_1214')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_15A0',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0022, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_128C',
    )

    ChrTalk(
        0x00FE,
        (
            '呀，之前真是帮了大忙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '后来我这边的工作\n',
            '也进行得很顺利。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么……\n',
            '我就先去工作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_159D')

    def _loc_128C(): pass

    label('loc_128C')

    If(
        (
            (Expr.Eval, "OP_29(0x0022, 0x00, 0x04)"),
            Expr.Return,
        ),
        'loc_134D',
    )

    ChrTalk(
        0x00FE,
        (
            '#1890170917V如果在阿伊纳街道周围\n',
            '找到导力枪的话，\n',
            '就拿过来给我看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890170918V那可能是我\n',
            '丢失的试制品也说不定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890170932V那么……\n',
            '这个先放一边，工作要紧啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_159D')

    def _loc_134D(): pass

    label('loc_134D')

    ChrTalk(
        0x00FE,
        (
            '#1890170907V为了对正在开发中的\n',
            '导力枪进行市场调查，\n',
            '我从蔡斯来到这里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890170908V途经阿伊纳街道的时候\n',
            '遭到凶暴魔兽的追击。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890170909V我丢下装有重要试制品的袋子，\n',
            '好不容易逃到了这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x0022, 0x00, 0x02)"),
            Expr.Return,
        ),
        'loc_14DF',
    )

    OP_28(0x0022, 0x04, 0x08)
    OP_28(0x0022, 0x04, 0x04)
    OP_28(0x0022, 0x01, 0x0001)
    OP_28(0x0022, 0x01, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010170913V#000F啊，我们从公告板上看到了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170914V丢失的是试制的导力枪吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#1890170915V嗯，是的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890170916V拜托你们把它找回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_159D')

    def _loc_14DF(): pass

    label('loc_14DF')

    OP_28(0x0022, 0x04, 0x08)
    OP_28(0x0022, 0x04, 0x04)
    OP_28(0x0022, 0x04, 0x02)
    OP_28(0x0022, 0x01, 0x0001)
    OP_28(0x0022, 0x01, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010170910V#002F和游击士协会联络了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#1890170911V是啊，而且很快就安排好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890170912V公告板上也应该出来了，\n',
            '一旦找到了请赶快来通知我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_159D(): pass

    label('loc_159D')

    Jump('loc_1906')

    def _loc_15A0(): pass

    label('loc_15A0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 6, 0x41E)),
            Expr.Return,
        ),
        'loc_1906',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0022, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_162A',
    )

    ChrTalk(
        0x00FE,
        (
            '呀，之前真是帮了大忙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '后来我这边的工作\n',
            '也进行得很顺利。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果再有什么事的话，\n',
            '到时候还得麻烦你们呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1906')

    def _loc_162A(): pass

    label('loc_162A')

    If(
        (
            (Expr.Eval, "OP_29(0x0022, 0x00, 0x04)"),
            Expr.Return,
        ),
        'loc_16B6',
    )

    ChrTalk(
        0x00FE,
        (
            '#1890170917V如果在阿伊纳街道周围\n',
            '找到导力枪的话，\n',
            '就拿过来给我看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890170918V那可能是我\n',
            '丢失的试制品也说不定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1906')

    def _loc_16B6(): pass

    label('loc_16B6')

    ChrTalk(
        0x00FE,
        (
            '#1890170907V为了对正在开发中的\n',
            '导力枪进行市场调查，\n',
            '我从蔡斯来到这里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890170908V途经阿伊纳街道的时候\n',
            '遭到凶暴魔兽的追击。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890170909V我丢下装有重要试制品的袋子，\n',
            '好不容易逃到了这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x0022, 0x00, 0x02)"),
            Expr.Return,
        ),
        'loc_1848',
    )

    OP_28(0x0022, 0x04, 0x08)
    OP_28(0x0022, 0x04, 0x04)
    OP_28(0x0022, 0x01, 0x0001)
    OP_28(0x0022, 0x01, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010170913V#000F啊，我们从公告板上看到了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170914V丢失的是试制的导力枪吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#1890170915V嗯，是的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890170916V拜托你们把它找回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1906')

    def _loc_1848(): pass

    label('loc_1848')

    OP_28(0x0022, 0x04, 0x08)
    OP_28(0x0022, 0x04, 0x04)
    OP_28(0x0022, 0x04, 0x02)
    OP_28(0x0022, 0x01, 0x0001)
    OP_28(0x0022, 0x01, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010170910V#002F和游击士协会联络了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#1890170911V是啊，而且很快就安排好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890170912V公告板上也应该出来了，\n',
            '一旦找到了请赶快来通知我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1906(): pass

    label('loc_1906')

    If(
        (
            (Expr.Eval, "OP_40(0x0067)"),
            (Expr.Eval, "OP_29(0x0022, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_191A',
    )

    Call(1, 0x0004)

    def _loc_191A(): pass

    label('loc_191A')

    TalkEnd(0x000C)

    Return()

# id: 0x0006 offset: 0x191E
@scena.Code('func_06_191E')
def func_06_191E():
    TalkBegin(0x000D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            Expr.Return,
        ),
        'loc_198C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_197A',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '哈……哈……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '从玛诺利亚村\n',
            '一口气走到这里，\n',
            '果然很累人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_198C')

    def _loc_197A(): pass

    label('loc_197A')

    ChrTalk(
        0x00FE,
        (
            '哈……哈……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_198C(): pass

    label('loc_198C')

    TalkEnd(0x000D)

    Return()

# id: 0x0007 offset: 0x1990
@scena.Code('func_07_1990')
def func_07_1990():
    Call(0, 0x0008)

    Return()

# id: 0x0008 offset: 0x1995
@scena.Code('func_08_1995')
def func_08_1995():
    TalkBegin(0x000E)
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
        1,
        (
            TXT(0x00, '对话\n'),
            TXT(0x01, '买东西\n'),
            TXT(0x02, '离开\n'),
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
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_19FF',
    )

    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 4, 0x42C)),
            Expr.Return,
        ),
        'loc_19F7',
    )

    OP_A9(0x32)

    Jump('loc_19F9')

    def _loc_19F7(): pass

    label('loc_19F7')

    OP_A9(0x1F)

    def _loc_19F9(): pass

    label('loc_19F9')

    OP_56(0x00)
    TalkEnd(0x000E)

    Return()

    def _loc_19FF(): pass

    label('loc_19FF')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1A10',
    )

    TalkEnd(0x000E)

    Return()

    def _loc_1A10(): pass

    label('loc_1A10')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_1A80',
    )

    ChrTalk(
        0x000E,
        (
            '呼～是戴尔蒙市长啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '虽然我很讨厌他那种\n',
            '做作的演技和态度，\n',
            '可是没想到他会做到这种地步……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_20CB')

    def _loc_1A80(): pass

    label('loc_1A80')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_1BAD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1B3E',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x000E,
        (
            '刚才在街上有一个\n',
            '发型很奇怪的大叔向我搭讪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '虽然他看上去很有钱，\n',
            '但是他太随便，不是个品德高尚的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '是卢安男人的素质都下降了呢。\n',
            '还是说他只是个观光客……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1BAA')

    def _loc_1B3E(): pass

    label('loc_1B3E')

    ChrTalk(
        0x000E,
        (
            '刚才在街上有一个\n',
            '发型很奇怪的大叔向我搭讪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '是卢安男人的素质都下降了呢。\n',
            '还是说他只是个观光客……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1BAA(): pass

    label('loc_1BAA')

    Jump('loc_20CB')

    def _loc_1BAD(): pass

    label('loc_1BAD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            Expr.Return,
        ),
        'loc_1C87',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1C5B',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x000E,
        (
            '妹妹她们的学园祭\n',
            '真是让我很开心呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '不过那孩子好像\n',
            '不太愿意让我去看……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '呵呵，这是监护人的义务呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '我很认真地观赏了\n',
            '她们的舞台剧哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C84')

    def _loc_1C5B(): pass

    label('loc_1C5B')

    ChrTalk(
        0x000E,
        (
            '妹妹她们的学园祭\n',
            '真是让我很开心呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C84(): pass

    label('loc_1C84')

    Jump('loc_20CB')

    def _loc_1C87(): pass

    label('loc_1C87')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_1CF4',
    )

    ChrTalk(
        0x000E,
        (
            '呼呼，马上就要到学园祭了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '我妹妹好像也要在舞台剧中登场，\n',
            '不知道她到底演的是什么角色。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_20CB')

    def _loc_1CF4(): pass

    label('loc_1CF4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_1E5D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1DDE',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x000E,
        (
            '在百日战役中王国军的事迹\n',
            '被宣传得轰轰烈烈……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '不过实际上，\n',
            '都是靠某位上校制定的作战计划\n',
            '赶走帝国军的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '但是，\n',
            '那位上校现在在哪里做什么，\n',
            '我就完全没有听说过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '嘿嘿，我很想知道他是个怎样的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E5A')

    def _loc_1DDE(): pass

    label('loc_1DDE')

    ChrTalk(
        0x000E,
        (
            '百日战役中，\n',
            '就是靠某位上校制定的作战计划\n',
            '赶走帝国军的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '但是，\n',
            '那位上校现在在哪里做什么，\n',
            '我就完全没有听说过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1E5A(): pass

    label('loc_1E5A')

    Jump('loc_20CB')

    def _loc_1E5D(): pass

    label('loc_1E5D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_1EC3',
    )

    ChrTalk(
        0x000E,
        (
            '嘿嘿，我来到这个城市\n',
            '已经有十年了呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '不过只有年龄在增长，\n',
            '却没有干成什么事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_20CB')

    def _loc_1EC3(): pass

    label('loc_1EC3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 0, 0x418)),
            Expr.Return,
        ),
        'loc_1FEE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1F87',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x000E,
        (
            '呵呵，游击士真辛苦呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '拥有很大权限的同时\n',
            '也背负了很大的责任啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '有责任感的人\n',
            '才能成为可靠的游击士啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '不过这样的人有时也会\n',
            '为某件事过分自责而消沉下去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1FEB')

    def _loc_1F87(): pass

    label('loc_1F87')

    ChrTalk(
        0x000E,
        (
            '有责任感的人\n',
            '才能成为可靠的游击士啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '不过这样的人有时也会\n',
            '为某件事过分自责而消沉下去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1FEB(): pass

    label('loc_1FEB')

    Jump('loc_20CB')

    def _loc_1FEE(): pass

    label('loc_1FEE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_20CB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_20A0',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x000E,
        (
            '啊～欢迎光临。\n',
            '好可爱的游击士呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '……不对，那个徽章，\n',
            '确切地说应该是准游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F哎～你知道得真清楚呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '呵呵，我的阅历可是不浅的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_20CB')

    def _loc_20A0(): pass

    label('loc_20A0')

    ChrTalk(
        0x000E,
        (
            '呵呵，欢迎欢迎。\n',
            '两位可爱的准游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_20CB(): pass

    label('loc_20CB')

    TalkEnd(0x000E)

    Return()

# id: 0x0009 offset: 0x20CF
@scena.Code('func_09_20CF')
def func_09_20CF():
    TalkBegin(0x000F)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 0, 0x418)),
            Expr.Return,
        ),
        'loc_2126',
    )

    ChrTalk(
        0x00FE,
        (
            '学校放假\n',
            '就到今天为止了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '明天开始又要上课了，\n',
            '我要去准备一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_22E9')

    def _loc_2126(): pass

    label('loc_2126')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_22E9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_22AE',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))
    ChrTurnDirection(0x00FE, 0x0136, 0)

    ChrTalk(
        0x00FE,
        (
            '咦，科洛丝前辈。\n',
            '来卢安有什么事情吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0136,
        (
            '#040F嗯，\n',
            '我正在带两位朋友参观这里呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F（是她在学院里的同学吗？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F（嗯，应该没错。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0136,
        (
            '#040F妮吉塔今天\n',
            '在家里休息是吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，\n',
            '今天没有社团活动……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说起来，前辈。\n',
            '『那个』已经决定了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0136,
        (
            '#045F还、还没有呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是吗……\n',
            '如果能早点决定就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#501F（『那个』是什么呢……？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_22E9')

    def _loc_22AE(): pass

    label('loc_22AE')

    ChrTurnDirection(0x00FE, 0x0136, 0)

    ChrTalk(
        0x00FE,
        (
            '科洛丝前辈，\n',
            '难得来城里一次，\n',
            '就好好逛逛街吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_22E9(): pass

    label('loc_22E9')

    TalkEnd(0x000F)

    Return()

# id: 0x000A offset: 0x22ED
@scena.Code('func_0A_22ED')
def func_0A_22ED():
    TalkBegin(0x0008)
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
        1,
        (
            TXT(0x00, '对话\n'),
            TXT(0x01, '报告\n'),
            TXT(0x02, '离开\n'),
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
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2443',
    )

    OP_0D()

    If(
        (
            (Expr.Eval, "OP_A9(0x22)"),
            Expr.Return,
        ),
        'loc_23C3',
    )

    Sleep(200)

    ChrTalk(
        0x0008,
        (
            '#0500061979V#650F辛苦了。\n',
            '看来目的顺利地达成了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500061980V如果完成其他任务的话，\n',
            '随时都可以来向我报告。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_243D')

    def _loc_23C3(): pass

    label('loc_23C3')

    Sleep(200)

    ChrTalk(
        0x0008,
        (
            '#0500061981V#650F你们现在好像\n',
            '没有需要报告的任务哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500061982V如果完成其他任务的话，\n',
            '随时都可以来向我报告。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_243D(): pass

    label('loc_243D')

    OP_56(0x00)
    TalkEnd(0x0008)

    Return()

    def _loc_2443(): pass

    label('loc_2443')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2454',
    )

    TalkEnd(0x0008)

    Return()

    def _loc_2454(): pass

    label('loc_2454')

    Call(0, 0x000B)

    Return()

# id: 0x000B offset: 0x2459
@scena.Code('func_0B_2459')
def func_0B_2459():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_2572',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2535',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x0008,
        (
            '#0500070130V#650F这就准备前往蔡斯地区了吗？\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500070131V如果在蔡斯能找到\n',
            '黑色导力器的线索就好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500070132V#651F期待你们能早日成为正游击士，\n',
            '并让我们也沾沾光，\n',
            '好让大家一起庆祝一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_256F')

    def _loc_2535(): pass

    label('loc_2535')

    ChrTalk(
        0x0008,
        (
            '#0500070133V#654F不过这样一来\n',
            '卢安这边就变得麻烦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_256F(): pass

    label('loc_256F')

    Jump('loc_34BF')

    def _loc_2572(): pass

    label('loc_2572')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_25ED',
    )

    ChrTalk(
        0x0008,
        (
            '#0500061434V#652F明白了吗？\n',
            '总之靠你们帮我拖延时间了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500061435V在王国军赶到之前\n',
            '一定要想办法留住市长。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_34BF')

    def _loc_25ED(): pass

    label('loc_25ED')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            Expr.Return,
        ),
        'loc_27FD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2758',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x0008,
        (
            '#0500060995V#653F啊呀，是你们啊……\n',
            '院长的事情我已经听说了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500060996V#652F很不巧，梅尔茨出去办事了，\n',
            '阿加特也去调查了，还没有回来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500060997V虽然学院的工作才刚结束，\n',
            '不过很抱歉，\n',
            '你们能马上去一次玛诺利亚村吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010060998V#002F嗯，交给我们吧！\n',
            '您不用这么客气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020060999V#012F那要赶快上路了。\n',
            '我也很担心卡露娜小姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_27FA')

    def _loc_2758(): pass

    label('loc_2758')

    ChrTalk(
        0x0008,
        (
            '#0500061000V#652F很不巧，梅尔茨出去办事了，\n',
            '阿加特也去调查了，还没有回来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500061001V虽然学院的工作才刚结束，\n',
            '不过很抱歉，\n',
            '你们能马上去一次玛诺利亚村吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_27FA(): pass

    label('loc_27FA')

    Jump('loc_34BF')

    def _loc_27FD(): pass

    label('loc_27FD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_297F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_28E3',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x0008,
        (
            '#0500050969V#650F对平民的协助、对地区的贡献，\n',
            '这是一份非常有意义的好工作呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500050970V希望你们出演学园祭的舞台剧，\n',
            '这个委托我还是第一次碰到呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500050971V#651F那么，我就等着你们的报告了。\n',
            '加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_297C')

    def _loc_28E3(): pass

    label('loc_28E3')

    ChrTalk(
        0x0008,
        (
            '#0500050972V#650F对平民的协助、对地区的贡献，\n',
            '这是一份非常有意义的好工作呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500050973V希望你们出演学园祭的舞台剧，\n',
            '这个委托我还是第一次碰到呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_297C(): pass

    label('loc_297C')

    Jump('loc_34BF')

    def _loc_297F(): pass

    label('loc_297F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_2B09',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2AA9',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x0008,
        (
            '#0500050583V#653F哦，是你们俩啊。\n',
            '孤儿院那里怎样了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010050584V#002F啊，那个……\n',
            '虽然调查暂时告一个段落了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020050585V#012F不过碰到了一点麻烦……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020050586V#010F稍后再过来提交工作报告。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500050587V#652F……你们好像很急。\n',
            '那我就等着你们的报告。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2B06')

    def _loc_2AA9(): pass

    label('loc_2AA9')

    ChrTalk(
        0x0008,
        (
            '#0500050588V#652F有什么事情一会儿再来报告吧。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500050589V你们现在不是有急事吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2B06(): pass

    label('loc_2B06')

    Jump('loc_34BF')

    def _loc_2B09(): pass

    label('loc_2B09')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 6, 0x41E)),
            Expr.Return,
        ),
        'loc_2B97',
    )

    ChrTalk(
        0x0008,
        (
            '#0500050137V#652F孤儿院发生了火灾，\n',
            '而且院长和孩子们的情况还没有得以确认。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500050138V这些都是你们\n',
            '要进行详细调查的范围。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_34BF')

    def _loc_2B97(): pass

    label('loc_2B97')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_33A1',
    )

    EventBegin(0x00)
    Fade(1000)
    ChrSetPos(0x0101, -3490, 0, 45210, 270)
    ChrSetPos(0x0102, -3520, 0, 44250, 270)
    CameraMove(-5640, 0, 45060, 0)
    ChrSetDirection(0x0008, 90, 0)
    OP_4A(0x0008, 255)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010050106V#001F嘉恩哥哥，早啊～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020050107V#010F早上好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500050108V#650F哟，早上好。\n',
            '这么早就来了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010050109V#006F嗯，约好的嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020050110V#010F抱歉有点心急了，\n',
            '能安排一些工作给我们做吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500050111V#651F嗯，没问题！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500050112V有很多事想请你们帮忙来着，\n',
            '嗯，选哪一件好呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010050113V#008F请、请手下留情……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    LoadEffect(0x00, 'map\\\\mp001_00.eff')
    PlayEffect(0x00, 0x00, 0x00FF, -6670, 1900, 46840, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(195, 0x00, 0x64)
    Sleep(500)

    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0500050114V#653F哎……？\n',
            '你们稍等一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0008, 0, 400)

    @scena.Lambda('lambda_2DF3')
    def lambda_2DF3():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_2DF3')

    DispatchAsync2(0x0101, 0x0002, lambda_2DF3)

    @scena.Lambda('lambda_2E04')
    def lambda_2E04():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_2E04')

    DispatchAsync2(0x0102, 0x0002, lambda_2E04)

    @scena.Lambda('lambda_2E15')
    def lambda_2E15():
        CameraMove(-5530, 0, 45850, 1200)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_2E15)

    ChrWalkTo(0x0008, -5980, 0, 46770, 3000, 0x00)
    ChrSetDirection(0x0008, 270, 400)
    Sleep(500)

    LoadEffect(0x01, 'map\\\\mp001_01.eff')
    PlayEffect(0x01, 0x00, 0x00FF, -6670, 1900, 46840, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(131, 0x00, 0x64)
    OP_23(0x00C3)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0500050115V#650F您好，这里是游击士协会。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500050116V哟，是白之木莲亭……\n',
            '说来你们也很久没发联络过来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500050117V你那里的古董通信器\n',
            '竟然还能用啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500050118V#653F………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500050119V#652F………………什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000005DC)
    OP_62(0x0101, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(1500)

    ChrTalk(
        0x0008,
        (
            '#0500050120V#652F是吗……\n',
            '这事可严重了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500050121V好，知道了。\n',
            '我马上派人过去了解情况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(131, 0x00, 0x64)
    StopEffect(0x00, 0x00)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010050122V#002F怎么了？\n',
            '出什么事了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#0500050123V#652F现在还不知道是\n',
            '事故还是人为的案件……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500050124V昨天晚上， \n',
            '海道边的孤儿院发生了火灾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    PlayBGM(86)

    ChrTalk(
        0x0101,
        (
            '#0010050125V#004F不、不会吧……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020050126V#012F已经确定了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3162')
    def lambda_3162():
        CameraMove(-5640, 0, 45060, 1200)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_3162)

    ChrWalkTo(0x0008, -5700, 0, 45100, 3000, 0x00)
    ChrSetDirection(0x0008, 90, 400)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)

    ChrTalk(
        0x0008,
        (
            '#0500050127V#652F是玛诺利亚旅店的主人\n',
            '特地发了联络通知我们的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500050128V是座名叫玛西亚的孤儿院，\n',
            '你们知道那里吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010050129V#003F何、何止知道……\n',
            '昨天下午我们还去过呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020050130V#012F那么，\n',
            '特蕾莎院长和那些孩子都还好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500050131V#652F这个还没确认。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500050132V总之，要先去调查一下，\n',
            '还要确认一下他们是否平安。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500050133V……可以拜托你们去吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010050134V#005F那还用说！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020050135V#012F那我们马上\n',
            '赶去孤儿院了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500050136V#652F好，拜托了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))
    SetScenaFlags(ScenaFlag(0x0083, 6, 0x41E))
    OP_28(0x003B, 0x04, 0x02)
    OP_28(0x003B, 0x04, 0x04)
    EventEnd(0x00)
    OP_4B(0x0008, 255)

    Jump('loc_34BF')

    def _loc_33A1(): pass

    label('loc_33A1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 0, 0x418)),
            Expr.Return,
        ),
        'loc_34BF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3456',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x0008,
        (
            '#0500041202V#650F哎呀，这个时候你们能来\n',
            '真是帮了我大忙了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500041203V明天开始就会有很多的工作需要你们去做，\n',
            '到时就拜托了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500041204V#651F请多关照！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_34BF')

    def _loc_3456(): pass

    label('loc_3456')

    ChrTalk(
        0x0008,
        (
            '#0500041205V#650F明天开始就会有很多的工作需要你们去做，\n',
            '到时就拜托了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500041206V#651F请多关照！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_34BF(): pass

    label('loc_34BF')

    TalkEnd(0x0008)

    Return()

# id: 0x000C offset: 0x34C3
@scena.Code('func_0C_34C3')
def func_0C_34C3():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_36E1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3656',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '#0320070134V#831F呀，是你们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070135V#001F啊，卡露娜姐姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070136V#010F身体已经没什么事了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0320070137V#830F啊，已经好了。\n',
            '今天开始继续执行任务。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320070138V#835F这次给你们两个\n',
            '添了许多麻烦，\n',
            '不向你们道谢就太说不过去了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070139V#008F哪里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0320070140V#830F你们成为正游击士后\n',
            '一定要再来卢安玩啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320070141V我等着你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_36DE')

    def _loc_3656(): pass

    label('loc_3656')

    ChrTalk(
        0x00FE,
        (
            '#0320070142V#830F这次给你们两个\n',
            '添了许多麻烦，\n',
            '不向你们道谢就太说不过去了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320070143V你们成为正游击士后\n',
            '一定要再来卢安玩啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_36DE(): pass

    label('loc_36DE')

    Jump('loc_3B49')

    def _loc_36E1(): pass

    label('loc_36E1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_37D7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3776',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '#0320050974V#830F事情我都听嘉恩说了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320050975V学园祭的警卫工作\n',
            '已经决定由我来负责了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320050976V那天就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_37D4')

    def _loc_3776(): pass

    label('loc_3776')

    ChrTalk(
        0x00FE,
        (
            '#0320050977V#830F学园祭的警卫工作\n',
            '已经决定由我来负责了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320050978V那天就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_37D4(): pass

    label('loc_37D4')

    Jump('loc_3B49')

    def _loc_37D7(): pass

    label('loc_37D7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_392E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_38A1',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '#0320050139V#835F最近到卢安来的\n',
            '观光游客大大增加了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320050140V所以事件也多了不少，\n',
            '护送旅客啊，寻找遗失物品啊，\n',
            '真是忙死人了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320050141V哎呀～\n',
            '你们能来真是帮了大忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_392B')

    def _loc_38A1(): pass

    label('loc_38A1')

    ChrTalk(
        0x00FE,
        (
            '#0320050142V#835F最近到卢安来的\n',
            '观光游客大大增加了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320050143V所以事件也多了不少，\n',
            '护送旅客啊，寻找遗失物品啊，\n',
            '真是忙死人了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_392B(): pass

    label('loc_392B')

    Jump('loc_3B49')

    def _loc_392E(): pass

    label('loc_392E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 0, 0x418)),
            Expr.Return,
        ),
        'loc_3AD1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3A52',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '#0320041207V#831F转属手续完成了吗？\n',
            '今后我们就是同伴了哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320041208V#833F这个支部除了我，\n',
            '还有一个和你们一样\n',
            '也是准游击士的同伴。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320041209V听说那家伙是\n',
            '临时调配过来的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320041210V……………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320041211V#830F呵呵，总之以后多多关照了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3ACE')

    def _loc_3A52(): pass

    label('loc_3A52')

    ChrTalk(
        0x00FE,
        (
            '#0320041212V#830F这个支部除了我，\n',
            '还有一个和你们一样\n',
            '也是准游击士的同伴。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320041213V听说那家伙是\n',
            '临时调配过来的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3ACE(): pass

    label('loc_3ACE')

    Jump('loc_3B49')

    def _loc_3AD1(): pass

    label('loc_3AD1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_3B49',
    )

    ChrTalk(
        0x00FE,
        (
            '#0320040967V#830F要办转属手续的话，\n',
            '嘉恩不回来可办不了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320040968V不如先去街上逛逛，\n',
            '打发一下时间如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3B49(): pass

    label('loc_3B49')

    TalkEnd(0x0009)

    Return()

# id: 0x000D offset: 0x3B4D
@scena.Code('func_0D_3B4D')
def func_0D_3B4D():
    TalkBegin(0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_3B8C',
    )

    ChrTalk(
        0x00FE,
        (
            '听说市长被捕了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……到底是怎么回事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3DAC')

    def _loc_3B8C(): pass

    label('loc_3B8C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_3BEF',
    )

    ChrTalk(
        0x00FE,
        (
            '昨天，卡露娜小姐到学园做警卫之后，\n',
            '到现在也没有回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是不是发生什么事情了呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3DAC')

    def _loc_3BEF(): pass

    label('loc_3BEF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_3CCE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3C90',
    )

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x00FE,
        (
            '卡露娜小姐去学园当警卫的时候，\n',
            '我在这里也要努力才行！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……啊、啊嚏！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0010, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '……唉，在这之前先要把感冒治好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3CCB')

    def _loc_3C90(): pass

    label('loc_3C90')

    ChrTalk(
        0x00FE,
        (
            '卡露娜小姐去学园当警卫的时候，\n',
            '我在这里也要努力才行！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3CCB(): pass

    label('loc_3CCB')

    Jump('loc_3DAC')

    def _loc_3CCE(): pass

    label('loc_3CCE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 0, 0x418)),
            Expr.Return,
        ),
        'loc_3DAC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3D5D',
    )

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x00FE,
        (
            '你们就是嘉恩所说的\n',
            '从柏斯来的新人吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我在考试中失败了许多次，\n',
            '前几天终于成为了准游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们互相加油吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3DAC')

    def _loc_3D5D(): pass

    label('loc_3D5D')

    ChrTalk(
        0x00FE,
        (
            '我在考试中失败了许多次，\n',
            '前几天终于成为了准游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们互相加油吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3DAC(): pass

    label('loc_3DAC')

    TalkEnd(0x0010)

    Return()

# id: 0x000E offset: 0x3DB0
@scena.Code('func_0E_3DB0')
def func_0E_3DB0():
    Call(0, 0x000F)

    Return()

# id: 0x000F offset: 0x3DB5
@scena.Code('func_0F_3DB5')
def func_0F_3DB5():
    TalkBegin(0x0011)
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
        1,
        (
            TXT(0x00, '对话\n'),
            TXT(0x01, '买东西\n'),
            TXT(0x02, '离开\n'),
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
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3E2B',
    )

    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0088, 2, 0x442)),
            Expr.Return,
        ),
        'loc_3E17',
    )

    OP_A9(0x2B)

    Jump('loc_3E25')

    def _loc_3E17(): pass

    label('loc_3E17')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_3E23',
    )

    OP_A9(0x26)

    Jump('loc_3E25')

    def _loc_3E23(): pass

    label('loc_3E23')

    OP_A9(0x20)

    def _loc_3E25(): pass

    label('loc_3E25')

    OP_56(0x00)
    TalkEnd(0x0011)

    Return()

    def _loc_3E2B(): pass

    label('loc_3E2B')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3E3C',
    )

    TalkEnd(0x0011)

    Return()

    def _loc_3E3C(): pass

    label('loc_3E3C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_3F56',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3F10',
    )

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x0011,
        (
            '没想到那个戴尔蒙市长\n',
            '竟然被逮捕了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '卢安的市长\n',
            '可是由戴尔蒙家族\n',
            '代代相传的职位啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '现在也没有其他继承人了，\n',
            '市长这一被逮捕\n',
            '不就什么都完了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '让我这个老者也为之震惊啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3F53')

    def _loc_3F10(): pass

    label('loc_3F10')

    ChrTalk(
        0x0011,
        (
            '哎呀～活了这么久，\n',
            '什么事情都见得差不多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '哇～哈～哈！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3F53(): pass

    label('loc_3F53')

    Jump('loc_489F')

    def _loc_3F56(): pass

    label('loc_3F56')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_40D2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_405E',
    )

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x0011,
        (
            '在这片广阔的大陆上……\n',
            '生活着很多国家的人们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '以你们的年龄来看，\n',
            '说不定今后能有机会\n',
            '去大陆各国巡游哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '与那些地方的人们见面，\n',
            '语言交流是很重要的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '如果你们想成为像我这样心胸宽广，\n',
            '而且崇高伟大的人的话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '哇～哈～哈！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_40CF')

    def _loc_405E(): pass

    label('loc_405E')

    ChrTalk(
        0x0011,
        (
            '在这片广阔的大陆上……\n',
            '生活着很多国家的人们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '以你们的年龄来看，\n',
            '说不定今后能有机会\n',
            '去大陆各国巡游哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_40CF(): pass

    label('loc_40CF')

    Jump('loc_489F')

    def _loc_40D2(): pass

    label('loc_40D2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            Expr.Return,
        ),
        'loc_41EA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4193',
    )

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x0011,
        (
            '如今每次看到海，\n',
            '我体内水手的血又沸腾起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '但是，\n',
            '现在船的动力装置都变成导力器了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '虽然方便了不少，\n',
            '但是总觉得有些失落……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '呼，\n',
            '我现在也上了年纪了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_41E7')

    def _loc_4193(): pass

    label('loc_4193')

    ChrTalk(
        0x0011,
        (
            '现在船的动力装置\n',
            '都变成导力器了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '虽然方便了不少，\n',
            '但是总觉得有些失落……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_41E7(): pass

    label('loc_41E7')

    Jump('loc_489F')

    def _loc_41EA(): pass

    label('loc_41EA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_433F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4313',
    )

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x0011,
        (
            '以前的埃雷波尼亚帝国的版图\n',
            '不是现在这个样子的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '反复的侵略，\n',
            '吞并了好几个国家与民族之后，\n',
            '成为了现在这样的大国。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '在国内，皇家掌握着绝对的权力，\n',
            '听说直到现在他们的统治也十分严厉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '连见惯大场面的我\n',
            '通过那个国家的领土时\n',
            '都会不禁紧张起来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '哇～哈～哈！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_433C')

    def _loc_4313(): pass

    label('loc_4313')

    ChrTalk(
        0x0011,
        (
            '怎么样，\n',
            '还想再听听我的冒险之旅吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_433C(): pass

    label('loc_433C')

    Jump('loc_489F')

    def _loc_433F(): pass

    label('loc_433F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_44EB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_44BF',
    )

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x0011,
        (
            '那还是在共和国\n',
            '附近海上航行的时候。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '那个时候的共和国\n',
            '政治还处于动荡的年代，\n',
            '治安也非常不好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '突然，\n',
            '载满客人的客船被海盗袭击了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '但是，作为海上男儿的我\n',
            '碰巧也在这艘船上，\n',
            '可谓是那些海盗的不幸了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '我把他们狠狠地打了一顿，\n',
            '狠狠地打……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '终于我把海盗们赶走了，\n',
            '然后就沉浸于带有异国风情的\n',
            '东方美女们的鼓掌喝彩声中了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '哇～哈～哈！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_44E8')

    def _loc_44BF(): pass

    label('loc_44BF')

    ChrTalk(
        0x0011,
        (
            '怎么样，\n',
            '还想再听听我的冒险之旅吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_44E8(): pass

    label('loc_44E8')

    Jump('loc_489F')

    def _loc_44EB(): pass

    label('loc_44EB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_4674',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_45F5',
    )

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x0011,
        (
            '这片大陆上有利贝尔、\n',
            '埃雷波尼亚、卡尔瓦德\n',
            '以及其他大大小小的国家。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '在卡尔瓦德的东面\n',
            '有着与利贝尔和埃雷波尼亚\n',
            '不同的文化圈。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '所以可以说共和国\n',
            '是融合了东方和西方\n',
            '各种不同文化的国家。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '呵呵，我以前也是\n',
            '驾船来往于各国之间的人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4671')

    def _loc_45F5(): pass

    label('loc_45F5')

    ChrTalk(
        0x0011,
        (
            '在卡尔瓦德的东面\n',
            '有着与利贝尔和埃雷波尼亚\n',
            '不同的文化圈。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '所以可以说共和国\n',
            '是融合了东方和西方\n',
            '各种不同文化的国家。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4671(): pass

    label('loc_4671')

    Jump('loc_489F')

    def _loc_4674(): pass

    label('loc_4674')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 0, 0x418)),
            Expr.Return,
        ),
        'loc_47D2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4765',
    )

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x0011,
        (
            '别看我现在这个样子，\n',
            '想当年我年轻气盛的时候曾经乘船到处冒险。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '为了寻求珍贵宝物，\n',
            '航海走遍了天涯海角呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '以前别人说起欧尼尔船长，\n',
            '就是指小有名气的本店长哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '就说给你们听听吧。\n',
            '我的那些光辉的冒险故事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_47CF')

    def _loc_4765(): pass

    label('loc_4765')

    ChrTalk(
        0x0011,
        (
            '以前别人说起欧尼尔船长，\n',
            '就是指小有名气的本店长哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '就说给你们听听吧。\n',
            '我的那些光辉的冒险故事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_47CF(): pass

    label('loc_47CF')

    Jump('loc_489F')

    def _loc_47D2(): pass

    label('loc_47D2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_489F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4863',
    )

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x0011,
        (
            '咳咳！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '我年轻的时候\n',
            '曾经只身单船出海，\n',
            '周游各个国家做买卖呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '卢安原本就是个\n',
            '聚集了如此多\n',
            '热血男人的地方啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_489F')

    def _loc_4863(): pass

    label('loc_4863')

    ChrTalk(
        0x0011,
        (
            '我年轻的时候\n',
            '曾经只身单船出海，\n',
            '周游各个国家做买卖呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_489F(): pass

    label('loc_489F')

    TalkEnd(0x0011)

    Return()

# id: 0x0010 offset: 0x48A3
@scena.Code('func_10_48A3')
def func_10_48A3():
    TalkBegin(0x0012)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_48F3',
    )

    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    ChrTalk(
        0x00FE,
        (
            '最初明明说\n',
            '只是来看看的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最终，还是买了不少东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4943')

    def _loc_48F3(): pass

    label('loc_48F3')

    ChrTalk(
        0x00FE,
        (
            '不过说起来，\n',
            '这里的店长话还真多……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '自从我们来了之后\n',
            '就一直讲个不停。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4943(): pass

    label('loc_4943')

    TalkEnd(0x0012)

    Return()

# id: 0x0011 offset: 0x4947
@scena.Code('func_11_4947')
def func_11_4947():
    TalkBegin(0x0013)

    ChrTalk(
        0x00FE,
        (
            '难得来一次，\n',
            '光看可不行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0013)

    Return()

# id: 0x0012 offset: 0x496F
@scena.Code('func_12_496F')
def func_12_496F():
    TalkBegin(0x0016)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_49C0',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，\n',
            '还没有找到合适的地图。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '再去找欧尼尔爷爷\n',
            '商量一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_49DF')

    def _loc_49C0(): pass

    label('loc_49C0')

    ChrTalk(
        0x00FE,
        (
            '嗯～\n',
            '没有再好点的地图吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_49DF(): pass

    label('loc_49DF')

    TalkEnd(0x0016)

    Return()

# id: 0x0013 offset: 0x49E3
@scena.Code('func_13_49E3')
def func_13_49E3():
    EventBegin(0x00)
    CameraMove(-20, 0, 40420, 0)
    CameraSetDistance(2800, 0)
    ChrSetFlags(0x0008, 0x0080)
    ChrSetPos(0x0101, -170, 0, 40420, 0)
    ChrSetPos(0x0102, 790, 0, 39400, 0)
    ChrSetPos(0x0136, -610, 0, 39400, 0)
    FadeIn(2000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010040935V#000F打扰了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CameraMove(-2850, 0, 44550, 1000)

    @scena.Lambda('lambda_4A77')
    def lambda_4A77():
        ChrWalkTo(0x00FE, -3150, 0, 44210, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_4A77)

    @scena.Lambda('lambda_4A92')
    def lambda_4A92():
        ChrSetDirection(0x00FE, 270, 0)
        Yield()

        Jump('lambda_4A92')

    DispatchAsync2(0x0101, 0x0001, lambda_4A92)

    Sleep(400)

    @scena.Lambda('lambda_4AA8')
    def lambda_4AA8():
        ChrWalkTo(0x00FE, -2950, 0, 42920, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0136, 0x0002, lambda_4AA8)

    @scena.Lambda('lambda_4AC3')
    def lambda_4AC3():
        ChrSetDirection(0x00FE, 270, 0)
        Yield()

        Jump('lambda_4AC3')

    DispatchAsync2(0x0136, 0x0001, lambda_4AC3)

    Sleep(300)

    @scena.Lambda('lambda_4AD9')
    def lambda_4AD9():
        ChrWalkTo(0x00FE, -1840, 0, 43640, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_4AD9)

    @scena.Lambda('lambda_4AF4')
    def lambda_4AF4():
        ChrSetDirection(0x00FE, 270, 0)
        Yield()

        Jump('lambda_4AF4')

    DispatchAsync2(0x0102, 0x0001, lambda_4AF4)

    WaitForThreadExit(0x0102, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010040936V#004F哎？负责人呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4A(0x0009, 255)
    OP_62(0x0009, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrSetDirection(0x0009, 225, 400)

    ChrTalk(
        0x0009,
        (
            '#0320040937V啊，小姑娘。\n',
            '你们有什么委托吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040938V#501F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0102, 0x01)
    TerminateThread(0x0136, 0x01)

    @scena.Lambda('lambda_4BAB')
    def lambda_4BAB():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_4BAB')

    DispatchAsync2(0x0101, 0x0001, lambda_4BAB)

    @scena.Lambda('lambda_4BBC')
    def lambda_4BBC():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_4BBC')

    DispatchAsync2(0x0102, 0x0001, lambda_4BBC)

    @scena.Lambda('lambda_4BCD')
    def lambda_4BCD():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_4BCD')

    DispatchAsync2(0x0136, 0x0001, lambda_4BCD)

    ChrWalkTo(0x0009, -2580, 0, 45260, 2000, 0x00)
    ChrSetDirection(0x0009, 180, 400)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0102, 0x01)
    TerminateThread(0x0136, 0x01)

    ChrTalk(
        0x0009,
        (
            '#0320040939V#830F负责接待的嘉恩\n',
            '正在二楼和客人谈话。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320040940V如果有什么事情，\n',
            '可以先跟我说说吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040941V#000F啊……\n',
            '我们不是客人呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0320040942V#835F嗯？那个徽章……\n',
            '原来你们是同行啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320040943V#830F我叫卡露娜。\n',
            '隶属于这个卢安支部。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320040944V以前都没见过你们，是新人吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040945V#006F嗯。\n',
            '我是准游击士艾丝蒂尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040946V#010F我是准游击士约修亚。\n',
            '请多多关照。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0320040947V#830F艾丝蒂尔和约修亚……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320040948V原来如此，\n',
            '你们就是从洛连特来的新人吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320040949V#831F听说你们和雪拉扎德一起\n',
            '在柏斯有非常活跃的表现哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040950V#008F啊、啊哈哈……\n',
            '也没那么了不起啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040951V#014F请问您是不是\n',
            '早就知道我们要来了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0320040952V#831F是啊，因为嘉恩说过\n',
            '会有两个有前途的新人过来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320040953V#830F不过要办理转属手续的话，\n',
            '也只能等他办完事再说了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320040954V要不你们先在城里游览一下，\n',
            '打发一下时间如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040955V#015F说的也是……\n',
            '反正在这里等着也做不了什么。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040956V#001F我也赞成！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040957V#501F啊，对了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_4FF7')
    def lambda_4FF7():
        ChrTurnDirection(0x00FE, 0x0136, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4FF7)

    Sleep(200)

    @scena.Lambda('lambda_500A')
    def lambda_500A():
        ChrTurnDirection(0x00FE, 0x0136, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_500A)

    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010040958V#008F那个，如果可以的话，\n',
            '你再陪我们一会儿好吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040959V好不容易才交到一个朋友\n',
            '就这么分别太可惜了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0136, 0x0101, 400)

    ChrTalk(
        0x0136,
        (
            '#0060040960V#041F嗯……我很乐意。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060040961V#041F如果不会妨碍到你们的话，\n',
            '我也很想带你们到处游览一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040962V#001F太棒了⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040963V#010F那就这么决定了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_5156')
    def lambda_5156():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_5156)

    Sleep(200)

    ChrTurnDirection(0x0101, 0x0009, 400)

    ChrTalk(
        0x0102,
        (
            '#0020040964V#010F那么我们就先\n',
            '在城里游览一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040965V#000F过一会儿就回来哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0320040966V好啊，玩得开心点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0009, 90, 400)
    ChrWalkTo(0x0009, -400, 0, 45400, 2000, 0x00)
    ChrSetDirection(0x0009, 90, 400)
    OP_4B(0x0009, 255)
    EventEnd(0x00)

    Return()

# id: 0x0014 offset: 0x5214
@scena.Code('func_14_5214')
def func_14_5214():
    MapClearFlags(0x00000001)
    EventBegin(0x00)
    CameraMove(-3330, 0, 43680, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2830, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0101, -160, 0, 39670, 315)
    ChrSetPos(0x0102, -100, 0, 40880, 315)
    ChrSetPos(0x0136, -1250, 0, 39900, 315)
    OP_4A(0x0008, 255)
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrSetDirection(0x0008, 135, 0)

    ChrTalk(
        0x0008,
        (
            '#0500041131V#650F欢迎光临。\n',
            '欢迎来到游击士协会！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500041132V#653F啊，这不是科洛丝吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0136,
        (
            '#0060041133V#040F您好，嘉恩先生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500041134V#650F今天又是受校长之托，\n',
            '来委托我们去消灭魔兽吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500041135V#651F啊啊，我知道了！\n',
            '是来委托我们做学园祭的警备吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0136,
        (
            '#0060041136V#045F不是呢，\n',
            '不过这件事迟早也要来麻烦你们。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060041137V#040F今天我是为了\n',
            '给艾丝蒂尔他们做向导而来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500041138V#653F咦？说起来……\n',
            '这两位好像不是学院的学生。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500041139V等等，这徽章是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_54A1')
    def lambda_54A1():
        ChrWalkTo(0x00FE, -3550, 0, 45310, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_54A1)

    @scena.Lambda('lambda_54BC')
    def lambda_54BC():
        ChrSetDirection(0x00FE, 270, 0)
        Yield()

        Jump('lambda_54BC')

    DispatchAsync2(0x0102, 0x0001, lambda_54BC)

    Sleep(200)

    @scena.Lambda('lambda_54D2')
    def lambda_54D2():
        ChrWalkTo(0x00FE, -3550, 0, 44220, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_54D2)

    @scena.Lambda('lambda_54ED')
    def lambda_54ED():
        ChrSetDirection(0x00FE, 270, 0)
        Yield()

        Jump('lambda_54ED')

    DispatchAsync2(0x0101, 0x0001, lambda_54ED)

    Sleep(800)

    @scena.Lambda('lambda_5503')
    def lambda_5503():
        CameraMove(-4540, 0, 45010, 2000)

        ExitThread()

    DispatchAsync(0x0136, 0x0003, lambda_5503)

    @scena.Lambda('lambda_551B')
    def lambda_551B():
        ChrWalkTo(0x00FE, -3670, 0, 43200, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0136, 0x0002, lambda_551B)

    Sleep(500)

    ChrSetDirection(0x0008, 90, 0)
    WaitForThreadExit(0x0101, 0x0002)
    WaitForThreadExit(0x0136, 0x0002)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)

    ChrTalk(
        0x0101,
        (
            '#0010041140V#000F#4P初次见面。\n',
            '我是准游击士艾丝蒂尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020041141V#010F我是准游击士约修亚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500041142V#650F啊啊……\n',
            '你们就是艾丝蒂尔和约修亚啊！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500041143V#651F哎呀～你们来了真是太好了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500041144V之前柏斯支部发来了联络，\n',
            '说你们很快就会来到卢安。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010041145V#501F#4P是吗，原来卢格兰爷爷\n',
            '已经帮我们打过招呼了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020041146V#010F下次见面得谢谢他呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500041147V#650F我叫嘉恩，\n',
            '负责卢安支部的接待工作。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500041148V今后我会全力支持你们的工作，\n',
            '当然也包括对你们进行监督。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500041149V还请你们多多关照哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010041150V#006F#4P嗯！\n',
            '请多指教，嘉恩哥哥。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020041151V#010F请多指教。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500041152V#651F呵呵，\n',
            '我对你们抱有很大的期待哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500041153V怎么说，你们可是漂亮地\n',
            '解决那次空贼事件的最大功臣。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0136, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x0136, 0x0101, 400)

    ChrTalk(
        0x0136,
        (
            '#0060041154V#044F空贼事件……\n',
            '是指柏斯地区发生的那件吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060041155V#041F我在《利贝尔通讯》的\n',
            '最新一期上看到这条新闻呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060041156V原来，那个事件\n',
            '是艾丝蒂尔你们解决的啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0136, 400)
    ChrTurnDirection(0x0102, 0x0136, 400)

    ChrTalk(
        0x0101,
        (
            '#0010041157V#008F#4P啊哈哈，也不是……\n',
            '我们只是帮了点忙而已啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020041158V#010F真正逮捕了空贼的\n',
            '是王国军的部队。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500041159V#650F呵呵，就别谦虚了。\n',
            '卢格兰老爷子也对你们赞誉有佳。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500041160V我马上就给你们办转属手续，\n',
            '你们两个在这份文件上签个名吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500041161V快快，就现在。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 270, 400)
    ChrSetDirection(0x0102, 270, 400)
    ChrSetDirection(0x0136, 315, 400)

    ChrTalk(
        0x0101,
        (
            '#0010041162V#004F#4P嗯、嗯……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020041163V#010F那我们这就……',
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
            '艾丝蒂尔和约修亚\n',
            '在转属手续的文书上签了字。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0008,
        (
            '#0500041164V#651F嗯嗯，这样一来，\n',
            '你们就隶属于卢安支部的了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500041165V哎呀，现在正是繁忙时期，\n',
            '你们来卢安真是帮了我们大忙啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500041166V呵呵……你们两个别想逃哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010041167V#007F#4P好、好像有点不好的预感。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020041168V#010F我们刚才已经听说了，\n',
            '这里好像正处于人手不足的状况。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020041169V是不是发生了什么事件呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500041170V#654F倒没有那么严重。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500041171V其实，现在有位王家的大人物\n',
            '正要来我们卢安市。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010041172V#004F#4P王家的大人物……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010041173V#001F难、难道是女王陛下！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500041174V#650F哈哈，怎么可能。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500041175V不过，来的人是王族成员，\n',
            '这一点是肯定没错的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500041176V据说这位大人物\n',
            '是来卢安市视察的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010041177V#501F#4P哦～有这种人物在啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010041178V可是可是，\n',
            '这和人手不足又有什么关系呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500041179V#650F毕竟是王族成员啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500041180V万一出什么意外可不得了啊，\n',
            '而且戴尔蒙市长对这件事非常重视。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500041181V所以他委托我们\n',
            '强化卢安市街区的警备。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020041182V#010F原来如此，\n',
            '刚才在二楼谈的就是这件事吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020041183V话说回来，有必要警戒街区吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500041184V#654F是啊……\n',
            '还不是因为港口那边有些不安分的人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500041185V应该是想要我们\n',
            '在这段时间里盯紧他们一点吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010041186V#009F#4P不安分的人……\n',
            '就是刚才来闹事的那帮家伙吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010041187V嗯～要是他们的话，\n',
            '没准真会惹出什么事情来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500041188V#653F怎么，你们认识他们吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020041189V#012F其实是……',
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
            '约修亚向嘉恩讲述了刚才发生的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0008,
        (
            '#0500041190V#652F是吗……\n',
            '原来你们去了仓库那里啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500041191V那里是一个叫做\n',
            '『渡鸦帮』的不良集团的据点。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500041192V来找你们麻烦的大概是\n',
            '充当集团首领的那群青年吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010041193V#009F#4P『渡鸦帮』……\n',
            '还真是适合那些坏蛋的名字呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500041194V#654F前一阵还挺老实的。\n',
            '不过最近，他们的老毛病好像又发作了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500041195V市长的担心固然没错，\n',
            '不过我们还必须把卢安\n',
            '其他地区的工作都做好才行啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500041196V#650F总之，就因为这样，\n',
            '我们正为人手不足而发愁呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500041197V你们来得正好，\n',
            '多谢多谢，真是及时雨啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010041198V#008F#4P啊哈哈……\n',
            '我们不会辜负你的期待的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010041199V那么，从明天开始，\n',
            '我们就参与这里的工作吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020041200V#010F有什么事的话，\n',
            '请不必客气尽管吩咐我们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500041201V#651F好啊，拜托了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T2100._SN', 100, 0, 0)
    IdleLoop()
    EventEnd(0x00)

    Return()

# id: 0x0015 offset: 0x63C3
@scena.Code('func_15_63C3')
def func_15_63C3():
    MapClearFlags(0x00000001)
    EventBegin(0x00)
    CameraMove(-1640, 0, 43790, 0)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0102, -690, 0, 39780, 315)
    ChrSetPos(0x0101, 790, 0, 39400, 315)

    @scena.Lambda('lambda_6408')
    def lambda_6408():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_6408')

    DispatchAsync2(0x0101, 0x0001, lambda_6408)

    @scena.Lambda('lambda_6419')
    def lambda_6419():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_6419')

    DispatchAsync2(0x0102, 0x0001, lambda_6419)

    @scena.Lambda('lambda_642A')
    def lambda_642A():
        CameraMove(-5410, 0, 45570, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_642A)

    @scena.Lambda('lambda_6442')
    def lambda_6442():
        ChrWalkTo(0x00FE, -3200, 0, 45110, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_6442)

    Sleep(500)

    @scena.Lambda('lambda_6462')
    def lambda_6462():
        ChrWalkTo(0x00FE, -3200, 0, 43960, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_6462)

    WaitForThreadExit(0x0101, 0x0002)
    WaitForThreadExit(0x0102, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010050075V#000F#2P嘉恩哥哥，早啊～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020050107V#010F早上好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500050077V#650F哟，早上好。\n',
            ' ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010050078V#000F那当然啦☆',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020050079V#010F抱歉有点心急了，\n',
            '能安排一些工作给我们做吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500050080V#650F嗯，没问题！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500050081V有很多事想请你们帮忙来着，\n',
            '嗯，选哪一件好呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010050082V#000F请、请手下留情……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500050083V#650F哎……？\n',
            '你们稍等一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0008, -5980, 0, 46770, 2000, 0x00)
    ChrSetDirection(0x0008, 270, 400)

    ChrTalk(
        0x0008,
        (
            '#0500050084V#650F您好，这里是游击士协会。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500050085V哟，是白之木莲亭……\n',
            '说来你们也很久没发联络过来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500050086V你那里的古董通信器\n',
            '竟然还能用啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500050087V………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500050088V………………什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500050089V#650F是吗……\n',
            '这事可严重了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500050090V好，知道了。\n',
            '我马上派人过去了解情况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010050091V#000F怎么了？\n',
            '出什么事了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#0500050092V#650F现在还不知道是\n',
            '事故还是人为的案件……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500050093V昨天晚上， \n',
            '海道边的孤儿院发生了火灾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010050094V#000F不、不会吧……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020050095V#010F已经确定了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0008, -5700, 0, 45100, 3000, 0x00)
    ChrSetDirection(0x0008, 90, 800)

    ChrTalk(
        0x0008,
        (
            '#0500050096V#650F是玛诺利亚旅店的主人\n',
            '特地发了联络通知我们的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500050097V是座名叫玛西亚的孤儿院，\n',
            '你们知道那里吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010050098V#000F何、何止知道……\n',
            '昨天下午我们还去过呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020050099V#010F那么，\n',
            '特蕾莎院长和那些孩子都还好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500050100V#650F这个还没确认。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500050101V总之，要先去调查一下，\n',
            '还要确认一下他们是否平安。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500050102V……可以拜托你们去吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010050103V#000F那还用说！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020050104V#010F那我们马上\n',
            '赶去孤儿院了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500050105V#650F好，拜托了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    EventEnd(0x00)

    Return()

# id: 0x0016 offset: 0x6A76
@scena.Code('func_16_6A76')
def func_16_6A76():
    MapClearFlags(0x00000001)
    EventBegin(0x00)
    CameraMove(-4700, 0, 45110, 0)
    CameraSetDistance(2800, 0)
    ChrClearFlags(0x0008, 0x0080)
    OP_4A(0x0008, 255)
    ChrSetPos(0x0101, -170, 0, 40420, 0)
    ChrSetPos(0x0102, -610, 0, 39400, 0)
    ChrSetPos(0x0105, 790, 0, 39400, 0)

    @scena.Lambda('lambda_6AD9')
    def lambda_6AD9():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_6AD9')

    DispatchAsync2(0x0008, 0x0001, lambda_6AD9)

    @scena.Lambda('lambda_6AEA')
    def lambda_6AEA():
        ChrSetDirection(0x00FE, 270, 0)
        Yield()

        Jump('lambda_6AEA')

    DispatchAsync2(0x0101, 0x0001, lambda_6AEA)

    @scena.Lambda('lambda_6AFB')
    def lambda_6AFB():
        ChrSetDirection(0x00FE, 270, 0)
        Yield()

        Jump('lambda_6AFB')

    DispatchAsync2(0x0102, 0x0001, lambda_6AFB)

    @scena.Lambda('lambda_6B0C')
    def lambda_6B0C():
        ChrSetDirection(0x00FE, 270, 0)
        Yield()

        Jump('lambda_6B0C')

    DispatchAsync2(0x0105, 0x0001, lambda_6B0C)

    FadeIn(1000, 0)

    @scena.Lambda('lambda_6B26')
    def lambda_6B26():
        ChrWalkTo(0x00FE, -3360, 0, 45110, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_6B26)

    Sleep(400)

    @scena.Lambda('lambda_6B46')
    def lambda_6B46():
        ChrWalkTo(0x00FE, -3530, 0, 43770, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_6B46)

    Sleep(100)

    @scena.Lambda('lambda_6B66')
    def lambda_6B66():
        ChrWalkTo(0x00FE, -2680, 0, 44210, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0002, lambda_6B66)

    WaitForThreadExit(0x0105, 0x0002)

    ChrTalk(
        0x0008,
        (
            '#0500050827V#651F哟，辛苦了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500050828V看来那男孩\n',
            '已经平安获救了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010050829V#006F嗯，总算还好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010050830V不过说起来真是吃了一惊。\n',
            '想不到那个红头发的家伙也来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500050831V#650F哈哈，是说阿加特吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500050832V他是为别的事情来卢安的，\n',
            '刚才被我硬逼着去了你们那里。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500050833V毕竟他曾经是\n',
            '『渡鸦帮』的首领啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020050834V#010F果然是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010050835V#007F难怪那家伙看起来\n',
            '一副粗鲁凶狠的样子啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500050836V#655F不过这也是过去的事了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500050837V他在和你们差不多大的时候\n',
            '流浪到卢安来了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500050838V纠集了一帮天不怕地不怕的流氓，\n',
            '在这个城市大闹了一阵子。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500050839V#650F不过，和那时候相比的话，\n',
            '现在的成员已经算很可爱了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010050840V#004F这、这样的家伙\n',
            '居然会当上了游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500050841V#651F嗯，因为他和某个人的相遇，\n',
            '让他完全地改变了自己。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500050842V从那之后他就立志要做游击士，\n',
            '而且，最后还靠自己的努力达成了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500050843V人啊，想变的话还是可以变的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(6, 0x00, 0x64)
    ChrSetPos(0x000A, 0, 0, 39060, 0)
    ChrClearFlags(0x000A, 0x0080)
    Sleep(500)

    ChrTalk(
        0x000A,
        (
            '#0050050844V……要说废话的话，\n',
            '还是等回到家自己对着墙说个够吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0105, 0xFF)

    @scena.Lambda('lambda_6F97')
    def lambda_6F97():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_6F97')

    DispatchAsync2(0x0008, 0x0001, lambda_6F97)

    @scena.Lambda('lambda_6FA8')
    def lambda_6FA8():
        ChrTurnDirection(0x00FE, 0x000A, 400)
        Yield()

        Jump('lambda_6FA8')

    DispatchAsync2(0x0101, 0x0002, lambda_6FA8)

    @scena.Lambda('lambda_6FB9')
    def lambda_6FB9():
        ChrTurnDirection(0x00FE, 0x000A, 400)
        Yield()

        Jump('lambda_6FB9')

    DispatchAsync2(0x0102, 0x0002, lambda_6FB9)

    @scena.Lambda('lambda_6FCA')
    def lambda_6FCA():
        ChrTurnDirection(0x00FE, 0x000A, 400)
        Yield()

        Jump('lambda_6FCA')

    DispatchAsync2(0x0105, 0x0002, lambda_6FCA)

    @scena.Lambda('lambda_6FDB')
    def lambda_6FDB():
        CameraMove(-4100, 0, 44500, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_6FDB)

    ChrWalkTo(0x000A, -2690, 0, 42540, 3000, 0x00)

    ChrTalk(
        0x0101,
        (
            '#0010050845V#004F啊，回来了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0050050846V#057F这个家伙， \n',
            '老是在别人背后说三道四的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050050847V还是和以前一样八卦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500050848V#651F哈哈，\n',
            '这话我就当作是表扬好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500050849V#650F话说回来，\n',
            '你的调查进行得怎样了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0050050850V#053F嗯，大致有数了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050050851V虽然还不能下结论，\n',
            '不过那帮家伙应该是清白的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010050852V#009F真的吗～？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010050853V虽说那帮家伙是你以前的同伴，\n',
            '不过你应该不会包庇他们吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0101, 400)

    ChrTalk(
        0x000A,
        (
            '#0050050854V#050F蠢材，别用这样的眼色看人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050050855V有证人看见他们\n',
            '昨晚在船员酒吧喝酒。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050050856V我问你，在醉酒的状态下， \n',
            '他们怎能做出那么周到的纵火……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010050857V#003F唔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020050858V#010F#1P既然这样的话，\n',
            '他们的嫌疑暂时先搁在一边吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020050859V#015F而且，我也并不认为\n',
            '他们有那么大的胆量去纵火。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010050860V#007F嗯，的确……\n',
            '感觉他们只会虚张声势而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0050050861V#053F总之， \n',
            '这段时间我会盯着那帮家伙的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050050862V顺便也一并搜捕犯人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010050863V#004F哎……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0050050864V#050F事件的调查由我来接手。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050050865V你们两个就不必再跟进了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010050866V#005F你、你说什么～！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010050867V明明是我们先来的，\n',
            '你凭什么不让我们跟进这个案件！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020050868V#012F#1P可以给我们\n',
            '一个合理的理由吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0050050869V#057F你们夹带太多的个人感情了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050050870V不止游击士，\n',
            '任何人都一样，关心则乱。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050050871V而且，居然也把\n',
            '普通的平民卷到战斗中去……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060050872V#043F啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060050873V#049F对不起，我……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0050050874V#051F你没有道歉的必要。\n',
            '只是这两个家伙觉悟不足。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050050875V关键是还欠缺职业意识。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010050876V#005F你、你凭什么\n',
            '这样批评我们啊！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010050877V不管你说什么都好，\n',
            '反正我们已经跟特蕾莎院长约定了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0008, 400)

    ChrTalk(
        0x000A,
        (
            '#0050050878V#051F喂，嘉恩。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050050879V当正游击士和准游击士\n',
            '要求接手同一桩任务的时候，\n',
            '按照规章，应该是哪方享有优先权？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500050880V#654F哎呀哎呀……\n',
            '你不是明知故问吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500050881V当然是正游击士了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010050882V#009F哼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020050883V#012F#1P我认为我们两个\n',
            '也有足够的战斗能力。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020050884V无论如何请让我们协助……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0101, 400)

    ChrTalk(
        0x000A,
        (
            '#0050050885V#050F普通的调查用不着这么多人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050050886V我就不多说了。\n',
            '你们还是想开点吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000A, 135, 400)
    ChrWalkTo(0x000A, 0, 0, 39060, 3000, 0x00)
    PlaySE(7, 0x00, 0x64)
    ChrSetFlags(0x000A, 0x0080)

    @scena.Lambda('lambda_7860')
    def lambda_7860():
        CameraMove(-4700, 0, 45110, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_7860)

    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010050887V#009F#2P他、他、他……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010050888V#005F他以为自己是谁啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020050889V#013F#1P虽然很不甘心，\n',
            '但他说的确实是事实……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020050890V我们也无从反驳。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0105, 0xFF)
    ChrTurnDirection(0x0105, 0x0008, 400)

    ChrTalk(
        0x0105,
        (
            '#0060050891V#043F真对不起……\n',
            '要是我不出剑的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010050892V#009F#2P跟这没有关系啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010050893V真是的，每次一有事，\n',
            '就总把我们看成是绊脚石……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0008, 0x01)
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#0500050894V#655F算了，他没有恶意的，\n',
            '你们也不要太过介意了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500050895V#655F那家伙是个不善言辞的人，\n',
            '向来就只会用那种语气说话。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500050896V#652F而且这次的事件……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500050897V#652F说不定还跟\n',
            '他正在追查的事件有关联。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_7AC1')
    def lambda_7AC1():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_7AC1)

    @scena.Lambda('lambda_7ACF')
    def lambda_7ACF():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_7ACF)

    @scena.Lambda('lambda_7ADD')
    def lambda_7ADD():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0002, lambda_7ADD)

    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010050898V#004F哎……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020050899V#014F阿加特正在追查的事件？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500050900V#652F详情我不便透露……\n',
            '总之，搜捕犯人的工作就交给他吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500050901V我也拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010050902V#003F怎、怎能这样呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020050903V#013F是吗……………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020050904V#015F那么，就先把我们至今为止\n',
            '调查所得的情况报告一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500050905V#655F嗯，有劳你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x003B, 0x04, 0x10)
    OP_28(0x003C, 0x04, 0x10)
    OP_28(0x003C, 0x04, 0x20)
    Sleep(100)

    OP_AF(0x22, 0x003B)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    ChrTalk(
        0x0008,
        (
            '#0500050906V#655F看来你们的调查做得很认真啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500050907V#652F不过就像我刚才所说的，\n',
            '这次的事件牵涉的东西很多。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500050908V虽然非常抱歉，不过事件的调查\n',
            '还是以这次报告为终结吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010050909V#003F可、可是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010050910V我本来想为特蕾莎院长\n',
            '还有那些孩子做点什么的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010050911V……现在竟然………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 0)
    Sleep(300)

    ChrTalk(
        0x0102,
        (
            '#0020050912V#013F艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0101, 0)

    ChrTalk(
        0x0105,
        (
            '#0060050913V#043F艾丝蒂尔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060050914V#047F……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0008, 0)
    Sleep(300)

    ChrTalk(
        0x0105,
        (
            '#0060050915V#042F那个，嘉恩先生。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060050916V如果我没记错的话， \n',
            '游击士的成员也可以参与\n',
            '协助由民间举办的活动对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500050917V#650F是啊，不过也要看内容。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500050918V像王立学院的学园祭，\n',
            '因为会有很多客人来参观，\n',
            '所以我们通常都会负责警卫的工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060050919V#040F这样的话……\n',
            '艾丝蒂尔、约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060050920V其实工作的意义还可以延伸一下，\n',
            '我想请你们协助学院舞台剧的举办。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_7FD3')
    def lambda_7FD3():
        ChrTurnDirection(0x00FE, 0x0105, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_7FD3)

    @scena.Lambda('lambda_7FE1')
    def lambda_7FE1():
        ChrTurnDirection(0x00FE, 0x0105, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_7FE1)

    ChrTalk(
        0x0101,
        (
            '#0010050921V#004F#2P哎……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020050922V#014F#1P这话怎么说？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060050923V#040F每年学园祭的最后，\n',
            '我们都会在礼堂表演舞台剧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060050924V更重要的是，\n',
            '那些孩子也一直在期待着演出呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060050925V#045F不过，有两个很重要的角色\n',
            '到现在都还没找到合适的人选……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010050926V#004F#2P难、难道说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020050927V#014F#1P要我们来演这两个角色吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060050928V#047F是的，如果再找不到演员，\n',
            '今年的舞台剧可能就要停演了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060050929V那样就太对不住那些\n',
            '期待着看表演的孩子们了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060050930V#040F于是昨晚，我和学院的学生会长\n',
            '说起了你们两人的事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060050931V结果她很感兴趣，\n',
            '叫我无论如何要把你们请过来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060050932V#041F我们会从预算经费中拨出酬金的，\n',
            '虽然数目不是很多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010050933V#004F#2P为、为什么选中我们两个？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010050934V不是我要推脱，\n',
            '舞台剧什么的我可是从来没演过啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060050935V#040F因为女生所扮演的角色\n',
            '一定要精通武术才能胜任……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060050936V如果由艾丝蒂尔扮演的话，\n',
            '我想这角色一定会演得非常好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010050937V#008F#2P原、原来是这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010050938V嗯，谈到武术的话，\n',
            '我倒还满有一点自信的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020050939V#019F#1P的确正适合你呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020050940V#010F那么，另一个角色呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060050941V#044F这、这个……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060050942V#049F这个……要我说的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020050943V#014F#1P要你说的话怎样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060050944V#045F……有点……不好意思呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0102,
        (
            '#0020050945V#018F#1P这、这是什么意思……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010050946V#006F#2P真是的，约修亚你呀，\n',
            '刨根问底的话可会让人为难哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010050947V既可以参加学园祭，\n',
            '又可以让那些孩子高兴……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010050948V再说这又算是工作，\n',
            '简直就是一石三鸟啊！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010050949V#001F当然是非做不可的啦㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020050950V#014F#1P等、等一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0008, 400)
    OP_62(0x0102, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x0102,
        (
            '#0020050951V#014F#1P嘉恩先生。 \n',
            '这样的工作也可以做吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_86A2')
    def lambda_86A2():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_86A2)

    ChrTalk(
        0x0008,
        (
            '#0500050952V#651F当然了，没问题。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500050953V对平民的协助、对地区的贡献，\n',
            '这是一份非常有意义的好工作呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500050954V#650F而且刚好阿加特来了，\n',
            '你们也可以挪出空闲来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500050955V可以的话就尽管去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010050956V#001F#2P太好啦㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 0)
    Sleep(400)

    ChrTalk(
        0x0102,
        (
            '#0020050957V#017F#1P呼……\n',
            '总有种不祥的预感。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020050958V#017F不过为了那些孩子，\n',
            '我们也只好尽力而为了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020050959V#010F不过，如果有什么未完的工作，\n',
            '最好还是在去王立学院之前\n',
            '处理完比较好吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020050960V一旦开始帮忙排演舞台剧，\n',
            '大概就没空做其他的事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010050961V#006F#2P是啊，的确呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_88E6')
    def lambda_88E6():
        ChrTurnDirection(0x00FE, 0x0105, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_88E6)

    @scena.Lambda('lambda_88F4')
    def lambda_88F4():
        ChrTurnDirection(0x00FE, 0x0105, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_88F4)

    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010050962V#501F#2P那个，科洛丝。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010050963V可能会稍微耽误些时间，\n',
            '先等我们完成工作再去可以吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060050964V#045F啊，好呢。\n',
            '你们就不用顾虑我了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060050965V#040F顺便说一下怎么去王立学院吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060050966V出了梅威海道，在第一个三叉路口处\n',
            '向东拐，然后沿着林道走就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010050967V#006F#2P嗯，知道了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010050968V#001F那么，我们走吧～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x003C, 0x01, 0x0040)
    OP_28(0x003C, 0x01, 0x0080)
    OP_28(0x003D, 0x04, 0x02)
    OP_28(0x003D, 0x04, 0x04)
    OP_28(0x003D, 0x01, 0x0001)
    OP_28(0x003D, 0x01, 0x0002)
    EventEnd(0x00)
    OP_4B(0x0008, 255)

    Return()

# id: 0x0017 offset: 0x8A92
@scena.Code('func_17_8A92')
def func_17_8A92():
    EventBegin(0x00)
    CameraMove(-4840, 0, 45450, 0)
    ChrSetPos(0x0101, -3350, 0, 45440, 270)
    ChrSetPos(0x0102, -3440, 0, 44470, 270)
    ChrSetPos(0x0105, 0, 0, 39060, 0)
    ChrSetFlags(0x0105, 0x0080)
    OP_4A(0x0008, 255)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0500061399V#652F……我明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500061400V真想不到戴尔蒙市长\n',
            '会是一连串事件的幕后主使。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500061401V嗯，这可是件大事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061402V#002F对了，嘉恩哥哥。\n',
            '我们可以去逮捕市长吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500061403V#654F这个嘛……\n',
            '很遗憾，恐怕很难。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500061404V但如果是现行犯的话，\n',
            '即使是市长也可以不容置辩地将其逮捕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020061405V#013F果然是这样吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061406V#005F怎、怎么会……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010061407V难道还要让那个恶毒的市长\n',
            '继续胡作非为下去吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500061408V#650F哎呀，不用那么紧张啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500061409V就算协会没权这么做……\n',
            '不过，王国军却可以逮捕市长。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061410V#004F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500061411V#652F艾丝蒂尔、约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500061412V你们现在就前往市长官邸，\n',
            '将事情问个清楚彻底。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500061413V就算或多或少把他惹火了也没关系，\n',
            '总之尽量拖延时间就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020061414V#010F原来如此，\n',
            '这期间你就和王国军联络是吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500061415V#650F呵呵呵，就是这样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500061416V我会利用导力通信，\n',
            '向雷斯顿要塞的司令部申请援助。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061417V#007F嗯，虽然求助于军队有点不爽，\n',
            '但也没办法了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010061418V#006F好吧，等科洛丝也来到之后，\n',
            '我们就去市长家……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(6, 0x00, 0x64)
    Sleep(500)

    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0102, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(500)

    @scena.Lambda('lambda_8F4D')
    def lambda_8F4D():
        CameraMove(-4770, 0, 44400, 1000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_8F4D)

    @scena.Lambda('lambda_8F65')
    def lambda_8F65():
        ChrTurnDirection(0x00FE, 0x0105, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_8F65)

    @scena.Lambda('lambda_8F73')
    def lambda_8F73():
        ChrTurnDirection(0x00FE, 0x0105, 400)
        Yield()

        Jump('lambda_8F73')

    DispatchAsync2(0x0101, 0x0001, lambda_8F73)

    @scena.Lambda('lambda_8F84')
    def lambda_8F84():
        ChrTurnDirection(0x00FE, 0x0105, 400)
        Yield()

        Jump('lambda_8F84')

    DispatchAsync2(0x0102, 0x0001, lambda_8F84)

    ChrClearFlags(0x0105, 0x0080)
    ChrWalkTo(0x0105, -3020, 0, 43110, 3000, 0x00)
    ChrTurnDirection(0x0105, 0x0101, 400)

    ChrTalk(
        0x0105,
        (
            '#0060061419V#049F#3P呼～呼～……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060061420V让、让你们久等了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061421V#006F#2P你来得正是时候⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020061422V#010F#2P回去学院一趟之后，\n',
            '竟还能这么快赶过来啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060061423V#045F#3P这、这个……\n',
            '我对自己的脚力还是有点自信的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060061424V#042F对了……\n',
            '事情进展得怎么样了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061425V#006F#2P我们正在讨论\n',
            '前往市长家的事呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010061426V要在王国军的人到达之前，\n',
            '一边探听情况一边尽量拖延时间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060061427V#044F#3P啊……这样吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060061428V#049F……我可能多此一举了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061429V#501F#2P？？？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010061430V那个，科洛丝也一起来吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060061431V#045F#3P啊，是。\n',
            '请一定让我同行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    ChrTurnDirection(0x0102, 0x0008, 400)

    ChrTalk(
        0x0102,
        (
            '#0020061432V#012F嘉恩先生，\n',
            '联络王国军的事就拜托您了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0102, 400)

    ChrTalk(
        0x0008,
        (
            '#0500061433V#652F嗯，交给我吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x003E, 0x01, 0x0400)
    EventEnd(0x00)
    OP_4B(0x0008, 255)

    Return()

# id: 0x0018 offset: 0x92A9
@scena.Code('func_18_92A9')
def func_18_92A9():
    EventBegin(0x00)
    CameraMove(-4700, 0, 45110, 0)
    CameraSetDistance(2800, 0)
    ChrClearFlags(0x0008, 0x0080)
    OP_4A(0x0008, 255)
    ChrSetPos(0x0101, -3360, 0, 45110, 270)
    ChrSetPos(0x0102, -3530, 0, 43770, 315)
    ChrSetPos(0x0105, -2350, 0, 44220, 270)
    FadeIn(2000, 0)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0500061890V#650F哦～这样啊。\n',
            '没想到王都的亲卫队竟然来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500061891V而且连传说中的最新型舰艇\n',
            '『埃尔赛尤号』也出动了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500061892V#654F要不是有接待工作的话，\n',
            '我也好想跑去亲眼看看啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061893V#506F想不到嘉恩哥哥\n',
            '还挺喜欢看热闹的嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010061894V#000F话说回来，\n',
            '嘉恩哥哥联络的是理查德上校对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500061895V#650F是啊，\n',
            '因为他正好在雷斯顿要塞的司令部。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500061896V不过亲卫队为什么会来，\n',
            '这点我就不知道了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500061897V大概是因为\n',
            '军队的联络系统也有好多种吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020061898V#010F除了普通的正规军，\n',
            '国境师团、情报部、王室亲卫队……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020061899V的确是非常复杂。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060061900V#043F话说回来，\n',
            '这次事件的善后处理会很麻烦吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060061901V今后卢安地区的行政工作\n',
            '将会如何进行下去呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061902V#004F啊，对啊……\n',
            '毕竟是市长已经被逮捕了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500061903V#652F我想应该会从王都\n',
            '派一位代理市长过来暂代政务吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500061904V市长被定罪之后，\n',
            '接着很快就会举行市长选举吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500061905V#651F对了对了，\n',
            '我想孤儿院也会受到正式补偿的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060061906V#047F是吗……太好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060061907V#048F这些都是多亏了\n',
            '艾丝蒂尔你们的全力帮助啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060061908V真的……太感谢你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    @scena.Lambda('lambda_976B')
    def lambda_976B():
        ChrTurnDirection(0x00FE, 0x0105, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_976B)

    ChrTurnDirection(0x0101, 0x0105, 400)

    ChrTalk(
        0x0101,
        (
            '#0010061909V#008F#2P没、没什么啦。\n',
            '你就别说得这么见外嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020061910V#010F#1P是啊，\n',
            '这些都是我们应该做的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020061911V更何况不止我们，\n',
            '阿加特兄他也帮了大忙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010061912V#004F#2P说、说起来！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_986F')
    def lambda_986F():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_986F)

    ChrTurnDirection(0x0102, 0x0008, 400)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010061913V#005F喂、喂，嘉恩哥哥！\n',
            '那个阿加特有联络吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500061914V#652F啊啊，这个嘛……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500061915V非常遗憾，\n',
            '似乎让那帮黑衣人跑掉了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500061916V他们好像还有其他同伙，\n',
            '一起对阿加特进行了伏击。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061917V#580F哎哎！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020061918V#012F他没事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500061919V#655F嗯，总算是突围成功了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500061920V现在应该正追着那帮家伙，\n',
            '往蔡斯方向去了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500061921V这会儿大概已经\n',
            '离开卢安地区了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061922V#007F是、是吗……\n',
            '还真是高难度的任务啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500061923V#650F哈哈，反正他也习惯了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500061924V阿加特这一段时间\n',
            '就一直在追捕那帮黑衣人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500061925V而且……\n',
            '这好像还是你们父亲拜托他做的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061926V#004F老、老爸！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020061927V#014F阿加特竟然会接受……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500061928V#651F呵呵，把曾经是『渡鸦帮』一员的\n',
            '阿加特引回正途的不是别人，\n',
            '正是卡西乌斯先生哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500061929V别看他嘴上不饶人，\n',
            '但一在你们父亲面前，他还是很乖的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061930V#004F哎哎？原来是这样吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500061931V#650F不过因为阿加特是那种性格，\n',
            '所以他经常会和别人一个劲地顶撞。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020061932V#010F原来如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020061933V他之所以对我们那么严厉，\n',
            '也恐怕是这个原因吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061934V#007F的确很有可能～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010061935V#005F也就是说，搞了半天，\n',
            '我们又是受了老爸的连累啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060061936V#045F呵呵……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060061937V#044F啊，\n',
            '提起艾丝蒂尔你们的父亲……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_9D95')
    def lambda_9D95():
        ChrTurnDirection(0x00FE, 0x0105, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_9D95)

    ChrTurnDirection(0x0101, 0x0105, 400)

    ChrTalk(
        0x0101,
        (
            '#0010061938V#004F#2P哎？怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060061939V#043F那个……\n',
            '在市长官邸出现黑光的时候……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061940V#002F#2P对了，还有这件事！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_9E38')
    def lambda_9E38():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_9E38)

    ChrSetDirection(0x0101, 180, 200)
    Fade(500)
    PlaySE(143, 0x00, 0x64)
    ChrSetChipByIndex(0x0101, 13)
    ChrClearFlags(0x0015, 0x0080)
    ChrSetPos(0x0015, -3600, 550, 44750, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010061941V#009F#2P发生了太多事情，\n',
            '不知不觉把这个忘掉了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010061942V这个，到底是什么东西呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020061943V#013F虽然这东西救了我们一命，\n',
            '但不知为什么，总觉得它有点诡异……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500061944V#653F很少见到这种颜色的导力器啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500061945V这东西是哪里来的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x0015, 0x0080)
    ChrSetChipByIndex(0x0101, 65535)

    @scena.Lambda('lambda_9F92')
    def lambda_9F92():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_9F92)

    ChrTurnDirection(0x0101, 0x0008, 400)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010061946V#003F这是……',
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
            '艾丝蒂尔向嘉恩说明了\n',
            '在寄给卡西乌斯的包裹里装有导力器和便条一事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0105,
        (
            '#0060061947V#044F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500061948V#655F嗯，Ｒ博士还有Ｋ吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500061949V难道是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061950V#004F哎？你知道吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500061951V#652F不，应该还\n',
            '称不上是什么线索……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500061952V但如果想调查这东西的来历，\n',
            '我想你们应该到蔡斯地区去一趟。\n',
            '也许会找到什么答案也说不定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061953V#505F蔡斯地区？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500061954V#652F正是如此，\n',
            '蔡斯市是以制造导力器而闻名的城市。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500061955V那里又被称作『工房都市』。\n',
            '拥有博士头衔的人也有很多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020061956V#010F原来如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020061957V就算找不到那位博士，\n',
            '但是至少也能弄清\n',
            '这个黑色导力器的真面目也说不定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061958V#007F唔……\n',
            '但我们还要留在这里修行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500061959V#651F呵呵，就是为了应付这种情况，\n',
            '我早已经全都准备好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '正游击士资格的推荐信',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    AddItem(0x0339, 1)

    ChrTalk(
        0x0101,
        (
            '#0010061960V#004F哎哎……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020061961V#014F这样可以吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500061962V#650F哈哈，就和空贼事件时一样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500061963V解决了那么大的事件，\n',
            '还有什么理由不发给你们呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500061964V评定和报酬也准备好了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x003D, 0x04, 0x10)
    OP_28(0x003E, 0x04, 0x10)
    Sleep(100)

    OP_AF(0x22, 0x003D)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    Sleep(100)

    OP_AF(0x22, 0x003E)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    ChrTalk(
        0x0101,
        (
            '#0010061965V#008F哇～……\n',
            '连学园祭的演出费都有……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020061966V#019F总之多谢您了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500061967V#651F别这么说，这是你们应得的报酬。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500061968V我也希望你们两个\n',
            '能尽早成为正游击士呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500061969V到那时候，\n',
            '你们就能更自由地展现自己的力量了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061970V#008F嘿嘿……\n',
            '谢谢，嘉恩哥哥。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020061971V#010F我们一定会努力，不辜负您的期望。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060061972V#048F太好了。\n',
            '艾丝蒂尔、约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060061973V#045F……只是以后，\n',
            '稍微有点寂寞呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_A630')
    def lambda_A630():
        ChrTurnDirection(0x00FE, 0x0105, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_A630)

    ChrTurnDirection(0x0101, 0x0105, 400)

    ChrTalk(
        0x0101,
        (
            '#0010061974V#003F#2P科洛丝……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020061975V#015F#1P……是啊。\n',
            '我们也很舍不得呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060061976V#045F啊……\n',
            '对不起，说了些任性的话。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060061977V#542F决定了出发的日子的话，\n',
            '可以告诉我一声吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060061978V我想，至少也让我\n',
            '送你们到艾尔·雷登关所……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000009C4)
    FadeOut(2000, 0, -1)
    OP_0D()
    OP_21()
    Sleep(1000)

    OP_AD('ED6_DT04/C_VIS047._CH', 0x0000, 0x0000, 0x00000064)
    Sleep(4000)

    OP_56(0x02)
    WaitEffect(0x13, 0x00)
    SetScenaFlags(ScenaFlag(0x0089, 3, 0x44B))

    ExecExpressionWithVar(
        0x31,
        (
            (Expr.PushLong, 0xF2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    CameraMove(100000, -100000, 100000, 0)
    FadeIn(0, 0)

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
        240,
        180,
        0,
        (
            TXT(0x00, '【保存进度】\n'),
            TXT(0x01, '【进入下一章】\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A7DA',
    )

    ShowSaveMenu()

    def _loc_A7DA(): pass

    label('loc_A7DA')

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeOut(0, 0, -1)
    OP_AE(0x000000C8)
    Sleep(2000)

    SetScenaFlags(ScenaFlag(0x0089, 4, 0x44C))
    SetScenaFlags(ScenaFlag(0x0088, 2, 0x442))
    OP_28(0x003E, 0x01, 0x0800)
    OP_28(0x0053, 0x04, 0x02)
    OP_28(0x0053, 0x04, 0x04)
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/R2412._SN', 0, 0, 0)
    IdleLoop()

    Return()

# id: 0x0019 offset: 0xA81A
@scena.Code('func_19_A81A')
def func_19_A81A():
    EventBegin(0x01)
    ChrTurnDirection(0x0009, 0x0000, 0)
    OP_4A(0x0009, 0)

    ExecExpressionWithValue(
        0x0014,
        0x01,
        (
            (Expr.GetChrWork, 0x9, 0x1),
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0014,
        0x02,
        (
            (Expr.GetChrWork, 0x9, 0x2),
            (Expr.GetChrWork, 0x0, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0014,
        0x03,
        (
            (Expr.GetChrWork, 0x9, 0x3),
            (Expr.GetChrWork, 0x0, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_69(0x0014, 1000)

    ChrTalk(
        0x0009,
        (
            '#0320040969V#830F抱歉，\n',
            '现在二楼正在进行商谈。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320040970V你们不妨到街上逛逛，\n',
            '消磨一些时间怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveToRelative(0x0000, 0, 0, -1500, 3000, 0x00)
    OP_4B(0x0009, 0)
    ChrSetDirection(0x0009, 90, 0)
    Sleep(50)

    EventEnd(0x04)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
