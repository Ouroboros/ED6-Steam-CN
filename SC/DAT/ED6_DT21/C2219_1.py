import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C2219_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C2219_1 ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'C0403.x'
    header.mapIndex       = 1
    header.bgm            = 15
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
            (Expr.Eval, "OP_29(0x006B, 0x00, 0x02)"),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x006B, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_13A7',
    )

    ChrSetDirection(0x00FE, 270, 0)
    OP_4A(0x00FE, 0)
    EventBegin(0x00)
    Fade(1000)
    ChrSetPos(0x0101, -1410, 0, 201500, 270)
    ChrSetPos(0x00F7, -1250, 0, 202500, 270)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_122',
    )

    ChrSetPos(0x0104, 0, 0, 201500, 270)
    ChrSetPos(0x0105, 250, 0, 202500, 270)

    Jump('loc_174')

    def _loc_122(): pass

    label('loc_122')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['朵洛希'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_155',
    )

    ChrSetPos(0x0104, 0, 0, 201500, 270)
    ChrSetPos(0x0127, 250, 0, 202500, 270)

    Jump('loc_174')

    def _loc_155(): pass

    label('loc_155')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_174',
    )

    ChrSetPos(0x0109, 125, 0, 202000, 270)

    def _loc_174(): pass

    label('loc_174')

    CameraMove(-1660, 0, 202610, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_0D()
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '#1730430487V嗯……\n',
            '还有点痛呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1730430488V这下可不能逞强了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x001D, 0x00, 0x10)"),
            (Expr.Eval, "OP_29(0x001C, 0x00, 0x10)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_217',
    )

    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    Jump('loc_21A')

    def _loc_217(): pass

    label('loc_217')

    ClearScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    def _loc_21A(): pass

    label('loc_21A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2AB',
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
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
        10,
        0,
        (
            TXT(0x00, '◇前篇完成过【灯塔的魔兽扫荡】或者【整备用箱子的搬运】\n'),
            TXT(0x01, '◇两个都没完成\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_56(0x00)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2A8',
    )

    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    Jump('loc_2AB')

    def _loc_2A8(): pass

    label('loc_2A8')

    ClearScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    def _loc_2AB(): pass

    label('loc_2AB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_4CE',
    )

    ChrTalk(
        0x0101,
        (
            '#0010430489V#1001F老爷爷，好久不见！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTurnDirection(0x00FE, 0x0101, 400)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '#1730430490V哎呀，怎么是你啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1730430491V看起来还是那么有精神啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_429',
    )

    ChrTalk(
        0x0106,
        (
            '#0050430492V#051F啊啊，想起来了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050430493V这不就是黑衣人事件中\n',
            '被催眠的老爷爷吗?',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0106, 400)

    ChrTalk(
        0x0101,
        (
            '#0010430494V#1001F嗯，是守灯塔的弗科特先生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0008, 400)

    ChrTalk(
        0x0101,
        (
            '#0010430495V#1000F好久不见了，\n',
            '老爷爷您还好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4CB')

    def _loc_429(): pass

    label('loc_429')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_4CB',
    )

    ChrTurnDirection(0x0103, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030430496V#023F难道之前你们见过吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010430497V#1000F嗯，说来话长。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0008, 400)

    ChrTalk(
        0x0101,
        (
            '#0010430495V#1000F好久不见了，\n',
            '老爷爷您还好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4CB(): pass

    label('loc_4CB')

    Jump('loc_749')

    def _loc_4CE(): pass

    label('loc_4CE')

    ChrTalk(
        0x0101,
        (
            '#0010430499V#1000F老爷爷，好久不见呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTurnDirection(0x00FE, 0x0101, 400)
    Sleep(1000)

    OP_62(0x00FE, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(1500)

    ChrTalk(
        0x00FE,
        (
            '#1730430500V咦，你是？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010430501V#1016F啊，对哦。\n',
            '嗯，不记得了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_61E',
    )

    ChrTalk(
        0x0106,
        (
            '#0050430492V#051F啊啊，想起来了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050430493V是黑衣人事件中\n',
            '被催眠的老爷爷吗?',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0106, 400)

    ChrTalk(
        0x0101,
        (
            '#0010430504V#1000F对，是守灯塔的老爷爷。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_68F')

    def _loc_61E(): pass

    label('loc_61E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_68F',
    )

    ChrTurnDirection(0x0103, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030430496V#023F以前见过吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010430506V#1015F嗯，这个地方\n',
            '就是那次事件的现场。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_68F(): pass

    label('loc_68F')

    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '#1730430507V哦，这样啊。\n',
            '事件发生的时候你们也过来啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0008, 400)

    ChrTalk(
        0x0101,
        (
            '#0010430508V#1006F嗯，就是那个时候的游击士哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430509V好久不见了，\n',
            '老爷爷您还好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_749(): pass

    label('loc_749')

    ChrTalk(
        0x00FE,
        (
            '#1730430510V还好吧，\n',
            '就是近来总有点……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    OP_62(0x00FE, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x00FE,
        (
            '#1730430511V……啊，痛痛痛！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x00F7, 270, 400)

    ChrTalk(
        0x0101,
        (
            '#0010430512V#1004F怎、怎么了！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430513V您、您看起来\n',
            '不是很精神呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1730430514V嗯，最近\n',
            '腰痛又发作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1730430515V只要一弯腰\n',
            '就疼得好厉害啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_8AC',
    )

    ChrTalk(
        0x0105,
        (
            '#0060430516V#043F啊，这可真够难受啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8AC(): pass

    label('loc_8AC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_8DB',
    )

    ChrTalk(
        0x0106,
        (
            '#0050430517V#052F好像很难受啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_907')

    def _loc_8DB(): pass

    label('loc_8DB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_907',
    )

    ChrTalk(
        0x0103,
        (
            '#0030430518V#022F好像很难受啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_907(): pass

    label('loc_907')

    ChrTalk(
        0x0101,
        (
            '#0010430519V#1015F没有什么药吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1730430520V已经是老毛病了。\n',
            '事到如今也不可能治好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1730430521V只能静静地待着\n',
            '等疼痛减轻了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1730430522V唉，不过老实说\n',
            '还真没办法休息……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370806V#1011F咦……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
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
        10,
        0,
        (
            TXT(0x00, '【有什么事情吗？】\n'),
            TXT(0x01, '【啊，请多保重……】\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_56(0x00)
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C59',
    )

    OP_28(0x006B, 0x04, 0x40)
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0101,
        (
            '#0010430524V#1000F啊，请您多保重啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_AEC',
    )

    ChrTalk(
        0x00FE,
        (
            '#1730430525V………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1730430526V……呼，还是那么\n',
            '不机灵啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B67')

    def _loc_AEC(): pass

    label('loc_AEC')

    ChrTalk(
        0x00FE,
        (
            '#1730430525V………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1730430528V……呼，哎呀呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1730430529V近来的游击士\n',
            '真是一点儿也不机灵呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B67(): pass

    label('loc_B67')

    ChrTalk(
        0x0101,
        (
            '#0010280631V#1004F咦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1730430531V算了，没什么事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1730430532V……哦，不好不好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1730430533V一不留神\n',
            '就光顾着说话了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1730430534V好了，你们也要\n',
            '努力工作啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010430535V#1006F那么，您多保重。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)
    ChrSetDirection(0x00FE, 270, 0)
    OP_4B(0x00FE, 0)

    Jump('loc_1397')

    def _loc_C59(): pass

    label('loc_C59')

    OP_28(0x006B, 0x04, 0x02)
    OP_28(0x006B, 0x04, 0x04)
    OP_28(0x006B, 0x04, 0x08)
    OP_65(0x00, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010430536V#1015F有什么要事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1730430537V唔，其实有很重要的工作\n',
            '还搁着没做完呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1730430538V……你们知道吗？\n',
            '灯塔也是使用导力器的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1730430539V虽然已经更换了零件，\n',
            '但还是没法试运行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010430540V#1007F哎呀呀，那可伤脑筋了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1730430541V嗯，不过这可是件\n',
            '责任重大的工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1730430542V要是拜托别人的话，\n',
            '我这灯塔看守就没有立足之地了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1730430543V所以我打算忍着腰痛，\n',
            '自己慢慢地做。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010430544V#1003F是吗…………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430545V#1002F但是，可别太勉强哦。\n',
            '万一恶化就糟糕了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1730430546V这点不用担心。\n',
            '我自己的身体自己知道。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1730430547V哦，不好不好……\n',
            '一不留神就只顾着说话了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1730430548V那好，\n',
            '你们也要加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010430549V#1006F嗯，谢谢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430550V那么，请多保重。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 90, 400)

    @scena.Lambda('lambda_0F5D')
    def lambda_0F5D():
        ChrSetDirection(0x0000, 90, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_0F5D)

    Sleep(100)

    @scena.Lambda('lambda_0F70')
    def lambda_0F70():
        ChrSetDirection(0x0001, 90, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_0F70)

    Sleep(50)

    @scena.Lambda('lambda_0F83')
    def lambda_0F83():
        ChrSetDirection(0x0002, 90, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_0F83)

    Sleep(100)

    @scena.Lambda('lambda_0F96')
    def lambda_0F96():
        ChrSetDirection(0x0003, 90, 400)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_0F96)

    Sleep(400)

    @scena.Lambda('lambda_0FA9')
    def lambda_0FA9():
        OP_94(0x01, 0x0000, 0x0000, 0x000001F4, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_0FA9)

    Sleep(50)

    @scena.Lambda('lambda_0FC4')
    def lambda_0FC4():
        OP_94(0x01, 0x0001, 0x0000, 0x000001F4, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_0FC4)

    @scena.Lambda('lambda_0FDA')
    def lambda_0FDA():
        OP_94(0x01, 0x0002, 0x0000, 0x000001F4, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_0FDA)

    Sleep(50)

    @scena.Lambda('lambda_0FF5')
    def lambda_0FF5():
        OP_94(0x01, 0x0003, 0x0000, 0x000001F4, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_0FF5)

    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    ChrTalk(
        0x00FE,
        (
            '#1730430551V……哦哦，等一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1730430552V差点给忘了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 270, 400)

    @scena.Lambda('lambda_106B')
    def lambda_106B():
        ChrSetDirection(0x0000, 270, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_106B)

    Sleep(100)

    @scena.Lambda('lambda_107E')
    def lambda_107E():
        ChrSetDirection(0x0001, 270, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_107E)

    Sleep(50)

    @scena.Lambda('lambda_1091')
    def lambda_1091():
        ChrSetDirection(0x0002, 270, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_1091)

    Sleep(100)

    @scena.Lambda('lambda_10A4')
    def lambda_10A4():
        ChrSetDirection(0x0003, 270, 400)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_10A4)

    OP_62(0x0101, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010430553V#1000F嗯，怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1730430554V唔，就是刚才说的\n',
            '试运行的事情啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x00FE, 315, 400)

    ChrTalk(
        0x00FE,
        (
            '#1730430555V有关操作方法的说明书\n',
            '放在那边的书架上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#1730430556V如果有兴趣的话，\n',
            '就去看看好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010430557V#1004F咦？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430558V#1016F啊，嗯，知道了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1730430559V说是重要的工作，\n',
            '其实也就是转转开开关而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1730430560V只要看了说明书之后，\n',
            '大概谁都会做吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010430561V#1019F（这、这难不成是……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430562V（绕了好大一圈,\n',
            '  还是要我们去做吧。)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_63(0x0101)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_12FF',
    )

    ChrTalk(
        0x0106,
        (
            '#0050430563V#551F（不用想也知道是了。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1335')

    def _loc_12FF(): pass

    label('loc_12FF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_1335',
    )

    ChrTalk(
        0x0103,
        (
            '#0030430564V#025F（不用想也知道是了吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1335(): pass

    label('loc_1335')

    ChrTalk(
        0x00FE,
        (
            '#1730430565V嗯？怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010430566V#1016F不，没什么。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430567V那，那我们走了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_1397(): pass

    label('loc_1397')

    EventEnd(0x00)
    ChrSetDirection(0x00FE, 270, 0)
    OP_4B(0x00FE, 0)

    Jump('loc_1B27')

    def _loc_13A7(): pass

    label('loc_13A7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_13F8',
    )

    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '呼，真没办法……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在的年轻人真是\n',
            '一点也不会察言观色。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Jump('loc_1B27')

    def _loc_13F8(): pass

    label('loc_13F8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_1468',
    )

    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '呼，给你们\n',
            '添麻烦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，最近\n',
            '要麻烦年轻人的事变多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我毕竟也是上了年纪啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Jump('loc_1B27')

    def _loc_1468(): pass

    label('loc_1468')

    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_1528',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_14F2',
    )

    ChrTalk(
        0x00FE,
        (
            '唔唔……伤脑筋。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '明明哪里都正常，\n',
            '灯塔却还是动不了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '或许就像扎古那小子所说的，\n',
            '可能不是故障吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Jump('loc_1525')

    def _loc_14F2(): pass

    label('loc_14F2')

    ChrTalk(
        0x00FE,
        (
            '唔唔……伤脑筋。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这可能真的\n',
            '不是故障吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1525(): pass

    label('loc_1525')

    Jump('loc_1B24')

    def _loc_1528(): pass

    label('loc_1528')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1621',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_15E2',
    )

    ChrTalk(
        0x00FE,
        (
            '那个乳臭未干的小子\n',
            '真是多嘴……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这个灯塔的事\n',
            '我是最清楚的了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这一次的故障\n',
            '肯定是内部结构的原因。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这点程度的异常，你看着吧!\n',
            '马上就可以修理好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Jump('loc_161E')

    def _loc_15E2(): pass

    label('loc_15E2')

    ChrTalk(
        0x00FE,
        (
            '那小子\n',
            '真是多嘴……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这个灯塔的事\n',
            '我是最清楚的了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_161E(): pass

    label('loc_161E')

    Jump('loc_1B24')

    def _loc_1621(): pass

    label('loc_1621')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_1787',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            (Expr.Eval, "OP_29(0x006B, 0x00, 0x08)"),
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x006B, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x006B, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1682',
    )

    ChrTalk(
        0x00FE,
        (
            '说明书在书架上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果有兴趣的话\n',
            '就读读看好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1784')

    def _loc_1682(): pass

    label('loc_1682')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_16E4',
    )

    ChrTalk(
        0x00FE,
        (
            '要是换成波尔多斯，\n',
            '他会明白灯塔的重要性的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一定能帮我找个\n',
            '看守灯塔的后继者。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1784')

    def _loc_16E4(): pass

    label('loc_16E4')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '唔，到底下任市长\n',
            '会是谁呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就我个人来说是\n',
            '很期待波尔多斯呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x006B, 0x00, 0x10)"),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x006B, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1784',
    )

    ChrTalk(
        0x00FE,
        (
            '此外……\n',
            '说明书在书架上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果有兴趣的话\n',
            '就读读看好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1784(): pass

    label('loc_1784')

    Jump('loc_1B24')

    def _loc_1787(): pass

    label('loc_1787')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_1911',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            (Expr.Eval, "OP_29(0x006B, 0x00, 0x08)"),
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x006B, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x006B, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_17E8',
    )

    ChrTalk(
        0x00FE,
        (
            '说明书在书架上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果有兴趣的话\n',
            '就读读看好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_190E')

    def _loc_17E8(): pass

    label('loc_17E8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1842',
    )

    ChrTalk(
        0x00FE,
        (
            '看守灯塔的工作\n',
            '可不是谁都能胜任的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '希望有志向的年轻人\n',
            '能够来继承啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_190E')

    def _loc_1842(): pass

    label('loc_1842')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '看守灯塔虽然是孤独的工作，\n',
            '但却具有守护海上安全的重要作用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '愿意为了大家而付出，\n',
            '有这种志向的人才能胜任。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x006B, 0x00, 0x10)"),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x006B, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_190E',
    )

    ChrTalk(
        0x00FE,
        (
            '此外……\n',
            '说明书在书架上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果有兴趣的话\n',
            '就读读看好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_190E(): pass

    label('loc_190E')

    Jump('loc_1B24')

    def _loc_1911(): pass

    label('loc_1911')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_1A25',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            (Expr.Eval, "OP_29(0x006B, 0x00, 0x08)"),
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x006B, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x006B, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1976',
    )

    ChrTalk(
        0x00FE,
        (
            '说明书在书架上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果有兴趣的话\n',
            '就读读看好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A22')

    def _loc_1976(): pass

    label('loc_1976')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '我也上年纪了，\n',
            '身体衰弱也没办法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '差不多该找个\n',
            '能交托这项工作的继任人了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x006B, 0x00, 0x10)"),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x006B, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1A22',
    )

    ChrTalk(
        0x00FE,
        (
            '此外……\n',
            '说明书在书架上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果有兴趣的话\n',
            '就读读看好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A22(): pass

    label('loc_1A22')

    Jump('loc_1B24')

    def _loc_1A25(): pass

    label('loc_1A25')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_1B24',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            (Expr.Eval, "OP_29(0x006B, 0x00, 0x08)"),
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x006B, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x006B, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1A86',
    )

    ChrTalk(
        0x00FE,
        (
            '说明书在书架上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果有兴趣的话\n',
            '就读读看好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B24')

    def _loc_1A86(): pass

    label('loc_1A86')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '呼，腰这么痛\n',
            '也没法好好工作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我也差不多该\n',
            '找个后继者了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x006B, 0x00, 0x10)"),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x006B, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1B24',
    )

    ChrTalk(
        0x00FE,
        (
            '此外……\n',
            '说明书在书架上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果有兴趣的话\n',
            '就读读看好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1B24(): pass

    label('loc_1B24')

    TalkEnd(0x00FE)

    def _loc_1B27(): pass

    label('loc_1B27')

    Return()

# id: 0x0001 offset: 0x1B28
@scena.Code('func_01_1B28')
def func_01_1B28():
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '书架上有巴伦诺灯塔·导力器简易手册。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    FadeOut(300, 0, 100)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
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
        10,
        1,
        (
            TXT(0x00, '【读书】\n'),
            TXT(0x01, '【放弃】\n'),
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
    SetMessageWindowPos(72, 320, 56, 3)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1BF0',
    )

    OP_B8(0x0231, 0x0000)
    OP_28(0x006B, 0x01, 0x0001)
    OP_28(0x006B, 0x01, 0x8000)
    OP_65(0x01, 0x0001)
    OP_65(0x02, 0x0001)
    OP_65(0x03, 0x0001)
    OP_65(0x04, 0x0001)

    def _loc_1BF0(): pass

    label('loc_1BF0')

    TalkEnd(0x00FF)

    Return()

# id: 0x0002 offset: 0x1BF4
@scena.Code('func_02_1BF4')
def func_02_1BF4():
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, 0, -1, -1)

    Talk(
        (
            '导力器启动开关',
            0x5,
            TxtCtl.Enter,
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

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_1C66',
    )

    Menu(
        0,
        -1,
        155,
        1,
        (
            TXT(0x00, '★【 ＯＮ 】\n'),
            TXT(0x01, '　【ＯＦＦ】\n'),
            TXT(0x02, '　【 放弃 】\n'),
        ),
    )

    Jump('loc_1C96')

    def _loc_1C66(): pass

    label('loc_1C66')

    Menu(
        0,
        -1,
        155,
        1,
        (
            TXT(0x00, '　【 ＯＮ 】\n'),
            TXT(0x01, '★【ＯＦＦ】\n'),
            TXT(0x02, '　【 放弃 】\n'),
        ),
    )

    def _loc_1C96(): pass

    label('loc_1C96')

    MenuEnd(0x0000)
    OP_5F(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_56(0x00)
    FadeIn(300, 0)
    OP_56(0x01)
    SetMessageWindowPos(72, 320, 56, 3)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1D5F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1CF5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1CEF',
    )

    PlaySE(156, 0x00, 0x64)
    Sleep(400)

    PlaySE(158, 0x01, 0x5A)

    def _loc_1CEF(): pass

    label('loc_1CEF')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Jump('loc_1D5C')

    def _loc_1CF5(): pass

    label('loc_1CF5')

    PlaySE(156, 0x00, 0x64)
    Sleep(400)

    PlaySE(158, 0x00, 0x5A)
    Sleep(1000)

    OP_23(0x009E)
    PlaySE(225, 0x00, 0x64)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1D5C',
    )

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '错误！　启动失败！',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    def _loc_1D5C(): pass

    label('loc_1D5C')

    Jump('loc_1D86')

    def _loc_1D5F(): pass

    label('loc_1D5F')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1D86',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_1D80',
    )

    PlaySE(156, 0x00, 0x64)
    Sleep(400)

    OP_23(0x009E)

    def _loc_1D80(): pass

    label('loc_1D80')

    ClearScenaFlags(ScenaFlag(0x0001, 0, 0x8))
    ClearScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_1D86(): pass

    label('loc_1D86')

    TalkEnd(0x00FF)

    Return()

# id: 0x0003 offset: 0x1D8A
@scena.Code('func_03_1D8A')
def func_03_1D8A():
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, 0, -1, -1)

    Talk(
        (
            '导力压',
            0x5,
            TxtCtl.Enter,
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

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_1E10',
    )

    Menu(
        0,
        -1,
        155,
        1,
        (
            TXT(0x00, '★【 ＨＩＧＨ 】\n'),
            TXT(0x01, '　【  ＭＩＤ  】\n'),
            TXT(0x02, '　【  ＬＯＷ  】\n'),
            TXT(0x03, '　【  放 弃  】\n'),
        ),
    )

    Jump('loc_1EB4')

    def _loc_1E10(): pass

    label('loc_1E10')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_1E67',
    )

    Menu(
        0,
        -1,
        155,
        1,
        (
            TXT(0x00, '　【 ＨＩＧＨ 】\n'),
            TXT(0x01, '　【  ＭＩＤ  】\n'),
            TXT(0x02, '★【  ＬＯＷ  】\n'),
            TXT(0x03, '　【  放　弃  】\n'),
        ),
    )

    Jump('loc_1EB4')

    def _loc_1E67(): pass

    label('loc_1E67')

    Menu(
        0,
        -1,
        155,
        1,
        (
            TXT(0x00, '　【 ＨＩＧＨ 】\n'),
            TXT(0x01, '★【  ＭＩＤ  】\n'),
            TXT(0x02, '　【  ＬＯＷ  】\n'),
            TXT(0x03, '　【  放　弃  】\n'),
        ),
    )

    def _loc_1EB4(): pass

    label('loc_1EB4')

    MenuEnd(0x0000)
    OP_5F(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_56(0x00)
    FadeIn(300, 0)
    OP_56(0x01)
    SetMessageWindowPos(72, 320, 56, 3)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1EF4',
    )

    PlaySE(100, 0x00, 0x64)
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))
    ClearScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    Jump('loc_1F2E')

    def _loc_1EF4(): pass

    label('loc_1EF4')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1F0F',
    )

    PlaySE(100, 0x00, 0x64)
    ClearScenaFlags(ScenaFlag(0x0000, 4, 0x4))
    ClearScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    Jump('loc_1F2E')

    def _loc_1F0F(): pass

    label('loc_1F0F')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1F2A',
    )

    PlaySE(100, 0x00, 0x64)
    ClearScenaFlags(ScenaFlag(0x0000, 4, 0x4))
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    Jump('loc_1F2E')

    def _loc_1F2A(): pass

    label('loc_1F2A')

    TalkEnd(0x00FF)

    Return()

    def _loc_1F2E(): pass

    label('loc_1F2E')

    Call(1, 0x0006)
    TalkEnd(0x00FF)

    Return()

# id: 0x0004 offset: 0x1F36
@scena.Code('func_04_1F36')
def func_04_1F36():
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, 0, -1, -1)

    Talk(
        (
            '水平尾翼强度',
            0x5,
            TxtCtl.Enter,
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

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_1FC3',
    )

    Menu(
        0,
        -1,
        155,
        1,
        (
            TXT(0x00, '★【 ＨＩＧＨ 】\n'),
            TXT(0x01, '　【  ＭＩＤ  】\n'),
            TXT(0x02, '　【  ＬＯＷ  】\n'),
            TXT(0x03, '　【  放　弃  】\n'),
        ),
    )

    Jump('loc_2067')

    def _loc_1FC3(): pass

    label('loc_1FC3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_201A',
    )

    Menu(
        0,
        -1,
        155,
        1,
        (
            TXT(0x00, '　【 ＨＩＧＨ 】\n'),
            TXT(0x01, '　【  ＭＩＤ  】\n'),
            TXT(0x02, '★【  ＬＯＷ  】\n'),
            TXT(0x03, '　【  放　弃  】\n'),
        ),
    )

    Jump('loc_2067')

    def _loc_201A(): pass

    label('loc_201A')

    Menu(
        0,
        -1,
        155,
        1,
        (
            TXT(0x00, '　【 ＨＩＧＨ 】\n'),
            TXT(0x01, '★【  ＭＩＤ  】\n'),
            TXT(0x02, '　【  ＬＯＷ  】\n'),
            TXT(0x03, '　【  放　弃  】\n'),
        ),
    )

    def _loc_2067(): pass

    label('loc_2067')

    MenuEnd(0x0000)
    OP_5F(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_56(0x00)
    FadeIn(300, 0)
    OP_56(0x01)
    SetMessageWindowPos(72, 320, 56, 3)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_20A7',
    )

    PlaySE(100, 0x00, 0x64)
    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))
    ClearScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    Jump('loc_20E1')

    def _loc_20A7(): pass

    label('loc_20A7')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_20C2',
    )

    PlaySE(100, 0x00, 0x64)
    ClearScenaFlags(ScenaFlag(0x0000, 6, 0x6))
    ClearScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    Jump('loc_20E1')

    def _loc_20C2(): pass

    label('loc_20C2')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_20DD',
    )

    PlaySE(100, 0x00, 0x64)
    ClearScenaFlags(ScenaFlag(0x0000, 6, 0x6))
    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    Jump('loc_20E1')

    def _loc_20DD(): pass

    label('loc_20DD')

    TalkEnd(0x00FF)

    Return()

    def _loc_20E1(): pass

    label('loc_20E1')

    Call(1, 0x0006)
    TalkEnd(0x00FF)

    Return()

# id: 0x0005 offset: 0x20E9
@scena.Code('func_05_20E9')
def func_05_20E9():
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, 0, -1, -1)

    Talk(
        (
            '结晶回路连接',
            0x5,
            TxtCtl.Enter,
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

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_2159',
    )

    Menu(
        0,
        -1,
        155,
        1,
        (
            TXT(0x00, '★【 ＯＮ 】\n'),
            TXT(0x01, '　【ＯＦＦ】\n'),
            TXT(0x02, '　【 放弃 】\n'),
        ),
    )

    Jump('loc_2189')

    def _loc_2159(): pass

    label('loc_2159')

    Menu(
        0,
        -1,
        155,
        1,
        (
            TXT(0x00, '　【 ＯＮ 】\n'),
            TXT(0x01, '★【ＯＦＦ】\n'),
            TXT(0x02, '　【 放弃 】\n'),
        ),
    )

    def _loc_2189(): pass

    label('loc_2189')

    MenuEnd(0x0000)
    OP_5F(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_56(0x00)
    FadeIn(300, 0)
    OP_56(0x01)
    SetMessageWindowPos(72, 320, 56, 3)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2316',
    )

    PlaySE(100, 0x00, 0x64)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2259',
    )

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))
    EventBegin(0x00)
    Sleep(1000)

    PlaySE(154, 0x00, 0x64)
    OP_7C(0, 100, 3000, 100)
    PlaySE(161, 0x01, 0x64)
    OP_23(0x009E)
    Sleep(400)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010191490V#1004F啊……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/C2209._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_2313')

    def _loc_2259(): pass

    label('loc_2259')

    Sleep(400)

    OP_23(0x009E)
    PlaySE(225, 0x00, 0x64)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Or,
            Expr.Return,
        ),
        'loc_22C5',
    )

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '错误！　输出不足！　启动解除！',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    Jump('loc_2310')

    def _loc_22C5(): pass

    label('loc_22C5')

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '控制不稳定化！　启动解除！',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    def _loc_2310(): pass

    label('loc_2310')

    ClearScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_2313(): pass

    label('loc_2313')

    Jump('loc_232B')

    def _loc_2316(): pass

    label('loc_2316')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_232B',
    )

    PlaySE(100, 0x00, 0x64)
    ClearScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    def _loc_232B(): pass

    label('loc_232B')

    TalkEnd(0x00FF)

    Return()

# id: 0x0006 offset: 0x232F
@scena.Code('func_06_232F')
def func_06_232F():
    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0004,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_2361',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_237F')

    def _loc_2361(): pass

    label('loc_2361')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_2375',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_237F')

    def _loc_2375(): pass

    label('loc_2375')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_237F(): pass

    label('loc_237F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_2393',
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_23B1')

    def _loc_2393(): pass

    label('loc_2393')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_23A7',
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_23B1')

    def _loc_23A7(): pass

    label('loc_23A7')

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_23B1(): pass

    label('loc_23B1')

    ExecExpressionWithReg(
        0x0004,
        (
            (Expr.PushReg, 0x2),
            (Expr.PushReg, 0x3),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushReg, 0x3),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_2431',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_242E',
    )

    Sleep(400)

    OP_23(0x009E)
    PlaySE(225, 0x00, 0x64)
    ClearScenaFlags(ScenaFlag(0x0000, 3, 0x3))
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '错误！　输出为零！　启动解除！',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    def _loc_242E(): pass

    label('loc_242E')

    Jump('loc_24A0')

    def _loc_2431(): pass

    label('loc_2431')

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x1),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_24A0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_24A0',
    )

    Sleep(400)

    OP_23(0x009E)
    PlaySE(225, 0x00, 0x64)
    ClearScenaFlags(ScenaFlag(0x0000, 3, 0x3))
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '控制不稳定化！　启动解除！',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    def _loc_24A0(): pass

    label('loc_24A0')

    Return()

# id: 0x0007 offset: 0x24A1
@scena.Code('func_07_24A1')
def func_07_24A1():
    EventBegin(0x00)
    OP_28(0x006B, 0x01, 0x0002)
    CameraMove(-1670, 0, 199940, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_4A(0x0008, 0)
    ChrSetDirection(0x0008, 180, 0)
    PlaySE(161, 0x01, 0x64)
    ChrSetPos(0x0101, -3090, 0, 199520, 0)
    ChrSetPos(0x00F7, -2130, 0, 199060, 0)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_254B',
    )

    ChrSetPos(0x0104, -2150, 0, 197690, 0)
    ChrSetPos(0x0105, -3300, 0, 198050, 0)

    Jump('loc_259D')

    def _loc_254B(): pass

    label('loc_254B')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['朵洛希'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_257E',
    )

    ChrSetPos(0x0104, -2150, 0, 197690, 0)
    ChrSetPos(0x0127, -3300, 0, 198050, 0)

    Jump('loc_259D')

    def _loc_257E(): pass

    label('loc_257E')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_259D',
    )

    ChrSetPos(0x0109, -2725, 0, 197870, 0)

    def _loc_259D(): pass

    label('loc_259D')

    FadeIn(2000, 0)
    OP_0D()
    Sleep(400)

    ChrTalk(
        0x0008,
        (
            '#1730430569V哦，似乎成功了嘛！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010430570V#1015F现在开始放着不管就行了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730430571V唔，现在进入的是\n',
            '试运行模式。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730430572V应该会\n',
            '自动停掉的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010430573V#1011F啊，那就放心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730430574V话说回来这还真了不起。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730430575V光靠那个说明书\n',
            '就完全明白怎么操作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010430576V#1016F啊哈哈……\n',
            '这可是相当难懂的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    OP_23(0x00A1)
    PlaySE(154, 0x00, 0x64)
    OP_7C(0, 100, 3000, 100)
    Sleep(1000)

    ChrSetDirection(0x0101, 90, 400)

    ChrTalk(
        0x0101,
        (
            '#0010430577V#1004F啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430578V#1015F好、好像停下了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730430579V唔，测试平安结束了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_2801',
    )

    ChrTalk(
        0x0008,
        (
            '#1730430580V不过，真是又给你们\n',
            '添麻烦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730430581V实在不好意思啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2850')

    def _loc_2801(): pass

    label('loc_2801')

    ChrTalk(
        0x0008,
        (
            '#1730430582V呀，真是又给你们\n',
            '添麻烦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730430581V实在不好意思啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2850(): pass

    label('loc_2850')

    ChrSetDirection(0x0101, 0, 400)

    ChrTalk(
        0x0101,
        (
            '#0010430584V#1001F哪里，没关系的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_28C7',
    )

    ChrTalk(
        0x0106,
        (
            '#0050430585V#051F#2P嗯嗯，道谢就不必了,\n',
            '早点把腰治好吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_290E')

    def _loc_28C7(): pass

    label('loc_28C7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_290E',
    )

    ChrTalk(
        0x0103,
        (
            '#0030430586V#021F#2P嗯嗯，道谢就不必了,\n',
            '请早点把腰治好吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_290E(): pass

    label('loc_290E')

    ChrTalk(
        0x0008,
        (
            '#1730430587V不不，那样说的话\n',
            '我心里过意不去啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730430588V把这些拿去吧。',
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
            '得到了５个',
            (TxtCtl.Item, ItemTable['海参']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了５个',
            (TxtCtl.Item, ItemTable['虾米']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    AddItem(ItemTable['海参'], 5)
    AddItem(ItemTable['虾米'], 5)

    ChrTalk(
        0x0101,
        (
            '#0010430589V#1011F啊……这是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730430590V唔，是海钓专用的鱼饵。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730430591V在这个灯塔的岩壁旁，\n',
            '偶尔也能意外地钓到大家伙呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730430592V如果有空的话\n',
            '就去试试好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010430593V#1001F嘿嘿，谢谢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430594V#1015F嗯～那么\n',
            '我们就先走了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
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
        10,
        0,
        (
            TXT(0x00, '【爷爷要保重身体】\n'),
            TXT(0x01, '【还有其他事吗？】\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_56(0x00)
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2C11',
    )

    ChrTalk(
        0x0101,
        (
            '#0010430595V#1000F……爷爷要保重身体哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730430596V唔，我会小心……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730430597V要是你们能再多问候一句，\n',
            '那才称得上细心到家了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730430598V也罢……\n',
            '那么，保重了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2D63')

    def _loc_2C11(): pass

    label('loc_2C11')

    ChrTalk(
        0x0101,
        (
            '#0010430599V#1000F……没其他别的事了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730430600V唔，没有别的事情了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730430601V不过，能细致地问这么一句才是最重要的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730430602V最近，像你们这样机灵的游击士\n',
            '还真不多见呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010430603V#1001F嘿嘿，没什么。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730430604V今后，也要时刻不能忘记\n',
            '这份细心才好哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730430605V那么，保重。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_2B(0x006B, 0x0001)
    OP_2C(0x006B, 0x01F4)

    def _loc_2D63(): pass

    label('loc_2D63')

    PlaySE(23, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【灯塔的试运转】',
            (TxtCtl.SetColor, 0x0),
            '完成了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_28(0x006B, 0x04, 0x10)
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    OP_64(0x00, 0x0001)
    OP_64(0x01, 0x0001)
    OP_64(0x02, 0x0001)
    OP_64(0x03, 0x0001)
    OP_64(0x04, 0x0001)
    EventEnd(0x00)
    ChrSetDirection(0x0008, 270, 0)
    OP_4B(0x0008, 0)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
