import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T0610_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0610_1 ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

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
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/T0610_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x2D44
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
    EventBegin(0x00)
    OP_8C(0x000D, 250, 0)
    Fade(1000)
    SetChrPos(0x0101, -62390, 0, -22680, 270)
    SetChrPos(0x0103, -62210, 0, -24020, 315)
    SetChrPos(0x00F8, -61170, 0, -23660, 270)
    SetChrPos(0x00F9, -61070, 0, -22240, 270)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_129',
    )

    SetChrPos(0x00F9, -61170, 0, -23660, 270)
    SetChrPos(0x00F8, -61070, 0, -22240, 270)

    def _loc_129(): pass

    label('loc_129')

    OP_6D(-63450, 0, -21840, 0)
    OP_67(0, 6710, -10000, 0)
    OP_6B(2710, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_1D9',
    )

    SetChrName('拜舍尔')

    ChrTalk(
        0x000D,
        (
            '#3440460837V#1P好了……\n',
            '总算雾散天晴了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3440460838V#1P我也还差不多该\n',
            '准备出发了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1FC')

    def _loc_1D9(): pass

    label('loc_1D9')

    ChrTalk(
        0x000D,
        (
            '#3440460839V#1P唉……真没劲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1FC(): pass

    label('loc_1FC')

    ChrTalk(
        0x0101,
        (
            '#0010460840V#1015F#2P嗯～打扰一下行吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000D, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    OP_63(0x000D)
    ChrTurnDirection(0x000D, 0x0101, 400)

    ChrTalk(
        0x000D,
        (
            '#3440460841V#1P嗯？什么事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010460842V#1011F#2P我们是协会\n',
            '派来的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460843V您是发出委托的\n',
            '拜舍尔先生？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3440460844V#1P哦，没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3440460845V#1P太好了。\n',
            '终于来了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010460846V#1006F#2P嗯，总之\n',
            '先来听听需要委托的是什么事吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030460847V#020F公告板上看来\n',
            '您好像是要委托调查什么吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0103, 400)

    ChrTalk(
        0x000D,
        (
            '#3440460848V#1P啊啊，其实是想委托\n',
            '调查洛连特地区的钓鱼地点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3440460849V#1P详细的过程\n',
            '我稍后再进行说明……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3440460850V#1P……那，怎样？\n',
            '能帮忙吗？',
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
        'loc_490',
    )

    Call(1, 0x0002)

    Jump('loc_5DC')

    def _loc_490(): pass

    label('loc_490')

    ChrTalk(
        0x0101,
        (
            '#0010460851V#1007F#2P唔……\n',
            '十分抱歉……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460852V很遗憾，现在\n',
            '没办法马上接受。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x000D,
        (
            '#3440460853V#1P哎呀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3440460854V#1P有什么紧急的\n',
            '工作在手吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030460855V#025F嗯嗯，抱歉哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030460856V有空了\n',
            '会再来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0103, 400)

    ChrTalk(
        0x000D,
        (
            '#3440460857V#1P嗯，那也没问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3440460858V#1P那么，以后再麻烦你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0073, 0x01, 0x8000)

    def _loc_5DC(): pass

    label('loc_5DC')

    EventEnd(0x00)

    Return()

# id: 0x0001 offset: 0x5DF
@scena.Code('Init')
def Init():
    EventBegin(0x00)
    Fade(1000)
    SetChrPos(0x0101, -62390, 0, -22680, 270)
    SetChrPos(0x0103, -62210, 0, -24020, 315)
    SetChrPos(0x00F8, -61170, 0, -23660, 270)
    SetChrPos(0x00F9, -61070, 0, -22240, 270)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_659',
    )

    SetChrPos(0x00F9, -61170, 0, -23660, 270)
    SetChrPos(0x00F8, -61070, 0, -22240, 270)

    def _loc_659(): pass

    label('loc_659')

    ChrTurnDirection(0x000D, 0x0101, 0)
    OP_6D(-63450, 0, -21840, 0)
    OP_67(0, 6710, -10000, 0)
    OP_6B(2710, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(
        0x000D,
        (
            '#3440460859V#1P哦，游击士们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3440460860V#1P钓鱼地点的调查，\n',
            '能接受了吗？',
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
        'loc_74B',
    )

    Call(1, 0x0002)

    Jump('loc_7EA')

    def _loc_74B(): pass

    label('loc_74B')

    ChrTalk(
        0x0101,
        (
            '#0010460861V#1007F#2P抱歉……\n',
            '还不行呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460862V有空了\n',
            '我们马上回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3440460863V#1P怎么，还不行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3440460864V#1P那，以后再麻烦你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7EA(): pass

    label('loc_7EA')

    EventEnd(0x00)

    Return()

# id: 0x0002 offset: 0x7ED
@scena.Code('ReInit')
def ReInit():
    ChrTalk(
        0x0101,
        (
            '#0010460865V#1006F#2P这点小事没问题的。\n',
            '交给我们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x000D,
        (
            '#3440460866V#1P呀～太感谢了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3440460867V#1P果然有困难就是\n',
            '要找游击士啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010460868V#1015F#2P不过，为什么\n',
            '要调查什么钓鱼地点呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460869V还特地付酬金……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3440460870V#1P啊啊，其实我是\n',
            '『钓公师团』的团员。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3440460871V#1P预计很快就要和同伴们\n',
            '开个钓鱼的讲习会了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3440460872V#1P于是就在候补场地洛连特地区\n',
            '先调查一下情况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9E0',
    )

    ChrTalk(
        0x0104,
        (
            '#0040460873V#030F嗬，钓鱼的讲习会啊。\n',
            '听起来真讲究。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B16')

    def _loc_9E0(): pass

    label('loc_9E0')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A43',
    )

    ChrTalk(
        0x0108,
        (
            '#0080460874V#070F噢，钓鱼的讲习会啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080460875V我要是有机会\n',
            '也想参加呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B16')

    def _loc_A43(): pass

    label('loc_A43')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_ABC',
    )

    ChrTalk(
        0x0106,
        (
            '#0050460876V#052F啊啊，有这样的事啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050460877V听起来更像是同好的聚会，\n',
            '活动还挺像那么回事呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B16')

    def _loc_ABC(): pass

    label('loc_ABC')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B16',
    )

    ChrTalk(
        0x0107,
        (
            '#0070460878V#560F钓鱼的讲习会啊～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070460879V嘿嘿，我也\n',
            '想学学看呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B16(): pass

    label('loc_B16')

    ChrTalk(
        0x000D,
        (
            '#3440460880V#1P嘿嘿，不错的计划吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3440460881V#1P在王都也是盛况空前啦，\n',
            '接下来打算办得更热闹哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3440460882V#1P本来这个调查\n',
            '打算自己做的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_C07',
    )

    ChrTalk(
        0x000D,
        (
            '#3440460883V#1P但是由于这雾耽误了时间。\n',
            '于是就打算拜托专业人士了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C45')

    def _loc_C07(): pass

    label('loc_C07')

    ChrTalk(
        0x000D,
        (
            '#3440460884V#1P不巧起了这雾。\n',
            '于是就打算拜托专业人士了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C45(): pass

    label('loc_C45')

    ChrTalk(
        0x0103,
        (
            '#0030460885V#020F……原来如此。\n',
            '调查的目的明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030460886V那么，具体来说\n',
            '怎么调查才好？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0103, 400)

    ChrTalk(
        0x000D,
        (
            '#3440460887V#1P啊啊，想拜托大家的就是\n',
            '确认一下钓鱼地点的位置。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3440460888V#1P哪里能钓到鱼，\n',
            '报告这个就可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010460889V#1015F#2P嗯～这也就是说……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460890V#1000F找个看起来不错的水边，\n',
            '试着钓１条就行了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x000D,
        (
            '#3440460891V#1P哦，没错了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3440460892V#1P你看起来好像很高兴，\n',
            '难不成也是钓鱼迷？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.Eval, "OP_C0(0x12, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)"),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_E40',
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_E40(): pass

    label('loc_E40')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.Eval, "OP_C0(0x12, 0x00000001, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)"),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_E89',
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_E89(): pass

    label('loc_E89')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.Eval, "OP_C0(0x12, 0x00000002, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)"),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_ED2',
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_ED2(): pass

    label('loc_ED2')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.Eval, "OP_C0(0x12, 0x00000003, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)"),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_F1B',
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_F1B(): pass

    label('loc_F1B')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.Eval, "OP_C0(0x12, 0x00000004, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)"),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_F64',
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_F64(): pass

    label('loc_F64')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.Eval, "OP_C0(0x12, 0x00000005, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)"),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_FAD',
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_FAD(): pass

    label('loc_FAD')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.Eval, "OP_C0(0x12, 0x00000006, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)"),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_FF6',
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_FF6(): pass

    label('loc_FF6')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.Eval, "OP_C0(0x12, 0x00000007, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)"),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_103F',
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_103F(): pass

    label('loc_103F')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.Eval, "OP_C0(0x12, 0x00000008, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)"),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_1088',
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1088(): pass

    label('loc_1088')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.Eval, "OP_C0(0x12, 0x00000009, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)"),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_10D1',
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_10D1(): pass

    label('loc_10D1')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.Eval, "OP_C0(0x12, 0x0000000A, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)"),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_111A',
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_111A(): pass

    label('loc_111A')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.Eval, "OP_C0(0x12, 0x0000000B, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)"),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_1163',
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1163(): pass

    label('loc_1163')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.Eval, "OP_C0(0x12, 0x0000000C, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)"),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_11AC',
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_11AC(): pass

    label('loc_11AC')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.Eval, "OP_C0(0x12, 0x0000000D, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)"),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_11F5',
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_11F5(): pass

    label('loc_11F5')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.Eval, "OP_C0(0x12, 0x0000000E, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)"),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_123E',
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_123E(): pass

    label('loc_123E')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.Eval, "OP_C0(0x12, 0x0000000F, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)"),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_1287',
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1287(): pass

    label('loc_1287')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.Eval, "OP_C0(0x12, 0x00000010, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)"),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_12D0',
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_12D0(): pass

    label('loc_12D0')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.Eval, "OP_C0(0x12, 0x00000011, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)"),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_1319',
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1319(): pass

    label('loc_1319')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.Eval, "OP_C0(0x12, 0x00000012, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)"),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_1362',
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1362(): pass

    label('loc_1362')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.Eval, "OP_C0(0x12, 0x00000013, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)"),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_13AB',
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_13AB(): pass

    label('loc_13AB')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.Eval, "OP_C0(0x12, 0x00000014, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)"),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_13F4',
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_13F4(): pass

    label('loc_13F4')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.Eval, "OP_C0(0x12, 0x00000015, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)"),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_143D',
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_143D(): pass

    label('loc_143D')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.Eval, "OP_C0(0x12, 0x00000016, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)"),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_1486',
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1486(): pass

    label('loc_1486')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.Eval, "OP_C0(0x12, 0x00000017, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)"),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_14CF',
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_14CF(): pass

    label('loc_14CF')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.Eval, "OP_C0(0x12, 0x00000018, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)"),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_1518',
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1518(): pass

    label('loc_1518')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.Eval, "OP_C0(0x12, 0x00000019, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)"),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_1561',
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1561(): pass

    label('loc_1561')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x4),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_1571',
    )

    OP_A2(0x000B)

    def _loc_1571(): pass

    label('loc_1571')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1607',
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
            TXT(0x00, '◇经常钓的（其实是用钓鱼系统分歧）\n'),
            TXT(0x01, '◇几乎没钓过（其实是用钓鱼系统分歧）\n'),
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
        'loc_1607',
    )

    OP_A2(0x000B)

    def _loc_1607(): pass

    label('loc_1607')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_169F',
    )

    ChrTalk(
        0x0101,
        (
            '#0010460893V#1001F#2P嘿嘿，算是吧⊙',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460894V工作就是钓鱼，\n',
            '还真没想到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3440460895V#1P咦～没想到游击士里\n',
            '也有同样兴趣的人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_172B')

    def _loc_169F(): pass

    label('loc_169F')

    ChrTalk(
        0x0101,
        (
            '#0010460896V#1003F#2P嗯～喜欢\n',
            '倒是喜欢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460897V#1007F不过最近很忙，\n',
            '几乎都没怎么钓了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3440460898V#1P哈哈，真是可怜啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_172B(): pass

    label('loc_172B')

    ChrTalk(
        0x000D,
        (
            '#3440460899V#1P唉，那就趁这次\n',
            '工作机会歇口气吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3440460900V#1P钓鱼反正是业余爱好嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010460901V#1006F#2P嗯，虽说不能偷懒，\n',
            '但您这样说真是轻松多了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460902V那么，我们就立刻\n',
            '去找钓鱼场了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030460903V#020F整理一遍\n',
            '再回来报告。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0103, 400)

    ChrTalk(
        0x000D,
        (
            '#3440460904V#1P啊啊，麻烦你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3440460905V#1P那么，小心哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0073, 0x01, 0x0001)
    OP_28(0x0073, 0x04, 0x04)
    OP_28(0x0073, 0x04, 0x08)

    If(
        (
            (Expr.Eval, "OP_29(0x0073, 0x01, 0x0400)"),
            Expr.Return,
        ),
        'loc_18A3',
    )

    OP_28(0x0073, 0x01, 0x0002)
    OP_28(0x0073, 0x01, 0x0004)

    def _loc_18A3(): pass

    label('loc_18A3')

    If(
        (
            (Expr.Eval, "OP_29(0x0073, 0x01, 0x0800)"),
            Expr.Return,
        ),
        'loc_18BA',
    )

    OP_28(0x0073, 0x01, 0x0002)
    OP_28(0x0073, 0x01, 0x0008)

    def _loc_18BA(): pass

    label('loc_18BA')

    If(
        (
            (Expr.Eval, "OP_29(0x0073, 0x01, 0x1000)"),
            Expr.Return,
        ),
        'loc_18D1',
    )

    OP_28(0x0073, 0x01, 0x0002)
    OP_28(0x0073, 0x01, 0x0010)

    def _loc_18D1(): pass

    label('loc_18D1')

    If(
        (
            (Expr.Eval, "OP_29(0x0073, 0x01, 0x2000)"),
            Expr.Return,
        ),
        'loc_18E8',
    )

    OP_28(0x0073, 0x01, 0x0002)
    OP_28(0x0073, 0x01, 0x0020)

    def _loc_18E8(): pass

    label('loc_18E8')

    If(
        (
            (Expr.Eval, "OP_29(0x0073, 0x01, 0x4000)"),
            Expr.Return,
        ),
        'loc_18FF',
    )

    OP_28(0x0073, 0x01, 0x0002)
    OP_28(0x0073, 0x01, 0x0040)

    def _loc_18FF(): pass

    label('loc_18FF')

    If(
        (
            (Expr.Eval, "OP_29(0x0073, 0x01, 0x0200)"),
            Expr.Return,
        ),
        'loc_1916',
    )

    OP_28(0x0073, 0x01, 0x0002)
    OP_28(0x0073, 0x01, 0x0080)

    def _loc_1916(): pass

    label('loc_1916')

    OP_A2(0x0008)

    Return()

# id: 0x0003 offset: 0x191A
@scena.Code('func_03_191A')
def func_03_191A():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_1975',
    )

    ChrTalk(
        0x000D,
        (
            '#3440460917V#1P调查有进展了\n',
            '再来报告啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3440460918V#1P哦，那就拜托了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Return()

    def _loc_1975(): pass

    label('loc_1975')

    EventBegin(0x00)
    Fade(1000)
    SetChrPos(0x0101, -62390, 0, -22680, 270)
    SetChrPos(0x0103, -62210, 0, -24020, 315)
    SetChrPos(0x00F8, -61170, 0, -23660, 270)
    SetChrPos(0x00F9, -61070, 0, -22240, 270)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_19EF',
    )

    SetChrPos(0x00F9, -61170, 0, -23660, 270)
    SetChrPos(0x00F8, -61070, 0, -22240, 270)

    def _loc_19EF(): pass

    label('loc_19EF')

    ChrTurnDirection(0x000D, 0x0101, 0)
    OP_6D(-63450, 0, -21840, 0)
    OP_67(0, 6710, -10000, 0)
    OP_6B(2710, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_1A84',
    )

    ChrTalk(
        0x000D,
        (
            '#3440460906V#1P啊，难不成……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3440460907V#1P就来报告了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AE2')

    def _loc_1A84(): pass

    label('loc_1A84')

    ChrTalk(
        0x000D,
        (
            '#3440460908V#1P哦，游击士们。\n',
            '真是辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3440460909V#1P那，我来看看\n',
            '调查的状况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1AE2(): pass

    label('loc_1AE2')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '报告了钓鱼地点的调查状况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0073, 0x01, 0x0004)"),
            Expr.Return,
        ),
        'loc_1B41',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_1B41(): pass

    label('loc_1B41')

    If(
        (
            (Expr.Eval, "OP_29(0x0073, 0x01, 0x0008)"),
            Expr.Return,
        ),
        'loc_1B56',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_1B56(): pass

    label('loc_1B56')

    If(
        (
            (Expr.Eval, "OP_29(0x0073, 0x01, 0x0010)"),
            Expr.Return,
        ),
        'loc_1B6B',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_1B6B(): pass

    label('loc_1B6B')

    If(
        (
            (Expr.Eval, "OP_29(0x0073, 0x01, 0x0020)"),
            Expr.Return,
        ),
        'loc_1B80',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_1B80(): pass

    label('loc_1B80')

    If(
        (
            (Expr.Eval, "OP_29(0x0073, 0x01, 0x0040)"),
            Expr.Return,
        ),
        'loc_1B95',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_1B95(): pass

    label('loc_1B95')

    If(
        (
            (Expr.Eval, "OP_29(0x0073, 0x01, 0x0080)"),
            Expr.Return,
        ),
        'loc_1BAA',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_1BAA(): pass

    label('loc_1BAA')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x5),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_1BBE',
    )

    Call(1, 0x0004)

    Jump('loc_1D86')

    def _loc_1BBE(): pass

    label('loc_1BBE')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x1),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_1D27',
    )

    ChrTalk(
        0x000D,
        (
            '#3440460910V#1P嗯～原来如此……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3440460911V#1P看来调查\n',
            '是有点进展。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3440460912V#1P不过，说实话，\n',
            '希望还能再深入点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010460913V#1007F#2P啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460914V还不够\n',
            '达到标准吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3440460915V#1P嗯，抱歉啦。\n',
            '就是这意思。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3440460916V#1P找找看有没有漏下的，\n',
            '麻烦重新调查一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3440460921V#1P那么，拜托了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0009)

    Jump('loc_1D86')

    def _loc_1D27(): pass

    label('loc_1D27')

    ChrTalk(
        0x000D,
        (
            '#3440460919V#1P怎么，调查\n',
            '完全没有进展嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3440460920V#1P好好调查后\n',
            '再来报告啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0009)

    def _loc_1D86(): pass

    label('loc_1D86')

    EventEnd(0x00)

    Return()

# id: 0x0004 offset: 0x1D89
@scena.Code('func_04_1D89')
def func_04_1D89():
    OP_62(0x000D, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1000)

    OP_63(0x000D)

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1E7D',
    )

    Sleep(500)

    OP_62(0x000D, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000D,
        (
            '#3440460922V#1P唔唔……这、这是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3440460923V#1P没、没想到这种地方\n',
            '居然隐藏着钓鱼场！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3440460924V#1P这可真厉害啊。\n',
            '简直是完美的调查结果啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_2B(0x0073, 0x0002)
    OP_2C(0x0073, 0x07D0)

    Jump('loc_1F59')

    def _loc_1E7D(): pass

    label('loc_1E7D')

    ChrTalk(
        0x000D,
        (
            '#3440460925V#1P唔唔……\n',
            '原来如此，原来如此……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3440460926V#1P虽然不算完美，\n',
            '但我看已经调查得够足了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3440460927V#1P呀～谢谢了。\n',
            '很努力了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3440460928V#1P这样出色的调查结果\n',
            '应该有信心提给总部了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1F59(): pass

    label('loc_1F59')

    ChrTalk(
        0x0101,
        (
            '#0010460929V#1011F#2P这么说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030460930V#020F这样就算完成工作了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0103, 400)

    ChrTalk(
        0x000D,
        (
            '#3440460931V#1P哦，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3440460932V#1P总而言之，请让我\n',
            '说声辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_204A',
    )

    ChrTalk(
        0x0104,
        (
            '#0040460933V#034F呼，哎呀哎呀……\n',
            '总算结束了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2101')

    def _loc_204A(): pass

    label('loc_204A')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2087',
    )

    ChrTalk(
        0x0107,
        (
            '#0070460934V#067F呼……\n',
            '终于结束了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2101')

    def _loc_2087(): pass

    label('loc_2087')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_20CE',
    )

    ChrTalk(
        0x0108,
        (
            '#0080460935V#075F呼，哎呀哎呀……\n',
            '总算结束了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2101')

    def _loc_20CE(): pass

    label('loc_20CE')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2101',
    )

    ChrTalk(
        0x0106,
        (
            '#0050460936V#551F终于结束了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2101(): pass

    label('loc_2101')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2146',
    )

    ChrTalk(
        0x0105,
        (
            '#0060460937V#045F到处跑来跑去\n',
            '的确是有点累啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2210')

    def _loc_2146(): pass

    label('loc_2146')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_218B',
    )

    ChrTalk(
        0x0106,
        (
            '#0050460938V#551F来来回回\n',
            '还真是转了不少路啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2210')

    def _loc_218B(): pass

    label('loc_218B')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_21D0',
    )

    ChrTalk(
        0x0108,
        (
            '#0080460939V#070F唔，这工作\n',
            '比想象的更辛苦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2210')

    def _loc_21D0(): pass

    label('loc_21D0')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2210',
    )

    ChrTalk(
        0x0107,
        (
            '#0070460940V#067F到处跑来跑去\n',
            '真是有点累啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2210(): pass

    label('loc_2210')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_2717',
    )

    ChrTalk(
        0x0101,
        (
            '#0010460941V#1015F#2P嗯，确实\n',
            '够辛苦的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460942V#1001F不过好久没钓鱼了，\n',
            '我觉得还挺开心的呢⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030460943V#021F呵呵，没想到\n',
            '好好放松了一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x000D,
        (
            '#3440460944V#1P哦，那就好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3440460945V#1P委托的报酬\n',
            '已经给协会了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3440460946V#1P机会也难得。\n',
            '顺便也收下这个吧。',
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
            (TxtCtl.Item, ItemTable['钢竿潜水艇']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(ItemTable['钢竿潜水艇'], 1)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010460947V#1004F#2P这、这是……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3440460948V#1P嘿嘿，很棒吧？\n',
            '这是钓大鱼的特制渔竿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3440460949V#1P你一定能好好利用的。\n',
            '代替谢礼送给你吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010460950V#1008F#2P可、可以吗？\n',
            '这么好的东西……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3440460951V#1P完全可以。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3440460952V#1P为了发展和普及钓鱼文化，\n',
            '『钓公师团』可是不惜投资的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3440460953V#1P哦哟，可不能\n',
            '再聊下去了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3440460954V#1P我得带着调查结果\n',
            '回王都才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010460955V#1011F#2P啊，是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_25AB',
    )

    ChrTalk(
        0x0108,
        (
            '#0080460956V#070F那么，路上小心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2654')

    def _loc_25AB(): pass

    label('loc_25AB')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_25E1',
    )

    ChrTalk(
        0x0106,
        (
            '#0050460957V#051F去王都要小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2654')

    def _loc_25E1(): pass

    label('loc_25E1')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2619',
    )

    ChrTalk(
        0x0104,
        (
            '#0040460958V#030F呼，祝一路顺风。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2654')

    def _loc_2619(): pass

    label('loc_2619')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2654',
    )

    ChrTalk(
        0x0107,
        (
            '#0070460959V#560F那个，去王都要小心哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2654(): pass

    label('loc_2654')

    ChrTalk(
        0x000D,
        (
            '#3440460960V#1P那么，就此别过了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3440460961V#1P今天真是多谢你们了。\n',
            '今后也要多努力啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3440460962V#1P有机会要来\n',
            '王都的总部玩哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010460963V#1000F#2P那时就麻烦您了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2C00')

    def _loc_2717(): pass

    label('loc_2717')

    ChrTalk(
        0x0101,
        (
            '#0010460941V#1015F#2P嗯，确实\n',
            '够辛苦的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460965V不过好久没钓鱼了，\n',
            '我觉得还挺开心的呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460966V#1007F不过，现在可不是\n',
            '说这种乐观话的时候……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x000D,
        (
            '#3440460967V#1P是吗，由于这雾，\n',
            '游击士们也很忙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3440460968V#1P这种时候\n',
            '还给你们添麻烦真抱歉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030460969V#020F哪里，别介意。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030460970V认真应对委托\n',
            '是我们的义务。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010460971V#1006F#2P对对，\n',
            '雪拉姐说的对。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460972V多亏了这任务还好好放松了一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3440460973V#1P哦，谢谢。\n',
            '这样说我也安心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3440460974V#1P那，委托的报酬\n',
            '就去协会领吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3440460946V#1P机会也难得。\n',
            '顺便也收下这个吧。',
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
            (TxtCtl.Item, ItemTable['钢竿潜水艇']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(ItemTable['钢竿潜水艇'], 1)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010460947V#1004F#2P这、这是……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3440460948V#1P嘿嘿，很棒吧？\n',
            '这是钓大鱼的特制渔竿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3440460949V#1P你一定能好好利用的。\n',
            '代替谢礼送给你吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010460950V#1008F#2P可、可以吗？\n',
            '这么好的东西……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3440460980V#1P完全可以。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3440460981V#1P为了发展和普及钓鱼文化，\n',
            '『钓公师团』不惜投资的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3440460960V#1P那么，就此别过了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3440460961V#1P今天真是多谢你们了。\n',
            '今后也要多努力啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340248V#1006F#2P嗯，谢谢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3440460985V#1P我也会向女神祈祷\n',
            '让这雾早点散去的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030460986V#020F路上小心哦。\n',
            '那么，再见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_2C00(): pass

    label('loc_2C00')

    @scena.Lambda('lambda_2C06')
    def lambda_2C06():
        ChrTurnDirection(0x00FE, 0x000D, 400)
        Yield()

        Jump('lambda_2C06')

    DispatchAsync2(0x0101, 0x0003, lambda_2C06)

    @scena.Lambda('lambda_2C17')
    def lambda_2C17():
        ChrTurnDirection(0x00FE, 0x000D, 400)
        Yield()

        Jump('lambda_2C17')

    DispatchAsync2(0x0103, 0x0003, lambda_2C17)

    @scena.Lambda('lambda_2C28')
    def lambda_2C28():
        ChrTurnDirection(0x00FE, 0x000D, 400)
        Yield()

        Jump('lambda_2C28')

    DispatchAsync2(0x00F8, 0x0003, lambda_2C28)

    @scena.Lambda('lambda_2C39')
    def lambda_2C39():
        ChrTurnDirection(0x00FE, 0x000D, 400)
        Yield()

        Jump('lambda_2C39')

    DispatchAsync2(0x00F9, 0x0003, lambda_2C39)

    OP_8C(0x000D, 0, 400)
    OP_8E(0x000D, -63600, 0, -21100, 2000, 0x00)
    OP_8E(0x000D, -61970, 0, -20530, 2000, 0x00)
    OP_8C(0x000D, 0, 400)
    OP_6F(0x0001, 0)
    OP_70(0x0001, 0x00000013)
    OP_73(0x0001)
    OP_8E(0x000D, -61970, 0, -18840, 2000, 0x00)
    SetChrFlags(0x000D, 0x0080)
    Sleep(500)

    OP_72(0x0001, 0x0800)
    OP_6F(0x0001, 19)
    OP_70(0x0001, 0x00000000)
    OP_22(0x0007, 0x00, 0x64)
    OP_73(0x0001)
    OP_71(0x0001, 0x0800)
    TerminateThread(0x0101, 0x03)
    TerminateThread(0x0103, 0x03)
    TerminateThread(0x00F8, 0x03)
    TerminateThread(0x00F9, 0x03)
    Sleep(500)

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    OP_22(0x0017, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【寻找钓鱼场】',
            (TxtCtl.SetColor, 0x0),
            '完成了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_28(0x0073, 0x01, 0x0100)
    OP_28(0x0073, 0x04, 0x10)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
