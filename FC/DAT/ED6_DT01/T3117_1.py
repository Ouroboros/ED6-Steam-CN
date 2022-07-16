import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T3117_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3117_1 ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'T3117.x'
    header.mapIndex       = 1
    header.bgm            = 10
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x36FD
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
    Return()

# id: 0x0001 offset: 0xA9
@scena.Code('Init')
def Init():
    Return()

# id: 0x0002 offset: 0xAA
@scena.Code('ReInit')
def ReInit():
    EventBegin(0x00)
    Fade(1000)
    CameraMove(-2740, 0, 8680, 0)
    SetChrPos(0x0101, -2790, 0, 7830, 0)
    SetChrPos(0x0102, -1340, 0, 8370, 315)

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_103',
    )

    SetChrPos(0x0107, -2190, 0, 6710, 315)

    def _loc_103(): pass

    label('loc_103')

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_122',
    )

    SetChrPos(0x0106, -1500, 0, 6000, 315)

    def _loc_122(): pass

    label('loc_122')

    If(
        (
            (Expr.Eval, "OP_42(0x000F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_141',
    )

    SetChrPos(0x0110, -2210, 0, 4820, 315)

    def _loc_141(): pass

    label('loc_141')

    If(
        (
            (Expr.Eval, "OP_42(0x003B)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_160',
    )

    SetChrPos(0x013C, -1500, 0, 6000, 315)

    def _loc_160(): pass

    label('loc_160')

    SetChrFlags(0x0009, 0x0010)
    TalkBegin(0x0009)
    OP_0D()

    If(
        (
            (Expr.Eval, "OP_29(0x002A, 0x01, 0x0400)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4C3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_2C8',
    )

    ClearChrFlags(0x0009, 0x0010)
    OP_62(0x0009, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    ChrTurnDirection(0x0009, 0x0101, 400)
    OP_4A(0x0009, 255)

    ChrTalk(
        0x0009,
        (
            '#2040180001V嗯？什么事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180002V是来找雷伊前辈的吗？\n',
            '他出去吃午饭了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180003V#000F唔，不是的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180004V我们是看了公告板而来的。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(800)

    ChrTalk(
        0x0009,
        (
            '#2040180005V啊，原来是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180006V呀～太感谢了，\n',
            '很高兴你们能来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180007V我叫蒂亚利，\n',
            '是中央工房的研究员。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_411')

    def _loc_2C8(): pass

    label('loc_2C8')

    ClearChrFlags(0x0009, 0x0010)

    ChrTalk(
        0x0009,
        (
            '#2040180008V呼～总之试制品已经做好了。\n',
            '之后就是等测试人员过来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180009V在那之前，\n',
            '我还是再调整一下鞋的内垫吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180010V#000F你好～现在有空吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180011V我们是看了公告板而来的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_4A(0x0009, 255)
    Sleep(800)

    ChrTurnDirection(0x0009, 0x0101, 400)

    ChrTalk(
        0x0009,
        (
            '#2040180012V哦，终于来了。\n',
            '哎呀～真是等急我了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180013V我叫蒂亚利，\n',
            '是中央工房的研究员。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_411(): pass

    label('loc_411')

    ChrTalk(
        0x0101,
        (
            '#0010180014V#006F我是准游击士艾丝蒂尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020180015V#010F我是约修亚，\n',
            '请多多关照。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180016V啊，彼此彼此。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180017V那么我这就把\n',
            '任务委托给你们……\n',
            '想问一下你们有空吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_525')

    def _loc_4C3(): pass

    label('loc_4C3')

    ClearChrFlags(0x0009, 0x0010)
    OP_62(0x0009, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    ChrTurnDirection(0x0009, 0x0101, 400)
    OP_4A(0x0009, 255)

    ChrTalk(
        0x0009,
        (
            '#2040180024V哦，是你们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180025V怎么样？\n',
            '有空了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_525(): pass

    label('loc_525')

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
        10,
        0,
        (
            TXT(0x00, '【是】\n'),
            TXT(0x01, '【否】\n'),
        ),
    )

    MenuEnd(0x0002)

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
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_667',
    )

    ChrTalk(
        0x0101,
        (
            '#0010180018V#007F呼～对不起呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180019V现在还不太方便……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180020V唔，\n',
            '游击士真是忙碌啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180021V那等你们\n',
            '有空时再过来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180022V#000F嗯，请稍微等一会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020180023V#010F待会儿请您多多关照。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x002A, 0x01, 0x0400)

    @scena.Lambda('lambda_0653')
    def lambda_0653():
        SetChrDirection(0x0009, 270, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0653)

    OP_4B(0x0009, 255)
    Sleep(50)

    EventEnd(0x04)

    Return()

    def _loc_667(): pass

    label('loc_667')

    ChrTalk(
        0x0101,
        (
            '#0010180026V#000F嗯，没问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020180027V#010F您的委托是测试新型的运动鞋……\n',
            '没错吧。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020180028V如果可以的话，\n',
            '请详细说明一下好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180029V嗯，当然。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0101, 400)

    ChrTalk(
        0x0009,
        (
            '#2040180030V不过，\n',
            '在此之前先把这个交给你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x000B, 400)
    Sleep(300)

    SetChrFlags(0x000B, 0x0080)
    ChrTurnDirection(0x0009, 0x0101, 400)
    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '斯托雷加α',
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
            '#0010180031V#000F这个就是新型的运动鞋吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180032V啊，是我们和斯托雷加社\n',
            '共同研制的新产品……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrName('蒂亚利')

    ChrTalk(
        0x0009,
        (
            '#2040180033V这次的测试内容\n',
            '就是穿着这双鞋\n',
            '在蔡斯的周边地区走一圈。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180034V这次测试完成之后，\n',
            '新型运动鞋就可以投放生产了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180035V#501F呼～原来是这样啊……',
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
            '#0010180036V#004F…………咦！？\n',
            '等、等一下！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180037V这、这运动鞋\n',
            '是斯托雷加社制造的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0009,
        (
            '#2040180038V咦…………？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180039V啊、啊啊，没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180040V#004F啊，\n',
            '难道说这个新型的运动鞋就是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180041V嗯，斯托雷加社的新产品哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180042V这双鞋仅供测试使用，\n',
            '刚才不已经说了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180043V#004F………………啊！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0101, 225, 400)
    OP_62(0x0101, 0x0000012C, 1600, 0x36, 0x39, 0x000000FA, 0x00)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010180044V#001F啊，女神呀……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180045V感谢您能够赐予我\n',
            '如此美妙的任务。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    SetChrDirection(0x0102, 225, 400)
    Sleep(800)

    ChrTurnDirection(0x0009, 0x0102, 400)

    ChrTalk(
        0x0009,
        (
            '#2040180046V喂，我说……\n',
            '她没事吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180047V怎么突然之间\n',
            '就开始祷告起来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0009, 400)

    ChrTalk(
        0x0102,
        (
            '#0020180048V#018F…………让您见笑了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020180049V#017F艾丝蒂尔有收集运动鞋的爱好……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020180050V而且她更是斯托雷加的忠实支持者。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_BDF',
    )

    ChrTalk(
        0x0107,
        (
            '#0070180051V#064F哦……是这样的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BDF(): pass

    label('loc_BDF')

    ChrTurnDirection(0x0009, 0x0101, 400)

    ChrTalk(
        0x0009,
        (
            '#2040180052V哦哦，这就是所谓的\n',
            '运动鞋狂热收藏者啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180053V虽然我是第一次见到，\n',
            '不过这样的反应还真是强烈呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0102, 225, 400)

    ChrTalk(
        0x0102,
        (
            '#0020180054V#018F……艾丝蒂尔，拜托，\n',
            '别在别人面前失礼了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020180055V我知道你很开心，\n',
            '但也要等接受完任务再开心吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_63(0x0101)
    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(800)

    ChrTurnDirection(0x0101, 0x0009, 400)

    ChrTalk(
        0x0101,
        (
            '#0010180056V#008F哦、哦哦…………\n',
            '说得对呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180057V唔，不全神贯注的话，\n',
            '最后很容易徒劳无功的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180058V请把这个测试坚持到底吧。\n',
            '只要保持平常状态就行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180059V#005F哦啊！明白！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0009, 400)

    ChrTalk(
        0x0102,
        (
            '#0020180060V#018F……不至于吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x0E, 0x0F, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0009,
        (
            '#2040180061V好、好的。\n',
            '总之就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020180062V#010F那么，\n',
            '再确认一下任务的内容吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020180063V#010F穿上刚才拿到的那双鞋子\n',
            '到各地走走就行了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0102, 400)

    ChrTalk(
        0x0009,
        (
            '#2040180064V嗯，就是如此。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180065V亚尔摩温泉、沃尔费堡垒，\n',
            '还有圣海姆门……\n',
            '这三个地方都要走一趟才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180066V如果觉得\n',
            '测试已经足够了，\n',
            '你们就回到我这里来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180067V我要把鞋子外到鞋子里……\n',
            '也就是说，\n',
            '把鞋底和鞋内的情况进行检查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180068V#006F那么，满足条件之后，\n',
            '回来报告就行了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0101, 400)

    ChrTalk(
        0x0009,
        (
            '#2040180069V对，不管怎样，\n',
            '这件事就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180070V抱着踏破鞋底的决心\n',
            '去好好测试吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180071V#006F嗯，交给我们吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020180072V#010F那么我们就告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    AddItem(0x011C, 1)
    OP_28(0x002A, 0x04, 0x08)
    OP_28(0x002A, 0x04, 0x04)
    OP_28(0x002A, 0x01, 0x0001)
    OP_28(0x002A, 0x01, 0x0002)
    OP_28(0x002A, 0x01, 0x0004)
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    @scena.Lambda('lambda_1092')
    def lambda_1092():
        SetChrDirection(0x0009, 270, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1092)

    OP_4B(0x0009, 255)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x0003 offset: 0x10A6
@scena.Code('func_03_10A6')
def func_03_10A6():
    EventBegin(0x00)
    Fade(1000)
    CameraMove(-2740, 0, 8680, 0)
    SetChrPos(0x0101, -2790, 0, 7830, 0)
    SetChrPos(0x0102, -1340, 0, 8370, 315)

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_10FF',
    )

    SetChrPos(0x0107, -2190, 0, 6710, 315)

    def _loc_10FF(): pass

    label('loc_10FF')

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_111E',
    )

    SetChrPos(0x0106, -1500, 0, 6000, 315)

    def _loc_111E(): pass

    label('loc_111E')

    If(
        (
            (Expr.Eval, "OP_42(0x000F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_113D',
    )

    SetChrPos(0x0110, -2210, 0, 4820, 315)

    def _loc_113D(): pass

    label('loc_113D')

    If(
        (
            (Expr.Eval, "OP_42(0x003B)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_115C',
    )

    SetChrPos(0x013C, -1500, 0, 6000, 315)

    def _loc_115C(): pass

    label('loc_115C')

    SetChrFlags(0x0009, 0x0010)
    TalkBegin(0x0009)
    ClearChrFlags(0x0009, 0x0010)
    ChrTurnDirection(0x0009, 0x0101, 0)
    OP_4A(0x0009, 255)
    OP_0D()

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.Eval, "OP_29(0x002A, 0x01, 0x0800)"),
            Expr.Return,
        ),
        'loc_1198',
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Add,
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1198(): pass

    label('loc_1198')

    If(
        (
            (Expr.Eval, "OP_29(0x002A, 0x01, 0x1000)"),
            Expr.Return,
        ),
        'loc_11B1',
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Add,
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_11B1(): pass

    label('loc_11B1')

    If(
        (
            (Expr.Eval, "OP_29(0x002A, 0x01, 0x2000)"),
            Expr.Return,
        ),
        'loc_11CA',
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Add,
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_11CA(): pass

    label('loc_11CA')

    If(
        (
            (Expr.Eval, "OP_29(0x002A, 0x01, 0x4000)"),
            Expr.Return,
        ),
        'loc_11E3',
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Add,
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_11E3(): pass

    label('loc_11E3')

    If(
        (
            (Expr.Eval, "OP_29(0x002A, 0x01, 0x8000)"),
            Expr.Return,
        ),
        'loc_11FC',
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Add,
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_11FC(): pass

    label('loc_11FC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_120A',
    )

    Call(1, 0x0004)

    Jump('loc_1221')

    def _loc_120A(): pass

    label('loc_120A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 6, 0x536)),
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_121D',
    )

    Call(1, 0x0005)

    Jump('loc_1221')

    def _loc_121D(): pass

    label('loc_121D')

    Call(1, 0x0006)

    def _loc_1221(): pass

    label('loc_1221')

    @scena.Lambda('lambda_1227')
    def lambda_1227():
        SetChrDirection(0x0009, 270, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1227)

    OP_4B(0x0009, 255)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x0004 offset: 0x123B
@scena.Code('func_04_123B')
def func_04_123B():
    If(
        (
            (Expr.Eval, "OP_40(0x011C)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_13CE',
    )

    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(800)

    ChrTalk(
        0x0009,
        (
            '#2040180137V哎？\n',
            '那双鞋子不见了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180138V呼，\n',
            '这么一来就不能继续测试了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180139V唔～很遗憾，\n',
            '不过确实是失败了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x14, 0x17, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(800)

    ChrTalk(
        0x0101,
        (
            '#0010180133V#007F呜……对不起啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180134V尽管专门来接受了任务，\n',
            '可还是没能帮上一点忙……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180142V没、没关系，\n',
            '最低限度的数据还是有的，\n',
            '你不用担心了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180143V再过不久成品就能上市了，\n',
            '敬请期待哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x002A, 0x04, 0x40)
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    Return()

    def _loc_13CE(): pass

    label('loc_13CE')

    ChrTalk(
        0x0101,
        (
            '#0010180073V#000F你好，蒂亚利研究员。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180074V那几个地方都已经走过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180075V哦，辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180076V好，\n',
            '那就让我检查一下这双鞋吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0009, 270, 400)
    OP_62(0x0009, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)

    ChrTalk(
        0x0009,
        (
            '#2040180077V…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x4),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_1B32',
    )

    OP_2B(0x002A, 0x0002)
    OP_63(0x0009)
    Sleep(400)

    OP_62(0x0009, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(800)

    ChrTalk(
        0x0009,
        (
            '#2040180078V……哦哦，真厉害。\n',
            '鞋底磨损了很多啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180079V从磨损的情况来看，\n',
            '我选择的材料\n',
            '是相当合适的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0101, 400)

    ChrTalk(
        0x0009,
        (
            '#2040180080V嗯，测试非常成功。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180081V#501F呼～太好了～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180082V我刚才还在想，\n',
            '如果您叫我们继续该怎么办。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1608',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_15E4',
    )

    ChrTalk(
        0x0107,
        (
            '#0070180083V#061F呵呵呵，太好了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1608')

    def _loc_15E4(): pass

    label('loc_15E4')

    ChrTalk(
        0x0107,
        (
            '#0070180084V#061F呵呵呵，太好了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1608(): pass

    label('loc_1608')

    ChrTalk(
        0x0009,
        (
            '#2040180085V感觉怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180086V会不会很容易滑倒，\n',
            '或者说有些太硬了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180087V#006F有些吧，不过问题不大。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180088V穿上去很合适，\n',
            '走起来也很舒服。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180089V不愧是斯托雷加啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180090V啊，对了。\n',
            '你是斯托雷加的\n',
            '忠实支持者对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180091V……那么，\n',
            '我就把这个作为礼物送给你吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180092V因为你们做得比我预想的要好得多，\n',
            '就当成是额外奖励吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '斯托雷加β',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(400)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(800)

    ChrTalk(
        0x0101,
        (
            '#0010180093V#004F这、这是……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180094V是厂家专门送过来的，\n',
            '给研究者参考用的新产品哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180095V这可是还没有向外界披露的新型号呢。\n',
            '商店里面自然也还没出售了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020180096V#014F这样好吗？\n',
            '这个东西太贵重了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0102, 400)

    ChrTalk(
        0x0009,
        (
            '#2040180097V唔，反正开发已经告一段落了，\n',
            '我也就不需要了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180098V把这双鞋送给懂得其价值的人，\n',
            '也算是体现出它的价值吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x08, 0x09, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(800)

    ChrTalk(
        0x0101,
        (
            '#0010180099V#001F哇啊，谢谢～！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180100V既可以协助开发，\n',
            '又还可以得到新产品……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180101V真的是～一件美妙的任务啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0101, 400)

    ChrTalk(
        0x0009,
        (
            '#2040180102V哈哈，彼此彼此吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180103V因为你们的努力才使得\n',
            '我的研究成果得到充分的证明呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180104V#006F您也要加油哦，\n',
            '我很期待新产品呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180105V唔，我一定会把你这番话\n',
            '转达给斯托雷加社的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020180106V#010F那么，多谢您的关照。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180107V#001F再见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    AddItem(0x011D, 1)
    PlaySE(23, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【测试新产品】',
            (TxtCtl.SetColor, 0x0),
            '完成！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_28(0x002A, 0x04, 0x10)
    OP_28(0x002A, 0x01, 0x0010)
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Return()

    def _loc_1B32(): pass

    label('loc_1B32')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1ECB',
    )

    OP_63(0x0009)
    Sleep(400)

    OP_62(0x0009, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(800)

    ChrTalk(
        0x0009,
        (
            '#2040180108V…………嗯。\n',
            '鞋底已经磨损得足够了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180079V从磨损的情况来看，\n',
            '我选择的材料\n',
            '是相当合适的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0101, 400)

    ChrTalk(
        0x0009,
        (
            '#2040180110V好，测试成功。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180081V#501F呼～太好了～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180082V我刚才还在想，\n',
            '如果您叫我们继续该怎么办。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1C9B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_1C77',
    )

    ChrTalk(
        0x0107,
        (
            '#0070180083V#061F呵呵呵，太好了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C9B')

    def _loc_1C77(): pass

    label('loc_1C77')

    ChrTalk(
        0x0107,
        (
            '#0070180084V#061F呵呵呵，太好了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C9B(): pass

    label('loc_1C9B')

    ChrTalk(
        0x0009,
        (
            '#2040180085V感觉怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180086V会不会很容易滑倒，\n',
            '或者说有些太硬了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180087V#006F有些吧，不过问题不大。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180088V穿上去很合适，\n',
            '走起来也很舒服。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180089V不愧是斯托雷加啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180120V这还只是样品，\n',
            '相信成品会更加出色的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180121V真是辛苦你们了。\n',
            '你们做得很好，帮了我大忙啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180104V#006F您也要加油哦，\n',
            '我很期待新产品呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180123V哈哈哈，我一定会把你这番话\n',
            '转达给斯托雷加社的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020180106V#010F那么，多谢您的关照。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180107V#001F再见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(23, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【测试新产品】',
            (TxtCtl.SetColor, 0x0),
            '完成！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_28(0x002A, 0x04, 0x10)
    OP_28(0x002A, 0x01, 0x0010)
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Return()

    def _loc_1ECB(): pass

    label('loc_1ECB')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Leq,
            Expr.Return,
        ),
        'loc_20E5',
    )

    OP_63(0x0009)
    Sleep(400)

    ChrTalk(
        0x0009,
        (
            '#2040180126V…………唔～～唔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180127V很抱歉，\n',
            '还走得不太够。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180128V鞋底还没怎么磨损，\n',
            '这样是无法得到测试结果的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180129V#003F嗯～这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180130V我还以为已经走得够多了呢……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180131V唔～\n',
            '可是已经没有时间了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0101, 400)

    ChrTalk(
        0x0009,
        (
            '#2040180132V很遗憾，\n',
            '任务已经失败了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x14, 0x17, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(800)

    ChrTalk(
        0x0101,
        (
            '#0010180133V#007F呜……对不起啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180134V尽管专门来接受了任务，\n',
            '可还是没能帮上一点忙……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180135V最低限度的数据还是有的，\n',
            '我想没什么问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180136V再过不久成品就能上市了，\n',
            '敬请期待哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x002A, 0x04, 0x40)
    OP_28(0x002A, 0x01, 0x0020)
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    Return()

    def _loc_20E5(): pass

    label('loc_20E5')

    Return()

# id: 0x0005 offset: 0x20E6
@scena.Code('func_05_20E6')
def func_05_20E6():
    If(
        (
            (Expr.Eval, "OP_40(0x011C)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2164',
    )

    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(800)

    ChrTalk(
        0x0009,
        (
            '#2040180137V哎？\n',
            '那双鞋子不见了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180183V没有『斯托雷加α』的话\n',
            '就不能继续测试了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Return()

    def _loc_2164(): pass

    label('loc_2164')

    ChrTalk(
        0x0101,
        (
            '#0010180144V#000F蒂亚利研究员，\n',
            '我们来汇报情况了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180145V因为我们还有急事，\n',
            '所以请赶快检查一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180146V哦，是吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180147V那么，\n',
            '这就检查一下这双鞋吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0009, 270, 400)
    OP_62(0x0009, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)

    ChrTalk(
        0x0009,
        (
            '#2040180077V…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x4),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_2630',
    )

    OP_2B(0x002A, 0x0002)
    OP_63(0x0009)
    Sleep(400)

    OP_62(0x0009, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(800)

    ChrTalk(
        0x0009,
        (
            '#2040180078V……哦哦，真厉害。\n',
            '鞋底磨损了很多啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180079V从磨损的情况来看，\n',
            '我选择的材料\n',
            '是相当合适的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0101, 400)

    ChrTalk(
        0x0009,
        (
            '#2040180080V嗯，测试非常成功。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180152V#501F呼，太好了～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180153V那么任务就此完成了吧？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180154V是啊，辛苦大家了。\n',
            '你们帮了我大忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180155V啊，等一下。\n',
            '你是斯托雷加的爱好者对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180156V……那么，\n',
            '这个送给你作为礼物吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '斯托雷加β',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(400)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(800)

    ChrTalk(
        0x0101,
        (
            '#0010180157V#000F这、这是……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180094V是厂家专门送过来的，\n',
            '给研究者参考用的新产品哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180159V开发已经告一段落了，\n',
            '这东西对我来说也不需要了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x08, 0x09, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(800)

    ChrTalk(
        0x0101,
        (
            '#0010180099V#001F哇啊，谢谢～！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180161V我期待着新产品的上市哦。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180162V我一定会把你这番话\n',
            '转达给斯托雷加社的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180163V那么，你们请多保重。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020180164V#010F真是麻烦你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180107V#001F再见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    AddItem(0x011D, 1)
    PlaySE(23, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【测试新产品】',
            (TxtCtl.SetColor, 0x0),
            '完成！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_28(0x002A, 0x04, 0x10)
    OP_28(0x002A, 0x01, 0x0010)
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Return()

    def _loc_2630(): pass

    label('loc_2630')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2874',
    )

    OP_63(0x0009)
    Sleep(400)

    OP_62(0x0009, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(800)

    ChrTalk(
        0x0009,
        (
            '#2040180108V…………嗯。\n',
            '鞋底已经磨损得足够了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180079V从磨损的情况来看，\n',
            '我选择的材料\n',
            '是相当合适的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0101, 400)

    ChrTalk(
        0x0009,
        (
            '#2040180110V好，测试成功。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180152V#501F呼，太好了～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180153V那么任务就此完成了吧？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180154V是啊，辛苦大家了。\n',
            '你们帮了我大忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180172V#006F我期待着新产品的上市哦。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180173V我一定会把你这番话\n',
            '转达给斯托雷加社的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180163V那么，你们请多保重。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020180175V#010F真是麻烦你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180107V#001F再见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(23, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【测试新产品】',
            (TxtCtl.SetColor, 0x0),
            '完成！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_28(0x002A, 0x04, 0x10)
    OP_28(0x002A, 0x01, 0x0010)
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Return()

    def _loc_2874(): pass

    label('loc_2874')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Leq,
            Expr.Return,
        ),
        'loc_296B',
    )

    OP_63(0x0009)
    Sleep(400)

    ChrTalk(
        0x0009,
        (
            '#2040180127V很抱歉，\n',
            '还走得不太够。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180128V鞋底还没怎么磨损，\n',
            '这样是无法得到测试结果的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180179V#505F嗯～这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180180V#000F那么，我们再继续吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0101, 400)

    ChrTalk(
        0x0009,
        (
            '#2040180181V啊，麻烦你们了，\n',
            '这件事就继续拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x002A, 0x01, 0x0008)

    Return()

    def _loc_296B(): pass

    label('loc_296B')

    Return()

# id: 0x0006 offset: 0x296C
@scena.Code('func_06_296C')
def func_06_296C():
    If(
        (
            (Expr.Eval, "OP_40(0x011C)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_29EA',
    )

    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(800)

    ChrTalk(
        0x0009,
        (
            '#2040180137V哎？\n',
            '那双鞋子不见了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180183V没有『斯托雷加α』的话\n',
            '就不能继续测试了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Return()

    def _loc_29EA(): pass

    label('loc_29EA')

    ChrTalk(
        0x0101,
        (
            '#0010180073V#000F你好，蒂亚利研究员。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180074V那几个地方都已经走过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180075V哦，辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180076V好，那就让我\n',
            '检查一下这双鞋吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0009, 270, 400)
    OP_62(0x0009, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)

    ChrTalk(
        0x0009,
        (
            '#2040180077V…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x4),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_314E',
    )

    OP_2B(0x002A, 0x0002)
    OP_63(0x0009)
    Sleep(400)

    OP_62(0x0009, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(800)

    ChrTalk(
        0x0009,
        (
            '#2040180078V……哦哦，真厉害。\n',
            '鞋底磨损了很多啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180079V从磨损的情况来看，\n',
            '我选择的材料\n',
            '是相当合适的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0101, 400)

    ChrTalk(
        0x0009,
        (
            '#2040180080V嗯，测试非常成功。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180081V#501F呼～太好了～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180082V我刚才还在想，\n',
            '如果您叫我们继续该怎么办。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2C24',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_2C00',
    )

    ChrTalk(
        0x0107,
        (
            '#0070180083V#061F呵呵呵，太好了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2C24')

    def _loc_2C00(): pass

    label('loc_2C00')

    ChrTalk(
        0x0107,
        (
            '#0070180084V#061F呵呵呵，太好了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2C24(): pass

    label('loc_2C24')

    ChrTalk(
        0x0009,
        (
            '#2040180085V感觉怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180086V会不会很容易滑倒，\n',
            '或者说有些太硬了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180087V#006F有些吧，不过问题不大。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180088V穿上去很合适，\n',
            '走起来也很舒服。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180089V不愧是斯托雷加啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180090V啊，对了。\n',
            '你是斯托雷加的\n',
            '忠实支持者对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180091V……那么，\n',
            '我就把这个作为礼物送给你吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180092V因为你们做得比我预想的要好得多，\n',
            '就当成是额外奖励吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '斯托雷加β',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(400)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(800)

    ChrTalk(
        0x0101,
        (
            '#0010180093V#004F这、这是……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180094V是厂家专门送过来的，\n',
            '给研究者参考用的新产品哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180095V这可是还没有向外界披露的新型号呢。\n',
            '商店里面自然也还没出售了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020180096V#014F这样好吗？\n',
            '这个东西太贵重了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0102, 400)

    ChrTalk(
        0x0009,
        (
            '#2040180097V唔，反正开发已经告一段落了，\n',
            '我也就不需要了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180098V把这双鞋送给懂得其价值的人，\n',
            '也算是体现出它的价值吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x08, 0x09, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(800)

    ChrTalk(
        0x0101,
        (
            '#0010180099V#001F哇啊，谢谢～！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180100V既可以协助开发，\n',
            '又还可以得到新产品……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180101V真的是～一件美妙的任务啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0101, 400)

    ChrTalk(
        0x0009,
        (
            '#2040180102V哈哈，彼此彼此吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180103V因为你们的努力才使得\n',
            '我的研究成果得到充分的证明呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180104V#006F您也要加油哦，\n',
            '我很期待新产品呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180105V唔，我一定会把你这番话\n',
            '转达给斯托雷加社的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020180106V#010F那么，多谢您的关照。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180107V#001F再见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    AddItem(0x011D, 1)
    PlaySE(23, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【测试新产品】',
            (TxtCtl.SetColor, 0x0),
            '完成！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_28(0x002A, 0x04, 0x10)
    OP_28(0x002A, 0x01, 0x0010)
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Return()

    def _loc_314E(): pass

    label('loc_314E')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_34E7',
    )

    OP_63(0x0009)
    Sleep(400)

    OP_62(0x0009, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(800)

    ChrTalk(
        0x0009,
        (
            '#2040180108V…………嗯。\n',
            '鞋底已经磨损得足够了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180079V从磨损的情况来看，\n',
            '我选择的材料\n',
            '是相当合适的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0101, 400)

    ChrTalk(
        0x0009,
        (
            '#2040180110V好，测试成功。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180081V#501F呼～太好了～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180082V我刚才还在想，\n',
            '如果您叫我们继续该怎么办。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_32B7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_3293',
    )

    ChrTalk(
        0x0107,
        (
            '#0070180083V#061F呵呵呵，太好了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_32B7')

    def _loc_3293(): pass

    label('loc_3293')

    ChrTalk(
        0x0107,
        (
            '#0070180084V#061F呵呵呵，太好了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_32B7(): pass

    label('loc_32B7')

    ChrTalk(
        0x0009,
        (
            '#2040180085V感觉怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180086V会不会很容易滑倒，\n',
            '或者说有些太硬了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180087V#006F有些吧，不过问题不大。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180088V穿上去很合适，\n',
            '走起来也很舒服。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180089V不愧是斯托雷加啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180120V这还只是样品，\n',
            '相信成品会更加出色的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180121V真是辛苦你们了。\n',
            '你们做得很好，帮了我大忙啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180104V#006F您也要加油哦，\n',
            '我很期待新产品呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180123V哈哈哈，我一定会把你这番话\n',
            '转达给斯托雷加社的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020180106V#010F那么，多谢您的关照。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180107V#001F再见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(23, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【测试新产品】',
            (TxtCtl.SetColor, 0x0),
            '完成！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_28(0x002A, 0x04, 0x10)
    OP_28(0x002A, 0x01, 0x0010)
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Return()

    def _loc_34E7(): pass

    label('loc_34E7')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Leq,
            Expr.Return,
        ),
        'loc_368C',
    )

    OP_63(0x0009)
    Sleep(400)

    ChrTalk(
        0x0009,
        (
            '#2040180126V…………唔～～唔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180127V很抱歉，\n',
            '还走得不太够。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0101, 400)

    ChrTalk(
        0x0009,
        (
            '#2040180128V鞋底还没怎么磨损，\n',
            '这样是无法得到测试结果的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180240V#505F嗯～这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180130V我还以为已经走得够多了呢……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020180242V#010F没办法，\n',
            '我们再继续吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180243V啊，麻烦你们了，\n',
            '不过还是请尽量多走些吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010170077V#006F嗯，我知道了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180245V那我们待会儿再来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2040180246V这件事就继续拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x002A, 0x01, 0x0008)

    Return()

    def _loc_368C(): pass

    label('loc_368C')

    Return()

# id: 0x0007 offset: 0x368D
@scena.Code('func_07_368D')
def func_07_368D():
    SetChrFlags(0x000C, 0x0080)
    OP_64(0x02, 0x0001)
    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '明日料理',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(0x0341, 1)
    OP_28(0x002D, 0x01, 0x0008)
    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
