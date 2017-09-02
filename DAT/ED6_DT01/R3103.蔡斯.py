from ED6ScenarioHelper import *

def main():
    # 蔡斯

    CreateScenaFile(
        FileName            = 'R3103   ._SN',
        MapName             = 'Zeiss',
        Location            = 'R3103.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60020",
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
        '蔡斯方向',                             # 9
        '沃尔费堡垒方向',                       # 10
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
        Unknown_3A              = 144,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT09/CH10610 ._CH',             # 00
        'ED6_DT09/CH10611 ._CH',             # 01
        'ED6_DT09/CH10080 ._CH',             # 02
        'ED6_DT09/CH10081 ._CH',             # 03
        'ED6_DT09/CH10120 ._CH',             # 04
        'ED6_DT09/CH10121 ._CH',             # 05
        'ED6_DT09/CH10140 ._CH',             # 06
        'ED6_DT09/CH10141 ._CH',             # 07
        'ED6_DT09/CH10620 ._CH',             # 08
        'ED6_DT09/CH10621 ._CH',             # 09
        'ED6_DT09/CH10600 ._CH',             # 0A
        'ED6_DT09/CH10601 ._CH',             # 0B
        'ED6_DT09/CH10400 ._CH',             # 0C
        'ED6_DT09/CH10401 ._CH',             # 0D
    )

    AddCharChipPat(
        'ED6_DT09/CH10610P._CP',             # 00
        'ED6_DT09/CH10611P._CP',             # 01
        'ED6_DT09/CH10080P._CP',             # 02
        'ED6_DT09/CH10081P._CP',             # 03
        'ED6_DT09/CH10120P._CP',             # 04
        'ED6_DT09/CH10121P._CP',             # 05
        'ED6_DT09/CH10140P._CP',             # 06
        'ED6_DT09/CH10141P._CP',             # 07
        'ED6_DT09/CH10620P._CP',             # 08
        'ED6_DT09/CH10621P._CP',             # 09
        'ED6_DT09/CH10600P._CP',             # 0A
        'ED6_DT09/CH10601P._CP',             # 0B
        'ED6_DT09/CH10400P._CP',             # 0C
        'ED6_DT09/CH10401P._CP',             # 0D
    )

    DeclNpc(
        X                   = -53110,
        Z                   = 0,
        Y                   = -14880,
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
        X                   = 22050,
        Z                   = -10,
        Y                   = 35970,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -30730,
        Z                   = -20,
        Y                   = 28880,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -27870,
        Z                   = 80,
        Y                   = 46700,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -14660,
        Z                   = -80,
        Y                   = 32810,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -24060,
        Z                   = 70,
        Y                   = -7910,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -10150,
        Z                   = 10,
        Y                   = -20920,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 13270,
        Z                   = -30,
        Y                   = -23320,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20A,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 15990,
        Z                   = -10,
        Y                   = 1090,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 31250,
        Z                   = 30,
        Y                   = -6140,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 39280,
        Z                   = 20,
        Y                   = -27110,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 23510,
        Z                   = 40,
        Y                   = -36040,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x21B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 10940,
        Z                   = 10,
        Y                   = -46410,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x21B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -10090,
        Z                   = 10,
        Y                   = -39590,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -25680,
        Z                   = -40,
        Y                   = -25220,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20A,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -29830,
        Z                   = -90,
        Y                   = -39580,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -30430,
        Z                   = -80,
        Y                   = -45390,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -21410,
        Z                   = -50,
        Y                   = -50290,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -22480,
        Z                   = 30,
        Y                   = -37550,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -30730,
        Z                   = -20,
        Y                   = 28880,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -27870,
        Z                   = 80,
        Y                   = 46700,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -14660,
        Z                   = -80,
        Y                   = 32810,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -24060,
        Z                   = 70,
        Y                   = -7910,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -10150,
        Z                   = 10,
        Y                   = -20920,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 13270,
        Z                   = -30,
        Y                   = -23320,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34A,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 15990,
        Z                   = -10,
        Y                   = 1090,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 31250,
        Z                   = 30,
        Y                   = -6140,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 39280,
        Z                   = 20,
        Y                   = -27110,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 23510,
        Z                   = 40,
        Y                   = -36040,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x35B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 10940,
        Z                   = 10,
        Y                   = -46410,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x35B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -10090,
        Z                   = 10,
        Y                   = -39590,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -25680,
        Z                   = -40,
        Y                   = -25220,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34A,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -29830,
        Z                   = -90,
        Y                   = -39580,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -30430,
        Z                   = -80,
        Y                   = -45390,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -21410,
        Z                   = -50,
        Y                   = -50290,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -22480,
        Z                   = 30,
        Y                   = -37550,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -17270,
        TriggerZ            = 0,
        TriggerY            = 42460,
        TriggerRange        = 1400,
        ActorX              = -17270,
        ActorZ              = 0,
        ActorY              = 42460,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 17230,
        TriggerZ            = 10,
        TriggerY            = -7630,
        TriggerRange        = 1000,
        ActorX              = 17890,
        ActorZ              = 10,
        ActorY              = -7630,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -12960,
        TriggerZ            = -20,
        TriggerY            = 45920,
        TriggerRange        = 1000,
        ActorX              = -12550,
        ActorZ              = -20,
        ActorY              = 46450,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -24020,
        TriggerZ            = -10,
        TriggerY            = -43750,
        TriggerRange        = 1000,
        ActorX              = -24580,
        ActorZ              = -10,
        ActorY              = -43380,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_5C2",          # 00, 0
        "Function_1_5C3",          # 01, 1
        "Function_2_734",          # 02, 2
        "Function_3_74A",          # 03, 3
        "Function_4_7E2",          # 04, 4
        "Function_5_A19",          # 05, 5
        "Function_6_C36",          # 06, 6
    )


    def Function_0_5C2(): pass

    label("Function_0_5C2")

    Return()

    # Function_0_5C2 end

    def Function_1_5C3(): pass

    label("Function_1_5C3")

    OP_16(0x2, 0xFA0, 0xFFFE0048, 0xFFFE13D0, 0x30030)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5ED")
    OP_B1("R3103_y")
    Jump("loc_5F6")

    label("loc_5ED")

    OP_B1("R3103_n")

    label("loc_5F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_65A")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    Jump("loc_6AF")

    label("loc_65A")

    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x20, 0x80)
    SetChrFlags(0x21, 0x80)
    SetChrFlags(0x22, 0x80)
    SetChrFlags(0x23, 0x80)
    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x25, 0x80)
    SetChrFlags(0x26, 0x80)
    SetChrFlags(0x27, 0x80)
    SetChrFlags(0x28, 0x80)
    SetChrFlags(0x29, 0x80)
    SetChrFlags(0x2A, 0x80)
    SetChrFlags(0x2B, 0x80)
    SetChrFlags(0x2C, 0x80)

    label("loc_6AF")

    OP_64(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x2F, 0x0, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x2F, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6CF")
    OP_65(0x0, 0x1)

    label("loc_6CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E1")
    OP_6F(0x0, 0)
    Jump("loc_6E8")

    label("loc_6E1")

    OP_6F(0x0, 60)

    label("loc_6E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB4, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6FA")
    OP_6F(0x1, 0)
    Jump("loc_701")

    label("loc_6FA")

    OP_6F(0x1, 60)

    label("loc_701")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_713")
    OP_6F(0x2, 0)
    Jump("loc_71A")

    label("loc_713")

    OP_6F(0x2, 60)

    label("loc_71A")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_726"),
        (SWITCH_DEFAULT, "loc_733"),
    )


    label("loc_726")

    ClearChrFlags(0x8, 0x1)
    ClearChrFlags(0x9, 0x1)
    Jump("loc_733")

    label("loc_733")

    Return()

    # Function_1_5C3 end

    def Function_2_734(): pass

    label("Function_2_734")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_749")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_734")

    label("loc_749")

    Return()

    # Function_2_734 end

    def Function_3_74A(): pass

    label("Function_3_74A")

    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "发现了一个油纸包。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "里面放着\x07\x02",
            "哈茨少年冒险记·下\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x344, 1)
    OP_64(0x0, 0x1)
    OP_28(0x2F, 0x1, 0x8)
    TalkEnd(0xFF)
    Return()

    # Function_3_74A end

    def Function_4_7E2(): pass

    label("Function_4_7E2")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9C5")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB4, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8E0")
    OP_9F(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xA, -12550, 1500, 46450, 320)
    TurnDirection(0xA, 0x0, 0)

    def lambda_831():
        OP_8F(0xFE, 0xFFFFCEFA, 0x3E8, 0xB572, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_831)

    def lambda_84C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x4B0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_84C)
    ClearChrFlags(0xA, 0x80)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "魔兽出现了！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_895")
    Battle(0x357, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_8A2")

    label("loc_895")

    Battle(0x217, 0x0, 0x0, 0x0, 0xFF)

    label("loc_8A2")

    SetChrFlags(0xA, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_8BB"),
        (2, "loc_8CD"),
        (1, "loc_8DD"),
        (SWITCH_DEFAULT, "loc_8E0"),
    )


    label("loc_8BB")

    OP_A2(0x5A3)
    OP_6F(0x0, 60)
    Sleep(500)
    Jump("loc_8E0")

    label("loc_8CD")

    OP_6F(0x0, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_8DD")

    OP_B4(0x0)
    Return()

    label("loc_8E0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x142, 1)"), scpexpr(EXPR_END)), "loc_93E")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "苍耀石护符\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x5A2)
    Jump("loc_9C2")

    label("loc_93E")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "苍耀石护符\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "苍耀石护符\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_9C2")

    Jump("loc_A0B")

    label("loc_9C5")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱里什么东西都没有。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_83(0xF, 0x93)

    label("loc_A0B")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_7E2 end

    def Function_5_A19(): pass

    label("Function_5_A19")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB4, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BEA")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB4, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B17")
    OP_9F(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xA, -24580, 1500, -43380, 320)
    TurnDirection(0xA, 0x0, 0)

    def lambda_A68():
        OP_8F(0xFE, 0xFFFF9FFC, 0x3E8, 0xFFFF568C, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_A68)

    def lambda_A83():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x4B0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_A83)
    ClearChrFlags(0xA, 0x80)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "魔兽出现了！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_ACC")
    Battle(0x357, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_AD9")

    label("loc_ACC")

    Battle(0x217, 0x0, 0x0, 0x0, 0xFF)

    label("loc_AD9")

    SetChrFlags(0xA, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_AF2"),
        (2, "loc_B04"),
        (1, "loc_B14"),
        (SWITCH_DEFAULT, "loc_B17"),
    )


    label("loc_AF2")

    OP_A2(0x5A5)
    OP_6F(0x1, 60)
    Sleep(500)
    Jump("loc_B17")

    label("loc_B04")

    OP_6F(0x1, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_B14")

    OP_B4(0x0)
    Return()

    label("loc_B17")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x14F, 1)"), scpexpr(EXPR_END)), "loc_B6F")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "长桶\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x5A4)
    Jump("loc_BE7")

    label("loc_B6F")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "长桶\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "长桶\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_BE7")

    Jump("loc_C28")

    label("loc_BEA")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱里什么东西都没有。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_83(0xF, 0x94)

    label("loc_C28")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_A19 end

    def Function_6_C36(): pass

    label("Function_6_C36")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D28")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_CAD")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "大回复药\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x5A1)
    Jump("loc_D25")

    label("loc_CAD")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "大回复药\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "大回复药\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_D25")

    Jump("loc_D69")

    label("loc_D28")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱里什么东西都没有。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_83(0xF, 0x95)

    label("loc_D69")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_C36 end

    SaveToFile()

Try(main)
