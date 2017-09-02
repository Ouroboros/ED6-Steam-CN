from ED6ScenarioHelper import *

def main():
    # 帕赛尔农场

    CreateScenaFile(
        FileName            = 'T0410   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0410.x',
        MapIndex            = 13,
        MapDefaultBGM       = "ed60015",
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
        '弗兰兹',                               # 9
        '汉娜',                                 # 10
        '查儿',                                 # 11
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 8000,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2600,
        Unknown_2C              = 262,
        Unknown_30              = 315,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 13,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 8000,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2600,
        Unknown_2C              = 262,
        Unknown_30              = 315,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 13,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH01020 ._CH',             # 00
        'ED6_DT07/CH01030 ._CH',             # 01
        'ED6_DT07/CH01070 ._CH',             # 02
        'ED6_DT07/CH00003 ._CH',             # 03
        'ED6_DT07/CH00013 ._CH',             # 04
    )

    AddCharChipPat(
        'ED6_DT07/CH01020P._CP',             # 00
        'ED6_DT07/CH01030P._CP',             # 01
        'ED6_DT07/CH01070P._CP',             # 02
        'ED6_DT07/CH00003P._CP',             # 03
        'ED6_DT07/CH00013P._CP',             # 04
    )

    DeclNpc(
        X                   = 550,
        Z                   = 0,
        Y                   = 34500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 2580,
        Z                   = 0,
        Y                   = 36100,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 1730,
        Z                   = 0,
        Y                   = 23000,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )


    DeclActor(
        TriggerX            = 720,
        TriggerZ            = 0,
        TriggerY            = 33340,
        TriggerRange        = 800,
        ActorX              = 550,
        ActorZ              = 1500,
        ActorY              = 34500,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_19A",          # 00, 0
        "Function_1_2EF",          # 01, 1
        "Function_2_2F0",          # 02, 2
        "Function_3_306",          # 03, 3
        "Function_4_32A",          # 04, 4
        "Function_5_32F",          # 05, 5
        "Function_6_4BE",          # 06, 6
        "Function_7_6E6",          # 07, 7
        "Function_8_7B4",          # 08, 8
        "Function_9_11AC",         # 09, 9
        "Function_10_11C8",        # 0A, 10
        "Function_11_11DA",        # 0B, 11
        "Function_12_14CF",        # 0C, 12
    )


    def Function_0_19A(): pass

    label("Function_0_19A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B0")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    OP_64(0x0, 0x1)

    label("loc_1B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_1DC")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8)
    OP_64(0x0, 0x1)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8)
    Jump("loc_208")

    label("loc_1DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_1F4")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8)
    OP_64(0x0, 0x1)
    Jump("loc_208")

    label("loc_1F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_1FE")
    Jump("loc_208")

    label("loc_1FE")

    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8)

    label("loc_208")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (1, "loc_21C"),
        (100, "loc_2AF"),
        (102, "loc_2AF"),
        (SWITCH_DEFAULT, "loc_2EE"),
    )


    label("loc_21C")

    SetChrPos(0x101, 400, 0, 22000, 0)
    SetChrPos(0x102, 1600, 0, 22000, 0)
    SetChrPos(0x8, 300, 0, 24400, 180)
    SetChrPos(0x9, 1400, 0, 24900, 180)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8)
    ClearMapFlags(0x1)
    OP_4F(0x65, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x66, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x67, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 11)
    Jump("loc_2EE")

    label("loc_2AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2EB")
    SetChrPos(0x8, 450, 0, 32400, 0)
    SetChrPos(0x9, 480, 0, 34510, 180)
    Event(0, 8)
    SetMapFlags(0x400000)
    ClearMapFlags(0x1)

    label("loc_2EB")

    Jump("loc_2EE")

    label("loc_2EE")

    Return()

    # Function_0_19A end

    def Function_1_2EF(): pass

    label("Function_1_2EF")

    Return()

    # Function_1_2EF end

    def Function_2_2F0(): pass

    label("Function_2_2F0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_305")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_2F0")

    label("loc_305")

    Return()

    # Function_2_2F0 end

    def Function_3_306(): pass

    label("Function_3_306")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_329")
    OP_8D(0xFE, 560, 22800, 2860, 25700, 3000)
    Jump("Function_3_306")

    label("loc_329")

    Return()

    # Function_3_306 end

    def Function_4_32A(): pass

    label("Function_4_32A")

    Call(0, 5)
    Return()

    # Function_4_32A end

    def Function_5_32F(): pass

    label("Function_5_32F")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_436")
    OP_A2(0x2)

    ChrTalk(
        0x8,
        (
            "这次你们真是帮了大忙。\x01",
            "这下就能恢复蔬菜的输出了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "感谢你们的\x01",
            "还有那些等着\x01",
            "我们农场蔬菜的人们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "必须加把劲了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4BA")

    label("loc_436")


    ChrTalk(
        0x8,
        (
            "这次你们真是帮了大忙，\x01",
            "这下就能恢复蔬菜的输出了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "真的十分感谢你们。\x02",
    )

    CloseMessageWindow()

    label("loc_4BA")

    TalkEnd(0x8)
    Return()

    # Function_5_32F end

    def Function_6_4BE(): pass

    label("Function_6_4BE")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_612")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_588")
    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "哎呀，\x01",
            "这不是艾丝蒂尔和约修亚吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "之前多亏你们，\x01",
            "现在孩子们晚上\x01",
            "可以安心地睡觉了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "果然还是要好好睡觉\x01",
            "才能安心工作啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_60F")

    label("loc_588")


    ChrTalk(
        0xFE,
        (
            "之前多亏你们，\x01",
            "现在孩子们晚上\x01",
            "可以安心地睡觉了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "果然还是要好好睡觉\x01",
            "才能安心工作啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_60F")

    Jump("loc_6E2")

    label("loc_612")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_6E2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_694")
    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "艾丝蒂尔、约修亚，\x01",
            "你们已经成为很棒的游击士了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但希望你们\x01",
            "工作也不要太过蛮干哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6E2")

    label("loc_694")


    ChrTalk(
        0xFE,
        (
            "有空就再来玩，\x01",
            "我们会等你们的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6E2")

    TalkEnd(0x9)
    Return()

    # Function_6_4BE end

    def Function_7_6E6(): pass

    label("Function_7_6E6")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_72F")
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(
        0xFE,
        "啊，约修亚……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那、那个……\x01",
            "你是为了见我而来的吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7B0")

    label("loc_72F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_7B0")
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(
        0xFE,
        (
            "啊，约修亚，\x01",
            "好想……你再来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我和维鲁等着你。\x02",
    )

    CloseMessageWindow()

    label("loc_7B0")

    TalkEnd(0xA)
    Return()

    # Function_7_6E6 end

    def Function_8_7B4(): pass

    label("Function_8_7B4")

    EventBegin(0x0)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_67(0, 7600, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_43(0x1, 0x1, 0x0, 0x9)
    OP_43(0x0, 0x1, 0x0, 0xA)
    OP_8E(0x101, 0x12C, 0x0, 0x5F50, 0xBB8, 0x0)
    TurnDirection(0x101, 0x9, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#001F叔叔、阿姨，\x01",
            "你们早上好啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F早上好，很久没见面了。\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "哎呀……\x01",
            "原来是艾丝蒂尔和约修亚啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x0, 400)

    ChrTalk(
        0x8,
        (
            "真是好久不见了。\x01",
            "来找缇欧玩的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F啊，刚才已经见到她了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F其实今天是为了协会的工作而来的。\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_6D(-560, 200, 28600, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2550, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    SetChrPos(0x8, -800, 200, 29120, 180)
    SetChrPos(0x9, 1150, 200, 29120, 180)
    SetChrPos(0x101, -800, 250, 26900, 0)
    SetChrPos(0x102, 1150, 250, 26800, 0)
    SetChrChipByIndex(0x101, 3)
    SetChrChipByIndex(0x102, 4)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    OP_22(0x11, 0x0, 0x64)
    OP_3F(0x320, 1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "两人交出了介绍信，\x01",
            "并说明了代替卡西乌斯执行任务的原因。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(
        0x9,
        "#2P……原来是这样啊，我知道了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2P但是，只派你们两个来清除魔兽，\x01",
            "是不是太危险了点？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2P是啊。\x01",
            "万一被魔兽弄伤了怎么办……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F叔叔你们别担心，\x01",
            "我们毕竟已经是游击士了。\x02\x03",
            "#006F清除魔兽之类的不算什么啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F而且我们已经得到协会的许可。\x01",
            "这件事就交给我们好吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#2P嗯……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#2P好吧，那就拜托你们了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F谢谢叔叔⊙\x02\x03",
            "对了……那些魔兽是什么样子的呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2P不太清楚到底是什么……\x01",
            "样子看起来像大胖猫那样的魔兽。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2P通常是三、四只在半夜里结伴出现，\x01",
            "把田里的菜咬得遍地残渣。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2P虽说不是很凶暴，\x01",
            "不过动作却敏捷得不得了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2P当你想要抓它的时候，\x01",
            "它总会很快地转身溜走。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F嗯……好奇怪的魔兽啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F半夜才出现……\x01",
            "也就是说我们要等到那个时候了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2P啊，天黑之前\x01",
            "你们就好好休息一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2P你们两个今晚\x01",
            "就在这里吃顿便饭吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F嘿嘿，当然啦⊙\x02\x03",
            "#001F汉娜阿姨做的菜最美味了，\x01",
            "我好期待呢㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#2P你这孩子真会说话。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2P好了，为了不负你们的期待，\x01",
            "我也会做出最拿手的好菜哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    NewScene("ED6_DT01/T0401   ._SN", 1, 0, 0)
    IdleLoop()
    Return()

    # Function_8_7B4 end

    def Function_9_11AC(): pass

    label("Function_9_11AC")

    OP_8E(0x102, 0x578, 0x0, 0x6144, 0xBB8, 0x0)
    TurnDirection(0x102, 0x9, 0)
    Return()

    # Function_9_11AC end

    def Function_10_11C8(): pass

    label("Function_10_11C8")

    OP_6D(0, 0, 28000, 2000)
    Return()

    # Function_10_11C8 end

    def Function_11_11DA(): pass

    label("Function_11_11DA")

    EventBegin(0x0)
    SetMapFlags(0x400000)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)

    ChrTalk(
        0x8,
        (
            "谢谢啊。\x01",
            "这次你们真是帮了大忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "不过最后却害你们没能完成任务。\x01",
            "实在是有点过意不去……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F请不要介意。\x01",
            "我们从这次任务中学到了很多东西。\x02\x03",
            "#010F如果以后再有需要帮助的地方，\x01",
            "尽管联络游击士协会就行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "一定会的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "工作不忙的话要经常来这里住哦。\x01",
            "到时候煮些更好吃的菜给你们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F谢谢啦，缇欧，还有阿姨。 \x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F我们一定会再来拜访的。\x02",
    )

    CloseMessageWindow()
    OP_43(0x0, 0x1, 0x0, 0xC)
    Sleep(800)
    OP_43(0x1, 0x1, 0x0, 0xC)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    NewScene("ED6_DT01/T0400   ._SN", 1, 0, 0)
    IdleLoop()
    Return()

    # Function_11_11DA end

    def Function_12_14CF(): pass

    label("Function_12_14CF")

    OP_8E(0xFE, 0x3E8, 0x0, 0x5334, 0x5DC, 0x0)
    OP_8E(0xFE, 0x3E8, 0x0, 0x4CF4, 0x5DC, 0x0)
    SetChrFlags(0xFE, 0x8)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_12_14CF end

    SaveToFile()

Try(main)
