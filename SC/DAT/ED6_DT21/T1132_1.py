import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T1132_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T1132_1 ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'C0403.x'
    header.mapIndex       = 1
    header.bgm            = 10
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/T1132_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
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
    ]

# id: 0x10001 offset: 0xA8
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10002 offset: 0xA8
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0xA8
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0xA8
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0xA8
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.Eval, "OP_29(0x0078, 0x00, 0x08)"),
            (Expr.Eval, "OP_29(0x0078, 0x00, 0x10)"),
            Expr.Or,
            (Expr.Eval, "OP_29(0x0078, 0x00, 0x40)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_C1',
    )

    Return()

    def _loc_C1(): pass

    label('loc_C1')

    If(
        (
            (Expr.Eval, "OP_29(0x0078, 0x00, 0x02)"),
            Expr.Return,
        ),
        'loc_E4',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0078, 0x01, 0x8000)"),
            Expr.Return,
        ),
        'loc_DD',
    )

    Call(1, 0x0002)

    Jump('loc_E1')

    def _loc_DD(): pass

    label('loc_DD')

    Call(1, 0x0001)

    def _loc_E1(): pass

    label('loc_E1')

    Jump('loc_1AF')

    def _loc_E4(): pass

    label('loc_E4')

    OP_4A(0x000B, 255)
    TalkBegin(0x000B)

    ChrTalk(
        0x000B,
        (
            '此房间现在\n',
            '归帝国大使馆使用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '闲杂人等\n',
            '请勿出入。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(1000)
    ChrSetPos(0x000B, -126260, 0, 138000, 270)
    ChrSetPos(0x00F6, -128130, 0, 138000, 270)
    ChrSetPos(0x00F7, -128130, 0, 138000, 270)
    ChrSetPos(0x00F8, -128130, 0, 138000, 270)
    ChrSetPos(0x00F9, -128130, 0, 138000, 270)

    If(
        (
            (Expr.PushValueByIndex, 0xE),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_19E',
    )

    ChrSetPos(0x0004, -128130, 0, 138000, 270)

    def _loc_19E(): pass

    label('loc_19E')

    OP_69(0x00F6, 0)
    OP_30(0x00)
    OP_0D()
    TalkEnd(0x000B)
    OP_4B(0x000B, 255)
    def _loc_1AF(): pass

    label('loc_1AF')

    Return()

# id: 0x0001 offset: 0x1B0
@scena.Code('func_01_1B0')
def func_01_1B0():
    EventBegin(0x00)
    OP_4A(0x000B, 255)
    ChrTurnDirection(0x000B, 0x0000, 0)
    ChrTurnDirection(0x0000, 0x000B, 0)
    ChrTurnDirection(0x0001, 0x000B, 0)
    ChrTurnDirection(0x0002, 0x000B, 0)
    ChrTurnDirection(0x0003, 0x000B, 0)

    If(
        (
            (Expr.PushValueByIndex, 0xE),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1EC',
    )

    ChrTurnDirection(0x0004, 0x000B, 0)

    def _loc_1EC(): pass

    label('loc_1EC')

    ChrTalk(
        0x000B,
        (
            '#3630480001V此房间现在\n',
            '归帝国大使馆使用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3630480002V闲杂人等\n',
            '请勿出入。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x0078, 0x00, 0x02)"),
            Expr.Return,
        ),
        'loc_A91',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_33A',
    )

    ChrTalk(
        0x0106,
        (
            '#0050480003V#052F这里是帝国大使馆的接待处吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3630480004V是，没错……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3630480005V有什么事情吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050480006V#050F有事的不是你们吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050480007V我们是游击士协会的游击士。\n',
            '看了公告板上的委托来到这里的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_72B')

    def _loc_33A(): pass

    label('loc_33A')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_428',
    )

    ChrTalk(
        0x0103,
        (
            '#0030480008V#020F这里是帝国大使馆的接待处吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3630480004V是，没错……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3630480005V有什么事情吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030480011V#020F有事的是你们吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030480012V我们是游击士协会的游击士。\n',
            '看了公告板上的委托来到这里的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_72B')

    def _loc_428(): pass

    label('loc_428')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_518',
    )

    ChrTalk(
        0x0108,
        (
            '#0080480013V#070F这里是帝国大使馆的接待处吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3630480004V是，没错……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3630480005V有什么事情吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080480016V#070F有事的不是你们吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080480017V我们是游击士协会的游击士。\n',
            '看了公告板上的委托来到这里的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_72B')

    def _loc_518(): pass

    label('loc_518')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_649',
    )

    ChrTalk(
        0x0104,
        (
            '#0040480018V#030F这里是帝国大使馆的接待处吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3630480004V是，没错……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3630480020V……还以为是谁呢，\n',
            '这不是奥利维尔吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3630480021V今天来大使馆有什么事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010480022V#1000F有事的\n',
            '不是你们吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480023V我们是游击士协会的游击士。\n',
            '看了公告板上的委托来到这里的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_72B')

    def _loc_649(): pass

    label('loc_649')

    ChrTalk(
        0x0101,
        (
            '#0010480024V#1011F这里是帝国大使馆的接待处？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3630480004V是，没错……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3630480005V有什么事情吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010480022V#1000F有事的\n',
            '不是你们吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480023V我们是游击士协会的游击士。\n',
            '看了公告板上的委托来到这里的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_72B(): pass

    label('loc_72B')

    ChrTalk(
        0x000B,
        (
            '#3630480029V啊，是游击士吗？\n',
            '真是失礼了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3630480030V可以的话，我想\n',
            '立即说明一下情况……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3630480031V你们方便吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_947',
    )

    ChrTalk(
        0x0101,
        (
            '#0010480032V#1007F抱、抱歉……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480033V考虑了一下，\n',
            '现在有点不方便。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3630480034V噢，这样吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3630480035V那么，事情处理完后\n',
            '麻烦再来这里吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010480036V#1000F那就先这样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480037V#1015F总之我们现在\n',
            '得先去一趟拉文努村。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(1000)
    ChrSetPos(0x000B, -126260, 0, 138000, 270)
    ChrSetPos(0x00F6, -128130, 0, 138000, 270)
    ChrSetPos(0x00F7, -128130, 0, 138000, 270)
    ChrSetPos(0x00F8, -128130, 0, 138000, 270)
    ChrSetPos(0x00F9, -128130, 0, 138000, 270)

    If(
        (
            (Expr.PushValueByIndex, 0xE),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_92D',
    )

    ChrSetPos(0x0004, -128130, 0, 138000, 270)

    def _loc_92D(): pass

    label('loc_92D')

    OP_69(0x00F6, 0)
    OP_0D()
    OP_4B(0x000B, 255)
    Sleep(50)

    EventEnd(0x04)
    OP_28(0x0078, 0x01, 0x8000)

    Return()

    def _loc_947(): pass

    label('loc_947')

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
            TXT(0x00, '【是】\n'),
            TXT(0x01, '【否】\n'),
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

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_9C3',
    )

    ChrTalk(
        0x0101,
        (
            '#0010480038V#1006F嗯，没问题哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(1, 0x0003)

    Return()

    def _loc_9C3(): pass

    label('loc_9C3')

    ChrTalk(
        0x0101,
        (
            '#0010480039V#1015F抱歉哦，\n',
            '现在可不行。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480040V我们还有其他要事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3630480034V噢，这样吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3630480035V那么，事情处理完后\n',
            '麻烦再来这里吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010480043V#1000F嗯，就先这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0078, 0x01, 0x8000)

    def _loc_A91(): pass

    label('loc_A91')

    Fade(1000)
    ChrSetPos(0x000B, -126260, 0, 138000, 270)
    ChrSetPos(0x00F6, -128130, 0, 138000, 270)
    ChrSetPos(0x00F7, -128130, 0, 138000, 270)
    ChrSetPos(0x00F8, -128130, 0, 138000, 270)
    ChrSetPos(0x00F9, -128130, 0, 138000, 270)

    If(
        (
            (Expr.PushValueByIndex, 0xE),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B08',
    )

    ChrSetPos(0x0004, -128130, 0, 138000, 270)

    def _loc_B08(): pass

    label('loc_B08')

    OP_69(0x00F6, 0)
    OP_0D()
    OP_4B(0x000B, 255)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x0002 offset: 0xB1C
@scena.Code('func_02_B1C')
def func_02_B1C():
    EventBegin(0x00)
    OP_4A(0x000B, 255)
    ChrTurnDirection(0x000B, 0x0000, 0)
    ChrTurnDirection(0x0000, 0x000B, 0)
    ChrTurnDirection(0x0001, 0x000B, 0)
    ChrTurnDirection(0x0002, 0x000B, 0)
    ChrTurnDirection(0x0003, 0x000B, 0)

    If(
        (
            (Expr.PushValueByIndex, 0xE),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B58',
    )

    ChrTurnDirection(0x0004, 0x000B, 0)

    def _loc_B58(): pass

    label('loc_B58')

    ChrTalk(
        0x000B,
        (
            '#3630480044V各位，等候多时了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3630480045V要事已经处理完了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_CA3',
    )

    ChrTalk(
        0x0101,
        (
            '#0010480046V#1007F抱、抱歉……\n',
            '还不行呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480037V#1015F总之我们现在\n',
            '得先去一趟拉文努村。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(1000)
    ChrSetPos(0x000B, -126260, 0, 138000, 270)
    ChrSetPos(0x00F6, -128130, 0, 138000, 270)
    ChrSetPos(0x00F7, -128130, 0, 138000, 270)
    ChrSetPos(0x00F8, -128130, 0, 138000, 270)
    ChrSetPos(0x00F9, -128130, 0, 138000, 270)

    If(
        (
            (Expr.PushValueByIndex, 0xE),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C89',
    )

    ChrSetPos(0x00FA, -128130, 0, 138000, 270)

    def _loc_C89(): pass

    label('loc_C89')

    OP_69(0x00F6, 0)
    OP_0D()
    OP_4B(0x000B, 255)
    Sleep(50)

    EventEnd(0x04)
    OP_28(0x0078, 0x01, 0x8000)

    Return()

    def _loc_CA3(): pass

    label('loc_CA3')

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
            TXT(0x00, '【是】\n'),
            TXT(0x01, '【否】\n'),
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

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D1F',
    )

    ChrTalk(
        0x0101,
        (
            '#0010480048V#1006F嗯，没问题了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(1, 0x0003)

    Return()

    def _loc_D1F(): pass

    label('loc_D1F')

    ChrTalk(
        0x0101,
        (
            '#0010480049V#1015F啊，抱歉哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480050V还得花点时间呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3630480051V唔，这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3630480052V没办法呢。\n',
            '那么，请稍后再来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(1000)
    ChrSetPos(0x000B, -126260, 0, 138000, 270)
    ChrSetPos(0x00F6, -128130, 0, 138000, 270)
    ChrSetPos(0x00F7, -128130, 0, 138000, 270)
    ChrSetPos(0x00F8, -128130, 0, 138000, 270)
    ChrSetPos(0x00F9, -128130, 0, 138000, 270)

    If(
        (
            (Expr.PushValueByIndex, 0xE),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E27',
    )

    ChrSetPos(0x0004, -128130, 0, 138000, 270)

    def _loc_E27(): pass

    label('loc_E27')

    OP_69(0x00F6, 0)
    OP_0D()
    OP_4B(0x000B, 255)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x0003 offset: 0xE3B
@scena.Code('func_03_E3B')
def func_03_E3B():
    ChrTalk(
        0x000B,
        (
            '#3630480053V那么这边请。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3630480054V详细情况\n',
            '由书记官来说明。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    TerminateThread(0x000B, 0x01)
    TerminateThread(0x000B, 0x02)
    ChrSetRGBAMask(0x000B, 255, 255, 255, 255, 0)
    CameraMove(-123540, 0, 180180, 0)
    OP_67(0, 5290, -10000, 0)
    CameraSetDistance(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    ChrSetPos(0x000B, -130449, 0, 179930, 90)
    ChrSetPos(0x0101, -131450, 0, 179930, 90)
    ChrSetPos(0x00F7, -132450, 0, 179930, 90)
    ChrSetPos(0x00F8, -133450, 0, 179930, 90)
    ChrSetPos(0x00F9, -134450, 0, 179930, 90)

    If(
        (
            (Expr.PushValueByIndex, 0xE),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_F51',
    )

    ChrSetPos(0x0004, -135450, 0, 179930, 90)

    def _loc_F51(): pass

    label('loc_F51')

    OP_4A(0x000D, 255)
    FadeIn(1000, 0)
    OP_0D()
    OP_62(0x000A, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(2000)

    OP_70(0x0002, 14)

    @scena.Lambda('lambda_0F88')
    def lambda_0F88():
        CameraMove(-126280, 0, 181030, 2000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0F88)

    ChrWalkTo(0x000B, -128280, 0, 179710, 2000, 0x00)
    ChrWalkTo(0x000B, -128419, 0, 180840, 2000, 0x00)
    ChrSetDirection(0x000B, 90, 400)
    WaitForThreadExit(0x000B, 0x0001)

    ChrTalk(
        0x000B,
        (
            '#3630480055V阁下，游击士们\n',
            '已经到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4A(0x000A, 255)
    ChrTurnDirection(0x000A, 0x000B, 400)
    ChrTurnDirection(0x000D, 0x000B, 400)

    ChrTalk(
        0x000A,
        (
            '#0670480056V#1101F喔喔，来了吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1037')
    def lambda_1037():
        ChrTurnDirection(0x000D, 0x0101, 400)
        Yield()

        Jump('lambda_1037')

    DispatchAsync2(0x000D, 0x0001, lambda_1037)

    CreateThread(0x0101, 0x00, 0x01, 0x0004)
    CreateThread(0x00F7, 0x00, 0x01, 0x0005)
    CreateThread(0x00F8, 0x00, 0x01, 0x0006)
    CreateThread(0x00F9, 0x00, 0x01, 0x0007)

    If(
        (
            (Expr.PushValueByIndex, 0xE),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1071',
    )

    CreateThread(0x0004, 0x00, 0x01, 0x0008)

    def _loc_1071(): pass

    label('loc_1071')

    @scena.Lambda('lambda_1077')
    def lambda_1077():
        CameraMove(-125210, 0, 179480, 2000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1077)

    ChrWalkTo(0x000A, -122680, 0, 179240, 1500, 0x00)
    ChrSetDirection(0x000A, 270, 400)

    If(
        (
            (Expr.PushValueByIndex, 0xE),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_10B8',
    )

    WaitForThreadExit(0x0004, 0x0000)

    Jump('loc_10BD')

    def _loc_10B8(): pass

    label('loc_10B8')

    WaitForThreadExit(0x00F9, 0x0000)

    def _loc_10BD(): pass

    label('loc_10BD')

    TerminateThread(0x000B, 0x01)
    CreateThread(0x000B, 0x00, 0x01, 0x0009)
    TerminateThread(0x000D, 0x01)

    ChrTalk(
        0x000A,
        (
            '#0670480057V#1100F啊，你们是……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1128',
    )

    ChrTalk(
        0x0105,
        (
            '#0060480058V#040F好久不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1150')

    def _loc_1128(): pass

    label('loc_1128')

    ChrTalk(
        0x0101,
        (
            '#0010480059V#1011F啊，好久不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1150(): pass

    label('loc_1150')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1185',
    )

    ChrTalk(
        0x0108,
        (
            '#0080480060V#070F唔，又见面了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1185(): pass

    label('loc_1185')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_11F3',
    )

    ChrTalk(
        0x0104,
        (
            '#0040480061V#030F呼，真高兴看到\n',
            '您一如既往地健康啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0670480062V#1100F呼……你也是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_11F3(): pass

    label('loc_11F3')

    ChrTalk(
        0x0101,
        (
            '#0010480063V#1000F那个，在王都时\n',
            '十分感谢您的协助。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480064V#1015F话说回来，您怎么会在柏斯？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_131B',
    )

    ChrTalk(
        0x000A,
        (
            '#0670480065V#1102F嗯，因为签署仪式圆满结束，\n',
            '日程总算空闲下来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670480066V于是就来落实\n',
            '早就预定好的视察了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670480067V#1100F遗憾的是由于超市事件的影响\n',
            '成果并不怎么显著。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1391')

    def _loc_131B(): pass

    label('loc_131B')

    ChrTalk(
        0x000A,
        (
            '#0670480065V#1102F嗯，因为签署仪式圆满结束，\n',
            '日程总算空闲下来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670480069V于是就来落实\n',
            '早就预定好的视察了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1391(): pass

    label('loc_1391')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_13CF',
    )

    ChrTalk(
        0x0103,
        (
            '#0030480070V#020F原来如此，您在视察啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1480')

    def _loc_13CF(): pass

    label('loc_13CF')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_140D',
    )

    ChrTalk(
        0x0106,
        (
            '#0050480071V#050F原来如此，是在视察啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1480')

    def _loc_140D(): pass

    label('loc_140D')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_144B',
    )

    ChrTalk(
        0x0108,
        (
            '#0080480072V#070F原来如此，您在视察啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1480')

    def _loc_144B(): pass

    label('loc_144B')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1480',
    )

    ChrTalk(
        0x0104,
        (
            '#0040480073V#030F呼，就是视察吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1480(): pass

    label('loc_1480')

    ChrTalk(
        0x000A,
        (
            '#0670480074V#1100F哼，不过这些事\n',
            '就先管不了那么多了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670480075V#1101F总、总而言之现在\n',
            '必须想方设法把勋章给找回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010480076V#1004F那，那\n',
            '什么勋章很重要吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0670480077V#1103F喂、书记官！\n',
            '还在磨蹭什么。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670480078V还不赶快拿那个东西\n',
            '给各位游击士看！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000D, 0x000A, 400)

    ChrTalk(
        0x000D,
        (
            '#3640480079V是，这就拿来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x000D, -123450, 0, 178620, 1000, 0x00)
    ChrTurnDirection(0x000D, 0x0101, 400)
    OP_62(0x000A, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    ChrWalkTo(0x000A, -122680, 0, 179240, 1500, 0x00)
    ChrSetDirection(0x000A, 90, 400)

    ChrTalk(
        0x0101,
        (
            '#0010480080V#1002F感、感觉大使\n',
            '好像相当焦躁……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3640480081V唔，这也难怪……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3640480082V这次的事件\n',
            '对阁下来说确实是一件大事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3640480083V不管怎么说那个勋章\n',
            '可是皇帝陛下所赐的荣誉之物。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3640480084V这个要是丢了，\n',
            '阁下可就颜面扫地了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3640480085V如果事情传到本国，\n',
            '阁下就会成为帝都的笑柄吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010480086V#1016F帝都的笑柄……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480087V会不会说得\n',
            '太夸张了点？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3640480088V不，身为帝国之人\n',
            '虽不便大肆宣扬——',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3640480089V但这种窘态\n',
            '简直就是社交界的好靶子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3640480090V一旦流言传开，\n',
            '绝非儿戏，到时必被\n',
            '城中千夫所指。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010480091V#1019F切，人们就爱议论些这个啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480092V#1007F呼……社交界\n',
            '其实是很恐怖的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_18F3',
    )

    ChrTalk(
        0x0107,
        (
            '#0070480093V#561F真、真的啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_18F3(): pass

    label('loc_18F3')

    ChrTalk(
        0x000D,
        (
            '#3640480094V这就是活在政界\n',
            '之人的宿命。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3640480095V请各位过来的原因\n',
            '能理解了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_19FF',
    )

    ChrTalk(
        0x0106,
        (
            '#0050480096V#053F原来如此。\n',
            '基本上了解情况了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050480097V#050F那，大使所说的\n',
            '『那个东西』是什么？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050480098V看起来像是有什么\n',
            '东西要给我们看似的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1BDD')

    def _loc_19FF(): pass

    label('loc_19FF')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1A9C',
    )

    ChrTalk(
        0x0103,
        (
            '#0030480099V#025F嗯，情况明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030480100V#027F那，大使所说的\n',
            '『那个东西』是什么？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030480101V好像有什么\n',
            '东西要给我们看似的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1BDD')

    def _loc_1A9C(): pass

    label('loc_1A9C')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1B3C',
    )

    ChrTalk(
        0x0108,
        (
            '#0080480102V#070F噢，情况了解了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080480103V对了，大使所说的\n',
            '『那个东西』是什么？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080480104V看起来好像有什么\n',
            '东西要给我们看似的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1BDD')

    def _loc_1B3C(): pass

    label('loc_1B3C')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1BDD',
    )

    ChrTalk(
        0x0104,
        (
            '#0040480105V#030F呼，情况了解啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040480106V对了，大使所说的\n',
            '『那个东西』到底是什么？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040480107V看起来好像有什么\n',
            '东西要给我们看似的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1BDD(): pass

    label('loc_1BDD')

    ChrTalk(
        0x000D,
        (
            '#3640480108V啊，其实……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3640480109V现场留下了疑似\n',
            '犯罪声明的卡片。',
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
            '#0010480110V#1004F卡、卡片吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3640480111V是，就是这样的东西──',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    OP_AD('ED6_DT24/C_VIS124._CH', 0x00BE, 0x0064, 0x000001F4)
    Sleep(1000)

    SetMessageWindowPos(-1, 300, -1, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0170480112V　　美丽的公主及其随从啊。　　\n',
            '　  制裁的钟声终于近了……\n',
            '    铁马的勋章也将落入吾手。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170480113V　　   若想将之夺还\n',
            '　　 就破解吾之谜题吧。　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170480114V　　第一把钥匙为以下咒文──\n',
            '　　 　ＲＩＣＵＬ\n',
            '　　 　面背的花查调',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170480115V　   一切之终即为始。 　\n',
            '　    汝，不可忘却。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_AE(0x000001F4)
    Sleep(1000)

    OP_62(0x0101, 0x00000000, 2000, 0x0E, 0x0F, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    If(
        (
            (Expr.Eval, "OP_29(0x006C, 0x00, 0x04)"),
            (Expr.Eval, "OP_29(0x00C4, 0x00, 0x04)"),
            Expr.Or,
            (Expr.Eval, "OP_29(0x0077, 0x00, 0x04)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_2098',
    )

    ChrTalk(
        0x0101,
        (
            '#0010480116V#1007F真是，每次都这么麻烦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480117V一直被他这样骚扰，\n',
            '连发牢骚的心情都没有了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1F0C',
    )

    ChrTalk(
        0x0108,
        (
            '#0080480118V#070F哈哈，这也算是一种觉悟吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080480119V总之，再确认一次\n',
            '卡片的要点吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2095')

    def _loc_1F0C(): pass

    label('loc_1F0C')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1F7E',
    )

    ChrTalk(
        0x0106,
        (
            '#0050480120V#552F这就是所谓举手投降了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050480121V#053F总之，再确认一下\n',
            '卡片的要点吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2095')

    def _loc_1F7E(): pass

    label('loc_1F7E')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1FEC',
    )

    ChrTalk(
        0x0103,
        (
            '#0030480122V#025F是说该举手投降了吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030480123V#020F总之，再确认一下\n',
            '卡片的要点吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2095')

    def _loc_1FEC(): pass

    label('loc_1FEC')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2095',
    )

    ChrTalk(
        0x0104,
        (
            '#0040480124V#030F持续的郁闷，\n',
            '打算对方已经坚持不住……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040480125V呼，简直就是游说的极致。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040480126V那，这些暂且不论，\n',
            '再确认一下卡片的要点吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2095(): pass

    label('loc_2095')

    Jump('loc_230D')

    def _loc_2098(): pass

    label('loc_2098')

    ChrTalk(
        0x0101,
        (
            '#0010480127V#1019F嗯、嗯…………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480128V这个怎么看\n',
            '都是张暗号卡片吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_211E',
    )

    ChrTalk(
        0x0105,
        (
            '#0060480129V#043F啊，看来是呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_211E(): pass

    label('loc_211E')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2164',
    )

    ChrTalk(
        0x0104,
        (
            '#0040480130V#035F呼，劲敌的挑战……\n',
            '就好好接招吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2164(): pass

    label('loc_2164')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_21EC',
    )

    ChrTalk(
        0x0108,
        (
            '#0080480131V#073F怪盗绅士……\n',
            '『噬身之蛇』的执行者吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080460318V#072F传闻倒是听过，\n',
            '好像是个相当特立独行的家伙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_21EC(): pass

    label('loc_21EC')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2235',
    )

    ChrTalk(
        0x0106,
        (
            '#0050480133V#050F唔，总之先确认一下\n',
            '卡片的要点吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_230D')

    def _loc_2235(): pass

    label('loc_2235')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_227E',
    )

    ChrTalk(
        0x0103,
        (
            '#0030480134V#022F唔，总之先确认一下\n',
            '卡片的要点吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_230D')

    def _loc_227E(): pass

    label('loc_227E')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_22C7',
    )

    ChrTalk(
        0x0107,
        (
            '#0070480135V#560F总、总之再确认一次\n',
            '卡片的要点吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_230D')

    def _loc_22C7(): pass

    label('loc_22C7')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_230D',
    )

    ChrTalk(
        0x0104,
        (
            '#0040480136V#030F总之应该先确认一下\n',
            '卡片的要点吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_230D(): pass

    label('loc_230D')

    ExecExpressionWithValue(
        0x001E,
        0x01,
        (
            (Expr.GetChrWork, 0x101, 0x1),
            (Expr.GetChrWork, 0xF9, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001E,
        0x02,
        (
            (Expr.GetChrWork, 0x101, 0x2),
            (Expr.GetChrWork, 0xF9, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001E,
        0x03,
        (
            (Expr.GetChrWork, 0x101, 0x3),
            (Expr.GetChrWork, 0xF9, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_2352')
    def lambda_2352():
        OP_69(0x001E, 1000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_2352)

    ChrSetDirection(0x0101, 270, 400)

    @scena.Lambda('lambda_2367')
    def lambda_2367():
        ChrTurnDirection(0x00F8, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_2367)

    Sleep(100)

    @scena.Lambda('lambda_237A')
    def lambda_237A():
        ChrTurnDirection(0x00F7, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_237A)

    Sleep(150)

    ChrTurnDirection(0x00F9, 0x0101, 400)

    If(
        (
            (Expr.PushValueByIndex, 0xE),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_23A1',
    )

    ChrTurnDirection(0x0004, 0x0101, 400)

    def _loc_23A1(): pass

    label('loc_23A1')

    WaitForThreadExit(0x00F7, 0x0001)
    WaitForThreadExit(0x00F8, 0x0001)
    WaitForThreadExit(0x000B, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010480137V#1002F嗯，关键在于\n',
            '这个『ＲＩＣＵＬ』吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480138V出发点应该是\n',
            '找出这个的意义吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_24A6',
    )

    ChrTalk(
        0x0106,
        (
            '#0050480139V#050F这么说来，这字母后面的文章\n',
            '应该才是最重要的部分啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050480140V那些部分很可能\n',
            '就是对这些字母的暗示。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_264D')

    def _loc_24A6(): pass

    label('loc_24A6')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2534',
    )

    ChrTalk(
        0x0103,
        (
            '#0030480141V#022F这么说来，这字母后面的文章\n',
            '应该才是最重要的部分啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030480142V那些部分很可能\n',
            '就是对这些字母的暗示。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_264D')

    def _loc_2534(): pass

    label('loc_2534')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_25C2',
    )

    ChrTalk(
        0x0108,
        (
            '#0080480143V#070F这么说来，这字母后面的文章\n',
            '应该才是最重要的部分啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080480144V那些部分很可能\n',
            '就是对这些字母的暗示。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_264D')

    def _loc_25C2(): pass

    label('loc_25C2')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_264D',
    )

    ChrTalk(
        0x0104,
        (
            '#0040480145V#030F这么说来，这字母后面的文章\n',
            '应该才是最重要的部分啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040480146V那些部分很可能\n',
            '就是对这些字母的暗示。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_264D(): pass

    label('loc_264D')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_26AB',
    )

    ChrTalk(
        0x0105,
        (
            '#0060480147V#042F『一切之终即为始』对吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060480148V记得是这样的话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_27D3')

    def _loc_26AB(): pass

    label('loc_26AB')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_271A',
    )

    ChrTalk(
        0x0107,
        (
            '#0070480149V#062F『一切之终即为始』\n',
            '……是说这个部分吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070480150V嗯，确实像是这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_27D3')

    def _loc_271A(): pass

    label('loc_271A')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2778',
    )

    ChrTalk(
        0x0104,
        (
            '#0040480151V#030F『一切之终即为始』吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040480152V记得是这样的话吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_27D3')

    def _loc_2778(): pass

    label('loc_2778')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_27D3',
    )

    ChrTalk(
        0x0103,
        (
            '#0030480153V#027F『一切之终即为始』吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030480154V记得是这样的话呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_27D3(): pass

    label('loc_27D3')

    ChrTalk(
        0x0101,
        (
            '#0010480155V#1002F作为开始调查的\n',
            '线索已经足够充分了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480156V首先以这个为线索，\n',
            '在市内调查看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3640480157V找到调查的起点了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_286D')
    def lambda_286D():
        CameraMove(-125210, 0, 179480, 1000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_286D)

    @scena.Lambda('lambda_2885')
    def lambda_2885():
        ChrSetDirection(0x00F8, 90, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_2885)

    Sleep(100)

    @scena.Lambda('lambda_2898')
    def lambda_2898():
        ChrSetDirection(0x00F7, 90, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_2898)

    Sleep(150)

    ChrSetDirection(0x0101, 90, 400)

    @scena.Lambda('lambda_28B2')
    def lambda_28B2():
        ChrSetDirection(0x00F9, 90, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_28B2)

    If(
        (
            (Expr.PushValueByIndex, 0xE),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_28CD',
    )

    ChrSetDirection(0x0004, 90, 400)

    def _loc_28CD(): pass

    label('loc_28CD')

    WaitForThreadExit(0x000B, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010480158V#1006F嗯，算是吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480159V那么，要是发现了什么\n',
            '就会再过来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3640480160V喔，期待你们的表现。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0101, 400)

    ChrTalk(
        0x000A,
        (
            '#0670480161V#1100F已经开始调查了吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670480162V那么，就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x000A, 400)

    ChrTalk(
        0x0101,
        (
            '#0010480163V#1006F嗯，交给我们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()
    OP_28(0x0078, 0x04, 0x04)
    OP_28(0x0078, 0x04, 0x08)
    OP_28(0x0078, 0x01, 0x0001)
    OP_28(0x0078, 0x01, 0x0002)
    FadeOut(1500, 0, -1)
    OP_0D()
    ChrSetPos(0x0000, -125660, 0, 179040, 90)
    ChrSetPos(0x0001, -125660, 0, 179040, 90)
    ChrSetPos(0x0002, -125660, 0, 179040, 90)
    ChrSetPos(0x0003, -125660, 0, 179040, 90)

    If(
        (
            (Expr.PushValueByIndex, 0xE),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2A52',
    )

    ChrSetPos(0x0004, -125660, 0, 179040, 90)

    def _loc_2A52(): pass

    label('loc_2A52')

    OP_69(0x0000, 0)
    OP_67(0, 6150, -10000, 0)
    CameraSetDistance(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_30(0x00)
    ChrSetDirection(0x0101, 90, 0)
    ChrSetDirection(0x00F7, 90, 0)
    ChrSetDirection(0x00F8, 90, 0)
    ChrSetDirection(0x00F9, 90, 0)

    If(
        (
            (Expr.PushValueByIndex, 0xE),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2AB6',
    )

    ChrSetDirection(0x00FA, 90, 0)

    def _loc_2AB6(): pass

    label('loc_2AB6')

    OP_4A(0x0000, 255)
    OP_4A(0x0001, 255)
    OP_4A(0x0002, 255)
    OP_4A(0x0003, 255)

    If(
        (
            (Expr.PushValueByIndex, 0xE),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2AD6',
    )

    OP_4A(0x0004, 255)

    def _loc_2AD6(): pass

    label('loc_2AD6')

    ChrSetPos(0x000B, -127460, 0, 181340, 180)
    ChrSetPos(0x000D, -123490, 0, 178400, 45)
    ChrSetPos(0x000A, -122680, 0, 179240, 270)
    OP_4B(0x000A, 255)
    OP_4B(0x000D, 255)
    ChrSetFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    FadeIn(1500, 0)
    EventEnd(0x00)

    Return()

# id: 0x0004 offset: 0x2B27
@scena.Code('func_04_2B27')
def func_04_2B27():
    ChrWalkTo(0x0101, -127460, 0, 179930, 2000, 0x00)
    ChrWalkTo(0x0101, -124730, 0, 178760, 2000, 0x00)
    ChrSetDirection(0x0101, 90, 400)

    Return()

# id: 0x0005 offset: 0x2B57
@scena.Code('func_05_2B57')
def func_05_2B57():
    Sleep(400)

    ChrWalkTo(0x00F7, -127460, 0, 179930, 2000, 0x00)
    ChrWalkTo(0x00F7, -125940, 0, 179640, 2000, 0x00)
    ChrSetDirection(0x00F7, 90, 400)

    Return()

# id: 0x0006 offset: 0x2B8C
@scena.Code('func_06_2B8C')
def func_06_2B8C():
    Sleep(800)

    ChrWalkTo(0x00F8, -127460, 0, 179930, 2000, 0x00)
    ChrWalkTo(0x00F8, -125330, 0, 177850, 2000, 0x00)
    ChrSetDirection(0x00F8, 90, 400)

    Return()

# id: 0x0007 offset: 0x2BC1
@scena.Code('func_07_2BC1')
def func_07_2BC1():
    Sleep(1200)

    ChrWalkTo(0x00F9, -128270, 0, 179930, 2000, 0x00)
    ChrWalkTo(0x00F9, -127460, 0, 179930, 2000, 0x00)
    ChrWalkTo(0x00F9, -126560, 0, 178910, 2000, 0x00)
    ChrSetDirection(0x00F9, 90, 400)

    Return()

# id: 0x0008 offset: 0x2C0A
@scena.Code('func_08_2C0A')
def func_08_2C0A():
    Sleep(1600)

    ChrWalkTo(0x0004, -128270, 0, 179930, 2000, 0x00)
    ChrWalkTo(0x0004, -127440, 0, 178220, 2000, 0x00)
    ChrSetDirection(0x0004, 90, 400)

    Return()

# id: 0x0009 offset: 0x2C3F
@scena.Code('func_09_2C3F')
def func_09_2C3F():
    ChrSetDirection(0x00FE, 180, 400)
    ChrWalkTo(0x000B, -128280, 0, 179710, 2000, 0x00)
    ChrSetDirection(0x00FE, 270, 400)
    OP_72(0x0002, 0x0800)
    OP_70(0x0002, 0)
    PlaySE(7, 0x00, 0x64)
    OP_73(0x0002)
    OP_71(0x0002, 0x0800)
    Sleep(500)

    ChrSetDirection(0x00FE, 90, 400)
    ChrWalkTo(0x000B, -128280, 0, 179710, 2000, 0x00)
    ChrWalkTo(0x000B, -128419, 0, 180840, 2000, 0x00)
    ChrSetDirection(0x000B, 90, 400)

    Return()

# id: 0x000A offset: 0x2CB6
@scena.Code('func_0A_2CB6')
def func_0A_2CB6():
    EventBegin(0x00)
    ChrSetPos(0x0101, -124730, 0, 178760, 90)
    ChrSetPos(0x00F7, -125890, 0, 178760, 90)
    ChrSetPos(0x00F8, -125330, 0, 177850, 90)
    ChrSetPos(0x00F9, -126540, 0, 178170, 90)

    If(
        (
            (Expr.PushValueByIndex, 0xE),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2D19',
    )

    ChrSetPos(0x0004, -127440, 0, 178220, 90)

    def _loc_2D19(): pass

    label('loc_2D19')

    ChrSetPos(0x000A, -123450, 0, 178760, 270)
    ChrSetPos(0x000D, -122420, 0, 179380, 270)
    ChrSetPos(0x000C, -128419, 0, 180840, 90)
    CameraMove(-125530, 0, 179560, 0)
    OP_67(0, 5290, -10000, 0)
    CameraSetDistance(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_4A(0x000A, 255)
    OP_4A(0x000D, 255)
    OP_4A(0x000C, 255)
    OP_0D()

    ChrTalk(
        0x000A,
        (
            '#0670480458V#1101F这、这是真的吗！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670480459V呵，真的\n',
            '找到勋章了吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010480460V#1006F#1P嗯，真的真的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480461V唔，事实胜于雄辩哦。\n',
            '勋章还给您了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#16I宝剑天马大勋章',
            (TxtCtl.SetColor, 0x0),
            '交出了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(
        0x000A,
        (
            '#0670480462V#1101F喔、喔喔！\n',
            '这确实是我的……！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670480463V……幸、幸好没事……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670480464V#1102F（沉～～默………………）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_CB(0xF6)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2F39',
    )

    OP_62(0x00F6, 0x00000000, 2300, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)

    Jump('loc_2F77')

    def _loc_2F39(): pass

    label('loc_2F39')

    If(
        (
            (Expr.Eval, "OP_CB(0xF6)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2F60',
    )

    OP_62(0x00F6, 0x00000000, 1700, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)

    Jump('loc_2F77')

    def _loc_2F60(): pass

    label('loc_2F60')

    OP_62(0x00F6, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)

    def _loc_2F77(): pass

    label('loc_2F77')

    Sleep(120)

    If(
        (
            (Expr.Eval, "OP_CB(0xF7)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2FA3',
    )

    OP_62(0x00F7, 0x00000000, 2300, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)

    Jump('loc_2FE1')

    def _loc_2FA3(): pass

    label('loc_2FA3')

    If(
        (
            (Expr.Eval, "OP_CB(0xF7)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2FCA',
    )

    OP_62(0x00F7, 0x00000000, 1700, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)

    Jump('loc_2FE1')

    def _loc_2FCA(): pass

    label('loc_2FCA')

    OP_62(0x00F7, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)

    def _loc_2FE1(): pass

    label('loc_2FE1')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3008',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)

    Jump('loc_3046')

    def _loc_3008(): pass

    label('loc_3008')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_302F',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)

    Jump('loc_3046')

    def _loc_302F(): pass

    label('loc_302F')

    OP_62(0x00F9, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)

    def _loc_3046(): pass

    label('loc_3046')

    Sleep(120)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3072',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)

    Jump('loc_30B0')

    def _loc_3072(): pass

    label('loc_3072')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3099',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)

    Jump('loc_30B0')

    def _loc_3099(): pass

    label('loc_3099')

    OP_62(0x00F8, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)

    def _loc_30B0(): pass

    label('loc_30B0')

    If(
        (
            (Expr.PushValueByIndex, 0xE),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_30F9',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xE),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_30E2',
    )

    OP_62(0x0004, 0x00000000, 2300, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)

    Jump('loc_30F9')

    def _loc_30E2(): pass

    label('loc_30E2')

    OP_62(0x0004, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)

    def _loc_30F9(): pass

    label('loc_30F9')

    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010480465V#1016F#1P打、打断您沉浸在欢乐中\n',
            '非常抱歉……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480466V不过您要找的东西，\n',
            '确实就是这个什么什么勋章吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000A,
        (
            '#0670480467V#1101F怒……！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670480468V不是什么什么勋章，\n',
            '是宝剑天马大勋章!!!',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670480469V居然那样称呼\n',
            '荣誉的赏赐，真是没礼貌。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010480470V#1019F#1P#1S那、那么长\n',
            '谁记得住啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0670480471V#1100F你刚才说什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010480472V#1016F#1P没、没有，没什么。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480473V不管怎样，是那个勋章\n',
            '没错吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0670480474V#1100F嗯，没有错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670480475V#1102F呼，总算\n',
            '逃过一劫了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670480476V之后只要抓住\n',
            '犯事的狂徒，\n',
            '这事就算解决了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670480477V#1100F那么，有\n',
            '犯人的眉目了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010480478V#1015F#1P其实犯人我们早就知道是谁……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480479V#1007F遗、遗憾的是\n',
            '其行踪却完全不明。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0670480480V#1101F你说什么？\n',
            '抓不到他吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_34BF',
    )

    ChrTalk(
        0x0106,
        (
            '#0050480481V#050F#1P马上抓到是不可能的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050480482V疑似犯人\n',
            '是国际犯罪组织的一员。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050480483V『怪盗Ｂ』这名字\n',
            '您有在哪里听说过吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_368F')

    def _loc_34BF(): pass

    label('loc_34BF')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_355B',
    )

    ChrTalk(
        0x0103,
        (
            '#0030480484V#026F#1P马上抓到是不可能的呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030480485V疑似犯人\n',
            '是国际犯罪组织的一员。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030480486V#027F『怪盗Ｂ』这名字\n',
            '您知道吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_368F')

    def _loc_355B(): pass

    label('loc_355B')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_35F5',
    )

    ChrTalk(
        0x0108,
        (
            '#0080480487V#074F#1P马上抓到不可能吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080480488V疑似犯人\n',
            '是国际犯罪组织的一员。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080480489V#072F『怪盗Ｂ』这名字\n',
            '您不知道吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_368F')

    def _loc_35F5(): pass

    label('loc_35F5')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_368F',
    )

    ChrTalk(
        0x0104,
        (
            '#0040480490V#030F#1P马上抓到是不可能的呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040480491V疑似犯人\n',
            '是国际犯罪组织的一员。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040480492V『怪盗Ｂ』这名字\n',
            '您没有听说过吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_368F(): pass

    label('loc_368F')

    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000A,
        (
            '#0670480493V#1101F你说『怪盗Ｂ』！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670480494V那家伙在利贝尔\n',
            '出现了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010480495V#1011F#1P啊，您果然知道？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0670480496V#1100F呼，嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670480497V他曾经一时间闹得帝国诸城\n',
            '鸡犬不宁。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670480498V#1102F他是连我们帝国军\n',
            '都抓不住的男人……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670480499V看来这次只是寻回勋章\n',
            '就该谢天谢地了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010480500V#1003F#1P啊啊，真遗憾……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0670480501V#1102F………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670480502V#1100F……巴克雷书记官。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3640480503V是！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0670480504V#1100F那个准备好了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3640480505V是，在这边。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x000D, 0x01, 0x01, 0x000B)
    WaitForThreadExit(0x000D, 0x0001)
    ChrSetDirection(0x000A, 90, 400)

    ChrTalk(
        0x000A,
        (
            '#0670480506V#1100F呼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    SetScenaFlags(ScenaFlag(0x0002, 6, 0x16))
    CreateThread(0x000D, 0x01, 0x01, 0x000B)
    Sleep(400)

    @scena.Lambda('lambda_390C')
    def lambda_390C():
        ChrSetDirection(0x000A, 270, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_390C)

    WaitForThreadExit(0x000D, 0x0001)

    ChrTalk(
        0x000A,
        (
            '#0670480507V#1100F无法抓到他\n',
            '实在遗憾……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670480508V但对方既是那个『怪盗Ｂ』\n',
            '就不能再有抱怨了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670480509V诸位出色地找到了勋章，\n',
            '确保了我帝国的威信。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670480510V#1102F鉴于如此劳苦功高，\n',
            '本埃雷波尼亚帝国大使馆──',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670480511V——特此授予铁骑功勋章。',
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
            (TxtCtl.Item, ItemTable['铁骑功勋章']),
            (TxtCtl.SetColor, 0x0),
            '被授予。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(ItemTable['铁骑功勋章'], 1)
    OP_62(0x000D, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x000C, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    PlaySE(191, 0x00, 0x64)

    ChrTalk(
        0x000D,
        (
            '#3640480512V诸位，恭喜！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#3630480513V恭喜！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_63(0x000D)
    OP_63(0x000C)
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(120)

    If(
        (
            (Expr.Eval, "OP_CB(0xF7)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3B0D',
    )

    OP_62(0x00F7, 0x00000000, 2300, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)

    Jump('loc_3B4B')

    def _loc_3B0D(): pass

    label('loc_3B0D')

    If(
        (
            (Expr.Eval, "OP_CB(0xF7)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3B34',
    )

    OP_62(0x00F7, 0x00000000, 1700, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)

    Jump('loc_3B4B')

    def _loc_3B34(): pass

    label('loc_3B34')

    OP_62(0x00F7, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)

    def _loc_3B4B(): pass

    label('loc_3B4B')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3B72',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)

    Jump('loc_3BB0')

    def _loc_3B72(): pass

    label('loc_3B72')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3B99',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)

    Jump('loc_3BB0')

    def _loc_3B99(): pass

    label('loc_3B99')

    OP_62(0x00F8, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)

    def _loc_3BB0(): pass

    label('loc_3BB0')

    Sleep(120)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3BDC',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)

    Jump('loc_3C1A')

    def _loc_3BDC(): pass

    label('loc_3BDC')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3C03',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)

    Jump('loc_3C1A')

    def _loc_3C03(): pass

    label('loc_3C03')

    OP_62(0x00F9, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)

    def _loc_3C1A(): pass

    label('loc_3C1A')

    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010480514V#1015F#1P啊，啊啊…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3C8A',
    )

    ChrTalk(
        0x0105,
        (
            '#0060480515V#045F突、突然就被\n',
            '授予了勋章呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3C8A(): pass

    label('loc_3C8A')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3CC5',
    )

    ChrTalk(
        0x0107,
        (
            '#0070480516V#562F好、好像有点难为情……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3CC5(): pass

    label('loc_3CC5')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3CFE',
    )

    ChrTalk(
        0x0106,
        (
            '#0050480517V#552F什么啊，这么突然……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3CFE(): pass

    label('loc_3CFE')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3D4C',
    )

    ChrTalk(
        0x0103,
        (
            '#0030480518V#025F还真是夸张呢……\n',
            '这就是所谓的帝国国风吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3D4C(): pass

    label('loc_3D4C')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3D89',
    )

    ChrTalk(
        0x0108,
        (
            '#0080480519V#071F哈哈，这就是帝国特色啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3D89(): pass

    label('loc_3D89')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3DD7',
    )

    ChrTalk(
        0x0104,
        (
            '#0040480520V#031F呼，虽然习惯了，\n',
            '但这次也感到有些意外啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3DD7(): pass

    label('loc_3DD7')

    ChrTalk(
        0x000A,
        (
            '#0670480521V#1102F突然被授予此等荣誉，\n',
            '你们迷惑的心情我可以理解。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670480522V年轻时的我，\n',
            '首次被授予勋章时也是这样……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670480523V#1100F然而，没什么好退缩的。\n',
            '这次的工作完全值得称赞。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670480524V#1100F不要被受勋者之名而拖累，\n',
            '期待你们今后的表现。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010480525V#1016F#1P啊，嗯……谢谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(23, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【帝国大使的委托】',
            (TxtCtl.SetColor, 0x0),
            '完成了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    OP_28(0x0078, 0x01, 0x0100)
    OP_28(0x0078, 0x04, 0x10)
    OP_4B(0x000A, 255)
    OP_4B(0x000D, 255)
    OP_4B(0x000C, 255)
    EventEnd(0x00)

    Return()

# id: 0x000B offset: 0x3F75
@scena.Code('func_0B_3F75')
def func_0B_3F75():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 6, 0x16)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3FA2',
    )

    ChrSetDirection(0x00FE, 180, 400)
    ChrWalkTo(0x00FE, -122580, 0, 178720, 1000, 0x00)
    ChrSetDirection(0x00FE, 270, 400)

    Jump('loc_3FC4')

    def _loc_3FA2(): pass

    label('loc_3FA2')

    ChrSetDirection(0x00FE, 0, 400)
    ChrWalkTo(0x00FE, -122420, 0, 179380, 1000, 0x00)
    ChrSetDirection(0x00FE, 270, 400)

    def _loc_3FC4(): pass

    label('loc_3FC4')

    Return()

# id: 0x000C offset: 0x3FC5
@scena.Code('func_0C_3FC5')
def func_0C_3FC5():
    If(
        (
            (Expr.PushValueByIndex, 0x13),
            (Expr.PushLong, 0x381),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3FD2',
    )

    Return()

    def _loc_3FD2(): pass

    label('loc_3FD2')

    If(
        (
            (Expr.Eval, "OP_29(0x0079, 0x00, 0x10)"),
            (Expr.Eval, "OP_29(0x0079, 0x00, 0x40)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_3FE4',
    )

    Return()

    def _loc_3FE4(): pass

    label('loc_3FE4')

    MapSetFlags(0x00000080)
    OP_C0(0x01, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)
    Sleep(30)

    If(
        (
            (Expr.Eval, "OP_CD(0x0008)"),
            Expr.Return,
        ),
        'loc_401F',
    )

    Call(1, 0x000D)

    Jump('loc_40C4')

    def _loc_401F(): pass

    label('loc_401F')

    If(
        (
            (Expr.Eval, "OP_CD(0x03E8)"),
            Expr.Return,
        ),
        'loc_402E',
    )

    Call(1, 0x000D)

    Jump('loc_40C4')

    def _loc_402E(): pass

    label('loc_402E')

    If(
        (
            (Expr.Eval, "OP_CD(0x00FF)"),
            Expr.Return,
        ),
        'loc_4086',
    )

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '试着出示了照片，\n',
            '但似乎没有见过的印象。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    Jump('loc_40C4')

    def _loc_4086(): pass

    label('loc_4086')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '附近没有人可以确认照片。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    def _loc_40C4(): pass

    label('loc_40C4')

    OP_0D()
    MapClearFlags(0x00000080)

    Return()

# id: 0x000D offset: 0x40CB
@scena.Code('func_0D_40CB')
def func_0D_40CB():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_4136',
    )

    ChrTalk(
        0x0008,
        (
            '#3820490603V照片上的脸…\n',
            '很遗憾，我没有印象。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3820490604V帮不上忙，\n',
            '实在不好意思。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_41EE')

    def _loc_4136(): pass

    label('loc_4136')

    ChrTalk(
        0x0008,
        (
            '#3820490599V是在找\n',
            '照片上的人吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3820490600V这可伤脑筋了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3820490601V别说是客人的脸了，\n',
            '还是１０年前的身影……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3820490602V实在抱歉，\n',
            '还是别强人所难了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_41EE(): pass

    label('loc_41EE')

    TalkEnd(0x0008)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
