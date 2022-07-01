import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T2330_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2330_1 ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

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
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x2550
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
    ]

# id: 0x10002 offset: 0xA8
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10003 offset: 0xA8
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0xA8
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0xA8
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0xA8
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_EC',
    )

    TalkBegin(0x000B)

    ChrTalk(
        0x000B,
        (
            '诸位，这次辛苦你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '下次工作时再见吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000B)

    Jump('loc_4E5')

    def _loc_EC(): pass

    label('loc_EC')

    If(
        (
            (Expr.Eval, "OP_29(0x0065, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_417',
    )

    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_189',
    )

    OP_A2(0x0005)

    ChrTalk(
        0x000B,
        (
            '接下来的贸易谈判是在柏斯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '离定期船开船\n',
            '还有足够的时间呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '不过在卢安\n',
            '打发时间很容易。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '提前出发可能\n',
            '也不错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_411')

    def _loc_189(): pass

    label('loc_189')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_269',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_1FE',
    )

    ChrTalk(
        0x000B,
        (
            '很希望将来能有机会品尝一下\n',
            '一流厨师烹调的本地珍馐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '我们奥维德商会\n',
            '也要为此更加努力才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_266')

    def _loc_1FE(): pass

    label('loc_1FE')

    OP_A2(0x0005)

    ChrTalk(
        0x000B,
        (
            '果然本地的土产\n',
            '有重新审视的价值。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '这种珍贵的食材\n',
            '要是能够在高级餐馆\n',
            '也简单地品尝到就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_266(): pass

    label('loc_266')

    Jump('loc_411')

    def _loc_269(): pass

    label('loc_269')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_360',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_2CF',
    )

    ChrTalk(
        0x000B,
        (
            '不过我一打算自己去探索\n',
            '就会被我侄女阿梅莉雅挽留。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '所以我就拜托了协会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_35D')

    def _loc_2CF(): pass

    label('loc_2CF')

    OP_A2(0x0005)

    ChrTalk(
        0x000B,
        (
            '本来这次也想\n',
            '自己去探索的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '不过被我侄女阿梅莉雅阻止了。\n',
            '所以我就拜托了协会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '平常总是让那孩子担心，\n',
            '偶尔也要听听她的话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_35D(): pass

    label('loc_35D')

    Jump('loc_411')

    def _loc_360(): pass

    label('loc_360')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_3B4',
    )

    ChrTalk(
        0x000B,
        (
            '海味、河味……\n',
            '连山珍都能享受到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '呵呵，不愧是\n',
            '孕育了我的土地。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_411')

    def _loc_3B4(): pass

    label('loc_3B4')

    OP_A2(0x0005)

    ChrTalk(
        0x000B,
        (
            '嗯～卢安果然是一片\n',
            '富于变化的土地啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '看着食材的清单，\n',
            '再次让我认识到了这一点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_411(): pass

    label('loc_411')

    TalkEnd(0x000B)

    Jump('loc_4E5')

    def _loc_417(): pass

    label('loc_417')

    If(
        (
            (Expr.Eval, "OP_29(0x0065, 0x00, 0x08)"),
            Expr.Return,
        ),
        'loc_428',
    )

    Call(1, 0x0004)

    Jump('loc_4E5')

    def _loc_428(): pass

    label('loc_428')

    If(
        (
            (Expr.Eval, "OP_29(0x0065, 0x00, 0x02)"),
            Expr.Return,
        ),
        'loc_439',
    )

    Call(1, 0x0002)

    Jump('loc_4E5')

    def _loc_439(): pass

    label('loc_439')

    SetChrFlags(0x000B, 0x0010)
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_47E',
    )

    ChrTalk(
        0x000B,
        (
            '唔～为了接下来的贸易谈判\n',
            '也要快点完成清单……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4DD')

    def _loc_47E(): pass

    label('loc_47E')

    OP_A2(0x0005)

    ChrTalk(
        0x000B,
        (
            '唔～不管怎么看都像是\n',
            '还有遗漏啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '为了准备接下来的贸易谈判\n',
            '也要快点完成清单……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4DD(): pass

    label('loc_4DD')

    TalkEnd(0x000B)
    ClearChrFlags(0x000B, 0x0010)

    def _loc_4E5(): pass

    label('loc_4E5')

    Return()

# id: 0x0001 offset: 0x4E6
@scena.Code('Init')
def Init():
    SetChrPos(0x0101, 650, 0, 880, 0)
    SetChrPos(0x00F7, 1540, 0, 670, 0)

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_53B',
    )

    SetChrPos(0x0104, 650, 0, -380, 0)
    SetChrPos(0x0105, 1490, 0, -570, 0)

    Jump('loc_58D')

    def _loc_53B(): pass

    label('loc_53B')

    If(
        (
            (Expr.Eval, "OP_42(0x26)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_56E',
    )

    SetChrPos(0x0104, 650, 0, -380, 0)
    SetChrPos(0x0127, 1490, 0, -570, 0)

    Jump('loc_58D')

    def _loc_56E(): pass

    label('loc_56E')

    If(
        (
            (Expr.Eval, "OP_42(0x08)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_58D',
    )

    SetChrPos(0x0109, 1095, 0, -475, 0)

    def _loc_58D(): pass

    label('loc_58D')

    OP_6D(90, 0, 1990, 0)

    Return()

# id: 0x0002 offset: 0x59F
@scena.Code('ReInit')
def ReInit():
    OP_4A(0x000B, 0)
    EventBegin(0x00)
    Fade(1000)
    Call(1, 0x0001)
    OP_0D()

    If(
        (
            (Expr.Eval, "OP_29(0x0065, 0x01, 0x8000)"),
            Expr.Return,
        ),
        'loc_60E',
    )

    ChrTurnDirection(0x000B, 0x0101, 400)
    Sleep(500)

    ChrTalk(
        0x000B,
        (
            '#1070430020V#2P哟，是你们啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1070430021V怎么样？有时间了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9CA')

    def _loc_60E(): pass

    label('loc_60E')

    ChrTalk(
        0x0101,
        (
            '#0010430001V#1011F#1P你好，能打搅你一下吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000B, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTurnDirection(0x000B, 0x0101, 400)
    Sleep(500)

    ChrTalk(
        0x000B,
        (
            '#1070430002V#2P嗯……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x0005, 0x00, 0x10)"),
            (Expr.Eval, "OP_29(0x001F, 0x00, 0x10)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_696',
    )

    OP_A2(0x0007)

    Jump('loc_699')

    def _loc_696(): pass

    label('loc_696')

    OP_A3(0x0007)

    def _loc_699(): pass

    label('loc_699')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_716',
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
            TXT(0x00, '◇完成过上一部的关联任务的情况下\n'),
            TXT(0x01, '◇没有完成的情况下\n'),
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

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_713',
    )

    OP_A2(0x0007)

    Jump('loc_716')

    def _loc_713(): pass

    label('loc_713')

    OP_A3(0x0007)

    def _loc_716(): pass

    label('loc_716')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_900',
    )

    ChrTalk(
        0x000B,
        (
            '#1070430003V#2P哦，原来是你啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1070430004V#2P还记得我吗？\n',
            '是很早以前拜托过你们工作的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00F7, 0x0101, 400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_7C3',
    )

    ChrTalk(
        0x0106,
        (
            '#0050430005V#052F#4P什么啊，原来你们认识？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7EB')

    def _loc_7C3(): pass

    label('loc_7C3')

    ChrTalk(
        0x0103,
        (
            '#0030430006V#023F#4P咦，你们认识？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7EB(): pass

    label('loc_7EB')

    ChrTurnDirection(0x0101, 0x00F7, 400)

    ChrTalk(
        0x0101,
        (
            '#0010430007V#1016F#1P嗯，算是认识吧。\n',
            '这个人是位食材商人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x000B, 400)

    ChrTalk(
        0x0101,
        (
            '#0010430008V#1000F#1P真是好久不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1070430009V#2P嗯，最后一次见面应该\n',
            '是在诞辰庆典之前吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1070430010V#2P没问题的话\n',
            '我立即来做工作的说明……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1070430011V#2P现在有时间吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9CA')

    def _loc_900(): pass

    label('loc_900')

    ChrTalk(
        0x000B,
        (
            '#1070430012V#2P哦，是游击士啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1070430013V#2P看来告示板过来的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010430014V#1000F#1P嗯，算是吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1070430015V#2P那么\n',
            '我立即来做工作的说明……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1070430011V#2P现在有时间吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9CA(): pass

    label('loc_9CA')

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
        100,
        0,
        (
            TXT(0x00, '【听工作的说明】\n'),
            TXT(0x01, '【放弃】\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x00FF)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_AB3',
    )

    OP_28(0x0065, 0x01, 0x8000)

    ChrTalk(
        0x0101,
        (
            '#0010430017V#1007F#1P不，对不起。\n',
            '现在有点不方便。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1070430018V#2P哦，这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1070430019V那么你们下次再来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1150')

    def _loc_AB3(): pass

    label('loc_AB3')

    If(
        (
            (Expr.Eval, "OP_29(0x0005, 0x00, 0x10)"),
            (Expr.Eval, "OP_29(0x001F, 0x00, 0x10)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_AEA',
    )

    ChrTalk(
        0x0101,
        (
            '#0010430022V#1006F#1P没问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B0D')

    def _loc_AEA(): pass

    label('loc_AEA')

    ChrTalk(
        0x0101,
        (
            '#0010430022V#1006F#1P没问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B0D(): pass

    label('loc_B0D')

    ChrTurnDirection(0x00F7, 0x000B, 400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_B4E',
    )

    ChrTalk(
        0x0106,
        (
            '#0050430024V#050F#4P那么，工作内容是什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B7E')

    def _loc_B4E(): pass

    label('loc_B4E')

    ChrTalk(
        0x0103,
        (
            '#0030430025V#020F#4P那么，委托内容是什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B7E(): pass

    label('loc_B7E')

    ChrTalk(
        0x000B,
        (
            '#1070430026V#2P嗯，你们听我说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1070430027V#2P其实我现在在做\n',
            '整个卢安地区的食材清单……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1070430028V#2P不过最近有很多危险的魔兽出没，\n',
            '我想去探索也没那个本事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1070430029V#2P所以就想到要找你们\n',
            '这些游击士帮忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010430030V#1015F#1P哦，原来是这样……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430031V#1000F具体需要帮你\n',
            '做些什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1070430032V#2P先看看这个吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '【暂定版魔兽食材清单】\n',
            '·魔兽羽翼·魔兽尾巴\n',
            '·魔兽眼珠·魔兽甲壳\n',
            '·魔兽之肉·魔兽之种\n',
            '·魔兽鱼肉·魔兽明胶',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0101,
        (
            '#0010430033V#1015F#1P等等啊，总之我先记下来了……\n',
            '这就是你刚才说的清单？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1070430034V#2P嗯，虽然还是未完成版。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1070430035V#2P我希望你们能找到这张\n',
            '清单上没有列出的魔兽食材。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1070430036V#2P记住，是清单上『没有』的食材。\n',
            '这点可别搞错了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1070430037V#2P发现了上面没有的食材\n',
            '就再到这里来报告吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1070430038V#2P当然，收集了一定数量后\n',
            '再来报告也没问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1070430039V#2P只不过每种食材\n',
            '需要留下一个作为样本，\n',
            '注意别吃得过头了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010430040V#1006F#1P得到了清单上没有的食材\n',
            '再来这里报告就行了是吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430041V#1015F不过一共有多少种类呢？\n',
            '就是没有出现在那个清单上的食材。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1070430042V#2P我也不知道确切数字，\n',
            '不过充其量也就是５、６种。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1070430043V#2P你们只要找到其中的一半\n',
            '我就会正常支付报酬的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1070430044V#2P还有什么其它要问的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010430045V#1000F#1P不，基本上都明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430046V好，我们会耐心地做的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1070430047V#2P嗯，那就好。\n',
            '不过这不是什么紧急的工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1070430048V#2P那么我就静候佳音了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0065, 0x04, 0x04)
    OP_28(0x0065, 0x04, 0x08)
    OP_28(0x0065, 0x01, 0x0001)
    OP_28(0x0065, 0x01, 0x0002)

    def _loc_1150(): pass

    label('loc_1150')

    OP_30(0x00)
    OP_4B(0x000B, 0)
    OP_8C(0x000B, 0, 0)
    EventEnd(0x00)

    Return()

# id: 0x0003 offset: 0x1160
@scena.Code('func_03_1160')
def func_03_1160():
    EventBegin(0x00)
    Fade(1000)
    OP_8C(0x000B, 180, 0)
    OP_4A(0x000B, 255)
    Call(1, 0x0001)
    OP_69(0x000B, 0x00000000)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x000B,
        (
            '#1070430049V#2P哟，找到什么了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010430050V#1015F#1P不，这倒没有。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430051V其实是我们有事情要办……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1070430052V#2P莫非是调查\n',
            '不能继续了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010430053V#1007F#1P嗯，是的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430054V对不起，\n',
            '半途而废了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1070430055V#2P不，别介意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1070430056V#2P因为我拜托你们调查的部分\n',
            '你们已经完成了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1070430057V#2P那么，我会通知协会说\n',
            '你们已经完成了委托。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1070430058V#2P那样的话你们应该能拿到报酬的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010430059V#1000F#1P谢谢，真是帮了我们的忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1070430060V#2P那么，诸位。\n',
            '这回辛苦你们了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1070430061V#2P下次工作时再见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010430062V#1000F#1P嗯，再见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_141A',
    )

    ChrTalk(
        0x0106,
        (
            '#0050430063V#051F#4P嗯，再见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_143E')

    def _loc_141A(): pass

    label('loc_141A')

    ChrTalk(
        0x0103,
        (
            '#0030430064V#020F#4P嗯，再见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_143E(): pass

    label('loc_143E')

    OP_22(0x0017, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【收集食材】',
            (TxtCtl.SetColor, 0x0),
            '完成了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x0004)
    OP_4B(0x000B, 255)
    OP_8C(0x000B, 0, 0)
    EventEnd(0x00)

    Return()

# id: 0x0004 offset: 0x149D
@scena.Code('func_04_149D')
def func_04_149D():
    TalkBegin(0x000B)

    If(
        (
            (Expr.Eval, "OP_29(0x0065, 0x01, 0x4000)"),
            Expr.Return,
        ),
        'loc_1537',
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
            TXT(0x00, '【报告】\n'),
            TXT(0x01, '【结束调查】\n'),
            TXT(0x02, '【放弃】\n'),
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
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1512',
    )

    Call(1, 0x0005)

    Jump('loc_1534')

    def _loc_1512(): pass

    label('loc_1512')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1534',
    )

    Call(1, 0x0003)
    OP_28(0x0065, 0x04, 0x10)
    OP_28(0x0065, 0x01, 0x0400)
    OP_A2(0x0004)

    Jump('loc_1534')

    def _loc_1534(): pass

    label('loc_1534')

    Jump('loc_1591')

    def _loc_1537(): pass

    label('loc_1537')

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
            TXT(0x00, '【报告】\n'),
            TXT(0x01, '【放弃】\n'),
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
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_158D',
    )

    Jump('loc_1591')

    def _loc_158D(): pass

    label('loc_158D')

    Call(1, 0x0005)

    def _loc_1591(): pass

    label('loc_1591')

    TalkEnd(0x000B)

    Return()

# id: 0x0005 offset: 0x1595
@scena.Code('func_05_1595')
def func_05_1595():
    OP_4A(0x000B, 255)

    ChrTalk(
        0x000B,
        (
            '#1070430065V哟，找到了什么吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '给奥维德看了身上的食材。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

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
            (Expr.Eval, "OP_40(0x03A1, 0x00)"),
            (Expr.Eval, "OP_29(0x0065, 0x01, 0x0004)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1616',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_1616(): pass

    label('loc_1616')

    If(
        (
            (Expr.Eval, "OP_40(0x03A3, 0x00)"),
            (Expr.Eval, "OP_29(0x0065, 0x01, 0x0008)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1632',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_1632(): pass

    label('loc_1632')

    If(
        (
            (Expr.Eval, "OP_40(0x039E, 0x00)"),
            (Expr.Eval, "OP_29(0x0065, 0x01, 0x0010)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_164E',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_164E(): pass

    label('loc_164E')

    If(
        (
            (Expr.Eval, "OP_40(0x03A7, 0x00)"),
            (Expr.Eval, "OP_29(0x0065, 0x01, 0x0020)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_166A',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_166A(): pass

    label('loc_166A')

    If(
        (
            (Expr.Eval, "OP_40(0x03AA, 0x00)"),
            (Expr.Eval, "OP_29(0x0065, 0x01, 0x0040)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1686',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_1686(): pass

    label('loc_1686')

    If(
        (
            (Expr.Eval, "OP_40(0x03A9, 0x00)"),
            (Expr.Eval, "OP_29(0x0065, 0x01, 0x0080)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_16A2',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_16A2(): pass

    label('loc_16A2')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x1),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_24B2',
    )

    OP_62(0x000B, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1500)

    OP_63(0x000B)
    Sleep(400)

    OP_62(0x000B, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000B,
        (
            '#1070430066V哟……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1070430067V这个食材\n',
            '清单上应该没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    If(
        (
            (Expr.Eval, "OP_40(0x03A1, 0x00)"),
            (Expr.Eval, "OP_29(0x0065, 0x01, 0x0004)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_177A',
    )

    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.Item, ItemTable['魔兽之骨']),
            (TxtCtl.SetColor, 0x0),
            '的报告完成！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_28(0x0065, 0x01, 0x0004)

    def _loc_177A(): pass

    label('loc_177A')

    If(
        (
            (Expr.Eval, "OP_40(0x03A3, 0x00)"),
            (Expr.Eval, "OP_29(0x0065, 0x01, 0x0008)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_17B9',
    )

    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.Item, ItemTable['魔兽之牙']),
            (TxtCtl.SetColor, 0x0),
            '的报告完成！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_28(0x0065, 0x01, 0x0008)

    def _loc_17B9(): pass

    label('loc_17B9')

    If(
        (
            (Expr.Eval, "OP_40(0x039E, 0x00)"),
            (Expr.Eval, "OP_29(0x0065, 0x01, 0x0010)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_17F8',
    )

    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.Item, ItemTable['魔兽之角']),
            (TxtCtl.SetColor, 0x0),
            '的报告完成！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_28(0x0065, 0x01, 0x0010)

    def _loc_17F8(): pass

    label('loc_17F8')

    If(
        (
            (Expr.Eval, "OP_40(0x03A7, 0x00)"),
            (Expr.Eval, "OP_29(0x0065, 0x01, 0x0020)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1837',
    )

    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.Item, ItemTable['魔兽鸟肉']),
            (TxtCtl.SetColor, 0x0),
            '的报告完成！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_28(0x0065, 0x01, 0x0020)

    def _loc_1837(): pass

    label('loc_1837')

    If(
        (
            (Expr.Eval, "OP_40(0x03AA, 0x00)"),
            (Expr.Eval, "OP_29(0x0065, 0x01, 0x0040)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1876',
    )

    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.Item, ItemTable['魔兽鱼卵']),
            (TxtCtl.SetColor, 0x0),
            '的报告完成！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_28(0x0065, 0x01, 0x0040)

    def _loc_1876(): pass

    label('loc_1876')

    If(
        (
            (Expr.Eval, "OP_40(0x03A9, 0x00)"),
            (Expr.Eval, "OP_29(0x0065, 0x01, 0x0080)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_18B5',
    )

    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.Item, ItemTable['魔兽鸟蛋']),
            (TxtCtl.SetColor, 0x0),
            '的报告完成！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_28(0x0065, 0x01, 0x0080)

    def _loc_18B5(): pass

    label('loc_18B5')

    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_0D()
    Sleep(400)

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
            (Expr.Eval, "OP_29(0x0065, 0x01, 0x0004)"),
            Expr.Return,
        ),
        'loc_18EC',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_18EC(): pass

    label('loc_18EC')

    If(
        (
            (Expr.Eval, "OP_29(0x0065, 0x01, 0x0008)"),
            Expr.Return,
        ),
        'loc_1901',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_1901(): pass

    label('loc_1901')

    If(
        (
            (Expr.Eval, "OP_29(0x0065, 0x01, 0x0010)"),
            Expr.Return,
        ),
        'loc_1916',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_1916(): pass

    label('loc_1916')

    If(
        (
            (Expr.Eval, "OP_29(0x0065, 0x01, 0x0020)"),
            Expr.Return,
        ),
        'loc_192B',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_192B(): pass

    label('loc_192B')

    If(
        (
            (Expr.Eval, "OP_29(0x0065, 0x01, 0x0040)"),
            Expr.Return,
        ),
        'loc_1940',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_1940(): pass

    label('loc_1940')

    If(
        (
            (Expr.Eval, "OP_29(0x0065, 0x01, 0x0080)"),
            Expr.Return,
        ),
        'loc_1955',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_1955(): pass

    label('loc_1955')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1DD4',
    )

    FadeOut(1000, 0, -1)
    OP_0D()
    EventBegin(0x00)
    OP_8C(0x000B, 180, 0)
    Call(1, 0x0001)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x000B,
        (
            '#1070430068V#2P嗯，这个可了不得。\n',
            '是超过我预计的成果。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1070430069V#2P现在可以说\n',
            '已经是完美的清单了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1070430070V#2P哎呀，诸位游击士。\n',
            '你们这次的工作完成得非常出色。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010430071V#1001F#1P嘿嘿，您过奖了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430072V那么，委托就算完成了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1070430073V#2P嗯，成果超过了预期，\n',
            '所以我要给你们额外奖励。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1070430074V#2P这是我的产品，\n',
            '祝你们好胃口。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了２０个',
            (TxtCtl.Item, ItemTable['魔兽羽翼']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(ItemTable['魔兽羽翼'], 20)

    If(
        (
            (Expr.Eval, "OP_42(0x26)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_1BA7',
    )

    ChrTalk(
        0x0127,
        (
            '#0280430075V#153F#3P哇、哇～！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280430076V这…这些东西…\n',
            '这个能吃吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1BA7(): pass

    label('loc_1BA7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_1BE5',
    )

    ChrTalk(
        0x0106,
        (
            '#0050430077V#053F#4P（……………………………）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C19')

    def _loc_1BE5(): pass

    label('loc_1BE5')

    ChrTalk(
        0x0103,
        (
            '#0030430078V#026F#4P（……………………………）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C19(): pass

    label('loc_1C19')

    ChrTalk(
        0x0101,
        (
            '#0010430079V#1008F#1P哈、哈哈……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430080V拿、拿了这么多\n',
            '真不好意思。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1070430081V#2P不，这是和你们的\n',
            '工作成果相符的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1070430082V#2P好了，别客气，\n',
            '收下来吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010430083V#1016F#1P哈哈……\n',
            '那、那我们就不客气了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1070430084V#2P嗯，你们这次\n',
            '真是辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1070430085V#2P那么，我们在下次工作时再见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_2B(0x0065, 0x0001)
    OP_2C(0x0065, 0x03E8)
    OP_28(0x0065, 0x04, 0x10)
    OP_28(0x0065, 0x01, 0x0400)
    OP_A2(0x0004)
    OP_22(0x0017, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【收集食材】',
            (TxtCtl.SetColor, 0x0),
            '完成了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x0004)
    EventEnd(0x00)

    Jump('loc_24AF')

    def _loc_1DD4(): pass

    label('loc_1DD4')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x4),
            Expr.Geq,
            (Expr.Eval, "OP_29(0x0065, 0x01, 0x4000)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_245E',
    )

    FadeOut(1000, 0, -1)
    OP_0D()
    EventBegin(0x00)
    OP_8C(0x000B, 180, 0)
    Call(1, 0x0001)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x000B,
        (
            '#1070430086V#2P嗯，你们已经找到很多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1070430087V#2P清单也几乎要完成了。\n',
            '可以说你们的工作已经干得很不错了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010430088V#1000F#1P那么，委托算是完成了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1070430089V#2P嗯，这么说确实也可以……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1070430090V#2P怎么样，想不想\n',
            '继续调查呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010430091V#1004F#1P咦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1070430092V#2P就是问你们想不想\n',
            '帮我完成清单。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1070430093V#2P估计还有２、３种\n',
            '食材没被找到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1070430094V#2P如果你们都能找到的话，\n',
            '我也会提供额外奖励……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1070430095V#2P怎么样？',
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
            TXT(0x00, '【结束调查】\n'),
            TXT(0x01, '【继续调查】\n'),
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
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2260',
    )

    ChrTalk(
        0x0101,
        (
            '#0010430096V#1015F#1P不了，还是\n',
            '到此为止吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430097V我们也还有其它的工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1070430098V#2P唔，看来你们完全没兴趣啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1070430099V#2P不过这也没办法。\n',
            '工作就到此为止吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1070430100V#2P我会按照约定\n',
            '全额支付报酬的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1070430101V#2P好，辛苦你们了。\n',
            '下次工作时再见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_21A9',
    )

    ChrTalk(
        0x0106,
        (
            '#0050430102V#051F#4P嗯，再见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_21CD')

    def _loc_21A9(): pass

    label('loc_21A9')

    ChrTalk(
        0x0103,
        (
            '#0030430103V#020F#4P嗯，再见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_21CD(): pass

    label('loc_21CD')

    ChrTalk(
        0x0101,
        (
            '#0010430104V#1006F#1P那么也希望你努力工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0065, 0x04, 0x10)
    OP_28(0x0065, 0x01, 0x0400)
    OP_A2(0x0004)
    OP_22(0x0017, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【收集食材】',
            (TxtCtl.SetColor, 0x0),
            '完成了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x0004)

    Jump('loc_2459')

    def _loc_2260(): pass

    label('loc_2260')

    OP_28(0x0065, 0x01, 0x4000)

    ChrTalk(
        0x0101,
        (
            '#0010430105V#1006F#1P嗯，我们试试。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430106V只做到一半，我们\n',
            '也觉得不畅快。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1070430107V#2P我就知道你会这么说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1070430108V#2P那报告什么的\n',
            '都请按和以前一样的顺序来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1070430109V#2P如果你们有急事\n',
            '而不能继续的话就跟我说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1070430110V#2P到时候我再想办法。\n',
            '不过报酬就只有一般程度的了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_23D9',
    )

    ChrTalk(
        0x0106,
        (
            '#0050430111V#051F#4P原来如此，明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2405')

    def _loc_23D9(): pass

    label('loc_23D9')

    ChrTalk(
        0x0103,
        (
            '#0030430112V#020F#4P原来如此，明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2405(): pass

    label('loc_2405')

    ChrTalk(
        0x0101,
        (
            '#0010430113V#1006F#1P那我们就走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1070430114V#2P我可等着你们的报告哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_2459(): pass

    label('loc_2459')

    EventEnd(0x00)

    Jump('loc_24AF')

    def _loc_245E(): pass

    label('loc_245E')

    ChrTalk(
        0x000B,
        (
            '#1070430115V应该还有一些食材\n',
            '是清单上没有的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1070430116V继续努力吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_24AF(): pass

    label('loc_24AF')

    Jump('loc_2538')

    def _loc_24B2(): pass

    label('loc_24B2')

    OP_62(0x000B, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1500)

    OP_63(0x000B)
    Sleep(400)

    ChrTalk(
        0x000B,
        (
            '#1070430117V唔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1070430118V很遗憾，\n',
            '好像没有新的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1070430119V下次再来报告吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_2538(): pass

    label('loc_2538')

    OP_4B(0x000B, 0)
    OP_8C(0x000B, 0, 0)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
