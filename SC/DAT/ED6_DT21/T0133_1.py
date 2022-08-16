import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T0133_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0133_1 ._SN')

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
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/T0133_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
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
    ChrTalk(
        0x0101,
        (
            '#0010470171V#1001F您好啊，潘杜爷爷。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030470172V#020F啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3680470173V哦，是你们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3680470174V找我有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010400813V#1015F嗯，其实……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '诉说了在寻找拉欧老人\n',
            '所说的炖煮料理食谱的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x0101,
        (
            '#0010470176V#1011F潘杜爷爷和拉欧爷爷\n',
            '的年龄似乎很接近啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030470177V#020F有关那个料理，\n',
            '您知道些什么吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0103, 400)

    ChrTalk(
        0x00FE,
        (
            '#3680470178V嗯，年轻的时候\n',
            '好像确实吃过……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3680470179V不过我和那老小子不同，\n',
            '对食物没有太大兴趣，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3680470180V直说好了，\n',
            '已经完全没印象了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010470181V#1016F啊，是那样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010470182V嗯、这可该怎么办呢。',
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
        'loc_341',
    )

    ChrTalk(
        0x0106,
        (
            '#0050470183V#053F……白跑了一趟啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3F1')

    def _loc_341(): pass

    label('loc_341')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_37B',
    )

    ChrTalk(
        0x0108,
        (
            '#0080470184V#070F嗯，白跑了一趟啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3F1')

    def _loc_37B(): pass

    label('loc_37B')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3B8',
    )

    ChrTalk(
        0x0104,
        (
            '#0040470185V#031F哈哈哈。\n',
            '白跑了一趟呢',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3F1')

    def _loc_3B8(): pass

    label('loc_3B8')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3F1',
    )

    ChrTalk(
        0x0105,
        (
            '#0060470186V#045F看来……没有收获呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3F1(): pass

    label('loc_3F1')

    ChrTalk(
        0x00FE,
        (
            '#3680470187V嗯、抱歉啊。\n',
            '没帮上你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030470188V#525F您不用在意。\n',
            '我们再去找别人打听就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0103, 400)

    ChrTalk(
        0x00FE,
        (
            '#3680470189V那么你们就找城里的老婆婆\n',
            '们多问问看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3680470190V在我们那个年代，\n',
            '几乎谁都会做呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))
    OP_28(0x0075, 0x01, 0x0100)

    Return()

# id: 0x0001 offset: 0x4D7
@scena.Code('func_01_4D7')
def func_01_4D7():
    EventBegin(0x00)
    Call(1, 0x0005)

    ChrTalk(
        0x000A,
        (
            '#3600470504V女神啊、拜托您了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3600470505V让我顺利接近那位\n',
            '美丽的姐姐吧…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010470506V#1015F#2P…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010470507V呼……\n',
            '请问现在方便吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3600470508V嗯？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0101, 400)
    OP_62(0x000A, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    OP_63(0x000A)

    ChrTalk(
        0x000A,
        (
            '#3600470509V啊……难道！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3600470510V你们、是协会的人吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010470511V#1006F#2P嗯，正是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030470512V#020F我们看了委托，\n',
            '您就是安敦先生吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3600470513V啊啊，请多关照，\n',
            '我就是王都来的安敦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3600470514V虽然才刚见面，\n',
            '不过委托很急，我就直说了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3600470515V不是太困难的工作，\n',
            '请你们一定要接受啊。',
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
        'loc_7A6',
    )

    ChrTalk(
        0x0101,
        (
            '#0010470516V#1000F#2P好，您说吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010470517V究竟是什么事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(1, 0x0003)

    Jump('loc_985')

    def _loc_7A6(): pass

    label('loc_7A6')

    ChrTalk(
        0x0101,
        (
            '#0010470518V#1015F#2P啊，抱歉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010470519V马上开始的话\n',
            '恐怕还不行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3600470520V啊、果然…\n',
            '我就知道会被拒绝。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000A, 180, 400)

    ChrTalk(
        0x000A,
        (
            '#3600470521V谁也不会听\n',
            '我说话啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3600470522V以前也是……\n',
            '以后也是。',
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
            '#0010470523V#1016F#2P不、不用那么大反应啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030470524V#020F并没有拒绝啊，\n',
            '不要误会。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030470525V等我们有空时会回来，\n',
            '请稍等一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3600470526V说好话谁都会，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3600470527V算了，我等你们，\n',
            '虽然也不抱什么希望。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0076, 0x01, 0x8000)

    def _loc_985(): pass

    label('loc_985')

    EventEnd(0x00)

    Return()

# id: 0x0002 offset: 0x988
@scena.Code('func_02_988')
def func_02_988():
    EventBegin(0x00)
    Call(1, 0x0005)

    ChrTalk(
        0x000A,
        (
            '#3600470528V…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3600470529V难道…\n',
            '你们是游击士协会的人？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010470530V#1002F#2P嗯……正是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3600470531V是吗……\n',
            '你们回来了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3600470532V那么，愿意帮助我\n',
            '这个不幸的人吗？',
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
        'loc_BAB',
    )

    ChrTalk(
        0x0101,
        (
            '#0010470533V#1006F#2P嗯，好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    OP_63(0x000A)

    ChrTalk(
        0x000A,
        (
            '#3600470534V噢噢！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0101, 400)

    ChrTalk(
        0x000A,
        (
            '#3600470535V呵，真的\n',
            '你们愿意接受吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010470536V#1016F#2P我、我们没有必要\n',
            '对你说谎啊！！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010470537V#1011F到底是什么委托啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(1, 0x0003)

    Jump('loc_CBB')

    def _loc_BAB(): pass

    label('loc_BAB')

    ChrTalk(
        0x0101,
        (
            '#0010470538V#1007F#2P抱歉……\n',
            '我们还有别的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3600470539V呼～是吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3600470540V果然，你们也是\n',
            '无情的家伙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010470541V#1019F#2P……说什么啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010470542V#1022F总之，等我们有空时\n',
            '就会回来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3600470543V算了，我等你们，\n',
            '虽然也不抱什么希望。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_CBB(): pass

    label('loc_CBB')

    EventEnd(0x00)

    Return()

# id: 0x0003 offset: 0xCBE
@scena.Code('func_03_CBE')
def func_03_CBE():
    ChrTalk(
        0x000A,
        (
            '#3600470544V嗯、其实…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3600470545V我希望你们替我\n',
            '收集药的材料。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3600470546V嗯……～？\n',
            '这就是材料一览。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '魔兽甲壳　　　×５个\n',
            '魔兽羽翼　　　×５个\n',
            '魔兽之种　　　×５个\n',
            '珍珠草　　　　×１条',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x0103,
        (
            '#0030470547V#025F魔兽的掉落物\n',
            '倒还好说…',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030470548V……不过『珍珠草』\n',
            '好像是鱼的一种吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3600470549V嗯，是种很少见的鱼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3600470550V我想做的药材\n',
            '需要那种鱼的肝。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3600470551V听说在水草多的浅河中\n',
            '可以钓到它。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010470552V#1015F#2P是吗、水草多的浅水河……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010470553V#1006F#2P……好，记录完毕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3600470554V啊、记录完毕？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3600470555V……那么、接下来就拜托了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000A, 180, 400)

    ChrTalk(
        0x0101,
        (
            '#0010470556V#1004F#2P啊、啊！？这就完了啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030470557V#022F请等一下！\n',
            '我还有话要问。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0101, 400)

    ChrTalk(
        0x000A,
        (
            '#3600470558V啊？什么？\n',
            '已经说明的很清楚了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030470559V#027F你刚才\n',
            '说是为了做药……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030470560V究竟是什么药？\n',
            '为什么目的而做？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030470561V请把药的名称和使用目的\n',
            '告诉我们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3600470562V为、为什么非要\n',
            '说那种事不可啊。',
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
        'loc_112A',
    )

    ChrTalk(
        0x0106,
        (
            '#0050470563V#050F我们有义务\n',
            '防止犯罪事件的发生。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050470564V药品因使用方法的不同，\n',
            '也可以用于毒品等途径呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_127F')

    def _loc_112A(): pass

    label('loc_112A')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_119E',
    )

    ChrTalk(
        0x0108,
        (
            '#0080470565V#070F并不是怀疑你，\n',
            '但毕竟药是有危险的，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080470566V请你配合一下，\n',
            '告诉我们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_127F')

    def _loc_119E(): pass

    label('loc_119E')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_120C',
    )

    ChrTalk(
        0x0104,
        (
            '#0040470567V#030F不管什么药\n',
            '也都存在危险，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040470568V为了防患于未然，\n',
            '必须要问清楚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_127F')

    def _loc_120C(): pass

    label('loc_120C')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_127F',
    )

    ChrTalk(
        0x0105,
        (
            '#0060470569V#040F不管是什么药，\n',
            '用得不对也都有风险，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060470570V保险起见，\n',
            '我们必须确认一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_127F(): pass

    label('loc_127F')

    ChrTalk(
        0x0103,
        (
            '#0030470571V#020F嗯，就是那样了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030470572V所以请您\n',
            '告诉我们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3600470573V呼、是吗。\n',
            '算了，其实也无所谓。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3600470574V我想做得药就是——\n',
            '『千杯不醉的秘药』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3600470575V服下这种药之后，\n',
            '不管怎么喝酒\n',
            '也绝对不会醉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3600470576V这是教区长告诉我的，\n',
            '所以绝对可信。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010470577V#1011F#2P嘿～好厉害的药啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010470578V怎么喝酒也都\n',
            '不会醉…',
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
        'loc_1431',
    )

    ChrTalk(
        0x0104,
        (
            '#0040470579V#032F哟哟……我很有兴趣啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1431(): pass

    label('loc_1431')

    ChrTalk(
        0x0103,
        (
            '#0030470580V#023F什么啊。\n',
            '好无聊的药。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030470581V怎么喝也都不会醉，\n',
            '那不就失去了喝酒的意义。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010470582V#1015F#2P呼～雪拉姐的\n',
            '喝酒方式也是不对的啦。',
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
        'loc_151D',
    )

    ChrTalk(
        0x0107,
        (
            '#0070470583V#064F可是可是～你为什么\n',
            '要做那种药呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15E5')

    def _loc_151D(): pass

    label('loc_151D')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1560',
    )

    ChrTalk(
        0x0105,
        (
            '#0060470584V#040F不过，为什么\n',
            '要做那种药呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15E5')

    def _loc_1560(): pass

    label('loc_1560')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_15A5',
    )

    ChrTalk(
        0x0108,
        (
            '#0080470585V#070F不过，你为什么\n',
            '要做那种药呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15E5')

    def _loc_15A5(): pass

    label('loc_15A5')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_15E5',
    )

    ChrTalk(
        0x0104,
        (
            '#0040470586V#030F不过，你为何\n',
            '要做那种药呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_15E5(): pass

    label('loc_15E5')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_162A',
    )

    ChrTalk(
        0x0106,
        (
            '#0050470587V#050F是想用在无法拒绝\n',
            '的酒宴中吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_16F0')

    def _loc_162A(): pass

    label('loc_162A')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_166D',
    )

    ChrTalk(
        0x0104,
        (
            '#0040470588V#030F难道是有无法拒绝\n',
            '的酒会吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_16F0')

    def _loc_166D(): pass

    label('loc_166D')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_16B0',
    )

    ChrTalk(
        0x0108,
        (
            '#0080470589V#070F是因为有无法拒绝\n',
            '的酒席吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_16F0')

    def _loc_16B0(): pass

    label('loc_16B0')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_16F0',
    )

    ChrTalk(
        0x0105,
        (
            '#0060470590V#040F是因为有无法拒绝\n',
            '的酒席吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_16F0(): pass

    label('loc_16F0')

    ChrTalk(
        0x000A,
        (
            '#3600470591V要说成无法拒绝的酒会倒是\n',
            '不太准确…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3600470592V不过…确实也是场\n',
            '无可避免的酒会啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3600470593V呼，所以无论如何\n',
            '也需要那种药。',
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
        'loc_17D1',
    )

    ChrTalk(
        0x0104,
        (
            '#0040470594V#035F呼～那种心情……\n',
            '我也深有体会啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_17D1(): pass

    label('loc_17D1')

    ChrTalk(
        0x0101,
        (
            '#0010470595V#1020F#2P但、但别喝太多，\n',
            '不行吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010470596V#1007F呼、还是适度\n',
            '饮酒比较好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030470597V#025F呼，这话说得没错……',
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
        'loc_18A2',
    )

    ChrTurnDirection(0x0106, 0x0103, 400)

    ChrTalk(
        0x0106,
        (
            '#0050470598V#551F但是不该由你来说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1957')

    def _loc_18A2(): pass

    label('loc_18A2')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_18E8',
    )

    ChrTurnDirection(0x0108, 0x0103, 400)

    ChrTalk(
        0x0108,
        (
            '#0080470599V#073F喂喂……\n',
            '你在说那个吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1957')

    def _loc_18E8(): pass

    label('loc_18E8')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1957',
    )

    ChrTurnDirection(0x0104, 0x0103, 400)

    ChrTalk(
        0x0104,
        (
            '#0040470600V#034F雪、雪拉……\n',
            '你竟然说喝酒要适量……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040470601V（真是不自觉啊。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1957(): pass

    label('loc_1957')

    ChrTalk(
        0x000A,
        (
            '#3600470602V……委托的理由\n',
            '你们现在都明白了？',
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
        'loc_19A2',
    )

    ChrSetDirection(0x0106, 135, 400)

    Jump('loc_19CF')

    def _loc_19A2(): pass

    label('loc_19A2')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_19BA',
    )

    ChrSetDirection(0x0108, 135, 400)

    Jump('loc_19CF')

    def _loc_19BA(): pass

    label('loc_19BA')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_19CF',
    )

    ChrSetDirection(0x0104, 135, 400)

    def _loc_19CF(): pass

    label('loc_19CF')

    ChrTalk(
        0x0101,
        (
            '#0010470603V#1002F#2P嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030470604V#020F……算可以了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030470605V那么，等材料收集完毕之后\n',
            '我们会回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3600470606V啊啊，拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3600470607V那就交给你们了。\n',
            '这可是关系到我将来的大事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010470608V#1011F#2P？？？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010470609V#1016F虽、虽然不懂……\n',
            '不过我们会努力的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))
    OP_28(0x0076, 0x04, 0x04)
    OP_28(0x0076, 0x04, 0x08)
    OP_28(0x0076, 0x01, 0x0001)
    OP_28(0x0076, 0x01, 0x0002)
    OP_28(0x0076, 0x01, 0x0004)
    ChrSetDirection(0x000A, 180, 400)
    UnlockAchievement(0x01, 0x0006, 0x00)

    Return()

# id: 0x0004 offset: 0x1B2B
@scena.Code('func_04_1B2B')
def func_04_1B2B():
    EventBegin(0x00)
    Call(1, 0x0005)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_1C07',
    )

    ChrTalk(
        0x0101,
        (
            '#0010470614V#1000F#2P那个～安敦先生，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010470615V能再打扰您一下吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3600470616V嗯……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0101, 400)

    ChrTalk(
        0x000A,
        (
            '#3600470617V啊，游击士，\n',
            '你们回来了啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3600470618V啊、难道说…\n',
            '药的材料都找到了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1CB7')

    def _loc_1C07(): pass

    label('loc_1C07')

    ChrTalk(
        0x0101,
        (
            '#0010470619V#1018F#2P哟！安敦先生，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010470620V打扰一下可以吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3600470616V嗯……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0101, 400)

    ChrTalk(
        0x000A,
        (
            '#3600470622V啊，各位游击士，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3600470623V药的材料都找到了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1CB7(): pass

    label('loc_1CB7')

    OP_61(0x0101)

    ChrTalk(
        0x0101,
        (
            '#0010470624V#1006F#2P嗯，确认一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '将材料拿给安敦看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    If(
        (
            (Expr.Eval, "OP_40(0x03A4, 0x00)"),
            (Expr.PushLong, 0x5),
            Expr.Geq,
            (Expr.Eval, "OP_40(0x039F, 0x00)"),
            (Expr.PushLong, 0x5),
            Expr.Geq,
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x03AB, 0x00)"),
            (Expr.PushLong, 0x5),
            Expr.Geq,
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x03BA, 0x00)"),
            (Expr.PushLong, 0x1),
            Expr.Geq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1D6A',
    )

    OP_28(0x0076, 0x01, 0x1000)
    RemoveItem(ItemTable['魔兽甲壳'], 5)
    RemoveItem(ItemTable['魔兽羽翼'], 5)
    RemoveItem(ItemTable['魔兽之种'], 5)
    RemoveItem(ItemTable['珍珠草'], 1)

    def _loc_1D6A(): pass

    label('loc_1D6A')

    If(
        (
            (Expr.Eval, "OP_29(0x0076, 0x01, 0x1000)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1E4D',
    )

    ChrTalk(
        0x000A,
        (
            '#3600470625V嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3600470626V不好意思，\n',
            '好像还没收集全啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010470627V#1004F#2P啊？是吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3600470628V啊啊，再确认一下笔记吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3600470629V那么，等材料收集完毕之后\n',
            '再来找我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000A, 180, 400)

    Jump('loc_21AC')

    def _loc_1E4D(): pass

    label('loc_1E4D')

    ChrTalk(
        0x000A,
        (
            '#3600470630V噢噢！！！\n',
            '全部都收集到了啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3600470631V太好了！\n',
            '太感谢了！各位游击士！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3600470632V很好！！\n',
            '那么马上去调制药吧！！',
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
            '#0010470633V#1004F#2P啊……？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010470634V我、我们也一起去吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3600470635V啊啊、是你们帮我收集到材料的啊，\n',
            '一定要一起来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3600470636V来见证我\n',
            '感动的瞬间吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010470637V#1007F#2P虽、虽然完全\n',
            '不明白……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030440822V#020F嗯，没关系吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030470639V不过都到了委托的最后环节，\n',
            '还是去看看吧。',
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
        'loc_2079',
    )

    ChrTalk(
        0x0106,
        (
            '#0050470640V#051F啊啊，没有拒绝的理由啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_212D')

    def _loc_2079(): pass

    label('loc_2079')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_20B3',
    )

    ChrTalk(
        0x0104,
        (
            '#0040470641V#030F嗯，没理由拒绝啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_212D')

    def _loc_20B3(): pass

    label('loc_20B3')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_20EF',
    )

    ChrTalk(
        0x0108,
        (
            '#0080470642V#070F嗯，没有理由拒绝啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_212D')

    def _loc_20EF(): pass

    label('loc_20EF')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_212D',
    )

    ChrTalk(
        0x0105,
        (
            '#0060470643V#040F啊啊～也没有理由\n',
            '拒绝啊…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_212D(): pass

    label('loc_212D')

    ChrTalk(
        0x000A,
        (
            '#3600470644V很好，决定了！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3600470645V那么！！这就去找教区长吧！！\n',
            'Ｌｅｔ＇ｓ　ｇｏ！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_28(0x0076, 0x01, 0x2000)
    NewScene('ED6_DT21/T0130._SN', 100, 0, 0)
    IdleLoop()

    def _loc_21AC(): pass

    label('loc_21AC')

    EventEnd(0x00)

    Return()

# id: 0x0005 offset: 0x21AF
@scena.Code('func_05_21AF')
def func_05_21AF():
    Fade(1000)
    OP_4A(0x000A, 255)
    ChrSetPos(0x0101, 54300, 10300, 45000, 135)
    ChrSetPos(0x0103, 53830, 10300, 46000, 135)
    ChrSetPos(0x00F8, 53300, 10300, 45070, 135)
    ChrSetPos(0x00F9, 52830, 10300, 46040, 135)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_222B',
    )

    ChrSetPos(0x00F9, 53300, 10300, 45070, 135)
    ChrSetPos(0x00F8, 52830, 10300, 46040, 135)

    def _loc_222B(): pass

    label('loc_222B')

    CameraMove(54840, 10300, 44060, 0)
    OP_67(0, 5660, -10000, 0)
    CameraSetDistance(2650, 0)
    OP_6C(180000, 0)
    OP_6E(262, 0)
    OP_0D()

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
