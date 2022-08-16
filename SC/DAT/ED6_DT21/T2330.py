import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T2330_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2330   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'T2330.x'
    header.mapIndex       = 1
    header.bgm            = 15
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT21/T2330._SN', 'ED6_DT21/T2330_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
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
        ('ED6_DT07/CH01270._CH', 'ED6_DT07/CH01270P._CP'),
        ('ED6_DT07/CH01030._CH', 'ED6_DT07/CH01030P._CP'),
        ('ED6_DT07/CH01563._CH', 'ED6_DT07/CH01563P._CP'),
        ('ED6_DT07/CH01120._CH', 'ED6_DT07/CH01120P._CP'),
        ('ED6_DT07/CH01760._CH', 'ED6_DT07/CH01760P._CP'),
        ('ED6_DT06/CH20020._CH', 'ED6_DT06/CH20020P._CP'),
        ('ED6_DT06/CH20021._CH', 'ED6_DT06/CH20021P._CP'),
        ('ED6_DT07/CH01300._CH', 'ED6_DT07/CH01300P._CP'),
    ]

# id: 0x10001 offset: 0xEA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '雷克斯',
            x                   = -25500,
            z                   = 0,
            y                   = 43210,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            name                = '卡拉',
            x                   = -37500,
            z                   = 0,
            y                   = 44500,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '达里奥',
            x                   = -37480,
            z                   = 200,
            y                   = 39900,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0115,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '奥维德',
            x                   = 1000,
            z                   = 0,
            y                   = 2330,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0000,
        ),
        ScenaNpcData(
            name                = '梅尔茨',
            x                   = -30680,
            z                   = 0,
            y                   = 44805,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = -2200,
            z                   = 0,
            y                   = 2490,
            direction           = 284,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '酒瓶',
            x                   = -37820,
            z                   = 750,
            y                   = 38730,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1966085,
            chipIndex           = 5,
            npcIndex            = 0x0166,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '酒瓶',
            x                   = -37470,
            z                   = 750,
            y                   = 38480,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1966085,
            chipIndex           = 5,
            npcIndex            = 0x0166,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '酒杯满',
            x                   = -37530,
            z                   = 750,
            y                   = 39070,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0166,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '酒杯空',
            x                   = -37260,
            z                   = 750,
            y                   = 38950,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 65542,
            chipIndex           = 6,
            npcIndex            = 0x0166,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '酒瓶',
            x                   = -37010,
            z                   = 800,
            y                   = 38560,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1900549,
            chipIndex           = 5,
            npcIndex            = 0x0166,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
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
        ScenaActorData(
            triggerX            = -37020,
            triggerZ            = 0,
            triggerY            = 42970,
            triggerRange        = 400,
            actorX              = -37500,
            actorZ              = 1500,
            actorY              = 44500,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -26870,
            triggerZ            = 0,
            triggerY            = 42820,
            triggerRange        = 400,
            actorX              = -25500,
            actorZ              = 1500,
            actorY              = 43210,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x292
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_2C4',
    )

    ChrClearFlags(0x000D, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000E, 0x0080)
    ChrSetFlags(0x000F, 0x0080)
    ChrSetFlags(0x0010, 0x0080)
    ChrSetFlags(0x0011, 0x0080)
    ChrSetFlags(0x0012, 0x0080)

    Jump('loc_2D5')

    def _loc_2C4(): pass

    label('loc_2C4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2D5',
    )

    ChrClearFlags(0x000C, 0x0080)

    def _loc_2D5(): pass

    label('loc_2D5')

    Return()

# id: 0x0001 offset: 0x2D6
@scena.Code('func_01_2D6')
def func_01_2D6():
    Return()

# id: 0x0002 offset: 0x2D7
@scena.Code('func_02_2D7')
def func_02_2D7():
    Call(0, 0x0003)

    Return()

# id: 0x0003 offset: 0x2DC
@scena.Code('func_03_2DC')
def func_03_2DC():
    TalkBegin(0x0008)
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
            TXT(0x02, '招牌菜『魅惑海鲜烧串』　600米拉\n'),
            TXT(0x03, '离开\n'),
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
        'loc_35A',
    )

    OP_0D()
    OP_A9(0x70)
    OP_56(0x00)
    TalkEnd(0x0008)

    Return()

    def _loc_35A(): pass

    label('loc_35A')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_466',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x12),
            (Expr.PushLong, 0x258),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_431',
    )

    RemoveMira(600)
    FadeOut(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    PlaySE(11, 0x00, 0x64)

    Talk(
        (
            TxtCtl.ShowAll,
            (TxtCtl.SetColor, 0x2),
            '魅惑海鲜烧串',
            (TxtCtl.SetColor, 0x0),
            '已经品尝了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetStatus(ChrTable['艾丝蒂尔'], 0xFD, 600)
    ChrSetStatus(ChrTable['约修亚'], 0xFD, 600)
    ChrSetStatus(ChrTable['雪拉扎德'], 0xFD, 600)
    ChrSetStatus(ChrTable['奥利维尔'], 0xFD, 600)
    ChrSetStatus(ChrTable['科洛丝'], 0xFD, 600)
    ChrSetStatus(ChrTable['阿加特'], 0xFD, 600)
    ChrSetStatus(ChrTable['提妲'], 0xFD, 600)
    ChrSetStatus(ChrTable['金'], 0xFD, 600)
    ChrSetStatus(ChrTable['凯文神父'], 0xFD, 600)

    If(
        (
            (Expr.Eval, "OP_40(0x020D, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_423',
    )

    If(
        (
            (Expr.Eval, "OP_AC(0x0001)"),
            Expr.Return,
        ),
        'loc_3F7',
    )

    Jump('loc_423')

    def _loc_3F7(): pass

    label('loc_3F7')

    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            TxtCtl.ShowAll,
            (TxtCtl.SetColor, 0x2),
            '魅惑海鲜烧串',
            (TxtCtl.SetColor, 0x0),
            '的做法已经学会了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_423(): pass

    label('loc_423')

    OP_56(0x00)
    FadeIn(1000, 0)

    Jump('loc_457')

    def _loc_431(): pass

    label('loc_431')

    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            '没有足够的米拉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeIn(300, 0)
    def _loc_457(): pass

    label('loc_457')

    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x0008)

    Return()

    def _loc_466(): pass

    label('loc_466')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_477',
    )

    TalkEnd(0x0008)

    Return()

    def _loc_477(): pass

    label('loc_477')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_506',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4E2',
    )

    ChrTalk(
        0x0008,
        (
            '受了伤的士兵\n',
            '似乎也好多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '反正警备艇也不能飞，\n',
            '现在还是希望他们好好休息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_503')

    def _loc_4E2(): pass

    label('loc_4E2')

    ChrTalk(
        0x0008,
        (
            '受了伤的士兵\n',
            '似乎也好多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_503(): pass

    label('loc_503')

    Jump('loc_96B')

    def _loc_506(): pass

    label('loc_506')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_5EF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_59A',
    )

    ChrTalk(
        0x0008,
        (
            '呀，欢迎。\n',
            '欢迎光临『白之木莲亭』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '进货虽然困难，\n',
            '里面还是和平时一样营业呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '因为在这种时候，\n',
            '想帮村民的忙嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_5EC')

    def _loc_59A(): pass

    label('loc_59A')

    ChrTalk(
        0x0008,
        (
            '进货虽然困难，\n',
            '不过，还是尽力在营业。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '这还多亏在村里\n',
            '采摘了许多食材呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5EC(): pass

    label('loc_5EC')

    Jump('loc_96B')

    def _loc_5EF(): pass

    label('loc_5EF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0245, 6, 0x122E)),
            Expr.Return,
        ),
        'loc_823',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_646',
    )

    ChrTalk(
        0x0008,
        (
            '这次选举\n',
            '我们店是投票所。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '承蒙大家关照\n',
            '我们也会努力干好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_820')

    def _loc_646(): pass

    label('loc_646')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_70F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_682',
    )

    ChrTalk(
        0x0008,
        (
            '就快到是市长选举了，\n',
            '该投票给谁呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_70C')

    def _loc_682(): pass

    label('loc_682')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '就快到是市长选举了，\n',
            '那么，该投票给谁呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '旅游业的发展是令人高兴，\n',
            '不过卢安还是港口城市嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '港口萧条了\n',
            '应该不大好吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_70C(): pass

    label('loc_70C')

    Jump('loc_820')

    def _loc_70F(): pass

    label('loc_70F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Return,
        ),
        'loc_780',
    )

    ChrTalk(
        0x0008,
        (
            '呀，莫非\n',
            '去看风车小屋了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '看了那景色的客人\n',
            '必定会再来的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '那里的风景\n',
            '就是那么好呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_820')

    def _loc_780(): pass

    label('loc_780')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_820',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_7CE',
    )

    ChrTalk(
        0x0008,
        (
            '要吃饭的话\n',
            '推荐新菜单哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '在我们这里是最受欢迎了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_820')

    def _loc_7CE(): pass

    label('loc_7CE')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '欢迎光临『白之木莲亭』。\n',
            '现在推荐新菜单哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '在我们这里是最受欢迎了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_820(): pass

    label('loc_820')

    Jump('loc_96B')

    def _loc_823(): pass

    label('loc_823')

    SetScenaFlags(ScenaFlag(0x0245, 6, 0x122E))
    ChrTurnDirection(0x0008, 0x0101, 0)

    ChrTalk(
        0x0008,
        (
            '欢迎光临『白之木莲亭』。\n',
            '没见过的脸呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '……不过，想一想\n',
            '又好像有见过的印象。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '以前来过吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1011F啊，还记得吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '时间比较久了，\n',
            '以前在这里买过便当哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '哦，是这样吗。\n',
            '那么试试新菜单怎样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '是我们这里现在\n',
            '最受欢迎的料理哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1018F哟～那倒是很令人期待。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '肚子饿了的话\n',
            '请务必试试。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_96B(): pass

    label('loc_96B')

    TalkEnd(0x0008)

    Return()

# id: 0x0004 offset: 0x96F
@scena.Code('func_04_96F')
def func_04_96F():
    Call(0, 0x0005)

    Return()

# id: 0x0005 offset: 0x974
@scena.Code('func_05_974')
def func_05_974():
    TalkBegin(0x0009)
    Call(6, 0x0006)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_98E',
    )

    OP_A9(0x6F)
    TalkEnd(0x0009)

    Return()

    def _loc_98E(): pass

    label('loc_98E')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_99F',
    )

    TalkEnd(0x0009)

    Return()

    def _loc_99F(): pass

    label('loc_99F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_A70',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A25',
    )

    ChrTalk(
        0x0009,
        (
            '警备艇好像还在海岸\n',
            '停靠着呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '导力器不能动的话，\n',
            '确实没办法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '那样的话倒不如\n',
            '大家都来村里的好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Jump('loc_A6D')

    def _loc_A25(): pass

    label('loc_A25')

    ChrTalk(
        0x0009,
        (
            '警备艇好像还在海岸\n',
            '停靠着呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '导力器不能动的话，\n',
            '确实没办法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A6D(): pass

    label('loc_A6D')

    Jump('loc_F11')

    def _loc_A70(): pass

    label('loc_A70')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_B53',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B06',
    )

    ChrTalk(
        0x0009,
        (
            '２楼的士兵\n',
            '是迫降的警备艇中的成员。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '村子被袭击的时候\n',
            '是他们保护了我们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '虽然伤得不重，\n',
            '但热情招待他是理所当然的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Jump('loc_B50')

    def _loc_B06(): pass

    label('loc_B06')

    ChrTalk(
        0x0009,
        (
            '乘坐警备艇的士兵\n',
            '保护了村子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '登上船撤退的时候\n',
            '发生了那个现象。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B50(): pass

    label('loc_B50')

    Jump('loc_F11')

    def _loc_B53(): pass

    label('loc_B53')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_C3B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_BBA',
    )

    ChrTalk(
        0x0009,
        (
            '哎呀，市长官邸现在\n',
            '不是戴尔蒙家的所有物了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '嗯～那样\n',
            '应该联络哪里才好呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C38')

    def _loc_BBA(): pass

    label('loc_BBA')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x0009,
        (
            '那位客人，真的\n',
            '是戴尔蒙家的管家吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '要是那样，得联络那里\n',
            '前来迎接他才行……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '喝得那么醉，\n',
            '一个人可回不去啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C38(): pass

    label('loc_C38')

    Jump('loc_F11')

    def _loc_C3B(): pass

    label('loc_C3B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_D1F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_C9D',
    )

    ChrTalk(
        0x0009,
        (
            '那位客人\n',
            '终于开始\n',
            '说胡话了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '『我不是我！』\n',
            '……之类的话都说出来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D1C')

    def _loc_C9D(): pass

    label('loc_C9D')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x0009,
        (
            '那位客人\n',
            '终于开始\n',
            '说胡话了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '『我不是我！』什么的\n',
            '话都说出来了，真是没救了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '呼，还是不要\n',
            '再拿酒出来了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D1C(): pass

    label('loc_D1C')

    Jump('loc_F11')

    def _loc_D1F(): pass

    label('loc_D1F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Return,
        ),
        'loc_DF7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_D84',
    )

    ChrTalk(
        0x0009,
        (
            '那个客人这么消沉，\n',
            '有些可怜的样子呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '也许真的是\n',
            '戴尔蒙家的管家也说不定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DF4')

    def _loc_D84(): pass

    label('loc_D84')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x0009,
        (
            '嗯～那个客人。\n',
            '有些可怜的样子呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '自己说自己是\n',
            '戴尔蒙家的管家……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '看那个样子\n',
            '说不定是真的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_DF4(): pass

    label('loc_DF4')

    Jump('loc_F11')

    def _loc_DF7(): pass

    label('loc_DF7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_F11',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_E7D',
    )

    ChrTalk(
        0x0009,
        (
            '那边酩酊大醉的人\n',
            '好像是戴尔蒙家的管家呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '不过，那样的话\n',
            '他说的事却很奇怪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '喝了那么多\n',
            '也难怪会这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F11')

    def _loc_E7D(): pass

    label('loc_E7D')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x0009,
        (
            '那边有个酩酊大醉的\n',
            '客人吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '那个人\n',
            '好像是戴尔蒙家的管家呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1004F咦？真的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '不知道是不是真的。\n',
            '只不过，他本人是那样说的哟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F11(): pass

    label('loc_F11')

    TalkEnd(0x0009)

    Return()

# id: 0x0006 offset: 0xF15
@scena.Code('func_06_F15')
def func_06_F15():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_11AB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 5, 0x1425)),
            Expr.Return,
        ),
        'loc_FA1',
    )

    ChrTalk(
        0x00FE,
        (
            '呜～……抽泣……\n',
            '那、那不是我……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '屋里的女佣们看到的……\n',
            '那、那个管家达里奥不是我……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呜呜～……抽泣……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11A8')

    def _loc_FA1(): pass

    label('loc_FA1')

    SetScenaFlags(ScenaFlag(0x0284, 5, 0x1425))

    ChrTalk(
        0x00FE,
        (
            '呜咿～……抽泣……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呜～…………\n',
            '那、那不是我……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#042F………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#042F（艾丝蒂尔……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '（这位…………\n',
            '　是戴尔蒙家的管家。)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1002F（嗯……\n',
            '是那家伙说的人吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#032F（唔、好像是呢。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_108B')
    def lambda_108B():
        ChrTurnDirection(0x00F7, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_108B)

    @scena.Lambda('lambda_1099')
    def lambda_1099():
        ChrTurnDirection(0x0104, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_1099)

    ChrTurnDirection(0x0101, 0x00FE, 400)
    Sleep(250)

    ChrTalk(
        0x00FE,
        (
            '呜呜～……那，那……\n',
            '那不是我……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '女佣们看见的我……\n',
            '管家达里奥不是我……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呜呜～……抽泣……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1002F（……………………）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '（那家伙说的事……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_117F',
    )

    ChrTalk(
        0x0103,
        (
            '#022F（嗯嗯……\n',
            '好像是真的呢。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11A8')

    def _loc_117F(): pass

    label('loc_117F')

    ChrTalk(
        0x0106,
        (
            '#050F（啊啊……\n',
            '　好像不是唬人的。)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_11A8(): pass

    label('loc_11A8')

    Jump('loc_14A8')

    def _loc_11AB(): pass

    label('loc_11AB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_12A1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_121E',
    )

    ChrTalk(
        0x00FE,
        (
            '抽泣……\n',
            '谁、谁来听我说啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '市长官邸的那个我……\n',
            '抽泣……不是我！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呜～……抽泣……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_129E')

    def _loc_121E(): pass

    label('loc_121E')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '呜～……抽泣……\n',
            '呜呜～……相信我……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '市长官邸那个我……\n',
            '抽泣……不是我！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只、只能这样……\n',
            '呜～……考虑了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_129E(): pass

    label('loc_129E')

    Jump('loc_14A8')

    def _loc_12A1(): pass

    label('loc_12A1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Return,
        ),
        'loc_13AE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_132B',
    )

    ChrTalk(
        0x00FE,
        (
            '呜～……抽泣……\n',
            '很、很奇怪啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '得到休假的我……\n',
            '怎、怎么会在屋子里？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '抽泣……那、那么……\n',
            '就有两个我！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_13AB')

    def _loc_132B(): pass

    label('loc_132B')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '呜～……抽泣……\n',
            '说、说起来很奇怪啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我、我得到休假……\n',
            '不在……宅邸的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '抽泣……为何大家\n',
            '都、都说我在！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_13AB(): pass

    label('loc_13AB')

    Jump('loc_14A8')

    def _loc_13AE(): pass

    label('loc_13AE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_14A8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1427',
    )

    ChrTalk(
        0x00FE,
        (
            '老……老爷被逮捕什么的……\n',
            '肯、肯定搞错了…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我不在的时候……\n',
            '到、到底发生了什么…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_14A8')

    def _loc_1427(): pass

    label('loc_1427')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '呜～……抽泣……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '老……老爷被逮捕什么的……\n',
            '肯、肯定搞错了…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我不在的时候……\n',
            '到、到底发生了什么…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_14A8(): pass

    label('loc_14A8')

    TalkEnd(0x00FE)

    Return()

# id: 0x0007 offset: 0x14AC
@scena.Code('func_07_14AC')
def func_07_14AC():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_14B9',
    )

    Jump('loc_1564')

    def _loc_14B9(): pass

    label('loc_14B9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_1564',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_1503',
    )

    ChrTalk(
        0x00FE,
        (
            '这里的便当很好吃。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是工作空闲时的\n',
            '小小乐趣哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1564')

    def _loc_1503(): pass

    label('loc_1503')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '啊，大家辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我正好来这里\n',
            '消灭通缉魔兽！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '近来魔兽变得很强\n',
            '说实话真是棘手。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1564(): pass

    label('loc_1564')

    TalkEnd(0x00FE)

    Return()

# id: 0x0008 offset: 0x1568
@scena.Code('func_08_1568')
def func_08_1568():
    TalkBegin(0x000D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_168D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1630',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然伤势没有大碍，\n',
            '可以返回船上……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过宿驿的人们很亲切，\n',
            '总觉得有点盛情难却啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '感觉因为这事故\n',
            '体会到了自己的使命呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样保护人们\n',
            '就是我们士兵的任务啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    Jump('loc_168A')

    def _loc_1630(): pass

    label('loc_1630')

    ChrTalk(
        0x00FE,
        (
            '与宿驿的人们互相接触\n',
            '体会到了自己的使命呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样保护人们\n',
            '就是我们士兵的任务啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_168A(): pass

    label('loc_168A')

    Jump('loc_1777')

    def _loc_168D(): pass

    label('loc_168D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1777',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1725',
    )

    ChrTalk(
        0x00FE,
        (
            '航行中的警备艇全导力\n',
            '都下降了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '由于高度低\n',
            '才偶然得救……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '由于迫降的冲击，\n',
            '我身上青一块紫一块的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好痛痛痛……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    Jump('loc_1777')

    def _loc_1725(): pass

    label('loc_1725')

    ChrTalk(
        0x00FE,
        (
            '航行中的警备艇全导力\n',
            '都下降了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '由于迫降的冲击\n',
            '我身上也是青一块紫一块。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1777(): pass

    label('loc_1777')

    TalkEnd(0x000D)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
