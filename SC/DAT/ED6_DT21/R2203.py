import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import R2203_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R2203   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '王国军士官'),
    TXT(0x02, '王国军士兵'),
    TXT(0x03, '王国军士兵'),
    TXT(0x04, '玛诺利亚村方向'),
    TXT(0x05, '玛西亚孤儿院方向'),
    TXT(0x06, '卢安方向'),
    TXT(0x07, ''),
    TXT(0x08, ''),
    TXT(0x09, ''),
    TXT(0x0A, ''),
    TXT(0x0B, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'R2203.x'
    header.mapIndex       = 101
    header.bgm            = 29
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0xB18
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
        ('ED6_DT29/CH12100._CH', 'ED6_DT29/CH12100P._CP'),
        ('ED6_DT29/CH12101._CH', 'ED6_DT29/CH12101P._CP'),
        ('ED6_DT29/CH12150._CH', 'ED6_DT29/CH12150P._CP'),
        ('ED6_DT29/CH12151._CH', 'ED6_DT29/CH12151P._CP'),
        ('ED6_DT07/CH01600._CH', 'ED6_DT07/CH01600P._CP'),
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
    ]

# id: 0x10002 offset: 0xDA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = -95890,
            z                   = -5970,
            y                   = 5490,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0002,
        ),
        ScenaNpcData(
            x                   = -94000,
            z                   = -6040,
            y                   = 4900,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            x                   = -86590,
            z                   = -2090,
            y                   = 20010,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = -139370,
            z                   = -2020,
            y                   = 15120,
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
            x                   = -28630,
            z                   = -1990,
            y                   = 79340,
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
            x                   = 7410,
            z                   = -2000,
            y                   = 29980,
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

# id: 0x10003 offset: 0x19A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = -96260,
            z           = -1950,
            y           = 27960,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0184,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -104740,
            z           = -5970,
            y           = 11000,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x018F,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -81100,
            z           = -5870,
            y           = 13330,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x018E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -88220,
            z           = -5960,
            y           = 9810,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x018F,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x20A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x20A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -114230,
            triggerZ            = -6050,
            triggerY            = 11770,
            triggerRange        = 1000,
            actorX              = -114730,
            actorZ              = -6040,
            actorY              = 12270,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -77980,
            triggerZ            = -6870,
            triggerY            = -11780,
            triggerRange        = 1000,
            actorX              = -77540,
            actorZ              = -6730,
            actorY              = -11140,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -21830,
            triggerZ            = -2000,
            triggerY            = 37790,
            triggerRange        = 1500,
            actorX              = -21830,
            actorZ              = -800,
            actorY              = 37790,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -18840,
            triggerZ            = -2000,
            triggerY            = 33860,
            triggerRange        = 1500,
            actorX              = -18840,
            actorZ              = -500,
            actorY              = 33860,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x29A
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_2E4',
    )

    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    SetChrPos(0x0009, -32430, -1940, 54880, 135)
    SetChrPos(0x000A, -117980, -2100, 18390, 135)
    SetChrFlags(0x000F, 0x0080)
    SetChrFlags(0x0010, 0x0080)
    SetChrFlags(0x0011, 0x0080)

    Jump('loc_309')

    def _loc_2E4(): pass

    label('loc_2E4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_309',
    )

    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000F, 0x0080)
    SetChrFlags(0x0010, 0x0080)
    SetChrFlags(0x0011, 0x0080)

    def _loc_309(): pass

    label('loc_309')

    Return()

# id: 0x0001 offset: 0x30A
@scena.Code('Init')
def Init():
    OP_16(0x02, 0x00000FA0, 0xFFFD21A0, 0xFFFE5638, 0x00230026)

    ExecExpressionWithVar(
        0x2A,
        (
            (Expr.PushLong, 0x186A),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_22(0x01C8, 0x01, 0x64)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0260, 2, 0x1302)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_33D',
    )

    OP_6F(0x0000, 0)

    Jump('loc_344')

    def _loc_33D(): pass

    label('loc_33D')

    OP_6F(0x0000, 60)

    def _loc_344(): pass

    label('loc_344')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0260, 3, 0x1303)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_356',
    )

    OP_6F(0x0001, 0)

    Jump('loc_35D')

    def _loc_356(): pass

    label('loc_356')

    OP_6F(0x0001, 60)

    def _loc_35D(): pass

    label('loc_35D')

    Return()

# id: 0x0002 offset: 0x35E
@scena.Code('ReInit')
def ReInit():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_47C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_414',
    )

    ChrTalk(
        0x00FE,
        (
            '看来王立学院\n',
            '好像被敌人占领了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过还不明白敌人的意图……\n',
            '说不定什么时候\n',
            '又会发生同样的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为了慎重起见，村子和孤儿院\n',
            '都已经配置了警备人员。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    Jump('loc_479')

    def _loc_414(): pass

    label('loc_414')

    ChrTalk(
        0x00FE,
        (
            '实在不行\n',
            '只能让居民\n',
            '躲在警备艇里面避难……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就算导力炮不能使用\n',
            '避避难的用场还是可以起到的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_479(): pass

    label('loc_479')

    Jump('loc_557')

    def _loc_47C(): pass

    label('loc_47C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_557',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_50B',
    )

    ChrTalk(
        0x00FE,
        (
            '唔，你们是游击士吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '相信各位一看就知道，\n',
            '我们的警备艇是无法飞行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然请求过救援，\n',
            '但不知道要等多久……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    Jump('loc_557')

    def _loc_50B(): pass

    label('loc_50B')

    ChrTalk(
        0x00FE,
        (
            '救援来之前\n',
            '我们打算在这边待命。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们能保护自己。\n',
            '各位也不用担心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_557(): pass

    label('loc_557')

    TalkEnd(0x0008)

    Return()

# id: 0x0003 offset: 0x55B
@scena.Code('func_03_55B')
def func_03_55B():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_5D4',
    )

    ChrTalk(
        0x00FE,
        (
            '队，队长要我\n',
            '守卫这个地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '万一有什么情况，让我带着孩子们\n',
            '到警备艇避难。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉……责任重大啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6BF')

    def _loc_5D4(): pass

    label('loc_5D4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_6BF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_677',
    )

    ChrTalk(
        0x00FE,
        (
            '返回要塞途中\n',
            '又发生了那个现象。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然情况危急，\n',
            '总算还是想办法迫降了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '降落的地方\n',
            '还好是在沙滩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因此负伤的人\n',
            '也都是轻伤。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    Jump('loc_6BF')

    def _loc_677(): pass

    label('loc_677')

    ChrTalk(
        0x00FE,
        (
            '其中一名伤员\n',
            '被送去附近的村子了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还是躺在床上\n',
            '休息休息好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6BF(): pass

    label('loc_6BF')

    TalkEnd(0x0009)

    Return()

# id: 0x0004 offset: 0x6C3
@scena.Code('func_04_6C3')
def func_04_6C3():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_753',
    )

    ChrTalk(
        0x00FE,
        (
            '听说那些红色士兵们\n',
            '在这附近出现了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且根据传言，他们在\n',
            '这种情况下还用了枪不是吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '光靠这种剑\n',
            '要怎样对抗才好啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_81F')

    def _loc_753(): pass

    label('loc_753')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_81F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7D5',
    )

    ChrTalk(
        0x00FE,
        (
            '哎呀，这种时候\n',
            '居然还有人通过街道啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，请确保\n',
            '自己的安全吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不好意思，\n',
            '我也抽不出手来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    Jump('loc_81F')

    def _loc_7D5(): pass

    label('loc_7D5')

    ChrTalk(
        0x00FE,
        (
            '呼，救援部队\n',
            '还不来吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没有人会想要待在\n',
            '有魔兽出没的地方啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_81F(): pass

    label('loc_81F')

    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0x823
@scena.Code('func_05_823')
def func_05_823():
    UnlockAchievement(0x02, 0xE0, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0260, 2, 0x1302)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_900',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0000, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['虾米'], 1)"),
            Expr.Return,
        ),
        'loc_897',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['虾米']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1302)

    Jump('loc_8FD')

    def _loc_897(): pass

    label('loc_897')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['虾米']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['虾米']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0000, 60)
    OP_70(0x0000, 0x00000000)

    def _loc_8FD(): pass

    label('loc_8FD')

    Jump('loc_931')

    def _loc_900(): pass

    label('loc_900')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_931(): pass

    label('loc_931')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0006 offset: 0x93F
@scena.Code('func_06_93F')
def func_06_93F():
    UnlockAchievement(0x02, 0xE1, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0260, 3, 0x1303)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A1C',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0001, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['复苏药'], 1)"),
            Expr.Return,
        ),
        'loc_9B3',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['复苏药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1303)

    Jump('loc_A19')

    def _loc_9B3(): pass

    label('loc_9B3')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['复苏药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['复苏药']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0001, 60)
    OP_70(0x0001, 0x00000000)

    def _loc_A19(): pass

    label('loc_A19')

    Jump('loc_A4D')

    def _loc_A1C(): pass

    label('loc_A1C')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_A4D(): pass

    label('loc_A4D')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0007 offset: 0xA5B
@scena.Code('func_07_A5B')
def func_07_A5B():
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '北　玛西亚孤儿院',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0008 offset: 0xA9E
@scena.Code('func_08_A9E')
def func_08_A9E():
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '东　卢安市　　２３８塞尔矩\n',
            '西　玛诺利亚村　７４塞尔矩',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
