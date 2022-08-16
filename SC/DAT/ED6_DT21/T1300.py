import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T1300_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T1300   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'T1300.x'
    header.mapIndex       = 1
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
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
        ('ED6_DT07/CH01300._CH', 'ED6_DT07/CH01300P._CP'),
    ]

# id: 0x10001 offset: 0xBA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '士兵卡多尔斯',
            x                   = -47800,
            z                   = -50,
            y                   = 11380,
            direction           = 0,
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
            name                = '士兵阿萨',
            x                   = -47800,
            z                   = -50,
            y                   = -8500,
            direction           = 180,
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
            name                = '玛诺利亚海岸方向',
            x                   = -50220,
            z                   = -500,
            y                   = -35780,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x00FF,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '西柏斯街道方向',
            x                   = -40370,
            z                   = -500,
            y                   = 36990,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x00FF,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x13A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x13A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x13A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -51690,
            triggerZ            = -470,
            triggerY            = 23510,
            triggerRange        = 1500,
            actorX              = -51690,
            actorZ              = 1800,
            actorY              = 23510,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -53780,
            triggerZ            = -510,
            triggerY            = -19530,
            triggerRange        = 1500,
            actorX              = -53780,
            actorZ              = 1900,
            actorY              = -19530,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -42460,
            triggerZ            = -50,
            triggerY            = -11830,
            triggerRange        = 1700,
            actorX              = -42460,
            actorZ              = 1200,
            actorY              = -11830,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x1A6
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1BE',
    )

    ChrSetPos(0x0009, -45660, -50, -12110, 90)

    def _loc_1BE(): pass

    label('loc_1BE')

    Return()

# id: 0x0001 offset: 0x1BF
@scena.Code('func_01_1BF')
def func_01_1BF():
    OP_16(0x02, 4000, -178000, -125000, 2293828)
    OP_B1('T1300_n')
    OP_71(0x0000, 0x0010)
    OP_1C(0x00, 0x00, 0x0008)
    OP_1C(0x01, 0x00, 0x0008)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_20D',
    )

    OP_72(0x0000, 0x0010)
    OP_6F(0x0000, 99)
    OP_72(0x0001, 0x0010)
    OP_6F(0x0001, 99)

    def _loc_20D(): pass

    label('loc_20D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_219',
    )

    OP_64(0x02, 0x0001)

    def _loc_219(): pass

    label('loc_219')

    Return()

# id: 0x0002 offset: 0x21A
@scena.Code('func_02_21A')
def func_02_21A():
    ExecExpressionWithReg(
        0x0001,
        (
            Expr.Rand,
            (Expr.PushLong, 0xE),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_23F',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_381')

    def _loc_23F(): pass

    label('loc_23F')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_258',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_381')

    def _loc_258(): pass

    label('loc_258')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_271',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_381')

    def _loc_271(): pass

    label('loc_271')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_28A',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_381')

    def _loc_28A(): pass

    label('loc_28A')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2A3',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_381')

    def _loc_2A3(): pass

    label('loc_2A3')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2BC',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_381')

    def _loc_2BC(): pass

    label('loc_2BC')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2D5',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_381')

    def _loc_2D5(): pass

    label('loc_2D5')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2EE',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_381')

    def _loc_2EE(): pass

    label('loc_2EE')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_307',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_381')

    def _loc_307(): pass

    label('loc_307')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_320',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_381')

    def _loc_320(): pass

    label('loc_320')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_339',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_381')

    def _loc_339(): pass

    label('loc_339')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_352',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_381')

    def _loc_352(): pass

    label('loc_352')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_36B',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_381')

    def _loc_36B(): pass

    label('loc_36B')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_381',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_381(): pass

    label('loc_381')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_396',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_381')

    def _loc_396(): pass

    label('loc_396')

    Return()

# id: 0x0003 offset: 0x397
@scena.Code('func_03_397')
def func_03_397():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_4B1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_442',
    )

    ChrTalk(
        0x00FE,
        (
            '就是在那个浮游物体出现后，\n',
            '导力停止现象马上就发生了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '刚发现照明灯熄灭，\n',
            '就看见湖面上出现了光亮。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '简直就像是日出时\n',
            '太阳一样的强光。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_4AE')

    def _loc_442(): pass

    label('loc_442')

    ChrTalk(
        0x00FE,
        (
            '就是在那个浮游物体出现后，\n',
            '导力停止现象马上就发生了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '刚发现照明灯熄灭，\n',
            '就看见湖面上出现了光亮。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4AE(): pass

    label('loc_4AE')

    Jump('loc_7D5')

    def _loc_4B1(): pass

    label('loc_4B1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_602',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_599',
    )

    ChrTalk(
        0x00FE,
        (
            '在这关所的卢安方向\n',
            '也能很清楚地看见那个浮游物体。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '阿萨那家伙\n',
            '竟然把警备工作扔下不管……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那东西、到底\n',
            '是什么呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '情报部的理查德上校\n',
            '如果在的话就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不管是什么疑问\n',
            '他也一定可以解答。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_5FF')

    def _loc_599(): pass

    label('loc_599')

    ChrTalk(
        0x00FE,
        (
            '有关那个浮游物体的原因，\n',
            '现在还是没有定论。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，这种时候，要是情报部的\n',
            '理查德上校在就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5FF(): pass

    label('loc_5FF')

    Jump('loc_7D5')

    def _loc_602(): pass

    label('loc_602')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_666',
    )

    ChrTalk(
        0x00FE,
        (
            '定期船恢复航行之后，\n',
            '超市也重新开始营业了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样一来，龙的事件\n',
            '总算是解决了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7D5')

    def _loc_666(): pass

    label('loc_666')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_6E4',
    )

    ChrTalk(
        0x00FE,
        (
            '因为发生了龙的事件，\n',
            '这里的关所也保持着警戒状态。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵、虽然应该不会再遭到袭击了，\n',
            '不过还是不能松懈大意啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7D5')

    def _loc_6E4(): pass

    label('loc_6E4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_7D5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_753',
    )

    ChrTalk(
        0x00FE,
        (
            '最近受通缉的魔兽相当多，\n',
            '使得街道也陷入一片混乱之中。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，在关所中\n',
            '稍微休息一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7D5')

    def _loc_753(): pass

    label('loc_753')

    ChrTalk(
        0x00FE,
        (
            '呀，步行到这里\n',
            '真是辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最近受通缉的魔兽相当多，\n',
            '使得街道也陷入一片混乱之中。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，在关所中\n',
            '稍微休息一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_7D5(): pass

    label('loc_7D5')

    TalkEnd(0x0008)

    Return()

# id: 0x0004 offset: 0x7D9
@scena.Code('func_04_7D9')
def func_04_7D9():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_8E5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_87C',
    )

    ChrTalk(
        0x00FE,
        (
            '现今的状况和湖上的浮游物体\n',
            '究竟有什么关系呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那种东西本来\n',
            '直接击落就好，不过…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '似乎不太可能啊。\n',
            '毕竟现在不能使用导力炮了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Jump('loc_8E2')

    def _loc_87C(): pass

    label('loc_87C')

    ChrTalk(
        0x00FE,
        (
            '那种高度的话，火炮也打不到。\n',
            '还有飞艇也不能用了…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总之，想把那东西击落\n',
            '根本就是不可能的嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8E2(): pass

    label('loc_8E2')

    Jump('loc_B91')

    def _loc_8E5(): pass

    label('loc_8E5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_9BC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_96F',
    )

    ChrTalk(
        0x00FE,
        (
            '在这里也能很清楚地\n',
            '看到那个浮游物体…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '怎么看也像是\n',
            '人工制造的建筑物啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就这么放着它不管\n',
            '也没关系吗…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Jump('loc_9B9')

    def _loc_96F(): pass

    label('loc_96F')

    ChrTalk(
        0x00FE,
        (
            '怎么看也像是\n',
            '人工制造的建筑物啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就这么放着它不管\n',
            '也没关系吗…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9B9(): pass

    label('loc_9B9')

    Jump('loc_B91')

    def _loc_9BC(): pass

    label('loc_9BC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_9F9',
    )

    ChrTalk(
        0x00FE,
        (
            '哟，辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '走这么远的路，\n',
            '一定累了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B91')

    def _loc_9F9(): pass

    label('loc_9F9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_AEA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_A63',
    )

    ChrTalk(
        0x00FE,
        (
            '情报部和空贼团都已经被捕了，\n',
            '警备总算是稍微轻松了一点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊，暂时还是很艰难啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_AE7')

    def _loc_A63(): pass

    label('loc_A63')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '因为定期船的原因，\n',
            '现在这里几乎没有人了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只是情报部的余党\n',
            '和空贼团的漏网之鱼还是行踪不明。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '暂时还是\n',
            '不能松懈啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_AE7(): pass

    label('loc_AE7')

    Jump('loc_B91')

    def _loc_AEA(): pass

    label('loc_AEA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_B91',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_B2C',
    )

    ChrTalk(
        0x00FE,
        (
            '附近还有很多凶猛的魔兽。\n',
            '请好好休息一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B91')

    def _loc_B2C(): pass

    label('loc_B2C')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '哎呀，旅行者真是少见，\n',
            '是步行来到这里的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '附近的魔兽可是很厉害啊。\n',
            '请好好休息一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B91(): pass

    label('loc_B91')

    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0xB95
@scena.Code('func_05_B95')
def func_05_B95():
    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_AD('ED6_DT24/C_VIS184._CH', 0x0000, 0x0000, 0x000001F4)
    Sleep(500)

    OP_56(0x03)
    OP_AE(0x000001F4)
    Sleep(500)

    SetScenaFlags(ScenaFlag(0x041D, 2, 0x20EA))
    TalkEnd(0x00FF)

    Return()

# id: 0x0006 offset: 0xBC3
@scena.Code('func_06_BC3')
def func_06_BC3():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '东北　柏斯市　　　４４１塞尔矩\n',
            '西南　卢安市　　　６６９塞尔矩\n',
            '　　　玛诺利亚村　３５７塞尔矩',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0007 offset: 0xC52
@scena.Code('func_07_C52')
def func_07_C52():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '西南　卢安市　　　６６９塞尔矩\n',
            '　　　玛诺利亚村　３５７塞尔矩\n',
            '东北　柏斯市　　　４４１塞尔矩',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0008 offset: 0xCE1
@scena.Code('func_08_CE1')
def func_08_CE1():
    TalkBegin(0x00FF)
    Sleep(400)

    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
