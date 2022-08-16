import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T3300_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3300   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'T3300.x'
    header.mapIndex       = 1
    header.bgm            = 16
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT01/T3300._SN', 'ED6_DT01/T3300_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
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
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01760._CH', 'ED6_DT07/CH01760P._CP'),
        ('ED6_DT07/CH01530._CH', 'ED6_DT07/CH01530P._CP'),
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
        ('ED6_DT07/CH01300._CH', 'ED6_DT07/CH01300P._CP'),
        ('ED6_DT07/CH01310._CH', 'ED6_DT07/CH01310P._CP'),
        ('ED6_DT07/CH01300._CH', 'ED6_DT07/CH01300P._CP'),
        ('ED6_DT07/CH01270._CH', 'ED6_DT07/CH01270P._CP'),
        ('ED6_DT07/CH01720._CH', 'ED6_DT07/CH01720P._CP'),
    ]

# id: 0x10001 offset: 0xF2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '加雷利',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            name                = '王',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '布鲁诺',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            name                = '士兵布拉姆',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '士兵赫宁',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '派斯队长',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '格温副长',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '伦法',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            name                = '鸡',
            x                   = 44200,
            z                   = 0,
            y                   = 18540,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0005,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '鸡',
            x                   = 44200,
            z                   = 0,
            y                   = 18540,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0005,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '鸡',
            x                   = 44200,
            z                   = 0,
            y                   = 18540,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0006,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '鸡',
            x                   = 44200,
            z                   = 0,
            y                   = 18540,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0006,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '托兰特平原道方向',
            x                   = 1990,
            z                   = -500,
            y                   = -280,
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

# id: 0x10002 offset: 0x292
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x292
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x292
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 8039,
            triggerZ            = 0,
            triggerY            = 21240,
            triggerRange        = 1500,
            actorX              = 8039,
            actorZ              = 2000,
            actorY              = 21240,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0011,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x2B6
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_2C0',
    )

    Jump('loc_3B6')

    def _loc_2C0(): pass

    label('loc_2C0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_2FD',
    )

    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, 11760, 20, 31780, 236)
    CreateThread(0x0008, 0x00, 0x00, func_03_5BE)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0009, 7490, -60, 24130, 273)

    Jump('loc_3B6')

    def _loc_2FD(): pass

    label('loc_2FD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_307',
    )

    Jump('loc_3B6')

    def _loc_307(): pass

    label('loc_307')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_311',
    )

    Jump('loc_3B6')

    def _loc_311(): pass

    label('loc_311')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_331',
    )

    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, 11890, 0, 41360, 226)

    Jump('loc_3B6')

    def _loc_331(): pass

    label('loc_331')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_351',
    )

    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, 11890, 0, 41360, 226)

    Jump('loc_3B6')

    def _loc_351(): pass

    label('loc_351')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_391',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0029, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_38E',
    )

    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0009, 13100, 0, 38170, 53)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, 16420, 0, 38700, 351)

    def _loc_38E(): pass

    label('loc_38E')

    Jump('loc_3B6')

    def _loc_391(): pass

    label('loc_391')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_39B',
    )

    Jump('loc_3B6')

    def _loc_39B(): pass

    label('loc_39B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_3A5',
    )

    Jump('loc_3B6')

    def _loc_3A5(): pass

    label('loc_3A5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Return,
        ),
        'loc_3AF',
    )

    Jump('loc_3B6')

    def _loc_3AF(): pass

    label('loc_3AF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_3B6',
    )

    def _loc_3B6(): pass

    label('loc_3B6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_3FC',
    )

    ChrClearFlags(0x000B, 0x0080)
    ChrSetPos(0x000B, 1000, 0, 48690, 180)
    ChrSetFlags(0x000B, 0x0010)
    TerminateThread(0x000B, 0xFF)
    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x000E, -7370, 5500, 49600, 74)
    CreateThread(0x000E, 0x00, 0x00, func_04_5E2)

    Jump('loc_53E')

    def _loc_3FC(): pass

    label('loc_3FC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_41C',
    )

    ChrClearFlags(0x000B, 0x0080)
    ChrSetPos(0x000B, 1000, 0, 48690, 180)

    Jump('loc_53E')

    def _loc_41C(): pass

    label('loc_41C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_478',
    )

    ChrClearFlags(0x000C, 0x0080)
    ChrSetPos(0x000C, 6340, 0, 48700, 159)
    ChrClearFlags(0x000B, 0x0080)
    ChrSetPos(0x000B, 1000, 0, 48690, 180)
    ChrSetFlags(0x000B, 0x0010)
    TerminateThread(0x000B, 0xFF)
    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x000E, -7370, 5500, 49600, 74)
    CreateThread(0x000E, 0x00, 0x00, func_04_5E2)

    Jump('loc_53E')

    def _loc_478(): pass

    label('loc_478')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_4BE',
    )

    ChrClearFlags(0x000B, 0x0080)
    ChrSetPos(0x000B, 1000, 0, 48690, 180)
    ChrSetFlags(0x000B, 0x0010)
    TerminateThread(0x000B, 0xFF)
    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x000E, -7370, 5500, 49600, 74)
    CreateThread(0x000E, 0x00, 0x00, func_04_5E2)

    Jump('loc_53E')

    def _loc_4BE(): pass

    label('loc_4BE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_4FB',
    )

    ChrClearFlags(0x000B, 0x0080)
    ChrSetPos(0x000B, 1000, 0, 48690, 180)

    If(
        (
            (Expr.Eval, "OP_29(0x0031, 0x00, 0x08)"),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x0031, 0x01, 0x8000)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4F8',
    )

    TerminateThread(0x000B, 0xFF)
    ChrSetFlags(0x000B, 0x0010)

    def _loc_4F8(): pass

    label('loc_4F8')

    Jump('loc_53E')

    def _loc_4FB(): pass

    label('loc_4FB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_53E',
    )

    ChrClearFlags(0x000B, 0x0080)
    ChrSetPos(0x000B, 790, 0, 48280, 180)
    ChrSetFlags(0x000B, 0x0010)
    TerminateThread(0x000B, 0xFF)
    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x000E, -7370, 5500, 49600, 74)
    CreateThread(0x000E, 0x00, 0x00, func_04_5E2)

    def _loc_53E(): pass

    label('loc_53E')

    Return()

# id: 0x0001 offset: 0x53F
@scena.Code('func_01_53F')
def func_01_53F():
    OP_16(0x02, 4000, -124000, -84000, 196693)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_560',
    )

    OP_71(0x0004, 0x0004)

    Jump('loc_593')

    def _loc_560(): pass

    label('loc_560')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_56A',
    )

    Jump('loc_593')

    def _loc_56A(): pass

    label('loc_56A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_574',
    )

    Jump('loc_593')

    def _loc_574(): pass

    label('loc_574')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_58E',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0029, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_58B',
    )

    OP_71(0x0004, 0x0004)

    def _loc_58B(): pass

    label('loc_58B')

    Jump('loc_593')

    def _loc_58E(): pass

    label('loc_58E')

    OP_71(0x0004, 0x0004)

    def _loc_593(): pass

    label('loc_593')

    If(
        (
            (Expr.GetChrWork, 0x101, 0x1E),
            (Expr.PushLong, 0x11C),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5A7',
    )

    OP_28(0x002A, 0x01, 0x1000)

    def _loc_5A7(): pass

    label('loc_5A7')

    Return()

# id: 0x0002 offset: 0x5A8
@scena.Code('func_02_5A8')
def func_02_5A8():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5BD',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_5A8')

    def _loc_5BD(): pass

    label('loc_5BD')

    Return()

# id: 0x0003 offset: 0x5BE
@scena.Code('func_03_5BE')
def func_03_5BE():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5E1',
    )

    OP_8D(0x00FE, 8640, 35670, 14490, 27640, 2000)

    Jump('func_03_5BE')

    def _loc_5E1(): pass

    label('loc_5E1')

    Return()

# id: 0x0004 offset: 0x5E2
@scena.Code('func_04_5E2')
def func_04_5E2():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_605',
    )

    OP_8D(0x00FE, -9410, 54290, -4840, 47630, 2000)

    Jump('func_04_5E2')

    def _loc_605(): pass

    label('loc_605')

    Return()

# id: 0x0005 offset: 0x606
@scena.Code('func_05_606')
def func_05_606():
    ChrSetFlags(0x00FE, 0x0040)
    OP_8D(0x00FE, -4320, 30420, 16309, 38200, 0)

    ExecExpressionWithValue(
        0x00FE,
        0x04,
        (
            Expr.Rand,
            (Expr.PushLong, 0x168),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_62F(): pass

    label('loc_62F')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_753',
    )

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x1),
            (Expr.PushLong, 0xBB8),
            Expr.Add,
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Gtr,
            (Expr.GetChrWork, 0xFE, 0x1),
            (Expr.PushLong, 0xBB8),
            Expr.Sub,
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Lss,
            Expr.Nez64,
            (Expr.GetChrWork, 0xFE, 0x3),
            (Expr.PushLong, 0xBB8),
            Expr.Add,
            (Expr.GetChrWork, 0x0, 0x3),
            Expr.Gtr,
            Expr.Nez64,
            (Expr.GetChrWork, 0xFE, 0x3),
            (Expr.PushLong, 0xBB8),
            Expr.Sub,
            (Expr.GetChrWork, 0x0, 0x3),
            Expr.Lss,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_718',
    )

    If(
        (
            (Expr.PushLong, 0x10E0),
            Expr.Neg,
            (Expr.PushLong, 0x3E8),
            Expr.Add,
            (Expr.GetChrWork, 0xFE, 0x1),
            Expr.Lss,
            (Expr.PushLong, 0x76D4),
            (Expr.PushLong, 0x3E8),
            Expr.Add,
            (Expr.GetChrWork, 0xFE, 0x3),
            Expr.Lss,
            Expr.Nez64,
            (Expr.PushLong, 0x3FB5),
            (Expr.PushLong, 0x3E8),
            Expr.Sub,
            (Expr.GetChrWork, 0xFE, 0x1),
            Expr.Gtr,
            Expr.Nez64,
            (Expr.PushLong, 0x9538),
            (Expr.PushLong, 0x3E8),
            Expr.Sub,
            (Expr.GetChrWork, 0xFE, 0x3),
            Expr.Gtr,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_6ED',
    )

    ChrSetFlags(0x00FE, 0x0020)
    ChrTurnDirection(0x00FE, 0x0000, 0)
    ChrClearFlags(0x00FE, 0x0020)

    @scena.Lambda('lambda_06DA')
    def lambda_06DA():
        OP_94(0x00, 0x00FE, 0x00B4, 0x0000012C, 0x00001770, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_06DA)

    Jump('loc_710')

    def _loc_6ED(): pass

    label('loc_6ED')

    @scena.Lambda('lambda_06F3')
    def lambda_06F3():
        OP_8D(0x00FE, -4320, 30420, 16309, 38200, 6000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_06F3)

    Sleep(200)

    def _loc_710(): pass

    label('loc_710')

    Sleep(30)

    Jump('loc_750')

    def _loc_718(): pass

    label('loc_718')

    Sleep(50)

    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x28),
            Expr.Mod,
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_750',
    )

    TerminateThread(0x00FE, 0x02)

    @scena.Lambda('lambda_0738')
    def lambda_0738():
        OP_8D(0x00FE, -4320, 30420, 16309, 38200, 1500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_0738)

    def _loc_750(): pass

    label('loc_750')

    Jump('loc_62F')

    def _loc_753(): pass

    label('loc_753')

    Return()

# id: 0x0006 offset: 0x754
@scena.Code('func_06_754')
def func_06_754():
    ChrSetFlags(0x00FE, 0x0040)
    OP_8D(0x00FE, -780, 24910, 8900, 46240, 0)

    ExecExpressionWithValue(
        0x00FE,
        0x04,
        (
            Expr.Rand,
            (Expr.PushLong, 0x168),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_77D(): pass

    label('loc_77D')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_8A1',
    )

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x1),
            (Expr.PushLong, 0xBB8),
            Expr.Add,
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Gtr,
            (Expr.GetChrWork, 0xFE, 0x1),
            (Expr.PushLong, 0xBB8),
            Expr.Sub,
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Lss,
            Expr.Nez64,
            (Expr.GetChrWork, 0xFE, 0x3),
            (Expr.PushLong, 0xBB8),
            Expr.Add,
            (Expr.GetChrWork, 0x0, 0x3),
            Expr.Gtr,
            Expr.Nez64,
            (Expr.GetChrWork, 0xFE, 0x3),
            (Expr.PushLong, 0xBB8),
            Expr.Sub,
            (Expr.GetChrWork, 0x0, 0x3),
            Expr.Lss,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_866',
    )

    If(
        (
            (Expr.PushLong, 0x30C),
            Expr.Neg,
            (Expr.PushLong, 0x3E8),
            Expr.Add,
            (Expr.GetChrWork, 0xFE, 0x1),
            Expr.Lss,
            (Expr.PushLong, 0x614E),
            (Expr.PushLong, 0x3E8),
            Expr.Add,
            (Expr.GetChrWork, 0xFE, 0x3),
            Expr.Lss,
            Expr.Nez64,
            (Expr.PushLong, 0x22C4),
            (Expr.PushLong, 0x3E8),
            Expr.Sub,
            (Expr.GetChrWork, 0xFE, 0x1),
            Expr.Gtr,
            Expr.Nez64,
            (Expr.PushLong, 0xB4A0),
            (Expr.PushLong, 0x3E8),
            Expr.Sub,
            (Expr.GetChrWork, 0xFE, 0x3),
            Expr.Gtr,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_83B',
    )

    ChrSetFlags(0x00FE, 0x0020)
    ChrTurnDirection(0x00FE, 0x0000, 0)
    ChrClearFlags(0x00FE, 0x0020)

    @scena.Lambda('lambda_0828')
    def lambda_0828():
        OP_94(0x00, 0x00FE, 0x00B4, 0x0000012C, 0x00001770, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_0828)

    Jump('loc_85E')

    def _loc_83B(): pass

    label('loc_83B')

    @scena.Lambda('lambda_0841')
    def lambda_0841():
        OP_8D(0x00FE, -780, 24910, 8900, 46240, 6000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_0841)

    Sleep(200)

    def _loc_85E(): pass

    label('loc_85E')

    Sleep(30)

    Jump('loc_89E')

    def _loc_866(): pass

    label('loc_866')

    Sleep(50)

    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x28),
            Expr.Mod,
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_89E',
    )

    TerminateThread(0x00FE, 0x02)

    @scena.Lambda('lambda_0886')
    def lambda_0886():
        OP_8D(0x00FE, -780, 24910, 8900, 46240, 1500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_0886)

    def _loc_89E(): pass

    label('loc_89E')

    Jump('loc_77D')

    def _loc_8A1(): pass

    label('loc_8A1')

    Return()

# id: 0x0007 offset: 0x8A2
@scena.Code('func_07_8A2')
def func_07_8A2():
    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_92C',
    )

    CreateThread(0x00FE, 0x02, 0x00, func_08_92D)
    PlaySE(401, 0x00, 0x64)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Ez,
            Expr.Rand,
            (Expr.PushLong, 0xA),
            Expr.Mod,
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_92C',
    )

    If(
        (
            (Expr.Eval, "AddItem(0x038B, 1)"),
            Expr.Return,
        ),
        'loc_92C',
    )

    TalkBegin(0x00FE)
    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '新鲜鸡蛋',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FE)

    def _loc_92C(): pass

    label('loc_92C')

    Return()

# id: 0x0008 offset: 0x92D
@scena.Code('func_08_92D')
def func_08_92D():
    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_948',
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    Yield()

    Jump('func_08_92D')

    def _loc_948(): pass

    label('loc_948')

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0009 offset: 0x953
@scena.Code('func_09_953')
def func_09_953():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_9A9',
    )

    ChrTalk(
        0x00FE,
        (
            '#2050180337V那我就由衷地\n',
            '拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2050180354V真是期待啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1342')

    def _loc_9A9(): pass

    label('loc_9A9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_ADF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_9EA',
    )

    OP_62(0x00FE, 0x00000000, 2000, 0x1C, 0x21, 0x000000FA, 0x00)
    Sleep(800)

    ChrTalk(
        0x00FE,
        (
            '……………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_63(0x00FE)

    Jump('loc_ADC')

    def _loc_9EA(): pass

    label('loc_9EA')

    If(
        (
            (Expr.Eval, "OP_29(0x0031, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A66',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))
    OP_62(0x00FE, 0x00000000, 2000, 0x1C, 0x21, 0x000000FA, 0x00)
    Sleep(800)

    ChrTalk(
        0x00FE,
        (
            '……………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……哦哦，菲……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '原……原谅……\n',
            '……我……………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_63(0x00FE)

    Jump('loc_ADC')

    def _loc_A66(): pass

    label('loc_A66')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))
    OP_62(0x00FE, 0x00000000, 2000, 0x1C, 0x21, 0x000000FA, 0x00)
    Sleep(800)

    ChrTalk(
        0x00FE,
        (
            '……………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……哦哦，菲……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我太高兴了……\n',
            '……明白……我的心意……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_63(0x00FE)

    def _loc_ADC(): pass

    label('loc_ADC')

    Jump('loc_1342')

    def _loc_ADF(): pass

    label('loc_ADF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_E79',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B2, 1, 0x591)),
            Expr.Return,
        ),
        'loc_B56',
    )

    ChrTalk(
        0x00FE,
        (
            '呵呵，\n',
            '菲已经读了我的信吧…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……总、总觉得\n',
            '紧张得脖子都快僵硬了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼啊啊～啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E76')

    def _loc_B56(): pass

    label('loc_B56')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_BE3',
    )

    ChrTalk(
        0x00FE,
        (
            '#2050180365V一想再过不久， \n',
            '菲就要看我的信……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2050180366V就、就紧张得\n',
            '脖子都要僵硬了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2050180367V呼啊啊～啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E76')

    def _loc_BE3(): pass

    label('loc_BE3')

    If(
        (
            (Expr.Eval, "OP_29(0x0031, 0x00, 0x08)"),
            Expr.Return,
        ),
        'loc_DE3',
    )

    ChrTalk(
        0x00FE,
        (
            '#2050180368V啊，是你们……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2050180369V怎、怎么样？\n',
            '信、信送到了没有？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x0031, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_D65',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0031, 0x01, 0x0020)"),
            (Expr.Eval, "OP_29(0x0031, 0x01, 0x0040)"),
            Expr.Or,
            (Expr.Eval, "OP_29(0x0031, 0x01, 0x0080)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_CAE',
    )

    ChrTalk(
        0x0101,
        (
            '#0010180370V#001F嗯，送到了哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180371V当然啦，还有礼物。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CD3')

    def _loc_CAE(): pass

    label('loc_CAE')

    ChrTalk(
        0x0101,
        (
            '#0010180372V#001F嗯，送到了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_CD3(): pass

    label('loc_CD3')

    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#2050180373V是、是吗。\n',
            '谢谢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2050180374V那、那么\n',
            '她现在应该在看了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2050180375V……为、为什么\n',
            '感觉这么紧张啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x00B2, 1, 0x591))

    Jump('loc_DE0')

    def _loc_D65(): pass

    label('loc_D65')

    ChrTalk(
        0x0101,
        (
            '#0010180376V#000F啊，\n',
            '还没有送去呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#2050180377V呼，是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2050180378V那么，\n',
            '就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))
    def _loc_DE0(): pass

    label('loc_DE0')

    Jump('loc_E76')

    def _loc_DE3(): pass

    label('loc_DE3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_E26',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，还是困啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天也早点睡吧。\n',
            '呼啊啊啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E76')

    def _loc_E26(): pass

    label('loc_E26')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '唔，好奇怪啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总觉得\n',
            '刚才周围一直很乱……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '正好把我给吵醒了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E76(): pass

    label('loc_E76')

    Jump('loc_1342')

    def _loc_E79(): pass

    label('loc_E79')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_ED1',
    )

    OP_62(0x00FE, 0x00000000, 2000, 0x1C, 0x21, 0x000000FA, 0x00)
    Sleep(800)

    ChrTalk(
        0x00FE,
        (
            '……………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            'ＺＺＺ～……ＺＺＺ～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_63(0x00FE)

    Jump('loc_1342')

    def _loc_ED1(): pass

    label('loc_ED1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_F3E',
    )

    OP_62(0x00FE, 0x00000000, 2000, 0x1C, 0x21, 0x000000FA, 0x00)
    Sleep(800)

    ChrTalk(
        0x00FE,
        (
            '……………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……嗯、嗯嗯～嗯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '菲……\n',
            '对……不起……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_63(0x00FE)

    Jump('loc_1342')

    def _loc_F3E(): pass

    label('loc_F3E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_129B',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0031, 0x00, 0x08)"),
            Expr.Return,
        ),
        'loc_1294',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0031, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_1138',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B2, 1, 0x591)),
            Expr.Return,
        ),
        'loc_FC7',
    )

    ChrTalk(
        0x00FE,
        (
            '现在菲说不定\n',
            '正在看我的信呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……总、总觉得\n',
            '紧张得脖子都快僵硬了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼啊啊～啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1135')

    def _loc_FC7(): pass

    label('loc_FC7')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))
    SetScenaFlags(ScenaFlag(0x00B2, 1, 0x591))

    ChrTalk(
        0x00FE,
        (
            '#2050180368V啊，是你们……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2050180369V怎、怎么样？\n',
            '信、信送到了没有？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x0031, 0x01, 0x0020)"),
            (Expr.Eval, "OP_29(0x0031, 0x01, 0x0040)"),
            Expr.Or,
            (Expr.Eval, "OP_29(0x0031, 0x01, 0x0080)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_1084',
    )

    ChrTalk(
        0x0101,
        (
            '#0010180370V#001F嗯，送到了哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180371V当然啦，还有礼物。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10A9')

    def _loc_1084(): pass

    label('loc_1084')

    ChrTalk(
        0x0101,
        (
            '#0010180372V#001F嗯，送到了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_10A9(): pass

    label('loc_10A9')

    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#2050180373V是、是吗。\n',
            '谢谢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2050180374V那、那么\n',
            '她现在应该在看了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2050180375V……为、为什么\n',
            '感觉这么紧张啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1135(): pass

    label('loc_1135')

    Jump('loc_1291')

    def _loc_1138(): pass

    label('loc_1138')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_11C5',
    )

    ChrTalk(
        0x00FE,
        (
            '#2050180365V一想再过不久， \n',
            '菲就要看我的信……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2050180366V就、就紧张得\n',
            '脖子都要僵硬了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2050180367V呼啊啊～啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1291')

    def _loc_11C5(): pass

    label('loc_11C5')

    ChrTalk(
        0x00FE,
        (
            '#2050180368V啊，是你们……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2050180369V怎、怎么样？\n',
            '信、信送到了没有？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180405V#000F啊，\n',
            '还没有送去呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#2050180377V呼，是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2050180378V那么，\n',
            '就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    def _loc_1291(): pass

    label('loc_1291')

    Jump('loc_1298')

    def _loc_1294(): pass

    label('loc_1294')

    Call(1, 0x0002)
    def _loc_1298(): pass

    label('loc_1298')

    Jump('loc_1342')

    def _loc_129B(): pass

    label('loc_129B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_1342',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_12DC',
    )

    OP_62(0x00FE, 0x00000000, 2000, 0x1C, 0x21, 0x000000FA, 0x00)
    Sleep(800)

    ChrTalk(
        0x00FE,
        (
            '……………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_63(0x00FE)

    Jump('loc_1342')

    def _loc_12DC(): pass

    label('loc_12DC')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))
    OP_62(0x00FE, 0x00000000, 2000, 0x1C, 0x21, 0x000000FA, 0x00)
    Sleep(800)

    ChrTalk(
        0x00FE,
        (
            '……………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……嗯嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没有～……\n',
            '……异常…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_63(0x00FE)

    def _loc_1342(): pass

    label('loc_1342')

    TalkEnd(0x00FE)

    Return()

# id: 0x000A offset: 0x1346
@scena.Code('func_0A_1346')
def func_0A_1346():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_1401',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_13AA',
    )

    ChrTalk(
        0x00FE,
        (
            '……哈，\n',
            '你们可别理旁边那家伙哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那个家伙\n',
            '可是这个守备队的大笑料呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1401')

    def _loc_13AA(): pass

    label('loc_13AA')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '现在正在进行盘查。\n',
            '因为蔡斯出了事嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在的出入境检查\n',
            '比平时更加严格哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1401(): pass

    label('loc_1401')

    TalkEnd(0x00FE)

    Return()

# id: 0x000B offset: 0x1405
@scena.Code('func_0B_1405')
def func_0B_1405():
    TalkBegin(0x00FE)
    TalkEnd(0x00FE)

    Return()

# id: 0x000C offset: 0x140C
@scena.Code('func_0C_140C')
def func_0C_140C():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_14FD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_1478',
    )

    ChrTalk(
        0x00FE,
        (
            '还是没有找到\n',
            '袭击工房犯人的下落。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '事到如今，\n',
            '下令再次盘查根本就没有意义了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_14FA')

    def _loc_1478(): pass

    label('loc_1478')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '那些工房袭击犯\n',
            '一点下落也没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这也是理所当然的结果吧。\n',
            '因为盘查被解除了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '也许那些犯人\n',
            '早已经逃亡到国外去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_14FA(): pass

    label('loc_14FA')

    Jump('loc_18CE')

    def _loc_14FD(): pass

    label('loc_14FD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_1623',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_156E',
    )

    ChrTalk(
        0x00FE,
        (
            '现在，\n',
            '这个沃尔费堡垒也实行了严格的盘查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在事件的真相明了之前\n',
            '这个态势还将维持下去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1620')

    def _loc_156E(): pass

    label('loc_156E')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '之前收到了紧急的联络。\n',
            '现在这个堡垒也进入了警戒状态。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '从已知的线索来判断，\n',
            '蔡斯事件应该是训练有素的犯罪者所为。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……说不定，\n',
            '也有可能是来自他国的不速之客所为。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1620(): pass

    label('loc_1620')

    Jump('loc_18CE')

    def _loc_1623(): pass

    label('loc_1623')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_178F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_16D6',
    )

    ChrTalk(
        0x00FE,
        (
            '如果情势有变化，\n',
            '现在与我们保持和平的共和国\n',
            '可能也会对我们虎视眈眈。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对他们来说，\n',
            '王国的七耀石资源非常诱人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以我认为守卫国境\n',
            '是非常重要的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_178C')

    def _loc_16D6(): pass

    label('loc_16D6')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '乍一看，卡尔瓦德共和国\n',
            '好像是利贝尔的友好的盟国……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '其实站在他们的角度来看，\n',
            '是因为有埃雷波尼亚帝国在\n',
            '他们才愿意和王国合作的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '也就是所谓的『敌人的敌人就是朋友』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_178C(): pass

    label('loc_178C')

    Jump('loc_18CE')

    def _loc_178F(): pass

    label('loc_178F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_18CE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_1833',
    )

    ChrTalk(
        0x00FE,
        (
            '有人打瞌睡有人偷懒……\n',
            '这里的守备队还真是过分啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这个样子下去\n',
            '万一发生什么事情怎么应对得了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '至少我自己要\n',
            '尽职地完成本分工作啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_18CE')

    def _loc_1833(): pass

    label('loc_1833')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '真是的……\n',
            '这里的守备队还真是过分啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有人打瞌睡有人偷懒……\n',
            '士兵们随心所欲，\n',
            '队长也都装没看见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，至少我自己要\n',
            '尽职地完成本分工作啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_18CE(): pass

    label('loc_18CE')

    TalkEnd(0x00FE)

    Return()

# id: 0x000D offset: 0x18D2
@scena.Code('func_0D_18D2')
def func_0D_18D2():
    TalkBegin(0x00FE)
    TalkEnd(0x00FE)

    Return()

# id: 0x000E offset: 0x18D9
@scena.Code('func_0E_18D9')
def func_0E_18D9():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_1AC6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00BA, 0, 0x5D0)),
            Expr.Return,
        ),
        'loc_1975',
    )

    ChrTalk(
        0x00FE,
        (
            '说起来，\n',
            '怎么会突然要检查啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果能在交接货物\n',
            '完成之后进行就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '商品要是不能\n',
            '运到共和国那边，\n',
            '我不就白来了一趟吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AC3')

    def _loc_1975(): pass

    label('loc_1975')

    ChrTalk(
        0x00FE,
        (
            '好像因为在蔡斯发生了事件，\n',
            '这里开始对过往行人进行盘查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样的话，\n',
            '我还是等会儿就回去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在那之前，\n',
            '就用看书来打发时间吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……你们几位也想看书吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不介意的话，\n',
            '我可以把看完的书送给你们哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x00BA, 0, 0x5D0))
    AddItem(0x0218, 1)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '红耀石　第７卷',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x00FE,
        (
            '这本小说很有意思的，\n',
            '推荐给你们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1AC3(): pass

    label('loc_1AC3')

    Jump('loc_2089')

    def _loc_1AC6(): pass

    label('loc_1AC6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_1F0C',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0028, 0x00, 0x04)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1C09',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1B35',
    )

    ChrTalk(
        0x00FE,
        (
            '还是要三思而后行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然雇游击士要花点钱，\n',
            '不过万一死了就什么也没有了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C06')

    def _loc_1B35(): pass

    label('loc_1B35')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '哎呀哎呀……\n',
            '这次的工作真是倒霉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '从蔡斯来这里的途中，\n',
            '搬运车在托兰特平原\n',
            '正中央发生了故障。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '担任护卫的游击士\n',
            '回去拿来了替换的零件，\n',
            '总算是得救了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……如果只有我自己，\n',
            '也许就糟糕了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C06(): pass

    label('loc_1C06')

    Jump('loc_1F09')

    def _loc_1C09(): pass

    label('loc_1C09')

    If(
        (
            (Expr.Eval, "OP_29(0x0028, 0x00, 0x10)"),
            (Expr.Eval, "OP_29(0x0029, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1D7C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1C7B',
    )

    ChrTalk(
        0x00FE,
        (
            '下次有工作的话，\n',
            '一定要再带那位\n',
            '游击士兄弟一起去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他真是个热心工作的人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D79')

    def _loc_1C7B(): pass

    label('loc_1C7B')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '哟，是你们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '上次发生危险的时候\n',
            '真是多亏了你们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊，叔叔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '你没事吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哦，\n',
            '后来那个游击士兄弟\n',
            '回城里取来了零件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '多亏了他，\n',
            '我才能平安地到这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎呀，\n',
            '游击士果然值得信赖啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们也辛苦了。\n',
            '路上要小心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1D79(): pass

    label('loc_1D79')

    Jump('loc_1F09')

    def _loc_1D7C(): pass

    label('loc_1D7C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1DDC',
    )

    ChrTalk(
        0x00FE,
        (
            '下次有工作的话，\n',
            '一定要再带那位\n',
            '游击士兄弟一起去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他真是个热心工作的人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F09')

    def _loc_1DDC(): pass

    label('loc_1DDC')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B0, 0, 0x580)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1E90',
    )

    ChrTalk(
        0x00FE,
        (
            '哦，是你们啊。\n',
            '这段时间多亏你们照顾了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '怎么了？\n',
            '亚尔摩那里的工作完成了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊，完成了。\n',
            '我们正准备回去呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哦，是吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么你们多保重。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F09')

    def _loc_1E90(): pass

    label('loc_1E90')

    ChrTalk(
        0x00FE,
        (
            '哦，是你们啊。\n',
            '亚尔摩那里的工作完成了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我这边\n',
            '总算也交接完货物了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '希望你们回去的路上\n',
            '也能够轻松愉快。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1F09(): pass

    label('loc_1F09')

    Jump('loc_2089')

    def _loc_1F0C(): pass

    label('loc_1F0C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_2089',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B0, 0, 0x580)),
            Expr.Return,
        ),
        'loc_1F75',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，之后只要等着领取\n',
            '从共和国运来的货物就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，\n',
            '趁现在好好放松一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2089')

    def _loc_1F75(): pass

    label('loc_1F75')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B0, 0, 0x580)),
            Expr.Return,
        ),
        'loc_2002',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '哦，是你们啊。\n',
            '这段时间多亏你们照顾了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我还要在这里\n',
            '等待共和国那边\n',
            '送过来的货物。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，\n',
            '趁现在好好放松一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2089')

    def _loc_2002(): pass

    label('loc_2002')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    SetScenaFlags(ScenaFlag(0x00B0, 0, 0x580))

    ChrTalk(
        0x00FE,
        (
            '哟，是你们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '怎么了？\n',
            '你们不是去亚尔摩吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊，嗯。\n',
            '我们正准备去呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哦，是吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么你们多保重。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2089(): pass

    label('loc_2089')

    TalkEnd(0x00FE)

    Return()

# id: 0x000F offset: 0x208D
@scena.Code('func_0F_208D')
def func_0F_208D():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_21D2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_2102',
    )

    ChrTalk(
        0x00FE,
        (
            '担任我的护卫的\n',
            '那个叫王的游击士\n',
            '好像是个东方人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '共和国的人\n',
            '如果都像他这样亲切就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_21D2')

    def _loc_2102(): pass

    label('loc_2102')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '因为蔡斯事件的调查，\n',
            '游击士们都很忙，\n',
            '我想委托可能会被推辞吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过出乎意料的是\n',
            '委托被接受了。\n',
            '真是让我吃了一惊啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在这种时候\n',
            '竟然也能接受\n',
            '我这样的委托啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '游击士协会\n',
            '果然很伟大啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_21D2(): pass

    label('loc_21D2')

    TalkEnd(0x00FE)

    Return()

# id: 0x0010 offset: 0x21D6
@scena.Code('func_10_21D6')
def func_10_21D6():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_2551',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_224B',
    )

    ChrTalk(
        0x00FE,
        (
            '现在我能做的事\n',
            '就是尽心尽责地\n',
            '完成分配下来的工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我相信这是给予\n',
            '调查活动的最好支持。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_254E')

    def _loc_224B(): pass

    label('loc_224B')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AF, 4, 0x57C)),
            Expr.Return,
        ),
        'loc_2408',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_22B5',
    )

    ChrTalk(
        0x00FE,
        (
            '现在冈多夫先生\n',
            '也不在蔡斯呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们的事\n',
            '就交给我来照顾吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '互相加油吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2405')

    def _loc_22B5(): pass

    label('loc_22B5')

    ChrTalk(
        0x00FE,
        (
            '啊，是你们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '调查得怎么样了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯～马马虎虎啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '王先生你这边呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '蔡斯事件之后， \n',
            '雾香接到了一大堆的工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因此我连\n',
            '轻松一下的空闲也没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我也打算用自己的方式\n',
            '来协助你们的调查啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊，\n',
            '不能再耽误你们的时间了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，我们互相加油吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯，你就放心吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F王先生也要保重啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2405(): pass

    label('loc_2405')

    Jump('loc_254E')

    def _loc_2408(): pass

    label('loc_2408')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_246E',
    )

    ChrTalk(
        0x00FE,
        (
            '现在冈多夫先生也不在，\n',
            '我要更加努力才行……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，\n',
            '稍微休息会儿就开始下一个工作吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_254E')

    def _loc_246E(): pass

    label('loc_246E')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '竟然袭击中央工房，\n',
            '实在是无法无天呀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '蔡斯事件之后， \n',
            '雾香接到了一大堆的工作。\n',
            '因此我连放松的空闲都没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在我能做的事\n',
            '就是尽心尽责地\n',
            '完成分配下来的工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我也打算用自己的方式\n',
            '来协助你们的调查啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_254E(): pass

    label('loc_254E')

    Jump('loc_25A6')

    def _loc_2551(): pass

    label('loc_2551')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_25A6',
    )

    ChrTalk(
        0x00FE,
        (
            '啊，是你们。\n',
            '谢谢，刚才你们帮了大忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们能到堡垒来\n',
            '真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_25A6(): pass

    label('loc_25A6')

    TalkEnd(0x00FE)

    Return()

# id: 0x0011 offset: 0x25AA
@scena.Code('func_11_25AA')
def func_11_25AA():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '东　卡尔瓦德共和国\n',
            '西　蔡斯市　２８０塞尔矩',
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
