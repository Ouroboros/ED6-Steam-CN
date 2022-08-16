import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T0610_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0610   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T0610.x'
    header.mapIndex       = 17
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
            word_3A         = 17,
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
        ('ED6_DT07/CH01310._CH', 'ED6_DT07/CH01310P._CP'),
        ('ED6_DT07/CH01300._CH', 'ED6_DT07/CH01300P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH01150._CH', 'ED6_DT07/CH01150P._CP'),
    ]

# id: 0x10001 offset: 0xD2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '罗宾队长',
            x                   = -19380,
            z                   = 0,
            y                   = -980,
            direction           = 98,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '古利乌副长',
            x                   = -111940,
            z                   = 0,
            y                   = 21850,
            direction           = 87,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '士兵安顿',
            x                   = -7220,
            z                   = 0,
            y                   = 2820,
            direction           = 162,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '萨姆',
            x                   = -90130,
            z                   = 0,
            y                   = -22320,
            direction           = 253,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '亚米丽',
            x                   = -57740,
            z                   = 0,
            y                   = -21510,
            direction           = 352,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
    )

# id: 0x10002 offset: 0x172
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x172
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x172
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -7430,
            triggerZ            = 0,
            triggerY            = 900,
            triggerRange        = 1000,
            actorX              = -7220,
            actorZ              = 1500,
            actorY              = 2820,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -109840,
            triggerZ            = 0,
            triggerY            = 21450,
            triggerRange        = 1000,
            actorX              = -111940,
            actorZ              = 1500,
            actorY              = 21850,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0009,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -92220,
            triggerZ            = 0,
            triggerY            = -22040,
            triggerRange        = 1000,
            actorX              = -90130,
            actorZ              = 1500,
            actorY              = -22320,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x1DE
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_1E8',
    )

    Jump('loc_217')

    def _loc_1E8(): pass

    label('loc_1E8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_1F2',
    )

    Jump('loc_217')

    def _loc_1F2(): pass

    label('loc_1F2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_1FC',
    )

    Jump('loc_217')

    def _loc_1FC(): pass

    label('loc_1FC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_206',
    )

    Jump('loc_217')

    def _loc_206(): pass

    label('loc_206')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_210',
    )

    Jump('loc_217')

    def _loc_210(): pass

    label('loc_210')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 6, 0x606)),
            Expr.Return,
        ),
        'loc_217',
    )

    def _loc_217(): pass

    label('loc_217')

    Return()

# id: 0x0001 offset: 0x218
@scena.Code('func_01_218')
def func_01_218():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_227',
    )

    OP_1B(0x00, 0x00, 0x000C)

    Jump('loc_22C')

    def _loc_227(): pass

    label('loc_227')

    OP_1B(0x01, 0x00, 0x000D)

    def _loc_22C(): pass

    label('loc_22C')

    OP_1C(0x05, 0x00, 0x000E)

    Return()

# id: 0x0002 offset: 0x232
@scena.Code('func_02_232')
def func_02_232():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_247',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_232')

    def _loc_247(): pass

    label('loc_247')

    Return()

# id: 0x0003 offset: 0x248
@scena.Code('func_03_248')
def func_03_248():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_26B',
    )

    OP_8D(0x00FE, -22660, -4810, -14730, 1940, 3000)

    Jump('func_03_248')

    def _loc_26B(): pass

    label('loc_26B')

    Return()

# id: 0x0004 offset: 0x26C
@scena.Code('func_04_26C')
def func_04_26C():
    Call(0, 0x0005)

    Return()

# id: 0x0005 offset: 0x271
@scena.Code('func_05_271')
def func_05_271():
    TalkBegin(0x000B)
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
        'loc_2D9',
    )

    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 6, 0x606)),
            Expr.Return,
        ),
        'loc_2D1',
    )

    OP_A9(0x66)

    Jump('loc_2D3')

    def _loc_2D1(): pass

    label('loc_2D1')

    OP_A9(0x64)

    def _loc_2D3(): pass

    label('loc_2D3')

    OP_56(0x00)
    TalkEnd(0x000B)

    Return()

    def _loc_2D9(): pass

    label('loc_2D9')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2EA',
    )

    TalkEnd(0x000B)

    Return()

    def _loc_2EA(): pass

    label('loc_2EA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_33B',
    )

    ChrTalk(
        0x000B,
        (
            '军队里的士兵\n',
            '都以一种很可怕的脸色在谈话呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '发生什么事了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_807')

    def _loc_33B(): pass

    label('loc_33B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_397',
    )

    ChrTalk(
        0x000B,
        (
            '武术大会今天结束了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '诞辰庆典快要举行了，\n',
            '各地的旅客又会\n',
            '开始多起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_807')

    def _loc_397(): pass

    label('loc_397')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_4A1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_40C',
    )

    ChrTalk(
        0x000B,
        (
            '军队的士兵好像都很忙，\n',
            '只有我好空，这也是没办法的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '这里什么娱乐活动都没有，\n',
            '怎么回事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_49E')

    def _loc_40C(): pass

    label('loc_40C')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x000B,
        (
            '呼啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '军队的士兵好像都很忙，\n',
            '只有我好空，这也是没办法的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '大扫除已经\n',
            '完成了大部分了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '没有客人，也没有娱乐。\n',
            '怎么回事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_49E(): pass

    label('loc_49E')

    Jump('loc_807')

    def _loc_4A1(): pass

    label('loc_4A1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_51A',
    )

    ChrTalk(
        0x000B,
        (
            '武术大会的决赛一开始，\n',
            '客人就明显减少。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '今天我想关门大吉，\n',
            '然后跑去王都那里观战，\n',
            '不过我不能这么做。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_807')

    def _loc_51A(): pass

    label('loc_51A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_576',
    )

    ChrTalk(
        0x000B,
        (
            '说起来\n',
            '没想到那支亲卫队竟然是恐怖集团。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '王都那里肯定\n',
            '引起很大的骚动吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_807')

    def _loc_576(): pass

    label('loc_576')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 6, 0x606)),
            Expr.Return,
        ),
        'loc_5D0',
    )

    ChrTalk(
        0x000B,
        (
            '不久之前来的客人\n',
            '都准备去格兰赛尔呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '那么，趁今天有空\n',
            '开始大扫除吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_807')

    def _loc_5D0(): pass

    label('loc_5D0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004D, 0, 0x268)),
            Expr.Return,
        ),
        'loc_630',
    )

    ChrTalk(
        0x000B,
        (
            '突然觉得通过关所的人\n',
            '增加了不少。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '距诞辰庆典还有段日子，\n',
            '发生什么事情了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_807')

    def _loc_630(): pass

    label('loc_630')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004C, 1, 0x261)),
            Expr.Return,
        ),
        'loc_677',
    )

    ChrTalk(
        0x000B,
        (
            '哟，终于来了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '最近客人特别少，\n',
            '我觉得好无聊啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_807')

    def _loc_677(): pass

    label('loc_677')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Return,
        ),
        'loc_6D0',
    )

    ChrTalk(
        0x000B,
        (
            '今天的客人真少啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '就是这种时候，\n',
            '才能搞搞平时无法完成的大扫除啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_807')

    def _loc_6D0(): pass

    label('loc_6D0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 7, 0x24F)),
            Expr.Return,
        ),
        'loc_719',
    )

    ChrTalk(
        0x000B,
        (
            '您好，欢迎光临。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '要住宿的话，\n',
            '过来跟我说一声就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_807')

    def _loc_719(): pass

    label('loc_719')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 1, 0x239)),
            Expr.Return,
        ),
        'loc_78C',
    )

    ChrTalk(
        0x000B,
        (
            '那么，趁今天这个好天气，\n',
            '把被单收集起来洗一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '机会这么难得， \n',
            '我也想让客人睡得舒服一点啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_807')

    def _loc_78C(): pass

    label('loc_78C')

    ChrTalk(
        0x000B,
        (
            '您好，欢迎光临。\n',
            '这里是谁都可以使用的\n',
            '旅行者专用旅馆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '隔壁还有一个食堂。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '觉得不错的话，\n',
            '就在这里住一晚吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_807(): pass

    label('loc_807')

    TalkEnd(0x000B)

    Return()

# id: 0x0006 offset: 0x80B
@scena.Code('func_06_80B')
def func_06_80B():
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

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_869',
    )

    FadeIn(300, 0)
    OP_0D()
    OP_A9(0x65)
    OP_56(0x00)
    TalkEnd(0x000C)

    Return()

    def _loc_869(): pass

    label('loc_869')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_883',
    )

    FadeIn(300, 0)
    TalkEnd(0x000C)

    Return()

    def _loc_883(): pass

    label('loc_883')

    FadeIn(300, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_8EB',
    )

    ChrTalk(
        0x000C,
        (
            '士兵们都\n',
            '慌慌张张的，\n',
            '局势果然很紧张啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '希望能够平安\n',
            '迎来诞辰庆典就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FB1')

    def _loc_8EB(): pass

    label('loc_8EB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_9F1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_962',
    )

    ChrTalk(
        0x000C,
        (
            '虽然我想挑战制作新的菜式，\n',
            '但是又失败了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '唔～顺利的话，我觉得可以\n',
            '往菜单里添加新的菜式了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9EE')

    def _loc_962(): pass

    label('loc_962')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x000C,
        (
            '虽然我想挑战制作新的菜式，\n',
            '但是又失败了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '唔～顺利的话，我觉得可以\n',
            '往菜单里添加新的菜式了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '趁着还有时间，\n',
            '多尝试一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9EE(): pass

    label('loc_9EE')

    Jump('loc_FB1')

    def _loc_9F1(): pass

    label('loc_9F1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_AD1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_A56',
    )

    ChrTalk(
        0x000C,
        (
            '今天都没有什么客人，\n',
            '好寂寞啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '但是，可以有机会\n',
            '一个人享受品茶时光呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_ACE')

    def _loc_A56(): pass

    label('loc_A56')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x000C,
        (
            '今天都没有什么客人，\n',
            '好寂寞啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '但是，可以有机会\n',
            '一个人享受品茶时光呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '今天来挑战一下\n',
            '新的菜式吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_ACE(): pass

    label('loc_ACE')

    Jump('loc_FB1')

    def _loc_AD1(): pass

    label('loc_AD1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_B23',
    )

    ChrTalk(
        0x000C,
        (
            '有时间的话，\n',
            '来烧制一些小点心吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '给繁忙的士兵们\n',
            '送点补品吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FB1')

    def _loc_B23(): pass

    label('loc_B23')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_C17',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_B92',
    )

    ChrTalk(
        0x000C,
        (
            '亲卫队的尤莉亚中尉，\n',
            '身为女性的我也非常仰慕她。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '又帅气，又有礼貌，\n',
            '而且实力非常强。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C14')

    def _loc_B92(): pass

    label('loc_B92')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x000C,
        (
            '亲卫队的尤莉亚中尉，\n',
            '身为女性的我也非常仰慕她。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '又帅气，又有礼貌，\n',
            '而且实力非常强。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '听说她是\n',
            '向老师学习剑术的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C14(): pass

    label('loc_C14')

    Jump('loc_FB1')

    def _loc_C17(): pass

    label('loc_C17')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 6, 0x606)),
            Expr.Return,
        ),
        'loc_CE6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_C7C',
    )

    ChrTalk(
        0x000C,
        (
            '几位客人是从\n',
            '王都那里过来的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '这种时候从格兰赛尔那边\n',
            '过来还真是少见呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CE3')

    def _loc_C7C(): pass

    label('loc_C7C')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x000C,
        (
            '欢迎光临。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '几位客人是从\n',
            '王都那里过来的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '这种时候从格兰赛尔那边\n',
            '过来还真是少见呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_CE3(): pass

    label('loc_CE3')

    Jump('loc_FB1')

    def _loc_CE6(): pass

    label('loc_CE6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004D, 0, 0x268)),
            Expr.Return,
        ),
        'loc_D89',
    )

    ChrTalk(
        0x00FE,
        (
            '最近，除了利贝尔\n',
            '和帝国的料理之外， \n',
            '东方的料理也广受关注呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '下次去王都的时候，\n',
            '也应该买本什么书回来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '会有怎样的料理，\n',
            '我好有兴趣啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FB1')

    def _loc_D89(): pass

    label('loc_D89')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004C, 1, 0x261)),
            Expr.Return,
        ),
        'loc_E12',
    )

    ChrTalk(
        0x00FE,
        (
            '这里的士兵们都非常善良，\n',
            '即使味道不太好，\n',
            '他们也都会说很好吃。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '某种意义上来说我很高兴，\n',
            '但是我也想听听直率的意见……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FB1')

    def _loc_E12(): pass

    label('loc_E12')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Return,
        ),
        'loc_E7B',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，这个时候\n',
            '有点无聊啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '正是这种时候，\n',
            '才应该有效地利用它，\n',
            '好好地配置一下菜单吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FB1')

    def _loc_E7B(): pass

    label('loc_E7B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 7, 0x24F)),
            Expr.Return,
        ),
        'loc_EA9',
    )

    ChrTalk(
        0x00FE,
        (
            '欢迎光临，请问你们想吃点什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FB1')

    def _loc_EA9(): pass

    label('loc_EA9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 1, 0x239)),
            Expr.Return,
        ),
        'loc_F6C',
    )

    ChrTalk(
        0x00FE,
        (
            '煎锅这东西越使用\n',
            '越觉得是一件上乘之品。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '随着烧菜时间的增长，\n',
            '而产生的黑色光泽，\n',
            '让我觉得无比愉快。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对于厨师来说，这就好像是\n',
            '刻入自己年轮的东西，\n',
            '换句话说，就和勋章一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FB1')

    def _loc_F6C(): pass

    label('loc_F6C')

    ChrTalk(
        0x00FE,
        (
            '欢迎光临。\n',
            '欢迎来到格鲁纳门的食堂。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '喜欢吃什么请随便点吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_FB1(): pass

    label('loc_FB1')

    TalkEnd(0x000C)

    Return()

# id: 0x0007 offset: 0xFB5
@scena.Code('func_07_FB5')
def func_07_FB5():
    Call(0, 0x0008)

    Return()

# id: 0x0008 offset: 0xFBA
@scena.Code('func_08_FBA')
def func_08_FBA():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_102E',
    )

    ChrTalk(
        0x000A,
        (
            '现在所有的关所\n',
            '都完全禁止通行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '真抱歉，这也是为了\n',
            '防止正在潜逃的恐怖分子们\n',
            '有不轨的行动啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1781')

    def _loc_102E(): pass

    label('loc_102E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_1123',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_10A2',
    )

    ChrTalk(
        0x000A,
        (
            '情报部的士兵们\n',
            '和亲卫队不同，\n',
            '态度是非常威严傲慢的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '唉，真不知道\n',
            '到底哪边才是恐怖分子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1120')

    def _loc_10A2(): pass

    label('loc_10A2')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x000A,
        (
            '情报部的士兵们\n',
            '好像巡逻回来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '和亲卫队不同，\n',
            '态度是非常威严傲慢的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '唉，真不知道\n',
            '到底哪边才是恐怖分子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1120(): pass

    label('loc_1120')

    Jump('loc_1781')

    def _loc_1123(): pass

    label('loc_1123')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_11BA',
    )

    ChrTalk(
        0x000A,
        (
            '从今天开始， \n',
            '如果通行者没有可以证明\n',
            '自己身份的东西，就无法通过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '对不起，如果要通过的话，\n',
            '请出示能够证明身份的书信\n',
            '或者其他物品。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1781')

    def _loc_11BA(): pass

    label('loc_11BA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_124C',
    )

    ChrTalk(
        0x000A,
        (
            '我想你们一眼就能看出来了，\n',
            '这座门是利用亚宁堡的一部分\n',
            '制作而成的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '虽然能感受到历史的氛围\n',
            '和它的万种风情，\n',
            '但也带了许多不便。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1781')

    def _loc_124C(): pass

    label('loc_124C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_12CA',
    )

    ChrTalk(
        0x000A,
        (
            '这座门的通行者没有对面的\n',
            '圣海姆门的人多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '只有像举办武术大会或者诞辰庆典\n',
            '这样的活动时通行的人才会多起来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1781')

    def _loc_12CA(): pass

    label('loc_12CA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 6, 0x606)),
            Expr.Return,
        ),
        'loc_1320',
    )

    ChrTalk(
        0x000A,
        (
            '咦……\n',
            '你们是旅行者吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '武术大会的时候基本没有\n',
            '什么人来洛连特的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1781')

    def _loc_1320(): pass

    label('loc_1320')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004D, 0, 0x268)),
            Expr.Return,
        ),
        'loc_13B1',
    )

    ChrTalk(
        0x000A,
        (
            '定期船停航的话，\n',
            '从这里通过的人多了不少。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '因为急事要去王都的人，\n',
            '只能从这个关所通过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '好像又回到没有\n',
            '飞艇的时代了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1781')

    def _loc_13B1(): pass

    label('loc_13B1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004C, 1, 0x261)),
            Expr.Return,
        ),
        'loc_1422',
    )

    ChrTalk(
        0x000A,
        (
            '神秘森林就在\n',
            '比这边还要北一点的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '从街道向东走，\n',
            '会有一条小道，\n',
            '走的时候可不要错过了呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1781')

    def _loc_1422(): pass

    label('loc_1422')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Return,
        ),
        'loc_1482',
    )

    ChrTalk(
        0x000A,
        (
            '北方的神秘森林\n',
            '是洛连特林业的中心地带。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '那里的工作人员\n',
            '有时候会来这里休息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1781')

    def _loc_1482(): pass

    label('loc_1482')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 7, 0x24F)),
            Expr.Return,
        ),
        'loc_157F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1522',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x000A,
        (
            '听说游击士可以自己\n',
            '选择所属的支部？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '真好啊，我们士兵\n',
            '可没有选择工作地点的权利。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '不过，如果可以这样的话，\n',
            '或许会变得很糟糕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_157C')

    def _loc_1522(): pass

    label('loc_1522')

    ChrTalk(
        0x000A,
        (
            '听说游击士可以自己\n',
            '选择所属的支部？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '真好啊，我们士兵\n',
            '可没有选择工作地点的权利。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_157C(): pass

    label('loc_157C')

    Jump('loc_1781')

    def _loc_157F(): pass

    label('loc_157F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 1, 0x239)),
            Expr.Return,
        ),
        'loc_1633',
    )

    ChrTalk(
        0x000A,
        (
            '王国的各个地方边境\n',
            '肯定会有像这样的关所。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '百日战役以来，\n',
            '检查要出入各个地区的人\n',
            '也是为了地区的安全和稳定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '就是和在飞艇坪买票的时候\n',
            '需要身份证明是一样的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1781')

    def _loc_1633(): pass

    label('loc_1633')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_170E',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x000A,
        (
            '啊呀，难道你们\n',
            '要去格兰赛尔？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊，不是的。\n',
            '我们并没有这个打算……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '是这样啊。\n',
            '最近来往于洛连特和王都\n',
            '之间的定期船已经成为主流。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '像以前一样步行前来\n',
            '通过关所的旅行者\n',
            '已经很少很少了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1781')

    def _loc_170E(): pass

    label('loc_170E')

    ChrTalk(
        0x000A,
        (
            '最近来往于洛连特和王都\n',
            '之间的定期船已经成为主流。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '像以前一样步行前来\n',
            '通过关所的旅行者\n',
            '已经少了很多了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1781(): pass

    label('loc_1781')

    TalkEnd(0x000A)

    Return()

# id: 0x0009 offset: 0x1785
@scena.Code('func_09_1785')
def func_09_1785():
    Call(0, 0x000A)

    Return()

# id: 0x000A offset: 0x178A
@scena.Code('func_0A_178A')
def func_0A_178A():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_1807',
    )

    ChrTalk(
        0x0009,
        (
            '昨天， \n',
            '本部传来通告， \n',
            '要求完全封锁关所。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '真是非常抱歉，\n',
            '除军队相关人员之外，\n',
            '连一只猫都不能放进去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E83')

    def _loc_1807(): pass

    label('loc_1807')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_1854',
    )

    ChrTalk(
        0x0009,
        (
            '今天武术大会就结束了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '我想王城那边\n',
            '也该有新的行动了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E83')

    def _loc_1854(): pass

    label('loc_1854')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_18BE',
    )

    ChrTalk(
        0x0009,
        (
            '今天开始，警戒体制的等级\n',
            '向上提升一级了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '要将通行者的身份完全\n',
            '确认之后，才能放行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E83')

    def _loc_18BE(): pass

    label('loc_18BE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_19D8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1939',
    )

    ChrTalk(
        0x0009,
        (
            '利贝尔王国的交通\n',
            '现在是以定期船为主要工具。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '航空被封锁之后，\n',
            '旅客和货物的通行就变得非常困难了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19D5')

    def _loc_1939(): pass

    label('loc_1939')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x0009,
        (
            '王国军的管制\n',
            '给人们带来了许多不便。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '利贝尔王国的交通\n',
            '现在是以定期船为主要工具。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '果然，航空被封锁之后，\n',
            '旅客和货物的通行就变得非常困难了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_19D5(): pass

    label('loc_19D5')

    Jump('loc_1E83')

    def _loc_19D8(): pass

    label('loc_19D8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_1A53',
    )

    ChrTalk(
        0x0009,
        (
            '我在演习的时候\n',
            '见过亲卫队的成员，\n',
            '他们作为守护陛下的人真的很称职。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '没想到竟然是他们\n',
            '引起的恐怖事件……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E83')

    def _loc_1A53(): pass

    label('loc_1A53')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 6, 0x606)),
            Expr.Return,
        ),
        'loc_1B1E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1AAD',
    )

    ChrTalk(
        0x0009,
        (
            '我记得圣海姆门那里\n',
            '好像刚刚征召了一些新兵。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '那边一定很辛苦吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B1B')

    def _loc_1AAD(): pass

    label('loc_1AAD')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x0009,
        (
            '因为现在处于警戒状态，\n',
            '全队的演习全部中止了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '这座格鲁纳门\n',
            '聚集了许多老兵，\n',
            '没有什么可以担心的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1B1B(): pass

    label('loc_1B1B')

    Jump('loc_1E83')

    def _loc_1B1E(): pass

    label('loc_1B1E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004D, 0, 0x268)),
            Expr.Return,
        ),
        'loc_1BE3',
    )

    ChrTalk(
        0x0009,
        (
            '柏斯那边的定期船\n',
            '好像消失了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '我好担心飞艇上的乘客，\n',
            '希望他们平安无事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '不过，在柏斯地区\n',
            '也有一支聚集了王国军中\n',
            '很多精英的国境守备队。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '我想他们一定能够\n',
            '把飞艇找出来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E83')

    def _loc_1BE3(): pass

    label('loc_1BE3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004C, 1, 0x261)),
            Expr.Return,
        ),
        'loc_1C85',
    )

    ChrTalk(
        0x0009,
        (
            '那么……\n',
            '今天一天也要加油。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '只有在和平的时候才应该\n',
            '随时待命，以备不时之需。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '这句话是队长说的，\n',
            '虽然我是现学现卖，\n',
            '不过觉得这话说得真好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E83')

    def _loc_1C85(): pass

    label('loc_1C85')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Return,
        ),
        'loc_1CEF',
    )

    ChrTalk(
        0x0009,
        (
            '百日战役结束以来，\n',
            '今年是第１０个年头了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '看着现在和平的王国，\n',
            '就想到很久以前的光景。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E83')

    def _loc_1CEF(): pass

    label('loc_1CEF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 7, 0x24F)),
            Expr.Return,
        ),
        'loc_1D94',
    )

    ChrTalk(
        0x0009,
        (
            '洛连特市长\n',
            '来过这里实地视察，\n',
            '他真是个好人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '市长让人感觉很亲切，\n',
            '就像是隔壁家的老爷爷。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '他对待市民也\n',
            '非常和蔼可亲，\n',
            '那样的话一定很得民心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E83')

    def _loc_1D94(): pass

    label('loc_1D94')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 1, 0x239)),
            Expr.Return,
        ),
        'loc_1E19',
    )

    ChrTalk(
        0x0009,
        (
            '最近，在王都\n',
            '聚集了许多喜爱钓鱼的人，\n',
            '好像已经形成了组织。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '我也非常喜欢钓鱼，\n',
            '所以对那是个怎样的组织非常有兴趣。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E83')

    def _loc_1E19(): pass

    label('loc_1E19')

    ChrTalk(
        0x0009,
        (
            '哟，你们好。\n',
            '是来观光，还是来做其他事情的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '这里的设施任何人都可以使用，\n',
            '你们可以好好休息一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1E83(): pass

    label('loc_1E83')

    TalkEnd(0x0009)

    Return()

# id: 0x000B offset: 0x1E87
@scena.Code('func_0B_1E87')
def func_0B_1E87():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_1F11',
    )

    ChrTalk(
        0x00FE,
        (
            '终于，各关所被完全封锁，\n',
            '定期船也全都停止航行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就算是理查德上校，\n',
            '没有女王陛下的许可\n',
            '就这样做，到底行不行啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2608')

    def _loc_1F11(): pass

    label('loc_1F11')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_1F8E',
    )

    ChrTalk(
        0x00FE,
        (
            '传闻中，自称是游击士的\n',
            '恐怖分子相当厉害。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一对一恐怕无法取胜，\n',
            '所以要考虑一下\n',
            '把现在警备体制联合起来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2608')

    def _loc_1F8E(): pass

    label('loc_1F8E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_20BC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_2017',
    )

    ChrTalk(
        0x00FE,
        (
            '听说在蔡斯出现的\n',
            '恐怖分子们穿着\n',
            '亲卫队的制服。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '即使假设犯人是亲卫队，\n',
            '他们为什么要在犯案时\n',
            '特地穿着制服呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_20B9')

    def _loc_2017(): pass

    label('loc_2017')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '听说在蔡斯出现的\n',
            '恐怖分子们穿着\n',
            '亲卫队的制服。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '亲卫队集中了王国军中\n',
            '最优秀的人才。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '即使假设他们是犯人，\n',
            '他们为什么要在犯案时\n',
            '特地穿着制服呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_20B9(): pass

    label('loc_20B9')

    Jump('loc_2608')

    def _loc_20BC(): pass

    label('loc_20BC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_21DD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_212B',
    )

    ChrTalk(
        0x00FE,
        (
            '现在洛连特地区\n',
            '也没有发生什么重大事件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，为了以防万一，\n',
            '应该随时处于出动状态。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_21DA')

    def _loc_212B(): pass

    label('loc_212B')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '游击士协会的洛连特支部中\n',
            '好像有一位非常能干的女性游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为了以防万一，\n',
            '现在洛连特地区\n',
            '也没有发生什么重大事件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，为了以防万一，\n',
            '应该随时处于出动状态。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_21DA(): pass

    label('loc_21DA')

    Jump('loc_2608')

    def _loc_21DD(): pass

    label('loc_21DD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_227C',
    )

    ChrTalk(
        0x00FE,
        (
            '有报告说是这次的恐怖事件\n',
            '是亲卫队干的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '也听说是恐怖分子装扮成\n',
            '亲卫队和游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '到底哪个是真的呢。\n',
            '真希望能够尽早得到正确的情报啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2608')

    def _loc_227C(): pass

    label('loc_227C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 6, 0x606)),
            Expr.Return,
        ),
        'loc_22EF',
    )

    ChrTalk(
        0x00FE,
        (
            '军队在全国\n',
            '都采取这样的警备状态\n',
            '还是百日战役以来的第一次啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……我想起了\n',
            '那个时候的许多事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2608')

    def _loc_22EF(): pass

    label('loc_22EF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004D, 0, 0x268)),
            Expr.Return,
        ),
        'loc_2383',
    )

    ChrTalk(
        0x00FE,
        (
            '神秘森林上空\n',
            '有奇怪的飞艇飞来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '调查的结果也显示， \n',
            '过去曾有好几次起飞降落的形迹。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要赶快向雷斯顿要塞总部\n',
            '报告这件事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2608')

    def _loc_2383(): pass

    label('loc_2383')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004C, 1, 0x261)),
            Expr.Return,
        ),
        'loc_2427',
    )

    ChrTalk(
        0x00FE,
        (
            '洛连特原本\n',
            '是不太会发生什么大事的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，即使这么说，\n',
            '我们也不能保证\n',
            '今后不会发生什么大事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不管地区的守备多么坚固，\n',
            '也不能放松警惕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2608')

    def _loc_2427(): pass

    label('loc_2427')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Return,
        ),
        'loc_24BA',
    )

    ChrTalk(
        0x00FE,
        (
            '今天也没有\n',
            '发生什么大事件呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然和平是件好事，\n',
            '但正是这样才应该防患于未然，\n',
            '要认真进行演习才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为这是我们的工作啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2608')

    def _loc_24BA(): pass

    label('loc_24BA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 7, 0x24F)),
            Expr.Return,
        ),
        'loc_254D',
    )

    ChrTalk(
        0x00FE,
        (
            '正因为这个\n',
            '关所通向王都，\n',
            '所以都分配了经验丰富的老兵。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '威尔特桥的关所却相反，\n',
            '分配的全都是新兵……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '阿斯顿队长没问题吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2608')

    def _loc_254D(): pass

    label('loc_254D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 1, 0x239)),
            Expr.Return,
        ),
        'loc_25B6',
    )

    ChrTalk(
        0x00FE,
        (
            '在王都，为女王陛下的诞辰庆典\n',
            '所做的准备正在有条不紊地进行中。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我从现在开始就很期待。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2608')

    def _loc_25B6(): pass

    label('loc_25B6')

    ChrTalk(
        0x00FE,
        (
            '哟，你们是游击士吗。\n',
            '你们也辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果发生什么事件，\n',
            '我们互相帮助吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2608(): pass

    label('loc_2608')

    TalkEnd(0x00FE)

    Return()

# id: 0x000C offset: 0x260C
@scena.Code('func_0C_260C')
def func_0C_260C():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_27A8',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_269E',
    )

    ChrTurnDirection(0x0102, 0x0101, 400)

    @scena.Lambda('lambda_2637')
    def lambda_2637():
        ChrTurnDirection(0x0101, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_2637)

    ChrTalk(
        0x0102,
        (
            '#0020141710V#010F这边是洛连特吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141711V要回去的话…………\n',
            '现在这个时候还不行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_278D')

    def _loc_269E(): pass

    label('loc_269E')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2722',
    )

    ChrTalk(
        0x0104,
        (
            '#0040141712V#030F哦，\n',
            '这边不就是令人怀念的洛连特吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040141713V虽然我还想再去拜访一下，\n',
            '不过现在还不是时候。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_278D')

    def _loc_2722(): pass

    label('loc_2722')

    ChrTalk(
        0x0108,
        (
            '#0080141714V#070F哦，\n',
            '这边是通往其他地区的出口。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080100536V被士兵缠上就麻烦了。\n',
            '还是乖乖地回去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_278D(): pass

    label('loc_278D')

    ChrMoveToRelative(0x0000, -1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_27A8(): pass

    label('loc_27A8')

    Return()

# id: 0x000D offset: 0x27A9
@scena.Code('func_0D_27A9')
def func_0D_27A9():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2A26',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_28C9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_284D',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    ChrTurnDirection(0x0102, 0x0101, 400)

    @scena.Lambda('lambda_27E0')
    def lambda_27E0():
        ChrTurnDirection(0x0101, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_27E0)

    ChrTalk(
        0x0102,
        (
            '#0020020248V#010F这边是格兰赛尔地区呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020020249V我们没有通行许可证，\n',
            '是不能通过这里的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_28C6')

    def _loc_284D(): pass

    label('loc_284D')

    ChrTurnDirection(0x0102, 0x0101, 400)

    @scena.Lambda('lambda_285A')
    def lambda_285A():
        ChrTurnDirection(0x0101, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_285A)

    ChrTalk(
        0x0102,
        (
            '#0020020250V#010F前面就是格兰赛尔地区了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020020251V我们没有通行许可证，\n',
            '是不能通过这里的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_28C6(): pass

    label('loc_28C6')

    Jump('loc_2A0B')

    def _loc_28C9(): pass

    label('loc_28C9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 0, 0x300)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2967',
    )

    ChrTurnDirection(0x0103, 0x0101, 400)

    @scena.Lambda('lambda_28DE')
    def lambda_28DE():
        ChrTurnDirection(0x0102, 0x0103, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_28DE)

    @scena.Lambda('lambda_28EC')
    def lambda_28EC():
        ChrTurnDirection(0x0101, 0x0103, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_28EC)

    ChrTalk(
        0x0103,
        (
            '#0030020252V#020F前面就是格兰赛尔地区了。\n',
            '要通过关所就需要许可证。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030020253V不过，现在也没有去的必要。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A0B')

    def _loc_2967(): pass

    label('loc_2967')

    ChrTurnDirection(0x0103, 0x0101, 400)

    @scena.Lambda('lambda_2974')
    def lambda_2974():
        ChrTurnDirection(0x0102, 0x0103, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_2974)

    @scena.Lambda('lambda_2982')
    def lambda_2982():
        ChrTurnDirection(0x0101, 0x0103, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_2982)

    ChrTalk(
        0x0103,
        (
            '#0030020254V#020F前面就是格兰赛尔地区了。\n',
            '要通过关所就需要许可证。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030020255V我们要去的威尔特桥也和这里一样，\n',
            '要注意啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2A0B(): pass

    label('loc_2A0B')

    ChrMoveToRelative(0x0000, 1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_2A26(): pass

    label('loc_2A26')

    Return()

# id: 0x000E offset: 0x2A27
@scena.Code('func_0E_2A27')
def func_0E_2A27():
    TalkBegin(0x00FF)
    Sleep(400)

    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
