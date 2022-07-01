import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T3221_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3221_1 ._SN')

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
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/T3221_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x35CC
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
    Fade(1000)
    SetChrPos(0x0008, 2590, 250, 5360, 180)
    SetChrPos(0x0101, 2000, 250, 3320, 0)
    SetChrPos(0x0107, 3030, 250, 2920, 0)
    SetChrPos(0x00F7, 1910, 250, 1820, 0)
    SetChrPos(0x00F9, 3060, 250, 1500, 0)
    OP_6D(1350, 250, 4070, 0)
    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0290, 2, 0x1482)),
            Expr.Return,
        ),
        'loc_2F1',
    )

    ChrTalk(
        0x0008,
        (
            '#0570450983V#683F哎呀，你们几个。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570450984V今天又凑在一起\n',
            '怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010450985V#1001F嗯，当然是\n',
            '来投宿的！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010450986V#1007F……真想早点有机会\n',
            '能这么说啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_23C',
    )

    ChrTalk(
        0x0106,
        (
            '#0050450987V#050F#1P很遗憾，今天也是为了工作。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050450988V我们看了告示板，\n',
            '这里好像发生什么问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A7')

    def _loc_23C(): pass

    label('loc_23C')

    ChrTalk(
        0x0103,
        (
            '#0030450989V#020F#1P很遗憾，今天也是为了工作。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030450990V我们看了告示板，\n',
            '这里好像发生什么问题了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2A7(): pass

    label('loc_2A7')

    ChrTalk(
        0x0008,
        (
            '#0570450991V#682F告示板……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570450992V就是说我联络协会的事吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9E2')

    def _loc_2F1(): pass

    label('loc_2F1')

    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    OP_63(0x0008)

    ChrTalk(
        0x0008,
        (
            '#0570450993V#680F哟，你们来了啊。\n',
            '咦，提妲也在。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070450994V#061F您好，婆婆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010450995V#1001F#1P麻绪婆婆，好久不见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0570450996V#681F嗯，艾丝蒂尔，好久不见。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570230859V与以前来的时候相比\n',
            '一下子变得更像大人了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010450998V#1008F#1P嘿嘿……是吗。',
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
        'loc_8B7',
    )

    ChrTalk(
        0x0104,
        (
            '#0040450999V#035F老板娘，上回有劳你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0104, 400)

    ChrTalk(
        0x0008,
        (
            '#0570451000V#683F哎呀，我还以为是谁呢，\n',
            '这不是奥利维尔吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570451001V怎么你也来了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0107, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    @scena.Lambda('lambda_04DF')
    def lambda_04DF():
        ChrTurnDirection(0x0107, 0x0104, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_04DF)

    Sleep(100)

    @scena.Lambda('lambda_04F2')
    def lambda_04F2():
        ChrTurnDirection(0x0101, 0x0104, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_04F2)

    Sleep(200)

    ChrTurnDirection(0x00F7, 0x0104, 400)

    ChrTalk(
        0x0107,
        (
            '#0070451002V#064F啊……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040451003V#031F呵呵，这里头有些缘故。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040231391V现在我作为协力人员\n',
            '和他们一起行动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010451005V#1004F#1P你、你们认识？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#0570231393V#680F嗯，不久前他\n',
            '在这里住宿过。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570231394V#685F我还是第一次看到有客人\n',
            '在澡堂里弹琴呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(100)

    OP_62(0x0107, 0x00000000, 1700, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(100)

    OP_62(0x00F7, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_6B1',
    )

    ChrTalk(
        0x0106,
        (
            '#0050451008V#551F#1P无论到哪里\n',
            '都会做同样的事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6EC')

    def _loc_6B1(): pass

    label('loc_6B1')

    ChrTalk(
        0x0103,
        (
            '#0030451009V#025F#1P唉，无论到哪里\n',
            '都会做同样的事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6EC(): pass

    label('loc_6EC')

    ChrTalk(
        0x0104,
        (
            '#0040451010V#031F这是我们艺术家的宿命。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040231398V对为美的女神服务的人来说\n',
            '时间和空间根本就是无关紧要的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010451012V#1007F#1P就算这样全裸\n',
            '状态下弹琴也太那个什么了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010231400V#1013F啊……不好……\n',
            '在脑中想象了一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0107, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x0107,
        (
            '#0070451014V#562F姐、姐姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0570231402V#680F反正无论如何，\n',
            '你能喜欢我很高兴。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570231403V这样的话大家\n',
            '一起住下来怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_087A')
    def lambda_087A():
        ChrTurnDirection(0x00F7, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_087A)

    Sleep(100)

    @scena.Lambda('lambda_088D')
    def lambda_088D():
        ChrTurnDirection(0x0101, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_088D)

    Sleep(150)

    @scena.Lambda('lambda_08A0')
    def lambda_08A0():
        ChrTurnDirection(0x0104, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_08A0)

    Sleep(50)

    ChrTurnDirection(0x0107, 0x0008, 400)

    Jump('loc_916')

    def _loc_8B7(): pass

    label('loc_8B7')

    ChrTalk(
        0x0008,
        (
            '#0570231404V#680F话虽这么说，难得\n',
            '大家都来了',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570231405V既然这样好好歇息\n',
            '一晚上怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_916(): pass

    label('loc_916')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_95D',
    )

    ChrTalk(
        0x0106,
        (
            '#0050451019V#050F#1P我倒是想这样，\n',
            '不过不是还有工作吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_99A')

    def _loc_95D(): pass

    label('loc_95D')

    ChrTalk(
        0x0103,
        (
            '#0030451020V#020F#1P我倒是想这样，\n',
            '不过不是还有工作吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_99A(): pass

    label('loc_99A')

    ChrTalk(
        0x0008,
        (
            '#0570451021V#680F工作……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570450992V就是说我联络协会的事吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1482)
    def _loc_9E2(): pass

    label('loc_9E2')

    ChrTalk(
        0x0101,
        (
            '#0010451023V#1002F#1P嗯，就是那个。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010451024V好像是说有\n',
            '偷窥犯出现什么的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0570451025V#682F嗯，很有可能有。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570451026V如果你们方便的话，\n',
            '希望你们马上展开调查……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570451027V你们有时间吗？',
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
        'loc_B42',
    )

    ChrTalk(
        0x0101,
        (
            '#0010451028V#1006F#1P嗯，没问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0070, 0x04, 0x08)
    OP_28(0x0070, 0x01, 0x0001)
    OP_28(0x0070, 0x01, 0x0002)
    Call(1, 0x0002)

    Jump('loc_C07')

    def _loc_B42(): pass

    label('loc_B42')

    ChrTalk(
        0x0101,
        (
            '#0010451029V#1007F#1P抱歉，现在暂时还不行。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010451030V#1002F我们很快会回来的，\n',
            '到时候再拜托你合作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0570451031V#680F哎呀，是吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570451032V也没关系，\n',
            '不过请你们早点回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0070, 0x01, 0x8000)
    EventEnd(0x00)

    Return()

    def _loc_C07(): pass

    label('loc_C07')

    Return()

# id: 0x0001 offset: 0xC08
@scena.Code('Init')
def Init():
    EventBegin(0x00)
    Fade(1000)
    SetChrPos(0x0008, 2590, 250, 5360, 180)
    SetChrPos(0x0101, 2000, 250, 3320, 0)
    SetChrPos(0x0107, 3030, 250, 2920, 0)
    SetChrPos(0x00F7, 1910, 250, 1820, 0)
    SetChrPos(0x00F9, 3060, 250, 1500, 0)
    OP_6D(1350, 250, 4070, 0)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0570450983V#683F哎呀，你们几个。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570451034V已经可以接\n',
            '这边的工作了吗？',
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
        'loc_D50',
    )

    ChrTalk(
        0x0101,
        (
            '#0010451035V#1006F#1P嗯，已经没问题了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0070, 0x04, 0x08)
    Call(1, 0x0002)

    Jump('loc_DE5')

    def _loc_D50(): pass

    label('loc_D50')

    ChrTalk(
        0x0101,
        (
            '#0010451036V#1007F#1P不，对不起。\n',
            '还有点困难。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0570451037V#685F你们好像很忙呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570451038V#680F也没关系，\n',
            '不过请你们早点回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0070, 0x01, 0x8000)
    EventEnd(0x00)

    def _loc_DE5(): pass

    label('loc_DE5')

    Return()

# id: 0x0002 offset: 0xDE6
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_E20',
    )

    ChrTalk(
        0x0106,
        (
            '#0050451039V#050F#1P请马上告诉我们情况吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E53')

    def _loc_E20(): pass

    label('loc_E20')

    ChrTalk(
        0x0103,
        (
            '#0030451040V#020F#1P能不能马上\n',
            '告诉我们情况？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E53(): pass

    label('loc_E53')

    ChrTalk(
        0x0008,
        (
            '#0570451041V#682F嗯，好像有人\n',
            '在偷窥我们的浴场。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570451042V最近有好几次\n',
            '听到女性客人这么说。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570451043V我有点在意，\n',
            '就联系了协会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010451044V#1009F#1P唔……\n',
            '偷窥最差劲了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010451045V发现罪犯的话\n',
            '一定要他好看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_FB5',
    )

    ChrTalk(
        0x0106,
        (
            '#0050451046V#050F#1P女性客人具体是\n',
            '怎么说的？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050451047V看到过罪犯的样子吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1017')

    def _loc_FB5(): pass

    label('loc_FB5')

    ChrTalk(
        0x0103,
        (
            '#0030451048V#022F#1P女性客人具体是\n',
            '怎么说的？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030451049V如果有看到过\n',
            '罪犯的样子就好办了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1017(): pass

    label('loc_1017')

    ChrTalk(
        0x0008,
        (
            '#0570451050V#682F不不，没有\n',
            '那么明确。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570451051V充其量只是感觉到有人\n',
            '或者是听到了响声之类的。',
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
        'loc_10C7',
    )

    ChrTalk(
        0x0104,
        (
            '#0040451052V#032F唔，这么说的话\n',
            '也有可能是误解了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_111D')

    def _loc_10C7(): pass

    label('loc_10C7')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_111D',
    )

    ChrTalk(
        0x0105,
        (
            '#0060451053V#042F感觉和响声吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060451054V也有可能是\n',
            '误解呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_111D(): pass

    label('loc_111D')

    ChrTalk(
        0x0008,
        (
            '#0570451055V#682F嗯，一开始\n',
            '我也这么认为。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570451056V不过就像刚才所说的，\n',
            '那样的说法出现过好几次了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570451057V这样一来也没办法简单地\n',
            '用错觉来解释了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010451058V#1015F#1P确实如此……\n',
            '这倒是有点为难。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010451059V也不知道算不算是案件，\n',
            '这样子根本没法调查啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_12C4',
    )

    ChrTalk(
        0x0106,
        (
            '#0050451060V#053F#1P既然情况不明了，\n',
            '就只能先试验一下了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050451061V无论怎样，这一类的罪犯\n',
            '如果不当场抓捕的话是很难将其逮捕的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1348')

    def _loc_12C4(): pass

    label('loc_12C4')

    ChrTalk(
        0x0103,
        (
            '#0030451062V#026F#1P既然情况不明了，\n',
            '就只能先实际试验一下了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030451063V无论怎样，这一类的案件\n',
            '不当场抓捕的话是很难侦破的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1348(): pass

    label('loc_1348')

    @scena.Lambda('lambda_134E')
    def lambda_134E():
        ChrTurnDirection(0x0107, 0x00F7, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_134E)

    Sleep(50)

    @scena.Lambda('lambda_1361')
    def lambda_1361():
        ChrTurnDirection(0x0101, 0x00F7, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1361)

    Sleep(100)

    ChrTurnDirection(0x00F9, 0x00F7, 400)

    ChrTalk(
        0x0107,
        (
            '#0070451064V#064F试验……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070451065V到底要试验什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00F7, 0x0107, 400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_1409',
    )

    ChrTalk(
        0x0106,
        (
            '#0050451066V#050F#1P这还用问。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050451067V当然是去实地洗澡了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1455')

    def _loc_1409(): pass

    label('loc_1409')

    ChrTalk(
        0x0103,
        (
            '#0030451068V#021F#1P呵呵，这还用问。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030451069V当然是我们去洗澡了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1455(): pass

    label('loc_1455')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_1A45',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1733',
    )

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010451070V#1004F#1P用自己做诱饵\n',
            '引蛇出洞！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010451071V#1015F我、我倒是没关系……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010451072V感觉还是有\n',
            '些问题的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060451073V#540F……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00F7, 0x0105, 400)

    ChrTalk(
        0x0106,
        (
            '#0050451074V#050F#1P我不会勉强你们的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050451075V#053F不过，你们愿意帮忙的话\n',
            '确实会很有助于调查。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050451076V因为诱饵越多\n',
            '效果就越好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0105, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x0105,
        (
            '#0060451077V#540F对、对不起……\n',
            '让你劳心了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060451078V#047F这样的话，\n',
            '也请让我帮忙。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060451079V#045F难得当了协力人员，\n',
            '我不希望自己帮不上忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050451080V#053F#1P太好了，不好意思。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050451081V#552F说实话，光有这家伙的话\n',
            '我还担心能不能构成诱饵呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x00F7, 400)

    ChrTalk(
        0x0101,
        (
            '#0010451082V#1007F#1P是是，对不起。\n',
            '反正我不够性感。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1890')

    def _loc_1733(): pass

    label('loc_1733')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1890',
    )

    ChrTalk(
        0x0101,
        (
            '#0010451070V#1004F#1P用自己做诱饵\n',
            '引蛇出洞！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010451084V#1015F不，我倒是\n',
            '没什么关系……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050451085V#552F#1P虽然能不能构成诱饵还是\n',
            '相当微妙的事情，不过也没办法。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050451086V#053F就尽量拜托你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010451082V#1007F#1P是是，对不起。\n',
            '反正我不够性感。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040451088V#031F呵呵，与其说艾丝蒂尔\n',
            '性感不如说是健康之美。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1890(): pass

    label('loc_1890')

    ChrTalk(
        0x0107,
        (
            '#0070451089V#061F嘿嘿……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0107, 400)

    ChrTalk(
        0x0101,
        (
            '#0010451090V#1009F#1P啊，过分。\n',
            '怎么连提妲也笑了！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0107, 0x0101, 400)

    ChrTalk(
        0x0107,
        (
            '#0070451091V#064F……不、不是的！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070451092V#560F只、只是感觉\n',
            '有点高兴。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070451093V好久没有和很多人\n',
            '在一起洗澡了……',
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
            '#0010451094V#1016F#1P很、很多人在一起洗澡……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010451095V那个，这好歹也算\n',
            '是诱饵搜查计划。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00F7, 0x0008, 400)
    Sleep(400)

    ChrTalk(
        0x0106,
        (
            '#0050451096V#051F#1P……那么，\n',
            '能不能请你借露天浴场给我们？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_228C')

    def _loc_1A45(): pass

    label('loc_1A45')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1F06',
    )

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010451070V#1004F#1P用自己做诱饵\n',
            '引蛇出洞！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010451098V#1015F我、我和雪拉姐\n',
            '一起的话倒是没关系……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010451072V感觉一小部分里还是有\n',
            '很严重的问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060451073V#540F……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00F7, 0x0105, 400)

    ChrTalk(
        0x0103,
        (
            '#0030451101V#026F#1P不会勉强你们的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030451102V#027F不过，你们愿意帮忙的话\n',
            '确实会很有助于调查。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030451103V热闹一点能\n',
            '增加诱饵的效果。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0105, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x0105,
        (
            '#0060451077V#540F对、对不起……\n',
            '让你劳心了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060451078V#047F这样的话，\n',
            '也请让我帮忙。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060451079V#045F难得当了协力人员，\n',
            '我不希望自己帮不上忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030451107V#021F#1P呵呵，感谢你的帮助。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030451108V#525F有这点资本的话\n',
            '诱饵就能够成立了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070451089V#061F嘿嘿……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0107, 400)

    ChrTalk(
        0x0101,
        (
            '#0010451110V#1011F#1P咦，提妲。\n',
            '你看起来好像很高兴。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0107, 0x0101, 400)

    ChrTalk(
        0x0107,
        (
            '#0070451111V#560F啊，嗯……\n',
            '因为我很期待。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070451112V好久没有和大家\n',
            '这样悠闲得在一起了。',
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
            '#0010451094V#1016F#1P很、很多人在一起洗澡……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010451095V那个，这好歹也算\n',
            '是诱饵搜查计划。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1E35')
    def lambda_1E35():
        ChrTurnDirection(0x00F9, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_1E35)

    ChrTurnDirection(0x00F7, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030451115V#020F#1P虽然，忘记这一点\n',
            '看上去不是更自然吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030451116V这回是全女性阵容，\n',
            '就尽量放松一点吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00F7, 0x0008, 400)
    Sleep(400)

    ChrTalk(
        0x0103,
        (
            '#0030451117V#020F#1P……那么，\n',
            '能不能请你借露天浴场给我们？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_228C')

    def _loc_1F06(): pass

    label('loc_1F06')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_228C',
    )

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010451118V#1004F#1P用自己做诱饵\n',
            '引蛇出洞！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030451119V#020F#1P嗯，总比干等\n',
            '偷窥犯出现来得好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030451120V#525F你一个人的话虽然有点那个，\n',
            '加上我和提妲的话\n',
            '诱饵就绰绰有余了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010451082V#1007F#1P是是，对不起。\n',
            '反正我不够性感。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040451088V#031F呵呵，与其说艾丝蒂尔\n',
            '性感不如说是健康之美。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070451089V#061F嘿嘿……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0107, 400)

    ChrTalk(
        0x0101,
        (
            '#0010451090V#1009F#1P啊，过分。\n',
            '怎么连提妲也笑了！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0107, 0x0101, 400)

    ChrTalk(
        0x0107,
        (
            '#0070451091V#064F啊……不、不是的！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070451092V#560F只、只是感觉\n',
            '有点高兴。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070451093V好久没有和很多人\n',
            '在一起洗澡了……',
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
            '#0010451094V#1016F#1P很、很多人在一起洗澡……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010451095V那个，这好歹也算\n',
            '是诱饵搜查计划。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030451115V#020F#1P虽然，忘记这一点\n',
            '看上去不是更自然吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030451131V就当作临时休假\n',
            '就尽量放松一点吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00F7, 0x0008, 400)
    Sleep(400)

    ChrTalk(
        0x0103,
        (
            '#0030451117V#020F#1P……那么，\n',
            '能不能请你借露天浴场给我们？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_228C(): pass

    label('loc_228C')

    ChrTalk(
        0x0008,
        (
            '#0570451133V#681F嗯，尽管用吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570451134V我会暂时打佯的，\n',
            '你们四个就好好地泡泡吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_22EE')
    def lambda_22EE():
        ChrTurnDirection(0x0107, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_22EE)

    Sleep(250)

    @scena.Lambda('lambda_2301')
    def lambda_2301():
        ChrTurnDirection(0x0101, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2301)

    Sleep(150)

    ChrTurnDirection(0x00F9, 0x0008, 400)

    ChrTalk(
        0x0107,
        (
            '#0070451135V#061F谢谢麻绪婆婆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010451136V#1015F#1P嗯，这样就决定了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_29B7',
    )

    ChrTalk(
        0x0106,
        (
            '#0050451137V#051F#1P嗯，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050451138V那就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010451139V#1004F#1P啊……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_23DB')
    def lambda_23DB():
        ChrTurnDirection(0x0107, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_23DB)

    @scena.Lambda('lambda_23E9')
    def lambda_23E9():
        ChrTurnDirection(0x00F9, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_23E9)

    ChrTurnDirection(0x0101, 0x0106, 400)

    ChrTalk(
        0x0101,
        (
            '#0010451140V#1004F#1P拜托我们……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010451141V莫非你\n',
            '不打算洗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050451142V#055F#1P啊！？\n',
            '你说什么呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050451143V为什么连我\n',
            '也要去洗澡？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0570451144V#682F等等等等，\n',
            '你才是在胡说八道。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570451145V不过都到了这里，\n',
            '我是不会允许你\n',
            '不去泡露天浴的。',
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
        'loc_255B',
    )

    ChrTalk(
        0x0104,
        (
            '#0040451146V#031F呼～真服了你们。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040451147V没什么好\n',
            '害羞的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_25BE')

    def _loc_255B(): pass

    label('loc_255B')

    ChrTalk(
        0x0101,
        (
            '#0010451148V#1012F#1P是啊是啊。\n',
            '而且是你提议的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010451149V#1002F……咦，你难道\n',
            '是在害羞？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_25BE(): pass

    label('loc_25BE')

    OP_62(0x0106, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x0106,
        (
            '#0050451150V#552F#1P我、我可不是害羞。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050451151V我只会考虑\n',
            '工作的事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0570451152V#685F啊，真要把人给急死了。\n',
            '别再说那种硬邦邦的事了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570451153V#682F是男人的话就别啰嗦，\n',
            '乖乖地去泡澡。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570451154V来温泉竟然不洗澡？\n',
            '我怎么能容忍这么愚蠢的事情发生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010451155V#1015F#1P…………我说你啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0106, 0x00000000, 2000, 0x0E, 0x0F, 0x000000FA, 0x02)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(1000)

    OP_63(0x0106)

    ChrTalk(
        0x0106,
        (
            '#0050451156V#551F#1P啊～你废话真多。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050451157V明白了啦。\n',
            '我去洗还不行啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050451158V#057F不过，你们几个……\n',
            '可别忘了自己是在工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010451159V#1006F#1P嗯，这你就放心吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0107, 400)

    ChrTalk(
        0x0101,
        (
            '#0010451160V#1006F#1P……我说？　提妲？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2825')
    def lambda_2825():
        ChrTurnDirection(0x00F9, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_2825)

    ChrTurnDirection(0x0107, 0x0101, 400)

    ChrTalk(
        0x0107,
        (
            '#0070451161V#560F嗯、嗯……不用担心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0107, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x0107, 0x0008, 400)

    ChrTalk(
        0x0107,
        (
            '#0070451162V#064F……啊，不好！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070451163V婆婆，\n',
            '借我一套毛巾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0570451164V#683F哎呀，你忘带了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070451165V#063F嗯，我没想到\n',
            '会来泡澡……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070451166V#064F啊，还有香波。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010451167V#1016F#1P（嗯、嗯。\n',
            '她真给当成是洗澡时间了。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050451168V#551F#1P（完全……没紧张感呢。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2EF7')

    def _loc_29B7(): pass

    label('loc_29B7')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2D8D',
    )

    ChrTalk(
        0x0104,
        (
            '#0040451169V#035F呼，那我们走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0104, 400)

    ChrTalk(
        0x0101,
        (
            '#0010451170V#1019F#1P……咦，你在这儿\n',
            '摆好架势干吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0104, 0x0101, 400)

    ChrTalk(
        0x0104,
        (
            '#0040451171V#031F哈哈哈。\n',
            '因为对这个旅馆很熟悉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040451172V我只是在想\n',
            '要不要给你们带路。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010451173V#1007F#1P嘴上这么说……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010451174V……实际上准备不声不响地\n',
            '跟到更衣室里面来吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0104, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0104,
        (
            '#0040451175V#033F呀………！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040451176V#031F你、你在说什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010451177V#1019F#1P别以为你一直都能\n',
            '耍成这一招。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010451178V#1007F……所以呢，\n',
            '雪拉姐你们先去。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010451179V我首先押送这家伙\n',
            '去男澡堂的更衣室。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x0104, 400)

    ChrTalk(
        0x0103,
        (
            '#0030451180V#021F#1P呵呵，拜托你了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030451181V那么奥利维尔，\n',
            '不好意思我先行一步了㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0107, 0x0104, 400)

    ChrTalk(
        0x0107,
        (
            '#0070451182V#560F露天浴场见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040451183V#035F呵、呵呵……没关系。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040451184V我会把这笔帐\n',
            '留在露天浴场……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010451185V#1019F#1P……如果你想这样讨还\n',
            '肯定饶不了你。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010451186V把你当作偷窥犯\n',
            '押去协会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0104, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0104,
        (
            '#0040451187V#034F知、知道了。\n',
            '我会自重的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2EF7')

    def _loc_2D8D(): pass

    label('loc_2D8D')

    ChrTalk(
        0x0103,
        (
            '#0030451188V#020F#1P嗯，那就走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0107, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x0107, 0x0008, 400)

    ChrTalk(
        0x0107,
        (
            '#0070451189V#064F啊，不行！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070451163V婆婆，\n',
            '借我一套毛巾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2E22')
    def lambda_2E22():
        ChrTurnDirection(0x00F7, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_2E22)

    @scena.Lambda('lambda_2E30')
    def lambda_2E30():
        ChrTurnDirection(0x00F9, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_2E30)

    ChrTurnDirection(0x0101, 0x0107, 400)

    ChrTalk(
        0x0008,
        (
            '#0570451191V#683F怎么了，忘了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070451192V#063F嗯，我没想到\n',
            '会来泡澡……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070451166V#064F啊，还有香波。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010451194V#1016F#1P（嗯、嗯。\n',
            '她真给当成是洗澡时间了。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2EF7(): pass

    label('loc_2EF7')

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene('ED6_DT21/T3200._SN', 107, 0, 0)
    IdleLoop()

    Return()

# id: 0x0003 offset: 0x2F0F
@scena.Code('func_03_2F0F')
def func_03_2F0F():
    EventBegin(0x00)
    SetChrPos(0x0008, 2590, 250, 5360, 180)
    SetChrPos(0x0101, 2000, 250, 3320, 0)
    SetChrPos(0x0107, 3030, 250, 2920, 0)
    SetChrPos(0x00F7, 1910, 250, 1820, 0)
    SetChrPos(0x00F9, 3060, 250, 1500, 0)
    OP_6D(1350, 250, 4070, 0)
    OP_4A(0x0008, 255)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0570451482V#683F#2P──原来如此。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570451483V偷窥犯的真身\n',
            '是魔兽啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_3040',
    )

    ChrTalk(
        0x0106,
        (
            '#0050451484V#050F虽然不敢确定，\n',
            '不过可能性很高。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050451485V我们已经教训过它们了，\n',
            '应该不会再来了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_30AD')

    def _loc_3040(): pass

    label('loc_3040')

    ChrTalk(
        0x0103,
        (
            '#0030451486V#020F虽然不敢确定，\n',
            '不过可能性很高。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030451487V我们已经教训过它们了，\n',
            '应该不会再来了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_30AD(): pass

    label('loc_30AD')

    ChrTalk(
        0x0101,
        (
            '#0010451488V#1015F#1P不过，一两只\n',
            '误闯进来还能让人理解……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010451489V#1002F一下子来那么多，\n',
            '你们不觉得有些奇怪吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0570451490V#682F#2P嗯，我第一次碰到这种事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570451491V可能发生过什么事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070451492V#063F说不定……\n',
            '和地震有关系。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_31B0')
    def lambda_31B0():
        ChrTurnDirection(0x0101, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_31B0)

    Sleep(150)

    @scena.Lambda('lambda_31C3')
    def lambda_31C3():
        ChrTurnDirection(0x00F7, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_31C3)

    Sleep(100)

    ChrTurnDirection(0x00F9, 0x0107, 400)

    ChrTalk(
        0x0101,
        (
            '#0010451493V#1004F#1P和地震？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0107, 0x0101, 400)

    ChrTalk(
        0x0107,
        (
            '#0070451494V#063F嗯、嗯，地震有可能\n',
            '造成魔兽发狂。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070451495V居住地的环境如果发生变化，\n',
            '好像也有可能会这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_32B5',
    )

    ChrTalk(
        0x0105,
        (
            '#0060451496V#042F原来如此……\n',
            '有道理呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_32EF')

    def _loc_32B5(): pass

    label('loc_32B5')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_32EF',
    )

    ChrTalk(
        0x0104,
        (
            '#0040451497V#030F原来如此……\n',
            '有道理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_32EF(): pass

    label('loc_32EF')

    ChrTalk(
        0x0008,
        (
            '#0570451498V#680F#2P算了，反正如果是自然\n',
            '造成的话也没办法。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570451499V如果再出现的话\n',
            '先放弃调查，和协会联络吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_336D')
    def lambda_336D():
        OP_8C(0x00F7, 0, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_336D)

    Sleep(150)

    @scena.Lambda('lambda_3380')
    def lambda_3380():
        OP_8C(0x0101, 0, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3380)

    Sleep(100)

    @scena.Lambda('lambda_3393')
    def lambda_3393():
        OP_8C(0x00F9, 0, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_3393)

    Sleep(50)

    OP_8C(0x0107, 0, 400)

    ChrTalk(
        0x0101,
        (
            '#0010451500V#1006F#1P嗯，应该这么做。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010451501V#1001F到时候又能\n',
            '好好洗澡了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_3445',
    )

    ChrTalk(
        0x0106,
        (
            '#0050451502V#551F嗯，总之我也想以\n',
            '和工作无关的方式来洗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3485')

    def _loc_3445(): pass

    label('loc_3445')

    ChrTalk(
        0x0103,
        (
            '#0030451503V#021F呵呵，总之我也想以\n',
            '和工作无关的方式来洗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3485(): pass

    label('loc_3485')

    ChrTalk(
        0x0008,
        (
            '#0570451504V#681F哈哈，你们随时\n',
            '都可以来洗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570451505V不管怎样，今天你们是帮了大忙了。\n',
            '有什么需要我会再找你们的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010451506V#1006F#1P嗯，那么再见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070451507V#061F再见，麻绪婆婆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0008)
    OP_28(0x0070, 0x04, 0x10)
    OP_28(0x0070, 0x01, 0x0004)
    OP_28(0x0070, 0x01, 0x0008)
    OP_22(0x0017, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【击退偷窥色魔】',
            (TxtCtl.SetColor, 0x0),
            '完成了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_4B(0x0008, 255)
    ClearMapFlags(0x10000000)
    EventEnd(0x00)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
