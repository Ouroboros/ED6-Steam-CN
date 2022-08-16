import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T3132_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3132_1 ._SN')

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
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/T3132_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
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
    ChrSetPos(0x0008, -1700, 0, 2400, 192)
    ChrSetPos(0x0101, -2340, 0, 450, 0)
    ChrSetPos(0x00F7, -1190, 0, 350, 0)
    ChrSetPos(0x00F8, -2290, 0, -670, 0)
    ChrSetPos(0x00F9, -1120, 0, -670, 0)
    CameraMove(-2000, 0, 50, 0)
    OP_67(0, 6150, -10000, 0)
    CameraSetDistance(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#3250460001V欢迎光临。\n',
            '欢迎光临蔡恩拉德酒店。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3250460002V你们是有预约的客人吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010460003V#1011F不，不是的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460004V我们是从\n',
            '协会赶来的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    ChrTalk(
        0x0008,
        (
            '#3250460005V啊，各位是游击士？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3250460006V失礼了。\n',
            '我一直在等你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3250460007V那个，能不能马上\n',
            '就着手寻找呢？',
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
        'loc_2F9',
    )

    ChrTalk(
        0x0101,
        (
            '#0010440863V#1006F嗯，没问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(1, 0x0002)

    Jump('loc_3BF')

    def _loc_2F9(): pass

    label('loc_2F9')

    ChrTalk(
        0x0101,
        (
            '#0010460009V#1007F啊，对不起。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460010V十分抱歉，\n',
            '现在马上开始还有些困难。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3250460011V哦，这样啊。\n',
            '这可不好办了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3250460012V那么请你们料理完\n',
            '手头的事之后马上过来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0071, 0x01, 0x8000)
    EventEnd(0x00)

    Return()

    def _loc_3BF(): pass

    label('loc_3BF')

    Return()

# id: 0x0001 offset: 0x3C0
@scena.Code('func_01_3C0')
def func_01_3C0():
    EventBegin(0x00)
    Fade(1000)
    ChrSetPos(0x0008, -1700, 0, 2400, 192)
    ChrSetPos(0x0101, -2340, 0, 450, 0)
    ChrSetPos(0x00F7, -1190, 0, 350, 0)
    ChrSetPos(0x00F8, -2290, 0, -670, 0)
    ChrSetPos(0x00F9, -1120, 0, -670, 0)
    CameraMove(-2000, 0, 50, 0)
    OP_67(0, 6150, -10000, 0)
    CameraSetDistance(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#3250460013V诸位游击士，\n',
            '我一直在等你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3250460014V我有必须马上拜托\n',
            '你们的急事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3250460015V你们没什么\n',
            '其他的事了吧？',
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
        'loc_56E',
    )

    ChrTalk(
        0x0101,
        (
            '#0010460016V#1006F让你久等了。\n',
            '已经没问题了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(1, 0x0002)

    Jump('loc_61D')

    def _loc_56E(): pass

    label('loc_56E')

    ChrTalk(
        0x0101,
        (
            '#0010460017V#1007F抱、抱歉……\n',
            '其实现在还不行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3250460018V呼，你们真忙……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3250460019V没办法，\n',
            '那就请你们尽早过来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010441543V#1006F嗯，好吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Return()

    def _loc_61D(): pass

    label('loc_61D')

    Return()

# id: 0x0002 offset: 0x61E
@scena.Code('func_02_61E')
def func_02_61E():
    If(
        (
            (Expr.Eval, "OP_29(0x001E, 0x00, 0x04)"),
            Expr.Return,
        ),
        'loc_62B',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_62B(): pass

    label('loc_62B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6A6',
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
            TXT(0x00, '【◇上部遇到过吉米的情况下】\n'),
            TXT(0x01, '【◇不变更】\n'),
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
        (0x00000000, 'loc_6A0'),
        (-1, 'loc_6A6'),
    )

    def _loc_6A0(): pass

    label('loc_6A0')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    Jump('loc_6A6')

    def _loc_6A6(): pass

    label('loc_6A6')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6F3',
    )

    ChrTalk(
        0x0108,
        (
            '#0080460021V#070F根据告示板的公告，\n',
            '好像客人不回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_786')

    def _loc_6F3(): pass

    label('loc_6F3')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_73C',
    )

    ChrTalk(
        0x0104,
        (
            '#0040460022V#030F我看了告示板，\n',
            '好像客人不回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_786')

    def _loc_73C(): pass

    label('loc_73C')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_786',
    )

    ChrTalk(
        0x0105,
        (
            '#0060460023V#040F看了告示板的公告，\n',
            '好像客人不回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_786(): pass

    label('loc_786')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_7B5',
    )

    ChrTalk(
        0x0106,
        (
            '#0050460024V#050F就是说失踪了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7DA')

    def _loc_7B5(): pass

    label('loc_7B5')

    ChrTalk(
        0x0103,
        (
            '#0030460025V#022F就是说失踪了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7DA(): pass

    label('loc_7DA')

    ChrTalk(
        0x0008,
        (
            '#3250460026V是、是的……\n',
            '是这样的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3250460027V三天前出去了\n',
            '就没回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010460028V#1002F三天都没回来\n',
            '确实令人担心呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460029V而且最近大道上也有\n',
            '很多讨厌的魔兽……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3250460030V不，要是大道\n',
            '的话还好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3250460031V可是那位客人……\n',
            '好像是去了钟乳洞。',
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
            '#0010460032V#1004F钟、钟乳洞！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460033V莫非是\n',
            '卡鲁迪亚隧道中途的那个？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3250460034V是，是……\n',
            '就是那个卡鲁迪亚钟乳洞。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3250460035V我们也拼命地\n',
            '阻止过他……',
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
        'loc_A28',
    )

    ChrTalk(
        0x0108,
        (
            '#0080460036V#072F这可不好办了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080460037V那里不是普通人\n',
            '能够进出的地方啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_AF5')

    def _loc_A28(): pass

    label('loc_A28')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A93',
    )

    ChrTalk(
        0x0106,
        (
            '#0050460038V#057F喂喂，开什么玩笑啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050460039V那里不是普通人\n',
            '能够进出的地方啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_AF5')

    def _loc_A93(): pass

    label('loc_A93')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_AF5',
    )

    ChrTalk(
        0x0103,
        (
            '#0030460040V#022F这可不好办了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030460041V钟乳洞可是这一带\n',
            '有名的难关呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_AF5(): pass

    label('loc_AF5')

    ChrTalk(
        0x0101,
        (
            '#0010460042V#1003F竟然不带护卫\n',
            '就去那种地方……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460043V#1002F那个客人到底是何方神圣？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3250460044V是个很普通的青年哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3250460045V名字叫吉米，\n',
            '据他说是来自卢安。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_DFD',
    )

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010460046V#1004F卢、卢安的吉米先生？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460047V#1019F那、那莫非是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0C26')
    def lambda_0C26():
        ChrTurnDirection(0x00F7, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_0C26)

    Sleep(50)

    @scena.Lambda('lambda_0C39')
    def lambda_0C39():
        ChrTurnDirection(0x00F8, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_0C39)

    Sleep(100)

    ChrTurnDirection(0x00F9, 0x0101, 400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_C76',
    )

    ChrTalk(
        0x0106,
        (
            '#0050460048V#052F你认识？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C95')

    def _loc_C76(): pass

    label('loc_C76')

    ChrTalk(
        0x0103,
        (
            '#0030460049V#023F你认识？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C95(): pass

    label('loc_C95')

    ChrTurnDirection(0x0101, 0x00F7, 400)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D55',
    )

    ChrTalk(
        0x0101,
        (
            '#0010460050V#1002F嗯，我曾接过叫这个\n',
            '名字的人的委托。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060460051V#043F记得他那时候在\n',
            '寻找海盗的宝藏吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060460052V他这次会不会也是\n',
            '去钟乳洞寻找什么宝藏？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DFA')

    def _loc_D55(): pass

    label('loc_D55')

    ChrTalk(
        0x0101,
        (
            '#0010460053V#1002F嗯，我曾接过叫这个\n',
            '名字的人的委托。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460054V#1015F记得他那时候在\n',
            '寻找海盗的宝藏吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460055V他这次会不会也是\n',
            '去钟乳洞寻找什么宝藏？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_DFA(): pass

    label('loc_DFA')

    Jump('loc_E4E')

    def _loc_DFD(): pass

    label('loc_DFD')

    ChrTalk(
        0x0101,
        (
            '#0010460056V#1015F卢安的吉米先生。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460057V听上去倒像是\n',
            '一个普通人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_E4E(): pass

    label('loc_E4E')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_EB2',
    )

    ChrTalk(
        0x0104,
        (
            '#0040460058V#032F总之我们要尽快\n',
            '赶往钟乳洞。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040460059V搞不好会\n',
            '来不及的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F7B')

    def _loc_EB2(): pass

    label('loc_EB2')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_F1A',
    )

    ChrTalk(
        0x0107,
        (
            '#0070460060V#062F总、总之得尽快\n',
            '去钟乳洞。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070460061V而且最近魔兽也\n',
            '特别多……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F7B')

    def _loc_F1A(): pass

    label('loc_F1A')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_F7B',
    )

    ChrTalk(
        0x0108,
        (
            '#0080460062V#072F总之我们要尽快\n',
            '赶往钟乳洞。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080460063V搞不好会\n',
            '来不及的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F7B(): pass

    label('loc_F7B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_1032',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_FE3',
    )

    ChrTalk(
        0x0106,
        (
            '#0050460064V#053F嗯，越快越好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0106, 0x0008, 400)

    ChrTalk(
        0x0106,
        (
            '#0050460065V#050F……没其他情报了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_102F')

    def _loc_FE3(): pass

    label('loc_FE3')

    ChrTalk(
        0x0106,
        (
            '#0050460066V#053F嗯，越快越好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050460067V#050F……没其他情报了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_102F(): pass

    label('loc_102F')

    Jump('loc_10DA')

    def _loc_1032(): pass

    label('loc_1032')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_1093',
    )

    ChrTalk(
        0x0103,
        (
            '#0030460068V#022F嗯，越快越好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x0008, 400)

    ChrTalk(
        0x0103,
        (
            '#0030460069V#022F……没其他情报了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10DA')

    def _loc_1093(): pass

    label('loc_1093')

    ChrTalk(
        0x0103,
        (
            '#0030460070V#022F嗯，越快越好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030460071V……没其他情报了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_10DA(): pass

    label('loc_10DA')

    @scena.Lambda('lambda_10E0')
    def lambda_10E0():
        ChrSetDirection(0x0101, 0, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_10E0)

    Sleep(50)

    @scena.Lambda('lambda_10F3')
    def lambda_10F3():
        ChrSetDirection(0x00F8, 0, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_10F3)

    Sleep(100)

    ChrSetDirection(0x00F9, 0, 400)
    WaitForThreadExit(0x00F8, 0x0001)

    ChrTalk(
        0x0008,
        (
            '#3250460072V该说的我都\n',
            '已经说了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3250460073V那么，客人就\n',
            '就麻烦你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010460074V#1002F嗯，我们会尽全力的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_11B9',
    )

    ChrTalk(
        0x0106,
        (
            '#0050460075V#050F那我们走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11DC')

    def _loc_11B9(): pass

    label('loc_11B9')

    ChrTalk(
        0x0103,
        (
            '#0030460076V#022F那我们走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_11DC(): pass

    label('loc_11DC')

    OP_28(0x0071, 0x04, 0x04)
    OP_28(0x0071, 0x04, 0x08)
    OP_28(0x0071, 0x01, 0x0001)
    OP_28(0x0071, 0x01, 0x0002)
    EventEnd(0x00)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
