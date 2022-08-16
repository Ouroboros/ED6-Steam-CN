import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T0100_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0100_1 ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T0100.x'
    header.mapIndex       = 1
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
    If(
        (
            (Expr.Eval, "OP_29(0x0004, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_172',
    )

    TalkBegin(0x0012)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 0, 0x10)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_10A',
    )

    SetScenaFlags(ScenaFlag(0x0002, 0, 0x10))

    ChrTalk(
        0x00FE,
        (
            '之前真是多谢了。\n',
            '真的是帮了大忙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这里明明是空港城市，\n',
            '还能坚持卖这些小玩意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我嘛，觉得这样正好哦。\n',
            '老妈也真是反应迟钝。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_16C')

    def _loc_10A(): pass

    label('loc_10A')

    ChrTalk(
        0x00FE,
        (
            '这里明明是空港城市，\n',
            '还能坚持卖这些小玩意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我嘛，觉得这样正好哦。\n',
            '老妈也真是反应迟钝。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_16C(): pass

    label('loc_16C')

    TalkEnd(0x0012)

    Jump('loc_12F8')

    def _loc_172(): pass

    label('loc_172')

    If(
        (
            (Expr.Eval, "OP_29(0x0004, 0x01, 0x0020)"),
            (Expr.Eval, "OP_40(0x0325)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_CED',
    )

    EventBegin(0x00)
    Fade(1000)
    ChrSetPos(0x0101, 31400, 0, 29390, 120)
    ChrSetPos(0x0102, 30330, 0, 28560, 120)
    OP_4A(0x0012, 255)
    CameraMove(31410, 0, 29350, 0)
    OP_6C(0, 0)
    OP_0D()
    Sleep(400)

    OP_62(0x0012, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    ChrTurnDirection(0x0012, 0x0101, 400)
    Sleep(400)

    ChrTalk(
        0x0012,
        (
            '#1060150065V啊…………！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#1060150066V……那块石头。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150067V#000F难道……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150068V这就是你刚才在找的石头？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '交出了',
            (TxtCtl.SetColor, 0x2),
            '结晶回路的碎片',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0012,
        (
            '#1060150069V啊，就是它没错。\n',
            '我美丽的石头……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0012, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(400)

    ChrTalk(
        0x0012,
        (
            '#1060150070V……………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_63(0x0012)

    ChrTalk(
        0x0012,
        (
            '#1060150071V……怎么回事，\n',
            '怎么弄得这么脏啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150072V#007F喂喂，\n',
            '发牢骚也要在表示过谢意之后吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#1060150073V啊，知道啦。\n',
            '你们是游击士对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#1060150074V我可是向游击士协会\n',
            '付过酬金的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#1060150075V这下我总该有\n',
            '发牢骚的权利了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010150076V#005F问题的关键根本不在这～里！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020150077V#017F艾丝蒂尔，冷静点，\n',
            '对方只是个孩子而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010150078V#009F哼，知道啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_04EF')
    def lambda_04EF():
        ChrTurnDirection(0x0102, 0x0012, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_04EF)

    Sleep(200)

    ChrTurnDirection(0x0101, 0x0012, 400)

    ChrTalk(
        0x0102,
        (
            '#0020150079V#010F你在找的就是\n',
            '这块结晶回路的碎片吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#1060150080V啊，没错……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#1060150081V……这块石头，\n',
            '是结晶回路？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#1060150082V装在导力器里面的\n',
            '那种结晶回路？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020150083V#019F嗯，\n',
            '这的确就是用耀晶片制成的结晶回路。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020150084V因为已经碎了，\n',
            '所以也没什么能量了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#1060150085V是这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0012, 45, 400)
    OP_62(0x0012, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(400)

    ChrTalk(
        0x0012,
        (
            '#1060150086V这块石头，\n',
            '果然是结晶回路啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#1060150070V……………………',
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
            '#0010150088V#000F？？？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150089V怎么回事呢？\n',
            '干嘛站在那里发呆？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_63(0x0012)
    OP_62(0x0012, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    ChrTurnDirection(0x0012, 0x0101, 400)

    ChrTalk(
        0x0012,
        (
            '#1060150090V……嗯？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#1060150091V啊，没什么，没事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#1060150092V不管怎样，\n',
            '谢谢你们帮我找东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#1060150093V那就这样吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_07D1')
    def lambda_07D1():
        ChrTurnDirection(0x0101, 0x0012, 400)
        Yield()

        Jump('lambda_07D1')

    DispatchAsync2(0x0101, 0x0001, lambda_07D1)

    @scena.Lambda('lambda_07E2')
    def lambda_07E2():
        ChrTurnDirection(0x0102, 0x0012, 400)
        Yield()

        Jump('lambda_07E2')

    DispatchAsync2(0x0102, 0x0001, lambda_07E2)

    ChrWalkTo(0x00FE, 32090, 0, 24090, 5000, 0x00)
    OP_62(0x0012, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0012,
        (
            '#1060150094V啊，对了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x00FE, 0, 400)
    ChrWalkTo(0x00FE, 31250, 0, 28800, 5000, 0x00)

    ChrTalk(
        0x0012,
        (
            '#1060150095V……差点忘了，\n',
            '这东西就给你吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了５个',
            (TxtCtl.SetColor, 0x2),
            '肉馅丸子',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    AddItem(0x01A5, 5)

    ChrTalk(
        0x0012,
        (
            '#1060150096V这些肉丸子对身体很有好处，\n',
            '是老妈刚才给我的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#1060150097V不过味道有些苦，\n',
            '我不喜欢吃。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1060150098V总之，今天还真是谢谢你们啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x00FE, 32140, 0, 18090, 5000, 0x00)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0102, 0x01)

    ChrTalk(
        0x0101,
        (
            '#0010150099V#007F呼～～\n',
            '真是个傲慢的小孩啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020150100V#010F一定是因为正值年少气盛吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020150101V#010F可是，那个孩子……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020150102V为什么要寻找\n',
            '结晶回路这样的东西呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010150103V#501F…………嗯？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150104V这么说来，\n',
            '的确有点不可思议……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150105V#001F哎呀，管他呢。\n',
            '每个人喜欢的东西都不一样嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020150106V#019F哈哈，说得也是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020150107V说不定那个孩子\n',
            '对结晶回路非常有兴趣呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150108V#505F嗯～\n',
            '真不知道那种复杂的机械有什么好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150109V真是个让我无法理解的世界啊～\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020150110V#010F不过，从现在开始\n',
            '你也要主动去了解才行啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020150111V如果不能把结晶回路运用自如，\n',
            '是不能胜任游击士这个工作的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010150112V#007F好～啦，我加把劲就是了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x0012, 62400, 250, 22000, 270)
    RemoveItem(0x0325, 1)
    OP_28(0x0004, 0x04, 0x10)
    OP_28(0x0004, 0x01, 0x0040)
    TerminateThread(0x0012, 0xFF)
    CreateThread(0x0012, 0x00, 0x00, 0x0008)
    PlaySE(23, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【寻找发光的石头】',
            (TxtCtl.SetColor, 0x0),
            '完成！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    EventEnd(0x00)

    Jump('loc_12F8')

    def _loc_CED(): pass

    label('loc_CED')

    If(
        (
            (Expr.Eval, "OP_29(0x0004, 0x00, 0x04)"),
            Expr.Return,
        ),
        'loc_D88',
    )

    TalkBegin(0x0012)

    ChrTalk(
        0x00FE,
        (
            '#1060150028V如果你们找到发光石头的话，\n',
            '赶快来告诉我。应该就在这附近。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1060150029V杂货店这边也找过了，\n',
            '……接下来该找哪里呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0012)

    Jump('loc_12F8')

    def _loc_D88(): pass

    label('loc_D88')

    If(
        (
            (Expr.Eval, "OP_29(0x0004, 0x00, 0x02)"),
            Expr.Return,
        ),
        'loc_11EF',
    )

    EventBegin(0x00)
    Fade(1000)
    ChrSetPos(0x0101, 31400, 0, 29390, 120)
    ChrSetPos(0x0102, 30690, 0, 29150, 133)
    OP_4A(0x0012, 255)
    CameraMove(31410, 0, 29350, 0)
    OP_6C(0, 0)
    OP_0D()
    Sleep(400)

    ChrTalk(
        0x0012,
        (
            '#1060150007V真是奇怪啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#1060150008V……到底掉到哪儿去了呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0012, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    ChrTurnDirection(0x0012, 0x0101, 400)
    Sleep(400)

    ChrTalk(
        0x0012,
        (
            '#1060150009V啊…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#1060150010V……喂喂，\n',
            '我有点事想问你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#1060150011V在这附近看到过\n',
            '一块漂亮的石头吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)

    ChrTalk(
        0x0101,
        (
            '#0010150012V#004F啊？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150013V漂亮的石头？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#1060150014V对呀，漂亮的石头，\n',
            '闪闪发光的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#1060150015V那样的石头\n',
            '会掉到哪儿去呢？ ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150016V#000F是弄丢的东西吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150017V#505F嗯～\n',
            '我们好像也没看到。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150018V大概掉在什么位置呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#1060150019V刚才老妈叫我，\n',
            '我就到杂货铺去了一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#1060150020V一开始石头还在手里的，\n',
            '回头的时候就不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150021V#000F杂货铺是里农老板开的那间吧。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150022V你在杂货铺的门口仔细找过了吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#1060150023V还用你说！\n',
            '不要把我当成小孩子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150024V#004F哎呀，好傲慢的小子～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#1060150025V还好已经委托游击士了，\n',
            '相信很快就能找到的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#1060150026V如果你们找到发光石头的话，\n',
            '一定要赶快来告诉我哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#1060150027V我想应该就在这附近。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0004, 0x04, 0x04)
    OP_28(0x0004, 0x04, 0x08)
    OP_28(0x0004, 0x01, 0x0001)
    OP_28(0x0004, 0x01, 0x0002)
    OP_65(0x01, 0x0001)
    OP_4B(0x0012, 255)
    ChrSetDirection(0x0012, 45, 0)
    EventEnd(0x00)

    Jump('loc_12F8')

    def _loc_11EF(): pass

    label('loc_11EF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Return,
        ),
        'loc_1294',
    )

    ChrSetFlags(0x0012, 0x0010)
    TalkBegin(0x0012)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 0, 0x10)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1249',
    )

    ChrTalk(
        0x00FE,
        (
            '可恶，\n',
            '到哪里去了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有可能的地方\n',
            '已经全找过了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_128C')

    def _loc_1249(): pass

    label('loc_1249')

    ChrTalk(
        0x00FE,
        (
            '真是奇怪啊……\n',
            '为什么会找不到呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊，到底掉到哪儿去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_128C(): pass

    label('loc_128C')

    ChrClearFlags(0x0012, 0x0010)

    Jump('loc_12F5')

    def _loc_1294(): pass

    label('loc_1294')

    ChrSetFlags(0x0012, 0x0010)
    TalkBegin(0x0012)

    ChrTalk(
        0x00FE,
        (
            '啊～\n',
            '这附近有各种各样的破烂啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽说都是些有趣的东西，\n',
            '不过通通都不值钱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x0012, 0x0010)
    def _loc_12F5(): pass

    label('loc_12F5')

    TalkEnd(0x0012)

    def _loc_12F8(): pass

    label('loc_12F8')

    Return()

# id: 0x0001 offset: 0x12F9
@scena.Code('func_01_12F9')
def func_01_12F9():
    TalkBegin(0x0012)

    If(
        (
            (Expr.Eval, "OP_29(0x0004, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_13B2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 0, 0x10)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_137A',
    )

    SetScenaFlags(ScenaFlag(0x0002, 0, 0x10))

    ChrTalk(
        0x00FE,
        (
            '这里明明是空港城市，\n',
            '还能坚持卖这些小玩意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '老妈反应这么迟钝，真是可叹啊。\n',
            '哎呀，我说真的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_13AF')

    def _loc_137A(): pass

    label('loc_137A')

    ChrTalk(
        0x00FE,
        (
            '老妈反应这么迟钝，真是可叹啊。\n',
            '哎呀，我说真的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_13AF(): pass

    label('loc_13AF')

    Jump('loc_1CE3')

    def _loc_13B2(): pass

    label('loc_13B2')

    If(
        (
            (Expr.Eval, "OP_29(0x0004, 0x01, 0x0002)"),
            (Expr.Eval, "OP_40(0x0325)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1945',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0004, 0x00, 0x04)"),
            Expr.Return,
        ),
        'loc_143C',
    )

    ChrTurnDirection(0x00FE, 0x0101, 0)
    OP_62(0x0012, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    Sleep(500)

    ChrTalk(
        0x00FE,
        (
            '啊…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……喂，那个。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x00FE, 0)

    ChrTalk(
        0x0101,
        (
            '#000F是这个吗？\n',
            '你要找的齿轮。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1541')

    def _loc_143C(): pass

    label('loc_143C')

    ChrTalk(
        0x00FE,
        (
            '喂喂，我有点事想问你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在这附近看到过一个齿轮吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x00FE, 0)

    ChrTalk(
        0x0101,
        (
            '#000F啊？齿轮？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '对啊。\n',
            '闪着金属光泽的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '会掉到哪儿去呢？ ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还好已经委托游击士了，\n',
            '相信很快就能找到的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊，说起来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#000F难道是这个？\n',
            '你要找的齿轮。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1541(): pass

    label('loc_1541')

    OP_28(0x0004, 0x04, 0x10)
    OP_28(0x0004, 0x01, 0x0004)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '交出了',
            (TxtCtl.SetColor, 0x2),
            '齿轮',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    RemoveItem(0x0325, 1)

    ChrTalk(
        0x00FE,
        (
            '啊，就是它没错。我的齿轮……',
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
            '……怎么回事，怎么弄得这么脏啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F喂喂，\n',
            '发牢骚也要在表示过谢意之后吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#000F这可是我们特地从\n',
            '排水沟里帮你捞上来的哦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我可是向游击士协会\n',
            '付过酬金的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这下我总该有发牢骚的权利了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#002F#5S问题的关键根本不在这～里！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……不管怎样，\n',
            '谢谢你们帮我找东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那就这样吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x0012, 0x0040)
    CreateThread(0x0101, 0x00, 0x01, 0x0006)
    CreateThread(0x0102, 0x00, 0x01, 0x0007)
    CreateThread(0x0012, 0x00, 0x01, 0x0005)
    SetScenaFlags(ScenaFlag(0x0002, 1, 0x11))
    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))
    SetScenaFlags(ScenaFlag(0x0001, 7, 0xF))
    OP_A5(0x0011)
    OP_A5(0x000E)
    OP_A5(0x000F)
    ChrSetPos(0x0012, 62400, 250, 22000, 270)
    ChrClearFlags(0x0012, 0x0040)
    ChrClearFlags(0x00FE, 0x0080)
    OP_85(0x0012)
    OP_62(0x0101, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#002F呼～～真是个傲慢的小孩啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 0)

    ChrTalk(
        0x0102,
        (
            '#010F艾丝蒂尔，冷静一点。\n',
            ' ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 0)

    ChrTalk(
        0x0101,
        (
            '#000F我、我知道啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirectionByPos(0x0102, 68300, 39000, 500)

    ChrTalk(
        0x0102,
        (
            '#0020150101V#010F可是，那个孩子……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#010F为什么要找齿轮这样的东西呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F……啊？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#000F嗯，\n',
            '听你这么一说，的确有点不可思议……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#000F哎呀，管他呢。\n',
            '每个人喜欢的东西都不一样嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 0)

    ChrTalk(
        0x0102,
        (
            '#010F哈哈，说得也是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#010F……那，\n',
            '那么我们也走吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#010F还得回协会\n',
            '报告一下情况呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯，走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_92(0x0001, 0x0000, 0, 3000, 0x00)
    OP_30(0x00)
    EventEnd(0x00)

    Jump('loc_1CE3')

    def _loc_1945(): pass

    label('loc_1945')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Return,
        ),
        'loc_1C12',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0004, 0x00, 0x04)"),
            Expr.Return,
        ),
        'loc_19C5',
    )

    ChrTalk(
        0x00FE,
        (
            '如果你们找到齿轮的话，\n',
            '赶快来告诉我。应该就在这附近。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……杂货店这边也找过了，\n',
            '接下来该找哪里呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C0F')

    def _loc_19C5(): pass

    label('loc_19C5')

    OP_28(0x0004, 0x04, 0x04)
    OP_28(0x0004, 0x04, 0x08)
    OP_28(0x0004, 0x01, 0x0001)
    OP_28(0x0004, 0x04, 0x02)

    ChrTalk(
        0x00FE,
        (
            '喂喂，我有点事想问你们。\n',
            '在这附近看到过一个齿轮吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x00FE, 0)

    ChrTalk(
        0x0101,
        (
            '#000F啊？齿轮？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '对啊。\n',
            '闪着金属光泽的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '会掉到哪儿去呢？ ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F弄丢了？\n',
            '嗯～我们好像也没看到。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#000F大概掉在什么位置呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '刚才老妈叫我，\n',
            '我就到杂货铺去了一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一开始石头还在手里的，\n',
            '回头的时候就不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F那应该就很可能掉在店前面了。\n',
            '你已经找过了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还用你说！\n',
            '不要把我当成小孩子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#002F哎呀，好傲慢的小子～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还好已经委托游击士了，\n',
            '相信很快就能找到的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是找到了，赶快来告诉我。\n',
            '我想应该就在这附近。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C0F(): pass

    label('loc_1C0F')

    Jump('loc_1CE3')

    def _loc_1C12(): pass

    label('loc_1C12')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 0, 0x10)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1C96',
    )

    SetScenaFlags(ScenaFlag(0x0002, 0, 0x10))

    ChrTalk(
        0x00FE,
        (
            '……飞艇这东西真不错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我来的时候也坐过，\n',
            '又大又舒服……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我的经验告诉我，\n',
            '这东西肯定是由导力器驱动的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1CE3')

    def _loc_1C96(): pass

    label('loc_1C96')

    ChrTalk(
        0x00FE,
        (
            '不错嘛，飞艇这玩意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我的经验告诉我，\n',
            '这东西肯定是由导力器驱动的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1CE3(): pass

    label('loc_1CE3')

    TalkEnd(0x0012)

    Return()

# id: 0x0002 offset: 0x1CE7
@scena.Code('func_02_1CE7')
def func_02_1CE7():
    TalkBegin(0x0013)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Return,
        ),
        'loc_2128',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0050, 0, 0x280)),
            Expr.Return,
        ),
        'loc_1D90',
    )

    ChrTurnDirection(0x0013, 0x0000, 0)

    ChrTalk(
        0x00FE,
        (
            '没办法，再在这里呆一阵\n',
            '就上格兰赛尔去试试吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我家那傻小子\n',
            '真是一点用都没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '才刚帮了一会儿忙\n',
            '又不知道跑到哪儿去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0013, 180, 0)

    Jump('loc_2125')

    def _loc_1D90(): pass

    label('loc_1D90')

    SetScenaFlags(ScenaFlag(0x0050, 0, 0x280))

    ChrTalk(
        0x00FE,
        (
            '哈啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '特地大老远跑来这里，\n',
            '真是白折腾一场。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '又没有顾客，\n',
            '商店也比想象中的破旧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '乡下果然\n',
            '就是乡下啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(200)

    ChrTalk(
        0x0101,
        (
            '#009F（哼。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0013, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '……嗯？\n',
            '你们是谁？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '算了，不管是谁，\n',
            '我给你们打折，随便买点什么吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#004F哎……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这个木雕小工艺品怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这么精细的工艺，\n',
            '只有在卡尔瓦德才买得到哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#501F卡尔瓦德，嗯～\n',
            '是我们的邻国吗……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#010F卡尔瓦德共和国是\n',
            '利贝尔王国东面的国家哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#008F这、这我当然知道啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1F8D')
    def lambda_1F8D():
        ChrTurnDirection(0x0102, 0x0013, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1F8D)

    ChrTurnDirection(0x0101, 0x0013, 400)

    ChrTalk(
        0x0102,
        (
            '#010F但是，卡尔瓦德的民间工艺品吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我想要是在王都摆卖的话，\n',
            '一定会更受欢迎的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0013, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '哈啊……\n',
            '果然是这样吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我本来以为稍微乡下点的地方会更好卖，\n',
            '但这里也实在有点乡下过头了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(200)

    ChrTalk(
        0x0101,
        (
            '#009F（哼哼。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0013, 0x0000, 400)

    ChrTalk(
        0x00FE,
        (
            '没办法，再在这里呆一阵\n',
            '就上格兰赛尔去试试吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……话说回来，\n',
            '我家的卡雷尔在做什么呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '才刚帮了一会儿忙\n',
            '又在到处乱转了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0013, 180, 0)

    def _loc_2125(): pass

    label('loc_2125')

    Jump('loc_2248')

    def _loc_2128(): pass

    label('loc_2128')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0003, 1, 0x19)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_21D8',
    )

    SetScenaFlags(ScenaFlag(0x0003, 1, 0x19))

    ChrTalk(
        0x00FE,
        (
            '这里虽然是个小的城镇，\n',
            '不过商店里东西的品种还是不少哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '托导力器的福， \n',
            '利贝尔王国和以前大不相同了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，明天要更加努力才行，\n',
            '销售额可不能降低呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2248')

    def _loc_21D8(): pass

    label('loc_21D8')

    ChrTalk(
        0x00FE,
        (
            '这里虽然是个小的城镇，\n',
            '不过商店里东西的品种还是不少哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，明天要更加努力才行，\n',
            '销售额可不能降低呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2248(): pass

    label('loc_2248')

    TalkEnd(0x0013)

    Return()

# id: 0x0003 offset: 0x224C
@scena.Code('func_03_224C')
def func_03_224C():
    TalkBegin(0x0014)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004D, 0, 0x268)),
            Expr.Return,
        ),
        'loc_22B4',
    )

    ChrTalk(
        0x00FE,
        (
            '唔～～啊，\n',
            '今天天气依旧很暖和啊～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '睡个午觉\n',
            '一定很舒服呢～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(402, 0x00, 0x64)

    ChrTalk(
        0x0015,
        (
            '喵～～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3389')

    def _loc_22B4(): pass

    label('loc_22B4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004C, 1, 0x261)),
            Expr.Return,
        ),
        'loc_243D',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0009, 0x01, 0x8000)"),
            Expr.Return,
        ),
        'loc_2321',
    )

    OP_62(0x0014, 0x00000000, 2000, 0x1C, 0x21, 0x000000FA, 0x00)
    Sleep(500)

    ChrTalk(
        0x00FE,
        (
            '…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……唔呀唔呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '……咕噜咕噜咕噜咕噜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_63(0x0014)

    Jump('loc_243A')

    def _loc_2321(): pass

    label('loc_2321')

    If(
        (
            (Expr.Eval, "OP_29(0x0009, 0x00, 0x04)"),
            (Expr.Eval, "OP_29(0x0009, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_23E2',
    )

    OP_28(0x0009, 0x01, 0x8000)

    ChrTalk(
        0x0101,
        (
            '#0010150667V#004F（啊……！）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150668V（小猫回来了。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1090150664V…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1090150665V……唔呀唔呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1090150671V……咕噜咕噜咕噜咕噜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_63(0x0014)

    Jump('loc_243A')

    def _loc_23E2(): pass

    label('loc_23E2')

    OP_62(0x0014, 0x00000000, 2000, 0x1C, 0x21, 0x000000FA, 0x00)
    Sleep(500)

    ChrTalk(
        0x00FE,
        (
            '…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……唔呀唔呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '……咕噜咕噜咕噜咕噜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_63(0x0014)

    def _loc_243A(): pass

    label('loc_243A')

    Jump('loc_3389')

    def _loc_243D(): pass

    label('loc_243D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Return,
        ),
        'loc_26D8',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0009, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_2544',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 2, 0x12)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_24EA',
    )

    SetScenaFlags(ScenaFlag(0x0002, 2, 0x12))
    ChrClearFlags(0x0014, 0x0010)

    ChrTalk(
        0x00FE,
        (
            '哎呀～～\n',
            '这不是尤基士君吗～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哦呵呵～㈱\n',
            '要不要和阿姨一起来午睡呢～～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0102,
        (
            '#018F……还是免了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2541')

    def _loc_24EA(): pass

    label('loc_24EA')

    ChrClearFlags(0x0014, 0x0010)

    ChrTalk(
        0x00FE,
        (
            '哎呀～～\n',
            '这不是尤基士君吗～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哦呵呵～㈱\n',
            '要不要和阿姨一起来午睡呢～～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2541(): pass

    label('loc_2541')

    Jump('loc_26D5')

    def _loc_2544(): pass

    label('loc_2544')

    If(
        (
            (Expr.Eval, "OP_29(0x0009, 0x01, 0x8000)"),
            Expr.Return,
        ),
        'loc_25A9',
    )

    ChrTalk(
        0x00FE,
        (
            '尤基士君～\n',
            '不好意思呢～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '小安莉尔\n',
            '自己回我这里来了哦～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(402, 0x00, 0x64)

    ChrTalk(
        0x0015,
        (
            '喵～～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_26D5')

    def _loc_25A9(): pass

    label('loc_25A9')

    If(
        (
            (Expr.Eval, "OP_29(0x0009, 0x00, 0x04)"),
            (Expr.Eval, "OP_29(0x0009, 0x01, 0x8000)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2672',
    )

    OP_28(0x0009, 0x01, 0x8000)

    ChrTalk(
        0x0101,
        (
            '#004F啊……！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '猫也会自己回家？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎哟哟～～\n',
            '这不是尤基士君吗～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '小安莉尔\n',
            '自己回我这里来了哦～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔～～啊，\n',
            '多么可爱伶俐的小乖乖啊～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(402, 0x00, 0x64)

    ChrTalk(
        0x0015,
        (
            '喵～～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_26D5')

    def _loc_2672(): pass

    label('loc_2672')

    ChrTalk(
        0x00FE,
        (
            '真是的～～\n',
            '那个小安莉尔\n',
            '到底去了哪儿呢～～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我真的是好担心呢～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(402, 0x00, 0x64)

    ChrTalk(
        0x0015,
        (
            '喵～～～呼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_26D5(): pass

    label('loc_26D5')

    Jump('loc_3389')

    def _loc_26D8(): pass

    label('loc_26D8')

    If(
        (
            (Expr.Eval, "OP_29(0x0009, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_273C',
    )

    ChrTalk(
        0x00FE,
        (
            '已经中午了， \n',
            '我要好好地睡上顿午觉～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '喂～～小安莉尔～～㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(402, 0x00, 0x64)

    ChrTalk(
        0x0015,
        (
            '喵～～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3389')

    def _loc_273C(): pass

    label('loc_273C')

    If(
        (
            (Expr.Eval, "OP_29(0x0009, 0x01, 0x0002)"),
            (Expr.Eval, "OP_29(0x0009, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2912',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 2, 0x12)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_287B',
    )

    SetScenaFlags(ScenaFlag(0x0002, 2, 0x12))
    ChrClearFlags(0x0014, 0x0010)
    ChrTurnDirection(0x0014, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '#1090150653V找到小安莉尔了吗～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150654V#000F嗯！找到了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150655V#007F……但是又被它给跑掉了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1090150656V哎呀，怎么会这样呢～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1090150657V奇怪了啊～\n',
            '它本来不是很怕陌生人的啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1090150658V阿姨会一直在这里等着的，\n',
            '拜托了啊，尤基士君。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_290F')

    def _loc_287B(): pass

    label('loc_287B')

    ChrClearFlags(0x0014, 0x0010)
    ChrTurnDirection(0x0014, 0x0000, 0)

    ChrTalk(
        0x00FE,
        (
            '#1090150659V真是奇怪啊，怎么会逃跑呢～？\n',
            '它本来不是很怕陌生人的啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1090150660V阿姨会一直在这里等着的，\n',
            '拜托了啊，尤基士君。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_290F(): pass

    label('loc_290F')

    Jump('loc_3389')

    def _loc_2912(): pass

    label('loc_2912')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 7, 0x24F)),
            Expr.Return,
        ),
        'loc_3285',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0009, 0x00, 0x04)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3212',
    )

    OP_28(0x0009, 0x04, 0x04)
    OP_28(0x0009, 0x04, 0x08)
    OP_28(0x0009, 0x04, 0x02)
    OP_28(0x0009, 0x01, 0x0001)
    EventBegin(0x00)
    Fade(1000)
    CameraMove(36950, 0, 57050, 0)
    OP_6C(0, 0)
    ChrSetPos(0x0101, 38560, 0, 57230, 270)
    ChrSetPos(0x0102, 37800, 0, 58080, 225)

    If(
        (
            (Expr.Eval, "OP_42(0x000F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_29AF',
    )

    ChrSetPos(0x0002, 39290, 0, 58080, 211)
    ChrSetPos(0x0003, 40280, 0, 58050, 212)

    Jump('loc_29CE')

    def _loc_29AF(): pass

    label('loc_29AF')

    If(
        (
            (Expr.Eval, "OP_42(0x000E)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_29CE',
    )

    ChrSetPos(0x0002, 39290, 0, 58080, 211)

    def _loc_29CE(): pass

    label('loc_29CE')

    OP_0D()
    Sleep(100)

    ChrTalk(
        0x00FE,
        (
            '#1090150612V真是的～\n',
            '究竟跑到哪儿去了呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1090150613V唉～～\n',
            '不知道尤基士看到委托了没有～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150614V#000F阿姨，您在等游击士吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x0014, 0x0010)
    ChrTurnDirection(0x0014, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '#1090150615V嗯，是啊～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1090150616V哎呀～～？\n',
            '难道你就是？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150617V#006F嗯⊙我就是游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0014, 0x0102, 0)

    ChrTalk(
        0x00FE,
        (
            '#1090150618V难道～那边那位也是～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0014, 0)

    ChrTalk(
        0x0102,
        (
            '#0020150619V#010F嗯，我也是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1090150620V哎呀呀，阿姨真的很高兴啊～☆',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1090150621V最近叫做尤基士的人\n',
            '好像很多呢～～',
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
            '#0010150622V#501F？？？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1090150623V哎呀，你们好像是姐弟嘛～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1090150624V对呀，对呀～～\n',
            '有相同的名字的一般就是一家人的嘛～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150625V#505F嗯……\n',
            '可以说是姐弟没错啦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 0)

    ChrTalk(
        0x0102,
        (
            '#0020150626V#014F（……艾丝蒂尔，\n',
            '　这位阿姨好像不知道什么是游击士啊。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020150627V#014F（她好像把游击士这个词的读音\n',
            '　当作人的名字了啊。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 0)
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010150628V#004F（…………不、不会吧～）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1090150629V哎呀～～你们两个\n',
            '在唧唧喳喳的说些什么呢～～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020150630V#017F（有些麻烦啊，只有顺着她的话说了。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150631V#506F（……知道～了。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0014, 400)
    Sleep(200)

    ChrTurnDirection(0x0101, 0x0014, 400)

    ChrTalk(
        0x0102,
        (
            '#0020150632V#010F是这样，\n',
            '您有什么困难吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0014, 0x0102, 0)

    ChrTalk(
        0x00FE,
        (
            '#1090150633V哎呀～这孩子看上去这么可爱，\n',
            '没想到洞察力这么敏锐呢～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1090150634V男孩子果然就是用心啊～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150635V#509F……阿姨，您到底有没有困难？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0014, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '#1090150636V啊，对了对了。\n',
            '说实话啊～\n',
            '我真的好苦恼的哦～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1090150637V我家的小安莉尔\n',
            '到现在还没有回来啊～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1090150638V我只不过在茶座小睡了一觉，\n',
            '就那么一不留神，它就不见了～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150639V#000F小安莉尔？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1090150640V是小猫呀～\n',
            '好可爱的小猫呢～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1090150641V而且不仅是外表可爱，\n',
            '内心也好温顺的哦～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020150642V#010F是什么颜色的小猫呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1090150643V嗯～让我想想啊～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1090150644V好像在秋天的夕阳中\n',
            '那种小麦田的颜色哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020150645V#010F……小麦色，对吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1090150646V它可能正在外面到处乱跑呢，\n',
            '拜托你们帮我把它捉回来好吗～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020150647V#010F我明白了，\n',
            '首先从茶座周围开始找吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020150648V#010F一旦找到了，\n',
            '我们就会回来告诉您的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1090150649V阿姨就在这里\n',
            '等着你们哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1090150650V拜托了啊，尤基士君。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(50)

    EventEnd(0x04)

    Jump('loc_3282')

    def _loc_3212(): pass

    label('loc_3212')

    ChrClearFlags(0x0014, 0x0010)
    ChrTurnDirection(0x0014, 0x0000, 0)

    ChrTalk(
        0x00FE,
        (
            '#1090150651V阿姨就在这里\n',
            '等着你们哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1090150652V小安莉尔就拜托你们去找了啊，\n',
            '尤基士君。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_3282(): pass

    label('loc_3282')

    Jump('loc_3389')

    def _loc_3285(): pass

    label('loc_3285')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 1, 0x239)),
            Expr.Return,
        ),
        'loc_32C7',
    )

    ChrTalk(
        0x00FE,
        (
            '哎～～真是不省心的孩子～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是不是在哪儿睡觉呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3389')

    def _loc_32C7(): pass

    label('loc_32C7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            Expr.Return,
        ),
        'loc_3329',
    )

    OP_62(0x0014, 0x00000000, 2000, 0x1C, 0x21, 0x000000FA, 0x00)
    Sleep(500)

    ChrTalk(
        0x00FE,
        (
            '…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……唔呀唔呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '……咕噜咕噜咕噜咕噜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_63(0x0014)

    Jump('loc_3389')

    def _loc_3329(): pass

    label('loc_3329')

    ChrTalk(
        0x00FE,
        (
            '嗯呼呼呼，\n',
            '今天天气很暖和哦～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可以睡上美美的一觉了～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(402, 0x00, 0x64)

    ChrTalk(
        0x0015,
        (
            '喵喵喵～～～咪咪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3389(): pass

    label('loc_3389')

    TalkEnd(0x0014)
    ChrSetFlags(0x0014, 0x0010)

    Return()

# id: 0x0004 offset: 0x3392
@scena.Code('func_04_3392')
def func_04_3392():
    If(
        (
            (Expr.Eval, "OP_29(0x0004, 0x01, 0x0020)"),
            Expr.Return,
        ),
        'loc_339E',
    )

    Return()

    def _loc_339E(): pass

    label('loc_339E')

    If(
        (
            (Expr.Eval, "OP_29(0x0004, 0x01, 0x0004)"),
            Expr.Return,
        ),
        'loc_34EA',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_343A',
    )

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020150049V#010F如果想要弄清是什么掉下去的话，\n',
            '就去地下水路调查一下吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020150050V地下水路的入口在教堂的后面。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_34E4')

    def _loc_343A(): pass

    label('loc_343A')

    ChrTalk(
        0x0101,
        (
            '#0010150051V#505F唔……\n',
            '什么东西掉下去了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020150052V#010F如果想要弄清楚的话，\n',
            '我们就去下面调查一下吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020150050V地下水路的入口在教堂的后面。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_34E4(): pass

    label('loc_34E4')

    TalkEnd(0x00FF)

    Jump('loc_39ED')

    def _loc_34EA(): pass

    label('loc_34EA')

    OP_28(0x0004, 0x01, 0x0004)
    OP_28(0x0004, 0x01, 0x0008)
    OP_28(0x0004, 0x01, 0x0010)
    EventBegin(0x00)
    Fade(1000)
    ChrSetPos(0x0000, 46120, 0, 26090, 225)
    ChrSetPos(0x0001, 45540, 0, 27200, 180)

    If(
        (
            (Expr.PushValueByIndex, 0x64),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            (Expr.PushValueByIndex, 0x64),
            (Expr.PushLong, 0x5A),
            Expr.Leq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3546',
    )

    OP_6C(350000, 0)

    Jump('loc_3567')

    def _loc_3546(): pass

    label('loc_3546')

    If(
        (
            (Expr.PushValueByIndex, 0x64),
            (Expr.PushLong, 0x5A),
            Expr.Gtr,
            (Expr.PushValueByIndex, 0x64),
            (Expr.PushLong, 0xB4),
            Expr.Lss,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3567',
    )

    OP_6C(350000, 0)

    Jump('loc_3567')

    def _loc_3567(): pass

    label('loc_3567')

    OP_0D()

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_36CC',
    )

    Sleep(400)

    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010150030V#004F……哎？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020150031V#010F怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150032V#002F那是什么……\n',
            '排水沟里面好像有东西在发光。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0102, 45430, 0, 26540, 2000, 0x00)
    LoadEffect(0x00, 'map\\\\evsepith.eff')
    PlayEffect(0x00, 0xFF, 0x00FF, 45050, 200, 25150, 0, 0, 0, 200, 400, 200, 0x00FF, 0, 0, 0, 0)
    Sleep(1000)

    ChrTalk(
        0x0102,
        (
            '#0020150033V#014F………果然。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020150034V好像有东西落到排水沟的沟底了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3869')

    def _loc_36CC(): pass

    label('loc_36CC')

    Sleep(400)

    OP_62(0x0102, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    ChrTalk(
        0x0102,
        (
            '#0020150035V#014F……嗯？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0001, 0x0000, 0)

    ChrTalk(
        0x0101,
        (
            '#0010150036V#000F怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020150037V#014F那是什么……\n',
            '排水沟里面好像有东西在发光。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirectionByPos(0x0101, 45430, 26540, 400)

    ChrTalk(
        0x0101,
        (
            '#0010150038V#000F哪里哪里？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0101, 45430, 0, 26540, 2000, 0x00)
    LoadEffect(0x00, 'map\\\\evsepith.eff')
    PlayEffect(0x00, 0xFF, 0x00FF, 45050, 200, 25150, 0, 0, 0, 200, 400, 200, 0x00FF, 0, 0, 0, 0)
    Sleep(800)

    ChrTalk(
        0x0101,
        (
            '#0010150039V#004F啊，是真的。\n',
            '还在闪闪发光呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020150040V#010F好像有东西落到排水沟的沟底了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3869(): pass

    label('loc_3869')

    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010150041V#505F排水沟的沟底？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020150042V#015F你忘记了城里的地下有什么了吗？\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020150043V不久之前我们才去过的。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150044V#508F啊，对呀！是地下水路。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020150045V#010F在实地研修时下去过的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020150046V地下水路的入口在教堂的后面。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020150047V如果想要弄清楚的话，\n',
            '我们就去下面调查一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150048V#006F嗯，去看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_65(0x02, 0x0001)
    StopEffect(0x00, 0x00)
    OP_84(0x00)
    EventEnd(0x00)
    def _loc_39ED(): pass

    label('loc_39ED')

    Return()

# id: 0x0005 offset: 0x39EE
@scena.Code('func_05_39EE')
def func_05_39EE():
    ChrSetFlags(0x0012, 0x0040)
    OP_A6(0x0011)
    ChrWalkTo(0x00FE, 68300, 0, 39000, 7000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)
    ClearScenaFlags(ScenaFlag(0x0002, 1, 0x11))

    Return()

# id: 0x0006 offset: 0x3A13
@scena.Code('func_06_3A13')
def func_06_3A13():
    OP_A6(0x000E)
    def _loc_3A16(): pass

    label('loc_3A16')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 1, 0x11)),
            Expr.Return,
        ),
        'loc_3A28',
    )

    ChrTurnDirection(0x00FE, 0x0012, 0)
    Yield()

    Jump('loc_3A16')

    def _loc_3A28(): pass

    label('loc_3A28')

    ClearScenaFlags(ScenaFlag(0x0001, 6, 0xE))

    Return()

# id: 0x0007 offset: 0x3A2C
@scena.Code('func_07_3A2C')
def func_07_3A2C():
    OP_A6(0x000F)
    def _loc_3A2F(): pass

    label('loc_3A2F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 1, 0x11)),
            Expr.Return,
        ),
        'loc_3A41',
    )

    ChrTurnDirection(0x00FE, 0x0012, 0)
    Yield()

    Jump('loc_3A2F')

    def _loc_3A41(): pass

    label('loc_3A41')

    ClearScenaFlags(ScenaFlag(0x0001, 7, 0xF))

    Return()

# id: 0x0008 offset: 0x3A45
@scena.Code('func_08_3A45')
def func_08_3A45():
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
        32,
        0,
        (
            TXT(0x00, '进入地下水路\n'),
            TXT(0x01, '离开\n'),
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

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_3A89'),
        (0x00000001, 'loc_3A95'),
        (-1, 'loc_3A9B'),
    )

    def _loc_3A89(): pass

    label('loc_3A89')

    NewScene('ED6_DT01/C0500._SN', 0, 0, 0)
    IdleLoop()

    Jump('loc_3A9B')

    def _loc_3A95(): pass

    label('loc_3A95')

    TalkEnd(0x00FF)

    Jump('loc_3A9B')

    def _loc_3A9B(): pass

    label('loc_3A9B')

    Sleep(30)

    Return()

# id: 0x0009 offset: 0x3AA1
@scena.Code('func_09_3AA1')
def func_09_3AA1():
    FadeIn(500, 0)
    CameraMove(76970, 0, 20370, 0)
    ChrSetPos(0x0101, 76970, 0, 20370, 180)
    ChrSetPos(0x0102, 76970, 0, 20370, 0)
    OP_30(0x00)
    OP_0D()
    MapSetFlags(0x00000001)
    MapClearFlags(0x00000080)

    Return()

# id: 0x000A offset: 0x3AEB
@scena.Code('func_0A_3AEB')
def func_0A_3AEB():
    If(
        (
            (Expr.Eval, "OP_29(0x0009, 0x00, 0x40)"),
            Expr.Return,
        ),
        'loc_3AF8',
    )

    Jump('loc_3E00')

    def _loc_3AF8(): pass

    label('loc_3AF8')

    If(
        (
            (Expr.Eval, "OP_29(0x0009, 0x01, 0x0002)"),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x0009, 0x00, 0x04)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3E00',
    )

    OP_28(0x0009, 0x01, 0x0002)
    EventBegin(0x00)
    Fade(1000)
    ChrSetPos(0x0016, 58830, 0, 40470, 165)
    ChrClearFlags(0x0016, 0x0080)
    ChrSetFlags(0x0016, 0x0040)
    CameraMove(59150, 0, 42330, 0)
    OP_6C(135000, 0)
    ChrSetPos(0x0101, 59390, 0, 55350, 176)
    ChrSetPos(0x0102, 57010, 0, 55120, 164)

    If(
        (
            (Expr.Eval, "OP_42(0x000F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3BA2',
    )

    ChrSetPos(0x0002, 59390, 0, 57350, 176)
    ChrSetPos(0x0003, 57010, 0, 57120, 164)

    Jump('loc_3BC1')

    def _loc_3BA2(): pass

    label('loc_3BA2')

    If(
        (
            (Expr.Eval, "OP_42(0x000E)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3BC1',
    )

    ChrSetPos(0x0002, 59390, 0, 57350, 176)

    def _loc_3BC1(): pass

    label('loc_3BC1')

    OP_0D()

    @scena.Lambda('lambda_3BC8')
    def lambda_3BC8():
        OP_6C(180000, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_3BC8)

    @scena.Lambda('lambda_3BD8')
    def lambda_3BD8():
        CameraMove(58950, 0, 46580, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_3BD8)

    ChrWalkTo(0x0016, 58940, 0, 46650, 2000, 0x00)
    ChrWalkTo(0x0101, 58910, 0, 52330, 6000, 0x00)

    ChrTalk(
        0x0101,
        (
            '#0010150701V#004F啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0016, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(400)

    OP_63(0x0016)
    OP_62(0x0016, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(600)

    @scena.Lambda('lambda_3C69')
    def lambda_3C69():
        ChrWalkTo(0x0101, 59740, 0, 43800, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3C69)

    @scena.Lambda('lambda_3C84')
    def lambda_3C84():
        ChrWalkTo(0x0102, 58510, 0, 46160, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_3C84)

    If(
        (
            (Expr.Eval, "OP_42(0x000F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3CE0',
    )

    @scena.Lambda('lambda_3CAD')
    def lambda_3CAD():
        ChrWalkTo(0x0002, 59230, 0, 48990, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_3CAD)

    @scena.Lambda('lambda_3CC8')
    def lambda_3CC8():
        ChrWalkTo(0x0003, 58260, 0, 48470, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_3CC8)

    Jump('loc_3D09')

    def _loc_3CE0(): pass

    label('loc_3CE0')

    If(
        (
            (Expr.Eval, "OP_42(0x000E)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3D09',
    )

    @scena.Lambda('lambda_3CF4')
    def lambda_3CF4():
        ChrWalkTo(0x0002, 59230, 0, 48990, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_3CF4)

    def _loc_3D09(): pass

    label('loc_3D09')

    ChrWalkTo(0x0016, 59080, 0, 44310, 6000, 0x00)

    @scena.Lambda('lambda_3D23')
    def lambda_3D23():
        CameraMove(59770, 0, 44910, 2000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_3D23)

    ChrWalkTo(0x0016, 61570, 0, 38330, 6000, 0x00)
    ChrSetFlags(0x0016, 0x0080)
    ChrClearFlags(0x0016, 0x0040)
    WaitForThreadExit(0x0000, 0x0003)
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010150702V#002F约修亚，刚才那只小猫……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020150703V#010F似乎就是那位阿姨要找的小猫呢。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150704V#002F绝对错不了啦，\n',
            '快追上它！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(50)

    EventEnd(0x04)

    Jump('loc_3E00')

    def _loc_3E00(): pass

    label('loc_3E00')

    Return()

# id: 0x000B offset: 0x3E01
@scena.Code('func_0B_3E01')
def func_0B_3E01():
    If(
        (
            (Expr.Eval, "OP_29(0x0009, 0x00, 0x40)"),
            Expr.Return,
        ),
        'loc_3E0E',
    )

    Jump('loc_40BC')

    def _loc_3E0E(): pass

    label('loc_3E0E')

    If(
        (
            (Expr.Eval, "OP_29(0x0009, 0x01, 0x0002)"),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x0009, 0x00, 0x04)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_40BC',
    )

    OP_28(0x0009, 0x01, 0x0002)
    EventBegin(0x00)
    MapClearFlags(0x00000001)
    ChrSetPos(0x0016, 48900, 0, 84200, 180)
    ChrClearFlags(0x0016, 0x0080)
    ChrClearFlags(0x0016, 0x0008)
    ChrSetFlags(0x0016, 0x0040)
    CreateThread(0x0016, 0x00, 0x01, 0x000C)
    CreateThread(0x0016, 0x01, 0x01, 0x000D)
    Fade(1000)
    ChrSetPos(0x0002, 47800, 0, 50200, 0)
    ChrSetPos(0x0003, 46800, 0, 50200, 0)
    Sleep(2000)

    ChrSetPos(0x0000, 48800, 0, 50200, 0)
    ChrSetPos(0x0001, 48800, 0, 50200, 0)
    OP_62(0x0016, 0x00000000, 1700, 0x08, 0x09, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    ChrWalkTo(0x0016, 49100, 0, 71400, 3000, 0x00)
    OP_63(0x0016)
    Sleep(500)

    ChrSetPos(0x0000, 48800, 0, 59200, 0)
    ChrSetPos(0x0001, 48800, 0, 59200, 0)

    ChrTalk(
        0x0101,
        (
            '#0010150701V#004F啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0016, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(500)

    OP_63(0x0016)
    OP_62(0x0016, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(600)

    CreateThread(0x0101, 0x00, 0x01, 0x000F)
    CreateThread(0x0102, 0x00, 0x01, 0x0010)
    CreateThread(0x0016, 0x00, 0x01, 0x000E)
    SetScenaFlags(ScenaFlag(0x0002, 5, 0x15))
    SetScenaFlags(ScenaFlag(0x0002, 3, 0x13))
    SetScenaFlags(ScenaFlag(0x0002, 4, 0x14))
    OP_A5(0x0015)
    OP_A5(0x0013)
    OP_A5(0x0014)
    ChrSetPos(0x0016, 5488, 0, 16806, 0)
    ChrSetFlags(0x0016, 0x0080)
    ChrSetFlags(0x0016, 0x0008)

    ChrTalk(
        0x0101,
        (
            '#0010150702V#002F约修亚，刚才那只小猫……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020150707V#010F好像是刚才说的那只小猫。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150704V#002F绝对错不了啦，\n',
            '快追上它！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x0002, 48800, 0, 62200, 0)
    ChrSetPos(0x0003, 48800, 0, 61200, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004A, 2, 0x252)),
            (Expr.TestScenaFlags, ScenaFlag(0x004A, 3, 0x253)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4078',
    )

    CreateThread(0x010F, 0x00, 0x01, 0x0011)
    CreateThread(0x0110, 0x00, 0x01, 0x0012)
    SetScenaFlags(ScenaFlag(0x0002, 7, 0x17))
    SetScenaFlags(ScenaFlag(0x0002, 6, 0x16))
    OP_92(0x0001, 0x0000, 0, 3000, 0x00)
    OP_A5(0x0016)
    OP_A5(0x0017)

    Jump('loc_40AB')

    def _loc_4078(): pass

    label('loc_4078')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004A, 2, 0x252)),
            Expr.Return,
        ),
        'loc_409D',
    )

    CreateThread(0x010F, 0x00, 0x01, 0x0011)
    SetScenaFlags(ScenaFlag(0x0002, 6, 0x16))
    OP_92(0x0001, 0x0000, 0, 3000, 0x00)
    OP_A5(0x0016)

    Jump('loc_40AB')

    def _loc_409D(): pass

    label('loc_409D')

    OP_92(0x0001, 0x0000, 0, 3000, 0x00)

    def _loc_40AB(): pass

    label('loc_40AB')

    OP_30(0x00)
    Sleep(50)

    EventEnd(0x04)
    MapSetFlags(0x00000001)

    Jump('loc_40BC')

    def _loc_40BC(): pass

    label('loc_40BC')

    Return()

# id: 0x000C offset: 0x40BD
@scena.Code('func_0C_40BD')
def func_0C_40BD():
    CameraMove(49100, 0, 76400, 3000)
    Sleep(500)

    CameraMove(49100, 0, 70400, 2500)

    Return()

# id: 0x000D offset: 0x40E5
@scena.Code('func_0D_40E5')
def func_0D_40E5():
    OP_6C(0, 3000)

    Return()

# id: 0x000E offset: 0x40EF
@scena.Code('func_0E_40EF')
def func_0E_40EF():
    ChrSetFlags(0x0016, 0x0040)
    OP_A6(0x0015)
    ChrWalkTo(0x0016, 58400, 0, 70000, 7000, 0x00)
    ChrSetFlags(0x0016, 0x0080)
    ClearScenaFlags(ScenaFlag(0x0002, 5, 0x15))

    Return()

# id: 0x000F offset: 0x4114
@scena.Code('func_0F_4114')
def func_0F_4114():
    OP_A6(0x0013)
    ChrSetFlags(0x0101, 0x0040)
    ChrWalkTo(0x0101, 49300, 0, 65800, 7000, 0x00)
    ChrSetDirection(0x0101, 45, 0)
    ChrClearFlags(0x0101, 0x0040)
    ClearScenaFlags(ScenaFlag(0x0002, 3, 0x13))

    Return()

# id: 0x0010 offset: 0x4140
@scena.Code('func_10_4140')
def func_10_4140():
    OP_A6(0x0014)
    ChrSetFlags(0x0102, 0x0040)
    ChrWalkTo(0x0102, 48100, 0, 65099, 3000, 0x00)
    ChrSetDirection(0x0102, 45, 0)
    ChrClearFlags(0x0102, 0x0040)
    ClearScenaFlags(ScenaFlag(0x0002, 4, 0x14))

    Return()

# id: 0x0011 offset: 0x416C
@scena.Code('func_11_416C')
def func_11_416C():
    ChrSetFlags(0x010F, 0x0040)
    OP_92(0x010F, 0x0000, 0, 3000, 0x00)
    ChrClearFlags(0x010F, 0x0040)
    ClearScenaFlags(ScenaFlag(0x0002, 6, 0x16))

    Return()

# id: 0x0012 offset: 0x4188
@scena.Code('func_12_4188')
def func_12_4188():
    ChrSetFlags(0x0110, 0x0040)
    OP_92(0x0110, 0x0000, 0, 3000, 0x00)
    ChrClearFlags(0x0110, 0x0040)
    ClearScenaFlags(ScenaFlag(0x0002, 7, 0x17))

    Return()

# id: 0x0013 offset: 0x41A4
@scena.Code('func_13_41A4')
def func_13_41A4():
    If(
        (
            (Expr.Eval, "OP_29(0x0009, 0x00, 0x40)"),
            Expr.Return,
        ),
        'loc_41B1',
    )

    Jump('loc_43FD')

    def _loc_41B1(): pass

    label('loc_41B1')

    If(
        (
            (Expr.Eval, "OP_29(0x0009, 0x01, 0x0004)"),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x0009, 0x01, 0x0002)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_43FD',
    )

    OP_28(0x0009, 0x01, 0x0004)
    EventBegin(0x00)
    MapClearFlags(0x00000001)
    ChrSetPos(0x0016, 60700, 0, 14400, 270)
    ChrClearFlags(0x0016, 0x0080)
    ChrClearFlags(0x0016, 0x0008)
    ChrSetFlags(0x0016, 0x0040)
    Fade(1000)
    CreateThread(0x0016, 0x00, 0x01, 0x0014)
    CreateThread(0x0016, 0x01, 0x01, 0x0015)

    If(
        (
            (Expr.Eval, "OP_42(0x000F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4238',
    )

    ChrSetPos(0x0002, 47400, 0, 50200, 0)
    ChrSetPos(0x0003, 46400, 0, 50200, 0)

    Jump('loc_4257')

    def _loc_4238(): pass

    label('loc_4238')

    If(
        (
            (Expr.Eval, "OP_42(0x000E)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4257',
    )

    ChrSetPos(0x0002, 47400, 0, 50200, 0)

    def _loc_4257(): pass

    label('loc_4257')

    ChrWalkTo(0x0016, 50600, 0, 14400, 3000, 0x00)
    ChrWalkTo(0x0016, 48600, 0, 15800, 3000, 0x00)
    ChrSetPos(0x0000, 48800, 0, 29600, 0)
    ChrSetPos(0x0001, 48800, 0, 29600, 0)

    ChrTalk(
        0x0101,
        (
            '#0010150709V#004F呀！是那只小猫！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0016, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrWalkTo(0x0016, 48600, 0, 16000, 3000, 0x00)
    Sleep(500)

    OP_63(0x0016)
    OP_62(0x0016, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(600)

    ChrTalk(
        0x0101,
        (
            '#0010150710V#005F你给我站住～～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0101, 0x00, 0x01, 0x0017)
    CreateThread(0x0102, 0x00, 0x01, 0x0018)
    CreateThread(0x0016, 0x00, 0x01, 0x0016)
    SetScenaFlags(ScenaFlag(0x0002, 5, 0x15))
    SetScenaFlags(ScenaFlag(0x0002, 3, 0x13))
    SetScenaFlags(ScenaFlag(0x0002, 4, 0x14))
    OP_A5(0x0015)
    OP_A5(0x0013)
    OP_A5(0x0014)
    ChrSetPos(0x0016, 5488, 0, 16806, 0)
    ChrSetFlags(0x0016, 0x0080)
    ChrSetFlags(0x0016, 0x0008)

    ChrTalk(
        0x0102,
        (
            '#0020150711V#017F呼～\n',
            '怎么感觉和帕赛尔农场的情形差不多……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020150712V#017F为什么最近总是在追过来赶过去的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(50)

    EventEnd(0x04)
    MapSetFlags(0x00000001)

    Jump('loc_43FD')

    def _loc_43FD(): pass

    label('loc_43FD')

    Return()

# id: 0x0014 offset: 0x43FE
@scena.Code('func_14_43FE')
def func_14_43FE():
    CameraMove(48800, 0, 16800, 3000)

    Return()

# id: 0x0015 offset: 0x4410
@scena.Code('func_15_4410')
def func_15_4410():
    If(
        (
            (Expr.PushValueByIndex, 0x64),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            (Expr.PushValueByIndex, 0x64),
            (Expr.PushLong, 0x5A),
            Expr.Lss,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4431',
    )

    OP_6C(0, 3000)

    Jump('loc_445B')

    def _loc_4431(): pass

    label('loc_4431')

    If(
        (
            (Expr.PushValueByIndex, 0x64),
            (Expr.PushLong, 0x10E),
            Expr.Gtr,
            (Expr.PushValueByIndex, 0x64),
            (Expr.PushLong, 0x168),
            Expr.Leq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4452',
    )

    OP_6C(0, 3000)

    Jump('loc_445B')

    def _loc_4452(): pass

    label('loc_4452')

    OP_6C(180000, 3000)

    def _loc_445B(): pass

    label('loc_445B')

    Return()

# id: 0x0016 offset: 0x445C
@scena.Code('func_16_445C')
def func_16_445C():
    ChrSetFlags(0x0016, 0x0040)
    OP_A6(0x0015)
    ChrWalkTo(0x0016, 55700, 0, 14400, 7000, 0x00)
    ChrSetFlags(0x0016, 0x0080)
    ClearScenaFlags(ScenaFlag(0x0002, 5, 0x15))

    Return()

# id: 0x0017 offset: 0x4481
@scena.Code('func_17_4481')
def func_17_4481():
    OP_A6(0x0013)
    ChrSetFlags(0x0101, 0x0040)
    ChrWalkTo(0x0101, 48200, 0, 20100, 7000, 0x00)
    ChrSetDirection(0x0101, 135, 0)
    ChrClearFlags(0x0101, 0x0040)
    ClearScenaFlags(ScenaFlag(0x0002, 3, 0x13))

    Return()

# id: 0x0018 offset: 0x44AD
@scena.Code('func_18_44AD')
def func_18_44AD():
    OP_A6(0x0014)
    ChrSetFlags(0x0102, 0x0040)
    ChrWalkTo(0x0102, 49400, 0, 21900, 3000, 0x00)
    ChrSetDirection(0x0102, 135, 0)
    ChrClearFlags(0x0102, 0x0040)
    ClearScenaFlags(ScenaFlag(0x0002, 4, 0x14))

    Return()

# id: 0x0019 offset: 0x44D9
@scena.Code('func_19_44D9')
def func_19_44D9():
    If(
        (
            (Expr.Eval, "OP_29(0x0009, 0x00, 0x40)"),
            Expr.Return,
        ),
        'loc_44E6',
    )

    Jump('loc_474B')

    def _loc_44E6(): pass

    label('loc_44E6')

    If(
        (
            (Expr.Eval, "OP_29(0x0009, 0x01, 0x0008)"),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x0009, 0x01, 0x0004)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_474B',
    )

    OP_28(0x0009, 0x01, 0x0008)
    EventBegin(0x00)
    MapClearFlags(0x00000001)
    Fade(1000)
    OP_6C(180000, 0)
    CameraMove(64629, 0, 38310, 0)
    ChrSetPos(0x0016, 75500, 0, 40200, 270)
    ChrSetFlags(0x0101, 0x0040)
    ChrSetFlags(0x0102, 0x0040)
    ChrClearFlags(0x0016, 0x0080)
    ChrClearFlags(0x0016, 0x0008)
    ChrSetFlags(0x0016, 0x0040)
    OP_0D()
    OP_62(0x0016, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)
    ChrWalkTo(0x0016, 64900, 0, 40400, 3000, 0x00)
    ChrTurnDirection(0x0101, 0x0016, 0)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010150713V#004F啊，在那里！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0101, 64500, 0, 35800, 6000, 0x00)
    ChrTurnDirection(0x0101, 0x0016, 0)
    ChrTurnDirection(0x0016, 0x0101, 0)

    @scena.Lambda('lambda_45E5')
    def lambda_45E5():
        OP_92(0x0102, 0x0101, 1500, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_45E5)

    OP_62(0x0016, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrJumpToRelative(0x0016, 0, 0, 0, 800, 12000)
    Sleep(500)

    WaitForThreadExit(0x0102, 0x0001)
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020150714V#014F等一下，艾丝蒂尔，听我说。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020150715V#014F那只小猫……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150716V#004F啊，它要跑了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveToRelative(0x0101, 0, 0, 1000, 7000, 0x00)
    CreateThread(0x0101, 0x00, 0x01, 0x001D)
    CreateThread(0x0016, 0x00, 0x01, 0x001C)
    SetScenaFlags(ScenaFlag(0x0002, 5, 0x15))
    SetScenaFlags(ScenaFlag(0x0002, 3, 0x13))
    OP_A5(0x0015)
    OP_A5(0x0013)

    ChrTalk(
        0x0101,
        (
            '#0010150717V#005F它朝教会那里跑去了，\n',
            '这回可一定要把它给捉住！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020150718V#017F唉……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x0101, 0x0040)
    ChrClearFlags(0x0102, 0x0040)
    Sleep(50)

    EventEnd(0x04)

    Jump('loc_474B')

    def _loc_474B(): pass

    label('loc_474B')

    Return()

# id: 0x001A offset: 0x474C
@scena.Code('func_1A_474C')
def func_1A_474C():
    CameraMove(64300, 0, 38200, 3000)

    Return()

# id: 0x001B offset: 0x475E
@scena.Code('func_1B_475E')
def func_1B_475E():
    If(
        (
            (Expr.PushValueByIndex, 0x64),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            (Expr.PushValueByIndex, 0x64),
            (Expr.PushLong, 0x5A),
            Expr.Lss,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_477F',
    )

    OP_6C(0, 3000)

    Jump('loc_47A9')

    def _loc_477F(): pass

    label('loc_477F')

    If(
        (
            (Expr.PushValueByIndex, 0x64),
            (Expr.PushLong, 0x10E),
            Expr.Gtr,
            (Expr.PushValueByIndex, 0x64),
            (Expr.PushLong, 0x168),
            Expr.Leq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_47A0',
    )

    OP_6C(0, 3000)

    Jump('loc_47A9')

    def _loc_47A0(): pass

    label('loc_47A0')

    OP_6C(180000, 3000)

    def _loc_47A9(): pass

    label('loc_47A9')

    Return()

# id: 0x001C offset: 0x47AA
@scena.Code('func_1C_47AA')
def func_1C_47AA():
    ChrSetFlags(0x0016, 0x0040)
    OP_A6(0x0015)
    OP_62(0x0016, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)
    ChrWalkTo(0x0016, 72700, 500, 34800, 7000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)
    ClearScenaFlags(ScenaFlag(0x0002, 5, 0x15))

    Return()

# id: 0x001D offset: 0x47E1
@scena.Code('func_1D_47E1')
def func_1D_47E1():
    OP_A6(0x0013)
    def _loc_47E4(): pass

    label('loc_47E4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 5, 0x15)),
            Expr.Return,
        ),
        'loc_47F6',
    )

    ChrTurnDirection(0x0101, 0x0016, 0)
    Yield()

    Jump('loc_47E4')

    def _loc_47F6(): pass

    label('loc_47F6')

    ClearScenaFlags(ScenaFlag(0x0002, 3, 0x13))

    Return()

# id: 0x001E offset: 0x47FA
@scena.Code('func_1E_47FA')
def func_1E_47FA():
    OP_92(0x0102, 0x0101, 1500, 3000, 0x00)

    Return()

# id: 0x001F offset: 0x4809
@scena.Code('func_1F_4809')
def func_1F_4809():
    If(
        (
            (Expr.Eval, "OP_29(0x0009, 0x00, 0x40)"),
            Expr.Return,
        ),
        'loc_4816',
    )

    Jump('loc_4AB2')

    def _loc_4816(): pass

    label('loc_4816')

    If(
        (
            (Expr.Eval, "OP_29(0x0009, 0x01, 0x0008)"),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x0009, 0x01, 0x0004)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4AB2',
    )

    OP_28(0x0009, 0x01, 0x0008)
    EventBegin(0x00)
    MapClearFlags(0x00000001)
    Fade(1000)
    OP_6C(90000, 0)
    CameraMove(64500, 0, 40400, 0)
    ChrSetPos(0x0016, 75500, 0, 40200, 270)
    ChrSetFlags(0x0101, 0x0040)
    ChrSetFlags(0x0102, 0x0040)
    ChrClearFlags(0x0016, 0x0080)
    ChrClearFlags(0x0016, 0x0008)
    ChrSetFlags(0x0016, 0x0040)
    ChrSetPos(0x0101, 61000, 0, 40300, 90)
    ChrSetPos(0x0102, 60000, 0, 42300, 90)

    If(
        (
            (Expr.Eval, "OP_42(0x000F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_48D5',
    )

    ChrSetPos(0x0002, 59000, 0, 41300, 90)
    ChrSetPos(0x0003, 59000, 0, 42800, 90)

    Jump('loc_48F4')

    def _loc_48D5(): pass

    label('loc_48D5')

    If(
        (
            (Expr.Eval, "OP_42(0x000E)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_48F4',
    )

    ChrSetPos(0x0002, 59000, 0, 41300, 90)

    def _loc_48F4(): pass

    label('loc_48F4')

    OP_0D()
    OP_62(0x0016, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)
    ChrWalkTo(0x0016, 65900, 0, 40400, 3000, 0x00)
    ChrTurnDirection(0x0101, 0x0016, 0)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010150719V#004F啊，在那里！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0016, 0)
    ChrTurnDirection(0x0016, 0x0101, 0)
    OP_62(0x0016, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrJumpToRelative(0x0016, 0, 0, 0, 800, 12000)
    Sleep(500)

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020150714V#014F等一下，艾丝蒂尔，听我说。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020150715V#014F那只小猫……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150722V#004F啊，它要跑了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0101, 0x00, 0x01, 0x0022)
    CreateThread(0x0016, 0x00, 0x01, 0x001C)
    SetScenaFlags(ScenaFlag(0x0002, 5, 0x15))
    SetScenaFlags(ScenaFlag(0x0002, 3, 0x13))
    OP_A5(0x0015)
    OP_A5(0x0013)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010150717V#005F它朝教会那里跑去了，\n',
            '这回可一定要把它给捉住！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020150718V#017F唉……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x0101, 0x0040)
    ChrClearFlags(0x0102, 0x0040)
    Sleep(50)

    EventEnd(0x04)

    Jump('loc_4AB2')

    def _loc_4AB2(): pass

    label('loc_4AB2')

    Return()

# id: 0x0020 offset: 0x4AB3
@scena.Code('func_20_4AB3')
def func_20_4AB3():
    CameraMove(64300, 0, 40200, 3000)

    Return()

# id: 0x0021 offset: 0x4AC5
@scena.Code('func_21_4AC5')
def func_21_4AC5():
    If(
        (
            (Expr.PushValueByIndex, 0x64),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            (Expr.PushValueByIndex, 0x64),
            (Expr.PushLong, 0xB4),
            Expr.Leq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4AE6',
    )

    OP_6C(90000, 3000)

    Jump('loc_4AEF')

    def _loc_4AE6(): pass

    label('loc_4AE6')

    OP_6C(270000, 3000)

    def _loc_4AEF(): pass

    label('loc_4AEF')

    Return()

# id: 0x0022 offset: 0x4AF0
@scena.Code('func_22_4AF0')
def func_22_4AF0():
    OP_A6(0x0013)
    ChrMoveToRelative(0x0101, 3000, 0, 0, 7000, 0x00)
    ChrSetDirection(0x0101, 135, 400)
    ClearScenaFlags(ScenaFlag(0x0002, 3, 0x13))

    Return()

# id: 0x0023 offset: 0x4B12
@scena.Code('func_23_4B12')
def func_23_4B12():
    EventBegin(0x00)
    FadeIn(1000, 0)
    OP_6C(45000, 0)
    CameraMove(36470, 0, 58400, 0)
    OP_67(0, 11530, -10000, 0)
    CameraSetDistance(2150, 0)
    ChrSetPos(0x0101, 38560, 0, 57230, 270)
    ChrSetPos(0x0102, 37800, 0, 58080, 225)
    ChrTurnDirection(0x0014, 0x0101, 0)

    If(
        (
            (Expr.Eval, "OP_42(0x000F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4BAD',
    )

    ChrSetPos(0x0002, 39290, 0, 58080, 211)
    ChrSetPos(0x0003, 40280, 0, 58050, 212)

    Jump('loc_4BCC')

    def _loc_4BAD(): pass

    label('loc_4BAD')

    If(
        (
            (Expr.Eval, "OP_42(0x000E)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4BCC',
    )

    ChrSetPos(0x0002, 39290, 0, 58080, 211)

    def _loc_4BCC(): pass

    label('loc_4BCC')

    ChrSetPos(0x0015, 36010, 0, 56150, 36)
    ChrClearFlags(0x0015, 0x0080)
    ChrClearFlags(0x0015, 0x0008)
    ChrClearFlags(0x0015, 0x0040)
    ChrTurnDirection(0x0014, 0x0102, 0)

    @scena.Lambda('lambda_4BF9')
    def lambda_4BF9():
        OP_6C(0, 4000)

        ExitThread()

    DispatchAsync(0x0015, 0x0001, lambda_4BF9)

    OP_0D()
    Sleep(3000)

    ChrTalk(
        0x0102,
        (
            '#0020150745V#010F……事情的经过就是这样的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(1000)

    ChrTalk(
        0x0102,
        (
            '#0020150746V#010F我想刚才安莉尔\n',
            '可能正要回阿姨您这里来的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020150747V#010F它每次都是朝着茶座这边跑来的。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010150748V#004F啊……\n',
            '确实，经你这么一说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020150749V#013F或许是我们把它吓跑到其他地方去了……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0014, 0x0102, 400)

    ChrTalk(
        0x0014,
        (
            '#1090150750V没有～\n',
            '没关系的啦～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0014, 0)

    ChrTalk(
        0x0014,
        (
            '#1090150751V能够平安无事把它送回我这里来～\n',
            '我已经很感激了啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#1090150752V特别是这位帅气的尤基士君，\n',
            '阿姨感动得都要哭了啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(402, 0x00, 0x64)

    ChrTalk(
        0x0015,
        (
            '#1100150742V喵喵～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020150754V#018F您、您实在太客气了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 0)

    ChrTalk(
        0x0101,
        (
            '#0010150755V#507F（嘿嘿，他害羞啦、他害羞啦。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#1090150756V呜呜～\n',
            '阿姨是认真的啊～～㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020150757V#511F对、对不起，\n',
            '我们必须要回协会报告情况了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020150758V告、告辞了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0014, 0)

    ChrTalk(
        0x0101,
        (
            '#0010150759V#508F阿姨再见～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#1090150760V哦呵呵～㈱\n',
            '再见了～～～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_4F6A')
    def lambda_4F6A():
        ChrTurnDirection(0x0000, 0x0014, 0)
        Yield()

        Jump('lambda_4F6A')

    DispatchAsync2(0x0000, 0x0001, lambda_4F6A)

    @scena.Lambda('lambda_4F7B')
    def lambda_4F7B():
        ChrTurnDirection(0x0001, 0x0014, 0)
        Yield()

        Jump('lambda_4F7B')

    DispatchAsync2(0x0001, 0x0001, lambda_4F7B)

    If(
        (
            (Expr.Eval, "OP_42(0x000F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4FB9',
    )

    @scena.Lambda('lambda_4F9A')
    def lambda_4F9A():
        ChrTurnDirection(0x0002, 0x0014, 0)
        Yield()

        Jump('lambda_4F9A')

    DispatchAsync2(0x0002, 0x0001, lambda_4F9A)

    @scena.Lambda('lambda_4FAB')
    def lambda_4FAB():
        ChrTurnDirection(0x0003, 0x0014, 0)
        Yield()

        Jump('lambda_4FAB')

    DispatchAsync2(0x0003, 0x0001, lambda_4FAB)

    Jump('loc_4FD8')

    def _loc_4FB9(): pass

    label('loc_4FB9')

    If(
        (
            (Expr.Eval, "OP_42(0x000E)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4FD8',
    )

    @scena.Lambda('lambda_4FCD')
    def lambda_4FCD():
        ChrTurnDirection(0x0002, 0x0014, 0)
        Yield()

        Jump('lambda_4FCD')

    DispatchAsync2(0x0002, 0x0001, lambda_4FCD)

    def _loc_4FD8(): pass

    label('loc_4FD8')

    ChrSetFlags(0x0015, 0x0040)
    ChrSetFlags(0x0014, 0x0040)

    @scena.Lambda('lambda_4FE8')
    def lambda_4FE8():
        ChrWalkTo(0x0015, 35510, 0, 51180, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0015, 0x0001, lambda_4FE8)

    @scena.Lambda('lambda_5003')
    def lambda_5003():
        ChrWalkTo(0x0014, 35530, 0, 51480, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_5003)

    Sleep(400)

    WaitForThreadExit(0x0014, 0x0001)
    WaitForThreadExit(0x0015, 0x0001)
    TerminateThread(0x0000, 0x01)
    TerminateThread(0x0001, 0x01)

    If(
        (
            (Expr.Eval, "OP_42(0x000F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5048',
    )

    TerminateThread(0x0002, 0x01)
    TerminateThread(0x0003, 0x01)

    Jump('loc_505A')

    def _loc_5048(): pass

    label('loc_5048')

    If(
        (
            (Expr.Eval, "OP_42(0x000E)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_505A',
    )

    TerminateThread(0x0002, 0x01)

    def _loc_505A(): pass

    label('loc_505A')

    ChrClearFlags(0x0015, 0x0040)
    ChrClearFlags(0x0014, 0x0040)
    ChrSetPos(0x0014, 39420, 250, 51560, 315)
    ChrSetPos(0x0015, 38700, 0, 50720, 315)
    ChrSetChipByIndex(0x0014, 20)
    PlaySE(23, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【寻找小猫】',
            (TxtCtl.SetColor, 0x0),
            '完成！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    Sleep(1000)

    MapClearFlags(0x00400000)
    EventEnd(0x00)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
