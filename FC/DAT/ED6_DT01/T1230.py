import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T1230_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T1230   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'T1230.x'
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
        ('ED6_DT07/CH01150._CH', 'ED6_DT07/CH01150P._CP'),
        ('ED6_DT07/CH01050._CH', 'ED6_DT07/CH01050P._CP'),
        ('ED6_DT07/CH01123._CH', 'ED6_DT07/CH01123P._CP'),
        ('ED6_DT07/CH01023._CH', 'ED6_DT07/CH01023P._CP'),
        ('ED6_DT07/CH01143._CH', 'ED6_DT07/CH01143P._CP'),
        ('ED6_DT07/CH01033._CH', 'ED6_DT07/CH01033P._CP'),
        ('ED6_DT07/CH01630._CH', 'ED6_DT07/CH01630P._CP'),
    ]

# id: 0x10001 offset: 0xE2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '阿波尔',
            x                   = -730,
            z                   = 0,
            y                   = 5300,
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
            name                = '莉莫奈',
            x                   = 440,
            z                   = 0,
            y                   = 32439,
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
            name                = '罗亚',
            x                   = -960,
            z                   = 270,
            y                   = 34690,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x01D5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '贝斯卡',
            x                   = -1680,
            z                   = 270,
            y                   = 32310,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x01D5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '梅洛涅',
            x                   = -1660,
            z                   = 300,
            y                   = 31080,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x01D5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '亚妮拉丝',
            x                   = -700,
            z                   = 0,
            y                   = 35300,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
    )

# id: 0x10002 offset: 0x1A2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x1A2
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x1A2
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -780,
            triggerZ            = 0,
            triggerY            = 4190,
            triggerRange        = 400,
            actorX              = -700,
            actorZ              = 1500,
            actorY              = 5300,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -1500,
            triggerZ            = 0,
            triggerY            = 31600,
            triggerRange        = 400,
            actorX              = 440,
            actorZ              = 1500,
            actorY              = 32439,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x1EA
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_1F4',
    )

    Jump('loc_247')

    def _loc_1F4(): pass

    label('loc_1F4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_212',
    )

    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetFlags(0x0009, 0x0010)

    Jump('loc_247')

    def _loc_212(): pass

    label('loc_212')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 5, 0x31D)),
            Expr.Return,
        ),
        'loc_221',
    )

    ChrClearFlags(0x000D, 0x0080)

    Jump('loc_247')

    def _loc_221(): pass

    label('loc_221')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 4, 0x31C)),
            Expr.Return,
        ),
        'loc_22B',
    )

    Jump('loc_247')

    def _loc_22B(): pass

    label('loc_22B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_247',
    )

    ChrSetPos(0x0009, 1360, 0, 38700, 45)

    Jump('loc_247')

    def _loc_247(): pass

    label('loc_247')

    Return()

# id: 0x0001 offset: 0x248
@scena.Code('func_01_248')
def func_01_248():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_252',
    )

    Jump('loc_27F')

    def _loc_252(): pass

    label('loc_252')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_25C',
    )

    Jump('loc_27F')

    def _loc_25C(): pass

    label('loc_25C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 5, 0x31D)),
            Expr.Return,
        ),
        'loc_266',
    )

    Jump('loc_27F')

    def _loc_266(): pass

    label('loc_266')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 4, 0x31C)),
            Expr.Return,
        ),
        'loc_270',
    )

    Jump('loc_27F')

    def _loc_270(): pass

    label('loc_270')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_27F',
    )

    OP_64(0x01, 0x0001)

    Jump('loc_27F')

    def _loc_27F(): pass

    label('loc_27F')

    Return()

# id: 0x0002 offset: 0x280
@scena.Code('func_02_280')
def func_02_280():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_295',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_280')

    def _loc_295(): pass

    label('loc_295')

    Return()

# id: 0x0003 offset: 0x296
@scena.Code('func_03_296')
def func_03_296():
    TalkBegin(0x0008)
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
            TXT(0x01, '休息\n'),
            TXT(0x02, '离开\n'),
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
        'loc_2F2',
    )

    OP_0D()
    OP_A9(0x0F)
    OP_56(0x00)
    TalkEnd(0x0008)

    Return()

    def _loc_2F2(): pass

    label('loc_2F2')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_303',
    )

    TalkEnd(0x0008)

    Return()

    def _loc_303(): pass

    label('loc_303')

    Call(0, 0x0004)
    ChrSetDirection(0x0008, 180, 0)

    Return()

# id: 0x0004 offset: 0x30F
@scena.Code('func_04_30F')
def func_04_30F():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_367',
    )

    ChrTalk(
        0x0008,
        (
            '我能够与莉莫奈一起\n',
            '开这家店真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我要更加更加努力才行……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_804')

    def _loc_367(): pass

    label('loc_367')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_3C7',
    )

    ChrTalk(
        0x0008,
        (
            '上午莉莫奈会来\n',
            '帮我打扫客房。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '晚上，酒馆很挤的时候，\n',
            '我也会去帮莉莫奈的忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_804')

    def _loc_3C7(): pass

    label('loc_3C7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_427',
    )

    ChrTalk(
        0x0008,
        (
            '莉莫奈一个人\n',
            '在酒馆那边没问题吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '要是她忙不过来的话，\n',
            '我一定要去帮忙……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_804')

    def _loc_427(): pass

    label('loc_427')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 5, 0x31D)),
            Expr.Return,
        ),
        'loc_53B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_503',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '虽然我是个很内向的人，\n',
            '但是我非常喜欢这项工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '有各种各样的人来访，\n',
            '让我增加了许多见识。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我觉得这里\n',
            '真的非常温馨呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '在这里住过一次的人\n',
            '再次来到这里住宿时，\n',
            '我会觉得更加开心……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_538')

    def _loc_503(): pass

    label('loc_503')

    ChrTalk(
        0x0008,
        (
            '虽然我是个很内向的人，\n',
            '但是我非常喜欢这项工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_538(): pass

    label('loc_538')

    Jump('loc_804')

    def _loc_53B(): pass

    label('loc_53B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 4, 0x31C)),
            Expr.Return,
        ),
        'loc_74B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6FE',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '在这个村里，\n',
            '特别是水果成熟的季节，\n',
            '人们都会来果树园体验采摘水果哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 0)

    ChrTalk(
        0x0101,
        (
            '#508F约修亚，可以体验摘水果呢！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#001F我想玩～我想摘～我想吃！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 0)

    ChrTalk(
        0x0102,
        (
            '#018F真是的，你啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#010F但是，现在离那个季节\n',
            '好像还早了一点吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0102, 0)

    ChrTalk(
        0x0008,
        (
            '是、是啊。\n',
            '好像还要过好几个月。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#007F啊～真扫兴……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#001F等到水果成熟的季节，\n',
            '我们再来吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '下次等没有工作的时候再来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F是是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '你在柏斯也说过这些话吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '呵呵呵……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_748')

    def _loc_6FE(): pass

    label('loc_6FE')

    ChrTalk(
        0x0008,
        (
            '在这个村里，\n',
            '特别是水果成熟的季节，\n',
            '人们都会来果树园体验采摘水果哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_748(): pass

    label('loc_748')

    Jump('loc_804')

    def _loc_74B(): pass

    label('loc_74B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_7C7',
    )

    ChrTalk(
        0x0008,
        (
            '那、那个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我、我推荐你们去尝尝\n',
            '二楼酒场的鲜榨果汁，很不错的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '可以的话，\n',
            '请客人务必去品尝一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_804')

    def _loc_7C7(): pass

    label('loc_7C7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_804',
    )

    ChrTalk(
        0x0008,
        (
            '啊，欢、欢迎光临……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '那个……你们要投宿吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_804(): pass

    label('loc_804')

    TalkEnd(0x0008)

    Return()

# id: 0x0005 offset: 0x808
@scena.Code('func_05_808')
def func_05_808():
    Call(0, 0x0006)

    Return()

# id: 0x0006 offset: 0x80D
@scena.Code('func_06_80D')
def func_06_80D():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_883',
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
        1,
        (
            TXT(0x00, '对话\n'),
            TXT(0x01, '买东西\n'),
            TXT(0x02, '离开\n'),
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
        'loc_872',
    )

    OP_0D()
    OP_A9(0x16)
    OP_56(0x00)
    TalkEnd(0x0009)

    Return()

    def _loc_872(): pass

    label('loc_872')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_883',
    )

    TalkEnd(0x0009)

    Return()

    def _loc_883(): pass

    label('loc_883')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_927',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8EE',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x0009,
        (
            '欢迎光临！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '现在店里有\n',
            '用刚摘下来的新鲜水果\n',
            '榨出来的果汁哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '来一杯吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_924')

    def _loc_8EE(): pass

    label('loc_8EE')

    ChrTalk(
        0x0009,
        (
            '现在店里有\n',
            '用刚摘下来的新鲜水果\n',
            '榨出来的果汁哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_924(): pass

    label('loc_924')

    Jump('loc_DE4')

    def _loc_927(): pass

    label('loc_927')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_9AC',
    )

    ChrTalk(
        0x0009,
        (
            '今天好像是\n',
            '村里集会的日子吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '村长早上来的时候，\n',
            '一幅非常烦恼的样子呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '这么忧虑，\n',
            '希望不要弄坏身子才好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DE4')

    def _loc_9AC(): pass

    label('loc_9AC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_9F4',
    )

    ChrTalk(
        0x0009,
        (
            '今、今天\n',
            '客人真是多啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '阿波尔～……\n',
            '来帮帮我吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DE4')

    def _loc_9F4(): pass

    label('loc_9F4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 5, 0x31D)),
            Expr.Return,
        ),
        'loc_A94',
    )

    ChrTalk(
        0x0009,
        (
            '这家店是我和\n',
            '青梅竹马的阿波尔一起开的哦。 ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '当然是我邀请她的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '那个孩子本来很害羞的，\n',
            '我原以为她不适合干这个的，\n',
            '没想到她越做越起劲呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DE4')

    def _loc_A94(): pass

    label('loc_A94')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 4, 0x31C)),
            Expr.Return,
        ),
        'loc_AF9',
    )

    ChrTalk(
        0x0009,
        (
            '唔，菜单里是不是应该再\n',
            '增加一些用水果制成的小点心呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '等会儿和阿波尔商量一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DE4')

    def _loc_AF9(): pass

    label('loc_AF9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_DA0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_D66',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x0009,
        (
            '欢迎光临～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '本店的招牌可是各式的果实酒哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '之所以称得上招牌，\n',
            '是因为我们所采用的原材料都是最新鲜的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F啊呀，听起来很不错……\n',
            '以前没有这家店的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0103, 0)

    ChrTalk(
        0x0009,
        (
            '是啊，我们这家店是最近才开的。\n',
            '以后也请多多关照哦㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F现在有什么好吃的菜\n',
            '可以推荐给我们吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '有呢～今天的特色菜点\n',
            '是石榴酒和杏子水果馅饼套餐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 0)

    ChrTalk(
        0x0101,
        (
            '#509F我说雪拉姐啊，\n',
            '今天不是以调查为首要任务吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x0101, 0)

    ChrTalk(
        0x0103,
        (
            '#020F我知道啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '像这样和当地人聊天\n',
            '也可以得到很多信息嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#020F不要着急，不要着急。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#505F唔～\n',
            '我们真的是在认真调查吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0103, 0)

    ChrTalk(
        0x0102,
        (
            '#019F哈哈，一碰到酒，\n',
            '雪拉姐姐就控制不住自己了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D9D')

    def _loc_D66(): pass

    label('loc_D66')

    ChrTalk(
        0x0009,
        (
            '多吃点多喝点，\n',
            '累了的话可以到下面的旅馆放松一下㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D9D(): pass

    label('loc_D9D')

    Jump('loc_DE4')

    def _loc_DA0(): pass

    label('loc_DA0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_DE4',
    )

    ChrTalk(
        0x0009,
        (
            '啊呀，是客人吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '非常抱歉～\n',
            '现在我们还在准备之中。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_DE4(): pass

    label('loc_DE4')

    TalkEnd(0x0009)

    Return()

# id: 0x0007 offset: 0xDE8
@scena.Code('func_07_DE8')
def func_07_DE8():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_E41',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '这两天，\n',
            '村长准备召开集会\n',
            '讨论栽培的方针。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果有进展就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E8D')

    def _loc_E41(): pass

    label('loc_E41')

    ChrTalk(
        0x00FE,
        (
            '老婆和波波\n',
            '现在都还好吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '也不知道他们\n',
            '在柏斯城里过得顺心吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E8D(): pass

    label('loc_E8D')

    TalkEnd(0x000A)

    Return()

# id: 0x0008 offset: 0xE91
@scena.Code('func_08_E91')
def func_08_E91():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_F9C',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '总是使用\n',
            '古老的方法也不行吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '优先考虑效率，\n',
            '使供货能够源源不断，\n',
            '这种独特想法也是很必要的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这里已经结果的树\n',
            '都比大家的身高要高不少吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这也是我在集会上\n',
            '打算要提出的内容。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只要减少高空的作业，\n',
            '也就不需要这么多人手了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FC7')

    def _loc_F9C(): pass

    label('loc_F9C')

    ChrTalk(
        0x00FE,
        (
            '唉……\n',
            '为什么我的提议他不愿意接受呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_FC7(): pass

    label('loc_FC7')

    TalkEnd(0x000B)

    Return()

# id: 0x0009 offset: 0xFCB
@scena.Code('func_09_FCB')
def func_09_FCB():
    TalkBegin(0x000C)

    ChrTalk(
        0x00FE,
        (
            '我很希望库赖爷爷\n',
            '也能够理解我丈夫的想法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一定会为村子\n',
            '带来好处的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000C)

    Return()

# id: 0x000A offset: 0x1022
@scena.Code('func_0A_1022')
def func_0A_1022():
    TalkBegin(0x000D)
    ChrTurnDirection(0x00FE, 0x0103, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006C, 0, 0x360)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1290',
    )

    SetScenaFlags(ScenaFlag(0x006C, 0, 0x360))
    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))
    ChrTurnDirection(0x00FE, 0x0103, 0)

    ChrTalk(
        0x00FE,
        (
            '#0120021698V#814F啊，难道……\n',
            '这不是雪拉扎德前辈吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120021699V很久不见了啊。\n',
            '自从您去修行之后就再没见面了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030021700V#020F这不是亚妮拉丝吗。\n',
            '你在这里做什么呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0120021701V#810F嗯～\n',
            '协会委托我来这边消灭通缉魔兽。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030021702V#020F是这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021703V对了，\n',
            '你已经找到所谓的剑之道了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0120021704V#819F呵呵，请别问了。\n',
            '我还处在修行阶段呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120021705V#810F说起来，\n',
            '前辈您也是在执行协会的任务吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030021706V#020F是啊，不过我和你的任务性质不同。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0120021707V#810F是这样啊……\n',
            '这个地方最近发生很多事呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120021708V您路上一定要小心哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_13DB')

    def _loc_1290(): pass

    label('loc_1290')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1372',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x0103,
        (
            '#0030021709V#020F啊，这不是亚妮拉丝吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0103, 0)

    ChrTalk(
        0x00FE,
        (
            '#0120021710V#814F啊，雪拉扎德前辈……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120021711V难道前辈也是\n',
            '因为工作才来这儿的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030021712V#020F算是吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0120021713V#810F咱们都挺忙的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_13DB')

    def _loc_1372(): pass

    label('loc_1372')

    ChrTurnDirection(0x00FE, 0x0103, 0)

    ChrTalk(
        0x00FE,
        (
            '#0120021714V#810F雪拉扎德前辈，\n',
            '这个地方最近处于多事之秋。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120021715V您路上一定要小心哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_13DB(): pass

    label('loc_13DB')

    TalkEnd(0x000D)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
