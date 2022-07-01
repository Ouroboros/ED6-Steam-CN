import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T0701_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0701_1 ._SN')

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
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/T0701_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x2739
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
    SetChrPos(0x0101, 42160, 4000, 32689, 135)
    SetChrPos(0x0103, 41220, 4000, 31800, 90)
    SetChrPos(0x00F8, 41110, 4000, 32970, 135)
    SetChrPos(0x00F9, 42320, 4000, 33710, 135)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_122',
    )

    SetChrPos(0x00F9, 41110, 4000, 32970, 135)
    SetChrPos(0x00F8, 42320, 4000, 33710, 135)

    def _loc_122(): pass

    label('loc_122')

    ChrTurnDirection(0x00FE, 0x0101, 0)
    OP_6D(42900, 4000, 32590, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(
        0x00FE,
        (
            '#3460461068V真是厉害的雾啊。\n',
            '连工作服也湿透了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010461069V#1000F请问，打扰一下行吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010450897V向你询问一些事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3460461071V哦，什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '向他说明了正在寻找\n',
            '褐色猫的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x00FE,
        (
            '#3460461072V唔～猫啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3460461073V不巧我没看到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010461074V#1000F啊？是吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3460461075V看见那只猫的\n',
            '肯定是斯库拉特。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3460461076V你们去找他问问吧。\n',
            '他应该在仓库附近。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0074, 0x01, 0x0008)
    EventEnd(0x00)

    Return()

# id: 0x0001 offset: 0x318
@scena.Code('Init')
def Init():
    EventBegin(0x00)
    OP_8C(0x00FE, 135, 0)
    Fade(1000)
    SetChrPos(0x0101, 36380, 0, 50200, 90)
    SetChrPos(0x0103, 35330, 0, 49670, 90)
    SetChrPos(0x00F8, 34610, 0, 50660, 90)
    SetChrPos(0x00F9, 33650, 0, 49980, 90)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_399',
    )

    SetChrPos(0x00F9, 34610, 0, 50660, 90)
    SetChrPos(0x00F8, 33650, 0, 49980, 90)

    def _loc_399(): pass

    label('loc_399')

    OP_4A(0x00FE, 255)
    OP_6D(37130, 0, 50200, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(2950, 0)
    OP_6C(90000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(
        0x00FE,
        (
            '#3470461077V呼，好厉害的露水啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3470461078V这下可得想点\n',
            '厉害的办法对付湿气啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010461079V#1011F请问～打扰一下行吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010461080V我们有事想问你。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#3470461081V嗯？　什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '向他说明了正在寻找\n',
            '褐色猫的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x00FE,
        (
            '#3470461082V啊啊，那只猫啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3470461083V确实见过呢。\n',
            '今天中午的样子。',
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
        'loc_58A',
    )

    ChrTalk(
        0x0105,
        (
            '#0060461084V#040F中午……是吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_629')

    def _loc_58A(): pass

    label('loc_58A')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5BE',
    )

    ChrTalk(
        0x0107,
        (
            '#0070461085V#060F中午啊……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_629')

    def _loc_5BE(): pass

    label('loc_5BE')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5F6',
    )

    ChrTalk(
        0x0104,
        (
            '#0040461086V#030F唔，中午……吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_629')

    def _loc_5F6(): pass

    label('loc_5F6')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_629',
    )

    ChrTalk(
        0x0108,
        (
            '#0080461087V#070F唔，中午吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_629(): pass

    label('loc_629')

    ChrTalk(
        0x0101,
        (
            '#0010461088V#1002F……和伊娜阿姨的话\n',
            '恰好相符呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030461089V#020F那，之后那猫\n',
            '去了哪里知道吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3470461090V之后啊……\n',
            '到底去了哪里呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3470461091V从那之后也再没看见，\n',
            '完全没印象呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3470461092V怎么说猫这东西呢，\n',
            '真是种反复无常的生物嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010461093V#1016F嗯，这倒是没错……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010461094V#1015F不过，真伤脑筋啊。\n',
            '线索断了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3470461095V那就去问问\n',
            '库因特那家伙怎样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3470461096V刚刚吃完晚饭，\n',
            '好象出城了来着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030461097V#023F库因特先生？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3470461098V啊啊，赛希莉亚号的操舵手。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3470461099V那个家伙也说起过猫呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010461100V#1006F操舵手库因特先生吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8C5',
    )

    ChrTalk(
        0x0106,
        (
            '#0050461101V#050F赶快去找吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_965')

    def _loc_8C5(): pass

    label('loc_8C5')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8F9',
    )

    ChrTalk(
        0x0108,
        (
            '#0080461102V#070F赶快去找吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_965')

    def _loc_8F9(): pass

    label('loc_8F9')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_934',
    )

    ChrTalk(
        0x0104,
        (
            '#0040461103V#030F那么就赶快\n',
            '去找吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_965')

    def _loc_934(): pass

    label('loc_934')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_965',
    )

    ChrTalk(
        0x0105,
        (
            '#0060461104V#040F赶快去找吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_965(): pass

    label('loc_965')

    ChrTalk(
        0x0103,
        (
            '#0030461105V#020F……谢谢您提供线索。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3470461106V哪里，一点小事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0074, 0x01, 0x0010)
    OP_28(0x0074, 0x01, 0x0020)
    EventEnd(0x00)

    Return()

# id: 0x0002 offset: 0x9C1
@scena.Code('ReInit')
def ReInit():
    EventBegin(0x00)
    OP_8C(0x00FE, 180, 0)
    Fade(1000)
    SetChrPos(0x0101, 30460, 0, 3220, 270)
    SetChrPos(0x00F7, 31440, 0, 3750, 270)
    SetChrPos(0x00F8, 31360, 0, 2610, 270)
    SetChrPos(0x00F9, 32270, 0, 3270, 270)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A42',
    )

    SetChrPos(0x00F9, 31360, 0, 2610, 270)
    SetChrPos(0x00F8, 32270, 0, 3270, 270)

    def _loc_A42(): pass

    label('loc_A42')

    OP_6D(29790, 0, 2710, 0)
    OP_67(0, 6680, -10000, 0)
    OP_6B(2850, 0)
    OP_6C(213000, 0)
    OP_6E(262, 0)
    OP_4A(0x00FE, 255)
    OP_0D()

    ChrTalk(
        0x00FE,
        (
            '#3480461145V呼～真安静啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010461146V#1003F#4P啊……果然是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#3480461147V哎呀～怎么了～～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010461148V#1007F#4P正找你呢，索斯摩夫先生。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010461149V你躲在这里\n',
            '到底在干什么呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3480461150V这不是一看就知道了吗，\n',
            '在享受森林浴哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3480461151V呀，船上待久了，\n',
            '就开始怀念绿色了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3480461152V所以就经常像这样\n',
            '被树木包围享受一阵自然浴呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010461153V#1019F#4P好、好奇怪的习惯啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030461154V#026F啊啊，不管怎样\n',
            '找到就好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030461155V#020F好啦，赶快\n',
            '把事情办完吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010461156V#1002F#4P嗯、说的是呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010461157V#1015F……其实有些事\n',
            '想跟索斯摩夫先生打听一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3480461158V哦～～是什么事呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '向他说明了正在寻找\n',
            '褐色猫的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x00FE,
        (
            '#3480461159V咦～在找猫吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030461160V#020F从库因特先生那里\n',
            '听说您好像见过猫。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3480461161V嗯嗯～确实看见过哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3480461162V今天中午，卸货时\n',
            '看到在船舱里面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3480461163V喵喵叫着\n',
            '吵得厉害呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010461164V#1015F#4P船舱？也就是说……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010461165V#1002F猫在飞船里了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3480461166V船舱……这么说、\n',
            '一般是在飞船里面吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3480461167V再怎么联想\n',
            '也只能是那里了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_F49',
    )

    ChrTalk(
        0x0106,
        (
            '#0050461168V#051F#1P原来如此，飞船里啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050461169V怪不得找不到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1091')

    def _loc_F49(): pass

    label('loc_F49')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_FBA',
    )

    ChrTalk(
        0x0108,
        (
            '#0080461170V#070F#1P不过，定期船里面啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080461171V#071F哈哈，在外面找\n',
            '难怪找不到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1091')

    def _loc_FBA(): pass

    label('loc_FBA')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_101F',
    )

    ChrTalk(
        0x0104,
        (
            '#0040461172V#030F#1P没想到在定期船里面啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040461173V呼，怪不得找不到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1091')

    def _loc_101F(): pass

    label('loc_101F')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1091',
    )

    ChrTalk(
        0x0105,
        (
            '#0060461174V#043F#1P话说回来，\n',
            '真没想到会在定期船里面……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060461175V#047F怪不得找不到了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1091(): pass

    label('loc_1091')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_10CA',
    )

    ChrTalk(
        0x0107,
        (
            '#0070461176V#067F#1P嘿嘿，真是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1178')

    def _loc_10CA(): pass

    label('loc_10CA')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1103',
    )

    ChrTalk(
        0x0105,
        (
            '#0060461177V#040F#1P呵呵，真是的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1178')

    def _loc_1103(): pass

    label('loc_1103')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1142',
    )

    ChrTalk(
        0x0104,
        (
            '#0040461178V#030F#1P呼，真没办法……呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1178')

    def _loc_1142(): pass

    label('loc_1142')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1178',
    )

    ChrTalk(
        0x0108,
        (
            '#0080461179V#070F#1P哈哈，真是的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1178(): pass

    label('loc_1178')

    ChrTalk(
        0x0103,
        (
            '#0030461180V#020F不过……\n',
            '现在还不能太高兴哟。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030461181V赶快去请求许可，\n',
            '到飞船里调查看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010461182V#1006F#4P嗯，就这么定了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x00FE, 400)

    ChrTalk(
        0x0101,
        (
            '#0010461183V#1006F#4P那么，索斯摩夫先生。\n',
            '真是谢谢您了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3480461184V哈，这倒不必……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3480461185V嗯……那个……\n',
            '怎么说呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010461186V#1011F#4P？？？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010461187V怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030461188V#023F您刚才好像想说什么吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3480461189V嗯嗯，说出来\n',
            '可能比较为难……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3480461190V……大家在寻找的\n',
            '是『褐色』的猫吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010461191V#1011F#4P嗯，是这样的没错……\n',
            '…………………………',
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
            '#0010461192V#1004F#4P……唔，难不成！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3480461193V啊，明白了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3480461194V嗯嗯，是你想的那样的。\n',
            '其实我看见的猫……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3480461195V不是褐色，\n',
            '是『纯黑』的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_14A3',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)

    Jump('loc_14E1')

    def _loc_14A3(): pass

    label('loc_14A3')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_14CA',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)

    Jump('loc_14E1')

    def _loc_14CA(): pass

    label('loc_14CA')

    OP_62(0x00F8, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)

    def _loc_14E1(): pass

    label('loc_14E1')

    If(
        (
            (Expr.Eval, "OP_CB(0xF6)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1508',
    )

    OP_62(0x00F6, 0x00000000, 2300, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)

    Jump('loc_1546')

    def _loc_1508(): pass

    label('loc_1508')

    If(
        (
            (Expr.Eval, "OP_CB(0xF6)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_152F',
    )

    OP_62(0x00F6, 0x00000000, 1700, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)

    Jump('loc_1546')

    def _loc_152F(): pass

    label('loc_152F')

    OP_62(0x00F6, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)

    def _loc_1546(): pass

    label('loc_1546')

    Sleep(120)

    If(
        (
            (Expr.Eval, "OP_CB(0xF7)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1572',
    )

    OP_62(0x00F7, 0x00000000, 2300, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)

    Jump('loc_15B0')

    def _loc_1572(): pass

    label('loc_1572')

    If(
        (
            (Expr.Eval, "OP_CB(0xF7)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1599',
    )

    OP_62(0x00F7, 0x00000000, 1700, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)

    Jump('loc_15B0')

    def _loc_1599(): pass

    label('loc_1599')

    OP_62(0x00F7, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)

    def _loc_15B0(): pass

    label('loc_15B0')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_15D7',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)

    Jump('loc_1615')

    def _loc_15D7(): pass

    label('loc_15D7')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_15FE',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)

    Jump('loc_1615')

    def _loc_15FE(): pass

    label('loc_15FE')

    OP_62(0x00F9, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)

    def _loc_1615(): pass

    label('loc_1615')

    Sleep(2000)

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_165E',
    )

    ChrTalk(
        0x0106,
        (
            '#0050461196V#551F#1P喂，大叔……\n',
            '这你早说啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1721')

    def _loc_165E(): pass

    label('loc_165E')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_16A0',
    )

    ChrTalk(
        0x0108,
        (
            '#0080461197V#075F#1P呼，这应该\n',
            '早说才是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1721')

    def _loc_16A0(): pass

    label('loc_16A0')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_16E4',
    )

    ChrTalk(
        0x0104,
        (
            '#0040461198V#031F#1P哈哈哈。\n',
            '真是被你打败了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1721')

    def _loc_16E4(): pass

    label('loc_16E4')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1721',
    )

    ChrTalk(
        0x0105,
        (
            '#0060461199V#045F#1P完、完全\n',
            '吃了一惊了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1721(): pass

    label('loc_1721')

    ChrTalk(
        0x00FE,
        (
            '#3480461200V对不起啊……\n',
            '怎么都说不出口呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3480461201V不过，飞船里确实\n',
            '是有猫肯定没错……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3480461202V要不还是去调查一下看看？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010461203V#1007F#4P嗯，确实……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010461204V也不确定安莉尔\n',
            '一定不在那。',
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
        'loc_1864',
    )

    ChrTalk(
        0x0107,
        (
            '#0070370068V#560F#1P是，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070461206V那只黑猫，搞不好\n',
            '是安莉尔的朋友呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1864(): pass

    label('loc_1864')

    ChrTalk(
        0x0103,
        (
            '#0030461207V#025F嗯嗯，是啊……\n',
            '反正也没有其他线索……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030461208V#020F调整调整心情，\n',
            '然后去调查看看吧。',
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
        'loc_1911',
    )

    ChrTalk(
        0x0108,
        (
            '#0080461209V#070F#1P是啊……去看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19C4')

    def _loc_1911(): pass

    label('loc_1911')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1955',
    )

    ChrTalk(
        0x0104,
        (
            '#0040461210V#030F#1P唔，是啊。\n',
            '就当散个步啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19C4')

    def _loc_1955(): pass

    label('loc_1955')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1992',
    )

    ChrTalk(
        0x0106,
        (
            '#0050461211V#551F#1P啊啊，只能这样了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19C4')

    def _loc_1992(): pass

    label('loc_1992')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_19C4',
    )

    ChrTalk(
        0x0107,
        (
            '#0070461212V#560F#1P啊……好！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_19C4(): pass

    label('loc_19C4')

    OP_28(0x0074, 0x01, 0x0100)
    EventEnd(0x00)

    Return()

# id: 0x0003 offset: 0x19CD
@scena.Code('func_03_19CD')
def func_03_19CD():
    EventBegin(0x00)
    Fade(1000)
    SetChrPos(0x0101, 43090, 4000, 33470, 180)
    SetChrPos(0x0103, 42250, 4000, 34000, 180)
    SetChrPos(0x00F8, 42150, 4000, 35100, 180)
    SetChrPos(0x00F9, 43120, 4000, 34660, 180)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1A47',
    )

    SetChrPos(0x00F9, 42150, 4000, 35100, 180)
    SetChrPos(0x00F8, 43120, 4000, 34660, 180)

    def _loc_1A47(): pass

    label('loc_1A47')

    ChrTurnDirection(0x00FE, 0x0101, 0)
    OP_4A(0x00FE, 255)
    OP_6D(43090, 4000, 33130, 0)
    OP_67(0, 8370, -10000, 0)
    OP_6B(2930, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()

    If(
        (
            (Expr.Eval, "OP_29(0x0074, 0x01, 0x0008)"),
            Expr.Return,
        ),
        'loc_1AF9',
    )

    ChrTalk(
        0x00FE,
        (
            '#3460461213V哟，猫找到了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010461214V#1011F嗯，其实关于这个\n',
            '想麻烦您帮个忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1BAB')

    def _loc_1AF9(): pass

    label('loc_1AF9')

    ChrTalk(
        0x00FE,
        (
            '#3460461215V哟，怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3460461216V这么晚还在工作，\n',
            '你们也真辛苦的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010461217V#1016F嗯，彼此彼此啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010461218V#1000F别提这个了，关于工作\n',
            '想麻烦您帮个忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1BAB(): pass

    label('loc_1BAB')

    ChrTalk(
        0x00FE,
        (
            '#3460461219V咦，什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030461220V#020F#3P嗯嗯，希望能让我们\n',
            '到定期船里面调查一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3460461221V这就是说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3460461222V要进入这艘\n',
            '赛希莉亚号，是吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010461223V#1015F嗯，是这么回事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x0074, 0x01, 0x0008)"),
            Expr.Return,
        ),
        'loc_1D1D',
    )

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '说明之前的经过和调查状况，\n',
            '传达了可能有猫在飞船内的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x00FE,
        (
            '#3460461224V原来如此啊……\n',
            '事情倒是明白了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E25')

    def _loc_1D1D(): pass

    label('loc_1D1D')

    ChrTalk(
        0x00FE,
        (
            '#3460461225V但是，这不是说说\n',
            '就ＯＫ的事情啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3460461226V把相关的根据\n',
            '说给我听听吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010441823V#1002F嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '说明之前的经过和调查状况，\n',
            '传达了可能有猫在飞船内的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x00FE,
        (
            '#3460461228V原来如此啊……\n',
            '这么回事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1E25(): pass

    label('loc_1E25')

    ChrTalk(
        0x00FE,
        (
            '#3460461229V但是，这不是我一个人\n',
            '就能批准的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3460461230V……不好意思，请放弃吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010461231V#1019F呜……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010461232V好，好干脆的就\n',
            '被拒绝了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3460461233V不是我干脆，\n',
            '不可能就是不可能啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3460461234V再纠缠也是徒劳的，\n',
            '还是赶快回去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x00FE, 90, 400)
    Sleep(400)

    OP_8C(0x0101, 270, 400)

    ChrTalk(
        0x0101,
        (
            '#0010461235V#1003F唉……没办法了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030461236V#026F#3P哎呀──',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrFlags(0x00FE, 0x0040)
    SetChrFlags(0x0101, 0x0020)

    @scena.Lambda('lambda_1FA0')
    def lambda_1FA0():
        OP_8C(0x00FE, 180, 100)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1FA0)

    OP_8E(0x0103, 42680, 4000, 31800, 1000, 0x00)
    OP_8C(0x0103, 90, 400)
    WaitForThreadExit(0x0101, 0x0003)
    ClearChrFlags(0x0101, 0x0020)
    OP_62(0x0103, 0x00000000, 2000, 0x0A, 0x0B, 0x000000FA, 0x02)
    OP_22(0x000F, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0103,
        (
            '#0030461237V#520F#3P你真是的㈱\n',
            '干吗说得那么死板嘛㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x00)

    ChrTalk(
        0x00FE,
        (
            '#3460461238V哇哇……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_63(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#3460461239V那，那个……？',
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
        'loc_20C3',
    )

    OP_62(0x0104, 0x00000000, 2000, 0x0A, 0x0B, 0x000000FA, 0x02)
    OP_22(0x000F, 0x00, 0x64)
    Sleep(1000)

    OP_63(0x0104)

    ChrTalk(
        0x0104,
        (
            '#0040461240V#037F（这、这是！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_20C3(): pass

    label('loc_20C3')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_211B',
    )

    OP_62(0x0106, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(1000)

    OP_63(0x0106)

    ChrTalk(
        0x0106,
        (
            '#0050461241V#552F（终于出手了啊……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_211B(): pass

    label('loc_211B')

    ChrTalk(
        0x0103,
        (
            '#0030461242V#027F#3P听好了哦？\n',
            '请仔～细考虑一下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030461243V万一猫在船里，\n',
            '你们也会有麻烦吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030461244V座椅被抓坏了\n',
            '可怎么办那？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3460461245V这、这个……确实。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3460461246V但、但是，也不能\n',
            '因此就随便批准……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8E(0x0103, 42760, 4000, 31800, 1000, 0x00)

    ChrTalk(
        0x0103,
        (
            '#0030461247V#027F#3P没关系㈱\n',
            '不会给你们添麻烦的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030461248V只要稍微\n',
            '进去一下就行啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030461249V#525F所以拜托……了呢㈱\n',
            '……………（软玉温香）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_9E(0x00FE, 0x00000032, 0x00000000, 0x000001F4, 0x000005DC)

    ChrTalk(
        0x00FE,
        (
            '#3460461250V☆△×○☆～～！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010461251V#1013F（雪拉姐，碰到了。\n',
            '  碰到了啦……）',
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
        'loc_23B8',
    )

    OP_62(0x0104, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0104,
        (
            '#0040461252V#039F（啊啊啊啊───！\n',
            '  好羡慕──！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_23B8(): pass

    label('loc_23B8')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_23FC',
    )

    ChrTalk(
        0x0107,
        (
            '#0070461253V#562F（真、真是的～～\n',
            '  雪拉姐……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_23FC(): pass

    label('loc_23FC')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2435',
    )

    ChrTalk(
        0x0105,
        (
            '#0060461254V#540F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2435(): pass

    label('loc_2435')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2472',
    )

    ChrTalk(
        0x0106,
        (
            '#0050461255V#551F（真是的……真厉害啊。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2472(): pass

    label('loc_2472')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_24BE',
    )

    ChrTalk(
        0x0108,
        (
            '#0080461256V#071F（哈哈，事到如今\n',
            '  美人计也是绝招啊。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_24BE(): pass

    label('loc_24BE')

    OP_8F(0x0103, 42260, 4000, 31800, 1000, 0x00)

    ChrTalk(
        0x0103,
        (
            '#0030461257V#526F#3P……如何？\n',
            '明白了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x0A, 0x0B, 0x000000FA, 0x02)
    OP_22(0x000F, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x00FE, 0x0103, 400)

    ChrTalk(
        0x00FE,
        (
            '#3460461258V真，真没办法啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3460461259V那么，真的\n',
            '只是一小会儿哦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3460461260V以、以后这事\n',
            '绝对下不为例哦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030461261V#021F#3P呵呵，明白啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(500, 0, -1)
    OP_0D()
    OP_71(0x000A, 0x0004)
    OP_8C(0x00FE, 90, 0)
    ClearChrFlags(0x00FE, 0x0040)
    SetChrPos(0x00FE, 43100, 4000, 30900, 90)
    SetChrPos(0x0103, 42250, 4000, 34000, 180)
    Sleep(1000)

    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x00FE,
        (
            '#3460461262V──好，准备完成了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8E(0x00FE, 43080, 4000, 32060, 2000, 0x00)
    ChrTurnDirection(0x00FE, 0x0101, 400)
    SetChrFlags(0x00FE, 0x0010)

    ChrTalk(
        0x00FE,
        (
            '#3460461263V那么，麻烦尽快啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0074, 0x01, 0x0200)
    EventEnd(0x00)
    OP_8C(0x00FE, 270, 0)

    Return()

# id: 0x0004 offset: 0x268F
@scena.Code('func_04_268F')
def func_04_268F():
    If(
        (
            (Expr.Eval, "OP_29(0x0074, 0x01, 0x0200)"),
            (Expr.Eval, "OP_29(0x0074, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_26A4',
    )

    Return()

    def _loc_26A4(): pass

    label('loc_26A4')

    EventBegin(0x01)
    OP_4A(0x0009, 255)
    ChrTurnDirection(0x0009, 0x0000, 0)
    OP_6D(41340, 4000, 35650, 1000)

    ChrTalk(
        0x0009,
        (
            '#3460461264V喂喂！\n',
            '去哪里啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3460461265V请赶快\n',
            '去调查啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_90(0x0000, 1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)
    OP_4B(0x0009, 255)
    OP_8C(0x0009, 270, 0)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
