import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T3116_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3116_1 ._SN')

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
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/T3116_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
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

    If(
        (
            (Expr.Eval, "OP_29(0x0022, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_B7',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_B7(): pass

    label('loc_B7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_133',
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
            TXT(0x00, '【◇在上部完成过QST034】\n'),
            TXT(0x01, '【◇在上部没完成过QST034】\n'),
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

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_127'),
        (0x00000001, 'loc_12D'),
        (-1, 'loc_133'),
    )

    def _loc_127(): pass

    label('loc_127')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Jump('loc_133')

    def _loc_12D(): pass

    label('loc_12D')

    ClearScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Jump('loc_133')

    def _loc_133(): pass

    label('loc_133')

    Call(1, 0x0011)

    ChrTalk(
        0x0101,
        (
            '#0010450495V#1011F请问～打扰一下行吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010450496V我们是从\n',
            '协会来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrSetDirection(0x00FE, 90, 400)

    ChrTalk(
        0x00FE,
        (
            '#1890450497V哦，你们来了啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_4E3',
    )

    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '#1890450498V咦、咦……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010450499V#1000F怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890450500V不，你莫非是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890450501V曾经在卢安\n',
            '把试制品送来给我的人？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010450502V#1004F有、有过吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890450503V嗯，应该没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890450504V你和黑发的男孩子\n',
            '一起来过武器店吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010450505V#1015F黑发的男孩子……\n',
            '怎么看都是约修亚吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010450506V嗯～这么说起来\n',
            '可能是有过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_3CD',
    )

    ChrTalk(
        0x0106,
        (
            '#0050450507V#053F反正你要是在意的话\n',
            '等会儿看看手册好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050450508V#050F现在要谈的是这次的工作吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_438')

    def _loc_3CD(): pass

    label('loc_3CD')

    ChrTalk(
        0x0103,
        (
            '#0030450509V#026F反正你要是在意的话\n',
            '等会儿看看手册好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030450510V#020F现在要谈的是这次的工作吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_438(): pass

    label('loc_438')

    ChrTalk(
        0x0101,
        (
            '#0010450511V#1011F啊，是哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890450512V……这么说你们果然是\n',
            '来看告示板的喽？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010450513V#1006F当然是的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010450514V你好像在募集\n',
            '导力枪的测试者呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_538')

    def _loc_4E3(): pass

    label('loc_4E3')

    ChrTalk(
        0x0101,
        (
            '#0010450515V#1006F我们看了告示板。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010450516V你好像在募集\n',
            '导力枪的测试者呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_538(): pass

    label('loc_538')

    ChrTalk(
        0x00FE,
        (
            '#1890450517V嗯，这倒没错……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890450518V不过我其实因为应聘的人\n',
            '太少而感到为难呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890450519V能不能请你们马上\n',
            '听我介绍呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6F8',
    )

    ChrTalk(
        0x0101,
        (
            '#0010450520V#1007F嗯～有可能的话\n',
            '我们也想这样……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010450521V不过最重要的那位\n',
            '枪手现在正好不在。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890450522V哎呀，那不就\n',
            '没法做介绍了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890450523V总之你们先把那个人\n',
            '带来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010450524V#1016F确实没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010450525V那么，我们会再来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x006E, 0x01, 0x8000)
    OP_28(0x006E, 0x01, 0x4000)
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))
    EventEnd(0x00)
    ChrSetDirection(0x00FE, 270, 0)
    ChrClearFlags(0x00FE, 0x0010)

    Return()

    def _loc_6F8(): pass

    label('loc_6F8')

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
        'loc_753',
    )

    OP_28(0x006E, 0x04, 0x04)
    Call(1, 0x0003)

    Return()

    def _loc_753(): pass

    label('loc_753')

    ChrTalk(
        0x0101,
        (
            '#0010450526V#1007F抱歉，现在还不行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890450527V哎呀，是吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010450528V#1006F嗯，有时间我们会来的。\n',
            '到时候就要拜托你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890450529V嗯，那就最好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x006E, 0x01, 0x8000)
    EventEnd(0x00)
    ChrSetDirection(0x00FE, 270, 0)
    ChrClearFlags(0x00FE, 0x0010)

    Return()

# id: 0x0001 offset: 0x815
@scena.Code('func_01_815')
def func_01_815():
    ChrTalk(
        0x00FE,
        (
            '#1890450618V总之你们先把那个枪手\n',
            '带来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890450619V不然我没办法\n',
            '做介绍。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Return()

# id: 0x0002 offset: 0x86C
@scena.Code('func_02_86C')
def func_02_86C():
    EventBegin(0x00)
    Call(1, 0x0011)

    If(
        (
            (Expr.Eval, "OP_29(0x006E, 0x01, 0x4000)"),
            Expr.Return,
        ),
        'loc_A33',
    )

    ChrSetDirection(0x00FE, 90, 400)

    ChrTalk(
        0x00FE,
        (
            '#1890450530V哟，是你们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890450531V你们把那个枪手\n',
            '带来了吗？',
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
        'loc_966',
    )

    ChrTalk(
        0x0101,
        (
            '#0010450532V#1006F嗯，就在这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040450533V#035F呵呵，让你久等了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890450534V好，那么可以谈\n',
            '测试的问题了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x006E, 0x02, 0x4000)

    Jump('loc_A30')

    def _loc_966(): pass

    label('loc_966')

    ChrTalk(
        0x0101,
        (
            '#0010450535V#1003F不，抱歉。\n',
            '还没带来哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890450523V总之你们先把那个人\n',
            '带来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890450537V不然我没办法\n',
            '做介绍。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010450538V#1000F明白了。\n',
            '我们会再来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x006E, 0x01, 0x4000)
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))
    EventEnd(0x00)
    ChrSetDirection(0x00FE, 270, 0)
    ChrClearFlags(0x00FE, 0x0010)

    Return()

    def _loc_A30(): pass

    label('loc_A30')

    Jump('loc_BC5')

    def _loc_A33(): pass

    label('loc_A33')

    ChrSetDirection(0x00FE, 90, 400)

    ChrTalk(
        0x00FE,
        (
            '#1890450539V啊，是你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890450540V关于导力枪的测试，\n',
            '这次可以听我说了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_BC5',
    )

    ChrTalk(
        0x0101,
        (
            '#0010450520V#1007F嗯～有可能的话\n',
            '我们也想这样……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010450521V不过最重要的那位\n',
            '枪手现在正好不在。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890450522V哎呀，那不就\n',
            '没法做介绍了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890450523V总之你们先把那个人\n',
            '带来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010450524V#1016F确实没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010450525V那么，我们会再来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x006E, 0x01, 0x8000)
    OP_28(0x006E, 0x01, 0x4000)
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))
    EventEnd(0x00)
    ChrSetDirection(0x00FE, 270, 0)
    ChrClearFlags(0x00FE, 0x0010)

    Return()

    def _loc_BC5(): pass

    label('loc_BC5')

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
        'loc_C20',
    )

    OP_28(0x006E, 0x04, 0x04)
    Call(1, 0x0003)

    Return()

    def _loc_C20(): pass

    label('loc_C20')

    ChrTalk(
        0x0101,
        (
            '#0010450547V#1007F不，抱歉。\n',
            '还有点不方便。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890450548V哎呀，怎么这样～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010450549V#1016F真对不起。\n',
            '有时间了我会再来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890450550V嗯，拜托了。\n',
            '我在这里等着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x006E, 0x01, 0x8000)
    EventEnd(0x00)
    ChrSetDirection(0x00FE, 270, 0)

    Return()

# id: 0x0003 offset: 0xCE7
@scena.Code('func_03_CE7')
def func_03_CE7():
    ChrTalk(
        0x0101,
        (
            '#0010450551V#1000F嗯，拜托你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890450552V那么，马上开始\n',
            '做个说明吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890450553V你们知道，\n',
            '委托内容是导力枪的测试。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890450554V我希望你们通过实战来检测\n',
            '它作为武器的可靠性。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010450555V#1011F可靠性检测？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890450556V最简单地说就是\n',
            '测试耐久度。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890450557V任何机械肯定都有只在\n',
            '实际使用中才会暴露的缺陷。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890450558V很多故障原因都是在\n',
            '开发过程中想象不到的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890450559V找出这种隐藏的弱点，\n',
            '并且提高其作为武器的可靠性。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890450560V这就是测试的目的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040450561V#030F是这样啊，主旨我已经明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040450562V就是说，用专业词汇来描述的话\n',
            '就是『实战检测』喽。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0104, 400)

    ChrTalk(
        0x00FE,
        (
            '#1890450563V嗯，一点没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890450564V对了，你就是\n',
            '帮忙测试的射手吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040450565V#031F嗯，让我来打个招呼。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040450566V漂泊的诗人兼演奏家，\n',
            '奥利维尔·朗海姆是也。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '#1890450567V演、演奏家……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010450568V#1001F啊，没事的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010450569V这家伙虽然看上去怪怪的，\n',
            '不过只有枪的技术#5S这一点#2S是可信赖的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0104, 0x0101, 400)

    ChrTalk(
        0x0104,
        (
            '#0040450570V#033F咦，是不是我多心了？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040450571V好像你在发言中\n',
            '特别强调了某一部分……',
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
        'loc_1193',
    )

    ChrTalk(
        0x0108,
        (
            '#0080450572V#071F哈哈，这有什么关系呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080450573V你的能力\n',
            '已经得到了大家的认可。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_125F')

    def _loc_1193(): pass

    label('loc_1193')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_11FD',
    )

    ChrTalk(
        0x0106,
        (
            '#0050450574V#051F好了，这又有什么关系呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050450575V你小子的能力\n',
            '已经得到了大家的认可。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_125F')

    def _loc_11FD(): pass

    label('loc_11FD')

    ChrTalk(
        0x0103,
        (
            '#0030450576V#021F哎呀，这又有什么关系呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030450577V奥利维尔的能力\n',
            '已经得到了大家的认可。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_125F(): pass

    label('loc_125F')

    ChrTalk(
        0x00FE,
        (
            '#1890450578V是、是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890450579V好了，既然这样，\n',
            '就拜托你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0104, 0x00FE, 400)

    ChrTalk(
        0x0104,
        (
            '#0040450580V#031F哈哈哈。\n',
            '你就放一百个心吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890450581V（真、真的没问题吗……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890450582V算、算了。\n',
            '总之我先把枪给你。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['零式导力枪α']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(ItemTable['零式导力枪α'], 1)
    OP_59()
    OP_0D()
    Fade(500)
    ChrSetChipByIndex(0x0104, 3)
    ChrSetSubChip(0x0104, 0)
    OP_0D()
    Call(1, 0x0012)

    ChrTalk(
        0x00FE,
        (
            '#1890450583V那就是要测试的枪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890450584V作为你们赶来的谢礼，\n',
            '就免费送给你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040450585V#035F哟，这可太感谢了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040450586V#032F不过话说回来，这把枪……\n',
            '构造看上去还真不习惯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890450587V哈哈，那是当然的。\n',
            '如果你以前见过我倒不好办了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890450588V因为这把枪的驱动方式\n',
            '是我们发明的新技术。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890450589V怎么样，会用吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0104, 0x01, 0x01, 0x0010)

    ChrTalk(
        0x0104,
        (
            '#0040450590V#035F呼，当然。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040450591V我和这把枪一定能\n',
            '发出美妙的共鸣。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890450592V多、多谢夸奖……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0008, 400)

    ChrTalk(
        0x0101,
        (
            '#0010450593V#1007F好了，先不管这些，\n',
            '请你继续介绍下去。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010450594V#1002F我们还不知道\n',
            '具体要做些什么呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0104, 0x0001)
    Fade(500)
    ChrSetChipByIndex(0x0104, 65535)
    ChrSetSubChip(0x0104, 0)
    OP_0D()

    ChrTalk(
        0x0104,
        (
            '#0040450595V#033F哦！确实如此。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040450596V来吧，快点介绍。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(1, 0x0013)

    ChrTalk(
        0x00FE,
        (
            '#1890450597V大、大致上和你\n',
            '前面自己说过的一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890450598V总之，你只要装备着那把枪\n',
            '去战斗就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890450599V测试场所就选在附近的\n',
            '托兰特平原道吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890450600V在那里就算碰上什么麻烦\n',
            '也不会引发严重的事态。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010450601V#1006F明白了。\n',
            '托兰特平原道是吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890450602V希望你们最起码\n',
            '能够进行１０次左右的战斗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890450603V当然这是计算\n',
            '完成作战次数的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890450604V老是撤退、撤退的，\n',
            '就不能算是战斗测试了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040450605V#030F好，那么确认一下……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040450606V装备着这把枪\n',
            '前往托兰特平原道……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040450607V在那里进行１０次\n',
            '左右的战斗就行了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_18F3',
    )

    ChrTalk(
        0x0106,
        (
            '#0050450608V#050F那么在完成之后\n',
            '再回来这里报告。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050450609V……就没问题了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1949')

    def _loc_18F3(): pass

    label('loc_18F3')

    ChrTalk(
        0x0103,
        (
            '#0030450610V#020F那么在完成之后\n',
            '再回来这里报告。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030450611V……就没问题了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1949(): pass

    label('loc_1949')

    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#1890450612V嗯，应该没问题了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890450613V如果已经没有疑问的话\n',
            '接下来就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010450614V#1006F没什么疑问了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010450615V那我们走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0104, 400)

    ChrTalk(
        0x00FE,
        (
            '#1890450616V奥利维尔先生……\n',
            '我可相信着你哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040450617V#031F呵呵，我不会辜负你的期待的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    OP_CE(
        0x00,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_28(0x006E, 0x04, 0x08)
    OP_28(0x006E, 0x01, 0x0001)
    OP_28(0x006E, 0x01, 0x0002)
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))
    ChrClearFlags(0x00FE, 0x0010)
    EventEnd(0x00)
    ChrSetDirection(0x00FE, 270, 0)

    Return()

# id: 0x0004 offset: 0x1A88
@scena.Code('func_04_1A88')
def func_04_1A88():
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
        1,
        (
            TXT(0x00, '【报告】\n'),
            TXT(0x01, '【确认工作内容】\n'),
            TXT(0x02, '【放弃】\n'),
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
        'loc_1AF1',
    )

    Call(1, 0x0005)

    Return()

    def _loc_1AF1(): pass

    label('loc_1AF1')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1C48',
    )

    ChrTalk(
        0x00FE,
        (
            '#1890450620V我想拜托的\n',
            '是『零式导力枪』的测试。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890450621V希望你们装备着那把枪\n',
            '最少进行１０次\n',
            '左右的战斗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890450622V进行试验的地方就选在\n',
            '托兰特平原道吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890450623V这一带就那里\n',
            '是相对安全的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890450624V如果达到了目标战斗次数\n',
            '就再来这里报告吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890450625V工作内容的确认\n',
            '差不多就是这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C77')

    def _loc_1C48(): pass

    label('loc_1C48')

    ChrTalk(
        0x00FE,
        (
            '#1890450626V那么，测试\n',
            '你们也要帮帮忙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C77(): pass

    label('loc_1C77')

    Return()

# id: 0x0005 offset: 0x1C78
@scena.Code('func_05_1C78')
def func_05_1C78():
    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1D1C',
    )

    ChrTalk(
        0x00FE,
        (
            '#1890450629V咦，奥利维尔先生\n',
            '怎么不见了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890450627V关键的射手不在的话\n',
            '就称不上报告了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890450628V不好意思，请你们下次再来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    Return()

    def _loc_1D1C(): pass

    label('loc_1D1C')

    If(
        (
            (Expr.PushVar, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_1DB8',
    )

    ChrTalk(
        0x00FE,
        (
            '#1890450632V咦，是来报告的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010450633V#1000F不……\n',
            '我们现在才刚要去测试。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890450634V原来是这样啊。\n',
            '那么，请多关照了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    Return()

    def _loc_1DB8(): pass

    label('loc_1DB8')

    EventBegin(0x00)
    Call(1, 0x0011)
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#1890450635V哟，是来报告的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010450636V#1000F嗯，我们战斗过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040450637V#030F那么就让我把之前的\n',
            '经过报告一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_40(0x005B, 0x00)"),
            (Expr.PushLong, 0x1),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1F26',
    )

    ChrTalk(
        0x00FE,
        (
            '#1890450638V嗯，这个倒是好事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890450639V不过关键的『零式导力枪α』\n',
            '你们好像没带着吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890450640V没有那个的话\n',
            '就无法确认测试结果了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890450628V不好意思，请你们下次再来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))
    EventEnd(0x00)

    Return()

    def _loc_1F26(): pass

    label('loc_1F26')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '向加鲁诺介绍了\n',
            '迄今为止的战斗测试状况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    If(
        (
            (Expr.PushVar, 0x0),
            (Expr.PushLong, 0xA),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_1F7B',
    )

    Call(1, 0x0006)

    Return()

    def _loc_1F7B(): pass

    label('loc_1F7B')

    Call(1, 0x0007)

    Return()

# id: 0x0006 offset: 0x1F80
@scena.Code('func_06_1F80')
def func_06_1F80():
    ChrTalk(
        0x00FE,
        (
            '#1890450644V嗯～原来如此。\n',
            '似乎也都很努力……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890450642V很遗憾，战斗次数\n',
            '比预定的还少呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010450646V#1008F啊，果然是这样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890450647V嗯，你们要是能\n',
            '再多战斗几次就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890450648V那么下次再来报告吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040450649V#030F呵呵，下次再来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))
    EventEnd(0x00)

    Return()

# id: 0x0007 offset: 0x2096
@scena.Code('func_07_2096')
def func_07_2096():
    ChrTurnDirection(0x00FE, 0x0104, 400)

    If(
        (
            (Expr.PushVar, 0x0),
            (Expr.PushLong, 0xF),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_2138',
    )

    ChrTalk(
        0x00FE,
        (
            '#1890450650V嗯，看来战斗得\n',
            '已经很充分了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890450651V呀～不管怎样，\n',
            '你们很努力呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010450652V#1001F嘿嘿，谢谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_2B(0x006E, 0x0001)
    OP_2C(0x006E, 0x03E8)

    Jump('loc_220A')

    def _loc_2138(): pass

    label('loc_2138')

    ChrTalk(
        0x00FE,
        (
            '#1890450650V嗯，看来战斗得\n',
            '已经很充分了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890450654V好，测试可以算是完成了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010450655V#1007F啊，终于结束了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010450656V比我想象的要累得多～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#1890450657V哈哈，你们好像很疲劳。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_220A(): pass

    label('loc_220A')

    ChrTalk(
        0x0104,
        (
            '#0040450658V#035F呵呵，作为一名协力人员，\n',
            '做这点事算不了什么。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0104, 400)

    ChrTalk(
        0x00FE,
        (
            '#1890450659V对了，奥利维尔先生。\n',
            '测试下来有什么问题吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040450660V#035F不，完全没有问题。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040450661V稳定的弹道、\n',
            '绝妙的重心平衡……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040450662V#030F是一件很让人期待其量产化的上品。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890450663V呼～太好了～\n',
            '听到这些我就放心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890450664V好，总算离产品化\n',
            '只剩一步之遥了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010450665V#1000F还没有产品化吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010450666V以我这个外行的眼光来看\n',
            '这已经像是完成品了',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#1890450667V不，还有一点工序。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890450668V接下来就要和生产方\n',
            '确定细节部分了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890450669V不过能这么说也是\n',
            '多亏了这次测试。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890450670V对接下来的研究也会\n',
            '起促进作用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_24DB',
    )

    ChrTalk(
        0x0106,
        (
            '#0050450671V#051F嗯，希望你们再接再厉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2502')

    def _loc_24DB(): pass

    label('loc_24DB')

    ChrTalk(
        0x0103,
        (
            '#0030450672V#020F请你们再接再厉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2502(): pass

    label('loc_2502')

    ChrTalk(
        0x0104,
        (
            '#0040450673V#031F新型导力枪……\n',
            '我会大为期待的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0104, 400)

    ChrTalk(
        0x00FE,
        (
            '#1890450674V嗯，你们就瞧好吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890450675V啊，对了……\n',
            '请先别走。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010450676V#1011F咦，还有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#1890450677V嗯，希望你们收下这个。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['命中３']),
            (TxtCtl.SetColor, 0x0),
            '结晶回路。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(ItemTable['命中３'], 1)
    Sleep(500)

    ChrTalk(
        0x00FE,
        (
            '#1890450678V米拉方面的报酬很少，\n',
            '我挺在意的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890450679V嘿嘿，就算是补偿吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890450680V而且也算是件有用的东西，\n',
            '请收下来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010450681V#1001F啊，嗯，谢谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040450682V#031F呵呵，我会珍惜它的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890450683V那以后有什么事的话\n',
            '我还会再拜托你们的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890450684V你们也当心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010450685V#1018F那么再见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x006E, 0x04, 0x10)
    OP_28(0x006E, 0x01, 0x0080)
    PlaySE(23, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【新型导力枪测试】',
            (TxtCtl.SetColor, 0x0),
            '完成了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))
    EventEnd(0x00)

    Return()

# id: 0x0008 offset: 0x27FB
@scena.Code('func_08_27FB')
def func_08_27FB():
    ChrTalk(
        0x00FE,
        (
            '#1890450686V那么，请多关照了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890450687V尤其是奥利维尔先生，\n',
            '特别需要拜托你了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Return()

# id: 0x0009 offset: 0x2859
@scena.Code('func_09_2859')
def func_09_2859():
    ChrTalk(
        0x00FE,
        (
            '#1890450688V各位，今天真是谢谢了，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890450689V我也会努力做出\n',
            '了不起的导力枪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890450690V那么再见了，\n',
            '有事我会再找你们的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Return()

# id: 0x000A offset: 0x28E6
@scena.Code('func_0A_28E6')
def func_0A_28E6():
    ChrTalk(
        0x00FE,
        (
            '#1890450627V关键的射手不在的话\n',
            '就称不上报告了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890450628V不好意思，请你们下次再来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Return()

# id: 0x000B offset: 0x294A
@scena.Code('func_0B_294A')
def func_0B_294A():
    ChrTalk(
        0x00FE,
        (
            '#1890450642V很遗憾，战斗次数\n',
            '比预定的还少呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890450643V继续战斗几次\n',
            '以后再来报告吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Return()

# id: 0x000C offset: 0x29AD
@scena.Code('func_0C_29AD')
def func_0C_29AD():
    If(
        (
            (Expr.PushValueByIndex, 0x13),
            (Expr.PushLong, 0x382),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_29BA',
    )

    Return()

    def _loc_29BA(): pass

    label('loc_29BA')

    ExecExpressionWithReg(
        0x0006,
        (
            (Expr.PushLong, 0xE4E5A8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0007,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.Eval, "OP_29(0x006F, 0x01, 0x0008)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2A4E',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x154),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0004,
        (
            (Expr.PushReg, 0x3),
            (Expr.PushReg, 0x2),
            Expr.Sub,
            (Expr.PushReg, 0x3),
            (Expr.PushReg, 0x2),
            Expr.Sub,
            Expr.Mul,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x3BCE),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.GetChrWork, 0x0, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0005,
        (
            (Expr.PushReg, 0x3),
            (Expr.PushReg, 0x2),
            Expr.Sub,
            (Expr.PushReg, 0x3),
            (Expr.PushReg, 0x2),
            Expr.Sub,
            Expr.Mul,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x6),
            (Expr.PushReg, 0x4),
            (Expr.PushReg, 0x5),
            Expr.Add,
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_2A4E',
    )

    ExecExpressionWithReg(
        0x0006,
        (
            (Expr.PushReg, 0x4),
            (Expr.PushReg, 0x5),
            Expr.Add,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0007,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2A4E(): pass

    label('loc_2A4E')

    If(
        (
            (Expr.Eval, "OP_29(0x006F, 0x01, 0x0010)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2ACD',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x10FE),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0004,
        (
            (Expr.PushReg, 0x3),
            (Expr.PushReg, 0x2),
            Expr.Sub,
            (Expr.PushReg, 0x3),
            (Expr.PushReg, 0x2),
            Expr.Sub,
            Expr.Mul,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x866),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.GetChrWork, 0x0, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0005,
        (
            (Expr.PushReg, 0x3),
            (Expr.PushReg, 0x2),
            Expr.Sub,
            (Expr.PushReg, 0x3),
            (Expr.PushReg, 0x2),
            Expr.Sub,
            Expr.Mul,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x6),
            (Expr.PushReg, 0x4),
            (Expr.PushReg, 0x5),
            Expr.Add,
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_2ACD',
    )

    ExecExpressionWithReg(
        0x0006,
        (
            (Expr.PushReg, 0x4),
            (Expr.PushReg, 0x5),
            Expr.Add,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0007,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2ACD(): pass

    label('loc_2ACD')

    If(
        (
            (Expr.Eval, "OP_29(0x006F, 0x01, 0x0020)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2B4C',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x11F8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0004,
        (
            (Expr.PushReg, 0x3),
            (Expr.PushReg, 0x2),
            Expr.Sub,
            (Expr.PushReg, 0x3),
            (Expr.PushReg, 0x2),
            Expr.Sub,
            Expr.Mul,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x3C3C),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.GetChrWork, 0x0, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0005,
        (
            (Expr.PushReg, 0x3),
            (Expr.PushReg, 0x2),
            Expr.Sub,
            (Expr.PushReg, 0x3),
            (Expr.PushReg, 0x2),
            Expr.Sub,
            Expr.Mul,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x6),
            (Expr.PushReg, 0x4),
            (Expr.PushReg, 0x5),
            Expr.Add,
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_2B4C',
    )

    ExecExpressionWithReg(
        0x0006,
        (
            (Expr.PushReg, 0x4),
            (Expr.PushReg, 0x5),
            Expr.Add,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0007,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2B4C(): pass

    label('loc_2B4C')

    MapSetFlags(0x00000080)
    OP_C0(0x01, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)
    Sleep(30)

    LoadEffect(0x00, 'map\\\\mp108_00.eff')
    PlayEffect(0x00, 0x00, 0x0000, 0, 0, 0, 0, 0, 0, 1300, 1300, 1300, 0x00FF, 0, 0, 0, 0)
    Sleep(600)

    If(
        (
            (Expr.PushReg, 0x6),
            (Expr.PushLong, 0xF4240),
            Expr.Leq,
            (Expr.PushReg, 0x7),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2C4C',
    )

    EventBegin(0x01)
    OP_62(0x0000, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(1000)

    OP_63(0x0000)
    OP_62(0x0000, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    OP_63(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x7),
            Expr.Return,
        ),
        (0x00000001, 'loc_2C32'),
        (0x00000002, 'loc_2C39'),
        (0x00000003, 'loc_2C40'),
        (-1, 'loc_2C47'),
    )

    def _loc_2C32(): pass

    label('loc_2C32')

    OP_65(0x00, 0x0001)

    Jump('loc_2C47')

    def _loc_2C39(): pass

    label('loc_2C39')

    OP_65(0x01, 0x0001)

    Jump('loc_2C47')

    def _loc_2C40(): pass

    label('loc_2C40')

    OP_65(0x02, 0x0001)

    Jump('loc_2C47')

    def _loc_2C47(): pass

    label('loc_2C47')

    EventEnd(0x01)

    Jump('loc_2D22')

    def _loc_2C4C(): pass

    label('loc_2C4C')

    If(
        (
            (Expr.PushReg, 0x6),
            (Expr.PushLong, 0x4C4B40),
            Expr.Leq,
            Expr.Return,
        ),
        'loc_2C9C',
    )

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '这附近有反应！',
            TxtCtl.Enter,
        ),
    )

    PlaySE(170, 0x00, 0x64)
    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    Jump('loc_2D22')

    def _loc_2C9C(): pass

    label('loc_2C9C')

    If(
        (
            (Expr.PushReg, 0x6),
            (Expr.PushLong, 0x989680),
            Expr.Leq,
            Expr.Return,
        ),
        'loc_2CE8',
    )

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '附近有反应',
            TxtCtl.Enter,
        ),
    )

    PlaySE(170, 0x00, 0x64)
    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    Jump('loc_2D22')

    def _loc_2CE8(): pass

    label('loc_2CE8')

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '没有反应',
            TxtCtl.Enter,
        ),
    )

    PlaySE(171, 0x00, 0x64)
    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    def _loc_2D22(): pass

    label('loc_2D22')

    OP_0D()
    MapClearFlags(0x00000080)

    Return()

# id: 0x000D offset: 0x2D29
@scena.Code('func_0D_2D29')
def func_0D_2D29():
    EventBegin(0x01)
    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['导力器零件']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(ItemTable['导力器零件'], 1)
    OP_28(0x006F, 0x01, 0x0008)
    OP_64(0x00, 0x0001)
    EventEnd(0x01)

    Return()

# id: 0x000E offset: 0x2D7C
@scena.Code('func_0E_2D7C')
def func_0E_2D7C():
    EventBegin(0x01)
    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['导力器零件']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(ItemTable['导力器零件'], 1)
    OP_28(0x006F, 0x01, 0x0010)
    OP_64(0x01, 0x0001)
    EventEnd(0x01)

    Return()

# id: 0x000F offset: 0x2DCF
@scena.Code('func_0F_2DCF')
def func_0F_2DCF():
    EventBegin(0x01)
    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['导力器零件']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(ItemTable['导力器零件'], 1)
    OP_28(0x006F, 0x01, 0x0020)
    OP_64(0x02, 0x0001)
    EventEnd(0x01)

    Return()

# id: 0x0010 offset: 0x2E22
@scena.Code('func_10_2E22')
def func_10_2E22():
    ChrSetChipByIndex(0x0104, 3)
    OP_99(0x0104, 0x00, 0x0E, 2000)
    WaitForThreadExit(0x0104, 0x0000)
    ChrSetSubChip(0x0104, 14)

    Return()

# id: 0x0011 offset: 0x2E3B
@scena.Code('func_11_2E3B')
def func_11_2E3B():
    Fade(1000)
    ChrSetPos(0x0008, -2000, 0, 3410, 270)
    ChrSetPos(0x0101, -420, 0, 3410, 270)

    If(
        (
            (Expr.Eval, "OP_CB(0xF7)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2EA5',
    )

    ChrSetPos(0x00F7, -490, 0, 5020, 245)
    ChrSetPos(0x00F8, 590, 0, 2940, 266)
    ChrSetPos(0x00F9, 950, 0, 4870, 240)

    Jump('loc_2F1B')

    def _loc_2EA5(): pass

    label('loc_2EA5')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2EE8',
    )

    ChrSetPos(0x00F8, -490, 0, 5020, 245)
    ChrSetPos(0x00F7, 590, 0, 2940, 266)
    ChrSetPos(0x00F9, 950, 0, 4870, 240)

    Jump('loc_2F1B')

    def _loc_2EE8(): pass

    label('loc_2EE8')

    ChrSetPos(0x00F9, -490, 0, 5020, 245)
    ChrSetPos(0x00F7, 590, 0, 2940, 266)
    ChrSetPos(0x00F8, 950, 0, 4870, 240)

    def _loc_2F1B(): pass

    label('loc_2F1B')

    CameraMove(-790, 0, 3710, 0)
    OP_67(0, 4800, -10000, 0)
    CameraSetDistance(2900, 0)
    OP_6C(57000, 0)
    OP_6E(280, 0)
    OP_0D()

    Return()

# id: 0x0012 offset: 0x2F5A
@scena.Code('func_12_2F5A')
def func_12_2F5A():
    @scena.Lambda('lambda_2F60')
    def lambda_2F60():
        ChrTurnDirection(0x0101, 0x0104, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2F60)

    If(
        (
            (Expr.Eval, "OP_CB(0xF7)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2F94',
    )

    @scena.Lambda('lambda_2F7B')
    def lambda_2F7B():
        ChrSetDirection(0x00F8, 315, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_2F7B)

    @scena.Lambda('lambda_2F89')
    def lambda_2F89():
        ChrTurnDirection(0x00F9, 0x0104, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_2F89)

    Jump('loc_2FDC')

    def _loc_2F94(): pass

    label('loc_2F94')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2FC0',
    )

    @scena.Lambda('lambda_2FA7')
    def lambda_2FA7():
        ChrSetDirection(0x00F7, 315, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_2FA7)

    @scena.Lambda('lambda_2FB5')
    def lambda_2FB5():
        ChrTurnDirection(0x00F9, 0x0104, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_2FB5)

    Jump('loc_2FDC')

    def _loc_2FC0(): pass

    label('loc_2FC0')

    @scena.Lambda('lambda_2FC6')
    def lambda_2FC6():
        ChrSetDirection(0x00F7, 315, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_2FC6)

    @scena.Lambda('lambda_2FD4')
    def lambda_2FD4():
        ChrTurnDirection(0x00F8, 0x0104, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_2FD4)

    def _loc_2FDC(): pass

    label('loc_2FDC')

    WaitForThreadExit(0x0101, 0x0001)

    Return()

# id: 0x0013 offset: 0x2FE2
@scena.Code('func_13_2FE2')
def func_13_2FE2():
    If(
        (
            (Expr.Eval, "OP_CB(0xF7)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_301C',
    )

    @scena.Lambda('lambda_2FF5')
    def lambda_2FF5():
        ChrSetDirection(0x00F7, 245, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_2FF5)

    @scena.Lambda('lambda_3003')
    def lambda_3003():
        ChrSetDirection(0x00F8, 266, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_3003)

    @scena.Lambda('lambda_3011')
    def lambda_3011():
        ChrSetDirection(0x00F9, 240, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_3011)

    Jump('loc_3080')

    def _loc_301C(): pass

    label('loc_301C')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3056',
    )

    @scena.Lambda('lambda_302F')
    def lambda_302F():
        ChrSetDirection(0x00F8, 245, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_302F)

    @scena.Lambda('lambda_303D')
    def lambda_303D():
        ChrSetDirection(0x00F7, 266, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_303D)

    @scena.Lambda('lambda_304B')
    def lambda_304B():
        ChrSetDirection(0x00F9, 240, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_304B)

    Jump('loc_3080')

    def _loc_3056(): pass

    label('loc_3056')

    @scena.Lambda('lambda_305C')
    def lambda_305C():
        ChrSetDirection(0x00F9, 245, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_305C)

    @scena.Lambda('lambda_306A')
    def lambda_306A():
        ChrSetDirection(0x00F7, 266, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_306A)

    @scena.Lambda('lambda_3078')
    def lambda_3078():
        ChrSetDirection(0x00F8, 240, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_3078)

    def _loc_3080(): pass

    label('loc_3080')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
