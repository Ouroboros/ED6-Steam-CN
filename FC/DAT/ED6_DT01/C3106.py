import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C3106_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C3106   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'C3106.x'
    header.mapIndex       = 1
    header.bgm            = 34
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
        ('ED6_DT07/CH02450._CH', 'ED6_DT07/CH02450P._CP'),
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
        ('ED6_DT07/CH01310._CH', 'ED6_DT07/CH01310P._CP'),
    ]

# id: 0x10001 offset: 0xC2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '希德少校',
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
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
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
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
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
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '王国军军官',
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
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
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
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x162
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x162
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x162
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 16500,
            triggerZ            = 0,
            triggerY            = 42000,
            triggerRange        = 800,
            actorX              = 16500,
            actorZ              = 1000,
            actorY              = 42000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -12960,
            triggerZ            = 0,
            triggerY            = 34480,
            triggerRange        = 1000,
            actorX              = -12960,
            actorZ              = 1000,
            actorY              = 34480,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x1AA
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_1C5',
    )

    MapSetFlags(0x40000000)
    FormationAddMember(0xFF, 0xFF)
    MapSetFlags(0x10000000)
    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, func_02_226)

    def _loc_1C5(): pass

    label('loc_1C5')

    Return()

# id: 0x0001 offset: 0x1C6
@scena.Code('func_01_1C6')
def func_01_1C6():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AE, 1, 0x571)),
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_1DC',
    )

    OP_65(0x00, 0x0001)

    def _loc_1DC(): pass

    label('loc_1DC')

    LoadEffect(0x00, 'map\\\\mp027_00.eff')
    PlayEffect(0x00, 0x00, 0x00FF, -12960, 1000, 34480, 0, 0, 0, 1300, 1300, 1300, 0x00FF, 0, 0, 0, 0)

    Return()

# id: 0x0002 offset: 0x226
@scena.Code('func_02_226')
def func_02_226():
    MapClearFlags(0x10000000)
    ChrSetPos(0x0000, -10080, 0, 27870, 0)
    ChrSetPos(0x0001, -10080, 0, 27870, 0)
    ChrSetPos(0x0002, -10080, 0, 27870, 0)
    ChrSetPos(0x0003, -10080, 0, 27870, 0)
    EventBegin(0x00)
    CameraMove(-1220, 0, 23900, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(4460, 0)
    OP_6C(67000, 0)
    OP_6E(423, 0)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetFlags(0x0009, 0x0040)
    ChrSetFlags(0x000A, 0x0040)
    ChrSetFlags(0x000B, 0x0040)
    ChrSetPos(0x0008, -11370, 0, 21640, 270)
    ChrSetPos(0x0009, -13090, 0, 22310, 90)
    ChrSetPos(0x000A, -13360, 0, 21070, 90)

    @scena.Lambda('lambda_0305')
    def lambda_0305():
        OP_6C(45000, 8000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_0305)

    FadeIn(2000, 0)
    OP_0D()

    @scena.Lambda('lambda_031F')
    def lambda_031F():
        OP_6E(262, 6000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_031F)

    @scena.Lambda('lambda_032F')
    def lambda_032F():
        CameraSetDistance(3250, 6000)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_032F)

    CameraMove(-12330, 0, 21630, 6000)

    ChrTalk(
        0x0008,
        (
            '#0620090884V#701F辛苦你们了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620090885V搬集装箱的事明天再来做吧。\n',
            '今天你们就先回兵营休息一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#4190090886V那、那个，少校……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#4190090887V这几天的非常体制，\n',
            '还要持续到什么时候啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0620090888V#700F……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2490090889V是、是啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2490090890V为什么我们正规军\n',
            '非要听那帮家伙的指挥不可……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0620090891V#703F你们说的意思我也很清楚……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620090892V但军人不该对上级的决定抱有质疑。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620090893V#701F而且……\n',
            '正所谓隔墙有耳。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620090894V你们要注意谨慎发言。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#4190090895V是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2490090896V明、明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000A, 270, 400)

    @scena.Lambda('lambda_058F')
    def lambda_058F():
        ChrWalkTo(0x00FE, -22160, 0, 22550, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_058F)

    Sleep(100)

    ChrSetDirection(0x0009, 270, 400)
    ChrWalkTo(0x0009, -22160, 0, 22550, 3000, 0x00)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x000A, 0x0080)

    ChrTalk(
        0x0008,
        (
            '#0620090897V#703F呼……\n',
            '真是问心有愧啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x000B, -22160, 0, 22550, 0)
    ChrClearFlags(0x000B, 0x0080)

    @scena.Lambda('lambda_061A')
    def lambda_061A():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_061A')

    DispatchAsync2(0x0008, 0x0001, lambda_061A)

    ChrWalkTo(0x000B, -13260, 0, 22810, 4000, 0x00)
    ChrTurnDirection(0x000B, 0x0008, 400)

    ChrTalk(
        0x000B,
        (
            '#2440090898V报告少校！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2440090899V凯诺娜上尉\n',
            '有急事找您，\n',
            '麻烦您马上过去一趟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0620090900V#700F是吗……知道了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620090901V#703F没办法……\n',
            '又要去听那只母狐狸训话了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_06FF')
    def lambda_06FF():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_06FF')

    DispatchAsync2(0x000B, 0x0001, lambda_06FF)

    @scena.Lambda('lambda_0710')
    def lambda_0710():
        ChrWalkTo(0x00FE, -22160, 0, 22550, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0710)

    Sleep(1000)

    ChrWalkTo(0x000B, -22160, 0, 22550, 3000, 0x00)
    CameraMove(-9480, 0, 27600, 5000)
    PlaySE(169, 0x00, 0x64)
    OP_B0(0x0012, 0x78)
    OP_70(0x0012, 180)
    OP_73(0x0012)
    Sleep(500)

    @scena.Lambda('lambda_076D')
    def lambda_076D():
        CameraMove(-7220, 0, 27280, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_076D)

    @scena.Lambda('lambda_0785')
    def lambda_0785():
        OP_6C(21000, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0785)

    @scena.Lambda('lambda_0795')
    def lambda_0795():
        CameraSetDistance(2800, 7000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_0795)

    ChrSetFlags(0x0106, 0x0004)
    ChrSetFlags(0x0107, 0x0004)
    ChrSetFlags(0x0101, 0x0004)
    ChrSetFlags(0x0102, 0x0004)
    ChrWalkTo(0x0106, -7170, 0, 28220, 3000, 0x00)
    ChrSetDirection(0x0106, 156, 400)
    ChrWalkTo(0x0107, -6220, 0, 27310, 3000, 0x00)
    ChrSetDirection(0x0107, 304, 400)
    ChrWalkTo(0x0101, -7020, 0, 26580, 3000, 0x00)
    ChrSetDirection(0x0101, 342, 400)
    ChrWalkTo(0x0102, -7970, 0, 27070, 3000, 0x00)
    ChrSetDirection(0x0102, 71, 400)
    ChrClearFlags(0x0106, 0x0004)
    ChrClearFlags(0x0107, 0x0004)
    ChrClearFlags(0x0101, 0x0004)
    ChrClearFlags(0x0102, 0x0004)
    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010090902V#007F呼～\n',
            '刚才真是太挤了～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010090903V#008F提妲，不要紧吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070090904V#066F嗯，还好呢。\n',
            '只是头有点晕乎乎的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070090905V不过装置能够运作正常，\n',
            '辛苦一点也是值得的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050090906V#053F嗯，了不起啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050090907V#051F虽然我之前反对你跟着来……\n',
            '不过看来有你在一起是正确的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070090908V#067F嘿嘿……\n',
            '谢谢，阿加特大哥哥。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070090909V不过真是被安东尼吓了一跳呢。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010090910V#007F嗯嗯，\n',
            '正好就是旁边的集装箱。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010090911V我还以为死定了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020090912V#010F我想那只猫是维修长特意放进去的。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020090913V多亏有了它的帮忙，\n',
            '刚才士兵的警戒也放松了很多。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020090914V而且维修长本人的应对也很冷静。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070090915V#560F呵呵……\n',
            '维修长叔叔也许为了我们才这么做。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050090916V#051F看来大叔很有一套嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050090917V那么我们就开始行动吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_AD('ED6_DT04/C_VIS018._CH', 0x0000, 0x0000, 0x000001F4)
    Sleep(1500)

    OP_77(0x00, 0x00, 0x00, 0x00, 0x00000000)
    SetMessageWindowPos(75, 300, -1, -1)
    TalkSetChrName('阿加特')

    Talk(
        (
            '#0050090918V',
            (TxtCtl.SetColor, 0x0),
            '#050F我们现在身处的飞艇停机坪\n',
            '——就在这附近。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_AE(0x000003E8)
    Sleep(500)

    OP_AD('ED6_DT04/C_VIS025._CH', 0x0000, 0x0000, 0x000001F4)
    Sleep(1500)

    SetMessageWindowPos(75, 300, -1, -1)
    TalkSetChrName('阿加特')

    Talk(
        (
            '#0050090919V#050F胡乱搜索是肯定无法\n',
            '找到老爷子被关押的位置的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050090920V艾丝蒂尔，\n',
            '你在地图上找找看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(400, 400, -1, -1)
    TalkSetChrName('艾丝蒂尔')

    Talk(
        (
            '#0010090921V#004F咦？\n',
            '为、为什么要我找？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(75, 300, -1, -1)
    TalkSetChrName('阿加特')

    Talk(
        (
            '#0050090922V#051F作为你的游击士前辈，\n',
            '想趁此测试一下你的洞察力而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050090923V喂，没时间了。\n',
            '快点给我找找看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
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
        12,
        12,
        0,
        (
            TXT(0x00, '【西南的兵营】\n'),
            TXT(0x01, '【中央的司令部】\n'),
            TXT(0x02, '【中央的研究所】\n'),
            TXT(0x03, '【东北的监视塔】\n'),
            TXT(0x04, '【南边的正门】\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_56(0x00)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_DC3'),
        (0x00000001, 'loc_F96'),
        (0x00000002, 'loc_10DF'),
        (0x00000003, 'loc_1272'),
        (0x00000004, 'loc_143C'),
        (-1, 'loc_15D6'),
    )

    def _loc_DC3(): pass

    label('loc_DC3')

    SetMessageWindowPos(75, 300, -1, -1)
    TalkSetChrName('阿加特')

    Talk(
        (
            '#0050090924V#053F虽然可能性并非为零，\n',
            '但这处的普通士兵肯定会很多。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050090925V考虑到保守军事机密，\n',
            '博士在别处的可能性比较高。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(400, 400, -1, -1)
    TalkSetChrName('艾丝蒂尔')

    Talk(
        (
            '#0010090926V#007F嗯，的确……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(75, 300, -1, -1)
    TalkSetChrName('阿加特')

    Talk(
        (
            '#0050090927V#050F约修亚，\n',
            '你的意见又如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(150, 350, -1, -1)
    TalkSetChrName('约修亚')

    Talk(
        (
            '#0020090928V#012F中央的研究所……\n',
            '我觉得博士最有可能在那里。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020090929V研究所有一个单独的区划，\n',
            '把博士关在那里也能掩人耳目地做研究。\n',
            '所以我认为博士在研究所的可能性最高。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_15D6')

    def _loc_F96(): pass

    label('loc_F96')

    SetMessageWindowPos(75, 300, -1, -1)
    TalkSetChrName('阿加特')

    Talk(
        (
            '#0050090930V#053F这里的可能性虽然很高，\n',
            '但其实还有更可疑的地方。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050090931V#050F约修亚，\n',
            '你的意见又如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(150, 350, -1, -1)
    TalkSetChrName('约修亚')

    Talk(
        (
            '#0020090932V#012F中央的研究所……\n',
            '我觉得博士最有可能在那里。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020090933V研究所有一个单独的区划，\n',
            '把博士关在那里也能掩人耳目地做研究。\n',
            '所以我认为博士在研究所的可能性最高。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_15D6')

    def _loc_10DF(): pass

    label('loc_10DF')

    SetMessageWindowPos(75, 300, -1, -1)
    TalkSetChrName('阿加特')

    Talk(
        (
            '#0050090934V#052F哦……不错嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(400, 400, -1, -1)
    TalkSetChrName('艾丝蒂尔')

    Talk(
        (
            '#0010090935V#502F哼哼，这太简单不过了⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(75, 300, -1, -1)
    TalkSetChrName('阿加特')

    Talk(
        (
            '#0050090936V#551F这家伙又在得意忘形了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050090937V#050F约修亚，\n',
            '你的意见怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(150, 350, -1, -1)
    TalkSetChrName('约修亚')

    Talk(
        (
            '#0020090938V#012F我也觉得那里可能性最高。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020090939V研究所有一个单独的区划，\n',
            '把博士关在那里也能掩人耳目地做研究。\n',
            '所以我认为博士在研究所的可能性最高。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_15D6')

    def _loc_1272(): pass

    label('loc_1272')

    SetMessageWindowPos(75, 300, -1, -1)
    TalkSetChrName('阿加特')

    Talk(
        (
            '#0050090940V#552F原来如此……\n',
            '这地方出入的人应该很少。\n',
            '这里的可能性虽然很高，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050090941V#051F但其实还有更可疑的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(400, 400, -1, -1)
    TalkSetChrName('艾丝蒂尔')

    Talk(
        (
            '#0010090942V#505F是这样吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(75, 300, -1, -1)
    TalkSetChrName('阿加特')

    Talk(
        (
            '#0050090943V#050F约修亚，\n',
            '你的意见又如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(150, 350, -1, -1)
    TalkSetChrName('约修亚')

    Talk(
        (
            '#0020090944V#012F中央的研究所……\n',
            '我觉得博士最有可能在那里。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020090945V研究所有一个单独的区划，\n',
            '把博士关在那里也能掩人耳目地做研究。\n',
            '所以我认为博士在研究所的可能性最高。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_15D6')

    def _loc_143C(): pass

    label('loc_143C')

    SetMessageWindowPos(75, 300, -1, -1)
    TalkSetChrName('阿加特')

    Talk(
        (
            '#0050090946V#551F那里是要塞的出口。\n',
            '用常识想想也知道不会在那种地方啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(400, 400, -1, -1)
    TalkSetChrName('艾丝蒂尔')

    Talk(
        (
            '#0010090947V#007F啊……是哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(75, 300, -1, -1)
    TalkSetChrName('阿加特')

    Talk(
        (
            '#0050090948V#050F约修亚，\n',
            '你的意见又如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(150, 350, -1, -1)
    TalkSetChrName('约修亚')

    Talk(
        (
            '#0020090949V#012F中央的研究所……\n',
            '我觉得博士最有可能在那里。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020090950V研究所有一个单独的区划，\n',
            '把博士关在那里也能掩人耳目地做研究。\n',
            '所以我认为博士在研究所的可能性最高。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_15D6')

    def _loc_15D6(): pass

    label('loc_15D6')

    SetMessageWindowPos(75, 300, -1, -1)
    TalkSetChrName('阿加特')

    Talk(
        (
            '#0050090951V#053F嗯，就这样了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_AE(0x000003E8)
    Sleep(500)

    OP_AD('ED6_DT04/C_VIS026._CH', 0x0000, 0x0000, 0x000001F4)
    Sleep(1500)

    SetMessageWindowPos(75, 300, -1, -1)
    TalkSetChrName('阿加特')

    Talk(
        (
            '#0050090952V#050F时间紧迫。\n',
            '就先从那里开始调查吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(150, 350, -1, -1)
    TalkSetChrName('约修亚')

    Talk(
        (
            '#0020090953V#010F阿加特兄，\n',
            '逃跑的路线要怎么决定？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(75, 300, -1, -1)
    TalkSetChrName('阿加特')

    Talk(
        (
            '#0050090954V#052F啊，对了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050090955V在这个停机坪的对面\n',
            '有个延伸到瓦雷利亚湖的码头。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_AE(0x000003E8)
    Sleep(500)

    OP_AD('ED6_DT04/C_VIS027._CH', 0x0000, 0x0000, 0x000001F4)
    Sleep(1500)

    RemoveItem(0x0359, 1)
    AddItem(0x035A, 1)
    SetMessageWindowPos(75, 300, -1, -1)
    TalkSetChrName('阿加特')

    Talk(
        (
            '#0050090956V#050F救出老爷子后就在那里抢船逃走。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(400, 400, -1, -1)
    TalkSetChrName('艾丝蒂尔')

    Talk(
        (
            '#0010090957V#002F嗯……明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_77(0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_AE(0x000001F4)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010090958V#006F那么，\n',
            '赶快向西北的研究所进发吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010090959V提妲，\n',
            '不要离开我们身边哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070090960V#062F嗯、嗯……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000B, 0x0080)
    EventEnd(0x00)

    Return()

# id: 0x0003 offset: 0x1887
@scena.Code('func_03_1887')
def func_03_1887():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_192F',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0106,
        (
            '#0050090961V#050F这边的楼梯是往码头去的。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050090962V回来的时候就从这里逃走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010090963V#006F好，知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020090964V#012F明白。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1989')

    def _loc_192F(): pass

    label('loc_192F')

    ChrTalk(
        0x0106,
        (
            '#0050090965V#050F这边的楼梯是往码头去的。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050090966V回来的时候就从这里逃走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1989(): pass

    label('loc_1989')

    TalkEnd(0x00FF)

    Return()

# id: 0x0004 offset: 0x198D
@scena.Code('func_04_198D')
def func_04_198D():
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
        'loc_1BA6',
    )

    FadeIn(100, 0)
    Sleep(500)

    OP_26(13)
    StopEffect(0x00, 0x02)
    PlayEffect(0x00, 0x02, 0x00FF, -12960, 1000, 34480, 0, 0, 0, 700, 700, 700, 0x00FF, 0, 0, 0, 0)
    OP_6F(0x0011, 0)
    OP_70(0x0011, 50)
    OP_73(0x0011)
    OP_20(0x00000BB8)
    PlaySE(12, 0x00, 0x64)
    StopEffect(0x02, 0x02)
    LoadEffect(0x01, 'map\\\\mp027_01.eff')
    PlayEffect(0x01, 0x01, 0x00FF, -12960, 1000, 34480, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
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
    ChrSetPos(0x0000, -14350, 0, 33010, 39)
    ChrSetPos(0x0001, -14350, 0, 33010, 39)
    ChrSetPos(0x0002, -14350, 0, 33010, 39)
    ChrSetPos(0x0003, -14350, 0, 33010, 39)
    OP_69(0x0000, 0)
    OP_30(0x00)
    Sleep(3500)

    StopEffect(0x01, 0x02)
    LoadEffect(0x00, 'map\\\\mp027_00.eff')
    PlayEffect(0x00, 0x00, 0x00FF, -12960, 1000, 34480, 0, 0, 0, 1300, 1300, 1300, 0x00FF, 0, 0, 0, 0)
    OP_6F(0x0011, 0)
    OP_1E()
    FadeIn(1000, 0)
    OP_56(0x00)
    TalkEnd(0x00FF)

    Return()

    def _loc_1BA6(): pass

    label('loc_1BA6')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1BC0',
    )

    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Return()

    def _loc_1BC0(): pass

    label('loc_1BC0')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
