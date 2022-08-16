import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T2132_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2132_1 ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'T2132.x'
    header.mapIndex       = 1
    header.bgm            = 12
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
            word_30         = 35,
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
    ChrTurnDirection(0x000E, 0x0000, 0)
    ChrTurnDirection(0x0000, 0x000E, 0)
    ChrTurnDirection(0x0001, 0x000E, 0)
    ChrTurnDirection(0x0002, 0x000E, 0)
    ChrTurnDirection(0x0003, 0x000E, 0)

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_19E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_145',
    )

    ChrTalk(
        0x000E,
        (
            '#2840441017V不过，怀疑昆茨\n',
            '看来是太草率了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#2840441018V关于这件事有机会\n',
            '一定要向他道歉……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19B')

    def _loc_145(): pass

    label('loc_145')

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x000E,
        (
            '#2840441019V哎呀，各位。\n',
            '今天非常感谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#2840441020V让我再次向你们道谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_19B(): pass

    label('loc_19B')

    Jump('loc_546')

    def _loc_19E(): pass

    label('loc_19E')

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x00, 0x40)"),
            Expr.Return,
        ),
        'loc_20F',
    )

    ChrTalk(
        0x000E,
        (
            '#2840441021V啊，游击士。\n',
            '今天真是辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#2840441022V以后再有什么事情的话\n',
            '还请多多关照。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_546')

    def _loc_20F(): pass

    label('loc_20F')

    If(
        (
            (Expr.Eval, "OP_29(0x006A, 0x01, 0x4000)"),
            Expr.Return,
        ),
        'loc_44D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_224',
    )

    Jump('loc_242')

    def _loc_224(): pass

    label('loc_224')

    ChrTalk(
        0x000E,
        (
            '#2840441007V咦？不们……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_242(): pass

    label('loc_242')

    ChrTalk(
        0x000E,
        (
            '#2840441008V你们\n',
            '能帮忙调查吗？',
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
            TXT(0x00, '【是】\n'),
            TXT(0x01, '【否】\n'),
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
        'loc_3A0',
    )

    ChrTalk(
        0x0101,
        (
            '#0010440863V#1006F嗯，没问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000E, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrTurnDirection(0x000E, 0x0101, 400)
    Sleep(1000)

    ChrTalk(
        0x000E,
        (
            '#2840441010V真、真的吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#2840440864V谢谢，我会记着这份人情的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#2840441012V来，进来吧。\n',
            '马上来介绍给你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    Sleep(1000)

    Call(1, 0x0004)
    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    Jump('loc_44A')

    def _loc_3A0(): pass

    label('loc_3A0')

    ChrTalk(
        0x0101,
        (
            '#0010441013V#1007F对、对不起。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441014V还是不行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000E, 0x0101, 400)

    ChrTalk(
        0x000E,
        (
            '#2840441015V那、那样啊…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#2840441016V没办法，我就先放弃了，\n',
            '等其它的游击士们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))
    ChrSetDirection(0x000E, 90, 0)

    def _loc_44A(): pass

    label('loc_44A')

    Jump('loc_546')

    def _loc_44D(): pass

    label('loc_44D')

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x00, 0x08)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_546',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_4C0',
    )

    ChrTalk(
        0x000E,
        (
            '现在在进行重要的会议，\n',
            '很遗憾我不能让你们进去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '十分抱歉，\n',
            '如果有事的话请以后再来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_53F')

    def _loc_4C0(): pass

    label('loc_4C0')

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x000E,
        (
            '这里是诺曼的选举事务所。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '现在在进行重要的会议，\n',
            '很遗憾我不能让你们进去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '十分抱歉，如果有事的话\n',
            '请以后再来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_53F(): pass

    label('loc_53F')

    ChrSetDirection(0x000E, 90, 0)

    def _loc_546(): pass

    label('loc_546')

    Return()

# id: 0x0001 offset: 0x547
@scena.Code('func_01_547')
def func_01_547():
    ClearScenaFlags(ScenaFlag(0x0001, 2, 0xA))
    OP_4A(0x000E, 0)

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x00, 0x08)"),
            (Expr.Eval, "OP_29(0x0069, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0069, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_138D',
    )

    TalkBegin(0x000E)
    Call(1, 0x0005)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_598'),
        (0x00000001, 'loc_697'),
        (0x00000002, 'loc_8EE'),
        (0x00000003, 'loc_9AE'),
        (0x00000004, 'loc_ABF'),
        (0x00000005, 'loc_F61'),
        (0x00000006, 'loc_112E'),
        (0x00000007, 'loc_12A5'),
        (-1, 'loc_1384'),
    )

    def _loc_598(): pass

    label('loc_598')

    OP_28(0x006A, 0x01, 0x0400)

    If(
        (
            (Expr.PushReg, 0x7),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_612',
    )

    ChrTalk(
        0x00FE,
        (
            '#2840441023V那时昆茨先生的\n',
            '表情非常吃惊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2840441024V自己的罪行被目击了，\n',
            '吃惊也很正常。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_694')

    def _loc_612(): pass

    label('loc_612')

    ExecExpressionWithReg(
        0x0007,
        (
            (Expr.PushLong, 0x1),
            Expr.Or2,
            Expr.Return,
        ),
    )

    ChrTalk(
        0x00FE,
        (
            '#2840441025V一看到我们\n',
            '昆茨先生就露出了吃惊的表情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2840441026V一定是因为自己的罪行被目击了\n',
            '就惊惶失措了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_694(): pass

    label('loc_694')

    Jump('loc_1387')

    def _loc_697(): pass

    label('loc_697')

    OP_28(0x006A, 0x01, 0x0400)

    If(
        (
            (Expr.PushReg, 0x7),
            (Expr.PushLong, 0x2),
            Expr.And,
            Expr.Return,
        ),
        'loc_773',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x01, 0x0004)"),
            Expr.Return,
        ),
        'loc_712',
    )

    ChrTalk(
        0x00FE,
        (
            '#2840441027V我没听到过\n',
            '那么大的声响。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2840441028V我能断言我在\n',
            '那里时没听到过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_770')

    def _loc_712(): pass

    label('loc_712')

    ChrTalk(
        0x00FE,
        (
            '#2840441029V房间里确实\n',
            '一直都很安静。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2840441030V如果有口角的话\n',
            '我一定会注意到的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_770(): pass

    label('loc_770')

    Jump('loc_8EB')

    def _loc_773(): pass

    label('loc_773')

    ExecExpressionWithReg(
        0x0007,
        (
            (Expr.PushLong, 0x2),
            Expr.Or2,
            Expr.Return,
        ),
    )

    ChrTalk(
        0x00FE,
        (
            '#2840441031V确、确实如\n',
            '昆茨先生所说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2840441032V我在门口守着，\n',
            '不过房间里一直都很安静。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2840441033V如果有口角的话\n',
            '我一定会注意到的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x01, 0x0004)"),
            Expr.Return,
        ),
        'loc_8EB',
    )

    ChrTalk(
        0x0101,
        (
            '#0010441034V#1015F可是说到巨大的响声，\n',
            '有人可以作证呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441035V#1002F说是在阳台下听到了\n',
            '物体碰撞的声音哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#2840441036V不，我没听见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2840441028V我能断言我在\n',
            '那里时没听到过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8EB(): pass

    label('loc_8EB')

    Jump('loc_1387')

    def _loc_8EE(): pass

    label('loc_8EE')

    OP_28(0x006A, 0x01, 0x0400)

    If(
        (
            (Expr.PushReg, 0x7),
            (Expr.PushLong, 0x4),
            Expr.And,
            Expr.Return,
        ),
        'loc_958',
    )

    ChrTalk(
        0x00FE,
        (
            '#2840441038V昆茨先生和平时\n',
            '没什么两样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2840441039V也看不出\n',
            '他在生气……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9AB')

    def _loc_958(): pass

    label('loc_958')

    ExecExpressionWithReg(
        0x0007,
        (
            (Expr.PushLong, 0x4),
            Expr.Or2,
            Expr.Return,
        ),
    )

    ChrTalk(
        0x00FE,
        (
            '#2840441040V昆茨先生生气了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2840441041V不过我可没\n',
            '看出来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9AB(): pass

    label('loc_9AB')

    Jump('loc_1387')

    def _loc_9AE(): pass

    label('loc_9AE')

    OP_28(0x006A, 0x01, 0x0400)

    If(
        (
            (Expr.PushReg, 0x7),
            (Expr.PushLong, 0x8),
            Expr.And,
            Expr.Return,
        ),
        'loc_A22',
    )

    ChrTalk(
        0x00FE,
        (
            '#2840441042V我也是人啊，\n',
            '也会有脸色不好的时候。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2840441043V但是那跟案子\n',
            '没关系吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_ABC')

    def _loc_A22(): pass

    label('loc_A22')

    ExecExpressionWithReg(
        0x0007,
        (
            (Expr.PushLong, 0x8),
            Expr.Or2,
            Expr.Return,
        ),
    )

    ChrTalk(
        0x00FE,
        (
            '#2840441044V说我脸色不好？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2840441045V那、那也是没办法的吧，\n',
            '因为遇上了那样的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2840441046V那么，这和案子\n',
            '又有什么关系呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_ABC(): pass

    label('loc_ABC')

    Jump('loc_1387')

    def _loc_ABF(): pass

    label('loc_ABF')

    OP_28(0x006A, 0x01, 0x0400)

    If(
        (
            (Expr.PushReg, 0x7),
            (Expr.PushLong, 0x20),
            Expr.And,
            (Expr.Eval, "OP_29(0x0069, 0x01, 0x0020)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_BCF',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x01, 0x0020)"),
            Expr.Return,
        ),
        'loc_B64',
    )

    ChrTalk(
        0x00FE,
        (
            '#2840441047V我确实上了２楼，\n',
            '不过只是因为有东西忘在那里了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2840441048V反正是无关紧要的事，\n',
            '我也没特意告诉你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BCC')

    def _loc_B64(): pass

    label('loc_B64')

    ChrTalk(
        0x00FE,
        (
            '#2840441049V午饭之后，我和诺曼先生\n',
            '去演说的地方预练了一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2840441050V虽然我有事\n',
            '迟到了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BCC(): pass

    label('loc_BCC')

    Jump('loc_F5E')

    def _loc_BCF(): pass

    label('loc_BCF')

    ExecExpressionWithReg(
        0x0007,
        (
            (Expr.PushLong, 0x20),
            Expr.Or2,
            Expr.Return,
        ),
    )

    ChrTalk(
        0x00FE,
        (
            '#2840441049V午饭之后，我和诺曼先生\n',
            '去演说的地方预练了一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2840441050V虽然我有事\n',
            '迟到了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2840441053V后来就和我前面说过的一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x01, 0x0010)"),
            Expr.Return,
        ),
        'loc_F5E',
    )

    OP_28(0x0069, 0x01, 0x0020)

    ChrTalk(
        0x0101,
        (
            '#0010441054V#1002F……不过，海利欧先生。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441055V你在此之前上了２楼吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrTurnDirection(0x00FE, 0x0101, 400)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '#2840441056V啊……！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010441057V#1002F隐瞒也没用。\n',
            '有人目击到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '#2840441058V我、我没有隐瞒！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2840441059V我、我只是想起有东西忘在事务所，\n',
            '所以就急忙回去了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010441060V#1002F那时候事务所里有些什么人？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2840441061V德尔斯在里面工作啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2840441062V我没看见其它人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010441063V#1000F嗯，了解到这些就够了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2840441064V那、那个……\n',
            '请别误解啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2840441065V我并无意要\n',
            '隐瞒上２楼的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010441066V#1010F不用担心。\n',
            '我们也没确定谁是犯人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441067V#1002F不过，希望你能明白\n',
            '这么做会使自己变得不利。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441068V那么，今后也请尽量合作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F5E(): pass

    label('loc_F5E')

    Jump('loc_1387')

    def _loc_F61(): pass

    label('loc_F61')

    OP_28(0x006A, 0x01, 0x0400)

    ChrTalk(
        0x00FE,
        (
            '#2840441069V我在外面听到过钟声。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2840441070V应该是在桥边遇见\n',
            '诺曼先生的时候。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2840441071V然后昆茨先生也来了，\n',
            '我就把他带到了这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x01, 0x0200)"),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x0069, 0x01, 0x0080)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_112B',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x01, 0x0400)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_10EE',
    )

    OP_28(0x0069, 0x01, 0x0200)

    ChrTalk(
        0x0101,
        (
            '#0010441072V#1015F海利欧先生在外面\n',
            '听到了钟声……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441073V就是说和那个响声无关了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060441074V#042F根据证词，响声发生在\n',
            '钟声刚结束之后……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060441075V如果这话是真的，\n',
            '那就是无关的了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_112B')

    def _loc_10EE(): pass

    label('loc_10EE')

    ChrTalk(
        0x0101,
        (
            '#0010441076V#1002F原来如此……\n',
            '和诺曼先生的证词一致呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_112B(): pass

    label('loc_112B')

    Jump('loc_1387')

    def _loc_112E(): pass

    label('loc_112E')

    OP_28(0x006A, 0x01, 0x0400)

    If(
        (
            (Expr.PushReg, 0x7),
            (Expr.PushLong, 0x40),
            Expr.And,
            Expr.Return,
        ),
        'loc_11AA',
    )

    ChrTalk(
        0x00FE,
        (
            '#2840441077V看来是在我出去的\n',
            '时候有人做了收拾善后。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2840441078V亚内斯特以往\n',
            '就是这么做的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12A2')

    def _loc_11AA(): pass

    label('loc_11AA')

    ExecExpressionWithReg(
        0x0007,
        (
            (Expr.PushLong, 0x40),
            Expr.Or2,
            Expr.Return,
        ),
    )

    ChrTalk(
        0x00FE,
        (
            '#2840441079V收拾善后？\n',
            '我不知道。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2840441080V大概，在我外出期间\n',
            '有人做了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010441081V#1002F在你外出前回到事务所时，\n',
            '餐具已经被收拾好了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2840441082V嗯，让我想想……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2840441083V我没仔细看，\n',
            '所以也说不清楚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_12A2(): pass

    label('loc_12A2')

    Jump('loc_1387')

    def _loc_12A5(): pass

    label('loc_12A5')

    OP_28(0x006A, 0x01, 0x0400)

    If(
        (
            (Expr.PushReg, 0x7),
            (Expr.PushLong, 0x80),
            Expr.And,
            Expr.Return,
        ),
        'loc_1319',
    )

    ChrTalk(
        0x00FE,
        (
            '#2840441084V你问我贝尔夫在哪里\n',
            '我也不知道啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2840441085V因为钟响的时候\n',
            '我出去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1381')

    def _loc_1319(): pass

    label('loc_1319')

    ExecExpressionWithReg(
        0x0007,
        (
            (Expr.PushLong, 0x80),
            Expr.Or2,
            Expr.Return,
        ),
    )

    ChrTalk(
        0x00FE,
        (
            '#2840441086V钟响的时候\n',
            '贝尔夫在哪里？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2840441087V那个我不知道。\n',
            '因为当时我出去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1381(): pass

    label('loc_1381')

    Jump('loc_1387')

    def _loc_1384(): pass

    label('loc_1384')

    Jump('loc_1387')

    def _loc_1387(): pass

    label('loc_1387')

    TalkEnd(0x000E)

    Jump('loc_13BD')

    def _loc_138D(): pass

    label('loc_138D')

    If(
        (
            (Expr.Eval, "OP_29(0x006A, 0x01, 0x4000)"),
            (Expr.Eval, "OP_29(0x0069, 0x00, 0x08)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_13B3',
    )

    EventBegin(0x02)
    Call(1, 0x0000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_13B0',
    )

    EventEnd(0x03)

    def _loc_13B0(): pass

    label('loc_13B0')

    Jump('loc_13BD')

    def _loc_13B3(): pass

    label('loc_13B3')

    TalkBegin(0x000E)
    Call(1, 0x0000)
    TalkEnd(0x000E)
    def _loc_13BD(): pass

    label('loc_13BD')

    OP_4B(0x000E, 0)

    Return()

# id: 0x0002 offset: 0x13C2
@scena.Code('func_02_13C2')
def func_02_13C2():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_13CA',
    )

    Return()

    def _loc_13CA(): pass

    label('loc_13CA')

    ClearScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            (Expr.Eval, "OP_29(0x0069, 0x00, 0x08)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1472',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x006A, 0x01, 0x4000)"),
            Expr.Return,
        ),
        'loc_1434',
    )

    EventBegin(0x01)
    ChrTurnDirection(0x000E, 0x0000, 0)
    ChrTurnDirection(0x0000, 0x000E, 0)
    OP_4A(0x000E, 0)
    Call(1, 0x0000)
    OP_4B(0x000E, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1430',
    )

    ChrSetDirection(0x000E, 90, 0)
    ChrMoveToRelative(0x0000, 1000, 0, 0, 2000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Jump('loc_1431')

    def _loc_1430(): pass

    label('loc_1430')

    Return()

    def _loc_1431(): pass

    label('loc_1431')

    Jump('loc_1472')

    def _loc_1434(): pass

    label('loc_1434')

    EventBegin(0x01)
    ChrTurnDirection(0x000E, 0x0000, 0)
    ChrTurnDirection(0x0000, 0x000E, 0)
    OP_4A(0x000E, 255)
    Call(1, 0x0000)
    ChrSetDirection(0x000E, 90, 0)
    OP_4B(0x000E, 255)
    ChrMoveToRelative(0x0000, 1000, 0, 0, 2000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_1472(): pass

    label('loc_1472')

    Return()

# id: 0x0003 offset: 0x1473
@scena.Code('func_03_1473')
def func_03_1473():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_147B',
    )

    Return()

    def _loc_147B(): pass

    label('loc_147B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 1, 0x1401)),
            (Expr.Eval, "OP_29(0x006A, 0x01, 0x8000)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1B0B',
    )

    EventBegin(0x00)
    OP_4A(0x000E, 0)
    ChrSetRGBAMask(0x000E, 255, 255, 255, 0, 0)
    ChrSetPos(0x000E, -2340, 0, 9540, 180)
    FadeOut(500, 0, -1)
    OP_0D()
    OP_28(0x006A, 0x01, 0x8000)
    CameraMove(1780, 0, 2230, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(35000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 4450, 0, 2400, 270)
    ChrSetPos(0x00F7, 5150, -50, 1910, 270)
    ChrSetPos(0x0104, 5700, -550, 2370, 270)
    ChrSetPos(0x0105, 6350, -1050, 1780, 270)
    CreateThread(0x0101, 0x01, 0x01, 0x001F)
    Sleep(300)

    CreateThread(0x00F7, 0x01, 0x01, 0x0020)
    Sleep(300)

    CreateThread(0x0104, 0x01, 0x01, 0x0021)
    Sleep(300)

    CreateThread(0x0105, 0x01, 0x01, 0x0022)
    FadeIn(1000, 0)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0001)

    NpcTalk(
        0x000E,
        '青年的声音',
        (
            '#2840440846V啊！你、你们！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetRGBAMask(0x000E, 255, 255, 255, 255, 1000)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_15CC')
    def lambda_15CC():
        ChrTurnDirection(0x00FE, 0x000E, 400)
        Yield()

        Jump('lambda_15CC')

    DispatchAsync2(0x0101, 0x0001, lambda_15CC)

    Sleep(200)

    @scena.Lambda('lambda_15E2')
    def lambda_15E2():
        ChrTurnDirection(0x00FE, 0x000E, 400)
        Yield()

        Jump('lambda_15E2')

    DispatchAsync2(0x00F7, 0x0001, lambda_15E2)

    @scena.Lambda('lambda_15F3')
    def lambda_15F3():
        ChrTurnDirection(0x00FE, 0x000E, 400)
        Yield()

        Jump('lambda_15F3')

    DispatchAsync2(0x0104, 0x0001, lambda_15F3)

    @scena.Lambda('lambda_1604')
    def lambda_1604():
        ChrTurnDirection(0x00FE, 0x000E, 400)
        Yield()

        Jump('lambda_1604')

    DispatchAsync2(0x0105, 0x0001, lambda_1604)

    CameraMove(-1610, 0, 6840, 2000)

    @scena.Lambda('lambda_1626')
    def lambda_1626():
        CameraMove(-170, 0, 2320, 2000)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_1626)

    ChrWalkTo(0x000E, -820, 0, 2280, 3000, 0x00)
    WaitForThreadExit(0x000E, 0x0001)
    ChrTurnDirection(0x000E, 0x0101, 400)
    WaitForThreadExit(0x000E, 0x0002)
    TerminateThread(0x0000, 0x01)
    TerminateThread(0x0001, 0x01)
    TerminateThread(0x0002, 0x01)
    TerminateThread(0x0003, 0x01)

    ChrTalk(
        0x000E,
        (
            '#2840440847V呼～呼～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#2840440848V你、你们是游击士吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010440849V#1002F是的……有什么问题吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440850V你好像很慌乱呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#2840440851V我、我有事想请你们\n',
            '马上调查……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#2840440852V能不能马上跟我来？',
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
            TXT(0x01, '【不】\n'),
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
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_19E3',
    )

    ChrTalk(
        0x0101,
        (
            '#0010440853V#1015F抱歉啊，现在不行。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440854V我们正准备\n',
            '出发去其它地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#2840440855V啊，是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_183F',
    )

    ChrTalk(
        0x0106,
        (
            '#0050440856V#050F你联络协会了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1871')

    def _loc_183F(): pass

    label('loc_183F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_1871',
    )

    ChrTalk(
        0x0103,
        (
            '#0030440857V#022F你已经联络协会了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1871(): pass

    label('loc_1871')

    ChrTalk(
        0x000E,
        (
            '#2840440858V嗯，刚联络过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#2840440859V没办法，我就等\n',
            '其它游击士来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010440860V#1007F真的很抱歉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#2840440861V没关系，大家都很忙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#2840440862V那我就先告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1936')
    def lambda_1936():
        ChrTurnDirection(0x00FE, 0x000E, 0)
        Yield()

        Jump('lambda_1936')

    DispatchAsync2(0x0000, 0x0001, lambda_1936)

    @scena.Lambda('lambda_1947')
    def lambda_1947():
        ChrTurnDirection(0x00FE, 0x000E, 0)
        Yield()

        Jump('lambda_1947')

    DispatchAsync2(0x0001, 0x0001, lambda_1947)

    @scena.Lambda('lambda_1958')
    def lambda_1958():
        ChrTurnDirection(0x00FE, 0x000E, 0)
        Yield()

        Jump('lambda_1958')

    DispatchAsync2(0x0002, 0x0001, lambda_1958)

    @scena.Lambda('lambda_1969')
    def lambda_1969():
        ChrTurnDirection(0x00FE, 0x000E, 0)
        Yield()

        Jump('lambda_1969')

    DispatchAsync2(0x0003, 0x0001, lambda_1969)

    ChrWalkTo(0x000E, 1500, 0, 130, 2000, 0x00)
    ChrWalkTo(0x000E, 5950, 2250, 160, 2000, 0x00)
    TerminateThread(0x0000, 0x01)
    TerminateThread(0x0001, 0x01)
    TerminateThread(0x0002, 0x01)
    TerminateThread(0x0003, 0x01)
    ChrWalkTo(0x000E, 5950, 2250, 1970, 2000, 0x00)
    Sleep(400)

    ChrSetPos(0x000E, 22470, 0, 76980, 90)
    OP_28(0x006A, 0x01, 0x4000)
    OP_4B(0x000E, 255)
    EventEnd(0x00)

    Return()

    def _loc_19E3(): pass

    label('loc_19E3')

    ChrTalk(
        0x0101,
        (
            '#0010440863V#1006F嗯，没问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#2840440864V谢谢，我会记着这份人情的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_1A68',
    )

    ChrTalk(
        0x0106,
        (
            '#0050440865V#050F那么我们应该去哪里？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A9A')

    def _loc_1A68(): pass

    label('loc_1A68')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_1A9A',
    )

    ChrTalk(
        0x0103,
        (
            '#0030440866V#020F那么我们应该去哪里？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A9A(): pass

    label('loc_1A9A')

    ChrTalk(
        0x000E,
        (
            '#2840440867V去这座酒店最顶层的\n',
            '诺曼先生选举事务所。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#2840440868V我立刻带你们去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    Sleep(1000)

    Call(1, 0x0004)
    EventEnd(0x00)

    def _loc_1B0B(): pass

    label('loc_1B0B')

    Return()

# id: 0x0004 offset: 0x1B0C
@scena.Code('func_04_1B0C')
def func_04_1B0C():
    ChrClearFlags(0x0014, 0x0080)
    ChrClearFlags(0x001A, 0x0080)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetPos(0x0000, 1500, 0, 79940, 274)
    ChrSetPos(0x000B, -3200, 0, 81000, 90)
    ChrSetPos(0x0014, -2140, 0, 81000, 270)
    CameraMove(-2540, 0, 80960, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(35000, 0)
    OP_6E(262, 0)
    EventBegin(0x00)
    OP_4A(0x000B, 0)
    OP_4A(0x0014, 0)
    OP_4A(0x000E, 0)
    FadeIn(2000, 0)
    OP_0D()
    OP_62(0x0014, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1500)

    ChrTalk(
        0x0014,
        (
            '#1790440869V我～都～说～了，\n',
            '不是我干的啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#1790440870V快点让我回去吧！\n',
            '我也有事情要办啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2870440871V#1P好了，冷静一点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2870440872V#1P你就忍耐到游击士来吧。\n',
            '调查结束了马上就能回去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    OP_70(0x0006, 29)
    OP_73(0x0006)
    OP_62(0x000B, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    ChrSetDirection(0x000B, 180, 400)

    ChrTalk(
        0x000B,
        (
            '#2870440873V#1P看，刚说\n',
            '他们就来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CameraMove(-1280, 0, 79170, 1500)
    CreateThread(0x000E, 0x01, 0x01, 0x0024)
    ChrSetDirection(0x0014, 180, 400)
    Sleep(600)

    @scena.Lambda('lambda_1D0F')
    def lambda_1D0F():
        CameraMove(-2420, 0, 79460, 2000)

        ExitThread()

    DispatchAsync(0x0014, 0x0002, lambda_1D0F)

    CreateThread(0x0101, 0x01, 0x01, 0x0025)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_1D3E',
    )

    CreateThread(0x0106, 0x01, 0x01, 0x0026)

    Jump('loc_1D4C')

    def _loc_1D3E(): pass

    label('loc_1D3E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_1D4C',
    )

    CreateThread(0x0103, 0x01, 0x01, 0x0026)

    def _loc_1D4C(): pass

    label('loc_1D4C')

    Sleep(500)

    CreateThread(0x0104, 0x01, 0x01, 0x0027)
    Sleep(500)

    CreateThread(0x0105, 0x01, 0x01, 0x0028)
    Sleep(300)

    WaitForThreadExit(0x000E, 0x0001)
    WaitForThreadExit(0x0105, 0x0001)
    WaitForThreadExit(0x0014, 0x0002)
    ChrTurnDirection(0x000B, 0x000E, 400)

    ChrTalk(
        0x000B,
        (
            '#2870440874V海利欧，\n',
            '你挺快的嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#2840440875V嗯，运气不错，\n',
            '正好碰到了各位游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    ChrSetDirection(0x000E, 215, 400)
    Sleep(400)

    ChrTalk(
        0x000E,
        (
            '#2840440876V这是诺曼先生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#2840440877V你们一定在街头巷尾的\n',
            '海报上见过他吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010440878V#1011F哦，是那位市长候选人啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440879V#1000F我是游击士\n',
            '艾丝蒂尔·布莱特。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_1F0E',
    )

    ChrTalk(
        0x0106,
        (
            '#0050440880V#050F我是她的同伴，\n',
            '阿加特·科洛斯纳。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050440881V请快告诉我们发生了什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F71')

    def _loc_1F0E(): pass

    label('loc_1F0E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_1F71',
    )

    ChrTalk(
        0x0103,
        (
            '#0030440882V#020F我是她的同伴，\n',
            '雪拉扎德·哈维。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030440883V请快告诉我们发生了什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1F71(): pass

    label('loc_1F71')

    ChrSetDirection(0x000B, 180, 400)

    ChrTalk(
        0x000B,
        (
            '#2870440884V我们的工作人员德尔斯\n',
            '受到了他人的暴力对待。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2870440885V也就是伤害案件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010440886V#1002F伤害案件……\n',
            '这可不是闹着玩的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440887V……受害者要不要紧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000B, 0x001A, 400)
    Sleep(400)

    ChrTalk(
        0x000B,
        (
            '#2870440888V嗯，他就在这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000B, 180, 400)

    ChrTalk(
        0x000B,
        (
            '#2870440889V刚才还处于昏迷状态，\n',
            '幸好没什么大事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010440890V#1007F啊……\n',
            '那真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x001A, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x001A,
        (
            '#2850440891V一点都不好哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001A,
        (
            '#2850440892V头后面肿得那么厉害，\n',
            '还阵阵地疼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010440893V#1004F啊，头后面……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440894V难道是被人从背后袭击了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001A,
        (
            '#2850440895V嗯，而且还是突然地。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001A,
        (
            '#2850440896V我当时正在阳台上休息，\n',
            '突然有人从背后打了我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_221E',
    )

    ChrTalk(
        0x0106,
        (
            '#0050440897V#057F这可是恶性事件……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2254')

    def _loc_221E(): pass

    label('loc_221E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_2254',
    )

    ChrTalk(
        0x0103,
        (
            '#0030440898V#022F这可是相当恶性的事件……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2254(): pass

    label('loc_2254')

    ChrTalk(
        0x0101,
        (
            '#0010440899V#1020F真、真狠啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_22D7',
    )

    ChrTalk(
        0x0106,
        (
            '#0050440900V#050F事情是什么时候发生的？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050440901V请仔细说说\n',
            '前后过程。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2334')

    def _loc_22D7(): pass

    label('loc_22D7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_2334',
    )

    ChrTalk(
        0x0103,
        (
            '#0030440902V#022F事情是什么时候发生的？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030440903V请把前后过程\n',
            '也仔细说说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2334(): pass

    label('loc_2334')

    ChrTalk(
        0x000E,
        (
            '#2840440904V嗯，那是今天午饭后的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#2840440905V我正和诺曼先生在大桥那边的\n',
            '演说场地进行预练……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#2840440906V这边的这位昆茨先生\n',
            '正好来到了那里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#2840440907V他对诺曼先生说有\n',
            '很重要的事要找他。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0014, 400)

    ChrTalk(
        0x0101,
        (
            '#0010440908V#1002F……什么样的事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0014, 0x0101, 400)

    ChrTalk(
        0x0014,
        (
            '#1790440909V我在波尔多斯先生的劝说下\n',
            '前来为桥上的骚乱道歉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#1790440910V虽然不全都是我的错，\n',
            '不过我确实煽动了人们的对立情绪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010440911V#1015F原来如此，你是来为\n',
            '那次骚乱道歉的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#2840440912V嗯，可是那个时候诺曼先生\n',
            '还有事要处理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#2840440913V所以我就让昆茨先生去\n',
            '事务所等着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#2840440914V然后我就把他\n',
            '带到了这个房间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000B, 180, 400)

    ChrTalk(
        0x000B,
        (
            '#2870440915V不久之后\n',
            '我返回了酒店。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2870440916V和在房间前等着的海利欧\n',
            '一起进入了事务所……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2870440917V然后就发现你们旁边的德尔斯\n',
            '在阳台上昏过去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x000E,
        (
            '#2840440918V并且在那旁边……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000E, 0x0014, 400)

    @scena.Lambda('lambda_267F')
    def lambda_267F():
        ChrTurnDirection(0x000B, 0x0014, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_267F)

    @scena.Lambda('lambda_268D')
    def lambda_268D():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_268D)

    CameraMove(-3080, 0, 79610, 1000)

    ChrTalk(
        0x000E,
        (
            '#2840440919V站着这位昆茨先生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0014, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x0014,
        (
            '#1790440920V我说啊～为什么你们后来\n',
            '就把我当成是犯人了啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#1790440921V我来到上阳台的时候\n',
            '这家伙已经倒在那里了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2870440922V我明白昆茨先生的心情，\n',
            '不过这么怀疑也是很正常的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2870440923V因为在这个房间里\n',
            '除了你和德尔斯以外\n',
            '没有别人了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010440924V#1002F确实是这样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000E, 0x0101, 400)

    ChrTalk(
        0x000E,
        (
            '#2840440925V把昆茨先生带来之后，\n',
            '我就在门外守着了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#2840440926V当然在诺曼先生来之前\n',
            '谁都不可能进来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#2840440927V不管怎么看都只有他们两个人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_28E6',
    )

    ChrTurnDirection(0x0106, 0x0014, 400)

    ChrTalk(
        0x0106,
        (
            '#0050440928V#050F……确实是这样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_291B')

    def _loc_28E6(): pass

    label('loc_28E6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_291B',
    )

    ChrTurnDirection(0x0106, 0x0014, 400)

    ChrTalk(
        0x0103,
        (
            '#0030440929V#022F……确实是这样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_291B(): pass

    label('loc_291B')

    OP_62(0x0014, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrTurnDirection(0x0014, 0x00F7, 400)

    ChrTalk(
        0x0014,
        (
            '#1790440930V这倒是事实……\n',
            '不过就像我刚才说的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#1790440931V我来到阳台上的时候\n',
            '德尔斯已经倒在那里了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_29F6',
    )

    ChrTalk(
        0x0106,
        (
            '#0050440932V#052F就是说…',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050440933V在你来之前\n',
            '案件已经发生了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A43')

    def _loc_29F6(): pass

    label('loc_29F6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_2A43',
    )

    ChrTalk(
        0x0103,
        (
            '#0030440934V#022F就是说',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030440935V在你来之前\n',
            '案件已经发生了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2A43(): pass

    label('loc_2A43')

    OP_62(0x0014, 0x00000000, 2000, 0x22, 0x24, 0x000000FA, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0014,
        (
            '#1790440936V嗯，就是这么回事！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#1790440937V呀～真是好沟通。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x000B, 400)

    ChrTalk(
        0x0101,
        (
            '#0010440938V#1015F那就等于是说在你之前\n',
            '已经有人来过这间房间了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440939V#1002F……德尔斯先生，你还记得些什么吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001A,
        (
            '#2850440940V印象中是有人来过……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001A,
        (
            '#2850440941V可是进出事务所的人很多。\n',
            '完全不会去注意是谁的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010440942V#1007F嗯，这倒也是。\n',
            '因为是选举事务所嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_2C87',
    )

    ChrTalk(
        0x0106,
        (
            '#0050440943V#053F……看来案件的焦点\n',
            '已经显露出来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050440944V这起案件的犯人\n',
            '是下面两个人中的一个。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050440945V#057F要么是这个大叔，要么是\n',
            '之前来到房间的某个人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2D3B')

    def _loc_2C87(): pass

    label('loc_2C87')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_2D3B',
    )

    ChrTalk(
        0x0103,
        (
            '#0030440946V#026F……看来案件的焦点\n',
            '已经显露出来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030440947V这起案件的犯人\n',
            '是下面两个人中的一个。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030440948V#027F要么是昆茨先生，要么是\n',
            '之前来到房间的某个人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2D3B(): pass

    label('loc_2D3B')

    ChrTurnDirection(0x0101, 0x00F7, 400)

    ChrTalk(
        0x0101,
        (
            '#0010440949V#1002F接下来就看证据了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440950V怎样？\n',
            '现在就去打听情况？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00F7, 0x0101, 400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_2E41',
    )

    ChrTalk(
        0x0106,
        (
            '#0050440951V#050F如果没什么其它情报的话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x00F7, 0, 400)
    Sleep(400)

    ChrTalk(
        0x0106,
        (
            '#0050440952V#050F……如果有什么在意的事情\n',
            '就趁现在说出来吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050440953V小事情也可以说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2EE7')

    def _loc_2E41(): pass

    label('loc_2E41')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_2EE7',
    )

    ChrTalk(
        0x0103,
        (
            '#0030440954V#020F嗯，如果没什么其它情报的话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x00F7, 0, 400)
    Sleep(400)

    ChrTalk(
        0x0103,
        (
            '#0030440955V#020F……如果有什么在意的事情\n',
            '就趁现在说出来吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030440956V小事情也没关系。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2EE7(): pass

    label('loc_2EE7')

    Sleep(400)

    ChrTurnDirection(0x000B, 0x00F7, 400)

    ChrTalk(
        0x000B,
        (
            '#2870440957V那么，我有一些话要说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2870440958V……我在观察案发后的房间时\n',
            '发现了一件不可思议的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x000B, 400)

    ChrTalk(
        0x0101,
        (
            '#0010440959V#1002F有被翻动过的痕迹？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2870440960V不，正相反。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2870440961V不如说是感觉收拾得\n',
            '比以前更干净了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010440962V#1004F啊？怎么回事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x0104,
        (
            '#0040440963V#032F嗯，如果一定要解释的话\n',
            '那就是为了消除翻动痕迹的伪装吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040440964V当然，这种过度的行为\n',
            '反而会招来怀疑。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x000B,
        (
            '#2870440965V哟，这可是有价值的意见……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2870440966V……对了，你是谁？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0104, 0x01, 0x01, 0x002B)
    Sleep(200)

    ChrTalk(
        0x0104,
        (
            '#0040440967V#035F呵呵，我等待这个问题很久了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040440968V我是漂泊的诗人兼天才演员……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x000B, 400)

    ChrTalk(
        0x0101,
        (
            '#0010440969V#1002F不过，如果没有东西失窃的话,\n',
            '伪装的说法很难成立哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440970V现在分析一堆理由\n',
            '也不是办法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_321A',
    )

    ChrTalk(
        0x0106,
        (
            '#0050440971V#053F#2P嗯，我有同感。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3249')

    def _loc_321A(): pass

    label('loc_321A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_3249',
    )

    ChrTalk(
        0x0103,
        (
            '#0030440972V#026F#2P嗯，我有同感。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3249(): pass

    label('loc_3249')

    OP_62(0x0104, 0x00000000, 2000, 0x14, 0x17, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0104,
        (
            '#0040440973V#035F呵、呵呵……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040440974V艾丝蒂尔……\n',
            '比以前更厉害了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040440975V应该说不愧是从\n',
            '卢·洛克尔受训回来的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0104, 400)

    ChrTalk(
        0x0105,
        (
            '#0060440976V#045F奥、奥利维尔先生……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x00F7, 400)

    ChrTalk(
        0x0101,
        (
            '#0010440977V#1007F这种时候\n',
            '最好不要理他。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440978V#1006F好了，如果没什么可以再问的\n',
            '我们就快点去打听情况吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_340A',
    )

    ChrTurnDirection(0x0106, 0x0101, 400)

    ChrTalk(
        0x0106,
        (
            '#0050440979V#052F#2P嗯、嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050440980V#053F（看来她已经很\n',
            '  了解对付他的方法了……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_347B')

    def _loc_340A(): pass

    label('loc_340A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_347B',
    )

    ChrTurnDirection(0x0103, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030440981V#023F是、是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030440982V#026F（她也开始明白应该\n',
            '  怎么对付奥利维尔了……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_347B(): pass

    label('loc_347B')

    ChrTalk(
        0x000B,
        (
            '#2870440983V那么，调查的事\n',
            '也请多关照了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_34E6',
    )

    ChrTurnDirection(0x0106, 0x000B, 400)

    ChrTalk(
        0x0106,
        (
            '#0050440984V#050F结果出来后再来汇报。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_351F')

    def _loc_34E6(): pass

    label('loc_34E6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_351F',
    )

    ChrTurnDirection(0x0103, 0x000B, 400)

    ChrTalk(
        0x0103,
        (
            '#0030440985V#020F结果出来后再来汇报。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_351F(): pass

    label('loc_351F')

    ChrTalk(
        0x000B,
        (
            '#2870440986V嗯，我等着你们的好消息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithValue(
        0x0018,
        0x01,
        (
            (Expr.GetChrWork, 0xF7, 0x1),
            (Expr.GetChrWork, 0x104, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0018,
        0x02,
        (
            (Expr.GetChrWork, 0xF7, 0x2),
            (Expr.GetChrWork, 0x104, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0018,
        0x03,
        (
            (Expr.GetChrWork, 0xF7, 0x3),
            (Expr.GetChrWork, 0x104, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(400)

    ChrSetSubChip(0x0104, 0)
    ChrSetChipByIndex(0x0104, 65535)
    ChrClearFlags(0x0104, 0x0002)
    CreateThread(0x0104, 0x01, 0x01, 0x002A)
    Sleep(100)

    CreateThread(0x0101, 0x01, 0x01, 0x002A)
    CreateThread(0x0105, 0x01, 0x01, 0x002A)
    CreateThread(0x00F7, 0x01, 0x01, 0x002A)
    OP_69(0x0018, 1000)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010440987V#1002F那么，我们应该从哪入手呢？\n',
            '这座酒店相当大呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_36AF',
    )

    ChrTalk(
        0x0106,
        (
            '#0050440988V#050F兵分两路行动比较好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050440989V你和公主一组。\n',
            '我和这个家伙一组。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050440990V他们两人现在也是协力人员。\n',
            '要请他们帮忙工作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3753')

    def _loc_36AF(): pass

    label('loc_36AF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_3753',
    )

    ChrTalk(
        0x0103,
        (
            '#0030440991V#020F兵分两路行动比较好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030440992V艾丝蒂尔和殿下一起。\n',
            '我和奥利维尔搭档。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030440993V他们两人现在也是协力人员，\n',
            '要请他们帮忙工作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3753(): pass

    label('loc_3753')

    ChrTalk(
        0x0101,
        (
            '#0010440994V#1017F哦，这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440995V嗯，让我再次说一声拜托。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060440996V#041F呵呵，彼此彼此。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040440997V#031F呵呵，作为协力人员这是理所应当的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010440998V#1019F啊，你还是恢复得\n',
            '和以前一样快呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_38F8',
    )

    ChrTalk(
        0x0106,
        (
            '#0050440999V#050F听着，我们首先要\n',
            '从收集嫌疑人的信息开始。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050441000V对所有有关人员都问一次',
            (TxtCtl.SetColor, 0x4),
            '『关于昆茨』\n',
            (TxtCtl.SetColor, 0x0),
            '应该能得到些什么。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050441001V如果有眉目了\n',
            '就到我这里来通知我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_39BB')

    def _loc_38F8(): pass

    label('loc_38F8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_39BB',
    )

    ChrTalk(
        0x0103,
        (
            '#0030441002V#020F听着，我们首先要\n',
            '从收集嫌疑人的信息开始。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030441003V对所有有关人员都问一次',
            (TxtCtl.SetColor, 0x4),
            '『关于昆茨』\n',
            (TxtCtl.SetColor, 0x0),
            '应该能得到些什么。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030441004V如果有了犯人的眉目\n',
            '就到我这里来通知我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_39BB(): pass

    label('loc_39BB')

    ChrTalk(
        0x0101,
        (
            '#0010441005V#1015F知道了犯人是谁\n',
            '来报告就行了吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441006V#1006F……好。\n',
            '那我们行动吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    ChrSetPos(0x000E, -3880, 0, 83810, 180)
    ChrSetPos(0x000B, -430, 0, 80990, 225)
    ChrSetPos(0x0014, -2450, 0, 80960, 180)
    OP_4B(0x000B, 0)
    OP_4B(0x0014, 0)
    OP_4B(0x000E, 0)
    OP_28(0x0069, 0x04, 0x02)
    OP_28(0x0069, 0x04, 0x04)
    OP_28(0x0069, 0x04, 0x08)
    FormationDelMember(0x03, 0xFF)
    ChrClearFlags(0x0017, 0x0080)
    ChrSetPos(0x0017, -1300, 0, 78180, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_3AB2',
    )

    FormationDelMember(0x05, 0xFF)
    ChrClearFlags(0x0015, 0x0080)
    ChrSetPos(0x0015, -2430, 0, 79710, 0)

    Jump('loc_3AD2')

    def _loc_3AB2(): pass

    label('loc_3AB2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_3AD2',
    )

    FormationDelMember(0x02, 0xFF)
    ChrClearFlags(0x0016, 0x0080)
    ChrSetPos(0x0016, -2430, 0, 79710, 0)

    def _loc_3AD2(): pass

    label('loc_3AD2')

    ChrSetPos(0x0101, -2160, 0, 77200, 205)
    ChrSetPos(0x0105, -2160, 0, 77200, 205)
    OP_30(0x00)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(35000, 0)
    OP_6E(262, 0)
    OP_69(0x0101, 0)
    MapSetFlags(0x00000001)
    FadeIn(1000, 0)
    OP_0D()
    EventEnd(0x02)

    Return()

# id: 0x0005 offset: 0x3B3B
@scena.Code('func_05_3B3B')
def func_05_3B3B():
    FadeOut(300, 0, 100)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0xFFFFFFF),
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

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetMessageWindowPos(-1, 16, -1, -1)

    Talk(
        (
            0x18,
            '要询问什么？',
            TxtCtl.Enter,
        ),
    )

    OP_CC(0x00, 0x00, 0x000A, 0x000A, 0x01)
    OP_CC(0x01, 0x00, '关于昆茨')

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x01, 0x0001)"),
            Expr.Return,
        ),
        'loc_3BD8',
    )

    OP_CC(0x01, 0x00, '声响')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0xFFFFFF0),
            Expr.And,
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x1),
            Expr.Mul,
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_3BD8(): pass

    label('loc_3BD8')

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x01, 0x0002)"),
            Expr.Return,
        ),
        'loc_3C0D',
    )

    OP_CC(0x01, 0x00, '发怒')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0xFFFFF0F),
            Expr.And,
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x10),
            Expr.Mul,
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_3C0D(): pass

    label('loc_3C0D')

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x01, 0x0008)"),
            Expr.Return,
        ),
        'loc_3C48',
    )

    OP_CC(0x01, 0x00, '关于海利欧')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0xFFFF0FF),
            Expr.And,
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x100),
            Expr.Mul,
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_3C48(): pass

    label('loc_3C48')

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x01, 0x0010)"),
            Expr.Return,
        ),
        'loc_3C7D',
    )

    OP_CC(0x01, 0x00, '午饭')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0xFFF0FFF),
            Expr.And,
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x1000),
            Expr.Mul,
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_3C7D(): pass

    label('loc_3C7D')

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x01, 0x0040)"),
            Expr.Return,
        ),
        'loc_3CB2',
    )

    OP_CC(0x01, 0x00, '钟声')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0xFF0FFFF),
            Expr.And,
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x10000),
            Expr.Mul,
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_3CB2(): pass

    label('loc_3CB2')

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x01, 0x0800)"),
            Expr.Return,
        ),
        'loc_3CEB',
    )

    OP_CC(0x01, 0x00, '收拾善后')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0xF0FFFFF),
            Expr.And,
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x100000),
            Expr.Mul,
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_3CEB(): pass

    label('loc_3CEB')

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x01, 0x2000)"),
            Expr.Return,
        ),
        'loc_3D26',
    )

    OP_CC(0x01, 0x00, '关于贝尔夫')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0xFFFFFF),
            Expr.And,
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x1000000),
            Expr.Mul,
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_3D26(): pass

    label('loc_3D26')

    OP_CC(0x01, 0x00, '离开')
    OP_CC(0x02, 0x00)
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
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3D6E',
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_3E74')

    def _loc_3D6E(): pass

    label('loc_3D6E')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x1),
            Expr.Div,
            (Expr.PushLong, 0xF),
            Expr.And,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3D92',
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_3E74')

    def _loc_3D92(): pass

    label('loc_3D92')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x10),
            Expr.Div,
            (Expr.PushLong, 0xF),
            Expr.And,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3DB6',
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_3E74')

    def _loc_3DB6(): pass

    label('loc_3DB6')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x100),
            Expr.Div,
            (Expr.PushLong, 0xF),
            Expr.And,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3DDA',
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_3E74')

    def _loc_3DDA(): pass

    label('loc_3DDA')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x1000),
            Expr.Div,
            (Expr.PushLong, 0xF),
            Expr.And,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3DFE',
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_3E74')

    def _loc_3DFE(): pass

    label('loc_3DFE')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x10000),
            Expr.Div,
            (Expr.PushLong, 0xF),
            Expr.And,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3E22',
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_3E74')

    def _loc_3E22(): pass

    label('loc_3E22')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x100000),
            Expr.Div,
            (Expr.PushLong, 0xF),
            Expr.And,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3E46',
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x6),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_3E74')

    def _loc_3E46(): pass

    label('loc_3E46')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x1000000),
            Expr.Div,
            (Expr.PushLong, 0xF),
            Expr.And,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3E6A',
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x7),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_3E74')

    def _loc_3E6A(): pass

    label('loc_3E6A')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_3E74(): pass

    label('loc_3E74')

    Return()

# id: 0x0006 offset: 0x3E75
@scena.Code('func_06_3E75')
def func_06_3E75():
    Call(1, 0x0005)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_3EA2'),
        (0x00000001, 'loc_4047'),
        (0x00000002, 'loc_408A'),
        (0x00000003, 'loc_41AB'),
        (0x00000004, 'loc_430E'),
        (0x00000005, 'loc_4984'),
        (0x00000006, 'loc_4B7D'),
        (0x00000007, 'loc_4C12'),
        (-1, 'loc_4C76'),
    )

    def _loc_3EA2(): pass

    label('loc_3EA2')

    OP_28(0x006A, 0x01, 0x0080)

    If(
        (
            (Expr.PushReg, 0x9),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_3F26',
    )

    ChrTalk(
        0x00FE,
        (
            '#2810441088V昆茨先生来到酒店的时候\n',
            '我正在前厅里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2810441089V不过总觉得那个人\n',
            '看起来好像在生气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4044')

    def _loc_3F26(): pass

    label('loc_3F26')

    ExecExpressionWithReg(
        0x0009,
        (
            (Expr.PushLong, 0x1),
            Expr.Or2,
            Expr.Return,
        ),
    )

    ChrTalk(
        0x00FE,
        (
            '#2810441088V昆茨先生来到酒店的时候\n',
            '我正在前厅里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x01, 0x0002)"),
            Expr.Return,
        ),
        'loc_3FAA',
    )

    ChrTalk(
        0x00FE,
        (
            '#2810441091V不过总觉得那个人好像\n',
            '生气了似的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3FEA')

    def _loc_3FAA(): pass

    label('loc_3FAA')

    ChrTalk(
        0x00FE,
        (
            '#2810441092V不过总觉得那个人好象\n',
            (TxtCtl.SetColor, 0x4),
            '『生气』',
            (TxtCtl.SetColor, 0x0),
            '了似的。',
            TxtCtl.Enter,
        ),
    )

    PlaySE(17, 0x00, 0x64)
    CloseMessageWindow()

    def _loc_3FEA(): pass

    label('loc_3FEA')

    ChrTalk(
        0x00FE,
        (
            '#2810441093V我就觉得会出什么事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2810441094V果然不出我所料，发生了案件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0069, 0x01, 0x0002)

    def _loc_4044(): pass

    label('loc_4044')

    Jump('loc_4C79')

    def _loc_4047(): pass

    label('loc_4047')

    OP_28(0x006A, 0x01, 0x0080)

    ChrTalk(
        0x00FE,
        (
            '#2810441095V声响啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2810441096V没什么印象。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4C79')

    def _loc_408A(): pass

    label('loc_408A')

    OP_28(0x006A, 0x01, 0x0080)

    If(
        (
            (Expr.PushReg, 0x9),
            (Expr.PushLong, 0x4),
            Expr.And,
            Expr.Return,
        ),
        'loc_411A',
    )

    ChrTalk(
        0x00FE,
        (
            '#2810441097V我觉得昆茨先生\n',
            '那时在生气哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2810441098V因为刚发生过\n',
            '那起骚乱呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2810441099V生气也很正常。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_41A8')

    def _loc_411A(): pass

    label('loc_411A')

    ExecExpressionWithReg(
        0x0009,
        (
            (Expr.PushLong, 0x4),
            Expr.Or2,
            Expr.Return,
        ),
    )

    ChrTalk(
        0x00FE,
        (
            '#2810441100V嗯，我觉得昆茨先生\n',
            '那时在生气哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2810441101V不过，因为刚发生过\n',
            '那起骚乱呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2810441099V生气也很正常。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_41A8(): pass

    label('loc_41A8')

    Jump('loc_4C79')

    def _loc_41AB(): pass

    label('loc_41AB')

    OP_28(0x006A, 0x01, 0x0080)

    If(
        (
            (Expr.PushReg, 0x9),
            (Expr.PushLong, 0x8),
            Expr.And,
            Expr.Return,
        ),
        'loc_4258',
    )

    ChrTalk(
        0x00FE,
        (
            '#2810441103V海利欧先生也受到了怀疑吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2810441104V嗯～我以前觉得他和\n',
            '德尔斯先生关系很好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2810441105V不过出人意料的是事实并非如此。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_430B')

    def _loc_4258(): pass

    label('loc_4258')

    ExecExpressionWithReg(
        0x0009,
        (
            (Expr.PushLong, 0x8),
            Expr.Or2,
            Expr.Return,
        ),
    )

    ChrTalk(
        0x00FE,
        (
            '#2810441106V这次是海利欧先生\n',
            '受到怀疑吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2810441107V确实在返回酒店的时候\n',
            '海利欧先生看起来也不大高兴哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2810441108V嗯，一定是和昆茨\n',
            '先生在一起的关系。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_430B(): pass

    label('loc_430B')

    Jump('loc_4C79')

    def _loc_430E(): pass

    label('loc_430E')

    OP_28(0x006A, 0x01, 0x0080)

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x01, 0x2000)"),
            Expr.Return,
        ),
        'loc_44D3',
    )

    OP_28(0x006A, 0x01, 0x0001)

    ChrTalk(
        0x00FE,
        (
            '#2810441109V在１楼吃完午饭后，\n',
            '就一直磨磨蹭蹭地待在地下室。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2810441110V真、真的哦。\n',
            '我没必要撒谎吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2810441111V不、不过。\n',
            '老爸那家伙也很狡猾啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2810441112V让我们吃普通的东西，\n',
            '自己一个人吃特制的什锦饭。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x006A, 0x01, 0x0001)"),
            (Expr.Eval, "OP_29(0x006A, 0x01, 0x0004)"),
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0069, 0x01, 0x0800)"),
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0069, 0x01, 0x1000)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_44D0',
    )

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    ChrTalk(
        0x0101,
        (
            '#0010441113V#1015F咦？可是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrTurnDirection(0x00FE, 0x0101, 400)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '#2810441114V啊啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '#2810441115V这、这次又怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(1, 0x0008)

    def _loc_44D0(): pass

    label('loc_44D0')

    Jump('loc_4981')

    def _loc_44D3(): pass

    label('loc_44D3')

    If(
        (
            (Expr.Eval, "OP_29(0x006A, 0x01, 0x0020)"),
            Expr.Return,
        ),
        'loc_4600',
    )

    OP_28(0x006A, 0x01, 0x0001)

    ChrTalk(
        0x00FE,
        (
            '#2810441116V午饭是在１楼的前厅吃的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2810441117V不过，老爸那家伙也很狡猾啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2810441112V让我们吃普通的东西，\n',
            '自己一个人吃特制的什锦饭。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x006A, 0x01, 0x0001)"),
            (Expr.Eval, "OP_29(0x006A, 0x01, 0x0004)"),
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0069, 0x01, 0x0800)"),
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0069, 0x01, 0x1000)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_45FD',
    )

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    ChrTalk(
        0x0101,
        (
            '#0010441113V#1015F咦？可是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#2810441120V你、你怎么那副怪表情……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(1, 0x0008)

    def _loc_45FD(): pass

    label('loc_45FD')

    Jump('loc_4981')

    def _loc_4600(): pass

    label('loc_4600')

    If(
        (
            (Expr.Eval, "OP_29(0x006A, 0x01, 0x0001)"),
            Expr.Return,
        ),
        'loc_4727',
    )

    ChrTalk(
        0x00FE,
        (
            '#2810441116V午饭是在１楼的前厅吃的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2810441117V不过，老爸那家伙也很狡猾啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2810441112V让我们吃普通的东西，\n',
            '自己一个人吃特制的什锦饭。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x006A, 0x01, 0x0001)"),
            (Expr.Eval, "OP_29(0x006A, 0x01, 0x0004)"),
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0069, 0x01, 0x0800)"),
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0069, 0x01, 0x1000)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4724',
    )

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    ChrTalk(
        0x0101,
        (
            '#0010441113V#1015F咦？可是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#2810441120V你、你怎么那副怪表情……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(1, 0x0008)

    def _loc_4724(): pass

    label('loc_4724')

    Jump('loc_4981')

    def _loc_4727(): pass

    label('loc_4727')

    OP_28(0x006A, 0x01, 0x0001)

    ChrTalk(
        0x00FE,
        (
            '#2810441126V嗯，午餐是什锦饭。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2810441127V我一个人在前厅吃的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2810441128V和老爸在一个房间吃饭\n',
            '总感觉很尴尬……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2810441117V不过，老爸那家伙也很狡猾啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2810441130V让我们吃普通的东西，\n',
            '他自己一个人吃特制的什锦饭哦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010441131V#1016F啊哈哈，是这样呀。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441132V有那么不一样吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#2810441133V嗯，天差地别呢。\n',
            '特制的里面放了很多很多的虾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2810441134V老爸好像没食欲，\n',
            '就留下了不少……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2810441135V多可惜啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x006A, 0x01, 0x0001)"),
            (Expr.Eval, "OP_29(0x006A, 0x01, 0x0004)"),
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0069, 0x01, 0x0800)"),
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0069, 0x01, 0x1000)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4981',
    )

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    ChrTalk(
        0x0101,
        (
            '#0010441113V#1015F咦？可是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#2810441120V你、你怎么那副怪表情……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(1, 0x0008)

    Jump('loc_4981')

    def _loc_4981(): pass

    label('loc_4981')

    Jump('loc_4C79')

    def _loc_4984(): pass

    label('loc_4984')

    OP_28(0x006A, 0x01, 0x0080)

    If(
        (
            (Expr.PushReg, 0x9),
            (Expr.PushLong, 0x20),
            Expr.And,
            Expr.Return,
        ),
        'loc_4A83',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x006A, 0x01, 0x0020)"),
            Expr.Return,
        ),
        'loc_4A0F',
    )

    OP_28(0x006A, 0x01, 0x0002)

    ChrTalk(
        0x00FE,
        (
            '#2810441138V我、我待在地下室，\n',
            '没听到什么钟声。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2810441110V真、真的哦。\n',
            '我没必要撒谎吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4A80')

    def _loc_4A0F(): pass

    label('loc_4A0F')

    OP_28(0x006A, 0x01, 0x0002)

    ChrTalk(
        0x00FE,
        (
            '#2810441140V是吗，桥上的钟已经响过了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2810441141V因为我在酒店的地下室，\n',
            '所以一点也没注意到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4A80(): pass

    label('loc_4A80')

    Jump('loc_4B7A')

    def _loc_4A83(): pass

    label('loc_4A83')

    ExecExpressionWithReg(
        0x0009,
        (
            (Expr.PushLong, 0x20),
            Expr.Or2,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x01, 0x2000)"),
            Expr.Return,
        ),
        'loc_4B05',
    )

    OP_28(0x006A, 0x01, 0x0002)

    ChrTalk(
        0x00FE,
        (
            '#2810441138V我、我待在地下室，\n',
            '没听到什么钟声。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2810441110V真、真的哦。\n',
            '我没必要撒谎吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4B7A')

    def _loc_4B05(): pass

    label('loc_4B05')

    OP_28(0x006A, 0x01, 0x0002)

    ChrTalk(
        0x00FE,
        (
            '#2810441144V咦，有钟声响过？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2810441145V因为我在酒店的地下室，\n',
            '没怎么注意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x006A, 0x01, 0x0020)"),
            (Expr.Eval, "OP_29(0x0069, 0x01, 0x2000)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4B7A',
    )

    Call(1, 0x0007)

    def _loc_4B7A(): pass

    label('loc_4B7A')

    Jump('loc_4C79')

    def _loc_4B7D(): pass

    label('loc_4B7D')

    OP_28(0x006A, 0x01, 0x0080)
    OP_28(0x006A, 0x01, 0x0002)

    ChrTalk(
        0x00FE,
        (
            '#2810441146V收拾事务所的餐具？\n',
            '我可没做那么麻烦的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2810441147V吃了饭以后\n',
            '我在酒店的地下室发呆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x006A, 0x01, 0x0020)"),
            (Expr.Eval, "OP_29(0x0069, 0x01, 0x2000)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4C0F',
    )

    Call(1, 0x0007)

    def _loc_4C0F(): pass

    label('loc_4C0F')

    Jump('loc_4C79')

    def _loc_4C12(): pass

    label('loc_4C12')

    OP_28(0x006A, 0x01, 0x0080)

    ChrTalk(
        0x00FE,
        (
            '#2810441148V我、我都说了\n',
            '钟响的时候我在地下室。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2810441149V午饭后一直在地下哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4C79')

    def _loc_4C76(): pass

    label('loc_4C76')

    Jump('loc_4C79')

    def _loc_4C79(): pass

    label('loc_4C79')

    Return()

# id: 0x0007 offset: 0x4C7A
@scena.Code('func_07_4C7A')
def func_07_4C7A():
    OP_28(0x0069, 0x01, 0x2000)

    ChrTalk(
        0x0101,
        (
            '#0010441182V#1019F……………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441183V……你真的一直在地下室？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrTurnDirection(0x00FE, 0x0101, 400)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '#2810441184V咦！？为、为什么这么问？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010441185V#1002F有一个人在钟刚响的时候\n',
            '正好去了地下室哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441186V根据那个人的证词\n',
            '地下室没有人在。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '#2810441187V不、不可能的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2810441188V因、因为我一直\n',
            '待在那里的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060441189V#042F（没不在场证明呢……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0105, 400)

    ChrTalk(
        0x0101,
        (
            '#0010441190V#1002F（谨慎起见去问问',
            (TxtCtl.SetColor, 0x4),
            '『关于贝尔夫』\n',
            (TxtCtl.SetColor, 0x0),
            '会比较好吧。）',
            TxtCtl.Enter,
        ),
    )

    PlaySE(17, 0x00, 0x64)
    CloseMessageWindow()

    Return()

# id: 0x0008 offset: 0x4E7E
@scena.Code('func_08_4E7E')
def func_08_4E7E():
    OP_28(0x0069, 0x01, 0x1000)

    ChrTalk(
        0x00FE,
        (
            '#2810441150V我说错了什么吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_4FE1',
    )

    ChrTalk(
        0x0101,
        (
            '#0010441151V#1015F不，我只是有点在意……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441152V#1002F……我说，贝尔夫。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441153V听说你的午饭\n',
            '是在１楼吃的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#2810441154V嗯、嗯……是的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2810441155V有什么问题吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010441156V#1015F可诺曼先生\n',
            '是在２楼吃的吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441157V在１楼的你，\n',
            '为什么会知道诺曼\n',
            '吃的是什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5269')

    def _loc_4FE1(): pass

    label('loc_4FE1')

    ChrTalk(
        0x0101,
        (
            '#0010441151V#1015F不，我只是有点在意……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441152V#1002F……我说，贝尔夫先生。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441160V你上回说了是\n',
            '特制什锦饭吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441161V还有你也说过诺曼先生一个人\n',
            '吃那个很狡猾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#2810441162V啊，啊啊……\n',
            '我好像没记错吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2810441155V有什么问题吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010441164V#1015F嗯，那你怎么会\n',
            '知道那些的呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441165V……我们实在是想不通。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2810441166V嗯、嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2810441167V这，这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010441168V#1010F你说你在１楼的前厅\n',
            '吃的午饭是吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441169V而诺曼先生是在２楼的\n',
            '事务所吃的什锦饭。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441170V#1002F在这种情况下\n',
            '你那番话是不是有点奇怪？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441157V在１楼的你，\n',
            '为什么会知道诺曼先生\n',
            '吃的是什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5269(): pass

    label('loc_5269')

    ChrTalk(
        0x00FE,
        (
            '#2810441172V那、那又怎么样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2810441173V当然是后来看到的了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '#2810441174V………………………………\n',
            '…………啊………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010441175V#1019F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060441176V#044F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '#2810441177V唔、唔……\n',
            '抱歉我说错了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2810441178V嗯，其实那些我是\n',
            '听说的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2810441179V很、很遗憾,\n',
            '我忘了是谁告诉我的了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2810441180V接、接下来你们\n',
            '调查一下不就好了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010441181V#1007F（真、真的很可疑。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Return()

# id: 0x0009 offset: 0x546A
@scena.Code('func_09_546A')
def func_09_546A():
    Call(1, 0x0005)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_5497'),
        (0x00000001, 'loc_5510'),
        (0x00000002, 'loc_5566'),
        (0x00000003, 'loc_5649'),
        (0x00000004, 'loc_5D59'),
        (0x00000005, 'loc_5E50'),
        (0x00000006, 'loc_61DA'),
        (0x00000007, 'loc_6241'),
        (-1, 'loc_6360'),
    )

    def _loc_5497(): pass

    label('loc_5497')

    OP_28(0x006A, 0x01, 0x0200)

    ChrTalk(
        0x000A,
        (
            '#1490441191V昆茨先生很少\n',
            '来我们酒店。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1490441192V大多数情况下都是因为\n',
            '工作上的集会来租用我们的房间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6363')

    def _loc_5510(): pass

    label('loc_5510')

    OP_28(0x006A, 0x01, 0x0200)

    ChrTalk(
        0x000A,
        (
            '#1490441193V哦，声响啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1490441194V不好意思，\n',
            '我什么也没听见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6363')

    def _loc_5566(): pass

    label('loc_5566')

    OP_28(0x006A, 0x01, 0x0200)

    If(
        (
            (Expr.PushReg, 0x8),
            (Expr.PushLong, 0x4),
            Expr.And,
            Expr.Return,
        ),
        'loc_55D8',
    )

    ChrTalk(
        0x000A,
        (
            '#1490441195V昆茨先生的样子\n',
            '和平时并没有不同。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1490441196V怎么也看不出\n',
            '是在生气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5646')

    def _loc_55D8(): pass

    label('loc_55D8')

    ExecExpressionWithReg(
        0x0008,
        (
            (Expr.PushLong, 0x4),
            Expr.Or2,
            Expr.Return,
        ),
    )

    ChrTalk(
        0x000A,
        (
            '#1490441197V所以，我无法赞同\n',
            '那一位的观点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1490441195V昆茨先生的样子\n',
            '和平时并没有不同。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5646(): pass

    label('loc_5646')

    Jump('loc_6363')

    def _loc_5649(): pass

    label('loc_5649')

    OP_28(0x006A, 0x01, 0x0200)

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x01, 0x0010)"),
            Expr.Return,
        ),
        'loc_5700',
    )

    ChrTalk(
        0x000A,
        (
            '#1490441199V非常抱歉我没有\n',
            '把该说的事情说出来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1490441200V可是，海利欧先生\n',
            '不可能是犯人的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1490441201V那位先生怎么会犯罪呢……\n',
            '我实在无法想象。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5D56')

    def _loc_5700(): pass

    label('loc_5700')

    If(
        (
            (Expr.Eval, "OP_29(0x006A, 0x01, 0x0010)"),
            Expr.Return,
        ),
        'loc_5C3E',
    )

    OP_28(0x0069, 0x01, 0x0010)
    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))
    SetScenaFlags(ScenaFlag(0x0001, 7, 0xF))

    ChrTalk(
        0x000A,
        (
            '#1490441202V您、您还在怀疑\n',
            '海利欧先生吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1490441203V海利欧先生是诚实的人。\n',
            '不可能是犯人的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1490441204V所以，那位先生\n',
            '不可能是犯人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010441205V#1002F？？？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441206V怎、怎么了？\n',
            '我好像觉得你有点顾虑？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4A(0x0017, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_587A',
    )

    OP_4A(0x0015, 0)

    ChrTalk(
        0x0015,
        (
            '#0050441207V#057F有什么瞒着我们的事情，\n',
            '还是坦白比较好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050441208V包庇的心情\n',
            '经常是会害人的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_58EC')

    def _loc_587A(): pass

    label('loc_587A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_58EC',
    )

    OP_4A(0x0016, 0)

    ChrTalk(
        0x0016,
        (
            '#0030441209V#027F有什么瞒着我们的事情，\n',
            '还是老实说比较好哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030441210V包庇别人往往\n',
            '会害人的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_58EC(): pass

    label('loc_58EC')

    ChrTalk(
        0x000A,
        (
            '#1490441211V……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1490441212V对、对不起……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010441213V#1002F你想说了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1490441214V是，其实………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1490441215V我看见了。\n',
            '海利欧先生上了２楼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_59E3',
    )

    ChrTalk(
        0x0015,
        (
            '#0050441216V#057F……那是什么时候？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0015, 400)

    Jump('loc_5A1A')

    def _loc_59E3(): pass

    label('loc_59E3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_5A1A',
    )

    ChrTalk(
        0x0016,
        (
            '#0030441217V#022F……那是什么时候？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0016, 400)

    def _loc_5A1A(): pass

    label('loc_5A1A')

    Sleep(400)

    ChrTalk(
        0x000A,
        (
            (TxtCtl.SetColor, 0x4),
            '#1490441218V『午餐』',
            (TxtCtl.SetColor, 0x0),
            '刚吃完之后。',
            TxtCtl.Enter,
        ),
    )

    PlaySE(17, 0x00, 0x64)
    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1490441219V海利欧先生和诺曼先生\n',
            '一起出了门……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1490441220V可是没过多久，\n',
            '海利欧先生一个人回来\n',
            '上了２楼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010441221V#1002F这是重要的证词……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_5B6E',
    )

    ChrTurnDirection(0x0015, 0x0101, 400)

    ChrTalk(
        0x0015,
        (
            '#0050441222V#050F艾丝蒂尔你们去\n',
            '调查一下该证词所说的事情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050441223V我们在这里\n',
            '再拖延一些时间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0015, 400)

    Jump('loc_5BEC')

    def _loc_5B6E(): pass

    label('loc_5B6E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_5BEC',
    )

    ChrTurnDirection(0x0016, 0x0101, 400)

    ChrTalk(
        0x0016,
        (
            '#0030441224V#022F艾丝蒂尔你们去\n',
            '调查一下该证词所说的事情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030441225V我们在这里\n',
            '再拖延一些时间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0016, 400)

    def _loc_5BEC(): pass

    label('loc_5BEC')

    ChrTalk(
        0x0101,
        (
            '#0010340419V#1002F嗯，明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4B(0x0017, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_5C29',
    )

    OP_4B(0x0015, 0)
    ChrTurnDirection(0x0015, 0x000A, 0)

    Jump('loc_5C3B')

    def _loc_5C29(): pass

    label('loc_5C29')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_5C3B',
    )

    OP_4B(0x0016, 0)
    ChrTurnDirection(0x0016, 0x000A, 0)

    def _loc_5C3B(): pass

    label('loc_5C3B')

    Jump('loc_5D56')

    def _loc_5C3E(): pass

    label('loc_5C3E')

    If(
        (
            (Expr.Eval, "OP_29(0x006A, 0x01, 0x0008)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5CE8',
    )

    OP_28(0x006A, 0x01, 0x0008)

    ChrTalk(
        0x000A,
        (
            '#1490441227V连海利欧先生\n',
            '你们也怀疑吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1490441228V他可不是一个\n',
            '会动用暴力的人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1490441229V所以，海利欧先生也\n',
            '不可能是犯人的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5D56')

    def _loc_5CE8(): pass

    label('loc_5CE8')

    ChrTalk(
        0x000A,
        (
            '#1490441203V海利欧先生是诚实的人。\n',
            '不可能是犯人的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1490441231V所以，海利欧先生\n',
            '怎么可能是犯人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5D56(): pass

    label('loc_5D56')

    Jump('loc_6363')

    def _loc_5D59(): pass

    label('loc_5D59')

    OP_28(0x006A, 0x01, 0x0200)

    If(
        (
            (Expr.PushReg, 0x8),
            (Expr.PushLong, 0x10),
            Expr.And,
            Expr.Return,
        ),
        'loc_5DDD',
    )

    ChrTalk(
        0x000A,
        (
            '#1490441232V午饭后诺曼先生\n',
            '和海利欧先生一同外出了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1490441233V然后海利欧先生\n',
            '一个人回来上了２楼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5E4D')

    def _loc_5DDD(): pass

    label('loc_5DDD')

    ExecExpressionWithReg(
        0x0008,
        (
            (Expr.PushLong, 0x10),
            Expr.Or2,
            Expr.Return,
        ),
    )

    ChrTalk(
        0x000A,
        (
            '#1490441234V午饭是从拉旺塔尔\n',
            '叫的外卖。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1490441235V大家是在令人怀念又怀念的\n',
            '地方用了餐呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5E4D(): pass

    label('loc_5E4D')

    Jump('loc_6363')

    def _loc_5E50(): pass

    label('loc_5E50')

    OP_28(0x006A, 0x01, 0x0200)

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x01, 0x0800)"),
            Expr.Return,
        ),
        'loc_5ED0',
    )

    ChrTalk(
        0x000A,
        (
            '#1490441236V中午桥上的钟响的时候\n',
            '我正在整理餐具。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1490441237V不知道是谁把事务所的餐具\n',
            '收拾好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_61D7')

    def _loc_5ED0(): pass

    label('loc_5ED0')

    ExecExpressionWithReg(
        0x0008,
        (
            (Expr.PushLong, 0x20),
            Expr.Or2,
            Expr.Return,
        ),
    )

    OP_28(0x0069, 0x01, 0x0800)

    ChrTalk(
        0x000A,
        (
            '#1490441238V中午桥上的钟响的时候？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1490441239V嗯，我正在\n',
            '做着客厅的准备。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1490441240V结束以后\n',
            '我就去整理了餐具。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1490441241V不知道是谁把事务所的餐具\n',
            '收拾好了，所以\n',
            '我的工作也就很快做完了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(30)

    OP_62(0x0105, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0105,
        (
            '#0060441242V#044F事务所的餐具被人收拾好了……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010441243V#1004F也、也就是说……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441244V午饭后有人\n',
            '去了事务所！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0101, 400)

    ChrTalk(
        0x000A,
        (
            '#1490441245V是的，如您所说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1490441246V在准备客厅的时候，',
            (TxtCtl.SetColor, 0x4),
            '\n',
            '『收拾善后』',
            (TxtCtl.SetColor, 0x0),
            '的事有人替我做了……',
            TxtCtl.Enter,
        ),
    )

    PlaySE(17, 0x00, 0x64)
    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1490441247V等我发现的时候\n',
            '餐具已经堆放在前台了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1490441248V不过说起来，那位好心人\n',
            '究竟是哪位客人呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1490441249V不好意思，我也\n',
            '不知道……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010441250V#1007F是、是吗，真遗憾。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441251V还是我们自己去\n',
            '问一遍吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_61D7(): pass

    label('loc_61D7')

    Jump('loc_6363')

    def _loc_61DA(): pass

    label('loc_61DA')

    OP_28(0x006A, 0x01, 0x0200)

    ChrTalk(
        0x000A,
        (
            '#1490441252V我也不知道是\n',
            '哪一位收拾的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1490441253V应该是在我准备客厅时\n',
            '收拾的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6363')

    def _loc_6241(): pass

    label('loc_6241')

    OP_28(0x006A, 0x01, 0x0200)

    If(
        (
            (Expr.PushReg, 0x8),
            (Expr.PushLong, 0x80),
            Expr.And,
            Expr.Return,
        ),
        'loc_62D7',
    )

    ChrTalk(
        0x000A,
        (
            '#1490441254V贝尔夫先生吗……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1490441255V钟响的时候\n',
            '没看见啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1490441256V在我整理好餐具的时候\n',
            '他还在前厅呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_635D')

    def _loc_62D7(): pass

    label('loc_62D7')

    ExecExpressionWithReg(
        0x0008,
        (
            (Expr.PushLong, 0x80),
            Expr.Or2,
            Expr.Return,
        ),
    )

    ChrTalk(
        0x000A,
        (
            '#1490441254V贝尔夫先生吗……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1490441258V不知道，钟响的时候\n',
            '没看见啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1490441259V我正好在做\n',
            '客房的准备。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_635D(): pass

    label('loc_635D')

    Jump('loc_6363')

    def _loc_6360(): pass

    label('loc_6360')

    Jump('loc_6363')

    def _loc_6363(): pass

    label('loc_6363')

    Return()

# id: 0x000A offset: 0x6364
@scena.Code('func_0A_6364')
def func_0A_6364():
    TalkBegin(0x00FE)
    Call(1, 0x0005)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_6394'),
        (0x00000001, 'loc_652D'),
        (0x00000002, 'loc_66FD'),
        (0x00000003, 'loc_6959'),
        (0x00000004, 'loc_6A7E'),
        (0x00000005, 'loc_6AFD'),
        (0x00000006, 'loc_6CC2'),
        (0x00000007, 'loc_6D2C'),
        (-1, 'loc_6D8D'),
    )

    def _loc_6394(): pass

    label('loc_6394')

    OP_28(0x006A, 0x01, 0x1000)

    If(
        (
            (Expr.PushReg, 0x5),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_6407',
    )

    ChrTalk(
        0x00FE,
        (
            '#1790441260V如果我们吵架的话，\n',
            '应该会有什么响声的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1790441261V没人说过这个吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_652A')

    def _loc_6407(): pass

    label('loc_6407')

    ExecExpressionWithReg(
        0x0005,
        (
            (Expr.PushLong, 0x1),
            Expr.Or2,
            Expr.Return,
        ),
    )

    ChrTalk(
        0x00FE,
        (
            '#1790441262V我说了好多次了，\n',
            '我只发现了德尔斯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x01, 0x0001)"),
            Expr.Return,
        ),
        'loc_649A',
    )

    ChrTalk(
        0x00FE,
        (
            '#1790441263V如果我们吵架的话，\n',
            '响声总会有的吧，\n',
            '没人说过这个吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_64ED')

    def _loc_649A(): pass

    label('loc_649A')

    ChrTalk(
        0x00FE,
        (
            '#1790441264V如果我们吵架的话，\n',
            (TxtCtl.SetColor, 0x4),
            '『响声』',
            (TxtCtl.SetColor, 0x0),
            '总会有的吧。\n',
            '没人说过这个吧？',
            TxtCtl.Enter,
        ),
    )

    PlaySE(17, 0x00, 0x64)
    CloseMessageWindow()

    def _loc_64ED(): pass

    label('loc_64ED')

    ChrTalk(
        0x00FE,
        (
            '#1790441265V当然了，我是很有礼貌地\n',
            '坐在沙发上的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0069, 0x01, 0x0001)

    def _loc_652A(): pass

    label('loc_652A')

    Jump('loc_6D90')

    def _loc_652D(): pass

    label('loc_652D')

    OP_28(0x006A, 0x01, 0x1000)

    If(
        (
            (Expr.PushReg, 0x5),
            (Expr.PushLong, 0x2),
            Expr.And,
            Expr.Return,
        ),
        'loc_65B1',
    )

    ChrTalk(
        0x00FE,
        (
            '#1790441266V我在这个房间的时候\n',
            '应该会有什么响声的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1790441267V是不是作证的那家伙的\n',
            '耳朵有问题？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_66FA')

    def _loc_65B1(): pass

    label('loc_65B1')

    ChrTalk(
        0x00FE,
        (
            '#1790441268V如果我和德尔斯争吵过的话\n',
            '应该会有什么响声的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x01, 0x0004)"),
            Expr.Return,
        ),
        'loc_66FA',
    )

    ExecExpressionWithReg(
        0x0005,
        (
            (Expr.PushLong, 0x2),
            Expr.Or2,
            Expr.Return,
        ),
    )

    ChrTalk(
        0x0101,
        (
            '#0010441269V#1015F可是说到巨大的响声，\n',
            '有人可以作证呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441270V还有人说有某种碰撞声\n',
            '从阳台传来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441271V#1002F……你对那个声音没印象吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1790441272V某种大的碰撞声？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1790441273V不，不可能的。\n',
            '我没听到过那种声音。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_66FA(): pass

    label('loc_66FA')

    Jump('loc_6D90')

    def _loc_66FD(): pass

    label('loc_66FD')

    OP_28(0x006A, 0x01, 0x1000)

    If(
        (
            (Expr.PushReg, 0x5),
            (Expr.PushLong, 0x4),
            Expr.And,
            Expr.Return,
        ),
        'loc_6790',
    )

    ChrTalk(
        0x00FE,
        (
            '#1790441274V我没有生过气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1790441275V再说我这次是\n',
            '代表我的阵营来道歉的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1790441276V怎么可能怒气冲冲的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6956')

    def _loc_6790(): pass

    label('loc_6790')

    ExecExpressionWithReg(
        0x0005,
        (
            (Expr.PushLong, 0x4),
            Expr.Or2,
            Expr.Return,
        ),
    )

    ChrTalk(
        0x00FE,
        (
            '#1790441277V说我生气了？\n',
            '说话真不负责任。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1790441278V要这么说的话海利欧\n',
            '那家伙比我态度还差呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1790441279V那家伙一看到我\n',
            '就露出厌恶的神情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x01, 0x0008)"),
            Expr.Return,
        ),
        'loc_688E',
    )

    ChrTalk(
        0x00FE,
        (
            '#1790441280V关于海利欧的事你们去打听一下吧。\n',
            '肯定能发现蛛丝马迹的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_68E4')

    def _loc_688E(): pass

    label('loc_688E')

    ChrTalk(
        0x00FE,
        (
            (TxtCtl.SetColor, 0x4),
            '#1790441281V『关于海利欧』',
            (TxtCtl.SetColor, 0x0),
            '的事你们去打听一下吧。\n',
            '肯定能发现蛛丝马迹的。',
            TxtCtl.Enter,
        ),
    )

    PlaySE(17, 0x00, 0x64)
    CloseMessageWindow()

    def _loc_68E4(): pass

    label('loc_68E4')

    ChrTalk(
        0x00FE,
        (
            '#1790441282V那家伙和德尔斯是争夺\n',
            '诺曼阵营二号人物的对手。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1790441283V一定是彼此不合就\n',
            '打起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0069, 0x01, 0x0008)

    def _loc_6956(): pass

    label('loc_6956')

    Jump('loc_6D90')

    def _loc_6959(): pass

    label('loc_6959')

    OP_28(0x006A, 0x01, 0x1000)

    If(
        (
            (Expr.PushReg, 0x5),
            (Expr.PushLong, 0x8),
            Expr.And,
            Expr.Return,
        ),
        'loc_69DB',
    )

    ChrTalk(
        0x00FE,
        (
            '#1790441284V海利欧和德尔斯是争夺\n',
            '诺曼阵营二号人物的对手。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1790441283V一定是彼此不合就\n',
            '打起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6A7B')

    def _loc_69DB(): pass

    label('loc_69DB')

    ExecExpressionWithReg(
        0x0005,
        (
            (Expr.PushLong, 0x8),
            Expr.Or2,
            Expr.Return,
        ),
    )

    ChrTalk(
        0x00FE,
        (
            '#1790441286V海利欧也有动机吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1790441282V那家伙和德尔斯是争夺\n',
            '诺曼阵营二号人物的对手。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1790441283V一定是彼此不合就\n',
            '打起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x006A, 0x01, 0x2000)

    def _loc_6A7B(): pass

    label('loc_6A7B')

    Jump('loc_6D90')

    def _loc_6A7E(): pass

    label('loc_6A7E')

    OP_28(0x006A, 0x01, 0x1000)

    ChrTalk(
        0x00FE,
        (
            '#1790441289V哟，原来是从拉旺塔尔\n',
            '叫来的外卖吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1790441290V还真有闲情逸致啊。\n',
            '下回我也去拜托波尔多斯先生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6D90')

    def _loc_6AFD(): pass

    label('loc_6AFD')

    OP_28(0x006A, 0x01, 0x1000)

    ChrTalk(
        0x00FE,
        (
            '#1790441291V拉升大桥时的钟声吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1790441292V哦，那时候我正好\n',
            '急着过桥呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1790441293V所以就偶然遇到了\n',
            '在桥边的诺曼先生他们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x01, 0x0100)"),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x0069, 0x01, 0x0080)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_6CBF',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x01, 0x0400)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6C77',
    )

    OP_28(0x0069, 0x01, 0x0100)

    ChrTalk(
        0x0101,
        (
            '#0010441294V#1019F唔……就是说……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441295V昆茨先生和\n',
            '那个声音没关系吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060441296V#047F根据证词，响声出现在\n',
            '钟声刚结束之后……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060441297V#042F据他本人所说，\n',
            '是这样的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6CBF')

    def _loc_6C77(): pass

    label('loc_6C77')

    ChrTalk(
        0x0101,
        (
            '#0010271019V#1002F这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441299V和诺曼先生的证词一样呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6CBF(): pass

    label('loc_6CBF')

    Jump('loc_6D90')

    def _loc_6CC2(): pass

    label('loc_6CC2')

    OP_28(0x006A, 0x01, 0x1000)

    ChrTalk(
        0x00FE,
        (
            '#1790441300V在找收拾餐具的人？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1790441301V算了，不管你们怎么做，\n',
            '快点证明我的无罪吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6D90')

    def _loc_6D2C(): pass

    label('loc_6D2C')

    OP_28(0x006A, 0x01, 0x1000)

    ChrTalk(
        0x00FE,
        (
            '#1790441302V钟响的时候\n',
            '贝尔夫在什么地方？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1790441303V我怎么可能\n',
            '知道那种事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6D90')

    def _loc_6D8D(): pass

    label('loc_6D8D')

    Jump('loc_6D90')

    def _loc_6D90(): pass

    label('loc_6D90')

    TalkEnd(0x00FE)

    Return()

# id: 0x000B offset: 0x6D94
@scena.Code('func_0B_6D94')
def func_0B_6D94():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x01, 0x2000)"),
            Expr.Return,
        ),
        'loc_6DFB',
    )

    ChrTalk(
        0x00FE,
        (
            '#0040441557V#030F呼，快要接近尾声了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040441558V那么，快点解决了\n',
            '举杯庆祝吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_754C')

    def _loc_6DFB(): pass

    label('loc_6DFB')

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x01, 0x0800)"),
            Expr.Return,
        ),
        'loc_6F22',
    )

    If(
        (
            (Expr.PushReg, 0xA),
            (Expr.PushLong, 0x40),
            Expr.And,
            Expr.Return,
        ),
        'loc_6E83',
    )

    ChrTalk(
        0x00FE,
        (
            '#0040441559V#035F我从小一直在城市里，\n',
            '站久了受不了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040441560V呵呵，就像美丽的花朵\n',
            '容易凋谢一样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6F1F')

    def _loc_6E83(): pass

    label('loc_6E83')

    ExecExpressionWithReg(
        0x000A,
        (
            (Expr.PushLong, 0x40),
            Expr.Or2,
            Expr.Return,
        ),
    )

    ChrTalk(
        0x00FE,
        (
            '#0040441561V#034F呼，开始有点累了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040441562V我从小一直在城市里，\n',
            '站久了受不了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040441563V#037F呵呵，就像美丽的花朵\n',
            '容易凋谢一样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6F1F(): pass

    label('loc_6F1F')

    Jump('loc_754C')

    def _loc_6F22(): pass

    label('loc_6F22')

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x01, 0x0040)"),
            Expr.Return,
        ),
        'loc_7039',
    )

    If(
        (
            (Expr.PushReg, 0xA),
            (Expr.PushLong, 0x20),
            Expr.And,
            Expr.Return,
        ),
        'loc_6FB3',
    )

    ChrTalk(
        0x00FE,
        (
            '#0040441564V#035F钟的事情我以前\n',
            '在旅游向导里读过。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040441565V想法是很好，\n',
            '不过如果用长笛代替钟\n',
            '的话应该更好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7036')

    def _loc_6FB3(): pass

    label('loc_6FB3')

    ExecExpressionWithReg(
        0x000A,
        (
            (Expr.PushLong, 0x20),
            Expr.Or2,
            Expr.Return,
        ),
    )

    ChrTalk(
        0x00FE,
        (
            '#0040441566V#030F钟就是指\n',
            '那座大桥上的钟吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040441567V那个以前\n',
            '在书里读过。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040441568V哦，那本书叫旅游向导。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7036(): pass

    label('loc_7036')

    Jump('loc_754C')

    def _loc_7039(): pass

    label('loc_7039')

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x01, 0x0010)"),
            Expr.Return,
        ),
        'loc_71BC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Return,
        ),
        'loc_70C3',
    )

    ChrTalk(
        0x00FE,
        (
            '#0040441569V#031F呵呵，我就觉得有点奇怪，\n',
            '果然是这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040441570V想不到连人心都能读懂……\n',
            '我还真是个罪人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_71B9')

    def _loc_70C3(): pass

    label('loc_70C3')

    If(
        (
            (Expr.PushReg, 0xA),
            (Expr.PushLong, 0x10),
            Expr.And,
            Expr.Return,
        ),
        'loc_7129',
    )

    ChrTalk(
        0x00FE,
        (
            '#0040441571V#030F我查到了今天的\n',
            '午饭菜谱……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040441572V呼，果然冷盘是个问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_71B9')

    def _loc_7129(): pass

    label('loc_7129')

    ExecExpressionWithReg(
        0x000A,
        (
            (Expr.PushLong, 0x10),
            Expr.Or2,
            Expr.Return,
        ),
    )

    ChrTalk(
        0x00FE,
        (
            '#0040441571V#030F我查到了今天的\n',
            '午饭菜谱……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040441574V#035F呼，果然冷盘是个问题。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040441575V真希望能拿出点\n',
            '更精致的菜肴。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_71B9(): pass

    label('loc_71B9')

    Jump('loc_754C')

    def _loc_71BC(): pass

    label('loc_71BC')

    If(
        (
            (Expr.Eval, "OP_29(0x006A, 0x01, 0x0010)"),
            Expr.Return,
        ),
        'loc_7248',
    )

    ChrTalk(
        0x00FE,
        (
            '#0040441576V#032F呼，总觉得这个\n',
            '在前台的人样子有点古怪。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040441577V如果用逼问让他动摇的话,\n',
            '说不定会得到意外的情报哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_754C')

    def _loc_7248(): pass

    label('loc_7248')

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x01, 0x0008)"),
            Expr.Return,
        ),
        'loc_73F2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_72DF',
    )

    ChrTalk(
        0x00FE,
        (
            '#0040441578V#034F呼，真服了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040441579V从刚才起阿加特\n',
            '就对我不理不睬。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040441580V#032F唔，要不要我在他\n',
            '耳边吹口气呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7366')

    def _loc_72DF(): pass

    label('loc_72DF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_7366',
    )

    ChrTalk(
        0x00FE,
        (
            '#0040441578V#034F呼，真服了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040441582V从刚才起雪拉\n',
            '就对我不理不睬。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040441580V#032F唔，要不要我在她\n',
            '耳边吹口气呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7366(): pass

    label('loc_7366')

    If(
        (
            (Expr.PushReg, 0xA),
            (Expr.PushLong, 0x2),
            Expr.And,
            Expr.Return,
        ),
        'loc_7376',
    )

    Jump('loc_73EF')

    def _loc_7376(): pass

    label('loc_7376')

    ExecExpressionWithReg(
        0x000A,
        (
            (Expr.PushLong, 0x2),
            Expr.Or2,
            Expr.Return,
        ),
    )

    ChrTalk(
        0x0101,
        (
            '#0010441584V#1015F我不会阻止你……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441585V#1007F不过我觉得那么做的话，\n',
            '伤害事件就会变成杀人事件了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_73EF(): pass

    label('loc_73EF')

    Jump('loc_754C')

    def _loc_73F2(): pass

    label('loc_73F2')

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x01, 0x0002)"),
            Expr.Return,
        ),
        'loc_7469',
    )

    ChrTalk(
        0x00FE,
        (
            '#0040441586V#030F嗯，从这里看晚霞的话\n',
            '一定非常美。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040441587V有时间的话我真想\n',
            '悠闲地多逗留一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_754C')

    def _loc_7469(): pass

    label('loc_7469')

    If(
        (
            (Expr.PushReg, 0xA),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_74BD',
    )

    ChrTalk(
        0x00FE,
        (
            '#0040441588V#031F呵呵，我那华丽的语言艺术\n',
            '终于可以大显神威了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_754C')

    def _loc_74BD(): pass

    label('loc_74BD')

    ExecExpressionWithReg(
        0x000A,
        (
            (Expr.PushLong, 0x1),
            Expr.Or2,
            Expr.Return,
        ),
    )

    ChrTalk(
        0x00FE,
        (
            '#0040441589V#031F呵呵，我那华丽的语言艺术\n',
            '终于可以大显神威了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040441590V你们就见识一下我那独占了\n',
            '社交界话题的玫瑰色语言吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_754C(): pass

    label('loc_754C')

    TalkEnd(0x00FE)

    Return()

# id: 0x000C offset: 0x7550
@scena.Code('func_0C_7550')
def func_0C_7550():
    Call(1, 0x0005)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_757D'),
        (0x00000001, 'loc_7686'),
        (0x00000002, 'loc_771C'),
        (0x00000003, 'loc_779E'),
        (0x00000004, 'loc_78BB'),
        (0x00000005, 'loc_7C94'),
        (0x00000006, 'loc_802B'),
        (0x00000007, 'loc_841B'),
        (-1, 'loc_84C1'),
    )

    def _loc_757D(): pass

    label('loc_757D')

    OP_28(0x006A, 0x01, 0x0800)

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_75E4',
    )

    ChrTalk(
        0x00FE,
        (
            '#2870441398V昆茨站在倒地的\n',
            '德尔斯旁边。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2870441399V他的脸色很吃惊哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7683')

    def _loc_75E4(): pass

    label('loc_75E4')

    ExecExpressionWithReg(
        0x0004,
        (
            (Expr.PushLong, 0x1),
            Expr.Or2,
            Expr.Return,
        ),
    )

    ChrTalk(
        0x00FE,
        (
            '#2870441398V昆茨站在倒地的\n',
            '德尔斯旁边。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2870441401V看到我们以后\n',
            '他好像很吃惊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2870441402V虽然没有兴奋的感觉，\n',
            '不过总之表情很惊讶。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7683(): pass

    label('loc_7683')

    Jump('loc_84C4')

    def _loc_7686(): pass

    label('loc_7686')

    OP_28(0x006A, 0x01, 0x0800)

    ChrTalk(
        0x00FE,
        (
            '#2870441403V就像昆茨说的那样，\n',
            '一点也没听见有什么响声。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2870441404V我那时正在前厅，\n',
            '如果有成年人上楼去的话，\n',
            '当然能听到些声音的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_84C4')

    def _loc_771C(): pass

    label('loc_771C')

    OP_28(0x006A, 0x01, 0x0800)

    ChrTalk(
        0x00FE,
        (
            '#2870441405V在大桥边遇到的时候\n',
            '没发现他有在生气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2870441406V当然，说不定是在\n',
            '领他去酒店的时候\n',
            '发生了什么吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_84C4')

    def _loc_779E(): pass

    label('loc_779E')

    OP_28(0x006A, 0x01, 0x0800)

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x8),
            Expr.And,
            Expr.Return,
        ),
        'loc_7824',
    )

    ChrTalk(
        0x00FE,
        (
            '#2870441407V争夺二号人物位置这种\n',
            '说法只不过是臆测而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2870441408V我想诸位也不会相信\n',
            '这种传言的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_78B8')

    def _loc_7824(): pass

    label('loc_7824')

    ExecExpressionWithReg(
        0x0004,
        (
            (Expr.PushLong, 0x8),
            Expr.Or2,
            Expr.Return,
        ),
    )

    ChrTalk(
        0x00FE,
        (
            '#2870441409V怀疑海利欧是无法\n',
            '令人信服的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2870441410V再说他为什么要\n',
            '伤害自己的同事德尔斯呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2870441411V有什么动机吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_78B8(): pass

    label('loc_78B8')

    Jump('loc_84C4')

    def _loc_78BB(): pass

    label('loc_78BB')

    OP_28(0x006A, 0x01, 0x0800)

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x10),
            Expr.And,
            Expr.Return,
        ),
        'loc_7945',
    )

    ChrTalk(
        0x00FE,
        (
            '#2870441412V午饭后，我和海利欧\n',
            '去演说现场进行了预练。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2870441413V海利欧因为有事，\n',
            '后来才在那里和我会合。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7C91')

    def _loc_7945(): pass

    label('loc_7945')

    ExecExpressionWithReg(
        0x0004,
        (
            (Expr.PushLong, 0x10),
            Expr.Or2,
            Expr.Return,
        ),
    )

    ChrTalk(
        0x00FE,
        (
            '#2870441414V嗯，今天的午饭\n',
            '是从拉旺塔尔叫的外卖。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2870441415V总是同样的菜谱的话\n',
            '工作人员也会吃腻的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010441416V#1011F哟，还真是用心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060441417V#040F或者说政治家的工作\n',
            '就是这些事情吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0105, 400)

    ChrTalk(
        0x00FE,
        (
            '#2870441418V哈哈，你说的很有道理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2870441419V无时无刻不在用心，\n',
            '脑细胞都被大量杀伤了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060441420V#045F好、好像很可怜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010441421V#1007F确、确实……\n',
            '做到这种程度真不容易。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441422V#1002F这些先说到这里，诺曼先生。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441423V你午饭后在干什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#2870441424V哦，我和海利欧\n',
            '为了去演说现场进行预练而出了门。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2870441425V海利欧因为有其它事\n',
            '而和我约好在目的地会合的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010441426V#1000F午饭后立即外出，\n',
            '然后在外面和海利欧先生会合了是吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441427V嗯，只要确认了这一点就ＯＫ了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2870441428V能帮上你们吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2870441429V那么，接下来还要继续拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7C91(): pass

    label('loc_7C91')

    Jump('loc_84C4')

    def _loc_7C94(): pass

    label('loc_7C94')

    OP_28(0x006A, 0x01, 0x0800)

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x20),
            Expr.And,
            Expr.Return,
        ),
        'loc_7D03',
    )

    ChrTalk(
        0x00FE,
        (
            '#2870441430V桥上的钟响了的时候吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2870441431V我和海利欧一起在\n',
            '演说现场预练。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8028')

    def _loc_7D03(): pass

    label('loc_7D03')

    ExecExpressionWithReg(
        0x0004,
        (
            (Expr.PushLong, 0x20),
            Expr.Or2,
            Expr.Return,
        ),
    )

    ChrTalk(
        0x00FE,
        (
            '#2870441430V桥上的钟响了的时候吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2870441431V我和海利欧一起在\n',
            '演说现场预练。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010441434V#1002F海利欧先生也在那里？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#2870441435V嗯，他那时已经来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2870441436V正好在钟响的时候\n',
            '那个昆茨来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2870441437V我拜托海利欧把他带去酒店，\n',
            '所以应该不会记错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010441438V#1015F是吗，那应该不会错了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x01, 0x0400)"),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x0069, 0x01, 0x0080)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_8028',
    )

    ChrTurnDirection(0x0105, 0x0101, 400)

    ChrTalk(
        0x0105,
        (
            '#0060441439V#043F这么说的话，艾丝蒂尔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060441440V穆拉德先生听到的响声\n',
            '看来和海利欧先生没关系了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0105, 400)

    ChrTalk(
        0x0101,
        (
            '#0010441441V#1015F嗯，不光是海利欧先生，\n',
            '和昆茨先生也变得无关了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441442V穆拉德先生听到响声\n',
            '是在钟刚响之后……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441443V不过那时两个人都和\n',
            '诺曼先生在一起。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441444V#1002F也就是说，那个响声的制造者既不是\n',
            '海利欧先生也不是昆茨先生……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441445V两个人作为犯人的可能性\n',
            '这样一来就相当低了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0069, 0x01, 0x0400)

    def _loc_8028(): pass

    label('loc_8028')

    Jump('loc_84C4')

    def _loc_802B(): pass

    label('loc_802B')

    OP_28(0x006A, 0x01, 0x0800)

    If(
        (
            (Expr.Eval, "OP_29(0x006A, 0x01, 0x0004)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_82C8',
    )

    OP_28(0x006A, 0x01, 0x0004)

    ChrTalk(
        0x00FE,
        (
            '#2870441446V那么，到底\n',
            '是谁做的呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2870441447V在我们出门的期间\n',
            '似乎有人收拾了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010441448V#1015F这么说……\n',
            '诺曼先生也不知道呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#2870441449V嗯，很遗憾……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2870441450V可是，虽然不知道是谁……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2870441451V不过我可能给那个好人\n',
            '留下了不好的回忆了。',
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

    ChrTalk(
        0x0105,
        (
            '#0060441453V#043F出什么事了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0105, 400)

    ChrTalk(
        0x00FE,
        (
            '#2870441454V嗯，其实最近……\n',
            '我一直没有食欲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2870441455V中午的什锦饭\n',
            '我也剩下了很多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2870441456V难得亚内斯特瞒着大家\n',
            '为我特别订了特制什锦饭……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2870441457V……哎呀，真是见笑了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010441458V#1007F是、是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441459V呼，参加选举也真不容易。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8418')

    def _loc_82C8(): pass

    label('loc_82C8')

    ChrTalk(
        0x00FE,
        (
            '#2870441447V在我们出门的期间\n',
            '似乎有人收拾了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2870441461V可是，我竟然会\n',
            '做出这么让人见笑的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2870441462V难得亚内斯特秘密地\n',
            '为我特别订了特制什锦饭……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2870441463V结果因为提不起食欲\n',
            '剩下了很多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2870441464V不好意思，请你们\n',
            '不要告诉大家这件事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2870441465V我不想惹上『健康问题』\n',
            '之类的不必要麻烦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8418(): pass

    label('loc_8418')

    Jump('loc_84C4')

    def _loc_841B(): pass

    label('loc_841B')

    OP_28(0x006A, 0x01, 0x0800)

    ChrTalk(
        0x00FE,
        (
            '#2870441466V唔，桥上的钟响时\n',
            '我儿子所在的地点是个疑点？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2870441467V如果有合理的嫌疑\n',
            '就不用顾及我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2870441468V拘捕贝尔夫，\n',
            '审讯他也没关系。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_84C4')

    def _loc_84C1(): pass

    label('loc_84C1')

    Jump('loc_84C4')

    def _loc_84C4(): pass

    label('loc_84C4')

    Return()

# id: 0x000D offset: 0x84C5
@scena.Code('func_0D_84C5')
def func_0D_84C5():
    Call(1, 0x0005)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_84F2'),
        (0x00000001, 'loc_85DD'),
        (0x00000002, 'loc_86EC'),
        (0x00000003, 'loc_8731'),
        (0x00000004, 'loc_8852'),
        (0x00000005, 'loc_88AA'),
        (0x00000006, 'loc_89BF'),
        (0x00000007, 'loc_8B2E'),
        (-1, 'loc_8C27'),
    )

    def _loc_84F2(): pass

    label('loc_84F2')

    If(
        (
            (Expr.PushReg, 0x6),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_8566',
    )

    ChrTalk(
        0x00FE,
        (
            '#2850441469V呼，如果我看到犯人的话\n',
            '就能帮上你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2850441470V好痛……\n',
            '头还是阵阵地疼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_85DA')

    def _loc_8566(): pass

    label('loc_8566')

    ExecExpressionWithReg(
        0x0006,
        (
            (Expr.PushLong, 0x1),
            Expr.Or2,
            Expr.Return,
        ),
    )

    ChrTalk(
        0x00FE,
        (
            '#2850441471V一瞬间我就昏过去了，\n',
            '所以没看见犯人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2850441472V如果看上一眼的话\n',
            '就能帮上你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_85DA(): pass

    label('loc_85DA')

    Jump('loc_8C2A')

    def _loc_85DD(): pass

    label('loc_85DD')

    If(
        (
            (Expr.PushReg, 0x6),
            (Expr.PushLong, 0x2),
            Expr.And,
            Expr.Return,
        ),
        'loc_865D',
    )

    ChrTalk(
        0x00FE,
        (
            '#2850441473V如果说声响的话，\n',
            '那就是我被袭击时的声音了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2850441474V因为那是响彻头脑的\n',
            '可怕冲击声啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_86E9')

    def _loc_865D(): pass

    label('loc_865D')

    ExecExpressionWithReg(
        0x0006,
        (
            (Expr.PushLong, 0x2),
            Expr.Or2,
            Expr.Return,
        ),
    )

    ChrTalk(
        0x00FE,
        (
            '#2850441475V声响吗……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2850441476V啊，那个应该\n',
            '是我被袭击时的声音了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2850441474V因为那是响彻头脑的\n',
            '可怕冲击。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_86E9(): pass

    label('loc_86E9')

    Jump('loc_8C2A')

    def _loc_86EC(): pass

    label('loc_86EC')

    ChrTalk(
        0x00FE,
        (
            '#2850441478V呼，是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2850441479V问我我也不知道啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8C2A')

    def _loc_8731(): pass

    label('loc_8731')

    If(
        (
            (Expr.PushReg, 0x6),
            (Expr.PushLong, 0x8),
            Expr.And,
            Expr.Return,
        ),
        'loc_8798',
    )

    ChrTalk(
        0x00FE,
        (
            '#2850441480V我甚至可以保证\n',
            '海利欧不是犯人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2850441481V因为他完全没有动机。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_884F')

    def _loc_8798(): pass

    label('loc_8798')

    ExecExpressionWithReg(
        0x0006,
        (
            (Expr.PushLong, 0x8),
            Expr.Or2,
            Expr.Return,
        ),
    )

    ChrTalk(
        0x00FE,
        (
            '#2850441482V海利欧不可能是犯人。\n',
            '这一点我可以保证啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2850441483V我们没什么过节，\n',
            '而且生意上还有合作关系！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2850441484V啊，好痛……\n',
            '因、因为太兴奋了头又……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_884F(): pass

    label('loc_884F')

    Jump('loc_8C2A')

    def _loc_8852(): pass

    label('loc_8852')

    ChrTalk(
        0x00FE,
        (
            '#2850441485V是的，饭菜是从\n',
            '拉旺塔尔叫的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2850441486V哎呀，真的很好吃啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8C2A')

    def _loc_88AA(): pass

    label('loc_88AA')

    If(
        (
            (Expr.PushReg, 0x6),
            (Expr.PushLong, 0x20),
            Expr.And,
            Expr.Return,
        ),
        'loc_8924',
    )

    ChrTalk(
        0x00FE,
        (
            '#2850441487V在我晕过去之前，\n',
            '好像听到了钟声……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2850441488V因为记忆有点模糊了，\n',
            '我也不敢确定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_89BC')

    def _loc_8924(): pass

    label('loc_8924')

    ExecExpressionWithReg(
        0x0006,
        (
            (Expr.PushLong, 0x20),
            Expr.Or2,
            Expr.Return,
        ),
    )

    ChrTalk(
        0x00FE,
        (
            '#2850441489V大桥上的钟声吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2850441490V这么一说，我在\n',
            '被袭击之前似乎听到过……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2850441491V嗯～抱歉。\n',
            '记忆实在是不清楚了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_89BC(): pass

    label('loc_89BC')

    Jump('loc_8C2A')

    def _loc_89BF(): pass

    label('loc_89BF')

    If(
        (
            (Expr.PushReg, 0x6),
            (Expr.PushLong, 0x40),
            Expr.And,
            Expr.Return,
        ),
        'loc_8A39',
    )

    ChrTalk(
        0x00FE,
        (
            '#2850441492V我当时在事务所，\n',
            '如果有人来收拾的话\n',
            '我应该会注意到的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2850441493V嗯～真奇怪啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8B2B')

    def _loc_8A39(): pass

    label('loc_8A39')

    ExecExpressionWithReg(
        0x0006,
        (
            (Expr.PushLong, 0x40),
            Expr.Or2,
            Expr.Return,
        ),
    )

    ChrTalk(
        0x00FE,
        (
            '#2850441494V咦，说起来\n',
            '是谁收拾的呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2850441495V对、对不起，\n',
            '我记不得了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010441496V#1002F不过你人在事务所吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441497V如果有人来收拾的话\n',
            '你应该能注意到的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2850441498V嗯～是啊。\n',
            '我自己也觉得很奇怪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8B2B(): pass

    label('loc_8B2B')

    Jump('loc_8C2A')

    def _loc_8B2E(): pass

    label('loc_8B2E')

    If(
        (
            (Expr.PushReg, 0x6),
            (Expr.PushLong, 0x80),
            Expr.And,
            Expr.Return,
        ),
        'loc_8BC0',
    )

    ChrTalk(
        0x00FE,
        (
            '#2850441499V听见钟声时\n',
            '贝尔夫在哪里？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2850441500V问我也没用啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2850441501V因为我连有没有听到\n',
            '过钟声都记不得了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8C24')

    def _loc_8BC0(): pass

    label('loc_8BC0')

    ExecExpressionWithReg(
        0x0006,
        (
            (Expr.PushLong, 0x80),
            Expr.Or2,
            Expr.Return,
        ),
    )

    ChrTalk(
        0x00FE,
        (
            '#2850441499V听见钟声时\n',
            '贝尔夫在哪里？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2850441503V不，我不知道……\n',
            '他有嫌疑吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8C24(): pass

    label('loc_8C24')

    Jump('loc_8C2A')

    def _loc_8C27(): pass

    label('loc_8C27')

    Jump('loc_8C2A')

    def _loc_8C2A(): pass

    label('loc_8C2A')

    Return()

# id: 0x000E offset: 0x8C2B
@scena.Code('func_0E_8C2B')
def func_0E_8C2B():
    If(
        (
            (Expr.Eval, "OP_29(0x006A, 0x01, 0x0008)"),
            (Expr.Eval, "OP_29(0x006A, 0x01, 0x0010)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_8FE5',
    )

    EventBegin(0x00)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirectionByPos(0x0101, 5710, 30, 400)

    ChrTalk(
        0x0101,
        (
            '#0010441546V#1011F啊……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    CameraMove(2870, 0, 2140, 0)
    ChrSetPos(0x0101, 560, 0, 2430, 122)
    ChrSetPos(0x0105, -370, 0, 2740, 122)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_8CDA',
    )

    OP_4A(0x0015, 0)
    CreateThread(0x0015, 0x01, 0x01, 0x001B)

    Jump('loc_8CEC')

    def _loc_8CDA(): pass

    label('loc_8CDA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_8CEC',
    )

    OP_4A(0x0016, 0)
    CreateThread(0x0016, 0x01, 0x01, 0x001B)

    def _loc_8CEC(): pass

    label('loc_8CEC')

    Sleep(400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_8D1D',
    )

    @scena.Lambda('lambda_8CFE')
    def lambda_8CFE():
        ChrTurnDirection(0x0101, 0x0015, 400)
        Yield()

        Jump('lambda_8CFE')

    DispatchAsync2(0x0101, 0x0002, lambda_8CFE)

    @scena.Lambda('lambda_8D0F')
    def lambda_8D0F():
        ChrTurnDirection(0x0105, 0x0015, 400)
        Yield()

        Jump('lambda_8D0F')

    DispatchAsync2(0x0105, 0x0002, lambda_8D0F)

    Jump('loc_8D46')

    def _loc_8D1D(): pass

    label('loc_8D1D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_8D46',
    )

    @scena.Lambda('lambda_8D2A')
    def lambda_8D2A():
        ChrTurnDirection(0x0101, 0x0016, 400)
        Yield()

        Jump('lambda_8D2A')

    DispatchAsync2(0x0101, 0x0002, lambda_8D2A)

    @scena.Lambda('lambda_8D3B')
    def lambda_8D3B():
        ChrTurnDirection(0x0105, 0x0016, 400)
        Yield()

        Jump('lambda_8D3B')

    DispatchAsync2(0x0105, 0x0002, lambda_8D3B)

    def _loc_8D46(): pass

    label('loc_8D46')

    ChrSetRGBAMask(0x0017, 255, 255, 255, 0, 0)

    @scena.Lambda('lambda_8D57')
    def lambda_8D57():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0017, 0x0002, lambda_8D57)

    OP_4A(0x0017, 0)
    CreateThread(0x0017, 0x01, 0x01, 0x001C)

    @scena.Lambda('lambda_8D74')
    def lambda_8D74():
        CameraMove(560, 0, 2430, 2000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_8D74)

    WaitForThreadExit(0x0017, 0x0001)
    WaitForThreadExit(0x0000, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010441547V#1000F事务所的\n',
            '询问已经结束了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_8E10',
    )

    ChrTalk(
        0x0015,
        (
            '#0050441548V#050F嗯，完成了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050441549V……你们那边怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8E5C')

    def _loc_8E10(): pass

    label('loc_8E10')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_8E5C',
    )

    ChrTalk(
        0x0016,
        (
            '#0030441550V#020F嗯，已经完成了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030441551V你们那边怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8E5C(): pass

    label('loc_8E5C')

    ChrTalk(
        0x0101,
        (
            '#0010441552V#1015F嗯，也差不多了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441553V#1006F好，再仔细调查一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_8EDD',
    )

    ChrTalk(
        0x0015,
        (
            '#0050441554V#050F……别松懈啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8F0B')

    def _loc_8EDD(): pass

    label('loc_8EDD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_8F0B',
    )

    ChrTalk(
        0x0016,
        (
            '#0030441555V#020F调查不能松懈哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8F0B(): pass

    label('loc_8F0B')

    ChrTalk(
        0x0101,
        (
            '#0010441556V#1000F嗯，交给我们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_8F44',
    )

    CreateThread(0x0015, 0x01, 0x01, 0x001D)

    Jump('loc_8F52')

    def _loc_8F44(): pass

    label('loc_8F44')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_8F52',
    )

    CreateThread(0x0016, 0x01, 0x01, 0x001D)

    def _loc_8F52(): pass

    label('loc_8F52')

    Sleep(400)

    CreateThread(0x0017, 0x01, 0x01, 0x001E)
    WaitForThreadExit(0x0017, 0x0001)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_8F82',
    )

    ChrSetPos(0x0015, -3320, 0, 9510, 45)
    OP_4B(0x0015, 0)

    Jump('loc_8F9E')

    def _loc_8F82(): pass

    label('loc_8F82')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_8F9E',
    )

    ChrSetPos(0x0016, -3320, 0, 9510, 45)
    OP_4B(0x0016, 0)

    def _loc_8F9E(): pass

    label('loc_8F9E')

    ChrSetPos(0x0017, -2620, 0, 8220, 0)
    OP_4B(0x0017, 0)
    OP_28(0x006A, 0x01, 0x0010)
    ChrSetPos(0x0014, -7880, 0, 83450, 0)
    ChrSetPos(0x000E, -3740, 0, 78670, 0)
    TerminateThread(0x0101, 0x02)
    TerminateThread(0x0105, 0x02)
    EventEnd(0x00)

    def _loc_8FE5(): pass

    label('loc_8FE5')

    Return()

# id: 0x000F offset: 0x8FE6
@scena.Code('func_0F_8FE6')
def func_0F_8FE6():
    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x00, 0x08)"),
            (Expr.Eval, "OP_29(0x0069, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0069, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_9120',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_908A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_903E',
    )

    ChrTalk(
        0x0101,
        (
            '#0010441591V#1007F还不能出去啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9087')

    def _loc_903E(): pass

    label('loc_903E')

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    ChrTalk(
        0x0101,
        (
            '#0010441592V#1015F啊，这边是门口了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441593V得先回去询问。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9087(): pass

    label('loc_9087')

    Jump('loc_9105')

    def _loc_908A(): pass

    label('loc_908A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_90BF',
    )

    ChrTalk(
        0x0105,
        (
            '#0060441594V#042F还不能去别的地方啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9105')

    def _loc_90BF(): pass

    label('loc_90BF')

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    ChrTalk(
        0x0105,
        (
            '#0060441595V#042F这边是门口呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060441596V得先回去询问呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9105(): pass

    label('loc_9105')

    ChrMoveToRelative(0x0000, 0, 0, 1000, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_9120(): pass

    label('loc_9120')

    Return()

# id: 0x0010 offset: 0x9121
@scena.Code('func_10_9121')
def func_10_9121():
    TalkBegin(0x00FE)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrTurnDirection(0x00FE, 0x0000, 0)
    OP_4A(0x00FE, 0)
    ChrTurnDirection(0x0000, 0x00FE, 0)
    ChrTurnDirection(0x0001, 0x00FE, 0)
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
            TXT(0x00, '【说话】\n'),
            TXT(0x01, '【报告】\n'),
            TXT(0x02, '【放弃】\n'),
            TXT(0x03, '【取消】\n'),
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

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_91B4'),
        (0x00000001, 'loc_91F3'),
        (0x00000002, 'loc_921D'),
        (-1, 'loc_9486'),
    )

    def _loc_91B4(): pass

    label('loc_91B4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_91C2',
    )

    Call(1, 0x0011)

    Jump('loc_91CD')

    def _loc_91C2(): pass

    label('loc_91C2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_91CD',
    )

    Call(1, 0x0012)

    def _loc_91CD(): pass

    label('loc_91CD')

    If(
        (
            (Expr.Eval, "OP_29(0x006A, 0x01, 0x0010)"),
            Expr.Return,
        ),
        'loc_91E2',
    )

    ChrTurnDirection(0x00FE, 0x000A, 0)

    Jump('loc_91E9')

    def _loc_91E2(): pass

    label('loc_91E2')

    ChrSetDirection(0x00FE, 0, 0)

    def _loc_91E9(): pass

    label('loc_91E9')

    OP_4B(0x00FE, 0)
    TalkEnd(0x00FE)

    Jump('loc_94AC')

    def _loc_91F3(): pass

    label('loc_91F3')

    Call(1, 0x0013)

    If(
        (
            (Expr.Eval, "OP_29(0x006A, 0x01, 0x0010)"),
            Expr.Return,
        ),
        'loc_920C',
    )

    ChrTurnDirection(0x00FE, 0x000A, 0)

    Jump('loc_9213')

    def _loc_920C(): pass

    label('loc_920C')

    ChrSetDirection(0x00FE, 0, 0)

    def _loc_9213(): pass

    label('loc_9213')

    OP_4B(0x00FE, 0)
    TalkEnd(0x00FE)

    Jump('loc_94AC')

    def _loc_921D(): pass

    label('loc_921D')

    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '要放弃吗？',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)

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
            TXT(0x00, '【放弃】\n'),
            TXT(0x01, '【再努力一下】\n'),
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
        'loc_92CE',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x006A, 0x01, 0x0010)"),
            Expr.Return,
        ),
        'loc_92BF',
    )

    ChrTurnDirection(0x00FE, 0x000A, 0)

    Jump('loc_92C6')

    def _loc_92BF(): pass

    label('loc_92BF')

    ChrSetDirection(0x00FE, 0, 0)

    def _loc_92C6(): pass

    label('loc_92C6')

    OP_4B(0x00FE, 0)
    TalkEnd(0x00FE)

    Return()

    def _loc_92CE(): pass

    label('loc_92CE')

    EventBegin(0x00)
    ChrTurnDirection(0x0017, 0x0000, 0)
    OP_4A(0x0017, 255)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_9371',
    )

    ChrTalk(
        0x0015,
        (
            '#0050441597V#052F……要放弃查吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050441598V#053F算了，随便你了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050441599V#050F我会继续调查的。\n',
            '在我搞定之前你就在外面等着吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9413')

    def _loc_9371(): pass

    label('loc_9371')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_9413',
    )

    ChrTalk(
        0x0016,
        (
            '#0030441600V#023F……要放弃调查吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030441601V#026F算了，如果没自信\n',
            '解决的话也没办法。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030441602V#022F我会继续调查的。\n',
            '你就在外边先等候一会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9413(): pass

    label('loc_9413')

    FadeOut(2000, 0, -1)
    OP_0D()
    PlaySE(262, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【选举事务所的伤人事件】',
            (TxtCtl.SetColor, 0x0),
            '失败了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_28(0x0069, 0x04, 0x80)
    OP_28(0x0069, 0x04, 0x40)
    OP_28(0x0069, 0x01, 0x4000)
    SetScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    NewScene('ED6_DT21/T2100._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_94AC')

    def _loc_9486(): pass

    label('loc_9486')

    If(
        (
            (Expr.Eval, "OP_29(0x006A, 0x01, 0x0010)"),
            Expr.Return,
        ),
        'loc_949B',
    )

    ChrTurnDirection(0x00FE, 0x000A, 0)

    Jump('loc_94A2')

    def _loc_949B(): pass

    label('loc_949B')

    ChrSetDirection(0x00FE, 0, 0)

    def _loc_94A2(): pass

    label('loc_94A2')

    OP_4B(0x00FE, 0)
    TalkEnd(0x00FE)

    Jump('loc_94AC')

    def _loc_94AC(): pass

    label('loc_94AC')

    Return()

# id: 0x0011 offset: 0x94AD
@scena.Code('func_11_94AD')
def func_11_94AD():
    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x01, 0x2000)"),
            Expr.Return,
        ),
        'loc_950E',
    )

    ChrTalk(
        0x00FE,
        (
            '#0050441603V#050F看来快要找到事件的真相了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050441604V有了眉目就来报告吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_99A9')

    def _loc_950E(): pass

    label('loc_950E')

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x01, 0x0800)"),
            Expr.Return,
        ),
        'loc_95B3',
    )

    ChrTalk(
        0x00FE,
        (
            '#0050441605V#050F到了现在\n',
            '又有重要的证词出现了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050441606V如果没头绪的话就把\n',
            '询问过的内容再询问一遍看看。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050441607V放弃的话就前功尽弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_99A9')

    def _loc_95B3(): pass

    label('loc_95B3')

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x01, 0x0040)"),
            Expr.Return,
        ),
        'loc_9620',
    )

    ChrTalk(
        0x00FE,
        (
            '#0050441608V#050F钟声吗……\n',
            '确实是一个线索。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050441609V没关系。\n',
            '就按你所想的去尝试吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_99A9')

    def _loc_9620(): pass

    label('loc_9620')

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x01, 0x0010)"),
            Expr.Return,
        ),
        'loc_96E9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Return,
        ),
        'loc_969E',
    )

    ChrTalk(
        0x00FE,
        (
            '#0050441610V#050F艾丝蒂尔你们\n',
            '去查一下刚才的证词内容吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050441223V我们再稍微\n',
            '在这里停留一会儿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_96E6')

    def _loc_969E(): pass

    label('loc_969E')

    ChrTalk(
        0x00FE,
        (
            '#0050441612V#050F有什么发现吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050441613V别放弃，要坚持\n',
            '追查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_96E6(): pass

    label('loc_96E6')

    Jump('loc_99A9')

    def _loc_96E9(): pass

    label('loc_96E9')

    If(
        (
            (Expr.Eval, "OP_29(0x006A, 0x01, 0x0010)"),
            Expr.Return,
        ),
        'loc_97C2',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x01, 0x0010)"),
            Expr.Return,
        ),
        'loc_976D',
    )

    ChrTalk(
        0x00FE,
        (
            '#0050441610V#050F艾丝蒂尔你们去\n',
            '去查一下刚才的证词内容吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050441223V我们再稍微\n',
            '在这里停留一会儿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_97BF')

    def _loc_976D(): pass

    label('loc_976D')

    ChrTalk(
        0x00FE,
        (
            '#0050441616V#050F有新线索了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050441617V希望能在其中\n',
            '找到可信的证词……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_97BF(): pass

    label('loc_97BF')

    Jump('loc_99A9')

    def _loc_97C2(): pass

    label('loc_97C2')

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x01, 0x0008)"),
            Expr.Return,
        ),
        'loc_9822',
    )

    ChrTalk(
        0x00FE,
        (
            '#0050441618V#050F嫌疑人仍然很模糊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050441619V该是扩大调查\n',
            '范围的时候了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_99A9')

    def _loc_9822(): pass

    label('loc_9822')

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x01, 0x0002)"),
            Expr.Return,
        ),
        'loc_98A7',
    )

    ChrTalk(
        0x00FE,
        (
            '#0050441620V#050F嫌疑人都已经询问过了，\n',
            '不过他们说的话都含糊不清。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050441621V别被那些刻意编排的\n',
            '证词给蒙蔽了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_99A9')

    def _loc_98A7(): pass

    label('loc_98A7')

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x01, 0x0001)"),
            Expr.Return,
        ),
        'loc_994B',
    )

    If(
        (
            (Expr.PushReg, 0xB),
            (Expr.PushLong, 0x2),
            Expr.And,
            Expr.Return,
        ),
        'loc_98F3',
    )

    ChrTalk(
        0x00FE,
        (
            '#0050441622V#050F……明白的话就快点开工吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9948')

    def _loc_98F3(): pass

    label('loc_98F3')

    ExecExpressionWithReg(
        0x000B,
        (
            (Expr.PushLong, 0x2),
            Expr.Or2,
            Expr.Return,
        ),
    )

    ChrTalk(
        0x00FE,
        (
            '#0050441623V#050F有什么新的线索了吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050441624V有的话就追查下去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9948(): pass

    label('loc_9948')

    Jump('loc_99A9')

    def _loc_994B(): pass

    label('loc_994B')

    ChrTalk(
        0x00FE,
        (
            '#0050441625V#050F先去询问有关嫌疑人的问题。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050441626V如果有新的线索\n',
            '就继续追查下去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_99A9(): pass

    label('loc_99A9')

    Return()

# id: 0x0012 offset: 0x99AA
@scena.Code('func_12_99AA')
def func_12_99AA():
    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x01, 0x2000)"),
            Expr.Return,
        ),
        'loc_9A10',
    )

    ChrTalk(
        0x00FE,
        (
            '#0030441627V#020F快要看到结果了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030441628V确定了嫌疑人的话\n',
            '就马上来报告吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9EFA')

    def _loc_9A10(): pass

    label('loc_9A10')

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x01, 0x0800)"),
            Expr.Return,
        ),
        'loc_9ABD',
    )

    ChrTalk(
        0x00FE,
        (
            '#0030441629V#022F到了现在\n',
            '又有重要的证词出现了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030441630V如果没头绪的话就把以前\n',
            '询问过的内容再询问一遍看看。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030441631V放弃的话就前功尽弃了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9EFA')

    def _loc_9ABD(): pass

    label('loc_9ABD')

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x01, 0x0040)"),
            Expr.Return,
        ),
        'loc_9B1F',
    )

    ChrTalk(
        0x00FE,
        (
            '#0030441632V#020F原来如此，钟声啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030441633V想法不错。\n',
            '按你的想法做吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9EFA')

    def _loc_9B1F(): pass

    label('loc_9B1F')

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x01, 0x0010)"),
            Expr.Return,
        ),
        'loc_9C12',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Return,
        ),
        'loc_9BA1',
    )

    ChrTalk(
        0x00FE,
        (
            '#0030441634V#022F艾丝蒂尔你们\n',
            '去追查一下刚才的证词的内容吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030441225V我们再稍微\n',
            '在这里停留一会儿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9C0F')

    def _loc_9BA1(): pass

    label('loc_9BA1')

    ChrTalk(
        0x00FE,
        (
            '#0030441636V#020F咦，有什么发现吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030441637V询问情况最需要坚韧不拔的毅力。\n',
            '不要放弃，继续追查下去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9C0F(): pass

    label('loc_9C0F')

    Jump('loc_9EFA')

    def _loc_9C12(): pass

    label('loc_9C12')

    If(
        (
            (Expr.Eval, "OP_29(0x006A, 0x01, 0x0010)"),
            Expr.Return,
        ),
        'loc_9CED',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x01, 0x0010)"),
            Expr.Return,
        ),
        'loc_9C98',
    )

    ChrTalk(
        0x00FE,
        (
            '#0030441634V#022F艾丝蒂尔你们\n',
            '去追查一下刚才的证词的内容吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030441225V我们再稍微\n',
            '在这里停留一会儿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9CEA')

    def _loc_9C98(): pass

    label('loc_9C98')

    ChrTalk(
        0x00FE,
        (
            '#0030441640V#020F有新线索了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030441641V希望能在其中\n',
            '找到可信的证词……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9CEA(): pass

    label('loc_9CEA')

    Jump('loc_9EFA')

    def _loc_9CED(): pass

    label('loc_9CED')

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x01, 0x0008)"),
            Expr.Return,
        ),
        'loc_9D51',
    )

    ChrTalk(
        0x00FE,
        (
            '#0030441642V#020F嫌疑人仍然很模糊啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030441643V该是扩大调查\n',
            '范围的时候了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9EFA')

    def _loc_9D51(): pass

    label('loc_9D51')

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x01, 0x0002)"),
            Expr.Return,
        ),
        'loc_9DD4',
    )

    ChrTalk(
        0x00FE,
        (
            '#0030441644V#020F嫌疑人都已经询问过了，\n',
            '不过他们说的话都含糊不清。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030441645V要相信哪个证词\n',
            '需要慎重地思考。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9EFA')

    def _loc_9DD4(): pass

    label('loc_9DD4')

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x01, 0x0001)"),
            Expr.Return,
        ),
        'loc_9E91',
    )

    If(
        (
            (Expr.PushReg, 0xB),
            (Expr.PushLong, 0x2),
            Expr.And,
            Expr.Return,
        ),
        'loc_9E36',
    )

    ChrTalk(
        0x00FE,
        (
            '#0030441646V#020F喂喂，还在磨蹭什么。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030441647V快点回去调查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9E8E')

    def _loc_9E36(): pass

    label('loc_9E36')

    ExecExpressionWithReg(
        0x000B,
        (
            (Expr.PushLong, 0x2),
            Expr.Or2,
            Expr.Return,
        ),
    )

    ChrTalk(
        0x00FE,
        (
            '#0030441648V#020F发现什么线索了吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030441649V如果有的话\n',
            '就追查下去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9E8E(): pass

    label('loc_9E8E')

    Jump('loc_9EFA')

    def _loc_9E91(): pass

    label('loc_9E91')

    ChrTalk(
        0x00FE,
        (
            '#0030441650V#020F首先要从收集\n',
            '嫌疑人的情报开始。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030441651V如果发现什么线索的话\n',
            '就立即追查下去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9EFA(): pass

    label('loc_9EFA')

    Return()

# id: 0x0013 offset: 0x9EFB
@scena.Code('func_13_9EFB')
def func_13_9EFB():
    EventBegin(0x00)

    ExecExpressionWithValue(
        0x0018,
        0x04,
        (
            (Expr.GetChrWork, 0x17, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrTurnDirection(0x0017, 0x0101, 0)
    OP_4A(0x0017, 255)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_9F6D',
    )

    ChrTurnDirection(0x0015, 0x0101, 0)

    ChrTalk(
        0x0015,
        (
            '#0050441652V#052F……有眉目了吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050441653V#057F那么嫌疑犯是谁？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9FC9')

    def _loc_9F6D(): pass

    label('loc_9F6D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_9FC9',
    )

    ChrTurnDirection(0x0016, 0x0101, 0)

    ChrTalk(
        0x0016,
        (
            '#0030441654V#023F……知道犯人是谁了？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030441655V#022F那么谁是嫌疑犯？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9FC9(): pass

    label('loc_9FC9')

    FadeOut(300, 0, 100)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0xFFFFFF),
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

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetMessageWindowPos(-1, 16, -1, -1)

    Talk(
        (
            0x18,
            '伤害案的犯人是谁？',
            TxtCtl.Enter,
        ),
    )

    OP_CC(0x00, 0x00, 0x000A, 0x000A, 0x01)
    OP_CC(0x01, 0x00, '昆茨')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0xFFFFF0),
            Expr.And,
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x1),
            Expr.Mul,
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.Eval, "OP_29(0x006A, 0x01, 0x0800)"),
            Expr.Return,
        ),
        'loc_A080',
    )

    OP_CC(0x01, 0x00, '诺曼')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0xFFFF0F),
            Expr.And,
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x10),
            Expr.Mul,
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_A080(): pass

    label('loc_A080')

    If(
        (
            (Expr.Eval, "OP_29(0x006A, 0x01, 0x0400)"),
            Expr.Return,
        ),
        'loc_A0B7',
    )

    OP_CC(0x01, 0x00, '海利欧')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0xFFF0FF),
            Expr.And,
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x100),
            Expr.Mul,
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_A0B7(): pass

    label('loc_A0B7')

    If(
        (
            (Expr.Eval, "OP_29(0x006A, 0x01, 0x0200)"),
            Expr.Return,
        ),
        'loc_A0F0',
    )

    OP_CC(0x01, 0x00, '亚内斯特')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0xFF0FFF),
            Expr.And,
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x1000),
            Expr.Mul,
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_A0F0(): pass

    label('loc_A0F0')

    If(
        (
            (Expr.Eval, "OP_29(0x006A, 0x01, 0x0100)"),
            Expr.Return,
        ),
        'loc_A12B',
    )

    OP_CC(0x01, 0x00, '穆拉德老人')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0xF0FFFF),
            Expr.And,
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x10000),
            Expr.Mul,
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_A12B(): pass

    label('loc_A12B')

    If(
        (
            (Expr.Eval, "OP_29(0x006A, 0x01, 0x0080)"),
            Expr.Return,
        ),
        'loc_A162',
    )

    OP_CC(0x01, 0x00, '贝尔夫')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0xFFFFF),
            Expr.And,
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x100000),
            Expr.Mul,
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_A162(): pass

    label('loc_A162')

    OP_CC(0x01, 0x00, '离开')
    OP_CC(0x02, 0x00)
    MenuEnd(0x0000)
    OP_5F(0x0000)
    SetMessageWindowPos(72, 320, 56, 3)

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
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x10),
            Expr.Div,
            (Expr.PushLong, 0xF),
            Expr.And,
            Expr.Equ,
            (Expr.PushReg, 0x0),
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x1000),
            Expr.Div,
            (Expr.PushLong, 0xF),
            Expr.And,
            Expr.Equ,
            Expr.Or,
            (Expr.PushReg, 0x0),
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x10000),
            Expr.Div,
            (Expr.PushLong, 0xF),
            Expr.And,
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_A52E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_A301',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x006A, 0x01, 0x0010)"),
            (Expr.PushReg, 0x0),
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x1000),
            Expr.Div,
            (Expr.PushLong, 0xF),
            Expr.And,
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_A27B',
    )

    ChrTalk(
        0x0015,
        (
            '#0050441656V#055F啊……！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050441657V你说这个大叔\n',
            '是犯人吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050441658V#551F算了……\n',
            '先说说排除第一个\n',
            '嫌疑人的理由吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A2FE')

    def _loc_A27B(): pass

    label('loc_A27B')

    ChrTalk(
        0x0015,
        (
            '#0050441656V#055F啊……！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050441660V你说那个大叔\n',
            '是犯人吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050441658V#551F算了……\n',
            '先说说排除第一个\n',
            '嫌疑人的理由吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A2FE(): pass

    label('loc_A2FE')

    Jump('loc_A438')

    def _loc_A301(): pass

    label('loc_A301')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_A438',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x006A, 0x01, 0x0010)"),
            (Expr.PushReg, 0x0),
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x1000),
            Expr.Div,
            (Expr.PushLong, 0xF),
            Expr.And,
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_A3B1',
    )

    ChrTalk(
        0x0016,
        (
            '#0030441662V#023F啊……！？\n',
            '你说这个人是犯人？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030441663V#025F有确凿的\n',
            '根据吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030441664V先说说排除第一个\n',
            '嫌疑人的理由吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A438')

    def _loc_A3B1(): pass

    label('loc_A3B1')

    ChrTalk(
        0x0016,
        (
            '#0030441665V#023F啊……！？\n',
            '你说那个人是犯人？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030441663V#025F有确凿的\n',
            '根据吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030441664V先说说排除第一个\n',
            '嫌疑人的理由吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A438(): pass

    label('loc_A438')

    ClearScenaFlags(ScenaFlag(0x0001, 4, 0xC))
    Call(1, 0x0014)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_A52B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_A4B8',
    )

    ChrTalk(
        0x0015,
        (
            '#0050441668V#050F那么，接下来就要拿出\n',
            '这个嫌疑人犯罪的证明了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050441669V……你有什么根据吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A527')

    def _loc_A4B8(): pass

    label('loc_A4B8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_A527',
    )

    ChrTalk(
        0x0016,
        (
            '#0030441670V#027F那么，接下来就要拿出\n',
            '这个嫌疑人犯罪的证明了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030441671V……你有什么根据吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A527(): pass

    label('loc_A527')

    Call(1, 0x0015)

    def _loc_A52B(): pass

    label('loc_A52B')

    Jump('loc_AA94')

    def _loc_A52E(): pass

    label('loc_A52E')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x1),
            Expr.Div,
            (Expr.PushLong, 0xF),
            Expr.And,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A5EB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_A596',
    )

    ChrTalk(
        0x0015,
        (
            '#0050441672V#057F……最初的嫌疑人吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050441673V那根据是什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A5E4')

    def _loc_A596(): pass

    label('loc_A596')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_A5E4',
    )

    ChrTalk(
        0x0016,
        (
            '#0030441674V#022F……最初的嫌疑人啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030441675V那根据是什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A5E4(): pass

    label('loc_A5E4')

    Call(1, 0x0016)

    Jump('loc_AA94')

    def _loc_A5EB(): pass

    label('loc_A5EB')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x100),
            Expr.Div,
            (Expr.PushLong, 0xF),
            Expr.And,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A7CF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_A668',
    )

    ChrTalk(
        0x0015,
        (
            '#0050441676V#052F……哟，是第一发现人吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050441677V#050F那么你这么想的根据是什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A6C6')

    def _loc_A668(): pass

    label('loc_A668')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_A6C6',
    )

    ChrTalk(
        0x0016,
        (
            '#0030441678V#023F……哟，那不是第一发现人吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030441679V你这么想的根据是什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A6C6(): pass

    label('loc_A6C6')

    ClearScenaFlags(ScenaFlag(0x0001, 5, 0xD))
    Call(1, 0x0017)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Return,
        ),
        'loc_A7CC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_A74F',
    )

    ChrTalk(
        0x0015,
        (
            '#0050441680V#050F但如果是这样的话，\n',
            '最初的嫌疑人又是怎么回事呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050441681V有可以否定\n',
            '昆茨犯罪的根据吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A7C5')

    def _loc_A74F(): pass

    label('loc_A74F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_A7C5',
    )

    ChrTalk(
        0x0016,
        (
            '#0030441682V#022F如果是这样的话，\n',
            '最初的嫌疑人又是怎么回事呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030441683V有可以否定\n',
            '昆茨犯罪的根据吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A7C5(): pass

    label('loc_A7C5')

    SetScenaFlags(ScenaFlag(0x0002, 0, 0x10))
    Call(1, 0x0014)

    def _loc_A7CC(): pass

    label('loc_A7CC')

    Jump('loc_AA94')

    def _loc_A7CF(): pass

    label('loc_A7CF')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x100000),
            Expr.Div,
            (Expr.PushLong, 0xF),
            Expr.And,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A9F5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_A86F',
    )

    ChrTalk(
        0x0015,
        (
            '#0050441684V#050F……渡鸦帮的小子啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050441685V你有确凿的\n',
            '根据吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050441686V先说说排除第一个\n',
            '嫌疑人昆茨的理由吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A8F7')

    def _loc_A86F(): pass

    label('loc_A86F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_A8F7',
    )

    ChrTalk(
        0x0016,
        (
            '#0030441687V#022F……渡鸦帮的小子啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030441688V你有确凿的\n',
            '根据吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030441689V说说排除第一个\n',
            '嫌疑人昆茨先生的理由吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A8F7(): pass

    label('loc_A8F7')

    ClearScenaFlags(ScenaFlag(0x0001, 4, 0xC))
    Call(1, 0x0014)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_A9F2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_A97B',
    )

    ChrTalk(
        0x0015,
        (
            '#0050441690V#050F那么接下来就要拿出\n',
            '这个嫌疑人犯罪的证明了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050441691V……那你有什么样的根据呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A9EE')

    def _loc_A97B(): pass

    label('loc_A97B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_A9EE',
    )

    ChrTalk(
        0x0016,
        (
            '#0030441692V#022F那么接下来就要拿出\n',
            '这个嫌疑人犯罪的证明了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030441693V……那你有什么样的根据呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A9EE(): pass

    label('loc_A9EE')

    Call(1, 0x0018)

    def _loc_A9F2(): pass

    label('loc_A9F2')

    Jump('loc_AA94')

    def _loc_A9F5(): pass

    label('loc_A9F5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_AA48',
    )

    ChrTalk(
        0x0015,
        (
            '#0050441694V#050F什么啊，还没确定？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050441695V好了，仔细调查吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_AA94')

    def _loc_AA48(): pass

    label('loc_AA48')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_AA94',
    )

    ChrTalk(
        0x0016,
        (
            '#0030441696V#020F咦，还没确定？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030441697V好了，仔细调查吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_AA94(): pass

    label('loc_AA94')

    ExecExpressionWithValue(
        0x0017,
        0x04,
        (
            (Expr.GetChrWork, 0x18, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_4B(0x0017, 255)
    MapSetFlags(0x00000001)
    EventEnd(0x03)

    Return()

# id: 0x0014 offset: 0xAAAA
@scena.Code('func_14_AAAA')
def func_14_AAAA():
    FadeOut(300, 0, 100)

    ExecExpressionWithReg(
        0x000C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0xFFFFFF),
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

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetMessageWindowPos(-1, 16, -1, -1)

    Talk(
        (
            0x18,
            '否定昆茨犯罪的根据呢？',
            TxtCtl.Enter,
        ),
    )

    OP_CC(0x00, 0x00, 0x000A, 0x000A, 0x00)
    OP_CC(0x01, 0x00, '【游击士的直觉：没什么根据，只不过那么想而已】')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0xFFFFF0),
            Expr.And,
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x1),
            Expr.Mul,
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x01, 0x0100)"),
            Expr.Return,
        ),
        'loc_ABB3',
    )

    OP_CC(0x01, 0x00, '【他本人的证词：　发出声响的时候在户外】')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0xFFFF0F),
            Expr.And,
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x10),
            Expr.Mul,
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_ABB3(): pass

    label('loc_ABB3')

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x01, 0x0400)"),
            Expr.Return,
        ),
        'loc_AC14',
    )

    OP_CC(0x01, 0x00, '【已被证明的事实：预想的犯罪时间内有不在场证明】')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0xFFF0FF),
            Expr.And,
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x100),
            Expr.Mul,
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_AC14(): pass

    label('loc_AC14')

    OP_CC(0x02, 0x00)
    MenuEnd(0x000C)
    OP_5F(0x0000)
    SetMessageWindowPos(72, 320, 56, 3)

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
            (Expr.PushReg, 0xC),
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x1),
            Expr.Div,
            (Expr.PushLong, 0xF),
            Expr.And,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_AD7A',
    )

    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '你说的犯罪理由\n',
            '好歹能够成立。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_ACF8',
    )

    ChrTalk(
        0x0015,
        (
            '#0050441698V#053F不行，这根本不象话……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050441699V好好地再去调查一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_AD4E')

    def _loc_ACF8(): pass

    label('loc_ACF8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_AD4E',
    )

    ChrTalk(
        0x0016,
        (
            '#0030441700V#025F不行，这根本不象话……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030441701V好好地再去调查一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_AD4E(): pass

    label('loc_AD4E')

    ChrTalk(
        0x0101,
        (
            '#0010290564V#1007F明、明白了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearScenaFlags(ScenaFlag(0x0001, 4, 0xC))

    Jump('loc_B3BE')

    def _loc_AD7A(): pass

    label('loc_AD7A')

    If(
        (
            (Expr.PushReg, 0xC),
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x10),
            Expr.Div,
            (Expr.PushLong, 0xF),
            Expr.And,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_AF32',
    )

    ChrTalk(
        0x0101,
        (
            '#0010441703V#1002F那个巨大的响声发出时，\n',
            '据他本人说他在户外。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441704V如果那个是犯罪发生时的声音的话，\n',
            '那么昆茨先生就不是嫌疑人了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_AE96',
    )

    ChrTalk(
        0x0015,
        (
            '#0050441705V#551F这只是他本人的辩解吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050441706V#057F怎么能随便地相信这些？\n',
            '取得证明之后再来说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_AF06')

    def _loc_AE96(): pass

    label('loc_AE96')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_AF06',
    )

    ChrTalk(
        0x0016,
        (
            '#0030441707V#025F这只是他本人的辩解吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030441708V#022F怎么能随便地相信这些？\n',
            '证实之后再来说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_AF06(): pass

    label('loc_AF06')

    ChrTalk(
        0x0101,
        (
            '#0010290564V#1007F明、明白了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearScenaFlags(ScenaFlag(0x0001, 4, 0xC))

    Jump('loc_B3BE')

    def _loc_AF32(): pass

    label('loc_AF32')

    If(
        (
            (Expr.PushReg, 0xC),
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x100),
            Expr.Div,
            (Expr.PushLong, 0xF),
            Expr.And,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B3BE',
    )

    ChrTalk(
        0x0101,
        (
            '#0010441710V#1002F那个巨大的响声发出时，\n',
            '昆茨先生确实在外面哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441711V从诺曼先生的证词中\n',
            '可以确认这一点。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441712V如果那个是犯罪发生时的声音的话，\n',
            '昆茨先生是犯人的可能性就很低了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_B074',
    )

    ChrTalk(
        0x0015,
        (
            '#0050441713V#053F哟，原来是这样……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050441714V那么同时海利欧的\n',
            '嫌疑也可以拿掉了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B0E1')

    def _loc_B074(): pass

    label('loc_B074')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_B0E1',
    )

    ChrTalk(
        0x0016,
        (
            '#0030441715V#022F原来如此，很合理的分析。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030441716V那么同时海利欧先生的\n',
            '嫌疑也可以拿掉了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B0E1(): pass

    label('loc_B0E1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 0, 0x10)),
            Expr.Return,
        ),
        'loc_B368',
    )

    ClearScenaFlags(ScenaFlag(0x0002, 0, 0x10))

    ChrTalk(
        0x0101,
        (
            '#0010441717V#1002F嗯，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441718V海利欧先生也确实\n',
            '和诺曼先生会合了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441719V#1015F……等等，咦、咦咦！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_B1C8',
    )

    ChrTalk(
        0x0015,
        (
            '#0050441720V#057F喂，你点什么头啊？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050441721V你刚才还在说\n',
            '海利欧是犯人的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B22B')

    def _loc_B1C8(): pass

    label('loc_B1C8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_B22B',
    )

    ChrTalk(
        0x0016,
        (
            '#0030441722V#025F唉，你同意个什么啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030441723V你刚才还在说\n',
            '海利欧先生是犯人的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B22B(): pass

    label('loc_B22B')

    ChrTalk(
        0x0101,
        (
            '#0010441724V#1008F啊，哈哈……抱歉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441725V头脑混乱到自己都不知道\n',
            '自己在说些什么了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_B2EA',
    )

    ChrTalk(
        0x0015,
        (
            '#0050441726V#053F把你要说的话整理好\n',
            '再来吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050441727V……然后我们再讨论。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B33F')

    def _loc_B2EA(): pass

    label('loc_B2EA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_B33F',
    )

    ChrTalk(
        0x0016,
        (
            '#0030441728V#026F整理一下论点\n',
            '再来吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030441729V……然后我们再讨论。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B33F(): pass

    label('loc_B33F')

    ChrTalk(
        0x0101,
        (
            '#0010290564V#1007F明、明白了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B3BE')

    def _loc_B368(): pass

    label('loc_B368')

    ChrTalk(
        0x0101,
        (
            '#0010441731V#1015F嗯，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441732V海利欧先生也确实\n',
            '和诺曼先生会合了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))

    def _loc_B3BE(): pass

    label('loc_B3BE')

    Return()

# id: 0x0015 offset: 0xB3BF
@scena.Code('func_15_B3BF')
def func_15_B3BF():
    FadeOut(300, 0, 100)

    ExecExpressionWithReg(
        0x000C,
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

    SetMessageWindowPos(-1, 16, -1, -1)

    Talk(
        (
            0x18,
            '证明嫌疑人犯罪的根据是？',
            TxtCtl.Enter,
        ),
    )

    OP_CC(0x00, 0x00, 0x000A, 0x000A, 0x00)
    OP_CC(0x01, 0x00, '【游击士的直觉：没什么根据，只不过那么想而已】')
    OP_CC(0x02, 0x00)
    MenuEnd(0x000C)
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
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '你说的犯罪理由\n',
            '好歹能够成立。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_B508',
    )

    ChrTalk(
        0x0015,
        (
            '#0050441698V#053F不行，这根本不象话……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050441699V好好地再去调查一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B55E')

    def _loc_B508(): pass

    label('loc_B508')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_B55E',
    )

    ChrTalk(
        0x0016,
        (
            '#0030441700V#025F不行，这根本不象话……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030441701V好好地再去调查一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B55E(): pass

    label('loc_B55E')

    ChrTalk(
        0x0101,
        (
            '#0010290564V#1007F明、明白了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Return()

# id: 0x0016 offset: 0xB585
@scena.Code('func_16_B585')
def func_16_B585():
    FadeOut(300, 0, 100)

    ExecExpressionWithReg(
        0x000C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0xFFFFFF),
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

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetMessageWindowPos(-1, 16, -1, -1)

    Talk(
        (
            0x18,
            '证明昆茨犯罪的根据是？',
            TxtCtl.Enter,
        ),
    )

    OP_CC(0x00, 0x00, 0x000A, 0x000A, 0x00)
    OP_CC(0x01, 0x00, '【游击士的直觉：从状况判断应该那样考虑】')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0xFFFFF0),
            Expr.And,
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x1),
            Expr.Mul,
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x01, 0x0002)"),
            Expr.Return,
        ),
        'loc_B68A',
    )

    OP_CC(0x01, 0x00, '【有关人员的证词：案件发生时嫌疑人在生气】')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0xFFFF0F),
            Expr.And,
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x10),
            Expr.Mul,
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_B68A(): pass

    label('loc_B68A')

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x01, 0x0400)"),
            Expr.Return,
        ),
        'loc_B6EB',
    )

    OP_CC(0x01, 0x00, '【已被证明的事实：预想的犯罪时间内有不在场证明】')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0xFFF0FF),
            Expr.And,
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x100),
            Expr.Mul,
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_B6EB(): pass

    label('loc_B6EB')

    OP_CC(0x02, 0x00)
    MenuEnd(0x000C)
    OP_5F(0x0000)
    SetMessageWindowPos(72, 320, 56, 3)

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
            (Expr.PushReg, 0xC),
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x1),
            Expr.Div,
            (Expr.PushLong, 0xF),
            Expr.And,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B796',
    )

    ChrTalk(
        0x0101,
        (
            '#0010441738V#1002F案件发生时的状况是最大的根据。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441739V想想桥上的骚乱，\n',
            '就能发现他的动机充足。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B97A')

    def _loc_B796(): pass

    label('loc_B796')

    If(
        (
            (Expr.PushReg, 0xC),
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x10),
            Expr.Div,
            (Expr.PushLong, 0xF),
            Expr.And,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B876',
    )

    ChrTalk(
        0x0101,
        (
            '#0010441740V#1002F首先状况是最大的根据。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441741V而且可以说动机也很充分。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441742V桥上的骚乱是最近的事，\n',
            '气没消也是很正常的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441743V因为确实有相关人员作证\n',
            '说嫌疑人当时在生气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B97A')

    def _loc_B876(): pass

    label('loc_B876')

    If(
        (
            (Expr.PushReg, 0xC),
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x100),
            Expr.Div,
            (Expr.PushLong, 0xF),
            Expr.And,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B97A',
    )

    ChrTalk(
        0x0101,
        (
            '#0010441710V#1002F那个巨大的响声发出时，\n',
            '昆茨先生确实在外面哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441711V从诺曼先生的证词中\n',
            '可以确认这一点。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441746V如果那个是犯罪发生时的声音的话，\n',
            '嫌疑人是犯人的可能性就很低了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441747V#1015F……等等，咦、咦咦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B97A(): pass

    label('loc_B97A')

    If(
        (
            (Expr.PushReg, 0xC),
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x100),
            Expr.Div,
            (Expr.PushLong, 0xF),
            Expr.And,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_BB71',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_B9F9',
    )

    ChrTalk(
        0x0015,
        (
            '#0050441748V#053F喂，你到底想说些什么？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050441749V这样一来昆茨\n',
            '不就不可能是犯人了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BA5A')

    def _loc_B9F9(): pass

    label('loc_B9F9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_BA5A',
    )

    ChrTalk(
        0x0016,
        (
            '#0030441750V#025F你到底想说些什么？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030441751V这样一来昆茨\n',
            '不就不可能是犯人了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BA5A(): pass

    label('loc_BA5A')

    ChrTalk(
        0x0101,
        (
            '#0010441724V#1008F啊，哈哈……抱歉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441725V头脑混乱到自己都不知道\n',
            '自己在说些什么了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_BB19',
    )

    ChrTalk(
        0x0015,
        (
            '#0050441726V#053F把你要说的话整理好\n',
            '再来吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050441727V……然后我们再讨论。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BB6E')

    def _loc_BB19(): pass

    label('loc_BB19')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_BB6E',
    )

    ChrTalk(
        0x0016,
        (
            '#0030441728V#026F整理一下论点\n',
            '再来吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030441729V……然后我们再讨论。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BB6E(): pass

    label('loc_BB6E')

    Jump('loc_BDE3')

    def _loc_BB71(): pass

    label('loc_BB71')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_BC47',
    )

    ChrTalk(
        0x0015,
        (
            '#0050441758V#053F嗯，确实是这样……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050441759V#050F可凭你刚才举出的这些根据，\n',
            '还不能否定所有其它的可能性。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050441760V就是说在这家伙之前可能\n',
            '已经有人进入房间了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050441761V你敢说这不可能吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BD1A')

    def _loc_BC47(): pass

    label('loc_BC47')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_BD1A',
    )

    ChrTalk(
        0x0016,
        (
            '#0030441762V#026F嗯，你所说的不错……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030441763V#022F可凭你刚才举出的这些根据，\n',
            '还不能否定所有其它的可能性。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030441764V就是说在这那之前可能\n',
            '已经有人进入房间了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030441765V你敢说这不可能吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BD1A(): pass

    label('loc_BD1A')

    ChrTalk(
        0x0101,
        (
            '#0010441766V#1015F这、这个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_BD93',
    )

    ChrTalk(
        0x0015,
        (
            '#0050441767V#053F那就再继续调查吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050441727V……然后我们再讨论。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BDE3')

    def _loc_BD93(): pass

    label('loc_BD93')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_BDE3',
    )

    ChrTalk(
        0x0016,
        (
            '#0030441769V#027F那就再继续调查吧',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030441729V……然后我们再讨论。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BDE3(): pass

    label('loc_BDE3')

    ChrTalk(
        0x0101,
        (
            '#0010290564V#1007F明、明白了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Return()

# id: 0x0017 offset: 0xBE0A
@scena.Code('func_17_BE0A')
def func_17_BE0A():
    FadeOut(300, 0, 100)

    ExecExpressionWithReg(
        0x000C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0xFFFFFF),
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

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetMessageWindowPos(-1, 16, -1, -1)

    Talk(
        (
            0x18,
            '证明海利欧是犯人的根据呢？',
            TxtCtl.Enter,
        ),
    )

    OP_CC(0x00, 0x00, 0x000A, 0x000A, 0x00)
    OP_CC(0x01, 0x00, '【游击士的直觉：没什么根据，只不过那么想而已】')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0xFFFFF0),
            Expr.And,
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x1),
            Expr.Mul,
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x01, 0x0010)"),
            Expr.Return,
        ),
        'loc_BF15',
    )

    OP_CC(0x01, 0x00, '【有关人员的证词：午饭后去过犯罪现场】')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0xFFFF0F),
            Expr.And,
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x10),
            Expr.Mul,
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_BF15(): pass

    label('loc_BF15')

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x01, 0x0020)"),
            Expr.Return,
        ),
        'loc_BF6C',
    )

    OP_CC(0x01, 0x00, '【已被证明的事实：午饭后去过犯罪现场】')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0xFFF0FF),
            Expr.And,
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x100),
            Expr.Mul,
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_BF6C(): pass

    label('loc_BF6C')

    OP_CC(0x02, 0x00)
    MenuEnd(0x000C)
    OP_5F(0x0000)
    SetMessageWindowPos(72, 320, 56, 3)

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
            (Expr.PushReg, 0xC),
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x1),
            Expr.Div,
            (Expr.PushLong, 0xF),
            Expr.And,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C0D2',
    )

    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '你说的犯罪理由\n',
            '好歹能够成立。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_C050',
    )

    ChrTalk(
        0x0015,
        (
            '#0050441698V#053F不行，这根本不象话……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050441699V好好地再去调查一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C0A6')

    def _loc_C050(): pass

    label('loc_C050')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_C0A6',
    )

    ChrTalk(
        0x0016,
        (
            '#0030441700V#025F不行，这根本不象话……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030441701V好好地再去调查一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C0A6(): pass

    label('loc_C0A6')

    ChrTalk(
        0x0101,
        (
            '#0010290564V#1007F明，明白了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearScenaFlags(ScenaFlag(0x0001, 5, 0xD))

    Jump('loc_C246')

    def _loc_C0D2(): pass

    label('loc_C0D2')

    If(
        (
            (Expr.PushReg, 0xC),
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x10),
            Expr.Div,
            (Expr.PushLong, 0xF),
            Expr.And,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C168',
    )

    ChrTalk(
        0x0101,
        (
            '#0010441777V#1002F有人目击海利欧先生\n',
            '在案件发生之前不久上了２楼。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441778V而且，他本人并没有\n',
            '积极地提供这一内容。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C246')

    def _loc_C168(): pass

    label('loc_C168')

    If(
        (
            (Expr.PushReg, 0xC),
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x100),
            Expr.Div,
            (Expr.PushLong, 0xF),
            Expr.And,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C246',
    )

    ChrTalk(
        0x0101,
        (
            '#0010441779V#1010F案件发生之前不久海利欧先生\n',
            '在事务所这点已经确定。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441780V而且，他本人并没有\n',
            '积极地提供这一内容……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441781V#1002F隐瞒曾在犯罪现场这一点\n',
            '就等于是在承认自己就是犯人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C246(): pass

    label('loc_C246')

    If(
        (
            (Expr.PushReg, 0xC),
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x1),
            Expr.Div,
            (Expr.PushLong, 0xF),
            Expr.And,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C260',
    )

    Jump('loc_C3A8')

    def _loc_C260(): pass

    label('loc_C260')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_C2C1',
    )

    ChrTalk(
        0x0015,
        (
            '#0050441782V#050F就是说有了可以怀疑他的证据是吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050441783V……动机怎么说呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C31F')

    def _loc_C2C1(): pass

    label('loc_C2C1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_C31F',
    )

    ChrTalk(
        0x0016,
        (
            '#0030441784V#020F就是说有了可以怀疑他的证据是吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030441785V……动机怎么说呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C31F(): pass

    label('loc_C31F')

    ChrTalk(
        0x0101,
        (
            '#0010441786V#1015F他和受害者是竞争\n',
            '二号人物的对手关系。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441787V虽然作为动机有点不够充分，\n',
            '不过在现在这种情况下就不好说了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 5, 0xD))

    def _loc_C3A8(): pass

    label('loc_C3A8')

    Return()

# id: 0x0018 offset: 0xC3A9
@scena.Code('func_18_C3A9')
def func_18_C3A9():
    FadeOut(300, 0, 100)

    ExecExpressionWithReg(
        0x000C,
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

    SetMessageWindowPos(-1, 16, -1, -1)

    Talk(
        (
            0x18,
            '能证明贝尔夫犯罪的根据呢？',
            TxtCtl.Enter,
        ),
    )

    OP_CC(0x00, 0x00, 0x000A, 0x000A, 0x00)
    OP_CC(0x01, 0x00, '【游击士的直觉：没什么根据，只不过那么想而已】')

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x01, 0x2000)"),
            Expr.Return,
        ),
        'loc_C468',
    )

    OP_CC(0x01, 0x00, '【已被证明的事实：预想的犯罪时间内没有不在场证明】')

    def _loc_C468(): pass

    label('loc_C468')

    OP_CC(0x02, 0x00)
    MenuEnd(0x000C)
    OP_5F(0x0000)
    SetMessageWindowPos(72, 320, 56, 3)

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
            (Expr.PushReg, 0xC),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C5BF',
    )

    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '你说的犯罪理由\n',
            '好歹能够成立。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_C542',
    )

    ChrTalk(
        0x0015,
        (
            '#0050441698V#053F不行，这根本不象话……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050441699V好好地再去调查一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C598')

    def _loc_C542(): pass

    label('loc_C542')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_C598',
    )

    ChrTalk(
        0x0016,
        (
            '#0030441700V#025F不行，这根本不象话……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030441701V好好地再去调查一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C598(): pass

    label('loc_C598')

    ChrTalk(
        0x0101,
        (
            '#0010290564V#1007F明，明白了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Return()

    def _loc_C5BF(): pass

    label('loc_C5BF')

    ChrTalk(
        0x0101,
        (
            '#0010441793V#1002F根据就是他的不在现场证明。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441794V有力的证词和他本人提供的\n',
            '不在现场证明相抵触。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441795V#1015F因为昆茨先生和海利欧先生\n',
            '是犯人的可能性已经被否定了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441796V这个人是最后一个\n',
            '有可能是犯人的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_C747',
    )

    ChrTalk(
        0x0015,
        (
            '#0050441797V#053F嗯，按照排除法的话确实是这样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050441798V#050F……但说到底这\n',
            '只能构成条件证据。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050441799V就没有更具有决定性的证据了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C7E1')

    def _loc_C747(): pass

    label('loc_C747')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_C7E1',
    )

    ChrTalk(
        0x0016,
        (
            '#0030441800V#026F嗯，按照排除法的话确实是这样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030441801V#022F……但说到底这\n',
            '只能构成条件证据。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030441802V还需要更具有决定性的证据呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C7E1(): pass

    label('loc_C7E1')

    FadeOut(300, 0, 100)

    ExecExpressionWithReg(
        0x000C,
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

    SetMessageWindowPos(-1, 16, -1, -1)

    Talk(
        (
            0x18,
            '支持贝尔夫就是犯人的证据呢？',
            TxtCtl.Enter,
        ),
    )

    OP_CC(0x00, 0x00, 0x000A, 0x000A, 0x00)
    OP_CC(0x01, 0x00, '【游击士的直觉：虽然没什么证据，不过我就是这么认为】')

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x01, 0x1000)"),
            Expr.Return,
        ),
        'loc_C898',
    )

    OP_CC(0x01, 0x00, '【证词矛盾：他知道特制什锦饭的事】')

    def _loc_C898(): pass

    label('loc_C898')

    OP_CC(0x02, 0x00)
    MenuEnd(0x000C)
    OP_5F(0x0000)
    SetMessageWindowPos(72, 320, 56, 3)

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
            (Expr.PushReg, 0xC),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_CA65',
    )

    ChrTalk(
        0x0101,
        (
            '#0010441803V#1007F嗯、嗯……虽然这么说。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441804V不过没什么特别有力的证据。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_C9B0',
    )

    ChrTalk(
        0x0015,
        (
            '#0050441805V#053F是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050441806V#050F那就再好好调查一下吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050441807V已经到最后关头了。\n',
            '只差一步应该就能解决案件了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CA3C')

    def _loc_C9B0(): pass

    label('loc_C9B0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_CA3C',
    )

    ChrTalk(
        0x0016,
        (
            '#0030441808V#026F是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030441809V#027F那就再好好调查一下吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030441810V已经到最后关头了。\n',
            '只差一步应该就能解决案件了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_CA3C(): pass

    label('loc_CA3C')

    ChrTalk(
        0x0101,
        (
            '#0010430933V#1002F嗯，我会努力的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Return()

    def _loc_CA65(): pass

    label('loc_CA65')

    ChrTalk(
        0x0101,
        (
            '#0010441812V#1015F虽然不知道是不是决定性的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441813V不过关于特制什锦饭的证词\n',
            '应该可以作为案件的参考。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_CB07',
    )

    ChrTalk(
        0x0015,
        (
            '#0050441814V#052F哦？怎么回事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CB33')

    def _loc_CB07(): pass

    label('loc_CB07')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_CB33',
    )

    ChrTalk(
        0x0016,
        (
            '#0030441815V#023F嗯？怎么回事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_CB33(): pass

    label('loc_CB33')

    ChrTalk(
        0x0101,
        (
            '#0010441816V#1002F嗯，贝尔夫先生说\n',
            '他是在１楼吃的午饭……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441817V可为什么他能看见在２楼的\n',
            '诺曼先生吃的特制什锦饭呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441818V而且连诺曼先生没吃完\n',
            '他都知道啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_CC3D',
    )

    ChrTalk(
        0x0015,
        (
            '#0050441819V#057F也就是说他上过２楼……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050441820V……你想说的是这个吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CC95')

    def _loc_CC3D(): pass

    label('loc_CC3D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_CC95',
    )

    ChrTalk(
        0x0016,
        (
            '#0030441821V#022F也就是说他上过２楼……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030441822V……你想说的是这个吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_CC95(): pass

    label('loc_CC95')

    ChrTalk(
        0x0101,
        (
            '#0010441823V#1002F嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_CD67',
    )

    ChrTalk(
        0x0015,
        (
            '#0050441824V#053F……………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050441825V#057F……好，我知道了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050441826V那就叫来贝尔夫\n',
            '问个清楚吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050441827V因为凭手头这点证据，\n',
            '还很难马上逮捕他。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CE39')

    def _loc_CD67(): pass

    label('loc_CD67')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_CE39',
    )

    ChrTalk(
        0x0016,
        (
            '#0030441828V#026F……………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030441829V#022F……明白了。\n',
            '我也基本上能够接受这一观点。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030441830V这样一来只能把他本人\n',
            '叫来问个清楚了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030441831V因为凭手头这点证据，\n',
            '还很难马上逮捕他。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_CE39(): pass

    label('loc_CE39')

    ChrTalk(
        0x0101,
        (
            '#0010441832V#1002F嗯、嗯……明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    Call(1, 0x0019)

    Return()

# id: 0x0019 offset: 0xCE73
@scena.Code('func_19_CE73')
def func_19_CE73():
    CameraMove(-44480, 0, 26180, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(72000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x000F, -46590, 0, 26370, 105)
    ChrSetPos(0x0101, -44610, 0, 25830, 300)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_CEF1',
    )

    ChrSetPos(0x0015, -44620, 0, 24750, 300)
    OP_4A(0x0015, 0)

    Jump('loc_CF0D')

    def _loc_CEF1(): pass

    label('loc_CEF1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_CF0D',
    )

    ChrSetPos(0x0016, -44620, 0, 24750, 300)
    OP_4A(0x0016, 0)

    def _loc_CF0D(): pass

    label('loc_CF0D')

    OP_4A(0x000F, 255)
    Sleep(1000)

    FadeIn(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x000F,
        (
            '#2810441833V怎、怎么了！？\n',
            '把我叫到这里来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#2810441834V我、我可什么都没做啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010441835V#1016F好了，冷静一点。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441836V我们又不会把你\n',
            '给吃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_D018',
    )

    ChrTalk(
        0x0015,
        (
            '#0050441837V#050F#2P如果你配合我们调查的话\n',
            '很快就能回去的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D060')

    def _loc_D018(): pass

    label('loc_D018')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_D060',
    )

    ChrTalk(
        0x0016,
        (
            '#0030441838V#020F#2P如果你配合我们调查的话\n',
            '很快就能回去的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D060(): pass

    label('loc_D060')

    ChrTalk(
        0x000F,
        (
            '#2810441839V配、配合……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010441840V#1002F嗯，希望你老实回答。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441841V……你午饭之后去了哪里？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000F, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x000F,
        (
            '#2810441842V我、我说了我一直在地下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_D176',
    )

    ChrTalk(
        0x0015,
        (
            '#0050441843V#057F#2P我可有言在先……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050441844V你撒谎的话是\n',
            '不可能离开这里的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D1D6')

    def _loc_D176(): pass

    label('loc_D176')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_D1D6',
    )

    ChrTalk(
        0x0016,
        (
            '#0030441845V#026F#2P我想提醒你一点……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030441846V你撒谎的话是\n',
            '不可能离开这里的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D1D6(): pass

    label('loc_D1D6')

    OP_62(0x000F, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000F,
        (
            '#2810441847V……唔……………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010441848V#1002F你并没有一直\n',
            '待在地下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441849V这一点我们已经知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#2810441850V……………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_D300',
    )

    ChrTalk(
        0x0015,
        (
            '#0050441851V#050F#2P如果没做什么亏心事的话\n',
            '就说实话吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050441852V#053F还是……\n',
            '已经没那种勇气了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D36F')

    def _loc_D300(): pass

    label('loc_D300')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_D36F',
    )

    ChrTalk(
        0x0016,
        (
            '#0030441853V#022F#2P如果没做什么亏心事的话\n',
            '就说实话吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030441854V还是……\n',
            '已经没那种勇气了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D36F(): pass

    label('loc_D36F')

    ChrTalk(
        0x000F,
        (
            '#2810441855V……唔……………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#2810441856V明、明白了……我说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#2810441857V今天……\n',
            '午饭之后……………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#2810441858V我……\n',
            '其实是去了事务所的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#2810441859V是去做善后工作的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010441860V#1002F善后工作……？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441861V那么，把餐具返还到\n',
            '前台的人就是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#2810441862V嗯，是我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#2810441863V因为大家都很忙，\n',
            '所以我就想去收拾餐具。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#2810441864V收拾完我又连\n',
            '事务所也清扫了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#2810441865V呼，想不到这件事会\n',
            '变成这样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010441866V#1004F哎……？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441867V话、话好像有点\n',
            '接不上……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441868V#1002F你只是收拾了餐具\n',
            '并且做了扫除吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441869V那个怎么会\n',
            '和案子扯上关系呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_D63A',
    )

    ChrTalk(
        0x0015,
        (
            '#0050441870V#050F#2P……你知道的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D66B')

    def _loc_D63A(): pass

    label('loc_D63A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_D66B',
    )

    ChrTalk(
        0x0016,
        (
            '#0030441871V#027F#2P……你知道的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D66B(): pass

    label('loc_D66B')

    ChrTalk(
        0x000F,
        (
            '#2810441872V嗯、嗯………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#2810441873V其实……………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    CameraMove(-2970, 0, 79000, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(35000, 0)
    OP_6E(262, 0)
    OP_4A(0x000B, 0)
    OP_4A(0x0014, 0)
    OP_4A(0x000E, 0)
    OP_4A(0x0017, 0)
    ChrSetPos(0x000B, -3200, 0, 81000, 180)
    ChrSetPos(0x0014, -2140, 0, 81000, 180)
    ChrSetPos(0x000E, -1300, 0, 80130, 215)
    ChrSetPos(0x000F, -2710, 0, 79250, 0)
    ChrSetPos(0x0101, -3400, 0, 77780, 0)
    ChrSetPos(0x0017, -3150, 0, 76370, 0)
    ChrSetPos(0x0105, -2150, 0, 76170, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_D793',
    )

    ChrSetPos(0x0015, -2400, 0, 77580, 0)

    Jump('loc_D7AB')

    def _loc_D793(): pass

    label('loc_D793')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_D7AB',
    )

    ChrSetPos(0x0016, -2400, 0, 77580, 0)

    def _loc_D7AB(): pass

    label('loc_D7AB')

    Sleep(1000)

    FadeIn(2000, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0x000B,
        (
            '#2870441874V…………呼，原来如此。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2870441875V我知道贝尔夫为了\n',
            '清扫而来过这个房间……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2870441876V这一点和本案……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2870441877V也就是对德尔斯的伤害案\n',
            '到底有怎样的关系呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010441878V#1007F#3P有很大的关系啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441879V#1000F总之先听听\n',
            '他本人的说明吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_D92A',
    )

    ChrTalk(
        0x0015,
        (
            '#0050441880V#050F……喂，说来听听。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#2810441881V啊，啊啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D97A')

    def _loc_D92A(): pass

    label('loc_D92A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_D97A',
    )

    ChrTalk(
        0x0016,
        (
            '#0030441882V#020F……喂，说明一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#2810441881V啊，啊啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D97A(): pass

    label('loc_D97A')

    ChrTalk(
        0x000F,
        (
            '#2810441884V房间的扫除结束之后，\n',
            '正想要回去的时候……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#2810441885V因为整理了很多地方，\n',
            '所以房间蒙上了一层灰。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#2810441886V然后就打开阳台的门\n',
            '想让空气流通一下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#2810441887V不过因为手上的餐具\n',
            '堆得像山一样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#2810441888V没、没办法的我……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#2810441889V就、就用力踢开了门。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x001A, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0014, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(30)

    OP_62(0x000E, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x000B, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(2000)

    CreateThread(0x0014, 0x01, 0x01, 0x001A)
    Sleep(30)

    CreateThread(0x000E, 0x01, 0x01, 0x001A)
    CreateThread(0x000B, 0x01, 0x01, 0x001A)

    @scena.Lambda('lambda_DB30')
    def lambda_DB30():
        CameraMove(-1140, 0, 84170, 2000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_DB30)

    @scena.Lambda('lambda_DB48')
    def lambda_DB48():
        CameraSetDistance(3030, 2000)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_DB48)

    OP_67(0, 5480, -10000, 2000)

    ChrTalk(
        0x001A,
        (
            '#2850441890V想、想不到那里的门………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010441891V#1007F#1P嗯，就像你们想象的一样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441892V那扇门正是\n',
            '砸晕德尔斯的犯人……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441893V#1002F猛然打开的门\n',
            '直接打击到了你的后脑部。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_DC73',
    )

    ChrTalk(
        0x0015,
        (
            '#0050441894V#551F#2P也就是说案件的真相\n',
            '其实是『不幸的意外』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DCBD')

    def _loc_DC73(): pass

    label('loc_DC73')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_DCBD',
    )

    ChrTalk(
        0x0016,
        (
            '#0030441895V#025F#2P也就是说案件的真相\n',
            '其实是『不幸的意外』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_DCBD(): pass

    label('loc_DCBD')

    Sleep(400)

    OP_59()
    Fade(1000)
    CameraMove(-2970, 0, 79000, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(35000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_62(0x0014, 0x00000000, 2000, 0x22, 0x24, 0x000000FA, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0014,
        (
            '#1790441896V咦！？那么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0014, 180, 800)
    Sleep(400)

    ChrTalk(
        0x0014,
        (
            '#1790441897V总之就是说我是无辜的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000E, 225, 400)
    Sleep(400)

    ChrTalk(
        0x000E,
        (
            '#2840441898V唔……\n',
            '看来是这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#1790441899V呼～真受不了。\n',
            '终于能无罪释放了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000B, 180, 400)
    Sleep(400)

    ChrTalk(
        0x000B,
        (
            '#2870441900V不过说起来还真是大动干戈呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2870441901V为什么你一开始没有自己承认？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2870441902V如果你那样做的话\n',
            '事情就不会闹得这么大了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#2810441903V对、对不起……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010441904V#1016F#3P嗯，话是没错，\n',
            '能不能就这么饶了他？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441905V到最后他还是\n',
            '拿出勇气说了出来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001A,
        (
            '#2850441906V嗯，身为被害者\n',
            '我也希望能够原谅他。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001A,
        (
            '#2850441907V因为我们已经知道了\n',
            '那个过失也不是恶意的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001A,
        (
            '#2850441908V当然，希望你开门的时候\n',
            '能够再小心一点……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000F, 0x001A, 400)

    ChrTalk(
        0x000F,
        (
            '#2810441909V德尔斯先生，真的很对不起。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000F, 0x0014, 400)

    ChrTalk(
        0x000F,
        (
            '#2810441910V还有昆茨先生也是。\n',
            '差点让你背负了这个罪名。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0014, 0x000F, 400)

    ChrTalk(
        0x0014,
        (
            '#1790441911V我倒是没什么。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#1790441912V到头来嫌疑还是被洗清了。\n',
            '这就足够了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '#0040441913V#031F#3P呼，这件事总算是了结了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060441914V#040F#4P嗯，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_E1C1',
    )

    ChrTalk(
        0x0015,
        (
            '#0050441915V#050F然后是贝尔夫……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050441916V接下来要怎么做\n',
            '全由你自己来决定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000F, 0x0015, 400)

    ChrTalk(
        0x000F,
        (
            '#2810441917V阿、阿加特先生……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '#0050441918V#051F啊啊，好好干啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050441919V#053F…………以上就是报告内容。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E1FB')

    def _loc_E1C1(): pass

    label('loc_E1C1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_E1FB',
    )

    ChrTalk(
        0x0016,
        (
            '#0030441920V#020F……以上就是报告内容，完毕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E1FB(): pass

    label('loc_E1FB')

    ChrTalk(
        0x000B,
        (
            '#2870441921V诸位游击士……\n',
            '今天真抱歉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2870441922V一个很过分的不小心\n',
            '给你们添了这么多麻烦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010441923V#1000F哪里的话，不用介意啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441924V这也是我们的工作啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_E2EB',
    )

    ChrTalk(
        0x0015,
        (
            '#0050441925V#050F那我们就先走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0014, 0x0015, 400)

    Jump('loc_E322')

    def _loc_E2EB(): pass

    label('loc_E2EB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_E322',
    )

    ChrTalk(
        0x0016,
        (
            '#0030441926V#020F那我们就先告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0014, 0x0016, 400)

    def _loc_E322(): pass

    label('loc_E322')

    ChrSetDirection(0x000F, 180, 400)

    ChrTalk(
        0x000F,
        (
            '#2810441927V真的……\n',
            '实在是感激不尽。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2870441928V真的很抱歉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#1790441929V那么，工作要加油啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021E, 4, 0x10F4))
    NewScene('ED6_DT21/T2100._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x001A offset: 0xE3B0
@scena.Code('func_1A_E3B0')
def func_1A_E3B0():
    ChrTurnDirectionByPos(0x00FE, -1140, 84170, 400)

    Return()

# id: 0x001B offset: 0xE3BE
@scena.Code('func_1B_E3BE')
def func_1B_E3BE():
    ChrSetPos(0x00FE, 5750, 2250, 380, 262)
    ChrWalkTo(0x00FE, 710, 0, 350, 1500, 0x00)
    ChrTurnDirection(0x00FE, 0x0101, 400)

    Return()

# id: 0x001C offset: 0xE3EB
@scena.Code('func_1C_E3EB')
def func_1C_E3EB():
    ChrSetPos(0x00FE, 6330, 2250, -170, 281)
    ChrWalkTo(0x00FE, 1410, 0, -190, 1500, 0x00)
    ChrTurnDirection(0x00FE, 0x0101, 400)

    Return()

# id: 0x001D offset: 0xE418
@scena.Code('func_1D_E418')
def func_1D_E418():
    ChrWalkTo(0x00FE, -690, 0, 350, 2000, 0x00)
    ChrWalkTo(0x00FE, -2800, 0, 3180, 2000, 0x00)
    ChrWalkTo(0x00FE, -3320, 0, 9510, 2000, 0x00)

    Return()

# id: 0x001E offset: 0xE455
@scena.Code('func_1E_E455')
def func_1E_E455():
    ChrWalkTo(0x00FE, -310, 0, -190, 2000, 0x00)
    ChrWalkTo(0x00FE, -2390, 0, 2660, 2000, 0x00)
    ChrWalkTo(0x00FE, -2620, 0, 8220, 2000, 0x00)

    Return()

# id: 0x001F offset: 0xE492
@scena.Code('func_1F_E492')
def func_1F_E492():
    ChrMoveToRelative(0x00FE, -4000, 0, 0, 1000, 0x00)

    Return()

# id: 0x0020 offset: 0xE4A7
@scena.Code('func_20_E4A7')
def func_20_E4A7():
    ChrMoveToRelative(0x00FE, -4000, 0, 0, 1000, 0x00)

    Return()

# id: 0x0021 offset: 0xE4BC
@scena.Code('func_21_E4BC')
def func_21_E4BC():
    ChrMoveToRelative(0x00FE, -4000, 0, 0, 1000, 0x00)

    Return()

# id: 0x0022 offset: 0xE4D1
@scena.Code('func_22_E4D1')
def func_22_E4D1():
    ChrMoveToRelative(0x00FE, -4000, 0, 0, 1000, 0x00)

    Return()

# id: 0x0023 offset: 0xE4E6
@scena.Code('func_23_E4E6')
def func_23_E4E6():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetPos(0x00FE, 500, 0, 76980, 255)

    @scena.Lambda('lambda_E508')
    def lambda_E508():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 0)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_E508)

    ChrWalkTo(0x00FE, -230, 0, 77000, 2000, 0x00)

    Return()

# id: 0x0024 offset: 0xE529
@scena.Code('func_24_E529')
def func_24_E529():
    Call(1, 0x0023)
    ChrWalkTo(0x00FE, -1430, 0, 77890, 2000, 0x00)
    ChrWalkTo(0x00FE, -1300, 0, 80130, 2000, 0x00)
    ChrTurnDirection(0x00FE, 0x000B, 400)

    Return()

# id: 0x0025 offset: 0xE55D
@scena.Code('func_25_E55D')
def func_25_E55D():
    Call(1, 0x0023)
    ChrWalkTo(0x00FE, -1000, 0, 77000, 2000, 0x00)
    ChrWalkTo(0x00FE, -3400, 0, 78780, 2000, 0x00)
    ChrTurnDirection(0x00FE, 0x000B, 400)

    Return()

# id: 0x0026 offset: 0xE591
@scena.Code('func_26_E591')
def func_26_E591():
    Call(1, 0x0023)
    ChrWalkTo(0x00FE, -1000, 0, 77000, 2000, 0x00)
    ChrWalkTo(0x00FE, -2400, 0, 78580, 2000, 0x00)
    ChrTurnDirection(0x00FE, 0x000B, 400)

    Return()

# id: 0x0027 offset: 0xE5C5
@scena.Code('func_27_E5C5')
def func_27_E5C5():
    Call(1, 0x0023)
    ChrWalkTo(0x00FE, -1000, 0, 77000, 2000, 0x00)
    ChrWalkTo(0x00FE, -3150, 0, 77370, 2000, 0x00)
    ChrTurnDirection(0x00FE, 0x000B, 400)

    Return()

# id: 0x0028 offset: 0xE5F9
@scena.Code('func_28_E5F9')
def func_28_E5F9():
    Call(1, 0x0023)
    ChrSetDirection(0x00FE, 90, 400)
    OP_72(0x0006, 0x0800)
    OP_70(0x0006, 0)
    PlaySE(7, 0x00, 0x64)
    OP_73(0x0006)
    OP_71(0x0006, 0x0800)
    Sleep(200)

    ChrWalkTo(0x00FE, -1000, 0, 77000, 2000, 0x00)
    ChrWalkTo(0x00FE, -2150, 0, 77170, 2000, 0x00)
    ChrTurnDirection(0x00FE, 0x000B, 400)

    Return()

# id: 0x0029 offset: 0xE652
@scena.Code('func_29_E652')
def func_29_E652():
    ChrTurnDirection(0x00FE, 0x0018, 400)

    Return()

# id: 0x002A offset: 0xE65A
@scena.Code('func_2A_E65A')
def func_2A_E65A():
    ChrTurnDirection(0x00FE, 0x0018, 400)

    Return()

# id: 0x002B offset: 0xE662
@scena.Code('func_2B_E662')
def func_2B_E662():
    ChrSetDirection(0x0104, 180, 400)
    ChrSetChipByIndex(0x0104, 10)
    ChrSetFlags(0x0104, 0x0002)
    OP_99(0x0104, 0x00, 0x03, 1200)
    Sleep(200)

    OP_99(0x0104, 0x03, 0x0A, 1200)

    Return()

# id: 0x002C offset: 0xE68B
@scena.Code('func_2C_E68B')
def func_2C_E68B():
    CameraMove(130, 0, 4860, 1000)
    CameraMove(-170, 0, 2320, 2000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
