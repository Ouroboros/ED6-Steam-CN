import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T2710_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2710   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'T2710.x'
    header.mapIndex       = 1
    header.bgm            = 16
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT01/T2710._SN', 'ED6_DT01/T2710_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
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
        ('ED6_DT07/CH01310._CH', 'ED6_DT07/CH01310P._CP'),
        ('ED6_DT07/CH01300._CH', 'ED6_DT07/CH01300P._CP'),
        ('ED6_DT07/CH01220._CH', 'ED6_DT07/CH01220P._CP'),
        ('ED6_DT07/CH01050._CH', 'ED6_DT07/CH01050P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT07/CH00010._CH', 'ED6_DT07/CH00010P._CP'),
        ('ED6_DT07/CH02140._CH', 'ED6_DT07/CH02140P._CP'),
        ('ED6_DT07/CH02470._CH', 'ED6_DT07/CH02470P._CP'),
        ('ED6_DT07/CH01270._CH', 'ED6_DT07/CH01270P._CP'),
        ('ED6_DT07/CH00100._CH', 'ED6_DT07/CH00100P._CP'),
        ('ED6_DT07/CH00101._CH', 'ED6_DT07/CH00101P._CP'),
        ('ED6_DT07/CH02490._CH', 'ED6_DT07/CH02490P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01043._CH', 'ED6_DT07/CH01043P._CP'),
    ]

# id: 0x10001 offset: 0x11A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '哈恩队长',
            x                   = 4750,
            z                   = 0,
            y                   = 90620,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '基恩茨副长',
            x                   = -2750,
            z                   = 0,
            y                   = 11470,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '士兵库隆',
            x                   = -4800,
            z                   = 0,
            y                   = 7900,
            direction           = 90,
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
            name                = '梅尔凯斯',
            x                   = -770,
            z                   = 0,
            y                   = 21500,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            name                = '琳塞',
            x                   = -770,
            z                   = 0,
            y                   = 22500,
            direction           = 0,
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
            name                = '巴拉特',
            x                   = -770,
            z                   = 0,
            y                   = 23500,
            direction           = 0,
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
            name                = '约修亚',
            x                   = 52155,
            z                   = -3000,
            y                   = 17688,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '目标用摄像机',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0080,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '杜南公爵',
            x                   = 20000,
            z                   = 0,
            y                   = 10000,
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
            name                = '管家菲利普',
            x                   = 4500,
            z                   = 5000,
            y                   = 0,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '塞萨尔',
            x                   = 95300,
            z                   = 0,
            y                   = 16000,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '加雷利',
            x                   = -3800,
            z                   = 0,
            y                   = 24700,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            name                = '蒂雅',
            x                   = 400,
            z                   = 0,
            y                   = 19200,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            name                = '士兵奥塔',
            x                   = 93480,
            z                   = 0,
            y                   = 85530,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
    )

# id: 0x10002 offset: 0x2DA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x2DA
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -6779,
            y           = -1000,
            z           = 1610,
            range       = -5847,
            dword_10    = 0x00000BB8,
            dword_14    = 0x0000189C,
            dword_18    = 0x00010000,
            dword_1C    = 0x00000019,
        ),
        ScenaEventData(
            x           = -3939,
            y           = -1000,
            z           = 1820,
            range       = 2122,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000011,
        ),
    )

# id: 0x10004 offset: 0x31A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -2990,
            triggerZ            = 0,
            triggerY            = 7710,
            triggerRange        = 1000,
            actorX              = -4800,
            actorZ              = 1500,
            actorY              = 7900,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000B,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 95800,
            triggerZ            = 0,
            triggerY            = 13660,
            triggerRange        = 1000,
            actorX              = 95300,
            actorZ              = 1500,
            actorY              = 16000,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0009,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 93600,
            triggerZ            = 0,
            triggerY            = 87450,
            triggerRange        = 1000,
            actorX              = 93480,
            actorZ              = 1500,
            actorY              = 85530,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000F,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x386
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_3A9',
    )

    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000D, 0x0080)
    ChrSetFlags(0x0013, 0x0080)
    ChrSetFlags(0x0014, 0x0080)

    Jump('loc_6FE')

    def _loc_3A9(): pass

    label('loc_3A9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_3CC',
    )

    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000D, 0x0080)
    ChrSetFlags(0x0013, 0x0080)
    ChrSetFlags(0x0014, 0x0080)

    Jump('loc_6FE')

    def _loc_3CC(): pass

    label('loc_3CC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_3EF',
    )

    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000D, 0x0080)
    ChrSetFlags(0x0013, 0x0080)
    ChrSetFlags(0x0014, 0x0080)

    Jump('loc_6FE')

    def _loc_3EF(): pass

    label('loc_3EF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_412',
    )

    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000D, 0x0080)
    ChrSetFlags(0x0013, 0x0080)
    ChrSetFlags(0x0014, 0x0080)

    Jump('loc_6FE')

    def _loc_412(): pass

    label('loc_412')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_435',
    )

    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000D, 0x0080)
    ChrSetFlags(0x0013, 0x0080)
    ChrSetFlags(0x0014, 0x0080)

    Jump('loc_6FE')

    def _loc_435(): pass

    label('loc_435')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 1, 0x501)),
            Expr.Return,
        ),
        'loc_48B',
    )

    ChrSetPos(0x0008, 4750, 0, 90620, 0)
    ChrSetPos(0x000A, -4800, 0, 7900, 90)
    ChrSetPos(0x0009, 2900, 0, 95100, 90)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000D, 0x0080)
    ChrSetFlags(0x0013, 0x0080)
    ChrSetFlags(0x0014, 0x0080)

    Jump('loc_6FE')

    def _loc_48B(): pass

    label('loc_48B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_680',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0023, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_518',
    )

    ChrSetPos(0x0008, -2810, 0, 92600, 270)
    ChrSetPos(0x0009, 96840, 0, 14020, 339)
    ChrSetPos(0x000B, -3090, 0, 18660, 270)
    ChrSetPos(0x000C, -3860, 0, 19770, 270)
    ChrSetPos(0x000D, -2570, 0, 23890, 315)
    TerminateThread(0x0013, 0xFF)
    ChrSetChipByIndex(0x0013, 13)
    ChrSetFlags(0x0013, 0x0004)
    ChrSetFlags(0x0013, 0x0010)
    ChrSetPos(0x0013, 95610, 200, 7550, 180)

    Jump('loc_67D')

    def _loc_518(): pass

    label('loc_518')

    If(
        (
            (Expr.Eval, "OP_29(0x0023, 0x01, 0x1000)"),
            Expr.Return,
        ),
        'loc_5F2',
    )

    ChrSetPos(0x0008, 0, 0, 5250, 0)
    ChrSetFlags(0x0008, 0x0010)
    ChrSetPos(0x000A, 92510, 0, 9380, 69)
    ChrSetPos(0x0009, 92630, 0, 12500, 90)
    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x000E, -680, 0, 5220, 0)
    ChrSetPos(0x0013, 320, 0, 23610, 176)
    ChrSetPos(0x0014, -3790, 0, 19850, 141)
    ChrSetPos(0x000B, 0, 0, 6230, 270)
    ChrSetPos(0x000C, 670, 0, 5960, 270)
    ChrSetPos(0x000D, -800, 0, 5880, 315)
    CreateThread(0x000B, 0x01, 0x01, func_08_1B2E)
    CreateThread(0x000C, 0x01, 0x01, func_09_24E3)
    CreateThread(0x000D, 0x01, 0x01, func_0A_24E8)
    ChrSetFlags(0x000B, 0x0010)
    ChrSetFlags(0x000C, 0x0010)
    ChrSetFlags(0x000D, 0x0010)
    ChrSetFlags(0x0008, 0x0010)

    Jump('loc_67D')

    def _loc_5F2(): pass

    label('loc_5F2')

    ChrSetPos(0x000B, 1596, 0, 12441, 90)
    ChrSetPos(0x000C, 1513, 0, 13617, 90)
    ChrSetPos(0x000D, 909, 0, 13169, 90)
    ChrSetFlags(0x000B, 0x0010)
    ChrSetFlags(0x000C, 0x0010)
    ChrSetFlags(0x000D, 0x0010)
    ChrSetPos(0x0013, 320, 0, 23610, 176)
    ChrSetPos(0x0014, -3790, 0, 19850, 141)
    ChrSetPos(0x000A, 92510, 0, 9380, 69)
    ChrSetPos(0x0009, 92630, 0, 12500, 90)
    ChrSetFlags(0x0008, 0x0080)

    def _loc_67D(): pass

    label('loc_67D')

    Jump('loc_6FE')

    def _loc_680(): pass

    label('loc_680')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_6FE',
    )

    ChrSetPos(0x0008, 1970, 0, 94650, 270)
    ChrSetPos(0x000A, -50, 0, 94650, 90)
    ChrSetFlags(0x0008, 0x0010)
    ChrSetFlags(0x000A, 0x0010)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetPos(0x000C, -3860, 0, 19770, 270)
    ChrSetPos(0x000D, -2570, 0, 23890, 315)
    TerminateThread(0x0013, 0xFF)
    ChrSetChipByIndex(0x0013, 13)
    ChrSetFlags(0x0013, 0x0004)
    ChrSetFlags(0x0013, 0x0010)
    ChrSetPos(0x0013, 95610, 200, 7550, 180)

    def _loc_6FE(): pass

    label('loc_6FE')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_716'),
        (0x00000065, 'loc_787'),
        (0x00000066, 'loc_7A8'),
        (0x00000067, 'loc_7FC'),
        (-1, 'loc_829'),
    )

    def _loc_716(): pass

    label('loc_716')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            (Expr.Eval, "OP_29(0x0023, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0023, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_784',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0023, 0x01, 0x8000)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_746',
    )

    OP_28(0x0023, 0x01, 0x8000)
    Event(1, 0x0000)

    Jump('loc_784')

    def _loc_746(): pass

    label('loc_746')

    If(
        (
            (Expr.Eval, "OP_29(0x0023, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_784',
    )

    ChrSetPos(0x000B, 1596, 0, 12441, 90)
    ChrSetPos(0x000C, 1513, 0, 13617, 90)
    ChrSetPos(0x000D, 909, 0, 13169, 90)

    def _loc_784(): pass

    label('loc_784')

    Jump('loc_829')

    def _loc_787(): pass

    label('loc_787')

    If(
        (
            (Expr.Eval, "OP_29(0x0023, 0x00, 0x08)"),
            (Expr.Eval, "OP_29(0x0023, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0023, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_7A5',
    )

    Event(1, 0x0001)

    def _loc_7A5(): pass

    label('loc_7A5')

    Jump('loc_829')

    def _loc_7A8(): pass

    label('loc_7A8')

    If(
        (
            (Expr.Eval, "OP_29(0x0023, 0x01, 0x0008)"),
            (Expr.Eval, "OP_29(0x0023, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0023, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_7D2',
    )

    FormationAddMember(0x01, 0xFF)
    OP_28(0x0023, 0x04, 0x10)
    Event(1, 0x0017)

    Jump('loc_7F9')

    def _loc_7D2(): pass

    label('loc_7D2')

    If(
        (
            (Expr.Eval, "OP_29(0x0023, 0x01, 0x0010)"),
            (Expr.Eval, "OP_29(0x0023, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0023, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_7F9',
    )

    FormationAddMember(0x01, 0xFF)
    OP_28(0x0023, 0x04, 0x10)
    Event(1, 0x0018)

    def _loc_7F9(): pass

    label('loc_7F9')

    Jump('loc_829')

    def _loc_7FC(): pass

    label('loc_7FC')

    If(
        (
            (Expr.Eval, "OP_29(0x0023, 0x00, 0x08)"),
            (Expr.Eval, "OP_29(0x0023, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0023, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_826',
    )

    TerminateThread(0x000B, 0xFF)
    TerminateThread(0x000C, 0xFF)
    TerminateThread(0x000D, 0xFF)
    Event(1, 0x000B)

    def _loc_826(): pass

    label('loc_826')

    Jump('loc_829')

    def _loc_829(): pass

    label('loc_829')

    Return()

# id: 0x0001 offset: 0x82A
@scena.Code('func_01_82A')
def func_01_82A():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 1, 0x501)),
            Expr.Return,
        ),
        'loc_834',
    )

    Jump('loc_86C')

    def _loc_834(): pass

    label('loc_834')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_861',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0023, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_848',
    )

    Jump('loc_85E')

    def _loc_848(): pass

    label('loc_848')

    If(
        (
            (Expr.Eval, "OP_29(0x0023, 0x01, 0x1000)"),
            Expr.Return,
        ),
        'loc_85A',
    )

    OP_64(0x00, 0x0001)

    Jump('loc_85E')

    def _loc_85A(): pass

    label('loc_85A')

    OP_64(0x00, 0x0001)

    def _loc_85E(): pass

    label('loc_85E')

    Jump('loc_86C')

    def _loc_861(): pass

    label('loc_861')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_86C',
    )

    OP_64(0x00, 0x0001)

    def _loc_86C(): pass

    label('loc_86C')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_888'),
        (0x00000065, 'loc_888'),
        (0x00000066, 'loc_888'),
        (0x00000068, 'loc_888'),
        (0x0000006A, 'loc_888'),
        (-1, 'loc_890'),
    )

    def _loc_888(): pass

    label('loc_888')

    PlaySE(454, 0x01, 0x64)

    Jump('loc_893')

    def _loc_890(): pass

    label('loc_890')

    OP_23(0x01C6)

    def _loc_893(): pass

    label('loc_893')

    OP_1C(0x03, 0x00, 0x0012)

    Return()

# id: 0x0002 offset: 0x899
@scena.Code('func_02_899')
def func_02_899():
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

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8BE',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_951')

    def _loc_8BE(): pass

    label('loc_8BE')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8D7',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_951')

    def _loc_8D7(): pass

    label('loc_8D7')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8F0',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_951')

    def _loc_8F0(): pass

    label('loc_8F0')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_909',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_951')

    def _loc_909(): pass

    label('loc_909')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_922',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_951')

    def _loc_922(): pass

    label('loc_922')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_93B',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_951')

    def _loc_93B(): pass

    label('loc_93B')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_951',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    def _loc_951(): pass

    label('loc_951')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_966',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_951')

    def _loc_966(): pass

    label('loc_966')

    Return()

# id: 0x0003 offset: 0x967
@scena.Code('func_03_967')
def func_03_967():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_974',
    )

    Jump('loc_AC7')

    def _loc_974(): pass

    label('loc_974')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_97E',
    )

    Jump('loc_AC7')

    def _loc_97E(): pass

    label('loc_97E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_988',
    )

    Jump('loc_AC7')

    def _loc_988(): pass

    label('loc_988')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_992',
    )

    Jump('loc_AC7')

    def _loc_992(): pass

    label('loc_992')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_9A6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 6, 0x506)),
            Expr.Return,
        ),
        'loc_9A3',
    )

    Jump('loc_9A3')

    def _loc_9A3(): pass

    label('loc_9A3')

    Jump('loc_AC7')

    def _loc_9A6(): pass

    label('loc_9A6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 1, 0x501)),
            Expr.Return,
        ),
        'loc_9B0',
    )

    Jump('loc_AC7')

    def _loc_9B0(): pass

    label('loc_9B0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_A91',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0023, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_A27',
    )

    ChrTalk(
        0x00FE,
        (
            '我是为了静思一些事情\n',
            '才来到这里的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '都是那个公爵，\n',
            '害我把刚才想的事情\n',
            '都忘得一干二净了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A8E')

    def _loc_A27(): pass

    label('loc_A27')

    If(
        (
            (Expr.Eval, "OP_29(0x0023, 0x00, 0x08)"),
            Expr.Return,
        ),
        'loc_A65',
    )

    OP_4A(0x00FE, 255)

    ChrTalk(
        0x00FE,
        (
            '你是这里的士兵吧！\n',
            '快点想想办法啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4B(0x00FE, 255)

    Jump('loc_A8E')

    def _loc_A65(): pass

    label('loc_A65')

    ChrTalk(
        0x00FE,
        (
            '……从钥匙孔\n',
            '不知道能不能看到里面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A8E(): pass

    label('loc_A8E')

    Jump('loc_AC7')

    def _loc_A91(): pass

    label('loc_A91')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_AC7',
    )

    ChrTalk(
        0x00FE,
        (
            '在遗迹这样的地方还会有瀑布，\n',
            '真是罕见啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_AC7(): pass

    label('loc_AC7')

    TalkEnd(0x000B)

    Return()

# id: 0x0004 offset: 0xACB
@scena.Code('func_04_ACB')
def func_04_ACB():
    TalkBegin(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_AD8',
    )

    Jump('loc_C22')

    def _loc_AD8(): pass

    label('loc_AD8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_AE2',
    )

    Jump('loc_C22')

    def _loc_AE2(): pass

    label('loc_AE2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_AEC',
    )

    Jump('loc_C22')

    def _loc_AEC(): pass

    label('loc_AEC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_AF6',
    )

    Jump('loc_C22')

    def _loc_AF6(): pass

    label('loc_AF6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_B0A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 6, 0x506)),
            Expr.Return,
        ),
        'loc_B07',
    )

    Jump('loc_B07')

    def _loc_B07(): pass

    label('loc_B07')

    Jump('loc_C22')

    def _loc_B0A(): pass

    label('loc_B0A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 1, 0x501)),
            Expr.Return,
        ),
        'loc_B14',
    )

    Jump('loc_C22')

    def _loc_B14(): pass

    label('loc_B14')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_BCF',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0023, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_B65',
    )

    ChrTalk(
        0x00FE,
        (
            '难得的出游，\n',
            '心情都被那个臭公爵破坏了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我要上诉！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BCC')

    def _loc_B65(): pass

    label('loc_B65')

    If(
        (
            (Expr.Eval, "OP_29(0x0023, 0x00, 0x08)"),
            Expr.Return,
        ),
        'loc_BB2',
    )

    OP_4A(0x00FE, 255)

    ChrTalk(
        0x000C,
        (
            '王国军不是市民的朋友吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '好歹也要做些什么吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4B(0x00FE, 255)

    Jump('loc_BCC')

    def _loc_BB2(): pass

    label('loc_BB2')

    ChrTalk(
        0x00FE,
        (
            '真是，要想点办法呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BCC(): pass

    label('loc_BCC')

    Jump('loc_C22')

    def _loc_BCF(): pass

    label('loc_BCF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_C22',
    )

    ChrTalk(
        0x00FE,
        (
            '你们也觉得\n',
            '这里的景色非常美丽吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不愧是\n',
            '『利贝尔十六景』之一啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C22(): pass

    label('loc_C22')

    TalkEnd(0x000C)

    Return()

# id: 0x0005 offset: 0xC26
@scena.Code('func_05_C26')
def func_05_C26():
    TalkBegin(0x000D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_C33',
    )

    Jump('loc_DE8')

    def _loc_C33(): pass

    label('loc_C33')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_C3D',
    )

    Jump('loc_DE8')

    def _loc_C3D(): pass

    label('loc_C3D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_C47',
    )

    Jump('loc_DE8')

    def _loc_C47(): pass

    label('loc_C47')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_C51',
    )

    Jump('loc_DE8')

    def _loc_C51(): pass

    label('loc_C51')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_C65',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 6, 0x506)),
            Expr.Return,
        ),
        'loc_C62',
    )

    Jump('loc_C62')

    def _loc_C62(): pass

    label('loc_C62')

    Jump('loc_DE8')

    def _loc_C65(): pass

    label('loc_C65')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 1, 0x501)),
            Expr.Return,
        ),
        'loc_C6F',
    )

    Jump('loc_DE8')

    def _loc_C6F(): pass

    label('loc_C6F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_D70',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0023, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_CF1',
    )

    ChrTalk(
        0x00FE,
        (
            '游击士好像把问题解决了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不知道面对那样我行我素的人\n',
            '是怎么把问题解决的，\n',
            '不过游击士果然很靠得住啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D6D')

    def _loc_CF1(): pass

    label('loc_CF1')

    If(
        (
            (Expr.Eval, "OP_29(0x0023, 0x00, 0x08)"),
            Expr.Return,
        ),
        'loc_D22',
    )

    OP_4A(0x00FE, 255)

    ChrTalk(
        0x000D,
        (
            '就这样任他无理取闹吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4B(0x00FE, 255)

    Jump('loc_D6D')

    def _loc_D22(): pass

    label('loc_D22')

    ChrTalk(
        0x00FE,
        (
            '如果连游击士面对\n',
            '大人物也处于弱势的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '前景真是一片黑暗啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D6D(): pass

    label('loc_D6D')

    Jump('loc_DE8')

    def _loc_D70(): pass

    label('loc_D70')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_DE8',
    )

    ChrTalk(
        0x00FE,
        (
            '充满田园风光的玛诺利亚，\n',
            '观光旅游的港口城市卢安，\n',
            '以及这个艾尔·雷登……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这个地区的\n',
            '风景名胜还真多啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_DE8(): pass

    label('loc_DE8')

    TalkEnd(0x000D)

    Return()

# id: 0x0006 offset: 0xDEC
@scena.Code('func_06_DEC')
def func_06_DEC():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_EA4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_E51',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '唔，\n',
            '新的通知又下来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '上级部门对于\n',
            '逮捕犯人的事情\n',
            '还没有放弃。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EA1')

    def _loc_E51(): pass

    label('loc_E51')

    ChrTalk(
        0x00FE,
        (
            '可是这次的通知\n',
            '却给我们出了个难题啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我得准确无误地\n',
            '向部下传达才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_EA1(): pass

    label('loc_EA1')

    Jump('loc_1AC2')

    def _loc_EA4(): pass

    label('loc_EA4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_F9F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_F5D',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '解除盘查的命令\n',
            '是确凿的事实。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对于这个命令，\n',
            '我个人的确还是有些疑问。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，军令如山。\n',
            '是不容我们自作主张的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '除了服从上级的命令之外\n',
            '别无选择。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F9C')

    def _loc_F5D(): pass

    label('loc_F5D')

    ChrTalk(
        0x00FE,
        (
            '就算是这样，\n',
            '现在要解除盘查……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……是有什么内幕吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F9C(): pass

    label('loc_F9C')

    Jump('loc_1AC2')

    def _loc_F9F(): pass

    label('loc_F9F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_11C7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1172',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    If(
        (
            (Expr.Eval, "OP_29(0x0023, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_1086',
    )

    ChrTalk(
        0x00FE,
        (
            '哦，是游击士们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '中央工房被袭击的事件\n',
            '我们已经收到了相关报告。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这个关所和各地的关所一起\n',
            '开始实行严格的盘查制度。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样一来\n',
            '犯人就无处可逃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '放心吧。\n',
            '我想很快就可以抓到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_116F')

    def _loc_1086(): pass

    label('loc_1086')

    ChrTalk(
        0x00FE,
        (
            '哟，你们是旅行者吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '非常抱歉，\n',
            '因为发生了中央工房的事件，\n',
            '所以关所这里要进行盘查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '除非有紧急情况，\n',
            '不然是不能给你们发通行证的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且最近一段时间之内\n',
            '这种状况都要持续下去。\n',
            '如果是要去旅行的话，以后还会有机会的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_116F(): pass

    label('loc_116F')

    Jump('loc_11C4')

    def _loc_1172(): pass

    label('loc_1172')

    ChrTalk(
        0x00FE,
        (
            '王国军也在全力协助\n',
            '搜捕袭击工房的犯人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我相信犯人一定会\n',
            '很快被逮捕的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_11C4(): pass

    label('loc_11C4')

    Jump('loc_1AC2')

    def _loc_11C7(): pass

    label('loc_11C7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_128F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1238',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '对昨夜在蔡斯发生的事件，\n',
            '王国军也非常关注。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '情报部的那些人\n',
            '现在肯定在拼命调查吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_128C')

    def _loc_1238(): pass

    label('loc_1238')

    ChrTalk(
        0x00FE,
        (
            '算了，\n',
            '反正很快一切又会恢复原状的，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '蔡斯的中央工房\n',
            '是王国最重要的财产啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_128C(): pass

    label('loc_128C')

    Jump('loc_1AC2')

    def _loc_128F(): pass

    label('loc_128F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 6, 0x506)),
            Expr.Return,
        ),
        'loc_1673',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B1, 7, 0x58F)),
            Expr.Return,
        ),
        'loc_13B7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1329',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '呼，接下来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '文件已经整理好了，\n',
            '去看看部下的情况吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果总是呆在房间里不出去，\n',
            '就不能给他们起好带头作用了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_13B4')

    def _loc_1329(): pass

    label('loc_1329')

    ChrTalk(
        0x00FE,
        (
            '自从公爵阁下那次事件以来，\n',
            '感觉自己好像得不到\n',
            '部下的信赖了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈哈，你们可能认为我太神经质了，\n',
            '不过这也是我作为队长的分内工作啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_13B4(): pass

    label('loc_13B4')

    Jump('loc_1670')

    def _loc_13B7(): pass

    label('loc_13B7')

    If(
        (
            (Expr.Eval, "OP_29(0x0023, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_1523',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_14BE',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '哎呀，是你们几位。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '公爵阁下来的时候\n',
            '你们真是帮了大忙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '多亏你们才没给\n',
            '其他的旅客添更多的麻烦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然我们之间存在许多问题，\n',
            '但我想今后还是和\n',
            '游击士协会共同合作好一些。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果再有什么事的话，\n',
            '可能就要再次拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1520')

    def _loc_14BE(): pass

    label('loc_14BE')

    ChrTalk(
        0x00FE,
        (
            '我想今后还是和\n',
            '游击士协会共同合作好一些。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果再有什么事的话，\n',
            '可能就要再次拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1520(): pass

    label('loc_1520')

    Jump('loc_1670')

    def _loc_1523(): pass

    label('loc_1523')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_160F',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '呼，前些日子\n',
            '遇到了一件很麻烦的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一位和王室有关系的大人物\n',
            '到这个关所来视察了……\n',
            '那可是个蛮不讲理的人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '给那些普通的旅客们\n',
            '带来了不少的麻烦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看到那样的人，\n',
            '我对利贝尔王室的印象\n',
            '也变得比较差了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1670')

    def _loc_160F(): pass

    label('loc_160F')

    ChrTalk(
        0x00FE,
        (
            '好不容易\n',
            '就快到女王的诞辰庆典了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看到那样的人，\n',
            '我对利贝尔王室的印象\n',
            '也变得比较差了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1670(): pass

    label('loc_1670')

    Jump('loc_1AC2')

    def _loc_1673(): pass

    label('loc_1673')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 1, 0x501)),
            Expr.Return,
        ),
        'loc_1939',
    )

    SetScenaFlags(ScenaFlag(0x00B1, 7, 0x58F))

    If(
        (
            (Expr.Eval, "OP_29(0x0023, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_17E9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1784',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '哎呀，是你们几位。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '公爵阁下来的时候\n',
            '你们真是帮了大忙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '多亏你们才没给\n',
            '其他的旅客添更多的麻烦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然我们之间存在许多问题，\n',
            '但我想今后还是和\n',
            '游击士协会共同合作好一些。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果再有什么事的话，\n',
            '可能就要再次拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17E6')

    def _loc_1784(): pass

    label('loc_1784')

    ChrTalk(
        0x00FE,
        (
            '我想今后还是和\n',
            '游击士协会共同合作好一些。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果再有什么事的话，\n',
            '可能就要再次拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_17E6(): pass

    label('loc_17E6')

    Jump('loc_1936')

    def _loc_17E9(): pass

    label('loc_17E9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_18D5',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '呼，前些日子\n',
            '遇到了一件很麻烦的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一位和王室有关系的大人物\n',
            '到这个关所来视察了……\n',
            '那可是个蛮不讲理的人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '给那些普通的旅客们\n',
            '带来了不少的麻烦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看到那样的人，\n',
            '我对利贝尔王室的印象\n',
            '也变得比较差了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1936')

    def _loc_18D5(): pass

    label('loc_18D5')

    ChrTalk(
        0x00FE,
        (
            '好不容易\n',
            '就快到女王的诞辰庆典了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看到那样的人，\n',
            '我对利贝尔王室的印象\n',
            '也变得比较差了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1936(): pass

    label('loc_1936')

    Jump('loc_1AC2')

    def _loc_1939(): pass

    label('loc_1939')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_19C3',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0023, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_1998',
    )

    ChrTalk(
        0x00FE,
        (
            '各位，这次辛苦你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎呀呀…………\n',
            '多灾多难的一天终于过去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19C0')

    def _loc_1998(): pass

    label('loc_1998')

    If(
        (
            (Expr.Eval, "OP_29(0x0023, 0x00, 0x08)"),
            Expr.Return,
        ),
        'loc_19C0',
    )

    ChrTalk(
        0x00FE,
        (
            '各、各位\n',
            '请冷静一点！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19C0')

    def _loc_19C0(): pass

    label('loc_19C0')

    Jump('loc_1AC2')

    def _loc_19C3(): pass

    label('loc_19C3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_1AC2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1AA8',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    OP_4A(0x000A, 255)

    ChrTalk(
        0x00FE,
        (
            '听说公爵要到\n',
            '卢安市去进行访问，\n',
            '不过没听说过会到这里来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '唉，好像是根据他本人的意愿\n',
            '而突然改变预定计划的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，这就没办法了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '视察的相关事项\n',
            '本来已经准备好了的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '是！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4B(0x000A, 255)
    ChrClearFlags(0x000A, 0x0010)

    Jump('loc_1AC2')

    def _loc_1AA8(): pass

    label('loc_1AA8')

    ChrTalk(
        0x00FE,
        (
            '唉，真是件麻烦事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1AC2(): pass

    label('loc_1AC2')

    TalkEnd(0x0008)

    Return()

# id: 0x0007 offset: 0x1AC6
@scena.Code('func_07_1AC6')
def func_07_1AC6():
    TalkBegin(0x000E)

    ChrTalk(
        0x000E,
        (
            '#0020170670V#010F这里由我们来想办法……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020170671V艾丝蒂尔你们赶快去食堂看看状况。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000E)

    Return()

# id: 0x0008 offset: 0x1B2E
@scena.Code('func_08_1B2E')
def func_08_1B2E():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_1B85',
    )

    ChrTalk(
        0x00FE,
        (
            '……所以说嘛，\n',
            '新的通知到现在才来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '早知道开始就\n',
            '不该解除盘查～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24DF')

    def _loc_1B85(): pass

    label('loc_1B85')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_1CE1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1C3C',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '队长虽然看起来很普通，\n',
            '但是属于那种刚直不阿的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他认为这次的命令\n',
            '无法让人接受。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过实际上，\n',
            '我也觉得无法接受呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊啊～可恶！\n',
            '真让人恼火。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1CDE')

    def _loc_1C3C(): pass

    label('loc_1C3C')

    ChrTalk(
        0x00FE,
        (
            '呼，\n',
            '一个不明不白的公爵事件就够呛了，\n',
            '这回又来了个不知所谓的命令……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这个国家的领导者\n',
            '怎么会变得这么奇怪呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说实话，\n',
            '实在不想再碰上这样的事情了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1CDE(): pass

    label('loc_1CDE')

    Jump('loc_24DF')

    def _loc_1CE1(): pass

    label('loc_1CE1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_1D4B',
    )

    ChrTalk(
        0x00FE,
        (
            '抱歉啊。\n',
            '现在关所正处于戒严状态。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我不能和你们\n',
            '说太多闲话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且部下还在旁边呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24DF')

    def _loc_1D4B(): pass

    label('loc_1D4B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_1DF4',
    )

    ChrTalk(
        0x00FE,
        (
            '听说了吗，蔡斯的事情。\n',
            '好像引起了很大的骚乱啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为那里是利贝尔王国中\n',
            '导力化程度最高的城市。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果那里一旦停止运转，\n',
            '想必一定会带来很多不便吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24DF')

    def _loc_1DF4(): pass

    label('loc_1DF4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 6, 0x506)),
            Expr.Return,
        ),
        'loc_20CA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B2, 0, 0x590)),
            Expr.Return,
        ),
        'loc_1E6C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1E46',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '啊，\n',
            '不能再偷懒了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '队长很快\n',
            '就要来巡视了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E69')

    def _loc_1E46(): pass

    label('loc_1E46')

    ChrTalk(
        0x00FE,
        (
            '没办法啊，\n',
            '这份工作太累人了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1E69(): pass

    label('loc_1E69')

    Jump('loc_20C7')

    def _loc_1E6C(): pass

    label('loc_1E6C')

    If(
        (
            (Expr.Eval, "OP_29(0x0023, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_1F8A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1F25',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '噢，是你们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，之前公爵阁下来的时候\n',
            '真是多亏你们帮了大忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '游击士和王国军之间\n',
            '经常会有各种纠纷………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过在表面上\n',
            '还是会经常互相协助的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F87')

    def _loc_1F25(): pass

    label('loc_1F25')

    ChrTalk(
        0x00FE,
        (
            '也是啊，台面上的话语\n',
            '还是交给那些所谓的伟人们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只要在事件现场\n',
            '能够处理得当就可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1F87(): pass

    label('loc_1F87')

    Jump('loc_20C7')

    def _loc_1F8A(): pass

    label('loc_1F8A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2046',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '前不久王室的那个什么公爵\n',
            '到这个关所来视察了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，那是个胡说八道、\n',
            '蛮不讲理的家伙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，\n',
            '一想到要为那样的家伙忙个不停……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就会觉得\n',
            '要是没来参军就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_20C7')

    def _loc_2046(): pass

    label('loc_2046')

    ChrTalk(
        0x00FE,
        (
            '一想到那个公爵\n',
            '也算是王室的一员……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就会觉得\n',
            '要是没来参军就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，以我现在的立场，\n',
            '这样的事情还是少说为妙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_20C7(): pass

    label('loc_20C7')

    Jump('loc_24DF')

    def _loc_20CA(): pass

    label('loc_20CA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 1, 0x501)),
            Expr.Return,
        ),
        'loc_2332',
    )

    SetScenaFlags(ScenaFlag(0x00B2, 0, 0x590))

    If(
        (
            (Expr.Eval, "OP_29(0x0023, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_21F2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_218D',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '噢，是你们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，之前公爵阁下来的时候\n',
            '真是多亏你们帮了大忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '游击士和王国军之间\n',
            '经常会有各种纠纷………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过在表面上\n',
            '还是会经常互相协助的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_21EF')

    def _loc_218D(): pass

    label('loc_218D')

    ChrTalk(
        0x00FE,
        (
            '也是啊，台面上的话语\n',
            '还是交给那些所谓的伟人们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只要在事件现场\n',
            '能够处理得当就可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_21EF(): pass

    label('loc_21EF')

    Jump('loc_232F')

    def _loc_21F2(): pass

    label('loc_21F2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_22AE',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '前不久王室的那个什么公爵\n',
            '到这个关所来视察了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，那是个胡说八道、\n',
            '蛮不讲理的家伙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，\n',
            '一想到要为那样的家伙忙个不停……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就会觉得\n',
            '要是没来参军就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_232F')

    def _loc_22AE(): pass

    label('loc_22AE')

    ChrTalk(
        0x00FE,
        (
            '一想到那个公爵\n',
            '也算是王室的一员……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就会觉得\n',
            '要是没来参军就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，以我现在的立场，\n',
            '这样的事情还是少说为妙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_232F(): pass

    label('loc_232F')

    Jump('loc_24DF')

    def _loc_2332(): pass

    label('loc_2332')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_2470',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0023, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_2460',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_23FC',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '哇哈哈哈，\n',
            '小姑娘还真是干净利落！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '游击士里\n',
            '也有些很有趣的人嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说起来，\n',
            '为什么那种人\n',
            '会出生在王家呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽说他是下任国王，\n',
            '我只是希望他的发型能正经点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_245D')

    def _loc_23FC(): pass

    label('loc_23FC')

    ChrTalk(
        0x00FE,
        (
            '说起来，\n',
            '为什么那种人\n',
            '会出生在王家呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽说他是下任国王，\n',
            '我只是希望他的发型能正经点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_245D(): pass

    label('loc_245D')

    Jump('loc_246D')

    def _loc_2460(): pass

    label('loc_2460')

    If(
        (
            (Expr.Eval, "OP_29(0x0023, 0x00, 0x08)"),
            Expr.Return,
        ),
        'loc_246D',
    )

    Jump('loc_246D')

    def _loc_246D(): pass

    label('loc_246D')

    Jump('loc_24DF')

    def _loc_2470(): pass

    label('loc_2470')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_24DF',
    )

    ChrTalk(
        0x00FE,
        (
            '库隆那家伙\n',
            '和队长说了些什么啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总觉得有不好的预感……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那家伙总是会带来\n',
            '一些不好的消息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_24DF(): pass

    label('loc_24DF')

    TalkEnd(0x0009)

    Return()

# id: 0x0009 offset: 0x24E3
@scena.Code('func_09_24E3')
def func_09_24E3():
    Call(0, 0x000A)

    Return()

# id: 0x000A offset: 0x24E8
@scena.Code('func_0A_24E8')
def func_0A_24E8():
    TalkBegin(0x0012)
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
        1,
        (
            TXT(0x00, '对话\n'),
            TXT(0x01, '买东西\n'),
            TXT(0x02, '离开\n'),
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

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2546',
    )

    FadeIn(300, 0)
    OP_0D()
    OP_A9(0x34)
    OP_56(0x00)
    TalkEnd(0x0012)

    Return()

    def _loc_2546(): pass

    label('loc_2546')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2560',
    )

    FadeIn(300, 0)
    TalkEnd(0x0012)

    Return()

    def _loc_2560(): pass

    label('loc_2560')

    FadeIn(300, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_2666',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_260A',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x0012,
        (
            '你们好，欢迎光临。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '看啊，现在这个样子。\n',
            '基本上没什么人来光顾了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '诞辰庆典也带走了很多旅客。\n',
            '唉～人气这个东西真是变幻莫测啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2663')

    def _loc_260A(): pass

    label('loc_260A')

    ChrTalk(
        0x0012,
        (
            '好吧，\n',
            '既然你们特地来到这里，\n',
            '我就给你们露一手吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '来吧，\n',
            '你们想点什么都可以！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2663(): pass

    label('loc_2663')

    Jump('loc_2B04')

    def _loc_2666(): pass

    label('loc_2666')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_2738',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_26DF',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x0012,
        (
            '你们好，欢迎光临。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '如你所见，\n',
            '现在盘查已经解除了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '不过这样好吗？\n',
            '这么快就解除盘查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2735')

    def _loc_26DF(): pass

    label('loc_26DF')

    ChrTalk(
        0x0012,
        (
            '哼，\n',
            '反正肯定还没抓到犯人吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '王国军真是没什么用啊。\n',
            '接下来就看游击士的了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2735(): pass

    label('loc_2735')

    Jump('loc_2B04')

    def _loc_2738(): pass

    label('loc_2738')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_27C3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_279B',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x0012,
        (
            '呼，\n',
            '最近烦人的消息接二连三……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '就算是我，\n',
            '今天也没有什么心情说话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_27C0')

    def _loc_279B(): pass

    label('loc_279B')

    ChrTalk(
        0x0012,
        (
            '呼，真是的。\n',
            '烦人的消息太多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_27C0(): pass

    label('loc_27C0')

    Jump('loc_2B04')

    def _loc_27C3(): pass

    label('loc_27C3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_282A',
    )

    ChrTalk(
        0x0012,
        (
            '听说了吗？\n',
            '蔡斯的事件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '所有导力器\n',
            '都停止运转了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '真是令人惊讶的\n',
            '神奇事件啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2B04')

    def _loc_282A(): pass

    label('loc_282A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 6, 0x506)),
            Expr.Return,
        ),
        'loc_2887',
    )

    ChrTalk(
        0x0012,
        (
            '噢，欢迎光临。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '这里唯一的优点就是景色不错，\n',
            '你们还是可以好好享受一下的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2B04')

    def _loc_2887(): pass

    label('loc_2887')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 1, 0x501)),
            Expr.Return,
        ),
        'loc_297E',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0023, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_2909',
    )

    ChrTalk(
        0x0012,
        (
            '哟，是你们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '之前真是多谢了。\n',
            '对了，今天来也是因为工作吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '如果有空的话，\n',
            '要记得经常来玩呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_297B')

    def _loc_2909(): pass

    label('loc_2909')

    ChrTalk(
        0x0012,
        (
            '哟，欢迎光临。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '欣赏了瀑布的风景之后，\n',
            '再来品尝一些美味的食物如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '总之，\n',
            '请在这里好好放松一下哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_297B(): pass

    label('loc_297B')

    Jump('loc_2B04')

    def _loc_297E(): pass

    label('loc_297E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_29E8',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0023, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_29D8',
    )

    ChrTalk(
        0x0012,
        (
            '唉……\n',
            '真是个令人头痛的大叔啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '完全搞不清\n',
            '什么是公共场合。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_29E5')

    def _loc_29D8(): pass

    label('loc_29D8')

    If(
        (
            (Expr.Eval, "OP_29(0x0023, 0x00, 0x08)"),
            Expr.Return,
        ),
        'loc_29E5',
    )

    Jump('loc_29E5')

    def _loc_29E5(): pass

    label('loc_29E5')

    Jump('loc_2B04')

    def _loc_29E8(): pass

    label('loc_29E8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_2B04',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2AA2',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x0012,
        (
            '哟，欢迎光临。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '在欣赏美景时如果没有佳肴做伴，\n',
            '那可就有些遗憾了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '这里的盐锅烤小鱼\n',
            '可是十分好吃的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '从头到尾都可以吃，\n',
            '是本店超级推荐的料理！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2B04')

    def _loc_2AA2(): pass

    label('loc_2AA2')

    ChrTalk(
        0x0012,
        (
            '在欣赏美景时如果没有佳肴做伴，\n',
            '那可就有些遗憾了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '这里的盐锅烤小鱼\n',
            '可是十分好吃的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2B04(): pass

    label('loc_2B04')

    TalkEnd(0x0012)

    Return()

# id: 0x000B offset: 0x2B08
@scena.Code('func_0B_2B08')
def func_0B_2B08():
    Call(0, 0x000C)

    Return()

# id: 0x000C offset: 0x2B0D
@scena.Code('func_0C_2B0D')
def func_0C_2B0D():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_2C06',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2B9A',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x000A,
        (
            '总部那边\n',
            '又下达了新的命令。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '大概又是\n',
            '与通行许可相关的通知吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '呼～\n',
            '差不多都可以猜出来是什么内容了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2C03')

    def _loc_2B9A(): pass

    label('loc_2B9A')

    ChrTalk(
        0x000A,
        (
            '好像又有一个\n',
            '新的命令下来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '唔～\n',
            '上级部门怎么忽左忽右的啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '感觉好像\n',
            '总是抓不住要点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2C03(): pass

    label('loc_2C03')

    Jump('loc_36C1')

    def _loc_2C06(): pass

    label('loc_2C06')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_2D2F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2CA3',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x000A,
        (
            '上级部门\n',
            '又下达新指示了，\n',
            '说要解除盘查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '可还没有听说犯人\n',
            '被逮捕了的消息啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '就这样恢复以往的通行状态，\n',
            '不会有问题吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2D2C')

    def _loc_2CA3(): pass

    label('loc_2CA3')

    ChrTalk(
        0x000A,
        (
            '虽说是上级部门的命令，\n',
            '但总感觉难以理解。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '犯人都还没有捉到，\n',
            '就把盘查给解除了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '难道说其他的关所\n',
            '也接到了相同的命令吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2D2C(): pass

    label('loc_2D2C')

    Jump('loc_36C1')

    def _loc_2D2F(): pass

    label('loc_2D2F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_2E1B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2DC2',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x000A,
        (
            '很抱歉，\n',
            '现在除非有紧急情况，\n',
            '否则不能签发通行许可证。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '在袭击蔡斯的犯人\n',
            '被逮捕之前的这段时间内\n',
            '都会保持现在的状况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2E18')

    def _loc_2DC2(): pass

    label('loc_2DC2')

    ChrTalk(
        0x000A,
        (
            '现在除非有紧急情况，\n',
            '否则不能签发通行许可证。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '如果能早些\n',
            '逮捕犯人就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2E18(): pass

    label('loc_2E18')

    Jump('loc_36C1')

    def _loc_2E1B(): pass

    label('loc_2E1B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_2EED',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2E92',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x000A,
        (
            '昨天晚上，\n',
            '蔡斯发生了奇怪的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '导力竟然都停止了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '唔～\n',
            '那种事情真的会发生吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2EEA')

    def _loc_2E92(): pass

    label('loc_2E92')

    ChrTalk(
        0x000A,
        (
            '据说昨晚蔡斯的\n',
            '导力发生了停止现象……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '有点难以置信呢。\n',
            '导力器竟然会停止工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2EEA(): pass

    label('loc_2EEA')

    Jump('loc_36C1')

    def _loc_2EED(): pass

    label('loc_2EED')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 1, 0x501)),
            Expr.Return,
        ),
        'loc_347F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_33DB',
    )

    EventBegin(0x00)
    Fade(1000)
    ChrSetDirection(0x000A, 90, 0)
    ChrSetPos(0x0101, -2800, 0, 6800, 270)
    ChrSetPos(0x0102, -2800, 0, 8000, 270)
    ChrSetPos(0x0105, -1800, 0, 7200, 270)
    CameraMove(-3900, 0, 7800, 1000)

    ChrTalk(
        0x000A,
        (
            '#1940070223V你们好。\n',
            '请问有什么事呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070224V#010F我们想进入蔡斯地区，\n',
            '请问能帮我们办理通行手续吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1940070225V啊，是这样啊。\n',
            '那就请到这边的柜台。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1940070226V通行手续办好之后，\n',
            '你们就无法再返回卢安地区了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1940070227V这样可以吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
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
        10,
        0,
        (
            TXT(0x00, '【办理通行手续】\n'),
            TXT(0x01, '【还是算了】\n'),
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
        (0x00000000, 'loc_30C4'),
        (0x00000001, 'loc_33A2'),
        (-1, 'loc_33D6'),
    )

    def _loc_30C4(): pass

    label('loc_30C4')

    SetScenaFlags(ScenaFlag(0x00A0, 2, 0x502))

    ChrTalk(
        0x0101,
        (
            '#0010070229V#006F嗯，\n',
            '就麻烦您了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1940070230V那么，\n',
            '请在这些文件上签字吧。',
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
            '艾丝蒂尔和约修亚\n',
            '在通行手续的文件上签了字。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x000A,
        (
            '#1940070231V好的，这样就ＯＫ了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1940070232V请问那位小姐\n',
            '也要办理通行手续吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060070233V#040F啊……\n',
            '我只是来为他们送行的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1940070234V哦，这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1940070235V那么你可以一直送到\n',
            '卡鲁迪亚隧道的入口。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060070236V#041F真是太感谢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010070237V#501F卡鲁迪亚隧道？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1940070238V嗯，没错。\n',
            '是一直连接到蔡斯市的地下通道。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1940070239V那可是一条贯穿整个\n',
            '卡鲁迪亚丘陵的超长隧道哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070240V#004F哎～是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070241V#010F地下的隧道吗……\n',
            '还是第一次走这种地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_33D6')

    def _loc_33A2(): pass

    label('loc_33A2')

    ChrTalk(
        0x000A,
        (
            '#1940070228V那么，\n',
            '准备好了之后再来找我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_33D6')

    def _loc_33D6(): pass

    label('loc_33D6')

    EventEnd(0x00)

    Jump('loc_347C')

    def _loc_33DB(): pass

    label('loc_33DB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 3, 0x503)),
            Expr.Return,
        ),
        'loc_342E',
    )

    ChrTalk(
        0x000A,
        (
            '哦，怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '既然已经办好通行手续，\n',
            '就不能再从这个关所回去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_347C')

    def _loc_342E(): pass

    label('loc_342E')

    ChrTalk(
        0x000A,
        (
            '送行的人可以送到\n',
            '卡鲁迪亚隧道入口。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '那么各位，\n',
            '路上请务必小心行走。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_347C(): pass

    label('loc_347C')

    Jump('loc_36C1')

    def _loc_347F(): pass

    label('loc_347F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_35B2',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0023, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_358C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3529',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x000A,
        (
            '没想到他竟然是\n',
            '艾莉茜雅女王的侄子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '这次也是由于我传达的命令不当\n',
            '而引发了这个事件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '哎呀呀，\n',
            '吃饭的时候又要被副长挖苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3589')

    def _loc_3529(): pass

    label('loc_3529')

    ChrTalk(
        0x000A,
        (
            '这次也是由于我传达的命令不当\n',
            '而引发了这个事件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '哎呀呀，\n',
            '吃饭的时候又要被副长挖苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3589(): pass

    label('loc_3589')

    Jump('loc_35AF')

    def _loc_358C(): pass

    label('loc_358C')

    If(
        (
            (Expr.Eval, "OP_29(0x0023, 0x00, 0x08)"),
            Expr.Return,
        ),
        'loc_3599',
    )

    Jump('loc_35AF')

    def _loc_3599(): pass

    label('loc_3599')

    ChrTalk(
        0x000A,
        (
            '副长他没事吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_35AF(): pass

    label('loc_35AF')

    Jump('loc_36C1')

    def _loc_35B2(): pass

    label('loc_35B2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_36C1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3698',
    )

    OP_4A(0x0008, 255)
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x0008,
        (
            '听说公爵要到\n',
            '卢安市去进行访问，\n',
            '不过没听说过会到这里来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '唉，\n',
            '好像是根据他本人的意愿\n',
            '而突然改变预定计划的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '呼，这就没办法了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '视察的相关事项\n',
            '本来已经准备好了的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '是！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4B(0x0008, 255)
    ChrClearFlags(0x000A, 0x0010)

    Jump('loc_36C1')

    def _loc_3698(): pass

    label('loc_3698')

    ChrTalk(
        0x000A,
        (
            '好像有一个大人物\n',
            '突然要来这里访问。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_36C1(): pass

    label('loc_36C1')

    TalkEnd(0x000A)

    Return()

# id: 0x000D offset: 0x36C5
@scena.Code('func_0D_36C5')
def func_0D_36C5():
    TalkBegin(0x0013)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_36D2',
    )

    Jump('loc_3839')

    def _loc_36D2(): pass

    label('loc_36D2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_36DC',
    )

    Jump('loc_3839')

    def _loc_36DC(): pass

    label('loc_36DC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_36E6',
    )

    Jump('loc_3839')

    def _loc_36E6(): pass

    label('loc_36E6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_36F0',
    )

    Jump('loc_3839')

    def _loc_36F0(): pass

    label('loc_36F0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_3704',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 6, 0x506)),
            Expr.Return,
        ),
        'loc_3701',
    )

    Jump('loc_3701')

    def _loc_3701(): pass

    label('loc_3701')

    Jump('loc_3839')

    def _loc_3704(): pass

    label('loc_3704')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 1, 0x501)),
            Expr.Return,
        ),
        'loc_370E',
    )

    Jump('loc_3839')

    def _loc_370E(): pass

    label('loc_370E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_37F3',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0023, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_3777',
    )

    ChrTalk(
        0x00FE,
        (
            '他居然是王家的人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我可不想让其他国家的人知道\n',
            '我们王国有如此蛮横的家伙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_37F0')

    def _loc_3777(): pass

    label('loc_3777')

    If(
        (
            (Expr.Eval, "OP_29(0x0023, 0x00, 0x08)"),
            Expr.Return,
        ),
        'loc_37C9',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯，士兵碰上这种事\n',
            '也是没有办法的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他们的心情我能理解。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_37F0')

    def _loc_37C9(): pass

    label('loc_37C9')

    ChrTalk(
        0x00FE,
        (
            '嗯嗯，\n',
            '那种我行我素的人到处都有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_37F0(): pass

    label('loc_37F0')

    Jump('loc_3839')

    def _loc_37F3(): pass

    label('loc_37F3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_3839',
    )

    ChrTalk(
        0x00FE,
        (
            '哇啊～这里真美。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '住宿又便宜，\n',
            '想在这里住多久都行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3839(): pass

    label('loc_3839')

    TalkEnd(0x0013)

    Return()

# id: 0x000E offset: 0x383D
@scena.Code('func_0E_383D')
def func_0E_383D():
    TalkBegin(0x0014)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_384A',
    )

    Jump('loc_3941')

    def _loc_384A(): pass

    label('loc_384A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_3854',
    )

    Jump('loc_3941')

    def _loc_3854(): pass

    label('loc_3854')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_385E',
    )

    Jump('loc_3941')

    def _loc_385E(): pass

    label('loc_385E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_3868',
    )

    Jump('loc_3941')

    def _loc_3868(): pass

    label('loc_3868')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_387C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 6, 0x506)),
            Expr.Return,
        ),
        'loc_3879',
    )

    Jump('loc_3879')

    def _loc_3879(): pass

    label('loc_3879')

    Jump('loc_3941')

    def _loc_387C(): pass

    label('loc_387C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 1, 0x501)),
            Expr.Return,
        ),
        'loc_3886',
    )

    Jump('loc_3941')

    def _loc_3886(): pass

    label('loc_3886')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_3907',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0023, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_38D3',
    )

    ChrTalk(
        0x00FE,
        (
            '你们几个\n',
            '就是解决事件的人吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不愧是游击士啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3904')

    def _loc_38D3(): pass

    label('loc_38D3')

    If(
        (
            (Expr.Eval, "OP_29(0x0023, 0x00, 0x08)"),
            Expr.Return,
        ),
        'loc_38F2',
    )

    ChrTalk(
        0x00FE,
        (
            '真伤脑筋……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3904')

    def _loc_38F2(): pass

    label('loc_38F2')

    ChrTalk(
        0x00FE,
        (
            '真伤脑筋……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3904(): pass

    label('loc_3904')

    Jump('loc_3941')

    def _loc_3907(): pass

    label('loc_3907')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_3941',
    )

    ChrTalk(
        0x00FE,
        (
            '虽说瀑布的水声很大，\n',
            '可是心里却感觉很平静呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3941(): pass

    label('loc_3941')

    TalkEnd(0x0014)

    Return()

# id: 0x000F offset: 0x3945
@scena.Code('func_0F_3945')
def func_0F_3945():
    Call(0, 0x0010)

    Return()

# id: 0x0010 offset: 0x394A
@scena.Code('func_10_394A')
def func_10_394A():
    TalkBegin(0x0015)
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
        1,
        (
            TXT(0x00, '对话\n'),
            TXT(0x01, '休息\n'),
            TXT(0x02, '离开\n'),
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
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_39A6',
    )

    OP_0D()
    OP_A9(0x35)
    OP_56(0x00)
    TalkEnd(0x0015)

    Return()

    def _loc_39A6(): pass

    label('loc_39A6')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_39B7',
    )

    TalkEnd(0x0015)

    Return()

    def _loc_39B7(): pass

    label('loc_39B7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_3B57',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00BA, 1, 0x5D1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3AFD',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x0015,
        (
            '留宿的人忘了带走的东西\n',
            '可真不少呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '虽然我们都暂时代为保管了，\n',
            '但很少有人回来取。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '这本书也是\n',
            '无人认领的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '……啊，想要这本书吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '唔～………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '你们能替我向队长保密吗？\n',
            '因为这是违反规定的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x00BA, 1, 0x5D1))
    AddItem(0x0219, 1)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '红耀石　第８卷',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    Jump('loc_3B54')

    def _loc_3AFD(): pass

    label('loc_3AFD')

    ChrTalk(
        0x0015,
        (
            '你们是旅行者吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '这个时候为了诞辰庆典，\n',
            '大家都赶往王都了，很少有人到这里来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3B54(): pass

    label('loc_3B54')

    Jump('loc_4132')

    def _loc_3B57(): pass

    label('loc_3B57')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_3C66',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3BF5',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x0015,
        (
            '刚才基恩茨副长来了，\n',
            '很粗暴地对我们大声吼叫。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '太、太可怕了，\n',
            '好像一下就变得勃然大怒了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '是发生了什么\n',
            '难以忍受的事情吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3C63')

    def _loc_3BF5(): pass

    label('loc_3BF5')

    ChrTalk(
        0x0015,
        (
            '呼，我们的副长\n',
            '平常是个乐呵呵的人……\n',
            '可一旦发怒就会变得极为恐怖。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '这种事情\n',
            '无论谁听了\n',
            '都会发怒啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3C63(): pass

    label('loc_3C63')

    Jump('loc_4132')

    def _loc_3C66(): pass

    label('loc_3C66')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_3D2C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3CCE',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x0015,
        (
            '总、总觉得\n',
            '好像出大事了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '我们这个关所\n',
            '也进入了前所未有的\n',
            '警戒状态了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3D29')

    def _loc_3CCE(): pass

    label('loc_3CCE')

    ChrTalk(
        0x0015,
        (
            '唉，\n',
            '光是听说袭击事件什么的\n',
            '就让人毛骨悚然了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '好希望早日能够将\n',
            '犯人绳之以法啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3D29(): pass

    label('loc_3D29')

    Jump('loc_4132')

    def _loc_3D2C(): pass

    label('loc_3D2C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_3E14',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3DAD',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x0015,
        (
            '哟，欢迎光临。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '蔡斯那里\n',
            '好像出事了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '导力器竟然都停止运转了。\n',
            '这世界上还有这等奇妙的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3E11')

    def _loc_3DAD(): pass

    label('loc_3DAD')

    ChrTalk(
        0x0015,
        (
            '据说是由于中央工房的\n',
            '实验而导致的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '可是不管是怎样的实验，\n',
            '也不至于把导力都给停止了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3E11(): pass

    label('loc_3E11')

    Jump('loc_4132')

    def _loc_3E14(): pass

    label('loc_3E14')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 6, 0x506)),
            Expr.Return,
        ),
        'loc_3FB1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3F6F',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3E55',
    )

    ChrTalk(
        0x0015,
        (
            '哟，欢迎来到艾尔·雷登。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3F6C')

    def _loc_3E55(): pass

    label('loc_3E55')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3EBB',
    )

    ChrTalk(
        0x0015,
        (
            '哦，你们是兄妹结伴旅行吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '从这里可以近距离看到瀑布，\n',
            '是个最佳的住宿地点哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3F6C')

    def _loc_3EBB(): pass

    label('loc_3EBB')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3F21',
    )

    ChrTalk(
        0x0015,
        (
            '哦，你们是兄妹结伴旅行吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '从这里可以近距离看到瀑布，\n',
            '是个最佳的住宿地点哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3F6C')

    def _loc_3F21(): pass

    label('loc_3F21')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3F6C',
    )

    ChrTalk(
        0x0015,
        (
            '哟，\n',
            '相当年轻的旅客啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '是和哥哥姐姐一起来旅行的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3F6C(): pass

    label('loc_3F6C')

    Jump('loc_3FAE')

    def _loc_3F6F(): pass

    label('loc_3F6F')

    ChrTalk(
        0x0015,
        (
            '如果有什么事情，\n',
            '和我说一声就是了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '那么，旅途愉快。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_3FAE(): pass

    label('loc_3FAE')

    Jump('loc_4132')

    def _loc_3FB1(): pass

    label('loc_3FB1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 1, 0x501)),
            Expr.Return,
        ),
        'loc_400D',
    )

    ChrTalk(
        0x0015,
        (
            '哟，欢迎光临。\n',
            '这里是旅行者的住宿设施。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '想要休息的时候\n',
            '就请告诉我一声。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4132')

    def _loc_400D(): pass

    label('loc_400D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_40DD',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0023, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_406D',
    )

    ChrTalk(
        0x0015,
        (
            '这么长时间\n',
            '一直在吵吵闹闹的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '过会儿向副长问一下\n',
            '发生了什么事吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_40DA')

    def _loc_406D(): pass

    label('loc_406D')

    If(
        (
            (Expr.Eval, "OP_29(0x0023, 0x00, 0x08)"),
            Expr.Return,
        ),
        'loc_40AA',
    )

    ChrTalk(
        0x0015,
        (
            '外面真吵啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '有什么人在挑起纷争吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_40DA')

    def _loc_40AA(): pass

    label('loc_40AA')

    ChrTalk(
        0x0015,
        (
            '外面真吵啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '有什么人在挑起纷争吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_40DA(): pass

    label('loc_40DA')

    Jump('loc_4132')

    def _loc_40DD(): pass

    label('loc_40DD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_4132',
    )

    ChrTalk(
        0x0015,
        (
            '今天希望在这里留宿的客人\n',
            '好像很多呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '得早点去\n',
            '把房间打扫干净才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4132(): pass

    label('loc_4132')

    TalkEnd(0x0015)

    Return()

# id: 0x0011 offset: 0x4136
@scena.Code('func_11_4136')
def func_11_4136():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_41DA',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4155',
    )

    ChrTurnDirection(0x0102, 0x0001, 400)

    Jump('loc_415C')

    def _loc_4155(): pass

    label('loc_4155')

    ChrTurnDirection(0x0102, 0x0000, 400)

    def _loc_415C(): pass

    label('loc_415C')

    ChrTalk(
        0x0102,
        (
            '#0020070332V#010F这边是卢安地区啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020070333V我们没有拿到通行证，\n',
            '是不能从这边出去的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveToRelative(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Jump('loc_425F')

    def _loc_41DA(): pass

    label('loc_41DA')

    If(
        (
            (Expr.Eval, "OP_29(0x0023, 0x00, 0x08)"),
            (Expr.Eval, "OP_29(0x0023, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0023, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_425F',
    )

    EventBegin(0x01)
    OP_4A(0x000E, 255)
    ChrTurnDirection(0x000E, 0x0101, 0)

    ChrTalk(
        0x000E,
        (
            '#0020170668V#012F艾丝蒂尔，\n',
            '赶快去食堂看看情况吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveToRelative(0x0000, 0, 0, 1500, 3000, 0x00)
    ChrSetDirection(0x000E, 0, 0)
    OP_4B(0x000E, 255)
    Sleep(50)

    EventEnd(0x04)

    def _loc_425F(): pass

    label('loc_425F')

    Return()

# id: 0x0012 offset: 0x4260
@scena.Code('func_12_4260')
def func_12_4260():
    TalkBegin(0x00FF)
    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
