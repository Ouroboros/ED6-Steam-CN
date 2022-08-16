import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T3410_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3410   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'T3410.x'
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
        ('ED6_DT07/CH01300._CH', 'ED6_DT07/CH01300P._CP'),
        ('ED6_DT07/CH01350._CH', 'ED6_DT07/CH01350P._CP'),
        ('ED6_DT07/CH01520._CH', 'ED6_DT07/CH01520P._CP'),
        ('ED6_DT07/CH01180._CH', 'ED6_DT07/CH01180P._CP'),
        ('ED6_DT07/CH01670._CH', 'ED6_DT07/CH01670P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01143._CH', 'ED6_DT07/CH01143P._CP'),
        ('ED6_DT26/CH20255._CH', 'ED6_DT26/CH20255P._CP'),
    ]

# id: 0x10001 offset: 0xF2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '迪尔队长',
            x                   = 111940,
            z                   = 0,
            y                   = 22150,
            direction           = 283,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '塔尔瓦托副队长',
            x                   = 17500,
            z                   = 0,
            y                   = 2380,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '黛米',
            x                   = 61040,
            z                   = 0,
            y                   = -24890,
            direction           = 265,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            name                = '桑吉特',
            x                   = 54970,
            z                   = 0,
            y                   = -21440,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            name                = '塔丽娅',
            x                   = 89560,
            z                   = 0,
            y                   = -22370,
            direction           = 98,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '士兵维恩',
            x                   = 6790,
            z                   = 0,
            y                   = 2810,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            name                = '利瓦尔牧师',
            x                   = 77860,
            z                   = 0,
            y                   = 26210,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '士兵埃克托尔',
            x                   = 2190,
            z                   = 0,
            y                   = 2570,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0011,
        ),
        ScenaNpcData(
            name                = '安敦',
            x                   = 25320,
            z                   = 4000,
            y                   = 85000,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x00F4,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '安敦',
            x                   = 25320,
            z                   = 4000,
            y                   = 85000,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x00F4,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '安敦',
            x                   = 25120,
            z                   = 4000,
            y                   = 83900,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0088,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '安敦',
            x                   = 25120,
            z                   = 4000,
            y                   = 84740,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0088,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '利库斯',
            x                   = 26560,
            z                   = 4700,
            y                   = 83080,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x01B5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0015,
        ),
        ScenaNpcData(
            name                = '安敦',
            x                   = 22030,
            z                   = 4000,
            y                   = 83790,
            direction           = 248,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0012,
        ),
        ScenaNpcData(
            name                = '安敦',
            x                   = 25000,
            z                   = 4000,
            y                   = 83850,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x01B5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '安敦',
            x                   = 25100,
            z                   = 4000,
            y                   = 84740,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x01B5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '安敦',
            x                   = 25000,
            z                   = 4000,
            y                   = 84340,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x01B5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x312
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x312
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x312
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 109850,
            triggerZ            = 0,
            triggerY            = 21800,
            triggerRange        = 1000,
            actorX              = 111940,
            actorZ              = 1500,
            actorY              = 22150,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0009,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 91680,
            triggerZ            = 0,
            triggerY            = -22240,
            triggerRange        = 1000,
            actorX              = 89560,
            actorZ              = 1500,
            actorY              = -22370,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 6760,
            triggerZ            = 0,
            triggerY            = 900,
            triggerRange        = 1000,
            actorX              = 6790,
            actorZ              = 1500,
            actorY              = 2810,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000C,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 25170,
            triggerZ            = 4000,
            triggerY            = 83960,
            triggerRange        = 1000,
            actorX              = 25170,
            actorZ              = 4500,
            actorY              = 83960,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0013,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x3A2
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_3EF',
    )

    ChrSetFlags(0x000E, 0x0080)
    ChrSetPos(0x0009, 110750, 0, 24170, 197)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3DB',
    )

    ChrSetPos(0x000A, 58340, 0, -22400, 90)

    Jump('loc_3EC')

    def _loc_3DB(): pass

    label('loc_3DB')

    ChrSetPos(0x000A, 94780, 0, -22050, 270)

    def _loc_3EC(): pass

    label('loc_3EC')

    Jump('loc_811')

    def _loc_3EF(): pass

    label('loc_3EF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_427',
    )

    ChrSetPos(0x0009, 4950, 0, -2820, 45)
    CreateThread(0x0009, 0x00, 0x00, func_04_92D)
    ChrSetPos(0x000A, 58340, 0, -22400, 90)
    ChrSetFlags(0x000E, 0x0080)

    Jump('loc_811')

    def _loc_427(): pass

    label('loc_427')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 2, 0x162A)),
            Expr.Return,
        ),
        'loc_45F',
    )

    ChrSetPos(0x0009, 4950, 0, -2820, 45)
    CreateThread(0x0009, 0x00, 0x00, func_04_92D)
    ChrSetPos(0x000A, 94780, 0, -22050, 270)
    ChrSetFlags(0x000E, 0x0080)

    Jump('loc_811')

    def _loc_45F(): pass

    label('loc_45F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            Expr.Return,
        ),
        'loc_49C',
    )

    ChrSetPos(0x0009, 4950, 0, -2820, 45)
    CreateThread(0x0009, 0x00, 0x00, func_04_92D)
    ChrSetFlags(0x000D, 0x0010)
    ChrSetPos(0x000A, 58340, 0, -22400, 90)
    ChrSetFlags(0x000E, 0x0080)

    Jump('loc_811')

    def _loc_49C(): pass

    label('loc_49C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_4D4',
    )

    ChrSetPos(0x0009, 4950, 0, -2820, 45)
    CreateThread(0x0009, 0x00, 0x00, func_04_92D)
    ChrSetPos(0x000A, 58340, 0, -22400, 90)
    ChrSetFlags(0x000E, 0x0080)

    Jump('loc_811')

    def _loc_4D4(): pass

    label('loc_4D4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_533',
    )

    ChrSetPos(0x0009, 4950, 0, -2820, 45)
    CreateThread(0x0009, 0x00, 0x00, func_04_92D)
    ChrSetPos(0x000A, 78750, 0, 26210, 270)
    ChrSetFlags(0x000A, 0x0010)
    ChrSetPos(0x000E, 77860, 0, 26210, 90)
    ChrSetFlags(0x000E, 0x0010)
    ChrClearFlags(0x0014, 0x0080)
    ChrClearFlags(0x0015, 0x0080)
    CreateThread(0x0015, 0x00, 0x00, func_06_975)

    Jump('loc_811')

    def _loc_533(): pass

    label('loc_533')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_630',
    )

    ChrSetPos(0x0008, 111940, 0, 22150, 0)
    ChrSetFlags(0x0008, 0x0010)
    ChrSetPos(0x0009, 111940, 0, 23370, 180)
    ChrSetFlags(0x0009, 0x0010)
    ChrSetPos(0x000F, 77580, 0, 23520, 0)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x000D, 6810, 0, 2810, 180)
    ChrSetPos(0x000A, 79530, 0, 24930, 315)
    ChrSetFlags(0x000E, 0x0010)
    ChrClearFlags(0x0014, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0012, 0x0080)
    ChrClearFlags(0x0013, 0x0080)

    ExecExpressionWithValue(
        0x0010,
        0x2A,
        (
            (Expr.PushLong, 0xAFC8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0010,
        0x2B,
        (
            (Expr.PushLong, 0x15F90),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0010,
        0x2C,
        (
            (Expr.PushLong, 0xFFFEA070),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetFlags(0x0011, 0x0040)
    ChrSetFlags(0x0011, 0x0008)
    ChrSetFlags(0x0011, 0x0004)
    ChrSetPos(0x0011, 25120, 3500, 83900, 0)
    ChrClearFlags(0x0016, 0x0080)
    ChrClearFlags(0x0017, 0x0080)
    ChrClearFlags(0x0018, 0x0080)

    ExecExpressionWithValue(
        0x0016,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0017,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0018,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_811')

    def _loc_630(): pass

    label('loc_630')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_71B',
    )

    ChrSetPos(0x0009, 52040, 0, 24880, 75)
    ChrSetPos(0x000F, 8700, 0, 3240, 344)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x000D, 4950, 0, -2820, 45)
    CreateThread(0x000D, 0x00, 0x00, func_04_92D)
    CreateThread(0x000A, 0x00, 0x00, func_02_8E5)
    ChrSetPos(0x000E, 15400, 0, 1400, 180)
    ChrClearFlags(0x0014, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0012, 0x0080)
    ChrClearFlags(0x0013, 0x0080)

    ExecExpressionWithValue(
        0x0010,
        0x2A,
        (
            (Expr.PushLong, 0xAFC8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0010,
        0x2B,
        (
            (Expr.PushLong, 0x15F90),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0010,
        0x2C,
        (
            (Expr.PushLong, 0xFFFEA070),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetFlags(0x0011, 0x0040)
    ChrSetFlags(0x0011, 0x0008)
    ChrSetFlags(0x0011, 0x0004)
    ChrSetPos(0x0011, 25120, 3500, 83900, 0)
    ChrClearFlags(0x0016, 0x0080)
    ChrClearFlags(0x0017, 0x0080)
    ChrClearFlags(0x0018, 0x0080)

    ExecExpressionWithValue(
        0x0016,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0017,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0018,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_811')

    def _loc_71B(): pass

    label('loc_71B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 5, 0x1415)),
            Expr.Return,
        ),
        'loc_77C',
    )

    ChrSetPos(0x0009, 51170, 0, 28460, 0)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x000D, 4950, 0, -2820, 45)
    CreateThread(0x000D, 0x00, 0x00, func_04_92D)
    ChrSetPos(0x000A, 58330, 0, -22280, 90)
    ChrSetPos(0x000E, 15400, 0, 1400, 180)
    CreateThread(0x000E, 0x00, 0x00, func_05_951)

    Jump('loc_811')

    def _loc_77C(): pass

    label('loc_77C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 3, 0x1413)),
            Expr.Return,
        ),
        'loc_7EB',
    )

    ChrSetPos(0x0009, 51170, 0, 28460, 0)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x000D, 4950, 0, -2820, 45)
    CreateThread(0x000D, 0x00, 0x00, func_04_92D)
    ChrSetPos(0x000C, 94890, 0, -22010, 90)
    CreateThread(0x000A, 0x00, 0x00, func_02_8E5)
    CreateThread(0x000B, 0x00, 0x00, func_03_909)
    ChrSetPos(0x000E, 15400, 0, 1400, 180)
    CreateThread(0x000E, 0x00, 0x00, func_05_951)

    Jump('loc_811')

    def _loc_7EB(): pass

    label('loc_7EB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_811',
    )

    CreateThread(0x000A, 0x00, 0x00, func_02_8E5)
    ChrSetPos(0x0009, 4950, 0, -2820, 45)
    CreateThread(0x0009, 0x00, 0x00, func_04_92D)

    def _loc_811(): pass

    label('loc_811')

    Return()

# id: 0x0001 offset: 0x812
@scena.Code('func_01_812')
def func_01_812():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_82D',
    )

    OP_72(0x0005, 0x0010)
    OP_6F(0x0005, 100)

    Jump('loc_832')

    def _loc_82D(): pass

    label('loc_82D')

    OP_1C(0x05, 0x00, 0x001D)

    def _loc_832(): pass

    label('loc_832')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_840',
    )

    OP_64(0x03, 0x0001)

    Jump('loc_88B')

    def _loc_840(): pass

    label('loc_840')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_84A',
    )

    Jump('loc_88B')

    def _loc_84A(): pass

    label('loc_84A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_858',
    )

    OP_64(0x02, 0x0001)

    Jump('loc_88B')

    def _loc_858(): pass

    label('loc_858')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 5, 0x1415)),
            Expr.Return,
        ),
        'loc_86A',
    )

    OP_64(0x02, 0x0001)
    OP_64(0x03, 0x0001)

    Jump('loc_88B')

    def _loc_86A(): pass

    label('loc_86A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 3, 0x1413)),
            Expr.Return,
        ),
        'loc_880',
    )

    OP_64(0x01, 0x0001)
    OP_64(0x02, 0x0001)
    OP_64(0x03, 0x0001)

    Jump('loc_88B')

    def _loc_880(): pass

    label('loc_880')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_88B',
    )

    OP_64(0x03, 0x0001)

    def _loc_88B(): pass

    label('loc_88B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_898',
    )

    OP_10(0x13, 0x00)

    Jump('loc_8A8')

    def _loc_898(): pass

    label('loc_898')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 5, 0x1415)),
            Expr.Return,
        ),
        'loc_8A5',
    )

    OP_10(0x12, 0x00)

    Jump('loc_8A8')

    def _loc_8A5(): pass

    label('loc_8A5')

    OP_10(0x13, 0x00)

    def _loc_8A8(): pass

    label('loc_8A8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 2, 0x1412)),
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_8C2',
    )

    MapSetFlags(0x02000000)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x22),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_8C2(): pass

    label('loc_8C2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_8D3',
    )

    OP_1B(0x01, 0x00, 0x0016)

    def _loc_8D3(): pass

    label('loc_8D3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_8E4',
    )

    OP_1B(0x00, 0x00, 0x0017)

    def _loc_8E4(): pass

    label('loc_8E4')

    Return()

# id: 0x0002 offset: 0x8E5
@scena.Code('func_02_8E5')
def func_02_8E5():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_908',
    )

    OP_8D(0x00FE, 56600, -23980, 64040, -26210, 2000)

    Jump('func_02_8E5')

    def _loc_908(): pass

    label('loc_908')

    Return()

# id: 0x0003 offset: 0x909
@scena.Code('func_03_909')
def func_03_909():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_92C',
    )

    OP_8D(0x00FE, 58110, -23110, 53730, -21470, 2000)

    Jump('func_03_909')

    def _loc_92C(): pass

    label('loc_92C')

    Return()

# id: 0x0004 offset: 0x92D
@scena.Code('func_04_92D')
def func_04_92D():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_950',
    )

    OP_8D(0x00FE, 3140, -1230, 9860, -4460, 2000)

    Jump('func_04_92D')

    def _loc_950(): pass

    label('loc_950')

    Return()

# id: 0x0005 offset: 0x951
@scena.Code('func_05_951')
def func_05_951():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_974',
    )

    OP_8D(0x00FE, 14200, 2000, 18960, 180, 2000)

    Jump('func_05_951')

    def _loc_974(): pass

    label('loc_974')

    Return()

# id: 0x0006 offset: 0x975
@scena.Code('func_06_975')
def func_06_975():
    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_97F(): pass

    label('loc_97F')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_9D5',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    OP_8D(0x00FE, 22690, 84450, 21020, 83270, 6000)

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_9D2',
    )

    OP_62(0x00FE, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_9D2(): pass

    label('loc_9D2')

    Jump('loc_97F')

    def _loc_9D5(): pass

    label('loc_9D5')

    Return()

# id: 0x0007 offset: 0x9D6
@scena.Code('func_07_9D6')
def func_07_9D6():
    Call(0, 0x0008)

    Return()

# id: 0x0008 offset: 0x9DB
@scena.Code('func_08_9DB')
def func_08_9DB():
    TalkBegin(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 3, 0x1413)),
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 5, 0x1415)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A13',
    )

    Call(6, 0x0006)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A02',
    )

    OP_A9(0xAC)
    TalkEnd(0x000C)

    Return()

    def _loc_A02(): pass

    label('loc_A02')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A13',
    )

    TalkEnd(0x000C)

    Return()

    def _loc_A13(): pass

    label('loc_A13')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_AD2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A87',
    )

    ChrTalk(
        0x000C,
        (
            '在这种时候\n',
            '竟然还要品评男人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '黛米真没\n',
            '紧张感啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '唉，看来是\n',
            '从小没教育好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    Jump('loc_ACF')

    def _loc_A87(): pass

    label('loc_A87')

    ChrTalk(
        0x000C,
        (
            '在这种时候\n',
            '竟然还要品评男人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '一定是整天\n',
            '在想着钓金龟婿吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_ACF(): pass

    label('loc_ACF')

    Jump('loc_1150')

    def _loc_AD2(): pass

    label('loc_AD2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_BC7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B76',
    )

    ChrTalk(
        0x000C,
        (
            '哎呀，你们是客人？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '近来或许因为世道不好，\n',
            '客人明显少了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '床也有富裕，\n',
            '请好好休息吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '特别优惠，\n',
            '一个人可以使用两个枕头。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    Jump('loc_BC4')

    def _loc_B76(): pass

    label('loc_B76')

    ChrTalk(
        0x000C,
        (
            '近来或许因为世道不好，\n',
            '客人明显少了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '床也有富裕，\n',
            '请好好休息吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BC4(): pass

    label('loc_BC4')

    Jump('loc_1150')

    def _loc_BC7(): pass

    label('loc_BC7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_BFE',
    )

    ChrTalk(
        0x000C,
        (
            '士兵们也没什么休息的\n',
            '空暇，真不容易……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1150')

    def _loc_BFE(): pass

    label('loc_BFE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 2, 0x162A)),
            Expr.Return,
        ),
        'loc_C43',
    )

    ChrTalk(
        0x000C,
        (
            '黛米又在偷懒了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '说不定很快\n',
            '就要被炒鱿鱼了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1150')

    def _loc_C43(): pass

    label('loc_C43')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            Expr.Return,
        ),
        'loc_C97',
    )

    ChrTalk(
        0x000C,
        (
            '呵呵，今天在这里\n',
            '住宿的人运气真好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '刚刚晾了被褥，\n',
            '非常暖和的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1150')

    def _loc_C97(): pass

    label('loc_C97')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_D1C',
    )

    ChrTalk(
        0x000C,
        (
            '欢迎光临，\n',
            '欢迎来到圣海姆门旅馆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '最近去亚尔摩温泉的\n',
            '客人总算增加了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '安全宣言发出后，\n',
            '地震好象也不发生了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1150')

    def _loc_D1C(): pass

    label('loc_D1C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_E03',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_D7F',
    )

    ChrTalk(
        0x000C,
        (
            '今天黛米恨难得地\n',
            '去做礼拜了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '今天来的牧师先生\n',
            '好像是个相当不错的男人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E00')

    def _loc_D7F(): pass

    label('loc_D7F')

    ChrTalk(
        0x000C,
        (
            '今天黛米恨难得地\n',
            '去做礼拜了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '那个女孩儿有这样的信仰心\n',
            '我觉得我们没有休息的余地……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '一定是因为牧师是个好男人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_E00(): pass

    label('loc_E00')

    Jump('loc_1150')

    def _loc_E03(): pass

    label('loc_E03')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_F12',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_E62',
    )

    ChrTalk(
        0x000C,
        (
            '只在地震的时候\n',
            '去祈祷真是失礼啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '太自说自话的话\n',
            '女神就不会生气吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F0F')

    def _loc_E62(): pass

    label('loc_E62')

    ChrTalk(
        0x000C,
        (
            '说起来从大圣堂\n',
            '来了牧师哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '又发生了地震，\n',
            '要不过一会去祈祷吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '不过只在地震的时候\n',
            '去祈祷是不是太失礼了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '如果我是女神的话\n',
            '一定会让这种人吃天罚的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_F0F(): pass

    label('loc_F0F')

    Jump('loc_1150')

    def _loc_F12(): pass

    label('loc_F12')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_FDD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_F74',
    )

    ChrTalk(
        0x000C,
        (
            '善后也基本上弄好了，\n',
            '我们也重新开始营业了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '需要的话就请在这里休息吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FDA')

    def _loc_F74(): pass

    label('loc_F74')

    ChrTalk(
        0x000C,
        (
            '哎呀，欢迎。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '善后也基本上弄好了，\n',
            '我们也重新开始营业了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '需要的话就请在这里休息吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_FDA(): pass

    label('loc_FDA')

    Jump('loc_1150')

    def _loc_FDD(): pass

    label('loc_FDD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 3, 0x1413)),
            Expr.Return,
        ),
        'loc_109A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_1036',
    )

    ChrTalk(
        0x000C,
        (
            '堆积着的行李\n',
            '好像都塌下来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '因为平常没整理，\n',
            '就变成这样了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1097')

    def _loc_1036(): pass

    label('loc_1036')

    ChrTalk(
        0x000C,
        (
            '是场挺大的地震呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '像这种真正的震感\n',
            '好久没碰见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '不管怎样，\n',
            '先要收拾一下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_1097(): pass

    label('loc_1097')

    Jump('loc_1150')

    def _loc_109A(): pass

    label('loc_109A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_1150',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_10ED',
    )

    ChrTalk(
        0x000C,
        (
            '吃饭请去\n',
            '旁边的食堂。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '价格公道，\n',
            '而且味道的评价也很好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1150')

    def _loc_10ED(): pass

    label('loc_10ED')

    ChrTalk(
        0x000C,
        (
            '欢迎来到圣海姆门。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '这里是任何人都欢迎的\n',
            '旅客用投宿设施哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '需要的时候\n',
            '请跟我说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_1150(): pass

    label('loc_1150')

    TalkEnd(0x000C)

    Return()

# id: 0x0009 offset: 0x1154
@scena.Code('func_09_1154')
def func_09_1154():
    Call(0, 0x000A)

    Return()

# id: 0x000A offset: 0x1159
@scena.Code('func_0A_1159')
def func_0A_1159():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_1272',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_121B',
    )

    ChrTalk(
        0x0008,
        (
            '身份不明的红衣士兵和\n',
            '像机械一样的魔兽群……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '现在在的王国中\n',
            '潜伏着看不见的敌人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '就算门不能关闭\n',
            '我们也不会让他们恣意妄为。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '因为我们是\n',
            '光荣的王都护盾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_126F')

    def _loc_121B(): pass

    label('loc_121B')

    ChrTalk(
        0x0008,
        (
            '就算门不能关闭\n',
            '也绝对不会让阴谋势力恣意妄为。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '因为我们是\n',
            '光荣的王都护盾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_126F(): pass

    label('loc_126F')

    Jump('loc_18A4')

    def _loc_1272(): pass

    label('loc_1272')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_13B8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_135D',
    )

    ChrTalk(
        0x0008,
        (
            '中央工房发明的那东西\n',
            '使通讯功能恢复了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '接下来要尽快\n',
            '恢复门的功能……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '那个零力场发生器\n',
            '还没批量生产吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '如果那东西有二、三十个的话\n',
            '整个哨所的功能都能完全恢复了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1007F（说、说得真轻松～）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_13B5')

    def _loc_135D(): pass

    label('loc_135D')

    ChrTalk(
        0x0008,
        (
            '中央工房发明的那东西\n',
            '使通讯功能恢复了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '唔，就不能再多\n',
            '分配几个那种发生器吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_13B5(): pass

    label('loc_13B5')

    Jump('loc_18A4')

    def _loc_13B8(): pass

    label('loc_13B8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_144E',
    )

    ChrTalk(
        0x0008,
        (
            '好像有报告说王都\n',
            '出现了巨大的人形兵器……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '到底在开什么玩笑？\n',
            '怎么可能有那种东西？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '等会儿得去向副队长确认一下这事儿的真实性。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_18A4')

    def _loc_144E(): pass

    label('loc_144E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 2, 0x162A)),
            Expr.Return,
        ),
        'loc_14CB',
    )

    ChrTalk(
        0x0008,
        (
            '希德中校担任警备本部的负责人啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '在王国军内部\n',
            '他那卓越的指挥能力是得到公认的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '虽然外界不太了解。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_18A4')

    def _loc_14CB(): pass

    label('loc_14CB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            Expr.Return,
        ),
        'loc_155D',
    )

    ChrTalk(
        0x0008,
        (
            '签字仪式的会场是艾尔贝离宫的话，\n',
            '这里的警戒就极为重要了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '有什么闪失的话\n',
            '就会成为外国人的笑柄了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '所以丝毫都不能松懈。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_18A4')

    def _loc_155D(): pass

    label('loc_155D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_15CB',
    )

    ChrTalk(
        0x0008,
        (
            '关于那场地震，\n',
            '好象已经发出安全宣言了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '虽然还心有余悸，\n',
            '不过这样的话就能集中精力警戒了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_18A4')

    def _loc_15CB(): pass

    label('loc_15CB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_16C3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_1642',
    )

    ChrTalk(
        0x0008,
        (
            '看来那一连串的地震的\n',
            '问题总算是解决了……不过',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '还有很多无法解释的地方。\n',
            '暂时还不能放松警惕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_16C0')

    def _loc_1642(): pass

    label('loc_1642')

    ChrTalk(
        0x0008,
        (
            '看来那一连串的地震的\n',
            '问题总算是解决了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '不过实在是\n',
            '还有很多无法解释的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '真是的……\n',
            '暂时还不能放松警惕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_16C0(): pass

    label('loc_16C0')

    Jump('loc_18A4')

    def _loc_16C3(): pass

    label('loc_16C3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_177C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_1716',
    )

    ChrTalk(
        0x0008,
        (
            '不管怎样我们也\n',
            '继续警戒。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '尽管面对地震\n',
            '确实是没办法……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1779')

    def _loc_1716(): pass

    label('loc_1716')

    ChrTalk(
        0x0008,
        (
            '这次轮到雷斯顿要塞\n',
            '发生地震了吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '地点都在军队的重要设施，\n',
            '实在无法相信这是偶然的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_1779(): pass

    label('loc_1779')

    Jump('loc_18A4')

    def _loc_177C(): pass

    label('loc_177C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 3, 0x1413)),
            Expr.Return,
        ),
        'loc_181A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 4, 0x1414)),
            Expr.Return,
        ),
        'loc_17CE',
    )

    ChrTalk(
        0x0008,
        (
            '什么？你们还有事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我不是说了我有工作吗？\n',
            '不要妨碍我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1817')

    def _loc_17CE(): pass

    label('loc_17CE')

    ChrTalk(
        0x0008,
        (
            '关于情况的说明\n',
            '你们去找塔尔瓦托副队长。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '因为我还有紧急的工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1817(): pass

    label('loc_1817')

    Jump('loc_18A4')

    def _loc_181A(): pass

    label('loc_181A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_18A4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_1868',
    )

    ChrTalk(
        0x0008,
        (
            '我都说了我在工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '老缠着我的话\n',
            '就把你们赶出哨所。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_18A4')

    def _loc_1868(): pass

    label('loc_1868')

    ChrTalk(
        0x0008,
        (
            '你们在搞什么啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '抱歉，我在工作。\n',
            '不要妨碍我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_18A4(): pass

    label('loc_18A4')

    TalkEnd(0x0008)

    Return()

# id: 0x000B offset: 0x18A8
@scena.Code('func_0B_18A8')
def func_0B_18A8():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_19B5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1968',
    )

    ChrTalk(
        0x00FE,
        (
            '敌人下一步想要干什么……\n',
            '实在无法预料。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在要紧的是\n',
            '不能随便行动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就是说要稳固好防线，\n',
            '然后看穿敌人的意图。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '当然，敌人也有可能\n',
            '正希望我们这么做。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Jump('loc_19B2')

    def _loc_1968(): pass

    label('loc_1968')

    ChrTalk(
        0x00FE,
        (
            '敌人下一步想要干什么……\n',
            '实在无法预料。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在只能先\n',
            '稳固好防线。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_19B2(): pass

    label('loc_19B2')

    Jump('loc_2146')

    def _loc_19B5(): pass

    label('loc_19B5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1AFA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1AA3',
    )

    ChrTalk(
        0x00FE,
        (
            '通讯机的修复\n',
            '真是一个久违了的好消息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在卡西乌斯准将的指挥下，\n',
            '各地的王国军终于\n',
            '有组织地开始行动了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然现在还处在主力装备\n',
            '无法使用的困境之下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '即便如此，努力做到最好也是\n',
            '我们军人的责任和义务。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Jump('loc_1AF7')

    def _loc_1AA3(): pass

    label('loc_1AA3')

    ChrTalk(
        0x00FE,
        (
            '通讯机的修复\n',
            '真是一个久违了的好消息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '整个王国军终于\n',
            '有组织地开始行动了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1AF7(): pass

    label('loc_1AF7')

    Jump('loc_2146')

    def _loc_1AFA(): pass

    label('loc_1AFA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_1BAD',
    )

    ChrTalk(
        0x00FE,
        (
            '为了抓情报部的余党，\n',
            '这里的部队也被借走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在想想，这是情报部为了\n',
            '在王都举兵而制造的假象吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '能看穿这一点而提前把尤莉亚上尉\n',
            '叫回来，真不愧是希德中校。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2146')

    def _loc_1BAD(): pass

    label('loc_1BAD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 2, 0x162A)),
            Expr.Return,
        ),
        'loc_1C1A',
    )

    ChrTalk(
        0x00FE,
        (
            '听说雷斯顿要塞\n',
            '收到了恐吓信。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然不了解内容，\n',
            '不过真要搞破坏的话\n',
            '偷偷地进行不就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2146')

    def _loc_1C1A(): pass

    label('loc_1C1A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            Expr.Return,
        ),
        'loc_1CB1',
    )

    ChrTalk(
        0x00FE,
        (
            '可能是因为签字仪式的关系，\n',
            '最近能看到很多外国人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们的魔鬼队长先生\n',
            '也快要开足马力了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在他说话之前我得\n',
            '赶紧去宣传加强警戒。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2146')

    def _loc_1CB1(): pass

    label('loc_1CB1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_1D4E',
    )

    ChrTalk(
        0x00FE,
        (
            '事情一件又一件的，\n',
            '真是忙乱到极点了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '地震的骚乱刚刚平息，\n',
            '接着就快要到签字仪式的日子了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '听说接下来要在\n',
            '艾尔贝离宫设置警备本部了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2146')

    def _loc_1D4E(): pass

    label('loc_1D4E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_1E2A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_1DA7',
    )

    ChrTalk(
        0x0009,
        (
            '军队的上层最近\n',
            '活动得挺积极的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '难道是旧情报部的\n',
            '余党落网了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E27')

    def _loc_1DA7(): pass

    label('loc_1DA7')

    ChrTalk(
        0x0009,
        (
            '似乎中央工房已经发出了\n',
            '地震终结的宣言。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '我们军队的上层也\n',
            '也发来了相同的通知。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '嗯，看来这不是单纯的\n',
            '自然现象。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_1E27(): pass

    label('loc_1E27')

    Jump('loc_2146')

    def _loc_1E2A(): pass

    label('loc_1E2A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_1EFD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_1E9D',
    )

    ChrTalk(
        0x0009,
        (
            '我要让士兵们\n',
            '继续保持警戒态势。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '关于要塞地震的受害情况\n',
            '等到有明确消息了我会告知你们的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1EFA')

    def _loc_1E9D(): pass

    label('loc_1E9D')

    ChrTalk(
        0x0009,
        (
            '雷斯顿要塞的受害程度\n',
            '好像被控制在最低限度了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '看来是事先觉察到\n',
            '会有地震发生了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_1EFA(): pass

    label('loc_1EFA')

    Jump('loc_2146')

    def _loc_1EFD(): pass

    label('loc_1EFD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_1F8A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_1F40',
    )

    ChrTalk(
        0x0009,
        (
            '呼，总算收拾整齐了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '真是重体力劳动啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F87')

    def _loc_1F40(): pass

    label('loc_1F40')

    ChrTalk(
        0x0009,
        (
            '呼～这边\n',
            '总算也收拾整齐了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '那么，我得去其他\n',
            '岗位看看了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_1F87(): pass

    label('loc_1F87')

    Jump('loc_2146')

    def _loc_1F8A(): pass

    label('loc_1F8A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 3, 0x1413)),
            Expr.Return,
        ),
        'loc_20AE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_1FE7',
    )

    ChrTalk(
        0x0009,
        (
            '对了，迪尔队长\n',
            '好象恨忙哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '就算你们问他什么，\n',
            '也只会被骂回来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_20AB')

    def _loc_1FE7(): pass

    label('loc_1FE7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 5, 0x1415)),
            Expr.Return,
        ),
        'loc_2052',
    )

    ChrTalk(
        0x0009,
        (
            '哟，各位游击士。\n',
            '调查有进展吗？？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '我这边也\n',
            '快要收拾好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '傍晚之前\n',
            '应该能弄好吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_20A8')

    def _loc_2052(): pass

    label('loc_2052')

    ChrTalk(
        0x0009,
        (
            '昨天切斯利看到了\n',
            '一个奇怪的男人哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '他在屋顶收拾，\n',
            '详细情况你们可以去问他。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_20A8(): pass

    label('loc_20A8')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_20AB(): pass

    label('loc_20AB')

    Jump('loc_2146')

    def _loc_20AE(): pass

    label('loc_20AE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_2146',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_210E',
    )

    ChrTalk(
        0x0009,
        (
            '登上里面的台阶\n',
            '就能到达『亚宁堡』的\n',
            '上层。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '来旅游的客人\n',
            '经常上去的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2146')

    def _loc_210E(): pass

    label('loc_210E')

    ChrTalk(
        0x0009,
        (
            '哎呀，欢迎。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '如果需要设施的说明\n',
            '请跟我说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_2146(): pass

    label('loc_2146')

    TalkEnd(0x0009)

    Return()

# id: 0x000C offset: 0x214A
@scena.Code('func_0C_214A')
def func_0C_214A():
    Call(0, 0x000D)

    Return()

# id: 0x000D offset: 0x214F
@scena.Code('func_0D_214F')
def func_0D_214F():
    TalkBegin(0x000D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_2273',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_220C',
    )

    ChrTalk(
        0x000D,
        (
            '最近我常做一个梦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '就是世界毁灭了，\n',
            '只剩下这座哨所。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '通讯机不能用的那段时间\n',
            '确实有那样的感觉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '现在如果没有旅客来的话，\n',
            '想起来还是觉得很可怕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    Jump('loc_2270')

    def _loc_220C(): pass

    label('loc_220C')

    ChrTalk(
        0x000D,
        (
            '最近常做世界毁灭了，\n',
            '只剩下这座哨所的梦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '现在如果没有旅客来的话，\n',
            '想起来还是觉得很可怕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2270(): pass

    label('loc_2270')

    Jump('loc_28B1')

    def _loc_2273(): pass

    label('loc_2273')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_2368',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2313',
    )

    ChrTalk(
        0x000D,
        (
            '因为现在门也不能锁，\n',
            '我对通行管理特别用心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '你们游击士可以\n',
            '随意出入，请放心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '因为有特别的通知，\n',
            '好象是卡西乌斯准将的命令。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    Jump('loc_2365')

    def _loc_2313(): pass

    label('loc_2313')

    ChrTalk(
        0x000D,
        (
            '你们游击士\n',
            '可以自由通行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '在卡西乌斯准将的命令下\n',
            '已经发出那样的通知了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2365(): pass

    label('loc_2365')

    Jump('loc_28B1')

    def _loc_2368(): pass

    label('loc_2368')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_23D0',
    )

    ChrTalk(
        0x000D,
        (
            '格兰赛尔亲卫队\n',
            '和情报部发生过战斗了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '原来在王都集中全部的\n',
            '战斗力就是为了这个啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_28B1')

    def _loc_23D0(): pass

    label('loc_23D0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 2, 0x162A)),
            Expr.Return,
        ),
        'loc_2432',
    )

    ChrTalk(
        0x000D,
        (
            '从昨天起希德中校\n',
            '好像进入了艾尔贝离宫。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '好像要布置\n',
            '比想象中更为森严的警戒啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_28B1')

    def _loc_2432(): pass

    label('loc_2432')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            Expr.Return,
        ),
        'loc_2478',
    )

    ChrTurnDirection(0x000D, 0x012F, 400)

    ChrTalk(
        0x000D,
        (
            '哟，好可爱的小姑娘。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '放松一点好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000D, 180, 0)

    Jump('loc_28B1')

    def _loc_2478(): pass

    label('loc_2478')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_252E',
    )

    ChrTalk(
        0x000D,
        (
            '真是的，前几天的地震\n',
            '可让我们吃了苦头了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '虽然不知道是不是和地震有关\n',
            '不过周游道的魔兽变得活跃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '有报告说在\n',
            '艾尔贝离宫附近\n',
            '出现了大型魔兽，你们要小心哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_28B1')

    def _loc_252E(): pass

    label('loc_252E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_25C8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_2587',
    )

    ChrTalk(
        0x000D,
        (
            '地震的善后工作\n',
            '也总算结束了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '哎呀呀，简直是\n',
            '一场飞来横祸啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_25C5')

    def _loc_2587(): pass

    label('loc_2587')

    ChrTalk(
        0x000D,
        (
            '呀，欢迎。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '现在已经和平常\n',
            '一样在办理通行手续了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    def _loc_25C5(): pass

    label('loc_25C5')

    Jump('loc_28B1')

    def _loc_25C8(): pass

    label('loc_25C8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_26C9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_262D',
    )

    ChrTalk(
        0x000D,
        (
            '唔～偶尔祈祷一次\n',
            '灵魂得到了安宁的感觉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '下次趁休息去参加\n',
            '大圣堂的礼拜吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_26C6')

    def _loc_262D(): pass

    label('loc_262D')

    ChrTalk(
        0x000D,
        (
            '刚才我去神父先生\n',
            '那里祈祷了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '偶尔祈祷一次\n',
            '灵魂得到了安宁的感觉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '至少应该在地震时\n',
            '向女神祈祷啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '那场地震也一定是\n',
            '女神的意志。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    def _loc_26C6(): pass

    label('loc_26C6')

    Jump('loc_28B1')

    def _loc_26C9(): pass

    label('loc_26C9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_2771',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_272E',
    )

    ChrTalk(
        0x000D,
        (
            '牧师先生是自己\n',
            '提出要帮忙的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '不愧是牧师先生啊。\n',
            '虽然年轻，可是很懂道理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_276E')

    def _loc_272E(): pass

    label('loc_272E')

    ChrTalk(
        0x000D,
        (
            '呼～终于收拾整齐了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '这也是拜牧师先生的\n',
            '帮忙所赐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    def _loc_276E(): pass

    label('loc_276E')

    Jump('loc_28B1')

    def _loc_2771(): pass

    label('loc_2771')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 3, 0x1413)),
            Expr.Return,
        ),
        'loc_2805',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_27CA',
    )

    ChrTalk(
        0x000D,
        (
            '刚才的地震\n',
            '摇得挺厉害啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '没有人受伤\n',
            '可以说是不可思议的事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2802')

    def _loc_27CA(): pass

    label('loc_27CA')

    ChrTalk(
        0x000D,
        (
            '看上去很凌乱吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '刚才的地震\n',
            '摇得挺厉害啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    def _loc_2802(): pass

    label('loc_2802')

    Jump('loc_28B1')

    def _loc_2805(): pass

    label('loc_2805')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_28B1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_2860',
    )

    ChrTalk(
        0x000D,
        (
            '诞辰庆典也结束了，\n',
            '最近游客少了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '反正我们这些\n',
            '士兵算是轻松了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_28B1')

    def _loc_2860(): pass

    label('loc_2860')

    ChrTalk(
        0x000D,
        (
            '欢迎来到圣海姆门。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '难得来一趟，\n',
            '请一定要欣赏一下\n',
            '『亚宁堡』的英姿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    def _loc_28B1(): pass

    label('loc_28B1')

    TalkEnd(0x000D)

    Return()

# id: 0x000E offset: 0x28B5
@scena.Code('func_0E_28B5')
def func_0E_28B5():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 5, 0x1415)),
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_28C6',
    )

    Call(0, 0x0018)

    Return()

    def _loc_28C6(): pass

    label('loc_28C6')

    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_29E4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2975',
    )

    ChrTalk(
        0x00FE,
        (
            '男人的价值\n',
            '要到紧急时刻才能看出来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '危难之时能够依靠的\n',
            '才是货真价实的男人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵，这么想的话\n',
            '现在正是绝好的机会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我要好好地品评～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Jump('loc_29E1')

    def _loc_2975(): pass

    label('loc_2975')

    ChrTalk(
        0x00FE,
        (
            '危难之时能够依靠的\n',
            '才是货真价实的男人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这么想的话\n',
            '现在正是绝好的机会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵，真令人期待啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_29E1(): pass

    label('loc_29E1')

    Jump('loc_2F66')

    def _loc_29E4(): pass

    label('loc_29E4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_2A9A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2A47',
    )

    ChrTalk(
        0x00FE,
        (
            '哎呀，游击士们。\n',
            '你们是来吃饭的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我正闲得发慌呢。\n',
            '呵呵，热烈欢迎㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Jump('loc_2A97')

    def _loc_2A47(): pass

    label('loc_2A47')

    ChrTalk(
        0x00FE,
        (
            '感觉～这世道\n',
            '真是不好混啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，我也想快点\n',
            '找到一个能依靠的男朋友啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2A97(): pass

    label('loc_2A97')

    Jump('loc_2F66')

    def _loc_2A9A(): pass

    label('loc_2A9A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_2AEC',
    )

    ChrTalk(
        0x00FE,
        (
            '士兵们说有巨大\n',
            '人偶袭击了王都……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '人偶……\n',
            '比如小熊小狗那种？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F66')

    def _loc_2AEC(): pass

    label('loc_2AEC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 2, 0x162A)),
            Expr.Return,
        ),
        'loc_2B28',
    )

    ChrTalk(
        0x00FE,
        (
            '好，快要到休息时间了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哪儿有好男人呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F66')

    def _loc_2B28(): pass

    label('loc_2B28')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            Expr.Return,
        ),
        'loc_2B65',
    )

    ChrTalk(
        0x00FE,
        (
            '士兵们终于\n',
            '吃完饭了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊，可把我忙坏了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F66')

    def _loc_2B65(): pass

    label('loc_2B65')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_2BE6',
    )

    ChrTalk(
        0x00FE,
        (
            '唉，牧师先生也回去了，\n',
            '真没劲……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我当时应该追他到\n',
            '王都的大圣堂的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，我也绝不想给\n',
            '对方添麻烦啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F66')

    def _loc_2BE6(): pass

    label('loc_2BE6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_2CA8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_2C6D',
    )

    ChrTalk(
        0x000A,
        (
            '唔～我将来的伴侣……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '莫非是……\n',
            '要是牧师先生的话㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '哎呀，我该怎么办呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000E, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Jump('loc_2CA5')

    def _loc_2C6D(): pass

    label('loc_2C6D')

    ChrTalk(
        0x000A,
        (
            '我的男人运\n',
            '可不好哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '怎样做才能改变\n',
            '命运呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2CA5(): pass

    label('loc_2CA5')

    Jump('loc_2F66')

    def _loc_2CA8(): pass

    label('loc_2CA8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_2DAE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_2D1B',
    )

    ChrTalk(
        0x000A,
        (
            '啊，他热心奉献\n',
            '祈祷的神情真是太棒了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '在牧师大人清秀的侧脸上\n',
            '我能感觉到女神的存在啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2DAB')

    def _loc_2D1B(): pass

    label('loc_2D1B')

    ChrTalk(
        0x000A,
        (
            '我听说有年轻的牧师在，\n',
            '今天就来做礼拜了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '没想到他不仅不年轻，\n',
            '而且还相当英俊呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '呵呵，要是这种礼拜的话\n',
            '我每天都能来参加㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_2DAB(): pass

    label('loc_2DAB')

    Jump('loc_2F66')

    def _loc_2DAE(): pass

    label('loc_2DAE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_2E85',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_2E15',
    )

    ChrTalk(
        0x000A,
        (
            '我是那种容易迷上别人，\n',
            '不过不会死缠烂打的类型。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '呵呵，这样才能\n',
            '享受恋爱啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2E82')

    def _loc_2E15(): pass

    label('loc_2E15')

    ChrTalk(
        0x000A,
        (
            '唔～真可惜。\n',
            '明明是个很帅的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '不过既然是特别人物那就算了。\n',
            '我还是放弃他，去找其它的好男人吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_2E82(): pass

    label('loc_2E82')

    Jump('loc_2F66')

    def _loc_2E85(): pass

    label('loc_2E85')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 3, 0x1413)),
            Expr.Return,
        ),
        'loc_2EC6',
    )

    ChrTalk(
        0x000A,
        (
            '唉～怎么收拾也\n',
            '收拾不完。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '真是的，讨厌死了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F66')

    def _loc_2EC6(): pass

    label('loc_2EC6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_2F66',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_2F37',
    )

    ChrTalk(
        0x000A,
        (
            '诞辰庆典也结束了，\n',
            '最近挺闲的～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '虽然经营方面出现困难，\n',
            '不过我能轻松一些，也挺高兴的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F66')

    def _loc_2F37(): pass

    label('loc_2F37')

    ChrTalk(
        0x000A,
        (
            '欢迎光临。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '请随意选择喜欢的座位。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_2F66(): pass

    label('loc_2F66')

    TalkEnd(0x000A)

    Return()

# id: 0x000F offset: 0x2F6A
@scena.Code('func_0F_2F6A')
def func_0F_2F6A():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 3, 0x1413)),
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 5, 0x1415)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3127',
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
        1,
        (
            TXT(0x00, '对话\n'),
            TXT(0x01, '买东西\n'),
            TXT(0x02, '招牌菜『东方火锅·力』　1200米拉\n'),
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
        'loc_2FF6',
    )

    FadeIn(300, 0)
    OP_0D()
    OP_A9(0xAD)
    OP_56(0x00)
    TalkEnd(0x000B)

    Return()

    def _loc_2FF6(): pass

    label('loc_2FF6')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3104',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x12),
            (Expr.PushLong, 0x4B0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_30CF',
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
            '东方火锅·力',
            (TxtCtl.SetColor, 0x0),
            '已经品尝过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetStatus(ChrTable['艾丝蒂尔'], 0xFD, 1800)
    ChrSetStatus(ChrTable['约修亚'], 0xFD, 1800)
    ChrSetStatus(ChrTable['雪拉扎德'], 0xFD, 1800)
    ChrSetStatus(ChrTable['奥利维尔'], 0xFD, 1800)
    ChrSetStatus(ChrTable['科洛丝'], 0xFD, 1800)
    ChrSetStatus(ChrTable['阿加特'], 0xFD, 1800)
    ChrSetStatus(ChrTable['提妲'], 0xFD, 1800)
    ChrSetStatus(ChrTable['金'], 0xFD, 1800)
    ChrSetStatus(ChrTable['凯文神父'], 0xFD, 1800)

    If(
        (
            (Expr.Eval, "OP_40(0x020D, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_30C1',
    )

    If(
        (
            (Expr.Eval, "OP_AC(0x0007)"),
            Expr.Return,
        ),
        'loc_3095',
    )

    Jump('loc_30C1')

    def _loc_3095(): pass

    label('loc_3095')

    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            TxtCtl.ShowAll,
            (TxtCtl.SetColor, 0x2),
            '东方火锅·力',
            (TxtCtl.SetColor, 0x0),
            '的做法已经学会了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_30C1(): pass

    label('loc_30C1')

    OP_56(0x00)
    FadeIn(1000, 0)

    Jump('loc_30F5')

    def _loc_30CF(): pass

    label('loc_30CF')

    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            '没有足够的米拉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeIn(300, 0)
    def _loc_30F5(): pass

    label('loc_30F5')

    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x000B)

    Return()

    def _loc_3104(): pass

    label('loc_3104')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_311E',
    )

    FadeIn(300, 0)
    TalkEnd(0x000B)

    Return()

    def _loc_311E(): pass

    label('loc_311E')

    FadeIn(300, 0)

    def _loc_3127(): pass

    label('loc_3127')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_31EF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_31AA',
    )

    ChrTalk(
        0x00FE,
        (
            '哟～欢迎光临～\n',
            '你们能～来真是太好了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '难得来一趟，\n',
            '好好享受吧～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们会用 最好的\n',
            '菜招待你们的～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Jump('loc_31EC')

    def _loc_31AA(): pass

    label('loc_31AA')

    ChrTalk(
        0x00FE,
        (
            '哟～欢迎光临～\n',
            '你们能～来真是太好了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我正闲得\n',
            '发慌呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_31EC(): pass

    label('loc_31EC')

    Jump('loc_3781')

    def _loc_31EF(): pass

    label('loc_31EF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_32AE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3271',
    )

    ChrTalk(
        0x00FE,
        (
            '唉～真没办法～\n',
            '炉子也不能用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还好有炭火式的烤炉，\n',
            '总算能做菜～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '果然还是要珍藏\n',
            '一些旧工具的～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Jump('loc_32AB')

    def _loc_3271(): pass

    label('loc_3271')

    ChrTalk(
        0x00FE,
        (
            '好久没有用\n',
            '炭火烹调了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这个说不定\n',
            '又有怪事了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_32AB(): pass

    label('loc_32AB')

    Jump('loc_3781')

    def _loc_32AE(): pass

    label('loc_32AE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_32F5',
    )

    ChrTalk(
        0x00FE,
        (
            '总觉得军队的人\n',
            '突然变得很慌乱～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '又要发生什么了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3781')

    def _loc_32F5(): pass

    label('loc_32F5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 2, 0x162A)),
            Expr.Return,
        ),
        'loc_33B2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_335B',
    )

    ChrTalk(
        0x00FE,
        (
            '说起来，地震\n',
            '已经完全歇下来了啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看来中央工房的安全宣言\n',
            '是有根据的呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Jump('loc_33AF')

    def _loc_335B(): pass

    label('loc_335B')

    ChrTalk(
        0x00FE,
        (
            '谁也不能说绝对\n',
            '不会再发生地震了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以他们说安全的时候\n',
            '我也有所怀疑的～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_33AF(): pass

    label('loc_33AF')

    Jump('loc_3781')

    def _loc_33B2(): pass

    label('loc_33B2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            Expr.Return,
        ),
        'loc_33DA',
    )

    ChrTalk(
        0x00FE,
        (
            '呼～终于可以歇口气了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3781')

    def _loc_33DA(): pass

    label('loc_33DA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_3446',
    )

    ChrTalk(
        0x00FE,
        (
            '黛米那家伙……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '工作偷懒，到头来还要\n',
            '叹气抱怨说没劲～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这种话也不能当着\n',
            '我的面说啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3781')

    def _loc_3446(): pass

    label('loc_3446')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_34D1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_3485',
    )

    ChrTalk(
        0x00FE,
        (
            '真是的，黛米那家伙～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '也该回来了吧～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_34CE')

    def _loc_3485(): pass

    label('loc_3485')

    ChrTalk(
        0x00FE,
        (
            '哟～欢迎光临～\n',
            '要点菜找我哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不知道为什么\n',
            '女服务员不～在。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_34CE(): pass

    label('loc_34CE')

    Jump('loc_3781')

    def _loc_34D1(): pass

    label('loc_34D1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_35BB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_3539',
    )

    ChrTalk(
        0x00FE,
        (
            '我在这里也\n',
            '干了很久了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过现在看到顾客吃菜时,\n',
            '一瞬间心里也还是七上八下的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_35B8')

    def _loc_3539(): pass

    label('loc_3539')

    ChrTalk(
        0x00FE,
        (
            '我在这里也\n',
            '干了很久了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过现在看到顾客吃菜时,\n',
            '一瞬间心里也还是七上八下的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以我一直是背对着\n',
            '客人工作的～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_35B8(): pass

    label('loc_35B8')

    Jump('loc_3781')

    def _loc_35BB(): pass

    label('loc_35BB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_35FE',
    )

    ChrTalk(
        0x00FE,
        (
            '哟～话已经说完了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '方便的话\n',
            '在这儿喝杯茶吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3781')

    def _loc_35FE(): pass

    label('loc_35FE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 3, 0x1413)),
            Expr.Return,
        ),
        'loc_36DB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 5, 0x1415)),
            Expr.Return,
        ),
        'loc_3685',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_363B',
    )

    ChrTalk(
        0x00FE,
        (
            '哟～欢迎光临～\n',
            '总算恢复营业了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3682')

    def _loc_363B(): pass

    label('loc_363B')

    ChrTalk(
        0x00FE,
        (
            '哟～欢迎光临～\n',
            '总算恢复营业了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们可以尝尝\n',
            '我的新菜式～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_3682(): pass

    label('loc_3682')

    Jump('loc_36D8')

    def _loc_3685(): pass

    label('loc_3685')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_36A3',
    )

    ChrTalk(
        0x00FE,
        (
            '唉～真没办法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_36D8')

    def _loc_36A3(): pass

    label('loc_36A3')

    ChrTalk(
        0x00FE,
        (
            '唉～真没办法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不收拾一下都没法营业了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_36D8(): pass

    label('loc_36D8')

    Jump('loc_3781')

    def _loc_36DB(): pass

    label('loc_36DB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_3781',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_3743',
    )

    ChrTalk(
        0x000B,
        (
            '诞辰庆典之后真闲啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '因为太闲，\n',
            '我就开发了新菜式哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '请一～定要试试哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3781')

    def _loc_3743(): pass

    label('loc_3743')

    ChrTalk(
        0x000B,
        (
            '欢迎光临～\n',
            '欢迎来到食堂。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '请随意选择喜欢的座位。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_3781(): pass

    label('loc_3781')

    TalkEnd(0x000B)

    Return()

# id: 0x0010 offset: 0x3785
@scena.Code('func_10_3785')
def func_10_3785():
    TalkBegin(0x000E)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_38DD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_37E7',
    )

    ChrTalk(
        0x00FE,
        (
            '那、那个……\n',
            '我也该回去了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '关于你的烦恼\n',
            '可以来大圣堂说给我听……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_38DA')

    def _loc_37E7(): pass

    label('loc_37E7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_3841',
    )

    ChrTalk(
        0x00FE,
        (
            '我就在大圣堂里，\n',
            '你随时都可以过来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，不好意思，\n',
            '我也该回去了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_38DA')

    def _loc_3841(): pass

    label('loc_3841')

    ChrTalk(
        0x00FE,
        (
            '你的烦恼\n',
            '我完全能理解。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可是，问题永远\n',
            '是在你自己身上的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '阻止你和将来的伴侣\n',
            '相遇的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不正是你心中那个\n',
            '『理想的异性』的幻影吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    def _loc_38DA(): pass

    label('loc_38DA')

    Jump('loc_3B7F')

    def _loc_38DD(): pass

    label('loc_38DD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_39BC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_395C',
    )

    ChrTalk(
        0x00FE,
        (
            '我会继续为您祈祷。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '当我们迷失道路时，\n',
            '请您为我们指引正确的方向……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在深远的黑暗中\n',
            '守护我们……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_39B9')

    def _loc_395C(): pass

    label('loc_395C')

    ChrTalk(
        0x00FE,
        (
            '空之女神啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '请保佑聚集\n',
            '在这里的人们……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '请您在天空之上\n',
            '永远注视我们……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    def _loc_39B9(): pass

    label('loc_39B9')

    Jump('loc_3B7F')

    def _loc_39BC(): pass

    label('loc_39BC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_3A58',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_3A08',
    )

    ChrTalk(
        0x00FE,
        (
            '终于收拾好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，差不多该\n',
            '真想快点开始礼拜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3A55')

    def _loc_3A08(): pass

    label('loc_3A08')

    ChrTalk(
        0x00FE,
        (
            '终于收拾\n',
            '好象结束了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过天可真热啊。\n',
            '祭司服好象不适合运动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    def _loc_3A55(): pass

    label('loc_3A55')

    Jump('loc_3B7F')

    def _loc_3A58(): pass

    label('loc_3A58')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 3, 0x1413)),
            Expr.Return,
        ),
        'loc_3ACA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_3A95',
    )

    ChrTalk(
        0x00FE,
        (
            '不过都给\n',
            '弄乱了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我也来\n',
            '帮忙吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3AC7')

    def _loc_3A95(): pass

    label('loc_3A95')

    ChrTalk(
        0x00FE,
        (
            '好像没有人\n',
            '受伤。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是不幸中之大幸。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    def _loc_3AC7(): pass

    label('loc_3AC7')

    Jump('loc_3B7F')

    def _loc_3ACA(): pass

    label('loc_3ACA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_3B7F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_3B19',
    )

    ChrTalk(
        0x000E,
        (
            '各位士兵都在\n',
            '努力工作呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '我就在这里\n',
            '再等一会儿吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3B7F')

    def _loc_3B19(): pass

    label('loc_3B19')

    ChrTalk(
        0x000E,
        (
            '我是从大圣堂来\n',
            '为士兵们祈祷的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '不过还没有\n',
            '人过来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '嗯，看来大家\n',
            '都在努力工作呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    def _loc_3B7F(): pass

    label('loc_3B7F')

    TalkEnd(0x000E)

    Return()

# id: 0x0011 offset: 0x3B83
@scena.Code('func_11_3B83')
def func_11_3B83():
    TalkBegin(0x000F)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_3BC9',
    )

    ChrTalk(
        0x00FE,
        (
            '来礼拜的人\n',
            '比平时多啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是不是因为发生了地震？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3D49')

    def _loc_3BC9(): pass

    label('loc_3BC9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_3C97',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_3C1B',
    )

    ChrTalk(
        0x00FE,
        (
            '呼～终于结束了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好，牧师先生也来了，\n',
            '我去做个礼拜吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3C94')

    def _loc_3C1B(): pass

    label('loc_3C1B')

    ChrTalk(
        0x00FE,
        (
            '呼～终于结束了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为大家合力的关系，\n',
            '善后工作比预计的早完成了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好，牧师先生也来了，\n',
            '我去做个礼拜吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    def _loc_3C94(): pass

    label('loc_3C94')

    Jump('loc_3D49')

    def _loc_3C97(): pass

    label('loc_3C97')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 3, 0x1413)),
            Expr.Return,
        ),
        'loc_3D49',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_3D02',
    )

    ChrTalk(
        0x00FE,
        (
            '我的工作岗位是在外面，\n',
            '不过现在是紧急情况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以就离开工作岗位\n',
            '到里面来帮忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3D49')

    def _loc_3D02(): pass

    label('loc_3D02')

    ChrTalk(
        0x00FE,
        (
            '哨所里到处\n',
            '都有行李塌下来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不收拾好的话\n',
            '也没法好好警戒。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    def _loc_3D49(): pass

    label('loc_3D49')

    TalkEnd(0x000F)

    Return()

# id: 0x0012 offset: 0x3D4D
@scena.Code('func_12_3D4D')
def func_12_3D4D():
    UnlockAchievement(0x01, 0x000B, 0x00)
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_3D9C',
    )

    ChrTalk(
        0x00FE,
        (
            '还是不能在\n',
            '这种地方浪费人生！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总、总之要回王都去！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3DDA')

    def _loc_3D9C(): pass

    label('loc_3D9C')

    ChrTalk(
        0x00FE,
        (
            '不、不能在\n',
            '这种地方浪费人生！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好，赶快回王都去！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    def _loc_3DDA(): pass

    label('loc_3DDA')

    TalkEnd(0x00FE)

    Return()

# id: 0x0013 offset: 0x3DDE
@scena.Code('func_13_3DDE')
def func_13_3DDE():
    Call(0, 0x0014)

    Return()

# id: 0x0014 offset: 0x3DE3
@scena.Code('func_14_3DE3')
def func_14_3DE3():
    UnlockAchievement(0x01, 0x000B, 0x00)
    TalkBegin(0x0011)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_3E7A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_3E39',
    )

    ChrTalk(
        0x0011,
        (
            '还是不能在\n',
            '这种地方浪费人生！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '总、总之要回王都去！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3E77')

    def _loc_3E39(): pass

    label('loc_3E39')

    ChrTalk(
        0x0011,
        (
            '不、不能在\n',
            '这种地方浪费人生！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '好，赶快回王都去！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    def _loc_3E77(): pass

    label('loc_3E77')

    Jump('loc_402E')

    def _loc_3E7A(): pass

    label('loc_3E7A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_3F52',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_3ECF',
    )

    ChrTalk(
        0x0011,
        (
            '这么躺着\n',
            '总觉得很烦躁。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '我怎能就这样\n',
            '每天在这里浪费时间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3F4F')

    def _loc_3ECF(): pass

    label('loc_3ECF')

    ChrTalk(
        0x0011,
        (
            '总觉得这么躺着\n',
            '心情就会烦躁。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '难、难道我只能这样\n',
            '每天待在这里浪费时间吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '不知不觉间一辈子\n',
            '就过去了，真可怕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    def _loc_3F4F(): pass

    label('loc_3F4F')

    Jump('loc_402E')

    def _loc_3F52(): pass

    label('loc_3F52')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_402E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_3F9C',
    )

    ChrTalk(
        0x0011,
        (
            '啊，利库斯，告诉我！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '我的存在意义\n',
            '到底是什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_402E')

    def _loc_3F9C(): pass

    label('loc_3F9C')

    ChrTalk(
        0x0011,
        (
            '诞辰庆典就失恋……\n',
            '有地震就差点死……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '真悲惨……\n',
            '我连爬起来的力气也没有了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '啊，利库斯，告诉我！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '我的存在意义\n',
            '到底是什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    def _loc_402E(): pass

    label('loc_402E')

    TalkEnd(0x0011)

    Return()

# id: 0x0015 offset: 0x4032
@scena.Code('func_15_4032')
def func_15_4032():
    TalkBegin(0x0014)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_40F4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_40A0',
    )

    ChrTalk(
        0x00FE,
        (
            '冷静一点，安敦。\n',
            '你着急也不是办法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '反正不管怎样，\n',
            '你能恢复精神，我就很高兴了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_40F1')

    def _loc_40A0(): pass

    label('loc_40A0')

    ChrTalk(
        0x00FE,
        (
            '冷静一点，安敦。\n',
            '你那么着急也不是办法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总之我已经准备\n',
            '要回王都了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    def _loc_40F1(): pass

    label('loc_40F1')

    Jump('loc_4289')

    def _loc_40F4(): pass

    label('loc_40F4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_4191',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_412C',
    )

    ChrTalk(
        0x00FE,
        (
            '安敦那家伙好像\n',
            '也开始感到无聊了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_418E')

    def _loc_412C(): pass

    label('loc_412C')

    ChrTalk(
        0x00FE,
        (
            '这里的地板不太\n',
            '适合午睡。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还是王城的\n',
            '空中庭园比较理想。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那里的草坪\n',
            '看上去很软。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    def _loc_418E(): pass

    label('loc_418E')

    Jump('loc_4289')

    def _loc_4191(): pass

    label('loc_4191')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_4289',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_4229',
    )

    ChrTalk(
        0x00FE,
        (
            '抱歉啊，\n',
            '阻碍你们走路了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '时不时就开始思考自我价值\n',
            '是我的伙伴的臭毛病。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过没关系，过几天\n',
            '他想腻之后就肯定会恢复正常。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4289')

    def _loc_4229(): pass

    label('loc_4229')

    ChrTalk(
        0x00FE,
        (
            '安敦…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '从现在的状况来看，\n',
            '你的存在意义已经很明确了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……对，就是通行的障碍。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    def _loc_4289(): pass

    label('loc_4289')

    TalkEnd(0x0014)

    Return()

# id: 0x0016 offset: 0x428D
@scena.Code('func_16_428D')
def func_16_428D():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 3, 0x1413)),
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_43D9',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_42EF',
    )

    ChrTalk(
        0x0101,
        (
            '#0010221318V#1000F现在没必要去王都啊，\n',
            '赶快把探听的工作解决吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_43BB')

    def _loc_42EF(): pass

    label('loc_42EF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_435E',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_430C',
    )

    ChrTurnDirection(0x0106, 0x0001, 400)

    Jump('loc_4313')

    def _loc_430C(): pass

    label('loc_430C')

    ChrTurnDirection(0x0106, 0x0000, 400)

    def _loc_4313(): pass

    label('loc_4313')

    ChrTalk(
        0x0106,
        (
            '#0050221319V#050F现在没必要去王都啊。\n',
            '还是尽快把探听的工作解决吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_43BB')

    def _loc_435E(): pass

    label('loc_435E')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4374',
    )

    ChrTurnDirection(0x0103, 0x0001, 400)

    Jump('loc_437B')

    def _loc_4374(): pass

    label('loc_4374')

    ChrTurnDirection(0x0103, 0x0000, 400)

    def _loc_437B(): pass

    label('loc_437B')

    ChrTalk(
        0x0103,
        (
            '#0030221320V#027F没必要去王都哦。\n',
            '还是赶快继续探听工作吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_43BB(): pass

    label('loc_43BB')

    ChrMoveToRelative(0x0000, -1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Jump('loc_4518')

    def _loc_43D9(): pass

    label('loc_43D9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4518',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_4478',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4404',
    )

    ChrTurnDirection(0x0106, 0x0001, 400)

    Jump('loc_440B')

    def _loc_4404(): pass

    label('loc_4404')

    ChrTurnDirection(0x0106, 0x0000, 400)

    def _loc_440B(): pass

    label('loc_440B')

    ChrTalk(
        0x0106,
        (
            '#0050221321V#050F前面就是格兰赛尔地区了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050220142V现在可没时间去别的地方。\n',
            '现在还是乖乖回去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_44FD')

    def _loc_4478(): pass

    label('loc_4478')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_448E',
    )

    ChrTurnDirection(0x0103, 0x0001, 400)

    Jump('loc_4495')

    def _loc_448E(): pass

    label('loc_448E')

    ChrTurnDirection(0x0103, 0x0000, 400)

    def _loc_4495(): pass

    label('loc_4495')

    ChrTalk(
        0x0103,
        (
            '#0030221323V#020F前面是格兰赛尔地区了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030220144V没时间去其它的地方了，\n',
            '现在还是乖乖回去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_44FD(): pass

    label('loc_44FD')

    ChrMoveToRelative(0x0000, -1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_4518(): pass

    label('loc_4518')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_48AD',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_462C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_459E',
    )

    ChrTalk(
        0x0108,
        (
            '#0080241178V#070F我记得雾香\n',
            '已经为我们准备\n',
            '好了定期船。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080241179V我们乘定期船\n',
            '去王都吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4629')

    def _loc_459E(): pass

    label('loc_459E')

    ChrTalk(
        0x0108,
        (
            '#0080241180V#070F唔，过了这里就是王都了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080241181V我记得雾香\n',
            '已经为我们准备\n',
            '好了定期船。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080241179V我们乘定期船\n',
            '去王都吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    def _loc_4629(): pass

    label('loc_4629')

    Jump('loc_4892')

    def _loc_462C(): pass

    label('loc_462C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_4762',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4649',
    )

    ChrTurnDirection(0x0106, 0x0001, 400)

    Jump('loc_4650')

    def _loc_4649(): pass

    label('loc_4649')

    ChrTurnDirection(0x0106, 0x0000, 400)

    def _loc_4650(): pass

    label('loc_4650')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_46B6',
    )

    ChrTalk(
        0x0106,
        (
            '#0050241183V#050F雾香应该为我们\n',
            '准备好了船票。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050241184V我们还是乘定期船去王都吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_475F')

    def _loc_46B6(): pass

    label('loc_46B6')

    ChrTalk(
        0x0106,
        (
            '#0050241185V#050F虽然都走到这里了，\n',
            '不过我们还是乘定期船去王都吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050241186V我记得雾香已经为\n',
            '我们准备好了船票。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050241187V至少在路途中\n',
            '应该好好享受一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    def _loc_475F(): pass

    label('loc_475F')

    Jump('loc_4892')

    def _loc_4762(): pass

    label('loc_4762')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4778',
    )

    ChrTurnDirection(0x0103, 0x0001, 400)

    Jump('loc_477F')

    def _loc_4778(): pass

    label('loc_4778')

    ChrTurnDirection(0x0103, 0x0000, 400)

    def _loc_477F(): pass

    label('loc_477F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_47ED',
    )

    ChrTalk(
        0x0103,
        (
            '#0030241188V#020F雾香小姐应该\n',
            '已经为我们准备好了船票。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030241189V我们还是乘定期船去王都吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4892')

    def _loc_47ED(): pass

    label('loc_47ED')

    ChrTalk(
        0x0103,
        (
            '#0030241190V#020F虽然已经到了这里，\n',
            '不过我们还是乘定期船去王都吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030241191V雾香小姐特意\n',
            '为我们准备好了船票。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030241192V在路上的时候要\n',
            '好好享受才对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))

    def _loc_4892(): pass

    label('loc_4892')

    ChrMoveToRelative(0x0000, -1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_48AD(): pass

    label('loc_48AD')

    Return()

# id: 0x0017 offset: 0x48AE
@scena.Code('func_17_48AE')
def func_17_48AE():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 0, 0x1638)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4A50',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_492B',
    )

    ChrTalk(
        0x0108,
        (
            '#0080291614V#070F喂，前面就是蔡斯地区了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080271276V现在没空去其它的地方，\n',
            '赶快回去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4A35')

    def _loc_492B(): pass

    label('loc_492B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_49B0',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4948',
    )

    ChrTurnDirection(0x0106, 0x0001, 400)

    Jump('loc_494F')

    def _loc_4948(): pass

    label('loc_4948')

    ChrTurnDirection(0x0106, 0x0000, 400)

    def _loc_494F(): pass

    label('loc_494F')

    ChrTalk(
        0x0106,
        (
            '#0050291616V#050F这边是蔡斯地区。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050220142V没时间去别的地方了。\n',
            '现在还是乖乖回去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4A35')

    def _loc_49B0(): pass

    label('loc_49B0')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_49C6',
    )

    ChrTurnDirection(0x0103, 0x0001, 400)

    Jump('loc_49CD')

    def _loc_49C6(): pass

    label('loc_49C6')

    ChrTurnDirection(0x0103, 0x0000, 400)

    def _loc_49CD(): pass

    label('loc_49CD')

    ChrTalk(
        0x0103,
        (
            '#0030291618V#020F过了这里就是蔡斯地区了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030220144V没时间去其它的地方了，\n',
            '现在还是乖乖回去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4A35(): pass

    label('loc_4A35')

    ChrMoveToRelative(0x0000, 1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_4A50(): pass

    label('loc_4A50')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 0, 0x1638)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4B04',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4AAC',
    )

    ChrTalk(
        0x0101,
        (
            '#0010271282V#1002F没时间闲逛了。\n',
            '……要赶快返回协会才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4AE9')

    def _loc_4AAC(): pass

    label('loc_4AAC')

    ChrTalk(
        0x0109,
        (
            '#0180271283V#1063F没时间闲逛了。\n',
            '……赶紧去王都协会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4AE9(): pass

    label('loc_4AE9')

    ChrMoveToRelative(0x0000, 1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_4B04(): pass

    label('loc_4B04')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4E1B',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4C26',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_4B95',
    )

    ChrTalk(
        0x0108,
        (
            '#0080240201V#070F虽说徒步移动是修行，\n',
            '但那样太浪费时间。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080271567V要去柏斯的话\n',
            '还是用定期船比较好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4C23')

    def _loc_4B95(): pass

    label('loc_4B95')

    ChrTalk(
        0x0108,
        (
            '#0080291624V#070F这边是蔡斯地区。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080240204V虽说徒步移动是修行，\n',
            '但那样太浪费时间。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080271567V要去柏斯的话\n',
            '还是用定期船比较好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    def _loc_4C23(): pass

    label('loc_4C23')

    Jump('loc_4E00')

    def _loc_4C26(): pass

    label('loc_4C26')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_4D1A',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4C43',
    )

    ChrTurnDirection(0x0106, 0x0001, 400)

    Jump('loc_4C4A')

    def _loc_4C43(): pass

    label('loc_4C43')

    ChrTurnDirection(0x0106, 0x0000, 400)

    def _loc_4C4A(): pass

    label('loc_4C4A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_4CBC',
    )

    ChrTalk(
        0x0106,
        (
            '#0050240206V#053F……要走过去\n',
            '说实话太浪费时间。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050271572V#050F要去柏斯\n',
            '还是去定期船飞船坪吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4D17')

    def _loc_4CBC(): pass

    label('loc_4CBC')

    ChrTalk(
        0x0106,
        (
            '#0050291616V#050F这边是蔡斯地区。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050271574V要去柏斯的话\n',
            '还是去定期船飞船坪吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    def _loc_4D17(): pass

    label('loc_4D17')

    Jump('loc_4E00')

    def _loc_4D1A(): pass

    label('loc_4D1A')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4D30',
    )

    ChrTurnDirection(0x0103, 0x0001, 400)

    Jump('loc_4D37')

    def _loc_4D30(): pass

    label('loc_4D30')

    ChrTurnDirection(0x0103, 0x0000, 400)

    def _loc_4D37(): pass

    label('loc_4D37')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_4DA9',
    )

    ChrTalk(
        0x0103,
        (
            '#0030240210V#026F……要走过去\n',
            '说实话是浪费时间。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030271576V#020F要去柏斯\n',
            '还是去定期船飞船坪吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4E00')

    def _loc_4DA9(): pass

    label('loc_4DA9')

    ChrTalk(
        0x0103,
        (
            '#0030291633V#020F这边是蔡斯地区。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030271578V要去柏斯\n',
            '还是去定期船飞船坪吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))

    def _loc_4E00(): pass

    label('loc_4E00')

    ChrMoveToRelative(0x0000, 1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_4E1B(): pass

    label('loc_4E1B')

    Return()

# id: 0x0018 offset: 0x4E1C
@scena.Code('func_18_4E1C')
def func_18_4E1C():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4E36',
    )

    Call(0, 0x001C)
    FadeIn(0, 0)

    def _loc_4E36(): pass

    label('loc_4E36')

    EventBegin(0x00)
    OP_4A(0x000A, 255)
    Fade(1000)
    ChrSetPos(0x0101, 58340, 0, -23470, 0)
    ChrSetPos(0x00F7, 57170, 0, -23130, 45)
    ChrSetPos(0x0105, 57830, 0, -24520, 0)
    ChrSetPos(0x0104, 57040, 0, -24090, 45)
    CameraMove(58120, 0, -22770, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(36000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(
        0x000A,
        (
            '#3100221115V呼～终于收拾好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrSetDirection(0x000A, 225, 400)

    ChrTalk(
        0x000A,
        (
            '#3100221116V咦……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_4F68',
    )

    ChrTalk(
        0x0106,
        (
            '#0050221117V#051F#6P你就是黛米吧？\n',
            '我们是游击士协会的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4FAB')

    def _loc_4F68(): pass

    label('loc_4F68')

    ChrTalk(
        0x0103,
        (
            '#0030221118V#020F#6P你就是黛米小姐吧？\n',
            '我们是游击士协会的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4FAB(): pass

    label('loc_4FAB')

    ChrTalk(
        0x0101,
        (
            '#0010221119V#1006F其实，有件事\n',
            '想要打听一下……',
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
            '向黛米询问了\n',
            '有关墨镜男子的事情。',
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
            '#3100221120V哦，是那个人啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3100221121V昨天的休息时间\n',
            '我在２层的走廊和他擦肩而过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3100221122V我估计那是他从\n',
            '屋顶回来的时候……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040221123V#035F和那位士兵的证词一致。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040221124V#030F那么，你们除了擦肩而过之外\n',
            '没有交谈吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3100221125V算是打了个招呼吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3100221126V然后那个人笑了笑，\n',
            '回了一声。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3100221127V我可被他的\n',
            '野性感觉给电到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 2000, 0x0A, 0x0B, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(1000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_52DD',
    )

    ChrTalk(
        0x0101,
        (
            '#0010221128V#1015F野性……\n',
            '就是说像这个阿加特一样的感觉？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050221129V#552F#6P怎么说呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3100221130V嗯，感觉比那位\n',
            '大哥哥还要高。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3100221131V虽然外边套着黑色外套，\n',
            '不过胸口敞开，里面什么也没穿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3100221132V还有，两只手\n',
            '都戴着黑色的手套。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_53A3')

    def _loc_52DD(): pass

    label('loc_52DD')

    ChrTalk(
        0x0103,
        (
            '#0030221133V#026F#6P唔……\n',
            '人物的形象渐渐浮现出来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030221134V#020F他穿着什么衣服？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3100221135V黑色套装，\n',
            '不过胸口敞开，什么也没穿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3100221132V还有，两只手\n',
            '都戴着黑色的手套。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_53A3(): pass

    label('loc_53A3')

    ChrTalk(
        0x0101,
        (
            '#0010221137V#1007F墨镜加黑色套装。\n',
            '还有黑色的手套？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010221138V#1019F很可疑啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3100221139V与其说可疑不如说是个\n',
            '狰狞又充满危险感的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3100221140V呵呵，就是说『危险的魅力』？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x00F7, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0105, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0104, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010221141V#1016F先、先不说这些……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010221142V#1015F擦肩而过又打了招呼，\n',
            '后来就没见过了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3100221143V嗯，是的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3100221144V我追上去\n',
            '想要套近乎……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3100221145V不过在古怪的地方跟丢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010221146V#1004F古怪的地方……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3100221147V唔～\n',
            '还是让你们看看比较方便。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_55F5')
    def lambda_55F5():
        CameraMove(56990, 0, -22070, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_55F5)

    ChrTurnDirection(0x000A, 0x000B, 400)
    WaitForThreadExit(0x0101, 0x0003)

    ChrTalk(
        0x000A,
        (
            '#3100221148V#2P我说，桑吉特。\n',
            '我能出去一下吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4A(0x000B, 255)
    ChrTurnDirection(0x000B, 0x000A, 400)

    ChrTalk(
        0x000B,
        (
            '#3120221149V#5P算了～没办法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3120221150V#5P在做准备之前回来啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(500)

    OP_4B(0x000B, 255)
    Call(0, 0x0019)

    Return()

# id: 0x0019 offset: 0x56B7
@scena.Code('func_19_56B7')
def func_19_56B7():
    ChrSetPos(0x000A, 1580, 4000, 42070, 0)
    ChrSetPos(0x00F7, 2080, 4000, 40570, 0)
    ChrSetPos(0x0101, 1080, 4000, 40570, 0)
    ChrSetPos(0x0105, 2080, 4000, 39570, 0)
    ChrSetPos(0x0104, 1080, 4000, 39570, 0)
    CameraMove(2020, 4000, 50500, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeIn(1000, 0)

    @scena.Lambda('lambda_5758')
    def lambda_5758():
        OP_94(0x00, 0x00FE, 0x0000, 0x00002328, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_5758)

    Sleep(80)

    @scena.Lambda('lambda_5773')
    def lambda_5773():
        OP_94(0x00, 0x00FE, 0x0000, 0x00002328, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5773)

    Sleep(120)

    @scena.Lambda('lambda_578E')
    def lambda_578E():
        OP_94(0x00, 0x00FE, 0x0000, 0x00002328, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_578E)

    Sleep(80)

    @scena.Lambda('lambda_57A9')
    def lambda_57A9():
        OP_94(0x00, 0x00FE, 0x0000, 0x00002328, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_57A9)

    Sleep(120)

    @scena.Lambda('lambda_57C4')
    def lambda_57C4():
        OP_94(0x00, 0x00FE, 0x0000, 0x00002328, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_57C4)

    OP_0D()
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x000A, 0x0001)
    ChrSetDirection(0x000A, 180, 400)

    ChrTalk(
        0x000A,
        (
            '#3100221151V#5P我是在这里和\n',
            '那个人擦肩而过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3100221152V#5P然后那个人就一直\n',
            '走到了对面……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3100221153V#5P我为了和他搭讪\n',
            '又返回了走廊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010221154V#1002F嗯嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x000A, 0x00, 0x00, func_1A_5B4B)

    @scena.Lambda('lambda_58AB')
    def lambda_58AB():
        ChrTurnDirection(0x00FE, 0x000A, 400)
        Yield()

        Jump('lambda_58AB')

    DispatchAsync2(0x0101, 0x0000, lambda_58AB)

    @scena.Lambda('lambda_58BC')
    def lambda_58BC():
        ChrTurnDirection(0x00FE, 0x000A, 400)
        Yield()

        Jump('lambda_58BC')

    DispatchAsync2(0x00F7, 0x0000, lambda_58BC)

    @scena.Lambda('lambda_58CD')
    def lambda_58CD():
        ChrTurnDirection(0x00FE, 0x000A, 400)
        Yield()

        Jump('lambda_58CD')

    DispatchAsync2(0x0105, 0x0000, lambda_58CD)

    @scena.Lambda('lambda_58DE')
    def lambda_58DE():
        ChrTurnDirection(0x00FE, 0x000A, 400)
        Yield()

        Jump('lambda_58DE')

    DispatchAsync2(0x0104, 0x0000, lambda_58DE)

    Sleep(1300)

    @scena.Lambda('lambda_58F4')
    def lambda_58F4():
        CameraMove(3290, 4000, 40300, 2800)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_58F4)

    @scena.Lambda('lambda_590C')
    def lambda_590C():
        OP_67(0, 8000, -10000, 2800)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_590C)

    WaitForThreadExit(0x0101, 0x0002)
    WaitForThreadExit(0x0101, 0x0002)
    TerminateThread(0x0101, 0x00)
    TerminateThread(0x00F7, 0x00)
    TerminateThread(0x0104, 0x00)
    TerminateThread(0x0105, 0x00)

    @scena.Lambda('lambda_593E')
    def lambda_593E():
        CameraMove(14530, 4000, 39860, 2800)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_593E)

    @scena.Lambda('lambda_5956')
    def lambda_5956():
        OP_67(0, 8000, -10000, 2800)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_5956)

    Sleep(2500)

    ChrSetPos(0x00F7, 3830, 4000, 39090, 90)
    ChrSetPos(0x0101, 3830, 4000, 40090, 90)
    ChrSetPos(0x0105, 2830, 4000, 39090, 90)
    ChrSetPos(0x0104, 2830, 4000, 40090, 90)

    @scena.Lambda('lambda_59B7')
    def lambda_59B7():
        ChrMoveToRelative(0x00FE, 9600, 0, 0, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_59B7)

    Sleep(120)

    @scena.Lambda('lambda_59D7')
    def lambda_59D7():
        ChrMoveToRelative(0x00FE, 9600, 0, 0, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_59D7)

    Sleep(80)

    @scena.Lambda('lambda_59F7')
    def lambda_59F7():
        ChrMoveToRelative(0x00FE, 9400, 0, 0, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_59F7)

    Sleep(120)

    @scena.Lambda('lambda_5A17')
    def lambda_5A17():
        ChrMoveToRelative(0x00FE, 9400, 0, 0, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_5A17)

    WaitForThreadExit(0x0105, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)
    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x000A,
        (
            '#3100221155V然后拐了个弯后，\n',
            '看见那里的门关上了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_5A78')
    def lambda_5A78():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_5A78)

    ChrSetDirection(0x0105, 180, 400)

    @scena.Lambda('lambda_5A8D')
    def lambda_5A8D():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5A8D)

    ChrSetDirection(0x0104, 180, 400)

    ChrTalk(
        0x000A,
        (
            '#3100221156V所以我觉得他一定是\n',
            '从这里出去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3100221157V我觉得那是搭讪的好机会，\n',
            '就追上去了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000A, 180, 400)
    FadeOut(1000, 0, -1)
    ChrWalkTo(0x000A, 15000, 4000, 36760, 2000, 0x00)
    ChrSetRGBAMask(0x000A, 255, 255, 255, 0, 400)
    ChrSetFlags(0x000A, 0x0080)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/T3400._SN', 103, 0, 0)
    IdleLoop()

    Return()

# id: 0x001A offset: 0x5B4B
@scena.Code('func_1A_5B4B')
def func_1A_5B4B():
    @scena.Lambda('lambda_5B51')
    def lambda_5B51():
        ChrWalkTo(0x00FE, 2920, 4000, 50890, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_5B51)

    WaitForThreadExit(0x000A, 0x0001)

    @scena.Lambda('lambda_5B71')
    def lambda_5B71():
        ChrWalkTo(0x00FE, 2810, 4000, 39910, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_5B71)

    WaitForThreadExit(0x000A, 0x0001)

    @scena.Lambda('lambda_5B91')
    def lambda_5B91():
        ChrWalkTo(0x00FE, 15170, 4000, 39740, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_5B91)

    WaitForThreadExit(0x000A, 0x0001)
    ChrSetDirection(0x000A, 270, 400)

    Return()

# id: 0x001B offset: 0x5BB3
@scena.Code('func_1B_5BB3')
def func_1B_5BB3():
    @scena.Lambda('lambda_5BB9')
    def lambda_5BB9():
        ChrWalkTo(0x00FE, 14940, 4000, 38550, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_5BB9)

    WaitForThreadExit(0x00FE, 0x0001)

    @scena.Lambda('lambda_5BD9')
    def lambda_5BD9():
        ChrWalkTo(0x00FE, 15000, 4000, 36760, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_5BD9)

    WaitForThreadExit(0x00FE, 0x0001)
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 400)

    Return()

# id: 0x001C offset: 0x5BFF
@scena.Code('func_1C_5BFF')
def func_1C_5BFF():
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
        (0x00000000, 'loc_5C79'),
        (0x00000001, 'loc_5C7F'),
        (-1, 'loc_5C85'),
    )

    def _loc_5C79(): pass

    label('loc_5C79')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_5C85')

    def _loc_5C7F(): pass

    label('loc_5C7F')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_5C85')

    def _loc_5C85(): pass

    label('loc_5C85')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_5C93',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    Jump('loc_5C97')

    def _loc_5C93(): pass

    label('loc_5C93')

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    def _loc_5C97(): pass

    label('loc_5C97')

    Return()

# id: 0x001D offset: 0x5C98
@scena.Code('func_1D_5C98')
def func_1D_5C98():
    TalkBegin(0x00FF)
    Sleep(400)

    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
