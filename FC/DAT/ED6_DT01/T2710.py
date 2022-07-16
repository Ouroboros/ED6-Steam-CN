import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T2710_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2710   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '哈恩队长'),
    TXT(0x02, '基恩茨副长'),
    TXT(0x03, '士兵库隆'),
    TXT(0x04, '梅尔凯斯'),
    TXT(0x05, '琳塞'),
    TXT(0x06, '巴拉特'),
    TXT(0x07, '约修亚'),
    TXT(0x08, '目标用摄像机'),
    TXT(0x09, '杜南公爵'),
    TXT(0x0A, '管家菲利普'),
    TXT(0x0B, '塞萨尔'),
    TXT(0x0C, '加雷利'),
    TXT(0x0D, '蒂雅'),
    TXT(0x0E, '士兵奥塔'),
    TXT(0x0F, ''),
]

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

# id: 0xFFFF offset: 0x4215
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
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

# id: 0x10001 offset: 0xA8
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

# id: 0x10002 offset: 0x11A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
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

# id: 0x10003 offset: 0x2DA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x2DA
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

# id: 0x10005 offset: 0x31A
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
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_3A9',
    )

    SetChrFlags(0x000B, 0x0080)
    SetChrFlags(0x000C, 0x0080)
    SetChrFlags(0x000D, 0x0080)
    SetChrFlags(0x0013, 0x0080)
    SetChrFlags(0x0014, 0x0080)

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

    SetChrFlags(0x000B, 0x0080)
    SetChrFlags(0x000C, 0x0080)
    SetChrFlags(0x000D, 0x0080)
    SetChrFlags(0x0013, 0x0080)
    SetChrFlags(0x0014, 0x0080)

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

    SetChrFlags(0x000B, 0x0080)
    SetChrFlags(0x000C, 0x0080)
    SetChrFlags(0x000D, 0x0080)
    SetChrFlags(0x0013, 0x0080)
    SetChrFlags(0x0014, 0x0080)

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

    SetChrFlags(0x000B, 0x0080)
    SetChrFlags(0x000C, 0x0080)
    SetChrFlags(0x000D, 0x0080)
    SetChrFlags(0x0013, 0x0080)
    SetChrFlags(0x0014, 0x0080)

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

    SetChrFlags(0x000B, 0x0080)
    SetChrFlags(0x000C, 0x0080)
    SetChrFlags(0x000D, 0x0080)
    SetChrFlags(0x0013, 0x0080)
    SetChrFlags(0x0014, 0x0080)

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

    SetChrPos(0x0008, 4750, 0, 90620, 0)
    SetChrPos(0x000A, -4800, 0, 7900, 90)
    SetChrPos(0x0009, 2900, 0, 95100, 90)
    SetChrFlags(0x000B, 0x0080)
    SetChrFlags(0x000C, 0x0080)
    SetChrFlags(0x000D, 0x0080)
    SetChrFlags(0x0013, 0x0080)
    SetChrFlags(0x0014, 0x0080)

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

    SetChrPos(0x0008, -2810, 0, 92600, 270)
    SetChrPos(0x0009, 96840, 0, 14020, 339)
    SetChrPos(0x000B, -3090, 0, 18660, 270)
    SetChrPos(0x000C, -3860, 0, 19770, 270)
    SetChrPos(0x000D, -2570, 0, 23890, 315)
    TerminateThread(0x0013, 0xFF)
    SetChrChipByIndex(0x0013, 13)
    SetChrFlags(0x0013, 0x0004)
    SetChrFlags(0x0013, 0x0010)
    SetChrPos(0x0013, 95610, 200, 7550, 180)

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

    SetChrPos(0x0008, 0, 0, 5250, 0)
    SetChrFlags(0x0008, 0x0010)
    SetChrPos(0x000A, 92510, 0, 9380, 69)
    SetChrPos(0x0009, 92630, 0, 12500, 90)
    ClearChrFlags(0x000E, 0x0080)
    SetChrPos(0x000E, -680, 0, 5220, 0)
    SetChrPos(0x0013, 320, 0, 23610, 176)
    SetChrPos(0x0014, -3790, 0, 19850, 141)
    SetChrPos(0x000B, 0, 0, 6230, 270)
    SetChrPos(0x000C, 670, 0, 5960, 270)
    SetChrPos(0x000D, -800, 0, 5880, 315)
    CreateThread(0x000B, 0x01, 0x01, 0x0008)
    CreateThread(0x000C, 0x01, 0x01, 0x0009)
    CreateThread(0x000D, 0x01, 0x01, 0x000A)
    SetChrFlags(0x000B, 0x0010)
    SetChrFlags(0x000C, 0x0010)
    SetChrFlags(0x000D, 0x0010)
    SetChrFlags(0x0008, 0x0010)

    Jump('loc_67D')

    def _loc_5F2(): pass

    label('loc_5F2')

    SetChrPos(0x000B, 1596, 0, 12441, 90)
    SetChrPos(0x000C, 1513, 0, 13617, 90)
    SetChrPos(0x000D, 909, 0, 13169, 90)
    SetChrFlags(0x000B, 0x0010)
    SetChrFlags(0x000C, 0x0010)
    SetChrFlags(0x000D, 0x0010)
    SetChrPos(0x0013, 320, 0, 23610, 176)
    SetChrPos(0x0014, -3790, 0, 19850, 141)
    SetChrPos(0x000A, 92510, 0, 9380, 69)
    SetChrPos(0x0009, 92630, 0, 12500, 90)
    SetChrFlags(0x0008, 0x0080)

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

    SetChrPos(0x0008, 1970, 0, 94650, 270)
    SetChrPos(0x000A, -50, 0, 94650, 90)
    SetChrFlags(0x0008, 0x0010)
    SetChrFlags(0x000A, 0x0010)
    SetChrFlags(0x000B, 0x0080)
    SetChrPos(0x000C, -3860, 0, 19770, 270)
    SetChrPos(0x000D, -2570, 0, 23890, 315)
    TerminateThread(0x0013, 0xFF)
    SetChrChipByIndex(0x0013, 13)
    SetChrFlags(0x0013, 0x0004)
    SetChrFlags(0x0013, 0x0010)
    SetChrPos(0x0013, 95610, 200, 7550, 180)

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

    SetChrPos(0x000B, 1596, 0, 12441, 90)
    SetChrPos(0x000C, 1513, 0, 13617, 90)
    SetChrPos(0x000D, 909, 0, 13169, 90)

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
@scena.Code('Init')
def Init():
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
@scena.Code('ReInit')
def ReInit():
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
    ClearChrFlags(0x000A, 0x0010)

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

# id: 0x0008 offset: 0x1B24
@scena.Code('func_08_1B24')
def func_08_1B24():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_1B7B',
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

    Jump('loc_24D5')

    def _loc_1B7B(): pass

    label('loc_1B7B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_1CD7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1C32',
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

    Jump('loc_1CD4')

    def _loc_1C32(): pass

    label('loc_1C32')

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

    def _loc_1CD4(): pass

    label('loc_1CD4')

    Jump('loc_24D5')

    def _loc_1CD7(): pass

    label('loc_1CD7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_1D41',
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

    Jump('loc_24D5')

    def _loc_1D41(): pass

    label('loc_1D41')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_1DEA',
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

    Jump('loc_24D5')

    def _loc_1DEA(): pass

    label('loc_1DEA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 6, 0x506)),
            Expr.Return,
        ),
        'loc_20C0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B2, 0, 0x590)),
            Expr.Return,
        ),
        'loc_1E62',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1E3C',
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

    Jump('loc_1E5F')

    def _loc_1E3C(): pass

    label('loc_1E3C')

    ChrTalk(
        0x00FE,
        (
            '没办法啊，\n',
            '这份工作太累人了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1E5F(): pass

    label('loc_1E5F')

    Jump('loc_20BD')

    def _loc_1E62(): pass

    label('loc_1E62')

    If(
        (
            (Expr.Eval, "OP_29(0x0023, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_1F80',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1F1B',
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

    Jump('loc_1F7D')

    def _loc_1F1B(): pass

    label('loc_1F1B')

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

    def _loc_1F7D(): pass

    label('loc_1F7D')

    Jump('loc_20BD')

    def _loc_1F80(): pass

    label('loc_1F80')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_203C',
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

    Jump('loc_20BD')

    def _loc_203C(): pass

    label('loc_203C')

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

    def _loc_20BD(): pass

    label('loc_20BD')

    Jump('loc_24D5')

    def _loc_20C0(): pass

    label('loc_20C0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 1, 0x501)),
            Expr.Return,
        ),
        'loc_2328',
    )

    SetScenaFlags(ScenaFlag(0x00B2, 0, 0x590))

    If(
        (
            (Expr.Eval, "OP_29(0x0023, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_21E8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2183',
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

    Jump('loc_21E5')

    def _loc_2183(): pass

    label('loc_2183')

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

    def _loc_21E5(): pass

    label('loc_21E5')

    Jump('loc_2325')

    def _loc_21E8(): pass

    label('loc_21E8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_22A4',
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

    Jump('loc_2325')

    def _loc_22A4(): pass

    label('loc_22A4')

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

    def _loc_2325(): pass

    label('loc_2325')

    Jump('loc_24D5')

    def _loc_2328(): pass

    label('loc_2328')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_2466',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0023, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_2456',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_23F2',
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

    Jump('loc_2453')

    def _loc_23F2(): pass

    label('loc_23F2')

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

    def _loc_2453(): pass

    label('loc_2453')

    Jump('loc_2463')

    def _loc_2456(): pass

    label('loc_2456')

    If(
        (
            (Expr.Eval, "OP_29(0x0023, 0x00, 0x08)"),
            Expr.Return,
        ),
        'loc_2463',
    )

    Jump('loc_2463')

    def _loc_2463(): pass

    label('loc_2463')

    Jump('loc_24D5')

    def _loc_2466(): pass

    label('loc_2466')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_24D5',
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

    def _loc_24D5(): pass

    label('loc_24D5')

    TalkEnd(0x0009)

    Return()

# id: 0x0009 offset: 0x24D9
@scena.Code('func_09_24D9')
def func_09_24D9():
    Call(0, 0x000A)

    Return()

# id: 0x000A offset: 0x24DE
@scena.Code('func_0A_24DE')
def func_0A_24DE():
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
        'loc_253C',
    )

    FadeIn(300, 0)
    OP_0D()
    OP_A9(0x34)
    OP_56(0x00)
    TalkEnd(0x0012)

    Return()

    def _loc_253C(): pass

    label('loc_253C')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2556',
    )

    FadeIn(300, 0)
    TalkEnd(0x0012)

    Return()

    def _loc_2556(): pass

    label('loc_2556')

    FadeIn(300, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_265C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2600',
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

    Jump('loc_2659')

    def _loc_2600(): pass

    label('loc_2600')

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

    def _loc_2659(): pass

    label('loc_2659')

    Jump('loc_2AFA')

    def _loc_265C(): pass

    label('loc_265C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_272E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_26D5',
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

    Jump('loc_272B')

    def _loc_26D5(): pass

    label('loc_26D5')

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

    def _loc_272B(): pass

    label('loc_272B')

    Jump('loc_2AFA')

    def _loc_272E(): pass

    label('loc_272E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_27B9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2791',
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

    Jump('loc_27B6')

    def _loc_2791(): pass

    label('loc_2791')

    ChrTalk(
        0x0012,
        (
            '呼，真是的。\n',
            '烦人的消息太多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_27B6(): pass

    label('loc_27B6')

    Jump('loc_2AFA')

    def _loc_27B9(): pass

    label('loc_27B9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_2820',
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

    Jump('loc_2AFA')

    def _loc_2820(): pass

    label('loc_2820')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 6, 0x506)),
            Expr.Return,
        ),
        'loc_287D',
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

    Jump('loc_2AFA')

    def _loc_287D(): pass

    label('loc_287D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 1, 0x501)),
            Expr.Return,
        ),
        'loc_2974',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0023, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_28FF',
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

    Jump('loc_2971')

    def _loc_28FF(): pass

    label('loc_28FF')

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

    def _loc_2971(): pass

    label('loc_2971')

    Jump('loc_2AFA')

    def _loc_2974(): pass

    label('loc_2974')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_29DE',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0023, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_29CE',
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

    Jump('loc_29DB')

    def _loc_29CE(): pass

    label('loc_29CE')

    If(
        (
            (Expr.Eval, "OP_29(0x0023, 0x00, 0x08)"),
            Expr.Return,
        ),
        'loc_29DB',
    )

    Jump('loc_29DB')

    def _loc_29DB(): pass

    label('loc_29DB')

    Jump('loc_2AFA')

    def _loc_29DE(): pass

    label('loc_29DE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_2AFA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2A98',
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

    Jump('loc_2AFA')

    def _loc_2A98(): pass

    label('loc_2A98')

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

    def _loc_2AFA(): pass

    label('loc_2AFA')

    TalkEnd(0x0012)

    Return()

# id: 0x000B offset: 0x2AFE
@scena.Code('func_0B_2AFE')
def func_0B_2AFE():
    Call(0, 0x000C)

    Return()

# id: 0x000C offset: 0x2B03
@scena.Code('func_0C_2B03')
def func_0C_2B03():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_2BFC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2B90',
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

    Jump('loc_2BF9')

    def _loc_2B90(): pass

    label('loc_2B90')

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

    def _loc_2BF9(): pass

    label('loc_2BF9')

    Jump('loc_3658')

    def _loc_2BFC(): pass

    label('loc_2BFC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_2D25',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2C99',
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

    Jump('loc_2D22')

    def _loc_2C99(): pass

    label('loc_2C99')

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

    def _loc_2D22(): pass

    label('loc_2D22')

    Jump('loc_3658')

    def _loc_2D25(): pass

    label('loc_2D25')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_2E11',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2DB8',
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

    Jump('loc_2E0E')

    def _loc_2DB8(): pass

    label('loc_2DB8')

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

    def _loc_2E0E(): pass

    label('loc_2E0E')

    Jump('loc_3658')

    def _loc_2E11(): pass

    label('loc_2E11')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_2EE3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2E88',
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

    Jump('loc_2EE0')

    def _loc_2E88(): pass

    label('loc_2E88')

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

    def _loc_2EE0(): pass

    label('loc_2EE0')

    Jump('loc_3658')

    def _loc_2EE3(): pass

    label('loc_2EE3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 1, 0x501)),
            Expr.Return,
        ),
        'loc_3416',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3372',
    )

    EventBegin(0x00)
    Fade(1000)
    SetChrDirection(0x000A, 90, 0)
    SetChrPos(0x0101, -2800, 0, 6800, 270)
    SetChrPos(0x0102, -2800, 0, 8000, 270)
    SetChrPos(0x0105, -1800, 0, 7200, 270)
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
        (0x00000000, 'loc_30A1'),
        (0x00000001, 'loc_333E'),
        (-1, 'loc_336D'),
    )

    def _loc_30A1(): pass

    label('loc_30A1')

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
    SetChrName('')

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

    Jump('loc_336D')

    def _loc_333E(): pass

    label('loc_333E')

    ChrTalk(
        0x000A,
        (
            '#1940070228V那么，\n',
            '准备好了之后再来找我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_336D')

    def _loc_336D(): pass

    label('loc_336D')

    EventEnd(0x00)

    Jump('loc_3413')

    def _loc_3372(): pass

    label('loc_3372')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 3, 0x503)),
            Expr.Return,
        ),
        'loc_33C5',
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

    Jump('loc_3413')

    def _loc_33C5(): pass

    label('loc_33C5')

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

    def _loc_3413(): pass

    label('loc_3413')

    Jump('loc_3658')

    def _loc_3416(): pass

    label('loc_3416')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_3549',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0023, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_3523',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_34C0',
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

    Jump('loc_3520')

    def _loc_34C0(): pass

    label('loc_34C0')

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

    def _loc_3520(): pass

    label('loc_3520')

    Jump('loc_3546')

    def _loc_3523(): pass

    label('loc_3523')

    If(
        (
            (Expr.Eval, "OP_29(0x0023, 0x00, 0x08)"),
            Expr.Return,
        ),
        'loc_3530',
    )

    Jump('loc_3546')

    def _loc_3530(): pass

    label('loc_3530')

    ChrTalk(
        0x000A,
        (
            '副长他没事吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3546(): pass

    label('loc_3546')

    Jump('loc_3658')

    def _loc_3549(): pass

    label('loc_3549')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_3658',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_362F',
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
    ClearChrFlags(0x000A, 0x0010)

    Jump('loc_3658')

    def _loc_362F(): pass

    label('loc_362F')

    ChrTalk(
        0x000A,
        (
            '好像有一个大人物\n',
            '突然要来这里访问。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3658(): pass

    label('loc_3658')

    TalkEnd(0x000A)

    Return()

# id: 0x000D offset: 0x365C
@scena.Code('func_0D_365C')
def func_0D_365C():
    TalkBegin(0x0013)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_3669',
    )

    Jump('loc_37D0')

    def _loc_3669(): pass

    label('loc_3669')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_3673',
    )

    Jump('loc_37D0')

    def _loc_3673(): pass

    label('loc_3673')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_367D',
    )

    Jump('loc_37D0')

    def _loc_367D(): pass

    label('loc_367D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_3687',
    )

    Jump('loc_37D0')

    def _loc_3687(): pass

    label('loc_3687')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_369B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 6, 0x506)),
            Expr.Return,
        ),
        'loc_3698',
    )

    Jump('loc_3698')

    def _loc_3698(): pass

    label('loc_3698')

    Jump('loc_37D0')

    def _loc_369B(): pass

    label('loc_369B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 1, 0x501)),
            Expr.Return,
        ),
        'loc_36A5',
    )

    Jump('loc_37D0')

    def _loc_36A5(): pass

    label('loc_36A5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_378A',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0023, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_370E',
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

    Jump('loc_3787')

    def _loc_370E(): pass

    label('loc_370E')

    If(
        (
            (Expr.Eval, "OP_29(0x0023, 0x00, 0x08)"),
            Expr.Return,
        ),
        'loc_3760',
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

    Jump('loc_3787')

    def _loc_3760(): pass

    label('loc_3760')

    ChrTalk(
        0x00FE,
        (
            '嗯嗯，\n',
            '那种我行我素的人到处都有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3787(): pass

    label('loc_3787')

    Jump('loc_37D0')

    def _loc_378A(): pass

    label('loc_378A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_37D0',
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

    def _loc_37D0(): pass

    label('loc_37D0')

    TalkEnd(0x0013)

    Return()

# id: 0x000E offset: 0x37D4
@scena.Code('func_0E_37D4')
def func_0E_37D4():
    TalkBegin(0x0014)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_37E1',
    )

    Jump('loc_38D8')

    def _loc_37E1(): pass

    label('loc_37E1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_37EB',
    )

    Jump('loc_38D8')

    def _loc_37EB(): pass

    label('loc_37EB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_37F5',
    )

    Jump('loc_38D8')

    def _loc_37F5(): pass

    label('loc_37F5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_37FF',
    )

    Jump('loc_38D8')

    def _loc_37FF(): pass

    label('loc_37FF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_3813',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 6, 0x506)),
            Expr.Return,
        ),
        'loc_3810',
    )

    Jump('loc_3810')

    def _loc_3810(): pass

    label('loc_3810')

    Jump('loc_38D8')

    def _loc_3813(): pass

    label('loc_3813')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 1, 0x501)),
            Expr.Return,
        ),
        'loc_381D',
    )

    Jump('loc_38D8')

    def _loc_381D(): pass

    label('loc_381D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_389E',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0023, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_386A',
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

    Jump('loc_389B')

    def _loc_386A(): pass

    label('loc_386A')

    If(
        (
            (Expr.Eval, "OP_29(0x0023, 0x00, 0x08)"),
            Expr.Return,
        ),
        'loc_3889',
    )

    ChrTalk(
        0x00FE,
        (
            '真伤脑筋……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_389B')

    def _loc_3889(): pass

    label('loc_3889')

    ChrTalk(
        0x00FE,
        (
            '真伤脑筋……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_389B(): pass

    label('loc_389B')

    Jump('loc_38D8')

    def _loc_389E(): pass

    label('loc_389E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_38D8',
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

    def _loc_38D8(): pass

    label('loc_38D8')

    TalkEnd(0x0014)

    Return()

# id: 0x000F offset: 0x38DC
@scena.Code('func_0F_38DC')
def func_0F_38DC():
    Call(0, 0x0010)

    Return()

# id: 0x0010 offset: 0x38E1
@scena.Code('func_10_38E1')
def func_10_38E1():
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
        'loc_393D',
    )

    OP_0D()
    OP_A9(0x35)
    OP_56(0x00)
    TalkEnd(0x0015)

    Return()

    def _loc_393D(): pass

    label('loc_393D')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_394E',
    )

    TalkEnd(0x0015)

    Return()

    def _loc_394E(): pass

    label('loc_394E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_3AEE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00BA, 1, 0x5D1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3A94',
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
    SetChrName('')
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

    Jump('loc_3AEB')

    def _loc_3A94(): pass

    label('loc_3A94')

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

    def _loc_3AEB(): pass

    label('loc_3AEB')

    Jump('loc_40C9')

    def _loc_3AEE(): pass

    label('loc_3AEE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_3BFD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3B8C',
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

    Jump('loc_3BFA')

    def _loc_3B8C(): pass

    label('loc_3B8C')

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

    def _loc_3BFA(): pass

    label('loc_3BFA')

    Jump('loc_40C9')

    def _loc_3BFD(): pass

    label('loc_3BFD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_3CC3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3C65',
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

    Jump('loc_3CC0')

    def _loc_3C65(): pass

    label('loc_3C65')

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

    def _loc_3CC0(): pass

    label('loc_3CC0')

    Jump('loc_40C9')

    def _loc_3CC3(): pass

    label('loc_3CC3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_3DAB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3D44',
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

    Jump('loc_3DA8')

    def _loc_3D44(): pass

    label('loc_3D44')

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

    def _loc_3DA8(): pass

    label('loc_3DA8')

    Jump('loc_40C9')

    def _loc_3DAB(): pass

    label('loc_3DAB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 6, 0x506)),
            Expr.Return,
        ),
        'loc_3F48',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3F06',
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
        'loc_3DEC',
    )

    ChrTalk(
        0x0015,
        (
            '哟，欢迎来到艾尔·雷登。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3F03')

    def _loc_3DEC(): pass

    label('loc_3DEC')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3E52',
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

    Jump('loc_3F03')

    def _loc_3E52(): pass

    label('loc_3E52')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3EB8',
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

    Jump('loc_3F03')

    def _loc_3EB8(): pass

    label('loc_3EB8')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3F03',
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

    def _loc_3F03(): pass

    label('loc_3F03')

    Jump('loc_3F45')

    def _loc_3F06(): pass

    label('loc_3F06')

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
    def _loc_3F45(): pass

    label('loc_3F45')

    Jump('loc_40C9')

    def _loc_3F48(): pass

    label('loc_3F48')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 1, 0x501)),
            Expr.Return,
        ),
        'loc_3FA4',
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

    Jump('loc_40C9')

    def _loc_3FA4(): pass

    label('loc_3FA4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_4074',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0023, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_4004',
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

    Jump('loc_4071')

    def _loc_4004(): pass

    label('loc_4004')

    If(
        (
            (Expr.Eval, "OP_29(0x0023, 0x00, 0x08)"),
            Expr.Return,
        ),
        'loc_4041',
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

    Jump('loc_4071')

    def _loc_4041(): pass

    label('loc_4041')

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

    def _loc_4071(): pass

    label('loc_4071')

    Jump('loc_40C9')

    def _loc_4074(): pass

    label('loc_4074')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_40C9',
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

    def _loc_40C9(): pass

    label('loc_40C9')

    TalkEnd(0x0015)

    Return()

# id: 0x0011 offset: 0x40CD
@scena.Code('func_11_40CD')
def func_11_40CD():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_4167',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_40EC',
    )

    ChrTurnDirection(0x0102, 0x0001, 400)

    Jump('loc_40F3')

    def _loc_40EC(): pass

    label('loc_40EC')

    ChrTurnDirection(0x0102, 0x0000, 400)

    def _loc_40F3(): pass

    label('loc_40F3')

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

    Jump('loc_41E7')

    def _loc_4167(): pass

    label('loc_4167')

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
        'loc_41E7',
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
    SetChrDirection(0x000E, 0, 0)
    OP_4B(0x000E, 255)
    Sleep(50)

    EventEnd(0x04)

    def _loc_41E7(): pass

    label('loc_41E7')

    Return()

# id: 0x0012 offset: 0x41E8
@scena.Code('func_12_41E8')
def func_12_41E8():
    TalkBegin(0x00FF)
    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
