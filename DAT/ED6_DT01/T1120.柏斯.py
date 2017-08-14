from ED6ScenarioHelper import *

def main():
    # 柏斯

    CreateScenaFile(
        FileName            = 'T1120   ._SN',
        MapName             = 'Bose',
        Location            = 'T1120.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60011",
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
        '马尔科',                               # 9
        '尼冈德',                               # 10
        '卡莉娅',                               # 11
        '赛恩',                                 # 12
        '奈尔',                                 # 13
        '朵洛希',                               # 14
        '科梅尔斯',                             # 15
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
        'ED6_DT07/CH01100 ._CH',             # 00
        'ED6_DT07/CH01120 ._CH',             # 01
        'ED6_DT07/CH01550 ._CH',             # 02
        'ED6_DT07/CH01020 ._CH',             # 03
        'ED6_DT07/CH02060 ._CH',             # 04
        'ED6_DT06/CH20063 ._CH',             # 05
        'ED6_DT07/CH01040 ._CH',             # 06
    )

    AddCharChipPat(
        'ED6_DT07/CH01100P._CP',             # 00
        'ED6_DT07/CH01120P._CP',             # 01
        'ED6_DT07/CH01550P._CP',             # 02
        'ED6_DT07/CH01020P._CP',             # 03
        'ED6_DT07/CH02060P._CP',             # 04
        'ED6_DT06/CH20063P._CP',             # 05
        'ED6_DT07/CH01040P._CP',             # 06
    )

    DeclNpc(
        X                   = -25890,
        Z                   = 0,
        Y                   = 1370,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -24500,
        Z                   = 0,
        Y                   = 4690,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -28800,
        Z                   = 0,
        Y                   = 24200,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 500,
        Z                   = 0,
        Y                   = 7400,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -620,
        Z                   = -1000,
        Y                   = -3500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -620,
        Z                   = -1000,
        Y                   = -3500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -24500,
        Z                   = 0,
        Y                   = 4690,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )


    DeclActor(
        TriggerX            = -24000,
        TriggerZ            = 0,
        TriggerY            = 3580,
        TriggerRange        = 700,
        ActorX              = -24500,
        ActorZ              = 1500,
        ActorY              = 4690,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 920,
        TriggerZ            = 0,
        TriggerY            = 6280,
        TriggerRange        = 700,
        ActorX              = 500,
        ActorZ              = 1500,
        ActorY              = 7400,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_20A",          # 00, 0
        "Function_1_2B9",          # 01, 1
        "Function_2_2CC",          # 02, 2
        "Function_3_2E2",          # 03, 3
        "Function_4_3FB",          # 04, 4
        "Function_5_C80",          # 05, 5
        "Function_6_1341",         # 06, 6
        "Function_7_13BE",         # 07, 7
        "Function_8_1D72",         # 08, 8
        "Function_9_1FFF",         # 09, 9
        "Function_10_20AC",        # 0A, 10
        "Function_11_2133",        # 0B, 11
        "Function_12_2413",        # 0C, 12
        "Function_13_2459",        # 0D, 13
        "Function_14_24A4",        # 0E, 14
        "Function_15_24E5",        # 0F, 15
        "Function_16_2521",        # 10, 16
    )


    def Function_0_20A(): pass

    label("Function_0_20A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_228")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x8, 0x80)
    Jump("loc_292")

    label("loc_228")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_248")
    SetChrFlags(0x9, 0x10)
    SetChrPos(0xA, -27920, 0, 87590, 270)
    Jump("loc_292")

    label("loc_248")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_26D")
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x10)
    SetChrPos(0xA, -27920, 0, 87590, 270)
    Jump("loc_292")

    label("loc_26D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_277")
    Jump("loc_292")

    label("loc_277")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_281")
    Jump("loc_292")

    label("loc_281")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_28B")
    Jump("loc_292")

    label("loc_28B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_292")

    label("loc_292")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (105, "loc_2A2"),
        (106, "loc_2A2"),
        (SWITCH_DEFAULT, "loc_2B8"),
    )


    label("loc_2A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2B5")
    OP_A2(0x338)
    Event(0, 16)

    label("loc_2B5")

    Jump("loc_2B8")

    label("loc_2B8")

    Return()

    # Function_0_20A end

    def Function_1_2B9(): pass

    label("Function_1_2B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2CB")
    OP_10(0x7, 0x1)
    OP_10(0x3, 0x0)

    label("loc_2CB")

    Return()

    # Function_1_2B9 end

    def Function_2_2CC(): pass

    label("Function_2_2CC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2E1")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_2CC")

    label("loc_2E1")

    Return()

    # Function_2_2CC end

    def Function_3_2E2(): pass

    label("Function_3_2E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_373")
    TalkBegin(0xE)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",            # 0
            "改造·换钱\x01",      # 1
            "离开\x01",            # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_354")
    OP_0D()
    OP_A9(0xA)
    OP_56(0x0)
    TalkEnd(0xE)
    Return()

    label("loc_354")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_365")
    TalkEnd(0xE)
    Return()

    label("loc_365")

    Call(0, 11)
    OP_8C(0xE, 180, 0)
    Jump("loc_3FA")

    label("loc_373")

    TalkBegin(0x9)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",            # 0
            "改造·换钱\x01",      # 1
            "离开\x01",            # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DE")
    OP_0D()
    OP_A9(0xA)
    OP_56(0x0)
    TalkEnd(0x9)
    Return()

    label("loc_3DE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3EF")
    TalkEnd(0x9)
    Return()

    label("loc_3EF")

    Call(0, 4)
    OP_8C(0x9, 180, 0)

    label("loc_3FA")

    Return()

    # Function_3_2E2 end

    def Function_4_3FB(): pass

    label("Function_4_3FB")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_605")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_544")
    OP_A2(0x1)

    ChrTalk(
        0x9,
        (
            "帐、帐、帐、\x01",
            "账本被军队没收了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "糟了糟了糟了啊……\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "不、不，等等……\x01",
            "应该不会出事吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "因为最不能被查到的东西\x01",
            "已经被强盗拿走了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_602")

    label("loc_544")


    ChrTalk(
        0x9,
        (
            "账本虽然被军队没收了，\x01",
            "不过应该不会出事的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "因为最不能被查到的东西\x01",
            "已经被强盗拿走了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_602")

    Jump("loc_C7C")

    label("loc_605")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_7FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_782")
    OP_A2(0x1)
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0x9,
        "工、工、工房～！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "我、我的工房里、商品都被～！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "要、要快点去向\x01",
            "军队或者游击士协会通报……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "不、不，等等……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "如果他们来调查\x01",
            "被盗走的那个东西的话……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "哇哇哇哇……\x01",
            "我该怎么做才好啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7FC")

    label("loc_782")


    ChrTalk(
        0x9,
        (
            "如果他们来调查\x01",
            "被盗走的那个东西的话……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "哇哇哇哇……\x01",
            "我该怎么做才好啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7FC")

    Jump("loc_C7C")

    label("loc_7FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_90D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8CC")
    OP_A2(0x1)

    ChrTalk(
        0x9,
        "店里的营业额走势非常好哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "虽然在与工匠的沟通上还有些问题，\x01",
            "不过没关系……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "嘿嘿嘿……\x01",
            "这样下去真能大赚一笔呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_90A")

    label("loc_8CC")


    ChrTalk(
        0x9,
        (
            "嘿嘿嘿……\x01",
            "这样下去真能大赚一笔呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_90A")

    Jump("loc_C7C")

    label("loc_90D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_A60")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9EC")
    OP_A2(0x1)

    ChrTalk(
        0x9,
        (
            "说起来，\x01",
            "那个人也真是太老实了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "哼，\x01",
            "这在商人的世界里\x01",
            "可是站不住脚的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "我才最适合\x01",
            "当这家店的店主。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "哇～哈～哈～哈！\x02",
    )

    CloseMessageWindow()
    Jump("loc_A5D")

    label("loc_9EC")


    ChrTalk(
        0x9,
        (
            "说起来，\x01",
            "那个人也真是太老实了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "我才最适合\x01",
            "当这家店的店主。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "哇～哈～哈～哈！\x02",
    )

    CloseMessageWindow()

    label("loc_A5D")

    Jump("loc_C7C")

    label("loc_A60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_BF1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B56")
    OP_A2(0x1)

    ChrTalk(
        0x9,
        "呼～呼～呼……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "哇～哈～哈～哈～哈！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "笑得合不拢嘴了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "没想到这么简单\x01",
            "就弄到自己的工房了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "这个世界只有聪明的人\x01",
            "才能够生存下来啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BEE")

    label("loc_B56")


    ChrTalk(
        0x9,
        (
            "没想到这么简单\x01",
            "就弄到自己的工房了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "笑得合不拢嘴了。\x01",
            "这个世界只有聪明的人才能生存下来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BEE")

    Jump("loc_C7C")

    label("loc_BF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_C7C")

    ChrTalk(
        0x9,
        (
            "呼，从今天开始\x01",
            "我就是这里的经营者了啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "太棒了！\x01",
            "我要赚越来越多的钱。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "哇～哈～哈！\x02",
    )

    CloseMessageWindow()

    label("loc_C7C")

    TalkEnd(0x9)
    Return()

    # Function_4_3FB end

    def Function_5_C80(): pass

    label("Function_5_C80")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_DFC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x14, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_D18")

    ChrTalk(
        0xFE,
        (
            "以前的店主\x01",
            "回到店里来了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "谢天谢地，\x01",
            "这下又可以专心地研究技术了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DF9")

    label("loc_D18")


    ChrTalk(
        0xFE,
        (
            "不知道为什么，\x01",
            "店主被军队带走了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我只追求自己的技术，\x01",
            "只要有一个工作的环境就可以了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "但是店长不在果然很让人头痛啊。\x02",
    )

    CloseMessageWindow()

    label("loc_DF9")

    Jump("loc_133D")

    label("loc_DFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_FD1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F44")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "店主好像比以前\x01",
            "更加冷静不下来了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "对于强盗入室这件事\x01",
            "好像受了非常大的打击。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我平时只管\x01",
            "强化自己的工艺技术……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "只要给我一个工作的地方，\x01",
            "就没有什么可以担心的了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FCE")

    label("loc_F44")


    ChrTalk(
        0xFE,
        (
            "店主好像比以前\x01",
            "更加冷静不下来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "对于强盗入室这件事\x01",
            "好像受了非常大的打击。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FCE")

    Jump("loc_133D")

    label("loc_FD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_105E")

    ChrTalk(
        0xFE,
        (
            "啊，那些强盗们\x01",
            "把大部分的商品都拿走了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "昨天应该是店主\x01",
            "负责关店门的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_133D")

    label("loc_105E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_113F")

    ChrTalk(
        0xFE,
        (
            "我不会做出\x01",
            "歪曲自己审美意识的作品。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "新来的店主所要求的作品中\x01",
            "品位低下的居多啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "只要看到他那张脸，\x01",
            "我就没有创作欲望了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_133D")

    label("loc_113F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_11E9")

    ChrTalk(
        0xFE,
        (
            "新的店主\x01",
            "总是提出各种各样奇怪的要求……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "以前的店主\x01",
            "却能给我自由创作的空间。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_133D")

    label("loc_11E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_12D3")

    ChrTalk(
        0xFE,
        (
            "不知道什么时候\x01",
            "尼冈德变成店主了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我平时只管\x01",
            "强化自己的工艺技术……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "只要给我一个工作的地方，\x01",
            "谁当店主对我来说都没什么影响。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_133D")

    label("loc_12D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_133D")

    ChrTalk(
        0xFE,
        (
            "唔，\x01",
            "最近店长都没来店里……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "他是不是生病了啊？\x02",
    )

    CloseMessageWindow()

    label("loc_133D")

    TalkEnd(0xA)
    Return()

    # Function_5_C80 end

    def Function_6_1341(): pass

    label("Function_6_1341")

    TalkBegin(0xB)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",        # 0
            "买东西\x01",      # 1
            "离开\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(300, 0)
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13A1")
    OP_0D()
    OP_A9(0xB)
    OP_56(0x0)
    TalkEnd(0xB)
    Return()

    label("loc_13A1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13B2")
    TalkEnd(0xB)
    Return()

    label("loc_13B2")

    Call(0, 7)
    OP_8C(0xB, 180, 0)
    Return()

    # Function_6_1341 end

    def Function_7_13BE(): pass

    label("Function_7_13BE")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_14A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1465")
    OP_A2(0x3)

    ChrTalk(
        0xB,
        (
            "被空贼偷走的商品\x01",
            "都被军队找回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "我终于能够静下心来\x01",
            "好好做买卖了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14A6")

    label("loc_1465")


    ChrTalk(
        0xB,
        (
            "希望军队能够\x01",
            "好好教训一下那帮空贼。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14A6")

    Jump("loc_1D6E")

    label("loc_14A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_162B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1593")
    OP_A2(0x3)

    ChrTalk(
        0xB,
        (
            "还没有找到\x01",
            "那些可恶的强盗犯吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "不管如何，\x01",
            "军队都一定要抓住犯人啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "再这样下去的话，\x01",
            "满肚子牢骚就发不完了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1628")

    label("loc_1593")


    ChrTalk(
        0xB,
        (
            "还没有找到\x01",
            "那些可恶的强盗犯吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "不管如何，\x01",
            "军队都一定要抓住犯人啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1628")

    Jump("loc_1D6E")

    label("loc_162B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_17D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1755")
    OP_A2(0x3)

    ChrTalk(
        0xB,
        "可恶至极！\x02",
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xB,
        "我的店铺也被那些强盗洗劫了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "值钱的商品都被\x01",
            "拿得一点都不剩了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "这种时候本来就没什么东西好卖，\x01",
            "我该怎么办啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17D6")

    label("loc_1755")


    ChrTalk(
        0xB,
        (
            "可恶至极！\x01",
            "我的店铺也被那些强盗洗劫了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "值钱的商品都被\x01",
            "拿得一点都不剩了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17D6")

    Jump("loc_1D6E")

    label("loc_17D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_199A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18E1")
    OP_A2(0x3)

    ChrTalk(
        0xB,
        (
            "在超市里开店的时候，\x01",
            "我的工作可是辛苦得很啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "我想正是有了那份辛苦与经验，\x01",
            "我才有能力经营这家店。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "果然积累是最重要的一环啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1997")

    label("loc_18E1")


    ChrTalk(
        0xB,
        (
            "正因为在超市里\x01",
            "积攒了不少辛苦与经验，\x01",
            "我才有能力经营这家店。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "果然积累是最重要的一环啊。\x02",
    )

    CloseMessageWindow()

    label("loc_1997")

    Jump("loc_1D6E")

    label("loc_199A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_1B98")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AFD")
    OP_A2(0x3)

    ChrTalk(
        0xB,
        (
            "柏斯的商人\x01",
            "大多都是从超市起家的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "一开始会得到市政府的援助，\x01",
            "而且如果有在超市经营的经验，\x01",
            "自己开店就会容易得到认可。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "从很远的地方\x01",
            "特意来到这里的商人也有不少。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B95")

    label("loc_1AFD")


    ChrTalk(
        0xB,
        (
            "一开始会得到市政府的援助，\x01",
            "而且如果有在超市经营的经验，\x01",
            "自己开店就会容易得到认可。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B95")

    Jump("loc_1D6E")

    label("loc_1B98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_1D08")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C76")
    OP_A2(0x3)

    ChrTalk(
        0xB,
        (
            "我年轻的时候\x01",
            "也在柏斯超市拥有店铺呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "现在去超市的时候\x01",
            "还是会感到很怀念。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "希望年轻人\x01",
            "也能够努力干出一番事业来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D05")

    label("loc_1C76")


    ChrTalk(
        0xB,
        (
            "我年轻的时候\x01",
            "也在柏斯超市拥有店铺呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "希望现在的年轻人\x01",
            "也能够努力干出一番事业来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D05")

    Jump("loc_1D6E")

    label("loc_1D08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_1D6E")

    ChrTalk(
        0xB,
        "噢，欢迎光临。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "你们慢慢挑选吧。\x02",
    )

    CloseMessageWindow()

    label("loc_1D6E")

    TalkEnd(0xB)
    Return()

    # Function_7_13BE end

    def Function_8_1D72(): pass

    label("Function_8_1D72")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_1EEE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E64")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "我是来做买卖的，\x01",
            "但不知道什么时候\x01",
            "这家店的主人好像变了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唉，我也只能和新的店主\x01",
            "从头开始谈判了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我什么时候才能把\x01",
            "好消息带回帝都去呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EEB")

    label("loc_1E64")


    ChrTalk(
        0xFE,
        (
            "我是来做买卖的，\x01",
            "但不知道什么时候\x01",
            "这家店的主人好像变了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唉，我也只能和新的店主\x01",
            "从头开始谈判了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EEB")

    Jump("loc_1FFB")

    label("loc_1EEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F82")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "和我做生意的那家店\x01",
            "好像被强盗洗劫了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "现在的确不是谈论\x01",
            "做买卖的时候啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FFB")

    label("loc_1F82")


    ChrTalk(
        0xFE,
        (
            "话又说回来，\x01",
            "现在连记者都赶到了，\x01",
            "为什么早没人去通知游击士？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FFB")

    TalkEnd(0x8)
    Return()

    # Function_8_1D72 end

    def Function_9_1FFF(): pass

    label("Function_9_1FFF")

    TalkBegin(0xC)

    ChrTalk(
        0xC,
        (
            "#141F多亏了你们提供的消息，\x01",
            "这次的杂志篇幅将会非常大哦。\x02\x03",
            "如果再有什么新闻的话一定要告诉我。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xC)
    Return()

    # Function_9_1FFF end

    def Function_10_20AC(): pass

    label("Function_10_20AC")

    TalkBegin(0xD)

    ChrTalk(
        0xD,
        (
            "#150F听说这里展示的最新型相机\x01",
            "也被空贼盗走了呢～\x02\x03",
            "那些空贼，\x01",
            "是不是对拍照很感兴趣呢？\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xD)
    Return()

    # Function_10_20AC end

    def Function_11_2133(): pass

    label("Function_11_2133")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x14, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2353")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22AA")
    OP_A2(0x4)

    ChrTalk(
        0xE,
        (
            "尼冈德做的坏事\x01",
            "终于被查出来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "我也重新成为了\x01",
            "这家店的店主。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "真是不禁令人感叹啊。\x01",
            "从此作为商人重新出发吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "我以前确实太老实了，\x01",
            "也说不定因此而让人看不起。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "虽然不甘心，\x01",
            "不过多亏了尼冈德让我认识了这一点。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2350")

    label("loc_22AA")


    ChrTalk(
        0xE,
        (
            "不过，\x01",
            "尼冈德毕竟曾经与我共患难过。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "找个时间去给他送饭，\x01",
            "顺便看望一下他吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2350")

    Jump("loc_240F")

    label("loc_2353")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_240F")

    ChrTalk(
        0xE,
        (
            "尼冈德那家伙\x01",
            "被带到哈肯大门那里去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "没有办法， \x01",
            "只好由我来暂时接管这个工房了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "那家伙好像\x01",
            "干了相当坏的事情。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_240F")

    TalkEnd(0xE)
    Return()

    # Function_11_2133 end

    def Function_12_2413(): pass

    label("Function_12_2413")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_243D")
    Sleep(500)
    Sleep(500)
    OP_8E(0xFE, 0xFFFFA312, 0x0, 0x166AC, 0xBB8, 0x0)

    label("loc_243D")

    OP_8E(0xFE, 0xFFFFA61E, 0x0, 0x15E82, 0xBB8, 0x0)
    TurnDirection(0xFE, 0xD, 400)
    Return()

    # Function_12_2413 end

    def Function_13_2459(): pass

    label("Function_13_2459")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2488")
    Sleep(500)
    Sleep(500)
    Sleep(500)
    OP_8E(0xFE, 0xFFFFA312, 0x0, 0x166AC, 0xBB8, 0x0)

    label("loc_2488")

    OP_8E(0xFE, 0xFFFFA89E, 0x0, 0x1615C, 0xBB8, 0x0)
    TurnDirection(0xFE, 0xC, 400)
    Return()

    # Function_13_2459 end

    def Function_14_24A4(): pass

    label("Function_14_24A4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24C9")
    Sleep(500)
    OP_8E(0xFE, 0xFFFFA312, 0x0, 0x166AC, 0xBB8, 0x0)

    label("loc_24C9")

    OP_8E(0xFE, 0xFFFFA24A, 0x0, 0x15C16, 0xBB8, 0x0)
    TurnDirection(0xFE, 0xC, 400)
    Return()

    # Function_14_24A4 end

    def Function_15_24E5(): pass

    label("Function_15_24E5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2505")
    OP_8E(0xFE, 0xFFFFA312, 0x0, 0x166AC, 0xBB8, 0x0)

    label("loc_2505")

    OP_8E(0xFE, 0xFFFFAC5E, 0x0, 0x15E46, 0xBB8, 0x0)
    TurnDirection(0xFE, 0xC, 400)
    Return()

    # Function_15_24E5 end

    def Function_16_2521(): pass

    label("Function_16_2521")

    EventBegin(0x0)
    OP_6D(-23490, 0, 87480, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    OP_4A(0xC, 255)
    OP_4A(0xD, 255)
    SetChrPos(0xD, -24322, 0, 85809, 270)
    SetChrPos(0xC, -21888, 0, 88170, 135)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25E7")
    SetChrPos(0x101, -28760, -2000, 92070, 180)
    SetChrPos(0x102, -28760, -2000, 92070, 180)
    SetChrPos(0x103, -28760, -2000, 92070, 180)
    SetChrPos(0x104, -28760, -2000, 92070, 180)
    Jump("loc_262B")

    label("loc_25E7")

    SetChrPos(0x101, -21890, 0, 91590, 180)
    SetChrPos(0x102, -21160, 0, 92440, 180)
    SetChrPos(0x103, -20430, 0, 91410, 180)
    SetChrPos(0x104, -22770, 0, 92110, 180)

    label("loc_262B")

    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0xD,
        "#151F嘿嘿，照得挺可爱的嘛。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xC, 400)

    ChrTalk(
        0xD,
        (
            "#150F奈尔前辈～\x01",
            "照出这种感觉就可以了吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xD, 400)

    ChrTalk(
        0xC,
        (
            "#140F啊啊，我要的就是这种。\x02\x03",
            "#140F不过只能从里面挑选一张，\x01",
            "抉择起来还真是很难啊。\x02\x03",
            "#142F………嗯？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2718():
        OP_8C(0xC, 0, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2718)

    def lambda_2726():
        OP_6D(-22600, 0, 89590, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2726)
    OP_43(0x101, 0x1, 0x0, 0xC)
    OP_43(0x102, 0x1, 0x0, 0xD)
    OP_43(0x103, 0x1, 0x0, 0xF)
    OP_43(0x104, 0x1, 0x0, 0xE)
    WaitChrThread(0x102, 0x1)
    WaitChrThread(0x101, 0x3)

    ChrTalk(
        0x102,
        (
            "#010F#2P你们好。\x01",
            "又要赶着去取材吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F#1P你们也很辛苦呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#141F哦，是你们啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#153F啊～！\x01",
            "是小艾和小约呢～！\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0xD, 0xFFFFA646, 0x0, 0x15568, 0xBB8, 0x0)
    TurnDirection(0xD, 0x101, 400)

    ChrTalk(
        0xD,
        "#151F太好了，终于释放了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#141F我们已经听说了。\x01",
            "军队那些家伙在废坑把你们逮捕了。\x02\x03",
            "真是的～害我们担心死了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F#1P说得好像完全事不关己一样，\x01",
            "你会担心才怪呢～\x02\x03",
            "不知道是谁给的情报，\x01",
            "害我们在村子遇到那种事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#141F喂喂，怎么反过来怪我呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#2P奈尔先生你们\x01",
            "也去过拉文努村的废坑那里吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#150F是的～就是昨天呢。\x02\x03",
            "#150F就在小约你们\x01",
            "被那些军人带走之后。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#142F要是我们也在逮捕现场的话，\x01",
            "一定会给你们拍几张有趣的照片……\x02\x03",
            "#147F呵呵，拿来自己收藏也不错。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009F哼，大叔你太过分了！\x01",
            "亏你还是个专业的杂志记者。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F对了，记者先生。 \x01",
            "你认为昨天的盗窃案是空贼干的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#140F啊啊，应该就是。\x02\x03",
            "现在军队也在\x01",
            "到处寻找案件的线索……\x02\x03",
            "不过暂时还没有头绪。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#026F哎呀，真的挺棘手啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#030F记者先生，可以问你一下吗？\x02\x03",
            "那些空贼，\x01",
            "是从哪个方向进入城里的？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x104, 400)

    ChrTalk(
        0xC,
        (
            "#140F啊啊，根据目击者的口述，\x01",
            "好像是从西门进来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#030F是吗，那就奇怪了。\x02\x03",
            "西门附近不就是\x01",
            "市长官邸和柏斯超市吗……\x02\x03",
            "按道理，向这两个地方下手\x01",
            "反而能得到更多好处才对啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#143F这么说来，的确是啊……\x02\x03",
            "#142F……对了，你是哪位？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#035F呵呵，你要仔细听好哦。\x02\x03",
            "奥利维尔·朗海姆……\x01",
            "漂泊的诗人，天才演奏家就是本人。\x02\x03",
            "你们应该听说过我的名字吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#151F啊～在餐厅里偷喝了\x01",
            "高级葡萄酒然后逃之夭夭的人。\x02\x03",
            "能够认识你真是太荣幸了～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#031F哈哈，我都被你称赞得脸红了。\x02\x03",
            "如果你们有需要的话，\x01",
            "我可是非常乐意接受你们的采访哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xD,
        "#151F呜哇～真的吗？\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0xC, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#007F真是服了这两个人了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F从某种意义上说……\x01",
            "他们也算是同一类型的吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#145F这丫头，不理睬一起干事的同伴，\x01",
            "却偏对刚认识的人这么热情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#021F呵呵，怎么吃起醋来了。\x02",
    )

    CloseMessageWindow()
    OP_28(0x37, 0x1, 0x2)
    OP_4B(0xC, 255)
    OP_4B(0xD, 255)
    EventEnd(0x0)
    Return()

    # Function_16_2521 end

    SaveToFile()

Try(main)
