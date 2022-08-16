import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T4313_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4313   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4313.x'
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
        ('ED6_DT07/CH01570._CH', 'ED6_DT07/CH01570P._CP'),
        ('ED6_DT07/CH02140._CH', 'ED6_DT07/CH02140P._CP'),
        ('ED6_DT27/CH03004._CH', 'ED6_DT27/CH03004P._CP'),
        ('ED6_DT27/CH03510._CH', 'ED6_DT27/CH03510P._CP'),
        ('ED6_DT27/CH03590._CH', 'ED6_DT27/CH03590P._CP'),
        ('ED6_DT27/CH03123._CH', 'ED6_DT27/CH03123P._CP'),
        ('ED6_DT27/CH03670._CH', 'ED6_DT27/CH03670P._CP'),
        ('ED6_DT27/CH03690._CH', 'ED6_DT27/CH03690P._CP'),
        ('ED6_DT07/CH01200._CH', 'ED6_DT07/CH01200P._CP'),
        ('ED6_DT07/CH01230._CH', 'ED6_DT07/CH01230P._CP'),
        ('ED6_DT27/CH03720._CH', 'ED6_DT27/CH03720P._CP'),
        ('ED6_DT07/CH01310._CH', 'ED6_DT07/CH01310P._CP'),
        ('ED6_DT07/CH01350._CH', 'ED6_DT07/CH01350P._CP'),
        ('ED6_DT07/CH01770._CH', 'ED6_DT07/CH01770P._CP'),
        ('ED6_DT07/CH01100._CH', 'ED6_DT07/CH01100P._CP'),
        ('ED6_DT07/CH01490._CH', 'ED6_DT07/CH01490P._CP'),
        ('ED6_DT07/CH01050._CH', 'ED6_DT07/CH01050P._CP'),
        ('ED6_DT07/CH01160._CH', 'ED6_DT07/CH01160P._CP'),
        ('ED6_DT07/CH02470._CH', 'ED6_DT07/CH02470P._CP'),
    ]

# id: 0x10001 offset: 0x142
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '管家雷蒙德',
            x                   = -11850,
            z                   = 0,
            y                   = 20220,
            direction           = 225,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '杜南公爵',
            x                   = -16000,
            z                   = 0,
            y                   = -38500,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '玲',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '希德中校',
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
            name                = '凯诺娜',
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
            name                = '卡西乌斯',
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
            name                = '理查德',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '沃尔特议员',
            x                   = -14110,
            z                   = 0,
            y                   = -8710,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '莉卡妲夫人',
            x                   = -10410,
            z                   = 0,
            y                   = -15620,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '爱尔莎大使',
            x                   = -14830,
            z                   = 0,
            y                   = -14420,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '贝尔克副队长',
            x                   = 11910,
            z                   = 0,
            y                   = 18100,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '西莫鲁',
            x                   = -19030,
            z                   = 0,
            y                   = 20590,
            direction           = 315,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '妮娜',
            x                   = -12710,
            z                   = 0,
            y                   = 48170,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '图书管理员皮埃多罗',
            x                   = 20140,
            z                   = 0,
            y                   = -42620,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            name                = '约克姆老人',
            x                   = 10340,
            z                   = 0,
            y                   = -41560,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            name                = '游客',
            x                   = 14120,
            z                   = 0,
            y                   = 50600,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 16,
            chipIndex           = 16,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            name                = '游客',
            x                   = 15980,
            z                   = 0,
            y                   = 50600,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            name                = '管家菲利普',
            x                   = -12960,
            z                   = 0,
            y                   = -44100,
            direction           = 87,
            word_0E             = 0,
            dword_10            = 18,
            chipIndex           = 18,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
    )

# id: 0x10002 offset: 0x382
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x382
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x382
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -13210,
            triggerZ            = 0,
            triggerY            = 18820,
            triggerRange        = 800,
            actorX              = -11850,
            actorZ              = 1500,
            actorY              = 20220,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -14700,
            triggerZ            = 0,
            triggerY            = 47000,
            triggerRange        = 2000,
            actorX              = -18500,
            actorZ              = 1500,
            actorY              = 46500,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0011,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -17800,
            triggerZ            = 0,
            triggerY            = 47000,
            triggerRange        = 2000,
            actorX              = -18500,
            actorZ              = 1500,
            actorY              = 46500,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0011,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -21000,
            triggerZ            = 0,
            triggerY            = 47000,
            triggerRange        = 2000,
            actorX              = -18500,
            actorZ              = 1500,
            actorY              = 46500,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0011,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 25980,
            triggerZ            = 0,
            triggerY            = 50580,
            triggerRange        = 800,
            actorX              = 25690,
            actorZ              = 1500,
            actorY              = 51500,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0013,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -10300,
            triggerZ            = 0,
            triggerY            = 19220,
            triggerRange        = 500,
            actorX              = -10900,
            actorZ              = 1500,
            actorY              = 19110,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x001C,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 22140,
            triggerZ            = 0,
            triggerY            = 50600,
            triggerRange        = 800,
            actorX              = 21830,
            actorZ              = 890,
            actorY              = 51760,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0022,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 18200,
            triggerZ            = 0,
            triggerY            = 51350,
            triggerRange        = 800,
            actorX              = 18200,
            actorZ              = 1800,
            actorY              = 51350,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0023,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 14200,
            triggerZ            = 0,
            triggerY            = 51310,
            triggerRange        = 800,
            actorX              = 14200,
            actorZ              = 2000,
            actorY              = 51310,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0024,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 10220,
            triggerZ            = 0,
            triggerY            = 51150,
            triggerRange        = 800,
            actorX              = 10220,
            actorZ              = 1200,
            actorY              = 51150,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0025,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 24340,
            triggerZ            = 0,
            triggerY            = 45480,
            triggerRange        = 800,
            actorX              = 24340,
            actorZ              = 500,
            actorY              = 45480,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0026,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x50E
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_561',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_55E',
    )

    ChrSetPos(0x0008, -15170, 0, 17070, 225)
    ChrSetPos(0x0013, -16940, 0, 16460, 90)
    ChrSetPos(0x0014, -15820, 0, 15350, 0)
    ChrSetFlags(0x000F, 0x0080)
    ChrSetFlags(0x0010, 0x0080)

    def _loc_55E(): pass

    label('loc_55E')

    Jump('loc_63E')

    def _loc_561(): pass

    label('loc_561')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_63E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_5A8',
    )

    ChrSetPos(0x000F, -14830, 0, -13010, 180)
    ChrSetPos(0x0014, 18250, 0, 44450, 0)
    ChrClearFlags(0x0012, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0016, 0x0080)

    Jump('loc_63E')

    def _loc_5A8(): pass

    label('loc_5A8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 3, 0x162B)),
            Expr.Return,
        ),
        'loc_5B2',
    )

    Jump('loc_63E')

    def _loc_5B2(): pass

    label('loc_5B2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            Expr.Return,
        ),
        'loc_625',
    )

    ChrSetPos(0x000F, -11700, 0, -14320, 274)
    ChrSetPos(0x0010, -13610, 0, -14320, 93)
    ChrSetFlags(0x0013, 0x0080)
    ChrSetFlags(0x0014, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0017, 23640, 0, 44900, 0)
    ChrSetPos(0x0018, 25640, 0, 44900, 270)
    ChrClearFlags(0x0017, 0x0080)
    ChrClearFlags(0x0018, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 0, 0x1618)),
            Expr.Return,
        ),
        'loc_622',
    )

    ChrClearFlags(0x0019, 0x0080)

    def _loc_622(): pass

    label('loc_622')

    Jump('loc_63E')

    def _loc_625(): pass

    label('loc_625')

    ChrSetFlags(0x0013, 0x0080)
    ChrSetFlags(0x0014, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x0017, 0x0080)
    ChrClearFlags(0x0018, 0x0080)

    def _loc_63E(): pass

    label('loc_63E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_65D',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    MapSetFlags(0x10000000)
    Event(0, func_1E_7124)

    Jump('loc_67D')

    def _loc_65D(): pass

    label('loc_65D')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_669'),
        (-1, 'loc_67D'),
    )

    def _loc_669(): pass

    label('loc_669')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 2, 0x1612)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_67A',
    )

    MapSetFlags(0x10000000)
    Event(0, func_14_2F53)

    def _loc_67A(): pass

    label('loc_67A')

    Jump('loc_67D')

    def _loc_67D(): pass

    label('loc_67D')

    Return()

# id: 0x0001 offset: 0x67E
@scena.Code('func_01_67E')
def func_01_67E():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_68E',
    )

    OP_64(0x00, 0x0001)

    def _loc_68E(): pass

    label('loc_68E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            Expr.Return,
        ),
        'loc_6A5',
    )

    OP_64(0x01, 0x0001)
    OP_64(0x02, 0x0001)
    OP_64(0x03, 0x0001)
    OP_64(0x05, 0x0001)

    def _loc_6A5(): pass

    label('loc_6A5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 3, 0x162B)),
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_6B6',
    )

    OP_72(0x0007, 0x0004)

    def _loc_6B6(): pass

    label('loc_6B6')

    Return()

# id: 0x0002 offset: 0x6B7
@scena.Code('func_02_6B7')
def func_02_6B7():
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
        'loc_6DC',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_81E')

    def _loc_6DC(): pass

    label('loc_6DC')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6F5',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_81E')

    def _loc_6F5(): pass

    label('loc_6F5')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_70E',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_81E')

    def _loc_70E(): pass

    label('loc_70E')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_727',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_81E')

    def _loc_727(): pass

    label('loc_727')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_740',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_81E')

    def _loc_740(): pass

    label('loc_740')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_759',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_81E')

    def _loc_759(): pass

    label('loc_759')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_772',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_81E')

    def _loc_772(): pass

    label('loc_772')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_78B',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_81E')

    def _loc_78B(): pass

    label('loc_78B')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7A4',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_81E')

    def _loc_7A4(): pass

    label('loc_7A4')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7BD',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_81E')

    def _loc_7BD(): pass

    label('loc_7BD')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7D6',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_81E')

    def _loc_7D6(): pass

    label('loc_7D6')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7EF',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_81E')

    def _loc_7EF(): pass

    label('loc_7EF')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_808',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_81E')

    def _loc_808(): pass

    label('loc_808')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_81E',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_81E(): pass

    label('loc_81E')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_833',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_81E')

    def _loc_833(): pass

    label('loc_833')

    Return()

# id: 0x0003 offset: 0x834
@scena.Code('func_03_834')
def func_03_834():
    Call(0, 0x0004)

    Return()

# id: 0x0004 offset: 0x839
@scena.Code('func_04_839')
def func_04_839():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_93D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_93A',
    )

    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_8B1',
    )

    ChrTalk(
        0x0008,
        (
            '什么也不做令人心神不宁，\n',
            '就决定开始大扫除了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '之后只有等待\n',
            '女王陛下的指示了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_937')

    def _loc_8B1(): pass

    label('loc_8B1')

    ChrTalk(
        0x0008,
        (
            '总之，到底\n',
            '会变成怎样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '什么也不做令人心神不宁，\n',
            '就决定开始离宫的大扫除了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '如果有事情做\n',
            '就用不着考虑多余的事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_937(): pass

    label('loc_937')

    TalkEnd(0x0008)

    def _loc_93A(): pass

    label('loc_93A')

    Jump('loc_E38')

    def _loc_93D(): pass

    label('loc_93D')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_E38',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_B1D',
    )

    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02CC, 2, 0x1662)),
            Expr.Return,
        ),
        'loc_9AF',
    )

    ChrTalk(
        0x0008,
        (
            '似乎发生了很多事，\n',
            '不过能解决就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '总是给你们添麻烦\n',
            '真是不好意思呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B17')

    def _loc_9AF(): pass

    label('loc_9AF')

    ChrTalk(
        0x0008,
        (
            '啊，你们是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '今天玲\n',
            '没有一起来吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1003F玲她……\n',
            '回到父母身边了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '咦咦！？\n',
            '找到她父母了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '听说在王都\n',
            '发生了不得了的事情\n',
            '正在担心呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '是吗，\n',
            '那就好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1005F一点都不好！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '咦！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1009F我一定要抓住她，\n',
            '把她给带回来！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '带、带回来，\n',
            '她父母有什么问题吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '嗯～最近由于父母的情况\n',
            '孩子的环境真是复杂啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x02CC, 2, 0x1662))

    def _loc_B17(): pass

    label('loc_B17')

    TalkEnd(0x0008)

    Jump('loc_E38')

    def _loc_B1D(): pass

    label('loc_B1D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 3, 0x162B)),
            Expr.Return,
        ),
        'loc_CE6',
    )

    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02CC, 1, 0x1661)),
            Expr.Return,
        ),
        'loc_B74',
    )

    ChrTalk(
        0x0008,
        (
            '玲似乎和大家\n',
            '相处融洽，我就放心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '早点找到父母就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CE0')

    def _loc_B74(): pass

    label('loc_B74')

    ChrTurnDirection(0x0008, 0x012F, 0)

    ChrTalk(
        0x0008,
        (
            '呀，这不是玲吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x012F,
        (
            '#261F啊、管家大哥哥！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#265F哈哈哈，今天\n',
            '也和玲躲猫猫吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '啊，啊哈哈……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '抱歉，今天\n',
            '还有工作，就算了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x012F,
        (
            '#268F男人真没意思。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#266F总是说工作、工作的\n',
            '结果又不陪我玩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '呜……真是一针见血……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0000, 400)

    ChrTalk(
        0x0008,
        (
            '但是，她和大家\n',
            '看上去好像很融洽，我可以放心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1016F啊、啊哈哈，托你的福。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x02CC, 1, 0x1661))

    def _loc_CE0(): pass

    label('loc_CE0')

    TalkEnd(0x0008)

    Jump('loc_E38')

    def _loc_CE6(): pass

    label('loc_CE6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            Expr.Return,
        ),
        'loc_D43',
    )

    TalkBegin(0x0008)

    ChrTalk(
        0x0008,
        (
            '说实话，我真是不知如何是好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '交给游击士协会的话，\n',
            '就能放心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0008)

    Jump('loc_E38')

    def _loc_D43(): pass

    label('loc_D43')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 6, 0x160E)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 7, 0x160F)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 0, 0x1610)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 1, 0x1611)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 2, 0x1612)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_D61',
    )

    Call(0, 0x001B)

    Jump('loc_E38')

    def _loc_D61(): pass

    label('loc_D61')

    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_DAD',
    )

    ChrTalk(
        0x0008,
        (
            '呼～话说回来\n',
            '到底藏在哪儿呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '这个离宫也很大啊～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E35')

    def _loc_DAD(): pass

    label('loc_DAD')

    ChrTalk(
        0x0008,
        (
            '呀，怎样，\n',
            '能找到那女孩吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1007F嗯～现在\n',
            '还不好说……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1006F不过，再到一些想到的地方\n',
            '找找看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '嗯，拜托你们了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_E35(): pass

    label('loc_E35')

    TalkEnd(0x0008)

    def _loc_E38(): pass

    label('loc_E38')

    Return()

# id: 0x0005 offset: 0xE39
@scena.Code('func_05_E39')
def func_05_E39():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 0, 0x1618)),
            Expr.Return,
        ),
        'loc_EDF',
    )

    TalkBegin(0x0009)

    ChrTalk(
        0x0009,
        (
            '#0640241022V#222F你们啊，是不是向菲利普\n',
            '灌输了什么？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640241023V最近只要看到他\n',
            '总是挑三拣四诸多要求……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640241024V#224F到底当我是什么人啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0009)

    Jump('loc_FA1')

    def _loc_EDF(): pass

    label('loc_EDF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            Expr.Return,
        ),
        'loc_F3A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 3, 0x1613)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_EF5',
    )

    Call(0, 0x001A)

    Jump('loc_F37')

    def _loc_EF5(): pass

    label('loc_EF5')

    TalkBegin(0x0009)

    ChrTalk(
        0x0009,
        (
            '#0640241025V#224F哎，带着这小丫头\n',
            '赶快从这房间里出去！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0009)

    def _loc_F37(): pass

    label('loc_F37')

    Jump('loc_FA1')

    def _loc_F3A(): pass

    label('loc_F3A')

    TalkBegin(0x0009)

    ChrTalk(
        0x0009,
        (
            '#0640241026V#222F穿白裙子的女孩？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640241027V#224F不认识那种小丫头！\n',
            '赶快从这房间里出去！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0009)

    def _loc_FA1(): pass

    label('loc_FA1')

    Return()

# id: 0x0006 offset: 0xFA2
@scena.Code('func_06_FA2')
def func_06_FA2():
    TalkBegin(0x000F)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_139B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_1004',
    )

    ChrTalk(
        0x00FE,
        (
            '第一次见到爱尔莎大使……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎呀……\n',
            '还真是相当伶牙俐齿的女性啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_139B')

    def _loc_1004(): pass

    label('loc_1004')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 3, 0x162B)),
            Expr.Return,
        ),
        'loc_1170',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_1057',
    )

    ChrTalk(
        0x00FE,
        (
            '哈哈，我妻子的话\n',
            '请别放在心上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '她是因为\n',
            '不太了解政治。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_116D')

    def _loc_1057(): pass

    label('loc_1057')

    ChrTalk(
        0x00FE,
        (
            '互不侵犯条约……共和国议会也是\n',
            '各种各样的意见交织混杂啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '厌恶帝国的民和党等从当初开始\n',
            '就表现出反对的态度。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要封住过激的在野党\n',
            '每次都让总统伤透脑筋……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '由于新型引擎的事\n',
            '这次很容易获得了过半数的赞成。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '靠艾莉茜雅女王的手腕共和国的\n',
            '总统似乎也能成事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_116D(): pass

    label('loc_116D')

    Jump('loc_139B')

    def _loc_1170(): pass

    label('loc_1170')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            Expr.Return,
        ),
        'loc_128D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_11DF',
    )

    ChrTalk(
        0x00FE,
        (
            '哈哈，看来她的心思\n',
            '都在王都旅游上呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，因为是各种各样的主义主张\n',
            '共存的共和国嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_128A')

    def _loc_11DF(): pass

    label('loc_11DF')

    ChrTalk(
        0x00FE,
        (
            '我的妻子对政治\n',
            '缺乏根本的理解。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这次打算纠正这个\n',
            '才带她同行……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈哈，看来她的心思\n',
            '都在王都旅游上呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，因为是各种各样的主义主张\n',
            '共存的共和国嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_128A(): pass

    label('loc_128A')

    Jump('loc_139B')

    def _loc_128D(): pass

    label('loc_128D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_139B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_12F4',
    )

    ChrTalk(
        0x00FE,
        (
            '我是共和国议会的议员，\n',
            '我叫沃尔特。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '顺便视察和准备签字仪式\n',
            '就提前到现场了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_139B')

    def _loc_12F4(): pass

    label('loc_12F4')

    ChrTalk(
        0x00FE,
        (
            '我是共和国议会的议员，\n',
            '我叫沃尔特。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '顺便视察和准备签字仪式\n',
            '就提前到现场了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔，相当\n',
            '出色的离宫不是吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '确实可以说是进行签字仪式\n',
            '最适合的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_139B(): pass

    label('loc_139B')

    TalkEnd(0x000F)

    Return()

# id: 0x0007 offset: 0x139F
@scena.Code('func_07_139F')
def func_07_139F():
    TalkBegin(0x0010)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_15AA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_1406',
    )

    ChrTalk(
        0x00FE,
        (
            '因此，我多次\n',
            '对丈夫说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在对政治高谈阔论之前\n',
            '应该先学习与人交往。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15AA')

    def _loc_1406(): pass

    label('loc_1406')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 3, 0x162B)),
            Expr.Return,
        ),
        'loc_14AC',
    )

    ChrTalk(
        0x00FE,
        (
            '像丈夫一样的小人物和总统啊\n',
            '艾莉茜雅女王等人谈话，\n',
            '实在太奇怪了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在成为大人物之前应该\n',
            '以谦虚的姿态行事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为公事而来\n',
            '却还没和大使打过招呼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15AA')

    def _loc_14AC(): pass

    label('loc_14AC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            Expr.Return,
        ),
        'loc_154D',
    )

    ChrTalk(
        0x00FE,
        (
            '像丈夫这样，\n',
            '一介议员为了签字仪式而出差,\n',
            '本来就没有必要嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好不容易当了议员\n',
            '就随便来看看而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '比起那个，早点去格兰赛尔\n',
            '旅游多好啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15AA')

    def _loc_154D(): pass

    label('loc_154D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_15AA',
    )

    ChrTalk(
        0x00FE,
        (
            '利贝尔王国\n',
            '虽然在地图上是小国家……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但人们都很亲切，\n',
            '并有着非常美丽的土地。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_15AA(): pass

    label('loc_15AA')

    TalkEnd(0x0010)

    Return()

# id: 0x0008 offset: 0x15AE
@scena.Code('func_08_15AE')
def func_08_15AE():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02CC, 3, 0x1663)),
            Expr.Return,
        ),
        'loc_15BA',
    )

    ChrSetFlags(0x00FE, 0x0010)

    def _loc_15BA(): pass

    label('loc_15BA')

    TalkBegin(0x0011)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1C51',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_1C51',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02CC, 3, 0x1663)),
            Expr.Return,
        ),
        'loc_1716',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_164F',
    )

    ChrTalk(
        0x0011,
        (
            '#0680271502V#1113F如果是官方的视察，\n',
            '应该先通过大使馆才对。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0680271503V还是说称为视察的\n',
            '公费旅游来的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1713')

    def _loc_164F(): pass

    label('loc_164F')

    ChrTalk(
        0x0011,
        (
            '#0680271504V#1113F好了，沃尔特议员。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0680271505V远道而来辛苦了\n',
            '虽然想这么说……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0680271506V#1112F如果是官方的视察，\n',
            '应该先通过大使馆才对。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0680271503V还是说称为视察的\n',
            '公费旅游来的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_1713(): pass

    label('loc_1713')

    Jump('loc_1C51')

    def _loc_1716(): pass

    label('loc_1716')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_17A8',
    )

    ChrTalk(
        0x0011,
        (
            '#0680271508V#1110F哎呀，这不是金先生吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0680271509V居然能在这里\n',
            '见面真是意外。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080271510V#070F哈哈，正好\n',
            '路过嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17F5')

    def _loc_17A8(): pass

    label('loc_17A8')

    ChrTalk(
        0x0011,
        (
            '#0680271511V#1110F哎呀，你们。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0680271509V居然能在这里\n',
            '见面真是意外。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_17F5(): pass

    label('loc_17F5')

    ChrTalk(
        0x0101,
        (
            '#0010271513V#1000F你好，爱尔莎大使。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0680271514V#1110F对了对了、恐吓信事件的始末，\n',
            '我听了利贝尔方面的报告哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010271515V#1011F啊，是吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0680271516V#1113F嗯嗯，情报部的余党，\n',
            '特务兵们的秘密工作……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0680271517V#1110F不过，对于艾莉茜雅女王来说\n',
            '应该料到了吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0680271518V不过，我感到\n',
            '没这么简单……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191053V#1016F啊、啊哈哈……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010271520V(和、和外国人这样\n',
            ' 说话真是紧张啊。)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_1A26',
    )

    ChrTalk(
        0x0106,
        (
            '#0050271521V#050F（嗯，这种时候关键看胆量。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050271522V(要是游击士无论对方是谁\n',
            '　最低限度的策略和谈判\n',
            '　还是要能上得了台面才行。)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AB7')

    def _loc_1A26(): pass

    label('loc_1A26')

    ChrTalk(
        0x0103,
        (
            '#0030271523V#020F（不过，还是要看经验和适应能力。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030271524V(要是游击士无论对方是谁\n',
            '　最低限度的策略和谈判\n',
            '　还是要能上得了台面才行。)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1AB7(): pass

    label('loc_1AB7')

    ChrTalk(
        0x0011,
        (
            '#0680271525V#1110F……艾莉茜雅女王看起来，\n',
            '似乎也相当辛苦啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0680271526V但是，政变的处理，\n',
            '不是相当顺利吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0680271527V你们也相当活跃\n',
            '大使馆都在谈论呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010271528V#1016F不，哪里……身为游击士\n',
            '这是应该做的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0680271529V#1111F呵呵，虽然想再详细问问，\n',
            '但现在开始似乎很忙呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0680271530V#1110F下次有机会再聊吧，\n',
            '艾丝蒂尔·布莱特。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010271531V#1000F好，好的，那么，\n',
            '今天就失陪了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x02CC, 3, 0x1663))

    def _loc_1C51(): pass

    label('loc_1C51')

    TalkEnd(0x0011)

    Return()

# id: 0x0009 offset: 0x1C55
@scena.Code('func_09_1C55')
def func_09_1C55():
    TalkBegin(0x0012)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1D9C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_1D9C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_1CD9',
    )

    ChrTalk(
        0x00FE,
        (
            '话说回来，没能追上\n',
            '那个巨大人偶真是懊悔啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今后，被那种东西袭击时，\n',
            '我们怎样应该应对……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D9C')

    def _loc_1CD9(): pass

    label('loc_1CD9')

    ChrTalk(
        0x00FE,
        (
            '虽说有亲卫队的帮助，\n',
            '但要破坏那怪物战车……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是的，你们\n',
            '游击士的力量真不得了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '话说回来，没能追上\n',
            '那个巨大人偶真是懊悔啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今后，被那种东西袭击时，\n',
            '我们应该怎样应对……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    def _loc_1D9C(): pass

    label('loc_1D9C')

    TalkEnd(0x0012)

    Return()

# id: 0x000A offset: 0x1DA0
@scena.Code('func_0A_1DA0')
def func_0A_1DA0():
    TalkBegin(0x0013)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1DEC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1DE9',
    )

    ChrTalk(
        0x00FE,
        (
            '这可是不能输的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '谁打扫的房间多\n',
            '就赢了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1DE9(): pass

    label('loc_1DE9')

    Jump('loc_1E8E')

    def _loc_1DEC(): pass

    label('loc_1DEC')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1E8E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_1E4E',
    )

    ChrTalk(
        0x00FE,
        (
            '希德中校他们\n',
            '好像一直没睡。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '军人也真是辛苦。\n',
            '别搞坏身体就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E8E')

    def _loc_1E4E(): pass

    label('loc_1E4E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 3, 0x162B)),
            Expr.Return,
        ),
        'loc_1E8E',
    )

    ChrTurnDirection(0x00FE, 0x012F, 0)

    ChrTalk(
        0x00FE,
        (
            '哎呀，玲……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵，今天和朋友在一起呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1E8E(): pass

    label('loc_1E8E')

    TalkEnd(0x0013)

    Return()

# id: 0x000B offset: 0x1E92
@scena.Code('func_0B_1E92')
def func_0B_1E92():
    TalkBegin(0x0014)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1F07',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1F04',
    )

    ChrTalk(
        0x00FE,
        (
            '西莫鲁真是的，完全\n',
            '中了雷蒙德先生的招……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，对于名为决斗的事\n',
            '我是不能插手的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1F04(): pass

    label('loc_1F04')

    Jump('loc_2093')

    def _loc_1F07(): pass

    label('loc_1F07')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2093',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_1FE7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_1F62',
    )

    ChrTalk(
        0x00FE,
        (
            '啦啦啦～⊙\n',
            '啦啦噜噜啦啦⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '竖着擦，\n',
            '横着擦，斜着擦⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1FE4')

    def _loc_1F62(): pass

    label('loc_1F62')

    ChrTalk(
        0x00FE,
        (
            '这里展示物多，\n',
            '打扫可辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，也是看本事的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啦啦啦～⊙\n',
            '啦啦噜噜啦啦⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '竖着擦，\n',
            '横着擦，斜着擦⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    def _loc_1FE4(): pass

    label('loc_1FE4')

    Jump('loc_2093')

    def _loc_1FE7(): pass

    label('loc_1FE7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 3, 0x162B)),
            Expr.Return,
        ),
        'loc_2093',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_203A',
    )

    ChrTalk(
        0x00FE,
        (
            '噜噜噜-噜噜-⊙\n',
            '啦啦啦啦啦⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '打扫起来～⊙\n',
            '心也亮晶晶～⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2093')

    def _loc_203A(): pass

    label('loc_203A')

    ChrTalk(
        0x00FE,
        (
            '怎么说这个房间\n',
            '似乎是用作作战会议室呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……啊不好，\n',
            '必须早点扫除完毕才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    def _loc_2093(): pass

    label('loc_2093')

    TalkEnd(0x0014)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_20AE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_20AE',
    )

    ChrSetFlags(0x00FE, 0x0010)

    def _loc_20AE(): pass

    label('loc_20AE')

    Return()

# id: 0x000C offset: 0x20AF
@scena.Code('func_0C_20AF')
def func_0C_20AF():
    TalkBegin(0x0015)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2118',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_2115',
    )

    ChrTalk(
        0x00FE,
        (
            '原来这里\n',
            '来访的人就少……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没有导力的时代也活过，\n',
            '并不觉得特别困难啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2115(): pass

    label('loc_2115')

    Jump('loc_22E8')

    def _loc_2118(): pass

    label('loc_2118')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_22E8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_2184',
    )

    ChrTalk(
        0x00FE,
        (
            '士兵们把瓦雷利亚湖的\n',
            '周边地图拿走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说要在湖里找人偶\n',
            '嘿，到底说什么呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_22E8')

    def _loc_2184(): pass

    label('loc_2184')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 3, 0x162B)),
            Expr.Return,
        ),
        'loc_220D',
    )

    ChrTalk(
        0x00FE,
        (
            '到签字仪式结束之前\n',
            '据说市民禁止进出。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，这下\n',
            '这个房间要变得更加安静了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样的话是不是劝劝\n',
            '士兵们也看看书呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_22E8')

    def _loc_220D(): pass

    label('loc_220D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            Expr.Return,
        ),
        'loc_22AC',
    )

    ChrTalk(
        0x00FE,
        (
            '读书就是要\n',
            '安静的环境。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在这一点上，这里可说\n',
            '是无可挑剔的地方……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过访问的市民大半\n',
            '都是来看庭园或者展览室的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是有点寂寞啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_22E8')

    def _loc_22AC(): pass

    label('loc_22AC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_22E8',
    )

    ChrTalk(
        0x00FE,
        (
            '在找什么书吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……女孩子？\n',
            '哦，没看到啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_22E8(): pass

    label('loc_22E8')

    TalkEnd(0x0015)

    Return()

# id: 0x000D offset: 0x22EC
@scena.Code('func_0D_22EC')
def func_0D_22EC():
    TalkBegin(0x0016)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_235C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_235C',
    )

    ChrTalk(
        0x00FE,
        (
            '今天是作为爱尔莎大使的陪同\n',
            '来到这个离宫了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '爱尔莎大使的话\n',
            '在访问议员的房间呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_235C(): pass

    label('loc_235C')

    TalkEnd(0x0016)

    Return()

# id: 0x000E offset: 0x2360
@scena.Code('func_0E_2360')
def func_0E_2360():
    TalkBegin(0x0017)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2429',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            Expr.Return,
        ),
        'loc_23D6',
    )

    ChrTalk(
        0x00FE,
        (
            '哦～这是利贝尔的先王\n',
            '埃德加Ⅲ世\n',
            '生前最爱用的椅子啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '原来如此～\n',
            '确实有高贵的感觉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2429')

    def _loc_23D6(): pass

    label('loc_23D6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_2429',
    )

    ChrTalk(
        0x00FE,
        (
            '这个共和国大使\n',
            '赠呈的壶真漂亮啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '果然壶\n',
            '还是要共和国的东西好啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2429(): pass

    label('loc_2429')

    TalkEnd(0x0017)

    Return()

# id: 0x000F offset: 0x242D
@scena.Code('func_0F_242D')
def func_0F_242D():
    TalkBegin(0x0018)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_24F4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            Expr.Return,
        ),
        'loc_2495',
    )

    ChrTalk(
        0x00FE,
        (
            '姐姐，在看说明之前，\n',
            '可是说了椅子不少坏话啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……真是的，够起劲的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24F4')

    def _loc_2495(): pass

    label('loc_2495')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_24F4',
    )

    ChrTalk(
        0x00FE,
        (
            '姐姐看的\n',
            '是帝国制作的壶啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '稍微往下看，\n',
            '就写着说明嘛……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是受不了了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_24F4(): pass

    label('loc_24F4')

    TalkEnd(0x0018)

    Return()

# id: 0x0010 offset: 0x24F8
@scena.Code('func_10_24F8')
def func_10_24F8():
    TalkBegin(0x0019)

    ChrTalk(
        0x0019,
        (
            '#0660850004V#720F我相信……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660850005V总有一天阁下\n',
            '会察觉到自己的使命。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660850006V到那天为止我菲利普，粉身碎骨\n',
            '也要诚心诚意服侍他。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0019)

    Return()

# id: 0x0011 offset: 0x258E
@scena.Code('func_11_258E')
def func_11_258E():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 6, 0x160E)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_259D',
    )

    Call(0, 0x0012)

    Jump('loc_25F9')

    def _loc_259D(): pass

    label('loc_259D')

    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '有聚餐用的大桌子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '桌子下没有任何人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    TalkEnd(0x00FF)

    def _loc_25F9(): pass

    label('loc_25F9')

    Return()

# id: 0x0012 offset: 0x25FA
@scena.Code('func_12_25FA')
def func_12_25FA():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2618',
    )

    Call(0, 0x0020)
    Call(0, 0x0021)
    FadeIn(0, 0)

    def _loc_2618(): pass

    label('loc_2618')

    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '有聚餐用的大桌子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_29EB',
    )

    EventBegin(0x00)
    FadeOut(1000, 0, -1)
    OP_0D()
    ChrSetPos(0x0101, -17710, 0, 44750, 360)
    ChrSetPos(0x0104, -17930, 0, 43630, 360)
    ChrSetPos(0x00F7, -19230, 0, 43930, 45)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_26C9',
    )

    ChrSetPos(0x0105, -16800, 0, 43480, 360)

    Jump('loc_270A')

    def _loc_26C9(): pass

    label('loc_26C9')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_26EB',
    )

    ChrSetPos(0x0107, -16800, 0, 43480, 360)

    Jump('loc_270A')

    def _loc_26EB(): pass

    label('loc_26EB')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_270A',
    )

    ChrSetPos(0x0108, -16800, 0, 43480, 360)

    def _loc_270A(): pass

    label('loc_270A')

    CameraMove(-17730, 0, 44700, 0)
    OP_67(0, 6660, -10000, 0)
    CameraSetDistance(1380, 0)
    OP_6C(40000, 0)
    OP_6E(504, 0)
    Sleep(500)

    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010240795V#1004F难不成，藏在\n',
            '这下面……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    ChrSetChipByIndex(0x0101, 2)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010240796V#1015F……………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240797V#1016F哈哈……\n',
            '果然不在呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040240798V#032F咳咳，这个且不说……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040240799V现在你的服装\n',
            '还是不要随便蹲下比较好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240800V#1004F哎？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040240801V#031F怎么说呢……快看到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrJumpToRelative(0x0101, 0, 0, 0, 800, 12000)
    ChrSetChipByIndex(0x0101, 65535)
    Sleep(500)

    ChrTurnDirection(0x0101, 0x0104, 600)

    ChrTalk(
        0x0101,
        (
            '#0010240802V#1019F～～～呜～～～～',
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
        'loc_2972',
    )

    ChrTalk(
        0x0106,
        (
            '#0050240803V#552F刚才是你不对。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050240804V穿的不是紧身裤\n',
            '稍微注意点吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_29BE')

    def _loc_2972(): pass

    label('loc_2972')

    ChrTalk(
        0x0103,
        (
            '#0030240805V#524F刚才是你不对。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030240806V穿的是裙子\n',
            '请稍微当心点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_29BE(): pass

    label('loc_29BE')

    ChrTalk(
        0x0101,
        (
            '#0010240807V#1013F呜呜……知道了啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2CB5')

    def _loc_29EB(): pass

    label('loc_29EB')

    EventBegin(0x00)
    FadeOut(1000, 0, -1)
    OP_0D()
    ChrSetPos(0x0101, -17710, 0, 44750, 360)
    ChrSetPos(0x00F7, -17930, 0, 43630, 360)
    ChrSetPos(0x00F8, -19230, 0, 43930, 45)
    ChrSetPos(0x00F9, -16800, 0, 43480, 360)
    CameraMove(-17730, 0, 44700, 0)
    OP_67(0, 6660, -10000, 0)
    CameraSetDistance(1380, 0)
    OP_6C(40000, 0)
    OP_6E(504, 0)
    Sleep(500)

    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010240795V#1004F难不成，藏在\n',
            '这下面……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    ChrSetChipByIndex(0x0101, 2)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010240796V#1015F……………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240797V#1016F哈哈……\n',
            '果然不在呢。',
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
        'loc_2B86',
    )

    ChrTalk(
        0x0106,
        (
            '#0050240811V#551F喂喂、艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050240812V穿的不是紧身裤,\n',
            '别那么随便就蹲下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2BDE')

    def _loc_2B86(): pass

    label('loc_2B86')

    ChrTalk(
        0x0103,
        (
            '#0030240813V#025F我说艾丝蒂尔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030240814V穿的不是紧身裤\n',
            '别那么随便就蹲下啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2BDE(): pass

    label('loc_2BDE')

    ChrTalk(
        0x0101,
        (
            '#0010240815V#1013F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrJumpToRelative(0x0101, 0, 0, 0, 800, 12000)
    ChrSetChipByIndex(0x0101, 65535)
    Sleep(500)

    ChrTurnDirection(0x0101, 0x00F7, 400)

    ChrTalk(
        0x0101,
        (
            '#0010240816V#1008F嘿嘿、不好意思。',
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
        'loc_2C90',
    )

    ChrTalk(
        0x0106,
        (
            '#0050240817V#552F真是的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2CB5')

    def _loc_2C90(): pass

    label('loc_2C90')

    ChrTalk(
        0x0103,
        (
            '#0030240818V#524F唉，真是的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2CB5(): pass

    label('loc_2CB5')

    SetScenaFlags(ScenaFlag(0x02C1, 6, 0x160E))
    OP_28(0x0089, 0x01, 0x0008)
    FadeOut(500, 0, -1)
    OP_0D()
    CameraMove(-17930, 0, 43830, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0000, -17930, 0, 43830, 180)
    ChrSetPos(0x0001, -17930, 0, 43830, 180)
    ChrSetPos(0x0002, -17930, 0, 43830, 180)
    ChrSetPos(0x0003, -17930, 0, 43830, 180)
    Sleep(500)

    FadeIn(500, 0)
    EventEnd(0x00)

    Return()

# id: 0x0013 offset: 0x2D5B
@scena.Code('func_13_2D5B')
def func_13_2D5B():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 7, 0x160F)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2F0C',
    )

    EventBegin(0x01)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '有大个的绯红色的壶。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x0101,
        (
            '#0010240819V#1006F解放离宫的时候，这个下面\n',
            '贴着备用钥匙吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240820V这壶相当大\n',
            '说不定藏在里面……',
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
        'loc_2E81',
    )

    ChrTalk(
        0x0106,
        (
            '#0050240821V#053F到底是不可能啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050240822V#555F第一、那么小的口\n',
            '怎么进去嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2ED6')

    def _loc_2E81(): pass

    label('loc_2E81')

    ChrTalk(
        0x0103,
        (
            '#0030240823V#025F怎么可能嘛……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030240824V#524F首先，那么小的口\n',
            '怎么进得去？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2ED6(): pass

    label('loc_2ED6')

    ChrTalk(
        0x0101,
        (
            '#0010240825V#1008F嘿嘿、这倒也是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x02C1, 7, 0x160F))
    OP_28(0x0089, 0x01, 0x0010)
    EventEnd(0x01)

    Jump('loc_2F52')

    def _loc_2F0C(): pass

    label('loc_2F0C')

    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '有大个的绯红色的壶。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    TalkEnd(0x00FF)
    def _loc_2F52(): pass

    label('loc_2F52')

    Return()

# id: 0x0014 offset: 0x2F53
@scena.Code('func_14_2F53')
def func_14_2F53():
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
        'loc_2F6A',
    )

    Call(0, 0x0020)
    Call(0, 0x0021)

    def _loc_2F6A(): pass

    label('loc_2F6A')

    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x00F7, 0x0080)
    ChrSetFlags(0x00F8, 0x0080)
    ChrSetFlags(0x00F9, 0x0080)
    ChrSetPos(0x0009, -15000, 0, -43330, 180)
    OP_4A(0x0009, 255)
    OP_67(0, 6640, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_69(0x0009, 0)
    FadeIn(2000, 0)
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    CreateThread(0x0009, 0x01, 0x00, func_15_4B2A)
    OP_0D()
    Sleep(1000)

    OP_4A(0x0009, 1)

    ChrTalk(
        0x0009,
        (
            '#0640240837V#222F好慢！太慢了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640240838V菲利普这家伙……\n',
            '买杂志和炸面圈\n',
            '得花多少时间啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4B(0x0009, 1)
    ClearScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    OP_A6(0x0001)
    OP_62(0x0009, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_3D29',
    )

    @scena.Lambda('lambda_307A')
    def lambda_307A():
        CameraMove(-14340, 0, -44170, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_307A)

    CreateThread(0x0101, 0x01, 0x00, func_16_4B79)
    CreateThread(0x00F7, 0x01, 0x00, func_17_4BD5)
    CreateThread(0x00F8, 0x01, 0x00, func_18_4C36)
    CreateThread(0x00F9, 0x01, 0x00, func_19_4C97)
    ChrSetDirection(0x0009, 180, 400)
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#0640240839V#224F#5P喂、菲利普！\n',
            '要我等多久才……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010240840V#1004F#6P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0640240841V#223F#5P你、你、你……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#0640240842V#226F#3S#5P你们是～！？',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_31D6',
    )

    ChrTalk(
        0x0106,
        (
            '#0050240843V#555F#2P怎么？\n',
            '这个奇怪的大叔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3219')

    def _loc_31D6(): pass

    label('loc_31D6')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3219',
    )

    ChrTalk(
        0x0103,
        (
            '#0030240844V#023F#2P哎呀……\n',
            '记得那时在城里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3219(): pass

    label('loc_3219')

    ChrTalk(
        0x0101,
        (
            '#0010240845V#1025F#6P杜南公爵……\n',
            '在这种地方啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240846V#1016F嗯，还好吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0640240847V#222F#5P哎、装模作样！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640240848V都是因为你们,\n',
            '都是因为你们……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640240849V#224F我要被迫在这里\n',
            '过软禁生活！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240850V#1007F#6P嗯～就算你说\n',
            '是因为我们……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240851V但上了理查德上校的套,\n',
            '算是公爵先生自作自受吧。',
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
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_33FB',
    )

    ChrTalk(
        0x0108,
        (
            '#0080240852V#070F不过，只被软禁\n',
            '应该算好运了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040240853V#035F呼，这要是在埃雷波尼亚\n',
            '就算是皇族也要处以极刑啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_350C')

    def _loc_33FB(): pass

    label('loc_33FB')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3480',
    )

    ChrTalk(
        0x0108,
        (
            '#0080240854V#074F不过，只被软禁\n',
            '应该算好运了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080240855V#070F要是在其他国家，就算是王族\n',
            '也免不了要服刑吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_350C')

    def _loc_3480(): pass

    label('loc_3480')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_350C',
    )

    ChrTalk(
        0x0104,
        (
            '#0040240856V#035F呼，身为利贝尔王族\n',
            '你应该谢天谢地才是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040240857V#030F这要是在埃雷波尼亚\n',
            '就算是皇族也要处以极刑啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_350C(): pass

    label('loc_350C')

    ChrTalk(
        0x0009,
        (
            '#0640240858V#226F#5P呜……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640240859V#222F哼、哼……\n',
            '的确幽禁陛下\n',
            '是过分了点，这我承认。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640240860V虽然是被理查德教唆,\n',
            '但这个还是不应该的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240861V#1006F#6P咦，相当微妙的台词嘛？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0640240862V#225F#5P哼，别误会。\n',
            '我也很敬爱陛下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640240863V无论作为君主还是姑母大人\n',
            '都是无可挑剔的人物。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640240864V#224F但是，要指明科洛蒂娅那小丫头\n',
            '当下任国王\n',
            '我无论如何也不能接受！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240865V#1009F#6P喂……\n',
            '我可听不下去了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240866V科洛丝头脑好又肯用功\n',
            '也有服众的气量。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240867V被公爵先生称做小丫头\n',
            '这太没道理了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0640240868V#220F#5P哼，我说的\n',
            '可不是这些。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640240869V诚然，确实像陛下说的那样\n',
            '那女孩是有才能。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640240870V但是，到底科洛蒂娅\n',
            '真的有成为女王的精神准备吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200268V#1026F#6P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0640240872V#220F#5P一直以来都是这样，\n',
            '她不太愿意在公务场合出面。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640240873V如果以知名度来说，我\n',
            '更加为国民所知吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640240874V也就是说，那女孩是没有\n',
            '立于人上的觉悟不是吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240875V#1003F#6P这，这个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0640240876V#222F#5P听说那女孩，隐藏身份\n',
            '过着学生生活。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640240877V还在孤儿院什么的\n',
            '长期逗留不是吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640240878V#225F比起那些，出席公共事务\n',
            '广为人知……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640240879V#224F这才是王族的义务吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240880V#1002F#6P…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240881V#1007F我对王族的义务什么的\n',
            '完全不清楚……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240882V说不定公爵先生的话\n',
            '也有一番道理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0640240883V#221F#5P哇哈哈，当然了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240884V#1002F#6P但是，我只对你这么说。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240885V科洛丝现在，虽然烦恼\n',
            '却也在努力寻找答案。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240886V#1005F至少、比以软禁为借口\n',
            '什么都不做的公爵先生强！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0640240887V#226F#5P什、什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240888V#1006F#6P科洛丝有没有女王的资格\n',
            '要做判断\n',
            '也等看了那个答案之后吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240889V大概，公爵先生\n',
            '也能理解吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0640240858V#226F#5P唔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640240891V#222F哼、哼，白痴一样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640240892V#224F哎、真不爽！\n',
            '赶快从房间出去！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240893V#1005F#6P还用你说！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240894V#1007F……啊，在这之前。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240895V#1015F这里有没有个穿白衣服的\n',
            '女孩子来过？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0640240896V#222F#5P那是什么……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640240897V#224F我一直待在这里！\n',
            '没看到那样的小丫头！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240898V#1019F#6P啊是吗，打扰了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4B08')

    def _loc_3D29(): pass

    label('loc_3D29')

    @scena.Lambda('lambda_3D2F')
    def lambda_3D2F():
        CameraMove(-14340, 0, -44170, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_3D2F)

    CreateThread(0x0101, 0x01, 0x00, func_16_4B79)
    CreateThread(0x0105, 0x01, 0x00, func_17_4BD5)
    CreateThread(0x00F7, 0x01, 0x00, func_18_4C36)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3D6E',
    )

    CreateThread(0x0104, 0x01, 0x00, func_19_4C97)

    Jump('loc_3D9B')

    def _loc_3D6E(): pass

    label('loc_3D6E')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3D86',
    )

    CreateThread(0x0107, 0x01, 0x00, func_19_4C97)

    Jump('loc_3D9B')

    def _loc_3D86(): pass

    label('loc_3D86')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3D9B',
    )

    CreateThread(0x0108, 0x01, 0x00, func_19_4C97)

    def _loc_3D9B(): pass

    label('loc_3D9B')

    ChrSetDirection(0x0009, 180, 400)
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#0640240839V#224F#5P喂、菲利普！\n',
            '要我等多久才……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010240900V#1004F#6P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0105, 0x0001)

    ChrTalk(
        0x0105,
        (
            '#0060240901V#043F#2P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0640240841V#223F#5P你、你、你……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#0640240842V#226F#3S#5P你们是～！？',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3EEE',
    )

    ChrTalk(
        0x0106,
        (
            '#0050240904V#555F#6P怎么？\n',
            '这个奇怪的大叔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3F33')

    def _loc_3EEE(): pass

    label('loc_3EEE')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3F33',
    )

    ChrTalk(
        0x0103,
        (
            '#0030240905V#023F#6P哎呀……\n',
            '记得那时在城里来着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3F33(): pass

    label('loc_3F33')

    ChrTalk(
        0x0101,
        (
            '#0010240906V#1019F#6P杜南公爵……\n',
            '在这种地方啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060240907V#542F#2P王叔……\n',
            '那个，还好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0640240847V#222F#5P哎、装模作样！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640240848V都是因为你们,\n',
            '都是因为你们……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640240849V#224F我要被迫在这里\n',
            '过软禁生活！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240850V#1007F#6P嗯～就算你说\n',
            '是因为我们……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240851V但上了理查德上校的套\n',
            '是公爵先生自作自受吧。',
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
        'loc_4113',
    )

    ChrTalk(
        0x0108,
        (
            '#0080240913V#074F#2P不过，只被软禁\n',
            '应该算好运了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080240855V#070F要是在其他国家，就算是王族\n',
            '也免不了要服刑吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_41A2')

    def _loc_4113(): pass

    label('loc_4113')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_41A2',
    )

    ChrTalk(
        0x0104,
        (
            '#0040240915V#035F#2P呼，身为利贝尔王族\n',
            '你应该谢天谢地才是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040240857V#030F这要是在埃雷波尼亚\n',
            '就算是皇族也要处以极刑啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_41A2(): pass

    label('loc_41A2')

    ChrTalk(
        0x0009,
        (
            '#0640240858V#226F#5P呜……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640240859V#222F哼、哼……\n',
            '的确幽禁陛下\n',
            '是过分了点，这我承认。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640240860V虽然是被理查德教唆,\n',
            '但这个还是不应该的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240861V#1006F#6P咦，相当微妙的台词嘛？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0640240862V#225F#5P哼，别误会。\n',
            '我也很敬爱陛下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640240863V无论作为君主还是姑母大人\n',
            '都是无可挑剔的人物。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640240923V#224F但是，科洛蒂娅！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640240924V像你这种小丫头\n',
            '当下任国王\n',
            '我无论如何也不能接受！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060240925V#049F#2P………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240926V#1005F#6P慢、慢着！\n',
            '我可听不下去了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240927V科洛丝头脑好又肯用功\n',
            '也有服众的气量！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240928V被公爵先生称做小丫头\n',
            '有什么理由……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060240929V#047F#2P……艾丝蒂尔，不必说了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060240930V#043F以前也说过，我……\n',
            '还没有继承王位的精神准备。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060240931V会让王叔感到不快\n',
            '也是理所当然的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010211091V#1026F#6P科洛丝……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0640240933V#220F#5P嗯，说得真微妙。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640240934V一直以来都是这样，\n',
            '不太愿意在公务场合出面。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640240873V如果以知名度来说，我\n',
            '更加为国民所知吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640240936V这也就是，你没有立于人上\n',
            '的精神准备。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060240937V#043F#2P…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0640240938V#222F#5P听说你隐藏身份\n',
            '过着学生生活。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640240877V还在孤儿院什么的\n',
            '长期逗留不是吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640240878V#225F比起那些，出席公共事务\n',
            '并广为人知……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640240879V#224F这才是王族的义务吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060240942V#049F#2P……那是………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240880V#1002F#6P…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240881V#1007F我对王族的义务什么的\n',
            '完全不清楚……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240882V说不定公爵先生的话\n',
            '也有一番道理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0640240883V#221F#5P哇哈哈，当然了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240884V#1002F#6P但是，我只对你这么说。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240885V科洛丝现在，虽然烦恼\n',
            '却也在努力寻找答案。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240949V#1005F至少、比以软禁为借口\n',
            '什么都不做的公爵先生强！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0640240887V#226F#5P什、什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060240951V#049F#2P艾丝蒂尔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060240952V#043F……那个，杜南王叔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060240953V我现在，正借助\n',
            '艾丝蒂尔的力量\n',
            '在寻找自己的道路。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060240954V#047F我当女王的资格\n',
            '到底有还是没有……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060240955V不久的将来，希望也能\n',
            '让王叔看到答案。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060240956V#042F所以在这之前……\n',
            '能请您耐心等待吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0640240858V#226F#5P唔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640240891V#222F哼、哼，白痴一样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640240892V#224F哎、真不爽！\n',
            '赶快从房间出去！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240893V#1005F#6P还用你说！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240894V#1007F……啊，在这之前。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240895V#1015F这里有没有个穿白衣服的\n',
            '女孩子来过？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0640240896V#222F#5P那是什么……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640240897V#224F我一直待在这里！\n',
            '没看到那样的小丫头！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240898V#1019F#6P啊是吗，打扰了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060240966V#047F……失陪了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_4B08(): pass

    label('loc_4B08')

    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(500)

    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    SetScenaFlags(ScenaFlag(0x02C2, 2, 0x1612))
    NewScene('ED6_DT21/T4303._SN', 100, 0, 0)
    IdleLoop()
    EventEnd(0x00)

    Return()

# id: 0x0015 offset: 0x4B2A
@scena.Code('func_15_4B2A')
def func_15_4B2A():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_4B5C',
    )

    ChrWalkTo(0x00FE, -14000, 0, -43330, 2000, 0x00)
    ChrWalkTo(0x00FE, -16000, 0, -43330, 2000, 0x00)

    Jump('func_15_4B2A')

    def _loc_4B5C(): pass

    label('loc_4B5C')

    PlaySE(6, 0x00, 0x64)
    ChrWalkTo(0x00FE, -15000, 0, -43330, 2000, 0x00)
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Return()

# id: 0x0016 offset: 0x4B79
@scena.Code('func_16_4B79')
def func_16_4B79():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetPos(0x00FE, -14130, 0, -49500, 180)
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)

    @scena.Lambda('lambda_4BA0')
    def lambda_4BA0():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_4BA0)

    ChrWalkTo(0x00FE, -14100, 0, -48520, 2500, 0x00)
    ChrMoveTo(0x00FE, -14530, 0, -45570, 2500, 0x00)

    Return()

# id: 0x0017 offset: 0x4BD5
@scena.Code('func_17_4BD5')
def func_17_4BD5():
    Sleep(500)

    ChrClearFlags(0x00FE, 0x0080)
    ChrSetPos(0x00FE, -14130, 0, -49500, 180)
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)

    @scena.Lambda('lambda_4C01')
    def lambda_4C01():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_4C01)

    ChrWalkTo(0x00FE, -14100, 0, -48520, 2500, 0x00)
    ChrMoveTo(0x00FE, -13690, 0, -46100, 2500, 0x00)

    Return()

# id: 0x0018 offset: 0x4C36
@scena.Code('func_18_4C36')
def func_18_4C36():
    Sleep(1000)

    ChrClearFlags(0x00FE, 0x0080)
    ChrSetPos(0x00FE, -14130, 0, -49500, 180)
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)

    @scena.Lambda('lambda_4C62')
    def lambda_4C62():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_4C62)

    ChrWalkTo(0x00FE, -14100, 0, -48520, 2500, 0x00)
    ChrMoveTo(0x00FE, -15270, 0, -46840, 2500, 0x00)

    Return()

# id: 0x0019 offset: 0x4C97
@scena.Code('func_19_4C97')
def func_19_4C97():
    Sleep(1500)

    ChrClearFlags(0x00FE, 0x0080)
    ChrSetPos(0x00FE, -14130, 0, -49500, 180)
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)

    @scena.Lambda('lambda_4CC3')
    def lambda_4CC3():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_4CC3)

    ChrWalkTo(0x00FE, -14260, 0, -47410, 2500, 0x00)

    Return()

# id: 0x001A offset: 0x4CE4
@scena.Code('func_1A_4CE4')
def func_1A_4CE4():
    EventBegin(0x00)
    Fade(1000)
    OP_4A(0x0009, 255)
    ChrSetDirection(0x0009, 180, 0)
    ChrSetPos(0x012F, -16400, 0, -39920, 0)
    ChrSetPos(0x0101, -15400, 0, -39750, 0)
    ChrSetPos(0x00F7, -15710, 0, -41000, 0)
    ChrSetPos(0x00F8, -16850, 0, -41250, 0)
    ChrSetPos(0x00F9, -14720, 0, -41100, 0)
    CameraMove(-15710, 0, -39150, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(
        0x0009,
        (
            '#0640241166V#222F#5P……怎么，还在啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x012F,
        (
            '#0220241167V#264F盯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0640241168V#223F#5P怎、怎么了你？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x012F,
        (
            '#0220241169V#260F对了，姐姐。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220241170V这位大叔\n',
            '怎么梳个这么有趣的发型？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0640241171V#226F#5P你、你说什么～！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010241172V#1016F#4P哎，算了算了。\n',
            '小孩子嘛……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010241173V#1006F顺带一提，这位大叔\n',
            '搞笑的不只是发型。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010241174V服装和性格也很有趣哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x012F,
        (
            '#0220241175V#261F哈哈哈，这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0640241176V#226F#5P这算是\n',
            '帮我吗～！！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640241025V#224F哎，带着这小丫头\n',
            '赶快从这房间里出去！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0009, 0, 400)
    OP_4B(0x0009, 255)
    SetScenaFlags(ScenaFlag(0x02C2, 3, 0x1613))
    EventEnd(0x00)

    Return()

# id: 0x001B offset: 0x4FA8
@scena.Code('func_1B_4FA8')
def func_1B_4FA8():
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
        'loc_4FC8',
    )

    Call(0, 0x0020)
    Call(0, 0x0021)
    FadeIn(0, 0)

    def _loc_4FC8(): pass

    label('loc_4FC8')

    Fade(1000)
    OP_4A(0x0008, 255)
    ChrSetPos(0x0101, -13290, 0, 18890, 45)
    ChrSetPos(0x00F7, -12530, 0, 18230, 0)
    ChrSetPos(0x00F8, -13740, 0, 17710, 45)
    ChrSetPos(0x00F9, -14560, 0, 18430, 45)
    CameraMove(-12740, 0, 19290, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02D0, 2, 0x1682)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_530F',
    )

    ChrTalk(
        0x0008,
        (
            '#2330241028V怎样，找到了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010241029V#1007F没有，很遗憾。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010241030V看起来可疑的地方\n',
            '都调查了一遍倒是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2330241031V难、难道说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2330241032V出去艾尔贝离宫外边\n',
            '的可能性……',
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
        'loc_5166',
    )

    ChrTalk(
        0x0106,
        (
            '#0050241033V#552F可恶……\n',
            '那可就麻烦了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_519A')

    def _loc_5166(): pass

    label('loc_5166')

    ChrTalk(
        0x0103,
        (
            '#0030241034V#522F嗯……\n',
            '如果是那样就麻烦了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_519A(): pass

    label('loc_519A')

    ChrTalk(
        0x0101,
        (
            '#0010241035V#1015F嗯～只不过是躲猫猫\n',
            '我想不会的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010241036V藏在一般能去的地方\n',
            '是规则嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010241037V#1006F大概，藏在意想不到的地方\n',
            '的可能性会比较高。',
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
        'loc_52A6',
    )

    ChrTalk(
        0x0106,
        (
            '#0050241038V#051F原来如此，偶尔\n',
            '你也会说点敏锐的话嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050241039V再稍微找找看？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5309')

    def _loc_52A6(): pass

    label('loc_52A6')

    ChrTalk(
        0x0103,
        (
            '#0030241042V#021F呵呵，不愧是艾丝蒂尔。\n',
            '对玩耍的事很敏锐呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030241043V#020F再稍微找找看？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5309(): pass

    label('loc_5309')

    SetScenaFlags(ScenaFlag(0x02D0, 2, 0x1682))

    Jump('loc_53B8')

    def _loc_530F(): pass

    label('loc_530F')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_536B',
    )

    ChrTalk(
        0x0106,
        (
            '#0050241040V#052F怎么办、艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050241041V还是在离宫里找找看？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_53B8')

    def _loc_536B(): pass

    label('loc_536B')

    ChrTalk(
        0x0103,
        (
            '#0030241044V#023F怎么办呢、艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030241045V还是在离宫里找找看？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_53B8(): pass

    label('loc_53B8')

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
            TXT(0x00, '【再稍微找找】\n'),
            TXT(0x01, '【死心考虑别的办法】\n'),
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
        (0x00000000, 'loc_5423'),
        (0x00000001, 'loc_5459'),
        (-1, 'loc_5AA4'),
    )

    def _loc_5423(): pass

    label('loc_5423')

    ChrTalk(
        0x0101,
        (
            '#0010241046V#1006F嗯，稍微改变想法\n',
            '找找看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5AA4')

    def _loc_5459(): pass

    label('loc_5459')

    ChrTalk(
        0x0101,
        (
            '#0010241047V#1007F嗯～既然陷入瓶颈\n',
            '最好是坦率地投降吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2330241048V投降就是说？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010241049V#1015F嗯，躲猫猫时\n',
            '要是鬼投降了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010241050V#1006F鬼哭着输～了！\n',
            '躲猫猫完～了！这样\n',
            '一边说一边到处转转就行了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010241051V要是那样的话，那个女孩子也\n',
            '一定会出来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2330241052V原，原来如此……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_55F6',
    )

    ChrTalk(
        0x0107,
        (
            '#0070241053V#067F嘿嘿，有点\n',
            '难为情啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070241054V为了请她出来\n',
            '没办法了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_56B9')

    def _loc_55F6(): pass

    label('loc_55F6')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_565A',
    )

    ChrTalk(
        0x0105,
        (
            '#0060241055V#045F呵呵，有点\n',
            '难为情啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060241056V为了请她出来\n',
            '没办法了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_56B9')

    def _loc_565A(): pass

    label('loc_565A')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_56B9',
    )

    ChrTalk(
        0x0104,
        (
            '#0040241057V#035F呼，稍微有点\n',
            '难为情啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040241058V#037F我就开心地说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_56B9(): pass

    label('loc_56B9')

    ChrTalk(
        0x0101,
        (
            '#0010241059V#1006F那么各位、\n',
            '练习说一次看看吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010241060V#1018F鬼哭着输～了！\n',
            '躲猫猫完～了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    SetMessageWindowPos(-1, 160, -1, -1)
    TalkSetChrName('全员')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0040241061V#3S鬼哭着输～了！\n',
            '躲猫猫完～了！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    ChrSetFlags(0x000A, 0x0004)
    ChrSetPos(0x000A, -10290, -500, 19160, 0)

    NpcTalk(
        0x000A,
        '声音',
        (
            '#0220241062V#5P喵呜⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x00F7, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_57FD',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x18, 0x1B, 0x000000FA, 0x00)

    Jump('loc_5831')

    def _loc_57FD(): pass

    label('loc_57FD')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_581F',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x18, 0x1B, 0x000000FA, 0x00)

    Jump('loc_5831')

    def _loc_581F(): pass

    label('loc_581F')

    OP_62(0x00F8, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)

    def _loc_5831(): pass

    label('loc_5831')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5853',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x18, 0x1B, 0x000000FA, 0x00)

    Jump('loc_5887')

    def _loc_5853(): pass

    label('loc_5853')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5875',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x18, 0x1B, 0x000000FA, 0x00)

    Jump('loc_5887')

    def _loc_5875(): pass

    label('loc_5875')

    OP_62(0x00F9, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)

    def _loc_5887(): pass

    label('loc_5887')

    OP_62(0x0008, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1500)

    OP_63(0x0101)
    OP_63(0x00F7)
    OP_63(0x00F8)
    OP_63(0x00F9)
    OP_63(0x0008)

    @scena.Lambda('lambda_58B3')
    def lambda_58B3():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_58B3)

    Sleep(50)

    @scena.Lambda('lambda_58C6')
    def lambda_58C6():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_58C6)

    Sleep(50)

    @scena.Lambda('lambda_58D9')
    def lambda_58D9():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_58D9)

    Sleep(50)

    @scena.Lambda('lambda_58EC')
    def lambda_58EC():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_58EC)

    Sleep(50)

    @scena.Lambda('lambda_58FF')
    def lambda_58FF():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_58FF)

    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010241063V#1008F刚，刚才的声音是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2330241064V难道…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000A,
        '声音',
        (
            '#0220241065V#5P嘻嘻，玲赢了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_5980')
    def lambda_5980():
        ChrTurnDirection(0x00FE, 0x000A, 400)
        Yield()

        Jump('lambda_5980')

    DispatchAsync2(0x0008, 0x0001, lambda_5980)

    @scena.Lambda('lambda_5991')
    def lambda_5991():
        CameraMove(-11020, 0, 19860, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_5991)

    ChrClearFlags(0x000A, 0x0080)
    ChrWalkTo(0x000A, -9890, 0, 20380, 1000, 0x00)
    TerminateThread(0x0008, 0x01)
    ChrSetDirection(0x000A, 225, 400)
    WaitForThreadExit(0x0101, 0x0002)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010241066V#1004F#6P啊～！？\n',
            '在艾尔·雷登遇见的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0220241067V#5P#261F哈哈哈……\n',
            '姐姐，好久不见呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220241068V还记得玲的事\n',
            '玲好高兴。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    ChrSetFlags(0x000A, 0x0080)
    SetScenaFlags(ScenaFlag(0x02C2, 5, 0x1615))
    OP_28(0x0089, 0x01, 0x0800)
    OP_28(0x0089, 0x01, 0x1000)
    Call(0, 0x001D)

    Jump('loc_5AA4')

    def _loc_5AA4(): pass

    label('loc_5AA4')

    OP_4B(0x0008, 255)
    EventEnd(0x00)

    Return()

# id: 0x001C offset: 0x5AAB
@scena.Code('func_1C_5AAB')
def func_1C_5AAB():
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
        'loc_5ACB',
    )

    Call(0, 0x0020)
    Call(0, 0x0021)
    FadeIn(0, 0)

    def _loc_5ACB(): pass

    label('loc_5ACB')

    Fade(1000)
    ChrSetPos(0x0101, -9950, 0, 20590, 180)
    ChrSetPos(0x00F7, -12280, 0, 18190, 45)
    ChrSetPos(0x00F8, -10910, 0, 18200, 0)
    ChrSetPos(0x00F9, -9550, 0, 18200, 0)
    CameraMove(-10150, 0, 20240, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)

    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔为慎重起见\n',
            '查看了一下柜台底下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    Fade(250)
    ChrSetFlags(0x0101, 0x0002)
    ChrSetChipByIndex(0x0101, 2)
    ChrSetSubChip(0x0101, 5)
    OP_0D()
    Sleep(500)

    OP_62(0x0101, 0x000000C8, 1400, 0x02, 0x07, 0x00000050, 0x01)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010241069V#1004F咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4A(0x0008, 255)
    ChrTurnDirection(0x0008, 0x0101, 400)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#2330241070V？？？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2330241071V怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010210165V#1016F啊哈哈……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010241073V没什么怎么了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x000A, 0x0004)
    ChrSetPos(0x000A, -10290, -500, 19160, 0)

    NpcTalk(
        0x000A,
        '声音',
        (
            '#0220241074V#5P呜喵～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000A,
        '声音',
        (
            '#0220241075V#5P啊～啊，玲输了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00F7, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5D22',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_5D60')

    def _loc_5D22(): pass

    label('loc_5D22')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5D49',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_5D60')

    def _loc_5D49(): pass

    label('loc_5D49')

    OP_62(0x00F8, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_5D60(): pass

    label('loc_5D60')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5D87',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_5DC5')

    def _loc_5D87(): pass

    label('loc_5D87')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5DAE',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_5DC5')

    def _loc_5DAE(): pass

    label('loc_5DAE')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_5DC5(): pass

    label('loc_5DC5')

    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    Fade(250)
    ChrClearFlags(0x0101, 0x0002)
    ChrSetSubChip(0x0101, 0)
    ChrSetChipByIndex(0x0101, 65535)
    OP_0D()
    Sleep(250)

    @scena.Lambda('lambda_5E01')
    def lambda_5E01():
        CameraMove(-10460, 0, 20440, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_5E01)

    ChrMoveTo(0x0101, -10110, 0, 21330, 1000, 0x00)
    ChrClearFlags(0x000A, 0x0080)
    ChrWalkTo(0x000A, -9890, 0, 20380, 1000, 0x00)
    TerminateThread(0x0008, 0x01)
    ChrSetDirection(0x000A, 225, 400)
    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0008,
        (
            '#2330241076V咦咦！？',
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
        'loc_5EBA',
    )

    ChrTalk(
        0x0106,
        (
            '#0050241077V#052F#6P难不成……\n',
            '是在艾尔·雷登遇见的……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5EF9')

    def _loc_5EBA(): pass

    label('loc_5EBA')

    ChrTalk(
        0x0103,
        (
            '#0030241078V#023F#6P难不成……\n',
            '是在艾尔·雷登遇见的孩子？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5EF9(): pass

    label('loc_5EF9')

    ChrTalk(
        0x0101,
        (
            '#0010241079V#1017F#5P呵呵，果然\n',
            '是玲啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0101, 400)
    Sleep(500)

    ChrTalk(
        0x000A,
        (
            '#0220241080V#261F#4P哈哈哈……\n',
            '姐姐，好久不见呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220241068V还记得玲的事\n',
            '玲好高兴。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    ChrSetFlags(0x000A, 0x0080)
    SetScenaFlags(ScenaFlag(0x02C2, 6, 0x1616))
    OP_28(0x0089, 0x01, 0x0080)
    OP_28(0x0089, 0x01, 0x0100)
    Call(0, 0x001D)

    Return()

# id: 0x001D offset: 0x5FB3
@scena.Code('func_1D_5FB3')
def func_1D_5FB3():
    EventBegin(0x00)
    FormationAddMember(ChrTable['玲'], 0xFF, 0xFF)
    ChrSetPos(0x0101, -13340, 0, 18690, 90)
    ChrSetPos(0x00F7, -13560, 0, 17570, 90)
    ChrSetPos(0x00F8, -14890, 0, 17470, 90)
    ChrSetPos(0x00F9, -14630, 0, 18640, 90)
    ChrSetPos(0x012F, -11980, 0, 18170, 270)
    ChrTurnDirection(0x0008, 0x0101, 0)
    CameraMove(-12300, 0, 19340, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(500)

    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#2330241082V#5P呀～没想到\n',
            '你们认识啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x012F, 400)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#2330241083V#5P嗯，你……\n',
            '叫玲对吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x012F, 0, 400)

    ChrTalk(
        0x012F,
        (
            '#0220241084V#260F嗯嗯，是啊。\n',
            '玲就是叫玲。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220241085V#261F对不起，请保密。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2330241086V#5P哈哈，我不介意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2330241087V#5P但是为什么突然\n',
            '玩起躲猫猫来了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x012F,
        (
            '#0220241088V#263F因为，听说\n',
            '姐姐来了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220241089V我想跟你一起玩,\n',
            '就努力藏起来了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010241090V#1016F啊哈哈，这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010241091V#1006F不过，你居然\n',
            '知道我们会来呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x012F, 270, 400)

    ChrTalk(
        0x012F,
        (
            '#0220241092V#264F#2P因为姐姐\n',
            '是游击士吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220241093V玲听说\n',
            '游击士来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010241094V#1025F嗯，话是没错……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010241095V但是游击士又不只我一个，\n',
            '说不定是其他的人来了哦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x012F,
        (
            '#0220241096V#260F#2P但是，玲相信的。\n',
            '来的是姐姐。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220241097V#261F作为证据，你看，\n',
            '是来了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010241098V#1016F唔、嗯……确实。',
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
        'loc_6599',
    )

    ChrTalk(
        0x0106,
        (
            '#0050241099V#053F#6P嗯，这个暂且不提……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050241100V#050F你爸爸妈妈\n',
            '到底去哪里了？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050241101V怎么在这种地方\n',
            '一个人玩？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x012F,
        (
            '#0220241102V#262F#2P盯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050241103V#055F#6P什、什么啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x012F,
        (
            '#0220241104V#268F#2P大哥哥，你不行啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220241105V好像完全不懂得\n',
            '怎么跟淑女说话嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050241106V#057F#6P我怒……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_650F',
    )

    ChrTalk(
        0x0107,
        (
            '#0070241107V#067F#6P阿、阿加特哥哥。\n',
            '你先忍忍……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_650F(): pass

    label('loc_650F')

    ChrTalk(
        0x012F,
        (
            '#0220241108V#263F#2P不过，玲是淑女\n',
            '就以宽大之心原谅你吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220241109V#260F那，爸爸妈妈\n',
            '去了哪里……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220241110V玲也不太清楚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6857')

    def _loc_6599(): pass

    label('loc_6599')

    ChrTalk(
        0x0103,
        (
            '#0030241111V#020F#6P嗯，这个暂且不提……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030241112V你的爸爸和妈妈\n',
            '到底去了哪里呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030241113V怎么在这种地方\n',
            '让玲一个人玩？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x012F,
        (
            '#0220241114V#264F#2P哇，仔细一看姐姐\n',
            '的衣服真有趣呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220241115V那样露出肚脐\n',
            '不会感冒吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030241116V#021F#6P嗯，习惯了嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030241117V#023F唔，不说这个了,\n',
            '玲的爸爸和妈妈……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x012F,
        (
            '#0220241118V#265F#2P不过，看那肤色\n',
            '是南国出身吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220241119V这样不怕冷吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030241120V#021F#6P从小就跟着旅行艺人剧团\n',
            '到处走过了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030241121V热的地方冷的地方都没问题哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030241122V#022F话·说·回·来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030241123V#027F玲的爸爸妈妈\n',
            '到底去了哪里呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x012F,
        (
            '#0220241124V#266F#2P呼，没办法了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220241125V#260F爸爸妈妈\n',
            '去了哪里……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220241110V玲也不太清楚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_6857(): pass

    label('loc_6857')

    ChrTalk(
        0x0101,
        (
            '#0010241127V#1004F不知道？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x012F,
        (
            '#0220241128V#263F#2P玲和爸爸妈妈一起\n',
            '来这里玩的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220241129V但是吃了午饭以后，爸爸他们\n',
            '一脸认真地对玲说。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220241130V#262F爸爸妈妈有很重要的事情\n',
            '不得不和玲分别了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220241131V不过没关系，事情办完了\n',
            '一定来接玲的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220241132V在爸爸妈妈回来之前\n',
            '乖乖地等着好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x00F7, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_69E0',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)

    Jump('loc_6A1E')

    def _loc_69E0(): pass

    label('loc_69E0')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6A07',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)

    Jump('loc_6A1E')

    def _loc_6A07(): pass

    label('loc_6A07')

    OP_62(0x00F8, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)

    def _loc_6A1E(): pass

    label('loc_6A1E')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6A45',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)

    Jump('loc_6A83')

    def _loc_6A45(): pass

    label('loc_6A45')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6A6C',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)

    Jump('loc_6A83')

    def _loc_6A6C(): pass

    label('loc_6A6C')

    OP_62(0x00F9, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)

    def _loc_6A83(): pass

    label('loc_6A83')

    OP_62(0x0008, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1500)

    ChrTalk(
        0x0101,
        (
            '#0010241133V#1019F这，这是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x012F,
        (
            '#0220241134V#261F#2P呵呵，玲已经１１岁了\n',
            '就回答当然好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220241135V然后，爸爸妈妈\n',
            '就走了。',
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
        'loc_6B64',
    )

    ChrTalk(
        0x0106,
        (
            '#0050241136V#551F#6P喂喂，开玩笑吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6B8E')

    def _loc_6B64(): pass

    label('loc_6B64')

    ChrTalk(
        0x0103,
        (
            '#0030241137V#025F#6P这可头痛了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6B8E(): pass

    label('loc_6B8E')

    ChrTalk(
        0x0008,
        (
            '#2330241138V#5P嗯……\n',
            '没想到事情是这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#2330241139V#5P怎么办？\n',
            '感觉没动力\n',
            '去找监护人了。',
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
        'loc_6C89',
    )

    ChrTalk(
        0x0101,
        (
            '#0010211304V#1007F嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010241141V#1015F阿加特、明白吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050241142V#552F#6P没办法……\n',
            '这也是协会的工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6D00')

    def _loc_6C89(): pass

    label('loc_6C89')

    ChrTalk(
        0x0101,
        (
            '#0010211304V#1007F嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010241144V#1015F雪拉姐、明白吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030241145V#524F#6P当然了。\n',
            '这也是协会的工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6D00(): pass

    label('loc_6D00')

    ChrTurnDirection(0x0101, 0x0008, 400)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010241146V#1006F管家先生、别担心。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010241147V这孩子我们\n',
            '会负责照顾的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2330241148V#5P咦……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x012F, 400)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010241149V#1006F对了，玲。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010241150V和姐姐们一起\n',
            '去王都的协会好吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010241151V一定会马上\n',
            '找到爸爸妈妈的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x012F,
        (
            '#0220241152V#264F#2P是吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220241153V但是爸爸妈妈，说\n',
            '有很重要的事情哦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010241154V#1006F没问题没问题。\n',
            '绝对会找到的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010241155V#1018F相信姐姐啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x012F,
        (
            '#0220241156V#267F#2P嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220241157V#265F那玲\n',
            '跟姐姐一起去。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220241158V就交给你照顾了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010241159V#1006F嗯！\n',
            '也请你多关照哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2330241160V#5P呼……真是抱歉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2330241161V#5P那孩子的事，就拜托了。',
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
        'loc_6FEC',
    )

    ChrTalk(
        0x0106,
        (
            '#0050241162V#053F#6P啊啊，交给我们吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050241163V#051F好……\n',
            '赶快返回协会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7040')

    def _loc_6FEC(): pass

    label('loc_6FEC')

    ChrTalk(
        0x0103,
        (
            '#0030241164V#021F#6P嗯嗯，交给我们吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030241165V#020F那么……\n',
            '就回协会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7040(): pass

    label('loc_7040')

    FadeOut(1000, 0, -1)
    OP_0D()
    CameraMove(-16620, 0, 16070, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0000, -16620, 0, 16070, 180)
    ChrSetPos(0x0001, -16620, 0, 16070, 180)
    ChrSetPos(0x0002, -16620, 0, 16070, 180)
    ChrSetPos(0x0003, -16620, 0, 16070, 180)
    ChrSetPos(0x012F, -16620, 0, 16070, 180)
    OP_64(0x05, 0x0001)
    ChrSetDirection(0x0008, 225, 0)
    OP_4B(0x0008, 255)
    SetScenaFlags(ScenaFlag(0x02C2, 7, 0x1617))
    Sleep(500)

    FadeIn(1000, 0)
    OP_28(0x0089, 0x01, 0x2000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 5, 0x1615)),
            Expr.Return,
        ),
        'loc_710D',
    )

    Jump('loc_7121')

    def _loc_710D(): pass

    label('loc_710D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02D0, 2, 0x1682)),
            Expr.Return,
        ),
        'loc_711C',
    )

    OP_2B(0x0089, 0x0001)

    Jump('loc_7121')

    def _loc_711C(): pass

    label('loc_711C')

    OP_2B(0x0089, 0x0003)

    def _loc_7121(): pass

    label('loc_7121')

    EventEnd(0x00)

    Return()

# id: 0x001E offset: 0x7124
@scena.Code('func_1E_7124')
def func_1E_7124():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '此后，王国军的警备艇\n',
            '进行了彻夜的搜索……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '结果，依然没能抓住少女所乘的\n',
            '巨大人形兵器的去向。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '翌日──',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(500)

    CameraMove(-11130, 0, -43550, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(1980, 0)
    OP_6C(33000, 0)
    OP_6E(386, 0)
    ChrSetPos(0x000C, -11940, 200, -43100, 180)
    ChrSetPos(0x010F, -11940, 0, -45090, 0)
    ChrSetPos(0x000B, -10710, 0, -43660, 270)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrSetFlags(0x000C, 0x0004)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0109, 0x0080)
    ChrSetFlags(0x00F7, 0x0080)
    PlayBGM(83)
    Sleep(100)

    FadeIn(3000, 0)
    CameraSetDistance(1780, 3000)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x000B,
        (
            '#0620270767V#700F──凯诺娜。\n',
            '求求你了说出来吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620270768V那少女，是以怎样的形式\n',
            '接触你们的？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620270769V还有你们了解\n',
            '『结社』的存在到什么程度？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0610270770V#1238F#5P……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010F,
        (
            '#0100270771V#176F凯诺娜……\n',
            '别耍性子了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100270772V#178F这样下去不仅是你\n',
            '连你部下们的罪也会加重。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100270773V这不是你的本意吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0610270774V#1231F#5P哼，他们和我\n',
            '都早已有死的觉悟。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610270775V岂会屈服于这种程度的威胁。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010F,
        (
            '#0100270776V#177F不要轻易言死！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100270777V#177F你也看到了吧！\n',
            '那个巨大的人形兵器！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100270778V使用那种东西的家伙\n',
            '潜入了王国啊！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100270779V事态严重\n',
            '你不可能不明白吧！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0610270770V#1238F#5P……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0620270781V#703F凯诺娜……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620270782V#700F在某种意义上来说\n',
            '理查德上校是高洁的爱国者。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620270783V比任何人都希望利贝尔自主独立\n',
            '不受任何威胁。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620270784V这点我认为是真心的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620270785V#703F而现在，利贝尔中\n',
            '新的乌云正在悄悄临近……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620270786V如果他知道了\n',
            '会怎么想？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0610270787V#1238F#5P……啰嗦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0620270788V#702F什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x000C, 1)
    Sleep(500)

    ChrTalk(
        0x000C,
        (
            '#0610270789V#1236F#6P#3S……啰嗦、闭嘴！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    Sleep(300)

    ChrTalk(
        0x000C,
        (
            '#0610270790V#1235F#6P别那么冠冕堂皇地\n',
            '谈论理查德阁下的心情！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610270791V赶走阁下\n',
            '抢走其地位之辈！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0620270792V#700F……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010F,
        (
            '#0100270793V#177F凯诺娜、你这家伙！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x000C, 0)
    Sleep(300)

    ChrTalk(
        0x000C,
        (
            '#0610270794V#1230F#5P你也一样，尤莉亚！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610270795V看着过去的竞争对手\n',
            '落魄至此\n',
            '想必很愉快吧！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610270796V#1234F那你就笑啊！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610270797V不管是来自内心的笑还是嘲笑都无所谓！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010F,
        (
            '#0100270798V#175F……凯诺娜…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0610270799V#1236F#5P我在泥泞中苟延残喘\n',
            '至今都是为了帮助阁下！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610270800V现在既然无法实现，\n',
            '我也没有生存的意义了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610270801V赶快枪毙我就是了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(6, 0x00, 0x64)
    Sleep(500)

    ChrSetPos(0x000D, -14860, 0, -49890, 90)

    NpcTalk(
        0x000D,
        '男性的声音',
        (
            '#0160270802V#5P喂喂……\n',
            '真是蠢话啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000C, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x000B, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x010F, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x000B, 0x000D, 400)
    ChrSetSubChip(0x000C, 0)
    Sleep(50)

    ChrSetSubChip(0x000C, 2)
    ChrTurnDirection(0x010F, 0x000D, 400)
    ChrSetRGBAMask(0x000D, 255, 255, 255, 0, 0)
    ChrSetPos(0x000D, -13940, 0, -49200, 360)
    ChrClearFlags(0x000D, 0x0080)

    @scena.Lambda('lambda_79E4')
    def lambda_79E4():
        ChrTurnDirection(0x00FE, 0x000D, 0)
        Yield()

        Jump('lambda_79E4')

    DispatchAsync2(0x000B, 0x0001, lambda_79E4)

    @scena.Lambda('lambda_79F5')
    def lambda_79F5():
        ChrTurnDirection(0x00FE, 0x000D, 0)
        Yield()

        Jump('lambda_79F5')

    DispatchAsync2(0x010F, 0x0001, lambda_79F5)

    @scena.Lambda('lambda_7A06')
    def lambda_7A06():
        CameraMove(-11520, 0, -44030, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_7A06)

    @scena.Lambda('lambda_7A1E')
    def lambda_7A1E():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0002, lambda_7A1E)

    ChrWalkTo(0x000D, -13840, 0, -45630, 2000, 0x00)
    ChrSetDirection(0x000D, 90, 400)
    Sleep(500)

    TerminateThread(0x000B, 0x01)
    TerminateThread(0x010F, 0x01)

    ChrTalk(
        0x000D,
        (
            '#0160270803V#1120F#6P让我来阻止你吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0620270804V#702F#2P准将……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010F,
        (
            '#0100270805V#173F#2P为、为什么在这里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0160270806V#1125F#6P关于这次的事件\n',
            '有些事想和陛下商量。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160270807V#1120F另外还有些事\n',
            '所以刚到王都。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0620270808V#701F#2P原来如此……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010F,
        (
            '#0100270809V#171F#2P百忙之中，辛苦您了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0610270810V#1231F#5P卡西乌斯·布莱特……\n',
            '万恶的根源出现了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610270811V你也是来……\n',
            '嘲笑我的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000D, 0x000C, 400)
    Sleep(500)

    ChrTalk(
        0x000D,
        (
            '#0160270812V#1123F#6P哎呀哎呀，被讨厌了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160270813V别看我这样\n',
            '也以不输给理查德的\n',
            '男人风度而自满啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x000C,
        (
            '#0610270814V#1234F#5P#3S开、开什么玩笑！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x000C,
        (
            '#0610270815V#1235F#5P要是没有你……\n',
            '阁下……理查德阁下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x000E, -14860, 0, -49890, 90)

    NpcTalk(
        0x000E,
        '男性的声音',
        (
            '#0130270816V#5P咳咳、准将……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000E,
        '男性的声音',
        (
            '#0130270817V#5P能不能不要\n',
            '戏弄她啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000C, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x000B, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x010F, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x000B, 0x000E, 400)
    ChrTurnDirection(0x010F, 0x000E, 400)
    ChrTurnDirection(0x000D, 0x000E, 400)

    ChrTalk(
        0x000C,
        (
            '#0610270818V#1232F#5P咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0620270819V#702F#5P刚才那是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010F,
        (
            '#0100270820V#173F#2P难、难道是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_7E49')
    def lambda_7E49():
        CameraMove(-12930, 0, -43070, 3500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_7E49)

    @scena.Lambda('lambda_7E61')
    def lambda_7E61():
        OP_67(0, 7500, -10000, 3500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_7E61)

    @scena.Lambda('lambda_7E79')
    def lambda_7E79():
        CameraSetDistance(1700, 3500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_7E79)

    @scena.Lambda('lambda_7E89')
    def lambda_7E89():
        OP_6C(0, 3500)

        ExitThread()

    DispatchAsync(0x010F, 0x0002, lambda_7E89)

    @scena.Lambda('lambda_7E99')
    def lambda_7E99():
        OP_6E(400, 3500)

        ExitThread()

    DispatchAsync(0x010F, 0x0003, lambda_7E99)

    CreateThread(0x000D, 0x00, 0x00, func_1F_8534)
    Sleep(500)

    ChrSetRGBAMask(0x000E, 255, 255, 255, 0, 0)
    ChrSetPos(0x000E, -13940, 0, -49200, 360)
    ChrClearFlags(0x000E, 0x0080)

    @scena.Lambda('lambda_7ED6')
    def lambda_7ED6():
        ChrTurnDirection(0x00FE, 0x000E, 0)
        Yield()

        Jump('lambda_7ED6')

    DispatchAsync2(0x000B, 0x0001, lambda_7ED6)

    @scena.Lambda('lambda_7EE7')
    def lambda_7EE7():
        ChrTurnDirection(0x00FE, 0x000E, 0)
        Yield()

        Jump('lambda_7EE7')

    DispatchAsync2(0x010F, 0x0001, lambda_7EE7)

    @scena.Lambda('lambda_7EF8')
    def lambda_7EF8():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_7EF8)

    ChrWalkTo(0x000E, -13780, 0, -45300, 1500, 0x00)
    ChrSetDirection(0x000E, 45, 400)
    TerminateThread(0x000B, 0x01)
    TerminateThread(0x010F, 0x01)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x000C,
        (
            '#0610270821V#1239F#2P…………啊………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010F,
        (
            '#0100270822V#173F#2P理、理查德上校！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0620270823V#701F#2P……好久不见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0130270824V#1170F#6P好久不见了。\n',
            '希德中校，舒华兹上尉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130270825V#1171F还有……凯诺娜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0610270826V#1239F#2P啊……啊啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0130270827V#1170F#6P虽还是服役之身\n',
            '但准将还是强人所难\n',
            '带我来这里了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130270828V无论如何也想和你，\n',
            '直接见面谈谈。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0610270829V#1239F#2P……和……我？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0130270830V#1170F#6P啊啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130270831V#1173F──抱歉，凯诺娜。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130270832V我的傲慢和目光短浅\n',
            '让你们也卷进来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130270833V让前途有望的年轻才干们\n',
            '承担了犯罪行为。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130270834V#1174F我一直想为此道歉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0610270835V#1233F#2P请别这样、阁下！\n',
            '我们是因自己的意志……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0130270836V#1172F#6P不，这是我的责任。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130270837V你们只不过是按照我的方针，\n',
            '来行动而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130270838V在这个意义上这次事件\n',
            '也可以算是我的责任吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0610270839V#1237F#2P怎、怎么会……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0130270840V#1173F#6P所以……\n',
            '我在此重新宣言。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130270841V#1172F──由现在开始\n',
            '王国军情报部解散。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130270842V以后，其任务会由军司令部\n',
            '全权接手吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130270843V#1171F凯诺娜……\n',
            '以前真是辛苦你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0610270844V#1232F#2P………啊……………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0130270845V#1170F#6P这下……\n',
            '你就不需要再勉强了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130270846V不需要再为了帮助我\n',
            '而压上性命了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130270847V#1174F所以去死之类……\n',
            '悲哀的事不要说了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0610270848V#1245F#2P理查德……阁下……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610270849V#1237F……呜呜……啊啊啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    OP_7C(0, 200, 3000, 100)
    FadeOut(1500, 0, -1)

    @scena.Lambda('lambda_84D1')
    def lambda_84D1():
        CameraSetDistance(1980, 1500)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_84D1)

    ChrTalk(
        0x000C,
        (
            '#0610270850V#1246F#4S#2P#16A呜啊啊啊啊啊啊啊……！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    OP_0D()
    OP_20(0x00000BB8)
    OP_21()
    Sleep(2000)

    FormationDelMember(0x0E, 0xFF)
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    MapClearFlags(0x02000000)
    NewScene('ED6_DT21/T4121._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x001F offset: 0x8534
@scena.Code('func_1F_8534')
def func_1F_8534():
    ChrSetDirection(0x00FE, 0, 400)
    ChrWalkTo(0x00FE, -14300, 0, -44180, 1500, 0x00)
    ChrSetDirection(0x00FE, 90, 400)

    Return()

# id: 0x0020 offset: 0x8557
@scena.Code('func_20_8557')
def func_20_8557():
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
        (0x00000000, 'loc_85D1'),
        (0x00000001, 'loc_85D7'),
        (-1, 'loc_85DD'),
    )

    def _loc_85D1(): pass

    label('loc_85D1')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_85DD')

    def _loc_85D7(): pass

    label('loc_85D7')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_85DD')

    def _loc_85DD(): pass

    label('loc_85DD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_85EB',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    Jump('loc_85EF')

    def _loc_85EB(): pass

    label('loc_85EB')

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    def _loc_85EF(): pass

    label('loc_85EF')

    Return()

# id: 0x0021 offset: 0x85F0
@scena.Code('func_21_85F0')
def func_21_85F0():
    MapClearFlags(0x00000001)
    CameraMove(-3960, 0, -27940, 0)
    Sleep(100)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_8633',
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

    Jump('loc_8651')

    def _loc_8633(): pass

    label('loc_8633')

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

    def _loc_8651(): pass

    label('loc_8651')

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

# id: 0x0022 offset: 0x8671
@scena.Code('func_22_8671')
def func_22_8671():
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '有着漂亮装饰的碟子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Return()

# id: 0x0023 offset: 0x86B8
@scena.Code('func_23_86B8')
def func_23_86B8():
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '放置着东方风格的壶。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Return()

# id: 0x0024 offset: 0x86FF
@scena.Code('func_24_86FF')
def func_24_86FF():
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '放置着帝国风格的壶。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Return()

# id: 0x0025 offset: 0x8746
@scena.Code('func_25_8746')
def func_25_8746():
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '罗列着美术品目录。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Return()

# id: 0x0026 offset: 0x878B
@scena.Code('func_26_878B')
def func_26_878B():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '『先王的宝席』\n',
            '　先王埃德加Ⅲ世\n',
            '　在艾尔贝离宫逗留时\n',
            '　常用的椅子。',
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
