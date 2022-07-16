import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T4120_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4120   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '卡露娜'),
    TXT(0x02, '史帕德'),
    TXT(0x03, '夏伊'),
    TXT(0x04, '塞森'),
    TXT(0x05, '多姆'),
    TXT(0x06, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4120.x'
    header.mapIndex       = 1
    header.bgm            = 14
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x26BE
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
        ('ED6_DT07/CH01240._CH', 'ED6_DT07/CH01240P._CP'),
        ('ED6_DT07/CH01680._CH', 'ED6_DT07/CH01680P._CP'),
        ('ED6_DT07/CH01690._CH', 'ED6_DT07/CH01690P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
    ]

# id: 0x10002 offset: 0xD2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            x                   = -1540,
            z                   = 0,
            y                   = 69240,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            x                   = 1260,
            z                   = 0,
            y                   = -240,
            direction           = 236,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            x                   = 58580,
            z                   = 0,
            y                   = 360,
            direction           = 102,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            x                   = 120030,
            z                   = 0,
            y                   = -1260,
            direction           = 10,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
    )

# id: 0x10003 offset: 0x172
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x172
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x172
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -10,
            triggerZ            = 0,
            triggerY            = -1600,
            triggerRange        = 800,
            actorX              = 1260,
            actorZ              = 1500,
            actorY              = -240,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 60410,
            triggerZ            = 0,
            triggerY            = 390,
            triggerRange        = 800,
            actorX              = 58580,
            actorZ              = 1500,
            actorY              = 360,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 119960,
            triggerZ            = 0,
            triggerY            = 650,
            triggerRange        = 800,
            actorX              = 120030,
            actorZ              = 1500,
            actorY              = -1260,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x1DE
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 3, 0x64B)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_200',
    )

    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, 5480, 4000, -2590, 90)

    def _loc_200(): pass

    label('loc_200')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_20A',
    )

    Jump('loc_27C')

    def _loc_20A(): pass

    label('loc_20A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_214',
    )

    Jump('loc_27C')

    def _loc_214(): pass

    label('loc_214')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_21E',
    )

    Jump('loc_27C')

    def _loc_21E(): pass

    label('loc_21E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_228',
    )

    Jump('loc_27C')

    def _loc_228(): pass

    label('loc_228')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_232',
    )

    Jump('loc_27C')

    def _loc_232(): pass

    label('loc_232')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_23C',
    )

    Jump('loc_27C')

    def _loc_23C(): pass

    label('loc_23C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_246',
    )

    Jump('loc_27C')

    def _loc_246(): pass

    label('loc_246')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_250',
    )

    Jump('loc_27C')

    def _loc_250(): pass

    label('loc_250')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_26B',
    )

    SetChrPos(0x0009, 3310, 0, 129900, 0)

    Jump('loc_27C')

    def _loc_26B(): pass

    label('loc_26B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_275',
    )

    Jump('loc_27C')

    def _loc_275(): pass

    label('loc_275')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_27C',
    )

    def _loc_27C(): pass

    label('loc_27C')

    Return()

# id: 0x0001 offset: 0x27D
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 1, 0x631)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 3, 0x623)),
            Expr.Or,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 3, 0x61B)),
            Expr.Or,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 6, 0x616)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2B0',
    )

    OP_B1('t4120_y')

    Jump('loc_2B9')

    def _loc_2B0(): pass

    label('loc_2B0')

    OP_B1('t4120_n')

    def _loc_2B9(): pass

    label('loc_2B9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 2, 0x66A)),
            Expr.Return,
        ),
        'loc_2C9',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x4B),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2C9(): pass

    label('loc_2C9')

    Return()

# id: 0x0002 offset: 0x2CA
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_2DF',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_2DF(): pass

    label('loc_2DF')

    Return()

# id: 0x0003 offset: 0x2E0
@scena.Code('func_03_2E0')
def func_03_2E0():
    Call(0, 0x0004)

    Return()

# id: 0x0004 offset: 0x2E5
@scena.Code('func_04_2E5')
def func_04_2E5():
    TalkBegin(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_340',
    )

    ChrTalk(
        0x000C,
        (
            '今天天气不错啊，\n',
            '和诞辰庆典很合称呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '好的，\n',
            '今天的工作也要加油干。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9DB')

    def _loc_340(): pass

    label('loc_340')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_385',
    )

    ChrTalk(
        0x000C,
        (
            '今天的顾客\n',
            '为何减少了许多呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '发生什么事了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9DB')

    def _loc_385(): pass

    label('loc_385')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_405',
    )

    ChrTalk(
        0x000C,
        (
            '必须重视客户的想法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '如果客户有急需，\n',
            '就算已经下班了也要接受维修委托。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '我要把这些想法\n',
            '和塞森交流一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9DB')

    def _loc_405(): pass

    label('loc_405')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_467',
    )

    ChrTalk(
        0x000C,
        (
            '马上就要关店了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '不过，\n',
            '修理的委托还是要尽快完成，\n',
            '然后把东西交还给客人才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9DB')

    def _loc_467(): pass

    label('loc_467')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_4D2',
    )

    ChrTalk(
        0x000C,
        (
            '今天好像是武术大会的决赛日啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '在客人都去看比赛的这段时间，\n',
            '我一定要把东西修理好才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9DB')

    def _loc_4D2(): pass

    label('loc_4D2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_598',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_511',
    )

    ChrTalk(
        0x000C,
        (
            '好像就连空贼\n',
            '都参加比赛了，\n',
            '这样好吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_595')

    def _loc_511(): pass

    label('loc_511')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x000C,
        (
            '武术大会\n',
            '似乎相当热闹。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '刚才，\n',
            '来取商品的客人\n',
            '都在和我兴奋地谈论这件事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '好像就连空贼\n',
            '都参加比赛了，\n',
            '这样好吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_595(): pass

    label('loc_595')

    Jump('loc_9DB')

    def _loc_598(): pass

    label('loc_598')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_6A2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_5E9',
    )

    ChrTalk(
        0x000C,
        (
            '对于我来说，\n',
            '能用自己的技术帮助顾客，\n',
            '那就是最快乐的事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_69F')

    def _loc_5E9(): pass

    label('loc_5E9')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x000C,
        (
            '对于我来说，\n',
            '能用自己的技术帮助顾客，\n',
            '那就是最快乐的事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '老爷爷爱惜了\n',
            '一辈子的时钟，\n',
            '孩子们心爱的玩具……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '每当修理好那些东西时，\n',
            '他们绽放出的笑颜是我最想看到的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_69F(): pass

    label('loc_69F')

    Jump('loc_9DB')

    def _loc_6A2(): pass

    label('loc_6A2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_7A2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_711',
    )

    ChrTalk(
        0x000C,
        (
            '本店销售的商品\n',
            '当然会给您保修……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '就算不是在本店买的商品，\n',
            '出问题了也可以拿来修理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_79F')

    def _loc_711(): pass

    label('loc_711')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x000C,
        (
            '我会尽量根据顾客的意见\n',
            '来满足他们的要求。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '对销售的商品\n',
            '进行修理和维护……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '就算不是在本店买的商品，\n',
            '出问题了也可以拿来修理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_79F(): pass

    label('loc_79F')

    Jump('loc_9DB')

    def _loc_7A2(): pass

    label('loc_7A2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_875',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_804',
    )

    ChrTalk(
        0x000C,
        (
            '虽然我很想去看武术大会，\n',
            '但还有修理的任务要做。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '要优先处理顾客的委托。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_872')

    def _loc_804(): pass

    label('loc_804')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x000C,
        (
            '今天开始大会就进入正式赛了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '虽然我很想去看，\n',
            '但还有修理的任务要做。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '要优先处理顾客的委托。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_872(): pass

    label('loc_872')

    Jump('loc_9DB')

    def _loc_875(): pass

    label('loc_875')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_925',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_8B3',
    )

    ChrTalk(
        0x000C,
        (
            '我还以为今年的武术大会\n',
            '肯定要取消呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_922')

    def _loc_8B3(): pass

    label('loc_8B3')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x000C,
        (
            '政变的混乱和女王陛下的卧病在床\n',
            '好像并没有带来太大的影响。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '我还以为今年的武术大会\n',
            '肯定要取消呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_922(): pass

    label('loc_922')

    Jump('loc_9DB')

    def _loc_925(): pass

    label('loc_925')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_9DB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_97C',
    )

    ChrTalk(
        0x000C,
        (
            '这个『文加尔德工房』的三楼\n',
            '是负责修理和维护的地方。\n',
            '请好好利用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9DB')

    def _loc_97C(): pass

    label('loc_97C')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x000C,
        (
            '您好，欢迎光临。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '这个『文加尔德工房』的三楼\n',
            '是负责修理和维护的地方。\n',
            '请好好利用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9DB(): pass

    label('loc_9DB')

    TalkEnd(0x000C)

    Return()

# id: 0x0005 offset: 0x9DF
@scena.Code('func_05_9DF')
def func_05_9DF():
    Call(0, 0x0006)

    Return()

# id: 0x0006 offset: 0x9E4
@scena.Code('func_06_9E4')
def func_06_9E4():
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
            TXT(0x01, '改造·换钱\n'),
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
        'loc_A46',
    )

    OP_0D()
    OP_A9(0x5A)
    OP_56(0x00)
    TalkEnd(0x000B)

    Return()

    def _loc_A46(): pass

    label('loc_A46')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A57',
    )

    TalkEnd(0x000B)

    Return()

    def _loc_A57(): pass

    label('loc_A57')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_B17',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_A91',
    )

    ChrTalk(
        0x000B,
        (
            '女王陛下的病好了，\n',
            '让人非常欣慰啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B14')

    def _loc_A91(): pass

    label('loc_A91')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x000B,
        (
            '街上一热闹，这里的客人也会增加。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '诞辰庆典的销售额\n',
            '应该会比平常高出五倍以上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '女王陛下的病好了，\n',
            '让人非常欣慰啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B14(): pass

    label('loc_B14')

    Jump('loc_12C1')

    def _loc_B17(): pass

    label('loc_B17')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_B7E',
    )

    ChrTalk(
        0x000B,
        (
            '王国军为了\n',
            '防止政变而加强了警戒，\n',
            '所以顾客减少了很多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '真是的……\n',
            '没想到会这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12C1')

    def _loc_B7E(): pass

    label('loc_B7E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_C3E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_BCA',
    )

    ChrTalk(
        0x000B,
        (
            '希望这种势头能持续到诞辰庆典，\n',
            '这样就可以大赚特赚了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C3B')

    def _loc_BCA(): pass

    label('loc_BCA')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x000B,
        (
            '哎呀，武术大会期间，\n',
            '每天的营业额相当可观啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '希望这种势头能持续到诞辰庆典，\n',
            '这样就可以大赚特赚了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C3B(): pass

    label('loc_C3B')

    Jump('loc_12C1')

    def _loc_C3E(): pass

    label('loc_C3E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_C9A',
    )

    ChrTalk(
        0x000B,
        (
            '好了，\n',
            '差不多该关店门了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '今天赚了多少钱呢？\n',
            '我已经迫不及待要去结算了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12C1')

    def _loc_C9A(): pass

    label('loc_C9A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_DD6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_D26',
    )

    ChrTalk(
        0x000B,
        (
            '请你们使用我们店里的结晶回路\n',
            '来获得最后的胜利吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '这样的话，\n',
            '本店既能赚钱又能得到宣传，\n',
            '真可谓是一举两得的妙计。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DD3')

    def _loc_D26(): pass

    label('loc_D26')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x000B,
        (
            '你们不就是要出战\n',
            '今天总决赛的游击士组吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '那么就使用我们店里的结晶回路\n',
            '来获得最后的胜利吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '这样的话，\n',
            '本店既能赚钱又能得到宣传，\n',
            '真可谓是一举两得的妙计。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_DD3(): pass

    label('loc_DD3')

    Jump('loc_12C1')

    def _loc_DD6(): pass

    label('loc_DD6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_E6C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_E14',
    )

    ChrTalk(
        0x000B,
        (
            '对我而言，\n',
            '最期待的还是明天能赚多少钱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E69')

    def _loc_E14(): pass

    label('loc_E14')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x000B,
        (
            '虽然很想知道谁会取胜，\n',
            '不过……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '对我而言，\n',
            '最期待的还是明天能赚多少钱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E69(): pass

    label('loc_E69')

    Jump('loc_12C1')

    def _loc_E6C(): pass

    label('loc_E6C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_F49',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_ECF',
    )

    ChrTalk(
        0x000B,
        (
            '这家店是我和从小长大的\n',
            '好友多姆一同经营的，\n',
            '不过工作上的想法总是合不到一起。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F46')

    def _loc_ECF(): pass

    label('loc_ECF')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x000B,
        (
            '这家店是我和从小长大的\n',
            '好友多姆一同经营的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '那家伙很有本事哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '不过，作为同事而言\n',
            '就不是那么投缘了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F46(): pass

    label('loc_F46')

    Jump('loc_12C1')

    def _loc_F49(): pass

    label('loc_F49')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_1038',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_FAE',
    )

    ChrTalk(
        0x000B,
        (
            '武术大会期间，\n',
            '大部分委托都是修理和改造。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '还是新商品的销售\n',
            '更能够盈利啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1035')

    def _loc_FAE(): pass

    label('loc_FAE')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x000B,
        (
            '虽说武术大会\n',
            '带来了很多顾客……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '但实际上，\n',
            '大部分人主要是来\n',
            '委托我们进行修理和改造。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '还是新商品的销售\n',
            '更能够盈利啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1035(): pass

    label('loc_1035')

    Jump('loc_12C1')

    def _loc_1038(): pass

    label('loc_1038')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_1145',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_109C',
    )

    ChrTalk(
        0x000B,
        (
            '一定要用我们的结晶回路\n',
            '作为武器去获得胜利。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '这样对本店也是个很好的宣传。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1142')

    def _loc_109C(): pass

    label('loc_109C')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x000B,
        (
            '难道说你们要\n',
            '在武术大会当中出场吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '我正准备关门，\n',
            '去竞技场观战呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '请一定要用我们的结晶回路\n',
            '作为武器去获得胜利。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '这样对本店也是个很好的宣传。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1142(): pass

    label('loc_1142')

    Jump('loc_12C1')

    def _loc_1145(): pass

    label('loc_1145')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_11BB',
    )

    ChrTalk(
        0x000B,
        (
            '由于没有亲卫队来关照，\n',
            '这里的生意都开始萧条了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '他们怎么会去做发动政变这种\n',
            '毫无价值可言的事情呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12C1')

    def _loc_11BB(): pass

    label('loc_11BB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_12C1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1230',
    )

    ChrTalk(
        0x000B,
        (
            '导力器的相关事宜一定要\n',
            '交给我们『文加尔德工房』来处理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '相信我准没错，\n',
            '不会让你们失望的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12C1')

    def _loc_1230(): pass

    label('loc_1230')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x000B,
        (
            '哦，你们是游击士吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '如果是的话，导力器的相关事宜一定要\n',
            '交给我们『文加尔德工房』来处理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '相信我准没错，\n',
            '这里不会让你们失望的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_12C1(): pass

    label('loc_12C1')

    TalkEnd(0x000B)

    Return()

# id: 0x0007 offset: 0x12C5
@scena.Code('func_07_12C5')
def func_07_12C5():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_12F3',
    )

    ChrTalk(
        0x00FE,
        (
            '今天外面\n',
            '实在是很热闹啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1741')

    def _loc_12F3(): pass

    label('loc_12F3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_1359',
    )

    ChrTalk(
        0x00FE,
        (
            '我刚才在外面看到了……\n',
            '那些黑衣士兵也是王国军吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是令人感到\n',
            '可怕的一群家伙……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1741')

    def _loc_1359(): pass

    label('loc_1359')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_139B',
    )

    ChrTalk(
        0x00FE,
        (
            '……武术大会\n',
            '才刚刚结束，\n',
            '街上也太过太安静些了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1741')

    def _loc_139B(): pass

    label('loc_139B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_13F2',
    )

    ChrTalk(
        0x00FE,
        (
            '……大会结束了，\n',
            '店里也稍微冷清了些。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天好像可以悠闲一会儿了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1741')

    def _loc_13F2(): pass

    label('loc_13F2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_1480',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_1428',
    )

    ChrTalk(
        0x00FE,
        (
            '我也想让\n',
            '自己的口才变好一些……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_147D')

    def _loc_1428(): pass

    label('loc_1428')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '唉，我也想让\n',
            '自己的口才变好一些……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总是不知道\n',
            '在别人面前说什么才好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_147D(): pass

    label('loc_147D')

    Jump('loc_1741')

    def _loc_1480(): pass

    label('loc_1480')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_14CF',
    )

    ChrTalk(
        0x00FE,
        (
            '明天要和妻子一起外出了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天就把这里的事情\n',
            '全部摆平吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1741')

    def _loc_14CF(): pass

    label('loc_14CF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_15A2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_153A',
    )

    ChrTalk(
        0x00FE,
        (
            '唔～\n',
            '现在商品的数量已经足够了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有这么多库存的话，\n',
            '撑到诞辰庆典结束应该没问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_159F')

    def _loc_153A(): pass

    label('loc_153A')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '……前几天来的那些戴手铐的人，\n',
            '好像也是大赛选手呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没想到他们竟然是\n',
            '柏斯事件的犯人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_159F(): pass

    label('loc_159F')

    Jump('loc_1741')

    def _loc_15A2(): pass

    label('loc_15A2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_15FE',
    )

    ChrTalk(
        0x00FE,
        (
            '大会开始以后，\n',
            '就会有许多选手前来光顾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以要在大会前\n',
            '进一些好装备……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1741')

    def _loc_15FE(): pass

    label('loc_15FE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_1672',
    )

    ChrTalk(
        0x00FE,
        (
            '得去进一些\n',
            '导力炮和导力枪了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '昨天来的客人\n',
            '买了不少这类的武器……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '让本店的库存都清空了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1741')

    def _loc_1672(): pass

    label('loc_1672')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_169F',
    )

    ChrTalk(
        0x00FE,
        (
            '……欢迎光临，\n',
            '请随便看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1741')

    def _loc_169F(): pass

    label('loc_169F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_1741',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_16ED',
    )

    ChrTalk(
        0x00FE,
        (
            '我不太会接待客人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最近店铺都是\n',
            '交给妻子打理的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1741')

    def _loc_16ED(): pass

    label('loc_16ED')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '……欢迎光临。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我不太会接待客人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最近店铺都是\n',
            '交给妻子打理的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1741(): pass

    label('loc_1741')

    TalkEnd(0x00FE)

    Return()

# id: 0x0008 offset: 0x1745
@scena.Code('func_08_1745')
def func_08_1745():
    Call(0, 0x0009)

    Return()

# id: 0x0009 offset: 0x174A
@scena.Code('func_09_174A')
def func_09_174A():
    TalkBegin(0x000A)
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
        'loc_17B4',
    )

    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_17AC',
    )

    OP_A9(0x60)

    Jump('loc_17AE')

    def _loc_17AC(): pass

    label('loc_17AC')

    OP_A9(0x5B)

    def _loc_17AE(): pass

    label('loc_17AE')

    OP_56(0x00)
    TalkEnd(0x000A)

    Return()

    def _loc_17B4(): pass

    label('loc_17B4')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_17C5',
    )

    TalkEnd(0x000A)

    Return()

    def _loc_17C5(): pass

    label('loc_17C5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_18B0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CF, 2, 0x67A)),
            Expr.Return,
        ),
        'loc_182B',
    )

    ChrTalk(
        0x000A,
        (
            '女王陛下的病治好了，\n',
            '真是太令人欣慰了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '这样一来利贝尔就可以国泰民安了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_18AD')

    def _loc_182B(): pass

    label('loc_182B')

    ChrTalk(
        0x000A,
        (
            '女王陛下和科洛蒂娅公主\n',
            '真是气质优雅啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '女王陛下的病治好了，\n',
            '真是太令人欣慰了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '这样一来利贝尔就可以国泰民安了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_18AD(): pass

    label('loc_18AD')

    Jump('loc_2316')

    def _loc_18B0(): pass

    label('loc_18B0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_18F2',
    )

    ChrTalk(
        0x000A,
        (
            '今天的天气\n',
            '虽然一点都不差，\n',
            '但却没有什么顾客啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2316')

    def _loc_18F2(): pass

    label('loc_18F2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_19B9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CF, 2, 0x67A)),
            Expr.Return,
        ),
        'loc_193C',
    )

    ChrTalk(
        0x000A,
        (
            '据说女王陛下也是有病在身，\n',
            '诞辰庆典到底会怎么样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19B6')

    def _loc_193C(): pass

    label('loc_193C')

    ChrTalk(
        0x000A,
        (
            '最近在街上经常能够\n',
            '见到穿黑衣服的士兵。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '兵荒马乱啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '据说女王陛下也是有病在身，\n',
            '诞辰庆典到底会怎么样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_19B6(): pass

    label('loc_19B6')

    Jump('loc_2316')

    def _loc_19B9(): pass

    label('loc_19B9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_1B7D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CF, 2, 0x67A)),
            Expr.Return,
        ),
        'loc_1ACC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_1A2B',
    )

    ChrTalk(
        0x000A,
        (
            '真是这几年里\n',
            '难得一见的激战啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '我真是太感动了。\n',
            '我已经完全成为你们的支持者了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AC9')

    def _loc_1A2B(): pass

    label('loc_1A2B')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x000A,
        (
            '你们干得太棒啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '恭喜你们获得优胜。\n',
            '比赛很精彩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '真是这几年里\n',
            '难得一见的激战啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '啊～我太感动了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '我已经完全\n',
            '成为你们的支持者了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1AC9(): pass

    label('loc_1AC9')

    Jump('loc_1B7A')

    def _loc_1ACC(): pass

    label('loc_1ACC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_1B15',
    )

    ChrTalk(
        0x000A,
        (
            '今天的决赛很精彩呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '没有工作\n',
            '而去观看比赛真是值得。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B7A')

    def _loc_1B15(): pass

    label('loc_1B15')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x000A,
        (
            '今天的决赛很精彩呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '我想是这几年里\n',
            '最棒的比赛了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '没有工作\n',
            '而去观看比赛真是值得。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1B7A(): pass

    label('loc_1B7A')

    Jump('loc_2316')

    def _loc_1B7D(): pass

    label('loc_1B7D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_1C2C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CF, 2, 0x67A)),
            Expr.Return,
        ),
        'loc_1BE6',
    )

    ChrTalk(
        0x000A,
        (
            '啊，是你们……\n',
            '今天终于要进行决赛了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '我们一会儿就暂停营业\n',
            '去赛场给你们加油！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C29')

    def _loc_1BE6(): pass

    label('loc_1BE6')

    ChrTalk(
        0x000A,
        (
            '今天是大会的第二天呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '啊啊，\n',
            '我也想到大会现场去看看呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C29(): pass

    label('loc_1C29')

    Jump('loc_2316')

    def _loc_1C2C(): pass

    label('loc_1C2C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_1E2C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_1C68',
    )

    ChrTalk(
        0x000A,
        (
            '为了明天的决赛，\n',
            '你们今天要好好休息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E29')

    def _loc_1C68(): pass

    label('loc_1C68')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CF, 2, 0x67A)),
            (Expr.TestScenaFlags, ScenaFlag(0x00CF, 3, 0x67B)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1DD8',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    SetScenaFlags(ScenaFlag(0x00CF, 3, 0x67B))

    ChrTalk(
        0x000A,
        (
            '啊，你们是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '干得真不错！\n',
            '恭喜你们进入决赛！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#001F嗯，谢谢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F谢谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '今天的比赛\n',
            '真是白热化呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '作为你们的支持者，我也很自豪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#006F嘿嘿，\n',
            '总算战胜了游击士前辈们，\n',
            '这样离冠军就是一步之遥了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#018F（又立刻得意忘形起来了……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '嗯嗯，已经到这一步了，\n',
            '就一定要取得优胜啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '总之，你们一定要加油！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E29')

    def _loc_1DD8(): pass

    label('loc_1DD8')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x000A,
        (
            '今天比赛的看点\n',
            '好像非常多呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '从街道上沸腾的气氛中\n',
            '就可以感觉得到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1E29(): pass

    label('loc_1E29')

    Jump('loc_2316')

    def _loc_1E2C(): pass

    label('loc_1E2C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_207E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CF, 2, 0x67A)),
            Expr.Return,
        ),
        'loc_1E7F',
    )

    ChrTalk(
        0x000A,
        (
            '我决定决赛那天\n',
            '歇业去看比赛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '为了晋级决赛，\n',
            '要加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_207B')

    def _loc_1E7F(): pass

    label('loc_1E7F')

    SetScenaFlags(ScenaFlag(0x00CF, 2, 0x67A))

    ChrTalk(
        0x000A,
        (
            '啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '莫非你们是\n',
            '武术大会的选手？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#073F唔，是啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '啊，果然！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '就是传说中的那个由壮汉、\n',
            '少年、还有少女组成的队伍。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '我决定今年\n',
            '替你们加油啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#008F哈、哈哈，\n',
            '真是非常感谢啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '嗯嗯，\n',
            '那么我想要你们的签名可以吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#004F签、签名！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#019F总觉得有点难为情……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '因为平时要看店，\n',
            '不能去竞技场呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '我决定决赛那天\n',
            '歇业去看比赛哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '你们请一定要努力。\n',
            '一定要让我看到\n',
            '你们的精彩比赛啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#001F嗯，虽说选手中高手如云，\n',
            '但我们保证一定会全力以赴的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_207B(): pass

    label('loc_207B')

    Jump('loc_2316')

    def _loc_207E(): pass

    label('loc_207E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_20F5',
    )

    ChrTalk(
        0x000A,
        (
            '武术大会总是会有\n',
            '引人注目的军队成员，\n',
            '今年好像也有许多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '究竟哪个小组会取得优胜\n',
            '我真是十分期待啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2316')

    def _loc_20F5(): pass

    label('loc_20F5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_21F1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_2168',
    )

    ChrTalk(
        0x000A,
        (
            '昨天士兵押送的\n',
            '几个戴手铐的人来了这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '按照常理，做了坏事被捕的人\n',
            '怎么能来买武器呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_21EE')

    def _loc_2168(): pass

    label('loc_2168')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x000A,
        (
            '昨天士兵押送的\n',
            '几个戴手铐的人来了这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '按照常理，做了坏事被捕的人\n',
            '怎么能来买武器呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '究竟要干什么？\n',
            '有点可怕……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_21EE(): pass

    label('loc_21EE')

    Jump('loc_2316')

    def _loc_21F1(): pass

    label('loc_21F1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_22DF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_2256',
    )

    ChrTalk(
        0x000A,
        (
            '亲卫队的中队长也\n',
            '经常到这里来光顾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '她是一位时常关心着\n',
            '女王陛下的好人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_22DC')

    def _loc_2256(): pass

    label('loc_2256')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x000A,
        (
            '不管怎样，\n',
            '我还是不相信亲卫队的人是恐怖分子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '那位中队长也\n',
            '经常到这里来光顾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '她是一位时常关心着\n',
            '女王陛下的好人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_22DC(): pass

    label('loc_22DC')

    Jump('loc_2316')

    def _loc_22DF(): pass

    label('loc_22DF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_2316',
    )

    ChrTalk(
        0x000A,
        (
            '欢迎光临，各位游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '请慢慢挑选吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2316(): pass

    label('loc_2316')

    TalkEnd(0x000A)

    Return()

# id: 0x000A offset: 0x231A
@scena.Code('func_0A_231A')
def func_0A_231A():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 3, 0x64B)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_26A4',
    )

    EventBegin(0x00)
    Fade(1000)
    CameraMove(4690, 4000, -2480, 0)
    SetChrPos(0x0101, 4350, 4000, -2160, 90)
    SetChrPos(0x0102, 4390, 4000, -3250, 90)
    SetChrPos(0x0108, 3200, 4000, -2630, 90)
    ChrTurnDirection(0x0008, 0x0108, 0)
    SetScenaFlags(ScenaFlag(0x00C9, 3, 0x64B))
    OP_28(0x004B, 0x01, 0x0020)

    If(
        (
            (Expr.Eval, "OP_29(0x004B, 0x01, 0x0010)"),
            (Expr.Eval, "OP_29(0x004B, 0x01, 0x0020)"),
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x004B, 0x01, 0x0040)"),
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x004B, 0x01, 0x0080)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_23AD',
    )

    OP_28(0x004B, 0x01, 0x0100)

    def _loc_23AD(): pass

    label('loc_23AD')

    OP_0D()
    SetChrSubChip(0x00FE, 0)

    ChrTalk(
        0x0101,
        (
            '#0010130116V#004F啊，卡露娜姐姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0320130117V#830F哦，是你们啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320130118V金大哥也在，\n',
            '到底有什么事呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080130119V#074F实际上，\n',
            '发生了一件十分棘手的事情……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0320130120V#832F……什么？\n',
            '究竟是怎么回事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔他们向卡露娜说明了\n',
            '至今为止发生的事情和女王的委托。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0008,
        (
            '#0320130121V#832F…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320130122V……唔……\n',
            '这可不能开玩笑的啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320130123V#833F关所和飞艇坪被封锁，\n',
            '虽然我从其中也嗅出了一些火药味……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320130124V#832F事情明白了。\n',
            '我该怎么做？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020130125V#012F首先大家要集中在一起，\n',
            '然后商量和制定作战计划。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020130126V请回游击士协会去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0320130127V#832F知道了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320130128V那我就先行一步了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2628')
    def lambda_2628():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_2628')

    DispatchAsync2(0x0101, 0x0001, lambda_2628)

    @scena.Lambda('lambda_2639')
    def lambda_2639():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_2639')

    DispatchAsync2(0x0102, 0x0001, lambda_2639)

    @scena.Lambda('lambda_264A')
    def lambda_264A():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_264A')

    DispatchAsync2(0x0108, 0x0001, lambda_264A)

    ChrWalkTo(0x0008, 5410, 4000, 630, 4000, 0x00)
    ChrWalkTo(0x0008, 3160, 4000, 2550, 4000, 0x00)
    ChrWalkTo(0x0008, -3500, 0, 2550, 4000, 0x00)
    SetChrFlags(0x0008, 0x0080)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0108, 0xFF)
    EventEnd(0x00)

    def _loc_26A4(): pass

    label('loc_26A4')

    TalkEnd(0x0008)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
