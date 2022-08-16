import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T4303_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4303   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4303.x'
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
        ('ED6_DT07/CH00060._CH', 'ED6_DT07/CH00060P._CP'),
        ('ED6_DT27/CH03510._CH', 'ED6_DT27/CH03510P._CP'),
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
        ('ED6_DT07/CH01570._CH', 'ED6_DT07/CH01570P._CP'),
        ('ED6_DT07/CH01350._CH', 'ED6_DT07/CH01350P._CP'),
        ('ED6_DT26/CH20291._CH', 'ED6_DT26/CH20291P._CP'),
        ('ED6_DT07/CH01010._CH', 'ED6_DT07/CH01010P._CP'),
        ('ED6_DT07/CH01060._CH', 'ED6_DT07/CH01060P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT07/CH01150._CH', 'ED6_DT07/CH01150P._CP'),
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
    ]

# id: 0x10001 offset: 0x102
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '提妲',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
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
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '管家雷蒙德',
            x                   = -19780,
            z                   = 1000,
            y                   = 29190,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '西莫鲁',
            x                   = -19840,
            z                   = 1000,
            y                   = 27860,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '王都市民',
            x                   = -2270,
            z                   = 250,
            y                   = 13100,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '王都市民',
            x                   = -2670,
            z                   = 360,
            y                   = 14060,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '旅行者',
            x                   = 4700,
            z                   = 250,
            y                   = 18020,
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
            name                = '旅行者',
            x                   = 4700,
            z                   = 250,
            y                   = 17020,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 2960,
            z                   = 1000,
            y                   = 37310,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = -2960,
            z                   = 1000,
            y                   = 37310,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = -350,
            z                   = 250,
            y                   = 12110,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = -19000,
            z                   = 1000,
            y                   = -7160,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 19000,
            z                   = 1000,
            y                   = -7160,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0005,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 20860,
            z                   = 1000,
            y                   = 31020,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0011,
        ),
    )

# id: 0x10002 offset: 0x2C2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x2C2
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 21800,
            y           = 1000,
            z           = 33960,
            range       = 21000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00007CD8,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000012,
        ),
    )

# id: 0x10004 offset: 0x2E2
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 9000,
            triggerZ            = 0,
            triggerY            = 30000,
            triggerRange        = 800,
            actorX              = 9000,
            actorZ              = 0,
            actorY              = 30000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0014,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -9000,
            triggerZ            = 0,
            triggerY            = 30000,
            triggerRange        = 800,
            actorX              = -9000,
            actorZ              = 0,
            actorY              = 30000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0014,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 13400,
            triggerZ            = 0,
            triggerY            = 27000,
            triggerRange        = 800,
            actorX              = 13400,
            actorZ              = 0,
            actorY              = 27000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0014,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 13400,
            triggerZ            = 0,
            triggerY            = 21000,
            triggerRange        = 800,
            actorX              = 13400,
            actorZ              = 0,
            actorY              = 21000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0014,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 13400,
            triggerZ            = 0,
            triggerY            = 11000,
            triggerRange        = 800,
            actorX              = 13400,
            actorZ              = 0,
            actorY              = 11000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0014,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 13400,
            triggerZ            = 0,
            triggerY            = 5000,
            triggerRange        = 800,
            actorX              = 13400,
            actorZ              = 0,
            actorY              = 5000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0014,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -13400,
            triggerZ            = 0,
            triggerY            = 27000,
            triggerRange        = 800,
            actorX              = -13400,
            actorZ              = 0,
            actorY              = 27000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0014,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -13400,
            triggerZ            = 0,
            triggerY            = 21000,
            triggerRange        = 800,
            actorX              = -13400,
            actorZ              = 0,
            actorY              = 21000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0014,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -13400,
            triggerZ            = 0,
            triggerY            = 11000,
            triggerRange        = 800,
            actorX              = -13400,
            actorZ              = 0,
            actorY              = 11000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0014,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -13400,
            triggerZ            = 0,
            triggerY            = 5000,
            triggerRange        = 800,
            actorX              = -13400,
            actorZ              = 0,
            actorY              = 5000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0014,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -22170,
            triggerZ            = 1000,
            triggerY            = 29080,
            triggerRange        = 800,
            actorX              = -22170,
            actorZ              = 1500,
            actorY              = 29080,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0013,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x46E
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4A0',
    )

    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000D, 0x0080)
    ChrSetFlags(0x000E, 0x0080)
    ChrSetFlags(0x000F, 0x0080)
    ChrClearFlags(0x0012, 0x0080)
    ChrClearFlags(0x0013, 0x0080)
    ChrClearFlags(0x0014, 0x0080)

    Jump('loc_50B')

    def _loc_4A0(): pass

    label('loc_4A0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 2, 0x162A)),
            Expr.Return,
        ),
        'loc_4DC',
    )

    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000D, 0x0080)
    ChrSetFlags(0x000E, 0x0080)
    ChrSetFlags(0x000F, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0012, 0x0080)
    ChrClearFlags(0x0013, 0x0080)
    ChrClearFlags(0x0014, 0x0080)
    ChrClearFlags(0x0015, 0x0080)

    Jump('loc_50B')

    def _loc_4DC(): pass

    label('loc_4DC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            Expr.Return,
        ),
        'loc_4F0',
    )

    ChrSetFlags(0x000E, 0x0010)
    ChrSetFlags(0x000F, 0x0010)

    Jump('loc_50B')

    def _loc_4F0(): pass

    label('loc_4F0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 2, 0x1612)),
            Expr.Return,
        ),
        'loc_4FA',
    )

    Jump('loc_50B')

    def _loc_4FA(): pass

    label('loc_4FA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 5, 0x160D)),
            Expr.Return,
        ),
        'loc_50B',
    )

    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000B, 0x0080)

    def _loc_50B(): pass

    label('loc_50B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_521',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    MapSetFlags(0x10000000)
    Event(0, func_15_186F)

    Jump('loc_577')

    def _loc_521(): pass

    label('loc_521')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_537',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    MapSetFlags(0x10000000)
    Event(0, func_1A_2573)

    Jump('loc_577')

    def _loc_537(): pass

    label('loc_537')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000066, 'loc_547'),
        (0x0000006A, 'loc_55F'),
        (-1, 'loc_577'),
    )

    def _loc_547(): pass

    label('loc_547')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 2, 0x1612)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 4, 0x1614)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_55C',
    )

    MapSetFlags(0x10000000)
    Event(0, func_15_186F)

    def _loc_55C(): pass

    label('loc_55C')

    Jump('loc_577')

    def _loc_55F(): pass

    label('loc_55F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 2, 0x162A)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 3, 0x162B)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_574',
    )

    MapSetFlags(0x10000000)
    Event(0, func_1E_275D)

    def _loc_574(): pass

    label('loc_574')

    Jump('loc_577')

    def _loc_577(): pass

    label('loc_577')

    Return()

# id: 0x0001 offset: 0x578
@scena.Code('func_01_578')
def func_01_578():
    OP_16(0x02, 4000, -128000, -112000, 2293858)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 2, 0x1612)),
            Expr.Return,
        ),
        'loc_598',
    )

    OP_64(0x0A, 0x0001)

    Jump('loc_59D')

    def _loc_598(): pass

    label('loc_598')

    OP_72(0x0003, 0x0010)

    def _loc_59D(): pass

    label('loc_59D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            Expr.Return,
        ),
        'loc_5CC',
    )

    OP_64(0x00, 0x0001)
    OP_64(0x01, 0x0001)
    OP_64(0x02, 0x0001)
    OP_64(0x03, 0x0001)
    OP_64(0x04, 0x0001)
    OP_64(0x05, 0x0001)
    OP_64(0x06, 0x0001)
    OP_64(0x07, 0x0001)
    OP_64(0x08, 0x0001)
    OP_64(0x09, 0x0001)

    def _loc_5CC(): pass

    label('loc_5CC')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5EA',
    )

    StopEffect(0x80, 0x00)
    StopEffect(0x81, 0x00)
    StopEffect(0x82, 0x00)
    StopEffect(0x83, 0x00)
    StopEffect(0x84, 0x00)

    Jump('loc_606')

    def _loc_5EA(): pass

    label('loc_5EA')

    OP_25(0x01CB, -130, 250, 15900, 2000, 25000, 0x64, 0x00000000)

    def _loc_606(): pass

    label('loc_606')

    Return()

# id: 0x0002 offset: 0x607
@scena.Code('func_02_607')
def func_02_607():
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
        'loc_62C',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_76E')

    def _loc_62C(): pass

    label('loc_62C')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_645',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_76E')

    def _loc_645(): pass

    label('loc_645')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_65E',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_76E')

    def _loc_65E(): pass

    label('loc_65E')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_677',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_76E')

    def _loc_677(): pass

    label('loc_677')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_690',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_76E')

    def _loc_690(): pass

    label('loc_690')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6A9',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_76E')

    def _loc_6A9(): pass

    label('loc_6A9')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6C2',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_76E')

    def _loc_6C2(): pass

    label('loc_6C2')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6DB',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_76E')

    def _loc_6DB(): pass

    label('loc_6DB')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6F4',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_76E')

    def _loc_6F4(): pass

    label('loc_6F4')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_70D',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_76E')

    def _loc_70D(): pass

    label('loc_70D')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_726',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_76E')

    def _loc_726(): pass

    label('loc_726')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_73F',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_76E')

    def _loc_73F(): pass

    label('loc_73F')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_758',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_76E')

    def _loc_758(): pass

    label('loc_758')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_76E',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_76E(): pass

    label('loc_76E')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_783',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_76E')

    def _loc_783(): pass

    label('loc_783')

    Return()

# id: 0x0003 offset: 0x784
@scena.Code('func_03_784')
def func_03_784():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_7A7',
    )

    OP_8D(0x00FE, -4370, 20680, 4760, 11150, 2000)

    Jump('func_03_784')

    def _loc_7A7(): pass

    label('loc_7A7')

    Return()

# id: 0x0004 offset: 0x7A8
@scena.Code('func_04_7A8')
def func_04_7A8():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_844',
    )

    ChrWalkTo(0x00FE, -19000, 1000, -7160, 2000, 0x00)
    Sleep(1000)

    ChrSetDirection(0x00FE, 0, 400)
    ChrWalkTo(0x00FE, -19000, 1000, 34000, 2000, 0x00)
    ChrWalkTo(0x00FE, -17800, 1000, 35100, 2000, 0x00)
    ChrWalkTo(0x00FE, -9000, 1000, 35100, 2000, 0x00)
    Sleep(1000)

    ChrSetDirection(0x00FE, 270, 400)
    ChrWalkTo(0x00FE, -17800, 1000, 35100, 2000, 0x00)
    ChrWalkTo(0x00FE, -19000, 1000, 34000, 2000, 0x00)

    Jump('func_04_7A8')

    def _loc_844(): pass

    label('loc_844')

    Return()

# id: 0x0005 offset: 0x845
@scena.Code('func_05_845')
def func_05_845():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_8E1',
    )

    ChrWalkTo(0x00FE, 19000, 1000, -7160, 2000, 0x00)
    Sleep(1000)

    ChrSetDirection(0x00FE, 0, 400)
    ChrWalkTo(0x00FE, 19000, 1000, 34000, 2000, 0x00)
    ChrWalkTo(0x00FE, 17800, 1000, 35100, 2000, 0x00)
    ChrWalkTo(0x00FE, 9000, 1000, 35100, 2000, 0x00)
    Sleep(1000)

    ChrSetDirection(0x00FE, 90, 400)
    ChrWalkTo(0x00FE, 17800, 1000, 35100, 2000, 0x00)
    ChrWalkTo(0x00FE, 19000, 1000, 34000, 2000, 0x00)

    Jump('func_05_845')

    def _loc_8E1(): pass

    label('loc_8E1')

    Return()

# id: 0x0006 offset: 0x8E2
@scena.Code('func_06_8E2')
def func_06_8E2():
    TalkBegin(0x000A)

    ChrTalk(
        0x00FE,
        (
            '总、总之，只有镇定下来\n',
            '仔细寻找了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那孩子可能\n',
            '有什么理由也不一定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000A)

    Return()

# id: 0x0007 offset: 0x937
@scena.Code('func_07_937')
def func_07_937():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_97B',
    )

    ChrTalk(
        0x00FE,
        (
            '那孩子一定在\n',
            '离宫中的某处。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '请一定要找到～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9C8')

    def _loc_97B(): pass

    label('loc_97B')

    ChrTalk(
        0x00FE,
        (
            '啊～真是的，那孩子\n',
            '就像捉弄人似的消失了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '绝对不能原谅～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    ChrClearFlags(0x000B, 0x0010)

    def _loc_9C8(): pass

    label('loc_9C8')

    TalkEnd(0x000B)

    Return()

# id: 0x0008 offset: 0x9CC
@scena.Code('func_08_9CC')
def func_08_9CC():
    TalkBegin(0x000C)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B1A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            Expr.Return,
        ),
        'loc_A30',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，凝视着喷泉\n',
            '心就不可思议地平静……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '水真是有各种各样的效果啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B1A')

    def _loc_A30(): pass

    label('loc_A30')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_B1A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_A7E',
    )

    ChrTalk(
        0x00FE,
        (
            '穿白裙子的女孩吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我见过这样的孩子\n',
            '在这附近玩呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B1A')

    def _loc_A7E(): pass

    label('loc_A7E')

    ChrTalk(
        0x00FE,
        (
            '……哦？\n',
            '穿白裙子的女孩吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这么说来，好象有见过\n',
            '在这附近玩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1004F知道去哪儿了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯……抱歉，\n',
            '记不起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1007F……是吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_B1A(): pass

    label('loc_B1A')

    TalkEnd(0x000C)

    Return()

# id: 0x0009 offset: 0xB1E
@scena.Code('func_09_B1E')
def func_09_B1E():
    TalkBegin(0x000D)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_BE6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            Expr.Return,
        ),
        'loc_B7A',
    )

    ChrTalk(
        0x00FE,
        (
            '能让飞船飞起来，\n',
            '让喷泉喷出水来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '导力真是不可思议啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BE6')

    def _loc_B7A(): pass

    label('loc_B7A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_BE6',
    )

    ChrTalk(
        0x00FE,
        (
            '对了，这喷泉\n',
            '也是导力驱动的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '世界上，各种各样的东西\n',
            '都是靠导力驱动的\n',
            '老爸是这么说的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BE6(): pass

    label('loc_BE6')

    TalkEnd(0x000D)

    Return()

# id: 0x000A offset: 0xBEA
@scena.Code('func_0A_BEA')
def func_0A_BEA():
    TalkBegin(0x000E)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C8E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            Expr.Return,
        ),
        'loc_C1B',
    )

    ChrTalk(
        0x00FE,
        (
            '公主！　我对你……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C8E')

    def _loc_C1B(): pass

    label('loc_C1B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_C8E',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯～原来如此。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '确实这个离宫\n',
            '是相当适合王室的地方呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只是待在这里\n',
            '就感觉自己也成了王子一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C8E(): pass

    label('loc_C8E')

    TalkEnd(0x000E)

    Return()

# id: 0x000B offset: 0xC92
@scena.Code('func_0B_C92')
def func_0B_C92():
    TalkBegin(0x000F)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D1F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            Expr.Return,
        ),
        'loc_CCE',
    )

    ChrTalk(
        0x00FE,
        (
            '不行，王子！\n',
            '下人们会看见的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D1F')

    def _loc_CCE(): pass

    label('loc_CCE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_D1F',
    )

    ChrTalk(
        0x00FE,
        (
            '呵呵，他真是\n',
            '个浪漫主义者。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他要是王子殿下\n',
            '那我就是公主殿下了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D1F(): pass

    label('loc_D1F')

    TalkEnd(0x000F)

    Return()

# id: 0x000C offset: 0xD23
@scena.Code('func_0C_D23')
def func_0C_D23():
    TalkBegin(0x0010)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F48',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_E55',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_DA3',
    )

    ChrTalk(
        0x00FE,
        (
            '听说签字仪式上\n',
            '会有国内外许多媒体到场。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼呼呼，我的初次杂志亮相\n',
            '说不定就近在咫尺了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E52')

    def _loc_DA3(): pass

    label('loc_DA3')

    ChrTalk(
        0x00FE,
        (
            '听说签字仪式上\n',
            '会有国内外许多媒体到场。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看来报道阵容已经得到批准\n',
            '使用照相机拍摄了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……我的杂志初次亮相难道近在咫尺了！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_E52(): pass

    label('loc_E52')

    Jump('loc_F48')

    def _loc_E55(): pass

    label('loc_E55')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 2, 0x162A)),
            Expr.Return,
        ),
        'loc_F48',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_EC2',
    )

    ChrTalk(
        0x00FE,
        (
            '不仅是原精锐部队，\n',
            '情报部还有白刃战的专家。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果在市区发生战斗，\n',
            '绝对不能轻视哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F48')

    def _loc_EC2(): pass

    label('loc_EC2')

    ChrTalk(
        0x00FE,
        (
            '万一要与情报部作战，\n',
            '必须提高警惕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不仅是原精锐部队，\n',
            '他们还有白刃战的专家。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果在市区发生战斗，\n',
            '绝对不能轻视哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_F48(): pass

    label('loc_F48')

    TalkEnd(0x0010)

    Return()

# id: 0x000D offset: 0xF4C
@scena.Code('func_0D_F4C')
def func_0D_F4C():
    TalkBegin(0x0011)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_10FF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_1044',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_FC7',
    )

    ChrTalk(
        0x00FE,
        (
            '从诞辰庆典开始\n',
            '事件持续不断\n',
            '到底是令人紧张啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只希望签字仪式\n',
            '能平安结束就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1041')

    def _loc_FC7(): pass

    label('loc_FC7')

    ChrTalk(
        0x00FE,
        (
            '签字仪式也近在眼前了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '从诞辰庆典开始\n',
            '事件持续不断\n',
            '到底是令人紧张啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只希望签字仪式\n',
            '能平安结束就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_1041(): pass

    label('loc_1041')

    Jump('loc_10FF')

    def _loc_1044(): pass

    label('loc_1044')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 2, 0x162A)),
            Expr.Return,
        ),
        'loc_10FF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_1094',
    )

    ChrTalk(
        0x00FE,
        (
            '能借助各位游击士的力量\n',
            '可真令人放心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一起努力吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10FF')

    def _loc_1094(): pass

    label('loc_1094')

    ChrTalk(
        0x00FE,
        (
            '听说今后要和\n',
            '游击士协会配合工作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '能借助各位游击士的力量\n',
            '可真令人放心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一起努力吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_10FF(): pass

    label('loc_10FF')

    TalkEnd(0x0011)

    Return()

# id: 0x000E offset: 0x1103
@scena.Code('func_0E_1103')
def func_0E_1103():
    TalkBegin(0x0012)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_116A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1167',
    )

    ChrTalk(
        0x00FE,
        (
            '如你所见，\n',
            '连喷泉都停了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是连平常的景色\n',
            '也有导力器渗透其中啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1167(): pass

    label('loc_1167')

    Jump('loc_124E')

    def _loc_116A(): pass

    label('loc_116A')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_124E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_11E0',
    )

    ChrTalk(
        0x00FE,
        (
            '多亏希德中校的指挥\n',
            '袭击似乎没有造成多大损害。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '作为佯攻的特务兵\n',
            '也真是找错了对象啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_124E')

    def _loc_11E0(): pass

    label('loc_11E0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 2, 0x162A)),
            Expr.Return,
        ),
        'loc_124E',
    )

    ChrTalk(
        0x00FE,
        (
            '现在还没什么异常。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只是，刚才副队长从通讯室\n',
            '慌慌张张跑了出去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……可得做好心理准备啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_124E(): pass

    label('loc_124E')

    TalkEnd(0x0012)

    Return()

# id: 0x000F offset: 0x1252
@scena.Code('func_0F_1252')
def func_0F_1252():
    TalkBegin(0x0013)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_12D4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_12D1',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然从这里看不见，\n',
            '听说瓦雷利亚湖上出现了\n',
            '不可思议的物体不是吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '连协会，\n',
            '也不知道其真面目吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_12D1(): pass

    label('loc_12D1')

    Jump('loc_139F')

    def _loc_12D4(): pass

    label('loc_12D4')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_139F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_1336',
    )

    ChrTalk(
        0x00FE,
        (
            '刚才爱尔莎大使\n',
            '和共和国议员来访了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看来是来熟悉会场\n',
            '和洽谈来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_139F')

    def _loc_1336(): pass

    label('loc_1336')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 2, 0x162A)),
            Expr.Return,
        ),
        'loc_139F',
    )

    ChrTalk(
        0x00FE,
        (
            '这么说来，共和国的\n',
            '议员们都住在这里呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '似乎是为了签字仪式的准备和视察，\n',
            '提前来到现场。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_139F(): pass

    label('loc_139F')

    TalkEnd(0x0013)

    Return()

# id: 0x0010 offset: 0x13A3
@scena.Code('func_10_13A3')
def func_10_13A3():
    TalkBegin(0x0014)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1441',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_143E',
    )

    ChrTalk(
        0x00FE,
        (
            '和守护哈肯门的时候\n',
            '相比，这里还很平静。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那边怎么说都经常\n',
            '受到帝国的威胁嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '待在那城堡里的话，晚上\n',
            '可是能睡得很香呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_143E(): pass

    label('loc_143E')

    Jump('loc_14DE')

    def _loc_1441(): pass

    label('loc_1441')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_14DE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_14AF',
    )

    ChrTalk(
        0x00FE,
        (
            '余党的事件结束后\n',
            '感觉真是转眼间的事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '竟然能那么快解决，\n',
            '他们也真有点可怜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_14DE')

    def _loc_14AF(): pass

    label('loc_14AF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 2, 0x162A)),
            Expr.Return,
        ),
        'loc_14DE',
    )

    ChrTalk(
        0x00FE,
        (
            '抱歉我正在巡逻。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不要妨碍我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_14DE(): pass

    label('loc_14DE')

    TalkEnd(0x0014)

    Return()

# id: 0x0011 offset: 0x14E2
@scena.Code('func_11_14E2')
def func_11_14E2():
    TalkBegin(0x0015)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1580',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_1533',
    )

    ChrTalk(
        0x00FE,
        (
            '这个房间是通信室。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在贝尔克副队长在里面哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1580')

    def _loc_1533(): pass

    label('loc_1533')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 2, 0x162A)),
            Expr.Return,
        ),
        'loc_1580',
    )

    ChrTalk(
        0x00FE,
        (
            '这个房间现在\n',
            '是作为通信室来使用的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '无关人员\n',
            '是不能进去的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1580(): pass

    label('loc_1580')

    TalkEnd(0x0015)

    Return()

# id: 0x0012 offset: 0x1584
@scena.Code('func_12_1584')
def func_12_1584():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 2, 0x162A)),
            Expr.Ez,
            Expr.Or,
            Expr.Return,
        ),
        'loc_1591',
    )

    Return()

    def _loc_1591(): pass

    label('loc_1591')

    EventBegin(0x02)
    OP_4A(0x0015, 255)
    ChrTurnDirection(0x0015, 0x0000, 0)
    ChrTurnDirection(0x0000, 0x0015, 0)
    ChrTurnDirection(0x0001, 0x0015, 0)
    ChrTurnDirection(0x0002, 0x0015, 0)
    ChrTurnDirection(0x0003, 0x0015, 0)

    ChrTalk(
        0x0015,
        (
            '这个房间是通信室。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '请不要随便进去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(500)
    ChrSetPos(0x0015, 20860, 1000, 31020, 270)
    ChrSetPos(0x0000, 20020, 1000, 32960, 270)
    ChrSetPos(0x0001, 20020, 1000, 32960, 270)
    ChrSetPos(0x0002, 20020, 1000, 32960, 270)
    ChrSetPos(0x0003, 20020, 1000, 32960, 270)
    OP_0D()
    OP_4B(0x0015, 255)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x0013 offset: 0x164F
@scena.Code('func_13_164F')
def func_13_164F():
    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门上着锁。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Return()

# id: 0x0014 offset: 0x1697
@scena.Code('func_14_1697')
def func_14_1697():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 1, 0x1611)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1828',
    )

    EventBegin(0x01)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '长椅周围没有任何人。',
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
            '#0010240831V#1015F长椅和树丛的\n',
            '缝隙里也没有吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240832V#1004F啊，难不成\n',
            '在树丛里面！',
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
        'loc_1785',
    )

    ChrTalk(
        0x0107,
        (
            '#0070240833V#067F简、简直是\n',
            '真正的猫啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17F8')

    def _loc_1785(): pass

    label('loc_1785')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_17C6',
    )

    ChrTalk(
        0x0106,
        (
            '#0050240834V#552F喂喂……\n',
            '又不是真正的猫。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17F8')

    def _loc_17C6(): pass

    label('loc_17C6')

    ChrTalk(
        0x0103,
        (
            '#0030240835V#524F真是的……\n',
            '又不是真正的猫。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_17F8(): pass

    label('loc_17F8')

    ChrTalk(
        0x0101,
        (
            '#0010240836V#1016F还是不行？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x01)
    SetScenaFlags(ScenaFlag(0x02C2, 1, 0x1611))
    OP_28(0x0089, 0x01, 0x0040)

    Jump('loc_186E')

    def _loc_1828(): pass

    label('loc_1828')

    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '长椅周围没有任何人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    TalkEnd(0x00FF)
    def _loc_186E(): pass

    label('loc_186E')

    Return()

# id: 0x0015 offset: 0x186F
@scena.Code('func_15_186F')
def func_15_186F():
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
        'loc_1886',
    )

    Call(0, 0x0021)
    Call(0, 0x0022)

    def _loc_1886(): pass

    label('loc_1886')

    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x00F7, 0x0080)
    ChrSetFlags(0x00F8, 0x0080)
    ChrSetFlags(0x00F9, 0x0080)
    CameraMove(-19850, 1000, 2930, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(335000, 0)
    OP_6E(262, 0)
    FadeIn(1000, 0)
    OP_0D()
    OP_72(0x0005, 0x0010)
    OP_6F(0x0005, 0)
    OP_70(0x0005, 29)
    OP_73(0x0005)
    Sleep(500)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_1D96',
    )

    CreateThread(0x0101, 0x01, 0x00, func_16_2463)
    Sleep(800)

    CreateThread(0x00F7, 0x01, 0x00, func_17_2495)
    Sleep(800)

    CreateThread(0x00F8, 0x01, 0x00, func_18_24C7)
    Sleep(800)

    CreateThread(0x00F9, 0x01, 0x00, func_19_250D)
    WaitForThreadExit(0x00F9, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010240967V#1005F真是的……\n',
            '什么嘛，那个公爵！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240968V抬高自己\n',
            '还贬低科洛丝！',
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
        'loc_1B8F',
    )

    ChrTalk(
        0x0106,
        (
            '#0050240969V#053F哎，别那么冲动嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050240970V#050F我倒觉得那公爵说的\n',
            '也有一番道理。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050240971V站在高处的人\n',
            '是不能显示出迷惘的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050240972V必须时时向周围的人\n',
            '展现自己的正确。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240973V#1026F但是，科洛丝……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050240974V#051F啊啊，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050240975V就算那个公爵不说\n',
            '公主肯定明白的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050240976V现在我们只要守护着\n',
            '公主找到答案就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240977V#1025F啊……\n',
            '嗯……明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240978V#1006F好！\n',
            '寻找迷路的孩子，再度开始吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050240979V#051F哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D93')

    def _loc_1B8F(): pass

    label('loc_1B8F')

    ChrTalk(
        0x0103,
        (
            '#0030240980V#026F哎，别那么冲动嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030240981V#020F那公爵先生，意外的\n',
            '也会说点正经话嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030240982V站在高处的人\n',
            '是不能显示出迷惘的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030240983V必须时时向周围的人\n',
            '展现自己的正确引导。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240973V#1026F但是，科洛丝……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030240985V#021F嗯嗯，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030240986V#027F就算公爵先生不说\n',
            '公主殿下应该也明白的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030240987V现在只要守护着公主殿下\n',
            '等她找到答案就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240977V#1025F啊……\n',
            '嗯……明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240978V#1006F好！\n',
            '寻找迷路的孩子，再度开始吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030240990V#021F哎哎。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1D93(): pass

    label('loc_1D93')

    Jump('loc_2458')

    def _loc_1D96(): pass

    label('loc_1D96')

    CreateThread(0x0101, 0x01, 0x00, func_16_2463)
    Sleep(800)

    CreateThread(0x0105, 0x01, 0x00, func_17_2495)
    Sleep(800)

    CreateThread(0x00F7, 0x01, 0x00, func_18_24C7)
    Sleep(800)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1DD2',
    )

    CreateThread(0x0104, 0x01, 0x00, func_19_250D)

    Jump('loc_1DFF')

    def _loc_1DD2(): pass

    label('loc_1DD2')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1DEA',
    )

    CreateThread(0x0107, 0x01, 0x00, func_19_250D)

    Jump('loc_1DFF')

    def _loc_1DEA(): pass

    label('loc_1DEA')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1DFF',
    )

    CreateThread(0x0108, 0x01, 0x00, func_19_250D)

    def _loc_1DFF(): pass

    label('loc_1DFF')

    WaitForThreadExit(0x00F9, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010240967V#1005F真是的……\n',
            '什么嘛，那个公爵！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240968V抬高自己\n',
            '还贬低科洛丝！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060240993V#047F不，叔叔的责难\n',
            '要我说也是当然。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060240994V身为王族的义务……\n',
            '这确实是存在的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240995V#1002F但、但是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2128',
    )

    ChrTalk(
        0x0104,
        (
            '#0040240996V#030F唔，知名度吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040240997V#035F历史上，几乎默默无闻地\n',
            '坐在君主之位上\n',
            '却留下了伟大业绩的人也不少。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040240998V埃雷波尼亚也有过因为内乱\n',
            '使得有力的皇子们相继死去\n',
            '而最后，无名的皇子继承了皇位……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040240999V那位皇子，日后成为了被称为中兴之祖的\n',
            '伟大皇帝。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0105, 187, 400)

    ChrTalk(
        0x0105,
        (
            '#0060241000V#040F#2P是说德莱凯斯大帝吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040241001V#031F呼，知道的真清楚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040241002V#030F所以我想公主殿下\n',
            '您无需多虑。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060241003V#045F#2P呵呵，或许吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060241004V#049F但我的心理准备\n',
            '正如叔叔所说的一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010241005V#1026F科洛丝……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0105, 127, 400)

    Jump('loc_2383')

    def _loc_2128(): pass

    label('loc_2128')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_22D8',
    )

    ChrTalk(
        0x0108,
        (
            '#0080241006V#074F嗯，共和国是通过选举\n',
            '来选出大总统的嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080241007V虽说这是王族的义务,\n',
            '你只不过还没完全进入角色……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080241008V#070F但是，那个公爵阁下的情况，\n',
            '倒是坏的知名度高涨了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080241009V认为他比你\n',
            '更适合当下任国王的人\n',
            '整个利贝尔都找不到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0105, 187, 400)
    Sleep(400)

    ChrTalk(
        0x0105,
        (
            '#0060241010V#043F#2P这……\n',
            '或许是吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060241004V#049F但我的心理准备\n',
            '正如叔叔所说的一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010241005V#1026F科洛丝……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0105, 127, 400)
    Sleep(400)

    Jump('loc_2383')

    def _loc_22D8(): pass

    label('loc_22D8')

    ChrTalk(
        0x0105,
        (
            '#0060241013V#049F即使不谈这义务……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060241014V但我的心理准备\n',
            '正如叔叔所说的一样。',
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
        'loc_2361',
    )

    ChrTalk(
        0x0107,
        (
            '#0070241015V#063F科洛丝……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2361(): pass

    label('loc_2361')

    ChrTalk(
        0x0101,
        (
            '#0010241005V#1026F科洛丝……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2383(): pass

    label('loc_2383')

    ChrTalk(
        0x0105,
        (
            '#0060241017V#542F我能在这里\n',
            '遇见叔叔真是太好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060241018V让我重新注意到了\n',
            '自己不足的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010241019V#1025F是哦……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010241020V#1006F好！\n',
            '寻找迷路的孩子，重新开始吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060241021V#041F好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_2458(): pass

    label('loc_2458')

    SetScenaFlags(ScenaFlag(0x02C2, 4, 0x1614))
    OP_71(0x0005, 0x0010)
    EventEnd(0x00)

    Return()

# id: 0x0016 offset: 0x2463
@scena.Code('func_16_2463')
def func_16_2463():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetPos(0x00FE, -22550, 1000, 3180, 90)
    ChrWalkTo(0x00FE, -18530, 1000, 2460, 2000, 0x00)
    ChrSetDirection(0x00FE, 296, 400)

    Return()

# id: 0x0017 offset: 0x2495
@scena.Code('func_17_2495')
def func_17_2495():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetPos(0x00FE, -22550, 1000, 3180, 90)
    ChrWalkTo(0x00FE, -19580, 1000, 3110, 2000, 0x00)
    ChrSetDirection(0x00FE, 127, 400)

    Return()

# id: 0x0018 offset: 0x24C7
@scena.Code('func_18_24C7')
def func_18_24C7():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetPos(0x00FE, -22550, 1000, 3180, 90)
    ChrWalkTo(0x00FE, -21520, 1000, 2790, 2000, 0x00)
    ChrWalkTo(0x00FE, -19450, 1000, 1650, 2000, 0x00)
    ChrSetDirection(0x00FE, 29, 400)

    Return()

# id: 0x0019 offset: 0x250D
@scena.Code('func_19_250D')
def func_19_250D():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetPos(0x00FE, -22550, 1000, 3180, 90)
    ChrWalkTo(0x00FE, -21520, 1000, 2790, 2000, 0x00)
    OP_72(0x0005, 0x0800)
    OP_6F(0x0005, 29)
    OP_70(0x0005, 0)
    OP_23(0x0006)
    PlaySE(7, 0x00, 0x64)
    ChrWalkTo(0x00FE, -20460, 1000, 2380, 2000, 0x00)
    ChrSetDirection(0x00FE, 101, 400)
    OP_71(0x0005, 0x0800)

    Return()

# id: 0x001A offset: 0x2573
@scena.Code('func_1A_2573')
def func_1A_2573():
    EventBegin(0x00)
    OP_DB()
    OP_11(0x9E, 0xFF, 0xFF, 35000, 294000, 0)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000D, 0x0080)
    ChrSetFlags(0x000E, 0x0080)
    ChrSetFlags(0x000F, 0x0080)
    ChrSetPos(0x0009, 2710, 250, 13190, 45)
    ChrSetPos(0x0008, 1030, 250, 12140, 90)
    OP_4A(0x0010, 255)
    OP_4A(0x0011, 255)
    OP_4A(0x0012, 255)
    OP_4A(0x0013, 255)
    ChrSetPos(0x0010, 19000, 1000, 16000, 360)
    ChrSetPos(0x0011, -1190, 1000, 33830, 360)
    ChrSetPos(0x0012, 19000, 1000, 17500, 360)
    ChrSetPos(0x0013, -2690, 1000, 33830, 360)
    ChrSetChipByIndex(0x0010, 2)
    ChrSetSubChip(0x0010, 0)
    ChrSetChipByIndex(0x0011, 2)
    ChrSetSubChip(0x0011, 0)
    ChrSetChipByIndex(0x0012, 2)
    ChrSetSubChip(0x0012, 0)
    ChrSetChipByIndex(0x0013, 2)
    ChrSetSubChip(0x0013, 0)
    CameraMove(4920, 0, 22470, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(4910, 0)
    OP_6C(43000, 0)
    OP_6E(350, 0)
    CreateThread(0x0009, 0x01, 0x00, func_1B_26C6)
    CreateThread(0x0008, 0x01, 0x00, func_1B_26C6)
    CreateThread(0x0010, 0x01, 0x00, func_1C_26ED)
    CreateThread(0x0011, 0x01, 0x00, func_1D_272F)
    CreateThread(0x0012, 0x01, 0x00, func_1C_26ED)
    CreateThread(0x0013, 0x01, 0x00, func_1D_272F)
    FadeIn(2000, 0)
    OP_0D()
    Sleep(2000)

    Sleep(1500)

    Sleep(1500)

    OP_DC()
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/T4312._SN', 105, 0, 0)
    IdleLoop()

    Return()

# id: 0x001B offset: 0x26C6
@scena.Code('func_1B_26C6')
def func_1B_26C6():
    ChrClearFlags(0x00FE, 0x0080)
    def _loc_26CB(): pass

    label('loc_26CB')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_26EC',
    )

    OP_97(0x00FE, -50, 16030, -90000, 6000, 0x0001)

    Jump('loc_26CB')

    def _loc_26EC(): pass

    label('loc_26EC')

    Return()

# id: 0x001C offset: 0x26ED
@scena.Code('func_1C_26ED')
def func_1C_26ED():
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, 19000, 1000, 35830, 2000, 0x00)
    ChrWalkTo(0x00FE, -18890, 1000, 35830, 2000, 0x00)
    ChrWalkTo(0x00FE, -18890, 1000, -2980, 2000, 0x00)

    Return()

# id: 0x001D offset: 0x272F
@scena.Code('func_1D_272F')
def func_1D_272F():
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, 18890, 1000, 33830, 2000, 0x00)
    ChrWalkTo(0x00FE, 18890, 1000, -2980, 2000, 0x00)

    Return()

# id: 0x001E offset: 0x275D
@scena.Code('func_1E_275D')
def func_1E_275D():
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
        'loc_2770',
    )

    Call(0, 0x0021)

    def _loc_2770(): pass

    label('loc_2770')

    FormationAddMember(ChrTable['提妲'], 0xF8, 0xFF)
    FormationAddMember(ChrTable['玲'], 0xFF, 0xFF)
    CameraMove(370, 1000, 42730, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2630, 0)
    OP_6C(33000, 0)
    OP_6E(262, 0)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x00F7, 0x0080)
    ChrSetPos(0x0107, 0, 0, 24820, 360)
    ChrSetPos(0x012F, 0, 0, 24820, 360)
    FadeIn(1000, 0)
    OP_0D()
    OP_6F(0x0000, 0)
    OP_70(0x0000, 29)
    OP_73(0x0000)
    Sleep(500)

    CreateThread(0x0101, 0x01, 0x00, func_1F_32BF)
    Sleep(800)

    CreateThread(0x00F7, 0x01, 0x00, func_20_3311)
    Sleep(3000)

    @scena.Lambda('lambda_281F')
    def lambda_281F():
        CameraMove(460, 1000, 34360, 3000)

        ExitThread()

    DispatchAsync(0x012F, 0x0000, lambda_281F)

    @scena.Lambda('lambda_2837')
    def lambda_2837():
        OP_6C(45000, 3000)

        ExitThread()

    DispatchAsync(0x012F, 0x0001, lambda_2837)

    WaitForThreadExit(0x012F, 0x0000)
    WaitForThreadExit(0x012F, 0x0001)

    NpcTalk(
        0x012F,
        '少女的声音',
        (
            '#0220260348V#5P啊、艾丝蒂尔！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_287F')
    def lambda_287F():
        ChrWalkTo(0x00FE, 950, 1000, 32960, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x012F, 0x0001, lambda_287F)

    Sleep(500)

    @scena.Lambda('lambda_289F')
    def lambda_289F():
        ChrWalkTo(0x00FE, -200, 1000, 32960, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_289F)

    WaitForThreadExit(0x012F, 0x0001)
    WaitForThreadExit(0x0107, 0x0001)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_2901',
    )

    ChrTalk(
        0x0107,
        (
            '#0070260349V#560F#6P姐姐、阿加特哥哥。\n',
            '真是辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2936')

    def _loc_2901(): pass

    label('loc_2901')

    ChrTalk(
        0x0107,
        (
            '#0070260350V#560F#6P姐姐、雪拉姐。\n',
            '真是辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2936(): pass

    label('loc_2936')

    ChrTalk(
        0x012F,
        (
            '#0220260351V#260F嗯、这么快\n',
            '就结束了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010260352V#1006F我不是说了吗？\n',
            '只是交调查的报告书而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010260353V乖乖在协会\n',
            '等着不就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x012F,
        (
            '#0220260354V#262F呀，好过分！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220260355V玲只是想和艾丝蒂尔\n',
            '在一起……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x012F, 0x0107, 400)

    ChrTalk(
        0x012F,
        (
            '#0220260356V#262F#5P喏，提妲也\n',
            '说点什么啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0107, 0x012F, 400)

    ChrTalk(
        0x0107,
        (
            '#0070260357V#064F#6P我，我？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070260358V#067F嗯～想和姐姐们\n',
            '在一起是没错……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070260359V但这是工作，不能\n',
            '太任性嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x012F,
        (
            '#0220260360V#269F#5P哼～是吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x012F, 0, 400)
    Sleep(500)

    ChrTalk(
        0x012F,
        (
            '#0220260361V#263F#5P那么艾丝蒂尔\n',
            '就归玲了哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220260362V因为提妲太不合群了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070260363V#065F#6P啊呜……\n',
            '玲好过分啦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010260364V#1016F#5P好啦好啦，不准吵架。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010260365V提妲是姐姐\n',
            '要稍微大度点嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0107, 0, 400)

    ChrTalk(
        0x0107,
        (
            '#0070260366V#562F#6P但，但是但是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070260367V不知什么时候开始\n',
            '就叫得那么亲密……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070260368V#063F姐姐……\n',
            '你不要我了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010260369V#1016F真是的～那种事\n',
            '怎么可能嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x0107, 0x0040)
    ChrMoveTo(0x0101, -180, 1000, 33490, 2000, 0x00)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0107, 0x0002)
    ChrSetChipByIndex(0x0107, 5)
    ChrSetSubChip(0x0107, 0)
    OP_99(0x0107, 0x00, 0x02, 1000)
    Sleep(500)

    ChrTurnDirection(0x012F, 0x0107, 400)
    OP_62(0x012F, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010260370V#1006F#5P喂喂，怎么了～？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010260371V摆出那张脸\n',
            '我会抱紧你的哦～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070260372V#067F#6P啊，真是的。\n',
            '姐姐你啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x012F,
        (
            '#0220260373V#1301F#5P啊啊！\n',
            '提妲，太狡猾了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_2E1F',
    )

    ChrTalk(
        0x0106,
        (
            '#0050260374V#053F#5P哎呀呀。\n',
            '真受不了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050260375V#051F别说这个了……\n',
            '赶快返回协会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2E88')

    def _loc_2E1F(): pass

    label('loc_2E1F')

    ChrTalk(
        0x0103,
        (
            '#0030260376V#021F#5P艾丝蒂尔啊\n',
            '真是受欢迎啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030260377V#020F这个暂且不提……\n',
            '要赶快返回协会了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2E88(): pass

    label('loc_2E88')

    ChrTalk(
        0x0101,
        (
            '#0010260378V#1004F#5P啊，是哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0107, 0x02, 0x00, 1000)
    ChrClearFlags(0x0101, 0x0080)
    ChrClearFlags(0x0107, 0x0002)
    ChrSetChipByIndex(0x0107, 65535)

    @scena.Lambda('lambda_2ECB')
    def lambda_2ECB():
        ChrMoveTo(0x00FE, 370, 1000, 34190, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2ECB)

    WaitForThreadExit(0x0101, 0x0001)
    Sleep(500)

    ChrTalk(
        0x0107,
        (
            '#0070260379V#064F#6P嗯……\n',
            '发生什么事了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_2F76',
    )

    ChrTalk(
        0x0106,
        (
            '#0050260380V#555F#5P啊啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050260381V似乎柏斯地区\n',
            '出现特务兵的余党了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2FCB')

    def _loc_2F76(): pass

    label('loc_2F76')

    ChrTalk(
        0x0103,
        (
            '#0030221188V#022F#5P嗯嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030260383V似乎柏斯地区\n',
            '似乎出现特务兵的余党了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2FCB(): pass

    label('loc_2FCB')

    OP_62(0x0107, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0107,
        (
            '#0070260384V#065F#2P真、真的吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010260385V#1002F嗯，虽然还不清楚\n',
            '详细情况……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010260386V不管怎么说协会\n',
            '应该会收到情报的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070260387V#062F#6P那、那确实\n',
            '要赶快回去才行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x012F, 0, 400)

    ChrTalk(
        0x012F,
        (
            '#0220260388V#262F唔～马上\n',
            '就说起玲不懂的话了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010260389V#1016F啊哈哈，抱歉抱歉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_3152',
    )

    ChrTalk(
        0x0106,
        (
            '#0050260390V#051F#5P总之有要事\n',
            '要赶快回协会就是了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3189')

    def _loc_3152(): pass

    label('loc_3152')

    ChrTalk(
        0x0103,
        (
            '#0030260391V#020F#1P总之有要事\n',
            '要赶快回协会才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3189(): pass

    label('loc_3189')

    ChrTalk(
        0x012F,
        (
            '#0220260392V#264F哎呀，是吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220260393V#263F真可惜，有这么多\n',
            '士兵在本想玩玩\n',
            '捉迷藏也不错的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220260394V#265F能藏的地方，就这附近\n',
            '所有的森林怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0107, 0x012F, 400)

    ChrTalk(
        0x0107,
        (
            '#0070260395V#067F#6P呜哎～……\n',
            '好积极啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010260396V#1016F这、这还是\n',
            '饶了我吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010260397V#1006F那么就马上\n',
            '返回王都吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x02C5, 3, 0x162B))
    EventEnd(0x00)

    Return()

# id: 0x001F offset: 0x32BF
@scena.Code('func_1F_32BF')
def func_1F_32BF():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetPos(0x00FE, 0, 1000, 43500, 180)
    ChrWalkTo(0x00FE, 380, 1000, 39220, 2000, 0x00)
    ChrTurnDirection(0x00FE, 0x00F7, 400)
    Sleep(1000)

    ChrSetDirection(0x00FE, 180, 400)
    ChrWalkTo(0x00FE, 370, 1000, 34190, 2000, 0x00)

    Return()

# id: 0x0020 offset: 0x3311
@scena.Code('func_20_3311')
def func_20_3311():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetPos(0x00FE, 0, 1000, 43500, 180)
    ChrWalkTo(0x00FE, 0, 1000, 41300, 2000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)
    Sleep(500)

    OP_72(0x0000, 0x0800)
    OP_6F(0x0000, 29)
    OP_70(0x0000, 0)
    OP_23(0x0006)
    PlaySE(7, 0x00, 0x64)
    OP_73(0x0000)
    OP_71(0x0000, 0x0800)
    Sleep(1000)

    ChrSetDirection(0x00FE, 180, 400)
    ChrWalkTo(0x00FE, -450, 1000, 35000, 2000, 0x00)

    Return()

# id: 0x0021 offset: 0x338B
@scena.Code('func_21_338B')
def func_21_338B():
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
        (0x00000000, 'loc_3405'),
        (0x00000001, 'loc_340B'),
        (-1, 'loc_3411'),
    )

    def _loc_3405(): pass

    label('loc_3405')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_3411')

    def _loc_340B(): pass

    label('loc_340B')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_3411')

    def _loc_3411(): pass

    label('loc_3411')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_341F',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    Jump('loc_3423')

    def _loc_341F(): pass

    label('loc_341F')

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    def _loc_3423(): pass

    label('loc_3423')

    Return()

# id: 0x0022 offset: 0x3424
@scena.Code('func_22_3424')
def func_22_3424():
    MapClearFlags(0x00000001)
    CameraMove(-23520, 1000, -41440, 0)
    Sleep(100)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_3467',
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

    Jump('loc_3485')

    def _loc_3467(): pass

    label('loc_3467')

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

    def _loc_3485(): pass

    label('loc_3485')

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

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
