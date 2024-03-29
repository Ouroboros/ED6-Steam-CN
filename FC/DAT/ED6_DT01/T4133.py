import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T4133_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4133   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4133.x'
    header.mapIndex       = 1
    header.bgm            = 84
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
        ('ED6_DT07/CH01540._CH', 'ED6_DT07/CH01540P._CP'),
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
        ('ED6_DT07/CH00100._CH', 'ED6_DT07/CH00100P._CP'),
        ('ED6_DT07/CH00110._CH', 'ED6_DT07/CH00110P._CP'),
        ('ED6_DT07/CH01220._CH', 'ED6_DT07/CH01220P._CP'),
        ('ED6_DT07/CH02390._CH', 'ED6_DT07/CH02390P._CP'),
        ('ED6_DT07/CH02550._CH', 'ED6_DT07/CH02550P._CP'),
        ('ED6_DT07/CH00040._CH', 'ED6_DT07/CH00040P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH02600._CH', 'ED6_DT07/CH02600P._CP'),
        ('ED6_DT07/CH01620._CH', 'ED6_DT07/CH01620P._CP'),
        ('ED6_DT06/CH20021._CH', 'ED6_DT06/CH20021P._CP'),
        ('ED6_DT07/CH00015._CH', 'ED6_DT07/CH00015P._CP'),
        ('ED6_DT07/CH01030._CH', 'ED6_DT07/CH01030P._CP'),
        ('ED6_DT07/CH01070._CH', 'ED6_DT07/CH01070P._CP'),
        ('ED6_DT07/CH01043._CH', 'ED6_DT07/CH01043P._CP'),
        ('ED6_DT07/CH02480._CH', 'ED6_DT07/CH02480P._CP'),
        ('ED6_DT07/CH02490._CH', 'ED6_DT07/CH02490P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT07/CH01150._CH', 'ED6_DT07/CH01150P._CP'),
        ('ED6_DT07/CH01690._CH', 'ED6_DT07/CH01690P._CP'),
        ('ED6_DT07/CH01630._CH', 'ED6_DT07/CH01630P._CP'),
    ]

# id: 0x10001 offset: 0x15A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '士兵',
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
            name                = '士兵',
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
            name                = '福立兹',
            x                   = 7410,
            z                   = 0,
            y                   = 3300,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '乔儿',
            x                   = 3020,
            z                   = 0,
            y                   = 1290,
            direction           = 119,
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
            name                = '汉斯',
            x                   = 3390,
            z                   = 0,
            y                   = -390,
            direction           = 36,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '科洛丝',
            x                   = 4740,
            z                   = 0,
            y                   = 960,
            direction           = 225,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '科林兹校长',
            x                   = 4970,
            z                   = 0,
            y                   = -600,
            direction           = 309,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '克鲁茨',
            x                   = 36400,
            z                   = 0,
            y                   = 111030,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '卡拉',
            x                   = 100960,
            z                   = 0,
            y                   = 113420,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '卢希娅',
            x                   = 97040,
            z                   = 0,
            y                   = 114630,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            name                = '米亚尔',
            x                   = 157590,
            z                   = 250,
            y                   = 55130,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x01D5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            name                = '帕菲',
            x                   = -26610,
            z                   = 0,
            y                   = 55500,
            direction           = 290,
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
            name                = '娜娜',
            x                   = -27940,
            z                   = 0,
            y                   = 55480,
            direction           = 90,
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
            name                = '阿鲁姆',
            x                   = 155000,
            z                   = 0,
            y                   = 114600,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 18,
            chipIndex           = 18,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '艾娅莉',
            x                   = 158680,
            z                   = 0,
            y                   = 110910,
            direction           = 190,
            word_0E             = 0,
            dword_10            = 19,
            chipIndex           = 19,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0011,
        ),
        ScenaNpcData(
            name                = '索菲娜',
            x                   = 35100,
            z                   = 0,
            y                   = 53750,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 20,
            chipIndex           = 20,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0012,
        ),
        ScenaNpcData(
            name                = '亚妮拉丝',
            x                   = 93210,
            z                   = 0,
            y                   = 53470,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 21,
            chipIndex           = 21,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            name                = '信',
            x                   = -24660,
            z                   = -200,
            y                   = 175270,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1114123,
            chipIndex           = 11,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x39A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x39A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x39A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 57010,
            triggerZ            = 0,
            triggerY            = 3770,
            triggerRange        = 800,
            actorX              = 57010,
            actorZ              = 1000,
            actorY              = 3770,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0016,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 7200,
            triggerZ            = 0,
            triggerY            = 1690,
            triggerRange        = 800,
            actorX              = 7410,
            actorZ              = 1500,
            actorY              = 3300,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 7000,
            triggerZ            = 0,
            triggerY            = 4890,
            triggerRange        = 800,
            actorX              = 7000,
            actorZ              = 1000,
            actorY              = 4890,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x001A,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x406
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_414',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, func_14_1E10)

    def _loc_414(): pass

    label('loc_414')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 3, 0x3FB)),
            Expr.Return,
        ),
        'loc_427',
    )

    MapSetFlags(0x10000000)
    ClearScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    Event(0, func_15_2217)

    def _loc_427(): pass

    label('loc_427')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 4, 0x3FC)),
            Expr.Return,
        ),
        'loc_43A',
    )

    MapSetFlags(0x10000000)
    ClearScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    Event(0, func_18_430C)

    def _loc_43A(): pass

    label('loc_43A')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x0000007A, 'loc_446'),
        (-1, 'loc_459'),
    )

    def _loc_446(): pass

    label('loc_446')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 3, 0x62B)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 2, 0x62A)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_456',
    )

    Event(0, func_17_35F6)

    def _loc_456(): pass

    label('loc_456')

    Jump('loc_459')

    def _loc_459(): pass

    label('loc_459')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_477',
    )

    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000E, 0x0080)

    Jump('loc_5A7')

    def _loc_477(): pass

    label('loc_477')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_486',
    )

    ChrClearFlags(0x0012, 0x0080)

    Jump('loc_5A7')

    def _loc_486(): pass

    label('loc_486')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_490',
    )

    Jump('loc_5A7')

    def _loc_490(): pass

    label('loc_490')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_49A',
    )

    Jump('loc_5A7')

    def _loc_49A(): pass

    label('loc_49A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_4A4',
    )

    Jump('loc_5A7')

    def _loc_4A4(): pass

    label('loc_4A4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 1, 0x629)),
            Expr.Return,
        ),
        'loc_502',
    )

    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x000F, 34910, 0, 113190, 0)
    CreateThread(0x000F, 0x00, 0x00, func_02_5EB)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0012, 0x0080)
    ChrClearFlags(0x0013, 0x0080)
    ChrSetFlags(0x0013, 0x0010)
    ChrClearFlags(0x0014, 0x0080)
    ChrSetFlags(0x0014, 0x0010)
    ChrClearFlags(0x0015, 0x0080)
    ChrClearFlags(0x0016, 0x0080)
    ChrClearFlags(0x0017, 0x0080)
    ChrClearFlags(0x0018, 0x0080)

    Jump('loc_5A7')

    def _loc_502(): pass

    label('loc_502')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_529',
    )

    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x000F, 154870, 0, 51420, 339)
    CreateThread(0x000F, 0x00, 0x00, func_03_601)

    Jump('loc_5A7')

    def _loc_529(): pass

    label('loc_529')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_533',
    )

    Jump('loc_5A7')

    def _loc_533(): pass

    label('loc_533')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_55A',
    )

    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x000F, 154870, 0, 51420, 339)
    CreateThread(0x000F, 0x00, 0x00, func_03_601)

    Jump('loc_5A7')

    def _loc_55A(): pass

    label('loc_55A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 7, 0x617)),
            Expr.Return,
        ),
        'loc_58C',
    )

    ChrClearFlags(0x0013, 0x0080)
    ChrSetFlags(0x0013, 0x0010)
    ChrClearFlags(0x0014, 0x0080)
    ChrSetFlags(0x0014, 0x0010)
    ChrClearFlags(0x0017, 0x0080)
    ChrClearFlags(0x0015, 0x0080)
    ChrClearFlags(0x0016, 0x0080)
    ChrClearFlags(0x0012, 0x0080)

    Jump('loc_5A7')

    def _loc_58C(): pass

    label('loc_58C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_596',
    )

    Jump('loc_5A7')

    def _loc_596(): pass

    label('loc_596')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_5A0',
    )

    Jump('loc_5A7')

    def _loc_5A0(): pass

    label('loc_5A0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_5A7',
    )

    def _loc_5A7(): pass

    label('loc_5A7')

    Return()

# id: 0x0001 offset: 0x5A8
@scena.Code('func_01_5A8')
def func_01_5A8():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 0, 0x628)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 3, 0x62B)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5BC',
    )

    OP_1B(0x00, 0x00, 0x0019)

    Jump('loc_5CD')

    def _loc_5BC(): pass

    label('loc_5BC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 7, 0x617)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 0, 0x618)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5CD',
    )

    OP_1B(0x00, 0x00, 0x0019)

    def _loc_5CD(): pass

    label('loc_5CD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 0, 0x618)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 2, 0x62A)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 1, 0x629)),
            Expr.Nez64,
            Expr.Or,
            Expr.Return,
        ),
        'loc_5E6',
    )

    OP_72(0x0012, 0x0010)

    Jump('loc_5EA')

    def _loc_5E6(): pass

    label('loc_5E6')

    OP_64(0x00, 0x0001)

    def _loc_5EA(): pass

    label('loc_5EA')

    Return()

# id: 0x0002 offset: 0x5EB
@scena.Code('func_02_5EB')
def func_02_5EB():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_600',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_5EB')

    def _loc_600(): pass

    label('loc_600')

    Return()

# id: 0x0003 offset: 0x601
@scena.Code('func_03_601')
def func_03_601():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_624',
    )

    OP_8D(0x00FE, 153520, 48510, 156020, 53700, 3000)

    Jump('func_03_601')

    def _loc_624(): pass

    label('loc_624')

    Return()

# id: 0x0004 offset: 0x625
@scena.Code('func_04_625')
def func_04_625():
    TalkBegin(0x00FE)

    ChrTalk(
        0x000E,
        (
            '#0530850026V#780F我和学院的学生代表乔儿还有汉斯一起\n',
            '来参加诞辰庆典了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0x67B
@scena.Code('func_05_67B')
def func_05_67B():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_6E2',
    )

    ChrTalk(
        0x0105,
        (
            '#0060140798V#040F艾丝蒂尔、约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060140799V能够遇到你们两个，\n',
            '我真是太幸福了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_92E')

    def _loc_6E2(): pass

    label('loc_6E2')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '#0060140785V#040F艾丝蒂尔、约修亚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140786V#000F科洛丝，原来你在这里啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0060940009V#040F啊，\n',
            '我听说校长、乔儿和汉斯他们都来这里了……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060140788V所以就从王城里面偷偷跑了出来。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊哈哈，真看不出来，\n',
            '科洛丝你也会做出这么大胆的行动呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#040F呵呵，这次真是多谢你们了。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060140791V我从头到尾一直都承蒙你们两位的关照。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯～\n',
            '我觉得倒是科洛丝你教会了我许多东西。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010140793V待人温柔，意志坚强……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '对不起，我不太会说话，\n',
            '所以说不出什么好的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '总之，我们以后继续像现在这样\n',
            '互相帮助、一起努力就可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#040F艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_92E(): pass

    label('loc_92E')

    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0x932
@scena.Code('func_06_932')
def func_06_932():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_9C6',
    )

    ChrTalk(
        0x00FE,
        (
            '#0521220003V#730F虽然发生了许多的事情，\n',
            '不过看到你这么有精神，我就放心了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520140816V如果再到卢安来的话，\n',
            '记得到学院来玩玩哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B7C')

    def _loc_9C6(): pass

    label('loc_9C6')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '#0520140808V#730F哟，约修亚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F这不是汉斯吗。\n',
            '你在这里做什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0521220002V#730F在这里做什么……\n',
            '这么久没见面了，\n',
            '你却说出这样绝情的话来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '自从学园祭之后，\n',
            '又回到独自过夜的生活真是寂寞啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '因为对你难以忘怀，\n',
            '所以千里迢迢追到王都来了哦。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F哈哈，你还是老样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0520140815V#730F嗯，虽然发生了许多的事情，\n',
            '不过看到你这么有精神，我就放心了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520140816V如果再到卢安来的话，\n',
            '记得到学院来玩玩哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B7C(): pass

    label('loc_B7C')

    TalkEnd(0x00FE)

    Return()

# id: 0x0007 offset: 0xB80
@scena.Code('func_07_B80')
def func_07_B80():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_BED',
    )

    ChrTalk(
        0x00FE,
        (
            '#0510140806V#640F我从科洛丝那里听说了，\n',
            '你们这次真是大显神威啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '不愧是红骑士尤利乌斯哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CB5')

    def _loc_BED(): pass

    label('loc_BED')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '#0510140800V#640F艾丝蒂尔、约修亚！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊，乔儿！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#640F好久不见了啦～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510140803V我从科洛丝那里听说了，\n',
            '你们这次真是大显神威啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '不愧是红骑士尤利乌斯哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊哈哈……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_CB5(): pass

    label('loc_CB5')

    TalkEnd(0x00FE)

    Return()

# id: 0x0008 offset: 0xCB9
@scena.Code('func_08_CB9')
def func_08_CB9():
    Call(0, 0x0009)

    Return()

# id: 0x0009 offset: 0xCBE
@scena.Code('func_09_CBE')
def func_09_CBE():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_D38',
    )

    ChrTalk(
        0x000A,
        (
            '不愧是诞辰庆典啊，\n',
            '比武术大会还要热闹许多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '从外国来的客人\n',
            '也比历年的要多很多，\n',
            '真是快忙不过来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1534')

    def _loc_D38(): pass

    label('loc_D38')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_D6F',
    )

    ChrTalk(
        0x000A,
        (
            '真是奇怪，\n',
            '这个时间王城的城门却紧闭着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1534')

    def _loc_D6F(): pass

    label('loc_D6F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_E26',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_DC6',
    )

    ChrTalk(
        0x000A,
        (
            '刚才游击士\n',
            '克鲁茨先生回来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '但他的脸色\n',
            '似乎不是很好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E23')

    def _loc_DC6(): pass

    label('loc_DC6')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x000A,
        (
            '刚才游击士\n',
            '克鲁茨先生回来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '但他的脸色\n',
            '似乎不是很好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '应该没事吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E23(): pass

    label('loc_E23')

    Jump('loc_1534')

    def _loc_E26(): pass

    label('loc_E26')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_FB7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_E9E',
    )

    ChrTalk(
        0x000A,
        (
            '恭喜你们二人取得\n',
            '这次武术大会的优胜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '你们就不用在意\n',
            '这边的安排了。\n',
            '请好好享受王城的晚宴吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FB4')

    def _loc_E9E(): pass

    label('loc_E9E')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x0101,
        (
            '#000F啊，福立兹先生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '哦，艾丝蒂尔小姐，\n',
            '有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F今天晚上我们准备住在别的地方了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '嗯，\n',
            '之前艾南先生已经告知我了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '恭喜你们取得\n',
            '武术大会的优胜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '不用在意这边的安排，\n',
            '请好好享受王城的晚宴吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F不愧是艾南先生啊，\n',
            '动作这么快。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_FB4(): pass

    label('loc_FB4')

    Jump('loc_1534')

    def _loc_FB7(): pass

    label('loc_FB7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_1037',
    )

    ChrTalk(
        0x000A,
        (
            '艾丝蒂尔小姐，约修亚先生，\n',
            '今天是武术大会的决赛吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '请两位比赛\n',
            '一定要加油。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '我会在这里默默支持你们的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1534')

    def _loc_1037(): pass

    label('loc_1037')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 1, 0x629)),
            Expr.Return,
        ),
        'loc_10A4',
    )

    ChrTalk(
        0x000A,
        (
            '外面有很多的士兵\n',
            '在到处巡逻。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '刚才外出的客人\n',
            '都被他们以禁止夜间外出的理由\n',
            '强行送了回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1534')

    def _loc_10A4(): pass

    label('loc_10A4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_11C2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1126',
    )

    ChrTalk(
        0x000A,
        (
            '听说从今天起\n',
            '士兵就要严加巡逻了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '虽然给你们带来种种不便，\n',
            '但是请不要在外面待得太晚，\n',
            '一定要早点回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11BF')

    def _loc_1126(): pass

    label('loc_1126')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x000A,
        (
            '刚才收到了\n',
            '王国军发来的联络……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '听说从今天起\n',
            '他们就要严加巡逻了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '虽然给你们带来种种不便，\n',
            '但是请不要在外面待得太晚，\n',
            '一定要早点回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_11BF(): pass

    label('loc_11BF')

    Jump('loc_1534')

    def _loc_11C2(): pass

    label('loc_11C2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_11E8',
    )

    ChrTalk(
        0x000A,
        (
            '出去的时候请务必小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1534')

    def _loc_11E8(): pass

    label('loc_11E8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_12C6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1245',
    )

    ChrTalk(
        0x000A,
        (
            '对了，\n',
            '还有另外两位游击士\n',
            '现在也住在酒店里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '你们见到他们了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12C3')

    def _loc_1245(): pass

    label('loc_1245')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x000A,
        (
            '艾丝蒂尔小姐，约修亚先生，\n',
            '欢迎你们回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '对了，\n',
            '还有另外两位游击士\n',
            '现在也住在酒店里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '你们见到他们了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_12C3(): pass

    label('loc_12C3')

    Jump('loc_1534')

    def _loc_12C6(): pass

    label('loc_12C6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_12FD',
    )

    ChrTalk(
        0x000A,
        (
            '两位打算外出吗？\n',
            '出去的时候请务必小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1534')

    def _loc_12FD(): pass

    label('loc_12FD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_14BD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 7, 0x617)),
            Expr.Return,
        ),
        'loc_1367',
    )

    ChrTalk(
        0x000A,
        (
            '两位的房间\n',
            '在楼上走廊尽头的\n',
            '２０２号室。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '如果有什么需要的话，\n',
            '请来前台告诉我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_14BA')

    def _loc_1367(): pass

    label('loc_1367')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_13F0',
    )

    ChrTalk(
        0x000A,
        (
            '尊敬的客人，非常抱歉。\n',
            '现在还不能为你们安排房间，\n',
            '因为房间还没有清扫完毕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '想要在这里登记住宿的话，\n',
            '请三点以后再来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_14BA')

    def _loc_13F0(): pass

    label('loc_13F0')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x000A,
        (
            '尊敬的客人，非常抱歉。\n',
            '现在还不能为你们安排房间，\n',
            '因为房间还没有清扫完毕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '想要在这里登记住宿的话，\n',
            '请三点以后再来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F待会儿来登记吧，\n',
            '还是先去找到金先生再说。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000FＯＫ。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_14BA(): pass

    label('loc_14BA')

    Jump('loc_1534')

    def _loc_14BD(): pass

    label('loc_14BD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_1534',
    )

    ChrTalk(
        0x000A,
        (
            '有许多客人\n',
            '都是从很远的地方\n',
            '赶来参加武术大会的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '我们也非常欢迎\n',
            '参加大会的选手\n',
            '前来光顾我们的酒店呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1534(): pass

    label('loc_1534')

    TalkEnd(0x000A)

    Return()

# id: 0x000A offset: 0x1538
@scena.Code('func_0A_1538')
def func_0A_1538():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_1545',
    )

    Jump('loc_1914')

    def _loc_1545(): pass

    label('loc_1545')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_154F',
    )

    Jump('loc_1914')

    def _loc_154F(): pass

    label('loc_154F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_1559',
    )

    Jump('loc_1914')

    def _loc_1559(): pass

    label('loc_1559')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_1563',
    )

    Jump('loc_1914')

    def _loc_1563(): pass

    label('loc_1563')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_156D',
    )

    Jump('loc_1914')

    def _loc_156D(): pass

    label('loc_156D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 3, 0x62B)),
            Expr.Return,
        ),
        'loc_15D7',
    )

    ChrTalk(
        0x00FE,
        (
            '#0330110479V#842F是错觉吗……？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330110480V刚才好像感觉到窗户外面\n',
            '有什么东西横着飞过……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1914')

    def _loc_15D7(): pass

    label('loc_15D7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 1, 0x629)),
            Expr.Return,
        ),
        'loc_1671',
    )

    ChrTalk(
        0x00FE,
        (
            '#0330110477V#840F为明天的比赛做好准备，\n',
            '你们今天就早点休息吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330110478V『有备而无患』，\n',
            '将身体状态调整好，\n',
            '这对于游击士来说很重要的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1914')

    def _loc_1671(): pass

    label('loc_1671')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_1781',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_16BF',
    )

    ChrTalk(
        0x00FE,
        (
            '#0330110485V『不动金』自不用说，\n',
            '你们的战斗也十分出色。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_177E')

    def _loc_16BF(): pass

    label('loc_16BF')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '#0330110481V哦，是你们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0330110482V『不动金』自不用说，\n',
            '你们的战斗也十分出色。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0330110483V每个人的技术都不错，\n',
            '配合也相当熟练。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0330110484V你们的将来无可限量呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_177E(): pass

    label('loc_177E')

    Jump('loc_1914')

    def _loc_1781(): pass

    label('loc_1781')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_178B',
    )

    Jump('loc_1914')

    def _loc_178B(): pass

    label('loc_178B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_18F9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_180A',
    )

    ChrTalk(
        0x00FE,
        (
            '#0330110487V今天我们都能顺利晋级，\n',
            '真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0330110489V这样我们的下一个对手\n',
            '说不定就是你们呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_18F6')

    def _loc_180A(): pass

    label('loc_180A')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '#0330110486V哟，这不是艾丝蒂尔和约修亚嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0330110487V今天我们都能顺利晋级，\n',
            '真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0330110488V虽然之前也听卡露娜说过，\n',
            '不过这次是亲眼见到你们的实力了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0330110489V这样我们的下一个对手\n',
            '说不定就是你们呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_18F6(): pass

    label('loc_18F6')

    Jump('loc_1914')

    def _loc_18F9(): pass

    label('loc_18F9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_1903',
    )

    Jump('loc_1914')

    def _loc_1903(): pass

    label('loc_1903')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_190D',
    )

    Jump('loc_1914')

    def _loc_190D(): pass

    label('loc_190D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_1914',
    )

    def _loc_1914(): pass

    label('loc_1914')

    TalkEnd(0x00FE)

    Return()

# id: 0x000B offset: 0x1918
@scena.Code('func_0B_1918')
def func_0B_1918():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '这家宾馆真是华丽。\n',
            '如果把丈夫也一道带来就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x000C offset: 0x1954
@scena.Code('func_0C_1954')
def func_0C_1954():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '哇～沙发好软呀～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x000D offset: 0x1971
@scena.Code('func_0D_1971')
def func_0D_1971():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 1, 0x629)),
            Expr.Return,
        ),
        'loc_19DA',
    )

    ChrTalk(
        0x00FE,
        (
            '为了明天有充足的精力看比赛，\n',
            '今天就早点休息吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要好好泡个热水澡\n',
            '让疲劳一扫而光。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A3B')

    def _loc_19DA(): pass

    label('loc_19DA')

    ChrTalk(
        0x00FE,
        (
            '哎呀～虽然明天才开始正式比赛，\n',
            '不过今天的比赛就很精彩了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '光是喊加油就已经精疲力尽了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A3B(): pass

    label('loc_1A3B')

    TalkEnd(0x00FE)

    Return()

# id: 0x000E offset: 0x1A3F
@scena.Code('func_0E_1A3F')
def func_0E_1A3F():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 1, 0x629)),
            Expr.Return,
        ),
        'loc_1A92',
    )

    ChrTalk(
        0x00FE,
        (
            '和同住一条街上的人交往～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是分手了，以后见面难道不尴尬吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AC2')

    def _loc_1A92(): pass

    label('loc_1A92')

    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '我说老姐啊～\n',
            '你是不是跟男友分手了啊～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1AC2(): pass

    label('loc_1AC2')

    TalkEnd(0x00FE)

    Return()

# id: 0x000F offset: 0x1AC6
@scena.Code('func_0F_1AC6')
def func_0F_1AC6():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 1, 0x629)),
            Expr.Return,
        ),
        'loc_1B06',
    )

    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '啊～那当然尴尬死了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '肯定不想碰面的～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B5D')

    def _loc_1B06(): pass

    label('loc_1B06')

    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '真的～！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，\n',
            '这样不是正好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他也只不过是个\n',
            '没什么钱的男人啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1B5D(): pass

    label('loc_1B5D')

    TalkEnd(0x00FE)

    Return()

# id: 0x0010 offset: 0x1B61
@scena.Code('func_10_1B61')
def func_10_1B61():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 1, 0x629)),
            Expr.Return,
        ),
        'loc_1BC8',
    )

    ChrTalk(
        0x00FE,
        (
            '本打算和她共赏\n',
            '王都美丽的夜景呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但从今天起夜间禁止外出。\n',
            '啊啊，好想去啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1BFE')

    def _loc_1BC8(): pass

    label('loc_1BC8')

    ChrTalk(
        0x00FE,
        (
            '一会儿我们打算出去看夜景。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '夜幕就要降临了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1BFE(): pass

    label('loc_1BFE')

    TalkEnd(0x00FE)

    Return()

# id: 0x0011 offset: 0x1C02
@scena.Code('func_11_1C02')
def func_11_1C02():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 1, 0x629)),
            Expr.Return,
        ),
        'loc_1C5C',
    )

    ChrTalk(
        0x00FE,
        (
            '偶尔像这样\n',
            '放松一下也不错呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只要和他在一起，我就感到非常幸福了㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1CA3')

    def _loc_1C5C(): pass

    label('loc_1C5C')

    ChrTalk(
        0x00FE,
        (
            '呵呵，能和他一起游览夜色中的王都，\n',
            '我的心都激动得扑嗵扑嗵在跳了㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1CA3(): pass

    label('loc_1CA3')

    TalkEnd(0x00FE)

    Return()

# id: 0x0012 offset: 0x1CA7
@scena.Code('func_12_1CA7')
def func_12_1CA7():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 1, 0x629)),
            Expr.Return,
        ),
        'loc_1CFD',
    )

    ChrTalk(
        0x00FE,
        (
            '今天街上感觉好安静啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '明天就是决赛了，\n',
            '本以为会热闹一点的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D75')

    def _loc_1CFD(): pass

    label('loc_1CFD')

    ChrTalk(
        0x00FE,
        (
            '虽然第一次在这里过夜，\n',
            '但是房间真的很豪华啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过我的哥哥\n',
            '并不太喜欢这样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '反而觉得豪华的地方不安稳。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1D75(): pass

    label('loc_1D75')

    TalkEnd(0x00FE)

    Return()

# id: 0x0013 offset: 0x1D79
@scena.Code('func_13_1D79')
def func_13_1D79():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#0120141615V#811F呀～两位游击士新人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120141616V嘻嘻，\n',
            '我现在想去冲个澡呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120141617V#851F今天也是出了一身汗，\n',
            '好想痛快地洗个澡哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0014 offset: 0x1E10
@scena.Code('func_14_1E10')
def func_14_1E10():
    EventBegin(0x00)
    CameraMove(7350, 0, -5650, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 6930, 0, 1460, 0)
    ChrSetPos(0x0102, 7840, 0, 1460, 0)
    OP_4A(0x000A, 255)
    FadeIn(1500, 0)
    CameraMove(7010, 0, 2460, 4000)

    ChrTalk(
        0x000A,
        (
            '#2230101590V晚上好。\n',
            '欢迎光临罗恩鲍姆酒店。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2230101591V请问二位客人，\n',
            '你们是要住店的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010101592V#006F是的，我们是游击士协会的……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020101593V#010F听说我们两个的房间已经订好了，\n',
            '请问能不能确认一下呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2230101594V哦哦……\n',
            '原来是你们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2230101595V没错，确实有这回事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010101596V#506F呼～太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020101597V#019F多亏了艾南先生呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2230101598V是艾丝蒂尔小姐和约修亚先生吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2230101599V虽然很失礼，\n',
            '不过请让我看一下游击士手册好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010101600V#501F啊，请等一下……',
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
            '把游击士手册展示给前台接待看。',
            (TxtCtl.SetColor, 0x0),
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
            '#2230101601V……好，没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2230101602V那么，\n',
            '请拿好这个。',
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
            '２０２号室的钥匙',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    AddItem(0x0375, 1)

    ChrTalk(
        0x000A,
        (
            '#2230101603V上楼梯到二楼，\n',
            '左边最里面的房间就是了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2230101604V如果有什么事情，\n',
            '随时到前台这里来找我即可。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x00C2, 6, 0x616))
    SetScenaFlags(ScenaFlag(0x00C2, 7, 0x617))
    OP_1B(0x00, 0x00, 0x0019)
    OP_4B(0x000A, 255)
    EventEnd(0x00)

    Return()

# id: 0x0015 offset: 0x2217
@scena.Code('func_15_2217')
def func_15_2217():
    MapClearFlags(0x10000000)
    EventBegin(0x00)
    CameraMove(6980, 0, -3210, 0)
    OP_67(0, 8310, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(337000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 6760, 0, -3090, 180)
    ChrSetPos(0x0102, 7760, 0, -3080, 180)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0008, 6510, -250, -4770, 0)
    ChrSetPos(0x0009, 7820, -250, -4970, 0)
    FadeIn(1500, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010111157V#008F那个……\n',
            '真是太感谢你们特地送我们回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111158V#010F谢谢你们的照顾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2490111159V没什么，\n',
            '我们也是你们的支持者啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#4190111160V虽然同样身为王国军的成员，\n',
            '但有些事情实在不吐不快……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#4190111161V因为我实在不喜欢\n',
            '特务部队的那些家伙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2490111162V是啊是啊，\n',
            '也不知道他们天天在想些什么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2490111163V哦哦……\n',
            '这样说对理查德上校有点失礼呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#4190111164V那就这样吧，\n',
            '期待着你们的精彩表演。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2490111165V明天的比赛，要加油哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111166V#506F啊哈哈……谢谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111167V#010F我们会全力以赴的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x0008, 0x0040)
    ChrSetFlags(0x0009, 0x0040)
    ChrSetDirection(0x0008, 180, 400)

    @scena.Lambda('lambda_2501')
    def lambda_2501():
        ChrWalkTo(0x00FE, 6510, -500, -7470, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2501)

    ChrSetDirection(0x0009, 180, 400)

    @scena.Lambda('lambda_2523')
    def lambda_2523():
        ChrWalkTo(0x00FE, 7820, -500, -7470, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_2523)

    WaitForThreadExit(0x0008, 0x0001)
    ChrSetFlags(0x0008, 0x0004)

    @scena.Lambda('lambda_2548')
    def lambda_2548():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 500)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_2548)

    @scena.Lambda('lambda_255A')
    def lambda_255A():
        ChrWalkTo(0x00FE, 6510, -250, -9000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_255A)

    WaitForThreadExit(0x0009, 0x0001)
    ChrSetFlags(0x0009, 0x0004)

    @scena.Lambda('lambda_257F')
    def lambda_257F():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 500)

        ExitThread()

    DispatchAsync(0x0009, 0x0003, lambda_257F)

    @scena.Lambda('lambda_2591')
    def lambda_2591():
        ChrWalkTo(0x00FE, 7820, -250, -9000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_2591)

    Sleep(1000)

    PlaySE(7, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010111168V#007F呼……真是复杂啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010111169V看来，那些士兵好像\n',
            '完全不知道理查德上校的阴谋呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020111170V#012F那也是啊……\n',
            '他们只不过是普通的士兵而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111171V从上级传来的情报和命令，\n',
            '他们能做到的也只有相信和服从。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111172V#505F嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010111173V他们还支持我们呢，\n',
            '真是不想和他们敌对啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111174V#010F不管怎么说，\n',
            '不要让一般士兵卷进事件来就好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111175V今天晚上就别再出去了，\n',
            '在房间里好好休息吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111176V#006F嗯，ＯＫ。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(1000)
    ChrSetPos(0x0101, 7090, 0, -2590, 0)
    ChrSetPos(0x0102, 7090, 0, -2590, 0)
    CameraMove(7090, 0, -2590, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetScenaFlags(ScenaFlag(0x00C5, 1, 0x629))
    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0009, 0x0080)
    OP_1B(0x00, 0x00, 0x0019)
    EventEnd(0x00)

    Return()

# id: 0x0016 offset: 0x281B
@scena.Code('func_16_281B')
def func_16_281B():
    EventBegin(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 0, 0x618)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 7, 0x617)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_32C5',
    )

    SetScenaFlags(ScenaFlag(0x00C3, 0, 0x618))

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2875',
    )

    ChrTalk(
        0x0101,
        (
            '#0010101605V#006F２０２号室……\n',
            '这就是我们的房间吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_28AB')

    def _loc_2875(): pass

    label('loc_2875')

    ChrTalk(
        0x0102,
        (
            '#0020101606V#010F２０２号室……\n',
            '嗯，就是这里了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_28AB(): pass

    label('loc_28AB')

    Sleep(100)

    Fade(1000)
    ChrSetPos(0x0101, 34420, 0, 108910, 0)
    ChrSetPos(0x0102, 35770, 0, 108690, 0)
    CameraMove(34410, 0, 115500, 0)
    OP_67(0, 5930, -10000, 0)
    CameraSetDistance(1890, 0)
    OP_6C(315000, 0)
    OP_6E(437, 0)
    PlaySE(6, 0x00, 0x64)
    CameraMove(35020, 0, 111190, 2000)

    ChrTalk(
        0x0101,
        (
            '#0010101607V#004F哇……\n',
            '这间屋子气氛很不错啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2964')
    def lambda_2964():
        CameraMove(31860, 0, 115500, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2964)

    @scena.Lambda('lambda_297C')
    def lambda_297C():
        ChrWalkTo(0x00FE, 34420, 0, 113010, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_297C)

    Sleep(600)

    @scena.Lambda('lambda_299C')
    def lambda_299C():
        ChrWalkTo(0x00FE, 35770, 0, 113090, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_299C)

    WaitForThreadExit(0x0101, 0x0001)
    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    @scena.Lambda('lambda_29D3')
    def lambda_29D3():
        ChrWalkTo(0x00FE, 31630, 0, 115500, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_29D3)

    WaitForThreadExit(0x0102, 0x0001)
    ChrTurnDirection(0x0102, 0x0101, 400)
    WaitForThreadExit(0x0101, 0x0001)
    ChrSetDirection(0x0101, 0, 400)

    ChrTalk(
        0x0101,
        (
            '#0010101608V#001F快看快看，\n',
            '从这边可以看到竞技场的夜景呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2A46')
    def lambda_2A46():
        CameraMove(31160, 0, 115440, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2A46)

    @scena.Lambda('lambda_2A5E')
    def lambda_2A5E():
        CameraSetDistance(1700, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2A5E)

    @scena.Lambda('lambda_2A6E')
    def lambda_2A6E():
        OP_6C(306000, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_2A6E)

    @scena.Lambda('lambda_2A7E')
    def lambda_2A7E():
        ChrTurnDirection(0x00FE, 0x0102, 400)
        Yield()

        Jump('lambda_2A7E')

    DispatchAsync2(0x0101, 0x0001, lambda_2A7E)

    ChrWalkTo(0x0102, 32500, 0, 115500, 4000, 0x00)
    ChrSetDirection(0x0102, 0, 400)

    @scena.Lambda('lambda_2AAA')
    def lambda_2AAA():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2AAA)

    WaitForThreadExit(0x0102, 0x0002)

    ChrTalk(
        0x0102,
        (
            '#0020101609V#014F哎……真的啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020101610V#019F在这里只是过夜的话，\n',
            '感觉还真是有点浪费了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020101611V就把这里作为我们\n',
            '在武术大会结束之前的根据地吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010101612V#503F#1P（……要在这里\n',
            '　和约修亚一起度过一段时间啊……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1200)

    OP_63(0x0101)

    ChrTalk(
        0x0101,
        (
            '#0010101613V#504F#3S#1P（哎呀，我在想什么呀～！？）\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)
    Sleep(400)

    ChrTalk(
        0x0102,
        (
            '#0020101614V#013F我说，艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_9E(0x0101, 15, 0, 300, 4000)
    Sleep(200)

    ChrTurnDirection(0x0101, 0x0102, 800)
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_94(0x01, 0x0101, 0x00B4, 0x000001F4, 0x00000FA0, 0x00)

    ChrTalk(
        0x0101,
        (
            '#0010101615V#008F#1P#3S呀！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020101616V#017F突然说这样的话可能你会觉得奇怪……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020101617V#010F嗯，我们是亲人……对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010101618V#004F#1P……哎………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020101619V#015F虽然我可能不像父亲那样值得信赖……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020101620V也可能不像雪拉姐姐那样\n',
            '耐心地听别人说话……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020101621V#010F不过我觉得作为家人，\n',
            '我一定要成为能够支持你的人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020101622V所以，你有什么烦恼的话，\n',
            '随时可以和我说说哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010101623V#004F#1P………啊…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020101624V#017F因为最近，\n',
            '你的样子好像有点奇怪……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020101625V#013F嗯，如果我弄错了的话，抱歉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010101626V#506F#1P哈啊……\n',
            '真不愧是约修亚啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010101627V还是那样的敏锐，\n',
            '不过却搞错重点啦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020101214V#014F哎……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_94(0x01, 0x0101, 0x0000, 0x000001F4, 0x000003E8, 0x00)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010101629V#008F#1P谢谢，约修亚。\n',
            '不过你不用那样担心。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010101630V#007F确实……\n',
            '我最近可能有点怪怪的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010101631V劳累、痛苦什么的，\n',
            '也不是什么大事啦……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010101632V只是自己的心情有些整理不清而已……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010101633V#006F所以……没关系的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010101634V你只要在一旁看着我，就可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020101635V#015F是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020101636V#010F嗯，那么我也不做多余的担心了。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020101637V不过，如果解决了烦恼就来告诉我，\n',
            '我一样会替你感到高兴的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020101638V#014F啊，不是强迫你说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010101639V#503F#1P哎，嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010101640V嗯……如果整理好心情的话，\n',
            '说不定会更加说不出口呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020101641V#014F哎？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010101642V#506F#1P没、没什么啦！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010101643V#006F虽然还有点早……\n',
            '不过现在就休息吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010101644V今天发生了很多事，有点累了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020101645V#010F是啊，明天还有比赛……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020101646V整理完行李就休息吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000005DC)
    FadeOut(1500, 0, -1)
    OP_0D()
    PlaySE(13, 0x00, 0x64)
    Sleep(3000)

    MapSetFlags(0x00100000)
    SetScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    NewScene('ED6_DT01/T4103._SN', 100, 0, 0)
    IdleLoop()

    Return()

    def _loc_32C5(): pass

    label('loc_32C5')

    OP_20(0x000005DC)
    Fade(1000)
    ChrSetPos(0x0102, 56580, 0, 2320, 0)
    ChrSetPos(0x0101, 57920, 0, 2070, 0)
    CameraMove(56650, 0, 3000, 0)
    OP_0D()
    PlaySE(130, 0x00, 0x64)
    PlaySE(140, 0x00, 0x32)
    Sleep(1000)

    OP_62(0x0101, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010111187V#505F哎……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010111188V刚才是不是有什么声音？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111189V#510F………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    PlayBGM(81)
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020111190V#015F（进入房间的同时保持临战状态，\n',
            '　然后确认里面的状况。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111191V#004F（哎……！？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111192V#012F（大概是入侵者。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111193V（有可能设置了爆炸陷阱，\n',
            '　所以一定要万分小心。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x0101,
        (
            '#0010111194V#580F（等、等一下……不是开玩笑的吧？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020111195V#015F（拜托了，照我说的去做……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111196V（如果有什么问题的话，\n',
            '　你在这里等着也可以。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111197V#005F（开、开玩笑！）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010111198V（我已经做好准备了，\n',
            '　总之赶快进去看看吧！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111199V#013F（……好吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x00C5, 2, 0x62A))
    OP_64(0x00, 0x0001)
    OP_71(0x0012, 0x0010)
    OP_1C(0x12, 0x00, 0xFFFF)
    FadeOut(500, 0, -1)
    OP_0D()
    Call(0, 0x0017)

    Return()

# id: 0x0017 offset: 0x35F6
@scena.Code('func_17_35F6')
def func_17_35F6():
    EventBegin(0x00)
    ChrClearFlags(0x0019, 0x0080)
    ChrSetPos(0x0019, -24300, -200, 175600, 0)
    CameraMove(-25590, 0, 170160, 0)
    OP_67(0, 7400, -10000, 0)
    CameraSetDistance(1500, 0)
    OP_6C(325000, 0)
    OP_6E(478, 0)
    ChrSetPos(0x0101, -23950, 0, 168970, 0)
    ChrSetPos(0x0102, -25320, 0, 168830, 0)
    ChrSetChipByIndex(0x0101, 2)
    ChrSetChipByIndex(0x0102, 3)
    FadeOut(0, 0, -1)
    PlaySE(6, 0x00, 0x64)
    Sleep(1000)

    FadeIn(1000, 0)
    CameraMove(-25590, 0, 172760, 1000)

    ChrTalk(
        0x0101,
        (
            '#0010111200V#004F#5P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111201V#012F#5P好像逃跑了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithValue(
        0x0102,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0102, 65535)
    Sleep(400)

    ChrTalk(
        0x0102,
        (
            '#0020111202V#013F#5P不过，奇怪了……\n',
            '感觉好像没有人来过啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111203V陷阱什么的……\n',
            '好像也没有设置过的迹象。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithValue(
        0x0101,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0101, 65535)
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010111204V#004F#5P连、连这些你也能看出来吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_37C9')
    def lambda_37C9():
        ChrTurnDirection(0x00FE, 0x0102, 0)
        Yield()

        Jump('lambda_37C9')

    DispatchAsync2(0x0101, 0x0002, lambda_37C9)

    @scena.Lambda('lambda_37DA')
    def lambda_37DA():
        CameraMove(-24940, 0, 175710, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_37DA)

    @scena.Lambda('lambda_37F2')
    def lambda_37F2():
        ChrWalkTo(0x00FE, -24440, 0, 174950, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_37F2)

    Sleep(800)

    @scena.Lambda('lambda_3812')
    def lambda_3812():
        ChrWalkTo(0x00FE, -24670, 0, 173620, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3812)

    WaitForThreadExit(0x0102, 0x0002)

    @scena.Lambda('lambda_3832')
    def lambda_3832():
        ChrSetDirection(0x00FE, 0, 0)
        Yield()

        Jump('lambda_3832')

    DispatchAsync2(0x0102, 0x0001, lambda_3832)

    WaitForThreadExit(0x0102, 0x0002)
    TerminateThread(0x0102, 0xFF)
    Fade(500)
    ChrSetChipByIndex(0x0102, 12)
    OP_0D()

    ChrTalk(
        0x0102,
        (
            '#0020111205V#015F#5P……看起来，\n',
            '好像只是给我们送来了礼物呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010111206V#505F那个是……信？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x0019, 0x0080)
    Fade(500)
    ChrSetChipByIndex(0x0102, 65535)
    OP_0D()
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(72, 320, 56, 3)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '约修亚打开信封。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    Sleep(400)

    ChrTalk(
        0x0102,
        (
            '#0020111207V#012F#5P『——今天晚上１０点，\n',
            '　请到大圣堂来。』',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111208V『另外请不要告诉别人。』',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010111209V#004F#6P……只有这些？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010111210V#505F大圣堂……\n',
            '指的是西街区那个大教会吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010111211V今天晚上１０点，\n',
            '马上就要到了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111212V#015F#5P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111213V#007F#6P嗯，虽然可疑的地方太多了，\n',
            '不过人不是常说『不入虎穴焉得虎子』……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010111214V#006F喂，约修亚。\n',
            '我们真的要应邀过去吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111215V#510F#3S#5P……不行！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010111216V#580F#6P怎、怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020111217V#013F#2P不好意思，突然这么大声……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111218V#010F对了，刚才那些士兵不是说过\n',
            '他们要强化夜间的巡逻吗？\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111219V这里离西街区很远，\n',
            '被发现和盘问的可能性很高。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111220V#004F#6P啊，忘记了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010111221V#007F嗯～不过如果就这样放着不管，\n',
            '又会让人觉得十分在意呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111222V#010F#2P所以，我一个人去就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111223V#004F#6P哎……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111224V#015F#2P这种情况下，\n',
            '一个人行动要比起两个人保险很多。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111225V这样就能绕过士兵安全到达大圣堂了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111226V#004F#6P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111227V#010F#2P只是去确认一下情况而已，\n',
            '所以我一个人去就够了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111228V所以你在这里等着……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111229V#509F#3S#6P我说……',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111230V#014F#2P哎……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111231V#009F#6P我可是游击士哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010111232V能自己够照顾自己，\n',
            '而且我也有自信不会拖你的后腿。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010111233V你就算再怎么花言巧语，\n',
            '也糊弄不过我的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111234V#013F#2P艾丝蒂尔，我不是打算这样……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111235V#500F#6P我知道，你不是不相信我。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010111236V说是担心……\n',
            '大概，也不只是因为这个吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010111237V#006F你是不是已经知道了什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111238V#013F#2P………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111239V我的话语已经没什么破绽了，\n',
            '为什么你连这个也能觉察到？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111240V#006F#6P这个……\n',
            '因为我是观察约修亚的第一人嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010111241V不管怎么说，我都会知道啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111238V#013F#2P………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111243V#015F（……到此为止…吗…………）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111244V#004F#6P哎？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111245V#010F#2P知道了，我不会阻止你了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111246V已经到指定的时间了，\n',
            '我们赶快去大圣堂吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111247V#008F#6P啊……嗯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111248V#012F#2P不过……\n',
            '我要你事先做好约定。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111249V如果发生什么事情，\n',
            '一定要照我的指示去做。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111250V一瞬间的判断失误，\n',
            '说不定就会丧命。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111251V#004F#6P嗯……我知道了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010111252V#006F那么我们赶快走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    OP_20(0x000005DC)
    Fade(1500)
    ChrSetPos(0x0101, -24630, 0, 173630, 180)
    ChrSetPos(0x0102, -24630, 0, 173630, 180)
    CameraMove(-24630, 0, 173630, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_28(0x0048, 0x01, 0x0100)
    OP_1B(0x00, 0x00, 0xFFFF)
    SetScenaFlags(ScenaFlag(0x00C5, 3, 0x62B))
    Sleep(500)

    EventEnd(0x00)
    PlayBGM(84)

    Return()

# id: 0x0018 offset: 0x430C
@scena.Code('func_18_430C')
def func_18_430C():
    MapClearFlags(0x10000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 5, 0x62D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_480F',
    )

    EventBegin(0x00)
    CameraMove(6980, 0, -3210, 0)
    OP_67(0, 8310, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(337000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 6760, 0, -3090, 180)
    ChrSetPos(0x0102, 7760, 0, -3080, 180)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0008, 6510, -250, -4770, 0)
    ChrSetPos(0x0009, 7820, -250, -4970, 0)
    FadeIn(1500, 0)
    OP_0D()

    If(
        (
            (Expr.Eval, "OP_29(0x0048, 0x01, 0x0800)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_43C5',
    )

    OP_28(0x0048, 0x01, 0x0800)

    Jump('loc_4416')

    def _loc_43C5(): pass

    label('loc_43C5')

    If(
        (
            (Expr.Eval, "OP_29(0x0048, 0x01, 0x1000)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_43DA',
    )

    OP_28(0x0048, 0x01, 0x1000)

    Jump('loc_4416')

    def _loc_43DA(): pass

    label('loc_43DA')

    If(
        (
            (Expr.Eval, "OP_29(0x0048, 0x01, 0x2000)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_43EF',
    )

    OP_28(0x0048, 0x01, 0x2000)

    Jump('loc_4416')

    def _loc_43EF(): pass

    label('loc_43EF')

    If(
        (
            (Expr.Eval, "OP_29(0x0048, 0x01, 0x4000)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4404',
    )

    OP_28(0x0048, 0x01, 0x4000)

    Jump('loc_4416')

    def _loc_4404(): pass

    label('loc_4404')

    If(
        (
            (Expr.Eval, "OP_29(0x0048, 0x01, 0x8000)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4416',
    )

    OP_28(0x0048, 0x01, 0x8000)

    def _loc_4416(): pass

    label('loc_4416')

    ChrTalk(
        0x0008,
        (
            '#4190111270V真是会给人添麻烦啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2490111271V为了防范恐怖分子，\n',
            '任何市民一律禁止夜间外出。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x0008, 0x0040)
    ChrSetFlags(0x0009, 0x0040)
    ChrSetDirection(0x0008, 180, 400)

    @scena.Lambda('lambda_4494')
    def lambda_4494():
        ChrWalkTo(0x00FE, 6510, -500, -7470, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_4494)

    ChrSetDirection(0x0009, 180, 400)

    @scena.Lambda('lambda_44B6')
    def lambda_44B6():
        ChrWalkTo(0x00FE, 7820, -500, -7470, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_44B6)

    WaitForThreadExit(0x0008, 0x0001)
    ChrSetFlags(0x0008, 0x0004)

    @scena.Lambda('lambda_44DB')
    def lambda_44DB():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 500)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_44DB)

    @scena.Lambda('lambda_44ED')
    def lambda_44ED():
        ChrWalkTo(0x00FE, 6510, -250, -9000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_44ED)

    WaitForThreadExit(0x0009, 0x0001)
    ChrSetFlags(0x0009, 0x0004)

    @scena.Lambda('lambda_4512')
    def lambda_4512():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 500)

        ExitThread()

    DispatchAsync(0x0009, 0x0003, lambda_4512)

    @scena.Lambda('lambda_4524')
    def lambda_4524():
        ChrWalkTo(0x00FE, 7820, -250, -9000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_4524)

    Sleep(2000)

    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010111272V#007F哎呀……\n',
            '被送回来了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010111273V只好再试一次了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020111274V#012F刚才我就注意到了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111275V那些监视着某个固定地方的士兵，\n',
            '我们最好不要靠近他们。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111276V为了保证不让他们发现，\n',
            '我们只好绕个远路了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111277V#505F原来如此……\n',
            '直接往大圣堂所在的\n',
            '西街区走确实比较困难。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111278V#010F还有，那些巡逻的士兵……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111279V因为晚上视野不好，\n',
            '只要不太靠近或是站在他们前面，\n',
            '也应该不会被发现。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111280V另外，他们各自的巡逻路线\n',
            '好像是事先安排好的，\n',
            '稍微注意一下就可以看出规律来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111281V#006F明白了……\n',
            '那么我们走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(1000)
    ChrSetPos(0x0101, 7090, 0, -2590, 0)
    ChrSetPos(0x0102, 7090, 0, -2590, 0)
    CameraMove(7090, 0, -2590, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetScenaFlags(ScenaFlag(0x00C5, 5, 0x62D))
    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0009, 0x0080)
    EventEnd(0x00)

    Jump('loc_4CDB')

    def _loc_480F(): pass

    label('loc_480F')

    EventBegin(0x00)
    CameraMove(7010, 0, -2900, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 6760, 0, -3090, 180)
    ChrSetPos(0x0102, 7760, 0, -3080, 180)
    ChrTurnDirection(0x0101, 0x0102, 0)
    ChrTurnDirection(0x0102, 0x0101, 0)
    FadeIn(1500, 0)
    OP_0D()

    If(
        (
            (Expr.Eval, "OP_29(0x0048, 0x01, 0x0800)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_49E8',
    )

    OP_28(0x0048, 0x01, 0x0800)

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x6A),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_492E',
    )

    ChrTalk(
        0x0102,
        (
            '#0020111282V#012F那些监视着某个固定地方的士兵，\n',
            '我们最好不要靠近他们。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111276V为了保证不让他们发现，\n',
            '我们只好绕个远路了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_49E5')

    def _loc_492E(): pass

    label('loc_492E')

    ChrTalk(
        0x0102,
        (
            '#0020111284V#012F因为晚上视野不好，\n',
            '只要不太靠近或是站在他们前面，\n',
            '也应该不会被发现。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111280V另外，他们各自的巡逻路线\n',
            '好像是事先安排好的，\n',
            '稍微注意一下就可以看出规律来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_49E5(): pass

    label('loc_49E5')

    Jump('loc_4CD9')

    def _loc_49E8(): pass

    label('loc_49E8')

    If(
        (
            (Expr.Eval, "OP_29(0x0048, 0x01, 0x1000)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4B48',
    )

    OP_28(0x0048, 0x01, 0x1000)

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x6A),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4A8E',
    )

    ChrTalk(
        0x0102,
        (
            '#0020111282V#012F那些监视着某个固定地方的士兵，\n',
            '我们最好不要靠近他们。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111276V为了保证不让他们发现，\n',
            '我们只好绕个远路了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4B45')

    def _loc_4A8E(): pass

    label('loc_4A8E')

    ChrTalk(
        0x0102,
        (
            '#0020111284V#012F因为晚上视野不好，\n',
            '只要不太靠近或是站在他们前面，\n',
            '也应该不会被发现。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111280V另外，他们各自的巡逻路线\n',
            '好像是事先安排好的，\n',
            '稍微注意一下就可以看出规律来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4B45(): pass

    label('loc_4B45')

    Jump('loc_4CD9')

    def _loc_4B48(): pass

    label('loc_4B48')

    If(
        (
            (Expr.Eval, "OP_29(0x0048, 0x01, 0x2000)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4B9B',
    )

    OP_28(0x0048, 0x01, 0x2000)

    ChrTalk(
        0x0102,
        (
            '#0020111290V#015F士兵好像减少了一些，\n',
            '别放松警惕，走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4CD9')

    def _loc_4B9B(): pass

    label('loc_4B9B')

    If(
        (
            (Expr.Eval, "OP_29(0x0048, 0x01, 0x4000)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4C10',
    )

    OP_28(0x0048, 0x01, 0x4000)

    ChrTalk(
        0x0102,
        (
            '#0020111291V#010F大部分士兵好像都回去了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111292V大概是夜间的巡逻快要结束了吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4CD9')

    def _loc_4C10(): pass

    label('loc_4C10')

    If(
        (
            (Expr.Eval, "OP_29(0x0048, 0x01, 0x8000)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4C6D',
    )

    OP_28(0x0048, 0x01, 0x8000)

    ChrTalk(
        0x0102,
        (
            '#0020111293V#010F酒店前面的士兵也走掉了，\n',
            '很容易就能到南街区了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4CD9')

    def _loc_4C6D(): pass

    label('loc_4C6D')

    ChrTalk(
        0x0102,
        (
            '#0020111294V#010F士兵基本上都撤走了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111295V沿着大道到南街区，\n',
            '然后就直接到西街区的大圣堂去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4CD9(): pass

    label('loc_4CD9')

    EventEnd(0x00)
    def _loc_4CDB(): pass

    label('loc_4CDB')

    Return()

# id: 0x0019 offset: 0x4CDC
@scena.Code('func_19_4CDC')
def func_19_4CDC():
    EventBegin(0x01)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 0, 0x628)),
            Expr.Return,
        ),
        'loc_4DEC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4D84',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020111177V#010F今晚就回房间休息吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111178V再随便外出的话\n',
            '被士兵碰上就不好办了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010111179V#000F嗯，说的也是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4DE9')

    def _loc_4D84(): pass

    label('loc_4D84')

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020111177V#010F今晚就回房间休息吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111181V再随便外出的话\n',
            '被士兵碰上就不好办了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4DE9(): pass

    label('loc_4DE9')

    Jump('loc_4F0E')

    def _loc_4DEC(): pass

    label('loc_4DEC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4E98',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020111182V#010F已经很晚了，\n',
            '还是不要到外面去了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111183V明天还有比赛呢。\n',
            '最好充分地休息一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010111179V#000F嗯，说的也是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4F0E')

    def _loc_4E98(): pass

    label('loc_4E98')

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020111185V#010F已经很晚了，\n',
            '还是不要到外面去了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111186V而且明天还有比赛呢。\n',
            '最好充分地休息一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4F0E(): pass

    label('loc_4F0E')

    ChrMoveToRelative(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x001A offset: 0x4F2A
@scena.Code('func_1A_4F2A')
def func_1A_4F2A():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '　　　　　　　事务室　　　　　　　\n',
            '※工作人员以外禁止进入。',
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
