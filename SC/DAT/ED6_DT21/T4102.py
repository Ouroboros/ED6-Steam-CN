import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T4102_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4102   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4102.x'
    header.mapIndex       = 1
    header.bgm            = 14
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
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
        ('ED6_DT07/CH01680._CH', 'ED6_DT07/CH01680P._CP'),
        ('ED6_DT07/CH01690._CH', 'ED6_DT07/CH01690P._CP'),
        ('ED6_DT07/CH01730._CH', 'ED6_DT07/CH01730P._CP'),
        ('ED6_DT07/CH01731._CH', 'ED6_DT07/CH01731P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH01053._CH', 'ED6_DT07/CH01053P._CP'),
        ('ED6_DT07/CH01153._CH', 'ED6_DT07/CH01153P._CP'),
    ]

# id: 0x10001 offset: 0xEA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '士兵达登',
            x                   = -89010,
            z                   = 250,
            y                   = -1030,
            direction           = 189,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            name                = '比卡',
            x                   = -78290,
            z                   = 0,
            y                   = -2530,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            name                = '夏妮',
            x                   = -40940,
            z                   = 0,
            y                   = -5120,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = -55400,
            z                   = 0,
            y                   = -3050,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0011,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = -78990,
            z                   = 1250,
            y                   = 8029,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0005,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0012,
        ),
        ScenaNpcData(
            name                = '鸽子',
            x                   = 34280,
            z                   = 430,
            y                   = 39120,
            direction           = 240,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0006,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '鸽子',
            x                   = 34280,
            z                   = 430,
            y                   = 39120,
            direction           = 240,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0006,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '鸽子',
            x                   = 34280,
            z                   = 430,
            y                   = 39120,
            direction           = 240,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0006,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '鸽子',
            x                   = 34280,
            z                   = 430,
            y                   = 39120,
            direction           = 240,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0006,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '鸽子',
            x                   = 34280,
            z                   = 430,
            y                   = 39120,
            direction           = 240,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0006,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '鸽子',
            x                   = 34280,
            z                   = 430,
            y                   = 39120,
            direction           = 240,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0006,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            name                = '鸽子',
            x                   = 34280,
            z                   = 430,
            y                   = 39120,
            direction           = 240,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0006,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            name                = '格斯',
            x                   = -44500,
            z                   = 250,
            y                   = -19980,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            name                = '游客',
            x                   = -58590,
            z                   = -3250,
            y                   = -22150,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0115,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0014,
        ),
        ScenaNpcData(
            name                = '游客',
            x                   = -58070,
            z                   = -3250,
            y                   = -23930,
            direction           = 315,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0115,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0015,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = -76190,
            z                   = -3500,
            y                   = -32240,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0016,
        ),
        ScenaNpcData(
            name                = '王都格兰赛尔·北街区',
            x                   = -39960,
            z                   = 0,
            y                   = 43920,
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
            x                   = -7520,
            z                   = 300,
            y                   = -20000,
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
            name                = '王都格兰赛尔·码头',
            x                   = -117000,
            z                   = 0,
            y                   = -4090,
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

# id: 0x10002 offset: 0x34A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x34A
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -63040,
            y           = -3750,
            z           = -33480,
            range       = 2000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000019,
        ),
        ScenaEventData(
            x           = -63390,
            y           = -3750,
            z           = -24940,
            range       = 2000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000001A,
        ),
        ScenaEventData(
            x           = -78840,
            y           = 1250,
            z           = 12430,
            range       = 2000,
            dword_10    = 0x000009C4,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000001B,
        ),
    )

# id: 0x10004 offset: 0x3AA
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -72220,
            triggerZ            = -3180,
            triggerY            = -15630,
            triggerRange        = 800,
            actorX              = -72220,
            actorZ              = -2000,
            actorY              = -15630,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0017,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -76990,
            triggerZ            = -3500,
            triggerY            = -30450,
            triggerRange        = 800,
            actorX              = -76990,
            actorZ              = -2500,
            actorY              = -30450,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0018,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x3F2
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_415',
    )

    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrSetFlags(0x0014, 0x0080)
    ChrSetFlags(0x0015, 0x0080)
    ChrSetFlags(0x0016, 0x0080)

    Jump('loc_45C')

    def _loc_415(): pass

    label('loc_415')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_429',
    )

    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)

    Jump('loc_45C')

    def _loc_429(): pass

    label('loc_429')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_43D',
    )

    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)

    Jump('loc_45C')

    def _loc_43D(): pass

    label('loc_43D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_44B',
    )

    Jump('loc_45C')

    def _loc_44B(): pass

    label('loc_44B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_455',
    )

    Jump('loc_45C')

    def _loc_455(): pass

    label('loc_455')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_45C',
    )

    def _loc_45C(): pass

    label('loc_45C')

    Return()

# id: 0x0001 offset: 0x45D
@scena.Code('func_01_45D')
def func_01_45D():
    OP_16(0x02, 4000, -185000, -131000, 2293853)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 5, 0x1625)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 6, 0x1626)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 4, 0x162C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_48F',
    )

    OP_B1('t4102_y')

    Jump('loc_498')

    def _loc_48F(): pass

    label('loc_48F')

    OP_B1('t4102_n')

    def _loc_498(): pass

    label('loc_498')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4B2',
    )

    OP_71(0x0008, 0x0004)
    OP_72(0x0011, 0x0004)
    OP_64(0x00, 0x0001)

    def _loc_4B2(): pass

    label('loc_4B2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            (Expr.TestScenaFlags, ScenaFlag(0x0300, 6, 0x1806)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4DA',
    )

    OP_10(0x02, 0x00)
    OP_72(0x000F, 0x0004)
    ChrSetPos(0x0008, -91300, 250, -3880, 90)

    Jump('loc_4DF')

    def _loc_4DA(): pass

    label('loc_4DA')

    OP_71(0x000F, 0x0004)

    def _loc_4DF(): pass

    label('loc_4DF')

    OP_64(0x01, 0x0001)

    Return()

# id: 0x0002 offset: 0x4E4
@scena.Code('func_02_4E4')
def func_02_4E4():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_507',
    )

    OP_8D(0x00FE, -83110, 1920, -74690, -5430, 3000)

    Jump('func_02_4E4')

    def _loc_507(): pass

    label('loc_507')

    Return()

# id: 0x0003 offset: 0x508
@scena.Code('func_03_508')
def func_03_508():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_564',
    )

    ChrWalkTo(0x00FE, -40940, 0, -36580, 2500, 0x00)
    ChrWalkTo(0x00FE, -54190, -3750, -36230, 2500, 0x00)
    ChrWalkTo(0x00FE, -54260, 0, -4990, 2500, 0x00)
    ChrWalkTo(0x00FE, -40940, 0, -5120, 2500, 0x00)

    Jump('func_03_508')

    def _loc_564(): pass

    label('loc_564')

    Return()

# id: 0x0004 offset: 0x565
@scena.Code('func_04_565')
def func_04_565():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5E9',
    )

    ChrWalkTo(0x00FE, -39990, 0, -3050, 2000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)
    Sleep(1500)

    ChrSetDirection(0x00FE, 180, 400)
    Sleep(1500)

    ChrWalkTo(0x00FE, -55010, 0, -3050, 2000, 0x00)
    ChrSetDirection(0x00FE, 180, 400)
    Sleep(1500)

    ChrWalkTo(0x00FE, -55910, 0, -3050, 2000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)
    Sleep(1500)

    ChrSetDirection(0x00FE, 270, 400)
    Sleep(1500)

    Jump('func_04_565')

    def _loc_5E9(): pass

    label('loc_5E9')

    Return()

# id: 0x0005 offset: 0x5EA
@scena.Code('func_05_5EA')
def func_05_5EA():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_676',
    )

    ChrWalkTo(0x00FE, -76010, 1250, 8029, 2000, 0x00)
    ChrSetDirection(0x00FE, 180, 400)
    Sleep(1500)

    ChrWalkTo(0x00FE, -78990, 1250, 8029, 2000, 0x00)
    ChrSetDirection(0x00FE, 180, 400)
    Sleep(1500)

    ChrWalkTo(0x00FE, -81900, 1250, 8029, 2000, 0x00)
    ChrSetDirection(0x00FE, 180, 400)
    Sleep(1500)

    ChrWalkTo(0x00FE, -78990, 1250, 8029, 2000, 0x00)
    ChrSetDirection(0x00FE, 180, 400)
    Sleep(1500)

    Jump('func_05_5EA')

    def _loc_676(): pass

    label('loc_676')

    Return()

# id: 0x0006 offset: 0x677
@scena.Code('func_06_677')
def func_06_677():
    ExecExpressionWithValue(
        0x00FE,
        0x28,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetFlags(0x00FE, 0x0040)
    OP_8D(0x00FE, -74920, -1510, -82870, 5610, 0)

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

    def _loc_6AB(): pass

    label('loc_6AB')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_8FD',
    )

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x1),
            (Expr.PushLong, 0x960),
            Expr.Add,
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Gtr,
            (Expr.GetChrWork, 0xFE, 0x1),
            (Expr.PushLong, 0x960),
            Expr.Sub,
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Lss,
            Expr.Nez64,
            (Expr.GetChrWork, 0xFE, 0x3),
            (Expr.PushLong, 0x960),
            Expr.Add,
            (Expr.GetChrWork, 0x0, 0x3),
            Expr.Gtr,
            Expr.Nez64,
            (Expr.GetChrWork, 0xFE, 0x3),
            (Expr.PushLong, 0x960),
            Expr.Sub,
            (Expr.GetChrWork, 0x0, 0x3),
            Expr.Lss,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_8C6',
    )

    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x64),
            Expr.Mod,
            (Expr.PushLong, 0x32),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_77B',
    )

    Sleep(250)

    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x64),
            Expr.Mod,
            (Expr.PushLong, 0x32),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_77B',
    )

    Sleep(500)

    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x64),
            Expr.Mod,
            (Expr.PushLong, 0x32),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_77B',
    )

    Sleep(500)

    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x64),
            Expr.Mod,
            (Expr.PushLong, 0x32),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_77B',
    )

    Sleep(500)

    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x64),
            Expr.Mod,
            (Expr.PushLong, 0x32),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_77B',
    )

    Sleep(500)

    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x64),
            Expr.Mod,
            (Expr.PushLong, 0x32),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_77B',
    )

    Sleep(500)

    def _loc_77B(): pass

    label('loc_77B')

    TerminateThread(0x00FE, 0x01)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_7B6',
    )

    @scena.Lambda('lambda_079A')
    def lambda_079A():
        OP_97(0x00FE, -78980, 14630, 360000, 7000, 0x0001)
        Yield()

        Jump('lambda_079A')

    DispatchAsync2(0x00FE, 0x0001, lambda_079A)

    Jump('loc_7D5')

    def _loc_7B6(): pass

    label('loc_7B6')

    @scena.Lambda('lambda_07BC')
    def lambda_07BC():
        OP_97(0x00FE, -78980, 14630, -360000, 7000, 0x0001)
        Yield()

        Jump('lambda_07BC')

    DispatchAsync2(0x00FE, 0x0001, lambda_07BC)

    def _loc_7D5(): pass

    label('loc_7D5')

    ChrSetChipByIndex(0x00FE, 3)
    ChrClearFlags(0x00FE, 0x0400)
    ChrSetFlags(0x00FE, 0x0004)
    def _loc_7E4(): pass

    label('loc_7E4')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_81C',
    )

    ExecExpressionWithValue(
        0x00FE,
        0x02,
        (
            (Expr.PushLong, 0xC8),
            Expr.Add2,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x2),
            (Expr.PushLong, 0x2328),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_814',
    )

    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 2000)

    Jump('loc_81C')

    def _loc_814(): pass

    label('loc_814')

    Sleep(15)

    Jump('loc_7E4')

    def _loc_81C(): pass

    label('loc_81C')

    ChrSetFlags(0x00FE, 0x0080)
    TerminateThread(0x00FE, 0x01)
    ChrClearFlags(0x00FE, 0x0004)
    ChrSetPos(0x00FE, -78690, 0, -40, 74)
    def _loc_83B(): pass

    label('loc_83B')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_8C3',
    )

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x1),
            (Expr.PushLong, 0x61A8),
            Expr.Add,
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Lss,
            (Expr.GetChrWork, 0xFE, 0x1),
            (Expr.PushLong, 0x61A8),
            Expr.Sub,
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Gtr,
            Expr.Or,
            (Expr.GetChrWork, 0xFE, 0x3),
            (Expr.PushLong, 0x61A8),
            Expr.Add,
            (Expr.GetChrWork, 0x0, 0x3),
            Expr.Lss,
            Expr.Or,
            (Expr.GetChrWork, 0xFE, 0x3),
            (Expr.PushLong, 0x61A8),
            Expr.Sub,
            (Expr.GetChrWork, 0x0, 0x3),
            Expr.Gtr,
            Expr.Or,
            Expr.Return,
        ),
        'loc_8BB',
    )

    ChrClearFlags(0x00FE, 0x0080)
    ChrSetChipByIndex(0x00FE, 4)
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 0)
    ChrClearFlags(0x00FE, 0x0004)
    OP_8D(0x00FE, -74920, -1510, -82870, 5610, 0)

    Jump('loc_8C3')

    def _loc_8BB(): pass

    label('loc_8BB')

    Sleep(500)

    Jump('loc_83B')

    def _loc_8C3(): pass

    label('loc_8C3')

    Jump('loc_8FA')

    def _loc_8C6(): pass

    label('loc_8C6')

    Sleep(100)

    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x14),
            Expr.Mod,
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8FA',
    )

    @scena.Lambda('lambda_08E2')
    def lambda_08E2():
        OP_8D(0x00FE, -74920, -1510, -82870, 5610, 1500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_08E2)

    def _loc_8FA(): pass

    label('loc_8FA')

    Jump('loc_6AB')

    def _loc_8FD(): pass

    label('loc_8FD')

    Return()

# id: 0x0007 offset: 0x8FE
@scena.Code('func_07_8FE')
def func_07_8FE():
    OP_4A(0x00FE, 255)
    TalkBegin(0x00FE)
    OP_62(0x00FE, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x00)
    ChrTurnDirection(0x00FE, 0x0101, 0)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '*chirp chirp*',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)
    OP_4B(0x00FE, 255)

    Return()

# id: 0x0008 offset: 0x93E
@scena.Code('func_08_93E')
def func_08_93E():
    OP_4A(0x00FE, 255)
    TalkBegin(0x00FE)
    OP_62(0x00FE, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrTurnDirection(0x00FE, 0x0101, 0)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '*CHIRP CHIRP!*',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)
    OP_4B(0x00FE, 255)

    Return()

# id: 0x0009 offset: 0x984
@scena.Code('func_09_984')
def func_09_984():
    OP_4A(0x00FE, 255)
    TalkBegin(0x00FE)
    OP_62(0x00FE, 0x00000000, 1900, 0x33, 0x35, 0x000000C8, 0x00)
    ChrTurnDirection(0x00FE, 0x0101, 0)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            'Nyaon? Fumyaaa...',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)
    OP_4B(0x00FE, 255)

    Return()

# id: 0x000A offset: 0x9C8
@scena.Code('func_0A_9C8')
def func_0A_9C8():
    OP_4A(0x00FE, 255)
    TalkBegin(0x00FE)
    OP_62(0x00FE, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    ChrTurnDirection(0x00FE, 0x0101, 0)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '*chirrr...*',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)
    OP_4B(0x00FE, 255)

    Return()

# id: 0x000B offset: 0xA06
@scena.Code('func_0B_A06')
def func_0B_A06():
    OP_4A(0x00FE, 255)
    TalkBegin(0x00FE)
    OP_62(0x00FE, 0x00000000, 2000, 0x14, 0x17, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    ChrTurnDirection(0x00FE, 0x0101, 0)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '*chirp chirp... chirp?*',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)
    OP_4B(0x00FE, 255)

    Return()

# id: 0x000C offset: 0xA55
@scena.Code('func_0C_A55')
def func_0C_A55():
    OP_4A(0x00FE, 255)
    TalkBegin(0x00FE)
    OP_62(0x00FE, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    ChrTurnDirection(0x00FE, 0x0101, 0)
    Sleep(1000)

    UnlockAchievement(0x00, 0x0002, 0x00)

    ChrTalk(
        0x00FE,
        (
            '*chiiiirp?*',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)
    OP_4B(0x00FE, 255)

    Return()

# id: 0x000D offset: 0xA9D
@scena.Code('func_0D_A9D')
def func_0D_A9D():
    OP_4A(0x00FE, 255)
    TalkBegin(0x00FE)
    OP_62(0x00FE, 0x00000000, 1900, 0x2C, 0x2F, 0x00000096, 0x01)
    PlaySE(47, 0x00, 0x64)
    ChrTurnDirection(0x00FE, 0x0101, 0)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '*CHIRP*',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)
    OP_4B(0x00FE, 255)

    Return()

# id: 0x000E offset: 0xADC
@scena.Code('func_0E_ADC')
def func_0E_ADC():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_B38',
    )

    ChrTalk(
        0x00FE,
        (
            '好像在港口能看见那个\n',
            '飘浮的像贝壳一样的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有好几个市民去参观了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D3C')

    def _loc_B38(): pass

    label('loc_B38')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_BBB',
    )

    ChrTalk(
        0x00FE,
        (
            '……竟然搬出导力坦克，\n',
            '搞得还真是大。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '抱歉，现在格兰赛尔港\n',
            '正在进行修复工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '应该还要过一阵子\n',
            '才能进去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D3C')

    def _loc_BBB(): pass

    label('loc_BBB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_C16',
    )

    ChrTalk(
        0x00FE,
        (
            '士兵数量一下子增加了，\n',
            '气氛好像变得很森严。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过签字仪式也是快到了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D3C')

    def _loc_C16(): pass

    label('loc_C16')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_C49',
    )

    ChrTalk(
        0x00FE,
        (
            '已经傍晚了啊……\n',
            '快要交接班了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D3C')

    def _loc_C49(): pass

    label('loc_C49')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_CA0',
    )

    ChrTalk(
        0x00FE,
        (
            '经常能在港口看见\n',
            '钓公师团的家伙们在钓鱼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那一带究竟能钓到什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D3C')

    def _loc_CA0(): pass

    label('loc_CA0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_D3C',
    )

    ChrTalk(
        0x00FE,
        (
            '前边是这个城市的旅游景点之一，\n',
            '格兰赛尔港和仓库街哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就是政变的时候被理查德\n',
            '上校命令封锁的地区。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果有时间的话\n',
            '你们可以去参观一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D3C(): pass

    label('loc_D3C')

    TalkEnd(0x00FE)

    Return()

# id: 0x000F offset: 0xD40
@scena.Code('func_0F_D40')
def func_0F_D40():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_D97',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，在天黑之前\n',
            '必须回家。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '王都的黑夜对大人来说\n',
            '也是暗得可怕的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F88')

    def _loc_D97(): pass

    label('loc_D97')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_DEE',
    )

    ChrTalk(
        0x00FE,
        (
            '情报部的事闹得全城都沸沸扬扬的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在港口的设施工作的\n',
            '家伙们没事吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F88')

    def _loc_DEE(): pass

    label('loc_DEE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_E35',
    )

    ChrTalk(
        0x00FE,
        (
            '午饭吃过了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '西街区这边的咖啡馆\n',
            '可是很不错的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F88')

    def _loc_E35(): pass

    label('loc_E35')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_EAE',
    )

    ChrTalk(
        0x00FE,
        (
            '最近好像有个\n',
            '竖着绿头发的家伙\n',
            '出入大圣堂……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那位小兄弟\n',
            '难道是神职人员？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '似乎有点看不出来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F88')

    def _loc_EAE(): pass

    label('loc_EAE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_F23',
    )

    ChrTalk(
        0x00FE,
        (
            '政变时摩尔根将军的\n',
            '孙女莉安妮好像被\n',
            '绑架过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '竟然把年幼的女孩子当作人质，\n',
            '情报部的作法真是卑鄙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F88')

    def _loc_F23(): pass

    label('loc_F23')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_F88',
    )

    ChrTalk(
        0x00FE,
        (
            '去港口看过了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '港口的卸货频率\n',
            '没有以前高了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在仓库街的作用\n',
            '只是出租仓库。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F88(): pass

    label('loc_F88')

    TalkEnd(0x00FE)

    Return()

# id: 0x0010 offset: 0xF8C
@scena.Code('func_10_F8C')
def func_10_F8C():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_FE7',
    )

    ChrTalk(
        0x00FE,
        (
            '导力器能不能\n',
            '快点恢复呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '想不到没有导力器的\n',
            '生活竟然这么悲惨……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12F0')

    def _loc_FE7(): pass

    label('loc_FE7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_1131',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_1049',
    )

    ChrTalk(
        0x00FE,
        (
            '又发生了凯诺娜上尉的事，\n',
            '西街区这边真是不太平。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要不要搬去南街区呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_112E')

    def _loc_1049(): pass

    label('loc_1049')

    ChrTalk(
        0x00FE,
        (
            '昨天听到这附近\n',
            '有人在争论的声音。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '反正那种时间也有可能\n',
            '是醉汉们在吵架。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '又发生了凯诺娜上尉的事，\n',
            '西街区这边真是不太平。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要不要搬去南街区呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '其实还是北街区最好，不过那儿\n',
            '是王城的黄金地段，房租也高。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_112E(): pass

    label('loc_112E')

    Jump('loc_12F0')

    def _loc_1131(): pass

    label('loc_1131')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_11A8',
    )

    ChrTalk(
        0x00FE,
        (
            '士兵的数量增加了不少呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我也知道在临近签字仪式的\n',
            '现在这也是没办法的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过总觉得有点紧张。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12F0')

    def _loc_11A8(): pass

    label('loc_11A8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_11D2',
    )

    ChrTalk(
        0x00FE,
        (
            '今天的晚饭吃什么呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12F0')

    def _loc_11D2(): pass

    label('loc_11D2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_1261',
    )

    ChrTalk(
        0x00FE,
        (
            '科洛蒂娅会不会\n',
            '出席签字仪式呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '感觉比起让杜南公爵出场，\n',
            '她要受欢迎得多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过科洛蒂娅公主好像\n',
            '很少出现在正式场合。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12F0')

    def _loc_1261(): pass

    label('loc_1261')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_12F0',
    )

    ChrTalk(
        0x00FE,
        (
            '你们好啊，最近怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这个街区有大圣堂、利贝尔通讯社\n',
            '和咖啡馆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '想要安静地度过属于成年人的\n',
            '时间还是只有在西街区才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_12F0(): pass

    label('loc_12F0')

    TalkEnd(0x00FE)

    Return()

# id: 0x0011 offset: 0x12F4
@scena.Code('func_11_12F4')
def func_11_12F4():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1331',
    )

    ChrTalk(
        0x00FE,
        (
            '艾莉茜雅女王\n',
            '应该有办法应对\n',
            '现在的局面……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1481')

    def _loc_1331(): pass

    label('loc_1331')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_13D2',
    )

    ChrTalk(
        0x00FE,
        (
            '王国军好像用军用艇\n',
            '进行了相当大规模的搜索。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然发现了几次目标，\n',
            '不过听说都被甩开了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '竟然能甩开那种军用艇……\n',
            '那机器究竟是谁造的呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1481')

    def _loc_13D2(): pass

    label('loc_13D2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_1462',
    )

    ChrTalk(
        0x00FE,
        (
            '希德中校虽然不好张扬，\n',
            '不过似乎是个相当优秀的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '当士官的水平自不必说，\n',
            '其实他的魔法也很厉害啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是不是感觉有点意外？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1481')

    def _loc_1462(): pass

    label('loc_1462')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1470',
    )

    Jump('loc_1481')

    def _loc_1470(): pass

    label('loc_1470')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_147A',
    )

    Jump('loc_1481')

    def _loc_147A(): pass

    label('loc_147A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_1481',
    )

    def _loc_1481(): pass

    label('loc_1481')

    TalkEnd(0x00FE)

    Return()

# id: 0x0012 offset: 0x1485
@scena.Code('func_12_1485')
def func_12_1485():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_14F3',
    )

    ChrTalk(
        0x00FE,
        (
            '市民对导力停止的反应\n',
            '不一而足。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '反正不管怎样，\n',
            '感觉不方便是肯定的，\n',
            '真希望能早点恢复。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1600')

    def _loc_14F3(): pass

    label('loc_14F3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_153E',
    )

    ChrTalk(
        0x00FE,
        (
            '凯诺娜上尉……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '当年情报部的精英士官\n',
            '竟然落得如此下场。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1600')

    def _loc_153E(): pass

    label('loc_153E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_15E1',
    )

    ChrTalk(
        0x00FE,
        (
            '本部要求我们重点\n',
            '加强西街区这边的警戒。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为大圣堂和利贝尔通讯社\n',
            '收到了恐吓信。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '利贝尔通讯社姑且不论，对大圣堂\n',
            '也寄恐吓信，真是胆大包天。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1600')

    def _loc_15E1(): pass

    label('loc_15E1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_15EF',
    )

    Jump('loc_1600')

    def _loc_15EF(): pass

    label('loc_15EF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_15F9',
    )

    Jump('loc_1600')

    def _loc_15F9(): pass

    label('loc_15F9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_1600',
    )

    def _loc_1600(): pass

    label('loc_1600')

    TalkEnd(0x00FE)

    Return()

# id: 0x0013 offset: 0x1604
@scena.Code('func_13_1604')
def func_13_1604():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1611',
    )

    Jump('loc_1746')

    def _loc_1611(): pass

    label('loc_1611')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_1642',
    )

    ChrTalk(
        0x00FE,
        (
            '听说港口发生了战斗……\n',
            '吓我一跳。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1746')

    def _loc_1642(): pass

    label('loc_1642')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_169E',
    )

    ChrTalk(
        0x00FE,
        (
            '我准备去港口的\n',
            '仓库街散步。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……湖上竟然有港口，\n',
            '总觉得有点不可思议哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1746')

    def _loc_169E(): pass

    label('loc_169E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_16CF',
    )

    ChrTalk(
        0x00FE,
        (
            '看着晚霞为何\n',
            '会让人想流泪呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1746')

    def _loc_16CF(): pass

    label('loc_16CF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_1702',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，那座建筑物\n',
            '就是利贝尔通讯社吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1746')

    def _loc_1702(): pass

    label('loc_1702')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_1746',
    )

    ChrTalk(
        0x00FE,
        (
            '从这里可以对西街区\n',
            '一览无遗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这是我很喜欢的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1746(): pass

    label('loc_1746')

    TalkEnd(0x00FE)

    Return()

# id: 0x0014 offset: 0x174A
@scena.Code('func_14_174A')
def func_14_174A():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1757',
    )

    Jump('loc_1865')

    def _loc_1757(): pass

    label('loc_1757')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_178A',
    )

    ChrTalk(
        0x00FE,
        (
            '我还想去参观呢，\n',
            '可是港口被封锁了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1865')

    def _loc_178A(): pass

    label('loc_178A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_17BD',
    )

    ChrTalk(
        0x00FE,
        (
            '不过你这个人……\n',
            '竟然喝得下黑咖啡。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1865')

    def _loc_17BD(): pass

    label('loc_17BD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_17EC',
    )

    ChrTalk(
        0x00FE,
        (
            '我们在旅行目的地\n',
            '尽聊天了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1865')

    def _loc_17EC(): pass

    label('loc_17EC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_1811',
    )

    ChrTalk(
        0x00FE,
        (
            '啊～哪里有\n',
            '好男人呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1865')

    def _loc_1811(): pass

    label('loc_1811')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_1865',
    )

    ChrTalk(
        0x00FE,
        (
            '两位少女大白天就在露天\n',
            '咖啡馆吃咖喱饭……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵，真像是我们的作风。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1865(): pass

    label('loc_1865')

    TalkEnd(0x00FE)

    Return()

# id: 0x0015 offset: 0x1869
@scena.Code('func_15_1869')
def func_15_1869():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1876',
    )

    Jump('loc_1999')

    def _loc_1876(): pass

    label('loc_1876')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_18A3',
    )

    ChrTalk(
        0x00FE,
        (
            '算了，也没办法。\n',
            '这就叫命运。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1999')

    def _loc_18A3(): pass

    label('loc_18A3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_18F5',
    )

    ChrTalk(
        0x00FE,
        (
            '只有咖啡才有像\n',
            '人生一样的苦味……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '用牛奶和糖掩盖\n',
            '是一种浪费。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1999')

    def _loc_18F5(): pass

    label('loc_18F5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_192E',
    )

    ChrTalk(
        0x00FE,
        (
            '只要开心不就好了。\n',
            '真像是我们的作风。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1999')

    def _loc_192E(): pass

    label('loc_192E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_196D',
    )

    ChrTalk(
        0x00FE,
        (
            '好男人当然有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只不过我们\n',
            '还没遇到而已……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1999')

    def _loc_196D(): pass

    label('loc_196D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_1999',
    )

    ChrTalk(
        0x00FE,
        (
            '把自己说成是少女\n',
            '真像你的作风。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1999(): pass

    label('loc_1999')

    TalkEnd(0x00FE)

    Return()

# id: 0x0016 offset: 0x199D
@scena.Code('func_16_199D')
def func_16_199D():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_19E7',
    )

    ChrTalk(
        0x00FE,
        (
            '下水道可以自由进入。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过请尽量别在\n',
            '里面惹出麻烦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B80')

    def _loc_19E7(): pass

    label('loc_19E7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_1A2B',
    )

    ChrTalk(
        0x00FE,
        (
            '听说情报部\n',
            '私藏了坦克。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '城里没受害\n',
            '真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B80')

    def _loc_1A2B(): pass

    label('loc_1A2B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_1A83',
    )

    ChrTalk(
        0x00FE,
        (
            '城里的警戒工作终于\n',
            '要动真格的了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就连我也不经意地\n',
            '变得警惕起来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B80')

    def _loc_1A83(): pass

    label('loc_1A83')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1AC8',
    )

    ChrTalk(
        0x00FE,
        (
            '……快要到交接班的时间了。\n',
            '这里的警戒工作真无聊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B80')

    def _loc_1AC8(): pass

    label('loc_1AC8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_1B2A',
    )

    ChrTalk(
        0x00FE,
        (
            '也有人把这儿的下水\n',
            '道当作训练场。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过现在只有负责剿灭\n',
            '魔兽的游击士才能进去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B80')

    def _loc_1B2A(): pass

    label('loc_1B2A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_1B80',
    )

    ChrTalk(
        0x00FE,
        (
            '哎呀，你们是游击士吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '进入下水道是可以，\n',
            '不过里面很暗，你们要小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1B80(): pass

    label('loc_1B80')

    TalkEnd(0x00FE)

    Return()

# id: 0x0017 offset: 0x1B84
@scena.Code('func_17_1B84')
def func_17_1B84():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '　　 待售房\n',
            '※可用于经营饮食店',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0018 offset: 0x1BD5
@scena.Code('func_18_1BD5')
def func_18_1BD5():
    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门上着锁。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0019 offset: 0x1C1B
@scena.Code('func_19_1C1B')
def func_19_1C1B():
    OP_13(0x00B8)

    Return()

# id: 0x001A offset: 0x1C1F
@scena.Code('func_1A_1C1F')
def func_1A_1C1F():
    OP_13(0x00B7)

    Return()

# id: 0x001B offset: 0x1C23
@scena.Code('func_1B_1C23')
def func_1B_1C23():
    OP_13(0x00AF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
