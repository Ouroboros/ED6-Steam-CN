import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T0410_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0410   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T0410.x'
    header.mapIndex       = 13
    header.bgm            = 15
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
        ('ED6_DT26/CH20331._CH', 'ED6_DT26/CH20331P._CP'),
        ('ED6_DT26/CH20336._CH', 'ED6_DT26/CH20336P._CP'),
        ('ED6_DT27/CH03080._CH', 'ED6_DT27/CH03080P._CP'),
        ('ED6_DT06/CH20020._CH', 'ED6_DT06/CH20020P._CP'),
        ('ED6_DT26/CH20313._CH', 'ED6_DT26/CH20313P._CP'),
        ('ED6_DT26/CH20314._CH', 'ED6_DT26/CH20314P._CP'),
        ('ED6_DT07/CH02480._CH', 'ED6_DT07/CH02480P._CP'),
        ('ED6_DT07/CH01060._CH', 'ED6_DT07/CH01060P._CP'),
        ('ED6_DT07/CH01070._CH', 'ED6_DT07/CH01070P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH01030._CH', 'ED6_DT07/CH01030P._CP'),
    ]

# id: 0x10001 offset: 0x102
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '缇欧',
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
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '维鲁',
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
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '查儿',
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
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '弗兰兹',
            x                   = 500,
            z                   = 0,
            y                   = 35040,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            name                = '汉娜',
            x                   = 1320,
            z                   = 0,
            y                   = 37500,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '凯文神父',
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
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '维鲁',
            x                   = 80,
            z                   = 0,
            y                   = 32400,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '查儿',
            x                   = 500,
            z                   = 0,
            y                   = 35060,
            direction           = 270,
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
            name                = '弗兰兹',
            x                   = -76340,
            z                   = 0,
            y                   = 31640,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 458753,
            chipIndex           = 1,
            npcIndex            = 0x0187,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '汉娜',
            x                   = -73490,
            z                   = 0,
            y                   = 31660,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1507329,
            chipIndex           = 1,
            npcIndex            = 0x0187,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '器皿',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 196611,
            chipIndex           = 3,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '器皿',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 196611,
            chipIndex           = 3,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '器皿',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 196611,
            chipIndex           = 3,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '器皿',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 196611,
            chipIndex           = 3,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '器皿',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 196611,
            chipIndex           = 3,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '沙拉',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 458755,
            chipIndex           = 3,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '面包',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1769475,
            chipIndex           = 3,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x322
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x322
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x322
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x322
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            (Expr.TestScenaFlags, ScenaFlag(0x0307, 3, 0x183B)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_335',
    )

    Jump('loc_3F9')

    def _loc_335(): pass

    label('loc_335')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3F9',
    )

    ChrSetPos(0x000D, -75610, 0, 2580, 270)
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x0008, 0xFF)
    ChrSetPos(0x0008, -77060, 0, 3150, 180)
    ChrSetPos(0x000A, -73600, 0, 2980, 180)
    ChrSetPos(0x0009, -72950, 0, 2980, 180)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetFlags(0x000A, 0x0004)
    ChrSetFlags(0x0009, 0x0004)
    ChrSetFlags(0x0008, 0x0004)
    ChrSetFlags(0x000A, 0x0002)
    ChrSetFlags(0x0009, 0x0002)
    ChrSetFlags(0x0008, 0x0002)
    ChrSetChipByIndex(0x000A, 1)
    ChrSetSubChip(0x000A, 55)
    ChrSetChipByIndex(0x0009, 1)
    ChrSetSubChip(0x0009, 71)
    ChrSetChipByIndex(0x0008, 1)
    ChrSetSubChip(0x0008, 39)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000C, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0011, 0x0080)

    def _loc_3F9(): pass

    label('loc_3F9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_42F',
    )

    ChrSetPos(0x000B, -39020, 0, 33240, 180)
    ChrClearFlags(0x000E, 0x0080)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x000F, 3820, 0, 24640, 155)

    Jump('loc_43B')

    def _loc_42F(): pass

    label('loc_42F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_43B',
    )

    ChrSetFlags(0x000B, 0x0080)

    def _loc_43B(): pass

    label('loc_43B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_455',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0xA),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    Event(0, func_14_41CC)

    Jump('loc_471')

    def _loc_455(): pass

    label('loc_455')

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x66),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_471',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 1, 0x1821)),
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_471',
    )

    Event(0, func_09_2104)

    def _loc_471(): pass

    label('loc_471')

    Return()

# id: 0x0001 offset: 0x472
@scena.Code('func_01_472')
def func_01_472():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 1, 0x1821)),
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_487',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x51),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_487(): pass

    label('loc_487')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            (Expr.TestScenaFlags, ScenaFlag(0x0307, 3, 0x183B)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_49A',
    )

    Jump('loc_4C6')

    def _loc_49A(): pass

    label('loc_49A')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4C6',
    )

    OP_6F(0x0005, 20)
    OP_6F(0x0006, 20)
    OP_6F(0x0007, 20)
    OP_6F(0x0008, 20)

    def _loc_4C6(): pass

    label('loc_4C6')

    Return()

# id: 0x0002 offset: 0x4C7
@scena.Code('func_02_4C7')
def func_02_4C7():
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
        'loc_4EC',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_62E')

    def _loc_4EC(): pass

    label('loc_4EC')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_505',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_62E')

    def _loc_505(): pass

    label('loc_505')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_51E',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_62E')

    def _loc_51E(): pass

    label('loc_51E')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_537',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_62E')

    def _loc_537(): pass

    label('loc_537')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_550',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_62E')

    def _loc_550(): pass

    label('loc_550')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_569',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_62E')

    def _loc_569(): pass

    label('loc_569')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_582',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_62E')

    def _loc_582(): pass

    label('loc_582')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_59B',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_62E')

    def _loc_59B(): pass

    label('loc_59B')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5B4',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_62E')

    def _loc_5B4(): pass

    label('loc_5B4')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5CD',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_62E')

    def _loc_5CD(): pass

    label('loc_5CD')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5E6',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_62E')

    def _loc_5E6(): pass

    label('loc_5E6')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5FF',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_62E')

    def _loc_5FF(): pass

    label('loc_5FF')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_618',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_62E')

    def _loc_618(): pass

    label('loc_618')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_62E',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_62E(): pass

    label('loc_62E')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_643',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_62E')

    def _loc_643(): pass

    label('loc_643')

    Return()

# id: 0x0003 offset: 0x644
@scena.Code('func_03_644')
def func_03_644():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_C65',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0415, 2, 0x20AA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_9FA',
    )

    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '喔！艾丝蒂尔、约修亚，\n',
            '你们回来了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1000F嗯！在协会\n',
            '有些工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1040F好久不见了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '啊啊，真的是好久好久了呢，\n',
            '你们看起来很有精神嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯……这样的话～\n',
            '看来洛连特还有希望啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_75F',
    )

    ChrTalk(
        0x0103,
        (
            '#021F呵呵，那样的话当然好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_75F(): pass

    label('loc_75F')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7BE',
    )

    ChrTalk(
        0x0106,
        (
            '#555F真是位会说话的大叔啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#051F算了，这些家伙确实\n',
            '也比以前进步了不少……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7BE(): pass

    label('loc_7BE')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7FE',
    )

    ChrTalk(
        0x0108,
        (
            '#071F哈哈，果然是家乡的人啊，\n',
            '期待度很高啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7FE(): pass

    label('loc_7FE')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_816',
    )

    ChrTurnDirection(0x00FE, 0x0108, 400)

    Jump('loc_843')

    def _loc_816(): pass

    label('loc_816')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_82E',
    )

    ChrTurnDirection(0x00FE, 0x0106, 400)

    Jump('loc_843')

    def _loc_82E(): pass

    label('loc_82E')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_843',
    )

    ChrTurnDirection(0x00FE, 0x0103, 400)

    def _loc_843(): pass

    label('loc_843')

    ChrTalk(
        0x00FE,
        (
            '大家都处在困境中呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '期待当地的游击士\n',
            '也是理所当然的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '虽然现在的状况\n',
            '确实很辛苦，\n',
            '但我们还是可以继续努力的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '农业类的工作，本来就是\n',
            '靠手工作业来完成的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1015F确实呢，以前根本\n',
            '就没有机械可以使用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只是没有定期船的话，\n',
            '运送工作就没办法做了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '盼望早日恢复原状的心情，\n',
            '我们大家都是一样的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1006F嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '虽然很困难，\n',
            '但我们一定会努力的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1040F大叔也要加油啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊啊，交给我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0415, 2, 0x20AA))

    Jump('loc_C62')

    def _loc_9FA(): pass

    label('loc_9FA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 5, 0x2085)),
            Expr.Return,
        ),
        'loc_B2E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_ACF',
    )

    ChrTalk(
        0x00FE,
        (
            '导力式的燃炉无法使用了，\n',
            '汉娜也很苦恼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天晚上只能像前人那样\n',
            '用火炉来做料理了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '话虽如此，但孩子们好像\n',
            '反而很喜欢火炉呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '到时大概还会像以前一样高兴地\n',
            '围着火炉转个不停。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Jump('loc_B2B')

    def _loc_ACF(): pass

    label('loc_ACF')

    ChrTalk(
        0x00FE,
        (
            '导力式的燃炉无法使用了，\n',
            '汉娜也很苦恼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天晚上只能像前人那样\n',
            '用火炉来做料理了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B2B(): pass

    label('loc_B2B')

    Jump('loc_C62')

    def _loc_B2E(): pass

    label('loc_B2E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_BF6',
    )

    ChrTalk(
        0x00FE,
        (
            '以手工作业的方式来完成\n',
            '农场的工作倒是小事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但没有定期船的话，\n',
            '种出的蔬菜就没办法运走。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们看看吧，\n',
            '这么多农作物都堆在这！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '再这样下去的话，\n',
            '岂不是全要烂在这里了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Jump('loc_C62')

    def _loc_BF6(): pass

    label('loc_BF6')

    ChrTalk(
        0x00FE,
        (
            '好不容易种出来的优质作物\n',
            '却运不出去，真是深受打击啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '盼望早日恢复原状的心情，\n',
            '我们大家都是一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C62(): pass

    label('loc_C62')

    Jump('loc_CD8')

    def _loc_C65(): pass

    label('loc_C65')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_CD8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0313, 7, 0x189F)),
            Expr.Return,
        ),
        'loc_CD4',
    )

    ChrTalk(
        0x00FE,
        (
            '自从协会开始调查以后\n',
            '雾更加严重了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天已经送货完毕了，\n',
            '但明天开始就很令人担心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CD8')

    def _loc_CD4(): pass

    label('loc_CD4')

    Call(0, 0x0005)

    def _loc_CD8(): pass

    label('loc_CD8')

    TalkEnd(0x000B)

    Return()

# id: 0x0004 offset: 0xCDC
@scena.Code('func_04_CDC')
def func_04_CDC():
    TalkBegin(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_104D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0415, 3, 0x20AB)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_F1F',
    )

    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '啊……\n',
            '这不是艾丝蒂尔和约修亚吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1001F您好，汉娜阿姨。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1040F一切都还好吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '啊啊～我是还好啦，\n',
            '但家里的事情可就不大好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '导力式的烹饪工具\n',
            '全都没法用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天的早餐\n',
            '只能吃凉的三明治。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '警备艇的人也来过，\n',
            '总觉得对他们很不好意思。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1015F嗯、嗯、这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '不过只要是阿姨做的三明治，\n',
            '就算是凉的肯定也很美味……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1040F我也有同感。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈哈，这么说真是\n',
            '让我高兴啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '等以后有空的话\n',
            '再来玩吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '到时候我会做好多好吃的\n',
            '料理给你们吃的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1001F嗯！非常期待！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1040F到时一定再来麻烦您。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0415, 3, 0x20AB))

    Jump('loc_104A')

    def _loc_F1F(): pass

    label('loc_F1F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 5, 0x2085)),
            Expr.Return,
        ),
        'loc_FC3',
    )

    ChrTalk(
        0x00FE,
        (
            '维鲁和查儿\n',
            '最近一直很热情地帮我做事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看来孩子们也能感觉到\n',
            '家里遇到困境了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈哈，看他们这么懂事，\n',
            '就算导力器无法使用\n',
            '也都不觉得烦恼了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_104A')

    def _loc_FC3(): pass

    label('loc_FC3')

    ChrTalk(
        0x00FE,
        (
            '导力式的烹饪工具\n',
            '无法运转了，真是麻烦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没有导力器的话，很难做出\n',
            '火候合适的料理呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，今天只有用火炉来\n',
            '烹饪料理了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_104A(): pass

    label('loc_104A')

    Jump('loc_1417')

    def _loc_104D(): pass

    label('loc_104D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_13A8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x034C, 7, 0x1A67)),
            Expr.Return,
        ),
        'loc_10CB',
    )

    ChrTalk(
        0x00FE,
        (
            '年纪轻轻却\n',
            '这么懂礼貌啊…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但有的时候太客气\n',
            '反而是失礼的行为呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好了，别人的好意\n',
            '接受就是了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_13A5')

    def _loc_10CB(): pass

    label('loc_10CB')

    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x00FE, 0x0101, 0)
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '艾丝蒂尔，雪拉小姐，\n',
            '你们终于来了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最近一段时间\n',
            '经常受你们的照顾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这点小意思请收下，\n',
            '是我们自制的茶。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1008F这、这个……\n',
            '我们不能收啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '帮助阿姨的是\n',
            '凯文神父。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈哈哈，给你们也是\n',
            '一样的啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那位神父先生\n',
            '也是不肯收。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1016F啊……\n',
            '是、是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '都不是外人了，\n',
            '不用那么客气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '别人的好意，接受就对了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#020F快收下吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '不然汉娜阿姨\n',
            '会不高兴哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1015F啊、嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1000F……那、就不客气了。',
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
            (TxtCtl.Item, ItemTable['清凉药草茶']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(ItemTable['清凉药草茶'], 1)

    ChrTalk(
        0x00FE,
        (
            '疲劳的时候喝下它的话\n',
            '就会精力十足的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1018F阿姨，谢谢啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x00FE, 400)

    ChrTalk(
        0x0103,
        (
            '#021F呵呵，那就谢谢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0103, 400)

    ChrTalk(
        0x00FE,
        (
            '这点小意思不用放在心上的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '以后有空的话\n',
            '还要再来玩啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x034C, 7, 0x1A67))

    def _loc_13A5(): pass

    label('loc_13A5')

    Jump('loc_1417')

    def _loc_13A8(): pass

    label('loc_13A8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_1417',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0313, 7, 0x189F)),
            Expr.Return,
        ),
        'loc_1413',
    )

    ChrTalk(
        0x00FE,
        (
            '我们出去送货的时候\n',
            '雾还没这么厉害呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，这样的话就不能再让\n',
            '孩子们跑出去玩了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1417')

    def _loc_1413(): pass

    label('loc_1413')

    Call(0, 0x0005)

    def _loc_1417(): pass

    label('loc_1417')

    TalkEnd(0x000C)

    Return()

# id: 0x0005 offset: 0x141B
@scena.Code('func_05_141B')
def func_05_141B():
    OP_4A(0x000C, 255)
    OP_4A(0x000B, 255)

    If(
        (
            (Expr.Eval, "OP_CD(0x000B)"),
            Expr.Return,
        ),
        'loc_14AC',
    )

    ChrTalk(
        0x000B,
        (
            '哎呀，这不是艾丝蒂尔吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000C, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    OP_63(0x000C)
    ChrTurnDirection(0x000C, 0x0101, 400)

    ChrTalk(
        0x000C,
        (
            '艾丝蒂尔？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '哎呀，真的是啊。\n',
            '好久不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x000C, 400)

    Jump('loc_1520')

    def _loc_14AC(): pass

    label('loc_14AC')

    If(
        (
            (Expr.Eval, "OP_CD(0x000C)"),
            Expr.Return,
        ),
        'loc_1520',
    )

    ChrTalk(
        0x000C,
        (
            '啊，这不是艾丝蒂尔吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000B, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    OP_63(0x000B)
    ChrTurnDirection(0x000B, 0x0101, 400)

    ChrTalk(
        0x000B,
        (
            '喔，好久不见了，\n',
            '身体还好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x000B, 400)

    def _loc_1520(): pass

    label('loc_1520')

    ChrTalk(
        0x0101,
        (
            '#1017F嘿嘿，好久不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '是从洛连特来的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '街道上起了大雾，\n',
            '什么都看不清楚了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x000B, 400)

    ChrTalk(
        0x0101,
        (
            '#1015F嗯，其实我们就是\n',
            '为了调查这雾而来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '那可辛苦你啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '艾丝蒂尔已经变成一位\n',
            '很厉害的游击士了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000C, 0x0103, 400)

    ChrTalk(
        0x000C,
        (
            '这也是因为有优秀前辈\n',
            '的指导吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x000C, 400)

    ChrTalk(
        0x0103,
        (
            '#021F呵呵，主要还是因为本人的努力啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '虽然在研修时确实费了不少力气，\n',
            '但我并没教她什么重要的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#1008F才不是那样的呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '雪拉姐不管在什么时候\n',
            '都一直指导着我… ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '两个人都很了不起，\n',
            '你们都做得很好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '今后也要继续加油啊，\n',
            '我们会永远支持你们的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x000B, 400)

    ChrTalk(
        0x0101,
        (
            '#1006F谢谢！我会加油的⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '嗯，也要小心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_177B')
    def lambda_177B():
        ChrSetDirection(0x000C, 0, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_177B)

    ChrSetDirection(0x000B, 180, 400)
    OP_4B(0x000C, 255)
    OP_4B(0x000B, 255)
    SetScenaFlags(ScenaFlag(0x0313, 7, 0x189F))

    Return()

# id: 0x0006 offset: 0x1796
@scena.Code('func_06_1796')
def func_06_1796():
    TalkBegin(0x000D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 3, 0x1823)),
            Expr.Return,
        ),
        'loc_1AA8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0313, 6, 0x189E)),
            Expr.Return,
        ),
        'loc_1849',
    )

    ChrTalk(
        0x000D,
        (
            '#0180290716V#1068F不过，在这种状况下\n',
            '去森林吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180290717V本来就是很容易迷路的地方，\n',
            '这下更加危险了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180290718V#1066F艾丝蒂尔，\n',
            '你们一定要小心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AA5')

    def _loc_1849(): pass

    label('loc_1849')

    ChrTalk(
        0x000D,
        (
            '#0180290719V#1060F啊，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180290720V好像已经向协会\n',
            '报告完毕了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290721V#1002F缇欧她们怎么样了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x000D,
        (
            '#0180290722V#1060F放心。\n',
            '大家都只是睡着了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180290723V调查进展得如何了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030290724V#022F虽然还不能确定，\n',
            '但发现了可疑的地方。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290725V接下来准备\n',
            '前去探查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290726V#1015F神秘森林就是\n',
            '东南部的大森林，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0180290727V#1065F神秘森林……\n',
            '利贝尔最大的森林地带啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180290728V#1063F做好准备之后\n',
            '再过去吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180290729V那里视线很差，\n',
            '要谨慎前进啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290730V#1006F凯文神父也是。\n',
            '缇欧就拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0180290731V#1060F喔！放心交给我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0313, 6, 0x189E))

    def _loc_1AA5(): pass

    label('loc_1AA5')

    Jump('loc_1C01')

    def _loc_1AA8(): pass

    label('loc_1AA8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_1C01',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1BA2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_1B27',
    )

    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x000D,
        (
            '#0180290732V#1060F这也是神父的工作之一啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180290733V这里就交给我。\n',
            '你们赶快回协会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B9F')

    def _loc_1B27(): pass

    label('loc_1B27')

    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x000D,
        (
            '#0180290734V#1064F怎么啦，艾丝蒂尔。\n',
            '还没回协会吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180290735V#1060F这里就交给我，\n',
            '你们赶快回协会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_1B9F(): pass

    label('loc_1B9F')

    Jump('loc_1C01')

    def _loc_1BA2(): pass

    label('loc_1BA2')

    ChrTalk(
        0x000D,
        (
            '#0180290732V#1060F这也是神父的工作之一啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180290733V这里就交给我。\n',
            '你们赶快回协会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C01(): pass

    label('loc_1C01')

    TalkEnd(0x000D)

    Return()

# id: 0x0007 offset: 0x1C05
@scena.Code('func_07_1C05')
def func_07_1C05():
    TalkBegin(0x000E)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1E21',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0415, 5, 0x20AD)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1CE8',
    )

    OP_62(0x00FE, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrTurnDirection(0x00FE, 0x0102, 0)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '啊！！约修亚哥哥！！\n',
            '是来找我玩的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1040F呀啊！你还好吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '可是，抱歉。\n',
            '现在还在工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉、真没意思…\n',
            '还想和你一起玩呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1049F哈哈，下次吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))
    SetScenaFlags(ScenaFlag(0x0415, 5, 0x20AD))

    Jump('loc_1E21')

    def _loc_1CE8(): pass

    label('loc_1CE8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 5, 0x2085)),
            Expr.Return,
        ),
        'loc_1DE5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_1D23',
    )

    ChrTurnDirection(0x00FE, 0x0102, 0)

    ChrTalk(
        0x00FE,
        (
            '约修亚哥哥！\n',
            '下次再来玩啊～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1DE2')

    def _loc_1D23(): pass

    label('loc_1D23')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1D9C',
    )

    ChrTurnDirection(0x00FE, 0x0102, 0)

    ChrTalk(
        0x00FE,
        (
            '啊！约修亚还有艾丝蒂尔，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我现在正在帮\n',
            '爸爸干活，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '导力器不能用了，\n',
            '有好多工作得做呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Jump('loc_1DE2')

    def _loc_1D9C(): pass

    label('loc_1D9C')

    ChrTalk(
        0x00FE,
        (
            '我现在正在帮\n',
            '爸爸干活，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '导力器不能用了，\n',
            '有好多工作得做呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1DE2(): pass

    label('loc_1DE2')

    Jump('loc_1E21')

    def _loc_1DE5(): pass

    label('loc_1DE5')

    ChrTurnDirection(0x00FE, 0x0102, 0)

    ChrTalk(
        0x00FE,
        (
            '约修亚哥哥！\n',
            '下次再来玩啊～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要再来玩哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1E21(): pass

    label('loc_1E21')

    TalkEnd(0x000E)

    Return()

# id: 0x0008 offset: 0x1E25
@scena.Code('func_08_1E25')
def func_08_1E25():
    TalkBegin(0x000F)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_2100',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0415, 4, 0x20AC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1F75',
    )

    ChrTurnDirection(0x00FE, 0x0102, 0)

    ChrTalk(
        0x00FE,
        (
            '啊……约修亚……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1040F呀，查儿。\n',
            '还好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，嗯……\n',
            '查儿很有精神呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在也在帮妈妈\n',
            '干活…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不好好干活的话\n',
            '可就不妙了… ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1040F是吗……\n',
            '要加油啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊，约修亚也\n',
            '在做什么工作了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1040F嗯、是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '不过，用不了不久\n',
            '我就会再过来玩了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯、嗯！！那我等你。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))
    SetScenaFlags(ScenaFlag(0x0415, 4, 0x20AC))

    Jump('loc_2100')

    def _loc_1F75(): pass

    label('loc_1F75')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 5, 0x2085)),
            Expr.Return,
        ),
        'loc_20C4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_1FC2',
    )

    ChrTurnDirection(0x00FE, 0x0102, 0)

    ChrTalk(
        0x00FE,
        (
            '约修亚……\n',
            '一定再来玩啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '查儿会等你的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_20C1')

    def _loc_1FC2(): pass

    label('loc_1FC2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_206F',
    )

    ChrTalk(
        0x00FE,
        (
            '啊，约修亚……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那个、昨天\n',
            '士兵先生来家里了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '查儿和妈妈给他们\n',
            '做了三明治。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '士兵先生们… \n',
            '很高兴呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '下、下次也想……\n',
            '做给约修亚吃呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    Jump('loc_20C1')

    def _loc_206F(): pass

    label('loc_206F')

    ChrTalk(
        0x00FE,
        (
            '查儿的三明治，\n',
            '士兵先生们都很喜欢的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '下、下次也想……\n',
            '做给约修亚吃呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_20C1(): pass

    label('loc_20C1')

    Jump('loc_2100')

    def _loc_20C4(): pass

    label('loc_20C4')

    ChrTurnDirection(0x00FE, 0x0102, 0)

    ChrTalk(
        0x00FE,
        (
            '约修亚……\n',
            '一定再来玩啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '查儿会等你的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2100(): pass

    label('loc_2100')

    TalkEnd(0x000F)

    Return()

# id: 0x0009 offset: 0x2104
@scena.Code('func_09_2104')
def func_09_2104():
    EventBegin(0x00)
    ChrSetPos(0x0018, 400, 800, 27970, 0)
    ChrSetPos(0x0017, -910, 800, 27970, 0)
    ChrSetPos(0x0012, -1340, 800, 28000, 0)
    ChrSetPos(0x0013, -940, 800, 27500, 0)
    ChrSetPos(0x0014, 890, 800, 27500, 0)
    ChrSetPos(0x0015, -760, 800, 28500, 0)
    ChrSetPos(0x0016, 830, 800, 28500, 0)
    ChrClearFlags(0x0018, 0x0080)
    ChrClearFlags(0x0017, 0x0080)
    ChrClearFlags(0x0012, 0x0080)
    ChrClearFlags(0x0013, 0x0080)
    ChrClearFlags(0x0014, 0x0080)
    ChrClearFlags(0x0015, 0x0080)
    ChrClearFlags(0x0016, 0x0080)
    OP_4A(0x000B, 255)
    OP_4A(0x000A, 255)
    OP_4A(0x0009, 255)
    OP_4A(0x0008, 255)
    OP_4A(0x000C, 255)
    ChrSetFlags(0x000B, 0x0004)
    ChrSetFlags(0x000A, 0x0004)
    ChrSetFlags(0x0009, 0x0004)
    ChrSetPos(0x000B, -2170, 0, 28020, 90)
    ChrSetPos(0x000A, -960, 200, 26970, 0)
    ChrSetPos(0x0009, 940, 200, 27000, 0)
    ChrSetPos(0x0008, 1730, 0, 31540, 270)
    ChrSetPos(0x000C, 1220, 0, 36190, 0)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x0008, 0x0001)
    ChrClearFlags(0x000C, 0x0001)
    ChrSetFlags(0x000B, 0x0002)
    ChrSetFlags(0x000A, 0x0002)
    ChrSetFlags(0x0009, 0x0002)
    ChrSetFlags(0x0008, 0x0002)
    ChrSetFlags(0x000C, 0x0002)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0103, 0x0080)
    ChrSetFlags(0x0107, 0x0080)
    ChrSetFlags(0x0105, 0x0080)
    ChrSetPos(0x0101, -5790, 0, 24110, 90)
    ChrSetPos(0x0103, -5790, 0, 24110, 90)
    ChrSetPos(0x0107, -5790, 0, 24110, 90)
    ChrSetPos(0x0105, -5790, 0, 24110, 90)
    ChrSetChipByIndex(0x000B, 0)
    ChrSetSubChip(0x000B, 5)
    ChrSetChipByIndex(0x000A, 0)
    ChrSetSubChip(0x000A, 27)
    ChrSetChipByIndex(0x0009, 0)
    ChrSetSubChip(0x0009, 35)
    ChrSetChipByIndex(0x0008, 0)
    ChrSetSubChip(0x0008, 16)
    ChrSetChipByIndex(0x000C, 0)
    ChrSetSubChip(0x000C, 9)
    CameraMove(-5540, 0, 24290, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    FadeIn(1000, 0)
    OP_0D()
    OP_6F(0x0000, 0)
    OP_70(0x0000, 59)
    OP_73(0x0000)
    Sleep(500)

    @scena.Lambda('lambda_2341')
    def lambda_2341():
        CameraMove(-3970, 0, 25940, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2341)

    CreateThread(0x0101, 0x01, 0x00, func_0A_28AC)
    Sleep(500)

    CreateThread(0x0103, 0x01, 0x00, func_0B_28FE)
    Sleep(500)

    CreateThread(0x0105, 0x01, 0x00, func_0D_29C2)
    Sleep(500)

    CreateThread(0x0107, 0x01, 0x00, func_0C_2950)
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010290609V#1020F#6P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0107, 0x0001)

    @scena.Lambda('lambda_23B4')
    def lambda_23B4():
        CameraMove(-2470, 0, 27900, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_23B4)

    @scena.Lambda('lambda_23CC')
    def lambda_23CC():
        ChrWalkTo(0x00FE, -2040, 0, 26810, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_23CC)

    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010290610V#1020F#6P弗兰兹叔叔！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_241A')
    def lambda_241A():
        ChrSetDirection(0x00FE, 100, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_241A)

    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010290611V#1020F#5P查儿、维鲁！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0103, 0x01, 0x00, func_0E_2A14)
    CreateThread(0x0107, 0x01, 0x00, func_10_2A9C)
    CreateThread(0x0105, 0x01, 0x00, func_0F_2A7B)

    @scena.Lambda('lambda_246B')
    def lambda_246B():
        CameraMove(-40, 0, 31820, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_246B)

    ChrWalkTo(0x0101, -3200, 0, 27110, 5000, 0x00)
    ChrWalkTo(0x0101, -3090, 0, 29850, 5000, 0x00)
    ChrWalkTo(0x0101, -2190, 0, 31160, 5000, 0x00)
    ChrWalkTo(0x0101, -70, 0, 32170, 5000, 0x00)
    ChrSetDirection(0x0101, 90, 600)
    Sleep(500)

    ChrSetDirection(0x0101, 0, 600)
    Sleep(500)

    ChrSetDirection(0x0101, 90, 600)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010290612V#1020F#5P缇欧！\n',
            '汉娜阿姨！！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290613V#1027F……骗人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    PlaySE(209, 0x00, 0x50)
    ChrSetFlags(0x0101, 0x0002)
    ChrSetChipByIndex(0x0101, 4)
    ChrSetSubChip(0x0101, 0)
    OP_0D()
    Sleep(1500)

    ChrTalk(
        0x0105,
        (
            '#0060290614V#049F#5P不妙……\n',
            '都昏睡过去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0107, 0x0101, 400)
    Sleep(500)

    ChrTalk(
        0x0107,
        (
            '#0070290615V#561F#6P嗯……这孩子也是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290616V#1003F……呜…………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290617V#1027F又……\n',
            '又没能赶上吗……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060231069V#043F#5P艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070290619V#063F姐、姐姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(7, 0x00, 0x64)
    Sleep(500)

    ChrClearFlags(0x0103, 0x0080)

    @scena.Lambda('lambda_267A')
    def lambda_267A():
        CameraMove(320, 0, 28710, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_267A)

    @scena.Lambda('lambda_2692')
    def lambda_2692():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0002, lambda_2692)

    ChrWalkTo(0x0103, 1040, 0, 24410, 2500, 0x00)
    WaitForThreadExit(0x0101, 0x0002)
    Sleep(200)

    ChrTalk(
        0x0103,
        (
            '#0030290620V#522F#6P没办法啊……\n',
            '又被对方逃走了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290621V我们的行动\n',
            '似乎完全都在她的掌握中呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_272C')
    def lambda_272C():
        ChrTurnDirection(0x00FE, 0x0103, 400)
        Yield()

        Jump('lambda_272C')

    DispatchAsync2(0x0105, 0x0001, lambda_272C)

    Sleep(100)

    @scena.Lambda('lambda_2742')
    def lambda_2742():
        ChrTurnDirection(0x00FE, 0x0103, 400)
        Yield()

        Jump('lambda_2742')

    DispatchAsync2(0x0107, 0x0001, lambda_2742)

    Sleep(400)

    ChrTalk(
        0x0105,
        (
            '#0060290622V#042F#5P『黑衣女子』吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030290623V#022F#6P……嗯，没错的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_27AC')
    def lambda_27AC():
        CameraMove(-40, 0, 31820, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_27AC)

    ChrWalkTo(0x0103, 3820, 0, 25000, 3000, 0x00)
    ChrWalkTo(0x0103, 3820, 0, 30870, 3000, 0x00)
    ChrTurnDirection(0x0103, 0x0101, 400)
    TerminateThread(0x0105, 0x01)
    TerminateThread(0x0107, 0x01)
    ChrSetDirection(0x0105, 0, 400)
    ChrSetDirection(0x0107, 0, 400)
    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0103,
        (
            '#0030290624V#022F#4P艾丝蒂尔……\n',
            '先把大家都抬到床上吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290625V你来带路。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0101, 0x00, 0x07, 1000)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010290626V#1027F#5P啊……嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000007D0)
    FadeOut(1500, 0, -1)
    OP_0D()
    Sleep(500)

    Call(0, 0x0011)

    Return()

# id: 0x000A offset: 0x28AC
@scena.Code('func_0A_28AC')
def func_0A_28AC():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_28C2')
    def lambda_28C2():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_28C2)

    ChrWalkTo(0x00FE, -4210, 0, 24080, 2500, 0x00)
    ChrWalkTo(0x00FE, -2270, 0, 25560, 2500, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x000B offset: 0x28FE
@scena.Code('func_0B_28FE')
def func_0B_28FE():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_2914')
    def lambda_2914():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2914)

    ChrWalkTo(0x00FE, -4210, 0, 24080, 2500, 0x00)
    ChrWalkTo(0x00FE, -1390, 0, 24140, 2500, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x000C offset: 0x2950
@scena.Code('func_0C_2950')
def func_0C_2950():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_2966')
    def lambda_2966():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2966)

    ChrWalkTo(0x00FE, -4210, 0, 24080, 2500, 0x00)
    OP_72(0x0000, 0x0800)
    OP_6F(0x0000, 59)
    OP_70(0x0000, 0)
    OP_23(0x0006)
    PlaySE(7, 0x00, 0x64)
    ChrWalkTo(0x00FE, -2970, 0, 25020, 2500, 0x00)
    ChrSetDirection(0x00FE, 0, 400)
    OP_71(0x0000, 0x0800)

    Return()

# id: 0x000D offset: 0x29C2
@scena.Code('func_0D_29C2')
def func_0D_29C2():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_29D8')
    def lambda_29D8():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_29D8)

    ChrWalkTo(0x00FE, -4210, 0, 24080, 2500, 0x00)
    ChrWalkTo(0x00FE, -2420, 0, 23780, 2500, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x000E offset: 0x2A14
@scena.Code('func_0E_2A14')
def func_0E_2A14():
    Sleep(1000)

    ChrSetDirection(0x00FE, 130, 400)
    ChrWalkTo(0x00FE, 1050, 0, 22090, 3000, 0x00)
    ChrSetDirection(0x00FE, 220, 400)
    Sleep(500)

    ChrSetDirection(0x00FE, 130, 400)
    Sleep(500)

    PlaySE(6, 0x00, 0x64)
    Sleep(500)

    ChrWalkTo(0x00FE, 940, 0, 19760, 3000, 0x00)
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 400)
    ChrSetFlags(0x0103, 0x0080)

    Return()

# id: 0x000F offset: 0x2A7B
@scena.Code('func_0F_2A7B')
def func_0F_2A7B():
    Sleep(2000)

    ChrWalkTo(0x00FE, -2090, 0, 27180, 2000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x0010 offset: 0x2A9C
@scena.Code('func_10_2A9C')
def func_10_2A9C():
    Sleep(1500)

    ChrWalkTo(0x00FE, -80, 0, 25840, 2000, 0x00)
    ChrWalkTo(0x00FE, -110, 0, 26790, 2000, 0x00)
    ChrSetDirection(0x00FE, 90, 400)
    Sleep(1000)

    ChrSetDirection(0x00FE, 0, 400)
    ChrSetDirection(0x00FE, 270, 400)

    Return()

# id: 0x0011 offset: 0x2AE4
@scena.Code('func_11_2AE4')
def func_11_2AE4():
    ChrSetPos(0x000B, -76340, 0, 31640, 180)
    ChrSetPos(0x000C, -73490, 0, 31660, 180)
    ChrSetPos(0x0008, -77060, 0, 3150, 180)
    ChrSetPos(0x000A, -73600, 0, 2980, 180)
    ChrSetPos(0x0009, -72950, 0, 2980, 180)
    ChrSetFlags(0x0101, 0x0004)
    ChrSetFlags(0x0107, 0x0004)
    ChrSetFlags(0x0105, 0x0004)
    ChrSetPos(0x0101, -75750, 0, 2700, 270)
    ChrSetPos(0x0103, -74780, 0, 2600, 90)
    ChrSetPos(0x0105, -75080, 0, 31410, 270)
    ChrSetPos(0x0107, -74700, 0, 32159, 90)
    ChrSetFlags(0x000B, 0x0002)
    ChrSetFlags(0x000A, 0x0002)
    ChrSetFlags(0x0009, 0x0002)
    ChrSetFlags(0x0008, 0x0002)
    ChrSetFlags(0x000C, 0x0002)
    ChrSetFlags(0x000B, 0x0004)
    ChrSetFlags(0x000A, 0x0004)
    ChrSetFlags(0x0009, 0x0004)
    ChrSetFlags(0x0008, 0x0004)
    ChrSetFlags(0x000C, 0x0004)
    ChrClearFlags(0x0101, 0x0002)
    ChrSetSubChip(0x0101, 0)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x000B, 1)
    ChrSetSubChip(0x000B, 7)
    ChrSetChipByIndex(0x000A, 1)
    ChrSetSubChip(0x000A, 55)
    ChrSetChipByIndex(0x0009, 1)
    ChrSetSubChip(0x0009, 71)
    ChrSetChipByIndex(0x0008, 1)
    ChrSetSubChip(0x0008, 39)
    ChrSetChipByIndex(0x000C, 1)
    ChrSetSubChip(0x000C, 23)
    OP_6F(0x0005, 60)
    OP_6F(0x0006, 60)
    OP_6F(0x0007, 60)
    OP_6F(0x0008, 60)
    CameraMove(-75020, 0, 33060, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    PlayBGM(83)
    Sleep(500)

    FadeIn(2000, 0)
    OP_0D()
    Sleep(1500)

    Fade(1000)
    CameraMove(-76380, 0, 4030, 0)
    OP_67(0, 4730, -10000, 0)
    CameraSetDistance(3100, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0103,
        (
            '#0030290627V#025F总算都抬到床上了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290628V#522F呼……\n',
            '接下来该怎么做好呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290629V#1027F#5P……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0103, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTurnDirection(0x0103, 0x0101, 500)
    Sleep(500)

    ChrTalk(
        0x0103,
        (
            '#0030290630V#022F艾丝蒂尔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290631V我知道你很沮丧，\n',
            '但现在必须赶快振作起来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290632V不然的话，是没办法\n',
            '让大家恢复清醒的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290633V#1027F#5P……可是……\n',
            '全都是因为我的不成熟才……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290634V我现在…还是连老爸的脚底都及不上……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290635V所以才会让缇欧她们\n',
            '遭遇到这种事情……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030290636V#023F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 90, 600)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010290637V#1023F#5P迄今为止……\n',
            '我虽然一直都在说些逞强的话……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290638V可是…\n',
            '完全都只是在吹牛而已…',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290639V这样下去的话…\n',
            '还说什么追寻答案… ',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290640V#1027F我……我……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030290641V#522F……………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290642V#026F……艾丝蒂尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(500)

    @scena.Lambda('lambda_2FE6')
    def lambda_2FE6():
        CameraSetDistance(2900, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2FE6)

    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0103, 0x0002)
    ChrSetChipByIndex(0x0103, 5)
    OP_0D()

    @scena.Lambda('lambda_3006')
    def lambda_3006():
        OP_99(0x00FE, 0x00, 0x07, 2000)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_3006)

    Sleep(300)

    PlaySE(165, 0x00, 0x64)
    WaitForThreadExit(0x0103, 0x0001)
    Sleep(500)

    OP_99(0x0103, 0x08, 0x0E, 1500)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010290643V#1026F#5P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x0107, -67520, 0, -1240, 270)
    ChrSetPos(0x0105, -67520, 0, -1240, 270)
    PlaySE(6, 0x00, 0x64)
    Sleep(500)

    ChrTalk(
        0x0105,
        (
            '#0060290644V#5P雪拉扎德！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070290645V#1P姐、姐姐！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0107, 0x01, 0x00, func_12_415A)
    Sleep(500)

    CreateThread(0x0105, 0x01, 0x00, func_13_4193)
    Sleep(1000)

    ChrTalk(
        0x0103,
        (
            '#0030290646V#022F……不成熟的不只是你。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290647V即使是我。\n',
            '不也一样完全比不上老师吗。\n',
            '但我从没气馁过，一直在努力提高自己。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290648V阿加特也是，金先生也是，\n',
            '连卡西乌斯老师，也是一样…',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290649V大家都会因自己的无力而痛苦懊恼，\n',
            '但同时也都会继续拼命努力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290650V#1026F#5P老、老爸也……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030290651V#522F你还记得吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290652V莱娜阿姨去世的时候，\n',
            '老师并没能及时赶到… ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010210915V#1026F#5P……啊………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030290654V#022F可是老师……\n',
            '最终还是摆脱了失去莱娜阿姨的阴影，\n',
            '步向了游击士的道路。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290655V并一直努力坚持，\n',
            '守护着自己珍视的人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290656V如今老师回归到了军队，\n',
            '但他这种信念也不会有丝毫改变。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290657V#026F艾丝蒂尔……\n',
            '你又该怎么做呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010210920V#1003F#5P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030290659V#022F其实这并不难思考。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290660V只要明白自己内心\n',
            '深处的真实想法就可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290661V#1003F#5P………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290662V答案…我现在还无法找到，但是…',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290663V#1026F即使如此……我也会继续前进。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290664V为了保护最重要的人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010290665V#1005F#5P虽然自己的力量还远远不够，\n',
            '但我不会就这么放弃的！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 50, 3000, 100)
    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030290666V#524F呵呵……\n',
            '你终于明白过来了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    ChrClearFlags(0x0101, 0x0080)
    ChrClearFlags(0x0103, 0x0002)
    ChrSetChipByIndex(0x0103, 65535)
    ChrSetSubChip(0x0103, 0)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetSubChip(0x0101, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010280781V#1025F#5P对不起，雪拉姐……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290668V我这个妹妹……\n',
            '总是给你添麻烦呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030290669V#027F呵呵，\n',
            '那也是姐姐的义务啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290670V而且越是添麻烦的孩子\n',
            '也就越可爱，对吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290671V#1015F#5P呼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070290672V#061F嘻嘻……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060290673V#041F#6P呵呵……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrSetDirection(0x0101, 180, 400)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010290674V#1008F#5P啊……抱、抱歉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290675V让、让大家担心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070290676V#560F嗯、虽然吓了一跳，不过……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070290677V姐姐和雪拉姐的关系\n',
            '还真是好的没得说呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070290678V#067F嘿嘿嘿……\n',
            '我都有点嫉妒了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060290679V#048F#6P呵呵，看到了这么感动的场面，\n',
            '我也很满足呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290680V#1013F#5P好、好了啦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010290681V#1015F#5P那么，雪拉姐，咱们现在该怎么做？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290682V虽然应该马上回协会报告，\n',
            '但是不能扔下缇欧她们不管…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030290683V#522F是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290684V看来只能是你我之中的一个人\n',
            '留在这里了… ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x000D, -68520, 0, -1240, 270)
    ChrSetRGBAMask(0x000D, 255, 255, 255, 0, 0)

    NpcTalk(
        0x000D,
        '青年的声音',
        (
            '#0180290685V#1P没有那个必要啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0103, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0105, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0107, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_39BD')
    def lambda_39BD():
        ChrTurnDirection(0x00FE, 0x000D, 400)
        Yield()

        Jump('lambda_39BD')

    DispatchAsync2(0x0101, 0x0001, lambda_39BD)

    @scena.Lambda('lambda_39CE')
    def lambda_39CE():
        ChrTurnDirection(0x00FE, 0x000D, 400)
        Yield()

        Jump('lambda_39CE')

    DispatchAsync2(0x0103, 0x0001, lambda_39CE)

    @scena.Lambda('lambda_39DF')
    def lambda_39DF():
        ChrTurnDirection(0x00FE, 0x000D, 400)
        Yield()

        Jump('lambda_39DF')

    DispatchAsync2(0x0105, 0x0001, lambda_39DF)

    @scena.Lambda('lambda_39F0')
    def lambda_39F0():
        ChrTurnDirection(0x00FE, 0x000D, 400)
        Yield()

        Jump('lambda_39F0')

    DispatchAsync2(0x0107, 0x0001, lambda_39F0)

    @scena.Lambda('lambda_3A01')
    def lambda_3A01():
        CameraMove(-75100, 0, 2370, 1800)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3A01)

    OP_4A(0x000D, 255)
    ChrClearFlags(0x000D, 0x0080)

    @scena.Lambda('lambda_3A22')
    def lambda_3A22():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0002, lambda_3A22)

    ChrWalkTo(0x000D, -70000, 0, -1040, 2500, 0x00)
    ChrWalkTo(0x000D, -72410, 0, 180, 2500, 0x00)
    ChrTurnDirection(0x000D, 0x0101, 400)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0103, 0x01)
    TerminateThread(0x0105, 0x01)
    TerminateThread(0x0107, 0x01)
    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0105,
        (
            '#0060290686V#044F#5P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070290687V#064F#5P呀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030290688V#023F呀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0180290689V#1062F#6P耶～大家好啊。\n',
            '我是七耀教会的凯文。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180290690V上次在王都分别后还没过多久嘛，\n',
            '没想到这么快就又见面了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180290691V#1061F果然是女神的引导啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290692V#1020F#5P什、什么……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290693V为什么凯文先生会突然\n',
            '出现在这里啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0180290694V#1066F#6P啊～说来也是很简单的啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180290695V昨天夜里，迪拜恩教区长\n',
            '将昏睡事件的报告\n',
            '发到了王都的大圣堂。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180290696V#1065F所以身为『星杯骑士』的我\n',
            '就跑过来确认一下情况啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180290697V穿过浓雾密布的街道，\n',
            '今天早上好不容易才抵达洛连特。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180290698V#1062F然后跑到协会就听说\n',
            '你们现在因为工作\n',
            '跑到这里来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290699V#1007F#5P啊～好啦好啦。\n',
            '事情的大概我明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290700V#1019F说来说去，这根本就不算是什么\n',
            '女神的引导嘛！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0180290701V#1066F#6P啊哈哈～～被揭穿了吗～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030290702V#020F不过，凯文神父，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290703V你刚才说的『没有那个必要』\n',
            '是什么意思？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0180290704V#1060F#6P啊，就是说大姐你和艾丝蒂尔\n',
            '没有必要留在这里了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180290705V这里交给我就好，\n',
            '你们两个一起回协会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290706V#1004F#5P哎哎！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060290707V#542F#5P那、那样好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0180290708V#1071F#6P这也是神父的工作啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180290709V我好歹也算是略通医术，\n',
            '放心交给我就好了啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070290710V#560F#5P那个……\n',
            '真是谢谢了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030290711V#021F呵呵，那么我们就\n',
            '恭敬不如从命了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290712V#020F各位！我们这就回洛连特！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290713V#1025F#5P嗯！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290714V凯文……\n',
            '缇欧…就拜托你了啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0180290715V#1060F#6P噢！\n',
            '没问题，放心走吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000007D0)
    FadeOut(1500, 0, -1)
    OP_0D()
    CameraMove(-73890, 0, 410, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    ChrClearFlags(0x0101, 0x0004)
    ChrClearFlags(0x0107, 0x0004)
    ChrClearFlags(0x0105, 0x0004)
    ChrSetPos(0x0000, -73890, 0, 410, 90)
    ChrSetPos(0x0001, -73890, 0, 410, 90)
    ChrSetPos(0x0002, -73890, 0, 410, 90)
    ChrSetPos(0x0003, -73890, 0, 410, 90)
    OP_69(0x0000, 0)
    ChrSetPos(0x000D, -75610, 0, 2580, 270)
    OP_4B(0x000D, 255)
    SetScenaFlags(ScenaFlag(0x0304, 2, 0x1822))
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    OP_28(0x0091, 0x01, 0x0008)
    OP_28(0x0091, 0x01, 0x0010)
    OP_28(0x0091, 0x01, 0x0020)
    Sleep(500)

    OP_21()
    PlayBGM(15)
    FadeIn(1000, 0)
    EventEnd(0x00)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0xF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0012 offset: 0x415A
@scena.Code('func_12_415A')
def func_12_415A():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)

    @scena.Lambda('lambda_416B')
    def lambda_416B():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_416B)

    ChrWalkTo(0x00FE, -75300, 0, 610, 4000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x0013 offset: 0x4193
@scena.Code('func_13_4193')
def func_13_4193():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)

    @scena.Lambda('lambda_41A4')
    def lambda_41A4():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_41A4)

    ChrWalkTo(0x00FE, -73790, 0, 220, 4000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x0014 offset: 0x41CC
@scena.Code('func_14_41CC')
def func_14_41CC():
    EventBegin(0x00)
    OP_DB()
    OP_4A(0x000D, 255)
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    ChrSetPos(0x000D, -74400, 0, 300, 315)
    ChrSetPos(0x000B, -75940, 0, 930, 135)
    ChrSetPos(0x000C, -75950, 0, 180, 135)
    ChrSetPos(0x000A, -75640, 0, 1920, 135)
    ChrSetPos(0x0009, -74730, 0, 2000, 135)
    ChrSetPos(0x0008, -75270, 0, 2740, 135)
    ChrSetChipByIndex(0x000B, 9)
    ChrSetSubChip(0x000B, 0)
    ChrSetChipByIndex(0x000A, 8)
    ChrSetSubChip(0x000A, 0)
    ChrSetChipByIndex(0x0009, 7)
    ChrSetSubChip(0x0009, 0)
    ChrSetChipByIndex(0x0008, 6)
    ChrSetSubChip(0x0008, 0)
    ChrSetChipByIndex(0x000C, 10)
    ChrSetSubChip(0x000C, 0)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    CameraMove(-72650, 0, 450, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)

    @scena.Lambda('lambda_42E0')
    def lambda_42E0():
        CameraMove(-75540, 0, 1480, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_42E0)

    FadeIn(2000, 0)
    OP_62(0x000D, 0x00000000, 2100, 0x26, 0x27, 0x000000FA, 0x00)
    Sleep(1000)

    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    ChrSetDirection(0x000D, 270, 400)
    Sleep(200)

    OP_62(0x000B, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    Sleep(1000)

    ChrSetDirection(0x000D, 0, 400)
    Sleep(1000)

    OP_62(0x000C, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    CreateThread(0x0009, 0x01, 0x00, func_15_438D)
    Sleep(2000)

    FadeOut(2000, 0, -1)
    OP_0D()
    OP_63(0x000D)
    OP_DC()
    SetScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    NewScene('ED6_DT21/T0121._SN', 103, 0, 0)
    IdleLoop()

    Return()

# id: 0x0015 offset: 0x438D
@scena.Code('func_15_438D')
def func_15_438D():
    ChrJumpToRelative(0x0009, 0, 0, 0, 800, 12000)
    Sleep(500)

    ChrJumpToRelative(0x000A, 0, 0, 0, 800, 12000)
    Sleep(1000)

    ChrJumpToRelative(0x0009, 0, 0, 0, 800, 12000)
    Sleep(500)

    ChrJumpToRelative(0x000A, 0, 0, 0, 800, 12000)
    ChrSetDirection(0x000D, 270, 400)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
