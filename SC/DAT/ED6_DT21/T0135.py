import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T0135_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0135   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '托露塔'),
    TXT(0x02, '伊莉莎'),
    TXT(0x03, '德瑟鲁'),
    TXT(0x04, '福克纳'),
    TXT(0x05, '矿工提恩特'),
    TXT(0x06, '矿工彭兹'),
    TXT(0x07, '佩特洛夫船长'),
    TXT(0x08, '乘务员诺拉'),
    TXT(0x09, '潘杜老人'),
    TXT(0x0A, '索斯摩夫'),
    TXT(0x0B, '安敦'),
    TXT(0x0C, '利库斯'),
    TXT(0x0D, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T0135.x'
    header.mapIndex       = 7
    header.bgm            = 84
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x25CC
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
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

# id: 0x10001 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT26/CH20330._CH', 'ED6_DT26/CH20330P._CP'),
        ('ED6_DT07/CH02490._CH', 'ED6_DT07/CH02490P._CP'),
        ('ED6_DT07/CH01280._CH', 'ED6_DT07/CH01280P._CP'),
        ('ED6_DT07/CH01270._CH', 'ED6_DT07/CH01270P._CP'),
        ('ED6_DT26/CH20312._CH', 'ED6_DT26/CH20312P._CP'),
        ('ED6_DT07/CH01503._CH', 'ED6_DT07/CH01503P._CP'),
        ('ED6_DT07/CH01500._CH', 'ED6_DT07/CH01500P._CP'),
        ('ED6_DT07/CH01443._CH', 'ED6_DT07/CH01443P._CP'),
        ('ED6_DT07/CH01540._CH', 'ED6_DT07/CH01540P._CP'),
        ('ED6_DT07/CH01250._CH', 'ED6_DT07/CH01250P._CP'),
        ('ED6_DT07/CH01450._CH', 'ED6_DT07/CH01450P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
    ]

# id: 0x10002 offset: 0x112
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            x                   = 36450,
            z                   = 0,
            y                   = 126300,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            x                   = 34500,
            z                   = 0,
            y                   = 75200,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = 39320,
            z                   = 220,
            y                   = 70940,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0155,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            x                   = 36640,
            z                   = 0,
            y                   = 72650,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            x                   = 39470,
            z                   = 1620,
            y                   = 77070,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0155,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            x                   = 41000,
            z                   = 1500,
            y                   = 79500,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            x                   = 37050,
            z                   = 0,
            y                   = 75490,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            x                   = 41530,
            z                   = 0,
            y                   = 67550,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            x                   = 44910,
            z                   = 0,
            y                   = 71790,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0111,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            x                   = 43750,
            z                   = 0,
            y                   = 73360,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
    )

# id: 0x10003 offset: 0x292
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x292
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x292
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 35580,
            triggerZ            = 0,
            triggerY            = 74990,
            triggerRange        = 800,
            actorX              = 34500,
            actorZ              = 1500,
            actorY              = 75200,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x2B6
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_2D0',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x51),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A3(0x10F0)
    Event(0, 0x000F)

    Jump('loc_32E')

    def _loc_2D0(): pass

    label('loc_2D0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 2, 0x1812)),
            Expr.Return,
        ),
        'loc_311',
    )

    OP_4A(0x0008, 255)
    ClearChrFlags(0x0008, 0x0002)
    SetChrSubChip(0x0008, 2)
    SetChrPos(0x0008, 88620, 0, 79000, 270)
    SetChrPos(0x0009, 87090, 0, 79170, 90)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)

    def _loc_311(): pass

    label('loc_311')

    If(
        (
            (Expr.Eval, "OP_29(0x0074, 0x01, 0x0040)"),
            Expr.Return,
        ),
        'loc_321',
    )

    SetChrFlags(0x0011, 0x0080)

    def _loc_321(): pass

    label('loc_321')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0313, 0, 0x1898)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_32E',
    )

    SetChrFlags(0x0010, 0x0010)

    def _loc_32E(): pass

    label('loc_32E')

    Return()

# id: 0x0001 offset: 0x32F
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 2, 0x1812)),
            Expr.Return,
        ),
        'loc_33D',
    )

    OP_6F(0x0000, 10)

    def _loc_33D(): pass

    label('loc_33D')

    Return()

# id: 0x0002 offset: 0x33E
@scena.Code('ReInit')
def ReInit():
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
        'loc_363',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000672)

    Jump('loc_4A5')

    def _loc_363(): pass

    label('loc_363')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_37C',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000640)

    Jump('loc_4A5')

    def _loc_37C(): pass

    label('loc_37C')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_395',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x0000060E)

    Jump('loc_4A5')

    def _loc_395(): pass

    label('loc_395')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3AE',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005DC)

    Jump('loc_4A5')

    def _loc_3AE(): pass

    label('loc_3AE')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3C7',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AA)

    Jump('loc_4A5')

    def _loc_3C7(): pass

    label('loc_3C7')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3E0',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x00000578)

    Jump('loc_4A5')

    def _loc_3E0(): pass

    label('loc_3E0')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3F9',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x00000546)

    Jump('loc_4A5')

    def _loc_3F9(): pass

    label('loc_3F9')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_412',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000677)

    Jump('loc_4A5')

    def _loc_412(): pass

    label('loc_412')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_42B',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000645)

    Jump('loc_4A5')

    def _loc_42B(): pass

    label('loc_42B')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_444',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x00000613)

    Jump('loc_4A5')

    def _loc_444(): pass

    label('loc_444')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_45D',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005E1)

    Jump('loc_4A5')

    def _loc_45D(): pass

    label('loc_45D')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_476',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AF)

    Jump('loc_4A5')

    def _loc_476(): pass

    label('loc_476')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_48F',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x0000057D)

    Jump('loc_4A5')

    def _loc_48F(): pass

    label('loc_48F')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4A5',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x0000054B)

    def _loc_4A5(): pass

    label('loc_4A5')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_4BA',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('loc_4A5')

    def _loc_4BA(): pass

    label('loc_4BA')

    Return()

# id: 0x0003 offset: 0x4BB
@scena.Code('func_03_4BB')
def func_03_4BB():
    Call(0, 0x0004)

    Return()

# id: 0x0004 offset: 0x4C0
@scena.Code('func_04_4C0')
def func_04_4C0():
    TalkBegin(0x000B)
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
            TXT(0x02, '招牌菜『三蛋黄杂烩粥』　1600米拉\n'),
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
        'loc_53F',
    )

    FadeIn(300, 0)
    OP_0D()
    OP_A9(0x04)
    OP_56(0x00)
    TalkEnd(0x000B)

    Return()

    def _loc_53F(): pass

    label('loc_53F')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_64D',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x12),
            (Expr.PushLong, 0x640),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_618',
    )

    SubMira(1600)
    FadeOut(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0x000B, 0x00, 0x64)

    Talk(
        (
            TxtCtl.ShowAll,
            (TxtCtl.SetColor, 0x2),
            '三蛋黄杂烩粥',
            (TxtCtl.SetColor, 0x0),
            '已经品尝过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrStatus(ChrTable['艾丝蒂尔'], 0xFD, 2000)
    SetChrStatus(ChrTable['约修亚'], 0xFD, 2000)
    SetChrStatus(ChrTable['雪拉扎德'], 0xFD, 2000)
    SetChrStatus(ChrTable['奥利维尔'], 0xFD, 2000)
    SetChrStatus(ChrTable['科洛丝'], 0xFD, 2000)
    SetChrStatus(ChrTable['阿加特'], 0xFD, 2000)
    SetChrStatus(ChrTable['提妲'], 0xFD, 2000)
    SetChrStatus(ChrTable['金'], 0xFD, 2000)
    SetChrStatus(ChrTable['凯文神父'], 0xFD, 2000)

    If(
        (
            (Expr.Eval, "OP_40(0x020D, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_60A',
    )

    If(
        (
            (Expr.Eval, "OP_AC(0x0006)"),
            Expr.Return,
        ),
        'loc_5DE',
    )

    Jump('loc_60A')

    def _loc_5DE(): pass

    label('loc_5DE')

    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            TxtCtl.ShowAll,
            (TxtCtl.SetColor, 0x2),
            '三蛋黄杂烩粥',
            (TxtCtl.SetColor, 0x0),
            '的做法已经学会了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_60A(): pass

    label('loc_60A')

    OP_56(0x00)
    FadeIn(1000, 0)

    Jump('loc_63E')

    def _loc_618(): pass

    label('loc_618')

    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            '没有足够的米拉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeIn(300, 0)
    def _loc_63E(): pass

    label('loc_63E')

    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x000B)

    Return()

    def _loc_64D(): pass

    label('loc_64D')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_667',
    )

    FadeIn(300, 0)
    TalkEnd(0x000B)

    Return()

    def _loc_667(): pass

    label('loc_667')

    FadeIn(300, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 2, 0x1812)),
            Expr.Return,
        ),
        'loc_778',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_6DB',
    )

    ChrTalk(
        0x000B,
        (
            '夫人昏睡不起，\n',
            '可老板还是像平常一样地工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '不过和平时相比，\n',
            '精神还是差很多啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_778')

    def _loc_6DB(): pass

    label('loc_6DB')

    ChrTalk(
        0x000B,
        (
            '夫人昏睡不起，\n',
            '可老板还是像平常一样地工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '不过和平时相比，\n',
            '精神还是差很多啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '伊莉莎也为了照顾夫人\n',
            '一直待在二楼……\n',
            '现在就得靠我努力了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_778(): pass

    label('loc_778')

    TalkEnd(0x000B)

    Return()

# id: 0x0005 offset: 0x77C
@scena.Code('func_05_77C')
def func_05_77C():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 2, 0x1812)),
            Expr.Return,
        ),
        'loc_9BD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0312, 4, 0x1894)),
            Expr.Return,
        ),
        'loc_807',
    )

    ChrTalk(
        0x00FE,
        (
            '在这么消沉的夜晚，\n',
            '酒馆可不能关门。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为大家都怀抱着不安\n',
            '聚集在这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '抱歉，托露塔就\n',
            '就拜托你们照顾了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9BD')

    def _loc_807(): pass

    label('loc_807')

    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x00FE, 0x0101, 0)
    Sleep(400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0312, 3, 0x1893)),
            Expr.Return,
        ),
        'loc_84D',
    )

    ChrTalk(
        0x00FE,
        (
            '哟，是艾丝蒂尔你们啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_878')

    def _loc_84D(): pass

    label('loc_84D')

    ChrTalk(
        0x00FE,
        (
            '哟，艾丝蒂尔和雪拉扎德。\n',
            '好久不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_878(): pass

    label('loc_878')

    ChrTalk(
        0x0101,
        (
            '#1003F德瑟鲁大叔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '抱歉，托露塔就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我也想过今晚\n',
            '要不要关门……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过在这么消沉的夜晚，\n',
            '大家都想来喝上一杯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '作为城里唯一的酒馆，\n',
            '自然不能关门。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1010F这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1002F嗯……明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F如果发现了什么\n',
            '我们会再来通知的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0103, 400)

    ChrTalk(
        0x00FE,
        (
            '……嗯，谢谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就靠你们了，游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1894)

    def _loc_9BD(): pass

    label('loc_9BD')

    TalkEnd(0x000A)

    Return()

# id: 0x0006 offset: 0x9C1
@scena.Code('func_06_9C1')
def func_06_9C1():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 4, 0x1814)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_9D0',
    )

    Call(0, 0x0010)

    Jump('loc_A1A')

    def _loc_9D0(): pass

    label('loc_9D0')

    TalkBegin(0x0009)

    ChrTalk(
        0x0009,
        (
            '艾丝蒂尔～\n',
            '妈妈就拜托了',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '我已经不要紧了，\n',
            '请你们努力调查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0009)

    def _loc_A1A(): pass

    label('loc_A1A')

    Return()

# id: 0x0007 offset: 0xA1B
@scena.Code('func_07_A1B')
def func_07_A1B():
    TalkBegin(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 2, 0x1812)),
            Expr.Return,
        ),
        'loc_B3A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_A85',
    )

    ChrTalk(
        0x00FE,
        (
            '今天的雾……\n',
            '我以前从没见过这么厉害的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果明天也不天晴，\n',
            '真不想去工作啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B3A')

    def _loc_A85(): pass

    label('loc_A85')

    ChrTalk(
        0x00FE,
        (
            '嘎嘎嘎嘎…\n',
            '…包子…虽然很好吃……嘎嘎',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啪咕啪啪咕啪…\n',
            '今…今天…的雾…雾真的…咕咕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '咯咯咯咯咯咯咯咯…\n',
            '如…如果明天…也不晴……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '…………嗝。\n',
            '真不想去工作啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    def _loc_B3A(): pass

    label('loc_B3A')

    TalkEnd(0x000C)

    Return()

# id: 0x0008 offset: 0xB3E
@scena.Code('func_08_B3E')
def func_08_B3E():
    TalkBegin(0x000D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 2, 0x1812)),
            Expr.Return,
        ),
        'loc_C8D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_B97',
    )

    ChrTalk(
        0x00FE,
        (
            '也没必要翘班\n',
            '过来吃饭吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真希望他能把这股子劲用在工作上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C8D')

    def _loc_B97(): pass

    label('loc_B97')

    ChrTalk(
        0x00FE,
        (
            '提恩特那家伙……\n',
            '今天又迟到了很久。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他的理由是在雾中迷路了，不过\n',
            '真正的原因肯定是去吃东西了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那家伙的贪吃\n',
            '可是有名的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样在工作中溜出矿山\n',
            '跑到这里来吃饭的那股劲儿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是用在工作中的话，\n',
            '他的作用起码是现在的十倍。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)

    def _loc_C8D(): pass

    label('loc_C8D')

    TalkEnd(0x000D)

    Return()

# id: 0x0009 offset: 0xC91
@scena.Code('func_09_C91')
def func_09_C91():
    TalkBegin(0x000E)
    ClearChrFlags(0x00FE, 0x0010)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x5A),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_CB6',
    )

    SetChrSubChip(0x00FE, 2)

    Jump('loc_CD1')

    def _loc_CB6(): pass

    label('loc_CB6')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x10E),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_CCC',
    )

    SetChrSubChip(0x00FE, 2)

    Jump('loc_CD1')

    def _loc_CCC(): pass

    label('loc_CCC')

    SetChrSubChip(0x00FE, 1)

    def _loc_CD1(): pass

    label('loc_CD1')

    OP_8C(0x00FE, 90, 0)
    SetChrFlags(0x00FE, 0x0010)

    If(
        (
            (Expr.Eval, "OP_29(0x0074, 0x01, 0x0100)"),
            Expr.Return,
        ),
        'loc_DE4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_D46',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然对不起乘客，\n',
            '不过天气不好也没有办法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在最多也就是祈求\n',
            '雾赶快散去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DE1')

    def _loc_D46(): pass

    label('loc_D46')

    ChrTalk(
        0x00FE,
        (
            '哟，这不是\n',
            '游击士们吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们这些乘务员今天\n',
            '也都停留在洛连特。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总之在天气恢复之前，\n',
            '只能保持这个状态了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总之现在只能\n',
            '祈求女神了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0004)

    def _loc_DE1(): pass

    label('loc_DE1')

    Jump('loc_FC6')

    def _loc_DE4(): pass

    label('loc_DE4')

    If(
        (
            (Expr.Eval, "OP_29(0x0074, 0x01, 0x0040)"),
            Expr.Return,
        ),
        'loc_E61',
    )

    ChrTalk(
        0x00FE,
        (
            '怎么？这回是\n',
            '来找索斯摩夫的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那家伙刚才\n',
            '回了飞船坪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他这人有点古怪，\n',
            '一定待在一些奇怪的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FC6')

    def _loc_E61(): pass

    label('loc_E61')

    If(
        (
            (Expr.Eval, "OP_29(0x0074, 0x01, 0x0010)"),
            Expr.Return,
        ),
        'loc_ECD',
    )

    ChrTalk(
        0x00FE,
        (
            '你们在找库因特吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那家伙很早就\n',
            '吃完饭出去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哼，肯定又是翘班\n',
            '在街上闲逛吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FC6')

    def _loc_ECD(): pass

    label('loc_ECD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_F2B',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然对不起乘客，\n',
            '不过天气不好也没有办法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在最多也就是祈求\n',
            '雾赶快散去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FC6')

    def _loc_F2B(): pass

    label('loc_F2B')

    ChrTalk(
        0x00FE,
        (
            '哟，这不是\n',
            '游击士们吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们这些乘务员今天\n',
            '也都停留在洛连特。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总之在天气恢复之前，\n',
            '只能保持这个状态了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总之现在只能\n',
            '祈求女神了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0004)

    def _loc_FC6(): pass

    label('loc_FC6')

    SetChrSubChip(0x00FE, 0)
    TalkEnd(0x000E)

    Return()

# id: 0x000A offset: 0xFCF
@scena.Code('func_0A_FCF')
def func_0A_FCF():
    TalkBegin(0x000F)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 2, 0x1812)),
            Expr.Return,
        ),
        'loc_1043',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_1002',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，到底什么时候\n',
            '出发呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1043')

    def _loc_1002(): pass

    label('loc_1002')

    ChrTalk(
        0x00FE,
        (
            '呼，到底什么时候\n',
            '出发呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我实在是\n',
            '等得受不了了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0005)

    def _loc_1043(): pass

    label('loc_1043')

    TalkEnd(0x000F)

    Return()

# id: 0x000B offset: 0x1047
@scena.Code('func_0B_1047')
def func_0B_1047():
    TalkBegin(0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 2, 0x1812)),
            Expr.Return,
        ),
        'loc_13D0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 6, 0x1816)),
            Expr.Return,
        ),
        'loc_13A0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0313, 0, 0x1898)),
            Expr.Return,
        ),
        'loc_10BE',
    )

    ChrTalk(
        0x00FE,
        (
            '那时候我要是在钟楼\n',
            '就不会让小家伙上去了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '偏偏在那种时候离开，\n',
            '我真生自己的气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_139D')

    def _loc_10BE(): pass

    label('loc_10BE')

    ClearChrFlags(0x00FE, 0x0010)

    ChrTalk(
        0x00FE,
        (
            '鲁克那小家伙还好吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真希望他没事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1002F……目前看来还可以。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '虽然没有醒，\n',
            '不过只是睡着了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    OP_63(0x00FE)
    ChrTurnDirection(0x00FE, 0x0101, 400)
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '哟，这不是卡西乌斯的\n',
            '调皮女儿吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是吗……\n',
            '你去看过小家伙了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1000F嗯，协会正在调查。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '是潘杜爷爷您把\n',
            '鲁克送回家的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他在钟楼上\n',
            '昏倒了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F当时有没有\n',
            '发生什么奇怪的事？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '就算是些细微的小事\n',
            '也请告诉我们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0103, 400)

    ChrTalk(
        0x00FE,
        (
            '唔，可是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我当时满脑子都在想\n',
            '鲁克的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '很遗憾，其他的事\n',
            '都记不得了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1015F是吗……\n',
            '嗯，人在那时都会那样的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '抱歉，帮不了你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F不，能确认到没发生\n',
            '什么特别的事已经很好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '感谢您的合作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1016F可别喝太多哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，这我知道。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么就这样。\n',
            '你们也要小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1898)

    def _loc_139D(): pass

    label('loc_139D')

    Jump('loc_13D0')

    def _loc_13A0(): pass

    label('loc_13A0')

    ChrTalk(
        0x00FE,
        (
            '鲁克那小家伙还好吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真希望他没事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_13D0(): pass

    label('loc_13D0')

    TalkEnd(0x0010)

    Return()

# id: 0x000C offset: 0x13D4
@scena.Code('func_0C_13D4')
def func_0C_13D4():
    TalkBegin(0x0011)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 2, 0x1812)),
            Expr.Return,
        ),
        'loc_1480',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_1421',
    )

    ChrTalk(
        0x00FE,
        (
            '呼……吃饱了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '肚子也胀起来了，\n',
            '得赶紧回去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1480')

    def _loc_1421(): pass

    label('loc_1421')

    ChrTalk(
        0x00FE,
        (
            '呼……吃饱了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好久没吃过这么\n',
            '象样的晚饭了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '肚子也胀起来了，\n',
            '得赶紧回去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0006)

    def _loc_1480(): pass

    label('loc_1480')

    TalkEnd(0x0011)

    Return()

# id: 0x000D offset: 0x1484
@scena.Code('func_0D_1484')
def func_0D_1484():
    UnlockAchievement(0x01, 0x08, 0x00, 0x00)
    TalkBegin(0x0012)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 2, 0x1812)),
            Expr.Return,
        ),
        'loc_156B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_14E3',
    )

    ChrTalk(
        0x00FE,
        (
            '明天起得收集那位\n',
            '小姐的情报。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，想要认识她\n',
            '首先要有努力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_156B')

    def _loc_14E3(): pass

    label('loc_14E3')

    ChrTalk(
        0x00FE,
        (
            '啊，金发的小姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真想不到会有\n',
            '那么动人的女性……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '偶然发生在乡间的\n',
            '冲动的相遇……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这已经是女神的引导\n',
            '和命令了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0007)

    def _loc_156B(): pass

    label('loc_156B')

    TalkEnd(0x0012)

    Return()

# id: 0x000E offset: 0x156F
@scena.Code('func_0E_156F')
def func_0E_156F():
    TalkBegin(0x0013)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 2, 0x1812)),
            Expr.Return,
        ),
        'loc_166E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_15CB',
    )

    ChrTalk(
        0x00FE,
        (
            '我那个同伴\n',
            '好像对谁一见钟情了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过他经常这样，\n',
            '也不用介意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_166E')

    def _loc_15CB(): pass

    label('loc_15CB')

    ChrTalk(
        0x00FE,
        (
            '总觉得我那个同伴……\n',
            '好像对谁一见钟情了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今晚他又要\n',
            '张口闭口提那个女人了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过他经常这样，\n',
            '也不用介意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '忽冷忽热的……\n',
            '安敦就是这样的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0008)

    def _loc_166E(): pass

    label('loc_166E')

    TalkEnd(0x0013)

    Return()

# id: 0x000F offset: 0x1672
@scena.Code('func_0F_1672')
def func_0F_1672():
    EventBegin(0x00)
    OP_DB()
    SetChrFlags(0x0000, 0x0080)
    SetChrFlags(0x0001, 0x0080)
    SetChrFlags(0x0002, 0x0080)
    SetChrFlags(0x0003, 0x0080)
    OP_4A(0x0008, 255)
    OP_6F(0x0000, 10)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0008, 0x0002)
    SetChrSubChip(0x0008, 2)
    SetChrPos(0x0008, 88620, 0, 79000, 270)
    SetChrPos(0x0009, 87090, 0, 79170, 90)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    OP_6D(82660, 0, 80340, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    FadeIn(1000, 0)
    OP_6D(86990, 0, 80450, 3000)
    OP_0D()
    FadeOut(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x0000, 0x0080)
    ClearChrFlags(0x0001, 0x0080)
    ClearChrFlags(0x0002, 0x0080)
    ClearChrFlags(0x0003, 0x0080)
    OP_DC()
    OP_A2(0x10F0)
    NewScene('ED6_DT21/T0112._SN', 106, 0, 0)
    IdleLoop()

    Return()

# id: 0x0010 offset: 0x1754
@scena.Code('func_10_1754')
def func_10_1754():
    EventBegin(0x00)
    OP_4A(0x0009, 255)
    Fade(1000)
    SetChrPos(0x0101, 86750, 0, 80570, 180)
    SetChrPos(0x0103, 87440, 0, 80930, 180)
    SetChrPos(0x00F8, 85880, 0, 80850, 135)
    SetChrPos(0x00F9, 85060, 0, 80750, 135)
    OP_8C(0x0009, 0, 0)
    OP_6D(86420, 0, 80630, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_187A',
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
        0,
        (
            TXT(0x00, '【◇没和伊莉莎再会】\n'),
            TXT(0x01, '【◇已和伊莉莎再会】\n'),
            TXT(0x02, '【◇不变更】\n'),
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
        (0x00000000, 'loc_186E'),
        (0x00000001, 'loc_1874'),
        (-1, 'loc_187A'),
    )

    def _loc_186E(): pass

    label('loc_186E')

    OP_A3(0x1882)

    Jump('loc_187A')

    def _loc_1874(): pass

    label('loc_1874')

    OP_A2(0x1882)

    Jump('loc_187A')

    def _loc_187A(): pass

    label('loc_187A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0310, 2, 0x1882)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_19C6',
    )

    ChrTalk(
        0x00FE,
        (
            '#3380281551V#6P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010281552V#1008F嗯……\n',
            '好久不见，伊莉莎。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3380281553V#6P哇，艾丝蒂尔！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3380281554V#6P太好了～\n',
            '看来训练顺利结束了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3380281555V#6P担心死我了～\n',
            '你总算是回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010281556V#1016F对不起，\n',
            '这么晚才来跟你见面。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010281557V#1015F先不说这个了……\n',
            '阿姨的情况怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A44')

    def _loc_19C6(): pass

    label('loc_19C6')

    ChrTalk(
        0x00FE,
        (
            '#3380281558V#6P啊，艾丝蒂尔，\n',
            '还有雪拉扎德小姐？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010281559V#1025F晚上好，伊莉莎。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010281560V阿姨的情况怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A44(): pass

    label('loc_1A44')

    ChrTalk(
        0x00FE,
        (
            '#3380281561V#6P唔～看上去只是在\n',
            '安稳地睡觉……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3380281562V#6P不管是摇她还是叫她，\n',
            '她一点反应都没有～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3380281563V#6P教区长先生虽然说\n',
            '不必担心……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010281564V#1003F是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030281565V#020F#2P我们是受市长先生的委托\n',
            '来调查此事件的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030281566V能不能请你配合一下？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3380281567V#6P啊、好，当然没问题～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3380281568V#6P请随便问吧～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010281569V#1015F那么……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010281570V#1002F首先，阿姨是在\n',
            '何时何地昏倒在地的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3380281571V#6P啊，嗯……～？\n',
            '时间是傍晚的５点左右吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3380281572V#6P我和妈妈在外面的阳台上\n',
            '收拾椅子什么的～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030281573V#023F#2P阳台上的椅子？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3380281574V#6P嗯，这种雾天\n',
            '不是很潮湿吗～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3380281575V#6P好不容易糊好了一楼的墙壁，\n',
            '想想二楼的椅子也该收拾一下～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030281576V#026F#2P原来如此……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3380281577V#6P在收拾的过程中\n',
            '爸爸叫我下楼去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3380281578V#6P再回来时妈妈已经\n',
            '靠在椅子上睡着了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010281579V#1002F是这样啊……\n',
            '阿姨睡着时你不在场？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3380281580V#6P嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3380281581V#6P然后我怎么叫她\n',
            '她也不醒……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3380281582V#6P我就赶紧叫来爸爸\n',
            '把她背到了二楼的床上……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3380281583V#6P然后……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3380281584V#6P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010281585V#1025F伊莉莎……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrFlags(0x0009, 0x0040)
    OP_8F(0x0101, 87060, 0, 79640, 1000, 0x00)
    SetChrFlags(0x0101, 0x0080)
    SetChrFlags(0x0009, 0x0002)
    SetChrChipByIndex(0x0009, 4)
    SetChrSubChip(0x0009, 0)
    Sleep(500)

    OP_99(0x0009, 0x01, 0x02, 0x000003E8)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '#3380281586V#6P呵呵，对不起……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3380281587V#6P看到艾丝蒂尔你们来了\n',
            '总算松了一口气……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010281588V#1012F#5P嗯……我知道。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010281589V不会有事的，不要勉强自己。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3380281580V#6P嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0009, 0x02, 0x00, 0x000003E8)
    Sleep(500)

    ClearChrFlags(0x0101, 0x0080)
    ClearChrFlags(0x0009, 0x0002)
    SetChrChipByIndex(0x0009, 1)
    SetChrSubChip(0x0009, 0)
    OP_8F(0x0101, 87000, 0, 79980, 1000, 0x00)
    Sleep(500)

    ChrTalk(
        0x00FE,
        (
            '#3380281591V#6P谢谢～我已经没事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3380281592V#6P还有没有什么其他要问的吗～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearChrFlags(0x0009, 0x0040)

    ChrTalk(
        0x0101,
        (
            '#0010281593V#1007F#5P唔…让我想想。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010281594V#1015F雪拉姐，你呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030281595V#026F#2P是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030281596V#022F在你妈妈昏睡前后\n',
            '有没有发生过什么怪事？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030281597V比如有陌生人来过之类的，\n',
            '或者听到怪异的声音？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3380281598V#6P陌生人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3380281599V#6P说起来，我被爸爸\n',
            '叫下楼的时候……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3380281600V#6P我看到有个女人\n',
            '从钟楼走出来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030281601V#023F#2P女人……\n',
            '是洛连特的人吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3380281602V#6P不，虽然她站在雾中，\n',
            '看不清脸……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3380281603V#6P不过她的服饰设计得很不可思议，\n',
            '我觉得像是旅行者～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010281604V#1004F#5P设计得不可思议……\n',
            '哪里不可思议？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3380281605V#6P唔，像是舒适的\n',
            '黑色礼服……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3380281606V#6P不过雾那么浓，\n',
            '具体细节实在看不清～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010281607V#1006F#5P是吗……\n',
            '不过这可能是重要的目击情报，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010281608V得去向爱娜姐报告一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030281609V#026F#2P嗯……是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030281610V#020F谢谢你，伊莉莎。\n',
            '告诉了我们这么多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3380281611V#6P啊，哪里哪里～\n',
            '你们工作辛苦了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010281612V#1006F#5P阿姨的事\n',
            '就交给我们吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010281613V我们一定会找出\n',
            '办法让她醒过来的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3380281614V#6P嗯……\n',
            '谢谢你～艾丝蒂尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_6D(82980, 0, 80630, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    SetChrPos(0x0101, 82980, 0, 80630, 270)
    SetChrPos(0x0103, 82980, 0, 80630, 270)
    SetChrPos(0x00F8, 82980, 0, 80630, 270)
    SetChrPos(0x00F9, 82980, 0, 80630, 270)
    OP_8C(0x0009, 90, 0)
    OP_4B(0x0009, 255)
    CreateThread(0x0009, 0x00, 0x00, 0x0002)
    OP_A2(0x1814)
    OP_28(0x0090, 0x02, 0x0008)
    OP_28(0x0090, 0x01, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 3, 0x1813)),
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 4, 0x1814)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 5, 0x1815)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 6, 0x1816)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2599',
    )

    OP_28(0x0090, 0x01, 0x0200)

    Jump('loc_2599')

    def _loc_2599(): pass

    label('loc_2599')

    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
