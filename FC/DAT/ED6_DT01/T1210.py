import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T1210_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T1210   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '奥兰橘婆婆'),
    TXT(0x02, '库赖老人'),
    TXT(0x03, '莱森村长'),
    TXT(0x04, '碧尔奈婆婆'),
    TXT(0x05, '鲁伊'),
    TXT(0x06, '菲戈'),
    TXT(0x07, '罗亚'),
    TXT(0x08, '贝斯卡'),
    TXT(0x09, '库赖老人'),
    TXT(0x0A, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'T1210.x'
    header.mapIndex       = 1
    header.bgm            = 15
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT01/T1210._SN', 'ED6_DT01/T1210_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x2CBD
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
        ('ED6_DT07/CH01010._CH', 'ED6_DT07/CH01010P._CP'),
        ('ED6_DT07/CH01000._CH', 'ED6_DT07/CH01000P._CP'),
        ('ED6_DT07/CH01490._CH', 'ED6_DT07/CH01490P._CP'),
        ('ED6_DT07/CH01180._CH', 'ED6_DT07/CH01180P._CP'),
        ('ED6_DT07/CH01470._CH', 'ED6_DT07/CH01470P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH01123._CH', 'ED6_DT07/CH01123P._CP'),
        ('ED6_DT07/CH01143._CH', 'ED6_DT07/CH01143P._CP'),
        ('ED6_DT07/CH00003._CH', 'ED6_DT07/CH00003P._CP'),
        ('ED6_DT07/CH00013._CH', 'ED6_DT07/CH00013P._CP'),
        ('ED6_DT07/CH00023._CH', 'ED6_DT07/CH00023P._CP'),
        ('ED6_DT07/CH01003._CH', 'ED6_DT07/CH01003P._CP'),
        ('ED6_DT07/CH01493._CH', 'ED6_DT07/CH01493P._CP'),
    ]

# id: 0x10002 offset: 0x112
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = -31600,
            z                   = 0,
            y                   = 2900,
            direction           = 270,
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
            x                   = -25500,
            z                   = 0,
            y                   = 8700,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            x                   = -1880,
            z                   = 0,
            y                   = 48500,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            x                   = 7500,
            z                   = 0,
            y                   = 46200,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            x                   = -1430,
            z                   = 0,
            y                   = 3310,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            x                   = 360,
            z                   = 0,
            y                   = 6440,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            x                   = 4650,
            z                   = 100,
            y                   = 45830,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x01D5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            x                   = 3300,
            z                   = 200,
            y                   = 48070,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x01D5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            x                   = 3430,
            z                   = 150,
            y                   = 45650,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x01D5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
    )

# id: 0x10003 offset: 0x232
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x232
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x232
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x232
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_27C',
    )

    SetChrPos(0x0009, 3300, -1000, 45700, 0)
    ClearChrFlags(0x0010, 0x0080)
    SetChrPos(0x000A, 6180, 0, 49500, 0)
    SetChrFlags(0x000A, 0x0010)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000E, 0x0080)
    ClearChrFlags(0x000F, 0x0080)

    Jump('loc_318')

    def _loc_27C(): pass

    label('loc_27C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_2A1',
    )

    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    SetChrPos(0x000D, -780, 0, 5750, 0)

    Jump('loc_318')

    def _loc_2A1(): pass

    label('loc_2A1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_2C6',
    )

    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    SetChrPos(0x000D, -780, 0, 5750, 0)

    Jump('loc_318')

    def _loc_2C6(): pass

    label('loc_2C6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_2E6',
    )

    ClearChrFlags(0x000D, 0x0080)
    SetChrPos(0x000D, -780, 0, 5750, 0)

    Jump('loc_318')

    def _loc_2E6(): pass

    label('loc_2E6')

    If(
        (
            (Expr.Eval, "OP_29(0x000E, 0x01, 0x0008)"),
            Expr.Return,
        ),
        'loc_318',
    )

    ClearChrFlags(0x000D, 0x0080)
    SetChrPos(0x000D, -1820, 0, 47460, 0)
    SetChrPos(0x000A, -1880, 0, 48500, 180)

    def _loc_318(): pass

    label('loc_318')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 5, 0x31D)),
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 6, 0x31E)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_329',
    )

    SetChrFlags(0x000A, 0x0080)

    def _loc_329(): pass

    label('loc_329')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_337',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, 0x000C)

    def _loc_337(): pass

    label('loc_337')

    Return()

# id: 0x0001 offset: 0x338
@scena.Code('Init')
def Init():
    Return()

# id: 0x0002 offset: 0x339
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_34E',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_34E(): pass

    label('loc_34E')

    Return()

# id: 0x0003 offset: 0x34F
@scena.Code('func_03_34F')
def func_03_34F():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_372',
    )

    OP_8D(0x00FE, -2590, 3920, 2730, 920, 1500)

    Jump('func_03_34F')

    def _loc_372(): pass

    label('loc_372')

    Return()

# id: 0x0004 offset: 0x373
@scena.Code('func_04_373')
def func_04_373():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_3BB',
    )

    ChrTalk(
        0x00FE,
        (
            '你们是来选购水果的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我家老头子\n',
            '到村长家去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8BF')

    def _loc_3BB(): pass

    label('loc_3BB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_493',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_456',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '希望老头子能找个机会\n',
            '和村里的人们一起\n',
            '坐下来好好谈谈。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是老头子很久以前\n',
            '就非常顽固……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '希望有人能够\n',
            '在其中调解一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_490')

    def _loc_456(): pass

    label('loc_456')

    ChrTalk(
        0x00FE,
        (
            '希望能够找个机会\n',
            '让老头子和村里的人\n',
            '坐下来好好谈谈。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_490(): pass

    label('loc_490')

    Jump('loc_8BF')

    def _loc_493(): pass

    label('loc_493')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_58E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_52D',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '又有军队的人\n',
            '来这个村子里调查案件了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '和之前来的士兵不同，\n',
            '他们的动作非常迅速干脆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那肯定是因为\n',
            '指挥他们的人换了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_58B')

    def _loc_52D(): pass

    label('loc_52D')

    ChrTalk(
        0x00FE,
        (
            '又有军队的人\n',
            '来这个村子里调查案件了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '和之前来的士兵不同，\n',
            '他们的动作非常迅速干脆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_58B(): pass

    label('loc_58B')

    Jump('loc_8BF')

    def _loc_58E(): pass

    label('loc_58E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 5, 0x31D)),
            Expr.Return,
        ),
        'loc_67C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_63D',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '我可不觉得\n',
            '老头子的意见有什么错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为他培育出了这个村里最好吃的东西，\n',
            '这可是事实。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，\n',
            '如果能稍微采纳一些其他的方法，\n',
            '是不是会更好呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_679')

    def _loc_63D(): pass

    label('loc_63D')

    ChrTalk(
        0x00FE,
        (
            '老头子如果能稍微\n',
            '采纳一些其他的方法，\n',
            '是不是会更好呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_679(): pass

    label('loc_679')

    Jump('loc_8BF')

    def _loc_67C(): pass

    label('loc_67C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 4, 0x31C)),
            Expr.Return,
        ),
        'loc_75F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_70C',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '我家的老头子，\n',
            '头脑真是有点硬呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一直拘泥于\n',
            '以前流传下来的古老方法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '和现在的年轻人\n',
            '所提出的意见总是不合。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_75C')

    def _loc_70C(): pass

    label('loc_70C')

    ChrTalk(
        0x00FE,
        (
            '我家的老头子，\n',
            '头脑真是有点硬呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '希望年轻人们\n',
            '不要因此望而生畏才好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_75C(): pass

    label('loc_75C')

    Jump('loc_8BF')

    def _loc_75F(): pass

    label('loc_75F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_864',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7FD',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '我们家的老头子啊，\n',
            '总是呆在果园里面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '即使去叫他回来吃饭，\n',
            '也要过一个小时才能看到他回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要等到饭菜都凉了，\n',
            '他才会回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_861')

    def _loc_7FD(): pass

    label('loc_7FD')

    ChrTalk(
        0x00FE,
        (
            '我们家的老头子啊，\n',
            '总是呆在果园里面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '即使去叫他回来吃饭，\n',
            '也要过一个小时才能看到他回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_861(): pass

    label('loc_861')

    Jump('loc_8BF')

    def _loc_864(): pass

    label('loc_864')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_8BF',
    )

    ChrTalk(
        0x00FE,
        (
            '难不成\n',
            '你们是来买水果的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真抱歉，老头子出去了。\n',
            '应该是到果树园那里去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8BF(): pass

    label('loc_8BF')

    TalkEnd(0x0008)

    Return()

# id: 0x0005 offset: 0x8C3
@scena.Code('func_05_8C3')
def func_05_8C3():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_913',
    )

    ChrTalk(
        0x00FE,
        (
            '我想用我自己的方法\n',
            '来种出美味的水果。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我不赞同那种做法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9CF')

    def _loc_913(): pass

    label('loc_913')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_959',
    )

    ChrTalk(
        0x00FE,
        (
            '下次开会时，\n',
            '我要让村里的年轻人\n',
            '再注意一下做法才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9CF')

    def _loc_959(): pass

    label('loc_959')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_9CF',
    )

    ChrTalk(
        0x00FE,
        (
            '我要让大家知道\n',
            '尽量让果树保持自然生长，\n',
            '这才是最重要的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就是要肯花时间，\n',
            '它们才能结出美味的果实。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9CF(): pass

    label('loc_9CF')

    TalkEnd(0x0009)

    Return()

# id: 0x0006 offset: 0x9D3
@scena.Code('func_06_9D3')
def func_06_9D3():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_A05',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，\n',
            '好像大家的意见无法统一啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_189B')

    def _loc_A05(): pass

    label('loc_A05')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_AD8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A8B',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '乍一看这个村子\n',
            '可能非常平静……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是还存在着\n',
            '好多隐藏的问题啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，\n',
            '也只有一个一个来解决它们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_AD5')

    def _loc_A8B(): pass

    label('loc_A8B')

    ChrTalk(
        0x00FE,
        (
            '乍一看这个村子\n',
            '可能非常平静……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是还存在着\n',
            '好多隐藏的问题啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_AD5(): pass

    label('loc_AD5')

    Jump('loc_189B')

    def _loc_AD8(): pass

    label('loc_AD8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_BA8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B3E',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '哦哦，是各位游击士啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那之后你们被王国军带走了，\n',
            '我还真替你们担心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BA5')

    def _loc_B3E(): pass

    label('loc_B3E')

    ChrTalk(
        0x00FE,
        (
            '没想到飞艇\n',
            '真的藏在那种地方……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为那些犯人\n',
            '很有可能还会再回来，\n',
            '所以废坑就由军队来接管了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BA5(): pass

    label('loc_BA5')

    Jump('loc_189B')

    def _loc_BA8(): pass

    label('loc_BA8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 5, 0x31D)),
            Expr.Return,
        ),
        'loc_C10',
    )

    OP_4A(0x00FE, 255)

    ChrTalk(
        0x00FE,
        (
            '要是在废坑中\n',
            '可以找到什么线索就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果你们知道了什么，\n',
            '一定要回来告诉我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_189B')

    def _loc_C10(): pass

    label('loc_C10')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 4, 0x31C)),
            Expr.Return,
        ),
        'loc_CC4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C8E',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '鲁伊所看到的空中飞影……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '难道说是『他』……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不会……不可能……\n',
            '已经好几十年没有发生过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CC1')

    def _loc_C8E(): pass

    label('loc_C8E')

    ChrTalk(
        0x00FE,
        (
            '不会……不可能……\n',
            '已经好几十年没有发生过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_CC1(): pass

    label('loc_CC1')

    Jump('loc_189B')

    def _loc_CC4(): pass

    label('loc_CC4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_1579',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 3, 0x31B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_152A',
    )

    SetScenaFlags(ScenaFlag(0x0063, 3, 0x31B))
    OP_28(0x0036, 0x01, 0x0004)
    EventBegin(0x00)
    OP_69(0x00FE, 1000)

    If(
        (
            (Expr.Eval, "OP_29(0x000E, 0x00, 0x04)"),
            Expr.Return,
        ),
        'loc_FBE',
    )

    ChrTalk(
        0x00FE,
        (
            '#1180021554V哦哦～\n',
            '你们都来了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1180021555V今天有什么事？\n',
            '大家是来这里玩的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030021556V#020F不是，我们还有工作要忙。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021557V有些遗憾呢，\n',
            '其实我很想喝一杯果实酒再走。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1180021558V呵、呵、呵。\n',
            '这个世上，有许多事不会随着你的想法而进行的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1180021559V对了，\n',
            '之前我忘了问了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1180021560V难道，\n',
            '你们是阿加特的同事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030021561V#020F嗯，虽然是同行，\n',
            '但并不代表我们会一起行动。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021562V充其量也就是认识而已吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1180021563V是这样吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1180021564V他依旧还是独来独往啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '村长幽寂地闭上了眼睛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0101,
        (
            '#0010021565V#501F？？？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010021566V怎么了，村长？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1180021567V啊，不好意思，失礼了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1180021568V那么，\n',
            '到这种偏僻的村庄有什么事呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1180021569V难道又是为了\n',
            '被通缉的魔兽而来的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1254')

    def _loc_FBE(): pass

    label('loc_FBE')

    ChrTalk(
        0x00FE,
        (
            '#1180021570V啊，几位客人。\n',
            '是来买水果的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030021571V#020F不，我们不是商人。\n',
            '我们是游击士协会的人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021572V您是这个村子的村长吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1180021573V嗯，是的。\n',
            '也算是本村的负责人吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1180021574V刚才是说游击士协会对吧。\n',
            '难道你们是阿加特的同事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030021575V#020F嗯，虽然是同行，\n',
            '但并不代表我们会一起行动。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021576V充其量也就是认识而已吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1180021577V是这样吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1180021578V他依旧还是独来独往啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '村长幽寂地闭上了眼睛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0101,
        (
            '#0010021579V#501F？？？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010021580V怎么了，村长？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1180021581V啊，不好意思，失礼了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1180021582V那么，各位游击士，\n',
            '到这种偏僻的村庄有什么事呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1180021583V难道说，是为了消灭\n',
            '这附近被通缉的魔兽而来的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1254(): pass

    label('loc_1254')

    ChrTalk(
        0x0102,
        (
            '#0020021584V#010F不是的，其实……\n',
            '我们正在调查\n',
            '失踪定期船的事件。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020021585V听说这里有目击者，\n',
            '所以前来打扰一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1180021586V什么，是说这个啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1180021587V前几天，\n',
            '王国军的士兵已经来调查过了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1180021588V他们把这附近都搜查了一遍，\n',
            '结果还不是两手空空地回去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021589V#000F果然是这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010021590V顺便问一下，那个目击到\n',
            '夜空中飞过的黑影的人是谁啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1180021591V是村里的孩子。\n',
            '一个叫鲁伊的男孩子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1180021592V事件发生的那个晚上，\n',
            '他好像看到了奇怪的影子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1180021593V不过毕竟还是个小孩子……\n',
            '说不定是睡糊涂了梦见的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021594V#002F嗯～是梦吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020021595V#010F总之，\n',
            '还是当面听那个孩子说说比较好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021596V#006F嗯，也对。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010021597V村长，打扰您了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1180021598V没事没事。\n',
            '还有什么事情的话就过来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x01)

    Jump('loc_1576')

    def _loc_152A(): pass

    label('loc_152A')

    ChrTalk(
        0x00FE,
        (
            '鲁伊那小子\n',
            '肯定就在村子里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这个村子很小，\n',
            '应该很快就能找到他的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_1576(): pass

    label('loc_1576')

    Jump('loc_189B')

    def _loc_1579(): pass

    label('loc_1579')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_189B',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x000E, 0x00, 0x10)"),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x000E, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_159A',
    )

    Call(1, 0x0000)

    Jump('loc_189B')

    def _loc_159A(): pass

    label('loc_159A')

    If(
        (
            (Expr.Eval, "OP_29(0x000E, 0x01, 0x0800)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_16D6',
    )

    OP_28(0x000E, 0x01, 0x0800)
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '哦哦，\n',
            '是游击士们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我都听说了，\n',
            '魔兽已经被你们消灭了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯，总算是成功了。\n',
            '它可是个颇强的对手呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '这样一来，\n',
            '我们今年就可以\n',
            '安安心心地种植树苗了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '各位，\n',
            '真的是辛苦你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们这个偏僻的小村，\n',
            '随时都欢迎你们的到来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#001F嗯，谢谢村长爷爷。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_189B')

    def _loc_16D6(): pass

    label('loc_16D6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_1742',
    )

    ChrTalk(
        0x00FE,
        (
            '各位能帮我们消灭魔兽，\n',
            '真的是太感谢你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们这个偏僻的小村，\n',
            '随时都欢迎你们的到来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_189B')

    def _loc_1742(): pass

    label('loc_1742')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1834',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '哦哦，是各位游击士啊。\n',
            '辛苦你们消灭魔兽了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '请进请进，\n',
            '不要客气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，现在村子的这个样子，\n',
            '我想都不敢想……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在１０年前的战争中，\n',
            '这里受到了很大的伤害。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '从战后的情况来看，\n',
            '这里竟然能够\n',
            '复兴到这个地步。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_189B')

    def _loc_1834(): pass

    label('loc_1834')

    ChrTalk(
        0x00FE,
        (
            '从战后的情况来看，\n',
            '这个村子能够走到这步，\n',
            '复兴到这个地步。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这一切都要归功于\n',
            '村民们的努力啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_189B(): pass

    label('loc_189B')

    TalkEnd(0x000A)

    Return()

# id: 0x0007 offset: 0x189F
@scena.Code('func_07_189F')
def func_07_189F():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_1933',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1905',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '唉……\n',
            '这次集会终于结束了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那两个人只要一见面，\n',
            '总会演变成那样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1930')

    def _loc_1905(): pass

    label('loc_1905')

    ChrTalk(
        0x00FE,
        (
            '那两个人只要一见面，\n',
            '总会演变成那样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1930(): pass

    label('loc_1930')

    Jump('loc_1DD7')

    def _loc_1933(): pass

    label('loc_1933')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_1A30',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_19D1',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '虽然很痛苦，\n',
            '但是我们也不能忘记１０年前的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '既为了不再让\n',
            '同样的错误重蹈覆辙……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '也要尽可能让下一代\n',
            '将这件事铭记于心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A2D')

    def _loc_19D1(): pass

    label('loc_19D1')

    ChrTalk(
        0x00FE,
        (
            '虽然很痛苦，\n',
            '但是我们也不能忘记１０年前的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为了不再让\n',
            '同样的错误重蹈覆辙……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A2D(): pass

    label('loc_1A2D')

    Jump('loc_1DD7')

    def _loc_1A30(): pass

    label('loc_1A30')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_1AFD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1AB6',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '看到这些士兵，\n',
            '我就会想起１０年前的事，\n',
            '然后就会感到揪心地痛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是不想见到他们\n',
            '在这个村子进进出出的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AFA')

    def _loc_1AB6(): pass

    label('loc_1AB6')

    ChrTalk(
        0x00FE,
        (
            '看到这些士兵，\n',
            '我就会想起１０年前的事，\n',
            '然后就会感到揪心地痛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1AFA(): pass

    label('loc_1AFA')

    Jump('loc_1DD7')

    def _loc_1AFD(): pass

    label('loc_1AFD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 6, 0x31E)),
            Expr.Return,
        ),
        'loc_1BB9',
    )

    ChrTalk(
        0x00FE,
        (
            '以前矿山很景气的时候，\n',
            '这个村子也非常繁荣。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '到处都是矿工和商人，\n',
            '人多得都可以和大城市相提并论了，\n',
            '村子非常有活力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '自从战争开始到现在，\n',
            '这里已经变得非常冷清了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1DD7')

    def _loc_1BB9(): pass

    label('loc_1BB9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 5, 0x31D)),
            Expr.Return,
        ),
        'loc_1C00',
    )

    ChrTalk(
        0x00FE,
        (
            '在找村长吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '平时这个时候，\n',
            '我想他应该在那里的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1DD7')

    def _loc_1C00(): pass

    label('loc_1C00')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 4, 0x31C)),
            Expr.Return,
        ),
        'loc_1C60',
    )

    ChrTalk(
        0x00FE,
        (
            '我们夫妇每天\n',
            '都会去山岗上扫墓。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '希望能够不使那些\n',
            '当时死去的村民们感到寂寞。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1DD7')

    def _loc_1C60(): pass

    label('loc_1C60')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_1D67',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1D08',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '能将皮肤烤焦的热气，\n',
            '满屋子被烧焦的味道……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '村民们的悲泣声此起彼伏，\n',
            '还有孩子们的哭叫声……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不管过了多久，\n',
            '我都无法忘却这一情景……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D64')

    def _loc_1D08(): pass

    label('loc_1D08')

    ChrTalk(
        0x00FE,
        (
            '说起来那个孩子\n',
            '好久才回来一次啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '跟我说一声的话，\n',
            '我可以早点去那家打扫一下的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1D64(): pass

    label('loc_1D64')

    Jump('loc_1DD7')

    def _loc_1D67(): pass

    label('loc_1D67')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_1DD7',
    )

    ChrTalk(
        0x00FE,
        (
            '这个村的人都是\n',
            '在１０年前的战火中\n',
            '幸存下来的村民。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大家都希望以后能够和睦相处，\n',
            '生活代代安定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1DD7(): pass

    label('loc_1DD7')

    TalkEnd(0x000B)

    Return()

# id: 0x0008 offset: 0x1DDB
@scena.Code('func_08_1DDB')
def func_08_1DDB():
    TalkBegin(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_205E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0071, 6, 0x38E)),
            Expr.Return,
        ),
        'loc_1E3D',
    )

    ChrTalk(
        0x00FE,
        (
            '废坑现在还处在\n',
            '军队的大叔们看管之下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他们好像\n',
            '调查到了很多东西呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_205E')

    def _loc_1E3D(): pass

    label('loc_1E3D')

    ChrTurnDirection(0x00FE, 0x0101, 0)
    SetScenaFlags(ScenaFlag(0x0071, 6, 0x38E))

    ChrTalk(
        0x00FE,
        (
            '啊，是姐姐啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#001F你好啊～鲁伊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那之后，\n',
            '军队就来把姐姐们带走了，\n',
            '把我吓死了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '姐姐们明明\n',
            '什么坏事也没有做啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没什么事吧？\n',
            '他们没有刁难你们吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#506F哎呀呀，\n',
            '让你为我们担心了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#006F没事啦，\n',
            '你看我现在不是很有活力吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，那就好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我所看到的那个，\n',
            '果然是飞艇啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '姐姐， \n',
            '谢谢你为我作证！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#505F嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '不过最后反正会被\n',
            '王国军证明清楚，\n',
            '我的心里还真不是滋味啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '他们还把我们\n',
            '误认为空贼而抓走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F算了，\n',
            '这次虽然有些丢脸，\n',
            '不过我们还是守住了约定……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '这不是挺好吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_205E(): pass

    label('loc_205E')

    TalkEnd(0x000C)

    Return()

# id: 0x0009 offset: 0x2062
@scena.Code('func_09_2062')
def func_09_2062():
    TalkBegin(0x000D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_20AC',
    )

    ChrTalk(
        0x00FE,
        (
            '呼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '种苗的栽插结束了，\n',
            '我也终于可以休息一下了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2510')

    def _loc_20AC(): pass

    label('loc_20AC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_21C9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2157',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '拉文努村果树园\n',
            '是由全体村民来管理的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过呢，\n',
            '最初是由个人进行管理的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '果树栽培非常需要人手，\n',
            '所以我觉得还是\n',
            '全体村民一起来干比较好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_21C6')

    def _loc_2157(): pass

    label('loc_2157')

    ChrTalk(
        0x00FE,
        (
            '拉文努村果树园\n',
            '是由全体村民来管理的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '果树栽培非常需要人手，\n',
            '所以我觉得还是\n',
            '全体村民一起来干比较好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_21C6(): pass

    label('loc_21C6')

    Jump('loc_2510')

    def _loc_21C9(): pass

    label('loc_21C9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_2227',
    )

    ChrTalk(
        0x00FE,
        (
            '鲁伊是在战争结束之后\n',
            '才出生的孩子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我可不想让那孩子\n',
            '经历那种恐怖的体验。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2510')

    def _loc_2227(): pass

    label('loc_2227')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 5, 0x31D)),
            Expr.Return,
        ),
        'loc_226E',
    )

    ChrTalk(
        0x00FE,
        (
            '鲁伊那家伙\n',
            '看起来心情似乎很好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '遇到什么好事了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2510')

    def _loc_226E(): pass

    label('loc_226E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 4, 0x31C)),
            Expr.Return,
        ),
        'loc_235E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_230D',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '鲁伊那家伙\n',
            '好像又在哭了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他说他看见夜空中\n',
            '有黑影在飞也确实有点……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我想他可能是\n',
            '看到动物或是别的什么，\n',
            '于是就误会了吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_235B')

    def _loc_230D(): pass

    label('loc_230D')

    ChrTalk(
        0x00FE,
        (
            '鲁伊那家伙\n',
            '好像又在哭了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他说他看见夜空中\n',
            '有黑影在飞也确实有点……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_235B(): pass

    label('loc_235B')

    Jump('loc_2510')

    def _loc_235E(): pass

    label('loc_235E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_2468',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_241C',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '去看过村里的墓地了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那些墓碑下的人\n',
            '是在百日战役中的牺牲者。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '１０年前的某一天，\n',
            '这里经历了战争的洗礼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '直到今日，\n',
            '我仍然能够在梦中见到那幅惨景。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2465')

    def _loc_241C(): pass

    label('loc_241C')

    ChrTalk(
        0x00FE,
        (
            '去看过村里的墓地了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那些墓碑下的人\n',
            '是在百日战役中的牺牲者。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2465(): pass

    label('loc_2465')

    Jump('loc_2510')

    def _loc_2468(): pass

    label('loc_2468')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_2510',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x000E, 0x00, 0x10)"),
            (Expr.Eval, "OP_29(0x000E, 0x01, 0x1000)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2510',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_24CA',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '呀，辛苦你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我已经向村长\n',
            '说明事情的经过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2510')

    def _loc_24CA(): pass

    label('loc_24CA')

    ChrTalk(
        0x00FE,
        (
            '那么，\n',
            '魔兽也已经被消灭了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '接下来就要\n',
            '开始挑选树苗了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2510(): pass

    label('loc_2510')

    TalkEnd(0x000D)

    Return()

# id: 0x000A offset: 0x2514
@scena.Code('func_0A_2514')
def func_0A_2514():
    TalkBegin(0x000E)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_25AB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_257A',
    )

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x00FE,
        (
            '唉……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果他们两个\n',
            '能够融洽相处的话，\n',
            '我就能够放心地去柏斯城里了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_25AB')

    def _loc_257A(): pass

    label('loc_257A')

    ChrTalk(
        0x00FE,
        (
            '真的很想早点跟\n',
            '在柏斯的老婆和孩子见面呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_25AB(): pass

    label('loc_25AB')

    TalkEnd(0x000E)

    Return()

# id: 0x000B offset: 0x25AF
@scena.Code('func_0B_25AF')
def func_0B_25AF():
    TalkBegin(0x000F)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_268C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2626',
    )

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x00FE,
        (
            '我们当然不是要\n',
            '舍弃口味而增加\n',
            '水果的出货量啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们是主张更加有效地\n',
            '生产美味的水果。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_268C')

    def _loc_2626(): pass

    label('loc_2626')

    ChrTalk(
        0x00FE,
        (
            '为什么他就是\n',
            '不能明白我们的意思呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果能得到库赖爷爷的合作，\n',
            '栽培就能更顺利地进行了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_268C(): pass

    label('loc_268C')

    TalkEnd(0x000F)

    Return()

# id: 0x000C offset: 0x2690
@scena.Code('func_0C_2690')
def func_0C_2690():
    SetScenaFlags(ScenaFlag(0x0063, 6, 0x31E))
    OP_28(0x0036, 0x01, 0x0080)
    ClearMapFlags(0x00000001)
    EventBegin(0x00)
    CameraMove(5700, 0, 48496, 0)
    OP_67(0, 7080, -10000, 0)
    ClearChrFlags(0x000A, 0x0080)
    SetChrFlags(0x0101, 0x0004)
    SetChrFlags(0x0102, 0x0004)
    SetChrFlags(0x0103, 0x0004)
    SetChrFlags(0x000A, 0x0004)
    SetChrFlags(0x000A, 0x0010)
    SetChrChipByIndex(0x000A, 12)
    SetChrSubChip(0x000A, 0)
    OP_4A(0x000A, 255)
    SetChrPos(0x000B, 1450, 0, 41600, 90)
    SetChrPos(0x000A, 5990, 200, 46960, 270)
    SetChrPos(0x0101, 4561, 200, 48200, 180)
    SetChrPos(0x0102, 3391, 200, 48200, 180)
    SetChrPos(0x0103, 4561, 200, 45845, 0)
    SetChrChipByIndex(0x0101, 8)
    SetChrChipByIndex(0x0102, 9)
    SetChrChipByIndex(0x0103, 10)
    SetChrSubChip(0x0101, 1)
    SetChrSubChip(0x0102, 1)
    SetChrSubChip(0x0103, 2)
    FadeIn(2000, 0)
    OP_0D()

    ChrTalk(
        0x000A,
        (
            '#1180021733V#2P嗯，是说那个废坑里\n',
            '可能会有什么线索吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1180021734V#2P……我记得王国军的士兵\n',
            '的确没有调查过废坑的内部。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021735V#000F#1P听了鲁伊那个孩子的话，\n',
            '实在是很在意……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010021736V为了以防万一想要调查一下。\n',
            '能不能把入口的钥匙借给我们呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1180021737V#2P那个挂锁的钥匙吗。\n',
            '你们在这儿稍等一下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(1000)
    SetChrSubChip(0x0101, 0)
    SetChrSubChip(0x0102, 0)
    SetChrSubChip(0x0103, 2)
    SetChrPos(0x000A, 5660, 0, 46450, 180)
    SetChrChipByIndex(0x000A, 2)
    SetChrSubChip(0x000A, 0)
    OP_0D()

    @scena.Lambda('lambda_28D5')
    def lambda_28D5():
        CameraMove(4094, 2000, 41516, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_28D5)

    ChrWalkTo(0x000A, 7994, 0, 43416, 3000, 0x00)
    ClearChrFlags(0x000A, 0x0004)
    ChrWalkTo(0x000A, 7994, 2000, 40098, 3000, 0x00)
    ChrWalkTo(0x000A, 4298, 2000, 40667, 3000, 0x00)
    SetChrDirection(0x000A, 0, 400)

    ChrTalk(
        0x000A,
        (
            '#1180021738V记得是放在抽屉里了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1180021739V噢，找到了，找到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2979')
    def lambda_2979():
        CameraMove(5700, 0, 48496, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_2979)

    ChrWalkTo(0x000A, 7994, 2000, 40098, 3000, 0x00)
    ChrWalkTo(0x000A, 7994, 0, 43416, 3000, 0x00)
    ChrWalkTo(0x000A, 5660, 0, 46450, 3000, 0x00)
    Fade(1000)
    SetChrSubChip(0x0101, 1)
    SetChrSubChip(0x0102, 1)
    SetChrSubChip(0x0103, 2)
    SetChrFlags(0x000A, 0x0004)
    SetChrPos(0x000A, 5990, 200, 46960, 270)
    SetChrChipByIndex(0x000A, 12)
    SetChrSubChip(0x000A, 0)
    TerminateThread(0x000A, 0xFF)
    OP_0D()

    ChrTalk(
        0x000A,
        (
            '#1180021740V#2P给，这就行了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    AddItem(0x032E, 1)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '废坑的钥匙',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0101,
        (
            '#0010021741V#004F#1P哇，好粗糙的钥匙……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010021742V#001F谢谢您，村长！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020021743V#010F#3P真是非常感谢您。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1180021744V#2P哪里哪里，\n',
            '我们总是受到游击士协会的关照。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1180021745V#2P现在帮点忙也是应该的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030021746V#021F呵呵……\n',
            '我们也经常受到\n',
            '像村长这样的好人相助呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020021747V#010F#3P如果发现了什么，\n',
            '我们一定会来向您报告的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1180021748V#2P嗯，那么就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    TerminateThread(0x000A, 0xFF)
    ClearChrFlags(0x0101, 0x0004)
    ClearChrFlags(0x0102, 0x0004)
    ClearChrFlags(0x0103, 0x0004)
    CameraMove(720, 0, 45250, 0)
    OP_67(0, 6150, -10000, 0)
    CameraSetDistance(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrSubChip(0x0101, 0)
    SetChrSubChip(0x0102, 0)
    SetChrSubChip(0x0103, 0)
    SetChrPos(0x0101, 720, 0, 45250, 180)
    SetChrPos(0x0102, 720, 0, 45250, 180)
    SetChrPos(0x0103, 720, 0, 45250, 180)
    SetChrChipByIndex(0x0101, 65535)
    SetChrChipByIndex(0x0103, 65535)
    SetChrChipByIndex(0x0102, 65535)
    OP_69(0x0101, 0)
    SetChrFlags(0x000A, 0x0004)
    SetChrFlags(0x000A, 0x0010)
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
