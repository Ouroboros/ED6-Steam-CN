import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T0600_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0600   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T0600.x'
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
        ('ED6_DT07/CH01300P._CP', 'ED6_DT07/CH01300P._CP'),
    ]

# id: 0x10001 offset: 0xC2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '士兵舒托尔',
            x                   = -35300,
            z                   = 0,
            y                   = 3650,
            direction           = 261,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '士兵巴兰克',
            x                   = -35300,
            z                   = 0,
            y                   = -3560,
            direction           = 265,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '士兵托马斯',
            x                   = -21590,
            z                   = 11750,
            y                   = 150,
            direction           = 101,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '士兵亚多罗瓦',
            x                   = -10690,
            z                   = 0,
            y                   = -3640,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '士兵洛克思',
            x                   = -10660,
            z                   = 0,
            y                   = 3600,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '艾利兹街道方向',
            x                   = 37180,
            z                   = 0,
            y                   = -1450,
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
            name                = '庭园大道方向',
            x                   = -83430,
            z                   = 0,
            y                   = -1170,
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
    )

# id: 0x0000 offset: 0x1A2
@scena.Code('Init')
def Init():
    Return()

# id: 0x0001 offset: 0x1A3
@scena.Code('func_01_1A3')
def func_01_1A3():
    OP_16(0x02, 4000, -150000, -130000, 196614)
    OP_6F(0x0000, 160)
    OP_6F(0x0001, 160)
    OP_72(0x0000, 0x0010)
    OP_72(0x0001, 0x0010)
    OP_1C(0x02, 0x00, 0x0009)
    OP_1C(0x03, 0x00, 0x0009)
    OP_1C(0x04, 0x00, 0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_1E6',
    )

    Jump('loc_215')

    def _loc_1E6(): pass

    label('loc_1E6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_1F0',
    )

    Jump('loc_215')

    def _loc_1F0(): pass

    label('loc_1F0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_1FA',
    )

    Jump('loc_215')

    def _loc_1FA(): pass

    label('loc_1FA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_204',
    )

    Jump('loc_215')

    def _loc_204(): pass

    label('loc_204')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_20E',
    )

    Jump('loc_215')

    def _loc_20E(): pass

    label('loc_20E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 6, 0x606)),
            Expr.Return,
        ),
        'loc_215',
    )

    def _loc_215(): pass

    label('loc_215')

    Return()

# id: 0x0002 offset: 0x216
@scena.Code('func_02_216')
def func_02_216():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_22B',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_216')

    def _loc_22B(): pass

    label('loc_22B')

    Return()

# id: 0x0003 offset: 0x22C
@scena.Code('func_03_22C')
def func_03_22C():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_24F',
    )

    OP_8D(0x00FE, -28070, -8920, -16500, 6400, 3000)

    Jump('func_03_22C')

    def _loc_24F(): pass

    label('loc_24F')

    Return()

# id: 0x0004 offset: 0x250
@scena.Code('func_04_250')
def func_04_250():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_2D4',
    )

    ChrTalk(
        0x00FE,
        (
            '塞维安那家伙，\n',
            '说什么在执勤的时候\n',
            '看到了一个女孩子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过也真是的， \n',
            '他很久没见到女儿，\n',
            '是不是产生幻觉了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_983')

    def _loc_2D4(): pass

    label('loc_2D4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_334',
    )

    ChrTalk(
        0x00FE,
        (
            '这一带还真是平静啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '从这里眺望远景，\n',
            '真是难以想象\n',
            '这个国家会发生恐怖事件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_983')

    def _loc_334(): pass

    label('loc_334')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_3B3',
    )

    ChrTalk(
        0x00FE,
        (
            '昨天我看见有军用艇\n',
            '从洛连特那边飞向王都。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那个时间本应该是\n',
            '定期船通行的时段，\n',
            '是不是发生什么紧急事件了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_983')

    def _loc_3B3(): pass

    label('loc_3B3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_4CB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_42B',
    )

    ChrTalk(
        0x00FE,
        (
            '说起来，\n',
            '之前我在周游道看到了一只白隼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '白隼是\n',
            '利贝尔王国的国徽，\n',
            '据说看到的人就会有好运气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4C8')

    def _loc_42B(): pass

    label('loc_42B')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '说起来，\n',
            '之前我在周游道看到了一只白隼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '白隼是\n',
            '利贝尔王国的国徽，\n',
            '据说看到的人就会有好运气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '希望诞辰庆典和武术大会\n',
            '能够平安无事地结束……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4C8(): pass

    label('loc_4C8')

    Jump('loc_983')

    def _loc_4CB(): pass

    label('loc_4CB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_54E',
    )

    ChrTalk(
        0x00FE,
        (
            '刚才有一架定期船\n',
            '从格鲁纳门上空通过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然为了盘查恐怖人员\n',
            '定期船被迫停航了一段时间，\n',
            '不过最后还是恢复正常了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_983')

    def _loc_54E(): pass

    label('loc_54E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 6, 0x606)),
            Expr.Return,
        ),
        'loc_606',
    )

    ChrTalk(
        0x00FE,
        (
            '今天的天气也很不错呢。\n',
            '连湖对岸的古罗尼连峰\n',
            '也能看得清清楚楚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '利贝尔王国的正中央\n',
            '有一个瓦雷利亚湖对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '湖的四面环山傍海，\n',
            '不管从哪个角度看，风景都十分迷人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_983')

    def _loc_606(): pass

    label('loc_606')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004D, 0, 0x268)),
            Expr.Return,
        ),
        'loc_677',
    )

    ChrTalk(
        0x00FE,
        (
            '我看到神秘森林那边\n',
            '有奇怪的飞艇起飞。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '向队长报告了以后， \n',
            '他脸色一变，然后就开始思考着什么。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_983')

    def _loc_677(): pass

    label('loc_677')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004C, 1, 0x261)),
            Expr.Return,
        ),
        'loc_6F1',
    )

    ChrTalk(
        0x00FE,
        (
            '好，今天也没有什么异常。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然战争已经结束了１０年了，\n',
            '只要一想起那时的状况，\n',
            '就不能放松对这里的警戒。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_983')

    def _loc_6F1(): pass

    label('loc_6F1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Return,
        ),
        'loc_78D',
    )

    ChrTalk(
        0x00FE,
        (
            '我觉得我们的队长\n',
            '是个非常率直的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是他总是\n',
            '为各种事情操心，\n',
            '难道他不累吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要调集兵力也很不容易啊。\n',
            '至少要加紧脚步行动才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_983')

    def _loc_78D(): pass

    label('loc_78D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 7, 0x24F)),
            Expr.Return,
        ),
        'loc_858',
    )

    ChrTalk(
        0x00FE,
        (
            '每一个关所\n',
            '都至少要配备\n',
            '一个守备队的警备力量才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然通过关所的人减少了，\n',
            '但是自从百日战役结束以来，\n',
            '也就一直像现在这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然战争结束了，\n',
            '但并不意味着帝国的威胁就这样消失了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_983')

    def _loc_858(): pass

    label('loc_858')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 1, 0x239)),
            Expr.Return,
        ),
        'loc_91D',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯，今天也没有什么异常。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我肚子也饿了，\n',
            '报告一下之后就去食堂吃饭吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为食堂的店主喜欢新鲜事物，\n',
            '所以那里的菜单经常换来换去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，我可不是说\n',
            '所有的饭菜都非常好吃。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_983')

    def _loc_91D(): pass

    label('loc_91D')

    ChrTalk(
        0x00FE,
        (
            '啊呀，没想到你们能来到这里。\n',
            '中途有没有迷路啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这栋建筑物的内部\n',
            '要比从外面看起来的复杂哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_983(): pass

    label('loc_983')

    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0x987
@scena.Code('func_05_987')
def func_05_987():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_A7A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_9F1',
    )

    ChrTalk(
        0x00FE,
        (
            '昨天开始王国各地的关所\n',
            '都已经被完全封锁了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在一切通行手续\n',
            '都无法办理呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A77')

    def _loc_9F1(): pass

    label('loc_9F1')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '欢迎来到格鲁纳门。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……虽然我想这么说，\n',
            '昨天开始王国各地的关所\n',
            '都已经被完全封锁了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在一切通行手续\n',
            '都无法办理呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A77(): pass

    label('loc_A77')

    Jump('loc_C2C')

    def _loc_A7A(): pass

    label('loc_A7A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_AD9',
    )

    ChrTalk(
        0x00FE,
        (
            '武术大会今天就结束了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，在恐怖分子被抓到之前，\n',
            '我们是不会掉以轻心的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C2C')

    def _loc_AD9(): pass

    label('loc_AD9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_B35',
    )

    ChrTalk(
        0x00FE,
        (
            '上头下达命令\n',
            '要求我们加强警备。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '通行证的发行\n',
            '从今天起也开始变得严格了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C2C')

    def _loc_B35(): pass

    label('loc_B35')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_B84',
    )

    ChrTalk(
        0x00FE,
        (
            '我记得武术大会的正式赛\n',
            '就是从今天开始吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今年谁会取胜呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C2C')

    def _loc_B84(): pass

    label('loc_B84')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_BE2',
    )

    ChrTalk(
        0x00FE,
        (
            '中央工房受到袭击，\n',
            '这可不是一件小事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '柏斯和卢安的事件\n',
            '才刚告一个段落……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C2C')

    def _loc_BE2(): pass

    label('loc_BE2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 6, 0x606)),
            Expr.Return,
        ),
        'loc_C2C',
    )

    ChrTalk(
        0x00FE,
        (
            '这里是格鲁纳门。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是连接格兰赛尔地区\n',
            '和洛连特地区的关所。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C2C(): pass

    label('loc_C2C')

    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0xC30
@scena.Code('func_06_C30')
def func_06_C30():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_CBD',
    )

    ChrTalk(
        0x00FE,
        (
            '听说王城里\n',
            '举办了宫廷晚宴，\n',
            '女王陛下是不是也出席了呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '关于生病和诞辰庆典的事情，\n',
            '还是应该正式对外\n',
            '宣告一下比较好呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FF2')

    def _loc_CBD(): pass

    label('loc_CBD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_D32',
    )

    ChrTalk(
        0x00FE,
        (
            '最近这几天，\n',
            '经常能在这附近\n',
            '看到情报部的特务部队。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在诞辰庆典前还抓不到恐怖分子，\n',
            '真让人不安啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FF2')

    def _loc_D32(): pass

    label('loc_D32')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_D7B',
    )

    ChrTalk(
        0x00FE,
        (
            '没有异常！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这里现在还没有出现\n',
            '亲卫队或者是可疑人物。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FF2')

    def _loc_D7B(): pass

    label('loc_D7B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_DF0',
    )

    ChrTalk(
        0x00FE,
        (
            '听说亲卫队犯了叛逆罪，\n',
            '我可是吓了一跳呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是任务就是任务。\n',
            '如果和他们遇上，\n',
            '也就不得不出手了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FF2')

    def _loc_DF0(): pass

    label('loc_DF0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_E7C',
    )

    ChrTalk(
        0x00FE,
        (
            '出于恐怖分子的原因，\n',
            '那位摩尔根将军\n',
            '终于要开始行动了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只要理查德上校\n',
            '和摩尔根将军齐上阵，\n',
            '解决这个事件只是时间的问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FF2')

    def _loc_E7C(): pass

    label('loc_E7C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 6, 0x606)),
            Expr.Return,
        ),
        'loc_FF2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_F3B',
    )

    ChrTalk(
        0x00FE,
        (
            '这条艾尔贝周游道\n',
            '是围绕王都地区一周的街道。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '庭园大道和艾尔贝周游道\n',
            '是围绕王都地区一周的街道。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以经常会有人没看清楚\n',
            '哪条路去王都更近一点，\n',
            '而绕了一个大圈子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FF2')

    def _loc_F3B(): pass

    label('loc_F3B')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '庭园大道和艾尔贝周游道\n',
            '是围绕王都地区一周的街道。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以经常会有人没有看清楚\n',
            '哪条路去王都更近一点，\n',
            '而绕了一个大圈子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '以前就有一个戴着眼镜的\n',
            '奇怪的姑娘绕了一整圈呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_FF2(): pass

    label('loc_FF2')

    TalkEnd(0x00FE)

    Return()

# id: 0x0007 offset: 0xFF6
@scena.Code('func_07_FF6')
def func_07_FF6():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004D, 0, 0x268)),
            Expr.Return,
        ),
        'loc_1091',
    )

    ChrTalk(
        0x00FE,
        (
            '什么，你们要去柏斯？\n',
            '那么，可不是往这边走哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '应该回到洛连特从城的西门出发，\n',
            '然后向威尔特桥那边走。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是朝着帕赛尔农场的方向哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1376')

    def _loc_1091(): pass

    label('loc_1091')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004C, 1, 0x261)),
            Expr.Return,
        ),
        'loc_10F2',
    )

    ChrTalk(
        0x00FE,
        (
            '最近，有报告说\n',
            '在神秘森林附近看见奇怪的人影。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们在通过街道的时候要小心点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1376')

    def _loc_10F2(): pass

    label('loc_10F2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Return,
        ),
        'loc_1170',
    )

    ChrTalk(
        0x00FE,
        (
            '自从定期船开始运航以来，\n',
            '从这里通行的人就大大减少了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这种时期，来这里的人\n',
            '大多都是来游览这座长城的旅客。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1376')

    def _loc_1170(): pass

    label('loc_1170')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 7, 0x24F)),
            Expr.Return,
        ),
        'loc_11D8',
    )

    ChrTalk(
        0x00FE,
        (
            '如今的王国军有一位\n',
            '虽然年轻但非常了不起的上校。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在普通士兵之间，\n',
            '他也非常受欢迎呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1376')

    def _loc_11D8(): pass

    label('loc_11D8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 1, 0x239)),
            Expr.Return,
        ),
        'loc_1260',
    )

    ChrTalk(
        0x00FE,
        (
            '百日战役的时候，\n',
            '多亏了这个亚宁堡，\n',
            '才让王都免于被帝国军侵占。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '占领了四个城市的帝国军\n',
            '也对这座长城\n',
            '感到无从下手呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1376')

    def _loc_1260(): pass

    label('loc_1260')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_12C4',
    )

    ChrTalk(
        0x00FE,
        (
            '这座巨大的长城\n',
            '被称为『亚宁堡』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '它是围绕隔壁的格兰赛尔地区\n',
            '而建造起来的城墙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1376')

    def _loc_12C4(): pass

    label('loc_12C4')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '这座巨大的长城\n',
            '被称为『亚宁堡』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '它是围绕隔壁的格兰赛尔地区\n',
            '而建造起来的城墙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '据说它在利贝尔王国\n',
            '建国之前就已经存在了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是什么人为了什么原因建起来的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1376(): pass

    label('loc_1376')

    TalkEnd(0x00FE)

    Return()

# id: 0x0008 offset: 0x137A
@scena.Code('func_08_137A')
def func_08_137A():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004D, 0, 0x268)),
            Expr.Return,
        ),
        'loc_13D2',
    )

    ChrTalk(
        0x00FE,
        (
            '欢迎来到格鲁纳门。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要去格兰赛尔地区的话，\n',
            '通过这个关所就能到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15CD')

    def _loc_13D2(): pass

    label('loc_13D2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004C, 1, 0x261)),
            Expr.Return,
        ),
        'loc_1420',
    )

    ChrTalk(
        0x00FE,
        (
            '哦？\n',
            '你们好像都是游击士嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '难道这一带\n',
            '发生了什么事情吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15CD')

    def _loc_1420(): pass

    label('loc_1420')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Return,
        ),
        'loc_148D',
    )

    ChrTalk(
        0x00FE,
        (
            '说起来，\n',
            '最近利贝尔通讯社的记者\n',
            '到过亚宁堡来取材呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说什么要写一篇\n',
            '关于古老遗迹的特集。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15CD')

    def _loc_148D(): pass

    label('loc_148D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 7, 0x24F)),
            Expr.Return,
        ),
        'loc_1537',
    )

    ChrTalk(
        0x00FE,
        (
            '这前面不止有王都，\n',
            '还有王家的艾尔贝离宫。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '离宫在公用时间之外，\n',
            '均向格兰赛尔市民开放，\n',
            '可以自由出入哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '艾莉茜雅女王即位以来，\n',
            '王家也改变了许多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15CD')

    def _loc_1537(): pass

    label('loc_1537')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 1, 0x239)),
            Expr.Return,
        ),
        'loc_15A0',
    )

    ChrTalk(
        0x00FE,
        (
            '格兰赛尔城位于瓦雷利亚湖畔上，\n',
            '是一座非常美丽的城堡。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '街上的热闹景象也非常让人惊叹。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15CD')

    def _loc_15A0(): pass

    label('loc_15A0')

    ChrTalk(
        0x00FE,
        (
            '前面就是格兰赛尔地区了。\n',
            '去王都有事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_15CD(): pass

    label('loc_15CD')

    TalkEnd(0x00FE)

    Return()

# id: 0x0009 offset: 0x15D1
@scena.Code('func_09_15D1')
def func_09_15D1():
    TalkBegin(0x00FF)
    Sleep(400)

    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
