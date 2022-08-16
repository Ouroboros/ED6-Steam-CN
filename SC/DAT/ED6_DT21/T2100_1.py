import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T2100_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2100_1 ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'T2100.x'
    header.mapIndex       = 1
    header.bgm            = 12
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
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0245, 3, 0x122B)),
            Expr.Return,
        ),
        'loc_539',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x00, 0x08)"),
            (Expr.Eval, "OP_29(0x0069, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0069, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_D3',
    )

    Call(1, 0x0002)

    Jump('loc_536')

    def _loc_D3(): pass

    label('loc_D3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_117',
    )

    ChrTalk(
        0x00FE,
        (
            '现在正在进行选举，\n',
            '客人相当少。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '请好好\n',
            '休息吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_536')

    def _loc_117(): pass

    label('loc_117')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_221',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x00, 0x10)"),
            (Expr.Eval, "OP_29(0x0069, 0x00, 0x40)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_1CC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_185',
    )

    ChrTalk(
        0x00FE,
        (
            '呵呵呵，\n',
            '看起来事件已经解决了嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我的证言\n',
            '也稍微派上点用场了不？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C9')

    def _loc_185(): pass

    label('loc_185')

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x00FE,
        (
            '呵呵呵，\n',
            '看起来事件已经解决了嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊，这真值得庆贺哟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C9(): pass

    label('loc_1C9')

    Jump('loc_21E')

    def _loc_1CC(): pass

    label('loc_1CC')

    ChrTalk(
        0x00FE,
        (
            '无论选举结果如何，\n',
            '我都只是在这里当班而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '以前是这样，\n',
            '以后也是这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_21E(): pass

    label('loc_21E')

    Jump('loc_536')

    def _loc_221(): pass

    label('loc_221')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_36F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_275',
    )

    ChrTalk(
        0x00FE,
        (
            '需要小船的话\n',
            '随时都可以来找我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在的话，可以随便坐哟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_36C')

    def _loc_275(): pass

    label('loc_275')

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_326',
    )

    ChrTalk(
        0x00FE,
        (
            '噢，你是刚才\n',
            '借用小船的人嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '怎样？\n',
            '想出好诗来了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#030F呼，托您的福创作出来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '奥利维尔·朗海姆\n',
            '毕生的大作啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵呵，\n',
            '那可太好喽。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_36C')

    def _loc_326(): pass

    label('loc_326')

    ChrTalk(
        0x00FE,
        (
            '刚才\n',
            '桥那边真吵得厉害。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '忽然安静下来了，\n',
            '我还觉得有点奇怪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_36C(): pass

    label('loc_36C')

    Jump('loc_536')

    def _loc_36F(): pass

    label('loc_36F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 4, 0x121C)),
            Expr.Return,
        ),
        'loc_3AC',
    )

    ChrTalk(
        0x00FE,
        (
            '哎呀，什么啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好像\n',
            '驶向大桥那边去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_536')

    def _loc_3AC(): pass

    label('loc_3AC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_477',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_402',
    )

    ChrTalk(
        0x00FE,
        (
            '为了创作诗词\n',
            '乘船在水上游来游去……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还真是风雅的人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_474')

    def _loc_402(): pass

    label('loc_402')

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x00FE,
        (
            '小船刚刚\n',
            '借出去了哟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '自称是什么旅行者，\n',
            '还真是风雅的人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要在船上创作诗词……\n',
            '他是这么说的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_474(): pass

    label('loc_474')

    Jump('loc_536')

    def _loc_477(): pass

    label('loc_477')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_4E1',
    )

    ChrTalk(
        0x00FE,
        (
            '我明白选举很重要，\n',
            '但最好还是不要大声叫喊吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看了海报谁要说什么\n',
            '大家也都知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_536')

    def _loc_4E1(): pass

    label('loc_4E1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_536',
    )

    ChrTalk(
        0x00FE,
        (
            '现在正在进行选举，\n',
            '客人也少了很多哟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '太悠闲了，弄得\n',
            '我都想钓鱼了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_536(): pass

    label('loc_536')

    Jump('loc_8F0')

    def _loc_539(): pass

    label('loc_539')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 4, 0x121C)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_57F',
    )

    ChrTalk(
        0x00FE,
        (
            '哎呀，什么来的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好像\n',
            '是驶向大桥那边去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8F0')

    def _loc_57F(): pass

    label('loc_57F')

    ChrTurnDirection(0x00FE, 0x0101, 0)
    SetScenaFlags(ScenaFlag(0x0245, 3, 0x122B))
    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    ChrTalk(
        0x00FE,
        (
            '哎呀，还在想是谁呢……\n',
            '真是好久不见了哟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x00, 0x08)"),
            (Expr.Eval, "OP_29(0x0069, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0069, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_720',
    )

    ChrTalk(
        0x0101,
        (
            '#1000F啊，老爷爷还好吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我记得上桥的时候\n',
            '借了您的小船吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#048F那时真是\n',
            '多谢您了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0105, 400)

    ChrTalk(
        0x00FE,
        (
            '哪里哪里，\n',
            '小事一桩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那，今天\n',
            '是来乘船游玩的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1007F很遗憾，又是工作。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我们正在调查\n',
            '酒店发生的事件呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '呵，那可辛苦哟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有什么想知道的\n',
            '就尽管问吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1006F嗯，谢谢。\n',
            '那我就问了哟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(1, 0x0002)

    Jump('loc_8F0')

    def _loc_720(): pass

    label('loc_720')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_7AB',
    )

    ChrTalk(
        0x0101,
        (
            '#1000F啊，老爷爷还好吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我记得上桥的时候\n',
            '借了您的小船吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#047F那时候要是没有船\n',
            '可就不得了了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '真的非常感谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_80A')

    def _loc_7AB(): pass

    label('loc_7AB')

    ChrTalk(
        0x0101,
        (
            '#1000F啊，老爷爷还好吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '记得追赶戴尔蒙市长的时候\n',
            '借了您的小船吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '那时候真是帮大忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_80A(): pass

    label('loc_80A')

    ChrTalk(
        0x00FE,
        (
            '哪里哪里，\n',
            '小事一桩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那，今天\n',
            '是来乘船游玩的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1016F很遗憾，还是工作。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '不过，这次看来\n',
            '是比较轻松了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是吗。\n',
            '那就慢慢来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '选举中客人也少。\n',
            '应该能比之前更放松了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1000F嗯，谢谢。\n',
            '那就先这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8F0(): pass

    label('loc_8F0')

    TalkEnd(0x00FE)

    Return()

# id: 0x0001 offset: 0x8F4
@scena.Code('func_01_8F4')
def func_01_8F4():
    FadeOut(300, 0, 100)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0xFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
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

    SetMessageWindowPos(-1, 16, -1, -1)

    Talk(
        (
            0x18,
            '<FIXME>何を質問しますか？',
            TxtCtl.Enter,
        ),
    )

    OP_CC(0x00, 0x00, 0x000A, 0x000A, 0x01)
    OP_CC(0x01, 0x00, '关于昆茨')

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x01, 0x0001)"),
            Expr.Return,
        ),
        'loc_99E',
    )

    OP_CC(0x01, 0x00, '声响')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0xFFFFFF0),
            Expr.And,
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x1),
            Expr.Mul,
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_99E(): pass

    label('loc_99E')

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x01, 0x0002)"),
            Expr.Return,
        ),
        'loc_9D3',
    )

    OP_CC(0x01, 0x00, '发怒')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0xFFFFF0F),
            Expr.And,
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x10),
            Expr.Mul,
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_9D3(): pass

    label('loc_9D3')

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x01, 0x0008)"),
            Expr.Return,
        ),
        'loc_A0E',
    )

    OP_CC(0x01, 0x00, '关于海利欧')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0xFFFF0FF),
            Expr.And,
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x100),
            Expr.Mul,
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_A0E(): pass

    label('loc_A0E')

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x01, 0x0010)"),
            Expr.Return,
        ),
        'loc_A43',
    )

    OP_CC(0x01, 0x00, '午饭')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0xFFF0FFF),
            Expr.And,
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x1000),
            Expr.Mul,
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_A43(): pass

    label('loc_A43')

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x01, 0x0040)"),
            Expr.Return,
        ),
        'loc_A78',
    )

    OP_CC(0x01, 0x00, '钟声')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0xFF0FFFF),
            Expr.And,
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x10000),
            Expr.Mul,
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_A78(): pass

    label('loc_A78')

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x01, 0x0800)"),
            Expr.Return,
        ),
        'loc_AB1',
    )

    OP_CC(0x01, 0x00, '善后处理')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0xF0FFFFF),
            Expr.And,
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x100000),
            Expr.Mul,
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_AB1(): pass

    label('loc_AB1')

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x01, 0x2000)"),
            Expr.Return,
        ),
        'loc_AEC',
    )

    OP_CC(0x01, 0x00, '关于贝尔夫')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0xFFFFFF),
            Expr.And,
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x1000000),
            Expr.Mul,
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_AEC(): pass

    label('loc_AEC')

    OP_CC(0x01, 0x00, '离开')
    OP_CC(0x02, 0x00)
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

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B2B',
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_C31')

    def _loc_B2B(): pass

    label('loc_B2B')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x1),
            Expr.Div,
            (Expr.PushLong, 0xF),
            Expr.And,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B4F',
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_C31')

    def _loc_B4F(): pass

    label('loc_B4F')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x10),
            Expr.Div,
            (Expr.PushLong, 0xF),
            Expr.And,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B73',
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_C31')

    def _loc_B73(): pass

    label('loc_B73')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x100),
            Expr.Div,
            (Expr.PushLong, 0xF),
            Expr.And,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B97',
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_C31')

    def _loc_B97(): pass

    label('loc_B97')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x1000),
            Expr.Div,
            (Expr.PushLong, 0xF),
            Expr.And,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_BBB',
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_C31')

    def _loc_BBB(): pass

    label('loc_BBB')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x10000),
            Expr.Div,
            (Expr.PushLong, 0xF),
            Expr.And,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_BDF',
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_C31')

    def _loc_BDF(): pass

    label('loc_BDF')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x100000),
            Expr.Div,
            (Expr.PushLong, 0xF),
            Expr.And,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C03',
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x6),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_C31')

    def _loc_C03(): pass

    label('loc_C03')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x1000000),
            Expr.Div,
            (Expr.PushLong, 0xF),
            Expr.And,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C27',
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x7),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_C31')

    def _loc_C27(): pass

    label('loc_C27')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_C31(): pass

    label('loc_C31')

    Return()

# id: 0x0002 offset: 0xC32
@scena.Code('func_02_C32')
def func_02_C32():
    Call(1, 0x0001)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_C5F'),
        (0x00000001, 'loc_CD2'),
        (0x00000002, 'loc_FA1'),
        (0x00000003, 'loc_1002'),
        (0x00000004, 'loc_1136'),
        (0x00000005, 'loc_1985'),
        (0x00000006, 'loc_1D8F'),
        (0x00000007, 'loc_1EAE'),
        (-1, 'loc_1F13'),
    )

    def _loc_C5F(): pass

    label('loc_C5F')

    OP_28(0x006A, 0x01, 0x0100)

    ChrTalk(
        0x00FE,
        (
            '#1520441304V唔，我知道。\n',
            '在港口工作的年轻人吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1520441305V最近大概所有人\n',
            '都参加选举运动了哟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F16')

    def _loc_CD2(): pass

    label('loc_CD2')

    OP_28(0x006A, 0x01, 0x0100)

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x01, 0x0080)"),
            Expr.Return,
        ),
        'loc_D81',
    )

    ChrTalk(
        0x00FE,
        (
            '#1520441306V我听到\n',
            '那个大的声响\n',
            '和钟声交替出现。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1520441307V哎呀？我还以为是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1520441308V肚子饿了就没在意，\n',
            '然后就去拉旺塔尔游戏吧了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F9E')

    def _loc_D81(): pass

    label('loc_D81')

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x01, 0x0004)"),
            Expr.Return,
        ),
        'loc_DF7',
    )

    ChrTalk(
        0x00FE,
        (
            '#1520441309V忘了是什么时候\n',
            '听到得那阵很大的声音了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1520441310V像是什么碰撞\n',
            '发出的声音似的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F9E')

    def _loc_DF7(): pass

    label('loc_DF7')

    ExecExpressionWithReg(
        0x0004,
        (
            (Expr.PushLong, 0x2),
            Expr.Or2,
            Expr.Return,
        ),
    )

    OP_28(0x0069, 0x01, 0x0001)

    ChrTalk(
        0x00FE,
        (
            '#1520441311V噢，声响啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1520441312V唔，确实上面\n',
            '有传来过什么很大的声音。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010441313V#1004F上面，\n',
            '是说酒店的阳台附近？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#1520441314V唔，大概就是那吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1520441315V像是什么东西碰撞的声音，\n',
            '听到的声音很大。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1520441316V是什么时候听到的，\n',
            '就想不起来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010441317V#1015F嗯……真可惜……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441318V#1006F不过，这情报很有价值。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441319V谢谢老爷爷。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0069, 0x01, 0x0004)

    def _loc_F9E(): pass

    label('loc_F9E')

    Jump('loc_1F16')

    def _loc_FA1(): pass

    label('loc_FA1')

    OP_28(0x006A, 0x01, 0x0100)

    ChrTalk(
        0x00FE,
        (
            '#1520441320V噢，昆茨那家伙\n',
            '那么生气吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1520441321V唉，年轻人\n',
            '就是脾气暴躁。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F16')

    def _loc_1002(): pass

    label('loc_1002')

    OP_28(0x006A, 0x01, 0x0100)

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x8),
            Expr.And,
            Expr.Return,
        ),
        'loc_1084',
    )

    ChrTalk(
        0x00FE,
        (
            '#1520441322V海利欧…\n',
            '就是那个年轻的商人吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1520441323V看起来是个教养良好，\n',
            '老老实实的年轻人哟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1133')

    def _loc_1084(): pass

    label('loc_1084')

    ExecExpressionWithReg(
        0x0004,
        (
            (Expr.PushLong, 0x8),
            Expr.Or2,
            Expr.Return,
        ),
    )

    ChrTalk(
        0x00FE,
        (
            '#1520441324V唔，海利欧…\n',
            '就是那个年轻的商人吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1520441325V作为商人，相貌\n',
            '没有点魄力可是不行的哟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1520441326V脸这么老实，\n',
            '就都只想跟他讨价还价了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1133(): pass

    label('loc_1133')

    Jump('loc_1F16')

    def _loc_1136(): pass

    label('loc_1136')

    OP_28(0x006A, 0x01, 0x0100)

    If(
        (
            (Expr.Eval, "OP_29(0x006A, 0x01, 0x0020)"),
            Expr.Return,
        ),
        'loc_11E5',
    )

    ChrTalk(
        0x00FE,
        (
            '#1520441327V和平常一样听到钟声\n',
            '就去拉旺塔尔游戏吧了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1520441328V那时酒店地下室里\n',
            '没有一个人哟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1520441329V回来的时候\n',
            '诺曼的儿子来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1982')

    def _loc_11E5(): pass

    label('loc_11E5')

    If(
        (
            (Expr.Eval, "OP_29(0x006A, 0x01, 0x0002)"),
            Expr.Return,
        ),
        'loc_14E5',
    )

    OP_28(0x006A, 0x01, 0x0020)

    ChrTalk(
        0x00FE,
        (
            '#1520441330V今天中午\n',
            '去拉旺塔尔游戏吧了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1520441331V我习惯每天听到\n',
            '钟声时出去吃午饭。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010441332V#1011F哎呀，真是有品味的生活呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441333V#1015F不过，既然出去了，\n',
            '应该是从酒店中走出去的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#1520441334V当然喽。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1520441335V又不可能\n',
            '从海上飞过去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010441336V#1016F啊哈哈，那倒是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441337V#1000F……那，当时\n',
            '在酒店中看见谁了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1520441338V当然１楼\n',
            '有亚内斯特在……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1520441339V其他地方都很安静。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010441340V#1011F咦……？\n',
            '就没别人了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1520441341V唔，我去的时候\n',
            '地下和１楼都很安静。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1520441329V回来的时候\n',
            '诺曼的儿子来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010441343V#1015F诺曼的儿子……\n',
            '对了，是贝尔夫吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441344V#1006F嗯，知道这个就足够了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1520441345V哪里哪里。\n',
            '那么，再见喽。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1982')

    def _loc_14E5(): pass

    label('loc_14E5')

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x01, 0x0040)"),
            Expr.Return,
        ),
        'loc_1557',
    )

    ChrTalk(
        0x00FE,
        (
            '#1520441346V今天要去\n',
            '拉旺塔尔游戏吧吃饭呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1520441347V我习惯每天听到\n',
            '钟声时出去吃午饭。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1982')

    def _loc_1557(): pass

    label('loc_1557')

    OP_28(0x0069, 0x01, 0x0040)

    ChrTalk(
        0x00FE,
        (
            '#1520441348V唔，午饭吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1520441349V今天午饭\n',
            '是在拉旺塔尔游戏吧吃的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1520441350V每天听到',
            (TxtCtl.SetColor, 0x4),
            '『钟声』',
            (TxtCtl.SetColor, 0x0),
            '的时候\n',
            '出去吃午饭是我的习惯。',
            TxtCtl.Enter,
        ),
    )

    PlaySE(17, 0x00, 0x64)
    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010441351V#1011F钟声……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0101, 400)

    ChrTalk(
        0x0105,
        (
            '#0060441352V#040F就是伦格兰德大桥的钟。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060441353V恩，吊桥上\n',
            '钟响了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0105, 400)

    ChrTalk(
        0x0101,
        (
            '#0010441354V#1018F啊，想起来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441355V嗯嗯，确实会响。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1520441356V固定时间到了就会响。\n',
            '已经代替我们的钟表了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x00FE, 400)

    ChrTalk(
        0x0101,
        (
            '#0010441357V#1000F咦，还可以这样用啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441358V要代替钟表的话\n',
            '形状好象稍微大了点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060441359V#040F不过，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060441360V问问大家关于钟声的事\n',
            '说不定很有帮助呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0105, 400)

    ChrTalk(
        0x0101,
        (
            '#0010441361V#1004F啊？为什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060441362V#040F钟声响起时发生的事\n',
            '他们一定记得特别清楚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060441363V钟声就是记忆的标志。\n',
            '就像这位老爷爷一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010441364V#1000F啊啊～原来如此～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441365V#1001F不愧是科洛丝。\n',
            '好理智的建议哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060441366V#048F呵呵，可别\n',
            '太夸我了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1520441367V唔，虽不知道怎么了，\n',
            '看来是有好事喽。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x00FE, 400)

    ChrTalk(
        0x0101,
        (
            '#0010441368V#1006F嗯，很好哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441369V那，赶快\n',
            '去问问看吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060341522V#041F好！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1982(): pass

    label('loc_1982')

    Jump('loc_1F16')

    def _loc_1985(): pass

    label('loc_1985')

    OP_28(0x006A, 0x01, 0x0100)

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x01, 0x0080)"),
            Expr.Return,
        ),
        'loc_1A34',
    )

    ChrTalk(
        0x00FE,
        (
            '#1520441306V我听到\n',
            '那个大的声响\n',
            '和钟声交替出现。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1520441307V哎呀？我还以为是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1520441308V肚子饿了就没在意，\n',
            '然后就去拉旺塔尔游戏吧了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D8C')

    def _loc_1A34(): pass

    label('loc_1A34')

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x01, 0x0004)"),
            Expr.Return,
        ),
        'loc_1D2E',
    )

    OP_28(0x0069, 0x01, 0x0080)

    ChrTalk(
        0x00FE,
        (
            '#1520441374V伦格兰德大桥\n',
            '的钟声啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1520441375V那可是我们生活中\n',
            '不可缺少的声音哟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1520441376V啊，说到钟声……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010441377V#1002F……想到什么了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#1520441378V不是，你……\n',
            '刚才问了什么吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1520441379V喏，就是那个，\n',
            '很大的声音怎么了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010441380V#1004F啊，声响的事？\n',
            '好像碰撞的声音那样的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1520441381V喔，就是那个。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1520441382V说起来好像是\n',
            '听到钟声的同时\n',
            '也听到那个声音了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010441383V#1015F和钟声交替……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441384V……也就是说，那个大的声响\n',
            '几乎是和钟声同时听见的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1520441385V唔，简单的说\n',
            '就是那样喽。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060441386V#042F如果那个声响\n',
            '是犯人发出的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010441387V#1002F钟声响起的时候\n',
            '没有不在场证明的就是犯人对吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441388V嗯，有必要确认\n',
            '一下嫌疑犯了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D8C')

    def _loc_1D2E(): pass

    label('loc_1D2E')

    ChrTalk(
        0x00FE,
        (
            '#1520441374V伦格兰德大桥\n',
            '的钟声啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1520441375V那可是我们生活中\n',
            '不可缺少的声音哟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1D8C(): pass

    label('loc_1D8C')

    Jump('loc_1F16')

    def _loc_1D8F(): pass

    label('loc_1D8F')

    OP_28(0x006A, 0x01, 0x0100)

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x40),
            Expr.And,
            Expr.Return,
        ),
        'loc_1E37',
    )

    ChrTalk(
        0x00FE,
        (
            '#1520441391V唔，到底是谁\n',
            '帮忙收拾了盘子呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1520441392V问我也没用哟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1520441393V那个时候我正在拉旺塔尔游戏吧里\n',
            '悠闲地吃着饭呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1EAB')

    def _loc_1E37(): pass

    label('loc_1E37')

    ExecExpressionWithReg(
        0x0004,
        (
            (Expr.PushLong, 0x40),
            Expr.Or2,
            Expr.Return,
        ),
    )

    ChrTalk(
        0x00FE,
        (
            '#1520441394V呵，有人代替亚内斯特\n',
            '收拾了盘子吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1520441395V呵呵呵，那可是近来\n',
            '少见的好心人那。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1EAB(): pass

    label('loc_1EAB')

    Jump('loc_1F16')

    def _loc_1EAE(): pass

    label('loc_1EAE')

    OP_28(0x006A, 0x01, 0x0100)

    ChrTalk(
        0x00FE,
        (
            '#1520441396V唔，贝尔夫\n',
            '是说那个年轻人吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1520441397V嗯……应该\n',
            '不在地下室的呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F16')

    def _loc_1F13(): pass

    label('loc_1F13')

    Jump('loc_1F16')

    def _loc_1F16(): pass

    label('loc_1F16')

    Return()

# id: 0x0003 offset: 0x1F17
@scena.Code('func_03_1F17')
def func_03_1F17():
    EventBegin(0x00)
    ChrSetPos(0x0101, 65180, 240, 94310, 90)
    ChrSetPos(0x00F7, 64550, 0, 95280, 90)
    ChrSetPos(0x0104, 64319, 0, 93660, 90)
    ChrSetPos(0x0127, 63690, 170, 94700, 90)
    CameraMove(65440, 260, 94110, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeIn(1500, 0)
    OP_0D()
    Sleep(1000)

    OP_70(0x0010, 20)
    OP_73(0x0010)
    Sleep(750)

    ChrSetPos(0x0031, 69180, 500, 93590, 0)
    ChrClearFlags(0x0031, 0x0080)
    ChrWalkTo(0x0031, 66157, 500, 93986, 2000, 0x00)
    Sleep(1000)

    If(
        (
            (Expr.Eval, "OP_29(0x0067, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_24B9',
    )

    ChrTalk(
        0x0031,
        (
            '#2940430912V今天百忙之中\n',
            '还麻烦您，真是谢谢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0031,
        (
            '#2940430913V孩子们也\n',
            '非常开心呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x0067, 0x01, 0x2000)"),
            Expr.Return,
        ),
        'loc_207D',
    )

    ChrTalk(
        0x0031,
        (
            '#2940430914V真是\n',
            '出色的授课呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_207D(): pass

    label('loc_207D')

    ChrTalk(
        0x0101,
        (
            '#0010430915V#1001F嘿嘿，谢谢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430916V之前我还挺没底的，\n',
            '你们满意就太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0031,
        (
            '#2940430917V还有其他的课，\n',
            '我就此告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0031,
        (
            '#2940430918V那么，有机会的话\n',
            '还请多指教。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010430486V#1006F嗯，那再见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0031, 69180, 500, 93590, 2000, 0x00)
    ChrSetFlags(0x0031, 0x0080)
    Sleep(500)

    OP_72(0x0010, 0x0800)
    OP_6F(0x0010, 20)
    OP_70(0x0010, 0)
    PlaySE(7, 0x00, 0x64)
    OP_73(0x0010)
    OP_71(0x0010, 0x0800)

    @scena.Lambda('lambda_219C')
    def lambda_219C():
        CameraMove(64560, 0, 94340, 2000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_219C)

    Sleep(2000)

    ChrTurnDirection(0x00F7, 0x0101, 400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_21EE',
    )

    ChrTalk(
        0x0106,
        (
            '#0050430920V#051F看来是\n',
            '顺利完成了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2219')

    def _loc_21EE(): pass

    label('loc_21EE')

    ChrTalk(
        0x0103,
        (
            '#0030430921V#021F呵呵，不算太顺利啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2219(): pass

    label('loc_2219')

    ChrSetDirection(0x0101, 270, 400)

    ChrTalk(
        0x0101,
        (
            '#0010430922V#1015F呼，勉强……吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0104, 0x0101, 400)

    ChrTalk(
        0x0104,
        (
            '#0040430923V#031F呼，不用谦虚了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040430924V你让我见识了\n',
            '相当棒的讲师哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010430925V#1008F是，是吗？\n',
            '那就好……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430926V#1003F……只不过，还是\n',
            '感到有点知识不足啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430927V一被问到细节\n',
            '就慌了手脚了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_23A4',
    )

    ChrTalk(
        0x0106,
        (
            '#0050430928V#053F不过，今后多加努力吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050430929V连规章都不熟悉的游击士\n',
            '可是得不到别人信任的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2413')

    def _loc_23A4(): pass

    label('loc_23A4')

    ChrTalk(
        0x0103,
        (
            '#0030430930V#026F不过，今后多加努力吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030430931V#027F连规章都不熟悉的游击士\n',
            '可是得不到别人信任的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2413(): pass

    label('loc_2413')

    ChrTurnDirection(0x0101, 0x00F7, 400)

    ChrTalk(
        0x0101,
        (
            '#0010430932V#1015F说得也是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430933V#1002F嗯，我会努力的。',
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
            '任务【主日学校的讲师】',
            (TxtCtl.SetColor, 0x0),
            '完成了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    Jump('loc_2A15')

    def _loc_24B9(): pass

    label('loc_24B9')

    ChrTalk(
        0x0031,
        (
            '#2940430934V呼，总之\n',
            '今天真是辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0031,
        (
            '#2940430935V孩子们\n',
            '是很开心……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0031,
        (
            '#2940430936V不过，也得\n',
            '再努力点啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x14, 0x17, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010430937V#1007F呜……\n',
            '真，真丢脸。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0031,
        (
            '#2940430938V那样授课\n',
            '可没法得到孩子们的信任哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0031,
        (
            '#2940430939V游击士是孩子们的憧憬，\n',
            '所以要更加努力啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010430940V#1007F是，知道了……\n',
            '我会铭记于心的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0031,
        (
            '#2940430941V那么，我还有课\n',
            '就此告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0031,
        (
            '#2940430942V下次再有机会的话\n',
            '还请多指教。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    ChrWalkTo(0x0031, 69180, 500, 93590, 2000, 0x00)
    ChrSetFlags(0x0031, 0x0080)
    Sleep(500)

    OP_72(0x0010, 0x0800)
    OP_6F(0x0010, 20)
    OP_70(0x0010, 0)
    PlaySE(7, 0x00, 0x64)
    OP_73(0x0010)
    OP_71(0x0010, 0x0800)

    @scena.Lambda('lambda_26C7')
    def lambda_26C7():
        CameraMove(64560, 0, 94340, 2000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_26C7)

    Sleep(2000)

    ChrTurnDirection(0x00F7, 0x0101, 400)
    Sleep(1000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_2775',
    )

    ChrTalk(
        0x0106,
        (
            '#0050430943V#057F……你上了什么课？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0104, 0x0101, 400)

    ChrTalk(
        0x0104,
        (
            '#0040430944V#031F呼，我全都看见了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040430945V简直是超乎想象的授课呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_27D4')

    def _loc_2775(): pass

    label('loc_2775')

    ChrTalk(
        0x0103,
        (
            '#0030430946V#025F哈，好厉害的授课啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0104, 0x0101, 400)

    ChrTalk(
        0x0104,
        (
            '#0040430947V#031F呼，超乎想象的有趣啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_27D4(): pass

    label('loc_27D4')

    ChrTalk(
        0x0127,
        (
            '#0280430948V#151F真的好好玩啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(400)

    ChrSetDirection(0x0101, 270, 400)

    ChrTalk(
        0x0101,
        (
            '#0010430949V#1022F啊～别说啦！\n',
            '我心情都变差了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430950V#1009F呜呜～今后我要好好学习～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430951V要把规章都\n',
            '倒背如流！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_2908',
    )

    ChrTalk(
        0x0106,
        (
            '#0050430952V#053F嗯，好好努力吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050430953V连规章都不熟悉的游击士\n',
            '谁都不会信任你的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2973')

    def _loc_2908(): pass

    label('loc_2908')

    ChrTalk(
        0x0103,
        (
            '#0030430954V#026F嗯，好好努力吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030430955V#027F身为游击士连规章都不知道\n',
            '可是得不到别人信任的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2973(): pass

    label('loc_2973')

    ChrTalk(
        0x0101,
        (
            '#0010430956V#1007F唉，果然是这样……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430957V#1002F好，我要加油！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(262, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【主日学校的讲师】',
            (TxtCtl.SetColor, 0x0),
            '失败了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    def _loc_2A15(): pass

    label('loc_2A15')

    OP_30(0x00)
    EventEnd(0x00)

    Return()

# id: 0x0004 offset: 0x2A1A
@scena.Code('func_04_2A1A')
def func_04_2A1A():
    EventBegin(0x00)
    ChrSetPos(0x002F, 28180, 0, 90850, 325)
    OP_4A(0x002F, 255)
    CameraMove(22810, 0, 94820, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_2A8D',
    )

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)
    ChrSetPos(0x0106, 17370, 0, 97650, 24)

    Jump('loc_2AA9')

    def _loc_2A8D(): pass

    label('loc_2A8D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_2AA9',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)
    ChrSetPos(0x0103, 17370, 0, 97650, 24)

    def _loc_2AA9(): pass

    label('loc_2AA9')

    FormationAddMember(ChrTable['奥利维尔'], 0xFF, 0xFF)
    ChrSetPos(0x0104, 17370, 0, 97650, 24)
    ChrSetPos(0x0101, 17370, 0, 97650, 24)
    ChrSetPos(0x0105, 17370, 0, 97650, 24)
    Sleep(1000)

    FadeIn(2000, 0)
    OP_0D()
    Sleep(1000)

    OP_70(0x000A, 29)
    OP_73(0x000A)
    Sleep(400)

    CreateThread(0x0101, 0x01, 0x01, 0x0008)
    Sleep(500)

    CreateThread(0x0105, 0x01, 0x01, 0x0009)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_2B2C',
    )

    CreateThread(0x0106, 0x01, 0x01, 0x0006)

    Jump('loc_2B3A')

    def _loc_2B2C(): pass

    label('loc_2B2C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_2B3A',
    )

    CreateThread(0x0103, 0x01, 0x01, 0x0006)

    def _loc_2B3A(): pass

    label('loc_2B3A')

    Sleep(500)

    CreateThread(0x0104, 0x01, 0x01, 0x0007)
    Sleep(400)

    OP_72(0x000A, 0x0800)
    OP_6F(0x000A, 29)
    OP_70(0x000A, 0)
    PlaySE(7, 0x00, 0x64)
    OP_73(0x000A)
    OP_71(0x000A, 0x0800)
    WaitForThreadExit(0x0104, 0x0001)
    Sleep(600)

    ChrTalk(
        0x0101,
        (
            '#0010441930V#1000F呼，总算解决了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441931V虽然做梦也没想到\n',
            '结果会变成这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040441932V#030F真是事实更甚于小说……呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040441933V#031F呼，能够顺利解决\n',
            '身为协力人员的我也很得意啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0104, 400)

    ChrTalk(
        0x0101,
        (
            '#0010441934V#1019F你可是什么也没干啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0105, 400)

    ChrTalk(
        0x0101,
        (
            '#0010441935V#1006F啊，不过\n',
            '真是非常感谢科洛丝啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441936V给了那么多忠告，\n',
            '调查也帮了好多忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0101, 400)

    ChrTalk(
        0x0105,
        (
            '#0060441937V#048F呵呵，太好了。\n',
            '看来帮上忙了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060441938V但是，艾丝蒂尔。\n',
            '感谢就不必了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010441939V#1008F是啊，你们俩\n',
            '都是协力人员了嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00F7, 0x0105, 400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_2DEB',
    )

    ChrTalk(
        0x0106,
        (
            '#0050441940V#050F啊啊，只是做了\n',
            '该做的事而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050441941V……那么，差不多该走了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2E4E')

    def _loc_2DEB(): pass

    label('loc_2DEB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_2E4E',
    )

    ChrTalk(
        0x0103,
        (
            '#0030441942V#020F呵呵，只是做了\n',
            '该做的事而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030441943V……那么，差不多该走了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2E4E(): pass

    label('loc_2E4E')

    ChrTurnDirection(0x0101, 0x00F7, 400)

    ChrTalk(
        0x0101,
        (
            '#0010441944V#1006F嗯，接下来该去蔡斯地区了。',
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
            '任务【选举事务所的伤人事件】',
            (TxtCtl.SetColor, 0x0),
            '完成了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_28(0x0069, 0x01, 0x8000)
    OP_28(0x0069, 0x04, 0x10)
    EventEnd(0x00)
    OP_4B(0x002F, 255)

    Return()

# id: 0x0005 offset: 0x2EF3
@scena.Code('func_05_2EF3')
def func_05_2EF3():
    EventBegin(0x00)
    ChrSetPos(0x002F, 28180, 0, 90850, 325)
    OP_4A(0x002F, 255)
    CameraMove(22810, 0, 94820, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_2F55',
    )

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    Jump('loc_2F60')

    def _loc_2F55(): pass

    label('loc_2F55')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_2F60',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    def _loc_2F60(): pass

    label('loc_2F60')

    ChrSetPos(0x00F7, 17370, 0, 97650, 24)
    FormationAddMember(ChrTable['奥利维尔'], 0xFF, 0xFF)
    ChrSetPos(0x0104, 17370, 0, 97650, 24)
    ChrSetPos(0x0101, 24000, 0, 94500, 180)
    ChrSetPos(0x0105, 24000, 0, 93300, 0)
    Sleep(1000)

    FadeIn(2000, 0)
    OP_0D()
    Sleep(1000)

    OP_70(0x000A, 29)
    OP_73(0x000A)
    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    @scena.Lambda('lambda_2FE3')
    def lambda_2FE3():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2FE3)

    Sleep(50)

    @scena.Lambda('lambda_2FF6')
    def lambda_2FF6():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_2FF6)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_300F',
    )

    CreateThread(0x0106, 0x01, 0x01, 0x0006)

    Jump('loc_301D')

    def _loc_300F(): pass

    label('loc_300F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_301D',
    )

    CreateThread(0x0103, 0x01, 0x01, 0x0006)

    def _loc_301D(): pass

    label('loc_301D')

    Sleep(500)

    CreateThread(0x0104, 0x01, 0x01, 0x0007)
    WaitForThreadExit(0x0104, 0x0001)
    OP_72(0x000A, 0x0800)
    OP_6F(0x000A, 29)
    OP_70(0x000A, 0)
    PlaySE(7, 0x00, 0x64)
    OP_73(0x000A)
    OP_71(0x0000, 0x0800)
    Sleep(600)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_309C',
    )

    ChrTalk(
        0x0106,
        (
            '#0050441945V#050F久等了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050441946V……那么，走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_30E0')

    def _loc_309C(): pass

    label('loc_309C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_30E0',
    )

    ChrTalk(
        0x0103,
        (
            '#0030441947V#020F久等了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030441948V……那么走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_30E0(): pass

    label('loc_30E0')

    ChrTalk(
        0x0101,
        (
            '#0010441949V#1002F那到底谁是犯人？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040441950V#031F呵呵，没想到居然是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_3162',
    )

    ChrTalk(
        0x0106,
        (
            '#0050441951V#057F喂，别说啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3192')

    def _loc_3162(): pass

    label('loc_3162')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_3192',
    )

    ChrTalk(
        0x0103,
        (
            '#0030441952V#026F不行哦，奥利维尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3192(): pass

    label('loc_3192')

    ChrTalk(
        0x0101,
        (
            '#0010441953V#1009F啊～为什么嘛。\n',
            '为什么不告诉我？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_3253',
    )

    ChrTalk(
        0x0106,
        (
            '#0050441954V#050F所谓保密义务吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050441955V如果没有正当理由，\n',
            '禁止公开工作内容。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050441956V即使对方是游击士也不行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_32E0')

    def _loc_3253(): pass

    label('loc_3253')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_32E0',
    )

    ChrTalk(
        0x0103,
        (
            '#0030441957V#022F有保密义务吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030441958V如果没有正当理由，\n',
            '公开工作内容是禁止事项哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030441959V即使对方是游击士也不行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_32E0(): pass

    label('loc_32E0')

    ChrTalk(
        0x0101,
        (
            '#0010441960V#1007F呜，是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x00F7, 400)

    ChrTalk(
        0x0105,
        (
            '#0060441961V#042F……好严格的规定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00F7, 0x0105, 400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_33A8',
    )

    ChrTalk(
        0x0106,
        (
            '#0050441962V#050F为了商务上的信誉嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050441963V#552F所以爱说漏嘴的家伙\n',
            '可不适合这工作……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_340B')

    def _loc_33A8(): pass

    label('loc_33A8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_340B',
    )

    ChrTalk(
        0x0103,
        (
            '#0030441964V#027F为了工作上的信誉嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030441965V所以爱说漏嘴的人\n',
            '可不适合这工作……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_340B(): pass

    label('loc_340B')

    ChrTalk(
        0x0104,
        (
            '#0040441966V#033F哎呀，那眼神是什么意思？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040441967V#035F呼，你们真是多心了……\n',
            '我的嘴可不是『漏』哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040441968V只不过是有点『滑』罢了。\n',
            '就像上等的香槟气泡一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010441969V#1019F是是，你就一辈子都这么说吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441970V#1015F唉～唉，不过工作\n',
            '只要坚持都会有结果的。',
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
        'loc_3591',
    )

    ChrTalk(
        0x0106,
        (
            '#0050441971V#053F嗯，不能放弃工作嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050441972V#050F……那么，差不多该走了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_35EB')

    def _loc_3591(): pass

    label('loc_3591')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_35EB',
    )

    ChrTalk(
        0x0103,
        (
            '#0030441973V#020F嗯，放弃工作可不行啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030441974V……那，差不多该走了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_35EB(): pass

    label('loc_35EB')

    EventEnd(0x00)
    OP_4B(0x002F, 255)

    Return()

# id: 0x0006 offset: 0x35F2
@scena.Code('func_06_35F2')
def func_06_35F2():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetPos(0x00FE, 19260, 1200, 94200, 86)

    @scena.Lambda('lambda_3614')
    def lambda_3614():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_3614)

    ChrMoveToRelative(0x00FE, 1500, 0, 0, 1500, 0x00)
    ChrWalkTo(0x00FE, 22520, 0, 94500, 1500, 0x00)
    ChrSetDirection(0x00FE, 90, 400)

    Return()

# id: 0x0007 offset: 0x3650
@scena.Code('func_07_3650')
def func_07_3650():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetPos(0x00FE, 19260, 1200, 93800, 86)

    @scena.Lambda('lambda_3672')
    def lambda_3672():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_3672)

    ChrMoveToRelative(0x00FE, 1500, 0, 0, 1500, 0x00)
    ChrWalkTo(0x00FE, 22200, 0, 93470, 1500, 0x00)
    ChrSetDirection(0x00FE, 90, 400)

    Return()

# id: 0x0008 offset: 0x36AE
@scena.Code('func_08_36AE')
def func_08_36AE():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetPos(0x00FE, 19260, 1200, 94200, 86)

    @scena.Lambda('lambda_36D0')
    def lambda_36D0():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_36D0)

    ChrMoveToRelative(0x00FE, 1500, 0, 0, 1500, 0x00)
    ChrWalkTo(0x00FE, 24000, 0, 94500, 1500, 0x00)
    Sleep(200)

    ChrSetDirection(0x00FE, 270, 400)

    Return()

# id: 0x0009 offset: 0x3711
@scena.Code('func_09_3711')
def func_09_3711():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetPos(0x00FE, 19260, 1200, 93800, 86)

    @scena.Lambda('lambda_3733')
    def lambda_3733():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_3733)

    ChrMoveToRelative(0x00FE, 1500, 0, 0, 1500, 0x00)
    ChrWalkTo(0x00FE, 23700, 0, 93470, 1500, 0x00)
    Sleep(200)

    ChrSetDirection(0x00FE, 270, 400)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
