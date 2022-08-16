import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import E0011_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('E0011_1 ._SN')

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
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/E0011_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
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
            (Expr.TestScenaFlags, ScenaFlag(0x0300, 7, 0x1807)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_83B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_C1',
    )

    Call(0, 0x0039)

    def _loc_C1(): pass

    label('loc_C1')

    EventBegin(0x00)
    Fade(1000)
    CameraMove(116310, 0, 3680, 0)
    OP_67(0, 6750, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 115700, 0, 3700, 90)
    ChrSetSubChip(0x0008, 1)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0050280393V#052F艾丝蒂尔……怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_2C7',
    )

    ChrTalk(
        0x0101,
        (
            '#0010280394V#1016F#6P啊，没什么。\n',
            '跟平常一样在船内散步。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0050280395V#051F是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050280396V嘿，你每次都是这样，\n',
            '永远都逛不够啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280397V#1019F#6P这有什么关系。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280398V距离抵达柏斯\n',
            '还有不少时间呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0050280399V#051F也对，足够用来\n',
            '睡一觉了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050280400V#552F不过，接下来是柏斯啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050280401V继卢安、蔡斯和王都之后\n',
            '又会发生什么事呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_537')

    def _loc_2C7(): pass

    label('loc_2C7')

    ChrTalk(
        0x0101,
        (
            '#0010280402V#1016F#6P啊，没什么。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280403V一搭上飞船\n',
            '就想在船内散步了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280404V光是坐在座位上\n',
            '总感觉平静不下来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0050280405V#051F哈哈，还真是像你呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050280406V#556F不过……\n',
            '……真辛苦你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280407V#1004F#6P咦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0050280408V#051F就是关于到目前为止\n',
            '『结社』所引发的事件。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050280409V让你接连不断地跑遍\n',
            '卢安、蔡斯和王都不是吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280410V#1025F#6P啊，嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280411V阿加特你们才是，\n',
            '为了调查情报部的余党\n',
            '而奔走各地吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280412V辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0050280413V#051F还好，我们只是\n',
            '跑跑腿而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050280400V#552F不过，接下来是柏斯啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050280415V不知道又会发生什么事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_537(): pass

    label('loc_537')

    ChrTalk(
        0x0101,
        (
            '#0010280416V#1015F#6P嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280417V最好不要发生什么事，\n',
            '不过这似乎不大可能……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0050280418V#053F嗯嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050280419V#050F总之到了柏斯之后\n',
            '就开始调查空贼吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280420V#1020F#6P咦……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0050280421V#052F……你在惊讶什么？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050280422V也不能排除他们是\n',
            '结社爪牙的可能性吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050280423V这可是你说的哦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280424V#1008F#6P啊，嗯，是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280425V#1013F但、但是我仔细想过后\n',
            '又觉得那种可能性看来很低。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0050280426V#050F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280427V#1016F#6P那、那个，因为我\n',
            '和他们交手好几次了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280428V感觉他们不像是结社爪牙\n',
            '那样的坏人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0050280429V#053F……反正也没关系。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050280430V#051F详细情况等到了柏斯\n',
            '就能从卢格兰老爷子那里得知了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280431V#1007F#6P嗯……说得也是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0300, 7, 0x1807))
    ChrSetSubChip(0x0008, 0)
    EventEnd(0x00)
    MapSetFlags(0x02000000)

    Jump('loc_9AB')

    def _loc_83B(): pass

    label('loc_83B')

    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.GetChrWork, 0x8, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0008,
        0x05,
        (
            (Expr.GetChrWork, 0x8, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TalkBegin(0x0008)
    ChrClearFlags(0x0008, 0x0010)
    ChrTurnDirection(0x0008, 0x0000, 0)

    ExecExpressionWithValue(
        0x0008,
        0x04,
        (
            (Expr.GetChrWork, 0x8, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.PushLong, 0x168),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0008,
        0x04,
        (
            (Expr.GetChrWork, 0x8, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.GetChrWork, 0x8, 0x5),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0008,
        0x05,
        (
            (Expr.GetChrWork, 0x8, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0x8, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Leq,
            (Expr.GetChrWork, 0x8, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Geq,
            (Expr.GetChrWork, 0x8, 0x4),
            (Expr.PushLong, 0x195),
            Expr.Leq,
            Expr.Nez64,
            Expr.Or,
            (Expr.GetChrWork, 0x8, 0x4),
            (Expr.PushLong, 0x2A3),
            Expr.Geq,
            Expr.Or,
            Expr.Return,
        ),
        'loc_8CB',
    )

    Jump('loc_90D')

    def _loc_8CB(): pass

    label('loc_8CB')

    If(
        (
            (Expr.GetChrWork, 0x8, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_8E7',
    )

    ExecExpressionWithValue(
        0x0008,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_90D')

    def _loc_8E7(): pass

    label('loc_8E7')

    If(
        (
            (Expr.GetChrWork, 0x8, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_903',
    )

    ExecExpressionWithValue(
        0x0008,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_90D')

    def _loc_903(): pass

    label('loc_903')

    ExecExpressionWithValue(
        0x0008,
        0x08,
        (
            (Expr.GetChrWork, 0x8, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_90D(): pass

    label('loc_90D')

    ExecExpressionWithValue(
        0x0008,
        0x04,
        (
            (Expr.GetChrWork, 0x0, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0008,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetFlags(0x0008, 0x0010)

    ChrTalk(
        0x0008,
        (
            '#0050280432V#053F空贼艇的抢夺事件吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050280430V#051F详细情况等到了柏斯\n',
            '就能从卢格兰老爷子那里得知了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0008, 0)
    TalkEnd(0x0008)
    def _loc_9AB(): pass

    label('loc_9AB')

    Return()

# id: 0x0001 offset: 0x9AC
@scena.Code('func_01_9AC')
def func_01_9AC():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 0, 0x1808)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_EED',
    )

    EventBegin(0x00)
    Fade(1000)
    CameraMove(117000, 0, -150, 0)
    OP_67(0, 6750, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetSubChip(0x000C, 1)
    ChrSetPos(0x0101, 116240, 0, -160, 90)
    OP_0D()

    ChrTalk(
        0x000C,
        (
            '#0080280434V#073F哟，艾丝蒂尔。\n',
            '你去了哪里？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280435V#1025F#6P啊，嗯……\n',
            '稍微去吹了吹风。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0080280436V#070F这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080280437V说起来下一站\n',
            '好像是个叫洛连特的城市……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080280438V我记得你家\n',
            '就在那边吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200104V#1011F#6P啊，嗯。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280440V准确地说，不是在城里，\n',
            '而是在郊外。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280441V似乎是老爸坚持要这样的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0080280442V#073F哦，原来如此。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080280443V#071F不过大人建的房子\n',
            '一定很漂亮吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280444V#1008F#6P唔……怎么说呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280445V先不管是不是漂亮，\n',
            '总之住起来很舒适。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280446V充满了我和爸爸妈妈……\n',
            '还有约修亚的回忆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0080280447V#572F……是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280448V#1016F#6P别、别这样，金先生。\n',
            '不要一副那种表情嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280449V#1017F如果真的到了洛连特，\n',
            '是应该招待一下金先生的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280450V不过还是下次吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0080280451V#070F啊啊，说得也是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080280452V……对了，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080280453V到了柏斯以后\n',
            '陪我练习练习吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280454V#1004F#6P啊……\n',
            '怎么突然这么说呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0080280455V#075F在王都睡得太久，\n',
            '没能好好地运动一下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080280456V我想活动活动僵化的身体。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280457V#1016F#6P哈哈，是吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280458V#1006F唔～不知道我够不够格\n',
            '当金先生的练习对手……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280459V不过我还是很乐意奉陪的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0080280460V#071F好，拜托你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0301, 0, 0x1808))
    ChrSetSubChip(0x000C, 0)
    EventEnd(0x00)
    MapSetFlags(0x02000000)

    Jump('loc_1040')

    def _loc_EED(): pass

    label('loc_EED')

    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.GetChrWork, 0xC, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000C,
        0x05,
        (
            (Expr.GetChrWork, 0xC, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TalkBegin(0x000C)
    ChrClearFlags(0x000C, 0x0010)
    ChrTurnDirection(0x000C, 0x0000, 0)

    ExecExpressionWithValue(
        0x000C,
        0x04,
        (
            (Expr.GetChrWork, 0xC, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.PushLong, 0x168),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000C,
        0x04,
        (
            (Expr.GetChrWork, 0xC, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.GetChrWork, 0xC, 0x5),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000C,
        0x05,
        (
            (Expr.GetChrWork, 0xC, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0xC, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Leq,
            (Expr.GetChrWork, 0xC, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Geq,
            (Expr.GetChrWork, 0xC, 0x4),
            (Expr.PushLong, 0x195),
            Expr.Leq,
            Expr.Nez64,
            Expr.Or,
            (Expr.GetChrWork, 0xC, 0x4),
            (Expr.PushLong, 0x2A3),
            Expr.Geq,
            Expr.Or,
            Expr.Return,
        ),
        'loc_F7D',
    )

    Jump('loc_FBF')

    def _loc_F7D(): pass

    label('loc_F7D')

    If(
        (
            (Expr.GetChrWork, 0xC, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_F99',
    )

    ExecExpressionWithValue(
        0x000C,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_FBF')

    def _loc_F99(): pass

    label('loc_F99')

    If(
        (
            (Expr.GetChrWork, 0xC, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_FB5',
    )

    ExecExpressionWithValue(
        0x000C,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_FBF')

    def _loc_FB5(): pass

    label('loc_FB5')

    ExecExpressionWithValue(
        0x000C,
        0x08,
        (
            (Expr.GetChrWork, 0xC, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_FBF(): pass

    label('loc_FBF')

    ExecExpressionWithValue(
        0x000C,
        0x04,
        (
            (Expr.GetChrWork, 0x0, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000C,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetFlags(0x000C, 0x0010)

    ChrTalk(
        0x000C,
        (
            '#0080280461V#070F那么……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080280462V也没有什么可做的事，\n',
            '我就先睡一会儿吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x000C, 0)
    TalkEnd(0x000C)

    def _loc_1040(): pass

    label('loc_1040')

    Return()

# id: 0x0002 offset: 0x1041
@scena.Code('func_02_1041')
def func_02_1041():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 1, 0x1809)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1E2B',
    )

    EventBegin(0x00)
    TerminateThread(0x000D, 0x00)
    Fade(1000)
    CameraMove(89340, -1000, 53720, 0)
    OP_67(0, 7240, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(33000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 89280, -1000, 52860, 270)
    ChrTurnDirection(0x000D, 0x0101, 0)
    ChrSetSubChip(0x000D, 0)
    OP_0D()

    ChrTalk(
        0x000D,
        (
            '#0060280463V#040F#6P艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280464V#1011F#2P科洛丝。\n',
            '你在这里啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0060280465V#041F#6P嗯……\n',
            '因为这里的景色很好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060280466V#542F艾丝蒂尔看起来\n',
            '又是在散步吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280467V#1016F#2P啊、嗯，随便走走。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211040V#1025F……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0060280469V#040F#6P……………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060280470V#047F……约修亚，\n',
            '他现在怎么样了呢？',
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
            '#0010280471V#1020F#2P咦咦！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280472V你、你、你怎么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0060280473V#048F#6P嘻……果然。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060280474V奈尔先生他们\n',
            '是跟你说有关他的事情吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280475V#1004F#2P……………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280476V#1019F……你，是在套我的话？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0060280477V#045F#6P呵呵……\n',
            '我可是女王候补哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060280478V多少得会施展\n',
            '一点小策略。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280479V#1007F#2P唉～败给你了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280480V#1025F嗯……\n',
            '确实是有关约修亚的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0060280481V#047F#6P……约修亚他没事，\n',
            '而且还在利贝尔国内。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060280482V不过有些事情\n',
            '却使你高兴不起来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060280483V#040F是这么回事吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1500)

    ChrTalk(
        0x000D,
        (
            '#0060280484V#542F#6P那个，我猜对了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280485V#1007F#2P科洛丝……\n',
            '你的洞察力太强了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280486V#1006F我觉得你一定能成为\n',
            '一位了不起的女王。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0060280487V#045F#6P呵呵，承蒙夸奖。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060280488V#048F……不过，太好了。\n',
            '约修亚他没事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060280489V光是知道了这点就令人高兴。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280490V#1025F#2P嗯……\n',
            '我也对此感到高兴……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280491V#1003F……………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0060280492V#044F#6P艾丝蒂尔？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280493V#1003F#2P逮捕戴尔蒙市长时……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280494V被市长用枪威胁的时候，\n',
            '约修亚的态度你还记得吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0060280495V#042F#6P……是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280496V#1026F#2P如果我说约修亚现在的\n',
            '眼神也和那时一样……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280497V科洛丝，你会怎样想？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0060280498V#043F#6P啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060280499V#049F……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280500V#1007F#2P对不起，科洛丝。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280501V我明明没跟你坦诚相对，\n',
            '却还要对你说这些故弄玄虚的话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0060280502V#047F#6P不……没关系。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060280503V#040F艾丝蒂尔的烦恼，\n',
            '我感觉能理解一些。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280504V#1025F#2P是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280505V#1015F…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280506V#1007F另、另外……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0060280507V#044F#6P嗯？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280508V#1013F#2P可、可能有点\n',
            '小题大做了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280509V我这么担心着他，\n',
            '他却还跟女孩子在一起，你怎么想？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0060280510V#044F#6P………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060280511V#042F……那女孩子多大了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280512V#1007F#2P和我们差不多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0060280513V#043F#6P…………………………………\n',
            '…………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060280514V#047F好像会涌现出一种\n',
            '无法接受的心情呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280515V#1005F#2P对、对吧！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280516V果然是无法接受吧！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0060280517V#042F#6P嗯，当然了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060280518V#047F约修亚也是的……\n',
            '到底在干些什么。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280519V#1019F#2P真是的……\n',
            '找到他以后一定要质问他一天一夜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000D, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x0101, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1000)

    OP_63(0x0101)
    OP_63(0x000D)
    Sleep(500)

    ChrTalk(
        0x000D,
        (
            '#045F#6P#1K呵呵……',
            TxtCtl.Enter,
        ),
    )

    ChrTalk(
        0x0101,
        (
            '#0010211110V#1016F#2P#1K呵呵……',
            TxtCtl.Enter,
        ),
    )

    OP_56(0x01)
    OP_59()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010280522V#1008F#2P谢谢你，科洛丝。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280523V我感觉心情\n',
            '好一点点了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0060280524V#048F#6P呵呵，不用客气。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060280525V能帮上你我就很高兴了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280526V#1017F#2P等我整理好心情\n',
            '就会和大家说这件事的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280527V你能等到那时候吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0060280528V#041F#6P嗯，当然。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060280529V#040F……那么我就\n',
            '先回座位了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280530V#1006F#2P嗯，回头见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000D, 270, 400)

    @scena.Lambda('lambda_1D36')
    def lambda_1D36():
        ChrTurnDirection(0x00FE, 0x000D, 400)
        Yield()

        Jump('lambda_1D36')

    DispatchAsync2(0x0101, 0x0002, lambda_1D36)

    ChrSetFlags(0x000D, 0x0004)
    ChrClearFlags(0x000D, 0x0020)
    ChrWalkTo(0x000D, 86730, -1000, 52850, 2500, 0x00)

    @scena.Lambda('lambda_1D65')
    def lambda_1D65():
        CameraMove(88830, -1000, 50980, 2500)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_1D65)

    ChrWalkTo(0x000D, 86810, -1000, 49570, 2500, 0x00)
    ChrClearFlags(0x000D, 0x0004)
    ChrWalkTo(0x000D, 87670, 100, 43990, 2500, 0x00)

    @scena.Lambda('lambda_1DAA')
    def lambda_1DAA():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0002, lambda_1DAA)

    ChrWalkTo(0x000D, 87900, 100, 43000, 2500, 0x00)
    ChrSetFlags(0x000D, 0x0080)
    TerminateThread(0x0101, 0x02)
    Sleep(500)

    Fade(1000)
    CameraMove(89280, -1000, 52860, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x0301, 1, 0x1809))
    ClearScenaFlags(ScenaFlag(0x0001, 0, 0x8))
    EventEnd(0x00)
    MapSetFlags(0x02000000)

    Jump('loc_1FA2')

    def _loc_1E2B(): pass

    label('loc_1E2B')

    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.GetChrWork, 0xD, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000D,
        0x05,
        (
            (Expr.GetChrWork, 0xD, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TalkBegin(0x000D)
    ChrClearFlags(0x000D, 0x0010)
    ChrTurnDirection(0x000D, 0x0000, 0)

    ExecExpressionWithValue(
        0x000D,
        0x04,
        (
            (Expr.GetChrWork, 0xD, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.PushLong, 0x168),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000D,
        0x04,
        (
            (Expr.GetChrWork, 0xD, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.GetChrWork, 0xD, 0x5),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000D,
        0x05,
        (
            (Expr.GetChrWork, 0xD, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0xD, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Leq,
            (Expr.GetChrWork, 0xD, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Geq,
            (Expr.GetChrWork, 0xD, 0x4),
            (Expr.PushLong, 0x195),
            Expr.Leq,
            Expr.Nez64,
            Expr.Or,
            (Expr.GetChrWork, 0xD, 0x4),
            (Expr.PushLong, 0x2A3),
            Expr.Geq,
            Expr.Or,
            Expr.Return,
        ),
        'loc_1EBB',
    )

    Jump('loc_1EFD')

    def _loc_1EBB(): pass

    label('loc_1EBB')

    If(
        (
            (Expr.GetChrWork, 0xD, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_1ED7',
    )

    ExecExpressionWithValue(
        0x000D,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1EFD')

    def _loc_1ED7(): pass

    label('loc_1ED7')

    If(
        (
            (Expr.GetChrWork, 0xD, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_1EF3',
    )

    ExecExpressionWithValue(
        0x000D,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1EFD')

    def _loc_1EF3(): pass

    label('loc_1EF3')

    ExecExpressionWithValue(
        0x000D,
        0x08,
        (
            (Expr.GetChrWork, 0xD, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1EFD(): pass

    label('loc_1EFD')

    ExecExpressionWithValue(
        0x000D,
        0x04,
        (
            (Expr.GetChrWork, 0x0, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000D,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetFlags(0x000D, 0x0010)

    ChrTalk(
        0x000D,
        (
            '#0060280531V#040F参加互不侵犯条约签字仪式的\n',
            '外国来宾就快要到达\n',
            '格兰赛尔了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060280532V要是能顺利\n',
            '结束就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x000D, 0)
    TalkEnd(0x000D)

    def _loc_1FA2(): pass

    label('loc_1FA2')

    Return()

# id: 0x0003 offset: 0x1FA3
@scena.Code('func_03_1FA3')
def func_03_1FA3():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 2, 0x180A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_29D7',
    )

    EventBegin(0x00)
    OP_4A(0x000B, 255)
    Fade(1000)
    CameraMove(58860, 0, -1390, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 58800, 0, -870, 180)
    OP_0D()

    ChrTalk(
        0x000B,
        (
            '#0070280533V#063F#6P…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280534V#1004F#5P提妲。\n',
            '你在这里做什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000B, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x000B, 0x0101, 400)

    ChrTalk(
        0x000B,
        (
            '#0070280535V#065F#8P啊……\n',
            '艾丝蒂尔姐姐。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070280536V#561F那个，我稍微\n',
            '在想一些心事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280537V#1015F#5P心事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0070280538V#561F#8P嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070280539V#063F……我说，姐姐。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070280540V我这个人毕竟还是\n',
            '靠不住的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200137V#1004F#5P咦……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0070280542V#062F#8P姐姐你\n',
            '看起来好像有烦恼……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070280543V在这件事情上，\n',
            '我是不是帮不了你呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280544V#1003F#5P啊，这……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280545V#1007F真是失败啊。\n',
            '连提妲都看出来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0070280546V#065F#8P果然是这样……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070280547V#562F任性地跟着大家来到这里，\n',
            '可我却什么忙也帮不上……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070280548V……也没能\n',
            '挽留住玲……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070280549V我……\n',
            '果然是个累赘。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280550V#1025F#5P提妲……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280551V#1016F傻孩子，\n',
            '你很在意这些吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0070280552V#065F#8P可、可是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280553V#1025F#5P我……\n',
            '与其说是在愤怒\n',
            '倒不如说是稍微有点混乱。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280554V光是依靠别人的话，\n',
            '什么问题也解决不了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280555V所以我现在只想……\n',
            '一个人稍微考虑考虑。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0070280556V#063F#8P姐姐………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070280557V现在有什么\n',
            '我能帮上姐姐的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280558V#1006F#5P当然有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x000B, 0x0040)
    ChrWalkTo(0x0101, 58750, 0, -1600, 1000, 0x00)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x000B, 0x0002)
    ChrSetChipByIndex(0x000B, 43)
    ChrSetSubChip(0x000B, 0)
    OP_99(0x000B, 0x00, 0x02, 1000)
    Sleep(500)

    ChrTalk(
        0x000B,
        (
            '#0070280559V#064F#8P咦？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070280560V#065F啊，姐姐！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280561V#1001F#5P嗯～这样果然最让人安心～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280562V温暖又光滑，\n',
            '这种拥抱的感觉真是绝妙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0070280563V#067F#8P啊……\n',
            '艾丝蒂尔姐姐真是的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280564V#1017F#5P我……\n',
            '能有提妲在身边真是太好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280565V当然，对机械非常了解啦、\n',
            '能解决专业问题这些都包括在内……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280566V不过只要看到提妲你的笑容，\n',
            '就能让人打起精神来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0070280567V#064F#8P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280568V#1006F#5P就算是玲，和你在一起时\n',
            '不是也玩得很开心吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280569V虽然那也有可能\n',
            '只是用来欺骗我们的演技……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280570V但是，我不觉得\n',
            '一切都是谎言。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280571V我想那孩子也一定体会到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0070280572V#560F#8P是、是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070280573V#061F如果是这样……我也感到很开心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280574V#1006F#5P呵呵。\n',
            '你终于笑了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280575V嗯嗯。\n',
            '提妲果然还是笑起来最可爱！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280576V#1001F虽然偶尔出现快哭出来的\n',
            '表情也算得上是很可爱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0070280577V#067F#8P真、真是的。\n',
            '姐姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x0101, 0x0080)
    ChrClearFlags(0x000B, 0x0002)
    ChrSetChipByIndex(0x000B, 5)
    ChrSetSubChip(0x000B, 0)
    ChrMoveTo(0x0101, 58750, 0, -1000, 800, 0x00)
    Sleep(500)

    ChrTalk(
        0x000B,
        (
            '#0070280578V#560F#8P谢谢姐姐。\n',
            '谢谢你能这么说……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070280579V我该回座位了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280580V#1006F#5P嗯，一会儿见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000B, 270, 400)

    @scena.Lambda('lambda_2947')
    def lambda_2947():
        ChrTurnDirection(0x00FE, 0x000B, 400)
        Yield()

        Jump('lambda_2947')

    DispatchAsync2(0x0101, 0x0001, lambda_2947)

    ChrWalkTo(0x000B, 57820, 0, -2070, 2500, 0x00)

    @scena.Lambda('lambda_296C')
    def lambda_296C():
        CameraMove(59600, 0, 2700, 3000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_296C)

    ChrWalkTo(0x000B, 57790, 0, 2230, 2500, 0x00)
    ChrWalkTo(0x000B, 60890, 0, 4860, 2500, 0x00)
    ChrWalkTo(0x000B, 61070, 2800, 8189, 2500, 0x00)
    ChrSetFlags(0x000B, 0x0080)
    TerminateThread(0x0101, 0x01)
    OP_69(0x0101, 1600)
    SetScenaFlags(ScenaFlag(0x0301, 2, 0x180A))
    EventEnd(0x00)
    MapSetFlags(0x02000000)

    Jump('loc_2B42')

    def _loc_29D7(): pass

    label('loc_29D7')

    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.GetChrWork, 0xB, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000B,
        0x05,
        (
            (Expr.GetChrWork, 0xB, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TalkBegin(0x000B)
    ChrClearFlags(0x000B, 0x0010)
    ChrTurnDirection(0x000B, 0x0000, 0)

    ExecExpressionWithValue(
        0x000B,
        0x04,
        (
            (Expr.GetChrWork, 0xB, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.PushLong, 0x168),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000B,
        0x04,
        (
            (Expr.GetChrWork, 0xB, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.GetChrWork, 0xB, 0x5),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000B,
        0x05,
        (
            (Expr.GetChrWork, 0xB, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0xB, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Leq,
            (Expr.GetChrWork, 0xB, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Geq,
            (Expr.GetChrWork, 0xB, 0x4),
            (Expr.PushLong, 0x195),
            Expr.Leq,
            Expr.Nez64,
            Expr.Or,
            (Expr.GetChrWork, 0xB, 0x4),
            (Expr.PushLong, 0x2A3),
            Expr.Geq,
            Expr.Or,
            Expr.Return,
        ),
        'loc_2A67',
    )

    Jump('loc_2AA9')

    def _loc_2A67(): pass

    label('loc_2A67')

    If(
        (
            (Expr.GetChrWork, 0xB, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_2A83',
    )

    ExecExpressionWithValue(
        0x000B,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2AA9')

    def _loc_2A83(): pass

    label('loc_2A83')

    If(
        (
            (Expr.GetChrWork, 0xB, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_2A9F',
    )

    ExecExpressionWithValue(
        0x000B,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2AA9')

    def _loc_2A9F(): pass

    label('loc_2A9F')

    ExecExpressionWithValue(
        0x000B,
        0x08,
        (
            (Expr.GetChrWork, 0xB, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2AA9(): pass

    label('loc_2AA9')

    ExecExpressionWithValue(
        0x000B,
        0x04,
        (
            (Expr.GetChrWork, 0x0, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000B,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetFlags(0x000B, 0x0010)

    ChrTalk(
        0x000B,
        (
            '#0070280581V#560F似乎很快就要到洛连特了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070280582V目的地柏斯就在它的下一站，\n',
            '所以还要花点时间吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x000B, 0)
    TalkEnd(0x000B)

    def _loc_2B42(): pass

    label('loc_2B42')

    Return()

# id: 0x0004 offset: 0x2B43
@scena.Code('func_04_2B43')
def func_04_2B43():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 3, 0x180B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3E02',
    )

    EventBegin(0x00)
    FadeOut(0, 0, -1)
    TerminateThread(0x000A, 0x00)
    CameraMove(31780, 0, 6980, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x000A, 31650, 0, 6980, 274)
    ChrSetFlags(0x000A, 0x0002)
    ChrSetChipByIndex(0x000A, 10)
    ChrClearFlags(0x000A, 0x0080)
    Sleep(500)

    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x000A,
        (
            '#0040280583V#035F嗯……原来如此。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040280584V#030F那个，其实有几位记者\n',
            '来找艾丝蒂尔了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040280585V后来她就变得有些怪怪的，\n',
            '我还在想是什么事情呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040280586V#035F呼，疑问终于得到了解答。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040280587V…………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040280588V#030F嗯，这样就ＯＫ了。\n',
            '没必要向王国军汇报。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040280589V反正对有关他的事，\n',
            '王国军应该都有所预测了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040280587V…………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040280591V#031F哈哈哈。\n',
            '我的眼力还不错吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040280592V呵呵，其实本来是很含糊的推测，\n',
            '想不到居然误打误撞被我蒙对了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040280587V…………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040280594V#030F……知道了、知道了。\n',
            '别发出那么可怕的声音。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040280595V无论怎样，等你到了帝都后\n',
            '就请立即着手准备吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040280596V#032F啊……尽可能\n',
            '不要让那个人插手进来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040280597V#035F就拜托你了，我的好友。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    Fade(250)
    ChrSetSubChip(0x000A, 5)
    OP_0D()
    PlaySE(156, 0x00, 0x64)
    Sleep(500)

    Fade(500)
    ChrClearFlags(0x000A, 0x0020)
    ChrClearFlags(0x000A, 0x0002)
    ChrSetSubChip(0x000A, 0)
    ChrSetChipByIndex(0x000A, 4)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x000A,
        (
            '#0040280598V#035F呼，想不到能和穆拉\n',
            '打得不分伯仲……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040280599V不愧是\n',
            '前『结社』成员呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040280600V#032F不过如果我\n',
            '猜的没错的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x0101, 30720, 0, -1440, 0)
    ChrClearFlags(0x0101, 0x0080)

    ChrTalk(
        0x0101,
        (
            '#0010280601V#1P没猜错什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_2FF2')
    def lambda_2FF2():
        CameraMove(31560, 0, 6450, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2FF2)

    @scena.Lambda('lambda_300A')
    def lambda_300A():
        OP_67(0, 7310, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_300A)

    @scena.Lambda('lambda_3022')
    def lambda_3022():
        OP_6E(282, 3000)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_3022)

    @scena.Lambda('lambda_3032')
    def lambda_3032():
        OP_6C(21000, 3000)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_3032)

    ChrTurnDirection(0x000A, 0x0101, 400)
    ChrWalkTo(0x0101, 30280, 0, 2600, 2500, 0x00)
    ChrWalkTo(0x0101, 30720, 0, 4380, 2500, 0x00)
    ChrTurnDirection(0x0101, 0x000A, 400)
    Sleep(500)

    WaitForThreadExit(0x000A, 0x0002)

    ChrTalk(
        0x000A,
        (
            '#0040280602V#033F艾、艾丝蒂尔！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280603V#1006F搞什么啊，在这里\n',
            '偷偷摸摸地说悄悄话……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280604V#1004F咦，奇怪？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 270, 400)
    Sleep(500)

    ChrSetDirection(0x0101, 0, 400)
    ChrSetDirection(0x0101, 90, 400)
    Sleep(500)

    ChrTurnDirection(0x0101, 0x000A, 400)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010280605V#1015F奥利维尔你在和谁说话？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0040280606V#035F呵呵，你在说什么呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040280607V#030F难道我会和除了你之外的\n',
            '其它女性在这种地方幽会吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280608V#1019F真奇怪……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280609V我明明听见\n',
            '你和别人说话的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0040280610V#031F哈哈哈，真拿你没办法。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040280611V自言自语被你听见了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280612V#1004F自、自言自语？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0040280613V#035F要说是自言自语\n',
            '可能稍微有点不准确……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040280614V#030F我只是把以前我饰演主角的\n',
            '舞台剧的台词念了一下而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280615V#1020F舞台剧的台词……\n',
            '为、为什么要在这种地方？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0040280616V#034F目的地柏斯是离\n',
            '埃雷波尼亚最近的地方……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040280617V随着离那边距离的缩短，\n',
            '我不禁顿起思乡之情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040280618V往昔那伤心的回忆\n',
            '就不自觉地从口中流露出来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280619V#1026F原、原来是这样……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280620V#1019F──你以为我就那么容易相信？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0040280621V#033F唔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280622V#1007F不管怎么看，奥利维尔\n',
            '可疑的地方都很多。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280623V之前好像还和老爸\n',
            '偷偷摸摸地商谈着什么。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280624V#1009F你也该告诉我你\n',
            '真正的目的了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0040280625V#030F嗯～想不到会被你\n',
            '这样穷追猛打。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040280626V#031F你真是长大了，艾丝蒂尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280627V#1016F是大家把我锻炼成这样的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280628V#1002F那么──你是说还是不说？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0040280629V#035F呵呵，与其说这些，\n',
            '我还是先给你吃颗定心丸吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040280630V希望这样你能放过我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280631V#1004F咦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0040280632V#030F关于那艘空贼团的飞艇……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040280633V被劫走应该也不至于\n',
            '构成什么大问题才对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280634V#1020F咦咦！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0040280635V#030F之前我也说过吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040280636V#035F空贼团的成员\n',
            '原本是埃雷波尼亚贵族这一点，\n',
            '对帝国来说也不是件光彩的事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040280637V不过利贝尔为了\n',
            '顺利签订互不侵犯条约，\n',
            '也不想过于声张此事……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040280638V#030F从这一点上来说，空贼艇\n',
            '在现在遭劫正好可以\n',
            '消除一个不安定因素。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280639V#1015F原来是这么回事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0040280640V#035F当然，如果接下来空贼们不学乖，\n',
            '还要干抢劫这类勾当的话就另当别论了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040280641V不过似乎不用担心这点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280642V#1025F的、的确……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280643V(有约修亚在，\n',
            '也会阻止他们抢劫的……)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1200)

    OP_63(0x0101)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010280644V#1009F……你为什么知道\n',
            '空贼们不会去抢劫？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0040280645V#030F艾丝蒂尔你又为什么\n',
            '会说出『的确』二字呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280646V#1019F唔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0040280647V#031F呵呵，那么……\n',
            '我要回座位上去了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040280648V#030F艾丝蒂尔你要不要也一起？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280649V#1007F……我就算了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280650V#1015F我说，奥利维尔。\n',
            '我只问你一个问题可以吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0040280651V#030F什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280652V#1007F奥利维尔的事我有\n',
            '很多都不知道……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280653V#1002F即便如此我还是把你当作同伴，\n',
            '并且非常信赖你。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280654V无论发生什么，我都会自作主张地\n',
            '把你当成值得我信赖的人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280655V#1013F……我这么做会不会给你添麻烦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0040280656V#033F………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280657V#1019F怎、怎么了啊。\n',
            '眼睛睁得那么大。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0040280658V#033F没、没有……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040280659V#031F呵呵，怎么可能会\n',
            '给我添麻烦呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040280660V为了回报你的爱和信赖，\n',
            '从现在起我要更加努力了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280661V#1007F我可没给你什么爱……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280662V#1017F不过还是要谢谢你，奥利维尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0040280663V#031F呵呵，不用客气。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040280664V#030F那么我就先告退了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3D2E')
    def lambda_3D2E():
        CameraMove(30630, 0, 4390, 3500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3D2E)

    @scena.Lambda('lambda_3D46')
    def lambda_3D46():
        OP_6C(1000, 3500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_3D46)

    @scena.Lambda('lambda_3D56')
    def lambda_3D56():
        ChrTurnDirection(0x00FE, 0x000A, 400)
        Yield()

        Jump('lambda_3D56')

    DispatchAsync2(0x0101, 0x0001, lambda_3D56)

    ChrWalkTo(0x000A, 29710, 0, 4370, 2500, 0x00)
    ChrWalkTo(0x000A, 29590, 0, -3590, 2500, 0x00)
    WaitForThreadExit(0x0101, 0x0002)
    WaitForThreadExit(0x0101, 0x0003)
    ChrSetFlags(0x000A, 0x0080)
    TerminateThread(0x0101, 0x01)
    Sleep(500)

    Fade(1000)
    CameraMove(30430, 0, 5730, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 30430, 0, 5730, 180)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x0301, 3, 0x180B))
    EventEnd(0x00)
    MapSetFlags(0x02000000)

    Jump('loc_3F99')

    def _loc_3E02(): pass

    label('loc_3E02')

    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.GetChrWork, 0xA, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000A,
        0x05,
        (
            (Expr.GetChrWork, 0xA, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TalkBegin(0x000A)
    ChrClearFlags(0x000A, 0x0010)
    ChrTurnDirection(0x000A, 0x0000, 0)

    ExecExpressionWithValue(
        0x000A,
        0x04,
        (
            (Expr.GetChrWork, 0xA, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.PushLong, 0x168),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000A,
        0x04,
        (
            (Expr.GetChrWork, 0xA, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.GetChrWork, 0xA, 0x5),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000A,
        0x05,
        (
            (Expr.GetChrWork, 0xA, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0xA, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Leq,
            (Expr.GetChrWork, 0xA, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Geq,
            (Expr.GetChrWork, 0xA, 0x4),
            (Expr.PushLong, 0x195),
            Expr.Leq,
            Expr.Nez64,
            Expr.Or,
            (Expr.GetChrWork, 0xA, 0x4),
            (Expr.PushLong, 0x2A3),
            Expr.Geq,
            Expr.Or,
            Expr.Return,
        ),
        'loc_3E92',
    )

    Jump('loc_3ED4')

    def _loc_3E92(): pass

    label('loc_3E92')

    If(
        (
            (Expr.GetChrWork, 0xA, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_3EAE',
    )

    ExecExpressionWithValue(
        0x000A,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_3ED4')

    def _loc_3EAE(): pass

    label('loc_3EAE')

    If(
        (
            (Expr.GetChrWork, 0xA, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_3ECA',
    )

    ExecExpressionWithValue(
        0x000A,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_3ED4')

    def _loc_3ECA(): pass

    label('loc_3ECA')

    ExecExpressionWithValue(
        0x000A,
        0x08,
        (
            (Expr.GetChrWork, 0xA, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_3ED4(): pass

    label('loc_3ED4')

    ExecExpressionWithValue(
        0x000A,
        0x04,
        (
            (Expr.GetChrWork, 0x0, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000A,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetFlags(0x000A, 0x0010)

    ChrTalk(
        0x000A,
        (
            '#0040280665V#035F呼，下一站就是\n',
            '洛连特了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040280666V#030F虽然还想再品尝一次\n',
            '使用天然原料制作的乡土菜肴……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040280667V不过看来得等下次了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x000A, 0)
    TalkEnd(0x000A)

    def _loc_3F99(): pass

    label('loc_3F99')

    Return()

# id: 0x0005 offset: 0x3F9A
@scena.Code('func_05_3F9A')
def func_05_3F9A():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    CameraMove(113330, 200, 4290, 0)
    OP_67(0, 6870, -10000, 0)
    CameraSetDistance(2730, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0016, 60470, -2000, 52850, 0)
    ChrSetPos(0x0101, 113430, 0, 4430, 180)
    Sleep(500)

    FadeIn(1000, 0)
    OP_0D()
    PlaySE(166, 0x00, 0x64)
    Sleep(1000)

    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('女性的声音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0880200720V……久等了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_62(0x0032, 0x00000000, 1700, 0x26, 0x26, 0x000000FA, 0x01)
    OP_4A(0x0032, 255)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0880280669V本船即将\n',
            '抵达洛连特市。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    @scena.Lambda('lambda_409A')
    def lambda_409A():
        ChrSetDirection(0x0032, 0, 500)

        ExitThread()

    DispatchAsync(0x0032, 0x0001, lambda_409A)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0880200722V着陆时会有少许摇晃，\n',
            '请尽快回到座位。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(
        0x0101,
        (
            '#0010280671V#1004F#5P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_410B')
    def lambda_410B():
        CameraMove(115290, 0, 2910, 1200)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_410B)

    Sleep(500)

    ChrSetSubChip(0x0009, 1)
    WaitForThreadExit(0x0009, 0x0001)

    ChrTalk(
        0x0009,
        (
            '#0030280672V#020F#2P快点，艾丝蒂尔。\n',
            '赶紧坐下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030280673V站着很危险的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280674V#1025F#5P嗯，说得也是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0009, 1)

    @scena.Lambda('lambda_41B1')
    def lambda_41B1():
        CameraMove(116550, 0, 2320, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_41B1)

    ChrWalkTo(0x0101, 116580, 0, 1550, 2000, 0x00)
    ChrSetSubChip(0x0009, 0)
    ChrSetFlags(0x0101, 0x0004)
    ChrSetSubChip(0x0101, 0)
    ChrSetDirection(0x0101, 0, 400)
    Fade(500)
    ChrSetPos(0x0101, 116650, 100, 1200, 0)
    ChrSetChipByIndex(0x0101, 20)
    OP_0D()
    Sleep(1000)

    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('女性的声音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0880280675V承蒙各位今日搭乘飞船公社的航班，\n',
            '实在是感激不尽。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0880280676V请在洛连特下船的旅客\n',
            '检查是否有物品遗忘──。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_20(0x00000BB8)

    @scena.Lambda('lambda_42BD')
    def lambda_42BD():
        CameraMove(116960, 200, 5430, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_42BD)

    @scena.Lambda('lambda_42D5')
    def lambda_42D5():
        OP_67(0, 4780, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_42D5)

    WaitForThreadExit(0x0101, 0x0001)
    Sleep(500)

    Fade(1000)
    OP_72(0x0003, 0x0004)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010280677V#1004F#6P咦！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030280678V#023F#2P这是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    PlayBGM(81)
    Sleep(200)

    Fade(1000)
    CameraMove(59370, -450, 53240, 0)
    OP_67(0, 4630, -10000, 0)
    CameraSetDistance(2840, 0)
    OP_6C(35000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x001E,
        (
            '#3320280679V#5P这、这是什么！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001E,
        (
            '#3320280680V#5P为什么会在这种高度\n',
            '就进入云层之中！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0020,
        (
            '#3330280681V#5P不、不对……\n',
            '这不像是云……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001F,
        (
            '#3340280682V#5P塔台传来联络！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001F,
        (
            '#3340280683V#5P据说洛连特市一带\n',
            '突然起了浓雾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001E,
        (
            '#3320280684V#5P你说什么……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(500)

    ChrSetSubChip(0x0101, 2)
    ChrSetSubChip(0x0009, 2)
    ChrSetSubChip(0x0008, 2)
    ChrSetSubChip(0x000A, 2)
    ChrSetSubChip(0x000D, 2)
    ChrSetSubChip(0x000B, 2)
    ChrSetSubChip(0x000C, 2)
    ChrSetPos(0x0032, 116140, 0, 11120, 40)
    OP_4B(0x0032, 255)
    ChrSetPos(0x0031, 116790, 0, 10500, 40)
    ChrSetChipByIndex(0x0031, 46)
    CreateThread(0x0031, 0x00, 0x00, 0x0002)
    CameraMove(118000, 100, 8660, 0)
    OP_67(0, 4780, -10000, 0)
    CameraSetDistance(2730, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeIn(1000, 0)
    CameraMove(118000, 100, 3330, 3000)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010280685V#1020F#6P这、这是怎么回事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0070280686V#064F#6P哇……一片纯白啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0040280687V#030F#6P嗯……\n',
            '是不是进入了云层？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030280688V#022F#6P有可能……\n',
            '不过这高度也太低了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0080280689V#072F#6P飞船着陆时\n',
            '经常会遇到这种事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0050280690V#552F#6P不，我看很少。\n',
            '至少我从来没见过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0060280691V#043F#6P我也是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(166, 0x00, 0x64)
    Sleep(1000)

    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('女性的声音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0880280692V……各位旅客。\n',
            '请大家镇静。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0880280693V据控制塔发来的联络，\n',
            '目前得知在洛连特市一带\n',
            '起了浓雾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0880280694V现在，为保证着陆时的视野，\n',
            '飞船坪方面正在准备\n',
            '夜间的照明设备。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0880280695V现在请各位旅客耐心等待。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(
        0x0101,
        (
            '#0010280696V#1015F#6P雾……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280697V洛连特确实会起雾，不过\n',
            '最多也只是薄雾吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030280698V#026F#6P嗯……\n',
            '我不记得有过这么浓的雾。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030280699V#022F……我有种不好的预感。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1500, 0, -1)
    OP_0D()
    ChrSetChipByIndex(0x0101, 65535)
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/T0700._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0006 offset: 0x48BC
@scena.Code('func_06_48BC')
def func_06_48BC():
    EventBegin(0x00)
    FadeIn(1000, 0)
    SetScenaFlags(ScenaFlag(0x034F, 1, 0x1A79))
    OP_0D()
    EventEnd(0x00)

    Return()

# id: 0x0007 offset: 0x48CE
@scena.Code('func_07_48CE')
def func_07_48CE():
    EventBegin(0x00)
    Fade(1000)
    CameraMove(57210, 0, -1640, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    CameraMove(57590, 0, -1400, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 57220, 0, -1100, 180)
    OP_4A(0x0008, 255)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0050300233V#552F#6P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300234V#1004F#5P啊……\n',
            '你怎么了？阿加特？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0050300235V#053F#6P……没什么。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0050300236V#051F你还在船内散步吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4ADA',
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
            TXT(0x00, '【◇在第４章最后有让阿加特加入】\n'),
            TXT(0x01, '【◇在第４章最后没有让阿加特加入】\n'),
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
        (0x00000000, 'loc_4ACE'),
        (0x00000001, 'loc_4AD4'),
        (-1, 'loc_4ADA'),
    )

    def _loc_4ACE(): pass

    label('loc_4ACE')

    SetScenaFlags(ScenaFlag(0x0307, 4, 0x183C))

    Jump('loc_4ADA')

    def _loc_4AD4(): pass

    label('loc_4AD4')

    ClearScenaFlags(ScenaFlag(0x0307, 4, 0x183C))

    Jump('loc_4ADA')

    def _loc_4ADA(): pass

    label('loc_4ADA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0307, 4, 0x183C)),
            Expr.Return,
        ),
        'loc_4E24',
    )

    ChrTalk(
        0x0101,
        (
            '#0010240505V#1006F#5P嗯，算是吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300238V#1015F话说回来……\n',
            '那个时候……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0050300239V#052F那个时候……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300240V#1007F#5P哎呀，就是在神秘森林里\n',
            '我们被催眠的时候啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300241V#1025F阿加特你也做梦了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0050300242V#552F………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300243V#1013F#5P啊……对、对不起。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300244V我是不是问了不该问的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0050300245V#053F不……没这回事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050300246V#051F我也做了梦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050300247V感觉是一个\n',
            '让我相当怀念的梦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300248V#1016F#5P是吗……\n',
            '阿加特也是这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300249V#1008F嗯，那个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0050300250V#551F喂喂，别这么露骨地\n',
            '摆出一副想要知道的表情啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050300251V#556F我梦见了小时候在村子里的\n',
            '很平常的一些回忆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300252V#1016F#5P啊，哈哈……是这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300253V#1006F说起来，阿加特是\n',
            '拉文努村出身的吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300254V也算是久违的重归故里了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4EAA')

    def _loc_4E24(): pass

    label('loc_4E24')

    ChrTalk(
        0x0101,
        (
            '#0010220228V#1016F#5P嗯，算是吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300253V#1006F说起来，阿加特是\n',
            '拉文努村出身的吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300254V也算是久违的重归故里了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4EAA(): pass

    label('loc_4EAA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_4F50',
    )

    ChrTalk(
        0x0008,
        (
            '#0050300258V#052F不，因为那起特务兵事件，\n',
            '前不久才刚刚顺道去过。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050300259V#055F──喂，你给我等等。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050300260V为什么你已经认定了\n',
            '我要回村子去？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5002')

    def _loc_4F50(): pass

    label('loc_4F50')

    ChrTalk(
        0x0008,
        (
            '#0050300261V#051F嗯，算是有一阵子了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050300262V最近的一次还是在\n',
            '诞辰庆典刚结束后…',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050300259V#055F──喂，你给我等等。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050300260V为什么你已经认定了\n',
            '我要回村子去？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5002(): pass

    label('loc_5002')

    ChrTalk(
        0x0101,
        (
            '#0010300265V#1001F#5P别害羞别害羞。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300266V#1006F我记得阿加特曾经说过\n',
            '自己在故乡有个妹妹吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300267V#1028F嘿嘿，你一定\n',
            '很疼爱她吧～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0050300268V#555F我说你啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300269V#1004F#5P对了，我记得阿加特的家\n',
            '也是在拉文努村吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300270V#1015F以前因为空贼事件路过时，\n',
            '倒是没遇到过类似的孩子呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300271V和鲁伊在一起的女孩子，\n',
            '感觉上年纪也太小了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0050300272V#051F……嗯，关于米夏，\n',
            '在不久的将来我会向你们介绍的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050300273V如果有机会路过村子的话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300274V#1016F#5P啊，嗯，拜托了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300275V#1006F不过这样一来的话……\n',
            '提妲也得一起带过去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0050300276V#055F为、为什么啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300277V#1006F#5P因为提妲和阿加特\n',
            '似乎相当亲近。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300278V如果不向她介绍的话，\n',
            '她一定会很失望的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0050300279V#552F……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300280V#1004F#5P啊，我明白了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300281V#1028F阿加特你是不想让妹妹\n',
            '和提妲见面吧～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0050300282V#052F什…什么…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300283V#1016F#5P哈哈，被我猜中了吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300284V#1006F因为她们两人会\n',
            '围绕着阿加特互相吃醋的嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300285V#1001F哎呀～\n',
            '当哥哥真不容易啊㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0050300286V#053F什么啊……原来是在说这个啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300287V#1015F#5P？？？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300288V#1006F反正你不用担心，\n',
            '到时候我会帮你的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300289V所以你可以放心地把提妲\n',
            '介绍给你妹妹哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0050300290V#051F嘿嘿……说得也是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050300291V到时候就靠你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0340, 3, 0x1A03))
    ChrSetDirection(0x0008, 270, 400)
    OP_4B(0x0008, 255)
    EventEnd(0x00)

    Return()

# id: 0x0008 offset: 0x556B
@scena.Code('func_08_556B')
def func_08_556B():
    EventBegin(0x00)
    Fade(1000)
    CameraMove(90670, 0, 44790, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_4A(0x000B, 255)
    ChrSetDirection(0x000B, 270, 0)
    ChrSetPos(0x0101, 90160, 0, 44840, 90)
    OP_0D()

    ChrTalk(
        0x000B,
        (
            '#0070300295V#061F啊，姐姐。\n',
            '你又在散步吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_56AC',
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
            TXT(0x00, '【◇在第４章最后有让提妲加入】\n'),
            TXT(0x01, '【◇在第４章最后没有让提妲加入】\n'),
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
        (0x00000000, 'loc_56A0'),
        (0x00000001, 'loc_56A6'),
        (-1, 'loc_56AC'),
    )

    def _loc_56A0(): pass

    label('loc_56A0')

    SetScenaFlags(ScenaFlag(0x0307, 5, 0x183D))

    Jump('loc_56AC')

    def _loc_56A6(): pass

    label('loc_56A6')

    ClearScenaFlags(ScenaFlag(0x0307, 5, 0x183D))

    Jump('loc_56AC')

    def _loc_56AC(): pass

    label('loc_56AC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0307, 5, 0x183D)),
            Expr.Return,
        ),
        'loc_599C',
    )

    ChrTalk(
        0x0101,
        (
            '#0010300296V#1006F#6P嗯，算是吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300297V#1015F话说回来……\n',
            '提妲你呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300298V那时候你是不是也做了梦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0070300299V#066F啊，嗯。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070300300V我梦见爸爸妈妈\n',
            '回到家了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070300301V妈妈和爷爷久别重逢，\n',
            '又在感情要好地斗嘴呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300302V#1016F#6P是、是这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300303V#1006F不过似乎是个\n',
            '美梦呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0070300304V#067F嘿嘿……嗯。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070300305V因为姐姐你们\n',
            '也一起出现了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300306V#1004F#6P啊，是吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0070300307V#560F在爸爸妈妈\n',
            '回家之后……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070300308V姐姐和约修亚哥哥\n',
            '还有阿加特哥哥都来家里。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070300309V然后在爷爷的提议下，\n',
            '大家一起去温泉玩了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300310V#1001F#6P啊哈哈……\n',
            '真是个相当快乐的梦呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300311V#1006F嗯……不过一定要\n',
            '让这个美梦成真哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0070300312V#061F嗯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5B28')

    def _loc_599C(): pass

    label('loc_599C')

    ChrTalk(
        0x0101,
        (
            '#0010240505V#1006F#6P嗯，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300314V#1015F对了，提妲你是\n',
            '第一次来柏斯吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0070300315V#560F嗯，是第一次。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070300316V我听说柏斯\n',
            '有家很大的商店……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300317V#1006F#6P哦，你是说柏斯超市啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300318V感觉就像是王都的百货商店\n',
            '变大了的样子。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300319V里面有各种店铺，\n',
            '非常的热闹呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0070300320V#064F哇～好厉害。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070300321V#067F嘿嘿嘿……\n',
            '真想早点到柏斯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5B28(): pass

    label('loc_5B28')

    ChrSetDirection(0x000B, 90, 400)
    OP_4B(0x000B, 255)
    SetScenaFlags(ScenaFlag(0x0340, 4, 0x1A04))
    EventEnd(0x00)

    Return()

# id: 0x0009 offset: 0x5B39
@scena.Code('func_09_5B39')
def func_09_5B39():
    EventBegin(0x00)
    Fade(1000)
    CameraMove(90670, 0, 44790, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_4A(0x000B, 255)
    ChrSetDirection(0x000B, 270, 0)
    ChrSetPos(0x0101, 90160, 0, 44840, 90)
    OP_0D()

    ChrTalk(
        0x000B,
        (
            '#0070300322V#560F对了，姐姐。\n',
            '你去过拉文努村吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300323V#1006F#6P嗯，以前因为工作去过。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300324V#1015F我记得……\n',
            '那里是阿加特的故乡吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0070300325V#061F嗯，他妹妹米夏\n',
            '小姐就住在那里。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070300326V听说阿加特先生为了\n',
            '探望妹妹，\n',
            '一年要回去好几次呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300327V#1004F#6P哦，还有这种事啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300328V#1006F不过，阿加特的妹妹啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300329V有个那么大大咧咧的哥哥，\n',
            '也一定很辛苦吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0070300330V#063F真是的～姐姐你怎么这么说。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070300331V阿加特哥哥虽然有些粗鲁，\n',
            '不过却是个很善良的人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300332V#1016F#6P啊，知道了知道了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300333V#1017F粗心又害羞这一点，\n',
            '我也承认。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0070300334V#061F嘿嘿……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070300335V#560F我觉得米夏小姐\n',
            '一定是个很好的人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070300336V阿加特哥哥\n',
            '每次提到米夏小姐时\n',
            '眼神就变得很温柔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070300337V……………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300338V#1004F#6P？　怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0070300339V#067F不，没什么。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070300340V只不过有点……\n',
            '心里有点复杂的感觉……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070300341V嘿嘿，不知是怎么了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300342V#1016F#6P（唔……\n',
            '这好像是在吃醋呢。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000B, 90, 400)
    OP_4B(0x000B, 255)
    SetScenaFlags(ScenaFlag(0x0340, 5, 0x1A05))
    EventEnd(0x00)

    Return()

# id: 0x000A offset: 0x5FAF
@scena.Code('func_0A_5FAF')
def func_0A_5FAF():
    EventBegin(0x00)
    Fade(1000)
    CameraMove(88790, 0, -3030, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 88300, 0, -2780, 90)
    ChrSetSubChip(0x000A, 1)
    OP_0D()

    ChrTalk(
        0x000A,
        (
            '#0040300414V#030F哎呀，艾丝蒂尔。\n',
            '马上就要到柏斯了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040300415V也就是说回到了我们\n',
            '初次相遇的回忆之地。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040300416V#035F呼……\n',
            '多么令人感慨啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300417V#1006F#6P被你这么一说，\n',
            '确实很令人感慨……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300418V#1019F不过那时候的奥利维尔\n',
            '可是个很没礼貌的人哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300419V居然说我『缺乏女性魅力』，\n',
            '真是过分……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0040300420V#031F呵呵，这是个误会。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040300421V你可以把那当作是我\n',
            '看到心仪之人后，因为害羞\n',
            '而做出的掩饰表现。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300422V#1007F#6P哼，又开始耍赖……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300423V#1009F明明对雪拉姐和约修亚\n',
            '马上就发起攻势了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0040300424V#035F那种事就不要去计较啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040300425V#030F现在的你，魅力\n',
            '已经完全不逊于她们了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040300426V柔美又健康的性感，\n',
            '再加上少女特有的娇羞……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040300427V#031F嗯嗯，真是长大了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300428V#1008F#6P谢、谢谢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300429V#1013F等等，请你少说这种\n',
            '会让人感觉不好意思的话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0040300430V#035F呵呵，没什么好害羞的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040300431V#037F不过，你终于离成年人\n',
            '又更近了一步。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040300432V为了向更高层次迈进，\n',
            '就让大哥哥我来亲切地指导……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300433V#1019F#6P这就不用你操心了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300434V与其拜托奥利维尔，\n',
            '我还不如去拜托雪拉姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0040300435V#034F呼，真遗憾。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040300436V#033F不过由雪拉来亲切地\n',
            '指导艾丝蒂尔啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040280587V…………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040300438V#037F…………啊啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300439V#1005F#6P你、你在想象些什么啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_65EC',
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
            TXT(0x00, '【◇在第４章最后有让奥利维尔加入】\n'),
            TXT(0x01, '【◇在第４章最后没有让奥利维尔加入】\n'),
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
        (0x00000000, 'loc_65E0'),
        (0x00000001, 'loc_65E6'),
        (-1, 'loc_65EC'),
    )

    def _loc_65E0(): pass

    label('loc_65E0')

    SetScenaFlags(ScenaFlag(0x0307, 6, 0x183E))

    Jump('loc_65EC')

    def _loc_65E6(): pass

    label('loc_65E6')

    ClearScenaFlags(ScenaFlag(0x0307, 6, 0x183E))

    Jump('loc_65EC')

    def _loc_65EC(): pass

    label('loc_65EC')

    ChrSetSubChip(0x000A, 0)
    SetScenaFlags(ScenaFlag(0x0340, 7, 0x1A07))
    EventEnd(0x00)

    Return()

# id: 0x000B offset: 0x65F7
@scena.Code('func_0B_65F7')
def func_0B_65F7():
    EventBegin(0x00)
    Fade(1000)
    CameraMove(88790, 0, -3030, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 88300, 0, -2780, 90)
    ChrSetSubChip(0x000A, 1)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010300440V#1004F#6P对了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300441V#1015F奥利维尔那时候\n',
            '也被催眠了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300442V你一定也做梦了对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0040300443V#033F嗯……算是吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040250844V#032F………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300445V#1026F#6P？　怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0040300446V#034F不……\n',
            '感觉实在是好～可惜啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040300447V因为那是一个绝世美女\n',
            '云集的后宫美梦啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040300448V如果不是被艾丝蒂尔吵醒的话，\n',
            '我还能做很多事的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040300449V#037F嘻嘻，现在也只能让艾丝蒂尔\n',
            '你自己来补偿了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300450V#1001F#6P要我用棍子来让你永远长眠吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0040300451V#036F只是开玩笑啦！请原谅我！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300452V#1007F#6P真受不了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300453V#1003F（不过奥利维尔……\n',
            '刚才的眼神有点孤寂……)',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300454V（究竟发生过什么事呢……？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0040300455V#035F呼……\n',
            '没必要摆出这副表情吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300456V#1004F#6P啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0040300457V#030F不是什么了不起的梦。\n',
            '只是少年时代的回忆罢了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040300458V穆拉等人也有在梦中登场。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240254V#1025F#6P这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300460V#1019F那、那你\n',
            '一开始就该这么说！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0040300461V#031F别生气嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x000A, 0)
    SetScenaFlags(ScenaFlag(0x0341, 0, 0x1A08))
    EventEnd(0x00)

    Return()

# id: 0x000C offset: 0x6A59
@scena.Code('func_0C_6A59')
def func_0C_6A59():
    EventBegin(0x00)
    Fade(1000)
    CameraMove(116960, 0, 3460, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 116470, 0, 3640, 90)
    ChrSetSubChip(0x000D, 1)
    OP_0D()

    ChrTalk(
        0x000D,
        (
            '#0060300464V#040F艾丝蒂尔。\n',
            '又在散步吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300465V#1008F#6P嘿嘿，算是吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300466V#1007F话说回来，真的很对不起。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300467V约修亚的事情\n',
            '我那么晚才说出来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0060300468V#041F呵呵，没有那么严重。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060300469V#542F说起来，和约修亚\n',
            '同行的女孩子\n',
            '是空贼团的人吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300470V#1019F#6P嗯，是一个名叫乔丝特，\n',
            '相当刁蛮又很任性的女孩子。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300471V说话也像男孩子，\n',
            '所以我叫她男人婆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0060300472V#542F是这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060300473V#045F不过，光从照片来看的话，\n',
            '也是位相当有魅力的女性呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300474V#1007F#6P唔，我也承认她不开口的话\n',
            '是个可爱的家伙。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300475V最开始遇见她的时候，\n',
            '还天衣无缝地扮演了一回大小姐呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0060300476V#044F？？？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '向科洛丝诉说了在洛连特\n',
            '市长家和乔丝特第一次见面时的情景。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x000D,
        (
            '#0060300477V#044F啊，还有这种事啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060300478V#041F真是个相当有心机的人物。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300479V#1015F#6P因为她是埃雷波尼亚的\n',
            '原贵族出身。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300480V所以擅于隐藏自己的真实面目。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300481V#1007F她的本性就像刚才说的，\n',
            '性格上既刁蛮又很任性。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0060300482V#048F呵呵，不过听到现在\n',
            '却感觉让人憎恨不起来呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060300483V我有种预感，如果试着和她\n',
            '交谈的话一定会很合得来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300484V#1019F#6P唔，我可能不行。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300485V感觉性格上\n',
            '和她相处不来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0060300486V#045F呵呵，这种事\n',
            '也是常有的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7071',
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
            TXT(0x00, '【◇在第４章最后有让科洛丝加入】\n'),
            TXT(0x01, '【◇在第４章最后没有让科洛丝加入】\n'),
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
        (0x00000000, 'loc_7065'),
        (0x00000001, 'loc_706B'),
        (-1, 'loc_7071'),
    )

    def _loc_7065(): pass

    label('loc_7065')

    SetScenaFlags(ScenaFlag(0x0307, 7, 0x183F))

    Jump('loc_7071')

    def _loc_706B(): pass

    label('loc_706B')

    ClearScenaFlags(ScenaFlag(0x0307, 7, 0x183F))

    Jump('loc_7071')

    def _loc_7071(): pass

    label('loc_7071')

    ChrSetSubChip(0x000D, 0)
    SetScenaFlags(ScenaFlag(0x0341, 1, 0x1A09))
    EventEnd(0x00)

    Return()

# id: 0x000D offset: 0x707C
@scena.Code('func_0D_707C')
def func_0D_707C():
    EventBegin(0x00)
    Fade(1000)
    CameraMove(116960, 0, 3460, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 116470, 0, 3640, 90)
    ChrSetSubChip(0x000D, 1)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010300440V#1004F#6P对了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300488V#1015F科洛丝你那时候，\n',
            '也被催眠了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300442V你一定也做梦了对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0060300490V#542F嗯……\n',
            '是『百日战役』时的梦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300491V#1004F#6P『百日战役』时……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300492V#1025F这样啊，我记得那时候\n',
            '你是和特蕾莎老师在一起……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0060300493V#040F嗯，受到老师她们的保护，\n',
            '暂时生活在一起。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060300494V#045F不过……呵呵。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300495V#1004F#6P怎、怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0060300496V#048F不，明明是１０年前的事，\n',
            '可是不知为什么克拉姆和乔儿他们\n',
            '中途也都加进来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060300497V如果一直做下去的话，\n',
            '艾丝蒂尔和约修亚也\n',
            '有可能会出现呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300498V#1016F#6P哈哈，果然是梦境，\n',
            '总会有不可思议的情景出现呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0060300499V#045F嗯。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060300500V#043F可是……\n',
            '现在想想也还有点后怕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300501V#1026F#6P咦……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0060300502V#049F梦中的我真的很幸福……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060300503V打从心底里希望日子能够\n',
            '就这样一直保持下去。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060300504V#043F可是我就是觉得\n',
            '哪里有点不对劲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300505V#1007F#6P嗯……\n',
            '我明白你想说什么。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300506V#1002F做了个好梦，确实\n',
            '感觉挺幸运的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300507V可是如果问我还想不想再做这个梦，\n',
            '我就会有点犹豫了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0060300508V#047F嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060300509V#042F『福音』拥有着另一种\n',
            '意义之下的危险性……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060300510V我隐约能够感觉到这一点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x000D, 0)
    SetScenaFlags(ScenaFlag(0x0341, 2, 0x1A0A))
    EventEnd(0x00)

    Return()

# id: 0x000E offset: 0x75A8
@scena.Code('func_0E_75A8')
def func_0E_75A8():
    EventBegin(0x00)
    Fade(1000)
    CameraMove(116890, 0, -550, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 116390, 0, -360, 90)
    ChrSetSubChip(0x000C, 1)
    OP_0D()

    ChrTalk(
        0x000C,
        (
            '#0080300513V#071F哟，艾丝蒂尔。\n',
            '这次辛苦你了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080300514V你又在游击士的\n',
            '道路上前进了一步。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300515V#1017F#6P嘿嘿……我还不够成熟。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300516V棒术的水平\n',
            '也和老爸有千里之遥。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0080300517V#070F哈哈，你不用太\n',
            '在意大人的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080300518V#075FＳ级的游击士都是\n',
            '一些悟出了『理』的高人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080300519V老实说，像我这种人花一辈子的时间\n',
            '都不知道能不能达到那种程度。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300520V#1004F#6P这、这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300521V#1025F虽然我对老爸有多强这一点，\n',
            '到现在为止都没有什么真实感……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300522V不过『理』究竟是什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0080300523V#074F嗯……这个嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080300524V#070F大人以前被称为『剑圣』，\n',
            '是位剑术超群的人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080300525V可是他现在用起棍棒来\n',
            '就像熟悉的剑一样挥洒自如。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080300526V你知道这是为什么吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300527V#1015F#6P嗯～拼命的练习？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0080300528V#070F当然这也是原因之一。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080300529V不过更重要的是，他迅速地\n',
            '掌握了棒术的本质。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080300530V#074F那是超越了招式、反应、力量\n',
            '和气劲的绝对高度……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080300531V把握住事物的本质，\n',
            '并能自由自在地操纵的境界……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080300532V#072F这就是『理』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300533V#1002F#6P事物的本质……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0080300534V#070F恐怕大人在『百日战役』中用来\n',
            '击退了帝国军的谋略也是同样道理。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080300535V正因为掌握了战争\n',
            '这一事物的本质，才能设计\n',
            '和实行了那么大胆的反攻作战。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080300536V如果他是敌人的话，\n',
            '一定是个最可怕的敌人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010261058V#1007F#6P原，原来如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300538V#1002F可是老爸在某种意义上来说，\n',
            '也被『结社』钻了空子了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300539V政变的时候\n',
            '也被诱骗到了国外去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0080300540V#072F嗯，他们也一定拥有\n',
            '能和大人匹敌的人物吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080300541V虽然不知道那是『莱维』\n',
            '还是『教授』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300542V#1015F#6P嗯～和我们战斗过的\n',
            '『洛伦斯少尉』怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0080300543V#073F那家伙啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080300544V#072F能力确实很强，\n',
            '不过不知道能不能和大人匹敌。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080300545V#572F而且我感觉那家伙的强\n',
            '并不是来自于『理』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080300546V却像是一把被冷冰冰地磨透、锤炼、\n',
            '不让任何人侵犯的利刃……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080300547V就是那样的感觉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300548V#1002F#6P……嗯。\n',
            '我可以明白你想说的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300549V#1007F后来就没见过他了，\n',
            '他究竟在干些什么呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300550V#1003F……约修亚似乎对他也很在意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0080300551V#072F嗯，在『结社』时\n',
            '可能有过什么因缘吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080300552V#074F不管是我还是雪拉扎德，\n',
            '都和他们有种巧妙因缘呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080300553V这说不定……\n',
            '也是女神的引导呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7F66',
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
            TXT(0x00, '【◇在第４章最后有让金加入】\n'),
            TXT(0x01, '【◇在第４章最后没有让金加入】\n'),
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
        (0x00000000, 'loc_7F5A'),
        (0x00000001, 'loc_7F60'),
        (-1, 'loc_7F66'),
    )

    def _loc_7F5A(): pass

    label('loc_7F5A')

    SetScenaFlags(ScenaFlag(0x0308, 0, 0x1840))

    Jump('loc_7F66')

    def _loc_7F60(): pass

    label('loc_7F60')

    ClearScenaFlags(ScenaFlag(0x0308, 0, 0x1840))

    Jump('loc_7F66')

    def _loc_7F66(): pass

    label('loc_7F66')

    ChrSetSubChip(0x000C, 0)
    SetScenaFlags(ScenaFlag(0x0341, 3, 0x1A0B))
    EventEnd(0x00)

    Return()

# id: 0x000F offset: 0x7F71
@scena.Code('func_0F_7F71')
def func_0F_7F71():
    EventBegin(0x00)
    Fade(1000)
    CameraMove(116890, 0, -550, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 116390, 0, -360, 90)
    ChrSetSubChip(0x000C, 1)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010300554V#1004F#6P啊，这么说来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300555V#1015F金先生那时候\n',
            '也被催眠了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300442V是不是也做了什么梦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0080300557V#070F啊啊……\n',
            '我梦见了在道场时的光景。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080300558V#071F当我注意到雾香和现在\n',
            '几乎没什么两样时，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080300559V在梦中情不自禁地笑了出来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300560V#1011F#6P哦～？雾香小姐\n',
            '从很早以前就是那样的感觉？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0080300561V#070F嗯，一直是那样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080300562V真想不透，她那个样子\n',
            '还能和瓦鲁特交往……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300563V#1004F#6P咦……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0080300564V#075F……说漏嘴了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080300565V#070F不好意思，请你忘了刚才的话吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300566V#1013F#6P嗯、嗯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x000C, 0)
    SetScenaFlags(ScenaFlag(0x0341, 4, 0x1A0C))
    EventEnd(0x00)

    Return()

# id: 0x0010 offset: 0x822D
@scena.Code('func_10_822D')
def func_10_822D():
    EventBegin(0x00)
    PlaySE(166, 0x00, 0x64)
    Sleep(500)

    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('女性的声音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0880200720V……久等了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0880300570V本船即将\n',
            '到达柏斯市。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0880200722V着陆时会有少许摇晃，\n',
            '请尽快回到座位。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/T1102._SN', 100, 0, 0)
    IdleLoop()

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
