from ED6ScenarioHelper import *

def main():
    # 蔡斯

    CreateScenaFile(
        FileName            = 'R3100   ._SN',
        MapName             = 'Zeiss',
        Location            = 'R3100.x',
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
        '东方打扮的男人',                       # 9
        '蔡斯方向',                             # 10
        '亚尔摩村方向',                         # 11
        '沃尔费堡垒方向',                       # 12
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
        'ED6_DT07/CH00070 ._CH',             # 00
        'ED6_DT07/CH00054 ._CH',             # 01
        'ED6_DT07/CH00015 ._CH',             # 02
        'ED6_DT09/CH10610 ._CH',             # 03
        'ED6_DT09/CH10611 ._CH',             # 04
        'ED6_DT09/CH10080 ._CH',             # 05
        'ED6_DT09/CH10081 ._CH',             # 06
        'ED6_DT09/CH10120 ._CH',             # 07
        'ED6_DT09/CH10121 ._CH',             # 08
        'ED6_DT09/CH10140 ._CH',             # 09
        'ED6_DT09/CH10141 ._CH',             # 0A
        'ED6_DT09/CH10620 ._CH',             # 0B
        'ED6_DT09/CH10621 ._CH',             # 0C
        'ED6_DT09/CH10600 ._CH',             # 0D
        'ED6_DT09/CH10601 ._CH',             # 0E
        'ED6_DT09/CH10400 ._CH',             # 0F
        'ED6_DT09/CH10401 ._CH',             # 10
        'ED6_DT06/CH20139 ._CH',             # 11
    )

    AddCharChipPat(
        'ED6_DT07/CH00070P._CP',             # 00
        'ED6_DT07/CH00054P._CP',             # 01
        'ED6_DT07/CH00015P._CP',             # 02
        'ED6_DT09/CH10610P._CP',             # 03
        'ED6_DT09/CH10611P._CP',             # 04
        'ED6_DT09/CH10080P._CP',             # 05
        'ED6_DT09/CH10081P._CP',             # 06
        'ED6_DT09/CH10120P._CP',             # 07
        'ED6_DT09/CH10121P._CP',             # 08
        'ED6_DT09/CH10140P._CP',             # 09
        'ED6_DT09/CH10141P._CP',             # 0A
        'ED6_DT09/CH10620P._CP',             # 0B
        'ED6_DT09/CH10621P._CP',             # 0C
        'ED6_DT09/CH10600P._CP',             # 0D
        'ED6_DT09/CH10601P._CP',             # 0E
        'ED6_DT09/CH10400P._CP',             # 0F
        'ED6_DT09/CH10401P._CP',             # 10
        'ED6_DT06/CH20139P._CP',             # 11
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
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -26180,
        Z                   = 0,
        Y                   = 75950,
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
        X                   = -27440,
        Z                   = 0,
        Y                   = -76050,
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
        X                   = 57120,
        Z                   = 20,
        Y                   = -11610,
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


    DeclMonster(
        X                   = -31930,
        Z                   = -10,
        Y                   = 25570,
        Unknown_0C          = 180,
        Unknown_0E          = 9,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -17900,
        Z                   = -100,
        Y                   = 29570,
        Unknown_0C          = 180,
        Unknown_0E          = 9,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -17830,
        Z                   = -50,
        Y                   = 10270,
        Unknown_0C          = 180,
        Unknown_0E          = 9,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -33160,
        Z                   = 80,
        Y                   = 9720,
        Unknown_0C          = 180,
        Unknown_0E          = 9,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -33640,
        Z                   = -20,
        Y                   = -11610,
        Unknown_0C          = 180,
        Unknown_0E          = 9,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -34150,
        Z                   = 10,
        Y                   = -34210,
        Unknown_0C          = 180,
        Unknown_0E          = 9,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -17610,
        Z                   = 60,
        Y                   = -32390,
        Unknown_0C          = 180,
        Unknown_0E          = 9,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 13750,
        Z                   = 20,
        Y                   = 4540,
        Unknown_0C          = 180,
        Unknown_0E          = 9,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 28640,
        Z                   = -50,
        Y                   = -14990,
        Unknown_0C          = 180,
        Unknown_0E          = 9,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 39490,
        Z                   = -40,
        Y                   = 9070,
        Unknown_0C          = 180,
        Unknown_0E          = 9,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 18010,
        Z                   = 0,
        Y                   = 13240,
        Unknown_0C          = 180,
        Unknown_0E          = 9,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 19410,
        Z                   = -90,
        Y                   = 27970,
        Unknown_0C          = 180,
        Unknown_0E          = 9,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 20370,
        Z                   = 10,
        Y                   = 8119,
        Unknown_0C          = 180,
        Unknown_0E          = 9,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 21540,
        Z                   = 50,
        Y                   = 3820,
        Unknown_0C          = 180,
        Unknown_0E          = 9,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -43300,
        Z                   = 80,
        Y                   = -22610,
        Unknown_0C          = 180,
        Unknown_0E          = 11,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20A,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -25500,
        Z                   = 20,
        Y                   = 17440,
        Unknown_0C          = 180,
        Unknown_0E          = 7,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 7640,
        Z                   = 0,
        Y                   = 5540,
        Unknown_0C          = 180,
        Unknown_0E          = 13,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -31930,
        Z                   = -10,
        Y                   = 25570,
        Unknown_0C          = 180,
        Unknown_0E          = 9,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -17900,
        Z                   = -100,
        Y                   = 29570,
        Unknown_0C          = 180,
        Unknown_0E          = 9,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -17830,
        Z                   = -50,
        Y                   = 10270,
        Unknown_0C          = 180,
        Unknown_0E          = 9,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -33160,
        Z                   = 80,
        Y                   = 9720,
        Unknown_0C          = 180,
        Unknown_0E          = 9,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -33640,
        Z                   = -20,
        Y                   = -11610,
        Unknown_0C          = 180,
        Unknown_0E          = 9,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -34150,
        Z                   = 10,
        Y                   = -34210,
        Unknown_0C          = 180,
        Unknown_0E          = 9,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -17610,
        Z                   = 60,
        Y                   = -32390,
        Unknown_0C          = 180,
        Unknown_0E          = 9,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 13750,
        Z                   = 20,
        Y                   = 4540,
        Unknown_0C          = 180,
        Unknown_0E          = 9,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 28640,
        Z                   = -50,
        Y                   = -14990,
        Unknown_0C          = 180,
        Unknown_0E          = 9,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 39490,
        Z                   = -40,
        Y                   = 9070,
        Unknown_0C          = 180,
        Unknown_0E          = 9,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 18010,
        Z                   = 0,
        Y                   = 13240,
        Unknown_0C          = 180,
        Unknown_0E          = 9,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 19410,
        Z                   = -90,
        Y                   = 27970,
        Unknown_0C          = 180,
        Unknown_0E          = 9,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 20370,
        Z                   = 10,
        Y                   = 8119,
        Unknown_0C          = 180,
        Unknown_0E          = 9,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 21540,
        Z                   = 50,
        Y                   = 3820,
        Unknown_0C          = 180,
        Unknown_0E          = 9,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -43300,
        Z                   = 80,
        Y                   = -22610,
        Unknown_0C          = 180,
        Unknown_0E          = 11,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34A,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -25500,
        Z                   = 20,
        Y                   = 17440,
        Unknown_0C          = 180,
        Unknown_0E          = 7,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 7640,
        Z                   = 0,
        Y                   = 5540,
        Unknown_0C          = 180,
        Unknown_0E          = 13,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -10960,
        Y                   = -1000,
        Z                   = -260,
        Range               = -9090,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0xFFFFD7CE,
        Unknown_18          = 0x0,
        Unknown_1C          = 3,
    )


    DeclActor(
        TriggerX            = -31610,
        TriggerZ            = 0,
        TriggerY            = 41470,
        TriggerRange        = 1500,
        ActorX              = -31610,
        ActorZ              = 1500,
        ActorY              = 41470,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -15330,
        TriggerZ            = 0,
        TriggerY            = -13840,
        TriggerRange        = 1500,
        ActorX              = -15330,
        ActorZ              = 1350,
        ActorY              = -13840,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -12250,
        TriggerZ            = 0,
        TriggerY            = -9350,
        TriggerRange        = 1500,
        ActorX              = -12250,
        ActorZ              = 1400,
        ActorY              = -9350,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 3410,
        TriggerZ            = -20,
        TriggerY            = -11850,
        TriggerRange        = 1000,
        ActorX              = 3410,
        ActorZ              = 1480,
        ActorY              = -12510,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -29130,
        TriggerZ            = 90,
        TriggerY            = -8189,
        TriggerRange        = 1000,
        ActorX              = -28780,
        ActorZ              = 1590,
        ActorY              = -8610,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_646",          # 00, 0
        "Function_1_647",          # 01, 1
        "Function_2_77B",          # 02, 2
        "Function_3_971",          # 03, 3
        "Function_4_1409",         # 04, 4
        "Function_5_149A",         # 05, 5
        "Function_6_14F5",         # 06, 6
        "Function_7_155D",         # 07, 7
        "Function_8_169E",         # 08, 8
    )


    def Function_0_646(): pass

    label("Function_0_646")

    Return()

    # Function_0_646 end

    def Function_1_647(): pass

    label("Function_1_647")

    OP_16(0x2, 0xFA0, 0xFFFE0048, 0xFFFE13D0, 0x3002D)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_671")
    OP_B1("R3100_y")
    Jump("loc_67A")

    label("loc_671")

    OP_B1("R3100_n")

    label("loc_67A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6DE")
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
    SetChrFlags(0x1C, 0x80)
    Jump("loc_733")

    label("loc_6DE")

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
    SetChrFlags(0x2D, 0x80)

    label("loc_733")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x346)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x29, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_748")
    OP_1B(0x1, 0x0, 0x2)

    label("loc_748")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_75A")
    OP_6F(0x0, 0)
    Jump("loc_761")

    label("loc_75A")

    OP_6F(0x0, 60)

    label("loc_761")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_773")
    OP_6F(0x1, 0)
    Jump("loc_77A")

    label("loc_773")

    OP_6F(0x1, 60)

    label("loc_77A")

    Return()

    # Function_1_647 end

    def Function_2_77B(): pass

    label("Function_2_77B")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_83F")
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F艾丝蒂尔，\x01",
            "先去把导力引擎送过去吧。\x02\x03",
            "王先生他们肯定还在等着呢。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#000F啊，对了。\x01",
            "是从这里往西走吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_955")

    label("loc_83F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8CD")

    ChrTalk(
        0x102,
        (
            "#010F往这边走就到亚尔摩村了……\x02\x03",
            "先去西边的平原\x01",
            "把导力引擎送到王先生他们手里吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_955")

    label("loc_8CD")


    ChrTalk(
        0x107,
        (
            "#060F（要先把导力引擎送过去才行……）\x01",
            "　\x02\x03",
            "#060F（运输车抛锚的地方\x01",
            "　从这里往西走就到了。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_955")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_2_77B end

    def Function_3_971(): pass

    label("Function_3_971")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1408")
    EventBegin(0x0)
    OP_A2(0x550)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -22660, 0, -12250, 45)

    NpcTalk(
        0x8,
        "男性的声音",
        (
            "哟？\x01",
            "你们几个是……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(-14850, -10, -5530, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3250, 0)
    OP_6C(215000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -12590, -10, -5620, 270)
    SetChrPos(0x107, -11250, 0, -6040, 270)
    SetChrPos(0x102, -11730, 0, -3960, 270)
    SetChrPos(0x106, -10690, 0, -4680, 270)

    def lambda_A54():

        label("loc_A54")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_A54")

    QueueWorkItem2(0x101, 3, lambda_A54)

    def lambda_A65():

        label("loc_A65")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_A65")

    QueueWorkItem2(0x102, 3, lambda_A65)

    def lambda_A76():

        label("loc_A76")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_A76")

    QueueWorkItem2(0x107, 3, lambda_A76)

    def lambda_A87():

        label("loc_A87")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_A87")

    QueueWorkItem2(0x106, 3, lambda_A87)

    def lambda_A98():
        OP_8E(0xFE, 0xFFFFC086, 0x0, 0xFFFFEA98, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_A98)
    OP_0D()
    WaitChrThread(0x8, 0x1)
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0x101,
        "#004F咦……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#064F从亚尔摩回来时遇到的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#071F哈哈，\x01",
            "那时真是谢谢你们指路啦。\x02\x03",
            "不过还能在街道遇到你们，\x01",
            "我们还真是有缘啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F啊哈，是啊。\x02\x03",
            "#501F这么说来，\x01",
            "大叔也是去亚尔摩村泡温泉的吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#075F话是没错……\x01",
            "不过别叫我大叔啦。\x02\x03",
            "#073F对了，\x01",
            "这位小哥之前好像没见过。\x02\x03",
            "你脸色不太好啊，不要紧吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F咦……\x02",
    )

    CloseMessageWindow()
    OP_20(0x7D0)

    def lambda_CE0():
        OP_6D(-12080, 0, -4480, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_CE0)
    OP_44(0x101, 0x3)
    OP_44(0x102, 0x3)
    OP_44(0x107, 0x3)
    OP_44(0x106, 0x3)

    def lambda_D08():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_D08)

    def lambda_D16():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_D16)

    def lambda_D24():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x107, 3, lambda_D24)
    TurnDirection(0x101, 0x106, 400)
    WaitChrThread(0x101, 0x2)

    ChrTalk(
        0x106,
        "#058F………………………………\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_1D(0x51)

    ChrTalk(
        0x101,
        "#2P#580F唔哇……脸色怎么会这样！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#065F阿、阿加特大哥哥……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#058F吵死了……\x01",
            "不是说了没事吗……\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0x106, 0x1E, 0x0, 0x258, 0xBB8)
    Fade(500)

    def lambda_E04():
        OP_6B(2900, 500)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_E04)
    SetChrChipByIndex(0x106, 1)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x106,
        "#059F……呜………………\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_22(0x20C, 0x0, 0x64)

    def lambda_E3A():
        OP_6B(2900, 500)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_E3A)
    SetChrFlags(0x106, 0x2)
    SetChrChipByIndex(0x106, 17)
    SetChrSubChip(0x106, 0)
    SetChrPos(0x106, -10570, 0, -4920, 91)
    OP_8C(0x107, 0, 0)
    OP_8C(0x101, 45, 0)
    OP_8C(0x102, 180, 0)
    OP_0D()
    Sleep(500)
    OP_62(0x107, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(
        0x107,
        "#069F呀……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#580F#2P怎、怎么回事！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#016F……等一下！\x02",
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x102, 2)
    OP_0D()

    def lambda_EF2():
        OP_8E(0xFE, 0xFFFFCC8E, 0x0, 0xFFFFEE76, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_EF2)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "约修亚用手拨开了阿加特的眼皮。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_62(0x102, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x102)

    ChrTalk(
        0x102,
        (
            "#013F糟了……\x01",
            "瞳孔怎么张得这么开。\x02\x03",
            "那些黑衣人的导力弹里\x01",
            "一定放了些什么……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#580F#2P什、什么……难道是毒！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#072F唔，应该没错。\x02\x03",
            "出现瞳孔张开的症状，\x01",
            "也许是中了植物性的神经毒药。\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x102, 65535)
    OP_0D()
    TurnDirection(0x102, 0x8, 400)

    ChrTalk(
        0x102,
        (
            "#012F我也认为很有可能。\x02\x03",
            "虽然还不能肯定……\x01",
            "但这样下去阿加特兄也许有生命危险。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#069F怎、怎么会……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#005F#2P总、总之要赶快\x01",
            "把他送到有治疗设施的地方！\x02\x03",
            "提妲，\x01",
            "这附近有能帮他治疗的地方吗！？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(
        0x107,
        (
            "#068F中、中央工房……！\x02\x03",
            "四楼有医务室！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#072F事不宜迟……\x01",
            "那就麻烦小姑娘带路了。\x02\x03",
            "我来背这个小哥好了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1249():
        OP_69(0x8, 0x320)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1249)

    def lambda_1257():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_1257)

    def lambda_1265():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x107, 3, lambda_1265)
    TurnDirection(0x101, 0x8, 400)
    WaitChrThread(0x101, 0x2)

    ChrTalk(
        0x101,
        "#505F哎……可以吗！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#070F#2P你看他这结实的块头。\x01",
            "反正苦力的活儿就交给我吧。\x02\x03",
            "而且……\x01",
            "看来我们还是同行呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F同行……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F难道说，您也是……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#074F#2P还没自我介绍呢。\x02\x03",
            "#070F金·瓦赛克——\x01",
            "隶属于共和国的游击士协会。\x02\x03",
            "#070F请多指教。\x01",
            "各位王国的游击士。\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    FadeToDark(1500, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T3118   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1408")

    Return()

    # Function_3_971 end

    def Function_4_1409(): pass

    label("Function_4_1409")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "北　蔡斯市\x01",
            "南　亚尔摩村　　１６５塞尔矩\x01",
            "　　沃尔费堡垒　２８０塞尔矩\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_4_1409 end

    def Function_5_149A(): pass

    label("Function_5_149A")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "南　亚尔摩村　　１３０塞尔矩\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_5_149A end

    def Function_6_14F5(): pass

    label("Function_6_14F5")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "北　蔡斯市\x01",
            "东　沃尔费堡垒　２４５塞尔矩\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_6_14F5 end

    def Function_7_155D(): pass

    label("Function_7_155D")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_164F")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_15D4")
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
    OP_A2(0x599)
    Jump("loc_164C")

    label("loc_15D4")

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
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_164C")

    Jump("loc_1690")

    label("loc_164F")

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
    OP_83(0xF, 0x8D)

    label("loc_1690")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_155D end

    def Function_8_169E(): pass

    label("Function_8_169E")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1790")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_1715")
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
    OP_A2(0x59A)
    Jump("loc_178D")

    label("loc_1715")

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
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_178D")

    Jump("loc_17D7")

    label("loc_1790")

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
    OP_83(0xF, 0x8E)

    label("loc_17D7")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_169E end

    SaveToFile()

Try(main)
