from ED6ScenarioHelper import *

def main():
    # 巴伦诺灯塔

    CreateScenaFile(
        FileName            = 'C2219   ._SN',
        MapName             = 'Ruan',
        Location            = 'C2219.x',
        MapIndex            = 84,
        MapDefaultBGM       = "ed60015",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/C2219   ._SN',
            'ED6_DT01/C2219_1 ._SN',
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
        '弗科特老人',                           # 9
        '照相机',                               # 10
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
        Unknown_3A              = 84,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH01000 ._CH',             # 00
        'ED6_DT09/CH11200 ._CH',             # 01
        'ED6_DT09/CH11201 ._CH',             # 02
    )

    AddCharChipPat(
        'ED6_DT07/CH01000P._CP',             # 00
        'ED6_DT09/CH11200P._CP',             # 01
        'ED6_DT09/CH11201P._CP',             # 02
    )

    DeclNpc(
        X                   = -2140,
        Z                   = 0,
        Y                   = 201500,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 0,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -250,
        Z                   = 0,
        Y                   = -890,
        Unknown_0C          = 180,
        Unknown_0E          = 1,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F2,
        Unknown_18          = 1184,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 99940,
        Z                   = 0,
        Y                   = 20,
        Unknown_0C          = 270,
        Unknown_0E          = 1,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F2,
        Unknown_18          = 1185,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 1790,
        Z                   = 0,
        Y                   = 102020,
        Unknown_0C          = 90,
        Unknown_0E          = 1,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F2,
        Unknown_18          = 1187,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -1430,
        Z                   = 0,
        Y                   = 95940,
        Unknown_0C          = 0,
        Unknown_0E          = 1,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F2,
        Unknown_18          = 1188,
        Unknown_1A          = 0,
    )


    ScpFunction(
        "Function_0_172",          # 00, 0
        "Function_1_1F9",          # 01, 1
        "Function_2_2B6",          # 02, 2
        "Function_3_2CC",          # 03, 3
    )


    def Function_0_172(): pass

    label("Function_0_172")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1C, 0x0, 0x40)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x1C, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_19A")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    Jump("loc_1CF")

    label("loc_19A")

    SetChrFlags(0x8, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x94, 0)), scpexpr(EXPR_END)), "loc_1AB")
    SetChrFlags(0xA, 0x80)

    label("loc_1AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x94, 1)), scpexpr(EXPR_END)), "loc_1B7")
    SetChrFlags(0xB, 0x80)

    label("loc_1B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x94, 3)), scpexpr(EXPR_END)), "loc_1C3")
    SetChrFlags(0xC, 0x80)

    label("loc_1C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x94, 4)), scpexpr(EXPR_END)), "loc_1CF")
    SetChrFlags(0xD, 0x80)

    label("loc_1CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_1DD")
    OP_A3(0x3FB)
    Event(1, 1)

    label("loc_1DD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1F8")
    SetChrPos(0x8, 3340, 1000, 193310, 178)

    label("loc_1F8")

    Return()

    # Function_0_172 end

    def Function_1_1F9(): pass

    label("Function_1_1F9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1C, 0x0, 0x40)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x1C, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_20D")
    Jump("loc_216")

    label("loc_20D")

    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_216")

    OP_71(0x1, 0x4)
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_71(0x5, 0x4)
    OP_71(0x6, 0x4)
    OP_71(0x7, 0x4)
    OP_71(0x8, 0x4)
    OP_71(0x9, 0x4)
    OP_71(0xA, 0x4)
    OP_71(0xB, 0x4)
    OP_71(0xC, 0x4)
    OP_71(0xD, 0x4)
    OP_71(0xE, 0x4)
    OP_71(0xF, 0x4)
    OP_B0(0x0, 0x78)
    OP_1C(0x0, 0x0, 0x3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x94, 0)), scpexpr(EXPR_END)), "loc_2B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x94, 1)), scpexpr(EXPR_END)), "loc_2B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x94, 3)), scpexpr(EXPR_END)), "loc_2B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x94, 4)), scpexpr(EXPR_END)), "loc_2B5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1C, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x1, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2B5")
    OP_28(0x1C, 0x1, 0x8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_2B1")
    OP_28(0x1D, 0x1, 0x10)

    label("loc_2B1")

    Event(1, 5)

    label("loc_2B5")

    Return()

    # Function_1_1F9 end

    def Function_2_2B6(): pass

    label("Function_2_2B6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2CB")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_2B6")

    label("loc_2CB")

    Return()

    # Function_2_2B6 end

    def Function_3_2CC(): pass

    label("Function_3_2CC")

    TalkBegin(0xFF)
    TalkEnd(0xFF)
    Return()

    # Function_3_2CC end

    SaveToFile()

Try(main)
