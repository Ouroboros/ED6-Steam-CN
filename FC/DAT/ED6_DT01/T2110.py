import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T2110_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2110   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'T2110.x'
    header.mapIndex       = 1
    header.bgm            = 12
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
        ('ED6_DT07/CH01290._CH', 'ED6_DT07/CH01290P._CP'),
        ('ED6_DT07/CH01540._CH', 'ED6_DT07/CH01540P._CP'),
        ('ED6_DT07/CH01170._CH', 'ED6_DT07/CH01170P._CP'),
        ('ED6_DT07/CH01080._CH', 'ED6_DT07/CH01080P._CP'),
        ('ED6_DT07/CH01460._CH', 'ED6_DT07/CH01460P._CP'),
        ('ED6_DT07/CH01030._CH', 'ED6_DT07/CH01030P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01680._CH', 'ED6_DT07/CH01680P._CP'),
        ('ED6_DT07/CH01690._CH', 'ED6_DT07/CH01690P._CP'),
        ('ED6_DT07/CH01083._CH', 'ED6_DT07/CH01083P._CP'),
        ('ED6_DT07/CH01200._CH', 'ED6_DT07/CH01200P._CP'),
        ('ED6_DT07/CH01230._CH', 'ED6_DT07/CH01230P._CP'),
        ('ED6_DT07/CH01470._CH', 'ED6_DT07/CH01470P._CP'),
    ]

# id: 0x10001 offset: 0x112
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '利顿',
            x                   = 2009,
            z                   = 0,
            y                   = -1890,
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
            name                = '希艾尔',
            x                   = -5910,
            z                   = 0,
            y                   = 5190,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '爱蕾塔',
            x                   = -4500,
            z                   = 4000,
            y                   = 5750,
            direction           = 270,
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
            name                = '基诺奇奥',
            x                   = 1670,
            z                   = 0,
            y                   = 1890,
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
            name                = '连茨',
            x                   = 22050,
            z                   = 0,
            y                   = -200,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '丽泽',
            x                   = 27240,
            z                   = 0,
            y                   = -1510,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '托尼奥',
            x                   = 26000,
            z                   = 4000,
            y                   = -500,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '波尔多斯',
            x                   = 25980,
            z                   = 0,
            y                   = 34030,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '诺莉雅',
            x                   = -2270,
            z                   = 0,
            y                   = 37540,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            name                = '罗基克',
            x                   = -2960,
            z                   = 0,
            y                   = 33440,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x01D5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            name                = '诺曼',
            x                   = -31900,
            z                   = 0,
            y                   = 63600,
            direction           = 135,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            name                = '布莉洁特',
            x                   = 24980,
            z                   = 0,
            y                   = 62760,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            name                = '路易',
            x                   = 4990,
            z                   = 0,
            y                   = 64730,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
    )

# id: 0x10002 offset: 0x2B2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x2B2
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x2B2
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x2B2
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_2C6',
    )

    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000B, 0x0008)

    Jump('loc_327')

    def _loc_2C6(): pass

    label('loc_2C6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_2EE',
    )

    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000B, 0x0008)
    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0008, 0x0008)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x0009, 0x0008)

    Jump('loc_327')

    def _loc_2EE(): pass

    label('loc_2EE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 0, 0x418)),
            Expr.Return,
        ),
        'loc_302',
    )

    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0011, 0x0080)

    Jump('loc_327')

    def _loc_302(): pass

    label('loc_302')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_327',
    )

    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0008, 0x0008)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x0009, 0x0008)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0011, 0x0080)

    def _loc_327(): pass

    label('loc_327')

    Return()

# id: 0x0001 offset: 0x328
@scena.Code('func_01_328')
def func_01_328():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 0, 0x418)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 4, 0x43C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Or,
            Expr.Return,
        ),
        'loc_349',
    )

    OP_B1('t2110_y')

    Jump('loc_352')

    def _loc_349(): pass

    label('loc_349')

    OP_B1('t2110_n')

    def _loc_352(): pass

    label('loc_352')

    Return()

# id: 0x0002 offset: 0x353
@scena.Code('func_02_353')
def func_02_353():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_368',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_353')

    def _loc_368(): pass

    label('loc_368')

    Return()

# id: 0x0003 offset: 0x369
@scena.Code('func_03_369')
def func_03_369():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_38C',
    )

    OP_8D(0x00FE, 22020, 37800, 27710, 33160, 1500)

    Jump('func_03_369')

    def _loc_38C(): pass

    label('loc_38C')

    Return()

# id: 0x0004 offset: 0x38D
@scena.Code('func_04_38D')
def func_04_38D():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_401',
    )

    ChrTalk(
        0x00FE,
        (
            '主张推进旅游业的市长\n',
            '已经被逮捕了，\n',
            '城市的形象也受到了损失。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '旅游和住宿的预约\n',
            '都大大减少了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6F0')

    def _loc_401(): pass

    label('loc_401')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_4F1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_490',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '我原来是个渔夫。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，市长换任之后，\n',
            '城里就开始盛行观光业了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '经过妻子的劝说，\n',
            '我就开始从事导游的工作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4EE')

    def _loc_490(): pass

    label('loc_490')

    ChrTalk(
        0x00FE,
        (
            '市长换任之后，\n',
            '城里就开始盛行观光业了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '经过妻子的劝说，\n',
            '我就开始从事导游的工作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4EE(): pass

    label('loc_4EE')

    Jump('loc_6F0')

    def _loc_4F1(): pass

    label('loc_4F1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            Expr.Return,
        ),
        'loc_541',
    )

    ChrTalk(
        0x00FE,
        (
            '我去参观了\n',
            '儿子学校的学园祭。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '正好我休息，\n',
            '我女儿也很高兴。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6F0')

    def _loc_541(): pass

    label('loc_541')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_62B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5CE',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '嗯～下一个工作计划是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……工作繁忙\n',
            '也是件很开心的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只是留守在家里的女儿很寂寞，\n',
            '我有点担心她啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_628')

    def _loc_5CE(): pass

    label('loc_5CE')

    ChrTalk(
        0x00FE,
        (
            '……工作繁忙\n',
            '也是件很开心的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只是留守在家里的女儿很寂寞，\n',
            '我有点担心她啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_628(): pass

    label('loc_628')

    Jump('loc_6F0')

    def _loc_62B(): pass

    label('loc_62B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 0, 0x418)),
            Expr.Return,
        ),
        'loc_6F0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6BD',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '呼，\n',
            '今天的观光客特别多呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '从远方特地来这里\n',
            '观光的人也增加了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '投注在导游工作里的精力\n',
            '比当渔夫的时候还要多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6F0')

    def _loc_6BD(): pass

    label('loc_6BD')

    ChrTalk(
        0x00FE,
        (
            '投注在导游工作里的精力\n',
            '比当渔夫的时候还要多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6F0(): pass

    label('loc_6F0')

    TalkEnd(0x0008)

    Return()

# id: 0x0005 offset: 0x6F4
@scena.Code('func_05_6F4')
def func_05_6F4():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_777',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然新任市长\n',
            '还没有定下来，\n',
            '但我认为诺曼先生不错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果由他来的话，\n',
            '这里作为观光都市\n',
            '一定会飞速向前发展的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B3A')

    def _loc_777(): pass

    label('loc_777')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_8A3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_839',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '布朗西酒店的老板\n',
            '名字叫做诺曼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他是个很有才干的人，\n',
            '买下了一间普通的旅店，\n',
            '改建成现在的酒店了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他和市长也很合得来，\n',
            '在我们的导游工作方面\n',
            '也帮了我们不少忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8A0')

    def _loc_839(): pass

    label('loc_839')

    ChrTalk(
        0x00FE,
        (
            '布朗西酒店的老板\n',
            '名字叫做诺曼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他和市长也很合得来，\n',
            '在我们的导游工作方面\n',
            '也帮了我们不少忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8A0(): pass

    label('loc_8A0')

    Jump('loc_B3A')

    def _loc_8A3(): pass

    label('loc_8A3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            Expr.Return,
        ),
        'loc_94E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_91A',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '那出剧真是杰作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，非常可惜，\n',
            '我儿子没有出场呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '算了，\n',
            '只要他认真念书就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_94B')

    def _loc_91A(): pass

    label('loc_91A')

    ChrTalk(
        0x00FE,
        (
            '我去参观儿子的学园祭了呢。\n',
            '那出剧真是杰作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_94B(): pass

    label('loc_94B')

    Jump('loc_B3A')

    def _loc_94E(): pass

    label('loc_94E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_A26',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_9E2',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '学园祭当天的工作，\n',
            '我准备全部推掉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '之前也给爱蕾塔\n',
            '添了很多麻烦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '什么才是最重要的事情，\n',
            '想来想去还是家庭啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A23')

    def _loc_9E2(): pass

    label('loc_9E2')

    ChrTalk(
        0x00FE,
        (
            '为了家庭\n',
            '而拼命工作的我……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '却恰恰错失了最重要的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A23(): pass

    label('loc_A23')

    Jump('loc_B3A')

    def _loc_A26(): pass

    label('loc_A26')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 0, 0x418)),
            Expr.Return,
        ),
        'loc_B3A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_AD7',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '我们夫妻俩\n',
            '一起在做导游的工作呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我丈夫本来是一个渔夫，\n',
            '但是最近做导游的收入很不错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '自从大儿子进入王立学院念书，\n',
            '家里的开销就大大增加了。 ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B3A')

    def _loc_AD7(): pass

    label('loc_AD7')

    ChrTalk(
        0x00FE,
        (
            '丈夫好像更愿意\n',
            '继续当一个渔夫……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '自从大儿子进入王立学院念书，\n',
            '家里的开销就大大增加了。 ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B3A(): pass

    label('loc_B3A')

    TalkEnd(0x0009)

    Return()

# id: 0x0006 offset: 0xB3E
@scena.Code('func_06_B3E')
def func_06_B3E():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_B86',
    )

    ChrTalk(
        0x00FE,
        (
            '爸爸和妈妈\n',
            '今天都在家，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '能不能陪我好好玩玩呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F2F')

    def _loc_B86(): pass

    label('loc_B86')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_BE8',
    )

    ChrTalk(
        0x00FE,
        (
            '今天爸爸和妈妈都没有工作，\n',
            '在家里休息呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，\n',
            '这下子他们可以陪我好好玩了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F2F')

    def _loc_BE8(): pass

    label('loc_BE8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            Expr.Return,
        ),
        'loc_CC0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C69',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '哥哥的学校有好多摊子，\n',
            '舞台剧也很好看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '提到要去见哥哥，\n',
            '不知怎的，我有点害羞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CBD')

    def _loc_C69(): pass

    label('loc_C69')

    ChrTalk(
        0x00FE,
        (
            '之前，\n',
            '我到哥哥的学校去玩了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '提到要去见哥哥，\n',
            '不知怎的，我有点害羞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_CBD(): pass

    label('loc_CBD')

    Jump('loc_F2F')

    def _loc_CC0(): pass

    label('loc_CC0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_D2F',
    )

    ChrTalk(
        0x00FE,
        (
            '嘿嘿……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这次我们全家\n',
            '都要去哥哥的学校玩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '妈妈也陪我们一起去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，好开心啊⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F2F')

    def _loc_D2F(): pass

    label('loc_D2F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_D89',
    )

    ChrTalk(
        0x00FE,
        (
            '啊啊，终于把衣服洗完，\n',
            '房间也打扫干净了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '希望大家\n',
            '都能早点回来啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F2F')

    def _loc_D89(): pass

    label('loc_D89')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_E1A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_DFF',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '今天是爱蕾塔一个人看家。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '爸爸和妈妈要工作，\n',
            '哥哥去学校上课了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……唉，好寂寞呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E17')

    def _loc_DFF(): pass

    label('loc_DFF')

    ChrTalk(
        0x00FE,
        (
            '……唉，好寂寞呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E17(): pass

    label('loc_E17')

    Jump('loc_F2F')

    def _loc_E1A(): pass

    label('loc_E1A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 0, 0x418)),
            Expr.Return,
        ),
        'loc_EB3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_E7F',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '明天又是\n',
            '我一个人在家啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '爱蕾塔真希望\n',
            '能够早点在主日学校交到朋友。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EB0')

    def _loc_E7F(): pass

    label('loc_E7F')

    ChrTalk(
        0x00FE,
        (
            '爱蕾塔真希望\n',
            '能够早点在主日学校交到朋友……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_EB0(): pass

    label('loc_EB0')

    Jump('loc_F2F')

    def _loc_EB3(): pass

    label('loc_EB3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_F2F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_F10',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '嗯，\n',
            '我终于把该洗的衣服都洗完了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天啊，\n',
            '哥哥来帮我干活了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F2F')

    def _loc_F10(): pass

    label('loc_F10')

    ChrTalk(
        0x00FE,
        (
            '爸爸和妈妈\n',
            '今天也要工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F2F(): pass

    label('loc_F2F')

    TalkEnd(0x000A)

    Return()

# id: 0x0007 offset: 0xF33
@scena.Code('func_07_F33')
def func_07_F33():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 0, 0x418)),
            Expr.Return,
        ),
        'loc_F7F',
    )

    ChrTalk(
        0x00FE,
        (
            '好～\n',
            '明天要上的课已经预习完了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '找点其它事情做吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1033')

    def _loc_F7F(): pass

    label('loc_F7F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_1033',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1006',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '在学校开始上课前，\n',
            '要先做好预习才行……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '把该做的事情做好，\n',
            '才不会引来别人的不满。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这是我的座右铭。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1033')

    def _loc_1006(): pass

    label('loc_1006')

    ChrTalk(
        0x00FE,
        (
            '在学校开始上课前，\n',
            '要先做好预习才行……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1033(): pass

    label('loc_1033')

    TalkEnd(0x000B)

    Return()

# id: 0x0008 offset: 0x1037
@scena.Code('func_08_1037')
def func_08_1037():
    TalkBegin(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_109C',
    )

    ChrTalk(
        0x00FE,
        (
            '戴尔蒙市长竟然\n',
            '做出了这种事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我本以为他还算有些男子汉气概，\n',
            '真是看走眼了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1662')

    def _loc_109C(): pass

    label('loc_109C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_10FC',
    )

    ChrTalk(
        0x00FE,
        (
            '要去王立学院念书的话，\n',
            '是不是要花费很多的米拉？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我妻子她\n',
            '到底想怎么做呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1662')

    def _loc_10FC(): pass

    label('loc_10FC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            Expr.Return,
        ),
        'loc_11F1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1190',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '我是被她\n',
            '强行拉去王立学院的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要进修的话，\n',
            '那里也许是个不错的选择。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，我想还是要\n',
            '看孩子他自己的想法才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11EE')

    def _loc_1190(): pass

    label('loc_1190')

    ChrTalk(
        0x00FE,
        (
            '要进修的话，\n',
            '王立学院也许是个不错的选择。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，我想还是要\n',
            '看孩子他自己的想法才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_11EE(): pass

    label('loc_11EE')

    Jump('loc_1662')

    def _loc_11F1(): pass

    label('loc_11F1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_123E',
    )

    ChrTalk(
        0x00FE,
        (
            '学园祭就是指祭祀典礼吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为什么学校\n',
            '要举行这样的活动呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1662')

    def _loc_123E(): pass

    label('loc_123E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_1384',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_132B',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '虽然调查一下王立学院\n',
            '也没什么损失……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在那之前，\n',
            '不是应该尊重一下孩子的想法吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_12B0')
    def lambda_12B0():
        ChrTurnDirection(0x000D, 0x000C, 1000)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_12B0)

    ChrTalk(
        0x000D,
        (
            '你在说什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_12D0')
    def lambda_12D0():
        ChrTurnDirection(0x000C, 0x000D, 1000)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_12D0)

    OP_62(0x000C, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '没～有，什么都没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_130F')
    def lambda_130F():
        ChrSetDirection(0x000D, 0, 1000)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_130F)

    Sleep(700)

    ChrTalk(
        0x00FE,
        (
            '呼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1381')

    def _loc_132B(): pass

    label('loc_132B')

    ChrTalk(
        0x00FE,
        (
            '虽然调查一下王立学院\n',
            '也没什么损失……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '在那之前，\n',
            '不是应该尊重一下孩子的想法吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1381(): pass

    label('loc_1381')

    Jump('loc_1662')

    def _loc_1384(): pass

    label('loc_1384')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_14FD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1482',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '对于儿子的将来，\n',
            '我又重新考虑过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在我不再强求他，\n',
            '无论他继承我的事业还是去上学，\n',
            '我都会支持他的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只要他有他自己的目标，\n',
            '堂堂正正地活下去，\n',
            '这样就足够了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只是完全把这些事情\n',
            '全都交给他自己，\n',
            '我很难说出口啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_14FA')

    def _loc_1482(): pass

    label('loc_1482')

    ChrTalk(
        0x00FE,
        (
            '只要儿子有自己的目标，\n',
            '堂堂正正地活下去，\n',
            '这样就足够了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只是完全把这些事情\n',
            '全都交给他自己，\n',
            '我很难说出口啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_14FA(): pass

    label('loc_14FA')

    Jump('loc_1662')

    def _loc_14FD(): pass

    label('loc_14FD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 0, 0x418)),
            Expr.Return,
        ),
        'loc_1574',
    )

    ChrTalk(
        0x00FE,
        (
            '我拥有身为船员的骄傲，\n',
            '生活得十分满足。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我觉得不用念什么书，\n',
            '只要活得像个男子汉，\n',
            '也可以生存下去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1662')

    def _loc_1574(): pass

    label('loc_1574')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_1662',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_160C',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '卢安原本就是个\n',
            '船员与渔夫聚集的城市。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是一个云集了\n',
            '在海上生活的男子汉的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我也希望儿子能够\n',
            '做个像样的海上男儿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1662')

    def _loc_160C(): pass

    label('loc_160C')

    ChrTalk(
        0x00FE,
        (
            '卢安原本就是个\n',
            '船员与渔夫聚集的城市。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我也希望儿子能够\n',
            '做个像样的海上男儿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1662(): pass

    label('loc_1662')

    TalkEnd(0x000C)

    Return()

# id: 0x0009 offset: 0x1666
@scena.Code('func_09_1666')
def func_09_1666():
    TalkBegin(0x000D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_16C7',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然市长的事件\n',
            '引起了很大的骚动……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过必须让我的儿子\n',
            '集中精力准备考试。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1BD9')

    def _loc_16C7(): pass

    label('loc_16C7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_17B4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_175D',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '对啊对啊，\n',
            '妮吉塔也是王立学院的学生呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可以去问一下\n',
            '考试到底是什么样的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过去问隔壁的太太\n',
            '总有那么点不太甘心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17B1')

    def _loc_175D(): pass

    label('loc_175D')

    ChrTalk(
        0x00FE,
        (
            '对啊对啊，\n',
            '妮吉塔也是王立学院的学生呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可以去问一下\n',
            '考试到底是什么样的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_17B1(): pass

    label('loc_17B1')

    Jump('loc_1BD9')

    def _loc_17B4(): pass

    label('loc_17B4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            Expr.Return,
        ),
        'loc_18B0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1862',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '我去王立学院侦察过了。\n',
            '不愧是一所名校啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然只是一场学园祭，\n',
            '但是仍让人感到学校优越的氛围啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我要想方设法让托尼奥\n',
            '能够穿上那里的校服。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_18AD')

    def _loc_1862(): pass

    label('loc_1862')

    ChrTalk(
        0x00FE,
        (
            '我去王立学院侦察过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我要想方设法让托尼奥\n',
            '能够穿上那里的校服。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_18AD(): pass

    label('loc_18AD')

    Jump('loc_1BD9')

    def _loc_18B0(): pass

    label('loc_18B0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_1994',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1936',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '最近王立学院要举行学园祭。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这是个好机会，\n',
            '可以让我参观一下孩子将来要上学的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一定要带我去呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1991')

    def _loc_1936(): pass

    label('loc_1936')

    ChrTalk(
        0x00FE,
        (
            '最近王立学院要举行学园祭。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这是个好机会，\n',
            '可以让我参观一下孩子将来要上学的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1991(): pass

    label('loc_1991')

    Jump('loc_1BD9')

    def _loc_1994(): pass

    label('loc_1994')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_1A0A',
    )

    ChrTalk(
        0x00FE,
        (
            '听说希望进入王立学院的人\n',
            '每年都在增加。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因此入学考试\n',
            '也变得越来越难了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对此我真是着急啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1BD9')

    def _loc_1A0A(): pass

    label('loc_1A0A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_1A68',
    )

    ChrTalk(
        0x00FE,
        (
            '王立学院的入学考试\n',
            '果然很难啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '光靠在主日学校学到的东西\n',
            '可远远不够啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1BD9')

    def _loc_1A68(): pass

    label('loc_1A68')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 0, 0x418)),
            Expr.Return,
        ),
        'loc_1B74',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1B2C',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '以孩子他爸的这种陈旧思想，\n',
            '会被周围人甩在后面的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在这个时代，\n',
            '如果不去学校上课可是不行的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '隔壁的基诺奇奥\n',
            '也去学院上学了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们家的孩子可不能输给他。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B71')

    def _loc_1B2C(): pass

    label('loc_1B2C')

    ChrTalk(
        0x00FE,
        (
            '隔壁的基诺奇奥\n',
            '也去学院上学了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们家的孩子可不能输给他。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1B71(): pass

    label('loc_1B71')

    Jump('loc_1BD9')

    def _loc_1B74(): pass

    label('loc_1B74')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_1BD9',
    )

    ChrTurnDirection(0x00FE, 0x0136, 0)

    ChrTalk(
        0x00FE,
        (
            '啊呀，那件制服是……\n',
            '难道你是王立学院的学生？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看上去果然让人感到与众不同呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1BD9(): pass

    label('loc_1BD9')

    TalkEnd(0x000D)

    Return()

# id: 0x000A offset: 0x1BDD
@scena.Code('func_0A_1BDD')
def func_0A_1BDD():
    TalkBegin(0x000E)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_1C15',
    )

    ChrTalk(
        0x00FE,
        (
            '大人们都在议论纷纷的，\n',
            '发生什么事了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_20C4')

    def _loc_1C15(): pass

    label('loc_1C15')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_1C88',
    )

    ChrTalk(
        0x00FE,
        (
            '我想自然系的课程\n',
            '应该和我要成为飞艇乘务员\n',
            '这个梦想相关吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我要试着努力\n',
            '去参加王立学院的考试。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_20C4')

    def _loc_1C88(): pass

    label('loc_1C88')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            Expr.Return,
        ),
        'loc_1CEE',
    )

    ChrTalk(
        0x00FE,
        (
            '我去参观过学园祭了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然我并不是去看\n',
            '那里的上课情况，\n',
            '不过学习的气氛真的很不错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_20C4')

    def _loc_1CEE(): pass

    label('loc_1CEE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_1DB4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1D88',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '总之，\n',
            '我决定去王立学院亲自看一看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，这可不是说我\n',
            '已经决定去参加入学考试了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只是不想让母亲\n',
            '对此事过分热心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1DB1')

    def _loc_1D88(): pass

    label('loc_1D88')

    ChrTalk(
        0x00FE,
        (
            '总之，\n',
            '我决定去王立学院亲自看一看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1DB1(): pass

    label('loc_1DB1')

    Jump('loc_20C4')

    def _loc_1DB4(): pass

    label('loc_1DB4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_1ED6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1E73',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '父亲让我认真考虑一下\n',
            '自己想做的事情是什么。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '然后，我就去调查了一下。\n',
            '要成为飞艇的乘务员之一，\n',
            '我还有许多要努力的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样想的话，\n',
            '去学院念书也并不坏啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1ED3')

    def _loc_1E73(): pass

    label('loc_1E73')

    ChrTalk(
        0x00FE,
        (
            '要成为飞艇的乘务员之一，\n',
            '我还有许多要努力的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样想的话，\n',
            '去学院念书也并不坏啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1ED3(): pass

    label('loc_1ED3')

    Jump('loc_20C4')

    def _loc_1ED6(): pass

    label('loc_1ED6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_1F9B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1F54',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '我想成为\n',
            '定期船的乘务员。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '从小时候开始\n',
            '我就向往这个职业。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这个梦想\n',
            '直至今日仍然没有改变。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F98')

    def _loc_1F54(): pass

    label('loc_1F54')

    ChrTalk(
        0x00FE,
        (
            '我想成为\n',
            '定期船的乘务员。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这个梦想\n',
            '直至今日仍然没有改变。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1F98(): pass

    label('loc_1F98')

    Jump('loc_20C4')

    def _loc_1F9B(): pass

    label('loc_1F9B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 0, 0x418)),
            Expr.Return,
        ),
        'loc_2078',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_204A',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '啊啊～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '父亲来劝我，\n',
            '希望我能够成为船员……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '母亲却要我\n',
            '去杰尼丝王立学院上学。\n',
            '真是好麻烦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我既不想成为船员，\n',
            '也不想去学校念书。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2075')

    def _loc_204A(): pass

    label('loc_204A')

    ChrTalk(
        0x00FE,
        (
            '我既不想成为船员，\n',
            '也不想去学校念书。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2075(): pass

    label('loc_2075')

    Jump('loc_20C4')

    def _loc_2078(): pass

    label('loc_2078')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_20C4',
    )

    ChrTalk(
        0x00FE,
        (
            '我差不多也该决定\n',
            '自己将来的事情了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为我有我想做的工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_20C4(): pass

    label('loc_20C4')

    TalkEnd(0x000E)

    Return()

# id: 0x000B offset: 0x20C8
@scena.Code('func_0B_20C8')
def func_0B_20C8():
    TalkBegin(0x000F)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2121',
    )

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x00FE,
        (
            '好了，\n',
            '我该去港口了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉～\n',
            '港口主任这份工作可不是说着玩的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_214E')

    def _loc_2121(): pass

    label('loc_2121')

    ChrTalk(
        0x00FE,
        (
            '唉～\n',
            '港口主任这份工作可不是说着玩的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_214E(): pass

    label('loc_214E')

    TalkEnd(0x000F)

    Return()

# id: 0x000C offset: 0x2152
@scena.Code('func_0C_2152')
def func_0C_2152():
    TalkBegin(0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_2271',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_221A',
    )

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x00FE,
        (
            '以前都是戴尔蒙家族的人\n',
            '垄断了卢安市市长这个职位。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但下任的选举\n',
            '则打破了这一惯例。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这对想当市长的人来说\n',
            '是次难得的机会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……我的丈夫\n',
            '如果能再加把劲就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_226E')

    def _loc_221A(): pass

    label('loc_221A')

    ChrTalk(
        0x00FE,
        (
            '这对想当市长的人来说\n',
            '是次难得的机会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……我的丈夫\n',
            '如果能再加把劲就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_226E(): pass

    label('loc_226E')

    Jump('loc_2668')

    def _loc_2271(): pass

    label('loc_2271')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            Expr.Return,
        ),
        'loc_23E1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_237B',
    )

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x00FE,
        (
            '最近，\n',
            '我丈夫总是在为很多事情烦恼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '反正又是为了\n',
            '不知道到底该去做哪件事情\n',
            '而迷茫不已吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在这种时候还是\n',
            '我们的儿子比较有魄力……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他就是那样子，\n',
            '不知道什么叫做让步。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '两边权衡一下\n',
            '不是挺好的方法吗，\n',
            '看他这样我都替他着急。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23DE')

    def _loc_237B(): pass

    label('loc_237B')

    ChrTalk(
        0x00FE,
        (
            '最近，\n',
            '我丈夫总是在为很多事情烦恼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '反正又是为了\n',
            '不知道到底该去做哪件事情\n',
            '而迷茫不已吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_23DE(): pass

    label('loc_23DE')

    Jump('loc_2668')

    def _loc_23E1(): pass

    label('loc_23E1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_2504',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_249B',
    )

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x00FE,
        (
            '说起来，我儿子学校的学园祭\n',
            '应该马上就要到了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，那家伙……\n',
            '听说我们要去学校就生气了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是的，这个年纪的孩子，\n',
            '不管是男孩还是女孩都很难管教啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2501')

    def _loc_249B(): pass

    label('loc_249B')

    ChrTalk(
        0x00FE,
        (
            '说起来，我儿子学校的学园祭\n',
            '应该马上就要到了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，那家伙……\n',
            '听说我们要去学校就生气了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2501(): pass

    label('loc_2501')

    Jump('loc_2668')

    def _loc_2504(): pass

    label('loc_2504')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_255A',
    )

    ChrTalk(
        0x00FE,
        (
            '啊啊，\n',
            '我明明打算要在桥起吊之前去买东西的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可恶……\n',
            '完全忘记了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2668')

    def _loc_255A(): pass

    label('loc_255A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_25D7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_25B3',
    )

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x00FE,
        (
            '丈夫去工作，\n',
            '儿子也去上学了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好吧～\n',
            '赶快把家务都做完吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_25D4')

    def _loc_25B3(): pass

    label('loc_25B3')

    ChrTalk(
        0x00FE,
        (
            '好吧～\n',
            '赶快把家务都做完吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_25D4(): pass

    label('loc_25D4')

    Jump('loc_2668')

    def _loc_25D7(): pass

    label('loc_25D7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 4, 0x414)),
            Expr.Return,
        ),
        'loc_2668',
    )

    ChrTalk(
        0x00FE,
        (
            '我的老公\n',
            '是港口的负责人，\n',
            '但他好像没什么干劲……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '既然他受到大家的信任，\n',
            '在市民间也非常有威望，\n',
            '为什么不能表现地更加凛然一点呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2668(): pass

    label('loc_2668')

    TalkEnd(0x0010)

    Return()

# id: 0x000D offset: 0x266C
@scena.Code('func_0D_266C')
def func_0D_266C():
    TalkBegin(0x0011)

    ChrTalk(
        0x00FE,
        (
            '啊，\n',
            '父亲放着我不管\n',
            '既有好处也有坏处。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '母亲也说\n',
            '这是没办法的事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0011)

    Return()

# id: 0x000E offset: 0x26C0
@scena.Code('func_0E_26C0')
def func_0E_26C0():
    TalkBegin(0x0012)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_27D6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2771',
    )

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    ChrTalk(
        0x00FE,
        (
            '这次的事件真让人遗憾，\n',
            '身为市长怎么能误入歧途呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '既然市长已经犯下了错误，\n',
            '让卢安繁荣发展的宗旨\n',
            '谁又能够继承下去呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔……………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_27D3')

    def _loc_2771(): pass

    label('loc_2771')

    ChrTalk(
        0x00FE,
        (
            '既然市长已经犯下了错误，\n',
            '让卢安繁荣发展的宗旨\n',
            '谁又能够继承下去呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔……………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_27D3(): pass

    label('loc_27D3')

    Jump('loc_2C65')

    def _loc_27D6(): pass

    label('loc_27D6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_2917',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2897',
    )

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    ChrTalk(
        0x00FE,
        (
            '卢安的改变果然还是从\n',
            '定期船通航后开始的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '前些天，定期船停航的时候，\n',
            '旅客们一个接一个地来退票。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎呀，可以说定期船\n',
            '对于卢安来说已经是\n',
            '一个不可或缺的存在了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2914')

    def _loc_2897(): pass

    label('loc_2897')

    ChrTalk(
        0x00FE,
        (
            '前些天，定期船停航的时候，\n',
            '旅客们一个接一个地来退票。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎呀，可以说定期船\n',
            '对于卢安来说已经是\n',
            '一个不可或缺的存在了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2914(): pass

    label('loc_2914')

    Jump('loc_2C65')

    def _loc_2917(): pass

    label('loc_2917')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_2988',
    )

    ChrTalk(
        0x00FE,
        (
            '说不定能把\n',
            '王立学院的学园祭\n',
            '作为季节限定的旅行计划呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，明年这个时候\n',
            '就这样计划试试看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2C65')

    def _loc_2988(): pass

    label('loc_2988')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_2A20',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_29F6',
    )

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    ChrTalk(
        0x00FE,
        (
            '港口的那些流氓\n',
            '真得让我很头疼啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '给观光客留下\n',
            '不愉快的印象\n',
            '也不是一次两次了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A1D')

    def _loc_29F6(): pass

    label('loc_29F6')

    ChrTalk(
        0x00FE,
        (
            '……真是的，\n',
            '那些混蛋真让人烦恼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2A1D(): pass

    label('loc_2A1D')

    Jump('loc_2C65')

    def _loc_2A20(): pass

    label('loc_2A20')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_2B51',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2AFF',
    )

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    ChrTalk(
        0x00FE,
        (
            '最近的卢安\n',
            '正在渐渐向\n',
            '观光城市转变。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对于我来说，\n',
            '现在正是个好机会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我准备了许多观光计划，\n',
            '不止是利贝尔各地的客人，\n',
            '国外的旅客也是我的招揽对象。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我非常赞成市长\n',
            '要振兴观光业的方针。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2B4E')

    def _loc_2AFF(): pass

    label('loc_2AFF')

    ChrTalk(
        0x00FE,
        (
            '最近的卢安\n',
            '正在渐渐向\n',
            '观光城市转变。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对于我来说，\n',
            '现在正是个好机会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2B4E(): pass

    label('loc_2B4E')

    Jump('loc_2C65')

    def _loc_2B51(): pass

    label('loc_2B51')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 4, 0x414)),
            Expr.Return,
        ),
        'loc_2C65',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2BFA',
    )

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    ChrTalk(
        0x00FE,
        (
            '我以卢安为中心\n',
            '经营观光业和酒店业。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵，\n',
            '最近建成的布朗西酒店\n',
            '受到观光客的不少好评。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '特别是顶楼那套别致的套房\n',
            '是我最最骄傲的杰作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2C65')

    def _loc_2BFA(): pass

    label('loc_2BFA')

    ChrTalk(
        0x00FE,
        (
            '呵呵，\n',
            '最近建成的布朗西酒店\n',
            '受到观光客的不少好评。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '特别是顶楼那套别致的套房\n',
            '是我最最骄傲的杰作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2C65(): pass

    label('loc_2C65')

    TalkEnd(0x0012)

    Return()

# id: 0x000F offset: 0x2C69
@scena.Code('func_0F_2C69')
def func_0F_2C69():
    TalkBegin(0x0013)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_2CCE',
    )

    ChrTalk(
        0x00FE,
        (
            '市长先生竟然做了\n',
            '那么过分的事………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我刚来的时候还以为\n',
            '他是个很伟大的人呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2EF4')

    def _loc_2CCE(): pass

    label('loc_2CCE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_2D2C',
    )

    ChrTalk(
        0x00FE,
        (
            '我也知道\n',
            '丈夫工作非常繁忙……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是我还是很希望他\n',
            '能多点机会和孩子们接触。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2EF4')

    def _loc_2D2C(): pass

    label('loc_2D2C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_2D8C',
    )

    ChrTalk(
        0x00FE,
        (
            '我也想让自家的长子\n',
            '去王立学院上学……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是他本人不想去的话，\n',
            '我们也没办法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2EF4')

    def _loc_2D8C(): pass

    label('loc_2D8C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_2E34',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2E0C',
    )

    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    ChrTalk(
        0x00FE,
        (
            '我们家还有\n',
            '另外一个儿子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为某些原因，\n',
            '他现在不住在这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那个孩子，\n',
            '有没有好好吃饭呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2E31')

    def _loc_2E0C(): pass

    label('loc_2E0C')

    ChrTalk(
        0x00FE,
        (
            '那个孩子，\n',
            '有没有好好吃饭呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2E31(): pass

    label('loc_2E31')

    Jump('loc_2EF4')

    def _loc_2E34(): pass

    label('loc_2E34')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_2EA3',
    )

    ChrTalk(
        0x00FE,
        (
            '路易真是个\n',
            '会乱来的孩子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '脑子里一想到什么事情，\n',
            '就会立刻去亲自实践一下，\n',
            '否则就安不下心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2EF4')

    def _loc_2EA3(): pass

    label('loc_2EA3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 4, 0x414)),
            Expr.Return,
        ),
        'loc_2EF4',
    )

    ChrTalk(
        0x00FE,
        (
            '我丈夫\n',
            '非常热衷于工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我还是担心他会不会\n',
            '因为工作过度而倒下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2EF4(): pass

    label('loc_2EF4')

    TalkEnd(0x0013)

    Return()

# id: 0x0010 offset: 0x2EF8
@scena.Code('func_10_2EF8')
def func_10_2EF8():
    TalkBegin(0x0014)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_2F53',
    )

    ChrTalk(
        0x00FE,
        (
            '哥哥回来了，\n',
            '但爸爸不让他进家门。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为什么爸爸总是\n',
            '对哥哥那么冷淡呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_30D9')

    def _loc_2F53(): pass

    label('loc_2F53')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_3020',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2FD3',
    )

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    ChrTalk(
        0x00FE,
        (
            '我的哥哥\n',
            '经常呆在港口那边。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，\n',
            '爸爸说我不可以跑过去找他玩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哼，\n',
            '爸爸他自己又不陪我玩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_301D')

    def _loc_2FD3(): pass

    label('loc_2FD3')

    ChrTalk(
        0x00FE,
        (
            '我的哥哥\n',
            '经常呆在港口那边。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，\n',
            '爸爸说我不可以跑过去找他玩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_301D(): pass

    label('loc_301D')

    Jump('loc_30D9')

    def _loc_3020(): pass

    label('loc_3020')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_304D',
    )

    ChrTalk(
        0x00FE,
        (
            '啊～啊，\n',
            '我好想去找哥哥玩啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_30D9')

    def _loc_304D(): pass

    label('loc_304D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_3071',
    )

    ChrTalk(
        0x00FE,
        (
            '妈妈～我肚子饿了～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_30D9')

    def _loc_3071(): pass

    label('loc_3071')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_30AC',
    )

    ChrTalk(
        0x00FE,
        (
            '前几天，我把爸爸的表给拆了，\n',
            '被他骂了一顿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_30D9')

    def _loc_30AC(): pass

    label('loc_30AC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 4, 0x414)),
            Expr.Return,
        ),
        'loc_30D9',
    )

    ChrTalk(
        0x00FE,
        (
            '爸爸他啊～\n',
            '一天到晚都在工作…… ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_30D9(): pass

    label('loc_30D9')

    TalkEnd(0x0014)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
