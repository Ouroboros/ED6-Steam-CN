import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
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
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
        ('ED6_DT07/CH01300._CH', 'ED6_DT07/CH01300P._CP'),
        ('ED6_DT07/CH01310._CH', 'ED6_DT07/CH01310P._CP'),
        ('ED6_DT07/CH01300._CH', 'ED6_DT07/CH01300P._CP'),
        ('ED6_DT07/CH01270._CH', 'ED6_DT07/CH01270P._CP'),
        ('ED6_DT07/CH01530._CH', 'ED6_DT07/CH01530P._CP'),
        ('ED6_DT07/CH01760._CH', 'ED6_DT07/CH01760P._CP'),
        ('ED6_DT07/CH01720._CH', 'ED6_DT07/CH01720P._CP'),
        ('ED6_DT07/CH01750._CH', 'ED6_DT07/CH01750P._CP'),
    ]

# id: 0x10001 offset: 0xF2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '士兵布拉姆',
            x                   = 1000,
            z                   = 0,
            y                   = 48690,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
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
            dword_10            = 0,
            chipIndex           = 0,
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
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '格温副队长',
            x                   = -7370,
            z                   = 5500,
            y                   = 49600,
            direction           = 74,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
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
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            name                = '王',
            x                   = 13200,
            z                   = 0,
            y                   = 38690,
            direction           = 0,
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
            name                = '冈多夫',
            x                   = 3900,
            z                   = 0,
            y                   = 40920,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            name                = '鸡',
            x                   = 44200,
            z                   = 0,
            y                   = 18540,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
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
            dword_10            = 7,
            chipIndex           = 7,
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
            dword_10            = 7,
            chipIndex           = 7,
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
            dword_10            = 7,
            chipIndex           = 7,
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

# id: 0x10002 offset: 0x272
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x272
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -2420,
            y           = -2000,
            z           = 9840,
            range       = 6500,
            dword_10    = 0x000007D0,
            dword_14    = 0x00002AF8,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000011,
        ),
        ScenaEventData(
            x           = 6530,
            y           = -1000,
            z           = 50580,
            range       = 1330,
            dword_10    = 0x000007D0,
            dword_14    = 0x0000C260,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000018,
        ),
    )

# id: 0x10004 offset: 0x2B2
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
            talkFunctionIndex   = 0x0017,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x2D6
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_320',
    )

    ChrSetFlags(0x000B, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0009, 6760, 0, 48670, 315)
    ChrSetPos(0x0008, 1020, 0, 48670, 45)
    CreateThread(0x0008, 0x00, 0x00, func_02_39D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_31D',
    )

    ChrClearFlags(0x000E, 0x0080)

    def _loc_31D(): pass

    label('loc_31D')

    Jump('loc_33B')

    def _loc_320(): pass

    label('loc_320')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 3, 0x1413)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_334',
    )

    ChrSetFlags(0x0008, 0x0010)

    Jump('loc_33B')

    def _loc_334(): pass

    label('loc_334')

    CreateThread(0x0008, 0x00, 0x00, func_02_39D)

    def _loc_33B(): pass

    label('loc_33B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_34C',
    )

    ChrClearFlags(0x000D, 0x0080)

    def _loc_34C(): pass

    label('loc_34C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 3, 0x140B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_35D',
    )

    MapSetFlags(0x10000000)
    Event(0, func_10_203D)

    def _loc_35D(): pass

    label('loc_35D')

    Return()

# id: 0x0001 offset: 0x35E
@scena.Code('func_01_35E')
def func_01_35E():
    OP_16(0x02, 4000, -124000, -84000, 2293845)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_37F',
    )

    Jump('loc_384')

    def _loc_37F(): pass

    label('loc_37F')

    OP_71(0x0004, 0x0004)

    def _loc_384(): pass

    label('loc_384')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_39C',
    )

    OP_72(0x0003, 0x0010)
    OP_6F(0x0003, 420)

    def _loc_39C(): pass

    label('loc_39C')

    Return()

# id: 0x0002 offset: 0x39D
@scena.Code('func_02_39D')
def func_02_39D():
    ExecExpressionWithReg(
        0x0001,
        (
            Expr.Rand,
            (Expr.PushLong, 0x8),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Switch(
        (
            (Expr.PushReg, 0x1),
            Expr.Return,
        ),
        (0x00000000, 'loc_3CE'),
        (0x00000001, 'loc_3DA'),
        (0x00000002, 'loc_3E6'),
        (0x00000003, 'loc_3F2'),
        (0x00000004, 'loc_3FE'),
        (0x00000005, 'loc_40A'),
        (0x00000006, 'loc_416'),
        (-1, 'loc_422'),
    )

    def _loc_3CE(): pass

    label('loc_3CE')

    OP_99(0x00FE, 0x00, 0x07, 1450)

    Jump('loc_42E')

    def _loc_3DA(): pass

    label('loc_3DA')

    OP_99(0x00FE, 0x00, 0x07, 1550)

    Jump('loc_42E')

    def _loc_3E6(): pass

    label('loc_3E6')

    OP_99(0x00FE, 0x00, 0x07, 1600)

    Jump('loc_42E')

    def _loc_3F2(): pass

    label('loc_3F2')

    OP_99(0x00FE, 0x00, 0x07, 1400)

    Jump('loc_42E')

    def _loc_3FE(): pass

    label('loc_3FE')

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_42E')

    def _loc_40A(): pass

    label('loc_40A')

    OP_99(0x00FE, 0x00, 0x07, 1350)

    Jump('loc_42E')

    def _loc_416(): pass

    label('loc_416')

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_42E')

    def _loc_422(): pass

    label('loc_422')

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_42E')

    def _loc_42E(): pass

    label('loc_42E')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_443',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_42E')

    def _loc_443(): pass

    label('loc_443')

    Return()

# id: 0x0003 offset: 0x444
@scena.Code('func_03_444')
def func_03_444():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_467',
    )

    OP_8D(0x00FE, -9410, 54290, -4840, 47630, 2000)

    Jump('func_03_444')

    def _loc_467(): pass

    label('loc_467')

    Return()

# id: 0x0004 offset: 0x468
@scena.Code('func_04_468')
def func_04_468():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_48B',
    )

    OP_8D(0x00FE, -3560, 41360, 11130, 38000, 2000)

    Jump('func_04_468')

    def _loc_48B(): pass

    label('loc_48B')

    Return()

# id: 0x0005 offset: 0x48C
@scena.Code('func_05_48C')
def func_05_48C():
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

    def _loc_4B5(): pass

    label('loc_4B5')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5D9',
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
        'loc_59E',
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
        'loc_573',
    )

    ChrSetFlags(0x00FE, 0x0020)
    ChrTurnDirection(0x00FE, 0x0000, 0)
    ChrClearFlags(0x00FE, 0x0020)

    @scena.Lambda('lambda_0560')
    def lambda_0560():
        OP_94(0x00, 0x00FE, 0x00B4, 0x0000012C, 0x00001770, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_0560)

    Jump('loc_596')

    def _loc_573(): pass

    label('loc_573')

    @scena.Lambda('lambda_0579')
    def lambda_0579():
        OP_8D(0x00FE, -4320, 30420, 16309, 38200, 6000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_0579)

    Sleep(200)

    def _loc_596(): pass

    label('loc_596')

    Sleep(30)

    Jump('loc_5D6')

    def _loc_59E(): pass

    label('loc_59E')

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
        'loc_5D6',
    )

    TerminateThread(0x00FE, 0x02)

    @scena.Lambda('lambda_05BE')
    def lambda_05BE():
        OP_8D(0x00FE, -4320, 30420, 16309, 38200, 1500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_05BE)

    def _loc_5D6(): pass

    label('loc_5D6')

    Jump('loc_4B5')

    def _loc_5D9(): pass

    label('loc_5D9')

    Return()

# id: 0x0006 offset: 0x5DA
@scena.Code('func_06_5DA')
def func_06_5DA():
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

    def _loc_603(): pass

    label('loc_603')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_727',
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
        'loc_6EC',
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
        'loc_6C1',
    )

    ChrSetFlags(0x00FE, 0x0020)
    ChrTurnDirection(0x00FE, 0x0000, 0)
    ChrClearFlags(0x00FE, 0x0020)

    @scena.Lambda('lambda_06AE')
    def lambda_06AE():
        OP_94(0x00, 0x00FE, 0x00B4, 0x0000012C, 0x00001770, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_06AE)

    Jump('loc_6E4')

    def _loc_6C1(): pass

    label('loc_6C1')

    @scena.Lambda('lambda_06C7')
    def lambda_06C7():
        OP_8D(0x00FE, -780, 24910, 8900, 46240, 6000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_06C7)

    Sleep(200)

    def _loc_6E4(): pass

    label('loc_6E4')

    Sleep(30)

    Jump('loc_724')

    def _loc_6EC(): pass

    label('loc_6EC')

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
        'loc_724',
    )

    TerminateThread(0x00FE, 0x02)

    @scena.Lambda('lambda_070C')
    def lambda_070C():
        OP_8D(0x00FE, -780, 24910, 8900, 46240, 1500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_070C)

    def _loc_724(): pass

    label('loc_724')

    Jump('loc_603')

    def _loc_727(): pass

    label('loc_727')

    Return()

# id: 0x0007 offset: 0x728
@scena.Code('func_07_728')
def func_07_728():
    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7AB',
    )

    CreateThread(0x00FE, 0x02, 0x00, func_08_7AC)
    PlaySE(401, 0x00, 0x64)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Rand,
            (Expr.PushLong, 0xA),
            Expr.Mod,
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_7AB',
    )

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['新鲜鸡蛋'], 1)"),
            Expr.Return,
        ),
        'loc_7AB',
    )

    TalkBegin(0x00FE)
    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['新鲜鸡蛋']),
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

    def _loc_7AB(): pass

    label('loc_7AB')

    Return()

# id: 0x0008 offset: 0x7AC
@scena.Code('func_08_7AC')
def func_08_7AC():
    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x7),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_7C7',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    Yield()

    Jump('func_08_7AC')

    def _loc_7C7(): pass

    label('loc_7C7')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0009 offset: 0x7D2
@scena.Code('func_09_7D2')
def func_09_7D2():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 4, 0x140C)),
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 0, 0x1410)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_7E3',
    )

    Call(0, 0x0015)

    Return()

    def _loc_7E3(): pass

    label('loc_7E3')

    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_912',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0031, 0x00, 0x10)"),
            (Expr.Eval, "OP_29(0x0031, 0x01, 0x0020)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_802',
    )

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    def _loc_802(): pass

    label('loc_802')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_87A',
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
            TXT(0x00, '【◇前作『爱的使者』高评价完成】\n'),
            TXT(0x01, '【◇没有完成】\n'),
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
        (0x00000000, 'loc_86E'),
        (0x00000001, 'loc_874'),
        (-1, 'loc_87A'),
    )

    def _loc_86E(): pass

    label('loc_86E')

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    Jump('loc_87A')

    def _loc_874(): pass

    label('loc_874')

    ClearScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    Jump('loc_87A')

    def _loc_87A(): pass

    label('loc_87A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8C9',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，呼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是太紧张了吧\n',
            '感觉好疲倦呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼啊啊…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_90F')

    def _loc_8C9(): pass

    label('loc_8C9')

    ChrTalk(
        0x00FE,
        (
            '果然是太紧张了，\n',
            '完全睡不着觉…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼啊啊…\n',
            '但却一直在打呵欠。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_90F(): pass

    label('loc_90F')

    Jump('loc_E57')

    def _loc_912(): pass

    label('loc_912')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_9C8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_96F',
    )

    ChrTalk(
        0x00FE,
        (
            '现在最头疼的事情\n',
            '就是大门关不上了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这，这害得\n',
            '我都睡不着觉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_9C5')

    def _loc_96F(): pass

    label('loc_96F')

    ChrTalk(
        0x00FE,
        (
            '不早点想办法\n',
            '能早日恢复啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大门关上再关不上的话，\n',
            '我大概就要患上失眠症了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9C5(): pass

    label('loc_9C5')

    Jump('loc_E57')

    def _loc_9C8(): pass

    label('loc_9C8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_A62',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_A18',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然没有发生什么\n',
            '大灾害，不过……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '地震真是好可怕啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A5F')

    def _loc_A18(): pass

    label('loc_A18')

    ChrTalk(
        0x00FE,
        (
            '听说连雷斯顿要塞\n',
            '也遭受到地震了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '吃了一惊，\n',
            '马上就醒了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_A5F(): pass

    label('loc_A5F')

    Jump('loc_E57')

    def _loc_A62(): pass

    label('loc_A62')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_C9B',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0031, 0x00, 0x10)"),
            (Expr.Eval, "OP_29(0x0031, 0x01, 0x0020)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_A7E',
    )

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    def _loc_A7E(): pass

    label('loc_A7E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_AF6',
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
            TXT(0x00, '【◇前作『爱的使者』高评价完成】\n'),
            TXT(0x01, '【◇没有完成】\n'),
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
        (0x00000000, 'loc_AEA'),
        (0x00000001, 'loc_AF0'),
        (-1, 'loc_AF6'),
    )

    def _loc_AEA(): pass

    label('loc_AEA')

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    Jump('loc_AF6')

    def _loc_AF0(): pass

    label('loc_AF0')

    ClearScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    Jump('loc_AF6')

    def _loc_AF6(): pass

    label('loc_AF6')

    OP_62(0x00FE, 0x00000000, 2000, 0x1C, 0x21, 0x000000FA, 0x00)
    Sleep(1500)

    OP_63(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_BDD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_B4A',
    )

    ChrTalk(
        0x00FE,
        (
            '……哎～哎嘿嘿………\n',
            '菲……不行啊…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BDA')

    def _loc_B4A(): pass

    label('loc_B4A')

    TalkSetChrName('士兵布拉姆')

    ChrTalk(
        0x00FE,
        (
            '…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkSetChrName('士兵布拉姆')

    ChrTalk(
        0x00FE,
        (
            '……哎～哎嘿嘿………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '菲……不行啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不……不要…………\n',
            '……不要抛弃我……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_BDA(): pass

    label('loc_BDA')

    Jump('loc_C98')

    def _loc_BDD(): pass

    label('loc_BDD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_C1C',
    )

    TalkSetChrName('士兵布拉姆')

    ChrTalk(
        0x00FE,
        (
            '……呜、呜呜～………\n',
            '菲……原谅我…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C98')

    def _loc_C1C(): pass

    label('loc_C1C')

    ChrTalk(
        0x00FE,
        (
            '…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……呜、呜呜～………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '菲……原谅我吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对……对不起…………\n',
            '……是我不好………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_C98(): pass

    label('loc_C98')

    Jump('loc_E57')

    def _loc_C9B(): pass

    label('loc_C9B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 3, 0x1413)),
            Expr.Return,
        ),
        'loc_D5F',
    )

    OP_62(0x00FE, 0x00000000, 2000, 0x1C, 0x21, 0x000000FA, 0x00)
    Sleep(1500)

    OP_63(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_CFA',
    )

    ChrTalk(
        0x00FE,
        (
            '…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呜～……呜～…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D5C')

    def _loc_CFA(): pass

    label('loc_CFA')

    ChrTalk(
        0x00FE,
        (
            '…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……嗯～……………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '异状……没有………\n',
            '……发～生～…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_D5C(): pass

    label('loc_D5C')

    Jump('loc_E57')

    def _loc_D5F(): pass

    label('loc_D5F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 2, 0x1412)),
            Expr.Return,
        ),
        'loc_D9A',
    )

    ChrTalk(
        0x00FE,
        (
            '呼哇哇～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯嗯嗯……\n',
            '我又睡着了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E57')

    def _loc_D9A(): pass

    label('loc_D9A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 1, 0x1411)),
            Expr.Return,
        ),
        'loc_DCE',
    )

    ChrTalk(
        0x00FE,
        (
            '呼哇哇～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯？见过赫宁了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E57')

    def _loc_DCE(): pass

    label('loc_DCE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 4, 0x140C)),
            Expr.Return,
        ),
        'loc_E22',
    )

    ChrTalk(
        0x00FE,
        (
            '赫宁那家伙现在\n',
            '应该在休息所。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在那里的２楼偷懒\n',
            '是他一贯的作法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E57')

    def _loc_E22(): pass

    label('loc_E22')

    ChrTalk(
        0x00FE,
        (
            '呼哇哇～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯嗯嗯……\n',
            '今天也是好天气啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E57(): pass

    label('loc_E57')

    TalkEnd(0x0008)

    Return()

# id: 0x000A offset: 0xE5B
@scena.Code('func_0A_E5B')
def func_0A_E5B():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_F45',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_EE6',
    )

    ChrTalk(
        0x00FE,
        (
            '布拉姆那小子\n',
            '从刚才开始就一直呵欠不断。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是今天可\n',
            '不能睡啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '像、像现在这种情况\n',
            '可不能只靠一个人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Jump('loc_F42')

    def _loc_EE6(): pass

    label('loc_EE6')

    ChrTalk(
        0x00FE,
        (
            '如果布拉姆睡觉的话\n',
            '警备工作就只能靠我一个了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是他再敢睡觉，\n',
            '我就用枪把他捅醒。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F42(): pass

    label('loc_F42')

    Jump('loc_1014')

    def _loc_F45(): pass

    label('loc_F45')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1014',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_FBC',
    )

    ChrTalk(
        0x00FE,
        (
            '对面是共和国，在安全方面\n',
            '大概没什么问题，不过……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '像这样毫无防备，\n',
            '总还是让人不放心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Jump('loc_1014')

    def _loc_FBC(): pass

    label('loc_FBC')

    ChrTalk(
        0x00FE,
        (
            '像这样毫无防备，\n',
            '总还是让人不踏实啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，难得空闲\n',
            '现在的状况让人不得不紧张。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1014(): pass

    label('loc_1014')

    TalkEnd(0x00FE)

    Return()

# id: 0x000B offset: 0x1018
@scena.Code('func_0B_1018')
def func_0B_1018():
    TalkBegin(0x00FE)
    TalkEnd(0x00FE)

    Return()

# id: 0x000C offset: 0x101F
@scena.Code('func_0C_101F')
def func_0C_101F():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_111C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_108B',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然地震已经停止了，\n',
            '但还是不能放松。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不久之后就是互不侵犯条约\n',
            '的签字仪式了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1119')

    def _loc_108B(): pass

    label('loc_108B')

    ChrTalk(
        0x00FE,
        (
            '中央工房好像做出了\n',
            '地震停止的公开宣言…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '其实军队上层也发布了\n',
            '类似的通知。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，理由暂且不问，\n',
            '不过总之地震确实是没再发生了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_1119(): pass

    label('loc_1119')

    Jump('loc_164B')

    def _loc_111C(): pass

    label('loc_111C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_11AD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_1170',
    )

    ChrTalk(
        0x00FE,
        (
            '地震的发生场所\n',
            '全都是重要设施所在地，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这似乎不是偶然啊…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11AA')

    def _loc_1170(): pass

    label('loc_1170')

    ChrTalk(
        0x00FE,
        (
            '这次是雷斯顿要塞吗…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '竟然专门挑选\n',
            '军事基地…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_11AA(): pass

    label('loc_11AA')

    Jump('loc_164B')

    def _loc_11AD(): pass

    label('loc_11AD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 3, 0x1413)),
            Expr.Return,
        ),
        'loc_1277',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_120C',
    )

    ChrTalk(
        0x00FE,
        (
            '圣海姆门也\n',
            '好像发生地震了啊，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们这里也不能大意，\n',
            '一定要加强警备！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1274')

    def _loc_120C(): pass

    label('loc_120C')

    ChrTalk(
        0x00FE,
        (
            '圣海姆门也\n',
            '好像发生地震了啊，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说不定这里也\n',
            '会发生地震呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '从现在开始一定\n',
            '要加强警备。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_1274(): pass

    label('loc_1274')

    Jump('loc_164B')

    def _loc_1277(): pass

    label('loc_1277')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 4, 0x140C)),
            Expr.Return,
        ),
        'loc_156E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 6, 0x140E)),
            Expr.Return,
        ),
        'loc_12E8',
    )

    ChrTalk(
        0x00FE,
        (
            '除了有地震之外\n',
            '就没有别的奇怪现象了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果有什么可疑的发现\n',
            '部下们应该会来报告给我的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_156B')

    def _loc_12E8(): pass

    label('loc_12E8')

    ChrTalk(
        0x00FE,
        (
            '嗯？有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1002F啊，我们是游击士协会的人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '希望您能配合我们\n',
            '做个调查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '可以是可以……\n',
            '不过请尽量长话短说吧。',
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
            '询问对方是否在地震前后\n',
            '发现了什么奇怪的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x00FE,
        (
            '地震……\n',
            '是指三天前的那场地震吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，除了地震之外\n',
            '就是很普通的一天了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果有什么可疑的发现\n',
            '部下们应该会来报告给我的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1015F是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#032F嗯，看来\n',
            '白跑了一趟呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还有别的要问吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_14E4',
    )

    ChrTalk(
        0x0106,
        (
            '#050F啊，这些就可以啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '抱歉打扰您的工作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0106, 400)

    Jump('loc_1528')

    def _loc_14E4(): pass

    label('loc_14E4')

    ChrTalk(
        0x0103,
        (
            '#027F嗯，这些就可以了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '打扰您的工作啦，真是不好意思。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0103, 400)

    def _loc_1528(): pass

    label('loc_1528')

    ChrTalk(
        0x00FE,
        (
            '哪里，不必客气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那我就先失礼了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0281, 6, 0x140E))

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 1, 0x1411)),
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 7, 0x140F)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_156B',
    )

    OP_28(0x0085, 0x01, 0x0800)

    Jump('loc_156B')

    def _loc_156B(): pass

    label('loc_156B')

    Jump('loc_164B')

    def _loc_156E(): pass

    label('loc_156E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 4, 0x140C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_164B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_15AB',
    )

    ChrTalk(
        0x00FE,
        (
            '真是的……\n',
            '这里的警备实在是太松懈了，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_164B')

    def _loc_15AB(): pass

    label('loc_15AB')

    ChrTalk(
        0x00FE,
        (
            '真是的……\n',
            '这里的警备实在是太松懈了，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '条约签字仪式的日子就快到了，\n',
            '现在应该强化警备才对……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '像现在这种状态，\n',
            '遇到紧急情况的话根本就无法应对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_164B(): pass

    label('loc_164B')

    TalkEnd(0x000B)

    Return()

# id: 0x000D offset: 0x164F
@scena.Code('func_0D_164F')
def func_0D_164F():
    TalkBegin(0x00FE)
    TalkEnd(0x00FE)

    Return()

# id: 0x000E offset: 0x1656
@scena.Code('func_0E_1656')
def func_0E_1656():
    TalkBegin(0x000D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AF, 4, 0x57C)),
            Expr.Return,
        ),
        'loc_1663',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_1663(): pass

    label('loc_1663')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_16D9',
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
        (0x00000000, 'loc_16CD'),
        (0x00000001, 'loc_16D3'),
        (-1, 'loc_16D9'),
    )

    def _loc_16CD(): pass

    label('loc_16CD')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    Jump('loc_16D9')

    def _loc_16D3(): pass

    label('loc_16D3')

    ClearScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    Jump('loc_16D9')

    def _loc_16D9(): pass

    label('loc_16D9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 7, 0x1427)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_18A5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1867',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_1864',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0286, 4, 0x1434)),
            Expr.Return,
        ),
        'loc_1732',
    )

    ChrTalk(
        0x00FE,
        (
            '现在应该赶快去\n',
            '亚尔摩村吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总之请小心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1864')

    def _loc_1732(): pass

    label('loc_1732')

    ChrTalk(
        0x00FE,
        (
            '呀，辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我现在正要\n',
            '回蔡斯了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在的时间\n',
            '应该很紧迫吧…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1015F嗯，其实是这样……',
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
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '那可真是\n',
            '太诡异了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不管怎么说，现在\n',
            '还是抓紧时间吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，请小心注意吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1006F嗯，我们走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0286, 4, 0x1434))

    def _loc_1864(): pass

    label('loc_1864')

    Jump('loc_18A2')

    def _loc_1867(): pass

    label('loc_1867')

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
    def _loc_18A2(): pass

    label('loc_18A2')

    Jump('loc_1DDC')

    def _loc_18A5(): pass

    label('loc_18A5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_1A64',
    )

    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_19B1',
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

    Jump('loc_1A61')

    def _loc_19B1(): pass

    label('loc_19B1')

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

    def _loc_1A61(): pass

    label('loc_1A61')

    Jump('loc_1BAC')

    def _loc_1A64(): pass

    label('loc_1A64')

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
            '请多指教。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊啊，彼此彼此。',
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
    def _loc_1BAC(): pass

    label('loc_1BAC')

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
        'loc_1D54',
    )

    ChrTurnDirection(0x00FE, 0x0106, 400)

    ChrTalk(
        0x00FE,
        (
            '连阿加特前辈也\n',
            '请多多关照了。',
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

    Jump('loc_1D9F')

    def _loc_1D54(): pass

    label('loc_1D54')

    ChrTurnDirection(0x00FE, 0x0103, 400)

    ChrTalk(
        0x00FE,
        (
            '雪拉扎德前辈也\n',
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

    def _loc_1D9F(): pass

    label('loc_1D9F')

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
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))
    def _loc_1DDC(): pass

    label('loc_1DDC')

    TalkEnd(0x000D)

    Return()

# id: 0x000F offset: 0x1DE0
@scena.Code('func_0F_1DE0')
def func_0F_1DE0():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_2039',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x041A, 1, 0x20D1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1FDD',
    )

    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '哟，艾丝蒂尔你们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1011F啊，冈多夫先生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1040F好久不见了。',
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
        'loc_1E86',
    )

    ChrTalk(
        0x0106,
        (
            '#050F在巡逻吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0106, 400)

    Jump('loc_1EE3')

    def _loc_1E86(): pass

    label('loc_1E86')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1EB7',
    )

    ChrTalk(
        0x0103,
        (
            '#020F是在巡逻中吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0103, 400)

    Jump('loc_1EE3')

    def _loc_1EB7(): pass

    label('loc_1EB7')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1EE3',
    )

    ChrTalk(
        0x0107,
        (
            '#064F是在巡逻吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0107, 400)

    def _loc_1EE3(): pass

    label('loc_1EE3')

    ChrTalk(
        0x00FE,
        (
            '啊，正是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不管怎么说，警戒工作\n',
            '可是不能松懈的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那，你们就集中精力\n',
            '完成自己的任务吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '维持治安之类的事情\n',
            '交给我们就可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1002F嗯……明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1040F……那可太好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '那么，请当心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '喔，真周到啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x041A, 1, 0x20D1))

    Jump('loc_2039')

    def _loc_1FDD(): pass

    label('loc_1FDD')

    ChrTalk(
        0x00FE,
        (
            '在现在这种形势下，\n',
            '不管再发生什么我也不会惊奇了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我只要做好自己的\n',
            '警戒就可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2039(): pass

    label('loc_2039')

    TalkEnd(0x00FE)

    Return()

# id: 0x0010 offset: 0x203D
@scena.Code('func_10_203D')
def func_10_203D():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_204E',
    )

    Call(0, 0x0016)

    def _loc_204E(): pass

    label('loc_204E')

    EventBegin(0x00)
    MapClearFlags(0x00000010)
    ChrSetPos(0x0101, 3000, -500, 13740, 0)
    ChrSetPos(0x00F7, 1560, -500, 13250, 0)
    ChrSetPos(0x0105, 2600, -500, 11780, 0)
    ChrSetPos(0x0104, 1630, -500, 10970, 0)
    CameraMove(4030, 0, 48420, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(6200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)

    @scena.Lambda('lambda_20DC')
    def lambda_20DC():
        CameraMove(3180, -500, 27340, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_20DC)

    @scena.Lambda('lambda_20F4')
    def lambda_20F4():
        OP_67(0, 9500, -10000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_20F4)

    OP_C8(0x0200, 0x0046, 'C_PLAC09._CH', 0x00, 0x03E8)
    ShowPlaceName('沃尔费堡垒')
    FadeIn(1000, 0)
    Sleep(1000)

    @scena.Lambda('lambda_213B')
    def lambda_213B():
        ChrWalkTo(0x00FE, 3520, -500, 20380, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_213B)

    Sleep(200)

    @scena.Lambda('lambda_215B')
    def lambda_215B():
        ChrWalkTo(0x00FE, 2170, -500, 20000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_215B)

    @scena.Lambda('lambda_2176')
    def lambda_2176():
        ChrWalkTo(0x00FE, 2270, -500, 18500, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_2176)

    @scena.Lambda('lambda_2191')
    def lambda_2191():
        ChrWalkTo(0x00FE, 3560, -500, 18870, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_2191)

    OP_0D()
    WaitForThreadExit(0x0101, 0x0002)
    WaitForThreadExit(0x0101, 0x0003)
    Fade(1000)
    CameraMove(3240, -500, 19880, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3100, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    WaitForThreadExit(0x0105, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010220823V#1011F沃尔费堡垒啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010220824V虽然是和卡尔瓦德共和国之间的国境线，\n',
            '但一直是个安宁平和的地方呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040220825V#033F#6P同为国境线，\n',
            '这里和哈肯大门就完全不同啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040220826V#035F呼～果然是利贝尔的友邦啊，\n',
            '享受的待遇和我的祖国完全不同。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_234A',
    )

    ChrTalk(
        0x0106,
        (
            '#0050220827V#552F#5P真是……\n',
            '就好像在说与己无关的事情一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2387')

    def _loc_234A(): pass

    label('loc_234A')

    ChrTalk(
        0x0103,
        (
            '#0030220828V#025F#5P唉……\n',
            '说得就好像完全与己无关一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2387(): pass

    label('loc_2387')

    ChrTalk(
        0x0105,
        (
            '#0060220829V#542F这里警备薄弱，虽然是有友邦\n',
            '的因素在内，不过……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060220830V更主要的原因是这里临接山道，\n',
            '军队是很难通行的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060220831V大门建造得比较小\n',
            '大概也是出于这种考虑。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040220832V#030F#6P原来如此，和面对广阔大道的\n',
            '哈肯大门确实是有所不同啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_2559',
    )

    ChrTalk(
        0x0106,
        (
            '#0050220833V#053F#5P就算是这样，\n',
            '在堡垒门口养鸡… \n',
            '也还真是前所未闻了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0106, 0x0101, 400)

    ChrTalk(
        0x0106,
        (
            '#0050220834V#051F#6P好了，咱们还是马上去\n',
            '调查『地震』的事吧，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050220835V首先要去和守备队长打个招呼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_261F')

    def _loc_2559(): pass

    label('loc_2559')

    ChrTalk(
        0x0103,
        (
            '#0030220836V#021F#5P呵呵，即使如此…\n',
            '在堡垒门口养鸡…\n',
            '还样的国境线还真是够随便啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030220837V#020F#6P好了，还是快点开始\n',
            '调查『地震』的事吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030220838V先去和守备队长打个招呼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_261F(): pass

    label('loc_261F')

    ChrTurnDirection(0x0101, 0x00F7, 400)

    ChrTalk(
        0x0101,
        (
            '#0010220839V#1006F嗯，了解！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0281, 3, 0x140B))
    OP_28(0x006D, 0x04, 0x40)
    OP_28(0x0085, 0x01, 0x0020)
    EventEnd(0x00)

    Return()

# id: 0x0011 offset: 0x2659
@scena.Code('func_11_2659')
def func_11_2659():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 4, 0x140C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2668',
    )

    Call(0, 0x0012)

    Jump('loc_2699')

    def _loc_2668(): pass

    label('loc_2668')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 1, 0x1411)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 6, 0x140E)),
            Expr.Ez,
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 7, 0x140F)),
            Expr.Ez,
            Expr.Or,
            Expr.Return,
        ),
        'loc_2681',
    )

    Call(0, 0x0013)

    Jump('loc_2699')

    def _loc_2681(): pass

    label('loc_2681')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 2, 0x1412)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 1, 0x1411)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 6, 0x140E)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 7, 0x140F)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2699',
    )

    Call(0, 0x0014)

    def _loc_2699(): pass

    label('loc_2699')

    Return()

# id: 0x0012 offset: 0x269A
@scena.Code('func_12_269A')
def func_12_269A():
    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_270D',
    )

    ChrTalk(
        0x0101,
        (
            '#0010220840V#1000F现在要抓紧时间\n',
            '调查地震的事……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010220841V先去和这里的队长\n',
            '打个招呼吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2815')

    def _loc_270D(): pass

    label('loc_270D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_2797',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_272A',
    )

    ChrTurnDirection(0x0106, 0x0001, 400)

    Jump('loc_2731')

    def _loc_272A(): pass

    label('loc_272A')

    ChrTurnDirection(0x0106, 0x0000, 400)

    def _loc_2731(): pass

    label('loc_2731')

    ChrTalk(
        0x0106,
        (
            '#0050220842V#050F现在要赶快进行\n',
            '地震的调查。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050220843V首先从守备队长\n',
            '快要需要试着听话了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2815')

    def _loc_2797(): pass

    label('loc_2797')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_27AD',
    )

    ChrTurnDirection(0x0103, 0x0001, 400)

    Jump('loc_27B4')

    def _loc_27AD(): pass

    label('loc_27AD')

    ChrTurnDirection(0x0103, 0x0000, 400)

    def _loc_27B4(): pass

    label('loc_27B4')

    ChrTalk(
        0x0103,
        (
            '#0030220844V#020F现在要赶快\n',
            '去调查地震的事情哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030220845V先去和这里的队长\n',
            '打个招呼吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2815(): pass

    label('loc_2815')

    ChrMoveToRelative(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x0013 offset: 0x2831
@scena.Code('func_13_2831')
def func_13_2831():
    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_28B5',
    )

    ChrTalk(
        0x0101,
        (
            '#0010220883V#1006F（喂……\n',
            '　调查还没结束啊。)',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010220884V(休息所的人也不要漏掉，\n',
            '　要探听出全部情报才行。)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A8F')

    def _loc_28B5(): pass

    label('loc_28B5')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2932',
    )

    ChrTalk(
        0x0105,
        (
            '#0060220885V#047F（调查还没完哦……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060220886V#040F（休息所里的人也要问到，\n',
            '　情报收集得越多越好。)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A8F')

    def _loc_2932(): pass

    label('loc_2932')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_29AF',
    )

    ChrTalk(
        0x0104,
        (
            '#0040220887V#030F（嗯……\n',
            '　调查还没结束哦。)',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040220888V(休息所里的人也不要忘记，\n',
            '　所有人都要问到。)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A8F')

    def _loc_29AF(): pass

    label('loc_29AF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_2A25',
    )

    ChrTalk(
        0x0106,
        (
            '#0050220889V#555F（调查还没完成啊。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050220890V(要收集足够多的情报才行，\n',
            '　休息所里的人也要问到。)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A8F')

    def _loc_2A25(): pass

    label('loc_2A25')

    ChrTalk(
        0x0103,
        (
            '#0030220891V#020F（调查还没完成哦，）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030220892V(休息所的人也不要漏掉，\n',
            '　继续去探听一下情报吧。)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2A8F(): pass

    label('loc_2A8F')

    ChrMoveToRelative(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x0014 offset: 0x2AAB
@scena.Code('func_14_2AAB')
def func_14_2AAB():
    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2B29',
    )

    ChrTalk(
        0x0101,
        (
            '#0010220984V#1015F……虽然情报已经收集完了，\n',
            '但还没有向队长报告呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010220985V报告完毕后再回协会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2C3C')

    def _loc_2B29(): pass

    label('loc_2B29')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_2BB6',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2B46',
    )

    ChrTurnDirection(0x0106, 0x0001, 400)

    Jump('loc_2B4D')

    def _loc_2B46(): pass

    label('loc_2B46')

    ChrTurnDirection(0x0106, 0x0000, 400)

    def _loc_2B4D(): pass

    label('loc_2B4D')

    ChrTalk(
        0x0106,
        (
            '#0050220986V#050F调查算是告一段落了，\n',
            '但还没向守备队长报告啊，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050220987V报告之后再回协会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2C3C')

    def _loc_2BB6(): pass

    label('loc_2BB6')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2BCC',
    )

    ChrTurnDirection(0x0103, 0x0001, 400)

    Jump('loc_2BD3')

    def _loc_2BCC(): pass

    label('loc_2BCC')

    ChrTurnDirection(0x0103, 0x0000, 400)

    def _loc_2BD3(): pass

    label('loc_2BD3')

    ChrTalk(
        0x0103,
        (
            '#0030220988V#020F调查虽然结束了，\n',
            '但还没有向队长报告呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030220989V过去做个报告之后\n',
            '再回协会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2C3C(): pass

    label('loc_2C3C')

    ChrMoveToRelative(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x0015 offset: 0x2C58
@scena.Code('func_15_2C58')
def func_15_2C58():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2C69',
    )

    Call(0, 0x0016)

    def _loc_2C69(): pass

    label('loc_2C69')

    EventBegin(0x00)
    OP_4A(0x0008, 255)
    Fade(1000)
    ChrSetPos(0x0105, 1860, 0, 46170, 0)
    ChrSetPos(0x0101, 1500, 0, 47410, 0)
    ChrSetPos(0x00F7, 300, 0, 47400, 0)
    ChrSetPos(0x0104, 700, 0, 46200, 0)
    CameraMove(1210, 0, 47890, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(33000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#2050220893V#5P呜啊啊啊～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2050220894V#5P嗯？有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220895V#1011F#4P啊……\n',
            '我是游击士协会的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060220896V#040F可以耽误您一点时间\n',
            '配合我们做一个调查吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2050220897V#5P啊、嗯，没问题……',
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
            '询问是否在３天前地震的前后\n',
            '遇到了什么奇怪的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x0008,
        (
            '#2050220898V#5P啊啊～那次的地震啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2050220899V#5P我当时正在打磕睡，忽然感觉有晃动，\n',
            '还以为副队长在推我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2050220900V#5P但睁眼一看，周围谁都没有……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2050220901V#5P虽然之后明白是发生地震了。\n',
            '但一开始还以为是有人在戏弄我呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220902V#1019F#4P那个算是奇怪的事情吗……\n',
            '明明只是你自己的工作态度问题而已……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040220903V#035F呼～能站着睡着\n',
            '也算是个了不起的特技了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040220904V#030F不过我也可以\n',
            '躺在沙发上就轻轻松松\n',
            '吃光一整套全餐呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_304C',
    )

    ChrTalk(
        0x0106,
        (
            '#0050220905V#551F#6P这种事有什么值得骄傲啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_307E')

    def _loc_304C(): pass

    label('loc_304C')

    ChrTalk(
        0x0103,
        (
            '#0030220906V#025F#6P那种事有什么可自豪的嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_307E(): pass

    label('loc_307E')

    ChrTalk(
        0x0105,
        (
            '#0060220907V#542F除、除了那个之外\n',
            '就没有别的发现了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2050220908V#5P……我想想。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2050220909V#5P啊，对了，赫宁\n',
            '他倒是问过我一件怪事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220910V#1015F#4P怪事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2050220911V#5P那是在地震发生\n',
            '的前一天……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2050220912V#5P同班的赫宁忽然过来问我\n',
            '有没有人通过大门。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2050220913V#5P我告诉他没有以后，\n',
            '他好像就显得很困惑……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060220914V#043F这是怎么回事呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 5, 0x140D)),
            Expr.Return,
        ),
        'loc_3279',
    )

    ChrTalk(
        0x0101,
        (
            '#0010220915V#1006F#4P也许他有什么发现也说不定。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010220916V去找那个叫赫宁的士兵\n',
            '再问一次吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_32D3')

    def _loc_3279(): pass

    label('loc_3279')

    ChrTalk(
        0x0101,
        (
            '#0010220915V#1006F#4P也许他有什么发现也说不定。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010220918V向那个士兵\n',
            '打个招呼吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_32D3(): pass

    label('loc_32D3')

    SetScenaFlags(ScenaFlag(0x0282, 0, 0x1410))
    OP_28(0x0085, 0x01, 0x0100)
    OP_4B(0x0008, 255)
    EventEnd(0x00)

    Return()

# id: 0x0016 offset: 0x32E3
@scena.Code('func_16_32E3')
def func_16_32E3():
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
        (0x00000000, 'loc_335D'),
        (0x00000001, 'loc_3363'),
        (-1, 'loc_3369'),
    )

    def _loc_335D(): pass

    label('loc_335D')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_3369')

    def _loc_3363(): pass

    label('loc_3363')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_3369')

    def _loc_3369(): pass

    label('loc_3369')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_3377',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    Jump('loc_337B')

    def _loc_3377(): pass

    label('loc_3377')

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    def _loc_337B(): pass

    label('loc_337B')

    Return()

# id: 0x0017 offset: 0x337C
@scena.Code('func_17_337C')
def func_17_337C():
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

# id: 0x0018 offset: 0x33DA
@scena.Code('func_18_33DA')
def func_18_33DA():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_33E7',
    )

    Return()

    def _loc_33E7(): pass

    label('loc_33E7')

    EventBegin(0x01)
    ChrTurnDirection(0x0009, 0x0000, 400)
    OP_4A(0x0009, 255)

    ChrTalk(
        0x0009,
        (
            '喂喂！\n',
            '那边是共和国的领土了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '这种非常时期\n',
            '别乱走啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveToRelative(0x0000, 0, 0, -1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)
    ChrSetDirection(0x0009, 315, 0)
    OP_4B(0x0009, 255)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
