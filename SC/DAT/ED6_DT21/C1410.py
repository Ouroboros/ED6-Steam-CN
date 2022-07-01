import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C1410_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C1410   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '维姆拉'),
    TXT(0x02, '龙谷'),
    TXT(0x03, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'C1410.x'
    header.mapIndex       = 62
    header.bgm            = 15
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x265D
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
        ('ED6_DT07/CH01680._CH', 'ED6_DT07/CH01680P._CP'),
        ('ED6_DT07/CH01660._CH', 'ED6_DT07/CH01660P._CP'),
    ]

# id: 0x10002 offset: 0xBA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 3200,
            z                   = 0,
            y                   = 33900,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            x                   = 3410,
            z                   = 0,
            y                   = 36700,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
    )

# id: 0x10003 offset: 0xFA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0xFA
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0xFA
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 4500,
            triggerZ            = 0,
            triggerY            = 39460,
            triggerRange        = 1500,
            actorX              = 5070,
            actorZ              = 500,
            actorY              = 39610,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x11E
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_134',
    )

    ClearChrFlags(0x0009, 0x0080)
    OP_8C(0x0008, 0, 0)

    Jump('loc_145')

    def _loc_134(): pass

    label('loc_134')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 6, 0x1A26)),
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 7, 0x1A27)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_145',
    )

    SetChrFlags(0x0008, 0x0080)

    def _loc_145(): pass

    label('loc_145')

    Return()

# id: 0x0001 offset: 0x146
@scena.Code('Init')
def Init():
    Return()

# id: 0x0002 offset: 0x147
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_15C',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('ReInit')

    def _loc_15C(): pass

    label('loc_15C')

    Return()

# id: 0x0003 offset: 0x15D
@scena.Code('func_03_15D')
def func_03_15D():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_1D1',
    )

    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '迄今为止发生的异变和\n',
            '巨龙事件也许有什么关系也说不定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '接下来大概还会有\n',
            '什么事情发生吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Jump('loc_BE6')

    def _loc_1D1(): pass

    label('loc_1D1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_2AB',
    )

    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_255',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯……是你们吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是难得，\n',
            '今天刚来了位客人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好像是龙的研究者，\n',
            '为了调查古代龙的住处而来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    Jump('loc_2A5')

    def _loc_255(): pass

    label('loc_255')

    ChrTalk(
        0x00FE,
        (
            '真是难得，\n',
            '今天刚来了位客人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是的……\n',
            '这种时候竟然还有这种心情啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2A5(): pass

    label('loc_2A5')

    TalkEnd(0x00FE)

    Jump('loc_BE6')

    def _loc_2AB(): pass

    label('loc_2AB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_82D',
    )

    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x034A, 1, 0x1A51)),
            Expr.Return,
        ),
        'loc_36E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_315',
    )

    ChrTalk(
        0x00FE,
        (
            '看来已经顺利\n',
            '把巨龙降服了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '身为居住在峡谷的人，\n',
            '我也要感谢你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_36B')

    def _loc_315(): pass

    label('loc_315')

    ChrTalk(
        0x00FE,
        (
            '大家吃了这顿火锅以后\n',
            '好好休息一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这一仗下来，你们肯定也\n',
            '疲惫不堪了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_36B(): pass

    label('loc_36B')

    Jump('loc_827')

    def _loc_36E(): pass

    label('loc_36E')

    ChrTalk(
        0x00FE,
        (
            '嗯，是你们吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看来已经顺利\n',
            '把巨龙降服了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '身为居住在峡谷的人，\n',
            '我也要感谢你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1006F这全都是靠维姆拉先生\n',
            '的帮助啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '如果只有我们几个的话，\n',
            '真的是什么也做不了。',
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
        'loc_46B',
    )

    ChrTalk(
        0x0106,
        (
            '#051F啊啊，正是如此。\n',
            '该说谢谢的应该是我们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_50E')

    def _loc_46B(): pass

    label('loc_46B')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_49D',
    )

    ChrTalk(
        0x0103,
        (
            '#020F是啊，多谢您的协助了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_50E')

    def _loc_49D(): pass

    label('loc_49D')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4CF',
    )

    ChrTalk(
        0x0108,
        (
            '#070F没错，谢谢您的协助啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_50E')

    def _loc_4CF(): pass

    label('loc_4CF')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_50E',
    )

    ChrTalk(
        0x0104,
        (
            '#031F呼～真服了你们。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '『谢谢您的协助了。』',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_50E(): pass

    label('loc_50E')

    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '为了说这句话\n',
            '还特意跑来一趟吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们还真是有闲心……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1016F啊…也、也不只是为了\n',
            '那个才来了啦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '算了，你们就在这里随意休息吧，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是肚子饿了的话\n',
            '那里有火锅料理可以吃。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1004F哎，那是给我们吃的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，虽然吃下这个\n',
            '需要有相当的觉悟……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但对你们这些时常要面对战斗的\n',
            '游击士来说，应该还是很有用的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好了，试试看吧。\n',
            '趁这个机会尝一尝。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x00FE, 90, 400)
    FadeOut(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0x000B, 0x00, 0x64)

    Talk(
        (
            TxtCtl.ShowAll,
            (TxtCtl.SetColor, 0x2),
            '黑暗火锅·觉悟',
            (TxtCtl.SetColor, 0x0),
            '已经品尝过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x00)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6EA',
    )

    SetChrStatus(ChrTable['艾丝蒂尔'], 0x02, 1)
    SetChrStatus(ChrTable['艾丝蒂尔'], 0x05, 0)

    def _loc_6EA(): pass

    label('loc_6EA')

    If(
        (
            (Expr.Eval, "OP_42(0x01)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6FD',
    )

    SetChrStatus(ChrTable['约修亚'], 0x05, 200)

    def _loc_6FD(): pass

    label('loc_6FD')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_710',
    )

    SetChrStatus(ChrTable['雪拉扎德'], 0x05, 200)

    def _loc_710(): pass

    label('loc_710')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_723',
    )

    SetChrStatus(ChrTable['奥利维尔'], 0x05, 200)

    def _loc_723(): pass

    label('loc_723')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_736',
    )

    SetChrStatus(ChrTable['科洛丝'], 0x05, 200)

    def _loc_736(): pass

    label('loc_736')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_749',
    )

    SetChrStatus(ChrTable['阿加特'], 0x05, 200)

    def _loc_749(): pass

    label('loc_749')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_75C',
    )

    SetChrStatus(ChrTable['提妲'], 0x05, 200)

    def _loc_75C(): pass

    label('loc_75C')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_76F',
    )

    SetChrStatus(ChrTable['金'], 0x05, 200)

    def _loc_76F(): pass

    label('loc_76F')

    If(
        (
            (Expr.Eval, "OP_42(0x08)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_782',
    )

    SetChrStatus(ChrTable['凯文神父'], 0x05, 200)

    def _loc_782(): pass

    label('loc_782')

    If(
        (
            (Expr.Eval, "OP_40(0x020D, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7CA',
    )

    If(
        (
            (Expr.Eval, "OP_AC(0x0008)"),
            Expr.Return,
        ),
        'loc_79C',
    )

    Jump('loc_7CA')

    def _loc_79C(): pass

    label('loc_79C')

    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            TxtCtl.ShowAll,
            (TxtCtl.SetColor, 0x2),
            '黑暗火锅·觉悟',
            (TxtCtl.SetColor, 0x0),
            '的做法已经学会了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7CA(): pass

    label('loc_7CA')

    OP_56(0x00)
    FadeIn(1000, 0)
    OP_0D()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '喔……\n',
            '平安回来了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有需要的话就再来吧，\n',
            '随时欢迎你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1A51)
    OP_A2(0x0000)
    def _loc_827(): pass

    label('loc_827')

    TalkEnd(0x00FE)

    Jump('loc_BE6')

    def _loc_82D(): pass

    label('loc_82D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 7, 0x1A27)),
            Expr.Return,
        ),
        'loc_8BF',
    )

    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_886',
    )

    ChrTalk(
        0x00FE,
        (
            '岩山的空洞中\n',
            '有很多危险的魔兽，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '请不要逞强，小心地前进吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8B9')

    def _loc_886(): pass

    label('loc_886')

    ChrTalk(
        0x00FE,
        (
            '嗯……回来了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在这里好好\n',
            '休息一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8B9(): pass

    label('loc_8B9')

    TalkEnd(0x00FE)

    Jump('loc_BE6')

    def _loc_8BF(): pass

    label('loc_8BF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 5, 0x1A25)),
            Expr.Return,
        ),
        'loc_8CD',
    )

    Call(0, 0x0005)

    Jump('loc_BE6')

    def _loc_8CD(): pass

    label('loc_8CD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0350, 0, 0x1A80)),
            Expr.Return,
        ),
        'loc_9AC',
    )

    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_944',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然不知道你们要做什么，\n',
            '不过居然会来到这个地方啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这个屋子里的东西\n',
            '你们可以随意使用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9A6')

    def _loc_944(): pass

    label('loc_944')

    ChrTalk(
        0x00FE,
        (
            '虽然不知道你们要做什么，\n',
            '不过居然会来到这个地方啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这个屋子里的东西\n',
            '你们可以随意使用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9A6(): pass

    label('loc_9A6')

    TalkEnd(0x00FE)

    Jump('loc_BE6')

    def _loc_9AC(): pass

    label('loc_9AC')

    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#3500300703V嗯……你们是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300704V#1011F啊，我们是\n',
            '游击士协会的人…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#3500300705V啊～，好像没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0106, 400)

    ChrTalk(
        0x00FE,
        (
            '#3500300706V那个红毛小鬼和我\n',
            '以前就认识了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050300707V#053F哼，不要一口\n',
            '一个小鬼。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050300708V#051F好久不见啦，\n',
            '维姆拉大叔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050300709V你身体还好吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3500300710V呵呵，我可不想\n',
            '输给你们年轻人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3500300711V虽然不知道你们要做什么，\n',
            '不过居然会来到这个地方啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3500300712V这个屋子里的东西\n',
            '你们可以随意使用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300713V#1018F啊、嗯，谢谢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050300714V#051F不好意思，真是帮大忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1A80)
    OP_A2(0x0000)
    TalkEnd(0x00FE)

    def _loc_BE6(): pass

    label('loc_BE6')

    Return()

# id: 0x0004 offset: 0xBE7
@scena.Code('func_04_BE7')
def func_04_BE7():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_D1A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_CBD',
    )

    ChrTalk(
        0x00FE,
        (
            '身为一名研究者，\n',
            '我对古代龙的住处也很有兴趣……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但那个地方好像很危险，\n',
            '维姆拉先生不让我去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '迄今为止，去那里的人\n',
            '几乎全都是游击士呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看来确实不是我这种人\n',
            '应该去的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    Jump('loc_D17')

    def _loc_CBD(): pass

    label('loc_CBD')

    ChrTalk(
        0x00FE,
        (
            '去过古代龙住处的人\n',
            '几乎全都是游击士呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '从这点可以清楚了解到\n',
            '那里的危险程度呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D17(): pass

    label('loc_D17')

    Jump('loc_E3F')

    def _loc_D1A(): pass

    label('loc_D1A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_E3F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_DDF',
    )

    ChrTalk(
        0x00FE,
        (
            '啊，你好。\n',
            '我是古代生物的研究者。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '听到古代龙住处的传闻之后\n',
            '特意赶到这里，不过……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那、那里的危险程度似乎\n',
            '远超乎我的预料呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我、我只是稍微\n',
            '来看看情况而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    Jump('loc_E3F')

    def _loc_DDF(): pass

    label('loc_DDF')

    ChrTalk(
        0x00FE,
        (
            '听到古代龙住处的传闻之后\n',
            '特意赶到这里，不过……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '非常危险呢。\n',
            '连、连一步都不敢踏出去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E3F(): pass

    label('loc_E3F')

    TalkEnd(0x0009)

    Return()

# id: 0x0005 offset: 0xE43
@scena.Code('func_05_E43')
def func_05_E43():
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
        'loc_E5A',
    )

    Call(0, 0x0006)
    Call(0, 0x0008)

    def _loc_E5A(): pass

    label('loc_E5A')

    Fade(1000)
    OP_6D(3740, 0, 36060, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x0101, 4260, 0, 35660, 225)
    SetChrPos(0x0106, 3350, 0, 36130, 180)
    SetChrPos(0x0107, 2660, 0, 36470, 180)
    SetChrPos(0x00F9, 3440, 0, 37310, 180)
    OP_4A(0x0008, 255)
    OP_0D()
    ChrTurnDirection(0x00F9, 0x0008, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_F8C',
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
            TXT(0x00, '【◇在后篇见过维姆拉】\n'),
            TXT(0x01, '【◇在后篇没见过维姆拉】\n'),
            TXT(0x02, '【◇什么也没有变更】\n'),
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

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_F80'),
        (0x00000001, 'loc_F86'),
        (-1, 'loc_F8C'),
    )

    def _loc_F80(): pass

    label('loc_F80')

    OP_A2(0x1A80)

    Jump('loc_F8C')

    def _loc_F86(): pass

    label('loc_F86')

    OP_A3(0x1A80)

    Jump('loc_F8C')

    def _loc_F8C(): pass

    label('loc_F8C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0350, 0, 0x1A80)),
            Expr.Return,
        ),
        'loc_10A5',
    )

    ChrTalk(
        0x0106,
        (
            '#0050310845V#051F哟。\n',
            '维姆拉大叔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0008, 0, 400)
    Sleep(700)

    ChrTalk(
        0x0008,
        (
            '#3500310846V阿加特……\n',
            '还有小姐们也来了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310847V#1011F#5P您好啊，维姆拉大叔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070310848V#560F#5P那个、打扰您了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3500310849V嗯，多次来这种\n',
            '偏僻荒凉的地方……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3500310850V有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_126E')

    def _loc_10A5(): pass

    label('loc_10A5')

    OP_8C(0x0008, 0, 400)
    Sleep(700)

    ChrTalk(
        0x0008,
        (
            '#3500310851V嗯……你们是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070310848V#560F#5P那个、打扰您了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310853V#1011F#5P嗯、我们是\n',
            '游击士协会的…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3500310854V啊啊，就是那样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3500310855V那个红毛小鬼和我\n',
            '以前就认识了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050300707V#053F哼，不要一口\n',
            '一个小鬼。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050300708V#051F好久不见啦，\n',
            '维姆拉大叔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050300709V你身体还好吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3500310859V呵呵，我可不想\n',
            '输给你们年轻人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3500310860V那么，有什么事吗？\n',
            '你们似乎是为什么事情而来的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_126E(): pass

    label('loc_126E')

    ChrTalk(
        0x0101,
        (
            '#0010310861V#1002F#5P嗯，其实……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '将柏斯地区出现龙的事件\n',
            '说明给了维姆拉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#3500310862V呼……原来如此。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3500310863V怪不得前一阵子\n',
            '外边那么乱呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050310864V#051F喂，大叔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050310865V记得你之前曾经说过，\n',
            '你到过西北部去吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050310866V现在想请你告诉我们\n',
            '那边的路怎么走。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1000)

    OP_63(0x0008)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#3500310867V……我拒绝',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0106, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0107, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1475',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_14B3')

    def _loc_1475(): pass

    label('loc_1475')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_149C',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_14B3')

    def _loc_149C(): pass

    label('loc_149C')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    def _loc_14B3(): pass

    label('loc_14B3')

    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010310868V#1004F#5P哎哎！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050310869V#055F慢着！！\n',
            '为什么想都不想就直接拒绝！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3500310870V……我只有一个问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3500310871V你们，找到龙之后\n',
            '准备怎么做？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010211066V#1015F#5P嗯、嗯嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010310873V它好像是被某些恶人操控了… \n',
            '可能的话，我们也不想杀死它……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050310874V#552F但如果将『福音』破坏\n',
            '也不能让它清醒的话，就没办法了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050310875V毕竟世界上没那么多完美结局啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3500310876V哎呀呀呀……说得真轻松啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3500310877V听你们的口气，\n',
            '似乎将龙同你们打倒过的魔兽\n',
            '混为一谈了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3500310878V那实在是太天真了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3500310879V龙可是在『大崩坏』之前\n',
            '就存在的神兽。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310880V#1015F#5P『大崩坏』之前……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010310881V#1020F#5P#3S哎哎！？',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x00000064)
    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070310882V#065F#5P那、那就是说\n',
            '在1200年前就……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050310883V#051F哈哈，那不太可能吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050310884V虽然能看出来它是个老家伙，\n',
            '但再怎么老也不可能……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_18DE',
    )

    ChrTalk(
        0x0103,
        (
            '#0030310885V#025F#5P不，那是有可能的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030310886V#022F虽然仅限于有龙之传承\n',
            '的国家……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030310887V但确实有『龙是不老不死的』\n',
            '这种说法一直在流传着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AEF')

    def _loc_18DE(): pass

    label('loc_18DE')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1995',
    )

    ChrTalk(
        0x0105,
        (
            '#0060310888V#043F#5P不，那是有可能的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060310889V龙的目击记录，在９００年前的\n',
            '利贝尔建国时期就已经有了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060310890V听说和现在不同，\n',
            '当时出现得相当频繁呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AEF')

    def _loc_1995(): pass

    label('loc_1995')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1A4C',
    )

    ChrTalk(
        0x0104,
        (
            '#0040310891V#035F#5P不，那是有可能的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040310892V#032F根据七耀教会的传说，\n',
            '龙是守护空之女神\n',
            '的圣兽。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040310893V这种存在，或许不是\n',
            '以我们的常识可以解释的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AEF')

    def _loc_1A4C(): pass

    label('loc_1A4C')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1AEF',
    )

    ChrTalk(
        0x0108,
        (
            '#0080310894V#074F#5P不，那是有可能的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080310895V#072F在东方，有很多人将龙\n',
            '视作神兽崇拜。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080310896V还是不要用一般人的常识来\n',
            '论断比较好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1AEF(): pass

    label('loc_1AEF')

    OP_62(0x0106, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0106,
        (
            '#0050310897V#055F……真的吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310898V#1007F#5P的、的确不要把它\n',
            '和普通的魔兽相提并论比较好呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3500310899V想将这样的家伙消灭？\n',
            '你们这种举动根本和自杀没区别。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3500310900V好了，总之这件事就交给\n',
            '军队去处理吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3500310901V虽然军队那群家伙也不怎么靠得住，\n',
            '但如果有那个男人在的话，也许…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310902V#1004F#5P哎……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3500310903V……不管怎么说，我可不愿意\n',
            '看着你们这些小家伙去白白送死。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3500310904V抱歉，我不能帮忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280758V#1026F#5P但，但是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050310906V#053F…………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050310907V#555F……喂，大叔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050310908V你的好意我们心领了，\n',
            '但你不觉得有点离题了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3500310909V……嗯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050310910V#050F我们遇到过\n',
            '棘手的敌人\n',
            '不是一次两次了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050310911V像之前的情报部，\n',
            '还有古代的人形兵器…',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050310912V#053F每一个也都是\n',
            '强大到令人绝望的对手。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050310913V但我们最终也都是克服重重困难\n',
            '合力战胜他们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3500310914V………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050310915V#051F这次的龙也是一样！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050310916V虽然它确实是前所未有的强敌，\n',
            '但我们也从没打算过去白白送死。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050310917V#053F所以……拜托了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050310918V无论如何请帮帮我们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0101, 270, 400)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010310919V#1025F#2P阿加特……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0107, 90, 400)
    Sleep(300)

    ChrTalk(
        0x0107,
        (
            '#0070310920V#560F#6P阿加特哥哥……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3500310921V呵呵……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3500310922V你什么时候变得\n',
            '这么能言善道了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3500310923V话都说到这个份上了，\n',
            '看来不帮你们也是不成的啦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050310924V#052F！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0101, 225, 400)
    OP_8C(0x0107, 180, 400)

    ChrTalk(
        0x0101,
        (
            '#0010310925V#1004F#5P真、真的吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070310926V#067F#5P谢、谢谢您了！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3500310927V哪里……\n',
            '没什么大不了的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3500310928V我有些准备工作要做，\n',
            '所以要先走一步了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3500310929V我会在西部最里侧等你们，\n',
            '跟过来就可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310930V#1015F#5P跟上来？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050310931V#555F喂！你直接把西北边的路\n',
            '告诉我们不就好了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3500310932V光是口头说说的话，\n',
            '大概你们也一样找不到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3500310933V总之你们到了峡谷西侧之后\n',
            '一直往深处走就是了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3500310934V我等着你们！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2276')
    def lambda_2276():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_2276')

    DispatchAsync2(0x0101, 0x0001, lambda_2276)

    @scena.Lambda('lambda_2287')
    def lambda_2287():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_2287')

    DispatchAsync2(0x0106, 0x0001, lambda_2287)

    @scena.Lambda('lambda_2298')
    def lambda_2298():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_2298')

    DispatchAsync2(0x0107, 0x0001, lambda_2298)

    @scena.Lambda('lambda_22A9')
    def lambda_22A9():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_22A9')

    DispatchAsync2(0x00F9, 0x0001, lambda_22A9)

    @scena.Lambda('lambda_22BA')
    def lambda_22BA():
        OP_6D(2020, 0, 36590, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_22BA)

    SetChrFlags(0x0008, 0x0004)
    OP_8E(0x0008, 3270, 0, 34950, 3000, 0x00)
    OP_8E(0x0008, 1280, 0, 36260, 3000, 0x00)
    OP_8E(0x0008, -4570, 0, 35920, 3000, 0x00)

    @scena.Lambda('lambda_2313')
    def lambda_2313():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000190)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2313)

    OP_8E(0x0008, -5490, 0, 35850, 3000, 0x00)
    ClearChrFlags(0x0008, 0x0004)
    SetChrFlags(0x0008, 0x0080)
    WaitForThreadExit(0x0101, 0x0002)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0106, 0x01)
    TerminateThread(0x0107, 0x01)
    TerminateThread(0x00F9, 0x01)

    ChrTalk(
        0x0101,
        (
            '#0010310935V#1020F#2P等、等一下……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_6D(3740, 0, 36060, 1500)

    ChrTalk(
        0x0106,
        (
            '#0050310936V#551F#5P……没办法。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050310937V#050F就照大叔说的\n',
            '跟过去吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310938V#1007F#2P是、是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010310939V#1002F嗯、是峡谷西侧\n',
            '最深处的地方对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2440')
    def lambda_2440():
        OP_8C(0x0107, 90, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_2440)

    @scena.Lambda('lambda_244E')
    def lambda_244E():
        OP_8C(0x00F9, 180, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_244E)

    OP_8C(0x0106, 90, 400)
    Sleep(500)

    ChrTalk(
        0x0106,
        (
            '#0050310940V#051F#6P啊啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050310941V这里的地形比较复杂，\n',
            '小心别迷路啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1A26)
    OP_28(0x0096, 0x01, 0x0040)
    OP_28(0x0096, 0x01, 0x0080)
    EventEnd(0x00)

    Return()

# id: 0x0006 offset: 0x24C5
@scena.Code('func_06_24C5')
def func_06_24C5():
    FadeOut(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x09, 0xFF)

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
        (0x00000000, 'loc_2542'),
        (0x00000001, 'loc_2548'),
        (-1, 'loc_254E'),
    )

    def _loc_2542(): pass

    label('loc_2542')

    OP_A2(0x1200)

    Jump('loc_254E')

    def _loc_2548(): pass

    label('loc_2548')

    OP_A2(0x1201)

    Jump('loc_254E')

    def _loc_254E(): pass

    label('loc_254E')

    Return()

# id: 0x0007 offset: 0x254F
@scena.Code('func_07_254F')
def func_07_254F():
    TalkBegin(0x00FF)
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
        'loc_25D7',
    )

    OP_26(13)
    OP_20(0x00000BB8)
    FadeOut(1000, 0, -1)
    OP_22(0x000D, 0x00, 0x64)
    OP_0D()
    SetChrStatus(0x00FF, 0xFE, 0)
    OP_69(0x0000, 0x00000000)
    OP_30(0x01)
    Sleep(3500)

    OP_1E()
    FadeIn(1000, 0)
    OP_56(0x00)
    TalkEnd(0x00FF)

    Return()

    def _loc_25D7(): pass

    label('loc_25D7')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_25F1',
    )

    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Return()

    def _loc_25F1(): pass

    label('loc_25F1')

    Return()

# id: 0x0008 offset: 0x25F2
@scena.Code('func_08_25F2')
def func_08_25F2():
    ClearMapFlags(0x00000001)
    OP_6D(97010, 0, 95840, 0)
    FadeIn(0, 0)
    Sleep(100)

    OP_C9(
        0x00,
        (
            0x0000,
            0x0005,
            0x0006,
            0x00FF,
        ),
        (
            0x0002,
            0x0003,
            0x0004,
            0x0007,
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

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0x00000000)
    Sleep(1000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
