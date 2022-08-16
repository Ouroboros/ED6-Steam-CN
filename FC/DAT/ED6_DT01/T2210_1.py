import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T2210_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2210_1 ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T2210.x'
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
    )

# id: 0x10000 offset: 0x64
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
    ]

# id: 0x10001 offset: 0x64
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10002 offset: 0x64
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x64
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x64
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x64
@scena.Code('Init')
def Init():
    EventBegin(0x00)
    Fade(1000)
    OP_4A(0x0010, 255)
    ChrSetPos(0x0101, 500, 0, 200, 0)
    ChrSetPos(0x0102, -500, 0, 200, 0)
    ChrSetPos(0x0105, 300, 0, -1300, 0)
    CameraMove(200, 0, 300, 0)
    OP_0D()

    If(
        (
            (Expr.Eval, "OP_29(0x0020, 0x01, 0x2000)"),
            Expr.Return,
        ),
        'loc_23D',
    )

    Sleep(400)

    ChrSetDirection(0x0010, 180, 400)

    ChrTalk(
        0x0010,
        (
            '#0480170099V#670F呀，是你们啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480170100V如何，\n',
            '现在可以去寻找了吗？',
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
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_23A',
    )

    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010170101V#003F对不起，还是不行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0480170102V#671F这样啊……\n',
            '虽然很遗憾，不过没有办法啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480170103V如果你们有空了，\n',
            '请尽快到我这里来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010170025V#006F嗯，我知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0020, 0x01, 0x2000)
    EventEnd(0x00)
    OP_4B(0x0010, 255)
    ChrSetDirection(0x0010, 0, 0)

    Return()

    def _loc_23A(): pass

    label('loc_23A')

    Jump('loc_7DE')

    def _loc_23D(): pass

    label('loc_23D')

    ChrTalk(
        0x0010,
        (
            '#0480170001V#673F唔，不见了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480170002V『苍耀之灯火』\n',
            '居然被盗走了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480170003V#671F而且偏偏还是在这种时候……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0010, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    ChrSetDirection(0x0010, 180, 400)
    Sleep(800)

    ChrTalk(
        0x0010,
        (
            '#0480170004V#670F呀，是你们啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480170005V我一直在等你们来呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480170006V#672F哦？怎么回事，\n',
            '竟然连科洛丝也和你们在一起。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0010, 400)

    ChrTalk(
        0x0105,
        (
            '#0060170007V#040F嗯，是我请他们带着我一起来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x0020, 0x00, 0x02)"),
            Expr.Return,
        ),
        'loc_484',
    )

    ChrTurnDirection(0x0102, 0x0010, 400)

    ChrTalk(
        0x0102,
        (
            '#0020170008V#010F我们已经看过公告板了。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020170009V这次是什么样的情况呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0010, 0x0102, 400)

    ChrTalk(
        0x0010,
        (
            '#0480170010V#671F请看这边。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0434')
    def lambda_0434():
        ChrSetDirection(0x0102, 0, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0434)

    ChrSetDirection(0x0010, 0, 400)

    ChrTalk(
        0x0010,
        (
            '#0480170011V#671F这个台座上本来\n',
            '放有一支作为装饰的烛台。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_571')

    def _loc_484(): pass

    label('loc_484')

    ChrTurnDirection(0x0101, 0x0010, 400)

    ChrTalk(
        0x0101,
        (
            '#0010170012V#501F等一下……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170013V……有什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0010, 0x0101, 400)

    ChrTalk(
        0x0010,
        (
            '#0480170010V#671F请看这边。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_04F4')
    def lambda_04F4():
        ChrSetDirection(0x0101, 0, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_04F4)

    ChrSetDirection(0x0010, 0, 400)

    ChrTalk(
        0x0010,
        (
            '#0480170015V#671F这个台座上本来放着装饰用的烛台，\n',
            '不知道被谁偷走了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060170016V#044F啊…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_571(): pass

    label('loc_571')

    OP_28(0x0020, 0x04, 0x02)

    ChrTalk(
        0x0101,
        (
            '#0010170017V#004F哎呀…………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170018V果然已经无影无踪了啊。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0010, 180, 400)

    ChrTalk(
        0x0010,
        (
            '#0480170019V#671F正是因为如此，\n',
            '我希望你们能够尽快找回来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480170020V怎么样，你们有时间吗？',
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
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7DE',
    )

    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010170021V#003F对不起啊，\n',
            '现在我们还有点事要做。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020170022V#015F十分抱歉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0480170023V#671F没事，没关系的。\n',
            '你们还有其他的事情要办嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480170024V如果待会儿有空了，\n',
            '就请来帮帮我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010170025V#006F嗯，我知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020170026V#010F那么，我们就先行告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0480170027V#670F嗯，待会儿就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0020, 0x01, 0x2000)
    EventEnd(0x00)
    OP_4B(0x0010, 255)
    ChrSetDirection(0x0010, 0, 0)

    Return()

    def _loc_7DE(): pass

    label('loc_7DE')

    OP_28(0x0020, 0x04, 0x08)
    OP_28(0x0020, 0x04, 0x04)
    OP_28(0x0020, 0x01, 0x0001)
    OP_28(0x0020, 0x01, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010160091V#006F嗯，没问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020170029V#010F请多指教。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0480170030V#670F彼此彼此。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480170031V那么我就立刻\n',
            '说明事情的状况…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0010, 0, 400)

    ChrTalk(
        0x0010,
        (
            '#0480170032V#671F被盗走的是\n',
            '名为『苍耀之灯火』的烛台。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480170033V是在导力革命之后不久\n',
            '所制造出的导力艺术珍品。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480170034V也是这个戴尔蒙家族的传家之宝。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480170035V#673F由于这是极为贵重的物品，\n',
            '一旦被卖出去，\n',
            '至少可以换来数百万米拉的金钱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrTurnDirection(0x0101, 0x0010, 400)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010170036V#004F数、数百万米拉…………！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0010, 400)

    ChrTalk(
        0x0102,
        (
            '#0020170037V#013F…………原来如此。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020170038V不过这一点好像并不是\n',
            '犯人的动机所在。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010170039V#002F嗯？为什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020170040V#015F如此高价的物品要想安全地脱手，\n',
            '必须要经过特殊的渠道才行。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020170041V然而我认为这次的这个犯人，\n',
            '不像是有那样的门路。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010170042V#505F这样啊………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170043V虽然偷走了，\n',
            '但却不能像一般的东西那样换成钱啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0010, 0x0102, 400)

    ChrTalk(
        0x0010,
        (
            '#0480170044V#672F是呀，总觉得有些奇怪……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480170045V这次的偷盗事件，\n',
            '犯人的动机似乎并不在于金钱啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0BE9')
    def lambda_0BE9():
        ChrTurnDirection(0x0101, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0BE9)

    ChrTurnDirection(0x0102, 0x0010, 400)

    ChrTalk(
        0x0101,
        (
            '#0010170046V#004F…………啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020170047V#014F究竟是怎么回事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0480170048V#671F请看看这张卡片。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            '#0170170049V',
            (TxtCtl.SetColor, 0x0),
            '『方才蚕食巢穴的乃是比野兽更狂野的兽中之兽。\n',
            '　\n',
            '　苍之光将黑暗中迷失的灵魂赞颂并传承。\n',
            '　让残存之耀得以救赎，而我即为解放者。\n',
            '　\n',
            '　啊，探寻者们。\n',
            '　如女神一般直视真实，抛弃虚伪吧。\n',
            '　\n',
            TxtCtl.Enter,
            '#0170170050V　前往耸立于此村落中的\n',
            '　三眼巨人所在之处吧。\n',
            '　如是，探寻者们，\n',
            '　汝等将至苍之光所在。\n',
            '　　　　　　　　　　　　　　　　　　　　怪盗Ｂ』',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(400)

    ChrTalk(
        0x0102,
        (
            '#0020170051V#012F…………这是？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0480170052V#671F空空如也的台座上留下的东西。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480170053V这上面所写的内容\n',
            '肯定是犯人留下的字句。\n',
            '我想这点应该是毫无疑问的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0010, 400)

    ChrTalk(
        0x0101,
        (
            '#0010170054V#002F也就是说…………\n',
            '这是犯罪声明之类的东西？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0010, 0x0101, 400)

    ChrTalk(
        0x0010,
        (
            '#0480170055V#671F我想大概就是这样，\n',
            '要不然也不会写成这个样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010170056V#002F原来是这样，如果是以钱为目的，\n',
            '就不会费心去弄这样的东西吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0F8D')
    def lambda_0F8D():
        ChrTurnDirection(0x0105, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_0F8D)

    ChrTurnDirection(0x0010, 0x0102, 400)

    ChrTalk(
        0x0105,
        (
            '#0060170057V#042F这篇文章到底是什么意思呢？\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060170058V再细细地品味一下，\n',
            '有些诗样的感觉呢…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0105, 400)

    ChrTalk(
        0x0102,
        (
            '#0020170059V#013F『苍之光将黑暗中……』是吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020170060V所谓的『苍之光』\n',
            '应该就是被盗的烛台吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0480170061V#671F是的，应该就是如此。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_10A9')
    def lambda_10A9():
        ChrTurnDirection(0x0105, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_10A9)

    ChrTurnDirection(0x0102, 0x0010, 400)

    ChrTalk(
        0x0010,
        (
            '#0480170062V#671F那个烛台，是市民们赠送给\n',
            '为城市的繁荣发展鞠躬尽瘁的\n',
            '戴尔蒙家前代的主人的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480170063V#670F如果这么考虑，\n',
            '『将灵魂赞颂并传承』这一句就讲得通了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0010, 400)

    ChrTalk(
        0x0101,
        (
            '#0010170064V#501F哎～原来是这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170065V那么最后的部分是什么意思呢？\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170066V为什么感觉上是\n',
            '为了指引我们才这么写的……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020170067V#010F就是这句『前往耸立于此村落中的\n',
            '　三眼巨人所在之处吧。』',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020170068V的确是这样……\n',
            '要去哪里寻找，\n',
            '已经给了我们提示了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010170069V#002F……意思就是说，\n',
            '已经提示出了所在地吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0101, 400)

    ChrTalk(
        0x0105,
        (
            '#0060170070V#042F『此村落』\n',
            '应该就是指卢安吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060170071V在这个城市里的某个地方\n',
            '有一个所谓的『三眼巨人』…………\n',
            '我想应该是这个意思吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0105, 400)

    ChrTalk(
        0x0101,
        (
            '#0010170072V#505F嗯，\n',
            '不过为什么要说什么巨人……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170073V不过这个肯定是线索没错啦。\n',
            '赶快把它仔细地记录下来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0010, 0x0101, 400)

    ChrTalk(
        0x0010,
        (
            '#0480170074V#673F唔，\n',
            '看起来已经没有我再解释的必要了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480170075V#670F那么我先就此失陪了。\n',
            '我还有一些事情要去处理。\n',
            '  ',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480170076V接下来就由你们去搜寻了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_149E')
    def lambda_149E():
        ChrTurnDirection(0x0101, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_149E)

    @scena.Lambda('lambda_14AC')
    def lambda_14AC():
        ChrTurnDirection(0x0105, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_14AC)

    ChrTurnDirection(0x0102, 0x0010, 400)

    ChrTalk(
        0x0101,
        (
            '#0010170077V#006F嗯，我知道了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170078V那就首先对屋子\n',
            '里面进行彻底的搜查吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0480170079V#672F啊，没有这个必要吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010170080V#004F为什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0480170081V#671F屋子里面我已经\n',
            '叫佣人找了个底朝天了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480170082V因此你们只需要\n',
            '在城里进行搜寻就可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010170083V#002F不过…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0480170084V#671F犯人留下的卡片\n',
            '上面留下了很明显的提示。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480170085V希望你们能够赶快展开调查。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480170086V以取回烛台为最首要的目的。\n',
            '其他的事情你们不需多管。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0010, 400)

    ChrTalk(
        0x0102,
        (
            '#0020170087V#015F…………这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020170088V#010F那我们会听取您的建议，\n',
            '以卡片的提示为根据行事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010170089V#505F好吧，既然委托人这样说，\n',
            '那我们就这样做啦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0010, 0x0102, 400)

    ChrTalk(
        0x0010,
        (
            '#0480170090V#673F由专业人士来处理，\n',
            '就不用我来操心或干预了。\n',
            '我的工作也非常的繁忙。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480170091V希望你们能够理解。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480170092V#670F那么…………\n',
            '接下来就拜托你们了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480170093V我会一直呆在二楼，\n',
            '如果有什么发现就请随时来找我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1866')
    def lambda_1866():
        ChrTurnDirection(0x0101, 0x0010, 0)
        Yield()

        Jump('lambda_1866')

    DispatchAsync2(0x0101, 0x0001, lambda_1866)

    @scena.Lambda('lambda_1877')
    def lambda_1877():
        ChrTurnDirection(0x0102, 0x0010, 0)
        Yield()

        Jump('lambda_1877')

    DispatchAsync2(0x0102, 0x0001, lambda_1877)

    @scena.Lambda('lambda_1888')
    def lambda_1888():
        ChrTurnDirection(0x0105, 0x0010, 0)
        Yield()

        Jump('lambda_1888')

    DispatchAsync2(0x0105, 0x0001, lambda_1888)

    ChrWalkTo(0x0010, 8500, 0, 1200, 3000, 0x00)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0102, 0x01)
    TerminateThread(0x0105, 0x01)
    ChrSetPos(0x0010, 4530, 0, 36330, 90)
    Sleep(1000)

    @scena.Lambda('lambda_18CF')
    def lambda_18CF():
        ChrTurnDirection(0x0101, 0x0105, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_18CF)

    @scena.Lambda('lambda_18DD')
    def lambda_18DD():
        ChrTurnDirection(0x0102, 0x0105, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_18DD)

    @scena.Lambda('lambda_18EB')
    def lambda_18EB():
        ChrTurnDirection(0x0105, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_18EB)

    ExecExpressionWithValue(
        0x0011,
        0x01,
        (
            (Expr.GetChrWork, 0x102, 0x1),
            (Expr.GetChrWork, 0x101, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0011,
        0x02,
        (
            (Expr.GetChrWork, 0x102, 0x2),
            (Expr.GetChrWork, 0x101, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0011,
        0x03,
        (
            (Expr.GetChrWork, 0x102, 0x3),
            (Expr.GetChrWork, 0x101, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_69(0x0011, 800)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010170094V#003F唉，\n',
            '为什么会有这么奇怪的事件呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020170095V#010F我们唯有先根据\n',
            '卡片上所写的去调查了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0102, 400)

    ChrTalk(
        0x0105,
        (
            '#0060170096V#040F在卢安的某个地方\n',
            '应该会有线索的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010170097V#006F与其在这里发呆，\n',
            '倒不如赶快开始调查。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170098V我们这就行动吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x0010, 0x0010)
    MapClearFlags(0x00400000)
    EventEnd(0x00)
    ChrSetDirection(0x0010, 0, 0)
    OP_4B(0x0010, 255)

    Return()

# id: 0x0001 offset: 0x1A63
@scena.Code('func_01_1A63')
def func_01_1A63():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetFlags(0x00FE, 0x0040)

    @scena.Lambda('lambda_1A7E')
    def lambda_1A7E():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_1A7E)

    ChrWalkTo(0x00FE, 500, -500, 200, 2000, 0x00)

    Return()

# id: 0x0002 offset: 0x1A9F
@scena.Code('func_02_1A9F')
def func_02_1A9F():
    Sleep(400)

    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetFlags(0x00FE, 0x0040)

    @scena.Lambda('lambda_1ABF')
    def lambda_1ABF():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_1ABF)

    ChrWalkTo(0x00FE, -500, -500, -300, 2000, 0x00)

    Return()

# id: 0x0003 offset: 0x1AE0
@scena.Code('func_03_1AE0')
def func_03_1AE0():
    Sleep(400)

    Sleep(400)

    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetFlags(0x00FE, 0x0040)

    @scena.Lambda('lambda_1B05')
    def lambda_1B05():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_1B05)

    ChrWalkTo(0x00FE, 300, -500, -1300, 2000, 0x00)

    Return()

# id: 0x0004 offset: 0x1B26
@scena.Code('func_04_1B26')
def func_04_1B26():
    MapClearFlags(0x00000001)
    EventBegin(0x00)
    FadeIn(2000, 0)
    ChrSetPos(0x0101, 500, 0, 200, 0)
    ChrSetPos(0x0102, -500, 0, 200, 0)
    ChrSetPos(0x0105, 300, 0, -1300, 0)
    ChrSetPos(0x0008, 0, 0, 1800, 180)
    ChrSetPos(0x0010, 1000, 0, 2000, 180)
    TerminateThread(0x0010, 0xFF)
    TerminateThread(0x0008, 0xFF)
    CameraMove(200, 0, 300, 2000)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0x0102,
        (
            '#0020170329V#010F…………事情的经过就是这样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020170330V我们将烛台完好无损地取了回来……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020170331V#015F不过遗憾的是，\n',
            '有关犯人的线索\n',
            '我们至今毫无头绪。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020170332V除了知道他自称为『怪盗Ｂ』……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010170333V#007F唉，\n',
            '如果能早点注意到那个是假冒的就好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170334V我匆匆忙忙追过去的时候，\n',
            '他已经逃得无影无踪了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0490170335V#661F呵呵，\n',
            '其实你们已经做得很好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490170336V能够顺利地取回『苍耀之灯火』，\n',
            '对我们来说就已经足够了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0480170337V#678F市长说的极是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480170338V你们已经做得十分出色了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020170339V#013F您的话让我们深感欣慰……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020170340V#013F不过，我们让犯人逃跑了，\n',
            '这是不争的事实。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010170341V#002F嗯，这点是不能让人信服的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170342V让那个喜欢愚弄人的家伙逍遥法外了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020170343V#012F如果可以的话，\n',
            '能否让我们再做进一步的搜查？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020170344V挨家挨户的搜索，\n',
            '一定会找到线索的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0102, 400)

    ChrTalk(
        0x0008,
        (
            '#0490170345V#662F不用了，没有那个必要。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490170346V而且，我的委托里面\n',
            '并没有说一定要抓到犯人吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490170347V能够取回烛台就已经足够了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020170348V#012F不过…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0490170349V#662F约修亚…………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490170350V为了正义而奋斗，\n',
            '你的热情是难能可贵的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490170351V说到底…… \n',
            '这次的事件最多也只能算是\n',
            '针对我个人的犯罪。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490170352V那些琐碎的细节是其次的，\n',
            '你们就不用再为这件事而费心了。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490170353V#664F此时此刻，\n',
            '我想一定还有其他有需要的人\n',
            '在等待着你们游击士的帮助。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490170354V在我看来，\n',
            '帮助有困难的人才应该是\n',
            '你们最优先去做的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0010, 0x0008, 400)

    ChrTalk(
        0x0010,
        (
            '#0480170355V#672F市长…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020170356V#015F……………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020170357V……我明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020170358V#010F那么，\n',
            '搜查就到此为止吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x0E, 0x0F, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010170359V#505F唔…………\n',
            '算了，这也是没办法的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0010, 0x0102, 400)

    ChrTalk(
        0x0008,
        (
            '#0490170360V#661F嗯，辛苦你们了，\n',
            '报酬会通过协会全额支付给你们的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490170361V#660F那么……\n',
            '我就先失陪了，\n',
            '还有一大堆的工作在等待我去处理呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490170362V希望以后\n',
            '能够看到你们更加杰出的表现。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010170363V#006F嗯，谢谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020170364V#010F那么，\n',
            '我们也就此告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    NewScene('ED6_DT01/T2200._SN', 101, 0, 0)
    IdleLoop()

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
