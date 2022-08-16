import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T3120_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3120   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'T3120.x'
    header.mapIndex       = 1
    header.bgm            = 13
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
        ('ED6_DT07/CH02610._CH', 'ED6_DT07/CH02610P._CP'),
        ('ED6_DT07/CH02050._CH', 'ED6_DT07/CH02050P._CP'),
        ('ED6_DT07/CH02070._CH', 'ED6_DT07/CH02070P._CP'),
        ('ED6_DT07/CH02620._CH', 'ED6_DT07/CH02620P._CP'),
        ('ED6_DT07/CH01200._CH', 'ED6_DT07/CH01200P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01030._CH', 'ED6_DT07/CH01030P._CP'),
        ('ED6_DT07/CH01060._CH', 'ED6_DT07/CH01060P._CP'),
        ('ED6_DT07/CH01160._CH', 'ED6_DT07/CH01160P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT07/CH01750._CH', 'ED6_DT07/CH01750P._CP'),
        ('ED6_DT07/CH01760._CH', 'ED6_DT07/CH01760P._CP'),
        ('ED6_DT07/CH01530._CH', 'ED6_DT07/CH01530P._CP'),
        ('ED6_DT07/CH02490._CH', 'ED6_DT07/CH02490P._CP'),
        ('ED6_DT07/CH01190._CH', 'ED6_DT07/CH01190P._CP'),
    ]

# id: 0x10001 offset: 0x122
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '雾香',
            x                   = 3500,
            z                   = 0,
            y                   = 1200,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '亚鲁瓦教授',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
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
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '玛多克工房长',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '斯坦因',
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
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '埃尔文',
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
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '艾妲',
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
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            name                = '库诺',
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
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            name                = '呆呆',
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
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            name                = '耶鲁克',
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
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            name                = '冈多夫',
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
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '王',
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
            talkScenaIndex      = 0x0011,
        ),
        ScenaNpcData(
            name                = '布鲁诺',
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
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '莫妮卡',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '加鲁诺',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
    )

# id: 0x10002 offset: 0x302
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x302
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x302
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 3480,
            triggerZ            = 0,
            triggerY            = -710,
            triggerRange        = 400,
            actorX              = 3500,
            actorZ              = 1500,
            actorY              = 1200,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0009,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 1830,
            triggerZ            = 1000,
            triggerY            = 51000,
            triggerRange        = 400,
            actorX              = 1780,
            actorZ              = 2500,
            actorY              = 53000,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0012,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 53210,
            triggerZ            = 0,
            triggerY            = 520,
            triggerRange        = 400,
            actorX              = 52970,
            actorZ              = 1500,
            actorY              = 2400,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0013,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -1320,
            triggerZ            = 0,
            triggerY            = -4700,
            triggerRange        = 1400,
            actorX              = -1320,
            actorZ              = 2000,
            actorY              = -4700,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x001A,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x392
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_3A0',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, func_17_86AD)

    def _loc_3A0(): pass

    label('loc_3A0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 3, 0x3FB)),
            Expr.Return,
        ),
        'loc_3B1',
    )

    OP_26(131)
    ClearScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    Event(0, func_19_BF67)

    def _loc_3B1(): pass

    label('loc_3B1')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_3BD'),
        (-1, 'loc_412'),
    )

    def _loc_3BD(): pass

    label('loc_3BD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 4, 0x50C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3CC',
    )

    SetScenaFlags(ScenaFlag(0x00A1, 4, 0x50C))
    Event(0, func_14_54B0)

    def _loc_3CC(): pass

    label('loc_3CC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A7, 0, 0x538)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3DF',
    )

    SetScenaFlags(ScenaFlag(0x00A7, 0, 0x538))
    Event(0, func_15_5FEE)

    def _loc_3DF(): pass

    label('loc_3DF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 2, 0x55A)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3F7',
    )

    MapSetFlags(0x10000000)
    SetScenaFlags(ScenaFlag(0x00AB, 2, 0x55A))
    Event(0, func_16_70FB)

    def _loc_3F7(): pass

    label('loc_3F7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AC, 0, 0x560)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 7, 0x55F)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_40F',
    )

    MapSetFlags(0x10000000)
    SetScenaFlags(ScenaFlag(0x00AC, 0, 0x560))
    Event(0, func_18_A73A)

    def _loc_40F(): pass

    label('loc_40F')

    Jump('loc_412')

    def _loc_412(): pass

    label('loc_412')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_4A7',
    )

    ChrClearFlags(0x000D, 0x0080)
    ChrSetPos(0x000D, 1780, 1000, 53000, 183)
    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x000E, 52200, 0, 53610, 270)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0010, 55570, 0, 51740, 63)
    CreateThread(0x0010, 0x00, 0x00, func_03_98A)
    ChrClearFlags(0x0011, 0x0080)
    ChrSetPos(0x0011, 52970, 0, 2400, 172)
    ChrClearFlags(0x0012, 0x0080)
    ChrSetPos(0x0012, 25360, 0, -2660, 102)
    ChrClearFlags(0x0013, 0x0080)
    ChrSetPos(0x0013, 54960, 4000, 2770, 11)

    Jump('loc_951')

    def _loc_4A7(): pass

    label('loc_4A7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_51F',
    )

    ChrClearFlags(0x000D, 0x0080)
    ChrSetPos(0x000D, 1780, 1000, 53000, 183)
    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x000E, -1150, 1000, 50950, 91)
    ChrClearFlags(0x0011, 0x0080)
    ChrSetPos(0x0011, 52970, 0, 2400, 172)
    ChrClearFlags(0x0014, 0x0080)
    ChrSetPos(0x0014, 22260, 0, 2140, 270)
    ChrClearFlags(0x0015, 0x0080)
    ChrSetPos(0x0015, 51500, 4000, 3030, 274)

    Jump('loc_951')

    def _loc_51F(): pass

    label('loc_51F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_5A5',
    )

    ChrClearFlags(0x000D, 0x0080)
    ChrSetPos(0x000D, 1780, 1000, 53000, 183)
    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x000E, 52200, 0, 53610, 270)
    ChrClearFlags(0x0011, 0x0080)
    ChrSetPos(0x0011, 52970, 0, 2400, 172)
    ChrClearFlags(0x0012, 0x0080)
    ChrSetPos(0x0012, 25360, 0, -2660, 102)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 2, 0x55A)),
            Expr.Return,
        ),
        'loc_5A2',
    )

    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, 3790, 0, -2310, 278)
    CreateThread(0x000A, 0x00, 0x00, func_02_974)

    def _loc_5A2(): pass

    label('loc_5A2')

    Jump('loc_951')

    def _loc_5A5(): pass

    label('loc_5A5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_61D',
    )

    ChrClearFlags(0x000D, 0x0080)
    ChrSetPos(0x000D, 1780, 1000, 53000, 183)
    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x000E, 52200, 0, 53610, 270)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x000F, 52110, 0, 50520, 255)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0010, 59030, 0, 54500, 355)
    ChrClearFlags(0x0011, 0x0080)
    ChrSetPos(0x0011, 52970, 0, 2400, 172)

    Jump('loc_951')

    def _loc_61D(): pass

    label('loc_61D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_69A',
    )

    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x000E, 1780, 1000, 53000, 183)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x000F, -710, 1000, 50990, 0)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0010, 2940, 1000, 53000, 269)
    ChrSetFlags(0x0010, 0x0010)
    ChrClearFlags(0x0011, 0x0080)
    ChrSetPos(0x0011, 52970, 0, 2400, 172)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0009, 4070, 0, -700, 0)

    Jump('loc_951')

    def _loc_69A(): pass

    label('loc_69A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_6E6',
    )

    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x000E, 1780, 1000, 53000, 183)
    ChrClearFlags(0x0011, 0x0080)
    ChrSetPos(0x0011, 52970, 0, 2400, 172)
    ChrClearFlags(0x0016, 0x0080)
    ChrSetPos(0x0016, 54570, 0, 540, 351)

    Jump('loc_951')

    def _loc_6E6(): pass

    label('loc_6E6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_732',
    )

    ChrClearFlags(0x000D, 0x0080)
    ChrSetPos(0x000D, 1780, 1000, 53000, 183)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x000F, -970, 1000, 51000, 352)
    ChrClearFlags(0x0011, 0x0080)
    ChrSetPos(0x0011, 52970, 0, 2400, 172)

    Jump('loc_951')

    def _loc_732(): pass

    label('loc_732')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_799',
    )

    ChrClearFlags(0x000C, 0x0080)
    ChrSetPos(0x000C, 61100, 2000, 2280, 11)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x000F, 3500, 0, 47710, 270)
    ChrClearFlags(0x000D, 0x0080)
    ChrSetPos(0x000D, 1780, 1000, 53000, 183)
    ChrSetFlags(0x000D, 0x0010)
    ChrClearFlags(0x0011, 0x0080)
    ChrSetPos(0x0011, 52970, 0, 2400, 172)

    Jump('loc_951')

    def _loc_799(): pass

    label('loc_799')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_856',
    )

    ChrClearFlags(0x000C, 0x0080)
    ChrSetPos(0x000C, 61100, 2000, 2280, 11)
    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x000E, 52200, 0, 53610, 270)
    ChrClearFlags(0x000D, 0x0080)
    ChrSetPos(0x000D, 1780, 1000, 53000, 183)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0010, 55570, 0, 51740, 63)
    CreateThread(0x0010, 0x00, 0x00, func_03_98A)
    ChrClearFlags(0x0011, 0x0080)
    ChrSetPos(0x0011, 52970, 0, 2400, 172)
    ChrClearFlags(0x0012, 0x0080)
    ChrSetPos(0x0012, 25360, 0, -2660, 102)
    ChrClearFlags(0x0013, 0x0080)
    ChrSetPos(0x0013, 27160, 0, -2710, 284)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AF, 5, 0x57D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_853',
    )

    ChrSetFlags(0x0012, 0x0010)
    ChrSetFlags(0x0013, 0x0010)

    def _loc_853(): pass

    label('loc_853')

    Jump('loc_951')

    def _loc_856(): pass

    label('loc_856')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Return,
        ),
        'loc_8D5',
    )

    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x000E, 52200, 0, 53610, 270)
    ChrClearFlags(0x000D, 0x0080)
    ChrSetPos(0x000D, 1780, 1000, 53000, 183)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0010, 55570, 0, 51740, 63)
    CreateThread(0x0010, 0x00, 0x00, func_03_98A)
    ChrClearFlags(0x0011, 0x0080)
    ChrSetPos(0x0011, 52970, 0, 2400, 172)
    ChrClearFlags(0x0013, 0x0080)
    ChrSetPos(0x0013, 54960, 4000, 2770, 11)

    Jump('loc_951')

    def _loc_8D5(): pass

    label('loc_8D5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_951',
    )

    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x000E, 52200, 0, 53610, 270)
    ChrClearFlags(0x000D, 0x0080)
    ChrSetPos(0x000D, 1780, 1000, 53000, 183)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0010, 55570, 0, 51740, 63)
    CreateThread(0x0010, 0x00, 0x00, func_03_98A)
    ChrClearFlags(0x0011, 0x0080)
    ChrSetPos(0x0011, 52970, 0, 2400, 172)
    ChrClearFlags(0x0013, 0x0080)
    ChrSetPos(0x0013, 54960, 4000, 2770, 11)

    def _loc_951(): pass

    label('loc_951')

    Return()

# id: 0x0001 offset: 0x952
@scena.Code('func_01_952')
def func_01_952():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A7, 2, 0x53A)),
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 0, 0x558)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_96A',
    )

    OP_B1('t3120_y')

    Jump('loc_973')

    def _loc_96A(): pass

    label('loc_96A')

    OP_B1('t3120_n')

    def _loc_973(): pass

    label('loc_973')

    Return()

# id: 0x0002 offset: 0x974
@scena.Code('func_02_974')
def func_02_974():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_989',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_974')

    def _loc_989(): pass

    label('loc_989')

    Return()

# id: 0x0003 offset: 0x98A
@scena.Code('func_03_98A')
def func_03_98A():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_9AD',
    )

    OP_8D(0x00FE, 52620, 51160, 59990, 53120, 3000)

    Jump('func_03_98A')

    def _loc_9AD(): pass

    label('loc_9AD')

    Return()

# id: 0x0004 offset: 0x9AE
@scena.Code('func_04_9AE')
def func_04_9AE():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_AE3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_A0C',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，说起来\n',
            '外面还真是吵啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '又是主日学校的孩子们\n',
            '在翘课打闹吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_AE3')

    def _loc_A0C(): pass

    label('loc_A0C')

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    ChrTalk(
        0x00FE,
        (
            '这把导力枪\n',
            '可以将内部驱动导力器的性能\n',
            '发挥至极限呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽说平衡性确实差了点，\n',
            '很有必要加以改进，\n',
            '不过也算是在可以忍受的范围内吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总而言之一切还算顺利。\n',
            '这样的话，\n',
            '应该可以比预定时间更早做出成品来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_AE3(): pass

    label('loc_AE3')

    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0xAE7
@scena.Code('func_05_AE7')
def func_05_AE7():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 2, 0x55A)),
            Expr.Return,
        ),
        'loc_B58',
    )

    ChrTalk(
        0x000A,
        (
            '#0280090134V#150F小艾，\n',
            '了解到什么的话要告诉我哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280090135V我想让这次的特辑\n',
            '有更多独家新闻。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B58(): pass

    label('loc_B58')

    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0xB5C
@scena.Code('func_06_B5C')
def func_06_B5C():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_BCB',
    )

    ChrTalk(
        0x00FE,
        (
            '唉，商品的说明果然\n',
            '必须像这样写才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '射程……精度……驱动时间……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊，多么具体啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BCB(): pass

    label('loc_BCB')

    TalkEnd(0x00FE)

    Return()

# id: 0x0007 offset: 0xBCF
@scena.Code('func_07_BCF')
def func_07_BCF():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_C74',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_C29',
    )

    ChrTalk(
        0x00FE,
        (
            '……杨？好像不是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那就是……汪？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不，好像两个都不对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C74')

    def _loc_C29(): pass

    label('loc_C29')

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    ChrTalk(
        0x00FE,
        (
            '唔～\n',
            '之前给我担任护卫的那个兄弟……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎呀，\n',
            '他到底叫什么来着？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C74(): pass

    label('loc_C74')

    TalkEnd(0x00FE)

    Return()

# id: 0x0008 offset: 0xC78
@scena.Code('func_08_C78')
def func_08_C78():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_CD4',
    )

    ChrTalk(
        0x0009,
        (
            '#0150081112V#130F看来发生了不得了的事情啊……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150081113V请务必要小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_CD4(): pass

    label('loc_CD4')

    TalkEnd(0x00FE)

    Return()

# id: 0x0009 offset: 0xCD8
@scena.Code('func_09_CD8')
def func_09_CD8():
    TalkBegin(0x0008)
    FadeOut(300, 0, 70)

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
            TXT(0x01, '报告\n'),
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
        'loc_E34',
    )

    OP_0D()

    If(
        (
            (Expr.Eval, "OP_A9(0x40)"),
            Expr.Return,
        ),
        'loc_DB6',
    )

    Sleep(200)

    ChrTalk(
        0x0008,
        (
            '#0580071148V#790F辛苦了。\n',
            '看来你们很顺利地完成了任务呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580071149V如果完成其他任务的话，\n',
            '别忘记回协会报告一下哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E2E')

    def _loc_DB6(): pass

    label('loc_DB6')

    Sleep(200)

    ChrTalk(
        0x0008,
        (
            '#0580071150V#790F啊，\n',
            '现在没有需要报告的工作呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580071151V如果完成其他任务的话，\n',
            '别忘记回协会报告一下哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E2E(): pass

    label('loc_E2E')

    OP_56(0x00)
    TalkEnd(0x0008)

    Return()

    def _loc_E34(): pass

    label('loc_E34')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E45',
    )

    TalkEnd(0x0008)

    Return()

    def _loc_E45(): pass

    label('loc_E45')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 3, 0x603)),
            Expr.Return,
        ),
        'loc_1075',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AF, 3, 0x57B)),
            Expr.Return,
        ),
        'loc_EBD',
    )

    ChrTalk(
        0x0008,
        (
            '#0580100316V#790F你们还是尽快动身离开这个地方吧。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580100317V愿女神保佑。\n',
            '你们俩都要小心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1072')

    def _loc_EBD(): pass

    label('loc_EBD')

    SetScenaFlags(ScenaFlag(0x00AF, 3, 0x57B))

    ChrTalk(
        0x0008,
        (
            '#0580100308V#790F哎呀，搭乘手续办好了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100309V#505F嗯，那个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔说明了有关王国军盘查的消息\n',
            '和退掉船票准备步行去王都的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    ChrTalk(
        0x0008,
        (
            '#0580100310V#792F是这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580100311V#790F对方的行动比想象的还要快啊。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580100312V你们最好也尽快动身离开这个地方吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100313V#010F嗯，这就出发。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100314V#000F再见了，雾香姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0580100315V#790F愿女神保佑。\n',
            '你们俩都要小心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1072(): pass

    label('loc_1072')

    Jump('loc_216B')

    def _loc_1075(): pass

    label('loc_1075')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_10EC',
    )

    ChrTalk(
        0x0008,
        (
            '#0580101071V#790F去往王都的船是１１点出发的……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580101072V你们最好赶快去飞艇坪办理搭乘手续吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_216B')

    def _loc_10EC(): pass

    label('loc_10EC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_1201',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 7, 0x55F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_116E',
    )

    ChrTalk(
        0x0008,
        (
            '#0580090424V#790F你们去把提妲所说的那个装置拿来。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580090425V在这段时间里， \n',
            '我会将要塞的资料准备好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11FE')

    def _loc_116E(): pass

    label('loc_116E')

    ChrTalk(
        0x0008,
        (
            '#0580071209V#790F工房船也差不多应该准备好了。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580071210V你们准备好的话\n',
            '就马上去飞艇坪吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580071211V愿女神保佑。\n',
            '你们要小心行事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_11FE(): pass

    label('loc_11FE')

    Jump('loc_216B')

    def _loc_1201(): pass

    label('loc_1201')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_12A4',
    )

    ChrTalk(
        0x0008,
        (
            '#0580071206V#790F去雷斯顿要塞的话，\n',
            '要从城里的东门出去。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580071207V街道的途中会有一个三岔路，\n',
            '从那里往北走就行了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580071208V……千万要小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_216B')

    def _loc_12A4(): pass

    label('loc_12A4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_137E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_130B',
    )

    ChrTalk(
        0x0008,
        (
            '#0580071204V#790F我这里会跟王国军事先联络好。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580071205V好了，快点动身吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_137B')

    def _loc_130B(): pass

    label('loc_130B')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '#0580071202V#790F这边如果有什么事情，\n',
            '我会交给王去处理。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580071203V你们快点到『红莲之塔』那里吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_137B(): pass

    label('loc_137B')

    Jump('loc_216B')

    def _loc_137E(): pass

    label('loc_137E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_15CA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_1406',
    )

    ChrTalk(
        0x0008,
        (
            '#0580071200V#790F你们俩赶快去中央工房那边看看吧。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580071201V如果发生什么紧急情况，\n',
            '就在现场果断处理就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15C7')

    def _loc_1406(): pass

    label('loc_1406')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '#0580071191V#790F太好了。\n',
            '你们俩来得正好呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010071192V#004F雾香姐，发生什么事了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020071193V#014F中央工房那边似乎发生了什么骚乱。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0580071194V#792F不巧，\n',
            '我在这里无法了解到现场的事态。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580071195V因为游击士都在外面执行任务，\n',
            '我自己没法行动。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580071196V你们俩可以马上赶去中央工房吗？\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580071197V如果发生什么紧急情况，\n',
            '就在现场果断处理就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010071198V#006F嗯，明白！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020071199V#012F明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_15C7(): pass

    label('loc_15C7')

    Jump('loc_216B')

    def _loc_15CA(): pass

    label('loc_15CA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_196B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AF, 2, 0x57A)),
            Expr.Return,
        ),
        'loc_1659',
    )

    ChrTalk(
        0x0008,
        (
            '#0580071189V#790F代替博士去办事\n',
            '也是在替他分担工作量啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580071190V虽说到亚尔摩并不算太远，\n',
            '你们路上也不要大意哦。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1968')

    def _loc_1659(): pass

    label('loc_1659')

    SetScenaFlags(ScenaFlag(0x00AF, 2, 0x57A))

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1715',
    )

    ChrTalk(
        0x0008,
        (
            '#0580071185V#790F啊，提妲。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580071186V我已经听说了。\n',
            '你们要去亚尔摩那里吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070071187V#060F啊……对，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070071188V这次是代替爷爷\n',
            '去修理村里的水泵。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_176F')

    def _loc_1715(): pass

    label('loc_1715')

    ChrTalk(
        0x0008,
        (
            '#0580071167V#790F啊，是你们两个人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580071168V我听说了哦。\n',
            '你们要去亚尔摩那里吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_176F(): pass

    label('loc_176F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B0, 1, 0x581)),
            Expr.Return,
        ),
        'loc_17EA',
    )

    ChrTalk(
        0x0101,
        (
            '#0010071169V#000F啊，对了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010071170V海泽尔小姐说\n',
            '已经跟这里联系过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0580071171V#790F嗯，是的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1866')

    def _loc_17EA(): pass

    label('loc_17EA')

    ChrTalk(
        0x0101,
        (
            '#0010071172V#004F哇～不愧是雾香姐姐。\n',
            '这么快就知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0580071173V#790F工房接待处的海泽尔\n',
            '已经跟我这里联系过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1866(): pass

    label('loc_1866')

    ChrTalk(
        0x0008,
        (
            '#0580071174V#790F我已经了解情况了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580071175V你们这次的工作内容\n',
            '就是代替博士去办事吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580071176V虽说到亚尔摩并不算太远，\n',
            '你们路上也不要大意哦。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010071177V#006F嗯，交给我们吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010071178V那我们出发了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020071179V#010F告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1968(): pass

    label('loc_1968')

    Jump('loc_216B')

    def _loc_196B(): pass

    label('loc_196B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_1AA6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_19FA',
    )

    ChrTalk(
        0x0008,
        (
            '#0580071180V#790F艾丝蒂尔、约修亚。\n',
            '就拜托你们给博士帮忙了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580071181V#791F协会这边也会密切关注\n',
            '那个导力器的真面目。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AA3')

    def _loc_19FA(): pass

    label('loc_19FA')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '#0580071182V#790F啊，艾丝蒂尔、约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580071183V#791F呵呵，你们真是辛苦了。\n',
            '就拜托你们给博士帮忙了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580071184V协会这边也会密切关注\n',
            '那个导力器的真面目。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1AA3(): pass

    label('loc_1AA3')

    Jump('loc_216B')

    def _loc_1AA6(): pass

    label('loc_1AA6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_1E47',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 2, 0x512)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1DC3',
    )

    SetScenaFlags(ScenaFlag(0x00A2, 2, 0x512))
    EventBegin(0x00)
    Fade(1000)
    CameraMove(3730, 0, 600, 0)
    ChrSetPos(0x0102, 4430, 0, -700, 0)
    ChrSetPos(0x0101, 3170, 0, -710, 0)
    ChrSetPos(0x0107, 4059, 0, -1760, 0)
    ChrSetDirection(0x0008, 180, 0)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0580071135V#791F#2P早上好。\n',
            '昨晚真是虚惊一场啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580071136V你们俩还是赶快\n',
            '把详细情况报告给我听吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010071137V#506F啊，雾香姐还真是开门见山。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0580071138V#792F#2P虽然大致情况\n',
            '已经从工房长那里听说了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580071139V不过还是想听\n',
            '实际在场的目击者说明一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020071140V#012F好吧，那就……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔他们向雾香报告了\n',
            '昨晚发生的『导力停止现象』的详细情况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0008,
        (
            '#0580071141V#790F#2P原来如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580071142V真不愧是匿名寄给\n',
            '卡西乌斯先生的东西，\n',
            '看来那个导力器不是简单的物品。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580071143V协会方面对此事也很在意，\n',
            '就请你们继续协助博士的研究吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010071144V#006F嗯，正打算这么做呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020071145V#010F如果发现什么的话，我们再回来报告。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Jump('loc_1E44')

    def _loc_1DC3(): pass

    label('loc_1DC3')

    ChrTalk(
        0x0008,
        (
            '#0580071146V#790F那个黑色导力器\n',
            '果然不是什么简单的东西啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580071147V协会这边也对它很感兴趣，\n',
            '你们就继续协助博士调查吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1E44(): pass

    label('loc_1E44')

    Jump('loc_216B')

    def _loc_1E47(): pass

    label('loc_1E47')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Return,
        ),
        'loc_20EF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_1EDE',
    )

    ChrTurnDirection(0x0008, 0x0101, 0)

    ChrTalk(
        0x0008,
        (
            '#0580071154V#790F拉赛尔博士的研究所\n',
            '在蔡斯城的西南边。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580071155V出了协会门口之后往左前方走，\n',
            '到了城门再向右拐就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_20EC')

    def _loc_1EDE(): pass

    label('loc_1EDE')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    ChrTurnDirection(0x0008, 0x0101, 0)

    ChrTalk(
        0x0008,
        (
            '#0580071156V#790F啊，艾丝蒂尔、约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580071157V……拉赛尔博士的研究所\n',
            '在蔡斯城的西南边。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010071158V#004F雾香姐姐， \n',
            '你、你好厉害哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010071159V你怎么知道\n',
            '我们要去博士家啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0580071160V#792F……怎么会不知道呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580071161V你们不是和博士的孙女儿在一起吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010071162V#008F哦，对啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010071163V呵呵，\n',
            '这回可省下报告的功夫了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0580071164V#790F博士是个很忙的人，\n',
            '你们俩可不要失礼哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580071165V那再见了，提妲。\n',
            '他们俩就拜托你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070071166V#060F啊，好的。\n',
            '我知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_20EC(): pass

    label('loc_20EC')

    Jump('loc_216B')

    def _loc_20EF(): pass

    label('loc_20EF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 4, 0x50C)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_216B',
    )

    ChrTalk(
        0x0008,
        (
            '#0580071152V#790F你们先去拜会一下\n',
            '玛多克工房长吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580071153V说不定能够了解到一些\n',
            '有关那个导力器的线索。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_216B(): pass

    label('loc_216B')

    TalkEnd(0x0008)

    Return()

# id: 0x000A offset: 0x216F
@scena.Code('func_0A_216F')
def func_0A_216F():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_2292',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_21B4',
    )

    ChrTalk(
        0x00FE,
        (
            '店里面也没有受到损失，\n',
            '暂且可以安心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2292')

    def _loc_21B4(): pass

    label('loc_21B4')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '昨天晚上导力停止了，\n',
            '真是把我吓坏了呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽说以前也听说过\n',
            '只有在特殊的结晶回路中\n',
            '才会有那种力量……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '想不到会产生\n',
            '影响到那么大范围的现象呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果这力量用于武器研制的话，\n',
            '恐怕会导致各国的军力失去平衡。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2292(): pass

    label('loc_2292')

    TalkEnd(0x00FE)

    Return()

# id: 0x000B offset: 0x2296
@scena.Code('func_0B_2296')
def func_0B_2296():
    TalkBegin(0x000D)
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
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_230C',
    )

    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AE, 1, 0x571)),
            Expr.Return,
        ),
        'loc_22F8',
    )

    OP_A9(0x4C)

    Jump('loc_2306')

    def _loc_22F8(): pass

    label('loc_22F8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_2304',
    )

    OP_A9(0x4B)

    Jump('loc_2306')

    def _loc_2304(): pass

    label('loc_2304')

    OP_A9(0x3E)

    def _loc_2306(): pass

    label('loc_2306')

    OP_56(0x00)
    TalkEnd(0x000D)

    Return()

    def _loc_230C(): pass

    label('loc_230C')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_231D',
    )

    TalkEnd(0x000D)

    Return()

    def _loc_231D(): pass

    label('loc_231D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_23CB',
    )

    ChrTalk(
        0x000D,
        (
            '哦～早上好啊。\n',
            '这里是贝尔杂货店。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '本店商品种类非常齐全，\n',
            '能充分满足各位顾客的要求哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '所以……\n',
            '想买什么就请来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '本店的经营\n',
            '也要靠大家的支持。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A7A')

    def _loc_23CB(): pass

    label('loc_23CB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_241F',
    )

    ChrTalk(
        0x000D,
        (
            '啊，你们好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '贝尔杂货店\n',
            '今天也会以齐全的商品\n',
            '来满足大家的要求。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A7A')

    def _loc_241F(): pass

    label('loc_241F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_25B5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_24C2',
    )

    ChrTalk(
        0x000D,
        (
            '妻子她表示了\n',
            '对我想法的理解呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '她说店里以后也要像以前那样\n',
            '保持商品种类的齐全。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '妻子为了我也很努力。\n',
            '我以后也要\n',
            '更加努力才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_25B2')

    def _loc_24C2(): pass

    label('loc_24C2')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x000D,
        (
            '啊，早上好！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '今天一大早\n',
            '就有开心的事哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '妻子头一次\n',
            '对我的想法表示理解。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '她说店里以后也要像以前那样\n',
            '保持商品种类的齐全。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '虽说经营方面形势严峻，\n',
            '但是只要节约开支的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '这样的话\n',
            '我就能安心地和顾客面对面了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_25B2(): pass

    label('loc_25B2')

    Jump('loc_2A7A')

    def _loc_25B5(): pass

    label('loc_25B5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_26AF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_262F',
    )

    ChrTalk(
        0x000D,
        (
            '唔～通常情况下， \n',
            '只要我擅作主张降了价，她就会生气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '今天，她心情很不错呢，\n',
            '发生了什么好事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_26AC')

    def _loc_262F(): pass

    label('loc_262F')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x000D,
        (
            '总觉得最近\n',
            '妻子的态度有点奇怪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '她应该知道，出事的时候\n',
            '我在给镇里面的人分派商品……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '……为什么她不生气呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_26AC(): pass

    label('loc_26AC')

    Jump('loc_2A7A')

    def _loc_26AF(): pass

    label('loc_26AF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_2792',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_26FE',
    )

    ChrTalk(
        0x000D,
        (
            '妻子艾妲\n',
            '肩膀酸疼得厉害。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '今天也要去\n',
            '礼拜堂拿药呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_278F')

    def _loc_26FE(): pass

    label('loc_26FE')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x000D,
        (
            '妻子艾妲\n',
            '肩膀酸疼得厉害。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '今天也要去\n',
            '礼拜堂拿药呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '中央工房里面\n',
            '也有研究医学的老师……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '但效果还是比不上\n',
            '传统的医疗法呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_278F(): pass

    label('loc_278F')

    Jump('loc_2A7A')

    def _loc_2792(): pass

    label('loc_2792')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_2869',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_27FF',
    )

    ChrTalk(
        0x000D,
        (
            '我家大儿子\n',
            '似乎对商品陈列很有兴趣。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '放着他不管的话，\n',
            '他会整整一天都在搞那些东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2866')

    def _loc_27FF(): pass

    label('loc_27FF')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    ChrTurnDirection(0x000D, 0x000F, 400)

    ChrTalk(
        0x000D,
        (
            '喂喂，库诺。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '不要再动\n',
            '那些商品了好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '不是说好了\n',
            '一天只整理一次商品吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x000D, 0x0010)

    def _loc_2866(): pass

    label('loc_2866')

    Jump('loc_2A7A')

    def _loc_2869(): pass

    label('loc_2869')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_297A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_28C4',
    )

    ChrTalk(
        0x000D,
        (
            '整个城市的导力\n',
            '全部都停止了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '世界上还有\n',
            '这么不可思议的事呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2977')

    def _loc_28C4(): pass

    label('loc_28C4')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x000D,
        (
            '昨天晚上\n',
            '你们没事吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '我以为是照明灯出故障了，\n',
            '打算立即去工房看看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '谁知一走到外面，\n',
            '发现整个城镇就像森林里一样漆黑。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '我马上就意识到\n',
            '这不是什么简单的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2977(): pass

    label('loc_2977')

    Jump('loc_2A7A')

    def _loc_297A(): pass

    label('loc_297A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Return,
        ),
        'loc_2A23',
    )

    ChrTalk(
        0x000D,
        (
            '我立志要把这个店\n',
            '经营成受大家喜爱的店。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '不管什么样的人来，\n',
            '都能在这里找到称心的商品。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '虽然这样采购的时候会很麻烦，\n',
            '不过毕竟不努力就不会成功啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A7A')

    def _loc_2A23(): pass

    label('loc_2A23')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_2A7A',
    )

    ChrTalk(
        0x000D,
        (
            '您好，欢迎光临。\n',
            '这里是贝尔杂货店。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '从食品到日用品，\n',
            '这里都一应俱全。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2A7A(): pass

    label('loc_2A7A')

    TalkEnd(0x000D)

    Return()

# id: 0x000C offset: 0x2A7E
@scena.Code('func_0C_2A7E')
def func_0C_2A7E():
    TalkBegin(0x000E)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_2A8B',
    )

    Jump('loc_2B16')

    def _loc_2A8B(): pass

    label('loc_2A8B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_2B16',
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
        'loc_2B05',
    )

    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AE, 1, 0x571)),
            Expr.Return,
        ),
        'loc_2AF1',
    )

    OP_A9(0x4C)

    Jump('loc_2AFF')

    def _loc_2AF1(): pass

    label('loc_2AF1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_2AFD',
    )

    OP_A9(0x4B)

    Jump('loc_2AFF')

    def _loc_2AFD(): pass

    label('loc_2AFD')

    OP_A9(0x3E)

    def _loc_2AFF(): pass

    label('loc_2AFF')

    OP_56(0x00)
    TalkEnd(0x000E)

    Return()

    def _loc_2B05(): pass

    label('loc_2B05')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2B16',
    )

    TalkEnd(0x000E)

    Return()

    def _loc_2B16(): pass

    label('loc_2B16')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_2B84',
    )

    ChrTalk(
        0x000E,
        (
            '呼，这样子的话\n',
            '下个月可能也很辛苦吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '不过，我早已经有思想准备了，\n',
            '一定要努力渡过难关。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_31C7')

    def _loc_2B84(): pass

    label('loc_2B84')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_2BCD',
    )

    ChrTalk(
        0x000E,
        (
            '欢迎光临～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '这里是贝尔杂货店。\n',
            '请慢慢挑选喜欢的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_31C7')

    def _loc_2BCD(): pass

    label('loc_2BCD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_2C96',
    )

    ChrTalk(
        0x000E,
        (
            '今天早上，我和丈夫商量了一下，\n',
            '制定了今后的经营方针。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '我们决定努力\n',
            '让商品种类更加齐全。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '和以前不同， \n',
            '采购的活儿由我全部负责。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '这样做到底会怎么样。\n',
            '不尝试一下不会知道呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_31C7')

    def _loc_2C96(): pass

    label('loc_2C96')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_2DF2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_2D5F',
    )

    ChrTalk(
        0x000E,
        (
            '我似乎也开始明白\n',
            '丈夫的目标了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '他只会常常做梦，\n',
            '不能说是个会做生意的人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '他总想让我们的店\n',
            '能给大家带来最大的方便和好处。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '如果真能做成这样的店，\n',
            '的确是很了不起。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2DEF')

    def _loc_2D5F(): pass

    label('loc_2D5F')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x000E,
        (
            '听说今天在出事现场，\n',
            '丈夫给避难的人们\n',
            '配发了必要物资。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '这样的话， \n',
            '这个月又会是赤字了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '唉，没办法啦。\n',
            '就当是捐赠，算了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2DEF(): pass

    label('loc_2DEF')

    Jump('loc_31C7')

    def _loc_2DF2(): pass

    label('loc_2DF2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_2EC5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_2E57',
    )

    ChrTalk(
        0x000E,
        (
            '真是让人难以置信。\n',
            '中央工房竟然会遭到袭击……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '为什么丈夫\n',
            '会发现这件事呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2EC2')

    def _loc_2E57(): pass

    label('loc_2E57')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x000E,
        (
            '刚才听说，\n',
            '中央工房遭到袭击了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '我丈夫也是，\n',
            '出去后到现在还没有回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '真是让人担心啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2EC2(): pass

    label('loc_2EC2')

    Jump('loc_31C7')

    def _loc_2EC5(): pass

    label('loc_2EC5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_2F4F',
    )

    ChrTalk(
        0x000E,
        (
            '丈夫他嘴里说着\n',
            '出了点奇怪的事什么的，\n',
            '就跑出去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '而且还擅自将\n',
            '店里面的商品也带走了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '唉，\n',
            '他究竟在想什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_31C7')

    def _loc_2F4F(): pass

    label('loc_2F4F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_3034',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_2FBE',
    )

    ChrTalk(
        0x000E,
        (
            '呼呼，\n',
            '说起来还有工作没完成呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '时间早的话，收拾一下，\n',
            '然后去礼拜堂拿点治肩酸的药。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3031')

    def _loc_2FBE(): pass

    label('loc_2FBE')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x000E,
        (
            '导力器使用不了的话，\n',
            '我们就什么都干不了了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '昨天发生了那样的事情之后，\n',
            '我们不得不考虑一下这件事情呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3031(): pass

    label('loc_3031')

    Jump('loc_31C7')

    def _loc_3034(): pass

    label('loc_3034')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Return,
        ),
        'loc_3153',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_30A5',
    )

    ChrTalk(
        0x000E,
        (
            '如果不进一些好卖的商品，\n',
            '那就谈不上有什么利润了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '啊，不但肩膀重，\n',
            '头也开始疼了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3150')

    def _loc_30A5(): pass

    label('loc_30A5')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x000E,
        (
            '我丈夫也不考虑\n',
            '商品能不能卖出去，\n',
            '只会一味地进货又进货。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '如果不清楚这些商品能不能卖掉，\n',
            '经营起来真的是很辛苦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '都不知道他有没有想过\n',
            '怎么去把生意做好？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3150(): pass

    label('loc_3150')

    Jump('loc_31C7')

    def _loc_3153(): pass

    label('loc_3153')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_31C7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_318F',
    )

    ChrTalk(
        0x000E,
        (
            '呼，一看见账簿\n',
            '我就觉得肩膀好沉重……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_31C7')

    def _loc_318F(): pass

    label('loc_318F')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x000E,
        (
            '哈啊……\n',
            '真令人头疼啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '这个月又快超支了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_31C7(): pass

    label('loc_31C7')

    TalkEnd(0x000E)

    Return()

# id: 0x000D offset: 0x31CB
@scena.Code('func_0D_31CB')
def func_0D_31CB():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_320B',
    )

    ChrTalk(
        0x00FE,
        (
            '唔，真是少见呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '妈妈她\n',
            '竟然会表扬爸爸。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_33C0')

    def _loc_320B(): pass

    label('loc_320B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_329A',
    )

    ChrTalk(
        0x00FE,
        (
            '爸爸他为什么要拿走\n',
            '各种各样的东西啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '药品、食品什么的也就罢了，\n',
            '带着人偶打算干什么呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且还一副\n',
            '慌慌张张的样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_33C0')

    def _loc_329A(): pass

    label('loc_329A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_32F0',
    )

    ChrTalk(
        0x00FE,
        (
            '……………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……嗯。\n',
            '这下就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '已经没有我\n',
            '去帮忙的必要了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_33C0')

    def _loc_32F0(): pass

    label('loc_32F0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_33C0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_3359',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然爸爸说\n',
            '一天整理一次商品就行了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过客人已经动过了，\n',
            '必须按照原样放好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_33C0')

    def _loc_3359(): pass

    label('loc_3359')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '嗯，\n',
            '然后将这条鱼放回左边。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……嗯，这下就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，终于又回到\n',
            '最完美的陈列状态了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_33C0(): pass

    label('loc_33C0')

    TalkEnd(0x00FE)

    Return()

# id: 0x000E offset: 0x33C4
@scena.Code('func_0E_33C4')
def func_0E_33C4():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_342F',
    )

    ChrTalk(
        0x00FE,
        (
            '博士！不得了了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '妈妈的肩\n',
            '好像开始疼起来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '什么！赶快啊。\n',
            '快点和教区长联系！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_361B')

    def _loc_342F(): pass

    label('loc_342F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_3454',
    )

    ChrTalk(
        0x00FE,
        (
            '今天去\n',
            '肯定还来得及。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_361B')

    def _loc_3454(): pass

    label('loc_3454')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_3484',
    )

    ChrTalk(
        0x00FE,
        (
            '我说，妈妈。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '爸爸在哪儿呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_361B')

    def _loc_3484(): pass

    label('loc_3484')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_34C6',
    )

    ChrTalk(
        0x00FE,
        (
            '昨天晚上\n',
            '外面好暗呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我睡在床上\n',
            '都看见了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_361B')

    def _loc_34C6(): pass

    label('loc_34C6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Return,
        ),
        'loc_35FA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_351E',
    )

    ChrTurnDirection(0x00FE, 0x0107, 0)

    ChrTalk(
        0x00FE,
        (
            '博士！\n',
            '导力压下降了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '什么！\n',
            '导力引擎的功率很正常啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_35F7')

    def _loc_351E(): pass

    label('loc_351E')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))
    ChrTurnDirection(0x00FE, 0x0107, 0)

    ChrTalk(
        0x00FE,
        (
            '哇～啊，\n',
            '是提妲姐～姐啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们来玩导力技师游戏吧。\n',
            '玩导力技师游戏。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#560F不好意思啊，呆呆。\n',
            '姐姐现在要给客人们带路啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#061F所以呢，还是下次玩吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，好吧～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我明白～了，提妲博士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_35F7(): pass

    label('loc_35F7')

    Jump('loc_361B')

    def _loc_35FA(): pass

    label('loc_35FA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_361B',
    )

    ChrTalk(
        0x00FE,
        (
            '姐姐～你们是谁～啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_361B(): pass

    label('loc_361B')

    TalkEnd(0x00FE)

    Return()

# id: 0x000F offset: 0x361F
@scena.Code('func_0F_361F')
def func_0F_361F():
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
        'loc_3689',
    )

    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 1, 0x531)),
            Expr.Return,
        ),
        'loc_3681',
    )

    OP_A9(0x42)

    Jump('loc_3683')

    def _loc_3681(): pass

    label('loc_3681')

    OP_A9(0x3D)

    def _loc_3683(): pass

    label('loc_3683')

    OP_56(0x00)
    TalkEnd(0x0011)

    Return()

    def _loc_3689(): pass

    label('loc_3689')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_369A',
    )

    TalkEnd(0x0011)

    Return()

    def _loc_369A(): pass

    label('loc_369A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_37F5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_3735',
    )

    ChrTalk(
        0x0011,
        (
            '不管怎么说\n',
            '老板也是个成功的人，\n',
            '值得学习的地方我也要学着点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '唉，\n',
            '就是觉得他思想有点顽固……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '把这些也算在\n',
            '学习范围之内吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_37F2')

    def _loc_3735(): pass

    label('loc_3735')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x0011,
        (
            '昨天，和斯坦因老板\n',
            '商量了一下采购的事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '暂时先决定按照\n',
            '老板的意向来选择商品。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '不过我并没有完全理解\n',
            '这位重视可靠性的\n',
            '斯坦因老板的想法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '啊，这也是需要学习的地方吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_37F2(): pass

    label('loc_37F2')

    Jump('loc_405D')

    def _loc_37F5(): pass

    label('loc_37F5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_391D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_387B',
    )

    ChrTalk(
        0x0011,
        (
            '唔，\n',
            '那个加鲁诺竟然会这么说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '我也渐渐觉得\n',
            '老板的话有些合理了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '……不、不行。\n',
            '不能受别人的影响。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_391A')

    def _loc_387B(): pass

    label('loc_387B')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x0011,
        (
            '今天一大清早加鲁诺就来了，\n',
            '只说了一句『我明白老板话里的意思了』，\n',
            '之后就回去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '唔，\n',
            '那个加鲁诺竟然会这么说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '老板的想法\n',
            '到底哪里正确了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_391A(): pass

    label('loc_391A')

    Jump('loc_405D')

    def _loc_391D(): pass

    label('loc_391D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_39E6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_3971',
    )

    ChrTalk(
        0x0011,
        (
            '唔，加鲁诺那家伙……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '不知道怎么\n',
            '就被斯坦因老板给教唆了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_39E3')

    def _loc_3971(): pass

    label('loc_3971')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x0011,
        (
            '今天一大清早加鲁诺就来了，\n',
            '只说了一句『我明白老板话里的意思了』，\n',
            '之后就回去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '那家伙\n',
            '到底怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_39E3(): pass

    label('loc_39E3')

    Jump('loc_405D')

    def _loc_39E6(): pass

    label('loc_39E6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_3A39',
    )

    ChrTalk(
        0x0011,
        (
            '哦，这么晚还有客人来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '店还没有关门，\n',
            '请放心挑选我们的商品吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_405D')

    def _loc_3A39(): pass

    label('loc_3A39')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_3AE9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_3A83',
    )

    ChrTalk(
        0x0011,
        (
            '有什么损失吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '要是研究计划\n',
            '没受影响就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3AE6')

    def _loc_3A83(): pass

    label('loc_3A83')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x0011,
        (
            '喂，你们听说了吗？\n',
            '中央工房遭到袭击了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '当时我在店里面忙着聊天，\n',
            '一点都没有注意到啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3AE6(): pass

    label('loc_3AE6')

    Jump('loc_405D')

    def _loc_3AE9(): pass

    label('loc_3AE9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_3C1A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_3B50',
    )

    ChrTalk(
        0x0011,
        (
            '哇，\n',
            '真的是一把非常棒的导力枪呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '平衡性若是再好些，\n',
            '我想肯定会更加畅销的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3C17')

    def _loc_3B50(): pass

    label('loc_3B50')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x0011,
        (
            '中央工房的加鲁诺\n',
            '把研究中的导力枪带来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '那家伙真厉害。\n',
            '真是把很棒的导力枪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '不过整体的平衡性有些特殊\n',
            '导致难以操作……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '就算操作多多少少有点难，\n',
            '不过只要威力强大就足以弥补了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3C17(): pass

    label('loc_3C17')

    Jump('loc_405D')

    def _loc_3C1A(): pass

    label('loc_3C1A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_3DAE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_3C83',
    )

    ChrTalk(
        0x0011,
        (
            '啊啊，加鲁诺……\n',
            '快把试制品拿来看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '最近唯一的期盼\n',
            '就是能看到那件产品了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3DAB')

    def _loc_3C83(): pass

    label('loc_3C83')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x0011,
        (
            '呵呵，欢迎啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '哎呀，\n',
            '又和斯坦因老板因为采购的事\n',
            '而发生争执了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '不管我们怎么说，\n',
            '他就是不愿意引进\n',
            '还处于研究阶段的导力枪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '虽然我已经尽可能劝说他了，\n',
            '不过我只是个被雇来的店长，没有权利管他啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '啊啊，加鲁诺……\n',
            '快把试制品拿来看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '最近嘛，\n',
            '只有这么点期盼了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3DAB(): pass

    label('loc_3DAB')

    Jump('loc_405D')

    def _loc_3DAE(): pass

    label('loc_3DAE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_3E84',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_3E0F',
    )

    ChrTalk(
        0x0011,
        (
            '中央工房里面\n',
            '现在一定乱成一团了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '因为那里\n',
            '全都是测量用的机器呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3E81')

    def _loc_3E0F(): pass

    label('loc_3E0F')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x0011,
        (
            '昨天晚上，\n',
            '我正在调整导力枪……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '突然，\n',
            '测量器停止了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '我还以为把商品弄坏了，\n',
            '当时一下子傻了眼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3E81(): pass

    label('loc_3E81')

    Jump('loc_405D')

    def _loc_3E84(): pass

    label('loc_3E84')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Return,
        ),
        'loc_3FFA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_3EFD',
    )

    ChrTalk(
        0x0011,
        (
            '我虽然也明白老板\n',
            '把武器的可靠性放在第一位的信条……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '不过稍微想想，\n',
            '老板是否有点太过固执了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3FF7')

    def _loc_3EFD(): pass

    label('loc_3EFD')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x0011,
        (
            '我们这里的老板是斯坦因，\n',
            '就住在这附近……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '根据斯坦因先生的原则，\n',
            '我们是绝对不会引进\n',
            '最先进的高尖端武器的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '这好像是因为\n',
            '过于先进的武器\n',
            '可靠性还得不到认可……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '有个工房的研究员亲自来出售\n',
            '正在研究中的超级导力枪，\n',
            '也被老板拒绝了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3FF7(): pass

    label('loc_3FF7')

    Jump('loc_405D')

    def _loc_3FFA(): pass

    label('loc_3FFA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_405D',
    )

    ChrTalk(
        0x0011,
        (
            '哦，欢迎光临。\n',
            '这里是斯坦因武器商会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '本店全是各种各样的好商品。\n',
            '请慢慢地看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_405D(): pass

    label('loc_405D')

    TalkEnd(0x0011)

    Return()

# id: 0x0010 offset: 0x4061
@scena.Code('func_10_4061')
def func_10_4061():
    TalkBegin(0x0012)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_418A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_40E3',
    )

    ChrTalk(
        0x00FE,
        (
            '虽说我也很在意博士这件事，\n',
            '不过现在也只有相信阿加特那家伙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '毕竟我们身上也有些\n',
            '非做不可的任务啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4187')

    def _loc_40E3(): pass

    label('loc_40E3')

    ChrTalk(
        0x00FE,
        (
            '哦，是你们啊。\n',
            '我听说你们的营救作战了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然事情还不算完美解决，\n',
            '不过现在也只有相信阿加特那家伙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果是那家伙出马， \n',
            '应该能让博士他们安全逃离的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4187(): pass

    label('loc_4187')

    Jump('loc_498C')

    def _loc_418A(): pass

    label('loc_418A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_453A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AF, 6, 0x57E)),
            Expr.Return,
        ),
        'loc_4245',
    )

    ChrTalk(
        0x00FE,
        (
            '王那家伙好像也是充满干劲地工作着，\n',
            '这样我就放心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '以前还担心他会因为\n',
            '觉得自己应该对事故负责\n',
            '而意志消沉下来呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是不是雾香\n',
            '用什么巧妙的办法激励他了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4537')

    def _loc_4245(): pass

    label('loc_4245')

    SetScenaFlags(ScenaFlag(0x00AF, 6, 0x57E))

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AF, 5, 0x57D)),
            Expr.Return,
        ),
        'loc_430B',
    )

    ChrTalk(
        0x0101,
        (
            '#000F啊，冈多夫先生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F是刚从王都回来的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哦，我刚得知了消息。\n',
            '然后就匆匆忙忙赶回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '雾香她已经告诉我\n',
            '这边大概的事情了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '阿加特那家伙\n',
            '已经没事了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_43C2')

    def _loc_430B(): pass

    label('loc_430B')

    ChrTalk(
        0x00FE,
        (
            '对了，\n',
            '你们就是那两个准游击士吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我是蔡斯所属的游击士，\n',
            '名叫冈多夫。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我听到消息之后， \n',
            '就从出差地王都赶了回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大体情况我已经问过雾香了……\n',
            '呃，阿加特他没事吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_43C2(): pass

    label('loc_43C2')

    ChrTalk(
        0x0101,
        (
            '#000F嗯，还好度过了危险期……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '……哎，你认识阿加特吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊，因为工作的关系\n',
            '我们已经见过很多次面了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '很久之前他\n',
            '就已经是个非常有名的家伙啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……总之，\n',
            '他没事就好啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，搜查的工作\n',
            '就交给你们和阿加特了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而我们就尽量去\n',
            '处理一些日常的零碎工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯，谢谢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '那就拜托您了。\n',
            '冈多夫先生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F我们告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哦，你们要保重哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4537(): pass

    label('loc_4537')

    Jump('loc_498C')

    def _loc_453A(): pass

    label('loc_453A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_498C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AF, 5, 0x57D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4942',
    )

    SetScenaFlags(ScenaFlag(0x00AF, 5, 0x57D))
    OP_4A(0x0013, 255)
    OP_4A(0x0012, 255)

    ChrTalk(
        0x0013,
        (
            '嗯？　出差！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '冈多夫先生你……吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '啊，不好意思。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '因为军方直接点名……\n',
            '我必须去一趟王都。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '又不是只剩下你一个，\n',
            '那些准游击士也在嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '你们同心协力的话，\n',
            '两三天肯定能应付过来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '是啊，是这样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '我明白了。\n',
            '我会拼命努力的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '哦……\n',
            '总之乐观一点吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '……嗯？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0012, 0x0000, 400)

    ChrTalk(
        0x0012,
        (
            '……哦，\n',
            '这就是传闻中的两个人吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '你们两个\n',
            '来得真是时候啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AF, 4, 0x57C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4794',
    )

    SetScenaFlags(ScenaFlag(0x00AF, 4, 0x57C))

    ChrTalk(
        0x0013,
        (
            '……嗯？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0013, 0x0000, 400)

    ChrTalk(
        0x0013,
        (
            '难道……\n',
            '你们就是那些准游击士？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F……嗯？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '啊，没错。\n',
            '我们就是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F初次见面。\n',
            '我是准游击士约修亚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊。\n',
            '我是准游击士艾丝蒂尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_47D4')

    def _loc_4794(): pass

    label('loc_4794')

    ChrTurnDirection(0x0013, 0x0000, 400)

    ChrTalk(
        0x0013,
        (
            '啊，\n',
            '是艾丝蒂尔和约修亚吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '你们来得正是时候。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_47D4(): pass

    label('loc_47D4')

    ChrTalk(
        0x0012,
        (
            '呵呵，果然是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '看到你们，\n',
            '我终于明白雾香说的话了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F对了，\n',
            '请问您要去王都吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '啊啊，没错。\n',
            '那边有很紧急的任务。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '蔡斯支部的工作\n',
            '就交给你们和王负责了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '你们就好好努力吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '……就是这样。\n',
            '总之希望能借助你们的力量。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯，知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F好，我们会尽全力的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '那就这样吧。\n',
            '拜托你们留守了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4B(0x0013, 255)
    OP_4B(0x0012, 255)
    ChrClearFlags(0x0012, 0x0010)
    ChrClearFlags(0x0013, 0x0010)

    Jump('loc_498C')

    def _loc_4942(): pass

    label('loc_4942')

    ChrTalk(
        0x0012,
        (
            '不好意思，\n',
            '拜托你们在这里留守了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '你们要和王那家伙\n',
            '好好合作啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_498C(): pass

    label('loc_498C')

    TalkEnd(0x0012)

    Return()

# id: 0x0011 offset: 0x4990
@scena.Code('func_11_4990')
def func_11_4990():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_4AC2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_4A1D',
    )

    ChrTalk(
        0x00FE,
        (
            '对了，\n',
            '听说你们要去王都了对吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没关系，\n',
            '你们肯定能够很快成为正游击士的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '以后也要精力充沛地\n',
            '努力工作哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4ABF')

    def _loc_4A1D(): pass

    label('loc_4A1D')

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x00FE,
        (
            '啊，是你们……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我听说了哦，\n',
            '营救作战按照计划顺利实行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然博士他们以后会怎样\n',
            '现在还不能放心……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总之，很感谢你们。\n',
            '谢谢把他们救了出来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4ABF(): pass

    label('loc_4ABF')

    Jump('loc_548B')

    def _loc_4AC2(): pass

    label('loc_4AC2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_4F53',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AF, 5, 0x57D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4ECA',
    )

    SetScenaFlags(ScenaFlag(0x00AF, 5, 0x57D))
    OP_4A(0x0012, 255)
    OP_4A(0x0013, 255)

    ChrTalk(
        0x0013,
        (
            '嗯？　出差！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '冈多夫先生你……吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '啊，不好意思。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '因为军方直接点名……\n',
            '我必须去一趟王都。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '又不是只剩下你一个，\n',
            '那些准游击士也在嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '你们同心协力的话，\n',
            '两三天肯定能应付过来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '是啊，是这样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '我明白了。\n',
            '我会拼命努力的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '哦……\n',
            '总之乐观一点吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '……嗯？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0012, 0x0000, 400)

    ChrTalk(
        0x0012,
        (
            '……哦，\n',
            '这就是传闻中的两个人吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '你们两个\n',
            '来得真是时候啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AF, 4, 0x57C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4D1C',
    )

    SetScenaFlags(ScenaFlag(0x00AF, 4, 0x57C))

    ChrTalk(
        0x0013,
        (
            '……嗯？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0013, 0x0000, 400)

    ChrTalk(
        0x0013,
        (
            '难道……\n',
            '你们就是那些准游击士？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F……嗯？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '啊，没错。\n',
            '我们就是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F初次见面。\n',
            '我是准游击士约修亚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊。\n',
            '我是准游击士艾丝蒂尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4D5C')

    def _loc_4D1C(): pass

    label('loc_4D1C')

    ChrTurnDirection(0x0013, 0x0000, 400)

    ChrTalk(
        0x0013,
        (
            '啊，\n',
            '是艾丝蒂尔和约修亚吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '你们来得正是时候。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4D5C(): pass

    label('loc_4D5C')

    ChrTalk(
        0x0012,
        (
            '呵呵，果然是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '看到你们，\n',
            '我终于明白雾香说的话了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F对了，\n',
            '请问您要去王都吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '啊啊，没错。\n',
            '那边有很紧急的任务。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '蔡斯支部的工作\n',
            '就交给你们和王负责了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '你们就好好努力吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '……就是这样。\n',
            '总之希望能借助你们的力量。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯，知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F好，我们会尽全力的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '那就这样吧。\n',
            '拜托你们留守了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x0012, 0x0010)
    ChrClearFlags(0x0013, 0x0010)
    OP_4B(0x0012, 255)
    OP_4B(0x0013, 255)

    Jump('loc_4F50')

    def _loc_4ECA(): pass

    label('loc_4ECA')

    ChrTalk(
        0x00FE,
        (
            '接下来一段时间\n',
            '冈多夫先生要到别的地方出差……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好吧，今后的工作， \n',
            '必须更加充满干劲去做才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '希望你们\n',
            '也能够协助我哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_4F50(): pass

    label('loc_4F50')

    Jump('loc_548B')

    def _loc_4F53(): pass

    label('loc_4F53')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Return,
        ),
        'loc_537A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AF, 4, 0x57C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_530B',
    )

    SetScenaFlags(ScenaFlag(0x00AF, 4, 0x57C))

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4FA8',
    )

    ChrTalk(
        0x00FE,
        (
            '啊啊，提妲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '竟然会来武器店，真少见啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4FDA')

    def _loc_4FA8(): pass

    label('loc_4FA8')

    ChrTurnDirection(0x00FE, 0x0107, 0)

    ChrTalk(
        0x00FE,
        (
            '嗯……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊，\n',
            '原来是提妲来了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4FDA(): pass

    label('loc_4FDA')

    ChrTalk(
        0x00FE,
        (
            '咦……？\n',
            '这两位不会是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#060F啊，是的。\n',
            '他们都是游击士哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我现在要带他们\n',
            '到我家里去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊，果然是这样啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我的名字叫做王。\n',
            '是蔡斯支部所属的游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我现在还是个新人，\n',
            '和你们差不多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊，是这样啊。\n',
            '彼此彼此，多多关照哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我是准游击士艾丝蒂尔。\n',
            '旁边的那位是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F我是约修亚，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '请多多关照。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我之前听雾香说过\n',
            '有关你们的事情。\n',
            '果然来了很厉害的准游击士呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '听说你们在全国各地\n',
            '都做出了相当的成绩呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#008F嘿嘿，就算是这样吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F说到成绩，\n',
            '我们只是尽了自己的本分而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '而且多亏得到了游击士前辈\n',
            '和各地百姓的鼎力相助。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈哈，\n',
            '我觉得能够得到百姓信任，\n',
            '得到他们的帮助也是一种才能呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '实际上，\n',
            '我们支部也处于人手不足的状态。\n',
            '我相当期待你们的表现哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '以后这段时间\n',
            '还要请你们多多关照啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#001F嗯，彼此彼此。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F还请以后多多指教。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5377')

    def _loc_530B(): pass

    label('loc_530B')

    ChrTalk(
        0x00FE,
        (
            '哟，艾丝蒂尔、约修亚。\n',
            '我相当期待你们今后的表现哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '也许相处时间不会太长，\n',
            '还要请你们多多关照啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_5377(): pass

    label('loc_5377')

    Jump('loc_548B')

    def _loc_537A(): pass

    label('loc_537A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_548B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_540A',
    )

    ChrTalk(
        0x00FE,
        (
            '是选平衡性呢，\n',
            '还是选突出的特性呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '算了，归根到底\n',
            '还是要看使用者的本事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我大概还没有可以\n',
            '选择武器的实力吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_548B')

    def _loc_540A(): pass

    label('loc_540A')

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x00FE,
        (
            '唔，好难啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是选性能比较平衡的武器呢，\n',
            '还是选非常有特点的武器呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是能二者兼顾的话，\n',
            '就不用那么烦恼了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_548B(): pass

    label('loc_548B')

    TalkEnd(0x00FE)

    Return()

# id: 0x0012 offset: 0x548F
@scena.Code('func_12_548F')
def func_12_548F():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Or,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_54A6',
    )

    Call(0, 0x000C)

    Jump('loc_54AA')

    def _loc_54A6(): pass

    label('loc_54A6')

    Call(0, 0x000B)

    def _loc_54AA(): pass

    label('loc_54AA')

    Return()

# id: 0x0013 offset: 0x54AB
@scena.Code('func_13_54AB')
def func_13_54AB():
    Call(0, 0x000F)

    Return()

# id: 0x0014 offset: 0x54B0
@scena.Code('func_14_54B0')
def func_14_54B0():
    EventBegin(0x00)
    CameraMove(2000, 0, -5200, 0)
    ChrSetPos(0x0101, 2400, 0, -5400, 0)
    ChrSetPos(0x0102, 1300, 0, -5500, 0)
    OP_4A(0x0008, 255)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010070576V#501F午安～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070577V#010F打扰了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_553C')
    def lambda_553C():
        CameraMove(3600, 0, 520, 2500)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_553C)

    @scena.Lambda('lambda_5554')
    def lambda_5554():
        ChrWalkTo(0x00FE, 3800, 0, -700, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5554)

    Sleep(500)

    @scena.Lambda('lambda_5574')
    def lambda_5574():
        ChrWalkTo(0x00FE, 3000, 0, -700, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_5574)

    WaitForThreadExit(0x0101, 0x0001)

    NpcTalk(
        0x0008,
        '东方打扮的女性',
        (
            '#0580070578V#792F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070579V#006F那个～我们是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '东方打扮的女性',
        (
            '#0580070580V#790F……总算到了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580070581V#790F艾丝蒂尔、约修亚。\n',
            '欢迎来到蔡斯支部。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070582V#004F咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070583V#014F您知道我们的事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '东方打扮的女性',
        (
            '#0580070584V#792F卢安支部的嘉恩\n',
            '已经和我联络过了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580070585V栗色的双马尾，\n',
            '黑发和琥珀色的眼睛……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580070586V#791F就是你们了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070587V#008F原、原来如此……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '东方打扮的女性',
        (
            '#0580070588V#790F我叫雾香，\n',
            '是蔡斯支部的负责人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580070589V以后就请多关照了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070590V#006F啊～嗯，彼此彼此！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070591V#010F请多指教。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0580070592V#790F那么……虽然有点仓促，\n',
            '我们还是先办理转属手续吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580070593V请在这些文件上签字。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070594V#000F嗯，好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔和约修亚\n',
            '在转属手续的文件上签了字。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0008,
        (
            '#0580070595V#792F……这就可以了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580070596V#790F从今天开始，\n',
            '你们就归蔡斯支部所属了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580070597V不过现在还没有\n',
            '什么紧要的任务要去执行。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580070598V你们就检查一下公告板，\n',
            '以自己的步调来安排工作吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070599V#007F稍微有点失望呢。\n',
            '不过嘛，没什么紧要的事也是好事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010070600V#002F对了，雾香姐。\n',
            '有一件事情想请问你……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0580070601V#792F是卡西乌斯先生的事吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070602V#004F哎！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070603V#014F请问……\n',
            '这也是从嘉恩先生那里听说的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0580070604V#790F大致听说了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580070605V不过很可惜，\n',
            '卡西乌斯先生不在蔡斯。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580070606V也许是忙于紧要的公务吧，\n',
            '他已经数月没到本支部来过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070607V#505F啊，是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070608V#013F那剩下的只有王都了，又或者……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0580070609V#792F不过关于另一件事，\n',
            '倒有点线索可以提供给你们。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580070610V这个拿去吧。',
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
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '给工房长的介绍信',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    AddItem(0x0360, 1)

    ChrTalk(
        0x0101,
        (
            '#0010070611V#004F哎，这个是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0580070612V#790F这是给中央工房的负责人\n',
            '玛多克工房长的介绍信。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580070613V他在蔡斯可是一位\n',
            '地位有如市长般的人物。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070614V#012F难不成……\n',
            '是关于黑色导力器的事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0580070615V#790F单从发生在市长官邸的事来看，\n',
            '的确是相当神秘的东西。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580070616V你们还是先去找\n',
            '玛多克工房长商量一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070617V#008F真、真是\n',
            '准备得太周到了呢～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010070618V雾香姐您难道有超能力？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0580070619V#790F支援你们游击士\n',
            '就是我的本职工作啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580070620V只不过是根据得到的情报\n',
            '做出相应的准备罢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070621V#506F劳、劳您费心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070622V#019F真是帮了大忙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0580070623V#791F不用客气。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580070624V要是有什么事件发生的话，\n',
            '可还是要麻烦你们俩回来工作哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070625V#008F啊哈哈……\n',
            '好！到时候就交给我们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070626V#010F既然如此，\n',
            '那我们马上去见工房长吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070627V#006F嗯，走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0053, 0x03, 0x02)
    OP_28(0x0053, 0x03, 0x04)
    OP_28(0x003F, 0x04, 0x02)
    OP_28(0x003F, 0x04, 0x04)
    OP_28(0x003F, 0x01, 0x0001)
    OP_4B(0x0008, 255)
    EventEnd(0x00)

    Return()

# id: 0x0015 offset: 0x5FEE
@scena.Code('func_15_5FEE')
def func_15_5FEE():
    EventBegin(0x00)
    CameraMove(1370, 0, -2580, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(345000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0102, 760, 0, -4930, 0)
    ChrSetPos(0x0101, 1850, 0, -5150, 0)
    ChrSetPos(0x0107, 1150, 0, -5860, 0)
    ChrSetPos(0x0106, 2350, 0, -5930, 0)

    @scena.Lambda('lambda_6077')
    def lambda_6077():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_6077')

    DispatchAsync2(0x0101, 0x0001, lambda_6077)

    @scena.Lambda('lambda_6088')
    def lambda_6088():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_6088')

    DispatchAsync2(0x0102, 0x0001, lambda_6088)

    @scena.Lambda('lambda_6099')
    def lambda_6099():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_6099')

    DispatchAsync2(0x0106, 0x0001, lambda_6099)

    @scena.Lambda('lambda_60AA')
    def lambda_60AA():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_60AA')

    DispatchAsync2(0x0107, 0x0001, lambda_60AA)

    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0009, 4070, 0, -700, 0)
    OP_4A(0x0008, 255)
    OP_4A(0x0009, 255)
    FadeIn(2000, 0)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0580081049V#790F#3P你们回来得正好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010081050V#004F咦……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020081051V#014F您是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_614B')
    def lambda_614B():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_614B)

    Sleep(400)

    ChrTalk(
        0x0009,
        (
            '#0150081052V#130F哎呀……\n',
            '艾丝蒂尔、约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150081053V好久不见了，你们还好吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_61B6')
    def lambda_61B6():
        CameraMove(3150, 0, -410, 1500)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_61B6)

    @scena.Lambda('lambda_61CE')
    def lambda_61CE():
        ChrWalkTo(0x00FE, 3060, 0, -1580, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_61CE)

    Sleep(100)

    @scena.Lambda('lambda_61EE')
    def lambda_61EE():
        ChrWalkTo(0x00FE, 2180, 0, -1130, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_61EE)

    Sleep(50)

    @scena.Lambda('lambda_620E')
    def lambda_620E():
        ChrWalkTo(0x00FE, 3970, 0, -2700, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0106, 0x0002, lambda_620E)

    Sleep(100)

    @scena.Lambda('lambda_622E')
    def lambda_622E():
        ChrWalkTo(0x00FE, 2630, 0, -2750, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0002, lambda_622E)

    WaitForThreadExit(0x0009, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010081054V#501F这不是亚鲁瓦教授嘛。\n',
            '你也到蔡斯来了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010081055V怎么，是来委托护卫工作吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0580081056V#792F并不是这样的，\n',
            '绑架犯的下落已经清楚了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580081057V这位先生就是目击者。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0106, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0107, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010081058V#004F哎……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050081059V#054F什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0150081060V#131F#2P嗯……\n',
            '那果然不是普通事件啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150081061V还好我及时赶来通报了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150081062V其实是这样的……\n',
            '我刚才一直在塔里面做研究调查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010081063V#002F说到塔……\n',
            '又是『四轮之塔』的其中一个吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050081064V#552F蔡斯有塔的地方……\n',
            '是在平原道北面的『红莲之塔』吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0150081065V#131F#2P嗯，没错。\n',
            '我看到有几个军人进到塔里去了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150081066V起初我还以为王国军也对那塔有兴趣，\n',
            '来做调查什么的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150081067V但不可思议的是……\n',
            '我在角落里听到他们说什么绑架、\n',
            '逃跑路线之类不对劲的话。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150081068V我觉得这件事很不寻常，\n',
            '所以就急急忙忙来这里通报了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020081069V#012F请问一下……\n',
            '那些军人穿着什么样的服装？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0150081070V#130F#2P唔，是以蓝白色为基调，\n',
            '很华丽很端庄的王国军军服……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150081071V不愧是女王陛下的国家，\n',
            '连军人的衣着也如此体面潇洒。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0106, 0xFF)
    ChrTurnDirection(0x0106, 0x0101, 400)

    ChrTalk(
        0x0106,
        (
            '#0050081072V#057F就此决定了……\n',
            '快去『红莲之塔』吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_6707')
    def lambda_6707():
        ChrTurnDirection(0x00FE, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_6707)

    @scena.Lambda('lambda_6715')
    def lambda_6715():
        ChrTurnDirection(0x00FE, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_6715)

    ChrTalk(
        0x0101,
        (
            '#0010081073V#005F嗯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020081074V#012F明白了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070081075V#065F那、那个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0106, 0xFF)
    TerminateThread(0x0107, 0xFF)

    @scena.Lambda('lambda_6788')
    def lambda_6788():
        CameraMove(3060, 0, -1580, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_6788)

    @scena.Lambda('lambda_67A0')
    def lambda_67A0():
        ChrTurnDirection(0x00FE, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_67A0)

    @scena.Lambda('lambda_67AE')
    def lambda_67AE():
        ChrTurnDirection(0x00FE, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_67AE)

    ChrTurnDirection(0x0106, 0x0107, 400)
    WaitForThreadExit(0x0101, 0x0003)
    WaitForThreadExit(0x0101, 0x0003)

    ChrTalk(
        0x0107,
        (
            '#0070081076V#062F艾丝蒂尔姐姐，请你们……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070081077V也、也带我一起去吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010081078V#004F#2P提妲……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020081079V#013F#5P这可……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0106, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1200)

    OP_63(0x0106)

    ChrTalk(
        0x0106,
        (
            '#0050081080V#050F喂喂，小不点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0107, 0xFF)
    ChrTurnDirection(0x0107, 0x0106, 400)

    ChrTalk(
        0x0107,
        (
            '#0070081081V#065F哎……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050081082V#050F我说啊……\n',
            '我们不可能带你去的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050081083V用常识想想，常识啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070081084V#063F但、但是但是……！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070081085V爷爷他被掳走了呢，\n',
            '我……我……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050081086V#053F没时间了，\n',
            '我就跟你直说好了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050081087V#057F你是个累赘，不要跟来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070081088V#065F……！',
            TxtCtl.Enter,
        ),
    )

    OP_9E(0x0107, 15, 0, 300, 4000)
    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    TerminateThread(0x0101, 0xFF)
    ChrTurnDirection(0x0101, 0x0106, 500)

    ChrTalk(
        0x0101,
        (
            '#0010081089V#005F等、等一下！\n',
            '这样说也太过分了吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050081090V#057F闭嘴。\n',
            '你也应该很清楚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050081091V她是个外行人，而且又是个小鬼，\n',
            '我们哪有余闲来照顾她。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010081092V#003F这、这个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 600)

    ChrTalk(
        0x0101,
        (
            '#0010081093V#009F约修亚，你也说点什么啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020081094V#013F很遗憾……我也反对。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020081095V那些黑衣人行事几乎毫无破绽，\n',
            '追击的困难大家可想而知。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020081096V为了安全起见，\n',
            '我不赞同带提妲去那么危险的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0107, 0x0102, 400)

    ChrTalk(
        0x0107,
        (
            '#0070081097V#065F约、约修亚哥哥……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010081098V#007F呜～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0107, 400)

    ChrTalk(
        0x0101,
        (
            '#0010081099V#003F……抱歉，提妲。\n',
            '看来还是不能带你去……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0107, 0x0101, 400)

    ChrTalk(
        0x0107,
        (
            '#0070081100V#065F艾、艾丝蒂尔姐姐也……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_9E(0x0107, 20, 0, 300, 4000)

    ChrTalk(
        0x0107,
        (
            '#0070081101V#069F……过分……好过分……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_6CEA')
    def lambda_6CEA():
        ChrTurnDirection(0x00FE, 0x0107, 400)
        Yield()

        Jump('lambda_6CEA')

    DispatchAsync2(0x0101, 0x0001, lambda_6CEA)

    @scena.Lambda('lambda_6CFB')
    def lambda_6CFB():
        ChrTurnDirection(0x00FE, 0x0107, 400)
        Yield()

        Jump('lambda_6CFB')

    DispatchAsync2(0x0102, 0x0001, lambda_6CFB)

    @scena.Lambda('lambda_6D0C')
    def lambda_6D0C():
        ChrTurnDirection(0x00FE, 0x0107, 400)
        Yield()

        Jump('lambda_6D0C')

    DispatchAsync2(0x0106, 0x0001, lambda_6D0C)

    OP_62(0x0107, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)
    ChrSetDirection(0x0107, 225, 800)

    @scena.Lambda('lambda_6D36')
    def lambda_6D36():
        CameraMove(2320, 0, -1650, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_6D36)

    ChrWalkTo(0x0107, 1730, 0, -4610, 5000, 0x00)
    ChrWalkTo(0x0107, 1520, 0, -6020, 5000, 0x00)
    PlaySE(6, 0x00, 0x64)
    Sleep(100)

    ChrWalkTo(0x0107, 1780, 0, -7840, 5000, 0x00)
    ChrSetFlags(0x0107, 0x0080)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0106, 0xFF)

    ChrTalk(
        0x0101,
        (
            '#0010081102V#004F提妲！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_6DC2')
    def lambda_6DC2():
        ChrWalkTo(0x00FE, 2340, 0, -2690, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_6DC2)

    Sleep(50)

    ChrWalkTo(0x0102, 2300, 0, -1820, 4000, 0x00)

    @scena.Lambda('lambda_6DF6')
    def lambda_6DF6():
        ChrMoveTo(0x00FE, 2340, 0, -2690, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_6DF6)

    @scena.Lambda('lambda_6E11')
    def lambda_6E11():
        ChrSetDirection(0x00FE, 225, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_6E11)

    @scena.Lambda('lambda_6E1F')
    def lambda_6E1F():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_6E1F')

    DispatchAsync2(0x0102, 0x0001, lambda_6E1F)

    ChrTalk(
        0x0102,
        (
            '#0020081103V#012F等等，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020081104V#015F现在就任她去吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020081105V我们得尽快救出博士，\n',
            '让她能早点安心才是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x0E, 0x0F, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010081106V#007F知道了……\n',
            '也许这也是为了她好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050081107V#053F真是的……\n',
            '又浪费了这么多时间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_6F42')
    def lambda_6F42():
        CameraMove(3150, 0, -410, 1000)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_6F42)

    ChrTurnDirection(0x0106, 0x0008, 400)

    @scena.Lambda('lambda_6F61')
    def lambda_6F61():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_6F61)

    Sleep(50)

    @scena.Lambda('lambda_6F74')
    def lambda_6F74():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_6F74)

    WaitForThreadExit(0x0009, 0x0002)

    ChrTalk(
        0x0106,
        (
            '#0050081108V#054F雾香。\n',
            '和军队的联络就麻烦你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0580081109V#790F嗯嗯。\n',
            '祝你们成功。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0150081110V#131F#2P哎呀哎呀……\n',
            '看来发生了不得了的大事呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150081111V请各位务必小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    ChrSetPos(0x0101, 1570, 0, -3490, 180)
    ChrSetPos(0x0102, 1570, 0, -3490, 180)
    ChrSetPos(0x0106, 1570, 0, -3490, 180)
    CameraMove(1570, 0, -3490, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_4B(0x0008, 255)
    OP_4B(0x0009, 255)
    ChrSetDirection(0x0009, 0, 400)
    Sleep(500)

    FadeIn(1000, 0)
    ChrSetPos(0x0107, 720, 0, -2310, 0)
    OP_28(0x0041, 0x01, 0x0100)
    OP_28(0x0041, 0x01, 0x0200)
    FormationDelMember(0x06, 0xFF)
    EventEnd(0x00)

    Return()

# id: 0x0016 offset: 0x70FB
@scena.Code('func_16_70FB')
def func_16_70FB():
    MapClearFlags(0x10000000)
    EventBegin(0x00)
    CameraMove(2000, 0, -5200, 0)
    OP_4A(0x0008, 255)
    OP_4A(0x000A, 0)
    ChrSetFlags(0x000A, 0x0040)
    ChrSetPos(0x000A, 1440, 0, -6280, 0)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetPos(0x0101, 2400, 0, -5400, 0)
    ChrSetPos(0x0102, 1300, 0, -5500, 0)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010090047V#001F雾香姐，早啊～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020090048V#010F早上好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_71AE')
    def lambda_71AE():
        CameraMove(3600, 0, 600, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_71AE)

    @scena.Lambda('lambda_71C6')
    def lambda_71C6():
        ChrWalkTo(0x00FE, 3800, 0, -700, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_71C6)

    Sleep(300)

    @scena.Lambda('lambda_71E6')
    def lambda_71E6():
        ChrWalkTo(0x00FE, 3000, 0, -700, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_71E6)

    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0008,
        (
            '#0580090049V#790F早啊，你们俩。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580090050V金已经出发了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020090051V#010F是的。\n',
            '刚才乘定期船飞去王都了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010090052V#000F说起来，\n',
            '雾香姐怎么没一起送行啊？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010090053V还有还有……\n',
            '雾香姐是怎么和金先生认识的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0580090054V#792F都是些陈年往事了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580090055V#790F别说这些了……\n',
            '事情好像变得迷雾重重了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010090056V#507F啊～雾香姐害羞了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010090057V#004F对了，迷雾重重是指……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020090058V#012F难道说……\n',
            '已经查到了那艘飞艇的线索？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0580090059V#790F不，目前还没有消息。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580090060V迷雾重重是指王国军最近的动向。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580090061V首先，\n',
            '我联络过雷斯顿要塞的军方司令部，\n',
            '但至今仍未得到任何的回音。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580090062V接着，\n',
            '设在各地的盘查在昨晚撤除了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010090063V#009F咦！？\n',
            '这是怎么回事？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010090064V他们又打算像空贼事件时那样\n',
            '和我们游击士协会抢功吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020090065V#013F不，那样的话，\n',
            '解除盘查岂不适得其反。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020090066V如果他们自己抓到了犯人，\n',
            '应该会马上联络这里的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020090067V#012F的确是迷雾重重啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0580090068V#792F而且最近这段时间，\n',
            '我和雷斯顿要塞的情报部也联络不上。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580090069V说不定王国军的内部\n',
            '发生了什么不可告人的大事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010090070V#002F什么事……\n',
            '#004F啊，难道是……！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010090071V朵洛希拍到的……那个！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020090072V#012F嗯……\n',
            '换装成亲卫队的黑衣人的照片。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x000A, 1440, 0, -6280, 0)
    ChrClearFlags(0x000A, 0x0040)
    ChrClearFlags(0x000A, 0x0080)
    PlaySE(6, 0x00, 0x64)

    ChrTalk(
        0x000A,
        (
            '#0280090073V#2P在说我吗～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_7762')
    def lambda_7762():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_7762)

    @scena.Lambda('lambda_7770')
    def lambda_7770():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_7770)

    CameraMove(2680, 0, -3240, 1500)

    ChrTalk(
        0x0101,
        (
            '#0010090074V#501F啊，朵洛希！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020090075V#010F真是说人人到啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_77D9')
    def lambda_77D9():
        CameraMove(3300, 0, -730, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_77D9)

    @scena.Lambda('lambda_77F1')
    def lambda_77F1():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_77F1')

    DispatchAsync2(0x0008, 0x0001, lambda_77F1)

    @scena.Lambda('lambda_7802')
    def lambda_7802():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_7802')

    DispatchAsync2(0x0101, 0x0001, lambda_7802)

    @scena.Lambda('lambda_7813')
    def lambda_7813():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_7813')

    DispatchAsync2(0x0102, 0x0001, lambda_7813)

    ChrWalkTo(0x000A, 3790, 0, -2310, 3000, 0x00)
    ChrTurnDirection(0x000A, 0x0101, 400)

    ChrTalk(
        0x000A,
        (
            '#0280090076V#152F哎呀～这次糟了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280090077V之前我联络编辑部的时候，\n',
            '正好碰上了奈尔前辈。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280090078V他知道我把那东西交给他们之后，\n',
            '就不由分说地对我大发脾气。\n',
            '还叫我无论如何都要把东西要回来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280090079V他们真的好过分呢～你们说是吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010090080V#004F你的意思是说……\n',
            '王国军还没把感光结晶回路还给你吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0280090081V#154F嗯，你们也觉得过分吧～？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280090082V他们就是不还给我，\n',
            '所以我就特地跑到要塞去要呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010090083V#506F哇哈～\n',
            '你还真有毅力啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0280090084V#151F嘿嘿～\n',
            '我也就只有这个优点嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280090085V实在没办法之下，\n',
            '我唯有拍了些要塞的照片给杂志充数。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280090086V嘿嘿～用探照灯打光，\n',
            '拍出来的照片可是十分可爱的哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010090087V#509F把要塞拍得十分可爱做什么用？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020090088V#014F没得到许可就随便拍摄军事设施，\n',
            '这样是不是不太好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0280090089V#151F没事没事。\n',
            '别说那么死板的话嘛㈱',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280090090V给，看啦看啦。\n',
            '照片刚刚才洗出来的哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_7BEA')
    def lambda_7BEA():
        CameraMove(3600, 0, 600, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_7BEA)

    ChrWalkTo(0x000A, 4640, 0, -1200, 2000, 0x00)
    ChrWalkTo(0x000A, 4660, 0, -710, 2000, 0x00)
    ChrSetDirection(0x0101, 45, 0)
    Sleep(500)

    ChrSetDirection(0x0101, 45, 0)
    ChrSetDirection(0x0102, 45, 0)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '朵洛希把雷斯顿要塞的照片放在柜台上。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_AD('ED6_DT04/C_VIS017._CH', 0x0000, 0x0000, 0x000001F4)
    Sleep(1500)

    SetMessageWindowPos(75, 250, -1, -1)
    TalkSetChrName('约修亚')

    Talk(
        (
            '#0020090091V#010F哦……\n',
            '拍得的确很漂亮啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020090092V#010F这就是雷斯顿要塞吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(150, 300, -1, -1)
    TalkSetChrName('艾丝蒂尔')

    Talk(
        (
            '#0010090093V#006F朵洛希真的很会拍照……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010090094V#004F………………咦咦………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(75, 250, -1, -1)
    TalkSetChrName('约修亚')

    Talk(
        (
            '#0020090095V#014F怎么了，艾丝蒂尔？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(150, 300, -1, -1)
    TalkSetChrName('艾丝蒂尔')

    Talk(
        (
            '#0010090096V#505F是心理作用吗……\n',
            '右上方好像有什么东西……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(75, 250, -1, -1)
    TalkSetChrName('约修亚')

    Talk(
        (
            '#0020090097V#014F咦……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020090098V#012F…………真的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(400, 250, -1, -1)
    TalkSetChrName('雾香')

    Talk(
        (
            '#0580090099V#790F虽然很模糊，\n',
            '但还真的有个很小的影子呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(300, 300, -1, -1)
    TalkSetChrName('朵洛希')

    Talk(
        (
            '#0280090100V#153F哎～\n',
            '艾丝蒂尔看得好仔细啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280090101V#153F我呢我呢，\n',
            '拍的时候一点都没发觉呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(150, 400, -1, -1)
    TalkSetChrName('艾丝蒂尔')

    Talk(
        (
            '#0010090102V#502F嘿嘿，多谢夸奖⊙',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010090103V#000F虽然只看到轮廓，\n',
            '不过应该是军队的警备飞艇吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(75, 250, -1, -1)
    TalkSetChrName('约修亚')

    Talk(
        (
            '#0020090104V#012F不……\n',
            '这不是警备飞艇……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020090105V#012F是那时候的飞艇。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(150, 400, -1, -1)
    TalkSetChrName('艾丝蒂尔')

    Talk(
        (
            '#0010090106V#004F那时候……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(300, 250, -1, -1)
    TalkSetChrName('雾香')

    Talk(
        (
            '#0580090107V#792F和黑衣人绑架博士时乘的飞艇\n',
            '是一模一样的轮廓吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(75, 250, -1, -1)
    TalkSetChrName('约修亚')

    Talk(
        (
            '#0020090108V#013F是的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_20(0x000005DC)
    SetMessageWindowPos(150, 400, -1, -1)
    TalkSetChrName('艾丝蒂尔')

    Talk(
        (
            '#0010090109V#505F绑架博士时乘的飞艇……\n',
            '……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    PlayBGM(86)
    SetMessageWindowPos(150, 400, -1, -1)

    Talk(
        (
            '#0010090110V#004F#5S咦咦咦咦咦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    TerminateThread(0x0008, 0xFF)
    ChrSetDirection(0x0008, 180, 0)
    ChrSetDirection(0x000A, 270, 0)
    ChrTurnDirection(0x0101, 0x0102, 0)
    OP_AE(0x000001F4)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010090111V#005F等、等一下！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010090112V为什么那艘飞艇会出现在这种地方！？\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010090113V太不可思议了！\n',
            '这里可是王国军的根据地啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020090114V#015F冷静点，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020090115V虽然有各种可能的情况，\n',
            '但现在就下结论的话还是太早了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020090116V#012F依现在的情况，\n',
            '我们应该直接前往雷斯顿要塞，\n',
            '当面询问他们飞艇的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010090117V#004F哎！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0580090118V#792F原来如此，\n',
            '打算去试探一下吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_8325')
    def lambda_8325():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_8325)

    ChrTurnDirection(0x0102, 0x0008, 400)

    ChrTalk(
        0x0102,
        (
            '#0020090119V#012F这样做不行吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0580090120V#790F不会，我许可。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580090121V不管怎样，\n',
            '我们这里可是差点有人丧命。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580090122V无论有什么原因，\n',
            '都不能让王国军的人看不起。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010090123V#007F呜哇，雾香姐，\n',
            '眼神突然变得凌厉了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010090124V#002F不过……确实是这样呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_8455')
    def lambda_8455():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_8455)

    ChrTurnDirection(0x0101, 0x000A, 400)

    ChrTalk(
        0x0101,
        (
            '#0010090125V#002F朵洛希，\n',
            '这照片能给我们一张吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0280090126V#150F嗯，没问题～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280090127V嘿嘿～毕竟我一直都\n',
            '受过小艾你们不少的关照嘛～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010090128V#006F谢谢，欠你个人情了！',
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
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '朵洛希拍的照片',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    AddItem(0x0358, 1)

    ChrTalk(
        0x0008,
        (
            '#0580090129V#790F要去雷斯顿要塞的话，\n',
            '首先从东面的门口出到利塔街道。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580090130V#790F然后在利塔街道途中的三岔路向北走，\n',
            '这样你们就能到达雷斯顿要塞了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580090131V请务必谨慎行动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_8638')
    def lambda_8638():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_8638)

    ChrTurnDirection(0x0101, 0x0008, 400)

    ChrTalk(
        0x0101,
        (
            '#0010090132V#006FＯＫ！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020090133V#010F明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0043, 0x04, 0x02)
    OP_28(0x0043, 0x04, 0x04)
    OP_28(0x0043, 0x01, 0x0001)
    OP_28(0x0033, 0x04, 0x40)
    OP_4B(0x000A, 0)
    CreateThread(0x0008, 0x00, 0x00, func_02_974)
    OP_20(0x000003E8)
    EventEnd(0x00)
    PlayBGM(13)

    Return()

# id: 0x0017 offset: 0x86AD
@scena.Code('func_17_86AD')
def func_17_86AD():
    EventBegin(0x00)
    CameraMove(3230, 0, 280, 0)
    FormationAddMember(0x06, 0xFF)
    FormationAddMember(0x05, 0xFF)
    ChrClearFlags(0x000B, 0x0080)
    ChrSetPos(0x000B, 4500, 0, -720, 270)
    ChrSetPos(0x0101, 3500, 0, -710, 90)
    ChrSetPos(0x0102, 2390, 0, -700, 90)
    ChrSetPos(0x0106, 1750, 0, -6420, 0)
    ChrSetPos(0x0107, 680, 0, -6020, 0)
    OP_4A(0x0008, 255)
    FadeIn(2000, 0)
    OP_0D()

    ChrTalk(
        0x000B,
        (
            '#0550090300V#805F拉、拉赛尔博士\n',
            '被囚禁在雷斯顿要塞里……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550090301V你们真的肯定吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0580090302V#790F朵洛希小姐拍的照片\n',
            '和大门前发生的导力停止现象。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580090303V将以上两者联系起来，\n',
            '这样的判断应该没错的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0550090304V#805F但、但是中央工房和王国军\n',
            '有着多年的友好合作关系。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550090305V实在无法接受他们会做出如此……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020090306V#012F虽说王国军都听令于女王，\n',
            '但也难保其内部一定坚如磐石。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020090307V袭击工房的犯人逃走时\n',
            '故意换装成王室亲卫队的样子，\n',
            '很有可能是出于某种政治上的目的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_892F')
    def lambda_892F():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_892F)

    @scena.Lambda('lambda_893D')
    def lambda_893D():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_893D)

    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010090308V#505F哎，你的意思是……',
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
            TXT(0x00, '「亲卫队和这些事件无关吗？」\n'),
            TXT(0x01, '「还是说亲卫队就是幕后主谋？」\n'),
            TXT(0x02, '「亲卫队是被别人栽赃的？」\n'),
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
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_8A21'),
        (0x00000001, 'loc_8B20'),
        (0x00000002, 'loc_8C15'),
        (-1, 'loc_8CE0'),
    )

    def _loc_8A21(): pass

    label('loc_8A21')

    ChrTalk(
        0x0101,
        (
            '#0010090309V#004F亲卫队和这些事件无关吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020090310V#012F嗯，就是这样。\n',
            '我认为他们和事件没有任何关系。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020090311V从犯人的犯案手法来看，\n',
            '亲卫队极有可能是被别人栽赃的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020090312V如果我没猜错的话……\n',
            '军队内部有什么阴谋正在进行着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_2B(0x0043, 0x0001)

    Jump('loc_8CE0')

    def _loc_8B20(): pass

    label('loc_8B20')

    ChrTalk(
        0x0101,
        (
            '#0010090313V#004F还是说亲卫队就是幕后主谋？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020090314V#017F唔……\n',
            '不排除有幕后主谋的可能性。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020090315V#012F不过幕后主谋另有其人，\n',
            '亲卫队极有可能是被别人栽赃的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020090316V如果我没猜错的话……\n',
            '军队内部有什么阴谋正在进行着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8CE0')

    def _loc_8C15(): pass

    label('loc_8C15')

    ChrTalk(
        0x0101,
        (
            '#0010090317V#004F难道说……\n',
            '亲卫队是被别人栽赃的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020090318V#012F嗯，我的想法和你一样。\n',
            '幕后主谋根本不是王室亲卫队。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020090319V如果我没猜错的话……\n',
            '军队内部有什么阴谋正在进行着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_2B(0x0043, 0x0003)

    Jump('loc_8CE0')

    def _loc_8CE0(): pass

    label('loc_8CE0')

    ChrTalk(
        0x000B,
        (
            '#0550090320V#806F唔……是这样吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550090321V但是，为什么他们\n',
            '会把博士也卷进这个阴谋里呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(6, 0x00, 0x64)
    Sleep(100)

    ChrTalk(
        0x0106,
        (
            '#0050090322V#2P……看来你们找到了\n',
            '绑架博士的那帮犯人的线索吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(500)

    PlaySE(7, 0x00, 0x64)
    Sleep(500)

    @scena.Lambda('lambda_8DD7')
    def lambda_8DD7():
        ChrTurnDirection(0x00FE, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_8DD7)

    @scena.Lambda('lambda_8DE5')
    def lambda_8DE5():
        ChrTurnDirection(0x00FE, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_8DE5)

    @scena.Lambda('lambda_8DF3')
    def lambda_8DF3():
        ChrTurnDirection(0x00FE, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_8DF3)

    @scena.Lambda('lambda_8E01')
    def lambda_8E01():
        ChrTurnDirection(0x00FE, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_8E01)

    @scena.Lambda('lambda_8E0F')
    def lambda_8E0F():
        CameraMove(2020, 0, -2230, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_8E0F)

    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010090323V#501F哎，阿加特！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020090324V#010F太好了……\n',
            '阿加特兄你总算醒来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_8E89')
    def lambda_8E89():
        CameraMove(2920, 0, -480, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_8E89)

    @scena.Lambda('lambda_8EA1')
    def lambda_8EA1():
        ChrTurnDirection(0x00FE, 0x0106, 0)
        Yield()

        Jump('lambda_8EA1')

    DispatchAsync2(0x000B, 0x0001, lambda_8EA1)

    @scena.Lambda('lambda_8EB2')
    def lambda_8EB2():
        ChrTurnDirection(0x00FE, 0x0106, 0)
        Yield()

        Jump('lambda_8EB2')

    DispatchAsync2(0x0101, 0x0001, lambda_8EB2)

    @scena.Lambda('lambda_8EC3')
    def lambda_8EC3():
        ChrTurnDirection(0x00FE, 0x0106, 0)
        Yield()

        Jump('lambda_8EC3')

    DispatchAsync2(0x0102, 0x0001, lambda_8EC3)

    @scena.Lambda('lambda_8ED4')
    def lambda_8ED4():
        ChrWalkTo(0x00FE, 3540, 0, -1870, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_8ED4)

    Sleep(300)

    @scena.Lambda('lambda_8EF4')
    def lambda_8EF4():
        ChrWalkTo(0x00FE, 2440, 0, -1760, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_8EF4)

    WaitForThreadExit(0x0106, 0x0001)
    ChrTurnDirection(0x0106, 0x0101, 400)
    WaitForThreadExit(0x0107, 0x0001)
    ChrTurnDirection(0x0107, 0x0102, 400)

    ChrTalk(
        0x0106,
        (
            '#0050090325V#552F啊，刚刚才醒。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050090326V起来后发现睡在不认识的地方，\n',
            '真是吓了一跳。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010090327V#008F#2P真是的……\n',
            '这两天大家都很担心你啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020090328V#010F不过才刚刚醒来，\n',
            '这样到处走动不会有问题吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050090329V#051F哈哈，\n',
            '睡多了身体反而变得僵硬。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050090330V还是要尽情地运动才会健康嘛。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0107, 0x0106, 400)

    ChrTalk(
        0x0107,
        (
            '#0070090331V#065F#1P但、但是，阿加特大哥哥。\n',
            '太勉强的话是不行的哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070090332V身上的毒才刚刚清除，\n',
            '医生说要再静养一段时间……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0106, 0x0107, 400)

    ChrTalk(
        0x0106,
        (
            '#0050090333V#551F好啦好啦。\n',
            '我不是都说了没事嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050090334V我可是和你们不一样，知道吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070090335V#069F#1P呜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0106, 0x00000000, 2000, 0x14, 0x17, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0106,
        (
            '#0050090336V#055F哎呀……\n',
            '知道了，知道了啦！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050090337V反正在伤势康复之前不会乱来，\n',
            '这样总成了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070090338V#067F#1P嘿嘿……好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050090339V#552F真是的……\n',
            '所以我就说小鬼是最……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010090340V#001F#2P啊哈哈。\n',
            '连阿加特也拿提妲没办法了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020090341V#019F因为受伤的时候是提妲一直在照顾着，\n',
            '既然阿加特兄受了人家的恩惠，\n',
            '那么以后说话不客气也不行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0106, 0x0101, 400)

    ChrTalk(
        0x0106,
        (
            '#0050090342V#551F啊～够了，真啰嗦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050090343V#051F不过在我休息的时候，\n',
            '绑架事件有了很多新的进展吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050090344V说给我听听吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010090345V#006F#2P嗯，好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0107, 0x0101, 400)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔他们告诉阿加特\n',
            '拉赛尔博士很有可能被捉到雷斯顿要塞的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x0107,
        (
            '#0070090346V#065F爷、爷爷他竟然\n',
            '被那些坏人捉到那里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050090347V#552F那些黑衣人竟然和军队有关系……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050090348V#053F哼……\n',
            '总算弄清他们的真面目了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050090349V看来事情也该做个了结了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010090350V#002F#2P做个了结？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050090351V#057F这还用我说吗。\n',
            '潜入雷斯顿要塞将事情解决掉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050090352V不仅要救出博士，\n',
            '还要把那些家伙一网打尽。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010090353V#006F#2P啊，原来是这样啊。\n',
            '看来这是最直截了当的方法呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0580090354V#790F没那么简单。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_9611')
    def lambda_9611():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_9611)

    @scena.Lambda('lambda_961F')
    def lambda_961F():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_961F)

    @scena.Lambda('lambda_962D')
    def lambda_962D():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_962D)

    @scena.Lambda('lambda_963B')
    def lambda_963B():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_963B)

    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010090355V#004F哎？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0580090356V#792F游击士协会的规约里有一条\n',
            '决不干涉各国军队内政的原则。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580090357V协会规约第三项。\n',
            '『不对国家主权进行干涉』……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580090358V『游击士不可对\n',
            '　国家授权或认可的公共机关\n',
            '　行使任何的搜查权及逮捕权。』',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580090359V#790F就是说，只要军队不认帐，\n',
            '我们就没有权力对其进行调查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050090360V#552F嘁，忘了还有这个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010090361V#005F怎、怎么会……\n',
            '这样太不合理了吧！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010090362V明明看到他们做了那么多坏事，\n',
            '难道就这样放过吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0580090363V#791F不过……\n',
            '这个规约也有空子可钻。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580090364V协会规约第二项。\n',
            '『对于平民有保护义务』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580090365V『当在平民的生命及权利\n',
            '　受到不正当威胁或侵犯的情况下，\n',
            '　游击士有保护他们的义务和责任。』',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580090366V#792F明白这是什么意思了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020090367V#010F原来如此……\n',
            '博士既不是佣兵也不是军人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020090368V只是一个受保护的平民。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010090369V#501F这、这么说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0580090370V#790F接下来……\n',
            '就要看工房长先生您了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580090371V这件事很可能\n',
            '引发中央工房与王国军的对立，\n',
            '即使这样，也要救出拉赛尔博士吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_9A45')
    def lambda_9A45():
        ChrTurnDirection(0x00FE, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_9A45)

    @scena.Lambda('lambda_9A53')
    def lambda_9A53():
        ChrTurnDirection(0x00FE, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_9A53)

    @scena.Lambda('lambda_9A61')
    def lambda_9A61():
        ChrTurnDirection(0x00FE, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_9A61)

    ChrTurnDirection(0x0107, 0x000B, 400)

    ChrTalk(
        0x000B,
        (
            '#0550090372V#803F……这根本不用考虑。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550090373V博士对于中央工房……\n',
            '不，对于整个利贝尔来说\n',
            '是个百年难得一遇的优秀人才。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550090374V#800F我在此委托你们营救他。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070090375V#560F#1P工房长叔叔……！\n',
            '真、真是太感谢您了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000B, 0x0107, 400)

    ChrTalk(
        0x000B,
        (
            '#0550090376V#801F不用道什么谢啦。\n',
            '博士也是我的恩师啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0580090377V#792F这样我们就有合适的理由了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580090378V游击士阿加特，\n',
            '还有艾丝蒂尔和约修亚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_9C06')
    def lambda_9C06():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_9C06)

    @scena.Lambda('lambda_9C14')
    def lambda_9C14():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_9C14)

    @scena.Lambda('lambda_9C22')
    def lambda_9C22():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_9C22)

    @scena.Lambda('lambda_9C30')
    def lambda_9C30():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_9C30)

    @scena.Lambda('lambda_9C3E')
    def lambda_9C3E():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_9C3E)

    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0580090379V#791F现委托你们前往营救\n',
            '被捉到雷斯顿要塞的拉赛尔博士。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580090380V虽然程序不是很正规，\n',
            '但这是游击士协会的正式委托。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010090381V#508F这样才对嘛！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020090382V#010F明白。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050090383V#051F哼，正合我意。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050090384V既然决定了，\n',
            '就有必要策划一下潜入方法。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050090385V不管怎样，雷斯顿要塞\n',
            '毕竟是个以无坚不摧而著称的基地。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020090386V#012F的确如此。\n',
            '那里的警戒体制相当严密。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020090387V如果有可行的潜入路线图就好了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0580090388V#792F很遗憾……\n',
            '那里的警戒体制可以说是接近完美。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580090389V要塞周围散布了导力传感器，\n',
            '就算从湖的方向潜入也相当困难。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050090390V#552F哼……\n',
            '我就知道没那么容易了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020090391V#012F正面突破很难成功啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x22, 0x24, 0x000000FA, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x0101, 0x000B, 400)

    ChrTalk(
        0x0101,
        (
            '#0010090392V#501F#2P说起来，工房长先生。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010090393V那艘橙色的飞艇\n',
            '不是去过雷斯顿要塞吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_9F90')
    def lambda_9F90():
        ChrTurnDirection(0x00FE, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_9F90)

    @scena.Lambda('lambda_9F9E')
    def lambda_9F9E():
        ChrTurnDirection(0x00FE, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_9F9E)

    @scena.Lambda('lambda_9FAC')
    def lambda_9FAC():
        ChrTurnDirection(0x00FE, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_9FAC)

    ChrTurnDirection(0x000B, 0x0101, 400)

    ChrTalk(
        0x000B,
        (
            '#0550090394V#802F啊啊……\n',
            '你说工房船『莱普尼兹号』吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550090395V我们的确是要定期向要塞\n',
            '运送材料和检查设备……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010090396V#006F#2P那么那么，\n',
            '我们藏在里面潜入要塞不就行了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0550090397V#805F不可能，飞艇一降落到基地，\n',
            '机上的所有人员都要接受严密的检查。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550090398V想任意行动几乎不可能……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050090399V#050F难道说……\n',
            '躲在货物里也行不通？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0550090400V#800F嗯，他们会用生命感应器\n',
            '逐一检查运来的所有箱子。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550090401V那个生命感应器也是\n',
            '拉赛尔博士发明的东西。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550090402V是连一只老鼠也不会放过的先进机器啊。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010090403V#007F#2P唉～还是不行啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0107, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0107,
        (
            '#0070090404V#064F……啊…………！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_A251')
    def lambda_A251():
        ChrTurnDirection(0x00FE, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_A251)

    @scena.Lambda('lambda_A25F')
    def lambda_A25F():
        ChrTurnDirection(0x00FE, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_A25F)

    @scena.Lambda('lambda_A26D')
    def lambda_A26D():
        ChrTurnDirection(0x00FE, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_A26D)

    ChrTalk(
        0x0101,
        (
            '#0010090405V#002F#2P咦，怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070090406V#560F艾丝蒂尔姐姐，你还记得吗！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070090407V那天姐姐你们来我家时\n',
            '爷爷刚做好的那个新发明啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010090408V#505F#2P我们来你家的时候……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010090409V#004F……啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020090410V#010F我想起来了……\n',
            '是我们也帮忙做实验的那个导力器？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070090411V#061F嗯，就是那个！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070090412V那个装置能产生\n',
            '阻碍生命感应器扫描的导力场。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070090413V启动测试也做过了。\n',
            '没问题的……肯定可以帮上忙的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050090414V#054F什么……真的吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0550090415V#803F那个博士也真是的，\n',
            '什么时候做了这种东西……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550090416V#800F那个装置现在在哪里？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070090417V#560F啊，我想应该是\n',
            '放在研究室的某个地方了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0580090418V#791F那么你们快去把那个装置取来。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580090419V我会在这段时间里准备好\n',
            '有关雷斯顿要塞的详细资料。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0106, 0x0008, 400)

    ChrTalk(
        0x0106,
        (
            '#0050090420V#051F好的，拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0580090421V#791F工房长先生，\n',
            '工房船的准备就拜托您了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000B, 0x0008, 400)

    ChrTalk(
        0x000B,
        (
            '#0550090422V#804F明、明白了。\n',
            '我马上和格斯塔夫维修长商量。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550090423V你们准备完了就到飞艇坪来吧！\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0043, 0x01, 0x0020)
    OP_28(0x0043, 0x01, 0x0040)

    @scena.Lambda('lambda_A66D')
    def lambda_A66D():
        ChrTurnDirection(0x00FE, 0x000B, 400)
        Yield()

        Jump('lambda_A66D')

    DispatchAsync2(0x0101, 0x0001, lambda_A66D)

    @scena.Lambda('lambda_A67E')
    def lambda_A67E():
        ChrTurnDirection(0x00FE, 0x000B, 400)
        Yield()

        Jump('lambda_A67E')

    DispatchAsync2(0x0102, 0x0001, lambda_A67E)

    @scena.Lambda('lambda_A68F')
    def lambda_A68F():
        ChrTurnDirection(0x00FE, 0x000B, 400)
        Yield()

        Jump('lambda_A68F')

    DispatchAsync2(0x0106, 0x0001, lambda_A68F)

    @scena.Lambda('lambda_A6A0')
    def lambda_A6A0():
        ChrTurnDirection(0x00FE, 0x000B, 400)
        Yield()

        Jump('lambda_A6A0')

    DispatchAsync2(0x0107, 0x0001, lambda_A6A0)

    ChrSetDirection(0x000B, 180, 400)
    ChrWalkTo(0x000B, 4430, 0, -2900, 4000, 0x00)
    ChrWalkTo(0x000B, 1630, 0, -6130, 4000, 0x00)
    PlaySE(6, 0x00, 0x64)

    @scena.Lambda('lambda_A6E5')
    def lambda_A6E5():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 500)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_A6E5)

    ChrWalkTo(0x000B, 1780, 0, -7750, 4000, 0x00)
    PlaySE(7, 0x00, 0x64)
    ChrSetFlags(0x000B, 0x0004)
    ChrWalkTo(0x000B, 1920, -500, -9290, 4000, 0x00)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0107, 0xFF)
    TerminateThread(0x0106, 0xFF)
    OP_4B(0x0008, 255)
    EventEnd(0x00)

    Return()

# id: 0x0018 offset: 0xA73A
@scena.Code('func_18_A73A')
def func_18_A73A():
    MapClearFlags(0x10000000)
    EventBegin(0x00)
    ChrSetPos(0x0101, 1520, 0, -4610, 0)
    ChrSetPos(0x0102, 2390, 0, -5240, 0)
    ChrSetPos(0x0106, 640, 0, -5220, 0)
    ChrSetPos(0x0107, 1640, 0, -5990, 0)
    OP_4A(0x0008, 255)
    CameraMove(2370, 0, -2250, 0)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010090439V#006F雾香姐。\n',
            '那个装置拿到了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_A7DA')
    def lambda_A7DA():
        CameraMove(3130, 0, 650, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_A7DA)

    @scena.Lambda('lambda_A7F2')
    def lambda_A7F2():
        ChrWalkTo(0x00FE, 3630, 0, -740, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_A7F2)

    Sleep(300)

    @scena.Lambda('lambda_A812')
    def lambda_A812():
        ChrWalkTo(0x00FE, 4170, 0, -1770, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_A812)

    Sleep(300)

    @scena.Lambda('lambda_A832')
    def lambda_A832():
        ChrWalkTo(0x00FE, 2820, 0, -1390, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0106, 0x0002, lambda_A832)

    Sleep(300)

    @scena.Lambda('lambda_A852')
    def lambda_A852():
        ChrWalkTo(0x00FE, 3120, 0, -2340, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0002, lambda_A852)

    @scena.Lambda('lambda_A86D')
    def lambda_A86D():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_A86D')

    DispatchAsync2(0x0101, 0x0001, lambda_A86D)

    @scena.Lambda('lambda_A87E')
    def lambda_A87E():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_A87E')

    DispatchAsync2(0x0102, 0x0001, lambda_A87E)

    @scena.Lambda('lambda_A88F')
    def lambda_A88F():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_A88F')

    DispatchAsync2(0x0107, 0x0001, lambda_A88F)

    @scena.Lambda('lambda_A8A0')
    def lambda_A8A0():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_A8A0')

    DispatchAsync2(0x0106, 0x0001, lambda_A8A0)

    WaitForThreadExit(0x0106, 0x0002)

    ChrTalk(
        0x0008,
        (
            '#0580090440V#790F我这里也准备好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580090441V顺带一提，\n',
            '这些资料绝对不能向他人外传。',
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
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '雷斯顿要塞概略图',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    AddItem(0x0359, 1)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0107, 0xFF)
    TerminateThread(0x0106, 0xFF)
    OP_AD('ED6_DT04/C_VIS018._CH', 0x0000, 0x0000, 0x000001F4)
    Sleep(1500)

    SetMessageWindowPos(75, 300, -1, -1)
    TalkSetChrName('阿加特')

    Talk(
        (
            '#0050090442V#051F哈哈……\n',
            '竟然有这么好的东西啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(150, 350, -1, -1)
    TalkSetChrName('约修亚')

    Talk(
        (
            '#0020090443V#014F这个是……\n',
            '雷斯顿要塞的简略图吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(300, 350, -1, -1)
    TalkSetChrName('提妲')

    Talk(
        (
            '#0070090444V#064F哇……\n',
            '好大好厉害啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070090445V#062F爷爷会在哪儿呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(400, 400, -1, -1)
    TalkSetChrName('艾丝蒂尔')

    Talk(
        (
            '#0010090446V#509F我说……\n',
            '这东西不是军事机密吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010090447V为什么协会会有这张地图？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(400, 0, -1, -1)
    TalkSetChrName('雾香')

    Talk(
        (
            '#0580090448V#792F正所谓蛇行蛇道。\n',
            '任何组织都会有其独特的门路。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580090449V#790F你们只要记住，\n',
            '游击士协会也有这样一面就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(400, 400, -1, -1)
    TalkSetChrName('艾丝蒂尔')

    Talk(
        (
            '#0010090450V#004F嗯、嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_AE(0x000001F4)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0580090451V#790F不必我多说，\n',
            '大家也知道这次情况相当特殊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580090452V与其他国家相比起来，\n',
            '王国军和协会一向保持着良好的关系。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580090453V为了不留下任何瑕疵，\n',
            '记住要尽量避免和士兵交战。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580090454V特别是阿加特……明白吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050090455V#053F哼，真没办法。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050090456V#057F不过，要是那帮黑衣人来碍事的话，\n',
            '我肯定决不会手软。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050090457V管他们是军人还是什么，\n',
            '总之干了坏事就是犯罪者。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0580090458V#790F那些就随你便吧。\n',
            '不过切记不能太过硬来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580090459V#792F艾丝蒂尔、约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580090460V本来按道理是不能安排\n',
            '你们准游击士做这种任务的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010090461V#005F等、等一下！\n',
            '游击士的地位和那无关吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020090462V#012F既然走到了这一步，\n',
            '就请让我们继续做下去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0580090463V#791F……就知道你们会这么说，\n',
            '所以我也不会阻拦你们了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580090464V顺带一提，\n',
            '你们是在蔡斯支部的监督之下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580090465V有什么责任就由我来承担，\n',
            '所以你们尽管放心好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010090466V#003F雾、雾香姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020090467V#015F不好意思……\n',
            '这次真的给您添麻烦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0580090468V#790F还有……提妲。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580090469V你并非游击士，\n',
            '其实本不该这么问你的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580090470V你真的下定决心了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070090471V#064F啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070090472V#062F……是！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_B041')
    def lambda_B041():
        ChrTurnDirection(0x00FE, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_B041)

    @scena.Lambda('lambda_B04F')
    def lambda_B04F():
        ChrTurnDirection(0x00FE, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_B04F)

    @scena.Lambda('lambda_B05D')
    def lambda_B05D():
        ChrTurnDirection(0x00FE, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_B05D)

    CameraMove(3240, 0, -550, 1000)

    ChrTalk(
        0x0101,
        (
            '#0010090473V#004F#2P咦、咦？\n',
            '这是怎么回事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020090474V#014F难道说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070090475V#063F那、那个……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070090476V能够操作这个感应干扰器的人\n',
            '也许只有我一个。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070090477V所以……\n',
            '我也要和姐姐你们一起去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010090478V#004F#2P咦咦！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020090479V#012F如此构造复杂的导力器，\n',
            '凭我们的确是无法正确使用……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070090480V#562F对不起……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070090481V我、我一定不会\n',
            '再给姐姐你们添麻烦的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050090482V#552F#5P……开什么玩笑。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_B245')
    def lambda_B245():
        ChrTurnDirection(0x00FE, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_B245)

    @scena.Lambda('lambda_B253')
    def lambda_B253():
        ChrTurnDirection(0x00FE, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_B253)

    ChrTurnDirection(0x0107, 0x0106, 400)
    Sleep(400)

    ChrTalk(
        0x0106,
        (
            '#0050090483V#057F#5P喂，小不点……\n',
            '我可没听说过这种事……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050090484V这么危险的任务，\n',
            '怎可能带你这种小鬼去啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070090485V#065F但、但是但是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070090486V如果我不去的话，\n',
            '这个装置就运作不了的呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050090487V#054F#5P那就不用这种方法好了！\n',
            '不用了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050090488V我们找别的潜入方法！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010090489V#002F#2P…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010090490V#007F我说阿加特啊，\n',
            '你就不会稍微变通一下吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010090491V怎么老是那么意气用事啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0106, 0x0102, 400)

    ChrTalk(
        0x0106,
        (
            '#0050090492V#055F#5P什么……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010090493V#009F#2P提妲她可是已经有所觉悟，\n',
            '才会说要帮我们的啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010090494V有了她的帮忙，\n',
            '我们的潜入行动也会容易许多。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010090495V而且救出博士的成功率\n',
            '也肯定会高很多对吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010090496V既然这样的话，\n',
            '你还有什么理由去反对呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050090497V#057F#5P你……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050090498V你打算让一个平民置身险境吗？\n',
            '要知道她还是个小孩子！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010090499V#006F#2P我也不想让她有危险，\n',
            '但我们可以好好地保护她啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010090500V而且这也是游击士的义务。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050090501V#552F#5P哼……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050090502V明明还是个经验浅薄的新人，\n',
            '还敢摆出这么一副老练的样子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020090503V#015F……我们的确是新人，\n',
            '但我认为这和辈分没什么关系。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020090504V保护身边重要的人这种心情，\n',
            '也并非游击士所专有的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020090505V#010F倒不如说，\n',
            '这种心情才正是我们工作的动力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050090506V#057F#5P……………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0107, 0x0101, 400)

    ChrTalk(
        0x0107,
        (
            '#0070090507V#065F艾丝蒂尔姐姐、约修亚哥哥……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070090508V#562F还有阿加特大哥哥。\n',
            '对不起呢，大家为了我的事操心……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070090509V但是但是，\n',
            '爷爷对我来说真的很重要……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070090510V无论如何，我都想去救他……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070090511V所以呢……\n',
            '我真的很想尽自己所能来帮忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050090512V#552F#5P……………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070090513V#063F阿加特大哥哥昨天救了我……\n',
            '而且他还教导了我，鼓励了我……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070090514V所以呢，我也希望能为大家做点事情。\n',
            '我知道自己帮不上什么忙……\n',
            '但是，就算能帮上那么的一点点也好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070090515V我绝对不是在勉强自己……\n',
            '因为我知道自己现在的心情……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070090516V#068F所以……求求你们了……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010090517V#008F#2P提妲……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020090518V#010F是这样啊……\n',
            '你真是个会为人着想的好孩子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050090519V#053F#5P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0106, 0x0107, 400)

    ChrTalk(
        0x0106,
        (
            '#0050090520V#057F#5P哼，都不知道你在说什么。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050090521V要知道你自己是多么的碍事。\n',
            '叫你别跟来也是为了你好。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0107, 0x0106, 400)

    ChrTalk(
        0x0107,
        (
            '#0070090522V#562F呜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050090523V#552F#5P不过在没有其他潜入方法的情况下……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050090524V真没办法……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050090525V#053F既然如此，\n',
            '这次就破例允许你跟我们去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070090526V#560F啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070090527V#067F谢谢你，阿加特大哥哥！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050090528V#051F#5P不用道谢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050090529V要是你再碍事的话，\n',
            '我会毫不留情地丢下你不管哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050090530V做好心理准备吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070090531V#560F是、是！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010090532V#509F#2P真是的……\n',
            '老是装模作样地闹别扭。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010090533V就不会老老实实接受人家的心意吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020090534V#019F算了算了，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020090535V阿加特兄是为了隐藏心中的羞涩\n',
            '才会装得那么严肃嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0106, 0x0102, 400)

    ChrTalk(
        0x0106,
        (
            '#0050090536V#055F#5P吵、吵死了，你们两个家伙！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070090537V#067F嘻嘻……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_BDA6')
    def lambda_BDA6():
        CameraMove(3130, 0, 650, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_BDA6)

    WaitForThreadExit(0x0101, 0x0003)

    ChrTalk(
        0x0008,
        (
            '#0580090538V#792F呵呵……\n',
            '意见一致就没问题了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580090539V#791F工房船也差不多该安排好了。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580090540V你们准备好的话，\n',
            '可以随时动身前往飞艇坪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_BE5E')
    def lambda_BE5E():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_BE5E)

    @scena.Lambda('lambda_BE6C')
    def lambda_BE6C():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_BE6C)

    @scena.Lambda('lambda_BE7A')
    def lambda_BE7A():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_BE7A)

    ChrTurnDirection(0x0107, 0x0008, 400)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010090541V#006F嗯，明白！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050090542V#051F我们走了，雾香。\n',
            '军队那边就拜托你应对了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0580090543V#791F嗯，\n',
            '即使被质问我也会妥善应对的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580090544V愿女神保佑你们。\n',
            '请各位行事多加小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0043, 0x01, 0x0200)
    OP_4B(0x0008, 255)
    EventEnd(0x00)

    Return()

# id: 0x0019 offset: 0xBF67
@scena.Code('func_19_BF67')
def func_19_BF67():
    EventBegin(0x00)
    CameraMove(3310, 0, -200, 0)
    OP_67(0, 6580, -10000, 0)
    CameraSetDistance(3000, 0)
    ChrSetPos(0x0101, 2770, 0, -720, 0)
    ChrSetPos(0x0102, 4310, 0, -890, 0)
    ChrSetPos(0x000B, 3260, 0, -2080, 0)
    ChrClearFlags(0x000B, 0x0080)
    ChrTurnDirection(0x0101, 0x000B, 0)
    ChrTurnDirection(0x0102, 0x000B, 0)
    ChrTurnDirection(0x000B, 0x0008, 0)
    OP_4A(0x0008, 255)
    RemoveItem(0x035A, 1)
    RemoveItem(0x0362, 1)
    RemoveItem(0x0364, 1)
    FadeIn(2000, 0)
    OP_0D()
    ChrSetStatus(0x0000, 0xFE, 0)
    ChrSetStatus(0x0001, 0xFE, 0)
    ChrSetStatus(0x0002, 0xFE, 0)
    ChrSetStatus(0x0003, 0xFE, 0)
    ChrSetStatus(0x0004, 0xFE, 0)
    ChrSetStatus(0x0005, 0xFE, 0)
    ChrSetStatus(0x0006, 0xFE, 0)
    ChrSetStatus(0x0007, 0xFE, 0)

    ChrTalk(
        0x000B,
        (
            '#0550100107V#803F是吗……\n',
            '已经把博士平安地救出来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550100108V演算器也取了回来，\n',
            '我该怎么表达我的感激之情呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550100109V#800F谢谢你们。\n',
            '艾丝蒂尔、约修亚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100110V#506F嗯～\n',
            '我们也没有做什么啦……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100111V说到底……\n',
            '我们只是给阿加特帮了一点忙而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100112V#010F要感谢的话，\n',
            '请感谢保护博士他们的阿加特兄吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0550100113V#805F我当然也要感谢他。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550100114V希望他们最后都能够\n',
            '顺利平安地逃开军队的搜索……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0580100115V#792F现在也只能相信阿加特了。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580100116V#790F不过，理查德上校好像\n',
            '正打算在王都有所行动的样子。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580100117V用那个被称为『福音』的黑色导力器……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100118V#007F嗯……\n',
            '虽然不知道要用它来做什么。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100119V只要按照博士的委托，\n',
            '把这件事禀告给女王就行了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0550100120V#803F嗯……\n',
            '没想到会在这里听到陛下的名字。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550100121V#800F的确……\n',
            '博士与女王曾有过私人的来往。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550100122V他会知道一些关于\n',
            '王国的机密事情也不奇怪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0008, 400)

    ChrTalk(
        0x0102,
        (
            '#0020100123V#012F雾香小姐，关于这件事，\n',
            '虽然我们受到了博士的正式委托……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100124V#012F但在现在这样的情况下，\n',
            '我们能够直接前往王都吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_C44E')
    def lambda_C44E():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_C44E)

    ChrTalk(
        0x0008,
        (
            '#0580100125V#792F他们又没有掌握你们潜入要塞的证据，\n',
            '现在这个时期应该没有问题。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580100126V#790F不过你们须要尽快赶往王都。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580100127V还有的是……\n',
            '中央工房会有被检查的可能性。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0550100128V#806F没错……\n',
            '现在必须制定出对策才行。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550100129V#800F艾丝蒂尔、约修亚。\n',
            '出发后一定要多加小心。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550100130V博士的委托就靠你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_C5B2')
    def lambda_C5B2():
        ChrTurnDirection(0x00FE, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_C5B2)

    ChrTurnDirection(0x0101, 0x000B, 400)

    ChrTalk(
        0x0101,
        (
            '#0010100131V#006F嗯，交给我们吧！\n',
            '一定会如实传达给女王的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100132V#012F请工房长您也要小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0550100133V#801F嗯，我们绝对不会被\n',
            '情报部那些家伙抓住把柄的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550100134V那么，我告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000B, 225, 400)
    ChrWalkTo(0x000B, 1550, 0, -6250, 3000, 0x00)
    PlaySE(6, 0x00, 0x64)

    @scena.Lambda('lambda_C6B4')
    def lambda_C6B4():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 500)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_C6B4)

    ChrWalkTo(0x000B, 1680, 0, -8109, 2000, 0x00)
    ChrSetFlags(0x000B, 0x0080)
    Sleep(300)

    PlaySE(7, 0x00, 0x64)
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010100135V#006F接下来……\n',
            '我们必须赶快行动了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100136V一定要尽快见到女王才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020100137V#010F这样的话，\n',
            '我们这次最好改乘定期船。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100138V步行到王都要半天的时间，\n',
            '乘坐飞艇的话只要不到一个小时。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100139V#505F是吗，确实……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100140V本来想步行环游王国一周的，\n',
            '不过这也是没有办法的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0580100141V#790F这样的话，请稍等一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_C865')
    def lambda_C865():
        CameraMove(3570, 0, 620, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_C865)

    @scena.Lambda('lambda_C87D')
    def lambda_C87D():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_C87D)

    @scena.Lambda('lambda_C88B')
    def lambda_C88B():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_C88B)

    ChrWalkTo(0x0008, 5350, 0, 1220, 2000, 0x00)

    @scena.Lambda('lambda_C8AD')
    def lambda_C8AD():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_C8AD')

    DispatchAsync2(0x0101, 0x0001, lambda_C8AD)

    @scena.Lambda('lambda_C8BE')
    def lambda_C8BE():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_C8BE')

    DispatchAsync2(0x0102, 0x0001, lambda_C8BE)

    ChrWalkTo(0x0008, 5380, 0, 2500, 2000, 0x00)
    ChrSetDirection(0x0008, 270, 400)
    Sleep(400)

    PlaySE(131, 0x00, 0x64)
    LoadEffect(0x00, 'map\\\\mp001_01.eff')
    PlayEffect(0x00, 0x00, 0x00FF, 4840, 2000, 2560, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(600)

    OP_62(0x0008, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1200)

    OP_63(0x0008)

    ChrTalk(
        0x0008,
        (
            '#0580100142V#792F这里是游击士协会……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580100143V您好。\n',
            '总是承蒙您的照顾。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580100144V……嗯……拜托您了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580100145V两张到王都格兰赛尔的……\n',
            '嗯、嗯……和平时的要求一样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580100146V#791F那么就拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(300)

    PlaySE(131, 0x00, 0x64)
    StopEffect(0x00, 0x00)
    Sleep(300)

    ChrSetDirection(0x0008, 180, 400)
    ChrWalkTo(0x0008, 5040, 0, 1200, 2000, 0x00)
    ChrWalkTo(0x0008, 3500, 0, 1200, 2000, 0x00)
    ChrSetDirection(0x0008, 180, 400)

    ChrTalk(
        0x0101,
        (
            '#0010100147V#501F？？？\n',
            '怎么了，雾香姐？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100148V#010F难道是打给飞艇坪的接待处？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0580100149V#791F嗯，没错。\n',
            '我预订了两张到王都的定期船票。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580100150V费用由蔡斯支部支付，\n',
            '所以你们只需要去办理搭乘手续就可以了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580100151V还有，请收下这个。',
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
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '正游击士资格的推荐信',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    AddItem(0x033A, 1)

    ChrTalk(
        0x0101,
        (
            '#0010100152V#004F哎～～！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100153V#019F真、真是准备得很周到啊……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0580100154V#791F定期船票的支出是\n',
            '传话给女王这一任务的必要经费。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580100155V推荐信则是对你们两个\n',
            '完成救出博士这一重要工作的评价。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580100156V请不要谦虚，\n',
            '与这次的报酬一起收下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100157V#008F啊……嗯！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100158V谢谢，雾香姐！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0041, 0x04, 0x10)
    OP_28(0x0043, 0x04, 0x10)
    Sleep(100)

    OP_AF(0x40, 0x0041)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    Sleep(100)

    OP_AF(0x40, 0x0043)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    ChrTalk(
        0x0102,
        (
            '#0020100159V#010F真的是……\n',
            '太麻烦雾香小姐您了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0580100160V#792F呵呵，之前我不是说过了吗？\n',
            '这只是身为支部负责人的工作而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580100161V#791F顺带一提……\n',
            '到王都的定期船１１点准时出发。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580100162V事不宜迟，\n',
            '赶快去飞艇坪办理搭乘手续吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580100163V愿女神保佑。\n',
            '你们俩行事时务必小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100164V#006F好的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100165V#010F劳您费心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)

    ExecExpressionWithVar(
        0x04,
        (
            (Expr.PushLong, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetScenaFlags(ScenaFlag(0x00C0, 1, 0x601))
    OP_28(0x0054, 0x01, 0x0001)
    OP_28(0x0042, 0x04, 0x10)
    OP_28(0x0042, 0x04, 0x20)
    OP_28(0x0044, 0x04, 0x10)
    OP_28(0x0044, 0x04, 0x20)
    OP_28(0x002B, 0x04, 0x40)

    If(
        (
            (Expr.Eval, "OP_40(0x0340)"),
            Expr.Ez,
            (Expr.Eval, "OP_40(0x0341)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x0342)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_CF19',
    )

    OP_28(0x002D, 0x04, 0x40)

    def _loc_CF19(): pass

    label('loc_CF19')

    If(
        (
            (Expr.Eval, "OP_40(0x0343)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_CF27',
    )

    OP_28(0x002E, 0x04, 0x40)

    def _loc_CF27(): pass

    label('loc_CF27')

    If(
        (
            (Expr.Eval, "OP_40(0x0344)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_CF35',
    )

    OP_28(0x002F, 0x04, 0x40)

    def _loc_CF35(): pass

    label('loc_CF35')

    If(
        (
            (Expr.Eval, "OP_40(0x0345)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_CF43',
    )

    OP_28(0x0030, 0x04, 0x40)

    def _loc_CF43(): pass

    label('loc_CF43')

    OP_4B(0x0008, 255)
    EventEnd(0x00)

    Return()

# id: 0x001A offset: 0xCF4A
@scena.Code('func_1A_CF4A')
def func_1A_CF4A():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_CF67',
    )

    OP_2A(0x002D, 0x0032, 0x002A, 0x0028, 0x002B, 0x002C, 0x0033, 0x0034, 0xFFFF)

    Jump('loc_CFF6')

    def _loc_CF67(): pass

    label('loc_CF67')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 2, 0x55A)),
            Expr.Return,
        ),
        'loc_CF84',
    )

    OP_2A(0x002D, 0x0032, 0x002A, 0x0028, 0x002B, 0x002C, 0x0033, 0x0034, 0xFFFF)

    Jump('loc_CFF6')

    def _loc_CF84(): pass

    label('loc_CF84')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_CF9F',
    )

    OP_2A(0x002D, 0x0032, 0x002A, 0x0028, 0x002B, 0x002C, 0x0033, 0xFFFF)

    Jump('loc_CFF6')

    def _loc_CF9F(): pass

    label('loc_CF9F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 7, 0x51F)),
            Expr.Return,
        ),
        'loc_CFBA',
    )

    OP_2A(0x002D, 0x0032, 0x002A, 0x0028, 0x002B, 0x002C, 0x0033, 0xFFFF)

    Jump('loc_CFF6')

    def _loc_CFBA(): pass

    label('loc_CFBA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_CFD5',
    )

    OP_2A(0x002D, 0x0032, 0x002A, 0x0028, 0x002B, 0x002C, 0x0033, 0xFFFF)

    Jump('loc_CFF6')

    def _loc_CFD5(): pass

    label('loc_CFD5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_CFE8',
    )

    OP_2A(0x002D, 0x0032, 0x002A, 0xFFFF)

    Jump('loc_CFF6')

    def _loc_CFE8(): pass

    label('loc_CFE8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_CFF6',
    )

    OP_2A(0x002D, 0x0032, 0xFFFF)

    def _loc_CFF6(): pass

    label('loc_CFF6')

    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
