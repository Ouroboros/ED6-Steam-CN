import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T4105_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4105   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4105.x'
    header.mapIndex       = 1
    header.bgm            = 14
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
        ('ED6_DT07/CH01690._CH', 'ED6_DT07/CH01690P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH01540._CH', 'ED6_DT07/CH01540P._CP'),
        ('ED6_DT07/CH01450._CH', 'ED6_DT07/CH01450P._CP'),
        ('ED6_DT07/CH01550._CH', 'ED6_DT07/CH01550P._CP'),
        ('ED6_DT07/CH01450._CH', 'ED6_DT07/CH01450P._CP'),
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
        ('ED6_DT07/CH01610._CH', 'ED6_DT07/CH01610P._CP'),
        ('ED6_DT07/CH01500._CH', 'ED6_DT07/CH01500P._CP'),
        ('ED6_DT07/CH01300._CH', 'ED6_DT07/CH01300P._CP'),
    ]

# id: 0x10001 offset: 0xFA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '索菲娜',
            x                   = 56030,
            z                   = 250,
            y                   = 133380,
            direction           = 258,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '鲁特尔',
            x                   = 77500,
            z                   = 1500,
            y                   = 142010,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '菲丝',
            x                   = 58770,
            z                   = 250,
            y                   = 137000,
            direction           = 281,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '卡鲁尼洛',
            x                   = 93960,
            z                   = 1500,
            y                   = 144440,
            direction           = 293,
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
            name                = '蒂法露',
            x                   = 84910,
            z                   = 1500,
            y                   = 141950,
            direction           = 187,
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
            name                = '修理员佩顿',
            x                   = 67710,
            z                   = -10000,
            y                   = 159300,
            direction           = 84,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 73000,
            z                   = -9800,
            y                   = 158970,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 63050,
            z                   = -3000,
            y                   = 160490,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 63040,
            z                   = -3000,
            y                   = 159620,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 73620,
            z                   = 1500,
            y                   = 143000,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            name                = '特务兵',
            x                   = 63050,
            z                   = -3000,
            y                   = 160490,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            name                = '特务兵',
            x                   = 63040,
            z                   = -3000,
            y                   = 159620,
            direction           = 270,
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
            name                = '特务兵',
            x                   = 73620,
            z                   = 1500,
            y                   = 143000,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0011,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 72120,
            z                   = -9800,
            y                   = 158930,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '菲',
            x                   = 72480,
            z                   = -10000,
            y                   = 169900,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0012,
        ),
        ScenaNpcData(
            name                = '鲁迪',
            x                   = 72480,
            z                   = -10000,
            y                   = 170720,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            name                = '士兵布拉姆',
            x                   = 72480,
            z                   = -10000,
            y                   = 170720,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0014,
        ),
        ScenaNpcData(
            name                = '王都格兰赛尔·东街区',
            x                   = 51050,
            z                   = 0,
            y                   = 83440,
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

# id: 0x10002 offset: 0x33A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x33A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x33A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 56800,
            triggerZ            = 250,
            triggerY            = 136940,
            triggerRange        = 800,
            actorX              = 58770,
            actorZ              = 1750,
            actorY              = 137000,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 53710,
            triggerZ            = 250,
            triggerY            = 137720,
            triggerRange        = 800,
            actorX              = 53710,
            actorZ              = 2450,
            actorY              = 137720,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0015,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 71160,
            triggerZ            = -10000,
            triggerY            = 151550,
            triggerRange        = 800,
            actorX              = 71160,
            actorZ              = -8500,
            actorY              = 151550,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0016,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x3A6
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_3E8',
    )

    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x000D, 73000, -9800, 158970, 270)
    ChrSetFlags(0x000E, 0x0080)
    ChrClearFlags(0x0016, 0x0080)

    If(
        (
            (Expr.Eval, "OP_29(0x0031, 0x01, 0x0020)"),
            Expr.Return,
        ),
        'loc_3E0',
    )

    ChrClearFlags(0x0018, 0x0080)

    Jump('loc_3E5')

    def _loc_3E0(): pass

    label('loc_3E0')

    ChrClearFlags(0x0017, 0x0080)

    def _loc_3E5(): pass

    label('loc_3E5')

    Jump('loc_562')

    def _loc_3E8(): pass

    label('loc_3E8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_432',
    )

    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x000B, 68580, 250, 147780, 45)
    ChrSetPos(0x000C, 66400, 0, 145250, 135)
    ChrSetFlags(0x000D, 0x0080)
    ChrClearFlags(0x0012, 0x0080)
    ChrClearFlags(0x0013, 0x0080)
    ChrClearFlags(0x0014, 0x0080)
    ChrClearFlags(0x0015, 0x0080)

    Jump('loc_562')

    def _loc_432(): pass

    label('loc_432')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_477',
    )

    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x000B, 68580, 250, 147780, 45)
    ChrSetPos(0x000C, 66400, 0, 145250, 135)
    ChrSetFlags(0x000D, 0x0080)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0011, 0x0080)

    Jump('loc_562')

    def _loc_477(): pass

    label('loc_477')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_4A3',
    )

    ChrSetPos(0x000C, 66860, 250, 147300, 90)
    ChrSetPos(0x000D, 68610, 250, 147270, 270)

    Jump('loc_562')

    def _loc_4A3(): pass

    label('loc_4A3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_4BE',
    )

    ChrSetPos(0x000D, 68470, 250, 147030, 90)

    Jump('loc_562')

    def _loc_4BE(): pass

    label('loc_4BE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_4EA',
    )

    ChrSetPos(0x000C, 77380, 1500, 144440, 270)
    ChrSetPos(0x000D, 76010, 1500, 144460, 90)

    Jump('loc_562')

    def _loc_4EA(): pass

    label('loc_4EA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_505',
    )

    ChrSetPos(0x000B, 83030, 1700, 141250, 180)

    Jump('loc_562')

    def _loc_505(): pass

    label('loc_505')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_520',
    )

    ChrSetPos(0x000B, 83030, 1700, 141250, 180)

    Jump('loc_562')

    def _loc_520(): pass

    label('loc_520')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_540',
    )

    ChrSetPos(0x000B, 83030, 1700, 141250, 180)
    ChrClearFlags(0x0009, 0x0080)

    Jump('loc_562')

    def _loc_540(): pass

    label('loc_540')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_55B',
    )

    ChrSetPos(0x000B, 83030, 1700, 141250, 180)

    Jump('loc_562')

    def _loc_55B(): pass

    label('loc_55B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_562',
    )

    def _loc_562(): pass

    label('loc_562')

    Return()

# id: 0x0001 offset: 0x563
@scena.Code('func_01_563')
def func_01_563():
    OP_16(0x02, 4000, -43000, 29000, 196703)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 1, 0x631)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 3, 0x623)),
            Expr.Or,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 3, 0x61B)),
            Expr.Or,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 6, 0x616)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_605',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5B5',
    )

    OP_B1('t4105_y0')

    Jump('loc_602')

    def _loc_5B5(): pass

    label('loc_5B5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5CE',
    )

    OP_B1('t4105_y1')

    Jump('loc_602')

    def _loc_5CE(): pass

    label('loc_5CE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5E7',
    )

    OP_B1('t4105_y2')

    Jump('loc_602')

    def _loc_5E7(): pass

    label('loc_5E7')

    OP_B1('t4105_y0')
    OP_71(0x000A, 0x0004)
    OP_71(0x000B, 0x0004)
    OP_6F(0x0005, 100)

    def _loc_602(): pass

    label('loc_602')

    Jump('loc_667')

    def _loc_605(): pass

    label('loc_605')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_61D',
    )

    OP_B1('t4105_0')

    Jump('loc_667')

    def _loc_61D(): pass

    label('loc_61D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_635',
    )

    OP_B1('t4105_1')

    Jump('loc_667')

    def _loc_635(): pass

    label('loc_635')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_64D',
    )

    OP_B1('t4105_2')

    Jump('loc_667')

    def _loc_64D(): pass

    label('loc_64D')

    OP_B1('t4105_0')
    OP_71(0x000A, 0x0004)
    OP_71(0x000B, 0x0004)
    OP_6F(0x0005, 100)

    def _loc_667(): pass

    label('loc_667')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 2, 0x66A)),
            Expr.Return,
        ),
        'loc_677',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x4B),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_677(): pass

    label('loc_677')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 3, 0x62B)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 6, 0x62E)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_688',
    )

    OP_72(0x0006, 0x0010)

    def _loc_688(): pass

    label('loc_688')

    Return()

# id: 0x0002 offset: 0x689
@scena.Code('func_02_689')
def func_02_689():
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
        'loc_6AE',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_7F0')

    def _loc_6AE(): pass

    label('loc_6AE')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6C7',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_7F0')

    def _loc_6C7(): pass

    label('loc_6C7')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6E0',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_7F0')

    def _loc_6E0(): pass

    label('loc_6E0')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6F9',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_7F0')

    def _loc_6F9(): pass

    label('loc_6F9')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_712',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_7F0')

    def _loc_712(): pass

    label('loc_712')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_72B',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_7F0')

    def _loc_72B(): pass

    label('loc_72B')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_744',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_7F0')

    def _loc_744(): pass

    label('loc_744')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_75D',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_7F0')

    def _loc_75D(): pass

    label('loc_75D')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_776',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_7F0')

    def _loc_776(): pass

    label('loc_776')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_78F',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_7F0')

    def _loc_78F(): pass

    label('loc_78F')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7A8',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_7F0')

    def _loc_7A8(): pass

    label('loc_7A8')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7C1',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_7F0')

    def _loc_7C1(): pass

    label('loc_7C1')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7DA',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_7F0')

    def _loc_7DA(): pass

    label('loc_7DA')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7F0',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_7F0(): pass

    label('loc_7F0')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_805',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_7F0')

    def _loc_805(): pass

    label('loc_805')

    Return()

# id: 0x0003 offset: 0x806
@scena.Code('func_03_806')
def func_03_806():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_829',
    )

    OP_8D(0x00FE, 52840, 136880, 55890, 126400, 3000)

    Jump('func_03_806')

    def _loc_829(): pass

    label('loc_829')

    Return()

# id: 0x0004 offset: 0x82A
@scena.Code('func_04_82A')
def func_04_82A():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_891',
    )

    ChrTalk(
        0x00FE,
        (
            '定期船总算可以\n',
            '正常地航行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '作为维修主任的我\n',
            '从现在开始也要更加努力才行啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C86')

    def _loc_891(): pass

    label('loc_891')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_8F1',
    )

    ChrTalk(
        0x00FE,
        (
            '代替王国军士兵的\n',
            '黑衣士兵来站岗了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '与之前的士兵相比\n',
            '有一种恐怖的威慑力……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C86')

    def _loc_8F1(): pass

    label('loc_8F1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_94E',
    )

    ChrTalk(
        0x00FE,
        (
            '唉，\n',
            '军方把我的工作地点封锁了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在定期船\n',
            '也不能运行了，\n',
            '究竟会怎样呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C86')

    def _loc_94E(): pass

    label('loc_94E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_99F',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，今天总算是\n',
            '按原定计划送走定期船了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是总能这样就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C86')

    def _loc_99F(): pass

    label('loc_99F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_9D4',
    )

    ChrTalk(
        0x00FE,
        (
            '呼～\n',
            '预定今天抵达的定期船终于要来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C86')

    def _loc_9D4(): pass

    label('loc_9D4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_A34',
    )

    ChrTalk(
        0x00FE,
        (
            '『埃尔赛尤号』是\n',
            '技术部全体人员憧憬的目标。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '什么时候我也能\n',
            '在那上面工作呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C86')

    def _loc_A34(): pass

    label('loc_A34')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_AA7',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯，这样一来，\n',
            '修理就应该全部完成了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为不知道飞船\n',
            '什么时候才会进港，\n',
            '所以比平时辛苦许多呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C86')

    def _loc_AA7(): pass

    label('loc_AA7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_B1B',
    )

    ChrTalk(
        0x00FE,
        (
            '原定的『赛希莉亚号』还没抵达，\n',
            '军队的警备飞艇却突然进港了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '『赛希莉亚号』\n',
            '在今天内能到达吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C86')

    def _loc_B1B(): pass

    label('loc_B1B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_B5B',
    )

    ChrTalk(
        0x00FE,
        (
            '怎么回事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '定期船一点都没有要到达的迹象。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C86')

    def _loc_B5B(): pass

    label('loc_B5B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_BAA',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯，\n',
            '机体部分的检查完成了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔，接下来要检查的项目是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C86')

    def _loc_BAA(): pass

    label('loc_BAA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_C86',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_C15',
    )

    ChrTalk(
        0x00FE,
        (
            '自从我当上维修主任以来，\n',
            '发生了许多事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '像是空贼事件，\n',
            '还有这次的恐怖事件……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C86')

    def _loc_C15(): pass

    label('loc_C15')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '自从我当上维修主任以来，\n',
            '发生了许多事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '像是空贼事件，\n',
            '还有这次的恐怖事件……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是不吉利啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C86(): pass

    label('loc_C86')

    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0xC8A
@scena.Code('func_05_C8A')
def func_05_C8A():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_CED',
    )

    ChrTalk(
        0x00FE,
        (
            '这下终于\n',
            '可以回到工作岗位了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为了能取回客人们的信赖，\n',
            '一定要加油干才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1206')

    def _loc_CED(): pass

    label('loc_CED')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_D34',
    )

    ChrTalk(
        0x00FE,
        (
            '军队的那些家伙\n',
            '该知道适可而止了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '早点滚出这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1206')

    def _loc_D34(): pass

    label('loc_D34')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_DF3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_D7A',
    )

    ChrTalk(
        0x00FE,
        (
            '哎…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说起来，\n',
            '佩顿师傅到哪里去了呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DF0')

    def _loc_D7A(): pass

    label('loc_D7A')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))
    OP_62(0x000C, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '啊～气死人了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '都这么久了，\n',
            '还没抓到那些恐怖分子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '什么嘛，我受够了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_DF0(): pass

    label('loc_DF0')

    Jump('loc_1206')

    def _loc_DF3(): pass

    label('loc_DF3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_E52',
    )

    ChrTalk(
        0x00FE,
        (
            '不愧是蔡斯的\n',
            '中央工房那里\n',
            '派来的佩顿师傅。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是能做我们的\n',
            '技术顾问就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1206')

    def _loc_E52(): pass

    label('loc_E52')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_E9C',
    )

    ChrTalk(
        0x00FE,
        (
            '好了，『赛希莉亚号』就要抵达了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要预先做好准备才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1206')

    def _loc_E9C(): pass

    label('loc_E9C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_FA2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_EFD',
    )

    ChrTalk(
        0x00FE,
        (
            '军队的那些家伙\n',
            '能不能赶快离开啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '又不能给我们工作帮忙，\n',
            '就会来打扰！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F9F')

    def _loc_EFD(): pass

    label('loc_EFD')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '我向佩顿师傅询问过很多\n',
            '有关『埃尔赛尤号』的情况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然还未完成，\n',
            '但却是一艘很棒的飞艇呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果没有那些军人的话，\n',
            '我就能到飞艇里面去参观一下了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F9F(): pass

    label('loc_F9F')

    Jump('loc_1206')

    def _loc_FA2(): pass

    label('loc_FA2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_1008',
    )

    ChrTalk(
        0x00FE,
        (
            '就算定期船再怎么延误，\n',
            '我们要做的也只有一件事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那就是全力保证\n',
            '飞艇和乘客的安全。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1206')

    def _loc_1008(): pass

    label('loc_1008')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_110D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_1079',
    )

    ChrTalk(
        0x00FE,
        (
            '那个女性军官的态度，\n',
            '也太蛮不讲理了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对本来就过于软弱的主任，\n',
            '她更是变本加厉的蛮横。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_110A')

    def _loc_1079(): pass

    label('loc_1079')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '那个女性军官的态度，\n',
            '好像自以为有多了不起似的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么蛮不讲理，我也只有忍了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但对本来就过于软弱的主任，\n',
            '她更是变本加厉的蛮横。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_110A(): pass

    label('loc_110A')

    Jump('loc_1206')

    def _loc_110D(): pass

    label('loc_110D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_1148',
    )

    ChrTalk(
        0x00FE,
        (
            '还没来啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不会又卷入\n',
            '什么事件了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1206')

    def _loc_1148(): pass

    label('loc_1148')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_119F',
    )

    ChrTalk(
        0x00FE,
        (
            '发动机部分没有异常。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '导力压调整完毕，\n',
            '分配给我的部分已经全部完成。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1206')

    def _loc_119F(): pass

    label('loc_119F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_1206',
    )

    ChrTalk(
        0x00FE,
        (
            '说实话，新来的维修主任的\n',
            '技术和态度都不太可靠。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '希望他能作为一个男人\n',
            '再好好地加把劲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1206(): pass

    label('loc_1206')

    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0x120A
@scena.Code('func_06_120A')
def func_06_120A():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_134D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_128F',
    )

    ChrTalk(
        0x00FE,
        (
            '终于看到让『埃尔赛尤号』\n',
            '再次试飞的希望了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '拉赛尔博士现在也没事了，\n',
            '这个项目也就可以\n',
            '向前跨一大步了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_134A')

    def _loc_128F(): pass

    label('loc_128F')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '终于看到让『埃尔赛尤号』\n',
            '再次试飞的希望了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '中央工房的新型引擎开发\n',
            '也得加快速度才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '拉赛尔博士现在也没事了，\n',
            '这个项目也就可以\n',
            '向前跨一大步了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好～的，加油干～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_134A(): pass

    label('loc_134A')

    Jump('loc_17F0')

    def _loc_134D(): pass

    label('loc_134D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_1357',
    )

    Jump('loc_17F0')

    def _loc_1357(): pass

    label('loc_1357')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_1361',
    )

    Jump('loc_17F0')

    def _loc_1361(): pass

    label('loc_1361')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_138C',
    )

    ChrTalk(
        0x00FE,
        (
            '哎呀，\n',
            '年轻人就是有热情呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17F0')

    def _loc_138C(): pass

    label('loc_138C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_151C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_142F',
    )

    ChrTalk(
        0x00FE,
        (
            '（我听中央工房的同事说，\n',
            '　拉赛尔博士好像被\n',
            '　不知道什么人绑架走了。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '（不过，我觉得\n',
            '　博士一定会平安无事逃走，\n',
            '　然后回到工房来的。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1519')

    def _loc_142F(): pass

    label('loc_142F')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '我在这里小声告诉你哦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '（我听中央工房的同事说，\n',
            '　拉赛尔博士好像被\n',
            '　不知道什么人绑架走了。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '（而且听说提妲也在一起，\n',
            '　我真是有些担心呢……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '（不过，我觉得\n',
            '　博士一定会平安无事逃走，\n',
            '　然后回到工房来的。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1519(): pass

    label('loc_1519')

    Jump('loc_17F0')

    def _loc_151C(): pass

    label('loc_151C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_157A',
    )

    ChrTalk(
        0x00FE,
        (
            '憋了一肚子的火\n',
            '就要爆发了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好想快点继续进行\n',
            '『埃尔赛尤号』的测试工作啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17F0')

    def _loc_157A(): pass

    label('loc_157A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_15C2',
    )

    ChrTalk(
        0x00FE,
        (
            '唔～反正我很无聊，\n',
            '『林德号』的检修工作\n',
            '我也去帮帮忙吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17F0')

    def _loc_15C2(): pass

    label('loc_15C2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_162E',
    )

    ChrTalk(
        0x00FE,
        (
            '那艘警备飞艇是最近\n',
            '才归雷斯顿要塞所有的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在这个时候来到这里，\n',
            '难道发生了什么事件吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17F0')

    def _loc_162E(): pass

    label('loc_162E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_169B',
    )

    ChrTalk(
        0x00FE,
        (
            '『埃尔赛尤号』\n',
            '现在还处于未完工状态。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '本来很快就要\n',
            '进行下一轮测试的，\n',
            '但现在这种状况……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17F0')

    def _loc_169B(): pass

    label('loc_169B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_1703',
    )

    ChrTalk(
        0x00FE,
        (
            '说起来……\n',
            '我有些担心尤莉亚中尉他们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说是由她发动了政变什么的，\n',
            '肯定是哪里搞错了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17F0')

    def _loc_1703(): pass

    label('loc_1703')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_17F0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_176C',
    )

    ChrTalk(
        0x00FE,
        (
            '『埃尔赛尤号』\n',
            '是王家所拥有的高速飞船。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不管怎么说，\n',
            '也不应该由王国军来保管。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17F0')

    def _loc_176C(): pass

    label('loc_176C')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '『埃尔赛尤号』\n',
            '是王家所拥有的高速飞船。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不管怎么说，\n',
            '也不应该由王国军来保管。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这真的是经过了\n',
            '女王陛下许可的吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_17F0(): pass

    label('loc_17F0')

    TalkEnd(0x00FE)

    Return()

# id: 0x0007 offset: 0x17F4
@scena.Code('func_07_17F4')
def func_07_17F4():
    Call(0, 0x0008)

    Return()

# id: 0x0008 offset: 0x17F9
@scena.Code('func_08_17F9')
def func_08_17F9():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_1850',
    )

    ChrTalk(
        0x000A,
        (
            '在不知不觉中，\n',
            '我们就被卷入了\n',
            '这次政变活动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '真是太令人惊讶了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D69')

    def _loc_1850(): pass

    label('loc_1850')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_1883',
    )

    ChrTalk(
        0x000A,
        (
            '唉，究竟要到何时\n',
            '才能正常开工啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D69')

    def _loc_1883(): pass

    label('loc_1883')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_1956',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_18E9',
    )

    ChrTalk(
        0x000A,
        (
            '因为今天王国军要\n',
            '搜捕恐怖分子，\n',
            '航运全部中止了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '我可以为您\n',
            '办理退票手续。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1953')

    def _loc_18E9(): pass

    label('loc_18E9')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x000A,
        (
            '非常抱歉……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '因为今天王国军要\n',
            '搜捕恐怖分子，\n',
            '航运全部中止了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '我可以为您\n',
            '办理退票手续。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1953(): pass

    label('loc_1953')

    Jump('loc_1D69')

    def _loc_1956(): pass

    label('loc_1956')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_199A',
    )

    ChrTalk(
        0x000A,
        (
            '呼，\n',
            '明天定期船要是也能这样\n',
            '按原定计划起航就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D69')

    def _loc_199A(): pass

    label('loc_199A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_19F7',
    )

    ChrTalk(
        0x000A,
        (
            '每次定期船延时到达，\n',
            '我都想到柏斯那件空贼事件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '这样的惯性思维真不好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D69')

    def _loc_19F7(): pass

    label('loc_19F7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_1A5E',
    )

    ChrTalk(
        0x000A,
        (
            '最近一段时间\n',
            '王国军频繁地\n',
            '在这附近巡逻。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '这段时间发生了不少事，\n',
            '让人有些不安呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D69')

    def _loc_1A5E(): pass

    label('loc_1A5E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_1AC8',
    )

    ChrTalk(
        0x000A,
        (
            '现在，停在港里的定期船\n',
            '是去往洛连特方向的『林德号』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '要乘坐的客人\n',
            '请前往普通登机口。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D69')

    def _loc_1AC8(): pass

    label('loc_1AC8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_1B38',
    )

    ChrTalk(
        0x000A,
        (
            '因为王国军飞艇要出入港的关系，\n',
            '今天的定期船航班\n',
            '出发和到达时间又要推迟了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '真叫人难办啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D69')

    def _loc_1B38(): pass

    label('loc_1B38')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_1C17',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1B9F',
    )

    ChrTalk(
        0x000A,
        (
            '奇怪了啊。\n',
            '『林德号』到现在都还没有抵达。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '今天明明可以\n',
            '按时到达这里的啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C14')

    def _loc_1B9F(): pass

    label('loc_1B9F')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x000A,
        (
            '奇怪了啊。\n',
            '『林德号』到现在都还没有抵达。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '今天明明可以\n',
            '按时到达这里的啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '我该怎么向旅客说明呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C14(): pass

    label('loc_1C14')

    Jump('loc_1D69')

    def _loc_1C17(): pass

    label('loc_1C17')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_1C54',
    )

    ChrTalk(
        0x000A,
        (
            '预定中午到达的『赛希莉亚号』\n',
            '现在终于抵达了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D69')

    def _loc_1C54(): pass

    label('loc_1C54')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_1D69',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1CD5',
    )

    ChrTalk(
        0x000A,
        (
            '因为王国军要盘查的缘故，\n',
            '所以出发和到达的时间都大幅度推迟了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '飞船一旦到达了，\n',
            '我就会通知你们搭乘的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D69')

    def _loc_1CD5(): pass

    label('loc_1CD5')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x000A,
        (
            '让你们久等了，\n',
            '实在很抱歉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '因为王国军要盘查的缘故，\n',
            '所以出发和到达的时间都大幅度推迟了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '飞船一旦到达了，\n',
            '我就会通知你们搭乘的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1D69(): pass

    label('loc_1D69')

    TalkEnd(0x000A)

    Return()

# id: 0x0009 offset: 0x1D6D
@scena.Code('func_09_1D6D')
def func_09_1D6D():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_1D7A',
    )

    Jump('loc_1ED6')

    def _loc_1D7A(): pass

    label('loc_1D7A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_1D84',
    )

    Jump('loc_1ED6')

    def _loc_1D84(): pass

    label('loc_1D84')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_1D8E',
    )

    Jump('loc_1ED6')

    def _loc_1D8E(): pass

    label('loc_1D8E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_1D98',
    )

    Jump('loc_1ED6')

    def _loc_1D98(): pass

    label('loc_1D98')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_1DA2',
    )

    Jump('loc_1ED6')

    def _loc_1DA2(): pass

    label('loc_1DA2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_1DAC',
    )

    Jump('loc_1ED6')

    def _loc_1DAC(): pass

    label('loc_1DAC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_1DB6',
    )

    Jump('loc_1ED6')

    def _loc_1DB6(): pass

    label('loc_1DB6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_1DC0',
    )

    Jump('loc_1ED6')

    def _loc_1DC0(): pass

    label('loc_1DC0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_1EC5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_1E29',
    )

    ChrTalk(
        0x00FE,
        (
            '我本来是来公社\n',
            '推销新型飞船的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过这里异常的忙乱，\n',
            '看来我来得不是时候……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1EC2')

    def _loc_1E29(): pass

    label('loc_1E29')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '我本来是来公社\n',
            '推销新型飞船的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过这里异常的忙乱，\n',
            '看来我来得不是时候……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且我有些担心\n',
            '新型引擎的研发计划，\n',
            '还是先回蔡斯一趟吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1EC2(): pass

    label('loc_1EC2')

    Jump('loc_1ED6')

    def _loc_1EC5(): pass

    label('loc_1EC5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_1ECF',
    )

    Jump('loc_1ED6')

    def _loc_1ECF(): pass

    label('loc_1ECF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_1ED6',
    )

    def _loc_1ED6(): pass

    label('loc_1ED6')

    TalkEnd(0x00FE)

    Return()

# id: 0x000A offset: 0x1EDA
@scena.Code('func_0A_1EDA')
def func_0A_1EDA():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_1F2F',
    )

    ChrTalk(
        0x00FE,
        (
            '定期船现在终于\n',
            '可以正常航行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样一来我就\n',
            '可以回柏斯去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_200B')

    def _loc_1F2F(): pass

    label('loc_1F2F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_1F72',
    )

    ChrTalk(
        0x00FE,
        (
            '既然不能乘坐定期船，\n',
            '至少也得和家里取得联络才行……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_200B')

    def _loc_1F72(): pass

    label('loc_1F72')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_1FBE',
    )

    ChrTalk(
        0x00FE,
        (
            '空港好像被\n',
            '王国军给封锁了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真糟糕啊。\n',
            '怎么会这样呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_200B')

    def _loc_1FBE(): pass

    label('loc_1FBE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_1FC8',
    )

    Jump('loc_200B')

    def _loc_1FC8(): pass

    label('loc_1FC8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_1FD2',
    )

    Jump('loc_200B')

    def _loc_1FD2(): pass

    label('loc_1FD2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_1FDC',
    )

    Jump('loc_200B')

    def _loc_1FDC(): pass

    label('loc_1FDC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_1FE6',
    )

    Jump('loc_200B')

    def _loc_1FE6(): pass

    label('loc_1FE6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_1FF0',
    )

    Jump('loc_200B')

    def _loc_1FF0(): pass

    label('loc_1FF0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_1FFA',
    )

    Jump('loc_200B')

    def _loc_1FFA(): pass

    label('loc_1FFA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_2004',
    )

    Jump('loc_200B')

    def _loc_2004(): pass

    label('loc_2004')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_200B',
    )

    def _loc_200B(): pass

    label('loc_200B')

    TalkEnd(0x00FE)

    Return()

# id: 0x000B offset: 0x200F
@scena.Code('func_0B_200F')
def func_0B_200F():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_201C',
    )

    Jump('loc_233F')

    def _loc_201C(): pass

    label('loc_201C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_2026',
    )

    Jump('loc_233F')

    def _loc_2026(): pass

    label('loc_2026')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_2030',
    )

    Jump('loc_233F')

    def _loc_2030(): pass

    label('loc_2030')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_20CE',
    )

    ChrTalk(
        0x00FE,
        (
            '有谣言说\n',
            '亲卫队的残党们\n',
            '已经潜入王都了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然已经严密警戒，\n',
            '可一个人也抓不到啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只能认为是有人把他们藏起来了。\n',
            '我想你也有同感吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_233F')

    def _loc_20CE(): pass

    label('loc_20CE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_2134',
    )

    ChrTalk(
        0x00FE,
        (
            '呼～好困啊。\n',
            '交班时间早点来就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '照这个样子看来，\n',
            '今年是没法去观看武术大会了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_233F')

    def _loc_2134(): pass

    label('loc_2134')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_2198',
    )

    ChrTalk(
        0x00FE,
        (
            '从今天开始似乎要\n',
            '加强市内的警戒了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看来真的是想要把\n',
            '亲卫队的残余分子揪出来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_233F')

    def _loc_2198(): pass

    label('loc_2198')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_21D6',
    )

    ChrTalk(
        0x00FE,
        (
            '亲卫队的人要是\n',
            '突然改变主意发动\n',
            '恐怖事件呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_233F')

    def _loc_21D6(): pass

    label('loc_21D6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_220A',
    )

    ChrTalk(
        0x00FE,
        (
            '那艘飞艇……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是谁从要塞来了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_233F')

    def _loc_220A(): pass

    label('loc_220A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_2283',
    )

    ChrTalk(
        0x00FE,
        (
            '因为是最新的机型，\n',
            '如果被逃窜中的亲卫队员\n',
            '夺走了就麻烦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以很抱歉，\n',
            '无论是谁都不许接近这艘飞艇。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_233F')

    def _loc_2283(): pass

    label('loc_2283')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_22FC',
    )

    ChrTalk(
        0x00FE,
        (
            '因为是最新的机型，\n',
            '如果被逃窜中的亲卫队员\n',
            '夺走了就麻烦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以很抱歉，\n',
            '无论是谁都不许接近这艘飞艇。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_233F')

    def _loc_22FC(): pass

    label('loc_22FC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_233F',
    )

    ChrTalk(
        0x00FE,
        (
            '『埃尔赛尤号』现由王国军保管。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '普通群众不得接近。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_233F(): pass

    label('loc_233F')

    TalkEnd(0x00FE)

    Return()

# id: 0x000C offset: 0x2343
@scena.Code('func_0C_2343')
def func_0C_2343():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_2350',
    )

    Jump('loc_23A3')

    def _loc_2350(): pass

    label('loc_2350')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_235A',
    )

    Jump('loc_23A3')

    def _loc_235A(): pass

    label('loc_235A')

    ChrTalk(
        0x00FE,
        (
            '很抱歉，就算是游击士，\n',
            '现在也不能予以信任。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好了，你们快走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_23A3(): pass

    label('loc_23A3')

    TalkEnd(0x00FE)

    Return()

# id: 0x000D offset: 0x23A7
@scena.Code('func_0D_23A7')
def func_0D_23A7():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_23B4',
    )

    Jump('loc_241C')

    def _loc_23B4(): pass

    label('loc_23B4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_23BE',
    )

    Jump('loc_241C')

    def _loc_23BE(): pass

    label('loc_23BE')

    ChrTalk(
        0x00FE,
        (
            '平民应该没有什么事情\n',
            '要到这里来办吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '老是在这里晃悠干吗？\n',
            '是要我们抓你们去问话吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_241C(): pass

    label('loc_241C')

    TalkEnd(0x00FE)

    Return()

# id: 0x000E offset: 0x2420
@scena.Code('func_0E_2420')
def func_0E_2420():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_242D',
    )

    Jump('loc_247E')

    def _loc_242D(): pass

    label('loc_242D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_2437',
    )

    Jump('loc_247E')

    def _loc_2437(): pass

    label('loc_2437')

    ChrTalk(
        0x00FE,
        (
            '格兰赛尔空港\n',
            '暂时处于封锁状态。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这也是为了市民们的安全着想。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_247E(): pass

    label('loc_247E')

    TalkEnd(0x00FE)

    Return()

# id: 0x000F offset: 0x2482
@scena.Code('func_0F_2482')
def func_0F_2482():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '……游击士算个什么呀？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0010 offset: 0x24A5
@scena.Code('func_10_24A5')
def func_10_24A5():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '你们要干什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不想挨揍的话\n',
            '就乖乖回家睡觉去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0011 offset: 0x24E5
@scena.Code('func_11_24E5')
def func_11_24E5():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '可疑的家伙……\n',
            '你们是恐怖分子的同伴吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '快点滚开，\n',
            '别让我再看见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0012 offset: 0x2538
@scena.Code('func_12_2538')
def func_12_2538():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_2609',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0031, 0x01, 0x0020)"),
            Expr.Return,
        ),
        'loc_25AC',
    )

    ChrTalk(
        0x00FE,
        (
            '我说布拉姆，你快看，\n',
            '那个流线型的舰桥构造！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '应该是最棒的对吧？\n',
            '我的心情好激动啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2606')

    def _loc_25AC(): pass

    label('loc_25AC')

    ChrTalk(
        0x00FE,
        (
            '我说鲁迪，你快看，\n',
            '那个流线型的舰桥构造！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '应该是最棒的对吧？\n',
            '我的心情好激动啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2606(): pass

    label('loc_2606')

    Jump('loc_267B')

    def _loc_2609(): pass

    label('loc_2609')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '哇啊～……\n',
            '好优美的形态啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '能够离这么近\n',
            '见到『埃尔赛尤号』……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '特意赶来诞辰庆典\n',
            '真的是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_267B(): pass

    label('loc_267B')

    TalkEnd(0x00FE)

    Return()

# id: 0x0013 offset: 0x267F
@scena.Code('func_13_267F')
def func_13_267F():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_2739',
    )

    ChrTalk(
        0x00FE,
        (
            '我邀请心仪已久的前辈来参加诞辰庆典，\n',
            '她竟然一下就答应了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可是，好不容易来了王都，\n',
            '却一直都逗留在空港这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呜～我一定要想办法把她\n',
            '带到更加有情调的地方才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_27DB')

    def _loc_2739(): pass

    label('loc_2739')

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x00FE,
        (
            '我邀请心仪已久的前辈来参加诞辰庆典，\n',
            '她竟然一下就答应了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然我的工作非常艰苦，\n',
            '但我还是努力坚持到了现在。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呜呜，\n',
            '我怎么不知不觉就哭起来了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_27DB(): pass

    label('loc_27DB')

    TalkEnd(0x00FE)

    Return()

# id: 0x0014 offset: 0x27DF
@scena.Code('func_14_27DF')
def func_14_27DF():
    If(
        (
            (Expr.Eval, "OP_29(0x0031, 0x01, 0x0200)"),
            Expr.Return,
        ),
        'loc_2838',
    )

    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '今天对你我来说\n',
            '都是决胜的日子！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '祝你们两个\n',
            '诞辰庆典玩得愉快！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A53')

    def _loc_2838(): pass

    label('loc_2838')

    TalkBegin(0x00FE)
    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))
    OP_28(0x0031, 0x01, 0x0200)
    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '啊，是你们！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#501F？？？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '是我，是我啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我是曾经让你们帮忙送信的\n',
            '沃尔费堡垒的布拉姆！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#501F啊～你是那个时候的士兵嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F很久不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎呀～\n',
            '真的不知道该怎么感谢你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '多亏了那封信，\n',
            '我和菲又重归于好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#001F真是不错啊。\n',
            '恭喜你们了⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，谢谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎，说起来你们俩\n',
            '今天也在一起啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#008F哎……！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#503F是、是啊，\n',
            '说得没错……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯嗯，看样子今天　\n',
            '对你我来说都是决胜的日子！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '愿你们两个\n',
            '也能得到幸福！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#506F啊，嗯……谢谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2A53(): pass

    label('loc_2A53')

    TalkEnd(0x00FE)

    Return()

# id: 0x0015 offset: 0x2A57
@scena.Code('func_15_2A57')
def func_15_2A57():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '定期船起降坪\n',
            '≡　开往洛连特市\n',
            '≡　开往蔡斯市\n',
            '≡　开往卡尔瓦德共和国',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※请勿携带易燃物和危险品\n',
            '　　　　　利贝尔飞艇公社',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0016 offset: 0x2B04
@scena.Code('func_16_2B04')
def func_16_2B04():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '　　　飞艇坪塔台　　　　\n',
            '　※无关人员禁止入内　　\n',
            '『利贝尔飞艇公社』　',
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
