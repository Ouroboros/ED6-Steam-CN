import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T3117_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3117   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '雷伊'),
    TXT(0x02, '蒂亚利'),
    TXT(0x03, '安东尼'),
    TXT(0x04, '运动鞋'),
    TXT(0x05, '书3'),
    TXT(0x06, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'T3117.x'
    header.mapIndex       = 1
    header.bgm            = 13
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT01/T3117._SN', 'ED6_DT01/T3117_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x2513
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
        ('ED6_DT07/CH01220._CH', 'ED6_DT07/CH01220P._CP'),
        ('ED6_DT07/CH01660._CH', 'ED6_DT07/CH01660P._CP'),
        ('ED6_DT07/CH01700._CH', 'ED6_DT07/CH01700P._CP'),
        ('ED6_DT06/CH20021._CH', 'ED6_DT06/CH20021P._CP'),
    ]

# id: 0x10002 offset: 0xCA
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
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
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
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            x                   = -3620,
            z                   = 750,
            y                   = 9560,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1441795,
            chipIndex           = 3,
            npcIndex            = 0x0146,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -410,
            z                   = 800,
            y                   = 6880,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1835011,
            chipIndex           = 3,
            npcIndex            = 0x0146,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x16A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x16A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x16A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 770,
            triggerZ            = 0,
            triggerY            = 14240,
            triggerRange        = 1200,
            actorX              = 770,
            actorZ              = 0,
            actorY              = 14240,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0009,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 4600,
            triggerZ            = 1000,
            triggerY            = 12780,
            triggerRange        = 1200,
            actorX              = 5880,
            actorZ              = 2000,
            actorY              = 13200,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -410,
            triggerZ            = 0,
            triggerY            = 6880,
            triggerRange        = 1200,
            actorX              = -410,
            actorZ              = 800,
            actorY              = 6880,
            flags               = 0x007C,
            talkScenaIndex      = 0x0001,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x1D6
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_20C',
    )

    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, 1060, 0, 9420, 253)
    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x0009, -2800, 0, 9310, 270)

    Jump('loc_3DE')

    def _loc_20C(): pass

    label('loc_20C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_242',
    )

    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, 1060, 0, 9420, 253)
    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x0009, -2800, 0, 9310, 270)

    Jump('loc_3DE')

    def _loc_242(): pass

    label('loc_242')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_278',
    )

    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, 1060, 0, 9420, 253)
    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x0009, -2800, 0, 9310, 270)

    Jump('loc_3DE')

    def _loc_278(): pass

    label('loc_278')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_29F',
    )

    ClearChrFlags(0x000A, 0x0080)
    SetChrPos(0x000A, 500, 0, 2880, 271)
    CreateThread(0x000A, 0x00, 0x00, 0x0003)

    Jump('loc_3DE')

    def _loc_29F(): pass

    label('loc_29F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 6, 0x536)),
            Expr.Return,
        ),
        'loc_2D5',
    )

    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, 4600, 1000, 13110, 69)
    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x0009, -2800, 0, 9310, 270)

    Jump('loc_3DE')

    def _loc_2D5(): pass

    label('loc_2D5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_2DF',
    )

    Jump('loc_3DE')

    def _loc_2DF(): pass

    label('loc_2DF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_2FF',
    )

    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x0009, -2800, 0, 9310, 270)

    Jump('loc_3DE')

    def _loc_2FF(): pass

    label('loc_2FF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_33A',
    )

    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, 1060, 0, 9420, 253)
    SetChrFlags(0x0008, 0x0010)
    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x0009, -2800, 0, 9310, 270)

    Jump('loc_3DE')

    def _loc_33A(): pass

    label('loc_33A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_370',
    )

    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, 1060, 0, 9420, 253)
    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x0009, -2800, 0, 9310, 270)

    Jump('loc_3DE')

    def _loc_370(): pass

    label('loc_370')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Return,
        ),
        'loc_3AB',
    )

    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, 1060, 0, 9420, 253)
    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x0009, -2790, 0, 9200, 270)
    SetChrFlags(0x0009, 0x0010)

    Jump('loc_3DE')

    def _loc_3AB(): pass

    label('loc_3AB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_3DE',
    )

    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, 1060, 0, 9420, 253)
    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x0009, -2800, 0, 9310, 270)

    def _loc_3DE(): pass

    label('loc_3DE')

    If(
        (
            (Expr.Eval, "OP_29(0x002A, 0x01, 0x0001)"),
            Expr.Return,
        ),
        'loc_3EE',
    )

    SetChrFlags(0x000B, 0x0080)

    def _loc_3EE(): pass

    label('loc_3EE')

    SetChrFlags(0x000C, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x002D, 0x01, 0x0008)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_409',
    )

    ClearChrFlags(0x000C, 0x0080)

    def _loc_409(): pass

    label('loc_409')

    Return()

# id: 0x0001 offset: 0x40A
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A7, 2, 0x53A)),
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 0, 0x558)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_422',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x54),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_44F')

    def _loc_422(): pass

    label('loc_422')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 2, 0x532)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 6, 0x536)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_43A',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x52),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_44F')

    def _loc_43A(): pass

    label('loc_43A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 4, 0x52C)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 2, 0x532)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_44F',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x51),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_44F(): pass

    label('loc_44F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 4, 0x52C)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 6, 0x536)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_502',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 2, 0x532)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4FF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A9, 3, 0x54B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4FB',
    )

    LoadEffect(0x01, 'map\\\\mpfog.eff')
    PlayEffect(0x01, 0x01, 0x00FF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    LoadEffect(0x00, 'map\\\\mpsmk0.eff')
    PlayEffect(0x00, 0x00, 0x00FF, 770, 0, 14240, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    Jump('loc_4FF')

    def _loc_4FB(): pass

    label('loc_4FB')

    OP_64(0x00, 0x0001)

    def _loc_4FF(): pass

    label('loc_4FF')

    Jump('loc_506')

    def _loc_502(): pass

    label('loc_502')

    OP_64(0x00, 0x0001)
    def _loc_506(): pass

    label('loc_506')

    OP_64(0x02, 0x0001)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x002D, 0x00, 0x04)"),
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x002D, 0x01, 0x0008)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_526',
    )

    OP_65(0x02, 0x0001)

    def _loc_526(): pass

    label('loc_526')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_531',
    )

    OP_64(0x01, 0x0001)

    def _loc_531(): pass

    label('loc_531')

    Return()

# id: 0x0002 offset: 0x532
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_547',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_547(): pass

    label('loc_547')

    Return()

# id: 0x0003 offset: 0x548
@scena.Code('func_03_548')
def func_03_548():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_56B',
    )

    OP_8D(0x00FE, -2990, 4830, 3120, 870, 3000)

    Jump('func_03_548')

    def _loc_56B(): pass

    label('loc_56B')

    Return()

# id: 0x0004 offset: 0x56C
@scena.Code('func_04_56C')
def func_04_56C():
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
        'loc_60B',
    )

    SetMapFlags(0x00000080)
    FadeOut(300, 0, 100)

    ExecExpressionWithReg(
        0x0001,
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

    MenuEnd(0x0001)
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
            (Expr.PushReg, 0x1),
            Expr.Return,
        ),
        (0x00000000, 'loc_5F6'),
        (0x00000001, 'loc_600'),
        (-1, 'loc_60A'),
    )

    def _loc_5F6(): pass

    label('loc_5F6')

    Call(0, 0x0006)
    TalkEnd(0x00FE)

    Jump('loc_60A')

    def _loc_600(): pass

    label('loc_600')

    Call(1, 0x0003)
    TalkEnd(0x00FE)

    Jump('loc_60A')

    def _loc_60A(): pass

    label('loc_60A')

    Return()

    def _loc_60B(): pass

    label('loc_60B')

    Call(0, 0x0006)
    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0x613
@scena.Code('func_05_613')
def func_05_613():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_630',
    )

    PlaySE(402, 0x00, 0x64)

    ChrTalk(
        0x00FE,
        (
            '喵呀呵。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_630(): pass

    label('loc_630')

    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0x634
@scena.Code('func_06_634')
def func_06_634():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_6B7',
    )

    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '不管怎么说，\n',
            '这次真是辛苦你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '得到了最低限度的资料，\n',
            '总会对研究有一点帮助的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，你们请多保重。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1234')

    def _loc_6B7(): pass

    label('loc_6B7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_709',
    )

    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '辛苦了。\n',
            '你们做得很好，帮了我大忙啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，你们请多保重。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1234')

    def _loc_709(): pass

    label('loc_709')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_811',
    )

    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_7AE',
    )

    ChrTalk(
        0x00FE,
        (
            '我好不容易积攒了\n',
            '下一阶段的研究费……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '雷伊前辈打算就靠那个西红柿\n',
            '混过下个阶段的研究吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '运、运动鞋的研究\n',
            '我也必须要努力才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_80E')

    def _loc_7AE(): pass

    label('loc_7AE')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '真、真是难以置信，\n',
            '那个苦西红柿\n',
            '竟然也有人要订货。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……这、这个世界\n',
            '到底是怎么了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_80E(): pass

    label('loc_80E')

    Jump('loc_1234')

    def _loc_811(): pass

    label('loc_811')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_9B0',
    )

    TalkBegin(0x00FE)

    If(
        (
            (Expr.Eval, "OP_29(0x002A, 0x00, 0x10)"),
            (Expr.Eval, "OP_29(0x002A, 0x00, 0x08)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_8BC',
    )

    ChrTalk(
        0x00FE,
        (
            '为了得到研究的预算，\n',
            '不得不多少谎报一些事情……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可是我自己\n',
            '并不擅长说谎啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在进行的运动鞋研究\n',
            '说什么也要做出实际的成绩来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9AD')

    def _loc_8BC(): pass

    label('loc_8BC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_941',
    )

    ChrTalk(
        0x00FE,
        (
            '为了得到研究的预算，\n',
            '果然还是要多少谎报一些事情吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过像雷伊前辈那样\n',
            '基本上全是谎报的，\n',
            '我还是觉得有点过分了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9AD')

    def _loc_941(): pass

    label('loc_941')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '唔～\n',
            '为了得到研究的预算，\n',
            '果然还是要多少谎报一些事情吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……可是说起来\n',
            '我自己也不擅长说谎啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9AD(): pass

    label('loc_9AD')

    Jump('loc_1234')

    def _loc_9B0(): pass

    label('loc_9B0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_B17',
    )

    TalkBegin(0x00FE)

    If(
        (
            (Expr.Eval, "OP_29(0x002A, 0x00, 0x10)"),
            (Expr.Eval, "OP_29(0x002A, 0x00, 0x08)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_A70',
    )

    ChrTalk(
        0x00FE,
        (
            '真是的，\n',
            '雷伊前辈，适可而止吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可是，就靠那样的研究题材\n',
            '也能得到不错的评价，\n',
            '不能不说前辈很厉害。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我也要以运动鞋的开发\n',
            '作为新的起点再加把劲了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B14')

    def _loc_A70(): pass

    label('loc_A70')

    ChrTalk(
        0x00FE,
        (
            '真是的，\n',
            '雷伊前辈，适可而止吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可是，就靠那样的研究题材\n',
            '也能得到不错的评价，\n',
            '不能不说前辈很厉害。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那种没有节制的随机应变，\n',
            '我要稍微学习一下才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B14(): pass

    label('loc_B14')

    Jump('loc_1234')

    def _loc_B17(): pass

    label('loc_B17')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 6, 0x536)),
            Expr.Return,
        ),
        'loc_C50',
    )

    TalkBegin(0x00FE)

    If(
        (
            (Expr.Eval, "OP_29(0x002A, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_B90',
    )

    ChrTalk(
        0x00FE,
        (
            '呼～\n',
            '实验室没有受害真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且测试也顺利完成了，\n',
            '可以按照日程来进行下面的工作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C4D')

    def _loc_B90(): pass

    label('loc_B90')

    If(
        (
            (Expr.Eval, "OP_29(0x002A, 0x00, 0x08)"),
            Expr.Return,
        ),
        'loc_C01',
    )

    ChrTalk(
        0x00FE,
        (
            '呼～\n',
            '实验室没有受害真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样一来，测试结束之后\n',
            '就可以按照日程来进行下面的工作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C4D')

    def _loc_C01(): pass

    label('loc_C01')

    ChrTalk(
        0x00FE,
        (
            '哈～～太好了。\n',
            '实验室没有什么变化。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '制造商送来的样品\n',
            '也毫发无损。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C4D(): pass

    label('loc_C4D')

    Jump('loc_1234')

    def _loc_C50(): pass

    label('loc_C50')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_DF7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_CB8',
    )

    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#2040180249V那么，\n',
            '测试就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2040180070V抱着踏破鞋底的决心\n',
            '去好好测试吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DF4')

    def _loc_CB8(): pass

    label('loc_CB8')

    If(
        (
            (Expr.Eval, "OP_29(0x002A, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_D30',
    )

    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '哎呀，真是辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这次你们干得不错，\n',
            '帮了我大忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '再过不久成品就能上市了，\n',
            '敬请期待哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DF4')

    def _loc_D30(): pass

    label('loc_D30')

    If(
        (
            (Expr.Eval, "OP_29(0x002A, 0x00, 0x08)"),
            Expr.Return,
        ),
        'loc_DA3',
    )

    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#2040180254V嗨～运动鞋的状况怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2040180255V到各个地方去转一转，\n',
            '然后回到我这里来报告就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DF4')

    def _loc_DA3(): pass

    label('loc_DA3')

    If(
        (
            (Expr.Eval, "OP_29(0x002A, 0x00, 0x02)"),
            Expr.Return,
        ),
        'loc_DB4',
    )

    Call(1, 0x0002)

    Jump('loc_DF4')

    def _loc_DB4(): pass

    label('loc_DB4')

    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '嗯？什么事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是来找雷伊前辈的吗？\n',
            '他出去吃午饭了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_DF4(): pass

    label('loc_DF4')

    Jump('loc_1234')

    def _loc_DF7(): pass

    label('loc_DF7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_FC7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_E5F',
    )

    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#2040180249V那么，\n',
            '测试就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2040180070V抱着踏破鞋底的决心\n',
            '去好好测试吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FC4')

    def _loc_E5F(): pass

    label('loc_E5F')

    If(
        (
            (Expr.Eval, "OP_29(0x002A, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_ED7',
    )

    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '哎呀，真是辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这次你们干得不错，\n',
            '帮了我大忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '再过不久成品就能上市了，\n',
            '敬请期待哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FC4')

    def _loc_ED7(): pass

    label('loc_ED7')

    If(
        (
            (Expr.Eval, "OP_29(0x002A, 0x00, 0x08)"),
            Expr.Return,
        ),
        'loc_F4A',
    )

    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#2040180254V嗨～运动鞋的状况怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2040180255V到各个地方去转一转，\n',
            '然后回到我这里来报告就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FC4')

    def _loc_F4A(): pass

    label('loc_F4A')

    If(
        (
            (Expr.Eval, "OP_29(0x002A, 0x00, 0x02)"),
            Expr.Return,
        ),
        'loc_F5B',
    )

    Call(1, 0x0002)

    Jump('loc_FC4')

    def _loc_F5B(): pass

    label('loc_F5B')

    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '呼～试制品总算做好了。\n',
            '之后就是等测试人员过来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在那之前，\n',
            '我还是再调整一下鞋的内垫吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_FC4(): pass

    label('loc_FC4')

    Jump('loc_1234')

    def _loc_FC7(): pass

    label('loc_FC7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_1047',
    )

    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '哎呀～\n',
            '昨天晚上真是吓了一跳啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们正赶着做试验品，\n',
            '突然房间一片漆黑。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '当时的情况\n',
            '真是乱作一团啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1234')

    def _loc_1047(): pass

    label('loc_1047')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Return,
        ),
        'loc_112F',
    )

    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B0, 7, 0x587)),
            Expr.Return,
        ),
        'loc_10C1',
    )

    ChrTalk(
        0x00FE,
        (
            '怎、怎么觉得背后\n',
            '有一股视线盯得我如芒在背呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一定是错觉啦，错觉。\n',
            '我还是集中精力工作吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_112C')

    def _loc_10C1(): pass

    label('loc_10C1')

    ChrTalk(
        0x00FE,
        (
            '嗯，\n',
            '运动鞋内垫的素材组合\n',
            '果然是关键呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然我可以亲自进行试验，\n',
            '不过最好还是可以有个体验者……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_112C(): pass

    label('loc_112C')

    Jump('loc_1234')

    def _loc_112F(): pass

    label('loc_112F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_1234',
    )

    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '被雷伊前辈称为\n',
            '『防止瞌睡食品』的超级蔬果\n',
            '已经可以吃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然外表看上去\n',
            '只是个普通的西红柿，\n',
            '不过味道却是奇苦无比。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为的确是太苦了，\n',
            '所以睡意一下子就被扫得一干二净……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这个和用晾衣服的夹子\n',
            '制成的『防止瞌睡装置』\n',
            '是同样的原理哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1234(): pass

    label('loc_1234')

    TalkEnd(0x00FE)

    Return()

# id: 0x0007 offset: 0x1238
@scena.Code('func_07_1238')
def func_07_1238():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_13CB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_12F4',
    )

    ChrTalk(
        0x00FE,
        (
            '呵呵，一会儿就要进行\n',
            '关于『苦西红柿』的商谈呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果进行顺利的话，\n',
            '在不远的将来\n',
            '这种西红柿就会作为食材流通了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼～这样的话，\n',
            '研究费就又可以大幅增长了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_13C8')

    def _loc_12F4(): pass

    label('loc_12F4')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '呼呼，该说是天助我也呢，\n',
            '还是顺理成章呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '推广温室『苦西红柿』的\n',
            '商谈即将进行呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果进行顺利的话，\n',
            '在不远的将来\n',
            '这种西红柿就会作为食材流通了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼～这样的话，\n',
            '研究费就又可以大幅增长了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_13C8(): pass

    label('loc_13C8')

    Jump('loc_1F8D')

    def _loc_13CB(): pass

    label('loc_13CB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_1549',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_148D',
    )

    ChrTalk(
        0x00FE,
        (
            '作为下一阶段的研究主题\n',
            '来继续进行温室的开发吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……当然这只是做个样子，\n',
            '实际怎么做就凭我自己的喜好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，对于优秀的研究员来说，\n',
            '必须要具备确保足够资金的手段。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1546')

    def _loc_148D(): pass

    label('loc_148D')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '作为下一阶段的研究主题\n',
            '来继续进行温室的开发吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……当然这只是做个样子，\n',
            '实际怎么做就凭我自己的喜好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔～对了。\n',
            '试试能不能再做出其他的奇怪农作物来\n',
            '也是很有意思的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1546(): pass

    label('loc_1546')

    Jump('loc_1F8D')

    def _loc_1549(): pass

    label('loc_1549')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_16FB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_1605',
    )

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，\n',
            '终于把这次的论文完成了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '论文的题目是……\n',
            '《特殊性能食品『苦西红柿』的\n',
            '　温室栽培法和营养价值分析》。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵～\n',
            '好不容易编出了这么多词，\n',
            '我真是要陶醉了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_16F8')

    def _loc_1605(): pass

    label('loc_1605')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，这样就……行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊，各位早上好。\n',
            '这次的论文已经完成了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '论文的题目是……\n',
            '《特殊性能食品『苦西红柿』的\n',
            '　温室栽培法和营养价值分析》。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '怎么样，\n',
            '看起来挺像回事吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵～\n',
            '好不容易编出了这么多词，\n',
            '我真是要陶醉了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_16F8(): pass

    label('loc_16F8')

    Jump('loc_1F8D')

    def _loc_16FB(): pass

    label('loc_16FB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 6, 0x536)),
            Expr.Return,
        ),
        'loc_17CA',
    )

    ChrTalk(
        0x00FE,
        (
            '演算室的导力演算器\n',
            '『卡佩尔』被抢走了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过真是遗憾，\n',
            '我的西红柿们一点事也没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我本来还在\n',
            '偷偷地期待着犯人\n',
            '会对这些西红柿产生兴趣呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……看起来\n',
            '根本没有被破坏的痕迹呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F8D')

    def _loc_17CA(): pass

    label('loc_17CA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_192B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_184C',
    )

    ChrTalk(
        0x00FE,
        (
            '哎呀哎呀，\n',
            '最近蒂亚利的态度有些不对头呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '明明身边就有\n',
            '我这么一个完美的模范，\n',
            '他为什么就不会学学呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1928')

    def _loc_184C(): pass

    label('loc_184C')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '蒂亚利，差不多到该提交\n',
            '下一阶段研究主题的时间了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……这次我们做什么呢。\n',
            '你有没有什么好素材？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4A(0x0009, 255)
    OP_62(0x0009, 0x00000000, 1700, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1200)

    OP_63(0x0009)

    ChrTalk(
        0x0009,
        (
            '……不知道。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '我正忙着呢。\n',
            '你自己考虑吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearChrFlags(0x00FE, 0x0010)
    OP_4B(0x0009, 255)

    def _loc_1928(): pass

    label('loc_1928')

    Jump('loc_1F8D')

    def _loc_192B(): pass

    label('loc_192B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_1B3E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_19AF',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，\n',
            '昨天产生的那种现象很有意思啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大家都哀叹这是场灾难，\n',
            '其实这对研究者来说\n',
            '不正是个绝好的研究题材吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B3B')

    def _loc_19AF(): pass

    label('loc_19AF')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '呼，\n',
            '昨天产生的那种现象很有意思啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好像是发生了\n',
            '干涉导力场的作用……\n',
            '总之那不是普通的现象。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大家都哀叹这是场灾难，\n',
            '其实这对研究者来说\n',
            '不正是个绝好的研究题材吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0107, 400)

    ChrTalk(
        0x00FE,
        (
            '提妲小妹妹，你怎么想？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#064F嗯，是、是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0107, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0107,
        (
            '#562F……其实，\n',
            '我也觉得挺有趣的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，真不愧是提妲。\n',
            '这才像是拉赛尔博士孙女嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '和蒂亚利\n',
            '果然不是一个档次的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1B3B(): pass

    label('loc_1B3B')

    Jump('loc_1F8D')

    def _loc_1B3E(): pass

    label('loc_1B3E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Return,
        ),
        'loc_1EAD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_1BE5',
    )

    ChrTalk(
        0x00FE,
        (
            '……真是的，蒂亚利那小子。\n',
            '就会做一些多余的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，\n',
            '要不要装出一幅困难的样子\n',
            '好好求一求提妲呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#509F（……哎～真是个奇怪的人。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1EAA')

    def _loc_1BE5(): pass

    label('loc_1BE5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B0, 7, 0x587)),
            Expr.Return,
        ),
        'loc_1C5E',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，\n',
            '如果提妲不想吃的话，\n',
            '这个苦西红柿就没有用处了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就在温室里面种植着，\n',
            '你们想要的话就随便拿点吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1EAA')

    def _loc_1C5E(): pass

    label('loc_1C5E')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    SetScenaFlags(ScenaFlag(0x00B0, 7, 0x587))

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1C9A',
    )

    ChrTalk(
        0x00FE,
        (
            '呵呵，提妲小妹妹。\n',
            '你来得正好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1CDA')

    def _loc_1C9A(): pass

    label('loc_1C9A')

    ChrTurnDirection(0x00FE, 0x0107, 0)

    ChrTalk(
        0x00FE,
        (
            '哦，\n',
            '这不是提妲小妹妹嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵，你来得正好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1CDA(): pass

    label('loc_1CDA')

    ChrTalk(
        0x0107,
        (
            '#560F啊，怎么了？雷伊哥哥。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '其实在温室的实验中\n',
            '培育出了很有趣的农作物。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我很想让提妲你\n',
            '尝一尝它的味道，\n',
            '所以就特别摘了一个。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果你愿意的话，\n',
            '尝尝看怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#065F啊，雷伊哥哥。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '你说的农作物，\n',
            '是不是西红柿啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，真不愧是提妲。\n',
            '你知道得还真清楚啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#060F呵呵，是啊。\n',
            '是蒂亚利哥哥告诉我的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '他说不要上雷伊哥哥的当，\n',
            '去吃很～苦的西红柿。',
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
        0x0107,
        (
            '#064F啊，不好了。\n',
            '我现在正在\n',
            '给客人们带路呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '那么我先告辞了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1EAA(): pass

    label('loc_1EAA')

    Jump('loc_1F8D')

    def _loc_1EAD(): pass

    label('loc_1EAD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_1F8D',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯，\n',
            '这次的研究项目是新型的温室………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这真是个无聊的研究。\n',
            '简直就是浪费我的才能。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，\n',
            '在这次实验中种出了一种怪味的西红柿，\n',
            '倒是唯一令我感到欣慰的事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哼哼哼，接下来……\n',
            '这个西红柿给谁吃好呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1F8D(): pass

    label('loc_1F8D')

    TalkEnd(0x00FE)

    Return()

# id: 0x0008 offset: 0x1F91
@scena.Code('func_08_1F91')
def func_08_1F91():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1FF5',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)
    SetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '苦西红柿',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(0x0385, 1)
    OP_64(0x01, 0x0001)
    TalkEnd(0x00FF)

    def _loc_1FF5(): pass

    label('loc_1FF5')

    Return()

# id: 0x0009 offset: 0x1FF6
@scena.Code('func_09_1FF6')
def func_09_1FF6():
    EventBegin(0x00)
    SetScenaFlags(ScenaFlag(0x00A9, 3, 0x54B))
    OP_64(0x00, 0x0001)
    OP_2B(0x0041, 0x0001)
    CameraMove(770, 0, 14240, 1000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 7, 0x52F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_23DD',
    )

    SetScenaFlags(ScenaFlag(0x00A5, 7, 0x52F))

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2089',
    )

    ChrTalk(
        0x0101,
        (
            '#0010080870V#004F啊……\n',
            '约修亚，这是！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080871V#012F是刚才所说的发烟筒。\n',
            '给我看看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_21B1')

    def _loc_2089(): pass

    label('loc_2089')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_20EC',
    )

    ChrTalk(
        0x0101,
        (
            '#0010080872V#004F啊……\n',
            '约修亚，那是！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080873V#012F嗯。\n',
            '是刚才所说的发烟筒。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_21B1')

    def _loc_20EC(): pass

    label('loc_20EC')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2153',
    )

    ChrTalk(
        0x0107,
        (
            '#0070080874V#065F啊……\n',
            '哥哥，这是！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080875V#012F是刚才所说的发烟筒。\n',
            '给我看看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_21B1')

    def _loc_2153(): pass

    label('loc_2153')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_21B1',
    )

    ChrTalk(
        0x0106,
        (
            '#0050080876V#057F这个……\n',
            '就是那发烟筒吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080877V#012F阿加特兄。\n',
            '给我看看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_21B1(): pass

    label('loc_21B1')

    FadeOut(1000, 0, -1)
    OP_0D()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '约修亚很熟练地把发烟筒拆散了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetChrPos(0x0102, -160, 0, 14080, 90)
    SetChrPos(0x0101, -420, 0, 15020, 129)
    SetChrPos(0x0107, -1610, 0, 13920, 104)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 1, 0x531)),
            Expr.Return,
        ),
        'loc_222D',
    )

    SetChrPos(0x0106, -1390, 0, 12660, 34)

    def _loc_222D(): pass

    label('loc_222D')

    FadeIn(600, 0)
    StopEffect(0x00, 0x02)
    StopEffect(0x01, 0x02)
    Sleep(1000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 1, 0x531)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2308',
    )

    ChrTalk(
        0x0101,
        (
            '#0010080878V#501F哇……\n',
            '烟雾没有了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070080879V#560F约修亚哥哥，\n',
            '好厉害……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080880V#012F别的地方肯定还有\n',
            '和这个一样的发烟筒。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020080881V找到了就把它们拆散吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080882V#006FＯＫ！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23DA')

    def _loc_2308(): pass

    label('loc_2308')

    SetScenaFlags(ScenaFlag(0x00A7, 6, 0x53E))

    ChrTalk(
        0x0101,
        (
            '#0010080883V#501F哇……\n',
            '烟雾没有了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070080884V#560F约修亚哥哥，\n',
            '好厉害……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050080885V#052F哦……\n',
            '还挺有两下子的嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080886V#012F别的地方肯定还有\n',
            '和这个一样的发烟筒。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020080887V找到了就把它们拆散吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_23DA(): pass

    label('loc_23DA')

    Jump('loc_24FC')

    def _loc_23DD(): pass

    label('loc_23DD')

    FadeOut(600, 0, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '约修亚很熟练地把发烟筒拆散了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetChrPos(0x0102, -160, 0, 14080, 90)
    SetChrPos(0x0101, -420, 0, 15020, 129)
    SetChrPos(0x0107, -1610, 0, 13920, 104)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 1, 0x531)),
            Expr.Return,
        ),
        'loc_2461',
    )

    SetChrPos(0x0106, -1390, 0, 12660, 34)

    def _loc_2461(): pass

    label('loc_2461')

    StopEffect(0x00, 0x02)
    StopEffect(0x01, 0x02)
    Sleep(1000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 1, 0x531)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A7, 6, 0x53E)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_24FC',
    )

    SetScenaFlags(ScenaFlag(0x00A7, 6, 0x53E))

    ChrTalk(
        0x0106,
        (
            '#0050080888V#052F哦……\n',
            '还挺有两下子的嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080889V#012F别的地方肯定还有\n',
            '和这个一样的发烟筒。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020080890V找到了就把它们拆散吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_24FC(): pass

    label('loc_24FC')

    EventEnd(0x00)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
