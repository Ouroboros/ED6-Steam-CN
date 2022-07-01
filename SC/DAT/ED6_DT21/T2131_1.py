import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T2131_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2131_1 ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'T2131.x'
    header.mapIndex       = 1
    header.bgm            = 12
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0xC060
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
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_286',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0068, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_141',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_FD',
    )

    ChrTalk(
        0x00FE,
        (
            '今天真是麻烦你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果有事\n',
            '还请多多帮忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_13E')

    def _loc_FD(): pass

    label('loc_FD')

    ChrTalk(
        0x00FE,
        (
            '我在这里等我丈夫。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '之后娱乐场的人\n',
            '一定会想办法解决的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_13E(): pass

    label('loc_13E')

    Jump('loc_283')

    def _loc_141(): pass

    label('loc_141')

    If(
        (
            (Expr.Eval, "OP_29(0x0068, 0x00, 0x40)"),
            Expr.Return,
        ),
        'loc_1E0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_19A',
    )

    ChrTalk(
        0x00FE,
        (
            '特地麻烦你们真不好意思。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果再发生什么事\n',
            '还请多多帮忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1DD')

    def _loc_19A(): pass

    label('loc_19A')

    ChrTalk(
        0x00FE,
        (
            '我在这里再等等丈夫。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '娱乐场的人\n',
            '要是能解决那个人就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1DD(): pass

    label('loc_1DD')

    Jump('loc_283')

    def _loc_1E0(): pass

    label('loc_1E0')

    If(
        (
            (Expr.Eval, "OP_29(0x0068, 0x00, 0x02)"),
            Expr.Return,
        ),
        'loc_1F6',
    )

    TalkEnd(0x00FE)
    EventBegin(0x00)
    Call(1, 0x0001)
    EventEnd(0x00)

    Return()

    def _loc_1F6(): pass

    label('loc_1F6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_219',
    )

    ChrTalk(
        0x00FE,
        (
            '谁来\n',
            '阻止我丈夫啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_283')

    def _loc_219(): pass

    label('loc_219')

    OP_A2(0x0007)

    ChrTalk(
        0x00FE,
        (
            '啊啊，怎么办呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我老公\n',
            '已经完全打算\n',
            '放手一搏了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '拜托谁来帮帮忙啊！\n',
            '请阻止我丈夫吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_283(): pass

    label('loc_283')

    Jump('loc_456')

    def _loc_286(): pass

    label('loc_286')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_368',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_2EA',
    )

    ChrTalk(
        0x00FE,
        (
            '我实在看不下去了,\n',
            '所以来了１楼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊啊，娱乐场的人\n',
            '求求你们阻止我丈夫吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_365')

    def _loc_2EA(): pass

    label('loc_2EA')

    OP_A2(0x0007)

    ChrTalk(
        0x00FE,
        (
            '啊，真伤脑筋……\n',
            '我丈夫真是昏了头了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他再这样下去，\n',
            '搞不好就要\n',
            '变成废人了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊啊，娱乐场的人\n',
            '请努力啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_365(): pass

    label('loc_365')

    Jump('loc_456')

    def _loc_368(): pass

    label('loc_368')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 4, 0x121C)),
            Expr.Return,
        ),
        'loc_3A8',
    )

    ChrTalk(
        0x00FE,
        (
            '真奇怪。\n',
            '店里没人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '服务生都\n',
            '到哪里去了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_456')

    def _loc_3A8(): pass

    label('loc_3A8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_456',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_3FB',
    )

    ChrTalk(
        0x00FE,
        (
            '但是，必须\n',
            '见好就收才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '否则我丈夫\n',
            '容易得意忘形。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_456')

    def _loc_3FB(): pass

    label('loc_3FB')

    OP_A2(0x0007)

    ChrTalk(
        0x00FE,
        (
            '吃角子游戏机真有趣。\n',
            '运气好可能会中大奖的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我丈夫好像也赢了，\n',
            '会赚钱回来吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_456(): pass

    label('loc_456')

    TalkEnd(0x00FE)

    Return()

# id: 0x0001 offset: 0x45A
@scena.Code('Init')
def Init():
    OP_4A(0x000E, 0)
    Fade(1000)
    SetChrPos(0x0101, 5600, 250, 33020, 0)
    SetChrPos(0x00F7, 4770, 250, 32659, 0)
    SetChrPos(0x0104, 5560, 250, 31520, 0)
    SetChrPos(0x0105, 4580, 250, 31210, 0)
    OP_6D(4960, 250, 33040, 0)
    OP_0D()

    If(
        (
            (Expr.Eval, "OP_29(0x0068, 0x01, 0x8000)"),
            Expr.Return,
        ),
        'loc_509',
    )

    ChrTalk(
        0x000E,
        (
            '#3140440008V啊，游击士！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#3140440009V有空听我说话了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_62E')

    def _loc_509(): pass

    label('loc_509')

    ChrTalk(
        0x0101,
        (
            '#0010440001V#1011F请问～打扰一下行吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440002V你是拉科舒小姐？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000E, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    ChrTalk(
        0x000E,
        (
            '#3140440003V啊……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#3140440004V难道你们是游击士！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010440005V#1000F是啊。\n',
            '我们看了公告板来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#3140440006V我、我有事\n',
            '想马上拜托你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#3140440007V……能听我说吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_62E(): pass

    label('loc_62E')

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
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_82B',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0068, 0x01, 0x8000)"),
            Expr.Return,
        ),
        'loc_73C',
    )

    ChrTalk(
        0x0101,
        (
            '#0010440010V#1015F嗯……抱歉……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440011V还不大方便。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#3140440012V咦～不行吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#3140440013V如果方便了\n',
            '请立刻过来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010440014V#1000F嗯，先就这样吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_820')

    def _loc_73C(): pass

    label('loc_73C')

    ChrTalk(
        0x0101,
        (
            '#0010440015V#1007F啊，抱歉……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440016V现在有点不方便。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#3140440017V咦～这样吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#3140440018V那，方便的时候\n',
            '请立刻过来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#3140440019V这关系到\n',
            '我们夫妇的未来啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010440020V#1000F嗯、嗯，明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_820(): pass

    label('loc_820')

    OP_28(0x0068, 0x01, 0x8000)
    OP_4B(0x000E, 0)

    Return()

    def _loc_82B(): pass

    label('loc_82B')

    If(
        (
            (Expr.Eval, "OP_29(0x0068, 0x01, 0x8000)"),
            Expr.Return,
        ),
        'loc_88C',
    )

    ChrTalk(
        0x0101,
        (
            '#0010440021V#1006F嗯，没问题了。\n',
            '让你久等了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440022V那么，是怎么回事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8D2')

    def _loc_88C(): pass

    label('loc_88C')

    ChrTalk(
        0x0101,
        (
            '#0010440023V#1006F嗯，当然可以。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440022V那么，是怎么回事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8D2(): pass

    label('loc_8D2')

    OP_4A(0x000D, 0)
    OP_4A(0x000B, 0)
    OP_28(0x0068, 0x01, 0x0001)
    OP_28(0x0068, 0x01, 0x0002)

    ChrTalk(
        0x000E,
        (
            '#3140440025V我想拜托的\n',
            '是很简单的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#3140440026V希望你们想办法\n',
            '打败我丈夫！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0000, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0001, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(100)

    OP_62(0x0002, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0003, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010440027V#1004F……咦！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_9F9',
    )

    ChrTalk(
        0x0106,
        (
            '#0050440028V#052F这就是委托的内容？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A1C')

    def _loc_9F9(): pass

    label('loc_9F9')

    ChrTalk(
        0x0103,
        (
            '#0030440029V#023F这是委托吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A1C(): pass

    label('loc_A1C')

    ChrTalk(
        0x0104,
        (
            '#0040440030V#033F只要\n',
            '赢了你丈夫就行吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#3140440031V对，任何游戏都可以，\n',
            '无论如何要赢了我丈夫。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#3140440032V我丈夫本来\n',
            '就容易得意忘形……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#3140440033V在娱乐场稍微连胜几盘\n',
            '就马上一副恶棍嘴脸了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#3140440034V他就是这种人，这样下去\n',
            '真的会沉迷了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#3140440035V所以，在变成那样之前\n',
            '我希望让他吃点苦头。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010440036V#1016F哈、哈哈……原来如此。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440037V真是家家有本难念的经啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_BEC',
    )

    ChrTalk(
        0x0106,
        (
            '#0050440038V#551F……你也够辛苦的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C17')

    def _loc_BEC(): pass

    label('loc_BEC')

    ChrTalk(
        0x0103,
        (
            '#0030440039V#026F嗯，你也够辛苦的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C17(): pass

    label('loc_C17')

    ChrTalk(
        0x000E,
        (
            '#3140440040V哪里，我也想得太简单了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#3140440041V他邀请我去娱乐场游玩的时候\n',
            '就该断然拒绝的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#3140440042V唉，发牢骚也不是办法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#3140440043V……那么，作为资本\n',
            '给你们１０００米拉吧。',
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
            '得到了',
            (TxtCtl.SetColor, 0x4),
            '１０００',
            (TxtCtl.SetColor, 0x0),
            '米拉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x000E,
        (
            '#3140440044V如果全部压上一回定胜负\n',
            '我丈夫一定会上钩的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060440045V#044F这么说……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060440046V你丈夫现在就在二楼的娱乐场里？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#3140440047V是的，他一直逗留在那里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#3140440048V在扑克台那里\n',
            '叫菲利奥的就是他。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010440049V#1000F明白。\n',
            '扑克台那里的菲利奥对吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#3140440050V绝不要手下留情。\n',
            '请彻底打败他。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#3140440051V……其它还有什么问题吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010440052V#1015F嗯，大概知道要做什么了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440053V话说回来，怎样赢他\n',
            '才是个问题呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440054V因为这些\n',
            '完全是靠运气嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x00F7, 90, 400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_F99',
    )

    ChrTalk(
        0x0106,
        (
            '#0050440055V#050F啊啊，不过活用运势\n',
            '也是靠手段的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050440056V能不能赢就看对手了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FF3')

    def _loc_F99(): pass

    label('loc_F99')

    ChrTalk(
        0x0103,
        (
            '#0030440057V#027F嗯，不过活用运势\n',
            '也是靠手段的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030440058V能不能赢就看对手了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_FF3(): pass

    label('loc_FF3')

    ChrTalk(
        0x0104,
        (
            '#0040440059V#031F呵，就是说要因势利导啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0101, 180, 400)

    ChrTalk(
        0x0101,
        (
            '#0010440060V#1015F嗯～……\n',
            '是这么回事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#3140440061V那就没问题了。\n',
            '我丈夫耍花招可是外行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#3140440062V又不擅长说谎，\n',
            '想什么都一目了然……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#3140440063V本来就是个\n',
            '完全不适合玩这个的人哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0101, 0, 400)

    ChrTalk(
        0x0101,
        (
            '#0010440064V#1011F啊，真的吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440065V#1006F嗯，这样说\n',
            '我就有点自信了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440066V……好！有精神了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_11DB',
    )

    ChrTalk(
        0x0106,
        (
            '#0050440067V#051F哦，就是这股劲。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050440068V要是输了气势，\n',
            '本来能赢的牌局也赢不了了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_123F')

    def _loc_11DB(): pass

    label('loc_11DB')

    ChrTalk(
        0x0103,
        (
            '#0030440069V#020F呵呵，就是这种气势。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030440070V或许算不上什么理由，\n',
            '不过比赛要的就是气势。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_123F(): pass

    label('loc_123F')

    ChrTalk(
        0x000E,
        (
            '#3140440071V那么，努力哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#3140440072V请尽可能的\n',
            '打败我丈夫吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    Sleep(1000)

    OP_20(0x000003E8)
    OP_26(254)
    OP_26(256)
    OP_26(663)
    SetChrPos(0x000D, 32530, 0, 29680, 79)
    SetChrPos(0x0101, 29280, 0, 35000, 180)
    SetChrPos(0x00F7, 30180, 0, 35430, 180)
    SetChrPos(0x0104, 28980, 0, 36040, 180)
    SetChrPos(0x0105, 29800, 0, 36620, 180)
    OP_6D(28300, 0, 25990, 0)
    OP_6C(332000, 0)

    @scena.Lambda('lambda_131D')
    def lambda_131D():
        OP_6D(29350, 0, 36160, 4000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_131D)

    @scena.Lambda('lambda_1335')
    def lambda_1335():
        OP_6C(315000, 4000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_1335)

    OP_21()
    OP_1D(0x19)
    Sleep(400)

    FadeIn(2000, 0)
    OP_0D()
    WaitForThreadExit(0x0000, 0x0001)
    WaitForThreadExit(0x0000, 0x0002)
    Sleep(400)

    ChrTalk(
        0x0104,
        (
            '#0040440073V#030F唔，这娱乐场\n',
            '气氛还挺不错嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040440074V设备也挺新，\n',
            '开张还没多久吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060440075V#040F对，似乎是诞辰庆典的时候\n',
            '重新装修开放的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010440076V#1011F啊，说起来\n',
            '之前来的时候还在装修中呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040440077V#035F原来如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040440078V#033F……对了，\n',
            '关键的对象在哪里？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010440079V#1015F嗯，记得太太\n',
            '说是在扑克台来着……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    OP_62(0x00F7, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x00F7, 0x000B, 400)
    Sleep(1000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_151E',
    )

    ChrTalk(
        0x0106,
        (
            '#0050440080V#050F……嗯，是那位吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_154E')

    def _loc_151E(): pass

    label('loc_151E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_154E',
    )

    ChrTalk(
        0x0103,
        (
            '#0030440081V#020F……一定是那位吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_154E(): pass

    label('loc_154E')

    @scena.Lambda('lambda_1554')
    def lambda_1554():
        ChrTurnDirection(0x0101, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1554)

    Sleep(100)

    @scena.Lambda('lambda_1567')
    def lambda_1567():
        ChrTurnDirection(0x0105, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_1567)

    Sleep(50)

    @scena.Lambda('lambda_157A')
    def lambda_157A():
        ChrTurnDirection(0x0104, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_157A)

    OP_4A(0x000D, 255)
    OP_4A(0x000B, 255)
    OP_6D(32170, 0, 30500, 2000)

    ChrTalk(
        0x000D,
        (
            '#3130440082V#1P……好～来吧～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000D, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(2500)

    OP_63(0x000D)
    OP_62(0x000D, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(400)

    OP_95(0x000D, 0x00000000, 0x00000000, 0x00000000, 0x00000320, 0x00002EE0)

    ChrTalk(
        0x000D,
        (
            '#3130440083V#3S#1P你看来了！是Ｊ！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3130440084V#1P唔～～这超强的手气！\n',
            '简直是无敌的感觉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3150440085V#2P……客人赢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3130440086V#1P哎呀～你也很努力了。\n',
            '就是找错了对手。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3130440087V#1P哈哈哈哈哈哈。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(1000)
    OP_6D(29520, 0, 35790, 0)
    OP_0D()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(1500)

    ChrTalk(
        0x0101,
        (
            '#0010440088V#1007F……真是一目了然啊～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440089V嗯，是那个人没错了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_17CD',
    )

    ChrTalk(
        0x0106,
        (
            '#0050440090V#050F赶快去搭话吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050440091V再磨磨蹭蹭的\n',
            '又要开始啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1820')

    def _loc_17CD(): pass

    label('loc_17CD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_1820',
    )

    ChrTalk(
        0x0103,
        (
            '#0030440092V#020F马上去搭话吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030440093V再磨磨蹭蹭的\n',
            '又要开始啰。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1820(): pass

    label('loc_1820')

    ChrTalk(
        0x0101,
        (
            '#0010440094V#1002F啊，是哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    CreateThread(0x0101, 0x01, 0x01, 0x0005)
    Sleep(100)

    CreateThread(0x0104, 0x01, 0x01, 0x0007)
    Sleep(400)

    CreateThread(0x00F7, 0x01, 0x01, 0x0006)
    Sleep(200)

    CreateThread(0x0105, 0x01, 0x01, 0x0008)
    Sleep(400)

    Fade(1000)
    OP_6D(32170, 0, 30500, 0)
    OP_6D(31090, 0, 31350, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x000D,
        (
            '#3130440095V好，那就……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0101, 0x0001)
    OP_62(0x000D, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTurnDirection(0x000D, 0x0101, 400)
    Sleep(1000)

    ChrTalk(
        0x000D,
        (
            '#3130440096V咦？你们怎么了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010440097V#1006F#5P大哥你\n',
            '就是传说中的强者吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440098V其实我们\n',
            '是来挑战你的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3130440099V挑战？找我吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3130440100V倒是可以，不过你们有钱吗？\n',
            '五块十块的恕不奉陪哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_1A13',
    )

    ChrTalk(
        0x0106,
        (
            '#0050440101V#050F#2P１０００米拉、\n',
            '全部押上定胜负怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A57')

    def _loc_1A13(): pass

    label('loc_1A13')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_1A57',
    )

    ChrTalk(
        0x0103,
        (
            '#0030440102V#027F#2P１０００米拉、\n',
            '全部押上定胜负如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A57(): pass

    label('loc_1A57')

    ChrTalk(
        0x000D,
        (
            '#3130440103V呵呵，真是不怕死啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3130440104V好啊，我就\n',
            '接受挑战吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3130440105V……那，谁来做我的对手？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3130440106V不然一起上\n',
            '也没关系哦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010440107V#1016F#5P一、一起上怎么可能……\n',
            '又不是抓阄。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000B, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_6D(32240, 0, 31870, 1000)

    ChrTalk(
        0x000B,
        (
            '#3150440108V#2P……那么，客人。\n',
            '变规则同花顺怎样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3150440109V#2P这个还能用复数次\n',
            '的胜负来做个决断。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1BD0')
    def lambda_1BD0():
        OP_8C(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_1BD0)

    Sleep(100)

    @scena.Lambda('lambda_1BE3')
    def lambda_1BE3():
        OP_8C(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_1BE3)

    @scena.Lambda('lambda_1BF1')
    def lambda_1BF1():
        OP_8C(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_1BF1)

    Sleep(150)

    @scena.Lambda('lambda_1C04')
    def lambda_1C04():
        OP_8C(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_1C04)

    ChrTurnDirection(0x000D, 0x000B, 400)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010440110V#1004F有这样的游戏吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3130440111V唔～好像很有趣嘛。\n',
            '说明一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3150440112V#2P好的，双方各出选手、\n',
            '以三回合对战决胜负。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3150440113V#2P对战就用普通的同花顺，\n',
            '先获得１胜的队伍就算赢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3150440114V#2P不过，『放弃』的机会\n',
            '两个队都只能有一次。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3150440115V#2P队伍中有一人放弃之后，\n',
            '那个队伍的选手\n',
            '就无法再放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3130440116V原来如此，三回定胜负吗～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3130440117V嗯，方便的\n',
            '好办法嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000D, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x000D, 0x0101, 400)
    OP_6D(30280, 0, 32090, 1000)

    ChrTalk(
        0x000D,
        (
            '#3130440118V咦……？\n',
            '但是，你们有４人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x000D, 400)

    ChrTalk(
        0x0101,
        (
            '#0010440119V#1006F#1P４人也无所谓啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440120V既然多的话，\n',
            '就退出一人好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x000D, 400)

    ChrTalk(
        0x0105,
        (
            '#0060440121V#043F#2P那个，这样的话……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060440122V……就让我退出吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(400)

    @scena.Lambda('lambda_1EF8')
    def lambda_1EF8():
        ChrTurnDirection(0x00FE, 0x0105, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_1EF8)

    @scena.Lambda('lambda_1F06')
    def lambda_1F06():
        ChrTurnDirection(0x00FE, 0x0105, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_1F06)

    @scena.Lambda('lambda_1F14')
    def lambda_1F14():
        ChrTurnDirection(0x00FE, 0x0105, 400)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_1F14)

    ChrTurnDirection(0x0000, 0x0105, 400)

    ChrTalk(
        0x0101,
        (
            '#0010440123V#1004F#3P咦？科洛丝吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060440124V#043F#2P对，校规禁止\n',
            '学生在娱乐场游玩。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060440125V所以，我就……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010440126V#1016F#3P啊哈哈……这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440127V唔，确实\n',
            '是不利于教育。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440128V#1000F……嗯，情况明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060440129V#047F#2P嗯，对不起了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0104, 0x000D, 400)

    ChrTalk(
        0x0104,
        (
            '#0040440130V#030F#1P嗯，这样\n',
            '３回定胜负就没问题了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3130440131V我几回定胜负都无所谓。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3130440132V反正最后\n',
            '总是要赢的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3150440133V就用刚才说明的\n',
            '游戏可以吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2107')
    def lambda_2107():
        OP_8C(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_2107)

    @scena.Lambda('lambda_2115')
    def lambda_2115():
        OP_8C(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_2115)

    @scena.Lambda('lambda_2123')
    def lambda_2123():
        OP_8C(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_2123)

    @scena.Lambda('lambda_2131')
    def lambda_2131():
        OP_8C(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_2131)

    ChrTurnDirection(0x000D, 0x000B, 400)

    ChrTalk(
        0x000D,
        (
            '#3130440134V嗯，这个就行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_2198',
    )

    ChrTalk(
        0x0106,
        (
            '#0050440135V#050F#2P啊啊，我们也没问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_21CB')

    def _loc_2198(): pass

    label('loc_2198')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_21CB',
    )

    ChrTalk(
        0x0103,
        (
            '#0030440136V#020F#2P嗯，我们也没问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_21CB(): pass

    label('loc_21CB')

    ChrTalk(
        0x000B,
        (
            '#3150440137V那么，我去准备一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3150440138V趁此机会请客人们\n',
            '决定出场顺序。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010440139V#1000F决定出场的\n',
            '顺序就可以了吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440140V嗯，明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3150440141V就麻烦你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000D, 0x0101, 400)

    ChrTalk(
        0x000D,
        (
            '#3130440142V赶快定吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0010)
    CreateThread(0x000B, 0x01, 0x01, 0x0014)

    ExecExpressionWithValue(
        0x0019,
        0x01,
        (
            (Expr.GetChrWork, 0x101, 0x1),
            (Expr.GetChrWork, 0x105, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0019,
        0x02,
        (
            (Expr.GetChrWork, 0x101, 0x2),
            (Expr.GetChrWork, 0x105, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0019,
        0x03,
        (
            (Expr.GetChrWork, 0x101, 0x3),
            (Expr.GetChrWork, 0x105, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_2301')
    def lambda_2301():
        ChrTurnDirection(0x00FE, 0x0019, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_2301)

    Sleep(100)

    @scena.Lambda('lambda_2314')
    def lambda_2314():
        ChrTurnDirection(0x00FE, 0x0019, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_2314)

    Sleep(150)

    @scena.Lambda('lambda_2327')
    def lambda_2327():
        ChrTurnDirection(0x00FE, 0x0019, 400)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_2327)

    ChrTurnDirection(0x0000, 0x0105, 400)

    @scena.Lambda('lambda_233C')
    def lambda_233C():
        OP_8C(0x000D, 90, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_233C)

    OP_69(0x0105, 0x000005DC)

    ChrTalk(
        0x0101,
        (
            '#0010440143V#1015F话是这么说……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440144V那么，怎么办呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040440145V#035F#1P嗯，应该按照\n',
            '玩牌的水平来决定吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_287B',
    )

    ChrTalk(
        0x0101,
        (
            '#0010440146V#1019F话先说在前头，\n',
            '我可没什么自信。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440147V以前总是输给约修亚的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050440148V#053F#2P我也金盆洗手\n',
            '好久了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050440149V#050F……不过，比赛是靠气势的。\n',
            '我尽量努力啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050440150V那，你怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040440151V#031F#1P呼，放心吧。\n',
            '玩牌我略有心得。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040440152V因势利导的中坚\n',
            '就交给我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050440153V#050F#2P好，那就这么办吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010440154V#1002F奥利维尔是２号。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440155V然后就看我和阿加特了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0106, 0x0101, 400)

    ChrTalk(
        0x0106,
        (
            '#0050440156V#057F#2P我第一个上。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050440157V你垫后吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    ChrTurnDirection(0x0101, 0x0106, 400)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010440158V#1020F啊……！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440159V怎、怎么擅自决定？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0104, 0x0101, 400)

    ChrTalk(
        0x0104,
        (
            '#0040440160V#031F#1P呵，所谓先手必胜嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040440161V就是说，策略就是\n',
            '靠我和阿加特来定胜负。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050440162V#053F#2P就这么回事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050440163V嗯，顺序什么的没多大意义。\n',
            '关键是能赢就行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A3(0x0010)

    ChrTalk(
        0x0101,
        (
            '#0010440164V#1007F话、话是没错啦，\n',
            '压力好大……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x000B, 0x0001)
    OP_8C(0x000B, 270, 400)

    ChrTalk(
        0x000B,
        (
            '#3150440165V客人，准备就绪了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0104, 0x000B, 400)

    ChrTalk(
        0x0104,
        (
            '#0040440166V#032F#1P嗯，那就上吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010440167V#1009F呜～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050440168V#552F#2P……来，开始啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060440169V#040F#1P艾丝蒂尔，加油。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0105, 400)

    ChrTalk(
        0x0101,
        (
            '#0010440170V#1016F唔、嗯，谢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0101, 90, 400)

    ChrTalk(
        0x0101,
        (
            '#0010440171V#1002F好，事到如今\n',
            '只有硬着头皮上了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2C68')

    def _loc_287B(): pass

    label('loc_287B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_2C68',
    )

    ChrTalk(
        0x0101,
        (
            '#0010440146V#1019F话先说在前头，\n',
            '我可没什么自信。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440147V以前总是输给约修亚的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010440174V#1006F啊，但是……\n',
            '雪拉姐有自信吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440175V占卜也是用牌的嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030440176V#020F#2P嗯，会一点。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030440177V#026F不过，我嘛…\n',
            '万不得已还有秘技……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    OP_22(0x0026, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010440178V#1011F秘技……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030440179V#525F#2P呵呵，秘技当然就是秘密啰。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040440180V#031F#1P呼，那就麻烦\n',
            '雪拉垫后了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040440181V#030F相对的，\n',
            '就由我担任中坚吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040440182V因为第二战\n',
            '似乎更需要策略。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010440183V#1015F雪拉姐最后，\n',
            '奥利维尔第二，这么说来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440184V#1004F我打头阵？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030440185V#021F#2P嗯，很轻松吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030440186V轻松的上场吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x0101, 400)
    OP_A3(0x0010)

    ChrTalk(
        0x0101,
        (
            '#0010440187V#1007F唔，轻松倒是轻松……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x000B, 0x0001)
    OP_8C(0x000B, 270, 400)

    ChrTalk(
        0x000B,
        (
            '#3150440165V客人，准备就绪了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    OP_8C(0x0101, 90, 400)

    ChrTalk(
        0x0101,
        (
            '#0010440189V#1002F啊，好像要开始了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0104, 90, 400)

    ChrTalk(
        0x0104,
        (
            '#0040440190V#030F#1P嗯，那就上吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060440191V#040F各位、\n',
            '请加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010440192V#1005F好，抖擞精神上阵吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2C68(): pass

    label('loc_2C68')

    FadeOut(2000, 0, -1)
    OP_0D()
    CreateThread(0x0009, 0x03, 0x01, 0x0002)
    WaitForThreadExit(0x0009, 0x0003)

    If(
        (
            (Expr.Eval, "OP_29(0x0068, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2C96',
    )

    CreateThread(0x0009, 0x03, 0x01, 0x0003)
    WaitForThreadExit(0x0009, 0x0003)

    def _loc_2C96(): pass

    label('loc_2C96')

    If(
        (
            (Expr.Eval, "OP_29(0x0068, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2CAD',
    )

    CreateThread(0x0009, 0x03, 0x01, 0x0004)
    WaitForThreadExit(0x0009, 0x0003)

    def _loc_2CAD(): pass

    label('loc_2CAD')

    Return()

# id: 0x0002 offset: 0x2CAE
@scena.Code('ReInit')
def ReInit():
    OP_4A(0x000B, 255)
    OP_4A(0x000D, 255)
    OP_4A(0x0018, 255)
    ChrTurnDirection(0x0018, 0x000D, 0)
    LoadEffect(0x00, 'craft\\cr201_01.eff')
    Sleep(1000)

    OP_6D(27430, 0, 32610, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_2D18',
    )

    SetChrPos(0x00F7, 33000, 0, 31870, 135)
    SetChrPos(0x0101, 28570, 0, 31000, 90)

    Jump('loc_2D3A')

    def _loc_2D18(): pass

    label('loc_2D18')

    SetChrPos(0x0101, 33000, 0, 31870, 135)
    SetChrPos(0x00F7, 28570, 0, 31000, 90)

    def _loc_2D3A(): pass

    label('loc_2D3A')

    SetChrPos(0x0105, 27670, 0, 31940, 90)
    SetChrPos(0x0104, 28850, 0, 32500, 90)
    FadeIn(2000, 0)
    OP_0D()
    OP_6D(32073, 0, 31585, 2000)
    Sleep(1000)

    ChrTalk(
        0x000B,
        (
            '#3150440193V……那么现在\n',
            '开始三回战决胜负。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3150440194V同花顺的规则\n',
            '和本地普通规则相同……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3150440195V不过图案也是有强弱之分的\n',
            '这点请多加注意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3150440196V最强的是黑桃，\n',
            '其次是红心，再次是方块\n',
            '梅花是最弱的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3150440197V……那么，现在发放手牌。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(1000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_4323',
    )

    Call(2, 0x0003)
    Sleep(400)

    OP_62(0x000D, 0x00000000, 2000, 0x08, 0x09, 0x000000FA, 0x02)
    OP_22(0x000F, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x000D,
        (
            '#3130440198V哟呵呵！\n',
            '起手就是好兆头！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3130440199V呀～这下搞不好\n',
            '可以速战速决了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()
    OP_6D(29690, 0, 31480, 1000)

    ChrTalk(
        0x0101,
        (
            '#0010440200V#1002F（怎，怎么对手\n',
            '  状况那么好啊……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040440201V#035F（哼，如果真是好牌\n',
            '  一般应该是沉默的哦。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040440202V#030F（对手要是放弃了\n',
            '  就不算赢的。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010440203V#1015F（啊，原来如此啊。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(32073, 0, 31585, 0)
    OP_0D()
    FadeOut(300, 0, 100)
    OP_C5(0x00, 0xFFCE, 0xFFB0, 0x0032, 0x0050, 0x01E3, 0x00F0, 0x0200, 0x0200, 0x0000, 0x0000, 0x0064, 0x00A0, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x01, 0xFFCE, 0xFFB0, 0x0032, 0x0050, 0x01E1, 0x00EE, 0x0200, 0x0200, 0x0000, 0x0000, 0x0064, 0x00A0, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x02, 0xFFCE, 0xFFB0, 0x0032, 0x0050, 0x01DF, 0x00EC, 0x0200, 0x0200, 0x0000, 0x0000, 0x0064, 0x00A0, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x03, 0xFFCE, 0xFFB0, 0x0032, 0x0050, 0x01DD, 0x00EA, 0x0200, 0x0200, 0x0000, 0x0000, 0x0064, 0x00A0, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x04, 0xFFCE, 0xFFB0, 0x0032, 0x0050, 0x01DB, 0x00E8, 0x0200, 0x0200, 0x0000, 0x0000, 0x0064, 0x00A0, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x05, 0xFFCE, 0xFFB0, 0x0032, 0x0050, 0x00A3, 0x00E8, 0x0200, 0x0200, 0x0190, 0x0000, 0x01F4, 0x00A0, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x06, 0xFFCE, 0xFFB0, 0x0032, 0x0050, 0x00F3, 0x00EA, 0x0200, 0x0200, 0x0000, 0x0140, 0x0064, 0x01E0, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x07, 0xFFCE, 0xFFB0, 0x0032, 0x0050, 0x0143, 0x00EC, 0x0200, 0x0200, 0x00C8, 0x0140, 0x012C, 0x01E0, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x08, 0xFFCE, 0xFFB0, 0x0032, 0x0050, 0x0193, 0x00EE, 0x0200, 0x0200, 0x0064, 0x0000, 0x00C8, 0x00A0, 0x00FFFFFF, 0x00, 'C_VIS229._CH')
    OP_C5(0x09, 0xFFCE, 0xFFB0, 0x0032, 0x0050, 0x01E3, 0x00F0, 0x0200, 0x0200, 0x0064, 0x0140, 0x00C8, 0x01E0, 0x00FFFFFF, 0x00, 'C_VIS229._CH')
    OP_C6(0x05, 0x03, -1, 400, 0)
    OP_C6(0x06, 0x03, -1, 400, 0)
    OP_C6(0x07, 0x03, -1, 400, 0)
    OP_C6(0x08, 0x03, -1, 400, 0)
    OP_C6(0x09, 0x03, -1, 400, 0)
    Sleep(1000)

    SetMessageWindowPos(-1, 320, -1, -1)
    SetChrName('阿加特')

    Talk(
        (
            '#0050440204V#050F（……那么，这样吧。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050440205V（应该以大牌为目标\n',
            '还是小牌保底呢……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

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

    Menu(
        0,
        10,
        100,
        0,
        (
            TXT(0x00, '【除了Ｋ其它全部换】\n'),
            TXT(0x01, '【以４～８的顺子为目标】\n'),
        ),
    )

    MenuEnd(0x0003)
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
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3398',
    )

    SetMessageWindowPos(-1, 320, -1, -1)
    SetChrName('阿加特')

    Talk(
        (
            '#0050440206V#050F（哪边都一样危险……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050440207V（不过，反正还是首战。\n',
            '  这里就以概率高的一方为目标吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_33FC')

    def _loc_3398(): pass

    label('loc_3398')

    SetMessageWindowPos(-1, 320, -1, -1)
    SetChrName('阿加特')

    Talk(
        (
            '#0050440206V#050F（哪边都一样危险……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050440209V（那就以大牌为目标吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_33FC(): pass

    label('loc_33FC')

    Call(2, 0x0017)
    OP_C7(0x01, 0xFF, 0x00)
    OP_C6(0x00, 0x06, 0, 0, 0)
    OP_C6(0x01, 0x06, 0, 0, 0)
    OP_C6(0x02, 0x06, 0, 0, 0)
    OP_C6(0x03, 0x06, 0, 0, 0)
    OP_C6(0x04, 0x06, 0, 0, 0)
    OP_C6(0x05, 0x06, 0, 0, 0)
    OP_C6(0x06, 0x06, 0, 0, 0)
    OP_C6(0x07, 0x06, 0, 0, 0)
    OP_C6(0x08, 0x06, 0, 0, 0)
    OP_C6(0x09, 0x06, 0, 0, 0)
    FadeIn(300, 0)
    Sleep(1000)

    ChrTurnDirection(0x000B, 0x0106, 400)

    ChrTalk(
        0x000B,
        (
            '#3150440210V要换牌吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3549',
    )

    ChrTalk(
        0x0106,
        (
            '#0050440211V#050F#2P啊啊，换４张。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000B, 0x000D, 400)

    ChrTalk(
        0x000B,
        (
            '#3150440212V……客人您呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3130440213V#1P我换３张。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_35B7')

    def _loc_3549(): pass

    label('loc_3549')

    ChrTalk(
        0x0106,
        (
            '#0050440214V#050F#2P啊啊，换２张。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000B, 0x000D, 400)

    ChrTalk(
        0x000B,
        (
            '#3150440212V……客人您呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3130440213V#1P我换３张。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_35B7(): pass

    label('loc_35B7')

    OP_59()
    Call(2, 0x0004)
    OP_59()
    Fade(1000)
    OP_6D(29690, 0, 31480, 0)
    OP_0D()

    ChrTalk(
        0x0105,
        (
            '#0060440217V#042F（阿加特的表情……\n',
            '  纹丝不动。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040440218V#031F#2P（嗯嗯，简直\n',
            '  就是扑克脸。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040440219V（充满了气魄的眼神，\n',
            '  令人着迷的男人风采。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000D, 0x00000000, 2000, 0x0A, 0x0B, 0x000000FA, 0x02)
    OP_22(0x000F, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x000D,
        (
            '#3130440220V#1P呼呼，不错哦～\n',
            '来的就是我要的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000D, 0x0106, 400)

    ChrTalk(
        0x000D,
        (
            '#3130440221V#1P好了、挑战者们。\n',
            '放马过来吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010440222V#1007F（对、对方真是截然相反啊～）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440223V（说是那么说，\n',
            '  谁知道是真是假。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(32073, 0, 31585, 0)
    OP_0D()
    Call(2, 0x0005)
    OP_0D()
    ChrTurnDirection(0x000B, 0x0106, 400)

    ChrTalk(
        0x000B,
        (
            '#3150440224V……要比牌吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3A9B',
    )

    OP_28(0x0068, 0x01, 0x0008)

    ChrTalk(
        0x0106,
        (
            '#0050440225V#053F#2P…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050440226V#050F……哎呀，我放弃。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000D, 0x0106, 400)

    ChrTalk(
        0x000D,
        (
            '#3130440227V#1P咦～要放弃吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3130440228V#1P嗯～难得\n',
            '我凑得一手好牌，真可惜啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3150440229V那么，这边的客人。\n',
            '之后就不能再放弃了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(1000)
    OP_6D(27210, 0, 33050, 0)
    OP_8C(0x000D, 90, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010440230V#1026F啊～啊，放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040440231V#033F#2P唔，看来是没办法的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3949')
    def lambda_3949():
        ChrTurnDirection(0x0104, 0x0106, 400)
        Yield()

        Jump('lambda_3949')

    DispatchAsync2(0x0104, 0x0001, lambda_3949)

    OP_8E(0x0106, 29900, 0, 31490, 2000, 0x00)
    TerminateThread(0x0104, 0x01)

    ChrTalk(
        0x0101,
        (
            '#0010440232V#1006F辛苦了，阿加特。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440233V放弃不像你的作风嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050440234V#551F#4P别说了……\n',
            '我也这么想。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050440235V#552F……不过，这下\n',
            '后面可没有退路了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060440236V#042F#1P嗯，因为规定是\n',
            '只能放弃一次嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010440237V#1015F啊，对哦……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440238V比想象的更严苛啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4206')

    def _loc_3A9B(): pass

    label('loc_3A9B')

    OP_28(0x0068, 0x01, 0x0004)

    ChrTalk(
        0x0106,
        (
            '#0050440239V#053F#2P啊啊，当然。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050440240V现在就比牌吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000D, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000D,
        (
            '#3130440241V#1P咦……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000D, 0x0106, 400)
    OP_62(0x000D, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(500)

    ChrTalk(
        0x000D,
        (
            '#3130440242V#1P这，这行吗？\n',
            '我手里可是无上的好牌……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0106, 0x000D, 400)
    Sleep(1000)

    ChrTalk(
        0x0106,
        (
            '#0050440243V#050F#2P……说得倒是好听。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050440244V说比就比。\n',
            '别说废话，快决定吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTurnDirection(0x000B, 0x000D, 400)

    ChrTalk(
        0x000B,
        (
            '#3150440245V客人要怎样做？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000D, 0x000B, 400)

    ChrTalk(
        0x000D,
        (
            '#3130440246V#1P唔～怎么办呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3130440247V#1P这手牌要比的话\n',
            '大概也能取胜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlayEffect(0x00, 0x00, 0x0106, 0, 200, 0, 0, 0, 0, 900, 900, 900, 0x00FF, 0, 0, 0, 0)
    Sleep(400)

    OP_22(0x0297, 0x00, 0x64)

    ChrTalk(
        0x0106,
        (
            '#0050440248V#057F#2P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000D, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    ChrTurnDirection(0x000D, 0x0106, 400)

    ChrTalk(
        0x000D,
        (
            '#3130440249V#1P…………行不行！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    OP_D9(0x00, 'CTI00150')
    FadeOut(300, 0, 100)
    OP_22(0x021F, 0x00, 0x64)
    Sleep(2000)

    OP_D9(0x01)
    FadeIn(300, 0)

    @scena.Lambda('lambda_3D55')
    def lambda_3D55():
        ChrTurnDirection(0x000B, 0x000D, 400)
        Yield()

        Jump('lambda_3D55')

    DispatchAsync2(0x000B, 0x0001, lambda_3D55)

    @scena.Lambda('lambda_3D66')
    def lambda_3D66():
        ChrTurnDirection(0x0018, 0x000D, 400)
        Yield()

        Jump('lambda_3D66')

    DispatchAsync2(0x0018, 0x0001, lambda_3D66)

    OP_62(0x000D, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    @scena.Lambda('lambda_3D89')
    def lambda_3D89():
        OP_8F(0x000D, 32392, 0, 28222, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_3D89)

    @scena.Lambda('lambda_3DA4')
    def lambda_3DA4():
        OP_9E(0x00FE, 0x0000001E, 0x00000000, 0x000003E8, 0x00001388)

        ExitThread()

    DispatchAsync(0x000D, 0x0002, lambda_3DA4)

    ChrTalk(
        0x000D,
        (
            '#3130440250V啊啊啊…啊啊啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3130440251V放、放弃！　我放弃！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3130440252V我放弃就是了，饶了我吧！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_82(0x00, 0x02)
    Sleep(500)

    TerminateThread(0x000B, 0x01)
    TerminateThread(0x0018, 0x01)
    ChrTurnDirection(0x0106, 0x000B, 400)
    Sleep(500)

    ChrTalk(
        0x0106,
        (
            '#0050440253V#050F#2P喂，他说放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    OP_62(0x000B, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x000B, 0x0106, 400)

    ChrTalk(
        0x000B,
        (
            '#3150440254V咦！？啊，是哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000B, 0x000D, 400)

    ChrTalk(
        0x000B,
        (
            '#3150440255V那么，菲利奥先生。\n',
            '以后的比赛中就不能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x000D, 0x02, 0x01, 0x0017)

    ChrTalk(
        0x000D,
        (
            '#3130440256V呼，呼…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3130440257V吓、吓死我了～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(1000)
    OP_6D(27210, 0, 33050, 0)
    OP_0D()
    OP_62(0x0101, 0x00000000, 2000, 0x08, 0x09, 0x000000FA, 0x02)
    OP_22(0x000F, 0x00, 0x64)

    ChrTalk(
        0x0101,
        (
            '#0010440258V#1018F好啊，对手放弃了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440259V#1016F不过，与其说是『放弃』，\n',
            '感觉更像是『被迫放弃』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060440260V#041F#1P嘻嘻……\n',
            '真像阿加特的风格。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_401B')
    def lambda_401B():
        ChrTurnDirection(0x0104, 0x0106, 400)
        Yield()

        Jump('lambda_401B')

    DispatchAsync2(0x0104, 0x0001, lambda_401B)

    @scena.Lambda('lambda_402C')
    def lambda_402C():
        ChrTurnDirection(0x000D, 0x0106, 400)
        Yield()

        Jump('lambda_402C')

    DispatchAsync2(0x000D, 0x0001, lambda_402C)

    OP_8E(0x0106, 29900, 0, 31490, 2000, 0x00)
    TerminateThread(0x0104, 0x01)
    TerminateThread(0x000D, 0x01)

    ChrTalk(
        0x0101,
        (
            '#0010440261V#1001F辛苦了，阿加特。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440262V你平时老说『胜负靠气势』\n',
            '果然不是盖的啊～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440263V仅靠气势就赢了牌，\n',
            '真是令人大吃一惊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040440264V#031F#2P唔，这就叫做\n',
            '转败为胜吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050440265V#051F#4P啊啊，算是吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050440266V#050F不过，还不算赢了。\n',
            '之后也要鼓足气势上阵哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060440267V#042F#1P说得也是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060440268V要是对方赢了\n',
            '胜负就定了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040440269V#030F#2P根据不同情况\n',
            '也可能需要激流勇退。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4206(): pass

    label('loc_4206')

    OP_8C(0x000B, 270, 0)
    OP_6D(29690, 0, 31480, 1000)

    ChrTalk(
        0x000B,
        (
            '#3150440270V客人，下一场比赛\n',
            '准备好了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0104, 90, 400)

    ChrTalk(
        0x0104,
        (
            '#0040440271V#033F#2P哦哦，该我上场了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040440272V#035F呼，那么我上了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0106, 0x0104, 400)

    ChrTalk(
        0x0106,
        (
            '#0050440273V#050F#2P啊啊，靠你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0104, 400)

    ChrTalk(
        0x0101,
        (
            '#0010440274V#1009F#1P牛皮都吹过了\n',
            '输了可不饶你哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    TerminateThread(0x000D, 0x02)

    Jump('loc_5D1F')

    def _loc_4323(): pass

    label('loc_4323')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_5D1F',
    )

    Call(2, 0x0006)
    Sleep(400)

    OP_62(0x000D, 0x00000000, 2000, 0x08, 0x09, 0x000000FA, 0x02)
    OP_22(0x000F, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x000D,
        (
            '#3130440198V哟呵呵！\n',
            '起手就是好兆头！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3130440199V呀～这下搞不好\n',
            '能马上拿下一局啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_6D(29690, 0, 31480, 1000)

    ChrTalk(
        0x0105,
        (
            '#0060440277V#040F（菲利奥的情况\n',
            '好像不错呢……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040440201V#035F（哼，如果真是好牌\n',
            '一般应该是沉默的哦。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040440202V#030F（对手要是放弃了\n',
            '是不算赢的。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030440280V#020F（要是那孩子\n',
            '察觉到就好了……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(32073, 0, 31585, 0)
    OP_0D()
    FadeOut(300, 0, 100)
    OP_C5(0x00, 0xFFCE, 0xFFB0, 0x0032, 0x0050, 0x01E3, 0x00F0, 0x0200, 0x0200, 0x0000, 0x0000, 0x0064, 0x00A0, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x01, 0xFFCE, 0xFFB0, 0x0032, 0x0050, 0x01E1, 0x00EE, 0x0200, 0x0200, 0x0000, 0x0000, 0x0064, 0x00A0, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x02, 0xFFCE, 0xFFB0, 0x0032, 0x0050, 0x01DF, 0x00EC, 0x0200, 0x0200, 0x0000, 0x0000, 0x0064, 0x00A0, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x03, 0xFFCE, 0xFFB0, 0x0032, 0x0050, 0x01DD, 0x00EA, 0x0200, 0x0200, 0x0000, 0x0000, 0x0064, 0x00A0, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x04, 0xFFCE, 0xFFB0, 0x0032, 0x0050, 0x01DB, 0x00E8, 0x0200, 0x0200, 0x0000, 0x0000, 0x0064, 0x00A0, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x05, 0xFFCE, 0xFFB0, 0x0032, 0x0050, 0x00A3, 0x00E8, 0x0200, 0x0200, 0x0000, 0x00A0, 0x0064, 0x0140, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x06, 0xFFCE, 0xFFB0, 0x0032, 0x0050, 0x00F3, 0x00EA, 0x0200, 0x0200, 0x0064, 0x0140, 0x00C8, 0x01E0, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x07, 0xFFCE, 0xFFB0, 0x0032, 0x0050, 0x0143, 0x00EC, 0x0200, 0x0200, 0x012C, 0x00A0, 0x0190, 0x0140, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x08, 0xFFCE, 0xFFB0, 0x0032, 0x0050, 0x0193, 0x00EE, 0x0200, 0x0200, 0x012C, 0x0000, 0x0190, 0x00A0, 0x00FFFFFF, 0x00, 'C_VIS229._CH')
    OP_C5(0x09, 0xFFCE, 0xFFB0, 0x0032, 0x0050, 0x01E3, 0x00F0, 0x0200, 0x0200, 0x012C, 0x0000, 0x0190, 0x00A0, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C6(0x05, 0x03, -1, 400, 0)
    OP_C6(0x06, 0x03, -1, 400, 0)
    OP_C6(0x07, 0x03, -1, 400, 0)
    OP_C6(0x08, 0x03, -1, 400, 0)
    OP_C6(0x09, 0x03, -1, 400, 0)
    Sleep(1000)

    SetMessageWindowPos(-1, 320, -1, -1)
    SetChrName('艾丝蒂尔')

    Talk(
        (
            '#0030440281V#1000F（……那么，就这样吧。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030440282V（以大牌为目标换牌，\n',
            '  还是踏实保本……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    ExecExpressionWithReg(
        0x0004,
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
            TXT(0x00, '【只留一个对子换牌】\n'),
            TXT(0x01, '【目标红心同花】\n'),
        ),
    )

    MenuEnd(0x0004)
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
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_47F1',
    )

    SetMessageWindowPos(-1, 320, -1, -1)
    SetChrName('艾丝蒂尔')

    Talk(
        (
            '#0030440283V#1015F（还有续局，\n',
            '  稳妥一点比较合理。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_487B')

    def _loc_47F1(): pass

    label('loc_47F1')

    SetMessageWindowPos(-1, 320, -1, -1)
    SetChrName('艾丝蒂尔')

    Talk(
        (
            '#0030440284V#1015F（还有续局，稳妥一点\n',
            '  似乎比较合理……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030440285V#1002F（就反其道以大牌为目标试试看吧！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_487B(): pass

    label('loc_487B')

    Call(2, 0x0017)
    OP_C7(0x01, 0xFF, 0x00)
    OP_C6(0x00, 0x06, 0, 0, 0)
    OP_C6(0x01, 0x06, 0, 0, 0)
    OP_C6(0x02, 0x06, 0, 0, 0)
    OP_C6(0x03, 0x06, 0, 0, 0)
    OP_C6(0x04, 0x06, 0, 0, 0)
    OP_C6(0x05, 0x06, 0, 0, 0)
    OP_C6(0x06, 0x06, 0, 0, 0)
    OP_C6(0x07, 0x06, 0, 0, 0)
    OP_C6(0x08, 0x06, 0, 0, 0)
    OP_C6(0x09, 0x06, 0, 0, 0)
    FadeIn(300, 0)
    Sleep(1000)

    ChrTurnDirection(0x000B, 0x0101, 400)

    ChrTalk(
        0x000B,
        (
            '#3150440210V要换牌吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_49C9',
    )

    ChrTalk(
        0x0101,
        (
            '#0010440287V#1000F#2P嗯，换３张。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000B, 0x000D, 400)

    ChrTalk(
        0x000B,
        (
            '#3150440212V……客人您呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3130440289V#1P我也换３张。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4A3B')

    def _loc_49C9(): pass

    label('loc_49C9')

    ChrTalk(
        0x0101,
        (
            '#0010440290V#1000F#2P嗯，换２张。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000B, 0x000D, 400)

    ChrTalk(
        0x000B,
        (
            '#3150440212V……客人您呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3130440213V#1P我换３张。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(1000)

    def _loc_4A3B(): pass

    label('loc_4A3B')

    OP_59()
    Call(2, 0x0007)
    OP_59()
    Fade(1000)
    OP_6D(29690, 0, 31480, 0)
    OP_0D()

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4B53',
    )

    ChrTalk(
        0x0105,
        (
            '#0060440293V#040F（艾丝蒂尔……\n',
            '  表情有点明显了。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040440294V#030F（嗯，这种程度\n',
            '  大概还不至于被看穿……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030440295V#025F（不过，万一牌不好\n',
            '  她一定会表现在脸上的。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030440296V（她说自己弱，\n',
            '  这也难怪了。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4CA2')

    def _loc_4B53(): pass

    label('loc_4B53')

    OP_59()
    OP_62(0x0105, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(150)

    OP_62(0x0103, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(100)

    OP_62(0x0104, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(2000)

    ChrTalk(
        0x0105,
        (
            '#0060440297V#045F（艾、艾丝蒂尔……\n',
            '  表情有点过于明显了……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040440298V#031F（唔，要看出艾丝蒂尔\n',
            '  在想什么简直易如反掌。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030440299V#025F（唉，她还说自己弱，\n',
            '  没想到这么离谱。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030440300V（这样怎么可能\n',
            ' 赢得了约修亚嘛。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4CA2(): pass

    label('loc_4CA2')

    OP_62(0x000D, 0x00000000, 2000, 0x0A, 0x0B, 0x000000FA, 0x02)
    OP_22(0x000F, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x000D,
        (
            '#3130440220V#1P呼呼，不错哦～\n',
            '来的就是我要的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000D, 0x0106, 400)

    ChrTalk(
        0x000D,
        (
            '#3130440221V#1P好了、挑战者们。\n',
            '放马过来吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060440303V#045F（菲利奥\n',
            '  也是老样子。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060440304V（到底有几分\n',
            '  是真的呢。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(32073, 0, 31585, 0)
    OP_0D()
    Call(2, 0x0008)
    OP_0D()
    ChrTurnDirection(0x000B, 0x0101, 400)

    ChrTalk(
        0x000B,
        (
            '#3150440224V……要比牌吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_520A',
    )

    OP_28(0x0068, 0x01, 0x0040)

    ChrTalk(
        0x0101,
        (
            '#0010440306V#1007F#2P唔唔，我放弃。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3130440227V#1P咦～要放弃吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3130440228V#1P嗯～难得\n',
            '我凑得一手好牌，真可惜啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3150440229V那么，这边的客人。\n',
            '之后就不能再放弃了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(27210, 0, 33050, 0)
    OP_8C(0x000D, 90, 0)
    OP_0D()

    ChrTalk(
        0x0103,
        (
            '#0030440310V#023F哎呀呀，放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040440311V#030F唔，看来对自己的牌没什么自信啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_4F1D')
    def lambda_4F1D():
        ChrTurnDirection(0x0104, 0x0101, 400)
        Yield()

        Jump('lambda_4F1D')

    DispatchAsync2(0x0104, 0x0001, lambda_4F1D)

    OP_8E(0x0101, 29900, 0, 31490, 2000, 0x00)
    TerminateThread(0x0104, 0x01)

    ChrTalk(
        0x0103,
        (
            '#0030440312V#021F没想到会放弃，\n',
            '还挺成熟的嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030440313V还以为你一定\n',
            '会生气争个输赢呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010440314V#1003F#4P我是很想比啦，\n',
            '不过手气实在是差强人意。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440315V#1007F逞强押下去的话\n',
            '输掉就没办法了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030440316V#027F嗯，这也是一种判断嘛……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030440317V#026F不过，这下\n',
            '就被逼入绝境了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060440236V#042F#1P嗯，因为规定是\n',
            '只能放弃一次嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010440319V#1015F#4P啊，是哦……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440238V比想象的更严重啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x000B, 270, 0)
    OP_6D(29690, 0, 31480, 1000)

    ChrTalk(
        0x000B,
        (
            '#3150440270V客人，下一场比赛\n',
            '准备好了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0104, 90, 400)

    ChrTalk(
        0x0104,
        (
            '#0040440271V#033F#2P哦哦，该我上场了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040440272V#035F呼，那么我上了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x0104, 400)

    ChrTalk(
        0x0103,
        (
            '#0030440324V#020F#1P嗯，我期待着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0104, 400)

    ChrTalk(
        0x0101,
        (
            '#0010440325V#1009F#4P说这种大话\n',
            '输了可不饶你哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()

    Jump('loc_5D1F')

    def _loc_520A(): pass

    label('loc_520A')

    ChrTalk(
        0x0101,
        (
            '#0010440326V#1005F#2P当然了！\n',
            '当然要比。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5794',
    )

    OP_28(0x0068, 0x01, 0x0010)
    OP_62(0x000D, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x000D, 0x0101, 400)
    Sleep(500)

    ChrTalk(
        0x000D,
        (
            '#3130440327V#1P咦！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3130440242V#1P这，这行吗？\n',
            '我手里可是无上的好牌……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x000D, 400)

    ChrTalk(
        0x0101,
        (
            '#0010440329V#1012F#2P是吗，无所谓啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440330V#1028F既然如此，\n',
            '不如趁早放马过来吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000B, 0x000D, 400)

    ChrTalk(
        0x000B,
        (
            '#3150440245V客人要怎样做？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000D, 0x000B, 400)

    ChrTalk(
        0x000D,
        (
            '#3130440246V#1P唔～怎么办呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3130440333V#1P这手牌要比的话\n',
            '倒是不一定输……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3130440334V#1P……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3130440335V#1P……不，我放弃。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3150440255V那么，菲利奥先生。\n',
            '以后的比赛中就不能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x08, 0x09, 0x000000FA, 0x02)
    OP_22(0x000F, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010440337V#1018F#2P好，成功了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(27210, 0, 33050, 0)
    OP_0D()

    @scena.Lambda('lambda_54A2')
    def lambda_54A2():
        ChrTurnDirection(0x0104, 0x0101, 400)
        Yield()

        Jump('lambda_54A2')

    DispatchAsync2(0x0104, 0x0001, lambda_54A2)

    OP_8E(0x0101, 29900, 0, 31490, 2000, 0x00)
    TerminateThread(0x0104, 0x01)

    ChrTalk(
        0x0103,
        (
            '#0030440338V#021F呵呵，看来\n',
            '挺努力的嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060440339V#040F#1P气势强硬看来是走对棋了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010440340V#1001F#4P嗯，总之\n',
            '没输就好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040440341V#031F#2P呼，这就够了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040440342V这下对手\n',
            '就被逼入绝境了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010440343V#1015F#4P啊，是哦……\n',
            '因为只能放弃一次嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440344V#1002F不过，还不算赢了，\n',
            '之后也不可松懈哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060440345V#042F#1P只要对方胜出一次，\n',
            '胜负就定了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030440346V#022F说得对，谨慎地上吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x000B, 270, 0)
    OP_6D(29690, 0, 31480, 1000)

    ChrTalk(
        0x000B,
        (
            '#3150440270V客人，下一场比赛\n',
            '准备好了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0104, 90, 400)

    ChrTalk(
        0x0104,
        (
            '#0040440271V#033F#2P哦哦，该我上场了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040440272V#035F呵，那么我上场了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x0104, 400)

    ChrTalk(
        0x0103,
        (
            '#0030440324V#020F#1P嗯，我期待着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0104, 400)

    ChrTalk(
        0x0101,
        (
            '#0010440325V#1009F#4P说这种大话\n',
            '输了可不饶你哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()

    Jump('loc_5D1F')

    def _loc_5794(): pass

    label('loc_5794')

    OP_28(0x0068, 0x01, 0x0020)
    ChrTurnDirection(0x000D, 0x0101, 400)
    Sleep(500)

    ChrTalk(
        0x000D,
        (
            '#3130440352V#1P嗯～这样好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3130440353V#1P情况好像不太妙，\n',
            '有什么绝招吗……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010440354V#1019F#2P呜…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x000D, 400)

    ChrTalk(
        0x0101,
        (
            '#0010440355V#1022F#2P少说废话，\n',
            '要上就上吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000B, 0x000D, 400)

    ChrTalk(
        0x000B,
        (
            '#3150440245V客人要怎样做？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000D, 0x000B, 400)

    ChrTalk(
        0x000D,
        (
            '#3130440246V#1P唔～怎么办呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3130440333V#1P这手牌要比的话\n',
            '倒是不一定输……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3130440334V#1P……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3130440360V#1P……好，就这样比牌吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010440361V#1020F#2P（惨、惨了……！\n',
            '  竟然将计就计了。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x000B, 270, 0)

    ChrTalk(
        0x000B,
        (
            '#3150440362V那么，从这边的客人开始\n',
            '请展示手牌。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    ChrTurnDirection(0x0101, 0x000B, 400)
    Sleep(1000)

    OP_63(0xFFFF)
    Call(2, 0x0016)
    OP_59()

    ChrTalk(
        0x000B,
        (
            '#3150440363V菲利奥先生赢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3150440364V那么，按照事前的规定，\n',
            '胜负已定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x14, 0x17, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010440365V#1008F#2P啊、呜……………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(27210, 0, 33050, 0)
    OP_8C(0x000D, 90, 0)
    OP_0D()
    OP_62(0x0105, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(150)

    OP_62(0x0103, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(100)

    OP_62(0x0104, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(2000)

    ChrTalk(
        0x0105,
        (
            '#0060440366V#045F#1P输、输了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030440367V#026F……你还真敢乱来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040440368V#031F#2P哈哈哈。\n',
            '哎呀，到底是艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040440369V输得真是豪爽啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    @scena.Lambda('lambda_5BE6')
    def lambda_5BE6():
        OP_6D(29690, 0, 31480, 1000)

        ExitThread()

    DispatchAsync(0x0019, 0x0001, lambda_5BE6)

    SetChrFlags(0x0101, 0x0040)
    OP_8E(0x0101, 32360, 0, 31600, 3000, 0x00)
    OP_8E(0x0101, 32390, 0, 30620, 3000, 0x00)
    ClearChrFlags(0x0101, 0x0040)

    @scena.Lambda('lambda_5C30')
    def lambda_5C30():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_5C30)

    CreateThread(0x000D, 0x02, 0x01, 0x0015)

    ChrTalk(
        0x000D,
        (
            '#3130440370V#1P哇、哇哇！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010440371V#1016F#2P喂、喂！\n',
            '拜托再来１次！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440372V求求你再比１次吧～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030440373V#025F唉，那个大傻瓜……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030440374V太丢人了\n',
            '还是赶快抓回去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    TerminateThread(0x000D, 0x02)
    Sleep(1000)

    Call(1, 0x0012)

    Return()

    def _loc_5D1F(): pass

    label('loc_5D1F')

    FadeOut(2000, 0, -1)
    OP_0D()

    Return()

# id: 0x0003 offset: 0x5D2B
@scena.Code('func_03_5D2B')
def func_03_5D2B():
    OP_4A(0x000B, 255)
    OP_4A(0x000D, 255)
    OP_4A(0x0018, 255)
    ChrTurnDirection(0x0018, 0x000D, 0)
    Sleep(1000)

    OP_6D(32073, 0, 31585, 0)
    SetChrPos(0x0104, 33000, 0, 31870, 135)
    SetChrPos(0x0101, 28570, 0, 31000, 90)
    SetChrPos(0x00F7, 28850, 0, 32500, 90)
    SetChrPos(0x0105, 27670, 0, 31940, 90)
    SetChrPos(0x000D, 32530, 0, 29680, 79)
    FadeIn(2000, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0x000B,
        (
            '#3150440375V那么，开始发放手牌。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(1000)

    Call(2, 0x0009)
    Sleep(400)

    OP_62(0x000D, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1000)

    ChrTalk(
        0x000D,
        (
            '#3130440376V#1P……………我吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3130440377V#1P呀……\n',
            '感觉好像也转运了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3130440378V#1P嗯～…………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_63(0x000D)
    OP_6D(29690, 0, 31480, 1000)

    ChrTalk(
        0x0101,
        (
            '#0010440379V#1002F（好、好像\n',
            '真的很烦恼呢……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060440380V#042F（嗯嗯，表情都不一样了。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_5F2E',
    )

    ChrTalk(
        0x0106,
        (
            '#0050440381V#052F（说不定有什么招。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5F6F')

    def _loc_5F2E(): pass

    label('loc_5F2E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_5F6F',
    )

    ChrTalk(
        0x0103,
        (
            '#0030440382V#022F（应该是真的拿到了\n',
            '  很不错的牌。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5F6F(): pass

    label('loc_5F6F')

    OP_59()
    Fade(1000)
    OP_6D(32073, 0, 31585, 0)
    OP_0D()
    FadeOut(300, 0, 100)
    OP_C5(0x00, 0xFFCE, 0xFFB0, 0x0032, 0x0050, 0x01E3, 0x00F0, 0x0200, 0x0200, 0x0000, 0x0000, 0x0064, 0x00A0, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x01, 0xFFCE, 0xFFB0, 0x0032, 0x0050, 0x01E1, 0x00EE, 0x0200, 0x0200, 0x0000, 0x0000, 0x0064, 0x00A0, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x02, 0xFFCE, 0xFFB0, 0x0032, 0x0050, 0x01DF, 0x00EC, 0x0200, 0x0200, 0x0000, 0x0000, 0x0064, 0x00A0, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x03, 0xFFCE, 0xFFB0, 0x0032, 0x0050, 0x01DD, 0x00EA, 0x0200, 0x0200, 0x0000, 0x0000, 0x0064, 0x00A0, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x04, 0xFFCE, 0xFFB0, 0x0032, 0x0050, 0x01DB, 0x00E8, 0x0200, 0x0200, 0x0000, 0x0000, 0x0064, 0x00A0, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x05, 0xFFCE, 0xFFB0, 0x0032, 0x0050, 0x00A3, 0x00E8, 0x0200, 0x0200, 0x0000, 0x0140, 0x0064, 0x01E0, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x06, 0xFFCE, 0xFFB0, 0x0032, 0x0050, 0x00F3, 0x00EA, 0x0200, 0x0200, 0x00C8, 0x0000, 0x012C, 0x00A0, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x07, 0xFFCE, 0xFFB0, 0x0032, 0x0050, 0x0143, 0x00EC, 0x0200, 0x0200, 0x0190, 0x0000, 0x01F4, 0x00A0, 0x00FFFFFF, 0x00, 'C_VIS229._CH')
    OP_C5(0x08, 0xFFCE, 0xFFB0, 0x0032, 0x0050, 0x0193, 0x00EE, 0x0200, 0x0200, 0x0064, 0x0000, 0x00C8, 0x00A0, 0x00FFFFFF, 0x00, 'C_VIS229._CH')
    OP_C5(0x09, 0xFFCE, 0xFFB0, 0x0032, 0x0050, 0x01E3, 0x00F0, 0x0200, 0x0200, 0x00C8, 0x0140, 0x012C, 0x01E0, 0x00FFFFFF, 0x00, 'C_VIS229._CH')
    OP_C6(0x05, 0x03, -1, 400, 0)
    OP_C6(0x06, 0x03, -1, 400, 0)
    OP_C6(0x07, 0x03, -1, 400, 0)
    OP_C6(0x08, 0x03, -1, 400, 0)
    OP_C6(0x09, 0x03, -1, 400, 0)
    Sleep(1000)

    SetMessageWindowPos(-1, 320, -1, -1)
    SetChrName('奥利维尔')

    Talk(
        (
            '#0040440383V#030F（那么、怎么办。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040440384V（直接进攻呢，\n',
            '  还是迷惑对手……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040440385V（呵呵，两种看起来都很有趣。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    ExecExpressionWithReg(
        0x0004,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0004,
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
            TXT(0x00, '【保留对子其余交换】\n'),
            TXT(0x01, '【保留对子只换一张】\n'),
        ),
    )

    MenuEnd(0x0004)
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
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_62F2',
    )

    SetMessageWindowPos(-1, 320, -1, -1)
    SetChrName('奥利维尔')

    Talk(
        (
            '#0040440386V#030F（嗯，那么……\n',
            '  还是老老实实上吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_633F')

    def _loc_62F2(): pass

    label('loc_62F2')

    SetMessageWindowPos(-1, 320, -1, -1)
    SetChrName('奥利维尔')

    Talk(
        (
            '#0040440387V#030F（嗯，那么……\n',
            '  还是迂回看看吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_633F(): pass

    label('loc_633F')

    Call(2, 0x0017)
    OP_C7(0x01, 0xFF, 0x00)
    OP_C6(0x00, 0x06, 0, 0, 0)
    OP_C6(0x01, 0x06, 0, 0, 0)
    OP_C6(0x02, 0x06, 0, 0, 0)
    OP_C6(0x03, 0x06, 0, 0, 0)
    OP_C6(0x04, 0x06, 0, 0, 0)
    OP_C6(0x05, 0x06, 0, 0, 0)
    OP_C6(0x06, 0x06, 0, 0, 0)
    OP_C6(0x07, 0x06, 0, 0, 0)
    OP_C6(0x08, 0x06, 0, 0, 0)
    OP_C6(0x09, 0x06, 0, 0, 0)
    FadeIn(300, 0)
    Sleep(1000)

    ChrTurnDirection(0x000B, 0x0104, 400)

    ChrTalk(
        0x000B,
        (
            '#3150440210V要换牌吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_648E',
    )

    ChrTalk(
        0x0104,
        (
            '#0040440389V#030F#2P嗯，麻烦换３张。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000B, 0x000D, 400)

    ChrTalk(
        0x000B,
        (
            '#3150440212V……客人您呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3130440391V#1P我换２张。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6500')

    def _loc_648E(): pass

    label('loc_648E')

    ChrTalk(
        0x0104,
        (
            '#0040440392V#030F#2P只换１张，麻烦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000B, 0x000D, 400)

    ChrTalk(
        0x000B,
        (
            '#3150440212V……客人您呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3130440391V#1P我换２张。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6500(): pass

    label('loc_6500')

    OP_59()
    Call(2, 0x000A)
    OP_59()
    Fade(1000)
    OP_6D(29690, 0, 31480, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010440395V#1002F（嗯～那表情……\n',
            '　完全看不透。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440396V（奥利维尔那家伙\n',
            '　在想什么呢……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060440397V#040F（呵呵，那也算是\n',
            '　一种扑克脸呢。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000D, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1000)

    OP_63(0x000D)

    ChrTalk(
        0x000D,
        (
            '#3130440398V#1P……好…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3130440399V#1P嗯，没问题了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_6689',
    )

    ChrTalk(
        0x0106,
        (
            '#0050440400V#555F（和刚才不同，\n',
            '　很保守的反应嘛。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050440401V（……拿到大牌了吗？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_66F0')

    def _loc_6689(): pass

    label('loc_6689')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_66F0',
    )

    ChrTalk(
        0x0103,
        (
            '#0030440402V#022F（和刚才不同，\n',
            '　非常保守的反应呢。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030440403V（会是拿到大牌了吗？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_66F0(): pass

    label('loc_66F0')

    OP_59()
    Fade(1000)
    OP_6D(32073, 0, 31585, 0)
    OP_0D()
    Call(2, 0x0014)
    OP_0D()
    ChrTurnDirection(0x000B, 0x0104, 400)

    ChrTalk(
        0x000B,
        (
            '#3150440224V……要比牌吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_71D9',
    )

    OP_28(0x0068, 0x01, 0x0100)

    ChrTalk(
        0x0104,
        (
            '#0040440405V#031F#2P呼，我放弃了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040440406V因为『退却』也是出色的战略嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3130440407V#1P可恶，放弃了吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0104, 0x000D, 400)

    ChrTalk(
        0x0104,
        (
            '#0040440408V#033F#2P哎呀？看起来很懊恼嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040440409V#031F要是浪费了\n',
            '你难得的好牌，我道歉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000D, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrTurnDirection(0x000D, 0x0104, 400)
    Sleep(400)

    ChrTalk(
        0x000D,
        (
            '#3130440410V#1P哪、哪里，也没什么懊恼的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3130440411V#1P我这里的牌\n',
            '也不是太好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3150440412V那么，这下这边的客人\n',
            '之后也不能再放弃了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(28820, 0, 31840, 0)
    OP_8C(0x000D, 90, 0)
    OP_8C(0x000B, 270, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010440413V#1004F哎呀呀，放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_6971',
    )

    ChrTalk(
        0x0106,
        (
            '#0050440414V#050F#2P看来是感觉对方的牌比较好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_69B1')

    def _loc_6971(): pass

    label('loc_6971')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_69B1',
    )

    ChrTalk(
        0x0103,
        (
            '#0030440415V#020F#2P嗯～看来\n',
            '是觉得对方比较有希望。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_69B1(): pass

    label('loc_69B1')

    @scena.Lambda('lambda_69B7')
    def lambda_69B7():
        ChrTurnDirection(0x00F7, 0x0104, 400)
        Yield()

        Jump('lambda_69B7')

    DispatchAsync2(0x00F7, 0x0001, lambda_69B7)

    OP_8E(0x0104, 29900, 0, 31490, 2000, 0x00)
    TerminateThread(0x00F7, 0x01)

    ChrTalk(
        0x0104,
        (
            '#0040440416V#031F#4P嗨，各位⊙',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040440417V呼呼，看到了吗？\n',
            '我那冷静的思考。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010440418V#1015F不过，菲利奥\n',
            '的手牌真那么好？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440419V要是比了的话\n',
            '说不定就赢了嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040440420V#035F#4P呼，十之八九是不会错的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040440421V要是比了的话，\n',
            '此时我们就在泪海里游泳了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010440422V#1016F少～来，又夸大其辞。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060440423V#040F#1P不过，这下\n',
            '双方各放弃一次了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_6FA6',
    )

    ChrTalk(
        0x0106,
        (
            '#0050440424V#050F#2P啊啊，没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050440425V下场胜负\n',
            '就是关键了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010440426V#1002F嗯，是啊……我说。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440427V#1004F下场胜负\n',
            '那不就是我上场！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0106, 0x0101, 400)

    ChrTalk(
        0x0106,
        (
            '#0050440428V#555F#2P事到如今还迷糊什么呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040440429V#030F#4P加油哦，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040440430V我也会\n',
            '在背后支持你的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010440431V#1016F支、支持有什么用……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440432V#1015F又不是支持我\n',
            '就能抽到好牌。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040440433V#031F#4P呵呵，这～可难说了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010440434V#1019F什、什么啦？\n',
            '话里有话的样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040440435V#032F#4P艾丝蒂尔，\n',
            '我有一言相劝……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040440436V与其为选牌而困惑，\n',
            '不如全部扔掉的好哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040440437V#031F喏，俗话不是这么说的吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040440438V『与其重新涂奶油\n',
            '  不如重新烤蛋糕』嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010440439V#1007F没、没听说过啦，\n',
            '哪有这么奇怪的俗话。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440440V#1002F不过，为什么\n',
            '这么说？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040440441V#031F#4P不，只是直觉。\n',
            '觉得这样比较好～的样子嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x000B, 270, 0)
    OP_6D(29690, 0, 31480, 1000)

    ChrTalk(
        0x000B,
        (
            '#3150440442V客人，到最后一局了。\n',
            '准备好了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050440443V#050F#2P喂，看来差不多到时间了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040440444V#031F#4P呼，那么祝你好运。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010440445V#1011F呜，嗯…………\n',
            '#1015F（真令人介意～）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_71B3')

    def _loc_6FA6(): pass

    label('loc_6FA6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_71B3',
    )

    ChrTalk(
        0x0103,
        (
            '#0030440446V#026F#2P嗯嗯，就是这样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030440447V下场胜负\n',
            '好好做个了结吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010440448V#1011F接着轮到雪拉姐了吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440449V#1001F嗯⊙感觉\n',
            '好像赢得了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030440450V#027F是就好了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030440451V不过，这个\n',
            '就要看空之女神的意思了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x000B, 270, 0)
    OP_6D(29690, 0, 31480, 1000)

    ChrTalk(
        0x000B,
        (
            '#3150440442V客人，到最后的比赛了。\n',
            '准备好了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040440453V#030F#4P嗯，看来到时间了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0104, 0x0103, 400)

    ChrTalk(
        0x0104,
        (
            '#0040440454V#030F#4P那么，雪拉。\n',
            '就让我们见识一下你的手腕吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x0104, 400)

    ChrTalk(
        0x0103,
        (
            '#0030440455V#021F呵呵……\n',
            '希望能让你满意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_71B3(): pass

    label('loc_71B3')

    FadeOut(2000, 0, -1)
    OP_0D()
    SetChrPos(0x000D, 32398, 0, 30463, 90)
    OP_8C(0x000B, 270, 0)

    Jump('loc_7972')

    def _loc_71D9(): pass

    label('loc_71D9')

    ChrTalk(
        0x0104,
        (
            '#0040440456V#031F#2P哼，当然了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040440457V我的辞典里\n',
            '可没有『退却』两字。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000B, 0x000D, 400)

    ChrTalk(
        0x000B,
        (
            '#3150440245V客人要怎样做？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3130440459V#1P啊啊，我接受。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000B, 0x0104, 400)

    ChrTalk(
        0x000B,
        (
            '#3150440362V那么，从这边的客人开始\n',
            '请展示手牌。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()
    Call(2, 0x0015)
    OP_59()

    ChrTalk(
        0x000B,
        (
            '#3150440363V菲利奥先生赢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3150440364V那么，按照事前的规定，\n',
            '胜负已定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0104,
        (
            '#0040440463V#035F#2P呵呵，胜败乃时运。\n',
            '若是败北也没有办法……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040440464V#031F可、可是，难道是错觉？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040440465V从刚才开始背后\n',
            '就一直感到一股异样的压力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(27210, 0, 33050, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010440466V#1009F#1P那、那个三流音乐家～～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440467V奥利维尔～你\n',
            '心知肚明的～吧～～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0101, 400)

    ChrTalk(
        0x0105,
        (
            '#0060440468V#045F#1P艾、艾丝蒂尔，冷静点。',
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
        'loc_75F8',
    )

    ChrTalk(
        0x0106,
        (
            '#0050440469V#053F#2P你还好意思说。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050440470V开始前，拼命发牢骚的\n',
            '到底是谁？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010440471V#1019F#1P呜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050440472V#057F#2P我们之所以会输\n',
            '又不光是那家伙的错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050440473V有空起内讧，\n',
            '还不如考虑一下怎么对委托人解释。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x00F7, 400)

    ChrTalk(
        0x0101,
        (
            '#0010440474V#1007F#1P是、是哦……\n',
            '工作失败了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440475V唉，没脸\n',
            '去见委托人了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7957')

    def _loc_75F8(): pass

    label('loc_75F8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_7957',
    )

    ChrTurnDirection(0x0103, 0x0101, 400)

    If(
        (
            (Expr.Eval, "OP_29(0x0068, 0x01, 0x0008)"),
            (Expr.Eval, "OP_29(0x0068, 0x01, 0x0040)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_77D8',
    )

    ChrTalk(
        0x0103,
        (
            '#0030440476V#027F#2P哎呀，艾丝蒂尔。\n',
            '你有立场这么说吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030440477V你不是也\n',
            '首战就放弃了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010440471V#1019F#1P呜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030440479V#025F#2P正因为你那时候放弃了，\n',
            '现在才不得不比的哦？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030440480V你自己也有一半的原因，\n',
            '就别胡乱指责别人了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010440481V#1007F#1P知、知道啦。\n',
            '我知道了啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440482V唉，话说回来\n',
            '该怎么向委托人道歉才好呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440483V#1014F啊～早知这样\n',
            '当时就比了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7957')

    def _loc_77D8(): pass

    label('loc_77D8')

    ChrTalk(
        0x0103,
        (
            '#0030440484V#027F#2P哎呀，艾丝蒂尔。\n',
            '你有立场这么说吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030440485V开始之前，是谁说\n',
            '不会打牌的啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010440471V#1019F#1P呜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030440487V#026F#2P我们会输\n',
            '并不仅是奥利维尔的原因。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030440488V有空发牢骚，\n',
            '还不如考虑一下怎么对委托人解释。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010440474V#1007F#1P是、是哦……\n',
            '工作失败了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440475V唉，没脸\n',
            '去见委托人了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7957(): pass

    label('loc_7957')

    OP_28(0x0068, 0x01, 0x0080)
    FadeOut(2000, 0, -1)
    OP_0D()
    Sleep(1000)

    Call(1, 0x0012)

    Return()

    def _loc_7972(): pass

    label('loc_7972')

    OP_6D(32073, 0, 31585, 0)
    SetChrPos(0x0105, 27670, 0, 31940, 90)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_79D1',
    )

    SetChrPos(0x0101, 33000, 0, 31870, 135)
    SetChrPos(0x00F7, 28570, 0, 31000, 90)
    SetChrPos(0x0104, 28850, 0, 32500, 90)

    Jump('loc_7A0B')

    def _loc_79D1(): pass

    label('loc_79D1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_7A0B',
    )

    SetChrPos(0x00F7, 33000, 0, 31870, 135)
    SetChrPos(0x0104, 28850, 0, 32500, 90)
    SetChrPos(0x0101, 28570, 0, 31000, 90)

    def _loc_7A0B(): pass

    label('loc_7A0B')

    SetChrPos(0x000D, 32530, 0, 29680, 79)
    FadeIn(2000, 0)
    OP_0D()

    Return()

# id: 0x0004 offset: 0x7A27
@scena.Code('func_04_7A27')
def func_04_7A27():
    Sleep(1000)

    ChrTalk(
        0x000B,
        (
            '#3150440491V两位都准备好了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3150440492V那么，开始最后一局了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(1000)

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_98DB',
    )

    Call(2, 0x000B)
    OP_59()
    Sleep(400)

    ChrTurnDirection(0x0101, 0x000D, 400)

    ChrTalk(
        0x0101,
        (
            '#0010440493V#1002F#2P（菲利奥的\n',
            '情况怎样？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(1, 0x0018)
    OP_62(0x0105, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(150)

    OP_62(0x0106, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(100)

    OP_62(0x0104, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    OP_6D(29690, 0, 31480, 1000)

    ChrTalk(
        0x0105,
        (
            '#0060440494V#045F（看、看起来\n',
            '  情况很古怪。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050440495V#050F（啊啊，好像转运了。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040440496V#030F（来吧，艾丝蒂尔该怎么办呢。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040440497V（要是我刚刚的意思\n',
            '  她能听懂就好了。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(32073, 0, 31585, 0)
    OP_0D()
    FadeOut(300, 0, 100)
    OP_C5(0x00, 0xFFCE, 0xFFB0, 0x0032, 0x0050, 0x01E3, 0x00F0, 0x0200, 0x0200, 0x0000, 0x0000, 0x0064, 0x00A0, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x01, 0xFFCE, 0xFFB0, 0x0032, 0x0050, 0x01E1, 0x00EE, 0x0200, 0x0200, 0x0000, 0x0000, 0x0064, 0x00A0, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x02, 0xFFCE, 0xFFB0, 0x0032, 0x0050, 0x01DF, 0x00EC, 0x0200, 0x0200, 0x0000, 0x0000, 0x0064, 0x00A0, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x03, 0xFFCE, 0xFFB0, 0x0032, 0x0050, 0x01DD, 0x00EA, 0x0200, 0x0200, 0x0000, 0x0000, 0x0064, 0x00A0, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x04, 0xFFCE, 0xFFB0, 0x0032, 0x0050, 0x01DB, 0x00E8, 0x0200, 0x0200, 0x0000, 0x0000, 0x0064, 0x00A0, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x05, 0xFFCE, 0xFFB0, 0x0032, 0x0050, 0x00A3, 0x00E8, 0x0200, 0x0200, 0x0190, 0x0000, 0x01F4, 0x00A0, 0x00FFFFFF, 0x00, 'C_VIS229._CH')
    OP_C5(0x06, 0xFFCE, 0xFFB0, 0x0032, 0x0050, 0x00F3, 0x00EA, 0x0200, 0x0200, 0x0000, 0x00A0, 0x0064, 0x0140, 0x00FFFFFF, 0x00, 'C_VIS229._CH')
    OP_C5(0x07, 0xFFCE, 0xFFB0, 0x0032, 0x0050, 0x0143, 0x00EC, 0x0200, 0x0200, 0x012C, 0x0000, 0x0190, 0x00A0, 0x00FFFFFF, 0x00, 'C_VIS229._CH')
    OP_C5(0x08, 0xFFCE, 0xFFB0, 0x0032, 0x0050, 0x0193, 0x00EE, 0x0200, 0x0200, 0x0064, 0x0140, 0x00C8, 0x01E0, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x09, 0xFFCE, 0xFFB0, 0x0032, 0x0050, 0x01E3, 0x00F0, 0x0200, 0x0200, 0x00C8, 0x0000, 0x012C, 0x00A0, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C6(0x05, 0x03, -1, 400, 0)
    OP_C6(0x06, 0x03, -1, 400, 0)
    OP_C6(0x07, 0x03, -1, 400, 0)
    OP_C6(0x08, 0x03, -1, 400, 0)
    OP_C6(0x09, 0x03, -1, 400, 0)
    Sleep(1000)

    ChrTurnDirection(0x0101, 0x000B, 0)
    SetMessageWindowPos(-1, 320, -1, -1)
    SetChrName('艾丝蒂尔')

    Talk(
        (
            '#0010440498V#1002F（不妙啊……\n',
            '  菲利奥看来形势大好。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440499V（即使凑成同花\n',
            '  说不定对方还有更厉害的。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440500V#1015F（话虽如此，除了同花\n',
            '  也没别的牌好凑……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440501V#1022F（啊～真像奥利维尔说的，\n',
            '  简直想全部扔掉换牌了。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    ExecExpressionWithReg(
        0x0004,
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
            TXT(0x00, '【目标方块同花】\n'),
            TXT(0x01, '【交换全部手牌】\n'),
        ),
    )

    MenuEnd(0x0004)
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
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_803A',
    )

    SetMessageWindowPos(-1, 320, -1, -1)
    SetChrName('艾丝蒂尔')

    Talk(
        (
            '#0010440502V#1007F（嗯、可是孤注一掷的话\n',
            '  无疑也是最佳选择哦。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440503V（无谓的强求也没什么意义。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_80D9')

    def _loc_803A(): pass

    label('loc_803A')

    SetMessageWindowPos(-1, 320, -1, -1)
    SetChrName('艾丝蒂尔')

    Talk(
        (
            '#0010440504V#1002F（即使完成了同花，\n',
            '  最后输了也没有意义。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440505V#1007F（嗯……这里就孤注一掷\n',
            '  试着遵从奥利维尔的意见吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_80D9(): pass

    label('loc_80D9')

    Call(2, 0x0017)
    OP_C7(0x01, 0xFF, 0x00)
    OP_C6(0x00, 0x06, 0, 0, 0)
    OP_C6(0x01, 0x06, 0, 0, 0)
    OP_C6(0x02, 0x06, 0, 0, 0)
    OP_C6(0x03, 0x06, 0, 0, 0)
    OP_C6(0x04, 0x06, 0, 0, 0)
    OP_C6(0x05, 0x06, 0, 0, 0)
    OP_C6(0x06, 0x06, 0, 0, 0)
    OP_C6(0x07, 0x06, 0, 0, 0)
    OP_C6(0x08, 0x06, 0, 0, 0)
    OP_C6(0x09, 0x06, 0, 0, 0)
    FadeIn(300, 0)
    Sleep(1000)

    ChrTurnDirection(0x000B, 0x0101, 400)

    ChrTalk(
        0x000B,
        (
            '#3150440210V要换牌吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_88EA',
    )

    ChrTalk(
        0x0101,
        (
            '#0010440507V#1002F#2P嗯，换２张。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000B, 0x000D, 400)

    ChrTalk(
        0x000B,
        (
            '#3150440212V……客人您呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3130440509V#1P哦，我只换１张。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()
    Call(2, 0x000C)
    OP_59()
    Fade(1000)
    OP_6D(29690, 0, 31480, 0)
    OP_0D()
    OP_62(0x0105, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    ChrTalk(
        0x0105,
        (
            '#0060440510V#040F（啊，艾丝蒂尔\n',
            '  似乎也转运了。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040440511V#030F#2P（那个表情看来\n',
            '  好像是相当不错的牌……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040440512V#034F（不过，居然连我们\n',
            '  旁观者都如此一目了然。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040440513V（艾丝蒂尔的表情\n',
            '  简直像手旗信号一样嘛。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050440514V#551F（虽然她早说过不擅长玩牌，\n',
            '  我看问题可不在这里……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(1000)
    OP_6D(32073, 0, 31585, 0)
    OP_0D()
    Call(1, 0x0011)
    OP_59()
    Call(2, 0x0013)
    OP_59()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    ChrTurnDirection(0x0101, 0x000D, 400)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010440515V#1020F#2P同、同花大顺什么的……咦！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440516V那不是最强的牌吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(29690, 0, 31480, 0)
    OP_0D()

    ChrTalk(
        0x0106,
        (
            '#0050440517V#055F喂、喂喂……\n',
            '怎么偏偏是那个啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050440518V那种牌一般怎么可能凑得出来啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060440519V#042F真的比不过……了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040440520V#031F哈哈哈。\n',
            '这实在是束手无策了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(32073, 0, 31585, 0)
    OP_0D()
    ChrTurnDirection(0x000B, 0x0101, 400)

    ChrTalk(
        0x000B,
        (
            '#3150440521V……客人也请开牌。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3150440522V不展示手牌的话，\n',
            '胜负是不清楚的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0101, 135, 400)

    ChrTalk(
        0x0101,
        (
            '#0010440523V#1016F#2P不、不过，这次\n',
            '已经是一目了然了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(2, 0x0010)
    OP_59()

    ChrTalk(
        0x000B,
        (
            '#3150440524V唔，确实……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x000B, 270, 400)

    ChrTalk(
        0x000B,
        (
            '#3150440525V那么这次比赛───\n',
            '菲利奥先生赢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3130440526V#1P哈哈哈。\n',
            '哎呀～这是当然的结果嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3130440527V#1P你们也很努力了\n',
            '就是选错了对手。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(27210, 0, 33050, 0)
    OP_8C(0x000D, 90, 0)
    OP_0D()

    ChrTalk(
        0x0105,
        (
            '#0060440528V#043F#5P唉，输了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040440529V#030F#2P唔～真可惜啊。\n',
            '就差一口气了嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050440530V#053F#1P唉，对手运气太好也没办法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_874E')
    def lambda_874E():
        ChrTurnDirection(0x0104, 0x0101, 400)
        Yield()

        Jump('lambda_874E')

    DispatchAsync2(0x0104, 0x0001, lambda_874E)

    OP_8E(0x0101, 29900, 0, 31490, 2000, 0x00)
    TerminateThread(0x0104, 0x01)

    ChrTalk(
        0x0101,
        (
            '#0010440531V#1007F#4P抱歉，输了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050440532V#050F#1P别跟我们道歉啊。\n',
            '输了是全体人员的责任。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050440533V要道歉的话，\n',
            '就去对这件工作的委托人道歉吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010440534V#1003F#4P是、是哦……\n',
            '工作失败了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440535V#1007F唉，没脸见人了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050440536V#552F#1P啊啊，话虽如此\n',
            '还是必须去见的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050440537V……这是游击士职业的尊严啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    Sleep(1000)

    OP_28(0x0068, 0x01, 0x0200)
    Call(1, 0x0012)

    Return()

    def _loc_88EA(): pass

    label('loc_88EA')

    ChrTalk(
        0x0101,
        (
            '#0010440538V#1002F#2P嗯…………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440539V#1007F……５张全换哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3150440540V…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_895F')
    def lambda_895F():
        ChrTurnDirection(0x0101, 0x0104, 400)
        Yield()

        Jump('lambda_895F')

    DispatchAsync2(0x0101, 0x0001, lambda_895F)

    ChrTalk(
        0x0101,
        (
            '#0010440541V#1009F#2P（看，照你说的做了啦。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040440542V#031F（呼呼，判断得好。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0104, 0x01, 0x01, 0x000E)
    ChrTurnDirection(0x000B, 0x000D, 400)

    ChrTalk(
        0x000B,
        (
            '#3150440543V……那么，客人呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3130440509V#1P哦，我只换１张。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0104, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010440545V#1002F#2P（……想，想干什么？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040440546V#035F#2P（呼…………）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()
    FadeOut(300, 0, 100)
    OP_D9(0x00, 'CTI00130')
    OP_22(0x021F, 0x00, 0x64)
    Sleep(2000)

    OP_D9(0x01)
    FadeIn(300, 0)
    Sleep(400)

    OP_62(0x0104, 0x00000000, 2000, 0x0A, 0x0B, 0x000000FA, 0x02)
    OP_22(0x000F, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0104,
        (
            '#0040440547V#035F#2P……呼～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '奥利维尔朝发牌者的耳朵吹了口气。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_0D()
    OP_9E(0x000B, 0x0000000F, 0x00000000, 0x0000012C, 0x00001388)
    OP_62(0x000B, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    CreateThread(0x000B, 0x01, 0x01, 0x0010)

    ChrTalk(
        0x000B,
        (
            '#3150440548V呜，呜哇啊啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x000B, 0x0001)

    ChrTalk(
        0x000B,
        (
            '#3150440549V您、您干什么呢！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040440550V#031F#2P哈哈哈，失礼了。\n',
            '哎呀，不觉得紧张得受不了了嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040440551V只是稍微打个岔，\n',
            '缓和一下气氛嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0105, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(100)

    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    OP_62(0x00F7, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(100)

    ChrTurnDirection(0x000D, 0x0104, 400)
    OP_62(0x000D, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    OP_62(0x000A, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    OP_62(0x0018, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(500)

    OP_9E(0x0101, 0x0000000F, 0x00000000, 0x000005DC, 0x00001388)

    ChrTalk(
        0x0101,
        (
            '#0010440552V#1022F#2P（那、那个呆子～～～～～！！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3150440553V那你已经达到目的了吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3150440554V好了，快下去！\n',
            '游戏都进行不下去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040440555V#030F#2P呼，那么打扰了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0104, 0x01, 0x01, 0x000F)
    Sleep(2000)

    ChrTalk(
        0x0101,
        (
            '#0010440556V#1009F#2P（………………～～唔！！）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440557V（呜～相信那呆子的我\n',
            '  也真够蠢的。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0x01)
    OP_8E(0x000B, 35010, 0, 30340, 2000, 0x00)
    OP_8C(0x000B, 270, 400)
    Sleep(500)

    ChrTalk(
        0x000B,
        (
            '#3150440558V那、那么，回到正题……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000B, 0x0101, 400)

    ChrTalk(
        0x000B,
        (
            '#3150440559V……客人是换５张？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_8E94')
    def lambda_8E94():
        ChrTurnDirection(0x0018, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_8E94)

    ChrTurnDirection(0x0101, 0x000B, 400)

    ChrTalk(
        0x0101,
        (
            '#0010440560V#1007F#2P呜呜……是啦………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x000B, 270, 400)

    ChrTalk(
        0x000B,
        (
            '#3150440561V那，我是１张……好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000D, 0x000B, 400)

    ChrTalk(
        0x000D,
        (
            '#3130440562V#1P呼呼呼……\n',
            '好，来吧～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(1, 0x0011)
    OP_59()
    Call(2, 0x0013)
    OP_59()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    ChrTurnDirection(0x0101, 0x000D, 400)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010440515V#1020F#2P同、同花大顺什么的……咦！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440516V那不是最强的牌吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(29690, 0, 31480, 0)
    OP_0D()

    ChrTalk(
        0x0106,
        (
            '#0050440565V#052F喂、喂喂……\n',
            '怎么偏偏是那个啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050440518V那种牌一般怎么可能凑得出来啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060440519V#042F穷途末路……了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040440568V#035F呼呼……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040440569V这～个嘛，可难说哦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060211097V#044F咦……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(32073, 0, 31585, 0)
    OP_0D()
    ChrTurnDirection(0x000B, 0x0101, 400)

    ChrTalk(
        0x000B,
        (
            '#3150440521V……客人也请开牌。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3150440522V不展示手牌的话，\n',
            '胜负是不清楚的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0101, 135, 400)

    ChrTalk(
        0x0101,
        (
            '#0010440573V#1007F#2P……好好，开牌了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440574V不过，面对那种手牌\n',
            '开牌也没什么意义了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(2, 0x0012)
    OP_59()

    ChrTalk(
        0x000B,
        (
            '#3150440575V……确实没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3150440576V而且，还是黑桃……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3150440577V唔，那么这边的牌\n',
            '比菲利奥先生的更大。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000D, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000D,
        (
            '#3130440578V#1P骗、骗人的吧！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3150440579V这场比赛───\n',
            '是各位赢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x000D, 0x01, 0x01, 0x0017)

    ChrTalk(
        0x0101,
        (
            '#0010440580V#1004F#2P赢、赢了……！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440581V赢了！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)

    @scena.Lambda('lambda_92E8')
    def lambda_92E8():
        OP_95(0x0101, 0x00000000, 0x000003E8, 0x00000000, 0x000003E8, 0x00001B58)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_92E8)

    ExecExpressionWithValue(
        0x0101,
        0x04,
        (
            (Expr.PushLong, 0x1E),
            Expr.Add2,
            Expr.Return,
        ),
    )

    Sleep(24)

    ExecExpressionWithValue(
        0x0101,
        0x04,
        (
            (Expr.PushLong, 0x1E),
            Expr.Add2,
            Expr.Return,
        ),
    )

    Sleep(24)

    ExecExpressionWithValue(
        0x0101,
        0x04,
        (
            (Expr.PushLong, 0x1E),
            Expr.Add2,
            Expr.Return,
        ),
    )

    Sleep(24)

    ExecExpressionWithValue(
        0x0101,
        0x04,
        (
            (Expr.PushLong, 0x1E),
            Expr.Add2,
            Expr.Return,
        ),
    )

    Sleep(24)

    ExecExpressionWithValue(
        0x0101,
        0x04,
        (
            (Expr.PushLong, 0x1E),
            Expr.Add2,
            Expr.Return,
        ),
    )

    Sleep(24)

    ExecExpressionWithValue(
        0x0101,
        0x04,
        (
            (Expr.PushLong, 0x1E),
            Expr.Add2,
            Expr.Return,
        ),
    )

    Sleep(24)

    ExecExpressionWithValue(
        0x0101,
        0x04,
        (
            (Expr.PushLong, 0x1E),
            Expr.Add2,
            Expr.Return,
        ),
    )

    Sleep(24)

    ExecExpressionWithValue(
        0x0101,
        0x04,
        (
            (Expr.PushLong, 0x1E),
            Expr.Add2,
            Expr.Return,
        ),
    )

    Sleep(24)

    ExecExpressionWithValue(
        0x0101,
        0x04,
        (
            (Expr.PushLong, 0x1E),
            Expr.Add2,
            Expr.Return,
        ),
    )

    Sleep(24)

    ExecExpressionWithValue(
        0x0101,
        0x04,
        (
            (Expr.PushLong, 0x1E),
            Expr.Add2,
            Expr.Return,
        ),
    )

    Sleep(24)

    ExecExpressionWithValue(
        0x0101,
        0x04,
        (
            (Expr.PushLong, 0x1E),
            Expr.Add2,
            Expr.Return,
        ),
    )

    Sleep(24)

    ExecExpressionWithValue(
        0x0101,
        0x04,
        (
            (Expr.PushLong, 0x1E),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ChrTalk(
        0x0101,
        (
            '#0010440582V#1001F#3S#2P呀呵～～赢了！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()
    CreateThread(0x0101, 0x01, 0x01, 0x0016)

    ChrTalk(
        0x000B,
        (
            '#3150440583V……这是赌金。\n',
            '请确认。',
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
            '得到了',
            (TxtCtl.SetColor, 0x4),
            '２０００',
            (TxtCtl.SetColor, 0x0),
            '米拉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    Fade(1000)
    OP_6D(27210, 0, 33050, 0)
    OP_0D()

    ChrTalk(
        0x0105,
        (
            '#0060440584V#044F#5P赢、赢了哦……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040440585V#031F哈哈哈。\n',
            '简直是大逆转呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0106, 0x0104, 400)

    ChrTalk(
        0x0106,
        (
            '#0050440586V#057F#1P……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0104, 0x0106, 400)
    Sleep(1000)

    ChrTalk(
        0x0104,
        (
            '#0040440587V#031F怎、怎么了？阿加特兄。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050440588V#053F#1P……哼，原来如此啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050440589V怪不得会做出\n',
            '那种可疑的举动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040440590V#031F哈哈，你说什～么呀？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050440591V#551F#1P算了……\n',
            '就当没看见吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050440592V因为这次就是\n',
            '靠那个才赢的嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040440593V#030F呵呵……\n',
            '能帮上忙是我的荣幸。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_63(0x0101)
    TerminateThread(0x0101, 0x01)
    OP_8E(0x0101, 29900, 0, 31490, 2000, 0x00)

    ChrTalk(
        0x0101,
        (
            '#0010440594V#1001F#4P嘿嘿～久等了～⊙',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440595V好了，赶快去报告…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010440596V#1019F#4P你、你们两个……\n',
            '干嘛在这大眼瞪小眼啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0104, 0x0101, 400)

    ChrTalk(
        0x0104,
        (
            '#0040440597V#035F#2P呼，你都看到啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040440598V阿加特想强迫我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050440599V#055F#1P白、白痴啊！！\n',
            '少在这说胡话！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0104, 0x0106, 400)

    ChrTalk(
        0x0104,
        (
            '#0040440600V#031F#2P哈哈哈。\n',
            '有什么好掩饰的嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040440601V真是的～阿加特害·羞·了㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x14, 0x17, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010440602V#1020F#4P……哇、哇啊…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0106, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrTurnDirection(0x0106, 0x0101, 400)

    ChrTalk(
        0x0106,
        (
            '#0050440603V#055F#1P别、别当真啊！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050440604V好、好啦！\n',
            '赶快去报告啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    Sleep(1000)

    TerminateThread(0x000D, 0x01)
    OP_28(0x0068, 0x01, 0x0400)
    Call(1, 0x0013)

    Return()

    def _loc_98DB(): pass

    label('loc_98DB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_AC93',
    )

    Call(2, 0x000E)
    OP_59()
    Sleep(400)

    ChrTurnDirection(0x0103, 0x000D, 400)

    ChrTalk(
        0x0103,
        (
            '#0030440605V#027F#2P（好了……\n',
            '对方的情况怎样？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(1, 0x0018)
    OP_62(0x0105, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(150)

    OP_62(0x0106, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(100)

    OP_62(0x0104, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    OP_6D(29690, 0, 31480, 1000)

    ChrTalk(
        0x0105,
        (
            '#0060440494V#045F（看、看起来\n',
            '  情况很古怪。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010440607V#1002F（嗯，看来有好牌。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040440608V#030F（好了，雪拉\n',
            '  打算怎样出？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(32073, 0, 31585, 0)
    OP_0D()
    FadeOut(300, 0, 100)
    OP_C5(0x00, 0xFFCE, 0xFFB0, 0x0032, 0x0050, 0x01E3, 0x00F0, 0x0200, 0x0200, 0x0000, 0x0000, 0x0064, 0x00A0, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x01, 0xFFCE, 0xFFB0, 0x0032, 0x0050, 0x01E1, 0x00EE, 0x0200, 0x0200, 0x0000, 0x0000, 0x0064, 0x00A0, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x02, 0xFFCE, 0xFFB0, 0x0032, 0x0050, 0x01DF, 0x00EC, 0x0200, 0x0200, 0x0000, 0x0000, 0x0064, 0x00A0, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x03, 0xFFCE, 0xFFB0, 0x0032, 0x0050, 0x01DD, 0x00EA, 0x0200, 0x0200, 0x0000, 0x0000, 0x0064, 0x00A0, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x04, 0xFFCE, 0xFFB0, 0x0032, 0x0050, 0x01DB, 0x00E8, 0x0200, 0x0200, 0x0000, 0x0000, 0x0064, 0x00A0, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x05, 0xFFCE, 0xFFB0, 0x0032, 0x0050, 0x00A3, 0x00E8, 0x0200, 0x0200, 0x0064, 0x0140, 0x00C8, 0x01E0, 0x00FFFFFF, 0x00, 'C_VIS229._CH')
    OP_C5(0x06, 0xFFCE, 0xFFB0, 0x0032, 0x0050, 0x00F3, 0x00EA, 0x0200, 0x0200, 0x0190, 0x0140, 0x01F4, 0x01E0, 0x00FFFFFF, 0x00, 'C_VIS229._CH')
    OP_C5(0x07, 0xFFCE, 0xFFB0, 0x0032, 0x0050, 0x0143, 0x00EC, 0x0200, 0x0200, 0x0064, 0x0000, 0x00C8, 0x00A0, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x08, 0xFFCE, 0xFFB0, 0x0032, 0x0050, 0x0193, 0x00EE, 0x0200, 0x0200, 0x0000, 0x0140, 0x0064, 0x01E0, 0x00FFFFFF, 0x00, 'C_VIS229._CH')
    OP_C5(0x09, 0xFFCE, 0xFFB0, 0x0032, 0x0050, 0x01E3, 0x00F0, 0x0200, 0x0200, 0x012C, 0x0000, 0x0190, 0x00A0, 0x00FFFFFF, 0x00, 'C_VIS229._CH')
    OP_C6(0x05, 0x03, -1, 400, 0)
    OP_C6(0x06, 0x03, -1, 400, 0)
    OP_C6(0x07, 0x03, -1, 400, 0)
    OP_C6(0x08, 0x03, -1, 400, 0)
    OP_C6(0x09, 0x03, -1, 400, 0)
    Sleep(1000)

    ChrTurnDirection(0x0103, 0x000B, 0)
    SetMessageWindowPos(-1, 320, -1, -1)
    SetChrName('雪拉扎德')

    Talk(
        (
            '#0030440609V#022F（那个样子的话\n',
            '对方是来了大牌了……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030440610V（这么说，普通的手牌\n',
            '  输的几率很大。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030440611V（这里还是应该追求\n',
            '  理想形态的同花顺吗？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

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

    Menu(
        0,
        10,
        100,
        0,
        (
            TXT(0x00, '【只留对Ａ其余交换】\n'),
            TXT(0x01, '【除黑桃以外全部交换】\n'),
        ),
    )

    MenuEnd(0x0003)
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
    OP_AE(0x000001F4)
    Sleep(1000)

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_9E11',
    )

    SetMessageWindowPos(-1, 320, -1, -1)
    SetChrName('雪拉扎德')

    Talk(
        (
            '#0030440612V#022F（话虽如此……\n',
            '  放弃对Ａ也不太可能。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030440613V（……好，就用这方法。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_9E11')

    def _loc_9E11(): pass

    label('loc_9E11')

    Call(2, 0x0017)
    OP_C7(0x01, 0xFF, 0x00)
    OP_C6(0x00, 0x06, 0, 0, 0)
    OP_C6(0x01, 0x06, 0, 0, 0)
    OP_C6(0x02, 0x06, 0, 0, 0)
    OP_C6(0x03, 0x06, 0, 0, 0)
    OP_C6(0x04, 0x06, 0, 0, 0)
    OP_C6(0x05, 0x06, 0, 0, 0)
    OP_C6(0x06, 0x06, 0, 0, 0)
    OP_C6(0x07, 0x06, 0, 0, 0)
    OP_C6(0x08, 0x06, 0, 0, 0)
    OP_C6(0x09, 0x06, 0, 0, 0)
    FadeIn(300, 0)
    Sleep(1000)

    ChrTurnDirection(0x000B, 0x0103, 400)

    ChrTalk(
        0x000B,
        (
            '#3150440210V要换牌吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_9F16',
    )

    ChrTalk(
        0x0103,
        (
            '#0030440615V#022F#2P麻烦换３张。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9F3C')

    def _loc_9F16(): pass

    label('loc_9F16')

    ChrTalk(
        0x0103,
        (
            '#0030440616V#022F#2P麻烦换２张。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9F3C(): pass

    label('loc_9F3C')

    ChrTurnDirection(0x000B, 0x000D, 400)

    ChrTalk(
        0x000B,
        (
            '#3150440212V……客人您呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3130440509V#1P哦，我只换１张。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()
    Call(2, 0x000F)
    OP_59()
    Call(1, 0x0011)
    OP_59()
    Call(2, 0x0013)
    OP_59()

    ChrTalk(
        0x0103,
        (
            '#0030440619V#022F#2P…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(29690, 0, 31480, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010440620V#1020F#2P同、同花大顺什么的……咦！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440516V那不是最强的牌吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060440519V#042F穷途末路……了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040440623V#032F#2P唔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(32073, 0, 31585, 0)
    OP_0D()
    ChrTurnDirection(0x000B, 0x0103, 400)

    ChrTalk(
        0x000B,
        (
            '#3150440521V……客人也请开牌。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3150440522V不展示手牌的话，\n',
            '胜负是不清楚的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A417',
    )

    ChrTalk(
        0x0103,
        (
            '#0030440626V#025F#1P嗯，意料之中，\n',
            '这次已经一目了然了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(2, 0x0011)
    OP_59()

    ChrTalk(
        0x000B,
        (
            '#3150440524V唔，确实……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x000B, 270, 400)

    ChrTalk(
        0x000B,
        (
            '#3150440525V那么这次比赛───\n',
            '菲利奥先生赢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3130440526V#1P哈哈哈。\n',
            '哎呀～这是当然的结果嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3130440527V#1P你们也很努力了\n',
            '就是选错了对手。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(27210, 0, 33050, 0)
    OP_8C(0x000D, 90, 0)
    OP_0D()

    ChrTalk(
        0x0105,
        (
            '#0060440528V#043F#5P唉，输了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040440632V#030F#2P唔～真可惜啊。\n',
            '虽说还是有机会的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_A291')
    def lambda_A291():
        ChrTurnDirection(0x0104, 0x0103, 400)
        Yield()

        Jump('lambda_A291')

    DispatchAsync2(0x0104, 0x0001, lambda_A291)

    OP_8E(0x0103, 29900, 0, 31490, 2000, 0x00)
    TerminateThread(0x0104, 0x01)

    ChrTalk(
        0x0103,
        (
            '#0030440633V#025F抱歉，我输了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030440634V虽然有好牌，\n',
            '但我不够坚持。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010440635V#1003F#1P哪里，连雪拉姐\n',
            '都输了的话就没办法了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440636V#1015F不过，这下\n',
            '委托就失败了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440637V嗯～该拿什么脸\n',
            '去见委托人才好呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030440638V#026F即使没脸去见\n',
            '也是非见不可的哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030440639V嗯，这职业的痛苦就在于此。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    Sleep(1000)

    OP_28(0x0068, 0x01, 0x0800)
    Call(1, 0x0012)

    Return()

    def _loc_A417(): pass

    label('loc_A417')

    ChrTalk(
        0x0103,
        (
            '#0030440640V#021F#2P呵呵，说得没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000D, 0x0103, 400)

    ChrTalk(
        0x000D,
        (
            '#3130440641V#1P哼，开也没用的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3130440642V#1P因为我这可是\n',
            '最强手牌啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030440643V#027F#2P哎呀……\n',
            '那又怎样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()
    FadeOut(300, 0, 100)
    OP_D9(0x00, 'CTI00120')
    OP_22(0x021F, 0x00, 0x64)
    Sleep(2000)

    OP_D9(0x01)
    FadeIn(300, 0)
    Fade(1000)
    OP_6D(29690, 0, 31480, 0)
    OP_0D()
    OP_62(0x0101, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    OP_22(0x0026, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010440644V#1004F哎、咦……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0101, 400)

    ChrTalk(
        0x0105,
        (
            '#0060440645V#044F怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010440646V#1015F刚才，雪拉姐的手……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190126V……………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440648V#1016F……抱、抱歉。\n',
            '看来是我错觉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060440649V#040F？？？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(32073, 0, 31585, 0)
    OP_8C(0x0105, 90, 0)
    OP_0D()
    Call(2, 0x0012)
    OP_59()
    OP_62(0x000D, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000D,
        (
            '#3130440650V#1P怎、怎么会！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3150440651V……确实，看来没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3150440576V而且，还是黑桃……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3150440577V唔，那么这边的牌\n',
            '比菲利奥先生的更大。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000D, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    @scena.Lambda('lambda_A70A')
    def lambda_A70A():
        OP_95(0x000D, 0x00000000, 0x000003E8, 0x00000000, 0x000001F4, 0x00001388)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_A70A)

    ChrTurnDirection(0x000D, 0x000B, 400)

    ChrTalk(
        0x000D,
        (
            '#3130440578V#1P骗、骗人的吧！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3150440579V这场比赛───\n',
            '是各位赢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x000D, 0x01, 0x01, 0x0017)

    ChrTalk(
        0x0103,
        (
            '#0030440656V#025F#2P呼，哎呀哎呀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3150440583V……这是赌金。\n',
            '请确认。',
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
            '得到了',
            (TxtCtl.SetColor, 0x4),
            '２０００',
            (TxtCtl.SetColor, 0x0),
            '米拉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    Fade(1000)
    OP_6D(27210, 0, 33050, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010440658V#1008F#1P啊哈哈……\n',
            '好、好像赢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060440659V#045F#5P难、难以置信……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040440585V#031F哈哈哈。\n',
            '简直是大逆转呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_A8CC')
    def lambda_A8CC():
        ChrTurnDirection(0x0104, 0x0103, 400)
        Yield()

        Jump('lambda_A8CC')

    DispatchAsync2(0x0104, 0x0001, lambda_A8CC)

    OP_8E(0x0103, 29900, 0, 31490, 2000, 0x00)
    TerminateThread(0x0104, 0x01)

    ChrTalk(
        0x0101,
        (
            '#0010440661V#1001F#1P雪拉姐，辛苦了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440662V居然能在那里反败为胜，\n',
            '真是～姐姐最可靠了㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040440663V#031F#2P呵呵，长见识了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x0104, 400)

    ChrTalk(
        0x0103,
        (
            '#0030440664V#027F好久没做了有点紧张……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030440665V#525F嗯，还好没岀差错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0104, 400)
    OP_62(0x0101, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    OP_22(0x0026, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010440666V#1011F#1P嗯？你们说什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0104, 0x0101, 400)

    ChrTalk(
        0x0104,
        (
            '#0040440667V#035F#2P呵，这是大人的私事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060440668V#040F#5P？？？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010440669V#1004F#1P…………啊………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440670V……难、难不成！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030440671V#023F哎呀，你没发现吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030440672V还以为你和奥利维尔\n',
            '都能看穿呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010440673V#1022F#1P败、败给你了～～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440674V怪不得那个时候\n',
            '觉得怪怪的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030440675V#021F呵呵，所谓蛇行蛇道嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030440676V#020F……那么，赶快\n',
            '去委托人那里报告吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030440677V虽说似乎没被拆穿，\n',
            '但还是不便久留吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010440678V#1002F#1P确、确实如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440679V好，赶快去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    Sleep(1000)

    TerminateThread(0x000D, 0x01)
    OP_28(0x0068, 0x01, 0x1000)
    Call(1, 0x0013)

    def _loc_AC93(): pass

    label('loc_AC93')

    Return()

# id: 0x0005 offset: 0xAC94
@scena.Code('func_05_AC94')
def func_05_AC94():
    OP_8C(0x00FE, 180, 400)
    OP_8E(0x00FE, 29280, 0, 32650, 1050, 0x00)
    OP_8E(0x00FE, 31260, 0, 30690, 1050, 0x00)

    Return()

# id: 0x0006 offset: 0xACC4
@scena.Code('func_06_ACC4')
def func_06_ACC4():
    OP_8C(0x00FE, 180, 400)
    Sleep(200)

    OP_8E(0x00FE, 30160, 0, 32940, 1000, 0x00)
    OP_8E(0x00FE, 31250, 0, 31850, 1000, 0x00)

    Return()

# id: 0x0007 offset: 0xACF9
@scena.Code('func_07_ACF9')
def func_07_ACF9():
    OP_8C(0x00FE, 180, 400)
    OP_8E(0x00FE, 28980, 0, 31880, 1050, 0x00)
    OP_8E(0x00FE, 30170, 0, 30740, 1050, 0x00)

    Return()

# id: 0x0008 offset: 0xAD29
@scena.Code('func_08_AD29')
def func_08_AD29():
    OP_8C(0x00FE, 180, 400)
    Sleep(200)

    OP_8E(0x00FE, 29800, 0, 32100, 1000, 0x00)
    ChrTurnDirection(0x00FE, 0x000D, 400)

    Return()

# id: 0x0009 offset: 0xAD51
@scena.Code('func_09_AD51')
def func_09_AD51():
    ChrTurnDirection(0x00FE, 0x000B, 400)

    Return()

# id: 0x000A offset: 0xAD59
@scena.Code('func_0A_AD59')
def func_0A_AD59():
    ChrTurnDirection(0x00FE, 0x0019, 400)

    Return()

# id: 0x000B offset: 0xAD61
@scena.Code('func_0B_AD61')
def func_0B_AD61():
    ChrTurnDirection(0x00FE, 0x0104, 400)

    Return()

# id: 0x000C offset: 0xAD69
@scena.Code('func_0C_AD69')
def func_0C_AD69():
    ChrTurnDirection(0x00FE, 0x0101, 400)

    Return()

# id: 0x000D offset: 0xAD71
@scena.Code('func_0D_AD71')
def func_0D_AD71():
    OP_69(0x000D, 0x000007D0)

    Return()

# id: 0x000E offset: 0xAD79
@scena.Code('func_0E_AD79')
def func_0E_AD79():
    OP_8E(0x0104, 31170, 0, 32710, 2000, 0x00)
    OP_8E(0x0104, 34920, 0, 32253, 2000, 0x00)
    OP_8E(0x0104, 35145, 0, 31023, 2000, 0x00)

    Return()

# id: 0x000F offset: 0xADB6
@scena.Code('func_0F_ADB6')
def func_0F_ADB6():
    OP_8E(0x0104, 34920, 0, 32253, 2000, 0x00)
    OP_8E(0x0104, 31170, 0, 32710, 2000, 0x00)
    OP_8E(0x0104, 28850, 0, 32500, 2000, 0x00)
    ChrTurnDirection(0x0104, 0x0101, 400)

    Return()

# id: 0x0010 offset: 0xADFA
@scena.Code('func_10_ADFA')
def func_10_ADFA():
    OP_62(0x000B, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    @scena.Lambda('lambda_AE17')
    def lambda_AE17():
        ChrTurnDirection(0x000B, 0x0104, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_AE17)

    @scena.Lambda('lambda_AE25')
    def lambda_AE25():
        ChrTurnDirection(0x0018, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_AE25)

    OP_8F(0x000B, 35029, 0, 28980, 8000, 0x00)
    OP_62(0x0018, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    Return()

# id: 0x0011 offset: 0xAE54
@scena.Code('func_11_AE54')
def func_11_AE54():
    Sleep(1000)

    ChrTalk(
        0x000B,
        (
            '#3150440680V……牌凑好了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3150440681V那么─────',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3150440682V────请亮岀手牌。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x000D,
        (
            '#3130440683V好，从我开始开吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Return()

# id: 0x0012 offset: 0xAEEB
@scena.Code('func_12_AEEB')
def func_12_AEEB():
    OP_28(0x0068, 0x04, 0x40)
    OP_28(0x0068, 0x04, 0x80)
    OP_22(0x0106, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【急聘牌技高手】',
            (TxtCtl.SetColor, 0x0),
            '失败了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_4A(0x000E, 0)
    OP_4A(0x000E, 0)
    SetChrPos(0x0101, 5600, 250, 33020, 0)
    SetChrPos(0x00F7, 4770, 250, 32659, 0)
    SetChrPos(0x0104, 5560, 250, 31520, 0)
    SetChrPos(0x0105, 4580, 250, 31210, 0)
    OP_6D(4960, 250, 33040, 0)
    OP_20(0x000003E8)
    OP_21()
    OP_1D(0x0C)
    Sleep(400)

    FadeIn(2000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010440805V#1003F……就是这样…………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440806V经过苦战，\n',
            '还是失败了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440807V#1007F……真是对不起。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_B07D',
    )

    ChrTalk(
        0x0106,
        (
            '#0050440808V#053F抱歉，无可辩驳。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050440809V关于这件事\n',
            '完全怪我们力量不足。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B0D4')

    def _loc_B07D(): pass

    label('loc_B07D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_B0D4',
    )

    ChrTalk(
        0x0103,
        (
            '#0030440810V#025F无可辩驳了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030440811V关于这件事\n',
            '完全怪我们力量不足。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B0D4(): pass

    label('loc_B0D4')

    ChrTalk(
        0x000E,
        (
            '#3140440812V是吗……不行啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#3140440813V唉，不过，这也没办法。\n',
            '这个什么的纯粹靠运气嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#3140440814V当然，游击士们\n',
            '请在别的事情上多加努力吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010440815V#1007F真、真丢脸……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040440816V#035F呼，确实我们\n',
            '没帮上忙……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040440817V#030F但是，您丈夫的事\n',
            '我想不必担心哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0101, 0x01, 0x01, 0x000B)
    CreateThread(0x0105, 0x01, 0x01, 0x000B)
    CreateThread(0x000E, 0x01, 0x01, 0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_B224',
    )

    CreateThread(0x0106, 0x01, 0x01, 0x000B)

    Jump('loc_B232')

    def _loc_B224(): pass

    label('loc_B224')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_B232',
    )

    CreateThread(0x0103, 0x01, 0x01, 0x000B)

    def _loc_B232(): pass

    label('loc_B232')

    ChrTalk(
        0x000E,
        (
            '#3140440818V咦？为什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010440819V#1004F我、我说奥利维尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_B2CD',
    )

    ChrTalk(
        0x0106,
        (
            '#0050440820V#050F嗯，没什么不好啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050440821V听他想说什么吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B319')

    def _loc_B2CD(): pass

    label('loc_B2CD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_B319',
    )

    ChrTalk(
        0x0103,
        (
            '#0030440822V#020F嗯，没关系吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030440823V听听他想说什么吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B319(): pass

    label('loc_B319')

    ChrTalk(
        0x0101,
        (
            '#0010440824V#1015F嗯、嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040440825V#035F是这样的，大部分娱乐场\n',
            '都会有个王牌类的人物。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040440826V平时不会去店里，\n',
            '但却是那个店里最强的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040440827V#030F不过，在我看来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040440828V这个店里，那个人物\n',
            '似乎还没出现呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_B450',
    )

    ChrTalk(
        0x0106,
        (
            '#0050440829V#052F也就是说，还没到\n',
            '那家伙出场的时候吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B493')

    def _loc_B450(): pass

    label('loc_B450')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_B493',
    )

    ChrTalk(
        0x0103,
        (
            '#0030440830V#023F也就是说，还没到\n',
            '那个人出场的时候吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B493(): pass

    label('loc_B493')

    ChrTurnDirection(0x0104, 0x00F7, 400)

    ChrTalk(
        0x0104,
        (
            '#0040440831V#030F啊啊，因为我们输了，\n',
            '所以我想很快就会登场了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010440832V#1015F王牌……啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#3140440833V唉，真是\n',
            '这样就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#3140440834V这个人的话……\n',
            '可以相信吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(100)

    OP_62(0x0105, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(150)

    OP_62(0x00F7, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_B5B2')
    def lambda_B5B2():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_B5B2)

    @scena.Lambda('lambda_B5C0')
    def lambda_B5C0():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_B5C0)

    @scena.Lambda('lambda_B5CE')
    def lambda_B5CE():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_B5CE)

    OP_8C(0x0104, 0, 400)

    ChrTalk(
        0x0101,
        (
            '#0010440835V#1016F唔、嗯～怎么说呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440836V相信不相信\n',
            '就看您自己的判断了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#3140440837V总之，我在这里\n',
            '再稍微等等看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#3140440838V不管会不会\n',
            '像这个人说的一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_B6EA',
    )

    ChrTalk(
        0x0106,
        (
            '#0050440839V#050F既然如此，\n',
            '我们就先走了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050440840V今天真是抱歉了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B73F')

    def _loc_B6EA(): pass

    label('loc_B6EA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_B73F',
    )

    ChrTalk(
        0x0103,
        (
            '#0030440841V#020F既然如此，\n',
            '我们就先走了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030440842V今天真是对不起。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B73F(): pass

    label('loc_B73F')

    ChrTalk(
        0x000E,
        (
            '#3140440843V我相信你们都尽力了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#3140440802V那么，游击士们。\n',
            '以后有事再麻烦你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010440845V#1006F嗯，请随时吩咐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0007)
    OP_8C(0x000E, 180, 0)
    OP_4B(0x000E, 255)
    OP_4B(0x000E, 255)
    OP_4B(0x000D, 255)
    OP_4B(0x0018, 255)
    OP_4B(0x000B, 255)
    OP_8C(0x0018, 270, 0)
    OP_8C(0x000B, 270, 0)

    Return()

# id: 0x0013 offset: 0xB7F3
@scena.Code('func_13_B7F3')
def func_13_B7F3():
    OP_28(0x0068, 0x04, 0x10)
    OP_4A(0x000E, 0)
    SetChrPos(0x0101, 5600, 250, 33020, 0)
    SetChrPos(0x00F7, 4770, 250, 32659, 0)
    SetChrPos(0x0104, 5560, 250, 31520, 0)
    SetChrPos(0x0105, 4580, 250, 31210, 0)
    OP_6D(4960, 250, 33040, 0)
    OP_20(0x000003E8)
    OP_21()
    OP_1D(0x0C)
    Sleep(400)

    FadeIn(2000, 0)
    OP_0D()

    ChrTalk(
        0x000E,
        (
            '#3140440776V真的……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#3140440777V呵，真的\n',
            '赢了我丈夫吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010440778V#1006F嗯，虽然挺辛苦\n',
            '总算还是成功了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_B944',
    )

    ChrTalk(
        0x0106,
        (
            '#0050440779V#050F这是拿回来的钱。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050440780V１０００加倍\n',
            '正好２０００米拉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B99F')

    def _loc_B944(): pass

    label('loc_B944')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_B99F',
    )

    ChrTalk(
        0x0103,
        (
            '#0030440781V#020F这是拿回来的钱。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030440782V１０００加倍\n',
            '正好２０００米拉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B99F(): pass

    label('loc_B99F')

    ChrTalk(
        0x000E,
        (
            '#3140440783V啊，不用了。\n',
            '请你们收下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#3140440784V就当作是补偿那\n',
            '太过便宜的报酬吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010440785V#1011F咦？可以吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440786V既然您都这样说了,\n',
            '那我们就感激地收下了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440787V#1015F……不过，真的\n',
            '这样就行了吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440788V您丈夫好像\n',
            '并没怎么吸取教训哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#3140440789V之后我想娱乐场的人\n',
            '会想办法解决的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#3140440790V他们也是专业的，\n',
            '不会让我丈夫一直赢下去的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_BBA4',
    )

    ChrTalk(
        0x0106,
        (
            '#0050440791V#051F呵，那倒是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050440792V#050F既然如此\n',
            '我们这就告辞了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050440793V……没问题吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BC1A')

    def _loc_BBA4(): pass

    label('loc_BBA4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_BC1A',
    )

    ChrTalk(
        0x0103,
        (
            '#0030440794V#021F呵呵，那倒也是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030440795V#020F既然如此\n',
            '我们就先走了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030440796V……没问题吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BC1A(): pass

    label('loc_BC1A')

    ChrTalk(
        0x000E,
        (
            '#3140440797V嗯，可以了。\n',
            '你们已经做得够多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#3140440798V这样胡来的委托\n',
            '游击士也在认真帮我们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#3140440799V……对你们有点改观了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010440800V#1001F嘿嘿，谢谢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440801V从今以后也请继续努力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#3140440802V那么，游击士们。\n',
            '以后有事再麻烦你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_BD60',
    )

    ChrTalk(
        0x0106,
        (
            '#0050440803V#051F啊啊，随时吩咐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BD90')

    def _loc_BD60(): pass

    label('loc_BD60')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_BD90',
    )

    ChrTalk(
        0x0103,
        (
            '#0030440804V#020F嗯嗯，请随时吩咐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BD90(): pass

    label('loc_BD90')

    OP_A2(0x0007)
    AddMira(2000)
    OP_22(0x0017, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【急聘牌技高手】',
            (TxtCtl.SetColor, 0x0),
            '完成了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_4B(0x000E, 255)
    OP_4B(0x000D, 255)
    OP_4B(0x0018, 255)
    OP_4B(0x000B, 255)
    OP_8C(0x0018, 270, 0)
    OP_8C(0x000B, 270, 0)

    Return()

# id: 0x0014 offset: 0xBE07
@scena.Code('func_14_BE07')
def func_14_BE07():
    OP_8E(0x000B, 35140, 0, 28590, 1000, 0x00)
    ChrTurnDirection(0x0018, 0x000B, 400)
    OP_4A(0x0018, 255)
    OP_A5(0x0010)

    @scena.Lambda('lambda_BE2F')
    def lambda_BE2F():
        OP_8C(0x0018, 270, 400)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_BE2F)

    OP_8E(0x000B, 35010, 0, 30340, 1000, 0x00)
    OP_8C(0x000B, 270, 400)

    Return()

# id: 0x0015 offset: 0xBE53
@scena.Code('func_15_BE53')
def func_15_BE53():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_BE8D',
    )

    OP_62(0x000D, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(400)

    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    Jump('func_15_BE53')

    def _loc_BE8D(): pass

    label('loc_BE8D')

    Return()

# id: 0x0016 offset: 0xBE8E
@scena.Code('func_16_BE8E')
def func_16_BE8E():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_BEB1',
    )

    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    Sleep(1500)

    Jump('func_16_BE8E')

    def _loc_BEB1(): pass

    label('loc_BEB1')

    Return()

# id: 0x0017 offset: 0xBEB2
@scena.Code('func_17_BEB2')
def func_17_BEB2():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_BED5',
    )

    OP_62(0x00FE, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1500)

    Jump('func_17_BEB2')

    def _loc_BED5(): pass

    label('loc_BED5')

    Return()

# id: 0x0018 offset: 0xBED6
@scena.Code('func_18_BED6')
def func_18_BED6():
    OP_62(0x000D, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x000D,
        (
            '#3130440684V#1P………嗯……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3130440685V#1P……来、来了！\n',
            '这下来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    OP_62(0x000D, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)

    ChrTalk(
        0x000D,
        (
            '#3130440686V#1P……啊……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x000D, 0, 400)
    Sleep(2000)

    ChrTalk(
        0x000D,
        (
            '#3130440687V#1P没，没事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3130440688V#1P请、请别介意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x000D, 90, 400)
    Sleep(1000)

    ChrTalk(
        0x000D,
        (
            '#3130440689V#1P啊、唉～……\n',
            '手气真差啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3130440690V#1P唔～这恐怕\n',
            '不行啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
