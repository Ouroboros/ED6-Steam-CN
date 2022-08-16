import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import R3402_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R3402   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'R3402.x'
    header.mapIndex       = 1
    header.bgm            = 30
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
        ('ED6_DT09/CH10130._CH', 'ED6_DT09/CH10130P._CP'),
        ('ED6_DT09/CH10131._CH', 'ED6_DT09/CH10131P._CP'),
        ('ED6_DT09/CH10750._CH', 'ED6_DT09/CH10750P._CP'),
        ('ED6_DT09/CH10751._CH', 'ED6_DT09/CH10751P._CP'),
        ('ED6_DT09/CH10760._CH', 'ED6_DT09/CH10760P._CP'),
        ('ED6_DT09/CH10761._CH', 'ED6_DT09/CH10761P._CP'),
        ('ED6_DT09/CH10770._CH', 'ED6_DT09/CH10770P._CP'),
        ('ED6_DT09/CH10771._CH', 'ED6_DT09/CH10771P._CP'),
        ('ED6_DT29/CH12410._CH', 'ED6_DT29/CH12410P._CP'),
        ('ED6_DT29/CH12411._CH', 'ED6_DT29/CH12411P._CP'),
        ('ED6_DT29/CH12930._CH', 'ED6_DT29/CH12930P._CP'),
        ('ED6_DT29/CH12931._CH', 'ED6_DT29/CH12931P._CP'),
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
    ]

# id: 0x10001 offset: 0x112
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '',
            x                   = 499140,
            z                   = 1000,
            y                   = -114740,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 411170,
            z                   = 20,
            y                   = -60950,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 416300,
            z                   = -20,
            y                   = -61210,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '艾尔·雷登关所方向',
            x                   = 320150,
            z                   = 0,
            y                   = -37050,
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
            name                = '蔡斯方向',
            x                   = 574100,
            z                   = 0,
            y                   = -54930,
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
            name                = '卡鲁迪亚钟乳洞方向',
            x                   = 400800,
            z                   = -30,
            y                   = 22800,
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

# id: 0x10002 offset: 0x1D2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '',
            x           = 367410,
            z           = 10,
            y           = -42400,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01D0,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 389970,
            z           = 10,
            y           = -68740,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01CD,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 425100,
            z           = 0,
            y           = -71190,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01CE,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 467260,
            z           = 0,
            y           = -70580,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01CF,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 497850,
            z           = -20,
            y           = -51510,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01CD,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 506530,
            z           = 0,
            y           = -62560,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01CE,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 526430,
            z           = 30,
            y           = -100000,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01CE,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 402970,
            z           = -20,
            y           = -38570,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01D0,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 422790,
            z           = -10,
            y           = -33010,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01CF,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 407380,
            z           = -20,
            y           = -4320,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01CE,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 536810,
            z           = -30,
            y           = -63870,
            word_0C     = 0x002D,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01CD,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 515280,
            z           = -10,
            y           = -100440,
            word_0C     = 0x003C,
            word_0E     = 0x000A,
            byte_10     = 0xC1,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01D1,
            word_18     = 0x16FA,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x322
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x322
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 499670,
            triggerZ            = -60,
            triggerY            = -114340,
            triggerRange        = 1000,
            actorX              = 499140,
            actorZ              = -60,
            actorY              = -114740,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 514840,
            triggerZ            = -20,
            triggerY            = -121220,
            triggerRange        = 1000,
            actorX              = 514850,
            actorZ              = -20,
            actorY              = -121830,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 423050,
            triggerZ            = -40,
            triggerY            = -33400,
            triggerRange        = 1000,
            actorX              = 423660,
            actorZ              = -40,
            actorY              = -33400,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 411920,
            triggerZ            = 0,
            triggerY            = -59400,
            triggerRange        = 1200,
            actorX              = 411920,
            actorZ              = 1500,
            actorY              = -58300,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 551940,
            triggerZ            = 0,
            triggerY            = -50340,
            triggerRange        = 1500,
            actorX              = 551940,
            actorZ              = 1500,
            actorY              = -50340,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0009,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x3D6
@scena.Code('Init')
def Init():
    Return()

# id: 0x0001 offset: 0x3D7
@scena.Code('func_01_3D7')
def func_01_3D7():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_457',
    )

    OP_71(0x0000, 0x0004)
    OP_71(0x0001, 0x0004)
    OP_71(0x0002, 0x0004)
    OP_71(0x0003, 0x0004)
    OP_71(0x0004, 0x0004)
    OP_71(0x0005, 0x0004)
    OP_71(0x0006, 0x0004)
    OP_71(0x0007, 0x0004)
    OP_71(0x0008, 0x0004)
    OP_71(0x0009, 0x0004)
    OP_71(0x000A, 0x0004)
    OP_71(0x000B, 0x0004)
    OP_71(0x000C, 0x0004)
    OP_71(0x000D, 0x0004)
    OP_71(0x000E, 0x0004)
    OP_79(0xFF, 0x0002)
    OP_C4(0x00, 0x00000001)
    OP_78(0x00, 0x00, 0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02DF, 2, 0x16FA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_454',
    )

    ExecExpressionWithValue(
        0x0019,
        0x24,
        (
            (Expr.PushLong, 0xD2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrClearFlags(0x0019, 0x0080)

    def _loc_454(): pass

    label('loc_454')

    Jump('loc_457')

    def _loc_457(): pass

    label('loc_457')

    OP_16(0x02, 4000, 320000, -179000, 2293817)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_493',
    )

    OP_71(0x0012, 0x0004)
    OP_72(0x0013, 0x0004)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_490',
    )

    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)

    def _loc_490(): pass

    label('loc_490')

    Jump('loc_49D')

    def _loc_493(): pass

    label('loc_493')

    OP_72(0x0012, 0x0004)
    OP_72(0x0013, 0x0004)
    def _loc_49D(): pass

    label('loc_49D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02A4, 6, 0x1526)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4AF',
    )

    OP_6F(0x000F, 0)

    Jump('loc_4B6')

    def _loc_4AF(): pass

    label('loc_4AF')

    OP_6F(0x000F, 60)

    def _loc_4B6(): pass

    label('loc_4B6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02A5, 0, 0x1528)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4C8',
    )

    OP_6F(0x0010, 0)

    Jump('loc_4CF')

    def _loc_4C8(): pass

    label('loc_4C8')

    OP_6F(0x0010, 60)

    def _loc_4CF(): pass

    label('loc_4CF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02A5, 1, 0x1529)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4E1',
    )

    OP_6F(0x0011, 0)

    Jump('loc_4E8')

    def _loc_4E1(): pass

    label('loc_4E1')

    OP_6F(0x0011, 60)

    def _loc_4E8(): pass

    label('loc_4E8')

    ExecExpressionWithValue(
        0x0014,
        0x24,
        (
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0018,
        0x24,
        (
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0019,
        0x24,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0002 offset: 0x50A
@scena.Code('func_02_50A')
def func_02_50A():
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
        'loc_52F',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_671')

    def _loc_52F(): pass

    label('loc_52F')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_548',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_671')

    def _loc_548(): pass

    label('loc_548')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_561',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_671')

    def _loc_561(): pass

    label('loc_561')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_57A',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_671')

    def _loc_57A(): pass

    label('loc_57A')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_593',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_671')

    def _loc_593(): pass

    label('loc_593')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5AC',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_671')

    def _loc_5AC(): pass

    label('loc_5AC')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5C5',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_671')

    def _loc_5C5(): pass

    label('loc_5C5')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5DE',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_671')

    def _loc_5DE(): pass

    label('loc_5DE')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5F7',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_671')

    def _loc_5F7(): pass

    label('loc_5F7')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_610',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_671')

    def _loc_610(): pass

    label('loc_610')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_629',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_671')

    def _loc_629(): pass

    label('loc_629')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_642',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_671')

    def _loc_642(): pass

    label('loc_642')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_65B',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_671')

    def _loc_65B(): pass

    label('loc_65B')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_671',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_671(): pass

    label('loc_671')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_686',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_671')

    def _loc_686(): pass

    label('loc_686')

    Return()

# id: 0x0003 offset: 0x687
@scena.Code('func_03_687')
def func_03_687():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.Eval, "OP_29(0x0071, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_779',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_6EC',
    )

    ChrTalk(
        0x00FE,
        (
            '不管怎样，那个青年\n',
            '没有受伤就好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '麻烦你们协会\n',
            '好好地训诫他一番吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_776')

    def _loc_6EC(): pass

    label('loc_6EC')

    ChrTalk(
        0x00FE,
        (
            '哦，游击士们。\n',
            '刚才干得真是漂亮啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然想说的实在很多，\n',
            '不过只要那青年没受伤就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '麻烦你们协会\n',
            '好好地训诫他一番吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_776(): pass

    label('loc_776')

    Jump('loc_7C5')

    def _loc_779(): pass

    label('loc_779')

    ChrTalk(
        0x00FE,
        (
            '也许有人\n',
            '已经进去了也说不定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没有向游击士协会\n',
            '进行任何的联络吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_7C5(): pass

    label('loc_7C5')

    TalkEnd(0x00FE)

    Return()

# id: 0x0004 offset: 0x7C9
@scena.Code('func_04_7C9')
def func_04_7C9():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.Eval, "OP_29(0x0071, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_8B7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_838',
    )

    ChrTalk(
        0x00FE,
        (
            '放着工作不做，\n',
            '跑去钟乳洞探险吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然令人感到头痛，\n',
            '但老实说也有点羡慕呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8B4')

    def _loc_838(): pass

    label('loc_838')

    ChrTalk(
        0x00FE,
        (
            '啊，辛苦了。\n',
            '刚才真是多谢你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '放着工作不做，\n',
            '在钟乳洞里四处乱晃……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最近的年轻人\n',
            '真是让人伤脑筋啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_8B4(): pass

    label('loc_8B4')

    Jump('loc_946')

    def _loc_8B7(): pass

    label('loc_8B7')

    ChrTalk(
        0x00FE,
        (
            '我巡逻时看了一下，\n',
            '发现钟乳洞的封锁被解除了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '居然将沙袋搬开，\n',
            '这也太缺乏责任感了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '万一有旅行者误入进去的话，\n',
            '该怎么办才好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_946(): pass

    label('loc_946')

    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0x94A
@scena.Code('func_05_94A')
def func_05_94A():
    UnlockAchievement(0x02, 0x01FA, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02A4, 6, 0x1526)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_AE2',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x000F, 60)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02A4, 7, 0x1527)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A2E',
    )

    ChrSetRGBAMask(0x0008, 255, 255, 255, 0, 0)
    ChrTurnDirection(0x0008, 0x0000, 0)
    ChrMoveToRelativeAsync(0x0008, 0, 1000, 0, 0, 0x00)

    @scena.Lambda('lambda_09A1')
    def lambda_09A1():
        ChrMoveToRelativeAsync(0x00FE, 0, -1000, 0, 600, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_09A1)

    @scena.Lambda('lambda_09BC')
    def lambda_09BC():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 600)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_09BC)

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
    Battle(0x000001D2, 0x00000000, 0x00, 0x0000, 0xFF)
    ChrSetFlags(0x0008, 0x0080)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_A09'),
        (0x00000002, 'loc_A1B'),
        (0x00000001, 'loc_A2B'),
        (-1, 'loc_A2E'),
    )

    def _loc_A09(): pass

    label('loc_A09')

    SetScenaFlags(ScenaFlag(0x02A4, 7, 0x1527))
    OP_6F(0x000F, 60)
    Sleep(500)

    Jump('loc_A2E')

    def _loc_A1B(): pass

    label('loc_A1B')

    OP_6F(0x000F, 0)
    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

    def _loc_A2B(): pass

    label('loc_A2B')

    OP_B4(0x00)

    Return()

    def _loc_A2E(): pass

    label('loc_A2E')

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['幻影戒指'], 1)"),
            Expr.Return,
        ),
        'loc_A7D',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['幻影戒指']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x02A4, 6, 0x1526))

    Jump('loc_ADF')

    def _loc_A7D(): pass

    label('loc_A7D')

    FadeOut(300, 0, 100)

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['幻影戒指']),
            (TxtCtl.SetColor, 0x0),
            '。 \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['幻影戒指']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x000F, 60)
    OP_70(0x000F, 0)

    def _loc_ADF(): pass

    label('loc_ADF')

    Jump('loc_B11')

    def _loc_AE2(): pass

    label('loc_AE2')

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
    def _loc_B11(): pass

    label('loc_B11')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0006 offset: 0xB1F
@scena.Code('func_06_B1F')
def func_06_B1F():
    UnlockAchievement(0x02, 0x01FB, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02A5, 0, 0x1528)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_BFC',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0010, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['青蛙'], 1)"),
            Expr.Return,
        ),
        'loc_B93',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['青蛙']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x02A5, 0, 0x1528))

    Jump('loc_BF9')

    def _loc_B93(): pass

    label('loc_B93')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['青蛙']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['青蛙']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0010, 60)
    OP_70(0x0010, 0)

    def _loc_BF9(): pass

    label('loc_BF9')

    Jump('loc_C2D')

    def _loc_BFC(): pass

    label('loc_BFC')

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
    def _loc_C2D(): pass

    label('loc_C2D')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0007 offset: 0xC3B
@scena.Code('func_07_C3B')
def func_07_C3B():
    UnlockAchievement(0x02, 0x01FC, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02A5, 1, 0x1529)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_D18',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0011, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['绝缘胶带'], 1)"),
            Expr.Return,
        ),
        'loc_CAF',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['绝缘胶带']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x02A5, 1, 0x1529))

    Jump('loc_D15')

    def _loc_CAF(): pass

    label('loc_CAF')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['绝缘胶带']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['绝缘胶带']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0011, 60)
    OP_70(0x0011, 0)

    def _loc_D15(): pass

    label('loc_D15')

    Jump('loc_D49')

    def _loc_D18(): pass

    label('loc_D18')

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
    def _loc_D49(): pass

    label('loc_D49')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0008 offset: 0xD57
@scena.Code('func_08_D57')
def func_08_D57():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            (Expr.Eval, "OP_40(0x0150, 0x02)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_D9B',
    )

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '漆黑一团，看不清楚。',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_DDC')

    def _loc_D9B(): pass

    label('loc_D9B')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '北　钟乳洞\n',
            '※魔兽游荡地区，现封锁中\n',
            '　　　　　　　　　王国军',
            TxtCtl.Enter,
        ),
    )

    def _loc_DDC(): pass

    label('loc_DDC')

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0009 offset: 0xDF5
@scena.Code('func_09_DF5')
def func_09_DF5():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            (Expr.Eval, "OP_40(0x0150, 0x02)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_E39',
    )

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '漆黑一团，看不清楚。',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_E65')

    def _loc_E39(): pass

    label('loc_E39')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '东　蔡斯市\n',
            '西　艾尔．雷登　４４８塞尔矩',
            TxtCtl.Enter,
        ),
    )

    def _loc_E65(): pass

    label('loc_E65')

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
