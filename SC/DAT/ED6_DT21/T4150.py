import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T4150_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4150   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4150.x'
    header.mapIndex       = 1
    header.bgm            = 34
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
        ('ED6_DT07/CH02320._CH', 'ED6_DT07/CH02320P._CP'),
        ('ED6_DT26/CH20238._CH', 'ED6_DT26/CH20238P._CP'),
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH01220._CH', 'ED6_DT07/CH01220P._CP'),
        ('ED6_DT07/CH01460._CH', 'ED6_DT07/CH01460P._CP'),
        ('ED6_DT07/CH01130._CH', 'ED6_DT07/CH01130P._CP'),
        ('ED6_DT07/CH01680._CH', 'ED6_DT07/CH01680P._CP'),
        ('ED6_DT07/CH01690._CH', 'ED6_DT07/CH01690P._CP'),
        ('ED6_DT07/CH01120._CH', 'ED6_DT07/CH01120P._CP'),
        ('ED6_DT07/CH01150._CH', 'ED6_DT07/CH01150P._CP'),
        ('ED6_DT26/CH20254._CH', 'ED6_DT26/CH20254P._CP'),
        ('ED6_DT07/CH01200._CH', 'ED6_DT07/CH01200P._CP'),
    ]

# id: 0x10001 offset: 0x112
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '基库',
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
            name                = '士兵',
            x                   = 6280,
            z                   = 0,
            y                   = 2180,
            direction           = 215,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = -6430,
            z                   = 0,
            y                   = -22020,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 4760,
            z                   = 0,
            y                   = -39600,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = -4540,
            z                   = 0,
            y                   = -29870,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '村中的中年男性',
            x                   = -6250,
            z                   = 0,
            y                   = -870,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            name                = '贵族青年',
            x                   = -6250,
            z                   = 0,
            y                   = -1920,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            name                = '船员',
            x                   = -8540,
            z                   = 250,
            y                   = 6040,
            direction           = 172,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            name                = '城中中年妇女',
            x                   = -8540,
            z                   = 250,
            y                   = 4630,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            name                = '街上中年男人２',
            x                   = -5690,
            z                   = 0,
            y                   = -7580,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '街上中年女人２',
            x                   = 13060,
            z                   = 250,
            y                   = 4130,
            direction           = 51,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0011,
        ),
        ScenaNpcData(
            name                = '街上中年男人',
            x                   = -8230,
            z                   = 250,
            y                   = -31580,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0012,
        ),
        ScenaNpcData(
            name                = '街上青年女人',
            x                   = 7330,
            z                   = 250,
            y                   = -27330,
            direction           = 37,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            name                = '伯登',
            x                   = 5760,
            z                   = 0,
            y                   = -46060,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0005,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0014,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 4760,
            z                   = 0,
            y                   = -39600,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0006,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0015,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = -4540,
            z                   = 0,
            y                   = -29870,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0007,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0016,
        ),
        ScenaNpcData(
            name                = '王都格兰赛尔·北街区',
            x                   = 10,
            z                   = 250,
            y                   = 36990,
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
            name                = '庭园大道方向',
            x                   = -50,
            z                   = 0,
            y                   = -90220,
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
            name                = '王都格兰赛尔·东街区',
            x                   = 54990,
            z                   = 0,
            y                   = -1130,
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
            name                = '王都格兰赛尔·西街区',
            x                   = -44420,
            z                   = 0,
            y                   = -19990,
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

# id: 0x10002 offset: 0x392
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x392
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -5000,
            y           = -2000,
            z           = -65600,
            range       = 5000,
            dword_10    = 0x000007D0,
            dword_14    = 0xFFFF0344,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000018,
        ),
        ScenaEventData(
            x           = 9240,
            y           = 0,
            z           = -25000,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000023,
        ),
        ScenaEventData(
            x           = -10280,
            y           = 0,
            z           = -11040,
            range       = 1500,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000024,
        ),
        ScenaEventData(
            x           = -14940,
            y           = 0,
            z           = -15750,
            range       = 1500,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000024,
        ),
        ScenaEventData(
            x           = -10290,
            y           = 0,
            z           = -30020,
            range       = 1500,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000025,
        ),
        ScenaEventData(
            x           = 9240,
            y           = 0,
            z           = -13010,
            range       = 1500,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000026,
        ),
        ScenaEventData(
            x           = 15900,
            y           = 0,
            z           = 6330,
            range       = 1500,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000027,
        ),
    )

# id: 0x10004 offset: 0x472
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x472
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_488',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    MapSetFlags(0x10000000)
    Event(0, func_1E_23E3)

    Jump('loc_4B5')

    def _loc_488(): pass

    label('loc_488')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_494'),
        (-1, 'loc_4B5'),
    )

    def _loc_494(): pass

    label('loc_494')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 0, 0x1638)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 1, 0x1639)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4B2',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x54),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MapSetFlags(0x10000000)
    Event(0, func_17_BD6)

    def _loc_4B2(): pass

    label('loc_4B2')

    Jump('loc_4B5')

    def _loc_4B5(): pass

    label('loc_4B5')

    ExecExpressionWithValue(
        0x0008,
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

# id: 0x0001 offset: 0x4C7
@scena.Code('func_01_4C7')
def func_01_4C7():
    OP_16(0x02, 4000, -128000, -148000, 2293851)
    OP_71(0x0002, 0x0010)
    OP_71(0x0000, 0x0010)
    OP_71(0x0003, 0x0010)
    OP_71(0x000D, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 2, 0x163A)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_503',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x54),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_503(): pass

    label('loc_503')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_524',
    )

    OP_1B(0x0A, 0x00, 0x001C)
    OP_1B(0x0B, 0x00, 0x0019)
    OP_1B(0x0C, 0x00, 0x001A)
    OP_1B(0x0D, 0x00, 0x0019)
    OP_1B(0x0E, 0x00, 0x001B)

    def _loc_524(): pass

    label('loc_524')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 1, 0x1639)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 2, 0x163A)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_535',
    )

    OP_1B(0x09, 0x00, 0x001D)

    def _loc_535(): pass

    label('loc_535')

    Return()

# id: 0x0002 offset: 0x536
@scena.Code('func_02_536')
def func_02_536():
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
        'loc_55B',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_69D')

    def _loc_55B(): pass

    label('loc_55B')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_574',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_69D')

    def _loc_574(): pass

    label('loc_574')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_58D',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_69D')

    def _loc_58D(): pass

    label('loc_58D')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5A6',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_69D')

    def _loc_5A6(): pass

    label('loc_5A6')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5BF',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_69D')

    def _loc_5BF(): pass

    label('loc_5BF')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5D8',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_69D')

    def _loc_5D8(): pass

    label('loc_5D8')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5F1',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_69D')

    def _loc_5F1(): pass

    label('loc_5F1')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_60A',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_69D')

    def _loc_60A(): pass

    label('loc_60A')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_623',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_69D')

    def _loc_623(): pass

    label('loc_623')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_63C',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_69D')

    def _loc_63C(): pass

    label('loc_63C')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_655',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_69D')

    def _loc_655(): pass

    label('loc_655')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_66E',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_69D')

    def _loc_66E(): pass

    label('loc_66E')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_687',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_69D')

    def _loc_687(): pass

    label('loc_687')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_69D',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_69D(): pass

    label('loc_69D')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_6B2',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_69D')

    def _loc_6B2(): pass

    label('loc_6B2')

    Return()

# id: 0x0003 offset: 0x6B3
@scena.Code('func_03_6B3')
def func_03_6B3():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_721',
    )

    ChrWalkTo(0x00FE, 4760, 0, -39600, 2500, 0x00)
    Sleep(1500)

    ChrSetDirection(0x00FE, 90, 400)
    Sleep(1500)

    ChrSetDirection(0x00FE, 270, 400)
    Sleep(1500)

    ChrWalkTo(0x00FE, 4760, 0, -1190, 2500, 0x00)
    Sleep(1500)

    ChrSetDirection(0x00FE, 90, 400)
    Sleep(1500)

    ChrSetDirection(0x00FE, 0, 400)
    Sleep(1500)

    Jump('func_03_6B3')

    def _loc_721(): pass

    label('loc_721')

    Return()

# id: 0x0004 offset: 0x722
@scena.Code('func_04_722')
def func_04_722():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_790',
    )

    ChrWalkTo(0x00FE, -4540, 0, -20540, 2500, 0x00)
    Sleep(1500)

    ChrSetDirection(0x00FE, 270, 400)
    Sleep(1500)

    ChrSetDirection(0x00FE, 90, 400)
    Sleep(1500)

    ChrWalkTo(0x00FE, -4430, 0, -39600, 2500, 0x00)
    Sleep(1500)

    ChrSetDirection(0x00FE, 270, 400)
    Sleep(1500)

    ChrSetDirection(0x00FE, 90, 400)
    Sleep(1500)

    Jump('func_04_722')

    def _loc_790(): pass

    label('loc_790')

    Return()

# id: 0x0005 offset: 0x791
@scena.Code('func_05_791')
def func_05_791():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_7B4',
    )

    OP_8D(0x00FE, 3700, -42040, 10110, -50100, 2000)

    Jump('func_05_791')

    def _loc_7B4(): pass

    label('loc_7B4')

    Return()

# id: 0x0006 offset: 0x7B5
@scena.Code('func_06_7B5')
def func_06_7B5():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_823',
    )

    ChrWalkTo(0x00FE, 4760, 0, -39600, 2500, 0x00)
    Sleep(1500)

    ChrSetDirection(0x00FE, 90, 400)
    Sleep(1500)

    ChrSetDirection(0x00FE, 270, 400)
    Sleep(1500)

    ChrWalkTo(0x00FE, 4760, 0, -1190, 2500, 0x00)
    Sleep(1500)

    ChrSetDirection(0x00FE, 90, 400)
    Sleep(1500)

    ChrSetDirection(0x00FE, 0, 400)
    Sleep(1500)

    Jump('func_06_7B5')

    def _loc_823(): pass

    label('loc_823')

    Return()

# id: 0x0007 offset: 0x824
@scena.Code('func_07_824')
def func_07_824():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_892',
    )

    ChrWalkTo(0x00FE, -4540, 0, -20540, 2500, 0x00)
    Sleep(1500)

    ChrSetDirection(0x00FE, 270, 400)
    Sleep(1500)

    ChrSetDirection(0x00FE, 90, 400)
    Sleep(1500)

    ChrWalkTo(0x00FE, -4430, 0, -39600, 2500, 0x00)
    Sleep(1500)

    ChrSetDirection(0x00FE, 270, 400)
    Sleep(1500)

    ChrSetDirection(0x00FE, 90, 400)
    Sleep(1500)

    Jump('func_07_824')

    def _loc_892(): pass

    label('loc_892')

    Return()

# id: 0x0008 offset: 0x893
@scena.Code('func_08_893')
def func_08_893():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '◆没有台词。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0009 offset: 0x8AC
@scena.Code('func_09_8AC')
def func_09_8AC():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '◆没有台词。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x000A offset: 0x8C5
@scena.Code('func_0A_8C5')
def func_0A_8C5():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '◆没有台词。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x000B offset: 0x8DE
@scena.Code('func_0B_8DE')
def func_0B_8DE():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '◆没有台词。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x000C offset: 0x8F7
@scena.Code('func_0C_8F7')
def func_0C_8F7():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '◆没有台词。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x000D offset: 0x910
@scena.Code('func_0D_910')
def func_0D_910():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '◆没有台词。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x000E offset: 0x929
@scena.Code('func_0E_929')
def func_0E_929():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '◆没有台词。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x000F offset: 0x942
@scena.Code('func_0F_942')
def func_0F_942():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '◆没有台词。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0010 offset: 0x95B
@scena.Code('func_10_95B')
def func_10_95B():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '◆没有台词。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0011 offset: 0x974
@scena.Code('func_11_974')
def func_11_974():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '◆没有台词。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0012 offset: 0x98D
@scena.Code('func_12_98D')
def func_12_98D():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '◆没有台词。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0013 offset: 0x9A6
@scena.Code('func_13_9A6')
def func_13_9A6():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '◆没有台词。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0014 offset: 0x9BF
@scena.Code('func_14_9BF')
def func_14_9BF():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 2, 0x163A)),
            Expr.Return,
        ),
        'loc_9ED',
    )

    ChrTalk(
        0x00FE,
        (
            '现在，鸟向西\n',
            '飞去了没有呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A41')

    def _loc_9ED(): pass

    label('loc_9ED')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 1, 0x1639)),
            Expr.Return,
        ),
        'loc_A41',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，夜晚的冷气真令人心情舒畅。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '走在夜晚的市街上\n',
            '不觉得也挺风雅吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A41(): pass

    label('loc_A41')

    TalkEnd(0x00FE)

    Return()

# id: 0x0015 offset: 0xA45
@scena.Code('func_15_A45')
def func_15_A45():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 2, 0x163A)),
            Expr.Return,
        ),
        'loc_A87',
    )

    ChrTalk(
        0x00FE,
        (
            '哎呀，这么晚了\n',
            '打算去哪里？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '出门要当心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B1D')

    def _loc_A87(): pass

    label('loc_A87')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 1, 0x1639)),
            Expr.Return,
        ),
        'loc_B1D',
    )

    ChrTalk(
        0x00FE,
        (
            '似乎有武装的神秘人物\n',
            '在这个地区出没呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '由于希德中校的指示王城\n',
            '配备了一个中队呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然不知道是什么人\n',
            '对王都应该是没法下手的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B1D(): pass

    label('loc_B1D')

    TalkEnd(0x00FE)

    Return()

# id: 0x0016 offset: 0xB21
@scena.Code('func_16_B21')
def func_16_B21():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 2, 0x163A)),
            Expr.Return,
        ),
        'loc_B6F',
    )

    ChrTalk(
        0x00FE,
        (
            '市街应该还安全……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过注意不要去\n',
            '没什么人烟的地方哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BD2')

    def _loc_B6F(): pass

    label('loc_B6F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 1, 0x1639)),
            Expr.Return,
        ),
        'loc_BD2',
    )

    ChrTalk(
        0x00FE,
        (
            '结社……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '目的果然还是\n',
            '妨碍签字仪式吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在有我们的王都地区\n',
            '引起骚乱真是愚蠢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BD2(): pass

    label('loc_BD2')

    TalkEnd(0x00FE)

    Return()

# id: 0x0017 offset: 0xBD6
@scena.Code('func_17_BD6')
def func_17_BD6():
    EventBegin(0x00)
    OP_DB()
    FormationAddMember(ChrTable['管家菲利普'], 0xFF, 0xFF)
    ChrSetFlags(0x0143, 0x0080)
    CameraMove(-1140, 0, -63570, 0)
    OP_67(0, 7480, -10000, 0)
    CameraSetDistance(1800, 0)
    OP_6C(0, 0)
    OP_6E(580, 0)
    ChrSetPos(0x0101, 630, 0, -64819, 0)
    ChrSetPos(0x0109, -700, 0, -65820, 0)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0109, 0x0080)
    FadeIn(2000, 0)

    @scena.Lambda('lambda_0C5A')
    def lambda_0C5A():
        CameraMove(50, 0, 5920, 14000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0C5A)

    @scena.Lambda('lambda_0C72')
    def lambda_0C72():
        OP_6C(320000, 16000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0C72)

    @scena.Lambda('lambda_0C82')
    def lambda_0C82():
        OP_67(0, 14750, -10000, 16000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0C82)

    WaitForThreadExit(0x0101, 0x0003)
    Fade(1000)
    CameraMove(110, 0, -61800, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(4200, 0)
    OP_6C(134000, 0)
    OP_6E(200, 0)
    ChrClearFlags(0x0101, 0x0080)
    ChrClearFlags(0x0109, 0x0080)

    @scena.Lambda('lambda_0CEB')
    def lambda_0CEB():
        ChrWalkTo(0x00FE, 630, 0, -61500, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0CEB)

    @scena.Lambda('lambda_0D06')
    def lambda_0D06():
        ChrWalkTo(0x00FE, -700, 0, -61640, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0109, 0x0001, lambda_0D06)

    WaitForThreadExit(0x0109, 0x0001)
    OP_DC()

    ChrTalk(
        0x0101,
        (
            '#0010270001V#1002F#5P呼……\n',
            '太阳下山了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010270002V艾尔贝离宫\n',
            '会变成怎样呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180270003V#1060F不过，协会\n',
            '可能也有联络了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180270004V嗨，去看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010270005V#1015F#5P嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0109, 400)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010270006V#1007F#5P嗯……凯文先生。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010270007V刚才真对不起。\n',
            '对你乱发脾气了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0109, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x0109, 0x0101, 400)

    ChrTalk(
        0x0109,
        (
            '#0180270008V#1061F没关系，没关系。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180270009V是为了男朋友的事\n',
            '脑子晕乎乎了吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180270010V#1060F我不在意的，放心吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010270011V#1017F#5P嘿嘿，谢谢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010270012V#1015F不过不好意思\n',
            '不能完全信任你\n',
            '这话是不会收回的哦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180200010V#1068F哎呀，真服了你。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180270014V#1060F不过也好，关于这个\n',
            '也许协会也……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x0143, 0x0080)
    ChrSetPos(0x0143, 30, 300, -49360, 180)

    NpcTalk(
        0x0143,
        '男性的声音',
        (
            '#0660270015V#2P艾丝蒂尔大人……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0109, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_103C')
    def lambda_103C():
        CameraMove(220, 0, -60300, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_103C)

    @scena.Lambda('lambda_1054')
    def lambda_1054():
        OP_67(0, 7890, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1054)

    @scena.Lambda('lambda_106C')
    def lambda_106C():
        OP_6E(217, 2000)

        ExitThread()

    DispatchAsync(0x0143, 0x0001, lambda_106C)

    @scena.Lambda('lambda_107C')
    def lambda_107C():
        ChrTurnDirection(0x00FE, 0x0143, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_107C)

    Sleep(50)

    @scena.Lambda('lambda_108F')
    def lambda_108F():
        ChrTurnDirection(0x00FE, 0x0143, 400)

        ExitThread()

    DispatchAsync(0x0109, 0x0001, lambda_108F)

    ChrWalkTo(0x0143, 30, 0, -58730, 3000, 0x00)
    WaitForThreadExit(0x0143, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010270016V#1004F咦，菲利普先生？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0143,
        (
            '#0660270017V#722F#6P你、你好。\n',
            '今天早上真是失礼了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660270018V那个，艾丝蒂尔大人……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660270019V您有在哪里\n',
            '见过公爵阁下吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010270020V#1004F哎……\n',
            '早上倒是见过……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010270021V#1015F公爵先生怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0143,
        (
            '#0660270022V#722F#6P傍晚出去逛街\n',
            '就没再回城里来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660270023V阁下能去的地方\n',
            '我都找过了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010270024V#1007F啊啊真是的，这么忙的时候\n',
            '到底在做什么……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010270025V#1006F菲利普先生。\n',
            '我们现在要回协会\n',
            '请一起来吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010270026V如果公爵先生有麻烦\n',
            '说不定会发来联络。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0143,
        (
            '#0660270027V#722F#6P是、是啊……\n',
            '那么请让我同行吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660270028V#721F……对了，这位是？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180270029V#1062F啊、七耀教会的巡回神父\n',
            '凯文·格拉汉姆。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180270030V#1061F请多多指教～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0143,
        (
            '#0660270031V#720F#6P这真是冒昧了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660270032V我是公爵阁下\n',
            '的管家，\n',
            '名叫菲利普……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010270033V#1007F啊～寒暄就省了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010270034V#1006F赶快回协会吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(1000)
    CameraMove(290, 0, -61590, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 290, 0, -61590, 0)
    ChrSetPos(0x0109, 290, 0, -61590, 0)
    ChrSetPos(0x0143, 290, 0, -61590, 0)
    SetScenaFlags(ScenaFlag(0x02C7, 1, 0x1639))
    OP_1B(0x0A, 0x00, 0x001C)
    OP_1B(0x0B, 0x00, 0x0019)
    OP_1B(0x0C, 0x00, 0x001A)
    OP_1B(0x0D, 0x00, 0x0019)
    OP_1B(0x0E, 0x00, 0x001B)
    OP_1B(0x09, 0x00, 0x001D)
    OP_0D()
    EventEnd(0x00)
    MapSetFlags(0x02000000)

    Return()

# id: 0x0018 offset: 0x14CC
@scena.Code('func_18_14CC')
def func_18_14CC():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 3, 0x163B)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_15A8',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_1539',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_14F7',
    )

    ChrTurnDirection(0x0103, 0x0001, 400)

    Jump('loc_14FE')

    def _loc_14F7(): pass

    label('loc_14F7')

    ChrTurnDirection(0x0103, 0x0000, 400)

    def _loc_14FE(): pass

    label('loc_14FE')

    ChrTalk(
        0x0103,
        (
            '#0030270242V#022F似乎时间不多了呢。\n',
            '赶快去码头吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_158A')

    def _loc_1539(): pass

    label('loc_1539')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_154F',
    )

    ChrTurnDirection(0x0106, 0x0001, 400)

    Jump('loc_1556')

    def _loc_154F(): pass

    label('loc_154F')

    ChrTurnDirection(0x0106, 0x0000, 400)

    def _loc_1556(): pass

    label('loc_1556')

    ChrTalk(
        0x0106,
        (
            '#0050270243V#050F没时间浪费了。\n',
            '赶快去码头吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_158A(): pass

    label('loc_158A')

    ChrMoveToRelative(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Jump('loc_17B6')

    def _loc_15A8(): pass

    label('loc_15A8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 2, 0x163A)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_16F7',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_15FE',
    )

    ChrTalk(
        0x0101,
        (
            '#0010270244V#1002F没空磨蹭了。\n',
            '赶紧去西街区那边吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_16D9')

    def _loc_15FE(): pass

    label('loc_15FE')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1646',
    )

    ChrTalk(
        0x0109,
        (
            '#0180270245V#1063F时间似乎无多。\n',
            '赶紧去西街区那边。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_16D9')

    def _loc_1646(): pass

    label('loc_1646')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1693',
    )

    ChrTalk(
        0x0103,
        (
            '#0030270246V#022F似乎时间不多了呢。\n',
            '赶紧去西街区那边吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_16D9')

    def _loc_1693(): pass

    label('loc_1693')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_16D9',
    )

    ChrTalk(
        0x0106,
        (
            '#0050270247V#050F没时间浪费了。\n',
            '赶紧去西街区那边吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_16D9(): pass

    label('loc_16D9')

    ChrMoveToRelative(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Jump('loc_17B6')

    def _loc_16F7(): pass

    label('loc_16F7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 1, 0x1639)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_17B6',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_174F',
    )

    ChrTalk(
        0x0101,
        (
            '#0010270248V#1000F……已经这么晚了。\n',
            '赶快返回协会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1796')

    def _loc_174F(): pass

    label('loc_174F')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1796',
    )

    ChrTalk(
        0x0109,
        (
            '#0180270249V#1060F……已经这么晚了啊。\n',
            '赶快去协会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1796(): pass

    label('loc_1796')

    ChrMoveToRelative(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)
    MapSetFlags(0x02000000)

    def _loc_17B6(): pass

    label('loc_17B6')

    Return()

# id: 0x0019 offset: 0x17B7
@scena.Code('func_19_17B7')
def func_19_17B7():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 3, 0x163B)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1878',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_1824',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_17E2',
    )

    ChrTurnDirection(0x0103, 0x0001, 400)

    Jump('loc_17E9')

    def _loc_17E2(): pass

    label('loc_17E2')

    ChrTurnDirection(0x0103, 0x0000, 400)

    def _loc_17E9(): pass

    label('loc_17E9')

    ChrTalk(
        0x0103,
        (
            '#0030270242V#022F似乎时间不多了呢。\n',
            '赶快去码头吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1875')

    def _loc_1824(): pass

    label('loc_1824')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_183A',
    )

    ChrTurnDirection(0x0106, 0x0001, 400)

    Jump('loc_1841')

    def _loc_183A(): pass

    label('loc_183A')

    ChrTurnDirection(0x0106, 0x0000, 400)

    def _loc_1841(): pass

    label('loc_1841')

    ChrTalk(
        0x0106,
        (
            '#0050270243V#050F没时间浪费了。\n',
            '赶快去码头吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_1875(): pass

    label('loc_1875')

    Jump('loc_1A47')

    def _loc_1878(): pass

    label('loc_1878')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 2, 0x163A)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_19AC',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_18CE',
    )

    ChrTalk(
        0x0101,
        (
            '#0010270244V#1002F没空磨蹭了。\n',
            '赶紧去西街区那边吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19A9')

    def _loc_18CE(): pass

    label('loc_18CE')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1916',
    )

    ChrTalk(
        0x0109,
        (
            '#0180270245V#1063F时间似乎无多。\n',
            '赶紧去西街区那边。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19A9')

    def _loc_1916(): pass

    label('loc_1916')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1963',
    )

    ChrTalk(
        0x0103,
        (
            '#0030270246V#022F似乎时间不多了呢。\n',
            '赶紧去西街区那边吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19A9')

    def _loc_1963(): pass

    label('loc_1963')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_19A9',
    )

    ChrTalk(
        0x0106,
        (
            '#0050270247V#050F没时间浪费了。\n',
            '赶紧去西街区那边吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_19A9(): pass

    label('loc_19A9')

    Jump('loc_1A47')

    def _loc_19AC(): pass

    label('loc_19AC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 2, 0x163A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1A47',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1A00',
    )

    ChrTalk(
        0x0101,
        (
            '#0010270248V#1000F……已经这么晚了。\n',
            '赶快返回协会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A47')

    def _loc_1A00(): pass

    label('loc_1A00')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1A47',
    )

    ChrTalk(
        0x0109,
        (
            '#0180270249V#1060F……已经这么晚了啊。\n',
            '赶快去协会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A47(): pass

    label('loc_1A47')

    ChrMoveToRelative(0x0000, 0, 0, -1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)
    MapSetFlags(0x02000000)

    Return()

# id: 0x001A offset: 0x1A68
@scena.Code('func_1A_1A68')
def func_1A_1A68():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 3, 0x163B)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1B29',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_1AD5',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1A93',
    )

    ChrTurnDirection(0x0103, 0x0001, 400)

    Jump('loc_1A9A')

    def _loc_1A93(): pass

    label('loc_1A93')

    ChrTurnDirection(0x0103, 0x0000, 400)

    def _loc_1A9A(): pass

    label('loc_1A9A')

    ChrTalk(
        0x0103,
        (
            '#0030270242V#022F似乎时间不多了呢。\n',
            '赶快去码头吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B26')

    def _loc_1AD5(): pass

    label('loc_1AD5')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1AEB',
    )

    ChrTurnDirection(0x0106, 0x0001, 400)

    Jump('loc_1AF2')

    def _loc_1AEB(): pass

    label('loc_1AEB')

    ChrTurnDirection(0x0106, 0x0000, 400)

    def _loc_1AF2(): pass

    label('loc_1AF2')

    ChrTalk(
        0x0106,
        (
            '#0050270243V#050F没时间浪费了。\n',
            '赶快去码头吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_1B26(): pass

    label('loc_1B26')

    Jump('loc_1CF8')

    def _loc_1B29(): pass

    label('loc_1B29')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 2, 0x163A)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1C5D',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1B7F',
    )

    ChrTalk(
        0x0101,
        (
            '#0010270244V#1002F没空磨蹭了。\n',
            '赶紧去西街区那边吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C5A')

    def _loc_1B7F(): pass

    label('loc_1B7F')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1BC7',
    )

    ChrTalk(
        0x0109,
        (
            '#0180270245V#1063F时间似乎无多。\n',
            '赶紧去西街区那边。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C5A')

    def _loc_1BC7(): pass

    label('loc_1BC7')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1C14',
    )

    ChrTalk(
        0x0103,
        (
            '#0030270246V#022F似乎时间不多了呢。\n',
            '赶紧去西街区那边吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C5A')

    def _loc_1C14(): pass

    label('loc_1C14')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1C5A',
    )

    ChrTalk(
        0x0106,
        (
            '#0050270247V#050F没时间浪费了。\n',
            '赶紧去西街区那边吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C5A(): pass

    label('loc_1C5A')

    Jump('loc_1CF8')

    def _loc_1C5D(): pass

    label('loc_1C5D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 2, 0x163A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1CF8',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1CB1',
    )

    ChrTalk(
        0x0101,
        (
            '#0010270248V#1000F……已经这么晚了。\n',
            '赶快返回协会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1CF8')

    def _loc_1CB1(): pass

    label('loc_1CB1')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1CF8',
    )

    ChrTalk(
        0x0109,
        (
            '#0180270249V#1060F……已经这么晚了啊。\n',
            '赶快去协会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1CF8(): pass

    label('loc_1CF8')

    OP_59()

    @scena.Lambda('lambda_1CFF')
    def lambda_1CFF():
        CameraMove(-3370, 0, 11000, 1000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_1CFF)

    Fade(1000)
    ChrSetPos(0x0000, -3370, 0, 12430, 180)
    ChrSetPos(0x0001, -3370, 0, 12430, 180)
    ChrSetPos(0x0002, -3370, 0, 12430, 180)
    ChrSetPos(0x0143, -3370, 0, 12430, 180)
    OP_0D()
    ChrSetDirection(0x0000, 180, 0)
    Sleep(50)

    EventEnd(0x04)
    MapSetFlags(0x02000000)

    Return()

# id: 0x001B offset: 0x1D6F
@scena.Code('func_1B_1D6F')
def func_1B_1D6F():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 3, 0x163B)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1E30',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_1DDC',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1D9A',
    )

    ChrTurnDirection(0x0103, 0x0001, 400)

    Jump('loc_1DA1')

    def _loc_1D9A(): pass

    label('loc_1D9A')

    ChrTurnDirection(0x0103, 0x0000, 400)

    def _loc_1DA1(): pass

    label('loc_1DA1')

    ChrTalk(
        0x0103,
        (
            '#0030270242V#022F似乎时间不多了呢。\n',
            '赶快去码头吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E2D')

    def _loc_1DDC(): pass

    label('loc_1DDC')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1DF2',
    )

    ChrTurnDirection(0x0106, 0x0001, 400)

    Jump('loc_1DF9')

    def _loc_1DF2(): pass

    label('loc_1DF2')

    ChrTurnDirection(0x0106, 0x0000, 400)

    def _loc_1DF9(): pass

    label('loc_1DF9')

    ChrTalk(
        0x0106,
        (
            '#0050270243V#050F没时间浪费了。\n',
            '赶快去码头吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_1E2D(): pass

    label('loc_1E2D')

    Jump('loc_1FFF')

    def _loc_1E30(): pass

    label('loc_1E30')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 2, 0x163A)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1F64',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1E86',
    )

    ChrTalk(
        0x0101,
        (
            '#0010270244V#1002F没空磨蹭了。\n',
            '赶紧去西街区那边吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F61')

    def _loc_1E86(): pass

    label('loc_1E86')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1ECE',
    )

    ChrTalk(
        0x0109,
        (
            '#0180270245V#1063F时间似乎无多。\n',
            '赶紧去西街区那边。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F61')

    def _loc_1ECE(): pass

    label('loc_1ECE')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1F1B',
    )

    ChrTalk(
        0x0103,
        (
            '#0030270246V#022F似乎时间不多了呢。\n',
            '赶紧去西街区那边吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F61')

    def _loc_1F1B(): pass

    label('loc_1F1B')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1F61',
    )

    ChrTalk(
        0x0106,
        (
            '#0050270247V#050F没时间浪费了。\n',
            '赶紧去西街区那边吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1F61(): pass

    label('loc_1F61')

    Jump('loc_1FFF')

    def _loc_1F64(): pass

    label('loc_1F64')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 2, 0x163A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1FFF',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1FB8',
    )

    ChrTalk(
        0x0101,
        (
            '#0010270248V#1000F……已经这么晚了。\n',
            '赶快返回协会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1FFF')

    def _loc_1FB8(): pass

    label('loc_1FB8')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1FFF',
    )

    ChrTalk(
        0x0109,
        (
            '#0180270249V#1060F……已经这么晚了啊。\n',
            '赶快去协会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1FFF(): pass

    label('loc_1FFF')

    OP_59()

    @scena.Lambda('lambda_2006')
    def lambda_2006():
        CameraMove(3370, 0, 11000, 1000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_2006)

    Fade(1000)
    ChrSetPos(0x0000, 3370, 0, 12430, 180)
    ChrSetPos(0x0001, 3370, 0, 12430, 180)
    ChrSetPos(0x0002, 3370, 0, 12430, 180)
    ChrSetPos(0x0143, 3370, 0, 12430, 180)
    OP_0D()
    ChrSetDirection(0x0000, 180, 0)
    Sleep(50)

    EventEnd(0x04)
    MapSetFlags(0x02000000)

    Return()

# id: 0x001C offset: 0x2076
@scena.Code('func_1C_2076')
def func_1C_2076():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 3, 0x163B)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2137',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_20E3',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_20A1',
    )

    ChrTurnDirection(0x0103, 0x0001, 400)

    Jump('loc_20A8')

    def _loc_20A1(): pass

    label('loc_20A1')

    ChrTurnDirection(0x0103, 0x0000, 400)

    def _loc_20A8(): pass

    label('loc_20A8')

    ChrTalk(
        0x0103,
        (
            '#0030270242V#022F似乎时间不多了呢。\n',
            '赶快去码头吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2134')

    def _loc_20E3(): pass

    label('loc_20E3')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_20F9',
    )

    ChrTurnDirection(0x0106, 0x0001, 400)

    Jump('loc_2100')

    def _loc_20F9(): pass

    label('loc_20F9')

    ChrTurnDirection(0x0106, 0x0000, 400)

    def _loc_2100(): pass

    label('loc_2100')

    ChrTalk(
        0x0106,
        (
            '#0050270243V#050F没时间浪费了。\n',
            '赶快去码头吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_2134(): pass

    label('loc_2134')

    Jump('loc_2306')

    def _loc_2137(): pass

    label('loc_2137')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 2, 0x163A)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_226B',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_218D',
    )

    ChrTalk(
        0x0101,
        (
            '#0010270244V#1002F没空磨蹭了。\n',
            '赶紧去西街区那边吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2268')

    def _loc_218D(): pass

    label('loc_218D')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_21D5',
    )

    ChrTalk(
        0x0109,
        (
            '#0180270245V#1063F时间似乎无多。\n',
            '赶紧去西街区那边。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2268')

    def _loc_21D5(): pass

    label('loc_21D5')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2222',
    )

    ChrTalk(
        0x0103,
        (
            '#0030270246V#022F似乎时间不多了呢。\n',
            '赶紧去西街区那边吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2268')

    def _loc_2222(): pass

    label('loc_2222')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2268',
    )

    ChrTalk(
        0x0106,
        (
            '#0050270247V#050F没时间浪费了。\n',
            '赶紧去西街区那边吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2268(): pass

    label('loc_2268')

    Jump('loc_2306')

    def _loc_226B(): pass

    label('loc_226B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 2, 0x163A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2306',
    )

    EventBegin(0x02)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_22BF',
    )

    ChrTalk(
        0x0101,
        (
            '#0010270248V#1000F……已经这么晚了。\n',
            '赶快返回协会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2306')

    def _loc_22BF(): pass

    label('loc_22BF')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2306',
    )

    ChrTalk(
        0x0109,
        (
            '#0180270249V#1060F……已经这么晚了啊。\n',
            '赶快去协会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2306(): pass

    label('loc_2306')

    ChrMoveToRelative(0x0000, -1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)
    MapSetFlags(0x02000000)

    Return()

# id: 0x001D offset: 0x2327
@scena.Code('func_1D_2327')
def func_1D_2327():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 2, 0x163A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_23E2',
    )

    EventBegin(0x02)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_237B',
    )

    ChrTalk(
        0x0101,
        (
            '#0010270248V#1000F……已经这么晚了。\n',
            '赶快返回协会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23C2')

    def _loc_237B(): pass

    label('loc_237B')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_23C2',
    )

    ChrTalk(
        0x0109,
        (
            '#0180270249V#1060F……已经这么晚了啊。\n',
            '赶快去协会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_23C2(): pass

    label('loc_23C2')

    ChrMoveToRelative(0x0000, 1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)
    MapSetFlags(0x02000000)

    def _loc_23E2(): pass

    label('loc_23E2')

    Return()

# id: 0x001E offset: 0x23E3
@scena.Code('func_1E_23E3')
def func_1E_23E3():
    EventBegin(0x00)
    OP_4A(0x0015, 255)
    OP_4A(0x0016, 255)
    OP_4A(0x0017, 255)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2402',
    )

    Call(0, 0x0022)

    def _loc_2402(): pass

    label('loc_2402')

    FormationDelMember(0x42, 0xFF)
    FormationDelMember(0x08, 0xFF)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_2420',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)
    ChrSetStatus(ChrTable['雪拉扎德'], 0x00, 56)
    ChrSetStatus(ChrTable['雪拉扎德'], 0xFE, 0)

    Jump('loc_242E')

    def _loc_2420(): pass

    label('loc_2420')

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)
    ChrSetStatus(ChrTable['阿加特'], 0x00, 56)
    ChrSetStatus(ChrTable['阿加特'], 0xFE, 0)

    def _loc_242E(): pass

    label('loc_242E')

    FormationAddMember(ChrTable['凯文神父'], 0xF8, 0xFF)
    OP_C0(0x15, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)
    OP_4A(0x0009, 255)
    OP_4A(0x000A, 255)
    OP_4A(0x000B, 255)
    OP_4A(0x000C, 255)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x00F7, 0x0080)
    ChrSetFlags(0x0109, 0x0080)
    CameraMove(8150, 250, -13250, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeIn(1500, 0)
    Sleep(500)

    OP_72(0x0001, 0x0010)
    OP_6F(0x0001, 0)
    OP_70(0x0001, 59)
    OP_73(0x0001)
    Sleep(500)

    CreateThread(0x0101, 0x01, 0x00, func_1F_2DA4)
    Sleep(800)

    CreateThread(0x00F7, 0x01, 0x00, func_20_2DF3)
    Sleep(800)

    CreateThread(0x0109, 0x01, 0x00, func_21_2E42)
    Sleep(500)

    @scena.Lambda('lambda_2503')
    def lambda_2503():
        CameraMove(5120, 0, -13430, 2000)

        ExitThread()

    DispatchAsync(0x0109, 0x0003, lambda_2503)

    OP_72(0x0001, 0x0800)
    OP_6F(0x0001, 59)
    OP_70(0x0001, 0)
    OP_71(0x0001, 0x0010)
    OP_23(0x0006)
    PlaySE(7, 0x00, 0x64)
    WaitForThreadExit(0x0109, 0x0001)
    WaitForThreadExit(0x0109, 0x0002)
    OP_71(0x0001, 0x0800)

    ChrTalk(
        0x0101,
        (
            '#0010270219V#1002F#6P茶会……\n',
            '你觉得到底是在哪里？',
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
        'loc_2614',
    )

    ChrTalk(
        0x0106,
        (
            '#0050270220V#053F#2P最可能的是\n',
            '格兰赛尔城……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050270221V#050F但记得有相当数量的\n',
            '士兵聚集着。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050270222V选其他地方比较好吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_26A3')

    def _loc_2614(): pass

    label('loc_2614')

    ChrTalk(
        0x0103,
        (
            '#0030270223V#026F#2P最可能的地方\n',
            '是格兰赛尔城……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030270224V#020F不过记得有相当数量的\n',
            '士兵聚集着吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030270225V选其他地方比较好吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_26A3(): pass

    label('loc_26A3')

    ChrTalk(
        0x0109,
        (
            '#0180270226V#1067F嗯～话虽如此\n',
            '这个城市真宽广啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180270227V要是没个大体的线索……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x0008, 0x0080)
    ChrSetFlags(0x0008, 0x0040)
    ChrSetPos(0x0008, -14000, 6000, -18050, 90)
    PlaySE(407, 0x00, 0x64)
    Sleep(500)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrSetDirection(0x0101, 270, 400)

    ChrTalk(
        0x0101,
        (
            '#0010270228V#1011F#5P啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(140, 0x00, 0x64)
    CreateThread(0x0008, 0x00, 0x00, func_02_536)

    @scena.Lambda('lambda_277B')
    def lambda_277B():
        CameraMove(-1390, 0, -15440, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_277B)

    @scena.Lambda('lambda_2793')
    def lambda_2793():
        OP_67(0, 12610, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2793)

    @scena.Lambda('lambda_27AB')
    def lambda_27AB():
        CameraSetDistance(1940, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_27AB)

    @scena.Lambda('lambda_27BB')
    def lambda_27BB():
        OP_6C(45000, 2000)

        ExitThread()

    DispatchAsync(0x0109, 0x0001, lambda_27BB)

    @scena.Lambda('lambda_27CB')
    def lambda_27CB():
        OP_6E(362, 2000)

        ExitThread()

    DispatchAsync(0x0109, 0x0002, lambda_27CB)

    @scena.Lambda('lambda_27DB')
    def lambda_27DB():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_27DB')

    DispatchAsync2(0x0109, 0x0000, lambda_27DB)

    @scena.Lambda('lambda_27EC')
    def lambda_27EC():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_27EC')

    DispatchAsync2(0x00F7, 0x0000, lambda_27EC)

    WaitForThreadExit(0x0101, 0x0001)
    ChrWalkTo(0x0008, 0, 2000, -20000, 10000, 0x00)
    TerminateThread(0x0101, 0x00)

    @scena.Lambda('lambda_281A')
    def lambda_281A():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_281A)

    @scena.Lambda('lambda_2828')
    def lambda_2828():
        CameraMove(4980, 0, -13500, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2828)

    @scena.Lambda('lambda_2840')
    def lambda_2840():
        OP_67(0, 11320, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2840)

    @scena.Lambda('lambda_2858')
    def lambda_2858():
        CameraSetDistance(1800, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2858)

    TerminateThread(0x0109, 0x00)
    OP_97(0x0008, 2000, -16000, -160000, 6000, 0x0001)
    ChrSetChipByIndex(0x0008, 11)
    ChrSetSubChip(0x0008, 0)
    ChrSetDirection(0x0008, 225, 400)
    TerminateThread(0x00F7, 0x00)

    @scena.Lambda('lambda_2896')
    def lambda_2896():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0000, lambda_2896)

    @scena.Lambda('lambda_28A4')
    def lambda_28A4():
        ChrSetDirection(0x00FE, 225, 400)

        ExitThread()

    DispatchAsync(0x0109, 0x0000, lambda_28A4)

    ChrMoveTo(0x0008, 4300, 300, -13800, 1000, 0x00)
    Fade(500)
    ChrSetFlags(0x0008, 0x0080)
    ChrSetChipByIndex(0x0101, 1)
    ChrSetSubChip(0x0101, 0)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0001)
    ChrSetSubChip(0x0101, 1)

    ChrTalk(
        0x0101,
        (
            '#0010270229V#1018F#6P基库！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0109, 0x00000000, 2300, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x0109,
        (
            '#0180270230V#1064F哇哇，什么东西！？',
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
        'loc_2977',
    )

    ChrTalk(
        0x0106,
        (
            '#0050270231V#051F哦哦，来了啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_29A0')

    def _loc_2977(): pass

    label('loc_2977')

    ChrTalk(
        0x0103,
        (
            '#0030270232V#021F呵呵，助手登场呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_29A0(): pass

    label('loc_29A0')

    ChrTalk(
        0x0008,
        (
            '#0440270233V#310F#2P啾啾！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0440270234V啾～～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010270235V#1006F#6P虽、虽然搞不太清楚状况……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010270236V它是打算\n',
            '给我们带路？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0440270237V#311F#2P啾⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(500)
    ChrSetPos(0x0008, 4300, 300, -13800, 225)
    ChrSetFlags(0x0008, 0x0080)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetSubChip(0x0101, 0)
    ChrClearFlags(0x0008, 0x0080)
    OP_0D()
    PlaySE(140, 0x00, 0x64)

    @scena.Lambda('lambda_2A82')
    def lambda_2A82():
        CameraMove(4980, 2000, -13500, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2A82)

    @scena.Lambda('lambda_2A9A')
    def lambda_2A9A():
        ChrMoveTo(0x00FE, 4500, 4000, -14000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_2A9A)

    WaitForThreadExit(0x0008, 0x0003)
    WaitForThreadExit(0x0101, 0x0003)
    ChrSetDirection(0x0008, 270, 400)
    Sleep(300)

    ChrSetChipByIndex(0x0008, 0)
    ChrSetSubChip(0x0008, 0)

    @scena.Lambda('lambda_2AD5')
    def lambda_2AD5():
        ChrWalkTo(0x00FE, -23970, 6000, -20020, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_2AD5)

    Sleep(500)

    @scena.Lambda('lambda_2AF5')
    def lambda_2AF5():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_2AF5')

    DispatchAsync2(0x0101, 0x0000, lambda_2AF5)

    @scena.Lambda('lambda_2B06')
    def lambda_2B06():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_2B06')

    DispatchAsync2(0x0109, 0x0000, lambda_2B06)

    @scena.Lambda('lambda_2B17')
    def lambda_2B17():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_2B17')

    DispatchAsync2(0x00F7, 0x0000, lambda_2B17)

    @scena.Lambda('lambda_2B28')
    def lambda_2B28():
        CameraMove(-30650, 0, -19610, 5000)

        ExitThread()

    DispatchAsync(0x00F7, 0x0003, lambda_2B28)

    @scena.Lambda('lambda_2B40')
    def lambda_2B40():
        CameraSetDistance(2530, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2B40)

    @scena.Lambda('lambda_2B50')
    def lambda_2B50():
        OP_6C(279000, 5000)

        ExitThread()

    DispatchAsync(0x0109, 0x0003, lambda_2B50)

    WaitForThreadExit(0x0008, 0x0002)
    TerminateThread(0x0008, 0x01)
    ChrWalkTo(0x0008, -35970, 8000, -20020, 6000, 0x00)
    TerminateThread(0x0101, 0x00)
    TerminateThread(0x0109, 0x00)
    TerminateThread(0x00F7, 0x00)
    ChrSetPos(0x0101, -15970, 0, -20020, 270)
    ChrSetPos(0x00F7, -15260, 0, -19020, 270)
    ChrSetPos(0x0109, -15170, 0, -21220, 270)

    @scena.Lambda('lambda_2BBC')
    def lambda_2BBC():
        ChrWalkTo(0x00FE, -27970, 0, -20020, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2BBC)

    Sleep(50)

    @scena.Lambda('lambda_2BDC')
    def lambda_2BDC():
        ChrWalkTo(0x00FE, -27260, 0, -19020, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_2BDC)

    Sleep(50)

    @scena.Lambda('lambda_2BFC')
    def lambda_2BFC():
        ChrWalkTo(0x00FE, -27170, 0, -21220, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0109, 0x0001, lambda_2BFC)

    WaitForThreadExit(0x0109, 0x0001)
    Sleep(500)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2C56',
    )

    ChrTalk(
        0x0106,
        (
            '#0050270238V#555F#4P西街区方向吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2C82')

    def _loc_2C56(): pass

    label('loc_2C56')

    ChrTalk(
        0x0103,
        (
            '#0030270239V#027F#4P西街区方向是吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2C82(): pass

    label('loc_2C82')

    ChrTalk(
        0x0101,
        (
            '#0010270240V#1006F#5P嗯，去看看吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180270241V#1068F#6P唉～……\n',
            '你们，可真是厉害啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x0008, 0x0080)
    Sleep(200)

    OP_4B(0x0009, 255)
    OP_4B(0x000A, 255)
    OP_4B(0x000B, 255)
    OP_4B(0x000C, 255)
    Fade(1000)
    CameraMove(-27270, 0, -19880, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(270000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0000, -27970, 0, -20020, 270)
    ChrSetPos(0x0001, -27970, 0, -20020, 270)
    ChrSetPos(0x0002, -27970, 0, -20020, 270)
    OP_69(0x0000, 0)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x02C7, 2, 0x163A))
    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    OP_1B(0x09, 0xFF, 0xFFFF)
    OP_28(0x008E, 0x04, 0x02)
    OP_28(0x008E, 0x04, 0x08)
    OP_28(0x008E, 0x01, 0x0001)
    EventEnd(0x00)
    OP_4B(0x0015, 255)
    OP_4B(0x0016, 255)
    OP_4B(0x0017, 255)

    Return()

# id: 0x001F offset: 0x2DA4
@scena.Code('func_1F_2DA4')
def func_1F_2DA4():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetPos(0x00FE, 11480, 750, -13010, 270)

    @scena.Lambda('lambda_2DCB')
    def lambda_2DCB():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 200)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2DCB)

    ChrWalkTo(0x00FE, 3880, 0, -13730, 2000, 0x00)
    ChrSetDirection(0x00FE, 90, 400)

    Return()

# id: 0x0020 offset: 0x2DF3
@scena.Code('func_20_2DF3')
def func_20_2DF3():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetPos(0x00FE, 11480, 750, -13010, 270)

    @scena.Lambda('lambda_2E1A')
    def lambda_2E1A():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 200)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2E1A)

    ChrWalkTo(0x00FE, 5520, 40, -14370, 2000, 0x00)
    ChrSetDirection(0x00FE, 270, 400)

    Return()

# id: 0x0021 offset: 0x2E42
@scena.Code('func_21_2E42')
def func_21_2E42():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetPos(0x00FE, 11480, 750, -13010, 270)

    @scena.Lambda('lambda_2E69')
    def lambda_2E69():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 200)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2E69)

    ChrWalkTo(0x00FE, 5550, 0, -13230, 2000, 0x00)
    ChrSetDirection(0x00FE, 225, 400)

    Return()

# id: 0x0022 offset: 0x2E91
@scena.Code('func_22_2E91')
def func_22_2E91():
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
        (0x00000000, 'loc_2F0B'),
        (0x00000001, 'loc_2F11'),
        (-1, 'loc_2F17'),
    )

    def _loc_2F0B(): pass

    label('loc_2F0B')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_2F17')

    def _loc_2F11(): pass

    label('loc_2F11')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_2F17')

    def _loc_2F17(): pass

    label('loc_2F17')

    Return()

# id: 0x0023 offset: 0x2F18
@scena.Code('func_23_2F18')
def func_23_2F18():
    OP_13(0x00B9)

    Return()

# id: 0x0024 offset: 0x2F1C
@scena.Code('func_24_2F1C')
def func_24_2F1C():
    OP_13(0x00B0)

    Return()

# id: 0x0025 offset: 0x2F20
@scena.Code('func_25_2F20')
def func_25_2F20():
    OP_13(0x00B2)

    Return()

# id: 0x0026 offset: 0x2F24
@scena.Code('func_26_2F24')
def func_26_2F24():
    OP_13(0x00AE)

    Return()

# id: 0x0027 offset: 0x2F28
@scena.Code('func_27_2F28')
def func_27_2F28():
    OP_13(0x00B3)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
