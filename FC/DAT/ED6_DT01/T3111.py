import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T3111_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3111   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'T3111.x'
    header.mapIndex       = 1
    header.bgm            = 13
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT01/T3111._SN', 'ED6_DT01/T3111_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
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
        ('ED6_DT07/CH01540._CH', 'ED6_DT07/CH01540P._CP'),
        ('ED6_DT07/CH01550._CH', 'ED6_DT07/CH01550P._CP'),
        ('ED6_DT07/CH01430._CH', 'ED6_DT07/CH01430P._CP'),
        ('ED6_DT07/CH01680._CH', 'ED6_DT07/CH01680P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT07/CH01500._CH', 'ED6_DT07/CH01500P._CP'),
        ('ED6_DT07/CH01550._CH', 'ED6_DT07/CH01550P._CP'),
        ('ED6_DT07/CH01450._CH', 'ED6_DT07/CH01450P._CP'),
        ('ED6_DT07/CH02070._CH', 'ED6_DT07/CH02070P._CP'),
        ('ED6_DT07/CH01690._CH', 'ED6_DT07/CH01690P._CP'),
        ('ED6_DT07/CH02640._CH', 'ED6_DT07/CH02640P._CP'),
        ('ED6_DT07/CH01190._CH', 'ED6_DT07/CH01190P._CP'),
        ('ED6_DT07/CH01700._CH', 'ED6_DT07/CH01700P._CP'),
    ]

# id: 0x10001 offset: 0x11A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '海泽尔',
            x                   = 260,
            z                   = 0,
            y                   = 5800,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '露依赛',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            name                = '雨果',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            name                = '鲁特尔',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            name                = '多杰',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            name                = '鲁迪',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '菲',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '埃里克',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '朵洛希',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '拉德米拉',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '卡雷尔',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '加鲁诺',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '汽油',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 14,
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
            name                = '安东尼',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
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
            x           = -203000,
            y           = -1000,
            z           = 137400,
            range       = 3000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000017,
        ),
        ScenaEventData(
            x           = -5000,
            y           = -1000,
            z           = 7500,
            range       = 3000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000018,
        ),
        ScenaEventData(
            x           = -5860,
            y           = -1000,
            z           = 7630,
            range       = -3720,
            dword_10    = 0x000003E8,
            dword_14    = 0x0000227E,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000001B,
        ),
    )

# id: 0x10004 offset: 0x33A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -109100,
            triggerZ            = -3500,
            triggerY            = -109000,
            triggerRange        = 1200,
            actorX              = -109100,
            actorZ              = -3500,
            actorY              = -109000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0019,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -9880,
            triggerZ            = 0,
            triggerY            = -3600,
            triggerRange        = 1200,
            actorX              = -9880,
            actorZ              = 0,
            actorY              = -3600,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x001E,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -98280,
            triggerZ            = -4000,
            triggerY            = -103420,
            triggerRange        = 1200,
            actorX              = -98280,
            actorZ              = -4000,
            actorY              = -103420,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x001F,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 50,
            triggerZ            = 0,
            triggerY            = 3900,
            triggerRange        = 400,
            actorX              = 260,
            actorZ              = 1500,
            actorY              = 5800,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0012,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 6900,
            triggerZ            = 0,
            triggerY            = -1410,
            triggerRange        = 400,
            actorX              = 8650,
            actorZ              = 1500,
            actorY              = -1120,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0013,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -103970,
            triggerZ            = 0,
            triggerY            = -99940,
            triggerRange        = 1200,
            actorX              = -103970,
            actorZ              = 1000,
            actorY              = -99940,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0014,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -5050,
            triggerZ            = 0,
            triggerY            = 8080,
            triggerRange        = 800,
            actorX              = -5050,
            actorZ              = 1000,
            actorY              = 8080,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x001C,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -202970,
            triggerZ            = 0,
            triggerY            = 138010,
            triggerRange        = 800,
            actorX              = -202970,
            actorZ              = 1000,
            actorY              = 138010,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x001D,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -200120,
            triggerZ            = 0,
            triggerY            = 118010,
            triggerRange        = 1200,
            actorX              = -200120,
            actorZ              = 1500,
            actorY              = 118010,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0023,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -121030,
            triggerZ            = -4000,
            triggerY            = -99900,
            triggerRange        = 800,
            actorX              = -121030,
            actorZ              = -3000,
            actorY              = -99900,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0024,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x4A2
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_4B0',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, func_16_5D1D)

    def _loc_4B0(): pass

    label('loc_4B0')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x0000006C, 'loc_4C8'),
        (0x00000064, 'loc_4DC'),
        (0x0000006A, 'loc_4F2'),
        (0x00000065, 'loc_4F2'),
        (-1, 'loc_4FA'),
    )

    def _loc_4C8(): pass

    label('loc_4C8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 2, 0x50A)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 0, 0x508)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4DC',
    )

    SetScenaFlags(ScenaFlag(0x00A1, 0, 0x508))
    Event(0, func_15_5B6D)

    def _loc_4DC(): pass

    label('loc_4DC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 5, 0x52D)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 4, 0x52C)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4EF',
    )

    SetScenaFlags(ScenaFlag(0x00A5, 5, 0x52D))
    Event(0, func_1A_67D5)

    def _loc_4EF(): pass

    label('loc_4EF')

    Jump('loc_4FA')

    def _loc_4F2(): pass

    label('loc_4F2')

    PlaySE(14, 0x00, 0x64)

    Jump('loc_4FA')

    def _loc_4FA(): pass

    label('loc_4FA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_530',
    )

    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x000E, -116000, -4000, -113000, 270)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x000F, 8650, 0, -1120, 274)

    Jump('loc_8FB')

    def _loc_530(): pass

    label('loc_530')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_592',
    )

    ChrClearFlags(0x000D, 0x0080)
    ChrSetPos(0x000D, -100740, -4000, -111030, 12)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x000F, 8650, 0, -1120, 274)
    ChrClearFlags(0x0011, 0x0080)
    ChrSetPos(0x0011, -7440, 0, -6000, 2)
    ChrClearFlags(0x0012, 0x0080)
    ChrSetPos(0x0012, 8720, 0, 3970, 39)

    Jump('loc_8FB')

    def _loc_592(): pass

    label('loc_592')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_60A',
    )

    ChrClearFlags(0x000D, 0x0080)
    ChrSetPos(0x000D, -100740, -4000, -111030, 12)
    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x000E, -116000, -4000, -113000, 270)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x000F, 8650, 0, -1120, 274)
    ChrClearFlags(0x0011, 0x0080)
    ChrSetPos(0x0011, -7440, 0, -6000, 2)
    ChrClearFlags(0x0012, 0x0080)
    ChrSetPos(0x0012, 8720, 0, 3970, 39)

    Jump('loc_8FB')

    def _loc_60A(): pass

    label('loc_60A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_656',
    )

    ChrClearFlags(0x000D, 0x0080)
    ChrSetPos(0x000D, -100740, -4000, -111030, 12)
    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x000E, -116000, -4000, -113000, 270)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x000F, 8650, 0, -1120, 274)

    Jump('loc_8FB')

    def _loc_656(): pass

    label('loc_656')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 6, 0x536)),
            Expr.Return,
        ),
        'loc_72B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_67F',
    )

    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0010, 10930, 0, -5500, 9)
    ChrSetFlags(0x0010, 0x0010)

    def _loc_67F(): pass

    label('loc_67F')

    ChrSetPos(0x0009, -9980, 0, -1060, 171)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x000A, -10100, 0, -2700, 347)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x000E, -116000, -4000, -113000, 270)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x000F, 8650, 0, -1120, 274)
    ChrClearFlags(0x0011, 0x0080)
    ChrSetPos(0x0011, 6890, 0, -3020, 169)
    ChrSetFlags(0x0011, 0x0010)
    ChrClearFlags(0x0012, 0x0080)
    ChrSetPos(0x0012, -7870, 0, -1230, 263)
    ChrSetFlags(0x0012, 0x0010)
    ChrClearFlags(0x0013, 0x0080)
    ChrSetPos(0x0013, 6870, 0, -4430, 11)
    ChrSetFlags(0x0013, 0x0010)

    Jump('loc_8FB')

    def _loc_72B(): pass

    label('loc_72B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_73A',
    )

    ChrSetFlags(0x0008, 0x0080)

    Jump('loc_8FB')

    def _loc_73A(): pass

    label('loc_73A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_7B2',
    )

    ChrSetPos(0x000B, -9980, 0, -1060, 171)
    ChrClearFlags(0x000B, 0x0080)
    ChrSetPos(0x000A, -10100, 0, -2700, 347)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrSetPos(0x000C, 6870, 0, 50, 90)
    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x000E, -116000, -4000, -113000, 270)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x000F, 8650, 0, -1120, 274)

    Jump('loc_8FB')

    def _loc_7B2(): pass

    label('loc_7B2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_81C',
    )

    ChrClearFlags(0x000D, 0x0080)
    ChrSetPos(0x000D, -100400, 0, -101990, 103)
    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x000E, -113390, -4000, -111160, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 6, 0x516)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_803',
    )

    ChrSetPos(0x000E, -116000, -4000, -113000, 270)
    ChrSetFlags(0x000E, 0x0010)

    def _loc_803(): pass

    label('loc_803')

    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x000F, 8650, 0, -1120, 274)

    Jump('loc_8FB')

    def _loc_81C(): pass

    label('loc_81C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_872',
    )

    ChrClearFlags(0x000D, 0x0080)
    ChrSetPos(0x000D, -120940, -4000, -106020, 182)
    ChrSetFlags(0x000D, 0x0010)
    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x000E, -120920, -4000, -107100, 355)
    ChrSetFlags(0x000E, 0x0010)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x000F, 8650, 0, -1120, 274)

    Jump('loc_8FB')

    def _loc_872(): pass

    label('loc_872')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Return,
        ),
        'loc_8C3',
    )

    ChrClearFlags(0x000D, 0x0080)
    ChrSetPos(0x000D, -100740, -4000, -111030, 12)
    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x000E, -116000, -4000, -113000, 270)
    ChrSetFlags(0x000E, 0x0010)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x000F, 8650, 0, -1120, 274)

    Jump('loc_8FB')

    def _loc_8C3(): pass

    label('loc_8C3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_8FB',
    )

    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x000E, -116000, -4000, -113000, 270)
    ChrSetFlags(0x000E, 0x0010)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x000F, 8650, 0, -1120, 274)

    def _loc_8FB(): pass

    label('loc_8FB')

    Return()

# id: 0x0001 offset: 0x8FC
@scena.Code('func_01_8FC')
def func_01_8FC():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A7, 2, 0x53A)),
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 0, 0x558)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_91E',
    )

    MapSetFlags(0x00000800)
    OP_1B(0x03, 0x00, 0x0003)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x54),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_94B')

    def _loc_91E(): pass

    label('loc_91E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 2, 0x532)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 6, 0x536)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_936',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x52),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_94B')

    def _loc_936(): pass

    label('loc_936')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 4, 0x52C)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 2, 0x532)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_94B',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x51),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_94B(): pass

    label('loc_94B')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x0000006C, 'loc_95B'),
        (0x0000006D, 'loc_95B'),
        (-1, 'loc_993'),
    )

    def _loc_95B(): pass

    label('loc_95B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 6, 0x516)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_98B',
    )

    OP_71(0x0006, 0x0004)
    OP_75(0xFF, 0x0000000F, 0x05)
    OP_75(0xFF, 0x00000018, 0x05)
    OP_75(0xFF, 0x00000024, 0x05)
    OP_75(0xFF, 0x00000033, 0x05)

    Jump('loc_990')

    def _loc_98B(): pass

    label('loc_98B')

    PlaySE(160, 0x01, 0x64)

    def _loc_990(): pass

    label('loc_990')

    Jump('loc_999')

    def _loc_993(): pass

    label('loc_993')

    OP_23(0x00A0)

    Jump('loc_999')

    def _loc_999(): pass

    label('loc_999')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 2, 0x50A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_9B0',
    )

    OP_6F(0x0005, 0)
    OP_72(0x0005, 0x0010)

    Jump('loc_9B4')

    def _loc_9B0(): pass

    label('loc_9B0')

    OP_64(0x05, 0x0001)

    def _loc_9B4(): pass

    label('loc_9B4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A7, 5, 0x53D)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 1, 0x519)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_9E2',
    )

    OP_65(0x00, 0x0001)
    OP_72(0x0008, 0x0004)
    OP_A1(0x0014, 0x0008)
    ChrSetPos(0x0014, -109320, -3300, -109150, 14)

    Jump('loc_9E6')

    def _loc_9E2(): pass

    label('loc_9E2')

    OP_64(0x00, 0x0001)

    def _loc_9E6(): pass

    label('loc_9E6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 4, 0x52C)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 6, 0x536)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_B76',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 2, 0x532)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B4A',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x64),
            Expr.Equ,
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x66),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_AAE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A8, 7, 0x547)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_AA7',
    )

    LoadEffect(0x01, 'map\\\\mpfog.eff')
    PlayEffect(0x01, 0x01, 0x00FF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    LoadEffect(0x00, 'map\\\\mpsmk0.eff')
    PlayEffect(0x00, 0x00, 0x00FF, -9880, 0, -3600, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    Jump('loc_AAB')

    def _loc_AA7(): pass

    label('loc_AA7')

    OP_64(0x01, 0x0001)

    def _loc_AAB(): pass

    label('loc_AAB')

    Jump('loc_B4A')

    def _loc_AAE(): pass

    label('loc_AAE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A9, 0, 0x548)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B46',
    )

    LoadEffect(0x01, 'map\\\\mpfog.eff')
    PlayEffect(0x01, 0x01, 0x00FF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    LoadEffect(0x00, 'map\\\\mpsmk0.eff')
    PlayEffect(0x00, 0x02, 0x00FF, -98280, -4000, -103420, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    Jump('loc_B4A')

    def _loc_B46(): pass

    label('loc_B46')

    OP_64(0x02, 0x0001)

    def _loc_B4A(): pass

    label('loc_B4A')

    OP_72(0x0000, 0x0010)
    OP_72(0x0003, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 2, 0x532)),
            Expr.Return,
        ),
        'loc_B73',
    )

    OP_72(0x0000, 0x0010)
    OP_6F(0x0000, 30)
    OP_72(0x0000, 0x0010)
    OP_10(0x01, 0x00)
    OP_64(0x06, 0x0001)

    def _loc_B73(): pass

    label('loc_B73')

    Jump('loc_B86')

    def _loc_B76(): pass

    label('loc_B76')

    OP_64(0x01, 0x0001)
    OP_64(0x02, 0x0001)
    OP_64(0x06, 0x0001)
    OP_64(0x07, 0x0001)
    def _loc_B86(): pass

    label('loc_B86')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 6, 0x536)),
            Expr.Return,
        ),
        'loc_B90',
    )

    Jump('loc_B9F')

    def _loc_B90(): pass

    label('loc_B90')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_B9F',
    )

    OP_64(0x03, 0x0001)
    OP_64(0x04, 0x0001)

    def _loc_B9F(): pass

    label('loc_B9F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 4, 0x52C)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 2, 0x532)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_BB0',
    )

    OP_1B(0x00, 0x00, 0x0022)

    def _loc_BB0(): pass

    label('loc_BB0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 4, 0x534)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 6, 0x536)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_BC4',
    )

    OP_1B(0x03, 0x00, 0x0021)

    Jump('loc_BD5')

    def _loc_BC4(): pass

    label('loc_BC4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 5, 0x52D)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 2, 0x532)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_BD5',
    )

    OP_1B(0x03, 0x00, 0x0020)

    def _loc_BD5(): pass

    label('loc_BD5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 0, 0x558)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_BE7',
    )

    OP_10(0x0C, 0x01)
    OP_10(0x00, 0x00)

    def _loc_BE7(): pass

    label('loc_BE7')

    If(
        (
            (Expr.Eval, "OP_42(0x003B)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_BFA',
    )

    OP_1B(0x00, 0x00, 0x0010)

    def _loc_BFA(): pass

    label('loc_BFA')

    If(
        (
            (Expr.Eval, "OP_42(0x003B)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C0D',
    )

    OP_1B(0x03, 0x00, 0x0011)

    def _loc_C0D(): pass

    label('loc_C0D')

    Return()

# id: 0x0002 offset: 0xC0E
@scena.Code('func_02_C0E')
def func_02_C0E():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_C23',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_C0E')

    def _loc_C23(): pass

    label('loc_C23')

    Return()

# id: 0x0003 offset: 0xC24
@scena.Code('func_03_C24')
def func_03_C24():
    MapClearFlags(0x00000800)
    OP_1B(0x03, 0x00, 0xFFFF)

    Return()

# id: 0x0004 offset: 0xC2F
@scena.Code('func_04_C2F')
def func_04_C2F():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 6, 0x536)),
            Expr.Return,
        ),
        'loc_D92',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_CE3',
    )

    ChrTalk(
        0x00FE,
        (
            '啊～怎么办呢。\n',
            '浅显易懂的说明吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但、但是除了性能以外的东西\n',
            '我就没办法说明了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '（唉，\n',
            '　才刚刚发生那样的事情，\n',
            '　没有卖东西的心情了啊……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D92')

    def _loc_CE3(): pass

    label('loc_CE3')

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    ChrTalk(
        0x00FE,
        (
            '啊……真是为难。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '性能方面\n',
            '这一种型号的透镜色差很小，\n',
            '我大胆向你推荐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯？是吗？\n',
            '使用方便的相机吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽、虽然说使用方便，\n',
            '也要看各人的具体情况吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D92(): pass

    label('loc_D92')

    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0xD96
@scena.Code('func_05_D96')
def func_05_D96():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_1165',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0004, 0x00, 0x10)"),
            (Expr.TestScenaFlags, ScenaFlag(0x00B0, 3, 0x583)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_10BE',
    )

    SetScenaFlags(ScenaFlag(0x00B0, 3, 0x583))
    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哟，好久不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#014F……？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#010F啊，我还以为是谁呢……\n',
            '真的是好久不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#501F嗯？是谁啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F呵呵，就是在洛连特\n',
            '寻找齿轮的那个孩子啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我们之前不是\n',
            '接受过他的委托去找那碎片吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '了不起呢，\n',
            '今天给母亲帮忙吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '啊啊，帮忙做一下吧。\n',
            '差不多要回卡尔瓦德了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……我决定，等我的\n',
            '几个妹妹再长大点之后，\n',
            '就来这个城市。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为做见习生就可以进入工房，\n',
            '然后将来就可以造飞船了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我的手很巧，\n',
            '这点连我老妈也是知道的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '这样也挺不错啊。\n',
            '已经找到了将来的目标。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '那当然的啦。\n',
            '我也要考虑自己的前途才行呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……唉，不过\n',
            '现在还是要先给老妈帮忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我有四个妹妹，\n',
            '年纪还都很小呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#006F嗯！你要努力帮忙哦。\n',
            '就算是为了你的几个妹妹。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '啊，谢谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '再见了，\n',
            '你们也加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1162')

    def _loc_10BE(): pass

    label('loc_10BE')

    ChrTalk(
        0x00FE,
        (
            '……我决定，等我的\n',
            '几个妹妹再长大点之后，\n',
            '就来这个城市。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为做见习生就可以进入工房，\n',
            '然后将来就可以造飞船了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我的手很巧，\n',
            '这点连我老妈也是知道的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1162(): pass

    label('loc_1162')

    Jump('loc_1590')

    def _loc_1165(): pass

    label('loc_1165')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_1534',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0004, 0x00, 0x10)"),
            (Expr.TestScenaFlags, ScenaFlag(0x00B0, 3, 0x583)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_145F',
    )

    SetScenaFlags(ScenaFlag(0x00B0, 3, 0x583))
    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哟，好久不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#014F……？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#010F啊，我还以为是谁呢……\n',
            '真的是好久不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#501F嗯？是谁啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F呵呵，就是在洛连特\n',
            '寻找齿轮的那个孩子啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我们之前不是\n',
            '接受过他的委托去找那碎片吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '了不起呢，\n',
            '今天给母亲帮忙吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '啊啊，帮忙做一下吧。\n',
            '差不多要回卡尔瓦德了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……我决定，等我的\n',
            '几个妹妹再长大点之后，\n',
            '就来这个城市。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为做见习生就可以进入工房，\n',
            '然后将来就可以造飞船了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '这样也挺不错啊。\n',
            '已经找到了将来的目标。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '那当然的啦。\n',
            '我也要考虑自己的前途才行呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……唉，不过\n',
            '现在还是要先给老妈帮忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我有四个妹妹，\n',
            '年纪还都很小呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#006F嗯！你要努力帮忙哦。\n',
            '就算是为了你的几个妹妹。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '啊，谢谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '再见了，\n',
            '你们也加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1531')

    def _loc_145F(): pass

    label('loc_145F')

    ChrTalk(
        0x00FE,
        (
            '等我家的几个妹妹\n',
            '再长大点之后，我\n',
            '就来这个城市。    ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为做见习生就可以进入工房，\n',
            '然后将来就可以造飞船了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……唉，不过\n',
            '现在还是要先给老妈帮忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我有四个妹妹，\n',
            '现在还很小，\n',
            '妈妈也很辛苦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1531(): pass

    label('loc_1531')

    Jump('loc_1590')

    def _loc_1534(): pass

    label('loc_1534')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 6, 0x536)),
            Expr.Return,
        ),
        'loc_1590',
    )

    ChrTalk(
        0x00FE,
        (
            '…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……了不起……………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '导力引擎\n',
            '是在这里做的啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1590(): pass

    label('loc_1590')

    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0x1594
@scena.Code('func_06_1594')
def func_06_1594():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_1623',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，这次的生意\n',
            '马上就要搞定了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '销售很顺利，\n',
            '进货也很顺利。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我家的卡雷尔\n',
            '似乎也确定了什么目标。\n',
            '嗯，这次非常好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17B2')

    def _loc_1623(): pass

    label('loc_1623')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_16A4',
    )

    ChrTalk(
        0x00FE,
        (
            '我是来拿\n',
            '在这里订购的导力相机的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '令人惊喜的是\n',
            '儿子也开始给我帮忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '卡雷尔那孩子\n',
            '好像有点变化了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17B2')

    def _loc_16A4(): pass

    label('loc_16A4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 6, 0x536)),
            Expr.Return,
        ),
        'loc_17B2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_170F',
    )

    ChrTalk(
        0x00FE,
        (
            '似乎发生了什么事呢，\n',
            '不过我只知道情况很严重。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '能不能简单明了地\n',
            '给我说明一下啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17B2')

    def _loc_170F(): pass

    label('loc_170F')

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x00FE,
        (
            '哎呀，我都说了，\n',
            '我不是询问你\n',
            '那些具体数字方面的情况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只是问问哪种相机操作简单，\n',
            '最适合新手使用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '相机不是你制造的吗？\n',
            '你就没有考虑过这些事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_17B2(): pass

    label('loc_17B2')

    TalkEnd(0x00FE)

    Return()

# id: 0x0007 offset: 0x17B6
@scena.Code('func_07_17B6')
def func_07_17B6():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 6, 0x536)),
            Expr.Return,
        ),
        'loc_181F',
    )

    ChrTalk(
        0x0010,
        (
            '#0280091647V#150F嗯～\n',
            '来五套普通的吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280091648V啊，对了对了，\n',
            '还要买全景摄影的器材。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_181F(): pass

    label('loc_181F')

    TalkEnd(0x00FE)

    Return()

# id: 0x0008 offset: 0x1823
@scena.Code('func_08_1823')
def func_08_1823():
    TalkBegin(0x000F)
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
            TXT(0x01, '改造·换钱\n'),
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
        'loc_1885',
    )

    OP_0D()
    OP_A9(0x3C)
    OP_56(0x00)
    TalkEnd(0x000F)

    Return()

    def _loc_1885(): pass

    label('loc_1885')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1896',
    )

    TalkEnd(0x000F)

    Return()

    def _loc_1896(): pass

    label('loc_1896')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_18F3',
    )

    ChrTalk(
        0x000F,
        (
            '欢迎来到维修柜台。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '虽然总是出一些乱子，\n',
            '但我还是会调整好心情努力工作的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F0D')

    def _loc_18F3(): pass

    label('loc_18F3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_195F',
    )

    ChrTalk(
        0x000F,
        (
            '嗯，怎么回事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '工房船的船员怎么\n',
            '慌慌张张地跑来跑去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '难道是什么地方\n',
            '发生事故了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F0D')

    def _loc_195F(): pass

    label('loc_195F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_19AF',
    )

    ChrTalk(
        0x000F,
        (
            '早上好。\n',
            '欢迎，这里是维修柜台。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '好的，\n',
            '今天也要努力工作啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F0D')

    def _loc_19AF(): pass

    label('loc_19AF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_1A32',
    )

    ChrTalk(
        0x000F,
        (
            '啊，谢谢了。\n',
            '干到这么晚真是辛苦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '现在我还在工作，\n',
            '有什么事的话请尽管说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '呼，今天出了很多事，\n',
            '真是累啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F0D')

    def _loc_1A32(): pass

    label('loc_1A32')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 6, 0x536)),
            Expr.Return,
        ),
        'loc_1BC9',
    )

    If(
        (
            (Expr.PushLong, 0x5),
            Expr.Return,
        ),
        'loc_1B19',
    )

    ChrTalk(
        0x000F,
        (
            '从导力相机到导力枪，\n',
            '加鲁诺都能从事开发，\n',
            '真是个具有广博开发实力的人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '在这个中央工房里，\n',
            '以拉赛尔博士为首，\n',
            '这种全能型的研究者真的很多呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '研究者工作的时候， \n',
            '肯定会毫无隔阂地彼此学习和交流吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1BC6')

    def _loc_1B19(): pass

    label('loc_1B19')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x000F,
        (
            '呼呼，\n',
            '刚刚才在想骚乱终于平息了，\n',
            '这下又来了个不得了的客人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '虽然是位大娘，\n',
            '不过一来就开始发牢骚呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '开发部的加鲁诺来帮我给她说明了，\n',
            '应该没有问题了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1BC6(): pass

    label('loc_1BC6')

    Jump('loc_1F0D')

    def _loc_1BC9(): pass

    label('loc_1BC9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_1C60',
    )

    ChrTalk(
        0x000F,
        (
            '在那边自言自语的客人\n',
            '似乎对导力器这种东西\n',
            '还不太了解。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '怎么办啊？\n',
            '是不是需要给他详细地说明一下呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '唔～连我也开始自言自语了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F0D')

    def _loc_1C60(): pass

    label('loc_1C60')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_1CE8',
    )

    ChrTalk(
        0x000F,
        (
            '啊，客人您好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '怎么样？\n',
            '不看看结晶回路吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '我自己这样说可能有点自卖自夸，\n',
            '不过这批货质量真的不错，品种也齐全。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F0D')

    def _loc_1CE8(): pass

    label('loc_1CE8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_1DD1',
    )

    ChrTalk(
        0x000F,
        (
            '啊，谢谢了。\n',
            '哎呀～今天一大早就开始忙碌起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '我们要检查昨天的事故\n',
            '是否给导力器造成故障和错误……\n',
            '光做这些应对工作就已经忙死了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '嗯，其实导力器技术的相关知识\n',
            '对于蔡斯的市民们来说\n',
            '也并不是显得那么高深莫测。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F0D')

    def _loc_1DD1(): pass

    label('loc_1DD1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Return,
        ),
        'loc_1E81',
    )

    ChrTalk(
        0x000F,
        (
            '欢迎来到维修柜台。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '其实我也是\n',
            '中央工房的研究员，\n',
            '不过现在还只是处于见习阶段。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '修理导力器\n',
            '也是我修行的一部分。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '什么时候我也有\n',
            '自己的研究室就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F0D')

    def _loc_1E81(): pass

    label('loc_1E81')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_1F0D',
    )

    ChrTalk(
        0x000F,
        (
            '欢迎来到维修柜台。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '虽说是柜台，\n',
            '但这里可是中央工房\n',
            '直接运营的导力器工房。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '这里和一般的工房没什么区别，\n',
            '请放心使用吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1F0D(): pass

    label('loc_1F0D')

    TalkEnd(0x000F)

    Return()

# id: 0x0009 offset: 0x1F11
@scena.Code('func_09_1F11')
def func_09_1F11():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 6, 0x516)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A7, 5, 0x53D)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_27A7',
    )

    TalkBegin(0x00FE)
    SetScenaFlags(ScenaFlag(0x00A7, 5, 0x53D))
    MapClearFlags(0x00000001)
    EventBegin(0x00)
    Fade(1000)
    ChrSetPos(0x0101, -114810, -4000, -111130, 90)
    ChrSetPos(0x0102, -114650, -4000, -112120, 45)
    ChrTurnDirection(0x000E, 0x0101, 0)
    OP_69(0x000E, 1000)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1F99',
    )

    ChrTalk(
        0x0101,
        (
            '#0010071468V#000F那个～能打扰一下吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1FCD')

    def _loc_1F99(): pass

    label('loc_1F99')

    ChrTalk(
        0x0102,
        (
            '#0020071469V#010F不好意思。\n',
            '请问能打扰一下吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1FCD(): pass

    label('loc_1FCD')

    ChrTalk(
        0x000E,
        (
            '#1980071470V#2P怎么，有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔他们向管理员菲\n',
            '说明了有关拉赛尔博士需要汽油的委托。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x000E,
        (
            '#1980071471V#2P哦～汽油啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#1980071472V#2P保管库里\n',
            '的确有几桶库存……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#1980071473V#2P稍等一下，我问问。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_20C8')
    def lambda_20C8():
        CameraMove(-112600, -4000, -109400, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_20C8)

    ChrSetDirection(0x000E, 0, 400)
    WaitForThreadExit(0x0101, 0x0002)
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '菲拨通了内线电话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x000E,
        (
            '#1980071474V#2P我是菲。\n',
            '有件事想问问你。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#1980071475V#2P共和国产的汽油，\n',
            '应该还有些库存对吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#1980071476V#2P嗯、嗯……\n',
            '给我送一桶过来行吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#1980071477V#2P要一桶可以带着走的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#1980071478V#2P谢了，拜托啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000E, 0x0101, 400)

    ChrTalk(
        0x000E,
        (
            '#1980071479V#2P稍等一下。\n',
            '马上就传送过来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020071480V#014F传送过来……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000E, 90, 400)
    OP_72(0x0008, 0x0004)
    OP_A1(0x0014, 0x0008)
    ChrSetPos(0x0014, -95360, -3300, -109080, 14)
    ChrSetFlags(0x0014, 0x0040)
    ChrSetFlags(0x0014, 0x0004)

    @scena.Lambda('lambda_228B')
    def lambda_228B():
        ChrMoveTo(0x00FE, -109320, -3300, -109150, 1600, 0x00)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_228B)

    PlaySE(91, 0x01, 0x64)
    OP_76(0x00FF, 0x0000000F, 0x0001, 2, 0, 1000, 0x00, 0x00)
    OP_76(0x00FF, 0x00000018, 0x0001, 2, 0, 1000, 0x00, 0x00)
    OP_76(0x00FF, 0x00000024, 0x0001, 2, 0, 1000, 0x00, 0x00)
    OP_76(0x00FF, 0x00000033, 0x0001, 2, 0, 1000, 0x00, 0x00)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010071481V#004F哇哇……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#1980071482V来了来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2347')
    def lambda_2347():
        CameraMove(-105100, -4000, -108200, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2347)

    @scena.Lambda('lambda_235F')
    def lambda_235F():
        ChrWalkTo(0x00FE, -107900, -4000, -111300, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_235F)

    Sleep(800)

    @scena.Lambda('lambda_237F')
    def lambda_237F():
        ChrWalkTo(0x00FE, -109600, -4000, -111100, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_237F)

    Sleep(500)

    @scena.Lambda('lambda_239F')
    def lambda_239F():
        ChrWalkTo(0x00FE, -110700, -4000, -111300, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_239F)

    WaitForThreadExit(0x000E, 0x0001)

    @scena.Lambda('lambda_23BF')
    def lambda_23BF():
        ChrTurnDirection(0x00FE, 0x0014, 400)
        Yield()

        Jump('lambda_23BF')

    DispatchAsync2(0x000E, 0x0001, lambda_23BF)

    WaitForThreadExit(0x0101, 0x0001)

    @scena.Lambda('lambda_23D5')
    def lambda_23D5():
        ChrTurnDirection(0x00FE, 0x0014, 400)
        Yield()

        Jump('lambda_23D5')

    DispatchAsync2(0x0101, 0x0001, lambda_23D5)

    WaitForThreadExit(0x0102, 0x0001)

    @scena.Lambda('lambda_23EB')
    def lambda_23EB():
        ChrTurnDirection(0x00FE, 0x0014, 400)
        Yield()

        Jump('lambda_23EB')

    DispatchAsync2(0x0102, 0x0001, lambda_23EB)

    @scena.Lambda('lambda_23FC')
    def lambda_23FC():
        CameraMove(-108840, -4000, -109520, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_23FC)

    WaitForThreadExit(0x0014, 0x0001)
    OP_75(0xFF, 0x0000000F, 0x05)
    OP_75(0xFF, 0x00000018, 0x05)
    OP_75(0xFF, 0x00000024, 0x05)
    OP_75(0xFF, 0x00000033, 0x05)
    OP_23(0x005B)
    WaitForThreadExit(0x0101, 0x0003)

    ChrTalk(
        0x0101,
        (
            '#0010071483V#501F哎呀～\n',
            '难道说这个桶里就是汽油吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020071484V#010F『传送过来』\n',
            '原来就是这个意思啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x000E, 0xFF)
    ChrTurnDirection(0x000E, 0x0101, 400)

    ChrTalk(
        0x000E,
        (
            '#1980071485V#2P呵呵，了不起吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#1980071486V#2P给你们介绍一下，\n',
            '这个传送系统不光能运送制品。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#1980071487V#2P它还有连接着\n',
            '广大的地下工场的功能呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x000E, 400)
    ChrTurnDirection(0x0101, 0x000E, 400)

    ChrTalk(
        0x0101,
        (
            '#0010071488V#004F啊，很方便嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#1980071489V#2P这也是拉赛尔博士所提出的方案哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#1980071490V#2P原本这个传送带\n',
            '只有运送制品的机能……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#1980071491V#2P是那个老爷子把它改造成了\n',
            '相当有用的系统。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#1980071492V#2P不过话说回来，\n',
            '在基础设施整理完善之前可是辛苦死了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010071493V#506F啊哈哈。\n',
            '不愧是博士的杰作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020071494V#010F那么感谢您的帮忙，\n',
            '这桶汽油我们就带走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000E, 0x0101, 400)

    ChrTalk(
        0x000E,
        (
            '#1980071495V#2P好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#1980071496V#2P啊，不知道你们用它来干什么，\n',
            '但处理起来一定要注意哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#1980071497V#2P汽油这种东西\n',
            '可是非常容易燃烧的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_65(0x00, 0x0001)
    EventEnd(0x00)
    CreateThread(0x000E, 0x00, 0x00, func_02_C0E)

    Jump('loc_318A')

    def _loc_27A7(): pass

    label('loc_27A7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_2820',
    )

    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '不好意思，\n',
            '还要你们专程送过来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们这么忙还帮我，\n',
            '真是太感谢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，\n',
            '我要回去工作了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

    def _loc_2820(): pass

    label('loc_2820')

    If(
        (
            (Expr.Eval, "OP_29(0x0031, 0x00, 0x08)"),
            (Expr.Eval, "OP_29(0x0031, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0031, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_284A',
    )

    If(
        (
            (Expr.Eval, "OP_40(0x035E)"),
            Expr.Return,
        ),
        'loc_284A',
    )

    Call(1, 0x0001)
    TalkEnd(0x00FE)

    Return()

    def _loc_284A(): pass

    label('loc_284A')

    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_294A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_28B6',
    )

    ChrTalk(
        0x00FE,
        (
            '不过，\n',
            '这难道真的是军队的所作所为……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '听到真相的时候\n',
            '对大家的打击确实不小呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2947')

    def _loc_28B6(): pass

    label('loc_28B6')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '啊……是你们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '谢谢你们救出了博士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然不能完全放心，\n',
            '不过现在的情况已经不错了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '希望以后你们也能\n',
            '作为市民的坚强依靠。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2947(): pass

    label('loc_2947')

    Jump('loc_318A')

    def _loc_294A(): pass

    label('loc_294A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_2B14',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_2A69',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0031, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_29CA',
    )

    ChrTalk(
        0x00FE,
        (
            '唉，怎么办啊。\n',
            '我又不能放下鲁迪不管。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '难得布拉姆\n',
            '给我写封信……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，\n',
            '真是太不凑巧了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A66')

    def _loc_29CA(): pass

    label('loc_29CA')

    ChrTalk(
        0x00FE,
        (
            '唉，怎么办啊。\n',
            '我又不能放下鲁迪不管。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没想到，\n',
            '我还挂念着那个没用的家伙……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊……\n',
            '怎么会这样呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这么说，\n',
            '我难道只能喜欢没用的男人吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2A66(): pass

    label('loc_2A66')

    Jump('loc_2B11')

    def _loc_2A69(): pass

    label('loc_2A69')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '唉，怎么办啊。\n',
            '真是头痛……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总觉得最近\n',
            '好像特别在意鲁迪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '其实也算不上喜欢吧，\n',
            '总之就是觉得\n',
            '不能丢下不管……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，真是讨厌。\n',
            '完全没有心情工作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_2B11(): pass

    label('loc_2B11')

    Jump('loc_318A')

    def _loc_2B14(): pass

    label('loc_2B14')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_2C09',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0031, 0x00, 0x10)"),
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2B7A',
    )

    ChrTalk(
        0x00FE,
        (
            '呼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '鲁迪也罢，\n',
            '布拉姆也罢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为什么我周围\n',
            '只有这种男人呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2C06')

    def _loc_2B7A(): pass

    label('loc_2B7A')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '我之前还严厉地\n',
            '训斥了鲁迪一顿……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那家伙整天闷闷不乐，\n',
            '工作也不干。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，真是没有办法。\n',
            '于是我就说『你也拿点血性出来啊』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2C06(): pass

    label('loc_2C06')

    Jump('loc_318A')

    def _loc_2C09(): pass

    label('loc_2C09')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 6, 0x536)),
            Expr.Return,
        ),
        'loc_2D2C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_2CB4',
    )

    ChrTalk(
        0x00FE,
        (
            '我正在工作的时候，\n',
            '工房突然间浓烟滚滚。\n',
            '我慌慌张张就逃向一楼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '鲁迪那家伙，傻呆呆的，\n',
            '吸了一肚子烟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为慎重起见，\n',
            '他刚刚去医务室做检查了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2D29')

    def _loc_2CB4(): pass

    label('loc_2CB4')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '我正在工作的时候，\n',
            '工房突然浓烟滚滚……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我慌慌张张就逃到一楼去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我想犯人们\n',
            '肯定是从地下进来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2D29(): pass

    label('loc_2D29')

    Jump('loc_318A')

    def _loc_2D2C(): pass

    label('loc_2D2C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_2E36',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0031, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_2DC6',
    )

    ChrTalk(
        0x00FE,
        (
            '现在必须把信的事放一边，\n',
            '集中精神工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不然的话，\n',
            '就没法给布拉姆起示范……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……啊，不对。\n',
            '就没法给鲁迪\n',
            '起示范作用了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2E33')

    def _loc_2DC6(): pass

    label('loc_2DC6')

    ChrTalk(
        0x00FE,
        (
            '我刚刚才\n',
            '怒斥过鲁迪呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那家伙一直在发愣，\n',
            '手也不动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是的，\n',
            '以前他明明不像这么没用的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2E33(): pass

    label('loc_2E33')

    Jump('loc_318A')

    def _loc_2E36(): pass

    label('loc_2E36')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_2F18',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 6, 0x516)),
            Expr.Return,
        ),
        'loc_2E9B',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然不知道用它来做什么，\n',
            '但处理起来一定要注意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '汽油这东西\n',
            '非常容易燃烧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F15')

    def _loc_2E9B(): pass

    label('loc_2E9B')

    OP_62(0x000E, 0x00000000, 1700, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1200)

    OP_63(0x000E)

    ChrTalk(
        0x00FE,
        (
            '呼～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好了，菲。\n',
            '要集中精力工作啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '传输方面一切正常，\n',
            '接下来检查一下仓库吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2F15(): pass

    label('loc_2F15')

    Jump('loc_318A')

    def _loc_2F18(): pass

    label('loc_2F18')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_2F9D',
    )

    ChrTalk(
        0x00FE,
        (
            '首先要检查装置\n',
            '有没有受昨天的现象影响\n',
            '而出现传输问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为了慎重起见，检查完那个之后\n',
            '麻烦你去确认一下外面的器材。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_318A')

    def _loc_2F9D(): pass

    label('loc_2F9D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Return,
        ),
        'loc_30C1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_3029',
    )

    ChrTalk(
        0x00FE,
        (
            '我啊，\n',
            '怎么会喜欢上\n',
            '那样的家伙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '长得又不帅，\n',
            '还总是一副睡不醒的样子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，事到如今对我来说都是个谜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_30BE')

    def _loc_3029(): pass

    label('loc_3029')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '呼～～\n',
            '悲哀啊～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我怎么会喜欢上\n',
            '那样的家伙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '长得又不帅，\n',
            '还总是一副睡不醒的样子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……冷静地想一下，\n',
            '他真是没什么优点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_30BE(): pass

    label('loc_30BE')

    Jump('loc_318A')

    def _loc_30C1(): pass

    label('loc_30C1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_318A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_310D',
    )

    ChrTalk(
        0x00FE,
        (
            '好了，工作，工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '必须快点忘了\n',
            '那个傻瓜的事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_318A')

    def _loc_310D(): pass

    label('loc_310D')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '哈啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那个傻瓜\n',
            '现在在做什么呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……哎呀，不行不行，\n',
            '我正在工作，必须集中精神。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_318A(): pass

    label('loc_318A')

    TalkEnd(0x00FE)

    Return()

# id: 0x000A offset: 0x318E
@scena.Code('func_0A_318E')
def func_0A_318E():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_31FB',
    )

    ChrTalk(
        0x00FE,
        (
            '从工房船回来之后，\n',
            '菲前辈还是没什么精神啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '难、难道说，\n',
            '她和前男友的关系又有变化了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3797')

    def _loc_31FB(): pass

    label('loc_31FB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_324F',
    )

    ChrTalk(
        0x00FE,
        (
            '菲前辈\n',
            '刚才被别人叫走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '工房船那里好像\n',
            '接到了紧急出动的通知。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3797')

    def _loc_324F(): pass

    label('loc_324F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_3330',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_32B8',
    )

    ChrTalk(
        0x00FE,
        (
            '或许是我的错觉吧，\n',
            '最近常常和前辈目光相交啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……反正只是我\n',
            '自己胡思乱想吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_332D')

    def _loc_32B8(): pass

    label('loc_32B8')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '或许是我的错觉吧，\n',
            '最近常常和前辈目光相交啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '难、难道前辈终于\n',
            '发现我的魅力了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……唉，不会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_332D(): pass

    label('loc_332D')

    Jump('loc_3797')

    def _loc_3330(): pass

    label('loc_3330')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_338F',
    )

    ChrTalk(
        0x00FE,
        (
            '又被前辈教训，\n',
            '还出了那样的事，\n',
            '简直干劲全无啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼呼～～\n',
            '真想早点回家。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3797')

    def _loc_338F(): pass

    label('loc_338F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_3506',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_344A',
    )

    ChrTalk(
        0x00FE,
        (
            '刚才在工作的时候\n',
            '又被菲前辈骂了一顿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '肯定是因为前辈\n',
            '认为我是个没用的家伙……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呜呜，\n',
            '好不容易前辈和男友分手，\n',
            '我以为会有机会的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉～我真是没用啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3503')

    def _loc_344A(): pass

    label('loc_344A')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '唉……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '刚才在工作的时候\n',
            '又被菲前辈骂了一顿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '肯定是因为前辈\n',
            '认为我是个没用的家伙……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呜呜，\n',
            '好不容易前辈和男友分手，\n',
            '我以为会有机会的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉～我真是没用啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3503(): pass

    label('loc_3503')

    Jump('loc_3797')

    def _loc_3506(): pass

    label('loc_3506')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_35EE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_356F',
    )

    ChrTalk(
        0x00FE,
        (
            '明明我下定决心\n',
            '要努力工作呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可总是在意着前辈的前男友，\n',
            '根本不能专心工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_35EB')

    def _loc_356F(): pass

    label('loc_356F')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '嗯，菲前辈的前男友\n',
            '到底是谁啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '以前也找朋友们打听过，\n',
            '但是没人知道。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎呀，真是的！\n',
            '根本不能专心工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_35EB(): pass

    label('loc_35EB')

    Jump('loc_3797')

    def _loc_35EE(): pass

    label('loc_35EE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_362D',
    )

    ChrTalk(
        0x00FE,
        (
            '是，我明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，\n',
            '我去检查传输装置了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3797')

    def _loc_362D(): pass

    label('loc_362D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Return,
        ),
        'loc_3720',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_36A2',
    )

    ChrTalk(
        0x00FE,
        (
            '可是，前辈到底喜欢什么样的人\n',
            '我完全不知道呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……已经分手的男友\n',
            '会不会也在工房里工作呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_371D')

    def _loc_36A2(): pass

    label('loc_36A2')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '听说菲前辈她\n',
            '最近刚刚和男友分手呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈哈，\n',
            '机会终于降临到我的头上了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一定要好好努力，展示一下我的优点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_371D(): pass

    label('loc_371D')

    Jump('loc_3797')

    def _loc_3720(): pass

    label('loc_3720')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_3797',
    )

    ChrTalk(
        0x00FE,
        (
            '唔，\n',
            '加上这罐的话总共就有八罐了………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好了，和清单上的一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，\n',
            '接下来就交给工场那边检查吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3797(): pass

    label('loc_3797')

    TalkEnd(0x00FE)

    Return()

# id: 0x000B offset: 0x379B
@scena.Code('func_0B_379B')
def func_0B_379B():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 3, 0x603)),
            Expr.Return,
        ),
        'loc_3804',
    )

    ChrTalk(
        0x0008,
        (
            '刚刚，格斯塔夫维修长\n',
            '急急忙忙地赶了过来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '似乎相当匆忙呢。\n',
            '飞艇坪出什么事了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4A18')

    def _loc_3804(): pass

    label('loc_3804')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_3899',
    )

    ChrTalk(
        0x0008,
        (
            '各位。\n',
            '营救作战大家辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '虽然很想\n',
            '好好向大家致谢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '……为了以防万一，\n',
            '这些话还是等以后再说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '那么，请务必小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4A18')

    def _loc_3899(): pass

    label('loc_3899')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_39A8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_38DB',
    )

    ChrTalk(
        0x0008,
        (
            '……各位。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '营救博士的事\n',
            '就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_39A5')

    def _loc_38DB(): pass

    label('loc_38DB')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x0008,
        (
            '……各位，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '营救博士的事\n',
            '就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '提妲也不要\n',
            '太过勉强哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#560F知道了……\n',
            '我会小心行事的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#061F阿加特大哥哥已经教育我\n',
            '不能再那样鲁莽地行动了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#052F………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_39A5(): pass

    label('loc_39A5')

    Jump('loc_4A18')

    def _loc_39A8(): pass

    label('loc_39A8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_3A12',
    )

    ChrTalk(
        0x0008,
        (
            '哎呀，早上好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '提妲她\n',
            '应该是去了四楼的医务室吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '她真是相当担心\n',
            '阿加特的情况呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4A18')

    def _loc_3A12(): pass

    label('loc_3A12')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_3A66',
    )

    ChrTalk(
        0x0008,
        (
            '刚才被抬走的\n',
            '好像是一位游击士呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '看起来脸色很差，\n',
            '没关系吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4A18')

    def _loc_3A66(): pass

    label('loc_3A66')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A7, 0, 0x538)),
            Expr.Return,
        ),
        'loc_3AD9',
    )

    ChrTalk(
        0x0008,
        (
            '根据工房长的判断，\n',
            '拉赛尔博士被掳走的事\n',
            '还是对大多数人保密比较好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '博士的事，\n',
            '无论如何拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4A18')

    def _loc_3AD9(): pass

    label('loc_3AD9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 6, 0x536)),
            Expr.Return,
        ),
        'loc_3C06',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_3B51',
    )

    ChrTalk(
        0x0008,
        (
            '根据工房长的判断，\n',
            '拉赛尔博士被掳走的事\n',
            '还是对大多数人保密比较好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '提妲，\n',
            '你也不要这么灰心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3C03')

    def _loc_3B51(): pass

    label('loc_3B51')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x0008,
        (
            '啊，各位……\n',
            '提妲……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '……根据工房长的判断，\n',
            '拉赛尔博士被掳走的事\n',
            '还是对大多数人保密比较好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '提妲，\n',
            '你也不要这么灰心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#063F………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '……好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3C03(): pass

    label('loc_3C03')

    Jump('loc_4A18')

    def _loc_3C06(): pass

    label('loc_3C06')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_3DC1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B0, 1, 0x581)),
            Expr.Return,
        ),
        'loc_3C69',
    )

    ChrTalk(
        0x0008,
        (
            '我已经通知过\n',
            '游击士协会了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '那么，就麻烦你们\n',
            '将提妲护送到亚尔摩那里了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3DBE')

    def _loc_3C69(): pass

    label('loc_3C69')

    SetScenaFlags(ScenaFlag(0x00B0, 1, 0x581))

    ChrTalk(
        0x0008,
        (
            '啊，提妲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '亚尔摩旅馆的事，\n',
            '我从玛多克工房长那里打听到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '提妲，\n',
            '你是要代替爷爷去吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#060F啊，是的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我也曾经帮过忙，\n',
            '所以应该没问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F我们会负责\n',
            '把提妲护送到亚尔摩村。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '所以，请不用担心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我已经通知过\n',
            '游击士协会了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '那么提妲\n',
            '就拜托你们照顾了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#006F嗯，交给我们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#060F那我们走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3DBE(): pass

    label('loc_3DBE')

    Jump('loc_4A18')

    def _loc_3DC1(): pass

    label('loc_3DC1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 1, 0x519)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 0, 0x518)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3E88',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_3E1F',
    )

    ChrTalk(
        0x0008,
        (
            '竟然能够扛得动那么重的东西……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '游击士受过的锻炼\n',
            '就是不一样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3E85')

    def _loc_3E1F(): pass

    label('loc_3E1F')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))
    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '哇，竟然能\n',
            '扛得动那么重的东西……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '游击士受过的锻炼\n',
            '就是不一样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3E85(): pass

    label('loc_3E85')

    Jump('loc_4A18')

    def _loc_3E88(): pass

    label('loc_3E88')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 1, 0x519)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 0, 0x518)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_3FBD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 1, 0x519)),
            Expr.Return,
        ),
        'loc_3F44',
    )

    ChrTalk(
        0x0101,
        (
            '#505F嗯，已经有汽油了。\n',
            '接下来就是要找那个\n',
            '叫格斯塔夫维修长的人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我想维修长\n',
            '大概在飞艇坪那边吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '除了来中央工房汇报情况，\n',
            '其他的时候他都不怎么回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3FBA')

    def _loc_3F44(): pass

    label('loc_3F44')

    ChrTalk(
        0x0101,
        (
            '#505F嗯，已经将内燃引擎设备借来了。\n',
            '接下来该去导力器工场那里了……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '要去工场的话，\n',
            '请坐导力梯到地下一层。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3FBA(): pass

    label('loc_3FBA')

    Jump('loc_4A18')

    def _loc_3FBD(): pass

    label('loc_3FBD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 6, 0x516)),
            Expr.Return,
        ),
        'loc_4121',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_4026',
    )

    ChrTalk(
        0x0008,
        (
            '要去工场的话，\n',
            '请坐导力梯到地下一层。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '要找维修长的话，\n',
            '他大概在飞艇坪那边吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_411E')

    def _loc_4026(): pass

    label('loc_4026')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x0008,
        (
            '啊，各位。\n',
            '有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#505F唔～我们要去导力器工场，\n',
            '还要找一个叫格斯塔夫维修长的人。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '要去工场的话，\n',
            '请坐导力梯到地下一层。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '要找维修长的话，\n',
            '他大概在飞艇坪那边吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '除了来中央工房汇报情况，\n',
            '其他的时候他都不怎么回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_411E(): pass

    label('loc_411E')

    Jump('loc_4A18')

    def _loc_4121(): pass

    label('loc_4121')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_4313',
    )

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_41D7',
    )

    ChrTalk(
        0x0008,
        (
            '啊，各位。\n',
            '有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#505F唔～\n',
            '到演算室去就行了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '演算室在五楼。\n',
            '乘导力梯的话会很方便的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '如果还有什么事的话，\n',
            '请别客气，随时来找我问吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4310')

    def _loc_41D7(): pass

    label('loc_41D7')

    ChrTalk(
        0x0008,
        (
            '啊，各位。\n',
            '有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '【格斯塔夫维修长】\n',
            '【导力器生产工场】\n',
            '【没什么事】',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '格斯塔夫维修长\n',
            '平时都会呆在飞艇坪的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '飞艇坪位于\n',
            '工房前广场的东面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '还有什么其他的事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '工场就在地下。\n',
            '乘导力梯的话会很方便的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '还有什么其他的事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '如果还有什么事的话，\n',
            '请别客气，随时来找我问吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4310(): pass

    label('loc_4310')

    Jump('loc_4A18')

    def _loc_4313(): pass

    label('loc_4313')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_440F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_437A',
    )

    ChrTalk(
        0x0008,
        (
            '拉赛尔博士已经在三楼的工作室\n',
            '开始作业了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我想他应该正焦急地\n',
            '等人去帮忙吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_440C')

    def _loc_437A(): pass

    label('loc_437A')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))
    OP_28(0x003F, 0x01, 0x0040)

    ChrTalk(
        0x0008,
        (
            '提妲，还有各位。\n',
            '昨天真是发生了不得了的事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '拉赛尔博士已经在三楼的工作室\n',
            '开始作业了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我想他应该正焦急地\n',
            '等人去帮忙吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_440C(): pass

    label('loc_440C')

    Jump('loc_4A18')

    def _loc_440F(): pass

    label('loc_440F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Return,
        ),
        'loc_451B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_4450',
    )

    ChrTurnDirection(0x0008, 0x0107, 0)

    ChrTalk(
        0x0008,
        (
            '那么，提妲。\n',
            '就麻烦你为客人带路了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4518')

    def _loc_4450(): pass

    label('loc_4450')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))
    ChrTurnDirection(0x0008, 0x0107, 0)

    ChrTalk(
        0x0008,
        (
            '哎呀，是提妲啊。\n',
            '这是要去哪里啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#560F啊，\n',
            '我现在要带他们去我家呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '他们要找\n',
            '爷爷商量一些事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '是这样啊，真是辛苦你了。\n',
            '那就麻烦你给他们带路吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#061F好的，我们走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4518(): pass

    label('loc_4518')

    Jump('loc_4A18')

    def _loc_451B(): pass

    label('loc_451B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 4, 0x50C)),
            Expr.Return,
        ),
        'loc_4982',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 5, 0x50D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4946',
    )

    SetScenaFlags(ScenaFlag(0x00A1, 5, 0x50D))
    OP_28(0x003F, 0x01, 0x0002)
    EventBegin(0x00)
    Fade(1000)
    CameraMove(220, 0, 5230, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 440, 0, 3680, 0)
    ChrSetPos(0x0102, -560, 0, 3680, 0)
    ChrSetDirection(0x0008, 180, 0)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#1950070628V啊，\n',
            '你们是刚才和提妲一起的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1950070629V欢迎来到中央工房。\n',
            '请问有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070630V#006F啊～您好。\n',
            '我们是游击士协会的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070631V#010F其实是这样的……\n',
            '我们想和你们的工房长见面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0008, 180, 400)
    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '交出了',
            (TxtCtl.SetColor, 0x2),
            '给工房长的介绍信',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    RemoveItem(0x0360, 1)

    ChrTalk(
        0x0008,
        (
            '#1950070632V哦，是这样啊。\n',
            '请两位稍等一下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0008, 315, 400)
    ChrWalkTo(0x0008, -940, 0, 7500, 2000, 0x00)
    ChrSetDirection(0x0008, 0, 400)
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '接待员小姐拨通了内线电话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0008,
        (
            '#1950070633V——啊，工房长。\n',
            '不好意思，打扰您休息了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1950070634V嗯……是的。\n',
            '是游击士协会的人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1950070635V………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1950070636V嗯，我知道了。\n',
            '那好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0008, 135, 400)
    ChrWalkTo(0x0008, 260, 0, 5800, 2000, 0x00)
    ChrSetDirection(0x0008, 180, 400)

    ChrTalk(
        0x0008,
        (
            '#1950070637V久等了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1950070638V玛多克工房长说\n',
            '你们直接上楼找他就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1950070639V他现在就在二楼的工房长室，\n',
            '两位可以搭乘左手边的导力梯上去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070640V#001F太好了。\n',
            '马上就能见面了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070641V#010F那我们快去二楼吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Jump('loc_497F')

    def _loc_4946(): pass

    label('loc_4946')

    ChrTalk(
        0x0008,
        (
            '工房长室就在二楼。\n',
            '两位可以搭乘左手边的导力梯上去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_497F(): pass

    label('loc_497F')

    Jump('loc_4A18')

    def _loc_4982(): pass

    label('loc_4982')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_4A18',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 4, 0x50C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_49DF',
    )

    ChrTalk(
        0x0008,
        (
            '欢迎来到蔡斯中央工房。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '如果有什么事的话，\n',
            '请随时到前台这里咨询。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4A18')

    def _loc_49DF(): pass

    label('loc_49DF')

    ChrTalk(
        0x0008,
        (
            '工房长室就在二楼。\n',
            '两位可以搭乘左手边的导力梯上去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4A18(): pass

    label('loc_4A18')

    TalkEnd(0x0008)

    Return()

# id: 0x000C offset: 0x4A1C
@scena.Code('func_0C_4A1C')
def func_0C_4A1C():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 6, 0x536)),
            Expr.Return,
        ),
        'loc_4A79',
    )

    ChrSetFlags(0x00FE, 0x0010)
    TalkBegin(0x00FE)
    TalkSetChrName('中央工房１Ｆ')

    ChrTalk(
        0x00FE,
        (
            '咦，\n',
            '调到新型导力引擎的开发项目！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是，是说我吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    def _loc_4A79(): pass

    label('loc_4A79')

    Return()

# id: 0x000D offset: 0x4A7A
@scena.Code('func_0D_4A7A')
def func_0D_4A7A():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 6, 0x536)),
            Expr.Return,
        ),
        'loc_4B92',
    )

    ChrSetFlags(0x00FE, 0x0010)
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4B38',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '不好意思啊。\n',
            '刚出了那样的事，\n',
            '就让你过去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总之有些事情\n',
            '需要尽快跟你说明。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '开门见山地说吧……\n',
            '想让你成为『埃尔赛尤号』\n',
            '新型引擎开发工作的研究员。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4B8C')

    def _loc_4B38(): pass

    label('loc_4B38')

    ChrTalk(
        0x00FE,
        (
            '因为第一候补人\n',
            '谢绝了这个工作……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对你来说是个好机会。\n',
            '请好好考虑一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4B8C(): pass

    label('loc_4B8C')

    TalkEnd(0x00FE)

    Jump('loc_51B3')

    def _loc_4B92(): pass

    label('loc_4B92')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_51B3',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x002C, 0x00, 0x08)"),
            (Expr.Eval, "OP_29(0x002C, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4EE0',
    )

    MapSetFlags(0x00000080)
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
            TXT(0x00, '对话\n'),
            TXT(0x01, '询问烟草的事情\n'),
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
        'loc_4C0A',
    )

    Call(1, 0x0000)

    Return()

    def _loc_4C0A(): pass

    label('loc_4C0A')

    ChrSetFlags(0x00FE, 0x0010)
    TalkBegin(0x00FE)
    OP_4A(0x000B, 255)
    OP_4A(0x000A, 255)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AE, 5, 0x575)),
            Expr.Return,
        ),
        'loc_4CD2',
    )

    ChrTalk(
        0x000B,
        (
            '研究员辞掉了工作\n',
            '真让人头疼啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '总之，\n',
            '必须赶快开始研究对策……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '已经发生了的事也没有办法了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '就将这看作是\n',
            '重新策划的机会，\n',
            '我们要以积极的工作态度去应对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4ECD')

    def _loc_4CD2(): pass

    label('loc_4CD2')

    SetScenaFlags(ScenaFlag(0x00AE, 5, 0x575))

    ChrTalk(
        0x000B,
        (
            '啊！？\n',
            '真、真的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '新型导力引擎的研究员\n',
            '辞退不干了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '唉，\n',
            '以前明明答应下来的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '是不是出了什么事啊。\n',
            '前几天，接到了他谢绝的消息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '是这样啊……\n',
            '真是头疼啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '本来这个开发计划\n',
            '是为『埃尔赛尤号』设计的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '如果计划开始不了，\n',
            '『埃尔赛尤号』正式投入使用\n',
            '这一目标显然也就难以实现了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '唉唉，\n',
            '这个我明白啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '『埃尔赛尤号』\n',
            '现在的导力引擎\n',
            '也只是旧型号的翻版而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '总之，\n',
            '眼下必须赶快选出代替的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '就将这看作是\n',
            '重新策划的机会，\n',
            '我们要以积极的工作态度去应对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4ECD(): pass

    label('loc_4ECD')

    OP_4B(0x000A, 255)
    OP_4B(0x000B, 255)
    TalkEnd(0x00FE)
    ChrClearFlags(0x00FE, 0x0010)

    Jump('loc_51B3')

    def _loc_4EE0(): pass

    label('loc_4EE0')

    ChrSetFlags(0x00FE, 0x0010)
    TalkBegin(0x00FE)
    OP_4A(0x000B, 255)
    OP_4A(0x000A, 255)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AE, 5, 0x575)),
            Expr.Return,
        ),
        'loc_4FA8',
    )

    ChrTalk(
        0x000B,
        (
            '研究员辞掉了工作\n',
            '真让人头疼啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '总之，\n',
            '必须赶快开始研究对策……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '已经发生了的事也没有办法了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '就将这看作是\n',
            '重新策划的机会，\n',
            '我们要以积极的工作态度去应对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_51A3')

    def _loc_4FA8(): pass

    label('loc_4FA8')

    SetScenaFlags(ScenaFlag(0x00AE, 5, 0x575))

    ChrTalk(
        0x000B,
        (
            '啊！？\n',
            '真、真的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '新型导力引擎的研究员\n',
            '辞退不干了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '唉，\n',
            '以前明明答应下来的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '是不是出了什么事啊。\n',
            '前几天，接到了他谢绝的消息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '是这样啊……\n',
            '真是头疼啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '本来这个开发计划\n',
            '是为『埃尔赛尤号』设计的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '如果计划开始不了，\n',
            '『埃尔赛尤号』正式投入使用\n',
            '这一目标显然也就难以实现了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '唉唉，\n',
            '这个我明白啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '『埃尔赛尤号』\n',
            '现在的导力引擎\n',
            '也只是旧型号的翻版而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '总之，\n',
            '眼下必须赶快选出代替的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '就将这看作是\n',
            '重新策划的机会，\n',
            '我们要以积极的工作态度去应对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_51A3(): pass

    label('loc_51A3')

    OP_4B(0x000A, 255)
    OP_4B(0x000B, 255)
    TalkEnd(0x00FE)
    ChrClearFlags(0x00FE, 0x0010)

    def _loc_51B3(): pass

    label('loc_51B3')

    Return()

# id: 0x000E offset: 0x51B4
@scena.Code('func_0E_51B4')
def func_0E_51B4():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_548E',
    )

    ChrSetFlags(0x00FE, 0x0010)
    TalkBegin(0x00FE)
    OP_4A(0x000B, 255)
    OP_4A(0x000A, 255)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AE, 5, 0x575)),
            Expr.Return,
        ),
        'loc_5283',
    )

    ChrTalk(
        0x000B,
        (
            '研究员辞掉了工作\n',
            '真让人头疼啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '总之，\n',
            '必须赶快开始研究对策……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '已经发生了的事也没有办法了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '就将这看作是\n',
            '重新策划的机会，\n',
            '我们要以积极的工作态度去应对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_547E')

    def _loc_5283(): pass

    label('loc_5283')

    SetScenaFlags(ScenaFlag(0x00AE, 5, 0x575))

    ChrTalk(
        0x000B,
        (
            '啊！？\n',
            '真、真的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '新型导力引擎的研究员\n',
            '辞退不干了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '唉，\n',
            '以前明明答应下来的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '是不是出了什么事啊。\n',
            '前几天，接到了他谢绝的消息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '是这样啊……\n',
            '真是头疼啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '本来这个开发计划\n',
            '是为『埃尔赛尤号』设计的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '如果计划开始不了，\n',
            '『埃尔赛尤号』正式投入使用\n',
            '这一目标显然也就难以实现了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '唉唉，\n',
            '这个我明白啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '『埃尔赛尤号』\n',
            '现在的导力引擎\n',
            '也只是旧型号的翻版而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '总之，\n',
            '眼下必须赶快选出代替的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '就将这看作是\n',
            '重新策划的机会，\n',
            '我们要以积极的工作态度去应对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_547E(): pass

    label('loc_547E')

    OP_4B(0x000A, 255)
    OP_4B(0x000B, 255)
    ChrClearFlags(0x00FE, 0x0010)
    TalkEnd(0x00FE)

    def _loc_548E(): pass

    label('loc_548E')

    Return()

# id: 0x000F offset: 0x548F
@scena.Code('func_0F_548F')
def func_0F_548F():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_5568',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_54DA',
    )

    ChrTalk(
        0x00FE,
        (
            '采暖用的导力器\n',
            '竟然有那么多种……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，头痛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5568')

    def _loc_54DA(): pass

    label('loc_54DA')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '怎么办啊……真为难。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我一说想要\n',
            '采暖用的导力器，\n',
            '他就拿出厚厚一摞清单让我看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '竟然有那么多种……\n',
            '究竟都是些什么我完全不懂。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5568(): pass

    label('loc_5568')

    TalkEnd(0x00FE)

    Return()

# id: 0x0010 offset: 0x556C
@scena.Code('func_10_556C')
def func_10_556C():
    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_55E0',
    )

    ChrTalk(
        0x0102,
        (
            '#0020181107V#010F这边是出去的路……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020181108V要是出去的话，\n',
            '把安东尼留在工房里比较好。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5639')

    def _loc_55E0(): pass

    label('loc_55E0')

    ChrTurnDirection(0x0102, 0x0000, 400)

    ChrTalk(
        0x0102,
        (
            '#0020181105V#014F要出去吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020181106V那样的话，\n',
            '还是让安东尼回去比较好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5639(): pass

    label('loc_5639')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x3B),
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_565C',
    )

    @scena.Lambda('lambda_5654')
    def lambda_5654():
        ChrTurnDirection(0x0000, 0x013C, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_5654)

    def _loc_565C(): pass

    label('loc_565C')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Gtr,
            (Expr.PushValueByIndex, 0xB),
            (Expr.PushLong, 0x3B),
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_567F',
    )

    @scena.Lambda('lambda_5677')
    def lambda_5677():
        ChrTurnDirection(0x0001, 0x013C, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_5677)

    def _loc_567F(): pass

    label('loc_567F')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            (Expr.PushValueByIndex, 0xC),
            (Expr.PushLong, 0x3B),
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_56A2',
    )

    @scena.Lambda('lambda_569A')
    def lambda_569A():
        ChrTurnDirection(0x0002, 0x013C, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_569A)

    def _loc_56A2(): pass

    label('loc_56A2')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x3),
            Expr.Gtr,
            (Expr.PushValueByIndex, 0xD),
            (Expr.PushLong, 0x3B),
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_56C5',
    )

    @scena.Lambda('lambda_56BD')
    def lambda_56BD():
        ChrTurnDirection(0x0003, 0x013C, 400)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_56BD)

    def _loc_56C5(): pass

    label('loc_56C5')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x4),
            Expr.Gtr,
            (Expr.PushValueByIndex, 0xE),
            (Expr.PushLong, 0x3B),
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_56E8',
    )

    @scena.Lambda('lambda_56E0')
    def lambda_56E0():
        ChrTurnDirection(0x0004, 0x013C, 400)

        ExitThread()

    DispatchAsync(0x0004, 0x0001, lambda_56E0)

    def _loc_56E8(): pass

    label('loc_56E8')

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
            TXT(0x00, '【外出】\n'),
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
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5757',
    )

    ChrMoveToRelative(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

    def _loc_5757(): pass

    label('loc_5757')

    ChrTalk(
        0x0102,
        (
            '#0020181109V#010F那么，安东尼。\n',
            '我们就暂时在这里分开吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x013C, 0x0102, 400)
    PlaySE(402, 0x00, 0x64)

    ChrTalk(
        0x013C,
        (
            '#2030181110V喵～呜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    FormationDelMember(0x3B, 0xFF)
    NewScene('ED6_DT01/T3101._SN', 100, 0, 0)
    IdleLoop()
    EventEnd(0x02)

    Return()

# id: 0x0011 offset: 0x57D5
@scena.Code('func_11_57D5')
def func_11_57D5():
    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5849',
    )

    ChrTalk(
        0x0102,
        (
            '#0020181107V#010F这边是出去的路……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020181108V要是出去的话，\n',
            '把安东尼留在工房里比较好。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_58A2')

    def _loc_5849(): pass

    label('loc_5849')

    ChrTurnDirection(0x0102, 0x0000, 400)

    ChrTalk(
        0x0102,
        (
            '#0020181105V#014F要出去吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020181106V那样的话，\n',
            '还是让安东尼回去比较好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_58A2(): pass

    label('loc_58A2')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x3B),
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_58C5',
    )

    @scena.Lambda('lambda_58BD')
    def lambda_58BD():
        ChrTurnDirection(0x0000, 0x013C, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_58BD)

    def _loc_58C5(): pass

    label('loc_58C5')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Gtr,
            (Expr.PushValueByIndex, 0xB),
            (Expr.PushLong, 0x3B),
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_58E8',
    )

    @scena.Lambda('lambda_58E0')
    def lambda_58E0():
        ChrTurnDirection(0x0001, 0x013C, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_58E0)

    def _loc_58E8(): pass

    label('loc_58E8')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            (Expr.PushValueByIndex, 0xC),
            (Expr.PushLong, 0x3B),
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_590B',
    )

    @scena.Lambda('lambda_5903')
    def lambda_5903():
        ChrTurnDirection(0x0002, 0x013C, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_5903)

    def _loc_590B(): pass

    label('loc_590B')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x3),
            Expr.Gtr,
            (Expr.PushValueByIndex, 0xD),
            (Expr.PushLong, 0x3B),
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_592E',
    )

    @scena.Lambda('lambda_5926')
    def lambda_5926():
        ChrTurnDirection(0x0003, 0x013C, 400)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_5926)

    def _loc_592E(): pass

    label('loc_592E')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x4),
            Expr.Gtr,
            (Expr.PushValueByIndex, 0xE),
            (Expr.PushLong, 0x3B),
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5951',
    )

    @scena.Lambda('lambda_5949')
    def lambda_5949():
        ChrTurnDirection(0x0004, 0x013C, 400)

        ExitThread()

    DispatchAsync(0x0004, 0x0001, lambda_5949)

    def _loc_5951(): pass

    label('loc_5951')

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
            TXT(0x00, '【外出】\n'),
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
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_59C0',
    )

    ChrMoveToRelative(0x0000, 1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

    def _loc_59C0(): pass

    label('loc_59C0')

    ChrTalk(
        0x0102,
        (
            '#0020181109V#010F那么，安东尼。\n',
            '我们就暂时在这里分开吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x013C, 0x0102, 400)
    PlaySE(402, 0x00, 0x64)

    ChrTalk(
        0x013C,
        (
            '#2030181116V喵～呜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    FormationDelMember(0x3B, 0xFF)
    NewScene('ED6_DT01/R3403._SN', 101, 0, 0)
    IdleLoop()
    EventEnd(0x02)

    Return()

# id: 0x0012 offset: 0x5A3E
@scena.Code('func_12_5A3E')
def func_12_5A3E():
    Call(0, 0x000B)

    Return()

# id: 0x0013 offset: 0x5A43
@scena.Code('func_13_5A43')
def func_13_5A43():
    Call(0, 0x0008)

    Return()

# id: 0x0014 offset: 0x5A48
@scena.Code('func_14_5A48')
def func_14_5A48():
    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5AE0',
    )

    ChrTurnDirection(0x0107, 0x0001, 400)

    ChrTalk(
        0x0107,
        (
            '#0070070506V#560F啊，\n',
            '这个门是通往紧急通道的楼梯呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070070507V要去一楼的话，\n',
            '还是从左边的门回到走廊，\n',
            '然后一直走比较快。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5B69')

    def _loc_5AE0(): pass

    label('loc_5AE0')

    ChrTurnDirection(0x0107, 0x0000, 400)

    ChrTalk(
        0x0107,
        (
            '#0070070508V#560F啊，\n',
            '这个门是通往紧急通道的楼梯呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070070509V要去一楼的话，\n',
            '还是从左边的门回到走廊，\n',
            '然后一直走比较快。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5B69(): pass

    label('loc_5B69')

    TalkEnd(0x00FF)

    Return()

# id: 0x0015 offset: 0x5B6D
@scena.Code('func_15_5B6D')
def func_15_5B6D():
    MapClearFlags(0x00000001)
    EventBegin(0x00)
    ChrSetPos(0x0101, -109900, 0, -101300, 180)
    ChrSetPos(0x0102, -110700, 0, -100900, 180)
    ChrSetPos(0x0107, -109300, 0, -100900, 180)

    ChrTalk(
        0x0101,
        (
            '#0010070501V#004F哇～这、这里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_5BD4')
    def lambda_5BD4():
        ChrWalkTo(0x00FE, -110800, 0, -105000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5BD4)

    @scena.Lambda('lambda_5BEF')
    def lambda_5BEF():
        ChrWalkTo(0x00FE, -112000, 0, -104800, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_5BEF)

    @scena.Lambda('lambda_5C0A')
    def lambda_5C0A():
        ChrWalkTo(0x00FE, -109900, 0, -105200, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_5C0A)

    CameraMove(-110500, 0, -107800, 2000)

    ChrTalk(
        0x0102,
        (
            '#0020070502V#014F好厉害……\n',
            '是全自动化的工场啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070070503V#061F嘿嘿……\n',
            '这就是蔡斯市地下\n',
            '庞大的导力器工场入口。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070070504V从照明灯到飞艇部件，\n',
            '全部都是在这里制造的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070505V#501F哈～……\n',
            '感觉好有压迫感呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Return()

# id: 0x0016 offset: 0x5D1D
@scena.Code('func_16_5D1D')
def func_16_5D1D():
    EventBegin(0x00)
    PlaySE(14, 0x00, 0x64)
    CameraMove(3680, 0, -4580, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(20000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, -4700, 0, 9200, 180)
    ChrSetPos(0x0102, -4700, 0, 9200, 180)
    ChrSetPos(0x0107, -4700, 0, 9200, 180)
    FadeIn(1000, 0)

    @scena.Lambda('lambda_5DA3')
    def lambda_5DA3():
        CameraMove(-4950, 0, 6440, 4000)

        ExitThread()

    DispatchAsync(0x0107, 0x0002, lambda_5DA3)

    @scena.Lambda('lambda_5DBB')
    def lambda_5DBB():
        OP_6C(45000, 4000)

        ExitThread()

    DispatchAsync(0x0107, 0x0003, lambda_5DBB)

    WaitForThreadExit(0x0107, 0x0002)
    OP_70(0x0000, 30)
    OP_73(0x0000)
    Sleep(500)

    @scena.Lambda('lambda_5DDF')
    def lambda_5DDF():
        ChrWalkTo(0x00FE, -4900, 0, 4400, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5DDF)

    Sleep(500)

    ChrWalkTo(0x0107, -5000, 0, 7600, 3000, 0x00)

    @scena.Lambda('lambda_5E13')
    def lambda_5E13():
        ChrWalkTo(0x00FE, -4000, 0, 5900, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_5E13)

    Sleep(200)

    @scena.Lambda('lambda_5E33')
    def lambda_5E33():
        ChrWalkTo(0x00FE, -5900, 0, 5500, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_5E33)

    Sleep(1000)

    OP_6F(0x0000, 30)
    OP_70(0x0000, 0)

    ChrTalk(
        0x0101,
        (
            '#0010070540V#501F哎～\n',
            '这个地方好大呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0107, 0x0101, 400)

    ChrTalk(
        0x0107,
        (
            '#0070070541V#060F这里就是中央工房的一楼了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070070542V这里除了有接待柜台，\n',
            '还有面向一般客人的导力器维修柜台。\n',
            '所以说这里每天都是很热闹的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070543V#010F原来如此。\n',
            '从这里就能通往城镇了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4A(0x0008, 255)
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrSetDirection(0x0008, 270, 400)

    ChrTalk(
        0x0008,
        (
            '#1950070544V啊，提妲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_5FA6')
    def lambda_5FA6():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5FA6)

    @scena.Lambda('lambda_5FB4')
    def lambda_5FB4():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_5FB4)

    @scena.Lambda('lambda_5FC2')
    def lambda_5FC2():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_5FC2)

    CameraMove(-1900, 0, 7200, 1500)

    ChrTalk(
        0x0107,
        (
            '#0070070545V#064F啊，海泽尔姐姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1950070546V你来得正好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1950070547V特莱斯主任\n',
            '刚才在找你呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1950070548V说要你去一趟演算室。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070070549V#560F啊……\n',
            '好的，我明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070550V#506F哎呀呀。\n',
            '看来你好像有急事呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_60D9')
    def lambda_60D9():
        ChrTurnDirection(0x00FE, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_60D9)

    @scena.Lambda('lambda_60E7')
    def lambda_60E7():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_60E7)

    @scena.Lambda('lambda_60F5')
    def lambda_60F5():
        ChrTurnDirection(0x00FE, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_60F5)

    @scena.Lambda('lambda_6103')
    def lambda_6103():
        CameraMove(-4950, 0, 6440, 1500)

        ExitThread()

    DispatchAsync(0x0107, 0x0002, lambda_6103)

    ChrSetDirection(0x0008, 180, 400)
    OP_4B(0x0008, 255)
    WaitForThreadExit(0x0107, 0x0002)

    ChrTalk(
        0x0102,
        (
            '#0020070551V#010F谢谢你。\n',
            '要你特地带我们到城里来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070070552V#560F哪、哪儿的话。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070070553V刚才承蒙哥哥你们的照顾，\n',
            '该说谢谢的其实是我才对呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070554V#501F对了，提妲。\n',
            '我们两个会在蔡斯呆一段时间。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010070555V有机会的话，来找我们玩吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070070556V#064F啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070070557V#067F好呢，非常乐意！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070070558V那么，再见啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_628D')
    def lambda_628D():
        ChrTurnDirection(0x00FE, 0x0107, 0)
        Yield()

        Jump('lambda_628D')

    DispatchAsync2(0x0101, 0x0001, lambda_628D)

    @scena.Lambda('lambda_629E')
    def lambda_629E():
        ChrTurnDirection(0x00FE, 0x0107, 0)
        Yield()

        Jump('lambda_629E')

    DispatchAsync2(0x0102, 0x0001, lambda_629E)

    ChrWalkTo(0x0107, -5000, 0, 7600, 3000, 0x00)
    ChrSetDirection(0x0107, 0, 400)
    Sleep(500)

    OP_6F(0x0000, 0)
    OP_70(0x0000, 30)
    OP_73(0x0000)
    ChrWalkTo(0x0107, -4700, 0, 9200, 3000, 0x00)
    Sleep(500)

    OP_6F(0x0000, 30)
    OP_70(0x0000, 0)
    Sleep(1000)

    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)

    ChrTalk(
        0x0102,
        (
            '#0020070559V#019F哈哈，很可爱的孩子啊。\n',
            '给人一种努力向上的感觉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070560V#001F嗯嗯，同感！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010070561V#507F啊～啊，要是我也有一个\n',
            '那么活泼那么可爱的妹妹就好啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010070562V不像某个弟弟那样，\n',
            '一点也不可爱，老是麻烦人家～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020070563V#019F我可是有好几次想提醒你，\n',
            '一直在照顾你的其实是我吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020070564V想摆姐姐的架子，\n',
            '就要表现得更加可靠才行哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010070565V#509F哼，我才不用你瞎操心。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010070566V#000F闲话少说……\n',
            '还是快去城里看看吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070567V#010F是啊，\n',
            '首先要去协会打个招呼。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020070568V然后还要……\n',
            '和协会的人商量一下\n',
            '父亲和那个黑色导力器的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070569V#006F嗯……没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x0107, -4900, 0, 4400, 0)
    ChrSetFlags(0x0107, 0x0080)
    MapClearFlags(0x10000000)
    EventEnd(0x00)
    FormationDelMember(0x06, 0xFF)

    Return()

# id: 0x0017 offset: 0x65B0
@scena.Code('func_17_65B0')
def func_17_65B0():
    SetScenaFlags(ScenaFlag(0x00A8, 0, 0x540))
    ClearScenaFlags(ScenaFlag(0x00A8, 1, 0x541))
    ClearScenaFlags(ScenaFlag(0x00A8, 2, 0x542))
    ClearScenaFlags(ScenaFlag(0x00A8, 3, 0x543))
    ClearScenaFlags(ScenaFlag(0x00A8, 4, 0x544))
    ClearScenaFlags(ScenaFlag(0x00A8, 5, 0x545))
    ClearScenaFlags(ScenaFlag(0x00A8, 6, 0x546))

    Return()

# id: 0x0018 offset: 0x65C6
@scena.Code('func_18_65C6')
def func_18_65C6():
    ClearScenaFlags(ScenaFlag(0x00A8, 0, 0x540))
    SetScenaFlags(ScenaFlag(0x00A8, 1, 0x541))
    ClearScenaFlags(ScenaFlag(0x00A8, 2, 0x542))
    ClearScenaFlags(ScenaFlag(0x00A8, 3, 0x543))
    ClearScenaFlags(ScenaFlag(0x00A8, 4, 0x544))
    ClearScenaFlags(ScenaFlag(0x00A8, 5, 0x545))
    ClearScenaFlags(ScenaFlag(0x00A8, 6, 0x546))

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 4, 0x52C)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 6, 0x536)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_6764',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 2, 0x532)),
            Expr.Return,
        ),
        'loc_6764',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 5, 0x535)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6764',
    )

    EventBegin(0x00)
    Fade(1000)
    CameraMove(-5490, 0, 5460, 0)
    ChrSetPos(0x0101, -5140, 0, 5030, 0)
    ChrSetPos(0x0102, -5030, 0, 3560, 0)
    ChrSetPos(0x0107, -6390, 0, 5230, 0)
    ChrSetPos(0x0106, -6860, 0, 3810, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010080928V#004F看，导力梯里面……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070080929V#065F爷爷不在呢……\n',
            '他们果然是在一楼停下的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080930V#013F这么说来，\n',
            '犯人是从正门逃走的吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020080931V门外有那么多人看着，\n',
            '他们究竟打算怎么离开呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050080932V#054F别管那么多了，快！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x00A6, 5, 0x535))
    EventEnd(0x00)

    Jump('loc_6764')

    def _loc_6764(): pass

    label('loc_6764')

    Return()

# id: 0x0019 offset: 0x6765
@scena.Code('func_19_6765')
def func_19_6765():
    SetScenaFlags(ScenaFlag(0x00A3, 1, 0x519))
    OP_28(0x003F, 0x01, 0x1000)

    If(
        (
            (Expr.Eval, "OP_29(0x003F, 0x01, 0x0800)"),
            Expr.Return,
        ),
        'loc_677F',
    )

    OP_28(0x003F, 0x01, 0x2000)

    def _loc_677F(): pass

    label('loc_677F')

    OP_71(0x0008, 0x0004)
    OP_64(0x00, 0x0001)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '汽油罐',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    AddItem(0x0367, 1)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x001A offset: 0x67D5
@scena.Code('func_1A_67D5')
def func_1A_67D5():
    EventBegin(0x00)
    CameraMove(-140, 0, 7500, 0)
    ChrSetPos(0x0101, -80, 0, -7570, 0)
    ChrSetPos(0x0102, -990, 0, -8530, 0)
    ChrSetPos(0x0107, 370, 0, -8440, 0)
    FadeIn(1000, 0)
    CameraMove(100, 0, -6040, 4000)

    ChrTalk(
        0x0101,
        (
            '#0010080729V#002F#1P呜哇……\n',
            '里面还真是烟雾弥漫啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010080730V#505F咦……闻起来，\n',
            '这烟好像又不怎么呛人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080731V#013F#6P这种烟雾……\n',
            '应该是扰乱用的烟幕。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020080732V据我推测……\n',
            '这座建筑物的地上应该放有发烟筒。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010080733V#004F#1P咦……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0107, 0x0102, 400)

    ChrTalk(
        0x0107,
        (
            '#0070080734V#065F为、为什么会有那种东西……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0107, 400)

    ChrTalk(
        0x0102,
        (
            '#0020080735V#012F#6P这就不得而知了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020080736V只要把发烟筒破坏掉的话，\n',
            '我想烟雾很快就会消散的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080737V#002F#1P明白了。\n',
            '找到发烟筒就马上把它破坏掉……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010080738V拉赛尔博士\n',
            '应该还在三楼的工作室吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070080739V#063F嗯、嗯……\n',
            '我想应该还在那里……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070080740V爷爷在专注于研究的时候，\n',
            '是完全不会注意周围的情况的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020080741V#012F#6P总之去三楼看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Return()

# id: 0x001B offset: 0x6B14
@scena.Code('func_1B_6B14')
def func_1B_6B14():
    Return()

# id: 0x001C offset: 0x6B15
@scena.Code('func_1C_6B15')
def func_1C_6B15():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 6, 0x52E)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6DEF',
    )

    EventBegin(0x00)
    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    CameraMove(-4900, 0, 8380, 1000)
    SetScenaFlags(ScenaFlag(0x00A5, 6, 0x52E))
    OP_28(0x0041, 0x01, 0x0002)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6BB1',
    )

    ChrTalk(
        0x0101,
        (
            '#0010080742V#004F咦……？\n',
            '自动门打不开。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080743V#012F导力断了吗……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6CAD')

    def _loc_6BB1(): pass

    label('loc_6BB1')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6C19',
    )

    ChrTalk(
        0x0102,
        (
            '#0020080744V#013F奇怪……\n',
            '自动门没有反应。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080745V#004F咦，导力停掉了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6CAD')

    def _loc_6C19(): pass

    label('loc_6C19')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6CAD',
    )

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '提妲按下按钮。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0107,
        (
            '#0070080746V#065F咦、咦咦……\n',
            '自动门怎么打不开。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080747V#004F咦，导力停掉了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6CAD(): pass

    label('loc_6CAD')

    ChrTalk(
        0x0107,
        (
            '#0070080748V#063F唔唔……\n',
            '好像还在运作啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070080749V也许……\n',
            '是谁正在使用导力梯吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080750V#501F是谁正在……\n',
            '难道是拉赛尔博士？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080751V#012F不，这一点不能马上断定。\n',
            '为什么导力梯没有马上下来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020080752V既然这样的话，\n',
            '要想上去就必须走紧急通道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070080753V#063F嗯……是呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x01)

    Jump('loc_6E4E')

    def _loc_6DEF(): pass

    label('loc_6DEF')

    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '按了按钮，没有任何反应。\n',
            '导力梯好像不能用了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    TalkEnd(0x00FF)
    def _loc_6E4E(): pass

    label('loc_6E4E')

    Return()

# id: 0x001D offset: 0x6E4F
@scena.Code('func_1D_6E4F')
def func_1D_6E4F():
    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '按了按钮，没有任何反应。\n',
            '导力梯好像不能用了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x001E offset: 0x6EB8
@scena.Code('func_1E_6EB8')
def func_1E_6EB8():
    EventBegin(0x00)
    SetScenaFlags(ScenaFlag(0x00A8, 7, 0x547))
    OP_64(0x01, 0x0001)
    OP_2B(0x0041, 0x0001)
    CameraMove(-9770, 0, -3590, 1000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 7, 0x52F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_72FB',
    )

    SetScenaFlags(ScenaFlag(0x00A5, 7, 0x52F))

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6F55',
    )

    ChrTalk(
        0x0101,
        (
            '#0010080786V#004F啊……\n',
            '约修亚，这是！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080787V#012F是刚才所说的发烟筒。\n',
            '给我看看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_709B')

    def _loc_6F55(): pass

    label('loc_6F55')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6FC2',
    )

    ChrTalk(
        0x0101,
        (
            '#0010080788V#004F啊……\n',
            '约修亚，那是！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080789V#012F嗯。\n',
            '是刚才所说的发烟筒。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_709B')

    def _loc_6FC2(): pass

    label('loc_6FC2')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7033',
    )

    ChrTalk(
        0x0107,
        (
            '#0070080790V#065F啊……\n',
            '哥哥，这是！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080791V#012F是刚才所说的发烟筒。\n',
            '给我看看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_709B')

    def _loc_7033(): pass

    label('loc_7033')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_709B',
    )

    ChrTalk(
        0x0106,
        (
            '#0050080792V#057F这个……\n',
            '就是那发烟筒吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080793V#012F阿加特兄。\n',
            '给我看看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_709B(): pass

    label('loc_709B')

    FadeOut(1000, 0, -1)
    OP_0D()
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '约修亚很熟练地把发烟筒拆散了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    ChrSetPos(0x0102, -9340, 0, -4190, 315)
    ChrSetPos(0x0101, -10070, 0, -5250, 0)
    ChrSetPos(0x0107, -8820, 0, -5380, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 1, 0x531)),
            Expr.Return,
        ),
        'loc_7119',
    )

    ChrSetPos(0x0106, -9730, 0, -6460, 0)

    def _loc_7119(): pass

    label('loc_7119')

    FadeIn(600, 0)
    StopEffect(0x00, 0x02)
    StopEffect(0x01, 0x02)
    Sleep(1000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 1, 0x531)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_720D',
    )

    ChrTalk(
        0x0101,
        (
            '#0010080794V#501F哇……\n',
            '烟雾没有了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070080795V#560F约修亚哥哥，\n',
            '好厉害……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080796V#012F别的地方肯定还有\n',
            '和这个一样的发烟筒。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020080797V找到了就把它们拆散吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080798V#006FＯＫ！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_72F8')

    def _loc_720D(): pass

    label('loc_720D')

    SetScenaFlags(ScenaFlag(0x00A7, 6, 0x53E))

    ChrTalk(
        0x0101,
        (
            '#0010080799V#501F哇……\n',
            '烟雾没有了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070080800V#560F约修亚哥哥，\n',
            '好厉害……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050080801V#052F哦……\n',
            '还挺有两下子的嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080802V#012F别的地方肯定还有\n',
            '和这个一样的发烟筒。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020080803V找到了就把它们拆散吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_72F8(): pass

    label('loc_72F8')

    Jump('loc_742B')

    def _loc_72FB(): pass

    label('loc_72FB')

    FadeOut(600, 0, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '约修亚很熟练地把发烟筒拆散了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    ChrSetPos(0x0102, -9340, 0, -4190, 315)
    ChrSetPos(0x0101, -10070, 0, -5250, 0)
    ChrSetPos(0x0107, -8820, 0, -5380, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 1, 0x531)),
            Expr.Return,
        ),
        'loc_7381',
    )

    ChrSetPos(0x0106, -9730, 0, -6460, 0)

    def _loc_7381(): pass

    label('loc_7381')

    StopEffect(0x00, 0x02)
    StopEffect(0x01, 0x02)
    Sleep(1000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 1, 0x531)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A7, 6, 0x53E)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_742B',
    )

    SetScenaFlags(ScenaFlag(0x00A7, 6, 0x53E))

    ChrTalk(
        0x0106,
        (
            '#0050080804V#052F哦……\n',
            '还挺有两下子的嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080805V#012F别的地方肯定还有\n',
            '和这个一样的发烟筒。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020080806V找到了就把它们拆散吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_742B(): pass

    label('loc_742B')

    EventEnd(0x00)

    Return()

# id: 0x001F offset: 0x742E
@scena.Code('func_1F_742E')
def func_1F_742E():
    EventBegin(0x00)
    SetScenaFlags(ScenaFlag(0x00A9, 0, 0x548))
    OP_64(0x02, 0x0001)
    OP_2B(0x0041, 0x0001)
    CameraMove(-98280, -4000, -103420, 1000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 7, 0x52F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7871',
    )

    SetScenaFlags(ScenaFlag(0x00A5, 7, 0x52F))

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_74CB',
    )

    ChrTalk(
        0x0101,
        (
            '#0010080807V#004F啊……\n',
            '约修亚，这是！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080808V#012F是刚才所说的发烟筒。\n',
            '给我看看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7611')

    def _loc_74CB(): pass

    label('loc_74CB')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7538',
    )

    ChrTalk(
        0x0101,
        (
            '#0010080809V#004F啊……\n',
            '约修亚，那是！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080810V#012F嗯。\n',
            '是刚才所说的发烟筒。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7611')

    def _loc_7538(): pass

    label('loc_7538')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_75A9',
    )

    ChrTalk(
        0x0107,
        (
            '#0070080811V#065F啊……\n',
            '哥哥，这是！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080812V#012F是刚才所说的发烟筒。\n',
            '给我看看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7611')

    def _loc_75A9(): pass

    label('loc_75A9')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7611',
    )

    ChrTalk(
        0x0106,
        (
            '#0050080813V#057F这个……\n',
            '就是那发烟筒吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080814V#012F阿加特兄。\n',
            '给我看看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7611(): pass

    label('loc_7611')

    FadeOut(1000, 0, -1)
    OP_0D()
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '约修亚很熟练地把发烟筒拆散了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    ChrSetPos(0x0102, -98680, -4000, -105420, 315)
    ChrSetPos(0x0101, -99580, -4000, -106640, 45)
    ChrSetPos(0x0107, -98140, -4000, -106180, 315)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 1, 0x531)),
            Expr.Return,
        ),
        'loc_768F',
    )

    ChrSetPos(0x0106, -98640, -4000, -107110, 45)

    def _loc_768F(): pass

    label('loc_768F')

    FadeIn(600, 0)
    StopEffect(0x01, 0x02)
    StopEffect(0x02, 0x02)
    Sleep(1000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 1, 0x531)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7783',
    )

    ChrTalk(
        0x0101,
        (
            '#0010080815V#501F哇……\n',
            '烟雾没有了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070080816V#560F约修亚哥哥，\n',
            '好厉害……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080817V#012F别的地方肯定还有\n',
            '和这个一样的发烟筒。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020080818V找到了就把它们拆散吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080819V#006FＯＫ！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_786E')

    def _loc_7783(): pass

    label('loc_7783')

    SetScenaFlags(ScenaFlag(0x00A7, 6, 0x53E))

    ChrTalk(
        0x0101,
        (
            '#0010080820V#501F哇……\n',
            '烟雾没有了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070080821V#560F约修亚哥哥，\n',
            '好厉害……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050080822V#052F哦……\n',
            '还挺有两下子的嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080823V#012F别的地方肯定还有\n',
            '和这个一样的发烟筒。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020080824V找到了就把它们拆散吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_786E(): pass

    label('loc_786E')

    Jump('loc_79A1')

    def _loc_7871(): pass

    label('loc_7871')

    FadeOut(600, 0, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '约修亚很熟练地把发烟筒拆散了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    ChrSetPos(0x0102, -98680, -4000, -105420, 315)
    ChrSetPos(0x0101, -99580, -4000, -106640, 45)
    ChrSetPos(0x0107, -98140, -4000, -106180, 315)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 1, 0x531)),
            Expr.Return,
        ),
        'loc_78F7',
    )

    ChrSetPos(0x0106, -98640, -4000, -107110, 45)

    def _loc_78F7(): pass

    label('loc_78F7')

    StopEffect(0x01, 0x02)
    StopEffect(0x02, 0x02)
    Sleep(1000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 1, 0x531)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A7, 6, 0x53E)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_79A1',
    )

    SetScenaFlags(ScenaFlag(0x00A7, 6, 0x53E))

    ChrTalk(
        0x0106,
        (
            '#0050080825V#052F哦……\n',
            '还挺有两下子的嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080826V#012F别的地方肯定还有\n',
            '和这个一样的发烟筒。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020080827V找到了就把它们拆散吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_79A1(): pass

    label('loc_79A1')

    EventEnd(0x00)

    Return()

# id: 0x0020 offset: 0x79A4
@scena.Code('func_20_79A4')
def func_20_79A4():
    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_79F9',
    )

    ChrTalk(
        0x0101,
        (
            '#0010080933V#002F（啊，这边是出口啊。\n',
            '　现在不是出去的时候。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7AD2')

    def _loc_79F9(): pass

    label('loc_79F9')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7A54',
    )

    ChrTalk(
        0x0102,
        (
            '#0020080934V#012F（不能随便出去啊。\n',
            '　现在要赶快在工房内部进行调查。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7AD2')

    def _loc_7A54(): pass

    label('loc_7A54')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7AA1',
    )

    ChrTalk(
        0x0107,
        (
            '#0070080935V#062F（啊，这边是出口。\n',
            '　要赶快找到爷爷。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7AD2')

    def _loc_7AA1(): pass

    label('loc_7AA1')

    ChrTalk(
        0x0106,
        (
            '#0050080936V#050F（……没有时间再出去了。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7AD2(): pass

    label('loc_7AD2')

    ChrMoveToRelative(0x0000, 1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x0021 offset: 0x7AEE
@scena.Code('func_21_7AEE')
def func_21_7AEE():
    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7B45',
    )

    ChrTalk(
        0x0101,
        (
            '#0010080924V#002F（犯人好像逃到一楼去了。\n',
            '　要赶快追上他们……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7C02')

    def _loc_7B45(): pass

    label('loc_7B45')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7B7F',
    )

    ChrTalk(
        0x0102,
        (
            '#0020080925V#012F（要赶快去一楼……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7C02')

    def _loc_7B7F(): pass

    label('loc_7B7F')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7BCA',
    )

    ChrTalk(
        0x0107,
        (
            '#0070080926V#062F（爷爷好像被他们带到一楼去了……）\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7C02')

    def _loc_7BCA(): pass

    label('loc_7BCA')

    ChrTalk(
        0x0106,
        (
            '#0050080927V#050F（不是这边。\n',
            '　他们去了一层……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7C02(): pass

    label('loc_7C02')

    ChrMoveToRelative(0x0000, 1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x0022 offset: 0x7C1E
@scena.Code('func_22_7C1E')
def func_22_7C1E():
    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7C73',
    )

    ChrTalk(
        0x0101,
        (
            '#0010080937V#002F（啊，这边是出口啊。\n',
            '　现在不是出去的时候。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7D4C')

    def _loc_7C73(): pass

    label('loc_7C73')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7CCE',
    )

    ChrTalk(
        0x0102,
        (
            '#0020080938V#012F（现在还不是回去的时候。\n',
            '　总之先在内部调查一下吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7D4C')

    def _loc_7CCE(): pass

    label('loc_7CCE')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7D1B',
    )

    ChrTalk(
        0x0107,
        (
            '#0070080939V#062F（啊，这边是出口。\n',
            '　要赶快找到爷爷。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7D4C')

    def _loc_7D1B(): pass

    label('loc_7D1B')

    ChrTalk(
        0x0106,
        (
            '#0050080940V#050F（……没有时间再出去了。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7D4C(): pass

    label('loc_7D4C')

    ChrMoveToRelative(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x0023 offset: 0x7D68
@scena.Code('func_23_7D68')
def func_23_7D68():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '左·中央工房导力梯\n',
            '右·地下导力器工场',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0024 offset: 0x7DC0
@scena.Code('func_24_7DC0')
def func_24_7DC0():
    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门上着锁，无法打开。',
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
