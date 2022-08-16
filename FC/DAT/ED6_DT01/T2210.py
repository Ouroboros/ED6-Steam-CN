import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T2210_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2210   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'T2210.x'
    header.mapIndex       = 1
    header.bgm            = 12
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT01/T2210._SN', 'ED6_DT01/T2210_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0x000157C0,
            dword_04        = 0x00000000,
            dword_08        = 0x000055F0,
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
        ('ED6_DT07/CH02410._CH', 'ED6_DT07/CH02410P._CP'),
        ('ED6_DT07/CH02470._CH', 'ED6_DT07/CH02470P._CP'),
        ('ED6_DT06/CH20088._CH', 'ED6_DT06/CH20088P._CP'),
        ('ED6_DT07/CH02060._CH', 'ED6_DT07/CH02060P._CP'),
        ('ED6_DT07/CH01350._CH', 'ED6_DT07/CH01350P._CP'),
        ('ED6_DT09/CH11020._CH', 'ED6_DT09/CH11020P._CP'),
        ('ED6_DT09/CH11021._CH', 'ED6_DT09/CH11021P._CP'),
        ('ED6_DT09/CH11022._CH', 'ED6_DT09/CH11022P._CP'),
        ('ED6_DT07/CH00100._CH', 'ED6_DT07/CH00100P._CP'),
        ('ED6_DT07/CH00110._CH', 'ED6_DT07/CH00110P._CP'),
        ('ED6_DT07/CH00140._CH', 'ED6_DT07/CH00140P._CP'),
        ('ED6_DT07/CH00101._CH', 'ED6_DT07/CH00101P._CP'),
        ('ED6_DT07/CH00111._CH', 'ED6_DT07/CH00111P._CP'),
        ('ED6_DT07/CH00141._CH', 'ED6_DT07/CH00141P._CP'),
        ('ED6_DT07/CH02420._CH', 'ED6_DT07/CH02420P._CP'),
        ('ED6_DT07/CH02540._CH', 'ED6_DT07/CH02540P._CP'),
        ('ED6_DT07/CH01560._CH', 'ED6_DT07/CH01560P._CP'),
        ('ED6_DT07/CH01280._CH', 'ED6_DT07/CH01280P._CP'),
        ('ED6_DT06/CH20081._CH', 'ED6_DT06/CH20081P._CP'),
        ('ED6_DT06/CH20082._CH', 'ED6_DT06/CH20082P._CP'),
        ('ED6_DT09/CH11030._CH', 'ED6_DT09/CH11030P._CP'),
        ('ED6_DT09/CH11031._CH', 'ED6_DT09/CH11031P._CP'),
        ('ED6_DT09/CH11032._CH', 'ED6_DT09/CH11032P._CP'),
        ('ED6_DT06/CH20020._CH', 'ED6_DT06/CH20020P._CP'),
        ('ED6_DT06/CH20021._CH', 'ED6_DT06/CH20021P._CP'),
        ('ED6_DT06/CH20034._CH', 'ED6_DT06/CH20034P._CP'),
    ]

# id: 0x10001 offset: 0x17A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '戴尔蒙市长',
            x                   = -63850,
            z                   = 0,
            y                   = 34900,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '奈尔',
            x                   = 24500,
            z                   = 0,
            y                   = 6100,
            direction           = 270,
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
            name                = '杜南公爵',
            x                   = 24500,
            z                   = 0,
            y                   = 6100,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0195,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '管家菲利普',
            x                   = 24500,
            z                   = 0,
            y                   = 6100,
            direction           = 270,
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
            name                = '芙罗拉',
            x                   = 470,
            z                   = 0,
            y                   = -670,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '多米尼克',
            x                   = -59600,
            z                   = 0,
            y                   = -18600,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '飞球',
            x                   = 24500,
            z                   = 0,
            y                   = 6100,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '野马',
            x                   = 24500,
            z                   = 0,
            y                   = 6100,
            direction           = 270,
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
            name                = '秘书基尔巴特',
            x                   = 4530,
            z                   = 0,
            y                   = 36330,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '照相机',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '达里奥',
            x                   = 68100,
            z                   = 0,
            y                   = -9000,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 16,
            chipIndex           = 16,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '比古',
            x                   = 37390,
            z                   = 0,
            y                   = 34110,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '玻璃杯',
            x                   = 20,
            z                   = 700,
            y                   = 39430,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 24,
            chipIndex           = 24,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '玻璃杯',
            x                   = -780,
            z                   = 700,
            y                   = 38600,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 24,
            chipIndex           = 24,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '瓶子',
            x                   = -150,
            z                   = 750,
            y                   = 38740,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1966103,
            chipIndex           = 23,
            npcIndex            = 0x01E6,
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
            dword_10            = 65560,
            chipIndex           = 24,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '玻璃杯',
            x                   = -780,
            z                   = 700,
            y                   = 38600,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 65560,
            chipIndex           = 24,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '瓶子',
            x                   = -150,
            z                   = 750,
            y                   = 38740,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1966103,
            chipIndex           = 23,
            npcIndex            = 0x01E6,
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
            dword_10            = 917528,
            chipIndex           = 24,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x3DA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x3DA
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x3DA
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -475,
            triggerZ            = 0,
            triggerY            = 3173,
            triggerRange        = 800,
            actorX              = -475,
            actorZ              = 800,
            actorY              = 3173,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000A,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -63800,
            triggerZ            = 0,
            triggerY            = 50790,
            triggerRange        = 900,
            actorX              = -63800,
            actorZ              = -300,
            actorY              = 50790,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0016,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -62370,
            triggerZ            = 0,
            triggerY            = -43110,
            triggerRange        = 500,
            actorX              = -62370,
            actorZ              = 2000,
            actorY              = -43110,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0017,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -59500,
            triggerZ            = 250,
            triggerY            = -36760,
            triggerRange        = 800,
            actorX              = -59500,
            actorZ              = 1250,
            actorY              = -36760,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0018,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x46A
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_4B1',
    )

    ChrSetPos(0x000C, -700, 0, -710, 90)
    ChrSetPos(0x000D, 790, 0, -710, 270)
    ChrSetPos(0x0013, 36970, 0, 27900, 270)
    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0010, 0x0080)

    Jump('loc_612')

    def _loc_4B1(): pass

    label('loc_4B1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_4FD',
    )

    ChrSetPos(0x000C, 36850, 0, 31730, 0)
    ChrSetFlags(0x000C, 0x0010)
    ChrSetPos(0x000D, 35800, 0, 34250, 180)
    ChrSetPos(0x0013, 36970, 0, 27900, 270)
    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0010, 0x0080)

    Jump('loc_612')

    def _loc_4FD(): pass

    label('loc_4FD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_573',
    )

    ChrSetPos(0x000C, 67550, 0, 28050, 90)
    ChrSetPos(0x000D, -61450, 0, 2440, 180)
    ChrSetPos(0x0013, 36970, 0, 27900, 270)

    If(
        (
            (Expr.Eval, "OP_29(0x0020, 0x00, 0x04)"),
            Expr.Return,
        ),
        'loc_55A',
    )

    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0010, 4530, 0, 36330, 90)

    Jump('loc_570')

    def _loc_55A(): pass

    label('loc_55A')

    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0010, 0, 0, 1800, 0)

    def _loc_570(): pass

    label('loc_570')

    Jump('loc_612')

    def _loc_573(): pass

    label('loc_573')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_5C1',
    )

    ChrSetPos(0x000C, 36850, 0, 31730, 0)
    ChrSetPos(0x000D, 35800, 0, 34250, 180)
    ChrSetPos(0x0013, 36970, 0, 27900, 270)
    ChrSetPos(0x0012, -2090, 0, 2630, 180)

    Jump('loc_612')

    def _loc_5C1(): pass

    label('loc_5C1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_5DC',
    )

    ChrSetPos(0x0013, 36970, 0, 27900, 270)

    Jump('loc_612')

    def _loc_5DC(): pass

    label('loc_5DC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 7, 0x417)),
            Expr.Return,
        ),
        'loc_5F7',
    )

    ChrSetPos(0x000C, 33500, 0, 24550, 270)

    Jump('loc_612')

    def _loc_5F7(): pass

    label('loc_5F7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 4, 0x414)),
            Expr.Return,
        ),
        'loc_612',
    )

    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0008, 0x0008)
    ChrSetFlags(0x0010, 0x0080)
    ChrSetFlags(0x0010, 0x0008)

    def _loc_612(): pass

    label('loc_612')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_622'),
        (0x00000072, 'loc_669'),
        (-1, 'loc_67F'),
    )

    def _loc_622(): pass

    label('loc_622')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0088, 0, 0x440)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 7, 0x43F)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_638',
    )

    SetScenaFlags(ScenaFlag(0x0088, 0, 0x440))
    Event(0, func_0B_2B53)

    Jump('loc_666')

    def _loc_638(): pass

    label('loc_638')

    If(
        (
            (Expr.Eval, "OP_29(0x0020, 0x01, 0x0200)"),
            (Expr.Eval, "OP_29(0x0020, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0020, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_666',
    )

    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0008, 0x0080)
    OP_28(0x0020, 0x04, 0x10)
    Event(1, 0x0004)

    def _loc_666(): pass

    label('loc_666')

    Jump('loc_67F')

    def _loc_669(): pass

    label('loc_669')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0088, 1, 0x441)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0088, 0, 0x440)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_67C',
    )

    SetScenaFlags(ScenaFlag(0x0088, 1, 0x441))
    Event(0, func_0C_3441)

    def _loc_67C(): pass

    label('loc_67C')

    Jump('loc_67F')

    def _loc_67F(): pass

    label('loc_67F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 3, 0x3FB)),
            Expr.Return,
        ),
        'loc_696',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x51),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    Event(0, func_0D_61B6)

    def _loc_696(): pass

    label('loc_696')

    Return()

# id: 0x0001 offset: 0x697
@scena.Code('func_01_697')
def func_01_697():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            (Expr.TestScenaFlags, ScenaFlag(0x0088, 2, 0x442)),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0020, 0x01, 0x0200)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_6D4',
    )

    OP_71(0x0007, 0x0004)
    OP_71(0x0000, 0x0004)
    OP_71(0x0001, 0x0004)
    OP_71(0x0002, 0x0004)
    OP_71(0x0003, 0x0004)
    OP_71(0x0004, 0x0004)
    OP_71(0x0005, 0x0004)
    OP_71(0x0006, 0x0004)

    def _loc_6D4(): pass

    label('loc_6D4')

    OP_72(0x0010, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_6E7',
    )

    OP_6F(0x0010, 300)

    def _loc_6E7(): pass

    label('loc_6E7')

    Return()

# id: 0x0002 offset: 0x6E8
@scena.Code('func_02_6E8')
def func_02_6E8():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_6FD',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_6E8')

    def _loc_6FD(): pass

    label('loc_6FD')

    Return()

# id: 0x0003 offset: 0x6FE
@scena.Code('func_03_6FE')
def func_03_6FE():
    If(
        (
            (Expr.Eval, "OP_29(0x0020, 0x00, 0x04)"),
            Expr.Return,
        ),
        'loc_72E',
    )

    def _loc_708(): pass

    label('loc_708')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_72B',
    )

    OP_8D(0x00FE, 3420, 32950, 6190, 40410, 1500)

    Jump('loc_708')

    def _loc_72B(): pass

    label('loc_72B')

    Jump('loc_743')

    def _loc_72E(): pass

    label('loc_72E')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_743',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_72E')

    def _loc_743(): pass

    label('loc_743')

    Return()

# id: 0x0004 offset: 0x744
@scena.Code('func_04_744')
def func_04_744():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_A5D',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0020, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_877',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_80D',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '#0490170399V#660F各位，\n',
            '这一次真是辛苦你们了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490170400V本来我应该\n',
            '专程去向你们道谢的。\n',
            '无奈事情堆积如山。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490170401V非常抱歉，\n',
            '我现在有事在身，没有时间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_874')

    def _loc_80D(): pass

    label('loc_80D')

    ChrTalk(
        0x00FE,
        (
            '#0490170399V#660F各位，\n',
            '这一次真是辛苦你们了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490170362V希望以后能够看到\n',
            '你们更加杰出的表现。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_874(): pass

    label('loc_874')

    Jump('loc_A5A')

    def _loc_877(): pass

    label('loc_877')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_9AB',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '#0490170391V#662F想必你们都已经听说了吧……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490170392V其实，我家被盗贼闯进过，\n',
            '传家宝也被盗走了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490170393V#664F但是，这件事只是件家务事。\n',
            '我必须以完成公务为先。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490170394V#660F所以，\n',
            '这件事就交给了秘书基尔巴特全权处理。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490170395V如果想了解有关情况的话，\n',
            '你们可以去问他。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A5A')

    def _loc_9AB(): pass

    label('loc_9AB')

    ChrTalk(
        0x00FE,
        (
            '#0490170396V#662F其实我家被盗贼闯进过。\n',
            '传家宝也被盗走了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490170397V#660F这件事我交给了\n',
            '秘书基尔巴特全权处理。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490170395V如果想了解有关情况的话，\n',
            '你们可以去问他。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A5A(): pass

    label('loc_A5A')

    Jump('loc_D98')

    def _loc_A5D(): pass

    label('loc_A5D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_B57',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B18',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '#0490050569V#660F对特蕾莎院长来说，\n',
            '这真是一场浩劫啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490050570V只要有我能帮上忙的，\n',
            '你们尽量来找我就行了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490050571V这是作为一市之长\n',
            '有义务去做的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B54')

    def _loc_B18(): pass

    label('loc_B18')

    ChrTalk(
        0x00FE,
        (
            '#0490050572V#660F对特蕾莎院长来说，\n',
            '这真是一场浩劫啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B54(): pass

    label('loc_B54')

    Jump('loc_D98')

    def _loc_B57(): pass

    label('loc_B57')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_C8D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C1F',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '#0490050063V#660F我想你们已经听说了，\n',
            '最近一段时间有一位\n',
            '王族的客人要来卢安。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490050064V就是今明两天，\n',
            '希望不要出什么事情……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490050065V请转告嘉恩\n',
            '让他做好万全的准备。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C8A')

    def _loc_C1F(): pass

    label('loc_C1F')

    ChrTalk(
        0x00FE,
        (
            '#0490050066V#660F最近一段时间有一位\n',
            '王族的客人要来卢安。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490050067V请转告嘉恩\n',
            '让他做好万全的准备。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C8A(): pass

    label('loc_C8A')

    Jump('loc_D98')

    def _loc_C8D(): pass

    label('loc_C8D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 4, 0x414)),
            Expr.Return,
        ),
        'loc_D98',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_D2D',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '#0490041214V#660F噢，原来是你们啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490041215V关于刚才那些家伙，\n',
            '市民都相继过来向我诉苦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490041216V看来我要采取一些行动了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D98')

    def _loc_D2D(): pass

    label('loc_D2D')

    ChrTalk(
        0x00FE,
        (
            '#0490041217V#660F关于刚才那些家伙，\n',
            '市民都相继过来向我诉苦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490041218V看来我要采取一些行动了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D98(): pass

    label('loc_D98')

    TalkEnd(0x0008)

    Return()

# id: 0x0005 offset: 0xD9C
@scena.Code('func_05_D9C')
def func_05_D9C():
    If(
        (
            (Expr.Eval, "OP_29(0x0020, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_F4E',
    )

    TalkBegin(0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_E98',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '#0480170404V#670F哟，各位游击士。\n',
            '这次干得很漂亮嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480170405V这下我就可以放心地\n',
            '去参加学院祭了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480170406V这样的机会是可遇不可求啊。\n',
            '能见到许多学长和学弟学妹。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480170407V我们每年也都\n',
            '期待着这个时候的到来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F48')

    def _loc_E98(): pass

    label('loc_E98')

    ChrTalk(
        0x00FE,
        (
            '#0480170408V#670F这下我就可以安心地\n',
            '去参加学院祭了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480170406V这样的机会是可遇不可求啊。\n',
            '能见到许多学长和学弟学妹。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480170407V我们每年也都\n',
            '期待着这个时候的到来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F48(): pass

    label('loc_F48')

    TalkEnd(0x0010)

    Jump('loc_14D7')

    def _loc_F4E(): pass

    label('loc_F4E')

    If(
        (
            (Expr.Eval, "OP_29(0x0020, 0x00, 0x04)"),
            (Expr.Eval, "OP_29(0x0020, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_125C',
    )

    TalkBegin(0x0010)

    ChrTalk(
        0x00FE,
        (
            '#0480170105V#670F呀，有什么疑问吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
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
        0,
        (
            TXT(0x00, '【确认卡片上的内容】\n'),
            TXT(0x01, '【没什么事】\n'),
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
        (0x00000000, 'loc_FFF'),
        (0x00000001, 'loc_1219'),
        (-1, 'loc_1219'),
    )

    def _loc_FFF(): pass

    label('loc_FFF')

    ChrTalk(
        0x00FE,
        (
            '#0480170106V#670F卡片的内容啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480170107V那你们再好好地确认一下吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            '#0170170049V',
            (TxtCtl.SetColor, 0x0),
            '『方才蚕食巢穴的乃是比野兽更狂野的兽中之兽。\n',
            '　\n',
            '　苍之光将黑暗中迷失的灵魂赞颂并传承。\n',
            '　让残存之耀得以救赎，而我即为解放者。\n',
            '　\n',
            '　啊，探寻者们。\n',
            '　如女神一般直视真实，抛弃虚伪吧。\n',
            '　\n',
            TxtCtl.Enter,
            '#0170170050V　前往耸立于此村落中的\n',
            '　三眼巨人所在之处吧。\n',
            '　如是，探寻者们，\n',
            '　汝等将至苍之光所在。\n',
            '　　　　　　　　　　　　　　　　　　　　怪盗Ｂ』',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '#0480170110V#670F那调查的事情\n',
            '就拜托你们继续进行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1256')

    def _loc_1219(): pass

    label('loc_1219')

    ChrTalk(
        0x00FE,
        (
            '#0480170110V#670F那调查的事情\n',
            '就拜托你们继续进行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1256')

    def _loc_1256(): pass

    label('loc_1256')

    TalkEnd(0x0010)

    Jump('loc_14D7')

    def _loc_125C(): pass

    label('loc_125C')

    If(
        (
            (Expr.Eval, "OP_29(0x0020, 0x00, 0x04)"),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x0020, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_127A',
    )

    Call(1, 0x0000)

    Jump('loc_14D7')

    def _loc_127A(): pass

    label('loc_127A')

    TalkBegin(0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_137F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1315',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '#0480050573V#671F找到犯人了吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480050574V无论如何，\n',
            '也不能让那些小流氓\n',
            '在街头横行霸道。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480050575V问题真是堆成山啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_137C')

    def _loc_1315(): pass

    label('loc_1315')

    ChrTalk(
        0x00FE,
        (
            '#0480050576V#670F无论如何，\n',
            '也不能让那些小流氓\n',
            '在街头横行霸道。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480050577V问题真是堆成山啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_137C(): pass

    label('loc_137C')

    Jump('loc_14D4')

    def _loc_137F(): pass

    label('loc_137F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_1404',
    )

    ChrTalk(
        0x00FE,
        (
            '#0480050068V#670F非常抱歉，卢安市里面\n',
            '的确有一些不像样的家伙。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480050069V说不定以后还要\n',
            '麻烦你们帮忙解决他们的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_14D4')

    def _loc_1404(): pass

    label('loc_1404')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 4, 0x414)),
            Expr.Return,
        ),
        'loc_14D4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1494',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '#0480041219V#671F真是的，\n',
            '渡鸦帮那些小混混老是在惹麻烦……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480041220V放任他们不管的话，\n',
            '恐怕会给城市带来不良影响。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_14D4')

    def _loc_1494(): pass

    label('loc_1494')

    ChrTalk(
        0x00FE,
        (
            '#0480041221V#671F真是的，\n',
            '渡鸦帮那些小混混老是在惹麻烦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_14D4(): pass

    label('loc_14D4')

    TalkEnd(0x0010)

    def _loc_14D7(): pass

    label('loc_14D7')

    Return()

# id: 0x0006 offset: 0x14D8
@scena.Code('func_06_14D8')
def func_06_14D8():
    TalkBegin(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_1CC6',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0020, 0x00, 0x04)"),
            (Expr.Eval, "OP_29(0x0020, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0020, 0x01, 0x0200)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1BEF',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0020, 0x01, 0x0400)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1B8A',
    )

    EventBegin(0x00)
    Fade(1000)
    ChrSetPos(0x0101, -760, 0, -1810, 0)
    ChrSetPos(0x0102, -1660, -250, -2470, 0)
    ChrSetPos(0x0105, -660, -500, -2740, 0)
    ChrTurnDirection(0x000C, 0x0101, 0)
    ChrTurnDirection(0x000D, 0x0101, 0)
    OP_4A(0x000D, 255)
    OP_28(0x0020, 0x01, 0x0400)
    OP_28(0x0020, 0x01, 0x0800)
    CameraMove(-1090, -250, -2370, 0)
    OP_0D()
    Sleep(100)

    OP_62(0x000C, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    ChrTalk(
        0x000C,
        (
            '啊，各位。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '请你们看看。\n',
            '烛台已经回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirectionByPos(0x0101, 10, 3910, 400)
    Sleep(100)

    ChrTurnDirectionByPos(0x0105, 10, 3910, 400)
    ChrTurnDirectionByPos(0x0102, 10, 3910, 400)

    ChrTalk(
        0x0101,
        (
            '#501F啊，真的呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '是谁找它回来的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '不，不是的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '不久之前\n',
            '它自己回来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '真是奇怪得很……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#505F……这么说，\n',
            '是犯人主动归还的了？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '犯人并不是为了钱，\n',
            '这点我明白是明白……\n',
            '可犯人的动机究竟是什么呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_16D4')
    def lambda_16D4():
        ChrTurnDirection(0x0102, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_16D4)

    @scena.Lambda('lambda_16E2')
    def lambda_16E2():
        ChrTurnDirection(0x0105, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_16E2)

    ChrTurnDirection(0x0101, 0x000C, 400)

    ChrTalk(
        0x0102,
        (
            '#012F是什么时候回来的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000C, 0x0102, 400)

    ChrTalk(
        0x000C,
        (
            '啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '这个……嗯……\n',
            '是市长大人被逮捕的后一天。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#013F……是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_176D')
    def lambda_176D():
        ChrTurnDirection(0x0105, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_176D)

    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#501F是怎么回事呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_179B')
    def lambda_179B():
        ChrTurnDirection(0x000C, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_179B)

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#012F嗯…………\n',
            '我是这么推测的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '犯人的目的并非是烛台，\n',
            '而是针对市长本人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '如果不是这样，\n',
            '那就没有理由要归还烛台了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#002F也就是说，\n',
            '是为了揭穿市长的恶行吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '那么犯人直接去告发\n',
            '不就行了吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '为什么还要盗取烛台后\n',
            '留下一张张卡片，\n',
            '绕了那么大一个圈子呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#013F也许不是为了揭露恶行……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '可能是……\n',
            '为了好玩吧，我是这么想的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#004F……………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#012F犯人肯定是一开始就知道\n',
            '市长的真面目的。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '一旦盗取了烛台，\n',
            '我们游击士就会在\n',
            '市长官邸里仔细调查。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '对戴尔蒙市长来说，\n',
            '他可能一早明白犯人的用意。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '他知道喂养魔兽的房间\n',
            '有被发现的危险。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#505F……唉，\n',
            '可是我们当时立场不够坚定，\n',
            '并没有那么做。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#003F是啊…………\n',
            '不过，市长他们当时\n',
            '可能吓得冒了一身冷汗哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '不愿让我们调查屋子，\n',
            '反而更加可疑……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#002F……犯人大概在某处\n',
            '看着市长的反应偷偷地冷笑吧？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F大概吧。\n',
            '不出预料的话，应该就是这样的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '因为如果不这么想的话，\n',
            '这件事就没法解释了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1B20')
    def lambda_1B20():
        ChrTurnDirection(0x0105, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_1B20)

    ChrSetDirection(0x0101, 0, 400)

    ChrTalk(
        0x0101,
        (
            '#505F…………怪盗Ｂ。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '真是一个来历不明的家伙呢。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Sleep(50)

    EventEnd(0x04)
    ChrSetDirection(0x000C, 90, 0)
    ChrSetDirection(0x000D, 270, 0)
    OP_4B(0x000D, 255)

    Jump('loc_1BEC')

    def _loc_1B8A(): pass

    label('loc_1B8A')

    ChrTalk(
        0x00FE,
        (
            '盗走的烛台，\n',
            '不久之前自己回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '主人也已经被逮捕了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，\n',
            '不知道到底怎么回事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1BEC(): pass

    label('loc_1BEC')

    Jump('loc_1CC3')

    def _loc_1BEF(): pass

    label('loc_1BEF')

    If(
        (
            (Expr.Eval, "OP_29(0x0020, 0x00, 0x04)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1C88',
    )

    ChrTalk(
        0x00FE,
        (
            '这个烛台，\n',
            '不久之前还是被盗走的东西……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不知道什么时候\n',
            '就自己回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '主人也已经被逮捕了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，\n',
            '不知道到底怎么回事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1CC3')

    def _loc_1C88(): pass

    label('loc_1C88')

    ChrTalk(
        0x00FE,
        (
            '主人已经被逮捕了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这座房子究竟会\n',
            '何去何从呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1CC3(): pass

    label('loc_1CC3')

    Jump('loc_20E1')

    def _loc_1CC6(): pass

    label('loc_1CC6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_1D7B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1D3F',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '噜嗯噜嗯噜噜噜～⊙\n',
            '啦嗯啦～啊哈哈嗯⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊啊，那炯炯的琥珀色眼睛……\n',
            '好像要把人吸进去似的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D78')

    def _loc_1D3F(): pass

    label('loc_1D3F')

    ChrTalk(
        0x00FE,
        (
            '啊啊，那炯炯的琥珀色眼睛……\n',
            '好像要把人吸进去似的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1D78(): pass

    label('loc_1D78')

    Jump('loc_20E1')

    def _loc_1D7B(): pass

    label('loc_1D7B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_1E34',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1DF7',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '就在不久之前，\n',
            '从王都来了一位\n',
            '埃雷波尼亚帝国的大使。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最近，地位显赫的大人物\n',
            '经常到这里来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E31')

    def _loc_1DF7(): pass

    label('loc_1DF7')

    ChrTalk(
        0x00FE,
        (
            '就在不久之前，\n',
            '从王都来了一位\n',
            '埃雷波尼亚帝国的大使。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1E31(): pass

    label('loc_1E31')

    Jump('loc_20E1')

    def _loc_1E34(): pass

    label('loc_1E34')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_1EF2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1ED0',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '不久前，我在路上走的时候，\n',
            '有一位一头红发眼神锐利的\n',
            '游击士向我打招呼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000C, 0x00000000, 2000, 0x0A, 0x0B, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '哈……\n',
            '有野性的男人真棒。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1EEF')

    def _loc_1ED0(): pass

    label('loc_1ED0')

    ChrTalk(
        0x00FE,
        (
            '哈……\n',
            '有野性的男人真棒。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1EEF(): pass

    label('loc_1EEF')

    Jump('loc_20E1')

    def _loc_1EF2(): pass

    label('loc_1EF2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_2048',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1FC3',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '卢安的市长一职\n',
            '是通过选举产生的，\n',
            '但每次戴尔蒙家族的主人都会当选。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '光是作为前贵族，\n',
            '戴尔蒙家族的影响力\n',
            '就已经非常大了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这座市长官邸\n',
            '也是由戴尔蒙家族的主人\n',
            '代代掌管的别墅。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2045')

    def _loc_1FC3(): pass

    label('loc_1FC3')

    ChrTalk(
        0x00FE,
        (
            '卢安的市长一职\n',
            '是通过选举产生的，\n',
            '但每次戴尔蒙家族的主人都会当选。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '光是作为前贵族，\n',
            '戴尔蒙家族的影响力\n',
            '就已经非常大了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2045(): pass

    label('loc_2045')

    Jump('loc_20E1')

    def _loc_2048(): pass

    label('loc_2048')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 7, 0x417)),
            Expr.Return,
        ),
        'loc_2079',
    )

    ChrTalk(
        0x00FE,
        (
            '因为市长回来了，\n',
            '我正在准备茶水。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_20E1')

    def _loc_2079(): pass

    label('loc_2079')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 4, 0x414)),
            Expr.Return,
        ),
        'loc_20E1',
    )

    ChrTalk(
        0x00FE,
        (
            '真是非常抱歉，\n',
            '市长现在外出了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果有什么事的话，\n',
            '告诉我就可以了。\n',
            '我会转达给市长的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_20E1(): pass

    label('loc_20E1')

    TalkEnd(0x000C)

    Return()

# id: 0x0007 offset: 0x20E5
@scena.Code('func_07_20E5')
def func_07_20E5():
    TalkBegin(0x000D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_2269',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0020, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_21EF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_218C',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '竟然被卷进这样的事，\n',
            '真是的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '接下来的事就交给\n',
            '管家达里奥先生好了，\n',
            '我还是赶快去找其他的工作吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '去试试做导游吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_21EC')

    def _loc_218C(): pass

    label('loc_218C')

    ChrTalk(
        0x00FE,
        (
            '接下来的事就交给\n',
            '管家达里奥先生好了，\n',
            '我还是赶快去找其他的工作吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '去试试做导游吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_21EC(): pass

    label('loc_21EC')

    Jump('loc_2266')

    def _loc_21EF(): pass

    label('loc_21EF')

    ChrTalk(
        0x00FE,
        (
            '戴尔蒙家的传家宝什么的\n',
            '跟我们又没什么关系。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '与之相比，\n',
            '我对找工作的事情\n',
            '更在意一些。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '去试试做导游吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_2266(): pass

    label('loc_2266')

    Jump('loc_257D')

    def _loc_2269(): pass

    label('loc_2269')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_22AE',
    )

    ChrTalk(
        0x00FE,
        (
            '哎呀哎呀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '芙罗拉这孩子\n',
            '真的很容易胡思乱想呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_257D')

    def _loc_22AE(): pass

    label('loc_22AE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_2325',
    )

    ChrTalk(
        0x00FE,
        (
            '为什么那些有权有势的人\n',
            '没什么事情就从大老远的地方\n',
            '特地赶到这里来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '用导力通信\n',
            '明明就已经足够了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_257D')

    def _loc_2325(): pass

    label('loc_2325')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_23AE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2384',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '唉～\n',
            '芙罗拉这孩子又开始发病了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我真希望她能够\n',
            '多动手少说话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23AB')

    def _loc_2384(): pass

    label('loc_2384')

    ChrTalk(
        0x00FE,
        (
            '唉～\n',
            '芙罗拉这孩子又开始发病了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_23AB(): pass

    label('loc_23AB')

    Jump('loc_257D')

    def _loc_23AE(): pass

    label('loc_23AE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_24E8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2485',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '有很多人说市长的坏话，\n',
            '但这也是没办法的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为血统的原因而当上市长，\n',
            '这也是事实……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '市民会有不满，\n',
            '也是理所当然的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……但是，\n',
            '选出市长的也是市民们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这又该怎么说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24E5')

    def _loc_2485(): pass

    label('loc_2485')

    ChrTalk(
        0x00FE,
        (
            '有很多人说市长的坏话，\n',
            '但这也是没办法的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为血统的原因而当上市长，\n',
            '这也是事实……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_24E5(): pass

    label('loc_24E5')

    Jump('loc_257D')

    def _loc_24E8(): pass

    label('loc_24E8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 7, 0x417)),
            Expr.Return,
        ),
        'loc_254C',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然他本人好像\n',
            '完全没有发觉……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '基尔巴特是那种很容易\n',
            '被那些小流氓钻空子的性格。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_257D')

    def _loc_254C(): pass

    label('loc_254C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 4, 0x414)),
            Expr.Return,
        ),
        'loc_257D',
    )

    ChrTalk(
        0x00FE,
        (
            '我现在很忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '能不能不要来烦我？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_257D(): pass

    label('loc_257D')

    TalkEnd(0x000D)

    Return()

# id: 0x0008 offset: 0x2581
@scena.Code('func_08_2581')
def func_08_2581():
    TalkBegin(0x0012)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_25F3',
    )

    ChrTalk(
        0x00FE,
        (
            '我在戴尔蒙家工作了三十多年……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '长年来为卢安作贡献的这个家族，\n',
            '却以这种形式拉下了大幕………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2861')

    def _loc_25F3(): pass

    label('loc_25F3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_2647',
    )

    ChrTalk(
        0x00FE,
        (
            '请问，\n',
            '你们有什么事情？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在我家主人\n',
            '与杜南公爵大人谈得正欢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2861')

    def _loc_2647(): pass

    label('loc_2647')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_2725',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0020, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_26C1',
    )

    ChrTalk(
        0x00FE,
        (
            '哦，各位游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们顺利地\n',
            '把烛台找了回来啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我代表这里的员工\n',
            '向你们表示深深的感谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2722')

    def _loc_26C1(): pass

    label('loc_26C1')

    ChrTalk(
        0x00FE,
        (
            '没想到传家宝烛台\n',
            '竟然被盗了…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '门窗都应该关严了。\n',
            '那个小偷到底是\n',
            '从哪里进来的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2722(): pass

    label('loc_2722')

    Jump('loc_2861')

    def _loc_2725(): pass

    label('loc_2725')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_2789',
    )

    ChrTalk(
        0x00FE,
        (
            '这个烛台是\n',
            '戴尔蒙家族的传家之宝。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为它的价值非常高，\n',
            '我打理它的时候非常紧张。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2861')

    def _loc_2789(): pass

    label('loc_2789')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_27F6',
    )

    ChrTalk(
        0x00FE,
        (
            '主人对于家庭名望\n',
            '非常地重视。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然已经不再是领主了，\n',
            '但这也是戴尔蒙家族\n',
            '流传下来的义务。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2861')

    def _loc_27F6(): pass

    label('loc_27F6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 7, 0x417)),
            Expr.Return,
        ),
        'loc_2825',
    )

    ChrTalk(
        0x00FE,
        (
            '主人他最近\n',
            '总是为很多事情操劳。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2861')

    def _loc_2825(): pass

    label('loc_2825')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 4, 0x414)),
            Expr.Return,
        ),
        'loc_2861',
    )

    ChrTalk(
        0x00FE,
        (
            '是客人吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是非常抱歉，\n',
            '主人现在外出了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2861(): pass

    label('loc_2861')

    TalkEnd(0x0012)

    Return()

# id: 0x0009 offset: 0x2865
@scena.Code('func_09_2865')
def func_09_2865():
    TalkBegin(0x0013)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_28D0',
    )

    ChrTalk(
        0x00FE,
        (
            '我一直以为市长是个伟大的人，\n',
            '所以才为他做饭到现在。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '结果却变成这样，\n',
            '真是太遗憾了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A9C')

    def _loc_28D0(): pass

    label('loc_28D0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_292C',
    )

    ChrTalk(
        0x00FE,
        (
            '基尔巴特那小子\n',
            '到底跑到哪里去了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '听说今天会有一个\n',
            '很重要的客人来访……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A9C')

    def _loc_292C(): pass

    label('loc_292C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_2991',
    )

    ChrTalk(
        0x00FE,
        (
            '说起东方的刀具，\n',
            '做得还真精致啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最近在厨师之间，\n',
            '东方产的菜刀\n',
            '引起了不少关注。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A9C')

    def _loc_2991(): pass

    label('loc_2991')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_29ED',
    )

    ChrTalk(
        0x00FE,
        (
            '午餐马上就做好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天的菜是浸泡烤鱼面\n',
            '和蒜香吐司，\n',
            '还有香草烤土鸡腿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A9C')

    def _loc_29ED(): pass

    label('loc_29ED')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_2A58',
    )

    ChrTalk(
        0x00FE,
        (
            '市长小的时候\n',
            '非常喜欢挑食，\n',
            '不过最近他什么都吃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大概，\n',
            '这也是作为市长的干劲之一吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A9C')

    def _loc_2A58(): pass

    label('loc_2A58')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 4, 0x414)),
            Expr.Return,
        ),
        'loc_2A9C',
    )

    ChrTalk(
        0x00FE,
        (
            '厨具就是厨师的生命。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '保养它们的时候\n',
            '必须非常细心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2A9C(): pass

    label('loc_2A9C')

    TalkEnd(0x0013)

    Return()

# id: 0x000A offset: 0x2AA0
@scena.Code('func_0A_2AA0')
def func_0A_2AA0():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '『苍耀之灯火』\n',
            '　被誉为早期导力艺术\n',
            '　的颠峰作品。\n',
            '　导力革命之后，卢安\n',
            '　市民将其赠与了为城\n',
            '　市的发展鞠躬尽瘁的\n',
            '　戴尔蒙家族。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x000B offset: 0x2B53
@scena.Code('func_0B_2B53')
def func_0B_2B53():
    EventBegin(0x00)
    CameraMove(-6240, 0, 6040, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    ChrSetPos(0x000C, -5830, 0, 5580, 315)
    ChrSetPos(0x0101, -600, -500, -3890, 0)
    ChrSetPos(0x0102, 950, -500, -3720, 315)
    ChrSetPos(0x0105, 570, -500, -5040, 0)
    FadeIn(1000, 0)
    OP_0D()
    OP_4A(0x000C, 255)
    OP_62(0x000C, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x000C, 0x0101, 400)

    @scena.Lambda('lambda_2C0D')
    def lambda_2C0D():
        CameraMove(-760, -500, -2510, 3000)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_2C0D)

    ChrWalkTo(0x000C, -580, 0, -1700, 3000, 0x00)
    ChrTurnDirection(0x000C, 0x0101, 400)
    WaitForThreadExit(0x000C, 0x0001)

    ChrTalk(
        0x000C,
        (
            '#1670061443V欢迎光临卢安市长官邸。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1670061444V非常抱歉，\n',
            '市长他现在正在会客……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1670061445V能请几位改日再来吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061446V#009F哎～～！\n',
            '等一下嘛……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020061447V#015F市长正在会见的那位客人，\n',
            '其实我们也认识。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020061448V是杜南公爵吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0105, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010061449V#004F哎……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000C, 0x0102, 400)

    ChrTalk(
        0x000C,
        (
            '#1670061450V是的，正是公爵大人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1670061451V……难道各位\n',
            '也是受市长邀请前来的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020061452V#010F是的，是市长亲自请我们来的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020061453V请问我们可以进去吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1670061454V仔细一看，各位原来是游击士啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1670061455V既然是这样，\n',
            '那就请各位进来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1670061456V市长和公爵大人\n',
            '正在二楼的大厅里谈话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020061457V#019F好的。\n',
            '谢谢你的热情接待。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1670061458V………………（脸红）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1670061459V对、对了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1670061460V既然多了几位客人，\n',
            '那我得去准备一下茶点才行……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1670061461V那我先失陪了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000C, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrSetDirection(0x000C, 90, 400)

    @scena.Lambda('lambda_2FDB')
    def lambda_2FDB():
        CameraMove(1390, 0, -20, 3000)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_2FDB)

    @scena.Lambda('lambda_2FF3')
    def lambda_2FF3():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2FF3)

    @scena.Lambda('lambda_3001')
    def lambda_3001():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_3001)

    @scena.Lambda('lambda_300F')
    def lambda_300F():
        ChrTurnDirection(0x00FE, 0x000C, 400)
        Yield()

        Jump('lambda_300F')

    DispatchAsync2(0x0102, 0x0001, lambda_300F)

    ChrWalkTo(0x000C, 5170, 0, 1180, 3000, 0x00)
    TerminateThread(0x0102, 0xFF)
    ChrSetFlags(0x000C, 0x0004)
    ChrWalkTo(0x000C, 11760, 0, 670, 3000, 0x00)
    ChrClearFlags(0x000C, 0x0004)
    ChrSetPos(0x000C, 33500, 0, 24550, 270)
    WaitForThreadExit(0x000C, 0x0001)
    CameraMove(-630, -500, -2970, 2000)

    ChrTalk(
        0x0101,
        (
            '#0010061462V#004F#1P……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060061463V#044F……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0102, 225, 400)

    ChrTalk(
        0x0102,
        (
            '#0020061464V#014F#2P咦？怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061465V#007F#1P没什么～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060061466V#045F这、这个嘛……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060061467V#040F对了，你怎么知道\n',
            '来的客人就是公爵大人？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020061468V#010F#2P啊，我也只是碰碰运气。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020061469V昨晚基尔巴特不是说过\n',
            '别墅是准备卖给国内外的富豪吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020061470V我想像杜南公爵这样的人，\n',
            '正是市长最理想的主顾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060061471V#044F的确是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061472V#009F#1P真是的，一肚子鬼点子。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010061473V居然信口开河说\n',
            '是市长邀请我们来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020061474V#011F#2P这可不是信口开河哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020061475V我们第一次见到戴尔蒙市长的时候，\n',
            '他不是这样说过吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020061476V要是渡鸦帮的人再给我们惹麻烦的话，\n',
            '可以不必客气，尽管来这里找他。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061477V#004F#1P啊……这样吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060061478V#048F呵呵……\n',
            '那的确就是应邀前来的了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020061479V#019F#2P没错，就是这样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020061480V#010F那么，就不必客气了，\n',
            '我们直接去二楼的大厅吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)
    OP_4B(0x000C, 255)

    Return()

# id: 0x000C offset: 0x3441
@scena.Code('func_0C_3441')
def func_0C_3441():
    EventBegin(0x00)
    CameraMove(-2510, 0, 40990, 0)
    OP_67(0, 6150, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    ChrClearFlags(0x0014, 0x0080)
    ChrClearFlags(0x0015, 0x0080)
    ChrClearFlags(0x0016, 0x0080)
    ChrSetPos(0x0014, 20, 700, 39500, 0)
    ChrSetPos(0x0015, -900, 700, 38600, 0)
    ChrSetPos(0x0016, -150, 850, 38740, 0)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0102, 0x0080)
    ChrSetFlags(0x0105, 0x0080)
    ChrSetPos(0x0101, 11020, 0, 36640, 270)
    ChrSetPos(0x0102, 11020, 0, 36640, 270)
    ChrSetPos(0x0105, 11020, 0, 36640, 270)
    ChrSetFlags(0x000A, 0x0004)
    ChrSetFlags(0x0008, 0x0004)
    OP_4A(0x0008, 255)
    ChrSetPos(0x000A, -50, 200, 40550, 180)
    ChrSetPos(0x0008, -2000, 0, 38810, 90)
    ChrSetPos(0x000B, 950, 0, 41760, 180)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x000A,
        (
            '#0640061481V#227F#2P嗝……\n',
            '嗯，听起来很不错嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640061482V这卢安的确是\n',
            '购置别墅的绝佳地方啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640061483V在这里住了一阵后深有体会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0490061484V#661F#1P呵呵，的确如此。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490061485V在这些高级别墅区中，\n',
            '我们计划为公爵大人您\n',
            '定制了一套位置极佳的豪华大屋。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490061486V相信您一定会喜欢的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0640061487V#227F#2P呵～呵～呵……\n',
            '市长还真是善解人意啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640061488V#483F很好，价格方面无所谓。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640061489V你尽管去准备一套\n',
            '配得起下任国王的豪宅就可以了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640061490V嗯，我想想……\n',
            '最起码要达到这座官邸的水准。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0660061491V#722F殿下，请稍等一下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660061492V不跟女王陛下商量\n',
            '就擅自动用如此大额的巨款……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x000A, 1)

    ChrTalk(
        0x000A,
        (
            '#0640061493V#482F#2P闭嘴，菲利普！\n',
            '我可是下任国王！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640061494V为自己买房子也是理所当然的吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0490061495V#661F#1P哎呀哎呀，\n',
            '我就知道公爵大人一定有这眼光的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490061496V稍后我会准备合同。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490061497V在那之前，我们再干一杯吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x000A, 0)

    ChrTalk(
        0x000A,
        (
            '#0640061498V#481F#2P哦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061499V#1P您好～\n',
            '我们是游击士协会的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x000B, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_3972')
    def lambda_3972():
        CameraMove(-380, 0, 39240, 2000)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_3972)

    CreateThread(0x0101, 0x01, 0x00, func_0E_7818)
    CreateThread(0x0102, 0x01, 0x00, func_0F_784D)
    CreateThread(0x0105, 0x01, 0x00, func_10_7887)
    ChrSetSubChip(0x000A, 1)
    ChrSetDirection(0x000B, 135, 400)
    WaitForThreadExit(0x0105, 0x0001)

    ChrTalk(
        0x0008,
        (
            '#0490061500V#663F你们是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0640061501V#480F嗝……\n',
            '你们是什么人？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640061502V我好像在哪见过你们……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0660061503V#721F哦哦，是上次的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061504V#006F您好，管家先生。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010061505V我们今天来\n',
            '是想向市长先生请教一件事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0490061506V#662F这种行为实在令人困扰……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490061507V身为协会的游击士，\n',
            '我想你们应该很清楚什么叫礼数吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490061508V我和公爵大人在谈很重要的事情，\n',
            '所以麻烦你们改天再来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020061509V#015F因为事出紧急，\n',
            '如有失礼之处还请市长多多见谅。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020061510V这件事其实是，\n',
            '我们终于找到纵火事件的犯人了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0490061511V#664F是这件事吗……那就没办法了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490061512V#661F公爵大人，\n',
            '我可以离开片刻吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x000A, 0)
    Sleep(300)

    ChrTalk(
        0x000A,
        (
            '#0640061513V#227F嗝……\n',
            '不，在这里说就好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640061514V我也很想听听是什么事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0490061515V#663F可、可是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061516V#006F这样不是更好嘛⊙\n',
            '连公爵大人都这么说了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010061517V反正又不是什么见不得人的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x000A, 1)

    ChrTalk(
        0x0008,
        (
            '#0490061518V#662F算了，反正又不是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490061519V说起来，\n',
            '特蕾莎院长他们昨晚又受到了袭击。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490061520V是和纵火事件的同一批犯人所做的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020061521V#012F这种可能性很高。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020061522V不过非常遗憾，\n',
            '一部分的犯案人员逃掉了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0490061523V#662F是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490061524V虽然没全部捉拿归案，\n',
            '不过能找到犯人就已经很不错了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490061525V那么犯人究竟是谁？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061526V#006F嗯，这个嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010061527V这些犯人究竟是谁，\n',
            '我想市长先生也应该心里有底了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0490061528V#664F是吗……那真是遗憾。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490061529V我本想他们总有一天\n',
            '会浪子回头痛改前非的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490061530V看来……\n',
            '这也只是我的一厢情愿罢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061531V#004F咦？市长先生。\n',
            '您这是在说谁啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0490061532V#661F谁？这还用问吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490061533V当然是在说\n',
            '『渡鸦帮』的那些流氓了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490061534V我听说他们从昨晚起就一直行踪不明，\n',
            '当然真正的犯人就是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020061535V#015F很遗憾……\n',
            '他们并不是犯人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020061536V在这次的事件中，\n',
            '他们甚至应该说是受害者才对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0490061537V#663F什、什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061538V#502F这次事件的犯人，就是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
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
        0,
        (
            TXT(0x00, '【戴尔蒙市长】\n'),
            TXT(0x01, '【杜南公爵】\n'),
            TXT(0x02, '【秘书基尔巴特】\n'),
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
        (0x00000000, 'loc_41C6'),
        (0x00000001, 'loc_4214'),
        (0x00000002, 'loc_43FB'),
        (-1, 'loc_4494'),
    )

    def _loc_41C6(): pass

    label('loc_41C6')

    OP_20(0x000003E8)
    Sleep(1000)

    PlayBGM(81)

    ChrTalk(
        0x0101,
        (
            '#0010061539V#005F#3S就是你，戴尔蒙市长！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    Jump('loc_4494')

    def _loc_4214(): pass

    label('loc_4214')

    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010061540V#005F#3S就是你，杜南公爵！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    OP_9E(0x000A, 15, 0, 300, 4000)
    OP_62(0x000A, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x000A,
        (
            '#0640061541V#484F什、什么！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0660061542V#721F是、是不是\n',
            '什么地方弄错了！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020061543V#018F艾丝蒂尔……\n',
            '你在说什么啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0101, 400)

    ChrTalk(
        0x0105,
        (
            '#0060061544V#045F艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061545V#008F嘿嘿，不好意思说错了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010061546V#502F……这次事件的犯人，那就是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_4397')
    def lambda_4397():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_4397)

    @scena.Lambda('lambda_43A5')
    def lambda_43A5():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_43A5)

    OP_20(0x000003E8)
    Sleep(1000)

    PlayBGM(81)

    ChrTalk(
        0x0101,
        (
            '#0010061547V#005F#3S就是你，戴尔蒙市长！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    Jump('loc_4494')

    def _loc_43FB(): pass

    label('loc_43FB')

    ChrTalk(
        0x0101,
        (
            '#0010061548V#002F市长秘书基尔巴特！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010061549V而其幕后主使就是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000003E8)
    Sleep(1000)

    PlayBGM(81)

    ChrTalk(
        0x0101,
        (
            '#0010061550V#005F#3S就是你，戴尔蒙市长！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    Jump('loc_4494')

    def _loc_4494(): pass

    label('loc_4494')

    ChrTalk(
        0x0008,
        (
            '#0490061551V#663F！！！',
            TxtCtl.Enter,
        ),
    )

    OP_9E(0x0008, 15, 0, 300, 4000)
    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020061552V#012F你的秘书基尔巴特\n',
            '已经在昨晚当场被捕了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020061553V而且还做出了\n',
            '受戴尔蒙市长指使，\n',
            '雇凶烧毁孤儿院并抢夺捐款的证言。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020061554V这证言应该没有错吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0490061555V#665F胡、胡说八道！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490061556V我才不认识那帮黑衣家伙！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061557V#006F哎～？奇怪了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010061558V我们刚刚可完全\n',
            '没提到什么黑衣家伙啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0490061559V#666F呜……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490061560V我不知道！我什么都不知道！\n',
            '一切都是那个秘书擅自做的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061561V#007F大叔你还真是厚颜无耻啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020061562V#012F因为孤儿院会妨碍到\n',
            '市长你建造高级别墅区的计划。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020061563V到了现在，你还想为自己开脱罪行吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0490061564V#665F太纠缠不休了，你们！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490061565V的确，我从很早之前\n',
            '就开始计划别墅区的开发！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490061566V但是，那只不过是\n',
            '卢安地区今后发展的其中一环！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490061567V难道我为了完成区区一个建筑计划，\n',
            '就会不惜犯罪来急着完成它！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061568V#004F这、这个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0009, 11020, 0, 36640, 270)

    NpcTalk(
        0x0009,
        '男人的声音',
        (
            '#0270061569V#1P……那是因为\n',
            '你欠下了庞大的债务吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0102, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0105, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x000A, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x000B, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    @scena.Lambda('lambda_48F7')
    def lambda_48F7():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_48F7)

    @scena.Lambda('lambda_4905')
    def lambda_4905():
        ChrSetDirection(0x00FE, 135, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4905)

    @scena.Lambda('lambda_4913')
    def lambda_4913():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_4913')

    DispatchAsync2(0x0102, 0x0001, lambda_4913)

    @scena.Lambda('lambda_4924')
    def lambda_4924():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_4924')

    DispatchAsync2(0x0105, 0x0001, lambda_4924)

    Sleep(200)

    @scena.Lambda('lambda_493A')
    def lambda_493A():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_493A')

    DispatchAsync2(0x0101, 0x0001, lambda_493A)

    ChrSetFlags(0x0009, 0x0004)
    ChrWalkTo(0x0009, 3110, 0, 36790, 3000, 0x00)
    ChrClearFlags(0x0009, 0x0004)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0105, 0xFF)

    ChrTalk(
        0x0101,
        (
            '#0010061570V#004F奈、奈尔！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020061571V#014F为什么会在这里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0270061572V#141F哟，我来这里\n',
            '是想采访戴尔蒙市长的。\n',
            '刚好在外面看见你们走了进来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270061573V我估计大概是有什么事，\n',
            '才刚进来就见到了这种情况。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270061574V#147F哎呀～\n',
            '我从头到尾都听见了哦㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0490061575V#663F你、你是什么人！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0270061576V#140F啊，我是《利贝尔通讯》的记者，\n',
            '奈尔·班兹。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270061577V其实是这样的。\n',
            '我这段时间一直在\n',
            '调查卢安市最近的财政情况……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270061578V戴尔蒙市长，您……\n',
            '透支了卢安市的预算吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_4B8F')
    def lambda_4B8F():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_4B8F)

    @scena.Lambda('lambda_4B9D')
    def lambda_4B9D():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4B9D)

    @scena.Lambda('lambda_4BAB')
    def lambda_4BAB():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_4BAB)

    @scena.Lambda('lambda_4BB9')
    def lambda_4BB9():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_4BB9)

    ChrSetSubChip(0x000A, 0)

    ChrTalk(
        0x0008,
        (
            '#0490061579V#663F……这、这个……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490061580V这是用作建造别墅区的资金……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0270061581V#142F这可说不通。\n',
            '施工还完全没有开始呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270061582V我觉得有点不寻常，\n',
            '就去王都的飞艇公社\n',
            '调查了一下你乘坐的飞艇的记录。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270061583V结果，大～吃一惊啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270061584V就在一年之前，\n',
            '你去了共和国好几次是吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0490061585V#663F……只、只是旅游性质……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0270061586V#145F这是表面理由吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270061587V真正的理由是……\n',
            '你在那里进行了投机买卖，\n',
            '并且落得损失惨重的结果对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0490061588V#666F！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061589V#505F那个……投机买卖是什么啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060061590V#043F就是利用市场的价格差\n',
            '来赚钱的交易行当。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060061591V比如趁低价时购入某一商品，\n',
            '然后再趁高价时将商品抛出……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061592V#501F哦，原来是这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010061593V那么，这个市长\n',
            '到底损失了多少钱呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0270061594V#140F就我在共和国的\n',
            '记者朋友调查所知……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270061595V大约也有一亿米拉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0105, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010061596V#005F#3S一、一、一亿米拉～！！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020061597V#015F是捐款数额的一百倍啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020061598V的确，为了偿还这巨额借款，\n',
            '甘心染指犯罪也不足为奇了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0640061599V#481F嗝，一亿啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640061600V#483F虽然我也是挥金如土，\n',
            '但没想到你比我还厉害啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0490061601V#666F呜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061602V#007F这种事也要拿来比啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0270061603V#145F总之，因为这个原因……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270061604V你为了偿还巨额借款\n',
            '而动用了卢安市的预算，\n',
            '但这也只是拆东墙补西墙罢了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270061605V我还在猜你下一步会怎么做的时候，\n',
            '没想到你居然不惜放火抢劫\n',
            '来建造什么高级别墅区。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270061606V#141F怎么说呢……\n',
            '还真是走投无路了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0490061607V#664F…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490061608V哼，你有证据吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490061609V#665F你敢把这种臆测当作新闻写出去试试。\n',
            '我一定会告你侵害现任市长的名誉！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0270061610V#143F哎呀，翻脸了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0490061611V#665F你们几个也一样！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490061612V游击士协会根本就没权\n',
            '逮捕身为市长的我！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490061613V你们，马上给我出去！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061614V#009F哼，果然使出了这一招。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020061615V#012F看来你对自己身为市长的权力\n',
            '倒是知道得很清楚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060061616V#049F……………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060061617V市长，有一点……\n',
            '可以请你回答一下吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0490061618V#665F你又怎么会在这里！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490061619V身为王立学院的学生，\n',
            '怎么能跟这些人混在一起……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490061620V快点回学院去！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060061621V#042F………………………………',
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
            '科洛丝以凛然的眼神\n',
            '直视着恼火中的戴尔蒙市长。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0008,
        (
            '#0490061622V#663F呜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060061623V#043F为什么你不以自己的财产\n',
            '来偿还投机欠下借款呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060061624V一亿米拉的确是很大的数目……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060061625V但是以戴尔蒙家族的财力，\n',
            '我想应该还是可以偿还的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060061626V比如说，\n',
            '这幢大宅就已经值一亿米拉了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0490061627V#665F说、说什么蠢话……！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490061628V这幢房子，可是我先祖代代相传的，\n',
            '也是我戴尔蒙家族的骄傲！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490061629V怎么能够拿去卖掉！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060061630V#049F其实孤儿院也是一样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060061631V对我和老师他们来说，\n',
            '那是个充满珍贵回忆的地方……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060061632V谁都没有权利\n',
            '去破坏这一份回忆……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060061633V#042F而为什么你却……\n',
            '能够做出那种事情来？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0490061634V#668F别、别把那间破烂的小屋\n',
            '和我这幢大宅混为一谈！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060061635V#047F你终究还是只在乎你自己……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060061636V你仅仅只在乎\n',
            '作为卢安市长的自己，\n',
            '和作为戴尔蒙家族主人的自己而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060061637V#049F真是可怜的人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_9E(0x0008, 15, 0, 300, 4000)

    ChrTalk(
        0x0008,
        (
            '#0490061638V#668F……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_9E(0x0008, 15, 0, 400, 5000)

    ChrTalk(
        0x0008,
        (
            '#0490061639V#667F……哼哼……哼哼哼哼哼………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490061640V说得真好啊，小丫头……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490061641V……既然事已至此，\n',
            '那我也不用顾虑什么后果了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(500)
    ChrSetPos(0x0008, -2230, 0, 39700, 90)
    ChrSetSubChip(0x000A, 2)
    OP_0D()
    ChrSetDirection(0x0008, 270, 400)

    @scena.Lambda('lambda_595E')
    def lambda_595E():
        CameraMove(-2940, 0, 40120, 2000)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_595E)

    ChrWalkTo(0x0008, -7440, 0, 40630, 3000, 0x00)
    Sleep(500)

    OP_20(0x000005DC)
    OP_72(0x0010, 0x0800)
    PlaySE(112, 0x00, 0x64)
    OP_72(0x0010, 0x0010)
    OP_70(0x0010, 300)
    Sleep(1500)

    ChrTalk(
        0x0008,
        (
            '#0490061642V#667F#3S飞球，野马！#2S',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490061643V#3S进餐的时间到了，出来吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0008, -7470, 0, 39130, 3000, 0x00)
    ChrTurnDirection(0x0008, 0x0101, 400)
    OP_73(0x0010)

    ChrTalk(
        0x0101,
        (
            '#0010061644V#580F#1P什、什么呀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020061645V#016F#1P是魔兽的气息……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_5A73')
    def lambda_5A73():
        CameraMove(-500, 0, 39570, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_5A73)

    @scena.Lambda('lambda_5A8B')
    def lambda_5A8B():
        OP_6C(291000, 4000)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_5A8B)

    @scena.Lambda('lambda_5A9B')
    def lambda_5A9B():
        CameraSetDistance(3100, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_5A9B)

    PlayBGM(86)
    ChrClearFlags(0x000E, 0x0080)
    ChrSetChipByIndex(0x000E, 6)
    ChrSetPos(0x000E, -9610, 0, 41180, 0)
    ChrWalkTo(0x000E, -6990, 0, 40780, 4000, 0x00)
    ChrWalkTo(0x000E, -4170, 0, 41590, 4000, 0x00)
    ChrTurnDirection(0x000E, 0x0101, 400)
    ChrSetChipByIndex(0x000E, 5)
    CreateThread(0x000E, 0x01, 0x00, func_02_6E8)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetChipByIndex(0x000F, 21)
    ChrSetPos(0x000F, -9610, 0, 41180, 0)
    ChrWalkTo(0x000F, -6990, 0, 40780, 5000, 0x00)
    ChrWalkTo(0x000F, -4570, 0, 38980, 5000, 0x00)
    ChrTurnDirection(0x000F, 0x0101, 400)
    ChrSetChipByIndex(0x000F, 20)
    CreateThread(0x000F, 0x01, 0x00, func_02_6E8)

    ChrTalk(
        0x0009,
        (
            '#0270061646V#144F#3P这、这两只是什么东西啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x000A,
        (
            '#0640061647V#484F#4P魔、魔兽～！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640061648V#228F呜……呜呜呜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(524, 0x00, 0x64)
    ChrSetSubChip(0x000A, 3)
    Sleep(500)

    ChrTurnDirection(0x000B, 0x000A, 0)

    ChrTalk(
        0x000B,
        (
            '#0660061649V#721F公、公爵大人！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000B, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrWalkTo(0x000B, 780, 0, 40710, 3000, 0x00)
    ChrTurnDirection(0x000B, 0x000A, 0)

    ChrTalk(
        0x0105,
        (
            '#0060061650V#042F真是难以置信……\n',
            '你竟然私自饲养魔兽……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0490061651V#667F#6P哼哼哼……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490061652V只要把你们全部杀光，\n',
            '就没人知道这件事的真相了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490061653V放心吧。它们吃剩的部分，\n',
            '我会帮你们扔进河里去的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490061654V呀————哈、哈、哈！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_94(0x01, 0x0009, 0x00B4, 0x000003E8, 0x00000BB8, 0x00)

    ChrTalk(
        0x0009,
        (
            '#0270061655V#142F#3P这、这家伙疯了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_5D93')
    def lambda_5D93():
        CameraMove(1064, 0, 38330, 1000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_5D93)

    @scena.Lambda('lambda_5DAB')
    def lambda_5DAB():
        OP_6C(315000, 1000)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_5DAB)

    @scena.Lambda('lambda_5DBB')
    def lambda_5DBB():
        CameraSetDistance(2800, 800)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_5DBB)

    ChrSetChipByIndex(0x000E, 6)
    ChrJumpTo(0x000E, 550, 1500, 38470, 2000, 6000)
    PlaySE(236, 0x00, 0x64)
    Fade(500)
    ChrSetFlags(0x0016, 0x0080)
    ChrSetFlags(0x0014, 0x0080)
    ChrSetFlags(0x0015, 0x0080)
    ChrClearFlags(0x0017, 0x0080)
    ChrClearFlags(0x0018, 0x0080)
    ChrClearFlags(0x0019, 0x0080)
    ChrClearFlags(0x0019, 0x0100)
    ChrClearFlags(0x0017, 0x0100)
    ChrClearFlags(0x0018, 0x0100)
    ChrSetPos(0x0017, 320, 1000, 39500, 0)
    ChrSetPos(0x0018, -100, 1500, 38100, 0)
    ChrSetPos(0x0019, 700, 1450, 38140, 0)

    ExecExpressionWithValue(
        0x0019,
        0x2A,
        (
            (Expr.PushLong, 0x7530),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0019,
        0x2B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0019,
        0x2C,
        (
            (Expr.PushLong, 0xFFFDF0A8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0019,
        0x2D,
        (
            (Expr.PushLong, 0x3E8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0019,
        0x2E,
        (
            (Expr.PushLong, 0x3E8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0019,
        0x2F,
        (
            (Expr.PushLong, 0x3E8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0017,
        0x2A,
        (
            (Expr.PushLong, 0x7530),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0017,
        0x2B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0017,
        0x2C,
        (
            (Expr.PushLong, 0xFFFEA070),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0017,
        0x2D,
        (
            (Expr.PushLong, 0x3E8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0017,
        0x2E,
        (
            (Expr.PushLong, 0x3E8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0017,
        0x2F,
        (
            (Expr.PushLong, 0x3E8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0018,
        0x2A,
        (
            (Expr.PushLong, 0x7530),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0018,
        0x2B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0018,
        0x2C,
        (
            (Expr.PushLong, 0xFFFD40E0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0018,
        0x2D,
        (
            (Expr.PushLong, 0x3E8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0018,
        0x2E,
        (
            (Expr.PushLong, 0x3E8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0018,
        0x2F,
        (
            (Expr.PushLong, 0x320),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_7C(0, 500, 3000, 100)
    ChrSetChipByIndex(0x000E, 5)
    CreateThread(0x000E, 0x01, 0x00, func_02_6E8)
    OP_0D()
    PlaySE(405, 0x00, 0x64)

    ChrTalk(
        0x000E,
        (
            '#4P嗷呜呜呜呜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x000F, 21)
    ChrJumpTo(0x000F, 440, 1500, 35970, 2000, 6000)
    PlaySE(236, 0x00, 0x64)
    OP_7C(0, 500, 3000, 100)
    ChrSetChipByIndex(0x000F, 20)
    CreateThread(0x000F, 0x01, 0x00, func_02_6E8)
    Sleep(500)

    PlaySE(405, 0x00, 0x64)

    ChrTalk(
        0x000F,
        (
            '#4P……嗷呜呜……………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_5FB6')
    def lambda_5FB6():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000001F4, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5FB6)

    Sleep(100)

    @scena.Lambda('lambda_5FD1')
    def lambda_5FD1():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000001F4, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_5FD1)

    Sleep(100)

    @scena.Lambda('lambda_5FEC')
    def lambda_5FEC():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000001F4, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_5FEC)

    WaitForThreadExit(0x0101, 0x0001)
    ChrSetFlags(0x0101, 0x1000)
    ChrSetChipByIndex(0x0101, 8)
    WaitForThreadExit(0x0102, 0x0001)
    ChrSetFlags(0x0102, 0x1000)
    ChrSetChipByIndex(0x0102, 9)
    WaitForThreadExit(0x0105, 0x0001)
    ChrSetFlags(0x0105, 0x1000)
    ChrSetChipByIndex(0x0105, 10)

    ChrTalk(
        0x0101,
        (
            '#0010061658V#002F没、没想到竟然要\n',
            '在这种房子里和魔兽战斗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020061659V#012F但这样一来，\n',
            '就可以将市长作为现行犯逮捕了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060061660V#047F虽然我和你们并无仇恨，\n',
            '但是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060061661V#046F如果你们想伤害大家的话，\n',
            '我决不会允许！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x000E, 7)
    ChrSetFlags(0x000E, 0x0020)

    ExecExpressionWithValue(
        0x000E,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_6138')
    def lambda_6138():
        ChrJumpTo(0x00FE, 4910, 0, 38450, 3000, 6000)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_6138)

    Sleep(150)

    ChrSetChipByIndex(0x000F, 22)
    ChrSetFlags(0x000F, 0x0020)

    ExecExpressionWithValue(
        0x000F,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_6170')
    def lambda_6170():
        ChrJumpTo(0x00FE, 4910, 0, 35450, 2500, 6000)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_6170)

    Sleep(400)

    Battle(0x00000394, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_61A6'),
        (-1, 'loc_61A9'),
    )

    def _loc_61A6(): pass

    label('loc_61A6')

    OP_B4(0x00)

    Return()

    def _loc_61A9(): pass

    label('loc_61A9')

    SetScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    NewScene('ED6_DT01/T2210._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000D offset: 0x61B6
@scena.Code('func_0D_61B6')
def func_0D_61B6():
    EventBegin(0x00)
    PlayBGM(81)
    OP_4A(0x0008, 255)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x000A, -50, 200, 40550, 180)
    ChrSetSubChip(0x000A, 3)
    ChrSetPos(0x000B, 780, 0, 40710, 225)
    ChrClearFlags(0x0017, 0x0080)
    ChrClearFlags(0x0018, 0x0080)
    ChrClearFlags(0x0019, 0x0080)
    ChrClearFlags(0x0019, 0x0100)
    ChrClearFlags(0x0017, 0x0100)
    ChrClearFlags(0x0018, 0x0100)
    ChrSetPos(0x0017, 320, 1000, 39500, 0)
    ChrSetPos(0x0018, -100, 1500, 38100, 0)
    ChrSetPos(0x0019, 700, 1450, 38140, 0)

    ExecExpressionWithValue(
        0x0019,
        0x2A,
        (
            (Expr.PushLong, 0x7530),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0019,
        0x2B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0019,
        0x2C,
        (
            (Expr.PushLong, 0xFFFDF0A8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0019,
        0x2D,
        (
            (Expr.PushLong, 0x3E8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0019,
        0x2E,
        (
            (Expr.PushLong, 0x3E8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0019,
        0x2F,
        (
            (Expr.PushLong, 0x3E8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0017,
        0x2A,
        (
            (Expr.PushLong, 0x7530),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0017,
        0x2B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0017,
        0x2C,
        (
            (Expr.PushLong, 0xFFFEA070),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0017,
        0x2D,
        (
            (Expr.PushLong, 0x3E8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0017,
        0x2E,
        (
            (Expr.PushLong, 0x3E8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0017,
        0x2F,
        (
            (Expr.PushLong, 0x3E8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0018,
        0x2A,
        (
            (Expr.PushLong, 0x7530),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0018,
        0x2B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0018,
        0x2C,
        (
            (Expr.PushLong, 0xFFFD40E0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0018,
        0x2D,
        (
            (Expr.PushLong, 0x3E8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0018,
        0x2E,
        (
            (Expr.PushLong, 0x3E8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0018,
        0x2F,
        (
            (Expr.PushLong, 0x320),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_6F(0x0010, 300)
    OP_72(0x0010, 0x0010)
    TerminateThread(0x000F, 0xFF)
    TerminateThread(0x000E, 0xFF)
    ChrSetFlags(0x000F, 0x0080)
    ChrSetFlags(0x000E, 0x0080)
    CameraMove(-5830, 0, 39000, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(346000, 0)
    OP_6E(280, 0)
    ChrSetPos(0x0008, -5850, 0, 40270, 180)
    ChrSetPos(0x0101, -5500, 0, 35010, 0)
    ChrSetPos(0x0102, -6750, 0, 35300, 0)
    ChrSetPos(0x0105, -4320, 0, 35440, 0)
    ChrSetPos(0x0009, -2140, 0, 42020, 270)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0490061662V#668F不、不可能……\n',
            '我忠实的爱犬竟然……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490061663V这群混蛋，看你们做的好事！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061664V#005F呼～呼～……\n',
            '这句话应该是我们说才对！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020061665V#012F现根据游击士协会的规定，\n',
            '我们要将你作为现行犯逮捕归案。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020061666V请你不要再做多余的抵抗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0490061667V#667F嘿嘿嘿嘿嘿……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490061668V这样的话没办法了……\n',
            '只有亮出我的最后底牌了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(500)
    PlaySE(143, 0x00, 0x64)
    ChrSetChipByIndex(0x0008, 18)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010061669V#580F哎！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020061670V#012F手杖……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_6595')
    def lambda_6595():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, 1000, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_6595)

    Sleep(100)

    @scena.Lambda('lambda_65B5')
    def lambda_65B5():
        OP_6C(315000, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_65B5)

    @scena.Lambda('lambda_65C5')
    def lambda_65C5():
        CameraMove(-6640, 0, 41150, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_65C5)

    @scena.Lambda('lambda_65DD')
    def lambda_65DD():
        ChrMoveToRelative(0x00FE, 0, 0, 5900, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_65DD)

    @scena.Lambda('lambda_65F8')
    def lambda_65F8():
        ChrMoveToRelative(0x00FE, 0, 0, 5900, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_65F8)

    @scena.Lambda('lambda_6613')
    def lambda_6613():
        ChrMoveToRelative(0x00FE, 0, 0, 5900, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_6613)

    Sleep(600)

    PlaySE(197, 0x00, 0x64)
    TerminateThread(0x0008, 0xFF)
    LoadEffect(0x00, 'map\\\\mp006_00.eff')
    PlayEffect(0x00, 0x00, 0x0008, -350, 1100, 200, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    ChrTalk(
        0x0008,
        (
            '#0490061671V#665F时间啊，停止吧！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    FadeOut(1, 16777215, -1)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0102, 0x01)
    TerminateThread(0x0105, 0x01)
    OP_0D()
    CreateThread(0x0101, 0x01, 0x00, func_15_7A84)
    FadeIn(400, 16777215)
    Sleep(500)

    OP_9E(0x0101, 15, 0, 300, 4000)
    Sleep(700)

    OP_9E(0x0101, 15, 0, 300, 4000)

    ChrTalk(
        0x0101,
        (
            '#0010061672V#581F身、身体动不了了……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_9E(0x0102, 15, 0, 300, 4000)

    ChrTalk(
        0x0102,
        (
            '#0020061673V#513F这、这是……\n',
            '导力魔法吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_9E(0x0105, 15, 0, 300, 4000)

    ChrTalk(
        0x0105,
        (
            '#0060061674V#541F不、不是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060061675V这恐怕是古代遗物的力量！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_9E(0x0009, 15, 0, 300, 4000)

    ChrTalk(
        0x0009,
        (
            '#0270061676V#144F那是什么东西！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0490061677V#667F#2P呵呵，科洛丝还真是博学。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490061678V这就是我戴尔蒙家族的传家之宝，\n',
            '古代遗物『封印宝杖』……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490061679V它拥有让一定范围内的人\n',
            '完全无法动弹的力量。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_9E(0x0101, 15, 0, 300, 4000)

    ChrTalk(
        0x0101,
        (
            '#0010061680V#581F怎、怎么有这种荒唐的力量……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020061681V#513F竟然还有这样强大的古代遗物\n',
            '未被教会回收而流传在外……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0490061682V#667F#2P呵呵……\n',
            '不愧是古代文明的智慧结晶。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490061683V拥有着战术导力器\n',
            '所无法比拟的力量啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490061684V不过……\n',
            '缺点就是只有这一项功能。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(500)
    PlaySE(216, 0x00, 0x64)
    ChrSetChipByIndex(0x0008, 19)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0490061685V#667F#2P没办法。\n',
            '只好由我来亲手了结你们了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490061686V呵呵呵……你们感到很荣幸吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_6A65')
    def lambda_6A65():
        CameraMove(-6640, 0, 40150, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_6A65)

    OP_92(0x0008, 0x0101, 1900, 1000, 0x00)

    ChrTalk(
        0x0008,
        (
            '#0490061687V#667F#2P那么首先第一个……\n',
            '就从狂妄的小丫头开始吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_9E(0x0101, 15, 0, 300, 4000)

    ChrTalk(
        0x0101,
        (
            '#0010061688V#009F哼，谁是狂妄的小丫头啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0105, 200)

    ChrTalk(
        0x0008,
        (
            '#0490061689V#667F#2P而自以为是的小丫头\n',
            '就留到最后解决好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_9E(0x0105, 15, 0, 300, 4000)

    ChrTalk(
        0x0105,
        (
            '#0060061690V#042F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 200)

    ChrTalk(
        0x0008,
        (
            '#0490061691V#667F#2P呵呵呵……\n',
            '刚才的气势跑到哪里去了？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490061692V要是现在乖乖求饶，\n',
            '或许我会大发慈悲放过你们哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_9E(0x0101, 15, 0, 300, 4000)

    ChrTalk(
        0x0101,
        (
            '#0010061693V#005F谁、谁要向你这种家伙……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_9E(0x0102, 15, 0, 300, 4000)

    ChrTalk(
        0x0102,
        (
            '#0020061694V#013F别用你那……脏手……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0490061695V#663F#2P什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_6CBD')
    def lambda_6CBD():
        OP_9E(0x0102, 15, 0, 2000, 4000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_6CBD)

    ChrTalk(
        0x0102,
        (
            '#0020061696V#510F别用你那脏手碰艾丝蒂尔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020061697V要是……\n',
            '你敢动她一根头发的话……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020061698V我一定不惜一切代价，\n',
            '让你尸骨无存……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x0008,
        (
            '#0490061699V#668F#2P什……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061700V#580F约、约修亚……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060061701V#044F约修亚……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0490061702V#666F#2P你、你根本连一根指头都动不了，\n',
            '还敢在我面前说狠话……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490061703V#666F好吧！\n',
            '我就先解决你再说！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_92(0x0008, 0x0102, 1200, 1000, 0x00)
    ChrTurnDirection(0x0008, 0x0102, 400)
    Sleep(400)

    OP_9E(0x0101, 15, 0, 300, 4000)

    ChrTalk(
        0x0101,
        (
            '#0010061704V#005F住、住手！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010061705V你要是敢伤害约修亚，\n',
            '我艾丝蒂尔绝对不会放过你！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020061706V#510F……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_9E(0x0105, 15, 0, 300, 4000)

    ChrTalk(
        0x0105,
        (
            '#0060061707V#043F约修亚！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0490061708V#667F#2P去死吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000005DC)
    TerminateThread(0x0101, 0xFF)

    @scena.Lambda('lambda_6F72')
    def lambda_6F72():
        OP_9E(0x0101, 15, 0, 2000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_6F72)

    ChrTalk(
        0x0101,
        (
            '#0010061709V#504F不要啊啊啊啊啊啊啊啊！！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(144, 0x00, 0x64)
    LoadEffect(0x01, 'map\\\\mp007_01.eff')
    PlayEffect(0x01, 0x02, 0x0101, 350, 800, 200, 0, 0, 0, 100, 100, 100, 0x00FF, 0, 0, 0, 0)
    OP_77(0xBE, 0xBE, 0xBE, 0x00, 0x000007D0)
    OP_0D()
    Sleep(1600)

    OP_62(0x0008, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x0008,
        (
            '#0490061710V#668F#2P什……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0008, 180, 400)
    ChrMoveTo(0x0008, -6020, 0, 41400, 3000, 0x00)
    OP_77(0xA0, 0xA0, 0xA0, 0x00, 0x000003E8)

    ChrTalk(
        0x0105,
        (
            '#0060061711V#044F这光是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_77(0x82, 0x82, 0x82, 0x00, 0x000003E8)

    ChrTalk(
        0x0009,
        (
            '#0270061712V#142F#3P可恶……\n',
            '要是手能动的话就能拍照了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(145, 0x00, 0x64)
    LoadEffect(0x01, 'map\\\\mp015_00.eff')
    PlayEffect(0x01, 0x03, 0x0101, 350, 800, 200, 0, 0, 0, 500, 500, 500, 0x00FF, 0, 0, 0, 0)
    OP_77(0x64, 0x64, 0x64, 0x00, 0x000001F4)
    Sleep(500)

    OP_23(0x0090)
    StopEffect(0x02, 0x02)
    StopEffect(0x00, 0x02)
    OP_77(0xFF, 0xFF, 0xFF, 0x00, 0x000003E8)
    Sleep(1500)

    ChrTalk(
        0x0008,
        (
            '#0490061713V#668F什、什什什什么——！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0xFF)

    ExecExpressionWithValue(
        0x0101,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0101, 65535)
    ChrSetSubChip(0x0101, 0)
    Sleep(50)

    TerminateThread(0x0102, 0xFF)

    ExecExpressionWithValue(
        0x0102,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0102, 65535)
    ChrSetSubChip(0x0102, 0)
    Sleep(50)

    TerminateThread(0x0105, 0xFF)

    ExecExpressionWithValue(
        0x0105,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0105, 65535)
    ChrSetSubChip(0x0105, 0)
    Sleep(500)

    ChrTalk(
        0x0105,
        (
            '#0060061714V#044F身体……能动了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020061715V#014F艾丝蒂尔……刚才那黑色的光是？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061716V#004F啊，嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010061717V是寄给老爸的\n',
            '那个黑色导力器……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(500)
    ChrSetChipByIndex(0x0101, 25)
    ChrClearFlags(0x001A, 0x0080)
    ChrSetPos(0x001A, -5500, 500, 38500, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010061718V#505F好像是那东西发出来的光……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0490061719V#668F这、这怎么可能……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490061720V#668F我戴尔蒙家族祖传的古代遗物\n',
            '怎么可能被这种东西破坏！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x001A, 0x0080)
    ChrSetChipByIndex(0x0101, 65535)

    @scena.Lambda('lambda_7358')
    def lambda_7358():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_7358)

    @scena.Lambda('lambda_7366')
    def lambda_7366():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_7366)

    @scena.Lambda('lambda_7374')
    def lambda_7374():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_7374)

    ChrTalk(
        0x0102,
        (
            '#0020061721V#015F不管怎样……\n',
            '现在你的手上已经没有底牌了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    PlaySE(501, 0x00, 0x64)
    ChrSetChipByIndex(0x0102, 9)
    OP_0D()

    ChrTalk(
        0x0102,
        (
            '#0020061722V#012F还是面对现实吧。\n',
            '戴尔蒙，你已经无处可逃了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061723V#009F没、没错！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    PlaySE(500, 0x00, 0x64)
    ChrSetChipByIndex(0x0101, 8)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010061724V#005F刚才你竟敢\n',
            '用那种无耻的手法整我们～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    PlaySE(504, 0x00, 0x64)
    ChrSetChipByIndex(0x0105, 10)
    OP_0D()

    ChrTalk(
        0x0105,
        (
            '#0060061725V#042F真卑劣……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_9E(0x0008, 15, 0, 300, 4000)

    ChrTalk(
        0x0008,
        (
            '#0490061726V#666F呜呜呜呜呜呜呜……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490061727V……你们休想抓住我！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_7510')
    def lambda_7510():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_7510')

    DispatchAsync2(0x0101, 0x0001, lambda_7510)

    @scena.Lambda('lambda_7521')
    def lambda_7521():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_7521')

    DispatchAsync2(0x0102, 0x0001, lambda_7521)

    @scena.Lambda('lambda_7532')
    def lambda_7532():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_7532')

    DispatchAsync2(0x0105, 0x0001, lambda_7532)

    ChrSetChipByIndex(0x0008, 0)
    ChrSetDirection(0x0008, 270, 800)
    ChrWalkTo(0x0008, -8780, 0, 40890, 6000, 0x00)
    ChrSetFlags(0x0008, 0x0080)

    ChrTalk(
        0x0101,
        (
            '#0010061728V#005F啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlayBGM(82)

    ChrTalk(
        0x0102,
        (
            '#0020061729V#016F我们快追！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060061730V#046F是！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x0101, 65535)
    CreateThread(0x0101, 0x01, 0x00, func_11_78C1)
    Sleep(400)

    ChrSetChipByIndex(0x0102, 65535)
    CreateThread(0x0102, 0x01, 0x00, func_11_78C1)
    Sleep(300)

    ChrSetChipByIndex(0x0105, 65535)
    CreateThread(0x0105, 0x01, 0x00, func_11_78C1)
    WaitForThreadExit(0x0105, 0x0001)

    ChrTalk(
        0x0009,
        (
            '#0270061731V#144F#3P啊啊，等等我！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270061732V这、这种爆炸性的新闻，\n',
            '岂能让我白白错过！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0009, 0x01, 0x00, func_11_78C1)
    Sleep(2000)

    CameraMove(-1160, 0, 41000, 2000)

    ChrTalk(
        0x000B,
        (
            '#0660061733V#722F哎呀哎呀……\n',
            '这下非减寿不可……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660061734V公爵大人，没事吧，大人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0640061735V#228F#1P嗯……\n',
            '有魔兽，魔兽……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0102, 0x0080)
    ChrSetFlags(0x0105, 0x0080)
    ChrSetFlags(0x0009, 0x0080)
    Fade(1000)
    CameraMove(-61080, 0, 54230, 0)
    ChrSetPos(0x0008, -59900, 0, 51220, 0)

    @scena.Lambda('lambda_7741')
    def lambda_7741():
        ChrWalkTo(0x00FE, -62580, 0, 50740, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_7741)

    CreateThread(0x0101, 0x01, 0x00, func_12_78F9)
    Sleep(700)

    @scena.Lambda('lambda_7768')
    def lambda_7768():
        ChrJumpTo(0x00FE, -63850, -5000, 50980, 1000, 6000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_7768)

    CreateThread(0x0102, 0x01, 0x00, func_12_78F9)
    Sleep(700)

    CreateThread(0x0105, 0x01, 0x00, func_12_78F9)
    WaitForThreadExit(0x0101, 0x0001)
    OP_72(0x000F, 0x0010)
    OP_6F(0x000F, 29)
    Fade(1000)
    CameraMove(-61320, 0, -38840, 0)
    CreateThread(0x0101, 0x01, 0x00, func_13_7994)
    Sleep(700)

    CreateThread(0x0102, 0x01, 0x00, func_13_7994)
    Sleep(700)

    CreateThread(0x0105, 0x01, 0x00, func_13_7994)
    Sleep(2200)

    OP_62(0x0009, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    CreateThread(0x0009, 0x01, 0x00, func_14_7A08)
    Sleep(500)

    WaitForThreadExit(0x0101, 0x0001)
    Sleep(1000)

    MapSetFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T2200._SN', 102, 0, 0)
    IdleLoop()

    Return()

# id: 0x000E offset: 0x7818
@scena.Code('func_0E_7818')
def func_0E_7818():
    ChrClearFlags(0x00FE, 0x0080)
    ChrMoveTo(0x00FE, 7500, 0, 37570, 4000, 0x00)
    ChrMoveTo(0x00FE, 2670, 0, 39450, 4000, 0x00)
    ChrSetDirection(0x00FE, 270, 400)

    Return()

# id: 0x000F offset: 0x784D
@scena.Code('func_0F_784D')
def func_0F_784D():
    Sleep(500)

    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, 7480, 0, 37020, 4000, 0x00)
    ChrWalkTo(0x00FE, 3330, 0, 37910, 4000, 0x00)
    ChrSetDirection(0x00FE, 270, 400)

    Return()

# id: 0x0010 offset: 0x7887
@scena.Code('func_10_7887')
def func_10_7887():
    Sleep(1000)

    ChrClearFlags(0x00FE, 0x0080)
    ChrMoveTo(0x00FE, 7480, 0, 37020, 4000, 0x00)
    ChrMoveTo(0x00FE, 4090, 0, 38540, 4000, 0x00)
    ChrSetDirection(0x00FE, 270, 400)

    Return()

# id: 0x0011 offset: 0x78C1
@scena.Code('func_11_78C1')
def func_11_78C1():
    ChrWalkTo(0x00FE, -7580, 0, 40850, 6000, 0x00)
    ChrSetFlags(0x00FE, 0x0004)
    ChrWalkTo(0x00FE, -12590, 0, 41010, 6000, 0x00)
    ChrClearFlags(0x00FE, 0x0004)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x0012 offset: 0x78F9
@scena.Code('func_12_78F9')
def func_12_78F9():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetPos(0x00FE, -55480, 0, 54970, 0)
    ChrWalkTo(0x00FE, -57930, 0, 54930, 5000, 0x00)
    ChrWalkTo(0x00FE, -59180, 0, 52070, 5000, 0x00)
    ChrWalkTo(0x00FE, -64010, 0, 52220, 5000, 0x00)
    ChrSetFlags(0x00FE, 0x0004)

    @scena.Lambda('lambda_7956')
    def lambda_7956():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0000, lambda_7956)

    ChrJumpTo(0x00FE, -64310, -500, 50900, 1000, 6000)
    Sleep(100)

    ChrMoveTo(0x00FE, -64310, -8000, 50900, 4000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x0013 offset: 0x7994
@scena.Code('func_13_7994')
def func_13_7994():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetPos(0x00FE, -62450, 2310, -43030, 270)
    ChrMoveTo(0x00FE, -62450, 1000, -43030, 4000, 0x00)
    ChrClearFlags(0x00FE, 0x0004)
    ChrJumpTo(0x00FE, -61540, 0, -43080, 200, 4000)
    ChrWalkTo(0x00FE, -62070, 0, -38060, 5000, 0x00)
    ChrWalkTo(0x00FE, -64280, 0, -37680, 5000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x0014 offset: 0x7A08
@scena.Code('func_14_7A08')
def func_14_7A08():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetFlags(0x00FE, 0x0004)
    ChrSetPos(0x00FE, -62450, 2310, -43030, 270)
    ChrJumpTo(0x00FE, -61950, 0, -43030, 200, 6000)
    ChrJumpTo(0x00FE, -61540, 0, -43080, 300, 6000)
    Sleep(500)

    ChrWalkTo(0x00FE, -62070, 0, -38060, 5000, 0x00)
    ChrWalkTo(0x00FE, -64280, 0, -37680, 5000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x0015 offset: 0x7A84
@scena.Code('func_15_7A84')
def func_15_7A84():
    OP_77(0xCD, 0xED, 0xF0, 0x00, 0x00000000)
    def _loc_7A8D(): pass

    label('loc_7A8D')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_7AB5',
    )

    OP_77(0xCD, 0xED, 0xF0, 0x00, 0x000001F4)
    Sleep(1000)

    OP_77(0x8C, 0xCE, 0xFF, 0x00, 0x000001F4)
    Sleep(1000)

    Jump('loc_7A8D')

    def _loc_7AB5(): pass

    label('loc_7AB5')

    Return()

# id: 0x0016 offset: 0x7AB6
@scena.Code('func_16_7AB6')
def func_16_7AB6():
    NewScene('ED6_DT01/T2210._SN', 123, 1, 0)
    IdleLoop()

    Return()

# id: 0x0017 offset: 0x7AC0
@scena.Code('func_17_7AC0')
def func_17_7AC0():
    NewScene('ED6_DT01/T2210._SN', 121, 1, 0)
    IdleLoop()

    Return()

# id: 0x0018 offset: 0x7ACA
@scena.Code('func_18_7ACA')
def func_18_7ACA():
    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '是开合桥的控制装置。',
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
