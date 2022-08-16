import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import E0010_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('E0010   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'event'
    header.mapModel       = 'E0010.x'
    header.mapIndex       = 1
    header.bgm            = 1
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
        ('ED6_DT07/CH01443._CH', 'ED6_DT07/CH01443P._CP'),
        ('ED6_DT07/CH01290._CH', 'ED6_DT07/CH01290P._CP'),
        ('ED6_DT07/CH01293._CH', 'ED6_DT07/CH01293P._CP'),
        ('ED6_DT07/CH01540._CH', 'ED6_DT07/CH01540P._CP'),
        ('ED6_DT07/CH01290._CH', 'ED6_DT07/CH01290P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH00023._CH', 'ED6_DT07/CH00023P._CP'),
        ('ED6_DT07/CH00053._CH', 'ED6_DT07/CH00053P._CP'),
        ('ED6_DT07/CH01410._CH', 'ED6_DT07/CH01410P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01030._CH', 'ED6_DT07/CH01030P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT07/CH01143._CH', 'ED6_DT07/CH01143P._CP'),
        ('ED6_DT07/CH01120._CH', 'ED6_DT07/CH01120P._CP'),
        ('ED6_DT07/CH01013._CH', 'ED6_DT07/CH01013P._CP'),
        ('ED6_DT07/CH01213._CH', 'ED6_DT07/CH01213P._CP'),
        ('ED6_DT07/CH01103._CH', 'ED6_DT07/CH01103P._CP'),
        ('ED6_DT07/CH01133._CH', 'ED6_DT07/CH01133P._CP'),
        ('ED6_DT07/CH01490._CH', 'ED6_DT07/CH01490P._CP'),
        ('ED6_DT07/CH01043._CH', 'ED6_DT07/CH01043P._CP'),
        ('ED6_DT07/CH01450._CH', 'ED6_DT07/CH01450P._CP'),
    ]

# id: 0x10001 offset: 0x152
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '古兰托机长',
            x                   = 59020,
            z                   = -600,
            y                   = 49310,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0115,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            name                = '乘务员迪蒙',
            x                   = 60800,
            z                   = -2000,
            y                   = 53360,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0111,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '乘务员卡尔托斯',
            x                   = 59190,
            z                   = -1950,
            y                   = 54200,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0115,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            name                = '乘务员卡拉莉丝',
            x                   = 88840,
            z                   = 0,
            y                   = 47400,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            name                = '乘务员波嘉',
            x                   = 85950,
            z                   = 0,
            y                   = 9240,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0111,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '罗伊德',
            x                   = 115970,
            z                   = 0,
            y                   = 11300,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0111,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            name                = '雪拉扎德',
            x                   = 117330,
            z                   = 200,
            y                   = 1160,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0195,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0016,
        ),
        ScenaNpcData(
            name                = '阿加特',
            x                   = 117330,
            z                   = 200,
            y                   = 1160,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0195,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0017,
        ),
        ScenaNpcData(
            name                = '修女萝萨',
            x                   = 89500,
            z                   = 0,
            y                   = 9050,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '菲利奥',
            x                   = 91250,
            z                   = 0,
            y                   = 44510,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            name                = '拉科舒',
            x                   = 91250,
            z                   = 0,
            y                   = 45520,
            direction           = 120,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '西蒙',
            x                   = 57200,
            z                   = 0,
            y                   = -1850,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '巴雷尔',
            x                   = 117490,
            z                   = 100,
            y                   = 5290,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0115,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '奥维德',
            x                   = 89340,
            z                   = -1000,
            y                   = 52850,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0111,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '乘客',
            x                   = 89270,
            z                   = 200,
            y                   = -3230,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0115,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '乘客',
            x                   = 85350,
            z                   = 150,
            y                   = -1370,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0115,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0011,
        ),
        ScenaNpcData(
            name                = '乘客',
            x                   = 117490,
            z                   = 100,
            y                   = 7300,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 16,
            chipIndex           = 16,
            npcIndex            = 0x0115,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0012,
        ),
        ScenaNpcData(
            name                = '乘客',
            x                   = 89270,
            z                   = 150,
            y                   = 430,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x0115,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            name                = '乘客',
            x                   = 88030,
            z                   = 0,
            y                   = 430,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 18,
            chipIndex           = 18,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0014,
        ),
        ScenaNpcData(
            name                = '乘客',
            x                   = 113400,
            z                   = 100,
            y                   = -630,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 19,
            chipIndex           = 19,
            npcIndex            = 0x0115,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0015,
        ),
        ScenaNpcData(
            name                = '登克',
            x                   = 31990,
            z                   = 0,
            y                   = 5410,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 20,
            chipIndex           = 20,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
    )

# id: 0x10002 offset: 0x3F2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x3F2
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x3F2
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x3F2
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x6E),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_40F',
    )

    OP_89(0x0101, 84860, 130, 5970, 0)

    def _loc_40F(): pass

    label('loc_40F')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000065, 'loc_43F'),
        (0x00000066, 'loc_43F'),
        (0x00000067, 'loc_43F'),
        (0x00000068, 'loc_43F'),
        (0x00000069, 'loc_43F'),
        (0x0000006A, 'loc_43F'),
        (0x0000006B, 'loc_43F'),
        (0x0000006D, 'loc_43F'),
        (0x0000006E, 'loc_43F'),
        (0x00000073, 'loc_43F'),
        (-1, 'loc_4C3'),
    )

    def _loc_43F(): pass

    label('loc_43F')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 7, 0x1207)),
            Expr.Return,
        ),
        'loc_45A',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_45A(): pass

    label('loc_45A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0241, 0, 0x1208)),
            Expr.Return,
        ),
        'loc_46B',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_46B(): pass

    label('loc_46B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0241, 1, 0x1209)),
            Expr.Return,
        ),
        'loc_47C',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_47C(): pass

    label('loc_47C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0241, 2, 0x120A)),
            Expr.Return,
        ),
        'loc_48D',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_48D(): pass

    label('loc_48D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0241, 3, 0x120B)),
            Expr.Return,
        ),
        'loc_49E',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_49E(): pass

    label('loc_49E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0241, 5, 0x120D)),
            Expr.Return,
        ),
        'loc_4AF',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_4AF(): pass

    label('loc_4AF')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4C0',
    )

    Event(0, func_18_2B58)

    def _loc_4C0(): pass

    label('loc_4C0')

    Jump('loc_4C3')

    def _loc_4C3(): pass

    label('loc_4C3')

    Return()

# id: 0x0001 offset: 0x4C4
@scena.Code('func_01_4C4')
def func_01_4C4():
    PlaySE(122, 0x01, 0x46)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_4D8',
    )

    ChrClearFlags(0x000E, 0x0080)

    Jump('loc_4DD')

    def _loc_4D8(): pass

    label('loc_4D8')

    ChrClearFlags(0x000F, 0x0080)

    def _loc_4DD(): pass

    label('loc_4DD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0241, 1, 0x1209)),
            Expr.Return,
        ),
        'loc_4E9',
    )

    ChrClearFlags(0x000D, 0x0010)

    def _loc_4E9(): pass

    label('loc_4E9')

    Return()

# id: 0x0002 offset: 0x4EA
@scena.Code('func_02_4EA')
def func_02_4EA():
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
        'loc_50F',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_651')

    def _loc_50F(): pass

    label('loc_50F')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_528',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_651')

    def _loc_528(): pass

    label('loc_528')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_541',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_651')

    def _loc_541(): pass

    label('loc_541')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_55A',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_651')

    def _loc_55A(): pass

    label('loc_55A')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_573',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_651')

    def _loc_573(): pass

    label('loc_573')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_58C',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_651')

    def _loc_58C(): pass

    label('loc_58C')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5A5',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_651')

    def _loc_5A5(): pass

    label('loc_5A5')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5BE',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_651')

    def _loc_5BE(): pass

    label('loc_5BE')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5D7',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_651')

    def _loc_5D7(): pass

    label('loc_5D7')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5F0',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_651')

    def _loc_5F0(): pass

    label('loc_5F0')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_609',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_651')

    def _loc_609(): pass

    label('loc_609')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_622',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_651')

    def _loc_622(): pass

    label('loc_622')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_63B',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_651')

    def _loc_63B(): pass

    label('loc_63B')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_651',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_651(): pass

    label('loc_651')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_666',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_651')

    def _loc_666(): pass

    label('loc_666')

    Return()

# id: 0x0003 offset: 0x667
@scena.Code('func_03_667')
def func_03_667():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 7, 0x1207)),
            Expr.Return,
        ),
        'loc_8A5',
    )

    ChrClearFlags(0x00FE, 0x0010)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    If(
        (
            (Expr.PushLong, 0x1E),
            (Expr.GetChrWork, 0xFE, 0x4),
            Expr.Lss,
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x96),
            Expr.Lss,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_69E',
    )

    ChrSetSubChip(0x00FE, 1)

    Jump('loc_6C4')

    def _loc_69E(): pass

    label('loc_69E')

    If(
        (
            (Expr.PushLong, 0xD2),
            (Expr.GetChrWork, 0xFE, 0x4),
            Expr.Lss,
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x14A),
            Expr.Lss,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_6BF',
    )

    ChrSetSubChip(0x00FE, 2)

    Jump('loc_6C4')

    def _loc_6BF(): pass

    label('loc_6BF')

    ChrSetSubChip(0x00FE, 0)

    def _loc_6C4(): pass

    label('loc_6C4')

    ChrSetDirection(0x00FE, 0, 0)
    ChrSetFlags(0x00FE, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_74F',
    )

    ChrTalk(
        0x00FE,
        (
            '#1281390015V能找到父亲可真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1281390016V虽然时间已经所剩无几，\n',
            '不过抵达前好好享受一下空中旅行吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8A2')

    def _loc_74F(): pass

    label('loc_74F')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '#1281390011V……话说回来，\n',
            '你们找到自己父亲了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0011350006V#1000F啊，嗯。\n',
            '总算是回来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0011350007V#1007F……真的是在最后关头呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1281390012V是吗，这实在是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1281390013V这些话我只在这里说，\n',
            '其实我也稍微有点担心呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1281390014V毕竟他突然提出\n',
            '要下船的要求嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0011350008V#1008F啊，啊哈哈……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8A2(): pass

    label('loc_8A2')

    Jump('loc_D10')

    def _loc_8A5(): pass

    label('loc_8A5')

    SetScenaFlags(ScenaFlag(0x0240, 7, 0x1207))

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ChrClearFlags(0x00FE, 0x0010)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    If(
        (
            (Expr.PushLong, 0x1E),
            (Expr.GetChrWork, 0xFE, 0x4),
            Expr.Lss,
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x96),
            Expr.Lss,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_8DF',
    )

    ChrSetSubChip(0x00FE, 1)

    Jump('loc_905')

    def _loc_8DF(): pass

    label('loc_8DF')

    If(
        (
            (Expr.PushLong, 0xD2),
            (Expr.GetChrWork, 0xFE, 0x4),
            Expr.Lss,
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x14A),
            Expr.Lss,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_900',
    )

    ChrSetSubChip(0x00FE, 2)

    Jump('loc_905')

    def _loc_900(): pass

    label('loc_900')

    ChrSetSubChip(0x00FE, 0)

    def _loc_905(): pass

    label('loc_905')

    ChrSetDirection(0x00FE, 0, 0)
    ChrSetFlags(0x00FE, 0x0010)

    ChrTalk(
        0x00FE,
        (
            '#1281390001V来操舵室有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '#1281390002V啊，你难道是\n',
            '解决那起空贼事件的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0011350009V#1011F啊，好久不见了，船长先生。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0011350010V还记得上次见面是在空贼团的要塞呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1281390003V哎呀，果然是这么回事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1281390004V对了对了，\n',
            '我好像还没有正式向你们道过谢吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1281390005V我在这里代表本船的全体成员，\n',
            '再次向你表示感谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0011350011V#1008F啊哈哈，太客气了。\n',
            '我们只是尽我们的义务而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0011350012V#1000F不过，感觉真不可思议呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0011350013V之前在废坑发现的林德号……\n',
            '现在居然能够像这个样子来搭乘。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1281390006V虽然维修花费了比较多的时间，\n',
            '不过基本上已经恢复了原貌。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1281390007V如果它知道你们也坐在上面，\n',
            '这条船肯定也会加倍努力的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    PlaySE(226, 0x00, 0x64)
    Sleep(600)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010191490V#1004F啊……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1281390008V哈哈，\n',
            '看来它听到我们的话了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1281390009V照现在这个风速的话，\n',
            '我想应该很快就会抵达卢安的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1281390010V虽然有点依依不舍，但至少到抵达前\n',
            '好好享受一下空中旅行吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0011350014V#1001F嗯，我们就不客气了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_D10(): pass

    label('loc_D10')

    ChrSetSubChip(0x00FE, 0)
    TalkEnd(0x00FE)

    Return()

# id: 0x0004 offset: 0xD19
@scena.Code('func_04_D19')
def func_04_D19():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_D7B',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，海风不强真是帮了大忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看来今天不必过份使用导力引擎\n',
            '就可以顺利飞行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DD6')

    def _loc_D7B(): pass

    label('loc_D7B')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '高度保持不变，\n',
            '推力固定在６０％。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '直到飞至卢比诺川上空之前，\n',
            '维持现在的航线。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_DD6(): pass

    label('loc_DD6')

    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0xDDA
@scena.Code('func_05_DDA')
def func_05_DDA():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_E47',
    )

    ChrTalk(
        0x00FE,
        (
            '各位乘客～再过一会儿\n',
            '就可以看见一条巨大的河流了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那就是王国最大的河流——\n',
            '卢比诺川。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EB2')

    def _loc_E47(): pass

    label('loc_E47')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '各位乘客～\n',
            '右手边看到的是瓦雷利亚湖。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '遗憾的是雾比较大，\n',
            '不过湖的大致形状应该还是能够看见的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_EB2(): pass

    label('loc_EB2')

    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0xEB6
@scena.Code('func_06_EB6')
def func_06_EB6():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_F39',
    )

    ChrTalk(
        0x00FE,
        (
            '我结束了在大圣堂的工作，\n',
            '正准备返回柏斯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们那边的教区长是个我行我素的人，\n',
            '真不知道这段时间教会怎样了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_100A')

    def _loc_F39(): pass

    label('loc_F39')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '我结束了在大圣堂的工作，\n',
            '正准备返回柏斯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那里没有我的话实在是很让人担心，\n',
            '结果在王都整个人都心不在焉的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然是反方向航行的船，\n',
            '但想都没想就了上来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊啊，\n',
            '主日学校顺利结束了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_100A(): pass

    label('loc_100A')

    TalkEnd(0x00FE)

    Return()

# id: 0x0007 offset: 0x100E
@scena.Code('func_07_100E')
def func_07_100E():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_103E',
    )

    ChrTalk(
        0x00FE,
        (
            '这，这次……\n',
            '可别再出事了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10B6')

    def _loc_103E(): pass

    label('loc_103E')

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x00FE,
        (
            '话说回来，这次是我\n',
            '第二次搭乘定期船……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '上次被卷进了\n',
            '那个空贼团的事件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '拜、拜托这次\n',
            '可别再出事了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_10B6(): pass

    label('loc_10B6')

    TalkEnd(0x00FE)

    Return()

# id: 0x0008 offset: 0x10BA
@scena.Code('func_08_10BA')
def func_08_10BA():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0241, 2, 0x120A)),
            Expr.Return,
        ),
        'loc_1125',
    )

    ChrTalk(
        0x00FE,
        (
            '这次的货物几乎都是\n',
            '在蔡斯装载的导力器。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然不知为什么，\n',
            '不过最近的物流还挺繁忙的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1180')

    def _loc_1125(): pass

    label('loc_1125')

    SetScenaFlags(ScenaFlag(0x0241, 2, 0x120A))

    ChrTalk(
        0x00FE,
        (
            '这里是储货仓。\n',
            '不是乘客该来的地方哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '摇摇晃晃地走来走去\n',
            '会撞到头的，小心哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1180(): pass

    label('loc_1180')

    TalkEnd(0x00FE)

    Return()

# id: 0x0009 offset: 0x1184
@scena.Code('func_09_1184')
def func_09_1184():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_11F1',
    )

    ChrTalk(
        0x00FE,
        (
            '唔～要把玛诺利亚周边\n',
            '全部食材都重新检视一遍……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还是需要做个列表\n',
            '有计划地调查才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_140F')

    def _loc_11F1(): pass

    label('loc_11F1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1280',
    )

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
            TXT(0x00, '◇完成『狩猎蘑菇』或『探索的护卫』\n'),
            TXT(0x01, '◇未完成『狩猎蘑菇』或『探索的护卫』\n'),
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

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1280',
    )

    OP_28(0x0005, 0x04, 0x10)

    def _loc_1280(): pass

    label('loc_1280')

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    If(
        (
            (Expr.Eval, "OP_29(0x0005, 0x00, 0x10)"),
            (Expr.Eval, "OP_29(0x001F, 0x00, 0x10)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_1383',
    )

    ChrTalk(
        0x00FE,
        (
            '唔唔～……\n',
            '…………嗯嗯嗯嗯嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#1019F（这，这个人是……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '下、下一笔生意\n',
            '无论如何都必须谈成功……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在还是先\n',
            '把当地的食材重新检视一遍吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，是啊。\n',
            '回到初学者的心态\n',
            '开始地道的调查吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_140F')

    def _loc_1383(): pass

    label('loc_1383')

    ChrTalk(
        0x00FE,
        (
            '唔唔～下次商谈\n',
            '无论如何都必须成功……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在还是先\n',
            '把当地的食材重新检视一遍吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，是啊。\n',
            '回到初学者的心态\n',
            '开始地道的调查吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_140F(): pass

    label('loc_140F')

    TalkEnd(0x00FE)

    Return()

# id: 0x000A offset: 0x1413
@scena.Code('func_0A_1413')
def func_0A_1413():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_1499',
    )

    ChrTalk(
        0x00FE,
        (
            '呼～刚回到柏斯\n',
            '马上又要掉头去蔡斯啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '米拉诺小姐安排的行程\n',
            '总是那么紧迫。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，这样倒也\n',
            '不会浪费时间……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_152F')

    def _loc_1499(): pass

    label('loc_1499')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '呼～才刚回到柏斯，\n',
            '马上又要掉头去蔡斯啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '和帝国的互不侵犯条约要是顺利签署，\n',
            '导力器的出口量也会增加。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '得趁现在去蔡斯\n',
            '多进一些现货。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_152F(): pass

    label('loc_152F')

    TalkEnd(0x00FE)

    Return()

# id: 0x000B offset: 0x1533
@scena.Code('func_0B_1533')
def func_0B_1533():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_15AE',
    )

    ChrTalk(
        0x00FE,
        (
            '不过，最近这个人\n',
            '确实很努力呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '也有在努力工作……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……呼，这样就马上\n',
            '变得宽容也是我的弱点呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15EE')

    def _loc_15AE(): pass

    label('loc_15AE')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '什么叫『偶尔』啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不是好不容易\n',
            '才刚刚找到工作吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_15EE(): pass

    label('loc_15EE')

    TalkEnd(0x00FE)

    Return()

# id: 0x000C offset: 0x15F2
@scena.Code('func_0C_15F2')
def func_0C_15F2():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '听说卢安的娱乐场\n',
            '又重新装修要开张了呢。\n',
            '于是我就马上从王都赶来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '人生也需要\n',
            '偶然放松一下嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x000D offset: 0x1662
@scena.Code('func_0D_1662')
def func_0D_1662():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0241, 1, 0x1209)),
            Expr.Return,
        ),
        'loc_1763',
    )

    ChrTalk(
        0x00FE,
        (
            '#1230200704V提到卢安肯定就要联想到海边垂钓了，\n',
            '不过其它地方也有不少优质的钓鱼场。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1230200705V市内流淌的卢比诺川，\n',
            '还有以瀑布闻名的艾尔·雷登，\n',
            '在钓鱼爱好者之间都是很有名的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1230200706V如果有机会去的话，\n',
            '务必要带上钓竿哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E14')

    def _loc_1763(): pass

    label('loc_1763')

    SetScenaFlags(ScenaFlag(0x0241, 1, 0x1209))

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    EventBegin(0x00)
    Fade(1000)
    ChrSetPos(0x0101, 115920, 0, 10120, 0)
    OP_69(0x0101, 0)
    OP_4A(0x00FE, 255)
    OP_0D()

    ChrTalk(
        0x00FE,
        (
            '#1230200673V哟哟，瓦雷利亚湖啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1230200674V在那广阔的湖中某处，\n',
            '对……有那传说中的鱼王。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200675V#1016F#2P（一点都没变呢～～）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1230200676V嗯……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x00FE, 0x0010)
    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTurnDirection(0x00FE, 0x0000, 400)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '#1230200677V啊，还以为是谁呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200678V#1000F#2P罗伊德先生，好久不见。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200679V又要去挑战瓦雷利亚湖的\n',
            '鱼王了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1230200680V不，这次\n',
            '预定去卢安。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1230200681V听说市内也有可以轻松享受的\n',
            '钓鱼点呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200682V#1016F#2P真是热心啊～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200683V虽然确实很有趣，不过我\n',
            '应该还没有那么入迷吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1230200684V哎呀……是吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1230200685V唔～那可真是遗憾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1230200686V以前在湖畔的旅馆我可是见识过，\n',
            '你的钓鱼天赋实在是相当出色啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '#1230200687V……对了。\n',
            '这个给你吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200688V#1000F#2P？？？',
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
            (TxtCtl.Item, ItemTable['垂钓手册']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, 0x24F),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(ItemTable['垂钓手册'], 1)
    AddItem(0x024F, 1)

    ChrTalk(
        0x0101,
        (
            '#0010200689V#1015F#2P这是……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1230200690V初级者用的钓竿\n',
            '和写下钓鱼记录的手册。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1230200691V毕竟我们『钓公师团』\n',
            '是以普及钓鱼文化为目的\n',
            '而进行活动的团体嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1230200692V对有素质的年轻人\n',
            '应该赠予这样的道具的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1230200693V话说回来…\n',
            '你也要去卢安吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200694V#1000F#2P嗯，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1230200695V嗯，那就尽快\n',
            '甩甩钓竿试试吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1230200696V卢安可是\n',
            '有很多钓场的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200697V#1011F#2P啊啊～是吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200698V这么说来确实是个\n',
            '有很多水边的地方呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1230200699V刚才我也说了…\n',
            '市内也有钓鱼点，\n',
            '先在那边练习练习吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1230200700V总之一开始还是轻轻松松\n',
            '享受就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200701V#1001F#2P嗯，谢谢。\n',
            '我一定试试看的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1230200702V希望你有朝一日也能\n',
            '加入『钓公师团』啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1230200703V那么，祝旅途顺利。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x00FE, 45, 400)
    EventEnd(0x00)

    def _loc_1E14(): pass

    label('loc_1E14')

    TalkEnd(0x00FE)

    Return()

# id: 0x000E offset: 0x1E18
@scena.Code('func_0E_1E18')
def func_0E_1E18():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0241, 0, 0x1208)),
            Expr.Return,
        ),
        'loc_1E99',
    )

    ChrTalk(
        0x00FE,
        (
            '#1321400011V话说回来，游击士\n',
            '总是忙忙碌碌的，真辛苦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1321400012V不过，多亏你们的努力\n',
            '才能维持和平呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2279')

    def _loc_1E99(): pass

    label('loc_1E99')

    SetScenaFlags(ScenaFlag(0x0241, 0, 0x1208))

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    OP_4A(0x00FE, 255)

    ChrTalk(
        0x00FE,
        (
            '#1321400001V哎呀…………？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(2000)

    ChrTalk(
        0x00FE,
        (
            '#1321400002V请问，客人是\n',
            '游击士协会的人，对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0011350015V#1000F嗯，是啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1321400003V呀，果然没错。\n',
            '真高兴能再次相见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1321400004V还记得吗？\n',
            '我在空贼团事件的时候\n',
            '承蒙你们相救了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0011350016V#1004F啊，是和船长先生在一起的人吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1321400005V嗯嗯，我是客室乘务员\n',
            '卡拉莉丝。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1321400006V全体乘务员都由衷地\n',
            '感谢你们呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1321400007V能像现在这样重新营业，\n',
            '也是多亏游击士们的活跃表现啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0011350017V#1008F啊哈哈，太客气了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0011350018V#1000F被当作人质的乘务员们\n',
            '都平安回到工作岗位了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1321400008V嗯嗯，大家都比以往\n',
            '更加努力工作呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0011350019V#1006F是吗，太好了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0011350020V大家都回到\n',
            '平常的生活了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1321400009V对了，今天是来旅行？\n',
            '还是工作呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0011350021V#1016F嘿嘿，很可惜是工作。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0011350022V今后因为公事要使用定期船\n',
            '的机会似乎变多了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0011350023V以后再乘坐的话\n',
            '就要麻烦你们关照了哦⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1321400010V是，期待你们的光临。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4B(0x00FE, 255)

    def _loc_2279(): pass

    label('loc_2279')

    TalkEnd(0x00FE)

    Return()

# id: 0x000F offset: 0x227D
@scena.Code('func_0F_227D')
def func_0F_227D():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_22DE',
    )

    ChrTalk(
        0x00FE,
        (
            '推力确定设定为６０％。\n',
            '导力驱动器固定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好，照这状况\n',
            '可以准时到达卢安吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2335')

    def _loc_22DE(): pass

    label('loc_22DE')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '高度良好。\n',
            '推进力变更为６０％。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '直到飞至卢比诺川上空之前，\n',
            '维持现在方向。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2335(): pass

    label('loc_2335')

    TalkEnd(0x00FE)

    Return()

# id: 0x0010 offset: 0x2339
@scena.Code('func_10_2339')
def func_10_2339():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '我们年轻的时候\n',
            '可要辛苦地在各个街道上徒步旅行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这个世界真是\n',
            '变得越来越方便了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这也多亏了女王陛下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x00FE, 0)
    TalkEnd(0x00FE)

    Return()

# id: 0x0011 offset: 0x23BB
@scena.Code('func_11_23BB')
def func_11_23BB():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_2415',
    )

    ChrTalk(
        0x00FE,
        (
            '代表港口的人物，\n',
            '还有推进旅游业的实业家。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '究竟谁会在选举中获胜呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2484')

    def _loc_2415(): pass

    label('loc_2415')

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    ChrTalk(
        0x00FE,
        (
            '卢安正在\n',
            '进行市长选举呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '港口的负责人和酒店的老板\n',
            '似乎都是候选人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '究竟谁会在选举中获胜呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2484(): pass

    label('loc_2484')

    ChrSetSubChip(0x00FE, 0)
    TalkEnd(0x00FE)

    Return()

# id: 0x0012 offset: 0x248D
@scena.Code('func_12_248D')
def func_12_248D():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_24C3',
    )

    ChrTalk(
        0x00FE,
        (
            '那个戴尔蒙市长事件\n',
            '真是令人震惊啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_254E')

    def _loc_24C3(): pass

    label('loc_24C3')

    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    ChrTalk(
        0x00FE,
        (
            '呼，接下来是卢安吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说到卢安市…\n',
            '戴尔蒙市长被捕一事\n',
            '可真是冲击性的事件啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '事件之后市民们\n',
            '似乎也相当动摇，\n',
            '这也难怪吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_254E(): pass

    label('loc_254E')

    TalkEnd(0x00FE)

    Return()

# id: 0x0013 offset: 0x2552
@scena.Code('func_13_2552')
def func_13_2552():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_25B9',
    )

    ChrTalk(
        0x00FE,
        (
            '虽说是空贼团，\n',
            '但要是没有飞船也就不足为惧了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '利贝尔通讯上\n',
            '也写着危险性很低呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_262F')

    def _loc_25B9(): pass

    label('loc_25B9')

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    ChrTalk(
        0x00FE,
        (
            '真是的，爷爷\n',
            '担心过头了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽说是空贼团，\n',
            '但他们已经没有飞船了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '利贝尔通讯上\n',
            '也写着危险性很低呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_262F(): pass

    label('loc_262F')

    ChrSetSubChip(0x00FE, 0)
    TalkEnd(0x00FE)

    Return()

# id: 0x0014 offset: 0x2638
@scena.Code('func_14_2638')
def func_14_2638():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_2690',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然空贼团逃亡到国外\n',
            '的可能性似乎很高……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……但还是有点不安啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_26DF')

    def _loc_2690(): pass

    label('loc_2690')

    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))

    ChrTalk(
        0x00FE,
        (
            '说起来，空贼团一党\n',
            '好像还没被逮捕吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '难道…\n',
            '还会再来袭击我们吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_26DF(): pass

    label('loc_26DF')

    TalkEnd(0x00FE)

    Return()

# id: 0x0015 offset: 0x26E3
@scena.Code('func_15_26E3')
def func_15_26E3():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Return,
        ),
        'loc_2754',
    )

    ChrTalk(
        0x00FE,
        (
            '毕竟在利贝尔王国以外，\n',
            '飞船还是特殊的交通工具嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '像这样市民能平常地\n',
            '搭乘真是令人惊讶啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_27DE')

    def _loc_2754(): pass

    label('loc_2754')

    SetScenaFlags(ScenaFlag(0x0001, 5, 0xD))

    ChrTalk(
        0x00FE,
        (
            '呼……\n',
            '利贝尔王国果然好厉害啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在我的故乡共和国，\n',
            '飞船还是特殊的交通工具呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '像这样子市民能平常地\n',
            '搭乘真是令人惊讶啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_27DE(): pass

    label('loc_27DE')

    ChrSetSubChip(0x00FE, 0)
    TalkEnd(0x00FE)

    Return()

# id: 0x0016 offset: 0x27E7
@scena.Code('func_16_27E7')
def func_16_27E7():
    TalkBegin(0x00FE)
    ChrClearFlags(0x00FE, 0x0010)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    If(
        (
            (Expr.PushLong, 0x1E),
            (Expr.GetChrWork, 0xFE, 0x4),
            Expr.Lss,
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x96),
            Expr.Lss,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2817',
    )

    ChrSetSubChip(0x00FE, 2)

    Jump('loc_283D')

    def _loc_2817(): pass

    label('loc_2817')

    If(
        (
            (Expr.PushLong, 0xD2),
            (Expr.GetChrWork, 0xFE, 0x4),
            Expr.Lss,
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x14A),
            Expr.Lss,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2838',
    )

    ChrSetSubChip(0x00FE, 1)

    Jump('loc_283D')

    def _loc_2838(): pass

    label('loc_2838')

    ChrSetSubChip(0x00FE, 0)

    def _loc_283D(): pass

    label('loc_283D')

    ChrSetDirection(0x00FE, 0, 0)
    ChrSetFlags(0x00FE, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0241, 5, 0x120D)),
            Expr.Return,
        ),
        'loc_28D4',
    )

    ChrTalk(
        0x00FE,
        (
            '#0030200707V#020F艾丝蒂尔，散步倒无所谓，\n',
            '可别忘了我们要在卢安下船哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030200708V着陆前会有广播提醒的，\n',
            '一定要回座位哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A1C')

    def _loc_28D4(): pass

    label('loc_28D4')

    SetScenaFlags(ScenaFlag(0x0241, 5, 0x120D))

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ChrTalk(
        0x00FE,
        (
            '#0030200709V#020F哎呀，艾丝蒂尔。\n',
            '散完步了吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030200710V离到达\n',
            '还有一段时间呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200669V#1015F嗯，说得也是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200712V#1011F那就再稍微\n',
            '走走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0030200713V#020F散步倒无所谓，\n',
            '可别忘了在卢安下船哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030200708V着陆前会有广播提醒的，\n',
            '一定要回座位哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200715V#1006F嗯，知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2A1C(): pass

    label('loc_2A1C')

    ChrSetSubChip(0x00FE, 0)
    TalkEnd(0x00FE)

    Return()

# id: 0x0017 offset: 0x2A25
@scena.Code('func_17_2A25')
def func_17_2A25():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0241, 5, 0x120D)),
            Expr.Return,
        ),
        'loc_2AB3',
    )

    TalkBegin(0x00FE)
    OP_62(0x00FE, 0x00000000, 2000, 0x1C, 0x21, 0x000000FA, 0x00)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '#0050200716V#053F……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_63(0x00FE)

    ChrTalk(
        0x0101,
        (
            '#0010200717V#1015F（睡得这么熟\n',
            '也够值得尊敬了。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Jump('loc_2B57')

    def _loc_2AB3(): pass

    label('loc_2AB3')

    SetScenaFlags(ScenaFlag(0x0241, 5, 0x120D))

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    TalkBegin(0x00FE)
    OP_62(0x00FE, 0x00000000, 2000, 0x1C, 0x21, 0x000000FA, 0x00)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '#0050200716V#053F……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_63(0x00FE)
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010200719V#1019F（已、已经睡熟了……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    def _loc_2B57(): pass

    label('loc_2B57')

    Return()

# id: 0x0018 offset: 0x2B58
@scena.Code('func_18_2B58')
def func_18_2B58():
    EventBegin(0x00)
    OP_0D()
    PlaySE(166, 0x00, 0x64)
    Sleep(500)

    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('女性的声音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0880200720V……久等了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0880200721V本船即将\n',
            '抵达卢安市。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0880200722V着陆时会有少许摇晃，\n',
            '请尽快回到座位上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    ChrTalk(
        0x0101,
        (
            '#0010200723V#1004F啊，不好。\n',
            '要早点回座位才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(72, 320, 56, 3)
    NewScene('ED6_DT21/T2102._SN', 100, 0, 0)
    IdleLoop()

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
