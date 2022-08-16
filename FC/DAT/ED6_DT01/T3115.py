import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T3115_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3115   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'T3115.x'
    header.mapIndex       = 1
    header.bgm            = 13
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT01/T3115._SN', 'ED6_DT01/T3115_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
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
        ('ED6_DT07/CH02620._CH', 'ED6_DT07/CH02620P._CP'),
        ('ED6_DT07/CH02100._CH', 'ED6_DT07/CH02100P._CP'),
        ('ED6_DT07/CH01310._CH', 'ED6_DT07/CH01310P._CP'),
        ('ED6_DT07/CH01430._CH', 'ED6_DT07/CH01430P._CP'),
        ('ED6_DT07/CH01190._CH', 'ED6_DT07/CH01190P._CP'),
        ('ED6_DT07/CH01680._CH', 'ED6_DT07/CH01680P._CP'),
        ('ED6_DT07/CH02440._CH', 'ED6_DT07/CH02440P._CP'),
        ('ED6_DT07/CH01230._CH', 'ED6_DT07/CH01230P._CP'),
        ('ED6_DT07/CH01700._CH', 'ED6_DT07/CH01700P._CP'),
        ('ED6_DT07/CH01250._CH', 'ED6_DT07/CH01250P._CP'),
        ('ED6_DT07/CH01100._CH', 'ED6_DT07/CH01100P._CP'),
        ('ED6_DT07/CH01450._CH', 'ED6_DT07/CH01450P._CP'),
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
        ('ED6_DT06/CH20021._CH', 'ED6_DT06/CH20021P._CP'),
        ('ED6_DT07/CH02623._CH', 'ED6_DT07/CH02623P._CP'),
    ]

# id: 0x10001 offset: 0x122
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '玛多克工房长',
            x                   = 2400,
            z                   = 0,
            y                   = 5300,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '凯诺娜上尉',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '将校',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '露依赛',
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
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            name                = '加鲁诺',
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
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            name                = '雨果',
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
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            name                = '格斯塔夫维修长',
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
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '康丝坦茨',
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
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '安东尼',
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
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '伊格尔',
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
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '普罗梅笛',
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
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '威尔姆',
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
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '玻璃杯',
            x                   = 20,
            z                   = 700,
            y                   = 39430,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 917517,
            chipIndex           = 13,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '烟灰缸',
            x                   = 520,
            z                   = 775,
            y                   = 100690,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1572877,
            chipIndex           = 13,
            npcIndex            = 0x0146,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '香烟',
            x                   = 1100,
            z                   = 800,
            y                   = 100800,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1638413,
            chipIndex           = 13,
            npcIndex            = 0x0146,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '书1',
            x                   = -105970,
            z                   = 800,
            y                   = 105440,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1703949,
            chipIndex           = 13,
            npcIndex            = 0x0146,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x342
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x342
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x342
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -101920,
            triggerZ            = 0,
            triggerY            = 93750,
            triggerRange        = 1200,
            actorX              = -101920,
            actorZ              = 0,
            actorY              = 93750,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0010,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -2950,
            triggerZ            = 0,
            triggerY            = 8029,
            triggerRange        = 800,
            actorX              = -2950,
            actorZ              = 1000,
            actorY              = 8029,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0015,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 4150,
            triggerZ            = 0,
            triggerY            = 6850,
            triggerRange        = 800,
            actorX              = 4070,
            actorZ              = 1000,
            actorY              = 7610,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0016,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 4700,
            triggerZ            = 0,
            triggerY            = 2240,
            triggerRange        = 800,
            actorX              = 5490,
            actorZ              = 1000,
            actorY              = 2270,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0017,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 1600,
            triggerZ            = 0,
            triggerY            = 3910,
            triggerRange        = 800,
            actorX              = 1600,
            actorZ              = 1200,
            actorY              = 3910,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0018,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -4430,
            triggerZ            = 0,
            triggerY            = 3760,
            triggerRange        = 800,
            actorX              = -5500,
            actorZ              = 1200,
            actorY              = 3500,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0019,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 190,
            triggerZ            = 0,
            triggerY            = 101690,
            triggerRange        = 1200,
            actorX              = 720,
            actorZ              = 800,
            actorY              = 100680,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x001A,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -105970,
            triggerZ            = 0,
            triggerY            = 105440,
            triggerRange        = 1500,
            actorX              = -105970,
            actorZ              = 800,
            actorY              = 105440,
            flags               = 0x007C,
            talkScenaIndex      = 0x0001,
            talkFunctionIndex   = 0x000C,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -100460,
            triggerZ            = 0,
            triggerY            = -3070,
            triggerRange        = 800,
            actorX              = -100460,
            actorZ              = 1200,
            actorY              = -3070,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x001B,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -100460,
            triggerZ            = 0,
            triggerY            = -4700,
            triggerRange        = 800,
            actorX              = -100460,
            actorZ              = 1200,
            actorY              = -4700,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x001C,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -100460,
            triggerZ            = 0,
            triggerY            = -6860,
            triggerRange        = 800,
            actorX              = -100460,
            actorZ              = 1200,
            actorY              = -6860,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x001D,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -103830,
            triggerZ            = 0,
            triggerY            = 5890,
            triggerRange        = 800,
            actorX              = -103830,
            actorZ              = 1200,
            actorY              = 5890,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x001E,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -104800,
            triggerZ            = 0,
            triggerY            = 9210,
            triggerRange        = 800,
            actorX              = -104800,
            actorZ              = 1200,
            actorY              = 9210,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x001F,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -101680,
            triggerZ            = 0,
            triggerY            = 9240,
            triggerRange        = 800,
            actorX              = -101680,
            actorZ              = 1200,
            actorY              = 9240,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0020,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -100410,
            triggerZ            = 0,
            triggerY            = 8100,
            triggerRange        = 800,
            actorX              = -100410,
            actorZ              = 1200,
            actorY              = 8100,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0021,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x55E
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_56C',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, func_11_8827)

    def _loc_56C(): pass

    label('loc_56C')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_578'),
        (-1, 'loc_58E'),
    )

    def _loc_578(): pass

    label('loc_578')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 5, 0x50D)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_58B',
    )

    SetScenaFlags(ScenaFlag(0x00A1, 6, 0x50E))
    Event(0, func_0F_6673)

    def _loc_58B(): pass

    label('loc_58B')

    Jump('loc_58E')

    def _loc_58E(): pass

    label('loc_58E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 3, 0x603)),
            Expr.Return,
        ),
        'loc_62F',
    )

    ChrSetPos(0x000F, 2240, 0, 3050, 6)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetFlags(0x000F, 0x0010)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0010, -101150, 0, 4900, 9)
    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x000E, -102890, 0, 97500, 280)
    ChrClearFlags(0x0012, 0x0080)
    ChrSetPos(0x0012, -108280, 0, 100340, 215)
    ChrClearFlags(0x0013, 0x0080)
    ChrSetPos(0x0013, -103290, 0, 108340, 355)
    ChrSetChipByIndex(0x0008, 14)
    ChrSetFlags(0x0008, 0x0010)
    ChrSetFlags(0x0008, 0x0004)
    TerminateThread(0x0008, 0xFF)
    ChrSetPos(0x0008, 2510, 250, 5400, 180)

    Jump('loc_B99')

    def _loc_62F(): pass

    label('loc_62F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_6B5',
    )

    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0010, -101150, 0, 4900, 9)
    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x000E, -102890, 0, 97500, 280)
    ChrClearFlags(0x0012, 0x0080)
    ChrSetPos(0x0012, -108280, 0, 100340, 215)
    ChrClearFlags(0x0013, 0x0080)
    ChrSetPos(0x0013, -103290, 0, 108340, 355)
    ChrSetChipByIndex(0x0008, 14)
    ChrSetFlags(0x0008, 0x0010)
    ChrSetFlags(0x0008, 0x0004)
    TerminateThread(0x0008, 0xFF)
    ChrSetPos(0x0008, 2510, 250, 5400, 180)

    Jump('loc_B99')

    def _loc_6B5(): pass

    label('loc_6B5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_723',
    )

    ChrSetFlags(0x0008, 0x0080)
    ChrSetPos(0x000C, -104580, 0, 101850, 186)
    ChrClearFlags(0x000C, 0x0080)
    CreateThread(0x000C, 0x00, 0x00, func_03_EAB)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0010, -101150, 0, 4900, 9)
    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x000E, -102890, 0, 97500, 280)
    ChrClearFlags(0x0013, 0x0080)
    ChrSetPos(0x0013, -103290, 0, 108340, 355)

    Jump('loc_B99')

    def _loc_723(): pass

    label('loc_723')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_7AE',
    )

    ChrSetPos(0x000C, -102800, 0, 96960, 277)
    ChrClearFlags(0x000C, 0x0080)
    ChrSetPos(0x000E, -102800, 0, 97960, 270)
    ChrClearFlags(0x000E, 0x0080)
    ChrSetFlags(0x000E, 0x0010)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0010, -101150, 0, 4900, 9)
    ChrClearFlags(0x0013, 0x0080)
    ChrSetPos(0x0013, -101470, 0, 105910, 180)
    ChrSetChipByIndex(0x0008, 14)
    ChrSetFlags(0x0008, 0x0010)
    ChrSetFlags(0x0008, 0x0004)
    TerminateThread(0x0008, 0xFF)
    ChrSetPos(0x0008, 2510, 250, 5400, 180)

    Jump('loc_B99')

    def _loc_7AE(): pass

    label('loc_7AE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_808',
    )

    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x000E, -102890, 0, 97500, 280)
    ChrClearFlags(0x0012, 0x0080)
    ChrSetPos(0x0012, -101150, 0, -4440, 100)
    ChrSetChipByIndex(0x0008, 14)
    ChrSetFlags(0x0008, 0x0010)
    ChrSetFlags(0x0008, 0x0004)
    TerminateThread(0x0008, 0xFF)
    ChrSetPos(0x0008, 2510, 250, 5400, 180)

    Jump('loc_B99')

    def _loc_808(): pass

    label('loc_808')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 6, 0x536)),
            Expr.Return,
        ),
        'loc_84C',
    )

    ChrClearFlags(0x0013, 0x0080)
    ChrSetPos(0x0013, -101430, 0, 102440, 267)
    ChrSetChipByIndex(0x0008, 14)
    ChrSetFlags(0x0008, 0x0010)
    ChrSetFlags(0x0008, 0x0004)
    TerminateThread(0x0008, 0xFF)
    ChrSetPos(0x0008, 2510, 250, 5400, 180)

    Jump('loc_B99')

    def _loc_84C(): pass

    label('loc_84C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_85B',
    )

    ChrSetFlags(0x0008, 0x0080)

    Jump('loc_B99')

    def _loc_85B(): pass

    label('loc_85B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_909',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 3, 0x51B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_86F',
    )

    ChrSetFlags(0x0008, 0x0080)

    def _loc_86F(): pass

    label('loc_86F')

    ChrSetChipByIndex(0x0008, 14)
    ChrSetFlags(0x0008, 0x0010)
    ChrSetFlags(0x0008, 0x0004)
    TerminateThread(0x0008, 0xFF)
    ChrSetPos(0x0008, 2510, 250, 5400, 180)
    ChrSetPos(0x000C, -103490, 0, 98980, 184)
    ChrClearFlags(0x000C, 0x0080)
    ChrSetPos(0x000D, -102800, 0, 97960, 270)
    ChrClearFlags(0x000D, 0x0080)
    ChrSetFlags(0x000D, 0x0010)
    ChrClearFlags(0x0014, 0x0080)
    ChrSetPos(0x0014, -102960, 0, 8850, 9)
    ChrClearFlags(0x0013, 0x0080)
    ChrSetPos(0x0013, -101660, 0, 107300, 0)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0010, -101150, 0, 4900, 9)

    Jump('loc_B99')

    def _loc_909(): pass

    label('loc_909')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_9B4',
    )

    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0010, -101150, 0, 4900, 9)
    ChrClearFlags(0x000D, 0x0080)
    ChrSetPos(0x000D, -102800, 0, 97440, 277)
    ChrSetFlags(0x000D, 0x0010)
    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x000E, 2180, 0, 3050, 352)
    ChrSetFlags(0x000E, 0x0010)
    ChrClearFlags(0x0012, 0x0080)
    ChrSetPos(0x0012, -101150, 0, -4440, 100)
    ChrSetFlags(0x0012, 0x0010)
    ChrClearFlags(0x0013, 0x0080)
    ChrSetPos(0x0013, -106230, 0, 107410, 325)
    ChrSetChipByIndex(0x0008, 14)
    ChrSetFlags(0x0008, 0x0010)
    ChrSetFlags(0x0008, 0x0004)
    TerminateThread(0x0008, 0xFF)
    ChrSetPos(0x0008, 2510, 250, 5400, 180)

    Jump('loc_B99')

    def _loc_9B4(): pass

    label('loc_9B4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_A5F',
    )

    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0010, -101150, 0, 4900, 9)
    ChrClearFlags(0x000D, 0x0080)
    ChrSetPos(0x000D, -106270, 0, 103210, 195)
    ChrSetFlags(0x000D, 0x0010)
    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x000E, -106210, 0, 102010, 343)
    ChrSetFlags(0x000E, 0x0010)
    ChrClearFlags(0x0012, 0x0080)
    ChrSetPos(0x0012, -101150, 0, -4440, 100)
    ChrSetFlags(0x0012, 0x0010)
    ChrClearFlags(0x0013, 0x0080)
    ChrSetPos(0x0013, -103290, 0, 108340, 355)
    ChrSetChipByIndex(0x0008, 14)
    ChrSetFlags(0x0008, 0x0010)
    ChrSetFlags(0x0008, 0x0004)
    TerminateThread(0x0008, 0xFF)
    ChrSetPos(0x0008, 2510, 250, 5400, 180)

    Jump('loc_B99')

    def _loc_A5F(): pass

    label('loc_A5F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Return,
        ),
        'loc_B07',
    )

    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0010, -101150, 0, 4900, 9)
    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x000E, -102890, 0, 97500, 280)
    ChrClearFlags(0x0011, 0x0080)
    ChrSetPos(0x0011, -104980, 0, 101930, 319)
    CreateThread(0x0011, 0x00, 0x00, func_04_ECF)
    ChrClearFlags(0x0012, 0x0080)
    ChrSetPos(0x0012, -108240, 0, 100430, 225)
    ChrClearFlags(0x0013, 0x0080)
    ChrSetPos(0x0013, -103290, 0, 108340, 355)
    ChrSetFlags(0x0013, 0x0010)
    ChrSetChipByIndex(0x0008, 14)
    ChrSetFlags(0x0008, 0x0010)
    ChrSetFlags(0x0008, 0x0004)
    TerminateThread(0x0008, 0xFF)
    ChrSetPos(0x0008, 2510, 250, 5400, 180)

    Jump('loc_B99')

    def _loc_B07(): pass

    label('loc_B07')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_B99',
    )

    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0010, -101150, 0, 4900, 9)
    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x000E, -102780, 0, 97390, 350)
    ChrSetFlags(0x000E, 0x0010)
    ChrClearFlags(0x0012, 0x0080)
    ChrSetPos(0x0012, -102830, 0, 98700, 178)
    ChrSetFlags(0x0012, 0x0010)
    ChrClearFlags(0x0013, 0x0080)
    ChrSetPos(0x0013, -103290, 0, 108340, 355)
    ChrSetFlags(0x0013, 0x0010)
    ChrSetChipByIndex(0x0008, 14)
    ChrSetFlags(0x0008, 0x0010)
    ChrSetFlags(0x0008, 0x0004)
    TerminateThread(0x0008, 0xFF)
    ChrSetPos(0x0008, 2510, 250, 5400, 180)

    def _loc_B99(): pass

    label('loc_B99')

    ChrSetFlags(0x0018, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x002D, 0x01, 0x0004)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_BB4',
    )

    ChrClearFlags(0x0018, 0x0080)

    def _loc_BB4(): pass

    label('loc_BB4')

    Return()

# id: 0x0001 offset: 0xBB5
@scena.Code('func_01_BB5')
def func_01_BB5():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A7, 2, 0x53A)),
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 0, 0x558)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_BCD',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x54),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_BFA')

    def _loc_BCD(): pass

    label('loc_BCD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 2, 0x532)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 6, 0x536)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_BE5',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x52),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_BFA')

    def _loc_BE5(): pass

    label('loc_BE5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 4, 0x52C)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 2, 0x532)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_BFA',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x51),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_BFA(): pass

    label('loc_BFA')

    OP_72(0x0000, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 4, 0x52C)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 6, 0x536)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_D2A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 2, 0x532)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_D27',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x67),
            Expr.Equ,
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x64),
            Expr.Equ,
            Expr.Or,
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x66),
            Expr.Equ,
            Expr.Or,
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x65),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_C8B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A9, 1, 0x549)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C88',
    )

    LoadEffect(0x01, 'map\\\\mpfog.eff')
    PlayEffect(0x01, 0x01, 0x00FF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    def _loc_C88(): pass

    label('loc_C88')

    Jump('loc_D27')

    def _loc_C8B(): pass

    label('loc_C8B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A9, 2, 0x54A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_D23',
    )

    LoadEffect(0x01, 'map\\\\mpfog.eff')
    PlayEffect(0x01, 0x01, 0x00FF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    LoadEffect(0x00, 'map\\\\mpsmk0.eff')
    PlayEffect(0x00, 0x00, 0x00FF, -101920, 0, 93750, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    Jump('loc_D27')

    def _loc_D23(): pass

    label('loc_D23')

    OP_64(0x00, 0x0001)

    def _loc_D27(): pass

    label('loc_D27')

    Jump('loc_D2E')

    def _loc_D2A(): pass

    label('loc_D2A')

    OP_64(0x00, 0x0001)
    def _loc_D2E(): pass

    label('loc_D2E')

    OP_64(0x02, 0x0001)
    OP_64(0x03, 0x0001)
    OP_64(0x04, 0x0001)
    OP_64(0x05, 0x0001)

    If(
        (
            (Expr.Eval, "OP_29(0x002C, 0x01, 0x0400)"),
            (Expr.Eval, "OP_29(0x002C, 0x01, 0x0800)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x002C, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x002C, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_D72',
    )

    OP_65(0x02, 0x0001)
    OP_65(0x03, 0x0001)
    OP_65(0x04, 0x0001)
    OP_65(0x05, 0x0001)

    def _loc_D72(): pass

    label('loc_D72')

    OP_64(0x06, 0x0001)
    ChrSetFlags(0x0016, 0x0080)
    ChrSetFlags(0x0017, 0x0080)

    If(
        (
            (Expr.Eval, "OP_29(0x002C, 0x01, 0x8000)"),
            (Expr.Eval, "OP_29(0x002C, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x002C, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_DA9',
    )

    OP_65(0x06, 0x0001)
    ChrClearFlags(0x0016, 0x0080)
    ChrClearFlags(0x0017, 0x0080)

    def _loc_DA9(): pass

    label('loc_DA9')

    If(
        (
            (Expr.Eval, "OP_29(0x002C, 0x01, 0x8000)"),
            (Expr.Eval, "OP_29(0x002C, 0x00, 0x40)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_DC4',
    )

    OP_71(0x0000, 0x0010)
    OP_64(0x01, 0x0001)

    def _loc_DC4(): pass

    label('loc_DC4')

    OP_64(0x07, 0x0001)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x002D, 0x00, 0x04)"),
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x002D, 0x01, 0x0004)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_DE4',
    )

    OP_65(0x07, 0x0001)

    def _loc_DE4(): pass

    label('loc_DE4')

    If(
        (
            (Expr.Eval, "OP_29(0x002E, 0x01, 0x0020)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_DF4',
    )

    OP_64(0x0D, 0x0001)

    def _loc_DF4(): pass

    label('loc_DF4')

    If(
        (
            (Expr.Eval, "OP_29(0x002F, 0x01, 0x0010)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_E04',
    )

    OP_64(0x09, 0x0001)

    def _loc_E04(): pass

    label('loc_E04')

    If(
        (
            (Expr.Eval, "OP_29(0x0030, 0x01, 0x0008)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_E14',
    )

    OP_64(0x0E, 0x0001)

    def _loc_E14(): pass

    label('loc_E14')

    OP_64(0x0A, 0x0001)
    OP_64(0x0B, 0x0001)
    OP_64(0x0C, 0x0001)

    If(
        (
            (Expr.Eval, "OP_40(0x0342)"),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x002D, 0x01, 0x0004)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_E35',
    )

    OP_65(0x0A, 0x0001)

    def _loc_E35(): pass

    label('loc_E35')

    If(
        (
            (Expr.Eval, "OP_40(0x0341)"),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x002D, 0x01, 0x0008)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_E4A',
    )

    OP_65(0x0B, 0x0001)

    def _loc_E4A(): pass

    label('loc_E4A')

    If(
        (
            (Expr.Eval, "OP_40(0x0340)"),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x002D, 0x01, 0x0010)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_E5F',
    )

    OP_65(0x0C, 0x0001)

    def _loc_E5F(): pass

    label('loc_E5F')

    If(
        (
            (Expr.Eval, "OP_29(0x002D, 0x00, 0x04)"),
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_E94',
    )

    If(
        (
            (Expr.Eval, "OP_40(0x0342)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_E7A',
    )

    OP_65(0x0A, 0x0001)

    def _loc_E7A(): pass

    label('loc_E7A')

    If(
        (
            (Expr.Eval, "OP_40(0x0341)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_E87',
    )

    OP_65(0x0B, 0x0001)

    def _loc_E87(): pass

    label('loc_E87')

    If(
        (
            (Expr.Eval, "OP_40(0x0340)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_E94',
    )

    OP_65(0x0C, 0x0001)

    def _loc_E94(): pass

    label('loc_E94')

    Return()

# id: 0x0002 offset: 0xE95
@scena.Code('func_02_E95')
def func_02_E95():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_EAA',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_E95')

    def _loc_EAA(): pass

    label('loc_EAA')

    Return()

# id: 0x0003 offset: 0xEAB
@scena.Code('func_03_EAB')
def func_03_EAB():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_ECE',
    )

    OP_8D(0x00FE, -105470, 104540, -101970, 99920, 3000)

    Jump('func_03_EAB')

    def _loc_ECE(): pass

    label('loc_ECE')

    Return()

# id: 0x0004 offset: 0xECF
@scena.Code('func_04_ECF')
def func_04_ECF():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_EF2',
    )

    OP_8D(0x00FE, -106870, 104010, -102300, 99050, 3000)

    Jump('func_04_ECF')

    def _loc_EF2(): pass

    label('loc_EF2')

    Return()

# id: 0x0005 offset: 0xEF3
@scena.Code('func_05_EF3')
def func_05_EF3():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_F65',
    )

    ChrTalk(
        0x000F,
        (
            '#0560100330V#690F王国军的对应措施\n',
            '采取得也太快了点。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560100331V可以看出来\n',
            '他们也十分焦急吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1098')

    def _loc_F65(): pass

    label('loc_F65')

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    ChrTalk(
        0x000F,
        (
            '#0560100318V#690F『莱普尼兹号』\n',
            '正在定期检修中，\n',
            '目前停放在地下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560100319V已经把可能露出马脚的东西\n',
            '都处理干净了，\n',
            '应该没问题了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0550100320V#803F是吗，那我就放心了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550100323V#800F说起来\n',
            '军队的反应也太过迅速了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550100322V如果我们动作再慢一点，\n',
            '说不定就会被他们抓住把柄了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1098(): pass

    label('loc_1098')

    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0x109C
@scena.Code('func_06_109C')
def func_06_109C():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_113F',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，\n',
            '『卡佩尔』的情况好转\n',
            '果然是与导力停止有关系的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大概是因为导力停止，\n',
            '才让整个系统重启了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '搞不好，\n',
            '可以将其作为\n',
            '新的维修方法使用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_113F(): pass

    label('loc_113F')

    TalkEnd(0x00FE)

    Return()

# id: 0x0007 offset: 0x1143
@scena.Code('func_07_1143')
def func_07_1143():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_11CD',
    )

    TalkBegin(0x0013)

    ChrTalk(
        0x00FE,
        (
            '据说…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '『埃尔赛尤号』的照片\n',
            '很快会在王都的\n',
            '历史资料馆里展出。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，什么时候有空，\n',
            '我也一定要去参观一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1713')

    def _loc_11CD(): pass

    label('loc_11CD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_1232',
    )

    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '哼，真是的，\n',
            '资料怎么都找不到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看来必须再次彻底地评估\n',
            '整个工房的管理体制了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1713')

    def _loc_1232(): pass

    label('loc_1232')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_1317',
    )

    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_12B2',
    )

    ChrTalk(
        0x00FE,
        (
            '『埃尔赛尤号』\n',
            '肯定也期待着能够\n',
            '拥有一双崭新的翅膀。 ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果计划能够像这样\n',
            '顺利进行下去的话就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1314')

    def _loc_12B2(): pass

    label('loc_12B2')

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    ChrTalk(
        0x00FE,
        (
            '那位年轻的女士\n',
            '是导力引擎开发项目里\n',
            '新来的成员吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是气质高雅啊。\n',
            '让人非常期待。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1314(): pass

    label('loc_1314')

    Jump('loc_1713')

    def _loc_1317(): pass

    label('loc_1317')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 6, 0x536)),
            Expr.Return,
        ),
        'loc_137A',
    )

    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '哦哦，太好了。\n',
            '研究室内似乎没事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样很快就可以\n',
            '将计划继续进行下去了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1713')

    def _loc_137A(): pass

    label('loc_137A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_151E',
    )

    If(
        (
            (Expr.Eval, "OP_40(0x0346)"),
            (Expr.Eval, "OP_29(0x0029, 0x00, 0x10)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_1438',
    )

    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_13E9',
    )

    ChrTalk(
        0x00FE,
        (
            '通过这次的事，\n',
            '我再次领会到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……我们还是没有\n',
            '理解导力的本质。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1435')

    def _loc_13E9(): pass

    label('loc_13E9')

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    ChrTalk(
        0x00FE,
        (
            '唔……\n',
            '据资料显示……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '上次那个现象\n',
            '只能解释为\n',
            '导力本身停止了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1435(): pass

    label('loc_1435')

    Jump('loc_151B')

    def _loc_1438(): pass

    label('loc_1438')

    If(
        (
            (Expr.Eval, "OP_29(0x0028, 0x01, 0x0001)"),
            (Expr.Eval, "OP_29(0x0029, 0x01, 0x0001)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1453',
    )

    Call(1, 0x0003)

    Jump('loc_151B')

    def _loc_1453(): pass

    label('loc_1453')

    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1503',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_14B4',
    )

    ChrTalk(
        0x00FE,
        (
            '通过这次的事，\n',
            '我再次领会到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……我们还是没有\n',
            '理解导力的本质。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1500')

    def _loc_14B4(): pass

    label('loc_14B4')

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    ChrTalk(
        0x00FE,
        (
            '唔……\n',
            '据资料显示……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '上次那个现象\n',
            '只能解释为\n',
            '导力本身停止了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1500(): pass

    label('loc_1500')

    Jump('loc_151B')

    def _loc_1503(): pass

    label('loc_1503')

    ChrTalk(
        0x00FE,
        (
            '咦，还有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_151B(): pass

    label('loc_151B')

    Jump('loc_1713')

    def _loc_151E(): pass

    label('loc_151E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_15C1',
    )

    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '昨天发生的现象\n',
            '还真让人吃惊啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '据我所知，\n',
            '以现在的导力理论\n',
            '应该还不足以解释那种现象。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵，我也算是个理论家，\n',
            '对此次事件也十分关注。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1713')

    def _loc_15C1(): pass

    label('loc_15C1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Return,
        ),
        'loc_1624',
    )

    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '呼，真是的。\n',
            '资料都放在哪里了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样的话重新\n',
            '设计一下图纸似乎还比较快。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1713')

    def _loc_1624(): pass

    label('loc_1624')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_1713',
    )

    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_1696',
    )

    ChrTalk(
        0x00FE,
        (
            '从王立学院回来的途中\n',
            '竟然被空贼抓作人质了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎呀呀，\n',
            '现在回想起来还是觉得很恐怖呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1713')

    def _loc_1696(): pass

    label('loc_1696')

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    ChrTalk(
        0x00FE,
        (
            '咦，\n',
            '以前准备的资料都放到哪儿去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在去王立学院演讲之前\n',
            '我都应该准备好了啊……\n',
            '这已经是很早之前的事了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x00FE, 0x0010)

    def _loc_1713(): pass

    label('loc_1713')

    TalkEnd(0x00FE)

    Return()

# id: 0x0008 offset: 0x1717
@scena.Code('func_08_1717')
def func_08_1717():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_180A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_1785',
    )

    ChrTalk(
        0x00FE,
        (
            '真的是不得不佩服\n',
            '你们游击士呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '竟然敢深入王国军后方，\n',
            '还顺利把拉赛尔救了出来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1807')

    def _loc_1785(): pass

    label('loc_1785')

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x00FE,
        (
            '哦，是小姑娘你们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '非常感谢你们\n',
            '把拉赛尔救出来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没～事，别担心啦\n',
            '那家伙很顽强的。\n',
            '肯定可以安然无恙地逃掉的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1807(): pass

    label('loc_1807')

    Jump('loc_208C')

    def _loc_180A(): pass

    label('loc_180A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_19CB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_18B9',
    )

    ChrTalk(
        0x00FE,
        (
            '唉，\n',
            '我要的资料怎么也找不到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '亏我经常严厉地\n',
            '告诫康丝坦茨，\n',
            '让她把资料整理好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说起来，\n',
            '那个女的今天也很早就回去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……真是的，头痛啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19C8')

    def _loc_18B9(): pass

    label('loc_18B9')

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x00FE,
        (
            '因为之前出现了导力停止现象，\n',
            '街头时钟的时间已经不太准确了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要把时间调整回来，\n',
            '就要找到建造当时的资料……\n',
            '但现在完全找不到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……康丝坦茨那家伙真是的，\n',
            '我总是说让她把资料室整理好，\n',
            '她就是当作耳旁风。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '关键的时刻派不上用场，\n',
            '那还叫做什么资料室啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_19C8(): pass

    label('loc_19C8')

    Jump('loc_208C')

    def _loc_19CB(): pass

    label('loc_19CB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_1B25',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_1A4F',
    )

    ChrTalk(
        0x00FE,
        (
            '唉，真是的。\n',
            '要查的书完全找不到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '脑子老是得不到满足，\n',
            '现在连肚子都饿了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，\n',
            '一会儿去吃点东西吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B22')

    def _loc_1A4F(): pass

    label('loc_1A4F')

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x00FE,
        (
            '唉，真是的。\n',
            '想查阅的书完全找不到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，有意思的是， \n',
            '和眼下研究无关的资料\n',
            '倒是一个接一个地发现了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，这个也想看看，\n',
            '那个也要回头翻一下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……但是重要的是\n',
            '还是找不到现在就需要的书。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1B22(): pass

    label('loc_1B22')

    Jump('loc_208C')

    def _loc_1B25(): pass

    label('loc_1B25')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_1C39',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_1B99',
    )

    ChrTurnDirection(0x0012, 0x0010, 400)

    ChrTalk(
        0x00FE,
        (
            '喂，康丝坦茨！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你就不能\n',
            '稍微用心点工作吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这个资料室里的书\n',
            '已经乱七八糟了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C36')

    def _loc_1B99(): pass

    label('loc_1B99')

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x00FE,
        (
            '呼，\n',
            '我想来调查一下昨天发生的现象……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这书架还是那么脏啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这就说明\n',
            '那个康丝坦茨\n',
            '根本就没有好好整理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是的，\n',
            '不好好工作光拿薪水……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C36(): pass

    label('loc_1C36')

    Jump('loc_208C')

    def _loc_1C39(): pass

    label('loc_1C39')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Return,
        ),
        'loc_1EFD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_1CDB',
    )

    ChrTurnDirection(0x00FE, 0x0107, 0)

    ChrTalk(
        0x00FE,
        (
            '哦，提妲丫头。\n',
            '辛苦你们啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，\n',
            '最好在游击士的陪同下\n',
            '去做这种工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这是我年轻时遭遇过很多次危险后\n',
            '总结出的经验教训呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1EFA')

    def _loc_1CDB(): pass

    label('loc_1CDB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B0, 6, 0x586)),
            Expr.Return,
        ),
        'loc_1D3F',
    )

    ChrTalk(
        0x00FE,
        (
            '好了，趁现在有空，\n',
            '就找找相关的资料吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就算光是浏览论文，\n',
            '都要花费相当的时间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1EFA')

    def _loc_1D3F(): pass

    label('loc_1D3F')

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))
    SetScenaFlags(ScenaFlag(0x00B0, 6, 0x586))
    ChrTurnDirection(0x00FE, 0x0107, 0)

    ChrTalk(
        0x00FE,
        (
            '哦，提妲丫头。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '卡鲁迪亚隧道的照明设备\n',
            '更换工作进行得还顺利吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#065F嗯，那个……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#067F那个……\n',
            '还、还可以啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还可以？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我不知道你说的是什么意思，\n',
            '总之更换好了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#061F嗯，是的。\n',
            '那个已经没有问题了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哦，那样就好。\n',
            '辛苦你们啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过呢，\n',
            '最好在游击士的陪同下\n',
            '去做这种工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这是我年轻时遭遇过很多次危险后\n',
            '总结出的经验教训呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#067F呵呵……\n',
            '您说得没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#562F嗯，今后我会注意的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1EFA(): pass

    label('loc_1EFA')

    Jump('loc_208C')

    def _loc_1EFD(): pass

    label('loc_1EFD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_208C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_1FC1',
    )

    ChrTalk(
        0x00FE,
        (
            '关于新型引擎的开发，\n',
            '本来应该是由拉赛尔\n',
            '担当所有工作的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是他把中枢部分的\n',
            '驱动导力器设计完成之后，\n',
            '就去开始别的研究了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '全是因为他，\n',
            '所以事情才会变成现在这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_208C')

    def _loc_1FC1(): pass

    label('loc_1FC1')

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x00FE,
        (
            '唔唔，研究员谢绝了邀请，\n',
            '真的是很麻烦啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽说『埃尔赛尤号』上\n',
            '搭载的是改良的飞艇引擎，\n',
            '但那只不过是暂时应付一下的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是没有正式的新型引擎，\n',
            '好不容易建造的新型飞艇就毫无意义了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_208C(): pass

    label('loc_208C')

    TalkEnd(0x00FE)

    Return()

# id: 0x0009 offset: 0x2090
@scena.Code('func_09_2090')
def func_09_2090():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Return,
        ),
        'loc_20AD',
    )

    PlaySE(402, 0x00, 0x64)

    ChrTalk(
        0x00FE,
        (
            '喵－噢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_20AD(): pass

    label('loc_20AD')

    TalkEnd(0x00FE)

    Return()

# id: 0x000A offset: 0x20B1
@scena.Code('func_0A_20B1')
def func_0A_20B1():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Return,
        ),
        'loc_2104',
    )

    ChrTalk(
        0x00FE,
        (
            '真是辛苦你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，再有什么事的话，\n',
            '还会拜托你们的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

    def _loc_2104(): pass

    label('loc_2104')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_27B5',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x002D, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2130',
    )

    If(
        (
            (Expr.Eval, "OP_40(0x0340)"),
            (Expr.Eval, "OP_40(0x0341)"),
            Expr.Or,
            (Expr.Eval, "OP_40(0x0342)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_2130',
    )

    Call(1, 0x0006)
    TalkEnd(0x00FE)

    Return()

    def _loc_2130(): pass

    label('loc_2130')

    If(
        (
            (Expr.Eval, "OP_29(0x002E, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_214B',
    )

    If(
        (
            (Expr.Eval, "OP_40(0x0343)"),
            Expr.Return,
        ),
        'loc_214B',
    )

    Call(1, 0x0008)
    TalkEnd(0x00FE)

    Return()

    def _loc_214B(): pass

    label('loc_214B')

    If(
        (
            (Expr.Eval, "OP_29(0x002F, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2166',
    )

    If(
        (
            (Expr.Eval, "OP_40(0x0344)"),
            Expr.Return,
        ),
        'loc_2166',
    )

    Call(1, 0x000A)
    TalkEnd(0x00FE)

    Return()

    def _loc_2166(): pass

    label('loc_2166')

    If(
        (
            (Expr.Eval, "OP_29(0x0030, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2181',
    )

    If(
        (
            (Expr.Eval, "OP_40(0x0345)"),
            Expr.Return,
        ),
        'loc_2181',
    )

    Call(1, 0x000B)
    TalkEnd(0x00FE)

    Return()

    def _loc_2181(): pass

    label('loc_2181')

    If(
        (
            (Expr.Eval, "OP_29(0x0030, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_2299',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_2206',
    )

    ChrTalk(
        0x00FE,
        (
            '……啊，\n',
            '工作已经做得差不多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽说有点早，\n',
            '不过现在去吃午饭也好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '到了中午，\n',
            '店里面就很拥挤了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2296')

    def _loc_2206(): pass

    label('loc_2206')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '呼，\n',
            '工房终于平静下来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这里老是出现混乱，\n',
            '都没有工作的时间了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过安排好预算的话\n',
            '还是能全部处理完的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呜呜…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2296(): pass

    label('loc_2296')

    Jump('loc_27B2')

    def _loc_2299(): pass

    label('loc_2299')

    If(
        (
            (Expr.Eval, "OP_29(0x002D, 0x01, 0x4000)"),
            Expr.Return,
        ),
        'loc_23A8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_2327',
    )

    ChrTalk(
        0x00FE,
        (
            '……啊，\n',
            '工作已经做得差不多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽说有点早，\n',
            '不过现在去吃午饭也好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天又没吃早点，\n',
            '这样下去会伤身体的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23A5')

    def _loc_2327(): pass

    label('loc_2327')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '呼，\n',
            '工房终于平静下来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这里老是出现混乱，\n',
            '都没有工作的时间了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '干脆使用一点预算\n',
            '让别人帮忙整理一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_23A5(): pass

    label('loc_23A5')

    Jump('loc_27B2')

    def _loc_23A8(): pass

    label('loc_23A8')

    If(
        (
            (Expr.Eval, "OP_29(0x002D, 0x00, 0x04)"),
            (Expr.Eval, "OP_29(0x0030, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_26BD',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x002D, 0x01, 0x8000)"),
            Expr.Return,
        ),
        'loc_2476',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然对你们有点不好意思， \n',
            '但是委托已经中止了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '剩下的工作就交给蔡斯支部来做，\n',
            '请放心吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果以后还有委托的话，\n',
            '就请你们一定要做到底。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，你们多保重。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_26BA')

    def _loc_2476(): pass

    label('loc_2476')

    OP_28(0x002D, 0x01, 0x8000)

    ChrTalk(
        0x00FE,
        (
            '咦，是你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然对你们有点不好意思， \n',
            '但是委托已经中止了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#004F嗯？为什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我从协会那里听说了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们马上就要\n',
            '调到别的支部去了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以调离之前，\n',
            '必须将委托的事宜整理好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#014F是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '对不起。\n',
            '委托半途而废……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#003F真的很抱歉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，别在意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为你们还有别的重要工作，\n',
            '这也是没办法的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '剩下的工作交给\n',
            '蔡斯支部接手就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F好吧，\n',
            '这样也算帮了我们大忙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那以后也要继续努力哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果以后还有委托的话，\n',
            '就请你们一定要做到底。',
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
            '#010F感谢最近一段时间\n',
            '您对我们的诸多照顾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_26BA(): pass

    label('loc_26BA')

    Jump('loc_27B2')

    def _loc_26BD(): pass

    label('loc_26BD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_2740',
    )

    ChrTalk(
        0x00FE,
        (
            '……啊，\n',
            '工作已经做得差不多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽说有点早，\n',
            '不过现在去吃午饭也好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天又没吃早点，\n',
            '这样下去会伤身体的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_27B2')

    def _loc_2740(): pass

    label('loc_2740')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '呼，\n',
            '工房终于平静下来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这里老是出现混乱，\n',
            '都没有工作的时间了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，\n',
            '快点开始整理资料吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_27B2(): pass

    label('loc_27B2')

    Jump('loc_37CF')

    def _loc_27B5(): pass

    label('loc_27B5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_295E',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x002D, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_27E1',
    )

    If(
        (
            (Expr.Eval, "OP_40(0x0340)"),
            (Expr.Eval, "OP_40(0x0341)"),
            Expr.Or,
            (Expr.Eval, "OP_40(0x0342)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_27E1',
    )

    Call(1, 0x0005)
    TalkEnd(0x00FE)

    Return()

    def _loc_27E1(): pass

    label('loc_27E1')

    If(
        (
            (Expr.Eval, "OP_29(0x002E, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_27FC',
    )

    If(
        (
            (Expr.Eval, "OP_40(0x0343)"),
            Expr.Return,
        ),
        'loc_27FC',
    )

    Call(1, 0x0007)
    TalkEnd(0x00FE)

    Return()

    def _loc_27FC(): pass

    label('loc_27FC')

    If(
        (
            (Expr.Eval, "OP_29(0x002F, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2817',
    )

    If(
        (
            (Expr.Eval, "OP_40(0x0344)"),
            Expr.Return,
        ),
        'loc_2817',
    )

    Call(1, 0x0009)
    TalkEnd(0x00FE)

    Return()

    def _loc_2817(): pass

    label('loc_2817')

    If(
        (
            (Expr.Eval, "OP_29(0x0030, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2832',
    )

    If(
        (
            (Expr.Eval, "OP_40(0x0345)"),
            Expr.Return,
        ),
        'loc_2832',
    )

    Call(1, 0x000B)
    TalkEnd(0x00FE)

    Return()

    def _loc_2832(): pass

    label('loc_2832')

    If(
        (
            (Expr.Eval, "OP_29(0x002D, 0x00, 0x04)"),
            (Expr.Eval, "OP_29(0x0030, 0x00, 0x10)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_28C4',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，\n',
            '我怎么又有种不太稳当的感觉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '工房长不知道去哪儿了不说，\n',
            '维修员也是到处乱跑……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是的，一点都安不下心来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_295B')

    def _loc_28C4(): pass

    label('loc_28C4')

    If(
        (
            (Expr.Eval, "OP_29(0x002D, 0x00, 0x02)"),
            (Expr.Eval, "OP_29(0x002D, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_28DD',
    )

    Call(1, 0x0004)

    Jump('loc_295B')

    def _loc_28DD(): pass

    label('loc_28DD')

    ChrTalk(
        0x00FE,
        (
            '呼，\n',
            '我怎么又有种不太稳当的感觉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '工房长不知道去哪儿了不说，\n',
            '维修员也是到处乱跑……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是的，一点都安不下心来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_295B(): pass

    label('loc_295B')

    Jump('loc_37CF')

    def _loc_295E(): pass

    label('loc_295E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_2AF4',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x002D, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_298A',
    )

    If(
        (
            (Expr.Eval, "OP_40(0x0340)"),
            (Expr.Eval, "OP_40(0x0341)"),
            Expr.Or,
            (Expr.Eval, "OP_40(0x0342)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_298A',
    )

    Call(1, 0x0005)
    TalkEnd(0x00FE)

    Return()

    def _loc_298A(): pass

    label('loc_298A')

    If(
        (
            (Expr.Eval, "OP_29(0x002E, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_29A5',
    )

    If(
        (
            (Expr.Eval, "OP_40(0x0343)"),
            Expr.Return,
        ),
        'loc_29A5',
    )

    Call(1, 0x0007)
    TalkEnd(0x00FE)

    Return()

    def _loc_29A5(): pass

    label('loc_29A5')

    If(
        (
            (Expr.Eval, "OP_29(0x002F, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_29C0',
    )

    If(
        (
            (Expr.Eval, "OP_40(0x0344)"),
            Expr.Return,
        ),
        'loc_29C0',
    )

    Call(1, 0x0009)
    TalkEnd(0x00FE)

    Return()

    def _loc_29C0(): pass

    label('loc_29C0')

    If(
        (
            (Expr.Eval, "OP_29(0x0030, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_29DB',
    )

    If(
        (
            (Expr.Eval, "OP_40(0x0345)"),
            Expr.Return,
        ),
        'loc_29DB',
    )

    Call(1, 0x000B)
    TalkEnd(0x00FE)

    Return()

    def _loc_29DB(): pass

    label('loc_29DB')

    If(
        (
            (Expr.Eval, "OP_29(0x0030, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_2A1C',
    )

    ChrTalk(
        0x00FE,
        (
            '啊，早上好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天一整天能平平安安就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2AF1')

    def _loc_2A1C(): pass

    label('loc_2A1C')

    If(
        (
            (Expr.Eval, "OP_29(0x002D, 0x00, 0x04)"),
            Expr.Return,
        ),
        'loc_2AA4',
    )

    ChrTalk(
        0x00FE,
        (
            '#2120181562V啊，早上好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181563V今天一整天能平平安安就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181564V想要的书\n',
            '也能快点找到就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2AF1')

    def _loc_2AA4(): pass

    label('loc_2AA4')

    If(
        (
            (Expr.Eval, "OP_29(0x002D, 0x00, 0x02)"),
            (Expr.Eval, "OP_29(0x002D, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2ABD',
    )

    Call(1, 0x0004)

    Jump('loc_2AF1')

    def _loc_2ABD(): pass

    label('loc_2ABD')

    ChrTalk(
        0x00FE,
        (
            '啊，早上好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天一整天能平平安安就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2AF1(): pass

    label('loc_2AF1')

    Jump('loc_37CF')

    def _loc_2AF4(): pass

    label('loc_2AF4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 6, 0x536)),
            Expr.Return,
        ),
        'loc_2D8D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Return,
        ),
        'loc_2B5F',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，建筑物里都是烟，\n',
            '好讨厌呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天还是早点回家吧。\n',
            '不管再发生什么我都要回家。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2D8A')

    def _loc_2B5F(): pass

    label('loc_2B5F')

    If(
        (
            (Expr.Eval, "OP_29(0x0030, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_2BC9',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，建筑物里都是烟，\n',
            '好讨厌呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天还是早点回家吧。\n',
            '不管再发生什么我都要回家。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 5, 0xD))

    Jump('loc_2D8A')

    def _loc_2BC9(): pass

    label('loc_2BC9')

    If(
        (
            (Expr.Eval, "OP_29(0x002D, 0x00, 0x04)"),
            Expr.Return,
        ),
        'loc_2C78',
    )

    ChrTalk(
        0x00FE,
        (
            '#2120181571V呼，建筑物里都是烟，\n',
            '好讨厌呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181572V……唔，这种情况下\n',
            '还是不要谈工作的事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181573V真是不好意思，\n',
            '明天再把书给我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 5, 0xD))

    Jump('loc_2D8A')

    def _loc_2C78(): pass

    label('loc_2C78')

    If(
        (
            (Expr.Eval, "OP_29(0x002D, 0x00, 0x02)"),
            Expr.Return,
        ),
        'loc_2D1F',
    )

    ChrTalk(
        0x00FE,
        (
            '#2120181571V呼，建筑物里都是烟，\n',
            '好讨厌呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181572V……唔，这种情况下\n',
            '还是不要谈工作的事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181576V委托的事\n',
            '只好拖到明天了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 5, 0xD))

    Jump('loc_2D8A')

    def _loc_2D1F(): pass

    label('loc_2D1F')

    ChrTalk(
        0x00FE,
        (
            '呼，因为刚才拼命地跑，\n',
            '身上的肌肉痛得受不了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天还是早点回家吧。\n',
            '不管再发生什么我都要回家。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 5, 0xD))

    def _loc_2D8A(): pass

    label('loc_2D8A')

    Jump('loc_37CF')

    def _loc_2D8D(): pass

    label('loc_2D8D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_2F28',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x002D, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2DB9',
    )

    If(
        (
            (Expr.Eval, "OP_40(0x0340)"),
            (Expr.Eval, "OP_40(0x0341)"),
            Expr.Or,
            (Expr.Eval, "OP_40(0x0342)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_2DB9',
    )

    Call(1, 0x0005)
    TalkEnd(0x00FE)

    Return()

    def _loc_2DB9(): pass

    label('loc_2DB9')

    If(
        (
            (Expr.Eval, "OP_29(0x002E, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2DD4',
    )

    If(
        (
            (Expr.Eval, "OP_40(0x0343)"),
            Expr.Return,
        ),
        'loc_2DD4',
    )

    Call(1, 0x0007)
    TalkEnd(0x00FE)

    Return()

    def _loc_2DD4(): pass

    label('loc_2DD4')

    If(
        (
            (Expr.Eval, "OP_29(0x002F, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2DEF',
    )

    If(
        (
            (Expr.Eval, "OP_40(0x0344)"),
            Expr.Return,
        ),
        'loc_2DEF',
    )

    Call(1, 0x0009)
    TalkEnd(0x00FE)

    Return()

    def _loc_2DEF(): pass

    label('loc_2DEF')

    If(
        (
            (Expr.Eval, "OP_29(0x0030, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2E0A',
    )

    If(
        (
            (Expr.Eval, "OP_40(0x0345)"),
            Expr.Return,
        ),
        'loc_2E0A',
    )

    Call(1, 0x000B)
    TalkEnd(0x00FE)

    Return()

    def _loc_2E0A(): pass

    label('loc_2E0A')

    If(
        (
            (Expr.Eval, "OP_29(0x002D, 0x00, 0x04)"),
            (Expr.Eval, "OP_29(0x0030, 0x00, 0x10)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_2E95',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯，\n',
            '那是演算室的威尔姆吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '第一次靠得这么近看，\n',
            '原来也就是个普通的男人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且……\n',
            '感觉他有点神经质啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F25')

    def _loc_2E95(): pass

    label('loc_2E95')

    If(
        (
            (Expr.Eval, "OP_29(0x002D, 0x00, 0x02)"),
            (Expr.Eval, "OP_29(0x002D, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2EAE',
    )

    Call(1, 0x0004)

    Jump('loc_2F25')

    def _loc_2EAE(): pass

    label('loc_2EAE')

    ChrTalk(
        0x00FE,
        (
            '嗯，\n',
            '那是演算室的威尔姆吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '第一次靠得这么近看，\n',
            '原来也就是个普通的男人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且……\n',
            '感觉他有点神经质啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2F25(): pass

    label('loc_2F25')

    Jump('loc_37CF')

    def _loc_2F28(): pass

    label('loc_2F28')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_307D',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x002D, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2F54',
    )

    If(
        (
            (Expr.Eval, "OP_40(0x0340)"),
            (Expr.Eval, "OP_40(0x0341)"),
            Expr.Or,
            (Expr.Eval, "OP_40(0x0342)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_2F54',
    )

    Call(1, 0x0005)
    TalkEnd(0x00FE)

    Return()

    def _loc_2F54(): pass

    label('loc_2F54')

    If(
        (
            (Expr.Eval, "OP_29(0x002E, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2F6F',
    )

    If(
        (
            (Expr.Eval, "OP_40(0x0343)"),
            Expr.Return,
        ),
        'loc_2F6F',
    )

    Call(1, 0x0007)
    TalkEnd(0x00FE)

    Return()

    def _loc_2F6F(): pass

    label('loc_2F6F')

    If(
        (
            (Expr.Eval, "OP_29(0x002F, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2F8A',
    )

    If(
        (
            (Expr.Eval, "OP_40(0x0344)"),
            Expr.Return,
        ),
        'loc_2F8A',
    )

    Call(1, 0x0009)
    TalkEnd(0x00FE)

    Return()

    def _loc_2F8A(): pass

    label('loc_2F8A')

    If(
        (
            (Expr.Eval, "OP_29(0x0030, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2FA5',
    )

    If(
        (
            (Expr.Eval, "OP_40(0x0345)"),
            Expr.Return,
        ),
        'loc_2FA5',
    )

    Call(1, 0x000B)
    TalkEnd(0x00FE)

    Return()

    def _loc_2FA5(): pass

    label('loc_2FA5')

    If(
        (
            (Expr.Eval, "OP_29(0x002D, 0x00, 0x04)"),
            (Expr.Eval, "OP_29(0x0030, 0x00, 0x10)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_300D',
    )

    ChrTalk(
        0x00FE,
        (
            '真是的，\n',
            '伊格尔就不能安静地看会儿书吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在这种场合下\n',
            '保持安静可是常识啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_307A')

    def _loc_300D(): pass

    label('loc_300D')

    If(
        (
            (Expr.Eval, "OP_29(0x002D, 0x00, 0x02)"),
            (Expr.Eval, "OP_29(0x002D, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3026',
    )

    Call(1, 0x0004)

    Jump('loc_307A')

    def _loc_3026(): pass

    label('loc_3026')

    ChrTalk(
        0x00FE,
        (
            '真是的，\n',
            '伊格尔就不能安静地看会儿书吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在这种场合下\n',
            '保持安静可是常识啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_307A(): pass

    label('loc_307A')

    Jump('loc_37CF')

    def _loc_307D(): pass

    label('loc_307D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_31CE',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x002D, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_30A9',
    )

    If(
        (
            (Expr.Eval, "OP_40(0x0340)"),
            (Expr.Eval, "OP_40(0x0341)"),
            Expr.Or,
            (Expr.Eval, "OP_40(0x0342)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_30A9',
    )

    Call(1, 0x0005)
    TalkEnd(0x00FE)

    Return()

    def _loc_30A9(): pass

    label('loc_30A9')

    If(
        (
            (Expr.Eval, "OP_29(0x002E, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_30C4',
    )

    If(
        (
            (Expr.Eval, "OP_40(0x0343)"),
            Expr.Return,
        ),
        'loc_30C4',
    )

    Call(1, 0x0007)
    TalkEnd(0x00FE)

    Return()

    def _loc_30C4(): pass

    label('loc_30C4')

    If(
        (
            (Expr.Eval, "OP_29(0x002F, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_30DF',
    )

    If(
        (
            (Expr.Eval, "OP_40(0x0344)"),
            Expr.Return,
        ),
        'loc_30DF',
    )

    Call(1, 0x0009)
    TalkEnd(0x00FE)

    Return()

    def _loc_30DF(): pass

    label('loc_30DF')

    If(
        (
            (Expr.Eval, "OP_29(0x0030, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_30FA',
    )

    If(
        (
            (Expr.Eval, "OP_40(0x0345)"),
            Expr.Return,
        ),
        'loc_30FA',
    )

    Call(1, 0x000B)
    TalkEnd(0x00FE)

    Return()

    def _loc_30FA(): pass

    label('loc_30FA')

    If(
        (
            (Expr.Eval, "OP_29(0x002D, 0x00, 0x04)"),
            (Expr.Eval, "OP_29(0x0030, 0x00, 0x10)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_3160',
    )

    ChrTalk(
        0x00FE,
        (
            '那边的伊格尔\n',
            '还真不是一般的啰嗦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我总算知道为什么\n',
            '他那种岁数还是单身。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_31CB')

    def _loc_3160(): pass

    label('loc_3160')

    If(
        (
            (Expr.Eval, "OP_29(0x002D, 0x00, 0x02)"),
            (Expr.Eval, "OP_29(0x002D, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3179',
    )

    Call(1, 0x0004)

    Jump('loc_31CB')

    def _loc_3179(): pass

    label('loc_3179')

    ChrTalk(
        0x00FE,
        (
            '那边的伊格尔\n',
            '还真不是一般的啰嗦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我总算知道为什么\n',
            '他那种岁数还是单身。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_31CB(): pass

    label('loc_31CB')

    Jump('loc_37CF')

    def _loc_31CE(): pass

    label('loc_31CE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Return,
        ),
        'loc_3548',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x002D, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_31FA',
    )

    If(
        (
            (Expr.Eval, "OP_40(0x0340)"),
            (Expr.Eval, "OP_40(0x0341)"),
            Expr.Or,
            (Expr.Eval, "OP_40(0x0342)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_31FA',
    )

    Call(1, 0x0005)
    TalkEnd(0x00FE)

    Return()

    def _loc_31FA(): pass

    label('loc_31FA')

    If(
        (
            (Expr.Eval, "OP_29(0x002E, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3215',
    )

    If(
        (
            (Expr.Eval, "OP_40(0x0343)"),
            Expr.Return,
        ),
        'loc_3215',
    )

    Call(1, 0x0007)
    TalkEnd(0x00FE)

    Return()

    def _loc_3215(): pass

    label('loc_3215')

    If(
        (
            (Expr.Eval, "OP_29(0x002F, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3230',
    )

    If(
        (
            (Expr.Eval, "OP_40(0x0344)"),
            Expr.Return,
        ),
        'loc_3230',
    )

    Call(1, 0x0009)
    TalkEnd(0x00FE)

    Return()

    def _loc_3230(): pass

    label('loc_3230')

    If(
        (
            (Expr.Eval, "OP_29(0x0030, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_324B',
    )

    If(
        (
            (Expr.Eval, "OP_40(0x0345)"),
            Expr.Return,
        ),
        'loc_324B',
    )

    Call(1, 0x000B)
    TalkEnd(0x00FE)

    Return()

    def _loc_324B(): pass

    label('loc_324B')

    If(
        (
            (Expr.Eval, "OP_29(0x0030, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_32E1',
    )

    ChrTalk(
        0x00FE,
        (
            '啊，我以为是谁呢，\n',
            '这不是各位游击士和提妲吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们特地为我把书收集回来，\n',
            '真是很感谢呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '多亏你们，\n',
            '看来我暂时不用工作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3545')

    def _loc_32E1(): pass

    label('loc_32E1')

    If(
        (
            (Expr.Eval, "OP_29(0x002D, 0x00, 0x04)"),
            Expr.Return,
        ),
        'loc_3344',
    )

    ChrTalk(
        0x00FE,
        (
            '那么，再找到其他书的话，\n',
            '记得送到这里来哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '各位游击士，\n',
            '之前多亏你们了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3545')

    def _loc_3344(): pass

    label('loc_3344')

    If(
        (
            (Expr.Eval, "OP_29(0x002D, 0x00, 0x02)"),
            (Expr.Eval, "OP_29(0x002D, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_335D',
    )

    Call(1, 0x0004)

    Jump('loc_3545')

    def _loc_335D(): pass

    label('loc_335D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_33D7',
    )

    ChrTurnDirection(0x00FE, 0x0107, 0)

    ChrTalk(
        0x00FE,
        (
            '提妲你偶尔\n',
            '也来帮忙整理一下书嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '光让我一个人干的话，\n',
            '我会有种资料室将发生\n',
            '不得了的事的预感。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3545')

    def _loc_33D7(): pass

    label('loc_33D7')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '欢迎来到资料室。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3417',
    )

    ChrTalk(
        0x00FE,
        (
            '啊，这不是提妲吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3439')

    def _loc_3417(): pass

    label('loc_3417')

    ChrTurnDirection(0x00FE, 0x0107, 400)

    ChrTalk(
        0x00FE,
        (
            '哎呀，\n',
            '这不是提妲吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3439(): pass

    label('loc_3439')

    ChrTalk(
        0x0107,
        (
            '#060F啊，康丝坦茨阿姨。\n',
            '好久不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是好久不见了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '提妲你偶尔\n',
            '也来帮忙整理一下书嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '光让我一个人干的话，\n',
            '我会有种资料室将发生\n',
            '不得了的事的预感。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#060F啊、啊哈哈……\n',
            '我、我知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎呀，\n',
            '提妲你可真是一个好孩子㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么就拜托了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3545(): pass

    label('loc_3545')

    Jump('loc_37CF')

    def _loc_3548(): pass

    label('loc_3548')

    If(
        (
            (Expr.Eval, "OP_29(0x002D, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_356D',
    )

    If(
        (
            (Expr.Eval, "OP_40(0x0340)"),
            (Expr.Eval, "OP_40(0x0341)"),
            Expr.Or,
            (Expr.Eval, "OP_40(0x0342)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_356D',
    )

    Call(1, 0x0005)
    TalkEnd(0x00FE)

    Return()

    def _loc_356D(): pass

    label('loc_356D')

    If(
        (
            (Expr.Eval, "OP_29(0x002E, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3588',
    )

    If(
        (
            (Expr.Eval, "OP_40(0x0343)"),
            Expr.Return,
        ),
        'loc_3588',
    )

    Call(1, 0x0007)
    TalkEnd(0x00FE)

    Return()

    def _loc_3588(): pass

    label('loc_3588')

    If(
        (
            (Expr.Eval, "OP_29(0x002F, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_35A3',
    )

    If(
        (
            (Expr.Eval, "OP_40(0x0344)"),
            Expr.Return,
        ),
        'loc_35A3',
    )

    Call(1, 0x0009)
    TalkEnd(0x00FE)

    Return()

    def _loc_35A3(): pass

    label('loc_35A3')

    If(
        (
            (Expr.Eval, "OP_29(0x0030, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_35BE',
    )

    If(
        (
            (Expr.Eval, "OP_40(0x0345)"),
            Expr.Return,
        ),
        'loc_35BE',
    )

    Call(1, 0x000B)
    TalkEnd(0x00FE)

    Return()

    def _loc_35BE(): pass

    label('loc_35BE')

    If(
        (
            (Expr.Eval, "OP_29(0x0030, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_3646',
    )

    ChrTalk(
        0x00FE,
        (
            '啊，我以为是谁呢，\n',
            '各位游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们特地为我把书收集回来，\n',
            '真是很感谢呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果有想要看的书，\n',
            '就请随便看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_37CF')

    def _loc_3646(): pass

    label('loc_3646')

    If(
        (
            (Expr.Eval, "OP_29(0x002D, 0x00, 0x04)"),
            Expr.Return,
        ),
        'loc_36C6',
    )

    ChrTalk(
        0x00FE,
        (
            '#2120181613V如果有想要看的资料，\n',
            '就请随便看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181614V拜托你们了，\n',
            '找到了书的话，\n',
            '就请拿到这里来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_37CF')

    def _loc_36C6(): pass

    label('loc_36C6')

    If(
        (
            (Expr.Eval, "OP_29(0x002D, 0x00, 0x02)"),
            (Expr.Eval, "OP_29(0x002D, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_36DF',
    )

    Call(1, 0x0004)

    Jump('loc_37CF')

    def _loc_36DF(): pass

    label('loc_36DF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_373B',
    )

    ChrTalk(
        0x00FE,
        (
            '如果有想要看的书，\n',
            '就请随便看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，看完之后，\n',
            '请务必把书放回原处。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_37CF')

    def _loc_373B(): pass

    label('loc_373B')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '哎，我好像没见过你们啊……\n',
            '啊，这种事倒也无所谓。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '欢迎你们来资料室。\n',
            '我是这里的管理员康丝坦茨。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果有想要看的书，\n',
            '就请随便看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_37CF(): pass

    label('loc_37CF')

    TalkEnd(0x00FE)

    Return()

# id: 0x000B offset: 0x37D3
@scena.Code('func_0B_37D3')
def func_0B_37D3():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 3, 0x603)),
            Expr.Return,
        ),
        'loc_398F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_384C',
    )

    ChrTalk(
        0x0008,
        (
            '#0550100323V#800F说起来\n',
            '军队的反应也太过迅速了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550100324V他们也会抱着\n',
            '拼命的决心来搜查吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3987')

    def _loc_384C(): pass

    label('loc_384C')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))
    OP_4A(0x000F, 255)

    ChrTalk(
        0x000F,
        (
            '#0560100318V#690F『莱普尼兹号』\n',
            '正在定期检修中，\n',
            '目前停放在地下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560100319V已经把可能露出马脚的东西\n',
            '都处理干净了，\n',
            '应该没问题了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0550100320V#803F是吗，那我就放心了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550100321V#800F说起来\n',
            '军队的反应也太过迅速了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550100322V如果我们动作再慢一点，\n',
            '说不定就会被他们抓住把柄了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4B(0x000F, 255)

    def _loc_3987(): pass

    label('loc_3987')

    ChrSetSubChip(0x00FE, 0)

    Jump('loc_5273')

    def _loc_398F(): pass

    label('loc_398F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_3B4A',
    )

    ChrClearFlags(0x00FE, 0x0010)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x87),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_39B8',
    )

    ChrSetSubChip(0x00FE, 1)

    Jump('loc_39D3')

    def _loc_39B8(): pass

    label('loc_39B8')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xE1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_39CE',
    )

    ChrSetSubChip(0x00FE, 0)

    Jump('loc_39D3')

    def _loc_39CE(): pass

    label('loc_39CE')

    ChrSetSubChip(0x00FE, 2)

    def _loc_39D3(): pass

    label('loc_39D3')

    ChrSetDirection(0x00FE, 180, 0)
    ChrSetFlags(0x00FE, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_3A8A',
    )

    ChrTalk(
        0x0008,
        (
            '#0550100169V#803F呼，\n',
            '总之『卡佩尔』已经隐藏好了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550100170V之后的问题就是\n',
            '『莱普尼兹号』了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550100171V#800F这事还是和格斯塔夫\n',
            '商量一下比较好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3B42')

    def _loc_3A8A(): pass

    label('loc_3A8A')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x0008,
        (
            '#0550100166V#802F咦，艾丝蒂尔、约修亚。\n',
            '还没有出发吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550100167V#801F这里的事你们不用担心。\n',
            '就算军队来检查，\n',
            '我也会设法应付他们的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550100168V总之去王都的路上要小心哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3B42(): pass

    label('loc_3B42')

    ChrSetSubChip(0x00FE, 0)

    Jump('loc_5273')

    def _loc_3B4A(): pass

    label('loc_3B4A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_4063',
    )

    ChrClearFlags(0x00FE, 0x0010)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x87),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_3B73',
    )

    ChrSetSubChip(0x00FE, 1)

    Jump('loc_3B8E')

    def _loc_3B73(): pass

    label('loc_3B73')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xE1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_3B89',
    )

    ChrSetSubChip(0x00FE, 0)

    Jump('loc_3B8E')

    def _loc_3B89(): pass

    label('loc_3B89')

    ChrSetSubChip(0x00FE, 2)

    def _loc_3B8E(): pass

    label('loc_3B8E')

    ChrSetDirection(0x00FE, 180, 0)
    ChrSetFlags(0x00FE, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 2, 0x55A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3E23',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_3C14',
    )

    ChrTalk(
        0x0008,
        (
            '#0550091553V#800F就算是为了提妲，\n',
            '你们也要救出拉赛尔博士啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550091554V那我就等着你们的好消息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3E20')

    def _loc_3C14(): pass

    label('loc_3C14')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x0008,
        (
            '#0550091541V#800F哟，早上好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550091542V找到什么线索没有？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010091543V#002F嗯，\n',
            '现在要去协会确认一下情报。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0550091544V#802F咦，\n',
            '说起来提妲没和你们一起吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020091545V#015F她去医务室\n',
            '照看阿加特兄了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020091546V提妲她似乎相当担心\n',
            '阿加特兄的情况呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0550091547V#803F……是吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550091548V就算是为了提妲，\n',
            '你们也要救出拉赛尔博士啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010091549V#002F嗯，我会加油的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020091550V#010F一定全力以赴。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020091551V那么，我们先告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0550091552V#800F嗯，等你们的好消息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3E20(): pass

    label('loc_3E20')

    Jump('loc_405B')

    def _loc_3E23(): pass

    label('loc_3E23')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_3E81',
    )

    ChrTalk(
        0x0008,
        (
            '#0550091565V#800F有力的线索吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550091566V我很期待呢。\n',
            '博士的事就拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_405B')

    def _loc_3E81(): pass

    label('loc_3E81')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x0008,
        (
            '#0550091555V#800F哟，各位。\n',
            '找到什么线索没有？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010091556V#505F嗯，\n',
            '虽然得到了一些情报……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020091557V#015F抱歉，工房长先生。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020091558V现在还在搜查当中，\n',
            '详细的情况暂时不便透露。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020091559V#012F不过……确实已经得到\n',
            '与犯人有关的有力线索。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0550091560V#802F哦哦，是吗！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550091561V#801F看来调查也取得了\n',
            '相当大的进展啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550091562V我等着你们的好消息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010091563V#000F嗯，我们一定会努力的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020091564V#010F那么，我们先告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_405B(): pass

    label('loc_405B')

    ChrSetSubChip(0x00FE, 0)

    Jump('loc_5273')

    def _loc_4063(): pass

    label('loc_4063')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_4458',
    )

    ChrClearFlags(0x00FE, 0x0010)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x87),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_408C',
    )

    ChrSetSubChip(0x00FE, 1)

    Jump('loc_40A7')

    def _loc_408C(): pass

    label('loc_408C')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xE1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_40A2',
    )

    ChrSetSubChip(0x00FE, 0)

    Jump('loc_40A7')

    def _loc_40A2(): pass

    label('loc_40A2')

    ChrSetSubChip(0x00FE, 2)

    def _loc_40A7(): pass

    label('loc_40A7')

    ChrSetDirection(0x00FE, 180, 0)
    ChrSetFlags(0x00FE, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_4109',
    )

    ChrTalk(
        0x0008,
        (
            '#0550091585V#800F现在不是闲聊的场合吧。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550091586V你们赶快去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4450')

    def _loc_4109(): pass

    label('loc_4109')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 6, 0x556)),
            Expr.Return,
        ),
        'loc_4199',
    )

    ChrTalk(
        0x0008,
        (
            '#0550091574V#800F据说受伤的游击士\n',
            '已经送到医务室去了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550091575V现在似乎不是闲聊的场合吧。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550091576V你们赶快去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4450')

    def _loc_4199(): pass

    label('loc_4199')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 1, 0x551)),
            Expr.Return,
        ),
        'loc_4312',
    )

    ChrTalk(
        0x0008,
        (
            '#0550091577V#800F哦哦，是你们啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550091578V据说受伤的游击士\n',
            '已经被送回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020091579V#012F嗯，\n',
            '他是中了某种未知的毒……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020091580V我们刚刚向皮克赛恩教区长\n',
            '请教了治疗方法。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020091581V现在马上就去钟乳石洞\n',
            '采集做药的材料。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0550091582V#800F嗯，\n',
            '那么这可不是闲聊的时候呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550091583V你们赶快去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020091584V#012F是的，我们这就去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4450')

    def _loc_4312(): pass

    label('loc_4312')

    ChrTalk(
        0x0008,
        (
            '#0550091567V#800F哦哦，是你们啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550091568V据说受伤的游击士\n',
            '已经被送回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020091569V#012F嗯，\n',
            '他是中了某种未知的毒……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020091570V我们正准备去找\n',
            '皮克塞恩教区长询问治疗方法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0550091571V#800F嗯，\n',
            '那么这可不是闲聊的时候呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550091572V你们赶快去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020091573V#012F是的，我们这就去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4450(): pass

    label('loc_4450')

    ChrSetSubChip(0x00FE, 0)

    Jump('loc_5273')

    def _loc_4458(): pass

    label('loc_4458')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A7, 0, 0x538)),
            Expr.Return,
        ),
        'loc_4559',
    )

    ChrClearFlags(0x00FE, 0x0010)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x87),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_4481',
    )

    ChrSetSubChip(0x00FE, 1)

    Jump('loc_449C')

    def _loc_4481(): pass

    label('loc_4481')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xE1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_4497',
    )

    ChrSetSubChip(0x00FE, 0)

    Jump('loc_449C')

    def _loc_4497(): pass

    label('loc_4497')

    ChrSetSubChip(0x00FE, 2)

    def _loc_449C(): pass

    label('loc_449C')

    ChrSetDirection(0x00FE, 180, 0)
    ChrSetFlags(0x00FE, 0x0010)

    ChrTalk(
        0x0008,
        (
            '#0550091599V#800F根据我的判断，\n',
            '拉赛尔博士被掳走的事\n',
            '还是瞒着大多数人比较好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550091600V这样子你们行动起来\n',
            '也会比较方便吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550091601V博士的事\n',
            '就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x00FE, 0)

    Jump('loc_5273')

    def _loc_4559(): pass

    label('loc_4559')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 6, 0x536)),
            Expr.Return,
        ),
        'loc_4849',
    )

    ChrClearFlags(0x00FE, 0x0010)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x87),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_4582',
    )

    ChrSetSubChip(0x00FE, 1)

    Jump('loc_459D')

    def _loc_4582(): pass

    label('loc_4582')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xE1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_4598',
    )

    ChrSetSubChip(0x00FE, 0)

    Jump('loc_459D')

    def _loc_4598(): pass

    label('loc_4598')

    ChrSetSubChip(0x00FE, 2)

    def _loc_459D(): pass

    label('loc_459D')

    ChrSetDirection(0x00FE, 180, 0)
    ChrSetFlags(0x00FE, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_4661',
    )

    ChrTalk(
        0x0008,
        (
            '#0550091602V#803F根据我的判断，\n',
            '拉赛尔博士被掳走的事\n',
            '还是瞒着大多数人比较好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550091603V#800F这样子你们行动起来\n',
            '也会比较方便吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550091604V博士的事\n',
            '就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4841')

    def _loc_4661(): pass

    label('loc_4661')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x0008,
        (
            '#0550091587V#803F…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550091588V……根据我的判断，\n',
            '拉赛尔博士被掳走的事\n',
            '还是瞒着大多数人比较好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550091589V这样子你们行动起来\n',
            '也会比较方便吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020091590V#015F我认为这个判断相当正确。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010091591V#003F嗯，要不然肯定会引起恐慌的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0550091592V#800F各位游击士。\n',
            '博士的事就拜托了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550091593V……提妲，\n',
            '你也不要太过沮丧哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550091594V没事的，\n',
            '博士一定会平安的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070091595V#063F好的…………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070091596V…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4841(): pass

    label('loc_4841')

    ChrSetSubChip(0x00FE, 0)

    Jump('loc_5273')

    def _loc_4849(): pass

    label('loc_4849')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_4A82',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 3, 0x51B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_48B6',
    )

    ChrTalk(
        0x0008,
        (
            '#0550091597V#800F提妲就拜托你们两个照顾了。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550091598V提妲，\n',
            '去的时候要当心哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4A7F')

    def _loc_48B6(): pass

    label('loc_48B6')

    ChrClearFlags(0x00FE, 0x0010)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x87),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_48D8',
    )

    ChrSetSubChip(0x00FE, 1)

    Jump('loc_48F3')

    def _loc_48D8(): pass

    label('loc_48D8')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xE1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_48EE',
    )

    ChrSetSubChip(0x00FE, 0)

    Jump('loc_48F3')

    def _loc_48EE(): pass

    label('loc_48EE')

    ChrSetSubChip(0x00FE, 2)

    def _loc_48F3(): pass

    label('loc_48F3')

    ChrSetDirection(0x00FE, 180, 0)
    ChrSetFlags(0x00FE, 0x0010)

    If(
        (
            (Expr.Eval, "OP_29(0x002C, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_49C4',
    )

    ChrTalk(
        0x0008,
        (
            '#0550181202V#805F啊，是你们啊。\n',
            '刚才很抱歉呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550181203V从现在起我要好好休养，\n',
            '还要努力争取\n',
            '早日和香烟一刀两断啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550181204V#800F那么，到亚尔摩去的路上\n',
            '提妲就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4A7A')

    def _loc_49C4(): pass

    label('loc_49C4')

    If(
        (
            (Expr.Eval, "OP_29(0x002C, 0x01, 0x0200)"),
            Expr.Return,
        ),
        'loc_49FE',
    )

    ChrTalk(
        0x0008,
        (
            '#0550181134V#805F发、发现什么了吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4A7A')

    def _loc_49FE(): pass

    label('loc_49FE')

    If(
        (
            (Expr.Eval, "OP_29(0x002C, 0x01, 0x0100)"),
            (Expr.Eval, "OP_42(0x003B)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4A20',
    )

    ChrSetSubChip(0x00FE, 0)
    Call(1, 0x0002)

    Jump('loc_4A7A')

    def _loc_4A20(): pass

    label('loc_4A20')

    ChrTalk(
        0x0008,
        (
            '#0550091605V#800F咦，怎么了？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550091606V去亚尔摩村的话，\n',
            '要从西南方的门口出城啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4A7A(): pass

    label('loc_4A7A')

    ChrSetSubChip(0x00FE, 0)

    def _loc_4A7F(): pass

    label('loc_4A7F')

    Jump('loc_5273')

    def _loc_4A82(): pass

    label('loc_4A82')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_4BA5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_4B0C',
    )

    ChrTalk(
        0x0008,
        (
            '#0550091610V#800F我听说了，\n',
            '卢安的库莱泽谢绝此次工作邀请了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550091611V代替他的人……\n',
            '不是那么容易可以找到的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4BA2')

    def _loc_4B0C(): pass

    label('loc_4B0C')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x0008,
        (
            '#0550091607V#800F哦，雨果。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550091608V我都听说了，\n',
            '卢安的库莱泽谢绝此次工作邀请了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550091609V代替他的人……\n',
            '不是那么容易可以找到的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4BA2(): pass

    label('loc_4BA2')

    Jump('loc_5273')

    def _loc_4BA5(): pass

    label('loc_4BA5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_514B',
    )

    ChrClearFlags(0x00FE, 0x0010)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x87),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_4BCE',
    )

    ChrSetSubChip(0x00FE, 1)

    Jump('loc_4BE9')

    def _loc_4BCE(): pass

    label('loc_4BCE')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xE1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_4BE4',
    )

    ChrSetSubChip(0x00FE, 0)

    Jump('loc_4BE9')

    def _loc_4BE4(): pass

    label('loc_4BE4')

    ChrSetSubChip(0x00FE, 2)

    def _loc_4BE9(): pass

    label('loc_4BE9')

    ChrSetDirection(0x00FE, 180, 0)
    ChrSetFlags(0x00FE, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B0, 4, 0x584)),
            Expr.Return,
        ),
        'loc_4CA4',
    )

    ChrTalk(
        0x0008,
        (
            '#0550091637V#800F博士应该在\n',
            '三楼的工作室里面。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550091638V#805F拜托了， \n',
            '千万不要太过蛮干。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550091639V#806F再发生昨天那样的事，\n',
            '短时间内就无法进行实验了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5143')

    def _loc_4CA4(): pass

    label('loc_4CA4')

    SetScenaFlags(ScenaFlag(0x00B0, 4, 0x584))
    OP_28(0x003F, 0x01, 0x0040)

    ChrTalk(
        0x0008,
        (
            '#0550091612V#800F哟，早上好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010091613V#001F早上好，工房长叔叔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070091614V#560F早上好～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0550091615V#805F唉，真是的，\n',
            '昨天的事让人头疼啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550091616V一大清早，\n',
            '市民就来发泄不满，忙得我团团转。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010091617V#506F哇，好可怜哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010091618V其实这又不是\n',
            '工房长叔叔的错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020091619V#013F抱歉，工房长叔叔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020091620V都怪我们，\n',
            '引起了这样的麻烦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0550091621V#802F啊，没有没有，\n',
            '你们不用道歉啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550091622V这样的事故\n',
            '在实验过程中时而发生\n',
            '也是可以理解的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550091623V#803F……唉，要是拉赛尔博士的话，\n',
            '简直就是经常性的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010091624V#501F博士已经来了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0550091625V#800F哦哦，似乎相当有干劲呢。\n',
            '这么一大清早就来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550091626V他肯定需要人帮忙，\n',
            '你们现在就去看看吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550091627V他现在肯定在\n',
            '三楼的工作室里面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020091628V#010F三楼的工作室吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020091629V我们马上过去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010091630V#000F嗯，我们也很在意呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0550091631V#800F啊，提妲！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070091632V#064F嗯？什么事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0550091633V#805F千、千万不要\n',
            '让博士再乱来哦。\n',
            '千万不要太过蛮干。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550091634V#806F再发生昨天那样的事，\n',
            '短时间内就无法进行实验了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070091635V#065F好的，我明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070091636V#060F那么，工房长叔叔，告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5143(): pass

    label('loc_5143')

    ChrSetSubChip(0x00FE, 0)

    Jump('loc_5273')

    def _loc_514B(): pass

    label('loc_514B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Return,
        ),
        'loc_5273',
    )

    ChrClearFlags(0x00FE, 0x0010)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x87),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_5174',
    )

    ChrSetSubChip(0x00FE, 1)

    Jump('loc_518F')

    def _loc_5174(): pass

    label('loc_5174')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xE1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_518A',
    )

    ChrSetSubChip(0x00FE, 0)

    Jump('loc_518F')

    def _loc_518A(): pass

    label('loc_518A')

    ChrSetSubChip(0x00FE, 2)

    def _loc_518F(): pass

    label('loc_518F')

    ChrSetDirection(0x00FE, 180, 0)
    ChrSetFlags(0x00FE, 0x0010)

    ChrTalk(
        0x0008,
        (
            '#0550091640V#802F哦，怎么了？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550091641V博士的工房\n',
            '在城市的西南方哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550091642V#801F如果有什么新发现，\n',
            '记得一定要先来告诉我啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550091643V对于我们这些技术工作者来说，\n',
            '这个可是非常让人感兴趣的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x00FE, 0)

    def _loc_5273(): pass

    label('loc_5273')

    TalkEnd(0x00FE)

    Return()

# id: 0x000C offset: 0x5277
@scena.Code('func_0C_5277')
def func_0C_5277():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_53B3',
    )

    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5312',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '关于新型导力引擎，\n',
            '我们刚才开了个讨论会，\n',
            '现在刚刚结束。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '昨天没想出什么好点子，真是急坏我了。\n',
            '但不管怎么说好歹混了过去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_53AD')

    def _loc_5312(): pass

    label('loc_5312')

    ChrTalk(
        0x00FE,
        (
            '不过，\n',
            '当思考遇到瓶颈的时候，\n',
            '吃点东西也是很有效果的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '昨天刚喝了些汤，\n',
            '霎时间灵光一现……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '再遇到大脑停电，\n',
            '就把乌尔斯叫来，\n',
            '让他给我炖汤。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_53AD(): pass

    label('loc_53AD')

    TalkEnd(0x00FE)

    Jump('loc_5884')

    def _loc_53B3(): pass

    label('loc_53B3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_561B',
    )

    ChrSetFlags(0x00FE, 0x0010)
    TalkBegin(0x00FE)
    TerminateThread(0x000E, 0xFF)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5559',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x000C,
        (
            '我们面临的现状是，\n',
            '就算将翼层断面和导力系统进行改良，\n',
            '推进效率也很难提高。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '所以，不妨转变一下视点，\n',
            '从操作简便性的方面\n',
            '重新考虑一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '重新评估机体各部件的配置，\n',
            '按照减阻装置的形状， \n',
            '将连接外部的通路简化。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '原来如此，是采用最适合\n',
            '『埃尔赛尤号』的发动机短舱形式，\n',
            '追求完备性吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '着眼点很有意思呢。\n',
            '比起极限性能，运转效率的重要性\n',
            '在应用方面是得到大家一致认同的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5612')

    def _loc_5559(): pass

    label('loc_5559')

    ChrTalk(
        0x00FE,
        (
            '这个引擎在功率输出方面\n',
            '已经得到保证了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果可以将拉赛尔博士\n',
            '新设计的驱动导力器实现的话，\n',
            '实际性能可以大大超出要求吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以，\n',
            '希望今后在设计上\n',
            '能够多多考虑完备性的方面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5612(): pass

    label('loc_5612')

    OP_85(0x000E)
    TalkEnd(0x00FE)

    Jump('loc_5884')

    def _loc_561B(): pass

    label('loc_561B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_5884',
    )

    ChrSetFlags(0x00FE, 0x0010)
    TalkBegin(0x00FE)
    OP_4A(0x000D, 255)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_57C1',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    TalkSetChrName('设计室')

    ChrTalk(
        0x000D,
        (
            '嗯，这个枪身的设计\n',
            '希望可以短一些。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '不然的话，我想就不能充分发挥\n',
            '苦心设计的导力高压的性能了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '嗯，确实，\n',
            '从工学的角度上来说是这样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '可是如果再短的话， \n',
            '会变得头重脚轻吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '考虑到握持方法的话，\n',
            '这种设计似乎……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '虽然我也\n',
            '考虑了这方面的因素，\n',
            '不过这不符合我的方针。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '总之我希望\n',
            '可以严格按照\n',
            '发挥最佳性能的方针进行设计。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '啊，是吗。\n',
            '是这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_587D')

    def _loc_57C1(): pass

    label('loc_57C1')

    ChrTalk(
        0x000C,
        (
            '不、不过……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '还是稍微考虑一下\n',
            '操作的简易性比较好吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '但是，那样的话，\n',
            '性能方面必然有所牺牲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '我希望露依赛你\n',
            '也能够做一个\n',
            '敢于挑战极限的技术人员。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '啊，是、是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_587D(): pass

    label('loc_587D')

    OP_4B(0x000D, 255)
    TalkEnd(0x00FE)

    def _loc_5884(): pass

    label('loc_5884')

    Return()

# id: 0x000D offset: 0x5885
@scena.Code('func_0D_5885')
def func_0D_5885():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_5B04',
    )

    OP_4A(0x000C, 255)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5A26',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    TalkSetChrName('设计室')

    ChrTalk(
        0x000D,
        (
            '嗯，这个枪身的设计\n',
            '希望可以短一些。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '不然的话，我想就不能充分发挥\n',
            '苦心设计的导力高压的性能了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '嗯，确实，\n',
            '从工学的角度上来说是这样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '可是如果再短的话， \n',
            '会变得头重脚轻吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '考虑到握持方法的话，\n',
            '这种设计似乎……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '虽然我也\n',
            '考虑了这方面的因素，\n',
            '不过这不符合我的方针。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '总之我希望\n',
            '可以严格按照\n',
            '发挥最佳性能的方针进行设计。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '啊，是吗。\n',
            '是这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5AFD')

    def _loc_5A26(): pass

    label('loc_5A26')

    ChrTalk(
        0x000C,
        (
            '不、不过……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '还是稍微考虑一下\n',
            '操作的简易性比较好吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '但是，那样的话，\n',
            '性能方面必然有所牺牲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '我希望露依赛你\n',
            '也能够做一个\n',
            '敢于挑战极限的技术人员。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '（这是最后一次机会了，\n',
            '　不好好做的话……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5AFD(): pass

    label('loc_5AFD')

    OP_4B(0x000C, 255)

    Jump('loc_5CBF')

    def _loc_5B04(): pass

    label('loc_5B04')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_5BAD',
    )

    ChrTalk(
        0x00FE,
        (
            '呼……\n',
            '露依赛要调到其他部门了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '能调到她最想去的飞艇部门，\n',
            '真是可喜可贺呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，我也不能输给她。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要努力争取早日让\n',
            '新型的导力枪成品化。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5CBF')

    def _loc_5BAD(): pass

    label('loc_5BAD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_5CBF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_5C1E',
    )

    ChrTalk(
        0x00FE,
        (
            '她是个优秀的研究员，\n',
            '经验也积累了不少。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '让她去做自己想做的事情，\n',
            '我想对工房也有好处。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5CBF')

    def _loc_5C1E(): pass

    label('loc_5C1E')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '露依赛啊……\n',
            '嗯，她是个优秀的研究员。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过真可惜呀……\n',
            '她好像已经对\n',
            '导力枪开发失去了热情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要她做其他开发项目我也赞成，\n',
            '这对她来说也是件好事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5CBF(): pass

    label('loc_5CBF')

    ChrSetSubChip(0x00FE, 0)
    TalkEnd(0x00FE)

    Return()

# id: 0x000E offset: 0x5CC8
@scena.Code('func_0E_5CC8')
def func_0E_5CC8():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_5E07',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_5D3E',
    )

    ChrTalk(
        0x00FE,
        (
            '不过，加鲁诺也是\n',
            '有着实际成就的研究员。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果是他的话，\n',
            '继续进行导力枪的研究是没问题的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5E04')

    def _loc_5D3E(): pass

    label('loc_5D3E')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '虽然经历了一些波折，\n',
            '不过导力引擎的开发计划\n',
            '终于开始有进展了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '中途加入的露依赛\n',
            '做得比预想还要好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然这让加鲁诺失去了一个优秀助手，\n',
            '总感觉有点对不起他，\n',
            '不过确实对我们帮助很大。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5E04(): pass

    label('loc_5E04')

    Jump('loc_666F')

    def _loc_5E07(): pass

    label('loc_5E07')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_5E6F',
    )

    ChrTalk(
        0x00FE,
        (
            '呼～第一次的商讨很顺利，\n',
            '真是让我松了一口气啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总之，\n',
            '感觉对新的工作越来越顺手了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_666F')

    def _loc_5E6F(): pass

    label('loc_5E6F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_6090',
    )

    TerminateThread(0x000C, 0xFF)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_600D',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x000C,
        (
            '我们面临的现状是，\n',
            '就算将翼层断面和导力系统进行改良，\n',
            '推进效率也很难提高。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '所以，不妨转变一下视点，\n',
            '从操作简便性的方面\n',
            '重新考虑一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '重新评估机体各部件的配置，\n',
            '按照减阻装置的形状， \n',
            '将连接外部的通路简化。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '原来如此，是采用最适合\n',
            '『埃尔赛尤号』的发动机短舱形式，\n',
            '追求完备性吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '着眼点很有意思呢。\n',
            '比起极限性能，运转效率的重要性\n',
            '在应用方面是得到大家一致认同的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_608A')

    def _loc_600D(): pass

    label('loc_600D')

    ChrTalk(
        0x00FE,
        (
            '虽然还处在概念阶段，\n',
            '不过这个方法真的很有前途。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '用整备性的观点\n',
            '对内部构造重新观察分析，\n',
            '是至今为止从没有过的想法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_608A(): pass

    label('loc_608A')

    OP_85(0x000C)

    Jump('loc_666F')

    def _loc_6090(): pass

    label('loc_6090')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_6179',
    )

    ChrTalk(
        0x00FE,
        (
            '新型导力引擎的开发\n',
            '大胆邀请了新手露依赛\n',
            '共同参加开发工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对于她是一个相当大的考验，\n',
            '而对于我们来说也是一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果年轻一代的想法\n',
            '能够有利于研究就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过说实话我还是很担心。\n',
            '真是的，胃又开始疼了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_666F')

    def _loc_6179(): pass

    label('loc_6179')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_61D7',
    )

    ChrTalk(
        0x00FE,
        (
            '对不起，我正忙着呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '其实是关于\n',
            '『埃尔赛尤号』\n',
            '新型导力引擎的开发工程……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_666F')

    def _loc_61D7(): pass

    label('loc_61D7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_6350',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_624A',
    )

    ChrTalk(
        0x00FE,
        (
            '我想露依赛她\n',
            '也差不多该独立了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果你的意见和我一样的话，\n',
            '我可以马上向工房长提出申请。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_634D')

    def _loc_624A(): pass

    label('loc_624A')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '虽然我知道昨晚发生了那样的事，\n',
            '你现在应该非常忙……\n',
            '不过请借用我一点时间可以吗，加鲁诺。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我听说了露依赛的事，\n',
            '她的志愿是做飞艇方面的研究吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可以的话，\n',
            '能不能让她参加这次的\n',
            '『埃尔赛尤号』新型引擎开发呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……你作为她的主管，\n',
            '意见如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_634D(): pass

    label('loc_634D')

    Jump('loc_666F')

    def _loc_6350(): pass

    label('loc_6350')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Return,
        ),
        'loc_652C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_6433',
    )

    ChrTalk(
        0x00FE,
        (
            '『埃尔赛尤号』\n',
            '是以新型引擎为前提\n',
            '设计出来的机体。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果借用旧的引擎，\n',
            '就不能发挥出原本的性能了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼～在这点上说不定需要\n',
            '大胆地转换思考的方向才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000E, 0x0011, 400)

    ChrTalk(
        0x00FE,
        (
            '喂，安东尼。\n',
            '如果是你，会选择谁呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6529')

    def _loc_6433(): pass

    label('loc_6433')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '能够担任开发『埃尔赛尤号』的\n',
            '新型引擎研究员……吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '心脏部分的设计\n',
            '不是谁都能轻易胜任的工作呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然这样的人不容易找，\n',
            '不过也不能随便就让『埃尔赛尤号』\n',
            '用替代引擎去飞行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼～在这点上说不定需要\n',
            '大胆地转换思考的方向才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6529(): pass

    label('loc_6529')

    Jump('loc_666F')

    def _loc_652C(): pass

    label('loc_652C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_666F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_65B3',
    )

    ChrTalk(
        0x00FE,
        (
            '库莱泽他\n',
            '为了养育年幼的弟弟，\n',
            '已经决心留在卢安了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他本人其实应该\n',
            '也很想在研究所工作的。\n',
            '我们是不会怪他的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_666F')

    def _loc_65B3(): pass

    label('loc_65B3')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '呼，『埃尔赛尤号』\n',
            '使用的新型导力引擎\n',
            '在开发过程中遇上了点问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '卢安的库莱泽\n',
            '本来是要和我们一起研究的，\n',
            '最后竟然辞掉了这个工作……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样下去整个工程\n',
            '就要陷入停滞状态了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_666F(): pass

    label('loc_666F')

    TalkEnd(0x00FE)

    Return()

# id: 0x000F offset: 0x6673
@scena.Code('func_0F_6673')
def func_0F_6673():
    EventBegin(0x00)
    CameraMove(1050, 0, 2760, 0)
    FormationAddMember(0x06, 0xFF)
    ChrSetPos(0x0101, -200, 0, 1000, 0)
    ChrSetPos(0x0102, -1600, 0, 900, 0)
    ChrSetSubChip(0x0008, 2)
    ChrTurnDirection(0x0101, 0x0008, 0)
    ChrTurnDirection(0x0102, 0x0008, 0)
    ChrSetFlags(0x0107, 0x0080)
    ChrSetPos(0x0107, -1100, 0, -1600, 0)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0550070644V#801F#3P哟，我正等着你们呢。\n',
            '艾丝蒂尔、约修亚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070645V#000F啊，您好。\n',
            '初次见面，工房长先生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070646V#010F在您百忙之中前来打扰。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_678F')
    def lambda_678F():
        CameraMove(2680, 0, 4730, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_678F)

    @scena.Lambda('lambda_67A7')
    def lambda_67A7():
        ChrWalkTo(0x00FE, 2610, 0, 3050, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_67A7)

    Sleep(500)

    @scena.Lambda('lambda_67C7')
    def lambda_67C7():
        ChrWalkTo(0x00FE, 1700, 0, 3050, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_67C7)

    WaitForThreadExit(0x0101, 0x0001)
    ChrSetSubChip(0x0008, 0)

    @scena.Lambda('lambda_67EC')
    def lambda_67EC():
        ChrTurnDirection(0x00FE, 0x0008, 0)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_67EC)

    WaitForThreadExit(0x0102, 0x0001)

    @scena.Lambda('lambda_67FF')
    def lambda_67FF():
        ChrTurnDirection(0x00FE, 0x0008, 0)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_67FF)

    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0008,
        (
            '#0550070647V#800F哪里哪里，\n',
            '都不用那么客气。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550070648V因为我们以前\n',
            '总是受到游击士协会……\n',
            '特别是卡西乌斯先生的关照。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550070649V他的孩子来了，\n',
            '一定要好好欢迎才行呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070650V#004F哎！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010070651V工房长先生\n',
            '认识我们的老爸吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0550070652V#803F哈哈，何止是认识，\n',
            '卡西乌斯先生还是我的大恩人呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550070653V#800F这个中央工房，\n',
            '就算说是整个大陆上\n',
            '导力技术最先进的地方也不为过。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550070654V而这种技术带来的这样那样的麻烦\n',
            '也是源源不绝啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550070655V以前每到实在难以应付的时候，\n',
            '我们就会联络洛连特支部，\n',
            '请他过来帮忙解决。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070656V#501F是、是这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070657V#019F哈哈，\n',
            '怪不得父亲经常出差呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0550070658V#801F没想到今天\n',
            '恩人的孩子们特地前来拜访。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550070659V务必让我一尽地主之宜哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070660V#008F嘿嘿……\n',
            '谢谢，工房长先生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070661V#012F这件事说来话长……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔他们向工房长\n',
            '详细地说明了迄今为止有关黑色导力器的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0008,
        (
            '#0550070662V#800F原来如此，\n',
            '竟然有这样的事啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550070663V不介意的话，\n',
            '可以让我看看那个导力器吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070664V#006F嗯，当然可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔从行李中取出黑色导力器，\n',
            '然后交给了玛多克工房长。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    Fade(500)
    PlaySE(130, 0x00, 0x64)
    ChrSetPos(0x0015, 2290, 800, 4650, 0)
    ChrClearFlags(0x0015, 0x0080)
    OP_0D()
    Sleep(500)

    OP_62(0x0008, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1200)

    OP_63(0x0008)

    ChrTalk(
        0x0008,
        (
            '#0550070665V#802F唔……\n',
            '的确是很奇妙的东西……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550070666V很明显是最近才制造的，\n',
            '不过奇怪的是……没有刻上序列号啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070667V#505F序列号？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070668V#014F就是刻在导力器外壳上的\n',
            '生产序号吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0550070669V#800F嗯，说得没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550070670V不管是什么样的导力器，\n',
            '都无一例外地刻有\n',
            '表示产地及日期的生产序号。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550070671V这一点不光是利贝尔，\n',
            '在大陆的其他各国也是一样的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550070672V这是从五十年前刚发明导力器时\n',
            '就保留下来的传统啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070673V#501F哦～是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '在一番好奇心之下，\n',
            '艾丝蒂尔从怀里取出自己的战术导力器。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0101,
        (
            '#0010070674V#004F……啊，真的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010070675V这上面也刻有号码呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070676V#017F唉……\n',
            '难道你以前都没发觉吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070677V#509F要、要你啰嗦～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010070678V#501F不过不过，\n',
            '没有生产序号是那么奇怪的事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0550070679V#803F嗯，没错。\n',
            '对导力技术者来说，\n',
            '在产品上刻上序号是基本的常识。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550070680V就算是试制品也是一样……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550070681V#800F照此看来，制作这个东西的背后\n',
            '很有可能藏有什么隐秘的目的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070682V#002F隐秘的目的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0550070683V#800F唔，更详细的情况\n',
            '不调查其内部是弄不清楚的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550070684V#802F…………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070685V#010F怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0550070686V#805F奇怪了……\n',
            '找不到可以打开的地方。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550070687V仔细看连接缝都没有……\n',
            '到底是怎么组装起来的呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550070688V唔……\n',
            '这样的话很难调查里面啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070689V#007F哎～怎么会……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010070690V#501F啊，要不这样吧。\n',
            '把导力器的外壳切开不就好了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0550070691V#805F唔……\n',
            '这样的确是最简单方便的做法。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550070692V但这是指名送给\n',
            '卡西乌斯先生的东西，\n',
            '随便破坏的话还是有点说不过去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070693V#003F这、这倒也是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070694V#013F……………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020070695V#015F如果那位博士在的话，\n',
            '我想我们也许可以拜托他……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010070696V#004F啊……\n',
            '一起寄来的便条……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010070697V#006F的确，如果那位博士在的话，\n',
            '说不定会有办法呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0550070698V#802F？？？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0008, 400)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010070699V#002F其实，和那个导力器一起送来的\n',
            '还有这张便条……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔把寄给卡西乌斯的包裹里的便条交给工房长。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0008,
        (
            '#0550070700V#802F『委托Ｒ博士调查………』',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070701V#012F关于那个Ｒ博士，\n',
            '不知道您有什么线索吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0550070702V#802F线索嘛……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550070703V首字母是Ｒ，\n',
            '又是卡西乌斯先生认识的人，\n',
            '那就一定是『拉赛尔博士』了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070704V#015F果然是他吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010070705V#004F拉赛尔博士？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010070706V这么说……\n',
            '也是约修亚认识的人？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)
    Sleep(400)

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070707V#010F不，我没见过他。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020070708V不过我知道他是一位\n',
            '将导力技术带进利贝尔王国的名人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0550070709V#800F哦，你也知道啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0008, 400)
    ChrTurnDirection(0x0101, 0x0008, 400)
    Sleep(400)

    ChrTalk(
        0x0008,
        (
            '#0550070710V#803F导力器的发明者\n',
            '是一位名叫爱普斯泰恩的博士……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550070711V而拉赛尔博士就是\n',
            '那位爱普斯泰恩博士的\n',
            '嫡传弟子的其中一个。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550070712V４０年前，\n',
            '多亏他带回了导力器技术，\n',
            '才让利贝尔成为了先进的导力技术王国。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550070713V#800F因此，他可以称得上是\n',
            '利贝尔的『导力革命之父』呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070714V#004F哎哎……\n',
            '是那么厉害的人啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010070715V#007F老爸这家伙，\n',
            '竟然有这么了不起的人际关系。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0550070716V#803F但是，要把这个导力器交给博士……\n',
            '真是让人有点担心啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550070717V不知道会发生什么样的事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070718V#004F哎？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0550070719V#805F怎么说呢……\n',
            '他是个在好坏各方面都算得上天才的人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550070720V一旦燃起了研究之心，\n',
            '就会经常引起各种各样的事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550070721V#806F对了，\n',
            '导力飞艇刚开发出来的时候也是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550070722V#806F…………呼…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070723V#506F（为、为什么在眺望远方……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070724V#015F（看来以前发生过很多事……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0550070725V#803F……咳咳，失礼了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550070726V#800F总之，如果是博士的话，\n',
            '我想他应该能帮你们\n',
            '查清这个黑色导力器的真面目。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550070727V我帮你们引见一下，和他商量看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070728V#006F谢谢，工房长先生！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070729V#010F那我们到哪里\n',
            '才能见到拉赛尔博士呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0550070730V#800F这个啊……\n',
            '你们稍微等一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(500)
    ChrSetChipByIndex(0x0008, 0)
    ChrClearFlags(0x0008, 0x0010)
    ChrSetPos(0x0008, 1720, 0, 5540, 270)
    OP_0D()
    ChrSetDirection(0x0008, 0, 400)
    ChrWalkTo(0x0008, 1360, 0, 7250, 2000, 0x00)
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '玛多克工房长拨通了内线电话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0008,
        (
            '#0550070731V#800F喂喂……\n',
            '#802F哦，来得正好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550070732V其实我正要找你呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550070733V不好意思，\n',
            '能到我这里来一下吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550070734V#801F嗯、嗯，我等着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070735V#000F难道说，\n',
            '刚才是和那位拉赛尔博士通话吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0008, 180, 400)
    ChrWalkTo(0x0008, 1720, 0, 5540, 2000, 0x00)

    ChrTalk(
        0x0008,
        (
            '#0550070736V#800F不不，当然不是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550070737V其实，\n',
            '博士在城镇里有自己的工房。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550070738V那里全是最新式的设备，\n',
            '所以他一般都在那里做研究。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070739V#501F哦～\n',
            '真不愧是位天才博士啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010070740V#505F……咦？\n',
            '那么，刚才是和谁通话啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0550070741V#801F啊，其实拉赛尔博士的孙女\n',
            '也在中央工房工作哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550070742V所以嘛，\n',
            '我想拜托那孩子为你们带路。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070743V#004F那孩子？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0107,
        '女孩子的声音',
        (
            '#0070070744V#1P打扰了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(109, 0x00, 0x64)

    @scena.Lambda('lambda_7EB8')
    def lambda_7EB8():
        CameraMove(1170, 0, 3070, 2000)

        ExitThread()

    DispatchAsync(0x0107, 0x0003, lambda_7EB8)

    @scena.Lambda('lambda_7ED0')
    def lambda_7ED0():
        ChrTurnDirection(0x00FE, 0x0107, 400)
        Yield()

        Jump('lambda_7ED0')

    DispatchAsync2(0x0101, 0x0001, lambda_7ED0)

    @scena.Lambda('lambda_7EE1')
    def lambda_7EE1():
        ChrTurnDirection(0x00FE, 0x0107, 400)
        Yield()

        Jump('lambda_7EE1')

    DispatchAsync2(0x0102, 0x0001, lambda_7EE1)

    ChrClearFlags(0x0107, 0x0080)
    ChrSetRGBAMask(0x0107, 255, 255, 255, 0, 0)

    @scena.Lambda('lambda_7F02')
    def lambda_7F02():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0107, 0x0002, lambda_7F02)

    ChrWalkTo(0x0107, -800, 0, 1200, 3000, 0x00)
    ChrTurnDirection(0x0107, 0x0101, 400)

    ChrTalk(
        0x0101,
        (
            '#0010070745V#004F#2P咦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070746V#014F#2P你是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070070747V#064F咦咦……\n',
            '艾丝蒂尔姐姐、约修亚哥哥？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_7FA9')
    def lambda_7FA9():
        CameraMove(2680, 0, 4730, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_7FA9)

    @scena.Lambda('lambda_7FC1')
    def lambda_7FC1():
        ChrWalkTo(0x00FE, 400, 0, 3170, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0002, lambda_7FC1)

    WaitForThreadExit(0x0107, 0x0002)
    ChrTurnDirection(0x0107, 0x0101, 400)
    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0008,
        (
            '#0550070748V#802F怎么怎么？\n',
            '难道说你们认识吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070749V#006F#2P嗯。\n',
            '刚认识不久呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070750V#010F#2P这么说，\n',
            '她就是博士的孙女了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0550070751V#800F嗯，正是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0107, 400)
    Sleep(400)

    ChrTalk(
        0x0008,
        (
            '#0550070752V#800F提妲。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550070753V其实是这样的，\n',
            '艾丝蒂尔他们有事想找博士商量。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550070754V#800F能带他们去你家里吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0107, 0x0008, 400)

    ChrTalk(
        0x0107,
        (
            '#0070070755V#560F去见爷爷吗……\n',
            '嗯，好的，我知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0550070756V#801F那就拜托你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)
    ChrTurnDirection(0x0107, 0x0101, 400)
    Sleep(400)

    ChrTalk(
        0x0008,
        (
            '#0550070757V#800F对了，有什么发现的话，\n',
            '希望你们也能顺便告诉我一下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550070758V作为一个技术工作者，\n',
            '我对这个可是非常感兴趣哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    ChrTurnDirection(0x0102, 0x0008, 400)
    ChrTurnDirection(0x0101, 0x0008, 400)

    ChrTalk(
        0x0101,
        (
            '#0010070759V#001F啊哈哈，好的，我知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070760V#010F那么我们告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_28(0x003F, 0x01, 0x0004)
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T3114._SN', 102, 0, 0)
    IdleLoop()

    Return()

# id: 0x0010 offset: 0x82B5
@scena.Code('func_10_82B5')
def func_10_82B5():
    EventBegin(0x00)
    SetScenaFlags(ScenaFlag(0x00A9, 2, 0x54A))
    OP_64(0x00, 0x0001)
    OP_2B(0x0041, 0x0001)
    CameraMove(-101920, 0, 93750, 1000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 7, 0x52F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_86F6',
    )

    SetScenaFlags(ScenaFlag(0x00A5, 7, 0x52F))

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8352',
    )

    ChrTalk(
        0x0101,
        (
            '#0010080849V#004F啊……\n',
            '约修亚，这是！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080850V#012F是刚才所说的发烟筒。\n',
            '给我看看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8498')

    def _loc_8352(): pass

    label('loc_8352')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_83BF',
    )

    ChrTalk(
        0x0101,
        (
            '#0010080851V#004F啊……\n',
            '约修亚，那是！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080852V#012F嗯。\n',
            '是刚才所说的发烟筒。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8498')

    def _loc_83BF(): pass

    label('loc_83BF')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8430',
    )

    ChrTalk(
        0x0107,
        (
            '#0070080853V#065F啊……\n',
            '哥哥，这是！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080854V#012F是刚才所说的发烟筒。\n',
            '给我看看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8498')

    def _loc_8430(): pass

    label('loc_8430')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8498',
    )

    ChrTalk(
        0x0106,
        (
            '#0050080855V#057F这个……\n',
            '就是那发烟筒吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080856V#012F阿加特兄。\n',
            '给我看看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8498(): pass

    label('loc_8498')

    FadeOut(1000, 0, -1)
    OP_0D()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '约修亚很熟练地把发烟筒拆散了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    ChrSetPos(0x0102, -102470, 0, 94470, 135)
    ChrSetPos(0x0101, -102530, 0, 95560, 135)
    ChrSetPos(0x0107, -103610, 0, 94520, 135)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 1, 0x531)),
            Expr.Return,
        ),
        'loc_8514',
    )

    ChrSetPos(0x0106, -101550, 0, 95550, 225)

    def _loc_8514(): pass

    label('loc_8514')

    FadeIn(600, 0)
    StopEffect(0x01, 0x02)
    StopEffect(0x00, 0x02)
    Sleep(1000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 1, 0x531)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8608',
    )

    ChrTalk(
        0x0101,
        (
            '#0010080857V#501F哇……\n',
            '烟雾没有了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070080858V#560F约修亚哥哥，\n',
            '好厉害……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080859V#012F别的地方肯定还有\n',
            '和这个一样的发烟筒。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020080860V找到了就把它们拆散吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080861V#006FＯＫ！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_86F3')

    def _loc_8608(): pass

    label('loc_8608')

    SetScenaFlags(ScenaFlag(0x00A7, 6, 0x53E))

    ChrTalk(
        0x0101,
        (
            '#0010080862V#501F哇……\n',
            '烟雾没有了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070080863V#560F约修亚哥哥，\n',
            '好厉害……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050080864V#052F哦……\n',
            '还挺有两下子的嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080865V#012F别的地方肯定还有\n',
            '和这个一样的发烟筒。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020080866V找到了就把它们拆散吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_86F3(): pass

    label('loc_86F3')

    Jump('loc_8824')

    def _loc_86F6(): pass

    label('loc_86F6')

    FadeOut(600, 0, -1)

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
    ChrSetPos(0x0102, -102470, 0, 94470, 135)
    ChrSetPos(0x0101, -102530, 0, 95560, 135)
    ChrSetPos(0x0107, -103610, 0, 94520, 135)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 1, 0x531)),
            Expr.Return,
        ),
        'loc_877A',
    )

    ChrSetPos(0x0106, -101550, 0, 95550, 225)

    def _loc_877A(): pass

    label('loc_877A')

    StopEffect(0x01, 0x02)
    StopEffect(0x00, 0x02)
    Sleep(1000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 1, 0x531)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A7, 6, 0x53E)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_8824',
    )

    SetScenaFlags(ScenaFlag(0x00A7, 6, 0x53E))

    ChrTalk(
        0x0106,
        (
            '#0050080867V#052F哦……\n',
            '还挺有两下子的嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080868V#012F别的地方肯定还有\n',
            '和这个一样的发烟筒。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020080869V找到了就把它们拆散吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8824(): pass

    label('loc_8824')

    EventEnd(0x00)

    Return()

# id: 0x0011 offset: 0x8827
@scena.Code('func_11_8827')
def func_11_8827():
    FormationAddMember(0x0F, 0xFF)
    EventBegin(0x00)
    CameraMove(2860, 0, 5340, 0)
    CameraSetDistance(3200, 0)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrSetPos(0x0009, 2360, 0, 2680, 0)
    ChrSetPos(0x0110, 4670, 0, 3000, 270)
    ChrSetPos(0x000A, 250, 0, 2990, 90)
    ChrSetPos(0x000B, 250, 0, 2040, 90)
    ChrSetPos(0x0102, -820, 0, 5490, 135)
    ChrSetPos(0x0101, -540, 0, 4290, 90)
    ChrSetPos(0x0106, 230, 0, 5620, 180)
    ChrSetPos(0x0107, -1830, 0, 4760, 90)

    @scena.Lambda('lambda_88E3')
    def lambda_88E3():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_88E3')

    DispatchAsync2(0x0101, 0x0001, lambda_88E3)

    @scena.Lambda('lambda_88F4')
    def lambda_88F4():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_88F4')

    DispatchAsync2(0x0102, 0x0001, lambda_88F4)

    @scena.Lambda('lambda_8905')
    def lambda_8905():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_8905')

    DispatchAsync2(0x0107, 0x0001, lambda_8905)

    SetScenaFlags(ScenaFlag(0x00A6, 3, 0x533))
    FadeIn(2000, 0)
    OP_0D()

    ChrTalk(
        0x0009,
        (
            '#0610080971V#182F详细情况我明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610080972V不管怎么说，\n',
            '那些人可真是明目张胆地犯罪啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610080973V就算将这件事\n',
            '称为恐怖袭击事件也毫不为过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0550080974V#805F#1P恐怖袭击事件……\n',
            '怎、怎么会有这种事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0610080975V#181F用发烟筒制造混乱，\n',
            '绑架了王国智慧象征的博士……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610080976V而且还抢夺了\n',
            '王国最新技术的导力演算器。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610080977V所作所为不可原谅。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070080978V#063F………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050080979V#050F#1P说了那么多，\n',
            '究竟王国军方面准备怎么行动？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0610080980V#182F我们已经在艾尔·雷登、\n',
            '沃尔费堡垒、佐达特军用道\n',
            '以及圣海姆门等地实行严密的盘查。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610080981V只要我们布下天罗地网，\n',
            '绑架犯想逃出蔡斯地区也是空谈。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080982V#004F哎～\n',
            '的确是很高明的方法啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0610080983V#181F呵呵……\n',
            '对突发事件做出迅速果断的应对\n',
            '是我们情报部的基本职责。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080984V#012F有件事想请问一下……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020080985V据说那些犯人换装成亲卫队队员，\n',
            '并在大庭广众面前走出了中央工房。\n',
            '请问您对这一点有何看法？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0610080986V#182F那也是啊……\n',
            '这可说是相当严重的事态。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0110, 400)

    ChrTalk(
        0x0009,
        (
            '#0610080987V#181F这样的话……\n',
            '朵洛希·海娅特小姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0110, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    @scena.Lambda('lambda_8D53')
    def lambda_8D53():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_8D53')

    DispatchAsync2(0x0110, 0x0001, lambda_8D53)

    ChrTalk(
        0x0110,
        (
            '#0280080988V#153F#2P哎……？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280080989V是、是叫我吗～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0610080990V#182F听说案发的当时，\n',
            '你拍到了逃走的绑架犯的样子是吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610080991V这样说可能有点冒昧……\n',
            '那个感光结晶回路可以交给我们保管吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0110,
        (
            '#0280080992V#152F#2P咦！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280080993V但是但是，\n',
            '这可是超级难得的独家报道～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0610080994V#182F我并非打算包庇同僚，\n',
            '毕竟王室亲卫队是王国军的荣耀。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610080995V为了确保他们的清白，\n',
            '更是为了顾全女王陛下的名誉，\n',
            '在真相查明之前希望你们能做出客观的报道。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610080996V#181F虽然是非正式的请求，\n',
            '但这也是我们全体王国军的想法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0110,
        (
            '#0280080997V#154F#2P唔～没办法了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280080998V等真相大白之后，\n',
            '记得一定要还给我哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0110, 2980, 0, 2670, 2000, 0x00)
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '朵洛希把自己拍照专用的感光结晶回路\n',
            '交给了凯诺娜上尉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    ChrMoveTo(0x0110, 3570, 0, 2840, 2000, 0x00)

    ChrTalk(
        0x0009,
        (
            '#0610080999V#182F谢谢你的合作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0106, 400)

    ChrTalk(
        0x0009,
        (
            '#0610081000V#182F此外，虽然这样说有点失礼，\n',
            '但为了军方的调查能顺利进展下去，\n',
            '希望你们游击士协会也要限制一下行动……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050081001V#057F#1P这个办不到。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050081002V那些穿黑衣的家伙，\n',
            '我可是从很久以前就开始追查了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050081003V不是不给军队面子，\n',
            '只是我没理由在这时候撤手。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0610081004V#181F………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610081005V#182F唉，没办法。\n',
            '那就请继续调查下去吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610081006V我们军方和协会向来有合作关系。\n',
            '总之，如果发现了什么，\n',
            '请务必向雷斯顿要塞的情报部报告。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050081007V#051F#1P知道了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050081008V你们如果查到了什么，\n',
            '也麻烦联络一下蔡斯支部。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0610081009V#182F明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610081010V#181F那么我们就告辞了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x000A, 0x0040)
    ChrSetFlags(0x000B, 0x0040)
    ChrSetFlags(0x0009, 0x0040)
    ChrSetDirection(0x0009, 225, 400)

    @scena.Lambda('lambda_931E')
    def lambda_931E():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_931E')

    DispatchAsync2(0x000A, 0x0001, lambda_931E)

    @scena.Lambda('lambda_932F')
    def lambda_932F():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_932F')

    DispatchAsync2(0x000B, 0x0001, lambda_932F)

    @scena.Lambda('lambda_9340')
    def lambda_9340():
        CameraMove(640, 0, 1650, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_9340)

    ChrWalkTo(0x0009, -980, 0, 490, 2000, 0x00)
    CreateThread(0x0009, 0x01, 0x00, func_12_9830)
    CreateThread(0x000A, 0x01, 0x00, func_13_987A)
    CreateThread(0x000B, 0x01, 0x00, func_14_98CE)
    WaitForThreadExit(0x000A, 0x0001)
    TerminateThread(0x0110, 0xFF)
    TerminateThread(0x0106, 0xFF)
    CameraMove(190, 0, 5120, 1500)

    ChrTalk(
        0x0101,
        (
            '#0010081011V#505F呼……\n',
            '真、真是觉得好紧张啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010081012V刚才那个女人是\n',
            '理查德上校的副官凯诺娜上尉吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020081013V#010F#3P嗯，没错。\n',
            '应该是代替上校前来调查的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050081014V#552F哼……\n',
            '我可是怎样都和当兵的合不来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0106, 0x0107, 400)

    ChrTalk(
        0x0106,
        (
            '#0050081015V#050F算了，不管王国军如何做出行动，\n',
            '总之那些黑衣人一定还\n',
            '潜伏在蔡斯地区的某个地方。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050081016V向协会报告之后，\n',
            '我们就到城镇外面好好搜索吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_9530')
    def lambda_9530():
        ChrTurnDirection(0x00FE, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_9530)

    @scena.Lambda('lambda_953E')
    def lambda_953E():
        ChrTurnDirection(0x00FE, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_953E)

    @scena.Lambda('lambda_954C')
    def lambda_954C():
        ChrTurnDirection(0x00FE, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_954C)

    @scena.Lambda('lambda_955A')
    def lambda_955A():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0110, 0x0001, lambda_955A)

    ChrTalk(
        0x0101,
        (
            '#0010081017V#004F也好……等等。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010081018V#009F你吃错药啦，\n',
            '这次怎么不说要我们别跟去之类的话？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050081019V#051F啊啊。\n',
            '你们看起来似乎还有点用处。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050081020V就让你们做我的助手好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010081021V#509F看来你那种嚣张的性格是不会改的～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010081022V#007F算了，已经习惯了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020081023V#010F那就请多指教了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050081024V#053F啊啊，可别大意了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0106, 0x0008, 400)

    ChrTalk(
        0x0106,
        (
            '#0050081025V#050F工房长，\n',
            '那么我们就出发了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0008, 2)
    Sleep(400)

    ChrTalk(
        0x0008,
        (
            '#0550081026V#800F啊……拜托你们了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550081027V#803F无论如何……\n',
            '请你们一定要救出博士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070081028V#063F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    ChrSetSubChip(0x0008, 0)
    ChrSetPos(0x0101, -1150, 0, 2880, 180)
    ChrSetPos(0x0102, -1150, 0, 2880, 180)
    ChrSetPos(0x0107, -1150, 0, 2880, 180)
    ChrSetPos(0x0106, -1150, 0, 2880, 180)
    ChrSetPos(0x0110, -1150, 0, 2880, 180)
    CameraMove(-1150, 0, 2880, 0)
    CameraSetDistance(3000, 0)
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x0012 offset: 0x9830
@scena.Code('func_12_9830')
def func_12_9830():
    ChrWalkTo(0x00FE, -900, 0, 300, 2000, 0x00)
    PlaySE(109, 0x00, 0x64)

    @scena.Lambda('lambda_984F')
    def lambda_984F():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_984F)

    ChrSetFlags(0x00FE, 0x0004)
    ChrWalkTo(0x00FE, -900, 0, -2480, 2000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x0013 offset: 0x987A
@scena.Code('func_13_987A')
def func_13_987A():
    Sleep(300)

    Sleep(300)

    ChrWalkTo(0x00FE, -1070, 0, -260, 2000, 0x00)

    @scena.Lambda('lambda_989E')
    def lambda_989E():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_989E)

    ChrSetFlags(0x00FE, 0x0004)
    ChrWalkTo(0x00FE, -1220, 0, -2480, 2000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)
    PlaySE(109, 0x00, 0x64)

    Return()

# id: 0x0014 offset: 0x98CE
@scena.Code('func_14_98CE')
def func_14_98CE():
    Sleep(300)

    ChrWalkTo(0x00FE, -1070, 0, -260, 2000, 0x00)

    @scena.Lambda('lambda_98ED')
    def lambda_98ED():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_98ED)

    ChrSetFlags(0x00FE, 0x0004)
    ChrWalkTo(0x00FE, -1220, 0, -2480, 2000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x0015 offset: 0x9918
@scena.Code('func_15_9918')
def func_15_9918():
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

    If(
        (
            (Expr.Eval, "OP_40(0x0356)"),
            Expr.Return,
        ),
        'loc_99D3',
    )

    FadeOut(300, 0, 100)
    PlaySE(115, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '使用了',
            (TxtCtl.SetColor, 0x2),
            '里面房间的钥匙',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_71(0x0000, 0x0010)
    OP_64(0x01, 0x0001)
    RemoveItem(0x0356, 1)
    OP_28(0x002C, 0x01, 0x8000)
    OP_65(0x06, 0x0001)

    Jump('loc_9B1E')

    def _loc_99D3(): pass

    label('loc_99D3')

    If(
        (
            (Expr.Eval, "OP_42(0x003B)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_29(0x002C, 0x01, 0x0100)"),
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x002C, 0x01, 0x0400)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_9B1E',
    )

    PlaySE(402, 0x00, 0x64)

    ChrTalk(
        0x013C,
        (
            '#2030181135V喵呀～～呵。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_9A1B')
    def lambda_9A1B():
        ChrTurnDirection(0x0102, 0x013C, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_9A1B)

    @scena.Lambda('lambda_9A29')
    def lambda_9A29():
        ChrTurnDirection(0x0107, 0x013C, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_9A29)

    ChrTurnDirection(0x0101, 0x013C, 400)

    ChrTalk(
        0x0101,
        (
            '#0010181136V#002F……在这里面吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x013C, 0x0101, 400)
    PlaySE(402, 0x00, 0x64)

    ChrTalk(
        0x013C,
        (
            '#2030181137V喵～噢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020181138V#012F找一下钥匙吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020181139V应该就在这个房间里的某个地方。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010181140V#002F嗯，明白。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_65(0x02, 0x0001)
    OP_65(0x03, 0x0001)
    OP_65(0x04, 0x0001)
    OP_65(0x05, 0x0001)
    OP_28(0x002C, 0x01, 0x0400)

    def _loc_9B1E(): pass

    label('loc_9B1E')

    TalkEnd(0x00FF)

    Return()

# id: 0x0016 offset: 0x9B22
@scena.Code('func_16_9B22')
def func_16_9B22():
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '调查了书架。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '没有找到什么特别的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0017 offset: 0x9B74
@scena.Code('func_17_9B74')
def func_17_9B74():
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '调查了资料。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '没有找到什么特别的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0018 offset: 0x9BC6
@scena.Code('func_18_9BC6')
def func_18_9BC6():
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '调查了笔筒。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '没有找到什么特别的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0019 offset: 0x9C18
@scena.Code('func_19_9C18')
def func_19_9C18():
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '调查了桌子上的书。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(17, 0x00, 0x64)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '里面房间的钥匙',
            (TxtCtl.SetColor, 0x0),
            '找到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_28(0x002C, 0x01, 0x0800)
    AddItem(0x0356, 1)
    OP_64(0x02, 0x0001)
    OP_64(0x03, 0x0001)
    OP_64(0x04, 0x0001)
    OP_64(0x05, 0x0001)
    TalkEnd(0x00FF)

    Return()

# id: 0x001A offset: 0x9C9B
@scena.Code('func_1A_9C9B')
def func_1A_9C9B():
    EventBegin(0x00)
    Fade(1000)
    CameraMove(710, 0, 100700, 0)
    ChrSetPos(0x0101, 60, 0, 101680, 189)
    ChrSetPos(0x0102, 780, 0, 102660, 179)

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9CF4',
    )

    ChrSetPos(0x0107, -600, 0, 102530, 168)

    def _loc_9CF4(): pass

    label('loc_9CF4')

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9D13',
    )

    ChrSetPos(0x0106, 120, 0, 102990, 182)

    def _loc_9D13(): pass

    label('loc_9D13')

    If(
        (
            (Expr.Eval, "OP_42(0x003B)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9D32',
    )

    ChrSetPos(0x013C, -1020, 0, 101070, 101)

    def _loc_9D32(): pass

    label('loc_9D32')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_9D4C',
    )

    @scena.Lambda('lambda_9D44')
    def lambda_9D44():
        ChrTurnDirection(0x0000, 0x0016, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_9D44)

    def _loc_9D4C(): pass

    label('loc_9D4C')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_9D66',
    )

    @scena.Lambda('lambda_9D5E')
    def lambda_9D5E():
        ChrTurnDirection(0x0001, 0x0016, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_9D5E)

    def _loc_9D66(): pass

    label('loc_9D66')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_9D80',
    )

    @scena.Lambda('lambda_9D78')
    def lambda_9D78():
        ChrTurnDirection(0x0002, 0x0016, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_9D78)

    def _loc_9D80(): pass

    label('loc_9D80')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x3),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_9D9A',
    )

    @scena.Lambda('lambda_9D92')
    def lambda_9D92():
        ChrTurnDirection(0x0003, 0x0016, 400)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_9D92)

    def _loc_9D9A(): pass

    label('loc_9D9A')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x4),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_9DB4',
    )

    @scena.Lambda('lambda_9DAC')
    def lambda_9DAC():
        ChrTurnDirection(0x0004, 0x0016, 400)

        ExitThread()

    DispatchAsync(0x0004, 0x0001, lambda_9DAC)

    def _loc_9DB4(): pass

    label('loc_9DB4')

    OP_0D()
    Sleep(400)

    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '烟草',
            (TxtCtl.SetColor, 0x0),
            '找到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(400)

    OP_62(0x0101, 0x00000000, 2000, 0x08, 0x09, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(800)

    ChrTalk(
        0x0101,
        (
            '#0010181141V#001F哈哈，找到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181142V#010F是啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070181143V#561F没想到犯人竟然是工房长先生……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0107, 400)

    ChrTalk(
        0x0101,
        (
            '#0010181144V#003F嗯，预料之外呢～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010181145V果真是人不可貌相……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x0008, 0x0080)
    ChrSetChipByIndex(0x0008, 0)
    ChrClearFlags(0x0008, 0x0004)
    ChrClearFlags(0x0008, 0x0010)

    @scena.Lambda('lambda_9F03')
    def lambda_9F03():
        ChrSetRGBAMask(0x0008, 255, 255, 255, 0, 0)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_9F03)

    ChrSetPos(0x0008, -3380, 0, 98500, 0)

    ChrTalk(
        0x0008,
        (
            '#0550181146V你、你们几个！搞错了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x0008, 0x0080)
    OP_62(0x0008, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    @scena.Lambda('lambda_9F65')
    def lambda_9F65():
        ChrSetRGBAMask(0x0008, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_9F65)

    ChrWalkTo(0x0008, -2120, 0, 101760, 4000, 0x00)

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_9F9F',
    )

    @scena.Lambda('lambda_9F97')
    def lambda_9F97():
        ChrTurnDirection(0x0000, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_9F97)

    def _loc_9F9F(): pass

    label('loc_9F9F')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_9FB9',
    )

    @scena.Lambda('lambda_9FB1')
    def lambda_9FB1():
        ChrTurnDirection(0x0001, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_9FB1)

    def _loc_9FB9(): pass

    label('loc_9FB9')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_9FD3',
    )

    @scena.Lambda('lambda_9FCB')
    def lambda_9FCB():
        ChrTurnDirection(0x0002, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_9FCB)

    def _loc_9FD3(): pass

    label('loc_9FD3')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x3),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_9FED',
    )

    @scena.Lambda('lambda_9FE5')
    def lambda_9FE5():
        ChrTurnDirection(0x0003, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_9FE5)

    def _loc_9FED(): pass

    label('loc_9FED')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x4),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_A007',
    )

    @scena.Lambda('lambda_9FFF')
    def lambda_9FFF():
        ChrTurnDirection(0x0004, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0004, 0x0001, lambda_9FFF)

    def _loc_A007(): pass

    label('loc_A007')

    ChrTurnDirection(0x0008, 0x0101, 400)
    OP_62(0x0008, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(400)

    ChrTalk(
        0x0008,
        (
            '#0550181147V#805F不、不要误会啊！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550181148V就、就抽一支嘛，\n',
            '马上就还回去……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181149V#015F工房长…………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020181150V想要解释的话，\n',
            '就请去找米妮亚姆医生吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    OP_28(0x002C, 0x01, 0x1000)
    SetScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    NewScene('ED6_DT01/T3118._SN', 100, 0, 0)
    IdleLoop()
    OP_64(0x06, 0x0001)
    EventEnd(0x00)

    Return()

# id: 0x001B offset: 0xA0F9
@scena.Code('func_1B_A0F9')
def func_1B_A0F9():
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '书架上放着《哈茨少年冒险记·上》。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
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
        1,
        (
            TXT(0x00, '【阅读】\n'),
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
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A1A3',
    )

    OP_B9(0x0374, 0x0000)

    def _loc_A1A3(): pass

    label('loc_A1A3')

    TalkEnd(0x00FF)

    Return()

# id: 0x001C offset: 0xA1A7
@scena.Code('func_1C_A1A7')
def func_1C_A1A7():
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '书架上放着《哈茨少年冒险记·下》。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
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
        1,
        (
            TXT(0x00, '【阅读】\n'),
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
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A251',
    )

    OP_B9(0x0344, 0x0000)

    def _loc_A251(): pass

    label('loc_A251')

    TalkEnd(0x00FF)

    Return()

# id: 0x001D offset: 0xA255
@scena.Code('func_1D_A255')
def func_1D_A255():
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '书架上放着《结晶光学论集》。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
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
        1,
        (
            TXT(0x00, '【阅读】\n'),
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
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A2F9',
    )

    OP_B9(0x0342, 0x0000)

    def _loc_A2F9(): pass

    label('loc_A2F9')

    TalkEnd(0x00FF)

    Return()

# id: 0x001E offset: 0xA2FD
@scena.Code('func_1E_A2FD')
def func_1E_A2FD():
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '书架上放着《明日料理》。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
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
        1,
        (
            TXT(0x00, '【阅读】\n'),
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
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A39D',
    )

    OP_B9(0x0341, 0x0000)

    def _loc_A39D(): pass

    label('loc_A39D')

    TalkEnd(0x00FF)

    Return()

# id: 0x001F offset: 0xA3A1
@scena.Code('func_1F_A3A1')
def func_1F_A3A1():
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '书架上放着《猫语日常会话入门》。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
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
        1,
        (
            TXT(0x00, '【阅读】\n'),
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
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A449',
    )

    OP_B9(0x0340, 0x0000)

    def _loc_A449(): pass

    label('loc_A449')

    TalkEnd(0x00FF)

    Return()

# id: 0x0020 offset: 0xA44D
@scena.Code('func_20_A44D')
def func_20_A44D():
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '书架上放着《艾尔贝啄木鸟的生态》。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
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
        1,
        (
            TXT(0x00, '【阅读】\n'),
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
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A4F7',
    )

    OP_B9(0x0343, 0x0000)

    def _loc_A4F7(): pass

    label('loc_A4F7')

    TalkEnd(0x00FF)

    Return()

# id: 0x0021 offset: 0xA4FB
@scena.Code('func_21_A4FB')
def func_21_A4FB():
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '书架上放着《３１棵丝柏树》。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
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
        1,
        (
            TXT(0x00, '【阅读】\n'),
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
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A59F',
    )

    OP_B9(0x0345, 0x0000)

    def _loc_A59F(): pass

    label('loc_A59F')

    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
