import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
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
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
        ('ED6_DT07/CH01300._CH', 'ED6_DT07/CH01300P._CP'),
        ('ED6_DT07/CH01310._CH', 'ED6_DT07/CH01310P._CP'),
        ('ED6_DT07/CH01300._CH', 'ED6_DT07/CH01300P._CP'),
        ('ED6_DT07/CH01270._CH', 'ED6_DT07/CH01270P._CP'),
        ('ED6_DT07/CH01530._CH', 'ED6_DT07/CH01530P._CP'),
    ]

# id: 0x10001 offset: 0xDA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '士兵布拉姆',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0002,
        ),
        ScenaNpcData(
            name                = '士兵赫宁',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
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
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '格温副队长',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
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
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '布鲁诺',
            x                   = 5990,
            z                   = 0,
            y                   = 9340,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
    )

# id: 0x10002 offset: 0x19A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x19A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x19A
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
            talkFunctionIndex   = 0x0009,
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
    )

# id: 0x0000 offset: 0x1E2
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_200',
    )

    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0009, 3860, 0, 68230, 108)

    def _loc_200(): pass

    label('loc_200')

    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, -51810, 0, 6820, 97)
    ChrClearFlags(0x000C, 0x0080)
    ChrSetPos(0x000C, 6990, 0, 11450, 189)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_23D',
    )

    ChrClearFlags(0x000D, 0x0080)

    def _loc_23D(): pass

    label('loc_23D')

    Return()

# id: 0x0001 offset: 0x23E
@scena.Code('func_01_23E')
def func_01_23E():
    Return()

# id: 0x0002 offset: 0x23F
@scena.Code('func_02_23F')
def func_02_23F():
    TalkBegin(0x00FE)
    TalkEnd(0x00FE)

    Return()

# id: 0x0003 offset: 0x246
@scena.Code('func_03_246')
def func_03_246():
    TalkBegin(0x000D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_2EB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_296',
    )

    ChrTalk(
        0x00FE,
        (
            '圣海姆门也\n',
            '好象有地震啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '幸好没有\n',
            '出现人员伤亡。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2EB')

    def _loc_296(): pass

    label('loc_296')

    ChrTalk(
        0x00FE,
        (
            '听说连圣海姆门那里\n',
            '之前也出现过地震呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '地震如此频繁，\n',
            '实在是不正常啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_2EB(): pass

    label('loc_2EB')

    TalkEnd(0x000D)

    Return()

# id: 0x0004 offset: 0x2EF
@scena.Code('func_04_2EF')
def func_04_2EF():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 0, 0x1410)),
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 1, 0x1411)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_300',
    )

    Call(0, 0x000C)

    Return()

    def _loc_300(): pass

    label('loc_300')

    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_3B7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_35E',
    )

    ChrTalk(
        0x0009,
        (
            '不管怎样，\n',
            '没有地震就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '这样的话又可以恢复到\n',
            '安稳的生活了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3B4')

    def _loc_35E(): pass

    label('loc_35E')

    ChrTalk(
        0x0009,
        (
            '地震好像已经平息了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '中央工房都已经正式声明了，\n',
            '那就肯定可以放心了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_3B4(): pass

    label('loc_3B4')

    Jump('loc_A79')

    def _loc_3B7(): pass

    label('loc_3B7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_458',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_410',
    )

    ChrTalk(
        0x0009,
        (
            '紧急联络\n',
            '好像发来了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '到底是什么事呢，\n',
            '又想知道又不想知道。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_455')

    def _loc_410(): pass

    label('loc_410')

    ChrTalk(
        0x0009,
        (
            '队长的紧急联络\n',
            '好像发来了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '这、这次\n',
            '又出了什么事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_455(): pass

    label('loc_455')

    Jump('loc_A79')

    def _loc_458(): pass

    label('loc_458')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 3, 0x1413)),
            Expr.Return,
        ),
        'loc_56B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_4BA',
    )

    ChrTalk(
        0x0009,
        (
            '我看到的那个可疑男子也好，\n',
            '地震继续发生也好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '好像是发生了什么事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_568')

    def _loc_4BA(): pass

    label('loc_4BA')

    ChrTalk(
        0x0009,
        (
            '呼，不得了了啊。\n',
            '连圣海姆门也发生地震了吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '这样看来的话\n',
            '地震绝对不是偶然啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '我看到的那个可疑男子也好，\n',
            '地震继续发生也好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '好像是发生了什么事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_568(): pass

    label('loc_568')

    Jump('loc_A79')

    def _loc_56B(): pass

    label('loc_56B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 1, 0x1411)),
            Expr.Return,
        ),
        'loc_5B5',
    )

    ChrTalk(
        0x00FE,
        (
            '能把话说出来\n',
            '就痛快多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一会队长那里\n',
            '也拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A79')

    def _loc_5B5(): pass

    label('loc_5B5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 4, 0x140C)),
            Expr.Return,
        ),
        'loc_9CA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 5, 0x140D)),
            Expr.Return,
        ),
        'loc_611',
    )

    ChrTalk(
        0x00FE,
        (
            '对地震的印象太过深刻，\n',
            '其他的事情都给忘了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没帮上忙，真抱歉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9C7')

    def _loc_611(): pass

    label('loc_611')

    ChrTalk(
        0x00FE,
        (
            '嗯，怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_67C',
    )

    ChrTalk(
        0x0106,
        (
            '#050F我们是游击士协会的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '有关３天前的地震，\n',
            '想向你询问一些事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0106, 400)

    Jump('loc_6D1')

    def _loc_67C(): pass

    label('loc_67C')

    ChrTalk(
        0x0103,
        (
            '#020F我们是游击士协会的人哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '有关３天前的地震，\n',
            '有些事想向你打听一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0103, 400)

    def _loc_6D1(): pass

    label('loc_6D1')

    ChrTalk(
        0x00FE,
        (
            '啊啊，那个吗……\n',
            '真是吓了一跳啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这还是第一次遇到地震，\n',
            '当时都不知道发生了什么。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，你们是来\n',
            '调查受害状况的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1015F啊，不是的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '嗯…其实是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '询问对方是否在地震前后\n',
            '发现了什么奇怪的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '啊～奇怪的事情……吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是那么说的话，\n',
            '当然是发生地震最奇怪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1016F啊～不，那当然\n',
            '没错，不过……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '除了地震之外\n',
            '还有没有别的奇异现象发生？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '抱歉，不记得有什么了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对地震的印象太强，\n',
            '之后的事情全都忘记了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1007F啊……是、是吗…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_93A',
    )

    ChrTalk(
        0x0106,
        (
            '#053F这样的话，\n',
            '再问下去也问不出什么了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#051F打扰啦，\n',
            '您继续工作吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0106, 400)

    Jump('loc_98F')

    def _loc_93A(): pass

    label('loc_93A')

    ChrTalk(
        0x0103,
        (
            '#026F那样的话，\n',
            '再问下去也没用了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#027F真是打扰您了，\n',
            '请继续工作吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0103, 400)

    def _loc_98F(): pass

    label('loc_98F')

    ChrTalk(
        0x00FE,
        (
            '啊啊，不好意思啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那，如果有事\n',
            '再来问吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0281, 5, 0x140D))

    def _loc_9C7(): pass

    label('loc_9C7')

    Jump('loc_A79')

    def _loc_9CA(): pass

    label('loc_9CA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_A1C',
    )

    ChrTalk(
        0x00FE,
        (
            '通行手续的话\n',
            '就去对面的建筑吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '和那里的队长说一下\n',
            '就可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A79')

    def _loc_A1C(): pass

    label('loc_A1C')

    ChrTalk(
        0x00FE,
        (
            '哟，怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '通行手续的话\n',
            '就去对面的建筑吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '和那里的队长说一下\n',
            '就可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_A79(): pass

    label('loc_A79')

    TalkEnd(0x0009)

    Return()

# id: 0x0005 offset: 0xA7D
@scena.Code('func_05_A7D')
def func_05_A7D():
    Call(0, 0x0006)

    Return()

# id: 0x0006 offset: 0xA82
@scena.Code('func_06_A82')
def func_06_A82():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 4, 0x140C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A8F',
    )

    Call(0, 0x000B)

    Return()

    def _loc_A8F(): pass

    label('loc_A8F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 2, 0x1412)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 1, 0x1411)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 6, 0x140E)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 7, 0x140F)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_AA8',
    )

    Call(0, 0x000D)

    Return()

    def _loc_AA8(): pass

    label('loc_AA8')

    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_C21',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0218, 1, 0x10C1)),
            Expr.Return,
        ),
        'loc_B24',
    )

    ChrTalk(
        0x000A,
        (
            '士兵们对关不上的大门\n',
            '感到很不安……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '但对比一下哈肯大门那里的情况，\n',
            '这里简直就是轻松的乐园了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C1E')

    def _loc_B24(): pass

    label('loc_B24')

    ChrTalk(
        0x000A,
        (
            '士兵们对关不上的大门\n',
            '感到很不安……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '但对比一下哈肯大门那里的情况，\n',
            '这里简直就是轻松的乐园了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '根本就没有必要\n',
            '那么紧张嘛……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '喔，你们也看看小说\n',
            '放松一下吧！',
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
            (TxtCtl.Item, ItemTable['牌技师杰克 13卷']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_59()
    AddItem(ItemTable['牌技师杰克 13卷'], 1)
    SetScenaFlags(ScenaFlag(0x0218, 1, 0x10C1))

    def _loc_C1E(): pass

    label('loc_C1E')

    Jump('loc_1199')

    def _loc_C21(): pass

    label('loc_C21')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_D8E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_CFC',
    )

    ChrTalk(
        0x000A,
        (
            '呀，各位游击士，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '多亏了那些发生器，\n',
            '通信总算恢复了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '虽然人数不多，但要塞那边\n',
            '派来了增援的士兵。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '马上派他们去亚尔摩村\n',
            '进行巡逻吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '那里离蔡斯比较远，\n',
            '居民们也更加不安呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_D8B')

    def _loc_CFC(): pass

    label('loc_CFC')

    ChrTalk(
        0x000A,
        (
            '增援的士兵们已经被\n',
            '派遣到亚尔摩村了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '那里离蔡斯比较远，\n',
            '居民也会更加不安。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '如果能看到我们王国军过去守卫，\n',
            '多少也能踏实一些吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D8B(): pass

    label('loc_D8B')

    Jump('loc_1199')

    def _loc_D8E(): pass

    label('loc_D8E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_E9C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_DFB',
    )

    ChrTalk(
        0x000A,
        (
            '我们这边也要面对签字仪式，\n',
            '警备不能松懈下来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '算了，反正这里永远也\n',
            '都是这么清闲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E99')

    def _loc_DFB(): pass

    label('loc_DFB')

    ChrTalk(
        0x000A,
        (
            '地震的事件\n',
            '总算是解决了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '虽然还有一些奇怪的事情没搞清楚，\n',
            '不过之后的调查交给协会就可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '我们这边也要面对签字仪式，\n',
            '警备不能松懈下来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_E99(): pass

    label('loc_E99')

    Jump('loc_1199')

    def _loc_E9C(): pass

    label('loc_E9C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_F8D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_EF5',
    )

    ChrTalk(
        0x000A,
        (
            '不过要塞那边\n',
            '好像有准将在吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '既然如此的话\n',
            '就完全不必担心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F8A')

    def _loc_EF5(): pass

    label('loc_EF5')

    ChrTalk(
        0x000A,
        (
            '听说雷斯顿要塞那里\n',
            '也遭到地震的侵袭了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '刚刚才接到那边\n',
            '的联络。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '不过要塞那里\n',
            '好像有准将在吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '既然如此的话\n',
            '就完全不必担心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_F8A(): pass

    label('loc_F8A')

    Jump('loc_1199')

    def _loc_F8D(): pass

    label('loc_F8D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 3, 0x1413)),
            Expr.Return,
        ),
        'loc_1087',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_FF6',
    )

    ChrTalk(
        0x000A,
        (
            '听说圣海姆门那里\n',
            '的受害情况并不严重。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '不过再这样下去的话\n',
            '实在是让人很不安啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1084')

    def _loc_FF6(): pass

    label('loc_FF6')

    ChrTalk(
        0x000A,
        (
            '呀，各位游击士。\n',
            '这一阵子真是很辛苦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '听说圣海姆门那里\n',
            '的受害情况并不严重。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '嗯，即使如此，\n',
            '再这么下去的话也让人放心不下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_1084(): pass

    label('loc_1084')

    Jump('loc_1199')

    def _loc_1087(): pass

    label('loc_1087')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 2, 0x1412)),
            Expr.Return,
        ),
        'loc_1124',
    )

    ChrTalk(
        0x000A,
        (
            '虽然不知道他是否和地震有关联，\n',
            '不过还是很在意那个奇怪的男子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '我也要把情况\n',
            '报告给雷斯顿要塞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '报告给协会的工作\n',
            '就拜托你们各位了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1199')

    def _loc_1124(): pass

    label('loc_1124')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 3, 0x140B)),
            Expr.Return,
        ),
        'loc_1199',
    )

    ChrTalk(
        0x000A,
        (
            '我没有接到什么\n',
            '可疑人物和事件的报告……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '但也许部下们\n',
            '有什么发现吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '可以的话你们去问问他们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1199(): pass

    label('loc_1199')

    TalkEnd(0x000A)

    Return()

# id: 0x0007 offset: 0x119D
@scena.Code('func_07_119D')
def func_07_119D():
    Call(0, 0x0008)

    Return()

# id: 0x0008 offset: 0x11A2
@scena.Code('func_08_11A2')
def func_08_11A2():
    TalkBegin(0x000B)
    TalkEnd(0x000B)

    Return()

# id: 0x0009 offset: 0x11A9
@scena.Code('func_09_11A9')
def func_09_11A9():
    Call(0, 0x000A)

    Return()

# id: 0x000A offset: 0x11AE
@scena.Code('func_0A_11AE')
def func_0A_11AE():
    TalkBegin(0x000C)
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
        'loc_1211',
    )

    OP_0D()
    OP_A9(0xAB)
    OP_56(0x00)
    TalkEnd(0x000C)

    Return()

    def _loc_1211(): pass

    label('loc_1211')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1227',
    )

    OP_0D()
    OP_A9(0xAA)
    OP_56(0x00)
    TalkEnd(0x000C)

    Return()

    def _loc_1227(): pass

    label('loc_1227')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1238',
    )

    TalkEnd(0x000C)

    Return()

    def _loc_1238(): pass

    label('loc_1238')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_1303',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_12C0',
    )

    ChrTalk(
        0x000C,
        (
            '队长一边吃饭\n',
            '一边发呆出神……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '想想的话，应该是哈肯大门\n',
            '发生了什么事吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '这些事情真是\n',
            '不愿意去想啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Jump('loc_1300')

    def _loc_12C0(): pass

    label('loc_12C0')

    ChrTalk(
        0x000C,
        (
            '哈肯大门\n',
            '发生了什么事吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '这些事情真是\n',
            '不愿意去想啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1300(): pass

    label('loc_1300')

    Jump('loc_1C9D')

    def _loc_1303(): pass

    label('loc_1303')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_13D7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_137C',
    )

    ChrTalk(
        0x000C,
        (
            '啊～不是发呆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '看一下就知道了，\n',
            '大门现在敞开着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '现在可以从共和国那边\n',
            '自由出入了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Jump('loc_13D4')

    def _loc_137C(): pass

    label('loc_137C')

    ChrTalk(
        0x000C,
        (
            '想想的话，其实国境线这种东西\n',
            '本来就是人为划定的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '不然根本就没有\n',
            '这些东西的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_13D4(): pass

    label('loc_13D4')

    Jump('loc_1C9D')

    def _loc_13D7(): pass

    label('loc_13D7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_16A0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C8, 0, 0x1640)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0286, 1, 0x1431)),
            Expr.Nez64,
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1527',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_14E7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_145E',
    )

    ChrTalk(
        0x000C,
        (
            '雷斯顿要塞那里好像\n',
            '发生了地震啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '难道是发动政变的那些家伙\n',
            '仍然贼心不死吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_14E4')

    def _loc_145E(): pass

    label('loc_145E')

    ChrTalk(
        0x000C,
        (
            '雷斯顿要塞那里好像\n',
            '发生了地震啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '竟然还专门挑选军用设施，\n',
            '还真是过分啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '难道是发动政变的那些家伙\n',
            '仍然贼心不死吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_14E4(): pass

    label('loc_14E4')

    Jump('loc_1524')

    def _loc_14E7(): pass

    label('loc_14E7')

    ChrTalk(
        0x000C,
        (
            '呼～今天没东西吃了吗，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '才来晚了一会，\n',
            '真是遗憾啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_1524(): pass

    label('loc_1524')

    Jump('loc_169D')

    def _loc_1527(): pass

    label('loc_1527')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_156F',
    )

    OP_62(0x000C, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    OP_63(0x000C)

    ChrTalk(
        0x000C,
        (
            '啊啊！这位客人是！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15C5')

    def _loc_156F(): pass

    label('loc_156F')

    ChrTalk(
        0x000C,
        (
            '嗯……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000C, 0x0108, 500)
    OP_62(0x000C, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    OP_63(0x000C)

    ChrTalk(
        0x000C,
        (
            '啊啊！站在那里的不就是！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_15C5(): pass

    label('loc_15C5')

    ChrTalk(
        0x0108,
        (
            '#071F哈哈，好久不见了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '正好到这附近办事，\n',
            '顺路过来看看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '要、要吃些东西吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#070F不了，现在没有\n',
            '空闲，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '不能待太久。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '是、是吗…\n',
            '没办法，以后有机会的话一定再来啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#070F喔！没问题！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x02C8, 0, 0x1640))
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    def _loc_169D(): pass

    label('loc_169D')

    Jump('loc_1C9D')

    def _loc_16A0(): pass

    label('loc_16A0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_17C2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_1713',
    )

    ChrTalk(
        0x000C,
        (
            '那个大块头的客人\n',
            '看起来好像也是共和国的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '我也是出身于那里，\n',
            '看一眼他的服装就知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17BF')

    def _loc_1713(): pass

    label('loc_1713')

    ChrTalk(
        0x000C,
        (
            '忘了具体是哪天了，\n',
            '来了一位身材巨大的客人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '那位客人的食量就如同\n',
            '他的外表一样惊人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '店里的食物全都\n',
            '被他吃光了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '哈哈哈。\n',
            '那个客人后来就没再来过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0286, 1, 0x1431))
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_17BF(): pass

    label('loc_17BF')

    Jump('loc_1C9D')

    def _loc_17C2(): pass

    label('loc_17C2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 3, 0x1413)),
            Expr.Return,
        ),
        'loc_1895',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_184A',
    )

    ChrTalk(
        0x000C,
        (
            '这里的客人本来\n',
            '就很少了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '地震的事情要是再传开\n',
            '生意就更要进入冰点了，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '哈哈哈～\n',
            '看来我也该去冬眠了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1892')

    def _loc_184A(): pass

    label('loc_184A')

    ChrTalk(
        0x000C,
        (
            '不知为什么，队长他们\n',
            '的脸色都不太好哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '还有什么问题吗～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_1892(): pass

    label('loc_1892')

    Jump('loc_1C9D')

    def _loc_1895(): pass

    label('loc_1895')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 4, 0x140C)),
            Expr.Return,
        ),
        'loc_1BD3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 7, 0x140F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1B86',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))
    SetScenaFlags(ScenaFlag(0x0281, 7, 0x140F))

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 6, 0x140E)),
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 1, 0x1411)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_18BE',
    )

    OP_28(0x0085, 0x01, 0x0800)

    Jump('loc_18BE')

    def _loc_18BE(): pass

    label('loc_18BE')

    ChrTalk(
        0x000C,
        (
            '啊，欢迎光临～\n',
            '这里是间没有任何特色的酒馆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1000F啊～可以稍微打扰一下吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000C, 0x0101, 400)

    ChrTalk(
        0x000C,
        (
            '好，什么事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1011F啊，我们是\n',
            '游击士协会的人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '希望您能配合我们\n',
            '做个调查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '啊，当然可以。\n',
            '反正现在一个客人也没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '询问对方是否在地震前后\n',
            '发现了什么奇怪的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x000C,
        (
            '啊～除了地震之外就没有\n',
            '什么奇怪的事情发生了～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '地震刚来的时候\n',
            '大家都很吃惊呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#044F那地震前后\n',
            '也没有奇怪的事情发生吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000C, 0x0105, 400)

    ChrTalk(
        0x000C,
        (
            '嗯…奇怪的事情…\n',
            '实在是想不起来啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '哈，最奇怪的事情也就是\n',
            '我一直留在店里没出去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1015F啊、是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0101, 400)

    ChrTalk(
        0x0105,
        (
            '#043F……看来是没有什么\n',
            '值得注意的情报啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '不能帮上你忙十分抱歉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1016F哪里，不用介意。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1000F谢谢您的配合。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1BD0')

    def _loc_1B86(): pass

    label('loc_1B86')

    ChrTalk(
        0x000C,
        (
            '我觉得，\n',
            '没什么太奇怪的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '无论发生什么，\n',
            '我一直都会在店里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_1BD0(): pass

    label('loc_1BD0')

    Jump('loc_1C9D')

    def _loc_1BD3(): pass

    label('loc_1BD3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1C49',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x000C,
        (
            '恭候各位的光临。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '如你们所见，\n',
            '这里是家没有任何特色的酒馆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '嘿，有需要的话\n',
            '就多来坐坐吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C9D')

    def _loc_1C49(): pass

    label('loc_1C49')

    ChrTalk(
        0x000C,
        (
            '啊，欢迎光临～\n',
            '这里是间没有任何特色的酒馆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '嘿，有需要的话\n',
            '就多来坐坐吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C9D(): pass

    label('loc_1C9D')

    TalkEnd(0x000C)

    Return()

# id: 0x000B offset: 0x1CA1
@scena.Code('func_0B_1CA1')
def func_0B_1CA1():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1CB2',
    )

    Call(0, 0x000E)

    def _loc_1CB2(): pass

    label('loc_1CB2')

    EventBegin(0x00)
    OP_4A(0x000A, 255)
    Fade(1000)
    ChrSetPos(0x0101, -49720, 0, 6390, 270)
    ChrSetPos(0x00F7, -49720, 0, 7460, 270)
    ChrSetPos(0x0104, -48400, 0, 7020, 270)
    ChrSetPos(0x0105, -49010, 0, 5660, 270)
    CameraMove(-50310, 0, 6810, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_0D()

    ChrTalk(
        0x000A,
        (
            '#3060220846V#6P啊，你们是游击士吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3060220847V#6P协会通知过我们，\n',
            '这次是来调查『地震』的事吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220848V#1004F啊，是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010220849V#1016F真不愧是雾香姐，\n',
            '安排得这么周到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3060220850V#6P哈哈，我们平时也是多次\n',
            '承蒙她的帮助呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3060220851V#6P你们的调查工作\n',
            '我一定会全力配合的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_1EDF',
    )

    ChrTalk(
        0x0106,
        (
            '#0050220852V#051F那可谢谢了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050220853V那可以先把地震的发生情况\n',
            '详细地说给我们听吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F3D')

    def _loc_1EDF(): pass

    label('loc_1EDF')

    ChrTalk(
        0x0103,
        (
            '#0030220854V#020F那就谢谢啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030220855V那可以先把地震的发生情况\n',
            '详细说给我们听听吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1F3D(): pass

    label('loc_1F3D')

    ChrTalk(
        0x000A,
        (
            '#3060220856V#6P这个啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3060220857V#6P地震的发生时间\n',
            '大概是３天前的下午５点左右。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3060220858V#6P震动并不算太强烈，\n',
            '而且只持续了１０秒而已……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3060220859V#6P但这里以前从没发生过地震，\n',
            '所以在军中还是引起了不小的骚动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3060220860V#6P之后，当天夜里──',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3060220861V#6P在我们和雷斯顿要塞进行定期联络时，\n',
            '发现了一个奇妙的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060220862V#043F是不是其他的地方\n',
            '完全没有发生地震？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3060220863V#6P啊，正是如此。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3060220864V#6P不但雷斯顿要塞没有发生地震，\n',
            '连圣海姆门那边也没有任何震动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3060220865V#6P蔡斯市和亚尔摩村\n',
            '也都一样没有发生任何地震。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220866V#1002F原来如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010220867V对了，今天蔡斯市发生地震了，\n',
            '您听说了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3060220868V#6P啊，这个已经听说了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3060220869V#6P只是这次我们这边\n',
            '完全没有任何摇晃。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040220870V#035F#2P范围极端狭小，\n',
            '而且场所会转移的局部地震吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040220871V#030F果然是非常诡异啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_2357',
    )

    ChrTalk(
        0x0106,
        (
            '#0050220872V#053F地震的情况我们已经了解了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050220873V#050F除此之外还有没有发生过\n',
            '什么不正常的事件？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050220874V比如看见过奇怪的人之类的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23F0')

    def _loc_2357(): pass

    label('loc_2357')

    ChrTalk(
        0x0103,
        (
            '#0030220875V#026F地震的情况我们已经了解啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030220876V#022F除此以外还有什么\n',
            '值得注意的事情发生吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030220877V比如目击到什么可疑人物之类的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_23F0(): pass

    label('loc_23F0')

    ChrTalk(
        0x000A,
        (
            '#3060220878V#6P嗯……\n',
            '我没有收到什么重要的报告。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3060220879V#6P不过也许我的部下们\n',
            '有什么发现吧，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3060220880V#6P你们自己去问问就可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220881V#1006F嗯，多谢您了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010220882V我们这就去向\n',
            '士兵们打听一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0281, 4, 0x140C))
    OP_28(0x0085, 0x01, 0x0040)
    OP_28(0x0085, 0x01, 0x0080)
    OP_4B(0x000A, 255)
    EventEnd(0x00)

    Return()

# id: 0x000C offset: 0x24F2
@scena.Code('func_0C_24F2')
def func_0C_24F2():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2503',
    )

    Call(0, 0x000E)

    def _loc_2503(): pass

    label('loc_2503')

    EventBegin(0x00)
    OP_4A(0x0009, 255)
    Fade(1000)
    ChrSetPos(0x0105, 6250, 0, 69020, 270)
    ChrSetPos(0x0101, 5250, 0, 68630, 270)
    ChrSetPos(0x00F7, 5320, 0, 67540, 270)
    ChrSetPos(0x0104, 6400, 0, 67950, 270)
    CameraMove(4490, 0, 68450, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 5, 0x140D)),
            Expr.Return,
        ),
        'loc_25F7',
    )

    ChrTalk(
        0x0009,
        (
            '#5P啊，还有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220927V#1002F#2P嗯，我们从布拉姆\n',
            '那里听到了一些情报……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_27CB')

    def _loc_25F7(): pass

    label('loc_25F7')

    ChrTalk(
        0x0009,
        (
            '#3070220919V#5P嗯，有什么事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_2686',
    )

    ChrTalk(
        0x0106,
        (
            '#0050220920V#051F我们是游击士协会的人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050220921V有关３天前的地震，\n',
            '想向你询问一些事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_26EA')

    def _loc_2686(): pass

    label('loc_2686')

    ChrTalk(
        0x0103,
        (
            '#0030220922V#020F我们是游击士协会的人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030220923V有关３天前的地震，\n',
            '有些事想向你打听一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_26EA(): pass

    label('loc_26EA')

    ChrTalk(
        0x0009,
        (
            '#3070220924V#5P啊啊，那个吗……\n',
            '真是吓了一跳啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3070220925V#5P地震还是第一次遇到，\n',
            '当时都不知道发生了什么。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3070220926V#5P嗯，还想问什么吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220927V#1002F#2P嗯，我们从布拉姆\n',
            '那里听到了一些情报……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_27CB(): pass

    label('loc_27CB')

    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '把门卫布拉姆所说的话\n',
            '告诉赫宁。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x0009,
        (
            '#3070220929V#5P啊，是那件事啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3070220930V#5P嗯，我确实是那么\n',
            '问过他。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060220931V#040F就是『有没有人\n',
            '通过大门？』对吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3070220932V#5P嗯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3070220933V#5P在４天前……\n',
            '也就是地震发生的前一天。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3070220934V#5P我值班结束，正要回休息所的时候，\n',
            '忽然看到从街道那边走来一名奇怪的男子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220935V#1004F#2P奇怪的男子……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040220936V#030F#6P是不是一个戴着面具，\n',
            '身穿白衣的男子？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3070220937V#5P面、面具？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3070220938V#5P就算是奇怪\n',
            '也不会奇怪到那种程度啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3070220939V#5P是个身穿黑色外套，\n',
            '个子很高的男人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3070220940V#5P而且还戴着黑色的眼镜。',
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
        'loc_2B12',
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
            TXT(0x00, '【◇在蔡斯看过瓦鲁特的情报】\n'),
            TXT(0x01, '【◇没有在蔡斯看过瓦鲁特的情报】\n'),
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
        (0x00000000, 'loc_2AFD'),
        (0x00000001, 'loc_2B03'),
        (-1, 'loc_2B09'),
    )

    def _loc_2AFD(): pass

    label('loc_2AFD')

    SetScenaFlags(ScenaFlag(0x0290, 0, 0x1480))

    Jump('loc_2B09')

    def _loc_2B03(): pass

    label('loc_2B03')

    ClearScenaFlags(ScenaFlag(0x0290, 0, 0x1480))

    Jump('loc_2B09')

    def _loc_2B09(): pass

    label('loc_2B09')

    FadeIn(300, 0)

    def _loc_2B12(): pass

    label('loc_2B12')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0290, 0, 0x1480)),
            Expr.Return,
        ),
        'loc_2C30',
    )

    ChrTalk(
        0x0101,
        (
            '#0010220941V#1004F#2P黑色的眼镜……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010220942V那个好像是叫做\n',
            '墨镜是吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0085, 0x01, 0x0200)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_2BD3',
    )

    ChrTalk(
        0x0106,
        (
            '#0050220943V#555F啊啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050220944V那种东西很稀有，\n',
            '看来和之前听说的是同一个人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2C2D')

    def _loc_2BD3(): pass

    label('loc_2BD3')

    ChrTalk(
        0x0103,
        (
            '#0030220945V#022F嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030220946V这种东西很少见，\n',
            '看来和之前听说的是同一个人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2C2D(): pass

    label('loc_2C2D')

    Jump('loc_2FC3')

    def _loc_2C30(): pass

    label('loc_2C30')

    ChrTalk(
        0x0101,
        (
            '#0010220947V#1015F#2P黑色的眼镜……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010220948V是指镜架是\n',
            '黑颜色的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3070220949V#5P不、不是这样的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3070220950V#5P镜片的部分\n',
            '也是纯黑的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220951V#1004F#2P那、那样的话\n',
            '岂不是看不见前边了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0085, 0x01, 0x0400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_2DB5',
    )

    ChrTalk(
        0x0106,
        (
            '#0050220952V#555F那个东西…\n',
            '大概就是所谓的『墨镜』了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050220953V据说那东西可以\n',
            '挡住强烈的日光照射。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050220954V而且还不会影响\n',
            '前方的视线。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2E71')

    def _loc_2DB5(): pass

    label('loc_2DB5')

    ChrTalk(
        0x0103,
        (
            '#0030220955V#020F那大概就是传闻中一种\n',
            '叫做墨镜的眼镜了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030220956V据说那东西\n',
            '有着抵挡太阳光的功效，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030220957V虽然戴上那个后视线多少会受一些影响，\n',
            '但看清楚前方还是没问题的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2E71(): pass

    label('loc_2E71')

    ChrTalk(
        0x0104,
        (
            '#0040220958V#035F#6P我也听说过那个，\n',
            '不过可不是随便就能搞到的东西啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040220959V#030F在帝都的黑街上倒是看见\n',
            '黑道的头目们戴过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220960V#1007F#2P真、真是听起来就危险的东西呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0104, 400)

    ChrTalk(
        0x0101,
        (
            '#0010220961V#1019F#5P可话说回来，你为什么会\n',
            '认识那些危险的人物呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040220962V#031F#6P哼哼……\n',
            '常言道『蛇走蛇道，鬼走鬼道』嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_2FC3(): pass

    label('loc_2FC3')

    ChrTalk(
        0x0009,
        (
            '#3070220963V#5P啊，原来那个奇怪的黑眼镜\n',
            '叫做墨镜啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0009, 400)

    ChrTalk(
        0x0009,
        (
            '#3070220964V#5P我继续说刚才的话，就在我要进休息所时，\n',
            '忽然看见那家伙从街道那边走来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3070220965V#5P一般来说，途经这里的人\n',
            '都会进这酒馆里休息一下，所以我\n',
            '以为他很快就会进来，就先进去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060220966V#043F可是……\n',
            '那个人就再没出现，对吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3070220967V#5P啊啊，正是如此。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3070220968V#5P然后我就去问布拉姆，\n',
            '结果他也说没有人通过……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3070220969V#5P那家伙虽然经常偷懒打磕睡，\n',
            '但毕竟不至于连有人通过大门\n',
            '都察觉不到啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040220970V#030F#6P嗯，但也有可能是他\n',
            '直接去了兵舍那边吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040220971V也许他是有事找队长呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3070220972V#5P我当时感到很蹊跷，\n',
            '就去问过了队长和副队长。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3070220973V#5P但他们都说那一段时间内\n',
            '没人来访过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3070220974V#5P可这样的话，我看见的那个男人\n',
            '到底是来干什么的呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3070220975V#5P每次一想起这件事\n',
            '我的头脑就一片混乱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220976V#1002F#2P嗯…确实是个很奇怪的家伙呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010220977V我们就把这件事\n',
            '报告给雾香姐吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_33DD',
    )

    ChrTalk(
        0x0106,
        (
            '#0050220978V#053F啊……\n',
            '就那么办吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050220979V#051F多谢您提供的情报啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_342C')

    def _loc_33DD(): pass

    label('loc_33DD')

    ChrTalk(
        0x0103,
        (
            '#0030220980V#020F嗯……\n',
            '就这么办吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030220981V#021F感谢您提供的情报。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_342C(): pass

    label('loc_342C')

    ChrTalk(
        0x0009,
        (
            '#3070220982V#5P哪里哪里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3070220983V#5P你们来问这些，\n',
            '我也松了口气呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0282, 1, 0x1411))

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 6, 0x140E)),
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 7, 0x140F)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3496',
    )

    OP_28(0x0085, 0x01, 0x0800)

    Jump('loc_3496')

    def _loc_3496(): pass

    label('loc_3496')

    OP_4B(0x0009, 255)
    EventEnd(0x00)

    Return()

# id: 0x000D offset: 0x349D
@scena.Code('func_0D_349D')
def func_0D_349D():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_34AE',
    )

    Call(0, 0x000E)

    def _loc_34AE(): pass

    label('loc_34AE')

    EventBegin(0x00)
    OP_4A(0x000A, 255)
    Fade(1000)
    ChrSetPos(0x0101, -49720, 0, 6390, 270)
    ChrSetPos(0x00F7, -49720, 0, 7460, 270)
    ChrSetPos(0x0104, -48400, 0, 7020, 270)
    ChrSetPos(0x0105, -49010, 0, 5660, 270)
    CameraMove(-50310, 0, 6810, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_0D()

    ChrTalk(
        0x000A,
        (
            '#3060220990V#6P啊，是你们啊。\n',
            '从部下那里打探到了什么有用的情报吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220991V#1002F嗯，其实……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '把有关墨镜男子的目击情报\n',
            '报告给了队长。',
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
            '#3060220992V#6P嗯…赫宁那小子，\n',
            '看见了那样的男子啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3060220993V#6P虽然还不知道他是否和地震\n',
            '有关系，不过确实是个很可疑的男人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3060220994V#6P那我们这边也\n',
            '报告给雷斯顿要塞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_375A',
    )

    ChrTalk(
        0x0106,
        (
            '#0050220995V#050F啊，那就拜托啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0106, 0x0101, 400)

    ChrTalk(
        0x0106,
        (
            '#0050220996V#051F那么……\n',
            '这里的调查就算是告一段落了，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050220997V这就回蔡斯\n',
            '向雾香报告吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_37E7')

    def _loc_375A(): pass

    label('loc_375A')

    ChrTalk(
        0x0103,
        (
            '#0030220998V#020F嗯，拜托您了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030220999V#526F那么……\n',
            '这里的调查算是完成了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030221000V我们这就回蔡斯\n',
            '向雾香报告吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_37E7(): pass

    label('loc_37E7')

    ChrTurnDirection(0x0101, 0x00F7, 400)

    ChrTalk(
        0x0101,
        (
            '#0010221001V#1006F#4P嗯！了解。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4B(0x000A, 255)
    SetScenaFlags(ScenaFlag(0x0282, 2, 0x1412))
    OP_28(0x0085, 0x01, 0x1000)
    EventEnd(0x00)

    Return()

# id: 0x000E offset: 0x3823
@scena.Code('func_0E_3823')
def func_0E_3823():
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
        (0x00000000, 'loc_389D'),
        (0x00000001, 'loc_38A3'),
        (-1, 'loc_38A9'),
    )

    def _loc_389D(): pass

    label('loc_389D')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_38A9')

    def _loc_38A3(): pass

    label('loc_38A3')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_38A9')

    def _loc_38A9(): pass

    label('loc_38A9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_38B7',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    Jump('loc_38BB')

    def _loc_38B7(): pass

    label('loc_38B7')

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    def _loc_38BB(): pass

    label('loc_38BB')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
