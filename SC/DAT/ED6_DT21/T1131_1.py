import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T1131_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T1131_1 ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'T1131.x'
    header.mapIndex       = 1
    header.bgm            = 11
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
    If(
        (
            (Expr.PushValueByIndex, 0x13),
            (Expr.PushLong, 0x381),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B5',
    )

    Return()

    def _loc_B5(): pass

    label('loc_B5')

    If(
        (
            (Expr.Eval, "OP_29(0x0079, 0x00, 0x10)"),
            (Expr.Eval, "OP_29(0x0079, 0x00, 0x40)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_C7',
    )

    Return()

    def _loc_C7(): pass

    label('loc_C7')

    MapSetFlags(0x00000080)
    OP_C0(0x01, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)
    Sleep(30)

    If(
        (
            (Expr.Eval, "OP_CD(0x0020)"),
            Expr.Return,
        ),
        'loc_102',
    )

    Call(0, 0x0023)

    Jump('loc_1DB')

    def _loc_102(): pass

    label('loc_102')

    If(
        (
            (Expr.Eval, "OP_CD(0x001B)"),
            Expr.Return,
        ),
        'loc_111',
    )

    Call(1, 0x0001)

    Jump('loc_1DB')

    def _loc_111(): pass

    label('loc_111')

    If(
        (
            (Expr.Eval, "OP_CD(0x03E8)"),
            Expr.Return,
        ),
        'loc_120',
    )

    Call(1, 0x0001)

    Jump('loc_1DB')

    def _loc_120(): pass

    label('loc_120')

    If(
        (
            (Expr.Eval, "OP_CD(0x0008)"),
            Expr.Return,
        ),
        'loc_12F',
    )

    Call(1, 0x0002)

    Jump('loc_1DB')

    def _loc_12F(): pass

    label('loc_12F')

    If(
        (
            (Expr.Eval, "OP_CD(0x00FF)"),
            Expr.Return,
        ),
        'loc_19D',
    )

    If(
        (
            (Expr.Eval, "OP_CD(0x001C)"),
            Expr.Return,
        ),
        'loc_142',
    )

    TalkBegin(0x001C)

    def _loc_142(): pass

    label('loc_142')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '试着出示了照片，\n',
            '但似乎没有见过的印象。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    If(
        (
            (Expr.Eval, "OP_CD(0x001C)"),
            Expr.Return,
        ),
        'loc_19A',
    )

    TalkEnd(0x001C)

    def _loc_19A(): pass

    label('loc_19A')

    Jump('loc_1DB')

    def _loc_19D(): pass

    label('loc_19D')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '附近没有人可以确认照片。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    def _loc_1DB(): pass

    label('loc_1DB')

    OP_0D()
    MapClearFlags(0x00000080)

    Return()

# id: 0x0001 offset: 0x1E2
@scena.Code('func_01_1E2')
def func_01_1E2():
    TalkBegin(0x001B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0003, 2, 0x1A)),
            Expr.Return,
        ),
        'loc_237',
    )

    ChrTalk(
        0x001B,
        (
            '#3800490591V不好意思，我没印象呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001B,
        (
            '#3800490592V问问其他人吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2C1')

    def _loc_237(): pass

    label('loc_237')

    ChrTalk(
        0x001B,
        (
            '#3800490588V啊啊，找人吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001B,
        (
            '#3800490589V好可爱的女孩啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001B,
        (
            '#3800490590V这孩子的父母因为战争去世了啊。\n',
            '战争果然是场错误啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0003, 2, 0x1A))

    def _loc_2C1(): pass

    label('loc_2C1')

    TalkEnd(0x001B)

    Return()

# id: 0x0002 offset: 0x2C5
@scena.Code('func_02_2C5')
def func_02_2C5():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_33E',
    )

    ChrTalk(
        0x0008,
        (
            '#3810490597V那照片中少女的眼睛……\n',
            '感觉似乎在哪里见过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3810490596V本店的客人中\n',
            '有这样的人吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3FA')

    def _loc_33E(): pass

    label('loc_33E')

    ChrTalk(
        0x0008,
        (
            '#3810490593V唔，寻找失踪的人吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3810490594V真不巧，我似乎\n',
            '没有见过的印象……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3810490595V……这绿色的眼睛\n',
            '含着某种牵挂。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3810490596V本店的客人中\n',
            '有这样的人吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_3FA(): pass

    label('loc_3FA')

    TalkEnd(0x0008)

    Return()

# id: 0x0003 offset: 0x3FE
@scena.Code('func_03_3FE')
def func_03_3FE():
    EventBegin(0x00)
    Fade(1000)
    ChrSetDirection(0x0020, 270, 0)
    ChrSetPos(0x0101, 1120, 0, 1500, 90)

    If(
        (
            (Expr.Eval, "OP_CB(0xF7)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_460',
    )

    ChrSetPos(0x00F8, 1000, 0, 110, 32)
    ChrSetPos(0x00F7, 10, 0, 1520, 90)
    ChrSetPos(0x00F9, -120, 0, 490, 90)

    Jump('loc_519')

    def _loc_460(): pass

    label('loc_460')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4A3',
    )

    ChrSetPos(0x00F7, 1000, 0, 110, 32)
    ChrSetPos(0x00F8, 10, 0, 1520, 90)
    ChrSetPos(0x00F9, -120, 0, 490, 90)

    Jump('loc_519')

    def _loc_4A3(): pass

    label('loc_4A3')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4E6',
    )

    ChrSetPos(0x00F7, 1000, 0, 110, 32)
    ChrSetPos(0x00F9, 10, 0, 1520, 90)
    ChrSetPos(0x00F8, -120, 0, 490, 90)

    Jump('loc_519')

    def _loc_4E6(): pass

    label('loc_4E6')

    ChrSetPos(0x00F7, 1000, 0, 110, 32)
    ChrSetPos(0x00F8, -120, 0, 490, 90)
    ChrSetPos(0x00F9, 10, 0, 1520, 90)

    def _loc_519(): pass

    label('loc_519')

    CameraMove(780, 0, 1170, 0)
    OP_67(0, 6150, -10000, 0)
    CameraSetDistance(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010370608V#1011F请问～打扰一下行吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3720490352V好，什么事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010490353V#1000F您是科尔娜女士吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010490354V我们是\n',
            '游击士协会的人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3720490355V呀，你们可来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3720490356V正等着你们呢。\n',
            '我就是提出委托的科尔娜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010490357V#1011F啊，幸会。\n',
            '我是游击士艾丝蒂尔·布莱特。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3720490358V突然叫你们来\n',
            '真是不好意思……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3720490359V但是靠我一个人的力量\n',
            '已经毫无办法了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3720490360V总之拜托你们先\n',
            '听听我的苦衷好吗？',
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
        'loc_7A1',
    )

    ChrTalk(
        0x0101,
        (
            '#0010451028V#1006F嗯，没问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(1, 0x0005)

    Jump('loc_895')

    def _loc_7A1(): pass

    label('loc_7A1')

    ChrTalk(
        0x0101,
        (
            '#0010490362V#1007F唔～实在对不起。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010490363V现在有点不方便。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3720490364V呀，这样吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3720490365V嗯，那么\n',
            '就请你们方便的时候，\n',
            '再过来找我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3720490366V我会在这里等你们的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010490367V#1000F嗯，知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0079, 0x01, 0x8000)

    def _loc_895(): pass

    label('loc_895')

    EventEnd(0x00)

    Return()

# id: 0x0004 offset: 0x898
@scena.Code('func_04_898')
def func_04_898():
    EventBegin(0x00)
    Fade(1000)
    ChrSetDirection(0x0020, 270, 0)
    ChrSetPos(0x0101, 1120, 0, 1500, 90)

    If(
        (
            (Expr.Eval, "OP_CB(0xF7)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8FA',
    )

    ChrSetPos(0x00F8, 1000, 0, 110, 32)
    ChrSetPos(0x00F7, 10, 0, 1520, 90)
    ChrSetPos(0x00F9, -120, 0, 490, 90)

    Jump('loc_9B3')

    def _loc_8FA(): pass

    label('loc_8FA')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_93D',
    )

    ChrSetPos(0x00F7, 1000, 0, 110, 32)
    ChrSetPos(0x00F8, 10, 0, 1520, 90)
    ChrSetPos(0x00F9, -120, 0, 490, 90)

    Jump('loc_9B3')

    def _loc_93D(): pass

    label('loc_93D')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_980',
    )

    ChrSetPos(0x00F7, 1000, 0, 110, 32)
    ChrSetPos(0x00F9, 10, 0, 1520, 90)
    ChrSetPos(0x00F8, -120, 0, 490, 90)

    Jump('loc_9B3')

    def _loc_980(): pass

    label('loc_980')

    ChrSetPos(0x00F7, 1000, 0, 110, 32)
    ChrSetPos(0x00F8, -120, 0, 490, 90)
    ChrSetPos(0x00F9, 10, 0, 1520, 90)

    def _loc_9B3(): pass

    label('loc_9B3')

    CameraMove(780, 0, 1170, 0)
    OP_67(0, 6150, -10000, 0)
    CameraSetDistance(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_0D()

    ChrTalk(
        0x00FE,
        (
            '#3720490368V哎呀，各位游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3720490369V这下方便了吗？',
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
        'loc_AB3',
    )

    ChrTalk(
        0x0101,
        (
            '#0010451035V#1006F嗯，没问题了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(1, 0x0005)

    Jump('loc_B2F')

    def _loc_AB3(): pass

    label('loc_AB3')

    ChrTalk(
        0x0101,
        (
            '#0010490371V#1007F唔～抱歉哦。\n',
            '还没什么空闲。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010490372V方便的时候\n',
            '再来找你吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3720490373V嗯，那就拜托了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B2F(): pass

    label('loc_B2F')

    EventEnd(0x00)

    Return()

# id: 0x0005 offset: 0xB32
@scena.Code('func_05_B32')
def func_05_B32():
    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B91',
    )

    ChrTalk(
        0x0103,
        (
            '#0030490374V#020F这么多人别站着说话吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030490375V先坐下来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    Jump('loc_D49')

    def _loc_B91(): pass

    label('loc_B91')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_BF4',
    )

    ChrTalk(
        0x0106,
        (
            '#0050490376V#050F这么多人别站着说话。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050490377V先找地方坐下来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0106, 400)

    Jump('loc_D49')

    def _loc_BF4(): pass

    label('loc_BF4')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C62',
    )

    ChrTalk(
        0x0108,
        (
            '#0080490378V#070F这么一堆人别站着说话。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080490379V先坐下来，\n',
            '然后再慢慢说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0108, 400)

    Jump('loc_D49')

    def _loc_C62(): pass

    label('loc_C62')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_CE1',
    )

    ChrTalk(
        0x0105,
        (
            '#0060490380V#040F站着说话不太好吧，\n',
            '不先找地方坐下吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060490381V这么多人\n',
            '会给店里添麻烦的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0105, 400)

    Jump('loc_D49')

    def _loc_CE1(): pass

    label('loc_CE1')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D49',
    )

    ChrTalk(
        0x0104,
        (
            '#0040490382V#030F唔，不过站着说话不太好吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040490383V不先找地方坐下来吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0104, 400)

    def _loc_D49(): pass

    label('loc_D49')

    ChrTalk(
        0x0101,
        (
            '#0010490384V#1000F啊，是呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010490385V那就找个地方\n',
            '先坐下来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    ChrSetFlags(0x0038, 0x0080)
    OP_4A(0x0020, 255)
    ChrSetChipByIndex(0x0020, 6)
    ChrSetFlags(0x0020, 0x0004)
    ChrSetPos(0x0020, 3800, 120, -3550, 0)
    LoadChip('ED6_DT27/CH03003._CH', 'ED6_DT27/CH03003P._CP', 36)

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF7)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_DF0'),
        (0x00000003, 'loc_DFD'),
        (0x00000004, 'loc_E0A'),
        (0x00000005, 'loc_E17'),
        (0x00000006, 'loc_E24'),
        (0x00000007, 'loc_E31'),
        (0x00000008, 'loc_E3E'),
        (-1, 'loc_E4B'),
    )

    def _loc_DF0(): pass

    label('loc_DF0')

    LoadChip('ED6_DT07/CH00023._CH', 'ED6_DT07/CH00023P._CP', 37)

    Jump('loc_E4B')

    def _loc_DFD(): pass

    label('loc_DFD')

    LoadChip('ED6_DT07/CH00033._CH', 'ED6_DT07/CH00033P._CP', 37)

    Jump('loc_E4B')

    def _loc_E0A(): pass

    label('loc_E0A')

    LoadChip('ED6_DT07/CH00043._CH', 'ED6_DT07/CH00043P._CP', 37)

    Jump('loc_E4B')

    def _loc_E17(): pass

    label('loc_E17')

    LoadChip('ED6_DT07/CH00053._CH', 'ED6_DT07/CH00053P._CP', 37)

    Jump('loc_E4B')

    def _loc_E24(): pass

    label('loc_E24')

    LoadChip('ED6_DT07/CH00063._CH', 'ED6_DT07/CH00063P._CP', 37)

    Jump('loc_E4B')

    def _loc_E31(): pass

    label('loc_E31')

    LoadChip('ED6_DT07/CH00073._CH', 'ED6_DT07/CH00073P._CP', 37)

    Jump('loc_E4B')

    def _loc_E3E(): pass

    label('loc_E3E')

    LoadChip('ED6_DT27/CH03083._CH', 'ED6_DT27/CH03083P._CP', 37)

    Jump('loc_E4B')

    def _loc_E4B(): pass

    label('loc_E4B')

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_E70'),
        (0x00000003, 'loc_E7D'),
        (0x00000004, 'loc_E8A'),
        (0x00000005, 'loc_E97'),
        (0x00000006, 'loc_EA4'),
        (0x00000007, 'loc_EB1'),
        (0x00000008, 'loc_EBE'),
        (-1, 'loc_ECB'),
    )

    def _loc_E70(): pass

    label('loc_E70')

    LoadChip('ED6_DT07/CH00023._CH', 'ED6_DT07/CH00023P._CP', 38)

    Jump('loc_ECB')

    def _loc_E7D(): pass

    label('loc_E7D')

    LoadChip('ED6_DT07/CH00033._CH', 'ED6_DT07/CH00033P._CP', 38)

    Jump('loc_ECB')

    def _loc_E8A(): pass

    label('loc_E8A')

    LoadChip('ED6_DT07/CH00043._CH', 'ED6_DT07/CH00043P._CP', 38)

    Jump('loc_ECB')

    def _loc_E97(): pass

    label('loc_E97')

    LoadChip('ED6_DT07/CH00053._CH', 'ED6_DT07/CH00053P._CP', 38)

    Jump('loc_ECB')

    def _loc_EA4(): pass

    label('loc_EA4')

    LoadChip('ED6_DT07/CH00063._CH', 'ED6_DT07/CH00063P._CP', 38)

    Jump('loc_ECB')

    def _loc_EB1(): pass

    label('loc_EB1')

    LoadChip('ED6_DT07/CH00073._CH', 'ED6_DT07/CH00073P._CP', 38)

    Jump('loc_ECB')

    def _loc_EBE(): pass

    label('loc_EBE')

    LoadChip('ED6_DT27/CH03083._CH', 'ED6_DT27/CH03083P._CP', 38)

    Jump('loc_ECB')

    def _loc_ECB(): pass

    label('loc_ECB')

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_EF0'),
        (0x00000003, 'loc_EFD'),
        (0x00000004, 'loc_F0A'),
        (0x00000005, 'loc_F17'),
        (0x00000006, 'loc_F24'),
        (0x00000007, 'loc_F31'),
        (0x00000008, 'loc_F3E'),
        (-1, 'loc_F4B'),
    )

    def _loc_EF0(): pass

    label('loc_EF0')

    LoadChip('ED6_DT07/CH00023._CH', 'ED6_DT07/CH00023P._CP', 39)

    Jump('loc_F4B')

    def _loc_EFD(): pass

    label('loc_EFD')

    LoadChip('ED6_DT07/CH00033._CH', 'ED6_DT07/CH00033P._CP', 39)

    Jump('loc_F4B')

    def _loc_F0A(): pass

    label('loc_F0A')

    LoadChip('ED6_DT07/CH00043._CH', 'ED6_DT07/CH00043P._CP', 39)

    Jump('loc_F4B')

    def _loc_F17(): pass

    label('loc_F17')

    LoadChip('ED6_DT07/CH00053._CH', 'ED6_DT07/CH00053P._CP', 39)

    Jump('loc_F4B')

    def _loc_F24(): pass

    label('loc_F24')

    LoadChip('ED6_DT07/CH00063._CH', 'ED6_DT07/CH00063P._CP', 39)

    Jump('loc_F4B')

    def _loc_F31(): pass

    label('loc_F31')

    LoadChip('ED6_DT07/CH00073._CH', 'ED6_DT07/CH00073P._CP', 39)

    Jump('loc_F4B')

    def _loc_F3E(): pass

    label('loc_F3E')

    LoadChip('ED6_DT27/CH03083._CH', 'ED6_DT27/CH03083P._CP', 39)

    Jump('loc_F4B')

    def _loc_F4B(): pass

    label('loc_F4B')

    ChrSetChipByIndex(0x0101, 36)
    ChrSetChipByIndex(0x00F7, 37)
    ChrSetChipByIndex(0x00F8, 38)
    ChrSetChipByIndex(0x00F9, 39)
    ChrSetFlags(0x0101, 0x0004)
    ChrSetFlags(0x00F7, 0x0004)
    ChrSetFlags(0x00F8, 0x0004)
    ChrSetFlags(0x00F9, 0x0004)
    ChrSetPos(0x0101, 2760, 200, -2500, 90)

    If(
        (
            (Expr.Eval, "OP_CB(0xF7)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_FAF',
    )

    ChrSetPos(0x00F7, 5100, 100, -950, 270)

    ExecExpressionWithReg(
        0x0007,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1059')

    def _loc_FAF(): pass

    label('loc_FAF')

    ChrSetPos(0x00F7, 5100, 200, -950, 270)

    If(
        (
            (Expr.Eval, "OP_CB(0xF7)"),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_FDA',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1059')

    def _loc_FDA(): pass

    label('loc_FDA')

    If(
        (
            (Expr.Eval, "OP_CB(0xF7)"),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_FF4',
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1059')

    def _loc_FF4(): pass

    label('loc_FF4')

    If(
        (
            (Expr.Eval, "OP_CB(0xF7)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_100E',
    )

    ExecExpressionWithReg(
        0x0004,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1059')

    def _loc_100E(): pass

    label('loc_100E')

    If(
        (
            (Expr.Eval, "OP_CB(0xF7)"),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1028',
    )

    ExecExpressionWithReg(
        0x0005,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1059')

    def _loc_1028(): pass

    label('loc_1028')

    If(
        (
            (Expr.Eval, "OP_CB(0xF7)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1042',
    )

    ExecExpressionWithReg(
        0x0006,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1059')

    def _loc_1042(): pass

    label('loc_1042')

    If(
        (
            (Expr.Eval, "OP_CB(0xF7)"),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1059',
    )

    ExecExpressionWithReg(
        0x0008,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1059(): pass

    label('loc_1059')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1084',
    )

    ChrSetPos(0x00F8, 5100, 100, -2550, 270)

    ExecExpressionWithReg(
        0x0007,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_112E')

    def _loc_1084(): pass

    label('loc_1084')

    ChrSetPos(0x00F8, 5100, 200, -2550, 270)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_10AF',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_112E')

    def _loc_10AF(): pass

    label('loc_10AF')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_10C9',
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_112E')

    def _loc_10C9(): pass

    label('loc_10C9')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_10E3',
    )

    ExecExpressionWithReg(
        0x0004,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_112E')

    def _loc_10E3(): pass

    label('loc_10E3')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_10FD',
    )

    ExecExpressionWithReg(
        0x0005,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_112E')

    def _loc_10FD(): pass

    label('loc_10FD')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1117',
    )

    ExecExpressionWithReg(
        0x0006,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_112E')

    def _loc_1117(): pass

    label('loc_1117')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_112E',
    )

    ExecExpressionWithReg(
        0x0008,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_112E(): pass

    label('loc_112E')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1159',
    )

    ChrSetPos(0x00F9, 2900, 100, -900, 90)

    ExecExpressionWithReg(
        0x0007,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1203')

    def _loc_1159(): pass

    label('loc_1159')

    ChrSetPos(0x00F9, 2900, 200, -900, 90)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1184',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1203')

    def _loc_1184(): pass

    label('loc_1184')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_119E',
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1203')

    def _loc_119E(): pass

    label('loc_119E')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_11B8',
    )

    ExecExpressionWithReg(
        0x0004,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1203')

    def _loc_11B8(): pass

    label('loc_11B8')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_11D2',
    )

    ExecExpressionWithReg(
        0x0005,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1203')

    def _loc_11D2(): pass

    label('loc_11D2')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_11EC',
    )

    ExecExpressionWithReg(
        0x0006,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1203')

    def _loc_11EC(): pass

    label('loc_11EC')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1203',
    )

    ExecExpressionWithReg(
        0x0008,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1203(): pass

    label('loc_1203')

    CameraMove(3330, 0, -1410, 0)
    ChrSetSubChip(0x0101, 2)
    ChrSetSubChip(0x00F9, 2)
    ChrSetSubChip(0x00F7, 1)
    ChrSetSubChip(0x00F8, 1)
    FadeIn(1000, 0)
    OP_0D()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_12A4',
    )

    ChrTalk(
        0x0106,
        (
            '#0050490386V#050F看了公告板，\n',
            '您好像要找人啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050490387V说是１０年前\n',
            '就失踪了什么的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_147C')

    def _loc_12A4(): pass

    label('loc_12A4')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1316',
    )

    ChrTalk(
        0x0103,
        (
            '#0030490388V#022F看了公告板，\n',
            '您好像要找人吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030490389V说是１０年前\n',
            '就失踪了什么的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_147C')

    def _loc_1316(): pass

    label('loc_1316')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1388',
    )

    ChrTalk(
        0x0108,
        (
            '#0080490390V#070F看了公告板，\n',
            '您好像要找人啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080490391V说是１０年前\n',
            '就失踪了什么的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_147C')

    def _loc_1388(): pass

    label('loc_1388')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_13FE',
    )

    ChrTalk(
        0x0105,
        (
            '#0060490392V#043F看了公告板，\n',
            '您好像要找什么人吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060490393V说是１０年前\n',
            '就失踪了什么的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_147C')

    def _loc_13FE(): pass

    label('loc_13FE')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_147C',
    )

    ChrTalk(
        0x0109,
        (
            '#0180490394V#1063F那么，就开门见山的说吧……\n',
            '您好像要找人吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180490395V说是１０年前\n',
            '就失踪了什么的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_147C(): pass

    label('loc_147C')

    ChrTalk(
        0x00FE,
        (
            '#3720490396V是，其实……\n',
            '我在寻找我侄女。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3720490397V她名叫蕾妮……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3720490398V如果平安无事，\n',
            '现在应该２０岁了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 1700, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(1000)

    OP_63(0x0101)

    ChrTalk(
        0x0101,
        (
            '#0010490399V#1015F如果平安无事……？',
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
        'loc_15AB',
    )

    ChrTalk(
        0x0106,
        (
            '#0050211830V#053F原来如此啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050490401V#552F总算明白\n',
            '１０年前的意思了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1731')

    def _loc_15AB(): pass

    label('loc_15AB')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_160D',
    )

    ChrTalk(
        0x0103,
        (
            '#0030490402V#026F原来如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030490403V#522F总算明白\n',
            '１０年前的意思了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1731')

    def _loc_160D(): pass

    label('loc_160D')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1673',
    )

    ChrTalk(
        0x0108,
        (
            '#0080490404V#074F呼，原来如此啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080490405V#072F总算明白\n',
            '10年前的意思了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1731')

    def _loc_1673(): pass

    label('loc_1673')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_16D8',
    )

    ChrTalk(
        0x0104,
        (
            '#0040490406V#032F唔，原来如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040490407V总算明白了。\n',
            '１０年前的意义了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1731')

    def _loc_16D8(): pass

    label('loc_16D8')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1731',
    )

    ChrTalk(
        0x0107,
        (
            '#0070490408V#065F难，难不成……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070490409V从现在算起１０年前是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1731(): pass

    label('loc_1731')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_17A6',
    )

    ChrTalk(
        0x0109,
        (
            '#0180490410V#1065F……………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180490411V听爷爷说那时发生一场『百日战役』……吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1897')

    def _loc_17A6(): pass

    label('loc_17A6')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_17E4',
    )

    ChrTalk(
        0x0105,
        (
            '#0060490412V#042F『百日战役』……对吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1897')

    def _loc_17E4(): pass

    label('loc_17E4')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1822',
    )

    ChrTalk(
        0x0107,
        (
            '#0070490413V#063F『百日战役』……对吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1897')

    def _loc_1822(): pass

    label('loc_1822')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_185E',
    )

    ChrTalk(
        0x0104,
        (
            '#0040490414V#032F『百日战役』……吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1897')

    def _loc_185E(): pass

    label('loc_185E')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1897',
    )

    ChrTalk(
        0x0108,
        (
            '#0080490415V#072F『百日战役』……啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1897(): pass

    label('loc_1897')

    ChrTalk(
        0x0101,
        (
            '#0010490416V#1026F……啊……………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3720490417V……是，正如你们所说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3720490418V当时，我姐姐一家\n',
            '还住在这个城市……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3720490419V不幸卷入了\n',
            '那场突如其来的战火。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3720490420V不久我便通过熟人的关系\n',
            '得知了姐姐夫妇的死讯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3720490421V而１０岁的蕾妮\n',
            '至今仍去向不明。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3720490422V从那以来过了１０年……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3720490423V我们也完全\n',
            '死心了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3720490424V然而，最近\n',
            '却有了新的消息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3720490425V有人说当时\n',
            '『蕾妮被寄养在当地人家里』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010490426V#1004F这、这么说，\n',
            '蕾妮还活着吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3720490427V这就……不清楚了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3720490428V因为连寄养的人家\n',
            '的名字也都不知道。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010490429V#1007F啊……\n',
            '这，这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3720490430V但是，我相信。\n',
            '那女孩一定还活着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3720490431V正因为这样相信\n',
            '才会请求各位协助。',
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
        'loc_1C5C',
    )

    ChrTalk(
        0x0106,
        (
            '#0050490432V#050F……事情我们明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050490433V确实有调查的价值啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1C2B',
    )

    ChrSetSubChip(0x0101, 1)
    ChrSetSubChip(0x00F8, 2)
    ChrSetSubChip(0x00F9, 0)

    Jump('loc_1C59')

    def _loc_1C2B(): pass

    label('loc_1C2B')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1C4A',
    )

    ChrSetSubChip(0x0101, 0)
    ChrSetSubChip(0x00F7, 1)
    ChrSetSubChip(0x00F9, 2)

    Jump('loc_1C59')

    def _loc_1C4A(): pass

    label('loc_1C4A')

    ChrSetSubChip(0x0101, 1)
    ChrSetSubChip(0x00F7, 0)
    ChrSetSubChip(0x00F8, 2)

    def _loc_1C59(): pass

    label('loc_1C59')

    Jump('loc_1F09')

    def _loc_1C5C(): pass

    label('loc_1C5C')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1D07',
    )

    ChrTalk(
        0x0103,
        (
            '#0030490434V#022F……事情我们明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030490435V确实有调查的价值呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1CD6',
    )

    ChrSetSubChip(0x0101, 1)
    ChrSetSubChip(0x00F8, 2)
    ChrSetSubChip(0x00F9, 0)

    Jump('loc_1D04')

    def _loc_1CD6(): pass

    label('loc_1CD6')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1CF5',
    )

    ChrSetSubChip(0x0101, 0)
    ChrSetSubChip(0x00F7, 1)
    ChrSetSubChip(0x00F9, 2)

    Jump('loc_1D04')

    def _loc_1CF5(): pass

    label('loc_1CF5')

    ChrSetSubChip(0x0101, 1)
    ChrSetSubChip(0x00F7, 0)
    ChrSetSubChip(0x00F8, 2)

    def _loc_1D04(): pass

    label('loc_1D04')

    Jump('loc_1F09')

    def _loc_1D07(): pass

    label('loc_1D07')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1DAE',
    )

    ChrTalk(
        0x0108,
        (
            '#0080490436V#070F……事情明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080490437V确实有调查的价值啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushReg, 0x7),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1D7D',
    )

    ChrSetSubChip(0x0101, 1)
    ChrSetSubChip(0x00F8, 2)
    ChrSetSubChip(0x00F9, 0)

    Jump('loc_1DAB')

    def _loc_1D7D(): pass

    label('loc_1D7D')

    If(
        (
            (Expr.PushReg, 0x7),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1D9C',
    )

    ChrSetSubChip(0x0101, 0)
    ChrSetSubChip(0x00F7, 1)
    ChrSetSubChip(0x00F9, 2)

    Jump('loc_1DAB')

    def _loc_1D9C(): pass

    label('loc_1D9C')

    ChrSetSubChip(0x0101, 1)
    ChrSetSubChip(0x00F7, 0)
    ChrSetSubChip(0x00F8, 2)

    def _loc_1DAB(): pass

    label('loc_1DAB')

    Jump('loc_1F09')

    def _loc_1DAE(): pass

    label('loc_1DAE')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1E55',
    )

    ChrTalk(
        0x0104,
        (
            '#0040490438V#032F……事情明白啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040490439V确实有调查的价值呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1E24',
    )

    ChrSetSubChip(0x0101, 1)
    ChrSetSubChip(0x00F8, 2)
    ChrSetSubChip(0x00F9, 0)

    Jump('loc_1E52')

    def _loc_1E24(): pass

    label('loc_1E24')

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1E43',
    )

    ChrSetSubChip(0x0101, 0)
    ChrSetSubChip(0x00F7, 1)
    ChrSetSubChip(0x00F9, 2)

    Jump('loc_1E52')

    def _loc_1E43(): pass

    label('loc_1E43')

    ChrSetSubChip(0x0101, 1)
    ChrSetSubChip(0x00F7, 0)
    ChrSetSubChip(0x00F8, 2)

    def _loc_1E52(): pass

    label('loc_1E52')

    Jump('loc_1F09')

    def _loc_1E55(): pass

    label('loc_1E55')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1F09',
    )

    ChrTalk(
        0x0109,
        (
            '#0180490440V#1060F……好啦，事情搞清楚了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180490441V看来这确实\n',
            '有调查的价值呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushReg, 0x8),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1EDB',
    )

    ChrSetSubChip(0x0101, 1)
    ChrSetSubChip(0x00F8, 2)
    ChrSetSubChip(0x00F9, 0)

    Jump('loc_1F09')

    def _loc_1EDB(): pass

    label('loc_1EDB')

    If(
        (
            (Expr.PushReg, 0x8),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1EFA',
    )

    ChrSetSubChip(0x0101, 0)
    ChrSetSubChip(0x00F7, 1)
    ChrSetSubChip(0x00F9, 2)

    Jump('loc_1F09')

    def _loc_1EFA(): pass

    label('loc_1EFA')

    ChrSetSubChip(0x0101, 1)
    ChrSetSubChip(0x00F7, 0)
    ChrSetSubChip(0x00F8, 2)

    def _loc_1F09(): pass

    label('loc_1F09')

    ChrTalk(
        0x0101,
        (
            '#0010490442V#1015F不过，\n',
            '线索实在少了点呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010490443V现在所知道的\n',
            '只有她的姓名和年龄哦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3720490444V那……这样的话\n',
            '请收下这张照片。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0101, 2)
    Sleep(50)

    ChrSetSubChip(0x00F7, 1)
    Sleep(50)

    ChrSetSubChip(0x00F9, 2)
    ChrSetSubChip(0x00F8, 1)

    ChrTalk(
        0x0101,
        (
            '#0010490445V#1011F照片里……是蕾妮？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3720490446V嗯，就是她……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    OP_AD('ED6_DT24/C_VIS123._CH', 0x0000, 0x0000, 0x000001F4)
    Sleep(1000)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_206F',
    )

    SetMessageWindowPos(50, 50, -1, -1)
    TalkSetChrName('提妲')

    Talk(
        (
            '#0070490447V#560F哇，真可爱的女孩子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_2241')

    def _loc_206F(): pass

    label('loc_206F')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_20C0',
    )

    SetMessageWindowPos(50, 50, -1, -1)
    TalkSetChrName('科洛丝')

    Talk(
        (
            '#0060490448V#048F呵呵，是个可爱的女孩子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_2241')

    def _loc_20C0(): pass

    label('loc_20C0')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_210F',
    )

    SetMessageWindowPos(50, 50, -1, -1)
    TalkSetChrName('雪拉扎德')

    Talk(
        (
            '#0030490449V#526F啊，不是可爱的女孩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_2241')

    def _loc_210F(): pass

    label('loc_210F')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2202',
    )

    SetMessageWindowPos(50, 50, -1, -1)
    TalkSetChrName('奥利维尔')

    Talk(
        (
            '#0040490450V#033F嗯，相当有潜力啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040490451V#037F呼呼呼……\n',
            '现在的样子真值得期待。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(50, 340, -1, -1)
    TalkSetChrName('艾丝蒂尔')

    Talk(
        (
            '#0010490452V#1019F你，你的感想\n',
            '怎么就这么直白啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010490453V#1000F不过，真的很可爱呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_2241')

    def _loc_2202(): pass

    label('loc_2202')

    SetMessageWindowPos(50, 50, -1, -1)
    TalkSetChrName('艾丝蒂尔')

    Talk(
        (
            '#0010490454V#1018F真是个可爱的女孩子㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_2241(): pass

    label('loc_2241')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_22B3',
    )

    SetMessageWindowPos(360, 340, -1, -1)
    TalkSetChrName('凯文神父')

    Talk(
        (
            '#0180490455V#1062F啊哈哈，真的吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180490456V大概１０岁左右的样子吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_245A')

    def _loc_22B3(): pass

    label('loc_22B3')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2318',
    )

    SetMessageWindowPos(360, 340, -1, -1)
    TalkSetChrName('金')

    Talk(
        (
            '#0080490457V#070F哈哈，没有错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080490458V１０岁左右的样子吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_245A')

    def _loc_2318(): pass

    label('loc_2318')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2381',
    )

    SetMessageWindowPos(360, 340, -1, -1)
    TalkSetChrName('阿加特')

    Talk(
        (
            '#0050490459V#051F啊啊，看来没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050490460V大概１０岁左右吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_245A')

    def _loc_2381(): pass

    label('loc_2381')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_23F4',
    )

    SetMessageWindowPos(360, 340, -1, -1)
    TalkSetChrName('奥利维尔')

    Talk(
        (
            '#0040490461V#037F是呀，我也有同感。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040490462V唔，１０岁左右的样子吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_245A')

    def _loc_23F4(): pass

    label('loc_23F4')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_245A',
    )

    SetMessageWindowPos(360, 50, -1, -1)
    TalkSetChrName('雪拉扎德')

    ChrTalk(
        0x0103,
        (
            '#0030490463V#021F呵呵，真的是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030490464V１０岁左右吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_245A(): pass

    label('loc_245A')

    SetMessageWindowPos(50, 340, -1, -1)
    TalkSetChrName('科尔娜')

    Talk(
        (
            '#3720490465V正好１０岁呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(50, 340, -1, -1)
    TalkSetChrName('科尔娜')

    Talk(
        (
            '#3720490466V过生日的时候\n',
            '拍摄的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_AE(0x000001F4)
    FadeIn(300, 0)

    ChrTalk(
        0x0101,
        (
            '#0010490467V#1026F…………………………',
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
        'loc_257D',
    )

    If(
        (
            (Expr.PushReg, 0x6),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2527',
    )

    ChrSetSubChip(0x0107, 1)

    Jump('loc_2541')

    def _loc_2527(): pass

    label('loc_2527')

    If(
        (
            (Expr.PushReg, 0x6),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_253C',
    )

    ChrSetSubChip(0x0107, 0)

    Jump('loc_2541')

    def _loc_253C(): pass

    label('loc_253C')

    ChrSetSubChip(0x0107, 2)

    def _loc_2541(): pass

    label('loc_2541')

    ChrTalk(
        0x0107,
        (
            '#0070490468V#064F？？？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070490469V姐姐，怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_276C')

    def _loc_257D(): pass

    label('loc_257D')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_25EB',
    )

    If(
        (
            (Expr.PushReg, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_25A0',
    )

    ChrSetSubChip(0x0105, 1)

    Jump('loc_25BA')

    def _loc_25A0(): pass

    label('loc_25A0')

    If(
        (
            (Expr.PushReg, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_25B5',
    )

    ChrSetSubChip(0x0105, 0)

    Jump('loc_25BA')

    def _loc_25B5(): pass

    label('loc_25B5')

    ChrSetSubChip(0x0105, 2)

    def _loc_25BA(): pass

    label('loc_25BA')

    ChrTalk(
        0x0105,
        (
            '#0060490470V#043F艾丝蒂尔，\n',
            '有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_276C')

    def _loc_25EB(): pass

    label('loc_25EB')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_266E',
    )

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_260E',
    )

    ChrSetSubChip(0x0104, 1)

    Jump('loc_2628')

    def _loc_260E(): pass

    label('loc_260E')

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2623',
    )

    ChrSetSubChip(0x0104, 0)

    Jump('loc_2628')

    def _loc_2623(): pass

    label('loc_2623')

    ChrSetSubChip(0x0104, 2)

    def _loc_2628(): pass

    label('loc_2628')

    ChrTalk(
        0x0104,
        (
            '#0040490471V#033F哎呀，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040490472V出什么事了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_276C')

    def _loc_266E(): pass

    label('loc_266E')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_26ED',
    )

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2691',
    )

    ChrSetSubChip(0x0103, 1)

    Jump('loc_26AB')

    def _loc_2691(): pass

    label('loc_2691')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_26A6',
    )

    ChrSetSubChip(0x0103, 0)

    Jump('loc_26AB')

    def _loc_26A6(): pass

    label('loc_26A6')

    ChrSetSubChip(0x0103, 2)

    def _loc_26AB(): pass

    label('loc_26AB')

    ChrTalk(
        0x0103,
        (
            '#0030490473V#023F嗯……？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030490474V艾丝蒂尔，怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_276C')

    def _loc_26ED(): pass

    label('loc_26ED')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_276C',
    )

    If(
        (
            (Expr.PushReg, 0x8),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2710',
    )

    ChrSetSubChip(0x0109, 1)

    Jump('loc_272A')

    def _loc_2710(): pass

    label('loc_2710')

    If(
        (
            (Expr.PushReg, 0x8),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2725',
    )

    ChrSetSubChip(0x0109, 0)

    Jump('loc_272A')

    def _loc_2725(): pass

    label('loc_2725')

    ChrSetSubChip(0x0109, 2)

    def _loc_272A(): pass

    label('loc_272A')

    ChrTalk(
        0x0109,
        (
            '#0180490475V#1063F…………？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180490476V艾丝蒂尔，怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_276C(): pass

    label('loc_276C')

    ChrSetSubChip(0x00F7, 1)
    ChrSetSubChip(0x00F8, 0)
    ChrSetSubChip(0x00F9, 2)
    ChrSetSubChip(0x0101, 0)

    ChrTalk(
        0x0101,
        (
            '#0010490477V#1025F唔，嗯……\n',
            '稍微有点难过。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010490478V一想到这孩子\n',
            '在那场战争中遭遇那么痛苦的事。',
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
        'loc_2960',
    )

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_280D',
    )

    ChrSetSubChip(0x0106, 1)

    Jump('loc_2827')

    def _loc_280D(): pass

    label('loc_280D')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2822',
    )

    ChrSetSubChip(0x0106, 0)

    Jump('loc_2827')

    def _loc_2822(): pass

    label('loc_2822')

    ChrSetSubChip(0x0106, 2)

    def _loc_2827(): pass

    label('loc_2827')

    ChrTalk(
        0x0106,
        (
            '#0050490479V#552F啊啊，真不知该说些什么。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050490480V#053F……想办法\n',
            '让她与家人重逢吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_289B',
    )

    ChrSetSubChip(0x0101, 1)

    Jump('loc_28B5')

    def _loc_289B(): pass

    label('loc_289B')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_28B0',
    )

    ChrSetSubChip(0x0101, 0)

    Jump('loc_28B5')

    def _loc_28B0(): pass

    label('loc_28B0')

    ChrSetSubChip(0x0101, 1)

    def _loc_28B5(): pass

    label('loc_28B5')

    ChrTalk(
        0x0101,
        (
            '#0010260931V#1025F啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010490482V#1006F嗯、嗯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0101, 2)

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2909',
    )

    ChrSetSubChip(0x0106, 1)

    Jump('loc_2923')

    def _loc_2909(): pass

    label('loc_2909')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_291E',
    )

    ChrSetSubChip(0x0106, 1)

    Jump('loc_2923')

    def _loc_291E(): pass

    label('loc_291E')

    ChrSetSubChip(0x0106, 2)

    def _loc_2923(): pass

    label('loc_2923')

    ChrTalk(
        0x0106,
        (
            '#0050490483V#051F那么，这张照片，\n',
            '就暂借我们一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2FBE')

    def _loc_2960(): pass

    label('loc_2960')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2ADA',
    )

    If(
        (
            (Expr.PushReg, 0x7),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2983',
    )

    ChrSetSubChip(0x0108, 1)

    Jump('loc_299D')

    def _loc_2983(): pass

    label('loc_2983')

    If(
        (
            (Expr.PushReg, 0x7),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2998',
    )

    ChrSetSubChip(0x0108, 0)

    Jump('loc_299D')

    def _loc_2998(): pass

    label('loc_2998')

    ChrSetSubChip(0x0108, 2)

    def _loc_299D(): pass

    label('loc_299D')

    ChrTalk(
        0x0108,
        (
            '#0080490484V#074F啊啊，真不知该说什么了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080490485V#070F……努力想办法\n',
            '让她与家人重逢吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushReg, 0x7),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2A15',
    )

    ChrSetSubChip(0x0101, 1)

    Jump('loc_2A2F')

    def _loc_2A15(): pass

    label('loc_2A15')

    If(
        (
            (Expr.PushReg, 0x7),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2A2A',
    )

    ChrSetSubChip(0x0101, 0)

    Jump('loc_2A2F')

    def _loc_2A2A(): pass

    label('loc_2A2A')

    ChrSetSubChip(0x0101, 1)

    def _loc_2A2F(): pass

    label('loc_2A2F')

    ChrTalk(
        0x0101,
        (
            '#0010490486V#1011F啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010490482V#1006F嗯、嗯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0101, 2)

    If(
        (
            (Expr.PushReg, 0x7),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2A83',
    )

    ChrSetSubChip(0x0108, 1)

    Jump('loc_2A9D')

    def _loc_2A83(): pass

    label('loc_2A83')

    If(
        (
            (Expr.PushReg, 0x7),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2A98',
    )

    ChrSetSubChip(0x0108, 1)

    Jump('loc_2A9D')

    def _loc_2A98(): pass

    label('loc_2A98')

    ChrSetSubChip(0x0108, 2)

    def _loc_2A9D(): pass

    label('loc_2A9D')

    ChrTalk(
        0x0108,
        (
            '#0080490488V#070F那么，这张照片，\n',
            '就暂借我们一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2FBE')

    def _loc_2ADA(): pass

    label('loc_2ADA')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2C5A',
    )

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2AFD',
    )

    ChrSetSubChip(0x0103, 1)

    Jump('loc_2B17')

    def _loc_2AFD(): pass

    label('loc_2AFD')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2B12',
    )

    ChrSetSubChip(0x0103, 0)

    Jump('loc_2B17')

    def _loc_2B12(): pass

    label('loc_2B12')

    ChrSetSubChip(0x0103, 2)

    def _loc_2B17(): pass

    label('loc_2B17')

    ChrTalk(
        0x0103,
        (
            '#0030490489V#522F嗯，真不知该说什么好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030490490V#020F……想办法用我们的力量\n',
            '让她与家人重逢吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2B95',
    )

    ChrSetSubChip(0x0101, 1)

    Jump('loc_2BAF')

    def _loc_2B95(): pass

    label('loc_2B95')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2BAA',
    )

    ChrSetSubChip(0x0101, 0)

    Jump('loc_2BAF')

    def _loc_2BAA(): pass

    label('loc_2BAA')

    ChrSetSubChip(0x0101, 1)

    def _loc_2BAF(): pass

    label('loc_2BAF')

    ChrTalk(
        0x0101,
        (
            '#0010490486V#1011F啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010490482V#1006F嗯、嗯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0101, 2)

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2C03',
    )

    ChrSetSubChip(0x0103, 1)

    Jump('loc_2C1D')

    def _loc_2C03(): pass

    label('loc_2C03')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2C18',
    )

    ChrSetSubChip(0x0103, 1)

    Jump('loc_2C1D')

    def _loc_2C18(): pass

    label('loc_2C18')

    ChrSetSubChip(0x0103, 2)

    def _loc_2C1D(): pass

    label('loc_2C1D')

    ChrTalk(
        0x0103,
        (
            '#0030490493V#020F那么，这张照片，\n',
            '就暂时借给我们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2FBE')

    def _loc_2C5A(): pass

    label('loc_2C5A')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2E03',
    )

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2C7D',
    )

    ChrSetSubChip(0x0104, 1)

    Jump('loc_2C97')

    def _loc_2C7D(): pass

    label('loc_2C7D')

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2C92',
    )

    ChrSetSubChip(0x0104, 0)

    Jump('loc_2C97')

    def _loc_2C92(): pass

    label('loc_2C92')

    ChrSetSubChip(0x0104, 2)

    def _loc_2C97(): pass

    label('loc_2C97')

    ChrTalk(
        0x0104,
        (
            '#0040490494V#035F唔，真不知该说什么。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040490495V虽然身为帝国人的我\n',
            '也没资格说什么……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040490496V#030F……还是想办法\n',
            '让她与家人重逢吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2D3E',
    )

    ChrSetSubChip(0x0101, 1)

    Jump('loc_2D58')

    def _loc_2D3E(): pass

    label('loc_2D3E')

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2D53',
    )

    ChrSetSubChip(0x0101, 0)

    Jump('loc_2D58')

    def _loc_2D53(): pass

    label('loc_2D53')

    ChrSetSubChip(0x0101, 1)

    def _loc_2D58(): pass

    label('loc_2D58')

    ChrTalk(
        0x0101,
        (
            '#0010490486V#1011F啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010490482V#1006F嗯、嗯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0101, 2)

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2DAC',
    )

    ChrSetSubChip(0x0104, 1)

    Jump('loc_2DC6')

    def _loc_2DAC(): pass

    label('loc_2DAC')

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2DC1',
    )

    ChrSetSubChip(0x0104, 1)

    Jump('loc_2DC6')

    def _loc_2DC1(): pass

    label('loc_2DC1')

    ChrSetSubChip(0x0104, 2)

    def _loc_2DC6(): pass

    label('loc_2DC6')

    ChrTalk(
        0x0104,
        (
            '#0040490499V#030F那么，这张照片，\n',
            '就暂时借给我们啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2FBE')

    def _loc_2E03(): pass

    label('loc_2E03')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2FBE',
    )

    If(
        (
            (Expr.PushReg, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2E26',
    )

    ChrSetSubChip(0x0105, 1)

    Jump('loc_2E40')

    def _loc_2E26(): pass

    label('loc_2E26')

    If(
        (
            (Expr.PushReg, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2E3B',
    )

    ChrSetSubChip(0x0105, 0)

    Jump('loc_2E40')

    def _loc_2E3B(): pass

    label('loc_2E3B')

    ChrSetSubChip(0x0105, 2)

    def _loc_2E40(): pass

    label('loc_2E40')

    ChrTalk(
        0x0105,
        (
            '#0060490500V#049F嗯，真不知该说什么好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060490501V#047F但是，接到这样的委托\n',
            '一定也是女神的指引……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060490502V#040F……想办法尽我们的力量\n',
            '让她与家人重逢吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushReg, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2EFC',
    )

    ChrSetSubChip(0x0101, 1)

    Jump('loc_2F16')

    def _loc_2EFC(): pass

    label('loc_2EFC')

    If(
        (
            (Expr.PushReg, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2F11',
    )

    ChrSetSubChip(0x0101, 0)

    Jump('loc_2F16')

    def _loc_2F11(): pass

    label('loc_2F11')

    ChrSetSubChip(0x0101, 1)

    def _loc_2F16(): pass

    label('loc_2F16')

    ChrTalk(
        0x0101,
        (
            '#0010490486V#1011F啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010490482V#1006F嗯、嗯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0101, 2)

    If(
        (
            (Expr.PushReg, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2F6A',
    )

    ChrSetSubChip(0x0105, 1)

    Jump('loc_2F84')

    def _loc_2F6A(): pass

    label('loc_2F6A')

    If(
        (
            (Expr.PushReg, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2F7F',
    )

    ChrSetSubChip(0x0105, 1)

    Jump('loc_2F84')

    def _loc_2F7F(): pass

    label('loc_2F7F')

    ChrSetSubChip(0x0105, 2)

    def _loc_2F84(): pass

    label('loc_2F84')

    ChrTalk(
        0x0105,
        (
            '#0060490505V#040F那么，就暂时\n',
            '把这张照片借给我们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2FBE(): pass

    label('loc_2FBE')

    ChrTalk(
        0x00FE,
        (
            '#3720490506V好的，请带上。',
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
            (TxtCtl.Item, 0x381),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(0x0381, 1)
    ChrSetSubChip(0x0101, 0)

    ChrTalk(
        0x0101,
        (
            '#0010490507V#1015F好了，这样\n',
            '总算是把事情弄清楚了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010490508V不过该怎样\n',
            '开始调查呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3156',
    )

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_30AC',
    )

    ChrSetSubChip(0x0103, 1)

    Jump('loc_30C6')

    def _loc_30AC(): pass

    label('loc_30AC')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_30C1',
    )

    ChrSetSubChip(0x0103, 0)

    Jump('loc_30C6')

    def _loc_30C1(): pass

    label('loc_30C1')

    ChrSetSubChip(0x0103, 2)

    def _loc_30C6(): pass

    label('loc_30C6')

    ChrTalk(
        0x0103,
        (
            '#0030490509V#020F也是，难得借来的，\n',
            '就从照片这线索开始吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3125',
    )

    ChrSetSubChip(0x0101, 1)
    ChrSetSubChip(0x00F8, 2)
    ChrSetSubChip(0x00F9, 0)

    Jump('loc_3153')

    def _loc_3125(): pass

    label('loc_3125')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3144',
    )

    ChrSetSubChip(0x0101, 0)
    ChrSetSubChip(0x00F7, 1)
    ChrSetSubChip(0x00F9, 2)

    Jump('loc_3153')

    def _loc_3144(): pass

    label('loc_3144')

    ChrSetSubChip(0x0101, 1)
    ChrSetSubChip(0x00F7, 0)
    ChrSetSubChip(0x00F8, 2)

    def _loc_3153(): pass

    label('loc_3153')

    Jump('loc_34CA')

    def _loc_3156(): pass

    label('loc_3156')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3231',
    )

    If(
        (
            (Expr.PushReg, 0x7),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3179',
    )

    ChrSetSubChip(0x0108, 1)

    Jump('loc_3193')

    def _loc_3179(): pass

    label('loc_3179')

    If(
        (
            (Expr.PushReg, 0x7),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_318E',
    )

    ChrSetSubChip(0x0108, 0)

    Jump('loc_3193')

    def _loc_318E(): pass

    label('loc_318E')

    ChrSetSubChip(0x0108, 2)

    def _loc_3193(): pass

    label('loc_3193')

    ChrTalk(
        0x0108,
        (
            '#0080490510V#070F呼，难得借来的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080490511V就有效地使用\n',
            '那张照片吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushReg, 0x7),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3200',
    )

    ChrSetSubChip(0x0101, 1)
    ChrSetSubChip(0x00F8, 2)
    ChrSetSubChip(0x00F9, 0)

    Jump('loc_322E')

    def _loc_3200(): pass

    label('loc_3200')

    If(
        (
            (Expr.PushReg, 0x7),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_321F',
    )

    ChrSetSubChip(0x0101, 0)
    ChrSetSubChip(0x00F7, 1)
    ChrSetSubChip(0x00F9, 2)

    Jump('loc_322E')

    def _loc_321F(): pass

    label('loc_321F')

    ChrSetSubChip(0x0101, 1)
    ChrSetSubChip(0x00F7, 0)
    ChrSetSubChip(0x00F8, 2)

    def _loc_322E(): pass

    label('loc_322E')

    Jump('loc_34CA')

    def _loc_3231(): pass

    label('loc_3231')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_32F6',
    )

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3254',
    )

    ChrSetSubChip(0x0106, 1)

    Jump('loc_326E')

    def _loc_3254(): pass

    label('loc_3254')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3269',
    )

    ChrSetSubChip(0x0106, 0)

    Jump('loc_326E')

    def _loc_3269(): pass

    label('loc_3269')

    ChrSetSubChip(0x0106, 2)

    def _loc_326E(): pass

    label('loc_326E')

    ChrTalk(
        0x0106,
        (
            '#0050490512V#050F说得也是，\n',
            '就从照片这线索开始吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_32C5',
    )

    ChrSetSubChip(0x0101, 1)
    ChrSetSubChip(0x00F8, 2)
    ChrSetSubChip(0x00F9, 0)

    Jump('loc_32F3')

    def _loc_32C5(): pass

    label('loc_32C5')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_32E4',
    )

    ChrSetSubChip(0x0101, 0)
    ChrSetSubChip(0x00F7, 1)
    ChrSetSubChip(0x00F9, 2)

    Jump('loc_32F3')

    def _loc_32E4(): pass

    label('loc_32E4')

    ChrSetSubChip(0x0101, 1)
    ChrSetSubChip(0x00F7, 0)
    ChrSetSubChip(0x00F8, 2)

    def _loc_32F3(): pass

    label('loc_32F3')

    Jump('loc_34CA')

    def _loc_32F6(): pass

    label('loc_32F6')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_33DB',
    )

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3319',
    )

    ChrSetSubChip(0x0104, 1)

    Jump('loc_3333')

    def _loc_3319(): pass

    label('loc_3319')

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_332E',
    )

    ChrSetSubChip(0x0104, 0)

    Jump('loc_3333')

    def _loc_332E(): pass

    label('loc_332E')

    ChrSetSubChip(0x0104, 2)

    def _loc_3333(): pass

    label('loc_3333')

    ChrTalk(
        0x0104,
        (
            '#0040490513V#030F呼呼，说得也是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040490514V难得借来的，\n',
            '就从照片这线索开始吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_33AA',
    )

    ChrSetSubChip(0x0101, 1)
    ChrSetSubChip(0x00F8, 2)
    ChrSetSubChip(0x00F9, 0)

    Jump('loc_33D8')

    def _loc_33AA(): pass

    label('loc_33AA')

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_33C9',
    )

    ChrSetSubChip(0x0101, 0)
    ChrSetSubChip(0x00F7, 1)
    ChrSetSubChip(0x00F9, 2)

    Jump('loc_33D8')

    def _loc_33C9(): pass

    label('loc_33C9')

    ChrSetSubChip(0x0101, 1)
    ChrSetSubChip(0x00F7, 0)
    ChrSetSubChip(0x00F8, 2)

    def _loc_33D8(): pass

    label('loc_33D8')

    Jump('loc_34CA')

    def _loc_33DB(): pass

    label('loc_33DB')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_34CA',
    )

    If(
        (
            (Expr.PushReg, 0x8),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_33FE',
    )

    ChrSetSubChip(0x0109, 1)

    Jump('loc_3418')

    def _loc_33FE(): pass

    label('loc_33FE')

    If(
        (
            (Expr.PushReg, 0x8),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3413',
    )

    ChrSetSubChip(0x0109, 0)

    Jump('loc_3418')

    def _loc_3413(): pass

    label('loc_3413')

    ChrSetSubChip(0x0109, 2)

    def _loc_3418(): pass

    label('loc_3418')

    ChrTalk(
        0x0109,
        (
            '#0180490515V#1067F呼……也是呀……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180490516V#1062F难得借来了，\n',
            '就从照片这线索开始吧，怎样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushReg, 0x8),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_349C',
    )

    ChrSetSubChip(0x0101, 1)
    ChrSetSubChip(0x00F8, 2)
    ChrSetSubChip(0x00F9, 0)

    Jump('loc_34CA')

    def _loc_349C(): pass

    label('loc_349C')

    If(
        (
            (Expr.PushReg, 0x8),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_34BB',
    )

    ChrSetSubChip(0x0101, 0)
    ChrSetSubChip(0x00F7, 1)
    ChrSetSubChip(0x00F9, 2)

    Jump('loc_34CA')

    def _loc_34BB(): pass

    label('loc_34BB')

    ChrSetSubChip(0x0101, 1)
    ChrSetSubChip(0x00F7, 0)
    ChrSetSubChip(0x00F8, 2)

    def _loc_34CA(): pass

    label('loc_34CA')

    ChrTalk(
        0x0101,
        (
            '#0010490517V#1004F啊，用照片？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_356A',
    )

    ChrTalk(
        0x0103,
        (
            '#0030490518V#020F嗯，总之先\n',
            '拿那个给城里的人看看。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030490519V看到照片上的人\n',
            '说不定会有人想起什么。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_376A')

    def _loc_356A(): pass

    label('loc_356A')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_35E8',
    )

    ChrTalk(
        0x0108,
        (
            '#0080490520V#070F啊啊，总之先拿那个\n',
            '给城里的人看看吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080490521V看到女孩的脸\n',
            '或许有人能想起什么吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_376A')

    def _loc_35E8(): pass

    label('loc_35E8')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_366A',
    )

    ChrTalk(
        0x0106,
        (
            '#0050490522V#050F啊啊，总之先拿这个\n',
            '给城里的人看看吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050490523V看到那女孩的脸，\n',
            '应该会有人想起什么的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_376A')

    def _loc_366A(): pass

    label('loc_366A')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_36EA',
    )

    ChrTalk(
        0x0104,
        (
            '#0040490524V#030F啊啊，总之拿照片\n',
            '给城里的人看看吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040490525V看到那女孩的脸，\n',
            '应该会有人想起什么的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_376A')

    def _loc_36EA(): pass

    label('loc_36EA')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_376A',
    )

    ChrTalk(
        0x0109,
        (
            '#0180490526V#1060F对对，总之拿照片\n',
            '给城里的人看看吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180490527V看到那小姑娘的脸，\n',
            '我想会有人能想起点啥。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_376A(): pass

    label('loc_376A')

    ChrTalk(
        0x0101,
        (
            '#0010490528V#1006F是吗，虽说是快\n',
            '１０年前的事了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010490529V那么，就先用这个方法\n',
            '试着开始调查吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3720490530V那就麻烦你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3720490531V如果发现了什么，\n',
            '请再来找我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0101, 2)
    ChrSetSubChip(0x00F7, 1)
    Sleep(40)

    ChrSetSubChip(0x00F9, 2)
    ChrSetSubChip(0x00F8, 1)

    ChrTalk(
        0x0101,
        (
            '#0010490367V#1000F嗯，知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0079, 0x04, 0x08)
    OP_28(0x0079, 0x04, 0x04)
    OP_28(0x0079, 0x01, 0x0001)
    OP_28(0x0079, 0x01, 0x0002)
    FadeOut(1000, 0, -1)
    OP_0D()
    ChrSetChipByIndex(0x0020, 20)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x00F7, 65535)
    ChrSetChipByIndex(0x00F8, 65535)
    ChrSetChipByIndex(0x00F9, 65535)
    ChrClearFlags(0x0020, 0x0004)
    ChrClearFlags(0x0101, 0x0004)
    ChrClearFlags(0x00F7, 0x0004)
    ChrClearFlags(0x00F8, 0x0004)
    ChrClearFlags(0x00F9, 0x0004)
    ChrSetPos(0x0020, 2400, 0, 1370, 0)
    OP_4B(0x0020, 255)
    ChrSetPos(0x0101, 360, 0, -2430, 180)
    ChrSetPos(0x00F7, 360, 0, -2430, 180)
    ChrSetPos(0x00F8, 360, 0, -2430, 180)
    ChrSetPos(0x00F9, 360, 0, -2430, 180)
    OP_69(0x0101, 0)
    OP_30(0x00)
    ChrSetDirection(0x0101, 180, 0)
    ChrSetDirection(0x00F7, 180, 0)
    ChrSetDirection(0x00F8, 180, 0)
    ChrSetDirection(0x00F9, 180, 0)
    OP_4A(0x0000, 255)
    OP_4A(0x0001, 255)
    OP_4A(0x0002, 255)
    OP_4A(0x0003, 255)
    ChrClearFlags(0x0038, 0x0080)
    FadeIn(1000, 0)
    OP_0D()

    Return()

# id: 0x0006 offset: 0x3955
@scena.Code('func_06_3955')
def func_06_3955():
    EventBegin(0x00)
    ChrClearFlags(0x0027, 0x0080)
    ChrClearFlags(0x0026, 0x0080)
    ChrSetPos(0x0020, -230, 0, -650, 180)
    ChrSetPos(0x0027, -230, 0, -1730, 0)
    ChrSetPos(0x0026, -1280, 0, -2300, 0)
    OP_4A(0x0020, 255)
    ChrSetPos(0x0101, 1710, 0, 0, 270)
    ChrSetPos(0x00F7, 2009, 0, -1460, 270)
    ChrSetPos(0x00F8, 2210, 0, -3180, 315)
    ChrSetPos(0x00F9, 2600, 0, -230, 270)
    ChrSetFlags(0x001C, 0x0080)
    ChrSetFlags(0x0038, 0x0080)
    OP_4A(0x001B, 255)
    CameraMove(-1220, 0, -240, 0)
    OP_67(0, 4240, -10000, 0)
    CameraSetDistance(2680, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_0D()

    ChrTalk(
        0x0020,
        (
            '#3720490869V#2P──是这样吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0020,
        (
            '#3720490870V#2P没想到，竟然\n',
            '会发生这种事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0020,
        (
            '#3720490871V#2P蕾妮……\n',
            '以前真是对不起了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0020,
        (
            '#3720490872V#2P真该早点……\n',
            '找到你才对的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0027,
        (
            '#0370490873V#621F#1P哪里的话，婶婶……\n',
            '请别向我道歉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370490874V一切都是时代的错……\n',
            '不是任何人的罪过。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370490875V而且，这１０年间……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370490876V我真的很幸福。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0020, 0x0026, 400)

    ChrTalk(
        0x0020,
        (
            '#3720490877V#2P梅贝尔小姐……\n',
            '请让我再次道谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0020,
        (
            '#3720490878V#2P您和令尊\n',
            '真的是我们的恩人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0026, 0x0020, 400)

    ChrTalk(
        0x0026,
        (
            '#0360490879V#1P#610F哪里，别这么说……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360490880V必须说谢谢的\n',
            '其实是我们才对。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360490881V莉拉的存在对我来说\n',
            '是多大的鼓励啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360490882V#615F#1P咳咳……\n',
            '抱歉，应该称呼为蕾妮小姐吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0020,
        (
            '#3720490883V#2P不用，还是和平常一样\n',
            '称呼她为莉拉就可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0020,
        (
            '#3720490884V#2P因为那是你一直\n',
            '称呼她的名字。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0020, 0x0027, 400)

    ChrTalk(
        0x0020,
        (
            '#3720490885V#2P不过，真是太好了……\n',
            '这孩子能够一直这么幸福地生活着，太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0020,
        (
            '#3720490886V#2P梅贝尔小姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0020,
        (
            '#3720490887V#2P从今以后，\n',
            '也请你们多多关照她了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0026,
        (
            '#0360490888V#613F#1P嗯，嗯……\n',
            '这是当然的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360490889V不过，您不打算\n',
            '把莉拉带回去吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0020, 0x0026, 400)

    ChrTalk(
        0x0020,
        (
            '#3720490890V#2P是，其实一开始\n',
            '是这个打算的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0020,
        (
            '#3720490891V#2P但看到这孩子现在的样子，\n',
            '我便打消了这个念头。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0020,
        (
            '#3720490892V#2P让她就这样继续生活下去……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0020,
        (
            '#3720490893V#2P对这孩子来说，\n',
            '这才是最幸福的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0027,
        (
            '#0370490894V#625F#1P婶婶……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0020, 0x0027, 400)

    ChrTalk(
        0x0020,
        (
            '#3720490895V#2P呵呵，别这副表情嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0020,
        (
            '#3720490896V#2P当然，偶尔\n',
            '也要来看看我哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0020,
        (
            '#3720490897V#2P因为我不能\n',
            '经常来看你……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0026,
        (
            '#0360490898V#610F#1P哎呀，为什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0020, 0x0026, 400)

    ChrTalk(
        0x0020,
        (
            '#3720490899V#2P还没和您提过，\n',
            '其实我们的故乡在很远的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0020,
        (
            '#3720490900V#2P列曼自治州，这个地方\n',
            '大家知道吗？',
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
            '#0010490901V#1004F#2P咦？\n',
            '列曼自治州！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010490902V这不就是协会\n',
            '那个训练场的所在地嘛。',
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
        'loc_413A',
    )

    ChrTalk(
        0x0106,
        (
            '#0050490903V#051F还真有这么有趣的巧合啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4237')

    def _loc_413A(): pass

    label('loc_413A')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_417A',
    )

    ChrTalk(
        0x0103,
        (
            '#0030490904V#020F还真有这么有趣的巧合呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4237')

    def _loc_417A(): pass

    label('loc_417A')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_41BA',
    )

    ChrTalk(
        0x0108,
        (
            '#0080490905V#070F还真有这么有趣的巧合啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4237')

    def _loc_41BA(): pass

    label('loc_41BA')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_41FA',
    )

    ChrTalk(
        0x0104,
        (
            '#0040490906V#030F还真有这么有趣的巧合啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4237')

    def _loc_41FA(): pass

    label('loc_41FA')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4237',
    )

    ChrTalk(
        0x0105,
        (
            '#0060490907V#040F还真有这么有趣的巧合呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4237(): pass

    label('loc_4237')

    ChrTalk(
        0x0101,
        (
            '#0010490908V#1015F#2P这样啊，莉拉\n',
            '原来是外国人啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010490909V（这么一说确实\n',
            '感觉很独特……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0020, 0x0027, 400)

    ChrTalk(
        0x0020,
        (
            '#3720490910V#2P虽说有飞船通航，\n',
            '不过往返还是挺麻烦的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0020,
        (
            '#3720490911V#2P虽然希望你\n',
            '有机会时常来看我……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0020,
        (
            '#3720490912V#2P在那之前，\n',
            '就写信联络吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0027,
        (
            '#0370490913V#621F#1P好的，那么……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370490914V有假期的话，\n',
            '我一定前去看您。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0020,
        (
            '#3720490915V#2P嗯，我会好好等着\n',
            '那天的到来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0020,
        (
            '#3720490916V#2P好了，蕾妮……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0020,
        (
            '#3720490917V#2P最后让我再好好\n',
            '看一看你的脸吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_94(0x01, 0x0020, 0x0000, 0x000000C8, 0x000003E8, 0x00)
    Sleep(1000)

    ChrTalk(
        0x0020,
        (
            '#3720490918V#2P真的，和姐姐\n',
            '长得一模一样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0027, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0027,
        (
            '#0370490919V#622F#1P和妈妈……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0020,
        (
            '#3720490920V#2P嗯嗯……简直是一个模子里刻出来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0020,
        (
            '#3720490921V#2P你和你那\n',
            '红颜薄命的妈妈……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0027,
        (
            '#0370490922V#623F#1P…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0020,
        (
            '#3720490923V#2P她一定一直\n',
            '守护着你。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0020,
        (
            '#3720490924V#2P你能够遇到这么好的人家，\n',
            '一定也是多亏她的保佑。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0020,
        (
            '#3720490925V#2P为了你的母亲，你也一定要……\n',
            '幸福地活下去哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0027,
        (
            '#0370490926V#626F#1P是，婶婶……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370490927V……我答应您。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    RemoveItem(0x0381, 1)
    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(1500)

    RemoveItem(0x0381, 1)
    AddItem(ItemTable['蕾妮的照片'], 1)
    PlaySE(23, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【遥远的记忆】',
            (TxtCtl.SetColor, 0x0),
            '完成了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_28(0x0079, 0x04, 0x10)
    OP_28(0x0079, 0x01, 0x0040)
    MapClearFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    NewScene('ED6_DT21/T1101._SN', 111, 0, 0)
    IdleLoop()

    Return()

# id: 0x0007 offset: 0x46AB
@scena.Code('func_07_46AB')
def func_07_46AB():
    EventBegin(0x00)

    If(
        (
            (Expr.Eval, "OP_CD(0x0013)"),
            Expr.Return,
        ),
        'loc_46BB',
    )

    SetScenaFlags(ScenaFlag(0x0001, 7, 0xF))

    Jump('loc_46C6')

    def _loc_46BB(): pass

    label('loc_46BB')

    If(
        (
            (Expr.Eval, "OP_CD(0x0014)"),
            Expr.Return,
        ),
        'loc_46C6',
    )

    ClearScenaFlags(ScenaFlag(0x0001, 7, 0xF))

    def _loc_46C6(): pass

    label('loc_46C6')

    ChrClearFlags(0x0013, 0x0010)
    ChrClearFlags(0x0014, 0x0010)
    OP_4A(0x0013, 255)
    OP_4A(0x0014, 255)
    Fade(1000)
    ChrSetPos(0x0106, -45770, 0, -2880, 270)
    ChrSetPos(0x0101, -45760, 0, -1750, 270)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4731',
    )

    ChrSetPos(0x0105, -44380, 0, -1770, 270)
    ChrSetPos(0x00F9, -44510, 0, -2770, 270)

    Jump('loc_4785')

    def _loc_4731(): pass

    label('loc_4731')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4763',
    )

    ChrSetPos(0x0105, -44380, 0, -1770, 270)
    ChrSetPos(0x00F8, -44510, 0, -2770, 270)

    Jump('loc_4785')

    def _loc_4763(): pass

    label('loc_4763')

    ChrSetPos(0x00F8, -44380, 0, -1770, 270)
    ChrSetPos(0x00F9, -44510, 0, -2770, 270)

    def _loc_4785(): pass

    label('loc_4785')

    ChrSetFlags(0x000C, 0x0080)
    CameraMove(-46730, 0, -2460, 0)
    OP_67(0, 6760, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Return,
        ),
        'loc_48B7',
    )

    ChrTalk(
        0x0013,
        (
            '#2900480829V请你想办法\n',
            '再拖延点时间吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#2900480830V我们已经\n',
            '安排人去找了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010480831V#1011F请问～打扰一下行吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0013, 0x0101, 400)
    ChrTurnDirection(0x0014, 0x0101, 400)

    ChrTalk(
        0x0013,
        (
            '#2900480832V……什么事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0013, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTalk(
        0x0013,
        (
            '#2900480833V哎呀，你是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_49ED')

    def _loc_48B7(): pass

    label('loc_48B7')

    ChrTalk(
        0x0014,
        (
            '#3660480834V没找到小姐\n',
            '说什么都没用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#3660480835V必须尽快想办法……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010480831V#1011F请问～打扰一下行吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0014, 0x0101, 400)

    ChrTalk(
        0x0014,
        (
            '#3660480837V是？\n',
            '有什么事情呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010480838V#1000F嗯，打扰你们说话了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480839V我们是\n',
            '游击士协会的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0013, 0x0101, 400)
    OP_62(0x0013, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTalk(
        0x0013,
        (
            '#2900480833V哎呀，你是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_49ED(): pass

    label('loc_49ED')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x034A, 4, 0x1A54)),
            Expr.Return,
        ),
        'loc_4B39',
    )

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4AB9',
    )

    ChrTurnDirection(0x0101, 0x0013, 400)

    ChrTalk(
        0x0101,
        (
            '#0010480841V#1001F你好，好久不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060480842V#040F你好，蕾娜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0013, 0x0105, 400)

    ChrTalk(
        0x0013,
        (
            '#2900480843V啊，连科洛丝都来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010480844V#1011F那，为什么\n',
            '蕾娜会在这里？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4B36')

    def _loc_4AB9(): pass

    label('loc_4AB9')

    ChrTurnDirection(0x0101, 0x0013, 400)

    ChrTalk(
        0x0101,
        (
            '#0010480845V#1001F嘿嘿，好久不见了。\n',
            '王立学院见过以后就没见过面了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480844V#1011F那，为什么\n',
            '蕾娜会在这里？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4B36(): pass

    label('loc_4B36')

    Jump('loc_4CED')

    def _loc_4B39(): pass

    label('loc_4B39')

    ChrTurnDirection(0x0101, 0x0013, 400)

    ChrTalk(
        0x0101,
        (
            '#0010480847V#1004F咦咦！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480848V你不是蕾娜……吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4C41',
    )

    ChrTalk(
        0x0105,
        (
            '#0060480849V#040F嗯，调查学院时\n',
            '我们见过面。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060480850V好久不见，蕾娜',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0013, 0x0105, 400)

    ChrTalk(
        0x0013,
        (
            '#2900480843V啊，连科洛丝都来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010480852V#1011F那个，为什么\n',
            '会在这种地方？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4CED')

    def _loc_4C41(): pass

    label('loc_4C41')

    ChrTurnDirection(0x0106, 0x0101, 400)

    ChrTalk(
        0x0106,
        (
            '#0050480853V#052F……熟人吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0106, 400)

    ChrTalk(
        0x0101,
        (
            '#0010480854V#1000F嗯，嗯……\n',
            '是王立学院的学生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_4CAD')
    def lambda_4CAD():
        ChrTurnDirection(0x0106, 0x0013, 400)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_4CAD)

    ChrTurnDirection(0x0101, 0x0013, 400)

    ChrTalk(
        0x0101,
        (
            '#0010480855V#1011F但是，怎么会\n',
            '在这种地方？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4CED(): pass

    label('loc_4CED')

    ChrTurnDirection(0x0013, 0x0101, 400)

    ChrTalk(
        0x0013,
        (
            '#2900480856V嗯，其实\n',
            '是有些原因……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#2900480857V各位是看了公告板\n',
            '才来这里的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010480858V#1000F是这样，怎么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#2900480859V我有件事\n',
            '想尽快委托各位处理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#2900480860V……你们能接受吗？',
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
        'loc_4E47',
    )

    ChrTalk(
        0x0101,
        (
            '#0010480861V#1006F嗯，交给我们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(1, 0x0009)

    Jump('loc_4F77')

    def _loc_4E47(): pass

    label('loc_4E47')

    ChrTalk(
        0x0101,
        (
            '#0010480862V#1007F抱歉。\n',
            '现在有点困难。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#2900480863V这样啊……\n',
            '那可真伤脑筋。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#2900480864V其他的事\n',
            '能马上办好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010480865V#1015F不太清楚呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480866V#1000F不过有空了\n',
            '就马上回来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#2900480867V嗯嗯，那就拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#2900480868V那么，稍后再见……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x007A, 0x01, 0x8000)
    ChrSetDirection(0x0013, 180, 0)
    ChrSetDirection(0x0014, 0, 0)

    def _loc_4F77(): pass

    label('loc_4F77')

    OP_4B(0x0013, 255)
    OP_4B(0x0014, 255)
    ChrClearFlags(0x000C, 0x0080)
    SetScenaFlags(ScenaFlag(0x034A, 5, 0x1A55))
    EventEnd(0x00)

    Return()

# id: 0x0008 offset: 0x4F8A
@scena.Code('func_08_4F8A')
def func_08_4F8A():
    EventBegin(0x00)
    OP_4A(0x0013, 255)
    OP_4A(0x0014, 255)
    ChrClearFlags(0x0013, 0x0010)
    ChrClearFlags(0x0014, 0x0010)
    Fade(1000)
    ChrSetPos(0x0106, -45770, 0, -2880, 270)
    ChrSetPos(0x0101, -45760, 0, -1750, 270)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4FF7',
    )

    ChrSetPos(0x0105, -44380, 0, -1770, 270)
    ChrSetPos(0x00F9, -44510, 0, -2770, 270)

    Jump('loc_504B')

    def _loc_4FF7(): pass

    label('loc_4FF7')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5029',
    )

    ChrSetPos(0x0105, -44380, 0, -1770, 270)
    ChrSetPos(0x00F8, -44510, 0, -2770, 270)

    Jump('loc_504B')

    def _loc_5029(): pass

    label('loc_5029')

    ChrSetPos(0x00F8, -44380, 0, -1770, 270)
    ChrSetPos(0x00F9, -44510, 0, -2770, 270)

    def _loc_504B(): pass

    label('loc_504B')

    ChrSetFlags(0x000C, 0x0080)
    CameraMove(-46730, 0, -2460, 0)
    OP_67(0, 6760, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ChrTurnDirection(0x0013, 0x0101, 0)
    ChrTurnDirection(0x0014, 0x0101, 0)
    OP_0D()

    ChrTalk(
        0x0014,
        (
            '#3660480869V啊，各位……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#2900480870V莫非是可以\n',
            '接受委托了？',
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
        'loc_5163',
    )

    ChrTalk(
        0x0101,
        (
            '#0010480861V#1006F嗯，交给我们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(1, 0x0009)

    Jump('loc_51ED')

    def _loc_5163(): pass

    label('loc_5163')

    ChrTalk(
        0x0101,
        (
            '#0010480872V#1015F唔～抱歉。\n',
            '现在还有点困难。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#2900480873V这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#2900480874V那么，麻烦\n',
            '你们稍后一定要来哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0013, 180, 0)
    ChrSetDirection(0x0014, 0, 0)

    def _loc_51ED(): pass

    label('loc_51ED')

    OP_4B(0x0013, 255)
    OP_4B(0x0014, 255)
    ChrClearFlags(0x000C, 0x0080)
    EventEnd(0x00)

    Return()

# id: 0x0009 offset: 0x51FD
@scena.Code('func_09_51FD')
def func_09_51FD():
    EventBegin(0x00)

    ChrTalk(
        0x0014,
        (
            '#3660480875V有人接受了吗。\n',
            '唔，非常感谢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0013, 0x0014, 400)

    ChrTalk(
        0x0013,
        (
            '#2900480876V我来向各位游击士\n',
            '说明一下情况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#2900480877V至于和对方的应对，\n',
            '就交给你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0014, 0x0013, 400)

    ChrTalk(
        0x0014,
        (
            '#3660480878V好的，那么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0014, 90, 400)

    ChrTalk(
        0x0014,
        (
            '#3660480879V小姐的事，\n',
            '就麻烦你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_52F8')
    def lambda_52F8():
        ChrTurnDirection(0x0013, 0x0014, 400)
        Yield()

        Jump('lambda_52F8')

    DispatchAsync2(0x0013, 0x0001, lambda_52F8)

    @scena.Lambda('lambda_5309')
    def lambda_5309():
        ChrTurnDirection(0x0101, 0x0014, 400)
        Yield()

        Jump('lambda_5309')

    DispatchAsync2(0x0101, 0x0001, lambda_5309)

    @scena.Lambda('lambda_531A')
    def lambda_531A():
        ChrTurnDirection(0x0106, 0x0014, 400)
        Yield()

        Jump('lambda_531A')

    DispatchAsync2(0x0106, 0x0001, lambda_531A)

    @scena.Lambda('lambda_532B')
    def lambda_532B():
        ChrTurnDirection(0x00F8, 0x0014, 400)
        Yield()

        Jump('lambda_532B')

    DispatchAsync2(0x00F8, 0x0001, lambda_532B)

    @scena.Lambda('lambda_533C')
    def lambda_533C():
        ChrTurnDirection(0x00F9, 0x0014, 400)
        Yield()

        Jump('lambda_533C')

    DispatchAsync2(0x00F9, 0x0001, lambda_533C)

    CreateThread(0x0014, 0x01, 0x01, 0x000B)
    CreateThread(0x0013, 0x02, 0x01, 0x000C)
    CameraMove(-43450, 0, -1960, 3000)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0106, 0x01)
    TerminateThread(0x00F8, 0x01)
    TerminateThread(0x00F9, 0x01)
    Sleep(1000)

    CameraMove(-46730, 0, -2460, 3000)

    @scena.Lambda('lambda_5392')
    def lambda_5392():
        ChrTurnDirection(0x0101, 0x0013, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5392)

    Sleep(100)

    @scena.Lambda('lambda_53A5')
    def lambda_53A5():
        ChrTurnDirection(0x0106, 0x0013, 400)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_53A5)

    Sleep(100)

    @scena.Lambda('lambda_53B8')
    def lambda_53B8():
        ChrTurnDirection(0x00F8, 0x0013, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_53B8)

    ChrTurnDirection(0x00F9, 0x0013, 400)
    ChrSetPos(0x0014, -33780, 1500, 2840, 0)

    ChrTalk(
        0x0101,
        (
            '#0010480880V#1016F请，请问～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0013, 0x0101, 400)

    ChrTalk(
        0x0013,
        (
            '#2900480881V是？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010480882V#1015F那个人……是谁？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#2900480883V是本家的管家。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#2900480884V和我一样，是负责\n',
            '照顾小姐的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010480885V#1004F照，照顾小姐～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#2900480886V嗯嗯，是的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#2900480887V那个暂且不提，首先\n',
            '还是说明一下状况吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010480888V#1002F啊，说得是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#2900480889V艾丝蒂尔，\n',
            '你认识芙拉瑟吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x007A, 0x01, 0x4000)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_56D3',
    )

    ChrTalk(
        0x0101,
        (
            '#0010480890V#1011F芙拉瑟？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480891V#1006F啊，嗯……\n',
            '见过的话应该会想起来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5612',
    )

    ChrTalk(
        0x0105,
        (
            '#0060480892V#040F在调查幽灵传闻的时候\n',
            '应该见过吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_56A1')

    def _loc_5612(): pass

    label('loc_5612')

    ChrTalk(
        0x0106,
        (
            '#0050480893V#050F#3P那也是王立学院的学生吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#2900480894V嗯，是的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#2900480895V穿着和我一样的制服，\n',
            '看到的话马上就会认出来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_56A1(): pass

    label('loc_56A1')

    ChrTalk(
        0x0101,
        (
            '#0010480896V#1000F芙拉瑟她\n',
            '出什么事了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5914')

    def _loc_56D3(): pass

    label('loc_56D3')

    ChrTalk(
        0x0101,
        (
            '#0010480890V#1011F芙拉瑟？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480898V#1006F啊，嗯……\n',
            '我在古罗尼山顶见过她哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0013, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0013,
        (
            '#2900480899V！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#2900480900V你见过\n',
            '芙拉瑟吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010480901V#1015F好像说早做社会实践什么的\n',
            '在关所附近徘徊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480902V#1011F……有什么问题吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#2900480903V是，是个很大的问题……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#2900480904V因为，我的委托\n',
            '就是寻找芙拉瑟。',
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
            '#0010480905V#1004F咦咦！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050480906V#051F#3P哈哈，这下可走运了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050480907V居然在寻找之前就已经找到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010480908V#1002F不过，为什么芙拉瑟\n',
            '会跑到山顶的关口去？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_5914(): pass

    label('loc_5914')

    ChrTalk(
        0x0013,
        (
            '#2900480909V她逃跑了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010480910V#1011F啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#2900480911V我是说，她是逃跑的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#2900480912V从这家安特洛丝餐厅逃跑了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010480913V#1004F你说……逃跑了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480914V有什么必要\n',
            '非得从餐厅逃掉不可？',
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
        'loc_5A88',
    )

    ChrTalk(
        0x0104,
        (
            '#0040480915V#031F#4P呼，一定是那样啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040480916V就是说，吃霸王餐啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0104, 400)

    ChrTalk(
        0x0101,
        (
            '#0010480917V#1019F……你以为谁都跟你一样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5A88(): pass

    label('loc_5A88')

    ChrTalk(
        0x0013,
        (
            '#2900480918V为什么要逃……\n',
            '其实也正是我们想知道的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0013, 400)

    ChrTalk(
        0x0013,
        (
            '#2900480919V因为今天对小姐来说\n',
            '本是一个良辰佳日啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050480920V#555F#3P？什么意思？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#2900480921V……请看那边。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4A(0x0016, 255)
    CameraMove(-32900, 1500, 3980, 3000)
    Sleep(2000)

    ChrSetDirection(0x0101, 45, 0)
    ChrSetDirection(0x0106, 45, 0)
    ChrSetDirection(0x00F8, 45, 0)
    ChrSetDirection(0x00F9, 45, 0)
    ChrSetDirection(0x0013, 90, 0)
    Fade(1000)
    CameraMove(-46730, 0, -2460, 0)
    OP_0D()
    OP_4B(0x0016, 255)

    ChrTalk(
        0x0101,
        (
            '#0010480922V#1011F那，那是……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#2900480923V他是某帝国贵族的子弟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#2900480924V为了和小姐相亲，\n',
            '特地远道而来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010480925V#1000F嗯……这样啊…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrTurnDirection(0x0101, 0x0013, 400)

    ChrTalk(
        0x0101,
        (
            '#0010480926V#1020F#3S……啊，相亲！？',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    @scena.Lambda('lambda_5CAC')
    def lambda_5CAC():
        ChrTurnDirection(0x0106, 0x0013, 400)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_5CAC)

    Sleep(100)

    @scena.Lambda('lambda_5CBF')
    def lambda_5CBF():
        ChrTurnDirection(0x00F8, 0x0013, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_5CBF)

    ChrTurnDirection(0x00F9, 0x0013, 400)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5D04',
    )

    ChrTalk(
        0x0105,
        (
            '#0060480927V#044F芙拉瑟……吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5DBB')

    def _loc_5D04(): pass

    label('loc_5D04')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5D42',
    )

    ChrTalk(
        0x0103,
        (
            '#0030480928V#023F那个叫芙拉瑟的女孩子？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5DBB')

    def _loc_5D42(): pass

    label('loc_5D42')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5D84',
    )

    ChrTalk(
        0x0107,
        (
            '#0070480929V#064F那个叫芙拉瑟的姐姐……吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5DBB')

    def _loc_5D84(): pass

    label('loc_5D84')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5DBB',
    )

    ChrTalk(
        0x0104,
        (
            '#0040480930V#033F那个芙拉瑟……吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5DBB(): pass

    label('loc_5DBB')

    ChrTalk(
        0x0013,
        (
            '#2900480931V虽说还是学生，\n',
            '但小姐也已年满１６……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#2900480932V作为帝国上层贵族千金，\n',
            '连一门亲事也没有是种耻辱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010480933V#1022F慢，慢着。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480934V#1002F比起家族的耻辱\n',
            '应该还有更重要的东西吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480935V你们考虑过她本人的心情吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#2900480936V这门亲事的对象\n',
            '论门第论人品都是无可挑剔的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#2900480937V小姐只要见到他，\n',
            '一定会有好感的。',
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
            '#0010480938V#1007F我说，不是这个问题……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480939V……嗯……总算\n',
            '能明白一点她逃跑的理由了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_606D',
    )

    ChrTalk(
        0x0105,
        (
            '#0060480940V#045F啊，是呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060480941V就是为了逃避\n',
            '有违本意的亲事吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050480942V#552F#3P啊啊，就这么回事吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050480943V不过，也要稍微\n',
            '考虑一下别人的难处啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6373')

    def _loc_606D(): pass

    label('loc_606D')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_613D',
    )

    ChrTalk(
        0x0103,
        (
            '#0030480944V#027F是为了逃避\n',
            '有违本意的亲事吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030480945V#021F呼呼，不挺好的嘛。\n',
            '真是青春的感觉啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050480946V#551F#3P你说什么风凉话呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050480947V老为这种事\n',
            '逃跑谁受得了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6373')

    def _loc_613D(): pass

    label('loc_613D')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_62A5',
    )

    ChrTalk(
        0x0104,
        (
            '#0040480948V#031F是为了逃避\n',
            '她不愿意的亲事吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040480949V呼，真是不谙世事啊。\n',
            '令我回想起我的少年时代了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0104, 400)

    ChrTalk(
        0x0101,
        (
            '#0010480950V#1019F反正你一定是被比你大的姐姐\n',
            '逼婚什么的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0104, 0x0101, 400)

    ChrTalk(
        0x0104,
        (
            '#0040480951V#033F啊，你怎么知道？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050480952V#551F#3P不管怎么说，可真麻烦啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050480947V老为这种事\n',
            '出逃谁受得了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_6293')
    def lambda_6293():
        ChrTurnDirection(0x0104, 0x0013, 400)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_6293)

    ChrTurnDirection(0x0101, 0x0013, 400)

    Jump('loc_6373')

    def _loc_62A5(): pass

    label('loc_62A5')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6373',
    )

    ChrTalk(
        0x0108,
        (
            '#0080480954V#070F是为了逃避\n',
            '她不愿意的亲事吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080480955V呼，心情可以理解，\n',
            '但还是太不懂事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050480956V#551F#3P啊啊，有欠考虑啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050480957V多少也得考虑一下\n',
            '别人的难处嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6373(): pass

    label('loc_6373')

    ChrTalk(
        0x0013,
        (
            '#2900480958V……各人有各人的想法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#2900480959V因此，我不会对\n',
            '诸位的意见提出异议。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#2900480960V当前最重要的事，\n',
            '不是讨论什么自由恋爱\n',
            '而是找到小姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x007A, 0x01, 0x4000)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_67E3',
    )

    ChrTalk(
        0x0106,
        (
            '#0050480961V#050F#3P嗯，同感。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050480962V那么，小姐会逃去哪\n',
            '有没有什么线索？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#2900480963V芙拉瑟是一想不通\n',
            '就会钻牛角尖的性格……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#2900480964V恐怕会跑去\n',
            '相当远的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010480965V#1015F相当远……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480966V#1002F应该不会\n',
            '跑出城了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#2900480967V不，城市里\n',
            '到处都没找到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#2900480968V这么说……\n',
            '肯定是出城了吧。',
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
            '#0010480969V#1020F这、这可不得了啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#2900480970V因此，才会这么急得想\n',
            '拜托诸位帮忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#2900480971V事态的紧急性\n',
            '各位能理解了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050480972V#057F#3P呼，这你早说啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050480973V给我们一些细微的线索也行。\n',
            '哪些地方她可能去的呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#2900480974V小姐之前说过\n',
            '要『返回学院』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#2900480975V除此以外，\n',
            '我也不知道什么了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010480976V#1002F要回学院的话，\n',
            '只有走去卢安的路才能到啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050480977V#050F#3P啊啊，就先沿着去卢安\n',
            '的路找找看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010480978V#1002F嗯，就这么办吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480979V那么，蕾娜。\n',
            '我们这就去了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480980V还有什么要说的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6890')

    def _loc_67E3(): pass

    label('loc_67E3')

    ChrTalk(
        0x0106,
        (
            '#0050480961V#050F#3P嗯，同感。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050480982V好，\n',
            '就快去快回吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010480983V#1015F不过……\n',
            '她会乖乖跟我们回来吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480984V没什么理由的话，\n',
            '我想没那么简单哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6890(): pass

    label('loc_6890')

    ChrTalk(
        0x0013,
        (
            '#2900480985V是的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#2900480986V那么，就麻烦\n',
            '给小姐传个话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010480987V#1011F传话？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#2900480988V是的，请这样\n',
            '对芙拉瑟说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#2900480989V『胆小鬼』……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010480990V#1019F…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480991V那个，这么说\n',
            '没问题吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#2900480992V没有问题。\n',
            '都在我的计算之内。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x007A, 0x01, 0x4000)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6A71',
    )

    ChrTalk(
        0x0106,
        (
            '#0050480993V#057F#3P别管那么多了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050480994V快点出发吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0106, 400)

    ChrTalk(
        0x0101,
        (
            '#0010480995V#1002F嗯、嗯，明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0013, 400)

    ChrTalk(
        0x0101,
        (
            '#0010480996V#1002F那，我们就走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6ADD')

    def _loc_6A71(): pass

    label('loc_6A71')

    ChrTalk(
        0x0106,
        (
            '#0050480997V#053F#3P既然委托人这么说\n',
            '我们就没必要管太多了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050480998V#050F要传的话……我们记下了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6ADD(): pass

    label('loc_6ADD')

    ChrTalk(
        0x0013,
        (
            '#2900480999V那么，就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x0014, 0x0010)
    ChrSetFlags(0x0013, 0x0010)
    OP_28(0x007A, 0x04, 0x04)
    OP_28(0x007A, 0x04, 0x08)
    OP_28(0x007A, 0x01, 0x0001)

    If(
        (
            (Expr.Eval, "OP_29(0x007A, 0x01, 0x4000)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6B32',
    )

    OP_28(0x007A, 0x01, 0x0002)

    Jump('loc_6B38')

    def _loc_6B32(): pass

    label('loc_6B32')

    OP_28(0x007A, 0x01, 0x0004)

    def _loc_6B38(): pass

    label('loc_6B38')

    SetScenaFlags(ScenaFlag(0x0002, 3, 0x13))

    Return()

# id: 0x000A offset: 0x6B3C
@scena.Code('func_0A_6B3C')
def func_0A_6B3C():
    FadeOut(0, 0, -1)
    EventBegin(0x00)
    ChrSetFlags(0x0008, 0x0008)
    ChrSetPos(0x0013, -44110, 0, 0, 180)
    ChrSetPos(0x0014, -43150, 0, 610, 180)
    ChrSetPos(0x0012, -44180, 0, -1550, 0)
    ChrSetPos(0x0101, -43640, 0, -3030, 0)
    ChrSetPos(0x0106, -44730, 0, -3030, 0)
    ChrSetPos(0x00F8, -43160, 0, -4320, 0)
    ChrSetPos(0x00F9, -45180, 0, -4320, 0)
    ChrSetChipByIndex(0x0012, 33)
    ChrSetFlags(0x0012, 0x0001)
    ChrClearFlags(0x0012, 0x0080)
    ChrClearFlags(0x0012, 0x0010)
    ChrClearFlags(0x0012, 0x0040)
    ChrClearFlags(0x0012, 0x0004)
    ChrClearFlags(0x0014, 0x0010)
    ChrClearFlags(0x0016, 0x0010)
    OP_4A(0x0013, 255)
    OP_4A(0x0014, 255)
    ChrSetFlags(0x000C, 0x0080)
    CameraMove(-43590, 11050, -920, 0)
    OP_67(0, 6760, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    FadeIn(2000, 0)
    CameraMove(-44180, 0, -1060, 5000)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0014,
        (
            '#3660481185V小姐……幸好您平安无事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#2900481186V……等候您多时了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x007A, 0x01, 0x0020)"),
            Expr.Return,
        ),
        'loc_6D6B',
    )

    ChrTalk(
        0x0012,
        (
            '#2890481187V#1P我并不是自己\n',
            '想回来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#2890481188V#1P只是看你们还惊动了游击士，\n',
            '不得已才陪着回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#2900481189V这都没关系。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#2900481190V不管怎样最终您\n',
            '还是回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6D7B')

    def _loc_6D6B(): pass

    label('loc_6D6B')

    If(
        (
            (Expr.Eval, "OP_29(0x007A, 0x01, 0x0010)"),
            Expr.Return,
        ),
        'loc_6D7B',
    )

    OP_2B(0x007A, 0x0002)

    def _loc_6D7B(): pass

    label('loc_6D7B')

    ChrTalk(
        0x0012,
        (
            '#2890481191V#1P……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#2890481192V#1P蕾娜，有一句话\n',
            '我得说在前头……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#2890481193V#1P我还没有\n',
            '原谅你哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#2900481194V是……\n',
            '这我心知肚明。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#2900481195V不过，\n',
            '这可以之后再说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#2890481196V#1P嗯，就这么办吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#2890481197V#1P反正一时半会儿\n',
            '也说不清楚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#2900481198V那么，请带小姐入席……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#3660481199V遵命。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#3660481200V请，小姐。\n',
            '这边走。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0012, 180, 400)

    ChrTalk(
        0x0012,
        (
            '#2890481201V#1P那么，我们就告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#2890481202V#1P今日实在是\n',
            '给你们添麻烦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010481203V#1006F#4P哪里，小事一桩。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010481204V那么，多保重哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6FEE',
    )

    ChrTalk(
        0x0105,
        (
            '#0060481205V#040F那么，以后学校见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6FEE(): pass

    label('loc_6FEE')

    ChrTalk(
        0x0012,
        (
            '#2890481206V#1P嗯，那再见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_7017')
    def lambda_7017():
        ChrTurnDirection(0x0013, 0x0012, 400)
        Yield()

        Jump('lambda_7017')

    DispatchAsync2(0x0013, 0x0001, lambda_7017)

    @scena.Lambda('lambda_7028')
    def lambda_7028():
        ChrTurnDirection(0x00FE, 0x0012, 400)
        Yield()

        Jump('lambda_7028')

    DispatchAsync2(0x0000, 0x0001, lambda_7028)

    @scena.Lambda('lambda_7039')
    def lambda_7039():
        ChrTurnDirection(0x00FE, 0x0012, 400)
        Yield()

        Jump('lambda_7039')

    DispatchAsync2(0x0001, 0x0001, lambda_7039)

    @scena.Lambda('lambda_704A')
    def lambda_704A():
        ChrTurnDirection(0x00FE, 0x0012, 400)
        Yield()

        Jump('lambda_704A')

    DispatchAsync2(0x0002, 0x0001, lambda_704A)

    @scena.Lambda('lambda_705B')
    def lambda_705B():
        ChrTurnDirection(0x00FE, 0x0012, 400)
        Yield()

        Jump('lambda_705B')

    DispatchAsync2(0x0003, 0x0001, lambda_705B)

    Sleep(400)

    ChrSetDirection(0x0012, 45, 400)

    @scena.Lambda('lambda_7078')
    def lambda_7078():
        ChrWalkTo(0x0012, -41670, 0, 500, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_7078)

    ChrSetDirection(0x0014, 90, 400)
    CreateThread(0x0013, 0x02, 0x01, 0x000D)

    @scena.Lambda('lambda_70A1')
    def lambda_70A1():
        ChrWalkTo(0x0014, -31760, 1500, 500, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_70A1)

    WaitForThreadExit(0x0012, 0x0001)
    ChrWalkTo(0x0012, -32759, 1500, 500, 2000, 0x00)
    TerminateThread(0x0013, 0x01)
    TerminateThread(0x0000, 0x01)
    TerminateThread(0x0001, 0x01)
    TerminateThread(0x0002, 0x01)
    TerminateThread(0x0003, 0x01)
    ChrSetDirection(0x0013, 180, 400)
    ChrWalkTo(0x0013, -44180, 0, -550, 1000, 0x00)
    ChrSetDirection(0x0013, 180, 400)
    WaitForThreadExit(0x0013, 0x0002)
    Sleep(1000)

    ChrTalk(
        0x0013,
        (
            '#2900481207V辛苦你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_7133')
    def lambda_7133():
        ChrSetDirection(0x0101, 0, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_7133)

    Sleep(100)

    @scena.Lambda('lambda_7146')
    def lambda_7146():
        ChrSetDirection(0x0106, 0, 400)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_7146)

    Sleep(100)

    @scena.Lambda('lambda_7159')
    def lambda_7159():
        ChrSetDirection(0x00F8, 0, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_7159)

    ChrSetDirection(0x00F9, 0, 400)

    ChrTalk(
        0x0013,
        (
            '#2900481208V我代替主人，\n',
            '衷心感谢大家的努力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x007A, 0x01, 0x0020)"),
            Expr.Return,
        ),
        'loc_722E',
    )

    ChrTalk(
        0x0101,
        (
            '#0010481209V#1015F#4P嗯、嗯，我们\n',
            '倒是没什么啦……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010481210V#1002F那个，蕾娜没关系吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010481211V和芙拉瑟\n',
            '闹别扭了吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7375')

    def _loc_722E(): pass

    label('loc_722E')

    If(
        (
            (Expr.Eval, "OP_29(0x007A, 0x01, 0x0010)"),
            Expr.Return,
        ),
        'loc_7375',
    )

    ChrTalk(
        0x0013,
        (
            '#2900481212V这是一点心意，\n',
            '谨表我们的感激之情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#2900481213V请收下。',
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
            (TxtCtl.Item, ItemTable['龙卷扇']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(ItemTable['龙卷扇'], 1)

    ChrTalk(
        0x0101,
        (
            '#0010481214V#1011F#4P啊，嗯，谢谢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010481215V#1015F不过，虽说工作\n',
            '算是解决……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010481210V#1002F那个，蕾娜没关系吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010481211V和芙拉瑟\n',
            '闹别扭了吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7375(): pass

    label('loc_7375')

    ChrTalk(
        0x0013,
        (
            '#2900481218V不，这也\n',
            '完全是为了小姐好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#2900481219V我们这些人\n',
            '生来就是要为主人着想的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7436',
    )

    ChrTalk(
        0x0105,
        (
            '#0060481220V#043F可是，蕾娜……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060481221V芙拉瑟\n',
            '或许不是这么想的呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7484')

    def _loc_7436(): pass

    label('loc_7436')

    ChrTalk(
        0x0101,
        (
            '#0010481222V#1003F#4P可是，蕾娜……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010481223V芙拉瑟\n',
            '她或许没这么想？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7484(): pass

    label('loc_7484')

    ChrTalk(
        0x0013,
        (
            '#2900481224V这……\n',
            '是什么意思？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010481225V#1002F#4P就是说芙拉瑟\n',
            '早就把你当朋友啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010481226V我感觉你们的矛盾\n',
            '就出在这里哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010481227V#1015F唔，不过外人\n',
            '也不好说什么就是了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#2900481228V…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#2900481229V不……\n',
            '很有参考价值。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#2900481230V总之必须和\n',
            '芙拉瑟好好谈谈了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#2900481231V那么，我也失陪了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010481232V#1011F#4P啊，嗯。\n',
            '工作辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_764D',
    )

    ChrTalk(
        0x0105,
        (
            '#0060481233V#040F那么，后会有期。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7675')

    def _loc_764D(): pass

    label('loc_764D')

    ChrTalk(
        0x0106,
        (
            '#0050481234V#050F#1P啊啊，再见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7675(): pass

    label('loc_7675')

    ChrTalk(
        0x0013,
        (
            '#2900481235V是，失陪了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_7699')
    def lambda_7699():
        ChrTurnDirection(0x00FE, 0x0013, 400)
        Yield()

        Jump('lambda_7699')

    DispatchAsync2(0x0000, 0x0001, lambda_7699)

    @scena.Lambda('lambda_76AA')
    def lambda_76AA():
        ChrTurnDirection(0x00FE, 0x0013, 400)
        Yield()

        Jump('lambda_76AA')

    DispatchAsync2(0x0001, 0x0001, lambda_76AA)

    @scena.Lambda('lambda_76BB')
    def lambda_76BB():
        ChrTurnDirection(0x00FE, 0x0013, 400)
        Yield()

        Jump('lambda_76BB')

    DispatchAsync2(0x0002, 0x0001, lambda_76BB)

    @scena.Lambda('lambda_76CC')
    def lambda_76CC():
        ChrTurnDirection(0x00FE, 0x0013, 400)
        Yield()

        Jump('lambda_76CC')

    DispatchAsync2(0x0003, 0x0001, lambda_76CC)

    Sleep(400)

    ChrSetDirection(0x0013, 90, 400)
    ChrWalkTo(0x0013, -35000, 0, -550, 2000, 0x00)
    TerminateThread(0x0000, 0x01)
    TerminateThread(0x0001, 0x01)
    TerminateThread(0x0002, 0x01)
    TerminateThread(0x0003, 0x01)

    ChrTalk(
        0x0101,
        (
            '#0010481236V#1007F#4P唔……怎么感觉\n',
            '又会发生新的争端啊～～。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010481237V要是她们能\n',
            '和好就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_77A3',
    )

    ChrTalk(
        0x0105,
        (
            '#0060481238V#043F嗯嗯，确实……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_77A3(): pass

    label('loc_77A3')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_780C',
    )

    ChrTalk(
        0x0103,
        (
            '#0030481239V#020F不过，我们\n',
            '也只能帮到这里了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030481240V之后就看她们自己的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_78EB')

    def _loc_780C(): pass

    label('loc_780C')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7881',
    )

    ChrTalk(
        0x0108,
        (
            '#0080481241V#070F担心可以理解，\n',
            '不过我们也只能帮到这里了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080481242V之后就看她们自己的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_78EB')

    def _loc_7881(): pass

    label('loc_7881')

    ChrTalk(
        0x0106,
        (
            '#0050481243V#050F啊，心情可以理解，\n',
            '不过我们的工作就到此为止了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050481244V之后就看她们自己的了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_78EB(): pass

    label('loc_78EB')

    FadeOut(1000, 0, -1)
    OP_0D()
    ChrSetChipByIndex(0x0012, 14)
    ChrClearFlags(0x0012, 0x0001)
    ChrSetFlags(0x0012, 0x0010)
    ChrSetFlags(0x0012, 0x0040)
    ChrSetFlags(0x0012, 0x0004)
    ChrSetPos(0x0013, -33800, 1500, 1300, 0)
    ChrSetPos(0x0014, -31760, 1500, 1300, 0)
    ChrSetPos(0x0012, -32930, 1600, 2650, 0)
    OP_4B(0x0013, 255)
    OP_4B(0x0014, 255)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x0008, 0x0008)
    PlaySE(23, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【失踪的小姐】',
            (TxtCtl.SetColor, 0x0),
            '完成了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_28(0x007A, 0x04, 0x10)
    ChrSetPos(0x0000, -43590, 0, -1450, 180)
    ChrSetPos(0x0001, -43590, 0, -1450, 180)
    ChrSetPos(0x0002, -43590, 0, -1450, 180)
    ChrSetPos(0x0003, -43590, 0, -1450, 180)
    OP_4A(0x0000, 255)
    OP_4A(0x0001, 255)
    OP_4A(0x0002, 255)
    OP_4A(0x0003, 255)
    OP_69(0x0101, 0)
    OP_30(0x00)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_69(0x0101, 0)
    OP_30(0x00)
    ChrSetDirection(0x0101, 180, 0)
    ChrSetDirection(0x00F7, 180, 0)
    ChrSetDirection(0x00F8, 180, 0)
    ChrSetDirection(0x00F9, 180, 0)
    OP_4A(0x0000, 255)
    OP_4A(0x0001, 255)
    OP_4A(0x0002, 255)
    OP_4A(0x0003, 255)
    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x000B offset: 0x7A60
@scena.Code('func_0B_7A60')
def func_0B_7A60():
    ChrSetDirection(0x00FE, 135, 400)
    ChrWalkTo(0x0014, -46680, 0, -3640, 2000, 0x00)
    ChrWalkTo(0x0014, -43680, 0, -3640, 2000, 0x00)
    ChrWalkTo(0x0014, -41000, 0, -200, 2000, 0x00)
    SetScenaFlags(ScenaFlag(0x0004, 2, 0x22))
    ChrWalkTo(0x0014, -37150, 1500, -200, 2000, 0x00)

    Return()

# id: 0x000C offset: 0x7ABB
@scena.Code('func_0C_7ABB')
def func_0C_7ABB():
    OP_A6(0x0022)
    TerminateThread(0x0013, 0x01)
    ChrWalkTo(0x0013, -47450, 0, -2270, 1000, 0x00)
    Sleep(150)

    ChrSetDirection(0x0013, 90, 400)

    Return()

# id: 0x000D offset: 0x7AE3
@scena.Code('func_0D_7AE3')
def func_0D_7AE3():
    CameraMove(-41920, 0, 210, 2000)
    Sleep(1500)

    CameraMove(-44560, 0, -2000, 2000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
