from ED6ScenarioHelper import *

def main():
    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4262   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4262.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60017",
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
        '克劳斯市长',                           # 9
        '莉拉',                                 # 10
        '梅贝尔市长',                           # 11
        '科林兹校长',                           # 12
        '茜亚',                                 # 13
        '金',                                   # 14
        '里拉老人',                             # 15
        '布莉姆',                               # 16
        '阿加特',                               # 17
        '奥利维尔',                             # 18
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
        'ED6_DT07/CH02353 ._CH',             # 00
        'ED6_DT07/CH02370 ._CH',             # 01
        'ED6_DT07/CH02363 ._CH',             # 02
        'ED6_DT07/CH02603 ._CH',             # 03
        'ED6_DT07/CH02623 ._CH',             # 04
        'ED6_DT07/CH02540 ._CH',             # 05
        'ED6_DT07/CH00070 ._CH',             # 06
        'ED6_DT07/CH02460 ._CH',             # 07
        'ED6_DT07/CH02230 ._CH',             # 08
        'ED6_DT07/CH02240 ._CH',             # 09
        'ED6_DT07/CH01100 ._CH',             # 0A
        'ED6_DT07/CH01350 ._CH',             # 0B
        'ED6_DT07/CH00050 ._CH',             # 0C
        'ED6_DT07/CH00030 ._CH',             # 0D
        'ED6_DT07/CH00073 ._CH',             # 0E
        'ED6_DT07/CH02350 ._CH',             # 0F
    )

    AddCharChipPat(
        'ED6_DT07/CH02353P._CP',             # 00
        'ED6_DT07/CH02370P._CP',             # 01
        'ED6_DT07/CH02363P._CP',             # 02
        'ED6_DT07/CH02603P._CP',             # 03
        'ED6_DT07/CH02623P._CP',             # 04
        'ED6_DT07/CH02540P._CP',             # 05
        'ED6_DT07/CH00070P._CP',             # 06
        'ED6_DT07/CH02460P._CP',             # 07
        'ED6_DT07/CH02230P._CP',             # 08
        'ED6_DT07/CH02240P._CP',             # 09
        'ED6_DT07/CH01100P._CP',             # 0A
        'ED6_DT07/CH01350P._CP',             # 0B
        'ED6_DT07/CH00050P._CP',             # 0C
        'ED6_DT07/CH00030P._CP',             # 0D
        'ED6_DT07/CH00073P._CP',             # 0E
        'ED6_DT07/CH02350P._CP',             # 0F
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -139520,
        Z                   = 4000,
        Y                   = 9500,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -78950,
        Z                   = 0,
        Y                   = 5960,
        Direction           = 359,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -81130,
        Z                   = 0,
        Y                   = 61160,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -77050,
        Z                   = 0,
        Y                   = 55320,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )


    ScpFunction(
        "Function_0_26A",          # 00, 0
        "Function_1_654",          # 01, 1
        "Function_2_677",          # 02, 2
        "Function_3_68D",          # 03, 3
        "Function_4_85B",          # 04, 4
        "Function_5_8F1",          # 05, 5
        "Function_6_DFA",          # 06, 6
        "Function_7_E5B",          # 07, 7
        "Function_8_101A",         # 08, 8
        "Function_9_1620",         # 09, 9
        "Function_10_23E3",        # 0A, 10
        "Function_11_25F6",        # 0B, 11
        "Function_12_37BE",        # 0C, 12
        "Function_13_4529",        # 0D, 13
        "Function_14_4564",        # 0E, 14
        "Function_15_5020",        # 0F, 15
        "Function_16_5698",        # 10, 16
        "Function_17_586E",        # 11, 17
    )


    def Function_0_26A(): pass

    label("Function_0_26A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_278")
    OP_A3(0x3FA)
    Event(0, 12)

    label("loc_278")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_289")
    OP_A3(0x3FB)
    OP_A2(0x63F)
    Event(0, 15)

    label("loc_289")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 4)), scpexpr(EXPR_END)), "loc_297")
    OP_A3(0x3FC)
    Event(0, 17)

    label("loc_297")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2FB")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xA, -28870, 200, 53540, 270)
    SetChrPos(0x9, -28040, 0, 54950, 211)
    SetChrPos(0xB, -83970, 200, -52980, 270)
    SetChrPos(0x8, -86020, 200, -52980, 90)

    label("loc_2FB")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (106, "loc_30B"),
        (101, "loc_32A"),
        (SWITCH_DEFAULT, "loc_340"),
    )


    label("loc_30B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_327")
    Event(0, 14)

    label("loc_327")

    Jump("loc_340")

    label("loc_32A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_33D")
    OP_A2(0x640)
    Event(0, 16)

    label("loc_33D")

    Jump("loc_340")

    label("loc_340")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_36A")
    SetChrChipByIndex(0x0, 7)
    SetChrChipByIndex(0x1, 8)
    SetChrChipByIndex(0x138, 9)
    SetChrFlags(0x0, 0x1000)
    SetChrFlags(0x1, 0x1000)
    SetChrFlags(0x138, 0x1000)

    label("loc_36A")

    OP_A2(0x639)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_42D")
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x10)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xD, 14)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x4)
    SetChrFlags(0xD, 0x10)
    SetChrFlags(0xD, 0x800)
    SetChrPos(0xD, -85910, 200, 59730, 270)
    SetChrChipByIndex(0x8, 15)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -25510, 0, -57090, 90)
    OP_43(0x8, 0x0, 0x0, 0x2)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x4)
    SetChrPos(0xB, -84730, 250, -53560, 270)
    SetChrFlags(0xB, 0x10)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x4)
    SetChrFlags(0xA, 0x10)
    SetChrPos(0xA, -28700, 250, 53020, 270)
    SetChrPos(0x9, -29640, 0, 51490, 0)
    Jump("loc_653")

    label("loc_42D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_43C")
    ClearChrFlags(0xF, 0x80)
    Jump("loc_653")

    label("loc_43C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_44B")
    SetChrFlags(0xE, 0x80)
    Jump("loc_653")

    label("loc_44B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_4FC")
    SetChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xD, 14)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x4)
    SetChrFlags(0xD, 0x10)
    SetChrFlags(0xD, 0x800)
    SetChrPos(0xD, -85910, 200, 59730, 270)
    SetChrChipByIndex(0x8, 15)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -25510, 0, -57090, 90)
    OP_43(0x8, 0x0, 0x0, 0x2)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x4)
    SetChrPos(0xB, -84730, 250, -53560, 270)
    SetChrFlags(0xB, 0x10)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x4)
    SetChrFlags(0xA, 0x10)
    SetChrPos(0xA, -28700, 250, 53020, 270)
    SetChrPos(0x9, -29640, 0, 51490, 0)
    Jump("loc_653")

    label("loc_4FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 7)), scpexpr(EXPR_END)), "loc_5AC")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -80180, 0, 61190, 0)
    OP_43(0xD, 0x0, 0x0, 0x2)
    SetChrChipByIndex(0x8, 15)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -25510, 0, -57090, 90)
    OP_43(0x8, 0x0, 0x0, 0x2)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x4)
    SetChrPos(0xB, -84730, 250, -53560, 270)
    SetChrFlags(0xB, 0x10)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x4)
    SetChrFlags(0xA, 0x10)
    SetChrPos(0xA, -28700, 250, 53020, 270)
    SetChrPos(0x9, -29640, 0, 51490, 0)
    SetChrPos(0xE, -138810, 0, 7070, 0)
    Jump("loc_653")

    label("loc_5AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_653")
    SetChrChipByIndex(0xD, 14)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x4)
    SetChrFlags(0xD, 0x10)
    SetChrFlags(0xD, 0x800)
    SetChrPos(0xD, -85910, 200, 59730, 270)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x8, -87350, 300, -53560, 90)
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x4)
    SetChrPos(0xB, -84730, 250, -53560, 270)
    SetChrFlags(0xB, 0x10)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x4)
    SetChrFlags(0xA, 0x10)
    SetChrPos(0xA, -28700, 250, 53020, 270)
    SetChrPos(0x9, -29640, 0, 51490, 0)

    label("loc_653")

    Return()

    # Function_0_26A end

    def Function_1_654(): pass

    label("Function_1_654")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_66D")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_66D")

    OP_4F(0x2B, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_654 end

    def Function_2_677(): pass

    label("Function_2_677")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_68C")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_677")

    label("loc_68C")

    Return()

    # Function_2_677 end

    def Function_3_68D(): pass

    label("Function_3_68D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_6FE")

    ChrTalk(
        0x11,
        (
            "#035F以前我就这么觉得……\x01",
            "他的演奏总是带有淡淡的忧伤呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_857")

    label("loc_6FE")

    OP_A2(0x7)

    ChrTalk(
        0x11,
        (
            "#033F……嗯？\x02\x03",
            "能听到口琴声呢。\x02\x03",
            "#030F这个好像是约修亚君\x01",
            "在柏斯湖畔吹奏的曲子吧……\x02\x03",
            "#035F以前我就这么觉得……\x01",
            "他的演奏总是带有淡淡的忧伤呢。\x02\x03",
            "虽然我没有听过，\x01",
            "原曲也是这么悲伤吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_857")

    TalkEnd(0xFE)
    Return()

    # Function_3_68D end

    def Function_4_85B(): pass

    label("Function_4_85B")

    TalkBegin(0xFE)

    ChrTalk(
        0x10,
        (
            "#050F…………………………\x02\x03",
            "结果还是没有和那个红头盔分出胜负……\x01",
            "　\x02\x03",
            "#057F真是个半吊子的结局啊。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_4_85B end

    def Function_5_8F1(): pass

    label("Function_5_8F1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_9E7")
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_91D")
    SetChrSubChip(0xFE, 2)
    Jump("loc_94E")

    label("loc_91D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_933")
    SetChrSubChip(0xFE, 1)
    Jump("loc_94E")

    label("loc_933")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_949")
    SetChrSubChip(0xFE, 0)
    Jump("loc_94E")

    label("loc_949")

    SetChrSubChip(0xFE, 2)

    label("loc_94E")

    OP_8C(0xFE, 270, 0)
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xD,
        (
            "#070F哎呀哎呀，\x01",
            "真没想到今天也能受到王城的招待呢。\x01",
            "　\x02\x03",
            "恢复和平之后，\x01",
            "喝起酒来心情也舒畅了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0)
    Jump("loc_DF6")

    label("loc_9E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_9F1")
    Jump("loc_DF6")

    label("loc_9F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_9FB")
    Jump("loc_DF6")

    label("loc_9FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_BE2")
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x102, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A24")
    SetChrSubChip(0xFE, 2)
    Jump("loc_A55")

    label("loc_A24")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A3A")
    SetChrSubChip(0xFE, 1)
    Jump("loc_A55")

    label("loc_A3A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A50")
    SetChrSubChip(0xFE, 0)
    Jump("loc_A55")

    label("loc_A50")

    SetChrSubChip(0xFE, 2)

    label("loc_A55")

    OP_8C(0xFE, 270, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_B12")

    ChrTalk(
        0xD,
        (
            "#070F不愧是王城啊。\x01",
            "王国里美丽的景色都集中在这里了。\x01",
            "　\x02\x03",
            "小姐们，如果打扫房间的话，\x01",
            "拜托你们动作麻利一点好吗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BDA")

    label("loc_B12")

    OP_A2(0x2)

    ChrTalk(
        0xD,
        (
            "#073F哦……\x02\x03",
            "#070F………………………………\x01",
            "………………………………\x02\x03",
            "不愧是王城啊。\x01",
            "王国里美丽的景色都集中在这里了。\x01",
            "　\x02\x03",
            "小姐们，如果打扫房间的话，\x01",
            "拜托你们动作麻利一点好吗。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BDA")

    SetChrSubChip(0xFE, 0)
    Jump("loc_DF6")

    label("loc_BE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 7)), scpexpr(EXPR_END)), "loc_C91")

    ChrTalk(
        0xD,
        (
            "#070F料理非常美味，\x01",
            "如果说还有什么美中不足的话，\x01",
            "就是酒还没有喝爽啊。\x02\x03",
            "我现在就要再去痛饮一番。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DF6")

    label("loc_C91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_DF6")
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x10E), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_CBA")
    SetChrSubChip(0xFE, 1)
    Jump("loc_CBF")

    label("loc_CBA")

    SetChrSubChip(0xFE, 0)

    label("loc_CBF")

    OP_8C(0xFE, 270, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_D36")

    ChrTalk(
        0xD,
        (
            "#070F说起来，\x01",
            "奥利维尔那家伙那么努力，\x01",
            "却没能来这里，真是可怜啊。\x02\x03",
            "不过这又能怨谁呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DF1")

    label("loc_D36")

    OP_A2(0x2)

    ChrTalk(
        0xD,
        (
            "#070F呼～不管什么时候，\x01",
            "只要呆在酒吧里就会觉得肚子饿……\x01",
            "　\x02\x03",
            "晚宴怎么还没开始啊，\x01",
            "我对宫廷料理的盛宴期待已久了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DF1")

    SetChrSubChip(0xFE, 0)

    label("loc_DF6")

    TalkEnd(0xFE)
    Return()

    # Function_5_8F1 end

    def Function_6_DFA(): pass

    label("Function_6_DFA")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "嗯，接下来是打扫客房。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为今天有许多客人要在城里留宿，\x01",
            "所以要做的准备不少啊～\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_DFA end

    def Function_7_E5B(): pass

    label("Function_7_E5B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_E68")
    Jump("loc_1016")

    label("loc_E68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_F15")

    ChrTalk(
        0xFE,
        (
            "《王城设计图》、《七至宝》、\x01",
            "《百日战役全貌》……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哎呀呀，\x01",
            "被情报部拿走的这些书\x01",
            "终于又回来了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1016")

    label("loc_F15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_F1F")
    Jump("loc_1016")

    label("loc_F1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_F29")
    Jump("loc_1016")

    label("loc_F29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_F90")

    ChrTalk(
        0xFE,
        (
            "完了，\x01",
            "格兰赛尔城的设计图纸竟然也不见了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "情报部的家伙\x01",
            "究竟打算拿去做什么啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1016")

    label("loc_F90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_1016")

    ChrTalk(
        0xFE,
        (
            "情报部的那群家伙，\x01",
            "到底要做什么啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "竟然把严禁外借的\x01",
            "重要资料强行取走了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1016")

    TalkEnd(0xFE)
    Return()

    # Function_7_E5B end

    def Function_8_101A(): pass

    label("Function_8_101A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1029")
    Call(0, 9)
    Jump("loc_161F")

    label("loc_1029")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_1126")
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1055")
    SetChrSubChip(0xFE, 2)
    Jump("loc_1086")

    label("loc_1055")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_106B")
    SetChrSubChip(0xFE, 1)
    Jump("loc_1086")

    label("loc_106B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1081")
    SetChrSubChip(0xFE, 0)
    Jump("loc_1086")

    label("loc_1081")

    SetChrSubChip(0xFE, 2)

    label("loc_1086")

    OP_8C(0xFE, 270, 0)
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xB,
        (
            "#780F真是个平静的夜晚。\x02\x03",
            "#780F王国能够恢复这样的和平，\x01",
            "多亏了艾丝蒂尔你们啊。\x01",
            "　\x02\x03",
            "卡西乌斯拥有这么好的孩子，\x01",
            "真是让人羡慕。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0)
    Jump("loc_161C")

    label("loc_1126")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_1130")
    Jump("loc_161C")

    label("loc_1130")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_113A")
    Jump("loc_161C")

    label("loc_113A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_1219")
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1163")
    SetChrSubChip(0xFE, 2)
    Jump("loc_1194")

    label("loc_1163")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1179")
    SetChrSubChip(0xFE, 1)
    Jump("loc_1194")

    label("loc_1179")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_118F")
    SetChrSubChip(0xFE, 0)
    Jump("loc_1194")

    label("loc_118F")

    SetChrSubChip(0xFE, 2)

    label("loc_1194")

    OP_8C(0xFE, 270, 0)
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xB,
        (
            "#780F哦，\x01",
            "想不到希尔丹夫人竟然亲自到访……\x02\x03",
            "唔，我明白了。\x01",
            "是在培训实习的侍女吧？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0)
    Jump("loc_161C")

    label("loc_1219")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_133B")
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1242")
    SetChrSubChip(0xFE, 2)
    Jump("loc_1273")

    label("loc_1242")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1258")
    SetChrSubChip(0xFE, 1)
    Jump("loc_1273")

    label("loc_1258")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_126E")
    SetChrSubChip(0xFE, 0)
    Jump("loc_1273")

    label("loc_126E")

    SetChrSubChip(0xFE, 2)

    label("loc_1273")

    OP_8C(0xFE, 270, 0)
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xB,
        (
            "#780F就上校所说的话来看，\x01",
            "是非常合乎情理的……\x02\x03",
            "但无论如何，也必须亲自向女王陛下\x01",
            "还有公主殿下询问才恰当啊。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0)
    Jump("loc_161C")

    label("loc_133B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_161C")
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1364")
    SetChrSubChip(0xFE, 2)
    Jump("loc_1395")

    label("loc_1364")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_137A")
    SetChrSubChip(0xFE, 1)
    Jump("loc_1395")

    label("loc_137A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1390")
    SetChrSubChip(0xFE, 0)
    Jump("loc_1395")

    label("loc_1390")

    SetChrSubChip(0xFE, 2)

    label("loc_1395")

    OP_8C(0xFE, 270, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1457")

    ChrTalk(
        0xB,
        (
            "#782F呼～我有些担心啊……\x02\x03",
            "她会不会在回王都之前，\x01",
            "先顺路去找特蕾莎院长了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1617")

    label("loc_1457")

    OP_A2(0x6)

    ChrTalk(
        0xB,
        (
            "#780F对了，我说你们俩啊……\x01",
            "见到科洛丝了吗？\x02\x03",
            "我从她那儿听说了\x01",
            "你们约好在王都相见的事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F唔～这个啊，\x01",
            "协会还没有通知我们……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F请问校长，\x01",
            "她已经来到王都了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#782F这是肯定的……\x02\x03",
            "#783F呼～我有些担心啊……\x02\x03",
            "她会不会在回王都之前，\x01",
            "先顺路去找特蕾莎院长了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1617")

    SetChrSubChip(0xFE, 0)

    label("loc_161C")

    TalkEnd(0xFE)

    label("loc_161F")

    Return()

    # Function_8_101A end

    def Function_9_1620(): pass

    label("Function_9_1620")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F8A")
    OP_A2(0x63B)
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, -85750, 0, -55050, 0)
    SetChrPos(0x102, -86740, 0, -55050, 0)
    OP_6D(-85810, 0, -53740, 0)
    SetChrSubChip(0xB, 1)
    SetChrSubChip(0x8, 2)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#601F#1P哦哦，来了吗。\x01",
            "艾丝蒂尔、约修亚。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#780F呵呵，好久不见了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F哎……校长！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F难道科林兹校长您\x01",
            "也被邀请参加今天的晚宴吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#780F是啊，就是乘今天的定期船\x01",
            "从卢安赶过来的呢。\x02\x03",
            "我已经听克劳斯市长说了，\x01",
            "你们赢得了武术大会的冠军啊。\x02\x03",
            "乔儿他们听到了肯定也会十分高兴的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F嘿嘿……谢谢了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F说起来，\x01",
            "我没有想到校长也会被邀请来呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#603F#1P科林兹校长作为利贝尔首屈一指的贤者，\x01",
            "每年都会出席王国会议。\x01",
            "　\x02\x03",
            "被邀请出席晚宴也没有什么奇怪的啦。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#780F哈哈，说我是贤者，\x01",
            "克劳斯市长你真是太过誉了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505F嗯……王国会议是什么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F是为解决整个王国范围内的问题\x01",
            "而召开的一年一度的例会。\x02\x03",
            "女王陛下、各地区的市长，\x01",
            "以及各界的代表人士齐聚一堂，\x01",
            "讨论和协商各种各样的问题。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F哎～是这样啊。\x02\x03",
            "那么，今天的晚宴\x01",
            "邀请的都是这些人啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#783F不……\x01",
            "其实连一半都不到。\x02\x03",
            "女王陛下身体欠佳，\x01",
            "摩尔根将军忙于军务……\x02\x03",
            "卢安的戴尔蒙市长\x01",
            "也因为那个案件被逮捕了。\x02\x03",
            "还有，拉赛尔博士也……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#603F和他相关的那个案件，\x01",
            "现在还有很多地方没有弄清楚呢。\x02\x03",
            "不仅牵扯到王室亲卫队，\x01",
            "而且还说是大规模的恐怖组织所为，\x01",
            "到底真相是怎样我们现在也很迷惑……\x02\x03",
            "#602F真是的，在这种情况下，\x01",
            "还有心思召开什么晚宴。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#003F………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#015F………………………………\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0)
    Sleep(300)

    ChrTalk(
        0xB,
        (
            "#780F不过，为了确认公爵大人真正的心意，\x01",
            "我们也有出席这次晚宴的必要。\x01",
            "　\x02\x03",
            "而且更重要的是……\x01",
            "可以借此机会探望和问候女王陛下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#603F嗯，这才是最重要的。\x01",
            "　\x02\x03",
            "#602F来到这格兰赛尔城，\x01",
            "却不能拜见陛下这不是很奇怪吗。\x01",
            "　\x02\x03",
            "#601F而且……\x01",
            "也很久没有见到科洛蒂娅公主了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F科洛蒂娅公主……\x01",
            "我记得是女王陛下的孙女吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F公主殿下也住在格兰赛尔城吗？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 1)
    Sleep(100)
    SetChrSubChip(0x8, 2)
    Sleep(200)

    ChrTalk(
        0x8,
        (
            "#604F#1P不，她平常是住在另外一个地方的。\x01",
            "　\x02\x03",
            "不过，听说几天前回到王都来了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F哎～是这样啊……\x02\x03",
            "#502F嗯～如果有机会，\x01",
            "一定要和她见上一面。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#781F呵呵，如果是你们，\x01",
            "肯定能见到她的。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0)
    SetChrSubChip(0x8, 0)
    EventEnd(0x0)
    Jump("loc_23E2")

    label("loc_1F8A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_2146")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1FF7")

    ChrTalk(
        0x8,
        (
            "#600F以后我们也会一如既往地努力，\x01",
            "为女王陛下工作。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2143")

    label("loc_1FF7")

    OP_A2(0x3)

    ChrTalk(
        0x8,
        (
            "#600F公主殿下被抓做人质，\x01",
            "女王陛下为此一定相当心痛吧……\x01",
            "　\x02\x03",
            "就算是为国家着想，\x01",
            "但理查德上校也不应该走上这样一条路……\x01",
            "　\x02\x03",
            "……以后我们也会一如既往地努力，\x01",
            "为女王陛下工作。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2143")

    Jump("loc_23DF")

    label("loc_2146")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_2150")
    Jump("loc_23DF")

    label("loc_2150")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_215A")
    Jump("loc_23DF")

    label("loc_215A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_21A0")

    ChrTalk(
        0x8,
        (
            "#600F哦，这不是希尔丹夫人吗……\x01",
            "这么晚了还有什么事呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23DF")

    label("loc_21A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_22CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_21F9")

    ChrTalk(
        0x8,
        (
            "#600F呼，一切都来得那么突然，\x01",
            "怎能不让人震惊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22C8")

    label("loc_21F9")

    OP_A2(0x3)

    ChrTalk(
        0x8,
        (
            "#602F没想到陛下正为退位的决定\x01",
            "而感到烦恼……\x01",
            "　\x02\x03",
            "而且那么快就把\x01",
            "科洛蒂娅公主的婚姻大事提了出来。\x01",
            "　\x02\x03",
            "#603F一切都来得那么突然，\x01",
            "怎能不让人震惊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22C8")

    Jump("loc_23DF")

    label("loc_22CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_23DF")
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_22F4")
    SetChrSubChip(0xFE, 1)
    Jump("loc_2325")

    label("loc_22F4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_230A")
    SetChrSubChip(0xFE, 0)
    Jump("loc_2325")

    label("loc_230A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x10E), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2320")
    SetChrSubChip(0xFE, 2)
    Jump("loc_2325")

    label("loc_2320")

    SetChrSubChip(0xFE, 1)

    label("loc_2325")

    OP_8C(0xFE, 90, 0)
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0x8,
        (
            "#603F真是的……\x02\x03",
            "在这种状况下还要召开晚宴，\x01",
            "不知道公爵是怎么想的。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0)

    label("loc_23DF")

    TalkEnd(0xFE)

    label("loc_23E2")

    Return()

    # Function_9_1620 end

    def Function_10_23E3(): pass

    label("Function_10_23E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23F2")
    Call(0, 11)
    Jump("loc_25F5")

    label("loc_23F2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_24A5")

    ChrTalk(
        0x9,
        (
            "#620F被卷入这样一个事件，\x01",
            "真是不得了……\x02\x03",
            "这几天就让公主殿下\x01",
            "好好休息一下吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25F2")

    label("loc_24A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_24AF")
    Jump("loc_25F2")

    label("loc_24AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_24B9")
    Jump("loc_25F2")

    label("loc_24B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_24F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_24D8")

    ChrTalk(
        0x9,
        "#620F…………………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_24F4")

    label("loc_24D8")

    OP_A2(0x4)

    ChrTalk(
        0x9,
        (
            "#620F……………………！\x02\x03",
            "#621F…………………………\x01",
            "…………………………\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24F4")

    Jump("loc_25F2")

    label("loc_24F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_2573")

    ChrTalk(
        0x9,
        (
            "#620F看样子在晚宴上\x01",
            "又出现了严重的事情……\x02\x03",
            "小姐的烦恼又增加了，\x01",
            "真让我担心啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25F2")

    label("loc_2573")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_25F2")

    ChrTalk(
        0x9,
        (
            "#621F小姐她因为能与你们二位相遇\x01",
            "而感到非常的愉快。\x02\x03",
            "请二位以后一定要\x01",
            "经常到柏斯来玩哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25F2")

    TalkEnd(0xFE)

    label("loc_25F5")

    Return()

    # Function_10_23E3 end

    def Function_11_25F6(): pass

    label("Function_11_25F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FB4")
    OP_A2(0x63A)
    EventBegin(0x0)
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, -28930, 0, 54500, 180)
    SetChrPos(0x102, -29780, 0, 54500, 180)
    OP_6D(-29260, 0, 53440, 0)
    SetChrSubChip(0xA, 2)
    OP_8C(0x9, 0, 0)
    OP_4A(0x9, 255)
    OP_0D()

    ChrTalk(
        0x101,
        "#501F啊……市长姐姐！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F莉拉小姐也来了啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#621F艾丝蒂尔小姐、约修亚先生……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#611F呵呵，我们又见面了呢。\x02\x03",
            "我一直等着你们两个的到来呢。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F市长姐姐果然也被邀请参加晚宴了。\x01",
            "　\x02\x03",
            "#004F哎，为什么会知道我们要来……？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#610F我是听克劳斯市长说的。\x02\x03",
            "你们在武术大会中获得优胜，\x01",
            "所以肯定会被邀请出席晚宴。\x02\x03",
            "#617F啊～如果早知道的话，\x01",
            "我就放下所有工作来给你们加油了……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#623F小姐，话虽这么说……\x02\x03",
            "可是，如果这样做的话，\x01",
            "小姐自己不是到最后又要非常辛苦了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#612F呜～我知道啦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F啊哈哈……\x01",
            "看来市长姐姐总是忙于公务啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#615F真是的，女王陛下暂且不论，\x01",
            "那个杜南公爵举办的晚宴，\x01",
            "本来就没有什么闲工夫来参加啊……\x02\x03",
            "都是因为那个军队的女军官\x01",
            "固执地催促让我出席，\x01",
            "我也是在没办法之下才来王都的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F是情报部的凯诺娜上尉吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#612F嗯，就是她。\x02\x03",
            "表面很有礼貌，但其实不把别人放在眼里，\x01",
            "我其实很不喜欢那种人呢。\x02\x03",
            "而且最近……\x01",
            "也没办法和摩尔根将军取得联系……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F那是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F和哈肯大门那边联系不上吗？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#615F那里守关的士兵老是说『将军不在』，\x01",
            "每次都让我吃了闭门羹。\x02\x03",
            "好像是为了应对恐怖事件，\x01",
            "看来他的工作相当繁忙啊。\x02\x03",
            "#610F本来还想能不能\x01",
            "在今天的晚宴上见到他呢……\x02\x03",
            "看起来好像也没有出席啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#003F是这样啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F请问市长您对这件事是怎么看的？\x02\x03",
            "在这个时候把各市的市长召集起来\x01",
            "召开这样的晚宴……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#613F这个嘛……\x02\x03",
            "如果是女王陛下举办的话，\x01",
            "应该是要宣布重要的事情吧……\x02\x03",
            "#611F不过这次大概只是为了\x01",
            "陪杜南公爵打发时间而已。\x02\x03",
            "滥用陛下代理人的特权，\x01",
            "让人认为他大权在握而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#509F哇～真是精辟啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F不过……\x01",
            "也有可能不只是为这样的理由。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#611F算了，听说格兰赛尔城的西餐\x01",
            "是整个利贝尔王国最棒的……\x02\x03",
            "总之，享用完美味的晚餐，\x01",
            "探望一下久未见面的女王陛下，\x01",
            "然后明天一大早就赶快回柏斯吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x9, 255)
    SetChrSubChip(0xA, 0)
    EventEnd(0x0)
    Jump("loc_37BD")

    label("loc_2FB4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_317F")
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2FE0")
    SetChrSubChip(0xFE, 2)
    Jump("loc_3011")

    label("loc_2FE0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2FF6")
    SetChrSubChip(0xFE, 1)
    Jump("loc_3011")

    label("loc_2FF6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_300C")
    SetChrSubChip(0xFE, 0)
    Jump("loc_3011")

    label("loc_300C")

    SetChrSubChip(0xFE, 2)

    label("loc_3011")

    OP_8C(0xFE, 270, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_30B4")

    ChrTalk(
        0xA,
        (
            "#610F艾丝蒂尔，\x01",
            "我们打算乘坐明天的定期船回柏斯。\x02\x03",
            "#611F如果你们再到柏斯，\x01",
            "一定要来找我们玩哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3177")

    label("loc_30B4")

    OP_A2(0x5)

    ChrTalk(
        0xA,
        (
            "#610F艾丝蒂尔，\x01",
            "我们打算乘坐明天的定期船回柏斯。\x02\x03",
            "#611F如果你们再到柏斯，\x01",
            "一定要来找我们玩哦。\x02\x03",
            "我们再去安特洛丝餐厅吃饭聊天吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3177")

    SetChrSubChip(0xFE, 0)
    Jump("loc_37BA")

    label("loc_317F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_3189")
    Jump("loc_37BA")

    label("loc_3189")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_3193")
    Jump("loc_37BA")

    label("loc_3193")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_347F")
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_31BC")
    SetChrSubChip(0xFE, 2)
    Jump("loc_31ED")

    label("loc_31BC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_31D2")
    SetChrSubChip(0xFE, 1)
    Jump("loc_31ED")

    label("loc_31D2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_31E8")
    SetChrSubChip(0xFE, 0)
    Jump("loc_31ED")

    label("loc_31E8")

    SetChrSubChip(0xFE, 2)

    label("loc_31ED")

    OP_8C(0xFE, 270, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_3262")

    ChrTalk(
        0xA,
        (
            "#610F您背后的是实习女佣吧。\x02\x03",
            "让我想起莉拉刚来的时候了呢。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3477")

    label("loc_3262")

    OP_A2(0x5)

    ChrTalk(
        0xA,
        "#610F希尔丹夫人，好久不见了。\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x0,
        "希尔丹夫人",
        (
            "#712F梅贝尔市长，\x01",
            "您好像非常劳累呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#617F呵呵，\x01",
            "果然还是被您看出来了啊。\x02\x03",
            "#610F来这里之前有些棘手的事情要处理，\x01",
            "所以就没有休息好。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x0,
        "希尔丹夫人",
        (
            "#710F那样可不行啊。\x02\x03",
            "稍后我拿一支催眠香为您点上吧。\x01",
            "　\x02\x03",
            "那个是最近从东方订购回来的呢。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#610F嗯，万分感激。\x02",
    )

    CloseMessageWindow()

    label("loc_3477")

    SetChrSubChip(0xFE, 0)
    Jump("loc_37BA")

    label("loc_347F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_3602")
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_34A8")
    SetChrSubChip(0xFE, 2)
    Jump("loc_34D9")

    label("loc_34A8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_34BE")
    SetChrSubChip(0xFE, 1)
    Jump("loc_34D9")

    label("loc_34BE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_34D4")
    SetChrSubChip(0xFE, 0)
    Jump("loc_34D9")

    label("loc_34D4")

    SetChrSubChip(0xFE, 2)

    label("loc_34D9")

    OP_8C(0xFE, 270, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_355E")

    ChrTalk(
        0xA,
        (
            "#612F那个杜南公爵将要继承王位……\x01",
            "　\x02\x03",
            "呼，\x01",
            "从现在开始我就感到头疼了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35FA")

    label("loc_355E")

    OP_A2(0x5)

    ChrTalk(
        0xA,
        (
            "#612F晚宴上的一席话真是让人震惊。\x01",
            "　\x02\x03",
            "那个杜南公爵将要继承王位……\x01",
            "　\x02\x03",
            "#617F呼，\x01",
            "从现在开始我就感到头疼了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35FA")

    SetChrSubChip(0xFE, 0)
    Jump("loc_37BA")

    label("loc_3602")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_37BA")
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_362B")
    SetChrSubChip(0xFE, 2)
    Jump("loc_365C")

    label("loc_362B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3641")
    SetChrSubChip(0xFE, 1)
    Jump("loc_365C")

    label("loc_3641")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3657")
    SetChrSubChip(0xFE, 0)
    Jump("loc_365C")

    label("loc_3657")

    SetChrSubChip(0xFE, 2)

    label("loc_365C")

    OP_8C(0xFE, 270, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_3702")

    ChrTalk(
        0xA,
        (
            "#615F以前公爵到柏斯视察时，\x01",
            "还在市内恣意妄为……\x01",
            "　\x02\x03",
            "#617F市民们纷纷跑来投诉，\x01",
            "真是让我难办得不得了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37B5")

    label("loc_3702")

    OP_A2(0x5)

    ChrTalk(
        0xA,
        (
            "#615F公爵真是个麻烦的人。\x02\x03",
            "以前他到柏斯视察时，\x01",
            "还在市内恣意妄为……\x02\x03",
            "#617F市民们纷纷跑来投诉，\x01",
            "真是让我难办得不得了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37B5")

    SetChrSubChip(0xFE, 0)

    label("loc_37BA")

    TalkEnd(0xFE)

    label("loc_37BD")

    Return()

    # Function_11_25F6 end

    def Function_12_37BE(): pass

    label("Function_12_37BE")

    EventBegin(0x0)
    SetChrPos(0x102, -52050, 0, 2040, 0)
    SetChrPos(0x101, -52050, 0, 2040, 0)
    SetChrPos(0x108, -52050, 0, 2040, 0)
    SetChrPos(0xC, -52050, 0, 2040, 0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x40)
    SetChrFlags(0xC, 0x4)
    SetChrFlags(0x101, 0x40)
    SetChrFlags(0x101, 0x4)
    OP_69(0xC, 0x0)
    OP_6A(0xC)

    def lambda_382D():
        OP_8E(0xFE, 0xFFFECE9C, 0x0, 0x884, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_382D)
    Sleep(500)

    def lambda_384D():
        OP_8E(0xFE, 0xFFFECE9C, 0x0, 0x884, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_384D)
    Sleep(500)

    def lambda_386D():

        label("loc_386D")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_386D")

    QueueWorkItem2(0x102, 2, lambda_386D)

    def lambda_387E():
        OP_8E(0xFE, 0xFFFECE9C, 0x0, 0x884, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_387E)
    Sleep(500)

    def lambda_389E():
        OP_8E(0xFE, 0xFFFECE9C, 0x0, 0x884, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_389E)
    WaitChrThread(0xC, 0x1)

    def lambda_38BE():
        OP_8E(0xFE, 0xFFFECB86, 0x0, 0x1CDE, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_38BE)
    WaitChrThread(0x101, 0x1)

    def lambda_38DE():
        OP_8E(0xFE, 0xFFFEC7F8, 0x0, 0x159A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_38DE)
    WaitChrThread(0x102, 0x1)

    def lambda_38FE():
        OP_8E(0xFE, 0xFFFECD2A, 0x0, 0x1554, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_38FE)
    WaitChrThread(0x108, 0x1)

    def lambda_391E():
        OP_8E(0xFE, 0xFFFECA50, 0x0, 0x1162, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_391E)
    WaitChrThread(0xC, 0x1)
    Sleep(200)
    OP_6F(0x1D, 0)
    OP_70(0x1D, 0x3C)
    Sleep(400)
    OP_8E(0xC, 0xFFFEC668, 0x0, 0x1C52, 0x7D0, 0x0)
    TurnDirection(0xC, 0x101, 400)

    ChrTalk(
        0xC,
        (
            "这个就是各位\x01",
            "晚上可以使用的房间。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "请进吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F啊，好的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F那么我们就不客气了。\x02",
    )

    CloseMessageWindow()
    OP_43(0x101, 0x1, 0x0, 0xD)
    Sleep(500)
    OP_44(0x102, 0x2)
    OP_43(0x102, 0x1, 0x0, 0xD)
    Sleep(500)
    OP_43(0x108, 0x1, 0x0, 0xD)
    Sleep(1000)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x108, 0xFF)
    ClearMapFlags(0x1)
    Fade(1000)
    OP_6D(-89640, 0, 57110, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_9F(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_9F(0x108, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrPos(0xC, -80040, 0, 50510, 0)
    SetChrPos(0x101, -80880, 0, 53000, 270)
    SetChrPos(0x102, -79650, 0, 53710, 270)
    SetChrPos(0x108, -78830, 0, 52390, 270)
    SetChrFlags(0xD, 0x80)
    OP_6D(-79120, 0, 55910, 5000)
    ClearChrFlags(0x101, 0x40)
    ClearChrFlags(0x101, 0x4)

    ChrTalk(
        0x101,
        "#004F#2P哇……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#2P能在这种地方过夜，\x01",
            "真是做梦也无法想象呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#071F#2P哎呀～真是不错啊，\x01",
            "回共和国之后可以当成炫耀的资本了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#2P在晚宴开始之前，\x01",
            "请各位客人在此等候。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3BC2():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3BC2)

    def lambda_3BD0():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3BD0)

    def lambda_3BDE():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_3BDE)
    OP_6D(-79790, 0, 52600, 1200)

    ChrTalk(
        0xC,
        (
            "虽然城内允许自由参观，\x01",
            "不过因为警卫上的理由，\x01",
            "有一些场所是禁止进入的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "请不要到那些地方去。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F嗯……\x01",
            "具体来说哪些地方不能去呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "首先是，\x01",
            "女王陛下居住的女王宫。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "就是在王城顶层空中庭园的一角\x01",
            "建造的小型宫殿。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F空中庭园……\x01",
            "听起来感觉十分的美丽呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "嘻嘻……诞辰庆典的时候，\x01",
            "陛下会在空中庭园的露台上\x01",
            "向王都的市民致意。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "如果只是到空中庭园去的话，\x01",
            "我想应该没有什么问题的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "还有，其他禁止进入的场所……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "一楼的亲卫队办公室\x01",
            "以及地下的宝物库。\x02",
        )
    )

    CloseMessageWindow()
    OP_9F(0x108, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    ChrTalk(
        0x102,
        "#012F亲卫队办公室……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#072F是不是被认定为恐怖分子\x01",
            "而受到王国军通缉的那些人呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "是、是的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "现在，那个办公室\x01",
            "正由情报部的人使用。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "所以不允许进入，\x01",
            "请各位客人理解。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F差不多明白了。\x02\x03",
            "#010F对了，请问一下\x01",
            "出席晚宴的其他客人现在在哪里呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "过一会儿，\x01",
            "你们就能见到了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "大概他们现在\x01",
            "正在各自的房间里休息吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F这样的话，\x01",
            "克劳斯市长已经来了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "是的，\x01",
            "刚刚才招待过他。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "那么，我先告退了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "如果各位客人有什么事情的话，\x01",
            "请到一楼的侍女休息室来找我。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xC, 180, 400)

    def lambda_4160():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_4160)
    OP_8E(0xC, 0xFFFEC6F4, 0x0, 0xBC3E, 0x7D0, 0x0)
    SetChrFlags(0xC, 0x4)

    ChrTalk(
        0x101,
        "#500F那么……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)
    TurnDirection(0x102, 0x101, 400)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾丝蒂尔和约修亚\x01",
            "趁金没有注意的时候交换了一下眼色。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    def lambda_421F():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_421F)
    Sleep(400)
    TurnDirection(0x102, 0x108, 400)
    TurnDirection(0x101, 0x108, 400)

    ChrTalk(
        0x101,
        (
            "#006F……我说，金先生。\x02\x03",
            "我们想借此机会在城里参观一下……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F晚宴开始之前就会回来。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#075F哎呀哎呀，刚刚比赛完，\x01",
            "你们年轻人真是精力旺盛啊。\x02\x03",
            "#070F好，你们去吧。\x02\x03",
            "晚宴开始之前，\x01",
            "我就在这豪华的房间里小憩一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(-79060, 0, 5600, 0)
    RemoveParty(0x7, 0xFF)
    SetChrPos(0x101, -79060, 0, 9840, 0)
    SetChrPos(0x102, -79060, 0, 9840, 0)
    OP_6F(0x1D, 60)

    def lambda_43C0():
        OP_8E(0xFE, 0xFFFECB2C, 0x0, 0x157C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_43C0)
    Sleep(600)

    def lambda_43E0():
        OP_8E(0xFE, 0xFFFECB2C, 0x0, 0x1900, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_43E0)
    WaitChrThread(0x101, 0x1)

    def lambda_4400():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4400)
    WaitChrThread(0x102, 0x1)

    def lambda_4413():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4413)
    OP_72(0x1D, 0x800)
    OP_22(0x7, 0x0, 0x64)
    OP_70(0x1D, 0x0)
    OP_73(0x1D)
    OP_71(0x1D, 0x800)

    ChrTalk(
        0x101,
        (
            "#006F#4P在晚宴开始之前，\x01",
            "一定要尽可能多做一些事情。\x02\x03",
            "首先要去找\x01",
            "尤莉亚小姐所说的希尔丹夫人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F之后还有时间的话，\x01",
            "我们最好去和其他的客人打个招呼。\x02\x03",
            "大概，认识的人会很多吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_6A(0x0)
    ClearMapFlags(0x1)
    EventEnd(0x0)
    Return()

    # Function_12_37BE end

    def Function_13_4529(): pass

    label("Function_13_4529")

    OP_8E(0xFE, 0xFFFECB5E, 0x0, 0x1CA2, 0xBB8, 0x0)

    def lambda_4543():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_4543)
    OP_8E(0xFE, 0xFFFECB68, 0x0, 0x2602, 0xBB8, 0x0)
    Return()

    # Function_13_4529 end

    def Function_14_4564(): pass

    label("Function_14_4564")

    EventBegin(0x0)
    OP_6D(-80000, 0, 52700, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrFlags(0xD, 0x80)
    AddParty(0x7, 0xFF)
    SetChrPos(0x101, -79490, 0, 51290, 0)
    SetChrPos(0x102, -80530, 0, 51090, 0)
    SetChrPos(0x108, -80180, 0, 61190, 0)

    def lambda_45E4():
        OP_6D(-79580, 0, 57340, 2000)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_45E4)
    Sleep(1000)
    OP_8C(0x108, 180, 400)
    WaitChrThread(0x108, 0x1)

    ChrTalk(
        0x108,
        (
            "#070F哟，艾丝蒂尔、约修亚。\x01",
            "回来得是不是有些晚呢。\x02\x03",
            "就要到晚宴开始的时候了吧？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4660():
        OP_6D(-80100, 0, 60780, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4660)

    def lambda_4678():
        OP_8E(0xFE, 0xFFFEC884, 0x0, 0xE98E, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4678)
    Sleep(300)

    def lambda_4698():
        OP_8E(0xFE, 0xFFFEC49C, 0x0, 0xE948, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4698)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x3)

    ChrTalk(
        0x101,
        (
            "#506F不好意思啊，金先生。\x02\x03",
            "东看看西逛逛的就把时间给忘了～\x01",
            "　\x02\x03",
            "#006F而且还和各地的市长谈了许多话哦。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#073F咦，你们俩之前就\x01",
            "认识那些有身份的人物吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F洛连特的市长平日就对我们很亲切。\x01",
            "　\x02\x03",
            "其他的几位是我们在\x01",
            "旅行途中经过各个城市时认识的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#074F原来如此啊。\x02\x03",
            "游击士在完成任务的时候，\x01",
            "的确有许多结识有身份人物的机会呢。\x02\x03",
            "#070F哈哈，这样看来，\x01",
            "你们在王国好像相当活跃对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F哈哈哈……还没有到那种程度啦。\x02\x03",
            "#501F对了，金先生到王都来\x01",
            "是因为有什么任务要完成吗？\x02\x03",
            "我想，虽说是在别国，\x01",
            "但还是照样可以完成相关任务吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F是啊，一旦成为了正游击士，\x01",
            "就可以去做一些超越国界的任务了……\x02\x03",
            "不过预选赛啊，大使馆的手续啊什么的，\x01",
            "忙得我连接受任务的时间都没有了。\x02\x03",
            "#075F不过，有其他四位游击士在，\x01",
            "好像就没有我出场的必要了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F的确，如果游击士都聚集到一起，\x01",
            "大部分事件都可以迎刃而解了。\x02\x03",
            "可是，假如都集中在王都的话，\x01",
            "其他地方的支部可就人手不足了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#071F哇哈哈，说的也是啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F呼，总觉得到现在\x01",
            "才想到这些也用处不大了。\x02\x03",
            "#505F雪拉姐现在在洛连特做什么呢……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#073F之前我也听你们提到过这个名字……\x01",
            "　\x02\x03",
            "那个雪拉姐莫非就是雪拉扎德？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#004F咦……你认识她！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F是啊，她是我们的前辈，\x01",
            "过去一直都在照顾着我们呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#071F原来如此，竟然是这样。\x02\x03",
            "以前她到卡尔瓦德来的时候，\x01",
            "我和她曾经有过一面之缘。\x02\x03",
            "真羡慕她有一个很好的老师啊，\x01",
            "年纪轻轻却见多识广、身手不凡。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#008F（他说的那个老师不就是……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#019F（嗯，就是父亲呢。）\x02",
    )

    CloseMessageWindow()
    OP_22(0x71, 0x0, 0x64)
    Sleep(500)
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x108, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrPos(0xC, -80290, 0, 50310, 0)
    SetChrFlags(0xC, 0x80)

    def lambda_4DF4():
        OP_6D(-80130, 0, 59550, 1500)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_4DF4)

    def lambda_4E0C():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4E0C)

    def lambda_4E1A():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_4E1A)

    def lambda_4E28():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4E28)
    OP_22(0x6, 0x0, 0x64)
    ClearChrFlags(0xC, 0x80)
    OP_8E(0xC, 0xFFFEC5E6, 0x0, 0xD1B0, 0x7D0, 0x0)
    WaitChrThread(0x108, 0x2)

    ChrTalk(
        0xC,
        (
            "#2P打搅一下，\x01",
            "晚宴已经准备完毕了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#2P现在我带大家过去可以吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F#5P哦，我都已经等不及了。\x02\x03",
            "#071F那～么，\x01",
            "我们这就去好好享用这顿美餐吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F#5P嗯，说起来在比赛之后\x01",
            "我的肚子已经饿得咕咕地叫了。\x02\x03",
            "#001F走吧～大吃一顿去了～⊙\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(800)
    OP_8C(0x102, 45, 400)

    ChrTalk(
        0x102,
        (
            "#019F#6P我说你们俩啊……\x02\x03",
            "还是不要忘记餐桌上的礼仪哦……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T4251   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_14_4564 end

    def Function_15_5020(): pass

    label("Function_15_5020")

    EventBegin(0x0)
    RemoveParty(0x7, 0xFF)
    ClearChrFlags(0xD, 0x80)
    OP_43(0xD, 0x0, 0x0, 0x2)
    SetChrChipByIndex(0xD, 6)
    OP_4A(0xD, 255)
    SetChrPos(0xD, -80180, 0, 61190, 180)
    SetChrPos(0x101, -79740, 0, 59790, 0)
    SetChrPos(0x102, -80740, 0, 59720, 0)
    OP_6D(-80100, 0, 60780, 0)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(
        0xD,
        (
            "#070F哎呀，竟然意外地在晚宴上\x01",
            "听到了这么出乎预料的消息。\x02\x03",
            "我一来就插入你们国家的谈话，\x01",
            "把你们两个吓了一跳对吧？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#005F那、那是当然的了！\x02\x03",
            "要、要不是说得还比较周到的话……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#073F啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F啊，嗯，没什么。\x02\x03",
            "#505F可是……真是遗憾啊。\x01",
            "　\x02\x03",
            "虽然特地让舌头沉醉于美味的料理之中，\x01",
            "可最后那道菜的精妙还是没能体会。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#019F哈哈，不用强求嘛。\x02\x03",
            "#010F对了，艾丝蒂尔。\x01",
            "去散散步消化一下食物如何？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#004F咦……？\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#006F啊啊！\x01",
            "对啊，好建议！\x02\x03",
            "不错呢～我也想好好\x01",
            "呼吸一下外面的新鲜空气了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#073F啊～刚才去参观王城各处，\x01",
            "这回吃完饭又要去散步了……\x02\x03",
            "#075F想不承认都不行啊，\x01",
            "这就是年纪的差异所体现的区别。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xD, 400)

    ChrTalk(
        0x101,
        "#001F啊哈哈，金先生你太夸张了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0xD, 400)

    ChrTalk(
        0x102,
        (
            "#010F金先生也一起去走走如何？\x01",
            "　\x02\x03",
            "这个历史悠久的建筑里\x01",
            "可供参观的地方还真是不少呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#070F嗯，等我想散步的时候，\x01",
            "再到处溜达一下也不迟。\x02\x03",
            "我现在要去厨房看看，\x01",
            "应该还有一些剩余的食物。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#509F不会吧……还要打算吃吗？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#071F就算是吧，只是想弄点酒菜。\x01",
            "　\x02\x03",
            "王城好像有可以喝酒的小酒吧，\x01",
            "待会儿我就去瞧瞧。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x4A, 0x4, 0x2)
    OP_28(0x4A, 0x4, 0x4)
    OP_28(0x4A, 0x1, 0x1)
    OP_28(0x4A, 0x1, 0x2)
    OP_28(0x4A, 0x1, 0x4)
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    OP_4B(0xD, 255)
    EventEnd(0x0)
    Return()

    # Function_15_5020 end

    def Function_16_5698(): pass

    label("Function_16_5698")

    EventBegin(0x0)
    OP_6D(-79060, 0, 5600, 0)
    RemoveParty(0x7, 0xFF)
    SetChrPos(0x101, -79060, 0, 9840, 0)
    SetChrPos(0x102, -79060, 0, 9840, 0)
    OP_6F(0x1D, 60)

    def lambda_56DD():
        OP_8E(0xFE, 0xFFFECB2C, 0x0, 0x157C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_56DD)
    Sleep(600)

    def lambda_56FD():
        OP_8E(0xFE, 0xFFFECB2C, 0x0, 0x1900, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_56FD)
    WaitChrThread(0x101, 0x1)

    def lambda_571D():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_571D)
    WaitChrThread(0x102, 0x1)

    def lambda_5730():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5730)
    OP_72(0x1D, 0x800)
    OP_22(0x7, 0x0, 0x64)
    OP_70(0x1D, 0x0)
    OP_73(0x1D)
    OP_71(0x1D, 0x800)

    ChrTalk(
        0x101,
        (
            "#007F#4P呼～……\x01",
            "真是出乎预料的事啊。\x02\x03",
            "越来越想见女王陛下，\x01",
            "问清楚这到底是怎么回事了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F首先按照约定去见希尔丹夫人吧。\x01",
            "　\x02\x03",
            "她应该有办法让我们见到陛下的。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F#4P嗯，好的。\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_16_5698 end

    def Function_17_586E(): pass

    label("Function_17_586E")

    EventBegin(0x0)
    OP_6D(-79390, 0, 54420, 0)
    OP_67(0, 4890, -10000, 0)
    OP_6B(1680, 0)
    OP_6C(38000, 0)
    OP_6E(509, 0)
    SetChrPos(0x101, -80040, 0, 48610, 0)
    SetChrPos(0x102, -80040, 0, 48610, 0)
    SetChrPos(0x108, -80040, 0, 48610, 0)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x108, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1500, 0)

    def lambda_5910():
        OP_6D(-79660, 0, 55810, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_5910)

    def lambda_5928():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_5928)

    def lambda_593A():
        OP_8E(0xFE, 0xFFFEC762, 0x0, 0xDA52, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_593A)
    Sleep(800)

    def lambda_595A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_595A)

    def lambda_596C():
        OP_8E(0xFE, 0xFFFEC640, 0x0, 0xD426, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_596C)
    Sleep(500)

    def lambda_598C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_598C)

    def lambda_599E():
        OP_8E(0xFE, 0xFFFECAC8, 0x0, 0xD3CC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_599E)
    WaitChrThread(0x108, 0x1)
    OP_8C(0x108, 180, 400)

    ChrTalk(
        0x108,
        (
            "#074F#5P哎呀呀……\x02\x03",
            "总算用比较擅长的手法蒙混过去了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 0x1)

    ChrTalk(
        0x101,
        (
            "#004F#6P哎……！\x02\x03",
            "金先生，你不是喝醉了吗？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F#5P那个嘛，只是演演戏而已。\x02\x03",
            "我可是一滴酒都没喝过哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009F#6P说谎！明明脸那么红……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F驱动内力，让血气上游，\x01",
            "让表面看起来一副喝醉的样子……\x02\x03",
            "#010F在东方的武术里，\x01",
            "这就是一种名为『气功』的功夫对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#073F#5P哦，这种功夫你都知道，\x01",
            "真是见多识广的年轻人啊。\x02\x03",
            "#071F哎呀，刚才看见你们遇到了麻烦，\x01",
            "所以我就忍不住叫了你们一声。\x02\x03",
            "怎么样，还算帮了点忙吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F#6P真是的，金先生你啊……\x01",
            "有时候也会让人捉摸不透呢～\x02\x03",
            "#509F虽说是来帮我们解围的，\x01",
            "但着实吓了人家一跳呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#071F#5P哈哈，抱歉抱歉。\x02\x03",
            "#070F那么，情况怎么样？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F#6P？？？\x02\x03",
            "什么怎么样呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F#5P已经办完了吧。\x02\x03",
            "和女王陛下见面的事情。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#005F#3S#6P怎、怎么会～！？\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#580F#6P为、为、为什么金先生你知道！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F难道说这件事您是从\x01",
            "艾南先生那里听说的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F#5P协会那个小哥并没有告诉我什么。\x01",
            "　\x02\x03",
            "#071F我只是根据自己的推断，\x01",
            "来套你们的话而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#509F#6P推、推断……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F……没有任何的情报，\x01",
            "是不可能做出这样的推断的。\x02\x03",
            "#012F金先生……\x01",
            "请问您究竟知道些什么？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#074F#5P嗯……\x02\x03",
            "也该是把那个东西\x01",
            "拿给你们看看的时候了。\x02",
        )
    )

    CloseMessageWindow()
    OP_92(0x108, 0x101, 0x320, 0x7D0, 0x0)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "金将一封信递给了艾丝蒂尔。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_8F(0x108, 0xFFFEC762, 0x0, 0xDA52, 0x7D0, 0x0)

    ChrTalk(
        0x101,
        "#004F#6P一、一封信……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F这个笔迹是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F#5P嗯，没错。\x01",
            "你们先拿来读一读吧。\x02\x03",
            "然后就知道怎么回事了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505F#6P嗯、嗯……\x02",
    )

    CloseMessageWindow()
    OP_1F(0x50, 0x1F4)
    FadeToDark(300, 0, 100)
    Sleep(500)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "金·瓦赛克阁下敬启。\x01",
            "久疏问候，身体可好。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "由于事出匆忙，\x01",
            "我唯有采取开门见山的方式，万望见谅。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "事实上，连同猎兵团在内的事件\x01",
            "已经朝向帝国方向发展了。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "可是，利贝尔国内似乎正有\x01",
            "一股微妙的势力正在滋长蔓延着。\x01",
            "若只是交给年轻人去处理，我有些放心不下。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "我想请你帮忙。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "在我外出的时候，请你到利贝尔来，\x01",
            "如果有什么情况发生的话，\x01",
            "就帮帮那些年轻人，可以吗？\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "因为你是第一次前往利贝尔，\x01",
            "所以顺便游山玩水也是不错的选择。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "女王诞辰庆典前夕，\x01",
            "会举办一场允许外国人参加的武术大会，\x01",
            "这是一个能了解形势的好机会。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "突然提出这样的请求，或许让你有些为难。\x01",
            "不过如果你有空的话，还请帮帮忙。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "女王诞辰庆典之时我会回来，\x01",
            "到那时我再一并向你感谢。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "卡西乌斯·布莱特\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "另：\x01",
            "你也许会有机会\x01",
            "见到我的女儿和儿子。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "我让他们在游击士协会实习，\x01",
            "当时没有想太多，只是锻炼一下他们。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "如果他们有什么事，\x01",
            "还请您助他们一臂之力，帮他们摆脱困境。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_1F(0x64, 0x1F4)
    Sleep(500)

    ChrTalk(
        0x101,
        "#580F#6P……这、这是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F金先生是受父亲委托来利贝尔的……\x01",
            "　\x02\x03",
            "#010F这么说父亲他现在……\x01",
            "正在埃雷波尼亚帝国了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#074F#5P嗯，就是这样的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#509F#6P什么叫就是这样的……\x02\x03",
            "关、关键的是金先生嘛。\x01",
            "哼哼，你竟然和老爸串通一气！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F#5P串通一气什么的不太好听啊。\x02\x03",
            "以前卡西乌斯大人来到我们卡尔瓦德时，\x01",
            "我也受到了他诸多方面的关照啊。\x01",
            "　\x02\x03",
            "我一直都想报答他，\x01",
            "这封信正好了却了我的心愿。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007F#6P是这样啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F请问金先生是什么时候\x01",
            "发觉我们是父亲的孩子的呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F#5P第一次见面时，\x01",
            "看见艾丝蒂尔拿着棍子，\x01",
            "我就开始有些注意了……\x02\x03",
            "在询问了雾香之后我才确信。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009F#6P金先生也真是的，\x01",
            "之前连一个字也没和我们提起过……\x02\x03",
            "我们不知道老爸的行踪，\x01",
            "一直都是忧心忡忡的呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#075F#5P这一点我很抱歉。\x02\x03",
            "但是从字面上来看，\x01",
            "感觉卡西乌斯大哥到帝国的行动\x01",
            "是一定要保密才行的……\x02\x03",
            "#070F话又说回来，看来你们俩\x01",
            "已经完成了一件不小的事情对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F#6P啊，嗯……\x02\x03",
            "#006F我说约修亚，\x01",
            "现在说出来已经没问题了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F嗯，既然如此，\x01",
            "我们就向您一一道来吧。\x02\x03",
            "我们刚刚办完的事情要说起来的话，\x01",
            "可是一个很长的故事。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾丝蒂尔他们向金说明了\x01",
            "拉赛尔博士的委托以及见到艾莉茜雅女王的事情……\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "之后说明了已经接受了女王的委托，\x01",
            "要将被囚禁的科洛蒂娅公主解救出来的事情。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(
        0x108,
        (
            "#074F#5P原来如此啊……\x02\x03",
            "听了晚宴上那些话后，\x01",
            "我就感觉充满了火药味……\x02\x03",
            "#070F好的，为了完成这个委托，\x01",
            "也让我助你们一臂之力吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F#6P咦，可以吗！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F#5P啊，这是报答卡西乌斯大人\x01",
            "恩情的绝好机会呢。\x02\x03",
            "请务必让我帮忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F#6P金、金大哥……\x01",
            "我、我们俩也请你多多关照了～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F再次请您多多关照。\x02",
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_21()
    OP_A2(0x3FA)
    ClearMapFlags(0x800)
    NewScene("ED6_DT01/C4300   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_17_586E end

    SaveToFile()

Try(main)
