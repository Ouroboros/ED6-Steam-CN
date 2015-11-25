from ED6ScenarioHelper import *

def main():
    # 拉文努村　村长家

    CreateScenaFile(
        FileName            = 'T1200   ._SN',
        MapName             = 'Bose',
        Location            = 'T1200.x',
        MapIndex            = 1,
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
        '巴德斯',                               # 9
        '弗兰',                                 # 10
        '鲁伊',                                 # 11
        '罗亚',                                 # 12
        '菲戈',                                 # 13
        '贝斯卡',                               # 14
        '梅洛涅',                               # 15
        '库赖老人',                             # 16
        '艾丝蒂尔',                             # 17
        '莱森村长',                             # 18
        '鸡',                                   # 19
        '鸡',                                   # 20
        '鸡',                                   # 21
        '鸡',                                   # 22
        '拉文努山道方向',                       # 23
        '拉文努村废坑方向',                     # 24
    )

    DeclEntryPoint(
        Unknown_00              = -1600,
        Unknown_04              = 0,
        Unknown_08              = 8800,
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
        'ED6_DT07/CH01060 ._CH',             # 00
        'ED6_DT07/CH01070 ._CH',             # 01
        'ED6_DT07/CH01470 ._CH',             # 02
        'ED6_DT07/CH01120 ._CH',             # 03
        'ED6_DT07/CH01020 ._CH',             # 04
        'ED6_DT07/CH01140 ._CH',             # 05
        'ED6_DT07/CH01030 ._CH',             # 06
        'ED6_DT07/CH01000 ._CH',             # 07
        'ED6_DT07/CH00107 ._CH',             # 08
        'ED6_DT07/CH01490 ._CH',             # 09
        'ED6_DT07/CH00100 ._CH',             # 0A
        'ED6_DT07/CH01720 ._CH',             # 0B
    )

    AddCharChipPat(
        'ED6_DT07/CH01060P._CP',             # 00
        'ED6_DT07/CH01070P._CP',             # 01
        'ED6_DT07/CH01470P._CP',             # 02
        'ED6_DT07/CH01120P._CP',             # 03
        'ED6_DT07/CH01020P._CP',             # 04
        'ED6_DT07/CH01140P._CP',             # 05
        'ED6_DT07/CH01030P._CP',             # 06
        'ED6_DT07/CH01000P._CP',             # 07
        'ED6_DT07/CH00107P._CP',             # 08
        'ED6_DT07/CH01490P._CP',             # 09
        'ED6_DT07/CH00100P._CP',             # 0A
        'ED6_DT07/CH01720P._CP',             # 0B
    )

    DeclNpc(
        X                   = 4720,
        Z                   = 0,
        Y                   = 28930,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 2730,
        Z                   = 0,
        Y                   = 27400,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 2610,
        Z                   = 0,
        Y                   = 28970,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 25370,
        Z                   = -4000,
        Y                   = 9110,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 14250,
        Z                   = -4000,
        Y                   = 21420,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 20710,
        Z                   = -4000,
        Y                   = 9840,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 18930,
        Z                   = -4000,
        Y                   = 15140,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 26300,
        Z                   = -4000,
        Y                   = 19500,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 33000,
        Z                   = 8000,
        Y                   = 36660,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 0,
        Z                   = -4000,
        Y                   = 0,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 7,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 0,
        Z                   = -4000,
        Y                   = 0,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 7,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 0,
        Z                   = -4000,
        Y                   = 0,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 7,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 0,
        Z                   = -4000,
        Y                   = 0,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 7,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -2080,
        Z                   = 0,
        Y                   = -80,
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
        X                   = 7170,
        Z                   = 8000,
        Y                   = 78890,
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
        X                   = 3260,
        Y                   = 7000,
        Z                   = 66870,
        Range               = 9230,
        Unknown_10          = 0x2710,
        Unknown_14          = 0x10C52,
        Unknown_18          = 0x0,
        Unknown_1C          = 22,
    )

    DeclEvent(
        X                   = 5000,
        Y                   = 0,
        Z                   = 34240,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 25,
    )

    DeclEvent(
        X                   = 5150,
        Y                   = 4550,
        Z                   = 41780,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 25,
    )

    DeclEvent(
        X                   = 5310,
        Y                   = 0,
        Z                   = 23020,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 26,
    )

    DeclEvent(
        X                   = 6000,
        Y                   = 4400,
        Z                   = 54640,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 27,
    )


    DeclActor(
        TriggerX            = -7280,
        TriggerZ            = 4460,
        TriggerY            = 54000,
        TriggerRange        = 800,
        ActorX              = -7280,
        ActorZ              = 5460,
        ActorY              = 54000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 21,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 33020,
        TriggerZ            = 8000,
        TriggerY            = 35080,
        TriggerRange        = 1000,
        ActorX              = 33020,
        ActorZ              = 9200,
        ActorY              = 35080,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 24,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_3F2",          # 00, 0
        "Function_1_587",          # 01, 1
        "Function_2_5B8",          # 02, 2
        "Function_3_735",          # 03, 3
        "Function_4_782",          # 04, 4
        "Function_5_817",          # 05, 5
        "Function_6_884",          # 06, 6
        "Function_7_8D1",          # 07, 7
        "Function_8_A23",          # 08, 8
        "Function_9_AAF",          # 09, 9
        "Function_10_AD5",         # 0A, 10
        "Function_11_1161",        # 0B, 11
        "Function_12_16AB",        # 0C, 12
        "Function_13_3022",        # 0D, 13
        "Function_14_37F9",        # 0E, 14
        "Function_15_40A2",        # 0F, 15
        "Function_16_4A46",        # 10, 16
        "Function_17_4EB8",        # 11, 17
        "Function_18_539B",        # 12, 18
        "Function_19_589D",        # 13, 19
        "Function_20_5A60",        # 14, 20
        "Function_21_6219",        # 15, 21
        "Function_22_6261",        # 16, 22
        "Function_23_6A82",        # 17, 23
        "Function_24_6EA2",        # 18, 24
        "Function_25_6FAC",        # 19, 25
        "Function_26_6FB0",        # 1A, 26
        "Function_27_6FB4",        # 1B, 27
    )


    def Function_0_3F2(): pass

    label("Function_0_3F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_42E")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8)
    Jump("loc_51B")

    label("loc_42E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_44C")
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8)
    Jump("loc_51B")

    label("loc_44C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_488")
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8)
    Jump("loc_51B")

    label("loc_488")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 5)), scpexpr(EXPR_END)), "loc_49C")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8)
    Jump("loc_51B")

    label("loc_49C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 4)), scpexpr(EXPR_END)), "loc_4C1")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8)
    SetChrPos(0xA, 35020, -3850, 8540, 180)
    Jump("loc_51B")

    label("loc_4C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_4EB")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8)
    SetChrPos(0xA, 35020, -3850, 8540, 180)
    SetChrFlags(0xA, 0x10)
    Jump("loc_51B")

    label("loc_4EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_51B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xE, 0x1, 0x1000)"), scpexpr(EXPR_END)), "loc_505")
    SetChrFlags(0xC, 0x80)
    Jump("loc_516")

    label("loc_505")

    SetChrPos(0xC, 4840, 8000, 66800, 180)

    label("loc_516")

    SetChrFlags(0xA, 0x10)

    label("loc_51B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_52C")
    ClearChrFlags(0x11, 0x80)

    label("loc_52C")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (108, "loc_53C"),
        (109, "loc_565"),
        (SWITCH_DEFAULT, "loc_586"),
    )


    label("loc_53C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_54E")
    OP_A2(0x31A)
    Event(0, 20)
    Jump("loc_562")

    label("loc_54E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_562")
    Event(0, 19)

    label("loc_562")

    Jump("loc_586")

    label("loc_565")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xE, 0x1, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0xE, 0x1, 0x1000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_583")
    OP_28(0xE, 0x1, 0x1000)
    Event(0, 23)

    label("loc_583")

    Jump("loc_586")

    label("loc_586")

    Return()

    # Function_0_3F2 end

    def Function_1_587(): pass

    label("Function_1_587")

    OP_16(0x2, 0xFA0, 0xFFFE5638, 0xFFFE98A0, 0x30043)
    OP_72(0x6, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5B2")
    OP_72(0xA, 0x4)
    Jump("loc_5B7")

    label("loc_5B2")

    OP_71(0xA, 0x4)

    label("loc_5B7")

    Return()

    # Function_1_587 end

    def Function_2_5B8(): pass

    label("Function_2_5B8")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5DD")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_71F")

    label("loc_5DD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F6")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_71F")

    label("loc_5F6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_60F")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_71F")

    label("loc_60F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_628")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_71F")

    label("loc_628")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_641")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_71F")

    label("loc_641")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_65A")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_71F")

    label("loc_65A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_673")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_71F")

    label("loc_673")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_68C")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_71F")

    label("loc_68C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6A5")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_71F")

    label("loc_6A5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6BE")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_71F")

    label("loc_6BE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6D7")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_71F")

    label("loc_6D7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F0")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_71F")

    label("loc_6F0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_709")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_71F")

    label("loc_709")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_71F")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_71F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_734")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_71F")

    label("loc_734")

    Return()

    # Function_2_5B8 end

    def Function_3_735(): pass

    label("Function_3_735")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_781")
    OP_8E(0xFE, 0x13C4, 0x0, 0x6ED2, 0x7D0, 0x0)
    OP_8C(0xFE, 225, 500)
    Sleep(1000)
    OP_8E(0xFE, 0xF96, 0x0, 0x72C4, 0x7D0, 0x0)
    OP_8C(0xFE, 225, 500)
    Sleep(1000)
    Jump("Function_3_735")

    label("loc_781")

    Return()

    # Function_3_735 end

    def Function_4_782(): pass

    label("Function_4_782")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_816")
    OP_8E(0xFE, 0xDC0, 0x0, 0x6E0A, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 500)
    Sleep(1000)
    OP_8E(0xFE, 0x105E, 0x0, 0x6B44, 0x7D0, 0x0)
    OP_8C(0xFE, 45, 500)
    Sleep(1000)
    OP_8E(0xFE, 0xEB0, 0x0, 0x65D6, 0x7D0, 0x0)
    OP_8E(0xFE, 0xBC2, 0x0, 0x6770, 0x7D0, 0x0)
    OP_8C(0xFE, 45, 500)
    Sleep(1000)
    OP_8E(0xFE, 0xAAA, 0x0, 0x6B08, 0x7D0, 0x0)
    Jump("Function_4_782")

    label("loc_816")

    Return()

    # Function_4_782 end

    def Function_5_817(): pass

    label("Function_5_817")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_883")
    OP_8E(0xFE, 0x631A, 0xFFFFF060, 0x2B48, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(1000)
    OP_8E(0xFE, 0x7224, 0xFFFFF060, 0x2120, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(1000)
    OP_8E(0xFE, 0x597E, 0xFFFFF060, 0x15EA, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Sleep(1000)
    Jump("Function_5_817")

    label("loc_883")

    Return()

    # Function_5_817 end

    def Function_6_884(): pass

    label("Function_6_884")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8D0")
    OP_8E(0xFE, 0x4222, 0xFFFFF060, 0x3E8A, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 500)
    Sleep(1000)
    OP_8E(0xFE, 0x53A2, 0xFFFFF060, 0x3638, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 500)
    Sleep(1000)
    Jump("Function_6_884")

    label("loc_8D0")

    Return()

    # Function_6_884 end

    def Function_7_8D1(): pass

    label("Function_7_8D1")

    SetChrFlags(0xFE, 0x40)
    SetChrFlags(0xFE, 0x4)
    OP_8D(0xFE, 12660, 3550, 26000, 18020, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8FF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A22")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9E7")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x3174), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_PUSH_LONG, 0xDDE), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_LONG, 0x6590), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_LONG, 0x4664), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9BC")
    SetChrFlags(0xFE, 0x20)
    TurnDirection(0xFE, 0x0, 0)
    ClearChrFlags(0xFE, 0x20)

    def lambda_9A9():
        OP_94(0x0, 0xFE, 0xB4, 0x12C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9A9)
    Jump("loc_9DF")

    label("loc_9BC")


    def lambda_9C2():
        OP_8D(0xFE, 12660, 3550, 26000, 18020, 6000)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9C2)
    Sleep(200)

    label("loc_9DF")

    Sleep(30)
    Jump("loc_A1F")

    label("loc_9E7")

    Sleep(50)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A1F")
    OP_44(0xFE, 0x2)

    def lambda_A07():
        OP_8D(0xFE, 12660, 3550, 26000, 18020, 1500)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A07)

    label("loc_A1F")

    Jump("loc_8FF")

    label("loc_A22")

    Return()

    # Function_7_8D1 end

    def Function_8_A23(): pass

    label("Function_8_A23")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AAE")
    OP_43(0xFE, 0x2, 0x0, 0x9)
    OP_22(0x191, 0x0, 0x64)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AAE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x38B, 1)"), scpexpr(EXPR_END)), "loc_AAE")
    TalkBegin(0xFE)
    OP_A2(0x9)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "新鲜鸡蛋\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFE)

    label("loc_AAE")

    Return()

    # Function_8_A23 end

    def Function_9_AAF(): pass

    label("Function_9_AAF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_ACA")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_48()
    Jump("Function_9_AAF")

    label("loc_ACA")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_9_AAF end

    def Function_10_AD5(): pass

    label("Function_10_AD5")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_BCD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B6E")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "啊～啊， \x01",
            "我可是在柏斯出生的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为柏斯市\x01",
            "没有果树园，\x01",
            "我都帮不上什么忙。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BCA")

    label("loc_B6E")


    ChrTalk(
        0xFE,
        (
            "因为我在柏斯市出生，\x01",
            "所以无法在果树园帮忙。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BCA")

    Jump("loc_115D")

    label("loc_BCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_C37")

    ChrTalk(
        0xFE,
        (
            "大人也有\x01",
            "大人要做的事情啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "真头痛。\x02",
    )

    CloseMessageWindow()
    Jump("loc_115D")

    label("loc_C37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_CB4")

    ChrTalk(
        0xFE,
        (
            "库赖爷爷和贝斯卡\x01",
            "又在吵架了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "最近经常能听到呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_115D")

    label("loc_CB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 5)), scpexpr(EXPR_END)), "loc_E56")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DD0")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        "我是从鲁伊那里听说的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "姐姐你们\x01",
            "是游击士对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "好厉害，\x01",
            "女人也能够成为游击士啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我觉得如果不是像阿加特\x01",
            "那样厉害是办不到的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E53")

    label("loc_DD0")


    ChrTalk(
        0xFE,
        (
            "原来女人也能够\x01",
            "成为游击士啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我觉得如果不是像阿加特\x01",
            "那样厉害是办不到的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E53")

    Jump("loc_115D")

    label("loc_E56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 4)), scpexpr(EXPR_END)), "loc_1071")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FA3")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "鲁伊的话不可信，\x01",
            "也有他自身的原因吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "也有人说，\x01",
            "说不定那怪影可能是龙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "龙是很久以前的生物吧？\x01",
            "这种说法就更不可信了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_106E")

    label("loc_FA3")


    ChrTalk(
        0xFE,
        (
            "鲁伊的话不可信，\x01",
            "也有他自身的原因吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "龙是很久以前的生物吧？\x01",
            "这种说法就更不可信了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_106E")

    Jump("loc_115D")

    label("loc_1071")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_10C6")

    ChrTalk(
        0xFE,
        (
            "最近，\x01",
            "鲁伊都没过来玩啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "发生什么事了？\x02",
    )

    CloseMessageWindow()
    Jump("loc_115D")

    label("loc_10C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_115D")

    ChrTalk(
        0xFE,
        (
            "你们说鲁伊啊，\x01",
            "他应该是看错了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "不会是星星看多了吧？\x02",
    )

    CloseMessageWindow()

    label("loc_115D")

    TalkEnd(0x8)
    Return()

    # Function_10_AD5 end

    def Function_11_1161(): pass

    label("Function_11_1161")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_126D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_120A")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "如果出生在商人之家，\x01",
            "可能会更麻烦吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为巴德斯\x01",
            "可不擅长学习。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_126A")

    label("loc_120A")


    ChrTalk(
        0xFE,
        (
            "如果出生在商人之家，\x01",
            "我想那一定更痛苦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_126A")

    Jump("loc_16A7")

    label("loc_126D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_12C0")

    ChrTalk(
        0xFE,
        (
            "既然住在同一个村里，\x01",
            "大家应该和平友好。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16A7")

    label("loc_12C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_1313")

    ChrTalk(
        0xFE,
        (
            "贝斯卡是前不久\x01",
            "才来到这个村里的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他是个平时很温柔，\x01",
            "认真起来也非常酷的大哥哥。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16A7")

    label("loc_1313")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 5)), scpexpr(EXPR_END)), "loc_143E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13EA")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "事到如今，\x01",
            "巴德斯还在说什么啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "从今以后\x01",
            "将是女性的时代了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "看罗亚家就知道，\x01",
            "他夫人比他厉害多了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "还有，女王陛下也是女性。\x02",
    )

    CloseMessageWindow()
    Jump("loc_143B")

    label("loc_13EA")


    ChrTalk(
        0xFE,
        (
            "事到如今，\x01",
            "巴德斯还在说什么啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "从今以后\x01",
            "将是女性的时代了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_143B")

    Jump("loc_16A7")

    label("loc_143E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 4)), scpexpr(EXPR_END)), "loc_15CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1523")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "我觉得巴德斯\x01",
            "说得一点都没错……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "听说爸爸们小的时候，\x01",
            "那一带附近还有龙哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "只要一次就好，\x01",
            "我也想见见龙啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15CC")

    label("loc_1523")


    ChrTalk(
        0xFE,
        (
            "听说爸爸们小的时候，\x01",
            "那一带附近还有龙哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "只要一次就好，\x01",
            "我也想见见龙啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15CC")

    Jump("loc_16A7")

    label("loc_15CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_1665")

    ChrTalk(
        0xFE,
        (
            "咦……\x01",
            "大姐姐你们是客人？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "要找村长家的话，\x01",
            "登上里面的坡道就是了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16A7")

    label("loc_1665")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_16A7")

    ChrTalk(
        0xFE,
        "大姐姐，你们是谁？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "柏斯的商人吗？\x02",
    )

    CloseMessageWindow()

    label("loc_16A7")

    TalkEnd(0x9)
    Return()

    # Function_11_1161 end

    def Function_12_16AB(): pass

    label("Function_12_16AB")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_1B69")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x71, 6)), scpexpr(EXPR_END)), "loc_17FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1799")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "过去，\x01",
            "这里曾经发生过一场大战。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "村里有好几个人\x01",
            "在战争中死去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我也想和\x01",
            "帝国的人交朋友……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "可是……\x01",
            "我讨厌悲伤的事情。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17FC")

    label("loc_1799")


    ChrTalk(
        0xFE,
        (
            "我也想和\x01",
            "帝国的人交朋友……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "可是……\x01",
            "我讨厌悲伤的事情。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17FC")

    Jump("loc_1B66")

    label("loc_17FF")

    OP_A2(0x38E)
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        "啊，是姐姐啊！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F你好啊～鲁伊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那之后，\x01",
            "军队就来把姐姐们带走了，\x01",
            "把我吓死了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "姐姐们明明\x01",
            "什么坏事也没有做啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "没什么事吧？\x01",
            "他们没有刁难你们吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F哎呀呀，\x01",
            "让你为我们担心了……\x02\x03",
            "#006F没事啦，\x01",
            "你看我现在不是很有活力吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "嗯，那就好……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我所看到的那个，\x01",
            "果然是飞艇啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "姐姐， \x01",
            "谢谢你为我作证！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F嗯……\x02\x03",
            "不过最后反正会被\x01",
            "王国军证明清楚，\x01",
            "我的心里还真不是滋味啊……\x02\x03",
            "他们还把我们\x01",
            "误认为空贼而抓走了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F算了，\x01",
            "这次虽然有些丢脸，\x01",
            "不过我们还是守住了约定……\x02\x03",
            "这不是挺好吗。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B66")

    Jump("loc_301E")

    label("loc_1B69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_1F3A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EE5")
    OP_A2(0x2)
    OP_A2(0x38E)
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        "啊，是姐姐啊！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F你好啊～鲁伊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那之后，\x01",
            "军队就来把姐姐们带走了，\x01",
            "把我吓死了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "姐姐们明明\x01",
            "什么坏事也没有做啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "没什么事吧？\x01",
            "他们没有刁难你们吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F哎呀呀，\x01",
            "让你为我们担心了……\x02\x03",
            "#006F没事啦，\x01",
            "你看我现在不是很有活力吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "嗯，那就好……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我所看到的那个，\x01",
            "果然是飞艇啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "姐姐， \x01",
            "谢谢你为我作证！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F嗯……\x02\x03",
            "不过最后反正会被\x01",
            "王国军证明清楚，\x01",
            "我的心里还真不是滋味啊……\x02\x03",
            "他们还把我们\x01",
            "误认为空贼而抓走了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F算了，\x01",
            "这次虽然有些丢脸，\x01",
            "不过我们还是守住了约定……\x02\x03",
            "这不是挺好吗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F37")

    label("loc_1EE5")


    ChrTalk(
        0xFE,
        (
            "姐姐，\x01",
            "谢谢你们为我的话作证！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F37")

    Jump("loc_301E")

    label("loc_1F3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 5)), scpexpr(EXPR_END)), "loc_20A3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2086")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        "是、是姐姐你们啊！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "怎样，找到什么线索了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F嗯～\x01",
            "还不能说是很清楚的线索……\x02\x03",
            "不过，你所看到的东西\x01",
            "真的不是什么梦境。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        "真的！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F现在我们要开始仔细调查，\x01",
            "你就等着好消息吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "嗯！\x01",
            "大姐姐你们要加油啊！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20A0")

    label("loc_2086")


    ChrTalk(
        0xFE,
        "大姐姐你们要加油啊！\x02",
    )

    CloseMessageWindow()

    label("loc_20A0")

    Jump("loc_301E")

    label("loc_20A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 4)), scpexpr(EXPR_END)), "loc_2127")

    ChrTalk(
        0xFE,
        (
            "在空中飞翔的两个影子\x01",
            "向北方飞去了，\x01",
            "然后就那样看不见了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我敢说\x01",
            "那个绝对不是在做梦！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_301E")

    label("loc_2127")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_2FE5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2F9B")
    OP_A2(0x31C)
    OP_28(0x36, 0x1, 0x8)
    OP_28(0x36, 0x1, 0x10)
    EventBegin(0x0)
    Fade(1000)
    OP_6D(34870, -3850, 9830, 0)
    OP_6B(2800, 0)
    OP_6C(135000, 0)
    SetChrPos(0x101, 35122, -3850, 10423, 180)
    SetChrPos(0x102, 35484, -3850, 11571, 180)
    SetChrPos(0x103, 34518, -3850, 11700, 180)
    TurnDirection(0xFE, 0x101, 0)
    OP_0D()

    ChrTalk(
        0xFE,
        (
            "哎～\x01",
            "我没见过大姐姐你们呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "是来这里买水果的商人吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F呵呵，不是呢。\x02\x03",
            "不瞒你说，我们是游击士哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "游击士？\x01",
            "和阿加特大哥哥一样吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "可是大姐姐，\x01",
            "你看起来好像不是很强呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#007F呜～\x01",
            "说得还真直接……\x02\x03",
            "#006F那么，让你见识一下我华丽的棒术吧，\x01",
            "这样就肯定不会再说同样的话了！\x02",
        )
    )

    CloseMessageWindow()
    Fade(1500)
    SetChrChipByIndex(0x101, 10)
    OP_6C(0, 1500)
    Sleep(500)
    Fade(250)
    SetChrChipByIndex(0x101, 8)
    OP_22(0x7E, 0x1, 0x64)

    def lambda_23D3():

        label("loc_23D3")

        OP_99(0xFE, 0x0, 0x7, 0xBB8)
        OP_48()
        Jump("loc_23D3")

    QueueWorkItem2(0x101, 0, lambda_23D3)
    Sleep(2000)
    OP_62(0xFE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_95(0xFE, 0x0, 0x0, 0x0, 0x320, 0x1F40)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "哇、哇哇！\x01",
            "棍子耍得骨碌转，好厉害呀！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)
    OP_44(0x101, 0xFF)
    OP_23(0x7E)
    OP_99(0x101, 0x0, 0xA, 0x7D0)
    OP_22(0x1F4, 0x0, 0x64)
    OP_99(0x101, 0xB, 0x13, 0x7D0)
    Sleep(300)

    ChrTalk(
        0x101,
        "#502F哈哈，知道我的厉害了吧。\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x101, 65535)
    OP_6C(135000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#001F再给你看个更厉害的招式……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#017F艾丝蒂尔，闹过头了。\x02\x03",
            "#010F对了……\x01",
            "你就是鲁伊吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "啊，是呀……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "为什么哥哥会知道我的名字呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F是从村长那里听说的。\x01",
            "你看到了夜空中飞过的影子是吧。\x02\x03",
            "我们想听你说说当时的情景。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "哎，可是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "士兵叔叔已经调查过了，\x01",
            "什么也没找到……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F嗯，那样也没关系的。\x01",
            "给我们讲一遍那晚发生的事好吗？\x02\x03",
            "越详细越好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "啊～嗯……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那个那个……\x01",
            "我非常喜欢看星星。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "所以，我经常半夜\x01",
            "从家里跑出来到这里看星星……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "前几天的晚上，\x01",
            "我看到有两个影子在夜空中飞过。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F哎，先停一下……\x02\x03",
            "夜空中飞过的影子有两个？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "是啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "啊，不过大小不一样哦。\x01",
            "就好像是大人带着孩子似的呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F大小不同的两个影子……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#022F定期船和空贼飞艇……\x01",
            "这么想的话就说得通了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F确实，在森林里见过的空贼飞艇\x01",
            "比定期船体形要小呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "然后，那两个影子\x01",
            "就向着北边的方向飞去……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "接着就那样消失了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F北边的方向……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F从村子的后村口出去，\x01",
            "会有一条通往北边的山道。\x02\x03",
            "山道尽头是一个七耀石矿山，\x01",
            "不过据说那里很久之前就成了废坑。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "士兵叔叔们虽然把北面的山道\x01",
            "彻底地搜查了一遍，\x01",
            "但是什么也没找到呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "所以呢，\x01",
            "他们都说是我睡迷糊了梦见的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "而且……\x01",
            "他们还把我当成傻瓜嘲笑了一番呢……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "说着说着，小男孩的眼眶已经湿润了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(
        0x101,
        (
            "#004F啊，怎么了……\x01",
            "男孩子不能这么轻易地哭哦！\x02",
        )
    )

    CloseMessageWindow()
    OP_92(0x101, 0xFE, 0x320, 0xBB8, 0x0)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#006F我们和士兵们可不一样哦。\x02\x03",
            "你说的话绝对不是在做梦，\x01",
            "我们一定会证明给你看的！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "真、真的……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F真的真的。\x01",
            "就交给姐姐我们吧！\x02\x03",
            "所以呢，\x01",
            "你可不能总是哭哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "啊～嗯……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "姐姐，你真是个好人！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#027F（呵呵，还是老样子，\x01",
            "　到哪里都这么受小孩子欢迎。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F（嗯……\x01",
            "　这大概也是她的优点所在吧。）\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 400)

    ChrTalk(
        0x101,
        "#501F嗯？怎么了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F没有，没什么。\x02\x03",
            "好了，我们下一步\x01",
            "要做的事情应该很清楚了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F嗯！\x02\x03",
            "赶快从后村口出发，\x01",
            "到北面的山道调查一下吧！\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Jump("loc_2FE2")

    label("loc_2F9B")


    ChrTalk(
        0xFE,
        "呼哧，没有人愿意相信我……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "那明明不是在做梦呀……\x02",
    )

    CloseMessageWindow()

    label("loc_2FE2")

    Jump("loc_301E")

    label("loc_2FE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_301E")

    ChrTalk(
        0xFE,
        "我说了我真的看到过的……\x02",
    )

    CloseMessageWindow()

    label("loc_301E")

    TalkEnd(0xA)
    Return()

    # Function_12_16AB end

    def Function_13_3022(): pass

    label("Function_13_3022")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_30F5")

    ChrTalk(
        0xFE,
        (
            "如果贝斯卡与库赖爷爷\x01",
            "能够在这次的集会上\x01",
            "达成和解就好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果那两人合作的话，\x01",
            "我想这个村子的果树园\x01",
            "会越来越兴旺的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37F5")

    label("loc_30F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_31FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31A8")
    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "这两天，\x01",
            "村长准备召开集会\x01",
            "讨论栽培的方针。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "如果有进展就好了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_31F8")

    label("loc_31A8")


    ChrTalk(
        0xFE,
        "波波那家伙现在怎么样了呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "他在柏斯过得好不好啊。\x02",
    )

    CloseMessageWindow()

    label("loc_31F8")

    Jump("loc_37F5")

    label("loc_31FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 5)), scpexpr(EXPR_END)), "loc_33B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32CA")
    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "我也明白\x01",
            "库赖爷爷说的话。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是，我觉得\x01",
            "贝斯卡所说的话更加有道理。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这件事对村里来说也很重要，\x01",
            "应该找一个机会让大家好好谈谈才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33B2")

    label("loc_32CA")


    ChrTalk(
        0xFE,
        (
            "如果不解决这个问题，\x01",
            "肯定是后患无穷，我也没有办法去柏斯。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我还是试着\x01",
            "向村长提议一下，\x01",
            "就果树栽培的方针进行一次谈话吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33B2")

    Jump("loc_37F5")

    label("loc_33B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 4)), scpexpr(EXPR_END)), "loc_357D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34F9")
    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "今天库赖爷爷\x01",
            "又和贝斯卡吵架了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "库赖爷爷在\x01",
            "开展果树栽培之前\x01",
            "就在村里种植水果了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "矿山封闭之后，\x01",
            "能够在村里重建果树园\x01",
            "都是爷爷的功劳。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "就凭这个，\x01",
            "爷爷他也有不肯让步的地方吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_357A")

    label("loc_34F9")


    ChrTalk(
        0xFE,
        (
            "今天库赖爷爷\x01",
            "又和贝斯卡吵架了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "库赖爷爷也有\x01",
            "许多不肯让步的地方吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_357A")

    Jump("loc_37F5")

    label("loc_357D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_37AF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36F5")
    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "其实，我准备放弃果园的，\x01",
            "打算在柏斯开家小店做生意了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是，\x01",
            "这个村里还有着各种各样的问题。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不把那些解决的话，\x01",
            "我没办法放心离去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "所以我安排\x01",
            "妻子和儿子先去柏斯了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37AC")

    label("loc_36F5")


    ChrTalk(
        0xFE,
        (
            "其实，我准备放弃果园的，\x01",
            "打算在柏斯开家小店做生意了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我安排妻子和儿子\x01",
            "先去柏斯等着我。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37AC")

    Jump("loc_37F5")

    label("loc_37AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_37F5")

    ChrTalk(
        0xFE,
        (
            "呼，库赖爷爷也真是的，\x01",
            "不管我怎么费尽口舌，他也听不进去……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37F5")

    TalkEnd(0xB)
    Return()

    # Function_13_3022 end

    def Function_14_37F9(): pass

    label("Function_14_37F9")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xE, 0x0, 0x4)"), scpexpr(EXPR_END)), "loc_3DA7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xE, 0x1, 0x2000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CFE")
    OP_28(0xE, 0x1, 0x2000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xE, 0x1, 0x4000)"), scpexpr(EXPR_END)), "loc_3A77")
    OP_28(0xE, 0x1, 0x4000)

    ChrTalk(
        0xC,
        (
            "非常抱歉，\x01",
            "前方地带现在禁止进入。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "详细的情况\x01",
            "请去询问村长吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯，关于委托的事情，\x01",
            "村长都告诉我们了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 400)

    ChrTalk(
        0xC,
        "哎，委托……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "难道说，\x01",
            "你们是游击士协会的人？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#020F嗯，没错。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x103, 400)

    ChrTalk(
        0xC,
        "那就太好了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "请赶快帮我们\x01",
            "消灭那些魔兽吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "很快就要进入\x01",
            "种植树苗的季节了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x0, 400)

    ChrTalk(
        0xC,
        (
            "……那么，请小心。\x01",
            "拜托你们了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CFB")

    label("loc_3A77")

    OP_28(0xE, 0x1, 0x4000)

    ChrTalk(
        0xC,
        (
            "非常抱歉，\x01",
            "前方地带现在禁止进入。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "不是我吓你们，\x01",
            "这里面的山道上\x01",
            "出现了非常凶暴的魔兽。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F啊，我们正是\x01",
            "接受了村长的委托而来的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 400)

    ChrTalk(
        0xC,
        "啊……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "难道说，\x01",
            "你们是游击士协会的人？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#020F嗯，没错。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x103, 400)

    ChrTalk(
        0xC,
        "那就太好了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "很快就要进入\x01",
            "种植树苗的季节了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "在开始忙碌之前，\x01",
            "请一定要帮我们消灭魔兽。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x0, 400)

    ChrTalk(
        0xC,
        (
            "那么，\x01",
            "请你们多加小心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CFB")

    Jump("loc_3DA4")

    label("loc_3CFE")


    ChrTalk(
        0xFE,
        (
            "很快就要\x01",
            "进入种植树苗的季节了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在开始忙碌之前，\x01",
            "拜托你们消灭掉魔兽。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那么，\x01",
            "请你们多加小心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DA4")

    Jump("loc_409E")

    label("loc_3DA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FDF")
    OP_A2(0x4)
    OP_28(0xE, 0x1, 0x4000)

    ChrTalk(
        0xC,
        (
            "非常抱歉，\x01",
            "前方地带现在禁止进入。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "不是我吓你们，\x01",
            "这里面的山道上\x01",
            "出现了非常凶暴的魔兽。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xE, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F26")

    ChrTalk(
        0x101,
        (
            "#004F咦……？！\x01",
            "有这样的传言吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 400)

    ChrTalk(
        0xC,
        (
            "只是传言的话就好了，\x01",
            "不过看起来应该是真的呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F26")

    TurnDirection(0xC, 0x0, 400)

    ChrTalk(
        0xC,
        (
            "详细的情况，\x01",
            "请去询问村长吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "以防万一，\x01",
            "我们委托了游击士协会来消灭魔兽。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_409E")

    label("loc_3FDF")


    ChrTalk(
        0xC,
        (
            "前方地带现在禁止进入。\x01",
            "详细的情况就请去问村长吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xC, 180, 400)

    ChrTalk(
        0xC,
        (
            "看，\x01",
            "往那边不是能看到屋顶吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "那就是村长的家了。\x02",
    )

    CloseMessageWindow()

    label("loc_409E")

    TalkEnd(0xC)
    Return()

    # Function_14_37F9 end

    def Function_15_40A2(): pass

    label("Function_15_40A2")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_421E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4190")
    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "我想试着在村里的\x01",
            "集会上提出我的想法。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然到最后，\x01",
            "我总是和库赖爷爷发生争吵……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我觉得还是应该冷静下来，\x01",
            "大家一起好好商量。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_421B")

    label("loc_4190")


    ChrTalk(
        0xFE,
        (
            "虽然到最后，\x01",
            "我总是和库赖爷爷发生争吵……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我觉得还是应该冷静下来，\x01",
            "大家一起好好商量。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_421B")

    Jump("loc_4A42")

    label("loc_421E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_43EC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43B3")
    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "总是使用\x01",
            "古老的方法也不行吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "多考虑一下总体的效率，\x01",
            "能够定期送货上市的独特想法\x01",
            "也是很必要的啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这里已经结果的树\x01",
            "都比大家的身高要高不少吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这也是我在集会上\x01",
            "打算要提出的内容。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "只要减少高空的作业，\x01",
            "也就不需要这么多人手了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43E9")

    label("loc_43B3")


    ChrTalk(
        0xFE,
        (
            "唉……\x01",
            "为什么我的提议他不愿意接受呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43E9")

    Jump("loc_4A42")

    label("loc_43EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 5)), scpexpr(EXPR_END)), "loc_4655")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45BC")
    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "我的意思可不是说\x01",
            "无论如何也要实行机械化啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "本来果树栽培的作业\x01",
            "要实行机械化就非常困难。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "就算拥有导力机械，\x01",
            "要依赖手工作业的部分仍然很多。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是，\x01",
            "这个村里并没有十分充足的人手啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我觉得该交给机械做的事情，\x01",
            "还是应该让机械来完成。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4652")

    label("loc_45BC")


    ChrTalk(
        0xFE,
        (
            "我好几次都想和库赖爷爷\x01",
            "好好谈一下……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "你别误会哦，\x01",
            "他只是有点钻牛角尖而已。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4652")

    Jump("loc_4A42")

    label("loc_4655")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 4)), scpexpr(EXPR_END)), "loc_47CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4745")
    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "库赖爷爷认为\x01",
            "我是为了能够轻松地工作\x01",
            "才依赖于机械作业的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "那可是个很大的误会……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我认为应该吸收各种果树栽培的技术，\x01",
            "然后慢慢提高进步。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47C8")

    label("loc_4745")


    ChrTalk(
        0xFE,
        (
            "库赖爷爷认为\x01",
            "我是为了能够轻松地工作\x01",
            "才依赖于机械作业的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "那可是个很大的误会……\x02",
    )

    CloseMessageWindow()

    label("loc_47C8")

    Jump("loc_4A42")

    label("loc_47CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_49B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48EA")
    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "我想成为果树农学家。\x01",
            "在数年前我来到了这个村庄。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "很早以前我就做了很多研究，\x01",
            "买齐了最新式的导力农机器具。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "为了不输给其他人，\x01",
            "我要种出更多的水果拿到外面出售。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49B4")

    label("loc_48EA")


    ChrTalk(
        0xFE,
        (
            "我想成为果树农学家。\x01",
            "在数年前我来到了这个村庄。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "很早以前我就做了很多研究，\x01",
            "买齐了最新式的导力农机器具。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49B4")

    Jump("loc_4A42")

    label("loc_49B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_4A42")

    ChrTalk(
        0xFE,
        "你好，来果树园参观吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "反正也不会少些什么，\x01",
            "慢慢四处看看吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A42")

    TalkEnd(0xD)
    Return()

    # Function_15_40A2 end

    def Function_16_4A46(): pass

    label("Function_16_4A46")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_4ACC")

    ChrTalk(
        0xFE,
        (
            "我丈夫去参加集会了，\x01",
            "很晚才能回来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果能和库赖爷爷\x01",
            "好好谈谈就好了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4EB4")

    label("loc_4ACC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_4B5F")

    ChrTalk(
        0xFE,
        (
            "我是永远站在\x01",
            "我丈夫这一边的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "夫妻之间要相互信赖\x01",
            "才能够天长地久。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4EB4")

    label("loc_4B5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_4BFA")

    ChrTalk(
        0xFE,
        (
            "我很希望库赖爷爷\x01",
            "也能够理解我丈夫的想法。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "一定会为村子带来好处的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4EB4")

    label("loc_4BFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 5)), scpexpr(EXPR_END)), "loc_4CFC")

    ChrTalk(
        0xFE,
        (
            "我也非常喜欢\x01",
            "种植水果的生活，\x01",
            "我觉得能跟着我丈夫来这里真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "花了不少时间，\x01",
            "终于能和村里的人融洽相处了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过还是有例外的，\x01",
            "那就是库赖爷爷了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4EB4")

    label("loc_4CFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 4)), scpexpr(EXPR_END)), "loc_4DBB")

    ChrTalk(
        0xFE,
        (
            "丈夫说得对，\x01",
            "库赖爷爷一定是\x01",
            "误解我们的意思了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我想双方静下心来好好交谈的话，\x01",
            "就一定能够达成一致的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4EB4")

    label("loc_4DBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_4E5B")

    ChrTalk(
        0xFE,
        (
            "我丈夫贝斯卡\x01",
            "非常热衷于研究呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "白天就像这样在果园里工作，\x01",
            "晚上就在研究各种各样的栽培方法。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4EB4")

    label("loc_4E5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_4EB4")

    ChrTalk(
        0xFE,
        "马上就要到午休的时间了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "要赶快把\x01",
            "工作都给解决掉。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4EB4")

    TalkEnd(0xE)
    Return()

    # Function_16_4A46 end

    def Function_17_4EB8(): pass

    label("Function_17_4EB8")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_4F28")

    ChrTalk(
        0xFE,
        (
            "在下次集会的时候，\x01",
            "我要让村里的年轻人\x01",
            "再注意一下做法才行啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5397")

    label("loc_4F28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_4FDF")

    ChrTalk(
        0xFE,
        (
            "要尽量让果树\x01",
            "保持自然生长，\x01",
            "这才是最重要的啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "就是要肯花时间，\x01",
            "才能种出美味的水果。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5397")

    label("loc_4FDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 5)), scpexpr(EXPR_END)), "loc_51AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50E6")
    OP_A2(0x7)

    ChrTalk(
        0xFE,
        (
            "贝斯卡的做法\x01",
            "太过依赖导力器这类的东西了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那家伙种出来的水果\x01",
            "在口味方面肯定\x01",
            "要比我的逊色许多。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他那种东西\x01",
            "是不可以作为\x01",
            "拉文努村的水果对外销售的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51AB")

    label("loc_50E6")


    ChrTalk(
        0xFE,
        (
            "那家伙种出来的水果\x01",
            "在口味方面肯定\x01",
            "要比我的逊色许多。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他那种东西\x01",
            "是不可以作为\x01",
            "拉文努村的水果对外销售的……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51AB")

    Jump("loc_5397")

    label("loc_51AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 4)), scpexpr(EXPR_END)), "loc_527C")

    ChrTalk(
        0xFE,
        (
            "年轻人栽培果树\x01",
            "真是大手大脚的啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不考虑产品的质量和口味， \x01",
            "一味追求数量来进行作业。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "真是可悲啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_5397")

    label("loc_527C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_5334")

    ChrTalk(
        0xFE,
        (
            "在这个村还是\x01",
            "以矿山而繁荣的时候，\x01",
            "我就开始在这里种植水果了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在完美培育水果方面，\x01",
            "我可不会输给村里的任何人。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5397")

    label("loc_5334")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_5397")

    ChrTalk(
        0xFE,
        (
            "嗯，今年的气候也很好，\x01",
            "所有的果实看上去都熟透了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5397")

    TalkEnd(0xF)
    Return()

    # Function_17_4EB8 end

    def Function_18_539B(): pass

    label("Function_18_539B")

    TalkBegin(0x11)
    EventBegin(0x0)
    Fade(1000)
    OP_6D(31970, 8000, 37320, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2920, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 32990, 8000, 38280, 180)
    SetChrPos(0x102, 33860, 8000, 39820, 180)
    SetChrPos(0x103, 31890, 8000, 39180, 180)
    OP_8C(0x11, 0, 400)
    OP_0D()

    ChrTalk(
        0x101,
        "#000F村长，您在这里啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1P哦，是刚才几位游击士啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#020F……好宏伟的坟墓啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#1P这是为了悼念十年前\x01",
            "战争中的牺牲者而建造的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#1P柏斯地区因为离帝国很近，\x01",
            "所以也成了战争中最惨烈的地方……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#1P这村子也被战火无情地席卷了，\x01",
            "不知多少人为此献出了自己的生命。\x02",
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
        "#013F………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#1P哈哈，不好意思，\x01",
            "让你们几位也触景生情了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#1P来这里打扫，\x01",
            "已经是我每天的必做之事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#1P话说回来，发生什么事了？\x01",
            "有什么我能帮忙的地方吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F啊，是的。\x01",
            "有件事想和您商量一下。\x02\x03",
            "啊，在这之前……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F来到这里也算是缘分，\x01",
            "能不能让我们先拜祭一下呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F虽然没有鲜花……\x01",
            "至少让我们向为了保卫祖国\x01",
            "而献身的人们祈祷一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1P哦，这样啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#1P当然没关系了。\x01",
            "你们能这样做，他们也会高兴吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3FA)
    FadeToDark(2000, 0, -1)
    NewScene("ED6_DT01/T1210   ._SN", 100, 0, 0)
    IdleLoop()
    TalkEnd(0x11)
    Return()

    # Function_18_539B end

    def Function_19_589D(): pass

    label("Function_19_589D")

    OP_A2(0x368)
    OP_28(0x36, 0x1, 0x2)
    EventBegin(0x0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    SetChrPos(0x101, 560, 0, 13490, 225)
    SetChrPos(0x102, 510, 0, 11530, 0)
    SetChrPos(0x103, -820, 0, 12480, 90)
    OP_6D(110, 0, 13180, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0x103,
        (
            "#020F接下来……\x02\x03",
            "先试着调查一下\x01",
            "这次事件的目击情报吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F那样的话，\x01",
            "先向村里的人都打听一下吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F突然问村民的话会让人怀疑的。\x02\x03",
            "总之，还是先听听\x01",
            "这里的村长是怎么说的吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F嗯，知道了。\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_19_589D end

    def Function_20_5A60(): pass

    label("Function_20_5A60")

    EventBegin(0x0)
    OP_6B(3800, 0)
    OP_6C(90000, 0)
    OP_6D(23730, 0, 31170, 0)
    SetChrPos(0x101, 560, 0, 13490, 0)
    SetChrPos(0x102, 510, 0, 11530, 0)
    SetChrPos(0x103, -820, 0, 12480, 0)
    StopSound(0x9470, 0x30D40, 0x0)
    FadeToBright(2000, 0)

    def lambda_5AD4():
        OP_6C(45000, 8000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5AD4)
    OP_6D(820, 0, 19100, 8000)
    Fade(2000)
    OP_6D(110, 0, 13180, 0)
    OP_6B(2800, 0)
    StopSound(0x9470, 0x186A0, 0x1F40)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#000F这里就是拉文努村……\x01",
            "真是个悠闲舒适的地方啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    ChrTalk(
        0x101,
        "#000F啊，那边有个果树园。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x102, 90, 400)
    OP_8C(0x103, 90, 400)

    ChrTalk(
        0x103,
        (
            "#020F现在这里是以种植水果闻名，\x01",
            "不过以前可是靠采矿业而兴旺的哦。\x02\x03",
            "据说村子北面有一个\x01",
            "已经被废弃的七耀石矿山呢。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5C5B():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5C5B)
    TurnDirection(0x102, 0x103, 400)

    ChrTalk(
        0x102,
        (
            "#010F了解得非常详细啊，\x01",
            "雪拉姐姐以前来过这里吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F嗯，为了成为正游击士，\x01",
            "我在巡回修行的时候来过这村子。\x02\x03",
            "那时候，我可是没有乘飞艇，\x01",
            "而是徒步走遍了全国的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F啊，为什么呢？\x01",
            "坐飞艇多方便啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#026F『飞艇的确很方便，\x01",
            "　可以在五大城市间任意往来。』\x02\x03",
            "『而这种方便一旦变成了习惯，\x01",
            "　就会减少许多在各地修行时的阅历。』\x02\x03",
            "『要守护一片土地，\x01",
            "　首先就要自己脚踏实地去看一看……』\x02\x03",
            "#020F——这些话\x01",
            "是卡西乌斯老师的教导呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F哎，是老爸他……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F确实如此，如果发生了事件，\x01",
            "而之前从没去过事发地点的话，\x01",
            "很有可能会延误到达的时间。\x02\x03",
            "而且在追击犯人的时候，\x01",
            "熟悉地理环境才能处于有利的局面……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_608C")

    ChrTalk(
        0x103,
        (
            "#021F呵呵，正是如此。\x02\x03",
            "你们如果有机会的话，\x01",
            "最好也尝试一下哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6216")

    label("loc_608C")

    OP_A2(0x368)
    OP_28(0x36, 0x1, 0x2)

    ChrTalk(
        0x103,
        (
            "#021F呵呵，正是如此。\x02\x03",
            "#020F接下来，不管怎么说……\x02\x03",
            "先试着调查一下\x01",
            "这次事件的目击情报吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F那样的话，\x01",
            "先向村里的人都打听一下吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F突然问村民的话会让人怀疑的。\x02\x03",
            "总之，还是先听听\x01",
            "这里的村长是怎么说的吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F嗯，知道了。\x02",
    )

    CloseMessageWindow()

    label("loc_6216")

    EventEnd(0x0)
    Return()

    # Function_20_5A60 end

    def Function_21_6219(): pass

    label("Function_21_6219")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "门上着锁，无法打开。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_21_6219 end

    def Function_22_6261(): pass

    label("Function_22_6261")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xE, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0xE, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6276")
    Return()

    label("loc_6276")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xE, 0x0, 0x4)"), scpexpr(EXPR_END)), "loc_675F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xE, 0x1, 0x2000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_675C")
    OP_28(0xE, 0x1, 0x2000)
    TalkBegin(0xC)
    EventBegin(0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xE, 0x1, 0x4000)"), scpexpr(EXPR_END)), "loc_64CC")
    OP_28(0xE, 0x1, 0x4000)

    ChrTalk(
        0xC,
        (
            "非常抱歉，\x01",
            "前方地带现在禁止进入。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "我不是说过了吗？\x01",
            "这里可能有凶暴的魔兽出没。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯，\x01",
            "村长先生已经委托我们了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 400)

    ChrTalk(
        0xC,
        "啊……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "难道说，\x01",
            "你们是游击士协会的人？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#020F嗯，没错。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x103, 400)

    ChrTalk(
        0xC,
        "那就太好了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "请赶快帮我们\x01",
            "消灭那些魔兽吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "很快就要进入\x01",
            "种植树苗的季节了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x0, 400)

    ChrTalk(
        0xC,
        (
            "……那么，请小心。\x01",
            "拜托你们了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6757")

    label("loc_64CC")

    OP_28(0xE, 0x1, 0x4000)

    ChrTalk(
        0xC,
        (
            "非常抱歉，\x01",
            "前方地带现在禁止进入。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "不是我吓你们，\x01",
            "这里面的山道上\x01",
            "出现了非常凶暴的魔兽。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F啊，我们正是\x01",
            "接受了村长的委托而来的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 400)

    ChrTalk(
        0xC,
        "啊……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "难道说，\x01",
            "你们是游击士协会的人？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#020F嗯，没错。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x103, 400)

    ChrTalk(
        0xC,
        "那就太好了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "很快就要进入\x01",
            "种植树苗的季节了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "在开始忙碌之前，\x01",
            "请一定要帮我们消灭魔兽。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x0, 400)

    ChrTalk(
        0xC,
        (
            "那么，\x01",
            "请你们多加小心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6757")

    EventEnd(0x3)
    TalkEnd(0xC)

    label("loc_675C")

    Jump("loc_6A81")

    label("loc_675F")

    TalkBegin(0xC)
    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_69A4")
    OP_A2(0x4)
    OP_28(0xE, 0x1, 0x4000)

    ChrTalk(
        0xC,
        (
            "非常抱歉，\x01",
            "前方地带现在禁止进入。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "不是我吓你们，\x01",
            "这里面的山道上\x01",
            "出现了非常凶暴的魔兽。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xE, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_68EB")

    ChrTalk(
        0x101,
        (
            "#004F咦……？！\x01",
            "有这样的传言吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 400)

    ChrTalk(
        0xC,
        (
            "只是传言的话就好了，\x01",
            "不过看起来应该是真的呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_68EB")

    TurnDirection(0xC, 0x0, 400)

    ChrTalk(
        0xC,
        (
            "详细的情况，\x01",
            "请去询问村长吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "以防万一，\x01",
            "我们委托了游击士协会来消灭魔兽。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A63")

    label("loc_69A4")


    ChrTalk(
        0xC,
        (
            "前方地带现在禁止进入。\x01",
            "详细的情况就请去问村长吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xC, 180, 400)

    ChrTalk(
        0xC,
        (
            "看，\x01",
            "往那边不是能看到屋顶吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "那就是村长的家了。\x02",
    )

    CloseMessageWindow()

    label("loc_6A63")

    OP_90(0x0, 0x0, 0x0, 0xFFFFF830, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    TalkEnd(0xC)

    label("loc_6A81")

    Return()

    # Function_22_6261 end

    def Function_23_6A82(): pass

    label("Function_23_6A82")

    FadeToBright(1000, 0)
    SetMapFlags(0x400000)
    EventBegin(0x0)
    OP_6C(45000, 0)
    OP_6D(9600, 8000, 68460, 0)

    def lambda_6AB2():
        OP_6D(7080, 8000, 66150, 3000)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_6AB2)
    SetChrPos(0xC, 5430, 8000, 66280, 180)
    SetChrPos(0x101, 7080, 8000, 68150, 180)
    SetChrPos(0x102, 7580, 8000, 69650, 180)
    SetChrPos(0x103, 6530, 8000, 69110, 180)

    def lambda_6B0E():
        OP_90(0x101, 0x0, 0x0, 0xFFFFF830, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6B0E)
    Sleep(400)

    def lambda_6B2E():
        OP_90(0x102, 0x0, 0x0, 0xFFFFF768, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6B2E)
    Sleep(400)

    def lambda_6B4E():
        OP_90(0x103, 0x0, 0x0, 0xFFFFF8F8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6B4E)
    OP_0D()
    WaitChrThread(0x101, 0x1)
    TurnDirection(0x101, 0xC, 400)
    WaitChrThread(0xC, 0x1)
    OP_62(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xC, 0x101, 400)
    OP_4A(0xC, 255)

    ChrTalk(
        0xC,
        "啊……是你们！？\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x103, 0x1)
    TurnDirection(0x103, 0xC, 400)
    WaitChrThread(0x102, 0x1)
    TurnDirection(0x102, 0xC, 400)

    ChrTalk(
        0xC,
        (
            "刚、刚才那场地震……\x01",
            "难道是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "魔兽果真出现了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#502F嘿嘿⊙\x01",
            "已经被我们干掉了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0xC,
        "真、真的吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F嗯，已经把它消灭了。\x02\x03",
            "虽然是个很难缠的家伙。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x103, 400)

    ChrTalk(
        0xC,
        (
            "呼，太好了。\x01",
            "真是个振奋人心的好消息。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "这样一来，\x01",
            "就不用担心魔兽\x01",
            "会在农忙期间来袭击了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "我现在就去把\x01",
            "这个好消息告诉村长。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 400)

    ChrTalk(
        0xC,
        "你们真是帮了大忙啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "虽然没什么可招待各位的，\x01",
            "还是请你们在这里好好休息。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F嗯，谢谢⊙\x02",
    )

    CloseMessageWindow()
    OP_8E(0xC, 0xE88, 0x1F40, 0xFBD6, 0xBB8, 0x0)
    OP_8E(0xC, 0xFFFFF827, 0x1770, 0xF8DE, 0xBB8, 0x0)

    def lambda_6E78():
        OP_92(0x102, 0x101, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6E78)
    OP_92(0x103, 0x101, 0x0, 0xBB8, 0x0)
    SetChrFlags(0xC, 0x80)
    ClearMapFlags(0x400000)
    EventEnd(0x0)
    Return()

    # Function_23_6A82 end

    def Function_24_6EA2(): pass

    label("Function_24_6EA2")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "七耀历１１９２年\x01",
            "在战火中丧生的\x01",
            "六个善良的灵魂，在此长眠。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "雷夫、阿贝尔、尼高尔\x01",
            "维姆、依蕾娜、米夏。\x01",
            "在女神的座前，安息吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_24_6EA2 end

    def Function_25_6FAC(): pass

    label("Function_25_6FAC")

    SetPlaceName(0x2E) # 拉文努村　村长家
    Return()

    # Function_25_6FAC end

    def Function_26_6FB0(): pass

    label("Function_26_6FB0")

    SetPlaceName(0x2D) # 拉文努村　村长家
    Return()

    # Function_26_6FB0 end

    def Function_27_6FB4(): pass

    label("Function_27_6FB4")

    SetPlaceName(0x2F) # 拉文努村　村长家
    Return()

    # Function_27_6FB4 end

    SaveToFile()

Try(main)
