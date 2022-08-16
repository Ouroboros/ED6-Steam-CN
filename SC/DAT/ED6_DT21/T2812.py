import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T2812_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2812   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'T2812.x'
    header.mapIndex       = 1
    header.bgm            = 84
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
        ('ED6_DT26/CH20271._CH', 'ED6_DT26/CH20271P._CP'),
        ('ED6_DT07/CH02390._CH', 'ED6_DT07/CH02390P._CP'),
        ('ED6_DT07/CH01360._CH', 'ED6_DT07/CH01360P._CP'),
        ('ED6_DT07/CH01780._CH', 'ED6_DT07/CH01780P._CP'),
        ('ED6_DT07/CH01080._CH', 'ED6_DT07/CH01080P._CP'),
        ('ED6_DT07/CH01580._CH', 'ED6_DT07/CH01580P._CP'),
        ('ED6_DT07/CH01370._CH', 'ED6_DT07/CH01370P._CP'),
        ('ED6_DT07/CH01363._CH', 'ED6_DT07/CH01363P._CP'),
        ('ED6_DT07/CH01090._CH', 'ED6_DT07/CH01090P._CP'),
        ('ED6_DT07/CH01093._CH', 'ED6_DT07/CH01093P._CP'),
        ('ED6_DT07/CH01460._CH', 'ED6_DT07/CH01460P._CP'),
        ('ED6_DT07/CH01583._CH', 'ED6_DT07/CH01583P._CP'),
    ]

# id: 0x10001 offset: 0x10A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '乔儿',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '罗迪',
            x                   = -1340,
            z                   = 4000,
            y                   = -1350,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '雅莉丝',
            x                   = -58700,
            z                   = 0,
            y                   = 25010,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '米克',
            x                   = -29460,
            z                   = 0,
            y                   = 30840,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '罗伊斯',
            x                   = -30830,
            z                   = 450,
            y                   = 26450,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0115,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '莫妮卡',
            x                   = -62080,
            z                   = 0,
            y                   = 27320,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '德尼斯',
            x                   = -28980,
            z                   = 0,
            y                   = 970,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '芙拉瑟',
            x                   = -60470,
            z                   = 0,
            y                   = 950,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '帕布尔',
            x                   = -61916,
            z                   = 200,
            y                   = 30650,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0115,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            name                = '艾福托老师',
            x                   = 30000,
            z                   = 0,
            y                   = 30750,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0002,
        ),
    )

# id: 0x10002 offset: 0x24A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x24A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x24A
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x24A
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_25D',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    MapSetFlags(0x10000000)
    Event(0, func_0C_8E1)

    def _loc_25D(): pass

    label('loc_25D')

    Return()

# id: 0x0001 offset: 0x25E
@scena.Code('func_01_25E')
def func_01_25E():
    Return()

# id: 0x0002 offset: 0x25F
@scena.Code('func_02_25F')
def func_02_25F():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '哦，怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '马上就是门禁了，\n',
            '别出去太久哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0003 offset: 0x29D
@scena.Code('func_03_29D')
def func_03_29D():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '小说的登场人物，\n',
            '多数也是以现实的人们\n',
            '为模型构思出来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只凭想象来写的话，\n',
            '人物很容易变得单薄。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0004 offset: 0x30F
@scena.Code('func_04_30F')
def func_04_30F():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_382',
    )

    ChrTalk(
        0x00FE,
        (
            '虽说是下人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对来自帝国的我来说\n',
            '蕾娜是我最好的朋友。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '到现在为止一直\n',
            '都是这么想的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3F2')

    def _loc_382(): pass

    label('loc_382')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '我有多么\n',
            '期待着旅行，\n',
            '蕾娜也应该知道。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '知道如此却瞒着我\n',
            '计划回去……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……这等于是背叛的行为。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3F2(): pass

    label('loc_3F2')

    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0x3F6
@scena.Code('func_05_3F6')
def func_05_3F6():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_444',
    )

    ChrTalk(
        0x00FE,
        (
            '现在考试刚刚结束，\n',
            '正是制造区别的机会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好！要学习了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4A9')

    def _loc_444(): pass

    label('loc_444')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '现在考试刚刚结束\n',
            '正是制造区别的机会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵，现在开始努力学习，\n',
            '下次考试一定要再拿高分。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4A9(): pass

    label('loc_4A9')

    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0x4AD
@scena.Code('func_06_4AD')
def func_06_4AD():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_50A',
    )

    ChrTalk(
        0x00FE,
        (
            '这个房间里的学生\n',
            '完全是七零八落的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过正因此\n',
            '才能相处好也说不定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_58A')

    def _loc_50A(): pass

    label('loc_50A')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '帕布尔是个文学少女，\n',
            '雅莉丝可爱又好奇……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……而我却\n',
            '喜欢运动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '住在这个房间里的学生，\n',
            '是来自不同的班级的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_58A(): pass

    label('loc_58A')

    TalkEnd(0x00FE)

    Return()

# id: 0x0007 offset: 0x58E
@scena.Code('func_07_58E')
def func_07_58E():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_5F7',
    )

    ChrTalk(
        0x00FE,
        (
            '学生之中对选举\n',
            '漠不关心的人似乎也挺多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好不容易有深刻讨论政治\n',
            '的机会，真是遗憾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_697')

    def _loc_5F7(): pass

    label('loc_5F7')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '我作为学习政治经济的人，\n',
            '对这次的选举也很有兴趣。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，学生之中\n',
            '漠不关心的人似乎也挺多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '罗基克的父亲就是候选人，\n',
            '想想是和自己非常近的事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_697(): pass

    label('loc_697')

    TalkEnd(0x00FE)

    Return()

# id: 0x0008 offset: 0x69B
@scena.Code('func_08_69B')
def func_08_69B():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '这么说来\n',
            '亚吉鲁那家伙不在呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '去哪儿了呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0009 offset: 0x6D7
@scena.Code('func_09_6D7')
def func_09_6D7():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_721',
    )

    ChrTalk(
        0x00FE,
        (
            '这套衣服，是坎诺\n',
            '帮我做的哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(0, 0x000A)

    ChrTalk(
        0x00FE,
        (
            '不愧是美术部呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_786')

    def _loc_721(): pass

    label('loc_721')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '在整理的时候发现了\n',
            '学院祭上穿的衣服！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这个是坎诺\n',
            '帮我做的哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(0, 0x000A)

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，很可爱吧㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_786(): pass

    label('loc_786')

    OP_63(0x00FE)
    TalkEnd(0x00FE)

    Return()

# id: 0x000A offset: 0x78D
@scena.Code('func_0A_78D')
def func_0A_78D():
    OP_62(0x00FE, 0x00000000, 2000, 0x0A, 0x0B, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)

    ExecExpressionWithValue(
        0x00FE,
        0x04,
        (
            (Expr.PushLong, 0x2D),
            Expr.Add2,
            Expr.Return,
        ),
    )

    Sleep(30)

    ExecExpressionWithValue(
        0x00FE,
        0x04,
        (
            (Expr.PushLong, 0x2D),
            Expr.Add2,
            Expr.Return,
        ),
    )

    Sleep(30)

    ExecExpressionWithValue(
        0x00FE,
        0x04,
        (
            (Expr.PushLong, 0x2D),
            Expr.Add2,
            Expr.Return,
        ),
    )

    Sleep(30)

    ExecExpressionWithValue(
        0x00FE,
        0x04,
        (
            (Expr.PushLong, 0x2D),
            Expr.Add2,
            Expr.Return,
        ),
    )

    Sleep(30)

    ExecExpressionWithValue(
        0x00FE,
        0x04,
        (
            (Expr.PushLong, 0x2D),
            Expr.Add2,
            Expr.Return,
        ),
    )

    Sleep(30)

    ExecExpressionWithValue(
        0x00FE,
        0x04,
        (
            (Expr.PushLong, 0x2D),
            Expr.Add2,
            Expr.Return,
        ),
    )

    Sleep(30)

    ExecExpressionWithValue(
        0x00FE,
        0x04,
        (
            (Expr.PushLong, 0x2D),
            Expr.Add2,
            Expr.Return,
        ),
    )

    Sleep(30)

    ExecExpressionWithValue(
        0x00FE,
        0x04,
        (
            (Expr.PushLong, 0x2D),
            Expr.Add2,
            Expr.Return,
        ),
    )

    Sleep(30)

    Return()

# id: 0x000B offset: 0x825
@scena.Code('func_0B_825')
def func_0B_825():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_88E',
    )

    ChrTalk(
        0x00FE,
        (
            '德尼斯那家伙\n',
            '每次都拿高分。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他总是拼命\n',
            '学习真是令人讨厌。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '富人更加富……吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8DD')

    def _loc_88E(): pass

    label('loc_88E')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '室友德尼斯那家伙\n',
            '已经开始学习了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '考试才刚刚结束\n',
            '真是讨厌的家伙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8DD(): pass

    label('loc_8DD')

    TalkEnd(0x00FE)

    Return()

# id: 0x000C offset: 0x8E1
@scena.Code('func_0C_8E1')
def func_0C_8E1():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_8F2',
    )

    Call(0, 0x000F)

    def _loc_8F2(): pass

    label('loc_8F2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_900',
    )

    Call(0, 0x000D)

    Jump('loc_904')

    def _loc_900(): pass

    label('loc_900')

    Call(0, 0x000E)

    def _loc_904(): pass

    label('loc_904')

    Return()

# id: 0x000D offset: 0x905
@scena.Code('func_0D_905')
def func_0D_905():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetFlags(0x0106, 0x0008)
    ChrSetFlags(0x0104, 0x0008)
    ChrSetFlags(0x0101, 0x0002)
    ChrSetFlags(0x0101, 0x0004)
    ChrClearFlags(0x0101, 0x0001)
    ChrSetChipByIndex(0x0101, 0)
    ChrSetSubChip(0x0101, 24)
    OP_6F(0x0009, 12)
    ChrSetPos(0x0101, -118350, 500, -2400, 0)
    ChrSetPos(0x0105, -118420, 0, -1130, 175)
    ChrSetPos(0x0008, -119240, 0, -1120, 145)
    ChrSetPos(0x0127, -120350, 0, -2570, 90)
    CameraMove(-118450, 500, -2400, 0)
    OP_67(0, 4720, -10000, 0)
    CameraSetDistance(3030, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_69(0x0101, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('女孩的声音')

    Talk(
        (
            '#0060211326V……艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('女孩的声音')

    Talk(
        (
            '#0060211327V艾丝蒂尔……来吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('艾丝蒂尔')

    Talk(
        (
            '#0010211328V#1007F嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    PlayBGM(84)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    ChrSetSubChip(0x0101, 39)
    Sleep(100)

    ChrSetSubChip(0x0101, 40)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010211329V#1004F咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0127,
        (
            '#0280211330V#150F啊、小艾！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060211331V#542F#5P太好了……\n',
            '你醒了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060211332V那个，感觉如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010211333V#1000F嗯……还好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(300)

    OP_6F(0x0009, 12)
    OP_70(0x0009, 15)
    ChrSetPos(0x0101, -118250, 500, -2400, 0)
    OP_99(0x0101, 0x19, 0x20, 1000)
    Sleep(500)

    ChrSetSubChip(0x0101, 41)
    Sleep(100)

    ChrSetSubChip(0x0101, 42)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010211334V#1015F咦……\n',
            '这里是女子宿舍吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211335V我怎么会在这里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 1500, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    Sleep(200)

    ChrSetFlags(0x0101, 0x0004)
    ChrClearFlags(0x0101, 0x0040)
    ChrClearFlags(0x0101, 0x0002)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetSubChip(0x0101, 0)
    ChrJumpTo(0x0101, -118670, 0, -3860, 100, 4000)
    ChrSetFlags(0x0101, 0x0001)
    ChrSetDirection(0x0101, 16, 0)
    OP_6F(0x0009, 15)
    OP_70(0x0009, 12)

    @scena.Lambda('lambda_0C51')
    def lambda_0C51():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_0C51)

    @scena.Lambda('lambda_0C5F')
    def lambda_0C5F():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0127, 0x0001, lambda_0C5F)

    @scena.Lambda('lambda_0C6D')
    def lambda_0C6D():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0C6D)

    WaitForThreadExit(0x0105, 0x0001)
    WaitForThreadExit(0x0127, 0x0001)
    WaitForThreadExit(0x0008, 0x0001)
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010211336V#1020F#2P啊、我！\n',
            '在窗外看到了『白影』！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211337V然后……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0510211338V#645F#1P唉……\n',
            '果然是看到幽灵了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060211339V#043F#5P艾丝蒂尔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060211340V那个『白影』\n',
            '是什么样子的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010211341V#1007F#2P嗯，嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211342V#1003F穿着古代的衣服，\n',
            '戴着面具的男人……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211343V白白的一边发光\n',
            '一边在空中滴溜溜地转……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211344V往旧校舍\n',
            '那边飞了去……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0127,
        (
            '#0280211345V#153F哎～看起来相当\n',
            '快乐的幽灵啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060211346V#047F#5P和各地目击\n',
            '『白影』的证言相同啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0510211347V#644F#1P而且，果然是旧校舍吗?',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010211348V#1019F#2P……什么玩笑。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0510211349V#643F#1P咦……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010211350V#1022F#2P谁知道是不是幽灵\n',
            '这不是正好吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211351V装神弄鬼的吓人\n',
            '还害我晕倒……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010211352V#1005F#2P#3S这笔帐，\n',
            '绝对要算清楚！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0510211353V#645F#1P算、算帐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0127,
        (
            '#0280211354V#153F小艾。\n',
            '你不是怕幽灵的吗～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0127, 500)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010211355V#1019F#2P我怕幽灵是因为\n',
            '不知道到底有没有！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211356V既然亲眼看到了，\n',
            '事到如今就没什么好怕的了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211357V我要让它再也出不来\n',
            '好好整治它一番！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0510211358V#644F#1P嗯～说你是顽强\n',
            '还是不正常了呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060211359V#041F#5P呵呵……\n',
            '到底是艾丝蒂尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(500)

    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/T2811._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000E offset: 0x1171
@scena.Code('func_0E_1171')
def func_0E_1171():
    EventBegin(0x00)
    OP_20(0x00000000)
    FadeOut(0, 0, -1)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetFlags(0x0104, 0x0008)
    ChrSetFlags(0x0101, 0x0002)
    ChrSetFlags(0x0101, 0x0004)
    ChrClearFlags(0x0101, 0x0001)
    ChrSetChipByIndex(0x0101, 0)
    ChrSetSubChip(0x0101, 24)
    OP_6F(0x0009, 12)
    ChrSetPos(0x0101, -118350, 500, -2400, 0)
    ChrSetPos(0x0103, -120030, 0, -4110, 35)
    ChrSetPos(0x0105, -118420, 0, -1130, 180)
    ChrSetPos(0x0008, -119240, 0, -1120, 145)
    ChrSetPos(0x0127, -120350, 0, -2570, 90)
    CameraMove(-118450, 500, -2400, 0)
    OP_67(0, 4720, -10000, 0)
    CameraSetDistance(3030, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_69(0x0101, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('女孩的声音')

    Talk(
        (
            '#0060211326V……艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('女孩的声音')

    Talk(
        (
            '#0060211327V艾丝蒂尔……醒醒……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('艾丝蒂尔')

    Talk(
        (
            '#0010211328V#1007F嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    PlayBGM(84)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    ChrSetSubChip(0x0101, 39)
    Sleep(100)

    ChrSetSubChip(0x0101, 40)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010211329V#1004F咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0127,
        (
            '#0280211330V#150F啊、小艾！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060211365V#542F#5P太好了……\n',
            '你醒了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030211366V#025F呼……\n',
            '冷汗都出来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030211367V#020F那么，感觉如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010211333V#1000F嗯……还好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(300)

    OP_6F(0x0009, 12)
    OP_70(0x0009, 15)
    ChrSetPos(0x0101, -118250, 500, -2400, 0)
    OP_99(0x0101, 0x19, 0x20, 1000)
    Sleep(500)

    ChrSetSubChip(0x0101, 41)
    Sleep(100)

    ChrSetSubChip(0x0101, 42)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010211334V#1015F咦……\n',
            '这里是女子宿舍吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211335V我怎么会在这里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 1500, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    Sleep(200)

    ChrSetFlags(0x0101, 0x0004)
    ChrClearFlags(0x0101, 0x0040)
    ChrClearFlags(0x0101, 0x0002)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetSubChip(0x0101, 0)
    ChrJumpTo(0x0101, -118670, 0, -3860, 100, 4000)
    ChrSetFlags(0x0101, 0x0001)
    ChrSetDirection(0x0101, 16, 0)
    OP_6F(0x0009, 15)
    OP_70(0x0009, 12)

    @scena.Lambda('lambda_14FF')
    def lambda_14FF():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_14FF)

    @scena.Lambda('lambda_150D')
    def lambda_150D():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_150D)

    @scena.Lambda('lambda_151B')
    def lambda_151B():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0127, 0x0001, lambda_151B)

    @scena.Lambda('lambda_1529')
    def lambda_1529():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1529)

    WaitForThreadExit(0x0105, 0x0001)
    WaitForThreadExit(0x0127, 0x0001)
    WaitForThreadExit(0x0008, 0x0001)
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010211336V#1020F#2P啊、我！\n',
            '在窗外看到了『白影』！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211337V然后……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030211373V#020F是是。\n',
            '我知道了，你镇定一点吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0510211338V#645F#1P唉……\n',
            '果然是看到幽灵了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060211339V#043F#5P艾丝蒂尔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060211340V那个『白影』\n',
            '是什么样子的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010211341V#1007F#2P嗯，嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211342V#1003F穿着古代的衣服，\n',
            '戴着面具的男人……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211343V白白的一边发光\n',
            '一边在空中滴溜溜地转……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211344V往旧校舍\n',
            '那边飞了去……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0127,
        (
            '#0280211345V#153F哎～看起来相当\n',
            '快乐的幽灵啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060211346V#047F#5P和各地目击\n',
            '『白影』的证言相同啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0510211347V#644F#1P而且，果然是旧校舍吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010211348V#1019F#2P……开什么玩笑。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0510211349V#643F#1P咦……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010211350V#1022F#2P是幽灵也好，恶作剧也好，\n',
            '胆子还真是不小啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211351V装神弄鬼地吓人，\n',
            '还害我丢脸晕倒……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010211352V#1005F#2P#3S这笔帐，\n',
            '绝对要算清楚！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0510211353V#645F#1P算、算帐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030211390V#027F真是的……\n',
            '你不是怕幽灵的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 500)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010211355V#1019F#2P我怕幽灵是因为\n',
            '不知道到底有没有！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211356V既然亲眼看到了，\n',
            '也就没什么好怕的了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211357V我要好好整治它一番！\n',
            '让它再也不敢出来！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0510211358V#644F#1P嗯～该说你顽强\n',
            '还是不正常呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060211359V#041F#5P呵呵……\n',
            '到底是艾丝蒂尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(500)

    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/T2811._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000F offset: 0x1A76
@scena.Code('func_0F_1A76')
def func_0F_1A76():
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
        (0x00000000, 'loc_1AF0'),
        (0x00000001, 'loc_1AF6'),
        (-1, 'loc_1AFC'),
    )

    def _loc_1AF0(): pass

    label('loc_1AF0')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_1AFC')

    def _loc_1AF6(): pass

    label('loc_1AF6')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_1AFC')

    def _loc_1AFC(): pass

    label('loc_1AFC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_1B0A',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    Jump('loc_1B0E')

    def _loc_1B0A(): pass

    label('loc_1B0A')

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    def _loc_1B0E(): pass

    label('loc_1B0E')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
