from ED6ScenarioHelper import *

def main():
    # 柏斯

    CreateScenaFile(
        FileName            = 'T1400   ._SN',
        MapName             = 'Bose',
        Location            = 'T1400.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60016",
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
        '卫兵',                                 # 9
        '卫兵',                                 # 10
        '卡尔科斯',                             # 11
        '卡尔科斯',                             # 12
        '金发青年',                             # 13
        '摩尔根将军',                           # 14
        '亚妮拉丝',                             # 15
        '王国军士兵',                           # 16
        '王国军士兵',                           # 17
        '目标用摄像机',                         # 18
        '钢壁之路方向',                         # 19
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
        'ED6_DT07/CH01640 ._CH',             # 00
        'ED6_DT07/CH01040 ._CH',             # 01
        'ED6_DT07/CH00030 ._CH',             # 02
        'ED6_DT07/CH02080 ._CH',             # 03
        'ED6_DT07/CH01630 ._CH',             # 04
        'ED6_DT07/CH01650 ._CH',             # 05
        'ED6_DT06/CH20045 ._CH',             # 06
        'ED6_DT06/CH20039 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT07/CH01640P._CP',             # 00
        'ED6_DT07/CH01040P._CP',             # 01
        'ED6_DT07/CH00030P._CP',             # 02
        'ED6_DT07/CH02080P._CP',             # 03
        'ED6_DT07/CH01630P._CP',             # 04
        'ED6_DT07/CH01650P._CP',             # 05
        'ED6_DT06/CH20045P._CP',             # 06
        'ED6_DT06/CH20039P._CP',             # 07
    )

    DeclNpc(
        X                   = 8250,
        Z                   = 0,
        Y                   = -12000,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -2400,
        Z                   = 0,
        Y                   = -7500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -2100,
        Z                   = 0,
        Y                   = -20100,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 2500,
        Z                   = 0,
        Y                   = -7500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 19250,
        Z                   = 0,
        Y                   = 14430,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 209710,
        Z                   = 0,
        Y                   = 11740,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -10600,
        Z                   = 0,
        Y                   = -29900,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -9000,
        Z                   = 11750,
        Y                   = 3000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 9000,
        Z                   = 11750,
        Y                   = 3000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 11890,
        Z                   = 40,
        Y                   = -60460,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = 8810,
        Y                   = -1000,
        Z                   = -12035,
        Range               = 3000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 19,
    )

    DeclEvent(
        X                   = 3830,
        Y                   = -1000,
        Z                   = -43570,
        Range               = 10270,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0xFFFF5880,
        Unknown_18          = 0x0,
        Unknown_1C          = 30,
    )


    ScpFunction(
        "Function_0_28A",          # 00, 0
        "Function_1_34F",          # 01, 1
        "Function_2_393",          # 02, 2
        "Function_3_3A9",          # 03, 3
        "Function_4_3CD",          # 04, 4
        "Function_5_3F1",          # 05, 5
        "Function_6_72E",          # 06, 6
        "Function_7_1070",         # 07, 7
        "Function_8_14A9",         # 08, 8
        "Function_9_1BF5",         # 09, 9
        "Function_10_1E29",        # 0A, 10
        "Function_11_2398",        # 0B, 11
        "Function_12_2716",        # 0C, 12
        "Function_13_2C73",        # 0D, 13
        "Function_14_32E4",        # 0E, 14
        "Function_15_3747",        # 0F, 15
        "Function_16_3777",        # 10, 16
        "Function_17_37AC",        # 11, 17
        "Function_18_37E1",        # 12, 18
        "Function_19_380F",        # 13, 19
        "Function_20_39F6",        # 14, 20
        "Function_21_5143",        # 15, 21
        "Function_22_5198",        # 16, 22
        "Function_23_51ED",        # 17, 23
        "Function_24_523D",        # 18, 24
        "Function_25_5263",        # 19, 25
        "Function_26_527F",        # 1A, 26
        "Function_27_52A0",        # 1B, 27
        "Function_28_52ED",        # 1C, 28
        "Function_29_5368",        # 1D, 29
        "Function_30_5389",        # 1E, 30
    )


    def Function_0_28A(): pass

    label("Function_0_28A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_2B4")
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8)
    SetChrPos(0x8, 8230, 0, -10540, 270)
    Jump("loc_30A")

    label("loc_2B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_2CF")
    SetChrPos(0x8, 8230, 0, -10540, 270)
    Jump("loc_30A")

    label("loc_2CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_2D9")
    Jump("loc_30A")

    label("loc_2D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 7)), scpexpr(EXPR_END)), "loc_2E8")
    ClearChrFlags(0xE, 0x80)
    Jump("loc_30A")

    label("loc_2E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_2F2")
    Jump("loc_30A")

    label("loc_2F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 1)), scpexpr(EXPR_END)), "loc_30A")
    SetChrPos(0x8, 8300, 0, -10500, 180)

    label("loc_30A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_31D")
    SetMapFlags(0x10000000)
    OP_A3(0x3FA)
    Event(0, 14)

    label("loc_31D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_330")
    SetMapFlags(0x10000000)
    OP_A3(0x3FB)
    Event(0, 20)

    label("loc_330")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_33C"),
        (SWITCH_DEFAULT, "loc_34E"),
    )


    label("loc_33C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34B")
    OP_A2(0x30D)
    Event(0, 13)

    label("loc_34B")

    Jump("loc_34E")

    label("loc_34E")

    Return()

    # Function_0_28A end

    def Function_1_34F(): pass

    label("Function_1_34F")

    OP_16(0x2, 0xFA0, 0xFFFE2370, 0xFFFE0430, 0x30045)
    OP_6F(0x3, 0)
    OP_72(0x3, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_377")
    Jump("loc_392")

    label("loc_377")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_386")
    Jump("loc_392")

    label("loc_386")

    OP_6F(0x1, 0)
    OP_72(0x1, 0x10)

    label("loc_392")

    Return()

    # Function_1_34F end

    def Function_2_393(): pass

    label("Function_2_393")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3A8")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_393")

    label("loc_3A8")

    Return()

    # Function_2_393 end

    def Function_3_3A9(): pass

    label("Function_3_3A9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3CC")
    OP_8D(0xFE, -7000, -13000, 3500, -25300, 2000)
    Jump("Function_3_3A9")

    label("loc_3CC")

    Return()

    # Function_3_3A9 end

    def Function_4_3CD(): pass

    label("Function_4_3CD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3F0")
    OP_8D(0xFE, -15100, -32400, -9800, -27500, 2000)
    Jump("Function_4_3CD")

    label("loc_3F0")

    Return()

    # Function_4_3CD end

    def Function_5_3F1(): pass

    label("Function_5_3F1")

    EventBegin(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "④到达哈肯门。\x01",            # 0
            "③和梅贝尔会面。\x01",          # 1
            "⑥和摩尔根将军会面。\x01",      # 2
            "⑧赶往拉文努村。\x01",          # 3
            "嘗被王国军释放。\x01",          # 4
            "嘙赶往湖畔旅馆。\x01",          # 5
            "标志解除光线\x01",              # 6
            "取消\x01",                      # 7
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_503"),
        (1, "loc_556"),
        (2, "loc_57C"),
        (3, "loc_5B9"),
        (4, "loc_60B"),
        (5, "loc_669"),
        (6, "loc_6CC"),
        (SWITCH_DEFAULT, "loc_712"),
    )


    label("loc_503")

    OP_A2(0x219)
    OP_A2(0x202)
    OP_A2(0x203)
    OP_A2(0x205)
    OP_A2(0x207)
    OP_A2(0x217)
    OP_A2(0x206)
    OP_A2(0x212)
    OP_A2(0x213)
    OP_A2(0x239)
    OP_A2(0x24F)
    OP_A2(0x259)
    OP_A2(0x261)
    OP_A2(0x301)
    OP_A2(0x30C)

    ChrTalk(
        0x101,
        "#000F④到达哈肯门。\x02",
    )

    CloseMessageWindow()
    Jump("loc_728")

    label("loc_556")

    OP_A2(0x301)
    OP_A2(0x30A)
    OP_A2(0x30B)

    ChrTalk(
        0x101,
        "#000F③和梅贝尔会面。\x02",
    )

    CloseMessageWindow()
    Jump("loc_728")

    label("loc_57C")

    OP_A2(0x301)
    OP_A2(0x30A)
    OP_A2(0x30B)
    OP_A2(0x30C)
    OP_A2(0x310)
    OP_A2(0x312)
    OP_A2(0x313)

    ChrTalk(
        0x101,
        "#000F⑥和摩尔根将军会面。\x02",
    )

    CloseMessageWindow()
    Jump("loc_728")

    label("loc_5B9")

    OP_A2(0x301)
    OP_A2(0x30A)
    OP_A2(0x30B)
    OP_A2(0x30C)
    OP_A2(0x310)
    OP_A2(0x312)
    OP_A2(0x314)
    OP_A2(0x317)
    OP_A2(0x318)
    OP_A2(0x313)

    ChrTalk(
        0x101,
        "#000F⑧赶往拉文努村。\x02",
    )

    CloseMessageWindow()
    Jump("loc_728")

    label("loc_60B")

    OP_A2(0x301)
    OP_A2(0x30A)
    OP_A2(0x30B)
    OP_A2(0x30C)
    OP_A2(0x310)
    OP_A2(0x312)
    OP_A2(0x314)
    OP_A2(0x317)
    OP_A2(0x318)
    OP_A2(0x31B)
    OP_A2(0x31C)
    OP_A2(0x31D)
    OP_A2(0x31E)
    OP_A2(0x32B)
    OP_A2(0x313)

    ChrTalk(
        0x101,
        "#000F嘗被王国军释放。\x02",
    )

    CloseMessageWindow()
    Jump("loc_728")

    label("loc_669")

    OP_A2(0x301)
    OP_A2(0x30A)
    OP_A2(0x30B)
    OP_A2(0x30C)
    OP_A2(0x310)
    OP_A2(0x312)
    OP_A2(0x314)
    OP_A2(0x317)
    OP_A2(0x318)
    OP_A2(0x31B)
    OP_A2(0x31C)
    OP_A2(0x31D)
    OP_A2(0x31E)
    OP_A2(0x32B)
    OP_A2(0x33A)
    OP_A2(0x313)

    ChrTalk(
        0x101,
        "#000F嘙赶往湖畔旅馆。\x02",
    )

    CloseMessageWindow()
    Jump("loc_728")

    label("loc_6CC")

    OP_A3(0x301)
    OP_A3(0x30A)
    OP_A3(0x30B)
    OP_A3(0x30C)
    OP_A3(0x310)
    OP_A3(0x312)
    OP_A3(0x314)
    OP_A3(0x317)
    OP_A3(0x318)
    OP_A3(0x31B)
    OP_A3(0x31C)
    OP_A3(0x31D)
    OP_A3(0x31E)
    OP_A3(0x32B)
    OP_A3(0x33A)
    OP_A3(0x313)

    ChrTalk(
        0x101,
        "#000F照射。\x02",
    )

    CloseMessageWindow()
    Jump("loc_728")

    label("loc_712")


    ChrTalk(
        0x101,
        "#000F什么也不做。\x02",
    )

    CloseMessageWindow()

    label("loc_728")

    OP_5F(0x0)
    EventEnd(0x0)
    Return()

    # Function_5_3F1 end

    def Function_6_72E(): pass

    label("Function_6_72E")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_790")

    ChrTalk(
        0xFE,
        "哦，你们是上次的游击士……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "找将军阁下有事吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_106C")

    label("loc_790")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_7EF")

    ChrTalk(
        0xFE,
        "找将军阁下有事吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "现在他应该\x01",
            "十分繁忙吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_106C")

    label("loc_7EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_843")

    ChrTalk(
        0xFE,
        "啊，是你们啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "找将军阁下有事吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_106C")

    label("loc_843")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_8EA")

    ChrTalk(
        0xFE,
        "记得你们是上次的游击士……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "抱歉啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "将军是那样说的，\x01",
            "连一只猫都不能放进去。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_106C")

    label("loc_8EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_96D")

    ChrTalk(
        0xFE,
        "抱歉啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "将军是那样说的，\x01",
            "连一只猫都不能放进去。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_106C")

    label("loc_96D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_A14")

    ChrTalk(
        0xFE,
        "将军的办公室在走廊尽头的左边。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "请记住不要\x01",
            "随便进入其它无关的场所。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_106C")

    label("loc_A14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FEC")
    EventBegin(0x0)
    OP_A2(0x30E)
    OP_69(0x8, 0x3E8)

    ChrTalk(
        0x8,
        (
            "你们几个……\x01",
            "到底从哪里进来的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "钢壁之路的监察站\x01",
            "应该还没有解除的呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我们是柏斯市的\x01",
            "梅贝尔市长派来的人。\x02\x03",
            "能不能请您\x01",
            "向摩尔根将军通报一下？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "在没有表明游击士身份的情况下，\x01",
            "众人对市长的委托进行了说明。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x8,
        "是这样啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "你们的来意我已经明白了，\x01",
            "不过非常不凑巧，将军现在不在这里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "他去现场指挥搜索行动了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F来的不是时候呢……\x02\x03",
            "那将军大概什么时候会回来？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "唔……应该在今天之内吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "那边的休息所里有酒馆，\x01",
            "或者你们先到那里等一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "将军一回来我就去通知你们。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DD4")

    ChrTalk(
        0x101,
        (
            "#004F休息所……还有酒馆……\x01",
            "为什么会有这种设施呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E3C")

    label("loc_DD4")


    ChrTalk(
        0x101,
        (
            "#000F酒馆就是刚才的那个地方吧。\x01",
            "为什么会有那种设施呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E3C")


    ChrTalk(
        0x8,
        "不管怎么说这里是和帝国接壤的国境呀。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "出入国境的审查很严格，\x01",
            "所以有很多旅行者被耽误了行程。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F原来如此。这样一来，\x01",
            "像旅馆这样的设施就必不可少了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F那么，就照你的意思，\x01",
            "我们去酒馆里等候消息吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x35, 0x1, 0x100)
    EventEnd(0x1)
    Jump("loc_106C")

    label("loc_FEC")


    ChrTalk(
        0x8,
        (
            "那边的休息所里有酒馆，\x01",
            "你们先到那里等一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "将军一回来我就去通知你们。\x02",
    )

    CloseMessageWindow()

    label("loc_106C")

    TalkEnd(0x8)
    Return()

    # Function_6_72E end

    def Function_7_1070(): pass

    label("Function_7_1070")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_10E9")

    ChrTalk(
        0xFE,
        "欢迎来到哈肯大门。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "空贼们被逮捕了，\x01",
            "终于可以从第一级警戒体制中\x01",
            "解放出来了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14A5")

    label("loc_10E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_1189")

    ChrTalk(
        0xFE,
        (
            "虽然找到了定期船，\x01",
            "不过犯人还是没有下落啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "现在国境守备队\x01",
            "仍然在全力搜索之中。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14A5")

    label("loc_1189")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_12B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1295")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        "欢迎来到哈肯大门！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呀？你们……\x01",
            "你们是之前被关进监狱的游击士吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#509F这种事情偏偏记得这么清楚～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哈哈，反正嫌疑已经洗清了，\x01",
            "这不是很好嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12B5")

    label("loc_1295")


    ChrTalk(
        0xFE,
        "欢迎来到哈肯大门！\x02",
    )

    CloseMessageWindow()

    label("loc_12B5")

    Jump("loc_14A5")

    label("loc_12B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_130B")

    ChrTalk(
        0xFE,
        (
            "欢迎来到哈肯大门！\x01",
            "打算去埃雷波尼亚帝国吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14A5")

    label("loc_130B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_1395")

    ChrTalk(
        0xFE,
        (
            "将军的怒吼声\x01",
            "站在这里都能听得到……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "你、你们\x01",
            "到底做了些什么？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14A5")

    label("loc_1395")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_1439")

    ChrTalk(
        0xFE,
        "现在这个关所处于戒严状态。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "请你们注意，\x01",
            "不要随便走动。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14A5")

    label("loc_1439")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 4)), scpexpr(EXPR_END)), "loc_14A5")

    ChrTalk(
        0xFE,
        "欢迎来到哈肯大门！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……啊，什么？\x01",
            "你们穿过街道了？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14A5")

    TalkEnd(0x9)
    Return()

    # Function_7_1070 end

    def Function_8_14A9(): pass

    label("Function_8_14A9")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_164A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_159B")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "我的出国手续\x01",
            "终于办理好了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "可是滞留在这里时\x01",
            "吃饭住宿也把旅费都用完了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哈哈，反正我的人生\x01",
            "也是走到哪里算哪里，\x01",
            "怎样都无所谓啦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1647")

    label("loc_159B")


    ChrTalk(
        0xFE,
        (
            "我的出国手续\x01",
            "终于办理好了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "可是滞留在这里时\x01",
            "吃饭住宿也把旅费都用完了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1647")

    Jump("loc_1BF1")

    label("loc_164A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_1861")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17C7")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "一个人是不是幸福，\x01",
            "要看最后他对人生\x01",
            "是否满足。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果本人感到满足的话，\x01",
            "不管谁再说什么，\x01",
            "他的人生都是幸福的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我的人生格言就是\x01",
            "走到哪里算哪里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "谁说我也没有用。\x02",
    )

    CloseMessageWindow()
    Jump("loc_185E")

    label("loc_17C7")


    ChrTalk(
        0xFE,
        (
            "我的人生格言就是\x01",
            "走到哪里算哪里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "谁说我也没有用。\x02",
    )

    CloseMessageWindow()

    label("loc_185E")

    Jump("loc_1BF1")

    label("loc_1861")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_1919")

    ChrTalk(
        0xFE,
        (
            "反正即使认真地对待生活，\x01",
            "该遭遇不幸的时候仍然会遭遇不幸。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "既然如此，\x01",
            "还是以随遇而安的态度活着比较轻松。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BF1")

    label("loc_1919")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_19DB")

    ChrTalk(
        0xFE,
        (
            "百日战役结束之后，\x01",
            "到帝国旅行的人\x01",
            "一直都很少。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那场战争对利贝尔的人民\x01",
            "果然留下了很深的创伤。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BF1")

    label("loc_19DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 4)), scpexpr(EXPR_END)), "loc_1BF1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B3F")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "我本来想要\x01",
            "去帝国那边旅行……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过现在好像\x01",
            "不能办理出境手续了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "算了，反正我的人生\x01",
            "也是走到哪里算哪里，\x01",
            "怎样都无所谓啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "想要去帝国旅行\x01",
            "也是一时兴起罢了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BF1")

    label("loc_1B3F")


    ChrTalk(
        0xFE,
        (
            "现在好像不能\x01",
            "办理出境手续了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "算了，反正我的人生\x01",
            "也是走到哪里算哪里，\x01",
            "怎样都无所谓啦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BF1")

    TalkEnd(0xA)
    Return()

    # Function_8_14A9 end

    def Function_9_1BF5(): pass

    label("Function_9_1BF5")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_1CB4")

    ChrTalk(
        0xFE,
        (
            "呵呵，没想到第一次的任务　\x01",
            "竟然是突入空贼的基地……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "漫无计划的人生\x01",
            "就是由各种各样的经历组成的啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E25")

    label("loc_1CB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_1E25")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DAE")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "我本来想要\x01",
            "去帝国那边旅行……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "由于没有旅费，\x01",
            "我加入了国境守备队。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "算了，\x01",
            "我的人生本来就是漫无计划的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我一点都没有后悔过哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E25")

    label("loc_1DAE")


    ChrTalk(
        0xFE,
        (
            "我本来想要\x01",
            "去帝国那边旅行……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "由于没有旅费，\x01",
            "我加入了国境守备队。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E25")

    TalkEnd(0xB)
    Return()

    # Function_9_1BF5 end

    def Function_10_1E29(): pass

    label("Function_10_1E29")

    TalkBegin(0xE)
    TurnDirection(0xFE, 0x103, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2180")
    OP_A2(0x360)
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "#814F啊，难道……\x01",
            "这不是雪拉扎德前辈吗？\x02\x03",
            "#850F很久不见了啊。\x01",
            "自从您去修行之后就再没见面了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F这不是亚妮拉丝吗。\x01",
            "你在这里做什么呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#810F嗯～\x01",
            "协会委托我来这边消灭通缉魔兽。\x02\x03",
            "街道的封锁被解除了，\x01",
            "我也终于能把委托给完成了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F是这样啊……\x02\x03",
            "对了，\x01",
            "你已经找到所谓的剑之道了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#819F呵呵，请别问了。\x01",
            "我还处在修行阶段呢。\x02\x03",
            "#810F说起来，\x01",
            "前辈您也是在执行协会的任务吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#020F是啊，不过我和你的任务性质不同。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#810F是这样啊……\x02\x03",
            "这个地方最近\x01",
            "发生了很多事呢。\x02\x03",
            "您路上一定要小心哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2394")

    label("loc_2180")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_230C")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "#810F啊，雪拉扎德前辈……\x02\x03",
            "前辈，您在调查那个失踪的定期船事件，\x01",
            "是真的吗？\x02\x03",
            "#856F不好意思，\x01",
            "这次我没能帮上什么忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F你就别说这么见外的话啦。\x02\x03",
            "而且这次的事件\x01",
            "不多不少也和我们有关系的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#814F原来是这样啊。\x02\x03",
            "#810F不管怎么说，\x01",
            "你们一定要小心哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2394")

    label("loc_230C")


    ChrTalk(
        0xFE,
        (
            "#856F最近，\x01",
            "柏斯支部的游击士都在忙于工作。\x02\x03",
            "由于发生了定期船的事件，\x01",
            "人手变得不够用了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2394")

    TalkEnd(0xE)
    Return()

    # Function_10_1E29 end

    def Function_11_2398(): pass

    label("Function_11_2398")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_24AD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2457")
    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "出动如此大规模的国境守备队\x01",
            "还是百日战役以来的第一次啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "帝国那边不要误会\x01",
            "我们有什么大的军事行动就好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24AA")

    label("loc_2457")


    ChrTalk(
        0xFE,
        (
            "出动如此大规模的国境守备队\x01",
            "还是百日战役以来的第一次啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24AA")

    Jump("loc_2712")

    label("loc_24AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_2565")

    ChrTalk(
        0xFE,
        (
            "听说摩尔根将军\x01",
            "改变了搜索的方针。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "好像是因为\x01",
            "王国军新设立的情报部\x01",
            "给搜索来了很多情报。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2712")

    label("loc_2565")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_2635")

    ChrTalk(
        0xFE,
        (
            "针对空贼团的搜索\x01",
            "好像陷入了困境。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "警备飞艇对北部山岳一带\x01",
            "进行了全方位的搜索……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过暂时好像还没有\x01",
            "找到什么重要的线索啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2712")

    label("loc_2635")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_2712")

    ChrTalk(
        0xFE,
        (
            "国境守备队经常要\x01",
            "随时面对来自帝国的威胁。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "无论什么时候，\x01",
            "我们都一定要非常谨慎才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为不知道\x01",
            "帝国又会找什么借口实行侵略。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2712")

    TalkEnd(0xF)
    Return()

    # Function_11_2398 end

    def Function_12_2716(): pass

    label("Function_12_2716")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_278A")

    ChrTalk(
        0xFE,
        "今天的天气很好啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "从这里可以很清楚望到帝国那边的领土。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2C6F")

    label("loc_278A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_2944")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2889")
    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "幸好帝国现在\x01",
            "还没有什么军事行动。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "两国缔结了不侵犯条约，\x01",
            "他们没有动静也是理所当然的啦……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过相互之间的紧张关系\x01",
            "是不会这么容易被化解的啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2941")

    label("loc_2889")


    ChrTalk(
        0xFE,
        (
            "幸好帝国现在\x01",
            "还没有什么军事行动。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "两国缔结了不侵犯条约，\x01",
            "他们没有动静也是理所当然的啦……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2941")

    Jump("loc_2C6F")

    label("loc_2944")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_2B6B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AB7")
    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "以前，国境线前面不远处\x01",
            "有一个被称为哈梅尔的帝国小村落。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "不过现在已经不能再看到那个村子啦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "据说在百日战役的时候，\x01",
            "那个村子消失在战火之中。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果不是利贝尔军反击战造成的，\x01",
            "那么消失的原因是什么呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B68")

    label("loc_2AB7")


    ChrTalk(
        0xFE,
        (
            "以前，国境线前面不远处\x01",
            "有一个被称为哈梅尔的帝国小村落。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "据说在百日战役的时候，\x01",
            "那个村子消失在战火之中。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B68")

    Jump("loc_2C6F")

    label("loc_2B6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_2C6F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C21")
    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "虽然这已经是十年之前的事情了。\x01",
            "但在这里站岗我还是觉得紧张。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "希望帝国军队\x01",
            "不要再次发动袭击\x01",
            "将这道门攻破……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C6F")

    label("loc_2C21")


    ChrTalk(
        0xFE,
        (
            "希望帝国军队\x01",
            "不要再次发动袭击\x01",
            "将这道门攻破……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C6F")

    TalkEnd(0x10)
    Return()

    # Function_12_2716 end

    def Function_13_2C73(): pass

    label("Function_13_2C73")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    SetChrPos(0x101, 7940, 30, -38220, 0)
    SetChrPos(0x102, 6200, 0, -38720, 0)
    SetChrPos(0x103, 7430, 0, -40110, 0)
    OP_6D(14550, 11750, 700, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(5560, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    StopSound(0x9470, 0x3D090, 0x0)
    FadeToBright(2000, 0)
    OP_6D(-8310, 11750, 800, 5000)
    Fade(1000)
    OP_6D(-440, 11200, -19210, 0)
    OP_67(0, 4860, -10000, 0)
    OP_6B(6560, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)

    def lambda_2D59():
        OP_6B(3250, 9000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_2D59)

    def lambda_2D69():
        OP_67(0, 8000, -10000, 9000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2D69)
    Sleep(3000)

    def lambda_2D86():
        OP_6C(45000, 6000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_2D86)

    def lambda_2D96():
        OP_6D(7190, 50, -38190, 6000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_2D96)
    StopSound(0x9470, 0x186A0, 0x1B58)
    Sleep(6000)

    ChrTalk(
        0x101,
        (
            "#004F这、这就是哈肯大门……\x02\x03",
            "真是大得夸张啊～！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F作为连通帝国方面的唯一关口，\x01",
            "这里是抵御威胁保卫王国的屏障……\x02\x03",
            "由于在１０年前的战争中被破坏过，\x01",
            "所以又重新加固了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F也就是说，这里的另一侧\x01",
            "就已经不再是利贝尔王国了吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F是啊……\x02\x03",
            "那边就是埃雷波尼亚帝国的领土，\x01",
            "一个以『黄金军马』为国徽的军事国家。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F埃雷波尼亚帝国……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#015F…………………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F那么，\x01",
            "我们赶快去和摩尔根将军会面吧。\x02\x03",
            "大门的旁边有营房……\x01",
            "我们就去那边看看吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#006F嗯，ＯＫ！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F在那之前……\x02\x03",
            "你们两个先把\x01",
            "胸前的游击士徽章摘下来吧。\x02\x03",
            "要是被摩尔根将军看到就麻烦了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x103, 400)
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(
        0x101,
        "#000F啊，我都忘了……\x02",
    )

    CloseMessageWindow()
    OP_22(0x8F, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾丝蒂尔和约修亚把游击士徽章摘了下来。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x101,
        (
            "#008F不、不知怎么搞的，\x01",
            "感觉很不习惯呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F嗯，的确感觉有些不适应。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#021F呵呵，这就证明\x01",
            "你们已经习惯游击士这个身份了。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_13_2C73 end

    def Function_14_32E4(): pass

    label("Function_14_32E4")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(-15040, 500, -25820, 0)
    OP_A2(0x310)
    SetChrPos(0x101, -14860, 500, -23500, 180)
    SetChrPos(0x103, -14860, 500, -23500, 180)
    SetChrPos(0x102, -14860, 500, -23500, 180)
    SetChrPos(0xC, -14860, 500, -23500, 180)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x40)
    Sleep(500)
    OP_70(0x0, 0x14)
    OP_73(0x0)
    SetChrPos(0x11, -15050, 500, -29150, 0)
    OP_43(0x103, 0x0, 0x0, 0xF)
    OP_43(0x102, 0x0, 0x0, 0x10)
    OP_43(0x101, 0x0, 0x0, 0x11)
    OP_43(0xC, 0x0, 0x0, 0x12)
    Sleep(2000)
    OP_6D(-10900, 0, -27570, 1500)
    WaitChrThread(0x101, 0x0)

    ChrTalk(
        0x101,
        (
            "#509F#2P……喂，\x01",
            "为什么你这么自然而然就跟过来了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#025F而且刚才又在\x01",
            "绝妙的时机来向我们搭话……\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xC,
        "金发青年",
        (
            "#035F呵呵，被发现了。\x02\x03",
            "好像有什么有趣的事情，\x01",
            "所以我也想顺便参观一下嘛。\x02\x03",
            "#030F好了，你们不用介意我，\x01",
            "去和那个将军谈话就行了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1200)

    ChrTalk(
        0x101,
        "#005F#3S#2P肯定是要介意的呀！#2S\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_8F(0x101, 0xFFFFD44A, 0x0, 0xFFFF92A0, 0xBB8, 0x0)

    ChrTalk(
        0x101,
        "#009F#2P喂，你赶快回去吧！\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xC,
        "金发青年",
        "#034F小气。\x02",
    )

    CloseMessageWindow()
    OP_8C(0xC, 270, 400)
    OP_8E(0xC, 0xFFFFC568, 0x0, 0xFFFF93A4, 0x7D0, 0x0)
    OP_8E(0xC, 0xFFFFC5F4, 0x1F4, 0xFFFFA330, 0xBB8, 0x0)
    OP_72(0x0, 0x800)
    OP_22(0x7, 0x0, 0x64)
    OP_6F(0x0, 20)
    OP_70(0x0, 0x0)
    OP_73(0x0)
    OP_71(0x0, 0x800)
    SetChrFlags(0xC, 0x80)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#017F捉摸不透的人……\x01",
            "他到底来王国做什么呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F确实不是什么简单的人物。\x01",
            "该怎么说呢，从各种意义上都是吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    ChrTalk(
        0x101,
        (
            "#509F为了社会和人类，\x01",
            "这样的怪人我们还是置之不理的好！\x02\x03",
            "赶快去将军那里吧！\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_14_32E4 end

    def Function_15_3747(): pass

    label("Function_15_3747")

    OP_8E(0xFE, 0xFFFFC568, 0x0, 0xFFFF93A4, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFDD3C, 0x0, 0xFFFF91EC, 0xBB8, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_15_3747 end

    def Function_16_3777(): pass

    label("Function_16_3777")

    Sleep(1000)
    OP_8E(0xFE, 0xFFFFC568, 0x0, 0xFFFF93A4, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFD878, 0x0, 0xFFFF8F80, 0xBB8, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_16_3777 end

    def Function_17_37AC(): pass

    label("Function_17_37AC")

    Sleep(1800)
    OP_8E(0xFE, 0xFFFFC568, 0x0, 0xFFFF93A4, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFD7C4, 0x0, 0xFFFF9444, 0xBB8, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_17_37AC end

    def Function_18_37E1(): pass

    label("Function_18_37E1")

    Sleep(3000)
    OP_8E(0xFE, 0xFFFFC568, 0x0, 0xFFFF93A4, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFCE1E, 0x0, 0xFFFF9156, 0xBB8, 0x0)
    Return()

    # Function_18_37E1 end

    def Function_19_380F(): pass

    label("Function_19_380F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_39F5")
    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_4A(0x8, 255)

    def lambda_382C():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_382C)

    def lambda_383A():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_383A)

    def lambda_3848():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3848)

    def lambda_3856():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3856)
    OP_69(0x8, 0x3E8)
    OP_A2(0x311)

    ChrTalk(
        0x8,
        (
            "刚才听见你们的吵架声了，\x01",
            "和其它的旅行者发生了争执吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F其、其实也不是什么大事。\x02\x03",
            "话说回来……\x01",
            "我们可以和将军见面了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "啊，请进去吧。\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x4)
    OP_8E(0x8, 0x206C, 0x0, 0xFFFFD6FC, 0xBB8, 0x0)
    TurnDirection(0x8, 0x0, 400)
    ClearChrFlags(0x8, 0x4)

    ChrTalk(
        0x8,
        "将军的办公室在走廊尽头的左边。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "请记住不要\x01",
            "随便进入其它无关的场所。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 180, 400)
    OP_4B(0x8, 255)
    OP_71(0x1, 0x10)
    EventEnd(0x1)

    label("loc_39F5")

    Return()

    # Function_19_380F end

    def Function_20_39F6(): pass

    label("Function_20_39F6")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(6980, 0, -10700, 0)
    SetChrPos(0x101, 11000, 500, -11970, 0)
    SetChrPos(0x103, 11000, 500, -11970, 0)
    SetChrPos(0x102, 11000, 500, -11970, 0)
    SetChrPos(0xD, 11000, 500, -11970, 0)
    SetChrPos(0x8, 11000, 500, -11970, 0)
    SetChrPos(0x9, 11000, 500, -11970, 0)
    OP_4A(0xD, 255)
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x103, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x8, 0x40)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0xD, 0x40)
    SetChrChipByIndex(0x8, 5)
    SetChrChipByIndex(0x9, 5)
    Sleep(500)
    OP_70(0x1, 0x14)
    OP_73(0x1)
    Sleep(500)
    OP_43(0x101, 0x0, 0x0, 0x15)
    OP_43(0x103, 0x0, 0x0, 0x17)
    OP_43(0x102, 0x0, 0x0, 0x16)
    Sleep(1500)
    ClearChrFlags(0x9, 0x80)
    OP_43(0x9, 0x1, 0x0, 0x1B)
    Sleep(300)
    ClearChrFlags(0x8, 0x80)
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_3B11():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_3B11)
    OP_8E(0x8, 0x1F4A, 0x0, 0xFFFFD06C, 0xFA0, 0x0)
    OP_8E(0x8, 0x1BB2, 0x0, 0xFFFFD4A4, 0xFA0, 0x0)
    OP_8C(0x8, 270, 0)

    ChrTalk(
        0x101,
        (
            "#009F等、等等，干什么呀！\x01",
            "像撵狗似的对待我们！\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xD, 0x80)
    OP_9F(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_3BB3():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 3, lambda_3BB3)
    OP_8E(0xD, 0x1F4A, 0x0, 0xFFFFD06C, 0xBB8, 0x0)

    ChrTalk(
        0xD,
        (
            "#160F#2P哼，因为你们就只配如此。\x02\x03",
            "故意隐瞒身份姑且不提，\x01",
            "竟然还明目张胆骗取军情……\x02\x03",
            "敢做出这种不知廉耻的事，\x01",
            "看来游击士的信用也不过如此！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#005F说、说什么骗取！？\x02\x03",
            "要说起来，这都是你的错！\x01",
            "谁让你不把消息通告给游击士协会！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#162F#2P胡闹！这种事件怎么能让\x01",
            "充其量只算民间团体的组织负责！\x02\x03",
            "#163F真是的……\x01",
            "那个梅贝尔究竟怎么想的？\x02\x03",
            "雇佣这种小女孩儿，\x01",
            "只会给搜索行动带来麻烦……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x103,
        "#022F……请适可而止吧。\x02",
    )

    CloseMessageWindow()

    def lambda_3EA1():
        OP_6D(7800, 0, -10140, 1200)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_3EA1)
    SetChrChipByIndex(0x8, 0)
    SetChrChipByIndex(0x9, 0)

    def lambda_3EC3():

        label("loc_3EC3")

        TurnDirection(0xFE, 0x103, 400)
        OP_48()
        Jump("loc_3EC3")

    QueueWorkItem2(0x8, 2, lambda_3EC3)

    def lambda_3ED4():

        label("loc_3ED4")

        TurnDirection(0xFE, 0x103, 400)
        OP_48()
        Jump("loc_3ED4")

    QueueWorkItem2(0x9, 2, lambda_3ED4)
    OP_8E(0x103, 0x1838, 0x0, 0xFFFFD01C, 0xBB8, 0x0)
    OP_44(0x8, 0x2)
    OP_44(0x9, 0x2)
    Sleep(400)

    ChrTalk(
        0x103,
        (
            "#025F#6P将军有没有想过\x01",
            "我们特地从洛连特\x01",
            "赶过来这里的原因啊？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x103,
        (
            "#024F#6P#3S不就是因为你们这些当兵的！\x01",
            "在关键时刻完全不中用！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#161F#2P什、什什什什什么～！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007F（哇啊……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#017F（雪拉姐姐，发飙了……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#022F#6P最近这几个月，\x01",
            "柏斯地区接连发生由空贼引起的盗窃案件。\x01",
            "敢问将军知道吗？\x02\x03",
            "没有经过认真的搜查，\x01",
            "就把责任一股脑推给游击士协会……\x02\x03",
            "#026F发生了这样的大事，还摆出一幅\x01",
            "目中无人的态度和我们划清界限……\x02\x03",
            "而且，先别说人质了，\x01",
            "连定期船的行踪到现在都还没有查明。\x02\x03",
            "#027F难道你们不会感到羞耻吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xD,
        "#162F#2P#3S给我闭嘴，小丫头！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#162F#2P有组织纪律约束的军队\x01",
            "岂能像你们那样任意妄为？\x02\x03",
            "不考虑清楚就行动的结果，\x01",
            "只会是打草惊蛇让犯人逃掉。\x01",
            "你们不懂就不要逞一时意气地胡说！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#022F#6P说得可真是好听……\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x40)
    SetChrChipByIndex(0xC, 6)
    OP_9F(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xC, 0, 0, -5000, 135)
    OP_1F(0x46, 0x190)
    Sleep(400)
    OP_22(0xBE, 0x0, 0x64)
    Sleep(1000)

    NpcTalk(
        0xC,
        "青年的声音",
        "呼，多么令人悲哀呀。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0xD, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x8, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1200)
    OP_1F(0x64, 0x190)
    OP_4A(0xC, 255)
    SetChrChipByIndex(0xC, 6)
    OP_9F(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xC, 0xFF, 0xFF, 0xFF, 0xFF, 0x64)
    SetChrPos(0xC, 0, 0, -7024, 135)

    def lambda_44FB():
        OP_6D(3580, 0, -8410, 2000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_44FB)

    def lambda_4513():
        OP_6C(0, 2000)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_4513)

    def lambda_4523():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_4523)

    def lambda_4531():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4531)

    def lambda_453F():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_453F)
    Sleep(500)

    def lambda_4552():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4552)

    def lambda_4560():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4560)

    def lambda_456E():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_456E)
    Sleep(2000)

    ChrTalk(
        0xC,
        (
            "#035F争吵是不会有结果的……\x01",
            "只会使这片干涸的大地更为荒凉。\x02\x03",
            "#030F本人谨向在场诸位，献歌一首。\x02\x03",
            "一首能润泽心中的荒野，\x01",
            "让美丽的希望之花盛开，\x01",
            "温柔而忧伤的歌曲……\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0xD, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x101)
    OP_63(0x103)
    OP_63(0x102)
    OP_63(0xD)
    OP_63(0x8)
    OP_63(0x9)
    Sleep(500)
    OP_4B(0xC, 255)
    Sleep(1000)
    OP_1D(0x47)
    Sleep(1000)

    ChrTalk(
        0xC,
        "#70A#50W滑过天边#1500W　#50W星之轨迹……  \x05\x02",
    )

    Sleep(7000)

    ChrTalk(
        0xC,
        "#70A#50W仿如路标#1000W　#50W引导向你……\x05\x02",
    )

    Sleep(7000)

    ChrTalk(
        0xC,
        "#70A#50W急切的#1500W　#50W思念#1000W　#50W满溢胸怀……\x05\x02",
    )

    Sleep(7000)

    ChrTalk(
        0xC,
        "#70A#50W月亮也嘲笑#1000W　#50W这份痛苦……\x05\x02",
    )

    Sleep(7000)

    ChrTalk(
        0xC,
        "#70A#50W若无法实现#3000W　#50W这份空想……\x05\x02",
    )

    Sleep(7500)

    ChrTalk(
        0xC,
        "#70A#50W至少请留下#3000W　#50W一道浅伤……\x05\x02",
    )

    Sleep(7500)

    ChrTalk(
        0xC,
        "#70A#50W最初之吻#3000W　#50W最后之吻…… \x05\x02",
    )

    Sleep(7500)

    ChrTalk(
        0xC,
        "#70A#50W你的泪滴#3000W  #50W化作琥珀……\x05\x02",
    )

    Sleep(7500)

    ChrTalk(
        0xC,
        "#60A#50W这份爱意#3500W　#50W永远封存……\x05\x02",
    )

    OP_21()
    Sleep(500)
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0xD, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(2000)
    OP_4A(0xC, 255)
    Sleep(1000)
    Fade(250)
    SetChrFlags(0xC, 0x2)
    SetChrChipByIndex(0xC, 7)
    SetChrSubChip(0xC, 0)
    OP_0D()
    OP_99(0xC, 0x0, 0x3, 0x5DC)
    Sleep(300)
    OP_99(0xC, 0x3, 0xA, 0x3E8)
    Sleep(500)

    ChrTalk(
        0xC,
        (
            "#035F呵呵……\x01",
            "看来大家已经明白了我的意思。\x02\x03",
            "世上最宝贵最重要的东西……\x01",
            "是爱与和平。\x02\x03",
            "#030F以时下的话来说，就是Love ＆ Peace。\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x89, 0x0, 0x64)
    OP_62(0xC, 0x12C, 1900, 0x36, 0x39, 0xFA, 0x0)
    Sleep(1000)
    Sleep(500)

    ChrTalk(
        0xD,
        "#163F#2P咳、咳咳……\x02",
    )

    CloseMessageWindow()

    def lambda_4B22():
        OP_6D(6980, 0, -10700, 1500)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_4B22)

    def lambda_4B3A():
        OP_6C(45000, 1500)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_4B3A)
    Sleep(1500)
    OP_1D(0x10)
    ClearChrFlags(0xC, 0x2)
    SetChrChipByIndex(0xC, 2)
    TurnDirection(0xD, 0x9, 400)
    OP_63(0xC)

    ChrTalk(
        0xD,
        (
            "#160F#2P各地搜索部队的报告\x01",
            "差不多也都传来了吧？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4BC5():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4BC5)

    def lambda_4BD3():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4BD3)

    def lambda_4BE1():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4BE1)

    def lambda_4BEF():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4BEF)

    def lambda_4BFD():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4BFD)

    ChrTalk(
        0x9,
        (
            "是、是的。\x01",
            "正等候将军的批阅！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#160F#2P那我回去工作了。\x01",
            "记住，不要让那些人再进来。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xD, 90, 400)
    OP_8E(0xD, 0x2544, 0x1F4, 0xFFFFD148, 0x7D0, 0x0)
    Sleep(500)

    ChrTalk(
        0xD,
        (
            "#163F#6P还有就是……\x01",
            "解除钢壁之路的监察站。\x02\x03",
            "我不想再看到他们呆在这里，\x01",
            "简直是太碍眼了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P遵、遵命！\x02",
    )

    CloseMessageWindow()
    OP_43(0x9, 0x1, 0x0, 0x1C)
    OP_43(0x8, 0x1, 0x0, 0x1D)

    def lambda_4D64():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 3, lambda_4D64)
    OP_8E(0xD, 0x2AF8, 0x1F4, 0xFFFFD13E, 0x7D0, 0x0)
    SetChrFlags(0xD, 0x80)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#509F（啊！逃掉了……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#017F（不过心情可以理解呢……）\x02",
    )

    CloseMessageWindow()

    def lambda_4DFB():
        OP_6D(4140, 0, -10880, 2000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_4DFB)

    def lambda_4E13():
        OP_6C(0, 2000)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_4E13)
    OP_8E(0xC, 0x960, 0x0, 0xFFFFD940, 0x7D0, 0x0)
    OP_8C(0xC, 135, 400)
    Sleep(500)

    ChrTalk(
        0xC,
        (
            "#031F呵呵，无论哪个国家，\x01",
            "军人都是一样不解风情呢。\x02\x03",
            "哈·哈·哈。\x01",
            "还是在场的你们几位更有眼光啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1200)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#506F#5P那、那么，\x01",
            "我们也该回去了吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x102, 45, 400)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#019F#6P是、是啊。\x02\x03",
            "虽然惹了些麻烦，\x01",
            "不过大致上还是得到了情报……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x102, 400)

    ChrTalk(
        0x103,
        (
            "#021F我们回到柏斯\x01",
            "再制定今后的对策吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x101, 0x0, 0x0, 0x18)
    OP_43(0x103, 0x0, 0x0, 0x1A)
    OP_43(0x102, 0x0, 0x0, 0x19)
    Sleep(1000)
    OP_62(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_8C(0xC, 180, 400)

    ChrTalk(
        0xC,
        (
            "#033F哎呀……\x02\x03",
            "等等，你们几位。\x01",
            "你们刚才说要去哪里来着？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)
    OP_90(0xC, 0x0, 0x0, 0xFFFFF448, 0xFA0, 0x0)

    ChrTalk(
        0xC,
        (
            "#036F#5P等、等一下！\x01",
            "不不，无论如何请稍等我一下啦！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5111():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFE4A8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_5111)
    FadeToDark(2000, 0, -1)
    OP_0D()
    ClearMapFlags(0x400000)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T1410   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_20_39F6 end

    def Function_21_5143(): pass

    label("Function_21_5143")

    Sleep(600)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    ClearChrFlags(0xFE, 0x80)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_5170():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_5170)
    OP_8E(0xFE, 0x1464, 0x0, 0xFFFFD314, 0x1770, 0x0)
    TurnDirection(0xFE, 0xD, 400)
    Return()

    # Function_21_5143 end

    def Function_22_5198(): pass

    label("Function_22_5198")

    Sleep(300)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    ClearChrFlags(0xFE, 0x80)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_51C5():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_51C5)
    OP_8E(0xFE, 0x125C, 0x0, 0xFFFFCD9C, 0x1770, 0x0)
    TurnDirection(0xFE, 0xD, 400)
    Return()

    # Function_22_5198 end

    def Function_23_51ED(): pass

    label("Function_23_51ED")

    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    ClearChrFlags(0xFE, 0x80)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_5215():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_5215)
    OP_8E(0xFE, 0xEE2, 0x0, 0xFFFFD04E, 0x1770, 0x0)
    TurnDirection(0xFE, 0xD, 400)
    Return()

    # Function_23_51ED end

    def Function_24_523D(): pass

    label("Function_24_523D")

    Sleep(500)
    Sleep(500)
    OP_8C(0xFE, 180, 400)
    OP_90(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0xBB8, 0x0)
    Return()

    # Function_24_523D end

    def Function_25_5263(): pass

    label("Function_25_5263")

    OP_8C(0xFE, 180, 400)
    OP_90(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0xBB8, 0x0)
    Return()

    # Function_25_5263 end

    def Function_26_527F(): pass

    label("Function_26_527F")

    Sleep(500)
    OP_8C(0xFE, 180, 400)
    OP_90(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0xBB8, 0x0)
    Return()

    # Function_26_527F end

    def Function_27_52A0(): pass

    label("Function_27_52A0")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_52B1():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_52B1)
    OP_8E(0xFE, 0x1F4A, 0x0, 0xFFFFD06C, 0xFA0, 0x0)
    OP_8E(0xFE, 0x1C0C, 0x0, 0xFFFFCBD0, 0xFA0, 0x0)
    OP_8C(0xFE, 270, 0)
    Return()

    # Function_27_52A0 end

    def Function_28_52ED(): pass

    label("Function_28_52ED")

    Sleep(500)
    OP_8E(0xFE, 0x1F4A, 0x0, 0xFFFFD06C, 0xFA0, 0x0)
    OP_8E(0xFE, 0x244A, 0x1F4, 0xFFFFD0EE, 0xFA0, 0x0)

    def lambda_5320():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_5320)
    OP_8E(0xFE, 0x2AF8, 0x1F4, 0xFFFFD13E, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Sleep(500)
    OP_72(0x1, 0x800)
    OP_22(0xE6, 0x0, 0x64)
    OP_6F(0x1, 20)
    OP_70(0x1, 0x0)
    OP_71(0x1, 0x800)
    Return()

    # Function_28_52ED end

    def Function_29_5368(): pass

    label("Function_29_5368")

    Sleep(3000)
    OP_8E(0xFE, 0x203A, 0x0, 0xFFFFD120, 0xBB8, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_29_5368 end

    def Function_30_5389(): pass

    label("Function_30_5389")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_54E8")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5451")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_53B5")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_53BC")

    label("loc_53B5")

    TurnDirection(0x103, 0x0, 400)

    label("loc_53BC")


    def lambda_53C2():
        TurnDirection(0x101, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_53C2)
    TurnDirection(0x102, 0x103, 400)

    ChrTalk(
        0x103,
        (
            "#020F在将军回来之前，\x01",
            "我们还是不要随便乱走了。\x02\x03",
            "就在酒馆里一边等一边休息一下吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_54CD")

    label("loc_5451")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5467")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_546E")

    label("loc_5467")

    TurnDirection(0x103, 0x0, 400)

    label("loc_546E")


    def lambda_5474():
        TurnDirection(0x101, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5474)
    TurnDirection(0x102, 0x103, 400)

    ChrTalk(
        0x103,
        (
            "#020F别到处乱走了。\x01",
            "赶快去和将军会面吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_54CD")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_54E8")

    Return()

    # Function_30_5389 end

    SaveToFile()

Try(main)
