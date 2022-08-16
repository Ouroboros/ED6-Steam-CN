import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T4130_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4130   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4130.x'
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
        ('ED6_DT07/CH02060._CH', 'ED6_DT07/CH02060P._CP'),
        ('ED6_DT07/CH01023._CH', 'ED6_DT07/CH01023P._CP'),
        ('ED6_DT07/CH01100._CH', 'ED6_DT07/CH01100P._CP'),
        ('ED6_DT07/CH01150._CH', 'ED6_DT07/CH01150P._CP'),
        ('ED6_DT07/CH01143._CH', 'ED6_DT07/CH01143P._CP'),
        ('ED6_DT07/CH01213._CH', 'ED6_DT07/CH01213P._CP'),
        ('ED6_DT07/CH02070._CH', 'ED6_DT07/CH02070P._CP'),
        ('ED6_DT07/CH01540._CH', 'ED6_DT07/CH01540P._CP'),
        ('ED6_DT06/CH20021._CH', 'ED6_DT06/CH20021P._CP'),
    ]

# id: 0x10001 offset: 0xF2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '奈尔',
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
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            name                = '总编',
            x                   = -54100,
            z                   = 200,
            y                   = 61000,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0115,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '诺蒂亚',
            x                   = -55730,
            z                   = 250,
            y                   = 119940,
            direction           = 181,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0115,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '法尔茨',
            x                   = -59030,
            z                   = 100,
            y                   = 59540,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0115,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            name                = '朵洛希',
            x                   = -56890,
            z                   = 0,
            y                   = 63750,
            direction           = 90,
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
            name                = '莎莉亚',
            x                   = -56630,
            z                   = 0,
            y                   = 5500,
            direction           = 174,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            name                = '巴拉尔',
            x                   = 61020,
            z                   = 0,
            y                   = 2490,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '科尼嘉',
            x                   = 65800,
            z                   = 100,
            y                   = -3410,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0115,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '小说',
            x                   = 66540,
            z                   = 750,
            y                   = -4140,
            direction           = 225,
            word_0E             = 0,
            dword_10            = 1703944,
            chipIndex           = 8,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '科蕾蒂',
            x                   = 4560,
            z                   = 0,
            y                   = 2500,
            direction           = 186,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '彭萨',
            x                   = 4500,
            z                   = 100,
            y                   = -3850,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0115,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
    )

# id: 0x10002 offset: 0x252
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x252
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x252
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 60700,
            triggerZ            = 0,
            triggerY            = 550,
            triggerRange        = 400,
            actorX              = 61020,
            actorZ              = 1500,
            actorY              = 2490,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 4530,
            triggerZ            = 0,
            triggerY            = 590,
            triggerRange        = 400,
            actorX              = 4560,
            actorZ              = 1500,
            actorY              = 2500,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -56840,
            triggerZ            = 0,
            triggerY            = 3500,
            triggerRange        = 400,
            actorX              = -56630,
            actorZ              = 1500,
            actorY              = 5500,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000E,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 57530,
            triggerZ            = 0,
            triggerY            = 400,
            triggerRange        = 800,
            actorX              = 57290,
            actorZ              = 900,
            actorY              = 340,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0018,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 2480,
            triggerZ            = -250,
            triggerY            = -3810,
            triggerRange        = 800,
            actorX              = 2480,
            actorZ              = 1100,
            actorY              = -3810,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0019,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x306
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_3C2',
    )

    ChrSetChipByIndex(0x0009, 1)
    ChrClearFlags(0x0009, 0x0004)
    ChrSetPos(0x0009, -56260, 0, 60900, 270)
    CreateThread(0x0009, 0x00, 0x06, func_02_5E1)
    ChrClearFlags(0x0009, 0x0010)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, -55850, 0, 63410, 90)
    ChrSetChipByIndex(0x000A, 5)
    ChrClearFlags(0x000A, 0x0004)
    ChrClearFlags(0x000A, 0x0010)
    ChrSetPos(0x000A, -61660, 0, 59440, 72)
    CreateThread(0x000A, 0x00, 0x06, func_02_5E1)
    ChrSetChipByIndex(0x000B, 9)
    ChrClearFlags(0x000B, 0x0004)
    ChrClearFlags(0x000B, 0x0010)
    ChrSetPos(0x000B, -59900, 0, 59400, 71)
    CreateThread(0x000B, 0x00, 0x06, func_02_5E1)
    ChrSetPos(0x0008, -58470, 0, 62920, 117)
    ChrSetPos(0x000C, -59920, 0, 62910, 134)
    ChrClearFlags(0x000C, 0x0080)

    Jump('loc_4CA')

    def _loc_3C2(): pass

    label('loc_3C2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_3F3',
    )

    ChrSetChipByIndex(0x000A, 5)
    ChrClearFlags(0x000A, 0x0004)
    ChrClearFlags(0x000A, 0x0010)
    ChrSetPos(0x000A, -56250, 0, 61030, 80)
    CreateThread(0x000A, 0x00, 0x06, func_02_5E1)

    Jump('loc_4CA')

    def _loc_3F3(): pass

    label('loc_3F3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_43F',
    )

    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, -64450, 0, 60580, 1)
    ChrSetChipByIndex(0x000A, 5)
    ChrClearFlags(0x000A, 0x0004)
    ChrClearFlags(0x000A, 0x0010)
    ChrSetPos(0x000A, -57850, 0, 61830, 263)
    CreateThread(0x000A, 0x00, 0x06, func_02_5E1)

    Jump('loc_4CA')

    def _loc_43F(): pass

    label('loc_43F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_497',
    )

    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, -59010, 0, 121400, 90)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 0, 0x1628)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_46D',
    )

    ChrSetFlags(0x0008, 0x0010)

    def _loc_46D(): pass

    label('loc_46D')

    ChrSetChipByIndex(0x000A, 5)
    ChrClearFlags(0x000A, 0x0004)
    ChrClearFlags(0x000A, 0x0010)
    ChrSetPos(0x000A, -56570, 0, 64660, 1)
    CreateThread(0x000A, 0x00, 0x06, func_02_5E1)

    Jump('loc_4CA')

    def _loc_497(): pass

    label('loc_497')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_4A1',
    )

    Jump('loc_4CA')

    def _loc_4A1(): pass

    label('loc_4A1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_4CA',
    )

    ChrSetPos(0x000A, -56250, 0, 61090, 103)
    ChrSetChipByIndex(0x000A, 5)
    ChrSetFlags(0x000A, 0x0010)
    CreateThread(0x000A, 0x00, 0x06, func_02_5E1)

    def _loc_4CA(): pass

    label('loc_4CA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x041D, 7, 0x20EF)),
            Expr.Ez,
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Nez64,
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x69),
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4ED',
    )

    MapSetFlags(0x10000000)
    Event(0, func_10_3DF3)

    def _loc_4ED(): pass

    label('loc_4ED')

    Return()

# id: 0x0001 offset: 0x4EE
@scena.Code('func_01_4EE')
def func_01_4EE():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 2, 0x162A)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_50A',
    )

    OP_B1('t4130_y')

    Jump('loc_513')

    def _loc_50A(): pass

    label('loc_50A')

    OP_B1('t4130_n')

    def _loc_513(): pass

    label('loc_513')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0217, 1, 0x10B9)),
            Expr.Return,
        ),
        'loc_51F',
    )

    ChrSetFlags(0x0010, 0x0080)

    def _loc_51F(): pass

    label('loc_51F')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_55D',
    )

    OP_72(0x0000, 0x0020)
    OP_72(0x0000, 0x0008)
    OP_72(0x0001, 0x0020)
    OP_72(0x0001, 0x0008)
    OP_72(0x0002, 0x0020)
    OP_72(0x0002, 0x0008)
    OP_72(0x0003, 0x0020)
    OP_72(0x0003, 0x0008)
    OP_72(0x0004, 0x0020)
    OP_72(0x0004, 0x0008)

    def _loc_55D(): pass

    label('loc_55D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_585',
    )

    LoadChip('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP', 1)
    LoadChip('ED6_DT07/CH01210._CH', 'ED6_DT07/CH01210P._CP', 5)
    LoadChip('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP', 9)

    Jump('loc_5E0')

    def _loc_585(): pass

    label('loc_585')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_599',
    )

    LoadChip('ED6_DT07/CH01210._CH', 'ED6_DT07/CH01210P._CP', 5)

    Jump('loc_5E0')

    def _loc_599(): pass

    label('loc_599')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_5AD',
    )

    LoadChip('ED6_DT07/CH01210._CH', 'ED6_DT07/CH01210P._CP', 5)

    Jump('loc_5E0')

    def _loc_5AD(): pass

    label('loc_5AD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5C5',
    )

    LoadChip('ED6_DT07/CH01210._CH', 'ED6_DT07/CH01210P._CP', 5)

    Jump('loc_5E0')

    def _loc_5C5(): pass

    label('loc_5C5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_5CF',
    )

    Jump('loc_5E0')

    def _loc_5CF(): pass

    label('loc_5CF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_5E0',
    )

    LoadChip('ED6_DT07/CH01210._CH', 'ED6_DT07/CH01210P._CP', 5)

    def _loc_5E0(): pass

    label('loc_5E0')

    Return()

# id: 0x0002 offset: 0x5E1
@scena.Code('func_02_5E1')
def func_02_5E1():
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
        'loc_606',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_748')

    def _loc_606(): pass

    label('loc_606')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_61F',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_748')

    def _loc_61F(): pass

    label('loc_61F')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_638',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_748')

    def _loc_638(): pass

    label('loc_638')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_651',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_748')

    def _loc_651(): pass

    label('loc_651')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_66A',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_748')

    def _loc_66A(): pass

    label('loc_66A')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_683',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_748')

    def _loc_683(): pass

    label('loc_683')

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

    Jump('loc_748')

    def _loc_69C(): pass

    label('loc_69C')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6B5',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_748')

    def _loc_6B5(): pass

    label('loc_6B5')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6CE',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_748')

    def _loc_6CE(): pass

    label('loc_6CE')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6E7',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_748')

    def _loc_6E7(): pass

    label('loc_6E7')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_700',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_748')

    def _loc_700(): pass

    label('loc_700')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_719',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_748')

    def _loc_719(): pass

    label('loc_719')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_732',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_748')

    def _loc_732(): pass

    label('loc_732')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_748',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_748(): pass

    label('loc_748')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_75D',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_748')

    def _loc_75D(): pass

    label('loc_75D')

    Return()

# id: 0x0003 offset: 0x75E
@scena.Code('func_03_75E')
def func_03_75E():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_B23',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x041A, 7, 0x20D7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_AB3',
    )

    ChrTurnDirection(0x0008, 0x0101, 0)

    ChrTalk(
        0x0101,
        (
            '#0010371003V#1001F奈尔！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0270371004V#143F哟，是艾丝蒂尔啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270371005V还有约修亚……\n',
            '一起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020371006V#1040F嗯，好久不见。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020371007V奈尔先生你们\n',
            '还是看上去很忙呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0270371008V#140F嗯，总编也说过，\n',
            '就这点程度的劳累\n',
            '是不会让我们放下笔杆的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270371009V我们才不会随了结社的心愿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010371010V#1015F不过导力器都不能用了，\n',
            '你们接下来准备怎么办？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 300)

    ChrTalk(
        0x0008,
        (
            '#0270371011V#145F嗯，问题就在这儿。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270371012V现在朵洛希的\n',
            '照相机也不能用了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270371013V#141F不过我们也不是束手无策。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270371014V接下来我准备晋见艾莉茜雅\n',
            '女王，和她商量一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010371015V#1001F哟，真努力……\n',
            '感觉放心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0102, 300)

    ChrTalk(
        0x0008,
        (
            '#0270371016V#141F那么，约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270371017V我有不可斗量的\n',
            '问题要采访你，\n',
            '不过先要推迟一下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270371018V#147F你就洗干净脖子等着吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020371019V#1054F哈哈……请手下留情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x041A, 7, 0x20D7))

    Jump('loc_B20')

    def _loc_AB3(): pass

    label('loc_AB3')

    ChrTalk(
        0x0008,
        (
            '#0270371020V#140F要做的事和要解决问题有很多，\n',
            '不能呆在这里发呆了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270371021V记者就是要\n',
            '行动优先的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B20(): pass

    label('loc_B20')

    Jump('loc_1153')

    def _loc_B23(): pass

    label('loc_B23')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_E32',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02CC, 6, 0x1666)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_DCA',
    )

    ChrTalk(
        0x0008,
        (
            '#0270271532V#145F哇～真没办法……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270271533V#140F……因为军队的管制\n',
            '所以没法清清楚楚地在报上\n',
            '报导那个巨大机器人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010271534V#1015F好像是希德中校说的吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010271535V#1000F不过，如果大众知道出现了\n',
            '那种东西一定会引发骚动的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010271536V中校应该也是\n',
            '顾虑到了这一点……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0270271537V#140F大概吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270271538V#142F可利贝尔通讯不是\n',
            '政府的御用杂志。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270271539V我们的使命终究是\n',
            '中立地发布信息。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270271540V明知有又不公开的行为\n',
            '也能算是撒谎。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010271541V#1015F可、可能\n',
            '也有点道理……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0270271542V#145F算了，这次就算我输了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270271543V#140F好，朵洛希那家伙\n',
            '也该回来了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270271544V能不能赶上你们出发倒是\n',
            '有点不得而知。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x02CC, 6, 0x1666))

    Jump('loc_E2F')

    def _loc_DCA(): pass

    label('loc_DCA')

    ChrTalk(
        0x0008,
        (
            '#0270271545V#140F朵洛希那家伙\n',
            '也该回来了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270271544V能不能赶上你们出发倒是\n',
            '有点不得而知。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E2F(): pass

    label('loc_E2F')

    Jump('loc_1153')

    def _loc_E32(): pass

    label('loc_E32')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_10B5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_FF5',
    )

    ChrTalk(
        0x0008,
        (
            '#0270251349V#143F……你问我有没有看见玲？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270251350V#140F就是昨天在酒馆\n',
            '一起吃饭的女孩子？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251351V#1011F对对，你在这附近\n',
            '有没有见过她？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0270251352V#140F抱歉，不巧的是我今天\n',
            '一直没离开杂志社。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251353V#1015F哦，这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C6, 2, 0x1632)),
            Expr.Return,
        ),
        'loc_FC0',
    )

    ChrTalk(
        0x0008,
        (
            '#0270251354V#140F那你们可以去问问其他人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270251355V#141F上次我请你们去的咖啡馆\n',
            '主人也是个相当有实力的情报通。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FEF')

    def _loc_FC0(): pass

    label('loc_FC0')

    ChrTalk(
        0x0008,
        (
            '#0270251356V#140F那你们可以去问问其他人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_FEF(): pass

    label('loc_FEF')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Jump('loc_10B2')

    def _loc_FF5(): pass

    label('loc_FF5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C6, 2, 0x1632)),
            Expr.Return,
        ),
        'loc_107A',
    )

    ChrTalk(
        0x0008,
        (
            '#0270251357V#140F抱歉，找迷路的孩子\n',
            '请去问其他人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270251358V上次我请你们去的咖啡馆\n',
            '主人也是个相当有实力的情报通。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10B2')

    def _loc_107A(): pass

    label('loc_107A')

    ChrTalk(
        0x0008,
        (
            '#0270251359V#140F抱歉，找迷路的孩子\n',
            '请去问其他人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_10B2(): pass

    label('loc_10B2')

    Jump('loc_1153')

    def _loc_10B5(): pass

    label('loc_10B5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1142',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 0, 0x1628)),
            Expr.Return,
        ),
        'loc_113B',
    )

    ChrTalk(
        0x0008,
        (
            '#0270251360V#140F今天跑了一天，也没\n',
            '找到什么不错的新闻线索。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270251361V希望朵洛希那家伙\n',
            '能抓到些什么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_113F')

    def _loc_113B(): pass

    label('loc_113B')

    Call(0, 0x0011)

    def _loc_113F(): pass

    label('loc_113F')

    Jump('loc_1153')

    def _loc_1142(): pass

    label('loc_1142')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_114C',
    )

    Jump('loc_1153')

    def _loc_114C(): pass

    label('loc_114C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_1153',
    )

    def _loc_1153(): pass

    label('loc_1153')

    TalkEnd(0x0008)

    Return()

# id: 0x0004 offset: 0x1157
@scena.Code('func_04_1157')
def func_04_1157():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_11CE',
    )

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
            '我不觉得现在是\n',
            '危机时刻。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '倒不如说是利贝尔通讯社的\n',
            '真正的价值正在受到考验。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_192E')

    def _loc_11CE(): pass

    label('loc_11CE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_1258',
    )

    ChrTalk(
        0x00FE,
        (
            '哟，昨天那么晚\n',
            '你们还在配合\n',
            '奈尔的采访啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他和刚才回来的\n',
            '朵洛希一起出去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说是要去城里收集\n',
            '昨天的事件的消息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_192E')

    def _loc_1258(): pass

    label('loc_1258')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_12F9',
    )

    ChrTalk(
        0x00FE,
        (
            '让朵洛希一个人去采访\n',
            '确实令人担心……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不管怎么样，还是希望能认真顺利地\n',
            '完成工作回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然途中可能会受到耽搁，\n',
            '不过这买卖看重的是结果。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_192E')

    def _loc_12F9(): pass

    label('loc_12F9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 0, 0x1628)),
            Expr.Return,
        ),
        'loc_141E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_13D1',
    )

    ChrTalk(
        0x00FE,
        (
            '……记者如果不死缠烂打\n',
            '就无法获得好的消息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，在写报道的时候必须\n',
            '尽量远离对象。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不用说采访对方和事件了，\n',
            '有时候甚至不能从外侧\n',
            '审视自我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只有发现真实的人\n',
            '才是真正的记者。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Jump('loc_141B')

    def _loc_13D1(): pass

    label('loc_13D1')

    ChrTalk(
        0x00FE,
        (
            '记者甚至不能从外侧\n',
            '审视自我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只有发现真实的人\n',
            '才是真正的记者。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_141B(): pass

    label('loc_141B')

    Jump('loc_192E')

    def _loc_141E(): pass

    label('loc_141E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_15C7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02CC, 4, 0x1664)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_15AC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02D0, 0, 0x1680)),
            Expr.Return,
        ),
        'loc_14C3',
    )

    ChrTalk(
        0x00FE,
        (
            '哟，艾丝蒂尔，\n',
            '奈尔刚才回来了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1000F啊，真的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，他在资料室。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈哈，瞧他那张脸就知道\n',
            '他没找到什么好的材料了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15A6')

    def _loc_14C3(): pass

    label('loc_14C3')

    ChrTalk(
        0x00FE,
        (
            '哎呀，这不是艾丝蒂尔吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1001F总编先生，好久不见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天是怎么了。\n',
            '莫非是找奈尔？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1000F嗯，因为协会的工作\n',
            '有点事想问问他。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '他已经从卢安\n',
            '回来了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，他应该正好在。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '刚才我还看见\n',
            '他上了资料室。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_15A6(): pass

    label('loc_15A6')

    SetScenaFlags(ScenaFlag(0x02CC, 4, 0x1664))

    Jump('loc_15C4')

    def _loc_15AC(): pass

    label('loc_15AC')

    ChrTalk(
        0x00FE,
        (
            '奈尔应该在资料室。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_15C4(): pass

    label('loc_15C4')

    Jump('loc_192E')

    def _loc_15C7(): pass

    label('loc_15C7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_17E2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02D0, 0, 0x1680)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1798',
    )

    ChrTalk(
        0x00FE,
        (
            '哎呀，这不是艾丝蒂尔吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1001F总编先生，好久不见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天是怎么了。\n',
            '莫非是找奈尔？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1000F嗯，因为协会的工作\n',
            '有点事想问问他。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '他已经从卢安\n',
            '回来了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，回来是回来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过我记得他又去\n',
            '外面采访了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1015F是吗？可以想象\n',
            '他仍然是那么忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，也是工作原因。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然不知道他在哪里，\n',
            '不过我听说他傍晚前会回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1006F嗯，明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F看来先去其他地方\n',
            '会比较好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#070F是啊，这里就\n',
            '放放吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x02D0, 0, 0x1680))

    Jump('loc_17DF')

    def _loc_1798(): pass

    label('loc_1798')

    ChrTalk(
        0x00FE,
        (
            '奈尔出去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然不知道他在哪里，\n',
            '不过我听说他傍晚前会回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_17DF(): pass

    label('loc_17DF')

    Jump('loc_192E')

    def _loc_17E2(): pass

    label('loc_17E2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_192E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_18BE',
    )

    ChrTalk(
        0x00FE,
        (
            '『卢安市的新市长\n',
            '　终于确定！』……了啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '奈尔写这种文章可能会觉得闷，\n',
            '不过写得还不错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好，虽然有点对不起诺蒂亚，\n',
            '不过还是把这作为下一期的头条吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1000F（他们看来在讨论呢……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Jump('loc_192E')

    def _loc_18BE(): pass

    label('loc_18BE')

    ChrTalk(
        0x00FE,
        (
            '『卢安市的新市长\n',
            '　终于确定！』……了啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好，虽然有点对不起诺蒂亚，\n',
            '不过还是把这作为下一期的头条吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_192E(): pass

    label('loc_192E')

    TalkEnd(0x0009)

    Return()

# id: 0x0005 offset: 0x1932
@scena.Code('func_05_1932')
def func_05_1932():
    Call(0, 0x0006)

    Return()

# id: 0x0006 offset: 0x1937
@scena.Code('func_06_1937')
def func_06_1937():
    TalkBegin(0x000E)
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
            TXT(0x02, '招牌菜『完熟咖喱饭』　900米拉\n'),
            TXT(0x03, '离开\n'),
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
        'loc_19B3',
    )

    FadeIn(300, 0)
    OP_0D()
    OP_A9(0xCB)
    OP_56(0x00)
    TalkEnd(0x000E)

    Return()

    def _loc_19B3(): pass

    label('loc_19B3')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1ABD',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x12),
            (Expr.PushLong, 0x384),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_1A88',
    )

    RemoveMira(900)
    FadeOut(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    PlaySE(11, 0x00, 0x64)

    Talk(
        (
            TxtCtl.ShowAll,
            (TxtCtl.SetColor, 0x2),
            '完熟咖喱饭',
            (TxtCtl.SetColor, 0x0),
            '已经品尝过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetStatus(ChrTable['艾丝蒂尔'], 0xFD, 1600)
    ChrSetStatus(ChrTable['约修亚'], 0xFD, 1600)
    ChrSetStatus(ChrTable['雪拉扎德'], 0xFD, 1600)
    ChrSetStatus(ChrTable['奥利维尔'], 0xFD, 1600)
    ChrSetStatus(ChrTable['科洛丝'], 0xFD, 1600)
    ChrSetStatus(ChrTable['阿加特'], 0xFD, 1600)
    ChrSetStatus(ChrTable['提妲'], 0xFD, 1600)
    ChrSetStatus(ChrTable['金'], 0xFD, 1600)
    ChrSetStatus(ChrTable['凯文神父'], 0xFD, 1600)

    If(
        (
            (Expr.Eval, "OP_40(0x020D, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1A7A',
    )

    If(
        (
            (Expr.Eval, "OP_AC(0x000B)"),
            Expr.Return,
        ),
        'loc_1A50',
    )

    Jump('loc_1A7A')

    def _loc_1A50(): pass

    label('loc_1A50')

    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            TxtCtl.ShowAll,
            (TxtCtl.SetColor, 0x2),
            '完熟咖喱饭',
            (TxtCtl.SetColor, 0x0),
            '的做法已经学会了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A7A(): pass

    label('loc_1A7A')

    OP_56(0x00)
    FadeIn(1000, 0)

    Jump('loc_1AAE')

    def _loc_1A88(): pass

    label('loc_1A88')

    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            '没有足够的米拉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeIn(300, 0)
    def _loc_1AAE(): pass

    label('loc_1AAE')

    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x000E)

    Return()

    def _loc_1ABD(): pass

    label('loc_1ABD')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1AD7',
    )

    FadeIn(300, 0)
    TalkEnd(0x000E)

    Return()

    def _loc_1AD7(): pass

    label('loc_1AD7')

    FadeIn(300, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1CF7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1BF3',
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
            TXT(0x00, '【◇集齐了全部『牌技师杰克』】\n'),
            TXT(0x01, '【◇没集齐全部『牌技师杰克』】\n'),
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
        (0x00000000, 'loc_1B61'),
        (0x00000001, 'loc_1BAA'),
        (-1, 'loc_1BF3'),
    )

    def _loc_1B61(): pass

    label('loc_1B61')

    AddItem(ItemTable['牌技师杰克 １卷'], 1)
    AddItem(ItemTable['牌技师杰克 ２卷'], 1)
    AddItem(ItemTable['牌技师杰克 ３卷'], 1)
    AddItem(ItemTable['牌技师杰克 ４卷'], 1)
    AddItem(ItemTable['牌技师杰克 ５卷'], 1)
    AddItem(ItemTable['牌技师杰克 ６卷'], 1)
    AddItem(ItemTable['牌技师杰克 ７卷'], 1)
    AddItem(ItemTable['牌技师杰克 ８卷'], 1)
    AddItem(ItemTable['牌技师杰克 ９卷'], 1)
    AddItem(ItemTable['牌技师杰克 10卷'], 1)
    AddItem(ItemTable['牌技师杰克 11卷'], 1)
    AddItem(ItemTable['牌技师杰克 12卷'], 1)
    AddItem(ItemTable['牌技师杰克 13卷'], 1)
    AddItem(ItemTable['牌技师杰克 14卷'], 1)

    Jump('loc_1BF3')

    def _loc_1BAA(): pass

    label('loc_1BAA')

    RemoveItem(ItemTable['牌技师杰克 １卷'], 1)
    RemoveItem(ItemTable['牌技师杰克 ２卷'], 1)
    RemoveItem(ItemTable['牌技师杰克 ３卷'], 1)
    RemoveItem(ItemTable['牌技师杰克 ４卷'], 1)
    RemoveItem(ItemTable['牌技师杰克 ５卷'], 1)
    RemoveItem(ItemTable['牌技师杰克 ６卷'], 1)
    RemoveItem(ItemTable['牌技师杰克 ７卷'], 1)
    RemoveItem(ItemTable['牌技师杰克 ８卷'], 1)
    RemoveItem(ItemTable['牌技师杰克 ９卷'], 1)
    RemoveItem(ItemTable['牌技师杰克 10卷'], 1)
    RemoveItem(ItemTable['牌技师杰克 11卷'], 1)
    RemoveItem(ItemTable['牌技师杰克 12卷'], 1)
    RemoveItem(ItemTable['牌技师杰克 13卷'], 1)
    RemoveItem(ItemTable['牌技师杰克 14卷'], 1)

    Jump('loc_1BF3')

    def _loc_1BF3(): pass

    label('loc_1BF3')

    If(
        (
            (Expr.Eval, "OP_40(0x023A, 0x00)"),
            (Expr.Eval, "OP_40(0x023B, 0x00)"),
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x023C, 0x00)"),
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x023D, 0x00)"),
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x023E, 0x00)"),
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x023F, 0x00)"),
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x0240, 0x00)"),
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x0241, 0x00)"),
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x0242, 0x00)"),
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x0243, 0x00)"),
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x0244, 0x00)"),
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x0245, 0x00)"),
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x0246, 0x00)"),
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x0247, 0x00)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1C6D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0218, 4, 0x10C4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1C6D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0218, 3, 0x10C3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1C65',
    )

    SetScenaFlags(ScenaFlag(0x0218, 3, 0x10C3))
    Call(0, 0x0015)
    TalkEnd(0x000E)

    Return()

    def _loc_1C65(): pass

    label('loc_1C65')

    Call(0, 0x0016)
    TalkEnd(0x000E)

    Return()

    def _loc_1C6D(): pass

    label('loc_1C6D')

    ChrTalk(
        0x000E,
        (
            '不用导力器做饭虽然麻烦，\n',
            '不过别有一番风味。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '同样是煮出来的咖啡，\n',
            '却感觉这样更加好喝。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '以后也可以考虑用\n',
            '炭火或者柴来煮。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_21C8')

    def _loc_1CF7(): pass

    label('loc_1CF7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_1D5D',
    )

    ChrTalk(
        0x000E,
        (
            '我想港口怎么这么吵，\n',
            '原来是发生了大事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '不过今后的夜晚会变得安静，\n',
            '不是也挺好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_21C8')

    def _loc_1D5D(): pass

    label('loc_1D5D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_1F0B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C6, 3, 0x1633)),
            Expr.Return,
        ),
        'loc_1DCC',
    )

    ChrTalk(
        0x000E,
        (
            '女孩子喝着奶咖，\n',
            '问了我一个奇怪的问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '她问『没人管就会消失的点心\n',
            '在哪儿有卖？』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F08')

    def _loc_1DCC(): pass

    label('loc_1DCC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C6, 2, 0x1632)),
            Expr.Return,
        ),
        'loc_1DDA',
    )

    Call(0, 0x0012)

    Jump('loc_1F08')

    def _loc_1DDA(): pass

    label('loc_1DDA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1EC7',
    )

    ChrTalk(
        0x000E,
        (
            '在城里工作的时候，\n',
            '每次去外国出差\n',
            '都是在卢安坐的船。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '那时候还没有\n',
            '定期船呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '船自然没飞船\n',
            '移动得快，\n',
            '不过也有它的长处。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '慢慢地花时间前进……\n',
            '人类本就是这样的生物。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '飞船出现之后人变得\n',
            '越来越忙碌了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_1F08')

    def _loc_1EC7(): pass

    label('loc_1EC7')

    ChrTalk(
        0x000E,
        (
            '哈哈，我会这么想\n',
            '说明我是老了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '算了，当我自言自语吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1F08(): pass

    label('loc_1F08')

    Jump('loc_21C8')

    def _loc_1F0B(): pass

    label('loc_1F0B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1F9E',
    )

    ChrTalk(
        0x000E,
        (
            '最近，利贝尔通讯的那帮人\n',
            '好像在利贝尔中上窜下跳的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '现在这当口，话题\n',
            '应该是很多吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '希望他们能尽量\n',
            '带来一些好消息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_21C8')

    def _loc_1F9E(): pass

    label('loc_1F9E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_210A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2073',
    )

    ChrTalk(
        0x000E,
        (
            '王国军的重建和签字仪\n',
            '式的准备使军人和官员们\n',
            '都看上去很忙呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '对市民来说平静的\n',
            '生活反而回来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '我渐渐感觉到自己\n',
            '是从仕官生活中解放出来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '虽然对以前的同事有点不好意思。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_2107')

    def _loc_2073(): pass

    label('loc_2073')

    ChrTalk(
        0x000E,
        (
            '王国军的重建和签字仪\n',
            '式的准备使军人和官员们\n',
            '都看上去很忙呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '虽然对以前的同事有点不好意思，\n',
            '但我渐渐感觉到自己\n',
            '是从仕官生活中解放出来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2107(): pass

    label('loc_2107')

    Jump('loc_21C8')

    def _loc_210A(): pass

    label('loc_210A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_21C8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2191',
    )

    ChrTalk(
        0x000E,
        (
            '哟，我好像见过你。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '你是奈尔认识的\n',
            '游击士小姐吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '咖啡和咖喱饭\n',
            '欢迎来到王都的特色咖啡厅『巴拉尔』！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_21C8')

    def _loc_2191(): pass

    label('loc_2191')

    ChrTalk(
        0x000E,
        (
            '咖啡和咖喱饭\n',
            '欢迎来到王都的特色咖啡厅『巴拉尔』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_21C8(): pass

    label('loc_21C8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_21D6',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_21D6')

    def _loc_21D6(): pass

    label('loc_21D6')

    TalkEnd(0x000E)

    Return()

# id: 0x0007 offset: 0x21DA
@scena.Code('func_07_21DA')
def func_07_21DA():
    Call(0, 0x0008)

    Return()

# id: 0x0008 offset: 0x21DF
@scena.Code('func_08_21DF')
def func_08_21DF():
    TalkBegin(0x0011)
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
            TXT(0x02, '招牌菜『热海汁』　1200米拉\n'),
            TXT(0x03, '离开\n'),
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
        'loc_2258',
    )

    FadeIn(300, 0)
    OP_0D()
    OP_A9(0xCA)
    OP_56(0x00)
    TalkEnd(0x0011)

    Return()

    def _loc_2258(): pass

    label('loc_2258')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_235A',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x12),
            (Expr.PushLong, 0x4B0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_2325',
    )

    RemoveMira(1200)
    FadeOut(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    PlaySE(11, 0x00, 0x64)

    Talk(
        (
            TxtCtl.ShowAll,
            (TxtCtl.SetColor, 0x2),
            '热海汁',
            (TxtCtl.SetColor, 0x0),
            '已经品尝过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetStatus(ChrTable['艾丝蒂尔'], 0xFD, 2500)
    ChrSetStatus(ChrTable['约修亚'], 0xFD, 2500)
    ChrSetStatus(ChrTable['雪拉扎德'], 0xFD, 2500)
    ChrSetStatus(ChrTable['奥利维尔'], 0xFD, 2500)
    ChrSetStatus(ChrTable['科洛丝'], 0xFD, 2500)
    ChrSetStatus(ChrTable['阿加特'], 0xFD, 2500)
    ChrSetStatus(ChrTable['提妲'], 0xFD, 2500)
    ChrSetStatus(ChrTable['金'], 0xFD, 2500)
    ChrSetStatus(ChrTable['凯文神父'], 0xFD, 2500)

    If(
        (
            (Expr.Eval, "OP_40(0x020D, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2317',
    )

    If(
        (
            (Expr.Eval, "OP_AC(0x0002)"),
            Expr.Return,
        ),
        'loc_22F1',
    )

    Jump('loc_2317')

    def _loc_22F1(): pass

    label('loc_22F1')

    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            TxtCtl.ShowAll,
            (TxtCtl.SetColor, 0x2),
            '热海汁',
            (TxtCtl.SetColor, 0x0),
            '的做法已经学会了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2317(): pass

    label('loc_2317')

    OP_56(0x00)
    FadeIn(1000, 0)

    Jump('loc_234B')

    def _loc_2325(): pass

    label('loc_2325')

    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            '没有足够的米拉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeIn(300, 0)
    def _loc_234B(): pass

    label('loc_234B')

    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x0011)

    Return()

    def _loc_235A(): pass

    label('loc_235A')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2374',
    )

    FadeIn(300, 0)
    TalkEnd(0x0011)

    Return()

    def _loc_2374(): pass

    label('loc_2374')

    FadeIn(300, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_23E0',
    )

    ChrTalk(
        0x0011,
        (
            '呼，总算习惯了\n',
            '用火来做饭……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '是钓公师团的人们\n',
            '告诉我的，\n',
            '大概是暂停营业了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_29B2')

    def _loc_23E0(): pass

    label('loc_23E0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_246D',
    )

    ChrTalk(
        0x0011,
        (
            '昨天在西街区情报部好像\n',
            '和王国军发生了战斗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '情报部的人好象\n',
            '尽数被亲卫队逮捕了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '能够恰好赶到，\n',
            '真不愧是尤莉亚上尉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_29B2')

    def _loc_246D(): pass

    label('loc_246D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_258F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2546',
    )

    ChrTalk(
        0x0011,
        (
            '我昨天去西街区的\n',
            '咖啡馆吃了\n',
            '咖喱饭。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '那种绝妙的调味掌控\n',
            '真如传说中那般会让人上瘾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '咖啡也很好喝，\n',
            '真令人满意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '特色是又苦又辣的店……\n',
            '构思也挺新颖的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '主人不愧是\n',
            '海归派。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Jump('loc_258C')

    def _loc_2546(): pass

    label('loc_2546')

    ChrTalk(
        0x0011,
        (
            '特色是又苦又辣的店……\n',
            '构思也挺新颖的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '主人不愧是\n',
            '海归派。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_258C(): pass

    label('loc_258C')

    Jump('loc_29B2')

    def _loc_258F(): pass

    label('loc_258F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 3, 0x162B)),
            Expr.Return,
        ),
        'loc_266F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2620',
    )

    ChrTalk(
        0x0011,
        (
            '欢迎！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '各位，昨晚都\n',
            '尽兴了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '你们能那么开心，\n',
            '作为店方的我们也很荣幸。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0011, 0x012F, 400)

    ChrTalk(
        0x0011,
        (
            '姐姐你们也请\n',
            '再来吃饭。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Jump('loc_266C')

    def _loc_2620(): pass

    label('loc_2620')

    ChrTalk(
        0x0011,
        (
            '各位，昨晚都\n',
            '尽兴了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '你们能那么开心，\n',
            '作为店方的我们也很荣幸。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_266C(): pass

    label('loc_266C')

    Jump('loc_29B2')

    def _loc_266F(): pass

    label('loc_266F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_26BC',
    )

    ChrTalk(
        0x0011,
        (
            '那么，接下来就是晚饭时间了，\n',
            '要忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '今天也要努力！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_29B2')

    def _loc_26BC(): pass

    label('loc_26BC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_28CF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2898',
    )

    ChrTalk(
        0x0011,
        (
            '欢迎！\n',
            '欢迎来到『阳光铃铛』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0011, 0x0104, 400)

    ChrTalk(
        0x0011,
        (
            '咦……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '难道你就是我以前点播\n',
            '钢琴演奏的奥利维尔先生？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#031F哈哈，正是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '好久没见了啊！\n',
            '今天到底是怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#034F啊，请不要说\n',
            '庸俗的话。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#035F在这家店里和你共同度过的\n',
            '模糊、甜蜜又痛苦的每一天……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '对孤独旅行的演奏家来说，\n',
            '你简直是暗夜里的明灯。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#030F我就是那无法忘记你，\n',
            '追寻着阳光\n',
            '返回的小鸟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '呵呵，你还是老样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '你看来很闲，能不能请你\n',
            '再演奏一曲呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#031F哈哈，当然！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Jump('loc_28CC')

    def _loc_2898(): pass

    label('loc_2898')

    ChrTurnDirection(0x0011, 0x0104, 400)

    ChrTalk(
        0x0011,
        (
            '奥利维尔先生，你有空\n',
            '我就再请你弹钢琴。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_28CC(): pass

    label('loc_28CC')

    Jump('loc_29B2')

    def _loc_28CF(): pass

    label('loc_28CF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            Expr.Return,
        ),
        'loc_295A',
    )

    ChrTalk(
        0x0011,
        (
            '现在还有很多人\n',
            '喜欢理查德上校。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '在客人的会话中\n',
            '也经常冒出上校的话题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '说明他虽然做了错事，\n',
            '不过还是个有魅力的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_29B2')

    def _loc_295A(): pass

    label('loc_295A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_29B2',
    )

    ChrTalk(
        0x0011,
        (
            '可能是快到签字仪式了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '最近，在这家店里也能\n',
            '看见星星点点的外国人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_29B2(): pass

    label('loc_29B2')

    TalkEnd(0x0011)

    Return()

# id: 0x0009 offset: 0x29B6
@scena.Code('func_09_29B6')
def func_09_29B6():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_2A3C',
    )

    ChrTalk(
        0x00FE,
        (
            '肉的表面烤得松脆，\n',
            '非常香。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '生烤菜挺有特色的，\n',
            '也不错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好象火候挺难把握的，\n',
            '科蕾蒂小姐看来也挺不容易的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F77')

    def _loc_2A3C(): pass

    label('loc_2A3C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_2B4A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2AF5',
    )

    ChrTalk(
        0x00FE,
        (
            '情报部的余党之前\n',
            '似乎潜伏在港口？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '逃亡的凯诺娜上尉\n',
            '据说也被亲卫队逮捕了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '情报部的所有人\n',
            '都被逮捕了吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样的话理查德上校的罪\n',
            '不会再加重吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    Jump('loc_2B47')

    def _loc_2AF5(): pass

    label('loc_2AF5')

    ChrTalk(
        0x00FE,
        (
            '情报部的余党之前\n',
            '似乎潜伏在港口？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样的话理查德上校的罪\n',
            '不会再加重吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2B47(): pass

    label('loc_2B47')

    Jump('loc_2F77')

    def _loc_2B4A(): pass

    label('loc_2B4A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_2C8B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2C2E',
    )

    ChrTalk(
        0x00FE,
        (
            '昨天我第一次吃了\n',
            '东街区卖的冰淇淋。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不愧是科洛蒂娅公主，居然\n',
            '会出城来买冰淇淋吃啊，\n',
            '确实很美味。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只不过我这个人本就\n',
            '不适应吃冰的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '吃的节奏一慢\n',
            '冰就不断地化掉了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有点郁闷啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    Jump('loc_2C88')

    def _loc_2C2E(): pass

    label('loc_2C2E')

    ChrTalk(
        0x00FE,
        (
            '我本来就不适应\n',
            '吃冰的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '吃的节奏一慢\n',
            '冰就不断地化掉了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有点郁闷啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2C88(): pass

    label('loc_2C88')

    Jump('loc_2F77')

    def _loc_2C8B(): pass

    label('loc_2C8B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 3, 0x162B)),
            Expr.Return,
        ),
        'loc_2CAF',
    )

    ChrTalk(
        0x00FE,
        (
            '唔～今天吃什么呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F77')

    def _loc_2CAF(): pass

    label('loc_2CAF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2D60',
    )

    ChrTalk(
        0x00FE,
        (
            '曾是理查德上校的女部下的\n',
            '一名上尉似乎钻了个空子，\n',
            '现在都还在逃亡。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我记得她叫……凯、凯、凯诺娜上尉？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好像在士官学校时\n',
            '和尤莉亚小姐就是竞争对手哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F77')

    def _loc_2D60(): pass

    label('loc_2D60')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_2E53',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2DFE',
    )

    ChrTalk(
        0x00FE,
        (
            '请不要外传……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '其实我写了信请求宽大\n',
            '处理理查德上校。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '过了那么久，\n',
            '我也想了很多……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我实在不认为那位上校\n',
            '只是个坏蛋。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    Jump('loc_2E50')

    def _loc_2DFE(): pass

    label('loc_2DFE')

    ChrTalk(
        0x00FE,
        (
            '其实我写了信请求宽大\n',
            '处理理查德上校。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我实在不认为那位上校\n',
            '只是个坏蛋。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2E50(): pass

    label('loc_2E50')

    Jump('loc_2F77')

    def _loc_2E53(): pass

    label('loc_2E53')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            Expr.Return,
        ),
        'loc_2EE1',
    )

    ChrTalk(
        0x00FE,
        (
            '政变的幕后黑手\n',
            '理查德上校\n',
            '好象被关在雷斯顿要塞。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……上校接下来会\n',
            '怎么样呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '作为政变的罪犯，\n',
            '是不可能简单脱罪的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F77')

    def _loc_2EE1(): pass

    label('loc_2EE1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_2F77',
    )

    ChrTalk(
        0x00FE,
        (
            '政变的时候\n',
            '很多的城里官员和佣人\n',
            '都被公爵放了假。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在那些人好像\n',
            '也在忙碌地工作哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '事件的善后很麻烦，\n',
            '应该是没法很快\n',
            '复原的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2F77(): pass

    label('loc_2F77')

    TalkEnd(0x00FE)

    Return()

# id: 0x000A offset: 0x2F7B
@scena.Code('func_0A_2F7B')
def func_0A_2F7B():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_2FF7',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然主人说得悠闲，\n',
            '不过我很着急！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为没了导力器\n',
            '晚上都不能读书啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '靠蜡烛的话\n',
            '眼睛会坏掉的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_332A')

    def _loc_2FF7(): pass

    label('loc_2FF7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_3095',
    )

    ChrTalk(
        0x00FE,
        (
            '那、那究竟是什么东西啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在昨天的骚动中我看见有台\n',
            '巨大的机器人飞走了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '利贝尔通讯有可能会\n',
            '登载详细情况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '下一期我一定要买！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_332A')

    def _loc_3095(): pass

    label('loc_3095')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_31C4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0217, 1, 0x10B9)),
            Expr.Return,
        ),
        'loc_30E3',
    )

    ChrTalk(
        0x00FE,
        (
            '今天利贝尔通讯的最新一期出了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '赶紧去买来\n',
            '看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_31C1')

    def _loc_30E3(): pass

    label('loc_30E3')

    ChrTalk(
        0x00FE,
        (
            '咦……今天是\n',
            '利贝尔通讯的发售日？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '利贝尔通讯当然是\n',
            '指利贝尔通讯啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这本书也读完了，\n',
            '我赶紧去买吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对了，这本书送给你吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x0010, 0x0080)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['牌技师杰克 ５卷']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_59()
    AddItem(ItemTable['牌技师杰克 ５卷'], 1)
    SetScenaFlags(ScenaFlag(0x0217, 1, 0x10B9))

    def _loc_31C1(): pass

    label('loc_31C1')

    Jump('loc_332A')

    def _loc_31C4(): pass

    label('loc_31C4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3228',
    )

    ChrTalk(
        0x00FE,
        (
            '哟，不知不觉已经\n',
            '到了傍晚了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '沉浸于书中的世界里的话\n',
            '一转眼时间就过去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_332A')

    def _loc_3228(): pass

    label('loc_3228')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_32A8',
    )

    ChrTalk(
        0x00FE,
        (
            '由艾莉茜雅女王倡导的互不侵犯\n',
            '条约的签署也马上就要进行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '作为利贝尔国民的一员,\n',
            '我也想了解一下\n',
            '条约的概要。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_332A')

    def _loc_32A8(): pass

    label('loc_32A8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_332A',
    )

    ChrTalk(
        0x00FE,
        (
            '艾尔·雷登那家店\n',
            '虽然也不错……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过还是这家店\n',
            '最能让我放松下来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '困了还能喝咖啡，\n',
            '是个正合适读书的地方哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_332A(): pass

    label('loc_332A')

    TalkEnd(0x00FE)

    Return()

# id: 0x000B offset: 0x332E
@scena.Code('func_0B_332E')
def func_0B_332E():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_3384',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯嗯，总编说得没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好～就算是手写也要\n',
            '把利贝尔通讯给弄出来！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_35EB')

    def _loc_3384(): pass

    label('loc_3384')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_33DA',
    )

    ChrTalk(
        0x00FE,
        (
            '你们就是奈尔\n',
            '认识的游击士吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '下次有什么新闻线索\n',
            '也要留点给我哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_35EB')

    def _loc_33DA(): pass

    label('loc_33DA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_343A',
    )

    ChrTalk(
        0x00FE,
        (
            '下一期没什么好的素材',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '恐吓信那边也有\n',
            '奈尔在追查……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '怎么就不\n',
            '出点事呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_35EB')

    def _loc_343A(): pass

    label('loc_343A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 0, 0x1628)),
            Expr.Return,
        ),
        'loc_34B6',
    )

    ChrTalk(
        0x00FE,
        (
            '下一期我一定要写出\n',
            '胜过奈尔的报道来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可是，到底是哪儿不对呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我是以地震受害者的\n',
            '心情来写完的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_35EB')

    def _loc_34B6(): pass

    label('loc_34B6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3551',
    )

    ChrTalk(
        0x00FE,
        (
            '帝国大使和共和国大使……\n',
            '两边我都采访了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '两个人都是老奸巨猾的，\n',
            '重要的事都没说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '尤其是帝国的达维尔大使的\n',
            '回答根本就没法登。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_35EB')

    def _loc_3551(): pass

    label('loc_3551')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_35BF',
    )

    ChrTalk(
        0x00FE,
        (
            '要写签字仪式的报道\n',
            '看来还是得去离宫……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '天气也不错，要是去艾尔贝\n',
            '周游道散步心情一定不错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_35EB')

    def _loc_35BF(): pass

    label('loc_35BF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_35EB',
    )

    ChrTalk(
        0x00FE,
        (
            '啊～这次的头条\n',
            '被奈尔给抢了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_35EB(): pass

    label('loc_35EB')

    TalkEnd(0x00FE)

    Return()

# id: 0x000C offset: 0x35EF
@scena.Code('func_0C_35EF')
def func_0C_35EF():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_367D',
    )

    ChrTalk(
        0x00FE,
        (
            '政变的时候也是的，\n',
            '越是受压迫，\n',
            '大家就反而更有热情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我来写点就算没有导力器\n',
            '也能轻松烹调的菜吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好～就这么办～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_38AF')

    def _loc_367D(): pass

    label('loc_367D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_36E5',
    )

    ChrTalk(
        0x00FE,
        (
            '在即将截稿之前\n',
            '新闻被换了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔～我也被拉来\n',
            '帮忙校对……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过我也习以为常了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_38AF')

    def _loc_36E5(): pass

    label('loc_36E5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_373E',
    )

    ChrTalk(
        0x00FE,
        (
            '唔～下一期的特辑做什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对了，卢安的游戏吧\n',
            '还没被拿来做过特辑呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_38AF')

    def _loc_373E(): pass

    label('loc_373E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 0, 0x1628)),
            Expr.Return,
        ),
        'loc_3766',
    )

    ChrTalk(
        0x00FE,
        (
            '今天要吃饱喝足睡大觉～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_38AF')

    def _loc_3766(): pass

    label('loc_3766')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_37BB',
    )

    ChrTalk(
        0x00FE,
        (
            '截稿终于结束了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在咖啡馆或者酒馆打个牙祭\n',
            '好好养精蓄锐一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_38AF')

    def _loc_37BB(): pass

    label('loc_37BB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_3856',
    )

    ChrTalk(
        0x00FE,
        (
            '因为我负责文化栏，\n',
            '所以不用像前辈们那样\n',
            '日程排得满满的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是也因为这点常被各处叫去\n',
            '帮忙，我也不轻松啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '或者说我反而比他们更忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_38AF')

    def _loc_3856(): pass

    label('loc_3856')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_38AF',
    )

    ChrTalk(
        0x00FE,
        (
            '结果还是不清楚亚尔摩\n',
            '温泉沸腾的理由。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '被总编批评成半吊子\n',
            '新闻了，唔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_38AF(): pass

    label('loc_38AF')

    TalkEnd(0x00FE)

    Return()

# id: 0x000D offset: 0x38B3
@scena.Code('func_0D_38B3')
def func_0D_38B3():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x041E, 2, 0x20F2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3AFE',
    )

    ChrTurnDirection(0x000C, 0x0102, 400)

    ChrTalk(
        0x000C,
        (
            '#0280371022V#153F啊～是约修亚～！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020371023V#1040F朵洛希小姐，好久不见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000C, 0x0101, 400)

    ChrTalk(
        0x000C,
        (
            '#0280371024V#151F你真的回来了。\n',
            '小艾，太好了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010371025V#1008F是、是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0280371026V#151F来张纪念照……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280371027V虽然心里这么想，\n',
            '#156F不过照相机没法用啊～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280371028V唉～\n',
            '总觉得现在很不正常～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010371029V#1001F哈哈，对朵洛希来说\n',
            '照相机果然是很重要的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0280371030V#150F那是自然！\n',
            '我就这点特长呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280371031V#151F真想马上去\n',
            '给湖里冒出来的可爱贝壳\n',
            '拍几张照片啊～㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020371032V#1054F哈哈，怎么说才好……\n',
            '你真是一点都没变啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x041E, 2, 0x20F2))

    Jump('loc_3B75')

    def _loc_3AFE(): pass

    label('loc_3AFE')

    ChrTalk(
        0x000C,
        (
            '#0280371033V#150F今天的总编先生不知\n',
            '为什么，看上去很帅～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280371034V实在想象不出他平时\n',
            '为什么会被大家叫作狸猫～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3B75(): pass

    label('loc_3B75')

    TalkEnd(0x00FE)

    Return()

# id: 0x000E offset: 0x3B79
@scena.Code('func_0E_3B79')
def func_0E_3B79():
    Call(0, 0x000F)

    Return()

# id: 0x000F offset: 0x3B7E
@scena.Code('func_0F_3B7E')
def func_0F_3B7E():
    TalkBegin(0x000D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_3BDD',
    )

    ChrTalk(
        0x000D,
        (
            '今天总编好像有话\n',
            '和记者们说哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '现在正好在编辑部\n',
            '开着少见的全体会议呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3DEF')

    def _loc_3BDD(): pass

    label('loc_3BDD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_3C2E',
    )

    ChrTalk(
        0x000D,
        (
            '据说港口发生了大事件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '记者们从昨晚开始\n',
            '好像就在通宵奔波哦，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3DEF')

    def _loc_3C2E(): pass

    label('loc_3C2E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_3C9E',
    )

    ChrTalk(
        0x000D,
        (
            '朵洛希不知道有没有\n',
            '在出差地好好工作呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '她虽然不是奈尔先生，\n',
            '不过我总会不知不觉担心起来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3DEF')

    def _loc_3C9E(): pass

    label('loc_3C9E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 0, 0x1628)),
            Expr.Return,
        ),
        'loc_3CC3',
    )

    ChrTalk(
        0x000D,
        (
            '要回去了吗？\n',
            '辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3DEF')

    def _loc_3CC3(): pass

    label('loc_3CC3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3D50',
    )

    ChrTalk(
        0x000D,
        (
            '那么，时间也到了，\n',
            '我也要下班了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '记者们平时都要工作到\n',
            '很晚，真不容易……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '每天我都会早下班，\n',
            '感觉有点不好意思。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3DEF')

    def _loc_3D50(): pass

    label('loc_3D50')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_3DA3',
    )

    ChrTalk(
        0x000D,
        (
            '欢迎来到利贝尔通讯社。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '如果找记者们有事的话\n',
            '请上二楼的编辑部。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3DEF')

    def _loc_3DA3(): pass

    label('loc_3DA3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_3DEF',
    )

    ChrTalk(
        0x000D,
        (
            '欢迎来到利贝尔通讯社。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '这里的一楼是接待处，\n',
            '二楼是编辑部。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3DEF(): pass

    label('loc_3DEF')

    TalkEnd(0x000D)

    Return()

# id: 0x0010 offset: 0x3DF3
@scena.Code('func_10_3DF3')
def func_10_3DF3():
    EventBegin(0x00)
    CameraMove(-59650, 0, 61820, 0)
    OP_67(0, 6150, -10000, 0)
    CameraSetDistance(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    ChrSetPos(0x0101, -63630, 0, 66440, 90)
    ChrSetPos(0x0102, -63630, 0, 66440, 90)
    ChrSetPos(0x00F8, -63630, 0, 66440, 90)
    ChrSetPos(0x00F9, -63630, 0, 66440, 90)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0102, 0x0080)
    ChrSetFlags(0x00F8, 0x0080)
    ChrSetFlags(0x00F9, 0x0080)
    OP_4A(0x0008, 255)
    OP_4A(0x0009, 255)
    OP_4A(0x000A, 255)
    OP_4A(0x000B, 255)
    OP_4A(0x000C, 255)
    OP_4A(0x000D, 255)

    @scena.Lambda('lambda_3EA8')
    def lambda_3EA8():
        CameraMove(-57880, 0, 61180, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3EA8)

    FadeIn(2000, 0)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(300)

    ChrClearFlags(0x0101, 0x0080)
    ChrClearFlags(0x0102, 0x0080)
    ChrClearFlags(0x00F8, 0x0080)
    ChrClearFlags(0x00F9, 0x0080)

    ChrTalk(
        0x0009,
        (
            '#2310370991V#2P……导力停止以后，照明和暖气\n',
            '自不必说，通讯也完全无法使用。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#2310370992V可是，我不认为像你们\n',
            '这样的记者会\n',
            '被打垮。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#4060370993V#6P当然了，我们有\n',
            '我们的任务！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2310370994V#2P对，市民们中有很多得\n',
            '不到信息而在不安中\n',
            '度日的人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#2310370995V正因为现状如此，\n',
            '我们更应该传递正确的信息，\n',
            '为社会做贡献。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0270370996V#140F#5P这还用说……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270370997V这本就是我们记者的\n',
            '存在意义。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0280370998V#156F#6P不过，奈尔前辈～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280370999V导力照相机不能用的话\n',
            '采访可不会顺利哦～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2310371000V#2P如朵洛希所述，\n',
            '大半的器材都不能用。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#2310371001V可是如果别人说我们以\n',
            '此为理由而放弃媒体的使命\n',
            '我可不甘心。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#2310371002V各自发挥创意，\n',
            '一定要想办法保持发行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(300)

    OP_69(0x0000, 2000)
    SetScenaFlags(ScenaFlag(0x041D, 7, 0x20EF))
    OP_4B(0x0008, 255)
    OP_4B(0x0009, 255)
    OP_4B(0x000A, 255)
    OP_4B(0x000B, 255)
    OP_4B(0x000C, 255)
    OP_4B(0x000D, 255)
    EventEnd(0x00)

    Return()

# id: 0x0011 offset: 0x41B8
@scena.Code('func_11_41B8')
def func_11_41B8():
    EventBegin(0x00)
    Fade(1000)
    ChrSetSubChip(0x0008, 0)
    ChrSetPos(0x0101, -59120, 0, 122980, 180)
    ChrSetPos(0x0105, -60010, 0, 123340, 180)
    ChrSetPos(0x0104, -58800, 0, 124220, 180)
    ChrSetPos(0x0108, -60490, 0, 124220, 180)
    CameraMove(-58080, 0, 123630, 0)
    OP_67(0, 4600, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(45000, 0)
    OP_6E(270, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010251241V#1011F#5P啊，找到了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010251242V#1001F喂～奈尔。\n',
            '你好～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0270251243V#142F#5P嗯……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0270251244V#141F怎么了怎么了！\n',
            '是你们啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060251245V#048F#5P你好，奈尔先生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040251246V#031F#5P呵呵，我们要打扰你们一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0270251247V#143F啊～连公主殿下、演奏家\n',
            '和『不动金』也在啊？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270251248V相当热闹啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251249V#1016F#5P嘿嘿……\n',
            '后来又发生了不少事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010251250V#1006F奈尔，你采访市长的事\n',
            '还顺利吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0270251251V#141F呵呵，那还用问？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270251252V那么你们今天有什么事？\n',
            '有什么好的新闻线索？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251253V#1025F#5P不，确切地说是\n',
            '我们要来问你。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010251254V关于寄到这里的恐吓信\n',
            '想要打听一下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0270251255V#143F怎么？你们也在\n',
            '调查这事儿？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270251256V我还以为王国军\n',
            '在调查呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251257V#1006F#5P嗯，我们是接受军方的\n',
            '委托在帮忙调查的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010251258V你有什么消息吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0270251259V#145F唔～我也是\n',
            '刚回王都，\n',
            '没得到什么重要消息。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270251260V倒是还要问问\n',
            '你们呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251261V#1019F#5P你真是靠不住啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040251262V#030F#5P你也算是媒体的人吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040251263V对罪犯的身份\n',
            '就没一点头绪？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0270251264V#142F唔……你们真没礼貌。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060251265V#045F#5P你们两个太没礼貌了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060251266V#043F那个，奈尔先生，\n',
            '我知道这有点强人所难。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060251267V你能不能告诉我们一点\n',
            '哪怕是细小的线索？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0270251268V#143F等、等等，公主殿下！\n',
            '请别对我这么客气！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270251269V#145F真是的……拿你们没办法。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270251270V#140F内部消息……\n',
            '恐吓信好像不只是\n',
            '寄到了这里。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270251271V先是雷斯顿要塞……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270251272V然后是大圣堂、飞船公社\n',
            '和罗恩鲍姆酒店……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270251273V接着是帝国和共和国的大使馆\n',
            '以及格兰赛尔城堡、艾尔贝离宫……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270251274V好像一共寄了９个地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x0108, 0x00000000, 2300, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x0105, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x0104, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0270251275V#143F嗯，怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_63(0x0101)
    OP_63(0x0105)
    OP_63(0x0104)
    OP_63(0x0108)

    ChrTalk(
        0x0101,
        (
            '#0010251276V#1007F#5P那个奈尔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010251277V这情报军队早就\n',
            '给过我们了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0270251278V#143F什么～！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270251279V#145F我、我这可是刚到手的\n',
            '最新资料啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080251280V#073F#5P这听不听都一样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251281V#1007F#5P嗯，我们还是\n',
            '去找别人吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0270251282V#144F你们给我等等～！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270251283V竟被小看到这种程度，\n',
            '利贝尔通讯头号实力派记者\n',
            '奈尔·班兹的名声可要受损了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270251284V#141F好吧……\n',
            '就把到目前为止我的\n',
            '推理说给你们听听吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251285V#1015F#5P哟……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040251286V#035F#5P呵呵，那就请你长话短说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0270251287V#142F唔……你们给我听好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270251288V我认为这次的案件\n',
            '是恶作剧型的犯罪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251289V#1025F#5P嗯～这我也不是\n',
            '没假设过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080251290V#070F#5P能不能说说你这么\n',
            '确定这一点的理由？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0270251291V#140F以记者的经验来看……\n',
            '那份恐吓信没有真实性。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270251292V本来恐吓信也该包含有\n',
            '具体且符合现实的要求，\n',
            '这样才有意义。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270251293V但是，那份恐吓信却并非如此。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040251294V#030F#5P呼，确实有点道理。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040251295V只是说『会发生灾难』的话\n',
            '有关人士根本无法应对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0270251296V#141F就是这么回事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270251297V实在无法相信这信真的\n',
            '想要妨碍条约。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270251298V虽然不知道是谁，不过\n',
            '那个人看来很高兴把时局搞乱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251299V#1004F#5P原、原来如此……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060251300V#047F#5P有点道理。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060251301V#542F只不过，恐吓信寄了９个地方\n',
            '很令人在意……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060251302V而且每一处都是与\n',
            '条约是有关联的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080251303V#074F#5P确实，如果只是恶作剧的话\n',
            '又似乎太了解内情了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0270251304V#145F嗯～被你这么一说……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270251305V#141F不过这些情况只要愿意，\n',
            '调查一下就行。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270251306V总之我现在在以恶作剧为前提\n',
            '收集着信息。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270251307V你们可以从别的\n',
            '角度尝试调查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251308V#1006F#5P嗯，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010251309V#1001F谢谢你，奈尔。\n',
            '你的意见很重要。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0270251310V#141F哼哼，不假吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270251311V反正查到些什么\n',
            '我们就彼此交换情报。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270251312V我在互不侵犯条约缔结前\n',
            '也准备留在王都。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251313V#1011F#5P哦，这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010251314V#1004F对了，说起来的话……\n',
            '朵洛希在干什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0270251315V#143F哦，那家伙在\n',
            '柏斯地区出差。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270251316V我想让她去\n',
            '拍点照片。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251317V#1015F#5P特辑？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0270251318V#141F王国军相关的特辑。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270251319V不是有座空贼使用过的\n',
            '中世纪的城堡吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270251320V现在那里成了王国军的\n',
            '训练基地。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270251321V好像在进行飞船的\n',
            '操纵训练什么的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251322V#1006F#5P哦，是吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010251323V那么她是去\n',
            '那座基地采访了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0270251324V#145F算是吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270251325V虽然目前交给她一个人\n',
            '还有点令人担心……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251326V#1016F#5P嗯……\n',
            '确实无法否定啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010251327V#1004F啊，对了。\n',
            '还有一件事想\n',
            '问问奈尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0270251328V#143F嗯？',
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
            '向奈尔询问了关于玲双亲的情况。',
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
            '#0270251329V#142F克洛斯贝尔的贸易商\n',
            '哈罗德·海瓦斯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270251330V唔，没听说过。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270251331V也不记得我们的杂志\n',
            '有登他们的寻人启事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251332V#1007F#5P是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0270251333V#141F算了，给你们免费服务一次。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270251334V如果实在找不到的话\n',
            '我也来帮忙吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270251335V我可以帮你们刊登寻人启事，\n',
            '或者去问问\n',
            '我在克洛斯贝尔的熟人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251336V#1001F#5P谢谢你，奈尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010251337V#1008F嘿嘿，感觉今天\n',
            '你比平时来得可靠。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010251338V我对你都有点刮目相看了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0270251339V#147F是吧是吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270251340V#144F等等，难道说我平时\n',
            '就不可靠吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251341V#1016F#5P讨厌～\n',
            '这是一种修辞啦。',
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
        'loc_56C3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_56C3',
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
            TXT(0x00, '【◇在第１章选了阿加特作为同伴】\n'),
            TXT(0x01, '【◇在第１章选了雪拉扎德作为同伴】\n'),
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
        (0x00000000, 'loc_56B7'),
        (0x00000001, 'loc_56BD'),
        (-1, 'loc_56C3'),
    )

    def _loc_56B7(): pass

    label('loc_56B7')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_56C3')

    def _loc_56BD(): pass

    label('loc_56BD')

    ClearScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_56C3')

    def _loc_56C3(): pass

    label('loc_56C3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_572D',
    )

    ChrTalk(
        0x0108,
        (
            '#0080251342V#070F#5P好，那么我们\n',
            '回协会吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080251343V阿加特那家伙也\n',
            '应该已经回去了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5789')

    def _loc_572D(): pass

    label('loc_572D')

    ChrTalk(
        0x0108,
        (
            '#0080251342V#070F#5P好，那么我们\n',
            '回协会吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080251345V雪拉扎德也\n',
            '应该已经回去了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5789(): pass

    label('loc_5789')

    ChrTalk(
        0x0104,
        (
            '#0040251346V#031F#5P嗯，是吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060251347V#048F#5P奈尔先生。\n',
            '非常感谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0270251348V#141F没什么的啦。\n',
            '请再来哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    CameraMove(-59640, 0, 123290, 0)
    OP_67(0, 6150, -10000, 0)
    CameraSetDistance(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    ChrSetDirection(0x0008, 90, 0)
    CreateThread(0x0008, 0x00, 0x00, func_02_5E1)
    ChrSetPos(0x0000, -59640, 0, 123290, 90)
    ChrSetPos(0x0001, -59640, 0, 123290, 90)
    ChrSetPos(0x0002, -59640, 0, 123290, 90)
    ChrSetPos(0x0003, -59640, 0, 123290, 90)
    Sleep(500)

    FadeIn(1000, 0)
    ChrClearFlags(0x0008, 0x0010)
    SetScenaFlags(ScenaFlag(0x02C5, 0, 0x1628))
    OP_28(0x008B, 0x02, 0x1000)
    OP_28(0x008B, 0x01, 0x2000)
    OP_28(0x008B, 0x01, 0x4000)
    EventEnd(0x00)

    Return()

# id: 0x0012 offset: 0x58CF
@scena.Code('func_12_58CF')
def func_12_58CF():
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
        'loc_58EF',
    )

    Call(0, 0x0013)
    Call(0, 0x0014)
    FadeIn(0, 0)

    def _loc_58EF(): pass

    label('loc_58EF')

    Fade(1000)
    ChrSetPos(0x0101, 61220, 0, 550, 0)
    ChrSetPos(0x0107, 60230, 0, 550, 0)
    ChrSetPos(0x00F7, 60630, 0, -480, 0)
    ChrSetPos(0x00F9, 61610, 0, -550, 0)
    ChrSetDirection(0x000E, 180, 0)
    ChrSetSubChip(0x000E, 0)
    CameraMove(61320, 0, 1590, 0)
    OP_67(0, 6150, -10000, 0)
    CameraSetDistance(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010260696V#1015F#6P我说老板啊，\n',
            '这里的招牌菜是什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#2380260697V#5P那当然是\n',
            '咖啡了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#2380260698V#5P那可是混和了龙豆、用玻璃壶\n',
            '沏的我们最为自豪的上品。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#2380260699V#5P还有大量使用了香料的\n',
            '咖喱饭也相当受欢迎哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010260700V#1006F#6P辣咖喱、苦咖啡……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070260701V#061F这就是所谓的『又辣又苦又美味的店』啊⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_5B20',
    )

    ChrTalk(
        0x0106,
        (
            '#0050260702V#051F请问，有没有一个穿\n',
            '白色礼服的小姑娘来过？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5B60')

    def _loc_5B20(): pass

    label('loc_5B20')

    ChrTalk(
        0x0103,
        (
            '#0030260703V#020F请问，有没有一个穿\n',
            '白色礼服的女孩子来过？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5B60(): pass

    label('loc_5B60')

    ChrTalk(
        0x000E,
        (
            '#2380260704V#5P嗯，刚才来过的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#2380260705V#5P点了咖啡牛奶，\n',
            '喝得津津有味的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#2380260706V#5P对了，她还问了我\n',
            '一个奇怪的问题……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5C23',
    )

    ChrTalk(
        0x0108,
        (
            '#0080260707V#073F什么问题？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5C46')

    def _loc_5C23(): pass

    label('loc_5C23')

    ChrTalk(
        0x0105,
        (
            '#0060260708V#044F是什么问题？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5C46(): pass

    label('loc_5C46')

    ChrTalk(
        0x000E,
        (
            '#2380260709V#5P『没人管就会消失的点心\n',
            '在哪儿有卖？』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010260710V#1006F#6P『没人管就会消失的点心』……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010260711V……好，我记下了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010260712V唔～感觉快要\n',
            '追上她了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x02C6, 3, 0x1633))
    OP_28(0x008C, 0x01, 0x0080)
    EventEnd(0x00)

    Return()

# id: 0x0013 offset: 0x5D0A
@scena.Code('func_13_5D0A')
def func_13_5D0A():
    FadeOut(0, 0, -1)
    ClearScenaFlags(ScenaFlag(0x0240, 0, 0x1200))
    ClearScenaFlags(ScenaFlag(0x0240, 1, 0x1201))
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x09, 0xFF)

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
        (0x00000000, 'loc_5D87'),
        (0x00000001, 'loc_5D8D'),
        (-1, 'loc_5D93'),
    )

    def _loc_5D87(): pass

    label('loc_5D87')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_5D93')

    def _loc_5D8D(): pass

    label('loc_5D8D')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_5D93')

    def _loc_5D93(): pass

    label('loc_5D93')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_5DA1',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    Jump('loc_5DA5')

    def _loc_5DA1(): pass

    label('loc_5DA1')

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    def _loc_5DA5(): pass

    label('loc_5DA5')

    Return()

# id: 0x0014 offset: 0x5DA6
@scena.Code('func_14_5DA6')
def func_14_5DA6():
    MapClearFlags(0x00000001)
    CameraMove(106730, -1920, 53920, 0)
    Sleep(100)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_5DE5',
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
            ChrTable['科洛丝'],
            ChrTable['金'],
            0xFFFF,
        ),
    )

    Jump('loc_5DFF')

    def _loc_5DE5(): pass

    label('loc_5DE5')

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
            ChrTable['科洛丝'],
            ChrTable['金'],
            0xFFFF,
        ),
    )

    def _loc_5DFF(): pass

    label('loc_5DFF')

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

# id: 0x0015 offset: 0x5E1F
@scena.Code('func_15_5E1F')
def func_15_5E1F():
    EventBegin(0x00)
    Fade(1000)
    ChrSetPos(0x0101, 60480, 0, 540, 0)
    ChrSetPos(0x0102, 61400, 0, 540, 0)
    ChrSetPos(0x00F8, 60480, 0, -800, 0)
    ChrSetPos(0x00F9, 61400, 0, -800, 0)
    OP_0D()

    ChrTalk(
        0x000E,
        (
            '#2380370924V哟……这本书是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#2380370925V应该是流行于街头巷尾的\n',
            '传说中的《牌技师杰克》吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370926V#1004F啊，你是说这本小说？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#2380370927V嗯，是的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#2380370928V以共和国为舞台、\n',
            '背负了不幸命运的\n',
            '牌技师们的故事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#2380370938V嗯嗯，真吸引人。\n',
            '我很早就想读它了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370939V#1015F（唔～我也受了不少\n',
            '　老板的关照……)',
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
            TXT(0x00, '【给店主小说】\n'),
            TXT(0x01, '【不给】\n'),
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
        'loc_6033',
    )

    Call(0, 0x0017)

    Jump('loc_605B')

    def _loc_6033(): pass

    label('loc_6033')

    ChrTalk(
        0x0101,
        (
            '#0010370940V#1016F（还是算了吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_605B(): pass

    label('loc_605B')

    EventEnd(0x00)

    Return()

# id: 0x0016 offset: 0x605E
@scena.Code('func_16_605E')
def func_16_605E():
    EventBegin(0x00)
    Fade(1000)
    ChrSetPos(0x0101, 60480, 0, 540, 0)
    ChrSetPos(0x0102, 61400, 0, 540, 0)
    ChrSetPos(0x00F8, 60480, 0, -800, 0)
    ChrSetPos(0x00F9, 61400, 0, -800, 0)
    OP_0D()

    ChrTalk(
        0x000E,
        (
            '#2380370987V咦，你这是？',
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
            TXT(0x00, '【给店主小说】\n'),
            TXT(0x01, '【不给】\n'),
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
        'loc_612A',
    )

    Call(0, 0x0017)

    Jump('loc_6152')

    def _loc_612A(): pass

    label('loc_612A')

    ChrTalk(
        0x0101,
        (
            '#0010370988V#1016F（还是算了吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6152(): pass

    label('loc_6152')

    EventEnd(0x00)

    Return()

# id: 0x0017 offset: 0x6155
@scena.Code('func_17_6155')
def func_17_6155():
    ChrTalk(
        0x0101,
        (
            '#0010370941V#1001F喏，给你。\n',
            '就送给老板吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#2380370942V啊，我不是为了要书\n',
            '才跟你们说这些的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370943V#1000F请别介意。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010370944V这就当\n',
            '美味咖喱和咖啡的回礼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#2380370945V你能这么说\n',
            '我真高兴…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#2380370946V这样的话\n',
            '那我就不客气了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '牌技师杰克',
            (TxtCtl.SetColor, 0x0),
            '交给了店主。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_59()
    RemoveItem(ItemTable['牌技师杰克 １卷'], 1)
    RemoveItem(ItemTable['牌技师杰克 ２卷'], 1)
    RemoveItem(ItemTable['牌技师杰克 ３卷'], 1)
    RemoveItem(ItemTable['牌技师杰克 ４卷'], 1)
    RemoveItem(ItemTable['牌技师杰克 ５卷'], 1)
    RemoveItem(ItemTable['牌技师杰克 ６卷'], 1)
    RemoveItem(ItemTable['牌技师杰克 ７卷'], 1)
    RemoveItem(ItemTable['牌技师杰克 ８卷'], 1)
    RemoveItem(ItemTable['牌技师杰克 ９卷'], 1)
    RemoveItem(ItemTable['牌技师杰克 10卷'], 1)
    RemoveItem(ItemTable['牌技师杰克 11卷'], 1)
    RemoveItem(ItemTable['牌技师杰克 12卷'], 1)
    RemoveItem(ItemTable['牌技师杰克 13卷'], 1)
    RemoveItem(ItemTable['牌技师杰克 14卷'], 1)
    OP_0D()

    ChrTalk(
        0x000E,
        (
            '#2380370970V谢谢，我会每晚\n',
            '一点点地读的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#2380370948V对了……\n',
            '这点不成敬意的东西\n',
            '请收下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.Item, ItemTable['塞姆里亚石']),
            (TxtCtl.SetColor, 0x0),
            '收下了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_59()
    AddItem(ItemTable['塞姆里亚石'], 1)
    OP_0D()

    ChrTalk(
        0x0102,
        (
            '#0020370949V#1044F这是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#2380370950V这是我还在当外交官的时候，\n',
            '在亚尔特利亚得到的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370951V#1015F亚尔特利亚应该是\n',
            '七耀教会的总部吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#2380370927V嗯，是的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#2380370953V这好像是用很久以前的塞姆里亚时代\n',
            '出产的金属制成的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020370954V#1044F塞姆里亚时代的？\n',
            '确实从没见过这样的金属……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#2380370955V哈哈，我也不知道\n',
            '是真是假。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#2380370956V顺带一提，加工此物的技术\n',
            '据说已经完全失传了了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370980V#1018F哟，这么看来，\n',
            '还挺有传奇色彩的嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00DE, 7, 0x6F7)),
            Expr.Return,
        ),
        'loc_6660',
    )

    ChrTalk(
        0x0102,
        (
            '#0020370958V#1040F记得以前老板也拿武器\n',
            '来跟我换过书吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#2380370959V哈哈，我还记得。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#2380370983V不过这次不是什么了不起的东西，\n',
            '不好意思……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370984V#1001F不不，我会好好珍惜它的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_66C9')

    def _loc_6660(): pass

    label('loc_6660')

    ChrTalk(
        0x000E,
        (
            '#2380370985V哈哈，这也不算什么，\n',
            '你就当作是护身符吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370961V#1001F嗯，我会好好珍惜它的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_66C9(): pass

    label('loc_66C9')

    SetScenaFlags(ScenaFlag(0x0218, 4, 0x10C4))

    Return()

# id: 0x0018 offset: 0x66CD
@scena.Code('func_18_66CD')
def func_18_66CD():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '巴拉尔咖啡厅的名菜！\n',
            '『完熟咖喱饭』 ９００米拉',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '请一定要品尝用秘传香料\n',
            '特制的辛辣咖喱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0019 offset: 0x675B
@scena.Code('func_19_675B')
def func_19_675B():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '～　目录　～\n',
            '仿手工制派　４００米拉\n',
            '苦西红柿三明治　１４００米拉',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '～ 本店招牌菜　～\n',
            '热海汁　１２００米拉',
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
