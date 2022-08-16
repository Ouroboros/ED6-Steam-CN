import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T2130_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2130_1 ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T2130.x'
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
    If(
        (
            (Expr.Eval, "OP_29(0x001E, 0x01, 0x0010)"),
            (Expr.Eval, "OP_40(0x0335)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_7B',
    )

    Call(1, 0x0001)

    Jump('loc_246C')

    def _loc_7B(): pass

    label('loc_7B')

    If(
        (
            (Expr.Eval, "OP_29(0x001E, 0x00, 0x04)"),
            Expr.Return,
        ),
        'loc_200',
    )

    TalkBegin(0x0011)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_109',
    )

    ChrTalk(
        0x00FE,
        (
            '#1770160904V如果有什么发现，\n',
            '一定要马上回来告诉我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1770160903V拜托了！\n',
            '如果找到了财宝，我会分给你们的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0011)

    Jump('loc_1FD')

    def _loc_109(): pass

    label('loc_109')

    ChrTalk(
        0x00FE,
        (
            '#1770160906V哦～你们回来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1770160907V那么，找到财宝了没有？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160908V#505F抱歉，还没有找到。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '#1770160904V如果有什么发现，\n',
            '一定要马上回来告诉我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1770160903V拜托了！\n',
            '如果找到了财宝，我会分给你们的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0011)

    def _loc_1FD(): pass

    label('loc_1FD')

    Jump('loc_246C')

    def _loc_200(): pass

    label('loc_200')

    EventBegin(0x00)
    MapClearFlags(0x00000001)
    ChrSetFlags(0x0011, 0x0010)
    Fade(1000)
    ChrSetPos(0x0101, 54200, 0, 49000, 270)
    ChrSetPos(0x0102, 54200, 0, 47500, 270)
    ChrSetPos(0x0105, 56000, 0, 48500, 270)
    TalkBegin(0x0011)

    ExecExpressionWithValue(
        0x0012,
        0x01,
        (
            (Expr.GetChrWork, 0x11, 0x1),
            (Expr.GetChrWork, 0x105, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0012,
        0x02,
        (
            (Expr.GetChrWork, 0x11, 0x2),
            (Expr.GetChrWork, 0x105, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0012,
        0x03,
        (
            (Expr.GetChrWork, 0x11, 0x3),
            (Expr.GetChrWork, 0x105, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_69(0x0012, 1000)
    ChrClearFlags(0x0011, 0x0010)

    If(
        (
            (Expr.Eval, "OP_29(0x001E, 0x01, 0x8000)"),
            Expr.Return,
        ),
        'loc_417',
    )

    OP_2B(0x001E, 0x0002)
    OP_2C(0x001E, 0x03E8)
    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '#1770160769V………咦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1770160770V你们不是前些日子的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020160771V#010F很久不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160772V#508F啊，我说呢，\n',
            '你不就是我们在沙滩遇到的那个人吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#1770160773V请叫我吉米。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1770160774V幸亏你们那时救了我啊。\n',
            '再次向你们表示感谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1770160775V嗯………………\n',
            '这次你们是\n',
            '看了公告板而来的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_49C')

    def _loc_417(): pass

    label('loc_417')

    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '#1770160776V………………咦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1770160777V喂，\n',
            '你们是游击士吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1770160778V对了，\n',
            '一定是看了公告板才来的对吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_49C(): pass

    label('loc_49C')

    If(
        (
            (Expr.Eval, "OP_29(0x001E, 0x00, 0x02)"),
            Expr.Return,
        ),
        'loc_673',
    )

    OP_28(0x001E, 0x04, 0x04)
    OP_28(0x001E, 0x04, 0x08)
    OP_28(0x001E, 0x01, 0x0001)
    OP_28(0x001E, 0x01, 0x0002)
    OP_28(0x001E, 0x01, 0x0004)
    OP_28(0x001E, 0x01, 0x0008)
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0101,
        (
            '#0010160525V#000F嗯，正是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160780V为什么你会选在\n',
            '这种地方等我们来啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1770160781V因为这里很好找啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1770160782V不过我要是一直在这里，\n',
            '就不能去赚钱了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1770160783V单是委托游击士办事，\n',
            '就要花掉不少的费用啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160784V#006F那你就快点告诉我们委托的内容吧。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160785V不管怎么说，\n',
            '公告板上写的那些东西\n',
            '让人有些好奇呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1770160786V嘿嘿嘿，我说了之后，\n',
            '你们可不要太过期待哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_849')

    def _loc_673(): pass

    label('loc_673')

    OP_28(0x001E, 0x04, 0x08)
    OP_28(0x001E, 0x04, 0x04)
    OP_28(0x001E, 0x04, 0x02)
    OP_28(0x001E, 0x01, 0x0001)
    OP_28(0x001E, 0x01, 0x0002)
    OP_28(0x001E, 0x01, 0x0004)
    OP_28(0x001E, 0x01, 0x0008)
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0101,
        (
            '#0010160787V#004F哎？\n',
            '委托的事情是什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1770160788V什么，你们没看见吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1770160789V我还以为你们\n',
            '仔细看过委托内容之后\n',
            '才来见面地点的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x00FE, 400)

    ChrTalk(
        0x0102,
        (
            '#0020160790V#014F见面地点……\n',
            '就是这个教堂吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '#1770160781V因为这里很好找啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1770160782V不过我要是一直在这里，\n',
            '就不能去赚钱了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1770160783V单是委托游击士办事，\n',
            '就要花掉不少的费用啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x00FE, 400)

    ChrTalk(
        0x0101,
        (
            '#0010160794V#006F那么，到底是什么委托呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_849(): pass

    label('loc_849')

    ChrSetDirection(0x00FE, 90, 0)

    ChrTalk(
        0x00FE,
        (
            '#1770160795V事实上我最近得到了\n',
            '一幅出乎意料的古地图。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1770160796V没想到那幅地图竟然是…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160797V#002F那幅地图是……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '#1770160798V竟然是大海盗希鲁玛\n',
            '留下来的藏宝图啊！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010160799V#004F哎呀啊！？真的吗！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160800V#000F……的确是大发现呢！\n',
            '但那个海盗又是什么人呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '#1770160801V连、连希鲁玛是谁\n',
            '你都不知道！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1770160802V难以置信啊，\n',
            '你还算是卢安的市民吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160803V#509F……不要主观臆断地\n',
            '把所有人都当成卢安的市民好不好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060160804V#040F希鲁玛这个人好像是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0AA4')
    def lambda_0AA4():
        ChrTurnDirection(0x0101, 0x0105, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0AA4)

    @scena.Lambda('lambda_0AB2')
    def lambda_0AB2():
        ChrTurnDirection(0x0102, 0x0105, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0AB2)

    @scena.Lambda('lambda_0AC0')
    def lambda_0AC0():
        ChrTurnDirection(0x00FE, 0x0105, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_0AC0)

    ChrTalk(
        0x0105,
        (
            '#0060160805V#040F一百年以前在卢安周围\n',
            '盘踞的一个海盗……吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1770160806V对呀！你真棒！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1770160807V王立学院就是不一样！\n',
            '不只是校服可爱而已哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160808V#004F啊～\n',
            '科洛丝，好厉害。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060160809V#045F哎呀，艾丝蒂尔……\n',
            '别这么夸我了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060160810V我只是因为听到你们讨论，\n',
            '才偶然想起来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1770160811V其实我就是想委托你们\n',
            '帮我去找希鲁玛的财宝。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0C45')
    def lambda_0C45():
        ChrTurnDirection(0x0101, 0x0011, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0C45)

    @scena.Lambda('lambda_0C53')
    def lambda_0C53():
        ChrTurnDirection(0x0102, 0x0011, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0C53)

    ChrTalk(
        0x00FE,
        (
            '#1770160812V首先从地图上\n',
            '标有记号的地方开始……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x001E, 0x01, 0x8000)"),
            Expr.Return,
        ),
        'loc_E8B',
    )

    ChrTalk(
        0x00FE,
        (
            '#1770160814V还记得我上次\n',
            '遇到你们的地方吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1770160815V看，\n',
            '沙滩中有一个看似洼地的地形。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020160816V#010F在梅威海道的中部\n',
            '稍微靠边一点的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '#1770160817V没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1770160818V藏宝图上也把那个洼地\n',
            '作为标志画了出来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160819V#000F也就是说那个地方有什么东西吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#1770160820V对，就是这样的。\n',
            '我本想去现场调查的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1770160821V好不容易找到了洼地，\n',
            '但是接下来\n',
            '就遇上了魔兽……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1770160822V所以啦，\n',
            '这次就只能拜托你们这些职业人士了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F76')

    def _loc_E8B(): pass

    label('loc_E8B')

    ChrTalk(
        0x00FE,
        (
            '#1770160813V梅威海道沿岸的沙滩上\n',
            '有一处被山崖\n',
            '围起来的洼地。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1770160823V藏宝图上也把那个洼地\n',
            '作为标志画了出来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1770160824V但我去那里调查的时候\n',
            '被魔兽袭击了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1770160825V所以这次我只能\n',
            '拜托你们这些职业人士了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F76(): pass

    label('loc_F76')

    ChrTalk(
        0x0101,
        (
            '#0010160826V#000F那找到洼地之后呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#1770160827V嗯，\n',
            '在地图上洼地的东南方向\n',
            '有一个标记了×的地方……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1770160828V不管怎么想，\n',
            '那里都应该是埋藏了财宝的场所。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160829V#002F嗯，\n',
            '的确是有这种可能。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160830V#004F…………哎呀，对了，\n',
            '应该把这些记录下来才是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 0, 400)
    OP_62(0x0101, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)

    ChrTalk(
        0x0102,
        (
            '#0020160831V#010F那么就先好好地整理一下思路吧……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020160832V到达洼地后往其东南方向……\n',
            '也就是卢安所在方向的沙滩，\n',
            '对那里进行调查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    If(
        (
            (Expr.Eval, "OP_29(0x001E, 0x01, 0x4000)"),
            (Expr.Eval, "OP_40(0x0335)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_206B',
    )

    OP_28(0x001E, 0x01, 0x0020)
    OP_63(0x0101)
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010160833V#505F往卢安方向的沙滩啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160834V#004F啊，对了，在这之前\n',
            '我们曾在沙滩边上发现过有趣的东西啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '#1770160835V什、什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1770160836V发、发、\n',
            '发现了什么东西？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020160837V#010F我想起来了，\n',
            '是那个飘到岸上的木桶……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020160838V而且还找到了短剑和一幅航海图。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160839V#000F说起那张航海图，\n',
            '都已经烂得差不多了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)
    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrJumpToRelative(0x00FE, 0, 0, 0, 800, 12000)
    Sleep(400)

    OP_63(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#1770160840V航、航海图！\n',
            '哇哦～～这可是大发现！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_94(0x01, 0x00FE, 0x0000, 0x000002BC, 0x00000BB8, 0x00)
    ChrTurnDirection(0x0101, 0x00FE, 400)
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_94(0x01, 0x00FE, 0x0000, 0x000000C8, 0x00001B58, 0x00)
    OP_94(0x01, 0x0101, 0x00B4, 0x000000C8, 0x00001B58, 0x00)
    OP_94(0x01, 0x00FE, 0x00B4, 0x000000C8, 0x00001B58, 0x00)
    OP_94(0x01, 0x0101, 0x0000, 0x000000C8, 0x00001B58, 0x00)
    OP_94(0x01, 0x00FE, 0x0000, 0x000000C8, 0x00001B58, 0x00)
    OP_94(0x01, 0x0101, 0x00B4, 0x000000C8, 0x00001B58, 0x00)
    OP_94(0x01, 0x00FE, 0x00B4, 0x000000C8, 0x00001B58, 0x00)
    OP_94(0x01, 0x0101, 0x0000, 0x000000C8, 0x00001B58, 0x00)
    OP_94(0x01, 0x00FE, 0x0000, 0x000000C8, 0x00001B58, 0x00)
    OP_94(0x01, 0x0101, 0x00B4, 0x000000C8, 0x00001B58, 0x00)
    OP_94(0x01, 0x00FE, 0x00B4, 0x000000C8, 0x00001B58, 0x00)
    OP_94(0x01, 0x0101, 0x0000, 0x000000C8, 0x00001B58, 0x00)
    OP_94(0x01, 0x00FE, 0x0000, 0x000000C8, 0x00001B58, 0x00)
    OP_94(0x01, 0x0101, 0x00B4, 0x000000C8, 0x00001B58, 0x00)

    ChrTalk(
        0x00FE,
        (
            '#1770160841V快、快点给我看看～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160842V#008F不、不要那么激动嘛。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '交出了',
            (TxtCtl.SetColor, 0x2),
            '古海图的残片',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    RemoveItem(0x0335, 1)
    OP_28(0x001E, 0x01, 0x0040)
    OP_28(0x001E, 0x04, 0x10)
    ChrWalkTo(0x00FE, 53000, 0, 48100, 2000, 0x00)
    ChrSetDirection(0x00FE, 270, 400)
    OP_62(0x00FE, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(800)

    OP_63(0x00FE)
    Sleep(400)

    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '#1770160843V哇啊～～\n',
            '这、这个是～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1770160844V太、太好了！\n',
            '这玩意儿，简直绝了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0105, 400)

    ChrTalk(
        0x00FE,
        (
            '#1770160845V这个肯定就是\n',
            '海盗希鲁玛的藏宝图！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0105, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#044F#4P#1K…………咦？',
            TxtCtl.Enter,
        ),
    )

    ChrTalk(
        0x0105,
        (
            '#0060160847V#004F#2P#1K啊？',
            TxtCtl.Enter,
        ),
    )

    Sleep(500)

    OP_56(0x01)
    OP_59()

    ChrTalk(
        0x0101,
        (
            '#0010160848V#509F我说大哥。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160849V你从刚才开始不是一直都说\n',
            '自己手上拿的就是藏宝图吗。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x00FE, 90, 400)

    ChrTalk(
        0x00FE,
        (
            '#1770160850V不不，我那个肯定就是\n',
            '『藏宝图的藏宝图』了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1770160851V是用来标示财宝的隐藏地点的\n',
            '地图所在的隐藏地点的地图啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0105, 0x00000000, 2000, 0x0E, 0x0F, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0101, 0x00000000, 2000, 0x0E, 0x0F, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x0E, 0x0F, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(800)

    ChrTalk(
        0x0105,
        (
            '#0060160852V#045F哎呀，好像有点复杂啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160853V#007F…………可是，\n',
            '那个航海图是从木桶里面找到的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020160854V#010F算了，就这样吧。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020160855V虽然怎么想都觉得\n',
            '里面会有那幅航海图是一种偶然……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020160856V不过那个位置的确是\n',
            '地图上标记了×的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0102, 400)

    ChrTalk(
        0x0105,
        (
            '#0060160857V#040F嗯，是呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010160858V#505F至少他本人是非常高兴的，\n',
            '这不就已经足够了吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160859V#004F……哦，对了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x00FE, 400)

    @scena.Lambda('lambda_197D')
    def lambda_197D():
        ChrTurnDirection(0x0102, 0x0011, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_197D)

    @scena.Lambda('lambda_198B')
    def lambda_198B():
        ChrTurnDirection(0x0105, 0x0011, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_198B)

    ChrTalk(
        0x0101,
        (
            '#0010160860V#000F请问，吉米先生。\n',
            '和图一起找到的短剑怎么处理呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#1770160861V哦，\n',
            '那个就送给你们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1770160862V作为谢礼可能有些寒酸，\n',
            '就算是我的一点点心意吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1770160863V你们就收下，\n',
            '想怎么用就怎么用吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160864V#000F嗯，谢谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '#1770160865V哎呀，真是太好了。\n',
            '终于找到了这幅航海图。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1770160866V嘿嘿嘿， \n',
            '现在开始可有的忙了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1770160867V好～的，\n',
            '快点解读它，\n',
            '让欧尼尔爷爷大吃一惊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060160868V#044F……欧尼尔爷爷？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1770160869V再见啦！\n',
            '谢谢你们的帮助！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1BA8')
    def lambda_1BA8():
        ChrTurnDirection(0x0101, 0x0011, 0)
        Yield()

        Jump('lambda_1BA8')

    DispatchAsync2(0x0101, 0x0001, lambda_1BA8)

    @scena.Lambda('lambda_1BB9')
    def lambda_1BB9():
        ChrTurnDirection(0x0102, 0x0011, 0)
        Yield()

        Jump('lambda_1BB9')

    DispatchAsync2(0x0102, 0x0001, lambda_1BB9)

    @scena.Lambda('lambda_1BCA')
    def lambda_1BCA():
        ChrTurnDirection(0x0105, 0x0011, 0)
        Yield()

        Jump('lambda_1BCA')

    DispatchAsync2(0x0105, 0x0001, lambda_1BCA)

    ChrSetFlags(0x00FE, 0x0040)
    ChrWalkTo(0x00FE, 53600, 0, 46500, 6000, 0x00)
    ChrSetDirection(0x00FE, 135, 0)
    ChrJumpTo(0x00FE, 55000, 0, 45000, 1500, 7000)
    ChrWalkTo(0x00FE, 57760, 0, 45050, 5000, 0x00)
    ChrWalkTo(0x00FE, 59000, 0, 37300, 6000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0102, 0x01)
    TerminateThread(0x0105, 0x01)

    ExecExpressionWithValue(
        0x0012,
        0x01,
        (
            (Expr.GetChrWork, 0x101, 0x1),
            (Expr.GetChrWork, 0x102, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0012,
        0x02,
        (
            (Expr.GetChrWork, 0x101, 0x2),
            (Expr.GetChrWork, 0x102, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0012,
        0x03,
        (
            (Expr.GetChrWork, 0x101, 0x3),
            (Expr.GetChrWork, 0x102, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_69(0x0012, 800)

    ChrTalk(
        0x0105,
        (
            '#0060160870V#043F是欧尼尔爷爷……吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060160871V原来如此……\n',
            '是这么一回事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1CE7')
    def lambda_1CE7():
        ChrTurnDirection(0x0101, 0x0105, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1CE7)

    @scena.Lambda('lambda_1CF5')
    def lambda_1CF5():
        ChrTurnDirection(0x0102, 0x0105, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1CF5)

    ChrTalk(
        0x0101,
        (
            '#0010160872V#501F嗯？\n',
            '欧尼尔爷爷怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0101, 400)

    ChrTalk(
        0x0105,
        (
            '#0060160873V#040F他是经营杂货店的那个老爷爷……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060160874V要说他有什么缺点的话，\n',
            '就是谈到无论什么事\n',
            '他都要夸大其词吹嘘一番。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160875V#506F哎呀，还有这样的人啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160876V这么说吉米先生就是\n',
            '把那个爷爷的夸夸其谈\n',
            '当作真的去对待了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060160877V#045F对啊，\n',
            '看起来好像就是这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160878V#007F唉，\n',
            '思想太过单纯也很麻烦啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160879V#000F啊，不过……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160880V虽说这样，\n',
            '但他还是通过那个爷爷说的话\n',
            '才找到了那张航海图。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020160881V#010F嗯，的确是这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060160882V#040F呵呵，\n',
            '真是让人觉得不可思议啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010160883V#505F只要去相信，就会有回报呢。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160884V……说实话，\n',
            '我觉得吉米先生也有点信过头了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020160885V#010F用尽全力追寻自己的梦想，\n',
            '又何尝不是一种人生呢。',
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
            '任务【调查古地图】',
            (TxtCtl.SetColor, 0x0),
            '完成！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    Jump('loc_2460')

    def _loc_206B(): pass

    label('loc_206B')

    ChrTurnDirection(0x00FE, 0x0102, 0)

    ChrTalk(
        0x00FE,
        (
            '#1770160886V就是这样吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1770160887V嗯，相当不错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020160888V#015F……过奖了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_63(0x0101)
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010160889V#505F唔～不过不太好找啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160890V照刚才所说的线索，\n',
            '从洼地向东南方向找就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0101, 0)

    ChrTalk(
        0x0105,
        (
            '#0060160891V#043F嗯，可是海滩范围相当大……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 0)

    ChrTalk(
        0x0102,
        (
            '#0020160892V#013F的确…………\n',
            '线索还不太够呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '#1770160893V哦～\n',
            '各位不用有什么顾虑。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x00FE, 0)
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#1770160894V沿着梅威海道的边上\n',
            '走遍每个角落的话，\n',
            '我想就一定可以找到的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x00FE, 0)

    ChrTalk(
        0x0101,
        (
            '#0010160895V#007F可关键是……\n',
            '要仔细找一遍，\n',
            '不知道有没有那么多体力呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020160896V#010F你肯定没问题的，艾丝蒂尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010160897V#505F算了，虽然不是非常困难的事情……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160898V但做起来也并不是很轻松…… ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020160899V#010F这样效率虽然很低，\n',
            '但是也仅有这个办法了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020160900V只有沿着海道边彻底走一遍了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160901V#007F呼，没办法了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_23C8')
    def lambda_23C8():
        ChrTurnDirection(0x0101, 0x0011, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_23C8)

    @scena.Lambda('lambda_23D6')
    def lambda_23D6():
        ChrTurnDirection(0x0102, 0x0011, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_23D6)

    ChrTalk(
        0x0102,
        (
            '#0020160902V#010F那么，要是发现了什么，\n',
            '我们会再来汇报的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '#1770160903V拜托了！\n',
            '如果找到了财宝，我会分给你们的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2460(): pass

    label('loc_2460')

    EventEnd(0x00)
    TalkEnd(0x0011)
    ChrSetDirection(0x0011, 90, 0)

    def _loc_246C(): pass

    label('loc_246C')

    Return()

# id: 0x0001 offset: 0x246D
@scena.Code('func_01_246D')
def func_01_246D():
    EventBegin(0x00)
    MapClearFlags(0x00000001)
    ChrSetFlags(0x0011, 0x0010)
    Fade(1000)
    ChrSetPos(0x0101, 54200, 0, 49000, 270)
    ChrSetPos(0x0102, 54200, 0, 47500, 270)
    ChrSetPos(0x0105, 56000, 0, 48500, 270)
    TalkBegin(0x0011)

    ExecExpressionWithValue(
        0x0012,
        0x01,
        (
            (Expr.GetChrWork, 0x11, 0x1),
            (Expr.GetChrWork, 0x105, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0012,
        0x02,
        (
            (Expr.GetChrWork, 0x11, 0x2),
            (Expr.GetChrWork, 0x105, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0012,
        0x03,
        (
            (Expr.GetChrWork, 0x11, 0x3),
            (Expr.GetChrWork, 0x105, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_69(0x0012, 1000)
    ChrClearFlags(0x0011, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 5, 0x435)),
            Expr.Return,
        ),
        'loc_259A',
    )

    ChrTalk(
        0x0101,
        (
            '#0010160927V#501F啊，吉米先生。\n',
            '我们回来晚了，真抱歉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#1770160928V哦哦，终于回来了吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1770160907V那么，找到财宝了没有？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2612')

    def _loc_259A(): pass

    label('loc_259A')

    ChrTalk(
        0x0101,
        (
            '#0010160930V#001F呀嗬～吉米先生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#1770160906V哦～你们回来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1770160907V那么，找到财宝了没有？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2612(): pass

    label('loc_2612')

    ChrTalk(
        0x0101,
        (
            '#0010160933V#505F嗯～财宝倒是没有找到……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160934V#508F不过，\n',
            '却发现了一把古代的短剑和一张航海图。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrJumpToRelative(0x00FE, 0, 0, 0, 800, 12000)
    Sleep(400)

    OP_63(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#1770160840V航、航海图！\n',
            '哇哦～～这可是大发现！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_94(0x01, 0x00FE, 0x0000, 0x000002BC, 0x00000BB8, 0x00)
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_94(0x01, 0x00FE, 0x0000, 0x000000C8, 0x00001B58, 0x00)
    OP_94(0x01, 0x0101, 0x00B4, 0x000000C8, 0x00001B58, 0x00)
    OP_94(0x01, 0x00FE, 0x00B4, 0x000000C8, 0x00001B58, 0x00)
    OP_94(0x01, 0x0101, 0x0000, 0x000000C8, 0x00001B58, 0x00)
    OP_94(0x01, 0x00FE, 0x0000, 0x000000C8, 0x00001B58, 0x00)
    OP_94(0x01, 0x0101, 0x00B4, 0x000000C8, 0x00001B58, 0x00)
    OP_94(0x01, 0x00FE, 0x00B4, 0x000000C8, 0x00001B58, 0x00)
    OP_94(0x01, 0x0101, 0x0000, 0x000000C8, 0x00001B58, 0x00)
    OP_94(0x01, 0x00FE, 0x0000, 0x000000C8, 0x00001B58, 0x00)
    OP_94(0x01, 0x0101, 0x00B4, 0x000000C8, 0x00001B58, 0x00)
    OP_94(0x01, 0x00FE, 0x00B4, 0x000000C8, 0x00001B58, 0x00)
    OP_94(0x01, 0x0101, 0x0000, 0x000000C8, 0x00001B58, 0x00)
    OP_94(0x01, 0x00FE, 0x0000, 0x000000C8, 0x00001B58, 0x00)
    OP_94(0x01, 0x0101, 0x00B4, 0x000000C8, 0x00001B58, 0x00)

    ChrTalk(
        0x00FE,
        (
            '#1770160841V快、快点给我看看～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160937V#008F不、不要那么激动嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '交出了',
            (TxtCtl.SetColor, 0x2),
            '古海图的残片',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    RemoveItem(0x0335, 1)
    OP_28(0x001E, 0x01, 0x0040)
    OP_28(0x001E, 0x04, 0x10)
    ChrWalkTo(0x00FE, 53000, 0, 48100, 2000, 0x00)
    ChrSetDirection(0x00FE, 270, 400)
    OP_62(0x00FE, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1000)

    OP_63(0x00FE)
    Sleep(400)

    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '#1770160843V哇啊～～\n',
            '这、这个是～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1770160844V太、太好了！\n',
            '这玩意儿，简直绝了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0105, 400)

    ChrTalk(
        0x00FE,
        (
            '#1770160845V这个肯定就是\n',
            '海盗希鲁玛的藏宝图！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0105, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010160941V#044F#4P#1K…………咦？',
            TxtCtl.Enter,
        ),
    )

    ChrTalk(
        0x0105,
        (
            '#0060160847V#004F#2P#1K啊？',
            TxtCtl.Enter,
        ),
    )

    Sleep(500)

    OP_56(0x01)
    OP_59()

    ChrTalk(
        0x0101,
        (
            '#0010160848V#509F我说大哥。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160944V你从刚才开始不是一直都说\n',
            '自己手上拿的就是藏宝图吗。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x00FE, 90, 400)

    ChrTalk(
        0x00FE,
        (
            '#1770160945V不不，我那个肯定就是\n',
            '『藏宝图的藏宝图』了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1770160946V是用来标示财宝的隐藏地点的\n',
            '地图所在的隐藏地点的地图啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0105, 0x00000000, 2000, 0x0E, 0x0F, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0101, 0x00000000, 2000, 0x0E, 0x0F, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x0E, 0x0F, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(800)

    ChrTalk(
        0x0105,
        (
            '#0060160852V#045F哎呀，好像有点复杂啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160948V#007F…………可是，\n',
            '那个航海图是从木桶里面找到的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 5, 0x435)),
            (Expr.TestScenaFlags, ScenaFlag(0x0088, 2, 0x442)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2F16',
    )

    ChrTalk(
        0x0102,
        (
            '#0020160854V#010F算了，就这样吧。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020160950V现在可不是拘泥于\n',
            '这种小事的时候。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160951V#004F哦，对了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160952V#002F对不起，吉米先生。\n',
            '我们有很急的事要办，\n',
            '不得不走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#1770160953V啊啊，没关系。\n',
            '总之今天要谢谢你们啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x00FE, 400)

    ChrTalk(
        0x00FE,
        (
            '#1770160954V哦，\n',
            '我也不能再在这里磨蹭了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1770160955V要尽早解读它，\n',
            '然后让欧尼尔爷爷\n',
            '大吃一惊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1770160956V再见啦！谢谢你们的帮助！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2D76')
    def lambda_2D76():
        ChrTurnDirection(0x0101, 0x0011, 0)
        Yield()

        Jump('lambda_2D76')

    DispatchAsync2(0x0101, 0x0001, lambda_2D76)

    @scena.Lambda('lambda_2D87')
    def lambda_2D87():
        ChrTurnDirection(0x0102, 0x0011, 0)
        Yield()

        Jump('lambda_2D87')

    DispatchAsync2(0x0102, 0x0001, lambda_2D87)

    @scena.Lambda('lambda_2D98')
    def lambda_2D98():
        ChrTurnDirection(0x0105, 0x0011, 0)
        Yield()

        Jump('lambda_2D98')

    DispatchAsync2(0x0105, 0x0001, lambda_2D98)

    ChrSetFlags(0x00FE, 0x0040)
    ChrWalkTo(0x00FE, 53600, 0, 46500, 6000, 0x00)
    ChrSetDirection(0x00FE, 135, 0)
    ChrJumpTo(0x00FE, 55000, 0, 45000, 1500, 7000)
    ChrWalkTo(0x00FE, 57760, 0, 45050, 5000, 0x00)
    ChrWalkTo(0x00FE, 59000, 0, 37300, 6000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0102, 0x01)
    TerminateThread(0x0105, 0x01)

    ExecExpressionWithValue(
        0x0012,
        0x01,
        (
            (Expr.GetChrWork, 0x101, 0x1),
            (Expr.GetChrWork, 0x102, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0012,
        0x02,
        (
            (Expr.GetChrWork, 0x101, 0x2),
            (Expr.GetChrWork, 0x102, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0012,
        0x03,
        (
            (Expr.GetChrWork, 0x101, 0x3),
            (Expr.GetChrWork, 0x102, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_69(0x0012, 800)
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020160957V#012F好，\n',
            '那我们也赶快走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2E94')
    def lambda_2E94():
        ChrTurnDirection(0x0101, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2E94)

    @scena.Lambda('lambda_2EA2')
    def lambda_2EA2():
        ChrTurnDirection(0x0105, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_2EA2)

    ChrTalk(
        0x0101,
        (
            '#0010151213V#002F嗯！',
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
            '任务【调查古地图】',
            (TxtCtl.SetColor, 0x0),
            '完成！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    Jump('loc_37FA')

    def _loc_2F16(): pass

    label('loc_2F16')

    ChrTalk(
        0x0102,
        (
            '#0020160854V#010F算了，就这样吧。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020160960V#010F虽然怎么想都觉得\n',
            '里面会有那幅航海图是一种偶然……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020160961V不过正因为吉米先生\n',
            '相信有那张古地图的存在，\n',
            '所以才有这样的发现吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0102, 400)

    ChrTalk(
        0x0105,
        (
            '#0060160962V#040F呵呵，的确是这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010160963V#505F唔～仔细想想看。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160964V至少他本人是非常高兴的，\n',
            '这不就已经足够了吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160859V#004F……哦，对了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x00FE, 400)

    @scena.Lambda('lambda_309B')
    def lambda_309B():
        ChrTurnDirection(0x0102, 0x0011, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_309B)

    @scena.Lambda('lambda_30A9')
    def lambda_30A9():
        ChrTurnDirection(0x0105, 0x0011, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_30A9)

    ChrTalk(
        0x0101,
        (
            '#0010160860V#000F请问，吉米先生。\n',
            '和图一起找到的短剑怎么处理呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_63(0x00FE)
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#1770160967V…………嗯？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1770160861V哦，\n',
            '那个就送给你们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1770160862V作为谢礼可能有些寒酸，\n',
            '就算是我的一点点心意吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1770160863V你们就收下，\n',
            '想怎么用就怎么用吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160864V#000F嗯，谢谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '#1770160972V这次你们完成了一件\n',
            '了不起的工作呢。\n',
            '这幅航海图肯定是个大发现。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1770160866V嘿嘿嘿， \n',
            '现在开始可有的忙了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1770160954V哦，\n',
            '我也不能再在这里磨蹭了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1770160955V要尽早解读它，\n',
            '然后让欧尼尔爷爷\n',
            '大吃一惊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060160868V#044F……欧尼尔爷爷？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1770160956V再见啦！谢谢你们的帮助！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3328')
    def lambda_3328():
        ChrTurnDirection(0x0101, 0x0011, 0)
        Yield()

        Jump('lambda_3328')

    DispatchAsync2(0x0101, 0x0001, lambda_3328)

    @scena.Lambda('lambda_3339')
    def lambda_3339():
        ChrTurnDirection(0x0102, 0x0011, 0)
        Yield()

        Jump('lambda_3339')

    DispatchAsync2(0x0102, 0x0001, lambda_3339)

    @scena.Lambda('lambda_334A')
    def lambda_334A():
        ChrTurnDirection(0x0105, 0x0011, 0)
        Yield()

        Jump('lambda_334A')

    DispatchAsync2(0x0105, 0x0001, lambda_334A)

    ChrSetFlags(0x00FE, 0x0040)
    ChrWalkTo(0x00FE, 53600, 0, 46500, 6000, 0x00)
    ChrSetDirection(0x00FE, 135, 0)
    ChrClearFlags(0x00FE, 0x0001)
    ChrJumpTo(0x00FE, 55000, 0, 45000, 1500, 7000)
    ChrWalkTo(0x00FE, 57760, 0, 45050, 5000, 0x00)
    ChrSetFlags(0x00FE, 0x0001)
    ChrWalkTo(0x00FE, 59000, 0, 37300, 6000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0102, 0x01)
    TerminateThread(0x0105, 0x01)

    ExecExpressionWithValue(
        0x0012,
        0x01,
        (
            (Expr.GetChrWork, 0x101, 0x1),
            (Expr.GetChrWork, 0x102, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0012,
        0x02,
        (
            (Expr.GetChrWork, 0x101, 0x2),
            (Expr.GetChrWork, 0x102, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0012,
        0x03,
        (
            (Expr.GetChrWork, 0x101, 0x3),
            (Expr.GetChrWork, 0x102, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_69(0x0012, 800)

    ChrTalk(
        0x0105,
        (
            '#0060160870V#043F是欧尼尔爷爷……吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060160871V原来如此……\n',
            '是这么一回事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3471')
    def lambda_3471():
        ChrTurnDirection(0x0101, 0x0105, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3471)

    @scena.Lambda('lambda_347F')
    def lambda_347F():
        ChrTurnDirection(0x0102, 0x0105, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_347F)

    ChrTalk(
        0x0101,
        (
            '#0010160980V#501F嗯…………？\n',
            '欧尼尔爷爷怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0101, 400)

    ChrTalk(
        0x0105,
        (
            '#0060160873V#040F他是经营杂货店的那个老爷爷……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060160874V要说他有什么缺点的话，\n',
            '就是谈到无论什么事\n',
            '他都要夸大其词吹嘘一番。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160875V#506F哎呀，还有这样的人啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160876V这么说吉米先生就是\n',
            '把那个爷爷的夸夸其谈\n',
            '当作真的去对待了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060160877V#045F对啊，\n',
            '看起来好像就是这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160878V#007F唉，\n',
            '思想太过单纯也很麻烦啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160879V#000F啊，不过……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160880V虽说这样，\n',
            '但他还是通过那个爷爷说的话\n',
            '才找到了那张航海图。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020160881V#010F嗯，的确是这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060160882V#040F呵呵，\n',
            '真是让人觉得不可思议啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010160883V#505F只要去相信，就会有回报呢。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160992V……说实话，\n',
            '我觉得吉米先生也有点信过头了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020160885V#010F用尽全力追寻自己的梦想，\n',
            '又何尝不是一种人生呢。',
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
            '任务【调查古地图】',
            (TxtCtl.SetColor, 0x0),
            '完成！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    def _loc_37FA(): pass

    label('loc_37FA')

    EventEnd(0x00)
    TalkEnd(0x0011)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
