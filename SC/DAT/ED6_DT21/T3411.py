import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T3411_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3411   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'T3411.x'
    header.mapIndex       = 1
    header.bgm            = 10
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
    ]

# id: 0x10001 offset: 0xEA
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
            talkScenaIndex      = 0x0009,
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
            talkScenaIndex      = 0x000A,
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
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            name                = '桑吉特',
            x                   = 54970,
            z                   = 0,
            y                   = -21440,
            direction           = 4,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
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
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '士兵维恩',
            x                   = 27480,
            z                   = 0,
            y                   = 1360,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
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
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            name                = '士兵埃克托尔',
            x                   = 560,
            z                   = 0,
            y                   = 1930,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '安敦',
            x                   = 25320,
            z                   = 4000,
            y                   = 83680,
            direction           = 0,
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
            y                   = 84320,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
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
            dword_10            = 6,
            chipIndex           = 6,
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
            talkScenaIndex      = 0x0013,
        ),
    )

# id: 0x10002 offset: 0x26A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x26A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x26A
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
            talkFunctionIndex   = 0x0008,
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
            talkFunctionIndex   = 0x0006,
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
            talkFunctionIndex   = 0x000B,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 25120,
            triggerZ            = 4000,
            triggerY            = 84320,
            triggerRange        = 1000,
            actorX              = 25120,
            actorZ              = 4500,
            actorY              = 84320,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0011,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 25320,
            triggerZ            = 4000,
            triggerY            = 83680,
            triggerRange        = 1000,
            actorX              = 25320,
            actorZ              = 5500,
            actorY              = 83680,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0011,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x31E
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_37E',
    )

    ChrSetPos(0x000A, 78750, 0, 26210, 270)
    ChrSetFlags(0x000A, 0x0010)
    ChrSetPos(0x000E, 77860, 0, 26210, 90)
    ChrSetFlags(0x000E, 0x0010)
    ChrClearFlags(0x0013, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0010, 0x0040)
    ChrClearFlags(0x0010, 0x0020)
    ChrClearFlags(0x0010, 0x0004)
    ChrSetFlags(0x0010, 0x0100)
    ChrSetFlags(0x0010, 0x0001)
    CreateThread(0x0010, 0x00, 0x06, func_02_66C)

    Jump('loc_57C')

    def _loc_37E(): pass

    label('loc_37E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_426',
    )

    ChrSetPos(0x0008, 111940, 0, 22150, 0)
    ChrSetFlags(0x0008, 0x0010)
    ChrSetPos(0x0009, 111940, 0, 23370, 180)
    ChrSetFlags(0x0009, 0x0010)
    ChrSetPos(0x000F, 77580, 0, 23520, 0)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x000D, 76130, 0, 24430, 45)
    ChrSetPos(0x000A, 79530, 0, 24930, 315)
    ChrSetFlags(0x000E, 0x0010)
    ChrClearFlags(0x0013, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0012, 0x0080)

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
            (Expr.PushLong, 0x15F90),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_57C')

    def _loc_426(): pass

    label('loc_426')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_4B5',
    )

    ChrSetPos(0x0009, 51170, 0, 28460, 0)
    ChrSetPos(0x000F, 2190, 0, 2570, 180)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x000D, 4950, 0, -2820, 45)
    CreateThread(0x000A, 0x00, 0x00, func_02_66C)
    ChrSetPos(0x000E, 15400, 0, 1400, 180)
    ChrClearFlags(0x0013, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0012, 0x0080)

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
            (Expr.PushLong, 0x15F90),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_57C')

    def _loc_4B5(): pass

    label('loc_4B5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 5, 0x1415)),
            Expr.Return,
        ),
        'loc_517',
    )

    ChrSetPos(0x0009, 51170, 0, 28460, 0)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x000A, 58330, 0, -22280, 90)
    ChrSetPos(0x000C, 94890, 0, -22010, 90)
    OP_64(0x01, 0x0001)
    OP_64(0x02, 0x0001)
    ChrSetPos(0x000E, 15400, 0, 1400, 180)
    CreateThread(0x000E, 0x00, 0x00, func_05_6D8)

    Jump('loc_57C')

    def _loc_517(): pass

    label('loc_517')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 3, 0x1413)),
            Expr.Return,
        ),
        'loc_56E',
    )

    ChrSetPos(0x0009, 51170, 0, 28460, 0)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x000C, 94890, 0, -22010, 90)
    CreateThread(0x000A, 0x00, 0x00, func_02_66C)
    CreateThread(0x000B, 0x00, 0x00, func_03_690)
    ChrSetPos(0x000E, 15400, 0, 1400, 180)
    CreateThread(0x000E, 0x00, 0x00, func_05_6D8)

    Jump('loc_57C')

    def _loc_56E(): pass

    label('loc_56E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_57C',
    )

    CreateThread(0x000A, 0x00, 0x00, func_02_66C)

    def _loc_57C(): pass

    label('loc_57C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_59B',
    )

    SetScenaFlags(ScenaFlag(0x0282, 3, 0x1413))

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x22),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MapSetFlags(0x02000000)
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    Event(0, func_14_2713)

    def _loc_59B(): pass

    label('loc_59B')

    Return()

# id: 0x0001 offset: 0x59C
@scena.Code('func_01_59C')
def func_01_59C():
    OP_1C(0x05, 0x00, 0x0019)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_5AF',
    )

    OP_64(0x03, 0x0001)

    Jump('loc_612')

    def _loc_5AF(): pass

    label('loc_5AF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_5C1',
    )

    OP_64(0x02, 0x0001)
    OP_64(0x04, 0x0001)

    Jump('loc_612')

    def _loc_5C1(): pass

    label('loc_5C1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_5D3',
    )

    OP_64(0x02, 0x0001)
    OP_64(0x04, 0x0001)

    Jump('loc_612')

    def _loc_5D3(): pass

    label('loc_5D3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 5, 0x1415)),
            Expr.Return,
        ),
        'loc_5E9',
    )

    OP_64(0x02, 0x0001)
    OP_64(0x03, 0x0001)
    OP_64(0x04, 0x0001)

    Jump('loc_612')

    def _loc_5E9(): pass

    label('loc_5E9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 3, 0x1413)),
            Expr.Return,
        ),
        'loc_603',
    )

    OP_64(0x01, 0x0001)
    OP_64(0x02, 0x0001)
    OP_64(0x03, 0x0001)
    OP_64(0x04, 0x0001)

    Jump('loc_612')

    def _loc_603(): pass

    label('loc_603')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_612',
    )

    OP_64(0x03, 0x0001)
    OP_64(0x04, 0x0001)

    def _loc_612(): pass

    label('loc_612')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_61F',
    )

    OP_10(0x11, 0x00)

    Jump('loc_62F')

    def _loc_61F(): pass

    label('loc_61F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 5, 0x1415)),
            Expr.Return,
        ),
        'loc_62C',
    )

    OP_10(0x11, 0x00)

    Jump('loc_62F')

    def _loc_62C(): pass

    label('loc_62C')

    OP_10(0x13, 0x00)

    def _loc_62F(): pass

    label('loc_62F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 2, 0x1412)),
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_649',
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

    def _loc_649(): pass

    label('loc_649')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_65A',
    )

    OP_1B(0x01, 0x00, 0x0017)

    def _loc_65A(): pass

    label('loc_65A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_66B',
    )

    OP_1B(0x00, 0x00, 0x0018)

    def _loc_66B(): pass

    label('loc_66B')

    Return()

# id: 0x0002 offset: 0x66C
@scena.Code('func_02_66C')
def func_02_66C():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_68F',
    )

    OP_8D(0x00FE, 56600, -23980, 64040, -26210, 2000)

    Jump('func_02_66C')

    def _loc_68F(): pass

    label('loc_68F')

    Return()

# id: 0x0003 offset: 0x690
@scena.Code('func_03_690')
def func_03_690():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_6B3',
    )

    OP_8D(0x00FE, 58110, -23110, 53730, -21470, 2000)

    Jump('func_03_690')

    def _loc_6B3(): pass

    label('loc_6B3')

    Return()

# id: 0x0004 offset: 0x6B4
@scena.Code('func_04_6B4')
def func_04_6B4():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_6D7',
    )

    OP_8D(0x00FE, 3140, -1230, 9860, -4460, 2000)

    Jump('func_04_6B4')

    def _loc_6D7(): pass

    label('loc_6D7')

    Return()

# id: 0x0005 offset: 0x6D8
@scena.Code('func_05_6D8')
def func_05_6D8():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_6FB',
    )

    OP_8D(0x00FE, 14200, 2000, 18960, 180, 2000)

    Jump('func_05_6D8')

    def _loc_6FB(): pass

    label('loc_6FB')

    Return()

# id: 0x0006 offset: 0x6FC
@scena.Code('func_06_6FC')
def func_06_6FC():
    Call(0, 0x0007)

    Return()

# id: 0x0007 offset: 0x701
@scena.Code('func_07_701')
def func_07_701():
    TalkBegin(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 3, 0x1413)),
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_739',
    )

    Call(6, 0x0006)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_728',
    )

    OP_A9(0xAC)
    TalkEnd(0x000C)

    Return()

    def _loc_728(): pass

    label('loc_728')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_739',
    )

    TalkEnd(0x000C)

    Return()

    def _loc_739(): pass

    label('loc_739')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_820',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_79C',
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

    Jump('loc_81D')

    def _loc_79C(): pass

    label('loc_79C')

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

    def _loc_81D(): pass

    label('loc_81D')

    Jump('loc_A6D')

    def _loc_820(): pass

    label('loc_820')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_8FC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_8AC',
    )

    ChrTalk(
        0x000C,
        (
            '不过因为有地震\n',
            '才去祈祷是很失礼的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '太自说自话\n',
            '女神就不会生气吗？',
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

    Jump('loc_8F9')

    def _loc_8AC(): pass

    label('loc_8AC')

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
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_8F9(): pass

    label('loc_8F9')

    Jump('loc_A6D')

    def _loc_8FC(): pass

    label('loc_8FC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 3, 0x1413)),
            Expr.Return,
        ),
        'loc_9B7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_955',
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

    Jump('loc_9B4')

    def _loc_955(): pass

    label('loc_955')

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
            '无论如何\n',
            '先要收拾一下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_9B4(): pass

    label('loc_9B4')

    Jump('loc_A6D')

    def _loc_9B7(): pass

    label('loc_9B7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_A6D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_A0A',
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

    Jump('loc_A6D')

    def _loc_A0A(): pass

    label('loc_A0A')

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

    def _loc_A6D(): pass

    label('loc_A6D')

    TalkEnd(0x000C)

    Return()

# id: 0x0008 offset: 0xA71
@scena.Code('func_08_A71')
def func_08_A71():
    Call(0, 0x0009)

    Return()

# id: 0x0009 offset: 0xA76
@scena.Code('func_09_A76')
def func_09_A76():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_B71',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_AF0',
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

    Jump('loc_B6E')

    def _loc_AF0(): pass

    label('loc_AF0')

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

    def _loc_B6E(): pass

    label('loc_B6E')

    Jump('loc_D52')

    def _loc_B71(): pass

    label('loc_B71')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_C2A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_BC4',
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

    Jump('loc_C27')

    def _loc_BC4(): pass

    label('loc_BC4')

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

    def _loc_C27(): pass

    label('loc_C27')

    Jump('loc_D52')

    def _loc_C2A(): pass

    label('loc_C2A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 3, 0x1413)),
            Expr.Return,
        ),
        'loc_CC8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 4, 0x1414)),
            Expr.Return,
        ),
        'loc_C7C',
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

    Jump('loc_CC5')

    def _loc_C7C(): pass

    label('loc_C7C')

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

    def _loc_CC5(): pass

    label('loc_CC5')

    Jump('loc_D52')

    def _loc_CC8(): pass

    label('loc_CC8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_D52',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_D16',
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

    Jump('loc_D52')

    def _loc_D16(): pass

    label('loc_D16')

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

    def _loc_D52(): pass

    label('loc_D52')

    TalkEnd(0x0008)

    Return()

# id: 0x000A offset: 0xD56
@scena.Code('func_0A_D56')
def func_0A_D56():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 4, 0x1414)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 3, 0x1413)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_D67',
    )

    Call(0, 0x0015)

    Return()

    def _loc_D67(): pass

    label('loc_D67')

    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_E42',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_DC3',
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

    Jump('loc_E3F')

    def _loc_DC3(): pass

    label('loc_DC3')

    ChrTalk(
        0x0009,
        (
            '地震结束的宣告\n',
            '已经从中央工房发出了。',
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
            '嗯，看来不是单纯的\n',
            '自然现象。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_E3F(): pass

    label('loc_E3F')

    Jump('loc_1160')

    def _loc_E42(): pass

    label('loc_E42')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_F15',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_EB5',
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

    Jump('loc_F12')

    def _loc_EB5(): pass

    label('loc_EB5')

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

    def _loc_F12(): pass

    label('loc_F12')

    Jump('loc_1160')

    def _loc_F15(): pass

    label('loc_F15')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_FA2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_F58',
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

    Jump('loc_F9F')

    def _loc_F58(): pass

    label('loc_F58')

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

    def _loc_F9F(): pass

    label('loc_F9F')

    Jump('loc_1160')

    def _loc_FA2(): pass

    label('loc_FA2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 3, 0x1413)),
            Expr.Return,
        ),
        'loc_10C6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_FFF',
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

    Jump('loc_10C3')

    def _loc_FFF(): pass

    label('loc_FFF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 5, 0x1415)),
            Expr.Return,
        ),
        'loc_106A',
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

    Jump('loc_10C0')

    def _loc_106A(): pass

    label('loc_106A')

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

    def _loc_10C0(): pass

    label('loc_10C0')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_10C3(): pass

    label('loc_10C3')

    Jump('loc_1160')

    def _loc_10C6(): pass

    label('loc_10C6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_1160',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_1128',
    )

    ChrTalk(
        0x0009,
        (
            '登上里面的台阶\n',
            '就能到达『亚宁堡』的\n',
            '的上层。',
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

    Jump('loc_1160')

    def _loc_1128(): pass

    label('loc_1128')

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

    def _loc_1160(): pass

    label('loc_1160')

    TalkEnd(0x0009)

    Return()

# id: 0x000B offset: 0x1164
@scena.Code('func_0B_1164')
def func_0B_1164():
    Call(0, 0x000C)

    Return()

# id: 0x000C offset: 0x1169
@scena.Code('func_0C_1169')
def func_0C_1169():
    TalkBegin(0x000D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_1206',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_11C5',
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
            '哎呀，人真是\n',
            '真是一场大灾难啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1203')

    def _loc_11C5(): pass

    label('loc_11C5')

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

    def _loc_1203(): pass

    label('loc_1203')

    Jump('loc_14AD')

    def _loc_1206(): pass

    label('loc_1206')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_12C5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_126B',
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

    Jump('loc_12C2')

    def _loc_126B(): pass

    label('loc_126B')

    ChrTalk(
        0x000D,
        (
            '必须在地震来临的时候\n',
            '去向女神祈祷。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '那场地震也一定是\n',
            '因为那是女神的意志。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    def _loc_12C2(): pass

    label('loc_12C2')

    Jump('loc_14AD')

    def _loc_12C5(): pass

    label('loc_12C5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_136D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_132A',
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

    Jump('loc_136A')

    def _loc_132A(): pass

    label('loc_132A')

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

    def _loc_136A(): pass

    label('loc_136A')

    Jump('loc_14AD')

    def _loc_136D(): pass

    label('loc_136D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 3, 0x1413)),
            Expr.Return,
        ),
        'loc_1401',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_13C6',
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

    Jump('loc_13FE')

    def _loc_13C6(): pass

    label('loc_13C6')

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

    def _loc_13FE(): pass

    label('loc_13FE')

    Jump('loc_14AD')

    def _loc_1401(): pass

    label('loc_1401')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_14AD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_145C',
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

    Jump('loc_14AD')

    def _loc_145C(): pass

    label('loc_145C')

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
            '『亚宁堡』的威容。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    def _loc_14AD(): pass

    label('loc_14AD')

    TalkEnd(0x000D)

    Return()

# id: 0x000D offset: 0x14B1
@scena.Code('func_0D_14B1')
def func_0D_14B1():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_1568',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_151C',
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

    Jump('loc_1565')

    def _loc_151C(): pass

    label('loc_151C')

    ChrTalk(
        0x000A,
        (
            '啊？　我这个人\n',
            '男人运是不是很坏～？',
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
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_1565(): pass

    label('loc_1565')

    Jump('loc_1826')

    def _loc_1568(): pass

    label('loc_1568')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_1672',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_15DB',
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

    Jump('loc_166F')

    def _loc_15DB(): pass

    label('loc_15DB')

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
            '虽然他不算个年轻男子，\n',
            '但还是相当英俊的呢～',
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

    def _loc_166F(): pass

    label('loc_166F')

    Jump('loc_1826')

    def _loc_1672(): pass

    label('loc_1672')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_1745',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_16D9',
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

    Jump('loc_1742')

    def _loc_16D9(): pass

    label('loc_16D9')

    ChrTalk(
        0x000A,
        (
            '唔～真可惜。\n',
            '明明是个很帅的人',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '不过既然是要特别当心的人就算了。\n',
            '我就放弃他去找其他的男人吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_1742(): pass

    label('loc_1742')

    Jump('loc_1826')

    def _loc_1745(): pass

    label('loc_1745')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 3, 0x1413)),
            Expr.Return,
        ),
        'loc_1786',
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

    Jump('loc_1826')

    def _loc_1786(): pass

    label('loc_1786')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_1826',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_17F7',
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

    Jump('loc_1826')

    def _loc_17F7(): pass

    label('loc_17F7')

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

    def _loc_1826(): pass

    label('loc_1826')

    TalkEnd(0x000A)

    Return()

# id: 0x000E offset: 0x182A
@scena.Code('func_0E_182A')
def func_0E_182A():
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
        'loc_19E7',
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
        'loc_18B6',
    )

    FadeIn(300, 0)
    OP_0D()
    OP_A9(0xAD)
    OP_56(0x00)
    TalkEnd(0x000B)

    Return()

    def _loc_18B6(): pass

    label('loc_18B6')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_19C4',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x12),
            (Expr.PushLong, 0x4B0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_198F',
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
        'loc_1981',
    )

    If(
        (
            (Expr.Eval, "OP_AC(0x0007)"),
            Expr.Return,
        ),
        'loc_1955',
    )

    Jump('loc_1981')

    def _loc_1955(): pass

    label('loc_1955')

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

    def _loc_1981(): pass

    label('loc_1981')

    OP_56(0x00)
    FadeIn(1000, 0)

    Jump('loc_19B5')

    def _loc_198F(): pass

    label('loc_198F')

    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            '没有足够的米拉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeIn(300, 0)
    def _loc_19B5(): pass

    label('loc_19B5')

    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x000B)

    Return()

    def _loc_19C4(): pass

    label('loc_19C4')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_19DE',
    )

    FadeIn(300, 0)
    TalkEnd(0x000B)

    Return()

    def _loc_19DE(): pass

    label('loc_19DE')

    FadeIn(300, 0)

    def _loc_19E7(): pass

    label('loc_19E7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_1A72',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_1A26',
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

    Jump('loc_1A6F')

    def _loc_1A26(): pass

    label('loc_1A26')

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

    def _loc_1A6F(): pass

    label('loc_1A6F')

    Jump('loc_1D20')

    def _loc_1A72(): pass

    label('loc_1A72')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_1B5A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_1AD9',
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
            '不过现在看到顾客吃菜的\n',
            '一瞬间心里也还是七上八下的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B57')

    def _loc_1AD9(): pass

    label('loc_1AD9')

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
            '不过现在看到顾客吃菜的\n',
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

    def _loc_1B57(): pass

    label('loc_1B57')

    Jump('loc_1D20')

    def _loc_1B5A(): pass

    label('loc_1B5A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_1B9D',
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

    Jump('loc_1D20')

    def _loc_1B9D(): pass

    label('loc_1B9D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 3, 0x1413)),
            Expr.Return,
        ),
        'loc_1C7A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 5, 0x1415)),
            Expr.Return,
        ),
        'loc_1C24',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_1BDA',
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

    Jump('loc_1C21')

    def _loc_1BDA(): pass

    label('loc_1BDA')

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
            '我的新菜谱～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_1C21(): pass

    label('loc_1C21')

    Jump('loc_1C77')

    def _loc_1C24(): pass

    label('loc_1C24')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_1C42',
    )

    ChrTalk(
        0x00FE,
        (
            '唉～真没办法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C77')

    def _loc_1C42(): pass

    label('loc_1C42')

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

    def _loc_1C77(): pass

    label('loc_1C77')

    Jump('loc_1D20')

    def _loc_1C7A(): pass

    label('loc_1C7A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_1D20',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_1CE2',
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
            '我就开发了新菜谱哦～',
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

    Jump('loc_1D20')

    def _loc_1CE2(): pass

    label('loc_1CE2')

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

    def _loc_1D20(): pass

    label('loc_1D20')

    TalkEnd(0x000B)

    Return()

# id: 0x000F offset: 0x1D24
@scena.Code('func_0F_1D24')
def func_0F_1D24():
    TalkBegin(0x000E)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_1E20',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_1D84',
    )

    ChrTalk(
        0x00FE,
        (
            '我就在大圣堂里，\n',
            '你随时都能来。',
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

    Jump('loc_1E1D')

    def _loc_1D84(): pass

    label('loc_1D84')

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

    def _loc_1E1D(): pass

    label('loc_1E1D')

    Jump('loc_20B2')

    def _loc_1E20(): pass

    label('loc_1E20')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_1EF5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_1E91',
    )

    ChrTalk(
        0x00FE,
        (
            '我再来为您祈祷',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '当我们迷失道路时，\n',
            '请您为我们指路……',
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

    Jump('loc_1EF2')

    def _loc_1E91(): pass

    label('loc_1E91')

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
            '并且请您在高天之上\n',
            '永远注视我们……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    def _loc_1EF2(): pass

    label('loc_1EF2')

    Jump('loc_20B2')

    def _loc_1EF5(): pass

    label('loc_1EF5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_1F89',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_1F3B',
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
            '开始礼拜了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F86')

    def _loc_1F3B(): pass

    label('loc_1F3B')

    ChrTalk(
        0x00FE,
        (
            '好像已经\n',
            '整理完了呢。',
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

    def _loc_1F86(): pass

    label('loc_1F86')

    Jump('loc_20B2')

    def _loc_1F89(): pass

    label('loc_1F89')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 3, 0x1413)),
            Expr.Return,
        ),
        'loc_1FFB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_1FC6',
    )

    ChrTalk(
        0x00FE,
        (
            '不过又给\n',
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

    Jump('loc_1FF8')

    def _loc_1FC6(): pass

    label('loc_1FC6')

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

    def _loc_1FF8(): pass

    label('loc_1FF8')

    Jump('loc_20B2')

    def _loc_1FFB(): pass

    label('loc_1FFB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_20B2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_204A',
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

    Jump('loc_20B2')

    def _loc_204A(): pass

    label('loc_204A')

    ChrTalk(
        0x000E,
        (
            '我是从大圣堂来\n',
            '为士兵们的祈祷的……',
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

    def _loc_20B2(): pass

    label('loc_20B2')

    TalkEnd(0x000E)

    Return()

# id: 0x0010 offset: 0x20B6
@scena.Code('func_10_20B6')
def func_10_20B6():
    TalkBegin(0x000F)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_20FC',
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

    Jump('loc_227A')

    def _loc_20FC(): pass

    label('loc_20FC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_21CA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_214E',
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

    Jump('loc_21C7')

    def _loc_214E(): pass

    label('loc_214E')

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

    def _loc_21C7(): pass

    label('loc_21C7')

    Jump('loc_227A')

    def _loc_21CA(): pass

    label('loc_21CA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 3, 0x1413)),
            Expr.Return,
        ),
        'loc_227A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_2233',
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
            '所以离开工作岗位\n',
            '到里面来帮忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_227A')

    def _loc_2233(): pass

    label('loc_2233')

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

    def _loc_227A(): pass

    label('loc_227A')

    TalkEnd(0x000F)

    Return()

# id: 0x0011 offset: 0x227E
@scena.Code('func_11_227E')
def func_11_227E():
    Call(0, 0x0012)

    Return()

# id: 0x0012 offset: 0x2283
@scena.Code('func_12_2283')
def func_12_2283():
    UnlockAchievement(0x01, 0x000B, 0x00)
    TalkBegin(0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_231A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_22D9',
    )

    ChrTalk(
        0x0010,
        (
            '还是不能在\n',
            '这种地方浪费人生！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '总、总之要回王都去！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2317')

    def _loc_22D9(): pass

    label('loc_22D9')

    ChrTalk(
        0x0010,
        (
            '不、不能在\n',
            '这种地方浪费人生！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '好，赶快回王都去！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    def _loc_2317(): pass

    label('loc_2317')

    Jump('loc_24C8')

    def _loc_231A(): pass

    label('loc_231A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_23EC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_236F',
    )

    ChrTalk(
        0x0010,
        (
            '这么躺着\n',
            '总觉得很烦躁。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '我能就这样\n',
            '每天在这里浪费时间吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23E9')

    def _loc_236F(): pass

    label('loc_236F')

    ChrTalk(
        0x0010,
        (
            '总觉得这么躺着\n',
            '心情就会烦躁。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '我、我能就这样\n',
            '每天在这里浪费时间吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '不知不觉间一辈子\n',
            '就过去了，真可怕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    def _loc_23E9(): pass

    label('loc_23E9')

    Jump('loc_24C8')

    def _loc_23EC(): pass

    label('loc_23EC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_24C8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_2436',
    )

    ChrTalk(
        0x0010,
        (
            '啊，利库斯，告诉我！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '我的存在意义\n',
            '到底是什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24C8')

    def _loc_2436(): pass

    label('loc_2436')

    ChrTalk(
        0x0010,
        (
            '诞辰庆典就失恋……\n',
            '有地震就差点死……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '真悲惨……\n',
            '我连爬起来的力气也没有了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '啊，利库斯，告诉我！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '我的存在意义\n',
            '到底是什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    def _loc_24C8(): pass

    label('loc_24C8')

    TalkEnd(0x0010)

    Return()

# id: 0x0013 offset: 0x24CC
@scena.Code('func_13_24CC')
def func_13_24CC():
    TalkBegin(0x0013)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_258A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_2536',
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
            '反正不管怎样，你\n',
            '有精神了，我挺高兴的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2587')

    def _loc_2536(): pass

    label('loc_2536')

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
            '总之我已经装备\n',
            '要回王都了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    def _loc_2587(): pass

    label('loc_2587')

    Jump('loc_270F')

    def _loc_258A(): pass

    label('loc_258A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_2627',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_25C2',
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

    Jump('loc_2624')

    def _loc_25C2(): pass

    label('loc_25C2')

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

    def _loc_2624(): pass

    label('loc_2624')

    Jump('loc_270F')

    def _loc_2627(): pass

    label('loc_2627')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_270F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_26AF',
    )

    ChrTalk(
        0x00FE,
        (
            '抱歉啊，\n',
            '我阻碍你们走路了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '时常开始寻找自我\n',
            '是我的伙伴的臭毛病。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没关系的，过几天他腻了\n',
            '就肯定会复活。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_270F')

    def _loc_26AF(): pass

    label('loc_26AF')

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

    def _loc_270F(): pass

    label('loc_270F')

    TalkEnd(0x0013)

    Return()

# id: 0x0014 offset: 0x2713
@scena.Code('func_14_2713')
def func_14_2713():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2724',
    )

    Call(0, 0x0016)

    def _loc_2724(): pass

    label('loc_2724')

    EventBegin(0x00)
    OP_4A(0x0008, 255)
    ChrSetPos(0x0008, 6790, 0, 2810, 180)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0101, 6930, 0, 900, 0)
    ChrSetPos(0x00F7, 5740, 0, 890, 0)
    ChrSetPos(0x0105, 6640, 0, -190, 0)
    ChrSetPos(0x0104, 5510, 0, -230, 0)
    ChrSetFlags(0x000D, 0x0080)
    ChrSetFlags(0x000E, 0x0080)
    OP_4A(0x000D, 255)
    OP_4A(0x000E, 255)
    ChrTurnDirection(0x000D, 0x0008, 0)
    CameraMove(6790, 0, 1300, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#2150221020V#5P真是的……\n',
            '游击士真是莫名其妙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2150221021V#5P如你们所见，大家因为收拾地震的\n',
            '残局都忙得不可开交。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2150221022V#5P要调查的话能不能过会儿？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_2909',
    )

    ChrTalk(
        0x0106,
        (
            '#0050221023V#053F#6P抱歉，我们也是为了工作。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050221024V#050F不会妨碍你们整理的，\n',
            '能不能允许我们调查情况？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2974')

    def _loc_2909(): pass

    label('loc_2909')

    ChrTalk(
        0x0103,
        (
            '#0030221025V#027F#6P抱歉，我们也是在工作。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030221026V不会妨碍你们整理的，\n',
            '能不能允许我们调查情况？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2974(): pass

    label('loc_2974')

    ChrTalk(
        0x0008,
        (
            '#2150221027V#5P呼，如果没司令部的指示的话\n',
            '我已经拒绝你们了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2150221028V#5P我有紧急的公务在身，\n',
            '关于地震的发生情况\n',
            '你们去找塔尔瓦托副队长。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2150221029V#5P应该在前面房间\n',
            '深处的仓库里整理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010221030V#1006F#2P明白了，是塔尔瓦托副队长吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2150221031V#5P请尽量不要妨碍其他\n',
            '人的整理工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2150221032V#5P那我就先告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0008, 90, 600)

    @scena.Lambda('lambda_2AE2')
    def lambda_2AE2():
        ChrWalkTo(0x0008, 22720, 0, 2410, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2AE2)

    @scena.Lambda('lambda_2AFD')
    def lambda_2AFD():
        CameraMove(18030, 0, 2160, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2AFD)

    @scena.Lambda('lambda_2B15')
    def lambda_2B15():
        OP_67(0, 8000, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2B15)

    @scena.Lambda('lambda_2B2D')
    def lambda_2B2D():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_2B2D')

    DispatchAsync2(0x0101, 0x0001, lambda_2B2D)

    @scena.Lambda('lambda_2B3E')
    def lambda_2B3E():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_2B3E')

    DispatchAsync2(0x00F7, 0x0001, lambda_2B3E)

    @scena.Lambda('lambda_2B4F')
    def lambda_2B4F():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_2B4F')

    DispatchAsync2(0x0105, 0x0001, lambda_2B4F)

    @scena.Lambda('lambda_2B60')
    def lambda_2B60():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_2B60')

    DispatchAsync2(0x0104, 0x0001, lambda_2B60)

    WaitForThreadExit(0x0101, 0x0002)
    WaitForThreadExit(0x0101, 0x0003)
    WaitForThreadExit(0x0008, 0x0001)
    ChrSetDirection(0x0008, 17, 600)
    ChrWalkTo(0x0008, 22860, 0, 3260, 3000, 0x00)
    PlaySE(6, 0x00, 0x64)
    OP_72(0x0001, 0x0010)
    OP_72(0x0001, 0x0800)
    OP_6F(0x0001, 0)
    OP_70(0x0001, 19)
    OP_6F(0x0001, 19)
    OP_73(0x0001)
    ChrWalkTo(0x0008, 23260, 0, 5530, 2000, 0x00)
    PlaySE(7, 0x00, 0x64)
    OP_6F(0x0001, 19)
    OP_70(0x0001, 0)
    OP_73(0x0001)
    OP_71(0x0001, 0x0010)
    OP_71(0x0001, 0x0800)
    ChrSetFlags(0x0008, 0x0080)

    @scena.Lambda('lambda_2BFB')
    def lambda_2BFB():
        CameraMove(6550, 0, 600, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2BFB)

    @scena.Lambda('lambda_2C13')
    def lambda_2C13():
        OP_67(0, 8000, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2C13)

    WaitForThreadExit(0x0101, 0x0002)
    WaitForThreadExit(0x0101, 0x0003)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x00F7, 0x01)
    TerminateThread(0x0105, 0x01)
    TerminateThread(0x0104, 0x01)
    ChrTurnDirection(0x0101, 0x0104, 400)
    ChrSetDirection(0x0105, 0, 400)
    ChrTurnDirection(0x0104, 0x0101, 400)

    ChrTalk(
        0x0101,
        (
            '#0010221033V#1015F#5P唔，好像很忙呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010221034V我们也帮忙\n',
            '一起整理吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_2D16',
    )

    ChrTalk(
        0x0106,
        (
            '#0050221035V#053F#6P别多管闲事了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050221036V#050F好歹也算是军事施设。\n',
            '有可能有机密文件什么的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2D85')

    def _loc_2D16(): pass

    label('loc_2D16')

    ChrTalk(
        0x0103,
        (
            '#0030221037V#020F#6P算了，好歹也算是军事施设，\n',
            '还是别多管闲事了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030221038V有可能还有机密文件什么的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2D85(): pass

    label('loc_2D85')

    ChrTalk(
        0x0101,
        (
            '#0010221039V#1007F#5P嗯～也对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060221040V#043F不过被害情况\n',
            '和蔡斯市的地震不同呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060221041V那时东西没散得\n',
            '这么乱的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040221042V#035F嗯，关于这个差别\n',
            '也应该确认一下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040221043V#030F接下来就是怪异人物的目击情报了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010221044V#1002F#5P那个戴墨镜的男人……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010221045V详细情况要首先问一下那个\n',
            '被称为副队长的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0086, 0x04, 0x02)
    OP_28(0x0086, 0x04, 0x08)
    OP_28(0x0086, 0x01, 0x0001)
    FadeOut(1000, 0, -1)
    OP_0D()
    ChrSetPos(0x0101, 5460, 0, 420, 0)
    ChrSetPos(0x00F7, 5460, 0, 420, 0)
    ChrSetPos(0x0105, 5460, 0, 420, 0)
    ChrSetPos(0x0104, 5460, 0, 420, 0)
    CameraMove(5460, 0, 420, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    OP_4B(0x000D, 255)
    OP_4B(0x000E, 255)
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)
    MapSetFlags(0x02000000)

    Return()

# id: 0x0015 offset: 0x2FA4
@scena.Code('func_15_2FA4')
def func_15_2FA4():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2FBE',
    )

    Call(0, 0x0016)
    FadeIn(0, 0)

    def _loc_2FBE(): pass

    label('loc_2FBE')

    EventBegin(0x00)
    OP_4A(0x0009, 255)
    Fade(1000)
    ChrSetPos(0x0101, 51640, 0, 26840, 0)
    ChrSetPos(0x00F7, 50500, 0, 26720, 0)
    ChrSetPos(0x0105, 51710, 0, 25760, 0)
    ChrSetPos(0x0104, 50580, 0, 25500, 0)
    CameraMove(51270, 0, 28050, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(
        0x0009,
        (
            '#3080221046V#5P哎呀哎呀……\n',
            '全部整理完是很辛苦的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3080221047V#5P得在黄昏前做完……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010221048V#1011F#2P那个……\n',
            '抱歉，在百忙之中打扰你。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrSetDirection(0x0009, 180, 400)

    ChrTalk(
        0x0009,
        (
            '#3080221049V#5P啊，你们是……',
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
            '艾丝蒂尔一行介绍了自己的游击士身份之后\n',
            '说明了自己是来调查地震的事的。',
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
            '#3080221050V#5P是吗，辛苦你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3080221051V#5P你们想了解\n',
            '地震的发生情况吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_3237',
    )

    ChrTalk(
        0x0106,
        (
            '#0050221052V#050F#6P嗯，我们想听听详细情况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3269')

    def _loc_3237(): pass

    label('loc_3237')

    ChrTalk(
        0x0103,
        (
            '#0030221053V#020F#6P嗯，我们想听听详细情况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3269(): pass

    label('loc_3269')

    ChrTalk(
        0x0009,
        (
            '#3080221054V#5P明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3080221055V#5P地震发生于下午１点左右……\n',
            '大概是２小时前。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3080221056V#5P能让堆积的木箱\n',
            '倒塌的摇晃\n',
            '持续了约３０秒吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010221057V#1004F#2P咦，那和\n',
            '沃尔费堡垒的地震比起来……',
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

    SetMessageWindowPos(-1, 50, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            0x18,
            (TxtCtl.SetColor, 0x5),
            '拿这次的地震和沃尔费堡垒的地震比？',
            TxtCtl.Enter,
        ),
    )

    Menu(
        0,
        -1,
        150,
        0,
        (
            TXT(0x00, '【摇晃的强度大】\n'),
            TXT(0x01, '【摇晃的时间长】\n'),
            TXT(0x02, '【两者都有】\n'),
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
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_3405'),
        (0x00000001, 'loc_345B'),
        (0x00000002, 'loc_34B1'),
        (-1, 'loc_3508'),
    )

    def _loc_3405(): pass

    label('loc_3405')

    OP_2B(0x0085, 0x0001)

    ChrTalk(
        0x0105,
        (
            '#0060221058V#043F嗯，是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060221059V还有摇晃的时间\n',
            '好象也变长了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3508')

    def _loc_345B(): pass

    label('loc_345B')

    OP_2B(0x0085, 0x0001)

    ChrTalk(
        0x0105,
        (
            '#0060221058V#043F嗯，是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060221061V还有摇晃的强度\n',
            '好象也变大了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3508')

    def _loc_34B1(): pass

    label('loc_34B1')

    OP_2B(0x0085, 0x0003)

    ChrTalk(
        0x0105,
        (
            '#0060211048V#047F是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060221063V#042F强度也变大了，\n',
            '时间也变长了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3508')

    def _loc_3508(): pass

    label('loc_3508')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_358E',
    )

    ChrTalk(
        0x0106,
        (
            '#0050221064V#555F#6P还有我们碰到的\n',
            '在蔡斯市的地震……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050221065V不管从强度还是时间来看\n',
            '都应该是处于两者中间的位置。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3608')

    def _loc_358E(): pass

    label('loc_358E')

    ChrTalk(
        0x0103,
        (
            '#0030221066V#022F#6P还有我们遇到的\n',
            '蔡斯市的地震……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030221067V不管从强度还是时间来看\n',
            '都应该是处于两者中间的位置。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3608(): pass

    label('loc_3608')

    ChrTalk(
        0x0104,
        (
            '#0040221068V#035F#7P就是说，这种局部的地震\n',
            '每一次都会变得更危险。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040221069V#030F或许可以这么说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010221070V#1020F#2P那、那岂不是不好办了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0009, 180, 400)

    ChrTalk(
        0x0009,
        (
            '#3080221071V#5P事态确实很严峻呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3080221072V#5P不过只要是自然现象\n',
            '就没办法防止了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3080221073V#5P游击士协会\n',
            '有什么对策吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010221074V#1007F#2P不，还不能确定，\n',
            '不过稍微有点线索。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010221075V#1002F另外地震前后\n',
            '有没有发生什么奇怪的事？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010221076V比如发现可疑人物什么的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3080221077V#5P可疑人物……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3080221078V#5P我记得昨天切斯利说\n',
            '他看到了一个怪异的男人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3080221079V#5P他正在整理屋顶，\n',
            '详细情况你们可以去问他。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_38B6',
    )

    ChrTalk(
        0x0106,
        (
            '#0050221080V#051F#6P明白了。\n',
            '屋顶的切斯利是吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_38EB')

    def _loc_38B6(): pass

    label('loc_38B6')

    ChrTalk(
        0x0103,
        (
            '#0030221081V#020F#6P明白了。\n',
            '屋顶的切斯利是吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_38EB(): pass

    label('loc_38EB')

    ChrTalk(
        0x0101,
        (
            '#0010221082V#1006F#2P感谢你的帮助。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3080221083V#5P不不。\n',
            '你们才辛苦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0009, 0, 400)
    OP_4B(0x0009, 255)
    SetScenaFlags(ScenaFlag(0x0282, 4, 0x1414))
    OP_28(0x0086, 0x01, 0x0002)
    OP_28(0x0086, 0x01, 0x0004)
    EventEnd(0x00)
    MapSetFlags(0x02000000)

    Return()

# id: 0x0016 offset: 0x395E
@scena.Code('func_16_395E')
def func_16_395E():
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
        (0x00000000, 'loc_39D8'),
        (0x00000001, 'loc_39DE'),
        (-1, 'loc_39E4'),
    )

    def _loc_39D8(): pass

    label('loc_39D8')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_39E4')

    def _loc_39DE(): pass

    label('loc_39DE')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_39E4')

    def _loc_39E4(): pass

    label('loc_39E4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_39F2',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    Jump('loc_39F6')

    def _loc_39F2(): pass

    label('loc_39F2')

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    def _loc_39F6(): pass

    label('loc_39F6')

    Return()

# id: 0x0017 offset: 0x39F7
@scena.Code('func_17_39F7')
def func_17_39F7():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 3, 0x1413)),
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3B70',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3A68',
    )

    ChrTalk(
        0x0101,
        (
            '#0010221318V<FIXME>#1000F王都側に用事はないよね。\n',
            '早く聞き込みを済ませましょ。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3B52')

    def _loc_3A68(): pass

    label('loc_3A68')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_3AE0',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3A85',
    )

    ChrTurnDirection(0x0106, 0x0001, 400)

    Jump('loc_3A8C')

    def _loc_3A85(): pass

    label('loc_3A85')

    ChrTurnDirection(0x0106, 0x0000, 400)

    def _loc_3A8C(): pass

    label('loc_3A8C')

    ChrTalk(
        0x0106,
        (
            '#0050221319V<FIXME>#050F王都側に用事はねえ。\n',
            'さっさと聞き込みを済ませるぞ。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3B52')

    def _loc_3AE0(): pass

    label('loc_3AE0')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3AF6',
    )

    ChrTurnDirection(0x0103, 0x0001, 400)

    Jump('loc_3AFD')

    def _loc_3AF6(): pass

    label('loc_3AF6')

    ChrTurnDirection(0x0103, 0x0000, 400)

    def _loc_3AFD(): pass

    label('loc_3AFD')

    ChrTalk(
        0x0103,
        (
            '#0030221320V<FIXME>#027F王都側に用事はないわ。\n',
            'さっさと聞き込みを済ませましょ。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3B52(): pass

    label('loc_3B52')

    ChrMoveToRelative(0x0000, -1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Jump('loc_3CA8')

    def _loc_3B70(): pass

    label('loc_3B70')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3CA8',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_3C07',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3B9B',
    )

    ChrTurnDirection(0x0106, 0x0001, 400)

    Jump('loc_3BA2')

    def _loc_3B9B(): pass

    label('loc_3B9B')

    ChrTurnDirection(0x0106, 0x0000, 400)

    def _loc_3BA2(): pass

    label('loc_3BA2')

    ChrTalk(
        0x0106,
        (
            '#0050221321V#050F前面是格兰赛尔地区。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050220142V没时间去别的地方了。\n',
            '现在还是乖乖回去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3C88')

    def _loc_3C07(): pass

    label('loc_3C07')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3C1D',
    )

    ChrTurnDirection(0x0103, 0x0001, 400)

    Jump('loc_3C24')

    def _loc_3C1D(): pass

    label('loc_3C1D')

    ChrTurnDirection(0x0103, 0x0000, 400)

    def _loc_3C24(): pass

    label('loc_3C24')

    ChrTalk(
        0x0103,
        (
            '#0030221323V#020F前面是格兰赛尔地区。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030220144V没时间去其它的地方了，\n',
            '现在还是乖乖回去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_3C88(): pass

    label('loc_3C88')

    ChrMoveToRelative(0x0000, -1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)
    MapSetFlags(0x02000000)

    def _loc_3CA8(): pass

    label('loc_3CA8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4029',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3DBC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_3D2E',
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

    Jump('loc_3DB9')

    def _loc_3D2E(): pass

    label('loc_3D2E')

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

    def _loc_3DB9(): pass

    label('loc_3DB9')

    Jump('loc_400E')

    def _loc_3DBC(): pass

    label('loc_3DBC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_3EEE',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3DD9',
    )

    ChrTurnDirection(0x0106, 0x0001, 400)

    Jump('loc_3DE0')

    def _loc_3DD9(): pass

    label('loc_3DD9')

    ChrTurnDirection(0x0106, 0x0000, 400)

    def _loc_3DE0(): pass

    label('loc_3DE0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_3E46',
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

    Jump('loc_3EEB')

    def _loc_3E46(): pass

    label('loc_3E46')

    ChrTalk(
        0x0106,
        (
            '#0050241185V#050F虽然都到了这里了，\n',
            '我们还是乘定期船去王都吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050241186V不过我记得雾香应该为\n',
            '我们准备好了船票。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050241187V至少移动的时候要\n',
            '好好享受。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    def _loc_3EEB(): pass

    label('loc_3EEB')

    Jump('loc_400E')

    def _loc_3EEE(): pass

    label('loc_3EEE')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3F04',
    )

    ChrTurnDirection(0x0103, 0x0001, 400)

    Jump('loc_3F0B')

    def _loc_3F04(): pass

    label('loc_3F04')

    ChrTurnDirection(0x0103, 0x0000, 400)

    def _loc_3F0B(): pass

    label('loc_3F0B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_3F71',
    )

    ChrTalk(
        0x0103,
        (
            '#0030241188V#020F雾香小姐应该\n',
            '为我们准备好了船票。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030241189V我们乘定期船去王都吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_400E')

    def _loc_3F71(): pass

    label('loc_3F71')

    ChrTalk(
        0x0103,
        (
            '#0030241190V#020F虽然已经到了这里，\n',
            '我们还是乘定期船去王都吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030241191V雾香小姐也\n',
            '为我们准备好了船票。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030241192V至少移动的时候要\n',
            '好好享受。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))

    def _loc_400E(): pass

    label('loc_400E')

    ChrMoveToRelative(0x0000, -1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_4029(): pass

    label('loc_4029')

    Return()

# id: 0x0018 offset: 0x402A
@scena.Code('func_18_402A')
def func_18_402A():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 0, 0x1638)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_41CC',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_40A7',
    )

    ChrTalk(
        0x0108,
        (
            '#0080291614V#070F哟，前面是蔡斯地区了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080271276V现在没空去其他的地方了，\n',
            '赶快回去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_41B1')

    def _loc_40A7(): pass

    label('loc_40A7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_412C',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_40C4',
    )

    ChrTurnDirection(0x0106, 0x0001, 400)

    Jump('loc_40CB')

    def _loc_40C4(): pass

    label('loc_40C4')

    ChrTurnDirection(0x0106, 0x0000, 400)

    def _loc_40CB(): pass

    label('loc_40CB')

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

    Jump('loc_41B1')

    def _loc_412C(): pass

    label('loc_412C')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4142',
    )

    ChrTurnDirection(0x0103, 0x0001, 400)

    Jump('loc_4149')

    def _loc_4142(): pass

    label('loc_4142')

    ChrTurnDirection(0x0103, 0x0000, 400)

    def _loc_4149(): pass

    label('loc_4149')

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

    def _loc_41B1(): pass

    label('loc_41B1')

    ChrMoveToRelative(0x0000, 1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_41CC(): pass

    label('loc_41CC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 0, 0x1638)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4280',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4228',
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

    Jump('loc_4265')

    def _loc_4228(): pass

    label('loc_4228')

    ChrTalk(
        0x0109,
        (
            '#0180271283V#1063F没时间闲逛了。\n',
            '……赶紧去王都协会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4265(): pass

    label('loc_4265')

    ChrMoveToRelative(0x0000, 1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_4280(): pass

    label('loc_4280')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4597',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_43A2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_4311',
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

    Jump('loc_439F')

    def _loc_4311(): pass

    label('loc_4311')

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

    def _loc_439F(): pass

    label('loc_439F')

    Jump('loc_457C')

    def _loc_43A2(): pass

    label('loc_43A2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_4496',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_43BF',
    )

    ChrTurnDirection(0x0106, 0x0001, 400)

    Jump('loc_43C6')

    def _loc_43BF(): pass

    label('loc_43BF')

    ChrTurnDirection(0x0106, 0x0000, 400)

    def _loc_43C6(): pass

    label('loc_43C6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_4438',
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

    Jump('loc_4493')

    def _loc_4438(): pass

    label('loc_4438')

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

    def _loc_4493(): pass

    label('loc_4493')

    Jump('loc_457C')

    def _loc_4496(): pass

    label('loc_4496')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_44AC',
    )

    ChrTurnDirection(0x0103, 0x0001, 400)

    Jump('loc_44B3')

    def _loc_44AC(): pass

    label('loc_44AC')

    ChrTurnDirection(0x0103, 0x0000, 400)

    def _loc_44B3(): pass

    label('loc_44B3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_4525',
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

    Jump('loc_457C')

    def _loc_4525(): pass

    label('loc_4525')

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

    def _loc_457C(): pass

    label('loc_457C')

    ChrMoveToRelative(0x0000, 1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_4597(): pass

    label('loc_4597')

    Return()

# id: 0x0019 offset: 0x4598
@scena.Code('func_19_4598')
def func_19_4598():
    TalkBegin(0x00FF)
    Sleep(400)

    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
