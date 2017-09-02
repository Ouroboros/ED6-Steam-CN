from ED6ScenarioHelper import *

def main():
    # 柏斯国际空港

    CreateScenaFile(
        FileName            = 'T1101   ._SN',
        MapName             = 'Bose',
        Location            = 'T1101.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60011",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/T1101   ._SN',
            'ED6_DT01/T1101_1 ._SN',
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
        '罗卡斯',                               # 9
        '爱蕾吉娅',                             # 10
        '哈里',                                 # 11
        '米娜',                                 # 12
        '雅哈多老人',                           # 13
        '马尔科',                               # 14
        '雷塔',                                 # 15
        '法娜',                                 # 16
        '梅贝尔市长',                           # 17
        '奈尔',                                 # 18
        '朵洛希',                               # 19
        '莉拉',                                 # 20
        '哈尔德',                               # 21
        '西柏斯街道方向',                       # 22
        '东柏斯街道方向',                       # 23
        '柏斯市·南街区',                       # 24
        '柏斯国际空港',                         # 25
    )

    DeclEntryPoint(
        Unknown_00              = 35000,
        Unknown_04              = 0,
        Unknown_08              = 16000,
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
        'ED6_DT07/CH01140 ._CH',             # 00
        'ED6_DT07/CH01150 ._CH',             # 01
        'ED6_DT07/CH01160 ._CH',             # 02
        'ED6_DT07/CH01170 ._CH',             # 03
        'ED6_DT07/CH01000 ._CH',             # 04
        'ED6_DT07/CH01100 ._CH',             # 05
        'ED6_DT07/CH02360 ._CH',             # 06
        'ED6_DT07/CH02060 ._CH',             # 07
        'ED6_DT07/CH02070 ._CH',             # 08
        'ED6_DT07/CH02370 ._CH',             # 09
        'ED6_DT07/CH01120 ._CH',             # 0A
        'ED6_DT07/CH01040 ._CH',             # 0B
        'ED6_DT07/CH01053 ._CH',             # 0C
    )

    AddCharChipPat(
        'ED6_DT07/CH01140P._CP',             # 00
        'ED6_DT07/CH01150P._CP',             # 01
        'ED6_DT07/CH01160P._CP',             # 02
        'ED6_DT07/CH01170P._CP',             # 03
        'ED6_DT07/CH01000P._CP',             # 04
        'ED6_DT07/CH01100P._CP',             # 05
        'ED6_DT07/CH02360P._CP',             # 06
        'ED6_DT07/CH02060P._CP',             # 07
        'ED6_DT07/CH02070P._CP',             # 08
        'ED6_DT07/CH02370P._CP',             # 09
        'ED6_DT07/CH01120P._CP',             # 0A
        'ED6_DT07/CH01040P._CP',             # 0B
        'ED6_DT07/CH01053P._CP',             # 0C
    )

    DeclNpc(
        X                   = 64280,
        Z                   = 0,
        Y                   = 52300,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 63060,
        Z                   = 0,
        Y                   = 49000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 36520,
        Z                   = 0,
        Y                   = 52210,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 36520,
        Z                   = 0,
        Y                   = 51220,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 48310,
        Z                   = 0,
        Y                   = 46460,
        Direction           = 262,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 66100,
        Z                   = 0,
        Y                   = 62200,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 67500,
        Z                   = 0,
        Y                   = 52540,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 69170,
        Z                   = 0,
        Y                   = 52540,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = -620,
        Z                   = -1000,
        Y                   = -3500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = -620,
        Z                   = -1000,
        Y                   = -3500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -620,
        Z                   = -1000,
        Y                   = -3500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -620,
        Z                   = -1000,
        Y                   = -3500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 23100,
        Z                   = 0,
        Y                   = 47200,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 0,
    )

    DeclNpc(
        X                   = 4530,
        Z                   = 0,
        Y                   = 45190,
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
        X                   = 87650,
        Z                   = 0,
        Y                   = 60410,
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
        X                   = 47990,
        Z                   = -3000,
        Y                   = 29310,
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
        X                   = 47940,
        Z                   = 0,
        Y                   = 93220,
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
        X                   = 17000,
        Y                   = -1000,
        Z                   = 50100,
        Range               = 18000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x9D6C,
        Unknown_18          = 0x0,
        Unknown_1C          = 17,
    )

    DeclEvent(
        X                   = 27800,
        Y                   = -1000,
        Z                   = 57900,
        Range               = 2000,
        Unknown_10          = 0x2710,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 22,
    )

    DeclEvent(
        X                   = 25200,
        Y                   = 0,
        Z                   = 57940,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 26,
    )

    DeclEvent(
        X                   = 18880,
        Y                   = 0,
        Z                   = 76030,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 27,
    )

    DeclEvent(
        X                   = 36200,
        Y                   = 0,
        Z                   = 79200,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 28,
    )

    DeclEvent(
        X                   = 59000,
        Y                   = 0,
        Z                   = 79200,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 29,
    )

    DeclEvent(
        X                   = 38540,
        Y                   = 0,
        Z                   = 59990,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 30,
    )

    DeclEvent(
        X                   = 48040,
        Y                   = 100,
        Z                   = 69500,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 30,
    )

    DeclEvent(
        X                   = 57480,
        Y                   = 0,
        Z                   = 60010,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 30,
    )

    DeclEvent(
        X                   = 48010,
        Y                   = 0,
        Z                   = 50550,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 30,
    )

    DeclEvent(
        X                   = 67340,
        Y                   = -500,
        Z                   = 73070,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 31,
    )

    DeclEvent(
        X                   = 72240,
        Y                   = 0,
        Z                   = 44910,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 32,
    )

    DeclEvent(
        X                   = 47960,
        Y                   = 0,
        Z                   = 85570,
        Range               = 1000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 33,
    )


    ScpFunction(
        "Function_0_4D2",          # 00, 0
        "Function_1_638",          # 01, 1
        "Function_2_65E",          # 02, 2
        "Function_3_7DB",          # 03, 3
        "Function_4_8D8",          # 04, 4
        "Function_5_9D5",          # 05, 5
        "Function_6_AD2",          # 06, 6
        "Function_7_12AB",         # 07, 7
        "Function_8_172A",         # 08, 8
        "Function_9_228F",         # 09, 9
        "Function_10_2DE1",        # 0A, 10
        "Function_11_38B1",        # 0B, 11
        "Function_12_3972",        # 0C, 12
        "Function_13_3B8A",        # 0D, 13
        "Function_14_3E52",        # 0E, 14
        "Function_15_3EA9",        # 0F, 15
        "Function_16_3ECC",        # 10, 16
        "Function_17_3F37",        # 11, 17
        "Function_18_412E",        # 12, 18
        "Function_19_4388",        # 13, 19
        "Function_20_4868",        # 14, 20
        "Function_21_4BE1",        # 15, 21
        "Function_22_584F",        # 16, 22
        "Function_23_644B",        # 17, 23
        "Function_24_6C4F",        # 18, 24
        "Function_25_7275",        # 19, 25
        "Function_26_7845",        # 1A, 26
        "Function_27_7849",        # 1B, 27
        "Function_28_784D",        # 1C, 28
        "Function_29_7851",        # 1D, 29
        "Function_30_7855",        # 1E, 30
        "Function_31_7859",        # 1F, 31
        "Function_32_785D",        # 20, 32
        "Function_33_7861",        # 21, 33
    )


    def Function_0_4D2(): pass

    label("Function_0_4D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_4E6")
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    Jump("loc_597")

    label("loc_4E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_4FA")
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    Jump("loc_597")

    label("loc_4FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_51C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x10, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x10, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_519")
    ClearChrFlags(0x14, 0x80)

    label("loc_519")

    Jump("loc_597")

    label("loc_51C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 7)), scpexpr(EXPR_END)), "loc_53C")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 66400, 0, 54570, 270)
    Jump("loc_597")

    label("loc_53C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_546")
    Jump("loc_597")

    label("loc_546")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_550")
    Jump("loc_597")

    label("loc_550")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_55A")
    Jump("loc_597")

    label("loc_55A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_597")
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x10)
    SetChrPos(0x10, 69070, 0, 48400, 0)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x10)
    SetChrPos(0x13, 69060, 0, 49440, 180)

    label("loc_597")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_5A5")
    OP_A3(0x3FA)
    Event(0, 20)

    label("loc_5A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_5B3")
    OP_A3(0x3FB)
    Event(0, 23)

    label("loc_5B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 4)), scpexpr(EXPR_END)), "loc_5C1")
    OP_A3(0x3FC)
    Event(0, 25)

    label("loc_5C1")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (115, "loc_5D5"),
        (110, "loc_5FA"),
        (116, "loc_611"),
        (SWITCH_DEFAULT, "loc_637"),
    )


    label("loc_5D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E4")
    OP_A2(0x307)
    Event(0, 19)

    label("loc_5E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5F7")
    OP_A2(0x313)
    Event(0, 21)

    label("loc_5F7")

    Jump("loc_637")

    label("loc_5FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_611")
    OP_A2(0x315)
    Event(0, 24)

    label("loc_611")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x10, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x10, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x10, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_637")
    OP_28(0x10, 0x3, 0x8)
    RemoveParty(0x34, 0xFF)
    Event(1, 2)

    label("loc_637")

    Return()

    # Function_0_4D2 end

    def Function_1_638(): pass

    label("Function_1_638")

    OP_16(0x2, 0xFA0, 0xFFFEC780, 0xFFFEF660, 0x30041)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x33)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_65D")
    OP_1B(0xF, 0x0, 0x10)

    label("loc_65D")

    Return()

    # Function_1_638 end

    def Function_2_65E(): pass

    label("Function_2_65E")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_683")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_7C5")

    label("loc_683")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_69C")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_7C5")

    label("loc_69C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B5")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_7C5")

    label("loc_6B5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6CE")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_7C5")

    label("loc_6CE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E7")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_7C5")

    label("loc_6E7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_700")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_7C5")

    label("loc_700")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_719")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_7C5")

    label("loc_719")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_732")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_7C5")

    label("loc_732")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_74B")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_7C5")

    label("loc_74B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_764")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_7C5")

    label("loc_764")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_77D")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_7C5")

    label("loc_77D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_796")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_7C5")

    label("loc_796")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7AF")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_7C5")

    label("loc_7AF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7C5")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_7C5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7DA")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_7C5")

    label("loc_7DA")

    Return()

    # Function_2_65E end

    def Function_3_7DB(): pass

    label("Function_3_7DB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8D7")
    OP_8E(0xFE, 0xFB18, 0x0, 0xAFFA, 0xBB8, 0x0)
    OP_8E(0xFE, 0xF6F4, 0x0, 0xAD0C, 0xBB8, 0x0)
    OP_8E(0xFE, 0xF15E, 0x0, 0xA99C, 0xBB8, 0x0)
    OP_8E(0xFE, 0x85FC, 0x0, 0xA99C, 0xBB8, 0x0)
    OP_8E(0xFE, 0x7EDF, 0x0, 0xB13A, 0xBB8, 0x0)
    OP_8E(0xFE, 0x7BE8, 0x0, 0xBA4A, 0xBB8, 0x0)
    OP_8E(0xFE, 0x7AA8, 0x0, 0x1249E, 0xBB8, 0x0)
    OP_8E(0xFE, 0x7EAE, 0x0, 0x128D6, 0xBB8, 0x0)
    OP_8E(0xFE, 0x8480, 0x0, 0x12B74, 0xBB8, 0x0)
    OP_8E(0xFE, 0xF596, 0x0, 0x12B74, 0xBB8, 0x0)
    OP_8E(0xFE, 0xF9CE, 0x0, 0x12700, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFB18, 0x0, 0x12340, 0xBB8, 0x0)
    Jump("Function_3_7DB")

    label("loc_8D7")

    Return()

    # Function_3_7DB end

    def Function_4_8D8(): pass

    label("Function_4_8D8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9D4")
    OP_8E(0xFE, 0xF654, 0x0, 0x119F4, 0x9C4, 0x0)
    OP_8E(0xFE, 0xF2A8, 0x0, 0x12214, 0x9C4, 0x0)
    OP_8E(0xFE, 0xEF74, 0x0, 0x12426, 0x9C4, 0x0)
    OP_8E(0xFE, 0x8A16, 0x0, 0x12426, 0x9C4, 0x0)
    OP_8E(0xFE, 0x839A, 0x0, 0x120A2, 0x9C4, 0x0)
    OP_8E(0xFE, 0x8048, 0x0, 0x11E36, 0x9C4, 0x0)
    OP_8E(0xFE, 0x8048, 0x0, 0xBC66, 0x9C4, 0x0)
    OP_8E(0xFE, 0x8264, 0x0, 0xB414, 0x9C4, 0x0)
    OP_8E(0xFE, 0x85E8, 0x0, 0xAFE6, 0x9C4, 0x0)
    OP_8E(0xFE, 0xEB96, 0x0, 0xAFE6, 0x9C4, 0x0)
    OP_8E(0xFE, 0xF122, 0x0, 0xB1C6, 0x9C4, 0x0)
    OP_8E(0xFE, 0xF654, 0x0, 0xB874, 0x9C4, 0x0)
    Jump("Function_4_8D8")

    label("loc_9D4")

    Return()

    # Function_4_8D8 end

    def Function_5_9D5(): pass

    label("Function_5_9D5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AD1")
    OP_8E(0xFE, 0x8E44, 0x0, 0xB57C, 0x7D0, 0x0)
    OP_8E(0xFE, 0x88F4, 0x0, 0xB770, 0x7D0, 0x0)
    OP_8E(0xFE, 0x8750, 0x0, 0xB9DC, 0x7D0, 0x0)
    OP_8E(0xFE, 0x8750, 0x0, 0x118D2, 0x7D0, 0x0)
    OP_8E(0xFE, 0x88C2, 0x0, 0x11D00, 0x7D0, 0x0)
    OP_8E(0xFE, 0x8B1A, 0x0, 0x11E4A, 0x7D0, 0x0)
    OP_8E(0xFE, 0xEA06, 0x0, 0x11E4A, 0x7D0, 0x0)
    OP_8E(0xFE, 0xEE34, 0x0, 0x11CBA, 0x7D0, 0x0)
    OP_8E(0xFE, 0xF046, 0x0, 0x11A62, 0x7D0, 0x0)
    OP_8E(0xFE, 0xF046, 0x0, 0xBB44, 0x7D0, 0x0)
    OP_8E(0xFE, 0xED62, 0x0, 0xB6EE, 0x7D0, 0x0)
    OP_8E(0xFE, 0xEB82, 0x0, 0xB57C, 0x7D0, 0x0)
    Jump("Function_5_9D5")

    label("loc_AD1")

    Return()

    # Function_5_9D5 end

    def Function_6_AD2(): pass

    label("Function_6_AD2")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_BF6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BCB")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "事情解决了，\x01",
            "好久没有这么愉快地\x01",
            "在街上散步了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "真想和对面走过来的人们\x01",
            "打个招呼啊～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "柏斯万岁，小姐万岁！\x02",
    )

    CloseMessageWindow()
    Jump("loc_BF3")

    label("loc_BCB")


    ChrTalk(
        0xFE,
        "柏斯万岁，小姐万岁！\x02",
    )

    CloseMessageWindow()

    label("loc_BF3")

    Jump("loc_12A7")

    label("loc_BF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_D7B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CD1")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "听说飞艇的失踪\x01",
            "都是空贼团干的好事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "而且他们竟然向王家\x01",
            "要求天价的赎金……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "怎么会有如此无法无天的家伙。\x02",
    )

    CloseMessageWindow()
    Jump("loc_D78")

    label("loc_CD1")


    ChrTalk(
        0xFE,
        (
            "听说飞艇的失踪\x01",
            "都是空贼团干的好事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "而且他们竟然向王家\x01",
            "要求天价的赎金……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D78")

    Jump("loc_12A7")

    label("loc_D7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_E1F")

    ChrTalk(
        0xFE,
        (
            "强盗案件也好，定期船失踪事件也好，\x01",
            "希望都能够尽快得到解决。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "最近这几个月，\x01",
            "总是发生一些让人心神不定的事情。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12A7")

    label("loc_E1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_EEB")

    ChrTalk(
        0xFE,
        (
            "本来想在超市\x01",
            "租一个摊位的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "却被告知现在暂停申请。\x01",
            "最近还真是多事之秋啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12A7")

    label("loc_EEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_F9A")

    ChrTalk(
        0xFE,
        (
            "柏斯超市\x01",
            "对于商人来说像登龙门一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果我要做生意，\x01",
            "还是要从超市开始啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12A7")

    label("loc_F9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_1138")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_110A")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "这个城市里\x01",
            "有着各种各样的商人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "首先是在这个超市\x01",
            "拥有摊位的各种商贩……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "然后就是在南街区自己\x01",
            "搭建店铺的零售商……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "还有像特里诺家和\x01",
            "博尔德家那样的贸易商……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "对了对了，\x01",
            "本市的市长也是一位大商人。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1135")

    label("loc_110A")


    ChrTalk(
        0xFE,
        (
            "这个城市里\x01",
            "有着各种各样的商人。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1135")

    Jump("loc_12A7")

    label("loc_1138")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_12A7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1223")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        "欢迎来到商业都市柏斯！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这里是利贝尔王国\x01",
            "商业最繁荣的城市。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "也是各地梦想成为\x01",
            "成功商人的奋斗者的云集之地。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我也是其中之一啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_12A7")

    label("loc_1223")


    ChrTalk(
        0xFE,
        (
            "这里是利贝尔王国\x01",
            "商业最繁荣的城市。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "也是各地梦想成为\x01",
            "成功商人的奋斗者的云集之地。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12A7")

    TalkEnd(0x8)
    Return()

    # Function_6_AD2 end

    def Function_7_12AB(): pass

    label("Function_7_12AB")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_1322")

    ChrTalk(
        0xFE,
        (
            "所有的商店\x01",
            "终于都能够进货了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这样就可以\x01",
            "尽情地购物了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1726")

    label("loc_1322")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_13B1")

    ChrTalk(
        0xFE,
        (
            "最近都没有\x01",
            "什么可以让人振奋的话题呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "去买买东西，\x01",
            "也许心情就能放松很多吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1726")

    label("loc_13B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_148A")

    ChrTalk(
        0xFE,
        (
            "南街区都是士兵，\x01",
            "现在可不是买东西的时候。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我本来想去见识一下\x01",
            "导力器工艺的，\x01",
            "不过还是去超市吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1726")

    label("loc_148A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_15B0")

    ChrTalk(
        0xFE,
        (
            "最近，\x01",
            "所有商店的商品种类都变少了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我想，\x01",
            "大概是由于定期船\x01",
            "不能前来运货的原因吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "想买的东西却买不到，\x01",
            "真是无聊啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1726")

    label("loc_15B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_164E")

    ChrTalk(
        0xFE,
        (
            "今天想去买双鞋\x01",
            "来搭配我昨天买的衣服……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "到店里瞧瞧去。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1726")

    label("loc_164E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_16BC")

    ChrTalk(
        0xFE,
        "今天要去买新衣服。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果能够找到\x01",
            "我喜欢的样式就好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1726")

    label("loc_16BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_1726")

    ChrTalk(
        0xFE,
        (
            "嘿嘿嘿，\x01",
            "今天要买些什么好呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果能够找到\x01",
            "我喜欢的衣服就好了㈱\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1726")

    TalkEnd(0x9)
    Return()

    # Function_7_12AB end

    def Function_8_172A(): pass

    label("Function_8_172A")

    TalkBegin(0xA)
    OP_4A(0xB, 255)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_1970")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_192B")
    OP_A2(0x1)
    TurnDirection(0xA, 0xB, 0)

    ChrTalk(
        0xA,
        "我说，米娜。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xA, 0)

    ChrTalk(
        0xB,
        "什么事？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "我一定会努力的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "……啊啊，是说想成为商人的事？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "这样说也没错，不过……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "那个……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "什么啊，赶快说啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "嗯，那个……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "我想成为米娜\x01",
            "理想中的那个人……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xB,
        (
            "………………………………\x01",
            "………………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "那么我就满怀期待了。\x02",
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xA,
        "啊、嗯！\x02",
    )

    CloseMessageWindow()
    OP_8C(0xB, 270, 0)
    Jump("loc_196D")

    label("loc_192B")


    ChrTalk(
        0xA,
        "（好！一定要加油！）\x02",
    )

    CloseMessageWindow()

    label("loc_196D")

    Jump("loc_2287")

    label("loc_1970")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_1AA3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A97")
    OP_A2(0x1)
    TurnDirection(0xA, 0xB, 0)

    ChrTalk(
        0xA,
        "那个……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xA, 0)

    ChrTalk(
        0xB,
        "什么事？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "米娜没有想过\x01",
            "将来要干什么事情吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "有啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "啊，什么什么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "想听？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "嗯！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "想成为大富豪的妻子。\x02",
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xA,
        "…………………………\x02",
    )

    CloseMessageWindow()
    OP_8C(0xB, 270, 0)
    Jump("loc_1AA0")

    label("loc_1A97")


    ChrTalk(
        0xA,
        "…………………………\x02",
    )

    CloseMessageWindow()

    label("loc_1AA0")

    Jump("loc_2287")

    label("loc_1AA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_1CAC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C54")
    OP_A2(0x1)
    TurnDirection(0xA, 0xB, 0)

    ChrTalk(
        0xA,
        "那个……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xA, 0)

    ChrTalk(
        0xB,
        "什么事？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "我还是想成为商人，\x01",
            "然后开一家属于自己的店。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "反正有目标\x01",
            "就是一件好事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "你自己是不是该好好考虑一下\x01",
            "怎么做才能成功呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "对、对啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "我也会在力所能及的范围里帮你的。\x02",
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xA,
        "真的？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "就这样。\x01",
            "就在力所能及的范围里哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xB, 270, 0)
    Jump("loc_1CA9")

    label("loc_1C54")


    ChrTalk(
        0xA,
        (
            "……我觉得这是米娜\x01",
            "第一次对我这么温柔地说话呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CA9")

    Jump("loc_2287")

    label("loc_1CAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_1E83")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E34")
    OP_A2(0x1)
    TurnDirection(0xA, 0xB, 0)

    ChrTalk(
        0xA,
        "我说，米娜……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xA, 0)

    ChrTalk(
        0xB,
        "什么事？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "米娜你……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "对我说话这么冷淡，\x01",
            "是不是讨厌我啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "……如果讨厌的话，\x01",
            "就不会跟你在一起了不是吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "你在害羞什么啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "我也没说喜欢你啊。\x02",
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xA,
        "哈哈，是这样啊……\x02",
    )

    CloseMessageWindow()
    OP_8C(0xB, 270, 0)
    Jump("loc_1E80")

    label("loc_1E34")


    ChrTalk(
        0xFE,
        "是这样啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "原来两个都不是啊。\x02",
    )

    CloseMessageWindow()

    label("loc_1E80")

    Jump("loc_2287")

    label("loc_1E83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_204F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FE7")
    OP_A2(0x1)
    TurnDirection(0xA, 0xB, 0)

    ChrTalk(
        0xA,
        (
            "哈啊……\x01",
            "虽然我是想成为一个商人的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "但是我不擅长算术，\x01",
            "我到底适不适合当商人呢？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xA, 0)

    ChrTalk(
        0xB,
        "不知道……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "反正，从一开始就对自己这么没自信，\x01",
            "那么以后做什么都不可能成功的。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(700)

    ChrTalk(
        0xA,
        "…………………………\x02",
    )

    CloseMessageWindow()
    OP_8C(0xB, 270, 0)
    Jump("loc_204C")

    label("loc_1FE7")

    TurnDirection(0x101, 0xA, 0)
    ClearChrFlags(0xA, 0x10)
    TurnDirection(0xA, 0x101, 0)

    ChrTalk(
        0xA,
        "我能哭一场吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F我、我觉得可以吧。\x02",
    )

    CloseMessageWindow()

    label("loc_204C")

    Jump("loc_2287")

    label("loc_204F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_2158")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2143")
    OP_A2(0x1)
    TurnDirection(0xA, 0xB, 0)

    ChrTalk(
        0xA,
        (
            "嗯～想成为商人\x01",
            "到底该怎么做才好呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xA, 0)

    ChrTalk(
        0xB,
        "不知道……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "对于在主日学校算术学得\x01",
            "一塌糊涂的人是不可能的。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(700)

    ChrTalk(
        0xA,
        "…………………………\x02",
    )

    CloseMessageWindow()
    OP_8C(0xB, 270, 0)
    Jump("loc_2155")

    label("loc_2143")


    ChrTalk(
        0xA,
        "呜呜……\x02",
    )

    CloseMessageWindow()

    label("loc_2155")

    Jump("loc_2287")

    label("loc_2158")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_2287")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2253")
    OP_A2(0x1)
    TurnDirection(0xA, 0xB, 0)

    ChrTalk(
        0xA,
        (
            "我什么时候才能成为商人，\x01",
            "住在大大的房子里呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xA, 0)

    ChrTalk(
        0xB,
        "……真是幼稚啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "商人并不是都能\x01",
            "住在大大的房子里啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(700)

    ChrTalk(
        0xA,
        "…………………………\x02",
    )

    CloseMessageWindow()
    OP_8C(0xB, 270, 0)
    Jump("loc_2287")

    label("loc_2253")


    ChrTalk(
        0xA,
        "（呜～是这样吗……）\x02",
    )

    CloseMessageWindow()

    label("loc_2287")

    OP_4B(0xB, 255)
    TalkEnd(0xA)
    Return()

    # Function_8_172A end

    def Function_9_228F(): pass

    label("Function_9_228F")

    TalkBegin(0xB)
    OP_4A(0xA, 255)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_24D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_249C")
    OP_A2(0x1)
    OP_8C(0xB, 270, 0)
    TurnDirection(0xA, 0xB, 0)

    ChrTalk(
        0xA,
        "我说，米娜。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xA, 0)

    ChrTalk(
        0xB,
        "什么事？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "我一定会努力的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "……啊啊，是说想成为商人的事？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "这样说也没错，不过……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "那个……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "什么啊，赶快说啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "嗯，那个……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "我想成为米娜\x01",
            "理想中的那个人……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xB,
        (
            "………………………………\x01",
            "………………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "那么我就满怀期待了。\x02",
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xA,
        "啊、嗯！\x02",
    )

    CloseMessageWindow()
    OP_8C(0xA, 270, 0)
    ClearChrFlags(0xB, 0x10)
    Jump("loc_24D4")

    label("loc_249C")


    ChrTalk(
        0xB,
        "不过，拥有梦想是人的自由嘛。\x02",
    )

    CloseMessageWindow()

    label("loc_24D4")

    Jump("loc_2DD9")

    label("loc_24D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_2611")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2605")
    OP_A2(0x1)
    OP_8C(0xB, 270, 0)
    TurnDirection(0xA, 0xB, 0)

    ChrTalk(
        0xA,
        "那个……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xA, 0)

    ChrTalk(
        0xB,
        "什么事？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "米娜没有想过\x01",
            "将来要干什么事情吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "有啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "啊，什么什么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "想听？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "嗯！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "想成为大富豪的妻子。\x02",
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xA,
        "…………………………\x02",
    )

    CloseMessageWindow()
    OP_8C(0xA, 270, 0)
    Jump("loc_260E")

    label("loc_2605")


    ChrTalk(
        0xB,
        "（前路漫漫啊……）\x02",
    )

    CloseMessageWindow()

    label("loc_260E")

    Jump("loc_2DD9")

    label("loc_2611")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_27EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27C9")
    OP_A2(0x1)
    OP_8C(0xB, 270, 0)
    TurnDirection(0xA, 0xB, 0)

    ChrTalk(
        0xA,
        "那个……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xA, 0)

    ChrTalk(
        0xB,
        "什么事？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "我还是想成为商人，\x01",
            "然后开一家属于自己的店。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "反正有目标\x01",
            "就是一件好事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "你自己是不是该好考虑一下\x01",
            "好怎么做才能成功呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "对、对啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "我也会在力所能及的范围里帮你的。\x02",
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xA,
        "真的？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "就这样。\x01",
            "就在力所能及的范围里哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xA, 270, 0)
    Jump("loc_27EB")

    label("loc_27C9")


    ChrTalk(
        0xB,
        "真的花了很多工夫啊……\x02",
    )

    CloseMessageWindow()

    label("loc_27EB")

    Jump("loc_2DD9")

    label("loc_27EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_299C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_297D")
    OP_A2(0x1)
    OP_8C(0xB, 270, 0)
    TurnDirection(0xA, 0xB, 0)

    ChrTalk(
        0xA,
        "我说，米娜……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xA, 0)

    ChrTalk(
        0xB,
        "什么事？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "米娜你……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "对我说话这么冷淡，\x01",
            "是不是讨厌我啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "……如果讨厌的话，\x01",
            "就不会跟你在一起了不是吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "你在害羞什么啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "我也没说喜欢你啊。\x02",
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xA,
        "哈哈，是这样啊……\x02",
    )

    CloseMessageWindow()
    OP_8C(0xA, 270, 0)
    Jump("loc_2999")

    label("loc_297D")


    ChrTalk(
        0xFE,
        "真是的……\x02",
    )

    CloseMessageWindow()

    label("loc_2999")

    Jump("loc_2DD9")

    label("loc_299C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_2B46")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B07")
    OP_A2(0x1)
    OP_8C(0xB, 270, 0)
    TurnDirection(0xA, 0xB, 0)

    ChrTalk(
        0xA,
        (
            "哈啊……\x01",
            "虽然我是想成为一个商人的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "但是我不擅长算术，\x01",
            "对我来说是不是不合适啊？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xA, 0)

    ChrTalk(
        0xB,
        "不知道……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "反正，从一开始就对自己这么没自信，\x01",
            "那么以后做什么都不可能成功的。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(800)

    ChrTalk(
        0xA,
        "…………………………\x02",
    )

    CloseMessageWindow()
    OP_8C(0xA, 270, 0)
    Jump("loc_2B43")

    label("loc_2B07")


    ChrTalk(
        0xB,
        (
            "真是的，\x01",
            "哈里就像个不折不扣的大少爷啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B43")

    Jump("loc_2DD9")

    label("loc_2B46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_2C89")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C41")
    OP_A2(0x1)
    OP_8C(0xB, 270, 0)
    TurnDirection(0xA, 0xB, 0)

    ChrTalk(
        0xA,
        (
            "嗯～想成为商人\x01",
            "到底该怎么做才好呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xA, 0)

    ChrTalk(
        0xB,
        "不知道……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "对于在主日学校算术学得\x01",
            "一塌糊涂的人是不可能的。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(700)

    ChrTalk(
        0xA,
        "…………………………\x02",
    )

    CloseMessageWindow()
    OP_8C(0xA, 270, 0)
    Jump("loc_2C86")

    label("loc_2C41")


    ChrTalk(
        0xB,
        (
            "不擅长和数字打交道的商人\x01",
            "从来没有听说过呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C86")

    Jump("loc_2DD9")

    label("loc_2C89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_2DD9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D8B")
    OP_A2(0x1)
    OP_8C(0xB, 270, 0)
    TurnDirection(0xA, 0xB, 0)

    ChrTalk(
        0xA,
        (
            "我什么时候才能成为商人，\x01",
            "住在大大的房子里呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xA, 0)

    ChrTalk(
        0xB,
        "……真是幼稚啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "商人并不是都能\x01",
            "住在大大的房子里啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(700)

    ChrTalk(
        0xA,
        "…………………………\x02",
    )

    CloseMessageWindow()
    OP_8C(0xA, 270, 0)
    Jump("loc_2DD9")

    label("loc_2D8B")


    ChrTalk(
        0xB,
        (
            "现实并不像\x01",
            "想象那样简单。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "这样教训他一下，\x01",
            "也是为他好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DD9")

    OP_4B(0xA, 255)
    TalkEnd(0xB)
    Return()

    # Function_9_228F end

    def Function_10_2DE1(): pass

    label("Function_10_2DE1")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_2F8F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EE7")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "柏斯和卢安之间的古罗尼连峰\x01",
            "是个很危险的地方。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "是由峭壁山岩林立的\x01",
            "险峻的山峰连绵而成。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果没做好准备的话\x01",
            "最好不要踏足那里。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F8C")

    label("loc_2EE7")


    ChrTalk(
        0xFE,
        (
            "柏斯和卢安之间的古罗尼连峰\x01",
            "是个很危险的地方。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果没做好准备的话\x01",
            "最好不要踏足那里。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F8C")

    Jump("loc_38AD")

    label("loc_2F8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_3162")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30A6")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "柏斯地区的东北方\x01",
            "有一个被称为迷雾峡谷的地方。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那里全年都\x01",
            "掩盖在迷漫的大雾之中……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在那种地形错综复杂的山谷中，\x01",
            "可以看到许多平时见不到的奇观。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_315F")

    label("loc_30A6")


    ChrTalk(
        0xFE,
        (
            "柏斯地区的东北方\x01",
            "有一个被称为迷雾峡谷的地方。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在那种地形错综复杂的山谷中，\x01",
            "可以看到许多平时见不到的奇观。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_315F")

    Jump("loc_38AD")

    label("loc_3162")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_3215")

    ChrTalk(
        0xFE,
        (
            "没想到不是游击士，\x01",
            "而是由边境军队亲自出马……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "强盗案件和定期船失踪\x01",
            "是不是存在着什么内在的关系呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38AD")

    label("loc_3215")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_340B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3337")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        "拉文努村的水果真的是绝品。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果说洛连特的蔬菜最好的话，\x01",
            "那么水果就要数柏斯了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这也是我们\x01",
            "柏斯市民的骄傲吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3408")

    label("loc_3337")


    ChrTalk(
        0xFE,
        (
            "如果说洛连特的蔬菜最好的话，\x01",
            "那么水果就要数柏斯了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这也是我们\x01",
            "柏斯市民的骄傲吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3408")

    Jump("loc_38AD")

    label("loc_340B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_35AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3510")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "说起摩尔根将军，\x01",
            "他可是在百日战争中非常活跃的人物啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哈肯大门可谓是\x01",
            "王国军事上最重要的地方……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他把边境军队\x01",
            "驻扎在那里也是理所当然的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35AB")

    label("loc_3510")


    ChrTalk(
        0xFE,
        (
            "说起摩尔根将军，\x01",
            "他可是在百日战争中非常活跃的猛将啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他把边境军队\x01",
            "驻扎在那里也是理所当然的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35AB")

    Jump("loc_38AD")

    label("loc_35AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_373D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36A2")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "梅贝尔市长虽然年轻，\x01",
            "不过作为商人却很有手段。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "政治手腕也很高明，\x01",
            "真是我们市民的骄傲啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呵呵呵，\x01",
            "而且还是个美人呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_373A")

    label("loc_36A2")


    ChrTalk(
        0xFE,
        (
            "梅贝尔市长虽然年轻，\x01",
            "不过作为商人却很有手段。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "政治手腕也很高明，\x01",
            "真是我们市民的骄傲啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_373A")

    Jump("loc_38AD")

    label("loc_373D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_38AD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_385B")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "柏斯可是一个不输给\x01",
            "王都格兰赛尔的繁荣都市。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这里与帝国保持着频繁的交易，\x01",
            "而且物产也算丰富。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呵呵呵，\x01",
            "像柏斯超市那样的场所\x01",
            "王都格兰赛尔可是没有哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38AD")

    label("loc_385B")


    ChrTalk(
        0xFE,
        (
            "呵呵呵，\x01",
            "像柏斯超市那样的场所\x01",
            "王都格兰赛尔可是没有哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38AD")

    TalkEnd(0xC)
    Return()

    # Function_10_2DE1 end

    def Function_11_38B1(): pass

    label("Function_11_38B1")

    TalkBegin(0xD)

    ChrTalk(
        0xFE,
        (
            "呼……\x01",
            "终于来到柏斯市了吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "真是的，\x01",
            "在哈肯门滞留了那么长时间。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "作为帝国商人的我\x01",
            "怎么能够一直呆在那种地方呢。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xD)
    Return()

    # Function_11_38B1 end

    def Function_12_3972(): pass

    label("Function_12_3972")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_3A24")

    ChrTalk(
        0xFE,
        (
            "最近超市里卖的服装\x01",
            "还真是合我心意啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "款式设计相当不错，\x01",
            "到底是什么牌子的呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B86")

    label("loc_3A24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_3AC1")

    ChrTalk(
        0xFE,
        (
            "为了再去安特洛丝餐厅吃饭，\x01",
            "如今要先找一份工作才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "还是要去柏斯超市啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3B86")

    label("loc_3AC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_3B86")

    ChrTalk(
        0xFE,
        (
            "法娜说，\x01",
            "想再去一次安特洛丝餐厅。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是，\x01",
            "现在可不是说去就去的时候。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "必须先打工存钱才行。\x02",
    )

    CloseMessageWindow()

    label("loc_3B86")

    TalkEnd(0xE)
    Return()

    # Function_12_3972 end

    def Function_13_3B8A(): pass

    label("Function_13_3B8A")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_3C5D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C19")
    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "超市蛋糕店卖的蛋糕\x01",
            "据说很好吃。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我要不要\x01",
            "到那里去看一下呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C5A")

    label("loc_3C19")


    ChrTalk(
        0xFE,
        (
            "超市蛋糕店卖的蛋糕\x01",
            "据说很好吃。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C5A")

    Jump("loc_3E4E")

    label("loc_3C5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_3CF3")

    ChrTalk(
        0xFE,
        "我也要去打工。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "只要一想到\x01",
            "可以品尝美味的食物，\x01",
            "不管多么辛苦我都会努力工作哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E4E")

    label("loc_3CF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_3E4E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DC3")
    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "吃下了美味的食物后，\x01",
            "就会觉得非常幸福。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "传闻中的安特洛丝餐厅\x01",
            "的饭菜非常可口。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我想每年去那里一次\x01",
            "好好奢侈一回。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E4E")

    label("loc_3DC3")


    ChrTalk(
        0xFE,
        (
            "传闻中的安特洛丝餐厅\x01",
            "的饭菜非常可口。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我想每年去那里一次\x01",
            "好好奢侈一回。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E4E")

    TalkEnd(0xF)
    Return()

    # Function_13_3B8A end

    def Function_14_3E52(): pass

    label("Function_14_3E52")

    TalkBegin(0x10)

    NpcTalk(
        0x10,
        "年轻女性",
        "莉拉，求求你了。\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x10,
        "年轻女性",
        (
            "如果不是这种非常时刻，\x01",
            "我也不会去看的。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x10)
    Return()

    # Function_14_3E52 end

    def Function_15_3EA9(): pass

    label("Function_15_3EA9")

    TalkBegin(0x13)

    NpcTalk(
        0x13,
        "女佣",
        (
            "大小姐，\x01",
            "您又做这样的事情啦……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x13)
    Return()

    # Function_15_3EA9 end

    def Function_16_3ECC(): pass

    label("Function_16_3ECC")

    EventBegin(0x2)
    TurnDirection(0x134, 0x0, 400)

    ChrTalk(
        0x134,
        (
            "#620F各位要到哪里去呢？\x01",
            "　\x02\x03",
            "市长应该就在\x01",
            "柏斯超市视察。\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_16_3ECC end

    def Function_17_3F37(): pass

    label("Function_17_3F37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 5)), scpexpr(EXPR_END)), "loc_3F45")
    Call(0, 18)
    Jump("loc_412D")

    label("loc_3F45")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x33)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3FC0")
    EventBegin(0x2)
    TurnDirection(0x134, 0x0, 400)

    ChrTalk(
        0x134,
        (
            "#620F各位要到哪里去呢？\x01",
            "　\x02\x03",
            "市长应该就在\x01",
            "柏斯超市视察。\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_412D")

    label("loc_3FC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_412D")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_407B")
    OP_A2(0x6)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FEB")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_3FF2")

    label("loc_3FEB")

    TurnDirection(0x103, 0x0, 400)

    label("loc_3FF2")


    ChrTalk(
        0x103,
        (
            "#020F先回协会支部\x01",
            "确认一下现在的状况吧。\x02\x03",
            "想去别的地方，\x01",
            "等以后办完事情再去也不晚。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4112")

    label("loc_407B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4091")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_4098")

    label("loc_4091")

    TurnDirection(0x103, 0x0, 400)

    label("loc_4098")


    ChrTalk(
        0x103,
        (
            "#020F先回协会支部\x01",
            "确认一下现在的状况吧。\x02\x03",
            "柏斯支部在北街区。\x01",
            "就在东口的附近。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4112")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_412D")

    Return()

    # Function_17_3F37 end

    def Function_18_412E(): pass

    label("Function_18_412E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xD, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0xD, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4387")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_41AB")
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F出发之前，\x01",
            "还是把教区长的信送到教会吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_436C")

    label("loc_41AB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4292")
    Sleep(100)
    OP_A2(0x5)

    ChrTalk(
        0x102,
        (
            "#014F等一下，艾丝蒂尔，听我说。\x02\x03",
            "迪拜恩教区长让我们送的信\x01",
            "还没有送到呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#008F啊……差点忘了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F出发之前，去教会一趟吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_436C")

    label("loc_4292")

    OP_A2(0x5)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#014F啊，说起来……\x02\x03",
            "迪拜恩教区长让我们送的信\x01",
            "还没有送到呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#008F啊……差点忘了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F出发之前，去教会一趟吧。\x02",
    )

    CloseMessageWindow()

    label("loc_436C")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_4387")

    Return()

    # Function_18_412E end

    def Function_19_4388(): pass

    label("Function_19_4388")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_6D(48080, 5850, 59960, 0)
    OP_6C(225000, 0)
    OP_67(0, 5395, -10000, 0)
    OP_6B(5350, 0)
    SetChrPos(0x103, 69550, 0, 60780, 270)
    SetChrPos(0x101, 70210, 0, 59570, 270)
    SetChrPos(0x102, 71260, 0, 60540, 270)
    StopSound(0x9470, 0x30D40, 0x0)

    def lambda_4409():
        OP_6C(270000, 8000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_4409)
    Sleep(3000)

    def lambda_441E():
        OP_6D(69410, 0, 60250, 5000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_441E)

    def lambda_4436():
        OP_67(0, 9500, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_4436)
    OP_6B(2800, 5000)
    StopSound(0x9470, 0x186A0, 0x1F40)

    ChrTalk(
        0x103,
        (
            "#020F终于到了啊。\x02\x03",
            "这里就是柏斯地区的中心，\x01",
            "商业都市柏斯。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F哇～……\x01",
            "果然是都市的感觉呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F柏斯在利贝尔的五大都市之中，\x01",
            "城市规模仅次于王都。\x02\x03",
            "和洛连特相比，这里的建筑物都是石制的，\x01",
            "给人一种巨大结实的感觉。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(
        0x101,
        (
            "#000F哎，那边那间大得夸张的房子\x01",
            "是做什么用的啊？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(
        0x103,
        (
            "#020F那个是柏斯超市。\x01",
            "一个汇集了各种商店的室内市场。\x02\x03",
            "食品、衣服、杂货、家具、书籍……\x02\x03",
            "除了武器和导力器以外的商品，\x01",
            "在那里基本都能买到。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F不愧是商业都市，\x01",
            "真是名副其实的繁华啊～\x02\x03",
            "#007F啊啊……\x01",
            "要是为了购物来这里玩就好了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F那样的事以后还有机会。\x02\x03",
            "我们还是先去趟协会支部，\x01",
            "确认一下到底发生了什么事吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#002F……嗯。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F顺便说一下，\x01",
            "柏斯支部就在前面很近的地方哦。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_19_4388 end

    def Function_20_4868(): pass

    label("Function_20_4868")

    EventBegin(0x0)
    OP_6D(64470, 0, 73180, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(261, 0)
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    OP_4A(0xC, 255)
    OP_44(0x10, 0xFF)
    OP_44(0x13, 0xFF)
    SetChrPos(0x103, 63280, 0, 74260, 180)
    SetChrPos(0x101, 64540, 0, 74600, 180)
    SetChrPos(0x102, 65730, 0, 74040, 225)
    SetChrPos(0x10, 64220, 0, 71730, 0)
    SetChrPos(0x13, 65120, 0, 70810, 0)
    TurnDirection(0x101, 0x10, 0)
    TurnDirection(0x102, 0x10, 0)
    TurnDirection(0x103, 0x10, 0)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x10, 0x40)
    SetChrFlags(0x13, 0x40)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(
        0x10,
        (
            "#610F……那么各位，\x01",
            "这件事无论如何拜托了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F嗯！交给我们吧！\x01",
            "得到什么消息就通知您。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#611F期待你们的好消息。\x02\x03",
            "那么，祝一路平安。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#620F……诸位请慢走。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10, 180, 400)

    def lambda_4A53():
        OP_8E(0x10, 0xFBA4, 0x0, 0xFBE9, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4A53)
    Sleep(500)
    OP_8C(0x13, 180, 400)
    OP_8E(0x13, 0xFBA4, 0x0, 0xFBE9, 0xBB8, 0x0)

    def lambda_4A8E():
        OP_69(0x101, 0x5DC)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_4A8E)
    Sleep(1000)
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(
        0x103,
        (
            "#020F好了，赶紧出发吧。\x02\x03",
            "去哈肯大门的话，\x01",
            "要先通过东柏斯街道北面的钢壁之路。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)
    TurnDirection(0x102, 0x103, 400)

    ChrTalk(
        0x102,
        (
            "#010F也就是说，从城的东门出去，\x01",
            "然后向北走就可以了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F那么，我们出发吧！\x02",
    )

    CloseMessageWindow()
    OP_4B(0x8, 255)
    OP_4B(0x9, 255)
    OP_4B(0xC, 255)
    EventEnd(0x0)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x13, 0x80)
    Return()

    # Function_20_4868 end

    def Function_21_4BE1(): pass

    label("Function_21_4BE1")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    OP_4A(0xC, 255)
    OP_44(0x104, 0xFF)
    OP_6D(70630, 0, 62020, 0)
    OP_6C(315000, 0)
    SetChrPos(0x104, 70660, 0, 60750, 270)
    SetChrPos(0x103, 72300, 0, 59880, 270)
    SetChrPos(0x101, 71730, 0, 61730, 270)
    SetChrPos(0x102, 73360, 0, 61130, 270)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x104,
        (
            "#030F#1P哦～这就是柏斯市。\x01",
            "比想象中还要繁华许多啊。\x02\x03",
            "那边那座高大的建筑物\x01",
            "是不是叫柏斯超市？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)

    ChrTalk(
        0x101,
        (
            "#000F#2P嗯，你知道的还挺多嘛。\x01",
            "不是第一次来利贝尔王国吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x104, 0)
    TurnDirection(0x104, 0x102, 400)

    ChrTalk(
        0x104,
        (
            "#035F#1P呵呵，因为我旅行出发前\x01",
            "买了一本观光手册啊。\x02\x03",
            "是一家叫『利贝尔通讯社』的\x01",
            "出版社出版的导游刊物。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F#2P观、观光手册～？\x01",
            "这种东西也有卖的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F怎么说呢，毕竟现在已经是\x01",
            "做什么事都十分便利的时代了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F那么你是不是\x01",
            "打算去超市购物啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#030F#1P啊啊，超市只是一般逛逛，\x01",
            "正餐倒是打算吃得豪华一点。\x02\x03",
            "根据观光手册上说，\x01",
            "这座城市有家三星级的高级饭店。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F#2P啊，就是我们和\x01",
            "市长商量事情的地方吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 400)

    ChrTalk(
        0x101,
        "#000F#1P就是那座建筑啊。\x02",
    )

    CloseMessageWindow()

    def lambda_4FE2():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4FE2)

    def lambda_4FF0():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4FF0)

    def lambda_4FFE():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4FFE)

    def lambda_500C():
        OP_6C(45000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_500C)
    OP_6D(67520, 260, 72190, 3000)
    Sleep(500)

    ChrTalk(
        0x102,
        (
            "#010F叫做『安特洛丝餐厅』，\x01",
            "以正宗利贝尔料理闻名的饭店。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(70630, 0, 62020, 0)
    OP_6C(315000, 0)
    OP_0D()

    ChrTalk(
        0x104,
        (
            "#031F#1P嗯，看样子就是这里。\x02\x03",
            "呵呵呵……今天开始要享福了！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)
    TurnDirection(0x102, 0x104, 400)
    TurnDirection(0x103, 0x104, 400)

    ChrTalk(
        0x103,
        (
            "#020F但是，要享受高档的美食，\x01",
            "花费还是相当的高哦。\x02\x03",
            "我劝你还是去普通的酒馆吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x102, 400)

    ChrTalk(
        0x104,
        (
            "#030F#1P请不用担心。\x01",
            "我带了很多的旅费呢。\x02\x03",
            "而且如果真的不够用，\x01",
            "本人还可以用自己的特技赚钱。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F特技……\x01",
            "是指刚才的唱歌和演奏吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#009F#2P打、打算靠那个赚钱？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#035F#1P呵呵，我还曾在帝都的大剧场\x01",
            "担任过歌剧的主演呢。\x02\x03",
            "那一次，虽然只有一个晚上，\x01",
            "却赚了足足一百万米拉呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007F#2P（太假了吧～……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#030F#1P那么各位，你们辛苦了！\x02\x03",
            "直到命中注定的再次相会为止，\x01",
            "让我们先暂时地分别吧！\x02\x03",
            "#031FAdeus amigo！（葡萄牙语：再见朋友）\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x104, 270, 400)
    Sleep(250)

    def lambda_542F():

        label("loc_542F")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_542F")

    QueueWorkItem2(0x101, 1, lambda_542F)

    def lambda_5440():

        label("loc_5440")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_5440")

    QueueWorkItem2(0x102, 1, lambda_5440)

    def lambda_5451():

        label("loc_5451")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_5451")

    QueueWorkItem2(0x103, 1, lambda_5451)
    OP_62(0x104, 0x0, 2300, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    OP_8E(0x104, 0xEF34, 0x0, 0xECE0, 0x1770, 0x0)
    Sleep(1000)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x103, 0xFF)

    def lambda_549E():
        OP_6D(72130, 0, 62020, 1500)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_549E)
    OP_8C(0x101, 135, 400)
    OP_8C(0x103, 45, 400)
    WaitChrThread(0x0, 0x2)

    ChrTalk(
        0x101,
        (
            "#008F哈～……\x01",
            "真是无可救药的家伙啊。\x02\x03",
            "埃雷波尼亚帝国的人\x01",
            "是不是都像他那样奇怪的啊？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#018F#4P那个样子的话，\x01",
            "一般的埃雷波尼亚人也会觉得困扰吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F哎？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F#4P没什么，\x01",
            "我觉得还是朴实的人比较多。\x02\x03",
            "曾经读过的书里说过，\x01",
            "他们崇尚质朴刚健的民风。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F唔～……\x02\x03",
            "这么说来，\x01",
            "艺术家果然都是不正常的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#021F哎呀哎呀。\x01",
            "要是其他艺术家听到了可是会生气的哦。\x02\x03",
            "#020F接下来……\x01",
            "我们到协会向卢格兰爷爷汇报一下\x01",
            "从将军那里打听到的消息吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#4P报告完毕之后，\x01",
            "最好再去市长官邸知会梅贝尔市长。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F协会和市长官邸啊……\x02\x03",
            "那我们赶快走吧。\x02",
        )
    )

    CloseMessageWindow()
    RemoveParty(0x3, 0xFF)
    OP_B8(0x3)
    OP_4B(0x8, 255)
    OP_4B(0x9, 255)
    OP_4B(0xC, 255)
    EventEnd(0x0)
    Return()

    # Function_21_4BE1 end

    def Function_22_584F(): pass

    label("Function_22_584F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_644A")
    OP_A2(0x316)
    OP_44(0x13, 0xFF)
    ClearMapFlags(0x1)
    EventBegin(0x0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 24359, 500, 57973, 90)
    SetChrPos(0x11, 25364, 0, 57280, 270)
    SetChrPos(0x12, 25497, 0, 58710, 270)
    TurnDirection(0x11, 0x13, 800)
    TurnDirection(0x12, 0x13, 800)

    def lambda_58BF():
        OP_6C(270000, 3000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_58BF)
    OP_6D(24400, 0, 57655, 3000)

    ChrTalk(
        0x11,
        (
            "#141F喂，小姐。\x01",
            "拜托你通报一下吧。\x02\x03",
            "只要市长一句话，\x01",
            "做一下评论就可以了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#151F就是就是，\x01",
            "之后再顺便照张相片就行了～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#620F#5P即使你们这么说……\x01",
            "市长她现在的公务非常繁忙。\x02\x03",
            "而且你们没有事先预约，\x01",
            "所以还是请回吧。\x02\x03",
            "请务必谅解。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#144F怎能这样！\x02\x03",
            "像这样的大事件，\x01",
            "我们却什么情况都不知道……\x02\x03",
            "一定要对读者有个交待才行呀！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#623F#5P可是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#151F没错没错，就是那样的哦。\x02\x03",
            "如果由那位传说中的美人市长作封面，\x01",
            "销量绝对会大增的哦～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#620F#5P……………………………\x02",
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1200)

    def lambda_5BFD():
        TurnDirection(0xFE, 0x12, 0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_5BFD)

    ChrTalk(
        0x11,
        (
            "#144F喂，朵洛希！\x01",
            "别说这么失礼的话！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5C54():
        TurnDirection(0xFE, 0x11, 0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5C54)

    ChrTalk(
        0x12,
        (
            "#153F哎～～\x01",
            "这不是奈尔前辈你跟我说的吗？\x02\x03",
            "如果没有什么新闻的话，\x01",
            "就把美人市长塑造为吸引读者的偶像，\x01",
            "作为杂志的封面人物。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#144F喂，笨蛋！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#620F#5P………………………………\x01",
            "………………………………\x01",
            "………………………………\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    TurnDirection(0x11, 0x13, 0)
    Sleep(500)

    ChrTalk(
        0x11,
        "#143F我、我说，女佣小姐？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#620F#5P真是非常有趣的客人呢……\x02\x03",
            "你们二位的话，\x01",
            "我会详细地向市长转达的。\x02\x03",
            "今天请二位先回去吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#144F等、等一下！\x01",
            "这之中稍微有点误会……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#624F#5P请·您·回·去·吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#145F是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#153F哎，美人市长的照片，\x01",
            "不拍也没关系吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#145F拜托……算我求你了……\x01",
            "从现在开始不要再多嘴了……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x11, 45, 400)

    def lambda_5F75():
        OP_8E(0xFE, 0x7B09, 0x0, 0xE22C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_5F75)
    Sleep(300)

    def lambda_5F95():

        label("loc_5F95")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_5F95")

    QueueWorkItem2(0x12, 1, lambda_5F95)
    OP_62(0x12, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0x12,
        (
            "#153F前、前辈！\x01",
            "请等一下啦～！\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x12, 0xFF)
    OP_8E(0x12, 0x7B09, 0x0, 0xE22C, 0xBB8, 0x0)

    ChrTalk(
        0x13,
        "#620F#5P呼……\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_62(0x13, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x13,
        "#622F#5P…………哎？\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrPos(0x101, 33497, 0, 57400, 0)
    SetChrPos(0x102, 33497, 0, 58550, 0)
    SetChrPos(0x103, 33497, 0, 57890, 0)

    def lambda_6086():
        OP_6D(25400, 0, 57800, 1500)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_6086)

    def lambda_609E():
        OP_8E(0xFE, 0x6CCA, 0x0, 0xE038, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_609E)
    Sleep(500)

    def lambda_60BE():
        OP_8E(0xFE, 0x6D60, 0x0, 0xE4B6, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_60BE)
    Sleep(500)

    def lambda_60DE():
        OP_8E(0xFE, 0x72B0, 0x0, 0xE222, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_60DE)
    WaitChrThread(0x103, 0x1)

    ChrTalk(
        0x101,
        "#000F你好，莉拉小姐。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#620F#1P啊，原来是诸位游击士啊。\x02\x03",
            "你们刚从\x01",
            "哈肯大门那边回来吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯，没错。\x02\x03",
            "话说回来，刚才的那些人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#620F#1P都是不速之客。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#620F#1P都是些意图\x01",
            "在小姐身上打主意的不法之徒。\x02\x03",
            "在我的眼皮底下，\x01",
            "他们休想碰小姐一根指头。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1200)

    ChrTalk(
        0x101,
        "#008F啊，啊哈哈……是啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#019F工、工作真是尽职尽责啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#621F#1P因为那是我的责任。\x02\x03",
            "好了，诸位请进吧。\x01",
            "市长正等着你们呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x13, 270, 400)
    OP_6F(0x6, 0)
    OP_70(0x6, 0x3C)
    OP_73(0x6)
    SetChrFlags(0x13, 0x40)
    OP_8E(0x13, 0x5B4F, 0x1F4, 0xE2C2, 0xBB8, 0x0)

    def lambda_63F4():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_63F4)
    SetChrFlags(0x13, 0x4)
    OP_94(0x0, 0x13, 0x0, 0x1F4, 0x5DC, 0x0)
    OP_72(0x6, 0x800)
    OP_22(0x7, 0x0, 0x64)
    OP_6F(0x6, 60)
    OP_70(0x6, 0x0)
    OP_73(0x6)
    OP_71(0x6, 0x800)
    SetChrFlags(0x13, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xC, 0x80)
    EventEnd(0x0)

    label("loc_644A")

    Return()

    # Function_22_584F end

    def Function_23_644B(): pass

    label("Function_23_644B")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    SetChrPos(0x101, 28680, 0, 57870, 90)
    SetChrPos(0x102, 29950, 0, 59190, 180)
    SetChrPos(0x103, 30030, 0, 56790, 0)
    OP_6D(28840, 0, 57170, 0)
    OP_6C(225000, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#002F#2P嗯……\x01",
            "市长姐姐她刚才怎么了？\x02\x03",
            "听到老爸名字的时候，\x01",
            "好像相当吃惊的样子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F确实如此呢……\x01",
            "不过也不难想象出来。\x02\x03",
            "也许父亲和市长\x01",
            "还有摩尔根将军以前就认识了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F#2P？？？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_66A4")

    ChrTalk(
        0x103,
        (
            "#020F好了，先把这个放在一边吧。\x02\x03",
            "向市长报告完毕了，\x01",
            "接着去游击士协会一趟吧。\x02\x03",
            "卢格兰爷爷\x01",
            "一定在等着我们的报告了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F#2P嗯，知道了！\x02",
    )

    CloseMessageWindow()
    Jump("loc_6C47")

    label("loc_66A4")

    OP_A2(0x315)

    ChrTalk(
        0x103,
        (
            "#020F好了，先把这个放在一边吧。\x02\x03",
            "接下来的问题就是\x01",
            "我们该采取什么行动了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F#2P嗯……\x02\x03",
            "光是要找定期船和空贼团的隐藏地点\x01",
            "就已经很困难了。\x02\x03",
            "如果能轻易找得到的话，\x01",
            "军队方面也应该早就发现才对啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 0)

    ChrTalk(
        0x102,
        "#014F…………………………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 0)

    ChrTalk(
        0x103,
        "#023F……………………………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)
    Sleep(200)
    TurnDirection(0x101, 0x103, 400)
    Sleep(200)
    OP_8C(0x101, 90, 400)
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#000F#2P嗯，你们两个怎么了啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F艾丝蒂尔，你变得成熟了呢……\x02\x03",
            "如果是以前的你，肯定只会说出\x01",
            "『彻底地搜查一遍不就好了』\x01",
            "这样不经考虑的话……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#021F没想到能从艾丝蒂尔的嘴里\x01",
            "听到这么理智的分析……\x02\x03",
            "姐姐我真是太感动了……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#009F#2P你们什么意思！\x01",
            "真是没礼貌！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#019F哈哈，这是在表扬你呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F确实，和洛连特不同，\x01",
            "柏斯地区幅员相当广阔。\x02\x03",
            "现在最需要的就是线索。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#003F#2P线索啊……\x02\x03",
            "#006F对了，刚才在市长家门前，\x01",
            "不是看见奈尔他们了吗？\x02\x03",
            "他们好像正在\x01",
            "为报道取材的事烦恼着……\x01",
            "会不会知道些什么线索呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F也有道理，\x01",
            "他们本来就比我们早一步到达柏斯。\x02\x03",
            "我觉得有打听一下的必要。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F#2P那两个人去了哪里呢？\x02",
    )

    CloseMessageWindow()
    OP_28(0x35, 0x1, 0x800)
    OP_28(0x35, 0x1, 0x1000)

    label("loc_6C47")

    ClearMapFlags(0x400000)
    EventEnd(0x0)
    Return()

    # Function_23_644B end

    def Function_24_6C4F(): pass

    label("Function_24_6C4F")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    OP_4A(0xC, 255)
    OP_6D(58940, 0, 77210, 0)
    SetChrPos(0x101, 58890, 0, 78180, 180)
    SetChrPos(0x102, 57570, 0, 76880, 90)
    SetChrPos(0x103, 59990, 0, 77000, 270)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x103,
        (
            "#020F#4P虽然已经向协会\x01",
            "还有市长报告过了……\x02\x03",
            "可是我们今后该如何行动才好呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F#1P嗯……\x02\x03",
            "光是要找定期船和空贼团的隐藏地点\x01",
            "就已经很困难了。\x02\x03",
            "如果能轻易找得到的话，\x01",
            "军队方面也应该早就发现才对啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 0)

    ChrTalk(
        0x102,
        "#014F…………………………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 0)

    ChrTalk(
        0x103,
        "#023F#4P…………………………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)
    Sleep(200)
    TurnDirection(0x101, 0x103, 400)
    Sleep(200)
    OP_8C(0x101, 180, 400)
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#000F#1P嗯，你们两个怎么了啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F艾丝蒂尔，你变得成熟了呢……\x02\x03",
            "如果是以前的你，肯定只会说出\x01",
            "『彻底地搜查一遍不就好了』\x01",
            "这样不经考虑的话……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#021F#4P没想到能从艾丝蒂尔的嘴里\x01",
            "听到这么理智的分析……\x02\x03",
            "姐姐我真是太感动了……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#009F#1P你们什么意思！\x01",
            "真是没礼貌！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#019F哈哈，这是在表扬你呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F#4P确实，和洛连特不同，\x01",
            "柏斯地区幅员相当广阔。\x02\x03",
            "现在最需要的就是线索。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#003F#1P线索啊……\x02\x03",
            "#006F对了，刚才在市长家门前，\x01",
            "不是看见奈尔他们了吗？\x02\x03",
            "他们好像正在\x01",
            "为报道取材的事烦恼着……\x01",
            "会不会知道些什么线索呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F也有道理，\x01",
            "他们本来就比我们早一步到达柏斯。\x02\x03",
            "我觉得有打听一下的必要。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F#1P那两个人去了哪里呢？\x02",
    )

    CloseMessageWindow()
    OP_28(0x35, 0x1, 0x800)
    OP_28(0x35, 0x1, 0x1000)
    OP_4B(0x8, 255)
    OP_4B(0x9, 255)
    OP_4B(0xC, 255)
    EventEnd(0x0)
    Return()

    # Function_24_6C4F end

    def Function_25_7275(): pass

    label("Function_25_7275")

    EventBegin(0x0)
    OP_6D(49570, 0, 86360, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3240, 0)
    OP_6C(45000, 0)
    OP_6E(261, 0)
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    OP_4A(0xC, 255)
    OP_B8(0x2)
    OP_B8(0x3)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x3, 0xFF)
    SetChrPos(0x101, 47600, 3000, 91910, 180)
    SetChrPos(0x102, 48600, 3000, 92500, 180)

    def lambda_72F2():
        OP_8E(0xFE, 0xB9F0, 0x0, 0x13F10, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_72F2)

    def lambda_730D():
        OP_8E(0xFE, 0xBDD8, 0x0, 0x14406, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_730D)
    FadeToBright(2000, 0)
    Sleep(3500)
    Fade(500)
    OP_6D(48040, 0, 83320, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(0, 0)
    OP_6E(261, 0)
    OP_0D()
    WaitChrThread(0x101, 0x1)
    OP_8C(0x101, 45, 400)
    WaitChrThread(0x102, 0x1)
    OP_8C(0x102, 225, 400)

    ChrTalk(
        0x101,
        (
            "#000F接下来，要环游整个王国的话，\x01",
            "那么下一个目的地就是卢安地区了。\x02\x03",
            "走哪条路好呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F#2P你这样说的话……\x01",
            "真的决定不坐定期船了？\x02\x03",
            "如果要步行，\x01",
            "应该会绕不少弯路的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F雪拉姐不是说过吗？\x02\x03",
            "要守护一片土地，\x01",
            "首先就要自己脚踏实地去看一看。\x02\x03",
            "啊，这是父亲说的吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#2P也对，我们的时间确实很充裕，\x01",
            "我也觉得慢慢走路去也不错。\x02\x03",
            "定期船的票钱也能节省下来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F是啊是啊，\x01",
            "就用省下来的钱去柏斯超市采购一番吧。\x02\x03",
            "空贼作乱的时候我们\x01",
            "都没办法静下心来好好买东西。\x02\x03",
            "#501F就在出发前先逛逛超市吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#017F#2P我倒没什么关系……\x01",
            "只是希望你不要太乱花钱了。\x02\x03",
            "#010F顺便说一下，要去卢安地区，\x01",
            "就必须经过西面的古罗尼山峰。\x02\x03",
            "买好东西后就从城里的西门出发吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006FＯＫ！城里的西门是吧。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x35D)
    OP_A2(0x35E)
    OP_A2(0x400)
    OP_4F(0x4, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4B(0x8, 255)
    OP_4B(0x9, 255)
    OP_4B(0xC, 255)
    EventEnd(0x0)
    Return()

    # Function_25_7275 end

    def Function_26_7845(): pass

    label("Function_26_7845")

    SetPlaceName(0x2A) # 柏斯国际空港
    Return()

    # Function_26_7845 end

    def Function_27_7849(): pass

    label("Function_27_7849")

    SetPlaceName(0x26) # 柏斯国际空港
    Return()

    # Function_27_7849 end

    def Function_28_784D(): pass

    label("Function_28_784D")

    SetPlaceName(0x25) # 柏斯国际空港
    Return()

    # Function_28_784D end

    def Function_29_7851(): pass

    label("Function_29_7851")

    SetPlaceName(0x20) # 柏斯国际空港
    Return()

    # Function_29_7851 end

    def Function_30_7855(): pass

    label("Function_30_7855")

    SetPlaceName(0x28) # 柏斯国际空港
    Return()

    # Function_30_7855 end

    def Function_31_7859(): pass

    label("Function_31_7859")

    SetPlaceName(0x2B) # 柏斯国际空港
    Return()

    # Function_31_7859 end

    def Function_32_785D(): pass

    label("Function_32_785D")

    SetPlaceName(0x21) # 柏斯国际空港
    Return()

    # Function_32_785D end

    def Function_33_7861(): pass

    label("Function_33_7861")

    SetPlaceName(0x27) # 柏斯国际空港
    Return()

    # Function_33_7861 end

    SaveToFile()

Try(main)
