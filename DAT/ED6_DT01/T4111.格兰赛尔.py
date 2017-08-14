from ED6ScenarioHelper import *

def main():
    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4111   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4111.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60014",
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
        '赫穆特',                               # 9
        '诺琪',                                 # 10
        '马丁',                                 # 11
        '玛丽安',                               # 12
        '海伦娜',                               # 13
        '卡特莉娜夫人',                         # 14
        '达丽娅',                               # 15
        '莉安妮',                               # 16
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
        'ED6_DT07/CH01220 ._CH',             # 00
        'ED6_DT07/CH01230 ._CH',             # 01
        'ED6_DT07/CH01020 ._CH',             # 02
        'ED6_DT07/CH01210 ._CH',             # 03
        'ED6_DT07/CH02490 ._CH',             # 04
        'ED6_DT07/CH01180 ._CH',             # 05
        'ED6_DT07/CH01350 ._CH',             # 06
        'ED6_DT07/CH01480 ._CH',             # 07
        'ED6_DT07/CH01023 ._CH',             # 08
    )

    AddCharChipPat(
        'ED6_DT07/CH01220P._CP',             # 00
        'ED6_DT07/CH01230P._CP',             # 01
        'ED6_DT07/CH01020P._CP',             # 02
        'ED6_DT07/CH01210P._CP',             # 03
        'ED6_DT07/CH02490P._CP',             # 04
        'ED6_DT07/CH01180P._CP',             # 05
        'ED6_DT07/CH01350P._CP',             # 06
        'ED6_DT07/CH01480P._CP',             # 07
        'ED6_DT07/CH01023P._CP',             # 08
    )

    DeclNpc(
        X                   = 60450,
        Z                   = 0,
        Y                   = 62340,
        Direction           = 10,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 60030,
        Z                   = 0,
        Y                   = 1650,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 6600,
        Z                   = 0,
        Y                   = -55590,
        Direction           = 83,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = -4760,
        Z                   = 0,
        Y                   = 1910,
        Direction           = 150,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 8,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = -2300,
        Z                   = 0,
        Y                   = 61070,
        Direction           = 87,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 9,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )


    ScpFunction(
        "Function_0_1F2",          # 00, 0
        "Function_1_70C",          # 01, 1
        "Function_2_759",          # 02, 2
        "Function_3_76F",          # 03, 3
        "Function_4_793",          # 04, 4
        "Function_5_7B7",          # 05, 5
        "Function_6_7DB",          # 06, 6
        "Function_7_7FF",          # 07, 7
        "Function_8_823",          # 08, 8
        "Function_9_847",          # 09, 9
        "Function_10_86B",         # 0A, 10
        "Function_11_D3A",         # 0B, 11
        "Function_12_1426",        # 0C, 12
        "Function_13_2153",        # 0D, 13
        "Function_14_29DD",        # 0E, 14
        "Function_15_307C",        # 0F, 15
        "Function_16_37BE",        # 10, 16
        "Function_17_3EF9",        # 11, 17
    )


    def Function_0_1F2(): pass

    label("Function_0_1F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_223")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 60480, 0, 62200, 17)
    SetChrPos(0xD, -3010, 0, -54540, 0)
    Jump("loc_70B")

    label("loc_223")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_2D2")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 59640, 0, 2040, 163)
    OP_43(0x8, 0x0, 0x0, 0x3)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 60480, 0, 62200, 17)
    SetChrChipByIndex(0xA, 8)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 122730, 250, 64200, 278)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xA, 0x4)
    OP_44(0xA, 0xFF)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 123540, 0, 68800, 3)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 113680, 0, -55940, 266)
    OP_43(0xC, 0x0, 0x0, 0x7)
    SetChrFlags(0xF, 0x80)
    SetChrPos(0xD, -3010, 0, -54540, 0)
    Jump("loc_70B")

    label("loc_2D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_347")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 115780, 0, 61020, 228)
    OP_43(0xA, 0x0, 0x0, 0x5)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 123540, 0, 68800, 3)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 113680, 0, -55940, 266)
    OP_43(0xC, 0x0, 0x0, 0x7)
    SetChrPos(0xD, -3010, 0, -54540, 0)
    SetChrFlags(0xF, 0x80)
    Jump("loc_70B")

    label("loc_347")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_3C6")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 115920, 0, 69500, 343)
    SetChrFlags(0xA, 0x10)
    TurnDirection(0xB, 0xA, 0)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 123540, 0, 68800, 3)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 113680, 0, -55940, 266)
    OP_43(0xC, 0x0, 0x0, 0x7)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrPos(0xD, -3010, 0, -54540, 0)
    Jump("loc_70B")

    label("loc_3C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_44F")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 58250, 0, 60130, 270)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 115780, 0, 61020, 228)
    OP_43(0xA, 0x0, 0x0, 0x6)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 126360, 0, 1830, 270)
    SetChrFlags(0xB, 0x10)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x10)
    SetChrPos(0xC, 126360, 0, 740, 270)
    SetChrPos(0xD, -3010, 0, -54540, 0)
    SetChrFlags(0xF, 0x80)
    Jump("loc_70B")

    label("loc_44F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_4BF")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 115780, 0, 61020, 228)
    OP_43(0xA, 0x0, 0x0, 0x5)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 121030, 0, -58010, 90)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 116840, 0, -55210, 90)
    OP_43(0xC, 0x0, 0x0, 0x7)
    SetChrPos(0xD, -3010, 0, -54540, 0)
    Jump("loc_70B")

    label("loc_4BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_537")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 123980, 0, 1080, 90)
    OP_43(0xA, 0x0, 0x0, 0x2)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 126360, 0, 1830, 270)
    SetChrFlags(0xB, 0x10)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x10)
    SetChrPos(0xC, 126360, 0, 740, 270)
    SetChrPos(0xD, -960, 0, -55790, 0)
    Jump("loc_70B")

    label("loc_537")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_59B")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 115780, 0, 61020, 228)
    OP_43(0xA, 0x0, 0x0, 0x5)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 123540, 0, 68800, 3)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 113680, 0, -55940, 266)
    OP_43(0xC, 0x0, 0x0, 0x7)
    Jump("loc_70B")

    label("loc_59B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_613")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 123980, 0, 1080, 90)
    OP_43(0xA, 0x0, 0x0, 0x2)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 126360, 0, 1830, 270)
    SetChrFlags(0xB, 0x10)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x10)
    SetChrPos(0xC, 126360, 0, 740, 270)
    SetChrPos(0xD, 2380, 0, -55230, 0)
    Jump("loc_70B")

    label("loc_613")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_699")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0xA, 8)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 122730, 250, 64200, 278)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xA, 0x4)
    OP_44(0xA, 0xFF)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 113680, 0, -55940, 266)
    OP_43(0xB, 0x0, 0x0, 0x7)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x10)
    SetChrPos(0xC, 115850, 0, 60880, 45)
    SetChrPos(0xD, -960, 0, -55790, 0)
    Jump("loc_70B")

    label("loc_699")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_70B")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 115780, 0, 61020, 228)
    OP_43(0xA, 0x0, 0x0, 0x5)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 123540, 0, 68800, 3)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 113680, 0, -55940, 266)
    OP_43(0xC, 0x0, 0x0, 0x7)
    SetChrPos(0xD, 6320, 0, -55580, 91)

    label("loc_70B")

    Return()

    # Function_0_1F2 end

    def Function_1_70C(): pass

    label("Function_1_70C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_73F")
    OP_B1("t4111_y")
    Jump("loc_748")

    label("loc_73F")

    OP_B1("t4111_n")

    label("loc_748")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 2)), scpexpr(EXPR_END)), "loc_758")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x4B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_758")

    Return()

    # Function_1_70C end

    def Function_2_759(): pass

    label("Function_2_759")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_76E")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_759")

    label("loc_76E")

    Return()

    # Function_2_759 end

    def Function_3_76F(): pass

    label("Function_3_76F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_792")
    OP_8D(0xFE, 59200, 2620, 64319, 1410, 2500)
    Jump("Function_3_76F")

    label("loc_792")

    Return()

    # Function_3_76F end

    def Function_4_793(): pass

    label("Function_4_793")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7B6")
    OP_8D(0xFE, 56200, 3180, 64330, 1570, 2500)
    Jump("Function_4_793")

    label("loc_7B6")

    Return()

    # Function_4_793 end

    def Function_5_7B7(): pass

    label("Function_5_7B7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7DA")
    OP_8D(0xFE, 113710, 62230, 117600, 58990, 3000)
    Jump("Function_5_7B7")

    label("loc_7DA")

    Return()

    # Function_5_7B7 end

    def Function_6_7DB(): pass

    label("Function_6_7DB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7FE")
    OP_8D(0xFE, 113710, 62230, 117600, 58990, 6000)
    Jump("Function_6_7DB")

    label("loc_7FE")

    Return()

    # Function_6_7DB end

    def Function_7_7FF(): pass

    label("Function_7_7FF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_822")
    OP_8D(0xFE, 113410, -55340, 116360, -56940, 3000)
    Jump("Function_7_7FF")

    label("loc_822")

    Return()

    # Function_7_7FF end

    def Function_8_823(): pass

    label("Function_8_823")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_846")
    OP_8D(0xFE, -6280, 2250, 4250, -530, 3000)
    Jump("Function_8_823")

    label("loc_846")

    Return()

    # Function_8_823 end

    def Function_9_847(): pass

    label("Function_9_847")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_86A")
    OP_8D(0xFE, -4570, 58630, -30, 63950, 3000)
    Jump("Function_9_847")

    label("loc_86A")

    Return()

    # Function_9_847 end

    def Function_10_86B(): pass

    label("Function_10_86B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_8C2")
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        (
            "啊，\x01",
            "游击士艾丝蒂尔姐姐！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "这次一定要陪莉安妮玩嘛。\x02",
    )

    CloseMessageWindow()
    Jump("loc_D36")

    label("loc_8C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_8CC")
    Jump("loc_D36")

    label("loc_8CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_8D6")
    Jump("loc_D36")

    label("loc_8D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_8E0")
    Jump("loc_D36")

    label("loc_8E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_981")

    ChrTalk(
        0xFE,
        (
            "今年爷爷他\x01",
            "没有参加比赛……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "真是无聊，\x01",
            "还是去外面玩吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D36")

    label("loc_981")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_9C9")

    ChrTalk(
        0xFE,
        (
            "奶奶好像\x01",
            "没有什么精神呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "她不要紧吧……\x02",
    )

    CloseMessageWindow()
    Jump("loc_D36")

    label("loc_9C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_A52")

    ChrTalk(
        0xFE,
        (
            "庆典开始了的话，\x01",
            "就能见到大家了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "想见见爷爷，\x01",
            "还有公主殿下呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D36")

    label("loc_A52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_B5D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_AD7")

    ChrTalk(
        0xFE,
        (
            "好久没有这样\x01",
            "和奶奶一起去王城里了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，\x01",
            "还是没能见到公主殿下。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B5A")

    label("loc_AD7")

    OP_A2(0x7)

    ChrTalk(
        0xFE,
        (
            "好久没有这样\x01",
            "和奶奶一起去王城里了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，\x01",
            "还是没能见到公主殿下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "呜呜……\x02",
    )

    CloseMessageWindow()

    label("loc_B5A")

    Jump("loc_D36")

    label("loc_B5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_BA5")

    ChrTalk(
        0xFE,
        (
            "我莉安妮啊，\x01",
            "和公主可是好朋友哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "是真的哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_D36")

    label("loc_BA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_C02")

    ChrTalk(
        0xFE,
        "呜……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "爷爷他\x01",
            "不知什么时候\x01",
            "才能回来啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D36")

    label("loc_C02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_D36")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_C95")

    ChrTalk(
        0xFE,
        (
            "哇～\x01",
            "爷爷很快就要回来了呢！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "快点回来吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_D36")

    label("loc_C95")

    OP_A2(0x7)

    ChrTalk(
        0xFE,
        (
            "哇～\x01",
            "爷爷很快就要回来了呢！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xF, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "快点回来吧。\x02",
    )

    CloseMessageWindow()

    label("loc_D36")

    TalkEnd(0xFE)
    Return()

    # Function_10_86B end

    def Function_11_D3A(): pass

    label("Function_11_D3A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_DD0")

    ChrTalk(
        0xFE,
        (
            "理查德先生\x01",
            "曾经几次到这里来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "连我家老爷都\x01",
            "称赞过他，\x01",
            "真是个了不起的人呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1422")

    label("loc_DD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_E14")

    ChrTalk(
        0xFE,
        (
            "莉安妮小姐\x01",
            "好像已经被找到了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "太好了～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1422")

    label("loc_E14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_E84")

    ChrTalk(
        0xFE,
        (
            "夫人已经委托\x01",
            "王国军去搜寻\x01",
            "莉安妮小姐的下落了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "但还没有什么消息呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1422")

    label("loc_E84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_E8E")
    Jump("loc_1422")

    label("loc_E8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_F1F")

    ChrTalk(
        0xFE,
        (
            "老爷怎么不和我们联络呢，\x01",
            "真有点奇怪啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "希望没出什么事就好了……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1422")

    label("loc_F1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_FED")

    ChrTalk(
        0xFE,
        (
            "夫人还有莉安妮小姐\x01",
            "都很期待诞辰庆典的到来，\x01",
            "因为只有那个时候老爷才会回来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "只要能够回来，\x01",
            "哪怕只是呆上一会儿也好啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1422")

    label("loc_FED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_10B1")

    ChrTalk(
        0xFE,
        (
            "每年诞辰庆典\x01",
            "老爷他都会受到女王陛下的招待。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "自从战争结束之后，\x01",
            "每年的这个时候\x01",
            "他都一定会回来……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1422")

    label("loc_10B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_11B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1122")

    ChrTalk(
        0xFE,
        (
            "我在这悄悄告诉你，\x01",
            "就算是老爷也\x01",
            "不敢惹夫人生气呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11B6")

    label("loc_1122")

    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "老爷他发起脾气\x01",
            "是很可怕的呢～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "不过，我在这里悄悄告诉你……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "就算是这样的老爷，\x01",
            "也不敢惹夫人呢，呵呵。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11B6")

    Jump("loc_1422")

    label("loc_11B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_133D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1251")

    ChrTalk(
        0xFE,
        (
            "我在百日战役时\x01",
            "失去了双亲。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "当时，老爷和夫人\x01",
            "收养了无依无靠的我，\x01",
            "让我在这里生活。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_133A")

    label("loc_1251")

    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "我在百日战役时\x01",
            "失去了双亲。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "当时，老爷和夫人\x01",
            "收养了无依无靠的我……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "现在还让我\x01",
            "在这个家里当保姆。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我真是太感谢他们两位了。\x02",
    )

    CloseMessageWindow()

    label("loc_133A")

    Jump("loc_1422")

    label("loc_133D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_13E3")

    ChrTalk(
        0xFE,
        (
            "诞辰庆典就要到了，\x01",
            "我本以为老爷肯定\x01",
            "就要回来了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "难道最近工作就\x01",
            "那么的繁忙吗～？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1422")

    label("loc_13E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1422")

    ChrTalk(
        0xFE,
        (
            "在老爷回来之前\x01",
            "得进行大扫除才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1422")

    TalkEnd(0xFE)
    Return()

    # Function_11_D3A end

    def Function_12_1426(): pass

    label("Function_12_1426")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_16B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1523")

    ChrTalk(
        0xFE,
        (
            "他曾经是真心为利贝尔着想的\x01",
            "军人之一啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "一定是因为这种想法太强烈，\x01",
            "才导致采取了这次行动的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16B0")

    label("loc_1523")

    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "那位理查德先生\x01",
            "竟然发起了政变……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他曾经是真心为利贝尔着想的\x01",
            "军人之一啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "一定是因为这种想法太强烈，\x01",
            "才导致采取了这次行动的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我是这么认为的……\x02",
    )

    CloseMessageWindow()

    label("loc_16B0")

    Jump("loc_214F")

    label("loc_16B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_18D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1796")

    ChrTalk(
        0xFE,
        (
            "就在刚才，\x01",
            "收到了游击士协会\x01",
            "一位叫艾南的先生的联络。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他说在艾贝尔离宫\x01",
            "找到了莉安妮。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "真是太好了……\x02",
    )

    CloseMessageWindow()
    Jump("loc_18D6")

    label("loc_1796")

    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "就在刚才，\x01",
            "收到了游击士协会\x01",
            "一位叫艾南的先生的联络。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他说在艾贝尔离宫\x01",
            "找到了莉安妮。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "真是太好了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果有什么意外的话，\x01",
            "我真是无颜面对\x01",
            "那孩子的父母……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18D6")

    Jump("loc_214F")

    label("loc_18D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_1A8D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_195E")

    ChrTalk(
        0xFE,
        (
            "身为他的妻子，\x01",
            "又是莉安妮的祖母，\x01",
            "我必须坚强……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A8A")

    label("loc_195E")

    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "……我孙女莉安妮\x01",
            "昨天傍晚出去以后一直未归。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "而且和我丈夫\x01",
            "也一直联系不上……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我该怎么办啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，身为他的妻子，\x01",
            "又是莉安妮的祖母，\x01",
            "我必须坚强……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A8A")

    Jump("loc_214F")

    label("loc_1A8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_1AD0")

    ChrTalk(
        0xFE,
        (
            "唉，\x01",
            "莉安妮跑到哪里去玩了呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_214F")

    label("loc_1AD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1BAE")

    ChrTalk(
        0xFE,
        (
            "女王陛下卧病在床也好，\x01",
            "丈夫失去音信也好……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "怎么总是发生\x01",
            "这些不好的事情啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_214F")

    label("loc_1BAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_1D0B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1C32")

    ChrTalk(
        0xFE,
        (
            "我和驻扎在哈肯大门的\x01",
            "丈夫怎么也联络不上。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "到底是\x01",
            "发生了什么事……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D08")

    label("loc_1C32")

    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "我和驻扎在柏斯哈肯大门的\x01",
            "丈夫怎么也联络不上。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这种事情自从战争结束后，\x01",
            "还从来没有发生过呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "到底是\x01",
            "发生了什么事啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D08")

    Jump("loc_214F")

    label("loc_1D0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_1DD6")

    ChrTalk(
        0xFE,
        (
            "不要说武术大会，\x01",
            "丈夫他连诞辰庆典\x01",
            "好像都不能回来参加……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "今天再联系一下他，\x01",
            "问问情况吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_214F")

    label("loc_1DD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1F8C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1E73")

    ChrTalk(
        0xFE,
        (
            "以前去看望陛下的时候\x01",
            "从来没有被拒绝过啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "好担心啊……\x01",
            "恐怕病得很重吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F89")

    label("loc_1E73")

    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "今天本想去看望女王陛下的，\x01",
            "可是到了那里，\x01",
            "却被拒绝进城。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然女王陛下\x01",
            "以前也曾经\x01",
            "生过几次病……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但还从来没有\x01",
            "不让人去探望的情况。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "好担心啊……\x01",
            "恐怕病得很重吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F89")

    Jump("loc_214F")

    label("loc_1F8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_2020")

    ChrTalk(
        0xFE,
        (
            "我今天打算到王城里面\x01",
            "去看望女王陛下，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "早点把其他的事情办完吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_214F")

    label("loc_2020")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_20C8")

    ChrTalk(
        0xFE,
        (
            "他今年\x01",
            "没有参加武术大会，\x01",
            "是怎么回事呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "会不会是\x01",
            "出什么事了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_214F")

    label("loc_20C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_214F")

    ChrTalk(
        0xFE,
        "哎呀呀，欢迎。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我现在正在为\x01",
            "孙女炖牛肉汤呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_214F")

    TalkEnd(0xFE)
    Return()

    # Function_12_1426 end

    def Function_13_2153(): pass

    label("Function_13_2153")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_2160")
    Jump("loc_29D9")

    label("loc_2160")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_2176")

    ChrTalk(
        0xFE,
        "唉…………\x02",
    )

    CloseMessageWindow()
    Jump("loc_29D9")

    label("loc_2176")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_221E")

    ChrTalk(
        0xFE,
        (
            "呼，这样下去的话，\x01",
            "诞辰庆典到底会怎么样啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这可是难得遇到的盛大活动，\x01",
            "一定要举办才行啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29D9")

    label("loc_221E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_2296")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_225B")

    ChrTalk(
        0xFE,
        (
            "哈～哈～哈，\x01",
            "夕阳无限好啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2293")

    label("loc_225B")

    OP_A2(0x2)

    ChrTalk(
        0xFE,
        "………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哈～哈～哈，\x01",
            "夕阳无限好啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2293")

    Jump("loc_29D9")

    label("loc_2296")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_23CC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_232B")

    ChrTalk(
        0xFE,
        (
            "说起来，\x01",
            "为什么没有一个人叫我起床呢！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "真是过分。\x02",
    )

    CloseMessageWindow()
    Jump("loc_23C9")

    label("loc_232B")

    OP_A2(0x2)

    ChrTalk(
        0xFE,
        "这是怎么回事。\x02",
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "今天是武术大会的决赛日，\x01",
            "我怎么会睡过头了啊！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23C9")

    Jump("loc_29D9")

    label("loc_23CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_259B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2473")

    ChrTalk(
        0xFE,
        (
            "我猜想十有八九\x01",
            "特务部队会取得优胜。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哈～哈～哈，\x01",
            "很期待明天的比赛啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2598")

    label("loc_2473")

    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "哈～哈～哈，\x01",
            "明天终于到决赛了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我猜想十有八九\x01",
            "特务部队会取得优胜。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#009F（哼……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "明天要鼓足干劲，\x01",
            "九点准时在门口集合。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哈～哈～哈，\x01",
            "这就去通知她们。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2598")

    Jump("loc_29D9")

    label("loc_259B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_260A")

    ChrTalk(
        0xFE,
        (
            "哈～哈～哈，\x01",
            "全员都到齐了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "那么，现在开始点名了哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_29D9")

    label("loc_260A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_26D8")

    ChrTalk(
        0xFE,
        (
            "哎呀，\x01",
            "我可是为比赛捏了一把汗啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "明天早晨十点\x01",
            "全员依旧要在门口集合。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哈～哈～哈，\x01",
            "这就去通知她们。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29D9")

    label("loc_26D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_2726")

    ChrTalk(
        0xFE,
        "好～的，全员集合了吗～？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那么，\x01",
            "现在说明一下今天的任务～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29D9")

    label("loc_2726")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_293C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_27BD")

    ChrTalk(
        0xFE,
        (
            "早晨１０点\x01",
            "在门口集合。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "接着大家散步\x01",
            "到竞技场去。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2939")

    label("loc_27BD")

    OP_A2(0x2)

    ChrTalk(
        0xFE,
        "唔～……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "早晨１０点\x01",
            "在门口集合。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "然后到咖啡馆\x01",
            "去吃点东西……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "接着大家散步\x01",
            "到竞技场去。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "好，明天全体家族成员\x01",
            "外出观看武术大会～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2939")

    Jump("loc_29D9")

    label("loc_293C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_29D9")

    ChrTalk(
        0xFE,
        (
            "哈～哈～哈，\x01",
            "武术大会终于要开始了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "毫无疑问，\x01",
            "像这种盛大的活动，\x01",
            "一定要家族全员全部参与才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29D9")

    TalkEnd(0xFE)
    Return()

    # Function_13_2153 end

    def Function_14_29DD(): pass

    label("Function_14_29DD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_29EA")
    Jump("loc_3078")

    label("loc_29EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_2A68")

    ChrTalk(
        0xFE,
        "街上的气氛很怪异。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "平常的那些士兵不见了，\x01",
            "黑衣士兵却增加了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3078")

    label("loc_2A68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_2AEF")

    ChrTalk(
        0xFE,
        (
            "我那老公啊，为了这次诞辰庆典，\x01",
            "简直急得上气不接下气了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3078")

    label("loc_2AEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_2B61")

    ChrTalk(
        0xFE,
        (
            "我丈夫在比赛后\x01",
            "就连饭也不吃了，\x01",
            "一直那个样子……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3078")

    label("loc_2B61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_2C1A")

    ChrTalk(
        0xFE,
        (
            "总是那么慌慌张张的，\x01",
            "就不能稍稍冷静一点吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "冷静一下又不会惹到谁。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3078")

    label("loc_2C1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_2CD7")

    ChrTalk(
        0xFE,
        (
            "他那么旺盛的精力\x01",
            "到底是从哪里来的啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "从我们认识开始\x01",
            "他就一直是那个样子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "本来以为年纪大了\x01",
            "他能够安分点呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3078")

    label("loc_2CD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_2D3F")

    ChrTalk(
        0xFE,
        (
            "最难办的是，\x01",
            "越是在这种时候\x01",
            "老公的干劲越足。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3078")

    label("loc_2D3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2DB0")

    ChrTalk(
        0xFE,
        (
            "嗯，\x01",
            "今天女儿也很累了，\x01",
            "我去帮她做晚饭。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3078")

    label("loc_2DB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_2E12")

    ChrTalk(
        0xFE,
        "我那老公啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "一旦起床了，\x01",
            "就要开始搞活动了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3078")

    label("loc_2E12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_2FC7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2ED4")

    ChrTalk(
        0xFE,
        (
            "诺琪和她丈夫\x01",
            "现在关系处得怎么样呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在柏斯旅行时常常\x01",
            "可以听到她的感叹。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FC4")

    label("loc_2ED4")

    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "诺琪和她丈夫\x01",
            "现在关系处得怎么样呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在柏斯旅行时常常\x01",
            "可以听到她的感叹。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "好像是考虑了许多事情。\x02",
    )

    CloseMessageWindow()

    label("loc_2FC4")

    Jump("loc_3078")

    label("loc_2FC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_3078")

    ChrTalk(
        0xFE,
        (
            "我那老公啊，\x01",
            "就是喜欢搞些活动。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "武术大会和诞辰庆典就要到了，\x01",
            "肯定又要热闹过头的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3078")

    TalkEnd(0xFE)
    Return()

    # Function_14_29DD end

    def Function_15_307C(): pass

    label("Function_15_307C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_3089")
    Jump("loc_37BA")

    label("loc_3089")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_317A")

    ChrTalk(
        0xFE,
        (
            "如果诞辰庆典不能举行，\x01",
            "那爸爸的情绪就会一直低落下去的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "就这么一言不发，\x01",
            "会让人很担心的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "因为我也是这种容易受挫的性格。\x02",
    )

    CloseMessageWindow()
    Jump("loc_37BA")

    label("loc_317A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_31BE")

    ChrTalk(
        0xFE,
        (
            "我家也总算能够\x01",
            "消停一阵子了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37BA")

    label("loc_31BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_32EE")

    ChrTalk(
        0xFE,
        (
            "决胜赛时爸爸\x01",
            "支持的队伍输了，\x01",
            "所以我要做点好吃的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "为了安慰爸爸。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……真是的，\x01",
            "总是给人家添些麻烦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37BA")

    label("loc_32EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_339C")

    ChrTalk(
        0xFE,
        (
            "原本我偷偷地\x01",
            "把爸爸的闹钟里的\x01",
            "导力器取出来了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "唉，结果他还是起来了……\x02",
    )

    CloseMessageWindow()
    Jump("loc_37BA")

    label("loc_339C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_344C")

    ChrTalk(
        0xFE,
        (
            "呼，连续三天\x01",
            "陪老爸看武术大会，累死人了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "武术大会什么的\x01",
            "只要知道个结果不就行了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37BA")

    label("loc_344C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_3522")

    ChrTalk(
        0xFE,
        (
            "明明是１０点集合，\x01",
            "９点前就在大门口\x01",
            "转来转去的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "爸爸为什么\x01",
            "总是那么紧张呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37BA")

    label("loc_3522")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_35D0")

    ChrTalk(
        0xFE,
        (
            "唉～我的爸爸呀，\x01",
            "如果我和妈妈说不去的话，\x01",
            "就会立刻发脾气。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "作女儿的也真是辛苦啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_37BA")

    label("loc_35D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_3707")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_3656")

    ChrTalk(
        0xFE,
        (
            "我的爸爸呀，\x01",
            "总是容易兴奋过头。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那样高度紧张，\x01",
            "会导致心脏病爆发的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3704")

    label("loc_3656")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "全员……\x01",
            "不是只有三人吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我的爸爸呀，\x01",
            "总是容易兴奋过头。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那样高度紧张，\x01",
            "会导致心脏病爆发的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3704")

    Jump("loc_37BA")

    label("loc_3707")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_373E")

    ChrTalk(
        0xFE,
        (
            "呼，\x01",
            "今年又到这个时期了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37BA")

    label("loc_373E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_37BA")

    ChrTalk(
        0xFE,
        "嗯～这么多东西啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "家里做饭的工作\x01",
            "是由我和妈妈轮流担当的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37BA")

    TalkEnd(0xFE)
    Return()

    # Function_15_307C end

    def Function_16_37BE(): pass

    label("Function_16_37BE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_3982")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_389A")

    ChrTalk(
        0xFE,
        (
            "我这次终于\x01",
            "顺利地通过『钓公师团』的\x01",
            "入团测试了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我丈夫又开始上班了，\x01",
            "我可以趁这段时间\x01",
            "努力缩小和他技术上的差距。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_397F")

    label("loc_389A")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        "哦～呵呵呵呵呵！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我这次终于\x01",
            "顺利地通过『钓公师团』的\x01",
            "入团测试了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我丈夫又开始上班了，\x01",
            "我可以趁这段时间\x01",
            "努力缩小和他技术上的差距。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_397F")

    Jump("loc_3EF5")

    label("loc_3982")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_3AEF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_39F3")

    ChrTalk(
        0xFE,
        (
            "现在我也把对家的热情\x01",
            "转移到钓鱼上面了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "这样一来，就会感到快乐了啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3AEC")

    label("loc_39F3")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        "哦～呵呵呵呵呵！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "老公只对钓鱼感兴趣，\x01",
            "所以现在我也把对家的热情\x01",
            "转移到钓鱼上面了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这样一来，\x01",
            "就会感到快乐了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不知不觉就可以\x01",
            "让时间流过了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AEC")

    Jump("loc_3EF5")

    label("loc_3AEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_3AF9")
    Jump("loc_3EF5")

    label("loc_3AF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_3B03")
    Jump("loc_3EF5")

    label("loc_3B03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_3B0D")
    Jump("loc_3EF5")

    label("loc_3B0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_3B17")
    Jump("loc_3EF5")

    label("loc_3B17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_3C86")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3BB4")

    ChrTalk(
        0xFE,
        "真让人恼火啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "既然这样，\x01",
            "我也要想想办法了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C83")

    label("loc_3BB4")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "我丈夫一大早\x01",
            "又出去钓鱼了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "……真让人恼火啊！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "既然这样，\x01",
            "我也要想想办法了！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C83")

    Jump("loc_3EF5")

    label("loc_3C86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3CE3")

    ChrTalk(
        0xFE,
        "呼…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我那老公啊，\x01",
            "最近就算回到家里\x01",
            "也不打声招呼……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3EF5")

    label("loc_3CE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_3D65")

    ChrTalk(
        0xFE,
        (
            "老公又连招呼都不打\x01",
            "就从家里出去了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "说什么他也不听，\x01",
            "我究竟该怎么办才好……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3EF5")

    label("loc_3D65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_3E22")

    ChrTalk(
        0xFE,
        (
            "我老公因为忙于工作和爱好，\x01",
            "不怎么回家来，\x01",
            "所以我最近也出去旅行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "前些日子和附近的玛丽安\x01",
            "一起到柏斯去玩了玩。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3EF5")

    label("loc_3E22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_3EF5")

    ChrTalk(
        0xFE,
        (
            "老公难得在家一次，\x01",
            "却总是只顾做自己喜欢的事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这样真是不知道\x01",
            "我们是为了什么生活在一起的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3EF5")

    TalkEnd(0xFE)
    Return()

    # Function_16_37BE end

    def Function_17_3EF9(): pass

    label("Function_17_3EF9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_3F06")
    Jump("loc_4847")

    label("loc_3F06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_40C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3F80")

    ChrTalk(
        0xFE,
        (
            "唔～虽然心情有点复杂，\x01",
            "不过反过来想想平日自己的所作所为，\x01",
            "就没办法再抱怨什么了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40C3")

    label("loc_3F80")

    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "听我说！\x01",
            "行踪不明的妻子竟然回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "而且还有啊，\x01",
            "这几天她一直都在练习钓鱼。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "虽说刚刚才开始起步，\x01",
            "但已经比我技术还好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40C3")

    Jump("loc_4847")

    label("loc_40C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_4126")

    ChrTalk(
        0xFE,
        "哈啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我可以放弃最喜欢的钓鱼……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "只要你能回来……\x02",
    )

    CloseMessageWindow()
    Jump("loc_4847")

    label("loc_4126")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_42F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_41DC")

    ChrTalk(
        0xFE,
        (
            "我委托了游击士协会\x01",
            "寻找我妻子的行踪。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，\x01",
            "他们叫我不用担心，\x01",
            "说她自己会回家的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42F4")

    label("loc_41DC")

    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "我委托游击士协会\x01",
            "寻找我妻子的行踪。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，\x01",
            "他们叫我不用担心，\x01",
            "说她自己会回家的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他们会帮我\x01",
            "好好寻找吗……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42F4")

    Jump("loc_4847")

    label("loc_42F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_4392")

    ChrTalk(
        0xFE,
        "不、不好了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "妻子昨天下午出门之后，\x01",
            "就再也没有回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "要、要是被那些\x01",
            "恐怖分子给抓走的话怎么办……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4847")

    label("loc_4392")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_454C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_4457")

    ChrTalk(
        0xFE,
        (
            "唉，\x01",
            "我在『钓公师团』的入团测试中落选了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……说起来一大早\x01",
            "我就见不到妻子的踪影了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "到哪里去了呢？\x02",
    )

    CloseMessageWindow()
    Jump("loc_4549")

    label("loc_4457")

    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "唉，\x01",
            "我在『钓公师团』的入团测试中落选了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这样的话只有重新磨练技术\x01",
            "以后再次挑战了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……说起来一大早\x01",
            "我就见不到妻子的踪影了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "到哪里去了呢？\x02",
    )

    CloseMessageWindow()

    label("loc_4549")

    Jump("loc_4847")

    label("loc_454C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_4556")
    Jump("loc_4847")

    label("loc_4556")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_45E3")

    ChrTalk(
        0xFE,
        (
            "据说『钓公师团』\x01",
            "正要进行入团测试。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "要赶快去试试看。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4847")

    label("loc_45E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_45ED")
    Jump("loc_4847")

    label("loc_45ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_477F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_46B1")

    ChrTalk(
        0xFE,
        (
            "说起来，\x01",
            "市内好像有个名为\x01",
            "『钓公师团』的钓鱼爱好者组织呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这是个好机会，\x01",
            "趁这次休假的时候\x01",
            "到那里去看看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_477C")

    label("loc_46B1")

    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "说起来，\x01",
            "市内好像有个名为\x01",
            "『钓公师团』的钓鱼爱好者组织呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "唔，好像很有趣……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这是个好机会，\x01",
            "趁这次休假的时候\x01",
            "到那里去看看吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_477C")

    Jump("loc_4847")

    label("loc_477F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_4847")

    ChrTalk(
        0xFE,
        (
            "我本来是在王城里工作的，\x01",
            "公爵突然就让我休假。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "没办法，\x01",
            "只有用钓鱼来消磨时间了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4847")

    TalkEnd(0xFE)
    Return()

    # Function_17_3EF9 end

    SaveToFile()

Try(main)
