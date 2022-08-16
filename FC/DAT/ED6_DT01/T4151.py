import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T4151_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4151   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4151.x'
    header.mapIndex       = 1
    header.bgm            = 84
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT01/T4101._SN', 'ED6_DT01/T4101_1._SN', 'ED6_DT01/T4101_2._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0x0000D2F0,
            dword_04        = 0x000000FA,
            dword_08        = 0x00000FA0,
            word_0C         = 0x0004,
            word_0E         = 0x0000,
            dword_10        = 0,
            dword_14        = 9500,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 4200,
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
        ('ED6_DT07/CH01650._CH', 'ED6_DT07/CH01650P._CP'),
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
        ('ED6_DT07/CH00003._CH', 'ED6_DT07/CH00003P._CP'),
        ('ED6_DT07/CH00013._CH', 'ED6_DT07/CH00013P._CP'),
    ]

# id: 0x10001 offset: 0xCA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '士兵',
            x                   = 74950,
            z                   = 0,
            y                   = 70230,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 79960,
            z                   = 250,
            y                   = 69120,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 83030,
            z                   = 750,
            y                   = -6740,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 86990,
            z                   = 750,
            y                   = 68660,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 43000,
            z                   = 1250,
            y                   = 47060,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 43000,
            z                   = 1250,
            y                   = 28960,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0005,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0006,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0007,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0008,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0009,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x000A,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x000B,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x000C,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x000D,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x000E,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '王都格兰赛尔·北街区',
            x                   = 17760,
            z                   = 0,
            y                   = 63880,
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
            name                = '王都格兰赛尔·南街区',
            x                   = 29270,
            z                   = 0,
            y                   = -950,
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
            name                = '王都格兰赛尔·空港',
            x                   = 51010,
            z                   = 0,
            y                   = 102170,
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

# id: 0x10002 offset: 0x32A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x32A
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 109720,
            y           = 1000,
            z           = 32980,
            range       = 2000,
            dword_10    = 0x00000FA0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000014,
        ),
        ScenaEventData(
            x           = 76740,
            y           = 1000,
            z           = 23010,
            range       = 2000,
            dword_10    = 0x000009C4,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000015,
        ),
        ScenaEventData(
            x           = 69950,
            y           = 1000,
            z           = 14290,
            range       = 2000,
            dword_10    = 0x000009C4,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000015,
        ),
        ScenaEventData(
            x           = 63260,
            y           = 1000,
            z           = 22960,
            range       = 2000,
            dword_10    = 0x000009C4,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000015,
        ),
        ScenaEventData(
            x           = 69910,
            y           = 1000,
            z           = 31710,
            range       = 2000,
            dword_10    = 0x000009C4,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000015,
        ),
        ScenaEventData(
            x           = 42920,
            y           = 0,
            z           = 81110,
            range       = 2000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000016,
        ),
        ScenaEventData(
            x           = 70940,
            y           = 0,
            z           = -9490,
            range       = 2000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000017,
        ),
        ScenaEventData(
            x           = 75010,
            y           = 0,
            z           = 71300,
            range       = 2000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000018,
        ),
    )

# id: 0x10004 offset: 0x42A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 124880,
            triggerZ            = -3500,
            triggerY            = 70940,
            triggerRange        = 800,
            actorX              = 124880,
            actorZ              = -2500,
            actorY              = 70940,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0010,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 75060,
            triggerZ            = 0,
            triggerY            = 71950,
            triggerRange        = 800,
            actorX              = 75060,
            actorZ              = 1000,
            actorY              = 71950,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0012,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 70950,
            triggerZ            = 0,
            triggerY            = -9930,
            triggerRange        = 800,
            actorX              = 70950,
            actorZ              = 1000,
            actorY              = -9930,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0013,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x496
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 5, 0x3FD)),
            Expr.Return,
        ),
        'loc_4AD',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x007F, 5, 0x3FD))
    Event(0, func_0F_10EC)

    def _loc_4AD(): pass

    label('loc_4AD')

    Return()

# id: 0x0001 offset: 0x4AE
@scena.Code('func_01_4AE')
def func_01_4AE():
    OP_16(0x02, 4000, -46000, -90000, 196700)
    OP_72(0x000E, 0x0020)
    OP_72(0x000F, 0x0020)
    OP_6F(0x000E, 118)
    OP_6F(0x000F, 118)
    OP_72(0x0005, 0x0010)
    OP_72(0x0008, 0x0010)
    OP_72(0x0006, 0x0010)
    OP_72(0x0007, 0x0010)
    OP_72(0x0009, 0x0010)
    OP_72(0x000A, 0x0010)
    OP_64(0x00, 0x0001)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 0, 0x630)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_50B',
    )

    OP_72(0x000B, 0x0010)
    OP_65(0x00, 0x0001)

    def _loc_50B(): pass

    label('loc_50B')

    If(
        (
            (Expr.Eval, "OP_42(0x0007)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_51E',
    )

    OP_1B(0x09, 0x00, 0x0011)

    def _loc_51E(): pass

    label('loc_51E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 3, 0x62B)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 6, 0x62E)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_548',
    )

    OP_72(0x0000, 0x0010)
    OP_72(0x0001, 0x0010)
    OP_72(0x0002, 0x0010)
    OP_72(0x0003, 0x0010)
    OP_72(0x000B, 0x0010)
    OP_72(0x0004, 0x0010)

    def _loc_548(): pass

    label('loc_548')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 3, 0x62B)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 6, 0x62E)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_6AC',
    )

    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0012, 0x0080)
    ChrClearFlags(0x0013, 0x0080)
    ChrClearFlags(0x0014, 0x0080)
    ChrClearFlags(0x0015, 0x0080)
    ChrClearFlags(0x0016, 0x0080)
    ChrClearFlags(0x0017, 0x0080)
    CreateThread(0x0008, 0x01, 0x00, func_04_AA1)
    CreateThread(0x000A, 0x01, 0x00, func_04_AA1)
    CreateThread(0x000B, 0x01, 0x00, func_04_AA1)
    CreateThread(0x000C, 0x01, 0x00, func_04_AA1)
    CreateThread(0x000D, 0x01, 0x00, func_04_AA1)
    CreateThread(0x000E, 0x01, 0x00, func_03_82A)
    CreateThread(0x000F, 0x01, 0x00, func_03_82A)
    CreateThread(0x0010, 0x01, 0x00, func_03_82A)
    CreateThread(0x0011, 0x01, 0x00, func_03_82A)
    CreateThread(0x0012, 0x01, 0x00, func_03_82A)
    CreateThread(0x0013, 0x01, 0x00, func_03_82A)
    CreateThread(0x0014, 0x01, 0x00, func_03_82A)
    CreateThread(0x0015, 0x01, 0x00, func_03_82A)
    CreateThread(0x0016, 0x01, 0x00, func_03_82A)
    CreateThread(0x0017, 0x01, 0x00, func_03_82A)

    If(
        (
            (Expr.Eval, "OP_29(0x0048, 0x01, 0x0800)"),
            Expr.Return,
        ),
        'loc_613',
    )

    def _loc_613(): pass

    label('loc_613')

    If(
        (
            (Expr.Eval, "OP_29(0x0048, 0x01, 0x1000)"),
            Expr.Return,
        ),
        'loc_639',
    )

    ChrSetFlags(0x0017, 0x0080)
    TerminateThread(0x0017, 0xFF)
    ChrSetFlags(0x0012, 0x0080)
    TerminateThread(0x0012, 0xFF)
    ChrSetFlags(0x0011, 0x0080)
    TerminateThread(0x0011, 0xFF)

    def _loc_639(): pass

    label('loc_639')

    If(
        (
            (Expr.Eval, "OP_29(0x0048, 0x01, 0x2000)"),
            Expr.Return,
        ),
        'loc_671',
    )

    ChrSetFlags(0x000C, 0x0080)
    TerminateThread(0x000C, 0xFF)
    ChrSetFlags(0x000D, 0x0080)
    TerminateThread(0x000D, 0xFF)
    ChrSetFlags(0x000E, 0x0080)
    TerminateThread(0x000E, 0xFF)
    ChrSetFlags(0x0013, 0x0080)
    TerminateThread(0x0013, 0xFF)
    ChrSetFlags(0x0014, 0x0080)
    TerminateThread(0x0014, 0xFF)

    def _loc_671(): pass

    label('loc_671')

    If(
        (
            (Expr.Eval, "OP_29(0x0048, 0x01, 0x4000)"),
            Expr.Return,
        ),
        'loc_68E',
    )

    ChrSetFlags(0x000F, 0x0080)
    TerminateThread(0x000F, 0xFF)
    ChrSetFlags(0x0016, 0x0080)
    TerminateThread(0x0016, 0xFF)

    def _loc_68E(): pass

    label('loc_68E')

    If(
        (
            (Expr.Eval, "OP_29(0x0048, 0x01, 0x8000)"),
            Expr.Return,
        ),
        'loc_699',
    )

    def _loc_699(): pass

    label('loc_699')

    CameraSetDistance(4200, 0)

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_6AC(): pass

    label('loc_6AC')

    Return()

# id: 0x0002 offset: 0x6AD
@scena.Code('func_02_6AD')
def func_02_6AD():
    ExecExpressionWithReg(
        0x0004,
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
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6D2',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_814')

    def _loc_6D2(): pass

    label('loc_6D2')

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6EB',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_814')

    def _loc_6EB(): pass

    label('loc_6EB')

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_704',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_814')

    def _loc_704(): pass

    label('loc_704')

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_71D',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_814')

    def _loc_71D(): pass

    label('loc_71D')

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_736',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_814')

    def _loc_736(): pass

    label('loc_736')

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_74F',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_814')

    def _loc_74F(): pass

    label('loc_74F')

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_768',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_814')

    def _loc_768(): pass

    label('loc_768')

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_781',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_814')

    def _loc_781(): pass

    label('loc_781')

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_79A',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_814')

    def _loc_79A(): pass

    label('loc_79A')

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7B3',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_814')

    def _loc_7B3(): pass

    label('loc_7B3')

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7CC',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_814')

    def _loc_7CC(): pass

    label('loc_7CC')

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7E5',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_814')

    def _loc_7E5(): pass

    label('loc_7E5')

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7FE',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_814')

    def _loc_7FE(): pass

    label('loc_7FE')

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_814',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_814(): pass

    label('loc_814')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_829',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_814')

    def _loc_829(): pass

    label('loc_829')

    Return()

# id: 0x0003 offset: 0x82A
@scena.Code('func_03_82A')
def func_03_82A():
    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_AA0',
    )

    Yield()

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x151),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_85D',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0xBB8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_97A')

    def _loc_85D(): pass

    label('loc_85D')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x125),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_883',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_97A')

    def _loc_883(): pass

    label('loc_883')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xF8),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_8A9',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_97A')

    def _loc_8A9(): pass

    label('loc_8A9')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xCA),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_8D0',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_97A')

    def _loc_8D0(): pass

    label('loc_8D0')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x9E),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_8F6',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_97A')

    def _loc_8F6(): pass

    label('loc_8F6')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x70),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_91C',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_97A')

    def _loc_91C(): pass

    label('loc_91C')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x44),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_941',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_97A')

    def _loc_941(): pass

    label('loc_941')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x16),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_966',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_97A')

    def _loc_966(): pass

    label('loc_966')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_97A(): pass

    label('loc_97A')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x1),
            (Expr.PushLong, 0xBB8),
            Expr.Add,
            (Expr.PushReg, 0x2),
            Expr.Add,
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Gtr,
            (Expr.GetChrWork, 0xFE, 0x1),
            (Expr.PushLong, 0xBB8),
            Expr.Sub,
            (Expr.PushReg, 0x2),
            Expr.Add,
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Lss,
            Expr.Nez64,
            (Expr.GetChrWork, 0xFE, 0x3),
            (Expr.PushLong, 0xBB8),
            Expr.Add,
            (Expr.PushReg, 0x3),
            Expr.Add,
            (Expr.GetChrWork, 0x0, 0x3),
            Expr.Gtr,
            Expr.Nez64,
            (Expr.GetChrWork, 0xFE, 0x3),
            (Expr.PushLong, 0xBB8),
            Expr.Sub,
            (Expr.PushReg, 0x3),
            Expr.Add,
            (Expr.GetChrWork, 0x0, 0x3),
            Expr.Lss,
            Expr.Nez64,
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_A9D',
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TerminateThread(0x00FE, 0x00)
    EventBegin(0x00)
    ChrTurnDirection(0x0000, 0x00FE, 0)
    ChrTurnDirection(0x0001, 0x00FE, 0)
    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrTurnDirection(0x00FE, 0x0000, 400)
    Sleep(1000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 5, 0x62D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A8E',
    )

    ChrTalk(
        0x00FE,
        (
            '#4190111258V你们是干什么的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111259V#580F（糟糕……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111260V#017F（被发现了吗……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A8E(): pass

    label('loc_A8E')

    SetScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    NewScene('ED6_DT01/T4133._SN', 106, 0, 0)
    IdleLoop()
    EventEnd(0x01)

    Return()

    def _loc_A9D(): pass

    label('loc_A9D')

    Jump('func_03_82A')

    def _loc_AA0(): pass

    label('loc_AA0')

    Return()

# id: 0x0004 offset: 0xAA1
@scena.Code('func_04_AA1')
def func_04_AA1():
    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D17',
    )

    Yield()

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x151),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_AD4',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0xBB8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_BF1')

    def _loc_AD4(): pass

    label('loc_AD4')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x125),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_AFA',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_BF1')

    def _loc_AFA(): pass

    label('loc_AFA')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xF8),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_B20',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_BF1')

    def _loc_B20(): pass

    label('loc_B20')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xCA),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_B47',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_BF1')

    def _loc_B47(): pass

    label('loc_B47')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x9E),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_B6D',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_BF1')

    def _loc_B6D(): pass

    label('loc_B6D')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x70),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_B93',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_BF1')

    def _loc_B93(): pass

    label('loc_B93')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x44),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_BB8',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_BF1')

    def _loc_BB8(): pass

    label('loc_BB8')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x16),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_BDD',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_BF1')

    def _loc_BDD(): pass

    label('loc_BDD')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_BF1(): pass

    label('loc_BF1')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x1),
            (Expr.PushLong, 0xBB8),
            Expr.Add,
            (Expr.PushReg, 0x2),
            Expr.Add,
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Gtr,
            (Expr.GetChrWork, 0xFE, 0x1),
            (Expr.PushLong, 0xBB8),
            Expr.Sub,
            (Expr.PushReg, 0x2),
            Expr.Add,
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Lss,
            Expr.Nez64,
            (Expr.GetChrWork, 0xFE, 0x3),
            (Expr.PushLong, 0xBB8),
            Expr.Add,
            (Expr.PushReg, 0x3),
            Expr.Add,
            (Expr.GetChrWork, 0x0, 0x3),
            Expr.Gtr,
            Expr.Nez64,
            (Expr.GetChrWork, 0xFE, 0x3),
            (Expr.PushLong, 0xBB8),
            Expr.Sub,
            (Expr.PushReg, 0x3),
            Expr.Add,
            (Expr.GetChrWork, 0x0, 0x3),
            Expr.Lss,
            Expr.Nez64,
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_D14',
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TerminateThread(0x00FE, 0x00)
    EventBegin(0x00)
    ChrTurnDirection(0x0000, 0x00FE, 0)
    ChrTurnDirection(0x0001, 0x00FE, 0)
    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrTurnDirection(0x00FE, 0x0000, 400)
    Sleep(1000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 5, 0x62D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_D05',
    )

    ChrTalk(
        0x00FE,
        (
            '#4190111258V你们是干什么的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111259V#580F（糟糕……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111260V#017F（被发现了吗……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D05(): pass

    label('loc_D05')

    SetScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    NewScene('ED6_DT01/T4133._SN', 105, 0, 0)
    IdleLoop()
    EventEnd(0x01)

    Return()

    def _loc_D14(): pass

    label('loc_D14')

    Jump('func_04_AA1')

    def _loc_D17(): pass

    label('loc_D17')

    Return()

# id: 0x0005 offset: 0xD18
@scena.Code('func_05_D18')
def func_05_D18():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_DAD',
    )

    ChrSetPos(0x00FE, 48010, 250, 59980, 270)
    ChrWalkTo(0x00FE, 35200, 250, 59980, 3000, 0x00)
    ChrWalkTo(0x00FE, 48010, 250, 59980, 3000, 0x00)
    ChrWalkTo(0x00FE, 48010, 250, 4310, 3000, 0x00)
    ChrWalkTo(0x00FE, 42030, 250, 4310, 3000, 0x00)
    ChrWalkTo(0x00FE, 48010, 250, 4310, 3000, 0x00)
    ChrWalkTo(0x00FE, 48010, 250, 59980, 3000, 0x00)

    Jump('func_05_D18')

    def _loc_DAD(): pass

    label('loc_DAD')

    Return()

# id: 0x0006 offset: 0xDAE
@scena.Code('func_06_DAE')
def func_06_DAE():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_DF3',
    )

    ChrSetPos(0x00FE, 39910, 0, 63710, 270)
    ChrWalkTo(0x00FE, 89750, 0, 63710, 3000, 0x00)
    ChrWalkTo(0x00FE, 39910, 0, 63710, 3000, 0x00)

    Jump('func_06_DAE')

    def _loc_DF3(): pass

    label('loc_DF3')

    Return()

# id: 0x0007 offset: 0xDF4
@scena.Code('func_07_DF4')
def func_07_DF4():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_E39',
    )

    ChrSetPos(0x00FE, 50960, 0, 16800, 0)
    ChrWalkTo(0x00FE, 50960, 0, 59090, 3000, 0x00)
    ChrWalkTo(0x00FE, 50960, 0, 16800, 3000, 0x00)

    Jump('func_07_DF4')

    def _loc_E39(): pass

    label('loc_E39')

    Return()

# id: 0x0008 offset: 0xE3A
@scena.Code('func_08_E3A')
def func_08_E3A():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_EA7',
    )

    ChrSetPos(0x00FE, 55970, 250, 6050, 0)
    ChrWalkTo(0x00FE, 55970, 250, 58080, 3000, 0x00)
    ChrWalkTo(0x00FE, 84170, 250, 58080, 3000, 0x00)
    ChrWalkTo(0x00FE, 84170, 250, 5990, 3000, 0x00)
    ChrWalkTo(0x00FE, 55970, 250, 6050, 3000, 0x00)

    Jump('func_08_E3A')

    def _loc_EA7(): pass

    label('loc_EA7')

    Return()

# id: 0x0009 offset: 0xEA8
@scena.Code('func_09_EA8')
def func_09_EA8():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_F15',
    )

    ChrSetPos(0x00FE, 53970, 250, 3940, 90)
    ChrWalkTo(0x00FE, 86060, 250, 3940, 3000, 0x00)
    ChrWalkTo(0x00FE, 86060, 250, 59960, 3000, 0x00)
    ChrWalkTo(0x00FE, 53920, 250, 59960, 3000, 0x00)
    ChrWalkTo(0x00FE, 53970, 250, 3940, 3000, 0x00)

    Jump('func_09_EA8')

    def _loc_F15(): pass

    label('loc_F15')

    Return()

# id: 0x000A offset: 0xF16
@scena.Code('func_0A_F16')
def func_0A_F16():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_F5B',
    )

    ChrSetPos(0x00FE, 54120, 250, 67800, 270)
    ChrWalkTo(0x00FE, 95480, 250, 67800, 3000, 0x00)
    ChrWalkTo(0x00FE, 54120, 250, 67800, 3000, 0x00)

    Jump('func_0A_F16')

    def _loc_F5B(): pass

    label('loc_F5B')

    Return()

# id: 0x000B offset: 0xF5C
@scena.Code('func_0B_F5C')
def func_0B_F5C():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_FA1',
    )

    ChrSetPos(0x00FE, 95540, 250, -5740, 90)
    ChrWalkTo(0x00FE, 42710, 250, -5740, 3000, 0x00)
    ChrWalkTo(0x00FE, 95540, 250, -5740, 3000, 0x00)

    Jump('func_0B_F5C')

    def _loc_FA1(): pass

    label('loc_FA1')

    Return()

# id: 0x000C offset: 0xFA2
@scena.Code('func_0C_FA2')
def func_0C_FA2():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_100F',
    )

    ChrSetPos(0x00FE, 42960, 0, -1020, 90)
    ChrWalkTo(0x00FE, 89990, 0, -1020, 3000, 0x00)
    ChrWalkTo(0x00FE, 89990, 0, 58750, 3000, 0x00)
    ChrWalkTo(0x00FE, 89990, 0, -1020, 3000, 0x00)
    ChrWalkTo(0x00FE, 42960, 0, -1020, 3000, 0x00)

    Jump('func_0C_FA2')

    def _loc_100F(): pass

    label('loc_100F')

    Return()

# id: 0x000D offset: 0x1010
@scena.Code('func_0D_1010')
def func_0D_1010():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_107D',
    )

    ChrSetPos(0x00FE, 61020, 1250, 53050, 180)
    ChrWalkTo(0x00FE, 61020, 1250, 37000, 3000, 0x00)
    ChrWalkTo(0x00FE, 79040, 1250, 37000, 3000, 0x00)
    ChrWalkTo(0x00FE, 79040, 1250, 52810, 3000, 0x00)
    ChrWalkTo(0x00FE, 61020, 1250, 53050, 3000, 0x00)

    Jump('func_0D_1010')

    def _loc_107D(): pass

    label('loc_107D')

    Return()

# id: 0x000E offset: 0x107E
@scena.Code('func_0E_107E')
def func_0E_107E():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_10EB',
    )

    ChrSetPos(0x00FE, 77980, 1250, 52000, 180)
    ChrWalkTo(0x00FE, 77980, 1250, 37980, 3000, 0x00)
    ChrWalkTo(0x00FE, 62050, 1250, 37980, 3000, 0x00)
    ChrWalkTo(0x00FE, 62050, 1250, 51960, 3000, 0x00)
    ChrWalkTo(0x00FE, 77980, 1250, 52000, 3000, 0x00)

    Jump('func_0E_107E')

    def _loc_10EB(): pass

    label('loc_10EB')

    Return()

# id: 0x000F offset: 0x10EC
@scena.Code('func_0F_10EC')
def func_0F_10EC():
    EventBegin(0x00)
    CameraMove(39290, 1250, 35000, 0)
    OP_67(0, 10000, -10000, 0)
    CameraSetDistance(2000, 0)
    OP_6C(225000, 0)
    OP_6E(508, 0)
    ChrSetPos(0x0101, 65430, 1250, 36430, 90)
    ChrSetPos(0x0102, 63950, 1250, 36430, 90)
    FadeIn(2000, 0)

    @scena.Lambda('lambda_115C')
    def lambda_115C():
        CameraMove(70100, 250, 42490, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_115C)

    Sleep(4000)

    @scena.Lambda('lambda_1179')
    def lambda_1179():
        ChrWalkTo(0x00FE, 70950, 1250, 38410, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1179)

    @scena.Lambda('lambda_1194')
    def lambda_1194():
        ChrWalkTo(0x00FE, 69800, 1250, 37490, 2900, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1194)

    WaitForThreadExit(0x0101, 0x0001)

    @scena.Lambda('lambda_11B4')
    def lambda_11B4():
        ChrWalkTo(0x00FE, 70660, 250, 42400, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_11B4)

    WaitForThreadExit(0x0102, 0x0001)

    @scena.Lambda('lambda_11D4')
    def lambda_11D4():
        ChrWalkTo(0x00FE, 69570, 250, 42530, 2900, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_11D4)

    WaitForThreadExit(0x0101, 0x0002)
    Fade(1000)
    CameraSetDistance(1330, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010111404V#501F呼……\n',
            '躲避着巡逻的士兵，\n',
            '没想到不知不觉来到这种地方了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010111405V看起来，\n',
            '这边好像已经没有士兵了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020111406V#010F嗯……他们好像都撤退了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111407V夜间巡逻也差不多该结束了。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111408V我们稍微休息一下就回旅馆吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010111409V#006FＯＫ！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1334')
    def lambda_1334():
        OP_67(0, 5350, -10000, 3500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1334)

    @scena.Lambda('lambda_134C')
    def lambda_134C():
        OP_6C(135000, 3500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_134C)

    @scena.Lambda('lambda_135C')
    def lambda_135C():
        CameraMove(73240, 250, 45110, 3500)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_135C)

    @scena.Lambda('lambda_1374')
    def lambda_1374():
        CameraSetDistance(1600, 3500)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_1374)

    @scena.Lambda('lambda_1384')
    def lambda_1384():
        ChrWalkTo(0x00FE, 73240, 250, 44890, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1384)

    Sleep(400)

    @scena.Lambda('lambda_13A4')
    def lambda_13A4():
        ChrWalkTo(0x00FE, 73240, 250, 45860, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_13A4)

    WaitForThreadExit(0x0101, 0x0001)
    ChrSetDirection(0x0101, 270, 400)
    ChrSetFlags(0x0101, 0x0004)
    ChrSetChipByIndex(0x0101, 2)

    @scena.Lambda('lambda_13D5')
    def lambda_13D5():
        ChrJumpTo(0x00FE, 73750, 450, 44890, 700, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_13D5)

    WaitForThreadExit(0x0102, 0x0001)
    ChrSetDirection(0x0102, 270, 400)
    ChrSetFlags(0x0102, 0x0004)
    ChrSetChipByIndex(0x0102, 3)

    @scena.Lambda('lambda_1409')
    def lambda_1409():
        ChrJumpTo(0x00FE, 73750, 450, 45860, 700, 5000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1409)

    WaitForThreadExit(0x0102, 0x0001)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010111410V#007F啊～发生了这么多事，\n',
            '脑子还处于不清醒状态呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0102, 1)

    ChrTalk(
        0x0102,
        (
            '#0020111411V#019F哈哈……确实。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111412V#010F没想到在大圣堂等着我们的人\n',
            '是尤莉亚中尉呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0101, 2)

    ChrTalk(
        0x0101,
        (
            '#0010111413V#501F啊，对了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010111414V约修亚最初认为那个送信的人\n',
            '肯定不是尤莉亚小姐吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010111415V不会是……\n',
            '是我们以前见过的人吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111416V#012F……那是…………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111417V#013F…………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111418V#004F啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010111419V#506F对不起，算我没说。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010111420V犯规了犯规了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111421V#014F艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111422V#007F在约修亚愿意自己说出来之前，\n',
            '是不会问你自己以前经历过的事情的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010111423V#505F虽然我一直在注意这个，\n',
            '不过还是不小心忘记了呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111424V#013F…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111425V艾丝蒂尔，我……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111426V#010F我，和你一起旅行，\n',
            '觉得自己已经变得坚强起来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111427V#004F哎……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0102, 0)
    Sleep(400)

    ChrTalk(
        0x0102,
        (
            '#0020111428V#015F在同一片天空下生活的各种各样的人，\n',
            '各种各样的人生……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111429V无数交织在一起的思念轨迹……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111430V每当感受到这些的时候，\n',
            '就似乎找回了自己丢失的东西……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111431V这种感觉……真美好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111432V#002F……约修亚……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111433V#013F……大概这是错觉吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111434V尽管如此，我也……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111435V#015F我也要感谢和你一起生活的这些日子……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111436V这片天空，以及父亲……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111437V#010F当然还有艾丝蒂尔……你。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111438V#004F约修亚……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0102, 1)
    Sleep(400)

    ChrTalk(
        0x0102,
        (
            '#0020111439V#015F所以……我们就此约定吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111440V如果这次的事情能够结束，\n',
            '父亲平安地回来的话……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111441V#010F我就告诉你我自己以前种种的经历。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010111442V#580F真、真的……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111443V#010F嗯。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111444V就和这片星空做个约定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111445V#008F……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0101, 0)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010111446V#582F#3S……好，决定了！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    @scena.Lambda('lambda_1B2D')
    def lambda_1B2D():
        OP_67(0, 7000, -10000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1B2D)

    @scena.Lambda('lambda_1B45')
    def lambda_1B45():
        OP_6C(115000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1B45)

    @scena.Lambda('lambda_1B55')
    def lambda_1B55():
        CameraSetDistance(1400, 1500)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_1B55)

    Sleep(500)

    ChrSetChipByIndex(0x0101, 65535)

    @scena.Lambda('lambda_1B6F')
    def lambda_1B6F():
        ChrJumpTo(0x00FE, 73000, 250, 44890, 700, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1B6F)

    WaitForThreadExit(0x0101, 0x0001)
    ChrWalkTo(0x0101, 72500, 250, 44890, 2000, 0x00)
    ChrSetSubChip(0x0102, 0)
    WaitForThreadExit(0x0101, 0x0003)

    ChrTalk(
        0x0102,
        (
            '#0020111447V#014F艾丝蒂尔……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010111448V#006F该怎么说呢……\n',
            '沉重的心情一扫而光呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010111449V全部事情结束之后，\n',
            '我也有话想对约修亚说呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111450V#014F哎……啊啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111451V难道是那个烦恼的事情？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111452V#006F对对，就是那个。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010111453V#008F嘿嘿……\n',
            '我已经做好准备了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111454V#014F准备……\n',
            '是很让人烦恼的事情吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111455V#012F那么现在说出来也……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111456V#503F不～行！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010111457V说那种话，是要挑选时机的。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010111458V#007F嗯～\n',
            '虽然现在这气氛相当的好～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111459V#010F？？？\n',
            '虽然不太明白……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111460V#010F为了我们今天的约定，\n',
            '明天的比赛一定不能输……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111461V#509F那当然了！\n',
            '怎么能让那种家伙们阻碍了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010111462V#005F#3S看我用少女的力量，\n',
            '把那些特务兵的家伙通通打飞！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111463V#014F打飞……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111464V#011F……呼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_9E(0x0102, 15, 0, 300, 4000)

    ChrTalk(
        0x0102,
        (
            '#0020111465V#512F呼……啊哈哈哈……！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111466V你……果然……\n',
            '……不愧是父亲的女儿啊……',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111467V#009F什么呀，这样说真是讨厌呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010111468V我跟那样的不良中年到底有哪点像啦？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111469V#019F嗯……是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111470V明天的决赛，\n',
            '我也有取胜的信心了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000007D0)
    FadeOut(2000, 0, -1)
    OP_0D()
    MapSetFlags(0x00100000)
    PlaySE(13, 0x00, 0x64)
    Sleep(2000)

    SetScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    NewScene('ED6_DT01/T4132._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0010 offset: 0x206F
@scena.Code('func_10_206F')
def func_10_206F():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 0, 0x628)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_20C9',
    )

    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门上着锁，无法打开。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Jump('loc_222E')

    def _loc_20C9(): pass

    label('loc_20C9')

    If(
        (
            (Expr.Eval, "OP_42(0x0007)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_21BD',
    )

    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门上着锁，无法打开。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020110945V#010F看起来这里就是艾南先生所说的\n',
            '地下水路的入口了。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020110431V今天已经很晚了，\n',
            '明天再和金先生他们一起进去看看吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FF)

    Jump('loc_222E')

    def _loc_21BD(): pass

    label('loc_21BD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 0, 0x630)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_222E',
    )

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '使用了',
            (TxtCtl.SetColor, 0x2),
            '地下水路的钥匙Ｂ',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    SetScenaFlags(ScenaFlag(0x00C6, 0, 0x630))
    OP_70(0x000B, 60)
    OP_73(0x000B)
    OP_64(0x00, 0x0001)
    OP_71(0x000B, 0x0010)
    TalkEnd(0x00FF)

    def _loc_222E(): pass

    label('loc_222E')

    Return()

# id: 0x0011 offset: 0x222F
@scena.Code('func_11_222F')
def func_11_222F():
    EventBegin(0x02)

    ChrTalk(
        0x0102,
        (
            '#0020110945V#010F看起来这里就是艾南先生所说的\n',
            '地下水路的入口了。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020110431V今天已经很晚了，\n',
            '明天再和金先生他们一起进去看看吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveToRelative(0x0000, -1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x0012 offset: 0x22DA
@scena.Code('func_12_22DA')
def func_12_22DA():
    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门紧紧地关着，无法打开。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0013 offset: 0x232E
@scena.Code('func_13_232E')
def func_13_232E():
    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门紧紧地关着，无法打开。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0014 offset: 0x2382
@scena.Code('func_14_2382')
def func_14_2382():
    OP_13(0x00BA)

    Return()

# id: 0x0015 offset: 0x2386
@scena.Code('func_15_2386')
def func_15_2386():
    OP_13(0x00B1)

    Return()

# id: 0x0016 offset: 0x238A
@scena.Code('func_16_238A')
def func_16_238A():
    OP_13(0x00BB)

    Return()

# id: 0x0017 offset: 0x238E
@scena.Code('func_17_238E')
def func_17_238E():
    OP_13(0x00BC)

    Return()

# id: 0x0018 offset: 0x2392
@scena.Code('func_18_2392')
def func_18_2392():
    OP_13(0x00BD)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
