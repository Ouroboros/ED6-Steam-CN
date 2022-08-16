import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T3300_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3300_1 ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'T3300.x'
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
    Return()

# id: 0x0001 offset: 0xA9
@scena.Code('func_01_A9')
def func_01_A9():
    Return()

# id: 0x0002 offset: 0xAA
@scena.Code('func_02_AA')
def func_02_AA():
    EventBegin(0x00)
    Fade(1000)
    CameraMove(1160, 0, 48100, 0)
    CameraSetDistance(2600, 0)
    ChrSetPos(0x0101, 1200, 0, 47440, 0)
    ChrSetPos(0x0102, -10, 0, 47200, 45)

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_10C',
    )

    ChrSetPos(0x0107, 2240, 0, 46790, 0)

    def _loc_10C(): pass

    label('loc_10C')

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_12B',
    )

    ChrSetPos(0x0106, 940, 0, 45200, 0)

    def _loc_12B(): pass

    label('loc_12B')

    OP_0D()
    OP_4A(0x00FE, 255)

    If(
        (
            (Expr.Eval, "OP_29(0x0031, 0x01, 0x8000)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_900',
    )

    OP_62(0x00FE, 0x00000000, 2000, 0x1C, 0x21, 0x000000FA, 0x00)
    Sleep(1500)

    ChrTalk(
        0x00FE,
        (
            '#2050180265V……………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    OP_94(0x01, 0x00FE, 0x005A, 0x00000064, 0x00000BB8, 0x00)
    OP_94(0x01, 0x00FE, 0x010E, 0x00000064, 0x00000BB8, 0x00)

    ChrTalk(
        0x00FE,
        (
            '#2050180266V……唔、唔～嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    OP_94(0x01, 0x00FE, 0x005A, 0x00000064, 0x00000BB8, 0x00)
    OP_94(0x01, 0x00FE, 0x010E, 0x00000064, 0x00000BB8, 0x00)
    OP_94(0x01, 0x00FE, 0x005A, 0x00000064, 0x00000BB8, 0x00)
    OP_94(0x01, 0x00FE, 0x010E, 0x00000064, 0x00000BB8, 0x00)

    ChrTalk(
        0x00FE,
        (
            '#2050180267V唔、唔唔、唔唔唔～嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_94(0x01, 0x00FE, 0x005A, 0x00000064, 0x00000BB8, 0x00)
    OP_94(0x01, 0x00FE, 0x010E, 0x00000064, 0x00000BB8, 0x00)
    OP_94(0x01, 0x00FE, 0x005A, 0x00000064, 0x00000BB8, 0x00)
    OP_94(0x01, 0x00FE, 0x010E, 0x00000064, 0x00000BB8, 0x00)
    OP_94(0x01, 0x00FE, 0x005A, 0x00000064, 0x00000BB8, 0x00)
    OP_94(0x01, 0x00FE, 0x010E, 0x00000064, 0x00000BB8, 0x00)
    OP_94(0x01, 0x00FE, 0x005A, 0x00000064, 0x00000BB8, 0x00)
    OP_94(0x01, 0x00FE, 0x010E, 0x00000064, 0x00000BB8, 0x00)
    OP_63(0x00FE)
    ChrJumpToRelative(0x00FE, 0, 0, 0, 800, 12000)

    ChrTalk(
        0x00FE,
        (
            '#2050180268V#5S菲、菲！\n',
            '原谅我吧！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    Sleep(400)

    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(800)

    ChrTalk(
        0x00FE,
        (
            '#2050180269V啊…………！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrSetDirection(0x00FE, 270, 800)
    Sleep(200)

    ChrSetDirection(0x00FE, 91, 800)
    Sleep(400)

    ChrTurnDirection(0x00FE, 0x0101, 400)
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '#2050180270V刚、刚才\n',
            '我说了什么吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(800)

    ChrTalk(
        0x0101,
        (
            '#0010180271V#509F#2P嗯、嗯，\n',
            '突然地放声大叫。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180272V说什么『菲！原谅我吧！』。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrJumpToRelative(0x00FE, 0, 0, 0, 800, 12000)
    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(800)

    OP_62(0x00FE, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x00FE,
        (
            '#2050180273V唔……哇，连名字都！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180274V#505F#2P嗯？菲……？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180275V好像在哪里听过这个名字……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0107, 0x0101, 400)

    ChrTalk(
        0x0107,
        (
            '#0070180276V#064F菲小姐……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070180277V是地下工场那个菲小姐吗～？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020180278V#010F是为我们准备好\n',
            '汽油罐的那位工作人员吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010180279V#000F#2P啊，对啊。\n',
            '是那位女工作员。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '#2050180280V咦？\n',
            '你们认识菲吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x00FE, 400)
    ChrSetDirection(0x0107, 0, 400)

    ChrTalk(
        0x0101,
        (
            '#0010180281V#000F#2P嗯，不久前，\n',
            '我们在工作上受到了她的帮助。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x00FE, 400)

    ChrTalk(
        0x0102,
        (
            '#0020180282V#010F因为我们是游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x00FE, 225, 400)

    ChrTalk(
        0x00FE,
        (
            '#2050180283V游击士……吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2050180284V这、这可真是太好了，\n',
            '太谢谢你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180285V#501F#2P咦……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020180286V#014F有什么委托吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#2050180287V唔～\n',
            '虽然是私人问题……\n',
            '但还是想委托你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2050180288V现在可以吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180289V#505F#2P嗯～\n',
            '能帮上忙的话我们当然乐意协助……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180290V#000F#2P……是什么样的委托呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2050180291V唔、唔唔……\n',
            '我想请你们帮我带一封信给菲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2050180292V事实上，\n',
            '我之前一直在和菲交往……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2050180293V可是我对这方面并不在行，\n',
            '所以她最后还是提出和我分手了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2050180294V可、可是，我想和她重归于好。\n',
            '所以就先给她写了一封信。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2050180295V你们如果去蔡斯的话，\n',
            '能不能帮我送一下这封信呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_956')

    def _loc_900(): pass

    label('loc_900')

    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#2050180347V啊，是你们…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2050180348V怎么样？\n',
            '能帮我送信了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_956(): pass

    label('loc_956')

    FadeOut(300, 0, 70)

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
            TXT(0x00, '【接受】\n'),
            TXT(0x01, '【拒绝】\n'),
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
        'loc_1303',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0031, 0x01, 0x8000)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A50',
    )

    ChrTalk(
        0x0101,
        (
            '#0010180296V#006F#2P嗯，没问题。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180297V…………约修亚，怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020180298V#010F是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020180299V如果不急的话\n',
            '我们接受下来也无妨。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A76')

    def _loc_A50(): pass

    label('loc_A50')

    ChrTalk(
        0x0101,
        (
            '#0010180300V#006F#2P嗯，没问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A76(): pass

    label('loc_A76')

    ChrTalk(
        0x00FE,
        (
            '#2050180301V太好了！\n',
            '呀～谢谢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2050180302V那么，\n',
            '我就把这个非常重要的东西交给你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '给菲的情书',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    ChrTalk(
        0x0101,
        (
            '#0010180303V#006F#2P嗯，这封信就交给我们吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180304V#505F#2P可是……好像有些困难啊，\n',
            '只靠写信能让她回心转意吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0107, 0x0101, 400)

    ChrTalk(
        0x0107,
        (
            '#0070180305V#064F咦？是～吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x14, 0x17, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '#2050180306V果、果真如此吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020180307V#017F艾丝蒂尔，\n',
            '你认为我们介入\n',
            '别人的事情是礼貌的举止吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x00FE, 225, 400)

    ChrTalk(
        0x00FE,
        (
            '#2050180308V没、没关系，不用介意，\n',
            '女性的意见是非常宝贵的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#2050180309V…………那，怎么办？\n',
            '只有一封信果然还是不够吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180310V#505F#2P是啊…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x22, 0x24, 0x000000FA, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(800)

    ChrTalk(
        0x0101,
        (
            '#0010180311V#508F#2P啊，对了，\n',
            '再赠送点礼物如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '#2050180312V啊～礼物对吗，\n',
            '糟了，我没有准备啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2050180313V这可就麻烦了，\n',
            '堡垒这里什么都买不到……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180314V#003F#2P的确是呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2050180315V唔～对不起……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2050180316V如果可以的话，\n',
            '拜托你们帮我准备可以吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180317V#004F#2P咦…………？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180318V让我们来准备礼物吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2050180319V嗯，\n',
            '在蔡斯买东西就很方便了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2050180320V准备好了之后，\n',
            '再和这封信一起交给她吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010180321V#506F#2P好、好吧，\n',
            '我倒是没什么关系……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180322V#505F不过这么一来，\n',
            '感觉责任重大呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020180323V#018F……艾丝蒂尔，靠你了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2050180324V虽说菲她一般都是\n',
            '穿着工作服积极地工作着……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2050180325V但她的性格和一般的女孩子差不多，\n',
            '非常喜欢可爱的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070180326V#064F可爱的东西吗……？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070180327V布娃娃……怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x00FE, 135, 400)

    ChrTalk(
        0x00FE,
        (
            '#2050180328V那、那个有点\n',
            '太孩子气了吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180329V#007F#2P好吧，\n',
            '总之就是可爱的东西……对吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#2050180330V那么，\n',
            '我先把这些米拉作为预付款给你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2050180331V也许不太够，\n',
            '但礼物的事就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '拿到了',
            (TxtCtl.SetColor, 0x4),
            '１０００',
            (TxtCtl.SetColor, 0x0),
            '米拉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    AddMira(1000)

    ChrTalk(
        0x0101,
        (
            '#0010180332V#006F嗯，我知道了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180333V那按照规矩，\n',
            '确认委托的内容……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180334V在蔡斯城里买一样礼物……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180335V把它和信一起交给菲小姐，\n',
            '对吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2050180336V啊，就是这样的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2050180337V那么，\n',
            '就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    AddItem(0x035E, 1)
    OP_28(0x0031, 0x04, 0x02)
    OP_28(0x0031, 0x04, 0x04)
    OP_28(0x0031, 0x04, 0x08)
    OP_28(0x0031, 0x01, 0x0001)
    OP_28(0x0031, 0x01, 0x0002)
    OP_28(0x0031, 0x01, 0x0004)
    OP_28(0x0031, 0x01, 0x0008)
    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))
    ChrClearFlags(0x00FE, 0x0010)

    Jump('loc_15F0')

    def _loc_1303(): pass

    label('loc_1303')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_15F0',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0031, 0x01, 0x8000)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1516',
    )

    ChrTalk(
        0x0101,
        (
            '#0010180338V#007F#2P对、对不起，\n',
            '现在没有空……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020180339V#010F非常抱歉，\n',
            '让您过于期待了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020180340V我们现在正有其他的任务，\n',
            '要前往亚尔摩那边。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '#2050180341V啊，好、好吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2050180342V请不用介意，\n',
            '只是一点小事而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#2050180343V实在是对不起，\n',
            '占用了你们的时间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180344V#003F#2P不不，我们才应该说对不起，\n',
            '没能帮上你的忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020180345V#010F那么我们就告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(800)

    OP_63(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#2050180346V…………我说的梦话，\n',
            '你们大家一定要保密哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15EA')

    def _loc_1516(): pass

    label('loc_1516')

    ChrTalk(
        0x0101,
        (
            '#0010180349V#003F#2P对不起，\n',
            '现在我们还有点事要做。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2050180350V请不用介意，\n',
            '只是一点小事而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2050180343V实在是对不起，\n',
            '占用了你们的时间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180352V#007F#2P拒绝了好几次，\n',
            '真是不好意思。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_15EA(): pass

    label('loc_15EA')

    OP_28(0x0031, 0x01, 0x8000)

    def _loc_15F0(): pass

    label('loc_15F0')

    OP_4B(0x00FE, 255)
    CreateThread(0x000B, 0x00, 0x00, 0x0002)
    EventEnd(0x00)

    Return()

# id: 0x0003 offset: 0x15FE
@scena.Code('func_03_15FE')
def func_03_15FE():
    EventBegin(0x00)
    EventEnd(0x00)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
