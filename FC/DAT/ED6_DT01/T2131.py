import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T2131_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2131   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'T2131.x'
    header.mapIndex       = 1
    header.bgm            = 12
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT01/T2131._SN', 'ED6_DT01/T2131_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
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
        ('ED6_DT07/CH01270._CH', 'ED6_DT07/CH01270P._CP'),
        ('ED6_DT07/CH01190._CH', 'ED6_DT07/CH01190P._CP'),
        ('ED6_DT07/CH02140._CH', 'ED6_DT07/CH02140P._CP'),
        ('ED6_DT07/CH02470._CH', 'ED6_DT07/CH02470P._CP'),
        ('ED6_DT07/CH02060._CH', 'ED6_DT07/CH02060P._CP'),
        ('ED6_DT07/CH01143._CH', 'ED6_DT07/CH01143P._CP'),
        ('ED6_DT07/CH01760._CH', 'ED6_DT07/CH01760P._CP'),
        ('ED6_DT07/CH01560._CH', 'ED6_DT07/CH01560P._CP'),
        ('ED6_DT07/CH01570._CH', 'ED6_DT07/CH01570P._CP'),
        ('ED6_DT07/CH01210._CH', 'ED6_DT07/CH01210P._CP'),
        ('ED6_DT07/CH01023._CH', 'ED6_DT07/CH01023P._CP'),
        ('ED6_DT07/CH01123._CH', 'ED6_DT07/CH01123P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH01000._CH', 'ED6_DT07/CH01000P._CP'),
        ('ED6_DT07/CH01050._CH', 'ED6_DT07/CH01050P._CP'),
        ('ED6_DT07/CH01043._CH', 'ED6_DT07/CH01043P._CP'),
        ('ED6_DT07/CH01213._CH', 'ED6_DT07/CH01213P._CP'),
        ('ED6_DT07/CH01443._CH', 'ED6_DT07/CH01443P._CP'),
        ('ED6_DT07/CH01460._CH', 'ED6_DT07/CH01460P._CP'),
        ('ED6_DT07/CH01123._CH', 'ED6_DT07/CH01123P._CP'),
        ('ED6_DT07/CH01023._CH', 'ED6_DT07/CH01023P._CP'),
        ('ED6_DT07/CH01003._CH', 'ED6_DT07/CH01003P._CP'),
        ('ED6_DT07/CH01053._CH', 'ED6_DT07/CH01053P._CP'),
    ]

# id: 0x10001 offset: 0x162
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '修比拉老板',
            x                   = 24640,
            z                   = 0,
            y                   = 27000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            name                = '照相机',
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
        ScenaNpcData(
            name                = '加鲁诺',
            x                   = 500,
            z                   = 0,
            y                   = 2200,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '杜南公爵',
            x                   = 32400,
            z                   = 0,
            y                   = 28200,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '管家菲利普',
            x                   = 31600,
            z                   = 0,
            y                   = 29700,
            direction           = 145,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '奈尔',
            x                   = -3500,
            z                   = 300,
            y                   = 34200,
            direction           = 270,
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
            name                = '西蒙',
            x                   = 7000,
            z                   = 300,
            y                   = 29100,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x01D5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '梅尔茨',
            x                   = -3490,
            z                   = 250,
            y                   = 32049,
            direction           = 270,
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
            name                = '普莱米奥',
            x                   = -5500,
            z                   = 300,
            y                   = 33800,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            name                = '哈尔德',
            x                   = 2900,
            z                   = 300,
            y                   = 26900,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0155,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0011,
        ),
        ScenaNpcData(
            name                = '鲁特尔',
            x                   = 2900,
            z                   = 300,
            y                   = 29150,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0012,
        ),
        ScenaNpcData(
            name                = '兰达老人',
            x                   = 29260,
            z                   = 400,
            y                   = 30200,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            name                = '米优',
            x                   = 27050,
            z                   = 400,
            y                   = 30200,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0014,
        ),
        ScenaNpcData(
            name                = '西加罗',
            x                   = -6400,
            z                   = 300,
            y                   = 27200,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x01D5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0015,
        ),
        ScenaNpcData(
            name                = '艾德尔',
            x                   = -4000,
            z                   = 300,
            y                   = 27200,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 16,
            chipIndex           = 16,
            npcIndex            = 0x01D5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0016,
        ),
        ScenaNpcData(
            name                = '斯库阿洛',
            x                   = -2940,
            z                   = 0,
            y                   = 5590,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            name                = '塞卡鲁特',
            x                   = -21740,
            z                   = 200,
            y                   = 1670,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x0155,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '贝斯卡',
            x                   = -1940,
            z                   = 0,
            y                   = 1220,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 18,
            chipIndex           = 18,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '波尔',
            x                   = -17720,
            z                   = 250,
            y                   = -840,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 19,
            chipIndex           = 19,
            npcIndex            = 0x0155,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '吉米',
            x                   = 6870,
            z                   = 250,
            y                   = 29240,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x01D5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0017,
        ),
    )

# id: 0x10002 offset: 0x3E2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x3E2
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x3E2
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 25600,
            triggerZ            = 0,
            triggerY            = 28000,
            triggerRange        = 1400,
            actorX              = 24920,
            actorZ              = 1000,
            actorY              = 28100,
            flags               = 0x007C,
            talkScenaIndex      = 0x0001,
            talkFunctionIndex   = 0x0000,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -4000,
            triggerZ            = 250,
            triggerY            = 33700,
            triggerRange        = 400,
            actorX              = -5500,
            actorZ              = 1800,
            actorY              = 33800,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000E,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -23760,
            triggerZ            = 0,
            triggerY            = 6340,
            triggerRange        = 1400,
            actorX              = -23760,
            actorZ              = 1500,
            actorY              = 6340,
            flags               = 0x007C,
            talkScenaIndex      = 0x0001,
            talkFunctionIndex   = 0x0001,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 28730,
            triggerZ            = 0,
            triggerY            = 37220,
            triggerRange        = 800,
            actorX              = 28730,
            actorZ              = 1800,
            actorY              = 37220,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0018,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x472
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_4B9',
    )

    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x0011, 0x0080)
    ChrSetFlags(0x0011, 0x0008)
    ChrSetPos(0x0008, 29470, 0, 32220, 180)

    If(
        (
            (Expr.Eval, "OP_29(0x001E, 0x00, 0x04)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4A7',
    )

    Jump('loc_4B6')

    def _loc_4A7(): pass

    label('loc_4A7')

    If(
        (
            (Expr.Eval, "OP_29(0x001E, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_4B6',
    )

    ChrClearFlags(0x001B, 0x0080)

    def _loc_4B6(): pass

    label('loc_4B6')

    Jump('loc_62D')

    def _loc_4B9(): pass

    label('loc_4B9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_500',
    )

    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x0011, 0x0080)
    ChrSetFlags(0x0011, 0x0008)
    ChrSetPos(0x0008, 29470, 0, 32220, 180)

    If(
        (
            (Expr.Eval, "OP_29(0x001E, 0x00, 0x04)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4EE',
    )

    Jump('loc_4FD')

    def _loc_4EE(): pass

    label('loc_4EE')

    If(
        (
            (Expr.Eval, "OP_29(0x001E, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_4FD',
    )

    ChrClearFlags(0x001B, 0x0080)

    def _loc_4FD(): pass

    label('loc_4FD')

    Jump('loc_62D')

    def _loc_500(): pass

    label('loc_500')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            Expr.Return,
        ),
        'loc_54C',
    )

    ChrSetFlags(0x000A, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrSetFlags(0x0011, 0x0080)
    ChrSetFlags(0x0011, 0x0008)
    ChrSetPos(0x0008, 29470, 0, 32220, 180)

    If(
        (
            (Expr.Eval, "OP_29(0x001E, 0x00, 0x04)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_53A',
    )

    Jump('loc_549')

    def _loc_53A(): pass

    label('loc_53A')

    If(
        (
            (Expr.Eval, "OP_29(0x001E, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_549',
    )

    ChrClearFlags(0x001B, 0x0080)

    def _loc_549(): pass

    label('loc_549')

    Jump('loc_62D')

    def _loc_54C(): pass

    label('loc_54C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_574',
    )

    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x0011, 0x0080)
    ChrSetFlags(0x0011, 0x0008)

    If(
        (
            (Expr.Eval, "OP_29(0x001E, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_571',
    )

    ChrClearFlags(0x001B, 0x0080)

    def _loc_571(): pass

    label('loc_571')

    Jump('loc_62D')

    def _loc_574(): pass

    label('loc_574')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_5A3',
    )

    ChrSetFlags(0x000A, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x0008, 29470, 0, 32220, 180)

    Jump('loc_62D')

    def _loc_5A3(): pass

    label('loc_5A3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 6, 0x41E)),
            Expr.Return,
        ),
        'loc_5CD',
    )

    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x0011, 0x0080)
    ChrSetFlags(0x0011, 0x0008)
    ChrSetPos(0x0008, 29470, 0, 32220, 180)

    Jump('loc_62D')

    def _loc_5CD(): pass

    label('loc_5CD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_5FC',
    )

    ChrSetFlags(0x0011, 0x0080)
    ChrSetFlags(0x0011, 0x0008)
    ChrClearFlags(0x0015, 0x0080)
    ChrClearFlags(0x0016, 0x0080)
    ChrSetPos(0x0008, 29470, 0, 32220, 180)

    Jump('loc_62D')

    def _loc_5FC(): pass

    label('loc_5FC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 0, 0x418)),
            Expr.Return,
        ),
        'loc_610',
    )

    ChrSetFlags(0x0011, 0x0080)
    ChrSetFlags(0x0011, 0x0008)

    Jump('loc_62D')

    def _loc_610(): pass

    label('loc_610')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_62D',
    )

    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x0008, 29470, 0, 32220, 180)

    def _loc_62D(): pass

    label('loc_62D')

    Return()

# id: 0x0001 offset: 0x62E
@scena.Code('func_01_62E')
def func_01_62E():
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
        'loc_64F',
    )

    OP_B1('t2131_y')

    Jump('loc_658')

    def _loc_64F(): pass

    label('loc_64F')

    OP_B1('t2131_n')

    def _loc_658(): pass

    label('loc_658')

    If(
        (
            (Expr.Eval, "OP_29(0x0020, 0x01, 0x0004)"),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x0020, 0x00, 0x40)"),
            Expr.Or,
            (Expr.Eval, "OP_29(0x0020, 0x01, 0x0008)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_677',
    )

    OP_64(0x00, 0x0001)

    def _loc_677(): pass

    label('loc_677')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_681',
    )

    Jump('loc_6CE')

    def _loc_681(): pass

    label('loc_681')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_68B',
    )

    Jump('loc_6CE')

    def _loc_68B(): pass

    label('loc_68B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            Expr.Return,
        ),
        'loc_695',
    )

    Jump('loc_6CE')

    def _loc_695(): pass

    label('loc_695')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_69F',
    )

    Jump('loc_6CE')

    def _loc_69F(): pass

    label('loc_69F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_6A9',
    )

    Jump('loc_6CE')

    def _loc_6A9(): pass

    label('loc_6A9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 6, 0x41E)),
            Expr.Return,
        ),
        'loc_6B3',
    )

    Jump('loc_6CE')

    def _loc_6B3(): pass

    label('loc_6B3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_6BD',
    )

    Jump('loc_6CE')

    def _loc_6BD(): pass

    label('loc_6BD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 0, 0x418)),
            Expr.Return,
        ),
        'loc_6C7',
    )

    Jump('loc_6CE')

    def _loc_6C7(): pass

    label('loc_6C7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_6CE',
    )

    def _loc_6CE(): pass

    label('loc_6CE')

    Return()

# id: 0x0002 offset: 0x6CF
@scena.Code('func_02_6CF')
def func_02_6CF():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_6E4',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_6CF')

    def _loc_6E4(): pass

    label('loc_6E4')

    Return()

# id: 0x0003 offset: 0x6E5
@scena.Code('func_03_6E5')
def func_03_6E5():
    TalkBegin(0x0017)

    If(
        (
            (Expr.Eval, "OP_40(0x0332)"),
            (Expr.Eval, "OP_29(0x0021, 0x01, 0x0800)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_93F',
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
            TXT(0x02, '欢迎品尝「健康泡饭」500米拉\n'),
            TXT(0x03, '归还钓鱼竿\n'),
            TXT(0x04, '离开\n'),
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
        'loc_77A',
    )

    OP_0D()
    OP_A9(0x24)
    OP_56(0x00)
    TalkEnd(0x0017)

    Return()

    def _loc_77A(): pass

    label('loc_77A')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_874',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x12),
            (Expr.PushLong, 0x1F4),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_83F',
    )

    RemoveMira(500)
    FadeOut(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    PlaySE(11, 0x00, 0x64)

    Talk(
        (
            TxtCtl.ShowAll,
            (TxtCtl.SetColor, 0x0),
            '尝了尝',
            (TxtCtl.SetColor, 0x2),
            '健康泡饭',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetStatus(0x0000, 0xFD, 750)
    ChrSetStatus(0x0001, 0xFD, 750)
    ChrSetStatus(0x0002, 0xFD, 750)
    ChrSetStatus(0x0003, 0xFD, 750)
    ChrSetStatus(0x0004, 0xFD, 750)
    ChrSetStatus(0x0005, 0xFD, 750)
    ChrSetStatus(0x0006, 0xFD, 750)
    ChrSetStatus(0x0007, 0xFD, 750)

    If(
        (
            (Expr.Eval, "OP_40(0x020D)"),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_831',
    )

    If(
        (
            (Expr.Eval, "OP_AC(0x0006)"),
            Expr.Return,
        ),
        'loc_80B',
    )

    Jump('loc_831')

    def _loc_80B(): pass

    label('loc_80B')

    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            TxtCtl.ShowAll,
            (TxtCtl.SetColor, 0x0),
            '学会了',
            (TxtCtl.SetColor, 0x2),
            '健康泡饭',
            (TxtCtl.SetColor, 0x0),
            '的做法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_831(): pass

    label('loc_831')

    OP_56(0x00)
    FadeIn(1000, 0)

    Jump('loc_865')

    def _loc_83F(): pass

    label('loc_83F')

    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            '没有足够的米拉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeIn(300, 0)
    def _loc_865(): pass

    label('loc_865')

    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x0017)

    Return()

    def _loc_874(): pass

    label('loc_874')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_92B',
    )

    RemoveItem(0x0332, 1)
    Sleep(400)

    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '归还了',
            (TxtCtl.SetColor, 0x2),
            '钓鱼竿',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(
        0x00FE,
        (
            '哦，辛苦了。\n',
            '钓鱼的成果怎么样啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果饿了就告诉我。\n',
            '我给你们做最好的料理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0017)

    Return()

    def _loc_92B(): pass

    label('loc_92B')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_93C',
    )

    TalkEnd(0x0017)

    Return()

    def _loc_93C(): pass

    label('loc_93C')

    Jump('loc_D0A')

    def _loc_93F(): pass

    label('loc_93F')

    If(
        (
            (Expr.Eval, "OP_40(0x0332)"),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x0021, 0x01, 0x0800)"),
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0021, 0x01, 0x0010)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_B88',
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
            TXT(0x02, '欢迎品尝「健康泡饭」500米拉\n'),
            TXT(0x03, '借钓鱼竿\n'),
            TXT(0x04, '离开\n'),
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
        'loc_9D9',
    )

    OP_0D()
    OP_A9(0x24)
    OP_56(0x00)
    TalkEnd(0x0017)

    Return()

    def _loc_9D9(): pass

    label('loc_9D9')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_AD3',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x12),
            (Expr.PushLong, 0x1F4),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_A9E',
    )

    RemoveMira(500)
    FadeOut(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    PlaySE(11, 0x00, 0x64)

    Talk(
        (
            TxtCtl.ShowAll,
            (TxtCtl.SetColor, 0x0),
            '尝了尝',
            (TxtCtl.SetColor, 0x2),
            '健康泡饭',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetStatus(0x0000, 0xFD, 750)
    ChrSetStatus(0x0001, 0xFD, 750)
    ChrSetStatus(0x0002, 0xFD, 750)
    ChrSetStatus(0x0003, 0xFD, 750)
    ChrSetStatus(0x0004, 0xFD, 750)
    ChrSetStatus(0x0005, 0xFD, 750)
    ChrSetStatus(0x0006, 0xFD, 750)
    ChrSetStatus(0x0007, 0xFD, 750)

    If(
        (
            (Expr.Eval, "OP_40(0x020D)"),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A90',
    )

    If(
        (
            (Expr.Eval, "OP_AC(0x0006)"),
            Expr.Return,
        ),
        'loc_A6A',
    )

    Jump('loc_A90')

    def _loc_A6A(): pass

    label('loc_A6A')

    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            TxtCtl.ShowAll,
            (TxtCtl.SetColor, 0x0),
            '学会了',
            (TxtCtl.SetColor, 0x2),
            '健康泡饭',
            (TxtCtl.SetColor, 0x0),
            '的做法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A90(): pass

    label('loc_A90')

    OP_56(0x00)
    FadeIn(1000, 0)

    Jump('loc_AC4')

    def _loc_A9E(): pass

    label('loc_A9E')

    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            '没有足够的米拉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeIn(300, 0)
    def _loc_AC4(): pass

    label('loc_AC4')

    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x0017)

    Return()

    def _loc_AD3(): pass

    label('loc_AD3')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B74',
    )

    ChrTalk(
        0x00FE,
        (
            '哦，要去钓鱼吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    AddItem(0x0332, 1)
    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '借来了',
            (TxtCtl.SetColor, 0x2),
            '钓鱼竿',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(
        0x00FE,
        (
            '#1820170488V如果用完了，\n',
            '记得把它还回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0017)

    Return()

    def _loc_B74(): pass

    label('loc_B74')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B85',
    )

    TalkEnd(0x0017)

    Return()

    def _loc_B85(): pass

    label('loc_B85')

    Jump('loc_D0A')

    def _loc_B88(): pass

    label('loc_B88')

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
            TXT(0x01, '买东西\n'),
            TXT(0x02, '欢迎品尝「健康泡饭」500米拉\n'),
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
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_BFF',
    )

    OP_0D()
    OP_A9(0x24)
    OP_56(0x00)
    TalkEnd(0x0017)

    Return()

    def _loc_BFF(): pass

    label('loc_BFF')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_CF9',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x12),
            (Expr.PushLong, 0x1F4),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_CC4',
    )

    RemoveMira(500)
    FadeOut(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    PlaySE(11, 0x00, 0x64)

    Talk(
        (
            TxtCtl.ShowAll,
            (TxtCtl.SetColor, 0x0),
            '尝了尝',
            (TxtCtl.SetColor, 0x2),
            '健康泡饭',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetStatus(0x0000, 0xFD, 750)
    ChrSetStatus(0x0001, 0xFD, 750)
    ChrSetStatus(0x0002, 0xFD, 750)
    ChrSetStatus(0x0003, 0xFD, 750)
    ChrSetStatus(0x0004, 0xFD, 750)
    ChrSetStatus(0x0005, 0xFD, 750)
    ChrSetStatus(0x0006, 0xFD, 750)
    ChrSetStatus(0x0007, 0xFD, 750)

    If(
        (
            (Expr.Eval, "OP_40(0x020D)"),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_CB6',
    )

    If(
        (
            (Expr.Eval, "OP_AC(0x0006)"),
            Expr.Return,
        ),
        'loc_C90',
    )

    Jump('loc_CB6')

    def _loc_C90(): pass

    label('loc_C90')

    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            TxtCtl.ShowAll,
            (TxtCtl.SetColor, 0x0),
            '学会了',
            (TxtCtl.SetColor, 0x2),
            '健康泡饭',
            (TxtCtl.SetColor, 0x0),
            '的做法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_CB6(): pass

    label('loc_CB6')

    OP_56(0x00)
    FadeIn(1000, 0)

    Jump('loc_CEA')

    def _loc_CC4(): pass

    label('loc_CC4')

    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            '没有足够的米拉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeIn(300, 0)
    def _loc_CEA(): pass

    label('loc_CEA')

    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x0017)

    Return()

    def _loc_CF9(): pass

    label('loc_CF9')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D0A',
    )

    TalkEnd(0x0017)

    Return()

    def _loc_D0A(): pass

    label('loc_D0A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Or,
            (Expr.Eval, "OP_29(0x0021, 0x01, 0x1000)"),
            (Expr.Eval, "OP_29(0x0021, 0x01, 0x0004)"),
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0021, 0x01, 0x0800)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0021, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0021, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_F40',
    )

    OP_28(0x0021, 0x01, 0x0800)

    ChrTalk(
        0x00FE,
        (
            '#1820170484V您好，欢迎光临。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010170485V#000F请问一下，\n',
            '能把二楼的那个钓鱼竿借给我们吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1820170486V哦，当然可以。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1820170487V你们只要说一声，\n',
            '随时都可以借走的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
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
            TXT(0x00, '【借钓鱼竿】\n'),
            TXT(0x01, '【不借】\n'),
        ),
    )

    MenuEnd(0x0001)

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
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_ED4',
    )

    OP_0D()
    AddItem(0x0332, 1)
    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '借来了',
            (TxtCtl.SetColor, 0x2),
            '钓鱼竿',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(
        0x00FE,
        (
            '#1820170488V如果用完了，\n',
            '记得把它还回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0017)

    Return()

    def _loc_ED4(): pass

    label('loc_ED4')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_F3D',
    )

    ChrTalk(
        0x00FE,
        (
            '#1820170489V如果需要，随时可以找我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1820170490V我会马上把钓鱼竿借给你们的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0017)

    Return()

    def _loc_F3D(): pass

    label('loc_F3D')

    Jump('loc_14F0')

    def _loc_F40(): pass

    label('loc_F40')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_1061',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_FFE',
    )

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    ChrTalk(
        0x00FE,
        (
            '现任市长已经被罢免了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就算是戴尔蒙家族的人，\n',
            '做出这种伤天害理的事，\n',
            '也肯定是要受到惩治的啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就连那些小混混也都被这件事吓一跳，\n',
            '都说戴尔蒙做得太过分了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_105E')

    def _loc_FFE(): pass

    label('loc_FFE')

    ChrTalk(
        0x00FE,
        (
            '选下一届市长的话，\n',
            '还是要选波尔多斯老大。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是他做市长的话，\n',
            '我想一定能把卢安治理好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_105E(): pass

    label('loc_105E')

    Jump('loc_14F0')

    def _loc_1061(): pass

    label('loc_1061')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_1171',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1102',
    )

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    ChrTalk(
        0x00FE,
        (
            '市长曾经准备\n',
            '停止提供对港湾设施的援助。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果不是波尔多斯老大直接和他面谈的话，\n',
            '还不知道会怎样呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '卢安还是很需要一个港口的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_116E')

    def _loc_1102(): pass

    label('loc_1102')

    ChrTalk(
        0x00FE,
        (
            '市长曾经准备\n',
            '停止提供对港湾设施的援助。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果不是波尔多斯老大直接和他面谈的话，\n',
            '还不知道会怎样呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_116E(): pass

    label('loc_116E')

    Jump('loc_14F0')

    def _loc_1171(): pass

    label('loc_1171')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_1210',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_11DA',
    )

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    ChrTalk(
        0x00FE,
        (
            '刚才有个红头发的游击士\n',
            '来这里打听了一些事情……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯～\n',
            '我好像在哪里见过他。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_120D')

    def _loc_11DA(): pass

    label('loc_11DA')

    ChrTalk(
        0x00FE,
        (
            '刚才那个红头发的游击士\n',
            '我好像在哪里见过他……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_120D(): pass

    label('loc_120D')

    Jump('loc_14F0')

    def _loc_1210(): pass

    label('loc_1210')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_1339',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_12DA',
    )

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    ChrTalk(
        0x00FE,
        (
            '渡鸦帮的那些人\n',
            '也经常来这家店。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在的那些家伙\n',
            '并不是粗野，\n',
            '而只是没骨气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为对自己没有信心，\n',
            '而将愤怒发泄在周围的人身上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过他们以前\n',
            '可确实是坏到骨子里了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1336')

    def _loc_12DA(): pass

    label('loc_12DA')

    ChrTalk(
        0x00FE,
        (
            '现在渡鸦帮的那些人\n',
            '并不是粗野，而只是没骨气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过他们以前\n',
            '可确实是坏到骨子里了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1336(): pass

    label('loc_1336')

    Jump('loc_14F0')

    def _loc_1339(): pass

    label('loc_1339')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_1443',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_13D3',
    )

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    ChrTalk(
        0x00FE,
        (
            '我原来也是个渔夫。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这家店里所使用的材料，\n',
            '都是我起早摸黑\n',
            '出海捕获而来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我可不是在自夸，\n',
            '这里的菜总是卢安最新鲜的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1440')

    def _loc_13D3(): pass

    label('loc_13D3')

    ChrTalk(
        0x00FE,
        (
            '这家店里所使用的材料，\n',
            '都是我起早摸黑\n',
            '出海捕获而来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我可不是在自夸，\n',
            '这里的菜总是卢安最新鲜的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1440(): pass

    label('loc_1440')

    Jump('loc_14F0')

    def _loc_1443(): pass

    label('loc_1443')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 4, 0x414)),
            Expr.Return,
        ),
        'loc_14F0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_14C7',
    )

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    ChrTalk(
        0x00FE,
        (
            '您好，欢迎光临！\n',
            '这里是亚克罗萨船员酒吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这里主要是\n',
            '渔夫和船员集中的酒馆，\n',
            '当然也欢迎一般的顾客啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_14F0')

    def _loc_14C7(): pass

    label('loc_14C7')

    ChrTalk(
        0x00FE,
        (
            '欢迎光临！\n',
            '这里是亚克罗萨船员酒吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_14F0(): pass

    label('loc_14F0')

    TalkEnd(0x0017)

    Return()

# id: 0x0004 offset: 0x14F4
@scena.Code('func_04_14F4')
def func_04_14F4():
    TalkBegin(0x000A)

    ChrTalk(
        0x00FE,
        (
            '定期船停航了，\n',
            '我只能从蔡斯步行而来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，真是的。\n',
            '路上好危险呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎呀哎呀，\n',
            '我再也不想这样了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000A)

    Return()

# id: 0x0005 offset: 0x156C
@scena.Code('func_05_156C')
def func_05_156C():
    TalkBegin(0x0018)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_15FA',
    )

    ChrTalk(
        0x00FE,
        (
            '马上就要出航了，\n',
            '遇上选举的话我就不能投票了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，要是能选出一个\n',
            '为港口事业着想的好市长，\n',
            '那对我们来说就最好不过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A14')

    def _loc_15FA(): pass

    label('loc_15FA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_171B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_16A6',
    )

    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    ChrTalk(
        0x00FE,
        (
            '下一次出海，\n',
            '要向埃雷波尼亚帝国运送导力器制品。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他们的港口有很多军舰驻扎，\n',
            '很有压迫感……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '即使现在想到入港的时候，\n',
            '我还是会觉得很紧张。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1718')

    def _loc_16A6(): pass

    label('loc_16A6')

    ChrTalk(
        0x00FE,
        (
            '下一次出海，\n',
            '要向埃雷波尼亚帝国运送导力器制品。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他们的港口有很多军舰驻扎，\n',
            '那种压迫感让我感到很紧张……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1718(): pass

    label('loc_1718')

    Jump('loc_1A14')

    def _loc_171B(): pass

    label('loc_171B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_1822',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_17D1',
    )

    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    ChrTalk(
        0x00FE,
        (
            '我在休假日\n',
            '也要帮忙装载货物。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '该让我多休息会儿才对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……但是，\n',
            '我可没有放弃当水手的打算。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我还是很喜欢大海的，\n',
            '而且这也是份值得骄傲的工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_181F')

    def _loc_17D1(): pass

    label('loc_17D1')

    ChrTalk(
        0x00FE,
        (
            '我在休假日\n',
            '也要帮忙装载货物。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……但是，\n',
            '我可没有放弃当水手的打算。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_181F(): pass

    label('loc_181F')

    Jump('loc_1A14')

    def _loc_1822(): pass

    label('loc_1822')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_192B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_18C3',
    )

    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    ChrTalk(
        0x00FE,
        (
            '来这里的途中，\n',
            '我看见有个孩子向着\n',
            '仓库的方向飞奔过去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '奇怪了，\n',
            '他要去那种地方做什么呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只要不被仓库里的\n',
            '那些家伙缠上就好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1928')

    def _loc_18C3(): pass

    label('loc_18C3')

    ChrTalk(
        0x00FE,
        (
            '来这里的途中，\n',
            '我看见有个孩子向着\n',
            '仓库的方向飞奔过去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只要不被仓库里的\n',
            '那些家伙缠上就好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1928(): pass

    label('loc_1928')

    Jump('loc_1A14')

    def _loc_192B(): pass

    label('loc_192B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_1988',
    )

    ChrTalk(
        0x00FE,
        (
            '我是贸易商船的航海员。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然现在非常悠闲，\n',
            '不过平时有好几个月要海上度过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A14')

    def _loc_1988(): pass

    label('loc_1988')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 4, 0x414)),
            Expr.Return,
        ),
        'loc_1A14',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_19F6',
    )

    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    ChrTalk(
        0x00FE,
        (
            '嗝……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我刚从卡尔瓦德共和国\n',
            '返航回到这里来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好久没在陆地上了……嗝……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A14')

    def _loc_19F6(): pass

    label('loc_19F6')

    ChrTalk(
        0x00FE,
        (
            '老大～！！　再来一杯～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A14(): pass

    label('loc_1A14')

    TalkEnd(0x0018)

    Return()

# id: 0x0006 offset: 0x1A18
@scena.Code('func_06_1A18')
def func_06_1A18():
    TalkBegin(0x0019)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_1A72',
    )

    ChrTalk(
        0x00FE,
        (
            '市长真的被捕了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然不很清楚情况，\n',
            '不过好像发生了很不得了的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1DD1')

    def _loc_1A72(): pass

    label('loc_1A72')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_1AF5',
    )

    ChrTalk(
        0x00FE,
        (
            '今天早上灯塔里的灯还是没有灭，\n',
            '到底发生什么事情了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我想那个弗科特大爷\n',
            '不会像我们这种人一样\n',
            '在偷懒打瞌睡吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1DD1')

    def _loc_1AF5(): pass

    label('loc_1AF5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_1B4C',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，今天打渔大丰收。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '鱼总是集中在同一个地方，\n',
            '这样打渔真是轻松啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1DD1')

    def _loc_1B4C(): pass

    label('loc_1B4C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_1C15',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1BD9',
    )

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    ChrTalk(
        0x00FE,
        (
            '仓库被那些家伙们占据着，\n',
            '为什么市长一点表示都没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '算了，反正我是个渔夫，\n',
            '这种麻烦的事情我可不想沾上什么边。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C12')

    def _loc_1BD9(): pass

    label('loc_1BD9')

    ChrTalk(
        0x00FE,
        (
            '仓库被那些家伙们占据着，\n',
            '为什么市长一点表示都没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C12(): pass

    label('loc_1C12')

    Jump('loc_1DD1')

    def _loc_1C15(): pass

    label('loc_1C15')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_1CF1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1C9A',
    )

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    ChrTalk(
        0x00FE,
        (
            '亚瑟利亚湾的海鲜\n',
            '真的非常美味呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对了，现在这个季节……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我向你们强烈推荐\n',
            '菜单上的这个酒蒸鱼籽。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1CEE')

    def _loc_1C9A(): pass

    label('loc_1C9A')

    ChrTalk(
        0x00FE,
        (
            '亚瑟利亚湾的海鲜\n',
            '真的非常美味呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我向你们强烈推荐\n',
            '菜单上的这个酒蒸鱼籽。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1CEE(): pass

    label('loc_1CEE')

    Jump('loc_1DD1')

    def _loc_1CF1(): pass

    label('loc_1CF1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 4, 0x414)),
            Expr.Return,
        ),
        'loc_1DD1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1D7D',
    )

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    ChrTalk(
        0x00FE,
        (
            '最近加入的同行\n',
            '非常能干活呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我除了会捕鱼之外，\n',
            '什么都不会了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总之只要还有人吃鱼，\n',
            '我就会继续做渔夫。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1DD1')

    def _loc_1D7D(): pass

    label('loc_1D7D')

    ChrTalk(
        0x00FE,
        (
            '我除了会捕鱼之外，\n',
            '什么都不会了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总之只要还有人吃鱼，\n',
            '我就会继续做渔夫。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1DD1(): pass

    label('loc_1DD1')

    TalkEnd(0x0019)

    Return()

# id: 0x0007 offset: 0x1DD5
@scena.Code('func_07_1DD5')
def func_07_1DD5():
    TalkBegin(0x001A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_1E38',
    )

    ChrTalk(
        0x00FE,
        (
            '北街区那些家伙\n',
            '应该是想选诺曼做市长吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们这边则是想选\n',
            '波尔多斯来做市长。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_22A7')

    def _loc_1E38(): pass

    label('loc_1E38')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_1ECC',
    )

    ChrTalk(
        0x00FE,
        (
            '现在不同于以往，\n',
            '港湾的设施建设都无法取得\n',
            '计划中那么多预算。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然波尔多斯主任很辛苦，\n',
            '但我还是希望作为负责人的他\n',
            '能够更加努力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_22A7')

    def _loc_1ECC(): pass

    label('loc_1ECC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_1FD2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1F94',
    )

    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))

    ChrTalk(
        0x00FE,
        (
            '以前卢安是军事要地，\n',
            '百日战役的时候这里可是激战连连。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总之，如果这里被攻破，\n',
            '到瓦雷利亚湖那一带就很容易被拿下了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，在瓦雷利亚湖\n',
            '还有一个坚不可摧的雷斯顿要塞。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1FCF')

    def _loc_1F94(): pass

    label('loc_1F94')

    ChrTalk(
        0x00FE,
        (
            '以前卢安是军事要地，\n',
            '百日战役的时候这里可是激战连连。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1FCF(): pass

    label('loc_1FCF')

    Jump('loc_22A7')

    def _loc_1FD2(): pass

    label('loc_1FD2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_213F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_20B2',
    )

    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))

    ChrTalk(
        0x00FE,
        (
            '流经这个城市的卢比诺川\n',
            '和位于利贝尔王国中央的\n',
            '瓦雷利亚湖相连。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在港口装运的海外物资\n',
            '都会经过这条运河\n',
            '直接运送到位于湖畔的王都。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '正因为这样，以前就有许多\n',
            '从国外来的各式各样的商人聚集于此。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_213C')

    def _loc_20B2(): pass

    label('loc_20B2')

    ChrTalk(
        0x00FE,
        (
            '流经这个城市的卢比诺川\n',
            '和位于利贝尔王国中央的\n',
            '瓦雷利亚湖相连。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在港口装运的海外物资\n',
            '都会经过这条运河\n',
            '直接运送到位于湖畔的王都。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_213C(): pass

    label('loc_213C')

    Jump('loc_22A7')

    def _loc_213F(): pass

    label('loc_213F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_21C5',
    )

    ChrTalk(
        0x00FE,
        (
            '如果想赚钱的话，\n',
            '比起做普通的船员，\n',
            '还不如开展观光事业比较好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，\n',
            '在这里聚集的这些家伙们\n',
            '可不是那么识时务……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_22A7')

    def _loc_21C5(): pass

    label('loc_21C5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 4, 0x414)),
            Expr.Return,
        ),
        'loc_22A7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2257',
    )

    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))

    ChrTalk(
        0x00FE,
        (
            '呼，\n',
            '出海之后喝的第一杯酒是非常特别的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……以前，\n',
            '这里是船员和渔夫的城市。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，\n',
            '现在出海的人数减少了很多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_22A7')

    def _loc_2257(): pass

    label('loc_2257')

    ChrTalk(
        0x00FE,
        (
            '……以前，\n',
            '这里是船员和渔夫的城市。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，\n',
            '现在出海的人数减少了很多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_22A7(): pass

    label('loc_22A7')

    TalkEnd(0x001A)

    Return()

# id: 0x0008 offset: 0x22AB
@scena.Code('func_08_22AB')
def func_08_22AB():
    TalkBegin(0x000B)

    ChrTalk(
        0x00FE,
        (
            '#0640061002V#226F可恶，一个小小的女孩\n',
            '竟敢羞辱我这个未来的国王……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640061003V#224F嘿～一决胜负吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000B)

    Return()

# id: 0x0009 offset: 0x231D
@scena.Code('func_09_231D')
def func_09_231D():
    TalkBegin(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_238F',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '#0660061004V#720F大人……大人……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660061005V天色已经不早了，\n',
            '我们还是回酒店去吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x000C, 0x0010)

    Jump('loc_23CD')

    def _loc_238F(): pass

    label('loc_238F')

    ChrTalk(
        0x00FE,
        (
            '#0660061006V#722F呼，\n',
            '虽然我也知道和他说这些没什么用……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_23CD(): pass

    label('loc_23CD')

    TalkEnd(0x000C)

    Return()

# id: 0x000A offset: 0x23D1
@scena.Code('func_0A_23D1')
def func_0A_23D1():
    TalkBegin(0x000D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            Expr.Return,
        ),
        'loc_24CE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_248D',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '#0270061007V#141F嘿嘿……\n',
            '这样所有的消息都收集齐了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270061008V这可能是大家想象不到的独家新闻呢。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270061009V#142F……接下来就是如何得到报道的确证了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24CB')

    def _loc_248D(): pass

    label('loc_248D')

    ChrTalk(
        0x00FE,
        (
            '#0270061010V#141F这可能是大家想象不到的独家新闻呢……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_24CB(): pass

    label('loc_24CB')

    Jump('loc_253B')

    def _loc_24CE(): pass

    label('loc_24CE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_253B',
    )

    ChrTalk(
        0x00FE,
        (
            '#0270050590V#141F哟，艾丝蒂尔、约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270050591V如果有什么事件发生，\n',
            '记得来给我提供资料啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_253B(): pass

    label('loc_253B')

    TalkEnd(0x000D)

    Return()

# id: 0x000B offset: 0x253F
@scena.Code('func_0B_253F')
def func_0B_253F():
    TalkBegin(0x000E)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_25A8',
    )

    ChrTalk(
        0x00FE,
        (
            '赌博和做买卖\n',
            '其实有几分相似。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '抱着玩玩儿的态度不会有什么压力，\n',
            '但是比较容易上瘾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2642')

    def _loc_25A8(): pass

    label('loc_25A8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_2642',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2615',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '呼，谈判结束了，\n',
            '我终于能够休息一下了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最近，\n',
            '米拉诺总是休假和出差连在一起。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2642')

    def _loc_2615(): pass

    label('loc_2615')

    ChrTalk(
        0x00FE,
        (
            '呼，谈判结束了，\n',
            '我终于能够休息一下了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2642(): pass

    label('loc_2642')

    TalkEnd(0x000E)

    Return()

# id: 0x000C offset: 0x2646
@scena.Code('func_0C_2646')
def func_0C_2646():
    TalkBegin(0x000F)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            Expr.Return,
        ),
        'loc_26B1',
    )

    ChrTalk(
        0x00FE,
        (
            '阿加特前辈好厉害。\n',
            '『重剑』的称号并非浪得虚名。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过在利贝尔\n',
            '好像还有更加厉害的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2824')

    def _loc_26B1(): pass

    label('loc_26B1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_2786',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2732',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '嘿哟、嘿哟……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '阿、阿嚏！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哆哆嗦嗦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '噗噜噗噜噗噜……\n',
            '染上感冒后，\n',
            '虽然很不舒服，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2783')

    def _loc_2732(): pass

    label('loc_2732')

    ChrTalk(
        0x00FE,
        (
            '不过我还是要吃很多饭！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '吃了之后才有体力，\n',
            '随时准备出击是游击士的职责！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2783(): pass

    label('loc_2783')

    Jump('loc_2824')

    def _loc_2786(): pass

    label('loc_2786')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_2824',
    )

    ChrTalk(
        0x00FE,
        (
            '之前，我在沙滩那里\n',
            '碰到一个非常敏捷的魔兽！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我本来想击退它的，\n',
            '但是一攻击，那把非常硬的剑就断了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然那家伙很小，\n',
            '但却绝不能小看它啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2824(): pass

    label('loc_2824')

    TalkEnd(0x000F)

    Return()

# id: 0x000D offset: 0x2828
@scena.Code('func_0D_2828')
def func_0D_2828():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_28AA',
    )

    ChrTalk(
        0x00FE,
        (
            '现役的市长被逮捕了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '根据利贝尔的法律，\n',
            '要进行市长选举。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '谁会是候选人呢，\n',
            '我对这一点\n',
            '非常感兴趣啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2C71')

    def _loc_28AA(): pass

    label('loc_28AA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_2935',
    )

    ChrTalk(
        0x0008,
        (
            '市长对我们这样的观光设施\n',
            '给予了很大的支持……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '而给港湾设施的预算\n',
            '年年都在削减。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '许许多多不满的声音\n',
            '也在日渐高涨。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2C71')

    def _loc_2935(): pass

    label('loc_2935')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            Expr.Return,
        ),
        'loc_2986',
    )

    ChrTalk(
        0x0008,
        (
            '本店的改建\n',
            '正在稳步进行中。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '离新装修的店重新开张已经不远了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2C71')

    def _loc_2986(): pass

    label('loc_2986')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_29F4',
    )

    ChrTalk(
        0x0008,
        (
            '转旋转圆盘的手艺是\n',
            '绝对不可以生疏下来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '为了让客人们得到消遣，\n',
            '精彩的表演也是很重要的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2C71')

    def _loc_29F4(): pass

    label('loc_29F4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_2A61',
    )

    ChrTalk(
        0x0008,
        (
            '为了配合重建，\n',
            '也差不多该\n',
            '购置个新轮盘了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我希望把这里装饰成\n',
            '观光客们能够经常来的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2C71')

    def _loc_2A61(): pass

    label('loc_2A61')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_2B6E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2B07',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x0008,
        (
            '旺季的时候，\n',
            '会有各地的游客过来玩两手。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '一旦观光业繁荣起来，\n',
            '客人会更加多吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '真希望这里快点装修完，\n',
            '然后像以往那样再次热闹起来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2B6B')

    def _loc_2B07(): pass

    label('loc_2B07')

    ChrTalk(
        0x0008,
        (
            '一旦观光业繁荣起来，\n',
            '客人会更加多吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '真希望这里快点装修完，\n',
            '然后像以往那样再次热闹起来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2B6B(): pass

    label('loc_2B6B')

    Jump('loc_2C71')

    def _loc_2B6E(): pass

    label('loc_2B6E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 0, 0x418)),
            Expr.Return,
        ),
        'loc_2BF9',
    )

    ChrTalk(
        0x0008,
        (
            '人生啊，\n',
            '就如同这个轮盘。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '即使今天非常顺手，\n',
            '说不定明天可能全盘皆输。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '可以的话，就请珍惜现在，\n',
            '好好享受不留遗憾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2C71')

    def _loc_2BF9(): pass

    label('loc_2BF9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_2C71',
    )

    ChrTalk(
        0x0008,
        (
            '拉旺塔尔赌吧\n',
            '将于女王诞辰庆典举行的同时\n',
            '重新向各位市民和游客开放。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '现在二楼的地板\n',
            '正在全面重新装修中。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2C71(): pass

    label('loc_2C71')

    TalkEnd(0x0008)

    Return()

# id: 0x000E offset: 0x2C75
@scena.Code('func_0E_2C75')
def func_0E_2C75():
    Call(0, 0x000F)

    Return()

# id: 0x000F offset: 0x2C7A
@scena.Code('func_0F_2C7A')
def func_0F_2C7A():
    TalkBegin(0x0010)

    If(
        (
            (Expr.Eval, "OP_29(0x001D, 0x00, 0x08)"),
            (Expr.Eval, "OP_29(0x001D, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x001D, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x001D, 0x01, 0x0004)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3569',
    )

    EventBegin(0x00)
    OP_4A(0x0010, 255)

    ChrTalk(
        0x0010,
        (
            '#1760160311V您好，欢迎光临。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#1760160312V…………嗯？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#1760160313V喂，你们几个。\n',
            '是要去巴伦诺灯塔吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2D87',
    )

    ChrTalk(
        0x0101,
        (
            '#0010160314V#000F嗯，是的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160315V我们要把这个维修工具箱\n',
            '交给弗科特老人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0010, 0x0101, 0)

    Jump('loc_2E8F')

    def _loc_2D87(): pass

    label('loc_2D87')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2DF3',
    )

    ChrTalk(
        0x0102,
        (
            '#0020160316V#010F嗯，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020160317V我们要把这个维修工具箱\n',
            '交给弗科特老人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0010, 0x0102, 0)

    Jump('loc_2E8F')

    def _loc_2DF3(): pass

    label('loc_2DF3')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2E8F',
    )

    ChrTalk(
        0x0105,
        (
            '#0060160318V#040F啊，是的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060160319V不过我只是\n',
            '稍微帮一下忙……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060160320V我们要把这个维修工具箱\n',
            '交给看守灯塔的弗科特老人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0010, 0x0105, 0)

    def _loc_2E8F(): pass

    label('loc_2E8F')

    ChrTalk(
        0x0010,
        (
            '#1760160321V果然是这样。\n',
            '怪不得你们拿着个大箱子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#1760160322V他老人家自从去了灯塔以后，\n',
            '已经很久没来过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#1760160323V希望他能够健康快乐啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160324V#000F老爷爷他以前很喜欢到这个店里来吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0010, 0x0101, 400)

    ChrTalk(
        0x0010,
        (
            '#1760160325V他是一个老渔夫了，\n',
            '对于酒和赌都很感兴趣。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#1760160326V他老人家最喜欢的就是\n',
            '用果实榨的汁所制成的，\n',
            '名为『亚瑟利亚葡萄酒』的鸡尾酒。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#1760160327V这种鸡尾酒\n',
            '和海鱼真是绝配。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#1760160328V可是他去了灯塔之后\n',
            '就再也没来品尝过了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#1760160329V他的工作可是十分艰苦的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160330V#003F嗯……\n',
            '真的很可怜呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#1760160331V哦，对了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#1760160332V如果方便的话，\n',
            '能带一瓶给他吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160333V#004F啊…………？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#1760160334V反正你们要去灯塔，\n',
            '所以我希望你们把鸡尾酒也带去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#1760160335V这倒不是什么委托。\n',
            '如果很忙的话，\n',
            '你们不接受也没有关系的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160336V#006F是给老爷爷捎去的对吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010160337V#006F我说，约修亚，\n',
            '应该是可以的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020160338V#010F嗯，我想没问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x001C, 0x00, 0x04)"),
            Expr.Return,
        ),
        'loc_32D7',
    )

    ChrTurnDirection(0x0101, 0x0105, 400)

    ChrTalk(
        0x0101,
        (
            '#0010160339V#505F唔，又多了一个需要小心携带的东西呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0101, 400)

    ChrTalk(
        0x0105,
        (
            '#0060160340V#041F呵呵，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_32D7(): pass

    label('loc_32D7')

    ChrTalk(
        0x0010,
        (
            '#1760160341V哦，\n',
            '那么记得帮我向他老人家问好哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3312')
    def lambda_3312():
        ChrTurnDirection(0x0101, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3312)

    @scena.Lambda('lambda_3320')
    def lambda_3320():
        ChrTurnDirection(0x0102, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_3320)

    @scena.Lambda('lambda_332E')
    def lambda_332E():
        ChrTurnDirection(0x0105, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_332E)

    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0102, 0x0001)
    WaitForThreadExit(0x0105, 0x0001)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '亚瑟利亚葡萄酒',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_28(0x001D, 0x01, 0x0004)
    AddItem(0x019A, 1)

    ChrTalk(
        0x0010,
        (
            '#1760160342V如果有下酒菜就更好了，\n',
            '不凑巧的是我这里的已经卖完了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#1760160343V这个季节用玛诺利亚村的特产\n',
            '『辣鳀鱼』来下酒是最爽的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#1760160344V……可惜没办法啊，\n',
            '这次只有酒了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#1760160345V你们努力工作吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_34B1',
    )

    ChrTalk(
        0x0101,
        (
            '#0010160346V#000F嗯，再见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3560')

    def _loc_34B1(): pass

    label('loc_34B1')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3508',
    )

    ChrTalk(
        0x0102,
        (
            '#0020160347V#010F嗯，再见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160348V#000F再见了，大叔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3560')

    def _loc_3508(): pass

    label('loc_3508')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3560',
    )

    ChrTalk(
        0x0105,
        (
            '#0060160349V#040F那么我们告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160348V#000F再见了，大叔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3560(): pass

    label('loc_3560')

    EventEnd(0x01)
    OP_4B(0x0010, 255)

    Jump('loc_3C2F')

    def _loc_3569(): pass

    label('loc_3569')

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
        'loc_35C4',
    )

    OP_0D()
    OP_A9(0x23)
    OP_56(0x00)
    TalkEnd(0x0010)

    Return()

    def _loc_35C4(): pass

    label('loc_35C4')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_35D5',
    )

    TalkEnd(0x0010)

    Return()

    def _loc_35D5(): pass

    label('loc_35D5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Return,
        ),
        'loc_3702',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x001D, 0x01, 0x2000)"),
            Expr.Return,
        ),
        'loc_3644',
    )

    ChrTalk(
        0x0010,
        (
            '老人家身体健康\n',
            '真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '特意帮忙送东西，真是谢谢你们。\n',
            '那么，工作要加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_36FF')

    def _loc_3644(): pass

    label('loc_3644')

    ChrTalk(
        0x0010,
        (
            '#1760160353V这次的事情\n',
            '你们可别往心里去哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#1760160354V本来也是我\n',
            '即兴拜托你们的嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#1760160355V反正慰问老人家的机会\n',
            '以后还多的是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#1760160356V到时候还要麻烦你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_36FF(): pass

    label('loc_36FF')

    Jump('loc_3C2F')

    def _loc_3702(): pass

    label('loc_3702')

    If(
        (
            (Expr.Eval, "OP_29(0x001D, 0x01, 0x2000)"),
            Expr.Return,
        ),
        'loc_3714',
    )

    Call(0, 0x0010)

    Jump('loc_3C2F')

    def _loc_3714(): pass

    label('loc_3714')

    If(
        (
            (Expr.Eval, "OP_29(0x001D, 0x00, 0x10)"),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x001D, 0x00, 0x40)"),
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x001D, 0x01, 0x0004)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_399D',
    )

    SetScenaFlags(ScenaFlag(0x0001, 5, 0xD))
    OP_28(0x001D, 0x01, 0x2000)

    ChrTalk(
        0x0010,
        (
            '#1760160357V哟，\n',
            '送维修工具箱的工作完成了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0010, 400)

    ChrTalk(
        0x0101,
        (
            '#0010160358V#003F嗯～抱歉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160359V最后还是没办法把工具箱送过去呢。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020160360V#017F对不起。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020160361V您还特地让我们送鸡尾酒的……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0010, 0x0102, 400)

    ChrTalk(
        0x0010,
        (
            '#1760160362V哦，是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#1760160363V你们不要介意。\n',
            '本来也是我\n',
            '即兴拜托你们的嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#1760160364V一开始我不是说了吗？\n',
            '如果太忙的话，\n',
            '不接受也没有关系的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160365V#007F真是太过意不去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0010, 0x0101, 400)

    ChrTalk(
        0x0010,
        (
            '#1760160366V慰问老人家的机会\n',
            '以后还多的是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#1760160356V到时候还要麻烦你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020160368V#010F是啊，\n',
            '以后也请多多关照。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0010, 0x0102, 400)

    ChrTalk(
        0x0010,
        (
            '#1760160369V哦，再见啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3C2F')

    def _loc_399D(): pass

    label('loc_399D')

    If(
        (
            (Expr.Eval, "OP_29(0x001D, 0x00, 0x10)"),
            (Expr.Eval, "OP_29(0x001D, 0x01, 0x0004)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3AFB',
    )

    OP_28(0x001D, 0x01, 0x2000)
    SetScenaFlags(ScenaFlag(0x0001, 5, 0xD))

    ChrTalk(
        0x0010,
        (
            '哟，送维修工具箱的\n',
            '看起来工作已经完成了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '弗科特他老人家\n',
            '身体还好吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#001F嗯，很健康呢。\n',
            '还让我们向大家问好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0010, 0x0101, 400)

    ChrTalk(
        0x0010,
        (
            '哦，是吗。\n',
            '那真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '这么老了还坚持工作，\n',
            '本来我一直很担心他的身体状况，\n',
            '看来没什么事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '特意帮忙送东西，真是谢谢你们。\n',
            '那么，工作要加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯，再见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3C2F')

    def _loc_3AFB(): pass

    label('loc_3AFB')

    If(
        (
            (Expr.Eval, "OP_29(0x001D, 0x01, 0x0004)"),
            (Expr.Eval, "OP_29(0x001D, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3C2B',
    )

    ChrTalk(
        0x0010,
        (
            '#1760160377V代我向老人家问好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#1760160378V如果要是有下酒菜\n',
            '就更好了…………\n',
            '不凑巧的是我这里的已经卖完了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#1760160343V这个季节用玛诺利亚村的特产\n',
            '『辣鳀鱼』来下酒是最爽的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#1760160344V……可惜没办法啊，\n',
            '这次只有酒了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#1760160345V好了，你们工作要努力哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3C2F')

    def _loc_3C2B(): pass

    label('loc_3C2B')

    Call(0, 0x0010)

    def _loc_3C2F(): pass

    label('loc_3C2F')

    TalkEnd(0x0010)

    Return()

# id: 0x0010 offset: 0x3C33
@scena.Code('func_10_3C33')
def func_10_3C33():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_3D72',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3D15',
    )

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x0010,
        (
            '渡鸦帮的家伙是被\n',
            '施了催眠术一类的东西，\n',
            '所以才做了市长的帮手。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '不瞒你们，\n',
            '我的弟弟也是其中的一员。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '他们平常不做正经事，\n',
            '是被社会摒弃的一群人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '真是不争气的家伙啊……\n',
            '这就叫做自食其果。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3D6F')

    def _loc_3D15(): pass

    label('loc_3D15')

    ChrTalk(
        0x0010,
        (
            '不瞒你们，\n',
            '我的弟弟也是渡鸦帮的一员。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '真是不争气的家伙啊……\n',
            '这就叫做自食其果。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3D6F(): pass

    label('loc_3D6F')

    Jump('loc_42CA')

    def _loc_3D72(): pass

    label('loc_3D72')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_3E1F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3DE7',
    )

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x0010,
        (
            '昨晚开始\n',
            '我弟弟就一直没有回家……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '他到底去哪里游手好闲了……\n',
            '算了，反正他总会回来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3E1C')

    def _loc_3DE7(): pass

    label('loc_3DE7')

    ChrTalk(
        0x0010,
        (
            '……唉，这个兔崽子，\n',
            '从小时候开始就让我操心……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3E1C(): pass

    label('loc_3E1C')

    Jump('loc_42CA')

    def _loc_3E1F(): pass

    label('loc_3E1F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            Expr.Return,
        ),
        'loc_3EB4',
    )

    ChrTalk(
        0x0010,
        (
            '二楼的改建到底\n',
            '要到什么时候才能结束啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '平时会有许多旅客\n',
            '慕名前来拉旺塔尔赌吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '不早点重新开业的话，\n',
            '本店的招牌可要垮了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_42CA')

    def _loc_3EB4(): pass

    label('loc_3EB4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_3FE0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3F5D',
    )

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x0010,
        (
            '哎呀哎呀，我弟弟这次\n',
            '真是给游击士协会添了很大麻烦啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '我早就料到会有这一天的到来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '算了，这也是个让那群笨蛋\n',
            '好好冷静一下的机会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3FDD')

    def _loc_3F5D(): pass

    label('loc_3F5D')

    ChrTalk(
        0x0010,
        (
            '哎呀哎呀，弟弟那家伙……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '这次真是给游击士协会\n',
            '添了很大的麻烦啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '算了，这也是个让那群笨蛋\n',
            '好好冷静一下的机会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3FDD(): pass

    label('loc_3FDD')

    Jump('loc_42CA')

    def _loc_3FE0(): pass

    label('loc_3FE0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_400F',
    )

    ChrTalk(
        0x0010,
        (
            '怎么了？\n',
            '你们是来找什么人的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_42CA')

    def _loc_400F(): pass

    label('loc_400F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_40D6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_40A6',
    )

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x0010,
        (
            '听说昨天弟弟\n',
            '那帮家伙们缠上市长了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '反抗比自己地位高的人，\n',
            '是想否定自己的自卑感吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '这样想来，他们还真是可悲啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_40D3')

    def _loc_40A6(): pass

    label('loc_40A6')

    ChrTalk(
        0x0010,
        (
            '好～\n',
            '新的一天又开始了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '加油干吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_40D3(): pass

    label('loc_40D3')

    Jump('loc_42CA')

    def _loc_40D6(): pass

    label('loc_40D6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 0, 0x418)),
            Expr.Return,
        ),
        'loc_41EF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4182',
    )

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x0010,
        (
            '弟弟那家伙加入了\n',
            '港口那边一个叫渡鸦帮的流氓集团。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '也不去找点工作做，\n',
            '只会给别人惹麻烦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '真是一点也不知道羞耻，\n',
            '怎么有脸去见老天爷啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_41EC')

    def _loc_4182(): pass

    label('loc_4182')

    ChrTalk(
        0x0010,
        (
            '弟弟那家伙加入了\n',
            '港口那边一个叫渡鸦帮的流氓集团。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '真是一点也不知道羞耻，\n',
            '怎么有脸去见老天爷啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_41EC(): pass

    label('loc_41EC')

    Jump('loc_42CA')

    def _loc_41EF(): pass

    label('loc_41EF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_42CA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4280',
    )

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x0010,
        (
            '第一次看到你们呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '你们是旅行者吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '如果是的话，\n',
            '就不要靠近港口的仓库。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '那一带是\n',
            '不良青年聚集的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_42CA')

    def _loc_4280(): pass

    label('loc_4280')

    ChrTalk(
        0x0010,
        (
            '你们最好不要到\n',
            '港口的仓库那边去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '那一带是\n',
            '不良青年聚集的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_42CA(): pass

    label('loc_42CA')

    TalkEnd(0x0010)

    Return()

# id: 0x0011 offset: 0x42CE
@scena.Code('func_11_42CE')
def func_11_42CE():
    TalkBegin(0x0011)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_43A3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4354',
    )

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x00FE,
        (
            '坐在那个座位上的人是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他不是米拉诺家的\n',
            '西蒙那小子吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '特里诺一家果然是\n',
            '柏斯商人的憧憬啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_43A0')

    def _loc_4354(): pass

    label('loc_4354')

    ChrTalk(
        0x00FE,
        (
            '米拉诺家的西蒙\n',
            '来这里了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '特里诺一家果然是\n',
            '柏斯商人的憧憬啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_43A0(): pass

    label('loc_43A0')

    Jump('loc_44F1')

    def _loc_43A3(): pass

    label('loc_43A3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 0, 0x418)),
            Expr.Return,
        ),
        'loc_4492',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4437',
    )

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x00FE,
        (
            '刚才在那边的牌桌上\n',
            '和别人赌博……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果自己赢了，\n',
            '当然很是高兴……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但如果被对手占了上风，\n',
            '就会变得很不愉快了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_448F')

    def _loc_4437(): pass

    label('loc_4437')

    ChrTalk(
        0x00FE,
        (
            '如果自己赢了，\n',
            '当然很是高兴……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但如果被对手占了上风，\n',
            '就会变得很不愉快了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_448F(): pass

    label('loc_448F')

    Jump('loc_44F1')

    def _loc_4492(): pass

    label('loc_4492')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_44F1',
    )

    ChrTalk(
        0x00FE,
        (
            '呼～因为定期船停航，\n',
            '我本以为生意谈不成了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '幸好我急急忙忙\n',
            '从柏斯赶过来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_44F1(): pass

    label('loc_44F1')

    TalkEnd(0x0011)

    Return()

# id: 0x0012 offset: 0x44F5
@scena.Code('func_12_44F5')
def func_12_44F5():
    TalkBegin(0x0012)
    OP_62(0x0012, 0x00000000, 2000, 0x08, 0x09, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '呼～\n',
            '偶尔独自一人也不错啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '父亲和女儿在二楼玩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0012)

    Return()

# id: 0x0013 offset: 0x4555
@scena.Code('func_13_4555')
def func_13_4555():
    TalkBegin(0x0013)

    ChrTalk(
        0x00FE,
        (
            '唔唔唔，再来一盘！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0013)

    Return()

# id: 0x0014 offset: 0x4574
@scena.Code('func_14_4574')
def func_14_4574():
    TalkBegin(0x0014)

    ChrTalk(
        0x00FE,
        (
            '好啊！！\n',
            '又是我赢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0014)

    Return()

# id: 0x0015 offset: 0x4596
@scena.Code('func_15_4596')
def func_15_4596():
    TalkBegin(0x0015)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_45BB',
    )

    ChrTalk(
        0x00FE,
        (
            '好，再来再来再来！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_45EB')

    def _loc_45BB(): pass

    label('loc_45BB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_45EB',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然有点晚了，\n',
            '不过我是来吃早饭的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_45EB(): pass

    label('loc_45EB')

    TalkEnd(0x0015)

    Return()

# id: 0x0016 offset: 0x45EF
@scena.Code('func_16_45EF')
def func_16_45EF():
    TalkBegin(0x0016)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_4627',
    )

    ChrTalk(
        0x00FE,
        (
            '唔～一旦输了，\n',
            '对胜负就会更加执着……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_467B')

    def _loc_4627(): pass

    label('loc_4627')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_467B',
    )

    ChrTalk(
        0x00FE,
        (
            '咦……\n',
            '我以为赌吧的底楼应该会很吵的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这家店给人感觉非常清爽呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_467B(): pass

    label('loc_467B')

    TalkEnd(0x0016)

    Return()

# id: 0x0017 offset: 0x467F
@scena.Code('func_17_467F')
def func_17_467F():
    TalkBegin(0x001B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_46DC',
    )

    ChrTalk(
        0x00FE,
        (
            '嘿嘿嘿，\n',
            '很快就可以解读这幅地图了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好～\n',
            '这一次一定要找到海盗的财宝。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4727')

    def _loc_46DC(): pass

    label('loc_46DC')

    ChrTalk(
        0x00FE,
        (
            '唔唔～哦，原来如此……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嘿嘿嘿，\n',
            '这幅地图的大概含义我已经明白了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4727(): pass

    label('loc_4727')

    TalkEnd(0x001B)

    Return()

# id: 0x0018 offset: 0x472B
@scena.Code('func_18_472B')
def func_18_472B():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '拉旺塔尔赌吧\n',
            '将于女王诞辰庆典举行的同时\n',
            '重新向各位市民和游客开放！！',
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
