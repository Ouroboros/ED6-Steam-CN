import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T4222_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4222   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4222.x'
    header.mapIndex       = 1
    header.bgm            = 17
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
        ('ED6_DT07/CH02350._CH', 'ED6_DT07/CH02350P._CP'),
        ('ED6_DT07/CH02370._CH', 'ED6_DT07/CH02370P._CP'),
        ('ED6_DT07/CH02360._CH', 'ED6_DT07/CH02360P._CP'),
        ('ED6_DT07/CH02600._CH', 'ED6_DT07/CH02600P._CP'),
        ('ED6_DT07/CH02620._CH', 'ED6_DT07/CH02620P._CP'),
        ('ED6_DT07/CH02540._CH', 'ED6_DT07/CH02540P._CP'),
        ('ED6_DT07/CH00070._CH', 'ED6_DT07/CH00070P._CP'),
        ('ED6_DT07/CH02460._CH', 'ED6_DT07/CH02460P._CP'),
        ('ED6_DT07/CH02230._CH', 'ED6_DT07/CH02230P._CP'),
        ('ED6_DT07/CH02240._CH', 'ED6_DT07/CH02240P._CP'),
        ('ED6_DT07/CH01100._CH', 'ED6_DT07/CH01100P._CP'),
        ('ED6_DT07/CH01350._CH', 'ED6_DT07/CH01350P._CP'),
    ]

# id: 0x10001 offset: 0x10A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '克劳斯市长',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '莉拉',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '梅贝尔市长',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '科林兹校长',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '茜亚',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '金',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '里拉老人',
            x                   = -139550,
            z                   = 4000,
            y                   = 9480,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '布莉姆',
            x                   = -78950,
            z                   = 0,
            y                   = 5960,
            direction           = 359,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
    )

# id: 0x10002 offset: 0x20A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x20A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x20A
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x20A
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_218',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, func_09_141A)

    def _loc_218(): pass

    label('loc_218')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 3, 0x3FB)),
            Expr.Return,
        ),
        'loc_226',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    Event(0, func_0C_288F)

    def _loc_226(): pass

    label('loc_226')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 4, 0x3FC)),
            Expr.Return,
        ),
        'loc_234',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    Event(0, func_0E_2E61)

    def _loc_234(): pass

    label('loc_234')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 1, 0x639)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 0, 0x640)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_298',
    )

    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrSetPos(0x000A, -28870, 0, 53540, 270)
    ChrSetPos(0x0009, -28040, 0, 54950, 211)
    ChrSetPos(0x000B, -83970, 0, -52980, 270)
    ChrSetPos(0x0008, -86020, 0, -52980, 90)

    def _loc_298(): pass

    label('loc_298')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x0000006A, 'loc_2A8'),
        (0x00000065, 'loc_2CA'),
        (-1, 'loc_2E0'),
    )

    def _loc_2A8(): pass

    label('loc_2A8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 2, 0x63A)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 3, 0x63B)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 4, 0x63C)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 6, 0x63E)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 7, 0x63F)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2C7',
    )

    SetScenaFlags(ScenaFlag(0x00C7, 7, 0x63F))
    Event(0, func_0B_1F85)

    def _loc_2C7(): pass

    label('loc_2C7')

    Jump('loc_2E0')

    def _loc_2CA(): pass

    label('loc_2CA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 7, 0x63F)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 0, 0x640)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2DD',
    )

    SetScenaFlags(ScenaFlag(0x00C8, 0, 0x640))
    Event(0, func_0D_2CED)

    def _loc_2DD(): pass

    label('loc_2DD')

    Jump('loc_2E0')

    def _loc_2E0(): pass

    label('loc_2E0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_30A',
    )

    ChrSetChipByIndex(0x0000, 7)
    ChrSetChipByIndex(0x0001, 8)
    ChrSetChipByIndex(0x0138, 9)
    ChrSetFlags(0x0000, 0x1000)
    ChrSetFlags(0x0001, 0x1000)
    ChrSetFlags(0x0138, 0x1000)

    def _loc_30A(): pass

    label('loc_30A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 7, 0x66F)),
            Expr.Return,
        ),
        'loc_319',
    )

    ChrSetFlags(0x000E, 0x0080)

    Jump('loc_357')

    def _loc_319(): pass

    label('loc_319')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_328',
    )

    ChrClearFlags(0x000F, 0x0080)

    Jump('loc_357')

    def _loc_328(): pass

    label('loc_328')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Return,
        ),
        'loc_337',
    )

    ChrSetFlags(0x000E, 0x0080)

    Jump('loc_357')

    def _loc_337(): pass

    label('loc_337')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            Expr.Return,
        ),
        'loc_346',
    )

    ChrSetFlags(0x000E, 0x0080)

    Jump('loc_357')

    def _loc_346(): pass

    label('loc_346')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 0, 0x640)),
            Expr.Return,
        ),
        'loc_350',
    )

    Jump('loc_357')

    def _loc_350(): pass

    label('loc_350')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 1, 0x639)),
            Expr.Return,
        ),
        'loc_357',
    )

    def _loc_357(): pass

    label('loc_357')

    Return()

# id: 0x0001 offset: 0x358
@scena.Code('func_01_358')
def func_01_358():
    ExecExpressionWithVar(
        0x2B,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0002 offset: 0x362
@scena.Code('func_02_362')
def func_02_362():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_377',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_362')

    def _loc_377(): pass

    label('loc_377')

    Return()

# id: 0x0003 offset: 0x378
@scena.Code('func_03_378')
def func_03_378():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '嗯，接下来是打扫客房。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为今天有许多客人要在城里留宿，\n',
            '所以要做的准备不少啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0004 offset: 0x3D8
@scena.Code('func_04_3D8')
def func_04_3D8():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 7, 0x66F)),
            Expr.Return,
        ),
        'loc_3E5',
    )

    Jump('loc_52B')

    def _loc_3E5(): pass

    label('loc_3E5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_458',
    )

    ChrTalk(
        0x00FE,
        (
            '《王城设计图》、《七至宝》、\n',
            '《百日战役全貌》……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎呀呀，\n',
            '被情报部拿走的这些书\n',
            '终于又回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_52B')

    def _loc_458(): pass

    label('loc_458')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Return,
        ),
        'loc_462',
    )

    Jump('loc_52B')

    def _loc_462(): pass

    label('loc_462')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            Expr.Return,
        ),
        'loc_46C',
    )

    Jump('loc_52B')

    def _loc_46C(): pass

    label('loc_46C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 0, 0x640)),
            Expr.Return,
        ),
        'loc_4CE',
    )

    ChrTalk(
        0x00FE,
        (
            '完了，\n',
            '格兰赛尔城的设计图纸竟然也不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '情报部的家伙\n',
            '究竟打算拿去做什么啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_52B')

    def _loc_4CE(): pass

    label('loc_4CE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 1, 0x639)),
            Expr.Return,
        ),
        'loc_52B',
    )

    ChrTalk(
        0x00FE,
        (
            '情报部的那群家伙，\n',
            '到底要做什么啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '竟然把严禁外借的\n',
            '重要资料强行取走了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_52B(): pass

    label('loc_52B')

    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0x52F
@scena.Code('func_05_52F')
def func_05_52F():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 3, 0x63B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_53B',
    )

    Call(0, 0x0006)

    def _loc_53B(): pass

    label('loc_53B')

    Return()

# id: 0x0006 offset: 0x53C
@scena.Code('func_06_53C')
def func_06_53C():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 3, 0x63B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_D43',
    )

    SetScenaFlags(ScenaFlag(0x00C7, 3, 0x63B))
    EventBegin(0x00)
    Fade(1000)
    ChrSetPos(0x0101, -85860, 0, -55170, 0)
    ChrSetPos(0x0102, -84960, 0, -55250, 0)
    CameraMove(-85030, 450, -53200, 1000)

    ChrTalk(
        0x0008,
        (
            '#600F哦哦，来了吗。\n',
            '艾丝蒂尔、约修亚，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0530850035V#780F呵呵，好久不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F哎……校长先生！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F难道校长先生您\n',
            '也被邀请参加晚宴吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0530850036V#780F是啊，就是乘今天的定期船\n',
            '从卢安赶过来的呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530850037V我已经听说了，\n',
            '你们不是获得武术大会的冠军了吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530850038V学生们听到了肯定也会十分高兴的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嘿嘿……\n',
            '真的非常感谢您。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F不过，只凭我们自己的力量\n',
            '是不可能赢的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '说起来，我没有想到\n',
            '校长也会被邀请来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0341330002V#600F科林兹校长作为\n',
            '利贝尔首屈一指的贤者，\n',
            '每年都会出席王国会议呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340120279V被邀请出席晚宴\n',
            '也没有什么奇怪的啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0530120280V#780F哈哈，说我是贤者，\n',
            '真是太过誉了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯……王国会议是什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F是为解决整个王国范围的问题，\n',
            '而召开的一年一度的例会。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '女王陛下、各地区的市长，\n',
            '以及各界的代表人士齐聚一堂，\n',
            '讨论和协商各种各样的问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F哎～是这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120285V那么，今天的晚宴邀请的\n',
            '都是这些人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0530850039V#780F不……\n',
            '其实连一半都不到。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530850040V女王陛下身体欠佳，\n',
            '摩尔根将军忙于军务……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530850041V卢安的戴尔蒙市长\n',
            '也因为那个案件被逮捕了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530120289V还有，拉赛尔博士也……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0341330003V#600F和他相关的那个案件，\n',
            '现在还有很多地方没有弄清楚呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0341330004V不仅牵扯到了亲卫队，\n',
            '还说是大规模的恐怖组织所为，\n',
            '到底有多少是真相啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0341330005V真是的，在这种情况下，\n',
            '还有心思召开什么晚宴。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0530850042V#780F不过，为了确认\n',
            '公爵阁下真正的心意，\n',
            '也有出席这次晚宴的必要。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530850043V而且，还要借此机会\n',
            '探望和问候女王陛下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0341330006V#600F嗯嗯。\n',
            '这个才是最重要的呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0341330007V来到这格兰赛尔城，\n',
            '不能拜见陛下\n',
            '这不是扯的么。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '而且，也很久没有见到\n',
            '科洛蒂娅公主了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F科洛蒂娅公主……\n',
            '我记得是女王陛下的孙女吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F公主殿下\n',
            '也住在格兰赛尔城吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#600F不，平常是住在\n',
            '另外一个地方的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340120303V不过，听说几天前\n',
            '回到王都来了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F哎～是这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '嗯～如果有机会，\n',
            '一定要和她见上一面呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0530850044V#780F呵呵，如果是你们，\n',
            '肯定能见到她的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    def _loc_D43(): pass

    label('loc_D43')

    Return()

# id: 0x0007 offset: 0xD44
@scena.Code('func_07_D44')
def func_07_D44():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 2, 0x63A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_D50',
    )

    Call(0, 0x0008)

    def _loc_D50(): pass

    label('loc_D50')

    Return()

# id: 0x0008 offset: 0xD51
@scena.Code('func_08_D51')
def func_08_D51():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 2, 0x63A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1419',
    )

    SetScenaFlags(ScenaFlag(0x00C7, 2, 0x63A))
    EventBegin(0x00)
    EventBegin(0x00)
    Fade(1000)
    ChrSetPos(0x0101, -29280, 0, 55240, 135)
    ChrSetPos(0x0102, -30310, 0, 54780, 135)
    CameraMove(-28840, 0, 54560, 1000)

    ChrTalk(
        0x0101,
        (
            '#000F啊……梅贝尔市长！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120199V#010F莉拉小姐也来了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#620F艾丝蒂尔小姐，约修亚先生……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#610F呵呵，我们又见面了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360120202V我一直等着\n',
            '你们两个的到来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F梅贝尔市长\n',
            '果然也被邀请参加晚宴呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '哎，\n',
            '为什么会知道我们要来……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0360120205V#610F我是听克劳斯市长说的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360120206V你们在武术大会中获得优胜，\n',
            '从而被邀请出席晚宴。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '啊～如果早知道的话，\n',
            ' \n',
            '来给你们加油了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#620F小姐，话虽这么说……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370120209V如果这样，之后小姐自己\n',
            '不是要非常辛苦了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#610F呜～我知道啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊哈哈……\n',
            ' ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#610F真是的，女王陛下暂且不论，\n',
            '那个公爵举办的晚宴，\n',
            '本来就没有什么闲工夫来参加啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360120213V都是因为那个军队的女士官\n',
            '固执地催促让我出席，\n',
            '实在没办法才来王都的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F是情报部的凯诺娜上尉吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#610F嗯，就是她。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360120216V虽然很有礼貌，其实不把人放在眼里，\n',
            '我真是不喜欢那个人呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360120217V最近，也没办法\n',
            '和摩尔根将军取得联系……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F那是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F和哈肯门那边\n',
            '联系不上吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#610F坚持说『将军不在』，\n',
            '让我吃了闭门羹。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360120221V好像是为了应对恐怖事件，\n',
            '工作相当地繁忙呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '本来还想能不能\n',
            '在今天的晚宴上见面呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360120223V看起来好像也没有出席呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120224V#000F是这样吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F市长对这件事是怎么想的？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020120226V在这个时候把市长们召集起来\n',
            '召开这样的晚宴……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#610F是呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360120228V如果是女王陛下举办的话，\n',
            '应该是要宣布重要的事情吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '不过这次大概只是为了\n',
            '陪公爵阁下打发时间而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0361290004V滥用陛下代理人的特权，\n',
            '让人认为他大权在握而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F哇～真是精辟啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F不过，\n',
            '也有可能不只是为这样的理由。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#610F算了，听说这里的西餐\n',
            '是整个王国最棒的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0361290005V享用完美味的晚餐，\n',
            '探望一下女王陛下，\n',
            '然后就赶快回柏斯吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    def _loc_1419(): pass

    label('loc_1419')

    Return()

# id: 0x0009 offset: 0x141A
@scena.Code('func_09_141A')
def func_09_141A():
    EventBegin(0x00)
    ChrSetPos(0x0101, -52050, 0, 2040, 0)
    ChrSetPos(0x0102, -52050, 0, 2040, 0)
    ChrSetPos(0x0108, -52050, 0, 2040, 0)
    ChrSetPos(0x000C, -52050, 0, 2040, 0)
    ChrClearFlags(0x000C, 0x0080)
    ChrSetFlags(0x000C, 0x0040)
    OP_69(0x0102, 0)
    OP_6A(0x0102)

    @scena.Lambda('lambda_147A')
    def lambda_147A():
        ChrWalkTo(0x00FE, -78180, 0, 2180, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_147A)

    Sleep(500)

    @scena.Lambda('lambda_149A')
    def lambda_149A():
        ChrWalkTo(0x00FE, -78180, 0, 2180, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_149A)

    Sleep(500)

    @scena.Lambda('lambda_14BA')
    def lambda_14BA():
        ChrWalkTo(0x00FE, -78180, 0, 2180, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_14BA)

    Sleep(500)

    @scena.Lambda('lambda_14DA')
    def lambda_14DA():
        ChrWalkTo(0x00FE, -78180, 0, 2180, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_14DA)

    WaitForThreadExit(0x000C, 0x0001)

    @scena.Lambda('lambda_14FA')
    def lambda_14FA():
        ChrWalkTo(0x00FE, -78970, 0, 7390, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_14FA)

    WaitForThreadExit(0x0102, 0x0001)

    @scena.Lambda('lambda_151A')
    def lambda_151A():
        ChrWalkTo(0x00FE, -79880, 0, 5530, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_151A)

    WaitForThreadExit(0x0101, 0x0001)

    @scena.Lambda('lambda_153A')
    def lambda_153A():
        ChrWalkTo(0x00FE, -78550, 0, 5460, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_153A)

    WaitForThreadExit(0x0108, 0x0001)

    @scena.Lambda('lambda_155A')
    def lambda_155A():
        ChrWalkTo(0x00FE, -79280, 0, 4450, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_155A)

    WaitForThreadExit(0x000C, 0x0001)
    Sleep(200)

    ChrWalkTo(0x000C, -80280, 0, 7250, 2000, 0x00)
    ChrTurnDirection(0x000C, 0x0102, 0)

    ChrTalk(
        0x000C,
        (
            '这个就是各位\n',
            '晚上可以使用的房间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '请进吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯、嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120136V#010F那么我们就告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0101, 0x01, 0x00, func_0A_1F4A)
    Sleep(500)

    CreateThread(0x0102, 0x01, 0x00, func_0A_1F4A)
    Sleep(500)

    CreateThread(0x0108, 0x01, 0x00, func_0A_1F4A)
    Sleep(1000)

    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0108, 0xFF)
    MapClearFlags(0x00000001)
    Fade(1000)
    CameraMove(-79120, 0, 55910, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetRGBAMask(0x0101, 255, 255, 255, 255, 0)
    ChrSetRGBAMask(0x0102, 255, 255, 255, 255, 0)
    ChrSetRGBAMask(0x0108, 255, 255, 255, 255, 0)
    ChrSetPos(0x000C, -80040, 0, 50510, 0)
    ChrSetPos(0x0101, -80880, 0, 53000, 315)
    ChrSetPos(0x0102, -79650, 0, 53710, 270)
    ChrSetPos(0x0108, -78830, 0, 52390, 0)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#000F哇……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F能在这种地方过夜，\n',
            '真是无法想象呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#070F哎呀～真是不错啊，\n',
            '可以当成炫耀的资本了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '在晚宴开始之前，\n',
            '请在此等候。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1786')
    def lambda_1786():
        ChrTurnDirection(0x00FE, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1786)

    @scena.Lambda('lambda_1794')
    def lambda_1794():
        ChrTurnDirection(0x00FE, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1794)

    @scena.Lambda('lambda_17A2')
    def lambda_17A2():
        ChrTurnDirection(0x00FE, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_17A2)

    CameraMove(-79790, 0, 52600, 1000)

    ChrTalk(
        0x000C,
        (
            '虽然城内允许自由参观，\n',
            '不过因为警卫上的理由，\n',
            '有一些禁止进入的区域。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2300120142V请不要到那些地方去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯，具体来说\n',
            '哪些地方不能去呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2300120144V首先是，\n',
            '女王陛下居住的女王宫。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2300120145V就是在屋顶空中庭园的一角\n',
            '建造的小型宫殿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F空中庭园……\n',
            '听起来感觉十分地美丽呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '嘻嘻……生日庆典的时候，\n',
            '陛下会在那里的阳台上\n',
            '向王都的市民致意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2300120148V如果只是到空中庭园去的话，\n',
            '也应该足够了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2300120149V还有，其他禁止进入的场所……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2300120150V在１楼的亲卫队办公室\n',
            '以及地下的宝物库。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetRGBAMask(0x0108, 255, 255, 255, 255, 0)

    ChrTalk(
        0x0102,
        (
            '#010F亲卫队办公室……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#070F是不是作为恐怖分子\n',
            '受到通缉的那些人呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2300120153V是、是的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2300120154V现在，那个办公室\n',
            '正由情报部的人使用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2300120155V所以不允许进入，\n',
            '请你们理解。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F差不多明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '对了，晚宴邀请的其他客人\n',
            '现在在哪里呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2300120158V过一会儿，\n',
            '你们就能见到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '大概他们现在\n',
            '正在各自的房间里休息吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120160V#010F是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F那么，\n',
            '克劳斯市长已经来了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2300120162V是的，\n',
            '刚刚才招待过他。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2300120163V那么，我先告退了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2300120164V如果有什么事情的话，\n',
            '请到１楼的休息室来找我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000C, 180, 400)

    @scena.Lambda('lambda_1C31')
    def lambda_1C31():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1C31)

    ChrWalkTo(0x000C, -80140, 0, 48190, 1000, 0x00)
    ChrSetFlags(0x000C, 0x0004)

    ChrTalk(
        0x0101,
        (
            '#000F嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)
    ChrTurnDirection(0x0102, 0x0101, 400)
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔和约修亚\n',
            '趁金没有注意交换了眼色。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    @scena.Lambda('lambda_1CBF')
    def lambda_1CBF():
        ChrTurnDirection(0x00FE, 0x0108, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1CBF)

    ChrTurnDirection(0x0101, 0x0108, 400)

    ChrTalk(
        0x0101,
        (
            '#000F……我说，金先生。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120167V我们想借此机会\n',
            '在城里参观一下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1D20')
    def lambda_1D20():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_1D20)

    ChrTalk(
        0x0102,
        (
            '#0020120168V#010F晚宴开始之前就会回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#070F哎呀哎呀，刚刚比赛完，\n',
            '年轻人真是精力旺盛啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '好，你们去吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080120171V吃饭之前\n',
            '我就在这豪华的房间里休息一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(1000)
    CameraMove(-79060, 0, 5580, 0)
    FormationDelMember(0x07, 0xFF)
    ChrSetPos(0x0101, -79060, 0, 9840, 0)
    ChrSetPos(0x0102, -79060, 0, 9840, 0)

    @scena.Lambda('lambda_1E15')
    def lambda_1E15():
        ChrWalkTo(0x00FE, -78290, 0, 5560, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1E15)

    Sleep(600)

    @scena.Lambda('lambda_1E35')
    def lambda_1E35():
        ChrWalkTo(0x00FE, -79270, 0, 6410, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1E35)

    WaitForThreadExit(0x0101, 0x0001)

    @scena.Lambda('lambda_1E55')
    def lambda_1E55():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1E55)

    WaitForThreadExit(0x0102, 0x0001)

    @scena.Lambda('lambda_1E68')
    def lambda_1E68():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1E68)

    ChrTalk(
        0x0101,
        (
            '#000F在晚宴开始之前，\n',
            '一定要尽可能多做一些事情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120173V首先要去找\n',
            '尤莉亚小姐所说的希尔丹夫人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120174V#010F还有，我们最好\n',
            '去和其他的客人打个招呼。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020120175V大概，认识的人会很多吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_6A(0x0000)
    MapClearFlags(0x00000001)
    EventEnd(0x00)

    Return()

# id: 0x000A offset: 0x1F4A
@scena.Code('func_0A_1F4A')
def func_0A_1F4A():
    ChrWalkTo(0x00FE, -79010, 0, 7330, 3000, 0x00)

    @scena.Lambda('lambda_1F64')
    def lambda_1F64():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_1F64)

    ChrWalkTo(0x00FE, -79000, 0, 9730, 3000, 0x00)

    Return()

# id: 0x000B offset: 0x1F85
@scena.Code('func_0B_1F85')
def func_0B_1F85():
    EventBegin(0x00)
    CameraMove(-80130, 0, 51090, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FormationAddMember(0x07, 0xFF)
    ChrSetPos(0x0101, -80670, 0, 51310, 270)
    ChrSetPos(0x0102, -79770, 0, 50560, 270)
    ChrSetPos(0x0108, -87580, 0, 52200, 90)
    CameraMove(-83020, 0, 52310, 2000)

    ChrTalk(
        0x0108,
        (
            '#0080120572V#070F哟，艾丝蒂尔、约修亚。\n',
            '回来的是不是有些晚呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080120573V就要到晚宴开始的时候了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_207D')
    def lambda_207D():
        ChrWalkTo(0x00FE, -82610, 0, 52640, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_207D)

    Sleep(300)

    @scena.Lambda('lambda_209D')
    def lambda_209D():
        CameraMove(-86640, 0, 52720, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_209D)

    @scena.Lambda('lambda_20B5')
    def lambda_20B5():
        ChrWalkTo(0x00FE, -82610, 0, 52640, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_20B5)

    WaitForThreadExit(0x0101, 0x0001)

    @scena.Lambda('lambda_20D5')
    def lambda_20D5():
        ChrWalkTo(0x00FE, -85950, 0, 53460, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_20D5)

    WaitForThreadExit(0x0102, 0x0001)

    @scena.Lambda('lambda_20F5')
    def lambda_20F5():
        ChrWalkTo(0x00FE, -86030, 0, 52040, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_20F5)

    WaitForThreadExit(0x0101, 0x0001)
    ChrTurnDirection(0x0101, 0x0108, 400)
    WaitForThreadExit(0x0101, 0x0003)

    ChrTalk(
        0x0101,
        (
            '#000F抱歉啊，金大哥。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120575V东看看西逛逛的\n',
            '就把时间给忘了～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '而且还和各地的市长们\n',
            '谈了许多哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#070F咦，你们俩之前就\n',
            '认识那些有身份的人物吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120578V#010F洛连特的市长\n',
            '平日里就对我们很亲切。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020120579V其他的几位是我们在旅行\n',
            '途中经过各个城市时认识的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#070F原来如此啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080120581V游击士在完成任务的时候，\n',
            '的确有许多结识有身份人物的机会呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0081040018V可是这样看来，\n',
            '你们好像极为活跃对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F哈哈哈……还没有到那种程度啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '金大哥到王都来是因为\n',
            '有什么任务要完成吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120585V我想，虽说是在别国，\n',
            '但还是照样可以完成相关任务吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080120586V#070F是啊，一旦成为了正游击士，\n',
            '就可以去做一些超越国界的任务了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080120587V预选赛啊，大使馆的手续啊什么的，\n',
            '弄得我连接受任务的时间都没有了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '唉，如果另外再来四位游击士的话，\n',
            '就可以不用我来参加比赛了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120589V#010F的确，如果游击士们都聚集到了这里，\n',
            '大部分事件都可以很快解决的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020120590V可若是都在王都集中了的话，\n',
            '其他地方的支部可就难办了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#070F哇哈哈，说的也是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F呼，总觉得到现在才\n',
            '想到这些也用处不大了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '雪拉姐现在在洛连特\n',
            '做什么呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#070F雪拉姐……\n',
            '是指雪拉扎德吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F咦……你认识她！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F是呀，她是我们的前辈，\n',
            '过去一直都在照顾着我们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#070F原来如此，竟然是这样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '以前她到卡尔瓦德来的时候\n',
            '和我认识的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080120600V她有一个很好的老师啊，\n',
            '年纪轻轻却是见多识广。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2652')
    def lambda_2652():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2652)

    @scena.Lambda('lambda_2660')
    def lambda_2660():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_2660)

    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#000F（他说的那个老师不就是……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F（嗯，就是父亲呢。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0108, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrSetPos(0x000C, -80120, 0, 48440, 315)

    @scena.Lambda('lambda_2714')
    def lambda_2714():
        ChrTurnDirection(0x00FE, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2714)

    @scena.Lambda('lambda_2722')
    def lambda_2722():
        ChrTurnDirection(0x00FE, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_2722)

    @scena.Lambda('lambda_2730')
    def lambda_2730():
        ChrTurnDirection(0x00FE, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_2730)

    ChrTalk(
        0x000C,
        (
            '打搅一下，\n',
            '晚宴已经准备完毕了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '让我带你们大家去可以吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#070F哦啊，我等的都有些腻烦了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '那～么，我们这就去\n',
            '好好享用这顿美餐吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯，说起来在比赛之后\n',
            '我的肚子已经饿的不行了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '走吧～大吃一顿去了～⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    ChrSetDirection(0x0102, 315, 400)
    Sleep(1000)

    ChrTalk(
        0x0102,
        (
            '#010F我说你们俩啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '还是不要忘记了\n',
            '餐桌上的那些礼仪了哦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T4251._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000C offset: 0x288F
@scena.Code('func_0C_288F')
def func_0C_288F():
    EventBegin(0x00)
    CameraMove(-79320, 0, 55910, 0)
    FormationDelMember(0x07, 0xFF)
    ChrClearFlags(0x000D, 0x0080)
    ChrSetPos(0x000D, -79660, 0, 56600, 192)
    ChrSetPos(0x0101, -80390, 0, 55080, 23)
    ChrSetPos(0x0102, -78690, 0, 55240, 315)

    ChrTalk(
        0x000D,
        (
            '#0080120782V#070F哎呀，出乎预料的事\n',
            '竟然意外的听说了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080120783V我一来就插入你们国家的谈话，\n',
            '把你们两个很是\n',
            '吓了一跳对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F那、那是当然的了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120785V要、要不是说的\n',
            '还比较周到的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#070F啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊，嗯，没什么。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '其实……\n',
            '真是遗憾啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120789V虽然特地让舌头沉醉于\n',
            '美味的料理之中，\n',
            '可最后那道菜的精妙还是没能体会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F哈哈，不用强求嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '对了，艾丝蒂尔，\n',
            '去散散步消化一下食物如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F咦……？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '啊啊！\n',
            '对呀，好建议！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120794V不错呢～我也想好好\n',
            '呼吸一下外面的新鲜空气了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#070F啊～刚才去参观各处，\n',
            '这回吃完饭又要去散步了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '想不承认都不行啊，\n',
            '这就是年纪的差异导致的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊哈哈，金大哥你太夸张了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120798V#010F金兄也去\n',
            '走走如何？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020120799V这个历史久远的建筑\n',
            '可供参观的地方不少呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0080120800V#070F嗯，等我想到了的时候\n',
            '再到处溜达一下也不迟。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我要去厨房看看，\n',
            '应该还有一些剩余的食物。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F不会吧……\n',
            '还要打算吃吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#070F也算是吧，\n',
            '就是想弄点酒菜。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0081040019V想喝酒可以到谈话室去，\n',
            '待会儿我就去瞧瞧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x004A, 0x04, 0x02)
    OP_28(0x004A, 0x04, 0x04)
    OP_28(0x004A, 0x01, 0x0001)
    OP_28(0x004A, 0x01, 0x0002)
    OP_28(0x004A, 0x01, 0x0004)
    EventEnd(0x00)

    Return()

# id: 0x000D offset: 0x2CED
@scena.Code('func_0D_2CED')
def func_0D_2CED():
    EventBegin(0x00)
    CameraMove(-79060, 0, 5580, 0)
    ChrSetPos(0x0101, -79060, 0, 9840, 0)
    ChrSetPos(0x0102, -79060, 0, 9840, 0)

    @scena.Lambda('lambda_2D28')
    def lambda_2D28():
        ChrWalkTo(0x00FE, -78290, 0, 5560, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2D28)

    Sleep(600)

    @scena.Lambda('lambda_2D48')
    def lambda_2D48():
        ChrWalkTo(0x00FE, -79270, 0, 6410, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_2D48)

    WaitForThreadExit(0x0101, 0x0001)

    @scena.Lambda('lambda_2D68')
    def lambda_2D68():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2D68)

    WaitForThreadExit(0x0102, 0x0001)

    @scena.Lambda('lambda_2D7B')
    def lambda_2D7B():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_2D7B)

    ChrTalk(
        0x0101,
        (
            '#000F呼～……\n',
            '真是出乎预料的事啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120806V越来越想去见女王陛下，\n',
            '并问问到底怎么回事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F首先按照约定\n',
            '去见希尔丹夫人吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020120808V她应该有办法\n',
            '让我们见到陛下的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120809V#000F嗯，明白。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Return()

# id: 0x000E offset: 0x2E61
@scena.Code('func_0E_2E61')
def func_0E_2E61():
    EventBegin(0x00)
    CameraMove(-79860, 0, 50720, 0)
    ChrSetPos(0x0101, -80040, 0, 48610, 0)
    ChrSetPos(0x0102, -80040, 0, 48610, 0)
    ChrSetPos(0x0108, -80040, 0, 48610, 0)
    ChrSetRGBAMask(0x0101, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0102, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0108, 255, 255, 255, 0, 0)

    @scena.Lambda('lambda_2ECE')
    def lambda_2ECE():
        CameraMove(-79660, 0, 55360, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2ECE)

    @scena.Lambda('lambda_2EE6')
    def lambda_2EE6():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0108, 0x0002, lambda_2EE6)

    @scena.Lambda('lambda_2EF8')
    def lambda_2EF8():
        ChrWalkTo(0x00FE, -80030, 0, 55890, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_2EF8)

    Sleep(500)

    @scena.Lambda('lambda_2F18')
    def lambda_2F18():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2F18)

    @scena.Lambda('lambda_2F2A')
    def lambda_2F2A():
        ChrWalkTo(0x00FE, -80320, 0, 54310, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2F2A)

    Sleep(500)

    @scena.Lambda('lambda_2F4A')
    def lambda_2F4A():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_2F4A)

    @scena.Lambda('lambda_2F5C')
    def lambda_2F5C():
        ChrWalkTo(0x00FE, -79160, 0, 54220, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_2F5C)

    WaitForThreadExit(0x0108, 0x0001)
    ChrSetDirection(0x0108, 180, 400)

    ChrTalk(
        0x0108,
        (
            '#070F哎呀哎呀……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080121562V总算是用比较擅长的\n',
            '手法蒙混过去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#000F哎……！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010121564V金大哥，\n',
            '你不是喝醉了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#070F那个啊，只是演技而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080121566V我可是一滴酒都没喝。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F说谎！？\n',
            '明明脸那么红……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F驱动内力，让血气上游，\n',
            '让表面看起来一副喝醉的样子……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '在东方武术里，\n',
            '这就是所谓『气功』的功夫对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#070F哦，这种事情\n',
            '你都知道，让我吃惊不小呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '哎呀，刚才看见你们陷入困境，\n',
            '我就忍不住叫了你们一声。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080121572V如何，还算帮了点忙吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F真是的，金大哥你呀，\n',
            '让人捉摸不透～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '虽说是来帮忙的，\n',
            '但着实吓了人一跳。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#070F哈哈，抱歉抱歉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '那么，情况怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150088V#000F？？？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010121578V什么怎么样呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#070F办完了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080121580V和女王陛下见面的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#000F什、什么～！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '为、为、为什么金大哥你知道！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F难道说是在艾南先生\n',
            '那里听说了什么吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#070F协会那个兄弟\n',
            '并没有告诉我什么。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '如果要说有什么的话，\n',
            '就是他曾经款待过我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F款待……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F……没有任何情报，\n',
            '是不可能做出这样的推断的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '金兄……\n',
            '你究竟知道些什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#070F嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080121590V也该是时候把那个东西\n',
            '拿给你们看看了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0108, -80170, 0, 54960, 2000, 0x00)
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '金从怀中取出一封信\n',
            '递给了艾丝蒂尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    ChrMoveTo(0x0108, -80030, 0, 55890, 2000, 0x00)

    ChrTalk(
        0x0101,
        (
            '#000F信、信……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F这个笔迹是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0081040020V#070F嗯，你们先拿来\n',
            '读一读吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080121594V然后就知道怎么回事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯、嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔\n',
            '开始阅读信的内容。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0160121596V',
            (TxtCtl.SetColor, 0x5),
            '金·瓦赛克阁下敬启。\n',
            '久疏问候，身体可好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0160121597V',
            (TxtCtl.SetColor, 0x5),
            '由于事出匆忙，我只有采取\n',
            '开门见山的方式，万望见谅。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '事实上，连同猎兵团在内的事件\n',
            '已经朝向帝国方向发展了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0160121599V',
            (TxtCtl.SetColor, 0x5),
            '可是，利贝尔国内似乎正有\n',
            '一股微妙的势力正在滋长蔓延着。\n',
            '若只是交给年轻人去处理，我有些放心不下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0160121600V',
            (TxtCtl.SetColor, 0x5),
            '我想请您帮忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0160121601V',
            (TxtCtl.SetColor, 0x5),
            '在我外出的时候，您到利贝尔来，\n',
            '如果有什么情况发生的话，\n',
            '就帮帮那些年轻人们，可以吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0160121602V',
            (TxtCtl.SetColor, 0x5),
            '因为您是第一次前往利贝尔，\n',
            '所以顺便游山玩水也是不错的选择。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0160121603V',
            (TxtCtl.SetColor, 0x5),
            '女王诞辰庆典前夕，会召开\n',
            '允许外国人参加的武术大会，\n',
            '这是一个很好的机会呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0160121604V',
            (TxtCtl.SetColor, 0x5),
            '突然提出这样的请求，或许让您有些为难，\n',
            '不过如果您有空的话，还请帮一帮忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0160121605V',
            (TxtCtl.SetColor, 0x5),
            '女王诞辰庆典时我会回来，\n',
            '到那时我再一并感谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '　　　　　　　卡西乌斯·布莱特',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0160121607V',
            (TxtCtl.SetColor, 0x5),
            '另：\n',
            '您也许会有机会见到\n',
            '我的女儿和儿子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0160121608V',
            (TxtCtl.SetColor, 0x5),
            '我让他们在游击士协会实习，\n',
            '当时没有想太多，只是锻炼一下他们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0160121609V',
            (TxtCtl.SetColor, 0x5),
            '如果他们有什么事，还请您\n',
            '助他们一臂之力，帮他们摆脱困境。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0101,
        (
            '#000F……这、这是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F金兄是父亲委托\n',
            '来利贝尔的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#070F嗯，就是这样的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F什么叫就是这样的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010121615V关、关键的是金大哥\n',
            '你竟然和老爸串通一气！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#070F串通一气什么的不太好听啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080121617V以前卡西乌斯大人\n',
            '来到我们卡尔瓦德时，\n',
            '我也受到了他很多的关照。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080121618V我一直都想报答他，\n',
            '这封信正好了却了我的心愿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F是这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F是什么时候\n',
            '发觉我们是父亲的孩子的呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0081040021V#070F第一次见面时，\n',
            '看见艾丝蒂尔拿着棒子，\n',
            '我就开始有些注意了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080121622V在询问了雾香之后我才确信。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F真是的，怎么能这样……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '之前连一个字\n',
            '也没有和我们提起过……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0081040022V#070F哈哈，大人的信上\n',
            '写着『不要太溺爱他们』呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0081040023V让我最低限度地帮助你们，\n',
            '平时守护着就可以了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0081040024V话又说回来，看来你们俩已经\n',
            '完成了一件不小的事情对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊，嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我说约修亚，\n',
            '现在说出来就没问题了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020121630V#010F嗯，既然如此，\n',
            '我就一一道来吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020121631V我们刚刚办完的事情\n',
            '要说起来是一个很长的故事呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔她们把博士的委托，\n',
            '见到艾莉茜雅女王……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '还有接受了女王的委托，要将被捉走的\n',
            '科洛蒂娅公主解救出来的事情说了出来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0108,
        (
            '#070F原来如此啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080121633V听了晚宴上那些话后，\n',
            '我就感觉充满了火药味……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '好的，为了完成这个委托，\n',
            '也让我助你们一臂之力吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F哎，可以吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#070F啊，这是报答卡西乌斯大人\n',
            '恩情的绝好机会呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080121637V请务必让我帮忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F我、我们俩也请你\n',
            '多多关照了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020121639V#010F再次请您多多关照。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0081040025V#070F哦，彼此彼此啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/C4300._SN', 100, 0, 0)
    IdleLoop()

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
