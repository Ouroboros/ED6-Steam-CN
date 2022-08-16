import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T4302_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4302   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4302.x'
    header.mapIndex       = 1
    header.bgm            = 17
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
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH01130._CH', 'ED6_DT07/CH01130P._CP'),
        ('ED6_DT07/CH01170._CH', 'ED6_DT07/CH01170P._CP'),
        ('ED6_DT07/CH01470._CH', 'ED6_DT07/CH01470P._CP'),
        ('ED6_DT07/CH02140._CH', 'ED6_DT07/CH02140P._CP'),
        ('ED6_DT07/CH02470._CH', 'ED6_DT07/CH02470P._CP'),
        ('ED6_DT07/CH01600._CH', 'ED6_DT07/CH01600P._CP'),
        ('ED6_DT07/CH01300._CH', 'ED6_DT07/CH01300P._CP'),
        ('ED6_DT07/CH00322._CH', 'ED6_DT07/CH00322P._CP'),
        ('ED6_DT07/CH00320._CH', 'ED6_DT07/CH00320P._CP'),
        ('ED6_DT07/CH00321._CH', 'ED6_DT07/CH00321P._CP'),
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
        ('ED6_DT07/CH01003._CH', 'ED6_DT07/CH01003P._CP'),
        ('ED6_DT07/CH01150._CH', 'ED6_DT07/CH01150P._CP'),
        ('ED6_DT07/CH01730._CH', 'ED6_DT07/CH01730P._CP'),
        ('ED6_DT07/CH01731._CH', 'ED6_DT07/CH01731P._CP'),
    ]

# id: 0x10001 offset: 0x12A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '王都市民',
            x                   = 7870,
            z                   = 0,
            y                   = 39410,
            direction           = 135,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '王都市民',
            x                   = 7190,
            z                   = 0,
            y                   = 38470,
            direction           = 135,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            name                = '王都市民',
            x                   = 11280,
            z                   = 20,
            y                   = 38050,
            direction           = 135,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            name                = '王都市民',
            x                   = 11270,
            z                   = 0,
            y                   = 36380,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            name                = '王都市民',
            x                   = 12000,
            z                   = 380,
            y                   = 27330,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0135,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            name                = '旅行者',
            x                   = -9500,
            z                   = 250,
            y                   = 43800,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '鸽子',
            x                   = 13510,
            z                   = 0,
            y                   = 37730,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0005,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '鸽子',
            x                   = 12860,
            z                   = 0,
            y                   = 36360,
            direction           = 315,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0006,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '杜南公爵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '管家菲利普',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '王国军士官',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '卫兵',
            x                   = -1960,
            z                   = 0,
            y                   = 19780,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0011,
        ),
        ScenaNpcData(
            name                = '卫兵',
            x                   = 1960,
            z                   = 0,
            y                   = 19780,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0012,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 8860,
            z                   = 250,
            y                   = 42720,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0007,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = -8860,
            z                   = 250,
            y                   = 31000,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0008,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0014,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 1920,
            z                   = 1000,
            y                   = 57170,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0015,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = -1920,
            z                   = 1000,
            y                   = 57170,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0016,
        ),
    )

# id: 0x10002 offset: 0x34A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x34A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x34A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -15850,
            triggerZ            = 0,
            triggerY            = 49490,
            triggerRange        = 1000,
            actorX              = -15740,
            actorZ              = -2000,
            actorY              = 51780,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0020,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x36E
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 2, 0x162A)),
            Expr.Return,
        ),
        'loc_3D6',
    )

    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000D, 0x0080)
    ChrSetFlags(0x000E, 0x0080)
    ChrSetFlags(0x000F, 0x0080)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3B6',
    )

    ChrClearFlags(0x0015, 0x0080)
    ChrClearFlags(0x0016, 0x0080)

    Jump('loc_3D6')

    def _loc_3B6(): pass

    label('loc_3B6')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3D6',
    )

    ChrClearFlags(0x0015, 0x0080)
    ChrClearFlags(0x0016, 0x0080)
    ChrClearFlags(0x0017, 0x0080)
    ChrClearFlags(0x0018, 0x0080)

    def _loc_3D6(): pass

    label('loc_3D6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_3F5',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    MapSetFlags(0x10000000)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, func_18_2964)

    Jump('loc_435')

    def _loc_3F5(): pass

    label('loc_3F5')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_405'),
        (0x00000065, 'loc_41D'),
        (-1, 'loc_435'),
    )

    def _loc_405(): pass

    label('loc_405')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 4, 0x160C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_41A',
    )

    MapSetFlags(0x10000000)
    Event(0, func_17_223E)

    def _loc_41A(): pass

    label('loc_41A')

    Jump('loc_435')

    def _loc_41D(): pass

    label('loc_41D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 3, 0x162B)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 4, 0x162C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_432',
    )

    MapSetFlags(0x10000000)
    Event(0, func_1A_2BED)

    def _loc_432(): pass

    label('loc_432')

    Jump('loc_435')

    def _loc_435(): pass

    label('loc_435')

    Return()

# id: 0x0001 offset: 0x436
@scena.Code('func_01_436')
def func_01_436():
    OP_16(0x02, 4000, -128000, -96000, 2293857)
    OP_6F(0x0001, 60)

    Return()

# id: 0x0002 offset: 0x450
@scena.Code('func_02_450')
def func_02_450():
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
        'loc_475',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_5B7')

    def _loc_475(): pass

    label('loc_475')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_48E',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_5B7')

    def _loc_48E(): pass

    label('loc_48E')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4A7',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_5B7')

    def _loc_4A7(): pass

    label('loc_4A7')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4C0',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_5B7')

    def _loc_4C0(): pass

    label('loc_4C0')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4D9',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_5B7')

    def _loc_4D9(): pass

    label('loc_4D9')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4F2',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_5B7')

    def _loc_4F2(): pass

    label('loc_4F2')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_50B',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_5B7')

    def _loc_50B(): pass

    label('loc_50B')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_524',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_5B7')

    def _loc_524(): pass

    label('loc_524')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_53D',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_5B7')

    def _loc_53D(): pass

    label('loc_53D')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_556',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_5B7')

    def _loc_556(): pass

    label('loc_556')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_56F',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_5B7')

    def _loc_56F(): pass

    label('loc_56F')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_588',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_5B7')

    def _loc_588(): pass

    label('loc_588')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5A1',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_5B7')

    def _loc_5A1(): pass

    label('loc_5A1')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5B7',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_5B7(): pass

    label('loc_5B7')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5CC',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_5B7')

    def _loc_5CC(): pass

    label('loc_5CC')

    Return()

# id: 0x0003 offset: 0x5CD
@scena.Code('func_03_5CD')
def func_03_5CD():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5F0',
    )

    OP_8D(0x00FE, 10600, 38120, 11980, 37360, 3000)

    Jump('func_03_5CD')

    def _loc_5F0(): pass

    label('loc_5F0')

    Return()

# id: 0x0004 offset: 0x5F1
@scena.Code('func_04_5F1')
def func_04_5F1():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_614',
    )

    OP_8D(0x00FE, 10270, 36610, 11740, 35690, 3000)

    Jump('func_04_5F1')

    def _loc_614(): pass

    label('loc_614')

    Return()

# id: 0x0005 offset: 0x615
@scena.Code('func_05_615')
def func_05_615():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_638',
    )

    OP_8D(0x00FE, 12960, 38330, 14560, 37580, 3000)

    Jump('func_05_615')

    def _loc_638(): pass

    label('loc_638')

    Return()

# id: 0x0006 offset: 0x639
@scena.Code('func_06_639')
def func_06_639():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_65C',
    )

    OP_8D(0x00FE, 12580, 37110, 13800, 35710, 3000)

    Jump('func_06_639')

    def _loc_65C(): pass

    label('loc_65C')

    Return()

# id: 0x0007 offset: 0x65D
@scena.Code('func_07_65D')
def func_07_65D():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_705',
    )

    ChrWalkTo(0x00FE, 8760, 250, 41640, 2000, 0x00)
    ChrSetDirection(0x00FE, 90, 400)
    Sleep(1000)

    ChrSetDirection(0x00FE, 270, 400)
    Sleep(1000)

    ChrWalkTo(0x00FE, 3400, 0, 41640, 2000, 0x00)
    ChrWalkTo(0x00FE, 2060, 0, 40640, 2000, 0x00)
    ChrWalkTo(0x00FE, 2060, 0, 33440, 2000, 0x00)
    ChrWalkTo(0x00FE, 3780, 0, 32520, 2000, 0x00)
    ChrWalkTo(0x00FE, 8760, 250, 32520, 2000, 0x00)
    ChrSetDirection(0x00FE, 180, 400)
    Sleep(1500)

    Jump('func_07_65D')

    def _loc_705(): pass

    label('loc_705')

    Return()

# id: 0x0008 offset: 0x706
@scena.Code('func_08_706')
def func_08_706():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_7AE',
    )

    ChrWalkTo(0x00FE, -8760, 250, 32560, 2000, 0x00)
    ChrSetDirection(0x00FE, 270, 400)
    Sleep(1000)

    ChrSetDirection(0x00FE, 90, 400)
    Sleep(1000)

    ChrWalkTo(0x00FE, -3260, 250, 32560, 2000, 0x00)
    ChrWalkTo(0x00FE, -1940, 0, 33880, 2000, 0x00)
    ChrWalkTo(0x00FE, -1940, 0, 40100, 2000, 0x00)
    ChrWalkTo(0x00FE, -3100, 0, 41680, 2000, 0x00)
    ChrWalkTo(0x00FE, -8760, 0, 41680, 2000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)
    Sleep(1500)

    Jump('func_08_706')

    def _loc_7AE(): pass

    label('loc_7AE')

    Return()

# id: 0x0009 offset: 0x7AF
@scena.Code('func_09_7AF')
def func_09_7AF():
    OP_4A(0x00FE, 255)
    TalkBegin(0x00FE)
    OP_62(0x00FE, 0x00000000, 1900, 0x30, 0x32, 0x00000096, 0x00)
    PlaySE(48, 0x00, 0x64)
    ChrTurnDirection(0x00FE, 0x0101, 0)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '*chirp chirp chirp chirp chirp chirp chirp*',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)
    OP_4B(0x00FE, 255)

    Return()

# id: 0x000A offset: 0x812
@scena.Code('func_0A_812')
def func_0A_812():
    OP_4A(0x00FE, 255)
    TalkBegin(0x00FE)
    OP_62(0x00FE, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    ChrTurnDirection(0x00FE, 0x0101, 0)
    Sleep(1000)

    UnlockAchievement(0x00, 0x0003, 0x00)

    ChrTalk(
        0x00FE,
        (
            '*chirp! chirp? chirp!*',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)
    OP_4B(0x00FE, 255)

    Return()

# id: 0x000B offset: 0x865
@scena.Code('func_0B_865')
def func_0B_865():
    TalkBegin(0x0008)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A15',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            Expr.Return,
        ),
        'loc_8D5',
    )

    ChrTalk(
        0x00FE,
        (
            '现在吃的是\n',
            '妻子做的三明治,很特别啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这是利贝尔第一……\n',
            '不，世界第一美味啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A15')

    def _loc_8D5(): pass

    label('loc_8D5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 5, 0x160D)),
            Expr.Return,
        ),
        'loc_94A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_906',
    )

    ChrTalk(
        0x00FE,
        (
            '……孩子们天真烂漫多好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_947')

    def _loc_906(): pass

    label('loc_906')

    ChrTalk(
        0x00FE,
        (
            '哎，什么？\n',
            '穿白裙子的女孩子？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯～大概\n',
            '没见过吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_947(): pass

    label('loc_947')

    Jump('loc_A15')

    def _loc_94A(): pass

    label('loc_94A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_A15',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_9A5',
    )

    ChrTalk(
        0x00FE,
        (
            '这个离宫只要得到许可，\n',
            '也能在庭园进餐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是有点\n',
            '郊游的感觉啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A15')

    def _loc_9A5(): pass

    label('loc_9A5')

    ChrTalk(
        0x00FE,
        (
            '这个离宫只要得到许可，\n',
            '也能在庭园进餐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '家庭围在一起\n',
            '不觉得很适合吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是有点\n',
            '郊游的感觉啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_A15(): pass

    label('loc_A15')

    TalkEnd(0x0008)

    Return()

# id: 0x000C offset: 0xA19
@scena.Code('func_0C_A19')
def func_0C_A19():
    TalkBegin(0x0009)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_BFF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            Expr.Return,
        ),
        'loc_A72',
    )

    ChrTalk(
        0x00FE,
        (
            '大家都开怀\n',
            '大吃就最开心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵，早起\n',
            '制作也值得了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BFF')

    def _loc_A72(): pass

    label('loc_A72')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 5, 0x160D)),
            Expr.Return,
        ),
        'loc_B45',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_AD1',
    )

    ChrTalk(
        0x00FE,
        (
            '女孩子是见过不少，\n',
            '详细的样子就不记得了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对不起，\n',
            '问问其他人好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B42')

    def _loc_AD1(): pass

    label('loc_AD1')

    ChrTalk(
        0x00FE,
        (
            '……哎，穿白裙子的女孩子？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '女孩子是见过不少，\n',
            '详细的样子就不记得了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对不起，\n',
            '问问其他人好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_B42(): pass

    label('loc_B42')

    Jump('loc_BFF')

    def _loc_B45(): pass

    label('loc_B45')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_BFF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_B9E',
    )

    ChrTalk(
        0x00FE,
        (
            '这么漂亮的地方，\n',
            '没理由不利用啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '又不收入场费，\n',
            '家计也省了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BFF')

    def _loc_B9E(): pass

    label('loc_B9E')

    ChrTalk(
        0x00FE,
        (
            '我们家经常\n',
            '来这个艾尔贝离宫的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '难得女王陛下向市民\n',
            '开放了嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没理由不利用啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_BFF(): pass

    label('loc_BFF')

    TalkEnd(0x0009)

    Return()

# id: 0x000D offset: 0xC03
@scena.Code('func_0D_C03')
def func_0D_C03():
    TalkBegin(0x000A)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_CD6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            Expr.Return,
        ),
        'loc_C60',
    )

    ChrTalk(
        0x00FE,
        (
            '喂，妈妈好不容易\n',
            '做的三明治哦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为什么要给鸽子\n',
            '那么多嘛！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CD6')

    def _loc_C60(): pass

    label('loc_C60')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 5, 0x160D)),
            Expr.Return,
        ),
        'loc_C9D',
    )

    ChrTalk(
        0x00FE,
        (
            '仔细听就明白了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '它们咕噜咕噜\n',
            '地说话呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CD6')

    def _loc_C9D(): pass

    label('loc_C9D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_CD6',
    )

    ChrTalk(
        0x00FE,
        (
            '笨蛋，鸽子叫\n',
            '从来都是咕噜咕噜\n',
            '的这还用说吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_CD6(): pass

    label('loc_CD6')

    TalkEnd(0x000A)

    Return()

# id: 0x000E offset: 0xCDA
@scena.Code('func_0E_CDA')
def func_0E_CDA():
    TalkBegin(0x000B)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_DC3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            Expr.Return,
        ),
        'loc_D3F',
    )

    ChrTalk(
        0x00FE,
        (
            '看、看着\n',
            '鸽子的眼睛，忍不住就……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我说，姐姐\n',
            '不是也在一起喂吗～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DC3')

    def _loc_D3F(): pass

    label('loc_D3F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 5, 0x160D)),
            Expr.Return,
        ),
        'loc_D8F',
    )

    ChrTalk(
        0x00FE,
        (
            '骗人，我听到的是\n',
            '啵啵的声音啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '喂食看看，\n',
            '这次好好听着啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DC3')

    def _loc_D8F(): pass

    label('loc_D8F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_DC3',
    )

    ChrTalk(
        0x00FE,
        (
            '对了，姐姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '鸽子\n',
            '是啵啵叫的对吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_DC3(): pass

    label('loc_DC3')

    TalkEnd(0x000B)

    Return()

# id: 0x000F offset: 0xDC7
@scena.Code('func_0F_DC7')
def func_0F_DC7():
    TalkBegin(0x000C)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_110D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            Expr.Return,
        ),
        'loc_EA2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_E2F',
    )

    ChrTalk(
        0x00FE,
        (
            '好了，从外观来看\n',
            '也完全恢复了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '天也晚了，\n',
            '差不多该回家了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E9F')

    def _loc_E2F(): pass

    label('loc_E2F')

    ChrTalk(
        0x00FE,
        (
            '好了，从外观来看\n',
            '也完全恢复了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '天也晚了，\n',
            '差不多该回家了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗬嗬，今天又是\n',
            '散了老长的步啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_E9F(): pass

    label('loc_E9F')

    Jump('loc_110D')

    def _loc_EA2(): pass

    label('loc_EA2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 5, 0x160D)),
            Expr.Return,
        ),
        'loc_1007',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_F34',
    )

    ChrTalk(
        0x00FE,
        (
            '怎么说，别看我这样，\n',
            '都活了７０岁以上了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '穿白衣服的女孩子\n',
            '多少看见过一个两个，\n',
            '但在哪看到的就不记得了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈哈哈。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1004')

    def _loc_F34(): pass

    label('loc_F34')

    ChrTalk(
        0x00FE,
        (
            '……有没看见\n',
            '穿白衣服的女孩子？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这个啊，好像有，\n',
            '又好像没有似的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '怎么说，别看我这样，\n',
            '都活了７０岁以上了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '穿白衣服的女孩子\n',
            '多少看见过一个两个，\n',
            '但在哪看到的就不记得了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈哈哈。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_1004(): pass

    label('loc_1004')

    Jump('loc_110D')

    def _loc_1007(): pass

    label('loc_1007')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_110D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1074',
    )

    ChrTalk(
        0x00FE,
        (
            '我的必杀技\n',
            '过肩摔想学吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样，把前襟\n',
            '一把抓住……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……好痛，腰、腰，腰啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_110D')

    def _loc_1074(): pass

    label('loc_1074')

    ChrTalk(
        0x00FE,
        (
            '离宫附近的草木丛中\n',
            '传来了恐怖的声音。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果是魔兽\n',
            '就拖出来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哐当～的来一个\n',
            '必杀技过肩摔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不知道是不是害怕我\n',
            '最终还是没现身。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_110D(): pass

    label('loc_110D')

    TalkEnd(0x000C)

    Return()

# id: 0x0010 offset: 0x1111
@scena.Code('func_10_1111')
def func_10_1111():
    TalkBegin(0x000D)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1296',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            Expr.Return,
        ),
        'loc_1174',
    )

    ChrTalk(
        0x00FE,
        (
            '艾尔贝离宫本\n',
            '打算看看就好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但感觉很舒服，\n',
            '不知不觉就久坐了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1296')

    def _loc_1174(): pass

    label('loc_1174')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 5, 0x160D)),
            Expr.Return,
        ),
        'loc_11BE',
    )

    ChrTalk(
        0x00FE,
        (
            '……在找穿白裙子\n',
            '的女孩子？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对不起，\n',
            '我看来帮不上忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1296')

    def _loc_11BE(): pass

    label('loc_11BE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_1296',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_1215',
    )

    ChrTalk(
        0x00FE,
        (
            '这里的庭园\n',
            '完全没有垃圾……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '使用这里的人们\n',
            '看来很懂礼仪啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1296')

    def _loc_1215(): pass

    label('loc_1215')

    ChrTalk(
        0x00FE,
        (
            '哦～虽然简单,\n',
            '但感觉很不错的庭园嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '树丛和草坪也仔细\n',
            '修剪过，相当漂亮。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '本来以为会更华丽的，\n',
            '这样的也不坏呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_1296(): pass

    label('loc_1296')

    TalkEnd(0x000D)

    Return()

# id: 0x0011 offset: 0x129A
@scena.Code('func_11_129A')
def func_11_129A():
    TalkBegin(0x0013)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_13DB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_13D8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_1335',
    )

    ChrTalk(
        0x00FE,
        (
            '这种混乱之中\n',
            '能来艾尔贝离宫可真稀奇。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果想进去，\n',
            '就尽管通过没关系的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在除了我们卫兵以外\n',
            '只有职员数名。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_13D8')

    def _loc_1335(): pass

    label('loc_1335')

    ChrTalk(
        0x00FE,
        (
            '哎呀，你们\n',
            '看来好像是游击士……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这种混乱之中\n',
            '能来艾尔贝离宫可真稀奇。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果想进去，\n',
            '就尽管通过没关系的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在除了我们卫兵以外\n',
            '只有职员数名。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_13D8(): pass

    label('loc_13D8')

    Jump('loc_17D3')

    def _loc_13DB(): pass

    label('loc_13DB')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_17D3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_148E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_1433',
    )

    ChrTalk(
        0x00FE,
        (
            '希德中校说过\n',
            '让你们游击士通过的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '别客气进去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_148B')

    def _loc_1433(): pass

    label('loc_1433')

    ChrTalk(
        0x00FE,
        (
            '欢迎光临艾尔贝离宫。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '希德中校说过\n',
            '让你们游击士通过的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '别客气进去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_148B(): pass

    label('loc_148B')

    Jump('loc_17D3')

    def _loc_148E(): pass

    label('loc_148E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 3, 0x162B)),
            Expr.Return,
        ),
        'loc_14EC',
    )

    ChrTalk(
        0x00FE,
        (
            '警备本部也平安设置好，\n',
            '感觉签字仪式也终于快到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '警备也比往常\n',
            '更加严格。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17D3')

    def _loc_14EC(): pass

    label('loc_14EC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            Expr.Return,
        ),
        'loc_1567',
    )

    ChrTalk(
        0x00FE,
        (
            '今天来离宫\n',
            '的人似乎挺多的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为签字仪式开始后\n',
            '普通市民就不能进来了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天来的人\n',
            '好像挺多的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17D3')

    def _loc_1567(): pass

    label('loc_1567')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 5, 0x160D)),
            Expr.Return,
        ),
        'loc_161A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_15BB',
    )

    ChrTalk(
        0x00FE,
        (
            '穿白裙子的女孩子？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '到底不可能全部记住\n',
            '入场的每一个人啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1617')

    def _loc_15BB(): pass

    label('loc_15BB')

    ChrTalk(
        0x00FE,
        (
            '穿白裙子的女孩子？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天人特别多……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '到底不可能全部记住\n',
            '入场的每一个人啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_1617(): pass

    label('loc_1617')

    Jump('loc_17D3')

    def _loc_161A(): pass

    label('loc_161A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_17D3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02CB, 5, 0x165D)),
            Expr.Return,
        ),
        'loc_1677',
    )

    ChrTalk(
        0x00FE,
        (
            '跑进去的\n',
            '老人碰到魔兽逃跑时\n',
            '好像腰痛起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那个人……不要紧吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17D3')

    def _loc_1677(): pass

    label('loc_1677')

    ChrTalk(
        0x00FE,
        (
            '我想问一下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '方才，有个\n',
            '说是听到可怕\n',
            '魔兽声音的老人跑进去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这里入口附近\n',
            '有发生什么奇怪的事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1015F啊啊，一定\n',
            '是说那只大魔兽吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1000F我们已经打倒它了,\n',
            '应该没问题了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哦哦，这样吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……这么说来，你们\n',
            '看来好像是游击士呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '作为搜索和惩治的\n',
            '先锋真是帮大忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '感谢你们的协助。\n',
            '在离宫好好放松吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x02CB, 5, 0x165D))

    def _loc_17D3(): pass

    label('loc_17D3')

    TalkEnd(0x0013)

    Return()

# id: 0x0012 offset: 0x17D7
@scena.Code('func_12_17D7')
def func_12_17D7():
    TalkBegin(0x0014)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1839',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1836',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然事态严重，但离宫里\n',
            '只有卫兵和相关人员……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不介意就通过吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1836(): pass

    label('loc_1836')

    Jump('loc_1A43')

    def _loc_1839(): pass

    label('loc_1839')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1A43',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_18E1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_1885',
    )

    ChrTalk(
        0x00FE,
        (
            '请进。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '来过指示，\n',
            '你们来了就让放行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_18DE')

    def _loc_1885(): pass

    label('loc_1885')

    ChrTalk(
        0x00FE,
        (
            '你们就是这次配合\n',
            '搜查的游击士吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '请进。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '上门有指示\n',
            '你们来了就放行的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_18DE(): pass

    label('loc_18DE')

    Jump('loc_1A43')

    def _loc_18E1(): pass

    label('loc_18E1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 3, 0x162B)),
            Expr.Return,
        ),
        'loc_1951',
    )

    ChrTalk(
        0x00FE,
        (
            '艾尔贝离宫在签字仪式当日之前\n',
            '都是王国军的警备本部。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '再次对市民开放\n',
            '要到签字仪式的结束后了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A43')

    def _loc_1951(): pass

    label('loc_1951')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            Expr.Return,
        ),
        'loc_19C0',
    )

    ChrTalk(
        0x00FE,
        (
            '为了迎接条约的签字仪式，\n',
            '听说格兰赛尔地区\n',
            '马上就要强化警备。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这里对市民开放\n',
            '也到那时为止。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A43')

    def _loc_19C0(): pass

    label('loc_19C0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 5, 0x160D)),
            Expr.Return,
        ),
        'loc_19FF',
    )

    ChrTalk(
        0x00FE,
        (
            '哎？　女孩子吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……对不起，\n',
            '我没有印象。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A43')

    def _loc_19FF(): pass

    label('loc_19FF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_1A43',
    )

    ChrTalk(
        0x00FE,
        (
            '这个艾尔贝离宫，现在\n',
            '是向市民开放的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '请自由进入。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A43(): pass

    label('loc_1A43')

    TalkEnd(0x0014)

    Return()

# id: 0x0013 offset: 0x1A47
@scena.Code('func_13_1A47')
def func_13_1A47():
    TalkBegin(0x0015)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1B42',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1B3F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_1AC1',
    )

    ChrTalk(
        0x00FE,
        (
            '导力灯不能使用的夜晚\n',
            '警备可真恐怖啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '何时会从森林中会跑出\n',
            '魔兽来袭击也说不定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B3F')

    def _loc_1AC1(): pass

    label('loc_1AC1')

    ChrTalk(
        0x00FE,
        (
            '这里白天警备时\n',
            '还没什么不安。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '导力灯不能使用的\n',
            '夜晚可真够吓人的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '何时会从森林中会跑出\n',
            '魔兽来袭击也说不定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    def _loc_1B3F(): pass

    label('loc_1B3F')

    Jump('loc_1C77')

    def _loc_1B42(): pass

    label('loc_1B42')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1C77',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_1BA4',
    )

    ChrTalk(
        0x00FE,
        (
            '情报部袭击这里\n',
            '目的似乎是佯攻啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，希德中校\n',
            '到底是看破了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C77')

    def _loc_1BA4(): pass

    label('loc_1BA4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 3, 0x162B)),
            Expr.Return,
        ),
        'loc_1C77',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_1BFF',
    )

    ChrTalk(
        0x00FE,
        (
            '让公爵呆在这里\n',
            '也只会妨碍警备……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是让他回\n',
            '格兰赛尔没问题吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C77')

    def _loc_1BFF(): pass

    label('loc_1BFF')

    ChrTalk(
        0x00FE,
        (
            '如你所见杜南公爵的\n',
            '防备心理似乎解除了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '让他呆在这里\n',
            '也只会妨碍警备……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是让他回\n',
            '格兰赛尔没问题吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    def _loc_1C77(): pass

    label('loc_1C77')

    TalkEnd(0x0015)

    Return()

# id: 0x0014 offset: 0x1C7B
@scena.Code('func_14_1C7B')
def func_14_1C7B():
    TalkBegin(0x0016)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1D62',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1D5F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_1CE6',
    )

    ChrTalk(
        0x00FE,
        (
            '部分的通信似乎也恢复了，\n',
            '但是离宫这里还没收到消息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是不安……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D5F')

    def _loc_1CE6(): pass

    label('loc_1CE6')

    ChrTalk(
        0x00FE,
        (
            '导力器不能使用了，\n',
            '今后会变成怎样呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '部分的通信似乎也恢复了，\n',
            '但是离宫这里还没收到消息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是不安……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    def _loc_1D5F(): pass

    label('loc_1D5F')

    Jump('loc_2025')

    def _loc_1D62(): pass

    label('loc_1D62')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2025',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_1E72',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_1E08',
    )

    ChrTalk(
        0x00FE,
        (
            '没想到，会再次和\n',
            '特务兵的人作战。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然想办法以数量取胜了，\n',
            '那些家伙可真不得了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '事关白刃战的技术，\n',
            '还真是相当了得啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E6F')

    def _loc_1E08(): pass

    label('loc_1E08')

    ChrTalk(
        0x00FE,
        (
            '虽然想办法以数量取胜了，\n',
            '特务兵的人真是不得了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '事关白刃战的技术，\n',
            '还真是相当了得啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    def _loc_1E6F(): pass

    label('loc_1E6F')

    Jump('loc_2025')

    def _loc_1E72(): pass

    label('loc_1E72')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 3, 0x162B)),
            Expr.Return,
        ),
        'loc_2025',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_1F12',
    )

    ChrTalk(
        0x00FE,
        (
            '希德中校和理查德上校\n',
            '比起来是比较保守……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但在守护要塞方面可比上校\n',
            '更加厉害，风评都是如此。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '卡西乌斯准将也相当\n',
            '看中希德中校吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2025')

    def _loc_1F12(): pass

    label('loc_1F12')

    ChrTalk(
        0x00FE,
        (
            '希德中校和理查德上校\n',
            '比起来是比较保守……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但在守护要塞方面可比上校\n',
            '更加厉害，风评都是如此。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '百日战役中，不是有利用关口\n',
            '将帝国军截断的作战吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那个时候，战斗最激烈区域\n',
            '圣海姆门能够防守成功\n',
            '就是多亏了希德中校哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '卡西乌斯准将也相当\n',
            '看中希德中校吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    def _loc_2025(): pass

    label('loc_2025')

    TalkEnd(0x0016)

    Return()

# id: 0x0015 offset: 0x2029
@scena.Code('func_15_2029')
def func_15_2029():
    TalkBegin(0x0017)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2157',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_2092',
    )

    ChrTalk(
        0x00FE,
        (
            '这下情报部的余党\n',
            '也终于全部抓到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '政变事件在真正\n',
            '意义上解决完毕了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2157')

    def _loc_2092(): pass

    label('loc_2092')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 3, 0x162B)),
            Expr.Return,
        ),
        'loc_2157',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_20E2',
    )

    ChrTalk(
        0x00FE,
        (
            '呀～轻松啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '即使是亲卫队也没有\n',
            '迎接公爵那么空闲啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2157')

    def _loc_20E2(): pass

    label('loc_20E2')

    ChrTalk(
        0x00FE,
        (
            '哟，我听说啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '杜南公爵的任性妄为\n',
            '让我们也经常很头痛的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要说教、告诫\n',
            '那公爵……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呀～轻松啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    def _loc_2157(): pass

    label('loc_2157')

    TalkEnd(0x0017)

    Return()

# id: 0x0016 offset: 0x215B
@scena.Code('func_16_215B')
def func_16_215B():
    TalkBegin(0x0018)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_223A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_21BE',
    )

    ChrTalk(
        0x00FE,
        (
            '最近真是\n',
            '好天气连续不断啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '签字仪式当天\n',
            '也有这样的天气就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_223A')

    def _loc_21BE(): pass

    label('loc_21BE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 3, 0x162B)),
            Expr.Return,
        ),
        'loc_223A',
    )

    ChrTalk(
        0x00FE,
        (
            '每次都是这样\n',
            '菲利普先生可真辛苦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果没有相当的忍耐力，\n',
            '可当不了公爵的管家啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那个人真的\n',
            '是个好人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_223A(): pass

    label('loc_223A')

    TalkEnd(0x0018)

    Return()

# id: 0x0017 offset: 0x223E
@scena.Code('func_17_223E')
def func_17_223E():
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
        'loc_2255',
    )

    Call(0, 0x001E)
    Call(0, 0x001F)

    def _loc_2255(): pass

    label('loc_2255')

    CameraMove(680, 1000, 52720, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(315000, 0)
    OP_6E(600, 0)
    OP_C8(0x0200, 0x0046, 'C_PLAC11._CH', 0x01, 0x05DC)
    ShowPlaceName('艾尔贝离宫')
    FadeIn(1500, 0)
    ChrSetPos(0x0101, -240, 0, 26720, 10)
    ChrSetPos(0x00F7, 780, 0, 26810, 10)
    ChrSetPos(0x00F8, -1170, 0, 26020, 10)
    ChrSetPos(0x00F9, 1520, 0, 25840, 10)

    @scena.Lambda('lambda_2306')
    def lambda_2306():
        CameraMove(190, 0, 26660, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2306)

    @scena.Lambda('lambda_231E')
    def lambda_231E():
        OP_6E(262, 9000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_231E)

    @scena.Lambda('lambda_232E')
    def lambda_232E():
        OP_6C(348000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_232E)

    WaitForThreadExit(0x0101, 0x0002)
    Sleep(500)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_237D',
    )

    ChrTalk(
        0x0107,
        (
            '#0070240697V#061F哇，好漂亮的地方……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_237D(): pass

    label('loc_237D')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2420',
    )

    ChrTalk(
        0x0108,
        (
            '#0080240700V#070F艾尔贝离宫……\n',
            '真奇怪，感觉好怀念啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240701V#1006F#5P嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240699V#1015F不过，好像还有普通人\n',
            '也在里面……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_248D')

    def _loc_2420(): pass

    label('loc_2420')

    ChrTalk(
        0x0101,
        (
            '#0010240698V#1006F#5P艾尔贝离宫……\n',
            '感觉好怀念啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240699V#1015F不过，好像还有普通人\n',
            '也在里面……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_248D(): pass

    label('loc_248D')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_24F3',
    )

    ChrTalk(
        0x0105,
        (
            '#0060240703V#040F平时是向\n',
            '市民开放的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060240704V可以算个稍事\n',
            '休息的地方吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_25D4')

    def _loc_24F3(): pass

    label('loc_24F3')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2565',
    )

    ChrTalk(
        0x0106,
        (
            '#0050240705V#051F平时似乎也是向\n',
            '一般市民们开放的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050240706V可以算个稍事\n',
            '休息的地方吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_25D4')

    def _loc_2565(): pass

    label('loc_2565')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_25D4',
    )

    ChrTalk(
        0x0103,
        (
            '#0030240707V#020F平时似乎也是向\n',
            '一般市民开放的呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030240708V可以算个稍事\n',
            '休息的地方吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_25D4(): pass

    label('loc_25D4')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_26C5',
    )

    ChrTalk(
        0x0104,
        (
            '#0040240709V#035F呼，待在精致的空间\n',
            '不由得涌出了创作欲望。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040240710V#030F这就用我的鲁特琴\n',
            '让各位更加愉悦吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240711V#1007F#5P算了吧你……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240712V#1011F不过，这么一说的确\n',
            '看起来有很多人全家都来玩呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2723')

    def _loc_26C5(): pass

    label('loc_26C5')

    ChrTalk(
        0x0101,
        (
            '#0010240713V#1011F#5P哦～这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240714V这么一说的确\n',
            '看起来有很多人全家都来玩呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2723(): pass

    label('loc_2723')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_27E2',
    )

    ChrTalk(
        0x0108,
        (
            '#0080240715V#070F迷路的孩子啊,\n',
            '是那种举家同游的客人家\n',
            '孩子的可能性也很大呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080240716V总而言之，赶快去找那个\n',
            '叫雷蒙德的管家大哥啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240717V#1006F#5PＯＫ。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_295E')

    def _loc_27E2(): pass

    label('loc_27E2')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_28A5',
    )

    ChrTalk(
        0x0106,
        (
            '#0050240718V#053F迷路的小鬼\n',
            '是那种举家同游的客人家\n',
            '孩子的可能性也很大呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050240719V#050F总而言之，赶快去找那个\n',
            '叫雷蒙德的管家吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240720V#1006F#5P嗯，明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_295E')

    def _loc_28A5(): pass

    label('loc_28A5')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_295E',
    )

    ChrTalk(
        0x0103,
        (
            '#0030240721V#020F迷路的孩子\n',
            '是那种举家同游的客人家\n',
            '孩子的可能性也很大呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030240722V总而言之，赶快去找那个\n',
            '叫雷蒙德的管家吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240723V#1006F#5P嗯，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_295E(): pass

    label('loc_295E')

    SetScenaFlags(ScenaFlag(0x02C1, 4, 0x160C))
    EventEnd(0x00)

    Return()

# id: 0x0018 offset: 0x2964
@scena.Code('func_18_2964')
def func_18_2964():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '第二天早晨，艾丝蒂尔等人\n',
            '向艾尔贝离宫的希德中校\n',
            '送交了有关恐吓信的调查报告书。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_DB()
    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000D, 0x0080)
    ChrClearFlags(0x0013, 0x0080)
    ChrClearFlags(0x0014, 0x0080)
    ChrClearFlags(0x0015, 0x0080)
    ChrClearFlags(0x0016, 0x0080)
    ChrClearFlags(0x0017, 0x0080)
    ChrClearFlags(0x0018, 0x0080)
    OP_4A(0x0015, 255)
    OP_4A(0x0016, 255)
    ChrSetPos(0x0013, -7380, 0, 36870, 270)
    ChrSetPos(0x0014, -11200, 0, 36810, 90)
    ChrSetPos(0x0015, 9950, 0, 36540, 314)
    ChrSetPos(0x0016, 6560, 0, 39190, 134)
    ChrSetPos(0x0017, 7820, 0, 31210, 90)
    ChrSetPos(0x0018, -8590, 0, 31290, 270)
    ChrSetChipByIndex(0x0013, 8)
    ChrSetSubChip(0x0013, 0)
    ChrSetChipByIndex(0x0014, 8)
    ChrSetSubChip(0x0014, 0)
    ChrSetChipByIndex(0x0015, 8)
    ChrSetSubChip(0x0015, 0)
    ChrSetChipByIndex(0x0016, 8)
    ChrSetSubChip(0x0016, 0)
    ChrSetChipByIndex(0x0017, 8)
    ChrSetSubChip(0x0017, 0)
    ChrSetChipByIndex(0x0018, 8)
    ChrSetSubChip(0x0018, 0)
    CreateThread(0x0013, 0x00, 0x00, func_19_2BC4)
    Sleep(50)

    CreateThread(0x0015, 0x00, 0x00, func_19_2BC4)
    Sleep(50)

    CreateThread(0x0014, 0x00, 0x00, func_19_2BC4)
    Sleep(50)

    CreateThread(0x0017, 0x00, 0x00, func_19_2BC4)
    Sleep(50)

    CreateThread(0x0016, 0x00, 0x00, func_19_2BC4)
    Sleep(50)

    CreateThread(0x0018, 0x00, 0x00, func_19_2BC4)
    CameraMove(-660, 0, 23220, 0)
    OP_67(0, 6170, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(344000, 0)
    OP_6E(409, 0)
    PlayBGM(17)
    PlaySE(450, 0x00, 0x64)

    @scena.Lambda('lambda_2B58')
    def lambda_2B58():
        CameraMove(680, 1000, 52720, 7000)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_2B58)

    @scena.Lambda('lambda_2B70')
    def lambda_2B70():
        OP_67(0, 8000, -10000, 7000)

        ExitThread()

    DispatchAsync(0x0014, 0x0002, lambda_2B70)

    @scena.Lambda('lambda_2B88')
    def lambda_2B88():
        OP_6C(315000, 8000)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_2B88)

    @scena.Lambda('lambda_2B98')
    def lambda_2B98():
        OP_6E(600, 8000)

        ExitThread()

    DispatchAsync(0x0013, 0x0002, lambda_2B98)

    FadeIn(2000, 0)
    OP_0D()
    WaitForThreadExit(0x0013, 0x0002)
    Sleep(1000)

    OP_DC()
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/T4303._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0019 offset: 0x2BC4
@scena.Code('func_19_2BC4')
def func_19_2BC4():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_2BEC',
    )

    OP_99(0x00FE, 0x00, 0x04, 2600)
    Sleep(500)

    OP_99(0x00FE, 0x04, 0x00, 2600)
    Sleep(1500)

    Jump('func_19_2BC4')

    def _loc_2BEC(): pass

    label('loc_2BEC')

    Return()

# id: 0x001A offset: 0x2BED
@scena.Code('func_1A_2BED')
def func_1A_2BED():
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
        'loc_2C00',
    )

    Call(0, 0x001E)

    def _loc_2C00(): pass

    label('loc_2C00')

    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0012, 0x0080)
    ChrClearFlags(0x0013, 0x0080)
    ChrClearFlags(0x0014, 0x0080)
    ChrSetPos(0x0101, 80, 1000, 59650, 180)
    ChrSetPos(0x00F7, 80, 1000, 59650, 180)
    ChrSetPos(0x0107, 80, 1000, 59650, 180)
    ChrSetPos(0x012F, 80, 1000, 59650, 180)
    ChrSetPos(0x0010, -220, 0, 44940, 180)
    ChrSetPos(0x0011, 560, 0, 45120, 180)
    ChrSetPos(0x0012, 50, 0, 42800, 0)
    ChrSetPos(0x0013, -750, 0, 42500, 0)
    ChrSetPos(0x0014, 750, 0, 42500, 0)
    ChrSetChipByIndex(0x0013, 11)
    ChrSetChipByIndex(0x0014, 11)
    ChrSetSubChip(0x0013, 0)
    ChrSetSubChip(0x0014, 0)
    OP_4A(0x0013, 255)
    OP_4A(0x0014, 255)
    ChrSetFlags(0x0015, 0x0080)
    ChrSetFlags(0x0016, 0x0080)
    OP_4A(0x0015, 255)
    OP_4A(0x0016, 255)
    CameraMove(580, 1000, 56480, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeIn(2000, 0)
    Sleep(1000)

    OP_6F(0x0000, 0)
    OP_70(0x0000, 29)
    OP_73(0x0000)

    @scena.Lambda('lambda_2D42')
    def lambda_2D42():
        ChrWalkTo(0x00FE, 500, 1000, 55180, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2D42)

    Sleep(600)

    @scena.Lambda('lambda_2D62')
    def lambda_2D62():
        ChrWalkTo(0x00FE, -500, 1000, 55180, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0000, lambda_2D62)

    Sleep(600)

    @scena.Lambda('lambda_2D82')
    def lambda_2D82():
        ChrWalkTo(0x00FE, -500, 1000, 56340, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0000, lambda_2D82)

    Sleep(600)

    @scena.Lambda('lambda_2DA2')
    def lambda_2DA2():
        ChrWalkTo(0x00FE, 500, 1000, 56340, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x012F, 0x0000, lambda_2DA2)

    WaitForThreadExit(0x0101, 0x0000)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010260416V#1004F#5P咦……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2DEA')
    def lambda_2DEA():
        CameraMove(470, 0, 44880, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2DEA)

    @scena.Lambda('lambda_2E02')
    def lambda_2E02():
        OP_6C(45000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2E02)

    @scena.Lambda('lambda_2E12')
    def lambda_2E12():
        OP_67(0, 8189, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2E12)

    CameraSetDistance(2450, 3000)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)
    WaitForThreadExit(0x0101, 0x0003)

    ChrTalk(
        0x0010,
        (
            '#0640260417V#224F#5P怎么回事，这是！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640260418V把拥有第一王位继承权的\n',
            '杜南·冯·奥赛雷丝\n',
            '当做无知的白痴来耍弄吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#2440260419V完、完全没有的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#2440260420V其实今天早上，进行了艾尔贝周游道\n',
            '的魔兽扫荡作战……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#2440260421V因此护卫的数量\n',
            '这样也足够了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0640260422V#224F#5P不是这个意思！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640260423V对我这样的重要人物\n',
            '护卫只有３个人实在太无礼了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640260424V至少要准备１０名！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#2440260425V可，可是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0011, 0x0013, 400)
    Sleep(500)

    ChrTalk(
        0x0011,
        (
            '#0660260426V#722F#2P阁下……\n',
            '别说得太过分了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660260427V难得陛下\n',
            '下了许可。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660260428V仅此\n',
            '就应该觉得万幸……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0640260429V#222F#5P住口，菲利普！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640260430V说到底处分这事\n',
            '就不当至极。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640260431V那么亲卫队全员\n',
            '出迎也是应该的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010260432V#4P嗯，亲卫队全员\n',
            '到底是来不了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010260433V可以的话我们\n',
            '陪你一起可以吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0010, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    @scena.Lambda('lambda_3178')
    def lambda_3178():
        CameraMove(-70, 0, 46500, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3178)

    @scena.Lambda('lambda_3190')
    def lambda_3190():
        OP_67(0, 8050, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_3190)

    @scena.Lambda('lambda_31A8')
    def lambda_31A8():
        OP_6E(300, 4000)

        ExitThread()

    DispatchAsync(0x00F7, 0x0003, lambda_31A8)

    @scena.Lambda('lambda_31B8')
    def lambda_31B8():
        ChrWalkTo(0x00FE, 180, 0, 46470, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_31B8)

    Sleep(100)

    @scena.Lambda('lambda_31D8')
    def lambda_31D8():
        ChrTurnDirection(0x0010, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_31D8)

    @scena.Lambda('lambda_31E6')
    def lambda_31E6():
        ChrTurnDirection(0x0011, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_31E6)

    @scena.Lambda('lambda_31F4')
    def lambda_31F4():
        ChrWalkTo(0x00FE, -950, 0, 46700, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_31F4)

    Sleep(50)

    @scena.Lambda('lambda_3214')
    def lambda_3214():
        ChrWalkTo(0x00FE, 200, 250, 47700, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x012F, 0x0001, lambda_3214)

    Sleep(100)

    @scena.Lambda('lambda_3234')
    def lambda_3234():
        ChrWalkTo(0x00FE, -900, 250, 47700, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_3234)

    WaitForThreadExit(0x0101, 0x0002)
    OP_62(0x0010, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0010,
        (
            '#0640260434V#226F#6P你、你们是！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0660260435V#721F#4P哦哦，各位……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010260436V#1007F真是的……\n',
            '公爵先生也是一点都没变呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010260437V#1019F说话太任性\n',
            '让大家为难可不行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0640260438V#226F#6P别、别随便\n',
            '乱叫什么公爵先生！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640260439V为什么你们\n',
            '会在这种地方！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640260440V不是已经禁止\n',
            '民间人士进入了吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010260441V#1006F只是有东西要交给\n',
            '这里的警备责任人啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010260442V那，公爵先生你们\n',
            '现在要去散步吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0640260443V#220F#6P哼、哼。\n',
            '听了可别吓坏了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640260444V#221F把束缚我的无理规定\n',
            '终于解除了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010260445V#1004F无理规定解除了……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_34F7',
    )

    ChrTalk(
        0x0106,
        (
            '#0050260446V#052F#5P难不成\n',
            '是禁足处分解除了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_352C')

    def _loc_34F7(): pass

    label('loc_34F7')

    ChrTalk(
        0x0103,
        (
            '#0030260447V#023F#5P难不成\n',
            '是禁足处分解除了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_352C(): pass

    label('loc_352C')

    ChrTalk(
        0x0011,
        (
            '#0660260448V#720F#4P是的，今天早晨\n',
            '收到了陛下的联络。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660260449V说要离开离宫，\n',
            '返回格兰赛尔城。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_35D7',
    )

    ChrTalk(
        0x0106,
        (
            '#0050260450V#051F#5P哎呀哎呀……\n',
            '真是老好人的婆婆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3608')

    def _loc_35D7(): pass

    label('loc_35D7')

    ChrTalk(
        0x0103,
        (
            '#0030260451V#027F#5P哎呀呀……\n',
            '相当简单呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3608(): pass

    label('loc_3608')

    ChrTalk(
        0x0101,
        (
            '#0010260452V#1011F哦～不过\n',
            '也好吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010260453V#1001F不要再次被利用\n',
            '要好好把持住自己哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0640260454V#223F#6P什么……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010260455V#1006F嗯～还是要把生活态度\n',
            '重新端正一下比较好吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010260456V公爵先生啊\n',
            '实在是自由散漫惯了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010260457V推荐你做点运动哦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00F7, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x0010, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x0011, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x0107, 0x00000000, 1700, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x012F, 0x00000000, 1700, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x0012, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x0013, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x0014, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1500)

    OP_63(0x00F7)
    OP_63(0x0010)
    OP_63(0x0011)
    OP_63(0x0107)
    OP_63(0x012F)
    OP_63(0x0012)
    OP_63(0x0013)
    OP_63(0x0014)

    ChrTalk(
        0x0101,
        (
            '#0010260458V#1015F咦？\n',
            '我说了什么奇怪的话？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0660260459V#720F#4P不……正如艾丝蒂尔大人\n',
            '说的一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0011, 270, 400)
    Sleep(500)

    ChrTalk(
        0x0011,
        (
            '#0660260460V#722F#2P如果阁下自己\n',
            '把持得住，也不会被\n',
            '理查德上校所利用……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660260461V我菲利普，希望\n',
            '就此再度进言……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0640260462V#226F#6P哎，说教够了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0010, 180, 600)

    ChrTalk(
        0x0010,
        (
            '#0640260463V#224F#5P够了，这个地方\n',
            '我一秒钟也不想再待了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640260464V赶紧去王都！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#2440260465V#2P哦哦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010260466V#1004F啊？\n',
            '不用陪同吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0010, 0, 600)

    ChrTalk(
        0x0010,
        (
            '#0640260467V#224F#6P不要！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640260468V走了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0012, 0x01, 0x00, func_1D_4080)
    Sleep(50)

    CreateThread(0x0013, 0x01, 0x00, func_1B_401E)
    CreateThread(0x0014, 0x01, 0x00, func_1C_4053)

    @scena.Lambda('lambda_39E7')
    def lambda_39E7():
        ChrTurnDirection(0x00FE, 0x0010, 400)
        Yield()

        Jump('lambda_39E7')

    DispatchAsync2(0x0011, 0x0002, lambda_39E7)

    ChrSetDirection(0x0010, 180, 600)
    ChrWalkTo(0x0010, -220, 0, 35000, 3000, 0x00)
    TerminateThread(0x0011, 0x02)
    ChrSetDirection(0x0011, 270, 400)
    ChrSetDirection(0x0011, 0, 400)

    ChrTalk(
        0x0011,
        (
            '#0660260469V#720F艾丝蒂尔小姐、每次\n',
            '都麻烦您真是感激不尽。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660260470V该如何感谢才好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010260471V#1016F啊哈哈，不用啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010260472V#1006F不过，菲利普先生\n',
            '偶尔也得好好训训他。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010260473V就是因为没人训他\n',
            '才变成那样不是吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0660260474V#721F哎……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010260475V#1006F我想他本性也不坏,\n',
            '只要有心还是能改过的啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010260476V需要的就是一个契机吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0660260477V#722F艾丝蒂尔小姐……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660260478V您的话，我菲利普，\n',
            '将铭刻在心……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0640260479V#5P菲利普！\n',
            '在干什么！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640260480V再磨磨蹭蹭\n',
            '我就丢下你不管了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0011, 270, 600)
    ChrSetDirection(0x0011, 180, 600)

    ChrTalk(
        0x0011,
        (
            '#0660260481V#721F#5P是、是，这就来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0011, 270, 600)
    ChrSetDirection(0x0011, 0, 600)

    ChrTalk(
        0x0011,
        (
            '#0660260482V#720F那么各位……\n',
            '我就告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0011, 270, 600)
    ChrSetDirection(0x0011, 180, 600)
    ChrSetFlags(0x0010, 0x0080)
    ChrSetFlags(0x0012, 0x0080)
    ChrSetFlags(0x0013, 0x0080)
    ChrSetFlags(0x0014, 0x0080)

    @scena.Lambda('lambda_3CDB')
    def lambda_3CDB():
        CameraMove(-370, 0, 43300, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_3CDB)

    ChrWalkTo(0x0011, -220, 0, 35000, 3000, 0x00)
    ChrSetFlags(0x0011, 0x0080)
    Sleep(500)

    CameraMove(-600, 250, 47270, 1600)

    ChrTalk(
        0x0101,
        (
            '#0010260483V#1015F嗯～虽然觉得还是\n',
            '陪着一起会比较好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00F7, 0x0101, 400)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_3DC5',
    )

    ChrTalk(
        0x0106,
        (
            '#0050260484V#051F……怎么说呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050260485V说实话，你这种地方\n',
            '还真是学不来啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3E15')

    def _loc_3DC5(): pass

    label('loc_3DC5')

    ChrTalk(
        0x0103,
        (
            '#0030260486V#021F……艾丝蒂尔你啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030260487V不愧是流着\n',
            '老师的血液呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3E15(): pass

    label('loc_3E15')

    ChrTurnDirection(0x0101, 0x00F7, 400)

    ChrTalk(
        0x0101,
        (
            '#0010260488V#1004F#2P咦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070260489V#067F嘿嘿嘿……\n',
            '还是姐姐厉害啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x012F,
        (
            '#0220260490V#268F虽然初次见面\n',
            '就有这种感觉……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220260491V艾丝蒂尔啊，真是个\n',
            '大好人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(1000)

    ChrSetDirection(0x0101, 0, 400)

    ChrTalk(
        0x0101,
        (
            '#0010260492V#1015F#6P好人……为什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_3F76',
    )

    ChrTalk(
        0x0106,
        (
            '#0050260493V#051F啊～不懂的话\n',
            '就保持这样好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050260494V总之回王都去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3FCA')

    def _loc_3F76(): pass

    label('loc_3F76')

    ChrTalk(
        0x0103,
        (
            '#0030260495V#027F呵呵，不懂的话\n',
            '就保持这样好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030260496V总之回王都去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3FCA(): pass

    label('loc_3FCA')

    SetScenaFlags(ScenaFlag(0x02C5, 4, 0x162C))
    TerminateThread(0x0013, 0x01)
    TerminateThread(0x0014, 0x01)
    ChrSetPos(0x0013, -1960, 0, 19780, 180)
    ChrSetPos(0x0014, 1960, 0, 19780, 180)
    ChrClearFlags(0x0013, 0x0080)
    ChrClearFlags(0x0014, 0x0080)
    OP_4B(0x0013, 255)
    OP_4B(0x0014, 255)
    ChrClearFlags(0x0015, 0x0080)
    ChrClearFlags(0x0016, 0x0080)
    OP_4B(0x0015, 255)
    OP_4B(0x0016, 255)
    EventEnd(0x00)

    Return()

# id: 0x001B offset: 0x401E
@scena.Code('func_1B_401E')
def func_1B_401E():
    ChrMoveTo(0x00FE, -1770, 0, 42640, 2500, 0x00)
    ChrSetDirection(0x00FE, 90, 500)
    Sleep(2000)

    ChrWalkTo(0x00FE, -1220, 0, 37000, 2500, 0x00)

    Return()

# id: 0x001C offset: 0x4053
@scena.Code('func_1C_4053')
def func_1C_4053():
    Sleep(1000)

    ChrSetDirection(0x00FE, 270, 500)
    Sleep(1500)

    ChrSetDirection(0x00FE, 180, 500)
    ChrWalkTo(0x00FE, 780, 0, 37000, 2500, 0x00)

    Return()

# id: 0x001D offset: 0x4080
@scena.Code('func_1D_4080')
def func_1D_4080():
    ChrMoveTo(0x00FE, 20, 0, 41640, 2500, 0x00)
    ChrSetDirection(0x00FE, 270, 500)
    ChrMoveTo(0x00FE, 690, 0, 41640, 2500, 0x00)
    Sleep(1000)

    ChrSetDirection(0x00FE, 180, 500)
    ChrWalkTo(0x00FE, -220, 0, 36000, 2500, 0x00)

    Return()

# id: 0x001E offset: 0x40D0
@scena.Code('func_1E_40D0')
def func_1E_40D0():
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
        (0x00000000, 'loc_414A'),
        (0x00000001, 'loc_4150'),
        (-1, 'loc_4156'),
    )

    def _loc_414A(): pass

    label('loc_414A')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_4156')

    def _loc_4150(): pass

    label('loc_4150')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_4156')

    def _loc_4156(): pass

    label('loc_4156')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_4164',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    Jump('loc_4168')

    def _loc_4164(): pass

    label('loc_4164')

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    def _loc_4168(): pass

    label('loc_4168')

    Return()

# id: 0x001F offset: 0x4169
@scena.Code('func_1F_4169')
def func_1F_4169():
    MapClearFlags(0x00000001)
    CameraMove(-11230, 0, -25420, 0)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_41AC',
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

    Jump('loc_41CA')

    def _loc_41AC(): pass

    label('loc_41AC')

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

    def _loc_41CA(): pass

    label('loc_41CA')

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

# id: 0x0020 offset: 0x41EA
@scena.Code('func_20_41EA')
def func_20_41EA():
    EventBegin(0x01)

    ChrTalk(
        0x0101,
        (
            '#0011860001V#1001F这里好像可以钓上什么来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '钓鱼吗？',
            (TxtCtl.SetColor, 0x0),
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
        1,
        (
            TXT(0x00, '钓鱼\n'),
            TXT(0x01, '离开\n'),
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

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_42D2',
    )

    @scena.Lambda('lambda_426D')
    def lambda_426D():
        CameraSetDistance(2800, 1500)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_426D)

    @scena.Lambda('lambda_427D')
    def lambda_427D():
        OP_6C(315000, 1500)

        ExitThread()

    DispatchAsync(0x0001, 0x0002, lambda_427D)

    WaitForThreadExit(0x0001, 0x0001)

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.GetChrWork, 0x101, 0x28),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0101,
        0x28,
        (
            (Expr.PushLong, 0x1),
            Expr.Not,
            Expr.And2,
            Expr.Return,
        ),
    )

    OP_C0(0x0E, 0x0000002F, 0xFFFFC216, 0x00000000, 0x0000C152, 0x00000000, 0xFFFFC284, 0xFFFFFAEC, 0x0000CA44)

    ExecExpressionWithValue(
        0x0101,
        0x28,
        (
            (Expr.PushReg, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_0D()
    EventEnd(0x01)

    Jump('loc_42E1')

    def _loc_42D2(): pass

    label('loc_42D2')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_42E1',
    )

    EventEnd(0x01)

    def _loc_42E1(): pass

    label('loc_42E1')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
