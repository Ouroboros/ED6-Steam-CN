import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
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
        ('ED6_DT07/CH01310._CH', 'ED6_DT07/CH01310P._CP'),
        ('ED6_DT27/CH03510._CH', 'ED6_DT27/CH03510P._CP'),
        ('ED6_DT27/CH03910._CH', 'ED6_DT27/CH03910P._CP'),
        ('ED6_DT27/CH03920._CH', 'ED6_DT27/CH03920P._CP'),
        ('ED6_DT07/CH01300._CH', 'ED6_DT07/CH01300P._CP'),
        ('ED6_DT07/CH01270._CH', 'ED6_DT07/CH01270P._CP'),
        ('ED6_DT07/CH01143._CH', 'ED6_DT07/CH01143P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01050._CH', 'ED6_DT07/CH01050P._CP'),
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
    ]

# id: 0x10001 offset: 0x102
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '目标用照相机',
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
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            name                = '玲',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '玲的父亲',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0011,
        ),
        ScenaNpcData(
            name                = '玲的母亲',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0012,
        ),
        ScenaNpcData(
            name                = '士兵库隆',
            x                   = -4800,
            z                   = 0,
            y                   = 7900,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '士兵奥塔',
            x                   = 93480,
            z                   = 0,
            y                   = 85530,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '塞萨尔',
            x                   = 95300,
            z                   = 0,
            y                   = 16000,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '基恩茨副队长',
            x                   = 93870,
            z                   = 0,
            y                   = 13580,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '科尼嘉',
            x                   = -3960,
            z                   = 0,
            y                   = 25000,
            direction           = 273,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            name                = '提克',
            x                   = -2580,
            z                   = 0,
            y                   = 16760,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            name                = '莫莉',
            x                   = -2580,
            z                   = 0,
            y                   = 23040,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            name                = '士兵尼克斯',
            x                   = 96770,
            z                   = 0,
            y                   = 14030,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
    )

# id: 0x10002 offset: 0x2A2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x2A2
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -3939,
            y           = -1000,
            z           = 1820,
            range       = 2122,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000019,
        ),
    )

# id: 0x10004 offset: 0x2C2
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
            talkFunctionIndex   = 0x0005,
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
            talkFunctionIndex   = 0x0007,
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
    )

# id: 0x0000 offset: 0x352
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_3A8',
    )

    ChrSetFlags(0x0011, 0x0080)
    ChrSetFlags(0x0012, 0x0080)
    ChrSetFlags(0x0013, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_394',
    )

    ChrSetPos(0x0010, -2580, 0, 93750, 180)
    ChrSetPos(0x0009, -710, 0, 92770, 277)

    Jump('loc_3A5')

    def _loc_394(): pass

    label('loc_394')

    ChrSetPos(0x0010, -2840, 0, 19000, 270)

    def _loc_3A5(): pass

    label('loc_3A5')

    Jump('loc_4F4')

    def _loc_3A8(): pass

    label('loc_3A8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_3E7',
    )

    ChrSetFlags(0x0011, 0x0080)
    ChrSetPos(0x0012, -2710, 0, 18290, 0)
    ChrSetPos(0x0013, -2710, 0, 19610, 180)
    CreateThread(0x0012, 0x00, 0x00, func_02_5E4)
    CreateThread(0x0013, 0x00, 0x00, func_02_5E4)

    Jump('loc_4F4')

    def _loc_3E7(): pass

    label('loc_3E7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_413',
    )

    ChrSetPos(0x0009, -670, 0, 92690, 270)
    ChrSetPos(0x0010, -2400, 0, 92690, 90)

    Jump('loc_4F4')

    def _loc_413(): pass

    label('loc_413')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_41D',
    )

    Jump('loc_4F4')

    def _loc_41D(): pass

    label('loc_41D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_442',
    )

    ChrClearFlags(0x0014, 0x0080)
    ChrSetFlags(0x000D, 0x0080)
    ChrSetPos(0x0010, -4800, 0, 7900, 90)

    Jump('loc_4F4')

    def _loc_442(): pass

    label('loc_442')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_44C',
    )

    Jump('loc_4F4')

    def _loc_44C(): pass

    label('loc_44C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 5, 0x1215)),
            Expr.Return,
        ),
        'loc_4AB',
    )

    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrSetPos(0x000B, 93664, 0, 87456, 180)
    ChrSetPos(0x000A, 95770, 0, 87453, 0)
    ChrSetPos(0x000C, 94561, 0, 88500, 0)
    ChrTurnDirection(0x000A, 0x000B, 0)
    ChrTurnDirection(0x000C, 0x000A, 0)
    ChrSetFlags(0x000C, 0x0010)

    Jump('loc_4F4')

    def _loc_4AB(): pass

    label('loc_4AB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            Expr.Return,
        ),
        'loc_4F4',
    )

    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrSetPos(0x000A, -3410, 0, 19050, 270)
    ChrSetPos(0x000B, -1990, 0, 20610, 135)
    ChrSetPos(0x000C, -1010, 0, 19120, 315)

    def _loc_4F4(): pass

    label('loc_4F4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_506',
    )

    ChrSetFlags(0x0012, 0x0080)
    ChrSetFlags(0x0013, 0x0080)

    def _loc_506(): pass

    label('loc_506')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_53B',
    )

    ChrSetFlags(0x0011, 0x0004)
    ChrSetFlags(0x0011, 0x0040)
    ChrSetPos(0x0011, 95590, 200, 7460, 180)
    ChrSetFlags(0x0011, 0x0010)
    TerminateThread(0x0011, 0x00)
    ChrSetChipByIndex(0x0011, 6)
    ChrSetSubChip(0x0011, 0)

    def _loc_53B(): pass

    label('loc_53B')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000065, 'loc_547'),
        (-1, 'loc_55F'),
    )

    def _loc_547(): pass

    label('loc_547')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 3, 0x1213)),
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_55C',
    )

    MapSetFlags(0x10000000)
    Event(0, func_14_41EF)

    def _loc_55C(): pass

    label('loc_55C')

    Jump('loc_55F')

    def _loc_55F(): pass

    label('loc_55F')

    Return()

# id: 0x0001 offset: 0x560
@scena.Code('func_01_560')
def func_01_560():
    OP_64(0x03, 0x0001)
    OP_1C(0x03, 0x00, 0x001A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_573',
    )

    Jump('loc_5BC')

    def _loc_573(): pass

    label('loc_573')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_57D',
    )

    Jump('loc_5BC')

    def _loc_57D(): pass

    label('loc_57D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_58F',
    )

    OP_65(0x00, 0x0001)
    OP_64(0x03, 0x0001)

    Jump('loc_5BC')

    def _loc_58F(): pass

    label('loc_58F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_5A1',
    )

    OP_64(0x00, 0x0001)
    OP_65(0x03, 0x0001)

    Jump('loc_5BC')

    def _loc_5A1(): pass

    label('loc_5A1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_5AB',
    )

    Jump('loc_5BC')

    def _loc_5AB(): pass

    label('loc_5AB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 5, 0x1215)),
            Expr.Return,
        ),
        'loc_5B5',
    )

    Jump('loc_5BC')

    def _loc_5B5(): pass

    label('loc_5B5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            Expr.Return,
        ),
        'loc_5BC',
    )

    def _loc_5BC(): pass

    label('loc_5BC')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_5D8'),
        (0x00000065, 'loc_5D8'),
        (0x00000066, 'loc_5D8'),
        (0x00000068, 'loc_5D8'),
        (0x0000006A, 'loc_5D8'),
        (-1, 'loc_5E0'),
    )

    def _loc_5D8(): pass

    label('loc_5D8')

    PlaySE(454, 0x01, 0x64)

    Jump('loc_5E3')

    def _loc_5E0(): pass

    label('loc_5E0')

    OP_23(0x01C6)

    def _loc_5E3(): pass

    label('loc_5E3')

    Return()

# id: 0x0002 offset: 0x5E4
@scena.Code('func_02_5E4')
def func_02_5E4():
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
        'loc_609',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_69C')

    def _loc_609(): pass

    label('loc_609')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_622',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_69C')

    def _loc_622(): pass

    label('loc_622')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_63B',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_69C')

    def _loc_63B(): pass

    label('loc_63B')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_654',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_69C')

    def _loc_654(): pass

    label('loc_654')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_66D',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_69C')

    def _loc_66D(): pass

    label('loc_66D')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_686',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_69C')

    def _loc_686(): pass

    label('loc_686')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_69C',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    def _loc_69C(): pass

    label('loc_69C')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_6B1',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_69C')

    def _loc_6B1(): pass

    label('loc_6B1')

    Return()

# id: 0x0003 offset: 0x6B2
@scena.Code('func_03_6B2')
def func_03_6B2():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_6D5',
    )

    OP_8D(0x00FE, -1070, 16329, -4540, 25330, 2000)

    Jump('func_03_6B2')

    def _loc_6D5(): pass

    label('loc_6D5')

    Return()

# id: 0x0004 offset: 0x6D6
@scena.Code('func_04_6D6')
def func_04_6D6():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_729',
    )

    ChrTalk(
        0x00FE,
        (
            '不知道为什么\n',
            '只有我一个人休息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以白天就来这里\n',
            '小酌一杯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_790')

    def _loc_729(): pass

    label('loc_729')

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x00FE,
        (
            '哟，详细情况我没听说，\n',
            '不过据说幽灵骚动解决了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且今天突然不用值勤，\n',
            '真是好事不断啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_790(): pass

    label('loc_790')

    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0x794
@scena.Code('func_05_794')
def func_05_794():
    Call(0, 0x0006)

    Return()

# id: 0x0006 offset: 0x799
@scena.Code('func_06_799')
def func_06_799():
    TalkBegin(0x000D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_8E6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_86C',
    )

    ChrTalk(
        0x000D,
        (
            '卡鲁迪亚隧道中\n',
            '现在是一片漆黑呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '但是，刚才有位旅行者\n',
            '通过了这里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '好像是中央工房的研究者，\n',
            '要通过现在的隧道\n',
            '还真不是一般的有胆量啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '聪明人想的事\n',
            '说实话真搞不懂。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Jump('loc_8E3')

    def _loc_86C(): pass

    label('loc_86C')

    ChrTalk(
        0x000D,
        (
            '这么说来那个人……\n',
            '还带着猫呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '嗯～说不定\n',
            '那是用来避邪什么的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '的、的确有宠物在的话\n',
            '说不定比较安心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8E3(): pass

    label('loc_8E3')

    Jump('loc_DBA')

    def _loc_8E6(): pass

    label('loc_8E6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_A0E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_9B7',
    )

    ChrTalk(
        0x000D,
        (
            '因为门关不上\n',
            '通行者的检查\n',
            '也比平常严格很多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '不过，有通知说\n',
            '要保证游击士们自由通行\n',
            '所以不用担心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '这是协助协会活动\n',
            '的特别措施……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '不过这在以前\n',
            '可是想都想不到的通知呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Jump('loc_A0B')

    def _loc_9B7(): pass

    label('loc_9B7')

    ChrTalk(
        0x000D,
        (
            '各位游击士\n',
            '可以自由通行哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '上面有这样的通知。\n',
            '以前可是想都想不到的事呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A0B(): pass

    label('loc_A0B')

    Jump('loc_DBA')

    def _loc_A0E(): pass

    label('loc_A0E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_AB5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_A65',
    )

    ChrTalk(
        0x000D,
        (
            '蔡斯的地震\n',
            '据说已经稳定了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '唉，地震\n',
            '没到这边来真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_AB2')

    def _loc_A65(): pass

    label('loc_A65')

    ChrTalk(
        0x000D,
        (
            '蔡斯的地震\n',
            '据说已经稳定了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '好像是中央工房发布的，\n',
            '大概没错吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_AB2(): pass

    label('loc_AB2')

    Jump('loc_DBA')

    def _loc_AB5(): pass

    label('loc_AB5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_B7E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_B12',
    )

    ChrTalk(
        0x000D,
        (
            '刚才从司令部\n',
            '发来了紧急联络……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '之后队长他们\n',
            '就没从房间里出来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B7B')

    def _loc_B12(): pass

    label('loc_B12')

    ChrTalk(
        0x000D,
        (
            '刚才从司令部\n',
            '发来了紧急联络……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '之后队长他们\n',
            '就没从房间里出来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '发、发生什么事了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_B7B(): pass

    label('loc_B7B')

    Jump('loc_DBA')

    def _loc_B7E(): pass

    label('loc_B7E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_C42',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_BCD',
    )

    ChrTalk(
        0x000D,
        (
            '蔡斯\n',
            '据说发生了地震。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '希、希望它不要\n',
            '可别过来啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C3F')

    def _loc_BCD(): pass

    label('loc_BCD')

    ChrTalk(
        0x000D,
        (
            '蔡斯好像\n',
            '发生了地震呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '其、其实我……\n',
            '最讨厌地震了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '因为地面会摇摆不定哦？\n',
            '当然会令人不安吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_C3F(): pass

    label('loc_C3F')

    Jump('loc_DBA')

    def _loc_C42(): pass

    label('loc_C42')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_CE1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_C95',
    )

    ChrTalk(
        0x000D,
        (
            '看起来还是\n',
            '游客很少啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '卢安的选举\n',
            '结束之前都是这样吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CDE')

    def _loc_C95(): pass

    label('loc_C95')

    ChrTalk(
        0x000D,
        (
            '呀，欢迎来到\n',
            '艾尔·雷登关所。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '客人还是那么少，\n',
            '就请自便吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_CDE(): pass

    label('loc_CDE')

    Jump('loc_DBA')

    def _loc_CE1(): pass

    label('loc_CE1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_D26',
    )

    ChrTalk(
        0x000D,
        (
            '队长和副队长\n',
            '两人一起在叹息呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '有什么烦恼事吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DBA')

    def _loc_D26(): pass

    label('loc_D26')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_DBA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_D6C',
    )

    ChrTalk(
        0x000D,
        (
            '现在游客很少。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '好象因为卢安选举\n',
            '的影响呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DBA')

    def _loc_D6C(): pass

    label('loc_D6C')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x000D,
        (
            '呀，欢迎来到\n',
            '艾尔·雷登关所。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '现在游客很少,\n',
            '可以悠闲欣赏瀑布哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_DBA(): pass

    label('loc_DBA')

    TalkEnd(0x000D)

    Return()

# id: 0x0007 offset: 0xDBE
@scena.Code('func_07_DBE')
def func_07_DBE():
    Call(0, 0x0008)

    Return()

# id: 0x0008 offset: 0xDC3
@scena.Code('func_08_DC3')
def func_08_DC3():
    TalkBegin(0x000E)
    Call(6, 0x0006)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_DDD',
    )

    OP_A9(0x79)
    TalkEnd(0x000E)

    Return()

    def _loc_DDD(): pass

    label('loc_DDD')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_DEE',
    )

    TalkEnd(0x000E)

    Return()

    def _loc_DEE(): pass

    label('loc_DEE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_E9F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_E67',
    )

    ChrTalk(
        0x000E,
        (
            '其他的部队\n',
            '好像发来了通讯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '难道有什么事件吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '不过，最近\n',
            '发生事件倒也不觉得稀奇……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Jump('loc_E9C')

    def _loc_E67(): pass

    label('loc_E67')

    ChrTalk(
        0x000E,
        (
            '其他的部队\n',
            '好像发来了通讯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '有什么事件吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E9C(): pass

    label('loc_E9C')

    Jump('loc_149F')

    def _loc_E9F(): pass

    label('loc_E9F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_F7B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_F1E',
    )

    ChrTalk(
        0x000E,
        (
            '欢迎光临。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '导力器的恢复装置\n',
            '似乎也没有作用呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '如果累了就不要勉强，\n',
            '最好在旅店休息一下哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Jump('loc_F78')

    def _loc_F1E(): pass

    label('loc_F1E')

    ChrTalk(
        0x000E,
        (
            '导力器的恢复装置\n',
            '似乎也没有作用呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '既然是这样的状况，\n',
            '可要多多注意不能勉强哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F78(): pass

    label('loc_F78')

    Jump('loc_149F')

    def _loc_F7B(): pass

    label('loc_F7B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_102C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_FDE',
    )

    ChrTalk(
        0x000E,
        (
            '其实雷斯顿要塞\n',
            '好像也发生了地震。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '虽然没有损害，\n',
            '听说这事还是吓一大跳。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1029')

    def _loc_FDE(): pass

    label('loc_FDE')

    ChrTalk(
        0x000E,
        (
            '其实雷斯顿要塞\n',
            '好像也发生了地震。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '难怪那时队长他们\n',
            '脸都青了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_1029(): pass

    label('loc_1029')

    Jump('loc_149F')

    def _loc_102C(): pass

    label('loc_102C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_1100',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_108B',
    )

    ChrTalk(
        0x000E,
        (
            '司令部发来的联络\n',
            '是经常有的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '如果次次都脸色发青\n',
            '那可没法工作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10FD')

    def _loc_108B(): pass

    label('loc_108B')

    ChrTalk(
        0x000E,
        (
            '库隆那家伙真是\n',
            '太神经质了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '司令部发来的联络\n',
            '是经常有的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '如果次次都脸色发青\n',
            '那可没法工作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_10FD(): pass

    label('loc_10FD')

    Jump('loc_149F')

    def _loc_1100(): pass

    label('loc_1100')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_11D6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_115D',
    )

    ChrTalk(
        0x000E,
        (
            '卢安在选举，\n',
            '而蔡斯是地震……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '不过处在中间的\n',
            '这个关所还真平静啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11D3')

    def _loc_115D(): pass

    label('loc_115D')

    ChrTalk(
        0x000E,
        (
            '蔡斯地震的事。\n',
            '这里也在传言呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '虽说规模好像不大\n',
            '但感觉真诡异啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '王国居然会地震\n',
            '实在是很少见的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_11D3(): pass

    label('loc_11D3')

    Jump('loc_149F')

    def _loc_11D6(): pass

    label('loc_11D6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_1273',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1231',
    )

    ChrTalk(
        0x000E,
        (
            '最近的街道\n',
            '比以前更加危险了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '不要勉强，出发前\n',
            '最好休息一下哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1270')

    def _loc_1231(): pass

    label('loc_1231')

    ChrTalk(
        0x000E,
        (
            '欢迎光临。\n',
            '来得正好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '刚才就一直犯困\n',
            '真是没辙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_1270(): pass

    label('loc_1270')

    Jump('loc_149F')

    def _loc_1273(): pass

    label('loc_1273')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_1315',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_12CE',
    )

    ChrTalk(
        0x000E,
        (
            '诞辰庆典的时候\n',
            '虽然忙得够呛……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '到现在回想起来，\n',
            '还是热闹好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1312')

    def _loc_12CE(): pass

    label('loc_12CE')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x000E,
        (
            '欢迎光临。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '现在我们这里有很多空床，\n',
            '随时都可以住下哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1312(): pass

    label('loc_1312')

    Jump('loc_149F')

    def _loc_1315(): pass

    label('loc_1315')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_136D',
    )

    ChrTalk(
        0x000E,
        (
            '前阵子来的一家人\n',
            '看起来真是幸福啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '看到那样的家庭\n',
            '我也开始憧憬了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_149F')

    def _loc_136D(): pass

    label('loc_136D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 5, 0x1215)),
            Expr.Return,
        ),
        'loc_144A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_13BE',
    )

    ChrTalk(
        0x000E,
        (
            '家族旅行\n',
            '真令人羡慕呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '啊啊，我也想\n',
            '早点拥有家庭啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1447')

    def _loc_13BE(): pass

    label('loc_13BE')

    ChrSetDirection(0x000E, 0, 0)
    OP_4A(0x000B, 255)
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    ChrTalk(
        0x000E,
        (
            '#5441410001V那么3人\n',
            '住宿一晚对吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0721230003V啊啊，就这样拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#5441410002V那么请在这边签字……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4B(0x000B, 255)

    def _loc_1447(): pass

    label('loc_1447')

    Jump('loc_149F')

    def _loc_144A(): pass

    label('loc_144A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_149F',
    )

    ChrTalk(
        0x000E,
        (
            '欢迎光临。\n',
            '这里是为旅客准备的投宿设施。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '如果想住的话\n',
            '请跟我说一声。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_149F(): pass

    label('loc_149F')

    TalkEnd(0x000E)

    Return()

# id: 0x0009 offset: 0x14A3
@scena.Code('func_09_14A3')
def func_09_14A3():
    Call(0, 0x000A)

    Return()

# id: 0x000A offset: 0x14A8
@scena.Code('func_0A_14A8')
def func_0A_14A8():
    TalkBegin(0x000F)
    Call(6, 0x0004)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_14C2',
    )

    OP_A9(0x78)
    TalkEnd(0x000F)

    Return()

    def _loc_14C2(): pass

    label('loc_14C2')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_14D3',
    )

    TalkEnd(0x000F)

    Return()

    def _loc_14D3(): pass

    label('loc_14D3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_15E3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_158C',
    )

    ChrTalk(
        0x000F,
        (
            '看来这状况\n',
            '还要继续延长的样子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '这、这么说导力炉子\n',
            '暂时也不能使用了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '过几天菜单\n',
            '也需要重新定制了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '……作为厨师，\n',
            '有失败的感觉，真不甘心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Jump('loc_15E0')

    def _loc_158C(): pass

    label('loc_158C')

    ChrTalk(
        0x000F,
        (
            '过几天菜单\n',
            '也需要重新定制了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '嗯，在此之前导力器\n',
            '恢复原状才是最重要的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_15E0(): pass

    label('loc_15E0')

    Jump('loc_1BA4')

    def _loc_15E3(): pass

    label('loc_15E3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_16D2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1673',
    )

    ChrTalk(
        0x000F,
        (
            '没想到导力器\n',
            '竟然不能使用……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '这里还好，\n',
            '但蔡斯一定发生大骚动了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '因为那里是不管什么都用导力\n',
            '驱动的城市嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Jump('loc_16CF')

    def _loc_1673(): pass

    label('loc_1673')

    ChrTalk(
        0x000F,
        (
            '导力器不能使用，\n',
            '蔡斯一定发生大骚动了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '因为那里是不管什么都用导力\n',
            '驱动的城市嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_16CF(): pass

    label('loc_16CF')

    Jump('loc_1BA4')

    def _loc_16D2(): pass

    label('loc_16D2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_172E',
    )

    ChrTalk(
        0x000F,
        (
            '利贝尔的大地\n',
            '好像终于平静下来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '正是这样的时候，\n',
            '才要感谢空之女神啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1BA4')

    def _loc_172E(): pass

    label('loc_172E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_17D7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_1789',
    )

    ChrTalk(
        0x000F,
        (
            '司令部好像传来了什么\n',
            '重要的联络。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '这个一定\n',
            '也是和地震相关的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17D4')

    def _loc_1789(): pass

    label('loc_1789')

    ChrTalk(
        0x000F,
        (
            '司令部好像传来了什么\n',
            '重要的联络。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '副队长气势汹汹\n',
            '飞奔出去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_17D4(): pass

    label('loc_17D4')

    Jump('loc_1BA4')

    def _loc_17D7(): pass

    label('loc_17D7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_1884',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_1830',
    )

    ChrTalk(
        0x000F,
        (
            '蔡斯的地震\n',
            '似乎还在持续啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '架子上的瓶子\n',
            '最好还是整理一下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1881')

    def _loc_1830(): pass

    label('loc_1830')

    ChrTalk(
        0x000F,
        (
            '蔡斯的地震\n',
            '似乎还在持续啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '以防扩展到这里\n',
            '还是整理一下架子上吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_1881(): pass

    label('loc_1881')

    Jump('loc_1BA4')

    def _loc_1884(): pass

    label('loc_1884')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_18E0',
    )

    ChrTalk(
        0x000F,
        (
            '虽然在王国很少见，\n',
            '地震可是很可怕的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '因为地面会突然\n',
            '喀哒喀哒地摇晃啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1BA4')

    def _loc_18E0(): pass

    label('loc_18E0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_193C',
    )

    ChrTalk(
        0x000F,
        (
            '基恩茨副队长\n',
            '好像在办理通行手续。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '嘿嘿，这可有趣了。\n',
            '待会儿去嘲弄他吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1BA4')

    def _loc_193C(): pass

    label('loc_193C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_19F9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_19A1',
    )

    ChrTalk(
        0x000F,
        (
            '尽管如此，\n',
            '那家人看起来好幸福啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '感觉像是跟画里描绘的\n',
            '理想的家庭一样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19F6')

    def _loc_19A1(): pass

    label('loc_19A1')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x000F,
        (
            '前阵子很少有\n',
            '来了一家子客人的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '这里离城市很远，\n',
            '很少有客人带孩子来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_19F6(): pass

    label('loc_19F6')

    Jump('loc_1BA4')

    def _loc_19F9(): pass

    label('loc_19F9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_1BA4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_1A47',
    )

    ChrTalk(
        0x000F,
        (
            '看过有名的瀑布了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '现在可以不受打扰\n',
            '好好观赏哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1BA4')

    def _loc_1A47(): pass

    label('loc_1A47')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1AD0',
    )

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
            TXT(0x00, '◇前篇看过说服公爵的任务\n'),
            TXT(0x01, '◇没看过说服公爵的任务\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_56(0x00)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1AC0'),
        (0x00000001, 'loc_1AC8'),
        (-1, 'loc_1AD0'),
    )

    def _loc_1AC0(): pass

    label('loc_1AC0')

    OP_28(0x0023, 0x03, 0x10)

    Jump('loc_1AD0')

    def _loc_1AC8(): pass

    label('loc_1AC8')

    OP_28(0x0023, 0x04, 0x10)

    Jump('loc_1AD0')

    def _loc_1AD0(): pass

    label('loc_1AD0')

    If(
        (
            (Expr.Eval, "OP_29(0x0023, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_1B49',
    )

    ChrTalk(
        0x000F,
        (
            '哎呀，你是\n',
            '曾经来过的游击士吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '现在客人也少,\n',
            '请好好休息一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '如果肚子饿了\n',
            '尝尝新菜如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1BA4')

    def _loc_1B49(): pass

    label('loc_1B49')

    ChrTalk(
        0x000F,
        (
            '哎呀，欢迎。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '现在客人也少,\n',
            '请好好休息一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '如果肚子饿了\n',
            '试试新菜单如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1BA4(): pass

    label('loc_1BA4')

    TalkEnd(0x000F)

    Return()

# id: 0x000B offset: 0x1BA8
@scena.Code('func_0B_1BA8')
def func_0B_1BA8():
    TalkBegin(0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_1C40',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1BFD',
    )

    ChrTalk(
        0x00FE,
        (
            '非常时期还袭击学校\n',
            '真不是人做的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是太过分了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    Jump('loc_1C3D')

    def _loc_1BFD(): pass

    label('loc_1BFD')

    ChrTalk(
        0x00FE,
        (
            '这种非常时期\n',
            '居然还袭击学校……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还有这种\n',
            '过分的人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C3D(): pass

    label('loc_1C3D')

    Jump('loc_21B5')

    def _loc_1C40(): pass

    label('loc_1C40')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1C98',
    )

    ChrTalk(
        0x00FE,
        (
            '协会派来\n',
            '巡视的小哥很有用呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这个状况下，都不知道\n',
            '会发生什么事呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_21B5')

    def _loc_1C98(): pass

    label('loc_1C98')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_1D6C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_1CF7',
    )

    ChrTalk(
        0x00FE,
        (
            '差不多该制订\n',
            '面向签字仪式的警备计划了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不提出文件\n',
            '司令部也很烦呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D69')

    def _loc_1CF7(): pass

    label('loc_1CF7')

    ChrTalk(
        0x00FE,
        (
            '哟，看来地震\n',
            '好像安定了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总算能松一口气\n',
            '进行下一项工作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '必须制订\n',
            '面向签字仪式的警备计划了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_1D69(): pass

    label('loc_1D69')

    Jump('loc_21B5')

    def _loc_1D6C(): pass

    label('loc_1D6C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_1E21',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_1DBF',
    )

    ChrTalk(
        0x00FE,
        (
            '没想到雷斯顿要塞\n',
            '都会有地震……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '到底是没法\n',
            '当作巧合啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E1E')

    def _loc_1DBF(): pass

    label('loc_1DBF')

    ChrTalk(
        0x00FE,
        (
            '没想到雷斯顿要塞\n',
            '都会有地震……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '到底是没法\n',
            '当作巧合啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，是我多心了吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_1E1E(): pass

    label('loc_1E1E')

    Jump('loc_21B5')

    def _loc_1E21(): pass

    label('loc_1E21')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_1EF3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_1E80',
    )

    ChrTalk(
        0x00FE,
        (
            '沃尔费堡垒之后\n',
            '是圣海姆门吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '竟然能这样像有目的似的\n',
            '发起地震吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1EF0')

    def _loc_1E80(): pass

    label('loc_1E80')

    ChrTalk(
        0x00FE,
        (
            '沃尔费堡垒之后\n',
            '圣海姆门发生地震啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哦，这么说\n',
            '还忘了蔡斯呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那个城市好像\n',
            '也发生地震了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_1EF0(): pass

    label('loc_1EF0')

    Jump('loc_21B5')

    def _loc_1EF3(): pass

    label('loc_1EF3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_1FA0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_1F4E',
    )

    ChrTalk(
        0x0010,
        (
            '最近沃尔费堡垒\n',
            '好像地震了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '在那里当副队长的\n',
            '格温和我是同期呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F9D')

    def _loc_1F4E(): pass

    label('loc_1F4E')

    ChrTalk(
        0x0010,
        (
            '最近沃尔费堡垒\n',
            '好像地震了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '嘿嘿，那里的士兵们\n',
            '想必也惊慌失措吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_1F9D(): pass

    label('loc_1F9D')

    Jump('loc_21B5')

    def _loc_1FA0(): pass

    label('loc_1FA0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_204B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_1FF6',
    )

    ChrTalk(
        0x0010,
        (
            '为什么当副队长的我\n',
            '会在前台……是吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '……唉，一言难尽啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2048')

    def _loc_1FF6(): pass

    label('loc_1FF6')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x0010,
        (
            '王立学院里\n',
            '有犯罪组织的人员潜伏吗?',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '总觉得这个事件，\n',
            '好像还有幕后啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2048(): pass

    label('loc_2048')

    Jump('loc_21B5')

    def _loc_204B(): pass

    label('loc_204B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_20DF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_207B',
    )

    ChrTalk(
        0x00FE,
        (
            '尼克斯的话好像\n',
            '是真的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_20DC')

    def _loc_207B(): pass

    label('loc_207B')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '从队长那儿听说了，\n',
            '尼克斯的话好像是真的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呀～真伤脑筋。\n',
            '我还狠狠地训了他一顿呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_20DC(): pass

    label('loc_20DC')

    Jump('loc_21B5')

    def _loc_20DF(): pass

    label('loc_20DF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_21B5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_213C',
    )

    ChrTalk(
        0x00FE,
        (
            '我们的士兵\n',
            '最近很懈怠啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '明明情报部的余党\n',
            '和空贼团都还没抓住呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_21B5')

    def _loc_213C(): pass

    label('loc_213C')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '我们的士兵\n',
            '最近很懈怠啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '前阵子还有人在站岗中睡大觉，\n',
            '真是个闹得满城风雨的白痴呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是要想想办法了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_21B5(): pass

    label('loc_21B5')

    TalkEnd(0x0010)

    Return()

# id: 0x000C offset: 0x21B9
@scena.Code('func_0C_21B9')
def func_0C_21B9():
    TalkBegin(0x0011)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_2279',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_222D',
    )

    ChrTalk(
        0x00FE,
        (
            '话说回来，这个关所\n',
            '是正适合读书的地方呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '和王都的咖啡店一样，\n',
            '我可是给五星评价的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2276')

    def _loc_222D(): pass

    label('loc_222D')

    ChrTalk(
        0x00FE,
        (
            '察觉到的时候\n',
            '已经待了很久了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，差不多该\n',
            '准备回王都了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    def _loc_2276(): pass

    label('loc_2276')

    Jump('loc_268D')

    def _loc_2279(): pass

    label('loc_2279')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_2306',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_22C7',
    )

    ChrTalk(
        0x00FE,
        (
            '哎，也好。\n',
            '反正和我没什么关系。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好了，专心读书吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2303')

    def _loc_22C7(): pass

    label('loc_22C7')

    ChrTalk(
        0x00FE,
        (
            '总觉得士兵们\n',
            '的行动很慌张呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '发生什么事了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    def _loc_2303(): pass

    label('loc_2303')

    Jump('loc_268D')

    def _loc_2306(): pass

    label('loc_2306')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_23A2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_2354',
    )

    ChrTalk(
        0x00FE,
        (
            '哎，也好。\n',
            '反正和我没什么关系。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好了，专心读书吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_239F')

    def _loc_2354(): pass

    label('loc_2354')

    ChrTalk(
        0x00FE,
        (
            '嗯～沃尔费堡垒\n',
            '发生地震了吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那个士兵\n',
            '声音好像稍微大了点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    def _loc_239F(): pass

    label('loc_239F')

    Jump('loc_268D')

    def _loc_23A2(): pass

    label('loc_23A2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_2402',
    )

    ChrTalk(
        0x00FE,
        (
            '唔，不知为何感觉好像\n',
            '比平常更能集中精神读书了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '远方回响的水声\n',
            '好像不错呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_268D')

    def _loc_2402(): pass

    label('loc_2402')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_24E8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_2465',
    )

    ChrTalk(
        0x00FE,
        (
            '我经常在王都的咖啡店里\n',
            '读书……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好象在这样有开放感的地方\n',
            '读书也不错呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24E5')

    def _loc_2465(): pass

    label('loc_2465')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '我经常在王都的咖啡店里\n',
            '读书……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好象在这样有开放感的地方\n',
            '读书也不错呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '即使读同样的文章\n',
            '感受的印象也不一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_24E5(): pass

    label('loc_24E5')

    Jump('loc_268D')

    def _loc_24E8(): pass

    label('loc_24E8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 3, 0x1213)),
            Expr.Return,
        ),
        'loc_2584',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_2524',
    )

    ChrTalk(
        0x00FE,
        (
            '看着幸福的家庭\n',
            '我也感受到幸福的心情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2581')

    def _loc_2524(): pass

    label('loc_2524')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '哈哈，正觉着热闹呢，\n',
            '原来有人带孩子来了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看起来真开心啊。\n',
            '好久没来旅行了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2581(): pass

    label('loc_2581')

    Jump('loc_268D')

    def _loc_2584(): pass

    label('loc_2584')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_268D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_25E3',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然在利贝尔通讯\n',
            '看过照片……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '若不真正站在这里\n',
            '就感受不到这魄力啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_268D')

    def _loc_25E3(): pass

    label('loc_25E3')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '听说选举期间，卢安的旅游景点\n',
            '到处都闲置着呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我正打算悠闲地读读书，\n',
            '就从王都赶来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '话虽如此……\n',
            '这瀑布真的是很壮观啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '水声好像在身体中回响呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_268D(): pass

    label('loc_268D')

    TalkEnd(0x0011)

    Return()

# id: 0x000D offset: 0x2691
@scena.Code('func_0D_2691')
def func_0D_2691():
    TalkBegin(0x0012)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_27F1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_2719',
    )

    ChrTalk(
        0x00FE,
        (
            '王都之旅就推迟一点，\n',
            '先去哈肯大门吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽说如此，利贝尔的珍珠\n',
            '格兰赛尔城也难以舍弃……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呜～真头痛啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_27EE')

    def _loc_2719(): pass

    label('loc_2719')

    ChrTalk(
        0x00FE,
        (
            '嗯～接着去哪里呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '圣海姆门也不错，\n',
            '但也想看看格兰赛尔城呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，王都有签字仪式\n',
            '警备可能很严格呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样的话干脆去柏斯的\n',
            '哈肯大门看看吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '作为百日战役史迹巡游旅，\n',
            '哈肯大门不可或缺哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    def _loc_27EE(): pass

    label('loc_27EE')

    Jump('loc_2B2A')

    def _loc_27F1(): pass

    label('loc_27F1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_2902',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_2879',
    )

    ChrTalk(
        0x00FE,
        (
            '卡鲁迪亚隧道\n',
            '也想走一次看看……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过从卢安乘定期船\n',
            '要放心很多呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这还是和茉莉商量一下\n',
            '再决定比较好呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_28FF')

    def _loc_2879(): pass

    label('loc_2879')

    ChrTalk(
        0x00FE,
        (
            '之后虽然打算去\n',
            '蔡斯地区……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一考虑发现必须通过\n',
            '卡鲁迪亚隧道才行呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然也想走一次看看，\n',
            '嗯～但还是觉得有点恐怖呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    def _loc_28FF(): pass

    label('loc_28FF')

    Jump('loc_2B2A')

    def _loc_2902(): pass

    label('loc_2902')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_2A39',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_297C',
    )

    ChrTalk(
        0x00FE,
        (
            '最近，茉莉经常看\n',
            '利贝尔通讯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是都只看照片\n',
            '却不读报道。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为她实在是\n',
            '不喜欢印刷字嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A36')

    def _loc_297C(): pass

    label('loc_297C')

    ChrTalk(
        0x00FE,
        (
            '最近，茉莉经常看\n',
            '利贝尔通讯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是都只看照片\n',
            '却不读报道。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '书迷的我正好相反，\n',
            '她很讨厌印刷字。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '孩提时代还经常一起\n',
            '看图画书来着……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '到底在哪里\n',
            '分道扬镳了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    def _loc_2A36(): pass

    label('loc_2A36')

    Jump('loc_2B2A')

    def _loc_2A39(): pass

    label('loc_2A39')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_2B2A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_2AA8',
    )

    ChrTalk(
        0x00FE,
        (
            '我们正循着百日战役\n',
            '这条线在巡游史迹。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '艾尔·雷登关所\n',
            '是和书里写的一样美丽的地方哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2B2A')

    def _loc_2AA8(): pass

    label('loc_2AA8')

    ChrTalk(
        0x00FE,
        (
            '呼～这里就是\n',
            '那个艾尔·雷登啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '历史悠久的石筑建筑物\n',
            '和罗蔡水道的瀑布……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呀～真是和书里写的一样\n',
            '美丽的地方啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    def _loc_2B2A(): pass

    label('loc_2B2A')

    TalkEnd(0x0012)

    Return()

# id: 0x000E offset: 0x2B2E
@scena.Code('func_0E_2B2E')
def func_0E_2B2E():
    TalkBegin(0x0013)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_2C07',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_2B8E',
    )

    ChrTalk(
        0x00FE,
        (
            '去哈肯大门\n',
            '说不定是个好主意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好难得来到这里，\n',
            '才有这种感觉的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2C04')

    def _loc_2B8E(): pass

    label('loc_2B8E')

    ChrTalk(
        0x00FE,
        (
            '雪白的格兰赛尔城啊。\n',
            '真想把它拍下来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是圣海姆门\n',
            '也确实很有魅力呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '从亚宁堡上\n',
            '一览平原一定很棒。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    def _loc_2C04(): pass

    label('loc_2C04')

    Jump('loc_2E9A')

    def _loc_2C07(): pass

    label('loc_2C07')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_2CEF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_2C6C',
    )

    ChrTalk(
        0x00FE,
        (
            '瀑布那样运动的\n',
            '拍摄对象果然很难拍呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '利贝尔通讯的摄影记者\n',
            '是怎样做的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2CEC')

    def _loc_2C6C(): pass

    label('loc_2C6C')

    ChrTalk(
        0x00FE,
        (
            '瀑布那样运动的\n',
            '拍摄对象果然很难拍呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '想表现出跃动感，\n',
            '却变成模模糊糊的照片……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '拘泥焦点的话\n',
            '又会丧失速度感。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    def _loc_2CEC(): pass

    label('loc_2CEC')

    Jump('loc_2E9A')

    def _loc_2CEF(): pass

    label('loc_2CEF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_2DEA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_2D45',
    )

    ChrTalk(
        0x00FE,
        (
            '利贝尔通讯的照片真厉害啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是能拍成那样\n',
            '就毫无怨言了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2DE7')

    def _loc_2D45(): pass

    label('loc_2D45')

    ChrTalk(
        0x00FE,
        (
            '利贝尔通讯的照片真厉害啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是能拍成那样\n',
            '就毫无怨言了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这么说来以前的利贝尔通讯\n',
            '有这个关所的照片呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好，我也要拍出\n',
            '不输给那个的照片。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    def _loc_2DE7(): pass

    label('loc_2DE7')

    Jump('loc_2E9A')

    def _loc_2DEA(): pass

    label('loc_2DEA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_2E9A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_2E43',
    )

    ChrTalk(
        0x00FE,
        (
            '我的梦想\n',
            '是成为摄影记者。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '此次的史迹巡游\n',
            '也是为此修行的一环。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2E9A')

    def _loc_2E43(): pass

    label('loc_2E43')

    ChrTalk(
        0x00FE,
        (
            '和青梅竹马的提克一起\n',
            '在做史迹巡游。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '多多拍摄有名的建筑物\n',
            '磨练拍摄手法哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    def _loc_2E9A(): pass

    label('loc_2E9A')

    TalkEnd(0x0013)

    Return()

# id: 0x000F offset: 0x2E9E
@scena.Code('func_0F_2E9E')
def func_0F_2E9E():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_2FCA',
    )

    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2F66',
    )

    ChrTalk(
        0x00FE,
        (
            '正好学院事件\n',
            '刚刚发来了联络。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '据说平安的解决了，\n',
            '本该感到喜悦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但乘着这阵混乱再引起的骚动\n',
            '以后说不定还会发生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以大家都不能松懈，\n',
            '还需要继续严格警戒。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_2FC4')

    def _loc_2F66(): pass

    label('loc_2F66')

    ChrTalk(
        0x00FE,
        (
            '像学院事件一样的骚动\n',
            '以后说不定还会发生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以大家都不能松懈，\n',
            '还需要继续严格警戒。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2FC4(): pass

    label('loc_2FC4')

    TalkEnd(0x0009)

    Jump('loc_3905')

    def _loc_2FCA(): pass

    label('loc_2FCA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_3105',
    )

    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_30AD',
    )

    ChrTalk(
        0x00FE,
        (
            '通信机虽说恢复原状了，\n',
            '但情报还不足……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总之强化关所的警备\n',
            '是最优先的行动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为大门持续\n',
            '关不上啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '卡鲁迪亚隧道的照明也灭了，\n',
            '现在是一片漆黑。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '草率进入会要人命的。\n',
            '请充分注意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_30FF')

    def _loc_30AD(): pass

    label('loc_30AD')

    ChrTalk(
        0x00FE,
        (
            '现在确保关所的安全\n',
            '是最优先的行动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们慌慌张张的\n',
            '只能让市民更加动摇。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_30FF(): pass

    label('loc_30FF')

    TalkEnd(0x0009)

    Jump('loc_3905')

    def _loc_3105(): pass

    label('loc_3105')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 2, 0x1212)),
            Expr.Return,
        ),
        'loc_3901',
    )

    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_3260',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_31AF',
    )

    ChrTalk(
        0x0009,
        (
            '配合签字仪式的日期\n',
            '关所也将强化警备。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '不仅仅是那个犯罪组织，\n',
            '情报部的残存势力也令人在意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '王国军的上层部\n',
            '会变得神经质也是当然。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_325D')

    def _loc_31AF(): pass

    label('loc_31AF')

    ChrTalk(
        0x0009,
        (
            '连续发生的地震\n',
            '也已经平息下来的样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '要塞似乎也没有受到太大的损坏，\n',
            '不管怎样，可以安心一下了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '这下总算平息了，条约签字仪式的\n',
            '准备工作也能顺利进行下去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_325D(): pass

    label('loc_325D')

    Jump('loc_38FB')

    def _loc_3260(): pass

    label('loc_3260')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_333B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_32B6',
    )

    ChrTalk(
        0x0009,
        (
            '雷斯顿要塞\n',
            '据说有很强的地震。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '虽说还好没有受到什么损害……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3338')

    def _loc_32B6(): pass

    label('loc_32B6')

    ChrTalk(
        0x0009,
        (
            '据说雷斯顿要塞\n',
            '遭遇了很强的地震。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '现在正好这边也\n',
            '刚刚有联络哟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '虽然有不祥的预感，\n',
            '但是没有想到真的成为现实……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_3338(): pass

    label('loc_3338')

    Jump('loc_38FB')

    def _loc_333B(): pass

    label('loc_333B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_3407',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_338C',
    )

    ChrTalk(
        0x0009,
        (
            '圣海姆门也\n',
            '好像地震了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '不知为何，\n',
            '总有种不祥的预感。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3404')

    def _loc_338C(): pass

    label('loc_338C')

    ChrTalk(
        0x0009,
        (
            '圣海姆门也\n',
            '好像地震了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '沃尔费堡垒之后，\n',
            '在军队设施这是第二次了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '为何不知道，\n',
            '有种很糟糕的预感哟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_3404(): pass

    label('loc_3404')

    Jump('loc_38FB')

    def _loc_3407(): pass

    label('loc_3407')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_34EE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_3472',
    )

    ChrTalk(
        0x0009,
        (
            '关于那个犯罪组织\n',
            '王国军也开始了调查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '为了不引起市民的不安，\n',
            '搜查是秘密进行的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_34EB')

    def _loc_3472(): pass

    label('loc_3472')

    ChrTalk(
        0x0009,
        (
            '哦哦，游击士的各位啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '关于那个犯罪组织\n',
            '王国军也在调查呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '为了不引起市民的不安，\n',
            '单纯是秘密搜查而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_34EB(): pass

    label('loc_34EB')

    Jump('loc_38FB')

    def _loc_34EE(): pass

    label('loc_34EE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_35D8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_354F',
    )

    ChrTalk(
        0x00FE,
        (
            '那个事件\n',
            '总算也解决了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然还有些疑惑，\n',
            '但现在就让我说声辛苦了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_35D5')

    def _loc_354F(): pass

    label('loc_354F')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '呀，那个事件\n',
            '总算解决了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '话说回来，犯罪组织的一员\n',
            '竟然潜伏在王立学院……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真没想到幽灵骚乱\n',
            '竟然联系着这样的事件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_35D5(): pass

    label('loc_35D5')

    Jump('loc_38FB')

    def _loc_35D8(): pass

    label('loc_35D8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_36BE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_362F',
    )

    ChrTalk(
        0x00FE,
        (
            '我们也会致力于\n',
            '增加与协会的合作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '也请各位游击士\n',
            '多多配合。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_36BB')

    def _loc_362F(): pass

    label('loc_362F')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '哎呀，是你们啊。\n',
            '幽灵骚动的调查有进展吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这边如果掌握了什么\n',
            '也会马上联系协会的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样的搜查\n',
            '军队和协会的合作是很重要的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_36BB(): pass

    label('loc_36BB')

    Jump('loc_38FB')

    def _loc_36BE(): pass

    label('loc_36BE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 3, 0x1213)),
            Expr.Return,
        ),
        'loc_3851',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_371F',
    )

    ChrTalk(
        0x00FE,
        (
            '还以为尼克斯那家伙\n',
            '一定是睡迷糊了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯～这个债\n',
            '看来不得不找机会还了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_384E')

    def _loc_371F(): pass

    label('loc_371F')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '得到什么情报了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1000F嗯，看来好像\n',
            '真的出现了什么。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_3789',
    )

    ChrTalk(
        0x0106,
        (
            '#050F虽然还不清楚原形。',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_37AB')

    def _loc_3789(): pass

    label('loc_3789')

    ChrTalk(
        0x0103,
        (
            '#020F嗯嗯，虽然还不清楚原形。',
            TxtCtl.Enter,
        ),
    )

    def _loc_37AB(): pass

    label('loc_37AB')

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔～是吗……\n',
            '对不起尼克斯了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这个债\n',
            '不得不找机会还啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1000F那么，我们\n',
            '就这样继续调查了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '队长，今天谢谢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊啊，查出什么的话\n',
            '请再联络。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_384E(): pass

    label('loc_384E')

    Jump('loc_38FB')

    def _loc_3851(): pass

    label('loc_3851')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_38FB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_389D',
    )

    ChrTalk(
        0x00FE,
        (
            '隧道入口在关所屋顶。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '请沿着柜台旁边的\n',
            '台阶上去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_38FB')

    def _loc_389D(): pass

    label('loc_389D')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '目击了白影的\n',
            '是名叫尼克斯的士兵。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他现在在卡鲁迪亚隧道\n',
            '入口放哨\n',
            '直接问他就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_38FB(): pass

    label('loc_38FB')

    TalkEnd(0x0009)

    Jump('loc_3905')

    def _loc_3901(): pass

    label('loc_3901')

    Call(0, 0x0013)
    def _loc_3905(): pass

    label('loc_3905')

    Return()

# id: 0x0010 offset: 0x3906
@scena.Code('func_10_3906')
def func_10_3906():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_393E',
    )

    ChrTalk(
        0x000A,
        (
            '#0220201573V#260F下次碰到再一起玩哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_397B')

    def _loc_393E(): pass

    label('loc_393E')

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    ChrTalk(
        0x000A,
        (
            '#0220201573V#260F哎呀，大姐姐。\n',
            '下次碰到再一起玩哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_397B(): pass

    label('loc_397B')

    TalkEnd(0x000A)

    Return()

# id: 0x0011 offset: 0x397F
@scena.Code('func_11_397F')
def func_11_397F():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_39D9',
    )

    ChrTalk(
        0x000B,
        (
            '#0721230001V#1363F这次是偶尔\n',
            '服务家族啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0721230002V平时总是出差嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3A63')

    def _loc_39D9(): pass

    label('loc_39D9')

    ChrSetDirection(0x00FE, 180, 0)
    OP_4A(0x000E, 255)
    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x000E,
        (
            '#5441410001V那么３人\n',
            '住宿一晚对吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0721230003V#1360F啊啊，拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#5441410002V那么请在这边签字……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4B(0x000E, 255)

    def _loc_3A63(): pass

    label('loc_3A63')

    TalkEnd(0x000B)

    Return()

# id: 0x0012 offset: 0x3A67
@scena.Code('func_12_3A67')
def func_12_3A67():
    TalkBegin(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_3AA3',
    )

    ChrTalk(
        0x000C,
        (
            '#0730860016V#1372F很快就完了\n',
            '乖乖待着哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3AD3')

    def _loc_3AA3(): pass

    label('loc_3AA3')

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    ChrTalk(
        0x000C,
        (
            '#0730860017V#1372F喂，玲。\n',
            '乖乖待着啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3AD3(): pass

    label('loc_3AD3')

    TalkEnd(0x000C)

    Return()

# id: 0x0013 offset: 0x3AD7
@scena.Code('func_13_3AD7')
def func_13_3AD7():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3AF1',
    )

    Call(0, 0x0018)
    FadeIn(0, 0)

    def _loc_3AF1(): pass

    label('loc_3AF1')

    EventBegin(0x00)
    OP_4A(0x0009, 255)
    Fade(1000)
    ChrSetPos(0x0101, 2980, 0, 91080, 90)
    ChrSetPos(0x00F7, 2410, 0, 90010, 90)

    ExecExpressionWithVar(
        0x65,
        (
            (Expr.GetChrWork, 0x101, 0x1),
            (Expr.GetChrWork, 0x9, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x66,
        (
            (Expr.GetChrWork, 0x101, 0x2),
            (Expr.GetChrWork, 0x9, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x67,
        (
            (Expr.GetChrWork, 0x101, 0x3),
            (Expr.GetChrWork, 0x9, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010201427V#1011F#5P那个，打扰一下。\n',
            '游击士协会的…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0101, 400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3C28',
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
            TXT(0x00, '【◇说服公爵事件未完成】\n'),
            TXT(0x01, '【◇说服公爵事件完成】\n'),
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
        (0x00000000, 'loc_3C0F'),
        (0x00000001, 'loc_3C17'),
        (-1, 'loc_3C1F'),
    )

    def _loc_3C0F(): pass

    label('loc_3C0F')

    OP_28(0x0023, 0x03, 0x10)

    Jump('loc_3C1F')

    def _loc_3C17(): pass

    label('loc_3C17')

    OP_28(0x0023, 0x04, 0x10)

    Jump('loc_3C1F')

    def _loc_3C1F(): pass

    label('loc_3C1F')

    FadeIn(300, 0)

    def _loc_3C28(): pass

    label('loc_3C28')

    If(
        (
            (Expr.Eval, "OP_29(0x0023, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_3D40',
    )

    ChrTalk(
        0x0009,
        (
            '#1860201428V啊啊，辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0009,
        (
            '#1860201429V啊，记得你是\n',
            '上次公爵阁下来时的那位游击士……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010201430V#1016F#5P啊哈哈。\n',
            '还记得啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1860201431V那当然，从没像那时一样\n',
            '感受到你们游击士\n',
            '的可贵嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1860201432V今天什么事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3D97')

    def _loc_3D40(): pass

    label('loc_3D40')

    TalkSetChrName('哈恩队长')

    ChrTalk(
        0x0009,
        (
            '#1860201428V啊啊，辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1860201434V没见过你啊，\n',
            '今天有什么事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3D97(): pass

    label('loc_3D97')

    ChrTalk(
        0x0101,
        (
            '#0010201435V#1002F#5P其实，听说这个关所\n',
            '有士兵看见了『白影』，\n',
            '好象就是你部队里的人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1860201436V怎么，都传到\n',
            '协会那儿去了吗?',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1860201437V真是丢脸啊。\n',
            '太难为情了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010201438V#1004F#5P难为情？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1860201439V当然是睡糊涂了，\n',
            '才说看见幽灵啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1860201440V如此松懈怠慢,\n',
            '一旦出事可要出人命啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1860201441V而部下的松懈\n',
            '也是我当队长的责任。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_3F7E',
    )

    ChrTalk(
        0x0106,
        (
            '#0050201442V#053F真不巧，这是\n',
            '你武断行事了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050201443V#050F那个幽灵，在卢安各地\n',
            '都有被目击呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3FEE')

    def _loc_3F7E(): pass

    label('loc_3F7E')

    ChrTalk(
        0x0103,
        (
            '#0030201444V#020F哎呀，这可是\n',
            '队长武断行事了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030201445V关于那个幽灵\n',
            '现在卢安各地\n',
            '好像都有人目击到哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3FEE(): pass

    label('loc_3FEE')

    ChrTalk(
        0x0009,
        (
            '#1860201446V什么……？',
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
            '把嘉恩拜托调查的事\n',
            '向哈恩队长说明了。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x0009,
        (
            '#1860201447V是这样吗?\n',
            '我还以为一定是\n',
            '睡糊涂了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1860201448V看来，这确实\n',
            '是我主观臆断了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1860201449V对不起尼克斯了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010201450V#1011F#5P尼克斯就是\n',
            '目击了白影的士兵？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1860201451V啊啊，对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1860201452V他现在在卡鲁迪亚隧道\n',
            '入口处放哨，\n',
            '直接问他就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1860201453V请你们跟他说\n',
            '我相信他了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010201454V#1006F#5P嗯，明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0009, 0, 400)
    OP_4B(0x0009, 255)
    SetScenaFlags(ScenaFlag(0x0242, 2, 0x1212))
    OP_28(0x0082, 0x02, 0x0002)
    OP_28(0x0082, 0x01, 0x0004)
    EventEnd(0x00)

    Return()

# id: 0x0014 offset: 0x41EF
@scena.Code('func_14_41EF')
def func_14_41EF():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4200',
    )

    Call(0, 0x0018)

    def _loc_4200(): pass

    label('loc_4200')

    EventBegin(0x00)
    MapClearFlags(0x00000001)
    CameraMove(-8390, 1000, 6270, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrSetPos(0x000A, -3410, 0, 19050, 270)
    ChrSetPos(0x000B, -1990, 0, 20610, 225)
    ChrSetPos(0x000C, -1260, 0, 19050, 270)
    ChrSetDirection(0x0000, 90, 0)
    OP_4A(0x000A, 255)
    OP_4A(0x000B, 255)
    OP_4A(0x000C, 255)
    ChrSetPos(0x0101, -7600, 3000, 8050, 149)
    ChrSetPos(0x00F7, -8180, 3000, 8050, 180)
    ChrSetRGBAMask(0x0101, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x00F7, 255, 255, 255, 0, 0)
    CreateThread(0x0101, 0x00, 0x00, func_16_596C)
    Sleep(600)

    CreateThread(0x00F7, 0x00, 0x00, func_17_59A7)

    @scena.Lambda('lambda_42EA')
    def lambda_42EA():
        CameraMove(-3350, 0, 5190, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_42EA)

    @scena.Lambda('lambda_4302')
    def lambda_4302():
        OP_67(0, 8000, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_4302)

    FadeIn(2000, 0)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0000)

    NpcTalk(
        0x000A,
        '少女的声音',
        (
            '#0220201506V#6P哇，好厉害哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000A,
        '少女的声音',
        (
            '#0220201507V#6P爸爸、妈妈、这边哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x00F7, 0x0000)

    @scena.Lambda('lambda_4390')
    def lambda_4390():
        CameraMove(-2740, 0, 19390, 3000)

        ExitThread()

    DispatchAsync(0x000A, 0x0000, lambda_4390)

    @scena.Lambda('lambda_43A8')
    def lambda_43A8():
        OP_67(0, 4890, -10000, 3000)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_43A8)

    @scena.Lambda('lambda_43C0')
    def lambda_43C0():
        CameraSetDistance(3330, 2000)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_43C0)

    @scena.Lambda('lambda_43D0')
    def lambda_43D0():
        OP_6E(262, 2000)

        ExitThread()

    DispatchAsync(0x000A, 0x0003, lambda_43D0)

    ChrTurnDirection(0x0101, 0x000A, 400)
    ChrTurnDirection(0x00F7, 0x000A, 400)
    WaitForThreadExit(0x000B, 0x0001)

    @scena.Lambda('lambda_43F3')
    def lambda_43F3():
        ChrTurnDirection(0x000B, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_43F3)

    WaitForThreadExit(0x000C, 0x0001)

    @scena.Lambda('lambda_4406')
    def lambda_4406():
        ChrTurnDirection(0x000C, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_4406)

    WaitForThreadExit(0x000C, 0x0001)
    WaitForThreadExit(0x000A, 0x0000)
    WaitForThreadExit(0x000A, 0x0001)
    WaitForThreadExit(0x000A, 0x0002)
    WaitForThreadExit(0x000A, 0x0003)

    NpcTalk(
        0x000B,
        '男性',
        (
            '#0720201508V#1363F#2P喂喂，跑那么快\n',
            '当心跌倒哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000C,
        '女性',
        (
            '#0730201509V#1371F#6P哈哈哈。\n',
            '但是真的好漂亮嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000C, 0x000B, 400)
    Sleep(300)

    NpcTalk(
        0x000C,
        '女性',
        (
            '#0730201510V#1372F#6P谢谢你，老公。\n',
            '能带我们一起来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000B, 180, 400)
    Sleep(300)

    NpcTalk(
        0x000B,
        '男性',
        (
            '#0720201511V#1361F#2P哪里，总是让你们\n',
            '感到寂寞嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0720201512V这是应该有的家庭责任啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x0101, -2060, 0, 7000, 0)
    ChrSetPos(0x00F7, -850, 0, 5500, 0)

    @scena.Lambda('lambda_457F')
    def lambda_457F():
        CameraMove(-2390, 0, 14690, 1800)

        ExitThread()

    DispatchAsync(0x000A, 0x0000, lambda_457F)

    @scena.Lambda('lambda_4597')
    def lambda_4597():
        OP_67(0, 4890, -10000, 1800)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_4597)

    Sleep(1000)

    @scena.Lambda('lambda_45B4')
    def lambda_45B4():
        ChrWalkTo(0x0101, -1960, 0, 9150, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_45B4)

    @scena.Lambda('lambda_45CF')
    def lambda_45CF():
        ChrWalkTo(0x00F7, -380, 0, 8440, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_45CF)

    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x00F7, 0x0001)
    ChrTurnDirection(0x0101, 0x000A, 0)
    ChrTurnDirection(0x00F7, 0x000A, 0)
    WaitForThreadExit(0x000A, 0x0000)
    WaitForThreadExit(0x000A, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010201513V#1017F#5P（嗯～\n',
            '　关系很好的家庭呢。)',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010201514V(是来旅行的吧？)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_46BD',
    )

    ChrTalk(
        0x0106,
        (
            '#0050201515V#051F#6P（啊啊，看起来是呢。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050201516V(说不定\n',
            ' 是从外国来的呢。)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4718')

    def _loc_46BD(): pass

    label('loc_46BD')

    ChrTalk(
        0x0103,
        (
            '#0030201517V#021F#6P（呵呵，大概是吧。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030201518V#020F（说不定\n',
            '　还是外国人呢。)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4718(): pass

    label('loc_4718')

    SetScenaFlags(ScenaFlag(0x0242, 4, 0x1214))

    NpcTalk(
        0x000A,
        '女孩子',
        (
            '#0220201519V#261F#8P哇……\n',
            '好厉害啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220201520V只是看着\n',
            '就感觉要被吸引过去一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x000A, 0x0101, 400)

    NpcTalk(
        0x000A,
        '女孩子',
        (
            '#0220201521V#265F#8P对了，这位姐姐。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220201522V这个瀑布叫什么名字？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220201523V这么多水\n',
            '是从哪儿来的呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010201524V#1016F#5P哟，突然袭击啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_484A')
    def lambda_484A():
        CameraMove(-3310, 0, 18760, 2000)

        ExitThread()

    DispatchAsync(0x000A, 0x0000, lambda_484A)

    @scena.Lambda('lambda_4862')
    def lambda_4862():
        OP_67(0, 4890, -10000, 2000)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_4862)

    @scena.Lambda('lambda_487A')
    def lambda_487A():
        ChrWalkTo(0x0101, -2810, 0, 17030, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_487A)

    @scena.Lambda('lambda_4895')
    def lambda_4895():
        ChrTurnDirection(0x000B, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_4895)

    ChrTurnDirection(0x000C, 0x0101, 400)

    @scena.Lambda('lambda_48AA')
    def lambda_48AA():
        ChrWalkTo(0x00F7, -990, 0, 15960, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_48AA)

    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x00F7, 0x0001)
    TerminateThread(0x000B, 0x00)
    TerminateThread(0x000B, 0x01)
    WaitForThreadExit(0x000A, 0x0000)
    WaitForThreadExit(0x000A, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010201525V#1006F#6P这瀑布叫『艾尔·雷登』哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010201526V是从瓦雷利亚湖，通过太古的水道\n',
            '流到这里来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000A,
        '女孩子',
        (
            '#0220201527V#265F#5P瓦雷利亚湖我知道的！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220201528V飞船到达之前看到的\n',
            '很大很大的湖对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010201529V#1004F#6P嗯，是啊……',
            TxtCtl.Enter,
            '\n',
            '#1000F难道你们是从外国来的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000A,
        '女孩子',
        (
            '#0220201530V#264F#5P说玲吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220201531V#263F嗯嗯，是啊。\n',
            '玲是从很远的地方来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010201532V#1001F#6P是吗。　\n',
            '你叫玲啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010201533V好可爱的名字哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0220201534V#261F#5P哈哈哈，是吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220201535V因为是爸爸和妈妈\n',
            '给取的名字嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000C, 0x000A, 400)
    Sleep(300)

    ChrTalk(
        0x000C,
        (
            '#0730201536V#1372F#4P玲，给姐姐\n',
            '添麻烦可不行哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0720201537V#1363F哈哈，不好意思。\n',
            '尽给素不相识的人添麻烦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x000C, 400)

    ChrTalk(
        0x000A,
        (
            '#0220201538V#262F#5P哼～\n',
            '玲才没有添麻烦呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010201539V#1016F#6P啊哈哈。\n',
            '请别介意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_4C32',
    )

    ChrTalk(
        0x0106,
        (
            '#0050201540V#051F#6P你们好像是从外国来的，\n',
            '是来利贝尔旅行的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4C6D')

    def _loc_4C32(): pass

    label('loc_4C32')

    ChrTalk(
        0x0103,
        (
            '#0030201541V#020F#6P你们好像是外国人，\n',
            '来利贝尔旅行？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4C6D(): pass

    label('loc_4C6D')

    ChrTurnDirection(0x000C, 0x00F7, 400)

    ChrTalk(
        0x000B,
        (
            '#0720201542V#1361F嗯嗯，我是贸易商人\n',
            '经常会来利贝尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0720201543V每次来访，都对这个国家的美丽\n',
            '惊叹不已……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0730201544V#1370F#4P所以这次，正好有商谈\n',
            '就顺便把我和女儿都带来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0730201545V#1371F呵呵，很少有呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010201546V#1017F#6P啊哈哈……\n',
            '真好啊，家庭关系这么好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0101, 400)

    ChrTalk(
        0x000A,
        (
            '#0220201547V#261F#5P哈哈哈，羡慕吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220201548V#265F爸爸虽然经常出差\n',
            '但总会买很多\n',
            '土产回来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220201549V妈妈平时也都笑眯眯的\n',
            '制作好吃的饭菜哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010201550V#1008F#6P这样啊。\n',
            '嗯～姐姐好羡慕哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0720201551V#1363F哈哈，真是的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0730201552V#1372F#4P不好意思……\n',
            '她还这么孩子气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0220201553V#260F#5P唔～能告诉我名字吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220201554V玲要怎么\n',
            '称呼姐姐呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010201555V#1006F#6P哦，被问到姓名\n',
            '不回答可就失礼了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010201556V我叫艾丝蒂尔。\n',
            '艾丝蒂尔·布莱特。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010201557V#1015F是游击士……\n',
            '嗯～游击士你知道吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0220201558V#266F#5P真是的，别当我是小孩子！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220201559V#265F不过姐姐\n',
            '是游击士啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220201560V可以消灭\n',
            '可怕的魔兽吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010201561V#1006F#6P嗯，有时候会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0720201562V#1362F哦……\n',
            '是游击士啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0730201563V#1371F#4P小小年纪就当上游击士\n',
            '实在是很厉害啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010201564V#1016F#6P啊哈哈……\n',
            '还只是个新人而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_5183',
    )

    ChrTalk(
        0x0106,
        (
            '#0050201565V#051F#6P利贝尔各都市\n',
            '都有协会的支部。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050201566V如果旅行中，有什么困难\n',
            '随时都可以去求助。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_51EF')

    def _loc_5183(): pass

    label('loc_5183')

    ChrTalk(
        0x0103,
        (
            '#0030201567V#020F#6P利贝尔五大都市\n',
            '都有协会的支部。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030201568V如果旅行中，有什么困难\n',
            '请随时去求助。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_51EF(): pass

    label('loc_51EF')

    ChrTalk(
        0x000B,
        (
            '#0720201569V#1361F多谢照顾了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0720201570V#1360F……那么我们\n',
            '去办住宿手续了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000C, 0x000A, 400)

    ChrTalk(
        0x000C,
        (
            '#0730201571V#1370F#4P来，玲，要走了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x000C, 400)

    ChrTalk(
        0x000A,
        (
            '#0220201572V#262F#5P呜～还想和姐姐\n',
            '多聊会儿呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0101, 400)
    Sleep(300)

    ChrTalk(
        0x000A,
        (
            '#0220201573V#265F#5P还有哦，姐姐。\n',
            '下次碰到了再一起玩哦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010201574V#1006F#6P嗯，好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0220201575V#261F#5P哈哈哈，好高兴哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220201576V#265F再见哦，艾丝蒂尔姐姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_537F')
    def lambda_537F():
        ChrTurnDirection(0x0101, 0x000A, 0)
        Yield()

        Jump('lambda_537F')

    DispatchAsync2(0x0101, 0x0001, lambda_537F)

    @scena.Lambda('lambda_5390')
    def lambda_5390():
        ChrTurnDirection(0x00F7, 0x000B, 0)
        Yield()

        Jump('lambda_5390')

    DispatchAsync2(0x00F7, 0x0001, lambda_5390)

    CreateThread(0x000B, 0x01, 0x00, func_15_5925)
    Sleep(1000)

    @scena.Lambda('lambda_53AD')
    def lambda_53AD():
        CameraMove(-1800, 0, 18780, 2000)

        ExitThread()

    DispatchAsync(0x000A, 0x0000, lambda_53AD)

    @scena.Lambda('lambda_53C5')
    def lambda_53C5():
        OP_67(0, 4890, -10000, 200)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_53C5)

    CreateThread(0x000C, 0x01, 0x00, func_15_5925)
    Sleep(500)

    CreateThread(0x000A, 0x01, 0x00, func_15_5925)
    Sleep(200)

    WaitForThreadExit(0x000A, 0x0000)
    WaitForThreadExit(0x000A, 0x0001)
    WaitForThreadExit(0x000A, 0x0002)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x00F7, 0x01)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_548C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_548C',
    )

    FadeOut(0, 0, -1)

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
            TXT(0x00, '【◇『听过孤儿院孩子们的话』状态】\n'),
            TXT(0x01, '【◇不变更】\n'),
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
        'loc_5483',
    )

    SetScenaFlags(ScenaFlag(0x0243, 2, 0x121A))

    def _loc_5483(): pass

    label('loc_5483')

    FadeIn(300, 0)

    def _loc_548C(): pass

    label('loc_548C')

    OP_69(0x0101, 1000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_56CD',
    )

    ChrTalk(
        0x0106,
        (
            '#0050201577V#051F#6P真老成的小鬼啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050201578V比提妲\n',
            '还小一两岁的样子吗?',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010201579V#1017F#5P嗯，差不多吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010201580V………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0106, 0x0101, 400)
    Sleep(400)

    ChrTalk(
        0x0106,
        (
            '#0050201581V#050F#6P怎么了。\n',
            '想起大叔了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0106, 400)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010201582V#1016F#5P嘿嘿……有点。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010201583V#1025F还有，初遇约修亚的时候，\n',
            '差不多也是那孩子那么大的时候呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Return,
        ),
        'loc_566D',
    )

    OP_28(0x0082, 0x01, 0x0400)

    ChrTalk(
        0x0106,
        (
            '#0050201584V#053F#6P是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050201585V#051F……目击情报全部收集到了,\n',
            '差不多该回卢安了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_56CA')

    def _loc_566D(): pass

    label('loc_566D')

    ChrTalk(
        0x0106,
        (
            '#0050201584V#053F#6P是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050201587V#051F……好了。\n',
            '赶快去问问\n',
            '下一条目击情报吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_56CA(): pass

    label('loc_56CA')

    Jump('loc_58F4')

    def _loc_56CD(): pass

    label('loc_56CD')

    ChrTalk(
        0x0103,
        (
            '#0030201588V#021F#6P哈哈哈。\n',
            '好老成的女孩子啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030201589V比提妲\n',
            '稍微小一点吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010201579V#1017F#5P嗯，差不多吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010201591V………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x0101, 400)
    Sleep(400)

    ChrTalk(
        0x0103,
        (
            '#0030201592V#027F#6P呵呵。\n',
            '想起老师的事了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010201582V#1016F#5P嘿嘿……有点。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010201583V#1025F还有，遇到约修亚\n',
            '差不多也是那孩子那么大的时候呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Return,
        ),
        'loc_589C',
    )

    OP_28(0x0082, 0x01, 0x0400)

    ChrTalk(
        0x0103,
        (
            '#0030201595V#026F#6P……是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030201596V#020F目击情报全部收集到了,\n',
            '差不多该回卢安了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_58F4')

    def _loc_589C(): pass

    label('loc_589C')

    ChrTalk(
        0x0103,
        (
            '#0030201595V#026F#6P……是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030201598V#020F对了……\n',
            '去探听下一条目击情报吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_58F4(): pass

    label('loc_58F4')

    ChrTalk(
        0x0101,
        (
            '#0010201599V#1006F#5P嗯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4B(0x000A, 255)
    OP_4B(0x000B, 255)
    OP_4B(0x000C, 255)
    SetScenaFlags(ScenaFlag(0x0242, 5, 0x1215))
    EventEnd(0x00)

    Return()

# id: 0x0015 offset: 0x5925
@scena.Code('func_15_5925')
def func_15_5925():
    ChrSetDirection(0x00FE, 90, 400)
    ChrWalkTo(0x00FE, 2630, 0, 20980, 2000, 0x00)

    @scena.Lambda('lambda_5946')
    def lambda_5946():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_5946)

    ChrWalkTo(0x00FE, 3520, 0, 21050, 2000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x0016 offset: 0x596C
@scena.Code('func_16_596C')
def func_16_596C():
    @scena.Lambda('lambda_5972')
    def lambda_5972():
        ChrSetRGBAMask(0x0101, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0000, lambda_5972)

    ChrWalkTo(0x0101, -7530, 1000, 4990, 2000, 0x00)
    ChrWalkTo(0x0101, -3290, 0, 5030, 2000, 0x00)

    Return()

# id: 0x0017 offset: 0x59A7
@scena.Code('func_17_59A7')
def func_17_59A7():
    @scena.Lambda('lambda_59AD')
    def lambda_59AD():
        ChrSetRGBAMask(0x00F7, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0000, lambda_59AD)

    ChrWalkTo(0x00F7, -7860, 1000, 4330, 2000, 0x00)
    ChrWalkTo(0x00F7, -3810, 0, 3790, 2000, 0x00)

    Return()

# id: 0x0018 offset: 0x59E2
@scena.Code('func_18_59E2')
def func_18_59E2():
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
        (0x00000000, 'loc_5A5C'),
        (0x00000001, 'loc_5A62'),
        (-1, 'loc_5A68'),
    )

    def _loc_5A5C(): pass

    label('loc_5A5C')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_5A68')

    def _loc_5A62(): pass

    label('loc_5A62')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_5A68')

    def _loc_5A68(): pass

    label('loc_5A68')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_5A76',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    Jump('loc_5A7A')

    def _loc_5A76(): pass

    label('loc_5A76')

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    def _loc_5A7A(): pass

    label('loc_5A7A')

    Return()

# id: 0x0019 offset: 0x5A7B
@scena.Code('func_19_5A7B')
def func_19_5A7B():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5BB6',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_5B14',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5AA6',
    )

    ChrTurnDirection(0x0106, 0x0001, 400)

    Jump('loc_5AAD')

    def _loc_5AA6(): pass

    label('loc_5AA6')

    ChrTurnDirection(0x0106, 0x0000, 400)

    def _loc_5AAD(): pass

    label('loc_5AAD')

    ChrTalk(
        0x0106,
        (
            '#0050220141V#050F前边就是卢安地区了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050220142V没时间去别的地方了。\n',
            '现在还是乖乖回去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5B9B')

    def _loc_5B14(): pass

    label('loc_5B14')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5B2A',
    )

    ChrTurnDirection(0x0103, 0x0001, 400)

    Jump('loc_5B31')

    def _loc_5B2A(): pass

    label('loc_5B2A')

    ChrTurnDirection(0x0103, 0x0000, 400)

    def _loc_5B31(): pass

    label('loc_5B31')

    ChrTalk(
        0x0103,
        (
            '#0030220143V#020F穿过这里就是卢安地区了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030220144V没时间去其它的地方了，\n',
            '现在还是乖乖回去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_5B9B(): pass

    label('loc_5B9B')

    ChrMoveToRelative(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_5BB6(): pass

    label('loc_5BB6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5ECB',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5CD2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_5C43',
    )

    ChrTalk(
        0x0108,
        (
            '#0080240201V#070F虽说徒步移动是修行，\n',
            '但那样太浪费时间。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080240202V要去王都\n',
            '还是用定期船比较好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5CCF')

    def _loc_5C43(): pass

    label('loc_5C43')

    ChrTalk(
        0x0108,
        (
            '#0080240203V#070F这边是卢安地区吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080240204V虽说徒步移动是修行，\n',
            '但那样太浪费时间。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080240202V要去王都\n',
            '还是用定期船比较好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))

    def _loc_5CCF(): pass

    label('loc_5CCF')

    Jump('loc_5EB0')

    def _loc_5CD2(): pass

    label('loc_5CD2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_5DC8',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5CEF',
    )

    ChrTurnDirection(0x0106, 0x0001, 400)

    Jump('loc_5CF6')

    def _loc_5CEF(): pass

    label('loc_5CEF')

    ChrTurnDirection(0x0106, 0x0000, 400)

    def _loc_5CF6(): pass

    label('loc_5CF6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Return,
        ),
        'loc_5D68',
    )

    ChrTalk(
        0x0106,
        (
            '#0050240206V#053F……要走过去\n',
            '说实话太浪费时间。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050240207V#050F要去王都\n',
            '还是去定期船飞船坪吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5DC5')

    def _loc_5D68(): pass

    label('loc_5D68')

    ChrTalk(
        0x0106,
        (
            '#0050220141V#050F前边就是卢安地区了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050240209V要去王都\n',
            '还是去定期船飞船坪吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 5, 0xD))

    def _loc_5DC5(): pass

    label('loc_5DC5')

    Jump('loc_5EB0')

    def _loc_5DC8(): pass

    label('loc_5DC8')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5DDE',
    )

    ChrTurnDirection(0x0103, 0x0001, 400)

    Jump('loc_5DE5')

    def _loc_5DDE(): pass

    label('loc_5DDE')

    ChrTurnDirection(0x0103, 0x0000, 400)

    def _loc_5DE5(): pass

    label('loc_5DE5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Return,
        ),
        'loc_5E57',
    )

    ChrTalk(
        0x0103,
        (
            '#0030240210V#026F……要走过去\n',
            '说实话是浪费时间。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030240211V#020F要去王都\n',
            '还是去定期船飞船坪吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5EB0')

    def _loc_5E57(): pass

    label('loc_5E57')

    ChrTalk(
        0x0103,
        (
            '#0030240212V#020F这边是卢安地区吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030240213V要去王都\n',
            '还是去定期船飞船坪吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))

    def _loc_5EB0(): pass

    label('loc_5EB0')

    ChrMoveToRelative(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_5ECB(): pass

    label('loc_5ECB')

    Return()

# id: 0x001A offset: 0x5ECC
@scena.Code('func_1A_5ECC')
def func_1A_5ECC():
    TalkBegin(0x00FF)
    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
