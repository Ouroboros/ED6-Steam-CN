import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import R3103_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R3103   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'R3103.x'
    header.mapIndex       = 1
    header.bgm            = 29
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
        ('ED6_DT09/CH10610._CH', 'ED6_DT09/CH10610P._CP'),
        ('ED6_DT09/CH10611._CH', 'ED6_DT09/CH10611P._CP'),
        ('ED6_DT09/CH10080._CH', 'ED6_DT09/CH10080P._CP'),
        ('ED6_DT09/CH10081._CH', 'ED6_DT09/CH10081P._CP'),
        ('ED6_DT09/CH10120._CH', 'ED6_DT09/CH10120P._CP'),
        ('ED6_DT09/CH10121._CH', 'ED6_DT09/CH10121P._CP'),
        ('ED6_DT09/CH10140._CH', 'ED6_DT09/CH10140P._CP'),
        ('ED6_DT09/CH10141._CH', 'ED6_DT09/CH10141P._CP'),
        ('ED6_DT09/CH10620._CH', 'ED6_DT09/CH10620P._CP'),
        ('ED6_DT09/CH10621._CH', 'ED6_DT09/CH10621P._CP'),
        ('ED6_DT09/CH10600._CH', 'ED6_DT09/CH10600P._CP'),
        ('ED6_DT09/CH10601._CH', 'ED6_DT09/CH10601P._CP'),
        ('ED6_DT09/CH10400._CH', 'ED6_DT09/CH10400P._CP'),
        ('ED6_DT09/CH10401._CH', 'ED6_DT09/CH10401P._CP'),
        ('ED6_DT09/CH11210._CH', 'ED6_DT09/CH11210P._CP'),
        ('ED6_DT09/CH11211._CH', 'ED6_DT09/CH11211P._CP'),
        ('ED6_DT09/CH11250._CH', 'ED6_DT09/CH11250P._CP'),
        ('ED6_DT09/CH11251._CH', 'ED6_DT09/CH11251P._CP'),
        ('ED6_DT07/CH01310._CH', 'ED6_DT07/CH01310P._CP'),
        ('ED6_DT07/CH00065._CH', 'ED6_DT07/CH00065P._CP'),
        ('ED6_DT07/CH00152._CH', 'ED6_DT07/CH00152P._CP'),
        ('ED6_DT07/CH00122._CH', 'ED6_DT07/CH00122P._CP'),
        ('ED6_DT27/CH04000._CH', 'ED6_DT27/CH04000P._CP'),
        ('ED6_DT07/CH00130._CH', 'ED6_DT07/CH00130P._CP'),
        ('ED6_DT07/CH00140._CH', 'ED6_DT07/CH00140P._CP'),
        ('ED6_DT06/CH20020._CH', 'ED6_DT06/CH20020P._CP'),
        ('ED6_DT29/CH13070._CH', 'ED6_DT29/CH13070P._CP'),
        ('ED6_DT29/CH13071._CH', 'ED6_DT29/CH13071P._CP'),
        ('ED6_DT07/CH00150._CH', 'ED6_DT07/CH00150P._CP'),
        ('ED6_DT07/CH00120._CH', 'ED6_DT07/CH00120P._CP'),
        ('ED6_DT29/CH13073._CH', 'ED6_DT29/CH13073P._CP'),
        ('ED6_DT07/CH00160._CH', 'ED6_DT07/CH00160P._CP'),
        ('ED6_DT29/CH12110._CH', 'ED6_DT29/CH12110P._CP'),
    ]

# id: 0x10001 offset: 0x1B2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '',
            x                   = -12550,
            z                   = 1000,
            y                   = 46450,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '派斯队长',
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
            name                = '测量仪',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 25,
            chipIndex           = 25,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '魔兽',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 26,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '魔兽',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 26,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '魔兽',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 26,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '魔兽',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 26,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '魔兽',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 26,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '魔兽',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 26,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '',
            x                   = 7230,
            z                   = -10,
            y                   = -35710,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 32,
            chipIndex           = 32,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '蔡斯方向',
            x                   = -53110,
            z                   = 0,
            y                   = -14880,
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
            name                = '沃尔费堡垒方向',
            x                   = 22050,
            z                   = -10,
            y                   = 35970,
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

# id: 0x10002 offset: 0x332
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '',
            x           = -30730,
            z           = -20,
            y           = 28880,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -27870,
            z           = 80,
            y           = 46700,
            word_0C     = 0x00B4,
            word_0E     = 0x000C,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020F,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -14660,
            z           = -80,
            y           = 32810,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -24060,
            z           = 70,
            y           = -7910,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020A,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -10150,
            z           = 10,
            y           = -20920,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020B,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 13270,
            z           = -30,
            y           = -23320,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 15990,
            z           = -10,
            y           = 1090,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 31250,
            z           = 30,
            y           = -6140,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020A,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 39280,
            z           = 20,
            y           = -27110,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020B,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 23510,
            z           = 40,
            y           = -36040,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 10940,
            z           = 10,
            y           = -46410,
            word_0C     = 0x00B4,
            word_0E     = 0x0010,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0211,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -10090,
            z           = 10,
            y           = -39590,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -25680,
            z           = -40,
            y           = -25220,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -29830,
            z           = -90,
            y           = -39580,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -30430,
            z           = -80,
            y           = -45390,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -21410,
            z           = -50,
            y           = -50290,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -22480,
            z           = 30,
            y           = -37550,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x50E
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 7230,
            y           = -500,
            z           = -35710,
            range       = 2000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000006,
        ),
    )

# id: 0x10004 offset: 0x52E
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -12960,
            triggerZ            = -20,
            triggerY            = 45920,
            triggerRange        = 1000,
            actorX              = -12550,
            actorZ              = -20,
            actorY              = 46450,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -24020,
            triggerZ            = -10,
            triggerY            = -43750,
            triggerRange        = 1000,
            actorX              = -24580,
            actorZ              = -10,
            actorY              = -43380,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 17230,
            triggerZ            = 10,
            triggerY            = -7630,
            triggerRange        = 1000,
            actorX              = 17890,
            actorZ              = 10,
            actorY              = -7630,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -12880,
            triggerZ            = -70,
            triggerY            = 37960,
            triggerRange        = 2000,
            actorX              = -12880,
            actorZ              = -70,
            actorY              = 37960,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0009,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x5BE
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 2, 0x1412)),
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 3, 0x1413)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5D1',
    )

    Event(0, func_07_DC0)

    Jump('loc_5F6')

    def _loc_5D1(): pass

    label('loc_5D1')

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x64),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5F6',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 7, 0x1417)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0283, 0, 0x1418)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5F6',
    )

    Event(0, func_08_12C9)

    def _loc_5F6(): pass

    label('loc_5F6')

    Return()

# id: 0x0001 offset: 0x5F7
@scena.Code('func_01_5F7')
def func_01_5F7():
    OP_16(0x02, 4000, -131000, -126000, 2293808)

    ExecExpressionWithVar(
        0x3A,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_624',
    )

    OP_10(0x00, 0x00)
    OP_10(0x03, 0x01)

    def _loc_624(): pass

    label('loc_624')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_636',
    )

    OP_10(0x01, 0x00)
    OP_10(0x04, 0x01)

    def _loc_636(): pass

    label('loc_636')

    If(
        (
            (Expr.PushValueByIndex, 0x29),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            (Expr.Eval, "OP_29(0x006E, 0x00, 0x08)"),
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x006E, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x006E, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_6E5',
    )

    If(
        (
            (Expr.GetChrWork, 0x104, 0x1C),
            (Expr.PushLong, 0x5B),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6E5',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x3),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6E5',
    )

    OP_CE(
        0x00,
        (
            (Expr.PushVar, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Add,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushVar, 0x0),
            (Expr.PushLong, 0xA),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_694',
    )

    OP_28(0x006E, 0x01, 0x0040)

    Jump('loc_6E5')

    def _loc_694(): pass

    label('loc_694')

    If(
        (
            (Expr.PushVar, 0x0),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6A9',
    )

    OP_28(0x006E, 0x01, 0x0020)

    Jump('loc_6E5')

    def _loc_6A9(): pass

    label('loc_6A9')

    If(
        (
            (Expr.PushVar, 0x0),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6BE',
    )

    OP_28(0x006E, 0x01, 0x0010)

    Jump('loc_6E5')

    def _loc_6BE(): pass

    label('loc_6BE')

    If(
        (
            (Expr.PushVar, 0x0),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6D3',
    )

    OP_28(0x006E, 0x01, 0x0008)

    Jump('loc_6E5')

    def _loc_6D3(): pass

    label('loc_6D3')

    If(
        (
            (Expr.PushVar, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6E5',
    )

    OP_28(0x006E, 0x01, 0x0004)

    def _loc_6E5(): pass

    label('loc_6E5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02A1, 0, 0x1508)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6F7',
    )

    OP_6F(0x0000, 0)

    Jump('loc_6FE')

    def _loc_6F7(): pass

    label('loc_6F7')

    OP_6F(0x0000, 60)

    def _loc_6FE(): pass

    label('loc_6FE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02A1, 2, 0x150A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_710',
    )

    OP_6F(0x0001, 0)

    Jump('loc_717')

    def _loc_710(): pass

    label('loc_710')

    OP_6F(0x0001, 60)

    def _loc_717(): pass

    label('loc_717')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02A1, 4, 0x150C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_729',
    )

    OP_6F(0x0002, 0)

    Jump('loc_730')

    def _loc_729(): pass

    label('loc_729')

    OP_6F(0x0002, 60)

    def _loc_730(): pass

    label('loc_730')

    ExecExpressionWithValue(
        0x0011,
        0x24,
        (
            (Expr.PushLong, 0xE7),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001E,
        0x24,
        (
            (Expr.PushLong, 0xBF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0283, 0, 0x1418)),
            (Expr.TestScenaFlags, ScenaFlag(0x0283, 1, 0x1419)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_759',
    )

    OP_65(0x03, 0x0001)

    Jump('loc_75D')

    def _loc_759(): pass

    label('loc_759')

    OP_64(0x03, 0x0001)

    def _loc_75D(): pass

    label('loc_75D')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            (Expr.TestScenaFlags, ScenaFlag(0x0283, 1, 0x1419)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_792',
    )

    OP_72(0x0003, 0x0004)
    OP_72(0x0004, 0x0004)
    OP_72(0x0005, 0x0004)
    OP_72(0x0006, 0x0004)

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x64),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_792',
    )

    PlaySE(158, 0x01, 0x55)

    def _loc_792(): pass

    label('loc_792')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 7, 0x1417)),
            (Expr.TestScenaFlags, ScenaFlag(0x0283, 1, 0x1419)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_7AD',
    )

    ChrSetFlags(0x0014, 0x0080)
    ChrSetFlags(0x0015, 0x0080)
    ChrSetFlags(0x0016, 0x0080)

    def _loc_7AD(): pass

    label('loc_7AD')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_7B9'),
        (-1, 'loc_7C6'),
    )

    def _loc_7B9(): pass

    label('loc_7B9')

    ChrClearFlags(0x0012, 0x0001)
    ChrClearFlags(0x0013, 0x0001)

    Jump('loc_7C6')

    def _loc_7C6(): pass

    label('loc_7C6')

    OP_B2(0x00, 0x00, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            (Expr.TestScenaFlags, ScenaFlag(0x041F, 5, 0x20FD)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_7E1',
    )

    ChrClearFlags(0x0011, 0x0080)
    OP_B2(0x01, 0x00, 0x0080)

    def _loc_7E1(): pass

    label('loc_7E1')

    Return()

# id: 0x0002 offset: 0x7E2
@scena.Code('func_02_7E2')
def func_02_7E2():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_7F7',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_7E2')

    def _loc_7F7(): pass

    label('loc_7F7')

    Return()

# id: 0x0003 offset: 0x7F8
@scena.Code('func_03_7F8')
def func_03_7F8():
    UnlockAchievement(0x02, 0x020A, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02A1, 0, 0x1508)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_990',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0000, 60)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02A1, 1, 0x1509)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8DC',
    )

    ChrSetRGBAMask(0x0008, 255, 255, 255, 0, 0)
    ChrTurnDirection(0x0008, 0x0000, 0)
    ChrMoveToRelativeAsync(0x0008, 0, 1000, 0, 0, 0x00)

    @scena.Lambda('lambda_084F')
    def lambda_084F():
        ChrMoveToRelativeAsync(0x00FE, 0, -1000, 0, 600, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_084F)

    @scena.Lambda('lambda_086A')
    def lambda_086A():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 600)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_086A)

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
    Battle(0x00000214, 0x00000000, 0x00, 0x0000, 0xFF)
    ChrSetFlags(0x0008, 0x0080)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_8B7'),
        (0x00000002, 'loc_8C9'),
        (0x00000001, 'loc_8D9'),
        (-1, 'loc_8DC'),
    )

    def _loc_8B7(): pass

    label('loc_8B7')

    SetScenaFlags(ScenaFlag(0x02A1, 1, 0x1509))
    OP_6F(0x0000, 60)
    Sleep(500)

    Jump('loc_8DC')

    def _loc_8C9(): pass

    label('loc_8C9')

    OP_6F(0x0000, 0)
    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

    def _loc_8D9(): pass

    label('loc_8D9')

    OP_B4(0x00)

    Return()

    def _loc_8DC(): pass

    label('loc_8DC')

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['银耳环'], 1)"),
            Expr.Return,
        ),
        'loc_92B',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['银耳环']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x02A1, 0, 0x1508))

    Jump('loc_98D')

    def _loc_92B(): pass

    label('loc_92B')

    FadeOut(300, 0, 100)

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['银耳环']),
            (TxtCtl.SetColor, 0x0),
            '。 \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['银耳环']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0000, 60)
    OP_70(0x0000, 0)

    def _loc_98D(): pass

    label('loc_98D')

    Jump('loc_9BF')

    def _loc_990(): pass

    label('loc_990')

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
    def _loc_9BF(): pass

    label('loc_9BF')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x9CD
@scena.Code('func_04_9CD')
def func_04_9CD():
    UnlockAchievement(0x02, 0x01F0, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02A1, 2, 0x150A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_AAA',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0001, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['还魂粉'], 1)"),
            Expr.Return,
        ),
        'loc_A41',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['还魂粉']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x02A1, 2, 0x150A))

    Jump('loc_AA7')

    def _loc_A41(): pass

    label('loc_A41')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['还魂粉']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['还魂粉']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0001, 60)
    OP_70(0x0001, 0)

    def _loc_AA7(): pass

    label('loc_AA7')

    Jump('loc_ADB')

    def _loc_AAA(): pass

    label('loc_AAA')

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
    def _loc_ADB(): pass

    label('loc_ADB')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0xAE9
@scena.Code('func_05_AE9')
def func_05_AE9():
    UnlockAchievement(0x02, 0x01F1, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02A1, 4, 0x150C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_BC6',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0002, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['活性之药'], 1)"),
            Expr.Return,
        ),
        'loc_B5D',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['活性之药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x02A1, 4, 0x150C))

    Jump('loc_BC3')

    def _loc_B5D(): pass

    label('loc_B5D')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['活性之药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['活性之药']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0002, 60)
    OP_70(0x0002, 0)

    def _loc_BC3(): pass

    label('loc_BC3')

    Jump('loc_BF7')

    def _loc_BC6(): pass

    label('loc_BC6')

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
    def _loc_BF7(): pass

    label('loc_BF7')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0006 offset: 0xC05
@scena.Code('func_06_C05')
def func_06_C05():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x041F, 5, 0x20FD)),
            Expr.Return,
        ),
        'loc_C0D',
    )

    Return()

    def _loc_C0D(): pass

    label('loc_C0D')

    EventBegin(0x01)

    ExecExpressionWithValue(
        0x0000,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0001,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0002,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0003,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0004,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0005,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0006,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0007,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetSubChip(0x0000, 0)
    ChrSetSubChip(0x0001, 0)
    ChrSetSubChip(0x0002, 0)
    ChrSetSubChip(0x0003, 0)
    ChrSetSubChip(0x0004, 0)
    ChrSetSubChip(0x0005, 0)
    ChrSetSubChip(0x0006, 0)
    ChrSetSubChip(0x0007, 0)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '大型魔兽正在四处游荡中。',
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
        0,
        (
            TXT(0x00, '【消灭它】\n'),
            TXT(0x01, '【放弃】\n'),
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
        (0x00000001, 'loc_CF2'),
        (-1, 'loc_D15'),
    )

    def _loc_CF2(): pass

    label('loc_CF2')

    Fade(500)
    OP_89(0x0000, 1900, 0, -31840, 132)
    OP_69(0x0000, 0)
    OP_30(0x01)
    OP_0D()
    EventEnd(0x00)

    Return()

    def _loc_D15(): pass

    label('loc_D15')

    Battle(0x00000EF4, 0x00000000, 0x00, 0x0000, 0xFF)
    EventBegin(0x01)
    OP_89(0x0000, 1900, 0, -31840, 132)
    OP_69(0x0000, 0)
    OP_30(0x01)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000002, 'loc_D4E'),
        (0x00000001, 'loc_D51'),
        (-1, 'loc_D54'),
    )

    def _loc_D4E(): pass

    label('loc_D4E')

    EventEnd(0x00)

    Return()

    def _loc_D51(): pass

    label('loc_D51')

    OP_B4(0x00)

    Return()

    def _loc_D54(): pass

    label('loc_D54')

    EventBegin(0x01)
    ChrSetFlags(0x0011, 0x0080)
    OP_B2(0x00, 0x00, 0x0080)
    OP_0D()
    Sleep(400)

    PlaySE(23, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '消灭了通缉魔兽！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetScenaFlags(ScenaFlag(0x041F, 5, 0x20FD))
    OP_28(0x00BC, 0x04, 0x10)
    OP_28(0x00BC, 0x04, 0x02)
    OP_28(0x00BC, 0x01, 0x0001)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x00)

    Return()

# id: 0x0007 offset: 0xDC0
@scena.Code('func_07_DC0')
def func_07_DC0():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_DD1',
    )

    Call(0, 0x0017)

    def _loc_DD1(): pass

    label('loc_DD1')

    EventBegin(0x00)
    ChrSetPos(0x0101, 23150, -80, 21080, 180)
    ChrSetPos(0x00F7, 21650, -80, 21380, 180)
    ChrSetPos(0x0105, 23090, -90, 22650, 180)
    ChrSetPos(0x0104, 21790, -90, 22950, 180)
    CameraMove(21860, -140, 20000, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(3250, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeIn(1000, 0)

    @scena.Lambda('lambda_0E63')
    def lambda_0E63():
        OP_94(0x00, 0x00FE, 0x0000, 0x00001194, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0E63)

    Sleep(50)

    @scena.Lambda('lambda_0E7E')
    def lambda_0E7E():
        OP_94(0x00, 0x00FE, 0x0000, 0x00001194, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_0E7E)

    Sleep(50)

    @scena.Lambda('lambda_0E99')
    def lambda_0E99():
        OP_94(0x00, 0x00FE, 0x0000, 0x00001194, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_0E99)

    Sleep(50)

    @scena.Lambda('lambda_0EB4')
    def lambda_0EB4():
        OP_94(0x00, 0x00FE, 0x0000, 0x00001194, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_0EB4)

    @scena.Lambda('lambda_0ECA')
    def lambda_0ECA():
        CameraMove(21860, -140, 18000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0ECA)

    OP_0D()
    ChrSetPos(0x0009, 22030, -60, 30800, 180)
    Sleep(1000)

    ChrTalk(
        0x0009,
        (
            '#3060221002V喂，你们几个！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x00F7, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0105, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0104, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    @scena.Lambda('lambda_0F66')
    def lambda_0F66():
        OP_67(0, 7500, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0F66)

    @scena.Lambda('lambda_0F7E')
    def lambda_0F7E():
        CameraMove(21860, -140, 19500, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0F7E)

    ChrClearFlags(0x0009, 0x0080)

    @scena.Lambda('lambda_0F9B')
    def lambda_0F9B():
        OP_94(0x00, 0x0009, 0x0000, 0x00002328, 0x00000FA0, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0F9B)

    @scena.Lambda('lambda_0FB1')
    def lambda_0FB1():
        ChrSetDirection(0x0105, 0, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_0FB1)

    @scena.Lambda('lambda_0FBF')
    def lambda_0FBF():
        ChrSetDirection(0x0104, 0, 400)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_0FBF)

    Sleep(200)

    @scena.Lambda('lambda_0FD2')
    def lambda_0FD2():
        ChrSetDirection(0x0101, 0, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0FD2)

    @scena.Lambda('lambda_0FE0')
    def lambda_0FE0():
        ChrSetDirection(0x00F7, 0, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_0FE0)

    WaitForThreadExit(0x0009, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0009,
        (
            '#3060221003V#5P太好了，赶上了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010221004V#1004F#2P咦，是队长先生？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060221005V#044F#2P怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3060221006V#5P我把刚才谈的事\n',
            '通知了雷斯顿要塞，\n',
            '却听到了意外的信息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3060221007V#5P我认为必须要告知你们才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010221008V#1015F#2P意外的信息……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000007D0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_1144',
    )

    ChrTalk(
        0x0106,
        (
            '#0050221009V#057F要告知我们？\n',
            '难道说…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1170')

    def _loc_1144(): pass

    label('loc_1144')

    ChrTalk(
        0x0103,
        (
            '#0030221010V#022F要告知我们？\n',
            '难道说…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1170(): pass

    label('loc_1170')

    ChrTalk(
        0x0009,
        (
            '#3060221011V#5P嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3060221012V#5P就在刚才，圣海姆门\n',
            '似乎发生了局部性的地震。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x00F7, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0105, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0104, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010221013V#1005F#2P#3S你、你说什么～！？',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '听到通知的艾丝蒂尔她们\n',
            '火速赶到了圣海姆门。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    NewScene('ED6_DT21/T3401._SN', 106, 0, 0)
    IdleLoop()

    Return()

# id: 0x0008 offset: 0x12C9
@scena.Code('func_08_12C9')
def func_08_12C9():
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
        'loc_12E0',
    )

    Call(0, 0x0017)
    Call(0, 0x0018)

    def _loc_12E0(): pass

    label('loc_12E0')

    CameraMove(-39970, -60, 33280, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(3250, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, -42890, -60, 32770, 90)
    ChrSetPos(0x0107, -43000, 80, 33740, 90)
    ChrSetPos(0x00F7, -44370, 130, 32299, 90)
    ChrSetPos(0x00F9, -44370, -80, 33600, 90)
    FadeIn(1000, 0)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x0283, 0, 0x1418))

    ChrTalk(
        0x0101,
        (
            '#0010230001V#1004F#5P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    Fade(1000)
    CameraMove(-17020, 10, 41980, 0)
    OP_67(0, 11580, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(17000, 0)
    OP_6E(541, 0)
    Sleep(1000)

    @scena.Lambda('lambda_13E1')
    def lambda_13E1():
        CameraMove(-17060, 30, 41950, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_13E1)

    @scena.Lambda('lambda_13F9')
    def lambda_13F9():
        OP_67(0, 8000, -10000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_13F9)

    @scena.Lambda('lambda_1411')
    def lambda_1411():
        OP_6C(45000, 6000)

        ExitThread()

    DispatchAsync(0x00F7, 0x0002, lambda_1411)

    @scena.Lambda('lambda_1421')
    def lambda_1421():
        OP_6E(360, 6000)

        ExitThread()

    DispatchAsync(0x00F7, 0x0003, lambda_1421)

    Sleep(4500)

    ChrSetPos(0x0101, -31130, -30, 40660, 90)
    ChrSetPos(0x0107, -31130, -60, 41260, 90)
    ChrSetPos(0x00F7, -32130, -30, 40260, 90)
    ChrSetPos(0x00F9, -32130, -30, 41360, 90)

    @scena.Lambda('lambda_147A')
    def lambda_147A():
        ChrWalkTo(0x00FE, -22150, -50, 40210, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_147A)

    Sleep(200)

    @scena.Lambda('lambda_149A')
    def lambda_149A():
        ChrWalkTo(0x00FE, -23130, -40, 41260, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_149A)

    Sleep(100)

    @scena.Lambda('lambda_14BA')
    def lambda_14BA():
        ChrWalkTo(0x00FE, -23480, -50, 39050, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_14BA)

    Sleep(200)

    @scena.Lambda('lambda_14DA')
    def lambda_14DA():
        ChrWalkTo(0x00FE, -24380, -50, 40100, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_14DA)

    WaitForThreadExit(0x00F7, 0x0001)
    Fade(1000)
    CameraMove(-23130, -70, 40230, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(3250, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_15F0',
    )

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
            TXT(0x00, '【◇在第一部中找到过资料室的书（第二本）】\n'),
            TXT(0x01, '【◇在第一部中没找到过资料室的书（第二本）】\n'),
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

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_15DE'),
        (0x00000001, 'loc_15E7'),
        (-1, 'loc_15F0'),
    )

    def _loc_15DE(): pass

    label('loc_15DE')

    OP_28(0x002F, 0x01, 0x0008)

    Jump('loc_15F0')

    def _loc_15E7(): pass

    label('loc_15E7')

    OP_28(0x002F, 0x02, 0x0008)

    Jump('loc_15F0')

    def _loc_15F0(): pass

    label('loc_15F0')

    If(
        (
            (Expr.Eval, "OP_29(0x002F, 0x01, 0x0008)"),
            Expr.Return,
        ),
        'loc_167F',
    )

    ChrTalk(
        0x0101,
        (
            '#0010230002V#1006F#5P对了，这里以前\n',
            '藏着资料室的书呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010230003V是『巨石阵』啊。\n',
            '唔～和过去一样，还是那么神秘的石柱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_16E7')

    def _loc_167F(): pass

    label('loc_167F')

    ChrTalk(
        0x0101,
        (
            '#0010230004V#1011F#5P听到『巨石阵』\n',
            '我还以为是什么呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010230005V唔～真是根颇有来历的石柱啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_16E7(): pass

    label('loc_16E7')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1766',
    )

    ChrTalk(
        0x0105,
        (
            '#0060230006V#040F我在书里读到过\n',
            '关于这根石柱的事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060230007V好像它还是在塞姆里亚文明\n',
            '出现前建造的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17DF')

    def _loc_1766(): pass

    label('loc_1766')

    ChrTalk(
        0x0104,
        (
            '#0040230008V#030F嗯，我想大概是比\n',
            '塞姆里亚文明更早的遗迹吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040230009V好像只是单纯地将岩石\n',
            '切割并且竖起来而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_17DF(): pass

    label('loc_17DF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_18F7',
    )

    ChrTalk(
        0x0106,
        (
            '#0050230010V#053F#6P塞姆里亚文明……\n',
            '那个繁荣的古代导力技术文明？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 270, 400)

    ChrTalk(
        0x0101,
        (
            '#0010230011V#1006F#2P『四轮之塔』和\n',
            '王城地下的『封印区域』\n',
            '都是塞姆里亚文明的产物吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x00F7, 0, 400)
    ChrSetDirection(0x0107, 180, 400)

    ChrTalk(
        0x0106,
        (
            '#0050230012V#051F#4P嗯，好像是的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050230013V这确实是和那些\n',
            '完全无关的东西呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A05')

    def _loc_18F7(): pass

    label('loc_18F7')

    ChrTalk(
        0x0103,
        (
            '#0030230014V#026F#6P塞姆里亚文明……\n',
            '那个繁荣的古代导力技术文明是吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 270, 400)

    ChrTalk(
        0x0101,
        (
            '#0010230015V#1006F#2P『四轮之塔』和\n',
            '王城地下的『封印区域』\n',
            '都是塞姆里亚文明的产物吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x00F7, 0, 400)
    ChrSetDirection(0x0107, 180, 400)

    ChrTalk(
        0x0103,
        (
            '#0030230016V#027F#4P嗯，没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030230017V这确实是和那些\n',
            '完全无关的东西呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A05(): pass

    label('loc_1A05')

    ChrTalk(
        0x0107,
        (
            '#0070230018V#560F#5P爷爷说\n',
            '这个地方可以清晰地\n',
            '检测到七耀脉的流动。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070230019V他还说这石柱也可能\n',
            '是带着某种宗教\n',
            '意义被建造的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010230020V#1015F#2P原来如此，也就是说\n',
            '很适合用来调查七耀脉的流动啰。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010230021V不过，测量仪应该\n',
            '设置在什么地方呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0107, 90, 400)

    ChrTalk(
        0x0107,
        (
            '#0070230022V#064F#5P嗯，这个嘛……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1B3D')
    def lambda_1B3D():
        ChrTurnDirection(0x00FE, 0x0107, 400)
        Yield()

        Jump('lambda_1B3D')

    DispatchAsync2(0x0101, 0x0003, lambda_1B3D)

    @scena.Lambda('lambda_1B4E')
    def lambda_1B4E():
        ChrTurnDirection(0x00FE, 0x0107, 400)
        Yield()

        Jump('lambda_1B4E')

    DispatchAsync2(0x00F7, 0x0003, lambda_1B4E)

    @scena.Lambda('lambda_1B5F')
    def lambda_1B5F():
        ChrTurnDirection(0x00FE, 0x0107, 400)
        Yield()

        Jump('lambda_1B5F')

    DispatchAsync2(0x00F9, 0x0003, lambda_1B5F)

    @scena.Lambda('lambda_1B70')
    def lambda_1B70():
        CameraMove(-17140, 30, 41840, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1B70)

    @scena.Lambda('lambda_1B88')
    def lambda_1B88():
        OP_6E(326, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1B88)

    ChrWalkTo(0x0107, -20000, 10, 41260, 3000, 0x00)
    Sleep(500)

    ChrSetDirection(0x0107, 0, 400)
    Sleep(500)

    ChrSetDirection(0x0107, 180, 400)
    Sleep(500)

    ChrWalkTo(0x0107, -16350, -30, 47640, 3000, 0x00)
    Sleep(500)

    ChrSetDirection(0x0107, 90, 400)
    Sleep(500)

    ChrSetDirection(0x0107, 270, 400)
    Sleep(500)

    ChrWalkTo(0x0107, -11490, -30, 42990, 3000, 0x00)
    Sleep(500)

    ChrSetDirection(0x0107, 0, 400)
    Sleep(500)

    ChrSetDirection(0x0107, 180, 400)
    Sleep(500)

    ChrWalkTo(0x0107, -13920, -80, 37960, 3000, 0x00)
    Sleep(500)

    ChrSetDirection(0x0107, 270, 400)
    Sleep(500)

    ChrSetDirection(0x0107, 90, 400)
    Sleep(500)

    Fade(500)
    ChrSetSubChip(0x0107, 0)
    ChrSetChipByIndex(0x0107, 19)
    OP_0D()
    TerminateThread(0x0101, 0x03)
    TerminateThread(0x00F7, 0x03)
    TerminateThread(0x00F9, 0x03)

    ChrTalk(
        0x0107,
        (
            '#0070230023V#060F#5P地面也很结实，\n',
            '也不像是遗迹的地基……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070230024V方位的确认……也没问题了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(500)
    ChrSetSubChip(0x0107, 0)
    ChrSetChipByIndex(0x0107, 65535)
    OP_0D()
    ChrTurnDirection(0x0107, 0x0101, 400)

    ChrTalk(
        0x0107,
        (
            '#0070230025V#061F#5P姐姐。\n',
            '我想这里应该可以哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070230026V现在就开始设置测量仪吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
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
            TXT(0x00, '【设置测量仪】\n'),
            TXT(0x01, '【先不设置】\n'),
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
        'loc_1DF8',
    )

    ChrTalk(
        0x0107,
        (
            '#0070230027V#061F#5P那么\n',
            '进行设置工作了哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070230028V请稍等一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F27')

    def _loc_1DF8(): pass

    label('loc_1DF8')

    ChrTalk(
        0x0107,
        (
            '#0070230029V#064F#5P哎……先不设置吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070230030V#060F那就等准备好以后\n',
            '再来这个地方调查吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070230031V到时再进行设置工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    CameraMove(-22150, -50, 40210, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(3250, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0000, -22150, -50, 40210, 90)
    ChrSetPos(0x0001, -22150, -50, 40210, 90)
    ChrSetPos(0x0002, -22150, -50, 40210, 90)
    ChrSetPos(0x0003, -22150, -50, 40210, 90)
    OP_69(0x0000, 0)
    OP_0D()
    OP_65(0x03, 0x0001)
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

    def _loc_1F27(): pass

    label('loc_1F27')

    FadeOut(1000, 0, -1)
    OP_0D()
    Call(0, 0x000A)

    Return()

# id: 0x0009 offset: 0x1F37
@scena.Code('func_09_1F37')
def func_09_1F37():
    EventBegin(0x00)
    Fade(1000)
    ChrSetPos(0x0101, -13030, -30, 39230, 180)
    ChrSetPos(0x00F7, -13550, -60, 36810, 0)
    ChrSetPos(0x00F9, -15000, -20, 38280, 90)
    ChrSetPos(0x0107, -13800, -80, 38110, 90)
    CameraMove(-13490, -80, 38160, 0)
    OP_67(0, 8580, -10000, 0)
    CameraSetDistance(3120, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
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
            TXT(0x00, '【设置测量仪】\n'),
            TXT(0x01, '【先不设置】\n'),
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
        'loc_206D',
    )

    ChrTalk(
        0x0107,
        (
            '#0070230032V#061F#6P那么\n',
            '进行设置工作了哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070230028V请稍等一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_20FB')

    def _loc_206D(): pass

    label('loc_206D')

    ChrSetDirection(0x0107, 45, 400)

    ChrTalk(
        0x0107,
        (
            '#0070230034V#064F#6P咦……不设置吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070230030V#060F那就等准备好以后\n',
            '再来这个地方调查吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070230031V到时再进行设置工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Return()

    def _loc_20FB(): pass

    label('loc_20FB')

    FadeOut(1000, 0, -1)
    OP_0D()
    Call(0, 0x000A)

    Return()

# id: 0x000A offset: 0x210B
@scena.Code('func_0A_210B')
def func_0A_210B():
    FadeOut(1000, 0, -1)
    ChrSetPos(0x0101, -13030, -30, 39230, 180)
    ChrSetPos(0x00F7, -13550, -60, 36810, 0)
    ChrSetPos(0x00F9, -15000, -20, 38280, 90)
    ChrSetPos(0x0107, -13800, -80, 38110, 90)
    CameraMove(-13490, -80, 38160, 0)
    OP_67(0, 8580, -10000, 0)
    CameraSetDistance(3120, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_72(0x0003, 0x0004)
    OP_72(0x0004, 0x0004)
    Sleep(2000)

    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0107,
        (
            '#0070230037V#061F#6P嗯，这样就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_22F5',
    )

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
            TXT(0x00, '【◇第一次设置测量仪】\n'),
            TXT(0x01, '【◇已经在卡鲁迪亚隧道设置了测量仪】\n'),
            TXT(0x02, '【◇设置了雷斯顿要塞的测量仪】\n'),
            TXT(0x03, '【◇卡鲁迪亚隧道和雷斯顿要塞已设置了测量仪】\n'),
            TXT(0x04, '【◇不变更】\n'),
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

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_22C5'),
        (0x00000001, 'loc_22D1'),
        (0x00000002, 'loc_22DD'),
        (0x00000003, 'loc_22E9'),
        (-1, 'loc_22F5'),
    )

    def _loc_22C5(): pass

    label('loc_22C5')

    ClearScenaFlags(ScenaFlag(0x0283, 1, 0x1419))
    ClearScenaFlags(ScenaFlag(0x0283, 3, 0x141B))
    ClearScenaFlags(ScenaFlag(0x0283, 7, 0x141F))

    Jump('loc_22F5')

    def _loc_22D1(): pass

    label('loc_22D1')

    ClearScenaFlags(ScenaFlag(0x0283, 1, 0x1419))
    SetScenaFlags(ScenaFlag(0x0283, 3, 0x141B))
    ClearScenaFlags(ScenaFlag(0x0283, 7, 0x141F))

    Jump('loc_22F5')

    def _loc_22DD(): pass

    label('loc_22DD')

    ClearScenaFlags(ScenaFlag(0x0283, 1, 0x1419))
    ClearScenaFlags(ScenaFlag(0x0283, 3, 0x141B))
    SetScenaFlags(ScenaFlag(0x0283, 7, 0x141F))

    Jump('loc_22F5')

    def _loc_22E9(): pass

    label('loc_22E9')

    ClearScenaFlags(ScenaFlag(0x0283, 1, 0x1419))
    SetScenaFlags(ScenaFlag(0x0283, 3, 0x141B))
    SetScenaFlags(ScenaFlag(0x0283, 7, 0x141F))

    Jump('loc_22F5')

    def _loc_22F5(): pass

    label('loc_22F5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0283, 3, 0x141B)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0283, 7, 0x141F)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2851',
    )

    ChrTalk(
        0x0101,
        (
            '#0010230038V#1004F#5P哟，组合起来的话\n',
            '原来是这样的啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010230039V#1015F不过……\n',
            '这个像盘子一样的东西是什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0107, 45, 400)

    ChrTalk(
        0x0107,
        (
            '#0070230040V#060F#6P它叫抛物面天线，\n',
            '是个可以集中导力波的天线。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070230041V通过它可以把强力的导力波\n',
            '传送到很远的地方……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070230042V即使在卡鲁迪亚隧道这种地方\n',
            '也都一样可以传送到呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_25C4',
    )

    ChrTalk(
        0x0104,
        (
            '#0040230043V#033F哦……\n',
            '那可是很厉害的东西啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040230044V#030F那么…\n',
            '在市场中也能买到这东西吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0107, 0x0104, 400)

    ChrTalk(
        0x0107,
        (
            '#0070230045V#560F#2P啊，我也不是\n',
            '很清楚呢，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070230046V不过爷爷的发明一般在问世\n',
            '半年后就会在市面贩卖了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040230047V#031F呼，这真令人期待。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_25C1',
    )

    ChrTalk(
        0x0103,
        (
            '#0030230048V#027F#2P哎呀……和你的『本职』有关吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040230049V#035F#5P我听不懂你在说什么呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_25C1(): pass

    label('loc_25C1')

    Jump('loc_2769')

    def _loc_25C4(): pass

    label('loc_25C4')

    ChrTalk(
        0x0105,
        (
            '#0060230050V#044F那个，提妲。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060230051V我以前听说过，导力波遇到障碍物\n',
            '就会减弱，不过……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060230052V这个装置为什么在洞窟这样的地方\n',
            '也可以使用呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0107, 0x0105, 400)

    ChrTalk(
        0x0107,
        (
            '#0070230053V#560F#2P那个，这天线\n',
            '会赋予导力波指向性，\n',
            '所以可以顺利进行传送。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070230054V即使是像洞窟那种地方，\n',
            '导力波似乎也能藉由墙壁反射\n',
            '一路传送到出口。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060230055V#040F原来如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060230056V#041F不愧是拉赛尔博士啊，\n',
            '天才的称号名不虚传。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_2769(): pass

    label('loc_2769')

    ChrTalk(
        0x0101,
        (
            '#0010230057V#1007F#5P唔，到现在还感觉不到\n',
            '这东西到底有多厉害……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010230058V#1006F不过这样一来就可以\n',
            '把地震情报传送出去了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0107, 45, 400)

    ChrTalk(
        0x0107,
        (
            '#0070230059V#560F#6P啊，不。\n',
            '现在还没有启动，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070230060V那我现在就按下开关了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_28B1')

    def _loc_2851(): pass

    label('loc_2851')

    ChrTalk(
        0x0101,
        (
            '#0010230061V#1006F#5P那么只剩下\n',
            '打开开关了对吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070230062V#560F#6P嗯，请等一下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_28B1(): pass

    label('loc_28B1')

    ChrSetDirection(0x0107, 90, 400)
    Sleep(300)

    OP_62(0x00F7, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    OP_20(0x000007D0)

    @scena.Lambda('lambda_28E4')
    def lambda_28E4():
        CameraMove(-13490, -80, 37160, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_28E4)

    ChrSetFlags(0x00F7, 0x0800)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_29C0',
    )

    CreateThread(0x0106, 0x01, 0x00, func_0B_3686)
    Sleep(800)

    ChrTalk(
        0x0106,
        (
            '#0050230063V#054F#5P#3S#15A呀！',
            TxtCtl.Enter,
        ),
    )

    Sleep(500)

    ChrSetDirection(0x00F9, 180, 400)
    Sleep(50)

    ChrSetDirection(0x0107, 180, 400)
    CloseMessageWindow()
    WaitForThreadExit(0x0106, 0x0001)
    OP_62(0x0107, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x0107,
        (
            '#0070230064V#065F#5P啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010230065V#1020F#5P什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0106, 0x07, 0x00, 1500)
    ChrSetChipByIndex(0x0106, 20)
    ChrSetSubChip(0x0106, 0)

    Jump('loc_2A68')

    def _loc_29C0(): pass

    label('loc_29C0')

    CreateThread(0x0103, 0x01, 0x00, func_0C_37CA)
    Sleep(800)

    ChrTalk(
        0x0103,
        (
            '#0030230066V#024F#5P#3S#15A嘿！',
            TxtCtl.Enter,
        ),
    )

    Sleep(500)

    ChrSetDirection(0x00F9, 180, 400)
    Sleep(50)

    ChrSetDirection(0x0107, 180, 400)
    CloseMessageWindow()
    WaitForThreadExit(0x0103, 0x0001)
    OP_62(0x0107, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x0107,
        (
            '#0070230064V#065F#5P啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010230065V#1020F#5P什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2A68(): pass

    label('loc_2A68')

    ChrClearFlags(0x00F7, 0x0800)
    ChrSetDirection(0x0101, 0, 500)
    Fade(250)
    PlaySE(213, 0x00, 0x64)
    ChrSetChipByIndex(0x0101, 22)
    ChrSetSubChip(0x0101, 0)
    OP_0D()

    @scena.Lambda('lambda_2A8F')
    def lambda_2A8F():
        CameraMove(-13490, -80, 38160, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2A8F)

    @scena.Lambda('lambda_2AA7')
    def lambda_2AA7():
        CameraSetDistance(3400, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2AA7)

    ChrSetDirection(0x00F9, 270, 400)
    PlayBGM(41)
    ChrSetRGBAMask(0x000B, 255, 255, 255, 255, 0)
    CreateThread(0x000B, 0x00, 0x00, func_0D_38F0)
    CreateThread(0x000C, 0x00, 0x00, func_0E_3942)
    CreateThread(0x000D, 0x00, 0x00, func_0F_3994)
    CreateThread(0x000E, 0x00, 0x00, func_10_39E6)
    CreateThread(0x000F, 0x00, 0x00, func_11_3A38)
    WaitForThreadExit(0x000B, 0x0000)
    WaitForThreadExit(0x000C, 0x0000)
    WaitForThreadExit(0x000D, 0x0000)
    WaitForThreadExit(0x000E, 0x0000)
    WaitForThreadExit(0x000F, 0x0000)
    WaitForThreadExit(0x0101, 0x0003)
    Sleep(500)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2B6F',
    )

    ChrTalk(
        0x0104,
        (
            '#0040230069V#032F#6P哟……\n',
            '这是从哪儿冒出来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    PlaySE(216, 0x00, 0x64)
    ChrSetChipByIndex(0x0104, 23)
    ChrSetSubChip(0x0104, 0)
    ChrSetChipByIndex(0x0107, 31)
    ChrSetSubChip(0x0107, 0)
    OP_0D()

    Jump('loc_2BBA')

    def _loc_2B6F(): pass

    label('loc_2B6F')

    ChrTalk(
        0x0105,
        (
            '#0060230070V#042F#6P我们被包围了呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    PlaySE(213, 0x00, 0x64)
    ChrSetChipByIndex(0x0105, 24)
    ChrSetSubChip(0x0105, 0)
    ChrSetChipByIndex(0x0107, 31)
    ChrSetSubChip(0x0107, 0)
    OP_0D()

    def _loc_2BBA(): pass

    label('loc_2BBA')

    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_2C20',
    )

    ChrTalk(
        0x0106,
        (
            '#0050230071V#054F#5P看来它们的目标\n',
            '是装置中的结晶回路。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050230072V击溃它们吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2C77')

    def _loc_2C20(): pass

    label('loc_2C20')

    ChrTalk(
        0x0103,
        (
            '#0030230073V#024F#5P看来它们的目标\n',
            '是装置中的结晶回路。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030230074V击退它们吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2C77(): pass

    label('loc_2C77')

    @scena.Lambda('lambda_2C7D')
    def lambda_2C7D():
        CameraSetDistance(2700, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2C7D)

    CreateThread(0x000B, 0x00, 0x00, func_12_3A8A)
    CreateThread(0x000C, 0x00, 0x00, func_13_3AB7)
    CreateThread(0x000D, 0x00, 0x00, func_14_3AE4)
    CreateThread(0x000E, 0x00, 0x00, func_15_3B11)
    CreateThread(0x000F, 0x00, 0x00, func_16_3B3E)
    Sleep(500)

    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x000B, 0xFF)
    TerminateThread(0x000C, 0xFF)
    TerminateThread(0x000D, 0xFF)
    TerminateThread(0x000E, 0xFF)
    TerminateThread(0x000F, 0xFF)
    Battle(0x0000021C, 0x00000000, 0x01, 0x0000, 0xFF)
    EventBegin(0x00)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000D, 0x0080)
    ChrSetFlags(0x000E, 0x0080)
    ChrSetFlags(0x000F, 0x0080)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x00F7, 65535)
    ChrSetChipByIndex(0x0107, 65535)
    ChrSetChipByIndex(0x00F9, 65535)
    ChrSetSubChip(0x0101, 0)
    ChrSetSubChip(0x00F7, 0)
    ChrSetSubChip(0x0107, 0)
    ChrSetSubChip(0x00F9, 0)
    CameraMove(-13490, -80, 38160, 0)
    OP_67(0, 8580, -10000, 0)
    CameraSetDistance(3120, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_72(0x0003, 0x0004)
    OP_72(0x0004, 0x0004)
    ChrSetPos(0x0101, -13030, -30, 39530, 0)
    ChrSetPos(0x00F7, -13550, -60, 36810, 180)
    ChrSetPos(0x00F9, -15000, -20, 38280, 270)
    ChrSetPos(0x0107, -13800, -80, 38110, 180)
    PlayBGM(29)
    Sleep(500)

    FadeIn(2000, 0)
    OP_0D()

    @scena.Lambda('lambda_2DB9')
    def lambda_2DB9():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2DB9)

    Sleep(80)

    @scena.Lambda('lambda_2DCC')
    def lambda_2DCC():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_2DCC)

    Sleep(120)

    @scena.Lambda('lambda_2DDF')
    def lambda_2DDF():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_2DDF)

    WaitForThreadExit(0x00F9, 0x0001)
    Sleep(200)

    @scena.Lambda('lambda_2DF7')
    def lambda_2DF7():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2DF7)

    Sleep(80)

    @scena.Lambda('lambda_2E0A')
    def lambda_2E0A():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_2E0A)

    Sleep(120)

    @scena.Lambda('lambda_2E1D')
    def lambda_2E1D():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_2E1D)

    WaitForThreadExit(0x00F9, 0x0001)
    Sleep(500)

    ChrSetDirection(0x0101, 225, 400)
    ChrTurnDirection(0x00F7, 0x0107, 400)
    ChrTurnDirection(0x00F9, 0x0107, 400)

    ChrTalk(
        0x0101,
        (
            '#0010230075V#1007F#5P唉……\n',
            '总算轰走了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010230076V#1015F唔，第一次见到\n',
            '这样的猿羊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_2EEB',
    )

    ChrTalk(
        0x0106,
        (
            '#0050230077V#552F大概就是艾南先生所说的\n',
            '新品种的魔兽吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F29')

    def _loc_2EEB(): pass

    label('loc_2EEB')

    ChrTalk(
        0x0103,
        (
            '#0030230078V#025F大概就是艾南先生\n',
            '所说的新种类的魔兽吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2F29(): pass

    label('loc_2F29')

    ChrTalk(
        0x0107,
        (
            '#0070230079V#561F#5P真、真吓人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2FD2',
    )

    ChrTalk(
        0x0104,
        (
            '#0040230080V#033F提妲，你没事吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040230081V#031F受伤的话我来帮你包扎，\n',
            '不用客气，只管跟大哥哥说就是了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3036')

    def _loc_2FD2(): pass

    label('loc_2FD2')

    ChrTalk(
        0x0105,
        (
            '#0060230082V#043F提妲你没受伤吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060230083V如果有擦伤什么的我帮你包扎，\n',
            '不用客气尽管说哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3036(): pass

    label('loc_3036')

    ChrTurnDirection(0x0107, 0x00F9, 400)

    ChrTalk(
        0x0107,
        (
            '#0070230084V#067F#2P嘿嘿，我没事的～\n',
            '因为大家都在保护我。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070230085V#560F比起这个……\n',
            '还是得赶紧打开开关才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0107, 90, 400)
    ChrSetDirection(0x0101, 180, 400)
    Fade(500)
    ChrSetSubChip(0x0107, 0)
    ChrSetChipByIndex(0x0107, 19)
    OP_0D()
    Sleep(1000)

    PlaySE(156, 0x00, 0x64)
    Sleep(1000)

    OP_72(0x0005, 0x0004)
    OP_72(0x0006, 0x0004)
    PlaySE(158, 0x01, 0x64)
    OP_24(0x009E, 0x55)
    Sleep(2000)

    Fade(500)
    ChrSetSubChip(0x0107, 0)
    ChrSetChipByIndex(0x0107, 65535)
    OP_0D()
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0283, 3, 0x141B)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0283, 7, 0x141F)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3246',
    )

    ChrTalk(
        0x0107,
        (
            '#0070230086V#061F#6P呼，启动完成。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 225, 400)

    ChrTalk(
        0x0101,
        (
            '#0010230087V#1006F#5P辛苦了，提妲。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010230088V#1015F不过要是刚才的魔兽\n',
            '来袭击装置怎么办？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0107, 45, 400)

    ChrTalk(
        0x0107,
        (
            '#0070230089V#560F#6P啊，那个不用担心。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070230090V因为装置具备了\n',
            '类似路灯的驱赶魔兽功能。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010230091V#1011F#5P是吗，那我就放心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3297')

    def _loc_3246(): pass

    label('loc_3246')

    ChrTalk(
        0x0107,
        (
            '#0070230086V#061F#6P呼，启动完成。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010230093V#1011F#5P辛苦了，提妲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3297(): pass

    label('loc_3297')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0283, 3, 0x141B)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0283, 7, 0x141F)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3364',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_32EA',
    )

    ChrTalk(
        0x0106,
        (
            '#0050230094V#051F好，就这样\n',
            '把剩下的测量仪也设置好吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3324')

    def _loc_32EA(): pass

    label('loc_32EA')

    ChrTalk(
        0x0103,
        (
            '#0030230095V#027F好，就这样\n',
            '继续设置剩余的测量仪吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3324(): pass

    label('loc_3324')

    ChrSetDirection(0x0107, 180, 400)

    @scena.Lambda('lambda_3331')
    def lambda_3331():
        ChrSetDirection(0x00F9, 180, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_3331)

    ChrSetDirection(0x0101, 180, 400)

    ChrTalk(
        0x0101,
        (
            '#0010230096V#1006F#5P明白！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_35DC')

    def _loc_3364(): pass

    label('loc_3364')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0283, 3, 0x141B)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0283, 7, 0x141F)),
            Expr.Ez,
            Expr.Or,
            Expr.Return,
        ),
        'loc_3457',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_33CA',
    )

    ChrTalk(
        0x0106,
        (
            '#0050230097V#051F好，这是第二个了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050230098V去把最后一个也搞定吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3417')

    def _loc_33CA(): pass

    label('loc_33CA')

    ChrTalk(
        0x0103,
        (
            '#0030230099V#526F那这是第二个了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030230100V马上去设置最后一个吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3417(): pass

    label('loc_3417')

    ChrSetDirection(0x0107, 180, 400)

    @scena.Lambda('lambda_3424')
    def lambda_3424():
        ChrSetDirection(0x00F9, 180, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_3424)

    ChrSetDirection(0x0101, 180, 400)

    ChrTalk(
        0x0101,
        (
            '#0010230101V#1006F#5PＯＫ！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_35DC')

    def _loc_3457(): pass

    label('loc_3457')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_34F8',
    )

    ChrTalk(
        0x0106,
        (
            '#0050230102V#051F好，这样一来所有的\n',
            '测量仪都设置完毕了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050230103V老爷子还在等着我们，\n',
            '赶快去中央工房的演算室吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0107, 180, 400)

    @scena.Lambda('lambda_34E6')
    def lambda_34E6():
        ChrSetDirection(0x00F9, 180, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_34E6)

    ChrSetDirection(0x0101, 180, 400)

    Jump('loc_359E')

    def _loc_34F8(): pass

    label('loc_34F8')

    ChrTalk(
        0x0103,
        (
            '#0030230104V#026F那么，这样一来所有的\n',
            '测量仪都设置完毕了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030230105V#020F拉赛尔博士还在等着我们，\n',
            '现在就回中央工房的演算室吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0107, 180, 400)

    @scena.Lambda('lambda_358F')
    def lambda_358F():
        ChrSetDirection(0x00F9, 180, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_358F)

    ChrSetDirection(0x0101, 180, 400)

    def _loc_359E(): pass

    label('loc_359E')

    ChrTalk(
        0x0101,
        (
            '#0010230106V#1006F#5PＯＫ！\n',
            '就在中央工房的５楼吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0087, 0x01, 0x0200)
    def _loc_35DC(): pass

    label('loc_35DC')

    FadeOut(1000, 0, -1)
    OP_0D()
    CameraMove(-14030, -80, 38070, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(3250, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0000, -14030, -80, 38070, 100)
    ChrSetPos(0x0001, -14030, -80, 38070, 100)
    ChrSetPos(0x0002, -14030, -80, 38070, 100)
    ChrSetPos(0x0003, -14030, -80, 38070, 100)
    OP_64(0x03, 0x0001)
    SetScenaFlags(ScenaFlag(0x0283, 1, 0x1419))
    OP_28(0x0087, 0x01, 0x0010)
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x000B offset: 0x3686
@scena.Code('func_0B_3686')
def func_0B_3686():
    LoadEffect(0x01, 'battle\\\\damage1.eff')
    ChrSetPos(0x000B, -15020, 500, 29210, 0)
    ChrClearFlags(0x000B, 0x0080)
    ChrSetChipByIndex(0x000B, 27)

    @scena.Lambda('lambda_36BD')
    def lambda_36BD():
        ChrWalkTo(0x00FE, -13620, 500, 35400, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0000, lambda_36BD)

    @scena.Lambda('lambda_36D8')
    def lambda_36D8():
        OP_99(0x00FE, 0x00, 0x07, 2500)
        Yield()

        Jump('lambda_36D8')

    DispatchAsync2(0x000B, 0x0003, lambda_36D8)

    Fade(250)
    PlaySE(213, 0x00, 0x64)
    ChrSetChipByIndex(0x0106, 28)
    OP_0D()
    Sleep(130)

    ChrSetDirection(0x0106, -180, 600)
    ChrSetChipByIndex(0x0106, 20)
    ChrSetSubChip(0x0106, 0)
    PlaySE(505, 0x00, 0x64)
    ChrSetFlags(0x0106, 0x1000)

    @scena.Lambda('lambda_371B')
    def lambda_371B():
        OP_99(0x0106, 0x00, 0x07, 2500)

        ExitThread()

    DispatchAsync(0x0106, 0x0003, lambda_371B)

    Sleep(80)

    ChrMoveTo(0x0106, -13730, -70, 36000, 15000, 0x00)
    Sleep(220)

    TerminateThread(0x000B, 0x00)
    TerminateThread(0x000B, 0x03)
    PlayEffect(0x01, 0xFF, 0x000B, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    ChrSetFlags(0x000B, 0x0020)
    ChrSetChipByIndex(0x000B, 30)
    ChrSetSubChip(0x000B, 0)
    ChrMoveTo(0x000B, -14510, -110, 31880, 20000, 0x00)

    @scena.Lambda('lambda_37A9')
    def lambda_37A9():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_37A9)

    WaitForThreadExit(0x000B, 0x0002)
    ChrSetFlags(0x000B, 0x0080)
    ChrClearFlags(0x000B, 0x0020)
    ChrClearFlags(0x0106, 0x1000)

    Return()

# id: 0x000C offset: 0x37CA
@scena.Code('func_0C_37CA')
def func_0C_37CA():
    LoadEffect(0x01, 'battle\\\\damage1.eff')
    ChrSetPos(0x000B, -15020, 500, 29210, 0)
    ChrClearFlags(0x000B, 0x0080)
    ChrSetChipByIndex(0x000B, 27)

    @scena.Lambda('lambda_3801')
    def lambda_3801():
        OP_99(0x00FE, 0x00, 0x07, 2500)
        Yield()

        Jump('lambda_3801')

    DispatchAsync2(0x000B, 0x0003, lambda_3801)

    @scena.Lambda('lambda_3814')
    def lambda_3814():
        ChrWalkTo(0x00FE, -13620, 500, 35400, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0000, lambda_3814)

    Fade(250)
    PlaySE(213, 0x00, 0x64)
    ChrSetChipByIndex(0x0103, 29)
    OP_0D()
    Sleep(200)

    ChrSetDirection(0x0103, -180, 600)
    ChrSetChipByIndex(0x0103, 21)
    ChrSetSubChip(0x0103, 0)
    PlaySE(502, 0x00, 0x64)

    @scena.Lambda('lambda_385A')
    def lambda_385A():
        OP_99(0x0103, 0x00, 0x09, 2500)

        ExitThread()

    DispatchAsync(0x0103, 0x0003, lambda_385A)

    Sleep(150)

    TerminateThread(0x000B, 0x00)
    TerminateThread(0x000B, 0x03)
    PlayEffect(0x01, 0xFF, 0x000B, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    ChrSetFlags(0x000B, 0x0020)
    ChrSetChipByIndex(0x000B, 30)
    ChrSetSubChip(0x000B, 0)
    PlaySE(521, 0x00, 0x64)
    ChrMoveTo(0x000B, -14510, 500, 31880, 20000, 0x00)

    @scena.Lambda('lambda_38D4')
    def lambda_38D4():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_38D4)

    WaitForThreadExit(0x000B, 0x0002)
    ChrSetFlags(0x000B, 0x0080)
    ChrClearFlags(0x000B, 0x0020)

    Return()

# id: 0x000D offset: 0x38F0
@scena.Code('func_0D_38F0')
def func_0D_38F0():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetFlags(0x00FE, 0x0040)
    ChrSetPos(0x00FE, -16470, 170, 27650, 315)
    ChrSetChipByIndex(0x00FE, 27)
    ChrWalkTo(0x00FE, -15610, 0, 31530, 5000, 0x00)
    ChrSetChipByIndex(0x00FE, 26)
    ChrSetSubChip(0x00FE, 0)

    @scena.Lambda('lambda_3934')
    def lambda_3934():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_3934')

    DispatchAsync2(0x00FE, 0x0003, lambda_3934)

    Return()

# id: 0x000E offset: 0x3942
@scena.Code('func_0E_3942')
def func_0E_3942():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetFlags(0x00FE, 0x0040)
    ChrSetPos(0x00FE, -23080, -30, 31340, 23)
    ChrSetChipByIndex(0x00FE, 27)
    ChrWalkTo(0x00FE, -18250, 0, 35320, 5000, 0x00)
    ChrSetChipByIndex(0x00FE, 26)
    ChrSetSubChip(0x00FE, 0)

    @scena.Lambda('lambda_3986')
    def lambda_3986():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_3986')

    DispatchAsync2(0x00FE, 0x0003, lambda_3986)

    Return()

# id: 0x000F offset: 0x3994
@scena.Code('func_0F_3994')
def func_0F_3994():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetFlags(0x00FE, 0x0040)
    ChrSetPos(0x00FE, -22800, -20, 42870, 122)
    ChrSetChipByIndex(0x00FE, 27)
    ChrWalkTo(0x00FE, -18090, 0, 40000, 5000, 0x00)
    ChrSetChipByIndex(0x00FE, 26)
    ChrSetSubChip(0x00FE, 0)

    @scena.Lambda('lambda_39D8')
    def lambda_39D8():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_39D8')

    DispatchAsync2(0x00FE, 0x0003, lambda_39D8)

    Return()

# id: 0x0010 offset: 0x39E6
@scena.Code('func_10_39E6')
def func_10_39E6():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetFlags(0x00FE, 0x0040)
    ChrSetPos(0x00FE, -9450, -50, 48040, 199)
    ChrSetChipByIndex(0x00FE, 27)
    ChrWalkTo(0x00FE, -12090, 0, 42770, 5000, 0x00)
    ChrSetChipByIndex(0x00FE, 26)
    ChrSetSubChip(0x00FE, 0)

    @scena.Lambda('lambda_3A2A')
    def lambda_3A2A():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_3A2A')

    DispatchAsync2(0x00FE, 0x0003, lambda_3A2A)

    Return()

# id: 0x0011 offset: 0x3A38
@scena.Code('func_11_3A38')
def func_11_3A38():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetFlags(0x00FE, 0x0040)
    ChrSetPos(0x00FE, -250, -20, 34650, 281)
    ChrSetChipByIndex(0x00FE, 27)
    ChrWalkTo(0x00FE, -9360, 0, 35260, 5000, 0x00)
    ChrSetChipByIndex(0x00FE, 26)
    ChrSetSubChip(0x00FE, 0)

    @scena.Lambda('lambda_3A7C')
    def lambda_3A7C():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_3A7C')

    DispatchAsync2(0x00FE, 0x0003, lambda_3A7C)

    Return()

# id: 0x0012 offset: 0x3A8A
@scena.Code('func_12_3A8A')
def func_12_3A8A():
    ChrSetChipByIndex(0x00FE, 27)

    @scena.Lambda('lambda_3A95')
    def lambda_3A95():
        OP_99(0x00FE, 0x00, 0x07, 2500)
        Yield()

        Jump('lambda_3A95')

    DispatchAsync2(0x00FE, 0x0003, lambda_3A95)

    ChrWalkTo(0x00FE, -14130, -70, 35390, 5000, 0x00)

    Return()

# id: 0x0013 offset: 0x3AB7
@scena.Code('func_13_3AB7')
def func_13_3AB7():
    ChrSetChipByIndex(0x00FE, 27)

    @scena.Lambda('lambda_3AC2')
    def lambda_3AC2():
        OP_99(0x00FE, 0x00, 0x07, 2500)
        Yield()

        Jump('lambda_3AC2')

    DispatchAsync2(0x00FE, 0x0003, lambda_3AC2)

    ChrWalkTo(0x00FE, -16870, -70, 36110, 5000, 0x00)

    Return()

# id: 0x0014 offset: 0x3AE4
@scena.Code('func_14_3AE4')
def func_14_3AE4():
    ChrSetChipByIndex(0x00FE, 27)

    @scena.Lambda('lambda_3AEF')
    def lambda_3AEF():
        OP_99(0x00FE, 0x00, 0x07, 2500)
        Yield()

        Jump('lambda_3AEF')

    DispatchAsync2(0x00FE, 0x0003, lambda_3AEF)

    ChrWalkTo(0x00FE, -15880, 0, 38710, 5000, 0x00)

    Return()

# id: 0x0015 offset: 0x3B11
@scena.Code('func_15_3B11')
def func_15_3B11():
    ChrSetChipByIndex(0x00FE, 27)

    @scena.Lambda('lambda_3B1C')
    def lambda_3B1C():
        OP_99(0x00FE, 0x00, 0x07, 2500)
        Yield()

        Jump('lambda_3B1C')

    DispatchAsync2(0x00FE, 0x0003, lambda_3B1C)

    ChrWalkTo(0x00FE, -12660, 0, 41010, 5000, 0x00)

    Return()

# id: 0x0016 offset: 0x3B3E
@scena.Code('func_16_3B3E')
def func_16_3B3E():
    ChrSetChipByIndex(0x00FE, 27)

    @scena.Lambda('lambda_3B49')
    def lambda_3B49():
        OP_99(0x00FE, 0x00, 0x07, 2500)
        Yield()

        Jump('lambda_3B49')

    DispatchAsync2(0x00FE, 0x0003, lambda_3B49)

    ChrWalkTo(0x00FE, -12210, -50, 35830, 5000, 0x00)

    Return()

# id: 0x0017 offset: 0x3B6B
@scena.Code('func_17_3B6B')
def func_17_3B6B():
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
        (0x00000000, 'loc_3BE5'),
        (0x00000001, 'loc_3BEB'),
        (-1, 'loc_3BF1'),
    )

    def _loc_3BE5(): pass

    label('loc_3BE5')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_3BF1')

    def _loc_3BEB(): pass

    label('loc_3BEB')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_3BF1')

    def _loc_3BF1(): pass

    label('loc_3BF1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_3BFF',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    Jump('loc_3C03')

    def _loc_3BFF(): pass

    label('loc_3BFF')

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    def _loc_3C03(): pass

    label('loc_3C03')

    Return()

# id: 0x0018 offset: 0x3C04
@scena.Code('func_18_3C04')
def func_18_3C04():
    MapClearFlags(0x00000001)
    CameraMove(0, 0, 0, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_3C3E',
    )

    FadeIn(0, 0)

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['雪拉扎德'],
            ChrTable['提妲'],
            0x00FF,
        ),
        (
            ChrTable['奥利维尔'],
            ChrTable['科洛丝'],
            0xFFFF,
        ),
    )

    Jump('loc_3C58')

    def _loc_3C3E(): pass

    label('loc_3C3E')

    FadeIn(0, 0)

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['阿加特'],
            ChrTable['提妲'],
            0x00FF,
        ),
        (
            ChrTable['奥利维尔'],
            ChrTable['科洛丝'],
            0xFFFF,
        ),
    )

    def _loc_3C58(): pass

    label('loc_3C58')

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
