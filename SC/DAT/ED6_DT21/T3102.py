import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T3102_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3102   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'T3102.x'
    header.mapIndex       = 1
    header.bgm            = 13
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
        ('ED6_DT07/CH01100._CH', 'ED6_DT07/CH01100P._CP'),
        ('ED6_DT07/CH01150._CH', 'ED6_DT07/CH01150P._CP'),
        ('ED6_DT07/CH01170._CH', 'ED6_DT07/CH01170P._CP'),
        ('ED6_DT07/CH01130._CH', 'ED6_DT07/CH01130P._CP'),
        ('ED6_DT07/CH01470._CH', 'ED6_DT07/CH01470P._CP'),
        ('ED6_DT07/CH01000._CH', 'ED6_DT07/CH01000P._CP'),
        ('ED6_DT07/CH01360._CH', 'ED6_DT07/CH01360P._CP'),
        ('ED6_DT07/CH01290._CH', 'ED6_DT07/CH01290P._CP'),
        ('ED6_DT07/CH01450._CH', 'ED6_DT07/CH01450P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH01210._CH', 'ED6_DT07/CH01210P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT07/CH01680._CH', 'ED6_DT07/CH01680P._CP'),
        ('ED6_DT07/CH02440._CH', 'ED6_DT07/CH02440P._CP'),
        ('ED6_DT07/CH01180._CH', 'ED6_DT07/CH01180P._CP'),
        ('ED6_DT07/CH01200._CH', 'ED6_DT07/CH01200P._CP'),
    ]

# id: 0x10001 offset: 0x132
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '乘客',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '乘客',
            x                   = 0,
            z                   = 0,
            y                   = 0,
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
            name                = '女孩子',
            x                   = 0,
            z                   = 0,
            y                   = 0,
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
            name                = '女性客人',
            x                   = 0,
            z                   = 0,
            y                   = 0,
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
            name                = '男孩',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '乘客',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '乘客',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '乘客',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '受理人吉拉尔',
            x                   = -20110,
            z                   = 8000,
            y                   = 121830,
            direction           = 177,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '巴拉特',
            x                   = -44890,
            z                   = -4000,
            y                   = 146670,
            direction           = 135,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '阿尔丹',
            x                   = -41630,
            z                   = 8000,
            y                   = 123450,
            direction           = 135,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '列曼',
            x                   = -44830,
            z                   = -4000,
            y                   = 141220,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '鲁特尔',
            x                   = -50230,
            z                   = 8000,
            y                   = 121120,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '诺蒂亚',
            x                   = -49500,
            z                   = 8000,
            y                   = 121470,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '法尔茨',
            x                   = -50910,
            z                   = 8000,
            y                   = 121470,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '雨果',
            x                   = -46020,
            z                   = -4000,
            y                   = 146670,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            name                = '格斯塔夫维修长',
            x                   = -39960,
            z                   = 8000,
            y                   = 129060,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            name                = '吉米',
            x                   = -44890,
            z                   = -4000,
            y                   = 140090,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            name                = '赛希莉亚号',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0184,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '赛希莉亚号影',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0184,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '蔡斯市·工房区',
            x                   = -18770,
            z                   = 8000,
            y                   = 89560,
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

# id: 0x10002 offset: 0x3D2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x3D2
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x3D2
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -19980,
            triggerZ            = 8000,
            triggerY            = 119710,
            triggerRange        = 400,
            actorX              = -20110,
            actorZ              = 9500,
            actorY              = 121830,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -41010,
            triggerZ            = 8000,
            triggerY            = 122500,
            triggerRange        = 800,
            actorX              = -41010,
            actorZ              = 10200,
            actorY              = 122500,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x002F,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -38900,
            triggerZ            = 8400,
            triggerY            = 122040,
            triggerRange        = 800,
            actorX              = -38900,
            actorZ              = 9900,
            actorY              = 122040,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0030,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x43E
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_491',
    )

    ChrClearFlags(0x0018, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_48E',
    )

    ChrSetFlags(0x0012, 0x0080)
    ChrSetPos(0x0010, -23200, 8000, 121010, 180)
    ChrClearFlags(0x0018, 0x0010)
    ChrClearFlags(0x0014, 0x0080)
    ChrSetPos(0x0014, -57460, 4000, 129380, 61)
    ChrSetDirection(0x0011, 90, 0)

    def _loc_48E(): pass

    label('loc_48E')

    Jump('loc_54A')

    def _loc_491(): pass

    label('loc_491')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 2, 0x1602)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4E0',
    )

    ChrSetPos(0x0012, -56860, 4000, 129490, 45)
    ChrSetPos(0x0014, -42830, 8000, 129500, 0)
    ChrClearFlags(0x0014, 0x0080)
    ChrClearFlags(0x0015, 0x0080)
    ChrClearFlags(0x0016, 0x0080)

    If(
        (
            (Expr.Eval, "OP_29(0x0071, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_4DD',
    )

    ChrClearFlags(0x0019, 0x0080)

    def _loc_4DD(): pass

    label('loc_4DD')

    Jump('loc_54A')

    def _loc_4E0(): pass

    label('loc_4E0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_525',
    )

    ChrSetPos(0x0011, -44890, -4000, 146670, 270)
    ChrSetFlags(0x0011, 0x0010)
    ChrSetPos(0x0012, -44340, -4000, 151130, 90)
    ChrClearFlags(0x0013, 0x0080)
    ChrClearFlags(0x0017, 0x0080)
    ChrClearFlags(0x0018, 0x0080)
    ChrClearFlags(0x0018, 0x0010)

    Jump('loc_54A')

    def _loc_525(): pass

    label('loc_525')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_540',
    )

    ChrSetPos(0x0012, -47490, -4000, 151130, 270)

    Jump('loc_54A')

    def _loc_540(): pass

    label('loc_540')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_54A',
    )

    Jump('loc_54A')

    def _loc_54A(): pass

    label('loc_54A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 0, 0x1408)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_55C',
    )

    ChrSetFlags(0x0011, 0x0080)
    ChrSetFlags(0x0012, 0x0080)

    def _loc_55C(): pass

    label('loc_55C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 0, 0x1408)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_56D',
    )

    MapSetFlags(0x10000000)
    Event(0, func_0F_272C)

    def _loc_56D(): pass

    label('loc_56D')

    Return()

# id: 0x0001 offset: 0x56E
@scena.Code('func_01_56E')
def func_01_56E():
    OP_16(0x02, 4000, -172000, 20000, 2293843)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5B4',
    )

    OP_B1('T3102_0')
    OP_6F(0x0000, 530)
    OP_72(0x0001, 0x0020)
    OP_72(0x0001, 0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_5B1',
    )

    OP_64(0x00, 0x0001)

    def _loc_5B1(): pass

    label('loc_5B1')

    Jump('loc_639')

    def _loc_5B4(): pass

    label('loc_5B4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 2, 0x1602)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5E2',
    )

    OP_B1('T3102_1')
    OP_71(0x0003, 0x0004)
    OP_71(0x0004, 0x0004)
    OP_71(0x0005, 0x0004)
    OP_6F(0x0000, 1001)

    Jump('loc_639')

    def _loc_5E2(): pass

    label('loc_5E2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_60A',
    )

    OP_B1('T3102_2')
    OP_6F(0x0004, 1)
    OP_6F(0x0003, 200)
    OP_6F(0x0000, 1001)

    Jump('loc_639')

    def _loc_60A(): pass

    label('loc_60A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_61D',
    )

    OP_B1('T3102_0')

    Jump('loc_639')

    def _loc_61D(): pass

    label('loc_61D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_630',
    )

    OP_B1('T3102_0')

    Jump('loc_639')

    def _loc_630(): pass

    label('loc_630')

    OP_B1('T3102_1')

    def _loc_639(): pass

    label('loc_639')

    Return()

# id: 0x0002 offset: 0x63A
@scena.Code('func_02_63A')
def func_02_63A():
    ExecExpressionWithReg(
        0x0001,
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
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_65F',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_7A1')

    def _loc_65F(): pass

    label('loc_65F')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_678',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_7A1')

    def _loc_678(): pass

    label('loc_678')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_691',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_7A1')

    def _loc_691(): pass

    label('loc_691')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6AA',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_7A1')

    def _loc_6AA(): pass

    label('loc_6AA')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6C3',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_7A1')

    def _loc_6C3(): pass

    label('loc_6C3')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6DC',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_7A1')

    def _loc_6DC(): pass

    label('loc_6DC')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6F5',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_7A1')

    def _loc_6F5(): pass

    label('loc_6F5')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_70E',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_7A1')

    def _loc_70E(): pass

    label('loc_70E')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_727',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_7A1')

    def _loc_727(): pass

    label('loc_727')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_740',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_7A1')

    def _loc_740(): pass

    label('loc_740')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_759',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_7A1')

    def _loc_759(): pass

    label('loc_759')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_772',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_7A1')

    def _loc_772(): pass

    label('loc_772')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_78B',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_7A1')

    def _loc_78B(): pass

    label('loc_78B')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7A1',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_7A1(): pass

    label('loc_7A1')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_7B6',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_7A1')

    def _loc_7B6(): pass

    label('loc_7B6')

    Return()

# id: 0x0003 offset: 0x7B7
@scena.Code('func_03_7B7')
def func_03_7B7():
    Call(0, 0x0004)

    Return()

# id: 0x0004 offset: 0x7BC
@scena.Code('func_04_7BC')
def func_04_7BC():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_88E',
    )

    TalkBegin(0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_82E',
    )

    ChrTalk(
        0x00FE,
        (
            '这里的飞船坪是可动式的，\n',
            '因此更加危险呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说明白一点的话，\n',
            '其实就是个技术漏洞。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Jump('loc_888')

    def _loc_82E(): pass

    label('loc_82E')

    ChrTalk(
        0x00FE,
        (
            '这里的飞船坪是可动式的，\n',
            '因此更加危险呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果是普通的飞船坪，\n',
            '还可以进行整备。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_888(): pass

    label('loc_888')

    TalkEnd(0x0010)

    Jump('loc_C17')

    def _loc_88E(): pass

    label('loc_88E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_977',
    )

    TalkBegin(0x0010)

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
            '导力停止现象的时候\n',
            '引起了很大骚乱，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '其实根本没有必要\n',
            '那么吵吵闹闹的嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈，虽然话是那么说，\n',
            '但我也一样很惊慌。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Jump('loc_971')

    def _loc_925(): pass

    label('loc_925')

    ChrTalk(
        0x00FE,
        (
            '导力停止现象的时候\n',
            '引起了很大骚乱，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '其实根本没有必要\n',
            '那么吵闹嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_971(): pass

    label('loc_971')

    TalkEnd(0x0010)

    Jump('loc_C17')

    def _loc_977(): pass

    label('loc_977')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 2, 0x1602)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_992',
    )

    OP_4A(0x0010, 255)
    Call(0, 0x0023)
    OP_4B(0x0010, 255)

    Jump('loc_C17')

    def _loc_992(): pass

    label('loc_992')

    TalkBegin(0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_A35',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_9E8',
    )

    ChrTalk(
        0x0010,
        (
            '工事要到雷斯顿要塞\n',
            '进行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '看来果然是关系到\n',
            '军事机密啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A32')

    def _loc_9E8(): pass

    label('loc_9E8')

    ChrTalk(
        0x0010,
        (
            '『埃尔赛尤』终于\n',
            '装上了新型的引擎啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '工作船现在正在整备中。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_A32(): pass

    label('loc_A32')

    Jump('loc_C14')

    def _loc_A35(): pass

    label('loc_A35')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_B54',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_AB4',
    )

    ChrTalk(
        0x0010,
        (
            '多亏利贝尔通讯的记者\n',
            '互不侵犯条约的事情终于清楚了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '嗯～不愧是利贝尔通讯，\n',
            '刊登的文章既详尽又有趣。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B51')

    def _loc_AB4(): pass

    label('loc_AB4')

    ChrTalk(
        0x0010,
        (
            '最近利贝尔通讯花了很大篇幅\n',
            '对互不侵犯条约事件进行了报道哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '多亏了杂志上的报道，\n',
            '我才明白了条约的重要性。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '这次的签字仪式实在是引人关注呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_B51(): pass

    label('loc_B51')

    Jump('loc_C14')

    def _loc_B54(): pass

    label('loc_B54')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_C14',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_BB7',
    )

    ChrTalk(
        0x0010,
        (
            '真是的，刚才实在\n',
            '太危险了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '在危机来临的时候，\n',
            '人会因恐惧而失去冷静。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C14')

    def _loc_BB7(): pass

    label('loc_BB7')

    ChrTalk(
        0x0010,
        (
            '呼～刚才完全慌了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '差一点陷入\n',
            '混乱之中。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '呼～不过我还是\n',
            '很快就镇定下来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_C14(): pass

    label('loc_C14')

    TalkEnd(0x0010)

    def _loc_C17(): pass

    label('loc_C17')

    Return()

# id: 0x0005 offset: 0xC18
@scena.Code('func_05_C18')
def func_05_C18():
    TalkBegin(0x0011)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_CF8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_CA5',
    )

    ChrTalk(
        0x00FE,
        (
            '接下来要检查一下\n',
            '飞船坪的设施了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼～就算检查。\n',
            '也只是个形式而已吧…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，至少总比\n',
            '什么都不做要强。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Jump('loc_CF5')

    def _loc_CA5(): pass

    label('loc_CA5')

    ChrTalk(
        0x00FE,
        (
            '接下来要检查一下\n',
            '飞船坪的设施了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼～就算检查。\n',
            '也只是个形式而已吧…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_CF5(): pass

    label('loc_CF5')

    Jump('loc_10C4')

    def _loc_CF8(): pass

    label('loc_CF8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_E06',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_DAD',
    )

    ChrTalk(
        0x00FE,
        (
            '这种现象是在\n',
            '移动工房船的时候出现的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '结果就在拉高到一半时\n',
            '突然停住不动了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就那样悬在半空，\n',
            '根本没办法整备。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是的……\n',
            '究竟是怎么回事呢，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Jump('loc_E03')

    def _loc_DAD(): pass

    label('loc_DAD')

    ChrTalk(
        0x00FE,
        (
            '竟然会在移动工房船的时候\n',
            '出现这种事…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '结果就在拉高到一半时\n',
            '突然停住不动了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E03(): pass

    label('loc_E03')

    Jump('loc_10C4')

    def _loc_E06(): pass

    label('loc_E06')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_EA3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_E65',
    )

    ChrTalk(
        0x00FE,
        (
            '装载新型引擎的\n',
            '『埃尔赛尤』啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊啊～真想早日瞻仰到\n',
            '它的雄姿呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EA0')

    def _loc_E65(): pass

    label('loc_E65')

    ChrTalk(
        0x00FE,
        (
            '刚好现在工房船\n',
            '正要出发了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真想赶快过去啊… ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_EA0(): pass

    label('loc_EA0')

    Jump('loc_10C4')

    def _loc_EA3(): pass

    label('loc_EA3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_F4B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_F08',
    )

    ChrTalk(
        0x00FE,
        (
            '新型引擎\n',
            '终于也进入实装阶段了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '改装工作要加油啊！\n',
            '我也要继续向女神祈祷！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F48')

    def _loc_F08(): pass

    label('loc_F08')

    ChrTalk(
        0x00FE,
        (
            '是，已经搬运完毕了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '需要的配件已经\n',
            '全部准备好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_F48(): pass

    label('loc_F48')

    Jump('loc_10C4')

    def _loc_F4B(): pass

    label('loc_F4B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_104B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_FB2',
    )

    ChrTalk(
        0x00FE,
        (
            '那么，接下来就要开始\n',
            '工房船的出港准备了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在维修长回来之前\n',
            '要全部完成才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1048')

    def _loc_FB2(): pass

    label('loc_FB2')

    ChrTalk(
        0x00FE,
        (
            '那么，马上要进行工房船\n',
            '的出港准备了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为了装配『埃尔赛尤』的引擎，\n',
            '接下来要去雷斯顿要塞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '维修长为此也是一大早\n',
            '就跑去中央工房了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_1048(): pass

    label('loc_1048')

    Jump('loc_10C4')

    def _loc_104B(): pass

    label('loc_104B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_10C4',
    )

    ChrTalk(
        0x00FE,
        (
            '地震是我干完工作之后的事情了，\n',
            '所以物品的检查没出什么乱子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '即使没出现什么问题，\n',
            '我们也不能松懈精神啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_10C4(): pass

    label('loc_10C4')

    TalkEnd(0x0011)

    Return()

# id: 0x0006 offset: 0x10C8
@scena.Code('func_06_10C8')
def func_06_10C8():
    TalkBegin(0x0012)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_11CC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_114C',
    )

    ChrTalk(
        0x00FE,
        (
            '那么！拍摄完『赛希莉亚号』\n',
            '的着陆照片之后就去王都！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊啊～『埃尔赛尤』啊……\n',
            '马上就去，再稍等一会吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11C9')

    def _loc_114C(): pass

    label('loc_114C')

    ChrTalk(
        0x00FE,
        (
            '嗯，工房船的起飞照片\n',
            '也顺利拍摄到了呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈～这次的摄影旅行\n',
            '还真是让人感动又兴奋呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有哭有笑，真是好忙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_11C9(): pass

    label('loc_11C9')

    Jump('loc_148C')

    def _loc_11CC(): pass

    label('loc_11CC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_12B5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_1223',
    )

    ChrTalk(
        0x00FE,
        (
            '没想到竟然可以这么近距离地\n',
            '看到工房船… ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呜呜～活着真好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12B2')

    def _loc_1223(): pass

    label('loc_1223')

    ChrTalk(
        0x00FE,
        (
            '这就是中央工房所有的\n',
            '工房船『莱普尼兹号』哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不但各种设施齐备，\n',
            '而且还可以进行制品搬运。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '它可是有着『飞行的工房』之称号呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_12B2(): pass

    label('loc_12B2')

    Jump('loc_148C')

    def _loc_12B5(): pass

    label('loc_12B5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_137F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_12FB',
    )

    ChrTalk(
        0x00FE,
        (
            '噢噢～\n',
            '现在不是感动的时候。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '拍照、拍照～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_137C')

    def _loc_12FB(): pass

    label('loc_12FB')

    ChrTalk(
        0x00FE,
        (
            '噢噢噢！！那、那是！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那不就是做梦都想看到的\n',
            '『莱普尼兹号』吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呜哇哇～～～太壮观了！！\n',
            '一直保管在地下吗～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_137C(): pass

    label('loc_137C')

    Jump('loc_148C')

    def _loc_137F(): pass

    label('loc_137F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_148C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_13EC',
    )

    ChrTalk(
        0x00FE,
        (
            '现、现在可不是为\n',
            '地震而吃惊的时候，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要在下一艘飞船到来之前\n',
            '准备好拍摄的准备工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_148C')

    def _loc_13EC(): pass

    label('loc_13EC')

    ChrTalk(
        0x00FE,
        (
            '呼～呼～\n',
            '似、似乎还能感觉到摇晃呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊啊～吓死我了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不、不过现在不是因\n',
            '地震而吃惊的时候，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要在下一艘飞船到来之前\n',
            '准备好拍摄的准备工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_148C(): pass

    label('loc_148C')

    TalkEnd(0x0012)

    Return()

# id: 0x0007 offset: 0x1490
@scena.Code('func_07_1490')
def func_07_1490():
    TalkBegin(0x0013)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_1542',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_14ED',
    )

    ChrTalk(
        0x00FE,
        (
            '还真是吓人呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为目的地相同，让我\n',
            '想起了营救博士的那一战呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1542')

    def _loc_14ED(): pass

    label('loc_14ED')

    ChrTalk(
        0x00FE,
        (
            '现在正在进行\n',
            '工房船的出行准备。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好久没有这么大的工作了，\n',
            '真是好紧张呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_1542(): pass

    label('loc_1542')

    TalkEnd(0x0013)

    Return()

# id: 0x0008 offset: 0x1546
@scena.Code('func_08_1546')
def func_08_1546():
    TalkBegin(0x0014)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_1653',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_15FC',
    )

    ChrTalk(
        0x00FE,
        (
            '最近利用飞船的\n',
            '合作多起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '特别是来自帝国和共和国的\n',
            '合作明显多了起来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '能签署正式协议\n',
            '确实是个好现象啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，也有可能\n',
            '只是泡沫现象…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    Jump('loc_1650')

    def _loc_15FC(): pass

    label('loc_15FC')

    ChrTalk(
        0x00FE,
        (
            '最近对飞船的\n',
            '合作明显多了起来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '期待度越高，\n',
            '希望破灭时的打击也就越大啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1650(): pass

    label('loc_1650')

    Jump('loc_17FD')

    def _loc_1653(): pass

    label('loc_1653')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1734',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_16E5',
    )

    ChrTalk(
        0x00FE,
        (
            '现在好像完全无法\n',
            '驱动导力引擎了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '难道飞船以后\n',
            '再也无法起飞了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '作为相关行业的人员，\n',
            '没有比这更大的打击了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    Jump('loc_1731')

    def _loc_16E5(): pass

    label('loc_16E5')

    ChrTalk(
        0x00FE,
        (
            '现在好像完全无法\n',
            '驱动导力引擎了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不、不过不会一直\n',
            '都这样子的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1731(): pass

    label('loc_1731')

    Jump('loc_17FD')

    def _loc_1734(): pass

    label('loc_1734')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_17FD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_1779',
    )

    ChrTalk(
        0x00FE,
        (
            '今天没有风，天气不错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，很适合飞行呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17FD')

    def _loc_1779(): pass

    label('loc_1779')

    ChrTalk(
        0x00FE,
        (
            '啊，你们也是在等\n',
            '『赛希莉亚号』吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我要去王都\n',
            '做一次短期出差。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，虽然是一次很短的旅行，\n',
            '不过还是很让人期待呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    def _loc_17FD(): pass

    label('loc_17FD')

    TalkEnd(0x0014)

    Return()

# id: 0x0009 offset: 0x1801
@scena.Code('func_09_1801')
def func_09_1801():
    TalkBegin(0x0015)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_1883',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_187F',
    )

    ChrTalk(
        0x00FE,
        (
            '地震之后，\n',
            '温泉又发生异变了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '二者看起来似乎有关联，\n',
            '但现在没空去管它了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯～～真遗憾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1883')

    def _loc_187F(): pass

    label('loc_187F')

    Call(0, 0x000B)

    def _loc_1883(): pass

    label('loc_1883')

    TalkEnd(0x0015)

    Return()

# id: 0x000A offset: 0x1887
@scena.Code('func_0A_1887')
def func_0A_1887():
    TalkBegin(0x0016)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_18ED',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_18E9',
    )

    ChrTalk(
        0x00FE,
        (
            '似乎原因在于\n',
            '温泉的源流呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '等编辑部的人回来以后\n',
            '去那里调查一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_18ED')

    def _loc_18E9(): pass

    label('loc_18E9')

    Call(0, 0x000B)

    def _loc_18ED(): pass

    label('loc_18ED')

    TalkEnd(0x0016)

    Return()

# id: 0x000B offset: 0x18F1
@scena.Code('func_0B_18F1')
def func_0B_18F1():
    OP_4A(0x0015, 255)
    OP_4A(0x0016, 255)

    ChrTalk(
        0x0015,
        (
            '法尔茨！\n',
            '亚尔摩村的采访怎么样了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '不会是泡温泉\n',
            '泡到忘了正事吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '啊～没有。\n',
            '因为出了意外。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '不知是什么原因，\n',
            '温泉的水沸腾了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '温泉沸腾了……真的吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '是的…已经做了\n',
            '简单的记录。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '虽然时间匆忙，\n',
            '不过这新闻值得报道。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '好！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '那么马上整理一下，\n',
            '归纳出一份报道吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4B(0x0015, 255)
    OP_4B(0x0016, 255)
    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))
    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    Return()

# id: 0x000C offset: 0x1A35
@scena.Code('func_0C_1A35')
def func_0C_1A35():
    TalkBegin(0x0017)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_1B09',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_1AB8',
    )

    ChrTalk(
        0x00FE,
        (
            '总之，要带的东西\n',
            '一定不能忘掉啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这次要去雷斯顿要塞\n',
            '工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是把东西忘在这里\n',
            '就没法回来取了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B09')

    def _loc_1AB8(): pass

    label('loc_1AB8')

    ChrTalk(
        0x00FE,
        (
            '『ＸＧ－０２』\n',
            '已经装载好了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '其他附带的零件\n',
            '也不要忘了搬进去啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    def _loc_1B09(): pass

    label('loc_1B09')

    TalkEnd(0x0017)

    Return()

# id: 0x000D offset: 0x1B0D
@scena.Code('func_0D_1B0D')
def func_0D_1B0D():
    TalkBegin(0x0018)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_21F3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_1C07',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1BAF',
    )

    ChrTalk(
        0x0018,
        (
            '#0561130014V#691F听说水泵已经\n',
            '修好了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0561130015V如果可能的话，我也想去\n',
            '亚尔摩泡泡温泉…',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0561130016V算了，以后再说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    Jump('loc_1C04')

    def _loc_1BAF(): pass

    label('loc_1BAF')

    ChrTalk(
        0x0018,
        (
            '#0561130017V#690F哎呀呀～虽然船\n',
            '就在那里…',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0561130018V但却没办法\n',
            '回收材料啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C04(): pass

    label('loc_1C04')

    Jump('loc_21F0')

    def _loc_1C07(): pass

    label('loc_1C07')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0401, 7, 0x200F)),
            Expr.Return,
        ),
        'loc_1D3D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1CE0',
    )

    ChrTalk(
        0x0018,
        (
            '#0561130019V#691F哦，要找的东西已经找到了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010311470V#1000F嗯，虽然有点麻烦\n',
            '但还是解决了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '#0561130020V#691F哈，不管怎么说，\n',
            '找到了就好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0561130021V水泵的修理工作要加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    Jump('loc_1D3A')

    def _loc_1CE0(): pass

    label('loc_1CE0')

    ChrTalk(
        0x0018,
        (
            '#0561130022V#691F哈，不管怎么说，\n',
            '找到了就好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0561130021V水泵的修理工作要加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1D3A(): pass

    label('loc_1D3A')

    Jump('loc_21F0')

    def _loc_1D3D(): pass

    label('loc_1D3D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0401, 3, 0x200B)),
            Expr.Return,
        ),
        'loc_1DB0',
    )

    ChrTalk(
        0x0018,
        (
            '#0561130023V#691F内燃引擎应该存放在\n',
            '雷斯顿要塞中。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0561130024V抱歉啊～你们自己\n',
            '去那里问问可以吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_21F0')

    def _loc_1DB0(): pass

    label('loc_1DB0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0401, 3, 0x200B)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0401, 2, 0x200A)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1DC3',
    )

    Call(0, 0x002B)

    Jump('loc_21F0')

    def _loc_1DC3(): pass

    label('loc_1DC3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_1E4C',
    )

    ChrTalk(
        0x0018,
        (
            '#0561130025V#691F这样下去的话，\n',
            '也许以后还会有什么事发生呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0561130026V也许还会需要你们的帮忙，\n',
            '到那时请一定多关照啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_21F0')

    def _loc_1E4C(): pass

    label('loc_1E4C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 4, 0x2084)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2183',
    )

    SetScenaFlags(ScenaFlag(0x0410, 4, 0x2084))
    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    ChrTalk(
        0x0018,
        (
            '#0561130027V#692F啊，我还以为是谁，\n',
            '这不是艾丝蒂尔吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0011350027V#1000F维修长先生，好久不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020370078V#1040F好久不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0018, 0x0102, 400)

    ChrTalk(
        0x0018,
        (
            '#0560370382V#691F噢！这不是约修亚吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560370383V怎么回事，好像\n',
            '有很久没见了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0011350028V#1016F哈，这个就\n',
            '说来话长了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0011350029V#1000F……那个，维修长先生，\n',
            '这里的情况怎么样了？',
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
        'loc_1FF7',
    )

    ChrTalk(
        0x0107,
        (
            '#0070890020V#063F啊，还是有一些\n',
            '骚乱的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1FF7(): pass

    label('loc_1FF7')

    ChrTurnDirection(0x0018, 0x0101, 400)

    ChrTalk(
        0x0018,
        (
            '#0560370387V#690F发生了这样的异变，\n',
            '确实不得了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560370388V总之城里的情况已经算是\n',
            '稳定下来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020370389V#1040F是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020370390V总算是暂时把\n',
            '混乱控制住了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '#0561130028V#691F啊啊，但是这样的话\n',
            '也许以后还会有什么事发生呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0561130029V#693F也许会需要你们的帮忙。\n',
            '到那时请一定多关照啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0011350030V#1001F嗯，彼此彼此。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020340430V#1040F拜托你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_21F0')

    def _loc_2183(): pass

    label('loc_2183')

    ChrTalk(
        0x0018,
        (
            '#0561130030V#690F这里的飞船坪\n',
            '是用特殊构造建筑的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0561130031V导力无法复员，\n',
            '船的整备也没办法进行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_21F0(): pass

    label('loc_21F0')

    Jump('loc_26DB')

    def _loc_21F3(): pass

    label('loc_21F3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0290, 3, 0x1483)),
            Expr.Return,
        ),
        'loc_2373',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2310',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_230D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_2274',
    )

    ChrTalk(
        0x0018,
        (
            '#0561130032V#690F听说连雷斯顿要塞\n',
            '也发生地震了啊？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0561130033V要是设备没有被损毁\n',
            '就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_230D')

    def _loc_2274(): pass

    label('loc_2274')

    ChrTalk(
        0x0018,
        (
            '#0561130034V#690F中央工房刚刚\n',
            '来联络过了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0561130035V雷斯顿要塞也\n',
            '也发生地震了啊？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0561130036V呼，『埃尔赛尤』的工事\n',
            '别出什么意外就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    def _loc_230D(): pass

    label('loc_230D')

    Jump('loc_2370')

    def _loc_2310(): pass

    label('loc_2310')

    ChrTalk(
        0x0018,
        (
            '#0561130037V#690F亚尔摩村竟然是震源……\n',
            '真是搞不懂。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0561130038V总之，大家要小心行事啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_2370(): pass

    label('loc_2370')

    Jump('loc_26DB')

    def _loc_2373(): pass

    label('loc_2373')

    ChrTalk(
        0x0101,
        (
            '#0011350031V#1004F啊！维修长先生！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0018, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    OP_63(0x0018)
    ChrTurnDirection(0x0018, 0x0101, 500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_2419',
    )

    ChrTalk(
        0x0018,
        (
            '#0561130039V#6901F喔喔……\n',
            '这不是艾丝蒂尔吗！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0561130040V真是好久不见了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_246B')

    def _loc_2419(): pass

    label('loc_2419')

    ChrTalk(
        0x0018,
        (
            '#0561130041V#691F喔喔……\n',
            '这不是艾丝蒂尔吗！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0561130040V真是好久不见了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_246B(): pass

    label('loc_246B')

    ChrTalk(
        0x0101,
        (
            '#0011350032V#1006F好久不见，\n',
            '维修长先生也很有精神啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '#0561130042V#691F你们现在正在调查地震是吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0561130043V发现了什么线索吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0011350033V#1015F嗯，是这样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '将地震源是亚尔摩村告诉给维修长。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x0018,
        (
            '#0561130044V#692F……真是令人不解啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0561130045V如果要去调查的话\n',
            '尽早行动比较好吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_25EA',
    )

    ChrTalk(
        0x0106,
        (
            '#0050440971V#050F嗯，同感…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_260F')

    def _loc_25EA(): pass

    label('loc_25EA')

    ChrTalk(
        0x0103,
        (
            '#0030440972V#026F啊，同感哦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_260F(): pass

    label('loc_260F')

    ChrTalk(
        0x0101,
        (
            '#0011350034V#1002F嗯……\n',
            '确实应该抓紧时间赶快去。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0011350035V那么，维修长先生，我们先走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0018, 0x0107, 400)

    ChrTalk(
        0x0018,
        (
            '#691F噢！大家加油吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#691F提妲也要多加小心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070890021V#560F是、是的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0290, 3, 0x1483))
    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))
    ChrClearFlags(0x0018, 0x0010)
    def _loc_26DB(): pass

    label('loc_26DB')

    TalkEnd(0x0018)

    Return()

# id: 0x000E offset: 0x26DF
@scena.Code('func_0E_26DF')
def func_0E_26DF():
    TalkBegin(0x0019)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_2728',
    )

    ChrTalk(
        0x00FE,
        (
            '定期船啊，\n',
            '好久没坐过了，真期待啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '噢噢～快点来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2728(): pass

    label('loc_2728')

    TalkEnd(0x0019)

    Return()

# id: 0x000F offset: 0x272C
@scena.Code('func_0F_272C')
def func_0F_272C():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_273D',
    )

    Call(0, 0x002C)

    def _loc_273D(): pass

    label('loc_273D')

    EventBegin(0x00)
    OP_DB()
    MapClearFlags(0x00000001)
    MapClearFlags(0x00000010)
    CameraMove(-33680, -4000, 150830, 0)
    OP_67(0, 14240, -10000, 0)
    CameraSetDistance(8800, 0)
    OP_6C(44000, 0)
    OP_6E(175, 0)
    OP_A1(0x001A, 0x0004)
    OP_72(0x0004, 0x0004)
    OP_72(0x0004, 0x0020)
    ChrSetPos(0x001A, -34000, -150, 148000, 0)
    ChrSetFlags(0x001A, 0x0004)
    OP_A1(0x001B, 0x0005)
    OP_72(0x0005, 0x0004)
    OP_72(0x000A, 0x0004)
    ChrSetPos(0x001B, -34000, -10150, 148000, 0)
    ChrSetFlags(0x001B, 0x0004)
    PlaySE(121, 0x00, 0x64)
    OP_71(0x0006, 0x0004)
    OP_6F(0x0003, 100)
    OP_6F(0x0004, 60)
    OP_6F(0x0005, 0)
    OP_C8(0x0200, 0x0046, 'C_PLAC08._CH', 0x00, 0x05DC)
    ShowPlaceName('蔡斯')
    FadeIn(1500, 0)

    @scena.Lambda('lambda_281A')
    def lambda_281A():
        OP_6C(57000, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_281A)

    @scena.Lambda('lambda_282A')
    def lambda_282A():
        CameraSetDistance(6800, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_282A)

    Call(0, 0x0010)
    Fade(1000)
    CameraMove(-46650, -4000, 144430, 0)
    OP_67(0, 11610, -10000, 0)
    CameraSetDistance(4120, 0)
    OP_6C(314000, 0)
    OP_6E(175, 0)
    OP_6F(0x0003, 200)
    OP_6F(0x0004, 1)
    OP_6F(0x0005, 0)
    OP_0D()
    CreateThread(0x0008, 0x01, 0x00, func_11_35CD)
    Sleep(500)

    CreateThread(0x0009, 0x01, 0x00, func_11_35CD)
    Sleep(1000)

    CreateThread(0x000E, 0x01, 0x00, func_11_35CD)
    Sleep(1000)

    CreateThread(0x000B, 0x01, 0x00, func_13_365E)
    Sleep(500)

    CreateThread(0x000A, 0x01, 0x00, func_12_3611)
    Sleep(500)

    CreateThread(0x000C, 0x01, 0x00, func_14_36B0)
    Sleep(1000)

    CreateThread(0x000D, 0x01, 0x00, func_15_3702)
    Sleep(500)

    CreateThread(0x000F, 0x01, 0x00, func_16_3768)
    Sleep(1000)

    CreateThread(0x0101, 0x01, 0x00, func_18_37F9)
    Sleep(500)

    CreateThread(0x00F7, 0x01, 0x00, func_19_383F)
    Sleep(500)

    CreateThread(0x0105, 0x01, 0x00, func_1A_3885)
    Sleep(500)

    CreateThread(0x0104, 0x01, 0x00, func_1B_38CB)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x00F7, 0x0001)
    WaitForThreadExit(0x0105, 0x0001)
    WaitForThreadExit(0x0104, 0x0001)
    OP_DC()

    ChrTalk(
        0x0101,
        (
            '#0010220376V#1006F#1P那么，先去一趟\n',
            '协会吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010220377V要先和雾香姐打个招呼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040220378V#033F喔～听名字好像\n',
            '是位东方的女子啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040220379V#031F是个什么样的人呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220380V#1007F#1P又开始了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_2ADB',
    )

    ChrTalk(
        0x0106,
        (
            '#0050220381V#051F#5P嗯，简单说，就是个精明强干的女人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050220382V她可是个比雪拉扎德更厉害的女中豪杰，\n',
            '想乱来的话先掂量一下吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050220383V#551F说明白一点，我不想被牵连到，\n',
            '拜托你别拖累我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2BBA')

    def _loc_2ADB(): pass

    label('loc_2ADB')

    ChrTalk(
        0x0103,
        (
            '#0030220384V#027F#5P一言以蔽之，就是个『能干的女人』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030220385V不但处理事务的能力近乎完美，\n',
            '武术造诣也是达人级的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030220386V#021F虽然是个美人，但她可是丝毫不讲情面的，\n',
            '如果有什么妄想的话，你可要有所觉悟才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2BBA(): pass

    label('loc_2BBA')

    ChrTalk(
        0x0104,
        (
            '#0040220387V#031F呼呼～听你这么一说，\n',
            '我对她越来越有兴趣了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040220388V那我们赶快去协会…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(133, 0x00, 0x64)
    OP_20(0x000005DC)

    @scena.Lambda('lambda_2C2C')
    def lambda_2C2C():
        OP_7C(200, 0, 2000, 3000)
        Yield()

        Jump('lambda_2C2C')

    DispatchAsync2(0x0101, 0x0003, lambda_2C2C)

    Sleep(500)

    OP_62(0x0104, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ClearScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    CreateThread(0x000A, 0x01, 0x00, func_1D_398B)
    Sleep(200)

    CreateThread(0x000B, 0x01, 0x00, func_1F_3A7F)
    Sleep(200)

    CreateThread(0x000C, 0x01, 0x00, func_20_3AC8)
    Sleep(200)

    CreateThread(0x000D, 0x01, 0x00, func_21_3B42)
    Sleep(200)

    CreateThread(0x000F, 0x01, 0x00, func_22_3B7D)
    ChrSetDirection(0x0104, 140, 400)
    OP_62(0x0104, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x0104,
        (
            '#0040220389V#036F#6P噢噢……！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040220390V这、这个难道就是…\n',
            '那个雾香小姐的愤怒吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 140, 400)

    ChrTalk(
        0x0101,
        (
            '#0010220391V#1019F#5P那、那怎么可能嘛～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0105, 90, 400)

    ChrTalk(
        0x0105,
        (
            '#0060220392V#043F好像……是地震啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#3020220393V#5P救、救命呀～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 184, 400)
    ChrSetDirection(0x00F7, 65, 400)

    ChrTalk(
        0x000F,
        (
            '#3040220394V#2P要、要掉下去了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4A(0x0010, 255)
    ChrSetPos(0x0010, -45950, 0, 128050, 0)

    ChrTalk(
        0x0010,
        (
            '#1970220395V#2P各、各位！\n',
            '请镇定！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2E13')
    def lambda_2E13():
        CameraMove(-46130, -4000, 138120, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2E13)

    @scena.Lambda('lambda_2E2B')
    def lambda_2E2B():
        OP_67(0, 11000, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2E2B)

    @scena.Lambda('lambda_2E43')
    def lambda_2E43():
        CameraSetDistance(4480, 3000)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_2E43)

    @scena.Lambda('lambda_2E53')
    def lambda_2E53():
        OP_6C(230000, 3000)

        ExitThread()

    DispatchAsync(0x0104, 0x0002, lambda_2E53)

    ChrWalkTo(0x0010, -46090, -3250, 136100, 2000, 0x00)
    WaitForThreadExit(0x0101, 0x0001)

    @scena.Lambda('lambda_2E7C')
    def lambda_2E7C():
        ChrSetDirection(0x00FE, 184, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_2E7C)

    Sleep(100)

    @scena.Lambda('lambda_2E8F')
    def lambda_2E8F():
        ChrSetDirection(0x00FE, 184, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_2E8F)

    @scena.Lambda('lambda_2E9D')
    def lambda_2E9D():
        ChrSetDirection(0x00FE, 184, 400)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_2E9D)

    WaitForThreadExit(0x0104, 0x0001)

    ChrTalk(
        0x0010,
        (
            '#1970220396V#5P这个飞船坪的下层\n',
            '在设计时就强化了抗震能力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#1970220397V#5P这次地震的震级并不高，\n',
            '大家不用担心！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_24(0x0085, 0x5A)
    TerminateThread(0x0101, 0x03)

    @scena.Lambda('lambda_2F32')
    def lambda_2F32():
        OP_7C(100, 0, 1000, 1000)
        Yield()

        Jump('lambda_2F32')

    DispatchAsync2(0x0101, 0x0003, lambda_2F32)

    Sleep(500)

    OP_24(0x0085, 0x4B)
    Sleep(500)

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    OP_24(0x0085, 0x3C)
    TerminateThread(0x0101, 0x03)

    @scena.Lambda('lambda_2F66')
    def lambda_2F66():
        OP_7C(50, 0, 500, 1000)
        Yield()

        Jump('lambda_2F66')

    DispatchAsync2(0x0101, 0x0003, lambda_2F66)

    Sleep(500)

    TerminateThread(0x000C, 0x01)
    OP_4A(0x000C, 255)
    OP_24(0x0085, 0x32)
    Sleep(500)

    @scena.Lambda('lambda_2F97')
    def lambda_2F97():
        ChrTurnDirection(0x00FE, 0x0010, 200)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_2F97)

    OP_24(0x0085, 0x28)
    TerminateThread(0x0101, 0x03)

    @scena.Lambda('lambda_2FAD')
    def lambda_2FAD():
        OP_7C(25, 0, 250, 1000)
        Yield()

        Jump('lambda_2FAD')

    DispatchAsync2(0x0101, 0x0003, lambda_2FAD)

    Sleep(500)

    TerminateThread(0x000A, 0x01)
    OP_4A(0x000A, 255)
    OP_24(0x0085, 0x1E)
    Sleep(500)

    @scena.Lambda('lambda_2FDE')
    def lambda_2FDE():
        ChrTurnDirection(0x00FE, 0x0010, 200)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_2FDE)

    OP_24(0x0085, 0x14)
    TerminateThread(0x0101, 0x03)

    @scena.Lambda('lambda_2FF4')
    def lambda_2FF4():
        OP_7C(12, 0, 125, 1000)
        Yield()

        Jump('lambda_2FF4')

    DispatchAsync2(0x0101, 0x0003, lambda_2FF4)

    Sleep(500)

    TerminateThread(0x000B, 0x01)
    OP_4A(0x000B, 255)
    OP_24(0x0085, 0x0A)
    Sleep(500)

    @scena.Lambda('lambda_3025')
    def lambda_3025():
        ChrTurnDirection(0x00FE, 0x0010, 200)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_3025)

    OP_23(0x0085)
    TerminateThread(0x0101, 0x03)
    Sleep(500)

    TerminateThread(0x000D, 0x01)
    OP_4A(0x000D, 255)

    @scena.Lambda('lambda_3047')
    def lambda_3047():
        ChrTurnDirection(0x00FE, 0x0010, 200)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_3047)

    Sleep(500)

    TerminateThread(0x000F, 0x01)
    OP_4A(0x000F, 255)

    @scena.Lambda('lambda_3062')
    def lambda_3062():
        ChrTurnDirection(0x00FE, 0x0010, 200)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_3062)

    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010220398V#1025F#2P停、停了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#1970220399V#5P已、已经没事了吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#1970220400V#5P好了，各位。\n',
            '已经没事了，请不要惊慌。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3050220401V真是的……\n',
            '好久没遇到地震了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x000C, 400)
    ChrTurnDirection(0x000C, 0x000A, 400)

    ChrTalk(
        0x000A,
        (
            '#3030220402V#5P嘿嘿～还真是刺激啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    ChrSetDirection(0x0010, 180, 400)

    @scena.Lambda('lambda_3173')
    def lambda_3173():
        ChrWalkTo(0x00FE, -45970, 0, 126600, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_3173)

    Sleep(400)

    ChrSetDirection(0x000B, 180, 400)

    @scena.Lambda('lambda_319A')
    def lambda_319A():
        ChrMoveToRelative(0x00FE, 0, 0, -10000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_319A)

    Sleep(100)

    ChrSetDirection(0x000A, 180, 400)

    @scena.Lambda('lambda_31C1')
    def lambda_31C1():
        ChrMoveToRelative(0x00FE, 0, 0, -10000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_31C1)

    Sleep(200)

    ChrSetDirection(0x000C, 180, 400)

    @scena.Lambda('lambda_31E8')
    def lambda_31E8():
        ChrMoveToRelative(0x00FE, 0, 0, -10000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_31E8)

    Sleep(200)

    ChrSetDirection(0x000D, 180, 400)

    @scena.Lambda('lambda_320F')
    def lambda_320F():
        ChrMoveToRelative(0x00FE, 0, 0, -10000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_320F)

    Sleep(200)

    ChrSetDirection(0x000F, 180, 400)

    @scena.Lambda('lambda_3236')
    def lambda_3236():
        ChrMoveToRelative(0x00FE, 0, 0, -10000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_3236)

    Sleep(1500)

    @scena.Lambda('lambda_3256')
    def lambda_3256():
        CameraMove(-46690, -4000, 143590, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_3256)

    @scena.Lambda('lambda_326E')
    def lambda_326E():
        OP_67(0, 11000, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_326E)

    ChrSetDirection(0x0101, 45, 400)
    ChrSetDirection(0x00F7, 135, 400)
    ChrSetDirection(0x0105, 225, 400)
    ChrSetDirection(0x0104, 0, 400)
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)
    ChrSetFlags(0x0010, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000D, 0x0080)
    ChrSetFlags(0x000F, 0x0080)

    ChrTalk(
        0x0101,
        (
            '#0010220403V#1007F呼……吓死人了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010220404V#1019F虽然震得并不算强烈，\n',
            '但在这种不安全的地方发生摇晃，\n',
            '还真是危险呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060220405V#045F呵呵，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060220406V#043F不过利贝尔可是\n',
            '很少发生地震的啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040220407V#033F#5P哦，是这样吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_343C',
    )

    ChrTalk(
        0x0106,
        (
            '#0050220408V#053F#2P嗯……\n',
            '只有过极少的几次。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050220409V#050F我们要确认一下受害情况，\n',
            '赶快到协会去吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_34AD')

    def _loc_343C(): pass

    label('loc_343C')

    ChrTalk(
        0x0103,
        (
            '#0030220410V#026F#2P嗯……\n',
            '几乎从来没发生过呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030220411V#022F我们要确认一下受害情况，\n',
            '赶快到协会去吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_34AD(): pass

    label('loc_34AD')

    OP_4B(0x0010, 255)
    FadeOut(1500, 0, -1)
    OP_0D()
    Sleep(500)

    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/T3120._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0010 offset: 0x34CE
@scena.Code('func_10_34CE')
def func_10_34CE():
    @scena.Lambda('lambda_34D4')
    def lambda_34D4():
        ChrMoveTo(0x00FE, -34000, -11150, 148000, 500, 0x00)

        ExitThread()

    DispatchAsync(0x001B, 0x0001, lambda_34D4)

    @scena.Lambda('lambda_34EF')
    def lambda_34EF():
        ChrMoveTo(0x00FE, -34000, -7150, 148000, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x001A, 0x0001, lambda_34EF)

    WaitForThreadExit(0x001A, 0x0001)

    @scena.Lambda('lambda_350F')
    def lambda_350F():
        ChrMoveTo(0x00FE, -34000, -10150, 148000, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x001A, 0x0001, lambda_350F)

    WaitForThreadExit(0x001A, 0x0001)

    @scena.Lambda('lambda_352F')
    def lambda_352F():
        ChrMoveTo(0x00FE, -34000, -11150, 148000, 500, 0x00)

        ExitThread()

    DispatchAsync(0x001A, 0x0001, lambda_352F)

    WaitForThreadExit(0x001A, 0x0001)
    OP_23(0x0079)
    PlaySE(200, 0x00, 0x64)
    OP_7C(0, 100, 3000, 100)
    ChrSetPos(0x001A, -34000, -11150, 148000, 0)
    Sleep(1000)

    PlaySE(118, 0x00, 0x46)
    OP_6F(0x0004, 60)
    OP_70(0x0004, 1)
    Sleep(1100)

    PlaySE(120, 0x00, 0x64)
    OP_6F(0x0003, 100)
    OP_70(0x0003, 200)
    Sleep(2500)

    OP_6F(0x0004, 410)
    OP_70(0x0004, 460)
    PlaySE(6, 0x00, 0x64)
    Sleep(800)

    PlaySE(6, 0x00, 0x64)
    OP_73(0x0004)
    TerminateThread(0x0000, 0x01)

    Return()

# id: 0x0011 offset: 0x35CD
@scena.Code('func_11_35CD')
def func_11_35CD():
    ChrSetPos(0x00FE, -37500, -4000, 143810, 270)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -45890, -4000, 143810, 2000, 0x00)
    ChrWalkTo(0x00FE, -45890, 0, 128160, 2000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x0012 offset: 0x3611
@scena.Code('func_12_3611')
def func_12_3611():
    ChrSetPos(0x00FE, -37500, -4000, 143810, 270)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -45890, -4000, 143810, 2000, 0x00)
    ChrWalkTo(0x00FE, -47370, -4000, 139300, 2000, 0x00)
    ChrSetDirection(0x00FE, 135, 400)
    CreateThread(0x00FE, 0x03, 0x00, func_02_63A)

    Return()

# id: 0x0013 offset: 0x365E
@scena.Code('func_13_365E')
def func_13_365E():
    ChrSetPos(0x00FE, -37500, -4000, 143810, 270)
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetFlags(0x00FE, 0x0040)
    ChrWalkTo(0x00FE, -45890, -4000, 143810, 2000, 0x00)
    ChrWalkTo(0x00FE, -46600, -4000, 138330, 2000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)
    CreateThread(0x00FE, 0x03, 0x00, func_02_63A)

    Return()

# id: 0x0014 offset: 0x36B0
@scena.Code('func_14_36B0')
def func_14_36B0():
    ChrSetPos(0x00FE, -37500, -4000, 143810, 270)
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetFlags(0x00FE, 0x0040)
    ChrWalkTo(0x00FE, -45890, -4000, 143810, 2000, 0x00)
    ChrWalkTo(0x00FE, -46480, -4000, 139500, 2000, 0x00)
    ChrSetDirection(0x00FE, 180, 400)
    CreateThread(0x00FE, 0x03, 0x00, func_02_63A)

    Return()

# id: 0x0015 offset: 0x3702
@scena.Code('func_15_3702')
def func_15_3702():
    ChrSetPos(0x00FE, -37500, -4000, 143810, 270)
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetFlags(0x00FE, 0x0040)
    ChrWalkTo(0x00FE, -45890, -4000, 143810, 2000, 0x00)
    ChrWalkTo(0x00FE, -45710, -4000, 141560, 2000, 0x00)
    ChrWalkTo(0x00FE, -45210, -4000, 140000, 2000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)
    CreateThread(0x00FE, 0x03, 0x00, func_02_63A)

    Return()

# id: 0x0016 offset: 0x3768
@scena.Code('func_16_3768')
def func_16_3768():
    ChrSetPos(0x00FE, -37500, -4000, 143810, 270)
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetFlags(0x00FE, 0x0040)
    ChrWalkTo(0x00FE, -45890, -4000, 143810, 2000, 0x00)
    ChrWalkTo(0x00FE, -45710, -4000, 141560, 2000, 0x00)
    ChrWalkTo(0x00FE, -45150, -4000, 141000, 2000, 0x00)
    ChrSetDirection(0x00FE, 180, 400)
    CreateThread(0x00FE, 0x03, 0x00, func_02_63A)

    Return()

# id: 0x0017 offset: 0x37CE
@scena.Code('func_17_37CE')
def func_17_37CE():
    ChrSetPos(0x00FE, -37500, -4000, 143810, 270)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -45890, -4000, 143810, 2000, 0x00)

    Return()

# id: 0x0018 offset: 0x37F9
@scena.Code('func_18_37F9')
def func_18_37F9():
    ChrSetPos(0x00FE, -37500, -4000, 143810, 270)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -45890, -4000, 143810, 2000, 0x00)
    ChrWalkTo(0x0101, -47060, -4000, 143620, 2000, 0x00)
    ChrSetDirection(0x0101, 90, 400)

    Return()

# id: 0x0019 offset: 0x383F
@scena.Code('func_19_383F')
def func_19_383F():
    ChrSetPos(0x00FE, -37500, -4000, 143810, 270)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -45890, -4000, 143810, 2000, 0x00)
    ChrWalkTo(0x00F7, -46880, -4000, 144700, 2000, 0x00)
    ChrSetDirection(0x00F7, 135, 400)

    Return()

# id: 0x001A offset: 0x3885
@scena.Code('func_1A_3885')
def func_1A_3885():
    ChrSetPos(0x00FE, -37500, -4000, 143810, 270)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -45890, -4000, 143810, 2000, 0x00)
    ChrWalkTo(0x0105, -45700, -4000, 144400, 2000, 0x00)
    ChrSetDirection(0x0105, 270, 400)

    Return()

# id: 0x001B offset: 0x38CB
@scena.Code('func_1B_38CB')
def func_1B_38CB():
    ChrSetPos(0x00FE, -37500, -4000, 143810, 270)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -45890, -4000, 143810, 2000, 0x00)
    ChrWalkTo(0x0104, -45900, -4000, 143250, 2000, 0x00)
    ChrSetDirection(0x0104, 315, 400)

    Return()

# id: 0x001C offset: 0x3911
@scena.Code('func_1C_3911')
def func_1C_3911():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_398A',
    )

    OP_62(0x00FE, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_395F',
    )

    ChrMoveToRelative(0x00FE, 0, 0, -1500, 4000, 0x00)
    ChrMoveToRelative(0x00FE, 0, 0, 1500, 4000, 0x00)

    Jump('loc_3987')

    def _loc_395F(): pass

    label('loc_395F')

    ChrMoveToRelative(0x00FE, 0, 0, -1500, 2000, 0x00)
    ChrMoveToRelative(0x00FE, 0, 0, 1500, 2000, 0x00)

    def _loc_3987(): pass

    label('loc_3987')

    Jump('func_1C_3911')

    def _loc_398A(): pass

    label('loc_398A')

    Return()

# id: 0x001D offset: 0x398B
@scena.Code('func_1D_398B')
def func_1D_398B():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3A04',
    )

    OP_62(0x00FE, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_39D9',
    )

    ChrMoveToRelative(0x00FE, 0, 0, 1500, 4000, 0x00)
    ChrMoveToRelative(0x00FE, 0, 0, -1500, 4000, 0x00)

    Jump('loc_3A01')

    def _loc_39D9(): pass

    label('loc_39D9')

    ChrMoveToRelative(0x00FE, 0, 0, 1500, 2000, 0x00)
    ChrMoveToRelative(0x00FE, 0, 0, -1500, 2000, 0x00)

    def _loc_3A01(): pass

    label('loc_3A01')

    Jump('func_1D_398B')

    def _loc_3A04(): pass

    label('loc_3A04')

    Return()

# id: 0x001E offset: 0x3A05
@scena.Code('func_1E_3A05')
def func_1E_3A05():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3A7E',
    )

    OP_62(0x00FE, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3A53',
    )

    ChrMoveToRelative(0x00FE, 1500, 0, 1500, 4000, 0x00)
    ChrMoveToRelative(0x00FE, -1500, 0, -1500, 4000, 0x00)

    Jump('loc_3A7B')

    def _loc_3A53(): pass

    label('loc_3A53')

    ChrMoveToRelative(0x00FE, 1500, 0, 1500, 2000, 0x00)
    ChrMoveToRelative(0x00FE, -1500, 0, -1500, 2000, 0x00)

    def _loc_3A7B(): pass

    label('loc_3A7B')

    Jump('func_1E_3A05')

    def _loc_3A7E(): pass

    label('loc_3A7E')

    Return()

# id: 0x001F offset: 0x3A7F
@scena.Code('func_1F_3A7F')
def func_1F_3A7F():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3AC7',
    )

    OP_62(0x00FE, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrSetDirection(0x00FE, 315, 400)
    Sleep(300)

    OP_62(0x00FE, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrSetDirection(0x00FE, 0, 400)
    Sleep(300)

    Jump('func_1F_3A7F')

    def _loc_3AC7(): pass

    label('loc_3AC7')

    Return()

# id: 0x0020 offset: 0x3AC8
@scena.Code('func_20_3AC8')
def func_20_3AC8():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3B41',
    )

    OP_62(0x00FE, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3B16',
    )

    ChrMoveToRelative(0x00FE, 0, 0, 1500, 4000, 0x00)
    ChrMoveToRelative(0x00FE, 0, 0, -1500, 4000, 0x00)

    Jump('loc_3B3E')

    def _loc_3B16(): pass

    label('loc_3B16')

    ChrMoveToRelative(0x00FE, 0, 0, 1500, 2000, 0x00)
    ChrMoveToRelative(0x00FE, 0, 0, -1500, 2000, 0x00)

    def _loc_3B3E(): pass

    label('loc_3B3E')

    Jump('func_20_3AC8')

    def _loc_3B41(): pass

    label('loc_3B41')

    Return()

# id: 0x0021 offset: 0x3B42
@scena.Code('func_21_3B42')
def func_21_3B42():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3B7C',
    )

    OP_62(0x00FE, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrSetDirection(0x00FE, 90, 400)
    ChrSetDirection(0x00FE, 0, 400)
    ChrSetDirection(0x00FE, 270, 400)
    ChrSetDirection(0x00FE, 180, 400)

    Jump('func_21_3B42')

    def _loc_3B7C(): pass

    label('loc_3B7C')

    Return()

# id: 0x0022 offset: 0x3B7D
@scena.Code('func_22_3B7D')
def func_22_3B7D():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3BB7',
    )

    OP_62(0x00FE, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrSetDirection(0x00FE, 180, 400)
    ChrSetDirection(0x00FE, 270, 400)
    ChrSetDirection(0x00FE, 0, 400)
    ChrSetDirection(0x00FE, 90, 400)

    Jump('func_22_3B7D')

    def _loc_3BB7(): pass

    label('loc_3BB7')

    Return()

# id: 0x0023 offset: 0x3BB8
@scena.Code('func_23_3BB8')
def func_23_3BB8():
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
        'loc_3BD8',
    )

    Call(0, 0x002C)
    Call(0, 0x002D)
    FadeIn(0, 0)

    def _loc_3BD8(): pass

    label('loc_3BD8')

    Fade(1000)
    ChrSetPos(0x0101, -19580, 8000, 119820, 0)
    ChrSetPos(0x00F7, -20630, 8000, 119820, 0)
    ChrSetPos(0x00F8, -19710, 8000, 118700, 0)
    ChrSetPos(0x00F9, -20720, 8000, 118640, 0)
    CameraMove(-20180, 8000, 120530, 0)
    OP_67(0, 8780, -10000, 0)
    CameraSetDistance(3500, 0)
    OP_6C(315000, 0)
    OP_6E(194, 0)
    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 1, 0x1601)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_41B4',
    )

    SetScenaFlags(ScenaFlag(0x02C0, 1, 0x1601))

    ChrTalk(
        0x0010,
        (
            '#1970240214V哟，欢迎光临。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#1970240215V你们就是要前往格兰赛尔\n',
            '的游击士们吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220147V#1011F啊，嗯，是的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#1970240217V雾香小姐已经\n',
            '支付了船票费用，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#1970240218V现在要办乘船手续吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00F7, 0x0101, 400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_3DC4',
    )

    ChrTalk(
        0x0106,
        (
            '#0050220150V#050F如果办好了手续，那在船到之前\n',
            '在这里等着就可以了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050240220V在蔡斯地区的事情\n',
            '没有事留下了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3E43')

    def _loc_3DC4(): pass

    label('loc_3DC4')

    ChrTalk(
        0x0103,
        (
            '#0030220152V#020F如果办好了手续，那在船到之前\n',
            '在这里等着就可以了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030240222V在蔡斯地区\n',
            '已经没有什么事情还需要做的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3E43(): pass

    label('loc_3E43')

    If(
        (
            (Expr.Eval, "OP_29(0x006F, 0x00, 0x08)"),
            (Expr.Eval, "OP_29(0x006F, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x006F, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_40E5',
    )

    ChrTalk(
        0x0101,
        (
            '#0010240223V#1015F啊，说起来的话……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240224V探测器好像\n',
            '还没还呢。',
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
        'loc_3EED',
    )

    ChrTalk(
        0x0107,
        (
            '#0070240225V#560F是『合金探测器』吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0107, 400)

    Jump('loc_3F76')

    def _loc_3EED(): pass

    label('loc_3EED')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3F30',
    )

    ChrTalk(
        0x0104,
        (
            '#0040240226V#030F是『合金探测器』呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0104, 400)

    Jump('loc_3F76')

    def _loc_3F30(): pass

    label('loc_3F30')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3F76',
    )

    ChrTalk(
        0x0105,
        (
            '#0060240227V#542F就是那个『合金探测器』吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0105, 400)

    def _loc_3F76(): pass

    label('loc_3F76')

    ChrTalk(
        0x0101,
        (
            '#0010240228V#1006F对对，就是那个。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240229V是在中央工房\n',
            '一楼的维修柜台\n',
            '借来的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_402D',
    )

    ChrTalk(
        0x0106,
        (
            '#0050240230V#051F工房一楼的维修柜台吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050240231V好，那我们就快点去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_407A')

    def _loc_402D(): pass

    label('loc_402D')

    ChrTalk(
        0x0103,
        (
            '#0030240232V#020F工房一楼的维修柜台吗，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030240233V那我们就赶快去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_407A(): pass

    label('loc_407A')

    ChrTalk(
        0x0010,
        (
            '#1970240234V那么，等你们的事情办完了\n',
            '再到这里找我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(500)
    OP_67(0, 11000, -10000, 0)
    CameraSetDistance(3500, 0)
    OP_6E(262, 0)
    EventEnd(0x00)

    Return()

    def _loc_40E5(): pass

    label('loc_40E5')

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
            TXT(0x00, '【还有事情】\n'),
            TXT(0x01, '【办理乘船手续】\n'),
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

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_41B1',
    )

    ChrTalk(
        0x0010,
        (
            '#1970240234V那么，等你们的事情办完了\n',
            '再到这里找我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(500)
    CameraSetDistance(3500, 0)
    OP_67(0, 11000, -10000, 0)
    OP_6E(262, 0)
    EventEnd(0x00)

    Return()

    def _loc_41B1(): pass

    label('loc_41B1')

    Jump('loc_437B')

    def _loc_41B4(): pass

    label('loc_41B4')

    ChrTalk(
        0x0010,
        (
            '#1970240236V哦。\n',
            '要办理乘船手续吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x006F, 0x00, 0x08)"),
            (Expr.Eval, "OP_29(0x006F, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x006F, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_42AF',
    )

    ChrTalk(
        0x0101,
        (
            '#0010240223V#1015F啊，说起来的话……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240238V合金探测器\n',
            '还没还呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#1970240234V那么，等你们的事情办完了\n',
            '再到这里找我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(500)
    CameraSetDistance(3500, 0)
    OP_67(0, 11000, -10000, 0)
    OP_6E(262, 0)
    EventEnd(0x00)

    Return()

    def _loc_42AF(): pass

    label('loc_42AF')

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
            TXT(0x00, '【还有事情】\n'),
            TXT(0x01, '【办理乘船手续】\n'),
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

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_437B',
    )

    ChrTalk(
        0x0010,
        (
            '#1970240234V那么，等你们的事情办完了\n',
            '再到这里找我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(500)
    CameraSetDistance(3500, 0)
    OP_67(0, 11000, -10000, 0)
    OP_6E(262, 0)
    EventEnd(0x00)

    Return()

    def _loc_437B(): pass

    label('loc_437B')

    ChrTalk(
        0x0010,
        (
            '#1970240241V明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#1970240242V那么，就去协会\n',
            '联络其他的同伴吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    TalkSetChrName('')
    SetMessageWindowPos(72, 320, 56, 3)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔一行人办理完乘船手续之后\n',
            '就在原地等待飞船起飞。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(500)

    OP_C0(0x15, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)
    ChrSetFlags(0x0012, 0x0080)
    ChrSetFlags(0x0014, 0x0080)
    ChrSetFlags(0x0015, 0x0080)
    ChrSetFlags(0x0016, 0x0080)
    ChrSetFlags(0x0019, 0x0080)
    Call(0, 0x0024)

    Return()

# id: 0x0024 offset: 0x446B
@scena.Code('func_24_446B')
def func_24_446B():
    EventBegin(0x00)
    OP_DB()

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_4493',
    )

    FormationAddMember(ChrTable['奥利维尔'], 0xFA, 0xFF)

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_4493(): pass

    label('loc_4493')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_44BD',
    )

    If(
        (
            (Expr.PushReg, 0x2),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_44B9',
    )

    FormationAddMember(ChrTable['科洛丝'], 0xFA, 0xFF)

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    Jump('loc_44BD')

    def _loc_44B9(): pass

    label('loc_44B9')

    FormationAddMember(ChrTable['科洛丝'], 0xFB, 0xFF)

    def _loc_44BD(): pass

    label('loc_44BD')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_44E7',
    )

    If(
        (
            (Expr.PushReg, 0x2),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_44E3',
    )

    FormationAddMember(ChrTable['提妲'], 0xFA, 0xFF)

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    Jump('loc_44E7')

    def _loc_44E3(): pass

    label('loc_44E3')

    FormationAddMember(ChrTable['提妲'], 0xFB, 0xFF)

    def _loc_44E7(): pass

    label('loc_44E7')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_4511',
    )

    If(
        (
            (Expr.PushReg, 0x2),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_450D',
    )

    FormationAddMember(ChrTable['金'], 0xFA, 0xFF)

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    Jump('loc_4511')

    def _loc_450D(): pass

    label('loc_450D')

    FormationAddMember(ChrTable['金'], 0xFB, 0xFF)

    def _loc_4511(): pass

    label('loc_4511')

    OP_72(0x0003, 0x0004)
    OP_72(0x0004, 0x0004)
    OP_72(0x0005, 0x0004)
    OP_6F(0x0004, 100)
    OP_6F(0x0003, 100)
    ChrSetPos(0x0101, -46010, -4000, 151140, 14)
    ChrSetPos(0x00F7, -47050, -4000, 152510, 87)
    ChrSetPos(0x0107, -47040, -4000, 153400, 87)
    ChrSetPos(0x0105, -45400, -4000, 151930, 267)
    ChrSetPos(0x0104, -45280, -4000, 153160, 267)
    ChrSetPos(0x0108, -46100, -4000, 154080, 177)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x0008, -46990, -4000, 147520, 177)
    ChrSetPos(0x0009, -46840, -4000, 144960, 357)
    ChrSetPos(0x000A, -46720, -4000, 146170, 87)
    ChrSetPos(0x000B, -46700, -4000, 148750, 177)
    ChrSetPos(0x000C, -46590, -4000, 149930, 177)
    ChrSetPos(0x000D, -45070, -3800, 144000, 87)
    ChrSetPos(0x000E, -46280, -4000, 143940, 87)
    CameraMove(-42120, -4000, 150190, 0)
    OP_67(0, 8330, -10000, 0)
    CameraSetDistance(3500, 0)
    OP_6C(62000, 0)
    OP_6E(331, 0)
    ChrSetPos(0x001A, -34000, -11150, 148000, 0)
    OP_A1(0x001A, 0x0004)
    OP_72(0x0004, 0x0004)
    ChrSetFlags(0x001A, 0x0004)
    OP_A1(0x001B, 0x0005)
    ChrSetPos(0x001B, -34000, -11150, 148000, 0)
    OP_72(0x0005, 0x0004)
    ChrSetFlags(0x001B, 0x0004)
    OP_6F(0x0004, 60)
    OP_71(0x0006, 0x0004)
    PlaySE(226, 0x00, 0x64)
    PlaySE(117, 0x00, 0x64)
    Sleep(3000)

    PlaySE(200, 0x00, 0x64)
    OP_7C(0, 100, 3000, 100)
    Sleep(1000)

    FadeIn(2000, 0)
    OP_0D()
    PlaySE(118, 0x00, 0x46)
    OP_6F(0x0004, 60)
    OP_70(0x0004, 1)
    Sleep(1100)

    PlaySE(120, 0x00, 0x64)
    OP_6F(0x0003, 100)
    OP_70(0x0003, 200)
    Sleep(2500)

    CreateThread(0x000D, 0x01, 0x00, func_25_4B61)
    Sleep(500)

    CreateThread(0x000E, 0x01, 0x00, func_26_4B8F)
    Sleep(800)

    CreateThread(0x0009, 0x01, 0x00, func_27_4BBD)
    CreateThread(0x000A, 0x01, 0x00, func_27_4BBD)
    Sleep(600)

    CreateThread(0x0008, 0x01, 0x00, func_28_4BFF)
    Sleep(500)

    CreateThread(0x000B, 0x01, 0x00, func_29_4C41)
    Sleep(500)

    CreateThread(0x000C, 0x01, 0x00, func_28_4BFF)
    Sleep(600)

    ChrSetDirection(0x0101, 225, 400)
    CreateThread(0x0101, 0x01, 0x00, func_2A_4C83)
    Sleep(300)

    ChrSetDirection(0x00F7, 180, 400)
    CreateThread(0x00F7, 0x01, 0x00, func_2A_4C83)
    Sleep(300)

    ChrSetDirection(0x0107, 180, 400)
    CreateThread(0x0107, 0x01, 0x00, func_2A_4C83)
    Sleep(300)

    ChrSetDirection(0x0105, 225, 400)
    Sleep(1200)

    CreateThread(0x0105, 0x01, 0x00, func_2A_4C83)
    Sleep(500)

    FadeOut(2000, 0, -1)
    CreateThread(0x0104, 0x01, 0x00, func_2A_4C83)
    Sleep(500)

    CreateThread(0x0108, 0x01, 0x00, func_2A_4C83)
    Sleep(1000)

    OP_0D()
    CameraMove(-33540, -6900, 151660, 0)
    OP_67(0, 600, -10000, 0)
    CameraSetDistance(4360, 0)
    OP_6C(169000, 0)
    OP_6E(425, 0)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x00F7, 0x01)
    TerminateThread(0x00F8, 0x01)
    TerminateThread(0x00F9, 0x01)
    TerminateThread(0x00FA, 0x01)
    TerminateThread(0x00FB, 0x01)
    TerminateThread(0x0008, 0x01)
    TerminateThread(0x0009, 0x01)
    TerminateThread(0x000A, 0x01)
    TerminateThread(0x000B, 0x01)
    TerminateThread(0x000C, 0x01)
    TerminateThread(0x000D, 0x01)
    TerminateThread(0x000E, 0x01)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x00F7, 0x0080)
    ChrSetFlags(0x00F8, 0x0080)
    ChrSetFlags(0x00F9, 0x0080)
    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000D, 0x0080)
    ChrSetFlags(0x000E, 0x0080)
    Sleep(1000)

    PlaySE(226, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_489B')
    def lambda_489B():
        OP_67(0, 3030, -10000, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_489B)

    FadeIn(2000, 0)
    OP_0D()
    Fade(500)
    OP_72(0x0006, 0x0004)
    OP_0D()
    PlaySE(120, 0x00, 0x64)
    OP_6F(0x0003, 0)
    OP_70(0x0003, 100)
    Sleep(1000)

    PlaySE(118, 0x00, 0x46)
    OP_6F(0x0004, 1)
    OP_70(0x0004, 60)
    OP_73(0x0004)
    Sleep(1000)

    PlaySE(119, 0x01, 0x64)
    OP_6F(0x0004, 61)
    OP_70(0x0004, 160)
    OP_73(0x0004)
    OP_71(0x0004, 0x0020)
    OP_6F(0x0004, 161)
    OP_70(0x0004, 260)
    OP_23(0x0075)
    ChrMoveToRelativeAsync(0x001A, 0, 300, 0, 300, 0x00)
    ChrMoveToRelativeAsync(0x001A, 0, 800, 0, 500, 0x00)
    Sleep(2000)

    @scena.Lambda('lambda_4954')
    def lambda_4954():
        CameraMove(-33490, -6100, 161910, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4954)

    @scena.Lambda('lambda_496C')
    def lambda_496C():
        OP_67(0, 3180, -10000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_496C)

    @scena.Lambda('lambda_4984')
    def lambda_4984():
        OP_94(0x01, 0x00FE, 0x0000, 0x000003E8, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x001B, 0x0001, lambda_4984)

    OP_94(0x01, 0x001A, 0x0000, 0x000003E8, 0x000003E8, 0x00)

    @scena.Lambda('lambda_49A9')
    def lambda_49A9():
        OP_94(0x01, 0x00FE, 0x0000, 0x000004B0, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x001B, 0x0001, lambda_49A9)

    OP_94(0x01, 0x001A, 0x0000, 0x000004B0, 0x000007D0, 0x00)

    @scena.Lambda('lambda_49CE')
    def lambda_49CE():
        OP_94(0x01, 0x00FE, 0x0000, 0x00000578, 0x00000BB8, 0x00)

        ExitThread()

    DispatchAsync(0x001B, 0x0001, lambda_49CE)

    OP_94(0x01, 0x001A, 0x0000, 0x00000578, 0x00000BB8, 0x00)

    @scena.Lambda('lambda_49F3')
    def lambda_49F3():
        OP_94(0x01, 0x00FE, 0x0000, 0x00000640, 0x00000FA0, 0x00)

        ExitThread()

    DispatchAsync(0x001B, 0x0001, lambda_49F3)

    OP_94(0x01, 0x001A, 0x0000, 0x00000640, 0x00000FA0, 0x00)

    @scena.Lambda('lambda_4A18')
    def lambda_4A18():
        OP_94(0x01, 0x00FE, 0x0000, 0x00000708, 0x00001388, 0x00)

        ExitThread()

    DispatchAsync(0x001B, 0x0001, lambda_4A18)

    FadeOut(2000, 0, -1)
    OP_94(0x01, 0x001A, 0x0000, 0x00000708, 0x00001388, 0x00)

    @scena.Lambda('lambda_4A47')
    def lambda_4A47():
        OP_94(0x01, 0x00FE, 0x0000, 0x000007D0, 0x00001770, 0x00)

        ExitThread()

    DispatchAsync(0x001B, 0x0001, lambda_4A47)

    OP_94(0x01, 0x001A, 0x0000, 0x000007D0, 0x00001770, 0x00)

    @scena.Lambda('lambda_4A6C')
    def lambda_4A6C():
        OP_94(0x01, 0x00FE, 0x0000, 0x00000898, 0x00001B58, 0x00)

        ExitThread()

    DispatchAsync(0x001B, 0x0001, lambda_4A6C)

    OP_94(0x01, 0x001A, 0x0000, 0x00000898, 0x00001B58, 0x00)

    @scena.Lambda('lambda_4A91')
    def lambda_4A91():
        OP_94(0x01, 0x00FE, 0x0000, 0x0000C350, 0x00001F40, 0x00)

        ExitThread()

    DispatchAsync(0x001B, 0x0001, lambda_4A91)

    @scena.Lambda('lambda_4AA7')
    def lambda_4AA7():
        OP_94(0x01, 0x00FE, 0x0000, 0x0000C350, 0x00001F40, 0x00)

        ExitThread()

    DispatchAsync(0x001A, 0x0001, lambda_4AA7)

    OP_24(0x0077, 0x5A)
    Sleep(100)

    OP_24(0x0077, 0x50)
    Sleep(100)

    OP_24(0x0077, 0x46)
    Sleep(100)

    OP_24(0x0077, 0x3C)
    Sleep(100)

    OP_24(0x0077, 0x32)
    Sleep(100)

    OP_24(0x0077, 0x28)
    Sleep(100)

    OP_24(0x0077, 0x1E)
    Sleep(100)

    OP_24(0x0077, 0x14)
    Sleep(100)

    OP_24(0x0077, 0x0A)
    Sleep(100)

    OP_23(0x0077)
    OP_0D()
    FormationDelMember(0x03, 0xFF)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x06, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x07, 0xFF)
    SetScenaFlags(ScenaFlag(0x02C0, 2, 0x1602))
    SetScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    OP_28(0x006C, 0x04, 0x40)
    OP_28(0x006D, 0x04, 0x40)
    OP_28(0x006E, 0x04, 0x40)
    OP_28(0x006F, 0x04, 0x40)
    OP_28(0x0070, 0x04, 0x40)
    OP_28(0x0071, 0x04, 0x40)
    OP_28(0x00A5, 0x04, 0x40)
    OP_28(0x00A6, 0x04, 0x40)
    OP_28(0x00A7, 0x04, 0x40)
    OP_28(0x00A8, 0x04, 0x40)
    OP_DC()
    NewScene('ED6_DT21/E0001._SN', 104, 0, 0)
    IdleLoop()

    Return()

# id: 0x0025 offset: 0x4B61
@scena.Code('func_25_4B61')
def func_25_4B61():
    ChrSetFlags(0x00FE, 0x0040)
    ChrWalkTo(0x00FE, -34680, -4000, 143750, 2000, 0x00)
    ChrWalkTo(0x00FE, -31280, -4000, 149160, 2000, 0x00)

    Return()

# id: 0x0026 offset: 0x4B8F
@scena.Code('func_26_4B8F')
def func_26_4B8F():
    ChrSetFlags(0x00FE, 0x0040)
    ChrWalkTo(0x00FE, -32110, -4000, 143750, 2000, 0x00)
    ChrWalkTo(0x00FE, -31280, -4000, 149160, 2000, 0x00)

    Return()

# id: 0x0027 offset: 0x4BBD
@scena.Code('func_27_4BBD')
def func_27_4BBD():
    ChrSetFlags(0x00FE, 0x0040)
    ChrWalkTo(0x00FE, -46140, -4000, 144110, 2000, 0x00)
    ChrWalkTo(0x00FE, -33110, -4000, 143750, 2000, 0x00)
    ChrWalkTo(0x00FE, -31280, -4000, 149160, 2000, 0x00)

    Return()

# id: 0x0028 offset: 0x4BFF
@scena.Code('func_28_4BFF')
def func_28_4BFF():
    ChrSetFlags(0x00FE, 0x0040)
    ChrWalkTo(0x00FE, -46820, -4000, 143950, 2000, 0x00)
    ChrWalkTo(0x00FE, -33210, -4000, 143690, 2000, 0x00)
    ChrWalkTo(0x00FE, -31280, -4000, 149160, 2000, 0x00)

    Return()

# id: 0x0029 offset: 0x4C41
@scena.Code('func_29_4C41')
def func_29_4C41():
    ChrSetFlags(0x00FE, 0x0040)
    ChrWalkTo(0x00FE, -46820, -4000, 143950, 2000, 0x00)
    ChrWalkTo(0x00FE, -33610, -4000, 143690, 2000, 0x00)
    ChrWalkTo(0x00FE, -31280, -4000, 149160, 2000, 0x00)

    Return()

# id: 0x002A offset: 0x4C83
@scena.Code('func_2A_4C83')
def func_2A_4C83():
    ChrWalkTo(0x00FE, -46870, -4000, 149030, 2000, 0x00)
    ChrWalkTo(0x00FE, -46680, -4000, 144140, 2000, 0x00)
    ChrWalkTo(0x00FE, -34500, -4000, 144110, 2000, 0x00)

    Return()

# id: 0x002B offset: 0x4CC0
@scena.Code('func_2B_4CC0')
def func_2B_4CC0():
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
        'loc_4CE0',
    )

    Call(0, 0x002C)
    Call(0, 0x002E)
    FadeIn(0, 0)

    def _loc_4CE0(): pass

    label('loc_4CE0')

    Fade(1000)
    CameraMove(-38930, 8000, 126550, 0)
    OP_67(0, 5300, -10000, 0)
    CameraSetDistance(3750, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, -39260, 8000, 127280, 0)
    ChrSetPos(0x0102, -40320, 8000, 127230, 0)
    ChrSetPos(0x00F8, -39030, 8000, 126180, 0)
    ChrSetPos(0x00F9, -40150, 8000, 126180, 0)
    OP_4A(0x0018, 255)
    ChrSetSubChip(0x0018, 0)
    ChrSetDirection(0x0018, 180, 0)
    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 4, 0x2084)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Ez,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0401, 7, 0x200F)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5047',
    )

    ChrTalk(
        0x0018,
        (
            '#0560370379V#692F#6P啊，我还说是谁，\n',
            '这不是艾丝蒂尔吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370380V#1025F#5P维修长先生，好久不见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020370381V#1040F#2P好久不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '#0560370382V#691F#6P噢！这不是约修亚吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560370383V怎么回事，好像\n',
            '有很久没见了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370384V#1016F#5P算了，稍微\n',
            '说来话长了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010370385V#1015F……嗯，工房长先生那边\n',
            '现在的情况怎么样了？',
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
        'loc_4F2B',
    )

    ChrTalk(
        0x0107,
        (
            '#0070370386V#063F#2P为什么会发生\n',
            '骚乱的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4F2B(): pass

    label('loc_4F2B')

    ChrTalk(
        0x0018,
        (
            '#0560370387V#691F#6P异常发生的当时\n',
            '确实不得了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560370388V总之城里的情况已经算是\n',
            '稳定下来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020370389V#1035F#2P是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020370390V#1040F总算是从\n',
            '混乱中摆脱了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '#0560370391V#691F#6P啊啊，是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560370392V那个暂且不说……\n',
            '这次来是有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))
    SetScenaFlags(ScenaFlag(0x0410, 4, 0x2084))

    Jump('loc_5268')

    def _loc_5047(): pass

    label('loc_5047')

    ChrTalk(
        0x0018,
        (
            '#0560370393V#691F#6P噢，是你们吗。\n',
            '还是和以前一样，总那么忙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370394V#1016F#5P啊哈哈……\n',
            '维修长先生也是一样啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020370395V#1040F#2P您辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '#0560370396V#690F#6P呵呵，忙虽然是忙，\n',
            '但特殊情况也没办法……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560370397V机械这东西，\n',
            '一点疏忽也都会要了命，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560370398V只能打起精神撑下去啦。',
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
        'loc_51C4',
    )

    ChrTalk(
        0x0107,
        (
            '#0070370399V#063F#2P那、那确实\n',
            '很辛苦呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_51C4(): pass

    label('loc_51C4')

    ChrTalk(
        0x0101,
        (
            '#0010370400V#1015F#5P嗯～和我\n',
            '学习棒术时的感觉\n',
            '应该很相似吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '#0560370401V#691F#6P哈，应该差不多吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560370402V那个暂且不说……\n',
            '你们这次来有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_5268(): pass

    label('loc_5268')

    ChrTalk(
        0x0102,
        (
            '#0020370403V#1040F#2P是的，其实……',
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
            '向格斯塔夫维修长说明了\n',
            '要借内燃引擎用的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0018,
        (
            '#0560370404V#692F#6P原来如此……\n',
            '真是个好主意啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560370405V#690F那东西只能驱动单体机械，\n',
            '现在已经没什么用了，\n',
            '可以的话借你们也没问题，可是…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_53B3',
    )

    ChrTalk(
        0x0106,
        (
            '#0050370406V#052F#2P有什么问题吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_542A')

    def _loc_53B3(): pass

    label('loc_53B3')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_53EC',
    )

    ChrTalk(
        0x0103,
        (
            '#0030370407V#023F#2P有什么问题吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_542A')

    def _loc_53EC(): pass

    label('loc_53EC')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_542A',
    )

    ChrTalk(
        0x0108,
        (
            '#0080370408V#073F#2P看起来似乎有些问题啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_542A(): pass

    label('loc_542A')

    ChrTalk(
        0x0018,
        (
            '#0560370409V#690F#6P这个嘛……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560370410V真是不巧，已经\n',
            '借给王国军了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560370411V就在上次『埃尔赛尤』\n',
            '改装引擎的时候。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370412V#1015F#5P是吗……',
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
        'loc_5521',
    )

    ChrTalk(
        0x0107,
        (
            '#0070370413V#064F#2P那也就是说，那东西现在\n',
            '在雷斯顿要塞吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_555F')

    def _loc_5521(): pass

    label('loc_5521')

    ChrTalk(
        0x0102,
        (
            '#0020370414V#1044F#2P那么，那东西现在\n',
            '在雷斯顿要塞对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_555F(): pass

    label('loc_555F')

    ChrTalk(
        0x0018,
        (
            '#0560370415V#691F#6P啊啊，就是那样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560370416V不好意思，如果一定要借的话，\n',
            '就只能请你们自己去要了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560370417V像现在这种状态，\n',
            '连通信器也没办法使用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370418V#1006F#5P嗯，好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020370419V#1040F#2P嗯，我们会尝试和雷斯顿要塞\n',
            '那边联络的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0401, 3, 0x200B))
    OP_28(0x00C2, 0x01, 0x0008)

    @scena.Lambda('lambda_5677')
    def lambda_5677():
        ChrSetDirection(0x0018, 0, 400)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_5677)

    OP_4B(0x0018, 255)
    EventEnd(0x00)

    Return()

# id: 0x002C offset: 0x5686
@scena.Code('func_2C_5686')
def func_2C_5686():
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
        (0x00000000, 'loc_5700'),
        (0x00000001, 'loc_5706'),
        (-1, 'loc_570C'),
    )

    def _loc_5700(): pass

    label('loc_5700')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_570C')

    def _loc_5706(): pass

    label('loc_5706')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_570C')

    def _loc_570C(): pass

    label('loc_570C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_571A',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    Jump('loc_571E')

    def _loc_571A(): pass

    label('loc_571A')

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    def _loc_571E(): pass

    label('loc_571E')

    Return()

# id: 0x002D offset: 0x571F
@scena.Code('func_2D_571F')
def func_2D_571F():
    MapClearFlags(0x00000001)
    CameraMove(0, 0, 0, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_575D',
    )

    FadeIn(0, 0)

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['雪拉扎德'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['奥利维尔'],
            ChrTable['科洛丝'],
            ChrTable['提妲'],
            ChrTable['金'],
            0xFFFF,
        ),
    )

    Jump('loc_577B')

    def _loc_575D(): pass

    label('loc_575D')

    FadeIn(0, 0)

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['阿加特'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['奥利维尔'],
            ChrTable['科洛丝'],
            ChrTable['提妲'],
            ChrTable['金'],
            0xFFFF,
        ),
    )

    def _loc_577B(): pass

    label('loc_577B')

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0)

    Return()

# id: 0x002E offset: 0x578D
@scena.Code('func_2E_578D')
def func_2E_578D():
    MapClearFlags(0x00000001)
    CameraMove(106730, -1920, 53920, 0)
    Sleep(100)

    FadeIn(0, 0)

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['约修亚'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['阿加特'],
            ChrTable['雪拉扎德'],
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

# id: 0x002F offset: 0x57E6
@scena.Code('func_2F_57E6')
def func_2F_57E6():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '定期船起降坪\n',
            '≡　开往王都格兰赛尔\n',
            '≡　前往卢安市',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※请勿携带易燃物和危险品\n',
            '　　　　『利贝尔飞船公社』',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0030 offset: 0x5882
@scena.Code('func_30_5882')
def func_30_5882():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '　　　飞船坪塔台　　　　\n',
            '　※无关人员禁止入内　　\n',
            ' 『利贝尔飞船公社』　',
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
