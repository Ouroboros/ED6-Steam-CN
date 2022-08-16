import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T0510_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0510   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T0510.x'
    header.mapIndex       = 18
    header.bgm            = 16
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
        ('ED6_DT07/CH01300._CH', 'ED6_DT07/CH01300P._CP'),
        ('ED6_DT07/CH01310._CH', 'ED6_DT07/CH01310P._CP'),
    ]

# id: 0x10001 offset: 0xBA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '戴恩副队长',
            x                   = 26800,
            z                   = 0,
            y                   = 29900,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '阿斯顿队长',
            x                   = 29800,
            z                   = 0,
            y                   = -73400,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '阿维因队长',
            x                   = 29800,
            z                   = 0,
            y                   = -73400,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
    )

# id: 0x10002 offset: 0x11A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x11A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x11A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 28250,
            triggerZ            = 0,
            triggerY            = 29800,
            triggerRange        = 500,
            actorX              = 26800,
            actorZ              = 1500,
            actorY              = 29900,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 28310,
            triggerZ            = 0,
            triggerY            = -73420,
            triggerRange        = 500,
            actorX              = 29850,
            actorZ              = 1500,
            actorY              = -73420,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 20640,
            triggerZ            = 0,
            triggerY            = 33000,
            triggerRange        = 1000,
            actorX              = 20640,
            actorZ              = 1000,
            actorY              = 33000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x186
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_190',
    )

    Jump('loc_1A6')

    def _loc_190(): pass

    label('loc_190')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 7, 0x181F)),
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1A6',
    )

    ChrSetFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)

    def _loc_1A6(): pass

    label('loc_1A6')

    Return()

# id: 0x0001 offset: 0x1A7
@scena.Code('func_01_1A7')
def func_01_1A7():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1FC',
    )

    LoadEffect(0x00, 'map\\\\mp027_00.eff')
    PlayEffect(0x00, 0x00, 0x00FF, 20640, 1000, 33000, 0, 0, 0, 1300, 1300, 1300, 0x00FF, 0, 0, 0, 0)

    def _loc_1FC(): pass

    label('loc_1FC')

    Return()

# id: 0x0002 offset: 0x1FD
@scena.Code('func_02_1FD')
def func_02_1FD():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_212',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_1FD')

    def _loc_212(): pass

    label('loc_212')

    Return()

# id: 0x0003 offset: 0x213
@scena.Code('func_03_213')
def func_03_213():
    Call(0, 0x0004)

    Return()

# id: 0x0004 offset: 0x218
@scena.Code('func_04_218')
def func_04_218():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 5, 0x2085)),
            Expr.Return,
        ),
        'loc_330',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2D3',
    )

    ChrTalk(
        0x0008,
        (
            '哈肯大门那边的情况\n',
            '好像相当紧迫啊…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '间接性地进行联络，\n',
            '一直都是那么紧张戒备中。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '虽然刚刚签署完互不侵犯条约，\n',
            '但不管什么时候也不能对帝国掉以轻心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_32D')

    def _loc_2D3(): pass

    label('loc_2D3')

    ChrTalk(
        0x0008,
        (
            '哈肯大门那边的情况\n',
            '好像相当紧迫啊…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '间接性地进行联络，\n',
            '一直都是那么紧张戒备中。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_32D(): pass

    label('loc_32D')

    Jump('loc_68F')

    def _loc_330(): pass

    label('loc_330')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_3EB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3A8',
    )

    ChrTalk(
        0x0008,
        (
            '喔，是各位游击士啊。\n',
            '辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '现在路灯都熄灭了，\n',
            '到处也都很危险。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '旅行时要\n',
            '小心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_3E8')

    def _loc_3A8(): pass

    label('loc_3A8')

    ChrTalk(
        0x0008,
        (
            '现在路灯都熄灭了，\n',
            '到处也都很危险。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '旅行时要\n',
            '小心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3E8(): pass

    label('loc_3E8')

    Jump('loc_68F')

    def _loc_3EB(): pass

    label('loc_3EB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_4CB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_456',
    )

    ChrTalk(
        0x0008,
        (
            '虽然不知道具体过程，\n',
            '但龙的骚乱似乎已经平息了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '呼，不管怎样，\n',
            '总算是个好消息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4C8')

    def _loc_456(): pass

    label('loc_456')

    ChrTalk(
        0x0008,
        (
            '虽然不知道具体过程，\n',
            '但龙的骚乱似乎平息了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '好久没有收到\n',
            '新消息了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '最后总算是\n',
            '把事情解决了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_4C8(): pass

    label('loc_4C8')

    Jump('loc_68F')

    def _loc_4CB(): pass

    label('loc_4CB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_5A5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_528',
    )

    ChrTalk(
        0x0008,
        (
            '听说连飞行舰队\n',
            '也无法将龙捕获。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '果然没有卡西乌斯准将\n',
            '还是不行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5A2')

    def _loc_528(): pass

    label('loc_528')

    ChrTalk(
        0x0008,
        (
            '为了捕获飞龙，竟然连\n',
            '飞行舰队都出动了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '而且居然这样\n',
            '也无法把龙抓住。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '果然没有卡西乌斯准将\n',
            '还是不行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_5A2(): pass

    label('loc_5A2')

    Jump('loc_68F')

    def _loc_5A5(): pass

    label('loc_5A5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_68F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_600',
    )

    ChrTalk(
        0x0008,
        (
            '前几天大雾的时候\n',
            '真是辛苦得要死。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '虽然只是雾，\n',
            '但也不能轻视啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_68F')

    def _loc_600(): pass

    label('loc_600')

    ChrTalk(
        0x0008,
        (
            '前几天大雾的时候\n',
            '真是辛苦得要死。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '洛连特的警备\n',
            '一直人手不足。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '已经向哈肯大门\n',
            '请求支援了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '虽然只是雾，\n',
            '但也不能轻视啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_68F(): pass

    label('loc_68F')

    TalkEnd(0x0008)

    Return()

# id: 0x0005 offset: 0x693
@scena.Code('func_05_693')
def func_05_693():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 7, 0x181F)),
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_6A6',
    )

    Call(0, 0x0007)

    Jump('loc_6AA')

    def _loc_6A6(): pass

    label('loc_6A6')

    Call(0, 0x0006)

    def _loc_6AA(): pass

    label('loc_6AA')

    Return()

# id: 0x0006 offset: 0x6AB
@scena.Code('func_06_6AB')
def func_06_6AB():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_CE2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0415, 6, 0x20AE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_AA7',
    )

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_726',
    )

    ChrTalk(
        0x0009,
        (
            '呀！艾丝蒂尔和约修亚，\n',
            '连雪拉扎德也在啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '前一阵子的大雾事件\n',
            '真是多谢你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_76B')

    def _loc_726(): pass

    label('loc_726')

    ChrTalk(
        0x0009,
        (
            '呀！艾丝蒂尔和约修亚，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '前一阵子的大雾事件\n',
            '真是多谢你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_76B(): pass

    label('loc_76B')

    ChrTalk(
        0x0009,
        (
            '今天又在\n',
            '执行任务吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1000F啊、嗯。\n',
            '正是如此。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1040F这边的情况怎么样？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '现在看起来，关所的大门\n',
            '一直开着…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0102, 400)

    ChrTalk(
        0x0009,
        (
            '那大门是导力式的，\n',
            '现在连开关都成了问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '为了不阻碍交通，\n',
            '只能一直开着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1007F是吗……\n',
            '那也只能如此了。',
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
        'loc_8D1',
    )

    ChrTalk(
        0x0103,
        (
            '#022F辛苦了，\n',
            '警备工作就拜托您了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '现在也许还有些不老实的家伙\n',
            '正在蠢蠢欲动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0103, 400)

    Jump('loc_99E')

    def _loc_8D1(): pass

    label('loc_8D1')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_934',
    )

    ChrTalk(
        0x0106,
        (
            '#057F辛苦了，\n',
            '警备工作就拜托您了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '那些可恶的白痴至今\n',
            '仍在蠢蠢欲动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0106, 400)

    Jump('loc_99E')

    def _loc_934(): pass

    label('loc_934')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_99E',
    )

    ChrTalk(
        0x0108,
        (
            '#072F辛苦您了，\n',
            '警备工作就拜托了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '在这种情况下，\n',
            '还不知道潜伏了什么样的角色。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0108, 400)

    def _loc_99E(): pass

    label('loc_99E')

    ChrTalk(
        0x0009,
        (
            '嗯，上边也做出了\n',
            '这样的指示。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '虽然是很麻烦的工作，\n',
            '但为了保证这里的安全。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '也只能拼命\n',
            '努力了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1042F拜托您了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我们也会尽全力来\n',
            '结束这种事态的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0102, 400)

    ChrTalk(
        0x0009,
        (
            '如果没有你们的努力，\n',
            '想解决这次的事件根本不可能。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '我也拜托你们加油了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))
    SetScenaFlags(ScenaFlag(0x0415, 6, 0x20AE))

    Jump('loc_CDF')

    def _loc_AA7(): pass

    label('loc_AA7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 5, 0x2085)),
            Expr.Return,
        ),
        'loc_C4C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_B4B',
    )

    ChrTalk(
        0x0009,
        (
            '我们王国军警备队\n',
            '也在努力进行关所的警备工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '不过，你们游击士\n',
            '是可以自由通行的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '如果没有你们的努力，\n',
            '想解决这次的事件根本不可能。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C49')

    def _loc_B4B(): pass

    label('loc_B4B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_BEF',
    )

    ChrTalk(
        0x0009,
        (
            '听说有警备艇\n',
            '迫降在了米尔西街道。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '这要是平时的话，雷斯顿要塞\n',
            '马上就会派出救援部队…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '但现在根本\n',
            '做不到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '救援工作\n',
            '只能暂时放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Jump('loc_C49')

    def _loc_BEF(): pass

    label('loc_BEF')

    ChrTalk(
        0x0009,
        (
            '虽然对不起警备艇的各位，\n',
            '但现在也没办法救援啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '救援队现在的移动\n',
            '能力极其有限。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C49(): pass

    label('loc_C49')

    Jump('loc_CDF')

    def _loc_C4C(): pass

    label('loc_C4C')

    ChrTalk(
        0x0009,
        (
            '我们王国军警备队\n',
            '也在努力进行关所的警备工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '不过，你们游击士\n',
            '是可以自由通行的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '如果没有你们的努力，\n',
            '想解决这次的事件根本不可能。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_CDF(): pass

    label('loc_CDF')

    Jump('loc_124D')

    def _loc_CE2(): pass

    label('loc_CE2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_EBE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x034D, 1, 0x1A69)),
            Expr.Return,
        ),
        'loc_D4D',
    )

    ChrTalk(
        0x0009,
        (
            '接下来也要靠你们\n',
            '游击士的努力了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '我们双方携手努力的话，\n',
            '一定可以让王国和平的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EBB')

    def _loc_D4D(): pass

    label('loc_D4D')

    OP_62(0x0009, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x0009, 0x0101, 0)
    Sleep(400)

    ChrTalk(
        0x0009,
        (
            '啊，艾丝蒂尔，\n',
            '还有雪拉扎德。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '这次也多谢你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '鲁克那小家伙\n',
            '也恢复了意识。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1017F嘿嘿，哪里的话，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '多亏阿斯顿先生\n',
            '帮忙保护城镇啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '哈哈，这些话我会\n',
            '转告给部下们的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '接下来也要靠你们\n',
            '游击士的努力了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '我们双方携手努力的话，\n',
            '一定可以让王国和平的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1006F嗯，拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F我们也拜托您了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x034D, 1, 0x1A69))

    def _loc_EBB(): pass

    label('loc_EBB')

    Jump('loc_124D')

    def _loc_EBE(): pass

    label('loc_EBE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_124D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0310, 7, 0x1887)),
            Expr.Return,
        ),
        'loc_F38',
    )

    ChrTalk(
        0x0009,
        (
            '定期船都停航了，\n',
            '看来雾很厉害呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '我们军队\n',
            '也会思索对策的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '总之现在大家\n',
            '要携手度过难关。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_124D')

    def _loc_F38(): pass

    label('loc_F38')

    OP_62(0x0009, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x0009, 0x0101, 0)
    Sleep(400)

    ChrTalk(
        0x0009,
        (
            '啊，艾丝蒂尔\n',
            '好久不见呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1001F好久不见了，阿斯顿先生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '协会有工作吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '现在要办通行手续的话\n',
            '要花些时间了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1015F啊、没关系，\n',
            '今天并不准备通行……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1011F办理手续需要花一些时间？\n',
            '难道是出了什么事情吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '那倒没有，只是受空贼艇抢夺\n',
            '事件的影响。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '所以上面下达了\n',
            '强化警备的指示。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1004F是、是这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#022F原来如此……\n',
            '军队也加强警备了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0103, 400)

    ChrTalk(
        0x0009,
        (
            '其实只是个形式而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '比起那个，\n',
            '我更在意洛连特的雾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '定期船都停航了，\n',
            '似乎浓得很不寻常啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1002F嗯，其实我们\n',
            '也在调查这阵大雾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0101, 400)

    ChrTalk(
        0x0009,
        (
            '原来如此，因为这个\n',
            '才来这里的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '要是有什么情况，\n',
            '就和军队也进行一下联络。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '这种时候\n',
            '才能体现出合作关系的重要。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F嗯，明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '那么，调查的事情\n',
            '就拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1006F嗯，先这么说啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0310, 7, 0x1887))

    def _loc_124D(): pass

    label('loc_124D')

    TalkEnd(0x0009)

    Return()

# id: 0x0007 offset: 0x1251
@scena.Code('func_07_1251')
def func_07_1251():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 7, 0x181F)),
            Expr.Return,
        ),
        'loc_1388',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_12BD',
    )

    ChrTalk(
        0x000A,
        (
            '在阿斯顿队长回来之前\n',
            '这里就由我们守备了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '任务很艰巨，\n',
            '所以一定要认真对待啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1388')

    def _loc_12BD(): pass

    label('loc_12BD')

    ChrTalk(
        0x000A,
        (
            '我们是从哈肯大门那边调派来这里\n',
            '暂时代替阿斯顿队长进行警备。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '在洛连特的警备结束前\n',
            '这里就交给我们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '在大雾中发生了什么事呢？\n',
            '真是让人不解。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '现在还不能放松警备，\n',
            '要多提醒部下才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_1388(): pass

    label('loc_1388')

    TalkEnd(0x000A)

    Return()

# id: 0x0008 offset: 0x138C
@scena.Code('func_08_138C')
def func_08_138C():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_13DF',
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

    Jump('loc_159A')

    def _loc_13DF(): pass

    label('loc_13DF')

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
        'loc_157F',
    )

    FadeIn(100, 0)
    Sleep(500)

    OP_26(13)
    StopEffect(0x00, 0x02)
    PlayEffect(0x00, 0x00, 0x00FF, 20640, 1000, 33000, 0, 0, 0, 700, 700, 700, 0x00FF, 0, 0, 0, 0)
    OP_6F(0x0001, 0)
    OP_70(0x0001, 50)
    OP_73(0x0001)
    OP_20(0x00000BB8)
    PlaySE(12, 0x00, 0x64)
    StopEffect(0x00, 0x02)
    LoadEffect(0x01, 'map\\\\mp027_01.eff')
    PlayEffect(0x01, 0x01, 0x00FF, 20640, 1000, 33000, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    FadeOut(1000, 0, -1)
    Sleep(700)

    PlaySE(13, 0x00, 0x64)
    OP_0D()
    ChrSetStatus(0x00FF, 0xFE, 0)
    OP_69(0x0000, 0)
    OP_30(0x01)
    Sleep(3500)

    StopEffect(0x01, 0x02)
    PlayEffect(0x00, 0x00, 0x00FF, 20640, 1000, 33000, 0, 0, 0, 1300, 1300, 1300, 0x00FF, 0, 0, 0, 0)
    OP_6F(0x0001, 0)
    OP_1E()
    FadeIn(1000, 0)
    OP_56(0x00)
    TalkEnd(0x00FF)

    Return()

    def _loc_157F(): pass

    label('loc_157F')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1599',
    )

    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Return()

    def _loc_1599(): pass

    label('loc_1599')

    Return()

    def _loc_159A(): pass

    label('loc_159A')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
