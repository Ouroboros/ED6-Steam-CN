from ED6ScenarioHelper import *

def main():
    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3400   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3400.x',
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
        '冈多夫',                               # 9
        '士兵儒勒',                             # 10
        '士兵埃克托尔',                         # 11
        '士兵切斯利',                           # 12
        '阿鲁姆',                               # 13
        '艾娅莉',                               # 14
        '士兵维恩',                             # 15
        '塔尔瓦托副长',                         # 16
        '桑吉特',                               # 17
        '黛米',                                 # 18
        '玛丽安',                               # 19
        '诺琪',                                 # 20
        '塔丽娅',                               # 21
        '迪鲁队长',                             # 22
        '士兵沃普',                             # 23
        '士兵欧鲁尼斯',                         # 24
        '利塔街道方向',                         # 25
        '庭园大道方向',                         # 26
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
        'ED6_DT07/CH01750 ._CH',             # 00
        'ED6_DT07/CH01640 ._CH',             # 01
        'ED6_DT07/CH01640 ._CH',             # 02
        'ED6_DT07/CH01300 ._CH',             # 03
        'ED6_DT07/CH01140 ._CH',             # 04
        'ED6_DT07/CH01150 ._CH',             # 05
        'ED6_DT07/CH01300 ._CH',             # 06
        'ED6_DT07/CH01300 ._CH',             # 07
        'ED6_DT07/CH01520 ._CH',             # 08
        'ED6_DT07/CH01350 ._CH',             # 09
        'ED6_DT07/CH01210 ._CH',             # 0A
        'ED6_DT07/CH01230 ._CH',             # 0B
        'ED6_DT07/CH01180 ._CH',             # 0C
        'ED6_DT07/CH01310 ._CH',             # 0D
        'ED6_DT07/CH01640 ._CH',             # 0E
    )

    AddCharChipPat(
        'ED6_DT07/CH01750P._CP',             # 00
        'ED6_DT07/CH01640P._CP',             # 01
        'ED6_DT07/CH01640P._CP',             # 02
        'ED6_DT07/CH01300P._CP',             # 03
        'ED6_DT07/CH01140P._CP',             # 04
        'ED6_DT07/CH01150P._CP',             # 05
        'ED6_DT07/CH01300P._CP',             # 06
        'ED6_DT07/CH01300P._CP',             # 07
        'ED6_DT07/CH01520P._CP',             # 08
        'ED6_DT07/CH01350P._CP',             # 09
        'ED6_DT07/CH01210P._CP',             # 0A
        'ED6_DT07/CH01230P._CP',             # 0B
        'ED6_DT07/CH01180P._CP',             # 0C
        'ED6_DT07/CH01310P._CP',             # 0D
        'ED6_DT07/CH01640P._CP',             # 0E
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
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
        TalkScenaIndex      = 15,
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
        TalkScenaIndex      = 16,
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
        TalkScenaIndex      = 17,
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
        TalkScenaIndex      = 18,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
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
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 35300,
        Z                   = 0,
        Y                   = -3600,
        Direction           = 92,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 35310,
        Z                   = 0,
        Y                   = 3610,
        Direction           = 92,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -37360,
        Z                   = 0,
        Y                   = 960,
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

    DeclNpc(
        X                   = 83520,
        Z                   = 0,
        Y                   = 630,
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


    ScpFunction(
        "Function_0_362",          # 00, 0
        "Function_1_6E8",          # 01, 1
        "Function_2_736",          # 02, 2
        "Function_3_74C",          # 03, 3
        "Function_4_770",          # 04, 4
        "Function_5_C22",          # 05, 5
        "Function_6_138B",         # 06, 6
        "Function_7_138C",         # 07, 7
        "Function_8_138D",         # 08, 8
        "Function_9_138E",         # 09, 9
        "Function_10_138F",        # 0A, 10
        "Function_11_1390",        # 0B, 11
        "Function_12_1391",        # 0C, 12
        "Function_13_1392",        # 0D, 13
        "Function_14_1393",        # 0E, 14
        "Function_15_18A1",        # 0F, 15
        "Function_16_1C49",        # 10, 16
        "Function_17_20D0",        # 11, 17
        "Function_18_2BE0",        # 12, 18
        "Function_19_2E14",        # 13, 19
        "Function_20_30AB",        # 14, 20
        "Function_21_36C4",        # 15, 21
    )


    def Function_0_362(): pass

    label("Function_0_362")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (106, "loc_36E"),
        (SWITCH_DEFAULT, "loc_384"),
    )


    label("loc_36E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_381")
    OP_A2(0x605)
    Event(0, 20)

    label("loc_381")

    Jump("loc_384")

    label("loc_384")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_38E")
    Jump("loc_436")

    label("loc_38E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_3AE")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 9970, 0, 6140, 257)
    Jump("loc_436")

    label("loc_3AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_3B8")
    Jump("loc_436")

    label("loc_3B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_3C2")
    Jump("loc_436")

    label("loc_3C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_3CC")
    Jump("loc_436")

    label("loc_3CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_3D6")
    Jump("loc_436")

    label("loc_3D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_3E0")
    Jump("loc_436")

    label("loc_3E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_3EA")
    Jump("loc_436")

    label("loc_3EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_3F4")
    Jump("loc_436")

    label("loc_3F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_419")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 9970, 0, 6140, 257)
    SetChrFlags(0x8, 0x10)
    Jump("loc_436")

    label("loc_419")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_436")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 3560, 0, -430, 90)

    label("loc_436")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_456")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 15080, 11750, -60, 276)
    Jump("loc_6E7")

    label("loc_456")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_476")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 15080, 11750, -60, 276)
    Jump("loc_6E7")

    label("loc_476")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_496")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 15080, 11750, -60, 276)
    Jump("loc_6E7")

    label("loc_496")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_4B6")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 15080, 11750, -60, 276)
    Jump("loc_6E7")

    label("loc_4B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_4D6")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 15080, 11750, -60, 276)
    Jump("loc_6E7")

    label("loc_4D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_END)), "loc_4F6")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 15080, 11750, -60, 276)
    Jump("loc_6E7")

    label("loc_4F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 5)), scpexpr(EXPR_END)), "loc_516")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 15080, 11750, -60, 276)
    Jump("loc_6E7")

    label("loc_516")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_562")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 10640, 0, -3930, 285)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 10660, 0, 3380, 263)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 15080, 11750, -60, 276)
    Jump("loc_6E7")

    label("loc_562")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_5AE")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 10640, 0, -3930, 285)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 10660, 0, 3380, 263)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 15080, 11750, -60, 276)
    Jump("loc_6E7")

    label("loc_5AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_5FA")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 10640, 0, -3930, 285)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 10660, 0, 3380, 263)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 15080, 11750, -60, 276)
    Jump("loc_6E7")

    label("loc_5FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_672")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 10640, 0, -3930, 285)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 10660, 0, 3380, 263)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 15080, 11750, -60, 276)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 26240, 7250, -33770, 101)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 26260, 7250, -34450, 85)
    Jump("loc_6E7")

    label("loc_672")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_6E7")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 10640, 0, -3930, 285)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 10660, 0, 3380, 263)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 15080, 11750, -60, 276)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 26240, 7250, -33770, 101)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 26260, 7250, -34450, 85)

    label("loc_6E7")

    Return()

    # Function_0_362 end

    def Function_1_6E8(): pass

    label("Function_1_6E8")

    OP_16(0x2, 0xFA0, 0xFFFE65D8, 0xFFFE0C00, 0x30056)
    OP_6F(0x0, 160)
    OP_6F(0x1, 160)
    OP_72(0x0, 0x10)
    OP_72(0x1, 0x10)
    OP_1C(0x2, 0x0, 0x15)
    OP_1C(0x3, 0x0, 0x15)
    OP_1C(0x4, 0x0, 0x15)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x11C), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_735")
    OP_28(0x2A, 0x1, 0x8000)

    label("loc_735")

    Return()

    # Function_1_6E8 end

    def Function_2_736(): pass

    label("Function_2_736")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_74B")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_736")

    label("loc_74B")

    Return()

    # Function_2_736 end

    def Function_3_74C(): pass

    label("Function_3_74C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_76F")
    OP_8D(0xFE, 7090, 6400, -600, -6500, 1500)
    Jump("Function_3_74C")

    label("loc_76F")

    Return()

    # Function_3_74C end

    def Function_4_770(): pass

    label("Function_4_770")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_81E")

    ChrTalk(
        0xFE,
        (
            "听前辈说起过，\x01",
            "国境守备队的摩尔根将军\x01",
            "是个很可怕的人呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但他毕竟是个\x01",
            "在教科书中也提到的名人，\x01",
            "一定是个很了不起的人吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C1E")

    label("loc_81E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_8B2")

    ChrTalk(
        0xFE,
        (
            "亲卫队里\x01",
            "似乎也聚集着一群\x01",
            "和特务部队一样强的人呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "要是被那样的家伙们袭击……\x01",
            "光是这么想想\x01",
            "就觉得很恐怖了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C1E")

    label("loc_8B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_A1C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_94F")

    ChrTalk(
        0xFE,
        (
            "王国军的\x01",
            "警戒等级提高了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "队长说这里也有\x01",
            "被袭击的可能性。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A19")

    label("loc_94F")

    OP_A2(0xE)

    ChrTalk(
        0xFE,
        (
            "王国军的\x01",
            "警戒等级提高了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "队长说这里也有\x01",
            "被袭击的可能性。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这……这么一来，\x01",
            "我现在连看守也觉得紧张了！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A19")

    Jump("loc_C1E")

    label("loc_A1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_A95")

    ChrTalk(
        0xFE,
        "武术大会的正式赛是从今天开始吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在我小的时候，\x01",
            "妈妈经常带我\x01",
            "去竞技场看比赛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C1E")

    label("loc_A95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_B21")

    ChrTalk(
        0xFE,
        (
            "呼～\x01",
            "之前刚进行了防恐怖袭击训练，\x01",
            "还没有从疲劳中恢复呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是，现在是非常时期，\x01",
            "不振作起来不行啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C1E")

    label("loc_B21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 7)), scpexpr(EXPR_END)), "loc_B7D")

    ChrTalk(
        0xFE,
        (
            "快要到诞辰庆典了，\x01",
            "要是能早点抓住恐怖分子就好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C1E")

    label("loc_B7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_END)), "loc_C17")

    ChrTalk(
        0xFE,
        (
            "我是刚刚被分配\x01",
            "到这里的守备队来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这里有很多严厉的前辈，\x01",
            "弄得我一天到晚都很紧张。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C1E")

    label("loc_C17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 5)), scpexpr(EXPR_END)), "loc_C1E")

    label("loc_C1E")

    TalkEnd(0xFE)
    Return()

    # Function_4_770 end

    def Function_5_C22(): pass

    label("Function_5_C22")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_D94")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_CD6")

    ChrTalk(
        0xFE,
        (
            "武术大会结束了，\x01",
            "但是还有诞辰庆典，\x01",
            "不能松懈啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为不知道恐怖分子\x01",
            "什么时候会袭击过来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D91")

    label("loc_CD6")

    OP_A2(0xF)

    ChrTalk(
        0xFE,
        "没有异常！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "武术大会结束了，\x01",
            "但是还有诞辰庆典，\x01",
            "不能松懈啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为不知道恐怖分子\x01",
            "什么时候会袭击过来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D91")

    Jump("loc_1387")

    label("loc_D94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_E2D")

    ChrTalk(
        0xFE,
        (
            "最近队长和副长\x01",
            "好像都在为什么而烦恼着。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "看来在军队里\x01",
            "麻烦事也不少呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1387")

    label("loc_E2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_F3D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_EAD")

    ChrTalk(
        0xFE,
        (
            "我之前一直\x01",
            "梦想当个游击士。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "直到最后还在犹豫\x01",
            "到底是要入伍还是当游击士。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F3A")

    label("loc_EAD")

    OP_A2(0xF)

    ChrTalk(
        0xFE,
        "你们是游击士吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我之前一直\x01",
            "梦想当个游击士。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "直到最后还在犹豫\x01",
            "到底是要入伍还是当游击士。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F3A")

    Jump("loc_1387")

    label("loc_F3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_1004")

    ChrTalk(
        0xFE,
        (
            "前一阵子我在周游道\x01",
            "发现了一种发光的魔兽。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他们只是一直在闪着光，\x01",
            "后来闪够了就走掉了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "真是有着\x01",
            "奇特魅力的小家伙啊！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1387")

    label("loc_1004")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1196")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_10AC")

    ChrTalk(
        0xFE,
        (
            "以前听说，\x01",
            "恐怖分子伪装成了亲卫队\x01",
            "对中央工房进行了袭击……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，实际上不就是\x01",
            "亲卫队自己犯下案件，\x01",
            "从王城中逃走失踪了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1193")

    label("loc_10AC")

    OP_A2(0xF)

    ChrTalk(
        0xFE,
        (
            "以前听说，\x01",
            "恐怖分子伪装成了亲卫队\x01",
            "对中央工房进行了袭击……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，实际上不就是\x01",
            "亲卫队自己犯下案件，\x01",
            "从王城中逃走失踪了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果要和亲卫队交战的话，\x01",
            "这里也不能保证平安无事啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1193")

    Jump("loc_1387")

    label("loc_1196")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 7)), scpexpr(EXPR_END)), "loc_122E")

    ChrTalk(
        0xFE,
        (
            "刚才通过这里的部队，\x01",
            "好像是为了抓捕恐怖分子\x01",
            "而被派遣去的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "总觉得他们趾高气扬，\x01",
            "有点让人讨厌啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1387")

    label("loc_122E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_END)), "loc_1380")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_12C8")

    ChrTalk(
        0xFE,
        (
            "说不定通缉中的\x01",
            "恐怖分子正潜藏在周围，\x01",
            "要小心点哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "当然，\x01",
            "这一带有王国军在巡逻，\x01",
            "我想应该很安全的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_137D")

    label("loc_12C8")

    OP_A2(0xF)

    ChrTalk(
        0xFE,
        "哦？你们要去王都吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "说不定通缉中的\x01",
            "恐怖分子正潜藏在周围，\x01",
            "要小心点哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "当然，\x01",
            "这一带有王国军在巡逻，\x01",
            "我想应该很安全的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_137D")

    Jump("loc_1387")

    label("loc_1380")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 5)), scpexpr(EXPR_END)), "loc_1387")

    label("loc_1387")

    TalkEnd(0xFE)
    Return()

    # Function_5_C22 end

    def Function_6_138B(): pass

    label("Function_6_138B")

    Return()

    # Function_6_138B end

    def Function_7_138C(): pass

    label("Function_7_138C")

    Return()

    # Function_7_138C end

    def Function_8_138D(): pass

    label("Function_8_138D")

    Return()

    # Function_8_138D end

    def Function_9_138E(): pass

    label("Function_9_138E")

    Return()

    # Function_9_138E end

    def Function_10_138F(): pass

    label("Function_10_138F")

    Return()

    # Function_10_138F end

    def Function_11_1390(): pass

    label("Function_11_1390")

    Return()

    # Function_11_1390 end

    def Function_12_1391(): pass

    label("Function_12_1391")

    Return()

    # Function_12_1391 end

    def Function_13_1392(): pass

    label("Function_13_1392")

    Return()

    # Function_13_1392 end

    def Function_14_1393(): pass

    label("Function_14_1393")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_178C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 7)), scpexpr(EXPR_END)), "loc_140E")
    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "呼……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唉，要消灭的魔兽太多，\x01",
            "还真是麻烦啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "简直要累死人了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1789")

    label("loc_140E")

    OP_A2(0x57F)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1477")
    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "哟，是你们啊。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x106, 400)

    ChrTalk(
        0xFE,
        (
            "……怎么，阿加特。\x01",
            "这不是很有精神嘛！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14E2")

    label("loc_1477")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(800)
    TurnDirection(0xFE, 0x106, 400)

    ChrTalk(
        0xFE,
        (
            "哦，我还以为是谁。\x01",
            "原来是阿加特啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……怎么回事，\x01",
            "这不是很有精神嘛！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14E2")


    ChrTalk(
        0x106,
        (
            "#051F哼，\x01",
            "那种程度根本算不了什么。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哈哈哈，\x01",
            "你还是那么命大呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果不振作起来的话，\x01",
            "背上的『重剑』也会哭的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#050F冈多夫。\x01",
            "你就别说这么多废话了。\x02\x03",
            "我们还有要紧的事去做呢。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "哦，对啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "再见了，\x01",
            "博士的事就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#051F不用你说我也知道该怎么做啦。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1683")
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(
        0xFE,
        (
            "你们这些准游击士\x01",
            "也要加把劲哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1707")

    label("loc_1683")

    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(
        0xFE,
        (
            "哦，\x01",
            "你们就是那些准游击士吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "事情我都听雾香说过了。\x01",
            "你们要好好协助阿加特哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1707")


    ChrTalk(
        0x102,
        "#012F嗯，我们会谨慎行动的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F嗯……\x01",
            "你也小心行事啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 400)

    ChrTalk(
        0xFE,
        "那就拜托你们了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "愿你们得到\x01",
            "女神爱德丝的保佑。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1789")

    Jump("loc_189D")

    label("loc_178C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_189D")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_17F9")

    ChrTalk(
        0xFE,
        "呼，真是的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "王那个家伙\x01",
            "如果再能干一点的话，\x01",
            "我就会轻松很多了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_189D")

    label("loc_17F9")

    OP_A2(0x0)

    ChrTalk(
        0xFE,
        "……真是麻烦啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这边消灭魔兽的委托\x01",
            "也太多了吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过因为有不少没见过的魔兽，\x01",
            "所以工作起来还是挺有乐趣的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_189D")

    TalkEnd(0xFE)
    Return()

    # Function_14_1393 end

    def Function_15_18A1(): pass

    label("Function_15_18A1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_191A")

    ChrTalk(
        0xFE,
        "欢迎来到圣海姆门。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "要办通行手续的话，\x01",
            "要过关的话请去里面登记。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C45")

    label("loc_191A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_1A85")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_19A3")

    ChrTalk(
        0xFE,
        (
            "听到解除盘查的命令时，\x01",
            "连队长都大吃一惊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "会不会是\x01",
            "哪里弄错了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A82")

    label("loc_19A3")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "还没抓住恐怖分子，\x01",
            "就忽然下了解除盘查的命令。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然无法理解……\x01",
            "但身为军人\x01",
            "绝对不能怀疑上级的决定。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "为了王国的和平，\x01",
            "只有老老实实执行任务了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A82")

    Jump("loc_1C45")

    label("loc_1A85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_1B14")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1A9F")

    ChrTalk(
        0xFE,
        "…………………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B11")

    label("loc_1A9F")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        "…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……现在正在执勤，\x01",
            "请不要和我聊天。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "想参观的话\x01",
            "还是过一段时间比较好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B11")

    Jump("loc_1C45")

    label("loc_1B14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_1BAA")

    ChrTalk(
        0xFE,
        (
            "从这个圣海姆门\x01",
            "可以登到长城\x01",
            "『亚宁堡』的城墙上。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "要是有空的话，\x01",
            "推荐去上面看一看。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C45")

    label("loc_1BAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1C45")

    ChrTalk(
        0xFE,
        (
            "欢迎来到圣海姆门！\x01",
            "如果有事的话请往里面走。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这个大门是\x01",
            "『亚宁堡』长城遗迹的一部分。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "非常欢迎游客前来参观。\x02",
    )

    CloseMessageWindow()

    label("loc_1C45")

    TalkEnd(0xFE)
    Return()

    # Function_15_18A1 end

    def Function_16_1C49(): pass

    label("Function_16_1C49")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_1CC2")

    ChrTalk(
        0xFE,
        (
            "啊，\x01",
            "难道你们是去参加诞辰庆典的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "其他的游客们\x01",
            "都已经去了哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20CC")

    label("loc_1CC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_1E07")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1D4D")

    ChrTalk(
        0xFE,
        (
            "难道说，\x01",
            "恐怖分子已经抓到了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "可是就算是这样，\x01",
            "也要向我们通知一声啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……算了，光是想也没用，\x01",
            "还是不要管了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E04")

    label("loc_1D4D")

    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "哟，盘查已经解除了哦。\x01",
            "到底是怎么回事啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "算了，我们这种小兵\x01",
            "也不可能知道内幕的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不管怎么说，\x01",
            "累人的任务结束了不是正好吗。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E04")

    Jump("loc_20CC")

    label("loc_1E07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_1EBA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1E4D")

    ChrTalk(
        0xFE,
        (
            "要是在这里徘徊的话\x01",
            "说不定会被抓起来呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EB7")

    label("loc_1E4D")

    OP_A2(0x2)

    ChrTalk(
        0xFE,
        "……啊，对不起。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "中央工房发生了一些事情，\x01",
            "现在需要进行盘查。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EB7")

    Jump("loc_20CC")

    label("loc_1EBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_2077")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1F37")

    ChrTalk(
        0xFE,
        (
            "如此雄伟的城墙\x01",
            "竟然是在没有导力的时代建造的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "真是令人佩服啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2074")

    label("loc_1F37")

    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "这座建筑拥有非常悠久的历史。\x01",
            "作为观光地也非常有名。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我们每天都能看到，\x01",
            "所以已经习以为常了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……但是，如此雄伟的城墙\x01",
            "竟然是在没有导力的时代建造的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "…………………………………\x02",
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "哦哦，我这是怎么了！\x01",
            "说着说着我又开始感叹了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2074")

    Jump("loc_20CC")

    label("loc_2077")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_20CC")

    ChrTalk(
        0xFE,
        "你们好，有什么事吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "队长就在这里面。\x01",
            "遇到麻烦的话就去找他吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20CC")

    TalkEnd(0xFE)
    Return()

    # Function_16_1C49 end

    def Function_17_20D0(): pass

    label("Function_17_20D0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_214C")

    ChrTalk(
        0xFE,
        (
            "从那以后，\x01",
            "蔡斯那边就好像\x01",
            "再没出现过恐怖事件了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "或许恐怖分子\x01",
            "已经逃到别的地方去了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BDC")

    label("loc_214C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_21CD")

    ChrTalk(
        0xFE,
        "决赛马上就要开始了呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我也是王国军的士兵，\x01",
            "所以当然要去\x01",
            "声援特务部队呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BDC")

    label("loc_21CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_2247")

    ChrTalk(
        0xFE,
        (
            "现在格兰赛尔的街上\x01",
            "应该很热闹吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "要是能早点抓住\x01",
            "恐怖分子就好了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BDC")

    label("loc_2247")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_22FD")

    ChrTalk(
        0xFE,
        "我也想参加一次武术大会。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是不在军队的预选赛中胜出的话，\x01",
            "就没有出场的资格。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BDC")

    label("loc_22FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_235E")

    ChrTalk(
        0xFE,
        (
            "唉呀，一直保持警戒状态，\x01",
            "都快累死了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "肩膀已经酸痛得不行了……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2BDC")

    label("loc_235E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_END)), "loc_23CC")

    ChrTalk(
        0xFE,
        (
            "那边的那个人\x01",
            "是学者还是别的什么人呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这个『亚宁堡』\x01",
            "也是相当古老的遗迹，\x01",
            "经常会有人来考察的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BDC")

    label("loc_23CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 5)), scpexpr(EXPR_END)), "loc_2531")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_247F")

    ChrTalk(
        0xFE,
        (
            "之前我看见了一艘陌生的飞艇，\x01",
            "于是就向队长汇报了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是上面的人\x01",
            "好像什么反应也没有。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那个果然是\x01",
            "试飞中的新型艇之类的吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_252E")

    label("loc_247F")

    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "上次看到了一艘\x01",
            "样子很奇怪的飞艇，\x01",
            "于是就向队长汇报了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是上面的人\x01",
            "好像什么反应也没有。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唉，我还以为立了功。\x01",
            "真是个傻瓜。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_252E")

    Jump("loc_2BDC")

    label("loc_2531")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_2701")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_25F5")

    ChrTalk(
        0xFE,
        (
            "那艘没见过的飞艇\x01",
            "向西边飞去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "说起西边，\x01",
            "那是雷斯顿要塞的方向……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "说不定是在\x01",
            "测试新型飞艇吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26FE")

    label("loc_25F5")

    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "昨天晚上，在西边的天空，\x01",
            "我看见了一艘陌生的飞艇。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我觉得应该和事件有关系，\x01",
            "就向队长汇报了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "盘查都已经解除了，\x01",
            "以后说不定就不再搜查了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26FE")

    Jump("loc_2BDC")

    label("loc_2701")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_2882")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_27A1")

    ChrTalk(
        0xFE,
        (
            "要是让恐怖分子逃跑了，\x01",
            "守备队的面子可就丢尽了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不能松懈的日子\x01",
            "好像还要一直持续下去呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_287F")

    label("loc_27A1")

    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "感觉犯人随时会从这茂密的树林中蹿出来，\x01",
            "真让人感到不安啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "要是让恐怖分子逃跑了，\x01",
            "守备队的面子可就丢尽了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不能松懈的日子\x01",
            "好像还要一直持续下去呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_287F")

    Jump("loc_2BDC")

    label("loc_2882")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_2A49")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2944")

    ChrTalk(
        0xFE,
        (
            "就因为每天\x01",
            "都这样眺望地平线，\x01",
            "眼力也变的太过敏锐了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因此经常让\x01",
            "当地的朋友感到不愉快。\x01",
            "这也是一种职业病吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A46")

    label("loc_2944")

    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "我们不是每天\x01",
            "都要这样眺望地平线吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "正因如此，\x01",
            "眼力也变的过于敏锐了。\x01",
            "经常让当地的朋友感到不愉快。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这也是一种职业病吧。\x01",
            "我们可不是在打什么坏主意哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A46")

    Jump("loc_2BDC")

    label("loc_2A49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2BDC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2AC8")

    ChrTalk(
        0xFE,
        "微风迎面吹来，心情真不错。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "今天的天气不错，\x01",
            "连卡鲁迪亚丘陵也能清楚地看到。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BDC")

    label("loc_2AC8")

    OP_A2(0x3)

    ChrTalk(
        0xFE,
        "今天的利贝尔王国也很和平啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果说哪里有问题的话，\x01",
            "那就是和平过了头，都让人想睡觉了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "呼啊啊啊……\x02",
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 1700, 0x1C, 0x21, 0xFA, 0x0)
    Sleep(3000)
    OP_63(0xB)
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_62(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(
        0xFE,
        (
            "糟、糟了……\x01",
            "都支撑不到交接班了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BDC")

    TalkEnd(0xFE)
    Return()

    # Function_17_20D0 end

    def Function_18_2BE0(): pass

    label("Function_18_2BE0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_2BED")
    Jump("loc_2E10")

    label("loc_2BED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_2BF7")
    Jump("loc_2E10")

    label("loc_2BF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_2C01")
    Jump("loc_2E10")

    label("loc_2C01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_2C82")

    ChrTalk(
        0xFE,
        "啊啊～真是幸福啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在环境这么优美的地方\x01",
            "和最爱的人在一起……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "啊啊～眼前整个世界都在闪闪发光。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E10")

    label("loc_2C82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2E10")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2D0E")

    ChrTalk(
        0xFE,
        (
            "其实我完全不记得\x01",
            "周游道的景色是什么样子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呵呵，\x01",
            "那是因为一直在注视着她嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E10")

    label("loc_2D0E")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "为了参观女王诞辰庆典，\x01",
            "我们从洛连特旅行来到这里……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "难得来一次，\x01",
            "我就邀请她一起到艾尔贝周游道散步。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呵呵呵，在美丽的树林中和她牵着手，\x01",
            "只有两个人的世界……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "啊啊，\x01",
            "简直就像做梦一样啊！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E10")

    TalkEnd(0xFE)
    Return()

    # Function_18_2BE0 end

    def Function_19_2E14(): pass

    label("Function_19_2E14")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_2E21")
    Jump("loc_30A7")

    label("loc_2E21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_2E2B")
    Jump("loc_30A7")

    label("loc_2E2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_2E35")
    Jump("loc_30A7")

    label("loc_2E35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_2F09")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2EA6")

    ChrTalk(
        0xFE,
        (
            "说起来，\x01",
            "这座城墙真是好壮观啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "和威尔特桥的关口\x01",
            "简直是天壤之别。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F06")

    label("loc_2EA6")

    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "才刚刚开始交往就一起出来旅行，\x01",
            "稍微感到有些不安……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呵呵，但是我相信他。\x01",
            "跟着他一起来真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F06")

    Jump("loc_30A7")

    label("loc_2F09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_30A7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2F9B")

    ChrTalk(
        0xFE,
        (
            "和他在周游道上散步，\x01",
            "那真是美丽的绿色小道啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我们两个人简直像是\x01",
            "进入了童话中的世界一样。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30A7")

    label("loc_2F9B")

    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "和他在周游道上散步，\x01",
            "那真是美丽的绿色小道啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "沉稳颜色的石头路，\x01",
            "弥漫着历史氛围和浪漫感……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我们两个人简直像是\x01",
            "进入了童话中的世界一样。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "呀～就像是变成了苍骑士奥斯卡\x01",
            "和塞茜莉亚公主一样呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30A7")

    TalkEnd(0xFE)
    Return()

    # Function_19_2E14 end

    def Function_20_30AB(): pass

    label("Function_20_30AB")

    EventBegin(0x0)
    OP_6D(29440, 0, 4420, 0)
    OP_67(0, 9960, -10000, 0)
    OP_6B(10000, 0)
    OP_6C(62000, 0)
    OP_6E(262, 0)
    StopSound(0x88B8, 0x61A80, 0x0)
    SetChrPos(0x101, -11860, 0, 1880, 0)
    SetChrPos(0x102, -11610, 0, 330, 0)
    FadeToBright(2000, 0)

    def lambda_3128():
        OP_6C(45000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3128)
    Sleep(1000)

    def lambda_313D():
        OP_6D(7000, 0, 4630, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_313D)
    Sleep(2000)

    def lambda_315A():
        OP_8E(0xFE, 0x67C, 0x0, 0x5E6, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_315A)
    Sleep(600)

    def lambda_317A():
        OP_8E(0xFE, 0x67C, 0x0, 0xFFFFFF38, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_317A)
    WaitChrThread(0x101, 0x2)
    Fade(500)
    OP_6D(4040, 0, -300, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3250, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    StopSound(0x88B8, 0x249F0, 0x0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x102, 0x1)

    ChrTalk(
        0x101,
        (
            "#006F#1P这里就是圣海姆门啊……\x02\x03",
            "总觉得看起来\x01",
            "和洛连特地区的格鲁纳门很像。\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 0x1)

    ChrTalk(
        0x102,
        (
            "#010F#6P因为都是建在包围王都地区的\x01",
            "长城『亚宁堡』上的门。\x02\x03",
            "虽然是一千年以前建造的，\x01",
            "不过真不愧是阻止过帝国军队进攻的建筑，\x01",
            "坚固得简直就像监牢围墙一般啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F#1P嗯嗯，我也觉得是。\x01",
            "看上去被大炮击中都不会损坏呢。\x02\x03",
            "#501F不过，这里也是观光胜地，\x01",
            "如果有时间的话真想登上去看看啊……\x02\x03",
            "#503F………………………………\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#019F#6P哈哈，如果是你的话，\x01",
            "一定是想沿着城墙一直全力奔跑下去吧？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x101, 0x102, 600)

    ChrTalk(
        0x101,
        (
            "#005F#1P才，才不是呢！\x02\x03",
            "#503F我想的是……\x01",
            "两个人坐在上面慢慢地吃午饭……\x02\x03",
            "或者吹着风……\x01",
            "谈些各种各样的话题之类的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#6P？？？\x02\x03",
            "为什么突然想起\x01",
            "这些平时经常做的事呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1200)

    ChrTalk(
        0x101,
        (
            "#007F#1P唉……算了。\x02\x03",
            "总之快点办完通行手续，\x01",
            "加快脚步去王都吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F#6P嗯……\x01",
            "是我神经过敏吗。\x02\x03",
            "你是不是心情不好啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#509F#1P的确是你神经过敏。\x02\x03",
            "哎呀～别再说无谓的话了。\x01",
            "赶、赶快进去吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#017F#6P（女孩子真是难懂啊……）\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_20_30AB end

    def Function_21_36C4(): pass

    label("Function_21_36C4")

    TalkBegin(0xFF)
    Sleep(400)
    TalkEnd(0xFF)
    Return()

    # Function_21_36C4 end

    SaveToFile()

Try(main)
