import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T0134_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0134_1 ._SN')

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
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/T0134_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x2C85
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
    Call(1, 0x0004)
    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 2, 0x1812)),
            Expr.Return,
        ),
        'loc_15E',
    )

    ChrTalk(
        0x000D,
        (
            '#3420460461V因为这雾的原因\n',
            '今天也看不见星星……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3420460462V不过只要有你在，\n',
            '我就一点儿也不寂寞。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3420460463V因为我所寻找的星星\n',
            '就是你啊，艾娅莉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_15E(): pass

    label('loc_15E')

    ChrTalk(
        0x0101,
        (
            '#0010460464V#1007F#3P打、打扰了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460429V请问现在方便吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000D, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTalk(
        0x000D,
        (
            '#3420460430V嗯……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_01DC')
    def lambda_01DC():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_01DC)

    Sleep(250)

    ChrTurnDirection(0x000E, 0x0101, 400)

    ChrTalk(
        0x000E,
        (
            '#3430460431V#2P……啊，是谁？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010460468V#1000F#3P我们是游击士协会的人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460433V您就是阿鲁姆先生吗？\n',
            '我们是看了告示板上的委托而来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3420460434V哇～终于来了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3420460435V太好了！\n',
            '我等你们好久了！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000E, 0x000D, 400)

    ChrTalk(
        0x000E,
        (
            '#3430460436V#2P太好了！阿鲁姆！\n',
            '我好高兴啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000D, 0x000E, 400)

    ChrTalk(
        0x000D,
        (
            '#3420460437V啊啊～艾娅莉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3420460438V你的心灵为什么\n',
            '这样美丽？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3420460439V明明让你痛苦\n',
            '的人就是我…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#3430460440V#2P不要那么说，阿鲁姆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#3430460441V#2P你心中的痛苦\n',
            '我全都明白！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#3430460442V#2P那一夜，咱们不是约定好了吗？\n',
            '不管到什么时候，你和我……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3420460443V……也要携手\n',
            '走完一生…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3420460444V啊啊！！艾娅莉！我爱你！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#3430460445V#2P我也是啊！阿鲁姆！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000F, 0x00000000, 1700, 0x0A, 0x0B, 0x000000FA, 0x02)
    OP_22(0x000F, 0x00, 0x64)
    Sleep(1500)

    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    OP_62(0x0103, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(150)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_521',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)

    Jump('loc_55F')

    def _loc_521(): pass

    label('loc_521')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_548',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)

    Jump('loc_55F')

    def _loc_548(): pass

    label('loc_548')

    OP_62(0x00F8, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)

    def _loc_55F(): pass

    label('loc_55F')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_586',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)

    Jump('loc_5C4')

    def _loc_586(): pass

    label('loc_586')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5AD',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)

    Jump('loc_5C4')

    def _loc_5AD(): pass

    label('loc_5AD')

    OP_62(0x00F9, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)

    def _loc_5C4(): pass

    label('loc_5C4')

    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010460482V#1016F#3P那、那个～……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460447V您有什么\n',
            '要求呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000D, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    ChrTalk(
        0x000D,
        (
            '#3420460448V啊……！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#3430460449V#2P对了！委托！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_066D')
    def lambda_066D():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_066D)

    Sleep(150)

    ChrTurnDirection(0x000E, 0x0101, 400)

    ChrTalk(
        0x000D,
        (
            '#3420460450V其、其实是一件关系到我们两个\n',
            '将来的重要事件！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3420460451V希望你们马上就开始调查，\n',
            '可以吗？',
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
        'loc_74D',
    )

    Call(1, 0x0002)

    Jump('loc_8ED')

    def _loc_74D(): pass

    label('loc_74D')

    ChrTalk(
        0x0101,
        (
            '#0010460488V#1015F#3P啊～抱歉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460453V马上开始的话\n',
            '可能有些困难。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3420460454V怎、怎么会…\n',
            '请不要抛弃我们啊！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#3430460455V#2P求你们了……\n',
            '这件事真的很重要！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030460456V#020F没关系，\n',
            '我们会回来的，放心吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010460493V#1000F#3P嗯，等我们有空的时候\n',
            '一定回来仔细听你们说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3420460458V真、真的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3420460459V好、好… \n',
            '我相信你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#3430460460V#2P一定要再来啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0072, 0x01, 0x8000)

    def _loc_8ED(): pass

    label('loc_8ED')

    ChrTurnDirection(0x000E, 0x000D, 0)
    ChrTurnDirection(0x000D, 0x000E, 0)
    OP_4B(0x000D, 255)
    OP_4B(0x000E, 255)
    EventEnd(0x00)

    Return()

# id: 0x0001 offset: 0x906
@scena.Code('Init')
def Init():
    EventBegin(0x00)
    Fade(1000)
    Call(1, 0x0004)
    OP_8C(0x000D, 270, 0)
    OP_8C(0x000E, 270, 0)
    OP_0D()

    ChrTalk(
        0x000D,
        (
            '#3420460497V那个、各位游击士……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3420460498V你们、可以接受\n',
            '我的委托吗？',
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
        'loc_9CB',
    )

    Call(1, 0x0002)

    Jump('loc_A79')

    def _loc_9CB(): pass

    label('loc_9CB')

    ChrTalk(
        0x0101,
        (
            '#0010460505V#1007F呼、呼……\n',
            '现在确实还有点为难呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3420460500V怎、怎么会…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010460507V#1016F抱歉抱歉。\n',
            '下次再来听你们说明。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#3430460502V嗯，会再来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A79(): pass

    label('loc_A79')

    ChrTurnDirection(0x000E, 0x000D, 0)
    ChrTurnDirection(0x000D, 0x000E, 0)
    OP_4B(0x000D, 255)
    OP_4B(0x000E, 255)
    EventEnd(0x00)

    Return()

# id: 0x0002 offset: 0xA92
@scena.Code('ReInit')
def ReInit():
    ChrTalk(
        0x0101,
        (
            '#0010460598V#1006F啊，嗯。\n',
            '没问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_BB4',
    )

    ChrTalk(
        0x000D,
        (
            '#3420460510V真、真的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030460511V#020F只是，既然很急的话，\n',
            '就麻烦您长话短说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3420460512V啊啊～那个倒无所谓！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3420460513V呀～不管怎样，\n',
            '多谢你们了，游击士！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3420460514V你们能来\n',
            '真是救了我们一命啊！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C05')

    def _loc_BB4(): pass

    label('loc_BB4')

    ChrTalk(
        0x000D,
        (
            '#3420460510V真、真的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3420460516V太感谢了！！\n',
            '谢谢了！！游击士！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C05(): pass

    label('loc_C05')

    ChrTurnDirection(0x000E, 0x000D, 400)

    ChrTalk(
        0x000E,
        (
            '#3430460436V#2P太好了！阿鲁姆！\n',
            '我好高兴啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000D, 0x000E, 400)

    ChrTalk(
        0x000D,
        (
            '#3420460437V啊啊～艾娅莉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3420460519V为什么你的心灵\n',
            '这样美丽？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#3430460520V#2P啊啊～阿鲁姆……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010460610V#1019F#4S……#2S',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460522V……我说委托的事…～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0D06')
    def lambda_0D06():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_0D06)

    Sleep(150)

    ChrTurnDirection(0x000E, 0x0101, 400)

    ChrTalk(
        0x000D,
        (
            '#3420460523V……失礼了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3420460524V那么，请听我说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030460525V#020F嗯，可能的话，请您尽量说简洁点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3420460526V想委托各位帮忙的事情并不是别的，\n',
            '就是寻找我们的结婚戒指。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3420460527V我拼命攒钱，好不容易\n',
            '买到了那个高档戒指，可是… ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3420460528V那、那只可恨的小偷乌鸦，\n',
            '竟然把它给偷走了！！！',
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
            '#0010460618V#1004F#3P乌、乌鸦！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_EE0',
    )

    ChrTalk(
        0x0107,
        (
            '#0070460530V#064F乌鸦……是那只鸟吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F9D')

    def _loc_EE0(): pass

    label('loc_EE0')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_F20',
    )

    ChrTalk(
        0x0105,
        (
            '#0060460531V#044F乌鸦吗……难道是那只鸟？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F9D')

    def _loc_F20(): pass

    label('loc_F20')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_F64',
    )

    ChrTalk(
        0x0104,
        (
            '#0040460532V#033F所谓的乌鸦……是指那只鸟吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F9D')

    def _loc_F64(): pass

    label('loc_F64')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_F9D',
    )

    ChrTalk(
        0x0106,
        (
            '#0050460533V#052F乌鸦……是那只鸟吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F9D(): pass

    label('loc_F9D')

    ChrTalk(
        0x000D,
        (
            '#3420460534V对！总之就是那个哇哇叫的混帐了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3420460535V那个可恶的家伙竟然\n',
            '把我们的结婚戒指给叼跑了！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x0072, 0x01, 0x4000)"),
            (Expr.Eval, "OP_40(0x0234, 0x00)"),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1518',
    )

    ChrTalk(
        0x0103,
        (
            '#0030460536V#026F确实，乌鸦的习性就是\n',
            '喜欢收集闪光的东西呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030460537V#027F话虽如此……\n',
            '但戒指被乌鸦偷走，还真是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010460538V#1011F啊、难道说……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460539V雪拉姐也\n',
            '想起那个戒指了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030460540V#020F嗯，保险起见，\n',
            '最好还是给他看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3420460541V？？？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3420460542V有什么线索吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0101, 90, 400)

    ChrTalk(
        0x0101,
        (
            '#0010460632V#1002F阿鲁姆先生，请您\n',
            '看一下这只戒指可以吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3420460633V#6A嗯、当然……',
            TxtCtl.Enter,
        ),
    )

    Call(1, 0x0005)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010460634V#1004F咦咦！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_125C',
    )

    ChrTalk(
        0x0107,
        (
            '#0070460546V#064F那个那个……\n',
            '确实就是这只戒指吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1337')

    def _loc_125C(): pass

    label('loc_125C')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1294',
    )

    ChrTalk(
        0x0105,
        (
            '#0060460547V#044F没、没搞错吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1337')

    def _loc_1294(): pass

    label('loc_1294')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_12CC',
    )

    ChrTalk(
        0x0104,
        (
            '#0040460548V#033F那个、没弄错吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1337')

    def _loc_12CC(): pass

    label('loc_12CC')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1308',
    )

    ChrTalk(
        0x0106,
        (
            '#0050460549V#055F喂喂、不会是真的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1337')

    def _loc_1308(): pass

    label('loc_1308')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1337',
    )

    ChrTalk(
        0x0108,
        (
            '#0080460550V#073F没弄错吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1337(): pass

    label('loc_1337')

    ChrTalk(
        0x000D,
        (
            '#3420460551V嗯、嗯……绝对没错！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3420460552V这就是我们的戒指！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#3430460553V#2P啊啊！！女神啊……\n',
            '衷心感谢您的恩德！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030460554V#021F呵呵，没想到\n',
            '会这么巧啊。',
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
        'loc_142D',
    )

    ChrTalk(
        0x0108,
        (
            '#0080460555V#073F真是惊人的巧合呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_14E5')

    def _loc_142D(): pass

    label('loc_142D')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1469',
    )

    ChrTalk(
        0x0106,
        (
            '#0050460556V#052F真是好惊人的巧合呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_14E5')

    def _loc_1469(): pass

    label('loc_1469')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_14AC',
    )

    ChrTalk(
        0x0104,
        (
            '#0040460557V#031F哈哈哈。\n',
            '真是惊人的巧合啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_14E5')

    def _loc_14AC(): pass

    label('loc_14AC')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_14E5',
    )

    ChrTalk(
        0x0105,
        (
            '#0060460558V#044F好、好惊人的巧合啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_14E5(): pass

    label('loc_14E5')

    Call(1, 0x0006)
    OP_28(0x0072, 0x01, 0x0008)
    OP_28(0x0072, 0x01, 0x0010)
    OP_28(0x0072, 0x04, 0x10)
    ChrTurnDirection(0x000E, 0x000D, 0)
    ChrTurnDirection(0x000D, 0x000E, 0)
    OP_63(0x000F)
    OP_4B(0x000D, 255)
    OP_4B(0x000E, 255)
    EventEnd(0x00)

    Jump('loc_1CF3')

    def _loc_1518(): pass

    label('loc_1518')

    ChrTalk(
        0x0103,
        (
            '#0030460559V#027F确实、乌鸦具有\n',
            '喜欢收集闪亮东西的习性。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030460560V所以会对戒指这种东西\n',
            '感兴趣的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010460650V#1015F#3P那么、戒指现在\n',
            '应该在它们的巢中吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460562V#1002F是让我们来找那戒指的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3420460563V嗯、那就是我们\n',
            '想委托你们办的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3420460564V虽然我明白\n',
            '这件事太过困难。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3420460565V但即使如此，\n',
            '也拜托你们尽力帮我们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010460655V#1007F#3P嗯，我们肯定\n',
            '会尽力而为，不过…',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460567V以现有的情报来说，\n',
            '实在是不容易找到。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460568V#1002F……能不能再提供给我们一些线索呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3420460569V啊啊，是要寻找\n',
            '乌鸦的巢穴了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3420460570V大概在洛连特北部吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3420460571V那家伙飞向玛鲁加山道\n',
            '那边去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3420460572V再加上现在起了大雾，\n',
            '能追上的可能性不大了吧…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x0072, 0x01, 0x4000)"),
            (Expr.Eval, "OP_40(0x0234, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1948',
    )

    ChrTalk(
        0x0101,
        (
            '#0010460662V#1015F#3P原来如此。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460574V巢穴大概在北边吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460575V…啊？北边？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x14, 0x17, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(1000)

    OP_63(0x0101)

    ChrTalk(
        0x0101,
        (
            '#0010460665V#1019F#3P（难、难道说……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460666V（在塔顶上\n',
            '  发现的那个戒指…）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3420460578V嗯？怎么啦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010460668V#1016F#3P呼、呼呼。没什么。\n',
            '（一定只是心理作用吧～）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_198F')

    def _loc_1948(): pass

    label('loc_1948')

    ChrTalk(
        0x0101,
        (
            '#0010460662V#1015F#3P原来如此。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460581V巢穴大概在北边吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_198F(): pass

    label('loc_198F')

    ChrTalk(
        0x0103,
        (
            '#0030460582V#026F……我们会做个参考的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030460583V不管怎样，巢穴肯定\n',
            '是在高处就对了。',
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
        'loc_1A56',
    )

    ChrTalk(
        0x0108,
        (
            '#0080460584V#075F啊，那肯定没错的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080460585V真是的……\n',
            '还真是个麻烦的工作啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B5B')

    def _loc_1A56(): pass

    label('loc_1A56')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1ABD',
    )

    ChrTalk(
        0x0106,
        (
            '#0050460586V#551F嗯，那肯定没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050460587V真是的……\n',
            '还真是个麻烦的工作啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B5B')

    def _loc_1ABD(): pass

    label('loc_1ABD')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1B24',
    )

    ChrTalk(
        0x0104,
        (
            '#0040460588V#034F嗯，那是肯定的啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040460589V呼～还真是件\n',
            '超级麻烦的工作啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B5B')

    def _loc_1B24(): pass

    label('loc_1B24')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1B5B',
    )

    ChrTalk(
        0x0105,
        (
            '#0060460590V#047F嗯，确实比较麻烦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1B5B(): pass

    label('loc_1B5B')

    ChrTalk(
        0x000D,
        (
            '#3420460591V除了协会之外，\n',
            '我们再也找不到人可以拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3420460592V所以无论如何\n',
            '你们也要帮帮忙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#3430460593V#2P你们是我们唯一的希望了。\n',
            '无论如何也请帮我们找找吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010460683V#1006F#3P嗯……\n',
            '我们会努力找找看的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030460595V#020F那么，有什么发现的话\n',
            '我们会再来报告给您。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3420460596V期待大家！我们会一直等的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#3430460597V#2P加油哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0072, 0x04, 0x04)
    OP_28(0x0072, 0x04, 0x08)
    OP_28(0x0072, 0x01, 0x0001)
    OP_28(0x0072, 0x01, 0x0002)
    OP_A2(0x0007)
    ClearChrFlags(0x000E, 0x0010)
    ClearChrFlags(0x000D, 0x0010)
    def _loc_1CF3(): pass

    label('loc_1CF3')

    Return()

# id: 0x0003 offset: 0x1CF4
@scena.Code('func_03_1CF4')
def func_03_1CF4():
    EventBegin(0x00)
    Fade(1000)
    Call(1, 0x0004)
    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 2, 0x1812)),
            Expr.Return,
        ),
        'loc_1DAA',
    )

    ChrTalk(
        0x000D,
        (
            '#3420460728V因为这雾的原因\n',
            '今天也看不见星星……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3420460729V不过只要有你在，\n',
            '我就一点儿也不寂寞。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3420460730V因为我所寻找的星星\n',
            '就是你啊，艾娅莉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1DAA(): pass

    label('loc_1DAA')

    ChrTalk(
        0x0101,
        (
            '#0010460731V#1007F（还、还没停啊……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3420460732V嗯……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1DF6')
    def lambda_1DF6():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_1DF6)

    Sleep(250)

    ChrTurnDirection(0x000E, 0x0101, 400)

    ChrTalk(
        0x000E,
        (
            '#3430460700V#2P……啊，游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000D, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    OP_63(0x000D)

    ChrTalk(
        0x000D,
        (
            '#3420460701V难、难道\n',
            '你们找到戒指了！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030460702V#020F嗯，找到了一只符合您\n',
            '说明的戒指。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030460703V但不知道是不是您\n',
            '丢失的那个。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010460737V#1000F所以\n',
            '希望您能确认一下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460705V阿鲁姆先生，\n',
            '看一下这只戒指可以吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3420460739V#6A嗯、当然……',
            TxtCtl.Enter,
        ),
    )

    Call(1, 0x0005)

    ChrTalk(
        0x0101,
        (
            '#0010191036V#1004F真、真的！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1FCA',
    )

    ChrTalk(
        0x0107,
        (
            '#0070460546V#064F那个那个……\n',
            '确实就是这只戒指吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_20A5')

    def _loc_1FCA(): pass

    label('loc_1FCA')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2002',
    )

    ChrTalk(
        0x0105,
        (
            '#0060460547V#044F没、没搞错吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_20A5')

    def _loc_2002(): pass

    label('loc_2002')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_203A',
    )

    ChrTalk(
        0x0104,
        (
            '#0040460548V#033F那个、没弄错吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_20A5')

    def _loc_203A(): pass

    label('loc_203A')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2076',
    )

    ChrTalk(
        0x0106,
        (
            '#0050460549V#055F喂喂、不会是真的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_20A5')

    def _loc_2076(): pass

    label('loc_2076')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_20A5',
    )

    ChrTalk(
        0x0108,
        (
            '#0080460550V#073F没弄错吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_20A5(): pass

    label('loc_20A5')

    ChrTalk(
        0x000D,
        (
            '#3420460551V嗯、嗯……绝对没错！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3420460552V这就是我们的戒指！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#3430460553V#2P啊啊！！女神啊……\n',
            '衷心感谢您的恩德！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030460719V#021F呵呵，太好了。\n',
            '终于物归原主了啊。',
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
        'loc_21C8',
    )

    ChrTalk(
        0x0108,
        (
            '#0080460720V#070F呼，真是没想到啊，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080460721V竟然会在那种\n',
            '地方找到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2320')

    def _loc_21C8(): pass

    label('loc_21C8')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2246',
    )

    ChrTalk(
        0x0105,
        (
            '#0060460722V#040F太好了……\n',
            '这样的话事情也就解决了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060460723V真是做梦也想不到会在\n',
            '那种地方找到啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2320')

    def _loc_2246(): pass

    label('loc_2246')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_22BA',
    )

    ChrTalk(
        0x0106,
        (
            '#0050460724V#051F啊啊，总算是解决了，\n',
            '松了口气。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050460725V真是没想到会在\n',
            '那种地方找到啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2320')

    def _loc_22BA(): pass

    label('loc_22BA')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2320',
    )

    ChrTalk(
        0x0104,
        (
            '#0040460726V#030F呼～真是不容易啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040460727V真没想到竟然会在\n',
            '那种地方找到啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2320(): pass

    label('loc_2320')

    Call(1, 0x0006)
    OP_28(0x0072, 0x01, 0x0010)
    OP_28(0x0072, 0x04, 0x10)
    ChrTurnDirection(0x000E, 0x000D, 0)
    ChrTurnDirection(0x000D, 0x000E, 0)
    OP_63(0x000F)
    OP_4B(0x000D, 255)
    OP_4B(0x000E, 255)
    EventEnd(0x00)

    Return()

# id: 0x0004 offset: 0x234B
@scena.Code('func_04_234B')
def func_04_234B():
    OP_4A(0x000D, 255)
    OP_4A(0x000E, 255)
    SetChrPos(0x0101, 62800, 0, 47270, 90)
    SetChrPos(0x0103, 61790, 0, 46800, 90)
    SetChrPos(0x00F8, 61270, 0, 47980, 90)
    SetChrPos(0x00F9, 60320, 0, 47290, 90)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_23C6',
    )

    SetChrPos(0x00F9, 61270, 0, 47980, 90)
    SetChrPos(0x00F8, 60320, 0, 47290, 90)

    def _loc_23C6(): pass

    label('loc_23C6')

    OP_6D(61800, 0, 48260, 0)
    OP_67(0, 6130, -10000, 0)
    OP_6B(2870, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)

    ExecExpressionWithValue(
        0x000F,
        0x01,
        (
            (Expr.GetChrWork, 0xD, 0x1),
            (Expr.GetChrWork, 0xE, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000F,
        0x02,
        (
            (Expr.GetChrWork, 0xD, 0x2),
            (Expr.GetChrWork, 0xE, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000F,
        0x03,
        (
            (Expr.GetChrWork, 0xD, 0x3),
            (Expr.GetChrWork, 0xE, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0005 offset: 0x2443
@scena.Code('func_05_2443')
def func_05_2443():
    OP_94(0x01, 0x000D, 0x0000, 0x000000C8, 0x000003E8, 0x00)
    OP_56(0x00)
    OP_59()
    OP_62(0x000D, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(100)

    @scena.Lambda('lambda_2477')
    def lambda_2477():
        OP_95(0x00FE, 0x00000000, 0x00000000, 0x00000000, 0x00000190, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_2477)

    Sleep(900)

    OP_63(0x000D)
    WaitForThreadExit(0x000D, 0x0001)

    ChrTalk(
        0x000D,
        (
            '#3420460707V#3S……啊啊啊啊啊啊啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3420460708V那那那、那个戒指！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3420460709V#3S那不就是我、我们的结婚戒指吗！！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0x00000000, 0x000001F4, 0x00000BB8, 0x00000064)
    CloseMessageWindow()

    Return()

# id: 0x0006 offset: 0x2534
@scena.Code('func_06_2534')
def func_06_2534():
    ChrTalk(
        0x0101,
        (
            '#0010460787V#1015F呼、真是无话可说了…',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460762V城镇市民的戒指\n',
            '最后竟然在塔顶找到…',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460763V#1000F……呵呵～不过还是\n',
            '先把戒指还给他吧。',
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
            (TxtCtl.Item, ItemTable['白金戒指']),
            (TxtCtl.SetColor, 0x0),
            '交出了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    RemoveItem(ItemTable['白金戒指'], 1)
    OP_94(0x01, 0x000D, 0x00B4, 0x000000C8, 0x000003E8, 0x00)

    ChrTalk(
        0x000D,
        (
            '#3420460764V啊、谢谢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3420460765V真是感激不尽！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#3430460766V#2P呵呵，相信游击士\n',
            '果然没有错㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010460793V#1017F哪里哪里，没什么。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030460768V#020F马上就要\n',
            '结婚了吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030460769V#525F祝你们幸福哦㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000E, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x000E,
        (
            '#3430460770V#2P喔…………\n',
            '啊、谢谢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#3430460771V#2P感、感觉真好啊！\n',
            '被人祝福的感觉…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000D, 0x000E, 400)

    ChrTalk(
        0x000D,
        (
            '#3420460772V这样的话，要尽快了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3420460773V我们的未来一定会\n',
            '得到无数的祝福的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000E, 0x000D, 400)

    ChrTalk(
        0x000E,
        (
            '#3430460520V#2P啊啊～阿鲁姆……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3420460775V艾娅莉……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000F, 0x00000000, 1800, 0x0A, 0x0B, 0x000000FA, 0x00)
    Sleep(1000)

    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    OP_62(0x0103, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(100)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2894',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)

    Jump('loc_28D2')

    def _loc_2894(): pass

    label('loc_2894')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_28BB',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)

    Jump('loc_28D2')

    def _loc_28BB(): pass

    label('loc_28BB')

    OP_62(0x00F8, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)

    def _loc_28D2(): pass

    label('loc_28D2')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_28F9',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)

    Jump('loc_2937')

    def _loc_28F9(): pass

    label('loc_28F9')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2920',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)

    Jump('loc_2937')

    def _loc_2920(): pass

    label('loc_2920')

    OP_62(0x00F9, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)

    def _loc_2937(): pass

    label('loc_2937')

    Sleep(1000)

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_298F',
    )

    ChrTalk(
        0x0107,
        (
            '#0070460776V#067F（啊哈～……\n',
            '  完全沉浸在二人世界中了啊。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A64')

    def _loc_298F(): pass

    label('loc_298F')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_29D9',
    )

    ChrTalk(
        0x0105,
        (
            '#0060460777V#540F（完、完全沉浸在二人世界中了啊。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A64')

    def _loc_29D9(): pass

    label('loc_29D9')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2A23',
    )

    ChrTalk(
        0x0104,
        (
            '#0040460778V#030F（呼～彻底沉浸在二人世界里了啊。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A64')

    def _loc_2A23(): pass

    label('loc_2A23')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2A64',
    )

    ChrTalk(
        0x0108,
        (
            '#0080460779V#070F（这就是所谓的二人世界吗。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2A64(): pass

    label('loc_2A64')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2AAA',
    )

    ChrTalk(
        0x0106,
        (
            '#0050460780V#552F（好像完全无视我们的存在呢。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2B71')

    def _loc_2AAA(): pass

    label('loc_2AAA')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2AF0',
    )

    ChrTalk(
        0x0108,
        (
            '#0080460781V#071F（哈哈，恋爱果然是盲目的呢。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2B71')

    def _loc_2AF0(): pass

    label('loc_2AF0')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2B36',
    )

    ChrTalk(
        0x0104,
        (
            '#0040460782V#031F（呵呵，恋爱果然是盲目的啊。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2B71')

    def _loc_2B36(): pass

    label('loc_2B36')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2B71',
    )

    ChrTalk(
        0x0105,
        (
            '#0060460783V#048F（不过……真不错呢。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2B71(): pass

    label('loc_2B71')

    ChrTalk(
        0x0103,
        (
            '#0030460784V#020F（咱们好像太打扰他们了……\n',
            '    还是赶快离开吧。)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010460811V#1013F（说、说的是啊。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460786V#1016F那、那么、\n',
            '我们这就走了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    OP_22(0x0017, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【消失在天空的定婚戒指】',
            (TxtCtl.SetColor, 0x0),
            '完成了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrFlags(0x000D, 0x0010)
    SetChrFlags(0x000E, 0x0010)
    OP_A2(0x0006)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
