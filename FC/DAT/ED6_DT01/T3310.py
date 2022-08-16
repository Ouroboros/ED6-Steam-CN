import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T3310_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3310   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'T3310.x'
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
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT07/CH01690._CH', 'ED6_DT07/CH01690P._CP'),
        ('ED6_DT07/CH02640._CH', 'ED6_DT07/CH02640P._CP'),
        ('ED6_DT07/CH01300._CH', 'ED6_DT07/CH01300P._CP'),
        ('ED6_DT07/CH01300._CH', 'ED6_DT07/CH01300P._CP'),
        ('ED6_DT07/CH01310._CH', 'ED6_DT07/CH01310P._CP'),
        ('ED6_DT07/CH01300._CH', 'ED6_DT07/CH01300P._CP'),
        ('ED6_DT07/CH01270._CH', 'ED6_DT07/CH01270P._CP'),
    ]

# id: 0x10001 offset: 0xEA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '多杰',
            x                   = -44500,
            z                   = 0,
            y                   = 7710,
            direction           = 82,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            name                = '拉德米拉',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '卡雷尔',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '士兵布拉姆',
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
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            name                = '士兵赫宁',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '派斯队长',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '格温副长',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '伦法',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
    )

# id: 0x10002 offset: 0x1EA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x1EA
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x1EA
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 7230,
            triggerZ            = 0,
            triggerY            = 9350,
            triggerRange        = 400,
            actorX              = 6990,
            actorZ              = 1500,
            actorY              = 11450,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000D,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -49710,
            triggerZ            = 0,
            triggerY            = 7160,
            triggerRange        = 400,
            actorX              = -51810,
            actorZ              = 1500,
            actorY              = 6820,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -49710,
            triggerZ            = 0,
            triggerY            = 7160,
            triggerRange        = 400,
            actorX              = -51810,
            actorZ              = 1500,
            actorY              = 6820,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x256
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_28C',
    )

    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0009, 6160, 0, 66940, 0)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, 11190, 0, 68400, 180)

    Jump('loc_2F7')

    def _loc_28C(): pass

    label('loc_28C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_296',
    )

    Jump('loc_2F7')

    def _loc_296(): pass

    label('loc_296')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_2A0',
    )

    Jump('loc_2F7')

    def _loc_2A0(): pass

    label('loc_2A0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_2AA',
    )

    Jump('loc_2F7')

    def _loc_2AA(): pass

    label('loc_2AA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_2B4',
    )

    Jump('loc_2F7')

    def _loc_2B4(): pass

    label('loc_2B4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_2BE',
    )

    Jump('loc_2F7')

    def _loc_2BE(): pass

    label('loc_2BE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_2C8',
    )

    Jump('loc_2F7')

    def _loc_2C8(): pass

    label('loc_2C8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_2D2',
    )

    Jump('loc_2F7')

    def _loc_2D2(): pass

    label('loc_2D2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_2DC',
    )

    Jump('loc_2F7')

    def _loc_2DC(): pass

    label('loc_2DC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Return,
        ),
        'loc_2EB',
    )

    ChrClearFlags(0x0008, 0x0080)

    Jump('loc_2F7')

    def _loc_2EB(): pass

    label('loc_2EB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_2F7',
    )

    ChrClearFlags(0x0008, 0x0080)

    def _loc_2F7(): pass

    label('loc_2F7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_343',
    )

    ChrClearFlags(0x000C, 0x0080)
    ChrSetPos(0x000C, 11650, 0, 7310, 359)
    ChrClearFlags(0x000D, 0x0080)
    ChrSetPos(0x000D, -51810, 0, 6820, 97)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x000F, 6990, 0, 11450, 189)

    Jump('loc_4D2')

    def _loc_343(): pass

    label('loc_343')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_3A5',
    )

    ChrClearFlags(0x000C, 0x0080)
    ChrSetPos(0x000C, 11650, 0, 7310, 359)
    ChrClearFlags(0x000D, 0x0080)
    ChrSetPos(0x000D, -55630, 0, 9700, 105)
    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x000E, -54180, 0, 9800, 267)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x000F, 6990, 0, 11450, 189)

    Jump('loc_4D2')

    def _loc_3A5(): pass

    label('loc_3A5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_3DB',
    )

    ChrClearFlags(0x000D, 0x0080)
    ChrSetPos(0x000D, -51810, 0, 6820, 97)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x000F, 6990, 0, 11450, 189)

    Jump('loc_4D2')

    def _loc_3DB(): pass

    label('loc_3DB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_427',
    )

    ChrClearFlags(0x000C, 0x0080)
    ChrSetPos(0x000C, 11650, 0, 7310, 359)
    ChrClearFlags(0x000D, 0x0080)
    ChrSetPos(0x000D, -51810, 0, 6820, 97)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x000F, 6990, 0, 11450, 189)

    Jump('loc_4D2')

    def _loc_427(): pass

    label('loc_427')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_489',
    )

    ChrClearFlags(0x000C, 0x0080)
    ChrSetPos(0x000C, 3860, 0, 68230, 108)
    ChrClearFlags(0x000D, 0x0080)
    ChrSetPos(0x000D, 3970, 0, 9040, 0)
    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x000E, -51810, 0, 6820, 97)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x000F, 6990, 0, 11450, 189)

    Jump('loc_4D2')

    def _loc_489(): pass

    label('loc_489')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_4D2',
    )

    ChrClearFlags(0x000C, 0x0080)
    ChrSetPos(0x000C, 11650, 0, 7310, 359)
    ChrClearFlags(0x000D, 0x0080)
    ChrSetPos(0x000D, -51810, 0, 6820, 97)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x000F, 6990, 0, 11450, 189)

    def _loc_4D2(): pass

    label('loc_4D2')

    Return()

# id: 0x0001 offset: 0x4D3
@scena.Code('func_01_4D3')
def func_01_4D3():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_4E1',
    )

    OP_64(0x02, 0x0001)

    Jump('loc_528')

    def _loc_4E1(): pass

    label('loc_4E1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_4F3',
    )

    OP_64(0x01, 0x0001)
    OP_64(0x02, 0x0001)

    Jump('loc_528')

    def _loc_4F3(): pass

    label('loc_4F3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_501',
    )

    OP_64(0x02, 0x0001)

    Jump('loc_528')

    def _loc_501(): pass

    label('loc_501')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_50F',
    )

    OP_64(0x02, 0x0001)

    Jump('loc_528')

    def _loc_50F(): pass

    label('loc_50F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_51D',
    )

    OP_64(0x01, 0x0001)

    Jump('loc_528')

    def _loc_51D(): pass

    label('loc_51D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_528',
    )

    OP_64(0x02, 0x0001)

    def _loc_528(): pass

    label('loc_528')

    Return()

# id: 0x0002 offset: 0x529
@scena.Code('func_02_529')
def func_02_529():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_53E',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_529')

    def _loc_53E(): pass

    label('loc_53E')

    Return()

# id: 0x0003 offset: 0x53F
@scena.Code('func_03_53F')
def func_03_53F():
    TalkBegin(0x00FE)
    TalkEnd(0x00FE)

    Return()

# id: 0x0004 offset: 0x546
@scena.Code('func_04_546')
def func_04_546():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_644',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_5D3',
    )

    ChrTalk(
        0x00FE,
        (
            '哦，\n',
            '马上就快到门卫的交班时间了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……不过，\n',
            '还是像平常那样等着吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '等布拉姆那家伙\n',
            '来叫我之后再离开吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_641')

    def _loc_5D3(): pass

    label('loc_5D3')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '袭击工房的犯人\n',
            '究竟逃到哪里去了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们的队长\n',
            '也百思不得其解。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '算了，\n',
            '那也不是队长的责任。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_641(): pass

    label('loc_641')

    Jump('loc_A25')

    def _loc_644(): pass

    label('loc_644')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_71E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_6B4',
    )

    ChrTalk(
        0x00FE,
        (
            '我想大概队长本人\n',
            '也不愿意接受这个命令吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……算了， \n',
            '他只是不愿轻易说出自己的意见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_71B')

    def _loc_6B4(): pass

    label('loc_6B4')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '不知道为什么，\n',
            '上面好像下令解除盘查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '怎么想都觉得很奇怪啊。\n',
            '真是不明白上面的人在想什么。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_71B(): pass

    label('loc_71B')

    Jump('loc_A25')

    def _loc_71E(): pass

    label('loc_71E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_889',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_802',
    )

    ChrTalk(
        0x00FE,
        (
            '一天到晚盯着共和国的动向\n',
            '也没什么用啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为了在关键时刻能发挥力量，\n',
            '平时就要放松一点嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '队长的这个想法\n',
            '我也非常地理解，\n',
            '可是副长的脑袋却很顽固……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '自从他来到这里，\n',
            '很多事情都变得难办起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_886')

    def _loc_802(): pass

    label('loc_802')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '工作的时候\n',
            '还是要讲究方法嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为了将来可能出现的关键时刻作准备，\n',
            '平时要保存力量才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这个堡垒\n',
            '也有这样的地方哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_886(): pass

    label('loc_886')

    Jump('loc_A25')

    def _loc_889(): pass

    label('loc_889')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_929',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_8E1',
    )

    ChrTalk(
        0x00FE,
        (
            '我可不是在偷懒。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只是整理一下床单，\n',
            '把花瓶的位置摆整齐而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_926')

    def _loc_8E1(): pass

    label('loc_8E1')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '这个时间\n',
            '队长应该下来吃饭了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以在这里\n',
            '先这么坚持吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_926(): pass

    label('loc_926')

    Jump('loc_A25')

    def _loc_929(): pass

    label('loc_929')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_A25',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_99F',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然已经是交班的时间了， \n',
            '但是布拉姆那家伙肯定还在睡觉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我也没有必要\n',
            '特地过去把他叫醒吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A25')

    def _loc_99F(): pass

    label('loc_99F')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '哦，再过不久就要和布拉姆\n',
            '进行门卫工作的交班了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……不过，\n',
            '还是不用那么心急了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '等布拉姆那家伙\n',
            '来叫我之后再离开吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A25(): pass

    label('loc_A25')

    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0xA29
@scena.Code('func_05_A29')
def func_05_A29():
    Call(0, 0x0006)

    Return()

# id: 0x0006 offset: 0xA2E
@scena.Code('func_06_A2E')
def func_06_A2E():
    TalkBegin(0x000D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_AF7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_A89',
    )

    ChrTalk(
        0x000D,
        (
            '但是，总部的命令真是奇怪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '说不定背后\n',
            '有什么见不得人的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_AF4')

    def _loc_A89(): pass

    label('loc_A89')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x000D,
        (
            '从军队总部发来了\n',
            '重新展开盘查的命令……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '恐怖袭击已经过了一段时间了。\n',
            '现在再盘查已经太迟了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_AF4(): pass

    label('loc_AF4')

    Jump('loc_119D')

    def _loc_AF7(): pass

    label('loc_AF7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_C67',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_B77',
    )

    ChrTalk(
        0x000D,
        (
            '不过命令是不能违抗的，\n',
            '那就不要违抗了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '正因如此，\n',
            '今后就以强化警备为由，\n',
            '继续维持盘查时的体制吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C64')

    def _loc_B77(): pass

    label('loc_B77')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x000D,
        (
            '副长的疑问暂且不说，\n',
            '命令就是命令。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '我们是不能违抗的。\n',
            '重新展开盘查是不可能的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '……但是，\n',
            '只要不违抗命令就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '正因如此，\n',
            '今后就以强化警备为由，\n',
            '继续维持盘查时的体制吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '绝对没有可疑的家伙\n',
            '从这里逃到国外。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C64(): pass

    label('loc_C64')

    Jump('loc_119D')

    def _loc_C67(): pass

    label('loc_C67')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_D93',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_CED',
    )

    ChrTalk(
        0x000D,
        (
            '因为蔡斯事件的影响，\n',
            '现在如果没有充足的理由\n',
            '是无法通行的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '打算去共和国的话，\n',
            '我想还是过一阵子再来比较好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D90')

    def _loc_CED(): pass

    label('loc_CED')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x000D,
        (
            '因为蔡斯事件的关系，\n',
            '现在如果没有充足的理由\n',
            '是无法通行的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '如果要去共和国的话，\n',
            '最好还是下次再来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '因为这是个相当严重的事件，\n',
            '调查也要花些时间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D90(): pass

    label('loc_D90')

    Jump('loc_119D')

    def _loc_D93(): pass

    label('loc_D93')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_EBB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_E27',
    )

    ChrTalk(
        0x000D,
        (
            '格温副长\n',
            '真是让我伤脑筋……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '如果放任他那种人不管的话，\n',
            '会带来很多麻烦的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '唔，不过大家要是能\n',
            '学习他的优点就太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EB8')

    def _loc_E27(): pass

    label('loc_E27')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x000D,
        (
            '呼，格温副长\n',
            '真是让我伤脑筋……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '他既有能力，\n',
            '也很有干劲，\n',
            '但就是做事有些欠考虑。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '如果放任他那种人不管的话，\n',
            '会带来很多麻烦的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_EB8(): pass

    label('loc_EB8')

    Jump('loc_119D')

    def _loc_EBB(): pass

    label('loc_EBB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_FEE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_F4F',
    )

    ChrTalk(
        0x000D,
        (
            '这一带本来就有\n',
            '很多共和国来的移民。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '比如，我们这里的酒保伦法\n',
            '也是共和国出生的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '作为友好邻邦，\n',
            '今后也要好好相处啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FEB')

    def _loc_F4F(): pass

    label('loc_F4F')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x000D,
        (
            '通过这个关所的\n',
            '主要是来往于\n',
            '共和国和利贝尔之间的商人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '虽然和共和国之间\n',
            '有定期船的航线，\n',
            '不过毕竟比较费钱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '现在步行过境的人\n',
            '还是很多的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_FEB(): pass

    label('loc_FEB')

    Jump('loc_119D')

    def _loc_FEE(): pass

    label('loc_FEE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_119D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_10C8',
    )

    ChrTalk(
        0x000D,
        (
            '这个关所的使命\n',
            '就是避免不必要的紧张局面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '我国已经和帝国不和睦了，\n',
            '再和共和国交恶的话，\n',
            '那么处境就很不妙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '所以我让部下\n',
            '工作时点到为止就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '哈～哈～哈，\n',
            '这真是受照顾的岗位呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_119D')

    def _loc_10C8(): pass

    label('loc_10C8')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x000D,
        (
            '啊，欢迎欢迎。\n',
            '千里迢迢来到这里真是辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '这里是沃尔费堡垒， \n',
            '是和卡尔瓦德共和国\n',
            '交界的守卫关所。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '因为对面是共和国，\n',
            '所以和哈肯大门那里\n',
            '是不一样的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '……正因如此， \n',
            '我们守卫起来也很轻松。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_119D(): pass

    label('loc_119D')

    TalkEnd(0x000D)

    Return()

# id: 0x0007 offset: 0x11A1
@scena.Code('func_07_11A1')
def func_07_11A1():
    Call(0, 0x0008)

    Return()

# id: 0x0008 offset: 0x11A6
@scena.Code('func_08_11A6')
def func_08_11A6():
    TalkBegin(0x000E)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_12A5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_1208',
    )

    ChrTalk(
        0x000E,
        (
            '队长！\n',
            '请重新开始盘查的工作！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '现在这样的话，\n',
            '犯人有可能会逃亡国外！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12A2')

    def _loc_1208(): pass

    label('loc_1208')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x000E,
        (
            '关于盘查解除的命令\n',
            '正好要向队长问一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '明明没有犯人被逮捕的消息，\n',
            '却自作主张下达这样的命令。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '到底该向士兵们\n',
            '怎么说明才好？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000E, 0x000D, 400)
    ChrSetFlags(0x000E, 0x0010)

    def _loc_12A2(): pass

    label('loc_12A2')

    Jump('loc_140A')

    def _loc_12A5(): pass

    label('loc_12A5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_140A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_1335',
    )

    ChrTalk(
        0x000E,
        (
            '部下的怠慢\n',
            '都是上司的责任啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '本来应该坚持让队长重新考虑一下，\n',
            '可是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '队长是这里的责任人。\n',
            '我也不能太过越权。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_140A')

    def _loc_1335(): pass

    label('loc_1335')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x000E,
        (
            '士兵们这么怠慢，\n',
            '派斯队长难逃其责。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '因为队长采取放任主义，\n',
            '都不注意士兵的行为。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '这件事我以前就和队长探讨过，\n',
            '但是……\n',
            '怎么说他也听不进去啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '算了，\n',
            '这里的负责人是派斯队长。\n',
            '我不能再多说了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_140A(): pass

    label('loc_140A')

    TalkEnd(0x000E)

    Return()

# id: 0x0009 offset: 0x140E
@scena.Code('func_09_140E')
def func_09_140E():
    TalkBegin(0x000F)
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
            TXT(0x00, '对话\n'),
            TXT(0x01, '买东西\n'),
            TXT(0x02, '休息\n'),
            TXT(0x03, '离开\n'),
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
        'loc_1471',
    )

    OP_0D()
    OP_A9(0x48)
    OP_56(0x00)
    TalkEnd(0x000F)

    Return()

    def _loc_1471(): pass

    label('loc_1471')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1487',
    )

    OP_0D()
    OP_A9(0x47)
    OP_56(0x00)
    TalkEnd(0x000F)

    Return()

    def _loc_1487(): pass

    label('loc_1487')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1498',
    )

    TalkEnd(0x000F)

    Return()

    def _loc_1498(): pass

    label('loc_1498')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_1524',
    )

    ChrTalk(
        0x000F,
        (
            '你们知道吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '袭击中央工房的犯人\n',
            '好像还没有抓到哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '军队那些家伙们\n',
            '到底都在干些什么啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '……连晚饭都不来吃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B04')

    def _loc_1524(): pass

    label('loc_1524')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_1661',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_15D4',
    )

    ChrTalk(
        0x000F,
        (
            '盘查被解除了我是很高兴，\n',
            '但是……\n',
            '抓犯人的事该怎么办啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '本来还想着\n',
            '以逮捕犯人为纪念\n',
            '发表一下我的新作特制料理呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '唉，\n',
            '等到下次有机会再说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_165E')

    def _loc_15D4(): pass

    label('loc_15D4')

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x000F,
        (
            '呼，盘查解除了呢。\n',
            '无论如何，安心了安心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '不过，犯人怎么样了，\n',
            '却完全没有消息呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '王国军那些家伙\n',
            '一定在全力搜索吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_165E(): pass

    label('loc_165E')

    Jump('loc_1B04')

    def _loc_1661(): pass

    label('loc_1661')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_178C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_16EF',
    )

    ChrTalk(
        0x000F,
        (
            '快点抓到犯人，\n',
            '这个关所就能\n',
            '恢复平时的通行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '……不这样的话，\n',
            '生意也会受到影响的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '哈哈哈，这下可不得了了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1789')

    def _loc_16EF(): pass

    label('loc_16EF')

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x000F,
        (
            '关于那个事件我刚才听说了。\n',
            '蔡斯的人们遇到难题了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '不过，竟然袭击中央工房，\n',
            '真是胆大妄为的家伙呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '这种事情可不是\n',
            '一般的罪犯能做出来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1789(): pass

    label('loc_1789')

    Jump('loc_1B04')

    def _loc_178C(): pass

    label('loc_178C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_18E2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_1857',
    )

    ChrTalk(
        0x000F,
        (
            '我跟你说，\n',
            '那个人在我的店里吃饭……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '他的食量\n',
            '和他的外观一样惊人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '连做饭的材料也都被他吃完了，\n',
            '那天晚上，队长以下的人都得饿肚子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '哈～哈～哈～\n',
            '但愿那个人不要再来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_18DF')

    def _loc_1857(): pass

    label('loc_1857')

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x000F,
        (
            '对了，\n',
            '最近这里来了个很高大的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '看起来是从共和国来的，\n',
            '不过他的体形也太过巨大了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '那种体形看起来\n',
            '简直就和魔兽一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_18DF(): pass

    label('loc_18DF')

    Jump('loc_1B04')

    def _loc_18E2(): pass

    label('loc_18E2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_1A0A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_1984',
    )

    ChrTalk(
        0x000F,
        (
            '唉，小的时候\n',
            '我梦想成为七耀石的输出大王，\n',
            '还要娶很多老婆……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '实际上却沦落到这样偏远的酒馆，\n',
            '我的人生已经没有未来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '啊哈哈哈哈。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A07')

    def _loc_1984(): pass

    label('loc_1984')

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x000F,
        (
            '我也是在\n',
            '共和国出生的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '由于种种原因，\n',
            '现在流落到\n',
            '这样偏远的酒馆来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '哈～哈～哈，\n',
            '我的人生已经一片黑暗了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A07(): pass

    label('loc_1A07')

    Jump('loc_1B04')

    def _loc_1A0A(): pass

    label('loc_1A0A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_1B04',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_1A6D',
    )

    ChrTalk(
        0x000F,
        (
            '欢迎光临\n',
            '这个一成不变的酒馆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '从饮料到简单的饭菜，\n',
            '希望有合你们胃口的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B04')

    def _loc_1A6D(): pass

    label('loc_1A6D')

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x000F,
        (
            '哎呀哎呀，\n',
            '真是欢迎你们的到来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '就像你们看到的，\n',
            '这里是一成不变的关所酒馆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '就算想要长住，\n',
            '也不需要付多余的钱，\n',
            '完全可以放心住下来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1B04(): pass

    label('loc_1B04')

    TalkEnd(0x000F)

    Return()

# id: 0x000A offset: 0x1B08
@scena.Code('func_0A_1B08')
def func_0A_1B08():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_1BB8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_1B5C',
    )

    ChrTurnDirection(0x00FE, 0x000A, 400)

    ChrTalk(
        0x00FE,
        (
            '喂，卡雷尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '差不多要走了，\n',
            '赶快准备好行李吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1BB8')

    def _loc_1B5C(): pass

    label('loc_1B5C')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '嗯，接下来。\n',
            '对了，\n',
            '快点去拿通行许可证吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '到卡尔瓦德还很远，\n',
            '必须早上就出发。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1BB8(): pass

    label('loc_1BB8')

    TalkEnd(0x00FE)

    Return()

# id: 0x000B offset: 0x1BBC
@scena.Code('func_0B_1BBC')
def func_0B_1BBC():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_1F78',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0004, 0x00, 0x10)"),
            (Expr.TestScenaFlags, ScenaFlag(0x00B0, 3, 0x583)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1ED6',
    )

    SetScenaFlags(ScenaFlag(0x00B0, 3, 0x583))
    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哟，好久不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#014F……？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#010F啊，我还以为是谁呢……\n',
            '真的是好久不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#501F嗯？是谁啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F呵呵，就是在洛连特\n',
            '寻找结晶回路碎片的那个孩子啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我们之前不是\n',
            '接受过他的委托去找那碎片吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '已经要回共和国了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '是啊，马上就要走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '其实……\n',
            '我还会再来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我决定等妹妹们\n',
            '稍微再长大一点，\n',
            '就回蔡斯这里来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为做见习生就可以进入工房，\n',
            '将来就可以造飞艇了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我的手很巧，\n',
            '这点连我老妈也是知道的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '这样也挺不错啊。\n',
            '已经找到了将来的目标。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那当然的啦。\n',
            '我也要考虑自己的前途才行呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……唉，\n',
            '不过现在还是要先给老妈帮忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我有四个妹妹，\n',
            '年纪还都很小呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#006F嗯！你要努力帮忙哦。\n',
            '就算是为了你的几个妹妹。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '啊，谢谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '再见了，\n',
            '你们也加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F78')

    def _loc_1ED6(): pass

    label('loc_1ED6')

    ChrTalk(
        0x00FE,
        (
            '……我决定，\n',
            '等我的几个妹妹再长大点之后，\n',
            '就回蔡斯这里来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为做见习生就可以进入工房，\n',
            '将来就可以造飞艇了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我的手很巧，\n',
            '这点连我老妈也是知道的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1F78(): pass

    label('loc_1F78')

    TalkEnd(0x00FE)

    Return()

# id: 0x000C offset: 0x1F7C
@scena.Code('func_0C_1F7C')
def func_0C_1F7C():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_2030',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_1FDF',
    )

    ChrTalk(
        0x00FE,
        (
            '就这样，\n',
            '尽量穿成像利贝尔人的样子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '怎么样？没有哪点不自然吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2030')

    def _loc_1FDF(): pass

    label('loc_1FDF')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '呼，\n',
            '这里已经是利贝尔王国了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，接下来就到蔡斯了，\n',
            '再坚持一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2030(): pass

    label('loc_2030')

    TalkEnd(0x00FE)

    Return()

# id: 0x000D offset: 0x2034
@scena.Code('func_0D_2034')
def func_0D_2034():
    Call(0, 0x0009)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
