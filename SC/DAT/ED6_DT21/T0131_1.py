import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T0131_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0131_1 ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T0131.x'
    header.mapIndex       = 7
    header.bgm            = 10
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
    EventBegin(0x00)
    Fade(1000)
    ChrSetPos(0x0101, 38600, 0, 127160, 270)
    ChrSetPos(0x0103, 39970, 0, 126320, 270)
    ChrSetPos(0x00F8, 41010, 0, 126700, 270)
    ChrSetPos(0x00F9, 39700, 0, 127590, 270)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_122',
    )

    ChrSetPos(0x00F9, 41010, 0, 126700, 270)
    ChrSetPos(0x00F8, 39700, 0, 127590, 270)

    def _loc_122(): pass

    label('loc_122')

    ChrSetDirection(0x000B, 90, 0)
    CameraMove(38020, 0, 128180, 0)
    OP_67(0, 6150, -10000, 0)
    CameraSetDistance(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_4A(0x000B, 255)
    OP_0D()

    ChrTalk(
        0x000B,
        (
            '#3550470001V哟，艾丝蒂尔，还有大家！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3550470002V我家的\n',
            '托露塔也醒来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3550470003V这次真是快\n',
            '担心死了，谢谢你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010470004V#1000F#2P哪里，不要在意。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010470005V那也是我们\n',
            '的工作啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030470006V#020F嗯，艾丝蒂尔说的对。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030470007V……那么，还有什么\n',
            '委托吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3550470008V噢，原来是\n',
            '看了那个而来的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3550470009V其实希望你们帮我\n',
            '收集食材。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3550470010V怎么样？\n',
            '有时间做吗？',
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
        'loc_36C',
    )

    Call(1, 0x0002)

    Jump('loc_456')

    def _loc_36C(): pass

    label('loc_36C')

    ChrTalk(
        0x0101,
        (
            '#0010470011V#1015F#2P嗯、对不起。\n',
            '现在不太方便。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3550470012V啊，不行吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3550470013V雾都散去了，\n',
            '你们却还是一样忙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3550470014V算了，等你们有空的时候\n',
            '再来找我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010470015V#1000F#2P嗯，好的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0002, 0, 0x10))
    OP_28(0x0075, 0x01, 0x8000)

    def _loc_456(): pass

    label('loc_456')

    EventEnd(0x00)

    Return()

# id: 0x0001 offset: 0x459
@scena.Code('func_01_459')
def func_01_459():
    EventBegin(0x00)
    Fade(1000)
    ChrSetPos(0x0101, 38600, 0, 127160, 270)
    ChrSetPos(0x0103, 39970, 0, 126320, 270)
    ChrSetPos(0x00F8, 41010, 0, 126700, 270)
    ChrSetPos(0x00F9, 39700, 0, 127590, 270)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4D3',
    )

    ChrSetPos(0x00F9, 41010, 0, 126700, 270)
    ChrSetPos(0x00F8, 39700, 0, 127590, 270)

    def _loc_4D3(): pass

    label('loc_4D3')

    ChrSetDirection(0x000B, 90, 0)
    CameraMove(38020, 0, 128180, 0)
    OP_67(0, 6150, -10000, 0)
    CameraSetDistance(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 0, 0x10)),
            Expr.Return,
        ),
        'loc_54D',
    )

    ChrTalk(
        0x000B,
        (
            '#3550470016V怎么？还是\n',
            '想要接受了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5AE')

    def _loc_54D(): pass

    label('loc_54D')

    ChrTalk(
        0x000B,
        (
            '#3550470017V噢，你们回来得\n',
            '很快啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3550470018V料理的调查和\n',
            '食材的收集，\n',
            '愿意接受吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5AE(): pass

    label('loc_5AE')

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
        'loc_606',
    )

    Call(1, 0x0002)

    Jump('loc_6A0')

    def _loc_606(): pass

    label('loc_606')

    ChrTalk(
        0x0101,
        (
            '#0010470019V#1007F#2P抱歉，还是不太方便呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3550470020V什么，还是不行吗？\n',
            '那可真遗憾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3550470021V算了，等你们有空的时候\n',
            '再来找我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0002, 0, 0x10))

    def _loc_6A0(): pass

    label('loc_6A0')

    EventEnd(0x00)

    Return()

# id: 0x0002 offset: 0x6A3
@scena.Code('func_02_6A3')
def func_02_6A3():
    ChrTalk(
        0x0101,
        (
            '#0010470022V#1006F#2P嗯，ＯＫ了哟。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010470023V那、要调查\n',
            '什么料理呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3550470024V啊，想让你们帮忙调查的\n',
            '是某个炖煮料理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3550470025V『洛连特风味炖煮』\n',
            '好像就是它的俗称。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x14, 0x17, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(100)

    OP_62(0x0103, 0x00000000, 2000, 0x14, 0x17, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7BB',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x14, 0x17, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)

    Jump('loc_7F9')

    def _loc_7BB(): pass

    label('loc_7BB')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7E2',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x14, 0x17, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)

    Jump('loc_7F9')

    def _loc_7E2(): pass

    label('loc_7E2')

    OP_62(0x00F8, 0x00000000, 2000, 0x14, 0x17, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)

    def _loc_7F9(): pass

    label('loc_7F9')

    Sleep(100)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_825',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x14, 0x17, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)

    Jump('loc_863')

    def _loc_825(): pass

    label('loc_825')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_84C',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x14, 0x17, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)

    Jump('loc_863')

    def _loc_84C(): pass

    label('loc_84C')

    OP_62(0x00F9, 0x00000000, 2000, 0x14, 0x17, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)

    def _loc_863(): pass

    label('loc_863')

    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010470026V#1019F#2P洛、洛连特风味炖煮……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010470027V好、好像一听名字\n',
            '就让人不想吃啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030470028V#025F啊啊……\n',
            '确实，一点食欲也引不起来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000B, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x000B,
        (
            '#3550470029V啊、啊、不用太\n',
            '在意名字啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3550470030V总之希望你们\n',
            '帮忙调查这个料理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3550470031V和城里的人打听一下，\n',
            '一定能有线索吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3550470032V以前这可是很\n',
            '有名的料理呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010470033V#1015F#2P那么、对这料理熟悉的人\n',
            '应该都上了年纪吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010470034V既然是古老的料理，\n',
            '年轻人应该都没听过。',
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
        'loc_A9B',
    )

    ChrTalk(
        0x0106,
        (
            '#0050470035V#051F对我们来说\n',
            '是很有用的意见吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B30')

    def _loc_A9B(): pass

    label('loc_A9B')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_ACD',
    )

    ChrTalk(
        0x0104,
        (
            '#0040470036V#035F嗯，确实。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B30')

    def _loc_ACD(): pass

    label('loc_ACD')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B01',
    )

    ChrTalk(
        0x0108,
        (
            '#0080470037V#070F嗯，确实啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B30')

    def _loc_B01(): pass

    label('loc_B01')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B30',
    )

    ChrTalk(
        0x0105,
        (
            '#0060470038V#040F嗯，确实。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B30(): pass

    label('loc_B30')

    ChrTalk(
        0x0103,
        (
            '#0030470039V#026F嗯，调查的目标\n',
            '已经没疑问了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030470040V但有关料理本身，\n',
            '情报还是不够啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010470041V#1007F#2P是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010470042V#1002F有什么线索\n',
            '可以提供吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3550470043V噢，那倒也没什么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3550470044V不过，可以去问问\n',
            '拉欧爷爷。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010470045V#1004F#2P啊……？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010470046V为什么要去问\n',
            '拉欧爷爷呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3550470047V本来不想说的……\n',
            '那位老爷爷啊，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3550470048V好像是在梦中\n',
            '尝到了怀念的料理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3550470049V一直在说要\n',
            '要把它制作出来。',
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
        'loc_D5C',
    )

    ChrTalk(
        0x0107,
        (
            '#0070470050V#560F原、原来是这样。\n',
            '难怪会有这样的委托……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E5D')

    def _loc_D5C(): pass

    label('loc_D5C')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D9B',
    )

    ChrTalk(
        0x0105,
        (
            '#0060470051V#040F原来如此……\n',
            '是那样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E5D')

    def _loc_D9B(): pass

    label('loc_D9B')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_DDA',
    )

    ChrTalk(
        0x0108,
        (
            '#0080470052V#070F原来如此……\n',
            '是那样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E5D')

    def _loc_DDA(): pass

    label('loc_DDA')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E1D',
    )

    ChrTalk(
        0x0104,
        (
            '#0040470053V#030F嗯，原来如此……\n',
            '是那样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E5D')

    def _loc_E1D(): pass

    label('loc_E1D')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E5D',
    )

    ChrTalk(
        0x0106,
        (
            '#0050470054V#050F呼，原来如此……\n',
            '是那样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E5D(): pass

    label('loc_E5D')

    ChrTalk(
        0x0101,
        (
            '#0010470055V#1015F#2P不过，特地\n',
            '为这个来寻求料理……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010470056V那道料理，难道\n',
            '就真的这么美味吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030470057V#020F不一定是味道的缘故，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030470058V也许是因为\n',
            '想起了某些回忆吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3550470059V虽然老爷爷什么都没说，\n',
            '不过看起来一定没错的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3550470060V总之是因为什么原因，\n',
            '所以他无论如何都想再吃到一次。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_100D',
    )

    ChrTalk(
        0x0104,
        (
            '#0040470061V#031F呼～还真是有意思啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040470062V既然如此的话，\n',
            '我也只能慷慨相助了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1118')

    def _loc_100D(): pass

    label('loc_100D')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1066',
    )

    ChrTalk(
        0x0108,
        (
            '#0080470063V#070F嗯，这样的话，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080470064V我们就帮\n',
            '他一下好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1118')

    def _loc_1066(): pass

    label('loc_1066')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_10B8',
    )

    ChrTalk(
        0x0106,
        (
            '#0050470065V#051F喔，是这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050470066V那就帮帮他吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1118')

    def _loc_10B8(): pass

    label('loc_10B8')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1118',
    )

    ChrTalk(
        0x0105,
        (
            '#0060470067V#040F是这样吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060470068V那我们要是能帮上忙的话\n',
            '也不错啊…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1118(): pass

    label('loc_1118')

    ChrSetDirection(0x0101, 90, 400)

    ChrTalk(
        0x0101,
        (
            '#0010470069V#1006F#2P嗯、拉欧爷爷\n',
            '也终于醒来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010470070V为了庆祝，一定想\n',
            '好好吃一顿吧。',
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
        'loc_11B5',
    )

    ChrTalk(
        0x0107,
        (
            '#0070470071V#061F嘿嘿……是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_11B5(): pass

    label('loc_11B5')

    ChrSetDirection(0x0101, 270, 400)

    ChrTalk(
        0x0103,
        (
            '#0030470072V#020F那么、料理的事情\n',
            '就去问拉欧爷爷吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030470073V……有关工作，\n',
            '还有什么别的注意事项吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3550470074V啊啊～料理的事情\n',
            '要想办法，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3550470075V还有，需要的食材\n',
            '最好也一起带来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3550470076V也许要用到什么\n',
            '特殊的配料也说不定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010470077V#1000F#2P嗯，明白。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010470078V那么、报告的时候\n',
            '我们会把食材也带来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3550470079V啊啊，那就拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3550470080V嗯，究竟是怎样的料理呢，\n',
            '还真让人好奇。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030470081V#020F为了不辜负你的期待，\n',
            '我们这就加油调查了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010470082V#1006F#2P期待我们的报告吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3550470083V啊啊，拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0002, 4, 0x14))
    OP_28(0x0075, 0x04, 0x04)
    OP_28(0x0075, 0x04, 0x08)
    OP_28(0x0075, 0x01, 0x0001)
    OP_28(0x0075, 0x01, 0x0002)
    OP_28(0x0075, 0x01, 0x0004)

    Return()

# id: 0x0003 offset: 0x1426
@scena.Code('func_03_1426')
def func_03_1426():
    EventBegin(0x00)
    ChrSetDirection(0x0011, 270, 0)
    Fade(1000)
    ChrSetPos(0x0101, 38190, 0, 75500, 270)
    ChrSetPos(0x0103, 38230, 0, 74290, 294)
    ChrSetPos(0x00F8, 39580, 0, 75500, 270)
    ChrSetPos(0x00F9, 39000, 0, 74690, 270)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_14A7',
    )

    ChrSetPos(0x00F9, 39580, 0, 75500, 270)
    ChrSetPos(0x00F8, 39000, 0, 74690, 270)

    def _loc_14A7(): pass

    label('loc_14A7')

    CameraMove(37010, 0, 76590, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_0D()

    ChrTalk(
        0x0011,
        (
            '#3560470084V#1P嗯……料理还是不行吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3560470085V#1P毕竟是很久前的料理，\n',
            '太辛苦厨师了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010470086V#1000F#2P拉欧爷爷，您有空吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0011, 0x0101, 400)
    OP_62(0x0011, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTalk(
        0x0011,
        (
            '#3560470087V#1P噢噢，我还说是谁，\n',
            '这不是卡西乌斯的丫头吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3560470088V#1P怎么，找我\n',
            '有什么事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010470089V#1015F#2P嗯，想打听一下\n',
            '料理的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3560470090V#1P喔？料理？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3560470091V#1P是说我梦见的那种\n',
            '炖煮料理吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030470092V#020F嗯，就是那个料理的事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030470093V其实是受到了德瑟鲁先生的委托……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '他委托我们\n',
            '调查料理的配料。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    ChrTurnDirection(0x0011, 0x0103, 400)

    ChrTalk(
        0x0011,
        (
            '#3560470094V#1P啊啊～那你们\n',
            '就来找我了解情况吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3560470095V#1P呵呵，这小子\n',
            '找到了强力的支援啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3560470096V#1P拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010470097V#1008F#2P那、谢谢您了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010470098V#1006F不过想完成委托还\n',
            '需要拉欧爷爷的协助啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030470099V#020F有关那个料理，\n',
            '希望您能详细介绍一下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030470100V比如材料、味道、\n',
            '在哪里吃过的…之类的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3560470101V#1P原来如此，说的有道理……\n',
            '那么我这就开始说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0011, 0x0101, 400)

    ChrTalk(
        0x0011,
        (
            '#3560470102V#1P首先，如你们所知，\n',
            '这是炖煮的料理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3560470103V#1P不过基本的风味\n',
            '应该是黑胡椒口味才对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3560470104V#1P那种香气令人食指大动，\n',
            '吃下去的感觉很痛快。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010470105V#1015F#2P嗯……\n',
            '黑胡椒的炖煮……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010470106V#1011F啊……请您继续说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3560470107V#1P嗯，主材是肉……\n',
            '还有鱼肉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3560470108V#1P我比较喜欢肉，\n',
            '就先说肉吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3560470109V#1P带着骨头的肉，\n',
            '实在是很美味呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0011, 180, 400)

    ChrTalk(
        0x0011,
        (
            '#3560470110V#1P另外还有一些\n',
            '特殊香草…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0011, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1000)

    OP_63(0x0011)

    ChrTalk(
        0x0011,
        (
            '#3560470111V#1P不过很遗憾，\n',
            '具体是什么已经忘了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3560470112V#1P只是记得很香，\n',
            '但不知道是什么。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3560470113V#1P嗯，就这些了吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010470114V#1015F#2P嗯，\n',
            '肉骨头……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010470115V还有香草…\n',
            '种类未知…',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010470116V#1000F……大概就这些了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030470117V#020F还算挺具体了。',
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
        'loc_1C31',
    )

    ChrTalk(
        0x0106,
        (
            '#0050470118V#051F啊啊～有这些情报\n',
            '就可以开始了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1CF9')

    def _loc_1C31(): pass

    label('loc_1C31')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1C72',
    )

    ChrTalk(
        0x0108,
        (
            '#0080470119V#070F嗯，这下子\n',
            '情报算是够了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1CF9')

    def _loc_1C72(): pass

    label('loc_1C72')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1CB5',
    )

    ChrTalk(
        0x0104,
        (
            '#0040470120V#030F嗯，得到这些情报\n',
            '就足够了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1CF9')

    def _loc_1CB5(): pass

    label('loc_1CB5')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1CF9',
    )

    ChrTalk(
        0x0105,
        (
            '#0060470121V#040F嗯，得到这些材料以后\n',
            '再回来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1CF9(): pass

    label('loc_1CF9')

    ChrSetDirection(0x0011, 90, 400)

    ChrTalk(
        0x0011,
        (
            '#3560470122V#1P嗯，对你们有点帮助吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010470123V#1006F#2P当然，\n',
            '谢谢您啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3560470124V#1P那么，调查就拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3560470125V#1P想想要是能再看到那料理\n',
            '一定会很开心的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0002, 1, 0x11))
    OP_28(0x0075, 0x01, 0x0008)
    EventEnd(0x00)

    Return()

# id: 0x0004 offset: 0x1DC8
@scena.Code('func_04_1DC8')
def func_04_1DC8():
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#3670470191V艾丝蒂尔也要找时间\n',
            '再来店里玩吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3670470192V我和伊莉莎一起\n',
            '期待你们回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010470193V#1001F嗯，以后\n',
            '要再来玩啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010470194V#1011F啊，说起来的话……\n',
            '托露塔阿姨。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010470195V其实我们是接受德瑟鲁大叔的委托\n',
            '来调查一些事情……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '诉说了在寻找拉欧爷爷\n',
            '所说的炖煮料理食谱的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x0008,
        (
            '#3670470196V啊，是料理的事吧。\n',
            '我听说了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030470197V#027F啊、那么……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030470198V……托露塔阿姨也\n',
            '应该知道的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0103, 400)

    ChrTalk(
        0x0008,
        (
            '#3670470199V嗯，真遗憾啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3670470200V在我开始学烹饪的时候，\n',
            '就已经没人做那道菜了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x0075, 0x01, 0x0800)"),
            Expr.Return,
        ),
        'loc_20B6',
    )

    ChrTurnDirection(0x0103, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030470144V#020F总之\n',
            '先去报告那个食谱吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010470145V#1015F嗯，只有先这样了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#3670470203V老公也很困扰，\n',
            '怎么也要帮帮他啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_22BC')

    def _loc_20B6(): pass

    label('loc_20B6')

    If(
        (
            (Expr.Eval, "OP_29(0x0075, 0x01, 0x0400)"),
            Expr.Return,
        ),
        'loc_216E',
    )

    ChrTurnDirection(0x0103, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030470146V#020F看来还是得\n',
            '调查雷特拉先生家了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010470147V#1015F嗯……或许是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#3670470203V老公他也很困扰，\n',
            '怎么也要帮帮他啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_22BC')

    def _loc_216E(): pass

    label('loc_216E')

    ChrTalk(
        0x0101,
        (
            '#0010470207V#1025F啊、那个……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010470208V#1015F嗯、人一上了年纪\n',
            '果然就是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030470209V#020F嗯，那样就好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030470210V……那么，\n',
            '继续调查吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010211196V#1000F啊、嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010470212V托露塔阿姨，\n',
            '谢谢您的合作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#3670470213V要道谢的是我才对，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3670470214V老公他也很困扰，\n',
            '调查到什么了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_22BC(): pass

    label('loc_22BC')

    SetScenaFlags(ScenaFlag(0x0002, 2, 0x12))
    OP_28(0x0075, 0x01, 0x0080)

    Return()

# id: 0x0005 offset: 0x22C6
@scena.Code('func_05_22C6')
def func_05_22C6():
    EventBegin(0x00)
    Fade(1000)
    ChrSetPos(0x0101, 38600, 0, 127160, 270)
    ChrSetPos(0x0103, 39970, 0, 126320, 270)
    ChrSetPos(0x00F8, 41010, 0, 126700, 270)
    ChrSetPos(0x00F9, 39700, 0, 127590, 270)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2340',
    )

    ChrSetPos(0x00F9, 41010, 0, 126700, 270)
    ChrSetPos(0x00F8, 39700, 0, 127590, 270)

    def _loc_2340(): pass

    label('loc_2340')

    ChrSetDirection(0x000B, 90, 0)
    CameraMove(38020, 0, 128180, 0)
    OP_67(0, 6150, -10000, 0)
    CameraSetDistance(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_4A(0x000B, 255)
    OP_0D()

    ChrTalk(
        0x000B,
        (
            '#3550470367V哟、艾丝蒂尔。\n',
            '调查进行得如何了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010470368V#1001F#2P嗯，大概\n',
            '知道配料了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000B, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000B,
        (
            '#3550470369V噢，已经找到了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3550470370V呀，工作完成得好早啊。\n',
            '游击士果然了不起。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010470371V#1015F#2P嗯、不过\n',
            '还不能高兴太早。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3550470372V哦？怎么回事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030470373V#020F嗯，其实……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '将找到的食谱已做了改动的事情\n',
            '做了说明。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x000B,
        (
            '#3550470374V原来如此…是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3550470375V但是，也未必就是坏事，\n',
            '就用那配料试试看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010470376V#1007F#2P抱歉啊，德瑟鲁大叔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010470377V要是能找到原始版\n',
            '的话自然最好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3550470378V哪里！基本部分并\n',
            '没有变化，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3550470379V再加上我的技术和经验，\n',
            '一定可以成功的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030470380V#021F呵呵，很有自信啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_26B3',
    )

    ChrTalk(
        0x0104,
        (
            '#0040470381V#031F不愧是职业厨师啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2767')

    def _loc_26B3(): pass

    label('loc_26B3')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_26ED',
    )

    ChrTalk(
        0x0105,
        (
            '#0060470382V#040F不愧是专业厨师啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2767')

    def _loc_26ED(): pass

    label('loc_26ED')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_272F',
    )

    ChrTalk(
        0x0108,
        (
            '#0080470383V#070F嗯，专业的就是不同凡响啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2767')

    def _loc_272F(): pass

    label('loc_272F')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2767',
    )

    ChrTalk(
        0x0107,
        (
            '#0070470384V#061F果然……\n',
            '名不虚传。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2767(): pass

    label('loc_2767')

    ChrTalk(
        0x0101,
        (
            '#0010470385V#1006F#2P那么，赶快\n',
            '将调查结果告诉您吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '报告了布露姆老奶奶的食谱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x000B,
        (
            '#3550470386V嗯嗯……\n',
            '原来如此。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3550470387V大致上和我想的一样。\n',
            '材料很让人意外呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3550470388V嗯，那么就努力\n',
            '试着制作吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010470389V#1011F#2P这也就是说，\n',
            '委托结束了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3550470390V噢、还没有……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3550470391V……之前说过吧，\n',
            '食材的收集也想拜托你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030470392V#020F嗯，确实说过呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030470393V#027F……已经准备完了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010470394V#1015F#2P啊，等一下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_40(0x0388, 0x00)"),
            (Expr.PushLong, 0x1),
            Expr.Geq,
            (Expr.Eval, "OP_40(0x0389, 0x00)"),
            (Expr.PushLong, 0x1),
            Expr.Geq,
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x0396, 0x00)"),
            (Expr.PushLong, 0x2),
            Expr.Geq,
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x0397, 0x00)"),
            (Expr.PushLong, 0x5),
            Expr.Geq,
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x0399, 0x00)"),
            (Expr.PushLong, 0x5),
            Expr.Geq,
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x039A, 0x00)"),
            (Expr.PushLong, 0x2),
            Expr.Geq,
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x039C, 0x00)"),
            (Expr.PushLong, 0x4),
            Expr.Geq,
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x03A1, 0x00)"),
            (Expr.PushLong, 0x2),
            Expr.Geq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_29DF',
    )

    SetScenaFlags(ScenaFlag(0x0002, 5, 0x15))

    def _loc_29DF(): pass

    label('loc_29DF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 5, 0x15)),
            Expr.Return,
        ),
        'loc_2A26',
    )

    ChrTurnDirection(0x0101, 0x000B, 400)

    ChrTalk(
        0x0101,
        (
            '#0010470395V#1006F#2P嗯……\n',
            '全部收集全了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(1, 0x0007)

    Jump('loc_2B69')

    def _loc_2A26(): pass

    label('loc_2A26')

    OP_62(0x0101, 0x00000000, 2000, 0x0E, 0x0F, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    OP_63(0x0101)
    ChrTurnDirection(0x0101, 0x000B, 400)

    ChrTalk(
        0x0101,
        (
            '#0010470396V#1007F#2P对、对不起，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010470397V料理需要的食材\n',
            '还没有收集全。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3550470398V啊，没关系。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3550470399V收集完以后\n',
            '再来找我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010470400V#1003F#2P嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030470401V#022F真是的……\n',
            '认真确认一下啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010470402V#1007F#2P……真、真丢人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0075, 0x01, 0x4000)

    def _loc_2B69(): pass

    label('loc_2B69')

    EventEnd(0x00)

    Return()

# id: 0x0006 offset: 0x2B6C
@scena.Code('func_06_2B6C')
def func_06_2B6C():
    EventBegin(0x00)
    Fade(1000)
    ChrSetPos(0x0101, 38600, 0, 127160, 270)
    ChrSetPos(0x0103, 39970, 0, 126320, 270)
    ChrSetPos(0x00F8, 41010, 0, 126700, 270)
    ChrSetPos(0x00F9, 39700, 0, 127590, 270)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2BE6',
    )

    ChrSetPos(0x00F9, 41010, 0, 126700, 270)
    ChrSetPos(0x00F8, 39700, 0, 127590, 270)

    def _loc_2BE6(): pass

    label('loc_2BE6')

    ChrSetDirection(0x000B, 90, 0)
    CameraMove(38020, 0, 128180, 0)
    OP_67(0, 6150, -10000, 0)
    CameraSetDistance(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_4A(0x000B, 255)
    OP_0D()

    ChrTalk(
        0x000B,
        (
            '#3550470403V噢，已经收集完毕了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_40(0x0388, 0x00)"),
            (Expr.PushLong, 0x1),
            Expr.Geq,
            (Expr.Eval, "OP_40(0x0389, 0x00)"),
            (Expr.PushLong, 0x1),
            Expr.Geq,
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x0396, 0x00)"),
            (Expr.PushLong, 0x2),
            Expr.Geq,
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x0397, 0x00)"),
            (Expr.PushLong, 0x5),
            Expr.Geq,
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x0399, 0x00)"),
            (Expr.PushLong, 0x5),
            Expr.Geq,
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x039A, 0x00)"),
            (Expr.PushLong, 0x2),
            Expr.Geq,
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x039C, 0x00)"),
            (Expr.PushLong, 0x4),
            Expr.Geq,
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x03A1, 0x00)"),
            (Expr.PushLong, 0x2),
            Expr.Geq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2CBD',
    )

    SetScenaFlags(ScenaFlag(0x0002, 5, 0x15))

    def _loc_2CBD(): pass

    label('loc_2CBD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 5, 0x15)),
            Expr.Return,
        ),
        'loc_2CF9',
    )

    ChrTalk(
        0x0101,
        (
            '#0010470404V#1006F#2P嗯！\n',
            '全部收集到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(1, 0x0007)

    Jump('loc_2D6E')

    def _loc_2CF9(): pass

    label('loc_2CF9')

    ChrTalk(
        0x0101,
        (
            '#0010470405V#1008F#2P啊、抱歉。\n',
            '还没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3550470406V啊，辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3550470407V很好，\n',
            '终于收集全了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2D6E(): pass

    label('loc_2D6E')

    EventEnd(0x00)

    Return()

# id: 0x0007 offset: 0x2D71
@scena.Code('func_07_2D71')
def func_07_2D71():
    EventBegin(0x00)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.Item, ItemTable['十年豆酱']),
            (TxtCtl.SetColor, 0x0),
            '×１\n',
            (TxtCtl.Item, ItemTable['百年古酒']),
            (TxtCtl.SetColor, 0x0),
            '×１\n',
            (TxtCtl.Item, ItemTable['枫糖']),
            (TxtCtl.SetColor, 0x0),
            '×２\n',
            (TxtCtl.Item, ItemTable['粗碎岩盐']),
            (TxtCtl.SetColor, 0x0),
            '×５\n',
            (TxtCtl.Item, ItemTable['清新香草']),
            (TxtCtl.SetColor, 0x0),
            '×５\n',
            (TxtCtl.Item, ItemTable['巨龙咖啡豆']),
            (TxtCtl.SetColor, 0x0),
            '×２\n',
            (TxtCtl.Item, ItemTable['黑胡椒']),
            (TxtCtl.SetColor, 0x0),
            '×４\n',
            (TxtCtl.Item, ItemTable['魔兽之骨']),
            (TxtCtl.SetColor, 0x0),
            '×２\n',
            (TxtCtl.SetColor, 0x0),
            '……将以上的食材交了出去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    RemoveItem(ItemTable['十年豆酱'], 1)
    RemoveItem(ItemTable['百年古酒'], 1)
    RemoveItem(ItemTable['枫糖'], 2)
    RemoveItem(ItemTable['粗碎岩盐'], 5)
    RemoveItem(ItemTable['清新香草'], 5)
    RemoveItem(ItemTable['巨龙咖啡豆'], 2)
    RemoveItem(ItemTable['黑胡椒'], 4)
    RemoveItem(ItemTable['魔兽之骨'], 2)

    ChrTalk(
        0x000B,
        (
            '#3550470408V嗯，辛苦啦。\n',
            '这样就准备完毕了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3550470409V能做出爷爷\n',
            '想要的料理吗……\n',
            '接下来就要看我的手艺了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3550470410V好！！拿出干劲\n',
            '试试看吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    ChrWalkTo(0x000B, 36640, 0, 126580, 2000, 0x00)
    ChrWalkTo(0x000B, 36640, 0, 125140, 2000, 0x00)
    ChrSetDirection(0x000B, 270, 400)
    OP_0D()
    PlaySE(19, 0x00, 0x64)
    PlaySE(202, 0x00, 0x64)
    ChrSetSubChip(0x0013, 6)
    ChrClearFlags(0x0013, 0x0080)
    ChrSetPos(0x0011, 36530, 0, 74730, 180)
    OP_4A(0x0011, 255)
    ChrSetPos(0x0101, 36500, 0, 73200, 0)
    ChrSetPos(0x0103, 37870, 0, 73310, 315)
    ChrSetPos(0x00F8, 37500, 0, 72090, 0)
    ChrSetPos(0x00F9, 36500, 0, 71860, 0)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2FB1',
    )

    ChrSetPos(0x00F9, 37500, 0, 72090, 0)
    ChrSetPos(0x00F8, 36500, 0, 71860, 0)

    def _loc_2FB1(): pass

    label('loc_2FB1')

    ChrSetPos(0x000B, 33950, 0, 75000, 90)
    OP_4A(0x000B, 255)
    ChrSetPos(0x000A, 33590, 0, 75990, 120)
    OP_4A(0x000C, 255)
    ChrSetPos(0x000C, 33500, 0, 76920, 120)
    OP_4A(0x000A, 255)
    ChrSetPos(0x0012, 45380, 0, 70160, 300)
    Sleep(5000)

    CameraMove(24580, 0, 77920, 0)
    OP_67(0, 5980, -10000, 0)
    CameraSetDistance(2950, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)

    @scena.Lambda('lambda_3049')
    def lambda_3049():
        CameraMove(34820, 0, 74740, 4000)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_3049)

    FadeIn(1000, 0)
    OP_0D()
    WaitForThreadExit(0x0011, 0x0001)

    ChrTalk(
        0x0011,
        (
            '#3560470411V#2P…………这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3560470412V#2P是吗，原始的食谱\n',
            '已经找不到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010470413V#1003F#1P……嗯，很遗憾，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010470414V虽然问过了\n',
            '很多人…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030470415V#026F#4P但还是\n',
            '没有结果呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3560470416V#2P哪里的话，\n',
            '所谓的原始版也只是我的说法，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3560470417V#2P你们没必要\n',
            '放在心上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3560470418V#2P呼，只是一想到\n',
            '再也尝不到那种味道，\n',
            '总还是很失望啊…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3550470419V喂！爷爷！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3550470420V灰心的话，\n',
            '现在太早了吧？！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0011, 0x000B, 400)

    ChrTalk(
        0x0011,
        (
            '#3560470421V#2P喔……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3260')
    def lambda_3260():
        ChrTurnDirection(0x00F6, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x00F6, 0x0001, lambda_3260)

    Sleep(100)

    @scena.Lambda('lambda_3273')
    def lambda_3273():
        ChrSetDirection(0x00F7, 270, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_3273)

    @scena.Lambda('lambda_3281')
    def lambda_3281():
        ChrTurnDirection(0x00F8, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_3281)

    Sleep(100)

    @scena.Lambda('lambda_3294')
    def lambda_3294():
        ChrTurnDirection(0x00F9, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_3294)

    ChrTalk(
        0x000B,
        (
            '#3550470422V我做的料理应该\n',
            '不会相差太多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3550470423V艾丝蒂尔他们辛苦找到的食谱，\n',
            '味道不会让您失望。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3380470424V说的对，再唠叨个没完，\n',
            '菜就该凉了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3347')
    def lambda_3347():
        ChrSetDirection(0x0101, 0, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3347)

    Sleep(100)

    @scena.Lambda('lambda_335A')
    def lambda_335A():
        ChrSetDirection(0x00F7, 315, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_335A)

    @scena.Lambda('lambda_3368')
    def lambda_3368():
        ChrSetDirection(0x00F8, 0, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_3368)

    Sleep(100)

    @scena.Lambda('lambda_337B')
    def lambda_337B():
        ChrSetDirection(0x00F9, 0, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_337B)

    ChrTurnDirection(0x0011, 0x000B, 400)

    ChrTalk(
        0x0101,
        (
            '#0010470425V#1016F哈哈，是啊，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010470426V好不容易做出的料理，\n',
            '还是趁热吃了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030470427V#025F真是的，光顾说别的，\n',
            '把正事都忘了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030470428V刚才就觉得味道很好闻，\n',
            '早就忍耐不住了。',
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
        'loc_3491',
    )

    ChrTalk(
        0x0107,
        (
            '#0070470429V#067F嘿嘿、总感觉\n',
            '肚子饿了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3650')

    def _loc_3491(): pass

    label('loc_3491')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3535',
    )

    ChrTalk(
        0x0106,
        (
            '#0050470430V#551F啊啊～味道\n',
            '确实很好闻呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050470431V#550F可恶……\n',
            '为什么肚子忽然饿了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0106, 400)

    ChrTalk(
        0x0101,
        (
            '#0010470432V#1019F生、生什么气嘛……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3650')

    def _loc_3535(): pass

    label('loc_3535')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_35AE',
    )

    ChrTalk(
        0x0108,
        (
            '#0080470433V#071F哈哈，忽然\n',
            '感觉肚子饿了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0108, 400)

    ChrTalk(
        0x0101,
        (
            '#0010470434V#1007F金、金先生\n',
            '也饿了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3650')

    def _loc_35AE(): pass

    label('loc_35AE')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3650',
    )

    ChrTalk(
        0x0104,
        (
            '#0040470435V#031F嗯～确实很能\n',
            '勾起食欲啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040470436V#037F如果能有\n',
            '原来的味道就好了…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0104, 400)

    ChrTalk(
        0x0101,
        (
            '#0010470437V#1007F嗯、马上就要\n',
            '试吃了啊…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3650(): pass

    label('loc_3650')

    ChrTurnDirection(0x0011, 0x0101, 400)

    ChrTalk(
        0x0011,
        (
            '#3560470438V#2P啊，真是的，\n',
            '马上就要有结果了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3560470439V#2P那么，我就不客气\n',
            '开动了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0011, 270, 400)

    @scena.Lambda('lambda_36C8')
    def lambda_36C8():
        CameraMove(34820, 0, 74740, 1500)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_36C8)

    @scena.Lambda('lambda_36E0')
    def lambda_36E0():
        ChrTurnDirection(0x00F6, 0x0011, 400)

        ExitThread()

    DispatchAsync(0x00F6, 0x0001, lambda_36E0)

    Sleep(100)

    @scena.Lambda('lambda_36F3')
    def lambda_36F3():
        ChrTurnDirection(0x00F7, 0x0011, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_36F3)

    @scena.Lambda('lambda_3701')
    def lambda_3701():
        ChrTurnDirection(0x00F8, 0x0011, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_3701)

    Sleep(100)

    @scena.Lambda('lambda_3714')
    def lambda_3714():
        ChrTurnDirection(0x00F9, 0x0011, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_3714)

    Sleep(1000)

    ChrTalk(
        0x0011,
        (
            '#3560470440V#2P呵………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3560470441V#2P嗯…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010470442V#1002F#1P（咕噜……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3550470443V#1P（……真、真紧张啊。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0011, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1000)

    OP_63(0x0011)
    OP_62(0x0011, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0011,
        (
            '#3560470444V#2P嗯……………………\n',
            '………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3560470445V#2P……这、这味道？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010470446V#1002F#1P怎、怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0011, 180, 400)

    ChrTalk(
        0x0011,
        (
            '#3560470447V#2P这、这……\n',
            '就是这个啊！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3560470448V#3S#2P这就是我做梦都想吃\n',
            '的炖煮料理啊！！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    OP_62(0x000C, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x000B, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(100)

    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0103, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(100)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_399D',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_39DB')

    def _loc_399D(): pass

    label('loc_399D')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_39C4',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_39DB')

    def _loc_39C4(): pass

    label('loc_39C4')

    OP_62(0x00F8, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_39DB(): pass

    label('loc_39DB')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3A02',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_3A40')

    def _loc_3A02(): pass

    label('loc_3A02')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3A29',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_3A40')

    def _loc_3A29(): pass

    label('loc_3A29')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_3A40(): pass

    label('loc_3A40')

    ChrTalk(
        0x0103,
        (
            '#0030400459V#023F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3380470450V哎哎哎！？',
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
        'loc_3AA7',
    )

    ChrTalk(
        0x0108,
        (
            '#0080470451V#073F喔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3B32')

    def _loc_3AA7(): pass

    label('loc_3AA7')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3AD9',
    )

    ChrTalk(
        0x0106,
        (
            '#0050360315V#052F真的吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3B32')

    def _loc_3AD9(): pass

    label('loc_3AD9')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3B07',
    )

    ChrTalk(
        0x0105,
        (
            '#0060470453V#044F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3B32')

    def _loc_3B07(): pass

    label('loc_3B07')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3B32',
    )

    ChrTalk(
        0x0104,
        (
            '#0040390897V#033F这……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3B32(): pass

    label('loc_3B32')

    ChrTalk(
        0x000C,
        (
            '#3590470455V真、真的吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0011, 0x000C, 400)

    ChrTalk(
        0x0011,
        (
            '#3560470456V#2P嗯、嗯，当然是真的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3560470457V#2P如此怀念的味道\n',
            '怎么可能记错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3560470458V#2P我吃过的料理\n',
            '就是这个！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x000B, 400)

    ChrTalk(
        0x0101,
        (
            '#0010470459V#1001F德瑟鲁大叔！好棒啊！！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010470460V梦中出现的料理\n',
            '也能做的出来!',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3550470461V嗯、嗯…\n',
            '确实让我信心大增呢，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3550470462V不过说实话，这会不会太巧了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0011, 0x000B, 400)

    ChrTalk(
        0x0011,
        (
            '#3560470463V#2P啊、不用谦虚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0011, 400)

    ChrTalk(
        0x0011,
        (
            '#3560470464V#2P料理做得很完美，\n',
            '正是我想要的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0011, 0, 400)
    OP_62(0x0011, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1000)

    OP_63(0x0011)

    ChrTalk(
        0x0011,
        (
            '#3560470465V#2P呼～吃过后让我想起了过去的事情……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3560470466V#2P已经久远模糊的青春……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3560470467V#2P我曾经深爱的那个女孩子\n',
            '非常擅长制作这道菜，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3560470468V#2P她嫁人的时候\n',
            '我一个人默默地躲起来哭泣…',
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
            '#0010470469V#1016F#1P好、好悲伤\n',
            '的青春啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#3590470470V嘿～第一次听说呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#3590470471V爷爷年轻的时候\n',
            '也是性情中人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030470472V#021F呵呵，年轻人的特权啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0011, 180, 400)

    ChrTalk(
        0x0011,
        (
            '#3560470473V#2P年轻人的特权吗……\n',
            '正是如此呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3560470474V#2P现在一切\n',
            '都已经变了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3560470475V#2P天使一样的姑娘\n',
            '如今也变成了满脸皱纹的老太婆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(1000)

    ChrClearFlags(0x0012, 0x0080)
    OP_4A(0x0012, 255)
    ChrSetPos(0x0012, 44480, 0, 71450, 270)

    NpcTalk(
        0x0012,
        '老婆婆的声音',
        (
            '#3570470476V#5P……你说谁是满脸皱纹的老太婆啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3FE0')
    def lambda_3FE0():
        ChrTurnDirection(0x00FE, 0x0012, 400)
        Yield()

        Jump('lambda_3FE0')

    DispatchAsync2(0x0101, 0x0003, lambda_3FE0)

    @scena.Lambda('lambda_3FF1')
    def lambda_3FF1():
        ChrTurnDirection(0x00FE, 0x0012, 400)
        Yield()

        Jump('lambda_3FF1')

    DispatchAsync2(0x0103, 0x0003, lambda_3FF1)

    @scena.Lambda('lambda_4002')
    def lambda_4002():
        ChrTurnDirection(0x00FE, 0x0012, 400)
        Yield()

        Jump('lambda_4002')

    DispatchAsync2(0x00F8, 0x0003, lambda_4002)

    @scena.Lambda('lambda_4013')
    def lambda_4013():
        ChrTurnDirection(0x00FE, 0x0012, 400)
        Yield()

        Jump('lambda_4013')

    DispatchAsync2(0x00F9, 0x0003, lambda_4013)

    @scena.Lambda('lambda_4024')
    def lambda_4024():
        ChrTurnDirection(0x00FE, 0x0012, 400)
        Yield()

        Jump('lambda_4024')

    DispatchAsync2(0x000B, 0x0003, lambda_4024)

    @scena.Lambda('lambda_4035')
    def lambda_4035():
        ChrTurnDirection(0x00FE, 0x0012, 400)
        Yield()

        Jump('lambda_4035')

    DispatchAsync2(0x000C, 0x0003, lambda_4035)

    @scena.Lambda('lambda_4046')
    def lambda_4046():
        ChrTurnDirection(0x00FE, 0x0012, 400)
        Yield()

        Jump('lambda_4046')

    DispatchAsync2(0x000A, 0x0003, lambda_4046)

    ChrSetDirection(0x0011, 90, 400)
    OP_62(0x0011, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    OP_63(0x0011)

    ChrTalk(
        0x0011,
        (
            '#3560470477V#2P那、那声音是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CameraMove(40740, 0, 75420, 3000)
    Sleep(1000)

    @scena.Lambda('lambda_40B8')
    def lambda_40B8():
        CameraMove(35940, 0, 74450, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_40B8)

    ChrWalkTo(0x0012, 40410, 0, 74580, 2000, 0x00)
    ChrWalkTo(0x0012, 38440, 0, 74740, 2000, 0x00)
    TerminateThread(0x0101, 0x03)
    TerminateThread(0x0103, 0x03)
    TerminateThread(0x00F8, 0x03)
    TerminateThread(0x00F9, 0x03)
    TerminateThread(0x000B, 0x03)
    TerminateThread(0x000C, 0x03)
    TerminateThread(0x000A, 0x03)

    ChrTalk(
        0x000B,
        (
            '#3550470478V布露姆老奶奶……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#3570470479V竟然在这么多人面前\n',
            '说别人的坏话！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#3570470480V你还是和以前一样，\n',
            '一点都没变。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0011, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    OP_63(0x0011)

    ChrTalk(
        0x0011,
        (
            '#3560470481V#2P啊、啊、那\n',
            '只是随口一说…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3550470482V怎么了？婆婆，\n',
            '您难得来这里啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3380470483V#2P嗯，好久不见啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#3570470484V刚才这些孩子\n',
            '来我家问食谱，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#3570470485V因为有点在意，\n',
            '就过来看看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000B, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    OP_63(0x000B)

    ChrTalk(
        0x000B,
        (
            '#3550470486V啊？那食谱是？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#3570470487V嗯，是我家的家传食谱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#3570470488V在我年轻的时候，\n',
            '是我最擅长的一道料理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#3570470489V当时也经常做给\n',
            '这老家伙吃呢。',
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
            '#0010470490V#1004F这、这么说的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3380470491V#2P爷、爷爷年轻时喜欢\n',
            '的那个女孩，就是…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_43E0')
    def lambda_43E0():
        ChrTurnDirection(0x00FE, 0x0011, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_43E0)

    Sleep(150)

    @scena.Lambda('lambda_43F3')
    def lambda_43F3():
        ChrTurnDirection(0x00FE, 0x0011, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0003, lambda_43F3)

    @scena.Lambda('lambda_4401')
    def lambda_4401():
        ChrTurnDirection(0x00FE, 0x0011, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_4401)

    Sleep(150)

    @scena.Lambda('lambda_4414')
    def lambda_4414():
        ChrTurnDirection(0x00FE, 0x0011, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0003, lambda_4414)

    @scena.Lambda('lambda_4422')
    def lambda_4422():
        ChrTurnDirection(0x00FE, 0x0011, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0003, lambda_4422)

    Sleep(1000)

    OP_62(0x0011, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0011,
        (
            '#3560470492V#2P嗯，啊啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3560470493V#2P呼～岁月的流逝\n',
            '真是残酷啊…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_44A2')
    def lambda_44A2():
        ChrTurnDirection(0x00FE, 0x0012, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_44A2)

    @scena.Lambda('lambda_44B0')
    def lambda_44B0():
        ChrTurnDirection(0x00FE, 0x0012, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0003, lambda_44B0)

    @scena.Lambda('lambda_44BE')
    def lambda_44BE():
        ChrTurnDirection(0x00FE, 0x0012, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0003, lambda_44BE)

    @scena.Lambda('lambda_44CC')
    def lambda_44CC():
        ChrTurnDirection(0x00FE, 0x0012, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0003, lambda_44CC)

    Sleep(1000)

    ChrTurnDirection(0x0012, 0x0101, 400)

    ChrTalk(
        0x0012,
        (
            '#3570470494V啊？怎么啦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010470495V#1016F嗯、也没什么啦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0012, 0x0011, 400)

    ChrTalk(
        0x0012,
        (
            '#3570470496V算啦，不管怎样，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#3570470497V再次回忆到这料理\n',
            '真是很高兴。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#3570470498V嗯，难得过来一趟，\n',
            '好久没做料理了，就试着再做一次吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#3570470499V你们也想见识一下\n',
            '正宗风味吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010470500V#1018F啊～当然⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3550470501V非常期待啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3550470502V我也想学习一下\n',
            '正宗的烹饪方法呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#3570470503V那么，厨房借用一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    OP_28(0x0075, 0x01, 0x1000)
    OP_28(0x0075, 0x04, 0x10)
    Sleep(1000)

    If(
        (
            (Expr.Eval, "OP_40(0x020D, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_46FA',
    )

    If(
        (
            (Expr.Eval, "OP_AC(0x0020)"),
            Expr.Return,
        ),
        'loc_46C4',
    )

    Jump('loc_46FA')

    def _loc_46C4(): pass

    label('loc_46C4')

    OP_AC(0x0020)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            TxtCtl.ShowAll,
            (TxtCtl.SetColor, 0x2),
            '香辣炖煮',
            (TxtCtl.SetColor, 0x0),
            '的做法已经学会了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_46FA(): pass

    label('loc_46FA')

    RemoveItem(ItemTable['料理抄本'], 1)
    Sleep(400)

    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')
    PlaySE(23, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【怀念的料理】',
            (TxtCtl.SetColor, 0x0),
            '完成了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    NewScene('ED6_DT21/T0100._SN', 114, 0, 0)
    IdleLoop()

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
