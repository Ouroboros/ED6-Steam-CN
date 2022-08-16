import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T3100_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3100   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'T3100.x'
    header.mapIndex       = 1
    header.bgm            = 13
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/T3100_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
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
        ('ED6_DT07/CH01060._CH', 'ED6_DT07/CH01060P._CP'),
        ('ED6_DT07/CH01100._CH', 'ED6_DT07/CH01100P._CP'),
        ('ED6_DT07/CH02490._CH', 'ED6_DT07/CH02490P._CP'),
        ('ED6_DT07/CH01530._CH', 'ED6_DT07/CH01530P._CP'),
        ('ED6_DT07/CH01130._CH', 'ED6_DT07/CH01130P._CP'),
        ('ED6_DT07/CH01470._CH', 'ED6_DT07/CH01470P._CP'),
        ('ED6_DT07/CH02610._CH', 'ED6_DT07/CH02610P._CP'),
        ('ED6_DT07/CH01200._CH', 'ED6_DT07/CH01200P._CP'),
        ('ED6_DT07/CH01000._CH', 'ED6_DT07/CH01000P._CP'),
        ('ED6_DT07/CH01760._CH', 'ED6_DT07/CH01760P._CP'),
        ('ED6_DT07/CH01250._CH', 'ED6_DT07/CH01250P._CP'),
        ('ED6_DT26/CH20311._CH', 'ED6_DT26/CH20311P._CP'),
    ]

# id: 0x10001 offset: 0x10A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '库诺',
            x                   = 38920,
            z                   = 0,
            y                   = 69060,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '科奇莫爷爷',
            x                   = 37980,
            z                   = 0,
            y                   = 77980,
            direction           = 315,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '莫妮卡',
            x                   = 38350,
            z                   = 0,
            y                   = 64680,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '布鲁诺',
            x                   = 36810,
            z                   = 0,
            y                   = 45690,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            name                = '阿利瑟',
            x                   = 14780,
            z                   = 3500,
            y                   = 72610,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            name                = '温丝',
            x                   = 16640,
            z                   = 3500,
            y                   = 73500,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '自动扶梯',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 18,
            chipIndex           = 18,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '雾香',
            x                   = 28770,
            z                   = 0,
            y                   = 61520,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '斯坦因',
            x                   = 20010,
            z                   = 0,
            y                   = 60550,
            direction           = 135,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '兰达老人',
            x                   = 42470,
            z                   = 0,
            y                   = 55580,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0005,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '王',
            x                   = 42250,
            z                   = 0,
            y                   = 54550,
            direction           = 360,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0005,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '运输车',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '伊格尔',
            x                   = 8500,
            z                   = 0,
            y                   = 58280,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0015,
        ),
        ScenaNpcData(
            name                = '蔡斯市·工房区',
            x                   = -17220,
            z                   = 8000,
            y                   = 59000,
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
            name                = '托兰特平原道方向',
            x                   = 81330,
            z                   = 0,
            y                   = 53110,
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
            name                = '利塔街道方向',
            x                   = 42990,
            z                   = 0,
            y                   = 104270,
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

# id: 0x10002 offset: 0x30A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x30A
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 39780,
            y           = 0,
            z           = 90710,
            range       = 46240,
            dword_10    = 0x000007D0,
            dword_14    = 0x00016544,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000001C,
        ),
        ScenaEventData(
            x           = 69760,
            y           = 0,
            z           = 48040,
            range       = 70360,
            dword_10    = 0x000007D0,
            dword_14    = 0x0000E20E,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000001D,
        ),
        ScenaEventData(
            x           = 7780,
            y           = -1000,
            z           = 63930,
            range       = 6420,
            dword_10    = 0x000003E8,
            dword_14    = 0x0000EA1A,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000001F,
        ),
        ScenaEventData(
            x           = 6420,
            y           = -1000,
            z           = 58250,
            range       = 7860,
            dword_10    = 0x000003E8,
            dword_14    = 0x0000D5D4,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000001F,
        ),
        ScenaEventData(
            x           = 43700,
            y           = 0,
            z           = 63080,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000020,
        ),
        ScenaEventData(
            x           = 40200,
            y           = 0,
            z           = 66870,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000020,
        ),
        ScenaEventData(
            x           = 52230,
            y           = 0,
            z           = 54590,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000021,
        ),
        ScenaEventData(
            x           = 47450,
            y           = 450,
            z           = 51500,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000021,
        ),
        ScenaEventData(
            x           = 47450,
            y           = 450,
            z           = 48500,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000021,
        ),
        ScenaEventData(
            x           = 59950,
            y           = 0,
            z           = 25220,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000022,
        ),
        ScenaEventData(
            x           = 36000,
            y           = 0,
            z           = 54740,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000023,
        ),
        ScenaEventData(
            x           = 27020,
            y           = 0,
            z           = 63460,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000024,
        ),
        ScenaEventData(
            x           = 23130,
            y           = 0,
            z           = 82450,
            range       = 1200,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000025,
        ),
        ScenaEventData(
            x           = 64030,
            y           = 0,
            z           = 69550,
            range       = 1200,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000026,
        ),
    )

# id: 0x10004 offset: 0x4CA
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 33000,
            triggerZ            = 500,
            triggerY            = 85510,
            triggerRange        = 800,
            actorX              = 33000,
            actorZ              = 1500,
            actorY              = 85510,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0011,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 56700,
            triggerZ            = 0,
            triggerY            = 48320,
            triggerRange        = 1000,
            actorX              = 56700,
            actorZ              = 1000,
            actorY              = 48320,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0013,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 30800,
            triggerZ            = 0,
            triggerY            = 63150,
            triggerRange        = 1000,
            actorX              = 30800,
            actorZ              = 3000,
            actorY              = 63150,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0014,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 35000,
            triggerZ            = 500,
            triggerY            = 87990,
            triggerRange        = 800,
            actorX              = 33610,
            actorZ              = 1850,
            actorY              = 87900,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0012,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x55A
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_5FC',
    )

    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetPos(0x0009, 12790, 0, 61820, 265)
    CreateThread(0x0009, 0x00, 0x00, func_02_85B)
    ChrClearFlags(0x0014, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_5B9',
    )

    ChrSetPos(0x000B, 18190, 0, 57240, 120)
    ChrSetPos(0x0014, 20310, 0, 56290, 180)
    ChrSetFlags(0x000D, 0x0080)

    Jump('loc_5F9')

    def _loc_5B9(): pass

    label('loc_5B9')

    ChrSetPos(0x000B, 8520, 0, 59530, 185)
    ChrClearFlags(0x0012, 0x0080)
    CreateThread(0x0012, 0x00, 0x00, func_02_85B)
    ChrSetPos(0x0012, 33570, 0, 57740, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0419, 2, 0x20CA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5F4',
    )

    ChrSetFlags(0x0012, 0x0010)

    def _loc_5F4(): pass

    label('loc_5F4')

    ChrSetFlags(0x000D, 0x0080)

    def _loc_5F9(): pass

    label('loc_5F9')

    Jump('loc_6D8')

    def _loc_5FC(): pass

    label('loc_5FC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_64A',
    )

    ChrSetPos(0x0008, 41870, 0, 61820, 270)
    ChrSetFlags(0x0008, 0x0010)
    ChrSetPos(0x000A, 40930, 0, 61820, 90)
    ChrSetFlags(0x000A, 0x0010)
    CreateThread(0x0009, 0x00, 0x00, func_03_9D8)
    ChrSetPos(0x0009, 34530, 0, 75930, 270)

    Jump('loc_6D8')

    def _loc_64A(): pass

    label('loc_64A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_69D',
    )

    ChrSetPos(0x0008, 41870, 0, 61820, 0)
    ChrSetPos(0x000A, 45950, 0, 61990, 0)
    ChrSetFlags(0x000B, 0x0080)
    CreateThread(0x0009, 0x00, 0x00, func_03_9D8)
    ChrSetPos(0x0009, 34530, 0, 75930, 270)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000D, 0x0080)

    Jump('loc_6D8')

    def _loc_69D(): pass

    label('loc_69D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_6CE',
    )

    ChrSetPos(0x000A, 45950, 0, 61990, 0)
    CreateThread(0x0009, 0x00, 0x00, func_03_9D8)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000D, 0x0080)
    ChrClearFlags(0x0012, 0x0080)

    Jump('loc_6D8')

    def _loc_6CE(): pass

    label('loc_6CE')

    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0011, 0x0080)

    def _loc_6D8(): pass

    label('loc_6D8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_705',
    )

    OP_28(0x0088, 0x01, 0x0010)
    OP_28(0x0088, 0x01, 0x0020)
    OP_28(0x0088, 0x01, 0x0040)
    OP_28(0x006C, 0x04, 0x40)
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    MapSetFlags(0x10000000)
    Event(0, func_16_3CD4)

    Jump('loc_71E')

    def _loc_705(): pass

    label('loc_705')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_71E',
    )

    OP_28(0x006C, 0x01, 0x0020)
    OP_28(0x006C, 0x04, 0x10)
    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    Event(1, 0x0002)

    def _loc_71E(): pass

    label('loc_71E')

    Return()

# id: 0x0001 offset: 0x71F
@scena.Code('func_01_71F')
def func_01_71F():
    OP_16(0x02, 4000, -93000, -69000, 2293841)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_79E',
    )

    OP_72(0x000E, 0x0008)
    OP_72(0x0010, 0x0008)
    OP_76(0x00FF, 0x00000025, 0x0000, 0, 0, 0, 0x00, 0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_77E',
    )

    OP_A1(0x0013, 0x0011)
    ChrSetPos(0x0013, 20000, 0, 55180, 270)

    Jump('loc_79B')

    def _loc_77E(): pass

    label('loc_77E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_79B',
    )

    OP_A1(0x0013, 0x0011)
    ChrSetPos(0x0013, 32590, 0, 59100, 90)

    def _loc_79B(): pass

    label('loc_79B')

    Jump('loc_7CF')

    def _loc_79E(): pass

    label('loc_79E')

    CreateThread(0x000E, 0x00, 0x00, func_1B_41BC)
    OP_6F(0x0010, 40)
    OP_70(0x0010, 0)
    OP_25(0x00A0, 460, 2780, 58940, 10000, 30000, 0x64, 0x00000000)
    def _loc_7CF(): pass

    label('loc_7CF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_7E0',
    )

    OP_71(0x0011, 0x0004)

    def _loc_7E0(): pass

    label('loc_7E0')

    If(
        (
            (Expr.Eval, "OP_29(0x006C, 0x00, 0x10)"),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x006C, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_800',
    )

    OP_71(0x0001, 0x0004)
    OP_72(0x0015, 0x0004)

    Jump('loc_80E')

    def _loc_800(): pass

    label('loc_800')

    OP_72(0x0001, 0x0004)
    OP_71(0x0015, 0x0004)
    OP_64(0x02, 0x0001)

    def _loc_80E(): pass

    label('loc_80E')

    If(
        (
            (Expr.Eval, "OP_29(0x006C, 0x00, 0x40)"),
            (Expr.Eval, "OP_29(0x006C, 0x01, 0x0004)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_82C',
    )

    OP_71(0x0016, 0x0004)
    OP_64(0x03, 0x0001)

    Jump('loc_83B')

    def _loc_82C(): pass

    label('loc_82C')

    If(
        (
            (Expr.Eval, "OP_29(0x006C, 0x00, 0x08)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_83B',
    )

    OP_64(0x03, 0x0001)

    def _loc_83B(): pass

    label('loc_83B')

    If(
        (
            (Expr.Eval, "OP_29(0x006C, 0x00, 0x40)"),
            (Expr.Eval, "OP_29(0x006C, 0x01, 0x0008)"),
            Expr.Ez,
            Expr.Or,
            (Expr.Eval, "OP_29(0x006C, 0x01, 0x0010)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_85A',
    )

    OP_64(0x01, 0x0001)

    def _loc_85A(): pass

    label('loc_85A')

    Return()

# id: 0x0002 offset: 0x85B
@scena.Code('func_02_85B')
def func_02_85B():
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
        'loc_880',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_9C2')

    def _loc_880(): pass

    label('loc_880')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_899',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_9C2')

    def _loc_899(): pass

    label('loc_899')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8B2',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_9C2')

    def _loc_8B2(): pass

    label('loc_8B2')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8CB',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_9C2')

    def _loc_8CB(): pass

    label('loc_8CB')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8E4',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_9C2')

    def _loc_8E4(): pass

    label('loc_8E4')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8FD',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_9C2')

    def _loc_8FD(): pass

    label('loc_8FD')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_916',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_9C2')

    def _loc_916(): pass

    label('loc_916')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_92F',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_9C2')

    def _loc_92F(): pass

    label('loc_92F')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_948',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_9C2')

    def _loc_948(): pass

    label('loc_948')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_961',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_9C2')

    def _loc_961(): pass

    label('loc_961')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_97A',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_9C2')

    def _loc_97A(): pass

    label('loc_97A')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_993',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_9C2')

    def _loc_993(): pass

    label('loc_993')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_9AC',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_9C2')

    def _loc_9AC(): pass

    label('loc_9AC')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_9C2',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_9C2(): pass

    label('loc_9C2')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_9D7',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_9C2')

    def _loc_9D7(): pass

    label('loc_9D7')

    Return()

# id: 0x0003 offset: 0x9D8
@scena.Code('func_03_9D8')
def func_03_9D8():
    ExecExpressionWithReg(
        0x0002,
        (
            Expr.Rand,
            (Expr.PushLong, 0x3),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Switch(
        (
            (Expr.PushReg, 0x2),
            Expr.Return,
        ),
        (0x00000000, 'loc_9F9'),
        (0x00000001, 'loc_A17'),
        (0x00000002, 'loc_A35'),
        (-1, 'loc_A8F'),
    )

    def _loc_9F9(): pass

    label('loc_9F9')

    ChrSetPos(0x0009, 34000, 0, 71810, 90)

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x64),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_A8F')

    def _loc_A17(): pass

    label('loc_A17')

    ChrSetPos(0x0009, 10000, 0, 71120, 90)

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x66),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_A8F')

    def _loc_A35(): pass

    label('loc_A35')

    ChrSetPos(0x0009, 21000, 0, 69900, 357)
    ChrWalkTo(0x00FE, 21000, 0, 74530, 2000, 0x00)
    ChrWalkTo(0x00FE, 20590, 0, 75310, 2000, 0x00)
    ChrWalkTo(0x00FE, 19920, 0, 76000, 2000, 0x00)

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x65),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_A8F')

    def _loc_A8F(): pass

    label('loc_A8F')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_BE7',
    )

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x64),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_AEB',
    )

    ChrWalkTo(0x00FE, 34000, 0, 74020, 2000, 0x00)
    ChrWalkTo(0x00FE, 32880, 0, 75340, 2000, 0x00)
    ChrWalkTo(0x00FE, 31930, 0, 76000, 2000, 0x00)

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x65),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_AEB(): pass

    label('loc_AEB')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x65),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B3E',
    )

    ChrWalkTo(0x00FE, 11650, 0, 76000, 2000, 0x00)
    ChrWalkTo(0x00FE, 10560, 0, 75370, 2000, 0x00)
    ChrWalkTo(0x00FE, 10000, 0, 74260, 2000, 0x00)

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x66),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_B3E(): pass

    label('loc_B3E')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x66),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B91',
    )

    ChrWalkTo(0x00FE, 10000, 0, 62290, 2000, 0x00)
    ChrWalkTo(0x00FE, 10920, 0, 61540, 2000, 0x00)
    ChrWalkTo(0x00FE, 12130, 0, 60500, 2000, 0x00)

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x67),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_B91(): pass

    label('loc_B91')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x67),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_BE4',
    )

    ChrWalkTo(0x00FE, 32830, 0, 60500, 2000, 0x00)
    ChrWalkTo(0x00FE, 33860, 0, 61430, 2000, 0x00)
    ChrWalkTo(0x00FE, 34000, 0, 62600, 2000, 0x00)

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x64),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_BE4(): pass

    label('loc_BE4')

    Jump('loc_A8F')

    def _loc_BE7(): pass

    label('loc_BE7')

    Return()

# id: 0x0004 offset: 0xBE8
@scena.Code('func_04_BE8')
def func_04_BE8():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_C0B',
    )

    OP_8D(0x00FE, 17690, 58310, 20560, 61470, 1000)

    Jump('func_04_BE8')

    def _loc_C0B(): pass

    label('loc_C0B')

    Return()

# id: 0x0005 offset: 0xC0C
@scena.Code('func_05_C0C')
def func_05_C0C():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_C2F',
    )

    OP_8D(0x00FE, 40220, 54770, 45110, 57860, 1000)

    Jump('func_05_C0C')

    def _loc_C2F(): pass

    label('loc_C2F')

    Return()

# id: 0x0006 offset: 0xC30
@scena.Code('func_06_C30')
def func_06_C30():
    TalkBegin(0x0012)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AF, 4, 0x57C)),
            Expr.Return,
        ),
        'loc_C3D',
    )

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    def _loc_C3D(): pass

    label('loc_C3D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_CB3',
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
        100,
        0,
        (
            TXT(0x00, '【◇在前作中与王相识】\n'),
            TXT(0x01, '【◇在前作中不认识王】\n'),
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
        (0x00000000, 'loc_CA7'),
        (0x00000001, 'loc_CAD'),
        (-1, 'loc_CB3'),
    )

    def _loc_CA7(): pass

    label('loc_CA7')

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    Jump('loc_CB3')

    def _loc_CAD(): pass

    label('loc_CAD')

    ClearScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    Jump('loc_CB3')

    def _loc_CB3(): pass

    label('loc_CB3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_F92',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0419, 2, 0x20CA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_ED5',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，来了吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 7, 0x1427)),
            Expr.Return,
        ),
        'loc_D1D',
    )

    ChrTalk(
        0x0101,
        (
            '#1011F啊，这不是王吗！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '你怎么会在这里？\n',
            '到底怎么了呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D3F')

    def _loc_D1D(): pass

    label('loc_D1D')

    ChrTalk(
        0x0101,
        (
            '#1015F？？？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '到底怎么了呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D3F(): pass

    label('loc_D3F')

    ChrTurnDirection(0x0012, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '啊啊，护卫的搬运车\n',
            '忽然停住不动了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真让人头疼啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0013, 400)
    OP_62(0x0101, 0x00000000, 2000, 0x0E, 0x0F, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#1019F嗯、嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '却偏偏\n',
            '在这种地方……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1048F这样的话就会\n',
            '严重妨碍通行了啊。',
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
        'loc_E28',
    )

    ChrTalk(
        0x0107,
        (
            '#561F……真是的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E7B')

    def _loc_E28(): pass

    label('loc_E28')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E50',
    )

    ChrTalk(
        0x0106,
        (
            '#551F……真的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E7B')

    def _loc_E50(): pass

    label('loc_E50')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E7B',
    )

    ChrTalk(
        0x0103,
        (
            '#025F……哎呀呀，是呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E7B(): pass

    label('loc_E7B')

    ChrTalk(
        0x00FE,
        (
            '确、确实啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，虽然很麻烦，\n',
            '但不想办法把它挪走的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x00FE, 0, 0)
    ChrClearFlags(0x00FE, 0x0010)
    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))
    SetScenaFlags(ScenaFlag(0x0419, 2, 0x20CA))

    Jump('loc_F8F')

    def _loc_ED5(): pass

    label('loc_ED5')

    If(
        (
            (Expr.PushLong, 0xA),
            Expr.Return,
        ),
        'loc_F31',
    )

    ChrTalk(
        0x00FE,
        (
            '搬运车竟然在\n',
            '这种地方不动了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然很麻烦，\n',
            '但不想办法把它挪走的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F8F')

    def _loc_F31(): pass

    label('loc_F31')

    ChrTalk(
        0x00FE,
        (
            '护卫的搬运车\n',
            '竟然停在这种地方不动了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，虽然很麻烦，\n',
            '但不想办法把它挪走的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F8F(): pass

    label('loc_F8F')

    Jump('loc_16DF')

    def _loc_F92(): pass

    label('loc_F92')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 7, 0x1427)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_11A4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_115F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_10EF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_1031',
    )

    ChrTalk(
        0x00FE,
        (
            '等修好之后\n',
            '还要继续进行护卫。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '导力器的输出工作\n',
            '还是和以前一样顺利啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '已经快忙不过来了，\n',
            '布鲁诺偏偏还不在。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10EC')

    def _loc_1031(): pass

    label('loc_1031')

    ChrTalk(
        0x00FE,
        (
            '等修好之后\n',
            '还要继续进行护卫。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最近出现了很多危险的魔兽，\n',
            '这种工作也变得很麻烦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么…在出发之前\n',
            '先去『福格尔酒馆』吃点东西吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '做往返护卫的任务\n',
            '真是很花时间啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    def _loc_10EC(): pass

    label('loc_10EC')

    Jump('loc_115C')

    def _loc_10EF(): pass

    label('loc_10EF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 0, 0x1408)),
            Expr.Return,
        ),
        'loc_115C',
    )

    ChrTalk(
        0x00FE,
        (
            '可能的话，我也想\n',
            '自己挑选工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '以后你们要是接到什么重要调查的话\n',
            '也分配一些简单任务给我吧，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_115C(): pass

    label('loc_115C')

    Jump('loc_11A1')

    def _loc_115F(): pass

    label('loc_115F')

    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '不好意思，\n',
            '很想帮到你们一些忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大家一起加油吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_11A1(): pass

    label('loc_11A1')

    Jump('loc_16DF')

    def _loc_11A4(): pass

    label('loc_11A4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_1363',
    )

    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_12B0',
    )

    ChrTalk(
        0x00FE,
        (
            '呀，好久不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还记得我吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1001F当然记得啦！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '你不是蔡斯支部\n',
            '的王吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈哈，谢谢，竟然还记得我。\n',
            '能再次相遇真是高兴啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你终于顺利晋升为\n',
            '正游击士了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '恭喜！\n',
            '凭你的实力，这也是理所当然的结果。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1360')

    def _loc_12B0(): pass

    label('loc_12B0')

    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '啊，这不是艾丝蒂尔吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1004F咦……？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1018F啊，我还说是谁，\n',
            '这不是王吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你终于顺利晋升为\n',
            '正游击士了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '恭喜！\n',
            '凭你的实力，这也是理所当然的结果。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1360(): pass

    label('loc_1360')

    Jump('loc_14AB')

    def _loc_1363(): pass

    label('loc_1363')

    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '…………哎呀？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你不就是…\n',
            '最近才转正的艾丝蒂尔吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1004F哎哎，是的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊，失礼了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我是王。\n',
            '蔡斯地区的游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1000F啊～是吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我是艾丝蒂尔·布莱特。\n',
            '麻烦您了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊啊，请多关照。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们的事情\n',
            '我也早有耳闻了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是立了大功啊，\n',
            '升为正游击士也是理所当然的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_14AB(): pass

    label('loc_14AB')

    ChrTalk(
        0x0101,
        (
            '#1008F嘿嘿，谢谢夸奖。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我们也还差得远呢，\n',
            '还需要不断努力进步。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯…保持上进心，永不懈怠吗…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这种谦虚的态度\n',
            '我也要多多学习。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对了，冈多夫\n',
            '出去办事了，你们知道吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1011F啊，嗯。\n',
            '从嘉恩那里听说了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我们就是为了增援\n',
            '才特意来蔡斯的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是这样吗。\n',
            '谢啦，真是帮了大忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是不好意思，\n',
            '很想帮到你们一些忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_165B',
    )

    ChrTurnDirection(0x00FE, 0x0106, 400)

    ChrTalk(
        0x00FE,
        (
            '阿加特前辈也是，\n',
            '就请你们多多关照了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#051F哪里，也请你们多关照了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_16A2')

    def _loc_165B(): pass

    label('loc_165B')

    ChrTurnDirection(0x00FE, 0x0103, 400)

    ChrTalk(
        0x00FE,
        (
            '雪拉扎德也\n',
            '请多多关照了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F哪里的话，互相关照吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_16A2(): pass

    label('loc_16A2')

    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '我也竭尽全力哟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，大家都加油吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0284, 7, 0x1427))
    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))
    def _loc_16DF(): pass

    label('loc_16DF')

    TalkEnd(0x0012)

    Return()

# id: 0x0007 offset: 0x16E3
@scena.Code('func_07_16E3')
def func_07_16E3():
    TalkBegin(0x0011)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_1733',
    )

    ChrTalk(
        0x00FE,
        (
            '最近我的孙女\n',
            '也一直频繁出入中央工房。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真让人放心不下啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17CB')

    def _loc_1733(): pass

    label('loc_1733')

    ChrTalk(
        0x00FE,
        (
            '嗯，不过看起来\n',
            '城里也没有发生太大的事故。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '算啦，这种程度的摇晃\n',
            '应该还不至于影响到中央工房。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为地震事件，\n',
            '出现了接连不断的受害事件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    def _loc_17CB(): pass

    label('loc_17CB')

    TalkEnd(0x0011)

    Return()

# id: 0x0008 offset: 0x17CF
@scena.Code('func_08_17CF')
def func_08_17CF():
    TalkBegin(0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_18E3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1878',
    )

    ChrTalk(
        0x00FE,
        (
            '再这样下去的话\n',
            '整个王国也都会被波及吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '想顺利解决这次危机的话\n',
            '就只有靠中央工房了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不管怎样，总之希望能尽快\n',
            '重新开始研究活动啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    Jump('loc_18E0')

    def _loc_1878(): pass

    label('loc_1878')

    ChrTalk(
        0x00FE,
        (
            '虽然拉赛尔博士不在，\n',
            '但你们也是很优秀能干的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只要发挥出中央工房的力量\n',
            '就一定可以解决危机的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_18E0(): pass

    label('loc_18E0')

    Jump('loc_19B2')

    def _loc_18E3(): pass

    label('loc_18E3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_1945',
    )

    ChrTalk(
        0x00FE,
        (
            '我在蔡斯市内\n',
            '经营武器店。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就是游击士协会对面的那家店，\n',
            '有机会的话多来光顾吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19B2')

    def _loc_1945(): pass

    label('loc_1945')

    ChrTalk(
        0x00FE,
        (
            '嗯，好像没有余震了，\n',
            '店应该不要紧吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过真奇怪，竟然会有地震。\n',
            '利贝尔可是很少发生地震的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    def _loc_19B2(): pass

    label('loc_19B2')

    TalkEnd(0x0010)

    Return()

# id: 0x0009 offset: 0x19B6
@scena.Code('func_09_19B6')
def func_09_19B6():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1D45',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0419, 1, 0x20C9)),
            Expr.Ez,
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1B57',
    )

    OP_62(0x00FE, 0x00000000, 1700, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x00FE, 0x0107, 0)
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '啊～提妲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好像发生了什么\n',
            '大事的样子哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#063F嗯……\n',
            '库诺不要紧吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '店里的生意一直很好，\n',
            '当然不要紧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '倒是提妲你啊…\n',
            '最近博士很头疼吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#562F嗯、嗯…爷爷他\n',
            '最近确实一直都很为难，不过……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#562F爷爷越在这种时候就越有干劲，\n',
            '一定不会放弃的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嘿嘿～好厉害啊。\n',
            '真不愧是拉赛尔博士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '中央工房的人\n',
            '果然就是不一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))
    SetScenaFlags(ScenaFlag(0x0419, 1, 0x20C9))

    Jump('loc_1D42')

    def _loc_1B57(): pass

    label('loc_1B57')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1BC6',
    )

    ChrTalk(
        0x00FE,
        (
            '在这种危机的情况下\n',
            '仍然还这么泰然自若……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真不愧是拉赛尔博士啊。\n',
            '期待他的成果！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D42')

    def _loc_1BC6(): pass

    label('loc_1BC6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_1CAF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1C58',
    )

    ChrTalk(
        0x00FE,
        (
            '现在的鱼和水果还都是\n',
            '很新鲜的货，不过……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大部分的商品\n',
            '都是用定期船运来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是一直这样的话\n',
            '这里可就惨了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_1CAC')

    def _loc_1C58(): pass

    label('loc_1C58')

    ChrTalk(
        0x00FE,
        (
            '鱼和水果几乎都是用\n',
            '定期船来运送的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果一直这么下去的话\n',
            '这里可就惨了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1CAC(): pass

    label('loc_1CAC')

    Jump('loc_1D42')

    def _loc_1CAF(): pass

    label('loc_1CAF')

    ChrTalk(
        0x00FE,
        (
            '如果是中央工房的人\n',
            '应该可以很快找出原因才对啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是不知为何，\n',
            '到现在好像也没有任何头绪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在大家都很困扰，\n',
            '还要更加努力才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1D42(): pass

    label('loc_1D42')

    Jump('loc_2051')

    def _loc_1D45(): pass

    label('loc_1D45')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_1D76',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_1D6F',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，客人\n',
            '太多了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D73')

    def _loc_1D6F(): pass

    label('loc_1D6F')

    Call(0, 0x000D)

    def _loc_1D73(): pass

    label('loc_1D73')

    Jump('loc_2051')

    def _loc_1D76(): pass

    label('loc_1D76')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_1E7F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_1DD7',
    )

    ChrTalk(
        0x00FE,
        (
            '要赶快把水果\n',
            '摆放好才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊啊～～真希望博士\n',
            '能早点把地震事件平息啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E7C')

    def _loc_1DD7(): pass

    label('loc_1DD7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0286, 2, 0x1432)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1DE6',
    )

    Call(0, 0x000C)

    Jump('loc_1E7C')

    def _loc_1DE6(): pass

    label('loc_1DE6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_1E3C',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯…堆太高的话\n',
            '一有地震就不得了了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '到时苹果也许会滚得\n',
            '满街都是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E7C')

    def _loc_1E3C(): pass

    label('loc_1E3C')

    ChrTalk(
        0x00FE,
        (
            '已经把水果摆放好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样摆放的话\n',
            '看起来很漂亮啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_1E7C(): pass

    label('loc_1E7C')

    Jump('loc_2051')

    def _loc_1E7F(): pass

    label('loc_1E7F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 7, 0x1417)),
            Expr.Return,
        ),
        'loc_1EED',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0286, 2, 0x1432)),
            Expr.Return,
        ),
        'loc_1EE6',
    )

    ChrTalk(
        0x00FE,
        (
            '那么，要赶快把商品\n',
            '摆好才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊啊～～真希望博士\n',
            '能早点把地震事件平息啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1EEA')

    def _loc_1EE6(): pass

    label('loc_1EE6')

    Call(0, 0x000C)

    def _loc_1EEA(): pass

    label('loc_1EEA')

    Jump('loc_2051')

    def _loc_1EED(): pass

    label('loc_1EED')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_1F97',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_1F4C',
    )

    ChrTalk(
        0x00FE,
        (
            '终于把商品重新\n',
            '摆放好了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但如果再出现\n',
            '一次地震的话该如何是好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F94')

    def _loc_1F4C(): pass

    label('loc_1F4C')

    ChrTalk(
        0x00FE,
        (
            '呼～终于把桔子\n',
            '摆放好了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼呼～这下就和原来一样完美了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_1F94(): pass

    label('loc_1F94')

    Jump('loc_2051')

    def _loc_1F97(): pass

    label('loc_1F97')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 0, 0x1408)),
            Expr.Return,
        ),
        'loc_2051',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_1FFA',
    )

    ChrTalk(
        0x00FE,
        (
            '必须要赶快把\n',
            '商品重新摆好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这种乱七八糟的丢人样子\n',
            '可不能给客人看见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2051')

    def _loc_1FFA(): pass

    label('loc_1FFA')

    ChrTalk(
        0x00FE,
        (
            '可恶！！花好大力气\n',
            '才弄好的展柜全都震坏了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可恶的地震～\n',
            '不可原谅啊～！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_2051(): pass

    label('loc_2051')

    TalkEnd(0x0008)

    Return()

# id: 0x000A offset: 0x2055
@scena.Code('func_0A_2055')
def func_0A_2055():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_219E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2129',
    )

    ChrTalk(
        0x00FE,
        (
            '导力灯现在不能用了，\n',
            '好像每天很早就天黑了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然确实很不方便，不过\n',
            '从健康角度来考虑的话好像也不错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '日出时起床，\n',
            '日落时睡觉，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们年轻的时候\n',
            '就一直是这样的作息时间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Jump('loc_219B')

    def _loc_2129(): pass

    label('loc_2129')

    ChrTalk(
        0x00FE,
        (
            '导力灯现在不能用了，\n',
            '好像每天很早就天黑了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然确实很不方便，不过\n',
            '从健康角度来考虑的话好像也不错呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_219B(): pass

    label('loc_219B')

    Jump('loc_263F')

    def _loc_219E(): pass

    label('loc_219E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_2273',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2226',
    )

    ChrTalk(
        0x00FE,
        (
            '连电梯\n',
            '也不能用了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看来导力工厂也\n',
            '完全失去机能了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是不能制造导力器的话，\n',
            '蔡斯可怎么办啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Jump('loc_2270')

    def _loc_2226(): pass

    label('loc_2226')

    ChrTalk(
        0x00FE,
        (
            '导力器产业可是\n',
            '这城市的生命线啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可是……\n',
            '竟然发生了这种事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2270(): pass

    label('loc_2270')

    Jump('loc_263F')

    def _loc_2273(): pass

    label('loc_2273')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_22CB',
    )

    ChrTalk(
        0x00FE,
        (
            '不知在什么时候\n',
            '放出了安全宣言。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎呀，到最后\n',
            '也是毫无来由的地震啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_263F')

    def _loc_22CB(): pass

    label('loc_22CB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_23F8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_2334',
    )

    ChrTalk(
        0x00FE,
        (
            '兰达的孙女\n',
            '好像也进中央工房了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这是和完成了新型引擎\n',
            '同样值得高兴的消息啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23F5')

    def _loc_2334(): pass

    label('loc_2334')

    ChrTalk(
        0x00FE,
        (
            '兰达的孙女\n',
            '好像也进中央工房了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这是和完成了新型引擎\n',
            '同样值得高兴的消息啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在的年轻人都\n',
            '想进入中央工房工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在当今的时代，\n',
            '技术力已经变成推动世界发展的最大动力了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_23F5(): pass

    label('loc_23F5')

    Jump('loc_263F')

    def _loc_23F8(): pass

    label('loc_23F8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_2547',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_2465',
    )

    ChrTalk(
        0x00FE,
        (
            '其实在这片大地上\n',
            '除了导力之外也还有其他的力量呢，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大自然确实是\n',
            '非常神秘的存在啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2544')

    def _loc_2465(): pass

    label('loc_2465')

    ChrTalk(
        0x00FE,
        (
            '虽然很多东西并不为人所知……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '其实在这片大地上\n',
            '但也确实是存在的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '像这次七耀石的矿脉上\n',
            '流动着力量波纹的现象……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然在规模上有些不同，\n',
            '但和结晶回路是一个原理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，大自然真的是\n',
            '不可思议的存在啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_2544(): pass

    label('loc_2544')

    Jump('loc_263F')

    def _loc_2547(): pass

    label('loc_2547')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 0, 0x1408)),
            Expr.Return,
        ),
        'loc_263F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_25B4',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯，街上的时钟\n',
            '好像一点也没有慢啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '已经是４０年前制造的东西了，\n',
            '竟然还这么结实。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_263F')

    def _loc_25B4(): pass

    label('loc_25B4')

    ChrTalk(
        0x00FE,
        (
            '嗯，街上的时钟\n',
            '好像一点也没有慢啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '已经是４０年前制造的东西了，\n',
            '竟然还这么结实。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈哈哈～简直就像拉赛尔那个老头子一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_263F(): pass

    label('loc_263F')

    TalkEnd(0x0009)

    Return()

# id: 0x000B offset: 0x2643
@scena.Code('func_0B_2643')
def func_0B_2643():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_26AD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_26A6',
    )

    ChrTalk(
        0x00FE,
        (
            '竟然一眼就看出来了，\n',
            '果然是职业的啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵呵，和你商量算是找对人了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_26AA')

    def _loc_26A6(): pass

    label('loc_26A6')

    Call(0, 0x000D)

    def _loc_26AA(): pass

    label('loc_26AA')

    Jump('loc_2930')

    def _loc_26AD(): pass

    label('loc_26AD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_2799',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_2718',
    )

    ChrTalk(
        0x00FE,
        (
            '也买过最右边的，\n',
            '不过……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '买来的苹果\n',
            '全部都是酸的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '倒霉～为什么会这样呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2796')

    def _loc_2718(): pass

    label('loc_2718')

    ChrTalk(
        0x00FE,
        (
            '虽然稍微有点经验了，\n',
            '但还是觉得买食物很麻烦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看起来的话\n',
            '哪个也都是一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈，还是决定\n',
            '听听店员的意见吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_2796(): pass

    label('loc_2796')

    Jump('loc_2930')

    def _loc_2799(): pass

    label('loc_2799')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_286B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_2802',
    )

    ChrTalk(
        0x00FE,
        (
            '爸爸让我来买\n',
            '『看起来就好吃的』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可是，『看起来就好吃』\n',
            '的苹果究竟是哪个呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2868')

    def _loc_2802(): pass

    label('loc_2802')

    ChrTalk(
        0x00FE,
        (
            '爸爸让我来买东西，\n',
            '不过……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他只说让我买\n',
            '『看起来好吃的』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那种说法\n',
            '会有谁能懂啊…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_2868(): pass

    label('loc_2868')

    Jump('loc_2930')

    def _loc_286B(): pass

    label('loc_286B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 0, 0x1408)),
            Expr.Return,
        ),
        'loc_2930',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_28C8',
    )

    ChrTalk(
        0x00FE,
        (
            '想买罐头，\n',
            '但是现在买不了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说是休整中……\n',
            '不过到底在休整什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2930')

    def _loc_28C8(): pass

    label('loc_28C8')

    ChrTalk(
        0x00FE,
        (
            '今天本来是来买罐头的，\n',
            '不过……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说是在休整中，\n',
            '暂时不能买。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '休整中……\n',
            '在休整什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_2930(): pass

    label('loc_2930')

    TalkEnd(0x000A)

    Return()

# id: 0x000C offset: 0x2934
@scena.Code('func_0C_2934')
def func_0C_2934():
    ChrTurnDirection(0x0008, 0x0107, 0)

    ChrTalk(
        0x00FE,
        (
            '啊～提妲。\n',
            '欢迎。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好多人啊，\n',
            '他们都是博士的助手吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#067F喔～虽然不是，\n',
            '但也算是帮忙研究工作的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#560F库诺也在帮忙吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，要赶快把被地震弄乱\n',
            '的商品重新摆放好哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不知道博士对地震的研究\n',
            '现在怎么样了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '希望他能早点发明出一个\n',
            '能控制地震的好东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '提妲也要\n',
            '努力帮忙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#061F嗯！在主日学校再见吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))
    SetScenaFlags(ScenaFlag(0x0286, 2, 0x1432))

    Return()

# id: 0x000D offset: 0x2A92
@scena.Code('func_0D_2A92')
def func_0D_2A92():
    OP_4A(0x0008, 255)
    OP_4A(0x000A, 255)

    ChrTalk(
        0x000A,
        (
            '啊……那个……\n',
            '抱歉，打扰你工作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '这家店里有没有卖\n',
            '『看起来很好吃』的苹果？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '看起来好吃的苹果？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '嗯……那就是颜色好看\n',
            '的苹果了嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0008, 0, 500)

    ChrTalk(
        0x0008,
        (
            '……那个如何？\n',
            '看起来应该很好吃的样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '哇，厉害。\n',
            '一眼就能看出来吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '啊啊！专业的果然就是不一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x000A, 500)

    ChrTalk(
        0x0008,
        (
            '不、不是什么\n',
            '值得佩服的大事吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '只不过是代选了\n',
            '一下而已啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4B(0x0008, 255)
    OP_4B(0x000A, 255)
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    ChrClearFlags(0x0008, 0x0010)
    ChrClearFlags(0x000A, 0x0010)

    Return()

# id: 0x000E offset: 0x2C12
@scena.Code('func_0E_2C12')
def func_0E_2C12():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_2CFB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2CC1',
    )

    ChrTalk(
        0x00FE,
        (
            '叫大家帮忙一起把搬运车\n',
            '推到路边自然最好，不过……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '正如我预想的一样，\n',
            '车子并没有任何异常状况啊，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是没办法。\n',
            '车上的东西还要急着运送……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Jump('loc_2CF8')

    def _loc_2CC1(): pass

    label('loc_2CC1')

    ChrTalk(
        0x00FE,
        (
            '真伤脑筋……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可不管怎么检查\n',
            '也发现不了问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2CF8(): pass

    label('loc_2CF8')

    Jump('loc_2F90')

    def _loc_2CFB(): pass

    label('loc_2CFB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_2D7D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2D4B',
    )

    ChrTalk(
        0x00FE,
        (
            '接下来我也要\n',
            '检查搬运车了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……好不容易等到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Jump('loc_2D7A')

    def _loc_2D4B(): pass

    label('loc_2D4B')

    ChrTalk(
        0x00FE,
        (
            '接下来轮到我的搬运车了。\n',
            '终于轮到我了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2D7A(): pass

    label('loc_2D7A')

    Jump('loc_2F90')

    def _loc_2D7D(): pass

    label('loc_2D7D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_2E33',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_2DD1',
    )

    ChrTalk(
        0x00FE,
        (
            '呼～下一站是王都了么，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看来这次又要委托王\n',
            '进行护卫了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2E30')

    def _loc_2DD1(): pass

    label('loc_2DD1')

    ChrTalk(
        0x00FE,
        (
            '已经不会再有地震了，\n',
            '玛多克工房长亲口说过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样下去的话\n',
            '简直就是大自然的惩罚啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_2E30(): pass

    label('loc_2E30')

    Jump('loc_2F90')

    def _loc_2E33(): pass

    label('loc_2E33')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_2EC2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_2E7D',
    )

    ChrTalk(
        0x00FE,
        (
            '没时间因为地震之类的\n',
            '东西惊叹了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '赶快工作吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2EBF')

    def _loc_2E7D(): pass

    label('loc_2E7D')

    ChrTalk(
        0x00FE,
        (
            '呼～还是这么忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '蔡斯的导力器\n',
            '还是和以前一样受好评。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_2EBF(): pass

    label('loc_2EBF')

    Jump('loc_2F90')

    def _loc_2EC2(): pass

    label('loc_2EC2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 0, 0x1408)),
            Expr.Return,
        ),
        'loc_2F90',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_2F18',
    )

    ChrTalk(
        0x00FE,
        (
            '呼～没有太大的受害情况\n',
            '就算是万幸了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '喔，还是赶快工作吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F90')

    def _loc_2F18(): pass

    label('loc_2F18')

    ChrTalk(
        0x00FE,
        (
            '虽然有些摇晃，\n',
            '不过现在已经停止了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '之前去沃尔费堡垒的时候\n',
            '也遇到小地震了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '震动比最近的地震\n',
            '还要小。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_2F90(): pass

    label('loc_2F90')

    TalkEnd(0x000B)

    Return()

# id: 0x000F offset: 0x2F94
@scena.Code('func_0F_2F94')
def func_0F_2F94():
    TalkBegin(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_3081',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_2FF7',
    )

    ChrTalk(
        0x00FE,
        (
            '中央工房好像已经做了发表，\n',
            '说今后不会再有地震了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总算是松了口气啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_307E')

    def _loc_2FF7(): pass

    label('loc_2FF7')

    ChrTalk(
        0x00FE,
        (
            '虽然听老公说过了，\n',
            '但真的不会再发生了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '本来为了保护花坛\n',
            '还特意想了很多防震对策呢…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，不管怎么说，总算松了口气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_307E(): pass

    label('loc_307E')

    Jump('loc_315E')

    def _loc_3081(): pass

    label('loc_3081')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 0, 0x1408)),
            Expr.Return,
        ),
        'loc_315E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_30EA',
    )

    ChrTalk(
        0x00FE,
        (
            '这是个难得的机会，\n',
            '正想改变花坛的放置位置呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，那好。\n',
            '一会儿就去看看花吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_315E')

    def _loc_30EA(): pass

    label('loc_30EA')

    ChrTalk(
        0x00FE,
        (
            '呼，还好。\n',
            '花坛总算没事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '地震也许还会再来，\n',
            '不能让它们被震倒啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯……不过\n',
            '该怎么摆放才好呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_315E(): pass

    label('loc_315E')

    TalkEnd(0x000C)

    Return()

# id: 0x0010 offset: 0x3162
@scena.Code('func_10_3162')
def func_10_3162():
    TalkBegin(0x000D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_3303',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_32BC',
    )

    ChrTalk(
        0x00FE,
        (
            '现在发生的这些\n',
            '好像是导力停止现象……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，究竟是什么原因\n',
            '引发了这种现象呢？',
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
        'loc_327F',
    )

    ChrTurnDirection(0x000D, 0x0107, 400)

    ChrTalk(
        0x00FE,
        (
            '……提妲。\n',
            '博士需要什么指示吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#064F哎……！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#067F嗯、嗯……\n',
            '好像还在苦恼中呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么说的话，\n',
            '这种状况还要持续一阵了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_32B6')

    def _loc_327F(): pass

    label('loc_327F')

    ChrTalk(
        0x00FE,
        (
            '如果不能找到原因，\n',
            '想解决这次的事情可就很困难了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_32B6(): pass

    label('loc_32B6')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    Jump('loc_3300')

    def _loc_32BC(): pass

    label('loc_32BC')

    ChrTalk(
        0x00FE,
        (
            '我想这次的现象\n',
            '正是导力停止现象。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过规模实在\n',
            '也太大了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_3300(): pass

    label('loc_3300')

    Jump('loc_347B')

    def _loc_3303(): pass

    label('loc_3303')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_33D0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_336C',
    )

    ChrTalk(
        0x00FE,
        (
            '看来今后也要做好\n',
            '地震的预防工作啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '以前我们对这种事\n',
            '根本就没有任何预防措施。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_33CD')

    def _loc_336C(): pass

    label('loc_336C')

    ChrTalk(
        0x00FE,
        (
            '玛多克工房长已经\n',
            '发出安全宣言了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不管怎样，地震没造成\n',
            '人员伤亡就是不幸中的万幸了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    def _loc_33CD(): pass

    label('loc_33CD')

    Jump('loc_347B')

    def _loc_33D0(): pass

    label('loc_33D0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 0, 0x1408)),
            Expr.Return,
        ),
        'loc_347B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_343B',
    )

    ChrTalk(
        0x00FE,
        (
            '控制大地震动…\n',
            '真是可怕的能源啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '用中央工房的『卡佩尔』\n',
            '说不定可以计算出来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_347B')

    def _loc_343B(): pass

    label('loc_343B')

    ChrTalk(
        0x00FE,
        (
            '那就是地震吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我还是第一次体验到，\n',
            '真是厉害啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    def _loc_347B(): pass

    label('loc_347B')

    TalkEnd(0x000D)

    Return()

# id: 0x0011 offset: 0x347F
@scena.Code('func_11_347F')
def func_11_347F():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '『导力式时钟第１号机』\n',
            '　七耀日历１１６２年·蔡斯技术工房制造',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Return()

# id: 0x0012 offset: 0x34E7
@scena.Code('func_12_34E7')
def func_12_34E7():
    If(
        (
            (Expr.Eval, "OP_29(0x006C, 0x00, 0x04)"),
            (Expr.Eval, "OP_29(0x006C, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x006C, 0x01, 0x0004)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_350F',
    )

    OP_28(0x006C, 0x01, 0x0004)
    Call(1, 0x0000)
    TalkEnd(0x00FF)

    def _loc_350F(): pass

    label('loc_350F')

    Return()

# id: 0x0013 offset: 0x3510
@scena.Code('func_13_3510')
def func_13_3510():
    OP_28(0x006C, 0x01, 0x0010)
    Call(1, 0x0001)
    OP_64(0x01, 0x0001)
    TalkEnd(0x00FF)

    Return()

# id: 0x0014 offset: 0x3522
@scena.Code('func_14_3522')
def func_14_3522():
    If(
        (
            (Expr.Eval, "OP_29(0x006C, 0x00, 0x08)"),
            Expr.Return,
        ),
        'loc_3739',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x006C, 0x01, 0x1000)"),
            Expr.Return,
        ),
        'loc_35AB',
    )

    ChrTalk(
        0x0101,
        (
            '#0010450762V#1007F嗯～纹章的部分没有了，\n',
            '情况果然很糟糕呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010450763V#1002F不早点把招牌板找回来的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3736')

    def _loc_35AB(): pass

    label('loc_35AB')

    EventBegin(0x00)
    Fade(1000)
    CameraMove(28590, 0, 63210, 0)
    OP_67(0, 7280, -10000, 0)
    CameraSetDistance(2970, 0)
    OP_6C(314000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 28590, 0, 63210, 81)
    ChrSetPos(0x00F7, 28200, 0, 62550, 90)
    ChrSetPos(0x00F8, 27430, 0, 63190, 90)
    ChrSetPos(0x00F9, 27170, 0, 62250, 90)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010450764V#1002F#1P啊，这就是那个招牌板了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_36D1',
    )

    ChrTalk(
        0x0106,
        (
            '#0050450765V#052F#1P可是…\n',
            '究竟是怎么盗走的呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050450766V#551F真是个不得了的家伙呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_372E')

    def _loc_36D1(): pass

    label('loc_36D1')

    ChrTalk(
        0x0103,
        (
            '#0030450767V#025F#1P看来纹章部分\n',
            '已经被人盗走了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030450768V那家伙的手段真是厉害。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_372E(): pass

    label('loc_372E')

    OP_28(0x006C, 0x01, 0x1000)
    EventEnd(0x00)

    def _loc_3736(): pass

    label('loc_3736')

    Jump('loc_3B16')

    def _loc_3739(): pass

    label('loc_3739')

    If(
        (
            (Expr.Eval, "OP_29(0x006C, 0x01, 0x1000)"),
            Expr.Return,
        ),
        'loc_3836',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x006C, 0x00, 0x02)"),
            Expr.Return,
        ),
        'loc_37BF',
    )

    ChrTalk(
        0x0101,
        (
            '#0010450769V#1015F嗯……\n',
            '要怎么做好呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010450770V如果手上没什么别的事的话，\n',
            '不如去问问雾香小姐吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3833')

    def _loc_37BF(): pass

    label('loc_37BF')

    ChrTalk(
        0x0101,
        (
            '#0010450771V#1015F竟然连协会都会\n',
            '遇到这种事件吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010450772V要是手上没其他事的话，\n',
            '还是去确认一下这件事吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3833(): pass

    label('loc_3833')

    Jump('loc_3B16')

    def _loc_3836(): pass

    label('loc_3836')

    EventBegin(0x00)
    Fade(1000)
    CameraMove(28590, 0, 63210, 0)
    OP_67(0, 7280, -10000, 0)
    CameraSetDistance(2970, 0)
    OP_6C(314000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 28590, 0, 63210, 81)
    ChrSetPos(0x00F7, 28200, 0, 62550, 90)
    ChrSetPos(0x00F8, 27430, 0, 63190, 90)
    ChrSetPos(0x00F9, 27170, 0, 62250, 90)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010450773V#1004F啊？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010450774V这里的招牌板……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x006C, 0x00, 0x02)"),
            Expr.Return,
        ),
        'loc_3A0B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_3970',
    )

    ChrTalk(
        0x0106,
        (
            '#0050450775V#053F是啊，招牌板\n',
            '竟然变成这个样子了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050450776V#050F稍后去和雾香确认一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_39E4')

    def _loc_3970(): pass

    label('loc_3970')

    ChrTalk(
        0x0103,
        (
            '#0030450777V#022F说起来的话，招牌板\n',
            '居然变成这样了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030450778V#020F如果在意的话，\n',
            '稍后去问问雾香小姐吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_39E4(): pass

    label('loc_39E4')

    ChrTalk(
        0x0101,
        (
            '#0010450779V#1015F嗯……了解。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3B0E')

    def _loc_3A0B(): pass

    label('loc_3A0B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_3A5C',
    )

    ChrTalk(
        0x0106,
        (
            '#0050450780V#555F这是怎么回事？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050450781V中间部分被挖去了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3A9A')

    def _loc_3A5C(): pass

    label('loc_3A5C')

    ChrTalk(
        0x0103,
        (
            '#0030450782V#023F什么啊！？这个。\n',
            '中心部分竟然被挖掉了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3A9A(): pass

    label('loc_3A9A')

    ChrTalk(
        0x0101,
        (
            '#0010450783V#1015F嗯…也许协会里\n',
            '发生什么事了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010450772V要是手上没其他事的话，\n',
            '还是去确认一下这件事吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_3B0E(): pass

    label('loc_3B0E')

    OP_28(0x006C, 0x01, 0x1000)
    EventEnd(0x00)
    def _loc_3B16(): pass

    label('loc_3B16')

    TalkEnd(0x00FF)

    Return()

# id: 0x0015 offset: 0x3B1A
@scena.Code('func_15_3B1A')
def func_15_3B1A():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_3BF0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3BA7',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯，这个也没有\n',
            '发现任何异常啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '无法运转\n',
            '是因为导力停止现象。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然有点对不起布鲁诺，\n',
            '但也只有放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 5, 0xD))

    Jump('loc_3BED')

    def _loc_3BA7(): pass

    label('loc_3BA7')

    ChrTalk(
        0x00FE,
        (
            '无法运转\n',
            '是因为导力停止现象。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '抱歉啊，这个\n',
            '但也只有放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3BED(): pass

    label('loc_3BED')

    Jump('loc_3CD0')

    def _loc_3BF0(): pass

    label('loc_3BF0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_3CD0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3C8A',
    )

    ChrTalk(
        0x00FE,
        (
            '已经检查过了，\n',
            '但根本不是故障原因。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '似乎和以前那次导力停止现象\n',
            '是同样性质的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还有浮在湖上的岛…\n',
            '究竟发生什么了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 5, 0xD))

    Jump('loc_3CD0')

    def _loc_3C8A(): pass

    label('loc_3C8A')

    ChrTalk(
        0x00FE,
        (
            '自动扶梯\n',
            '没有任何故障，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这就是和上次一样的\n',
            '导力停止现象啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3CD0(): pass

    label('loc_3CD0')

    TalkEnd(0x00FE)

    Return()

# id: 0x0016 offset: 0x3CD4
@scena.Code('func_16_3CD4')
def func_16_3CD4():
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
        'loc_3CE7',
    )

    Call(0, 0x001E)

    def _loc_3CE7(): pass

    label('loc_3CE7')

    ChrSetStatus(ChrTable['金'], 0x00, 54)
    ChrSetStatus(ChrTable['金'], 0xFE, 0)
    EquipCmd(ChrTable['金'], 0x0000, 0xFF)
    EquipCmd(ChrTable['金'], ItemTable['兽皮拳套'], 0xFF)
    EquipCmd(ChrTable['金'], ItemTable['强化夹克'], 0xFF)
    EquipCmd(ChrTable['金'], ItemTable['纤维靴'], 0xFF)
    EquipCmd(ChrTable['金'], ItemTable['防御３'], 0x00)
    EquipCmd(ChrTable['金'], ItemTable['ＨＰ１'], 0x01)
    EquipCmd(ChrTable['金'], ItemTable['省ＥＰ１'], 0x02)
    EquipCmd(ChrTable['金'], ItemTable['封魔之刃'], 0x05)
    EquipCmd(ChrTable['金'], ItemTable['移动３'], 0x06)
    AddCraft(ChrTable['金'], 0x0000)
    OP_BB(0x07, 0x06, 0x0000010A)
    CameraMove(25720, 0, 5470, 0)
    OP_67(0, 10000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    ChrSetStatus(ChrTable['艾丝蒂尔'], 0xFE, 0)
    ChrSetStatus(ChrTable['雪拉扎德'], 0xFE, 0)
    ChrSetStatus(ChrTable['奥利维尔'], 0xFE, 0)
    ChrSetStatus(ChrTable['科洛丝'], 0xFE, 0)
    ChrSetStatus(ChrTable['阿加特'], 0xFE, 0)
    ChrSetStatus(ChrTable['提妲'], 0xFE, 0)
    ChrSetStatus(ChrTable['金'], 0xFE, 0)
    OP_C0(0x15, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)
    FadeIn(0, 0)
    OP_0D()
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※进行队伍的重新编组。\n',
            '　请选择２名固定成员以外的同行者。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_3E3B',
    )

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

    Jump('loc_3E50')

    def _loc_3E3B(): pass

    label('loc_3E3B')

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

    def _loc_3E50(): pass

    label('loc_3E50')

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeOut(0, 0, -1)
    OP_0D()
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x00F7, 0x0080)
    ChrSetFlags(0x00F8, 0x0080)
    ChrSetFlags(0x00F9, 0x0080)
    ChrSetPos(0x0101, 27020, 0, 65640, 180)
    ChrSetPos(0x00F7, 27020, 0, 65640, 180)
    ChrSetPos(0x00F8, 27020, 0, 65640, 180)
    ChrSetPos(0x00F9, 27020, 0, 65640, 180)
    OP_4A(0x0009, 255)
    CameraMove(27420, 0, 61770, 0)
    FadeIn(2000, 0)
    Sleep(1500)

    OP_6F(0x000C, 0)
    OP_70(0x000C, 29)
    OP_73(0x000C)
    CreateThread(0x0101, 0x01, 0x00, func_17_40CD)
    Sleep(800)

    CreateThread(0x00F8, 0x01, 0x00, func_19_4123)
    Sleep(800)

    CreateThread(0x00F9, 0x01, 0x00, func_18_40EE)
    Sleep(800)

    CreateThread(0x00F7, 0x01, 0x00, func_1A_4158)
    WaitForThreadExit(0x00F7, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010240114V#1011F#6P那么……\n',
            '接下来要去王都格兰赛尔了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240115V准备完毕后\n',
            '就马上去飞船坪吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_4019',
    )

    ChrTalk(
        0x0106,
        (
            '#0050240116V#051F#5P既然是军队的直接委托，\n',
            '我们最好尽快过去。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050240117V不过，要是还有委托没完成的话，\n',
            '先解决之后再去也可以。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_40A1')

    def _loc_4019(): pass

    label('loc_4019')

    ChrTalk(
        0x0103,
        (
            '#0030240118V#020F#5P既然是军队的委托，\n',
            '我们还是尽快过去比较好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030240119V不过，要是还有委托没完成的话，\n',
            '先解决掉再去也来得及。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_40A1(): pass

    label('loc_40A1')

    ChrTalk(
        0x0101,
        (
            '#0010240120V#1006F#6P嗯，明白。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4B(0x0009, 255)
    EventEnd(0x00)

    Return()

# id: 0x0017 offset: 0x40CD
@scena.Code('func_17_40CD')
def func_17_40CD():
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, 27020, 0, 60020, 2000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x0018 offset: 0x40EE
@scena.Code('func_18_40EE')
def func_18_40EE():
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, 27050, 0, 63120, 2000, 0x00)
    ChrWalkTo(0x00FE, 27900, 0, 61000, 2000, 0x00)
    ChrSetDirection(0x00FE, 270, 400)

    Return()

# id: 0x0019 offset: 0x4123
@scena.Code('func_19_4123')
def func_19_4123():
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, 27050, 0, 63120, 2000, 0x00)
    ChrWalkTo(0x00FE, 26160, 0, 61000, 2000, 0x00)
    ChrSetDirection(0x00FE, 90, 400)

    Return()

# id: 0x001A offset: 0x4158
@scena.Code('func_1A_4158')
def func_1A_4158():
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, 27020, 0, 63460, 2000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)
    OP_72(0x000C, 0x0800)
    OP_6F(0x000C, 29)
    OP_70(0x000C, 0)
    OP_23(0x0006)
    PlaySE(7, 0x00, 0x64)
    OP_73(0x000C)
    OP_71(0x000C, 0x0800)
    Sleep(500)

    ChrSetDirection(0x00FE, 180, 400)
    ChrWalkTo(0x00FE, 27020, 0, 62040, 2000, 0x00)

    Return()

# id: 0x001B offset: 0x41BC
@scena.Code('func_1B_41BC')
def func_1B_41BC():
    OP_72(0x0010, 0x0020)
    OP_72(0x000E, 0x0020)
    def _loc_41C6(): pass

    label('loc_41C6')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_41F1',
    )

    OP_6F(0x0010, 40)
    OP_70(0x0010, 0)
    OP_6F(0x000E, 0)
    OP_70(0x000E, 40)
    OP_73(0x0010)

    Jump('loc_41C6')

    def _loc_41F1(): pass

    label('loc_41F1')

    Return()

# id: 0x001C offset: 0x41F2
@scena.Code('func_1C_41F2')
def func_1C_41F2():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4357',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4274',
    )

    ChrTalk(
        0x0101,
        (
            '#0010220499V#1000F出城之前还是先去同\n',
            '提妲和博士打个招呼比较好……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010220500V去一趟拉赛尔工房吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_433C')

    def _loc_4274(): pass

    label('loc_4274')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_42DA',
    )

    ChrTalk(
        0x0106,
        (
            '#0050220501V#050F出城之前还是先去通知\n',
            '提妲和老爷爷一声吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050220502V赶快去工房吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_433C')

    def _loc_42DA(): pass

    label('loc_42DA')

    ChrTalk(
        0x0103,
        (
            '#0030220503V#020F出城之前最好先去同\n',
            '提妲还有博士打个招呼，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030220504V这就去博士的工房吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_433C(): pass

    label('loc_433C')

    ChrMoveToRelative(0x0000, 0, 0, -1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_4357(): pass

    label('loc_4357')

    Return()

# id: 0x001D offset: 0x4358
@scena.Code('func_1D_4358')
def func_1D_4358():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_44BD',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_43DA',
    )

    ChrTalk(
        0x0101,
        (
            '#0010220499V#1000F出城之前还是先去同\n',
            '提妲和博士打个招呼比较好……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010220500V去一趟拉赛尔工房吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_44A2')

    def _loc_43DA(): pass

    label('loc_43DA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_4440',
    )

    ChrTalk(
        0x0106,
        (
            '#0050220501V#050F出城之前还是先去通知\n',
            '提妲和老爷爷一声吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050220502V赶快去工房吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_44A2')

    def _loc_4440(): pass

    label('loc_4440')

    ChrTalk(
        0x0103,
        (
            '#0030220503V#020F出城之前最好先去同\n',
            '提妲还有博士打个招呼，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030220504V这就去博士的工房吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_44A2(): pass

    label('loc_44A2')

    ChrMoveToRelative(0x0000, -1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_44BD(): pass

    label('loc_44BD')

    Return()

# id: 0x001E offset: 0x44BE
@scena.Code('func_1E_44BE')
def func_1E_44BE():
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
        (0x00000000, 'loc_4538'),
        (0x00000001, 'loc_453E'),
        (-1, 'loc_4544'),
    )

    def _loc_4538(): pass

    label('loc_4538')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_4544')

    def _loc_453E(): pass

    label('loc_453E')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_4544')

    def _loc_4544(): pass

    label('loc_4544')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_4552',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    Jump('loc_4556')

    def _loc_4552(): pass

    label('loc_4552')

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    def _loc_4556(): pass

    label('loc_4556')

    Return()

# id: 0x001F offset: 0x4557
@scena.Code('func_1F_4557')
def func_1F_4557():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 0, 0x1408)),
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 1, 0x1409)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4815',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4737',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_45CC',
    )

    ChrTalk(
        0x0101,
        (
            '#0010220511V#1000F提妲和博士\n',
            '应该在拉赛尔工房里，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010220512V赶快过去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4734')

    def _loc_45CC(): pass

    label('loc_45CC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_4680',
    )

    ChrTalk(
        0x0101,
        (
            '#0010220513V#1011F……从这里上去就是中央工房了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x0000, 400)

    ChrTalk(
        0x0103,
        (
            '#0030220514V#020F先去拉赛尔工房\n',
            '看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0000, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010220515V#1000F嗯，拉赛尔工房应该在城的西南角。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4731')

    def _loc_4680(): pass

    label('loc_4680')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_4731',
    )

    ChrTalk(
        0x0101,
        (
            '#0010220513V#1011F……从这里上去就是中央工房了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0106, 0x0000, 400)

    ChrTalk(
        0x0106,
        (
            '#0050220517V#051F先去拉赛尔工房\n',
            '看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0000, 0x0106, 400)

    ChrTalk(
        0x0101,
        (
            '#0010220515V#1000F嗯，拉赛尔工房应该在城的西南角。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4731(): pass

    label('loc_4731')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    def _loc_4734(): pass

    label('loc_4734')

    Jump('loc_47FA')

    def _loc_4737(): pass

    label('loc_4737')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_479C',
    )

    ChrTurnDirection(0x0103, 0x0000, 400)

    ChrTalk(
        0x0103,
        (
            '#0030220519V#020F这边是中央工房的方向哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030220520V先去拉赛尔工房\n',
            '看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_47FA')

    def _loc_479C(): pass

    label('loc_479C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_47FA',
    )

    ChrTurnDirection(0x0106, 0x0000, 400)

    ChrTalk(
        0x0106,
        (
            '#0050220521V#050F那边就是中央工房了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050220522V先去拉赛尔工房\n',
            '看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_47FA(): pass

    label('loc_47FA')

    ChrMoveToRelative(0x0000, 1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_4815(): pass

    label('loc_4815')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 1, 0x1409)),
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_496A',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4883',
    )

    ChrTalk(
        0x0101,
        (
            '#0010220511V#1000F提妲和博士\n',
            '应该在拉赛尔工房里，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010220512V赶快过去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_494F')

    def _loc_4883(): pass

    label('loc_4883')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_48E5',
    )

    ChrTalk(
        0x0103,
        (
            '#0030220525V#020F提妲和博士应该在\n',
            '拉赛尔工房里，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030220526V赶快过去打个招呼吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_494F')

    def _loc_48E5(): pass

    label('loc_48E5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_494F',
    )

    ChrTurnDirection(0x0106, 0x0000, 400)

    ChrTalk(
        0x0106,
        (
            '#0050220527V#050F提妲和老爷爷现在应该在\n',
            '拉赛尔工房，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050220528V赶快过去打个招呼吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_494F(): pass

    label('loc_494F')

    ChrMoveToRelative(0x0000, 1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_496A(): pass

    label('loc_496A')

    Return()

# id: 0x0020 offset: 0x496B
@scena.Code('func_20_496B')
def func_20_496B():
    OP_13(0x007D)

    Return()

# id: 0x0021 offset: 0x496F
@scena.Code('func_21_496F')
def func_21_496F():
    OP_13(0x007F)

    Return()

# id: 0x0022 offset: 0x4973
@scena.Code('func_22_4973')
def func_22_4973():
    OP_13(0x0082)

    Return()

# id: 0x0023 offset: 0x4977
@scena.Code('func_23_4977')
def func_23_4977():
    OP_13(0x007C)

    Return()

# id: 0x0024 offset: 0x497B
@scena.Code('func_24_497B')
def func_24_497B():
    OP_13(0x007A)

    Return()

# id: 0x0025 offset: 0x497F
@scena.Code('func_25_497F')
def func_25_497F():
    OP_13(0x007B)

    Return()

# id: 0x0026 offset: 0x4983
@scena.Code('func_26_4983')
def func_26_4983():
    OP_13(0x0080)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
