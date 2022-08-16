import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T3131_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3131   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'T3131.x'
    header.mapIndex       = 1
    header.bgm            = 13
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
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
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH01270._CH', 'ED6_DT07/CH01270P._CP'),
        ('ED6_DT07/CH01003._CH', 'ED6_DT07/CH01003P._CP'),
    ]

# id: 0x10001 offset: 0xC2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '贝恩',
            x                   = -2470,
            z                   = -1000,
            y                   = 4710,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '乌尔斯',
            x                   = 5480,
            z                   = -1000,
            y                   = 5320,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '兰达老人',
            x                   = -450,
            z                   = -650,
            y                   = 2280,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0135,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
    )

# id: 0x10002 offset: 0x122
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x122
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x122
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -530,
            triggerZ            = -1000,
            triggerY            = 4660,
            triggerRange        = 400,
            actorX              = -2470,
            actorZ              = 500,
            actorY              = 4710,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x146
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_150',
    )

    Jump('loc_173')

    def _loc_150(): pass

    label('loc_150')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_15A',
    )

    Jump('loc_173')

    def _loc_15A(): pass

    label('loc_15A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_164',
    )

    Jump('loc_173')

    def _loc_164(): pass

    label('loc_164')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_16E',
    )

    Jump('loc_173')

    def _loc_16E(): pass

    label('loc_16E')

    ChrSetFlags(0x000A, 0x0080)

    def _loc_173(): pass

    label('loc_173')

    Return()

# id: 0x0001 offset: 0x174
@scena.Code('func_01_174')
def func_01_174():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1A8',
    )

    OP_72(0x0000, 0x0020)
    OP_72(0x0000, 0x0008)
    OP_72(0x0001, 0x0020)
    OP_72(0x0001, 0x0008)
    OP_72(0x0002, 0x0020)
    OP_72(0x0002, 0x0008)
    OP_72(0x0003, 0x0020)
    OP_72(0x0003, 0x0008)

    def _loc_1A8(): pass

    label('loc_1A8')

    Return()

# id: 0x0002 offset: 0x1A9
@scena.Code('func_02_1A9')
def func_02_1A9():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1CC',
    )

    OP_8D(0x00FE, 400, 5540, 5960, 4780, 2000)

    Jump('func_02_1A9')

    def _loc_1CC(): pass

    label('loc_1CC')

    Return()

# id: 0x0003 offset: 0x1CD
@scena.Code('func_03_1CD')
def func_03_1CD():
    Call(0, 0x0004)

    Return()

# id: 0x0004 offset: 0x1D2
@scena.Code('func_04_1D2')
def func_04_1D2():
    TalkBegin(0x0008)
    Call(6, 0x0004)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1EC',
    )

    OP_A9(0x9B)
    TalkEnd(0x0008)

    Return()

    def _loc_1EC(): pass

    label('loc_1EC')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1FD',
    )

    TalkEnd(0x0008)

    Return()

    def _loc_1FD(): pass

    label('loc_1FD')

    If(
        (
            (Expr.Eval, "OP_29(0x002B, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_20A',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_20A(): pass

    label('loc_20A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_296',
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
            TXT(0x00, '【◇完成过任务【新食材的收集】】\n'),
            TXT(0x01, '【◇没完成过任务【新食材的收集】】\n'),
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
        (0x00000000, 'loc_28A'),
        (0x00000001, 'loc_290'),
        (-1, 'loc_296'),
    )

    def _loc_28A(): pass

    label('loc_28A')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_296')

    def _loc_290(): pass

    label('loc_290')

    ClearScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_296')

    def _loc_296(): pass

    label('loc_296')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 6, 0x1426)),
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Or,
            Expr.Return,
        ),
        'loc_81F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_780',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_37B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_327',
    )

    ChrTalk(
        0x0008,
        (
            '你们也看见过\n',
            '那个浮游物体了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '听说那东西的上面\n',
            '有个城镇呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '简直像童话中的世界一样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Jump('loc_378')

    def _loc_327(): pass

    label('loc_327')

    ChrTalk(
        0x0008,
        (
            '听说那个浮游物体的上面\n',
            '有个城镇一样的东西呢',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '简直像童话中的世界一样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_378(): pass

    label('loc_378')

    Jump('loc_77D')

    def _loc_37B(): pass

    label('loc_37B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_45D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_413',
    )

    ChrTalk(
        0x0008,
        (
            '虽然空调不能用了，\n',
            '但正常营业还是没问题的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '毕竟这家店的精髓\n',
            '是明火烹调的料理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '就算导力没有了\n',
            '也不会受太大的影响。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Jump('loc_45A')

    def _loc_413(): pass

    label('loc_413')

    ChrTalk(
        0x0008,
        (
            '但正常营业还是没问题的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '毕竟这家店的精髓\n',
            '是明火烹调的料理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_45A(): pass

    label('loc_45A')

    Jump('loc_77D')

    def _loc_45D(): pass

    label('loc_45D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_53A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_4C4',
    )

    ChrTalk(
        0x0008,
        (
            '不会再发生地震了…\n',
            '这真是个好消息啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我的原则是——\n',
            '只要是好事就绝不怀疑。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_537')

    def _loc_4C4(): pass

    label('loc_4C4')

    ChrTurnDirection(0x0008, 0x000A, 0)

    ChrTalk(
        0x0008,
        (
            '不管怎样，\n',
            '不会再发生地震了…\n',
            '好消息是绝对不会有差错的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '老爷爷想得太多，\n',
            '所以脑袋秃得更快了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_537(): pass

    label('loc_537')

    Jump('loc_77D')

    def _loc_53A(): pass

    label('loc_53A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_605',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_5A5',
    )

    ChrTalk(
        0x0008,
        (
            '互不侵犯条约的签字仪式\n',
            '似乎也快到了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '要是从共和国来的客人\n',
            '因此而增多就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_602')

    def _loc_5A5(): pass

    label('loc_5A5')

    ChrTalk(
        0x0008,
        (
            '嗯，听说互不侵犯条约的\n',
            '签字仪式就要到了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '真期待共和国的客人\n',
            '会因此而增多啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_602(): pass

    label('loc_602')

    Jump('loc_77D')

    def _loc_605(): pass

    label('loc_605')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_6C8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_65C',
    )

    ChrTalk(
        0x0008,
        (
            '老爷爷的孙女都已经到了\n',
            '能工作的年龄了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '所以我也都\n',
            '老了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6C5')

    def _loc_65C(): pass

    label('loc_65C')

    ChrTalk(
        0x0008,
        (
            '呼～兰达爷爷的孙女\n',
            '都已经到了可以工作的年龄了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '呜呼，看来看来，我也\n',
            '快要变成一个老头子了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_6C5(): pass

    label('loc_6C5')

    Jump('loc_77D')

    def _loc_6C8(): pass

    label('loc_6C8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 0, 0x1408)),
            Expr.Return,
        ),
        'loc_77D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_723',
    )

    ChrTalk(
        0x0008,
        (
            '尽管如此\n',
            '地震真是好久没遇到了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '还好哪里都没有\n',
            '出现人员伤亡。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_77D')

    def _loc_723(): pass

    label('loc_723')

    ChrTalk(
        0x0008,
        (
            '噢，累了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我们这里有可以消除疲劳\n',
            '的特制料理哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '有兴趣的话来试试吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_77D(): pass

    label('loc_77D')

    Jump('loc_81C')

    def _loc_780(): pass

    label('loc_780')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_7E0',
    )

    ChrTalk(
        0x0008,
        (
            '现在的情况虽然很糟糕，\n',
            '但也只有努力度过难关了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '好啦～大家一起\n',
            '加油努力吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_81C')

    def _loc_7E0(): pass

    label('loc_7E0')

    ChrTalk(
        0x0008,
        (
            '肚子饿了的时候\n',
            '随时欢迎光临。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '那么，\n',
            '继续加油吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_81C(): pass

    label('loc_81C')

    Jump('loc_B61')

    def _loc_81F(): pass

    label('loc_81F')

    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x0008, 0x0101, 0)
    OP_63(0x0008)

    ChrTalk(
        0x0008,
        (
            '噢！我还以为是谁呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '这不是帮我找到苦西红柿\n',
            '的游击士们吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1011F啊，您还记得我们吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '当然记得了！\n',
            '你简直就是我的恩人嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我们的『苦西红柿料理』\n',
            '现在可是大受欢迎啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1004F哎哎………………！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1016F……不、不会吧？',
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
        'loc_9BF',
    )

    ChrTurnDirection(0x0107, 0x0101, 400)

    ChrTalk(
        0x0107,
        (
            '#064F嗯，是真的哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '中央工房的人\n',
            '几乎都来吃过了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#561F听说大家都是从营养学的角度\n',
            '考虑才会选它的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0107, 400)

    Jump('loc_A1D')

    def _loc_9BF(): pass

    label('loc_9BF')

    ChrTalk(
        0x0008,
        (
            '哈哈哈～没有骗人的啦。\n',
            '特别是在研究员群体中最受好评。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '在疲劳的时候吃这个\n',
            '很管用的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A1D(): pass

    label('loc_A1D')

    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#1007F嗯……还是很难理解呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '噢，难得来了，\n',
            '不如来尝尝最新的料理吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '当然是我请客！',
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
        'loc_AB8',
    )

    @scena.Lambda('lambda_0AB0')
    def lambda_0AB0():
        ChrTurnDirection(0x0107, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_0AB0)

    def _loc_AB8(): pass

    label('loc_AB8')

    ChrTurnDirection(0x0101, 0x0008, 400)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['苦西红柿三明治']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    AddItem(ItemTable['苦西红柿三明治'], 1)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x0008,
        (
            '吃了营养十足的料理\n',
            '今后也要继续加油啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '一定会精力十足，\n',
            '以后也会充满干劲！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    SetScenaFlags(ScenaFlag(0x0284, 6, 0x1426))
    def _loc_B61(): pass

    label('loc_B61')

    TalkEnd(0x0008)

    Return()

# id: 0x0005 offset: 0xB65
@scena.Code('func_05_B65')
def func_05_B65():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_C98',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C2D',
    )

    ChrTalk(
        0x00FE,
        (
            '中央工房为了恢复研究\n',
            '也一直在努力啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '露依赛那家伙最近\n',
            '早上很早就会出去工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '结果她的妹妹就\n',
            '只会给我添麻烦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……这么一想的话，\n',
            '导力停止现象还真是讨厌呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Jump('loc_C95')

    def _loc_C2D(): pass

    label('loc_C2D')

    ChrTalk(
        0x00FE,
        (
            '仔细想想的话，我会照顾她的妹妹，\n',
            '也全是因为这次的异变。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，换种眼光看的话，\n',
            '影响真是很大呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C95(): pass

    label('loc_C95')

    Jump('loc_10D8')

    def _loc_C98(): pass

    label('loc_C98')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_D95',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_D38',
    )

    ChrTalk(
        0x00FE,
        (
            '仔细想想，我们的店里\n',
            '并没有导力式的器具。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以今天还是可以\n',
            '像平时一样正常营业。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼～本来以为会停业休息\n',
            '还稍微期待了一下呢…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Jump('loc_D92')

    def _loc_D38(): pass

    label('loc_D38')

    ChrTalk(
        0x00FE,
        (
            '仔细想想，我们的店里\n',
            '并没有导力式的器具。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以今天还是可以\n',
            '像平时一样正常营业。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D92(): pass

    label('loc_D92')

    Jump('loc_10D8')

    def _loc_D95(): pass

    label('loc_D95')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_E4C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_DEE',
    )

    ChrTalk(
        0x00FE,
        (
            '乌缇总是一个人\n',
            '留在家呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对那种年龄的孩子来说\n',
            '肯定很寂寞吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E49')

    def _loc_DEE(): pass

    label('loc_DEE')

    ChrTalk(
        0x00FE,
        (
            '呼～等休息时间到了以后\n',
            '还要去露依赛家里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '留下看家的乌缇\n',
            '也许现在都已经饿了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_E49(): pass

    label('loc_E49')

    Jump('loc_10D8')

    def _loc_E4C(): pass

    label('loc_E4C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_F4E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_E9A',
    )

    ChrTalk(
        0x00FE,
        (
            '她出外工作的时候是谁\n',
            '替她照看妹妹？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还不都是我嘛！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F4B')

    def _loc_E9A(): pass

    label('loc_E9A')

    ChrTalk(
        0x00FE,
        (
            '露依赛也真是的，\n',
            '动不动就要出差呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这次听说是要去雷斯顿要塞\n',
            '修整飞船。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '等一下…\n',
            '仔细想想的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '她出外工作的时候是谁\n',
            '替她照看妹妹？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还不都是我嘛！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_F4B(): pass

    label('loc_F4B')

    Jump('loc_10D8')

    def _loc_F4E(): pass

    label('loc_F4E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_FF3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_FAF',
    )

    ChrTalk(
        0x00FE,
        (
            '我店里的盘子好像\n',
            '叠了很高呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样不管的话，\n',
            '再有地震可就全要摔碎了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FF0')

    def _loc_FAF(): pass

    label('loc_FAF')

    ChrTalk(
        0x00FE,
        (
            '呼，太好了。\n',
            '餐具全都没摔坏。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '多亏平时整理\n',
            '得好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_FF0(): pass

    label('loc_FF0')

    Jump('loc_10D8')

    def _loc_FF3(): pass

    label('loc_FF3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 0, 0x1408)),
            Expr.Return,
        ),
        'loc_10D8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_1052',
    )

    ChrTalk(
        0x00FE,
        (
            '我的女朋友在中央工房\n',
            '工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '刚才的地震\n',
            '没有造成重大伤亡算是万幸……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10D8')

    def _loc_1052(): pass

    label('loc_1052')

    ChrTalk(
        0x00FE,
        (
            '呼，比想象中摇动得更强啊，\n',
            '还真吓了一跳。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对了，露依赛\n',
            '好像说过今天要去工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，中央工房没有\n',
            '受到灾害再好不过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_10D8(): pass

    label('loc_10D8')

    TalkEnd(0x0009)

    Return()

# id: 0x0006 offset: 0x10DC
@scena.Code('func_06_10DC')
def func_06_10DC():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_11DA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1177',
    )

    ChrTalk(
        0x00FE,
        (
            '但那浮游物体…\n',
            '好像连工房的人也很有兴趣。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵～未知物体\n',
            '本来就是研究者的最爱啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……不过，这么悠闲\n',
            '真的没问题吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    Jump('loc_11D7')

    def _loc_1177(): pass

    label('loc_1177')

    ChrTalk(
        0x00FE,
        (
            '但那浮游物体…\n',
            '好像连工房的人也很有兴趣。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说心里话，难道研究\n',
            '真的不会因此而受影响吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_11D7(): pass

    label('loc_11D7')

    Jump('loc_166E')

    def _loc_11DA(): pass

    label('loc_11DA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_12DC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_127F',
    )

    ChrTalk(
        0x00FE,
        (
            '其实老板也很想用\n',
            '导力烤炉的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但刚开业的时候资金有限，\n',
            '买不起呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没想到现在却因祸得福，\n',
            '可以继续营业。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '果然是世事\n',
            '难料啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    Jump('loc_12D9')

    def _loc_127F(): pass

    label('loc_127F')

    ChrTalk(
        0x00FE,
        (
            '老板在刚开店的时候很穷，\n',
            '连导力炉都买不起。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过现在却因祸得福，\n',
            '可以照常营业。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_12D9(): pass

    label('loc_12D9')

    Jump('loc_166E')

    def _loc_12DC(): pass

    label('loc_12DC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_13D8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_135E',
    )

    ChrTalk(
        0x00FE,
        (
            '拉赛尔那老家伙现在肯定\n',
            '还在继续他的研究。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '地震什么的也根本不能\n',
            '打断他……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，果然是个\n',
            '一根筋呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_13D5')

    def _loc_135E(): pass

    label('loc_135E')

    ChrTalk(
        0x00FE,
        (
            '安全宣言虽然发表了，\n',
            '但还是不能放心…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '地震不会再发生了什么的，\n',
            '这种事很难确保吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯……果然很可疑。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_13D5(): pass

    label('loc_13D5')

    Jump('loc_166E')

    def _loc_13D8(): pass

    label('loc_13D8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_14FB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_1441',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯，果然牵连到\n',
            '和诸国的关系啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '选择保持外交往来，\n',
            '女王陛下真是很有先见之明。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_14F8')

    def _loc_1441(): pass

    label('loc_1441')

    ChrTalk(
        0x00FE,
        (
            '即使如此，导力器的\n',
            '出货仍然很受好评。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不但国内状况十分稳定，\n',
            '而且输出量也增加了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，果然牵连到\n',
            '和诸国的关系啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '选择保持外交往来，\n',
            '女王陛下真是很有先见之明。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_14F8(): pass

    label('loc_14F8')

    Jump('loc_166E')

    def _loc_14FB(): pass

    label('loc_14FB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_15B1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_1551',
    )

    ChrTalk(
        0x00FE,
        (
            '呼～我的孙女是个\n',
            '粗心大意的孩子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一定又会搞出什么乱子吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15AE')

    def _loc_1551(): pass

    label('loc_1551')

    ChrTalk(
        0x00FE,
        (
            '我孙女米优现在\n',
            '在中央工房帮忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不知道她能不能把工作干好，\n',
            '我瞎担心也是没用啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_15AE(): pass

    label('loc_15AE')

    Jump('loc_166E')

    def _loc_15B1(): pass

    label('loc_15B1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 0, 0x1408)),
            Expr.Return,
        ),
        'loc_166E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_1605',
    )

    ChrTalk(
        0x00FE,
        (
            '最近我的孙女\n',
            '也一直频繁出入中央工房。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真让人放心不下啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_166E')

    def _loc_1605(): pass

    label('loc_1605')

    ChrTalk(
        0x00FE,
        (
            '算啦，这种程度的摇晃\n',
            '应该还不至于影响到中央工房。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为地震事件，\n',
            '出现了接连不断的受害事件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_166E(): pass

    label('loc_166E')

    TalkEnd(0x000A)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
