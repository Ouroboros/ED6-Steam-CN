import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T1311_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T1311   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'T1311.x'
    header.mapIndex       = 1
    header.bgm            = 84
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
            dword_00        = 0x0000BB80,
            dword_04        = 0xFFFFF448,
            dword_08        = 0x00006978,
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
        ScenaEntryPoint(
            dword_00        = 0x0000BB80,
            dword_04        = 0xFFFFF448,
            dword_08        = 0x00006978,
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
        ScenaEntryPoint(
            dword_00        = 0x0000BB80,
            dword_04        = 0xFFFFF448,
            dword_08        = 0x00006978,
            word_0C         = 0x0004,
            word_0E         = 0x0000,
            dword_10        = 0,
            dword_14        = 6000,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 3000,
            dword_2C        = 280,
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

# id: 0x10000 offset: 0x130
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT07/CH01300._CH', 'ED6_DT07/CH01300P._CP'),
        ('ED6_DT07/CH01310._CH', 'ED6_DT07/CH01310P._CP'),
        ('ED6_DT07/CH01240._CH', 'ED6_DT07/CH01240P._CP'),
        ('ED6_DT07/CH00003._CH', 'ED6_DT07/CH00003P._CP'),
        ('ED6_DT07/CH00013._CH', 'ED6_DT07/CH00013P._CP'),
        ('ED6_DT06/CH20020._CH', 'ED6_DT06/CH20020P._CP'),
        ('ED6_DT06/CH20021._CH', 'ED6_DT06/CH20021P._CP'),
        ('ED6_DT06/CH20053._CH', 'ED6_DT06/CH20053P._CP'),
        ('ED6_DT06/CH20053._CH', 'ED6_DT06/CH20053P._CP'),
        ('ED6_DT06/CH20062._CH', 'ED6_DT06/CH20062P._CP'),
    ]

# id: 0x10001 offset: 0x182
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '赛罗斯副长',
            x                   = 19990,
            z                   = 0,
            y                   = 22490,
            direction           = 90,
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
            name                = '士兵阿萨',
            x                   = 22000,
            z                   = 0,
            y                   = 9500,
            direction           = 27,
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
            name                = '赛尔斯特队长',
            x                   = 81840,
            z                   = 0,
            y                   = 13080,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0105,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '亚妮拉丝',
            x                   = 21900,
            z                   = 0,
            y                   = 22100,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '士兵艾格尔',
            x                   = 19990,
            z                   = 0,
            y                   = 7950,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '士兵迈奇',
            x                   = 76700,
            z                   = 0,
            y                   = 7590,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '士兵卡多尔斯',
            x                   = 25000,
            z                   = 0,
            y                   = 10500,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '器皿',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 65541,
            chipIndex           = 5,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '器皿',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 65541,
            chipIndex           = 5,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '咖啡',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1572869,
            chipIndex           = 5,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '咖啡',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1572869,
            chipIndex           = 5,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x2E2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x2E2
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x2E2
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 21950,
            triggerZ            = 0,
            triggerY            = 22540,
            triggerRange        = 400,
            actorX              = 19990,
            actorZ              = 1500,
            actorY              = 22490,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 18440,
            triggerZ            = 0,
            triggerY            = 12120,
            triggerRange        = 1000,
            actorX              = 18440,
            actorZ              = 1000,
            actorY              = 12120,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000E,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x32A
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_352',
    )

    OP_71(0x0002, 0x0010)
    ChrClearFlags(0x000E, 0x0080)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x0009, 0x0008)
    ChrSetFlags(0x000D, 0x0080)
    ChrSetFlags(0x0009, 0x0008)

    Jump('loc_3EF')

    def _loc_352(): pass

    label('loc_352')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_37A',
    )

    OP_71(0x0002, 0x0010)
    ChrClearFlags(0x000E, 0x0080)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x0009, 0x0008)
    ChrSetFlags(0x000D, 0x0080)
    ChrSetFlags(0x0009, 0x0008)

    Jump('loc_3EF')

    def _loc_37A(): pass

    label('loc_37A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 5, 0x40D)),
            Expr.Return,
        ),
        'loc_393',
    )

    OP_71(0x0002, 0x0010)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x0009, 0x0008)

    Jump('loc_3EF')

    def _loc_393(): pass

    label('loc_393')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0080, 7, 0x407)),
            Expr.Return,
        ),
        'loc_3AC',
    )

    OP_71(0x0002, 0x0010)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x0009, 0x0008)

    Jump('loc_3EF')

    def _loc_3AC(): pass

    label('loc_3AC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0080, 6, 0x406)),
            Expr.Return,
        ),
        'loc_3C0',
    )

    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x0009, 0x0008)

    Jump('loc_3EF')

    def _loc_3C0(): pass

    label('loc_3C0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_3D9',
    )

    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x0009, 0x0008)
    ChrClearFlags(0x000C, 0x0080)

    Jump('loc_3EF')

    def _loc_3D9(): pass

    label('loc_3D9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_3EF',
    )

    ChrClearFlags(0x000B, 0x0080)
    ChrSetFlags(0x000D, 0x0080)
    ChrSetFlags(0x000D, 0x0008)

    def _loc_3EF(): pass

    label('loc_3EF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 4, 0x3FC)),
            Expr.Return,
        ),
        'loc_3FD',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    Event(0, func_0B_24E7)

    def _loc_3FD(): pass

    label('loc_3FD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_414',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x52),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, func_0C_3A22)

    def _loc_414(): pass

    label('loc_414')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 3, 0x3FB)),
            Expr.Return,
        ),
        'loc_422',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    Event(0, func_0D_3D89)

    def _loc_422(): pass

    label('loc_422')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000068, 'loc_42E'),
        (-1, 'loc_441'),
    )

    def _loc_42E(): pass

    label('loc_42E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0080, 5, 0x405)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0080, 4, 0x404)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_43E',
    )

    Event(0, func_0B_24E7)

    def _loc_43E(): pass

    label('loc_43E')

    Jump('loc_441')

    def _loc_441(): pass

    label('loc_441')

    Return()

# id: 0x0001 offset: 0x442
@scena.Code('func_01_442')
def func_01_442():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0080, 5, 0x405)),
            Expr.Return,
        ),
        'loc_46F',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x52),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000D, 0x0080)
    OP_64(0x00, 0x0001)

    def _loc_46F(): pass

    label('loc_46F')

    LoadEffect(0x00, 'map\\\\mp027_00.eff')
    PlayEffect(0x00, 0x00, 0x00FF, 18440, 1000, 12120, 0, 0, 0, 1300, 1300, 1300, 0x00FF, 0, 0, 0, 0)

    Return()

# id: 0x0002 offset: 0x4B9
@scena.Code('func_02_4B9')
def func_02_4B9():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_4CE',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_4B9')

    def _loc_4CE(): pass

    label('loc_4CE')

    Return()

# id: 0x0003 offset: 0x4CF
@scena.Code('func_03_4CF')
def func_03_4CF():
    Call(0, 0x0004)

    Return()

# id: 0x0004 offset: 0x4D4
@scena.Code('func_04_4D4')
def func_04_4D4():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_535',
    )

    ChrTalk(
        0x0008,
        (
            '从卢安订购的鱼\n',
            '终于送过来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '今晚就稍微奢侈一下，\n',
            '给大家振奋一下士气吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_101A')

    def _loc_535(): pass

    label('loc_535')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_593',
    )

    ChrTalk(
        0x0008,
        (
            '自那以后，\n',
            '袭击这里的魔兽再也没有出现过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '果然，\n',
            '不是住在这一带的魔兽呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_101A')

    def _loc_593(): pass

    label('loc_593')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 5, 0x40D)),
            Expr.Return,
        ),
        'loc_5DE',
    )

    ChrTalk(
        0x0008,
        (
            '啊，你们不就是游击士的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '怎么了，\n',
            '来这里有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_101A')

    def _loc_5DE(): pass

    label('loc_5DE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0080, 6, 0x406)),
            Expr.Return,
        ),
        'loc_D0A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0080, 7, 0x407)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C3F',
    )

    MapClearFlags(0x00000001)
    OP_69(0x0008, 1000)

    ChrTalk(
        0x0101,
        (
            '#000F士兵先生，早上好～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040333V#010F早上好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1440040334V哦，早啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1440040335V昨天真的是\n',
            '辛苦你们啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嘿嘿，没什么啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040337V士兵先生你们呢？\n',
            '后来巡逻的时候\n',
            '没有发生什么事情吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1440040338V啊啊。\n',
            '之后一切正常。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1440040339V不过……有一点比较奇怪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F奇怪……怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1440040341V街道和关所附近的照明设施\n',
            '有驱赶魔兽的防御效果，\n',
            '这点你们应该很清楚的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1440040342V就算魔兽真的靠近了关所，\n',
            '充其量也只有两三只。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1440040343V但是昨天却来了一大群，\n',
            '这种情况我们还是第一次遇到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F这样说来的确是有点奇怪……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1440040345V呵呵，不过比起那些帝国军，\n',
            '这些魔兽还算挺可爱的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1440040346V就把这次骚动\n',
            '当成防卫关所的演习好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F这、这样没问题吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1440040348V对于我们来说，\n',
            '帝国那边的动静才是最令人担心的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '至于魔兽之类的，\n',
            '还是交给你们游击士处理吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1440040350V那么……\n',
            '你们也该出发了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1440040351V现在办理通行手续吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040353V#010F是的，麻烦您了。',
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
            '通往卢安地区的通行手续已经办理完毕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0008,
        (
            '#1440040354V……这样就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1440040355V那么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0008, 45, 400)
    OP_70(0x0002, 100)
    CameraMove(23765, 0, 25450, 2000)

    ChrTalk(
        0x0008,
        (
            '#1440040356V碧海白花环抱的卢安\n',
            '欢迎你们的到来！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_69(0x0008, 1000)
    ChrTurnDirection(0x0008, 0x0000, 400)

    ChrTalk(
        0x0008,
        (
            '#1440040357V对了对了，\n',
            '小姑娘你们是不是打算去卢安市？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1440040359V那就麻烦你们把昨天的情况\n',
            '向卢安的支部报告一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1440040360V军队也会支付相应的酬金的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊，这样可以吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1440040362V呵呵，\n',
            '这些酬金你们就和阿加特平分吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1440040363V那么后会有期，\n',
            '期待你们早日成为正游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040365V#010F承蒙你们多方关照了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0080, 7, 0x407))
    OP_28(0x0011, 0x04, 0x40)
    OP_28(0x0013, 0x04, 0x40)
    NewScene('ED6_DT01/T1300._SN', 101, 0, 0)
    IdleLoop()

    Jump('loc_D07')

    def _loc_C3F(): pass

    label('loc_C3F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_CB6',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '啊呀，是你们啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '那就麻烦你们把昨天的情况\n',
            '向卢安的支部报告一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '去卢安的路上要小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D07')

    def _loc_CB6(): pass

    label('loc_CB6')

    ChrTalk(
        0x0008,
        (
            '那就麻烦你们把昨天的情况\n',
            '向卢安的支部报告一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '去卢安的路上要小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D07(): pass

    label('loc_D07')

    Jump('loc_101A')

    def _loc_D0A(): pass

    label('loc_D0A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_D4F',
    )

    ChrTalk(
        0x0008,
        (
            '啊呀，这种时间\n',
            '还到这里来啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '外面已经很冷了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_101A')

    def _loc_D4F(): pass

    label('loc_D4F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_E75',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_E1D',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '不管多么习惯旅行在外，\n',
            '晚上在这一带行走还是非常危险的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '山路崎岖，而且魔兽也多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '说起来\n',
            '最近很奇怪的是，\n',
            '我看到了有首领带领的魔兽群体。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '可是至今为止都没有见过的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E72')

    def _loc_E1D(): pass

    label('loc_E1D')

    ChrTalk(
        0x0008,
        (
            '最近很奇怪的是，\n',
            '会看到有首领带领的魔兽群体。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '可是至今为止都没有见过的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E72(): pass

    label('loc_E72')

    Jump('loc_101A')

    def _loc_E75(): pass

    label('loc_E75')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_EE8',
    )

    ChrTalk(
        0x0008,
        (
            '我有义务\n',
            '让士兵们平时保持\n',
            '６个小时以上的睡眠。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '睡眠不足的话，\n',
            '就无法将自己的实力好好发挥出来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_101A')

    def _loc_EE8(): pass

    label('loc_EE8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_F9F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_F5E',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '别看我这个样子，\n',
            '我可以非常喜欢烹饪的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我会经常请求队长，\n',
            '让我到这里来\n',
            '给士兵们做饭。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F9C')

    def _loc_F5E(): pass

    label('loc_F5E')

    ChrTalk(
        0x0008,
        (
            '顺带一提，那里有\n',
            '供旅行者专用的房间，\n',
            '你们可以随时使用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F9C(): pass

    label('loc_F9C')

    Jump('loc_101A')

    def _loc_F9F(): pass

    label('loc_F9F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_101A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_FFE',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '啊呀，小姑娘\n',
            '你们要去卢安吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '要去卢安的话，\n',
            '必须要有许可证……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_101A')

    def _loc_FFE(): pass

    label('loc_FFE')

    ChrTalk(
        0x0008,
        (
            '啊呀，你们要去卢安吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_101A(): pass

    label('loc_101A')

    TalkEnd(0x0008)

    Return()

# id: 0x0005 offset: 0x101E
@scena.Code('func_05_101E')
def func_05_101E():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_10F0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_10A3',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '今天该轮到\n',
            '我来炒菜做饭了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过刚才副长来，\n',
            '说要代替我做饭。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那个人，真的\n',
            '非常喜欢烹饪啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10ED')

    def _loc_10A3(): pass

    label('loc_10A3')

    ChrTalk(
        0x00FE,
        (
            '不过刚才副长来，\n',
            '说要代替我做饭。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那个人，真的\n',
            '非常喜欢烹饪啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_10ED(): pass

    label('loc_10ED')

    Jump('loc_1492')

    def _loc_10F0(): pass

    label('loc_10F0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_1195',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1163',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '自从空贼被逮捕以来，\n',
            '柏斯地区就非常和平。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎呀，这样接连不断\n',
            '发生事件真是很难办啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1192')

    def _loc_1163(): pass

    label('loc_1163')

    ChrTalk(
        0x00FE,
        (
            '自从空贼被逮捕以来，\n',
            '柏斯地区就非常和平。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1192(): pass

    label('loc_1192')

    Jump('loc_1492')

    def _loc_1195(): pass

    label('loc_1195')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 5, 0x40D)),
            Expr.Return,
        ),
        'loc_11E7',
    )

    ChrTalk(
        0x00FE,
        (
            '这之前的魔兽们\n',
            '比想象中的要厉害啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们也要\n',
            '加紧训练才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1492')

    def _loc_11E7(): pass

    label('loc_11E7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0080, 6, 0x406)),
            Expr.Return,
        ),
        'loc_1235',
    )

    ChrTalk(
        0x00FE,
        (
            '昨天的袭击\n',
            '真是个很好的教训。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看来平时\n',
            '就要做好充分准备。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1492')

    def _loc_1235(): pass

    label('loc_1235')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_1296',
    )

    ChrTalk(
        0x00FE,
        (
            '这样持续拖延搜索，\n',
            '国境师团的家伙也相当疲劳吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果有什么新的进展就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1492')

    def _loc_1296(): pass

    label('loc_1296')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_1306',
    )

    ChrTalk(
        0x00FE,
        (
            '这一带\n',
            '越往山中走魔兽越多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且被通缉的魔兽\n',
            '也越来越多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '每天的训练是必不可少的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1492')

    def _loc_1306(): pass

    label('loc_1306')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_13AD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1372',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '这座古罗尼连峰的\n',
            '地形也是起伏频繁的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '难不成\n',
            '空贼团那些家伙们\n',
            '都藏在这一带？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_13AA')

    def _loc_1372(): pass

    label('loc_1372')

    ChrTalk(
        0x00FE,
        (
            '说起来，\n',
            '国境师团的搜查队\n',
            '已经在这里调查好几次了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_13AA(): pass

    label('loc_13AA')

    Jump('loc_1492')

    def _loc_13AD(): pass

    label('loc_13AD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_1492',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1438',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '这么险峻的山道，\n',
            '一般的登山者\n',
            '是根本不会走的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在飞艇还在停航，\n',
            '急着去卢安和柏斯的人们\n',
            '不得不从这里通过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1492')

    def _loc_1438(): pass

    label('loc_1438')

    ChrTalk(
        0x00FE,
        (
            '但是不管怎么说，\n',
            '还是应该尽量避免\n',
            '在晚上翻越这座山峰啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对一般人来说太危险了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1492(): pass

    label('loc_1492')

    TalkEnd(0x0009)

    Return()

# id: 0x0006 offset: 0x1496
@scena.Code('func_06_1496')
def func_06_1496():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_15A6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1538',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '利贝尔各地的关所\n',
            '在十年前分裂帝国军时\n',
            '起到了很大的作用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且如今也\n',
            '作为军事要地被广泛利用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这些地方的守备\n',
            '绝对不能放松。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15A3')

    def _loc_1538(): pass

    label('loc_1538')

    ChrTalk(
        0x00FE,
        (
            '利贝尔各地的关所\n',
            '在十年前分裂帝国军时\n',
            '起到了很大的作用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以说，这些地方的守备\n',
            '绝对不可以放松。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_15A3(): pass

    label('loc_15A3')

    Jump('loc_1AC3')

    def _loc_15A6(): pass

    label('loc_15A6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_167E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1629',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '为了镇守关所，\n',
            '才让士兵们驻守在这里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '偶尔也会向\n',
            '一些登山者实行救助。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为来古罗尼连峰登山\n',
            ' ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_167B')

    def _loc_1629(): pass

    label('loc_1629')

    ChrTalk(
        0x00FE,
        (
            '为了镇守关所，\n',
            '才让士兵们驻守在这里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '偶尔也会向\n',
            '一些登山者实行救助。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_167B(): pass

    label('loc_167B')

    Jump('loc_1AC3')

    def _loc_167E(): pass

    label('loc_167E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 5, 0x40D)),
            Expr.Return,
        ),
        'loc_16DB',
    )

    ChrTalk(
        0x00FE,
        (
            '如果敌人从两个方向发动进攻，\n',
            '该如何防守呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天训练的议题就是这个了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AC3')

    def _loc_16DB(): pass

    label('loc_16DB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0080, 7, 0x407)),
            Expr.Return,
        ),
        'loc_1709',
    )

    ChrTalk(
        0x00FE,
        (
            '喂，要出发了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '小心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AC3')

    def _loc_1709(): pass

    label('loc_1709')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0080, 6, 0x406)),
            Expr.Return,
        ),
        'loc_1750',
    )

    ChrTalk(
        0x00FE,
        (
            '哦，睡得还好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '昨天你们出手\n',
            '真是帮了我们大忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AC3')

    def _loc_1750(): pass

    label('loc_1750')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0080, 0, 0x400)),
            Expr.Return,
        ),
        'loc_18F3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0080, 4, 0x404)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_18B5',
    )

    SetScenaFlags(ScenaFlag(0x0080, 4, 0x404))
    MapClearFlags(0x00000001)
    OP_69(0x00FE, 1000)

    ChrTalk(
        0x00FE,
        (
            '#1430040138V啊，你们是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040139V#010F您好，不好意思打扰一下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020040140V其实我们……',
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
            '两人向队长说明情况，\n',
            '并且请求在关所留宿一晚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x00FE,
        (
            '#1430040141V哦，没问题。\n',
            '游击士的身份就是一种保证。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '隔壁的房间请自由使用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040143V#000F谢谢，队长先生！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_69(0x0000, 1000)
    MapSetFlags(0x00000001)

    Jump('loc_18F0')

    def _loc_18B5(): pass

    label('loc_18B5')

    ChrTalk(
        0x00FE,
        (
            '这里隔壁的休息室\n',
            '房间请自由使用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '先取个暖如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_18F0(): pass

    label('loc_18F0')

    Jump('loc_1AC3')

    def _loc_18F3(): pass

    label('loc_18F3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_193E',
    )

    ChrTalk(
        0x00FE,
        (
            '国境师团好像要求增员了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看来将军\n',
            '准备在这几天动手了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AC3')

    def _loc_193E(): pass

    label('loc_193E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_19AA',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯，摩尔根将军已经将搜索范围\n',
            '缩小到北部山区了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '空贼们果然藏在\n',
            '国境附近的某个地方啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AC3')

    def _loc_19AA(): pass

    label('loc_19AA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_1A7E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1A20',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '摩尔根将军\n',
            '要求强化这一带的警备，\n',
            '下达了这样的命令。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '空贼们藏在哪里，\n',
            '还不是很清楚呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A7B')

    def _loc_1A20(): pass

    label('loc_1A20')

    ChrTalk(
        0x00FE,
        (
            '尤其是山林，\n',
            '那里是他们最好的藏身之处。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我要赶快通知\n',
            '队里的人，\n',
            '让他们提高警惕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A7B(): pass

    label('loc_1A7B')

    Jump('loc_1AC3')

    def _loc_1A7E(): pass

    label('loc_1A7E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_1AC3',
    )

    ChrTalk(
        0x00FE,
        (
            '需要通行许可证的话，我就发给你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '随时来找我好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1AC3(): pass

    label('loc_1AC3')

    TalkEnd(0x000A)

    Return()

# id: 0x0007 offset: 0x1AC7
@scena.Code('func_07_1AC7')
def func_07_1AC7():
    TalkBegin(0x000B)
    ChrTurnDirection(0x00FE, 0x0103, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006C, 0, 0x360)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1D35',
    )

    SetScenaFlags(ScenaFlag(0x006C, 0, 0x360))
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '#0120030603V啊，难不成……\n',
            '这不是雪拉扎德前辈吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0120030604V很久不见了啊。\n',
            '自从您去修行之后就再没见面了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030030605V#020F这不是亚妮拉丝吗。\n',
            '你在这里做什么呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0120030606V呵呵，协会委派我来这里\n',
            '就在这个方向。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030030607V#020F是这样……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030030608V对了，你已经找到\n',
            '所谓的剑之道了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0120030609V呵呵，请别问了。\n',
            '我还是处在修行阶段呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0120030610V说起来，前辈您也是在\n',
            '执行协会的任务吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030030611V#020F是啊，不过我和你的任务性质不同。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0120030612V是这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0120030613V这个地方\n',
            '最近事情很多啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0120030614V您路上一定要小心哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E47')

    def _loc_1D35(): pass

    label('loc_1D35')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1DE6',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x0103,
        (
            '#0030030615V#020F啊，这不是亚妮拉丝吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0120030616V雪拉扎德前辈！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0120030617V怎么样？\n',
            '调查进行得顺利吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030030618V#020F嗯，有一点进展了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E47')

    def _loc_1DE6(): pass

    label('loc_1DE6')

    ChrTalk(
        0x00FE,
        (
            '#0120030619V雪拉扎德前辈，\n',
            '这个地方最近处于多事之秋。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0120030620V您路上一定要小心哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1E47(): pass

    label('loc_1E47')

    TalkEnd(0x000B)

    Return()

# id: 0x0008 offset: 0x1E4B
@scena.Code('func_08_1E4B')
def func_08_1E4B():
    TalkBegin(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_1E88',
    )

    ChrTalk(
        0x000C,
        (
            '这里的海拔比较高，\n',
            '太阳一落山果然就会很冷啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1E88(): pass

    label('loc_1E88')

    TalkEnd(0x000C)

    Return()

# id: 0x0009 offset: 0x1E8C
@scena.Code('func_09_1E8C')
def func_09_1E8C():
    TalkBegin(0x000D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_1EED',
    )

    ChrTalk(
        0x00FE,
        (
            '被魔兽打伤的地方\n',
            '终于痊愈了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要尽量避免这类事情的发生，\n',
            '所以要加紧训练。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2009')

    def _loc_1EED(): pass

    label('loc_1EED')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_1F42',
    )

    ChrTalk(
        0x00FE,
        (
            '副长还真是喜欢烹饪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有时候明明不是他当班，\n',
            '但是却在厨房烧饭呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2009')

    def _loc_1F42(): pass

    label('loc_1F42')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 5, 0x40D)),
            Expr.Return,
        ),
        'loc_1F93',
    )

    ChrTalk(
        0x00FE,
        (
            '柴火差不多要用完了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '训练结束后去报告一下，\n',
            '然后去砍些柴吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2009')

    def _loc_1F93(): pass

    label('loc_1F93')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0080, 6, 0x406)),
            Expr.Return,
        ),
        'loc_1FD8',
    )

    ChrTalk(
        0x00FE,
        (
            '痛痛痛痛痛……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是失策。\n',
            '被魔兽打伤的地方好痛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2009')

    def _loc_1FD8(): pass

    label('loc_1FD8')

    ChrTalk(
        0x00FE,
        (
            '我还要再值会儿班。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '趁现在\n',
            '赶快吃饭吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2009(): pass

    label('loc_2009')

    TalkEnd(0x000D)

    Return()

# id: 0x000A offset: 0x200D
@scena.Code('func_0A_200D')
def func_0A_200D():
    TalkBegin(0x000E)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_2055',
    )

    ChrTalk(
        0x00FE,
        (
            '离值勤还有段时间……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我还是先\n',
            '稍微小睡一会儿吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24E3')

    def _loc_2055(): pass

    label('loc_2055')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_2134',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2106',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '这里是深山老林，\n',
            '食物的供应非常不方便。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然有很多东西都是\n',
            '从柏斯和卢安那里运送过来的，\n',
            '这些都是靠这条山路呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '兼任保卫的途中\n',
            '过来迎接你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2131')

    def _loc_2106(): pass

    label('loc_2106')

    ChrTalk(
        0x00FE,
        (
            '这里一到冬天，\n',
            '大雪堆积，特别不方便。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2131(): pass

    label('loc_2131')

    Jump('loc_24E3')

    def _loc_2134(): pass

    label('loc_2134')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 5, 0x40D)),
            Expr.Return,
        ),
        'loc_218B',
    )

    ChrTalk(
        0x00FE,
        (
            '差不多到训练的时间了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为发生过魔兽袭击事件，\n',
            '大家要提高警惕了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24E3')

    def _loc_218B(): pass

    label('loc_218B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0080, 6, 0x406)),
            Expr.Return,
        ),
        'loc_2239',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_21F9',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '早上好，昨天谢谢你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然看上去挺年轻，\n',
            '但不愧是游击士呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '干得真棒。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2236')

    def _loc_21F9(): pass

    label('loc_21F9')

    ChrTalk(
        0x00FE,
        (
            '虽然看上去挺年轻，\n',
            '不愧是游击士呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '昨天干得真棒。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2236(): pass

    label('loc_2236')

    Jump('loc_24E3')

    def _loc_2239(): pass

    label('loc_2239')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_22E2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_22AA',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '有什么事？\n',
            '没关系，你们可以进去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '想使用里面的屋子时，\n',
            '和我们队长打声招呼就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_22DF')

    def _loc_22AA(): pass

    label('loc_22AA')

    ChrTalk(
        0x00FE,
        (
            '想使用里面的屋子时，\n',
            '和我们队长打声招呼就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_22DF(): pass

    label('loc_22DF')

    Jump('loc_24E3')

    def _loc_22E2(): pass

    label('loc_22E2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_23C5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2387',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '好像找不到\n',
            '空贼团的所在之处啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '国境师团的家伙们\n',
            '也经常到这里\n',
            '来进行调查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '柏斯这个地方\n',
            '就是山岳比较多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            ' \n',
            '可是最理想的了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23C2')

    def _loc_2387(): pass

    label('loc_2387')

    ChrTalk(
        0x00FE,
        (
            '柏斯这个地方\n',
            '就是山岳比较多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            ' \n',
            '可是最理想的了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_23C2(): pass

    label('loc_23C2')

    Jump('loc_24E3')

    def _loc_23C5(): pass

    label('loc_23C5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_242C',
    )

    ChrTalk(
        0x00FE,
        (
            '消失的飞艇\n',
            '好像被找到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为犯人还没有被抓住，\n',
            '所以还要在关所\n',
            '就得继续进行检查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24E3')

    def _loc_242C(): pass

    label('loc_242C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_2495',
    )

    ChrTalk(
        0x00FE,
        (
            '空贼团啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，这次是由那位\n',
            '摩尔根将军亲临指挥呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '肯定马上就会抓到他们的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24E3')

    def _loc_2495(): pass

    label('loc_2495')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_24E3',
    )

    ChrTalk(
        0x00FE,
        (
            '现在正处在戒严状态中。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果是这样的话，\n',
            '必须先在里面办手续。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_24E3(): pass

    label('loc_24E3')

    TalkEnd(0x000E)

    Return()

# id: 0x000B offset: 0x24E7
@scena.Code('func_0B_24E7')
def func_0B_24E7():
    EventBegin(0x00)
    CameraMove(80990, 200, 53320, 0)
    ChrSetFlags(0x0101, 0x0004)
    ChrSetFlags(0x0102, 0x0004)
    ChrSetPos(0x0101, 81090, 200, 51050, 270)
    ChrSetPos(0x0102, 78250, 200, 51000, 90)
    ChrSetChipByIndex(0x0101, 3)
    ChrSetChipByIndex(0x0102, 4)
    ChrSetPos(0x000F, 79980, 750, 50430, 0)
    ChrSetPos(0x0010, 79200, 750, 51110, 0)
    ChrSetPos(0x0011, 80060, 700, 51150, 0)
    ChrSetPos(0x0012, 79240, 700, 50480, 0)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0012, 0x0080)
    FadeIn(2000, 0)
    OP_0D()
    Sleep(1000)

    OP_62(0x0101, 0x00000000, 1700, 0x08, 0x09, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(1000)

    ChrSetStatus(0x0000, 0xFE, 0)
    ChrSetStatus(0x0001, 0xFE, 0)
    ChrSetStatus(0x0002, 0xFE, 0)
    ChrSetStatus(0x0003, 0xFE, 0)
    ChrSetStatus(0x0004, 0xFE, 0)
    ChrSetStatus(0x0005, 0xFE, 0)
    ChrSetStatus(0x0006, 0xFE, 0)
    ChrSetStatus(0x0007, 0xFE, 0)

    ChrTalk(
        0x0101,
        (
            '#0010040144V#001F#2P哈～～吃饱啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040145V还说不要太期待什么的，\n',
            '没想到原来是这么好吃呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040146V#010F是啊。\n',
            '想不到军队里也有如此好吃的饭菜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(113, 0x00, 0x64)
    Sleep(1000)

    ChrSetFlags(0x0008, 0x0040)
    ChrSetRGBAMask(0x0008, 255, 255, 255, 0, 0)
    ChrSetPos(0x0008, 72320, 0, 52990, 90)

    ChrTalk(
        0x0008,
        (
            '#1440040147V#2P打扰了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 1700, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0102, 0x00000000, 1700, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(500)

    PlaySE(6, 0x00, 0x64)
    Sleep(500)

    OP_4A(0x0008, 255)
    ChrSetFlags(0x0008, 0x0004)

    @scena.Lambda('lambda_2708')
    def lambda_2708():
        CameraMove(79690, 0, 53470, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2708)

    ChrSetSubChip(0x0102, 1)
    ChrSetDirection(0x0008, 90, 0)
    ChrClearFlags(0x0008, 0x0080)

    @scena.Lambda('lambda_2731')
    def lambda_2731():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_2731)

    ChrWalkTo(0x0008, 79660, 0, 52870, 3000, 0x00)
    ChrSetDirection(0x0008, 180, 400)

    ChrTalk(
        0x0101,
        (
            '#0010040148V#001F#2P啊，副长先生。\n',
            '饭菜真的很好吃哦⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040149V#010F谢谢你们的款待。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1440040150V#1P只是些粗茶淡饭，\n',
            '能合你们的口味就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1440040151V#1P啊，对了……\n',
            '又有一位客人来了，\n',
            '你们不介意和他住一个房间吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040152V#014F客人……\n',
            '这么晚了还有人来这里？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040153V#000F#2P这位客人胆子还挺大的呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040154V我们倒无所谓，\n',
            '说到底自己也同样是客人罢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1440040155V#1P你们能这么说真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1440040156V#1P说起来，他和小姑娘你们是同行，\n',
            '因此也没必要太过顾虑哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040157V#004F#2P哎？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040158V#014F同行？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x0106, 0x0080)
    ChrSetRGBAMask(0x0106, 255, 255, 255, 0, 0)
    ChrSetChipByIndex(0x0106, 7)
    ChrSetPos(0x0106, 72320, 0, 52990, 90)

    NpcTalk(
        0x0106,
        '青年的声音',
        (
            '#0050040159V#2P哼……\n',
            '没想到你们也来了这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x0106, 0x0004)

    @scena.Lambda('lambda_2A0A')
    def lambda_2A0A():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0106, 0x0003, lambda_2A0A)

    @scena.Lambda('lambda_2A1C')
    def lambda_2A1C():
        ChrWalkTo(0x00FE, 78640, 0, 53600, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_2A1C)

    Sleep(500)

    OP_62(0x0101, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(100)

    OP_62(0x0102, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    WaitForThreadExit(0x0106, 0x0001)
    ChrSetDirection(0x0106, 180, 400)
    ChrClearFlags(0x0106, 0x0004)

    ChrTalk(
        0x0101,
        (
            '#0010040160V#004F#2P啊，是你……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040161V#014F『重剑阿加特』……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1440040162V#1P什么，原来你们认识啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0008, 270, 400)

    ChrTalk(
        0x0008,
        (
            '#1440040163V#2P对了阿加特，\n',
            '你吃过晚饭没有？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050040164V#050F谢了，不用了。\n',
            '刚刚已经吃过了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050040165V让我在这里睡一晚就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1440040166V#2P没问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1440040167V#2P好了。\n',
            '你们就自己分配床位吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0008, 180, 400)
    Sleep(300)

    ChrTalk(
        0x0008,
        (
            '#1440040168V#1P晚安了，各位。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0008, 270, 400)
    TerminateThread(0x0106, 0xFF)
    ChrWalkTo(0x0008, 78400, 0, 52700, 3000, 0x00)

    @scena.Lambda('lambda_2C2C')
    def lambda_2C2C():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_2C2C')

    DispatchAsync2(0x0106, 0x0003, lambda_2C2C)

    ChrWalkTo(0x0008, 74570, 0, 52910, 3000, 0x00)

    @scena.Lambda('lambda_2C51')
    def lambda_2C51():
        ChrWalkTo(0x00FE, 72320, 0, 52990, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2C51)

    ChrSetRGBAMask(0x0008, 255, 255, 255, 0, 500)
    PlaySE(7, 0x00, 0x64)
    ChrSetFlags(0x0008, 0x0080)
    WaitForThreadExit(0x0008, 0x0001)
    Sleep(500)

    @scena.Lambda('lambda_2C8B')
    def lambda_2C8B():
        CameraMove(80990, 200, 53320, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2C8B)

    TerminateThread(0x0106, 0xFF)
    ChrSetDirection(0x0106, 135, 400)
    ChrWalkTo(0x0106, 79660, 0, 52870, 2000, 0x00)
    ChrSetDirection(0x0106, 180, 400)

    ChrTalk(
        0x0106,
        (
            '#0050040169V#050F#1P对了……\n',
            '你们两个是大叔的孩子吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050040170V为什么你们\n',
            '会在这种地方过夜？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050040171V雪拉扎德没和你们在一起吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040172V#010F雪拉姐姐她\n',
            '已经回洛连特去了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020040173V现在只有我们两个一起旅行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040174V#006F#2P嗯，我们以成为正游击士为目标，\n',
            '打算环游整个王国一周。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040175V同时为了修行，选择了徒步旅行哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050040176V#052F#1P正游击士？\n',
            '徒步环游整个王国一周？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050040177V真是两个无忧无虑的小鬼啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 1700, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010040178V#009F#2P你、你说什么～！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050040179V#053F#1P像你们这种小鬼可以\n',
            '那么简单就成为正游击士吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050040180V用常识想想，常识啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040181V#005F#2P别、别小看我们！\n',
            '之前我们还抓住了那些空贼呢！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040182V而且我们也获得了推荐信，\n',
            '你别把我们当作三岁小孩子！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050040183V#050F#1P捉空贼那件事吗？\n',
            '我从卢格兰老爷子那听说过了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050040184V#050F我倒要问问你们……\n',
            '假如只有你们两个的话，\n',
            '事件真的会那么容易就解决吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050040185V假如没有雪拉扎德在身边，\n',
            '你们自己可以对付得了空贼吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040186V#003F#2P这、这个嘛……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040187V#015F……我想会很难。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050040188V#050F#1P那是当然的啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050040189V你们只是初出茅庐的新人，还是小鬼而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050040190V能力不够、经验不足，\n',
            '遇到突发事件又不能做出敏锐的判断。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050040191V而且还这么不知天高地厚，\n',
            '你们迟早有一天会摔跟头的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040192V#009F#2P什、什么不知天高地厚啊！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040193V你才是呢！\n',
            '这个时候还上山来，\n',
            '你究竟知不知道有多危险啊？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040194V还有资格说别人吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050040195V#054F#1P蠢材！我和你们可不一样！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050040196V而且我有任务在身，\n',
            '不像你们那样在到处游山玩水。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040197V#012F任务？\n',
            '是游击士协会的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050040198V#050F#1P啊啊，就是你们那个老爸，\n',
            '出差前把自己的任务强推给我……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040199V#004F#2P啊……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040200V#014F父亲强推给你的任务？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050040201V#050F#1P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0106, 0, 400)

    ChrTalk(
        0x0106,
        (
            '#0050040202V#053F不说了，明天还要早起。\n',
            '赶快睡觉要紧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050040203V你们也别再啰嗦了，上床睡觉吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_345A')
    def lambda_345A():
        CameraMove(79640, 0, 54740, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_345A)

    ChrWalkTo(0x0106, 77650, 0, 56480, 2500, 0x00)
    ChrSetDirection(0x0106, 180, 400)
    ChrSetFlags(0x0106, 0x0004)
    ChrJumpTo(0x0106, 75800, 1000, 55700, 1200, 5000)
    PlaySE(209, 0x00, 0x64)
    ChrSetFlags(0x0106, 0x0002)
    ChrSetChipByIndex(0x0106, 9)
    OP_7C(0, 100, 2000, 100)

    ChrTalk(
        0x0101,
        (
            '#0010040204V#005F#2P啊～这样就想糊弄过去吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040205V#018F说得那么明显，\n',
            '分明就是要让我们在意嘛……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0106, 0x00000000, 1700, 0x0E, 0x0F, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1200)

    OP_99(0x0106, 0x00, 0x02, 1000)
    Sleep(300)

    ChrSetSubChip(0x0106, 3)

    ChrTalk(
        0x0106,
        (
            '#0050040206V#054F#1P够啦！别再烦我啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050040207V我是为了你们两个小鬼好，\n',
            '多管闲事只会惹来一身麻烦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050040208V明天一早就给我快点去卢安，\n',
            '看看协会的公告板上有什么活干！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0106, 0x03, 0x05, 1000)
    Sleep(400)

    ChrTalk(
        0x0106,
        (
            '#0050040209V#053F#1P那种才是……呼啊……\n',
            '你们应该去过的生活……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050040210V……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0106, 0x00000000, 1700, 0x1C, 0x21, 0x000000FA, 0x00)
    Sleep(1000)

    OP_62(0x0101, 0x00000000, 1700, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 1700, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010040211V#004F#2P等、等一下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040212V#014F好像已经睡着了。\n',
            '和艾丝蒂尔你一样能睡呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040213V#005F#2P别把我和他混为一谈！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040214V#007F真是的～这家伙究竟怎么想的！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040215V难道除了吵架，\n',
            '他就不会做点别的事情吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0102, 0)
    Sleep(300)

    ChrTalk(
        0x0102,
        (
            '#0020040216V#010F算了算了。\n',
            '毕竟我们还是新人啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020040217V也许他只是担心我们，\n',
            '才会特意说那么严厉的话吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040218V#009F#2P………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040219V我说约修亚，\n',
            '难道你真的这样想吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040220V#015F这个嘛，我也不太肯定。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020040221V#010F不过，正如他所说的，\n',
            '我们最好也早点休息吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020040222V明天还要下山呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040223V#007F#2P唔～虽然感到很不爽，\n',
            '不过没办法啦……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040224V#006F嘿嘿，我们干脆在他脸上涂鸦，\n',
            '给他一点教训吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040225V我看他睡得挺熟的，应该没问题☆',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040226V#018F还是不要这么做吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    MapSetFlags(0x02000000)
    NewScene('ED6_DT01/T1301._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000C offset: 0x3A22
@scena.Code('func_0C_3A22')
def func_0C_3A22():
    EventBegin(0x00)
    CameraMove(79640, 0, 54740, 0)
    ChrSetFlags(0x0101, 0x0004)
    ChrSetFlags(0x0102, 0x0004)
    ChrSetPos(0x0101, 81090, 200, 51050, 270)
    ChrSetPos(0x0102, 78250, 200, 51000, 90)
    ChrSetChipByIndex(0x0101, 3)
    ChrSetChipByIndex(0x0102, 4)
    ChrSetSubChip(0x0102, 1)
    ChrSetPos(0x000F, 79980, 750, 50430, 0)
    ChrSetPos(0x0010, 79200, 750, 51110, 0)
    ChrSetPos(0x0011, 80060, 700, 51150, 0)
    ChrSetPos(0x0012, 79240, 700, 50480, 0)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0012, 0x0080)
    ChrSetFlags(0x0106, 0x0004)
    ChrSetFlags(0x0106, 0x0002)
    ChrSetPos(0x0106, 75800, 1000, 55700, 0)
    ChrSetChipByIndex(0x0106, 9)
    ChrSetSubChip(0x0106, 2)
    OP_0D()
    OP_62(0x0101, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0106, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010040239V#004F#2P刚、刚才你有没有听到什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040240V#012F好像发生了什么事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0106, 0x00000000, 1700, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1200)

    OP_63(0x0106)
    Sleep(300)

    ChrSetChipByIndex(0x0106, 7)
    ChrClearFlags(0x0106, 0x0002)
    ChrSetDirection(0x0106, 90, 0)
    ChrSetSubChip(0x0106, 0)
    ChrJumpTo(0x0106, 77730, 0, 56070, 600, 6000)
    ChrWalkTo(0x0106, 77520, 0, 53330, 4000, 0x00)

    ChrTalk(
        0x0106,
        (
            '#0050040241V#050F#1P我到外面看看情况，\n',
            '你们两个乖乖留在这里睡觉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0106, 74770, 0, 52900, 6000, 0x00)
    PlaySE(6, 0x00, 0x64)

    @scena.Lambda('lambda_3C5D')
    def lambda_3C5D():
        ChrWalkTo(0x00FE, 72320, 0, 52990, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_3C5D)

    ChrSetRGBAMask(0x0106, 255, 255, 255, 0, 200)
    ChrSetFlags(0x0106, 0x0080)

    ChrTalk(
        0x0101,
        (
            '#0010040242V#004F#2P啊……\n',
            '等、等一下嘛！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040243V#012F为了谨慎起见，\n',
            '我们也出去看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040244V#002F#2P嗯，那当然啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(1000)
    FormationDelMember(0x05, 0xFF)
    ChrClearFlags(0x0101, 0x0004)
    ChrClearFlags(0x0102, 0x0004)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0102, 65535)
    ChrSetPos(0x0102, 77820, 0, 53250, 270)
    ChrSetPos(0x0101, 77820, 0, 53250, 270)
    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000D, 0x0080)
    CameraMove(77820, 0, 53250, 0)
    EventEnd(0x00)
    MapSetFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x0080, 5, 0x405))

    Return()

# id: 0x000D offset: 0x3D89
@scena.Code('func_0D_3D89')
def func_0D_3D89():
    FormationDelMember(0x05, 0xFF)
    MapClearFlags(0x00000001)
    EventBegin(0x00)
    CameraMove(83887, 0, 57065, 0)
    ChrSetPos(0x0101, 84150, 0, 57128, 270)
    ChrSetPos(0x0102, 82890, 0, 56215, 90)
    OP_77(0x00, 0x00, 0x00, 0x00, 0x00000000)

    ChrTalk(
        0x0102,
        (
            '#0020040316V#010F艾丝蒂尔。\n',
            '……天亮了，该起床了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040317V#000F呼啊～～……\n',
            '讨厌……做什么嘛～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_77(0xFF, 0xFF, 0xFF, 0x00, 0x000003E8)
    Sleep(1300)

    ChrTalk(
        0x0101,
        (
            '#0010040318V#000F咦，约修亚……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040319V这么早就要去协会吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040320V#010F你在说什么呀？\n',
            '我们还在古罗尼关所呢。',
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
            '#0010040321V#000F啊，对了……\n',
            '昨天晚上发生了魔兽骚动……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040322V咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 315, 400)
    Sleep(300)

    ChrSetDirection(0x0101, 315, 400)
    Sleep(300)

    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010040323V#000F那个红头发的刀子嘴呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040324V#010F他好像一大早就出发了，\n',
            '应该是有紧要任务要去执行吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040325V#000F是这样吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040326V难得昨天晚上\n',
            '还同心协力把魔兽击退了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040327V连个招呼也不打就走了，\n',
            '真是个没礼貌的家伙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040328V#010F算了算了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020040329V我们也该准备动身出发了，\n',
            '最好在中午之前翻过这座山峰。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040330V#000F嗯，我知道了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040331V终于要到卢安了呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0080, 6, 0x406))
    OP_28(0x003A, 0x04, 0x02)
    OP_28(0x003A, 0x04, 0x04)
    OP_28(0x003A, 0x01, 0x0001)
    OP_28(0x003A, 0x01, 0x0002)
    Fade(1000)
    ChrSetPos(0x0101, 82076, 0, 53560, 270)
    ChrSetPos(0x0102, 82076, 0, 53560, 270)
    EventEnd(0x00)

    Return()

# id: 0x000E offset: 0x4153
@scena.Code('func_0E_4153')
def func_0E_4153():
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '这是一台可供旅行者回复体力的导力器装置。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

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
        32,
        1,
        (
            TXT(0x00, '在此休息\n'),
            TXT(0x01, '离开\n'),
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

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_436C',
    )

    FadeIn(100, 0)
    Sleep(500)

    OP_26(13)
    StopEffect(0x00, 0x02)
    PlayEffect(0x00, 0x02, 0x00FF, 18440, 1000, 12120, 0, 0, 0, 700, 700, 700, 0x00FF, 0, 0, 0, 0)
    OP_6F(0x000A, 0)
    OP_70(0x000A, 50)
    OP_73(0x0033)
    OP_20(0x00000BB8)
    PlaySE(12, 0x00, 0x64)
    StopEffect(0x02, 0x02)
    LoadEffect(0x01, 'map\\\\mp027_01.eff')
    PlayEffect(0x01, 0x01, 0x00FF, 18440, 1000, 12120, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    FadeOut(1000, 0, -1)
    Sleep(700)

    PlaySE(13, 0x00, 0x64)
    OP_0D()
    ChrSetStatus(0x0000, 0xFE, 0)
    ChrSetStatus(0x0001, 0xFE, 0)
    ChrSetStatus(0x0002, 0xFE, 0)
    ChrSetStatus(0x0003, 0xFE, 0)
    ChrSetStatus(0x0004, 0xFE, 0)
    ChrSetStatus(0x0005, 0xFE, 0)
    ChrSetStatus(0x0006, 0xFE, 0)
    ChrSetStatus(0x0007, 0xFE, 0)
    ChrSetPos(0x0000, 19740, 0, 13090, 217)
    ChrSetPos(0x0001, 19740, 0, 13090, 217)
    ChrSetPos(0x0002, 19740, 0, 13090, 217)
    ChrSetPos(0x0003, 19740, 0, 13090, 217)
    OP_69(0x0000, 0)
    OP_30(0x00)
    Sleep(3500)

    StopEffect(0x01, 0x02)
    LoadEffect(0x00, 'map\\\\mp027_00.eff')
    PlayEffect(0x00, 0x00, 0x00FF, 18440, 1000, 12120, 0, 0, 0, 1300, 1300, 1300, 0x00FF, 0, 0, 0, 0)
    OP_6F(0x000A, 0)
    OP_1E()
    FadeIn(1000, 0)
    OP_56(0x00)
    TalkEnd(0x00FF)

    Return()

    def _loc_436C(): pass

    label('loc_436C')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4386',
    )

    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Return()

    def _loc_4386(): pass

    label('loc_4386')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
