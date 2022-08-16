import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T2131_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2131   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'T2131.x'
    header.mapIndex       = 1
    header.bgm            = 12
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT21/T2131._SN', 'ED6_DT21/T2131_1._SN', 'ED6_DT21/T2131_2._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
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
        ('ED6_DT07/CH01270._CH', 'ED6_DT07/CH01270P._CP'),
        ('ED6_DT07/CH01560._CH', 'ED6_DT07/CH01560P._CP'),
        ('ED6_DT27/CH03930._CH', 'ED6_DT27/CH03930P._CP'),
        ('ED6_DT07/CH01570._CH', 'ED6_DT07/CH01570P._CP'),
        ('ED6_DT07/CH01120._CH', 'ED6_DT07/CH01120P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01030._CH', 'ED6_DT07/CH01030P._CP'),
        ('ED6_DT07/CH01123._CH', 'ED6_DT07/CH01123P._CP'),
        ('ED6_DT06/CH20020._CH', 'ED6_DT06/CH20020P._CP'),
        ('ED6_DT07/CH01680._CH', 'ED6_DT07/CH01680P._CP'),
        ('ED6_DT07/CH01120._CH', 'ED6_DT07/CH01120P._CP'),
        ('ED6_DT07/CH01463._CH', 'ED6_DT07/CH01463P._CP'),
        ('ED6_DT07/CH02510._CH', 'ED6_DT07/CH02510P._CP'),
        ('ED6_DT07/CH01460._CH', 'ED6_DT07/CH01460P._CP'),
        ('ED6_DT07/CH01443._CH', 'ED6_DT07/CH01443P._CP'),
    ]

# id: 0x10001 offset: 0x122
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '普莱米奥',
            x                   = -5500,
            z                   = 300,
            y                   = 33800,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0016,
        ),
        ScenaNpcData(
            name                = '修比拉老板',
            x                   = 26000,
            z                   = 0,
            y                   = 27230,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0012,
        ),
        ScenaNpcData(
            name                = '洛特丽亚',
            x                   = 33420,
            z                   = 0,
            y                   = 35300,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            name                = '费高',
            x                   = 35010,
            z                   = 0,
            y                   = 30340,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '阿伦特',
            x                   = 24900,
            z                   = 250,
            y                   = 35290,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '菲利奥',
            x                   = 24900,
            z                   = 250,
            y                   = 35290,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '拉科舒',
            x                   = 24900,
            z                   = 250,
            y                   = 35290,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0000,
        ),
        ScenaNpcData(
            name                = '迪恩',
            x                   = -3510,
            z                   = 250,
            y                   = 31610,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0017,
        ),
        ScenaNpcData(
            name                = '斯库阿洛',
            x                   = -2940,
            z                   = 0,
            y                   = 5590,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0014,
        ),
        ScenaNpcData(
            name                = '哈尔德',
            x                   = -1860,
            z                   = 200,
            y                   = 305,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0195,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '兰切',
            x                   = -2860,
            z                   = 750,
            y                   = 300,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 655368,
            chipIndex           = 8,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '茶',
            x                   = -2920,
            z                   = 750,
            y                   = -220,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1638408,
            chipIndex           = 8,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '波尔多斯',
            x                   = -17250,
            z                   = 0,
            y                   = 1960,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '波尔',
            x                   = -22080,
            z                   = 0,
            y                   = 2720,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '贝斯卡',
            x                   = -300,
            z                   = 200,
            y                   = 2126,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0115,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            name                = '塞卡鲁特',
            x                   = -17650,
            z                   = 200,
            y                   = 3320,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x01D5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0018,
        ),
        ScenaNpcData(
            name                = '君特',
            x                   = 35040,
            z                   = 0,
            y                   = 27960,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            name                = '目标用照相机',
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
            name                = '目标用照相机２',
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
    )

# id: 0x10002 offset: 0x382
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x382
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x382
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -4000,
            triggerZ            = 250,
            triggerY            = 33700,
            triggerRange        = 400,
            actorX              = -5500,
            actorZ              = 1800,
            actorY              = 33800,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0015,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 33310,
            triggerZ            = 0,
            triggerY            = 33689,
            triggerRange        = 400,
            actorX              = 33420,
            actorZ              = 1700,
            actorY              = 35300,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000E,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 33190,
            triggerZ            = 0,
            triggerY            = 30422,
            triggerRange        = 1000,
            actorX              = 35010,
            actorZ              = 1700,
            actorY              = 30340,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000A,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 33190,
            triggerZ            = 0,
            triggerY            = 27980,
            triggerRange        = 1000,
            actorX              = 35040,
            actorZ              = 1700,
            actorY              = 27960,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000C,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 25610,
            triggerZ            = 0,
            triggerY            = 28960,
            triggerRange        = 1700,
            actorX              = 26000,
            actorZ              = 1700,
            actorY              = 27230,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0012,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 27820,
            triggerZ            = 0,
            triggerY            = 28620,
            triggerRange        = 1700,
            actorX              = 26000,
            actorZ              = 1700,
            actorY              = 27230,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0012,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 25000,
            triggerZ            = 250,
            triggerY            = 36880,
            triggerRange        = 700,
            actorX              = 25150,
            actorZ              = 1500,
            actorY              = 37640,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0011,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 27030,
            triggerZ            = 250,
            triggerY            = 36880,
            triggerRange        = 700,
            actorX              = 27030,
            actorZ              = 1500,
            actorY              = 37640,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0010,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 28730,
            triggerZ            = 0,
            triggerY            = 37220,
            triggerRange        = 800,
            actorX              = 28730,
            actorZ              = 1800,
            actorY              = 37220,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0019,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x4C6
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_523',
    )

    ChrSetFlags(0x000D, 0x0080)
    ChrSetFlags(0x000E, 0x0080)
    ChrSetFlags(0x0014, 0x0080)
    ChrSetPos(0x0016, -1030, 0, 2240, 0)
    ChrSetChipByIndex(0x0016, 13)
    ChrClearFlags(0x0016, 0x0010)
    ChrClearFlags(0x0016, 0x0004)
    CreateThread(0x0016, 0x00, 0x06, func_02_725)
    ChrClearFlags(0x0017, 0x0080)
    ChrSetDirection(0x0015, 180, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_520',
    )

    ChrClearFlags(0x000F, 0x0080)
    ChrSetFlags(0x000C, 0x0080)

    def _loc_520(): pass

    label('loc_520')

    Jump('loc_646')

    def _loc_523(): pass

    label('loc_523')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_580',
    )

    ChrSetPos(0x000C, -6569, 0, 32668, 270)

    If(
        (
            (Expr.Eval, "OP_29(0x0068, 0x00, 0x10)"),
            (Expr.Eval, "OP_29(0x0068, 0x00, 0x40)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_54F',
    )

    Jump('loc_565')

    def _loc_54F(): pass

    label('loc_54F')

    ChrSetPos(0x000D, 32520, 0, 29800, 90)
    ChrSetFlags(0x000D, 0x0010)

    def _loc_565(): pass

    label('loc_565')

    ChrSetPos(0x000E, 5386, 250, 34285, 180)
    ChrSetDirection(0x0009, 90, 0)

    Jump('loc_646')

    def _loc_580(): pass

    label('loc_580')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_5AF',
    )

    ChrSetFlags(0x000C, 0x0080)
    ChrSetPos(0x000E, 4570, 250, 30488, 90)
    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0012, 0x0080)
    ChrClearFlags(0x0013, 0x0080)

    Jump('loc_646')

    def _loc_5AF(): pass

    label('loc_5AF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 4, 0x121C)),
            Expr.Return,
        ),
        'loc_5FB',
    )

    ChrSetFlags(0x0008, 0x0080)
    ChrSetPos(0x000C, 32603, 0, 29644, 67)
    ChrSetPos(0x000D, 33180, 0, 31996, 135)
    ChrSetFlags(0x000D, 0x0010)
    ChrSetFlags(0x000C, 0x0010)
    ChrSetPos(0x000E, -2350, 250, 33680, 270)

    Jump('loc_646')

    def _loc_5FB(): pass

    label('loc_5FB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_635',
    )

    ChrSetPos(0x000C, 32603, 0, 29644, 67)
    ChrSetPos(0x000D, 33180, 0, 31996, 135)
    ChrSetFlags(0x000D, 0x0010)
    ChrSetFlags(0x000C, 0x0010)

    Jump('loc_646')

    def _loc_635(): pass

    label('loc_635')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_646',
    )

    ChrSetFlags(0x000D, 0x0080)
    ChrSetFlags(0x000E, 0x0080)

    def _loc_646(): pass

    label('loc_646')

    Return()

# id: 0x0001 offset: 0x647
@scena.Code('func_01_647')
def func_01_647():
    OP_71(0x0003, 0x0008)
    OP_71(0x0003, 0x0020)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 4, 0x121C)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_661',
    )

    OP_64(0x00, 0x0001)

    def _loc_661(): pass

    label('loc_661')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_695',
    )

    OP_72(0x0000, 0x0020)
    OP_72(0x0000, 0x0008)
    OP_72(0x0001, 0x0020)
    OP_72(0x0001, 0x0008)
    OP_72(0x0002, 0x0020)
    OP_72(0x0002, 0x0008)
    OP_72(0x0003, 0x0020)
    OP_72(0x0003, 0x0008)

    def _loc_695(): pass

    label('loc_695')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6E4',
    )

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000069, 'loc_6B5'),
        (0x0000006A, 'loc_6C5'),
        (0x0000006B, 'loc_6C5'),
        (-1, 'loc_6D5'),
    )

    def _loc_6B5(): pass

    label('loc_6B5')

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x1A),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(0, 0x0002)

    Jump('loc_6E1')

    def _loc_6C5(): pass

    label('loc_6C5')

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x19),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(0, 0x0002)

    Jump('loc_6E1')

    def _loc_6D5(): pass

    label('loc_6D5')

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x1A),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_6E1')

    def _loc_6E1(): pass

    label('loc_6E1')

    Jump('loc_724')

    def _loc_6E4(): pass

    label('loc_6E4')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000069, 'loc_6F8'),
        (0x0000006A, 'loc_708'),
        (0x0000006B, 'loc_708'),
        (-1, 'loc_718'),
    )

    def _loc_6F8(): pass

    label('loc_6F8')

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0xC),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(0, 0x0002)

    Jump('loc_724')

    def _loc_708(): pass

    label('loc_708')

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x19),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(0, 0x0002)

    Jump('loc_724')

    def _loc_718(): pass

    label('loc_718')

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0xC),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_724')

    def _loc_724(): pass

    label('loc_724')

    Return()

# id: 0x0002 offset: 0x725
@scena.Code('func_02_725')
def func_02_725():
    OP_20(0x000003E8)
    OP_21()

    Return()

# id: 0x0003 offset: 0x72C
@scena.Code('func_03_72C')
def func_03_72C():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_7F4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7A0',
    )

    ChrTalk(
        0x00FE,
        (
            '啊……啊，导力引擎\n',
            '不能早点动起来吗～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只要出动我自豪的船，\n',
            '一定能捕到百倍的鱼啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))

    Jump('loc_7F0')

    def _loc_7A0(): pass

    label('loc_7A0')

    ChrTalk(
        0x00FE,
        (
            '啊……啊，导力引擎\n',
            '不能早点动起来吗～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在那天到来之前\n',
            '只能省着点了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7F0(): pass

    label('loc_7F0')

    TalkEnd(0x00FE)

    Return()

    def _loc_7F4(): pass

    label('loc_7F4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_8E2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_88A',
    )

    ChrTalk(
        0x00FE,
        (
            '平时的船不能动了，\n',
            '现在只能乘小船去打鱼啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只能捕到很少的一些鱼，\n',
            '生活真困苦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '努力了一天，\n',
            '才终于能赚个酒钱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))

    Jump('loc_8DE')

    def _loc_88A(): pass

    label('loc_88A')

    ChrTalk(
        0x00FE,
        (
            '不能出船，\n',
            '我这个当渔夫的也要失业喽……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '用小船努力一天\n',
            '才终于能赚个酒钱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8DE(): pass

    label('loc_8DE')

    TalkEnd(0x00FE)

    Return()

    def _loc_8E2(): pass

    label('loc_8E2')

    ChrClearFlags(0x00FE, 0x0010)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    If(
        (
            (Expr.PushLong, 0x1E),
            (Expr.GetChrWork, 0xFE, 0x4),
            Expr.Lss,
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x96),
            Expr.Lss,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_90F',
    )

    ChrSetSubChip(0x00FE, 2)

    Jump('loc_935')

    def _loc_90F(): pass

    label('loc_90F')

    If(
        (
            (Expr.PushLong, 0xD2),
            (Expr.GetChrWork, 0xFE, 0x4),
            Expr.Lss,
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x14A),
            Expr.Lss,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_930',
    )

    ChrSetSubChip(0x00FE, 1)

    Jump('loc_935')

    def _loc_930(): pass

    label('loc_930')

    ChrSetSubChip(0x00FE, 0)

    def _loc_935(): pass

    label('loc_935')

    ChrSetDirection(0x00FE, 0, 0)
    ChrSetFlags(0x00FE, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_9A1',
    )

    ChrTalk(
        0x00FE,
        (
            '聚在仓库里的家伙\n',
            '对选举漠不关心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果诺曼成了市长\n',
            '一定会把他们赶出去的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_ADA')

    def _loc_9A1(): pass

    label('loc_9A1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_9E0',
    )

    ChrTalk(
        0x00FE,
        (
            '感觉大家\n',
            '好像都很焦躁。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽说吵架是不好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_ADA')

    def _loc_9E0(): pass

    label('loc_9E0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_A55',
    )

    ChrTalk(
        0x00FE,
        (
            '我是不太明白\n',
            '复杂的东西啦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '确实戴尔蒙市长\n',
            '什么也没为我们做过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '连起重机\n',
            '都没修理过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_ADA')

    def _loc_A55(): pass

    label('loc_A55')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_ADA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_A8B',
    )

    ChrTalk(
        0x00FE,
        (
            '我有空的时候\n',
            '也去帮忙发传单吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_ADA')

    def _loc_A8B(): pass

    label('loc_A8B')

    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))

    ChrTalk(
        0x00FE,
        (
            '因为我是渔夫嘛。\n',
            '没有港口就麻烦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '希望波尔多斯主任\n',
            '多多努力啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_ADA(): pass

    label('loc_ADA')

    ChrSetSubChip(0x00FE, 0)
    TalkEnd(0x00FE)

    Return()

# id: 0x0004 offset: 0xAE3
@scena.Code('func_04_AE3')
def func_04_AE3():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_B9B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B4F',
    )

    ChrTalk(
        0x00FE,
        (
            '导力引擎不能动，\n',
            '我们船员就没事可做。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '飞船的乘务员们，\n',
            '一定也感到无聊吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    Jump('loc_B98')

    def _loc_B4F(): pass

    label('loc_B4F')

    ChrTalk(
        0x00FE,
        (
            '导力引擎不能动，\n',
            '我们船员就没事可做。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就像是被捞起来的鱼一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B98(): pass

    label('loc_B98')

    Jump('loc_F43')

    def _loc_B9B(): pass

    label('loc_B9B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_C7C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C37',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然好多了，\n',
            '但城市还很混乱呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，关键的诺曼市长\n',
            '自己却一直躲在市长官邸……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是的，所以说波尔多斯\n',
            '当市长不就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    Jump('loc_C79')

    def _loc_C37(): pass

    label('loc_C37')

    ChrTalk(
        0x00FE,
        (
            '让诺曼来当\n',
            '结果就是这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是的，卢安市民\n',
            '真是没眼光。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C79(): pass

    label('loc_C79')

    Jump('loc_F43')

    def _loc_C7C(): pass

    label('loc_C7C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_CD8',
    )

    ChrTalk(
        0x00FE,
        (
            '也得告诉桥对面的人\n',
            '港口的问题才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不能只当成是\n',
            '在港口工作的人的问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F43')

    def _loc_CD8(): pass

    label('loc_CD8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_D47',
    )

    ChrTalk(
        0x00FE,
        (
            '总之没人受伤\n',
            '就是万幸了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '波尔多斯\n',
            '在这种时候也很冷静。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '关键时刻\n',
            '果然是可靠的男人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F43')

    def _loc_D47(): pass

    label('loc_D47')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_E3C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_D9F',
    )

    ChrTalk(
        0x00FE,
        (
            '港口问题\n',
            '并不仅是钱的多少问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是这个城市的灵魂问题哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E39')

    def _loc_D9F(): pass

    label('loc_D9F')

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    ChrTalk(
        0x00FE,
        (
            '呀，欢迎。\n',
            '欢迎来到波尔多斯阵营事务所。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为我也是船员。\n',
            '此次的选举确实是一件大事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '让诺曼什么的当市长看看啊。\n',
            '港口只会比现在更萧条的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E39(): pass

    label('loc_E39')

    Jump('loc_F43')

    def _loc_E3C(): pass

    label('loc_E3C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_F43',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_EAF',
    )

    ChrTalk(
        0x00FE,
        (
            '波尔多斯虽然有软弱的一面，\n',
            '但他是真正的海之男儿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不管怎样这次的市长选举\n',
            '都要支持他啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F43')

    def _loc_EAF(): pass

    label('loc_EAF')

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    ChrTalk(
        0x00FE,
        (
            '呀，欢迎。\n',
            '欢迎来到波尔多斯阵营事务所。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '波尔多斯虽然也有软弱的一面，\n',
            '但他是真正的海之男儿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不管怎样这次的市长选举\n',
            '都要支持他啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F43(): pass

    label('loc_F43')

    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0xF47
@scena.Code('func_05_F47')
def func_05_F47():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_10B7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_FBF',
    )

    ChrTalk(
        0x00FE,
        (
            '从现在起要在北街区的运动中\n',
            '投入更多力量。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还是希望经营旅游业的人们\n',
            '也能理解我们的主张啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10B4')

    def _loc_FBF(): pass

    label('loc_FBF')

    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    ChrTalk(
        0x00FE,
        (
            '从现在起要在北街区的运动中\n',
            '投入更多力量。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还是希望经营旅游业的人们\n',
            '也能理解我们的主张啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们也认为旅游业\n',
            '是重要的产业。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只是，要把前市长时期\n',
            '所走的极端\n',
            '重新恢复平衡。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然是简单的道理……\n',
            '却很难得到大家正确的理解。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_10B4(): pass

    label('loc_10B4')

    Jump('loc_13D2')

    def _loc_10B7(): pass

    label('loc_10B7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_1192',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_1112',
    )

    ChrTalk(
        0x00FE,
        (
            '港口的家伙真是\n',
            '性情暴躁得不行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但也说明了\n',
            '老实的人也很多呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_118F')

    def _loc_1112(): pass

    label('loc_1112')

    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    ChrTalk(
        0x00FE,
        (
            '呼，总之\n',
            '还好没闹成大事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '引起这次骚乱的人\n',
            '打算去找诺曼候选人\n',
            '道歉呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '支持者之间的对立\n',
            '可不能遗留下来啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_118F(): pass

    label('loc_118F')

    Jump('loc_13D2')

    def _loc_1192(): pass

    label('loc_1192')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_12CA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_1215',
    )

    ChrTalk(
        0x00FE,
        (
            '卢安经济的中心是旅游业，\n',
            '但也不能为此牺牲港口。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果对老旧化的设施置之不理，\n',
            '就会有发生事故的危险。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12C7')

    def _loc_1215(): pass

    label('loc_1215')

    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    ChrTalk(
        0x00FE,
        (
            '诺曼候选人说得对，\n',
            '卢安经济的中心是旅游业。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，也不能因此\n',
            '就对港口置之不理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果对老旧化的设施置之不理，\n',
            '就会有发生事故的危险。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '变成那样就为时已晚了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_12C7(): pass

    label('loc_12C7')

    Jump('loc_13D2')

    def _loc_12CA(): pass

    label('loc_12CA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_13D2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_1338',
    )

    ChrTalk(
        0x00FE,
        (
            '身为港湾地区的代表，\n',
            '想想我自己都觉得不适合了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎呀哎呀，这次的市长候选人吗～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_13D2')

    def _loc_1338(): pass

    label('loc_1338')

    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    ChrTalk(
        0x00FE,
        (
            '哎呀哎呀，市长候选人\n',
            '真不是我能胜任的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我是被大家硬推上来的。\n',
            '实在没办法才来当候选人的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但既然站出来了，\n',
            '就要以当选为目标而努力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_13D2(): pass

    label('loc_13D2')

    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0x13D6
@scena.Code('func_06_13D6')
def func_06_13D6():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_1414',
    )

    ChrTalk(
        0x0011,
        (
            '对了，外边\n',
            '好像很吵闹……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '……有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1459')

    def _loc_1414(): pass

    label('loc_1414')

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x0011,
        (
            '嗯，价格合适、\n',
            '味道也可以说合格。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '这样游客\n',
            '应该也会喜欢的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1459(): pass

    label('loc_1459')

    TalkEnd(0x00FE)

    Return()

# id: 0x0007 offset: 0x145D
@scena.Code('func_07_145D')
def func_07_145D():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_157F',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0068, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_14C4',
    )

    ChrTalk(
        0x00FE,
        (
            '哈、哈哈哈，\n',
            '只不过是输了一场，没什么啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好了～连赢几盘\n',
            '马上赢回来！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_157C')

    def _loc_14C4(): pass

    label('loc_14C4')

    If(
        (
            (Expr.Eval, "OP_29(0x0068, 0x00, 0x40)"),
            Expr.Return,
        ),
        'loc_1530',
    )

    ChrTalk(
        0x00FE,
        (
            '哈哈哈～～\n',
            '你们也很努力了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，今天是\n',
            '找错了对手。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，暂且\n',
            '在此赚点钱吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_157C')

    def _loc_1530(): pass

    label('loc_1530')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_1575',
    )

    ChrTalk(
        0x000D,
        (
            '呀～你也很努力战斗了。\n',
            '就是找错了对手。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '哈哈哈。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_157C')

    def _loc_1575(): pass

    label('loc_1575')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))
    Call(0, 0x0009)

    def _loc_157C(): pass

    label('loc_157C')

    Jump('loc_169D')

    def _loc_157F(): pass

    label('loc_157F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_1649',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_15D8',
    )

    ChrTalk(
        0x00FE,
        (
            '大家都怕我，\n',
            '不跟我比牌啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没办法只好暂时\n',
            '玩玩吃角子游戏了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1646')

    def _loc_15D8(): pass

    label('loc_15D8')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '呀～吃角子游戏\n',
            '也中大奖了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这是要我辞掉工作\n',
            '专门干这个吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，空之女神一定\n',
            '是这样说的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1646(): pass

    label('loc_1646')

    Jump('loc_169D')

    def _loc_1649(): pass

    label('loc_1649')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_169D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_1696',
    )

    ChrTalk(
        0x00FE,
        (
            '呜哦哦哦，\n',
            '又赢了哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '难不成我\n',
            '是游戏天才！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_169D')

    def _loc_1696(): pass

    label('loc_1696')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))
    Call(0, 0x0009)

    def _loc_169D(): pass

    label('loc_169D')

    TalkEnd(0x00FE)

    Return()

# id: 0x0008 offset: 0x16A1
@scena.Code('func_08_16A1')
def func_08_16A1():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_17C4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1767',
    )

    ChrTalk(
        0x00FE,
        (
            '在１楼的店里\n',
            '洗盘子的打工费到手了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '于是就这样\n',
            '来一决胜负了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '定期船恢复原状之前\n',
            '需要赚交通费嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，虽然以前运气超级不好，\n',
            '只要状态回来了那是小事一桩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    Jump('loc_17C1')

    def _loc_1767(): pass

    label('loc_1767')

    ChrTalk(
        0x00FE,
        (
            '定期船恢复原状之前\n',
            '预定先赚够回去的交通费。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，首先从吃角子游戏开始\n',
            '赚回来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_17C1(): pass

    label('loc_17C1')

    Jump('loc_1980')

    def _loc_17C4(): pass

    label('loc_17C4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_183F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_1802',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯～活动身体来工作\n',
            '总觉得很有充实感啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_183C')

    def _loc_1802(): pass

    label('loc_1802')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '把回家的钱\n',
            '都输光了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以就留在这里打工。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_183C(): pass

    label('loc_183C')

    Jump('loc_1980')

    def _loc_183F(): pass

    label('loc_183F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_1849',
    )

    Jump('loc_1980')

    def _loc_1849(): pass

    label('loc_1849')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_18BE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_18B4',
    )

    ChrTalk(
        0x00FE,
        (
            '呼哦哦哦哦哦～\n',
            '又是我输了！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不、不，一定是搞错了。\n',
            '怎么可能输给这种外行？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_18BB')

    def _loc_18B4(): pass

    label('loc_18B4')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))
    Call(0, 0x0009)

    def _loc_18BB(): pass

    label('loc_18BB')

    Jump('loc_1980')

    def _loc_18BE(): pass

    label('loc_18BE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_1980',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_191D',
    )

    ChrTalk(
        0x00FE,
        (
            '好像玩吃角子游戏\n',
            '的感觉老回不来啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没办法，去找些肥鸭\n',
            '用牌榨干吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1980')

    def _loc_191D(): pass

    label('loc_191D')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '嗯～到底是\n',
            '古董的吃角子游戏机。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '和普通的触感就是不同。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……嗯，就是因此\n',
            '才输了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1980(): pass

    label('loc_1980')

    TalkEnd(0x00FE)

    Return()

# id: 0x0009 offset: 0x1984
@scena.Code('func_09_1984')
def func_09_1984():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_1ADB',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))
    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))
    OP_4A(0x000D, 255)
    OP_4A(0x000B, 255)

    ChrTalk(
        0x000D,
        (
            '……好，来吧～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000D, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1000)

    OP_63(0x000D)
    OP_62(0x000D, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(400)

    ExecExpressionWithReg(
        0x0005,
        (
            Expr.Rand,
            (Expr.PushLong, 0x3),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x5),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1A17',
    )

    ChrTalk(
        0x000D,
        (
            '看吧来了！是Ｊ！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A5B')

    def _loc_1A17(): pass

    label('loc_1A17')

    If(
        (
            (Expr.PushReg, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1A45',
    )

    ChrTalk(
        0x000D,
        (
            '看吧来了！是Ｊｏｋｅｒ！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A5B')

    def _loc_1A45(): pass

    label('loc_1A45')

    ChrTalk(
        0x000D,
        (
            '来了来了！是Ａ！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A5B(): pass

    label('loc_1A5B')

    ChrTalk(
        0x000B,
        (
            '………………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '……客人您赢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '呀～你也很努力战斗了。\n',
            '就是找错了对手。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '哈哈哈。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4B(0x000D, 255)
    OP_4B(0x000B, 255)

    Jump('loc_1CC7')

    def _loc_1ADB(): pass

    label('loc_1ADB')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))
    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))
    OP_4A(0x000D, 255)
    OP_4A(0x000B, 255)
    OP_4A(0x000C, 255)

    ChrTalk(
        0x000B,
        (
            '轮到客人您了哦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '唔唔～…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithReg(
        0x0005,
        (
            Expr.Rand,
            (Expr.PushLong, 0x4),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x5),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1B4C',
    )

    ChrTalk(
        0x000C,
        (
            '好、好！比牌吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1BBD')

    def _loc_1B4C(): pass

    label('loc_1B4C')

    If(
        (
            (Expr.PushReg, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1B70',
    )

    ChrTalk(
        0x000C,
        (
            '当然！比牌吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1BBD')

    def _loc_1B70(): pass

    label('loc_1B70')

    If(
        (
            (Expr.PushReg, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1BA5',
    )

    ChrTalk(
        0x000C,
        (
            '这、这次一定赢！\n',
            '当然，比牌吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1BBD')

    def _loc_1BA5(): pass

    label('loc_1BA5')

    ChrTalk(
        0x000C,
        (
            '一决胜负！比牌吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1BBD(): pass

    label('loc_1BBD')

    ChrTalk(
        0x000D,
        (
            '哼哼，这样好吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithReg(
        0x0005,
        (
            Expr.Rand,
            (Expr.PushLong, 0x4),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x5),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1C07',
    )

    ChrTalk(
        0x000D,
        (
            '这边可是三张Ａ哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C98')

    def _loc_1C07(): pass

    label('loc_1C07')

    If(
        (
            (Expr.PushReg, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1C38',
    )

    ChrTalk(
        0x000D,
        (
            '这边可是绰绰有余的\n',
            '葫芦哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C98')

    def _loc_1C38(): pass

    label('loc_1C38')

    If(
        (
            (Expr.PushReg, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1C5F',
    )

    ChrTalk(
        0x000D,
        (
            '这边可是\n',
            '四条哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C98')

    def _loc_1C5F(): pass

    label('loc_1C5F')

    ChrTalk(
        0x000D,
        (
            '这边可是\n',
            '同花哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '咦？ 仔细一看\n',
            '原来还带顺呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C98(): pass

    label('loc_1C98')

    ChrTalk(
        0x000C,
        (
            '呼哦哦哦哦哦～\n',
            '又是我输了！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4B(0x000D, 255)
    OP_4B(0x000B, 255)
    OP_4B(0x000C, 255)
    def _loc_1CC7(): pass

    label('loc_1CC7')

    Return()

# id: 0x000A offset: 0x1CC8
@scena.Code('func_0A_1CC8')
def func_0A_1CC8():
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
            TXT(0x01, '玩同花顺\n'),
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
        'loc_1D6D',
    )

    FadeOut(300, 0, -1)
    OP_0D()

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_C0(0x0F, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_56(0x00)
    FadeIn(300, 0)
    TalkEnd(0x000B)

    Return()

    def _loc_1D6D(): pass

    label('loc_1D6D')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1D80',
    )

    OP_56(0x00)
    TalkEnd(0x000B)

    Return()

    def _loc_1D80(): pass

    label('loc_1D80')

    Call(0, 0x000B)
    TalkEnd(0x000B)

    Return()

# id: 0x000B offset: 0x1D88
@scena.Code('func_0B_1D88')
def func_0B_1D88():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1FC0',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0068, 0x00, 0x10)"),
            (Expr.Eval, "OP_29(0x0068, 0x00, 0x80)"),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x0416, 6, 0x20B6)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1E91',
    )

    ChrTalk(
        0x000B,
        (
            '啊……\n',
            '好久不见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '当时让我见识了\n',
            '精彩的比赛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1016F啊哈哈……\n',
            '还有那样的委托啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '嗯，虽然我\n',
            '没派上什么用场……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000B, 0x0101, 400)

    ChrTalk(
        0x000B,
        (
            '这真是谦虚了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '可以的话\n',
            '我随时都能奉陪哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '那么，请慢慢\n',
            '享受胜负的乐趣吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))
    SetScenaFlags(ScenaFlag(0x0416, 6, 0x20B6))

    Jump('loc_1FBD')

    def _loc_1E91(): pass

    label('loc_1E91')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_1EE1',
    )

    ChrTalk(
        0x000B,
        (
            '可以的话\n',
            '我随时都能奉陪哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '那么，请慢慢\n',
            '享受胜负的乐趣吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1FBD')

    def _loc_1EE1(): pass

    label('loc_1EE1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_1F94',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1F55',
    )

    ChrTalk(
        0x000B,
        (
            '这种情况下\n',
            '客人也少。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '南区的船员们\n',
            '几乎都不来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '果然桥不能通行的\n',
            '影响很大啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Jump('loc_1F91')

    def _loc_1F55(): pass

    label('loc_1F55')

    ChrTalk(
        0x000B,
        (
            '这种情况下\n',
            '客人也少。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '南区的船员们\n',
            '几乎都不来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1F91(): pass

    label('loc_1F91')

    Jump('loc_1FBD')

    def _loc_1F94(): pass

    label('loc_1F94')

    ChrTalk(
        0x000B,
        (
            '欢迎光临。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '可以的话\n',
            '我奉陪哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1FBD(): pass

    label('loc_1FBD')

    Jump('loc_216F')

    def _loc_1FC0(): pass

    label('loc_1FC0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_20B8',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0068, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_2018',
    )

    ChrTalk(
        0x000B,
        (
            '哟，刚才辛苦了。\n',
            '之后交给我们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '那位客人\n',
            '我们会照顾的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_20B5')

    def _loc_2018(): pass

    label('loc_2018')

    If(
        (
            (Expr.Eval, "OP_29(0x0068, 0x00, 0x40)"),
            Expr.Return,
        ),
        'loc_2071',
    )

    ChrTalk(
        0x000B,
        (
            '游击士们\n',
            '会输也是没办法的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '差不多该是最终武器\n',
            '出场的时候了吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_20B5')

    def _loc_2071(): pass

    label('loc_2071')

    ChrTalk(
        0x000B,
        (
            '这位客人……\n',
            '似乎非常幸运呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '如何？\n',
            '能和客人比试一场吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_20B5(): pass

    label('loc_20B5')

    Jump('loc_216F')

    def _loc_20B8(): pass

    label('loc_20B8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_210E',
    )

    ChrTalk(
        0x000B,
        (
            '支持者们\n',
            '为什么那么热衷于选举呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '难道在选举结果上\n',
            '也压了米拉吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_216F')

    def _loc_210E(): pass

    label('loc_210E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_2133',
    )

    ChrTalk(
        0x000B,
        (
            '客人也来\n',
            '玩牌吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_216F')

    def _loc_2133(): pass

    label('loc_2133')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_216F',
    )

    ChrTalk(
        0x000B,
        (
            '欢迎来到\n',
            '用牌开拓命运的世界……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '我奉陪哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_216F(): pass

    label('loc_216F')

    Return()

# id: 0x000C offset: 0x2170
@scena.Code('func_0C_2170')
def func_0C_2170():
    TalkBegin(0x0018)
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
            TXT(0x01, '玩二十一点\n'),
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
        'loc_2217',
    )

    FadeOut(300, 0, -1)
    OP_0D()

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_C0(0x0D, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_56(0x00)
    FadeIn(300, 0)
    TalkEnd(0x0018)

    Return()

    def _loc_2217(): pass

    label('loc_2217')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_222A',
    )

    OP_56(0x00)
    TalkEnd(0x0018)

    Return()

    def _loc_222A(): pass

    label('loc_222A')

    Call(0, 0x000D)
    TalkEnd(0x0018)

    Return()

# id: 0x000D offset: 0x2232
@scena.Code('func_0D_2232')
def func_0D_2232():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_22C1',
    )

    ChrTalk(
        0x0018,
        (
            '引入非导力式的机器\n',
            '是老板的爱好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '因此我们的吃角子游戏机\n',
            '现在还能用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '说不定是老板的直觉，\n',
            '感到会变成这样也不一定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2551')

    def _loc_22C1(): pass

    label('loc_22C1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_231F',
    )

    ChrTalk(
        0x0018,
        (
            '哟，虽然时世危急，\n',
            '不来比试一盘吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '正是这种时候\n',
            '才需要享受人生的悠闲啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2551')

    def _loc_231F(): pass

    label('loc_231F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_2389',
    )

    ChrTalk(
        0x0018,
        (
            '虽然乘胜追击是很重要，\n',
            '但太得意忘形可是会吃苦头的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '看穿这个节奏，\n',
            '这正是人生的奥秘。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2551')

    def _loc_2389(): pass

    label('loc_2389')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_2449',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Return,
        ),
        'loc_23DF',
    )

    ChrTalk(
        0x0018,
        (
            '我一辈子\n',
            '也不想和政治扯上关系。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '啊啊，当然投票也不会去的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2446')

    def _loc_23DF(): pass

    label('loc_23DF')

    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))

    ChrTalk(
        0x0018,
        (
            '桥那边支持者们\n',
            '好像有纠纷。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '跟政治有关的人，\n',
            '脱了皮都一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '我一辈子都不想扯上关系。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2446(): pass

    label('loc_2446')

    Jump('loc_2551')

    def _loc_2449(): pass

    label('loc_2449')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_2492',
    )

    ChrTalk(
        0x0018,
        (
            '重要的是时机。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '只要不搞错这点，\n',
            '它就能丰富人生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2551')

    def _loc_2492(): pass

    label('loc_2492')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_2551',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Return,
        ),
        'loc_24DA',
    )

    ChrTalk(
        0x0018,
        (
            '二十一点\n',
            '是客人也有胜算的游戏。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '请务必试试。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2551')

    def _loc_24DA(): pass

    label('loc_24DA')

    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))

    ChrTalk(
        0x0018,
        (
            '呀，欢迎。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '这个台子上可以玩\n',
            '二十一点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '是根据玩法确实能赚到钱的\n',
            '少数卡牌游戏之一。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '请随意享受。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2551(): pass

    label('loc_2551')

    Return()

# id: 0x000E offset: 0x2552
@scena.Code('func_0E_2552')
def func_0E_2552():
    TalkBegin(0x000A)
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
            TXT(0x01, '兑换代币\n'),
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
        'loc_25ED',
    )

    OP_0D()

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_25C8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0455, 6, 0x22AE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_25C3',
    )

    OP_A9(0x6C)

    Jump('loc_25C5')

    def _loc_25C3(): pass

    label('loc_25C3')

    OP_A9(0x80)

    def _loc_25C5(): pass

    label('loc_25C5')

    Jump('loc_25D7')

    def _loc_25C8(): pass

    label('loc_25C8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0455, 6, 0x22AE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_25D5',
    )

    OP_A9(0x69)

    Jump('loc_25D7')

    def _loc_25D5(): pass

    label('loc_25D5')

    OP_A9(0x7D)

    def _loc_25D7(): pass

    label('loc_25D7')

    If(
        (
            (Expr.Eval, "OP_40(0x023B, 0x00)"),
            (Expr.PushLong, 0x1),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_25E9',
    )

    SetScenaFlags(ScenaFlag(0x0216, 6, 0x10B6))

    def _loc_25E9(): pass

    label('loc_25E9')

    TalkEnd(0x000A)

    Return()

    def _loc_25ED(): pass

    label('loc_25ED')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2600',
    )

    OP_56(0x00)
    TalkEnd(0x000A)

    Return()

    def _loc_2600(): pass

    label('loc_2600')

    Call(0, 0x000F)
    TalkEnd(0x000A)

    Return()

# id: 0x000F offset: 0x2608
@scena.Code('func_0F_2608')
def func_0F_2608():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_26A8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2661',
    )

    ChrTalk(
        0x000A,
        (
            '客人太少，\n',
            '感觉店也很寂寞。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '真希望导力器\n',
            '尽快恢复原状啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Jump('loc_26A5')

    def _loc_2661(): pass

    label('loc_2661')

    ChrTalk(
        0x000A,
        (
            '客人太少\n',
            '感觉店也很寂寞。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '老板对于这些\n',
            '似乎完全不在乎……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_26A5(): pass

    label('loc_26A5')

    Jump('loc_2AE6')

    def _loc_26A8(): pass

    label('loc_26A8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_2733',
    )

    ChrTalk(
        0x000A,
        (
            '导力器停了的时候\n',
            '老板也很平静。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '真是，任何时候都是那张\n',
            '扑克脸啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '如果内心其实是在心惊胆战的话，\n',
            '那就很有趣了哟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2AE6')

    def _loc_2733(): pass

    label('loc_2733')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_2897',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0068, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_27BE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_2782',
    )

    ChrTalk(
        0x000A,
        (
            '下次请丢开工作\n',
            '再来玩哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '我也会\n',
            '奉陪的㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_27BB')

    def _loc_2782(): pass

    label('loc_2782')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x000A,
        (
            '大家好厉害！\n',
            '我太感动了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '游击士\n',
            '这么强啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_27BB(): pass

    label('loc_27BB')

    Jump('loc_2894')

    def _loc_27BE(): pass

    label('loc_27BE')

    If(
        (
            (Expr.Eval, "OP_29(0x0068, 0x00, 0x40)"),
            Expr.Return,
        ),
        'loc_2846',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_2803',
    )

    ChrTalk(
        0x000A,
        (
            '呜呼呼，好久没有\n',
            '这么认真玩了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '嗯嗯⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2843')

    def _loc_2803(): pass

    label('loc_2803')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x000A,
        (
            '各位真是遗憾啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '但是没关系哦。\n',
            '我会帮你们报仇的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2843(): pass

    label('loc_2843')

    Jump('loc_2894')

    def _loc_2846(): pass

    label('loc_2846')

    ChrTalk(
        0x000A,
        (
            '刚才开始费高先生\n',
            '就和老板用眼神交流着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '难道…\n',
            '是轮到我出场了吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_2894(): pass

    label('loc_2894')

    Jump('loc_2AE6')

    def _loc_2897(): pass

    label('loc_2897')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_291F',
    )

    ChrTalk(
        0x000A,
        (
            '老板他无论\n',
            '客人怎么赢\n',
            '都完全不动摇哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '还能若无其事地\n',
            '和那人聊天气呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '摆出那种扑克脸，\n',
            '到底是深谙此道之人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2AE6')

    def _loc_291F(): pass

    label('loc_291F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_2A6B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_2A03',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_29B5',
    )

    ChrTalk(
        0x000A,
        (
            '真是的～客人\n',
            '还真是固执呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '明白了。\n',
            '那么稍微给点提示㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '……头发长的一方获胜哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2A00')

    def _loc_29B5(): pass

    label('loc_29B5')

    ChrTalk(
        0x000A,
        (
            '所以说，其实我知道哦。\n',
            '选举哪一方会胜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '当然不会跟任何人说的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2A00(): pass

    label('loc_2A00')

    Jump('loc_2A68')

    def _loc_2A03(): pass

    label('loc_2A03')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x000A,
        (
            '别看我这样\n',
            '可是很擅长这个的哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '不知为何就是知道。\n',
            '一看就知道会来什么牌或者骰子是多少。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_2A68(): pass

    label('loc_2A68')

    Jump('loc_2AE6')

    def _loc_2A6B(): pass

    label('loc_2A6B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_2AE6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_2AA3',
    )

    ChrTalk(
        0x000A,
        (
            '不明白怎么玩的时候\n',
            '就尽管问我哦㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2AE6')

    def _loc_2AA3(): pass

    label('loc_2AA3')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x000A,
        (
            '我最近刚刚\n',
            '加入这家店哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '在很热闹的地方\n',
            '快乐地工作！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2AE6(): pass

    label('loc_2AE6')

    Return()

# id: 0x0010 offset: 0x2AE7
@scena.Code('func_10_2AE7')
def func_10_2AE7():
    TalkBegin(0x00FF)
    FadeOut(300, 0, 100)

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

    Menu(
        0,
        10,
        10,
        1,
        (
            TXT(0x00, '玩１代币\n'),
            TXT(0x01, '离开\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_56(0x00)
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2B8F',
    )

    FadeOut(300, 0, -1)
    OP_0D()

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_C0(0x0C, 0x00000001, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_56(0x00)
    FadeIn(300, 0)

    def _loc_2B8F(): pass

    label('loc_2B8F')

    TalkEnd(0x00FF)

    Return()

# id: 0x0011 offset: 0x2B93
@scena.Code('func_11_2B93')
def func_11_2B93():
    TalkBegin(0x00FF)
    FadeOut(300, 0, 100)

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

    Menu(
        0,
        10,
        10,
        1,
        (
            TXT(0x00, '玩１０代币\n'),
            TXT(0x01, '离开\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_56(0x00)
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2C3D',
    )

    FadeOut(300, 0, -1)
    OP_0D()

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_C0(0x0C, 0x0000000A, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_56(0x00)
    FadeIn(300, 0)

    def _loc_2C3D(): pass

    label('loc_2C3D')

    TalkEnd(0x00FF)

    Return()

# id: 0x0012 offset: 0x2C41
@scena.Code('func_12_2C41')
def func_12_2C41():
    TalkBegin(0x0009)
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
            TXT(0x01, '玩轮盘\n'),
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
        'loc_2CE4',
    )

    FadeOut(300, 0, -1)
    OP_0D()

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_C0(0x0B, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_56(0x00)
    FadeIn(300, 0)
    TalkEnd(0x0009)

    Return()

    def _loc_2CE4(): pass

    label('loc_2CE4')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2CF7',
    )

    OP_56(0x00)
    TalkEnd(0x0009)

    Return()

    def _loc_2CF7(): pass

    label('loc_2CF7')

    Call(0, 0x0013)
    TalkEnd(0x0009)

    Return()

# id: 0x0013 offset: 0x2CFF
@scena.Code('func_13_2CFF')
def func_13_2CFF():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_2E25',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2DB8',
    )

    ChrTalk(
        0x0009,
        (
            '刚才到屋顶上\n',
            '透了口气……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '那个浮在天上的物体\n',
            '总是散发着金色的光芒啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '明明是那么异样的存在，\n',
            '但最近却好像已经习惯了似的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '唔，习惯还\n',
            '真是可怕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Jump('loc_2E22')

    def _loc_2DB8(): pass

    label('loc_2DB8')

    ChrTalk(
        0x0009,
        (
            '那种东西的存在本身\n',
            '实在应该令人觉得奇怪……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '但看着看着就习惯了，\n',
            '这正是人这种生物可怕的地方啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2E22(): pass

    label('loc_2E22')

    Jump('loc_3367')

    def _loc_2E25(): pass

    label('loc_2E25')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_2F30',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2EC3',
    )

    ChrTalk(
        0x0009,
        (
            '欢迎来到\n',
            '『拉旺塔尔』游戏吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '虽然现在是这样的非常时期，\n',
            '但还请和平常一样的享受。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '因为本店的娱乐机器是\n',
            '非导力驱动的古董。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Jump('loc_2F2D')

    def _loc_2EC3(): pass

    label('loc_2EC3')

    ChrTalk(
        0x0009,
        (
            '虽然现在是这样的非常时期，\n',
            '本店还是和平时一样正在营业。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '正是在事态严峻的时候\n',
            '世间才更需要娱乐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2F2D(): pass

    label('loc_2F2D')

    Jump('loc_3367')

    def _loc_2F30(): pass

    label('loc_2F30')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_305C',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0068, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_2F9C',
    )

    ChrTalk(
        0x0009,
        (
            '如果胜运偏离了\n',
            '以后就很难再回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '那位客人，马上就会把\n',
            '赢走的份都输回去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3059')

    def _loc_2F9C(): pass

    label('loc_2F9C')

    If(
        (
            (Expr.Eval, "OP_29(0x0068, 0x00, 0x40)"),
            Expr.Return,
        ),
        'loc_2FDB',
    )

    ChrTalk(
        0x0009,
        (
            '唔，没办法啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '差不多该轮到她出场了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3059')

    def _loc_2FDB(): pass

    label('loc_2FDB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_3016',
    )

    ChrTalk(
        0x0009,
        (
            '乘着气势得来的胜利\n',
            '要崩溃起来也是很快的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3059')

    def _loc_3016(): pass

    label('loc_3016')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x0009,
        (
            '唔，那位客人似乎\n',
            '乘上胜运了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '只有祈祷他\n',
            '不要失足了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3059(): pass

    label('loc_3059')

    Jump('loc_3367')

    def _loc_305C(): pass

    label('loc_305C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_311D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_3092',
    )

    ChrTalk(
        0x0009,
        (
            '希望新市长也能继续\n',
            '援助旅游业。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_311A')

    def _loc_3092(): pass

    label('loc_3092')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x0009,
        (
            '虽然前市长很不幸的\n',
            '发生那样的事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '但前市长重视旅游的政策\n',
            '对我们的店也有很大帮助。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '希望新市长也能继续\n',
            '援助旅游业啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_311A(): pass

    label('loc_311A')

    Jump('loc_3367')

    def _loc_311D(): pass

    label('loc_311D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_31FF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_3182',
    )

    ChrTalk(
        0x0009,
        (
            '本店引以自豪的吃角子游戏机\n',
            '已经试过了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '全部是非导力驱动\n',
            '的古董哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_31FC')

    def _loc_3182(): pass

    label('loc_3182')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x0009,
        (
            '本店引以自豪的吃角子游戏机\n',
            '已经试过了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '全部是非导力驱动\n',
            '的古董。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '应该能体会到\n',
            '拉杆所具有的厚重感哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_31FC(): pass

    label('loc_31FC')

    Jump('loc_3367')

    def _loc_31FF(): pass

    label('loc_31FF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_3367',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_325A',
    )

    ChrTalk(
        0x0009,
        (
            '欢迎来到\n',
            '『拉旺塔尔』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '虽然让大家久等了，\n',
            '总算重新装修开张了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3367')

    def _loc_325A(): pass

    label('loc_325A')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x0009,
        (
            '欢迎来到\n',
            '『拉旺塔尔』游戏吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '世上有无法进行合理判断\n',
            '而被迫进行选择的时候。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '可是，女神传授给了我们\n',
            '解决那种状况的方法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '……对，那就是第六感。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '和人生的选择一样，\n',
            '它的胜负\n',
            '也是找不到合理的理由的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '是否能用直觉感知危机，\n',
            '那就是它的真髓。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3367(): pass

    label('loc_3367')

    Return()

# id: 0x0014 offset: 0x3368
@scena.Code('func_14_3368')
def func_14_3368():
    TalkBegin(0x0010)
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
            TXT(0x02, '招牌菜『海风通心汤粉』　400米拉\n'),
            TXT(0x03, '离开\n'),
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
        'loc_33E6',
    )

    OP_0D()
    OP_A9(0x6A)
    OP_56(0x00)
    TalkEnd(0x0010)

    Return()

    def _loc_33E6(): pass

    label('loc_33E6')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_34F4',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x12),
            (Expr.PushLong, 0x190),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_34BF',
    )

    RemoveMira(400)
    FadeOut(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    PlaySE(11, 0x00, 0x64)

    Talk(
        (
            TxtCtl.ShowAll,
            (TxtCtl.SetColor, 0x2),
            '海风通心汤粉',
            (TxtCtl.SetColor, 0x0),
            '已经品尝过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetStatus(ChrTable['艾丝蒂尔'], 0xFD, 800)
    ChrSetStatus(ChrTable['约修亚'], 0xFD, 800)
    ChrSetStatus(ChrTable['雪拉扎德'], 0xFD, 800)
    ChrSetStatus(ChrTable['奥利维尔'], 0xFD, 800)
    ChrSetStatus(ChrTable['科洛丝'], 0xFD, 800)
    ChrSetStatus(ChrTable['阿加特'], 0xFD, 800)
    ChrSetStatus(ChrTable['提妲'], 0xFD, 800)
    ChrSetStatus(ChrTable['金'], 0xFD, 800)
    ChrSetStatus(ChrTable['凯文神父'], 0xFD, 800)

    If(
        (
            (Expr.Eval, "OP_40(0x020D, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_34B1',
    )

    If(
        (
            (Expr.Eval, "OP_AC(0x0003)"),
            Expr.Return,
        ),
        'loc_3485',
    )

    Jump('loc_34B1')

    def _loc_3485(): pass

    label('loc_3485')

    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            TxtCtl.ShowAll,
            (TxtCtl.SetColor, 0x2),
            '海风通心汤粉',
            (TxtCtl.SetColor, 0x0),
            '的做法已经学会了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_34B1(): pass

    label('loc_34B1')

    OP_56(0x00)
    FadeIn(1000, 0)

    Jump('loc_34E5')

    def _loc_34BF(): pass

    label('loc_34BF')

    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            '没有足够的米拉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeIn(300, 0)
    def _loc_34E5(): pass

    label('loc_34E5')

    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x0010)

    Return()

    def _loc_34F4(): pass

    label('loc_34F4')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3505',
    )

    TalkEnd(0x0010)

    Return()

    def _loc_3505(): pass

    label('loc_3505')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_35FD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_35B5',
    )

    ChrTalk(
        0x00FE,
        (
            '渔夫们也很困苦哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '满载导力引擎的船全部不能动了，\n',
            '只能出动小型船。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，有工作做\n',
            '就算不错了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看看船员们吧。\n',
            '全都沉没在里面的二楼了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    Jump('loc_35FA')

    def _loc_35B5(): pass

    label('loc_35B5')

    ChrTalk(
        0x00FE,
        (
            '渔夫们也很困苦哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，还算有工作做，\n',
            '比起船员还好点吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_35FA(): pass

    label('loc_35FA')

    Jump('loc_3A88')

    def _loc_35FD(): pass

    label('loc_35FD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_36CD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_366C',
    )

    ChrTalk(
        0x00FE,
        (
            '欢迎光临。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '把柴火放进暖炉后\n',
            '总算能营业了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '暂时还是按照平日的\n',
            '菜单来做的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    Jump('loc_36CA')

    def _loc_366C(): pass

    label('loc_366C')

    ChrTalk(
        0x00FE,
        (
            '把柴火放进暖炉后\n',
            '总算能营业了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '厨房也快变成桑拿浴室了，\n',
            '现在只能靠气势渡过难关啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_36CA(): pass

    label('loc_36CA')

    Jump('loc_3A88')

    def _loc_36CD(): pass

    label('loc_36CD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_37C6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_3727',
    )

    ChrTalk(
        0x00FE,
        (
            '都参加过武术大会了，\n',
            '却又回到仓库生活。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是没有上进心的家伙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_37C3')

    def _loc_3727(): pass

    label('loc_3727')

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    ChrTalk(
        0x00FE,
        (
            '这么说来渡鸦帮的家伙\n',
            '参加了王都的武术大会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在利贝尔通讯上看到照片\n',
            '的时候真是大吃一惊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '话虽如此，结果还是和以前一样\n',
            '又回到了仓库生活。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_37C3(): pass

    label('loc_37C3')

    Jump('loc_3A88')

    def _loc_37C6(): pass

    label('loc_37C6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_38AD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_3827',
    )

    ChrTalk(
        0x00FE,
        (
            '在有选举权的人眼前引起骚动\n',
            '可不妙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是打起来的话\n',
            '超级破坏形象啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_38AA')

    def _loc_3827(): pass

    label('loc_3827')

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    ChrTalk(
        0x00FE,
        (
            '骚动的事我听说了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '确实对方也有错的地方，\n',
            '但出言挑衅的人也不对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有选举权的人都在看着呢，\n',
            '以后做事希望能三思啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_38AA(): pass

    label('loc_38AA')

    Jump('loc_3A88')

    def _loc_38AD(): pass

    label('loc_38AD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_39B5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_3920',
    )

    ChrTalk(
        0x00FE,
        (
            '与海共同生活的人\n',
            '拥有对这个城市港口的留恋。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '波尔多斯就是代表这个心情\n',
            '的市长候选人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_39B2')

    def _loc_3920(): pass

    label('loc_3920')

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    ChrTalk(
        0x00FE,
        (
            '我原来也是渔夫，\n',
            '有着对这个城市港口的留恋。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '波尔多斯就是代表这个心情\n',
            '的市长候选人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就算再怎么糊涂也不会\n',
            '投票给诺曼那暴发户的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_39B2(): pass

    label('loc_39B2')

    Jump('loc_3A88')

    def _loc_39B5(): pass

    label('loc_39B5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_3A88',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_39EB',
    )

    ChrTalk(
        0x00FE,
        (
            '哟！欢迎光临。\n',
            '欢迎来亚克罗萨。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3A88')

    def _loc_39EB(): pass

    label('loc_39EB')

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    ChrTalk(
        0x00FE,
        (
            '哟！欢迎光临。\n',
            '欢迎来亚克罗萨。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '二楼成为波尔多斯\n',
            '先生的选举事务所了，\n',
            '不过店里还是和平时一样在营业啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '请尽情享受\n',
            '我们这儿自豪的新鲜海鲜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3A88(): pass

    label('loc_3A88')

    TalkEnd(0x0010)

    Return()

# id: 0x0015 offset: 0x3A8C
@scena.Code('func_15_3A8C')
def func_15_3A8C():
    Call(0, 0x0016)

    Return()

# id: 0x0016 offset: 0x3A91
@scena.Code('func_16_3A91')
def func_16_3A91():
    TalkBegin(0x0008)
    Call(6, 0x0004)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3AAB',
    )

    OP_A9(0x68)
    TalkEnd(0x0008)

    Return()

    def _loc_3AAB(): pass

    label('loc_3AAB')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3ABC',
    )

    TalkEnd(0x0008)

    Return()

    def _loc_3ABC(): pass

    label('loc_3ABC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_3BA8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3B5B',
    )

    ChrTalk(
        0x0008,
        (
            '弟弟上次来店里\n',
            '到底是多久以前的事了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '嗯，要改变心情\n',
            '就得开始努力了，\n',
            '我也要开始支持啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '无论怎么说\n',
            '他是我唯一的弟弟嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_3BA5')

    def _loc_3B5B(): pass

    label('loc_3B5B')

    ChrTalk(
        0x0008,
        (
            '弟弟上次来店里\n',
            '到底是多久以前的事了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '为此勉强开店\n',
            '也值得了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3BA5(): pass

    label('loc_3BA5')

    Jump('loc_3FE3')

    def _loc_3BA8(): pass

    label('loc_3BA8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_3C97',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3C3A',
    )

    ChrTalk(
        0x0008,
        (
            '桥还是吊在上面，\n',
            '炉子也不能用，真头痛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '尽管如此\n',
            '还是勉强开店营业……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '不过说实话，真不知道\n',
            '要持续到什么时候。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_3C94')

    def _loc_3C3A(): pass

    label('loc_3C3A')

    ChrTalk(
        0x0008,
        (
            '桥还是吊在上面，\n',
            '炉子也不能用，真头痛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '军队或者游击士谁都行，\n',
            '赶快想点办法吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3C94(): pass

    label('loc_3C94')

    Jump('loc_3FE3')

    def _loc_3C97(): pass

    label('loc_3C97')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_3D40',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_3CEA',
    )

    ChrTalk(
        0x0008,
        (
            '不过，连路费\n',
            '都输光了真是难以置信。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '想必是\n',
            '冲昏了头吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3D3D')

    def _loc_3CEA(): pass

    label('loc_3CEA')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '在娱乐场输光了的客人\n',
            '我就雇他们打零工。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '嗯，有他们在\n',
            '就不会有麻烦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3D3D(): pass

    label('loc_3D3D')

    Jump('loc_3FE3')

    def _loc_3D40(): pass

    label('loc_3D40')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_3DB7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3D63',
    )

    ChrTalk(
        0x0008,
        (
            '哟，游击士们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3D63(): pass

    label('loc_3D63')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '刚才真是危险，\n',
            '还好没事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '双方都很热心是没错，\n',
            '但希望能再成熟点啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3FE3')

    def _loc_3DB7(): pass

    label('loc_3DB7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_3E8B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_3E31',
    )

    ChrTalk(
        0x0008,
        (
            '那边很近的酒店\n',
            '是诺曼阵营的事务所。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '经常为众多的宣传员\n',
            '叫外卖，\n',
            '对我们来说也是不错的客人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3E88')

    def _loc_3E31(): pass

    label('loc_3E31')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '在这附近做买卖的人\n',
            '全都支持诺曼先生哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '要是没有游客\n',
            '买卖就做不下去了嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3E88(): pass

    label('loc_3E88')

    Jump('loc_3FE3')

    def _loc_3E8B(): pass

    label('loc_3E8B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_3FE3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_3F27',
    )

    ChrTalk(
        0x0008,
        (
            '我弟弟迪恩好像\n',
            '参加了最近的武术大会呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '但是，才刚刚有点改观，\n',
            '现在却又在仓库里偷懒了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '那些家伙真是，\n',
            '到底有没有干劲啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3FE3')

    def _loc_3F27(): pass

    label('loc_3F27')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '我弟弟迪恩\n',
            '在港口的渡鸦帮\n',
            '当小混混……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '那些家伙们似乎\n',
            '参加了最近的武术大会呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '但是，才刚刚有点改观，\n',
            '现在却又在仓库里偷懒了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '那些家伙真是的…\n',
            '到底有没有干劲啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3FE3(): pass

    label('loc_3FE3')

    TalkEnd(0x0008)

    Return()

# id: 0x0017 offset: 0x3FE7
@scena.Code('func_17_3FE7')
def func_17_3FE7():
    TalkBegin(0x000F)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_40E2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_407E',
    )

    ChrTalk(
        0x00FE,
        (
            '#0450360364V#1740F嘿嘿，来大哥的店\n',
            '吃午饭呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0450360365V真是好久没有\n',
            '在外边碰到了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0450360366V以后经常\n',
            '来露个脸吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 5, 0xD))

    Jump('loc_40E2')

    def _loc_407E(): pass

    label('loc_407E')

    ChrTalk(
        0x00FE,
        (
            '#0450360367V#1740F大哥做的饭菜\n',
            '果然是最美味的啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0450360368V#1746F嘿，令人想起\n',
            '妈妈的事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_40E2(): pass

    label('loc_40E2')

    TalkEnd(0x000F)

    Return()

# id: 0x0018 offset: 0x40E6
@scena.Code('func_18_40E6')
def func_18_40E6():
    TalkBegin(0x0017)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_41C2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_416D',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，出航的时候\n',
            '总是怀念陆地……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不能出航的时候，\n',
            '反而怀念起大海来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎呀，人总是\n',
            '不能满足啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 7, 0xF))

    Jump('loc_41BF')

    def _loc_416D(): pass

    label('loc_416D')

    ChrTalk(
        0x00FE,
        (
            '不能出航的时候，\n',
            '就怀念起大海来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '船员这种生物\n',
            '果然不能在陆上久留啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_41BF(): pass

    label('loc_41BF')

    Jump('loc_4273')

    def _loc_41C2(): pass

    label('loc_41C2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_4273',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4223',
    )

    ChrTalk(
        0x00FE,
        (
            '航海归来是好，\n',
            '却又不能出航了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就当是休息的机会\n',
            '老实地喝喝酒吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 7, 0xF))

    Jump('loc_4273')

    def _loc_4223(): pass

    label('loc_4223')

    ChrTalk(
        0x00FE,
        (
            '航海归来是好，\n',
            '却又不能出航了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '导力器竟然动不了，\n',
            '到底是什么原因呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4273(): pass

    label('loc_4273')

    TalkEnd(0x0017)

    Return()

# id: 0x0019 offset: 0x4277
@scena.Code('func_19_4277')
def func_19_4277():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_42DA',
    )

    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '心里一直想着去赚钱。\n',
            '『拉旺塔尔』游戏吧',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Jump('loc_4348')

    def _loc_42DA(): pass

    label('loc_42DA')

    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '祝．新拉旺塔尔开张！\n',
            '为你带来惊险和兴奋。\n',
            '『拉旺塔尔』游戏吧',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    def _loc_4348(): pass

    label('loc_4348')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
