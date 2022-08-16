import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T2130_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2130   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'T2130.x'
    header.mapIndex       = 1
    header.bgm            = 12
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT01/T2130._SN', 'ED6_DT01/T2130_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
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
        ('ED6_DT07/CH01390._CH', 'ED6_DT07/CH01390P._CP'),
        ('ED6_DT07/CH02590._CH', 'ED6_DT07/CH02590P._CP'),
        ('ED6_DT07/CH02570._CH', 'ED6_DT07/CH02570P._CP'),
        ('ED6_DT07/CH00050._CH', 'ED6_DT07/CH00050P._CP'),
        ('ED6_DT07/CH00370._CH', 'ED6_DT07/CH00370P._CP'),
        ('ED6_DT07/CH00371._CH', 'ED6_DT07/CH00371P._CP'),
        ('ED6_DT07/CH00373._CH', 'ED6_DT07/CH00373P._CP'),
        ('ED6_DT07/CH00374._CH', 'ED6_DT07/CH00374P._CP'),
        ('ED6_DT07/CH00100._CH', 'ED6_DT07/CH00100P._CP'),
        ('ED6_DT07/CH00110._CH', 'ED6_DT07/CH00110P._CP'),
        ('ED6_DT07/CH00140._CH', 'ED6_DT07/CH00140P._CP'),
        ('ED6_DT07/CH00101._CH', 'ED6_DT07/CH00101P._CP'),
        ('ED6_DT07/CH00111._CH', 'ED6_DT07/CH00111P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01670._CH', 'ED6_DT07/CH01670P._CP'),
        ('ED6_DT07/CH01410._CH', 'ED6_DT07/CH01410P._CP'),
        ('ED6_DT07/CH01023._CH', 'ED6_DT07/CH01023P._CP'),
        ('ED6_DT07/CH01003._CH', 'ED6_DT07/CH01003P._CP'),
        ('ED6_DT07/CH01053._CH', 'ED6_DT07/CH01053P._CP'),
        ('ED6_DT07/CH01043._CH', 'ED6_DT07/CH01043P._CP'),
        ('ED6_DT07/CH01213._CH', 'ED6_DT07/CH01213P._CP'),
        ('ED6_DT07/CH02510._CH', 'ED6_DT07/CH02510P._CP'),
        ('ED6_DT07/CH02520._CH', 'ED6_DT07/CH02520P._CP'),
        ('ED6_DT07/CH02530._CH', 'ED6_DT07/CH02530P._CP'),
        ('ED6_DT07/CH00450._CH', 'ED6_DT07/CH00450P._CP'),
        ('ED6_DT07/CH00451._CH', 'ED6_DT07/CH00451P._CP'),
        ('ED6_DT07/CH00453._CH', 'ED6_DT07/CH00453P._CP'),
        ('ED6_DT07/CH00454._CH', 'ED6_DT07/CH00454P._CP'),
        ('ED6_DT07/CH00460._CH', 'ED6_DT07/CH00460P._CP'),
        ('ED6_DT07/CH00461._CH', 'ED6_DT07/CH00461P._CP'),
        ('ED6_DT07/CH00463._CH', 'ED6_DT07/CH00463P._CP'),
        ('ED6_DT07/CH00464._CH', 'ED6_DT07/CH00464P._CP'),
        ('ED6_DT07/CH00470._CH', 'ED6_DT07/CH00470P._CP'),
        ('ED6_DT07/CH00471._CH', 'ED6_DT07/CH00471P._CP'),
        ('ED6_DT07/CH00473._CH', 'ED6_DT07/CH00473P._CP'),
        ('ED6_DT07/CH00474._CH', 'ED6_DT07/CH00474P._CP'),
        ('ED6_DT06/CH20058._CH', 'ED6_DT06/CH20058P._CP'),
        ('ED6_DT07/CH00051._CH', 'ED6_DT07/CH00051P._CP'),
        ('ED6_DT07/CH01393._CH', 'ED6_DT07/CH01393P._CP'),
    ]

# id: 0x10001 offset: 0x1E2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '迪恩',
            x                   = -4150,
            z                   = 0,
            y                   = 9070,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 21,
            chipIndex           = 21,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '雷斯',
            x                   = -4950,
            z                   = 0,
            y                   = 4460,
            direction           = 120,
            word_0E             = 0,
            dword_10            = 22,
            chipIndex           = 22,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            name                = '洛克',
            x                   = -2970,
            z                   = 0,
            y                   = 7390,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 23,
            chipIndex           = 23,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            name                = '巴克',
            x                   = -11930,
            z                   = 0,
            y                   = 4280,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '多姆斯',
            x                   = -11460,
            z                   = 0,
            y                   = 1930,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '加布',
            x                   = -10100,
            z                   = 0,
            y                   = 2930,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '克拉姆',
            x                   = -6030,
            z                   = 0,
            y                   = 4040,
            direction           = 270,
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
            name                = '特蕾莎院长',
            x                   = 0,
            z                   = 0,
            y                   = 33500,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '阿加特',
            x                   = 0,
            z                   = 0,
            y                   = 33500,
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
            name                = '吉米',
            x                   = 53000,
            z                   = 0,
            y                   = 48100,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0000,
        ),
        ScenaNpcData(
            name                = '照相机',
            x                   = 53000,
            z                   = 0,
            y                   = 33500,
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
            name                = '迪奥德罗教区长',
            x                   = 58900,
            z                   = 1000,
            y                   = 52200,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '修女芙丽达',
            x                   = 54400,
            z                   = 0,
            y                   = 50000,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '鲁特尔',
            x                   = 56580,
            z                   = 0,
            y                   = 42980,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 16,
            chipIndex           = 16,
            npcIndex            = 0x01D5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '兰达老人',
            x                   = 55130,
            z                   = 0,
            y                   = 45990,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x01D5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '米优',
            x                   = 56110,
            z                   = 0,
            y                   = 45990,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 18,
            chipIndex           = 18,
            npcIndex            = 0x01D5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '西加罗',
            x                   = 61600,
            z                   = 0,
            y                   = 45930,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 19,
            chipIndex           = 19,
            npcIndex            = 0x01D5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '艾德尔',
            x                   = 62560,
            z                   = 0,
            y                   = 45930,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 20,
            chipIndex           = 20,
            npcIndex            = 0x01D5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '贝尔夫',
            x                   = -11800,
            z                   = 250,
            y                   = 4070,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 38,
            chipIndex           = 38,
            npcIndex            = 0x0155,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            name                = '布鲁托',
            x                   = -11600,
            z                   = 250,
            y                   = 1950,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 38,
            chipIndex           = 38,
            npcIndex            = 0x0155,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            name                = '巴克',
            x                   = -10100,
            z                   = 0,
            y                   = 2930,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '多姆斯',
            x                   = 350,
            z                   = 0,
            y                   = 1410,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0011,
        ),
        ScenaNpcData(
            name                = '杰克',
            x                   = -13330,
            z                   = 600,
            y                   = 6230,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 38,
            chipIndex           = 38,
            npcIndex            = 0x0155,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0012,
        ),
        ScenaNpcData(
            name                = '皮卡罗',
            x                   = -7720,
            z                   = 0,
            y                   = 10340,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
    )

# id: 0x10002 offset: 0x4E2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x4E2
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x4E2
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 58980,
            triggerZ            = 1000,
            triggerY            = 50440,
            triggerRange        = 400,
            actorX              = 58900,
            actorZ              = 2500,
            actorY              = 52200,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x506
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_521',
    )

    ChrSetPos(0x0014, 62350, 0, 48350, 180)

    Jump('loc_67F')

    def _loc_521(): pass

    label('loc_521')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_569',
    )

    ChrSetPos(0x0014, 62350, 0, 48350, 180)
    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x001A, 0x0080)
    ChrSetFlags(0x001B, 0x0080)
    ChrSetFlags(0x001C, 0x0080)
    ChrSetFlags(0x001D, 0x0080)
    ChrSetFlags(0x001E, 0x0080)
    ChrSetFlags(0x001F, 0x0080)

    Jump('loc_67F')

    def _loc_569(): pass

    label('loc_569')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_584',
    )

    ChrSetPos(0x0014, -17370, 0, 42870, 270)

    Jump('loc_67F')

    def _loc_584(): pass

    label('loc_584')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 4, 0x42C)),
            Expr.Return,
        ),
        'loc_59F',
    )

    ChrSetPos(0x0014, 14600, 0, 44890, 270)

    Jump('loc_67F')

    def _loc_59F(): pass

    label('loc_59F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_5E7',
    )

    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x001A, 0x0080)
    ChrSetFlags(0x001B, 0x0080)
    ChrSetFlags(0x001C, 0x0080)
    ChrSetFlags(0x001D, 0x0080)
    ChrSetFlags(0x001E, 0x0080)
    ChrSetFlags(0x001F, 0x0080)
    ChrSetPos(0x0014, 14600, 0, 44890, 270)

    Jump('loc_67F')

    def _loc_5E7(): pass

    label('loc_5E7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_5F1',
    )

    Jump('loc_67F')

    def _loc_5F1(): pass

    label('loc_5F1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 0, 0x418)),
            Expr.Return,
        ),
        'loc_614',
    )

    ChrClearFlags(0x0015, 0x0080)
    ChrClearFlags(0x0016, 0x0080)
    ChrClearFlags(0x0017, 0x0080)
    ChrClearFlags(0x0018, 0x0080)
    ChrClearFlags(0x0019, 0x0080)

    Jump('loc_67F')

    def _loc_614(): pass

    label('loc_614')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 7, 0x417)),
            Expr.Return,
        ),
        'loc_61E',
    )

    Jump('loc_67F')

    def _loc_61E(): pass

    label('loc_61E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 4, 0x414)),
            Expr.Return,
        ),
        'loc_67F',
    )

    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0008, 0x0008)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x0009, 0x0008)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000A, 0x0008)
    ChrSetFlags(0x001A, 0x0080)
    ChrSetFlags(0x001A, 0x0008)
    ChrSetFlags(0x001B, 0x0080)
    ChrSetFlags(0x001B, 0x0008)
    ChrSetFlags(0x001C, 0x0080)
    ChrSetFlags(0x001C, 0x0008)
    ChrSetFlags(0x001D, 0x0080)
    ChrSetFlags(0x001D, 0x0008)
    ChrSetFlags(0x001E, 0x0080)
    ChrSetFlags(0x001E, 0x0008)
    ChrSetFlags(0x001F, 0x0080)
    ChrSetFlags(0x001F, 0x0008)

    def _loc_67F(): pass

    label('loc_67F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            (Expr.Eval, "OP_29(0x001E, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_6B7',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x001E, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6A1',
    )

    ChrClearFlags(0x0011, 0x0080)

    Jump('loc_6B7')

    def _loc_6A1(): pass

    label('loc_6A1')

    If(
        (
            (Expr.Eval, "OP_29(0x001E, 0x00, 0x04)"),
            (Expr.Eval, "OP_29(0x001E, 0x00, 0x40)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_6B7',
    )

    ChrClearFlags(0x0011, 0x0080)

    def _loc_6B7(): pass

    label('loc_6B7')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x0000006C, 'loc_6C3'),
        (-1, 'loc_6D9'),
    )

    def _loc_6C3(): pass

    label('loc_6C3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 4, 0x42C)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 3, 0x42B)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_6D6',
    )

    SetScenaFlags(ScenaFlag(0x0085, 4, 0x42C))
    Event(0, func_14_229D)

    def _loc_6D6(): pass

    label('loc_6D6')

    Jump('loc_6D9')

    def _loc_6D9(): pass

    label('loc_6D9')

    Return()

# id: 0x0001 offset: 0x6DA
@scena.Code('func_01_6DA')
def func_01_6DA():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 0, 0x418)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 4, 0x43C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Or,
            Expr.Return,
        ),
        'loc_6FB',
    )

    OP_B1('t2130_y')

    Jump('loc_704')

    def _loc_6FB(): pass

    label('loc_6FB')

    OP_B1('t2130_n')

    def _loc_704(): pass

    label('loc_704')

    Return()

# id: 0x0002 offset: 0x705
@scena.Code('func_02_705')
def func_02_705():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_71A',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_705')

    def _loc_71A(): pass

    label('loc_71A')

    Return()

# id: 0x0003 offset: 0x71B
@scena.Code('func_03_71B')
def func_03_71B():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_73E',
    )

    OP_8D(0x00FE, -8060, 7500, -1360, 2009, 1500)

    Jump('func_03_71B')

    def _loc_73E(): pass

    label('loc_73E')

    Return()

# id: 0x0004 offset: 0x73F
@scena.Code('func_04_73F')
def func_04_73F():
    TalkBegin(0x0013)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_83F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7DE',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x0013,
        (
            '市长被金钱蒙蔽了双眼，\n',
            '做出了犯罪的行径。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '希望这片地区不要因此\n',
            '陷入一片混乱才好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '空之女神啊……\n',
            '请给予我们指引吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_83C')

    def _loc_7DE(): pass

    label('loc_7DE')

    ChrTalk(
        0x0013,
        (
            '市长被金钱蒙蔽了双眼，\n',
            '做出了犯罪的行径。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '希望这片地区不要因此\n',
            '陷入一片混乱才好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_83C(): pass

    label('loc_83C')

    Jump('loc_D58')

    def _loc_83F(): pass

    label('loc_83F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_881',
    )

    ChrTalk(
        0x0013,
        (
            '说起来，\n',
            '这里的市长平时很忙，\n',
            '很少来教会里看看呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D58')

    def _loc_881(): pass

    label('loc_881')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            Expr.Return,
        ),
        'loc_9A6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_93C',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x0013,
        (
            '祈求所有人都能受到女神的祝福……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '……呼，一天终于结束了。\n',
            '今天的观光客还是和往常一样多啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '可能市长会非常高兴吧，\n',
            '不过他是不是忘了一件很重要的事情呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9A3')

    def _loc_93C(): pass

    label('loc_93C')

    ChrTalk(
        0x0013,
        (
            '今天的观光客还是和往常一样多啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '可能市长会非常高兴吧，\n',
            '不过他是不是忘了一件很重要的事情呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9A3(): pass

    label('loc_9A3')

    Jump('loc_D58')

    def _loc_9A6(): pass

    label('loc_9A6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_AE1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_AA3',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x0013,
        (
            '多亏了导力器，\n',
            '很多事情做起来都变得很方便了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '不过自从飞艇被发明以来，\n',
            '卢安的港口就变得非常冷清了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '七耀教会在如今的世界\n',
            '也渐渐变成了一座被人们遗忘的雕像。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '我只希望卢安的市民至少不要\n',
            '忘记对爱德丝女神的信仰……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_ADE')

    def _loc_AA3(): pass

    label('loc_AA3')

    ChrTalk(
        0x0013,
        (
            '我只希望卢安的市民至少不要\n',
            '忘记对爱德丝女神的信仰……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_ADE(): pass

    label('loc_ADE')

    Jump('loc_D58')

    def _loc_AE1(): pass

    label('loc_AE1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_BEB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B7E',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x0013,
        (
            '如今来这里的人当中，\n',
            '观光客人数要比本地居民多很多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '其中也有没礼貌的家伙。\n',
            '做弥撒的时候吵吵闹闹的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '让人头痛啊，真是的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BE8')

    def _loc_B7E(): pass

    label('loc_B7E')

    ChrTalk(
        0x0013,
        (
            '如今来这里的人当中，\n',
            '观光客人数要比本地居民多很多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '其中也有没礼貌的家伙。\n',
            '让人头痛啊，真是的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BE8(): pass

    label('loc_BE8')

    Jump('loc_D58')

    def _loc_BEB(): pass

    label('loc_BEB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_C16',
    )

    ChrTalk(
        0x0013,
        (
            '呼，\n',
            '早晨的弥撒好冷清啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D58')

    def _loc_C16(): pass

    label('loc_C16')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 0, 0x418)),
            Expr.Return,
        ),
        'loc_C39',
    )

    ChrTalk(
        0x0013,
        (
            '各位，\n',
            '请认真祈祷。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D58')

    def _loc_C39(): pass

    label('loc_C39')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_D58',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_CE1',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x0013,
        (
            '很久以前，\n',
            '这里曾是海盗的盘踞之地。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '不过最近经由杂志\n',
            '以『海之教会』之名宣传了之后，\n',
            '竟然变成了一个观光胜地。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '世事真是变化莫测啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D58')

    def _loc_CE1(): pass

    label('loc_CE1')

    ChrTalk(
        0x0013,
        (
            '很久以前，\n',
            '这里曾是海盗的盘踞之地。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '不过最近经由杂志\n',
            '以『海之教会』之名宣传了之后，\n',
            '完全变成了一个观光胜地。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D58(): pass

    label('loc_D58')

    TalkEnd(0x0013)

    Return()

# id: 0x0005 offset: 0xD5C
@scena.Code('func_05_D5C')
def func_05_D5C():
    TalkBegin(0x0014)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_E44',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_DF7',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '把幼小的孩子也牵连进去了……\n',
            '真是让人痛心的事件啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '教区长曾经\n',
            '去孤儿院探望过\n',
            '那些可怜的孩子们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '下次我也要一起去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E41')

    def _loc_DF7(): pass

    label('loc_DF7')

    ChrTalk(
        0x00FE,
        (
            '教区长曾经\n',
            '去孤儿院探望过\n',
            '那些可怜的孩子们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '下次我也要一起去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E41(): pass

    label('loc_E41')

    Jump('loc_10C4')

    def _loc_E44(): pass

    label('loc_E44')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_EAE',
    )

    ChrTalk(
        0x00FE,
        (
            '在卢安居住的居民\n',
            '大多数都很繁忙的样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '从这一点可以看出\n',
            '城里总有一股积极向上的势头。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10C4')

    def _loc_EAE(): pass

    label('loc_EAE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            Expr.Return,
        ),
        'loc_EFB',
    )

    ChrTalk(
        0x00FE,
        (
            '今天傍晚的弥撒也很壮观。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '教区长看起来\n',
            '好像有一些疲惫……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10C4')

    def _loc_EFB(): pass

    label('loc_EFB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_F49',
    )

    ChrTalk(
        0x00FE,
        (
            '我们的教区长\n',
            '平时看起来挺普通的，\n',
            '其实他比其他人都要虔诚得多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10C4')

    def _loc_F49(): pass

    label('loc_F49')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_F97',
    )

    ChrTalk(
        0x00FE,
        (
            '呵呵……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '教区长好像不太喜欢\n',
            '别人把这个教会\n',
            '当作观光胜地。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10C4')

    def _loc_F97(): pass

    label('loc_F97')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_FE0',
    )

    ChrTalk(
        0x00FE,
        (
            '早上好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在正要开始早晨的弥撒。\n',
            '一起来唱诵赞歌吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10C4')

    def _loc_FE0(): pass

    label('loc_FE0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 0, 0x418)),
            Expr.Return,
        ),
        'loc_104C',
    )

    ChrTalk(
        0x00FE,
        (
            '现在正在举行傍晚的弥撒。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这个时间有许多观光客\n',
            '为了看夕阳照射下的彩色玻璃\n',
            '而聚集到这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10C4')

    def _loc_104C(): pass

    label('loc_104C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_10C4',
    )

    ChrTalk(
        0x00FE,
        (
            '这里一到傍晚，\n',
            '海面上的夕阳照射在彩色玻璃上，\n',
            '看起来非常漂亮。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '建筑物也非常漂亮，\n',
            '特别受到女性的欢迎。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_10C4(): pass

    label('loc_10C4')

    TalkEnd(0x0014)

    Return()

# id: 0x0006 offset: 0x10C8
@scena.Code('func_06_10C8')
def func_06_10C8():
    TalkBegin(0x0015)

    ChrTalk(
        0x00FE,
        (
            '哈哈，这个真漂亮……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0015)

    Return()

# id: 0x0007 offset: 0x10E9
@scena.Code('func_07_10E9')
def func_07_10E9():
    TalkBegin(0x0016)

    ChrTalk(
        0x00FE,
        (
            '哦哦，这真是壮观啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0016)

    Return()

# id: 0x0008 offset: 0x110A
@scena.Code('func_08_110A')
def func_08_110A():
    TalkBegin(0x0017)

    ChrTalk(
        0x00FE,
        (
            '哇～！\n',
            '爷爷，快看快看！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好漂亮啊……\n',
            '和观光导游书上说的一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0017)

    Return()

# id: 0x0009 offset: 0x1159
@scena.Code('func_09_1159')
def func_09_1159():
    TalkBegin(0x0018)

    ChrTalk(
        0x00FE,
        (
            '巡礼也平安无事地结束了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '自从出来旅游之后，\n',
            '这还是我第一次和妻子就想去的地方达成一致。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0018)

    Return()

# id: 0x000A offset: 0x11C3
@scena.Code('func_0A_11C3')
def func_0A_11C3():
    TalkBegin(0x0019)

    ChrTalk(
        0x00FE,
        (
            '反射在水面上的夕阳\n',
            '透过彩色玻璃照射进来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好漂亮……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0019)

    Return()

# id: 0x000B offset: 0x1209
@scena.Code('func_0B_1209')
def func_0B_1209():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_1296',
    )

    ChrTalk(
        0x00FE,
        (
            '#0450070144V我们好像被市长操纵，\n',
            '做了许多十分霸道的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0450070145V偏偏被那个市长耍得团团转……\n',
            '……我们真没面子呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1428')

    def _loc_1296(): pass

    label('loc_1296')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_131D',
    )

    ChrTalk(
        0x00FE,
        (
            '#0450050994V阿加特大哥，\n',
            '不知道为什么突然紧急回到卢安了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0450050995V没办法啊……\n',
            '大哥在卢安的时候\n',
            '我就老实点吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1428')

    def _loc_131D(): pass

    label('loc_131D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_139B',
    )

    ChrTalk(
        0x00FE,
        (
            '#0450050578V疼疼疼……\n',
            '还是那么可怕的力量啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0450050579V阿加特大哥，\n',
            '不知道为什么突然紧急回到卢安了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1428')

    def _loc_139B(): pass

    label('loc_139B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_13EC',
    )

    ChrTalk(
        0x00FE,
        (
            '#0450050070V哼，\n',
            '昨天我好像喝过头了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0450050071V头好晕啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1428')

    def _loc_13EC(): pass

    label('loc_13EC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 4, 0x414)),
            Expr.Return,
        ),
        'loc_1428',
    )

    ChrTalk(
        0x00FE,
        (
            '#0450041222V干、干什么呀，\n',
            '你们竟然会到这里来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1428(): pass

    label('loc_1428')

    TalkEnd(0x0008)

    Return()

# id: 0x000C offset: 0x142C
@scena.Code('func_0C_142C')
def func_0C_142C():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_14CF',
    )

    ChrTalk(
        0x00FE,
        (
            '#0470070146V哼，\n',
            '为什么非得生我的气不可啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0470070147V今天我还被军队里的\n',
            '那个大姐狠狠地教训了一顿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0470070148V我还真是命犯桃花啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1649')

    def _loc_14CF(): pass

    label('loc_14CF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_1586',
    )

    ChrTalk(
        0x00FE,
        (
            '#0470050996V好痛痛痛痛，可恶，\n',
            '也不用这么用力打我吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0470050997V那个人成为游击士之后\n',
            '是不是就越来越有蛮力了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0470050998V这样的话，\n',
            '我还是暂时老实点吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1649')

    def _loc_1586(): pass

    label('loc_1586')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_15BF',
    )

    ChrTalk(
        0x00FE,
        (
            '#0470050580V不行了，\n',
            '还是敌不过那个人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1649')

    def _loc_15BF(): pass

    label('loc_15BF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_1618',
    )

    ChrTalk(
        0x0009,
        (
            '#0470050072V啊～哈哈哈！\n',
            '我喝不下了！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0470050073V啊～嗝……嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1649')

    def _loc_1618(): pass

    label('loc_1618')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 4, 0x414)),
            Expr.Return,
        ),
        'loc_1649',
    )

    ChrTalk(
        0x00FE,
        (
            '#0470041223V……什么呀，不要看着我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1649(): pass

    label('loc_1649')

    TalkEnd(0x0009)

    Return()

# id: 0x000D offset: 0x164D
@scena.Code('func_0D_164D')
def func_0D_164D():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_170F',
    )

    ChrTalk(
        0x00FE,
        (
            '#0460070149V我醒来的时候\n',
            '已经被抓到军队的飞艇上了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0460070150V穿蓝白相间军装的大姐\n',
            '把我们所犯下的罪行\n',
            '一条一条地陈列了出来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0460070151V………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1875')

    def _loc_170F(): pass

    label('loc_170F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_1799',
    )

    ChrTalk(
        0x00FE,
        (
            '#0460050999V啊哇哇，\n',
            '没、没想到那个人竟然回来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0460051000V……我还以为会被杀了呢。\n',
            '他还是那样有惊人的威慑力啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1875')

    def _loc_1799(): pass

    label('loc_1799')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_17FE',
    )

    ChrTalk(
        0x00FE,
        (
            '#0460050581V啊哇哇，\n',
            '没、没想到那个人竟然回来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0460050582V从来没听说过啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1875')

    def _loc_17FE(): pass

    label('loc_17FE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_1837',
    )

    ChrTalk(
        0x00FE,
        (
            '#0460050074V怎么了，\n',
            '想和我们比试比试吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1875')

    def _loc_1837(): pass

    label('loc_1837')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 4, 0x414)),
            Expr.Return,
        ),
        'loc_1875',
    )

    ChrTalk(
        0x00FE,
        (
            '#0460041224V哼，各位游击士大人\n',
            '来这里有何贵干呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1875(): pass

    label('loc_1875')

    TalkEnd(0x000A)

    Return()

# id: 0x000E offset: 0x1879
@scena.Code('func_0E_1879')
def func_0E_1879():
    TalkBegin(0x001A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_18C7',
    )

    ChrTalk(
        0x00FE,
        (
            '疼呀………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这个伤口看来是\n',
            '阿加特大哥的剑留下的…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A66')

    def _loc_18C7(): pass

    label('loc_18C7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_1947',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然我以前听说过他，\n',
            '但没有想到那就是阿加特大哥……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '果然是像迅雷一样的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '迪恩他们\n',
            '都变得唯唯诺诺了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A66')

    def _loc_1947(): pass

    label('loc_1947')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_198A',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然我以前听说过他，\n',
            '但没有想到那就是阿加特大哥……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A66')

    def _loc_198A(): pass

    label('loc_198A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_1A24',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1A07',
    )

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    ChrTalk(
        0x00FE,
        (
            '我好想回家啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啰嗦的老爸老妈\n',
            '是不是在家里等着我呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不……\n',
            '已经不会有什么人在等我了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A21')

    def _loc_1A07(): pass

    label('loc_1A07')

    ChrTalk(
        0x00FE,
        (
            '呆在这里是最开心的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A21(): pass

    label('loc_1A21')

    Jump('loc_1A66')

    def _loc_1A24(): pass

    label('loc_1A24')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 4, 0x414)),
            Expr.Return,
        ),
        'loc_1A66',
    )

    ChrTalk(
        0x00FE,
        (
            '对于那些贪赃枉法的大人们所考虑的事情，\n',
            '我已经厌烦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A66(): pass

    label('loc_1A66')

    TalkEnd(0x001A)

    Return()

# id: 0x000F offset: 0x1A6A
@scena.Code('func_0F_1A6A')
def func_0F_1A6A():
    TalkBegin(0x001B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_1ABE',
    )

    ChrTalk(
        0x00FE,
        (
            '基尔巴特和我们\n',
            '被带上了不同的飞艇。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那家伙被带到哪里去了呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1BDA')

    def _loc_1ABE(): pass

    label('loc_1ABE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_1B65',
    )

    ChrTalk(
        0x00FE,
        (
            '他还是和以前\n',
            '一样的可怕啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '阿加特大哥\n',
            '以前就对我们很严厉，\n',
            '我和迪恩他们都非常尊敬他。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '渡鸦帮变成现在这样，\n',
            '是阿加特大哥\n',
            '走了之后的事情了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1BDA')

    def _loc_1B65(): pass

    label('loc_1B65')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_1B92',
    )

    ChrTalk(
        0x00FE,
        (
            '他还是和以前\n',
            '一样的可怕啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1BDA')

    def _loc_1B92(): pass

    label('loc_1B92')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_1BBB',
    )

    ChrTalk(
        0x00FE,
        (
            '喂，\n',
            '有什么好玩的事情吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1BDA')

    def _loc_1BBB(): pass

    label('loc_1BBB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 4, 0x414)),
            Expr.Return,
        ),
        'loc_1BDA',
    )

    ChrTalk(
        0x00FE,
        (
            '……嗯～好无聊啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1BDA(): pass

    label('loc_1BDA')

    TalkEnd(0x001B)

    Return()

# id: 0x0010 offset: 0x1BDE
@scena.Code('func_10_1BDE')
def func_10_1BDE():
    TalkBegin(0x001C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_1C60',
    )

    ChrTalk(
        0x00FE,
        (
            '雷斯向军队里\n',
            '那个短发的大姐挑战。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但没一会儿工夫\n',
            '那家伙就被打败回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最近的好多女人\n',
            '都又强又可爱㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1DAC')

    def _loc_1C60(): pass

    label('loc_1C60')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_1CBE',
    )

    ChrTalk(
        0x00FE,
        (
            '巧克力香烟吃吗？\n',
            '我很喜欢这个。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然我也坏，\n',
            '但是我敌不过阿加特大哥啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1DAC')

    def _loc_1CBE(): pass

    label('loc_1CBE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_1CF1',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然我也坏，\n',
            '但是我不过那个人啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1DAC')

    def _loc_1CF1(): pass

    label('loc_1CF1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_1D5E',
    )

    ChrTalk(
        0x00FE,
        (
            '昨天虽然有点害怕，\n',
            '但是从渔船那里\n',
            '抢来了一条沙丁鱼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，别看我这样，\n',
            '其实我也很坏吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1DAC')

    def _loc_1D5E(): pass

    label('loc_1D5E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 4, 0x414)),
            Expr.Return,
        ),
        'loc_1DAC',
    )

    ChrTalk(
        0x00FE,
        (
            '今天在路边捡到的１米拉，\n',
            '老子占为己有了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，我很邪恶吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1DAC(): pass

    label('loc_1DAC')

    TalkEnd(0x001C)

    Return()

# id: 0x0011 offset: 0x1DB0
@scena.Code('func_11_1DB0')
def func_11_1DB0():
    TalkBegin(0x001D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_1E1D',
    )

    ChrTalk(
        0x00FE,
        (
            '我只记得基尔巴特那家伙\n',
            '来这里时的事情……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对于我们所犯的罪行，\n',
            '真的是一点也不记得了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1FC2')

    def _loc_1E1D(): pass

    label('loc_1E1D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_1EAC',
    )

    ChrTalk(
        0x00FE,
        (
            '要是我知道\n',
            '阿加特大哥会回来，\n',
            '早就从仓库逃走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他真是引人注目啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '头发的颜色和那把大剑，\n',
            '站在城里马上就会被认出来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1FC2')

    def _loc_1EAC(): pass

    label('loc_1EAC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_1F10',
    )

    ChrTalk(
        0x00FE,
        (
            '要是我知道\n',
            '阿加特大哥会回来，\n',
            '早就从仓库逃走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '做人就是要像他那样顶天立地啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1FC2')

    def _loc_1F10(): pass

    label('loc_1F10')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_1F6B',
    )

    ChrTalk(
        0x00FE,
        (
            '因为没什么事情可以做，\n',
            '所以就都聚集到这里来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们真是在浪费青春啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1FC2')

    def _loc_1F6B(): pass

    label('loc_1F6B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 4, 0x414)),
            Expr.Return,
        ),
        'loc_1FC2',
    )

    ChrTalk(
        0x00FE,
        (
            '我可不会干那些\n',
            '惹祸上身的麻烦事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果发生什么事，\n',
            '我马上就远走高飞。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1FC2(): pass

    label('loc_1FC2')

    TalkEnd(0x001D)

    Return()

# id: 0x0012 offset: 0x1FC6
@scena.Code('func_12_1FC6')
def func_12_1FC6():
    TalkBegin(0x001E)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_1FF8',
    )

    ChrTalk(
        0x00FE,
        (
            '那个市长\n',
            '比起我们来可坏得多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2135')

    def _loc_1FF8(): pass

    label('loc_1FF8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_2049',
    )

    ChrTalk(
        0x00FE,
        (
            '那就是阿加特前辈吗。\n',
            '真是吓我一跳啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那的确是他本人啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2135')

    def _loc_2049(): pass

    label('loc_2049')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_207F',
    )

    ChrTalk(
        0x00FE,
        (
            '哇～他就是阿加特前辈啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真酷啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2135')

    def _loc_207F(): pass

    label('loc_207F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_20C6',
    )

    ChrTalk(
        0x00FE,
        (
            '啊～啊，\n',
            '哪里可以轻松地搞到钱啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '赌吧也关门了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2135')

    def _loc_20C6(): pass

    label('loc_20C6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 4, 0x414)),
            Expr.Return,
        ),
        'loc_2135',
    )

    ChrTalk(
        0x00FE,
        (
            '呼啊～啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我觉得工作\n',
            '是一件很麻烦的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '被家人赶出来的确很迷惘，\n',
            '不知不觉就到了这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2135(): pass

    label('loc_2135')

    TalkEnd(0x001E)

    Return()

# id: 0x0013 offset: 0x2139
@scena.Code('func_13_2139')
def func_13_2139():
    TalkBegin(0x001F)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_2191',
    )

    ChrTalk(
        0x00FE,
        (
            '……（发抖）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是这次的事被阿加特大哥知道的话，\n',
            '肯定又要挨揍了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2299')

    def _loc_2191(): pass

    label('loc_2191')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_21D4',
    )

    ChrTalk(
        0x00FE,
        (
            '……（发抖）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我一点也没有想到\n',
            '阿加特大哥会来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2299')

    def _loc_21D4(): pass

    label('loc_21D4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_220F',
    )

    ChrTalk(
        0x00FE,
        (
            '……（发抖）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '太可怕了，\n',
            '我都站不稳了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2299')

    def _loc_220F(): pass

    label('loc_220F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_2246',
    )

    ChrTalk(
        0x00FE,
        (
            '唉，我一说要离开渡鸦帮，\n',
            '他们就发怒了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2299')

    def _loc_2246(): pass

    label('loc_2246')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 4, 0x414)),
            Expr.Return,
        ),
        'loc_2299',
    )

    ChrTalk(
        0x00FE,
        (
            '唉～\n',
            '我可不是自己想呆在这里的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我是被大家硬拉过来的，\n',
            '无法拒绝啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2299(): pass

    label('loc_2299')

    TalkEnd(0x001F)

    Return()

# id: 0x0014 offset: 0x229D
@scena.Code('func_14_229D')
def func_14_229D():
    MapClearFlags(0x00000001)
    EventBegin(0x00)
    FormationDelMember(0x35, 0xFF)
    FormationAddMember(0x04, 0xFF)
    ChrSetStatus(0x0004, 0x00, 17)
    OP_B5(0x0004, 0x00)
    OP_B5(0x0004, 0x05)
    OP_B5(0x0004, 0x04)
    OP_B5(0x0004, 0x03)
    OP_B5(0x0004, 0x02)
    OP_B5(0x0004, 0x01)
    EquipCmd(0x04, 0x0079)
    EquipCmd(0x04, 0x00F4)
    EquipCmd(0x04, 0x0112)
    EquipCmd(0x04, 0x0259, 0x00)
    EquipCmd(0x04, 0x0262, 0x05)
    EquipCmd(0x04, 0x02C8, 0x04)
    EquipCmd(0x04, 0x0265, 0x03)
    EquipCmd(0x04, 0x025B, 0x02)
    EquipCmd(0x04, 0x02D4, 0x01)
    AddCraft(0x0004, 0x00BE)
    AddSCraft(0x0004, 0x00FA)
    FadeOut(0, 0, -1)
    OP_20(0x000009C4)
    OP_21()

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x56),
            Expr.Nop,
            Expr.Return,
        ),
    )

    PlayBGM(86)
    ChrSetPos(0x0008, -10880, 0, 6920, 135)
    ChrSetPos(0x0009, -9460, 0, 7150, 270)
    ChrSetPos(0x000A, -10770, 0, 5350, 0)
    ChrSetPos(0x000B, -11290, 0, 4290, 90)
    ChrSetPos(0x000C, -10500, 0, 1550, 90)
    ChrSetFlags(0x000B, 0x0004)
    ChrSetFlags(0x000C, 0x0004)
    OP_4A(0x0008, 255)
    OP_4A(0x0009, 255)
    OP_4A(0x000A, 255)
    OP_4A(0x000B, 255)
    OP_4A(0x000C, 255)
    OP_4A(0x000D, 255)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000E, 0x0080)

    @scena.Lambda('lambda_23B4')
    def lambda_23B4():
        ChrTurnDirection(0x00FE, 0x000E, 0)
        Yield()

        Jump('lambda_23B4')

    DispatchAsync2(0x0008, 0x0001, lambda_23B4)

    @scena.Lambda('lambda_23C5')
    def lambda_23C5():
        ChrTurnDirection(0x00FE, 0x000E, 0)
        Yield()

        Jump('lambda_23C5')

    DispatchAsync2(0x0009, 0x0001, lambda_23C5)

    @scena.Lambda('lambda_23D6')
    def lambda_23D6():
        ChrTurnDirection(0x00FE, 0x000E, 0)
        Yield()

        Jump('lambda_23D6')

    DispatchAsync2(0x000A, 0x0001, lambda_23D6)

    @scena.Lambda('lambda_23E7')
    def lambda_23E7():
        ChrTurnDirection(0x00FE, 0x000E, 0)
        Yield()

        Jump('lambda_23E7')

    DispatchAsync2(0x000B, 0x0001, lambda_23E7)

    @scena.Lambda('lambda_23F8')
    def lambda_23F8():
        ChrTurnDirection(0x00FE, 0x000E, 0)
        Yield()

        Jump('lambda_23F8')

    DispatchAsync2(0x000C, 0x0001, lambda_23F8)

    @scena.Lambda('lambda_2409')
    def lambda_2409():
        ChrTurnDirection(0x00FE, 0x000E, 0)
        Yield()

        Jump('lambda_2409')

    DispatchAsync2(0x000D, 0x0001, lambda_2409)

    CameraMove(-9740, 0, 5080, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x000E,
        (
            '#0400050633V#776F……别装蒜了！\n',
            '是你们干的好事吧！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0400050634V我饶不了你们！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0460050635V你这小鬼在说什么呀？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0450050636V喂喂，这里可不是\n',
            '你这种小鬼头能来的地方哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0450050637V快点滚回家去，\n',
            '乖乖地喝妈妈的奶吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0470050638V哈哈哈，说得对、说得对！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_92(0x000E, 0x0009, 3800, 2000, 0x00)

    ChrTalk(
        0x000E,
        (
            '#0400050639V#776F呜呜呜呜呜……',
            TxtCtl.Enter,
        ),
    )

    OP_94(0x01, 0x000E, 0x005A, 0x00000064, 0x00000BB8, 0x00)
    OP_94(0x01, 0x000E, 0x010E, 0x00000064, 0x00000BB8, 0x00)
    OP_94(0x01, 0x000E, 0x005A, 0x00000064, 0x00000BB8, 0x00)
    OP_94(0x01, 0x000E, 0x010E, 0x00000064, 0x00000BB8, 0x00)
    OP_94(0x01, 0x000E, 0x005A, 0x00000064, 0x00000BB8, 0x00)
    OP_94(0x01, 0x000E, 0x010E, 0x00000064, 0x00000BB8, 0x00)
    CloseMessageWindow()
    OP_62(0x000E, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x000E,
        (
            '#0400050640V#778F#3S哇啊啊啊啊啊啊啊啊……！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)

    @scena.Lambda('lambda_265A')
    def lambda_265A():
        CameraMove(-12160, 0, 5450, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_265A)

    OP_94(0x01, 0x000E, 0x005A, 0x00000064, 0x00000BB8, 0x00)
    OP_94(0x01, 0x000E, 0x010E, 0x00000064, 0x00000BB8, 0x00)
    OP_94(0x01, 0x000E, 0x005A, 0x00000064, 0x00000BB8, 0x00)
    OP_94(0x01, 0x000E, 0x010E, 0x00000064, 0x00000BB8, 0x00)
    OP_94(0x01, 0x000E, 0x005A, 0x00000064, 0x00000BB8, 0x00)
    OP_94(0x01, 0x000E, 0x010E, 0x00000064, 0x00000BB8, 0x00)
    OP_94(0x01, 0x000E, 0x005A, 0x00000064, 0x00000BB8, 0x00)
    OP_94(0x01, 0x000E, 0x010E, 0x00000064, 0x00000BB8, 0x00)
    OP_94(0x01, 0x000E, 0x005A, 0x00000064, 0x00000BB8, 0x00)
    OP_94(0x01, 0x000E, 0x010E, 0x00000064, 0x00000BB8, 0x00)
    OP_94(0x01, 0x000E, 0x005A, 0x00000064, 0x00000BB8, 0x00)
    OP_94(0x01, 0x000E, 0x010E, 0x00000064, 0x00000BB8, 0x00)
    CloseMessageWindow()
    OP_92(0x000E, 0x0009, 500, 6000, 0x00)

    @scena.Lambda('lambda_2735')
    def lambda_2735():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x00001770, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_2735)

    PlaySE(125, 0x00, 0x64)
    OP_94(0x01, 0x0009, 0x00B4, 0x00000320, 0x00001770, 0x00)
    Sleep(200)

    OP_92(0x000E, 0x000A, 800, 6000, 0x00)

    @scena.Lambda('lambda_2772')
    def lambda_2772():
        OP_94(0x01, 0x00FE, 0x00B4, 0x00000258, 0x00001770, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_2772)

    PlaySE(125, 0x00, 0x64)
    OP_94(0x01, 0x000A, 0x00B4, 0x00000258, 0x00001770, 0x00)

    ChrTalk(
        0x0008,
        (
            '#0450050641V搞、搞什么……？',
            TxtCtl.Enter,
        ),
    )

    OP_92(0x000E, 0x000A, 600, 6000, 0x00)

    @scena.Lambda('lambda_27CB')
    def lambda_27CB():
        OP_94(0x01, 0x00FE, 0x00B4, 0x0000012C, 0x00001770, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_27CB)

    PlaySE(125, 0x00, 0x64)
    OP_94(0x01, 0x000A, 0x00B4, 0x0000012C, 0x00001770, 0x00)
    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0470050642V这小鬼……\n',
            '发什么癫呀？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0400050643V#778F#2P别以为我没有妈妈\n',
            '就随意看不起人家！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0400050644V#2P老师就是我的妈妈！\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_92(0x000E, 0x000A, 600, 6000, 0x00)

    @scena.Lambda('lambda_2890')
    def lambda_2890():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000001F4, 0x00001770, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_2890)

    PlaySE(125, 0x00, 0x64)
    OP_94(0x01, 0x000A, 0x00B4, 0x0000012C, 0x00001770, 0x00)

    ChrTalk(
        0x000E,
        (
            '#0400050645V#776F#2P你们竟然把老师宝贵的家给……\n',
            '竟然、竟然、竟然把……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_92(0x000E, 0x000A, 600, 6000, 0x00)

    @scena.Lambda('lambda_2917')
    def lambda_2917():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000001F4, 0x00001770, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_2917)

    PlaySE(125, 0x00, 0x64)
    OP_94(0x01, 0x000A, 0x00B4, 0x0000012C, 0x00001770, 0x00)

    ChrTalk(
        0x000A,
        (
            '#0460050646V嘁……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x000E, 0x0020)
    ChrSetFlags(0x000E, 0x0040)
    OP_94(0x01, 0x000E, 0x00B4, 0x000003E8, 0x00000BB8, 0x00)
    OP_92(0x000E, 0x000A, 800, 6000, 0x00)

    @scena.Lambda('lambda_2980')
    def lambda_2980():
        OP_94(0x00, 0x00FE, 0x0000, 0x0000012C, 0x00000FA0, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_2980)

    OP_92(0x000E, 0x000A, 500, 6000, 0x00)
    PlaySE(521, 0x00, 0x64)
    ChrJumpTo(0x000E, -10860, 0, 5210, 500, 5000)
    ChrJumpTo(0x000E, -10100, 0, 5200, 200, 5000)

    ChrTalk(
        0x000E,
        (
            '#0400050647V#778F#4P哇啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_92(0x0008, 0x000E, 700, 2000, 0x00)
    OP_63(0x000E)
    ChrTurnDirection(0x000E, 0x0008, 400)
    Sleep(500)

    @scena.Lambda('lambda_2A16')
    def lambda_2A16():
        OP_94(0x01, 0x00FE, 0x010E, 0x000000C8, 0x000001F4, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_2A16)

    ChrSetFlags(0x000E, 0x0004)
    ChrClearFlags(0x000E, 0x0400)
    TerminateThread(0x0008, 0xFF)

    @scena.Lambda('lambda_2A3A')
    def lambda_2A3A():
        OP_99(0x00FE, 0x00, 0x04, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2A3A)

    @scena.Lambda('lambda_2A4A')
    def lambda_2A4A():
        OP_94(0x01, 0x00FE, 0x0000, 0x00000064, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_2A4A)

    OP_94(0x01, 0x000E, 0x00B4, 0x00000064, 0x000003E8, 0x00)
    OP_94(0x01, 0x000E, 0x0000, 0x00000064, 0x000003E8, 0x00)

    @scena.Lambda('lambda_2A7E')
    def lambda_2A7E():
        ChrMoveToRelativeAsync(0x00FE, 0, 400, 0, 800, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_2A7E)

    OP_9E(0x000E, 15, 0, 300, 3000)

    ChrTalk(
        0x0008,
        (
            '#0450050648V#2P我们懒得理你，\n',
            '你这小鬼头就得意起来了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_92(0x000A, 0x000E, 1000, 2000, 0x00)

    ChrTalk(
        0x000A,
        (
            '#0460050649V看来不给你\n',
            '尝尝苦头也不行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_92(0x0009, 0x000E, 1500, 2000, 0x00)

    ChrTalk(
        0x0009,
        (
            '#0470050650V不如就打一百下屁股吧？\n',
            '哇～哈、哈、哈！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x0101, -1130, 0, 4490, 0)
    ChrSetPos(0x0105, -1130, 0, 4490, 0)
    ChrSetPos(0x0102, -1130, 0, 4490, 0)

    ChrTalk(
        0x0105,
        (
            '#0060050651V#1P请你们住手！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x000B, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x000C, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x000D, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_2C5D')
    def lambda_2C5D():
        ChrTurnDirection(0x00FE, 0x0102, 0)
        Yield()

        Jump('lambda_2C5D')

    DispatchAsync2(0x0009, 0x0001, lambda_2C5D)

    @scena.Lambda('lambda_2C6E')
    def lambda_2C6E():
        ChrTurnDirection(0x00FE, 0x0105, 0)
        Yield()

        Jump('lambda_2C6E')

    DispatchAsync2(0x000A, 0x0001, lambda_2C6E)

    @scena.Lambda('lambda_2C7F')
    def lambda_2C7F():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_2C7F')

    DispatchAsync2(0x000B, 0x0001, lambda_2C7F)

    @scena.Lambda('lambda_2C90')
    def lambda_2C90():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_2C90')

    DispatchAsync2(0x000C, 0x0001, lambda_2C90)

    @scena.Lambda('lambda_2CA1')
    def lambda_2CA1():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_2CA1')

    DispatchAsync2(0x000D, 0x0001, lambda_2CA1)

    ChrSetFlags(0x0101, 0x1000)
    ChrSetFlags(0x0102, 0x1000)
    ChrSetChipByIndex(0x0101, 11)
    ChrSetChipByIndex(0x0102, 12)

    @scena.Lambda('lambda_2CC6')
    def lambda_2CC6():
        CameraMove(-10300, 0, 5530, 1000)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_2CC6)

    @scena.Lambda('lambda_2CDE')
    def lambda_2CDE():
        ChrWalkTo(0x00FE, -7430, 0, 4920, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_2CDE)

    Sleep(500)

    @scena.Lambda('lambda_2CFE')
    def lambda_2CFE():
        ChrWalkTo(0x00FE, -6650, 0, 5880, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_2CFE)

    Sleep(300)

    @scena.Lambda('lambda_2D1E')
    def lambda_2D1E():
        ChrWalkTo(0x00FE, -6040, 0, 4040, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2D1E)

    WaitForThreadExit(0x0101, 0x0001)
    ChrSetChipByIndex(0x0101, 8)
    ChrSetSubChip(0x0101, 6)
    WaitForThreadExit(0x0102, 0x0001)
    ChrSetChipByIndex(0x0102, 9)
    ChrSetSubChip(0x0102, 6)

    ChrTalk(
        0x0008,
        (
            '#0450050652V你、你们是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(508, 0x00, 0x64)
    ChrSetChipByIndex(0x0009, 28)
    Sleep(100)

    ChrSetChipByIndex(0x000A, 32)
    Sleep(100)

    ChrSetChipByIndex(0x000B, 4)
    Sleep(100)

    ChrSetChipByIndex(0x000C, 4)
    Sleep(100)

    ChrSetChipByIndex(0x000D, 4)
    Sleep(100)

    ChrSetFlags(0x000E, 0x0040)

    @scena.Lambda('lambda_2DB3')
    def lambda_2DB3():
        ChrSetDirection(0x00FE, 270, 800)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_2DB3)

    ChrJumpTo(0x000E, -10940, 0, 6120, 500, 5000)
    ChrClearFlags(0x000E, 0x0020)
    ChrSetFlags(0x000E, 0x0400)
    ChrJumpTo(0x000E, -11820, 0, 6570, 200, 5000)
    ChrClearFlags(0x000E, 0x0004)
    ChrSetChipByIndex(0x0008, 24)
    ChrSetDirection(0x0008, 90, 400)

    ChrTalk(
        0x000E,
        (
            '#0400050653V#778F咳咳……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000E, 0x0105, 250)

    ChrTalk(
        0x000E,
        (
            '#0400050654V#775F科洛丝……姐姐？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0105, 0x0001)

    ChrTalk(
        0x0105,
        (
            '#0060050655V#049F竟然对一个\n',
            '手无寸铁的小孩子使用暴力……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060050656V太差劲了……\n',
            '难道你们不觉得羞耻吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0450050657V你、你说什么～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0470050658V哟哟，小姑娘。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0470050659V本来觉得你那张小嘴蛮可爱的，\n',
            '没想到还这么牙尖嘴利嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0460050660V就算有游击士在，\n',
            '但跟这么多人动手，你以为自己能赢吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010050661V#005F科洛丝，你先退后！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020050662V#012F我们会争取时间。\n',
            '你趁空隙把孩子救出去……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0105, 90, 400)
    Sleep(200)

    ChrTalk(
        0x0105,
        (
            '#0060050663V#042F#1P不……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060050664V请让我也参加战斗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010050665V#004F哎……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060050666V#047F#1P其实我本来\n',
            '并不想用这个的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060050667V但是我曾经学过——\n',
            '剑，应在保护他人之时才握于手中的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    PlaySE(504, 0x00, 0x64)
    ChrSetChipByIndex(0x0105, 10)
    ChrSetSubChip(0x0105, 6)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0105,
        (
            '#0060050668V#042F#1P现在，就是该出剑的时候了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010050669V#004F哎！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020050670V#014F防身用的细剑？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x0105, 0x0020)

    @scena.Lambda('lambda_317E')
    def lambda_317E():
        ChrSetDirection(0x00FE, 270, 800)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_317E)

    WaitForThreadExit(0x0105, 0x0001)
    Sleep(500)

    ChrClearFlags(0x0105, 0x0020)

    ChrTalk(
        0x0105,
        (
            '#0060050671V#046F请放了那孩子。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060050672V否则……\n',
            '我就只好强行救人了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1530050673V好、好酷呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1540050674V……真是惹人怜爱的小妹妹哦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(800)

    ChrTalk(
        0x0008,
        (
            '#0450050675V#3S惹、惹人怜爱个屁！！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0470050676V连这种小娘们儿都小看我们，\n',
            '真是岂有此理！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0460050677V让他们好好尝尝\n',
            '我们『渡鸦帮』的厉害！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2P#1K喔！',
            TxtCtl.Enter,
        ),
    )

    ChrTalk(
        0x000C,
        (
            '#1P#1K喔！',
            TxtCtl.Enter,
        ),
    )

    ChrTalk(
        0x000D,
        (
            '#1550050680V#4P#1K喔！',
            TxtCtl.Enter,
        ),
    )

    Sleep(500)

    OP_56(0x01)
    OP_59()
    ChrSetChipByIndex(0x0008, 25)
    ChrSetChipByIndex(0x0009, 29)
    ChrSetChipByIndex(0x000A, 33)
    ChrSetChipByIndex(0x000B, 5)
    ChrSetChipByIndex(0x000C, 5)
    ChrSetChipByIndex(0x000D, 5)

    @scena.Lambda('lambda_3362')
    def lambda_3362():
        OP_92(0x00FE, 0x0105, 1000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_3362)

    @scena.Lambda('lambda_3377')
    def lambda_3377():
        OP_92(0x00FE, 0x0102, 1000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_3377)

    @scena.Lambda('lambda_338C')
    def lambda_338C():
        OP_92(0x00FE, 0x0105, 1000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_338C)

    @scena.Lambda('lambda_33A1')
    def lambda_33A1():
        OP_92(0x00FE, 0x0101, 1000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_33A1)

    @scena.Lambda('lambda_33B6')
    def lambda_33B6():
        OP_92(0x00FE, 0x0101, 1000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_33B6)

    @scena.Lambda('lambda_33CB')
    def lambda_33CB():
        OP_92(0x00FE, 0x0101, 1000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0002, lambda_33CB)

    Sleep(300)

    Battle(0x00000397, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_33F8'),
        (-1, 'loc_33FB'),
    )

    def _loc_33F8(): pass

    label('loc_33F8')

    OP_B4(0x00)

    Return()

    def _loc_33FB(): pass

    label('loc_33FB')

    EventBegin(0x00)
    ChrSetPos(0x000E, -11720, 0, 5630, 90)
    ChrSetPos(0x0105, -7070, 0, 5350, 270)
    ChrSetPos(0x0101, -6160, 0, 4019, 270)
    ChrSetPos(0x0102, -6120, 0, 5950, 270)
    ChrSetChipByIndex(0x0008, 24)
    ChrSetChipByIndex(0x0009, 28)
    ChrSetChipByIndex(0x000A, 32)
    ChrSetChipByIndex(0x000B, 7)
    ChrSetChipByIndex(0x000C, 7)
    ChrSetChipByIndex(0x000D, 7)
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x000B, 0xFF)
    TerminateThread(0x000C, 0xFF)
    TerminateThread(0x000D, 0xFF)

    ExecExpressionWithValue(
        0x000B,
        0x08,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000C,
        0x08,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000D,
        0x08,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetPos(0x000B, -11300, 0, 10000, 135)
    ChrSetPos(0x000C, -14730, 0, 3670, 90)
    ChrSetPos(0x000D, -10480, 0, -290, 0)
    ChrSetPos(0x0008, -11270, 0, 6060, 90)
    ChrSetPos(0x0009, -9150, 0, 3860, 90)
    ChrSetPos(0x000A, -8760, 0, 7620, 90)
    ChrTurnDirection(0x0009, 0x0105, 0)
    ChrTurnDirection(0x000A, 0x0105, 0)
    CameraMove(-10660, 0, 5990, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    FadeIn(1000, 0)
    Sleep(1000)

    OP_62(0x0008, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x0009, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x000A, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x0008,
        (
            '#0450050681V这、这帮家伙是怪物吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0470050682V游击士也就算了，\n',
            '连那个小丫头也不是泛泛之辈……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0400050683V#774F好、好厉害啊姐姐！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010050684V#001F哇哦～！\n',
            '科洛丝，你好厉害啊～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020050685V#010F如此超凡的剑法\n',
            '应该也是师从名家的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060050686V#045F呵呵，我还差得远呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    PlaySE(213, 0x00, 0x64)
    ChrSetChipByIndex(0x0105, 65535)
    OP_0D()
    Sleep(500)

    OP_94(0x01, 0x0105, 0x0000, 0x000003E8, 0x000003E8, 0x00)

    ChrTalk(
        0x0105,
        (
            '#0060050687V#043F那个，再战斗下去，\n',
            '我想也已经没有意义了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060050688V求求你们……\n',
            '请把那孩子放了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0460050689V这、这娘们儿……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0450050690V被、被你们耍成这样， \n',
            '怎可能说句『哦，好』就了事啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x0010, -990, 0, 1560, 315)
    ChrSetPos(0x000F, -2200, 0, 1380, 0)

    NpcTalk(
        0x0010,
        '青年的声音',
        (
            '#0050050691V#1P……给我到此为止吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3813')
    def lambda_3813():
        ChrTurnDirection(0x00FE, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_3813)

    @scena.Lambda('lambda_3821')
    def lambda_3821():
        ChrTurnDirection(0x00FE, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_3821)

    @scena.Lambda('lambda_382F')
    def lambda_382F():
        ChrTurnDirection(0x00FE, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_382F)

    @scena.Lambda('lambda_383D')
    def lambda_383D():
        ChrTurnDirection(0x00FE, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_383D)

    @scena.Lambda('lambda_384B')
    def lambda_384B():
        ChrTurnDirection(0x00FE, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_384B)

    @scena.Lambda('lambda_3859')
    def lambda_3859():
        ChrTurnDirection(0x00FE, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_3859)

    ChrTalk(
        0x0008,
        (
            '#0450050692V是、是谁！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0460050693V新来的吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_38A3')
    def lambda_38A3():
        ChrTurnDirection(0x00FE, 0x0010, 0)
        Yield()

        Jump('lambda_38A3')

    DispatchAsync2(0x0008, 0x0001, lambda_38A3)

    @scena.Lambda('lambda_38B4')
    def lambda_38B4():
        ChrTurnDirection(0x00FE, 0x0010, 0)
        Yield()

        Jump('lambda_38B4')

    DispatchAsync2(0x0009, 0x0001, lambda_38B4)

    @scena.Lambda('lambda_38C5')
    def lambda_38C5():
        ChrTurnDirection(0x00FE, 0x0010, 0)
        Yield()

        Jump('lambda_38C5')

    DispatchAsync2(0x000A, 0x0001, lambda_38C5)

    @scena.Lambda('lambda_38D6')
    def lambda_38D6():
        ChrTurnDirection(0x00FE, 0x0010, 0)
        Yield()

        Jump('lambda_38D6')

    DispatchAsync2(0x0101, 0x0001, lambda_38D6)

    @scena.Lambda('lambda_38E7')
    def lambda_38E7():
        ChrTurnDirection(0x00FE, 0x0010, 0)
        Yield()

        Jump('lambda_38E7')

    DispatchAsync2(0x0102, 0x0001, lambda_38E7)

    @scena.Lambda('lambda_38F8')
    def lambda_38F8():
        ChrTurnDirection(0x00FE, 0x0010, 0)
        Yield()

        Jump('lambda_38F8')

    DispatchAsync2(0x0105, 0x0001, lambda_38F8)

    @scena.Lambda('lambda_3909')
    def lambda_3909():
        CameraMove(-9840, 0, 5810, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3909)

    ChrClearFlags(0x0010, 0x0080)
    ChrWalkTo(0x0010, -4030, 0, 4430, 3000, 0x00)
    ChrSetDirection(0x0010, 270, 400)

    ChrTalk(
        0x0010,
        (
            '#0050050694V#053F#1P哎呀哎呀，难得回来一趟，\n',
            '居然连我的声音都不记得了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    OP_62(0x0008, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x0009, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x000A, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x0008,
        (
            '#0450050695V阿、阿加特大哥！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0470050696V你、你来了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0050050697V#050F#1P…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3A82')
    def lambda_3A82():
        CameraMove(-10660, 0, 5990, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3A82)

    @scena.Lambda('lambda_3A9A')
    def lambda_3A9A():
        ChrWalkTo(0x00FE, -8650, 0, 5350, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_3A9A)

    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0102, 65535)
    Sleep(600)

    TerminateThread(0x0105, 0xFF)
    ChrSetDirection(0x0105, 45, 400)
    ChrMoveToRelative(0x0105, 1000, 0, 1000, 2000, 0x00)
    ChrSetDirection(0x0105, 180, 400)

    @scena.Lambda('lambda_3AEA')
    def lambda_3AEA():
        ChrTurnDirection(0x00FE, 0x0010, 0)
        Yield()

        Jump('lambda_3AEA')

    DispatchAsync2(0x0105, 0x0001, lambda_3AEA)

    WaitForThreadExit(0x0010, 0x0001)
    ChrSetDirection(0x0010, 270, 400)

    ChrTalk(
        0x0101,
        (
            '#0010050698V#004F你、你怎么会……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010050699V难道说，\n',
            '你也认识这帮家伙！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0050050700V#053F……雷斯……………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0470050701V是、是，什么事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0010, 0x0009, 400)
    ChrSetFlags(0x0009, 0x0020)
    ChrSetFlags(0x0009, 0x0004)
    ChrSetFlags(0x0009, 0x0040)
    ChrSetFlags(0x0010, 0x0020)
    ChrSetChipByIndex(0x0010, 36)
    ChrSetSubChip(0x0010, 0)
    OP_92(0x0010, 0x0009, 400, 8000, 0x00)
    ChrSetSubChip(0x0010, 1)
    PlaySE(507, 0x00, 0x64)

    @scena.Lambda('lambda_3BE1')
    def lambda_3BE1():
        OP_94(0x00, 0x00FE, 0x0000, 0x0000012C, 0x00001F40, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_3BE1)

    ChrSetChipByIndex(0x0009, 30)
    ChrSetFlags(0x0009, 0x0020)

    ExecExpressionWithValue(
        0x0009,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_94(0x01, 0x0009, 0x00B4, 0x000001F4, 0x00001F40, 0x00)
    PlaySE(521, 0x00, 0x64)

    @scena.Lambda('lambda_3C20')
    def lambda_3C20():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000001F4, 0x00002AF8, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_3C20)

    WaitForThreadExit(0x0009, 0x0001)
    ChrSetChipByIndex(0x0009, 31)
    OP_99(0x0009, 0x00, 0x03, 2000)

    ChrTalk(
        0x0009,
        (
            '#0470050702V呜啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0010, 0)
    Sleep(80)

    ChrSetChipByIndex(0x0010, 3)
    ChrClearFlags(0x0010, 0x0020)
    Sleep(500)

    ChrTurnDirection(0x0010, 0x000A, 400)
    OP_92(0x0010, 0x0009, 3000, 8000, 0x00)

    ChrTalk(
        0x0010,
        (
            '#0050050703V#057F你们几个……都干了些什么？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050050704V调戏妇女、虐待小孩……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050050705V也太目无法纪了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0460050706V啰、啰嗦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0460050707V你这种已经离队的家伙\n',
            '没有资格对我们指手画脚……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3D61')
    def lambda_3D61():
        CameraMove(-10660, 0, 7680, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3D61)

    ChrSetFlags(0x000A, 0x0020)
    ChrSetFlags(0x000A, 0x0004)
    ChrSetFlags(0x000A, 0x0040)
    ChrSetChipByIndex(0x0010, 37)
    OP_92(0x0010, 0x000A, 1000, 10000, 0x00)
    ChrSetFlags(0x0010, 0x0020)
    ChrSetChipByIndex(0x0010, 36)
    ChrSetSubChip(0x0010, 0)
    OP_92(0x0010, 0x000A, 400, 10000, 0x00)
    ChrSetSubChip(0x0010, 1)
    PlaySE(507, 0x00, 0x64)
    PlaySE(521, 0x00, 0x64)

    @scena.Lambda('lambda_3DC7')
    def lambda_3DC7():
        OP_94(0x00, 0x00FE, 0x0000, 0x0000012C, 0x00001F40, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_3DC7)

    ChrSetChipByIndex(0x000A, 34)
    ChrSetFlags(0x000A, 0x0020)

    ExecExpressionWithValue(
        0x000A,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_94(0x01, 0x000A, 0x00B4, 0x000001F4, 0x00001F40, 0x00)

    @scena.Lambda('lambda_3E01')
    def lambda_3E01():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000001F4, 0x00002AF8, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_3E01)

    WaitForThreadExit(0x000A, 0x0001)
    ChrSetSubChip(0x0010, 2)
    ChrMoveTo(0x000A, -8790, 2000, 11500, 15000, 0x00)
    PlayEffect(0x12, 0xFF, 0x000A, 0, 0, -500, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)

    ChrTalk(
        0x000A,
        (
            '#0460050708V呜哇！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    PlaySE(142, 0x00, 0x64)
    CameraSetDistance(3070, 0)
    CameraSetDistance(3000, 80)
    Sleep(500)

    ChrMoveTo(0x000A, -8790, 0, 11500, 2000, 0x00)
    PlaySE(524, 0x00, 0x64)
    ChrSetChipByIndex(0x000A, 35)
    OP_99(0x000A, 0x01, 0x03, 1000)
    ChrSetChipByIndex(0x0010, 3)
    ChrSetSubChip(0x0010, 0)
    ChrClearFlags(0x0010, 0x0020)
    Sleep(500)

    ChrTalk(
        0x0010,
        (
            '#0050050709V#050F……你刚刚说什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x0008,
        (
            '#0450050710V大、大哥，饶了我们吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3F3C')
    def lambda_3F3C():
        ChrTurnDirection(0x00FE, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_3F3C)

    TerminateThread(0x0008, 0xFF)
    ChrSetChipByIndex(0x0008, 21)
    ChrWalkTo(0x0008, -11810, 0, 6350, 3000, 0x00)
    ChrWalkTo(0x0008, -12260, 0, 5600, 3000, 0x00)
    ChrSetDirection(0x0008, 90, 400)

    ChrTalk(
        0x0008,
        (
            '#0450050711V这小孩……你看，我这就放了他！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3FB2')
    def lambda_3FB2():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_3FB2)

    @scena.Lambda('lambda_3FC0')
    def lambda_3FC0():
        ChrTurnDirection(0x00FE, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3FC0)

    @scena.Lambda('lambda_3FCE')
    def lambda_3FCE():
        ChrTurnDirection(0x00FE, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_3FCE)

    ChrTalk(
        0x000E,
        (
            '#0400050712V#775F#1P科洛丝姐姐！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_4002')
    def lambda_4002():
        CameraMove(-9010, 0, 6820, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_4002)

    @scena.Lambda('lambda_401A')
    def lambda_401A():
        ChrWalkTo(0x00FE, -8860, 0, 5270, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_401A)

    Sleep(300)

    ChrWalkTo(0x0105, -8130, 0, 5420, 2000, 0x00)
    ChrSetDirection(0x0105, 270, 400)

    ChrTalk(
        0x0105,
        (
            '#0060050713V#048F太好了……\n',
            '已经没事了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0050050714V#053F哼，\n',
            '早这么做不就得了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0010, 400)

    ChrTalk(
        0x0101,
        (
            '#0010050715V#007F你还是那么粗暴啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010050716V#009F还有，你为什么会在\n',
            '这么恰到好处的时候出现？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0010, 0x0101, 400)

    ChrTalk(
        0x0010,
        (
            '#0050050717V#050F我只是听嘉恩那家伙说了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050050718V说洛连特来的两个小鬼\n',
            '正在调查纵火事件什么的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050050719V#053F好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0010, 0x000E, 400)
    Sleep(500)

    ChrTalk(
        0x0010,
        (
            '#0050050720V#050F#2P喂，小鬼头。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000E, 0x0010, 400)

    ChrTalk(
        0x000E,
        (
            '#0400050721V#775F什、什么事啊……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0050050722V#051F#2P敢一个人闯进来，\n',
            '还真是个有胆量的小子。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050050723V不过这样有点太胡闹了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050050724V下次再让你妈妈操心的话，\n',
            '可真的要打屁股哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0400050725V#774F哎……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000F,
        '女性的声音',
        (
            '#0390050726V克拉姆……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_42F7')
    def lambda_42F7():
        ChrTurnDirection(0x00FE, 0x000F, 400)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_42F7)

    @scena.Lambda('lambda_4305')
    def lambda_4305():
        ChrTurnDirection(0x00FE, 0x000F, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4305)

    @scena.Lambda('lambda_4313')
    def lambda_4313():
        ChrTurnDirection(0x00FE, 0x000F, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_4313)

    @scena.Lambda('lambda_4321')
    def lambda_4321():
        ChrTurnDirection(0x00FE, 0x000F, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_4321)

    @scena.Lambda('lambda_432F')
    def lambda_432F():
        ChrTurnDirection(0x00FE, 0x000F, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_432F)

    ChrTurnDirection(0x000E, 0x000F, 400)
    Sleep(500)

    @scena.Lambda('lambda_4349')
    def lambda_4349():
        ChrTurnDirection(0x00FE, 0x000F, 0)
        Yield()

        Jump('lambda_4349')

    DispatchAsync2(0x0101, 0x0001, lambda_4349)

    @scena.Lambda('lambda_435A')
    def lambda_435A():
        ChrTurnDirection(0x00FE, 0x000F, 0)
        Yield()

        Jump('lambda_435A')

    DispatchAsync2(0x0102, 0x0001, lambda_435A)

    @scena.Lambda('lambda_436B')
    def lambda_436B():
        ChrTurnDirection(0x00FE, 0x000F, 0)
        Yield()

        Jump('lambda_436B')

    DispatchAsync2(0x0105, 0x0001, lambda_436B)

    ChrClearFlags(0x000F, 0x0080)

    @scena.Lambda('lambda_4381')
    def lambda_4381():
        CameraMove(-9140, 0, 5560, 1500)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_4381)

    ChrWalkTo(0x000F, -6590, 0, 2810, 2000, 0x00)
    ChrTurnDirection(0x000F, 0x000E, 0)
    ChrTurnDirection(0x000E, 0x000F, 0)

    ChrTalk(
        0x000E,
        (
            '#0400050727V#774F#1P老、老师！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060050728V#044F#2P您怎么来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0390050729V#754F我从协会得知你们来了这里，\n',
            '然后我就拜托这位先生带我来的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390050730V#752F克拉姆，你这孩子真是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0400050731V#772F#1P只、只有这次，\n',
            '我是绝对不会道歉的！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0400050732V放火烧了我们房子的犯人\n',
            '我绝对要亲手将他们……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0390050733V#755F#3S克拉姆！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    Sleep(200)

    OP_62(0x000E, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)

    @scena.Lambda('lambda_4545')
    def lambda_4545():
        ChrJumpToRelative(0x00FE, 0, 0, 0, 800, 6000)

        ExitThread()

    DispatchAsync(0x000E, 0x0003, lambda_4545)

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060050734V#043F#2P特蕾莎老师……\n',
            '不管怎样，请您不要责怪他。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0390050735V#754F不。\n',
            '我不是要怪他。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390050736V#757F克拉姆……\n',
            '你的心情我很明白。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390050737V那毕竟是大家一起生活过的地方。\n',
            '对我们来说，那更加是无可替代的家园。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390050738V但是呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390050739V#756F就算你向犯人报复，\n',
            '烧毁的家也不会再回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0400050740V#775F#1P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0390050741V#750F只要你们没事，\n',
            '对老师来说就已经很满足了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390050742V这就是我唯一的希望……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390050743V#758F所以呢，克拉姆……\n',
            '你以后不要再做危险的事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0400050744V#775F#1P老、老师……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0400050745V#777F……呜呜呜呜呜呜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    OP_62(0x000E, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x00)

    ChrTalk(
        0x000E,
        (
            '#0400050746V#778F#1P#5S呜哇啊啊阿～～～！#2S',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    OP_92(0x000E, 0x000F, 600, 5000, 0x00)
    ChrSetFlags(0x000F, 0x0020)
    OP_94(0x01, 0x000F, 0x00B4, 0x00000064, 0x000005DC, 0x00)
    OP_94(0x01, 0x000F, 0x0000, 0x00000064, 0x000005DC, 0x00)
    ChrClearFlags(0x000F, 0x0020)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010050747V#003F#2P呜……\n',
            '这种场面真是太让人感动了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060050748V#049F#1P是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060050749V#049F能平安无事真是太好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0010, 0x00000000, 2000, 0x0E, 0x0F, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_48F4')
    def lambda_48F4():
        CameraMove(-9840, 0, 6260, 1000)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_48F4)

    WaitForThreadExit(0x000C, 0x0001)

    ChrTalk(
        0x0010,
        (
            '#0050050750V#551F真是的……\n',
            '所以就说女人和小孩麻烦嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050050751V#552F喂，黑发的小子。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050050752V带着院长她们\n',
            '快点离开这地方吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050050753V我可不会应付这种场面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0102, 0xFF)
    ChrSetDirection(0x0102, 270, 400)

    ChrTalk(
        0x0102,
        (
            '#0020050754V#014F没问题，可是……\n',
            '阿加特兄打算做什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0050050755V#057F这还用说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0010, 0x0008, 400)

    @scena.Lambda('lambda_4A34')
    def lambda_4A34():
        CameraMove(-10420, 0, 6530, 1500)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_4A34)

    ChrWalkTo(0x0010, -10870, 0, 5600, 3000, 0x00)
    ChrSetDirection(0x0008, 90, 0)
    ChrTurnDirection(0x0010, 0x0008, 400)

    ChrTalk(
        0x0010,
        (
            '#0050050756V#054F#2P我要好好问个清楚，\n',
            '看看这帮蠢货到底是不是犯人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050050757V给我洗好脖子等着吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_9E(0x0008, 50, 0, 300, 6000)
    Sleep(500)

    TerminateThread(0x0008, 0xFF)

    ChrTalk(
        0x0008,
        (
            '#0450050758V哎～？\n',
            '饶、饶了我们吧～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020050759V#010F原来如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020050760V#019F既然这样的话，\n',
            '那我们还是不打扰你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1500, 0, -1)
    OP_0D()
    OP_28(0x003C, 0x01, 0x0020)
    SetScenaFlags(ScenaFlag(0x007F, 6, 0x3FE))
    NewScene('ED6_DT01/T2100._SN', 100, 0, 0)
    IdleLoop()

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
