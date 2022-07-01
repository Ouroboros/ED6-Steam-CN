import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T4101_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4101_1 ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4101.x'
    header.mapIndex       = 1
    header.bgm            = 14
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT21/T4101._SN', 'ED6_DT21/T4101_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x93C6
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
    ]

# id: 0x10002 offset: 0xA8
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10003 offset: 0xA8
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0xA8
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0xA8
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0xA8
@scena.Code('PreInit')
def PreInit():
    Return()

# id: 0x0001 offset: 0xA9
@scena.Code('Init')
def Init():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02D1, 2, 0x168A)),
            Expr.Return,
        ),
        'loc_11B',
    )

    ChrTalk(
        0x00FE,
        (
            '#0070250410V#063F阿加特哥哥为什么\n',
            '不一起吃冰淇淋？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070250411V等我长大了他\n',
            '会不会和我一起吃？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_343')

    def _loc_11B(): pass

    label('loc_11B')

    ChrTalk(
        0x00FE,
        (
            '#0070250412V#563F这里的冰淇淋\n',
            '明明这么好吃……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070250413V#063F阿加特哥哥为什么\n',
            '不一起吃？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070250414V#064F啊……难道他\n',
            '讨厌冰淇淋？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250415V#1016F我倒不这么认为。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250416V#1007F按照阿加特的性格，\n',
            '肯定是因为害羞而逞强。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 300)

    ChrTalk(
        0x00FE,
        (
            '#0070250417V#065F难、难道是因为要\n',
            '和我这样的孩子一起的关系？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070250418V那个那个……那么等我长大了\n',
            '他会不会和我一起吃？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250419V#1016F这、这个么……\n',
            '去问问他本人如何？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250420V#1015F不过，长大后的提妲啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250421V#1016F给阿加特可能太浪费了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0070250422V#065F啊啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x168A)

    def _loc_343(): pass

    label('loc_343')

    TalkEnd(0x00FE)

    Return()

# id: 0x0002 offset: 0x347
@scena.Code('ReInit')
def ReInit():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02D1, 1, 0x1689)),
            Expr.Return,
        ),
        'loc_387',
    )

    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '#0220250423V#261F赶紧完成工作\n',
            '回来哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_49F')

    def _loc_387(): pass

    label('loc_387')

    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '#0220250424V#260F啊，姐姐。\n',
            '工作还没结束？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250425V#1000F很快就好了，\n',
            '你再稍微等会儿？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250426V等我去利贝尔通讯\n',
            '调查完就回协会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0220250427V#264F真的？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220250428V#265F那在此之前\n',
            '我们就回去等着了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250429V#1001F晚饭大伙儿\n',
            '一起吃吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1689)

    def _loc_49F(): pass

    label('loc_49F')

    TalkEnd(0x00FE)

    Return()

# id: 0x0003 offset: 0x4A3
@scena.Code('func_03_4A3')
def func_03_4A3():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_4E5',
    )

    ChrTalk(
        0x00FE,
        (
            '去下水道有事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '进去是可以，\n',
            '不过要小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_685')

    def _loc_4E5(): pass

    label('loc_4E5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_520',
    )

    ChrTalk(
        0x00FE,
        (
            '去下水道有事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '游击士倒是\n',
            '可以进去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_685')

    def _loc_520(): pass

    label('loc_520')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_577',
    )

    ChrTalk(
        0x00FE,
        (
            '哎呀，你们是游击士吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我听说通缉魔兽的事了。\n',
            '不用客气，请过去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_685')

    def _loc_577(): pass

    label('loc_577')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5C7',
    )

    ChrTalk(
        0x00FE,
        (
            '很遗憾，不能\n',
            '让你们进去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果要训练的话\n',
            '请去别的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_685')

    def _loc_5C7(): pass

    label('loc_5C7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_60C',
    )

    ChrTalk(
        0x00FE,
        (
            '去下水道有事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不好意思，暂时不能\n',
            '让你们进去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_685')

    def _loc_60C(): pass

    label('loc_60C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_685',
    )

    ChrTalk(
        0x00FE,
        (
            '这条下水道现在被封锁了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为最近来王都的\n',
            '外国人增加。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为了不让他们乱闯，\n',
            '为慎重起见就在此警戒了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_685(): pass

    label('loc_685')

    TalkEnd(0x00FE)

    Return()

# id: 0x0004 offset: 0x689
@scena.Code('func_04_689')
def func_04_689():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_87D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x041B, 1, 0x20D9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_86E',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7A1',
    )

    ChrTalk(
        0x00FE,
        (
            '这不是金先生吗？\n',
            '请进请进！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#070F嗯，谢谢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '在这种情况下大使馆的\n',
            '那帮家伙也很忙吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是啊，特别是\n',
            '爱尔莎大使，为了了解情况\n',
            '好像在到处跑呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '她想问你们一些事，\n',
            '所以告诉我如果各位游击士\n',
            '来了就领进来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1000F哟，是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_868')

    def _loc_7A1(): pass

    label('loc_7A1')

    ChrTalk(
        0x00FE,
        (
            '请进吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1004F咦？方便吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '爱尔莎大使说你们来了\n',
            '就请进来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1015F唔，到底是怎么了呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看来为了了解情况\n',
            '而想和各种人聊聊呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1000F哦，原来如此……\n',
            '那么我们就不客气了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_868(): pass

    label('loc_868')

    OP_A2(0x20D9)

    Jump('loc_87A')

    def _loc_86E(): pass

    label('loc_86E')

    ChrTalk(
        0x00FE,
        (
            '请进。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_87A(): pass

    label('loc_87A')

    Jump('loc_103D')

    def _loc_87D(): pass

    label('loc_87D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_B0A',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_AA5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_8A8',
    )

    ChrTalk(
        0x0008,
        (
            '请进。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_AA2')

    def _loc_8A8(): pass

    label('loc_8A8')

    EventBegin(0x00)
    Fade(1000)
    SetChrPos(0x0108, 70570, 0, -7070, 180)
    SetChrPos(0x0101, 70550, 0, -5430, 180)

    If(
        (
            (Expr.Eval, "OP_CB(0xF7)"),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8F2',
    )

    SetChrPos(0x0106, 69580, 0, -4260, 180)

    Jump('loc_903')

    def _loc_8F2(): pass

    label('loc_8F2')

    SetChrPos(0x0103, 69580, 0, -4260, 180)

    def _loc_903(): pass

    label('loc_903')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_924',
    )

    SetChrPos(0x00F9, 70970, 0, -4310, 180)

    Jump('loc_935')

    def _loc_924(): pass

    label('loc_924')

    SetChrPos(0x00F8, 70970, 0, -4310, 180)

    def _loc_935(): pass

    label('loc_935')

    OP_6D(71710, 0, -7860, 0)
    OP_67(0, 5770, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(129000, 0)
    OP_6E(262, 0)
    OP_8C(0x0008, 0, 0)
    SetChrSubChip(0x0008, 0)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#2P金先生，你要进大使馆吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#070F啊啊，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0008, 180, 400)
    OP_22(0x0073, 0x00, 0x64)
    Sleep(500)

    OP_6F(0x000A, 0)
    OP_70(0x000A, 0x0000003C)
    Sleep(1000)

    OP_8E(0x0008, 68770, 250, -9000, 3000, 0x00)
    OP_8C(0x0008, 0, 400)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#2P请进。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(500)
    OP_6D(71150, 0, -6670, 0)
    OP_67(0, 10000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0000, 71150, 0, -6670, 180)
    SetChrPos(0x0001, 71150, 0, -6670, 180)
    SetChrPos(0x0002, 71150, 0, -6670, 180)
    SetChrPos(0x0003, 71150, 0, -6670, 180)
    OP_69(0x0000, 0x00000000)
    OP_0D()
    OP_A2(0x0003)
    EventEnd(0x00)

    def _loc_AA2(): pass

    label('loc_AA2')

    Jump('loc_B07')

    def _loc_AA5(): pass

    label('loc_AA5')

    ChrTalk(
        0x00FE,
        (
            '潜伏在港口的\n',
            '情报部余党好像被抓住了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在签字仪式前减少了一个不\n',
            '安因素，让人松了口气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_B07(): pass

    label('loc_B07')

    Jump('loc_103D')

    def _loc_B0A(): pass

    label('loc_B0A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_D78',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D32',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_B35',
    )

    ChrTalk(
        0x0008,
        (
            '请进。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D2F')

    def _loc_B35(): pass

    label('loc_B35')

    EventBegin(0x00)
    Fade(1000)
    SetChrPos(0x0108, 70570, 0, -7070, 180)
    SetChrPos(0x0101, 70550, 0, -5430, 180)

    If(
        (
            (Expr.Eval, "OP_CB(0xF7)"),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B7F',
    )

    SetChrPos(0x0106, 69580, 0, -4260, 180)

    Jump('loc_B90')

    def _loc_B7F(): pass

    label('loc_B7F')

    SetChrPos(0x0103, 69580, 0, -4260, 180)

    def _loc_B90(): pass

    label('loc_B90')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_BB1',
    )

    SetChrPos(0x00F9, 70970, 0, -4310, 180)

    Jump('loc_BC2')

    def _loc_BB1(): pass

    label('loc_BB1')

    SetChrPos(0x00F8, 70970, 0, -4310, 180)

    def _loc_BC2(): pass

    label('loc_BC2')

    OP_6D(71710, 0, -7860, 0)
    OP_67(0, 5770, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(129000, 0)
    OP_6E(262, 0)
    OP_8C(0x0008, 0, 0)
    SetChrSubChip(0x0008, 0)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#2P金先生，你要进大使馆吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#070F啊啊，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0008, 180, 400)
    OP_22(0x0073, 0x00, 0x64)
    Sleep(500)

    OP_6F(0x000A, 0)
    OP_70(0x000A, 0x0000003C)
    Sleep(1000)

    OP_8E(0x0008, 68770, 250, -9000, 3000, 0x00)
    OP_8C(0x0008, 0, 400)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#2P请进。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(500)
    OP_6D(71150, 0, -6670, 0)
    OP_67(0, 10000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0000, 71150, 0, -6670, 180)
    SetChrPos(0x0001, 71150, 0, -6670, 180)
    SetChrPos(0x0002, 71150, 0, -6670, 180)
    SetChrPos(0x0003, 71150, 0, -6670, 180)
    OP_69(0x0000, 0x00000000)
    OP_0D()
    OP_A2(0x0003)
    EventEnd(0x00)

    def _loc_D2F(): pass

    label('loc_D2F')

    Jump('loc_D75')

    def _loc_D32(): pass

    label('loc_D32')

    ChrTalk(
        0x00FE,
        (
            '……穿着白色礼服的女孩子啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没印象，\n',
            '不过肯定不在里面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_D75(): pass

    label('loc_D75')

    Jump('loc_103D')

    def _loc_D78(): pass

    label('loc_D78')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_DE7',
    )

    ChrTalk(
        0x00FE,
        (
            '前不久爱尔莎大使和\n',
            '帝国的达维尔大使\n',
            '在这里撞见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我清清楚楚地闻见两人\n',
            '之间的火药味。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_103D')

    def _loc_DE7(): pass

    label('loc_DE7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_ECC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 5, 0x161D)),
            Expr.Return,
        ),
        'loc_E67',
    )

    ChrTalk(
        0x00FE,
        (
            '各位见到\n',
            '爱尔莎大使了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '爱尔莎大使从以前起\n',
            '就是个有点可怕的人哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有时候也会让\n',
            '客人吃闭门羹。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EC9')

    def _loc_E67(): pass

    label('loc_E67')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 3, 0x161B)),
            Expr.Return,
        ),
        'loc_EC5',
    )

    ChrTalk(
        0x00FE,
        (
            '请进。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊，因为大使馆的领域内\n',
            '拥有治外法权，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '言行举止请\n',
            '谨慎一些哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EC9')

    def _loc_EC5(): pass

    label('loc_EC5')

    Call(0, 0x000B)

    def _loc_EC9(): pass

    label('loc_EC9')

    Jump('loc_103D')

    def _loc_ECC(): pass

    label('loc_ECC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_103D',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_FED',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02CD, 4, 0x166C)),
            Expr.Return,
        ),
        'loc_F1C',
    )

    ChrTalk(
        0x0008,
        (
            '金先生要是来了\n',
            '爱尔莎大使一定会感到高兴的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FEA')

    def _loc_F1C(): pass

    label('loc_F1C')

    ChrTalk(
        0x0108,
        (
            '#071F哟，兄弟，好久不见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '咦？\n',
            '这不是金先生吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '你又来利贝尔\n',
            '玩了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#070F哈哈，也差不多吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '接下来会有一阵子\n',
            '要面对些麻烦，\n',
            '要请你帮忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '明白！\n',
            '爱尔莎大使一定会感到高兴的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x166C)

    def _loc_FEA(): pass

    label('loc_FEA')

    Jump('loc_103D')

    def _loc_FED(): pass

    label('loc_FED')

    ChrTalk(
        0x00FE,
        (
            '等等哦，这里是\n',
            '卡尔瓦德共和国大使馆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '抱歉，没有事的人\n',
            '是不能出入的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_103D(): pass

    label('loc_103D')

    TalkEnd(0x0008)

    Return()

# id: 0x0005 offset: 0x1041
@scena.Code('func_05_1041')
def func_05_1041():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_117B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x041B, 0, 0x20D8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1124',
    )

    ChrTalk(
        0x00FE,
        (
            '你们是……请进。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1015F咦？奥利维尔不在\n',
            '也能进去？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，没问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在这种情况下大使\n',
            '很需要各种信息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他说如果各位游击士到来，\n',
            '就让你们进来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1000F原来如此，那我们就不客气了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x20D8)

    Jump('loc_1178')

    def _loc_1124(): pass

    label('loc_1124')

    ChrTalk(
        0x00FE,
        (
            '在这种情况下大使\n',
            '很需要各种信息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他说如果各位游击士到来，\n',
            '就让你们进来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1178(): pass

    label('loc_1178')

    Jump('loc_199D')

    def _loc_117B(): pass

    label('loc_117B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_151B',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1397',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_11A6',
    )

    ChrTalk(
        0x0009,
        (
            '请进。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1394')

    def _loc_11A6(): pass

    label('loc_11A6')

    EventBegin(0x00)
    Fade(1000)
    SetChrPos(0x0104, 75550, 0, 69160, 0)
    SetChrPos(0x0101, 75460, 0, 67600, 0)

    If(
        (
            (Expr.Eval, "OP_CB(0xF7)"),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_11F0',
    )

    SetChrPos(0x0106, 76600, 0, 66230, 0)

    Jump('loc_1201')

    def _loc_11F0(): pass

    label('loc_11F0')

    SetChrPos(0x0103, 76600, 0, 66230, 0)

    def _loc_1201(): pass

    label('loc_1201')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1222',
    )

    SetChrPos(0x00F9, 75320, 0, 66060, 0)

    Jump('loc_1233')

    def _loc_1222(): pass

    label('loc_1222')

    SetChrPos(0x00F8, 75320, 0, 66060, 0)

    def _loc_1233(): pass

    label('loc_1233')

    OP_6D(74500, 0, 71450, 0)
    OP_67(0, 5770, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_8C(0x0009, 180, 0)
    SetChrSubChip(0x0009, 0)
    OP_0D()

    ChrTalk(
        0x0009,
        (
            '#2P奥利维尔先生，你要进大使馆吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#030F嗯，我要进去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0009, 0, 400)
    OP_22(0x0073, 0x00, 0x64)
    Sleep(500)

    OP_6F(0x0009, 0)
    OP_70(0x0009, 0x0000003C)
    Sleep(1000)

    OP_8C(0x0009, 180, 400)
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#2P请进。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(500)
    OP_6D(75200, 0, 68360, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0000, 75200, 0, 68360, 0)
    SetChrPos(0x0001, 75200, 0, 68360, 0)
    SetChrPos(0x0002, 75200, 0, 68360, 0)
    SetChrPos(0x0003, 75200, 0, 68360, 0)
    OP_69(0x0000, 0x00000000)
    OP_0D()
    OP_A2(0x0005)
    EventEnd(0x00)

    def _loc_1394(): pass

    label('loc_1394')

    Jump('loc_1518')

    def _loc_1397(): pass

    label('loc_1397')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_1401',
    )

    ChrTalk(
        0x00FE,
        (
            '穆拉先生好像去柏斯\n',
            '出差了，要过一阵子才能回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样的话奥利维尔先生\n',
            '又能被放养了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1518')

    def _loc_1401(): pass

    label('loc_1401')

    ChrTalk(
        0x00FE,
        (
            '穆拉先生好像去柏斯\n',
            '出差了，要过一阵子才能回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好像他说是去王国军\n',
            '相关的设施了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样的话奥利维尔先生\n',
            '又能被放养了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1515',
    )

    ChrTalk(
        0x0104,
        (
            '#033F士兵朋友，别说这种失礼的话\n',
            '污人清白啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#034F你知道他出门，我内心深处\n',
            '有多么寂寞吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0104, 400)

    ChrTalk(
        0x00FE,
        (
            '……请别撒谎。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1515(): pass

    label('loc_1515')

    OP_A2(0x0004)

    def _loc_1518(): pass

    label('loc_1518')

    Jump('loc_199D')

    def _loc_151B(): pass

    label('loc_151B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_15AA',
    )

    ChrTalk(
        0x00FE,
        (
            '哎呀，诸位……\n',
            '莫非是来找奥利维尔先生的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '奥利维尔先生刚才\n',
            '跟穆拉先生出去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那两个人虽然常斗嘴，\n',
            '不过感情非常好哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_199D')

    def _loc_15AA(): pass

    label('loc_15AA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1602',
    )

    ChrTalk(
        0x00FE,
        (
            '辛苦了。\n',
            '和大使的会面怎么样了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果各位的目的\n',
            '能够达成就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_199D')

    def _loc_1602(): pass

    label('loc_1602')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_16BA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 7, 0x161F)),
            Expr.Return,
        ),
        'loc_1651',
    )

    ChrTalk(
        0x00FE,
        (
            '请进。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大使馆的领域内\n',
            '有治外法权，\n',
            '所以请小心一些。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_16B7')

    def _loc_1651(): pass

    label('loc_1651')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 5, 0x161D)),
            Expr.Return,
        ),
        'loc_165F',
    )

    Call(0, 0x000D)

    Jump('loc_16B7')

    def _loc_165F(): pass

    label('loc_165F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 6, 0x161E)),
            Expr.Return,
        ),
        'loc_16B3',
    )

    ChrTalk(
        0x00FE,
        (
            '达维尔大使和穆拉先生\n',
            '还没从外面回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然我想不会\n',
            '拖到很晚……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_16B7')

    def _loc_16B3(): pass

    label('loc_16B3')

    Call(0, 0x000C)

    def _loc_16B7(): pass

    label('loc_16B7')

    Jump('loc_199D')

    def _loc_16BA(): pass

    label('loc_16BA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_199D',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1917',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02CD, 5, 0x166D)),
            Expr.Return,
        ),
        'loc_172E',
    )

    ChrTurnDirection(0x0009, 0x0104, 0)

    ChrTalk(
        0x0009,
        (
            '奥利维尔先生，\n',
            '请你不要藏头露尾的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '这次的事达维尔大使\n',
            '也很生气哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1914')

    def _loc_172E(): pass

    label('loc_172E')

    ChrTurnDirection(0x0009, 0x0104, 0)

    ChrTalk(
        0x0104,
        (
            '#031F#6P哟，士兵朋友。\n',
            '你还好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0009,
        (
            '#5P奥、奥利维尔先生！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#5P你之前都在干什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#033F#6P咦，怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#5P不是怎么不怎么的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#5P你去亚尔摩后就\n',
            '就行踪不明了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#5P穆拉先生可生气了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#035F#6P呼……\n',
            '这个男人还是那么可爱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1007F#6P对了，奥利维尔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1019F难道你没告诉\n',
            '大使馆你和我们\n',
            '在一起行动？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#031F#6P哈哈哈。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '寻求爱的彷徨旅途\n',
            '是注定要隐忍的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1007F#6P你在嘟囔些什么\n',
            '莫明其妙的东西……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x166D)

    def _loc_1914(): pass

    label('loc_1914')

    Jump('loc_199D')

    def _loc_1917(): pass

    label('loc_1917')

    ChrTalk(
        0x00FE,
        (
            '前面是埃雷波尼亚帝国大使馆。\n',
            '不相干人员禁止入内。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '特别是临近签字仪式的现在，\n',
            '我们接到了强化警戒的指示。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '抱歉，请谅解。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_199D(): pass

    label('loc_199D')

    TalkEnd(0x0009)

    Return()

# id: 0x0006 offset: 0x19A1
@scena.Code('func_06_19A1')
def func_06_19A1():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1A17',
    )

    ChrTalk(
        0x00FE,
        (
            '导力器不能使用的话\n',
            '华光之王都的夜真是一片漆黑。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '女王她们虽然\n',
            '做了很多调查，\n',
            '真的能恢复使用吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1BA0')

    def _loc_1A17(): pass

    label('loc_1A17')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_1A92',
    )

    ChrTalk(
        0x00FE,
        (
            '港口的事件真厉害啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那个罪犯凯诺娜就是一直紧贴着\n',
            '理查德上校的那个人吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你的表情看上去很严肃呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1BA0')

    def _loc_1A92(): pass

    label('loc_1A92')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_1AEB',
    )

    ChrTalk(
        0x00FE,
        (
            '怎么了怎么了？难道是在找人？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '穿白色礼服的女孩子……\n',
            '唔～我没看见啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1BA0')

    def _loc_1AEB(): pass

    label('loc_1AEB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1B13',
    )

    ChrTalk(
        0x00FE,
        (
            '乌鸦在叫着让我回家⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1BA0')

    def _loc_1B13(): pass

    label('loc_1B13')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_1B4A',
    )

    ChrTalk(
        0x00FE,
        (
            '真无聊，要不要去艾德尔\n',
            '百货店买东西呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1BA0')

    def _loc_1B4A(): pass

    label('loc_1B4A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_1BA0',
    )

    ChrTalk(
        0x00FE,
        (
            'Ｙｅａｈ！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '格兰竞技场没什么活动，\n',
            '好像暂时休馆了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有点寂寞呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1BA0(): pass

    label('loc_1BA0')

    TalkEnd(0x00FE)

    Return()

# id: 0x0007 offset: 0x1BA4
@scena.Code('func_07_1BA4')
def func_07_1BA4():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1C2C',
    )

    ChrTalk(
        0x00FE,
        (
            '我还以为只有王都导力停止了呢，\n',
            '看来其他地方也一样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真想这样一直\n',
            '如果导力器没法使用，\n',
            '这个国家会变成什么样！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E4E')

    def _loc_1C2C(): pass

    label('loc_1C2C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_1CA9',
    )

    ChrTalk(
        0x00FE,
        (
            '确实，最近话题少，\n',
            '感觉没劲……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过还是不希望\n',
            '发生昨天那种事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我想要能够大家\n',
            '能在一起欢呼的话题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E4E')

    def _loc_1CA9(): pass

    label('loc_1CA9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_1CFA',
    )

    ChrTalk(
        0x00FE,
        (
            '最近没什么话题，感觉无聊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '能不能……\n',
            '发生点什么刺激的事呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E4E')

    def _loc_1CFA(): pass

    label('loc_1CFA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1D54',
    )

    ChrTalk(
        0x00FE,
        (
            '傍晚很美，可你不觉得\n',
            '它会让人感觉寂寞吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看着晚霞，\n',
            '我都流泪了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E4E')

    def _loc_1D54(): pass

    label('loc_1D54')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_1DBC',
    )

    ChrTalk(
        0x00FE,
        (
            '哎呀，莫非你就是在武术大赛\n',
            '中取得冠军的游击士？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊，能在这种地方\n',
            '遇见你真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E4E')

    def _loc_1DBC(): pass

    label('loc_1DBC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_1E4E',
    )

    ChrTalk(
        0x00FE,
        (
            '我是在看武术大赛时\n',
            '喜欢上王都的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在我就在这座城市生活。\n',
            '还是城市里有意思啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我也能顺利地参加明年的\n',
            '诞辰庆典和武术大赛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1E4E(): pass

    label('loc_1E4E')

    TalkEnd(0x00FE)

    Return()

# id: 0x0008 offset: 0x1E52
@scena.Code('func_08_1E52')
def func_08_1E52():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1ECF',
    )

    ChrTalk(
        0x00FE,
        (
            '利贝尔是因导力器\n',
            '发展起来的国家吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果一直像这样不能使用导力器的话……\n',
            '就不仅是不方便这么简单了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_20ED')

    def _loc_1ECF(): pass

    label('loc_1ECF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_1F27',
    )

    ChrTalk(
        0x00FE,
        (
            '情报部那些家伙们\n',
            '又引发了不得了的事件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没有市民伤亡\n',
            '真是太好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_20ED')

    def _loc_1F27(): pass

    label('loc_1F27')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_1F9D',
    )

    ChrTalk(
        0x00FE,
        (
            '天气真好，要不要去\n',
            '离宫午睡呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在王国军的家伙们\n',
            '把那儿当作警备本部了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '算了，也没办法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_20ED')

    def _loc_1F9D(): pass

    label('loc_1F9D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1FFC',
    )

    ChrTalk(
        0x00FE,
        (
            '可能因为签字仪式近了，\n',
            '在城里执勤的人看来也很忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '公务员也真不容易啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_20ED')

    def _loc_1FFC(): pass

    label('loc_1FFC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_20A1',
    )

    ChrTalk(
        0x00FE,
        (
            '在那么多事件和活动之后，\n',
            '王都总算平静下来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……不过，想一想\n',
            '接下来就是等待签字仪式了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '反正，要是这么以来就能\n',
            '得到和平的话我是很欢迎的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_20ED')

    def _loc_20A1(): pass

    label('loc_20A1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_20ED',
    )

    ChrTalk(
        0x00FE,
        (
            '啊，好困……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要不要去西街区的咖啡屋\n',
            '要杯咖啡来提提神呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_20ED(): pass

    label('loc_20ED')

    TalkEnd(0x00FE)

    Return()

# id: 0x0009 offset: 0x20F1
@scena.Code('func_09_20F1')
def func_09_20F1():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_2139',
    )

    ChrTalk(
        0x00FE,
        (
            '……说起来，真\n',
            '感觉受不了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样的生活岂不悲惨？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_224D')

    def _loc_2139(): pass

    label('loc_2139')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_216A',
    )

    ChrTalk(
        0x00FE,
        (
            '那个超级差劲的\n',
            '公爵好像回王都了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_224D')

    def _loc_216A(): pass

    label('loc_216A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_21C6',
    )

    ChrTalk(
        0x00FE,
        (
            '说起来，幽灵到底是什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……咦，真的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不会吧，怎么可能有那东西！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_224D')

    def _loc_21C6(): pass

    label('loc_21C6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_21EE',
    )

    ChrTalk(
        0x00FE,
        (
            '说起来，今天吃什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_224D')

    def _loc_21EE(): pass

    label('loc_21EE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_2210',
    )

    ChrTalk(
        0x00FE,
        (
            '说起来，要玩什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_224D')

    def _loc_2210(): pass

    label('loc_2210')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_224D',
    )

    ChrTalk(
        0x00FE,
        (
            '说起来，签字仪式是什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '和我们有～关系吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_224D(): pass

    label('loc_224D')

    TalkEnd(0x00FE)

    Return()

# id: 0x000A offset: 0x2251
@scena.Code('func_0A_2251')
def func_0A_2251():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_22A0',
    )

    ChrTalk(
        0x00FE,
        (
            '出现在那座湖里\n',
            '绝对可疑～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为一看不就\n',
            '让人感觉很可疑？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23D9')

    def _loc_22A0(): pass

    label('loc_22A0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_22E3',
    )

    ChrTalk(
        0x00FE,
        (
            '咦，真的？\n',
            '不过，那个公爵啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是不是有点可爱？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23D9')

    def _loc_22E3(): pass

    label('loc_22E3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_2330',
    )

    ChrTalk(
        0x00FE,
        (
            '我都说了，真的\n',
            '在卢安出现了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你为什么不相信？　真气人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23D9')

    def _loc_2330(): pass

    label('loc_2330')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2381',
    )

    ChrTalk(
        0x00FE,
        (
            '去不去西街区的咖啡店？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那里的咖喱，\n',
            '好吃得让人实在受不了',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23D9')

    def _loc_2381(): pass

    label('loc_2381')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_23A7',
    )

    ChrTalk(
        0x00FE,
        (
            '对了，想不想吃冰淇淋？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23D9')

    def _loc_23A7(): pass

    label('loc_23A7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_23D9',
    )

    ChrTalk(
        0x00FE,
        (
            '总之就是那个。\n',
            '大家搞好关系，之类的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_23D9(): pass

    label('loc_23D9')

    TalkEnd(0x00FE)

    Return()

# id: 0x000B offset: 0x23DD
@scena.Code('func_0B_23DD')
def func_0B_23DD():
    UnlockAchievement(0x01, 0x0C, 0x00, 0x00)
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_2416',
    )

    ChrTalk(
        0x00FE,
        (
            '恋破山河在……\n',
            '千军万马梦留痕……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_267A')

    def _loc_2416(): pass

    label('loc_2416')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_2498',
    )

    ChrTalk(
        0x00FE,
        (
            '昨天我面向夕阳全力狂奔，\n',
            '想不到感觉很舒畅。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好吧，光在这里发愁\n',
            '也没任何的意义。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对了，去什么地方旅行吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_267A')

    def _loc_2498(): pass

    label('loc_2498')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_251F',
    )

    ChrTalk(
        0x00FE,
        (
            '夕阳染得云绯红……\n',
            '世界多么美丽啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '并且，我是个多么\n',
            '渺小的存在啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '喂，利库斯……\n',
            '渺小的我应该做些什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_267A')

    def _loc_251F(): pass

    label('loc_251F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_256C',
    )

    ChrTalk(
        0x00FE,
        (
            '我这么苦恼，\n',
            '亏你还能打哈欠。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是哥们的话就和我一起烦恼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_267A')

    def _loc_256C(): pass

    label('loc_256C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_267A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2620',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，到头来什么也没改变……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天也是像这样\n',
            '稀里糊涂地度过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天也是像这样\n',
            '稀里糊涂地度过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没有工作，没有女友……\n',
            '我的人生像这样下去好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    Jump('loc_267A')

    def _loc_2620(): pass

    label('loc_2620')

    ChrTalk(
        0x00FE,
        (
            '呼，今天到头来\n',
            '稀里糊涂地度过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没有工作，没有女友……\n',
            '我的人生像这样下去好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_267A(): pass

    label('loc_267A')

    TalkEnd(0x00FE)

    Return()

# id: 0x000C offset: 0x267E
@scena.Code('func_0C_267E')
def func_0C_267E():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_26D2',
    )

    ChrTalk(
        0x00FE,
        (
            '安敦那家伙，\n',
            '在洛连特也失恋了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他的下一个目标好像是珀艾玛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2810')

    def _loc_26D2(): pass

    label('loc_26D2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_273E',
    )

    ChrTalk(
        0x00FE,
        (
            '安敦那家伙，\n',
            '真是语出惊人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他说简单的最美。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然意思有点不对，\n',
            '不过也挺合适的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2810')

    def _loc_273E(): pass

    label('loc_273E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_27AA',
    )

    ChrTalk(
        0x00FE,
        (
            '……面向夕阳\n',
            '奔跑一下怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然没什么大的意义，\n',
            '不过有可能因为那节奏使心情变好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2810')

    def _loc_27AA(): pass

    label('loc_27AA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_27CE',
    )

    ChrTalk(
        0x00FE,
        (
            '哇～今天天气也不错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2810')

    def _loc_27CE(): pass

    label('loc_27CE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_2810',
    )

    ChrTalk(
        0x00FE,
        (
            '哈哈，安敦，你看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那朵云像不像\n',
            '杜南公爵的发型。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2810(): pass

    label('loc_2810')

    TalkEnd(0x00FE)

    Return()

# id: 0x000D offset: 0x2814
@scena.Code('func_0D_2814')
def func_0D_2814():
    TalkBegin(0x0011)
    Call(6, 0x0004)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_282E',
    )

    OP_A9(0xCE)
    TalkEnd(0x0011)

    Return()

    def _loc_282E(): pass

    label('loc_282E')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_283F',
    )

    TalkEnd(0x0011)

    Return()

    def _loc_283F(): pass

    label('loc_283F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_28CC',
    )

    ChrTalk(
        0x00FE,
        (
            '冰淇淋是在格兰赛尔\n',
            '城堡的厨房做的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '女王说要把这里的\n',
            '冰淇淋让大家一起吃……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '听说女王好像吃过我的冰淇淋，\n',
            '我真吃惊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2C86')

    def _loc_28CC(): pass

    label('loc_28CC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_293E',
    )

    ChrTalk(
        0x00FE,
        (
            '听说昨晚发生了可怕的事件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '客人都在讨论\n',
            '港口的事件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因此我也了解了\n',
            '不是关于事件的内容。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2C86')

    def _loc_293E(): pass

    label('loc_293E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_2A31',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C6, 4, 0x1634)),
            Expr.Return,
        ),
        'loc_29B2',
    )

    ChrTalk(
        0x00FE,
        (
            '穿白色礼服的女孩子，\n',
            '应该在空港吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '她倒是乐呵呵地说\n',
            '『我和姐姐她们\n',
            '约好在空港见面的』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A2E')

    def _loc_29B2(): pass

    label('loc_29B2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C6, 3, 0x1633)),
            Expr.Return,
        ),
        'loc_29C0',
    )

    Call(0, 0x0018)

    Jump('loc_2A2E')

    def _loc_29C0(): pass

    label('loc_29C0')

    ChrTalk(
        0x00FE,
        (
            '象利贝尔通讯那样的杂志\n',
            '能对我们介绍当然好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过最让我感到高兴的还是\n',
            '孩子们能津津有味地吃冰淇淋。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2A2E(): pass

    label('loc_2A2E')

    Jump('loc_2C86')

    def _loc_2A31(): pass

    label('loc_2A31')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2A76',
    )

    ChrTalk(
        0x00FE,
        (
            '欢迎～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要不要来个冰淇淋\n',
            '作为晚饭后的甜食？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2C86')

    def _loc_2A76(): pass

    label('loc_2A76')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_2AB1',
    )

    ChrTalk(
        0x00FE,
        (
            '欢迎～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要不要尝尝冰凉\n',
            '美味的冰淇淋？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2C86')

    def _loc_2AB1(): pass

    label('loc_2AB1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_2C86',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2C22',
    )

    ChrTalk(
        0x00FE,
        (
            '有人说我们是王室御用的，\n',
            '不过那只是传言而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然能让科洛蒂娅殿下品尝\n',
            '我自然很高兴……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2C1C',
    )

    ChrTurnDirection(0x0101, 0x0105, 400)

    ChrTalk(
        0x0101,
        (
            '#1000F（……科洛丝，你\n',
            '　吃过这里的冰淇淋吗？)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F（…………唔。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '(其实祖母大人也向我\n',
            ' 推荐过。)',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '(她老人家吃得\n',
            ' 非常开心。)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0011, 400)

    ChrTalk(
        0x0101,
        (
            '#1001F大姐姐，没问题的。\n',
            '我觉得你可以为王室御用这个称号感到自豪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '？？？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2C1C(): pass

    label('loc_2C1C')

    OP_A2(0x0001)

    Jump('loc_2C86')

    def _loc_2C22(): pass

    label('loc_2C22')

    ChrTalk(
        0x00FE,
        (
            '有人说我们是王室御用的，\n',
            '不过那到底只是传言而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果科洛蒂娅殿下真的吃过\n',
            '我自然很高兴。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2C86(): pass

    label('loc_2C86')

    TalkEnd(0x0011)

    Return()

# id: 0x000E offset: 0x2C8A
@scena.Code('func_0E_2C8A')
def func_0E_2C8A():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_2CE7',
    )

    ChrTalk(
        0x00FE,
        (
            '我搭乘的林德号\n',
            '停泊在洛连特……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过因为担心孩子，\n',
            '就急着返回王都了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2D77')

    def _loc_2CE7(): pass

    label('loc_2CE7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_2D24',
    )

    ChrTalk(
        0x00FE,
        (
            '呵呵，抱歉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要不要一起\n',
            '吃那边的冰淇淋？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2D77')

    def _loc_2D24(): pass

    label('loc_2D24')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_2D77',
    )

    ChrTalk(
        0x00FE,
        (
            '趁飞行的间歇\n',
            '我来稍微陪会儿孩子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '平时总让这孩子\n',
            '忍耐很多事情……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2D77(): pass

    label('loc_2D77')

    TalkEnd(0x00FE)

    Return()

# id: 0x000F offset: 0x2D7B
@scena.Code('func_0F_2D7B')
def func_0F_2D7B():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_2E00',
    )

    ChrTalk(
        0x00FE,
        (
            '房间又冷又暗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我虽然很害怕，\n',
            '可还是拼命忍耐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我因为看到妈妈的脸而安心得\n',
            '哭出来了，不过这可是秘密哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F48')

    def _loc_2E00(): pass

    label('loc_2E00')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_2E3F',
    )

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，我很乖地\n',
            '在家看家哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一点也不寂寞！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F48')

    def _loc_2E3F(): pass

    label('loc_2E3F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_2E8C',
    )

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，就算妈妈去工作\n',
            '我也能忍耐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为我是妈妈的好孩子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F48')

    def _loc_2E8C(): pass

    label('loc_2E8C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2ED0',
    )

    ChrTalk(
        0x00FE,
        (
            '妈妈……呜呜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好想能早点和妈妈一起玩……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F48')

    def _loc_2ED0(): pass

    label('loc_2ED0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_2F0D',
    )

    ChrTalk(
        0x00FE,
        (
            '太好了～妈妈从单位\n',
            '回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们羡慕吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F48')

    def _loc_2F0D(): pass

    label('loc_2F0D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_2F48',
    )

    ChrTalk(
        0x00FE,
        (
            '妈妈能不能早点回来呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我会努力等着的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2F48(): pass

    label('loc_2F48')

    TalkEnd(0x00FE)

    Return()

# id: 0x0010 offset: 0x2F4C
@scena.Code('func_10_2F4C')
def func_10_2F4C():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_2FE0',
    )

    ChrTalk(
        0x00FE,
        (
            '在国际社会中\n',
            '利贝尔的优势\n',
            '是基于导力技术保持的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '互不侵犯条约也算是这点的象征吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果这状况持续下去的话\n',
            '就算是女王……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3229')

    def _loc_2FE0(): pass

    label('loc_2FE0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_3060',
    )

    ChrTalk(
        0x00FE,
        (
            '情报部竟然闹出那种事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是因为念着理查德上校\n',
            '所以才这么做的吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '无论如何，武力解决\n',
            '都无法让人钦佩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3229')

    def _loc_3060(): pass

    label('loc_3060')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_30D0',
    )

    ChrTalk(
        0x00FE,
        (
            '在签字仪式那天治理各地的\n',
            '市长们好像也会出席。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '卢安应该会派\n',
            '新市长来吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不知道啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3229')

    def _loc_30D0(): pass

    label('loc_30D0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_315A',
    )

    ChrTalk(
        0x00FE,
        (
            '王国军从政变的重创中\n',
            '恢复过来需要时间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可是我们有尤莉亚上尉、\n',
            '希德中校和卡西乌斯准将。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '利贝尔一定没问题的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3229')

    def _loc_315A(): pass

    label('loc_315A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_31C2',
    )

    ChrTalk(
        0x00FE,
        (
            '帝国竟然也会同意在\n',
            '互不侵犯条约上签字呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵，女王陛下究竟使用了\n',
            '什么样的魔法呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3229')

    def _loc_31C2(): pass

    label('loc_31C2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_3229',
    )

    ChrTalk(
        0x00FE,
        (
            '王室亲卫队的尤莉亚队长\n',
            '最近听说晋升为上尉了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵，想想她的能力和\n',
            '实绩就能理解了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3229(): pass

    label('loc_3229')

    TalkEnd(0x00FE)

    Return()

# id: 0x0011 offset: 0x322D
@scena.Code('func_11_322D')
def func_11_322D():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_3293',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，因为导力器不能使用\n',
            '夜晚变长了，让人不安得睡不着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '日暮真是让人感觉忧郁……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_34CE')

    def _loc_3293(): pass

    label('loc_3293')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_330D',
    )

    ChrTalk(
        0x00FE,
        (
            '我想了很多……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要想遇上优秀的男性，\n',
            '我也要对自己的内涵进行磨炼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果能和对方互相激励\n',
            '岂不更好？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_34CE')

    def _loc_330D(): pass

    label('loc_330D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_338E',
    )

    ChrTalk(
        0x00FE,
        (
            '人生会因为终生伴侣\n',
            '而产生很大的改变。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我觉得还是要\n',
            '磨炼好辨别男性的眼力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '首先要观察对方的表\n',
            '和鞋子吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_34CE')

    def _loc_338E(): pass

    label('loc_338E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3401',
    )

    ChrTalk(
        0x00FE,
        (
            '有个不认识的老奶奶\n',
            '突然对我说\n',
            '『能不能嫁给我儿子』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我怎么可能嫁给一个\n',
            '从来没见过的人呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_34CE')

    def _loc_3401(): pass

    label('loc_3401')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_346E',
    )

    ChrTalk(
        0x00FE,
        (
            '刚才有个不认识的老奶奶\n',
            '直直地盯着我看……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '到底是什么意思呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '难道我脸上有什么东西？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_34CE')

    def _loc_346E(): pass

    label('loc_346E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_34CE',
    )

    ChrTalk(
        0x00FE,
        (
            '我以前曾被一个呆在百货商店\n',
            '台阶上的男人纠缠过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那真令人感到恶心和毛骨悚然……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_34CE(): pass

    label('loc_34CE')

    TalkEnd(0x00FE)

    Return()

# id: 0x0012 offset: 0x34D2
@scena.Code('func_12_34D2')
def func_12_34D2():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_356F',
    )

    ChrTalk(
        0x00FE,
        (
            '对现在年轻的人来说，\n',
            '好像导力停止之后\n',
            '都感到非常不安呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '当然，烧热水是一件\n',
            '很麻烦的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '即便是我也已经\n',
            '习惯于有导力的生活了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3757')

    def _loc_356F(): pass

    label('loc_356F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_35DC',
    )

    ChrTalk(
        0x00FE,
        (
            '昨天的事件亲卫队和游击士\n',
            '好像联手解决了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '王国军和协会\n',
            '如果合作的话\n',
            '就没什么可怕的事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3757')

    def _loc_35DC(): pass

    label('loc_35DC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_361B',
    )

    ChrTalk(
        0x00FE,
        (
            '虽说是工作，不过每到节日\n',
            '士兵们都要忙于警戒呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3757')

    def _loc_361B(): pass

    label('loc_361B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3654',
    )

    ChrTalk(
        0x00FE,
        (
            '哎呀，太阳落山的时间\n',
            '有点提早了呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3757')

    def _loc_3654(): pass

    label('loc_3654')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_36E1',
    )

    ChrTalk(
        0x00FE,
        (
            '最近看不到游击士协会的\n',
            '克鲁茨先生呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他是不是出门\n',
            '去了别的什么地方……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '克鲁茨先生那种彬彬有礼的\n',
            '品格很受我们欢迎。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3757')

    def _loc_36E1(): pass

    label('loc_36E1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_3757',
    )

    ChrTurnDirection(0x0101, 0x00FE, 400)

    ChrTalk(
        0x00FE,
        (
            '呀，你胸口的那枚徽章……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大姐和……\n',
            '你莫非是正游击士？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们工作辛苦了。\n',
            '真是年轻有为啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3757(): pass

    label('loc_3757')

    TalkEnd(0x00FE)

    Return()

# id: 0x0013 offset: 0x375B
@scena.Code('func_13_375B')
def func_13_375B():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C9, 1, 0x1649)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_39E0',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0071, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_393C',
    )

    ChrTalk(
        0x00FE,
        (
            '历史资料馆……\n',
            '嗯，应该就是这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1011F咦，这不是吉米先生吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊？　对了，你是\n',
            '在蔡斯救过我的游击士吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1000F你在这里干什么啊？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1004F哦，对了……是来上交\n',
            '那个古代遗物的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是啊，就算失去了力量，不过\n',
            '还是不知道这东西会引起什么事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我打算放在这里委托他们调查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1001F是吗？了不起了不起。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '如果你能放弃寻宝\n',
            '而认真工作的话，就更了不起了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哇，你嘴好厉害……\n',
            '不过那是没的商量的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '除非我能找到比\n',
            '寻宝更浪漫的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_39DA')

    def _loc_393C(): pass

    label('loc_393C')

    ChrTalk(
        0x00FE,
        (
            '历史资料馆……\n',
            '哇，看来没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这里一定能保管\n',
            '古代遗物。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '其实我在蔡斯找到了\n',
            '已失去力量的古代遗物……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我想请这座历史资料馆\n',
            '调查，就过来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_39DA(): pass

    label('loc_39DA')

    OP_A2(0x1649)

    Jump('loc_3A29')

    def _loc_39E0(): pass

    label('loc_39E0')

    ChrTalk(
        0x00FE,
        (
            '准备让他们帮我\n',
            '调查失去了力量的古代遗物。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '首先得去见负责人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_3A29(): pass

    label('loc_3A29')

    TalkEnd(0x00FE)

    Return()

# id: 0x0014 offset: 0x3A2D
@scena.Code('func_14_3A2D')
def func_14_3A2D():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_3A78',
    )

    ChrTalk(
        0x00FE,
        (
            '要是蔡斯的拉赛尔博士\n',
            '关于此次的事件\n',
            '应该会知道点什么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3B01')

    def _loc_3A78(): pass

    label('loc_3A78')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_3ADC',
    )

    ChrTalk(
        0x00FE,
        (
            '那样的巨大人形兵器……\n',
            '靠我们实在无法对付。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果下次再被袭击的话\n',
            '肯定承受不了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3B01')

    def _loc_3ADC(): pass

    label('loc_3ADC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_3B01',
    )

    ChrTalk(
        0x00FE,
        (
            '咦？你们在找迷路的孩子？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3B01(): pass

    label('loc_3B01')

    TalkEnd(0x00FE)

    Return()

# id: 0x0015 offset: 0x3B05
@scena.Code('func_15_3B05')
def func_15_3B05():
    TalkBegin(0x00FE)
    OP_4A(0x00FE, 255)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_3B5F',
    )

    ChrTalk(
        0x00FE,
        (
            '王国军现在仍处于警戒态势。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为了应付紧急情况，\n',
            '我也必须努力了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3BE4')

    def _loc_3B5F(): pass

    label('loc_3B5F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_3BAA',
    )

    ChrTalk(
        0x00FE,
        (
            '有传闻说事件的主谋\n',
            '是个不多大的小孩……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可这怎么可能？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3BE4')

    def _loc_3BAA(): pass

    label('loc_3BAA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_3BE4',
    )

    ChrTalk(
        0x00FE,
        (
            '东街区有很多重要设施，\n',
            '所以得一丝不苟地警戒。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3BE4(): pass

    label('loc_3BE4')

    OP_4B(0x00FE, 255)
    TalkEnd(0x00FE)

    Return()

# id: 0x0016 offset: 0x3BEC
@scena.Code('func_16_3BEC')
def func_16_3BEC():
    TalkBegin(0x00FE)
    OP_4A(0x00FE, 255)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_3C53',
    )

    ChrTalk(
        0x00FE,
        (
            '王国军里有那卡西乌斯准将\n',
            '希德中校在。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '光是想到这点，\n',
            '我们就能冷静地行动了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3CF5')

    def _loc_3C53(): pass

    label('loc_3C53')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_3CC9',
    )

    ChrTalk(
        0x00FE,
        (
            '昨天的事件虽然令人惊讶，\n',
            '不过尤莉亚队长回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是希德中校把她叫回来的，\n',
            '不过时机真是恰到好处啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3CF5')

    def _loc_3CC9(): pass

    label('loc_3CC9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_3CF5',
    )

    ChrTalk(
        0x00FE,
        (
            '现在没发生任何\n',
            '疑似问题的问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3CF5(): pass

    label('loc_3CF5')

    OP_4B(0x00FE, 255)
    TalkEnd(0x00FE)

    Return()

# id: 0x0017 offset: 0x3CFD
@scena.Code('func_17_3CFD')
def func_17_3CFD():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_3D0A',
    )

    Jump('loc_3E1E')

    def _loc_3D0A(): pass

    label('loc_3D0A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_3D3B',
    )

    ChrTalk(
        0x00FE,
        (
            '拜托了，光昨天一天，\n',
            '还没看够呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3E1E')

    def _loc_3D3B(): pass

    label('loc_3D3B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_3D92',
    )

    ChrTalk(
        0x00FE,
        (
            '好不容易来一趟，\n',
            '得参观一下学术方面的设施。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对人来说教育也很重要。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3E1E')

    def _loc_3D92(): pass

    label('loc_3D92')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3DC6',
    )

    ChrTalk(
        0x00FE,
        (
            '……对意料之外的费用感到头痛啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3E1E')

    def _loc_3DC6(): pass

    label('loc_3DC6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_3DF7',
    )

    ChrTalk(
        0x00FE,
        (
            '想不到格兰竞技场竟然\n',
            '处于淡季……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3E1E')

    def _loc_3DF7(): pass

    label('loc_3DF7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_3E1E',
    )

    ChrTalk(
        0x00FE,
        (
            '哟，这里就是格兰竞技场啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3E1E(): pass

    label('loc_3E1E')

    TalkEnd(0x00FE)

    Return()

# id: 0x0018 offset: 0x3E22
@scena.Code('func_18_3E22')
def func_18_3E22():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_3E2F',
    )

    Jump('loc_3F4F')

    def _loc_3E2F(): pass

    label('loc_3E2F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_3E8B',
    )

    ChrTalk(
        0x00FE,
        (
            '这人看来是\n',
            '迷上了历史资料馆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好不容易旅行一次，\n',
            '我今天想去别的地方啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3F4F')

    def _loc_3E8B(): pass

    label('loc_3E8B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_3EDC',
    )

    ChrTalk(
        0x00FE,
        (
            '这历史资料馆……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '也没什么有意思的东西，\n',
            '说实话我不太感兴趣。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3F4F')

    def _loc_3EDC(): pass

    label('loc_3EDC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3F02',
    )

    ChrTalk(
        0x00FE,
        (
            '呵呵，购物很愉快。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3F4F')

    def _loc_3F02(): pass

    label('loc_3F02')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_3F2B',
    )

    ChrTalk(
        0x00FE,
        (
            '唉……这个人\n',
            '真没计划性。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3F4F')

    def _loc_3F2B(): pass

    label('loc_3F2B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_3F4F',
    )

    ChrTalk(
        0x00FE,
        (
            '那个……\n',
            '莫非大门关着？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3F4F(): pass

    label('loc_3F4F')

    TalkEnd(0x00FE)

    Return()

# id: 0x0019 offset: 0x3F53
@scena.Code('func_19_3F53')
def func_19_3F53():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_3F60',
    )

    Jump('loc_40D4')

    def _loc_3F60(): pass

    label('loc_3F60')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_3FB5',
    )

    ChrTalk(
        0x00FE,
        (
            '帝国虽然有种危险的感觉，\n',
            '不过那也正是它的魅力……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真想去玩玩啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_40D4')

    def _loc_3FB5(): pass

    label('loc_3FB5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_3FEA',
    )

    ChrTalk(
        0x00FE,
        (
            '……穿白衣服的女孩子？\n',
            '嗯，没看见啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_40D4')

    def _loc_3FEA(): pass

    label('loc_3FEA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4040',
    )

    ChrTalk(
        0x00FE,
        (
            '你们和黑发的\n',
            '帝国军人说过话了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真好啊……\n',
            '我是他的粉丝啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_40D4')

    def _loc_4040(): pass

    label('loc_4040')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_4096',
    )

    ChrTalk(
        0x00FE,
        (
            '刚才从大使馆出来了\n',
            '一个黑发的军人哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然不太亲切，\n',
            '不过很帅啊㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_40D4')

    def _loc_4096(): pass

    label('loc_4096')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_40D4',
    )

    ChrTalk(
        0x00FE,
        (
            '『黄金军马』的徽章啊……\n',
            '凑近看的话真有震撼力啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_40D4(): pass

    label('loc_40D4')

    TalkEnd(0x00FE)

    Return()

# id: 0x001A offset: 0x40D8
@scena.Code('func_1A_40D8')
def func_1A_40D8():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_40E5',
    )

    Jump('loc_421D')

    def _loc_40E5(): pass

    label('loc_40E5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_410E',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯……空港\n',
            '在那个方向呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_421D')

    def _loc_410E(): pass

    label('loc_410E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_4130',
    )

    ChrTalk(
        0x00FE,
        (
            '今天去哪儿参观呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_421D')

    def _loc_4130(): pass

    label('loc_4130')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4177',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，在王都的参观很令我满意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '也该回\n',
            '宾馆了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_421D')

    def _loc_4177(): pass

    label('loc_4177')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_41E9',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯～这里是东街区的\n',
            '共和国大使馆前，那么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '太广阔了，很容易迷路，\n',
            '所以我在百货商店买了地图。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_421D')

    def _loc_41E9(): pass

    label('loc_41E9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_421D',
    )

    ChrTalk(
        0x00FE,
        (
            '我是第一次来王都，\n',
            '这真是个广阔的城市。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_421D(): pass

    label('loc_421D')

    TalkEnd(0x00FE)

    Return()

# id: 0x001B offset: 0x4221
@scena.Code('func_1B_4221')
def func_1B_4221():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_422E',
    )

    Jump('loc_4357')

    def _loc_422E(): pass

    label('loc_422E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_4265',
    )

    ChrTalk(
        0x00FE,
        (
            '好象发生了什么事件呢。\n',
            '到底是什么呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4357')

    def _loc_4265(): pass

    label('loc_4265')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_42AA',
    )

    ChrTalk(
        0x00FE,
        (
            '有没有看见一个女孩子？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我看见了，\n',
            '她走过这里的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4357')

    def _loc_42AA(): pass

    label('loc_42AA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_42D6',
    )

    ChrTalk(
        0x00FE,
        (
            '哎呀，好漂亮的晚霞啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4357')

    def _loc_42D6(): pass

    label('loc_42D6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_4330',
    )

    ChrTalk(
        0x00FE,
        (
            '光是参观景点\n',
            '不能算是旅游。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '像这样悠闲的时刻\n',
            '也能成为旅行的美好回忆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4357')

    def _loc_4330(): pass

    label('loc_4330')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_4357',
    )

    ChrTalk(
        0x00FE,
        (
            '呵呵，这里真是个好地方……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4357(): pass

    label('loc_4357')

    TalkEnd(0x00FE)

    Return()

# id: 0x001C offset: 0x435B
@scena.Code('func_1C_435B')
def func_1C_435B():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_4368',
    )

    Jump('loc_44EF')

    def _loc_4368(): pass

    label('loc_4368')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_43C4',
    )

    ChrTalk(
        0x00FE,
        (
            '快乐的旅行也\n',
            '只到今天为止了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '从明天开始又要恢复\n',
            '一如既往的主妇生活了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_44EF')

    def _loc_43C4(): pass

    label('loc_43C4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_4419',
    )

    ChrTalk(
        0x00FE,
        (
            '穿白衣服的女孩子？\n',
            '刚才我好像看见了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我记得好像就在这附近……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_44EF')

    def _loc_4419(): pass

    label('loc_4419')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_447C',
    )

    ChrTalk(
        0x00FE,
        (
            '在旅行目的地买东西的话，不知不觉\n',
            '让钱包见底了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '买纪念品的钱很快就不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_44EF')

    def _loc_447C(): pass

    label('loc_447C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_44C0',
    )

    ChrTalk(
        0x00FE,
        (
            '冰淇淋\n',
            '非常好吃。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好了，该去百货商店\n',
            '买东西了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_44EF')

    def _loc_44C0(): pass

    label('loc_44C0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_44EF',
    )

    ChrTalk(
        0x00FE,
        (
            '附近有\n',
            '好吃的冰淇淋\n',
            '我是听说的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_44EF(): pass

    label('loc_44EF')

    TalkEnd(0x00FE)

    Return()

# id: 0x001D offset: 0x44F3
@scena.Code('func_1D_44F3')
def func_1D_44F3():
    EventBegin(0x00)
    SetChrFlags(0x0000, 0x0080)
    SetChrFlags(0x0001, 0x0080)
    SetChrFlags(0x0002, 0x0080)
    SetChrFlags(0x0003, 0x0080)
    SetChrFlags(0x0011, 0x0080)
    OP_D2(0x000700E1, 0x000700E5, 0x00)
    OP_D2(0x0007030A, 0x00070311, 0x01)
    OP_D2(0x0007030B, 0x00070312, 0x02)
    OP_D2(0x0007030C, 0x00070313, 0x03)
    OP_D2(0x0007013B, 0x0007013F, 0x04)
    OP_D2(0x00070530, 0x00070538, 0x05)
    OP_D2(0x00070531, 0x00070539, 0x06)
    OP_D2(0x00070532, 0x0007053A, 0x07)
    OP_D2(0x002700C0, 0x002700C4, 0x08)
    OP_D2(0x0007014A, 0x0007014E, 0x09)
    OP_D2(0x0006007B, 0x00060080, 0x0A)
    OP_D2(0x0006007C, 0x00060081, 0x0B)
    OP_D2(0x00290142, 0x00290146, 0x0C)
    OP_D2(0x0029014C, 0x00290150, 0x0D)
    OP_D2(0x0026000E, 0x00260013, 0x0E)
    OP_D2(0x00270312, 0x0027031C, 0x0F)
    OP_D2(0x00270315, 0x0027031F, 0x10)
    OP_D2(0x00270316, 0x00270320, 0x11)
    OP_D2(0x00070310, 0x00070317, 0x12)
    OP_D3(0x13)
    OP_D2(0x00060053, 0x00060058, 0x13)
    OP_D3(0x14)
    OP_D2(0x00290143, 0x00290147, 0x14)
    OP_D2(0x00290144, 0x00290148, 0x15)
    OP_D2(0x0029014A, 0x0029014B, 0x16)
    OP_D2(0x00070540, 0x00070541, 0x17)
    OP_D2(0x0029014D, 0x00290151, 0x18)
    OP_D2(0x0029014F, 0x00290153, 0x19)
    OP_D2(0x0029014E, 0x00290152, 0x1A)
    OP_D2(0x0007030F, 0x00070316, 0x1B)
    OP_D2(0x00070310, 0x00070317, 0x1C)
    OP_D2(0x00270313, 0x0027031D, 0x1D)
    OP_D2(0x00270314, 0x0027031E, 0x1E)
    OP_D2(0x00270318, 0x00270322, 0x1F)
    OP_D2(0x0026000D, 0x00260012, 0x20)
    OP_D2(0x00270326, 0x00270330, 0x21)
    OP_D2(0x0027032A, 0x00270334, 0x22)
    OP_D2(0x00270327, 0x00270331, 0x23)
    OP_D2(0x00270328, 0x00270332, 0x24)
    OP_D2(0x0027032C, 0x00270336, 0x25)
    SetChrChipByIndex(0x0028, 8)
    SetChrChipByIndex(0x0029, 2)
    SetChrChipByIndex(0x002A, 2)
    SetChrChipByIndex(0x002B, 2)
    SetChrChipByIndex(0x002C, 2)
    SetChrChipByIndex(0x002D, 2)
    SetChrChipByIndex(0x002E, 2)
    SetChrChipByIndex(0x002F, 2)
    SetChrChipByIndex(0x0030, 2)
    SetChrChipByIndex(0x0031, 6)
    SetChrChipByIndex(0x0032, 6)
    SetChrChipByIndex(0x0033, 6)
    SetChrChipByIndex(0x0034, 6)
    SetChrChipByIndex(0x0035, 6)
    SetChrChipByIndex(0x0036, 6)
    SetChrChipByIndex(0x0037, 6)
    SetChrChipByIndex(0x0038, 6)
    SetChrChipByIndex(0x0049, 19)
    SetChrChipByIndex(0x004A, 19)
    SetChrChipByIndex(0x004B, 19)
    SetChrChipByIndex(0x004C, 19)
    SetChrSubChip(0x0028, 0)
    SetChrSubChip(0x0029, 0)
    SetChrSubChip(0x002A, 0)
    SetChrSubChip(0x002B, 0)
    SetChrSubChip(0x002C, 0)
    SetChrSubChip(0x002D, 0)
    SetChrSubChip(0x002E, 0)
    SetChrSubChip(0x002F, 0)
    SetChrSubChip(0x0030, 0)
    SetChrSubChip(0x0031, 0)
    SetChrSubChip(0x0032, 0)
    SetChrSubChip(0x0033, 0)
    SetChrSubChip(0x0034, 0)
    SetChrSubChip(0x0035, 0)
    SetChrSubChip(0x0036, 0)
    SetChrSubChip(0x0037, 0)
    SetChrSubChip(0x0038, 0)
    SetChrSubChip(0x0049, 0)
    SetChrSubChip(0x004A, 0)
    SetChrSubChip(0x004B, 0)
    SetChrSubChip(0x004C, 0)
    SetChrPos(0x0028, 35820, 0, -960, 90)
    SetChrPos(0x0029, 34250, 0, 720, 90)
    SetChrPos(0x002A, 34250, 0, -320, 90)
    SetChrPos(0x002B, 34250, 0, -1560, 90)
    SetChrPos(0x002C, 34250, 0, -2570, 90)
    SetChrPos(0x002D, 33000, 0, 720, 90)
    SetChrPos(0x002E, 33000, 0, -320, 90)
    SetChrPos(0x002F, 33000, 0, -1560, 90)
    SetChrPos(0x0030, 33000, 0, -2570, 90)
    SetChrPos(0x0031, 31750, 0, 720, 90)
    SetChrPos(0x0032, 31750, 0, -320, 90)
    SetChrPos(0x0033, 31750, 0, -1560, 90)
    SetChrPos(0x0034, 31750, 0, -2570, 90)
    SetChrPos(0x0035, 30500, 0, 720, 90)
    SetChrPos(0x0036, 30500, 0, -320, 90)
    SetChrPos(0x0037, 30500, 0, -1560, 90)
    SetChrPos(0x0038, 30500, 0, -2570, 90)
    SetChrPos(0x0049, 42120, 250, -7020, 90)
    SetChrPos(0x004A, 99670, 250, 40980, 180)
    SetChrPos(0x004B, 94910, 250, 44180, 90)
    ClearChrFlags(0x0028, 0x0080)
    ClearChrFlags(0x0029, 0x0080)
    ClearChrFlags(0x002A, 0x0080)
    ClearChrFlags(0x002B, 0x0080)
    ClearChrFlags(0x002C, 0x0080)
    ClearChrFlags(0x002D, 0x0080)
    ClearChrFlags(0x002E, 0x0080)
    ClearChrFlags(0x002F, 0x0080)
    ClearChrFlags(0x0030, 0x0080)
    ClearChrFlags(0x0031, 0x0080)
    ClearChrFlags(0x0032, 0x0080)
    ClearChrFlags(0x0033, 0x0080)
    ClearChrFlags(0x0034, 0x0080)
    ClearChrFlags(0x0035, 0x0080)
    ClearChrFlags(0x0036, 0x0080)
    ClearChrFlags(0x0037, 0x0080)
    ClearChrFlags(0x0038, 0x0080)
    ClearChrFlags(0x004A, 0x0080)
    ClearChrFlags(0x004B, 0x0080)
    OP_6D(41080, 0, -1410, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(235000, 0)
    OP_6E(262, 0)
    LoadEffect(0x00, 'map\\\\mp009_00.eff')
    LoadEffect(0x01, 'monster\\\\msc0100.eff')
    LoadEffect(0x02, 'Craft\\\\cr161_00.eff')
    LoadEffect(0x03, 'map\\\\mp032_00.eff')
    LoadEffect(0x04, 'map\\\\mpsmk0.eff')
    LoadEffect(0x05, 'map\\\\mpfire2.eff')
    LoadEffect(0x06, 'map\\\\mpkaji0.eff')
    LoadEffect(0x07, 'monster\\ms00300.eff')
    OP_22(0x0087, 0x01, 0x50)
    OP_22(0x00AE, 0x01, 0x50)
    PlayEffect(0x06, 0xFF, 0x00FF, 50440, 0, 64220, 0, 0, 0, 2000, 2000, 2000, 0x00FF, 0, 0, 0, 0)
    OP_C8(0x0200, 0x0046, 'C_PLAC24._CH', 0x01, 0x03E8)
    FadeIn(1000, 0)
    Sleep(300)

    @scena.Lambda('lambda_4A5B')
    def lambda_4A5B():
        OP_6D(43810, 0, -2060, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_4A5B)

    @scena.Lambda('lambda_4A73')
    def lambda_4A73():
        OP_67(0, 6770, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4A73)

    @scena.Lambda('lambda_4A8B')
    def lambda_4A8B():
        OP_6B(2200, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_4A8B)

    @scena.Lambda('lambda_4A9B')
    def lambda_4A9B():
        OP_6E(368, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_4A9B)

    @scena.Lambda('lambda_4AAB')
    def lambda_4AAB():
        OP_94(0x00, 0x00FE, 0x0000, 0x00002BAC, 0x00000BB8, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_4AAB)

    Sleep(80)

    @scena.Lambda('lambda_4AC6')
    def lambda_4AC6():
        OP_94(0x00, 0x00FE, 0x0000, 0x00002BAC, 0x00000BB8, 0x00)

        ExitThread()

    DispatchAsync(0x0029, 0x0001, lambda_4AC6)

    @scena.Lambda('lambda_4ADC')
    def lambda_4ADC():
        OP_94(0x00, 0x00FE, 0x0000, 0x00002BAC, 0x00000BB8, 0x00)

        ExitThread()

    DispatchAsync(0x002D, 0x0001, lambda_4ADC)

    @scena.Lambda('lambda_4AF2')
    def lambda_4AF2():
        OP_94(0x00, 0x00FE, 0x0000, 0x00002BAC, 0x00000BB8, 0x00)

        ExitThread()

    DispatchAsync(0x0031, 0x0001, lambda_4AF2)

    @scena.Lambda('lambda_4B08')
    def lambda_4B08():
        OP_94(0x00, 0x00FE, 0x0000, 0x00002BAC, 0x00000BB8, 0x00)

        ExitThread()

    DispatchAsync(0x0035, 0x0001, lambda_4B08)

    Sleep(80)

    @scena.Lambda('lambda_4B23')
    def lambda_4B23():
        OP_94(0x00, 0x00FE, 0x0000, 0x00002BAC, 0x00000BB8, 0x00)

        ExitThread()

    DispatchAsync(0x002A, 0x0001, lambda_4B23)

    @scena.Lambda('lambda_4B39')
    def lambda_4B39():
        OP_94(0x00, 0x00FE, 0x0000, 0x00002BAC, 0x00000BB8, 0x00)

        ExitThread()

    DispatchAsync(0x002E, 0x0001, lambda_4B39)

    @scena.Lambda('lambda_4B4F')
    def lambda_4B4F():
        OP_94(0x00, 0x00FE, 0x0000, 0x00002BAC, 0x00000BB8, 0x00)

        ExitThread()

    DispatchAsync(0x0032, 0x0001, lambda_4B4F)

    @scena.Lambda('lambda_4B65')
    def lambda_4B65():
        OP_94(0x00, 0x00FE, 0x0000, 0x00002BAC, 0x00000BB8, 0x00)

        ExitThread()

    DispatchAsync(0x0036, 0x0001, lambda_4B65)

    Sleep(80)

    @scena.Lambda('lambda_4B80')
    def lambda_4B80():
        OP_94(0x00, 0x00FE, 0x0000, 0x00002BAC, 0x00000BB8, 0x00)

        ExitThread()

    DispatchAsync(0x002B, 0x0001, lambda_4B80)

    @scena.Lambda('lambda_4B96')
    def lambda_4B96():
        OP_94(0x00, 0x00FE, 0x0000, 0x00002BAC, 0x00000BB8, 0x00)

        ExitThread()

    DispatchAsync(0x002F, 0x0001, lambda_4B96)

    @scena.Lambda('lambda_4BAC')
    def lambda_4BAC():
        OP_94(0x00, 0x00FE, 0x0000, 0x00002BAC, 0x00000BB8, 0x00)

        ExitThread()

    DispatchAsync(0x0033, 0x0001, lambda_4BAC)

    @scena.Lambda('lambda_4BC2')
    def lambda_4BC2():
        OP_94(0x00, 0x00FE, 0x0000, 0x00002BAC, 0x00000BB8, 0x00)

        ExitThread()

    DispatchAsync(0x0037, 0x0001, lambda_4BC2)

    Sleep(80)

    @scena.Lambda('lambda_4BDD')
    def lambda_4BDD():
        OP_94(0x00, 0x00FE, 0x0000, 0x00002BAC, 0x00000BB8, 0x00)

        ExitThread()

    DispatchAsync(0x002C, 0x0001, lambda_4BDD)

    @scena.Lambda('lambda_4BF3')
    def lambda_4BF3():
        OP_94(0x00, 0x00FE, 0x0000, 0x00002BAC, 0x00000BB8, 0x00)

        ExitThread()

    DispatchAsync(0x0030, 0x0001, lambda_4BF3)

    @scena.Lambda('lambda_4C09')
    def lambda_4C09():
        OP_94(0x00, 0x00FE, 0x0000, 0x00002BAC, 0x00000BB8, 0x00)

        ExitThread()

    DispatchAsync(0x0034, 0x0001, lambda_4C09)

    @scena.Lambda('lambda_4C1F')
    def lambda_4C1F():
        OP_94(0x00, 0x00FE, 0x0000, 0x00002BAC, 0x00000BB8, 0x00)

        ExitThread()

    DispatchAsync(0x0038, 0x0001, lambda_4C1F)

    WaitForThreadExit(0x0028, 0x0001)
    OP_8C(0x0028, 270, 400)
    WaitForThreadExit(0x0035, 0x0001)
    SetChrChipByIndex(0x0029, 1)
    SetChrChipByIndex(0x002D, 1)
    SetChrChipByIndex(0x0031, 4)
    SetChrChipByIndex(0x0035, 4)
    OP_22(0x00D5, 0x00, 0x64)
    WaitForThreadExit(0x0036, 0x0001)
    SetChrChipByIndex(0x002A, 1)
    SetChrChipByIndex(0x002E, 1)
    SetChrChipByIndex(0x0032, 4)
    SetChrChipByIndex(0x0036, 4)
    OP_22(0x00D5, 0x00, 0x64)
    WaitForThreadExit(0x0037, 0x0001)
    SetChrChipByIndex(0x002B, 1)
    SetChrChipByIndex(0x002F, 1)
    SetChrChipByIndex(0x0033, 4)
    SetChrChipByIndex(0x0037, 4)
    OP_22(0x00D5, 0x00, 0x64)
    WaitForThreadExit(0x0038, 0x0001)
    SetChrChipByIndex(0x002C, 1)
    SetChrChipByIndex(0x0030, 1)
    SetChrChipByIndex(0x0034, 4)
    SetChrChipByIndex(0x0038, 4)
    OP_22(0x00D5, 0x00, 0x64)
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(500)

    ChrTalk(
        0x0028,
        (
            '#0610380464V#1186F#6P现在开始对人形兵器和\n',
            '猎兵团进行扫荡！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610380465V保护市民和支援\n',
            '正规军是我们的首要任务！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    SetMessageWindowPos(250, 100, -1, -1)
    SetChrName('特务兵们')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#2620380466V#5S是，长官！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x00000064)
    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_DB()
    SetChrChipByIndex(0x0029, 2)
    SetChrChipByIndex(0x002A, 2)
    SetChrChipByIndex(0x002B, 2)
    SetChrChipByIndex(0x002C, 2)
    CreateThread(0x0029, 0x00, 0x01, 0x002F)
    CreateThread(0x002A, 0x00, 0x01, 0x0030)
    CreateThread(0x002B, 0x00, 0x01, 0x0031)
    CreateThread(0x002C, 0x00, 0x01, 0x0032)
    Sleep(100)

    SetChrChipByIndex(0x002D, 2)
    SetChrChipByIndex(0x002E, 2)
    SetChrChipByIndex(0x002F, 2)
    SetChrChipByIndex(0x0030, 2)
    CreateThread(0x002D, 0x00, 0x01, 0x002F)
    CreateThread(0x002E, 0x00, 0x01, 0x0030)
    CreateThread(0x002F, 0x00, 0x01, 0x0031)
    CreateThread(0x0030, 0x00, 0x01, 0x0032)
    Sleep(100)

    SetChrChipByIndex(0x0031, 6)
    SetChrChipByIndex(0x0032, 6)
    SetChrChipByIndex(0x0033, 6)
    SetChrChipByIndex(0x0034, 6)
    CreateThread(0x0031, 0x00, 0x01, 0x002F)
    CreateThread(0x0032, 0x00, 0x01, 0x0030)
    CreateThread(0x0033, 0x00, 0x01, 0x0031)
    CreateThread(0x0034, 0x00, 0x01, 0x0032)
    Sleep(100)

    SetChrChipByIndex(0x0035, 6)
    SetChrChipByIndex(0x0036, 6)
    SetChrChipByIndex(0x0037, 6)
    SetChrChipByIndex(0x0038, 6)
    CreateThread(0x0035, 0x00, 0x01, 0x002F)
    CreateThread(0x0036, 0x00, 0x01, 0x0030)
    CreateThread(0x0037, 0x00, 0x01, 0x0031)
    CreateThread(0x0038, 0x00, 0x01, 0x0032)
    Sleep(100)

    @scena.Lambda('lambda_4E60')
    def lambda_4E60():
        OP_6D(47810, 0, -2060, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_4E60)

    OP_8C(0x0028, 90, 400)
    Sleep(1000)

    FadeOut(1000, 0, -1)
    OP_0D()
    TerminateThread(0x0101, 0x00)
    TerminateThread(0x0029, 0x00)
    TerminateThread(0x002A, 0x00)
    TerminateThread(0x002B, 0x00)
    TerminateThread(0x002C, 0x00)
    TerminateThread(0x002D, 0x00)
    TerminateThread(0x002E, 0x00)
    TerminateThread(0x002F, 0x00)
    TerminateThread(0x0030, 0x00)
    TerminateThread(0x0031, 0x00)
    TerminateThread(0x0032, 0x00)
    TerminateThread(0x0033, 0x00)
    TerminateThread(0x0034, 0x00)
    TerminateThread(0x0035, 0x00)
    TerminateThread(0x0036, 0x00)
    TerminateThread(0x0037, 0x00)
    TerminateThread(0x0038, 0x00)
    OP_6D(97060, 250, 34890, 0)
    OP_67(0, 8290, -10000, 0)
    OP_6B(3120, 0)
    OP_6C(40000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x0043, 0x0080)
    ClearChrFlags(0x0044, 0x0080)
    ClearChrFlags(0x0045, 0x0080)
    ClearChrFlags(0x0046, 0x0080)
    SetChrFlags(0x0043, 0x0004)
    SetChrFlags(0x0044, 0x0004)
    SetChrFlags(0x0045, 0x0004)
    SetChrFlags(0x0046, 0x0004)
    SetChrChipByIndex(0x0043, 20)
    SetChrChipByIndex(0x0044, 20)
    SetChrChipByIndex(0x0045, 13)
    SetChrChipByIndex(0x0046, 13)
    SetChrSubChip(0x0043, 0)
    SetChrSubChip(0x0044, 0)
    SetChrSubChip(0x0045, 0)
    SetChrSubChip(0x0046, 0)
    SetChrPos(0x0043, 100320, 1000, 33430, 270)
    SetChrPos(0x0044, 103220, 1000, 36090, 270)
    SetChrPos(0x0045, 96780, 550, 70110, 180)
    SetChrPos(0x0046, 94780, 550, 70110, 180)
    SetChrPos(0x0029, 95630, 250, 61420, 180)
    SetChrPos(0x0031, 95850, 0, 24930, 0)
    SetChrPos(0x0032, 88010, 0, 35790, 90)
    SetChrPos(0x0033, 89710, 0, 40080, 90)
    ClearChrFlags(0x0031, 0x0080)
    ClearChrFlags(0x0032, 0x0080)
    ClearChrFlags(0x0033, 0x0080)
    SetChrFlags(0x0029, 0x0020)
    SetChrFlags(0x002A, 0x0020)
    SetChrFlags(0x002B, 0x0020)
    SetChrFlags(0x002C, 0x0020)
    SetChrFlags(0x0031, 0x0020)
    SetChrFlags(0x0032, 0x0020)
    SetChrFlags(0x0033, 0x0020)
    SetChrFlags(0x0034, 0x0020)
    SetChrFlags(0x0043, 0x0020)

    @scena.Lambda('lambda_5024')
    def lambda_5024():
        OP_99(0x00FE, 0x00, 0x07, 0x000005DC)
        Yield()

        Jump('lambda_5024')

    DispatchAsync2(0x0043, 0x0002, lambda_5024)

    CreateThread(0x0028, 0x03, 0x01, 0x0047)

    @scena.Lambda('lambda_503E')
    def lambda_503E():
        OP_8F(0x00FE, 90900, 1000, 33430, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0043, 0x0001, lambda_503E)

    CreateThread(0x0043, 0x00, 0x01, 0x0033)
    Sleep(400)

    SetChrFlags(0x0044, 0x0020)

    @scena.Lambda('lambda_506A')
    def lambda_506A():
        OP_99(0x00FE, 0x00, 0x07, 0x000005DC)
        Yield()

        Jump('lambda_506A')

    DispatchAsync2(0x0044, 0x0002, lambda_506A)

    @scena.Lambda('lambda_507D')
    def lambda_507D():
        OP_8F(0x00FE, 93400, 1000, 36090, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0044, 0x0001, lambda_507D)

    FadeIn(1000, 0)
    OP_0D()
    Sleep(1000)

    @scena.Lambda('lambda_50A7')
    def lambda_50A7():
        OP_6D(96790, 250, 33400, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_50A7)

    @scena.Lambda('lambda_50BF')
    def lambda_50BF():
        OP_67(0, 5810, -10000, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_50BF)

    @scena.Lambda('lambda_50D7')
    def lambda_50D7():
        OP_6B(2860, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_50D7)

    SetChrChipByIndex(0x0031, 6)
    SetChrSubChip(0x0031, 0)
    OP_7D(0x00, 0x0031, 0x0032, 0x00C8)
    ClearChrFlags(0x0031, 0x0020)

    @scena.Lambda('lambda_50FE')
    def lambda_50FE():
        OP_8E(0x00FE, 95850, 0, 28780, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0031, 0x0001, lambda_50FE)

    WaitForThreadExit(0x0031, 0x0001)
    OP_7D(0x01, 0x0031, 0x0000, 0x0000)
    SetChrFlags(0x0031, 0x0020)
    SetChrChipByIndex(0x0031, 23)
    SetChrSubChip(0x0031, 1)

    @scena.Lambda('lambda_5135')
    def lambda_5135():
        OP_96(0x00FE, 0x0001766A, 0x00000000, 0x00007E68, 0x000003E8, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x0031, 0x0001, lambda_5135)

    Sleep(300)

    @scena.Lambda('lambda_5158')
    def lambda_5158():
        OP_99(0x00FE, 0x01, 0x04, 0x000007D0)

        ExitThread()

    DispatchAsync(0x0031, 0x0002, lambda_5158)

    Sleep(100)

    @scena.Lambda('lambda_516D')
    def lambda_516D():
        OP_6D(96820, 250, 35080, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_516D)

    TerminateThread(0x0028, 0x03)
    OP_23(0x013A)
    OP_22(0x00D6, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x0043, 0, 500, -1000, 0, 0, 0, 2000, 2000, 2000, 0x00FF, 0, 0, 0, 0)
    OP_7C(0x00000000, 0x00000190, 0x00000BB8, 0x000000C8)
    TerminateThread(0x0043, 0x01)
    TerminateThread(0x0044, 0x01)
    TerminateThread(0x0043, 0x02)
    SetChrChipByIndex(0x0044, 12)
    SetChrSubChip(0x0044, 0)
    SetChrChipByIndex(0x0043, 12)
    SetChrSubChip(0x0043, 0)

    @scena.Lambda('lambda_51F7')
    def lambda_51F7():
        OP_8C(0x00FE, 220, 200)

        ExitThread()

    DispatchAsync(0x0044, 0x0003, lambda_51F7)

    @scena.Lambda('lambda_5205')
    def lambda_5205():
        OP_8F(0x00FE, 95080, 750, 36500, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x0043, 0x0001, lambda_5205)

    @scena.Lambda('lambda_5220')
    def lambda_5220():
        OP_9E(0x00FE, 0x0000003C, 0x00000000, 0x000002BC, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x0043, 0x0002, lambda_5220)

    @scena.Lambda('lambda_523A')
    def lambda_523A():
        OP_8C(0x00FE, 175, 400)

        ExitThread()

    DispatchAsync(0x0043, 0x0003, lambda_523A)

    WaitForThreadExit(0x0043, 0x0001)

    @scena.Lambda('lambda_524D')
    def lambda_524D():
        OP_99(0x00FE, 0x00, 0x07, 0x000005DC)
        Yield()

        Jump('lambda_524D')

    DispatchAsync2(0x0043, 0x0002, lambda_524D)

    TerminateThread(0x0044, 0x02)
    SetChrChipByIndex(0x0044, 21)
    SetChrSubChip(0x0044, 0)

    @scena.Lambda('lambda_526E')
    def lambda_526E():
        OP_99(0x00FE, 0x00, 0x02, 0x000005DC)

        ExitThread()

    DispatchAsync(0x0044, 0x0002, lambda_526E)

    Sleep(400)

    @scena.Lambda('lambda_5283')
    def lambda_5283():
        OP_99(0x00FE, 0x02, 0x05, 0x000009C4)

        ExitThread()

    DispatchAsync(0x0044, 0x0002, lambda_5283)

    @scena.Lambda('lambda_5293')
    def lambda_5293():
        OP_8F(0x00FE, 96850, 1000, 33660, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0044, 0x0001, lambda_5293)

    Sleep(100)

    OP_7D(0x00, 0x0031, 0x0014, 0x0064)
    SetChrChipByIndex(0x0031, 6)
    SetChrSubChip(0x0031, 0)

    @scena.Lambda('lambda_52C5')
    def lambda_52C5():
        OP_8C(0x00FE, 310, 400)

        ExitThread()

    DispatchAsync(0x0031, 0x0003, lambda_52C5)

    @scena.Lambda('lambda_52D3')
    def lambda_52D3():
        OP_96(0x00FE, 0x0001836C, 0x000000FA, 0x000078A0, 0x000001F4, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x0031, 0x0001, lambda_52D3)

    Sleep(100)

    OP_22(0x0084, 0x00, 0x64)
    WaitForThreadExit(0x0031, 0x0001)
    OP_22(0x00A4, 0x00, 0x64)
    OP_7D(0x01, 0x0031, 0x0000, 0x0000)

    @scena.Lambda('lambda_530D')
    def lambda_530D():
        OP_6C(55000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_530D)

    @scena.Lambda('lambda_531D')
    def lambda_531D():
        OP_6B(3000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_531D)

    SetChrChipByIndex(0x0032, 7)
    SetChrSubChip(0x0032, 1)

    @scena.Lambda('lambda_5337')
    def lambda_5337():
        OP_96(0x00FE, 0x00016D78, 0x00000000, 0x00008E94, 0x000001F4, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0032, 0x0001, lambda_5337)

    Sleep(300)

    @scena.Lambda('lambda_535A')
    def lambda_535A():
        OP_99(0x00FE, 0x01, 0x05, 0x000007D0)

        ExitThread()

    DispatchAsync(0x0032, 0x0002, lambda_535A)

    Sleep(200)

    @scena.Lambda('lambda_536F')
    def lambda_536F():
        OP_6D(98560, 250, 36300, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_536F)

    OP_22(0x00D6, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x0043, -1000, 500, 0, 0, 0, 0, 2000, 2000, 2000, 0x00FF, 0, 0, 0, 0)
    OP_7C(0x00000000, 0x00000190, 0x00000BB8, 0x000000C8)

    @scena.Lambda('lambda_53D2')
    def lambda_53D2():
        OP_8F(0x00FE, 98740, 1000, 37110, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x0043, 0x0001, lambda_53D2)

    @scena.Lambda('lambda_53ED')
    def lambda_53ED():
        OP_9E(0x00FE, 0x0000003C, 0x00000000, 0x000002BC, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x0043, 0x0002, lambda_53ED)

    @scena.Lambda('lambda_5407')
    def lambda_5407():
        OP_8C(0x00FE, 280, 400)

        ExitThread()

    DispatchAsync(0x0043, 0x0003, lambda_5407)

    SetChrFlags(0x0033, 0x0004)
    SetChrChipByIndex(0x0033, 6)
    SetChrSubChip(0x0033, 2)
    OP_7D(0x00, 0x0033, 0x0032, 0x00C8)

    @scena.Lambda('lambda_542C')
    def lambda_542C():
        OP_96(0x00FE, 0x00017AAC, 0x000000FA, 0x00009C90, 0x000001F4, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0033, 0x0001, lambda_542C)

    WaitForThreadExit(0x0033, 0x0001)
    OP_22(0x00A4, 0x00, 0x64)
    OP_7D(0x01, 0x0033, 0x0000, 0x0000)
    OP_8C(0x0033, 160, 0)

    @scena.Lambda('lambda_5463')
    def lambda_5463():
        OP_6D(99800, 250, 37640, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_5463)

    @scena.Lambda('lambda_547B')
    def lambda_547B():
        OP_67(0, 4650, -10000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_547B)

    @scena.Lambda('lambda_5493')
    def lambda_5493():
        OP_6B(3190, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_5493)

    @scena.Lambda('lambda_54A3')
    def lambda_54A3():
        OP_96(0x00FE, 0x00018312, 0x000007D0, 0x000091E6, 0x000009C4, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x0033, 0x0001, lambda_54A3)

    WaitForThreadExit(0x0033, 0x0001)
    OP_22(0x00A4, 0x00, 0x64)
    CreateThread(0x0031, 0x00, 0x01, 0x0034)
    OP_8C(0x0033, 225, 0)
    SetChrFlags(0x0033, 0x0800)
    SetChrChipByIndex(0x0033, 23)
    SetChrSubChip(0x0033, 1)

    @scena.Lambda('lambda_54E8')
    def lambda_54E8():
        OP_96(0x00FE, 0x00017D0E, 0x000000FA, 0x000089B2, 0x000003E8, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x0033, 0x0001, lambda_54E8)

    Sleep(200)

    @scena.Lambda('lambda_550B')
    def lambda_550B():
        OP_99(0x00FE, 0x01, 0x05, 0x000007D0)

        ExitThread()

    DispatchAsync(0x0033, 0x0002, lambda_550B)

    Sleep(200)

    @scena.Lambda('lambda_5520')
    def lambda_5520():
        OP_6D(98770, 250, 35640, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_5520)

    OP_22(0x00D6, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x0044, 900, 500, 1200, 0, 0, 0, 2000, 2000, 2000, 0x00FF, 0, 0, 0, 0)
    OP_7C(0x00000000, 0x00000190, 0x00000BB8, 0x000000C8)
    SetChrChipByIndex(0x0044, 22)
    SetChrSubChip(0x0044, 0)

    @scena.Lambda('lambda_558D')
    def lambda_558D():
        OP_8F(0x00FE, 95130, 750, 32049, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x0044, 0x0001, lambda_558D)

    @scena.Lambda('lambda_55A8')
    def lambda_55A8():
        OP_9E(0x00FE, 0x0000003C, 0x00000000, 0x000002BC, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x0044, 0x0002, lambda_55A8)

    WaitForThreadExit(0x0044, 0x0001)
    SetChrFlags(0x0032, 0x0800)
    SetChrChipByIndex(0x0032, 7)
    SetChrSubChip(0x0032, 0)

    @scena.Lambda('lambda_55D6')
    def lambda_55D6():
        OP_96(0x00FE, 0x0001712E, 0x00000000, 0x0000843A, 0x000005DC, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x0032, 0x0001, lambda_55D6)

    OP_8C(0x0032, 190, 1000)
    OP_8C(0x0032, 270, 1000)
    OP_8C(0x0032, 0, 1000)
    OP_8C(0x0032, 90, 1000)
    Sleep(50)

    OP_8C(0x0032, 190, 0)

    @scena.Lambda('lambda_561C')
    def lambda_561C():
        OP_99(0x00FE, 0x01, 0x05, 0x000007D0)

        ExitThread()

    DispatchAsync(0x0032, 0x0002, lambda_561C)

    Sleep(100)

    @scena.Lambda('lambda_5631')
    def lambda_5631():
        OP_6D(97710, 250, 35190, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_5631)

    OP_22(0x00D6, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x0044, -500, 500, 1000, 0, 0, 0, 2000, 2000, 2000, 0x00FF, 0, 0, 0, 0)
    OP_7C(0x00000000, 0x00000190, 0x00000BB8, 0x000000C8)

    @scena.Lambda('lambda_5694')
    def lambda_5694():
        OP_8F(0x00FE, 94590, 750, 30140, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x0044, 0x0001, lambda_5694)

    @scena.Lambda('lambda_56AF')
    def lambda_56AF():
        OP_9E(0x00FE, 0x0000003C, 0x00000000, 0x000002BC, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x0044, 0x0002, lambda_56AF)

    @scena.Lambda('lambda_56C9')
    def lambda_56C9():
        OP_8C(0x00FE, 190, 400)

        ExitThread()

    DispatchAsync(0x0044, 0x0003, lambda_56C9)

    WaitForThreadExit(0x0044, 0x0001)

    @scena.Lambda('lambda_56DC')
    def lambda_56DC():
        OP_9E(0x00FE, 0x00000014, 0x00000000, 0x00000000, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x0044, 0x0002, lambda_56DC)

    Sleep(1000)

    PlayEffect(0x01, 0x02, 0x0044, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_83(0x01, 0x02)
    TerminateThread(0x0044, 0x02)
    SetChrFlags(0x0044, 0x0080)
    OP_83(0x01, 0x00)
    WaitForThreadExit(0x0031, 0x0000)
    Sleep(600)

    OP_22(0x0193, 0x00, 0x64)
    Sleep(600)

    SetChrChipByIndex(0x0032, 5)
    SetChrSubChip(0x0032, 0)

    @scena.Lambda('lambda_575D')
    def lambda_575D():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0032, 0x0003, lambda_575D)

    Sleep(50)

    SetChrChipByIndex(0x0033, 5)
    SetChrSubChip(0x0033, 0)

    @scena.Lambda('lambda_577A')
    def lambda_577A():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0033, 0x0003, lambda_577A)

    Sleep(50)

    SetChrChipByIndex(0x0031, 5)
    SetChrSubChip(0x0031, 0)

    @scena.Lambda('lambda_5797')
    def lambda_5797():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0031, 0x0003, lambda_5797)

    @scena.Lambda('lambda_57A5')
    def lambda_57A5():
        OP_6D(96430, 250, 59720, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_57A5)

    @scena.Lambda('lambda_57BD')
    def lambda_57BD():
        OP_67(0, 7420, -10000, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_57BD)

    @scena.Lambda('lambda_57D5')
    def lambda_57D5():
        OP_6C(42000, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_57D5)

    @scena.Lambda('lambda_57E5')
    def lambda_57E5():
        OP_6B(2630, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_57E5)

    WaitForThreadExit(0x0101, 0x0000)
    SetChrChipByIndex(0x0031, 23)
    SetChrSubChip(0x0031, 2)
    SetChrChipByIndex(0x0032, 23)
    SetChrSubChip(0x0032, 2)
    SetChrFlags(0x0032, 0x0004)
    SetChrPos(0x0031, 88410, 250, 51790, 75)
    SetChrPos(0x0032, 102920, 1250, 51790, 255)
    SetChrChipByIndex(0x0046, 24)
    SetChrSubChip(0x0046, 0)
    CreateThread(0x0028, 0x03, 0x01, 0x0048)

    @scena.Lambda('lambda_5846')
    def lambda_5846():
        OP_8E(0x00FE, 94780, 550, 45190, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0046, 0x0001, lambda_5846)

    Sleep(200)

    SetChrChipByIndex(0x0045, 24)
    SetChrSubChip(0x0045, 0)

    @scena.Lambda('lambda_5870')
    def lambda_5870():
        OP_8E(0x00FE, 96780, 550, 45190, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0045, 0x0001, lambda_5870)

    Sleep(600)

    @scena.Lambda('lambda_5890')
    def lambda_5890():
        OP_6D(96430, 250, 52470, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_5890)

    Sleep(450)

    CreateThread(0x0046, 0x00, 0x01, 0x0035)
    Sleep(50)

    CreateThread(0x0045, 0x00, 0x01, 0x0036)
    WaitForThreadExit(0x0046, 0x0000)
    WaitForThreadExit(0x0045, 0x0000)
    Sleep(400)

    @scena.Lambda('lambda_58CF')
    def lambda_58CF():
        OP_6D(96010, 250, 52510, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_58CF)

    @scena.Lambda('lambda_58E7')
    def lambda_58E7():
        OP_6C(23000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_58E7)

    @scena.Lambda('lambda_58F7')
    def lambda_58F7():
        OP_6B(2530, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_58F7)

    SetChrChipByIndex(0x0031, 5)
    SetChrSubChip(0x0031, 0)

    @scena.Lambda('lambda_5911')
    def lambda_5911():
        OP_8C(0x00FE, 355, 400)

        ExitThread()

    DispatchAsync(0x0031, 0x0003, lambda_5911)

    @scena.Lambda('lambda_591F')
    def lambda_591F():
        OP_96(0x00FE, 0x0001723C, 0x000000FA, 0x0000BD4C, 0x000001F4, 0x000009C4)

        ExitThread()

    DispatchAsync(0x0031, 0x0001, lambda_591F)

    Sleep(200)

    SetChrChipByIndex(0x0032, 5)
    SetChrSubChip(0x0032, 0)

    @scena.Lambda('lambda_594C')
    def lambda_594C():
        OP_8C(0x00FE, 355, 400)

        ExitThread()

    DispatchAsync(0x0032, 0x0003, lambda_594C)

    @scena.Lambda('lambda_595A')
    def lambda_595A():
        OP_96(0x00FE, 0x00017A0C, 0x000000FA, 0x0000BF40, 0x000001F4, 0x000009C4)

        ExitThread()

    DispatchAsync(0x0032, 0x0001, lambda_595A)

    WaitForThreadExit(0x0031, 0x0001)
    ClearChrFlags(0x0031, 0x0800)
    OP_22(0x00A4, 0x00, 0x64)
    WaitForThreadExit(0x0032, 0x0001)
    ClearChrFlags(0x0032, 0x0800)
    ClearChrFlags(0x0032, 0x0004)
    OP_22(0x00A4, 0x00, 0x64)
    SetChrChipByIndex(0x0046, 26)
    SetChrSubChip(0x0046, 0)

    @scena.Lambda('lambda_59A5')
    def lambda_59A5():
        OP_99(0x00FE, 0x00, 0x03, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0046, 0x0002, lambda_59A5)

    Sleep(200)

    SetChrChipByIndex(0x0045, 26)
    SetChrSubChip(0x0045, 0)

    @scena.Lambda('lambda_59C4')
    def lambda_59C4():
        OP_99(0x00FE, 0x00, 0x03, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0045, 0x0002, lambda_59C4)

    WaitForThreadExit(0x0045, 0x0002)
    OP_22(0x0193, 0x00, 0x64)
    Sleep(1000)

    ClearChrFlags(0x0029, 0x0080)
    SetChrChipByIndex(0x0029, 3)
    SetChrSubChip(0x0029, 0)

    @scena.Lambda('lambda_59F2')
    def lambda_59F2():
        OP_6D(96010, 250, 58040, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_59F2)

    WaitForThreadExit(0x0101, 0x0000)
    Sleep(400)

    @scena.Lambda('lambda_5A14')
    def lambda_5A14():
        OP_6D(96010, 250, 57370, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_5A14)

    @scena.Lambda('lambda_5A2C')
    def lambda_5A2C():
        OP_67(0, 5360, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5A2C)

    @scena.Lambda('lambda_5A44')
    def lambda_5A44():
        OP_6C(40000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_5A44)

    @scena.Lambda('lambda_5A54')
    def lambda_5A54():
        OP_99(0x00FE, 0x00, 0x02, 0x000005DC)

        ExitThread()

    DispatchAsync(0x0029, 0x0002, lambda_5A54)

    Sleep(100)

    OP_82(0x01, 0x00)
    PlayEffect(0x07, 0x01, 0x0029, -200, 400, -800, 0, 0, 0, 1000, 1000, 1000, 0x0045, 0, 0, -200, 0)
    Sleep(40)

    PlayEffect(0x07, 0x02, 0x0029, 200, 400, -800, 0, 0, 0, 1000, 1000, 1000, 0x0046, 0, 0, -200, 0)
    Sleep(40)

    PlayEffect(0x07, 0x03, 0x0029, -200, 400, -800, 0, 0, 0, 1000, 1000, 1000, 0x0045, 200, 0, 0, 0)
    Sleep(40)

    PlayEffect(0x07, 0x04, 0x0029, 200, 400, -800, 0, 0, 0, 1000, 1000, 1000, 0x0046, -200, 0, 0, 0)
    Sleep(1300)

    OP_7C(0x00000000, 0x00000190, 0x00000BB8, 0x000000C8)
    CreateThread(0x0046, 0x00, 0x01, 0x0037)
    Sleep(50)

    OP_7C(0x00000000, 0x00000190, 0x00000BB8, 0x000000C8)
    CreateThread(0x0045, 0x00, 0x01, 0x0038)
    WaitForThreadExit(0x0046, 0x0000)
    WaitForThreadExit(0x0045, 0x0000)
    SetChrChipByIndex(0x0029, 1)
    SetChrSubChip(0x0029, 0)
    OP_8C(0x0029, 0, 800)

    @scena.Lambda('lambda_5BA4')
    def lambda_5BA4():
        OP_6B(3530, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_5BA4)

    SetChrChipByIndex(0x0029, 2)
    SetChrSubChip(0x0029, 0)
    ClearChrFlags(0x0029, 0x0020)

    @scena.Lambda('lambda_5BC3')
    def lambda_5BC3():
        OP_8E(0x00FE, 95630, 250, 70000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0029, 0x0001, lambda_5BC3)

    SetChrChipByIndex(0x0031, 6)
    SetChrSubChip(0x0031, 0)
    ClearChrFlags(0x0031, 0x0020)
    SetChrChipByIndex(0x0032, 6)
    SetChrSubChip(0x0032, 0)
    ClearChrFlags(0x0032, 0x0020)

    @scena.Lambda('lambda_5BFC')
    def lambda_5BFC():
        OP_8E(0x00FE, 96780, 250, 70000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0032, 0x0001, lambda_5BFC)

    Sleep(100)

    @scena.Lambda('lambda_5C1C')
    def lambda_5C1C():
        OP_8E(0x00FE, 94780, 250, 70000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0031, 0x0001, lambda_5C1C)

    Sleep(400)

    FadeOut(1000, 0, -1)
    OP_0D()
    LoadEffect(0x01, 'monster\\\\msc0568.eff')
    LoadEffect(0x02, 'monster\\\\msc0555.eff')
    LoadEffect(0x07, 'map\\\\mp003_00.eff')
    TerminateThread(0x0101, 0x00)
    TerminateThread(0x0029, 0x01)
    TerminateThread(0x0031, 0x01)
    TerminateThread(0x0032, 0x01)
    SetChrPos(0x0049, 40700, 1250, 46910, 270)
    SetChrPos(0x004A, 99670, 250, 40980, 180)
    SetChrPos(0x004B, 94910, 250, 44180, 90)
    OP_6D(70190, 1250, 52590, 0)
    OP_67(0, 10000, -10000, 0)
    OP_6B(3160, 0)
    OP_6C(156000, 0)
    OP_6E(262, 0)
    SetChrChipByIndex(0x0039, 29)
    SetChrChipByIndex(0x003A, 29)
    SetChrChipByIndex(0x003B, 35)
    SetChrChipByIndex(0x003C, 35)
    SetChrChipByIndex(0x003D, 35)
    SetChrChipByIndex(0x0029, 0)
    SetChrChipByIndex(0x002A, 0)
    SetChrChipByIndex(0x002B, 2)
    SetChrChipByIndex(0x002C, 2)
    SetChrChipByIndex(0x002D, 2)
    SetChrChipByIndex(0x0031, 4)
    SetChrSubChip(0x0039, 0)
    SetChrSubChip(0x003A, 0)
    SetChrSubChip(0x003B, 0)
    SetChrSubChip(0x003C, 0)
    SetChrSubChip(0x003D, 0)
    SetChrSubChip(0x0029, 0)
    SetChrSubChip(0x002A, 0)
    SetChrSubChip(0x002B, 0)
    SetChrSubChip(0x002C, 0)
    SetChrSubChip(0x002D, 0)
    SetChrSubChip(0x0031, 0)
    SetChrPos(0x0039, 81020, 1250, 53150, 0)
    SetChrPos(0x003A, 59440, 1250, 53150, 0)
    SetChrPos(0x003B, 70350, 1250, 33350, 0)
    SetChrPos(0x003C, 68900, 1250, 31550, 0)
    SetChrPos(0x003D, 71360, 1250, 31750, 0)
    SetChrPos(0x0029, 59440, 1250, 53150, 90)
    SetChrPos(0x002A, 81020, 1250, 53150, 270)
    SetChrPos(0x002B, 70130, 1250, 35150, 0)
    SetChrPos(0x002C, 71250, 1250, 33950, 0)
    SetChrPos(0x002D, 69040, 1250, 33380, 0)
    SetChrPos(0x0031, 69960, 250, 66900, 180)
    ClearChrFlags(0x0039, 0x0080)
    ClearChrFlags(0x003A, 0x0080)
    ClearChrFlags(0x003B, 0x0080)
    ClearChrFlags(0x003C, 0x0080)
    ClearChrFlags(0x003D, 0x0080)
    SetChrFlags(0x0029, 0x0080)
    SetChrFlags(0x002A, 0x0080)
    SetChrFlags(0x0031, 0x0080)
    SetChrFlags(0x0039, 0x0040)
    SetChrFlags(0x003A, 0x0040)
    SetChrFlags(0x003B, 0x0040)
    SetChrFlags(0x003C, 0x0040)
    SetChrFlags(0x003D, 0x0040)
    SetChrFlags(0x0029, 0x0040)
    SetChrFlags(0x002A, 0x0040)
    SetChrFlags(0x002B, 0x0040)
    SetChrFlags(0x002C, 0x0040)
    SetChrFlags(0x002D, 0x0040)
    SetChrFlags(0x0031, 0x0040)

    @scena.Lambda('lambda_5E91')
    def lambda_5E91():
        OP_6B(2800, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_5E91)

    FadeIn(1000, 0)

    @scena.Lambda('lambda_5EAA')
    def lambda_5EAA():
        OP_8E(0x00FE, 71020, 1250, 53150, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0039, 0x0001, lambda_5EAA)

    Sleep(400)

    @scena.Lambda('lambda_5ECA')
    def lambda_5ECA():
        OP_8E(0x00FE, 69440, 1250, 53150, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x003A, 0x0001, lambda_5ECA)

    OP_0D()
    WaitForThreadExit(0x0039, 0x0001)
    SetChrChipByIndex(0x0039, 14)
    SetChrSubChip(0x0039, 0)
    WaitForThreadExit(0x003A, 0x0001)
    SetChrChipByIndex(0x003A, 14)
    SetChrSubChip(0x003A, 0)
    WaitForThreadExit(0x0101, 0x0000)
    ClearChrFlags(0x0029, 0x0080)
    ClearChrFlags(0x002A, 0x0080)
    ClearChrFlags(0x0031, 0x0080)
    CreateThread(0x0029, 0x00, 0x01, 0x0039)
    Sleep(400)

    @scena.Lambda('lambda_5F24')
    def lambda_5F24():
        OP_6D(70280, 1250, 52460, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_5F24)

    @scena.Lambda('lambda_5F3C')
    def lambda_5F3C():
        OP_6B(2150, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5F3C)

    Sleep(200)

    CreateThread(0x002A, 0x00, 0x01, 0x003C)
    WaitForThreadExit(0x0029, 0x0000)

    @scena.Lambda('lambda_5F5D')
    def lambda_5F5D():
        OP_6D(70160, 1250, 52920, 3400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_5F5D)

    @scena.Lambda('lambda_5F75')
    def lambda_5F75():
        OP_67(0, 11000, -10000, 3400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5F75)

    @scena.Lambda('lambda_5F8D')
    def lambda_5F8D():
        OP_6B(2340, 3400)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_5F8D)

    @scena.Lambda('lambda_5F9D')
    def lambda_5F9D():
        OP_6C(90000, 3400)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_5F9D)

    CreateThread(0x003A, 0x00, 0x01, 0x003B)
    WaitForThreadExit(0x002A, 0x0000)
    CreateThread(0x002A, 0x00, 0x01, 0x003D)
    WaitForThreadExit(0x0101, 0x0000)
    SetChrChipByIndex(0x003A, 15)
    SetChrSubChip(0x003A, 0)
    SetChrPos(0x003A, 69170, 1250, 53160, 250)
    SetChrChipByIndex(0x002A, 1)
    SetChrSubChip(0x002A, 0)

    @scena.Lambda('lambda_5FEA')
    def lambda_5FEA():
        OP_6D(69190, 2150, 55290, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_5FEA)

    @scena.Lambda('lambda_6002')
    def lambda_6002():
        OP_67(0, 7040, -10000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_6002)

    @scena.Lambda('lambda_601A')
    def lambda_601A():
        OP_6C(46000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_601A)

    SetChrFlags(0x0031, 0x0800)
    SetChrChipByIndex(0x0031, 23)
    SetChrSubChip(0x0031, 2)

    @scena.Lambda('lambda_6039')
    def lambda_6039():
        OP_96(0x00FE, 0x00011148, 0x000004E2, 0x0000D58E, 0x000007D0, 0x000005DC)

        ExitThread()

    DispatchAsync(0x0031, 0x0001, lambda_6039)

    Sleep(650)

    @scena.Lambda('lambda_605C')
    def lambda_605C():
        OP_99(0x00FE, 0x02, 0x05, 0x000007D0)

        ExitThread()

    DispatchAsync(0x0031, 0x0002, lambda_605C)

    Sleep(150)

    PlayEffect(0x01, 0x01, 0x00FF, 69960, 1250, 53070, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    OP_7C(0x00000000, 0x00000258, 0x00000BB8, 0x000000C8)

    @scena.Lambda('lambda_60B7')
    def lambda_60B7():
        OP_6D(69320, 2150, 48410, 600)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_60B7)

    @scena.Lambda('lambda_60CF')
    def lambda_60CF():
        OP_6B(2560, 600)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_60CF)

    @scena.Lambda('lambda_60DF')
    def lambda_60DF():
        OP_6C(32000, 600)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_60DF)

    SetChrChipByIndex(0x0039, 16)
    SetChrSubChip(0x0039, 0)
    OP_8C(0x0039, 0, 0)

    @scena.Lambda('lambda_6100')
    def lambda_6100():
        OP_9E(0x00FE, 0x0000003C, 0x00000000, 0x000001F4, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x0039, 0x0002, lambda_6100)

    @scena.Lambda('lambda_611A')
    def lambda_611A():
        OP_96(0x00FE, 0x000116CA, 0x000000FA, 0x0000B284, 0x000001F4, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x0039, 0x0001, lambda_611A)

    SetChrChipByIndex(0x003A, 16)
    SetChrSubChip(0x003A, 0)
    OP_8C(0x003A, 0, 0)

    @scena.Lambda('lambda_6149')
    def lambda_6149():
        OP_9E(0x00FE, 0x0000003C, 0x00000000, 0x000001F4, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x003A, 0x0002, lambda_6149)

    @scena.Lambda('lambda_6163')
    def lambda_6163():
        OP_96(0x00FE, 0x00010E96, 0x000000FA, 0x0000B158, 0x000001F4, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x003A, 0x0001, lambda_6163)

    WaitForThreadExit(0x003A, 0x0001)
    SetChrChipByIndex(0x003A, 17)
    SetChrSubChip(0x003A, 2)
    CreateThread(0x003A, 0x00, 0x01, 0x001E)
    WaitForThreadExit(0x0039, 0x0001)
    SetChrChipByIndex(0x0039, 17)
    SetChrSubChip(0x0039, 3)
    CreateThread(0x0039, 0x00, 0x01, 0x001F)
    WaitForThreadExit(0x0101, 0x0000)

    @scena.Lambda('lambda_61B2')
    def lambda_61B2():
        OP_6D(71130, 250, 45090, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_61B2)

    @scena.Lambda('lambda_61CA')
    def lambda_61CA():
        OP_67(0, 9520, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_61CA)

    @scena.Lambda('lambda_61E2')
    def lambda_61E2():
        OP_6B(1750, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_61E2)

    @scena.Lambda('lambda_61F2')
    def lambda_61F2():
        OP_6C(44000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_61F2)

    @scena.Lambda('lambda_6202')
    def lambda_6202():
        OP_6E(354, 2000)

        ExitThread()

    DispatchAsync(0x0028, 0x0000, lambda_6202)

    @scena.Lambda('lambda_6212')
    def lambda_6212():
        OP_8F(0x00FE, 70350, 250, 44110, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x003B, 0x0001, lambda_6212)

    @scena.Lambda('lambda_622D')
    def lambda_622D():
        OP_8F(0x00FE, 68900, 250, 43390, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x003C, 0x0001, lambda_622D)

    @scena.Lambda('lambda_6248')
    def lambda_6248():
        OP_8F(0x00FE, 71360, 250, 42970, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x003D, 0x0001, lambda_6248)

    WaitForThreadExit(0x003B, 0x0001)
    SetChrChipByIndex(0x003B, 33)
    SetChrSubChip(0x003B, 0)
    WaitForThreadExit(0x003C, 0x0001)
    SetChrChipByIndex(0x003C, 33)
    SetChrSubChip(0x003C, 0)
    WaitForThreadExit(0x003D, 0x0001)
    SetChrChipByIndex(0x003D, 33)
    SetChrSubChip(0x003D, 0)
    WaitForThreadExit(0x0101, 0x0000)

    @scena.Lambda('lambda_6295')
    def lambda_6295():
        OP_6D(70780, 250, 47510, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_6295)

    @scena.Lambda('lambda_62AD')
    def lambda_62AD():
        OP_67(0, 8460, -10000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_62AD)

    @scena.Lambda('lambda_62C5')
    def lambda_62C5():
        OP_6B(2270, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_62C5)

    @scena.Lambda('lambda_62D5')
    def lambda_62D5():
        OP_6C(32000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_62D5)

    SetChrChipByIndex(0x0029, 2)
    SetChrSubChip(0x0029, 0)
    SetChrChipByIndex(0x0031, 6)
    SetChrSubChip(0x0031, 0)
    SetChrChipByIndex(0x002A, 2)
    SetChrSubChip(0x002A, 0)
    SetChrPos(0x0029, 68800, 1250, 55030, 180)
    SetChrPos(0x0031, 70040, 1250, 53370, 180)
    SetChrPos(0x002A, 71540, 1250, 55010, 180)
    ClearChrFlags(0x0029, 0x0020)
    ClearChrFlags(0x0031, 0x0020)
    ClearChrFlags(0x002A, 0x0020)

    @scena.Lambda('lambda_6345')
    def lambda_6345():
        OP_8F(0x00FE, 68800, 1250, 51030, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0029, 0x0001, lambda_6345)

    @scena.Lambda('lambda_6360')
    def lambda_6360():
        OP_8F(0x00FE, 70040, 1250, 50370, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0031, 0x0001, lambda_6360)

    @scena.Lambda('lambda_637B')
    def lambda_637B():
        OP_8F(0x00FE, 71540, 1250, 51010, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x002A, 0x0001, lambda_637B)

    WaitForThreadExit(0x0029, 0x0001)
    SetChrChipByIndex(0x0029, 1)
    SetChrSubChip(0x0029, 0)
    WaitForThreadExit(0x0031, 0x0001)
    SetChrChipByIndex(0x0031, 5)
    SetChrSubChip(0x0031, 0)
    WaitForThreadExit(0x002A, 0x0001)
    SetChrChipByIndex(0x002A, 1)
    SetChrSubChip(0x002A, 0)
    WaitForThreadExit(0x0101, 0x0000)
    Sleep(1000)

    OP_62(0x003D, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_22(0x00D5, 0x00, 0x64)
    Sleep(400)

    @scena.Lambda('lambda_63EE')
    def lambda_63EE():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x003D, 0x0003, lambda_63EE)

    Sleep(400)

    @scena.Lambda('lambda_6401')
    def lambda_6401():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x003C, 0x0003, lambda_6401)

    Sleep(200)

    @scena.Lambda('lambda_6414')
    def lambda_6414():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x003B, 0x0003, lambda_6414)

    Sleep(400)

    Fade(500)
    OP_6D(70570, 250, 40500, 0)
    OP_67(0, 8460, -10000, 0)
    OP_6B(2270, 0)
    OP_6C(144000, 0)
    OP_6E(354, 0)
    SetChrPos(0x0039, 71170, 250, 45200, 0)
    SetChrPos(0x003B, 70190, 250, 44050, 180)
    SetChrPos(0x003D, 71660, 250, 42970, 180)
    ClearChrFlags(0x002B, 0x0080)
    ClearChrFlags(0x002C, 0x0080)
    ClearChrFlags(0x002D, 0x0080)
    ClearChrFlags(0x002B, 0x0020)
    ClearChrFlags(0x002C, 0x0020)
    ClearChrFlags(0x002D, 0x0020)

    @scena.Lambda('lambda_64BA')
    def lambda_64BA():
        OP_8F(0x00FE, 70130, 1250, 39150, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x002B, 0x0001, lambda_64BA)

    @scena.Lambda('lambda_64D5')
    def lambda_64D5():
        OP_8F(0x00FE, 71250, 1250, 38450, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x002C, 0x0001, lambda_64D5)

    @scena.Lambda('lambda_64F0')
    def lambda_64F0():
        OP_8F(0x00FE, 69040, 1250, 38380, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x002D, 0x0001, lambda_64F0)

    WaitForThreadExit(0x002B, 0x0001)
    SetChrChipByIndex(0x002B, 1)
    SetChrSubChip(0x002B, 0)
    WaitForThreadExit(0x002C, 0x0001)
    SetChrChipByIndex(0x002C, 1)
    SetChrSubChip(0x002C, 0)
    WaitForThreadExit(0x002D, 0x0001)
    SetChrChipByIndex(0x002D, 1)
    SetChrSubChip(0x002D, 0)

    @scena.Lambda('lambda_6538')
    def lambda_6538():
        OP_6D(70870, 250, 43890, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_6538)

    @scena.Lambda('lambda_6550')
    def lambda_6550():
        OP_6B(2400, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_6550)

    @scena.Lambda('lambda_6560')
    def lambda_6560():
        OP_6C(135000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_6560)

    SetChrChipByIndex(0x003C, 35)
    SetChrSubChip(0x003C, 0)

    @scena.Lambda('lambda_657A')
    def lambda_657A():
        OP_8F(0x00FE, 68900, 250, 43690, 500, 0x00)

        ExitThread()

    DispatchAsync(0x003C, 0x0001, lambda_657A)

    WaitForThreadExit(0x003C, 0x0001)
    TerminateThread(0x003C, 0x02)
    SetChrChipByIndex(0x003C, 33)
    SetChrSubChip(0x003C, 0)
    SetChrChipByIndex(0x003D, 35)
    SetChrSubChip(0x003D, 0)

    @scena.Lambda('lambda_65B2')
    def lambda_65B2():
        OP_8F(0x00FE, 71660, 250, 43670, 500, 0x00)

        ExitThread()

    DispatchAsync(0x003D, 0x0001, lambda_65B2)

    WaitForThreadExit(0x003D, 0x0001)
    TerminateThread(0x003D, 0x02)
    SetChrChipByIndex(0x003D, 33)
    SetChrSubChip(0x003D, 0)
    Sleep(1000)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearMapFlags(0x00000010)
    CreateThread(0x0029, 0x00, 0x01, 0x0022)
    CreateThread(0x002A, 0x00, 0x01, 0x0021)
    CreateThread(0x0031, 0x00, 0x01, 0x0020)
    CreateThread(0x002B, 0x00, 0x01, 0x0023)
    CreateThread(0x002C, 0x00, 0x01, 0x0024)
    CreateThread(0x002D, 0x00, 0x01, 0x0025)
    CreateThread(0x0039, 0x00, 0x01, 0x0026)
    CreateThread(0x003A, 0x00, 0x01, 0x0027)
    CreateThread(0x003B, 0x00, 0x01, 0x0028)
    CreateThread(0x003C, 0x00, 0x01, 0x0029)
    CreateThread(0x003D, 0x00, 0x01, 0x002A)
    Sleep(200)

    FadeOut(1000, 0, -1)
    OP_0D()

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetMapFlags(0x00000010)
    Sleep(200)

    OP_22(0x00D6, 0x00, 0x64)
    Sleep(100)

    OP_22(0x00D6, 0x00, 0x64)
    Sleep(200)

    OP_22(0x01F7, 0x00, 0x64)
    Sleep(200)

    OP_22(0x00D6, 0x00, 0x64)
    Sleep(100)

    OP_22(0x0084, 0x00, 0x64)
    Sleep(100)

    OP_22(0x00A4, 0x00, 0x64)
    Sleep(200)

    OP_22(0x01F7, 0x00, 0x64)
    Sleep(100)

    OP_22(0x01F7, 0x00, 0x64)
    Sleep(100)

    OP_22(0x00D6, 0x00, 0x64)
    Sleep(200)

    OP_22(0x00D6, 0x00, 0x64)
    Sleep(100)

    OP_22(0x00A4, 0x00, 0x64)
    Sleep(100)

    OP_22(0x01F7, 0x00, 0x5A)
    Sleep(200)

    OP_22(0x00D6, 0x00, 0x5A)
    Sleep(100)

    OP_22(0x00D6, 0x00, 0x5A)
    Sleep(100)

    OP_22(0x0084, 0x00, 0x5A)
    Sleep(200)

    OP_22(0x00D6, 0x00, 0x5A)
    Sleep(200)

    OP_22(0x01F7, 0x00, 0x5A)
    Sleep(100)

    OP_22(0x01F7, 0x00, 0x5A)
    Sleep(100)

    OP_22(0x00A4, 0x00, 0x5A)
    Sleep(200)

    OP_22(0x0084, 0x00, 0x50)
    Sleep(100)

    OP_22(0x00D6, 0x00, 0x50)
    Sleep(100)

    OP_22(0x00D6, 0x00, 0x50)
    Sleep(100)

    OP_22(0x00A4, 0x00, 0x50)
    Sleep(100)

    OP_22(0x01F7, 0x00, 0x50)
    Sleep(100)

    OP_22(0x01F7, 0x00, 0x50)
    Sleep(100)

    OP_22(0x00D6, 0x00, 0x50)
    Sleep(100)

    OP_22(0x00D6, 0x00, 0x50)
    Sleep(200)

    OP_22(0x00D6, 0x00, 0x46)
    Sleep(100)

    OP_22(0x00D6, 0x00, 0x46)
    Sleep(2000)

    OP_6D(42310, 1250, 51050, 0)
    OP_67(0, 5870, -10000, 0)
    OP_6B(2400, 0)
    OP_6C(304000, 0)
    OP_6E(332, 0)
    SetChrChipByIndex(0x0047, 9)
    SetChrChipByIndex(0x0048, 10)
    SetChrPos(0x0047, 43000, 1250, 50000, 90)
    SetChrPos(0x0048, 43000, 1250, 51100, 90)
    ClearChrFlags(0x0047, 0x0080)
    ClearChrFlags(0x0048, 0x0080)
    FadeIn(1000, 0)
    OP_0D()
    OP_DC()

    ChrTalk(
        0x0047,
        (
            '#0270380467V#143F#5P喂喂，是真的吗？！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270380468V怎么特务兵\n',
            '会突然出现！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270380469V而且他们似乎在\n',
            '向『结社』发动攻击……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0048,
        (
            '#0280380470V#151F#5P呵呵，他们一定是\n',
            '反省之后来帮忙了吧～⊙',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280380471V这就叫作\n',
            '洗心回面吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0047, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0047,
        (
            '#0270380472V#145F#5P都回面了岂不是没意义了……\n',
            '应该是洗心革面吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270380473V#144F哎呀，无所谓了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270380474V终于轮到照相机\n',
            '大显身手的时候了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270380475V在预定时间到来之前\n',
            '尽情拍个够吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0048,
        (
            '#0280380476V#150F#5P是，前辈！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x0048, 11)
    OP_0D()
    Sleep(300)

    OP_22(0x007C, 0x00, 0x64)
    PlayEffect(0x03, 0xFF, 0x0048, 0, 1500, 500, 0, 0, 0, 500, 500, 500, 0x00FF, 0, 0, 0, 0)
    Sleep(300)

    OP_22(0x007C, 0x00, 0x64)
    PlayEffect(0x03, 0xFF, 0x0048, 0, 1500, 500, 0, 0, 0, 500, 500, 500, 0x00FF, 0, 0, 0, 0)
    Sleep(300)

    OP_22(0x007C, 0x00, 0x64)
    PlayEffect(0x03, 0xFF, 0x0048, 0, 1500, 500, 0, 0, 0, 500, 500, 500, 0x00FF, 0, 0, 0, 0)
    Sleep(300)

    SetMapFlags(0x02000000)
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F2)
    NewScene('ED6_DT21/T4201._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x001E offset: 0x6AD9
@scena.Code('func_1E_6AD9')
def func_1E_6AD9():
    @scena.Lambda('lambda_6ADF')
    def lambda_6ADF():
        OP_9E(0x00FE, 0x00000014, 0x00000000, 0x00000000, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x003A, 0x0002, lambda_6ADF)

    Sleep(1200)

    TerminateThread(0x003A, 0x02)

    @scena.Lambda('lambda_6B02')
    def lambda_6B02():
        OP_99(0x00FE, 0x02, 0x00, 0x000003E8)

        ExitThread()

    DispatchAsync(0x003A, 0x0002, lambda_6B02)

    WaitForThreadExit(0x003A, 0x0002)

    Return()

# id: 0x001F offset: 0x6B12
@scena.Code('func_1F_6B12')
def func_1F_6B12():
    @scena.Lambda('lambda_6B18')
    def lambda_6B18():
        OP_9E(0x00FE, 0x00000014, 0x00000000, 0x00000000, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x0039, 0x0002, lambda_6B18)

    Sleep(2000)

    TerminateThread(0x0039, 0x02)

    @scena.Lambda('lambda_6B3B')
    def lambda_6B3B():
        OP_99(0x00FE, 0x03, 0x00, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0039, 0x0002, lambda_6B3B)

    WaitForThreadExit(0x0039, 0x0002)

    Return()

# id: 0x0020 offset: 0x6B4B
@scena.Code('func_20_6B4B')
def func_20_6B4B():
    SetChrChipByIndex(0x0031, 23)
    SetChrSubChip(0x0031, 2)

    @scena.Lambda('lambda_6B5B')
    def lambda_6B5B():
        OP_96(0x00FE, 0x00011198, 0x000000FA, 0x0000B4D2, 0x000003E8, 0x000009C4)

        ExitThread()

    DispatchAsync(0x0031, 0x0001, lambda_6B5B)

    Sleep(400)

    @scena.Lambda('lambda_6B7E')
    def lambda_6B7E():
        OP_99(0x00FE, 0x02, 0x05, 0x000007D0)

        ExitThread()

    DispatchAsync(0x0031, 0x0002, lambda_6B7E)

    WaitForThreadExit(0x0031, 0x0001)
    OP_22(0x0084, 0x00, 0x64)
    Sleep(400)

    @scena.Lambda('lambda_6B9D')
    def lambda_6B9D():
        OP_99(0x00FE, 0x05, 0x07, 0x000007D0)

        ExitThread()

    DispatchAsync(0x0031, 0x0002, lambda_6B9D)

    @scena.Lambda('lambda_6BAD')
    def lambda_6BAD():
        OP_96(0x00FE, 0x00011198, 0x000000FA, 0x0000BEB4, 0x000001F4, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x0031, 0x0001, lambda_6BAD)

    WaitForThreadExit(0x0031, 0x0001)
    OP_22(0x00A4, 0x00, 0x64)

    @scena.Lambda('lambda_6BD5')
    def lambda_6BD5():
        OP_96(0x00FE, 0x00011198, 0x000000FA, 0x0000AD02, 0x000003E8, 0x000007D0)

        ExitThread()

    DispatchAsync(0x0031, 0x0001, lambda_6BD5)

    Sleep(300)

    @scena.Lambda('lambda_6BF8')
    def lambda_6BF8():
        OP_99(0x00FE, 0x02, 0x05, 0x000007D0)

        ExitThread()

    DispatchAsync(0x0031, 0x0002, lambda_6BF8)

    WaitForThreadExit(0x0031, 0x0001)

    Return()

# id: 0x0021 offset: 0x6C08
@scena.Code('func_21_6C08')
def func_21_6C08():
    Sleep(200)

    SetChrFlags(0x002A, 0x0020)
    SetChrChipByIndex(0x002A, 2)
    SetChrSubChip(0x002A, 2)

    @scena.Lambda('lambda_6C22')
    def lambda_6C22():
        OP_96(0x00FE, 0x000117B0, 0x000000FA, 0x0000B98C, 0x000001F4, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x002A, 0x0001, lambda_6C22)

    WaitForThreadExit(0x002A, 0x0001)
    OP_22(0x00A4, 0x00, 0x64)

    @scena.Lambda('lambda_6C4A')
    def lambda_6C4A():
        OP_96(0x00FE, 0x00011E04, 0x000000FA, 0x0000B216, 0x000001F4, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x002A, 0x0001, lambda_6C4A)

    WaitForThreadExit(0x002A, 0x0001)
    OP_22(0x00A4, 0x00, 0x64)

    @scena.Lambda('lambda_6C72')
    def lambda_6C72():
        OP_96(0x00FE, 0x00011E86, 0x000000FA, 0x0000BA40, 0x000001F4, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x002A, 0x0001, lambda_6C72)

    WaitForThreadExit(0x002A, 0x0001)
    OP_22(0x00A4, 0x00, 0x64)
    SetChrChipByIndex(0x002A, 3)
    SetChrSubChip(0x002A, 5)
    OP_8C(0x002A, 220, 0)

    @scena.Lambda('lambda_6CAB')
    def lambda_6CAB():
        OP_8F(0x00FE, 71780, 250, 45850, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x002A, 0x0001, lambda_6CAB)

    WaitForThreadExit(0x002A, 0x0001)

    Return()

# id: 0x0022 offset: 0x6CC6
@scena.Code('func_22_6CC6')
def func_22_6CC6():
    Sleep(600)

    SetChrFlags(0x0029, 0x0020)
    SetChrChipByIndex(0x0029, 2)
    SetChrSubChip(0x0029, 2)

    @scena.Lambda('lambda_6CE0')
    def lambda_6CE0():
        OP_96(0x00FE, 0x00010DEC, 0x000000FA, 0x0000BA2C, 0x000000C8, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x0029, 0x0001, lambda_6CE0)

    WaitForThreadExit(0x0029, 0x0001)
    OP_22(0x00A4, 0x00, 0x64)

    @scena.Lambda('lambda_6D08')
    def lambda_6D08():
        OP_96(0x00FE, 0x00010E64, 0x000000FA, 0x0000BF68, 0x000000C8, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x0029, 0x0001, lambda_6D08)

    WaitForThreadExit(0x0029, 0x0001)
    OP_22(0x00A4, 0x00, 0x64)
    SetChrChipByIndex(0x0029, 3)
    SetChrSubChip(0x0029, 5)

    @scena.Lambda('lambda_6D3A')
    def lambda_6D3A():
        OP_8F(0x00FE, 69160, 250, 46090, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0029, 0x0001, lambda_6D3A)

    WaitForThreadExit(0x0029, 0x0001)

    Return()

# id: 0x0023 offset: 0x6D55
@scena.Code('func_23_6D55')
def func_23_6D55():
    Sleep(400)

    SetChrFlags(0x002B, 0x0020)
    SetChrChipByIndex(0x002B, 2)
    SetChrSubChip(0x002B, 2)

    @scena.Lambda('lambda_6D6F')
    def lambda_6D6F():
        OP_96(0x00FE, 0x00010CD4, 0x000000FA, 0x0000A0E6, 0x000000C8, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x002B, 0x0001, lambda_6D6F)

    WaitForThreadExit(0x002B, 0x0001)
    OP_22(0x00A4, 0x00, 0x64)

    @scena.Lambda('lambda_6D97')
    def lambda_6D97():
        OP_96(0x00FE, 0x00011774, 0x000000FA, 0x0000A3DE, 0x000000C8, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x002B, 0x0001, lambda_6D97)

    WaitForThreadExit(0x002B, 0x0001)
    OP_22(0x00A4, 0x00, 0x64)

    @scena.Lambda('lambda_6DBF')
    def lambda_6DBF():
        OP_96(0x00FE, 0x000111D4, 0x000002EE, 0x00009D58, 0x00000258, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x002B, 0x0001, lambda_6DBF)

    WaitForThreadExit(0x002B, 0x0001)
    OP_22(0x00A4, 0x00, 0x64)
    SetChrChipByIndex(0x002B, 3)
    SetChrSubChip(0x002B, 5)

    @scena.Lambda('lambda_6DF1')
    def lambda_6DF1():
        OP_8F(0x00FE, 70110, 250, 43170, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x002B, 0x0001, lambda_6DF1)

    WaitForThreadExit(0x002B, 0x0001)

    Return()

# id: 0x0024 offset: 0x6E0C
@scena.Code('func_24_6E0C')
def func_24_6E0C():
    Sleep(100)

    SetChrFlags(0x002C, 0x0020)
    SetChrChipByIndex(0x002C, 2)
    SetChrSubChip(0x002C, 2)

    @scena.Lambda('lambda_6E26')
    def lambda_6E26():
        OP_96(0x00FE, 0x00011774, 0x000000FA, 0x0000A258, 0x000000C8, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x002C, 0x0001, lambda_6E26)

    WaitForThreadExit(0x002C, 0x0001)
    OP_22(0x00A4, 0x00, 0x64)
    OP_8C(0x002C, 315, 0)

    @scena.Lambda('lambda_6E55')
    def lambda_6E55():
        OP_96(0x00FE, 0x00011D00, 0x000000FA, 0x0000A60E, 0x000000C8, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x002C, 0x0001, lambda_6E55)

    WaitForThreadExit(0x002C, 0x0001)
    OP_22(0x00A4, 0x00, 0x64)
    OP_8C(0x002C, 225, 0)

    @scena.Lambda('lambda_6E84')
    def lambda_6E84():
        OP_96(0x00FE, 0x00011D8C, 0x000000FA, 0x0000AED8, 0x000000C8, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x002C, 0x0001, lambda_6E84)

    WaitForThreadExit(0x002C, 0x0001)
    OP_22(0x00A4, 0x00, 0x64)
    SetChrChipByIndex(0x002C, 3)
    SetChrSubChip(0x002C, 5)

    @scena.Lambda('lambda_6EB6')
    def lambda_6EB6():
        OP_8F(0x00FE, 72260, 250, 43950, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x002C, 0x0001, lambda_6EB6)

    WaitForThreadExit(0x002C, 0x0001)

    Return()

# id: 0x0025 offset: 0x6ED1
@scena.Code('func_25_6ED1')
def func_25_6ED1():
    Sleep(600)

    SetChrFlags(0x002D, 0x0020)
    SetChrChipByIndex(0x002D, 2)
    SetChrSubChip(0x002D, 2)

    @scena.Lambda('lambda_6EEB')
    def lambda_6EEB():
        OP_96(0x00FE, 0x00011594, 0x000004E2, 0x00009B78, 0x000000C8, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x002D, 0x0001, lambda_6EEB)

    WaitForThreadExit(0x002D, 0x0001)
    OP_22(0x00A4, 0x00, 0x64)

    @scena.Lambda('lambda_6F13')
    def lambda_6F13():
        OP_96(0x00FE, 0x00010D6A, 0x000001F4, 0x00009E2A, 0x000000C8, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x002D, 0x0001, lambda_6F13)

    WaitForThreadExit(0x002D, 0x0001)
    OP_22(0x00A4, 0x00, 0x64)
    OP_8C(0x002D, 45, 0)

    @scena.Lambda('lambda_6F42')
    def lambda_6F42():
        OP_96(0x00FE, 0x00010734, 0x000000FA, 0x0000A58C, 0x000000C8, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x002D, 0x0001, lambda_6F42)

    WaitForThreadExit(0x002D, 0x0001)
    OP_22(0x00A4, 0x00, 0x64)
    SetChrChipByIndex(0x002D, 3)
    SetChrSubChip(0x002D, 5)

    @scena.Lambda('lambda_6F74')
    def lambda_6F74():
        OP_8F(0x00FE, 68290, 250, 43280, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x002D, 0x0001, lambda_6F74)

    WaitForThreadExit(0x002D, 0x0001)

    Return()

# id: 0x0026 offset: 0x6F8F
@scena.Code('func_26_6F8F')
def func_26_6F8F():
    Sleep(300)

    SetChrFlags(0x0039, 0x0020)
    SetChrChipByIndex(0x0039, 29)
    SetChrSubChip(0x0039, 2)
    OP_8C(0x0039, 270, 0)

    @scena.Lambda('lambda_6FB0')
    def lambda_6FB0():
        OP_96(0x00FE, 0x00011CF6, 0x000000FA, 0x0000AF8C, 0x000001F4, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x0039, 0x0001, lambda_6FB0)

    WaitForThreadExit(0x0039, 0x0001)
    OP_22(0x00A4, 0x00, 0x64)
    SetChrChipByIndex(0x0039, 30)
    SetChrSubChip(0x0039, 0)

    @scena.Lambda('lambda_6FE2')
    def lambda_6FE2():
        OP_99(0x00FE, 0x00, 0x07, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x0039, 0x0002, lambda_6FE2)

    @scena.Lambda('lambda_6FF2')
    def lambda_6FF2():
        OP_8F(0x00FE, 71140, 250, 45360, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0039, 0x0001, lambda_6FF2)

    WaitForThreadExit(0x0039, 0x0001)

    Return()

# id: 0x0027 offset: 0x700D
@scena.Code('func_27_700D')
def func_27_700D():
    Sleep(300)

    SetChrFlags(0x003A, 0x0020)
    SetChrChipByIndex(0x003A, 29)
    SetChrSubChip(0x003A, 2)
    OP_8C(0x003A, 90, 0)

    @scena.Lambda('lambda_702E')
    def lambda_702E():
        OP_96(0x00FE, 0x0001091E, 0x000000FA, 0x0000B18A, 0x000001F4, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x003A, 0x0001, lambda_702E)

    WaitForThreadExit(0x003A, 0x0001)
    OP_22(0x00A4, 0x00, 0x64)

    @scena.Lambda('lambda_7056')
    def lambda_7056():
        OP_96(0x00FE, 0x000107C0, 0x000000FA, 0x0000AADC, 0x000001F4, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x003A, 0x0001, lambda_7056)

    WaitForThreadExit(0x003A, 0x0001)
    OP_22(0x00A4, 0x00, 0x64)
    SetChrChipByIndex(0x003A, 30)
    SetChrSubChip(0x003A, 0)

    @scena.Lambda('lambda_7088')
    def lambda_7088():
        OP_99(0x00FE, 0x00, 0x07, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x003A, 0x0002, lambda_7088)

    @scena.Lambda('lambda_7098')
    def lambda_7098():
        OP_8F(0x00FE, 69150, 250, 45610, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x003A, 0x0001, lambda_7098)

    WaitForThreadExit(0x003A, 0x0001)

    Return()

# id: 0x0028 offset: 0x70B3
@scena.Code('func_28_70B3')
def func_28_70B3():
    Sleep(200)

    SetChrFlags(0x00FE, 0x0020)
    SetChrChipByIndex(0x00FE, 36)
    SetChrSubChip(0x00FE, 0)

    @scena.Lambda('lambda_70CD')
    def lambda_70CD():
        OP_99(0x00FE, 0x00, 0x07, 0x000007D0)
        Yield()

        Jump('lambda_70CD')

    DispatchAsync2(0x00FE, 0x0002, lambda_70CD)

    OP_22(0x01F7, 0x00, 0x64)
    PlayEffect(0x02, 0xFF, 0x00FE, 0, 750, 1000, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x07, 0xFF, 0x00FE, 0, 500, -4000, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(500)

    OP_22(0x01F7, 0x00, 0x64)
    PlayEffect(0x02, 0xFF, 0x00FE, 0, 750, 1000, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x07, 0xFF, 0x00FE, 0, 500, -4000, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(500)

    OP_22(0x01F7, 0x00, 0x64)
    Sleep(1000)

    TerminateThread(0x00FE, 0x02)

    Return()

# id: 0x0029 offset: 0x71D1
@scena.Code('func_29_71D1')
def func_29_71D1():
    Sleep(400)

    SetChrFlags(0x00FE, 0x0020)
    SetChrChipByIndex(0x00FE, 36)
    SetChrSubChip(0x00FE, 0)

    @scena.Lambda('lambda_71EB')
    def lambda_71EB():
        OP_99(0x00FE, 0x00, 0x07, 0x000007D0)
        Yield()

        Jump('lambda_71EB')

    DispatchAsync2(0x00FE, 0x0002, lambda_71EB)

    OP_22(0x01F7, 0x00, 0x64)
    PlayEffect(0x02, 0xFF, 0x00FE, 0, 750, 1000, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x07, 0xFF, 0x00FE, 0, 500, -4000, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(500)

    OP_22(0x01F7, 0x00, 0x64)
    PlayEffect(0x02, 0xFF, 0x00FE, 0, 750, 1000, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x07, 0xFF, 0x00FE, 0, 500, -4000, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(500)

    OP_22(0x01F7, 0x00, 0x64)
    Sleep(1000)

    TerminateThread(0x00FE, 0x02)

    Return()

# id: 0x002A offset: 0x72EF
@scena.Code('func_2A_72EF')
def func_2A_72EF():
    Sleep(600)

    SetChrFlags(0x00FE, 0x0020)
    SetChrChipByIndex(0x00FE, 36)
    SetChrSubChip(0x00FE, 0)

    @scena.Lambda('lambda_7309')
    def lambda_7309():
        OP_99(0x00FE, 0x00, 0x07, 0x000007D0)
        Yield()

        Jump('lambda_7309')

    DispatchAsync2(0x00FE, 0x0002, lambda_7309)

    OP_22(0x01F7, 0x00, 0x64)
    PlayEffect(0x02, 0xFF, 0x00FE, 0, 750, 1000, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x07, 0xFF, 0x00FE, 0, 500, -4000, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(500)

    OP_22(0x01F7, 0x00, 0x64)
    PlayEffect(0x02, 0xFF, 0x00FE, 0, 750, 1000, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x07, 0xFF, 0x00FE, 0, 500, -4000, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(500)

    OP_22(0x01F7, 0x00, 0x64)
    Sleep(1000)

    TerminateThread(0x00FE, 0x02)

    Return()

# id: 0x002B offset: 0x740D
@scena.Code('func_2B_740D')
def func_2B_740D():
    OP_8E(0x00FE, 46940, 0, 1330, 5000, 0x00)
    OP_8E(0x00FE, 51860, 0, 1330, 5000, 0x00)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x002C offset: 0x743B
@scena.Code('func_2C_743B')
def func_2C_743B():
    OP_8E(0x00FE, 46940, 0, 130, 5000, 0x00)
    OP_8E(0x00FE, 51810, 0, 130, 5000, 0x00)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x002D offset: 0x7469
@scena.Code('func_2D_7469')
def func_2D_7469():
    OP_8E(0x00FE, 46860, 0, -2170, 5000, 0x00)
    OP_8E(0x00FE, 48140, 0, -1690, 5000, 0x00)
    OP_8E(0x00FE, 54500, 0, -1690, 5000, 0x00)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x002E offset: 0x74AB
@scena.Code('func_2E_74AB')
def func_2E_74AB():
    OP_8E(0x00FE, 46860, 0, -3310, 5000, 0x00)
    OP_8E(0x00FE, 48140, 0, -2850, 5000, 0x00)
    OP_8E(0x00FE, 54500, 0, -2850, 5000, 0x00)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x002F offset: 0x74ED
@scena.Code('func_2F_74ED')
def func_2F_74ED():
    OP_8E(0x00FE, 48940, 0, 1630, 5000, 0x00)
    OP_8E(0x00FE, 51130, 0, 3210, 5000, 0x00)
    OP_8E(0x00FE, 52340, 0, 5570, 5000, 0x00)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x0030 offset: 0x752F
@scena.Code('func_30_752F')
def func_30_752F():
    OP_8E(0x00FE, 48070, 0, 200, 5000, 0x00)
    OP_8E(0x00FE, 51990, 0, 860, 5000, 0x00)
    OP_8E(0x00FE, 58440, 0, 860, 5000, 0x00)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x0031 offset: 0x7571
@scena.Code('func_31_7571')
def func_31_7571():
    OP_8E(0x00FE, 47970, 0, -2150, 5000, 0x00)
    OP_8E(0x00FE, 51860, 0, -2820, 5000, 0x00)
    OP_8E(0x00FE, 58360, 0, -2820, 5000, 0x00)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x0032 offset: 0x75B3
@scena.Code('func_32_75B3')
def func_32_75B3():
    SetChrFlags(0x00FE, 0x0004)
    OP_8E(0x00FE, 46710, 0, -3740, 5000, 0x00)
    OP_8E(0x00FE, 53000, 250, -5890, 5000, 0x00)
    OP_8E(0x00FE, 57080, 250, -6700, 5000, 0x00)
    SetChrFlags(0x00FE, 0x0080)
    ClearChrFlags(0x00FE, 0x0004)

    Return()

# id: 0x0033 offset: 0x75FF
@scena.Code('func_33_75FF')
def func_33_75FF():
    If(
        (
            (Expr.GetChrWork, 0xFE, 0x1),
            (Expr.PushLong, 0x178F4),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_7615',
    )

    Sleep(15)

    Jump('func_33_75FF')

    def _loc_7615(): pass

    label('loc_7615')

    ExecExpressionWithValue(
        0x00FE,
        0x02,
        (
            (Expr.PushLong, 0x2EE),
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_7626')
    def lambda_7626():
        OP_8F(0x00FE, 90900, 750, 33430, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_7626)

    Return()

# id: 0x0034 offset: 0x763C
@scena.Code('func_34_763C')
def func_34_763C():
    SetChrChipByIndex(0x0031, 6)
    SetChrSubChip(0x0031, 6)
    OP_7D(0x00, 0x0031, 0x0032, 0x0064)

    @scena.Lambda('lambda_7654')
    def lambda_7654():
        OP_8C(0x00FE, 280, 400)

        ExitThread()

    DispatchAsync(0x0031, 0x0003, lambda_7654)

    @scena.Lambda('lambda_7662')
    def lambda_7662():
        OP_96(0x00FE, 0x00018D76, 0x000000FA, 0x00008160, 0x000001F4, 0x000007D0)

        ExitThread()

    DispatchAsync(0x0031, 0x0001, lambda_7662)

    WaitForThreadExit(0x0031, 0x0001)
    OP_22(0x00A4, 0x00, 0x64)
    OP_7D(0x01, 0x0031, 0x0000, 0x0000)
    SetChrChipByIndex(0x0031, 7)
    SetChrSubChip(0x0031, 1)

    @scena.Lambda('lambda_769C')
    def lambda_769C():
        OP_96(0x00FE, 0x000184A2, 0x000000FA, 0x00008B92, 0x000001F4, 0x000007D0)

        ExitThread()

    DispatchAsync(0x0031, 0x0001, lambda_769C)

    Sleep(200)

    @scena.Lambda('lambda_76BF')
    def lambda_76BF():
        OP_99(0x00FE, 0x01, 0x05, 0x000007D0)

        ExitThread()

    DispatchAsync(0x0031, 0x0002, lambda_76BF)

    Sleep(100)

    OP_22(0x00D6, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x0043, 500, 500, -1200, 0, 0, 0, 2000, 2000, 2000, 0x00FF, 0, 0, 0, 0)
    OP_7C(0x00000000, 0x00000190, 0x00000BB8, 0x000000C8)
    SetChrChipByIndex(0x0043, 22)
    SetChrSubChip(0x0043, 0)

    @scena.Lambda('lambda_7729')
    def lambda_7729():
        OP_8F(0x00FE, 96270, 750, 37960, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x0043, 0x0001, lambda_7729)

    @scena.Lambda('lambda_7744')
    def lambda_7744():
        OP_9E(0x00FE, 0x0000003C, 0x00000000, 0x000002BC, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x0043, 0x0002, lambda_7744)

    WaitForThreadExit(0x0043, 0x0001)

    @scena.Lambda('lambda_7763')
    def lambda_7763():
        OP_9E(0x00FE, 0x00000014, 0x00000000, 0x00000000, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x0043, 0x0002, lambda_7763)

    Sleep(1000)

    PlayEffect(0x01, 0x01, 0x0043, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_83(0x01, 0x02)
    TerminateThread(0x0043, 0x02)
    SetChrFlags(0x0043, 0x0080)
    OP_83(0x01, 0x00)

    Return()

# id: 0x0035 offset: 0x77C1
@scena.Code('func_35_77C1')
def func_35_77C1():
    @scena.Lambda('lambda_77C7')
    def lambda_77C7():
        OP_96(0x00FE, 0x00016D8C, 0x00000000, 0x0000CA4E, 0x000003E8, 0x000009C4)

        ExitThread()

    DispatchAsync(0x0031, 0x0001, lambda_77C7)

    Sleep(400)

    @scena.Lambda('lambda_77EA')
    def lambda_77EA():
        OP_99(0x00FE, 0x02, 0x05, 0x000007D0)

        ExitThread()

    DispatchAsync(0x0031, 0x0002, lambda_77EA)

    Sleep(200)

    TerminateThread(0x0046, 0x01)
    TerminateThread(0x0028, 0x03)
    OP_23(0x013F)
    OP_22(0x00D6, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x0031, 1000, 500, 0, 0, 0, 0, 2000, 2000, 2000, 0x00FF, 0, 0, 0, 0)
    OP_7C(0x00000000, 0x00000190, 0x00000BB8, 0x000000C8)
    SetChrFlags(0x0046, 0x0020)
    SetChrChipByIndex(0x0046, 25)
    SetChrSubChip(0x0046, 0)

    @scena.Lambda('lambda_7864')
    def lambda_7864():
        OP_8F(0x00FE, 94780, 550, 54230, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x0046, 0x0001, lambda_7864)

    @scena.Lambda('lambda_787F')
    def lambda_787F():
        OP_9E(0x00FE, 0x0000003C, 0x00000000, 0x000002BC, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x0046, 0x0002, lambda_787F)

    WaitForThreadExit(0x0046, 0x0001)

    Return()

# id: 0x0036 offset: 0x7899
@scena.Code('func_36_7899')
def func_36_7899():
    @scena.Lambda('lambda_789F')
    def lambda_789F():
        OP_96(0x00FE, 0x00017EBC, 0x00000000, 0x0000CA4E, 0x000005DC, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x0032, 0x0001, lambda_789F)

    Sleep(550)

    @scena.Lambda('lambda_78C2')
    def lambda_78C2():
        OP_99(0x00FE, 0x02, 0x05, 0x000007D0)

        ExitThread()

    DispatchAsync(0x0032, 0x0002, lambda_78C2)

    Sleep(200)

    TerminateThread(0x0045, 0x01)
    OP_22(0x00D6, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x0032, -1000, 500, 0, 0, 0, 0, 2000, 2000, 2000, 0x00FF, 0, 0, 0, 0)
    OP_7C(0x00000000, 0x00000190, 0x00000BB8, 0x000000C8)
    SetChrFlags(0x0045, 0x0020)
    SetChrChipByIndex(0x0045, 25)
    SetChrSubChip(0x0045, 0)

    @scena.Lambda('lambda_7935')
    def lambda_7935():
        OP_8F(0x00FE, 96780, 550, 53230, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x0045, 0x0001, lambda_7935)

    @scena.Lambda('lambda_7950')
    def lambda_7950():
        OP_9E(0x00FE, 0x0000003C, 0x00000000, 0x000002BC, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x0045, 0x0002, lambda_7950)

    WaitForThreadExit(0x0045, 0x0001)

    Return()

# id: 0x0037 offset: 0x796A
@scena.Code('func_37_796A')
def func_37_796A():
    SetChrChipByIndex(0x0046, 25)
    SetChrSubChip(0x0046, 0)

    @scena.Lambda('lambda_797A')
    def lambda_797A():
        OP_9E(0x00FE, 0x0000003C, 0x00000000, 0x000003E8, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x0046, 0x0002, lambda_797A)

    WaitForThreadExit(0x0046, 0x0002)

    @scena.Lambda('lambda_7999')
    def lambda_7999():
        OP_9E(0x00FE, 0x00000014, 0x00000000, 0x00000000, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x0046, 0x0002, lambda_7999)

    Sleep(1000)

    PlayEffect(0x01, 0x05, 0x0046, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_83(0x05, 0x02)
    TerminateThread(0x0046, 0x02)
    SetChrFlags(0x0046, 0x0080)
    OP_83(0x05, 0x00)

    Return()

# id: 0x0038 offset: 0x79F7
@scena.Code('func_38_79F7')
def func_38_79F7():
    SetChrChipByIndex(0x0045, 25)
    SetChrSubChip(0x0045, 0)

    @scena.Lambda('lambda_7A07')
    def lambda_7A07():
        OP_9E(0x00FE, 0x0000003C, 0x00000000, 0x000003E8, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x0045, 0x0002, lambda_7A07)

    WaitForThreadExit(0x0045, 0x0002)

    @scena.Lambda('lambda_7A26')
    def lambda_7A26():
        OP_9E(0x00FE, 0x00000014, 0x00000000, 0x00000000, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x0045, 0x0002, lambda_7A26)

    Sleep(1200)

    PlayEffect(0x01, 0x06, 0x0045, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_83(0x06, 0x02)
    TerminateThread(0x0045, 0x02)
    SetChrFlags(0x0045, 0x0080)
    OP_83(0x06, 0x00)

    Return()

# id: 0x0039 offset: 0x7A84
@scena.Code('func_39_7A84')
def func_39_7A84():
    OP_7D(0x00, 0x0029, 0x0014, 0x0064)

    @scena.Lambda('lambda_7A92')
    def lambda_7A92():
        OP_96(0x00FE, 0x0000FDFB, 0x000004E2, 0x0000C6AC, 0x000001F4, 0x000007D0)

        ExitThread()

    DispatchAsync(0x0029, 0x0001, lambda_7A92)

    WaitForThreadExit(0x0029, 0x0001)
    OP_22(0x00A4, 0x00, 0x64)

    @scena.Lambda('lambda_7ABA')
    def lambda_7ABA():
        OP_8C(0x00FE, 250, 300)

        ExitThread()

    DispatchAsync(0x003A, 0x0003, lambda_7ABA)

    OP_8C(0x0029, 20, 0)
    SetChrChipByIndex(0x0029, 3)
    SetChrSubChip(0x0029, 0)

    @scena.Lambda('lambda_7AD9')
    def lambda_7AD9():
        OP_96(0x00FE, 0x00010B94, 0x000004E2, 0x0000CD32, 0x000001F4, 0x000007D0)

        ExitThread()

    DispatchAsync(0x0029, 0x0001, lambda_7AD9)

    Sleep(200)

    @scena.Lambda('lambda_7AFC')
    def lambda_7AFC():
        OP_99(0x00FE, 0x00, 0x02, 0x000005DC)

        ExitThread()

    DispatchAsync(0x0029, 0x0002, lambda_7AFC)

    WaitForThreadExit(0x0029, 0x0001)
    OP_22(0x00D6, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x003A, -500, 500, -500, 0, 0, 0, 2000, 2000, 2000, 0x00FF, 0, 0, 0, 0)
    OP_7C(0x00000000, 0x00000190, 0x00000BB8, 0x000000C8)
    OP_7D(0x01, 0x0029, 0x0000, 0x0000)
    SetChrChipByIndex(0x003A, 17)
    SetChrSubChip(0x003A, 1)
    TerminateThread(0x003A, 0x03)
    OP_8C(0x003A, 200, 0)
    SetChrFlags(0x003A, 0x0020)

    @scena.Lambda('lambda_7B7E')
    def lambda_7B7E():
        OP_9E(0x00FE, 0x00000028, 0x00000000, 0x000001F4, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x003A, 0x0002, lambda_7B7E)

    @scena.Lambda('lambda_7B98')
    def lambda_7B98():
        OP_8F(0x00FE, 69640, 1250, 53350, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x003A, 0x0001, lambda_7B98)

    WaitForThreadExit(0x003A, 0x0001)

    Return()

# id: 0x003A offset: 0x7BB3
@scena.Code('func_3A_7BB3')
def func_3A_7BB3():
    OP_7D(0x00, 0x0029, 0x0014, 0x0064)
    SetChrChipByIndex(0x0029, 2)
    SetChrSubChip(0x0029, 6)

    @scena.Lambda('lambda_7BCB')
    def lambda_7BCB():
        OP_96(0x00FE, 0x00010806, 0x000004E2, 0x0000C8E6, 0x000001F4, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x0029, 0x0001, lambda_7BCB)

    WaitForThreadExit(0x0029, 0x0001)
    OP_22(0x00A4, 0x00, 0x64)

    @scena.Lambda('lambda_7BF3')
    def lambda_7BF3():
        OP_8C(0x00FE, 340, 400)

        ExitThread()

    DispatchAsync(0x0029, 0x0003, lambda_7BF3)

    @scena.Lambda('lambda_7C01')
    def lambda_7C01():
        OP_96(0x00FE, 0x00011242, 0x000004E2, 0x0000C8E6, 0x000001F4, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x0029, 0x0001, lambda_7C01)

    WaitForThreadExit(0x0029, 0x0001)
    OP_22(0x00A4, 0x00, 0x64)

    @scena.Lambda('lambda_7C29')
    def lambda_7C29():
        OP_8C(0x00FE, 160, 400)

        ExitThread()

    DispatchAsync(0x0029, 0x0003, lambda_7C29)

    @scena.Lambda('lambda_7C37')
    def lambda_7C37():
        OP_96(0x00FE, 0x00010996, 0x000004E2, 0x0000D804, 0x000005DC, 0x00001388)

        ExitThread()

    DispatchAsync(0x0029, 0x0001, lambda_7C37)

    WaitForThreadExit(0x0029, 0x0001)
    OP_22(0x00A4, 0x00, 0x64)
    OP_7D(0x01, 0x0029, 0x0000, 0x0000)
    SetChrChipByIndex(0x0029, 3)
    SetChrSubChip(0x0029, 5)

    @scena.Lambda('lambda_7C71')
    def lambda_7C71():
        OP_8F(0x00FE, 68840, 1250, 53640, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x0029, 0x0001, lambda_7C71)

    Sleep(100)

    OP_22(0x00D6, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x0029, 500, 500, -1000, 0, 0, 0, 2000, 2000, 2000, 0x00FF, 0, 0, 0, 0)
    OP_7C(0x00000000, 0x00000190, 0x00000BB8, 0x000000C8)
    SetChrChipByIndex(0x003A, 31)
    SetChrSubChip(0x003A, 0)
    OP_8C(0x003A, 340, 0)

    @scena.Lambda('lambda_7CED')
    def lambda_7CED():
        OP_9E(0x00FE, 0x00000028, 0x00000000, 0x000001F4, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x003A, 0x0002, lambda_7CED)

    @scena.Lambda('lambda_7D07')
    def lambda_7D07():
        OP_96(0x00FE, 0x00011238, 0x000004E2, 0x0000C832, 0x000000C8, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x003A, 0x0001, lambda_7D07)

    WaitForThreadExit(0x003A, 0x0001)
    OP_22(0x00A4, 0x00, 0x64)
    SetChrChipByIndex(0x003A, 30)
    SetChrSubChip(0x003A, 0)

    @scena.Lambda('lambda_7D39')
    def lambda_7D39():
        OP_99(0x00FE, 0x00, 0x03, 0x000009C4)

        ExitThread()

    DispatchAsync(0x003A, 0x0002, lambda_7D39)

    WaitForThreadExit(0x003A, 0x0002)
    OP_7D(0x00, 0x0029, 0x0014, 0x0064)
    SetChrChipByIndex(0x0029, 1)
    SetChrSubChip(0x0029, 2)

    @scena.Lambda('lambda_7D60')
    def lambda_7D60():
        OP_8C(0x00FE, 80, 400)

        ExitThread()

    DispatchAsync(0x0029, 0x0003, lambda_7D60)

    @scena.Lambda('lambda_7D6E')
    def lambda_7D6E():
        OP_96(0x00FE, 0x000104DC, 0x000004E2, 0x0000CFDA, 0x000001F4, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x0029, 0x0001, lambda_7D6E)

    @scena.Lambda('lambda_7D8C')
    def lambda_7D8C():
        OP_99(0x00FE, 0x03, 0x07, 0x000009C4)

        ExitThread()

    DispatchAsync(0x003A, 0x0002, lambda_7D8C)

    @scena.Lambda('lambda_7D9C')
    def lambda_7D9C():
        OP_8F(0x00FE, 69380, 1250, 52980, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x003A, 0x0001, lambda_7D9C)

    Sleep(100)

    OP_22(0x0084, 0x00, 0x64)
    WaitForThreadExit(0x0029, 0x0001)
    OP_22(0x00A4, 0x00, 0x64)
    OP_7D(0x01, 0x0029, 0x0000, 0x0000)

    Return()

# id: 0x003B offset: 0x7DCE
@scena.Code('func_3B_7DCE')
def func_3B_7DCE():
    Sleep(400)

    SetChrFlags(0x003A, 0x0020)
    SetChrChipByIndex(0x003A, 30)
    SetChrSubChip(0x003A, 0)

    @scena.Lambda('lambda_7DE8')
    def lambda_7DE8():
        OP_96(0x00FE, 0x000113A0, 0x000004E2, 0x0000D570, 0x000001F4, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x003A, 0x0001, lambda_7DE8)

    @scena.Lambda('lambda_7E06')
    def lambda_7E06():
        OP_99(0x00FE, 0x00, 0x03, 0x000009C4)

        ExitThread()

    DispatchAsync(0x003A, 0x0002, lambda_7E06)

    WaitForThreadExit(0x003A, 0x0001)
    CreateThread(0x0029, 0x00, 0x01, 0x003A)
    OP_22(0x00A4, 0x00, 0x64)

    @scena.Lambda('lambda_7E27')
    def lambda_7E27():
        OP_99(0x00FE, 0x03, 0x07, 0x000009C4)

        ExitThread()

    DispatchAsync(0x003A, 0x0002, lambda_7E27)

    @scena.Lambda('lambda_7E37')
    def lambda_7E37():
        OP_8F(0x00FE, 69170, 1250, 53520, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x003A, 0x0001, lambda_7E37)

    Sleep(100)

    OP_22(0x0084, 0x00, 0x64)

    Return()

# id: 0x003C offset: 0x7E57
@scena.Code('func_3C_7E57')
def func_3C_7E57():
    SetChrChipByIndex(0x002A, 3)
    SetChrSubChip(0x002A, 5)
    OP_7D(0x00, 0x002A, 0x0014, 0x00C8)

    @scena.Lambda('lambda_7E6F')
    def lambda_7E6F():
        OP_8F(0x00FE, 72270, 1250, 53150, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x002A, 0x0001, lambda_7E6F)

    Sleep(100)

    @scena.Lambda('lambda_7E8F')
    def lambda_7E8F():
        OP_8C(0x00FE, 90, 200)

        ExitThread()

    DispatchAsync(0x0039, 0x0003, lambda_7E8F)

    WaitForThreadExit(0x002A, 0x0001)
    OP_22(0x00D6, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x0039, 1000, 500, 0, 0, 0, 0, 2000, 2000, 2000, 0x00FF, 0, 0, 0, 0)
    OP_7C(0x00000000, 0x00000190, 0x00000BB8, 0x000000C8)
    OP_7D(0x01, 0x002A, 0x0000, 0x0000)
    SetChrChipByIndex(0x0039, 15)
    SetChrSubChip(0x0039, 0)
    TerminateThread(0x0039, 0x03)
    OP_8C(0x0039, 100, 0)

    @scena.Lambda('lambda_7F0A')
    def lambda_7F0A():
        OP_9E(0x00FE, 0x00000028, 0x00000000, 0x000001F4, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x0039, 0x0002, lambda_7F0A)

    @scena.Lambda('lambda_7F24')
    def lambda_7F24():
        OP_8F(0x00FE, 70820, 1250, 53150, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0039, 0x0001, lambda_7F24)

    WaitForThreadExit(0x0039, 0x0001)

    Return()

# id: 0x003D offset: 0x7F3F
@scena.Code('func_3D_7F3F')
def func_3D_7F3F():
    @scena.Lambda('lambda_7F45')
    def lambda_7F45():
        OP_8F(0x00FE, 71220, 1250, 53150, 500, 0x00)

        ExitThread()

    DispatchAsync(0x0039, 0x0001, lambda_7F45)

    @scena.Lambda('lambda_7F60')
    def lambda_7F60():
        OP_8F(0x00FE, 72670, 1250, 53150, 500, 0x00)

        ExitThread()

    DispatchAsync(0x002A, 0x0001, lambda_7F60)

    @scena.Lambda('lambda_7F7B')
    def lambda_7F7B():
        OP_9E(0x00FE, 0x0000003C, 0x00000000, 0x00000000, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x0039, 0x0002, lambda_7F7B)

    @scena.Lambda('lambda_7F95')
    def lambda_7F95():
        OP_9E(0x00FE, 0x0000003C, 0x00000000, 0x00000000, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x002A, 0x0002, lambda_7F95)

    WaitForThreadExit(0x0039, 0x0001)
    TerminateThread(0x0039, 0x02)
    WaitForThreadExit(0x002A, 0x0001)
    TerminateThread(0x002A, 0x02)
    OP_22(0x00D6, 0x00, 0x64)
    SetChrChipByIndex(0x0039, 30)
    SetChrSubChip(0x0039, 7)
    PlayEffect(0x00, 0xFF, 0x0039, 1000, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    SetChrChipByIndex(0x002A, 2)
    WaitForThreadExit(0x002A, 0x0002)

    @scena.Lambda('lambda_800F')
    def lambda_800F():
        OP_96(0x00FE, 0x00012386, 0x000004E2, 0x0000CF8A, 0x000001F4, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x002A, 0x0001, lambda_800F)

    WaitForThreadExit(0x002A, 0x0001)
    OP_22(0x00A4, 0x00, 0x64)
    SetChrChipByIndex(0x002A, 3)
    SetChrSubChip(0x002A, 5)
    OP_7D(0x00, 0x002A, 0x0014, 0x00C8)

    @scena.Lambda('lambda_8049')
    def lambda_8049():
        OP_8F(0x00FE, 72670, 1250, 53150, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x002A, 0x0001, lambda_8049)

    WaitForThreadExit(0x002A, 0x0001)
    OP_22(0x00D6, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x0039, 1000, 500, 0, 0, 0, 0, 2000, 2000, 2000, 0x00FF, 0, 0, 0, 0)
    OP_7C(0x00000000, 0x00000190, 0x00000BB8, 0x000000C8)
    OP_7D(0x01, 0x002A, 0x0000, 0x0000)
    SetChrChipByIndex(0x0039, 15)
    WaitForThreadExit(0x0039, 0x0000)

    @scena.Lambda('lambda_80C6')
    def lambda_80C6():
        OP_9E(0x00FE, 0x0000003C, 0x00000000, 0x000001F4, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x0039, 0x0002, lambda_80C6)

    @scena.Lambda('lambda_80E0')
    def lambda_80E0():
        OP_8F(0x00FE, 70420, 1250, 53150, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0039, 0x0001, lambda_80E0)

    WaitForThreadExit(0x0039, 0x0001)
    Sleep(200)

    @scena.Lambda('lambda_8105')
    def lambda_8105():
        OP_8C(0x00FE, 160, 400)

        ExitThread()

    DispatchAsync(0x0039, 0x0003, lambda_8105)

    @scena.Lambda('lambda_8113')
    def lambda_8113():
        OP_96(0x00FE, 0x000116E8, 0x000004E2, 0x0000D6EC, 0x000001F4, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x0039, 0x0001, lambda_8113)

    WaitForThreadExit(0x0039, 0x0001)
    OP_22(0x00A4, 0x00, 0x64)
    SetChrChipByIndex(0x0039, 30)
    SetChrSubChip(0x0039, 3)

    @scena.Lambda('lambda_8145')
    def lambda_8145():
        OP_99(0x00FE, 0x03, 0x07, 0x000009C4)

        ExitThread()

    DispatchAsync(0x0039, 0x0002, lambda_8145)

    @scena.Lambda('lambda_8155')
    def lambda_8155():
        OP_96(0x00FE, 0x000119AE, 0x000004E2, 0x0000D1A6, 0x000001F4, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x0039, 0x0001, lambda_8155)

    Sleep(100)

    OP_22(0x00D6, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x0039, 1000, 500, -1000, 0, 0, 0, 2000, 2000, 2000, 0x00FF, 0, 0, 0, 0)
    OP_7C(0x00000000, 0x00000190, 0x00000BB8, 0x000000C8)
    SetChrChipByIndex(0x002A, 27)
    SetChrSubChip(0x002A, 0)
    OP_8C(0x002A, 340, 0)

    @scena.Lambda('lambda_81D4')
    def lambda_81D4():
        OP_9E(0x00FE, 0x0000003C, 0x00000000, 0x000001F4, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x002A, 0x0002, lambda_81D4)

    @scena.Lambda('lambda_81EE')
    def lambda_81EE():
        OP_8F(0x00FE, 73710, 1250, 51110, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x002A, 0x0001, lambda_81EE)

    WaitForThreadExit(0x002A, 0x0001)
    Sleep(200)

    OP_7D(0x00, 0x002A, 0x0014, 0x00C8)

    @scena.Lambda('lambda_821B')
    def lambda_821B():
        OP_8C(0x00FE, 250, 400)

        ExitThread()

    DispatchAsync(0x002A, 0x0003, lambda_821B)

    @scena.Lambda('lambda_8229')
    def lambda_8229():
        OP_96(0x00FE, 0x0001255C, 0x000004E2, 0x0000CFDA, 0x000001F4, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x002A, 0x0001, lambda_8229)

    WaitForThreadExit(0x002A, 0x0001)
    OP_22(0x00A4, 0x00, 0x64)
    SetChrChipByIndex(0x002A, 3)
    SetChrSubChip(0x002A, 5)

    @scena.Lambda('lambda_825B')
    def lambda_825B():
        OP_8F(0x00FE, 72970, 1250, 53210, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x002A, 0x0001, lambda_825B)

    SetChrChipByIndex(0x0039, 15)
    WaitForThreadExit(0x0039, 0x0000)

    @scena.Lambda('lambda_8280')
    def lambda_8280():
        OP_8C(0x00FE, 70, 400)

        ExitThread()

    DispatchAsync(0x0039, 0x0003, lambda_8280)

    @scena.Lambda('lambda_828E')
    def lambda_828E():
        OP_96(0x00FE, 0x000112A6, 0x000004E2, 0x0000CFA8, 0x000001F4, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x0039, 0x0001, lambda_828E)

    WaitForThreadExit(0x002A, 0x0001)
    OP_7D(0x01, 0x002A, 0x0000, 0x0000)
    OP_22(0x0084, 0x00, 0x64)

    Return()

# id: 0x003E offset: 0x82B9
@scena.Code('func_3E_82B9')
def func_3E_82B9():
    @scena.Lambda('lambda_82BF')
    def lambda_82BF():
        OP_99(0x00FE, 0x00, 0x07, 0x000005DC)
        Yield()

        Jump('lambda_82BF')

    DispatchAsync2(0x0043, 0x0000, lambda_82BF)

    @scena.Lambda('lambda_82D2')
    def lambda_82D2():
        OP_99(0x00FE, 0x00, 0x07, 0x000005DC)
        Yield()

        Jump('lambda_82D2')

    DispatchAsync2(0x0044, 0x0000, lambda_82D2)

    @scena.Lambda('lambda_82E5')
    def lambda_82E5():
        OP_8E(0x00FE, 100580, 250, 30720, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x002B, 0x0001, lambda_82E5)

    Sleep(100)

    @scena.Lambda('lambda_8305')
    def lambda_8305():
        OP_8E(0x00FE, 99300, 250, 32090, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x002C, 0x0001, lambda_8305)

    Sleep(200)

    OP_8C(0x0043, 225, 400)
    WaitForThreadExit(0x002B, 0x0001)
    OP_8C(0x002B, 0, 400)
    SetChrChipByIndex(0x002B, 7)
    WaitForThreadExit(0x002C, 0x0001)
    OP_8C(0x002C, 90, 400)
    SetChrChipByIndex(0x002C, 7)
    OP_22(0x00D6, 0x00, 0x64)
    PlayEffect(0x00, 0x00, 0x0043, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_99(0x002B, 0x00, 0x07, 0x00000BB8)

    @scena.Lambda('lambda_8391')
    def lambda_8391():
        OP_9E(0x0043, 0x0000001E, 0x00000000, 0x000007D0, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x0043, 0x0001, lambda_8391)

    OP_22(0x00D6, 0x00, 0x64)
    PlayEffect(0x00, 0x01, 0x0043, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_99(0x002C, 0x00, 0x07, 0x00000BB8)
    OP_22(0x00D6, 0x00, 0x64)
    PlayEffect(0x00, 0x00, 0x0043, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_99(0x002B, 0x00, 0x07, 0x00000BB8)
    OP_22(0x00D6, 0x00, 0x64)
    PlayEffect(0x00, 0x01, 0x0043, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_99(0x002C, 0x00, 0x07, 0x00000BB8)
    PlayEffect(0x01, 0x00, 0x0043, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(200)

    @scena.Lambda('lambda_84AE')
    def lambda_84AE():
        OP_96(0x00FE, 0x000188F8, 0x000000FA, 0x00007364, 0x000003E8, 0x00001388)

        ExitThread()

    DispatchAsync(0x002B, 0x0001, lambda_84AE)

    Sleep(100)

    @scena.Lambda('lambda_84D1')
    def lambda_84D1():
        OP_96(0x00FE, 0x00017FCA, 0x000000FA, 0x00007D00, 0x000003E8, 0x00001388)

        ExitThread()

    DispatchAsync(0x002C, 0x0001, lambda_84D1)

    WaitForThreadExit(0x002B, 0x0001)
    SetChrChipByIndex(0x002B, 5)
    WaitForThreadExit(0x002C, 0x0001)
    SetChrChipByIndex(0x002C, 5)
    OP_83(0x00, 0x02)
    SetChrFlags(0x0043, 0x0080)

    Return()

# id: 0x003F offset: 0x8506
@scena.Code('func_3F_8506')
def func_3F_8506():
    @scena.Lambda('lambda_850C')
    def lambda_850C():
        OP_8E(0x00FE, 99470, 250, 35230, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x002F, 0x0001, lambda_850C)

    Sleep(100)

    @scena.Lambda('lambda_852C')
    def lambda_852C():
        OP_8E(0x00FE, 99520, 250, 34120, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0030, 0x0001, lambda_852C)

    Sleep(200)

    WaitForThreadExit(0x002F, 0x0001)
    OP_8C(0x002F, 90, 400)
    SetChrChipByIndex(0x002F, 7)
    WaitForThreadExit(0x0030, 0x0001)
    OP_8C(0x0030, 90, 400)
    SetChrChipByIndex(0x0030, 7)
    OP_22(0x00D6, 0x00, 0x64)
    PlayEffect(0x00, 0x02, 0x0044, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_99(0x002F, 0x00, 0x07, 0x00000BB8)

    @scena.Lambda('lambda_85B1')
    def lambda_85B1():
        OP_9E(0x0044, 0x0000001E, 0x00000000, 0x000007D0, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x0044, 0x0001, lambda_85B1)

    OP_22(0x00D6, 0x00, 0x64)
    PlayEffect(0x00, 0x03, 0x0044, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_99(0x0030, 0x00, 0x07, 0x00000BB8)
    OP_22(0x00D6, 0x00, 0x64)
    PlayEffect(0x00, 0x02, 0x0044, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_99(0x002F, 0x00, 0x07, 0x00000BB8)
    OP_22(0x00D6, 0x00, 0x64)
    PlayEffect(0x00, 0x03, 0x0044, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_99(0x0030, 0x00, 0x07, 0x00000BB8)
    PlayEffect(0x01, 0x02, 0x0044, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(200)

    @scena.Lambda('lambda_86CE')
    def lambda_86CE():
        OP_96(0x00FE, 0x000180EC, 0x000000FA, 0x0000894E, 0x000003E8, 0x00001388)

        ExitThread()

    DispatchAsync(0x002F, 0x0001, lambda_86CE)

    Sleep(100)

    @scena.Lambda('lambda_86F1')
    def lambda_86F1():
        OP_96(0x00FE, 0x00018146, 0x000000FA, 0x00008552, 0x000003E8, 0x00001388)

        ExitThread()

    DispatchAsync(0x0030, 0x0001, lambda_86F1)

    WaitForThreadExit(0x002F, 0x0001)
    SetChrChipByIndex(0x002F, 5)
    WaitForThreadExit(0x0030, 0x0001)
    SetChrChipByIndex(0x0030, 5)
    OP_83(0x02, 0x02)
    SetChrFlags(0x0044, 0x0080)

    Return()

# id: 0x0040 offset: 0x8726
@scena.Code('func_40_8726')
def func_40_8726():
    @scena.Lambda('lambda_872C')
    def lambda_872C():
        OP_8E(0x00FE, 97220, 250, 37240, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0033, 0x0001, lambda_872C)

    Sleep(100)

    @scena.Lambda('lambda_874C')
    def lambda_874C():
        OP_8E(0x00FE, 97460, 250, 35920, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0034, 0x0001, lambda_874C)

    Sleep(200)

    OP_8C(0x0045, 270, 400)
    WaitForThreadExit(0x0033, 0x0001)
    OP_8C(0x0033, 90, 400)
    SetChrChipByIndex(0x0033, 7)
    WaitForThreadExit(0x0034, 0x0001)
    OP_8C(0x0034, 45, 400)
    SetChrChipByIndex(0x0034, 7)
    OP_22(0x00D6, 0x00, 0x64)
    PlayEffect(0x00, 0x04, 0x0045, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_99(0x0033, 0x00, 0x07, 0x00000BB8)

    @scena.Lambda('lambda_87D8')
    def lambda_87D8():
        OP_9E(0x0045, 0x0000001E, 0x00000000, 0x000007D0, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x0045, 0x0001, lambda_87D8)

    OP_22(0x00D6, 0x00, 0x64)
    PlayEffect(0x00, 0x05, 0x0045, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_99(0x0034, 0x00, 0x07, 0x00000BB8)
    OP_22(0x00D6, 0x00, 0x64)
    PlayEffect(0x00, 0x04, 0x0045, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_99(0x0033, 0x00, 0x07, 0x00000BB8)
    OP_22(0x00D6, 0x00, 0x64)
    PlayEffect(0x00, 0x05, 0x0045, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_99(0x0034, 0x00, 0x07, 0x00000BB8)
    PlayEffect(0x01, 0x04, 0x0045, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(200)

    @scena.Lambda('lambda_88F5')
    def lambda_88F5():
        OP_96(0x00FE, 0x000178A4, 0x00000000, 0x000091E6, 0x000003E8, 0x00001388)

        ExitThread()

    DispatchAsync(0x0033, 0x0001, lambda_88F5)

    Sleep(100)

    @scena.Lambda('lambda_8918')
    def lambda_8918():
        OP_96(0x00FE, 0x00017A48, 0x000000FA, 0x000089B2, 0x000003E8, 0x00001388)

        ExitThread()

    DispatchAsync(0x0034, 0x0001, lambda_8918)

    WaitForThreadExit(0x0033, 0x0001)
    SetChrChipByIndex(0x0033, 5)
    WaitForThreadExit(0x0034, 0x0001)
    SetChrChipByIndex(0x0034, 5)
    OP_83(0x04, 0x02)
    SetChrFlags(0x0045, 0x0080)

    Return()

# id: 0x0041 offset: 0x894D
@scena.Code('func_41_894D')
def func_41_894D():
    @scena.Lambda('lambda_8953')
    def lambda_8953():
        OP_8E(0x00FE, 95200, 0, 33040, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0038, 0x0001, lambda_8953)

    Sleep(100)

    @scena.Lambda('lambda_8973')
    def lambda_8973():
        OP_8E(0x00FE, 93820, 0, 34210, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0037, 0x0001, lambda_8973)

    Sleep(200)

    OP_8C(0x0046, 180, 400)
    WaitForThreadExit(0x0038, 0x0001)
    OP_8C(0x0038, 0, 400)
    SetChrChipByIndex(0x0038, 7)
    WaitForThreadExit(0x0037, 0x0001)
    OP_8C(0x0037, 90, 400)
    SetChrChipByIndex(0x0037, 7)
    OP_22(0x00D6, 0x00, 0x64)
    PlayEffect(0x00, 0x06, 0x0046, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_99(0x0038, 0x00, 0x07, 0x00000BB8)

    @scena.Lambda('lambda_89FF')
    def lambda_89FF():
        OP_9E(0x0046, 0x0000001E, 0x00000000, 0x000007D0, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x0046, 0x0001, lambda_89FF)

    OP_22(0x00D6, 0x00, 0x64)
    PlayEffect(0x00, 0x07, 0x0046, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_99(0x0037, 0x00, 0x07, 0x00000BB8)
    OP_22(0x00D6, 0x00, 0x64)
    PlayEffect(0x00, 0x06, 0x0046, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_99(0x0038, 0x00, 0x07, 0x00000BB8)
    OP_22(0x00D6, 0x00, 0x64)
    PlayEffect(0x00, 0x07, 0x0046, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_99(0x0037, 0x00, 0x07, 0x00000BB8)
    PlayEffect(0x01, 0x06, 0x0046, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(200)

    @scena.Lambda('lambda_8B1C')
    def lambda_8B1C():
        OP_96(0x00FE, 0x00017426, 0x00000000, 0x00007DD2, 0x000003E8, 0x00001388)

        ExitThread()

    DispatchAsync(0x0038, 0x0001, lambda_8B1C)

    Sleep(100)

    @scena.Lambda('lambda_8B3F')
    def lambda_8B3F():
        OP_96(0x00FE, 0x00016AB2, 0x00000000, 0x0000858E, 0x000003E8, 0x00001388)

        ExitThread()

    DispatchAsync(0x0037, 0x0001, lambda_8B3F)

    WaitForThreadExit(0x0038, 0x0001)
    SetChrChipByIndex(0x0038, 5)
    WaitForThreadExit(0x0037, 0x0001)
    SetChrChipByIndex(0x0037, 5)
    OP_83(0x06, 0x02)
    SetChrFlags(0x0046, 0x0080)

    Return()

# id: 0x0042 offset: 0x8B74
@scena.Code('func_42_8B74')
def func_42_8B74():
    OP_8E(0x002E, 69910, 250, 43750, 5000, 0x00)
    SetChrChipByIndex(0x002E, 3)
    OP_8C(0x002E, 90, 400)
    OP_99(0x002E, 0x00, 0x07, 0x00000BB8)
    PlayEffect(0x02, 0x00, 0x003D, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    SetChrChipByIndex(0x003D, 17)

    @scena.Lambda('lambda_8BDD')
    def lambda_8BDD():
        OP_99(0x00FE, 0x00, 0x03, 0x000007D0)

        ExitThread()

    DispatchAsync(0x003D, 0x0001, lambda_8BDD)

    OP_8C(0x002E, 270, 400)
    OP_99(0x002E, 0x00, 0x07, 0x00000BB8)
    PlayEffect(0x02, 0x01, 0x003E, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    SetChrChipByIndex(0x003E, 17)

    @scena.Lambda('lambda_8C37')
    def lambda_8C37():
        OP_99(0x00FE, 0x00, 0x03, 0x000007D0)

        ExitThread()

    DispatchAsync(0x003E, 0x0001, lambda_8C37)

    Return()

# id: 0x0043 offset: 0x8C42
@scena.Code('func_43_8C42')
def func_43_8C42():
    OP_8E(0x0031, 70780, 250, 42910, 5000, 0x00)
    SetChrChipByIndex(0x0031, 3)
    OP_22(0x00D6, 0x00, 0x64)
    PlayEffect(0x00, 0x02, 0x003D, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_99(0x0031, 0x00, 0x07, 0x00000BB8)

    @scena.Lambda('lambda_8CA4')
    def lambda_8CA4():
        OP_9E(0x003D, 0x0000001E, 0x00000000, 0x000007D0, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x003D, 0x0001, lambda_8CA4)

    Return()

# id: 0x0044 offset: 0x8CB9
@scena.Code('func_44_8CB9')
def func_44_8CB9():
    OP_8E(0x0032, 69070, 250, 42910, 5000, 0x00)
    SetChrChipByIndex(0x0032, 3)
    OP_22(0x00D6, 0x00, 0x64)
    PlayEffect(0x00, 0x03, 0x003E, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_99(0x0032, 0x00, 0x07, 0x00000BB8)

    @scena.Lambda('lambda_8D1B')
    def lambda_8D1B():
        OP_9E(0x003E, 0x0000001E, 0x00000000, 0x000007D0, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x003E, 0x0001, lambda_8D1B)

    Return()

# id: 0x0045 offset: 0x8D30
@scena.Code('func_45_8D30')
def func_45_8D30():
    OP_8E(0x0035, 71610, 250, 45020, 5000, 0x00)
    SetChrChipByIndex(0x0035, 3)
    OP_8C(0x0035, 315, 400)
    OP_99(0x0035, 0x00, 0x07, 0x00000BB8)
    PlayEffect(0x02, 0x04, 0x003B, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_8D94')
    def lambda_8D94():
        OP_9E(0x003B, 0x0000001E, 0x00000000, 0x000007D0, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x003B, 0x0001, lambda_8D94)

    SetChrChipByIndex(0x003B, 17)

    @scena.Lambda('lambda_8DB3')
    def lambda_8DB3():
        OP_99(0x00FE, 0x00, 0x03, 0x000007D0)

        ExitThread()

    DispatchAsync(0x003B, 0x0001, lambda_8DB3)

    Return()

# id: 0x0046 offset: 0x8DBE
@scena.Code('func_46_8DBE')
def func_46_8DBE():
    OP_8E(0x0036, 68340, 250, 45060, 5000, 0x00)
    SetChrChipByIndex(0x0036, 3)
    OP_8C(0x0036, 45, 400)
    OP_99(0x0036, 0x00, 0x07, 0x00000BB8)
    PlayEffect(0x02, 0x05, 0x003C, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_8E22')
    def lambda_8E22():
        OP_9E(0x003C, 0x0000001E, 0x00000000, 0x000007D0, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x003C, 0x0001, lambda_8E22)

    SetChrChipByIndex(0x003C, 17)

    @scena.Lambda('lambda_8E41')
    def lambda_8E41():
        OP_99(0x00FE, 0x00, 0x03, 0x000007D0)

        ExitThread()

    DispatchAsync(0x003C, 0x0001, lambda_8E41)

    Return()

# id: 0x0047 offset: 0x8E4C
@scena.Code('func_47_8E4C')
def func_47_8E4C():
    Sleep(200)

    def _loc_8E51(): pass

    label('loc_8E51')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_8E6F',
    )

    OP_22(0x013A, 0x00, 0x64)
    Sleep(200)

    OP_23(0x013A)
    Sleep(200)

    Jump('loc_8E51')

    def _loc_8E6F(): pass

    label('loc_8E6F')

    Return()

# id: 0x0048 offset: 0x8E70
@scena.Code('func_48_8E70')
def func_48_8E70():
    Sleep(150)

    def _loc_8E75(): pass

    label('loc_8E75')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_8E95',
    )

    OP_22(0x013F, 0x00, 0x5A)
    Sleep(150)

    OP_22(0x013F, 0x00, 0x5A)
    Sleep(300)

    Jump('loc_8E75')

    def _loc_8E95(): pass

    label('loc_8E95')

    Return()

# id: 0x0049 offset: 0x8E96
@scena.Code('func_49_8E96')
def func_49_8E96():
    If(
        (
            (Expr.Eval, "OP_29(0x00C4, 0x01, 0x0100)"),
            Expr.Return,
        ),
        'loc_8EA2',
    )

    Return()

    def _loc_8EA2(): pass

    label('loc_8EA2')

    EventBegin(0x00)
    Fade(500)
    OP_6D(109680, 1500, 33080, 0)
    OP_67(0, 8200, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(44000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 108790, 1250, 32950, 90)
    SetChrPos(0x0105, 107810, 1250, 33760, 90)
    SetChrPos(0x0104, 107340, 1250, 32390, 90)
    SetChrPos(0x0108, 106280, 1250, 33000, 90)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010460357V#1004F咦？锁开着？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060460358V#044F这里的入口\n',
            '在没有武术大会等活动的时候\n',
            '都一直上着锁。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060460359V#042F那么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040460360V#035F呼，看来这就是\n',
            '最终的目的地了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080460361V#070F好……\n',
            '赶紧进去吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x00C4, 0x01, 0x0100)
    EventEnd(0x00)

    Return()

# id: 0x004A offset: 0x901E
@scena.Code('func_4A_901E')
def func_4A_901E():
    If(
        (
            (Expr.Eval, "OP_29(0x00C4, 0x01, 0x0100)"),
            Expr.Return,
        ),
        'loc_902A',
    )

    Return()

    def _loc_902A(): pass

    label('loc_902A')

    EventBegin(0x00)
    Fade(500)
    OP_6D(109680, 1500, 35580, 0)
    OP_67(0, 8200, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(44000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 108790, 1250, 35450, 90)
    SetChrPos(0x0105, 107810, 1250, 36260, 90)
    SetChrPos(0x0104, 107340, 1250, 34890, 90)
    SetChrPos(0x0108, 106280, 1250, 35500, 90)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010460357V#1004F咦？锁开着？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060460358V#044F这里的入口\n',
            '在没有武术大会等活动的时候\n',
            '都一直上着锁。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060460359V#042F那么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040460360V#035F呼，看来这就是\n',
            '最终的目的地了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080460361V#070F好……\n',
            '赶紧进去吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x00C4, 0x01, 0x0100)
    EventEnd(0x00)

    Return()

# id: 0x004B offset: 0x91A6
@scena.Code('func_4B_91A6')
def func_4B_91A6():
    If(
        (
            (Expr.Eval, "OP_29(0x00C4, 0x01, 0x0100)"),
            Expr.Return,
        ),
        'loc_91B2',
    )

    Return()

    def _loc_91B2(): pass

    label('loc_91B2')

    EventBegin(0x00)
    Fade(500)
    OP_6D(109680, 1500, 30580, 0)
    OP_67(0, 8200, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(44000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 108790, 1250, 30450, 90)
    SetChrPos(0x0105, 107810, 1250, 31260, 90)
    SetChrPos(0x0104, 107340, 1250, 29890, 90)
    SetChrPos(0x0108, 106280, 1250, 30500, 90)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010460357V#1004F咦？锁开着？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060460358V#044F这里的入口\n',
            '在没有武术大会等活动的时候\n',
            '都一直上着锁。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060460359V#042F那么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040460360V#035F呼，看来这就是\n',
            '最终的目的地了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080460361V#070F好……\n',
            '赶紧进去吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x00C4, 0x01, 0x0100)
    EventEnd(0x00)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
