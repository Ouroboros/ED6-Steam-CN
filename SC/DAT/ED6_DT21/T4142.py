import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T4142_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4142   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4142.x'
    header.mapIndex       = 1
    header.bgm            = 34
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
        ('ED6_DT07/CH01100._CH', 'ED6_DT07/CH01100P._CP'),
        ('ED6_DT07/CH01150._CH', 'ED6_DT07/CH01150P._CP'),
        ('ED6_DT07/CH01023._CH', 'ED6_DT07/CH01023P._CP'),
        ('ED6_DT07/CH02060._CH', 'ED6_DT07/CH02060P._CP'),
        ('ED6_DT07/CH01210._CH', 'ED6_DT07/CH01210P._CP'),
        ('ED6_DT07/CH01143._CH', 'ED6_DT07/CH01143P._CP'),
    ]

# id: 0x10001 offset: 0xDA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '巴拉尔',
            x                   = 61020,
            z                   = 0,
            y                   = 2490,
            direction           = 180,
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
            name                = '科蕾蒂',
            x                   = 4560,
            z                   = 0,
            y                   = 2500,
            direction           = 186,
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
            name                = '彭萨',
            x                   = 4500,
            z                   = 100,
            y                   = -3850,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0115,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '奈尔',
            x                   = -64450,
            z                   = 0,
            y                   = 60580,
            direction           = 1,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '诺蒂亚',
            x                   = -53860,
            z                   = 250,
            y                   = 121340,
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
            name                = '法尔茨',
            x                   = -59030,
            z                   = 100,
            y                   = 59540,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0115,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
    )

# id: 0x10002 offset: 0x19A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x19A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x19A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 60700,
            triggerZ            = 0,
            triggerY            = 550,
            triggerRange        = 400,
            actorX              = 61020,
            actorZ              = 1500,
            actorY              = 2490,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 4530,
            triggerZ            = 0,
            triggerY            = 590,
            triggerRange        = 400,
            actorX              = 4560,
            actorZ              = 1500,
            actorY              = 2500,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x1E2
@scena.Code('Init')
def Init():
    Return()

# id: 0x0001 offset: 0x1E3
@scena.Code('func_01_1E3')
def func_01_1E3():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 2, 0x163A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1F4',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x54),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1F4(): pass

    label('loc_1F4')

    Return()

# id: 0x0002 offset: 0x1F5
@scena.Code('func_02_1F5')
def func_02_1F5():
    Call(0, 0x0003)

    Return()

# id: 0x0003 offset: 0x1FA
@scena.Code('func_03_1FA')
def func_03_1FA():
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
            TXT(0x02, '招牌菜『完熟咖喱饭』　900米拉\n'),
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

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_276',
    )

    FadeIn(300, 0)
    OP_0D()
    OP_A9(0xCB)
    OP_56(0x00)
    TalkEnd(0x0008)

    Return()

    def _loc_276(): pass

    label('loc_276')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_380',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x12),
            (Expr.PushLong, 0x384),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_34B',
    )

    RemoveMira(900)
    FadeOut(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    PlaySE(11, 0x00, 0x64)

    Talk(
        (
            TxtCtl.ShowAll,
            (TxtCtl.SetColor, 0x2),
            '完熟咖喱饭',
            (TxtCtl.SetColor, 0x0),
            '已经品尝过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetStatus(ChrTable['艾丝蒂尔'], 0xFD, 1600)
    ChrSetStatus(ChrTable['约修亚'], 0xFD, 1600)
    ChrSetStatus(ChrTable['雪拉扎德'], 0xFD, 1600)
    ChrSetStatus(ChrTable['奥利维尔'], 0xFD, 1600)
    ChrSetStatus(ChrTable['科洛丝'], 0xFD, 1600)
    ChrSetStatus(ChrTable['阿加特'], 0xFD, 1600)
    ChrSetStatus(ChrTable['提妲'], 0xFD, 1600)
    ChrSetStatus(ChrTable['金'], 0xFD, 1600)
    ChrSetStatus(ChrTable['凯文神父'], 0xFD, 1600)

    If(
        (
            (Expr.Eval, "OP_40(0x020D, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_33D',
    )

    If(
        (
            (Expr.Eval, "OP_AC(0x000B)"),
            Expr.Return,
        ),
        'loc_313',
    )

    Jump('loc_33D')

    def _loc_313(): pass

    label('loc_313')

    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            TxtCtl.ShowAll,
            (TxtCtl.SetColor, 0x2),
            '完熟咖喱饭',
            (TxtCtl.SetColor, 0x0),
            '的做法已经学会了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_33D(): pass

    label('loc_33D')

    OP_56(0x00)
    FadeIn(1000, 0)

    Jump('loc_371')

    def _loc_34B(): pass

    label('loc_34B')

    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            '没有足够的米拉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeIn(300, 0)
    def _loc_371(): pass

    label('loc_371')

    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x0008)

    Return()

    def _loc_380(): pass

    label('loc_380')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_39A',
    )

    FadeIn(300, 0)
    TalkEnd(0x0008)

    Return()

    def _loc_39A(): pass

    label('loc_39A')

    FadeIn(300, 0)
    TalkEnd(0x0008)

    Return()

# id: 0x0004 offset: 0x3A7
@scena.Code('func_04_3A7')
def func_04_3A7():
    Call(0, 0x0005)

    Return()

# id: 0x0005 offset: 0x3AC
@scena.Code('func_05_3AC')
def func_05_3AC():
    TalkBegin(0x0009)
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
            TXT(0x02, '招牌菜『热海汁』　1200米拉\n'),
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

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_425',
    )

    FadeIn(300, 0)
    OP_0D()
    OP_A9(0xCA)
    OP_56(0x00)
    TalkEnd(0x0009)

    Return()

    def _loc_425(): pass

    label('loc_425')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_527',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x12),
            (Expr.PushLong, 0x4B0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_4F2',
    )

    RemoveMira(1200)
    FadeOut(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    PlaySE(11, 0x00, 0x64)

    Talk(
        (
            TxtCtl.ShowAll,
            (TxtCtl.SetColor, 0x2),
            '热海汁',
            (TxtCtl.SetColor, 0x0),
            '已经品尝过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetStatus(ChrTable['艾丝蒂尔'], 0xFD, 2500)
    ChrSetStatus(ChrTable['约修亚'], 0xFD, 2500)
    ChrSetStatus(ChrTable['雪拉扎德'], 0xFD, 2500)
    ChrSetStatus(ChrTable['奥利维尔'], 0xFD, 2500)
    ChrSetStatus(ChrTable['科洛丝'], 0xFD, 2500)
    ChrSetStatus(ChrTable['阿加特'], 0xFD, 2500)
    ChrSetStatus(ChrTable['提妲'], 0xFD, 2500)
    ChrSetStatus(ChrTable['金'], 0xFD, 2500)
    ChrSetStatus(ChrTable['凯文神父'], 0xFD, 2500)

    If(
        (
            (Expr.Eval, "OP_40(0x020D, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4E4',
    )

    If(
        (
            (Expr.Eval, "OP_AC(0x0002)"),
            Expr.Return,
        ),
        'loc_4BE',
    )

    Jump('loc_4E4')

    def _loc_4BE(): pass

    label('loc_4BE')

    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            TxtCtl.ShowAll,
            (TxtCtl.SetColor, 0x2),
            '热海汁',
            (TxtCtl.SetColor, 0x0),
            '的做法已经学会了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4E4(): pass

    label('loc_4E4')

    OP_56(0x00)
    FadeIn(1000, 0)

    Jump('loc_518')

    def _loc_4F2(): pass

    label('loc_4F2')

    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            '没有足够的米拉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeIn(300, 0)
    def _loc_518(): pass

    label('loc_518')

    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x0009)

    Return()

    def _loc_527(): pass

    label('loc_527')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_541',
    )

    FadeIn(300, 0)
    TalkEnd(0x0009)

    Return()

    def _loc_541(): pass

    label('loc_541')

    FadeIn(300, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 2, 0x163A)),
            Expr.Return,
        ),
        'loc_581',
    )

    ChrTalk(
        0x0009,
        (
            '……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '刚才有没有听见\n',
            '外面有鸟叫？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5C3')

    def _loc_581(): pass

    label('loc_581')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 1, 0x1639)),
            Expr.Return,
        ),
        'loc_5C3',
    )

    ChrTalk(
        0x0009,
        (
            '好了，忙的时间也过去了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '得准备明天的\n',
            '工作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5C3(): pass

    label('loc_5C3')

    TalkEnd(0x0009)

    Return()

# id: 0x0006 offset: 0x5C7
@scena.Code('func_06_5C7')
def func_06_5C7():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 2, 0x163A)),
            Expr.Return,
        ),
        'loc_614',
    )

    ChrTalk(
        0x00FE,
        (
            '好，回家\n',
            '洗个澡吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一天的紧绷还是要\n',
            '靠洗澡来消除啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6AC')

    def _loc_614(): pass

    label('loc_614')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 1, 0x1639)),
            Expr.Return,
        ),
        'loc_6AC',
    )

    ChrTalk(
        0x00FE,
        (
            '对了，我在港口工作的\n',
            '朋友告诉我一些奇怪的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好像说本来应该没人的仓库\n',
            '却每晚都发出声音来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '难道……\n',
            '难道是幽灵！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '怕怕……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6AC(): pass

    label('loc_6AC')

    TalkEnd(0x00FE)

    Return()

# id: 0x0007 offset: 0x6B0
@scena.Code('func_07_6B0')
def func_07_6B0():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C9, 2, 0x164A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_944',
    )

    ChrTalk(
        0x000B,
        (
            '#0270270344V#143F哟，什么什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010270345V#1002F奈尔，这附近没\n',
            '发生什么怪事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0270270346V#140F怪事……\n',
            '是说什么案子吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010270347V#1002F嗯，比如有什么骚动\n',
            '或者什么可疑的人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0270270348V#142F唔～没看到什么\n',
            '可疑的人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270270349V如果有什么骚动，我们的人\n',
            '也应该早已听说了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010270350V#1003F是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0270270351V#143F……你是不是碰到了什么问题？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270270352V#141F那我也一起去。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270270353V我马上准备一下，\n',
            '在一楼的大厅等我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010270354V#1000F啊，嗯、嗯。\n',
            '不过要快一点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0270270355V#143F什么？原来是紧急情况啊？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270270356V#140F那么\n',
            '你们赶快先去！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010270357V#1002F嗯，抱歉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x02C9, 2, 0x164A))

    Jump('loc_9B7')

    def _loc_944(): pass

    label('loc_944')

    ChrTalk(
        0x000B,
        (
            '#0270270358V#140F现场在西街区附近吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270270359V我一准备好\n',
            '就去追你们。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270270360V你们现在就\n',
            '赶快先去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9B7(): pass

    label('loc_9B7')

    TalkEnd(0x000B)

    Return()

# id: 0x0008 offset: 0x9BB
@scena.Code('func_08_9BB')
def func_08_9BB():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '在这种时候只有记者还全体\n',
            '坚守岗位，真悲哀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过这工作很有意义。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0009 offset: 0xA0D
@scena.Code('func_09_A0D')
def func_09_A0D():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '啊～好想快点回家吃饭哟～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
