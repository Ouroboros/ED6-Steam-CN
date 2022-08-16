import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T2512_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2512   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'T2512.x'
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
        ('ED6_DT07/CH01360._CH', 'ED6_DT07/CH01360P._CP'),
        ('ED6_DT07/CH01363._CH', 'ED6_DT07/CH01363P._CP'),
        ('ED6_DT07/CH01090._CH', 'ED6_DT07/CH01090P._CP'),
        ('ED6_DT07/CH01370._CH', 'ED6_DT07/CH01370P._CP'),
        ('ED6_DT26/CH20208._CH', 'ED6_DT26/CH20208P._CP'),
        ('ED6_DT07/CH01360._CH', 'ED6_DT07/CH01360P._CP'),
        ('ED6_DT07/CH01580._CH', 'ED6_DT07/CH01580P._CP'),
        ('ED6_DT26/CH20441._CH', 'ED6_DT26/CH20441P._CP'),
        ('ED6_DT07/CH01370._CH', 'ED6_DT07/CH01370P._CP'),
        ('ED6_DT07/CH01590._CH', 'ED6_DT07/CH01590P._CP'),
        ('ED6_DT07/CH01430._CH', 'ED6_DT07/CH01430P._CP'),
        ('ED6_DT07/CH01080._CH', 'ED6_DT07/CH01080P._CP'),
        ('ED6_DT26/CH20501._CH', 'ED6_DT26/CH20501P._CP'),
    ]

# id: 0x10001 offset: 0x112
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '亚吉鲁',
            x                   = -30910,
            z                   = 0,
            y                   = 25940,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '德尼斯',
            x                   = -28980,
            z                   = 0,
            y                   = 970,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '芙拉瑟',
            x                   = -60900,
            z                   = 0,
            y                   = -2690,
            direction           = 315,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '蕾娜',
            x                   = -61500,
            z                   = 0,
            y                   = -1880,
            direction           = 135,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '雅莉丝',
            x                   = -60440,
            z                   = 0,
            y                   = 30850,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            name                = '莫妮卡',
            x                   = -62350,
            z                   = 0,
            y                   = 25980,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            name                = '米丽亚老师',
            x                   = -31110,
            z                   = 0,
            y                   = 29000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            name                = '米克',
            x                   = -28350,
            z                   = 0,
            y                   = 29790,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0011,
        ),
        ScenaNpcData(
            name                = '强化猎兵',
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
            name                = '强化猎兵',
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
            name                = '强化猎兵',
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
            name                = '强化猎兵',
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
            name                = '罗迪',
            x                   = -29450,
            z                   = 0,
            y                   = 30290,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '罗伊斯',
            x                   = -30710,
            z                   = 0,
            y                   = 28800,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '巴克斯',
            x                   = -30900,
            z                   = 300,
            y                   = 29850,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0195,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '黛拉',
            x                   = -60450,
            z                   = 0,
            y                   = 28840,
            direction           = 315,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '妮吉塔',
            x                   = -61710,
            z                   = 0,
            y                   = 29010,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
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
    )

# id: 0x10002 offset: 0x352
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x352
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x352
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -29730,
            triggerZ            = 0,
            triggerY            = 30330,
            triggerRange        = 400,
            actorX              = -31730,
            actorZ              = 1500,
            actorY              = 30100,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000F,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x376
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_3DB',
    )

    ChrClearFlags(0x000C, 0x0080)
    ChrSetPos(0x0008, -160, 0, -940, 10)
    ChrClearFlags(0x000D, 0x0080)
    ChrSetFlags(0x000B, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    ChrClearFlags(0x0016, 0x0080)
    ChrSetFlags(0x0016, 0x0004)
    ChrSetPos(0x0016, -31700, -50, 30400, 90)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetPos(0x000F, -27860, 0, 27430, 328)

    Jump('loc_548')

    def _loc_3DB(): pass

    label('loc_3DB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0403, 7, 0x201F)),
            Expr.Return,
        ),
        'loc_4EA',
    )

    ChrSetFlags(0x000B, 0x0080)
    ChrClearFlags(0x0014, 0x0080)
    ChrClearFlags(0x0015, 0x0080)
    ChrClearFlags(0x0016, 0x0080)
    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x0016, 0x0004)
    ChrSetPos(0x0016, -31700, -50, 30400, 90)
    ChrClearFlags(0x0017, 0x0080)
    ChrClearFlags(0x0018, 0x0080)
    ChrSetPos(0x000A, -60810, 0, 29920, 180)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 2, 0x202A)),
            Expr.Return,
        ),
        'loc_48C',
    )

    ChrSetPos(0x0010, -1570, 0, -2940, 0)
    ChrSetPos(0x0011, 480, 0, -3440, 0)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0010, 0x0001)
    ChrSetFlags(0x0010, 0x0002)
    ChrSetChipByIndex(0x0010, 12)
    ChrSetSubChip(0x0010, 8)
    ChrClearFlags(0x0011, 0x0001)
    ChrSetFlags(0x0011, 0x0002)
    ChrSetChipByIndex(0x0011, 12)
    ChrSetSubChip(0x0011, 11)

    def _loc_48C(): pass

    label('loc_48C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 4, 0x202C)),
            Expr.Return,
        ),
        'loc_4E7',
    )

    ChrSetPos(0x0012, -88920, 0, -3130, 0)
    ChrSetPos(0x0013, -90170, 0, -3000, 0)
    ChrClearFlags(0x0012, 0x0080)
    ChrClearFlags(0x0013, 0x0080)
    ChrClearFlags(0x0012, 0x0001)
    ChrSetFlags(0x0012, 0x0002)
    ChrSetChipByIndex(0x0012, 12)
    ChrSetSubChip(0x0012, 9)
    ChrClearFlags(0x0013, 0x0001)
    ChrSetFlags(0x0013, 0x0002)
    ChrSetChipByIndex(0x0013, 12)
    ChrSetSubChip(0x0013, 14)

    def _loc_4E7(): pass

    label('loc_4E7')

    Jump('loc_548')

    def _loc_4EA(): pass

    label('loc_4EA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_503',
    )

    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x0008, 0x0080)

    Jump('loc_548')

    def _loc_503(): pass

    label('loc_503')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0244, 1, 0x1221)),
            Expr.Return,
        ),
        'loc_517',
    )

    ChrSetFlags(0x000A, 0x0010)
    ChrSetFlags(0x000B, 0x0010)

    Jump('loc_548')

    def _loc_517(): pass

    label('loc_517')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0246, 4, 0x1234)),
            Expr.Return,
        ),
        'loc_537',
    )

    ChrSetFlags(0x000A, 0x0010)
    ChrSetPos(0x000A, -60520, 0, -2690, 90)

    Jump('loc_548')

    def _loc_537(): pass

    label('loc_537')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 6, 0x121E)),
            Expr.Return,
        ),
        'loc_548',
    )

    ChrSetFlags(0x000A, 0x0010)
    ChrSetFlags(0x000B, 0x0010)

    def _loc_548(): pass

    label('loc_548')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_55E',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    MapSetFlags(0x10000000)
    Event(0, func_12_2740)

    Jump('loc_62E')

    def _loc_55E(): pass

    label('loc_55E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_574',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    MapSetFlags(0x10000000)
    Event(0, func_13_2827)

    Jump('loc_62E')

    def _loc_574(): pass

    label('loc_574')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 2, 0x10F2)),
            Expr.Return,
        ),
        'loc_58A',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    MapSetFlags(0x10000000)
    Event(0, func_14_28FD)

    Jump('loc_62E')

    def _loc_58A(): pass

    label('loc_58A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 3, 0x10F3)),
            Expr.Return,
        ),
        'loc_5A0',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    MapSetFlags(0x10000000)
    Event(0, func_15_29CD)

    Jump('loc_62E')

    def _loc_5A0(): pass

    label('loc_5A0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 4, 0x10F4)),
            Expr.Return,
        ),
        'loc_5B6',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 4, 0x10F4))
    MapSetFlags(0x10000000)
    Event(0, func_16_2A88)

    Jump('loc_62E')

    def _loc_5B6(): pass

    label('loc_5B6')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_5CE'),
        (0x0000006B, 'loc_5E6'),
        (0x0000006D, 'loc_5FE'),
        (0x00000074, 'loc_616'),
        (-1, 'loc_62E'),
    )

    def _loc_5CE(): pass

    label('loc_5CE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0403, 7, 0x201F)),
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 2, 0x202A)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5E3',
    )

    MapSetFlags(0x10000000)
    Event(0, func_19_2BBE)

    def _loc_5E3(): pass

    label('loc_5E3')

    Jump('loc_62E')

    def _loc_5E6(): pass

    label('loc_5E6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0403, 7, 0x201F)),
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 3, 0x202B)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5FB',
    )

    MapSetFlags(0x10000000)
    Event(0, func_20_328D)

    def _loc_5FB(): pass

    label('loc_5FB')

    Jump('loc_62E')

    def _loc_5FE(): pass

    label('loc_5FE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0403, 7, 0x201F)),
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 4, 0x202C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_613',
    )

    MapSetFlags(0x10000000)
    Event(0, func_27_3DEB)

    def _loc_613(): pass

    label('loc_613')

    Jump('loc_62E')

    def _loc_616(): pass

    label('loc_616')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0403, 7, 0x201F)),
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 5, 0x202D)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_62B',
    )

    MapSetFlags(0x10000000)
    Event(0, func_2E_45D3)

    def _loc_62B(): pass

    label('loc_62B')

    Jump('loc_62E')

    def _loc_62E(): pass

    label('loc_62E')

    Return()

# id: 0x0001 offset: 0x62F
@scena.Code('func_01_62F')
def func_01_62F():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0244, 1, 0x1221)),
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_647',
    )

    OP_B1('t2512_y')

    Jump('loc_650')

    def _loc_647(): pass

    label('loc_647')

    OP_B1('t2512_n')

    def _loc_650(): pass

    label('loc_650')

    OP_64(0x00, 0x0001)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_66C',
    )

    OP_65(0x00, 0x0001)
    OP_71(0x000F, 0x0004)
    OP_72(0x0010, 0x0004)

    Jump('loc_6A9')

    def _loc_66C(): pass

    label('loc_66C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0403, 7, 0x201F)),
            Expr.Return,
        ),
        'loc_684',
    )

    OP_71(0x000F, 0x0004)
    OP_72(0x0010, 0x0004)
    OP_65(0x00, 0x0001)

    Jump('loc_6A9')

    def _loc_684(): pass

    label('loc_684')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_68E',
    )

    Jump('loc_6A9')

    def _loc_68E(): pass

    label('loc_68E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0244, 1, 0x1221)),
            Expr.Return,
        ),
        'loc_698',
    )

    Jump('loc_6A9')

    def _loc_698(): pass

    label('loc_698')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0246, 4, 0x1234)),
            Expr.Return,
        ),
        'loc_6A2',
    )

    Jump('loc_6A9')

    def _loc_6A2(): pass

    label('loc_6A2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 6, 0x121E)),
            Expr.Return,
        ),
        'loc_6A9',
    )

    def _loc_6A9(): pass

    label('loc_6A9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_6B3',
    )

    Jump('loc_6E0')

    def _loc_6B3(): pass

    label('loc_6B3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0403, 7, 0x201F)),
            Expr.Return,
        ),
        'loc_6CB',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x59),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MapSetFlags(0x02000000)

    Jump('loc_6E0')

    def _loc_6CB(): pass

    label('loc_6CB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 3, 0x2013)),
            Expr.Return,
        ),
        'loc_6E0',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x6E),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MapSetFlags(0x02000000)

    def _loc_6E0(): pass

    label('loc_6E0')

    Return()

# id: 0x0002 offset: 0x6E1
@scena.Code('func_02_6E1')
def func_02_6E1():
    EventBegin(0x00)
    Fade(1000)
    ChrSetPos(0x0101, -61000, 0, -3720, 0)
    ChrSetPos(0x0105, -60410, 0, -4540, 0)

    ExecExpressionWithValue(
        0x0019,
        0x01,
        (
            (Expr.GetChrWork, 0xB, 0x1),
            (Expr.GetChrWork, 0xA, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0019,
        0x02,
        (
            (Expr.GetChrWork, 0xB, 0x2),
            (Expr.GetChrWork, 0xA, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0019,
        0x03,
        (
            (Expr.GetChrWork, 0xB, 0x3),
            (Expr.GetChrWork, 0xA, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_69(0x0019, 0)
    OP_4A(0x000A, 255)
    OP_4A(0x000B, 255)
    OP_0D()
    ChrClearFlags(0x000A, 0x0010)
    ChrClearFlags(0x000B, 0x0010)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010211130V#1000F那个……打扰一下………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2890211131V#2P#4S那种事从来没有听说过！！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CreateThread(0x0101, 0x01, 0x00, func_03_1569)
    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010211132V#1004F（呜、呜哇……！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x000A,
        (
            '#2890211133V我之前不是早就说过，\n',
            '放假时要在利贝尔旅行的吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2890211134V为什么事到如今\n',
            '还说什么要我回国探亲！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2900211135V芙拉瑟，请你\n',
            '冷静一点啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2890211136V不！我什么都不要听！\n',
            '今天我必须要把话说清楚！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveToRelativeAsync(0x0101, 0, 0, 400, 1000, 0x00)

    ChrTalk(
        0x0101,
        (
            '#0010211137V#1015F哎，那个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2890211138V考试好不容易才结束，\n',
            '本以为终于可以去旅行了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2890211139V为什么要在这种时候\n',
            '给我订帝国的往返票！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2890211140V你是和老头子串通好了\n',
            '来整我的吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x0E, 0x0F, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010211141V#1007F（呜啊～好像插不上嘴啊。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060211142V#045F（暂、暂且就先旁观一会吧……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2900211143V那个…芙拉瑟啊…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2900211144V你现在最好还是\n',
            '什么都别说了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2890211145V最、最好什么都别说……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2890211146V#3S最、最好什么都别说！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2890211147V仆、仆人竟然敢\n',
            '用这种口气对主人讲话……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ExecExpressionWithValue(
        0x0019,
        0x01,
        (
            (Expr.GetChrWork, 0x101, 0x1),
            (Expr.GetChrWork, 0xA, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0019,
        0x02,
        (
            (Expr.GetChrWork, 0x101, 0x2),
            (Expr.GetChrWork, 0xA, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0019,
        0x03,
        (
            (Expr.GetChrWork, 0x101, 0x3),
            (Expr.GetChrWork, 0xA, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_0B9A')
    def lambda_0B9A():
        OP_69(0x0019, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0B9A)

    ChrTurnDirection(0x000A, 0x0101, 400)
    Sleep(400)

    ChrTurnDirection(0x000B, 0x0101, 400)
    Sleep(1000)

    OP_62(0x000A, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1500)

    ChrTalk(
        0x000A,
        (
            '#2890211148V……啊…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010211149V#1008F啊…啊哈哈～……你们好～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000B, 0x0101, 400)

    ChrTalk(
        0x000B,
        (
            '#2900211150V(所以我才会那么说啊……)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2890211151V#2P咳、咳咳……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2890211152V#2P……你们有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010211153V#1016F嗯、嗯……\n',
            '抱歉打扰你们了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211154V我们这次来\n',
            '是想调查一些事情……',
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
            '艾丝蒂尔表示自己正在调查\n',
            '考试期间发生的奇异事件。',
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
            '#2890211155V#2P……………………………\n',
            '……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2900211156V原来如此，是为了\n',
            '调查那件事而来的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2890211157V#2P蕾娜！别再说了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2890211158V#2P我、我不想再想起那件事了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010211159V#1002F…………发生了什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2900211160V嗯，其实…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2900211161V……在考试期间中，\n',
            '我们目击到了奇怪的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2900211162V说具体些的话，\n',
            '就是『在空中飞舞的人影』……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(15)

    OP_62(0x0105, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    ChrTalk(
        0x0105,
        (
            '#0060211163V#044F这……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x000B, 400)

    ChrTalk(
        0x000A,
        (
            '#2890211164V#2P#3S蕾娜……！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010211165V#1002F……可以说得\n',
            '再详细一点吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2900211166V那我就说了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000B, 0x000A, 400)

    ChrTalk(
        0x000B,
        (
            '#2900211167V……可以吗？芙拉瑟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 2000, 0x0E, 0x0F, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000A,
        (
            '#2890211168V#2P呜～……随、随便你了啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000A, 90, 400)
    ChrWalkTo(0x000A, -60520, 0, -2690, 1000, 0x00)

    ExecExpressionWithValue(
        0x0019,
        0x01,
        (
            (Expr.GetChrWork, 0x101, 0x1),
            (Expr.GetChrWork, 0xB, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0019,
        0x02,
        (
            (Expr.GetChrWork, 0x101, 0x2),
            (Expr.GetChrWork, 0xB, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0019,
        0x03,
        (
            (Expr.GetChrWork, 0x101, 0x3),
            (Expr.GetChrWork, 0xB, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_10A2')
    def lambda_10A2():
        OP_69(0x0019, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_10A2)

    Sleep(500)

    ChrTurnDirection(0x000B, 0x0101, 400)
    Sleep(1500)

    ChrTalk(
        0x000B,
        (
            '#2900211169V那是在考试前一天\n',
            '的深夜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2900211170V突然就听到芙拉瑟\n',
            '喊道『窗外有人！』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010211171V#1002F好、好像在讲校园怪谈一样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2900211172V我们打开窗子向外看去，\n',
            '在校舍的上空确实有个人影。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2900211173V就像是被风吹动一样，\n',
            '在天上轻飘飘地转着圈。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 2000, 0x14, 0x17, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)

    @scena.Lambda('lambda_11EF')
    def lambda_11EF():
        OP_9E(0x00FE, 20, 0, 300, 3000)

        ExitThread()

    DispatchAsync(0x000A, 0x0003, lambda_11EF)

    Sleep(1000)

    ChrTalk(
        0x000A,
        (
            '#2890211174V#2P呜呜…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x000A, 0x03)

    ChrTalk(
        0x000B,
        (
            '#2900211175V不久之后人影就消失在\n',
            '校舍的深处不见了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x000B,
        (
            '#2900211176V……真正不得了的事情\n',
            '还在后边。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2900211177V受到惊吓的大小姐\n',
            '拼命往我的被子里钻……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    TerminateThread(0x000A, 0x03)

    @scena.Lambda('lambda_12F3')
    def lambda_12F3():
        ChrJumpToRelative(0x00FE, 0, 0, 0, 400, 6000)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_12F3)

    ChrTurnDirection(0x000A, 0x000B, 10000)

    ChrTalk(
        0x000A,
        (
            '#2890211178V#2P#3S那、那种事\n',
            '就没必要说了！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010211179V#1016F啊、那种事不说也没关系啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2900211180V哎呀，是这样吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2900211181V真遗憾……\n',
            '其实接下来的事情更有意思呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010211182V#1015F嗯、嗯，\n',
            '那么……就来整理一下证言吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211183V人影出现在校舍的上空，\n',
            '然后就在校舍深处消失了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2900211184V嗯，就是那样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2900211185V对你们有用吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010211186V#1018F是的，知道这些就已经足够了。\n',
            '谢谢你们二位的合作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0101, 400)

    ChrTalk(
        0x0105,
        (
            '#0060211187V#040F很有力的目击证词啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0105, 400)

    ChrTalk(
        0x0101,
        (
            '#0010211188V#1006F是啊……\n',
            '马上记录到笔记上吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000A, 90, 0)
    ChrSetFlags(0x000A, 0x0010)
    OP_4B(0x000A, 255)
    OP_4B(0x000B, 255)
    EventEnd(0x00)

    Return()

# id: 0x0003 offset: 0x1569
@scena.Code('func_03_1569')
def func_03_1569():
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrJumpToRelative(0x0101, 0, 0, -200, 400, 6000)
    OP_62(0x0105, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrJumpToRelative(0x0101, 0, 0, -100, 300, 6000)
    ChrJumpToRelative(0x0101, 0, 0, -100, 100, 6000)
    Sleep(400)

    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    Return()

# id: 0x0004 offset: 0x15F4
@scena.Code('func_04_15F4')
def func_04_15F4():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 5, 0x202D)),
            Expr.Return,
        ),
        'loc_16AB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1659',
    )

    ChrTalk(
        0x00FE,
        (
            '竟、竟然\n',
            '会发生这种事件……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样的话\n',
            '如果不早点向蕾娜\n',
            '道歉的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Jump('loc_16A8')

    def _loc_1659(): pass

    label('loc_1659')

    ChrTalk(
        0x00FE,
        (
            '这样的话\n',
            '如果不早点向蕾娜\n',
            '道歉的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '拜托了，\n',
            '请一定别出什么事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_16A8(): pass

    label('loc_16A8')

    Jump('loc_17CB')

    def _loc_16AB(): pass

    label('loc_16AB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0244, 1, 0x1221)),
            Expr.Return,
        ),
        'loc_1737',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_16EF',
    )

    ChrTalk(
        0x00FE,
        (
            '我一定要去\n',
            '旅行的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '怎么能回家去探亲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1734')

    def _loc_16EF(): pass

    label('loc_16EF')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '我一定要去\n',
            '旅行的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎哎，你只要不跟来\n',
            '不就可以了吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1734(): pass

    label('loc_1734')

    Jump('loc_17CB')

    def _loc_1737(): pass

    label('loc_1737')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 6, 0x121E)),
            Expr.Return,
        ),
        'loc_17CB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0246, 4, 0x1234)),
            Expr.Return,
        ),
        'loc_17BE',
    )

    ChrTalk(
        0x00FE,
        (
            '#2890211189V呜呜呜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2890211190V又把当时的事情\n',
            '全部想起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2890211191V呼，本来已经都\n',
            '忘干净了…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17CB')

    def _loc_17BE(): pass

    label('loc_17BE')

    SetScenaFlags(ScenaFlag(0x0246, 4, 0x1234))
    OP_28(0x0083, 0x01, 0x0020)
    Call(0, 0x0002)

    def _loc_17CB(): pass

    label('loc_17CB')

    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0x17CF
@scena.Code('func_05_17CF')
def func_05_17CF():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_17DC',
    )

    Jump('loc_1922')

    def _loc_17DC(): pass

    label('loc_17DC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0244, 1, 0x1221)),
            Expr.Return,
        ),
        'loc_1892',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_1837',
    )

    ChrTalk(
        0x00FE,
        (
            '要是小姐能老老实实回去\n',
            '就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在社交界中还有\n',
            '很多交际活动呢…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_188F')

    def _loc_1837(): pass

    label('loc_1837')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '小姐如果再继续故意任性的话\n',
            '又会让老爷不高兴的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '本来关系就已经很紧张了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_188F(): pass

    label('loc_188F')

    Jump('loc_1922')

    def _loc_1892(): pass

    label('loc_1892')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 6, 0x121E)),
            Expr.Return,
        ),
        'loc_1922',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0246, 4, 0x1234)),
            Expr.Return,
        ),
        'loc_1915',
    )

    ChrTalk(
        0x00FE,
        (
            '#2900211192V真希望芙拉瑟\n',
            '的态度能改变一下啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2900211193V就算拥有高贵的血统，\n',
            '也还是低调一点比较好吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1922')

    def _loc_1915(): pass

    label('loc_1915')

    SetScenaFlags(ScenaFlag(0x0246, 4, 0x1234))
    OP_28(0x0083, 0x01, 0x0020)
    Call(0, 0x0002)

    def _loc_1922(): pass

    label('loc_1922')

    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0x1926
@scena.Code('func_06_1926')
def func_06_1926():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_19F9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_199E',
    )

    ChrTalk(
        0x00FE,
        (
            '大家因为这次的事件\n',
            '都心慌意乱，正是大好机会啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我要趁现在拼命学习，\n',
            '把差距继续扩大。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Jump('loc_19F6')

    def _loc_199E(): pass

    label('loc_199E')

    ChrTalk(
        0x00FE,
        (
            '校园生活的准备工作\n',
            '和我一点关系也没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那是职员们的工作，\n',
            '我们学生没必要管。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_19F6(): pass

    label('loc_19F6')

    Jump('loc_1B9F')

    def _loc_19F9(): pass

    label('loc_19F9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_1AA3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_1A55',
    )

    ChrTalk(
        0x00FE,
        (
            '社团活动之类的东西\n',
            '也没有什么意义。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '学生的首要任务只有学习而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AA0')

    def _loc_1A55(): pass

    label('loc_1A55')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '呵呵，大家努力参加\n',
            '社团活动就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在那期间\n',
            '我会拼命学习的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1AA0(): pass

    label('loc_1AA0')

    Jump('loc_1B9F')

    def _loc_1AA3(): pass

    label('loc_1AA3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0244, 1, 0x1221)),
            Expr.Return,
        ),
        'loc_1AF9',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯，这次考试的分数\n',
            '也快下来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我的成绩排名前列\n',
            '肯定是没问题的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B9F')

    def _loc_1AF9(): pass

    label('loc_1AF9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 6, 0x121E)),
            Expr.Return,
        ),
        'loc_1B9F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_1B4B',
    )

    ChrTalk(
        0x00FE,
        (
            '没别的事了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那就别再打扰我了，\n',
            '我正在挑选参考书呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B9F')

    def _loc_1B4B(): pass

    label('loc_1B4B')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '干什么？\n',
            '现在忙得很啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……考试期间的奇异事件？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好像没什么哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1B9F(): pass

    label('loc_1B9F')

    TalkEnd(0x00FE)

    Return()

# id: 0x0007 offset: 0x1BA3
@scena.Code('func_07_1BA3')
def func_07_1BA3():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_1CEB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1C9A',
    )

    ChrTalk(
        0x00FE,
        (
            '啊，游击士……\n',
            '刚才干得漂亮啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然事件总算是顺利解决了，\n',
            '但接下来也很让人头疼呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '导力器现在无法运转……\n',
            '照明设施几乎完全瘫痪了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '也就是说，今天开始\n',
            '每天晚上都是漆黑一团。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼呼呼……\n',
            '我很期待呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_1CE8')

    def _loc_1C9A(): pass

    label('loc_1C9A')

    ChrTalk(
        0x00FE,
        (
            '一团漆黑的话\n',
            '总觉得很安祥平静。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵呵……\n',
            '没有灯火的夜晚最美丽了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1CE8(): pass

    label('loc_1CE8')

    Jump('loc_1E25')

    def _loc_1CEB(): pass

    label('loc_1CEB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0244, 1, 0x1221)),
            Expr.Return,
        ),
        'loc_1DA2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_1D46',
    )

    ChrTalk(
        0x00FE,
        (
            '明白了吧？\n',
            '是那个啦，那个。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵呵……\n',
            '大概是什么东西的怨灵吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D9F')

    def _loc_1D46(): pass

    label('loc_1D46')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '最近学院中的气氛\n',
            '很怪异呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '也许那种东西\n',
            '会出来也说不定吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼呼呼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1D9F(): pass

    label('loc_1D9F')

    Jump('loc_1E25')

    def _loc_1DA2(): pass

    label('loc_1DA2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 6, 0x121E)),
            Expr.Return,
        ),
        'loc_1E25',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_1DD6',
    )

    ChrTalk(
        0x00FE,
        (
            '呼呼呼……\n',
            '啊，我也不知道啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E25')

    def _loc_1DD6(): pass

    label('loc_1DD6')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '考试期间的奇异事件…\n',
            '好象没有，但…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼呼呼……\n',
            '啊，我也不知道啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1E25(): pass

    label('loc_1E25')

    TalkEnd(0x00FE)

    Return()

# id: 0x0008 offset: 0x1E29
@scena.Code('func_08_1E29')
def func_08_1E29():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 3, 0x202B)),
            Expr.Return,
        ),
        'loc_1EC8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1EB4',
    )

    ChrTalk(
        0x00FE,
        (
            '就算有什么骚动\n',
            '我们也会在这里不动的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '贸然行动的话，\n',
            '只会拖你们的后腿而已吧…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，\n',
            '要小心行事啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    Jump('loc_1EC8')

    def _loc_1EB4(): pass

    label('loc_1EB4')

    ChrTalk(
        0x00FE,
        (
            '要小心行事啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1EC8(): pass

    label('loc_1EC8')

    TalkEnd(0x00FE)

    Return()

# id: 0x0009 offset: 0x1ECC
@scena.Code('func_09_1ECC')
def func_09_1ECC():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 3, 0x202B)),
            Expr.Return,
        ),
        'loc_1F13',
    )

    ChrTalk(
        0x00FE,
        (
            '按照你们的指示，\n',
            '我们就在这里待命了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大家多保重。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1F13(): pass

    label('loc_1F13')

    TalkEnd(0x00FE)

    Return()

# id: 0x000A offset: 0x1F17
@scena.Code('func_0A_1F17')
def func_0A_1F17():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 5, 0x202D)),
            Expr.Return,
        ),
        'loc_1F9C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1F79',
    )

    ChrTalk(
        0x00FE,
        (
            '请、请一定把大家\n',
            '都救出来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我也会在这里祈祷\n',
            '大家平安无事的…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    Jump('loc_1F9C')

    def _loc_1F79(): pass

    label('loc_1F79')

    ChrTalk(
        0x00FE,
        (
            '请、请一定把大家\n',
            '都救出来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1F9C(): pass

    label('loc_1F9C')

    TalkEnd(0x00FE)

    Return()

# id: 0x000B offset: 0x1FA0
@scena.Code('func_0B_1FA0')
def func_0B_1FA0():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 5, 0x202D)),
            Expr.Return,
        ),
        'loc_207F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2033',
    )

    ChrTalk(
        0x00FE,
        (
            '听你们的，\n',
            '我就在这里不动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，基诺奇奥那小子\n',
            '没有乱来虽然很好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但他那种轻率的性格\n',
            '还是很让人担心啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    Jump('loc_207F')

    def _loc_2033(): pass

    label('loc_2033')

    ChrTalk(
        0x00FE,
        (
            '听你们的，\n',
            '我就在这里不动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '基诺奇奥那小子也\n',
            '没有乱来虽然很好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_207F(): pass

    label('loc_207F')

    TalkEnd(0x00FE)

    Return()

# id: 0x000C offset: 0x2083
@scena.Code('func_0C_2083')
def func_0C_2083():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2126',
    )

    ChrTalk(
        0x00FE,
        (
            '夜晚使用的油灯\n',
            '已经准备好了阿⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但遗憾的是没有\n',
            '可爱些的灯台啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真想早点找到一个草莓色的\n',
            '可爱灯台呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一会去找坎诺\n',
            '聊聊吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    Jump('loc_216A')

    def _loc_2126(): pass

    label('loc_2126')

    ChrTalk(
        0x00FE,
        (
            '真想要个草莓色的\n',
            '可爱灯台啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，一会赶快去找\n',
            '坎诺吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_216A(): pass

    label('loc_216A')

    TalkEnd(0x00FE)

    Return()

# id: 0x000D offset: 0x216E
@scena.Code('func_0D_216E')
def func_0D_216E():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_21F7',
    )

    ChrTalk(
        0x00FE,
        (
            '最近怎么总出\n',
            '事啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '雅莉丝已经准备好\n',
            '油灯了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '灯台虽然没有\n',
            '中意的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……不过暂时\n',
            '不去管它了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    Jump('loc_224F')

    def _loc_21F7(): pass

    label('loc_21F7')

    ChrTalk(
        0x00FE,
        (
            '虽然最近全都是\n',
            '那种事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '雅莉丝已经准备好\n',
            '油灯了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是乐天的性格啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_224F(): pass

    label('loc_224F')

    TalkEnd(0x00FE)

    Return()

# id: 0x000E offset: 0x2253
@scena.Code('func_0E_2253')
def func_0E_2253():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_2309',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_22C4',
    )

    ChrTalk(
        0x00FE,
        (
            '还是这么平静。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他现在是因为\n',
            '过度疲劳导致的昏倒。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还不确定什么时候能醒来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    Jump('loc_2309')

    def _loc_22C4(): pass

    label('loc_22C4')

    ChrTalk(
        0x00FE,
        (
            '他现在是因为\n',
            '过度疲劳导致的昏倒。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还不确定什么时候能醒来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2309(): pass

    label('loc_2309')

    TalkEnd(0x00FE)

    Return()

# id: 0x000F offset: 0x230D
@scena.Code('func_0F_230D')
def func_0F_230D():
    Call(0, 0x0010)

    Return()

# id: 0x0010 offset: 0x2312
@scena.Code('func_10_2312')
def func_10_2312():
    TalkBegin(0x0016)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_239D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_236E',
    )

    ChrTalk(
        0x0016,
        (
            '嗯嗯～………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '呼呼…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0016, 0xFFFFFED4, 1800, 0x1C, 0x21, 0x000000FA, 0x01)
    Sleep(1000)

    OP_63(0x0016)
    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    Jump('loc_239A')

    def _loc_236E(): pass

    label('loc_236E')

    ChrTalk(
        0x0016,
        (
            '呼呼…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0016, 0xFFFFFED4, 1800, 0x1C, 0x21, 0x000000FA, 0x01)
    Sleep(1000)

    OP_63(0x0016)

    def _loc_239A(): pass

    label('loc_239A')

    Jump('loc_23D8')

    def _loc_239D(): pass

    label('loc_239D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 3, 0x202B)),
            Expr.Return,
        ),
        'loc_23D8',
    )

    ChrTalk(
        0x0016,
        (
            '…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0016, 0xFFFFFED4, 1800, 0x1C, 0x21, 0x000000FA, 0x01)
    Sleep(1000)

    OP_63(0x0016)

    def _loc_23D8(): pass

    label('loc_23D8')

    TalkEnd(0x0016)

    Return()

# id: 0x0011 offset: 0x23DC
@scena.Code('func_11_23DC')
def func_11_23DC():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x041A, 4, 0x20D4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_26C7',
    )

    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrTurnDirection(0x00FE, 0x0101, 0)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '啊，是艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是谢谢你们了。\n',
            '不然还不知会怎么样呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1006F哪里，全靠协会的通知\n',
            '我们才能及时赶到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1043F确实啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '要是没有援军的话\n',
            '战斗肯定会很惨烈的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrTurnDirection(0x00FE, 0x0102, 0)
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '不、不要啊。\n',
            '我那个只是偶然。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '并不是和大叔一样\n',
            '的勇敢行为……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1002F勤务员先生怎么样了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '啊啊…\n',
            '没有生命危险。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只是疲劳过度，\n',
            '大概还要睡一阵子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1007F太好了，这样\n',
            '就不用再担心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '松了一口气呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大叔的事情就\n',
            '交给我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不好好照看他的话\n',
            '实在是过意不去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1025F是哦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1040F嗯，那就拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，有机会的话\n',
            '还要再来学院啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '艾丝蒂尔的话\n',
            '我们随时都欢迎。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1006F嗯，一言为定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1040F到时多关照关照了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x041A, 4, 0x20D4))

    Jump('loc_273C')

    def _loc_26C7(): pass

    label('loc_26C7')

    ChrTalk(
        0x00FE,
        (
            '我也这就要去\n',
            '给大叔道歉了…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不管怎么说，\n',
            '毕竟一个人逃跑也是事实……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不好好照看他的话\n',
            '实在是过意不去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_273C(): pass

    label('loc_273C')

    TalkEnd(0x00FE)

    Return()

# id: 0x0012 offset: 0x2740
@scena.Code('func_12_2740')
def func_12_2740():
    EventBegin(0x00)
    LoadChip('ED6_DT26/CH20209._CH', 'ED6_DT26/CH20209P._CP', 22)
    ChrSetFlags(0x0102, 0x0080)
    ChrSetPos(0x0010, 600, 0, -2740, 270)
    ChrSetPos(0x0011, -1130, 0, -2730, 90)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    ChrSetChipByIndex(0x0011, 22)
    ChrSetSubChip(0x0011, 0)
    CameraMove(4730, -250, -1620, 0)
    OP_67(0, 5870, -10000, 0)
    CameraSetDistance(3130, 0)
    OP_6C(315000, 0)
    OP_6E(277, 0)
    OP_62(0x0010, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x00)
    Sleep(50)

    OP_62(0x0011, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x00)
    FadeIn(1000, 0)
    CameraMove(-1280, -250, -1580, 3000)
    Sleep(1000)

    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021F, 6, 0x10FE))
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    NewScene('ED6_DT21/T2500._SN', 124, 0, 0)
    IdleLoop()

    Return()

# id: 0x0013 offset: 0x2827
@scena.Code('func_13_2827')
def func_13_2827():
    EventBegin(0x00)
    LoadChip('ED6_DT26/CH20209._CH', 'ED6_DT26/CH20209P._CP', 22)
    ChrSetFlags(0x0102, 0x0080)
    ChrSetPos(0x0010, 600, 0, -2740, 270)
    ChrSetPos(0x0011, -1130, 0, -2730, 90)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    ChrSetChipByIndex(0x0011, 22)
    ChrSetSubChip(0x0011, 0)
    CameraMove(-1280, -250, -1580, 0)
    OP_67(0, 5870, -10000, 0)
    CameraSetDistance(3130, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_62(0x0010, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x00)
    Sleep(50)

    OP_62(0x0011, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x00)
    FadeIn(1000, 0)
    Sleep(3000)

    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021F, 6, 0x10FE))
    SetScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    NewScene('ED6_DT21/T2500._SN', 124, 0, 0)
    IdleLoop()

    Return()

# id: 0x0014 offset: 0x28FD
@scena.Code('func_14_28FD')
def func_14_28FD():
    EventBegin(0x00)
    ChrSetFlags(0x0102, 0x0080)
    OP_4A(0x0014, 255)
    OP_4A(0x0015, 255)
    ChrSetFlags(0x0016, 0x0004)
    ChrSetPos(0x0014, -29450, 0, 30290, 270)
    ChrSetPos(0x0015, -30710, 0, 28800, 0)
    ChrSetPos(0x0016, -31700, -50, 30400, 90)
    ChrClearFlags(0x0014, 0x0080)
    ChrClearFlags(0x0015, 0x0080)
    ChrClearFlags(0x0016, 0x0080)
    ChrSetSubChip(0x0014, 0)
    ChrSetSubChip(0x0015, 0)
    OP_71(0x000F, 0x0004)
    OP_72(0x0010, 0x0004)
    CameraMove(-31890, 0, 30730, 0)
    OP_67(0, 5520, -10000, 0)
    CameraSetDistance(3040, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    FadeIn(1000, 0)
    Sleep(3000)

    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021F, 6, 0x10FE))
    SetScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    NewScene('ED6_DT21/T2500._SN', 124, 0, 0)
    IdleLoop()

    Return()

# id: 0x0015 offset: 0x29CD
@scena.Code('func_15_29CD')
def func_15_29CD():
    EventBegin(0x00)
    ChrSetFlags(0x0102, 0x0080)
    ChrSetPos(0x0017, -60450, 0, 28840, 315)
    ChrSetPos(0x0018, -61710, 0, 29010, 45)
    ChrSetPos(0x000A, -60810, 0, 29920, 180)
    OP_4A(0x0017, 255)
    OP_4A(0x0018, 255)
    OP_4A(0x000A, 255)
    ChrClearFlags(0x0017, 0x0080)
    ChrClearFlags(0x0018, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    CameraMove(-60840, 0, 29610, 0)
    OP_67(0, 6520, -10000, 0)
    CameraSetDistance(2900, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeIn(1000, 0)
    Sleep(3000)

    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021F, 6, 0x10FE))
    SetScenaFlags(ScenaFlag(0x021F, 4, 0x10FC))
    NewScene('ED6_DT21/T2500._SN', 123, 0, 0)
    IdleLoop()

    Return()

# id: 0x0016 offset: 0x2A88
@scena.Code('func_16_2A88')
def func_16_2A88():
    EventBegin(0x00)
    ChrSetFlags(0x0102, 0x0080)
    LoadChip('ED6_DT26/CH20209._CH', 'ED6_DT26/CH20209P._CP', 22)
    CreateThread(0x0010, 0x01, 0x00, func_17_2B0D)
    CreateThread(0x0011, 0x01, 0x00, func_18_2B65)
    CameraMove(-89450, 0, -3010, 0)
    OP_67(0, 5520, -10000, 0)
    CameraSetDistance(3150, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeIn(1000, 0)
    Sleep(3000)

    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021F, 6, 0x10FE))
    SetScenaFlags(ScenaFlag(0x021F, 5, 0x10FD))
    NewScene('ED6_DT21/T2500._SN', 123, 0, 0)
    IdleLoop()

    Return()

# id: 0x0017 offset: 0x2B0D
@scena.Code('func_17_2B0D')
def func_17_2B0D():
    ChrSetPos(0x0010, -90230, -250, -6440, 180)
    ChrSetChipByIndex(0x0010, 22)
    ChrClearFlags(0x0010, 0x0080)
    def _loc_2B28(): pass

    label('loc_2B28')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_2B64',
    )

    ChrSetDirection(0x0010, 90, 400)
    Sleep(700)

    ChrSetDirection(0x0010, 0, 400)
    Sleep(700)

    ChrSetDirection(0x0010, 270, 400)
    Sleep(700)

    ChrSetDirection(0x0010, 180, 400)
    Sleep(700)

    Jump('loc_2B28')

    def _loc_2B64(): pass

    label('loc_2B64')

    Return()

# id: 0x0018 offset: 0x2B65
@scena.Code('func_18_2B65')
def func_18_2B65():
    ChrSetPos(0x0011, -87160, 0, -3040, 270)
    ChrClearFlags(0x0011, 0x0080)
    def _loc_2B7B(): pass

    label('loc_2B7B')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_2BBD',
    )

    ChrWalkTo(0x0011, -93970, 0, -3050, 2000, 0x00)
    ChrSetDirection(0x00FE, 90, 400)
    ChrWalkTo(0x0011, -87160, 0, -3040, 2000, 0x00)
    ChrSetDirection(0x00FE, 270, 400)

    Jump('loc_2B7B')

    def _loc_2BBD(): pass

    label('loc_2BBD')

    Return()

# id: 0x0019 offset: 0x2BBE
@scena.Code('func_19_2BBE')
def func_19_2BBE():
    Call(0, 0x001A)
    Call(0, 0x001B)

    Return()

# id: 0x001A offset: 0x2BC7
@scena.Code('func_1A_2BC7')
def func_1A_2BC7():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    LoadChip('ED6_DT27/CH04000._CH', 'ED6_DT27/CH04000P._CP', 13)
    LoadChip('ED6_DT27/CH04001._CH', 'ED6_DT27/CH04001P._CP', 14)
    LoadChip('ED6_DT27/CH04010._CH', 'ED6_DT27/CH04010P._CP', 15)
    LoadChip('ED6_DT27/CH04011._CH', 'ED6_DT27/CH04011P._CP', 16)
    LoadChip('ED6_DT07/CH00420._CH', 'ED6_DT07/CH00420P._CP', 17)
    LoadChip('ED6_DT07/CH00421._CH', 'ED6_DT07/CH00421P._CP', 18)
    LoadChip('ED6_DT07/CH00410._CH', 'ED6_DT07/CH00410P._CP', 19)
    LoadChip('ED6_DT07/CH00411._CH', 'ED6_DT07/CH00411P._CP', 20)
    LoadChip('ED6_DT26/CH20209._CH', 'ED6_DT26/CH20209P._CP', 22)
    LoadChip('ED6_DT27/CH04621._CH', 'ED6_DT27/CH04621P._CP', 23)
    LoadChip('ED6_DT27/CH04611._CH', 'ED6_DT27/CH04611P._CP', 24)
    LoadChip('ED6_DT27/CH04620._CH', 'ED6_DT27/CH04620P._CP', 25)
    LoadChip('ED6_DT27/CH04610._CH', 'ED6_DT27/CH04610P._CP', 26)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0102, 0x0080)
    ChrSetFlags(0x010A, 0x0080)
    ChrSetFlags(0x010E, 0x0080)
    ChrSetPos(0x0010, 600, 0, -2740, 270)
    ChrSetPos(0x0011, -1130, 0, -2730, 90)
    ChrSetChipByIndex(0x0010, 4)
    ChrSetChipByIndex(0x0011, 22)
    ChrSetSubChip(0x0010, 0)
    ChrSetSubChip(0x0011, 0)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    CameraMove(-1830, -250, -1580, 0)
    OP_67(0, 4700, -10000, 0)
    CameraSetDistance(2860, 0)
    OP_6C(315000, 0)
    OP_6E(301, 0)
    OP_62(0x0010, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x00)
    Sleep(500)

    OP_62(0x0011, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x00)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    PlaySE(6, 0x00, 0x64)
    Sleep(500)

    OP_63(0x0010)

    @scena.Lambda('lambda_2D31')
    def lambda_2D31():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_2D31)

    Sleep(100)

    OP_63(0x0011)

    @scena.Lambda('lambda_2D47')
    def lambda_2D47():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_2D47)

    Sleep(400)

    @scena.Lambda('lambda_2D5A')
    def lambda_2D5A():
        CameraMove(-1210, 0, -4610, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2D5A)

    CreateThread(0x0101, 0x01, 0x00, func_1C_3151)
    Sleep(200)

    CreateThread(0x0102, 0x01, 0x00, func_1D_31A0)
    Sleep(200)

    CreateThread(0x010A, 0x01, 0x00, func_1E_31EF)
    Sleep(200)

    CreateThread(0x010E, 0x01, 0x00, func_1F_323E)
    WaitForThreadExit(0x010E, 0x0001)
    WaitForThreadExit(0x0101, 0x0000)
    TerminateThread(0x0101, 0x01)

    ChrTalk(
        0x0010,
        (
            '#4210360973V#2P……你们是？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#4220360974V#5P哼，还有没抓到的\n',
            '漏网学生吗──',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0010, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0011, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0010,
        (
            '#4210360975V#2P那、那个徽章是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#4220360861V#5P游、游击士！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010E,
        (
            '#0330360977V#845F#6P没错！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(300)

    Fade(250)
    PlaySE(213, 0x00, 0x64)
    ChrSetChipByIndex(0x0101, 13)
    ChrSetChipByIndex(0x0102, 15)
    ChrSetChipByIndex(0x010A, 17)
    ChrSetChipByIndex(0x010E, 19)
    ChrSetSubChip(0x0101, 0)
    ChrSetSubChip(0x0102, 0)
    ChrSetSubChip(0x010A, 0)
    ChrSetSubChip(0x010E, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x010A,
        (
            '#0120360978V#815F#6P你们\n',
            '觉悟吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2F06')
    def lambda_2F06():
        CameraMove(-1230, 0, -3110, 300)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2F06)

    @scena.Lambda('lambda_2F1E')
    def lambda_2F1E():
        CameraSetDistance(2600, 300)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2F1E)

    @scena.Lambda('lambda_2F2E')
    def lambda_2F2E():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, 3000, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2F2E)

    Sleep(20)

    PlaySE(216, 0x00, 0x64)
    ChrSetChipByIndex(0x0010, 25)
    ChrSetSubChip(0x0011, 0)

    @scena.Lambda('lambda_2F5D')
    def lambda_2F5D():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, 3000, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_2F5D)

    Sleep(20)

    PlaySE(213, 0x00, 0x64)
    ChrSetChipByIndex(0x0011, 26)
    ChrSetSubChip(0x0011, 0)

    @scena.Lambda('lambda_2F8C')
    def lambda_2F8C():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, 3000, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x010A, 0x0001, lambda_2F8C)

    Sleep(20)

    @scena.Lambda('lambda_2FAC')
    def lambda_2FAC():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, 3000, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x010E, 0x0001, lambda_2FAC)

    WaitForThreadExit(0x0101, 0x0003)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x010A, 0xFF)
    TerminateThread(0x010E, 0xFF)
    TerminateThread(0x0102, 0xFF)
    Battle(0x0000079B, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_2FEF'),
        (-1, 'loc_2FF4'),
    )

    def _loc_2FEF(): pass

    label('loc_2FEF')

    OP_B4(0x00)

    Jump('loc_2FF4')

    def _loc_2FF4(): pass

    label('loc_2FF4')

    Return()

# id: 0x001B offset: 0x2FF5
@scena.Code('func_1B_2FF5')
def func_1B_2FF5():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    ChrSetFlags(0x0010, 0x0080)
    ChrSetFlags(0x0011, 0x0080)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x010A, 0x01)
    TerminateThread(0x010E, 0x01)
    TerminateThread(0x0102, 0x01)
    Sleep(500)

    CameraMove(390, 0, -5570, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0102, 65535)
    ChrSetChipByIndex(0x010A, 65535)
    ChrSetChipByIndex(0x010E, 65535)
    ChrClearFlags(0x0000, 0x0080)
    ChrClearFlags(0x0001, 0x0080)
    ChrClearFlags(0x0002, 0x0080)
    ChrClearFlags(0x0003, 0x0080)
    ChrSetPos(0x0000, 390, 0, -5570, 0)
    ChrSetPos(0x0001, 390, 0, -5570, 0)
    ChrSetPos(0x0002, 390, 0, -5570, 0)
    ChrSetPos(0x0003, 390, 0, -5570, 0)
    OP_69(0x0000, 0)
    ChrSetPos(0x0010, -1570, 0, -2940, 0)
    ChrSetPos(0x0011, 480, 0, -3440, 0)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0010, 0x0001)
    ChrSetFlags(0x0010, 0x0002)
    ChrSetChipByIndex(0x0010, 12)
    ChrSetSubChip(0x0010, 8)
    ChrClearFlags(0x0011, 0x0001)
    ChrSetFlags(0x0011, 0x0002)
    ChrSetChipByIndex(0x0011, 12)
    ChrSetSubChip(0x0011, 11)
    SetScenaFlags(ScenaFlag(0x0405, 2, 0x202A))
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)
    MapSetFlags(0x02000000)

    Return()

# id: 0x001C offset: 0x3151
@scena.Code('func_1C_3151')
def func_1C_3151():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetPos(0x00FE, 860, -500, -9240, 0)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_3178')
    def lambda_3178():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_3178)

    ChrWalkTo(0x00FE, 730, -250, -7450, 5000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x001D offset: 0x31A0
@scena.Code('func_1D_31A0')
def func_1D_31A0():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetPos(0x00FE, -290, -500, -9230, 0)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_31C7')
    def lambda_31C7():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_31C7)

    ChrWalkTo(0x00FE, -470, -250, -7520, 5000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x001E offset: 0x31EF
@scena.Code('func_1E_31EF')
def func_1E_31EF():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetPos(0x00FE, 860, -500, -9240, 0)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_3216')
    def lambda_3216():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_3216)

    ChrWalkTo(0x00FE, 1260, -270, -8570, 5000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x001F offset: 0x323E
@scena.Code('func_1F_323E')
def func_1F_323E():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetPos(0x00FE, -290, -500, -9230, 0)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_3265')
    def lambda_3265():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_3265)

    ChrWalkTo(0x00FE, -430, -310, -8570, 5000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x0020 offset: 0x328D
@scena.Code('func_20_328D')
def func_20_328D():
    EventBegin(0x00)
    LoadChip('ED6_DT07/CH00415._CH', 'ED6_DT07/CH00415P._CP', 14)
    LoadChip('ED6_DT07/CH00416._CH', 'ED6_DT07/CH00416P._CP', 16)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0102, 0x0080)
    ChrSetFlags(0x010A, 0x0080)
    ChrSetFlags(0x010E, 0x0080)
    OP_4A(0x0014, 255)
    OP_4A(0x0015, 255)
    ChrSetPos(0x0014, -29450, 0, 30290, 270)
    ChrSetPos(0x0015, -30710, 0, 28800, 0)
    ChrClearFlags(0x0014, 0x0080)
    ChrClearFlags(0x0015, 0x0080)
    ChrClearFlags(0x0016, 0x0080)
    ChrSetFlags(0x0016, 0x0004)
    ChrSetPos(0x0016, -31700, -50, 30400, 90)
    OP_71(0x000F, 0x0004)
    OP_72(0x0010, 0x0004)
    CameraMove(-31660, 0, 30680, 0)
    OP_67(0, 5290, -10000, 0)
    CameraSetDistance(2190, 0)
    OP_6C(315000, 0)
    OP_6E(381, 0)
    LoadEffect(0x00, 'Craft\\\\cr000_00.eff')
    LoadEffect(0x01, 'magic\\\\mg112_0.eff')
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    PlaySE(6, 0x00, 0x64)
    Sleep(500)

    @scena.Lambda('lambda_3397')
    def lambda_3397():
        CameraMove(-30540, 0, 29960, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3397)

    @scena.Lambda('lambda_33AF')
    def lambda_33AF():
        OP_67(0, 5780, -10000, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_33AF)

    @scena.Lambda('lambda_33C7')
    def lambda_33C7():
        CameraSetDistance(2160, 2500)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_33C7)

    @scena.Lambda('lambda_33D7')
    def lambda_33D7():
        OP_6E(381, 2500)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_33D7)

    OP_62(0x0014, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_33FE')
    def lambda_33FE():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_33FE)

    Sleep(100)

    OP_62(0x0015, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_3428')
    def lambda_3428():
        ChrSetDirection(0x00FE, 135, 400)

        ExitThread()

    DispatchAsync(0x0015, 0x0001, lambda_3428)

    CreateThread(0x0101, 0x01, 0x00, func_21_3CE2)
    Sleep(200)

    CreateThread(0x0102, 0x01, 0x00, func_22_3D0D)
    Sleep(300)

    CreateThread(0x010A, 0x01, 0x00, func_23_3D3F)
    Sleep(300)

    CreateThread(0x010E, 0x01, 0x00, func_24_3D6A)
    WaitForThreadExit(0x0101, 0x0002)
    WaitForThreadExit(0x010A, 0x0001)

    ChrTalk(
        0x0014,
        (
            '#3990360979V#5P你、你们……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '#4000360980V#5P你们不是艾丝蒂尔\n',
            '和约修亚吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010360981V#1006F#6P二位，好久不见了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020360982V#1040F#6P长话短说，先把事情\n',
            '做个简单说明吧！',
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
            '将作战计划，以及解救人质\n',
            '的经过向大家说明。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0014,
        (
            '#3990360983V#5P是、是这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#3990360984V哇～游击士\n',
            '果然威风啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010360985V#1016F#6P哪、哪里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 315, 400)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010360986V#1002F#6P──对了，\n',
            '勤务员要不要紧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010360987V听说他遭到了枪击……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x010E, 315, 400)

    ChrTalk(
        0x0015,
        (
            '#4000360988V#5P嗯，不过幸好\n',
            '伤得不太重……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#4000360989V给他做了包扎之后\n',
            '就昏睡过去了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#4000360990V新学期才刚开始，\n',
            '本来正是大叔该忙的时候……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290399V#1007F#6P是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020360992V#1043F#6P脸色很不好，\n',
            '似乎是因为疲劳过度了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010E,
        (
            '#0330360993V#840F#6P嗯……让我来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_377B')
    def lambda_377B():
        CameraMove(-31390, 0, 30690, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_377B)

    CreateThread(0x0102, 0x00, 0x00, func_25_3D95)
    Sleep(300)

    CreateThread(0x010E, 0x00, 0x00, func_26_3DBB)
    Sleep(150)

    @scena.Lambda('lambda_37AB')
    def lambda_37AB():
        ChrTurnDirection(0x00FE, 0x010E, 400)
        Yield()

        Jump('lambda_37AB')

    DispatchAsync2(0x0101, 0x0001, lambda_37AB)

    Sleep(50)

    @scena.Lambda('lambda_37C1')
    def lambda_37C1():
        ChrTurnDirection(0x00FE, 0x010E, 400)
        Yield()

        Jump('lambda_37C1')

    DispatchAsync2(0x010A, 0x0001, lambda_37C1)

    Sleep(50)

    @scena.Lambda('lambda_37D7')
    def lambda_37D7():
        ChrTurnDirection(0x00FE, 0x010E, 400)
        Yield()

        Jump('lambda_37D7')

    DispatchAsync2(0x0015, 0x0001, lambda_37D7)

    Sleep(50)

    @scena.Lambda('lambda_37ED')
    def lambda_37ED():
        ChrTurnDirection(0x00FE, 0x010E, 400)
        Yield()

        Jump('lambda_37ED')

    DispatchAsync2(0x0014, 0x0001, lambda_37ED)

    WaitForThreadExit(0x010E, 0x0000)
    WaitForThreadExit(0x0101, 0x0002)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0102, 0x01)
    TerminateThread(0x010A, 0x01)
    TerminateThread(0x0015, 0x01)
    TerminateThread(0x0014, 0x01)
    Sleep(500)

    Fade(250)
    ChrSetSubChip(0x010E, 0)
    ChrSetChipByIndex(0x010E, 14)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x010E,
        (
            '#0330360994V#843F#6P方术──稳泛沧浪海天阔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x010E, 0)
    ChrSetChipByIndex(0x010E, 16)

    ExecExpressionWithValue(
        0x010E,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    ExecExpressionWithValue(
        0x010E,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(240)

    PlayEffect(0x00, 0x00, 0x010E, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    WaitEffect(0x00, 0x02)
    PlayEffect(0x01, 0x01, 0x0016, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_38FF')
    def lambda_38FF():
        ChrSetDirection(0x00FE, 315, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_38FF)

    Sleep(100)

    @scena.Lambda('lambda_3912')
    def lambda_3912():
        ChrSetDirection(0x00FE, 315, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_3912)

    Sleep(100)

    @scena.Lambda('lambda_3925')
    def lambda_3925():
        ChrSetDirection(0x00FE, 315, 400)

        ExitThread()

    DispatchAsync(0x010A, 0x0001, lambda_3925)

    Sleep(100)

    @scena.Lambda('lambda_3938')
    def lambda_3938():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0015, 0x0001, lambda_3938)

    Sleep(100)

    ChrSetDirection(0x0014, 270, 400)
    WaitEffect(0x01, 0x02)

    @scena.Lambda('lambda_3955')
    def lambda_3955():
        CameraMove(-31070, 0, 30140, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3955)

    ChrSetSubChip(0x010E, 0)
    ChrSetChipByIndex(0x010E, 65535)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010340674V#1004F#6P哇哇……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020360996V#1040F好厉害的法术。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120360997V#811F#6P嘿嘿，前辈的方术\n',
            '可是帮了我们无数次大忙的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#3990360998V#2P啊，大叔的脸色\n',
            '确实比刚才好多了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '#4000360999V#5P嗯，让他继续静养\n',
            '一阵就会没事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0015, 135, 400)
    Sleep(300)

    ChrTalk(
        0x0015,
        (
            '#4000361000V#5P──各位。\n',
            '非常感谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3AB0')
    def lambda_3AB0():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_3AB0)

    Sleep(100)

    ChrSetDirection(0x0014, 135, 400)

    ChrTalk(
        0x0015,
        (
            '#4000361001V#5P有什么事情可以\n',
            '让我们帮忙吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020361002V#1054F#4P不好意思，可以的话\n',
            '还是希望你们先待在这里。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020361003V外边现在还很危险。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '#4000361004V#5P是吗……那好吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#3990361005V#5P你们也要小心啊！',
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
            '取出游击士手册，\n',
            '在罗迪、罗伊斯、巴克斯勤务员\n',
            '的名字上做了标记了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0405, 3, 0x202B))
    OP_28(0x00C0, 0x01, 0x1000)
    OP_28(0x00C1, 0x02, 0x0040)
    OP_28(0x00C1, 0x01, 0x0080)
    FadeOut(1000, 0, -1)
    OP_0D()
    ChrSetDirection(0x0015, 0, 0)
    ChrSetDirection(0x0014, 270, 0)
    CameraMove(-28710, 0, 27260, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0000, -28730, 0, 27100, 180)
    ChrSetPos(0x0001, -28730, 0, 27100, 180)
    ChrSetPos(0x0002, -28730, 0, 27100, 180)
    ChrSetPos(0x0003, -28730, 0, 27100, 180)
    OP_69(0x0000, 0)
    OP_4B(0x0014, 255)
    OP_4B(0x0015, 255)
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)
    MapSetFlags(0x02000000)

    Return()

# id: 0x0021 offset: 0x3CE2
@scena.Code('func_21_3CE2')
def func_21_3CE2():
    ChrSetPos(0x00FE, -28530, 0, 20820, 0)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -29430, 0, 27600, 5000, 0x00)

    Return()

# id: 0x0022 offset: 0x3D0D
@scena.Code('func_22_3D0D')
def func_22_3D0D():
    ChrSetPos(0x00FE, -28530, 0, 20820, 0)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -28280, 0, 27530, 5000, 0x00)
    ChrSetDirection(0x00FE, 315, 400)

    Return()

# id: 0x0023 offset: 0x3D3F
@scena.Code('func_23_3D3F')
def func_23_3D3F():
    ChrSetPos(0x00FE, -28530, 0, 20820, 0)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -29260, 0, 26310, 5000, 0x00)

    Return()

# id: 0x0024 offset: 0x3D6A
@scena.Code('func_24_3D6A')
def func_24_3D6A():
    ChrSetPos(0x00FE, -28530, 0, 20820, 0)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -28040, 0, 26310, 5000, 0x00)

    Return()

# id: 0x0025 offset: 0x3D95
@scena.Code('func_25_3D95')
def func_25_3D95():
    ChrWalkTo(0x00FE, -27900, 0, 29050, 2000, 0x00)

    @scena.Lambda('lambda_3DAF')
    def lambda_3DAF():
        ChrTurnDirection(0x00FE, 0x010E, 400)
        Yield()

        Jump('lambda_3DAF')

    DispatchAsync2(0x0102, 0x0001, lambda_3DAF)

    Return()

# id: 0x0026 offset: 0x3DBB
@scena.Code('func_26_3DBB')
def func_26_3DBB():
    ChrWalkTo(0x00FE, -28420, 0, 28060, 2000, 0x00)
    ChrWalkTo(0x00FE, -29020, 0, 28620, 2000, 0x00)
    ChrSetDirection(0x00FE, 315, 400)

    Return()

# id: 0x0027 offset: 0x3DEB
@scena.Code('func_27_3DEB')
def func_27_3DEB():
    Call(0, 0x0028)
    Call(0, 0x0029)

    Return()

# id: 0x0028 offset: 0x3DF4
@scena.Code('func_28_3DF4')
def func_28_3DF4():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    LoadChip('ED6_DT27/CH04000._CH', 'ED6_DT27/CH04000P._CP', 13)
    LoadChip('ED6_DT27/CH04001._CH', 'ED6_DT27/CH04001P._CP', 14)
    LoadChip('ED6_DT27/CH04010._CH', 'ED6_DT27/CH04010P._CP', 15)
    LoadChip('ED6_DT27/CH04011._CH', 'ED6_DT27/CH04011P._CP', 16)
    LoadChip('ED6_DT07/CH00420._CH', 'ED6_DT07/CH00420P._CP', 17)
    LoadChip('ED6_DT07/CH00421._CH', 'ED6_DT07/CH00421P._CP', 18)
    LoadChip('ED6_DT07/CH00410._CH', 'ED6_DT07/CH00410P._CP', 19)
    LoadChip('ED6_DT07/CH00411._CH', 'ED6_DT07/CH00411P._CP', 20)
    LoadChip('ED6_DT26/CH20209._CH', 'ED6_DT26/CH20209P._CP', 22)
    LoadChip('ED6_DT27/CH04621._CH', 'ED6_DT27/CH04621P._CP', 23)
    LoadChip('ED6_DT27/CH04611._CH', 'ED6_DT27/CH04611P._CP', 24)
    LoadChip('ED6_DT27/CH04620._CH', 'ED6_DT27/CH04620P._CP', 25)
    LoadChip('ED6_DT27/CH04610._CH', 'ED6_DT27/CH04610P._CP', 26)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0102, 0x0080)
    ChrSetFlags(0x010A, 0x0080)
    ChrSetFlags(0x010E, 0x0080)
    ChrSetPos(0x0012, -91240, 0, -3150, 90)
    ChrSetPos(0x0013, -89920, 0, -3190, 270)
    ChrSetChipByIndex(0x0012, 4)
    ChrSetChipByIndex(0x0013, 22)
    ChrSetSubChip(0x0012, 0)
    ChrSetSubChip(0x0013, 0)
    ChrClearFlags(0x0012, 0x0080)
    ChrClearFlags(0x0013, 0x0080)
    CameraMove(-90060, 0, -2540, 0)
    OP_67(0, 5220, -10000, 0)
    CameraSetDistance(2900, 0)
    OP_6C(45000, 0)
    OP_6E(267, 0)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    PlaySE(6, 0x00, 0x64)
    Sleep(500)

    @scena.Lambda('lambda_3F32')
    def lambda_3F32():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_3F32)

    Sleep(100)

    @scena.Lambda('lambda_3F45')
    def lambda_3F45():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_3F45)

    Sleep(400)

    @scena.Lambda('lambda_3F58')
    def lambda_3F58():
        CameraMove(-89530, 0, -4660, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_3F58)

    @scena.Lambda('lambda_3F70')
    def lambda_3F70():
        CameraSetDistance(3070, 1000)

        ExitThread()

    DispatchAsync(0x0102, 0x0000, lambda_3F70)

    CreateThread(0x0101, 0x01, 0x00, func_2A_446A)
    Sleep(200)

    CreateThread(0x0102, 0x01, 0x00, func_2B_44C8)
    Sleep(200)

    CreateThread(0x010A, 0x01, 0x00, func_2C_4521)
    Sleep(200)

    CreateThread(0x010E, 0x01, 0x00, func_2D_457A)
    OP_62(0x0012, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(100)

    OP_62(0x0013, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0012,
        (
            '#4230361006V#5P你、你们是什么人？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#4250361007V#5P到这里干什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010361008V#1007F#6P那是我们的台词。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010361009V#1019F像你们这种老男人，\n',
            '来这种地方，\n',
            '难道不会觉得羞耻吗？！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#4230361010V#5P什、什么……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120361011V#1311F#6P女生宿舍\n',
            '是羞涩少女们的花园……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120361012V#816F怎么能让你们这种\n',
            '心怀不轨的大叔玷污。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0012, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x0013, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1200)

    OP_63(0x0012)
    OP_63(0x0013)
    Sleep(500)

    ChrTalk(
        0x0012,
        (
            '#4230361013V#5P#3S少、少愚弄人了！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#4250361014V#5P不、不要胡乱\n',
            '想象一些奇怪的东西！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_41E3')
    def lambda_41E3():
        CameraMove(-89560, 0, -4540, 150)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_41E3)

    @scena.Lambda('lambda_41FB')
    def lambda_41FB():
        CameraSetDistance(2800, 150)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_41FB)

    @scena.Lambda('lambda_420B')
    def lambda_420B():
        ChrMoveToRelativeAsync(0x00FE, -200, 0, 3000, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_420B)

    Sleep(20)

    ChrSetChipByIndex(0x0012, 23)
    ChrSetFlags(0x0012, 0x1000)

    @scena.Lambda('lambda_4235')
    def lambda_4235():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -3000, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_4235)

    @scena.Lambda('lambda_4250')
    def lambda_4250():
        ChrMoveToRelativeAsync(0x00FE, -200, 0, 3000, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_4250)

    Sleep(20)

    ChrSetChipByIndex(0x0013, 24)
    ChrSetFlags(0x0013, 0x1000)

    @scena.Lambda('lambda_427A')
    def lambda_427A():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -3000, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_427A)

    @scena.Lambda('lambda_4295')
    def lambda_4295():
        ChrMoveToRelativeAsync(0x00FE, -200, 0, 3000, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x010A, 0x0001, lambda_4295)

    Sleep(20)

    @scena.Lambda('lambda_42B5')
    def lambda_42B5():
        ChrMoveToRelativeAsync(0x00FE, -200, 0, 3000, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x010E, 0x0001, lambda_42B5)

    WaitForThreadExit(0x0101, 0x0003)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x010A, 0xFF)
    TerminateThread(0x010E, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0012, 0xFF)
    TerminateThread(0x0013, 0xFF)
    Battle(0x0000079C, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_4300'),
        (-1, 'loc_4305'),
    )

    def _loc_4300(): pass

    label('loc_4300')

    OP_B4(0x00)

    Jump('loc_4305')

    def _loc_4305(): pass

    label('loc_4305')

    Return()

# id: 0x0029 offset: 0x4306
@scena.Code('func_29_4306')
def func_29_4306():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    ChrSetFlags(0x0012, 0x0080)
    ChrSetFlags(0x0013, 0x0080)
    TerminateThread(0x0012, 0x01)
    TerminateThread(0x0013, 0x01)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x010A, 0x01)
    TerminateThread(0x010E, 0x01)
    TerminateThread(0x0102, 0x01)
    Sleep(500)

    CameraMove(-90270, 0, -5390, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0102, 65535)
    ChrSetChipByIndex(0x010A, 65535)
    ChrSetChipByIndex(0x010E, 65535)
    ChrClearFlags(0x0000, 0x0080)
    ChrClearFlags(0x0001, 0x0080)
    ChrClearFlags(0x0002, 0x0080)
    ChrClearFlags(0x0003, 0x0080)
    ChrSetPos(0x0000, -90270, 0, -5390, 0)
    ChrSetPos(0x0001, -90270, 0, -5390, 0)
    ChrSetPos(0x0002, -90270, 0, -5390, 0)
    ChrSetPos(0x0003, -90270, 0, -5390, 0)
    OP_69(0x0000, 0)
    ChrSetPos(0x0012, -88920, 0, -3130, 0)
    ChrSetPos(0x0013, -90170, 0, -3000, 0)
    ChrClearFlags(0x0012, 0x0080)
    ChrClearFlags(0x0013, 0x0080)
    ChrClearFlags(0x0012, 0x0001)
    ChrSetFlags(0x0012, 0x0002)
    ChrSetChipByIndex(0x0012, 12)
    ChrSetSubChip(0x0012, 9)
    ChrClearFlags(0x0013, 0x0001)
    ChrSetFlags(0x0013, 0x0002)
    ChrSetChipByIndex(0x0013, 12)
    ChrSetSubChip(0x0013, 14)
    SetScenaFlags(ScenaFlag(0x0405, 4, 0x202C))
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)
    MapSetFlags(0x02000000)

    Return()

# id: 0x002A offset: 0x446A
@scena.Code('func_2A_446A')
def func_2A_446A():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetChipByIndex(0x0101, 13)
    ChrSetPos(0x00FE, -90840, -500, -9250, 0)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_4496')
    def lambda_4496():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_4496)

    ChrWalkTo(0x00FE, -90510, -250, -7120, 5000, 0x00)
    ChrSetChipByIndex(0x0101, 13)
    ChrSetSubChip(0x00FE, 0)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x002B offset: 0x44C8
@scena.Code('func_2B_44C8')
def func_2B_44C8():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetChipByIndex(0x0102, 15)
    ChrSetPos(0x00FE, -89620, -500, -9230, 0)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_44F4')
    def lambda_44F4():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_44F4)

    ChrWalkTo(0x00FE, -89460, -250, -7390, 5000, 0x00)
    ChrSetSubChip(0x00FE, 0)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x002C offset: 0x4521
@scena.Code('func_2C_4521')
def func_2C_4521():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetChipByIndex(0x010A, 17)
    ChrSetPos(0x00FE, -90840, -500, -9250, 0)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_454D')
    def lambda_454D():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_454D)

    ChrWalkTo(0x00FE, -91130, -250, -8460, 5000, 0x00)
    ChrSetSubChip(0x00FE, 0)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x002D offset: 0x457A
@scena.Code('func_2D_457A')
def func_2D_457A():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetChipByIndex(0x010E, 19)
    ChrSetPos(0x00FE, -89620, -500, -9230, 0)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_45A6')
    def lambda_45A6():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_45A6)

    ChrWalkTo(0x00FE, -89610, -250, -8420, 5000, 0x00)
    ChrSetSubChip(0x00FE, 0)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x002E offset: 0x45D3
@scena.Code('func_2E_45D3')
def func_2E_45D3():
    EventBegin(0x00)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0102, 0x0080)
    ChrSetFlags(0x010A, 0x0080)
    ChrSetFlags(0x010E, 0x0080)
    ChrSetPos(0x0017, -60450, 0, 28840, 315)
    ChrSetPos(0x0018, -61710, 0, 29010, 45)
    ChrSetPos(0x000A, -60810, 0, 29920, 180)
    OP_4A(0x0017, 255)
    OP_4A(0x0018, 255)
    OP_4A(0x000A, 255)
    ChrClearFlags(0x0017, 0x0080)
    ChrClearFlags(0x0018, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    CameraMove(-60370, 0, 30030, 0)
    OP_67(0, 6100, -10000, 0)
    CameraSetDistance(2420, 0)
    OP_6C(45000, 0)
    OP_6E(305, 0)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    PlaySE(6, 0x00, 0x64)
    Sleep(500)

    @scena.Lambda('lambda_4693')
    def lambda_4693():
        CameraMove(-60370, 0, 28260, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_4693)

    @scena.Lambda('lambda_46AB')
    def lambda_46AB():
        OP_6E(325, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_46AB)

    OP_62(0x0017, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_46D2')
    def lambda_46D2():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0017, 0x0001, lambda_46D2)

    Sleep(100)

    OP_62(0x0018, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_46FC')
    def lambda_46FC():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_46FC)

    Sleep(100)

    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_4726')
    def lambda_4726():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_4726)

    CreateThread(0x0101, 0x01, 0x00, func_2F_4B3D)
    Sleep(400)

    CreateThread(0x0102, 0x01, 0x00, func_30_4B6F)
    Sleep(400)

    CreateThread(0x010A, 0x01, 0x00, func_31_4BA1)
    Sleep(400)

    CreateThread(0x010E, 0x01, 0x00, func_32_4BD3)
    WaitForThreadExit(0x0101, 0x0002)
    WaitForThreadExit(0x010E, 0x0001)

    ChrTalk(
        0x000A,
        (
            '#2890361015V#5P你、你们……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '#4010361016V#5P艾丝蒂尔、约修亚！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010361017V#1017F#6P嘿嘿，让大家久等了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020361018V#1040F#4P长话短说，先把事情\n',
            '做个简单说明吧！',
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
            '将作战计划，以及解救人质\n',
            '的经过向大家说明。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0017,
        (
            '#4020361019V#5P是这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#4020361020V呼……\n',
            '总算可以松口气了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2890361021V#5P那么……\n',
            '我们现在该怎么做？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '#4010361022V#5P去和其他人会合吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010361023V#1003F#6P嗯……\n',
            '战斗还没有结束，\n',
            '你们还是先在这里等一会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020361024V#1042F#4P我们一定会把大家都救出来，\n',
            '请放心吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '#4010361025V#5P是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2890361026V#5P……我明白了。\n',
            '一切都拜托你们了。',
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
            '取出游击士手册，\n',
            '在妮吉塔、芙拉瑟、黛拉的\n',
            '的名字上做了标记了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0405, 5, 0x202D))
    OP_28(0x00C0, 0x01, 0x2000)
    OP_28(0x00C1, 0x02, 0x0100)
    OP_28(0x00C1, 0x01, 0x0200)
    FadeOut(1000, 0, -1)
    OP_0D()
    ChrSetDirection(0x0015, 0, 0)
    ChrSetDirection(0x0014, 0, 0)
    CameraMove(-61470, 0, 26430, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0000, -61470, 0, 26430, 180)
    ChrSetPos(0x0001, -61470, 0, 26430, 180)
    ChrSetPos(0x0002, -61470, 0, 26430, 180)
    ChrSetPos(0x0003, -61470, 0, 26430, 180)
    OP_69(0x0000, 0)
    ChrSetDirection(0x0018, 45, 0)
    ChrSetDirection(0x000A, 180, 0)
    ChrSetDirection(0x0017, 315, 0)
    OP_4B(0x0017, 255)
    OP_4B(0x0018, 255)
    OP_4B(0x000A, 255)
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)
    MapSetFlags(0x02000000)

    Return()

# id: 0x002F offset: 0x4B3D
@scena.Code('func_2F_4B3D')
def func_2F_4B3D():
    ChrSetPos(0x00FE, -61530, 0, 20850, 0)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -61680, 0, 26630, 5000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x0030 offset: 0x4B6F
@scena.Code('func_30_4B6F')
def func_30_4B6F():
    ChrSetPos(0x00FE, -61530, 0, 20850, 0)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -60750, 0, 26610, 5000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x0031 offset: 0x4BA1
@scena.Code('func_31_4BA1')
def func_31_4BA1():
    ChrSetPos(0x00FE, -61530, 0, 20850, 0)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -61760, 0, 25630, 5000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x0032 offset: 0x4BD3
@scena.Code('func_32_4BD3')
def func_32_4BD3():
    ChrSetPos(0x00FE, -61530, 0, 20850, 0)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -60550, 0, 25630, 5000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
