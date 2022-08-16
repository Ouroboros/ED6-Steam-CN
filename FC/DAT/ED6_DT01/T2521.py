import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T2521_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2521   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'T2521.x'
    header.mapIndex       = 1
    header.bgm            = 14
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT01/T2521._SN', 'ED6_DT01/T2521_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
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
        ('ED6_DT07/CH01080._CH', 'ED6_DT07/CH01080P._CP'),
        ('ED6_DT07/CH01360._CH', 'ED6_DT07/CH01360P._CP'),
        ('ED6_DT07/CH02390._CH', 'ED6_DT07/CH02390P._CP'),
        ('ED6_DT07/CH02550._CH', 'ED6_DT07/CH02550P._CP'),
        ('ED6_DT07/CH01130._CH', 'ED6_DT07/CH01130P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH02103._CH', 'ED6_DT07/CH02103P._CP'),
        ('ED6_DT07/CH01023._CH', 'ED6_DT07/CH01023P._CP'),
        ('ED6_DT07/CH01033._CH', 'ED6_DT07/CH01033P._CP'),
        ('ED6_DT07/CH01070._CH', 'ED6_DT07/CH01070P._CP'),
        ('ED6_DT07/CH02050._CH', 'ED6_DT07/CH02050P._CP'),
        ('ED6_DT07/CH01043._CH', 'ED6_DT07/CH01043P._CP'),
        ('ED6_DT07/CH01213._CH', 'ED6_DT07/CH01213P._CP'),
        ('ED6_DT07/CH01080._CH', 'ED6_DT07/CH01080P._CP'),
        ('ED6_DT06/CH20021._CH', 'ED6_DT06/CH20021P._CP'),
        ('ED6_DT07/CH00013._CH', 'ED6_DT07/CH00013P._CP'),
        ('ED6_DT07/CH02553._CH', 'ED6_DT07/CH02553P._CP'),
    ]

# id: 0x10001 offset: 0x132
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '米克',
            x                   = -3600,
            z                   = 0,
            y                   = -6100,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '德尼斯',
            x                   = -31200,
            z                   = 0,
            y                   = 52500,
            direction           = 225,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '乔儿',
            x                   = 28700,
            z                   = 0,
            y                   = 55100,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '汉斯',
            x                   = 29600,
            z                   = 0,
            y                   = 53800,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '约修亚',
            x                   = 29600,
            z                   = 0,
            y                   = 53800,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '德波拉',
            x                   = 3500,
            z                   = 0,
            y                   = 4500,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            name                = '凯诺娜上尉',
            x                   = -4970,
            z                   = 250,
            y                   = -4830,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x01D5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            name                = '雷克斯',
            x                   = -1700,
            z                   = 250,
            y                   = -1000,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x01D5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            name                = '卡拉',
            x                   = -3000,
            z                   = 250,
            y                   = 300,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x01D5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            name                = '卢希娅',
            x                   = 550,
            z                   = 0,
            y                   = -2060,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '亚鲁瓦教授',
            x                   = 4120,
            z                   = 0,
            y                   = 2470,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0011,
        ),
        ScenaNpcData(
            name                = '西加罗',
            x                   = 3960,
            z                   = 100,
            y                   = -5890,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x01D5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0012,
        ),
        ScenaNpcData(
            name                = '艾德尔',
            x                   = 4000,
            z                   = 100,
            y                   = -4200,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x01D5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            name                = '罗基克',
            x                   = -31470,
            z                   = 0,
            y                   = 58630,
            direction           = 0,
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
            name                = 'CH22000',
            x                   = -31350,
            z                   = 330,
            y                   = 23900,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1835022,
            chipIndex           = 14,
            npcIndex            = 0x0166,
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
        ScenaEventData(
            x           = -2200,
            y           = 0,
            z           = 50000,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000015,
        ),
        ScenaEventData(
            x           = -2200,
            y           = 0,
            z           = 42000,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000016,
        ),
        ScenaEventData(
            x           = 2130,
            y           = 0,
            z           = 42010,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000017,
        ),
        ScenaEventData(
            x           = 2200,
            y           = 0,
            z           = 50000,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000018,
        ),
    )

# id: 0x10004 offset: 0x392
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 3340,
            triggerZ            = 0,
            triggerY            = 3110,
            triggerRange        = 400,
            actorX              = 3500,
            actorZ              = 1500,
            actorY              = 4500,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000B,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -31350,
            triggerZ            = 330,
            triggerY            = 23900,
            triggerRange        = 500,
            actorX              = -31350,
            actorZ              = 500,
            actorY              = 23900,
            flags               = 0x007C,
            talkScenaIndex      = 0x0001,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 2920,
            triggerZ            = 0,
            triggerY            = 49990,
            triggerRange        = 800,
            actorX              = 2920,
            actorZ              = 1000,
            actorY              = 49990,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000A,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -31560,
            triggerZ            = 0,
            triggerY            = 59430,
            triggerRange        = 800,
            actorX              = -31560,
            actorZ              = 1000,
            actorY              = 59430,
            flags               = 0x007C,
            talkScenaIndex      = 0x0001,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 0,
            triggerZ            = 0,
            triggerY            = 53550,
            triggerRange        = 800,
            actorX              = 0,
            actorZ              = 1000,
            actorY              = 53550,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0014,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x446
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_455',
    )

    ChrClearFlags(0x0008, 0x0080)

    Jump('loc_5BC')

    def _loc_455(): pass

    label('loc_455')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            Expr.Return,
        ),
        'loc_45F',
    )

    Jump('loc_5BC')

    def _loc_45F(): pass

    label('loc_45F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_49F',
    )

    ChrClearFlags(0x0009, 0x0080)
    ChrSetFlags(0x0009, 0x0010)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, 250, 0, -1810, 180)
    ChrClearFlags(0x000B, 0x0080)
    ChrSetPos(0x000B, 280, 0, -3490, 0)

    Jump('loc_5BC')

    def _loc_49F(): pass

    label('loc_49F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_4FB',
    )

    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, -28900, 0, 22980, 0)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetFlags(0x000A, 0x0010)
    ChrClearFlags(0x000B, 0x0080)
    ChrSetFlags(0x000B, 0x0010)
    ChrClearFlags(0x000E, 0x0080)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0012, 0x0080)
    ChrClearFlags(0x0013, 0x0080)
    ChrClearFlags(0x0014, 0x0080)

    Jump('loc_5BC')

    def _loc_4FB(): pass

    label('loc_4FB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 0, 0x430)),
            Expr.Return,
        ),
        'loc_588',
    )

    ChrClearFlags(0x0015, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0089, 0, 0x448)),
            Expr.Return,
        ),
        'loc_563',
    )

    TerminateThread(0x000B, 0xFF)
    TerminateThread(0x000C, 0xFF)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrSetFlags(0x000B, 0x0004)
    ChrSetFlags(0x000B, 0x0010)
    ChrSetChipByIndex(0x000B, 16)
    ChrSetSubChip(0x000B, 0)
    ChrSetFlags(0x000C, 0x0004)
    ChrSetFlags(0x000C, 0x0010)
    ChrSetPos(0x000C, -1800, 250, -1090, 270)
    ChrSetPos(0x000B, -3030, 250, 290, 180)

    Jump('loc_585')

    def _loc_563(): pass

    label('loc_563')

    ChrSetPos(0x000B, 3610, 0, 50080, 0)
    ChrSetPos(0x000C, 3610, 0, 50080, 0)

    def _loc_585(): pass

    label('loc_585')

    Jump('loc_5BC')

    def _loc_588(): pass

    label('loc_588')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 7, 0x42F)),
            Expr.Return,
        ),
        'loc_597',
    )

    ChrClearFlags(0x0008, 0x0080)

    Jump('loc_5BC')

    def _loc_597(): pass

    label('loc_597')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 6, 0x42E)),
            Expr.Return,
        ),
        'loc_5A1',
    )

    Jump('loc_5BC')

    def _loc_5A1(): pass

    label('loc_5A1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_5AB',
    )

    Jump('loc_5BC')

    def _loc_5AB(): pass

    label('loc_5AB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 6, 0x41E)),
            Expr.Return,
        ),
        'loc_5B5',
    )

    Jump('loc_5BC')

    def _loc_5B5(): pass

    label('loc_5B5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_5BC',
    )

    def _loc_5BC(): pass

    label('loc_5BC')

    Return()

# id: 0x0001 offset: 0x5BD
@scena.Code('func_01_5BD')
def func_01_5BD():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 4, 0x43C)),
            Expr.Ez,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 0, 0x430)),
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Or,
            Expr.Return,
        ),
        'loc_5DE',
    )

    OP_B1('t2521_y')

    Jump('loc_5E7')

    def _loc_5DE(): pass

    label('loc_5DE')

    OP_B1('t2521_n')

    def _loc_5E7(): pass

    label('loc_5E7')

    OP_64(0x01, 0x0001)
    OP_64(0x03, 0x0001)

    If(
        (
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x0020)"),
            Expr.Return,
        ),
        'loc_5FE',
    )

    OP_65(0x01, 0x0001)

    def _loc_5FE(): pass

    label('loc_5FE')

    If(
        (
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x0040)"),
            Expr.Return,
        ),
        'loc_612',
    )

    OP_64(0x01, 0x0001)
    ChrSetFlags(0x0016, 0x0080)

    def _loc_612(): pass

    label('loc_612')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0089, 0, 0x448)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_629',
    )

    OP_6F(0x0000, 0)
    OP_72(0x0000, 0x0010)

    Jump('loc_62D')

    def _loc_629(): pass

    label('loc_629')

    OP_64(0x02, 0x0001)

    def _loc_62D(): pass

    label('loc_62D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_66A',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x0020)"),
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x1000)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_66A',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x0200)"),
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x0400)"),
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x0800)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_666',
    )

    Jump('loc_66A')

    def _loc_666(): pass

    label('loc_666')

    OP_65(0x03, 0x0001)

    def _loc_66A(): pass

    label('loc_66A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_67F',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x4B),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_67F(): pass

    label('loc_67F')

    Return()

# id: 0x0002 offset: 0x680
@scena.Code('func_02_680')
def func_02_680():
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
        'loc_6A5',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_7E7')

    def _loc_6A5(): pass

    label('loc_6A5')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6BE',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_7E7')

    def _loc_6BE(): pass

    label('loc_6BE')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6D7',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_7E7')

    def _loc_6D7(): pass

    label('loc_6D7')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6F0',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_7E7')

    def _loc_6F0(): pass

    label('loc_6F0')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_709',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_7E7')

    def _loc_709(): pass

    label('loc_709')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_722',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_7E7')

    def _loc_722(): pass

    label('loc_722')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_73B',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_7E7')

    def _loc_73B(): pass

    label('loc_73B')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_754',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_7E7')

    def _loc_754(): pass

    label('loc_754')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_76D',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_7E7')

    def _loc_76D(): pass

    label('loc_76D')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_786',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_7E7')

    def _loc_786(): pass

    label('loc_786')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_79F',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_7E7')

    def _loc_79F(): pass

    label('loc_79F')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7B8',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_7E7')

    def _loc_7B8(): pass

    label('loc_7B8')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7D1',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_7E7')

    def _loc_7D1(): pass

    label('loc_7D1')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7E7',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_7E7(): pass

    label('loc_7E7')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_7FC',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_7E7')

    def _loc_7FC(): pass

    label('loc_7FC')

    Return()

# id: 0x0003 offset: 0x7FD
@scena.Code('func_03_7FD')
def func_03_7FD():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_820',
    )

    OP_8D(0x00FE, -590, -1050, 1740, -4800, 3000)

    Jump('func_03_7FD')

    def _loc_820(): pass

    label('loc_820')

    Return()

# id: 0x0004 offset: 0x821
@scena.Code('func_04_821')
def func_04_821():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_869',
    )

    ChrTalk(
        0x00FE,
        (
            '呼啊啊啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊，终于完了。\n',
            '稍微休息一下就回去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A55')

    def _loc_869(): pass

    label('loc_869')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_926',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8E0',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '我一点也不想\n',
            '参加学园祭。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '稍微偷下懒，\n',
            '混过这一天算了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为什么我要参加这种活动……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_923')

    def _loc_8E0(): pass

    label('loc_8E0')

    ChrTalk(
        0x00FE,
        (
            '稍微偷下懒，\n',
            '混过这一天算了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为什么我要参加这种活动……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_923(): pass

    label('loc_923')

    Jump('loc_A55')

    def _loc_926(): pass

    label('loc_926')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 0, 0x430)),
            Expr.Return,
        ),
        'loc_A04',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_9AF',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '呼啊～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎呀哎呀～～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果在教室里无所事事，\n',
            '那个多事的学生会长又会啰嗦了。\n',
            '还是在这里打发时间吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A01')

    def _loc_9AF(): pass

    label('loc_9AF')

    ChrTalk(
        0x00FE,
        (
            '如果在教室里无所事事，\n',
            '那个多事的学生会长又会啰嗦了。\n',
            '还是在这里打发时间吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A01(): pass

    label('loc_A01')

    Jump('loc_A55')

    def _loc_A04(): pass

    label('loc_A04')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 7, 0x42F)),
            Expr.Return,
        ),
        'loc_A55',
    )

    ChrTalk(
        0x00FE,
        (
            '学园祭的准备工作\n',
            '真是麻烦死了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '让想干的家伙\n',
            '去干个够不就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A55(): pass

    label('loc_A55')

    TalkEnd(0x0008)

    Return()

# id: 0x0005 offset: 0xA59
@scena.Code('func_05_A59')
def func_05_A59():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_B81',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B36',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '为什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有那样杰出的求婚者，\n',
            '而且还是两位……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x0009, 0x0101, 800)

    ChrTalk(
        0x00FE,
        (
            '哇，你们什么时候来的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '不、不要误会了，\n',
            '刚才的是舞台剧的台词。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x0009, 0x0010)

    Jump('loc_B7E')

    def _loc_B36(): pass

    label('loc_B36')

    ChrTalk(
        0x00FE,
        (
            '我可不想在\n',
            '演出的时候弄错台词，\n',
            '像个傻瓜一样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '咕噜咕噜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B7E(): pass

    label('loc_B7E')

    Jump('loc_BBB')

    def _loc_B81(): pass

    label('loc_B81')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_BBB',
    )

    ChrTalk(
        0x00FE,
        (
            '唔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们在干什么？\n',
            '不要妨碍我学习呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BBB(): pass

    label('loc_BBB')

    TalkEnd(0x0009)

    Return()

# id: 0x0006 offset: 0xBBF
@scena.Code('func_06_BBF')
def func_06_BBF():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_CEF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_CA3',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    ChrTurnDirection(0x00FE, 0x0105, 0)

    ChrTalk(
        0x00FE,
        (
            '#0510060388V#640F啊，科洛丝……\n',
            '孤儿院的孩子们都来了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060060389V#040F嗯，\n',
            '大家都来玩了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0510060390V#640F是吗，把讨厌的事忘掉，\n',
            '尽情地玩个够吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060060391V#040F是啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CEC')

    def _loc_CA3(): pass

    label('loc_CA3')

    ChrTalk(
        0x00FE,
        (
            '#0510060392V#640F让孤儿院的孩子们\n',
            '把讨厌的事忘掉，\n',
            '尽情地玩个够吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_CEC(): pass

    label('loc_CEC')

    Jump('loc_D9D')

    def _loc_CEF(): pass

    label('loc_CEF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_D9D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_D65',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '#0510060104V#640F嗯，完成了。\n',
            '估计就这些东西了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510060105V只要有这些东西，一定……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x000A, 0x0010)

    Jump('loc_D9D')

    def _loc_D65(): pass

    label('loc_D65')

    ChrTalk(
        0x00FE,
        (
            '#0510060106V#640F怎么了，你们三个。\n',
            '玩得还愉快吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D9D(): pass

    label('loc_D9D')

    TalkEnd(0x000A)

    Return()

# id: 0x0007 offset: 0xDA1
@scena.Code('func_07_DA1')
def func_07_DA1():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_E93',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_E30',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '#0520060393V#733F咦，科洛丝和艾丝蒂尔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520060394V#730F放着两个可爱的女孩子不管，\n',
            '约修亚那小子跑到哪里去了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E90')

    def _loc_E30(): pass

    label('loc_E30')

    ChrTalk(
        0x00FE,
        (
            '#0520060395V#730F演出一开始，\n',
            '这座建筑物就要锁起来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520060396V这也是为了保证安全啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E90(): pass

    label('loc_E90')

    Jump('loc_135B')

    def _loc_E93(): pass

    label('loc_E93')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_EF5',
    )

    ChrTalk(
        0x00FE,
        (
            '#0520060107V#730F文件方面准备好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520060108V接着只要取得校长的同意就行了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_135B')

    def _loc_EF5(): pass

    label('loc_EF5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0089, 2, 0x44A)),
            Expr.Return,
        ),
        'loc_1350',
    )

    ChrTalk(
        0x00FE,
        (
            '#0520051495V#730F怎么了？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520051496V现在就点菜吧？',
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
            TXT(0x00, '【现在点菜】\n'),
            TXT(0x01, '【还有点事】\n'),
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

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000001, 'loc_FA2'),
        (0x00000000, 'loc_FD7'),
        (-1, 'loc_134D'),
    )

    def _loc_FA2(): pass

    label('loc_FA2')

    ChrTalk(
        0x00FE,
        (
            '#0520051497V#730F好吧，\n',
            '事情办完了赶快回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_134D')

    def _loc_FD7(): pass

    label('loc_FD7')

    EventBegin(0x00)
    Fade(1000)
    CameraMove(-1640, 0, -1220, 0)
    ChrSetPos(0x0101, -1160, 0, -1960, 315)
    ChrSetPos(0x0105, -1530, 0, -3000, 0)
    ChrSetPos(0x013B, -2250, 0, -2380, 0)
    ChrSetSubChip(0x000C, 1)
    OP_0D()

    ChrTalk(
        0x013B,
        (
            '#0510051498V#645F#3P啊～肚子咕咕叫了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510051499V忙着搞舞台剧的最后加工，\n',
            '今天在学院里跑了整整一天……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060051500V#048F呵呵……\n',
            '不过也就到今天为止了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x013B,
        (
            '#0510051501V#644F#3P是啊，真的呢。\n',
            '得重新调整节奏了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510051502V而且又有新的事情要做……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0520051503V#733F新的事情？\n',
            '是什么事啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x013B,
        (
            '#0510051504V#640F#3P嗯，一会儿再告诉你。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510051505V#641F那么，为了预祝学园祭的成功，\n',
            '今晚就好好地狂欢一番吧！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510051506V艾丝蒂尔、约修亚。\n',
            '明天就拜托你们了哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x013B, 0)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010051507V#006F嗯，看我们的吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0020051508V#019F必定全力以赴演出。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000005DC)
    FadeOut(2000, 0, -1)
    OP_0D()
    OP_21()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '当晚，艾丝蒂尔他们\n',
            '在食堂度过了开心热闹的一晚……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '最后，为了预祝舞台剧的成功，大家一起用饮料干杯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '回宿舍之后，\n',
            '艾丝蒂尔他们为了明天的活动都早早就寝了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '学园祭当天的早晨——',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetScenaFlags(ScenaFlag(0x0086, 1, 0x431))
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    FormationDelMember(0x3A, 0xFF)
    NewScene('ED6_DT01/T2523._SN', 113, 0, 0)
    IdleLoop()

    Jump('loc_134D')

    def _loc_134D(): pass

    label('loc_134D')

    Jump('loc_135B')

    def _loc_1350(): pass

    label('loc_1350')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0089, 0, 0x448)),
            Expr.Return,
        ),
        'loc_135B',
    )

    Call(0, 0x0009)

    def _loc_135B(): pass

    label('loc_135B')

    TalkEnd(0x000B)

    Return()

# id: 0x0008 offset: 0x135F
@scena.Code('func_08_135F')
def func_08_135F():
    TalkBegin(0x000C)
    ChrClearFlags(0x000C, 0x0010)
    ChrTurnDirection(0x000C, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xC, 0x4),
            (Expr.PushLong, 0x5A),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_1384',
    )

    ChrSetSubChip(0x000C, 2)

    Jump('loc_13B5')

    def _loc_1384(): pass

    label('loc_1384')

    If(
        (
            (Expr.GetChrWork, 0xC, 0x4),
            (Expr.PushLong, 0xE1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_139A',
    )

    ChrSetSubChip(0x000C, 1)

    Jump('loc_13B5')

    def _loc_139A(): pass

    label('loc_139A')

    If(
        (
            (Expr.GetChrWork, 0xC, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_13B0',
    )

    ChrSetSubChip(0x000C, 0)

    Jump('loc_13B5')

    def _loc_13B0(): pass

    label('loc_13B0')

    ChrSetSubChip(0x000C, 2)

    def _loc_13B5(): pass

    label('loc_13B5')

    ChrSetDirection(0x000C, 270, 0)
    ChrSetFlags(0x000C, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0089, 2, 0x44A)),
            Expr.Return,
        ),
        'loc_1820',
    )

    ChrTalk(
        0x000C,
        (
            '#0020051478V#010F现在点菜吗？',
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
            TXT(0x00, '【现在点菜】\n'),
            TXT(0x01, '【还有点事】\n'),
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

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000001, 'loc_1456'),
        (0x00000000, 'loc_1498'),
        (-1, 'loc_181D'),
    )

    def _loc_1456(): pass

    label('loc_1456')

    ChrTalk(
        0x000C,
        (
            '#0020051479V#010F我们占着座位，\n',
            '办完事情就赶快回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x000C, 0)

    Jump('loc_181D')

    def _loc_1498(): pass

    label('loc_1498')

    EventBegin(0x00)
    Fade(1000)
    CameraMove(-1640, 0, -1220, 0)
    ChrSetPos(0x0101, -1160, 0, -1960, 315)
    ChrSetPos(0x0105, -1530, 0, -3000, 0)
    ChrSetPos(0x013B, -2250, 0, -2380, 0)
    ChrSetSubChip(0x000C, 1)
    OP_0D()

    ChrTalk(
        0x013B,
        (
            '#0510051480V#645F#3P啊～肚子咕咕叫了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510051481V忙着搞舞台剧的最后加工，\n',
            '今天在学院里跑了整整一天……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060051482V#048F呵呵……\n',
            '不过也就到今天为止了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x013B,
        (
            '#0510051483V#644F#3P是啊，真的呢。\n',
            '得重新调整节奏了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510051484V而且又有新的事情要做……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0520051485V#733F新的事情？\n',
            '是什么事啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x013B,
        (
            '#0510051486V#640F#3P嗯，一会儿再告诉你。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510051487V#641F那么，为了预祝学园祭的成功，\n',
            '今晚就好好地狂欢一番吧！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510051488V艾丝蒂尔、约修亚。\n',
            '明天就拜托你们了哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x013B, 0)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010051489V#006F嗯，看我们的吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0020051490V#019F必定全力以赴演出。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000005DC)
    FadeOut(2000, 0, -1)
    OP_0D()
    OP_21()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '当晚，艾丝蒂尔他们\n',
            '在食堂度过了开心热闹的一晚……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '最后，为了预祝舞台剧的成功，大家一起用饮料干杯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '回宿舍之后，\n',
            '艾丝蒂尔他们为了明天的活动都早早就寝了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '学园祭当天的早晨——',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Sleep(500)

    MapSetFlags(0x00100000)
    PlaySE(13, 0x00, 0x64)
    SetScenaFlags(ScenaFlag(0x0086, 1, 0x431))
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    FormationDelMember(0x3A, 0xFF)
    NewScene('ED6_DT01/T2523._SN', 113, 0, 0)
    IdleLoop()

    Jump('loc_181D')

    def _loc_181D(): pass

    label('loc_181D')

    Jump('loc_182B')

    def _loc_1820(): pass

    label('loc_1820')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0089, 0, 0x448)),
            Expr.Return,
        ),
        'loc_182B',
    )

    Call(0, 0x0009)

    def _loc_182B(): pass

    label('loc_182B')

    TalkEnd(0x000C)

    Return()

# id: 0x0009 offset: 0x182F
@scena.Code('func_09_182F')
def func_09_182F():
    EventBegin(0x00)
    Fade(1000)
    CameraMove(-1640, 0, -1220, 0)
    ChrSetPos(0x0101, -1160, 0, -1960, 315)
    ChrSetPos(0x0105, -1530, 0, -3000, 0)
    ChrSetPos(0x013B, -2250, 0, -2380, 0)
    ChrSetSubChip(0x000C, 1)
    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0089, 1, 0x449)),
            Expr.Return,
        ),
        'loc_18B8',
    )

    ChrTalk(
        0x0101,
        (
            '#0010051456V#503F嗯……\n',
            '我们把她带来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_18EA')

    def _loc_18B8(): pass

    label('loc_18B8')

    ChrTalk(
        0x0101,
        (
            '#0010051457V#001F呀嗬～⊙\n',
            '我们把她带来了哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_18EA(): pass

    label('loc_18EA')

    ChrTalk(
        0x013B,
        (
            '#0510051458V#641F#3P呵呵～大家辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0020051459V#010F辛苦了，乔儿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0520051460V#730F哟，已经等你好久了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520051461V我们快点菜吧。',
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
            TXT(0x00, '【现在点菜】\n'),
            TXT(0x01, '【还有点事】\n'),
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

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000001, 'loc_19ED'),
        (0x00000000, 'loc_1A34'),
        (-1, 'loc_1D6E'),
    )

    def _loc_19ED(): pass

    label('loc_19ED')

    ChrTalk(
        0x000C,
        (
            '#0020051462V#010F我们占着座位，\n',
            '办完事情就赶快回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x000C, 0)
    SetScenaFlags(ScenaFlag(0x0089, 2, 0x44A))
    EventEnd(0x00)

    Jump('loc_1D6E')

    def _loc_1A34(): pass

    label('loc_1A34')

    ChrTalk(
        0x013B,
        (
            '#0510051463V#645F#3P啊～肚子咕咕叫了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510051464V忙着搞舞台剧的最后加工，\n',
            '今天在学院里跑了整整一天……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060051465V#048F呵呵……\n',
            '不过也就到今天为止了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x013B,
        (
            '#0510051466V#644F#3P是啊，真的呢。\n',
            '得重新调整节奏了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510051467V而且又有新的事情要做……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0520051468V#733F新的事情？\n',
            '是什么事啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x013B,
        (
            '#0510051469V#640F#3P嗯，一会儿再告诉你。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510051470V#641F那么，为了预祝学园祭的成功，\n',
            '今晚就好好地狂欢一番吧！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510051471V艾丝蒂尔、约修亚。\n',
            '明天就拜托你们了哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x013B, 0)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010051472V#006F嗯，看我们的吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0020051473V#019F必定全力以赴演出。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000005DC)
    FadeOut(2000, 0, -1)
    OP_0D()
    OP_21()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '当晚，艾丝蒂尔他们\n',
            '在食堂度过了开心热闹的一晚……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '最后，为了预祝舞台剧的成功，大家一起用饮料干杯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '回宿舍之后，\n',
            '艾丝蒂尔他们为了明天的活动都早早就寝了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '学园祭当天的早晨——',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Sleep(500)

    MapSetFlags(0x00100000)
    PlaySE(13, 0x00, 0x64)
    SetScenaFlags(ScenaFlag(0x0086, 1, 0x431))
    OP_28(0x003D, 0x01, 0x0800)
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    FormationDelMember(0x3A, 0xFF)
    NewScene('ED6_DT01/T2523._SN', 113, 0, 0)
    IdleLoop()

    Jump('loc_1D6E')

    def _loc_1D6E(): pass

    label('loc_1D6E')

    Return()

# id: 0x000A offset: 0x1D6F
@scena.Code('func_0A_1D6F')
def func_0A_1D6F():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0089, 1, 0x449)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2316',
    )

    SetScenaFlags(ScenaFlag(0x0089, 1, 0x449))
    EventBegin(0x00)

    NpcTalk(
        0x000B,
        '汉斯的声音',
        (
            '#0520051407V#2P……碧欧拉老师真是个美人啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520051408V就算不怎么特意打扮，\n',
            '也是十分漂亮呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520051409V不过我对米丽亚老师\n',
            '那冰冷眼镜后的美貌\n',
            '也是心跳不止啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520051410V眼镜这东西果然\n',
            '还是和成熟的女性最相配。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000C,
        '约修亚的声音',
        (
            '#0020051411V#1P唔，我对你的说法\n',
            '没什么反对意见……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020051412V不过这么说来，\n',
            '你觉得乔儿怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000B,
        '汉斯的声音',
        (
            '#0520051413V#2P并、并不是\n',
            '带眼镜就一定会漂亮的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520051414V还必须要有大人的魅力才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000C,
        '约修亚的声音',
        (
            '#0020051415V#1P哈哈，你有点紧张哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000B,
        '汉斯的声音',
        (
            '#0520051416V#2P才没这回事呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x0105, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1200)

    OP_63(0x0101)
    OP_63(0x0105)

    ChrTalk(
        0x0101,
        (
            '#0010051417V#007F（说是去占座，\n',
            '　竟然在聊这种事……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010051418V（真是拿男生没办法啊。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060051419V#045F（就连约修亚\n',
            '　也在聊这种事……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060051420V（真是很意外呢。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000B,
        '汉斯的声音',
        (
            '#0520051421V#2P……约修亚你呢，\n',
            '和艾丝蒂尔发展到什么地步了？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520051422V难道说……\n',
            '已经到了『那个』的程度吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000C,
        '约修亚的声音',
        (
            '#0020051423V#1P不好意思，\n',
            '我们不是你想象的那样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020051424V该怎么说好呢……\n',
            '总之不是那种关系啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000B,
        '汉斯的声音',
        (
            '#0520051425V#2P哎……是吗。\n',
            '我觉得你们是不错的一对呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520051426V要不然，\n',
            '你就大胆地去追科洛丝怎么样？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520051427V你们练习的时候很合拍，\n',
            '我想一定很般配的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000C,
        '约修亚的声音',
        (
            '#0020051428V#1P你瞎说什么呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x0105, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1200)

    OP_63(0x0101)
    OP_63(0x0105)
    ChrTurnDirection(0x0101, 0x0105, 400)

    ChrTalk(
        0x0101,
        (
            '#0010051429V#503F（……我们还是去校长室吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0101, 400)

    ChrTalk(
        0x0105,
        (
            '#0060051430V#542F（是，是啊。\n',
            '　还是去找乔儿吧……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x01)

    Jump('loc_23A5')

    def _loc_2316(): pass

    label('loc_2316')

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2365',
    )

    ChrTalk(
        0x0101,
        (
            '#0010051431V#503F（还、还是去校长室\n',
            '　叫乔儿去吃饭吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23A3')

    def _loc_2365(): pass

    label('loc_2365')

    ChrTalk(
        0x0105,
        (
            '#0060051432V#540F（啊，这个……\n',
            '　还是不要打扰他们了。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_23A3(): pass

    label('loc_23A3')

    EventEnd(0x01)

    def _loc_23A5(): pass

    label('loc_23A5')

    Return()

# id: 0x000B offset: 0x23A6
@scena.Code('func_0B_23A6')
def func_0B_23A6():
    Call(0, 0x000C)

    Return()

# id: 0x000C offset: 0x23AB
@scena.Code('func_0C_23AB')
def func_0C_23AB():
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
            TXT(0x02, '欢迎品尝「学院午餐」500米拉\n'),
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
        'loc_2425',
    )

    FadeIn(300, 0)
    OP_0D()
    OP_A9(0x30)
    OP_56(0x00)
    TalkEnd(0x000D)

    Return()

    def _loc_2425(): pass

    label('loc_2425')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_251F',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x12),
            (Expr.PushLong, 0x1F4),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_24EA',
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
            '学院午餐',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetStatus(0x0000, 0xFD, 700)
    ChrSetStatus(0x0001, 0xFD, 700)
    ChrSetStatus(0x0002, 0xFD, 700)
    ChrSetStatus(0x0003, 0xFD, 700)
    ChrSetStatus(0x0004, 0xFD, 700)
    ChrSetStatus(0x0005, 0xFD, 700)
    ChrSetStatus(0x0006, 0xFD, 700)
    ChrSetStatus(0x0007, 0xFD, 700)

    If(
        (
            (Expr.Eval, "OP_40(0x020D)"),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_24DC',
    )

    If(
        (
            (Expr.Eval, "OP_AC(0x0009)"),
            Expr.Return,
        ),
        'loc_24B6',
    )

    Jump('loc_24DC')

    def _loc_24B6(): pass

    label('loc_24B6')

    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            TxtCtl.ShowAll,
            (TxtCtl.SetColor, 0x0),
            '学会了',
            (TxtCtl.SetColor, 0x2),
            '学院午餐',
            (TxtCtl.SetColor, 0x0),
            '的做法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_24DC(): pass

    label('loc_24DC')

    OP_56(0x00)
    FadeIn(1000, 0)

    Jump('loc_2510')

    def _loc_24EA(): pass

    label('loc_24EA')

    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            '没有足够的米拉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeIn(300, 0)
    def _loc_2510(): pass

    label('loc_2510')

    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x000D)

    Return()

    def _loc_251F(): pass

    label('loc_251F')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2539',
    )

    FadeIn(300, 0)
    TalkEnd(0x000D)

    Return()

    def _loc_2539(): pass

    label('loc_2539')

    FadeIn(300, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_256D',
    )

    ChrTalk(
        0x000D,
        (
            '欢迎光临。\n',
            '想要点些什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2945')

    def _loc_256D(): pass

    label('loc_256D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            Expr.Return,
        ),
        'loc_265B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_262B',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x000D,
        (
            '舞台剧我也看了哦。\n',
            '你们真是非常努力啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '辛苦你们了，\n',
            '这是一点小意思，\n',
            '就当是我看演出的门票吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '不用客气，吃吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x008A, 2, 0x452)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2628',
    )

    SetScenaFlags(ScenaFlag(0x008A, 2, 0x452))
    AddItem(0x0384, 1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '荧光菇',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_2628(): pass

    label('loc_2628')

    Jump('loc_2658')

    def _loc_262B(): pass

    label('loc_262B')

    ChrTalk(
        0x000D,
        (
            '舞台剧我也看了哦。\n',
            '你们真是非常努力啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_2658(): pass

    label('loc_2658')

    Jump('loc_2945')

    def _loc_265B(): pass

    label('loc_265B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_26B0',
    )

    ChrTalk(
        0x000D,
        (
            '你们要参加演出吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '阿姨我也要去看。\n',
            '真是很期待呀，你们要加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2945')

    def _loc_26B0(): pass

    label('loc_26B0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_2708',
    )

    ChrTalk(
        0x000D,
        (
            '今天这里作为\n',
            '休息的场所对公众开放。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '不过和平时一样，\n',
            '也可以点菜哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2945')

    def _loc_2708(): pass

    label('loc_2708')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 0, 0x430)),
            Expr.Return,
        ),
        'loc_2776',
    )

    ChrTalk(
        0x000D,
        (
            '一直忙于学园祭的准备，\n',
            '都还没吃饭吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '像你们这样的孩子\n',
            '必须要好好摄取营养才能健康成长啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2945')

    def _loc_2776(): pass

    label('loc_2776')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 7, 0x42F)),
            Expr.Return,
        ),
        'loc_27DC',
    )

    ChrTalk(
        0x000D,
        (
            '学园祭的准备，\n',
            '还顺利吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '在准备期间我特别准备了丰盛的饭菜，\n',
            '你们随时都能来用餐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2945')

    def _loc_27DC(): pass

    label('loc_27DC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 6, 0x42E)),
            Expr.Return,
        ),
        'loc_2828',
    )

    ChrTalk(
        0x000D,
        (
            '啊～\n',
            '马上就要下课了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '同学们要来吃饭了，\n',
            '必须加把劲呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2945')

    def _loc_2828(): pass

    label('loc_2828')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_2884',
    )

    ChrTalk(
        0x000D,
        (
            '呀，是科洛丝啊。\n',
            '现在应该还在上课啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '不好意思，\n',
            '现在这边还在准备中。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2945')

    def _loc_2884(): pass

    label('loc_2884')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 6, 0x41E)),
            Expr.Return,
        ),
        'loc_28EE',
    )

    ChrTalk(
        0x000D,
        (
            '啊，\n',
            '你们两个是想来入学的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '就算不是学生也能来这里吃饭哦。\n',
            '作为参观纪念想吃些什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2945')

    def _loc_28EE(): pass

    label('loc_28EE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_2945',
    )

    ChrTalk(
        0x000D,
        (
            '这个学生食堂\n',
            '假日里也会开放的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '如果饿了，\n',
            '就不要客气，尽管点菜吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2945(): pass

    label('loc_2945')

    TalkEnd(0x000D)

    Return()

# id: 0x000D offset: 0x2949
@scena.Code('func_0D_2949')
def func_0D_2949():
    TalkBegin(0x000E)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2A8A',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x0101,
        (
            '#0010060173V#501F（啊，这个人……\n',
            '　我好像在哪儿见到过。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020060174V#010F（她是那个在空贼基地里\n',
            '　和理查德上校一起出现的女性军官。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0610060175V#181F呵呵，\n',
            '上校他很久以前就想来\n',
            '王立学院这里拜访了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610060176V可实在是抽不出空……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610060177V相信不久之后\n',
            '他就有空好好拜访这里了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2B28')

    def _loc_2A8A(): pass

    label('loc_2A8A')

    ChrTalk(
        0x00FE,
        (
            '#0610060178V#181F呵呵，\n',
            '上校他很久以前就想来\n',
            '王立学院这里拜访了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610060179V可实在是抽不出空……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610060180V相信不久之后\n',
            '他就有空好好拜访这里了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2B28(): pass

    label('loc_2B28')

    TalkEnd(0x000E)

    Return()

# id: 0x000E offset: 0x2B2C
@scena.Code('func_0E_2B2C')
def func_0E_2B2C():
    TalkBegin(0x000F)

    ChrTalk(
        0x00FE,
        (
            '我和妻子移居到\n',
            '玛诺利亚村好几年了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可王立学院还是第一次来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000F)

    Return()

# id: 0x000F offset: 0x2B7C
@scena.Code('func_0F_2B7C')
def func_0F_2B7C():
    TalkBegin(0x0010)

    ChrTalk(
        0x00FE,
        (
            '真让人吃惊，\n',
            '学园祭竟然这么热闹……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0010)

    Return()

# id: 0x0010 offset: 0x2BAC
@scena.Code('func_10_2BAC')
def func_10_2BAC():
    TalkBegin(0x0011)

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，卢希娅我啊，\n',
            '是和克拉姆他们一起来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0011)

    Return()

# id: 0x0011 offset: 0x2BE4
@scena.Code('func_11_2BE4')
def func_11_2BE4():
    TalkBegin(0x0012)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x008B, 1, 0x459)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3218',
    )

    EventBegin(0x00)
    Fade(1000)
    ChrSetPos(0x0101, 4710, 0, 1390, 0)
    ChrSetPos(0x0105, 3350, 0, 1120, 0)
    ChrSetPos(0x0102, 3900, 0, 320, 0)
    CameraMove(4270, 0, 2180, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    ChrSetDirection(0x00FE, 180, 0)
    OP_4A(0x00FE, 255)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x008B, 1, 0x459))

    ChrTalk(
        0x0101,
        (
            '#0010060183V#004F…………咦？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010060184V这不是亚鲁瓦教授吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0150060185V#130F哎呀，\n',
            '原来是艾丝蒂尔和约修亚啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150060186V我们真是有缘啊。\n',
            '看起来你们俩还是那么充满干劲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020060187V#010F教授也收到了\n',
            '参加学园祭的邀请吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0150060188V#130F不，很遗憾并不是这样。\n',
            '我来学院是为了其他事情的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150060189V我来卢安是为了\n',
            '考察这里的『绀碧之塔』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150060190V顺便来王立学院\n',
            '看看有没有相关的研究资料。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010060191V#506F啊～还是那么热衷于工作呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0150060192V#130F哈哈，在没钱的情况下，\n',
            '支撑着自己的学术研究的\n',
            '就只有这股热情和体力了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150060193V#132F说起来，这个学院的全部课程\n',
            '似乎分为几大学科。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150060194V请问有没有举办什么学术展览呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060060195V#040F有呢，不过三个学科之中\n',
            '只有社会系办了展览……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060060196V展览里面发表的都是\n',
            '学生们的自主研究的作品。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0150060197V#130F哦哦，真是不错啊。\n',
            '让我想起自己的学生时代来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150060198V那请问学术展览\n',
            '在哪里可以看到呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010060199V#505F这个嘛，\n',
            '教授还是第一次来学院吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010060200V嗯……该怎么跟你说呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060060201V#045F是啊。\n',
            '这学院的建筑太多了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060060202V#040F如果可以的话，不如我们带您去吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0150060203V#131F这样的话当然是最好不过……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150060204V可是，大家都在高高兴兴地参加学园祭，\n',
            '要麻烦你们实在是太不好意思了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010060205V#001F没事没事。\n',
            '费不了什么事的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0150060206V#130F这样啊……\n',
            '那就麻烦你们在方便的时候\n',
            '带我到展览室一趟就行了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150060207V在那之前，\n',
            '我就在这学生食堂等着好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x00FE, 0, 400)
    OP_4B(0x00FE, 255)
    EventEnd(0x00)

    Jump('loc_3333')

    def _loc_3218(): pass

    label('loc_3218')

    ChrTalk(
        0x00FE,
        (
            '#0150060208V#130F呵呵，话说回来，\n',
            '在这时代做学生真是好啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150060209V每天用那么少钱就可以吃饱睡饱，\n',
            '真是羡慕死人了。',
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
            TXT(0x00, '【继续参观学园祭】\n'),
            TXT(0x01, '【带教授到社会系教室参观】\n'),
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

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_3316'),
        (0x00000001, 'loc_3319'),
        (-1, 'loc_3333'),
    )

    def _loc_3316(): pass

    label('loc_3316')

    Jump('loc_3333')

    def _loc_3319(): pass

    label('loc_3319')

    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T2520._SN', 123, 0, 0)
    IdleLoop()

    Jump('loc_3333')

    def _loc_3333(): pass

    label('loc_3333')

    TalkEnd(0x0012)

    Return()

# id: 0x0012 offset: 0x3337
@scena.Code('func_12_3337')
def func_12_3337():
    TalkBegin(0x0013)

    ChrTalk(
        0x00FE,
        (
            '哎，\n',
            '最近的学校真是好先进啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说起上学，\n',
            '我只读过主日学校呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0013)

    Return()

# id: 0x0013 offset: 0x3386
@scena.Code('func_13_3386')
def func_13_3386():
    TalkBegin(0x0014)

    ChrTalk(
        0x00FE,
        (
            '在旅行时听说了王立学院，\n',
            '所以我们就想来看看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0014)

    Return()

# id: 0x0014 offset: 0x33C0
@scena.Code('func_14_33C0')
def func_14_33C0():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '　　　　学生会办公室　　　　\n',
            '※谢绝外来人员进入。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0015 offset: 0x3424
@scena.Code('func_15_3424')
def func_15_3424():
    OP_13(0x0071)

    Return()

# id: 0x0016 offset: 0x3428
@scena.Code('func_16_3428')
def func_16_3428():
    OP_13(0x0072)

    Return()

# id: 0x0017 offset: 0x342C
@scena.Code('func_17_342C')
def func_17_342C():
    OP_13(0x0075)

    Return()

# id: 0x0018 offset: 0x3430
@scena.Code('func_18_3430')
def func_18_3430():
    OP_13(0x0070)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
