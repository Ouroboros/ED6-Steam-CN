import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T2511_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2511   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'T2511.x'
    header.mapIndex       = 1
    header.bgm            = 14
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
        ('ED6_DT07/CH02390._CH', 'ED6_DT07/CH02390P._CP'),
        ('ED6_DT07/CH02550._CH', 'ED6_DT07/CH02550P._CP'),
        ('ED6_DT07/CH01080._CH', 'ED6_DT07/CH01080P._CP'),
        ('ED6_DT07/CH01090._CH', 'ED6_DT07/CH01090P._CP'),
        ('ED6_DT07/CH01370._CH', 'ED6_DT07/CH01370P._CP'),
        ('ED6_DT07/CH01580._CH', 'ED6_DT07/CH01580P._CP'),
        ('ED6_DT07/CH01130._CH', 'ED6_DT07/CH01130P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH00003._CH', 'ED6_DT07/CH00003P._CP'),
        ('ED6_DT07/CH00013._CH', 'ED6_DT07/CH00013P._CP'),
        ('ED6_DT07/CH00043._CH', 'ED6_DT07/CH00043P._CP'),
        ('ED6_DT07/CH01083._CH', 'ED6_DT07/CH01083P._CP'),
        ('ED6_DT07/CH01373._CH', 'ED6_DT07/CH01373P._CP'),
        ('ED6_DT06/CH20021._CH', 'ED6_DT06/CH20021P._CP'),
    ]

# id: 0x10001 offset: 0x11A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '乔儿',
            x                   = 30800,
            z                   = 0,
            y                   = 55110,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '汉斯',
            x                   = 29460,
            z                   = 0,
            y                   = 53800,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '米克',
            x                   = -3600,
            z                   = 0,
            y                   = -6100,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            name                = '帕布尔',
            x                   = -31590,
            z                   = 0,
            y                   = 58850,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '黛拉',
            x                   = 4100,
            z                   = 0,
            y                   = -4000,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '罗伊斯',
            x                   = -29000,
            z                   = 0,
            y                   = 53100,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '巴托姆',
            x                   = -28800,
            z                   = 0,
            y                   = 27800,
            direction           = 90,
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
            name                = '芙拉瑟',
            x                   = 27700,
            z                   = 0,
            y                   = 23300,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '蕾娜',
            x                   = 29700,
            z                   = 0,
            y                   = 23300,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '德波拉',
            x                   = 3500,
            z                   = 0,
            y                   = 4500,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            name                = '巴克斯',
            x                   = -30000,
            z                   = 0,
            y                   = 56000,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            name                = 'CH22000',
            x                   = -31350,
            z                   = 330,
            y                   = 23900,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1835021,
            chipIndex           = 13,
            npcIndex            = 0x0166,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x29A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x29A
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
            dword_1C    = 0x00000013,
        ),
        ScenaEventData(
            x           = -2200,
            y           = 0,
            z           = 42000,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000014,
        ),
        ScenaEventData(
            x           = 2130,
            y           = 0,
            z           = 42010,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000015,
        ),
        ScenaEventData(
            x           = 2200,
            y           = 0,
            z           = 50000,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000016,
        ),
    )

# id: 0x10004 offset: 0x31A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -31560,
            triggerZ            = 0,
            triggerY            = 59430,
            triggerRange        = 800,
            actorX              = -31560,
            actorZ              = 1000,
            actorY              = 59430,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0012,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 3060,
            triggerZ            = 0,
            triggerY            = 2500,
            triggerRange        = 400,
            actorX              = 3500,
            actorZ              = 1500,
            actorY              = 4500,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000C,
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
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0011,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x386
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_400',
    )

    ChrClearFlags(0x000A, 0x0080)
    ChrSetChipByIndex(0x000A, 11)
    ChrSetPos(0x000A, -3680, 200, -5980, 270)
    ChrSetFlags(0x000A, 0x0004)
    ChrSetFlags(0x000A, 0x0010)
    TerminateThread(0x000A, 0xFF)
    ChrClearFlags(0x000B, 0x0080)
    ChrSetPos(0x000B, -32240, 0, 58170, 270)
    ChrClearFlags(0x000E, 0x0080)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, 28700, 0, 54820, 90)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0009, 30850, 0, 55030, 270)

    Jump('loc_4F2')

    def _loc_400(): pass

    label('loc_400')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            Expr.Return,
        ),
        'loc_40A',
    )

    Jump('loc_4F2')

    def _loc_40A(): pass

    label('loc_40A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_414',
    )

    Jump('loc_4F2')

    def _loc_414(): pass

    label('loc_414')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_434',
    )

    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, -31700, 0, 58360, 0)

    Jump('loc_4F2')

    def _loc_434(): pass

    label('loc_434')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 0, 0x430)),
            Expr.Return,
        ),
        'loc_443',
    )

    ChrClearFlags(0x000A, 0x0080)

    Jump('loc_4F2')

    def _loc_443(): pass

    label('loc_443')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 7, 0x42F)),
            Expr.Return,
        ),
        'loc_4CD',
    )

    ChrClearFlags(0x000A, 0x0080)
    ChrSetChipByIndex(0x000A, 11)
    ChrSetPos(0x000A, -3680, 200, -5980, 270)
    ChrSetFlags(0x000A, 0x0004)
    ChrSetFlags(0x000A, 0x0010)
    TerminateThread(0x000A, 0xFF)
    ChrClearFlags(0x000C, 0x0080)
    ChrSetChipByIndex(0x000C, 12)
    ChrSetPos(0x000C, 4050, 200, -4080, 180)
    ChrSetFlags(0x000C, 0x0004)
    ChrSetFlags(0x000C, 0x0010)
    TerminateThread(0x000C, 0xFF)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    ChrClearFlags(0x000F, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4B8',
    )

    ChrSetFlags(0x000F, 0x0010)

    def _loc_4B8(): pass

    label('loc_4B8')

    ChrClearFlags(0x0010, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4CA',
    )

    ChrSetFlags(0x0010, 0x0010)

    def _loc_4CA(): pass

    label('loc_4CA')

    Jump('loc_4F2')

    def _loc_4CD(): pass

    label('loc_4CD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 6, 0x42E)),
            Expr.Return,
        ),
        'loc_4D7',
    )

    Jump('loc_4F2')

    def _loc_4D7(): pass

    label('loc_4D7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_4E1',
    )

    Jump('loc_4F2')

    def _loc_4E1(): pass

    label('loc_4E1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 6, 0x41E)),
            Expr.Return,
        ),
        'loc_4EB',
    )

    Jump('loc_4F2')

    def _loc_4EB(): pass

    label('loc_4EB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_4F2',
    )

    def _loc_4F2(): pass

    label('loc_4F2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_509',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, func_10_33AF)
    OP_B1('t2511_n')

    def _loc_509(): pass

    label('loc_509')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x0000006C, 'loc_515'),
        (-1, 'loc_571'),
    )

    def _loc_515(): pass

    label('loc_515')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 0, 0x430)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 7, 0x42F)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_56E',
    )

    SetScenaFlags(ScenaFlag(0x0086, 0, 0x430))
    OP_28(0x001F, 0x04, 0x40)
    OP_28(0x001D, 0x04, 0x40)
    OP_28(0x0022, 0x04, 0x40)
    OP_28(0x0023, 0x04, 0x40)
    OP_28(0x0024, 0x04, 0x40)
    OP_28(0x001C, 0x04, 0x40)
    OP_28(0x0020, 0x04, 0x40)

    If(
        (
            (Expr.Eval, "OP_40(0x0334)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_555',
    )

    OP_28(0x0021, 0x04, 0x40)

    def _loc_555(): pass

    label('loc_555')

    If(
        (
            (Expr.Eval, "OP_29(0x001E, 0x00, 0x04)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_565',
    )

    OP_28(0x001E, 0x04, 0x40)

    def _loc_565(): pass

    label('loc_565')

    OP_28(0x0026, 0x04, 0x40)
    Event(0, func_0F_1DB9)

    def _loc_56E(): pass

    label('loc_56E')

    Jump('loc_571')

    def _loc_571(): pass

    label('loc_571')

    Return()

# id: 0x0001 offset: 0x572
@scena.Code('func_01_572')
def func_01_572():
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
        'loc_593',
    )

    OP_B1('t2511_y')

    Jump('loc_59C')

    def _loc_593(): pass

    label('loc_593')

    OP_B1('t2511_n')

    def _loc_59C(): pass

    label('loc_59C')

    OP_64(0x00, 0x0001)
    OP_64(0x02, 0x0001)

    If(
        (
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x0020)"),
            Expr.Return,
        ),
        'loc_5B3',
    )

    OP_65(0x02, 0x0001)

    def _loc_5B3(): pass

    label('loc_5B3')

    If(
        (
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x0040)"),
            Expr.Return,
        ),
        'loc_5C7',
    )

    OP_64(0x02, 0x0001)
    ChrSetFlags(0x0013, 0x0080)

    def _loc_5C7(): pass

    label('loc_5C7')

    If(
        (
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x0020)"),
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x1000)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5F1',
    )

    If(
        (
            (Expr.Eval, "OP_40(0x033D)"),
            (Expr.Eval, "OP_40(0x033E)"),
            Expr.Or,
            (Expr.Eval, "OP_40(0x033F)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_5F1',
    )

    OP_65(0x00, 0x0001)

    def _loc_5F1(): pass

    label('loc_5F1')

    Return()

# id: 0x0002 offset: 0x5F2
@scena.Code('func_02_5F2')
def func_02_5F2():
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
        'loc_617',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_759')

    def _loc_617(): pass

    label('loc_617')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_630',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_759')

    def _loc_630(): pass

    label('loc_630')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_649',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_759')

    def _loc_649(): pass

    label('loc_649')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_662',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_759')

    def _loc_662(): pass

    label('loc_662')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_67B',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_759')

    def _loc_67B(): pass

    label('loc_67B')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_694',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_759')

    def _loc_694(): pass

    label('loc_694')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6AD',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_759')

    def _loc_6AD(): pass

    label('loc_6AD')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6C6',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_759')

    def _loc_6C6(): pass

    label('loc_6C6')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6DF',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_759')

    def _loc_6DF(): pass

    label('loc_6DF')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6F8',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_759')

    def _loc_6F8(): pass

    label('loc_6F8')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_711',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_759')

    def _loc_711(): pass

    label('loc_711')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_72A',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_759')

    def _loc_72A(): pass

    label('loc_72A')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_743',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_759')

    def _loc_743(): pass

    label('loc_743')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_759',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_759(): pass

    label('loc_759')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_76E',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_759')

    def _loc_76E(): pass

    label('loc_76E')

    Return()

# id: 0x0003 offset: 0x76F
@scena.Code('func_03_76F')
def func_03_76F():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_7B7',
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

    Jump('loc_9A3')

    def _loc_7B7(): pass

    label('loc_7B7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_874',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_82E',
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

    Jump('loc_871')

    def _loc_82E(): pass

    label('loc_82E')

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

    def _loc_871(): pass

    label('loc_871')

    Jump('loc_9A3')

    def _loc_874(): pass

    label('loc_874')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 0, 0x430)),
            Expr.Return,
        ),
        'loc_952',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8FD',
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

    Jump('loc_94F')

    def _loc_8FD(): pass

    label('loc_8FD')

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

    def _loc_94F(): pass

    label('loc_94F')

    Jump('loc_9A3')

    def _loc_952(): pass

    label('loc_952')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 7, 0x42F)),
            Expr.Return,
        ),
        'loc_9A3',
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

    def _loc_9A3(): pass

    label('loc_9A3')

    TalkEnd(0x000A)

    Return()

# id: 0x0004 offset: 0x9A7
@scena.Code('func_04_9A7')
def func_04_9A7():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0099, 4, 0x4CC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_AB8',
    )

    SetScenaFlags(ScenaFlag(0x0099, 4, 0x4CC))

    ChrTalk(
        0x00FE,
        (
            '唔，\n',
            '是这里吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我为了写小说，\n',
            '正在寻找资料。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '受了最近读的书的影响，\n',
            '我的创作欲望不断增强哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果可以的话，\n',
            '你们也来读读那本书吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    AddItem(0x0217, 1)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '红耀石　第６卷',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x00FE,
        (
            '呵呵，书是心灵的养料。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_AF2')

    def _loc_AB8(): pass

    label('loc_AB8')

    ChrTalk(
        0x00FE,
        (
            '唔，\n',
            '是这里吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我为了写小说，\n',
            '正在寻找资料。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_AF2(): pass

    label('loc_AF2')

    TalkEnd(0x000B)

    Return()

# id: 0x0005 offset: 0xAF6
@scena.Code('func_05_AF6')
def func_05_AF6():
    TalkBegin(0x000C)

    ChrTalk(
        0x00FE,
        (
            '吹奏部的人怎么还不来啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就靠我一个人开始准备\n',
            '没问题吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000C)

    Return()

# id: 0x0006 offset: 0xB42
@scena.Code('func_06_B42')
def func_06_B42():
    TalkBegin(0x000D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_BFF',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))
    ChrTurnDirection(0x00FE, 0x0105, 0)

    ChrTalk(
        0x00FE,
        (
            '啊，科洛丝。\n',
            '你回来了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F啊，罗伊斯，\n',
            '你看起来好像很忙呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为了做好班级展示，\n',
            '我正在调查资料呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈哈，不快点完成的话\n',
            '又要听罗基克啰嗦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C2E')

    def _loc_BFF(): pass

    label('loc_BFF')

    ChrTalk(
        0x00FE,
        (
            '为了做我们的班级展示，\n',
            '我正在调查东西呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C2E(): pass

    label('loc_C2E')

    TalkEnd(0x000D)

    Return()

# id: 0x0007 offset: 0xC32
@scena.Code('func_07_C32')
def func_07_C32():
    TalkBegin(0x000E)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_D1C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_CCC',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '现在开始要社团练习了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为学园祭休息了一阵子，\n',
            '感觉都变得迟钝了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '再怎么每天坚持练习，\n',
            '休息一阵子就会变成这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D19')

    def _loc_CCC(): pass

    label('loc_CCC')

    ChrTalk(
        0x00FE,
        (
            '现在开始要社团练习了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为学园祭休息了一阵子，\n',
            '感觉都变得迟钝了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D19(): pass

    label('loc_D19')

    Jump('loc_E51')

    def _loc_D1C(): pass

    label('loc_D1C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 7, 0x42F)),
            Expr.Return,
        ),
        'loc_E51',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_DA2',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '学园祭的准备期间\n',
            '连社团的训练都中止了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我今天来这儿\n',
            '是来拿道具的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈哈，\n',
            '因为是很重要的东西呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E51')

    def _loc_DA2(): pass

    label('loc_DA2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_E10',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '我和科洛丝一样\n',
            '是击剑部的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '接下来必须要\n',
            '去社团的摊位帮忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我很担心莉秋尔呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E51')

    def _loc_E10(): pass

    label('loc_E10')

    ChrTalk(
        0x00FE,
        (
            '那么，\n',
            '接下来要去社团的摊位帮忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我很担心莉秋尔呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E51(): pass

    label('loc_E51')

    TalkEnd(0x000E)

    Return()

# id: 0x0008 offset: 0xE55
@scena.Code('func_08_E55')
def func_08_E55():
    TalkBegin(0x000F)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 7, 0x42F)),
            Expr.Return,
        ),
        'loc_10EB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_10AF',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))
    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))
    OP_4A(0x0010, 255)

    ChrTalk(
        0x000F,
        (
            '啊，忙死了忙死了，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '班级展示、舞台剧，\n',
            '还要准备社团的摊位……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '想不到我也有么辛苦的时候呀。\n',
            '要推辞掉哪一边才好呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '……人的语言\n',
            '有时候是个暧昧的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000F, 0x0010, 500)

    ChrTalk(
        0x000F,
        (
            '…………哎？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '工作总是拼尽全力，\n',
            '得到好结果的人说自己很忙，\n',
            '这样谁都能接受。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '而固执于一件事\n',
            '却没有什么进展的人，\n',
            '倒是也有权利说自己很忙……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000F, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000F,
        (
            '你到底想说什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '不，我想知道芙拉瑟\n',
            '你说的忙是哪种情况呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '当然啦，你那么厉害，\n',
            '我想应该是前者吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000F, 0x00000000, 2000, 0x0E, 0x0F, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000F,
        (
            '……啊，我知道啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '我都做就好了吧，都做！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0010)
    ChrClearFlags(0x000F, 0x0010)
    ChrClearFlags(0x0010, 0x0010)
    OP_4B(0x0010, 255)

    Jump('loc_10EB')

    def _loc_10AF(): pass

    label('loc_10AF')

    ChrTalk(
        0x00FE,
        (
            '真是的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '蕾娜老是\n',
            '喜欢这样在旁边\n',
            '煽风点火的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_10EB(): pass

    label('loc_10EB')

    TalkEnd(0x000F)

    Return()

# id: 0x0009 offset: 0x10EF
@scena.Code('func_09_10EF')
def func_09_10EF():
    TalkBegin(0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 7, 0x42F)),
            Expr.Return,
        ),
        'loc_1343',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1318',
    )

    TalkBegin(0x000F)
    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))
    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))
    OP_4A(0x000F, 255)

    ChrTalk(
        0x000F,
        (
            '啊，忙死了忙死了，\n',
            '班级展示、舞台剧，\n',
            '还要准备社团的摊位……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '好忙呀好忙呀，\n',
            '想不到我也有么辛苦的时候呀……\n',
            '要推辞掉哪一边才好呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '……人的语言\n',
            '有时候是个暧昧的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000F, 0x0010, 500)

    ChrTalk(
        0x000F,
        (
            '哎？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '工作总是拼尽全力，\n',
            '得到好结果的人说自己很忙，\n',
            '这样谁都能接受。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '而固执于一件事\n',
            '却没有什么进展的人，\n',
            '倒是也有权利说自己很忙……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '你到底想说什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '不，我想知道芙拉瑟\n',
            '你说的忙是哪种情况呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '当然啦，你那么厉害，\n',
            '我想应该是前者吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '……啊，我知道啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '我都做就好了吧，都做！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x000F, 0x0010)
    ChrClearFlags(0x0010, 0x0010)
    OP_4B(0x000F, 255)
    TalkEnd(0x000F)

    Jump('loc_1343')

    def _loc_1318(): pass

    label('loc_1318')

    ChrTalk(
        0x00FE,
        (
            '呵呵，我知道你有能力，\n',
            '就不要推托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1343(): pass

    label('loc_1343')

    TalkEnd(0x0010)

    Return()

# id: 0x000A offset: 0x1347
@scena.Code('func_0A_1347')
def func_0A_1347():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_148A',
    )

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))
    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '#0510070187V#643F艾丝蒂尔、约修亚……\n',
            '你们是特地过来找我们的吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510070188V#640F……在这一段不算长的时间里，\n',
            '好事呀坏事呀，\n',
            '真是发生不少了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510070189V啊，\n',
            '能遇到你们实在是太好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510070190V总之最后全部\n',
            '都是好结果呢。\n',
            '就这样保持乐观继续前进吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510070191V#648F到了蔡斯也要加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1504')

    def _loc_148A(): pass

    label('loc_148A')

    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '#0510070192V#640F总之最后\n',
            '全部都是好结果呢。\n',
            '就这样保持乐观继续前进吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510070193V到了蔡斯也要继续加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1504(): pass

    label('loc_1504')

    TalkEnd(0x0008)

    Return()

# id: 0x000B offset: 0x1508
@scena.Code('func_0B_1508')
def func_0B_1508():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_163D',
    )

    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))
    ChrTurnDirection(0x00FE, 0x0102, 0)

    ChrTalk(
        0x00FE,
        (
            '#0520070194V#733F……是约修亚你们啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520070195V#732F我读过《利贝尔通讯》了……\n',
            '那个戴尔蒙市长竟然是幕后黑手啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520070196V背地里策划那种坏事，\n',
            '来学园祭捐款的时候还能面不改色。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520070197V而且后来还袭击特蕾莎院长……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520070198V…………哼，\n',
            '真是坏到骨子里去了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17B9')

    def _loc_163D(): pass

    label('loc_163D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1730',
    )

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))
    ChrTurnDirection(0x00FE, 0x0102, 0)

    ChrTalk(
        0x00FE,
        (
            '#0520070199V#730F对了，\n',
            '你们俩不是要去蔡斯吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520070200V那我们就暂时见不到面了……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520070201V不过，只要活着的话，\n',
            '总会再见面的吧，\n',
            '那我就不说再见了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520070202V为了成为一流的正游击士，\n',
            '你们一定要加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17B9')

    def _loc_1730(): pass

    label('loc_1730')

    ChrTurnDirection(0x00FE, 0x0102, 0)

    ChrTalk(
        0x00FE,
        (
            '#0520070203V#730F只要活着的话，\n',
            '总会再见面的吧，\n',
            '那我就不说再见了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520070204V为了成为一流的正游击士，\n',
            '你们一定要加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_17B9(): pass

    label('loc_17B9')

    TalkEnd(0x0009)

    Return()

# id: 0x000C offset: 0x17BD
@scena.Code('func_0C_17BD')
def func_0C_17BD():
    Call(0, 0x000D)

    Return()

# id: 0x000D offset: 0x17C2
@scena.Code('func_0D_17C2')
def func_0D_17C2():
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
        'loc_183C',
    )

    FadeIn(300, 0)
    OP_0D()
    OP_A9(0x30)
    OP_56(0x00)
    TalkEnd(0x0011)

    Return()

    def _loc_183C(): pass

    label('loc_183C')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1936',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x12),
            (Expr.PushLong, 0x1F4),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_1901',
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
        'loc_18F3',
    )

    If(
        (
            (Expr.Eval, "OP_AC(0x0009)"),
            Expr.Return,
        ),
        'loc_18CD',
    )

    Jump('loc_18F3')

    def _loc_18CD(): pass

    label('loc_18CD')

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

    def _loc_18F3(): pass

    label('loc_18F3')

    OP_56(0x00)
    FadeIn(1000, 0)

    Jump('loc_1927')

    def _loc_1901(): pass

    label('loc_1901')

    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            '没有足够的米拉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeIn(300, 0)
    def _loc_1927(): pass

    label('loc_1927')

    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x0011)

    Return()

    def _loc_1936(): pass

    label('loc_1936')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1950',
    )

    FadeIn(300, 0)
    TalkEnd(0x0011)

    Return()

    def _loc_1950(): pass

    label('loc_1950')

    FadeIn(300, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_1984',
    )

    ChrTalk(
        0x0011,
        (
            '欢迎光临。\n',
            '想要点些什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D80')

    def _loc_1984(): pass

    label('loc_1984')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            Expr.Return,
        ),
        'loc_1A97',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x008A, 2, 0x452)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1A67',
    )

    ChrTalk(
        0x0011,
        (
            '舞台剧我也看了哦。\n',
            '你们真是非常努力啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '辛苦你们了，\n',
            '这是一点小意思，\n',
            '就当是我看演出的门票吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '不用客气，吃吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x008A, 2, 0x452))
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '沙拉三明治',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(0x0193, 1)

    Jump('loc_1A94')

    def _loc_1A67(): pass

    label('loc_1A67')

    ChrTalk(
        0x0011,
        (
            '舞台剧我也看了哦。\n',
            '你们真是非常努力啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A94(): pass

    label('loc_1A94')

    Jump('loc_1D80')

    def _loc_1A97(): pass

    label('loc_1A97')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_1AEC',
    )

    ChrTalk(
        0x0011,
        (
            '你们要参加演出吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '阿姨我也要去看。\n',
            '真是很期待呀，你们要加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D80')

    def _loc_1AEC(): pass

    label('loc_1AEC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_1B44',
    )

    ChrTalk(
        0x0011,
        (
            '今天这里作为\n',
            '休息的场所对公众开放。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '不过和平时一样，\n',
            '也可以点菜哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D80')

    def _loc_1B44(): pass

    label('loc_1B44')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 0, 0x430)),
            Expr.Return,
        ),
        'loc_1BB7',
    )

    ChrTalk(
        0x0011,
        (
            '一直忙于学园祭的准备，\n',
            '都还没吃饭吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '像你们这样的孩子\n',
            '必须要好好摄取营养\n',
            '身体才能健康成长啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D80')

    def _loc_1BB7(): pass

    label('loc_1BB7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 7, 0x42F)),
            Expr.Return,
        ),
        'loc_1C18',
    )

    ChrTalk(
        0x0011,
        (
            '学园祭的准备还顺利吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '这段时间我特别准备了丰盛的饭菜，\n',
            '你们随时都能来用餐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D80')

    def _loc_1C18(): pass

    label('loc_1C18')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 6, 0x42E)),
            Expr.Return,
        ),
        'loc_1C63',
    )

    ChrTalk(
        0x0011,
        (
            '啊，马上就要下课了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '同学们要来吃饭了，\n',
            '必须加把劲呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D80')

    def _loc_1C63(): pass

    label('loc_1C63')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_1CBF',
    )

    ChrTalk(
        0x0011,
        (
            '呀，是科洛丝啊。\n',
            '现在应该还在上课啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '不好意思，\n',
            '现在这边还在准备中。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D80')

    def _loc_1CBF(): pass

    label('loc_1CBF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 6, 0x41E)),
            Expr.Return,
        ),
        'loc_1D29',
    )

    ChrTalk(
        0x0011,
        (
            '啊，\n',
            '你们两个是想来入学的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '就算不是学生也能来这里吃饭哦。\n',
            '作为参观纪念想吃些什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D80')

    def _loc_1D29(): pass

    label('loc_1D29')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_1D80',
    )

    ChrTalk(
        0x0011,
        (
            '这个学生食堂\n',
            '假日里也会开放的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '如果饿了，\n',
            '就不要客气，尽管点菜吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1D80(): pass

    label('loc_1D80')

    TalkEnd(0x0011)

    Return()

# id: 0x000E offset: 0x1D84
@scena.Code('func_0E_1D84')
def func_0E_1D84():
    TalkBegin(0x0012)

    ChrTalk(
        0x00FE,
        (
            '这里没有别人了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还是把门锁起来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0012)

    Return()

# id: 0x000F offset: 0x1DB9
@scena.Code('func_0F_1DB9')
def func_0F_1DB9():
    EventBegin(0x00)
    MapSetFlags(0x10000000)
    CameraMove(31070, 0, 57740, 0)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0102, 0x0080)
    ChrSetFlags(0x0105, 0x0080)
    ChrSetFlags(0x0008, 0x0004)
    ChrSetFlags(0x0009, 0x0040)
    OP_4A(0x0008, 255)
    OP_4A(0x0009, 255)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0510051055V#644F#1P啊～忙死了、忙死了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510051056V各货摊的检查\n',
            '还有预算的分配都ＯＫ了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510051057V请柬的发送也没问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0520051058V#734F剩下的问题就只有舞台剧了啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520051059V再找不到人选的话，\n',
            '恐怕就只有我们亲自上阵了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0009, 400)

    ChrTalk(
        0x0008,
        (
            '#0510051060V#645F#1P我自己就暂且不说，\n',
            '你……我看还是算了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510051061V一想起你试穿戏服时\n',
            '那个恐怖十足的打扮我就……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0520051062V#732F别提啦……\n',
            '我也是不堪回首啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x0102, 24910, 0, 55980, 243)
    ChrSetPos(0x0101, 24910, 0, 55980, 243)
    ChrSetPos(0x0105, 24910, 0, 55980, 243)
    ChrSetRGBAMask(0x0101, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0102, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0105, 255, 255, 255, 0, 0)

    ChrTalk(
        0x0105,
        (
            '#0060051063V#2P我回来了。\n',
            '乔儿、汉斯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x0008, 0x0105, 400)
    ChrTurnDirection(0x0009, 0x0105, 400)

    @scena.Lambda('lambda_2082')
    def lambda_2082():
        CameraMove(29890, 0, 55890, 1500)

        ExitThread()

    DispatchAsync(0x0105, 0x0002, lambda_2082)

    ChrClearFlags(0x0105, 0x0080)

    @scena.Lambda('lambda_209F')
    def lambda_209F():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0105, 0x0003, lambda_209F)

    ChrWalkTo(0x0105, 26920, 0, 55710, 2000, 0x00)

    @scena.Lambda('lambda_20C5')
    def lambda_20C5():
        ChrWalkTo(0x00FE, 27910, 0, 54400, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_20C5)

    ChrSetDirection(0x0009, 270, 0)
    ChrClearFlags(0x0101, 0x0080)

    @scena.Lambda('lambda_20EC')
    def lambda_20EC():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_20EC)

    ChrWalkTo(0x0101, 26920, 0, 55710, 2000, 0x00)

    @scena.Lambda('lambda_2112')
    def lambda_2112():
        ChrWalkTo(0x00FE, 27030, 0, 54700, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2112)

    ChrClearFlags(0x0102, 0x0080)

    @scena.Lambda('lambda_2132')
    def lambda_2132():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_2132)

    @scena.Lambda('lambda_2144')
    def lambda_2144():
        ChrWalkTo(0x00FE, 27440, 0, 55750, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_2144)

    WaitForThreadExit(0x0105, 0x0001)

    @scena.Lambda('lambda_2164')
    def lambda_2164():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_2164)

    WaitForThreadExit(0x0101, 0x0001)

    @scena.Lambda('lambda_2177')
    def lambda_2177():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2177)

    WaitForThreadExit(0x0102, 0x0001)

    @scena.Lambda('lambda_218A')
    def lambda_218A():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_218A)

    @scena.Lambda('lambda_2198')
    def lambda_2198():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_2198')

    DispatchAsync2(0x0102, 0x0001, lambda_2198)

    @scena.Lambda('lambda_21A9')
    def lambda_21A9():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_21A9')

    DispatchAsync2(0x0101, 0x0001, lambda_21A9)

    @scena.Lambda('lambda_21BA')
    def lambda_21BA():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_21BA')

    DispatchAsync2(0x0105, 0x0001, lambda_21BA)

    ChrTalk(
        0x0008,
        (
            '#0510051064V#642F啊，科洛丝！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510051065V火灾的事我们也听说了。\n',
            '事情好像很严重啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0520051066V#732F特蕾莎院长和小家伙们\n',
            '都平安无事吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060051067V#040F嗯……\n',
            '还好，大家总算没事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060051068V#049F最遗憾的是，\n',
            '孤儿院的房子被完全烧毁了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0520051069V#732F是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0510051070V#644F打起精神来嘛。\n',
            '发愁也解决不了问题啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510051071V为了让那些小家伙高兴起来，\n',
            '我们一定要把学园祭办好哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060051072V#045F嗯，特蕾莎老师\n',
            '也是这样和我说的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060051073V所以，我一定会全力以赴。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0510051074V#641F你要是认真起来，足以以一当百。\n',
            '我可是很期待你的精彩演出哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510051075V#640F对了，\n',
            '刚才就想问了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510051076V这两位是谁呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010051077V#501F初次见面。\n',
            '我叫艾丝蒂尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020051078V#010F我叫约修亚，请多关照。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0510051079V#643F那么，你们两个就是\n',
            '科洛丝昨天提过的……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060051080V#041F呵呵，我如约把他们带来了哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060051081V他们两人都答应帮我们的忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0510051082V#641F啊～这回有救了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510051083V#641F初次见面。\n',
            '艾丝蒂尔、约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510051084V我是学院的学生会长\n',
            '乔儿·利德那。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510051085V也是这次舞台剧的导演。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0520051086V#730F我是副会长汉斯。\n',
            '负责剧本和组织工作。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520051087V还请两位多多关照。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010051088V#000F嗯，彼此彼此。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020051089V#010F请多关照。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0510051090V#644F嗯，不过话说回来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1200)

    OP_63(0x0008)

    ChrTalk(
        0x0101,
        (
            '#0010051091V#004F什、什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0510051092V#640F不愧是游击士，\n',
            '看上去真的充满运动细胞啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510051093V艾丝蒂尔，你会用剑吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010051094V#008F这个，也不是很擅长啦……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010051095V我主要学的是棒术，\n',
            '不过倒也跟老爸学过一点剑法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0510051096V#641F太好了，那就这么定了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510051097V你就用细剑\n',
            '和科洛丝来场精彩的决斗吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010051098V#004F决、决斗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0105, 0xFF)
    TerminateThread(0x0102, 0xFF)
    ChrTurnDirection(0x0102, 0x0105, 400)
    ChrTurnDirection(0x0105, 0x0101, 400)

    ChrTalk(
        0x0105,
        (
            '#0060051099V#040F#2P当然是在舞台剧的时候。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0510051100V#640F舞台剧的高潮部分，\n',
            '会有两位骑士决斗的剧情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510051101V总之，这是今年学园祭里\n',
            '最扣人心弦的压轴好戏啦……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510051102V#645F可惜到现在还找不到一个\n',
            '能在剑法上和科洛丝一拼的女生。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510051103V这丫头甚至在学院的击剑大赛里\n',
            '打赢了男生取得优胜呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010051104V#501F哇～好厉害！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0510051105V#649F顺便一提，在决赛中输给她的\n',
            '就是我旁边的这位汉斯哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0520051106V#734F真不好意思，输掉了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520051107V不过可不是我太弱，\n',
            '而是科洛丝实在太强了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060051108V#045F#2P太、太夸奖了，\n',
            '其实我也只是业余水准……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060051109V跟职业水平的艾丝蒂尔比起来，\n',
            '我也是小巫见大巫呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010051110V#006F又来了又来了，你太谦虚了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010051111V不过，这种事的话\n',
            '或许我真的能帮上点忙。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010051112V#001F科洛丝，我们一起加油哦⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060051113V#041F#2P是。\n',
            '请多多指教。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020051114V#019F#1P哈哈，不过话说回来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020051115V女骑士之间的对决，\n',
            '这题材真是挺独一无二的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0102, 400)

    ChrTalk(
        0x0009,
        (
            '#0520051116V#733F女骑士？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520051117V她们要演的可是\n',
            '受人仰慕的男性骑士哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2CB5')
    def lambda_2CB5():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_2CB5)

    ChrTurnDirection(0x0102, 0x0009, 0)
    Sleep(400)

    ChrTalk(
        0x0102,
        (
            '#0020051118V#014F#1P哎？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0510051119V#649F不过约修亚也真是无可挑剔，\n',
            '另一个重要角色非你莫属呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510051120V期待你的表现哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0520051121V#731F嗯嗯，虽然不甘心，不过我也有同感。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010051122V#501F？？？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0008, 400)

    ChrTalk(
        0x0102,
        (
            '#0020051123V#014F那个，这出舞台剧……\n',
            '大致的故事情节是什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0510051124V#640F剧名叫『白花恋诗』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510051125V是以废除贵族制度时期的王都为舞台，\n',
            '一个非常有名的故事哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510051126V#647F贵族出身的骑士和\n',
            '平民出身的骑士同时\n',
            '爱上了王族公主的爱情诗剧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510051127V#642F这三个人虽然身份地位悬殊，\n',
            '但却是从小一起长大的好朋友。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510051128V而剧情当中又夹杂着\n',
            '贵族势力和平民势力的明争暗斗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510051129V#648F不过最后还是大团圆，\n',
            '无可挑剔的完满结局哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010051130V#001F哎～听起来很有趣啊⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020051131V#014F那、那么……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020051132V为什么要由女孩来演男性角色？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0520051133V#731F这是今年的学园祭才有的，\n',
            '可说是独创且又刺激的安排哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520051134V由男女演员反串出演，\n',
            '以一种新鲜的形式表现舞台剧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010051135V#004F男女反串？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010051136V哎～这样子安排，\n',
            '老师居然也会批准啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0510051137V#644F摆脱性别歧视！\n',
            '从性别中解放出来！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510051138V我们诌了一堆这样那样的理由，\n',
            '好不容易才逼他们同意的哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510051139V#641F不过话说回来，\n',
            '其实也只是因为好玩啦㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060051140V#045F乔儿你真是的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0520051141V#734F唉，这种家伙居然当上了学生会长，\n',
            '看来这世道也快到头了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010051142V#001F啊哈哈☆\n',
            '嗯，看来的确很好玩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 2000, 0x14, 0x17, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x0102, 0x0105, 400)

    ChrTalk(
        0x0102,
        (
            '#0020051143V#018F#1P等、等一下！\n',
            '照你们这样说的话……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020051144V那个非我莫属的\n',
            '『重要角色』难道是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0520051145V#731F哎呀，你能参与可真是帮了大忙呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0510051146V#641F科洛丝，多谢你啦。\n',
            '介绍了这么好的两个人来㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060051147V#045F#4P啊、啊哈哈……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060051148V对不起呢，约修亚……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1500, 0, -1)
    OP_0D()
    OP_28(0x003D, 0x01, 0x0020)
    OP_28(0x003D, 0x01, 0x0040)
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T2513._SN', 113, 0, 0)
    IdleLoop()

    Return()

# id: 0x0010 offset: 0x33AF
@scena.Code('func_10_33AF')
def func_10_33AF():
    EventBegin(0x00)
    CameraMove(6500, 0, -150, 0)
    OP_77(0xFF, 0xC8, 0x96, 0x00, 0x00000000)
    OP_4A(0x0008, 255)
    OP_4A(0x0009, 255)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetFlags(0x0101, 0x0004)
    ChrSetFlags(0x0105, 0x0004)
    ChrSetFlags(0x0102, 0x0004)
    ChrSetFlags(0x0008, 0x0004)
    ChrSetFlags(0x0009, 0x0004)
    ChrSetPos(0x0105, 6070, 100, -420, 180)
    ChrSetPos(0x0101, 6070, 100, -2400, 0)
    ChrSetPos(0x0008, 5150, 0, -260, 180)
    ChrSetChipByIndex(0x0101, 8)
    ChrSetChipByIndex(0x0105, 10)
    ChrSetPos(0x0102, -230, -250, -7260, 0)
    ChrSetPos(0x0009, 280, -250, -6290, 0)
    OP_62(0x0101, 0x00000000, 1850, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0105, 0x00000000, 1850, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    Sleep(2000)

    OP_62(0x0101, 0x00000000, 1850, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0105, 0x00000000, 1850, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    Sleep(2000)

    @scena.Lambda('lambda_34D1')
    def lambda_34D1():
        CameraMove(5210, 0, -1580, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_34D1)

    @scena.Lambda('lambda_34E9')
    def lambda_34E9():
        ChrWalkTo(0x00FE, 2280, 0, -1810, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_34E9)

    Sleep(500)

    @scena.Lambda('lambda_3509')
    def lambda_3509():
        ChrWalkTo(0x00FE, 2300, 0, -2900, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_3509)

    ChrSetSubChip(0x0101, 1)
    ChrSetSubChip(0x0105, 2)

    @scena.Lambda('lambda_352E')
    def lambda_352E():
        ChrTurnDirection(0x00FE, 0x0102, 0)
        Yield()

        Jump('lambda_352E')

    DispatchAsync2(0x0008, 0x0001, lambda_352E)

    WaitForThreadExit(0x0009, 0x0001)

    @scena.Lambda('lambda_3544')
    def lambda_3544():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_3544)

    WaitForThreadExit(0x0102, 0x0001)

    @scena.Lambda('lambda_3557')
    def lambda_3557():
        ChrSetDirection(0x00FE, 45, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_3557)

    Sleep(500)

    OP_62(0x0009, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0102, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    Sleep(2000)

    OP_62(0x0101, 0x00000000, 1850, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0105, 0x00000000, 1850, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    Sleep(1000)

    FadeOut(2000, 0, -1)
    OP_0D()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '中午，他们就和大家一起在饭堂里\n',
            '共进午餐、谈天说地……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    NewScene('ED6_DT01/T2513._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0011 offset: 0x361D
@scena.Code('func_11_361D')
def func_11_361D():
    ClearScenaFlags(ScenaFlag(0x0001, 5, 0xD))
    ClearScenaFlags(ScenaFlag(0x0001, 6, 0xE))
    PlaySE(17, 0x00, 0x64)
    ChrSetFlags(0x0013, 0x0080)
    OP_64(0x02, 0x0001)
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '卢安经济史·上',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(0x033D, 1)
    OP_28(0x0027, 0x01, 0x0040)
    TalkEnd(0x00FF)

    Return()

# id: 0x0012 offset: 0x3689
@scena.Code('func_12_3689')
def func_12_3689():
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
            TXT(0x00, '【归还卢安经济史】\n'),
            TXT(0x01, '【不归还】\n'),
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
        (0x00000000, 'loc_36F8'),
        (0x00000001, 'loc_3803'),
        (-1, 'loc_3806'),
    )

    def _loc_36F8(): pass

    label('loc_36F8')

    If(
        (
            (Expr.Eval, "OP_40(0x033D)"),
            Expr.Return,
        ),
        'loc_3750',
    )

    RemoveItem(0x033D, 1)
    OP_28(0x0027, 0x01, 0x0200)
    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '归还了',
            (TxtCtl.SetColor, 0x2),
            '卢安经济史·上',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    def _loc_3750(): pass

    label('loc_3750')

    If(
        (
            (Expr.Eval, "OP_40(0x033E)"),
            Expr.Return,
        ),
        'loc_37A8',
    )

    RemoveItem(0x033E, 1)
    OP_28(0x0027, 0x01, 0x0400)
    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '归还了',
            (TxtCtl.SetColor, 0x2),
            '卢安经济史·中',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    def _loc_37A8(): pass

    label('loc_37A8')

    If(
        (
            (Expr.Eval, "OP_40(0x033F)"),
            Expr.Return,
        ),
        'loc_3800',
    )

    RemoveItem(0x033F, 1)
    OP_28(0x0027, 0x01, 0x0800)
    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '归还了',
            (TxtCtl.SetColor, 0x2),
            '卢安经济史·下',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    def _loc_3800(): pass

    label('loc_3800')

    Jump('loc_3806')

    def _loc_3803(): pass

    label('loc_3803')

    Jump('loc_3806')

    def _loc_3806(): pass

    label('loc_3806')

    If(
        (
            (Expr.Eval, "OP_40(0x033D)"),
            Expr.Ez,
            (Expr.Eval, "OP_40(0x033E)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x033F)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_381F',
    )

    OP_64(0x00, 0x0001)

    def _loc_381F(): pass

    label('loc_381F')

    TalkEnd(0x00FF)

    Return()

# id: 0x0013 offset: 0x3823
@scena.Code('func_13_3823')
def func_13_3823():
    OP_13(0x0071)

    Return()

# id: 0x0014 offset: 0x3827
@scena.Code('func_14_3827')
def func_14_3827():
    OP_13(0x0072)

    Return()

# id: 0x0015 offset: 0x382B
@scena.Code('func_15_382B')
def func_15_382B():
    OP_13(0x0075)

    Return()

# id: 0x0016 offset: 0x382F
@scena.Code('func_16_382F')
def func_16_382F():
    OP_13(0x0070)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
