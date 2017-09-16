from ED6ScenarioHelper import *

def main():
    # 蔡斯

    CreateScenaFile(
        FileName            = 'C3106   ._SN',
        MapName             = 'Zeiss',
        Location            = 'C3106.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60034",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        '希德少校',                             # 9
        '士兵',                                 # 10
        '士兵',                                 # 11
        '王国军军官',                           # 12
        '士兵',                                 # 13
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 6000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 0,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH02450 ._CH',             # 00
        'ED6_DT07/CH01640 ._CH',             # 01
        'ED6_DT07/CH01310 ._CH',             # 02
    )

    AddCharChipPat(
        'ED6_DT07/CH02450P._CP',             # 00
        'ED6_DT07/CH01640P._CP',             # 01
        'ED6_DT07/CH01310P._CP',             # 02
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 16500,
        TriggerZ            = 0,
        TriggerY            = 42000,
        TriggerRange        = 800,
        ActorX              = 16500,
        ActorZ              = 1000,
        ActorY              = 42000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -12960,
        TriggerZ            = 0,
        TriggerY            = 34480,
        TriggerRange        = 1000,
        ActorX              = -12960,
        ActorZ              = 1000,
        ActorY              = 34480,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1AA",          # 00, 0
        "Function_1_1C6",          # 01, 1
        "Function_2_226",          # 02, 2
        "Function_3_1821",         # 03, 3
        "Function_4_192B",         # 04, 4
    )


    def Function_0_1AA(): pass

    label("Function_0_1AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_1C5")
    SetMapFlags(0x40000000)
    AddParty(0xFF, 0xFF)
    SetMapFlags(0x10000000)
    OP_A3(0x3FA)
    Event(0, 2)

    label("loc_1C5")

    Return()

    # Function_0_1AA end

    def Function_1_1C6(): pass

    label("Function_1_1C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 1)), scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1DC")
    OP_65(0x0, 0x1)

    label("loc_1DC")

    LoadEffect(0x0, "map\\\\mp027_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, -12960, 1000, 34480, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_1_1C6 end

    def Function_2_226(): pass

    label("Function_2_226")

    ClearMapFlags(0x10000000)
    SetChrPos(0x0, -10080, 0, 27870, 0)
    SetChrPos(0x1, -10080, 0, 27870, 0)
    SetChrPos(0x2, -10080, 0, 27870, 0)
    SetChrPos(0x3, -10080, 0, 27870, 0)
    EventBegin(0x0)
    OP_6D(-1220, 0, 23900, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(4460, 0)
    OP_6C(67000, 0)
    OP_6E(423, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0xA, 0x40)
    SetChrFlags(0xB, 0x40)
    SetChrPos(0x8, -11370, 0, 21640, 270)
    SetChrPos(0x9, -13090, 0, 22310, 90)
    SetChrPos(0xA, -13360, 0, 21070, 90)

    def lambda_305():
        OP_6C(45000, 8000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_305)
    FadeToBright(2000, 0)
    OP_0D()

    def lambda_31F():
        OP_6E(262, 6000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_31F)

    def lambda_32F():
        OP_6B(3250, 6000)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_32F)
    OP_6D(-12330, 0, 21630, 6000)

    ChrTalk(
        0x8,
        (
            "#701F辛苦你们了。\x02\x03",
            "搬集装箱的事明天再来做吧。\x01",
            "今天你们就先回兵营休息一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "那、那个，少校……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "这几天的非常体制，\x01",
            "还要持续到什么时候啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#700F……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "是、是啊！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "为什么我们正规军\x01",
            "非要听那帮家伙的指挥不可……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#703F你们说的意思我也很清楚……\x01",
            "　\x02\x03",
            "但军人不该对上级的决定抱有质疑。\x01",
            "　\x02\x03",
            "#701F而且……\x01",
            "正所谓隔墙有耳。\x02\x03",
            "你们要注意谨慎发言。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "明、明白了。\x02",
    )

    CloseMessageWindow()
    OP_8C(0xA, 270, 400)

    def lambda_5BD():
        OP_8E(0xFE, 0xFFFFA970, 0x0, 0x5816, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_5BD)
    Sleep(100)
    OP_8C(0x9, 270, 400)
    OP_8E(0x9, 0xFFFFA970, 0x0, 0x5816, 0xBB8, 0x0)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)

    ChrTalk(
        0x8,
        (
            "#703F呼……\x01",
            "真是问心有愧啊……\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0xB, -22160, 0, 22550, 0)
    ClearChrFlags(0xB, 0x80)

    def lambda_63A():

        label("loc_63A")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_63A")

    QueueWorkItem2(0x8, 1, lambda_63A)
    OP_8E(0xB, 0xFFFFCC34, 0x0, 0x591A, 0xFA0, 0x0)
    TurnDirection(0xB, 0x8, 400)

    ChrTalk(
        0xB,
        "报告少校！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "凯诺娜上尉\x01",
            "有急事找您，\x01",
            "麻烦您马上过去一趟。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#700F是吗……知道了。\x02\x03",
            "#703F没办法……\x01",
            "又要去听那只母狐狸训话了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_730():

        label("loc_730")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_730")

    QueueWorkItem2(0xB, 1, lambda_730)

    def lambda_741():
        OP_8E(0xFE, 0xFFFFA970, 0x0, 0x5816, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_741)
    Sleep(1000)
    OP_8E(0xB, 0xFFFFA970, 0x0, 0x5816, 0xBB8, 0x0)
    OP_6D(-9480, 0, 27600, 5000)
    OP_22(0xA9, 0x0, 0x64)
    OP_B0(0x12, 0x78)
    OP_70(0x12, 0xB4)
    OP_73(0x12)
    Sleep(500)

    def lambda_79E():
        OP_6D(-7220, 0, 27280, 7000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_79E)

    def lambda_7B6():
        OP_6C(21000, 7000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_7B6)

    def lambda_7C6():
        OP_6B(2800, 7000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7C6)
    SetChrFlags(0x106, 0x4)
    SetChrFlags(0x107, 0x4)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    OP_8E(0x106, 0xFFFFE3FE, 0x0, 0x6E3C, 0xBB8, 0x0)
    OP_8C(0x106, 156, 400)
    OP_8E(0x107, 0xFFFFE7B4, 0x0, 0x6AAE, 0xBB8, 0x0)
    OP_8C(0x107, 304, 400)
    OP_8E(0x101, 0xFFFFE494, 0x0, 0x67D4, 0xBB8, 0x0)
    OP_8C(0x101, 342, 400)
    OP_8E(0x102, 0xFFFFE0DE, 0x0, 0x69BE, 0xBB8, 0x0)
    OP_8C(0x102, 71, 400)
    ClearChrFlags(0x106, 0x4)
    ClearChrFlags(0x107, 0x4)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    WaitChrThread(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#007F呼～\x01",
            "刚才真是太挤了～\x02\x03",
            "#008F提妲，不要紧吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#066F嗯，还好呢。\x01",
            "只是头有点晕乎乎的……\x02\x03",
            "不过装置能够运作正常，\x01",
            "辛苦一点也是值得的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#053F嗯，了不起啊。\x02\x03",
            "#051F虽然我之前反对你跟着来……\x01",
            "不过看来有你在一起是正确的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#067F嘿嘿……\x01",
            "谢谢，阿加特大哥哥。\x02\x03",
            "不过真是被安东尼吓了一跳呢。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F嗯嗯，\x01",
            "正好就是旁边的集装箱。\x02\x03",
            "我还以为死定了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我想那只猫是维修长特意放进去的。\x01",
            "　\x02\x03",
            "多亏有了它的帮忙，\x01",
            "刚才士兵的警戒也放松了很多。\x02\x03",
            "而且维修长本人的应对也很冷静。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#560F呵呵……\x01",
            "维修长叔叔也许为了我们才这么做。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#051F看来大叔很有一套嘛。\x02\x03",
            "那么我们就开始行动吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_AD(0x40025, 0x0, 0x0, 0x1F4)
    Sleep(1500)
    OP_77(0x0, 0x0, 0x0, 0x0, 0x0)
    SetMessageWindowPos(75, 300, -1, -1)
    SetChrName("阿加特")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#050F我们现在身处的飞艇停机坪\x01",
            "——就在这附近。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0x3E8)
    Sleep(500)
    OP_AD(0x4002C, 0x0, 0x0, 0x1F4)
    Sleep(1500)
    SetMessageWindowPos(75, 300, -1, -1)
    SetChrName("阿加特")

    AnonymousTalk(
        (
            "#050F胡乱搜索是肯定无法\x01",
            "找到老爷子被关押的位置的。\x02\x03",
            "艾丝蒂尔，\x01",
            "你在地图上找找看。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(400, 400, -1, -1)
    SetChrName("艾丝蒂尔")

    AnonymousTalk(
        (
            "#004F咦？\x01",
            "为、为什么要我找？\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(75, 300, -1, -1)
    SetChrName("阿加特")

    AnonymousTalk(
        (
            "#051F作为你的游击士前辈，\x01",
            "想趁此测试一下你的洞察力而已。\x02\x03",
            "喂，没时间了。\x01",
            "快点给我找找看吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        12,
        12,
        0,
        (
            "【西南的兵营】\x01",        # 0
            "【中央的司令部】\x01",      # 1
            "【中央的研究所】\x01",      # 2
            "【东北的监视塔】\x01",      # 3
            "【南边的正门】\x01",        # 4
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_DE7"),
        (1, "loc_F95"),
        (2, "loc_10DD"),
        (3, "loc_1246"),
        (4, "loc_142B"),
        (SWITCH_DEFAULT, "loc_15AA"),
    )


    label("loc_DE7")

    SetMessageWindowPos(75, 300, -1, -1)
    SetChrName("阿加特")

    AnonymousTalk(
        (
            "#053F虽然可能性并非为零，\x01",
            "但这处的普通士兵肯定会很多。\x02\x03",
            "考虑到保守军事机密，\x01",
            "博士在别处的可能性比较高。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(400, 400, -1, -1)
    SetChrName("艾丝蒂尔")

    AnonymousTalk(
        "#007F嗯，的确……\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(75, 300, -1, -1)
    SetChrName("阿加特")

    AnonymousTalk(
        (
            "#050F约修亚，\x01",
            "你的意见又如何？\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(150, 350, -1, -1)
    SetChrName("约修亚")

    AnonymousTalk(
        (
            "#012F中央的研究所……\x01",
            "我觉得博士最有可能在那里。\x02\x03",
            "研究所有一个单独的区划，\x01",
            "把博士关在那里也能掩人耳目地做研究。\x01",
            "所以我认为博士在研究所的可能性最高。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_15AA")

    label("loc_F95")

    SetMessageWindowPos(75, 300, -1, -1)
    SetChrName("阿加特")

    AnonymousTalk(
        (
            "#053F这里的可能性虽然很高，\x01",
            "但其实还有更可疑的地方。\x02\x03",
            "#050F约修亚，\x01",
            "你的意见又如何？\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(150, 350, -1, -1)
    SetChrName("约修亚")

    AnonymousTalk(
        (
            "#012F中央的研究所……\x01",
            "我觉得博士最有可能在那里。\x02\x03",
            "研究所有一个单独的区划，\x01",
            "把博士关在那里也能掩人耳目地做研究。\x01",
            "所以我认为博士在研究所的可能性最高。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_15AA")

    label("loc_10DD")

    SetMessageWindowPos(75, 300, -1, -1)
    SetChrName("阿加特")

    AnonymousTalk(
        "#052F哦……不错嘛。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(400, 400, -1, -1)
    SetChrName("艾丝蒂尔")

    AnonymousTalk(
        "#502F哼哼，这太简单不过了⊙\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(75, 300, -1, -1)
    SetChrName("阿加特")

    AnonymousTalk(
        (
            "#551F这家伙又在得意忘形了。\x02\x03",
            "#050F约修亚，\x01",
            "你的意见怎么样？\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(150, 350, -1, -1)
    SetChrName("约修亚")

    AnonymousTalk(
        (
            "#012F我也觉得那里可能性最高。\x02\x03",
            "研究所有一个单独的区划，\x01",
            "把博士关在那里也能掩人耳目地做研究。\x01",
            "所以我认为博士在研究所的可能性最高。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_15AA")

    label("loc_1246")

    SetMessageWindowPos(75, 300, -1, -1)
    SetChrName("阿加特")

    AnonymousTalk(
        (
            "#552F原来如此……\x01",
            "这地方出入的人应该很少。\x01",
            "这里的可能性虽然很高，\x02\x03",
            "#051F但其实还有更可疑的地方。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(400, 400, -1, -1)
    SetChrName("艾丝蒂尔")

    AnonymousTalk(
        "#505F是这样吗？\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(75, 300, -1, -1)
    SetChrName("阿加特")

    AnonymousTalk(
        (
            "#050F约修亚，\x01",
            "你的意见又如何？\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(150, 350, -1, -1)
    SetChrName("约修亚")

    AnonymousTalk(
        (
            "#012F中央的研究所……\x01",
            "我觉得博士最有可能在那里。\x02\x03",
            "研究所有一个单独的区划，\x01",
            "把博士关在那里也能掩人耳目地做研究。\x01",
            "所以我认为博士在研究所的可能性最高。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_15AA")

    label("loc_142B")

    SetMessageWindowPos(75, 300, -1, -1)
    SetChrName("阿加特")

    AnonymousTalk(
        (
            "#551F那里是要塞的出口。\x01",
            "用常识想想也知道不会在那种地方啦。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(400, 400, -1, -1)
    SetChrName("艾丝蒂尔")

    AnonymousTalk(
        "#007F啊……是哦。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(75, 300, -1, -1)
    SetChrName("阿加特")

    AnonymousTalk(
        (
            "#050F约修亚，\x01",
            "你的意见又如何？\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(150, 350, -1, -1)
    SetChrName("约修亚")

    AnonymousTalk(
        (
            "#012F中央的研究所……\x01",
            "我觉得博士最有可能在那里。\x02\x03",
            "研究所有一个单独的区划，\x01",
            "把博士关在那里也能掩人耳目地做研究。\x01",
            "所以我认为博士在研究所的可能性最高。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_15AA")

    label("loc_15AA")

    SetMessageWindowPos(75, 300, -1, -1)
    SetChrName("阿加特")

    AnonymousTalk(
        "#053F嗯，就这样了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0x3E8)
    Sleep(500)
    OP_AD(0x4002D, 0x0, 0x0, 0x1F4)
    Sleep(1500)
    SetMessageWindowPos(75, 300, -1, -1)
    SetChrName("阿加特")

    AnonymousTalk(
        (
            "#050F时间紧迫。\x01",
            "就先从那里开始调查吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(150, 350, -1, -1)
    SetChrName("约修亚")

    AnonymousTalk(
        (
            "#010F阿加特兄，\x01",
            "逃跑的路线要怎么决定？\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(75, 300, -1, -1)
    SetChrName("阿加特")

    AnonymousTalk(
        (
            "#052F啊，对了。\x02\x03",
            "在这个停机坪的对面\x01",
            "有个延伸到瓦雷利亚湖的码头。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0x3E8)
    Sleep(500)
    OP_AD(0x4002E, 0x0, 0x0, 0x1F4)
    Sleep(1500)
    OP_3F(0x359, 1)
    OP_3E(0x35A, 1)
    SetMessageWindowPos(75, 300, -1, -1)
    SetChrName("阿加特")

    AnonymousTalk(
        (
            "#050F救出老爷子后就在那里抢船逃走。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(400, 400, -1, -1)
    SetChrName("艾丝蒂尔")

    AnonymousTalk(
        "#002F嗯……明白了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_77(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_AE(0x1F4)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#006F那么，\x01",
            "赶快向西北的研究所进发吧。\x02\x03",
            "提妲，\x01",
            "不要离开我们身边哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#062F嗯、嗯……！\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    EventEnd(0x0)
    Return()

    # Function_2_226 end

    def Function_3_1821(): pass

    label("Function_3_1821")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18C1")
    OP_A2(0x0)

    ChrTalk(
        0x106,
        (
            "#050F这边的楼梯是往码头去的。\x01",
            "　\x02\x03",
            "回来的时候就从这里逃走吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F好，知道了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F明白。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1927")

    label("loc_18C1")


    ChrTalk(
        0x106,
        (
            "#050F这边的楼梯是往码头去的。\x01",
            "　\x02\x03",
            "回来的时候就从这里逃走吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1927")

    TalkEnd(0xFF)
    Return()

    # Function_3_1821 end

    def Function_4_192B(): pass

    label("Function_4_192B")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这是一台可供旅行者回复体力的导力器装置。\x07\x00\x02",
        )
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "在此休息\x01",      # 0
            "离开\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B3C")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_82(0x0, 0x2)
    PlayEffect(0x0, 0x2, 0xFF, -12960, 1000, 34480, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    OP_6F(0x11, 0)
    OP_70(0x11, 0x32)
    OP_73(0x11)
    OP_20(0xBB8)
    OP_22(0xC, 0x0, 0x64)
    OP_82(0x2, 0x2)
    LoadEffect(0x1, "map\\\\mp027_01.eff")
    PlayEffect(0x1, 0x1, 0xFF, -12960, 1000, 34480, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    OP_22(0xD, 0x0, 0x64)
    OP_0D()
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    SetChrPos(0x0, -14350, 0, 33010, 39)
    SetChrPos(0x1, -14350, 0, 33010, 39)
    SetChrPos(0x2, -14350, 0, 33010, 39)
    SetChrPos(0x3, -14350, 0, 33010, 39)
    OP_69(0x0, 0x0)
    OP_30(0x0)
    Sleep(3500)
    OP_82(0x1, 0x2)
    LoadEffect(0x0, "map\\\\mp027_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, -12960, 1000, 34480, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    OP_6F(0x11, 0)
    OP_1E()
    FadeToBright(1000, 0)
    OP_56(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_1B3C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B56")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_1B56")

    Return()

    # Function_4_192B end

    SaveToFile()

Try(main)
