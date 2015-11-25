from ED6ScenarioHelper import *

def main():
    # 蔡斯

    CreateScenaFile(
        FileName            = 'C3115   ._SN',
        MapName             = 'Zeiss',
        Location            = 'C3115.x',
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
        '凯诺娜上尉',                           # 9
        '洛伦斯少尉',                           # 10
        '理查德上校',                           # 11
        '希德少校',                             # 12
        '拉赛尔博士',                           # 13
        '黑色导力器',                           # 14
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
        'ED6_DT07/CH02100 ._CH',             # 01
        'ED6_DT07/CH02200 ._CH',             # 02
        'ED6_DT07/CH02030 ._CH',             # 03
        'ED6_DT07/CH02020 ._CH',             # 04
        'ED6_DT06/CH20021 ._CH',             # 05
        'ED6_DT06/CH20141 ._CH',             # 06
    )

    AddCharChipPat(
        'ED6_DT07/CH02450P._CP',             # 00
        'ED6_DT07/CH02100P._CP',             # 01
        'ED6_DT07/CH02200P._CP',             # 02
        'ED6_DT07/CH02030P._CP',             # 03
        'ED6_DT07/CH02020P._CP',             # 04
        'ED6_DT06/CH20021P._CP',             # 05
        'ED6_DT06/CH20141P._CP',             # 06
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
        Unknown3            = 3,
        ChipIndex           = 0x3,
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
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 917509,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_1A2",          # 00, 0
        "Function_1_1D0",          # 01, 1
        "Function_2_1E9",          # 02, 2
        "Function_3_13C6",         # 03, 3
    )


    def Function_0_1A2(): pass

    label("Function_0_1A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_1B0")
    OP_A3(0x3FA)
    Event(0, 2)

    label("loc_1B0")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_1BC"),
        (SWITCH_DEFAULT, "loc_1CF"),
    )


    label("loc_1BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAD, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAD, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1CC")
    Event(0, 3)

    label("loc_1CC")

    Jump("loc_1CF")

    label("loc_1CF")

    Return()

    # Function_0_1A2 end

    def Function_1_1D0(): pass

    label("Function_1_1D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAD, 3)), scpexpr(EXPR_END)), "loc_1DC")
    OP_22(0xAC, 0x1, 0x46)

    label("loc_1DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAD, 1)), scpexpr(EXPR_END)), "loc_1E8")
    OP_71(0x0, 0x4)

    label("loc_1E8")

    Return()

    # Function_1_1D0 end

    def Function_2_1E9(): pass

    label("Function_2_1E9")

    EventBegin(0x0)
    OP_6D(-6060, 0, 3830, 0)
    OP_67(0, 5730, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x106, 0x80)
    SetChrFlags(0x107, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xC, 3670, 0, 4750, 180)
    SetChrPos(0xA, 3550, 0, 2260, 0)
    SetChrPos(0x8, 2710, 0, 1010, 0)
    SetChrPos(0xB, 4000, 0, 770, 0)
    SetChrPos(0xD, 3520, 800, 2960, 0)
    ClearChrFlags(0xD, 0x80)
    OP_6D(4650, 0, 3040, 4000)

    ChrTalk(
        0xA,
        (
            "#111F拉赛尔博士，\x01",
            "这次真是太感谢您了。\x02\x03",
            "竟然真的有掌握\x01",
            "这个导力器『福音』的控制方法。\x02\x03",
            "我代表情报部由衷地感谢您。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#102F哼……\x01",
            "果然你就是幕后黑手……\x02\x03",
            "情报部理查德上校……\x02\x03",
            "记得你本来是卡西乌斯的部下吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#113F哦哦，说起来……\x01",
            "博士和他是几十年的老交情吧。\x02\x03",
            "#110F其实我们王国军也\x01",
            "一直在寻找卡西乌斯·布莱特的行踪，\x01",
            "但可惜的是至今仍未有任何线索。\x02\x03",
            "如果有什么线索的话，\x01",
            "还望您能顺便告诉我……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#104F不知道。\x01",
            "知道了也不会告诉你。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#115F呵呵……那就算了。\x02\x03",
            "如果这个『福音』回到他的手上，\x01",
            "必定会对我们的工作构成很大的阻挠……\x01",
            "　\x02\x03",
            "不过……即使他现在出面，\x01",
            "也无法阻整个事态的发展了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#102F『黑色导力器』……\x01",
            "不，应该是说『福音』才对……\x02\x03",
            "你们到底打算用它做什么？\x01",
            "　\x02\x03",
            "不，在此之前……\x01",
            "我有一个问题是非问不可的。\x01",
            "这个导力器你们到底是从哪里得到的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#111F当然是从某种渠道得来的。\x02\x03",
            "而我们的目的嘛……\x01",
            "呵呵，很快您就能知道了。\x02\x03",
            "等博士您明白一切之时，\x01",
            "也会是我们让您回去的适当时机，\x01",
            "在那之前，就委屈您在要塞小住一阵了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#102F我可是知道你们干的坏事哦，\x01",
            "这么简单就放我回去……\x02\x03",
            "还真是令人难以置信啊。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#111F哈哈，随您怎么想了。\x02\x03",
            "不过事成之后，\x01",
            "我会以个人名义援助博士的研究。\x01",
            "　\x02\x03",
            "希望博士能发明更多的东西，\x01",
            "来为我们的利贝尔王国添彩……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#104F哼，我拒绝。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#188F博士，\x01",
            "请别把话说得那么绝情哦。\x01",
            "　\x02\x03",
            "博士的孙女要是有个万一，\x01",
            "这点我们可是保证不了哦。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#105F小、小丫头……\x01",
            "又用这个来威胁我……！？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x8, 400)

    ChrTalk(
        0xA,
        (
            "#115F哎呀哎呀，凯诺娜上尉。\x02\x03",
            "怎么可以用这种口吻和博士谈话？\x01",
            "不觉得你的交涉方法有欠优雅吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xA, 400)

    ChrTalk(
        0x8,
        "#182F呵呵……失礼了。\x02",
    )

    CloseMessageWindow()

    def lambda_B61():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_B61)
    TurnDirection(0xA, 0xC, 400)

    ChrTalk(
        0xA,
        (
            "#110F上尉她总是有种特殊的幽默感。\x01",
            "　\x02\x03",
            "希望您不要误会，\x01",
            "我们毕竟只是一群忧国忧民的军人罢了。\x01",
            "　\x02\x03",
            "我可以在此对您发誓，\x01",
            "把平民卷入计划绝非我的本意。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#102F忧国忧民……\x02\x03",
            "更加离谱的是……\x01",
            "那个能停止导力现象的黑色导力器……\x02\x03",
            "原来如此……\x01",
            "你们的目的我总算能看出点眉目了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#112F哦……\x02",
    )

    CloseMessageWindow()
    OP_22(0x6A, 0x0, 0x64)
    Sleep(500)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -850, 0, -4650, 0)

    ChrTalk(
        0x9,
        "#1P……打扰了。\x02",
    )

    CloseMessageWindow()

    def lambda_D59():

        label("loc_D59")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_D59")

    QueueWorkItem2(0xB, 1, lambda_D59)

    def lambda_D6A():

        label("loc_D6A")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_D6A")

    QueueWorkItem2(0xA, 1, lambda_D6A)

    def lambda_D7B():

        label("loc_D7B")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_D7B")

    QueueWorkItem2(0xC, 1, lambda_D7B)

    def lambda_D8C():

        label("loc_D8C")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_D8C")

    QueueWorkItem2(0x8, 1, lambda_D8C)

    def lambda_D9D():
        OP_6D(3120, 0, 2260, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D9D)
    OP_8E(0x9, 0x4E2, 0x0, 0x636, 0xBB8, 0x0)
    TurnDirection(0x9, 0xA, 400)

    ChrTalk(
        0x8,
        (
            "#180F哎呀，少尉。\x01",
            "上校正和博士谈话呢。\x02\x03",
            "可别打扰到他们哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#110F啊，没关系。\x02\x03",
            "洛伦斯，就在这里报告吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#281F王都的行动已经开始了。\x02\x03",
            "和上校预计的一样，\x01",
            "白翼似乎已经全部落网了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#188F这可真是……\x02",
    )

    CloseMessageWindow()
    OP_44(0xA, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)

    ChrTalk(
        0xA,
        (
            "#115F呵呵……\x01",
            "这样就向前迈进一大步了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_F26():
        OP_6D(4650, 0, 3040, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F26)
    TurnDirection(0xA, 0xC, 400)

    def lambda_F45():

        label("loc_F45")

        TurnDirection(0xFE, 0xA, 400)
        OP_48()
        Jump("loc_F45")

    QueueWorkItem2(0xB, 1, lambda_F45)

    def lambda_F56():

        label("loc_F56")

        TurnDirection(0xFE, 0xA, 400)
        OP_48()
        Jump("loc_F56")

    QueueWorkItem2(0xC, 1, lambda_F56)

    def lambda_F67():

        label("loc_F67")

        TurnDirection(0xFE, 0xA, 400)
        OP_48()
        Jump("loc_F67")

    QueueWorkItem2(0x8, 1, lambda_F67)
    WaitChrThread(0x101, 0x1)

    ChrTalk(
        0xA,
        (
            "#111F博士，\x01",
            "那么我们就此告辞了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    Fade(500)
    SetChrFlags(0xD, 0x80)
    OP_0D()
    Sleep(500)
    TurnDirection(0xA, 0xB, 400)

    ChrTalk(
        0xA,
        (
            "#110F希德少校，\x01",
            "为了不要让博士感到不自在，\x01",
            "请你在他身边的时候多注意一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#703F是……明白。\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0xA, 0x40)
    SetChrFlags(0x8, 0x40)
    SetChrFlags(0x9, 0x40)
    OP_8C(0xA, 225, 400)
    OP_8E(0xA, 0x992, 0x0, 0x776, 0x7D0, 0x0)
    SetChrFlags(0xA, 0x4)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x9, 0x4)

    def lambda_1069():
        OP_8E(0xFE, 0xFFFFF9D4, 0x0, 0xFFFFE52A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1069)
    Sleep(1000)

    def lambda_1089():
        OP_8E(0xFE, 0xFFFFF9D4, 0x0, 0xFFFFE52A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1089)
    Sleep(500)

    def lambda_10A9():
        OP_8E(0xFE, 0xFFFFF9D4, 0x0, 0xFFFFE52A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_10A9)
    WaitChrThread(0x9, 0x1)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    OP_22(0xE6, 0x0, 0x64)
    Sleep(500)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)
    TurnDirection(0xB, 0xC, 400)
    Sleep(500)

    def lambda_10F6():
        OP_6D(4430, 0, 4440, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_10F6)
    OP_8E(0xB, 0xDDE, 0x0, 0x8D4, 0x7D0, 0x0)
    TurnDirection(0xB, 0xC, 400)
    WaitChrThread(0x101, 0x1)

    ChrTalk(
        0xB,
        (
            "#701F拉赛尔博士，\x01",
            "请问您还有什么需要吗？\x02\x03",
            "一般的要求我们都能做到的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xB, 400)

    ChrTalk(
        0xC,
        (
            "#104F#5P哼，免了。\x02\x03",
            "#102F我一直认为你和他们不同，\x01",
            "是个有骨气有原则的军人……\x02\x03",
            "看来我真是看错你了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#703F……惭愧。\x02\x03",
            "#700F不管博士怎么想都好，\x01",
            "现在您已经是反叛者的阶下囚了。\x02\x03",
            "在此您有什么消息或口信\x01",
            "要让我向您的孙女代为传达的吗？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xC,
        "#105F#3S#5P快从我眼前消失！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#703F……失陪了。\x02",
    )

    CloseMessageWindow()
    OP_8C(0xB, 225, 400)
    OP_8E(0xB, 0xFFFFFAF6, 0x0, 0xFFFFEBF6, 0xFA0, 0x0)
    OP_22(0x6A, 0x0, 0x64)
    Sleep(500)
    OP_22(0xE6, 0x0, 0x64)
    Sleep(500)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/C3107   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_1E9 end

    def Function_3_13C6(): pass

    label("Function_3_13C6")

    AddParty(0xA, 0xFF)
    EventBegin(0x0)
    OP_6D(-250, 0, 1940, 0)
    OP_67(0, 6560, -10000, 0)
    OP_6B(3000, 0)
    SetChrPos(0x10B, -310, 0, 3630, 0)
    SetChrPos(0x101, -1040, 0, -6570, 0)
    SetChrPos(0x106, -1040, 0, -6570, 0)
    SetChrPos(0x102, -1040, 0, -6570, 0)
    SetChrPos(0x107, -1040, 0, -6570, 0)
    FadeToBright(1000, 0)

    def lambda_145A():
        OP_8E(0xFE, 0xFFFFFCFE, 0x0, 0x14, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_145A)
    Sleep(400)

    def lambda_147A():
        OP_8E(0xFE, 0xA0, 0x0, 0xFFFFFE0C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_147A)
    Sleep(400)

    def lambda_149A():
        OP_8E(0xFE, 0xFFFFF6E6, 0x0, 0xFFFFFD30, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_149A)
    Sleep(400)

    def lambda_14BA():
        OP_8E(0xFE, 0xFFFFF97A, 0x0, 0xFFFFFA6A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_14BA)

    ChrTalk(
        0x10B,
        "#104F怎么又来了……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10B, 0x107, 400)

    ChrTalk(
        0x10B,
        (
            "#105F#3S不要烦我了！\x01",
            "都说了什么也不需要……\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0x10B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x107,
        "#560F爷、爷爷……\x02",
    )

    CloseMessageWindow()
    OP_8E(0x10B, 0xFFFFFEF2, 0x0, 0x8D4, 0x5DC, 0x0)

    ChrTalk(
        0x10B,
        (
            "#103F提、提妲！？\x02\x03",
            "难道……\x01",
            "我这是在做梦吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#068F爷爷啊！\x02",
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    def lambda_15DA():
        OP_6D(-250, 0, 2840, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_15DA)
    OP_92(0x107, 0x10B, 0x190, 0x1388, 0x0)

    def lambda_1600():
        OP_8F(0x107, 0xFFFFFF88, 0x0, 0x820, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_1600)
    SetChrChipByIndex(0x107, 6)
    SetChrSubChip(0x107, 0)
    SetChrFlags(0x107, 0x20)
    OP_94(0x1, 0x10B, 0xB4, 0x12C, 0x7D0, 0x0)

    ChrTalk(
        0x107,
        (
            "#069F#2P太、太好了！\x01",
            "爷爷您平安无事……\x02\x03",
            "呜呜呜……\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0x107, 0xF, 0x0, 0x12C, 0xFA0)
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(
        0x107,
        "#068F#3S#2P呜哇哇哇哇啊啊啊！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(
        0x10B,
        (
            "#100F看、看来……\x01",
            "我这老骨头不是做梦啊。\x02\x03",
            "还有，你们也来了啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F呀嗬，博士。\x01",
            "看来你还挺精神的嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我们是受工房长先生的委托，\x01",
            "前来这里营救博士您的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10B,
        (
            "#103F怎么……\x01",
            "你们竟然能想到办法潜入这里。\x02\x03",
            "#101F真不愧是卡西乌斯的孩子……\x01",
            "无论是胆量还是意志都很优秀啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#050F哟，老爷子。\x02\x03",
            "很抱歉打断你们叙旧，\x01",
            "还是赶快做一下逃离的准备吧。\x02\x03",
            "我们也没什么时间了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10B,
        (
            "#102F说起来，你又是谁啊？\x02\x03",
            "外表这么古怪的年轻人，\x01",
            "头发像个公鸡一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#055F公、公鸡……\x02",
    )

    CloseMessageWindow()
    OP_9E(0x106, 0xF, 0x0, 0x12C, 0xFA0)

    ChrTalk(
        0x106,
        "#054F#3S说什么呀，你这老头！？\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F啊哈哈。\x01",
            "博士说得太形象了呀～！\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x107, 0x20)
    SetChrChipByIndex(0x107, 65535)
    OP_8F(0x107, 0xFFFFFEDE, 0x0, 0x528, 0x7D0, 0x0)
    TurnDirection(0x107, 0x10B, 0)

    ChrTalk(
        0x107,
        (
            "#562F爷、爷爷啊……\x01",
            "别说这种失礼的话啦。\x02\x03",
            "#560F这个大哥哥叫阿加特，\x01",
            "他也是游击士协会的游击士，\x01",
            "而且还是姐姐他们的前辈哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10B,
        (
            "#103F哦……\x01",
            "你也是游击士啊。\x02\x03",
            "#101F对了对了……\x01",
            "我好像从卡西乌斯那里听说过你。\x02\x03",
            "一个又倔又别扭的不良青年。\x01",
            " \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#057F那、那个胡子大叔……！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x106, 400)

    ChrTalk(
        0x102,
        "#019F好啦好啦，阿加特兄。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x10B, 400)

    ChrTalk(
        0x102,
        (
            "#010F博士也是，详细情况等以后再说吧。\x01",
            "当务之急还是快点逃离这里。\x02\x03",
            "有什么东西要带走的吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1C46():

        label("loc_1C46")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_1C46")

    QueueWorkItem2(0x101, 2, lambda_1C46)

    def lambda_1C57():

        label("loc_1C57")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_1C57")

    QueueWorkItem2(0x107, 2, lambda_1C57)

    def lambda_1C68():

        label("loc_1C68")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_1C68")

    QueueWorkItem2(0x106, 2, lambda_1C68)

    def lambda_1C79():

        label("loc_1C79")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_1C79")

    QueueWorkItem2(0x10B, 2, lambda_1C79)

    ChrTalk(
        0x10B,
        (
            "#100F是啊……\x02\x03",
            "那么能不能把这个\x01",
            "『卡佩尔』的中枢设备送回去？\x02\x03",
            "随便放在这里的话，\x01",
            "准会被那帮家伙拿去做坏事了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F明白了。\x02",
    )

    CloseMessageWindow()
    OP_8E(0x102, 0xFFFFFAB0, 0x0, 0x29E, 0xBB8, 0x0)
    OP_8E(0x102, 0xFFFFFE7A, 0x0, 0x15A4, 0xBB8, 0x0)
    Sleep(500)
    OP_71(0x0, 0x4)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "演算导力器\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3E(0x364, 1)
    OP_8C(0x102, 180, 400)

    def lambda_1DAB():
        OP_6D(-900, 0, 1970, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1DAB)
    OP_8E(0x102, 0xFFFFF8D0, 0x0, 0x7ED, 0xBB8, 0x0)
    TurnDirection(0x102, 0x10B, 400)
    OP_44(0x101, 0xFF)
    OP_44(0x107, 0xFF)
    OP_44(0x106, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x10B, 0xFF)

    def lambda_1DF2():
        TurnDirection(0xFE, 0x10B, 400)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_1DF2)

    def lambda_1E00():
        TurnDirection(0xFE, 0x10B, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1E00)

    def lambda_1E0E():
        TurnDirection(0xFE, 0x10B, 400)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_1E0E)

    ChrTalk(
        0x10B,
        (
            "#102F他们强迫我用它来研究\x01",
            "『黑色导力器』的控制方法。\x01",
            "　\x02\x03",
            "虽然不能解析那东西的构造，\x01",
            "但已经知道数据和控制方法了。\x02\x03",
            "那帮家伙随时都能引起那个现象。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#003F是吗……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10B, 0x101, 400)

    ChrTalk(
        0x10B,
        (
            "#104F抱歉，艾丝蒂尔、约修亚。\x02\x03",
            "你们特地交给我的东西就这样……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F请博士您不用太介意。\x02\x03",
            "他们拿提妲的安全做威胁，\x01",
            "您被迫就范也是没办法的事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F而且说起来，\x01",
            "是我们把博士卷进这件事的呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#054F好了～！\x01",
            "没时间罗嗦啦！\x02\x03",
            "快点准备逃跑吧！\x02\x03",
            "老爷子，赶快！\x01",
            "跑的时候小心别闪到腰！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10B, 0x106, 400)

    ChrTalk(
        0x10B,
        (
            "#102F哼，说什么呀……\x02\x03",
            "我还不至于输给你们年轻人！\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x106, 400)

    ChrTalk(
        0x107,
        "#067F真、真是的，你们两个……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x569)
    OP_28(0x44, 0x1, 0x40)
    EventEnd(0x0)
    Return()

    # Function_3_13C6 end

    SaveToFile()

Try(main)
