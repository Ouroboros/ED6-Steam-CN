import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T3170_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3170   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'T3170.x'
    header.mapIndex       = 1
    header.bgm            = 84
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT01/T3170._SN', 'ED6_DT01/T3170_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
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
        ('ED6_DT07/CH01143._CH', 'ED6_DT07/CH01143P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH01270._CH', 'ED6_DT07/CH01270P._CP'),
        ('ED6_DT07/CH01000._CH', 'ED6_DT07/CH01000P._CP'),
        ('ED6_DT07/CH01100._CH', 'ED6_DT07/CH01100P._CP'),
        ('ED6_DT07/CH01250._CH', 'ED6_DT07/CH01250P._CP'),
        ('ED6_DT07/CH01450._CH', 'ED6_DT07/CH01450P._CP'),
        ('ED6_DT07/CH01230._CH', 'ED6_DT07/CH01230P._CP'),
        ('ED6_DT07/CH01220._CH', 'ED6_DT07/CH01220P._CP'),
        ('ED6_DT07/CH01663._CH', 'ED6_DT07/CH01663P._CP'),
        ('ED6_DT07/CH01223._CH', 'ED6_DT07/CH01223P._CP'),
    ]

# id: 0x10001 offset: 0x102
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '多杰',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01D5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '贝恩',
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
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            name                = '乌尔斯',
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
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            name                = '兰达老人',
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
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            name                = '科奇莫爷爷',
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
            name                = '伊格尔',
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
            name                = '雷曼',
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
            talkScenaIndex      = 0x0009,
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
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '雷伊',
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
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '蒂亚利',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
    )

# id: 0x10002 offset: 0x242
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x242
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x242
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -530,
            triggerZ            = -1000,
            triggerY            = 4660,
            triggerRange        = 400,
            actorX              = -2470,
            actorZ              = 500,
            actorY              = 4710,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000C,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x266
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_2B2',
    )

    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0009, -2470, -1000, 4710, 82)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, -580, -1000, 8800, 356)
    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x000E, 790, -1000, 6110, 1)

    Jump('loc_63D')

    def _loc_2B2(): pass

    label('loc_2B2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_2FE',
    )

    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0009, -2470, -1000, 4710, 82)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, -580, -1000, 8800, 356)
    ChrClearFlags(0x000B, 0x0080)
    ChrSetPos(0x000B, -450, -650, 2280, 266)

    Jump('loc_63D')

    def _loc_2FE(): pass

    label('loc_2FE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_34A',
    )

    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0009, -2470, -1000, 4710, 82)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, -580, -1000, 8800, 356)
    ChrClearFlags(0x000B, 0x0080)
    ChrSetPos(0x000B, -450, -650, 2280, 266)

    Jump('loc_63D')

    def _loc_34A(): pass

    label('loc_34A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_419',
    )

    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, 1800, 4000, 7110, 0)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0009, -580, -1000, 8800, 356)
    CreateThread(0x0009, 0x00, 0x00, func_03_6C8)
    ChrClearFlags(0x000C, 0x0080)
    ChrSetPos(0x000C, -260, 4000, 7710, 192)
    CreateThread(0x000C, 0x00, 0x00, func_05_710)
    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x000E, 790, -1000, 6110, 1)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x000F, -540, -1000, 4640, 270)
    TerminateThread(0x0010, 0xFF)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetFlags(0x0010, 0x0004)
    ChrSetChipByIndex(0x0010, 10)
    ChrSetPos(0x0010, -2630, 4200, 7900, 182)
    ChrSetFlags(0x0010, 0x0010)
    ChrClearFlags(0x0011, 0x0080)
    ChrSetFlags(0x0011, 0x0004)
    ChrSetPos(0x0011, -3800, 4200, 6600, 90)
    ChrSetFlags(0x0011, 0x0010)

    Jump('loc_63D')

    def _loc_419(): pass

    label('loc_419')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_46C',
    )

    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0009, -2470, -1000, 4710, 82)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, 1200, -1000, 5200, 97)
    CreateThread(0x000A, 0x00, 0x00, func_04_6EC)
    ChrClearFlags(0x000B, 0x0080)
    ChrSetPos(0x000B, 1810, -1000, 2230, 105)

    Jump('loc_63D')

    def _loc_46C(): pass

    label('loc_46C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_4B8',
    )

    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0009, -2470, -1000, 4710, 82)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, -580, -1000, 8800, 356)
    ChrClearFlags(0x000B, 0x0080)
    ChrSetPos(0x000B, -450, -650, 2280, 266)

    Jump('loc_63D')

    def _loc_4B8(): pass

    label('loc_4B8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_50B',
    )

    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0009, -580, -1000, 8800, 356)
    ChrClearFlags(0x000B, 0x0080)
    ChrSetPos(0x000B, 1200, -1000, 5200, 97)
    CreateThread(0x000B, 0x00, 0x00, func_04_6EC)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0010, 640, -1000, 6620, 9)

    Jump('loc_63D')

    def _loc_50B(): pass

    label('loc_50B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_557',
    )

    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, 3450, -1000, 8500, 185)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0009, -2470, -1000, 4710, 82)
    ChrClearFlags(0x000B, 0x0080)
    ChrSetPos(0x000B, -450, -650, 2280, 266)

    Jump('loc_63D')

    def _loc_557(): pass

    label('loc_557')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_5A3',
    )

    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, -580, -1000, 8800, 356)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0009, -2470, -1000, 4710, 82)
    ChrClearFlags(0x000B, 0x0080)
    ChrSetPos(0x000B, -450, -650, 2280, 266)

    Jump('loc_63D')

    def _loc_5A3(): pass

    label('loc_5A3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Return,
        ),
        'loc_5EF',
    )

    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, -580, -1000, 8800, 356)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0009, -2470, -1000, 4710, 82)
    ChrClearFlags(0x000B, 0x0080)
    ChrSetPos(0x000B, 1810, -1000, 2230, 105)

    Jump('loc_63D')

    def _loc_5EF(): pass

    label('loc_5EF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_63D',
    )

    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, -580, -1000, 8800, 356)
    ChrSetFlags(0x000A, 0x0010)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0009, -2470, -1000, 4710, 82)
    ChrClearFlags(0x000B, 0x0080)
    ChrSetPos(0x000B, 1810, -1000, 2230, 105)

    def _loc_63D(): pass

    label('loc_63D')

    Return()

# id: 0x0001 offset: 0x63E
@scena.Code('func_01_63E')
def func_01_63E():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_648',
    )

    Jump('loc_6B1')

    def _loc_648(): pass

    label('loc_648')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_652',
    )

    Jump('loc_6B1')

    def _loc_652(): pass

    label('loc_652')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_65C',
    )

    Jump('loc_6B1')

    def _loc_65C(): pass

    label('loc_65C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_66A',
    )

    OP_64(0x00, 0x0001)

    Jump('loc_6B1')

    def _loc_66A(): pass

    label('loc_66A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_674',
    )

    Jump('loc_6B1')

    def _loc_674(): pass

    label('loc_674')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_67E',
    )

    Jump('loc_6B1')

    def _loc_67E(): pass

    label('loc_67E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_68C',
    )

    OP_64(0x00, 0x0001)

    Jump('loc_6B1')

    def _loc_68C(): pass

    label('loc_68C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_696',
    )

    Jump('loc_6B1')

    def _loc_696(): pass

    label('loc_696')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_6A0',
    )

    Jump('loc_6B1')

    def _loc_6A0(): pass

    label('loc_6A0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Return,
        ),
        'loc_6AA',
    )

    Jump('loc_6B1')

    def _loc_6AA(): pass

    label('loc_6AA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_6B1',
    )

    def _loc_6B1(): pass

    label('loc_6B1')

    Return()

# id: 0x0002 offset: 0x6B2
@scena.Code('func_02_6B2')
def func_02_6B2():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_6C7',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_6B2')

    def _loc_6C7(): pass

    label('loc_6C7')

    Return()

# id: 0x0003 offset: 0x6C8
@scena.Code('func_03_6C8')
def func_03_6C8():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_6EB',
    )

    OP_8D(0x00FE, -1880, 8780, 440, 8570, 3000)

    Jump('func_03_6C8')

    def _loc_6EB(): pass

    label('loc_6EB')

    Return()

# id: 0x0004 offset: 0x6EC
@scena.Code('func_04_6EC')
def func_04_6EC():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_70F',
    )

    OP_8D(0x00FE, 400, 5540, 5960, 4780, 3000)

    Jump('func_04_6EC')

    def _loc_70F(): pass

    label('loc_70F')

    Return()

# id: 0x0005 offset: 0x710
@scena.Code('func_05_710')
def func_05_710():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_733',
    )

    OP_8D(0x00FE, -1460, 6310, 0, 9500, 3000)

    Jump('func_05_710')

    def _loc_733(): pass

    label('loc_733')

    Return()

# id: 0x0006 offset: 0x734
@scena.Code('func_06_734')
def func_06_734():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.Eval, "OP_29(0x002A, 0x00, 0x08)"),
            (Expr.Eval, "OP_29(0x002A, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x002A, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_878',
    )

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
            TXT(0x00, '【对话】\n'),
            TXT(0x01, '【报告测试结果】\n'),
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
        (0x00000000, 'loc_7BC'),
        (0x00000001, 'loc_833'),
        (-1, 'loc_874'),
    )

    def _loc_7BC(): pass

    label('loc_7BC')

    ChrTalk(
        0x00FE,
        (
            '前辈的想法，\n',
            '与其说是积极，\n',
            '不如说是马马虎虎呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这么糟糕的西红柿，\n',
            '就算取了个好名字，\n',
            '也是卖不出去的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_874')

    def _loc_833(): pass

    label('loc_833')

    ChrTalk(
        0x00FE,
        (
            '抱歉，\n',
            '今天工作已经结束了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那件事情\n',
            '等明天再说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_874')

    def _loc_874(): pass

    label('loc_874')

    TalkEnd(0x00FE)

    Return()

    def _loc_878(): pass

    label('loc_878')

    ChrTalk(
        0x00FE,
        (
            '前辈的想法，\n',
            '与其说是积极，\n',
            '不如说是马马虎虎呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这么糟糕的西红柿，\n',
            '就算取了个好名字，\n',
            '也是卖不出去的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0007 offset: 0x8F0
@scena.Code('func_07_8F0')
def func_07_8F0():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_A43',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_96C',
    )

    ChrTalk(
        0x00FE,
        (
            '蒂亚利，\n',
            '我觉得你的积极构想还远远不够。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不管跌倒了多少次都要爬起来，\n',
            '那样的韧劲是必不可少的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A40')

    def _loc_96C(): pass

    label('loc_96C')

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x00FE,
        (
            '蒂亚利，\n',
            '我觉得你的积极构想还远远不够。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就拿那个苦西红柿来说吧。\n',
            '若是取一个适当的名字，\n',
            '搞不好会异常畅销。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是啊！比如……\n',
            '『苦味西红柿』什么的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔，相当不错啊。\n',
            '那么就叫『苦味西红柿』吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A40(): pass

    label('loc_A40')

    Jump('loc_BF7')

    def _loc_A43(): pass

    label('loc_A43')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_BF7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_AED',
    )

    ChrTalk(
        0x00FE,
        (
            '适合在研究中吃的饭，\n',
            '果然还要数蔡斯的传统料理啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是的，\n',
            '要是蒂亚利也跟过来就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '整天呆在研究室，\n',
            '头脑中是不会涌现出什么新构想的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BF7')

    def _loc_AED(): pass

    label('loc_AED')

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x00FE,
        (
            '呼呼，适合在研究中吃的饭，\n',
            '果然还要数蔡斯的传统料理啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然经常会被美食家\n',
            '批评说缺乏细腻……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过在刺激头脑这点上，\n',
            '没有什么能比得过蔡斯的料理了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '身为一名研究员，\n',
            '很少会有\n',
            '享受美食的空闲时间的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为不知道\n',
            '什么时候就会找到\n',
            '研究的线索。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BF7(): pass

    label('loc_BF7')

    TalkEnd(0x00FE)

    Return()

# id: 0x0008 offset: 0xBFB
@scena.Code('func_08_BFB')
def func_08_BFB():
    ChrSetFlags(0x000F, 0x0010)
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_E67',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_C64',
    )

    ChrTalk(
        0x00FE,
        (
            '呼呼，\n',
            '今天可是特别烦累的一天。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看来要喝上一杯，\n',
            '舒缓一下压力才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E67')

    def _loc_C64(): pass

    label('loc_C64')

    If(
        (
            (Expr.Eval, "OP_29(0x0030, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_CC4',
    )

    ChrTalk(
        0x00FE,
        (
            '呼呼，\n',
            '今天可是特别烦累的一天。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看来要喝上一杯，\n',
            '舒缓一下压力才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))

    Jump('loc_E67')

    def _loc_CC4(): pass

    label('loc_CC4')

    If(
        (
            (Expr.Eval, "OP_29(0x002D, 0x00, 0x04)"),
            Expr.Return,
        ),
        'loc_D6A',
    )

    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(800)

    ChrTurnDirection(0x00FE, 0x0000, 400)

    ChrTalk(
        0x00FE,
        (
            '哎呀，\n',
            '难道你们把书拿来了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过正如你们所见，\n',
            '现在已经下班了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '工作的事情，\n',
            '现在还是不要谈了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))
    ChrSetDirection(0x00FE, 270, 400)

    Jump('loc_E67')

    def _loc_D6A(): pass

    label('loc_D6A')

    If(
        (
            (Expr.Eval, "OP_29(0x002D, 0x00, 0x02)"),
            Expr.Return,
        ),
        'loc_E14',
    )

    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(800)

    ChrTurnDirection(0x00FE, 0x0000, 400)

    ChrTalk(
        0x00FE,
        (
            '哎呀，\n',
            '难道你们是来谈工作的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过正如你们所见，\n',
            '现在已经下班了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '工作的事情，\n',
            '现在还是不要谈了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))
    ChrSetDirection(0x00FE, 270, 400)

    Jump('loc_E67')

    def _loc_E14(): pass

    label('loc_E14')

    ChrTalk(
        0x00FE,
        (
            '呼呼，\n',
            '今天可是特别烦累的一天。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看来要喝上一杯，\n',
            '舒缓一下压力才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))

    def _loc_E67(): pass

    label('loc_E67')

    TalkEnd(0x00FE)

    Return()

# id: 0x0009 offset: 0xE6B
@scena.Code('func_09_E6B')
def func_09_E6B():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_FCE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_EDB',
    )

    ChrTalk(
        0x00FE,
        (
            '真是的！\n',
            '好不容易参加了营救博士的作战……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但却不能向别人夸耀这件事，\n',
            '真是痛苦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FCB')

    def _loc_EDB(): pass

    label('loc_EDB')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '哟，\n',
            '你们在要塞那边干得很漂亮呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '作为一名工房船的船员，\n',
            '我能帮上忙真是感到自豪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过当集装箱被士兵们围住的时候\n',
            '我紧张得手心都出汗了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……哎呀，因为现在没有事了，\n',
            '才能这样轻松地谈笑啊。\n',
            '当时全体船员都是脸色苍白哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_FCB(): pass

    label('loc_FCB')

    Jump('loc_10DB')

    def _loc_FCE(): pass

    label('loc_FCE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_10DB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_1042',
    )

    ChrTalk(
        0x00FE,
        (
            '明天工房船\n',
            '似乎又要出动\n',
            '去雷斯顿要塞执行任务了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说起来，\n',
            '最近来自军方的任务也太多了点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10DB')

    def _loc_1042(): pass

    label('loc_1042')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '明天工房船\n',
            '似乎又要出动\n',
            '去雷斯顿要塞执行任务了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，\n',
            '现在大家都在做出动的准备吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就是在这种时候，\n',
            '我觉得自己是个驾驶员真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_10DB(): pass

    label('loc_10DB')

    TalkEnd(0x00FE)

    Return()

# id: 0x000A offset: 0x10DF
@scena.Code('func_0A_10DF')
def func_0A_10DF():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_11E5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_1162',
    )

    ChrTalk(
        0x00FE,
        (
            '我特地来找兰达那家伙，\n',
            '谁知他已经回去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没办法。\n',
            '既然难得来一趟，\n',
            '至少要好好享受一下怀旧的风味吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11E5')

    def _loc_1162(): pass

    label('loc_1162')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '呼呼，什么呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我特地来找兰达那家伙，\n',
            '谁知他已经回去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是个让人捉摸不透的家伙。\n',
            '和年轻的时候真是一点都没变。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_11E5(): pass

    label('loc_11E5')

    TalkEnd(0x00FE)

    Return()

# id: 0x000B offset: 0x11E9
@scena.Code('func_0B_11E9')
def func_0B_11E9():
    Return()

# id: 0x000C offset: 0x11EA
@scena.Code('func_0C_11EA')
def func_0C_11EA():
    Call(0, 0x000D)

    Return()

# id: 0x000D offset: 0x11EF
@scena.Code('func_0D_11EF')
def func_0D_11EF():
    TalkBegin(0x0009)

    If(
        (
            (Expr.Eval, "OP_29(0x002B, 0x00, 0x02)"),
            (Expr.Eval, "OP_29(0x002B, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x002B, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_129B',
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
            TXT(0x02, '让他看食材\n'),
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
        'loc_1272',
    )

    OP_0D()
    OP_A9(0x41)
    OP_56(0x00)
    TalkEnd(0x0009)

    Return()

    def _loc_1272(): pass

    label('loc_1272')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1287',
    )

    Call(1, 0x0002)
    TalkEnd(0x0009)

    Return()

    def _loc_1287(): pass

    label('loc_1287')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1298',
    )

    TalkEnd(0x0009)

    Return()

    def _loc_1298(): pass

    label('loc_1298')

    Jump('loc_1307')

    def _loc_129B(): pass

    label('loc_129B')

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
        'loc_12F6',
    )

    OP_0D()
    OP_A9(0x41)
    OP_56(0x00)
    TalkEnd(0x0009)

    Return()

    def _loc_12F6(): pass

    label('loc_12F6')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1307',
    )

    TalkEnd(0x0009)

    Return()

    def _loc_1307(): pass

    label('loc_1307')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_135B',
    )

    ChrTalk(
        0x0009,
        (
            '#2100180846V谢了。\n',
            '今天多亏你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '敬请期待\n',
            '本店全新的菜单吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_21E1')

    def _loc_135B(): pass

    label('loc_135B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_14FC',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x002B, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1461',
    )

    ChrTalk(
        0x0009,
        (
            '刚才从工房来的客人\n',
            '好像正在谈论\n',
            '什么珍贵西红柿的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '我问了问能否用在这个新菜谱里面，\n',
            '于是就得到了样品……\n',
            '这可是非常合适啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '马上去工房打听一下\n',
            '那个西红柿的情况吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '同时也预定将它\n',
            '尽快添加到店里的菜单上。\n',
            '敬请期待哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_14F9')

    def _loc_1461(): pass

    label('loc_1461')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x0009,
        (
            '哦，是你们啊。\n',
            '之前多谢你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '刚才，\n',
            '我去了工房和他们商谈\n',
            '关于那个西红柿的供货问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '离加入店里菜单的日子\n',
            '已经不远了。\n',
            '敬请期待哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_14F9(): pass

    label('loc_14F9')

    Jump('loc_21E1')

    def _loc_14FC(): pass

    label('loc_14FC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_1619',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x002B, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_15AE',
    )

    ChrTalk(
        0x0009,
        (
            '哦，辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '我们这边的午餐时间\n',
            '也正好刚刚结束，\n',
            '可以休息一下喘口气了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '哦，对了。\n',
            '你们想尝尝『苦西红柿三明治』吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F还、还是算了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1616')

    def _loc_15AE(): pass

    label('loc_15AE')

    ChrTalk(
        0x0009,
        (
            '哦，辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '我们这边的午餐时间\n',
            '也正好刚刚结束，\n',
            '可以休息一下喘口气了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '你们请随便坐吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1616(): pass

    label('loc_1616')

    Jump('loc_21E1')

    def _loc_1619(): pass

    label('loc_1619')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_1827',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_1685',
    )

    ChrTalk(
        0x0009,
        (
            '我们这里\n',
            '每天都在开发新的菜谱，\n',
            '真是非常繁忙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '同时也得注意\n',
            '不要累坏了身子呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1824')

    def _loc_1685(): pass

    label('loc_1685')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_16D3',
    )

    ChrTalk(
        0x0009,
        (
            '这里每天\n',
            '都是那么繁忙呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '同时也得注意\n',
            '不要累坏了身子呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1824')

    def _loc_16D3(): pass

    label('loc_16D3')

    If(
        (
            (Expr.Eval, "OP_29(0x002B, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_17A0',
    )

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    ChrTalk(
        0x0009,
        (
            '嗯，每天这里都\n',
            '持续着忙碌的日子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '因为除了平常的工作，\n',
            '还要开发新的菜谱\n',
            '来满足客人的需要。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '这样拼命地工作，\n',
            '一定会把身体搞坏。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '忙碌的同时也要注意身体。\n',
            '你们也要注意啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1824')

    def _loc_17A0(): pass

    label('loc_17A0')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x0009,
        (
            '嗯，每天这里都\n',
            '持续着忙碌的日子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '这样拼命地工作，\n',
            '一定会把身体搞坏。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '忙碌的同时也要注意身体。\n',
            '你们也要注意啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1824(): pass

    label('loc_1824')

    Jump('loc_21E1')

    def _loc_1827(): pass

    label('loc_1827')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_193B',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x002B, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_18D1',
    )

    ChrTalk(
        0x0009,
        (
            '唔，该死。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '乌尔斯已经回去了，\n',
            '兰达也不在……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '……………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '……没办法，工作吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '必须研究一下\n',
            '那个西红柿该用什么方法烹饪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1938')

    def _loc_18D1(): pass

    label('loc_18D1')

    ChrTalk(
        0x0009,
        (
            '唔，该死。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '乌尔斯已经回去了，\n',
            '兰达也不在……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '……………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '……没办法，工作吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1938(): pass

    label('loc_1938')

    Jump('loc_21E1')

    def _loc_193B(): pass

    label('loc_193B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_19B8',
    )

    ChrTalk(
        0x0009,
        (
            '工房那里\n',
            '似乎发生了什么骚乱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '那里聚集了大量的先进技术，\n',
            '大概小偷是瞄准了这一点，\n',
            '想盗走什么研究成果吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_21E1')

    def _loc_19B8(): pass

    label('loc_19B8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_1B23',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_19FC',
    )

    ChrTalk(
        0x0009,
        (
            '那么，老爷子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '先帮我尝尝\n',
            '这个西红柿吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B20')

    def _loc_19FC(): pass

    label('loc_19FC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_1A2F',
    )

    ChrTalk(
        0x0009,
        (
            '那么，老爷子。\n',
            '今天咱们聊些什么呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B20')

    def _loc_1A2F(): pass

    label('loc_1A2F')

    If(
        (
            (Expr.Eval, "OP_29(0x002B, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_1AAE',
    )

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    ChrTalk(
        0x0009,
        (
            '最近一段时间，\n',
            '在乌尔斯外出的时候，\n',
            '我拼命地工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '今天将工作全部交给他了，\n',
            '我要继续构想我的新菜谱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B20')

    def _loc_1AAE(): pass

    label('loc_1AAE')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x0009,
        (
            '最近一段时间，\n',
            '在乌尔斯外出的时候，\n',
            '我拼命地工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '今天将工作全部交给他了，\n',
            '我决心一秒都不再工作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1B20(): pass

    label('loc_1B20')

    Jump('loc_21E1')

    def _loc_1B23(): pass

    label('loc_1B23')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_1C96',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_1B4D',
    )

    ChrTalk(
        0x0009,
        (
            '老爷子！\n',
            '煎肉来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C93')

    def _loc_1B4D(): pass

    label('loc_1B4D')

    If(
        (
            (Expr.Eval, "OP_29(0x002B, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_1C00',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x0009,
        (
            '刚刚乌尔斯\n',
            '那家伙出去了，\n',
            '只好我自己来掌勺……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '偶尔自己亲自动动手，\n',
            '觉得其实做饭还是很有乐趣的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '在新菜谱里\n',
            '使用那个西红柿的构想\n',
            '也涌现在我脑子里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C93')

    def _loc_1C00(): pass

    label('loc_1C00')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x0009,
        (
            '刚刚乌尔斯\n',
            '那家伙出去了，\n',
            '只好我自己来掌勺……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '偶尔自己亲自动动手，\n',
            '觉得其实做饭还是很有乐趣的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '新菜谱的构想\n',
            '也涌现在我脑子里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C93(): pass

    label('loc_1C93')

    Jump('loc_21E1')

    def _loc_1C96(): pass

    label('loc_1C96')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_1D72',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_1D16',
    )

    ChrTalk(
        0x0009,
        (
            '唔，\n',
            '不过那可是道很刺激的料理呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '传统料理的菜谱\n',
            '也已经用完了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '不快点想出新点子来\n',
            '就糟糕了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D6F')

    def _loc_1D16(): pass

    label('loc_1D16')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x0009,
        (
            '每天都吃同样东西的话，\n',
            '就算再好吃也会感到厌烦的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '老爷子\n',
            '是一个任性的人呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1D6F(): pass

    label('loc_1D6F')

    Jump('loc_21E1')

    def _loc_1D72(): pass

    label('loc_1D72')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_1E86',
    )

    ChrTalk(
        0x0009,
        (
            '昨天整个城市的导力\n',
            '好像全部停止了，\n',
            '还引起了大骚动哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '话说回来，\n',
            '现在的年轻人\n',
            '根本无法想象没有导力的世界。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '照明啊，采暖啊，\n',
            '打扫啊，洗涤啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '日常生活和工作\n',
            '渐渐地都交给了导力器处理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '这样一想，\n',
            '普及推广导力器的拉赛尔博士\n',
            '实在是太伟大了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_21E1')

    def _loc_1E86(): pass

    label('loc_1E86')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Return,
        ),
        'loc_2127',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_1F57',
    )

    ChrTalk(
        0x0009,
        (
            '反正搞研究的人身体不好\n',
            '这种事也不是今天才开始的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '蔡斯的料理\n',
            '就是为他们设计出来的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '做法和吃法都很简单，\n',
            '作为食品，营养也很丰富……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '这也是蔡斯的厨师\n',
            '所追求的理想料理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2124')

    def _loc_1F57(): pass

    label('loc_1F57')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AE, 6, 0x576)),
            Expr.Return,
        ),
        'loc_1FFA',
    )

    ChrTalk(
        0x0009,
        (
            '蔡斯的料理\n',
            '多数是为了没什么空闲的技师\n',
            '而做的快餐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '做法和吃法都很简单，\n',
            '作为食品，营养也很丰富……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '这也是蔡斯的厨师\n',
            '所追求的理想料理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2124')

    def _loc_1FFA(): pass

    label('loc_1FFA')

    SetScenaFlags(ScenaFlag(0x00AE, 6, 0x576))

    ChrTalk(
        0x0009,
        (
            '哦，真少见，\n',
            '这不是提妲大小姐吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '怎么样，\n',
            '拉赛尔博士身体还好吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#060F嗯，是的。\n',
            '要多棒有多棒呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '他在研究所里闭门不出，\n',
            '一～直埋头做实验。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '也就是说……\n',
            '还是每天都过着\n',
            '没有规律的生活啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '呼，真是的。\n',
            '他以为自己几岁？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '有时间还是让博士他\n',
            '到外面走走散散心比较好吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2124(): pass

    label('loc_2124')

    Jump('loc_21E1')

    def _loc_2127(): pass

    label('loc_2127')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_21E1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_218A',
    )

    ChrTalk(
        0x0009,
        (
            '我这里还供应\n',
            '传统的蔡斯料理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '『简单又高效』……\n',
            '这是蔡斯料理的特点哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_21E1')

    def _loc_218A(): pass

    label('loc_218A')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x0009,
        (
            '噢，欢迎光临。\n',
            '以前没见过你们，是旅行者吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '那么，\n',
            '在这里好好休息一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_21E1(): pass

    label('loc_21E1')

    TalkEnd(0x0009)

    Return()

# id: 0x000E offset: 0x21E5
@scena.Code('func_0E_21E5')
def func_0E_21E5():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_22C7',
    )

    If(
        (
            (Expr.PushLong, 0x2),
            Expr.Return,
        ),
        'loc_225B',
    )

    ChrTalk(
        0x00FE,
        (
            '露依赛她的工作\n',
            '终于也步入正轨了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '之后，只要祈祷老板的新菜谱\n',
            '像平常一样美味就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_22C4')

    def _loc_225B(): pass

    label('loc_225B')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '不知何时开始\n',
            '老板又在构思新菜谱了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，既期待又有点不安，\n',
            '两种感情混杂在一起真是很微妙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_22C4(): pass

    label('loc_22C4')

    Jump('loc_2B43')

    def _loc_22C7(): pass

    label('loc_22C7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_2363',
    )

    If(
        (
            (Expr.PushLong, 0x2),
            Expr.Return,
        ),
        'loc_230D',
    )

    ChrTalk(
        0x00FE,
        (
            '呼呼，露依赛她的新工作\n',
            '要是能进展顺利就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2360')

    def _loc_230D(): pass

    label('loc_230D')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '呼～\n',
            '午饭时间终于结束了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '然后就是轻松地处理\n',
            '傍晚之前的准备工作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2360(): pass

    label('loc_2360')

    Jump('loc_2B43')

    def _loc_2363(): pass

    label('loc_2363')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_24B4',
    )

    If(
        (
            (Expr.PushLong, 0x2),
            Expr.Return,
        ),
        'loc_2413',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然工作的时候要热心，\n',
            '不过一点空闲都没有也不行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只有工作的人生\n',
            '不是一点意思都没有吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '话说回来，像我们的老板那样\n',
            '完全不工作也很让人头痛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24B1')

    def _loc_2413(): pass

    label('loc_2413')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '昨天，\n',
            '我到露依赛家试着做了做\n',
            '向老板学成的汤……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '她好像很忙，\n',
            '连吃饭的时间都没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过她妹妹乌缇\n',
            '跟我说汤很好喝，\n',
            '这样看来还是不错的嘛……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_24B1(): pass

    label('loc_24B1')

    Jump('loc_2B43')

    def _loc_24B4(): pass

    label('loc_24B4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_2589',
    )

    If(
        (
            (Expr.PushLong, 0x2),
            Expr.Return,
        ),
        'loc_252A',
    )

    ChrTalk(
        0x00FE,
        (
            '露依赛受到\n',
            '导力文明的毒害，\n',
            '运动方面完全不在行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '她是那种一个人玩相扑\n',
            '也会受重伤的类型。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2586')

    def _loc_252A(): pass

    label('loc_252A')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '喂喂，听说了吗？\n',
            '中央工房出事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '露依赛说今天\n',
            '她也要去上班的。\n',
            '有点担心她啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2586(): pass

    label('loc_2586')

    Jump('loc_2B43')

    def _loc_2589(): pass

    label('loc_2589')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_2678',
    )

    If(
        (
            (Expr.PushLong, 0x2),
            Expr.Return,
        ),
        'loc_25E3',
    )

    ChrTalk(
        0x00FE,
        (
            '可恶，气死了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '明明没有多少客人来，\n',
            '却还这么忙，真让人不爽！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2675')

    def _loc_25E3(): pass

    label('loc_25E3')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '唔～然后是煎肉……\n',
            '啊，不对，是先做汤吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呜呜，不知什么时候\n',
            '洗物槽已经被盘子给堆满了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊，老板。\n',
            '拜托了，帮我分担一些工作吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2675(): pass

    label('loc_2675')

    Jump('loc_2B43')

    def _loc_2678(): pass

    label('loc_2678')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_27B2',
    )

    If(
        (
            (Expr.PushLong, 0x2),
            Expr.Return,
        ),
        'loc_270C',
    )

    ChrTalk(
        0x00FE,
        (
            '不过，\n',
            '露依赛最近也有点奇怪呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '请她来吃饭也不来，\n',
            '好像都不和妹妹一同出门了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说起来，\n',
            '觉得她一点空闲都没有啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_27AF')

    def _loc_270C(): pass

    label('loc_270C')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '……真是的，露依赛那家伙。\n',
            '只有这种时候才会想到我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说什么自己的工作很忙，\n',
            '照顾她妹妹的任务\n',
            '就硬推给我了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哼，说起来，\n',
            '那家伙明明是有时间的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_27AF(): pass

    label('loc_27AF')

    Jump('loc_2B43')

    def _loc_27B2(): pass

    label('loc_27B2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_28AA',
    )

    If(
        (
            (Expr.PushLong, 0x2),
            Expr.Return,
        ),
        'loc_2808',
    )

    ChrTalk(
        0x00FE,
        (
            '仔细想想，\n',
            '当时我竟然没从楼梯上摔下来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，我真厉害啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_28A7')

    def _loc_2808(): pass

    label('loc_2808')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '唉～\n',
            '昨天真是糟透了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那时候我正好\n',
            '在二楼清理桌子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '正要下楼梯时，\n',
            '突然店里一片漆黑。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我现在已经想不起来\n',
            '当时是怎么保护盘子没有摔碎的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_28A7(): pass

    label('loc_28A7')

    Jump('loc_2B43')

    def _loc_28AA(): pass

    label('loc_28AA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Return,
        ),
        'loc_29F1',
    )

    If(
        (
            (Expr.PushLong, 0x2),
            Expr.Return,
        ),
        'loc_291C',
    )

    ChrTalk(
        0x00FE,
        (
            '不过，如果这个就是菜式的话，\n',
            '即使是我也可以轻易地做出来啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '下次去女朋友家做做看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_29EE')

    def _loc_291C(): pass

    label('loc_291C')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '我还是有点\n',
            '不敢相信呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '尝了一下刚才偷工减料做的汤，\n',
            '竟然那么有效果。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这只不过是把材料投进锅里\n',
            '用火煮煮就好的汤而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0009, 400)

    ChrTalk(
        0x00FE,
        (
            '我对你要重新评价了，老板。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你啊，\n',
            '不是个单纯的懒人呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_29EE(): pass

    label('loc_29EE')

    Jump('loc_2B43')

    def _loc_29F1(): pass

    label('loc_29F1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_2B43',
    )

    If(
        (
            (Expr.PushLong, 0x2),
            Expr.Return,
        ),
        'loc_2A86',
    )

    ChrTalk(
        0x00FE,
        (
            '这种汤据说有种\n',
            '提高集中力的效果呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……不过，真的有效吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '其实，不就是把水、鸡骨头、青菜\n',
            '还有胡椒放到一起煮吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2B43')

    def _loc_2A86(): pass

    label('loc_2A86')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '唔～\n',
            '放入鸡骨头……\n',
            '接着是青菜、胡椒和水吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '然后一边等\n',
            '一边煮一会儿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……啊？　\n',
            '老板的菜谱\n',
            '到这里就写完了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '………………\n',
            '难道这样就可以了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2B43(): pass

    label('loc_2B43')

    TalkEnd(0x00FE)

    Return()

# id: 0x000F offset: 0x2B47
@scena.Code('func_0F_2B47')
def func_0F_2B47():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_2B9B',
    )

    ChrTalk(
        0x00FE,
        (
            '呵呵，老板。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天你身上运动了的部分\n',
            '不会只有嘴旁边的肌肉吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_31CB')

    def _loc_2B9B(): pass

    label('loc_2B9B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_2BEA',
    )

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，\n',
            '竟然可以一本正经地说出那样的台词……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不愧是老板啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_31CB')

    def _loc_2BEA(): pass

    label('loc_2BEA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_2C85',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_2C2F',
    )

    ChrTalk(
        0x00FE,
        (
            '不过，\n',
            '当时光顾忙着说话，\n',
            '完全没有注意到骚动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2C82')

    def _loc_2C2F(): pass

    label('loc_2C2F')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '唔～\n',
            '以前工房也常常会有小偷出现……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过这一回\n',
            '似乎是相当大的案子呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2C82(): pass

    label('loc_2C82')

    Jump('loc_31CB')

    def _loc_2C85(): pass

    label('loc_2C85')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_2D28',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_2CCA',
    )

    ChrTalk(
        0x00FE,
        (
            '好吧，\n',
            '我就跟老板你说说\n',
            '我去卢安的旅行见闻吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2D25')

    def _loc_2CCA(): pass

    label('loc_2CCA')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '呵呵，\n',
            '年轻人果然就是要劳动才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看着他们麻利工作的身姿，\n',
            '自己心情也舒畅啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2D25(): pass

    label('loc_2D25')

    Jump('loc_31CB')

    def _loc_2D28(): pass

    label('loc_2D28')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_2DDB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_2D6A',
    )

    ChrTalk(
        0x00FE,
        (
            '老板，\n',
            '煎肉还没好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '客人们都等着呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2DD8')

    def _loc_2D6A(): pass

    label('loc_2D6A')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '乌尔斯那孩子\n',
            '竟然擅自跑出去了。\n',
            '我也来帮帮忙吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是的，中午这一会儿\n',
            '应该是忙得团团转的时候啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2DD8(): pass

    label('loc_2DD8')

    Jump('loc_31CB')

    def _loc_2DDB(): pass

    label('loc_2DDB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_2E4C',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，\n',
            '真是感到郁闷啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '每天都来这里，\n',
            '不管什么样的菜都吃腻了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔～\n',
            '想吃点刺激的菜呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_31CB')

    def _loc_2E4C(): pass

    label('loc_2E4C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_2EDA',
    )

    ChrTalk(
        0x00FE,
        (
            '真是的，每个人都是这样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不能使用导力器，\n',
            '一个个都慌乱得不得了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '又不去试想一下，\n',
            '没有导力的年代人家是怎么生活的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_31CB')

    def _loc_2EDA(): pass

    label('loc_2EDA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Return,
        ),
        'loc_30F7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AE, 6, 0x576)),
            (Expr.TestScenaFlags, ScenaFlag(0x00AE, 7, 0x577)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2F9E',
    )

    SetScenaFlags(ScenaFlag(0x00AE, 7, 0x577))

    ChrTalk(
        0x00FE,
        (
            '呵呵，拉赛尔那家伙\n',
            '好像还在很努力地工作吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我曾经也是个钟表工匠，\n',
            '还和那个家伙一起工作过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '后来我的眼力不好，就退休不干了。\n',
            '真是羡慕拉赛尔现在还在工作啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_30F4')

    def _loc_2F9E(): pass

    label('loc_2F9E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_3025',
    )

    ChrTalk(
        0x00FE,
        (
            '话又说回来，\n',
            '贝恩的料理还是挺简单方便的，\n',
            '味道方面也算是让人放心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '也就是说那家伙\n',
            '有自己的一套做料理的聪明方法吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_30F4')

    def _loc_3025(): pass

    label('loc_3025')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '要特别注意\n',
            '这里的老板贝恩哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他最擅长给各种料理\n',
            '加上各种各样的名堂来偷工减料了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    MapClearFlags(0x00000001)
    OP_69(0x0009, 1000)

    ChrTalk(
        0x0009,
        (
            '够了吧，老爷子！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '别老是跟客人\n',
            '说些容易误会的话！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_69(0x0000, 1000)
    MapSetFlags(0x00000001)

    ChrTalk(
        0x00FE,
        (
            '呵呵，\n',
            '我可没有瞎说啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_30F4(): pass

    label('loc_30F4')

    Jump('loc_31CB')

    def _loc_30F7(): pass

    label('loc_30F7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_31CB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_3149',
    )

    ChrTalk(
        0x00FE,
        (
            '唉呀，\n',
            '我是刚刚从卢安旅行回来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还是呆在家里舒服啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_31CB')

    def _loc_3149(): pass

    label('loc_3149')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '呼，\n',
            '好不容易才回到家里来了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉呀，\n',
            '我是刚刚从卢安旅行回来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '尽管可以尽情的游玩，\n',
            '不过还是呆在家里舒服啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_31CB(): pass

    label('loc_31CB')

    TalkEnd(0x00FE)

    Return()

# id: 0x0010 offset: 0x31CF
@scena.Code('func_10_31CF')
def func_10_31CF():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_32B5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_3244',
    )

    ChrTalk(
        0x00FE,
        (
            '虽说多数是些很简单的菜，\n',
            '不过味道可不差嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不为吃饭花时间， \n',
            '正好符合技术人员的性格。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_32B5')

    def _loc_3244(): pass

    label('loc_3244')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '每天呆在酒店里也不是办法，\n',
            '于是就来这里尝尝看了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不愧是符合工房都市的特点，\n',
            '菜色简单而味道也不错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_32B5(): pass

    label('loc_32B5')

    TalkEnd(0x00FE)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
