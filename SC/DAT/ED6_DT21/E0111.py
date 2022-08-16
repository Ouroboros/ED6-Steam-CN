import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import E0111_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('E0111   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Event'
    header.mapModel       = 'E0111.x'
    header.mapIndex       = 1
    header.bgm            = 62
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
        ('ED6_DT27/CH03100._CH', 'ED6_DT27/CH03100P._CP'),
        ('ED6_DT07/CH02110._CH', 'ED6_DT07/CH02110P._CP'),
        ('ED6_DT07/CH02120._CH', 'ED6_DT07/CH02120P._CP'),
        ('ED6_DT07/CH01380._CH', 'ED6_DT07/CH01380P._CP'),
    ]

# id: 0x10001 offset: 0xCA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '乔丝特',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '多伦',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '吉尔',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            name                = '空贼雷古',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '通信员利昂',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '空贼阿伦',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
    )

# id: 0x10002 offset: 0x18A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x18A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x18A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 51600,
            triggerZ            = 0,
            triggerY            = 74000,
            triggerRange        = 1000,
            actorX              = 51600,
            actorZ              = 1000,
            actorY              = 74000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000A,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x1AE
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x66),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1CD',
    )

    OP_89(0x0000, 49900, 500, 77980, 270)
    OP_30(0x01)

    def _loc_1CD(): pass

    label('loc_1CD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 0, 0x2230)),
            Expr.Return,
        ),
        'loc_227',
    )

    ChrSetPos(0x000A, 45810, 0, 6940, 0)
    ChrClearFlags(0x000A, 0x0080)
    CreateThread(0x000A, 0x00, 0x00, func_02_370)
    ChrSetPos(0x000B, -21870, 650, 4940, 315)
    ChrClearFlags(0x000B, 0x0080)
    CreateThread(0x000B, 0x00, 0x00, func_02_370)
    ChrSetPos(0x000D, 46020, 0, 77750, 0)
    ChrClearFlags(0x000D, 0x0080)

    Jump('loc_294')

    def _loc_227(): pass

    label('loc_227')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 4, 0x222C)),
            Expr.Return,
        ),
        'loc_294',
    )

    ChrSetPos(0x000A, 45810, 0, 6940, 0)
    ChrClearFlags(0x000A, 0x0080)
    CreateThread(0x000A, 0x00, 0x00, func_02_370)
    ChrSetPos(0x000B, -21870, 650, 4940, 315)
    ChrClearFlags(0x000B, 0x0080)
    ChrSetFlags(0x000B, 0x0010)
    CreateThread(0x000B, 0x00, 0x00, func_02_370)
    ChrSetPos(0x000C, -22620, 650, 5630, 135)
    ChrSetPos(0x000D, 46020, 0, 77750, 0)
    ChrClearFlags(0x000D, 0x0080)

    def _loc_294(): pass

    label('loc_294')

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x68),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2B5',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            (Expr.TestScenaFlags, ScenaFlag(0x0300, 5, 0x1805)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2B5',
    )

    Event(0, func_06_144B)

    def _loc_2B5(): pass

    label('loc_2B5')

    Return()

# id: 0x0001 offset: 0x2B6
@scena.Code('func_01_2B6')
def func_01_2B6():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2D4',
    )

    ExecExpressionWithVar(
        0x3B,
        (
            (Expr.PushLong, 0x227),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x3C,
        (
            (Expr.PushLong, 0x10A),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2D4(): pass

    label('loc_2D4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0300, 6, 0x1806)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2E5',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x59),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2E5(): pass

    label('loc_2E5')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_33A',
    )

    LoadEffect(0x00, 'map\\\\mp027_00.eff')
    PlayEffect(0x00, 0x00, 0x00FF, 51600, 1000, 74000, 0, 0, 0, 1300, 1300, 1300, 0x00FF, 0, 0, 0, 0)

    def _loc_33A(): pass

    label('loc_33A')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_364',
    )

    OP_10(0x00, 0x00)
    OP_10(0x05, 0x01)
    OP_D0(5000, 0)

    ExecExpressionWithValue(
        0x000A,
        0x2A,
        (
            (Expr.PushLong, 0x1388),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_36F')

    def _loc_364(): pass

    label('loc_364')

    OP_10(0x00, 0x01)
    OP_10(0x05, 0x00)
    OP_71(0x0001, 0x0004)

    def _loc_36F(): pass

    label('loc_36F')

    Return()

# id: 0x0002 offset: 0x370
@scena.Code('func_02_370')
def func_02_370():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_385',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_370')

    def _loc_385(): pass

    label('loc_385')

    Return()

# id: 0x0003 offset: 0x386
@scena.Code('func_03_386')
def func_03_386():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 0, 0x2230)),
            Expr.Return,
        ),
        'loc_7EC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0459, 2, 0x22CA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_75F',
    )

    SetScenaFlags(ScenaFlag(0x0459, 2, 0x22CA))

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0452, 6, 0x2296)),
            Expr.Return,
        ),
        'loc_553',
    )

    ChrTalk(
        0x000A,
        (
            '#0290400629V#200F哟，是你们吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290400630V航行控制的毛病\n',
            '总算已经解决了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_45B',
    )

    ChrTalk(
        0x010B,
        (
            '#0090400631V#213F真、真的吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090400632V#211F太棒了！\n',
            '不愧是吉尔哥啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x010B, 400)

    Jump('loc_495')

    def _loc_45B(): pass

    label('loc_45B')

    ChrTalk(
        0x0101,
        (
            '#0010400633V#1011F啊，真的吗？\n',
            '那不是很好吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0101, 400)

    def _loc_495(): pass

    label('loc_495')

    ChrTalk(
        0x000A,
        (
            '#0290400634V#200F其实、这全都多亏了\n',
            '拉赛尔博士的建议。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290400635V真是个了不起的老爷爷啊。\n',
            '连看都没看过，就可以\n',
            '马上说出故障的部位。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290400636V果然不愧是世界著名的\n',
            '导力学者啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_75C')

    def _loc_553(): pass

    label('loc_553')

    ChrTalk(
        0x000A,
        (
            '#0290400629V#200F哟，是你们吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290400638V航行控制方面出了一些毛病，\n',
            '不过总算已经解决了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_625',
    )

    ChrTalk(
        0x010B,
        (
            '#0090400639V#211F嘿嘿，吉尔哥果然厉害。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090400640V简直比导力技师\n',
            '还要了不起呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x010B, 400)

    Jump('loc_697')

    def _loc_625(): pass

    label('loc_625')

    ChrTalk(
        0x0101,
        (
            '#0010400641V#1011F哟～挺了不起的嘛。\n',
            '居然可以自己一个人修理。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010400642V真是没有辜负空贼的称号呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0101, 400)

    def _loc_697(): pass

    label('loc_697')

    ChrTalk(
        0x000A,
        (
            '#0290400643V#200F不，其实都多亏了\n',
            '拉赛尔博士的建议。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290400644V我们通过导力通信进行联络，\n',
            '他马上就找到了原因。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290400645V真是好厉害的老爷爷呢，\n',
            '身为世界著名的导力学者，\n',
            '果然是名不虚传。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_75C(): pass

    label('loc_75C')

    Jump('loc_7E9')

    def _loc_75F(): pass

    label('loc_75F')

    ChrTalk(
        0x000A,
        (
            '#0290400646V#200F拉赛尔博士\n',
            '果然是个了不起的学者啊，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290400647V只是听了一下症状，\n',
            '马上就能找到故障部位……\n',
            '真是个了不起的老爷子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_7E9(): pass

    label('loc_7E9')

    Jump('loc_D71')

    def _loc_7EC(): pass

    label('loc_7EC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 4, 0x222C)),
            Expr.Return,
        ),
        'loc_D71',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0443, 7, 0x221F)),
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 5, 0x222D)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_807',
    )

    Call(0, 0x0007)
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    Return()

    def _loc_807(): pass

    label('loc_807')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_86C',
    )

    ChrTalk(
        0x000A,
        (
            '#0290400648V#200F终端的密码吗？\n',
            '确实有这个可能。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290400649V总之有试一试\n',
            '的价值呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D71')

    def _loc_86C(): pass

    label('loc_86C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0452, 6, 0x2296)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_D06',
    )

    ChrTalk(
        0x000A,
        (
            '#0290400650V#203F呼，真是麻烦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8E0',
    )

    ChrTalk(
        0x010B,
        (
            '#0090400651V#213F吉尔哥，有什么麻烦吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x010B, 400)

    Jump('loc_90D')

    def _loc_8E0(): pass

    label('loc_8E0')

    ChrTalk(
        0x0101,
        (
            '#0010400652V#1002F有什么问题吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0101, 400)

    def _loc_90D(): pass

    label('loc_90D')

    ChrTalk(
        0x000A,
        (
            '#0290400653V#207F嗯，航行控制这方面，\n',
            '稍微出了点问题。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290400654V虽然可以勉强起飞，\n',
            '但飞行中的姿势无法稳定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9B6',
    )

    ChrTalk(
        0x010B,
        (
            '#0090400655V#215F是、是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9F3')

    def _loc_9B6(): pass

    label('loc_9B6')

    ChrTalk(
        0x0101,
        (
            '#0010400656V#1019F虽、虽然听不大懂\n',
            '不过看起来很麻烦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9F3(): pass

    label('loc_9F3')

    ChrTalk(
        0x000A,
        (
            '#0290400657V#206F船体的修复还算可以，\n',
            '但精密仪器就无能为力了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290400658V不如和『埃尔赛尤』\n',
            '联络一下寻求帮助吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290400659V也不知道在通信中\n',
            '能不能解决问题…',
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
        'loc_BC7',
    )

    ChrTalk(
        0x0101,
        (
            '#0010400660V#1015F嗯……\n',
            '提妲不能帮忙吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070400661V#561F我、我虽然懂得一点……\n',
            '不过最好还是让专业人员来做。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070400662V因为飞翔引擎在飞船中\n',
            '是最为复杂的部分了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0107, 400)

    ChrTalk(
        0x0101,
        (
            '#0010400663V#1004F有、有那么复杂啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020400664V#1043F看来只能够\n',
            '询问一下了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x00FE, 400)

    Jump('loc_CB2')

    def _loc_BC7(): pass

    label('loc_BC7')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C46',
    )

    ChrTalk(
        0x010B,
        (
            '#0090400665V#210F不过也只有试试看了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090400666V难得这次可以彼此携手合作，\n',
            '要是不利用一下就太可惜了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CB2')

    def _loc_C46(): pass

    label('loc_C46')

    ChrTalk(
        0x0101,
        (
            '#0010400667V#1011F不过，还是有\n',
            '试试看的必要吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010400668V拉赛尔博士也在上面，\n',
            '或许可以给点提示哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_CB2(): pass

    label('loc_CB2')

    ChrTalk(
        0x000A,
        (
            '#0290400669V#200F啊，说的也是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290400670V还是再耐心地\n',
            '等一等吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0452, 6, 0x2296))

    Jump('loc_D71')

    def _loc_D06(): pass

    label('loc_D06')

    ChrTalk(
        0x000A,
        (
            '#0290400671V#200F航行控制的问题\n',
            '凭我们是解决不了的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290400672V毕竟这种精密仪器\n',
            '可不能随便应付的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D71(): pass

    label('loc_D71')

    TalkEnd(0x00FE)

    Return()

# id: 0x0004 offset: 0xD75
@scena.Code('func_04_D75')
def func_04_D75():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 0, 0x2230)),
            Expr.Return,
        ),
        'loc_F5D',
    )

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E8B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_E1A',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x000B,
        (
            '噢，小姐，\n',
            '联络工作辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '多亏『埃尔赛尤』的帮忙，\n',
            '飞翔引擎也修理好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '双方一起协力合作，\n',
            '果然是有所价值啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E88')

    def _loc_E1A(): pass

    label('loc_E1A')

    ChrTalk(
        0x000B,
        (
            '多亏『埃尔赛尤』的帮忙，\n',
            '飞翔引擎也修理好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '呼，毕竟要是帮不上忙的话，\n',
            '协力合作就没有什么价值了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E88(): pass

    label('loc_E88')

    Jump('loc_F5A')

    def _loc_E8B(): pass

    label('loc_E8B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_F0C',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x000B,
        (
            '控制装置的故障\n',
            '似乎也已经解除了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '那么～我们也要\n',
            '赶紧调整计量器了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '再磨磨蹭蹭的话\n',
            '会被老大骂的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F5A')

    def _loc_F0C(): pass

    label('loc_F0C')

    ChrTalk(
        0x000B,
        (
            '控制装置的故障\n',
            '似乎也已经解除了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '那么～我们也要\n',
            '赶紧调整计量器了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F5A(): pass

    label('loc_F5A')

    Jump('loc_114F')

    def _loc_F5D(): pass

    label('loc_F5D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 4, 0x222C)),
            Expr.Return,
        ),
        'loc_114F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_10CF',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x000C,
        (
            (TxtCtl.SetColor, 0x5),
            '#2P#1S……这里是埃尔赛尤号……\n',
            '……山猫号，请回答。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            (TxtCtl.SetColor, 0x5),
            '#2P#1S……重复，山猫号请回答。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            (TxtCtl.SetColor, 0x0),
            '#1P嗯嗯，我是山猫号……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            (TxtCtl.SetColor, 0x0),
            '#1P接收信号良好……\n',
            '埃尔赛尤号，你们那里听得清楚吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            (TxtCtl.SetColor, 0x5),
            '#2P#1S埃尔赛尤呼叫山猫号……\n',
            '我们这边的信号也很好。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            (TxtCtl.SetColor, 0x5),
            '#2P#1S贵舰现在有\n',
            '什么物资不足吗？',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            (TxtCtl.SetColor, 0x5),
            '#2P#1S重复……\n',
            '山猫号，有什么物资不足吗……',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_114F')

    def _loc_10CF(): pass

    label('loc_10CF')

    ChrTalk(
        0x000B,
        (
            (TxtCtl.SetColor, 0x0),
            '#1P呃～其实我们的航行控制装置\n',
            '出了点问题无法解决，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            (TxtCtl.SetColor, 0x0),
            '#1P希望贵舰的维修人员能提供建议。\n',
            '重复一次，希望贵舰的维修员…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_114F(): pass

    label('loc_114F')

    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0x1153
@scena.Code('func_05_1153')
def func_05_1153():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 0, 0x2230)),
            Expr.Return,
        ),
        'loc_12AC',
    )

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1253',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_11F3',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))
    ChrTurnDirection(0x000D, 0x010B, 0)

    ChrTalk(
        0x000D,
        (
            '啊，小姐……\n',
            '你辛苦了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '飞翔引擎也修好了，\n',
            '现在已经完全恢复正常了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '『山猫号』马上\n',
            '就能完全复原了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1250')

    def _loc_11F3(): pass

    label('loc_11F3')

    ChrTurnDirection(0x000D, 0x010B, 0)

    ChrTalk(
        0x000D,
        (
            '飞翔引擎也修好了，\n',
            '现在已经完全恢复正常了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '『山猫号』马上\n',
            '就能完全复原了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1250(): pass

    label('loc_1250')

    Jump('loc_12A9')

    def _loc_1253(): pass

    label('loc_1253')

    ChrTalk(
        0x00FE,
        (
            '飞翔引擎修复完毕\n',
            '可真是个好消息啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样看来的话，\n',
            '就可以从这里逃出去了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_12A9(): pass

    label('loc_12A9')

    Jump('loc_1447')

    def _loc_12AC(): pass

    label('loc_12AC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 4, 0x222C)),
            Expr.Return,
        ),
        'loc_1447',
    )

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1376',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1324',
    )

    ChrTurnDirection(0x000D, 0x010B, 0)
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x000D,
        (
            '啊，小姐！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '嘿嘿，刚才您\n',
            '真是太帅了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '小姐果然\n',
            '是我们的女神啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1373')

    def _loc_1324(): pass

    label('loc_1324')

    ChrTurnDirection(0x000D, 0x010B, 0)

    ChrTalk(
        0x000D,
        (
            '嘿嘿，刚才您\n',
            '真是太帅了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '我们会努力修船，\n',
            '请小姐耐心期待吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1373(): pass

    label('loc_1373')

    Jump('loc_1447')

    def _loc_1376(): pass

    label('loc_1376')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_13E9',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x000D,
        (
            '哦，是你们啊。\n',
            '刚才多谢了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '『结社』的那群家伙\n',
            '还真是奇怪啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '你们最好\n',
            '也多加小心吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1447')

    def _loc_13E9(): pass

    label('loc_13E9')

    ChrTalk(
        0x000D,
        (
            '『结社』的那群家伙\n',
            '还真是奇怪啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '我们本来也有相当的实力，\n',
            '但却完全不是他们的对手。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1447(): pass

    label('loc_1447')

    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0x144B
@scena.Code('func_06_144B')
def func_06_144B():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    ChrSetPos(0x012A, -25710, -500, 6350, 158)
    ChrSetPos(0x0129, -26570, -500, 5830, 143)
    ChrSetPos(0x0146, -26910, -500, 4600, 90)
    ChrSetPos(0x0102, -25290, -500, 3650, 0)
    CameraMove(-25995, -500, 5000, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    Sleep(1000)

    FadeIn(1500, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x012A,
        (
            '#0290280250V#203F#2P不行……\n',
            '没有启动钥匙就动不了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0129,
        (
            '#0300280251V#197F可恶……都走到这一步了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020280252V#1033F#6P看上去确实不像那种\n',
            '能轻易破坏的锁。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020280253V#1030F还是去找启动钥匙比较快吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0146,
        (
            '#0090280254V#214F#5P果、果然是在\n',
            '这里的守备队长手中吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020280255V#1031F#6P恐怕是的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020280256V应该有一间队长室的，\n',
            '我们先去调查那里吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    ChrSetPos(0x0000, -23370, 0, 3020, 90)
    ChrSetPos(0x0001, -23370, 0, 3020, 90)
    ChrSetPos(0x0002, -23370, 0, 3020, 90)
    ChrSetPos(0x0003, -23370, 0, 3020, 90)
    CameraMove(-23370, 0, 3020, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    Sleep(500)

    SetScenaFlags(ScenaFlag(0x0300, 5, 0x1805))
    FadeIn(1000, 0)
    EventEnd(0x00)
    MapSetFlags(0x02000000)

    Return()

# id: 0x0007 offset: 0x16FE
@scena.Code('func_07_16FE')
def func_07_16FE():
    EventBegin(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1723',
    )

    Call(0, 0x0008)
    Call(0, 0x0009)
    FadeIn(0, 0)
    Sleep(100)

    def _loc_1723(): pass

    label('loc_1723')

    Fade(500)
    CameraMove(44790, 100, 7060, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(2910, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    ChrSetPos(0x0101, 45590, 0, 5520, 0)
    ChrSetPos(0x0102, 46620, 0, 5450, 0)
    ChrSetPos(0x00F8, 45580, 0, 4260, 0)
    ChrSetPos(0x00F9, 47010, 0, 4130, 0)
    ChrSetDirection(0x000A, 180, 0)
    OP_4A(0x000A, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x000A,
        (
            '#0290400598V#200F#2P对了……忘了一件事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290400568V你们听过\n',
            '『Ｏ·Ｒ·Ｐ·Ｈ·Ｅ·Ｕ·Ｓ』\n',
            '这个词吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010400600V#1004F#6P那、那是什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_189F',
    )

    ChrTalk(
        0x010B,
        (
            '#0090400601V#213F#6PＯＲＰＨＥＵＳ……\n',
            '是读作奥菲斯吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A24')

    def _loc_189F(): pass

    label('loc_189F')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_18EE',
    )

    ChrTalk(
        0x0105,
        (
            '#0060400602V#1164F#6PＯＲＰＨＥＵＳ……\n',
            '是读作奥菲斯吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A24')

    def _loc_18EE(): pass

    label('loc_18EE')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_193C',
    )

    ChrTalk(
        0x0104,
        (
            '#0040400603V#030F#6PＯＲＰＨＥＵＳ……\n',
            '是读作奥菲斯吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A24')

    def _loc_193C(): pass

    label('loc_193C')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_198B',
    )

    ChrTalk(
        0x0109,
        (
            '#0180400604V#1060F#6PＯＲＰＨＥＵＳ……\n',
            '是读作奥菲斯吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A24')

    def _loc_198B(): pass

    label('loc_198B')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_19D9',
    )

    ChrTalk(
        0x0107,
        (
            '#0070400605V#064F#6PＯＲＰＨＥＵＳ……\n',
            '是读作奥菲斯吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A24')

    def _loc_19D9(): pass

    label('loc_19D9')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1A24',
    )

    ChrTalk(
        0x0106,
        (
            '#0050400606V#555F#6PＯＲＰＨＥＵＳ……\n',
            '是读作奥菲斯吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A24(): pass

    label('loc_1A24')

    ChrTalk(
        0x0102,
        (
            '#0020400607V#1044F#6P……这个词怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0290400608V#206F#2P没什么，只是监视我们的\n',
            '猎兵们曾经提到过它。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290400578V我觉得它可能有什么含义，\n',
            '所以就记下来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1B60',
    )

    ChrTalk(
        0x010B,
        (
            '#0090400610V#210F#6P原来如此……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010400611V#1015F#6P嗯……\n',
            '确实让人很在意呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010400612V#1004F（啊……或许是！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1BBA')

    def _loc_1B60(): pass

    label('loc_1B60')

    ChrTalk(
        0x0101,
        (
            '#0010400611V#1015F#6P嗯……\n',
            '确实让人很在意呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010400614V#1004F（啊……或许是！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1BBA(): pass

    label('loc_1BBA')

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

    SetMessageWindowPos(-1, 50, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            0x18,
            (TxtCtl.SetColor, 0x5),
            '关于这个词你有什么线索吗？',
            TxtCtl.Enter,
        ),
    )

    Menu(
        0,
        -1,
        150,
        0,
        (
            TXT(0x00, '【工业区域的通称】\n'),
            TXT(0x01, '【福音的正式名称】\n'),
            TXT(0x02, '【终端密码】\n'),
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
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1C76'),
        (0x00000001, 'loc_1D47'),
        (0x00000002, 'loc_1E21'),
        (-1, 'loc_1EAA'),
    )

    def _loc_1C76(): pass

    label('loc_1C76')

    ChrTurnDirection(0x0102, 0x0101, 400)
    Sleep(300)

    ChrTalk(
        0x0102,
        (
            '#0020400615V#1035F#4P不，工业区域的名字\n',
            '应该是『法克特里亚』哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020400616V#1040F莫非是……\n',
            '工业区域的终端所要求输入\n',
            '的密码也说不定啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010400617V#1018F#5P是……是那个啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1EAA')

    def _loc_1D47(): pass

    label('loc_1D47')

    ChrTurnDirection(0x0102, 0x0101, 400)
    Sleep(300)

    ChrTalk(
        0x0102,
        (
            '#0020400618V#1035F#4P不，『福音』这名字\n',
            '在这座都市里似乎也是\n',
            '同样的叫法。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020400616V#1040F或许是……\n',
            '工业区域的终端所要求输入\n',
            '的密码也说不定啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010400617V#1018F#5P是……是那个啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1EAA')

    def _loc_1E21(): pass

    label('loc_1E21')

    ChrTurnDirection(0x0102, 0x0101, 400)
    Sleep(300)

    ChrTalk(
        0x0102,
        (
            '#0020400621V#1040F#4P嗯。\n',
            '大概就是工业区域车站的终端密码。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010400622V#1018F#5P啊，约修亚你也这么认为？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1EAA')

    def _loc_1EAA(): pass

    label('loc_1EAA')

    ChrTalk(
        0x000A,
        (
            '#0290400623V#206F#2P？　怎么回事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0102, 0, 400)
    ChrSetDirection(0x0101, 0, 400)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '将工业区域终端\n',
            '需要密码口令才能打开地下道入口\n',
            '的事情向吉尔说明了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x000A,
        (
            '#0290400624V#200F#2P原来如此……\n',
            '确实有这个可能。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290400594V看来很有试一试的必要啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010400626V#1006F#6P嘿嘿，果然没错吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2011',
    )

    ChrTalk(
        0x010B,
        (
            '#0090400627V#211F#6P谢谢啦，吉尔哥！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2011(): pass

    label('loc_2011')

    ChrTalk(
        0x0102,
        (
            '#0020400628V#1040F#6P赶快去确认一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000A, 0, 400)
    OP_4B(0x000A, 0)
    SetScenaFlags(ScenaFlag(0x0445, 5, 0x222D))
    OP_28(0x009E, 0x01, 0x0200)
    EventEnd(0x00)

    Return()

# id: 0x0008 offset: 0x2055
@scena.Code('func_08_2055')
def func_08_2055():
    FadeOut(0, 0, -1)
    ClearScenaFlags(ScenaFlag(0x0240, 0, 0x1200))
    ClearScenaFlags(ScenaFlag(0x0240, 1, 0x1201))
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)

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
            TXT(0x00, '【◇选择雪拉扎德为队友】\n'),
            TXT(0x01, '【◇选择阿加特为队友】\n'),
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
        (0x00000000, 'loc_20CF'),
        (0x00000001, 'loc_20D5'),
        (-1, 'loc_20DB'),
    )

    def _loc_20CF(): pass

    label('loc_20CF')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_20DB')

    def _loc_20D5(): pass

    label('loc_20D5')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_20DB')

    def _loc_20DB(): pass

    label('loc_20DB')

    Return()

# id: 0x0009 offset: 0x20DC
@scena.Code('func_09_20DC')
def func_09_20DC():
    FadeOut(0, 0, -1)
    CameraMove(-182260, 0, -191970, 0)
    OP_67(0, 6500, -10000, 0)
    CameraSetDistance(4500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    Sleep(200)

    FadeIn(0, 0)
    OP_0D()

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['约修亚'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['阿加特'],
            ChrTable['雪拉扎德'],
            ChrTable['科洛丝'],
            ChrTable['奥利维尔'],
            ChrTable['提妲'],
            ChrTable['金'],
            ChrTable['凯文神父'],
            ChrTable['乔丝特'],
            0xFFFF,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0)

    Return()

# id: 0x000A offset: 0x216F
@scena.Code('func_0A_216F')
def func_0A_216F():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_21C2',
    )

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '好像是导力停止了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Jump('loc_237D')

    def _loc_21C2(): pass

    label('loc_21C2')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '这是一台可供旅行者回复体力的导力器装置。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
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
        32,
        1,
        (
            TXT(0x00, '在这里休息\n'),
            TXT(0x01, '离开\n'),
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

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2362',
    )

    FadeIn(100, 0)
    Sleep(500)

    OP_26(13)
    StopEffect(0x00, 0x02)
    PlayEffect(0x00, 0x00, 0x00FF, 51600, 1000, 74000, 0, 0, 0, 700, 700, 700, 0x00FF, 0, 0, 0, 0)
    OP_6F(0x0000, 0)
    OP_70(0x0000, 50)
    OP_73(0x0000)
    OP_20(0x00000BB8)
    PlaySE(12, 0x00, 0x64)
    StopEffect(0x00, 0x02)
    LoadEffect(0x01, 'map\\\\mp027_01.eff')
    PlayEffect(0x01, 0x01, 0x00FF, 51600, 1000, 74000, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    FadeOut(1000, 0, -1)
    Sleep(700)

    PlaySE(13, 0x00, 0x64)
    OP_0D()
    ChrSetStatus(0x00FF, 0xFE, 0)
    OP_69(0x0000, 0)
    OP_30(0x01)
    Sleep(3500)

    StopEffect(0x01, 0x02)
    PlayEffect(0x00, 0x00, 0x00FF, 51600, 1000, 74000, 0, 0, 0, 1300, 1300, 1300, 0x00FF, 0, 0, 0, 0)
    OP_6F(0x0000, 0)
    OP_1E()
    FadeIn(1000, 0)
    OP_56(0x00)
    TalkEnd(0x00FF)

    Return()

    def _loc_2362(): pass

    label('loc_2362')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_237C',
    )

    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Return()

    def _loc_237C(): pass

    label('loc_237C')

    Return()

    def _loc_237D(): pass

    label('loc_237D')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
