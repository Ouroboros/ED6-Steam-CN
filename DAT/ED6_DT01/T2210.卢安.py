from ED6ScenarioHelper import *

def main():
    # 卢安

    CreateScenaFile(
        FileName            = 'T2210   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2210.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60012",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/T2210   ._SN',
            'ED6_DT01/T2210_1 ._SN',
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
        'Mayor Dalmore',                        # 9
        'Nial',                                 # 10
        'Duke Dunan',                           # 11
        'Butler Phillip',                       # 12
        'Flora',                                # 13
        'Dominique',                            # 14
        'Bronco',                               # 15
        'Fango',                                # 16
        'Steward Gilbert',                      # 17
        'Camera',                               # 18
        'Dario',                                # 19
        'Viego',                                # 20
        'Orbment',                              # 21
        'Orbment',                              # 22
        'Bottle',                               # 23
        'Orbment',                              # 24
        'Orbment',                              # 25
        'Bottle',                               # 26
        'Orbment',                              # 27
    )

    DeclEntryPoint(
        Unknown_00              = 88000,
        Unknown_04              = 0,
        Unknown_08              = 22000,
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
        'ED6_DT07/CH02410 ._CH',             # 00
        'ED6_DT07/CH02470 ._CH',             # 01
        'ED6_DT06/CH20088 ._CH',             # 02
        'ED6_DT07/CH02060 ._CH',             # 03
        'ED6_DT07/CH01350 ._CH',             # 04
        'ED6_DT09/CH11020 ._CH',             # 05
        'ED6_DT09/CH11021 ._CH',             # 06
        'ED6_DT09/CH11022 ._CH',             # 07
        'ED6_DT07/CH00100 ._CH',             # 08
        'ED6_DT07/CH00110 ._CH',             # 09
        'ED6_DT07/CH00140 ._CH',             # 0A
        'ED6_DT07/CH00101 ._CH',             # 0B
        'ED6_DT07/CH00111 ._CH',             # 0C
        'ED6_DT07/CH00141 ._CH',             # 0D
        'ED6_DT07/CH02420 ._CH',             # 0E
        'ED6_DT07/CH02540 ._CH',             # 0F
        'ED6_DT07/CH01560 ._CH',             # 10
        'ED6_DT07/CH01280 ._CH',             # 11
        'ED6_DT06/CH20081 ._CH',             # 12
        'ED6_DT06/CH20082 ._CH',             # 13
        'ED6_DT09/CH11030 ._CH',             # 14
        'ED6_DT09/CH11031 ._CH',             # 15
        'ED6_DT09/CH11032 ._CH',             # 16
        'ED6_DT06/CH20020 ._CH',             # 17
        'ED6_DT06/CH20021 ._CH',             # 18
        'ED6_DT06/CH20034 ._CH',             # 19
    )

    AddCharChipPat(
        'ED6_DT07/CH02410P._CP',             # 00
        'ED6_DT07/CH02470P._CP',             # 01
        'ED6_DT06/CH20088P._CP',             # 02
        'ED6_DT07/CH02060P._CP',             # 03
        'ED6_DT07/CH01350P._CP',             # 04
        'ED6_DT09/CH11020P._CP',             # 05
        'ED6_DT09/CH11021P._CP',             # 06
        'ED6_DT09/CH11022P._CP',             # 07
        'ED6_DT07/CH00100P._CP',             # 08
        'ED6_DT07/CH00110P._CP',             # 09
        'ED6_DT07/CH00140P._CP',             # 0A
        'ED6_DT07/CH00101P._CP',             # 0B
        'ED6_DT07/CH00111P._CP',             # 0C
        'ED6_DT07/CH00141P._CP',             # 0D
        'ED6_DT07/CH02420P._CP',             # 0E
        'ED6_DT07/CH02540P._CP',             # 0F
        'ED6_DT07/CH01560P._CP',             # 10
        'ED6_DT07/CH01280P._CP',             # 11
        'ED6_DT06/CH20081P._CP',             # 12
        'ED6_DT06/CH20082P._CP',             # 13
        'ED6_DT09/CH11030P._CP',             # 14
        'ED6_DT09/CH11031P._CP',             # 15
        'ED6_DT09/CH11032P._CP',             # 16
        'ED6_DT06/CH20020P._CP',             # 17
        'ED6_DT06/CH20021P._CP',             # 18
        'ED6_DT06/CH20034P._CP',             # 19
    )

    DeclNpc(
        X                   = -63850,
        Z                   = 0,
        Y                   = 34900,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 24500,
        Z                   = 0,
        Y                   = 6100,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 24500,
        Z                   = 0,
        Y                   = 6100,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x195,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 24500,
        Z                   = 0,
        Y                   = 6100,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 470,
        Z                   = 0,
        Y                   = -670,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -59600,
        Z                   = 0,
        Y                   = -18600,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 24500,
        Z                   = 0,
        Y                   = 6100,
        Direction           = 270,
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
        X                   = 24500,
        Z                   = 0,
        Y                   = 6100,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 4530,
        Z                   = 0,
        Y                   = 36330,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
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

    DeclNpc(
        X                   = 68100,
        Z                   = 0,
        Y                   = -9000,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 37390,
        Z                   = 0,
        Y                   = 34110,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 20,
        Z                   = 700,
        Y                   = 39430,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 24,
        ChipIndex           = 0x18,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -780,
        Z                   = 700,
        Y                   = 38600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 24,
        ChipIndex           = 0x18,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -150,
        Z                   = 750,
        Y                   = 38740,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1966103,
        ChipIndex           = 0x17,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 20,
        Z                   = 700,
        Y                   = 39430,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 65560,
        ChipIndex           = 0x18,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -780,
        Z                   = 700,
        Y                   = 38600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 65560,
        ChipIndex           = 0x18,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -150,
        Z                   = 750,
        Y                   = 38740,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1966103,
        ChipIndex           = 0x17,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 20,
        Z                   = 700,
        Y                   = 39430,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 917528,
        ChipIndex           = 0x18,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = -475,
        TriggerZ            = 0,
        TriggerY            = 3173,
        TriggerRange        = 800,
        ActorX              = -475,
        ActorZ              = 800,
        ActorY              = 3173,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -63800,
        TriggerZ            = 0,
        TriggerY            = 50790,
        TriggerRange        = 900,
        ActorX              = -63800,
        ActorZ              = -300,
        ActorY              = 50790,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 22,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -62370,
        TriggerZ            = 0,
        TriggerY            = -43110,
        TriggerRange        = 500,
        ActorX              = -62370,
        ActorZ              = 2000,
        ActorY              = -43110,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 23,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -59500,
        TriggerZ            = 250,
        TriggerY            = -36760,
        TriggerRange        = 800,
        ActorX              = -59500,
        ActorZ              = 1250,
        ActorY              = -36760,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 24,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_46A",          # 00, 0
        "Function_1_697",          # 01, 1
        "Function_2_6E8",          # 02, 2
        "Function_3_6FE",          # 03, 3
        "Function_4_744",          # 04, 4
        "Function_5_F08",          # 05, 5
        "Function_6_16CE",         # 06, 6
        "Function_7_2704",         # 07, 7
        "Function_8_2D9B",         # 08, 8
        "Function_9_3219",         # 09, 9
        "Function_10_353D",        # 0A, 10
        "Function_11_3638",        # 0B, 11
        "Function_12_3ED8",        # 0C, 12
        "Function_13_6B07",        # 0D, 13
        "Function_14_7FEB",        # 0E, 14
        "Function_15_8020",        # 0F, 15
        "Function_16_805A",        # 10, 16
        "Function_17_8094",        # 11, 17
        "Function_18_80CC",        # 12, 18
        "Function_19_8167",        # 13, 19
        "Function_20_81DB",        # 14, 20
        "Function_21_8257",        # 15, 21
        "Function_22_8289",        # 16, 22
        "Function_23_8293",        # 17, 23
        "Function_24_829D",        # 18, 24
    )


    def Function_0_46A(): pass

    label("Function_0_46A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4B1")
    SetChrPos(0xC, -700, 0, -710, 90)
    SetChrPos(0xD, 790, 0, -710, 270)
    SetChrPos(0x13, 36970, 0, 27900, 270)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x10, 0x80)
    Jump("loc_612")

    label("loc_4B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_4FD")
    SetChrPos(0xC, 36850, 0, 31730, 0)
    SetChrFlags(0xC, 0x10)
    SetChrPos(0xD, 35800, 0, 34250, 180)
    SetChrPos(0x13, 36970, 0, 27900, 270)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x10, 0x80)
    Jump("loc_612")

    label("loc_4FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_573")
    SetChrPos(0xC, 67550, 0, 28050, 90)
    SetChrPos(0xD, -61450, 0, 2440, 180)
    SetChrPos(0x13, 36970, 0, 27900, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x0, 0x4)"), scpexpr(EXPR_END)), "loc_55A")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 4530, 0, 36330, 90)
    Jump("loc_570")

    label("loc_55A")

    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 0, 0, 1800, 0)

    label("loc_570")

    Jump("loc_612")

    label("loc_573")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_5C1")
    SetChrPos(0xC, 36850, 0, 31730, 0)
    SetChrPos(0xD, 35800, 0, 34250, 180)
    SetChrPos(0x13, 36970, 0, 27900, 270)
    SetChrPos(0x12, -2090, 0, 2630, 180)
    Jump("loc_612")

    label("loc_5C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_5DC")
    SetChrPos(0x13, 36970, 0, 27900, 270)
    Jump("loc_612")

    label("loc_5DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 7)), scpexpr(EXPR_END)), "loc_5F7")
    SetChrPos(0xC, 33500, 0, 24550, 270)
    Jump("loc_612")

    label("loc_5F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 4)), scpexpr(EXPR_END)), "loc_612")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8)

    label("loc_612")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_622"),
        (114, "loc_669"),
        (SWITCH_DEFAULT, "loc_67F"),
    )


    label("loc_622")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x88, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_638")
    OP_A2(0x440)
    Event(0, 11)
    Jump("loc_666")

    label("loc_638")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x1, 0x200)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_666")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x8, 0x80)
    OP_28(0x20, 0x4, 0x10)
    Event(1, 4)

    label("loc_666")

    Jump("loc_67F")

    label("loc_669")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x88, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x88, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_67C")
    OP_A2(0x441)
    Event(0, 12)

    label("loc_67C")

    Jump("loc_67F")

    label("loc_67F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_696")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x51), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3FB)
    Event(0, 13)

    label("loc_696")

    Return()

    # Function_0_46A end

    def Function_1_697(): pass

    label("Function_1_697")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x88, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x1, 0x200)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6D4")
    OP_71(0x7, 0x4)
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_71(0x5, 0x4)
    OP_71(0x6, 0x4)

    label("loc_6D4")

    OP_72(0x10, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_6E7")
    OP_6F(0x10, 300)

    label("loc_6E7")

    Return()

    # Function_1_697 end

    def Function_2_6E8(): pass

    label("Function_2_6E8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6FD")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_6E8")

    label("loc_6FD")

    Return()

    # Function_2_6E8 end

    def Function_3_6FE(): pass

    label("Function_3_6FE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x0, 0x4)"), scpexpr(EXPR_END)), "loc_72E")

    label("loc_708")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_72B")
    OP_8D(0xFE, 3420, 32950, 6190, 40410, 1500)
    Jump("loc_708")

    label("loc_72B")

    Jump("loc_743")

    label("loc_72E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_743")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_72E")

    label("loc_743")

    Return()

    # Function_3_6FE end

    def Function_4_744(): pass

    label("Function_4_744")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_B32")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_86A")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "#660FLadies and gentleman, your efforts\x01",
            "are most appreciated.\x02\x03",
            "By all rights, I really should thank\x01",
            "you more properly, but I have a great\x01",
            "deal of work that needs my attention.\x02\x03",
            "Unfortunately, the circumstances\x01",
            "do not permit me to spend any\x01",
            "time with you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8D2")

    label("loc_86A")


    ChrTalk(
        0xFE,
        (
            "#660FLadies and gentlemen, your efforts\x01",
            "are most appreciated.\x02\x03",
            "I would gladly work with you again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8D2")

    Jump("loc_B2F")

    label("loc_8D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A5F")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "#662FYou may have already heard...\x02\x03",
            "A thief has broken into\x01",
            "my estate and stolen a\x01",
            "precious heirloom.\x02\x03",
            "#664FThat being a family matter, however, I cannot\x01",
            "allow it to get in the way of my work. Which\x01",
            "is why I've asked the guild for assistance.\x02\x03",
            "#660FI will let Gilbert fill you in\x01",
            "on the specifics.\x02\x03",
            "If you should need assistance\x01",
            "with your investigation, please\x01",
            "let him know.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B2F")

    label("loc_A5F")


    ChrTalk(
        0xFE,
        (
            "#662FA thief has broken into\x01",
            "my estate and stolen a\x01",
            "precious heirloom.\x02\x03",
            "#660FI will let Gilbert fill you in\x01",
            "on the specifics.\x02\x03",
            "If you should need assistance\x01",
            "with your investigation, please\x01",
            "let him know.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B2F")

    Jump("loc_F04")

    label("loc_B32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_C13")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BCD")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "#660FIt is truly dreadful, what's\x01",
            "happened to Matron Theresa.\x02\x03",
            "I will do anything I can to help.\x02\x03",
            "I feel it is my duty as mayor.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C10")

    label("loc_BCD")


    ChrTalk(
        0xFE,
        (
            "#660FIt is truly dreadful, what's\x01",
            "happened to Matron Theresa.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C10")

    Jump("loc_F04")

    label("loc_C13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_DCE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D22")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "#660FI'm sure you've heard that \x01",
            "someone from the Royal Family\x01",
            "is currently visiting Ruan.\x02\x03",
            "In light of yesterday's incident\x01",
            "and the potential dangers\x01",
            "to His Excellency...\x02\x03",
            "Jean is being called upon to\x01",
            "make certain that his visit\x01",
            "goes smoothly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DCB")

    label("loc_D22")


    ChrTalk(
        0xFE,
        (
            "#660FI'm sure you've heard that \x01",
            "someone from the Royal Family\x01",
            "is currently visiting Ruan.\x02\x03",
            "Jean is being called upon to\x01",
            "make certain that his visit\x01",
            "goes smoothly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DCB")

    Jump("loc_F04")

    label("loc_DCE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 4)), scpexpr(EXPR_END)), "loc_F04")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E7D")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "#660FAh, here you are.\x02\x03",
            "I've received many complaints\x01",
            "from the townsfolk regarding\x01",
            "that gang.\x02\x03",
            "Something will eventually have\x01",
            "to be done about them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F04")

    label("loc_E7D")


    ChrTalk(
        0xFE,
        (
            "#660FI've received many complaints\x01",
            "from the townsfolk regarding\x01",
            "that gang.\x02\x03",
            "Something will eventually have\x01",
            "to be done about them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F04")

    TalkEnd(0x8)
    Return()

    # Function_4_744 end

    def Function_5_F08(): pass

    label("Function_5_F08")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_10B0")
    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FFD")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "#670FHello, bracers. You've done\x01",
            "some fine work.\x02\x03",
            "Now, we can go to the campus\x01",
            "festival and actually enjoy ourselves.\x02\x03",
            "This presents an opportunity\x01",
            "to meet many of the students.\x02\x03",
            "We look forward to it every year.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10AA")

    label("loc_FFD")


    ChrTalk(
        0xFE,
        (
            "#670FNow, we can go to the campus\x01",
            "festival and actually enjoy ourselves.\x02\x03",
            "This presents an opportunity\x01",
            "to meet many of the students.\x02\x03",
            "We look forward to it every year.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10AA")

    TalkEnd(0x10)
    Jump("loc_16CD")

    label("loc_10B0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x0, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13FC")
    TalkBegin(0x10)

    ChrTalk(
        0xFE,
        "#670FHmm? Did you need something?\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[Confirm the card's details]\x01",      # 0
            "[Never mind]\x01",                      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1167"),
        (1, "loc_13A8"),
        (SWITCH_DEFAULT, "loc_13A8"),
    )


    label("loc_1167")


    ChrTalk(
        0xFE,
        (
            "#670FAhh, the card.\x02\x03",
            "Please, have a look.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "'That which nests here is a beast more dire than\x01",
            "any other. Continue to give praise to the spirit\x01",
            "whose blue light was lost in the darkness. Free\x01",
            "the spark it left behind, and I will be free. Ahh,\x01",
            "seeker. The eyes of Aidios see only the truth,\x01",
            "and pass it on to you.'\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "'Look to the three-eyed giant which towers over\x01",
            "this settlement. Do so, and the blue light will be\x01",
            "revealed.\x01\x01",
            "-Phantom Thief B'\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(400)

    ChrTalk(
        0xFE,
        (
            "#670FThat being the case, I ask that\x01",
            "you continue your investigation.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13F6")

    label("loc_13A8")


    ChrTalk(
        0xFE,
        (
            "#670FThat being the case, I ask that\x01",
            "you continue your investigation.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13F6")

    label("loc_13F6")

    TalkEnd(0x10)
    Jump("loc_16CD")

    label("loc_13FC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x0, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_141A")
    Call(1, 0)
    Jump("loc_16CD")

    label("loc_141A")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_1540")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14C5")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "#671FDo you have any suspects?\x02\x03",
            "Those hoodlums certainly can't\x01",
            "be allowed to run about freely.\x02\x03",
            "So many questions, piling atop\x01",
            "one another...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_153D")

    label("loc_14C5")


    ChrTalk(
        0xFE,
        (
            "#670FThose hoodlums certainly can't\x01",
            "be allowed to run about freely.\x02\x03",
            "So many questions, piling atop\x01",
            "one another...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_153D")

    Jump("loc_16CA")

    label("loc_1540")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_15F3")

    ChrTalk(
        0xFE,
        (
            "#670FFor every just and true person, there\x01",
            "is another like those you met yesterday.\x02\x03",
            "I suspect we may wind up employing your\x01",
            "services as bracers before too long...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16CA")

    label("loc_15F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 4)), scpexpr(EXPR_END)), "loc_16CA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1694")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "#671FThose Ravens are getting to be\x01",
            "a real bother.\x02\x03",
            "If they're allowed to run free,\x01",
            "they'll do severe damage to\x01",
            "the town's reputation.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16CA")

    label("loc_1694")


    ChrTalk(
        0xFE,
        (
            "#671FThose Ravens are getting to\x01",
            "be real bother.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16CA")

    TalkEnd(0x10)

    label("loc_16CD")

    Return()

    # Function_5_F08 end

    def Function_6_16CE(): pass

    label("Function_6_16CE")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_21BC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x0, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x1, 0x200)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_208C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x1, 0x400)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_200C")
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, -760, 0, -1810, 0)
    SetChrPos(0x102, -1660, -250, -2470, 0)
    SetChrPos(0x105, -660, -500, -2740, 0)
    TurnDirection(0xC, 0x101, 0)
    TurnDirection(0xD, 0x101, 0)
    OP_4A(0xD, 255)
    OP_28(0x20, 0x1, 0x400)
    OP_28(0x20, 0x1, 0x800)
    OP_6D(-1090, -250, -2370, 0)
    OP_0D()
    Sleep(100)
    OP_62(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(
        0xC,
        "Hi, there!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Please, take a look. The candelabrum\x01",
            "has been returned.\x02",
        )
    )

    CloseMessageWindow()
    OP_8B(0x101, 0xA, 0xF46, 0x190)
    Sleep(100)
    OP_8B(0x105, 0xA, 0xF46, 0x190)
    OP_8B(0x102, 0xA, 0xF46, 0x190)

    ChrTalk(
        0x101,
        (
            "#501FOh, you're right.\x02\x03",
            "Who got it back?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Well...no one did.\x01",
            "No one we know anyway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "It was simply returned, at some point.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "I've no idea why, though...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505FSo the thief returned it?\x02\x03",
            "I get that it wasn't stolen for\x01",
            "money...but what was the\x01",
            "thief thinking?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_191C():
        TurnDirection(0x102, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_191C)

    def lambda_192A():
        TurnDirection(0x105, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_192A)
    TurnDirection(0x101, 0xC, 400)

    ChrTalk(
        0x102,
        "#012FSo, when was it brought back?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x102, 400)

    ChrTalk(
        0xC,
        "Ah, yes...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Umm...well...the master of the\x01",
            "house was arrested the next day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#013F...I see.\x02",
    )

    CloseMessageWindow()

    def lambda_19D7():
        TurnDirection(0x105, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_19D7)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#501FSomething wrong?\x02",
    )

    CloseMessageWindow()

    def lambda_1A07():
        TurnDirection(0xC, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1A07)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#012FWell...this is just conjecture\x01",
            "on my part...\x02\x03",
            "...but what if the candelabrum\x01",
            "wasn't what the thief wanted,\x01",
            "but rather the mayor, himself?\x02\x03",
            "Otherwise, I can't figure out\x01",
            "any reason to bring the\x01",
            "candelabrum back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002FSo you're saying someone wanted\x01",
            "to expose what the mayor was up\x01",
            "to?\x02\x03",
            "Whatever happened to lodging a\x01",
            "simple complaint or just plain\x01",
            "old notifying the guild?\x02\x03",
            "Why go to the trouble of taking the\x01",
            "candelabrum and leaving behind a\x01",
            "card with a freaking novel on it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013FNot to expose a crime,\x01",
            "that's for sure...\x02\x03",
            "I hate to say it...but I think it\x01",
            "was probably just for fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012FWhoever did this had to have\x01",
            "known what the mayor was\x01",
            "really like from the beginning.\x02\x03",
            "They knew that, by stealing\x01",
            "the candelabrum, bracers would\x01",
            "be called to investigate.\x02\x03",
            "And there's no chance that the\x01",
            "way he was living wouldn't come\x01",
            "to light.\x02\x03",
            "There's also the risk that the\x01",
            "room where those monsters\x01",
            "were kept could be discovered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F...So he actually snapped because\x01",
            "we were putting too much pressure\x01",
            "on him?\x02\x03",
            "#003FRight. I'll bet the mayor and his\x01",
            "cronies were breaking out in\x01",
            "cold sweats.\x02\x03",
            "He wouldn't want his estate \x01",
            "being investigated, but he\x01",
            "had to avoid suspicion...\x02\x03",
            "#002F...and wasn't he grinning like mad\x01",
            "when he saw the arsonists?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FProbably. But we can't jump\x01",
            "to conclusions.\x02\x03",
            "Still, I can't think of any other\x01",
            "scenario that would make\x01",
            "sense of this case.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1FA5():
        TurnDirection(0x105, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1FA5)
    OP_8C(0x101, 0, 400)

    ChrTalk(
        0x101,
        (
            "#505F'Phantom Thief B'...\x02\x03",
            "What a bizarre person.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Sleep(50)
    EventEnd(0x4)
    OP_8C(0xC, 90, 0)
    OP_8C(0xD, 270, 0)
    OP_4B(0xD, 255)
    Jump("loc_2089")

    label("loc_200C")


    ChrTalk(
        0xFE,
        (
            "The candelabrum was put back,\x01",
            "at some point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Right around when the mayor\x01",
            "was arrested...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I just don't get it.\x02",
    )

    CloseMessageWindow()

    label("loc_2089")

    Jump("loc_21B9")

    label("loc_208C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x0, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_214F")

    ChrTalk(
        0xFE,
        (
            "This candelabrum had been stolen,\x01",
            "not too long ago...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But now, it's been put back\x01",
            "where it was.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Right around when the mayor\x01",
            "was arrested...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I just don't get it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_21B9")

    label("loc_214F")


    ChrTalk(
        0xFE,
        (
            "Who would have believed that\x01",
            "the mayor would be arrested?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What's to become of this\x01",
            "estate, now?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21B9")

    Jump("loc_2700")

    label("loc_21BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_2297")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2243")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        "Hmmm hmm hmm...la la la...侓\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, those piercing amber-colored\x01",
            "eyes...I swear, I could get lost\x01",
            "in them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2294")

    label("loc_2243")


    ChrTalk(
        0xFE,
        (
            "Oh, those piercing amber-\x01",
            "colored eyes...I swear,\x01",
            "I could get lost in them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2294")

    Jump("loc_2700")

    label("loc_2297")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_239C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2345")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "We had an Erebonian Imperial \x01",
            "Ambassador come to visit here,\x01",
            "not too long ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems that many of high\x01",
            "status have been coming by,\x01",
            "of late.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2399")

    label("loc_2345")


    ChrTalk(
        0xFE,
        (
            "We had an Erebonian Imperial \x01",
            "Ambassador come to visit here,\x01",
            "not too long ago.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2399")

    Jump("loc_2700")

    label("loc_239C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_249F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2464")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "I saw another bracer out on the\x01",
            "street earlier. He had brilliant\x01",
            "red hair and sharp eyes.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "There's just something about\x01",
            "a wild-looking man...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_249C")

    label("loc_2464")


    ChrTalk(
        0xFE,
        (
            "There's just something about\x01",
            "a wild-looking man...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_249C")

    Jump("loc_2700")

    label("loc_249F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_262A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2593")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "The mayor's always been the\x01",
            "head of House Dalmore...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since the mayor comes from such\x01",
            "a noble background, he carries\x01",
            "quite a bit of clout.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This estate has belonged to the head\x01",
            "of the Dalmores for generations.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2627")

    label("loc_2593")


    ChrTalk(
        0xFE,
        (
            "The mayor's always been the\x01",
            "head of House Dalmore...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since the mayor comes from such\x01",
            "a noble background, he carries\x01",
            "quite a bit of clout.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2627")

    Jump("loc_2700")

    label("loc_262A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 7)), scpexpr(EXPR_END)), "loc_2669")

    ChrTalk(
        0xFE,
        (
            "The mayor's returned, so I'm\x01",
            "preparing his tea.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2700")

    label("loc_2669")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 4)), scpexpr(EXPR_END)), "loc_2700")

    ChrTalk(
        0xFE,
        (
            "I'm terribly sorry, but the mayor\x01",
            "isn't here at the moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you would like to give him a\x01",
            "message, I'd be happy to take\x01",
            "it for you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2700")

    TalkEnd(0xC)
    Return()

    # Function_6_16CE end

    def Function_7_2704(): pass

    label("Function_7_2704")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_28EB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2841")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27CB")
    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "I've gotten wrapped up in this\x01",
            "whole mess...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think that Dario and I are\x01",
            "going to leave soon and go\x01",
            "find new jobs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe I should become\x01",
            "a guide...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_283E")

    label("loc_27CB")


    ChrTalk(
        0xFE,
        (
            "I think that Dario and I are\x01",
            "going to leave soon and go\x01",
            "find new jobs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe I should become\x01",
            "a guide...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_283E")

    Jump("loc_28E8")

    label("loc_2841")


    ChrTalk(
        0xFE,
        (
            "I have nothing to do with House\x01",
            "Dalmore's family heirlooms.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Right now, I'm just trying to\x01",
            "focus on finding a new job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe I should become\x01",
            "a guide...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28E8")

    Jump("loc_2D97")

    label("loc_28EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_2935")

    ChrTalk(
        0xFE,
        "Oh, dear...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My little daughter seems\x01",
            "utterly smitten.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D97")

    label("loc_2935")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_29F4")

    ChrTalk(
        0xFE,
        (
            "For an influential man, he certainly\x01",
            "isn't all that impressive...but, he\x01",
            "is probably coming from a long ways away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I suppose that orbal communication\x01",
            "works well enough...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D97")

    label("loc_29F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_2A7E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A5F")
    OP_A2(0x3)

    ChrTalk(
        0xFE,
        "Flora's at it again...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I want her to move her hands,\x01",
            "rather than her mouth.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A7B")

    label("loc_2A5F")


    ChrTalk(
        0xFE,
        "Flora's at it again...\x02",
    )

    CloseMessageWindow()

    label("loc_2A7B")

    Jump("loc_2D97")

    label("loc_2A7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_2CAA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C10")
    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "Can't do much of anything\x01",
            "about all the things that\x01",
            "the mayor says.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They say that the mayor is elected\x01",
            "because of his lineage...well, they're\x01",
            "half right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Upset the townsfolk enough, and\x01",
            "you can be sure that they'll\x01",
            "fight back in some way or other.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...But it was those townsfolk who\x01",
            "elected him, all the same.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They share the blame for this,\x01",
            "don't you know.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CA7")

    label("loc_2C10")


    ChrTalk(
        0xFE,
        (
            "Can't do much of anything\x01",
            "about all the things that\x01",
            "the mayor says.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The mayor is elected because\x01",
            "of his lineage...but that's only\x01",
            "half true.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CA7")

    Jump("loc_2D97")

    label("loc_2CAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 7)), scpexpr(EXPR_END)), "loc_2D48")

    ChrTalk(
        0xFE,
        (
            "He himself may not have realized\x01",
            "what kind of man he'd become...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But Gilbert always seemed to\x01",
            "be the sort who'd cave in to\x01",
            "unsavory folk.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D97")

    label("loc_2D48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 4)), scpexpr(EXPR_END)), "loc_2D97")

    ChrTalk(
        0xFE,
        "I'm busy right now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Leave me be for the time being,\x01",
            "will you?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D97")

    TalkEnd(0xD)
    Return()

    # Function_7_2704 end

    def Function_8_2D9B(): pass

    label("Function_8_2D9B")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2E50")

    ChrTalk(
        0xFE,
        (
            "I've served House Dalmore for\x01",
            "over thirty years...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That such a distinguished family, with\x01",
            "a long history of dedicated service to\x01",
            "Ruan, should come to this...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3215")

    label("loc_2E50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_2EDC")

    ChrTalk(
        0xFE,
        (
            "I must wonder what's being discussed\x01",
            "behind these doors right now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The master is speaking with\x01",
            "Duke Dunan, you see...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3215")

    label("loc_2EDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_3046")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2F93")

    ChrTalk(
        0xFE,
        "Hello, bracers.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I understand that the candelabrum\x01",
            "has been safely recovered?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Allow me to speak for all of\x01",
            "the servants when I express\x01",
            "my gratitude.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3043")

    label("loc_2F93")


    ChrTalk(
        0xFE,
        (
            "I would never have thought that\x01",
            "such a precious heirloom could\x01",
            "be stolen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I know that it was securely locked\x01",
            "up. I can't imagine how thieves\x01",
            "could have gotten to it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3043")

    Jump("loc_3215")

    label("loc_3046")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_30CF")

    ChrTalk(
        0xFE,
        (
            "The candelabrum is an heirloom\x01",
            "of House Dalmore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Handling an item of such\x01",
            "extreme value can be\x01",
            "quite nerve-wracking.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3215")

    label("loc_30CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_3176")

    ChrTalk(
        0xFE,
        (
            "I have immense respect for the\x01",
            "master's good name.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Feudal lords may no longer exist,\x01",
            "but House Dalmore still bears a\x01",
            "great deal of responsibility.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3215")

    label("loc_3176")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 7)), scpexpr(EXPR_END)), "loc_31AD")

    ChrTalk(
        0xFE,
        (
            "The master has been very busy,\x01",
            "of late.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3215")

    label("loc_31AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 4)), scpexpr(EXPR_END)), "loc_3215")

    ChrTalk(
        0xFE,
        "Are you guests of the house?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm dreadfully sorry, but the\x01",
            "master is not currently in.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3215")

    TalkEnd(0x12)
    Return()

    # Function_8_2D9B end

    def Function_9_3219(): pass

    label("Function_9_3219")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_32B3")

    ChrTalk(
        0xFE,
        (
            "I'd always thought the mayor to\x01",
            "be a fine man, and I was proud\x01",
            "to prepare his meals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We've come to a sorry state,\x01",
            "more's the pity.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3539")

    label("loc_32B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_331C")

    ChrTalk(
        0xFE,
        "Now, where's that Gilbert lad?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'd heard that we had an\x01",
            "important guest coming in...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3539")

    label("loc_331C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_33A6")

    ChrTalk(
        0xFE,
        (
            "Using cutlery from the Far East\x01",
            "takes some true skill.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But lately, such cutlery has been\x01",
            "quite popular amongst chefs.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3539")

    label("loc_33A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_3423")

    ChrTalk(
        0xFE,
        "Lunch will be ready soon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Today is salmon marinade on \x01",
            "garlic toast and free-range\x01",
            "herb-roasted chicken.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3539")

    label("loc_3423")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_34CE")

    ChrTalk(
        0xFE,
        (
            "The mayor could be very particular about\x01",
            "what he'd eat as a child. Nowadays,\x01",
            "though, he'll eat almost anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Perhaps it's just part of being mayor.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3539")

    label("loc_34CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 4)), scpexpr(EXPR_END)), "loc_3539")

    ChrTalk(
        0xFE,
        (
            "Cookware is the life's blood\x01",
            "of a chef.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's why it absolutely must\x01",
            "be well-maintained.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3539")

    TalkEnd(0x13)
    Return()

    # Function_9_3219 end

    def Function_10_353D(): pass

    label("Function_10_353D")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "'Sapphire Glim'\x01",
            "Said to be the culmination of early orbal arts.\x01",
            "Given to House Dalmore by the citizens of Ruan\x01",
            "immediately after the Orbal Revolution, as\x01",
            "thanks for contributions to the city's growth.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_10_353D end

    def Function_11_3638(): pass

    label("Function_11_3638")

    EventBegin(0x0)
    OP_6D(-6240, 0, 6040, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    SetChrPos(0xC, -5830, 0, 5580, 315)
    SetChrPos(0x101, -600, -500, -3890, 0)
    SetChrPos(0x102, 950, -500, -3720, 315)
    SetChrPos(0x105, 570, -500, -5040, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_4A(0xC, 255)
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0xC, 0x101, 400)

    def lambda_36F2():
        OP_6D(-760, -500, -2510, 3000)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_36F2)
    OP_8E(0xC, 0xFFFFFDBC, 0x0, 0xFFFFF95C, 0xBB8, 0x0)
    TurnDirection(0xC, 0x101, 400)
    WaitChrThread(0xC, 0x1)

    ChrTalk(
        0xC,
        "Welcome to the Ruan mayoral estate.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I'm terribly sorry, but the\x01",
            "mayor is currently attending\x01",
            "to some guests...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Perhaps you could come\x01",
            "back another time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009FWhat...?! Now hold on,\x01",
            "just one second...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015FI'm pretty sure we know who\x01",
            "the guest is. \x02\x03",
            "It's Duke Dunan, isn't it?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#004FWha...?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x102, 400)

    ChrTalk(
        0xC,
        "Why, that's exactly it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Have you received an\x01",
            "invitation as well?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FYes. It came directly from\x01",
            "the mayor himself.\x02\x03",
            "I apologize for the inconvenience,\x01",
            "but would you mind...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Now that I take a closer look,\x01",
            "you appear to be bracers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "If circumstances demand it,\x01",
            "then please, go on up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "The mayor and duke are in the\x01",
            "banquet hall on the second floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019FExcellent.\x01",
            "Thank you for your help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "*blush*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Oh, right!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "W-With so many guests arriving,\x01",
            "I really must prepare some tea.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Please, pardon me!\x02",
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0xC, 90, 400)

    def lambda_3ADD():
        OP_6D(1390, 0, -20, 3000)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_3ADD)

    def lambda_3AF5():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3AF5)

    def lambda_3B03():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3B03)

    def lambda_3B11():

        label("loc_3B11")

        TurnDirection(0xFE, 0xC, 400)
        OP_48()
        Jump("loc_3B11")

    QueueWorkItem2(0x102, 1, lambda_3B11)
    OP_8E(0xC, 0x1432, 0x0, 0x49C, 0xBB8, 0x0)
    OP_44(0x102, 0xFF)
    SetChrFlags(0xC, 0x4)
    OP_8E(0xC, 0x2DF0, 0x0, 0x29E, 0xBB8, 0x0)
    ClearChrFlags(0xC, 0x4)
    SetChrPos(0xC, 33500, 0, 24550, 270)
    WaitChrThread(0xC, 0x1)
    OP_6D(-630, -500, -2970, 2000)

    ChrTalk(
        0x101,
        "#004F#3P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#044F...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x102, 225, 400)

    ChrTalk(
        0x102,
        "#014F#2PWhat?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007F#3POh, nothing...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#045FU-Um...\x02\x03",
            "#040FI was just thinking how\x01",
            "impressive it was that you\x01",
            "knew the duke was here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#2POh, it's just a matter of\x01",
            "asking the right questions.\x02\x03",
            "He's planning to sell vacation homes\x01",
            "to the rich, remember?\x02\x03",
            "Duke Dunan might as well have a\x01",
            "bull's-eye target painted on his\x01",
            "misshapen head...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#044FWow...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009F#3PThat's smart thinking.\x02\x03",
            "Where'd you come up with that\x01",
            "line about the mayor inviting us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#011F#2PIt wasn't a 'line'.\x02\x03",
            "He did invite us over, the\x01",
            "first time we met him.\x02\x03",
            "'If those Ravens start making trouble\x01",
            "again, feel free to drop by and let me\x01",
            "know,' or something like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F#3POh... That's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#048FHa ha... So he did invite us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F#2PExactly.\x02\x03",
            "#010FWell, why don't we head up\x01",
            "to the banquet hall?\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    OP_4B(0xC, 255)
    Return()

    # Function_11_3638 end

    def Function_12_3ED8(): pass

    label("Function_12_3ED8")

    EventBegin(0x0)
    OP_6D(-2510, 0, 40990, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x14, 20, 700, 39500, 0)
    SetChrPos(0x15, -900, 700, 38600, 0)
    SetChrPos(0x16, -150, 850, 38740, 0)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x105, 0x80)
    SetChrPos(0x101, 11020, 0, 36640, 270)
    SetChrPos(0x102, 11020, 0, 36640, 270)
    SetChrPos(0x105, 11020, 0, 36640, 270)
    SetChrFlags(0xA, 0x4)
    SetChrFlags(0x8, 0x4)
    OP_4A(0x8, 255)
    SetChrPos(0xA, -50, 200, 40550, 180)
    SetChrPos(0x8, -2000, 0, 38810, 90)
    SetChrPos(0xB, 950, 0, 41760, 180)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0xA,
        (
            "#227F#2P*hic*...\x01",
            "I like the sound of that.\x02\x03",
            "Ruan would be the perfect\x01",
            "place for a vacation home.\x02\x03",
            "I think I might stay for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#661F#1PHa ha... I had a feeling\x01",
            "you'd think so.\x02\x03",
            "I'll see to it that you get the\x01",
            "finest place available, my Lord.\x02\x03",
            "I believe you'll be quite satisfied.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#227F#2PHa ha ha... You're quite the\x01",
            "smooth talker.\x02\x03",
            "#483FBut good. Money is no object.\x02\x03",
            "Prepare me an estate that is\x01",
            "worthy of your future king.\x02\x03",
            "Make it as splendid as\x01",
            "your holdings here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#722FPardon me, my Lord, but \x01",
            "wait a moment...\x02\x03",
            "The queen asked you to\x01",
            "consult with her before\x01",
            "spending such an amount of--\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 1)

    ChrTalk(
        0xA,
        (
            "#482F#2PSilence, Phillip! I am to be\x01",
            "your next king!\x02\x03",
            "Such purchases are everyday\x01",
            "for a man of my standing!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#661F#1PYes, of course...\x01",
            "Well said, Your Excellency.\x02\x03",
            "We can get a written contract\x01",
            "together shortly.\x02\x03",
            "But first, one more drink...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0)

    ChrTalk(
        0xA,
        "#481F#2POhh ho...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1PHi there! Greetings from the\x01",
            "Bracer Guild!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_43FF():
        OP_6D(-380, 0, 39240, 2000)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_43FF)
    OP_43(0x101, 0x1, 0x0, 0xE)
    OP_43(0x102, 0x1, 0x0, 0xF)
    OP_43(0x105, 0x1, 0x0, 0x10)
    SetChrSubChip(0xA, 1)
    OP_8C(0xB, 135, 400)
    WaitChrThread(0x105, 0x1)

    ChrTalk(
        0x8,
        "#663FYou...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#480F*hic*...\x01",
            "What do you people want?\x02\x03",
            "You look...kind of familiar...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#721FOh, it's you...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006FHi, Mr. Butler.\x02\x03",
            "We just dropped by to talk\x01",
            "to the mayor. No biggie.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#662FThis won't do...\x02\x03",
            "If you're here on guild business,\x01",
            "you should speak with some\x01",
            "semblance of manners.\x02\x03",
            "I'm in the middle of an\x01",
            "important discussion, so why\x01",
            "don't you come back later?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015FI apologize for our rudeness,\x01",
            "Mayor. We intend no disrespect.\x02\x03",
            "We simply came to report to\x01",
            "you that we have identified\x01",
            "the arsonist.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#664FAh, that...\x01",
            "Well, then I suppose...\x02\x03",
            "#661FMy Lord, would you excuse us\x01",
            "for a moment?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0)
    Sleep(300)

    ChrTalk(
        0xA,
        (
            "#227F*hic*... No... Say what you're\x01",
            "going to say here.\x02\x03",
            "This sounds interesting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#663FB-But...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006FIt's okay! Maybe the duke\x01",
            "will have something to add.\x02\x03",
            "It won't do any harm for him\x01",
            "to hear this, will it?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 1)

    ChrTalk(
        0x8,
        (
            "#662FWell, if we must...\x02\x03",
            "While we're on the subject,\x01",
            "it seems that Matron Theresa\x01",
            "was attacked again last night.\x02\x03",
            "Could the arsonist be\x01",
            "linked to that? \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012FIt seems very likely.\x02\x03",
            "Unfortunately, the attackers\x01",
            "are still at large.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#662FI see...\x02\x03",
            "Still, at least you say you\x01",
            "know who they are now.\x02\x03",
            "So, who did it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006FHmm, who indeed?\x02\x03",
            "It's exactly who you think\x01",
            "it is, Mayor Dalmore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#664FAh, I see...\x01",
            "That's quite a shame.\x02\x03",
            "I was hoping I could make\x01",
            "them see the error of their\x01",
            "ways before it was too late.\x02\x03",
            "I suppose that was a vain\x01",
            "hope on my part.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004FHuh? Who are you talking\x01",
            "about, Mr. Mayor?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#661FWhat do you mean, 'who'?\x02\x03",
            "Why, the Ravens, of course.\x02\x03",
            "They've been in hiding ever\x01",
            "since last night...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015FI'm sorry, sir...but they\x01",
            "aren't responsible.\x02\x03",
            "This time, they claim to be\x01",
            "victims themselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#663FWh-What?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#502FSo, without further ado...\x01",
            "The culprit is...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[Mayor Dalmore]\x01",        # 0
            "[Duke Dunan]\x01",           # 1
            "[Steward Gilbert]\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4BD6"),
        (1, "loc_4C1A"),
        (2, "loc_4DD7"),
        (SWITCH_DEFAULT, "loc_4E62"),
    )


    label("loc_4BD6")

    OP_20(0x3E8)
    Sleep(1000)
    OP_1D(0x51)

    ChrTalk(
        0x101,
        "#005F#3S...you, Mayor Dalmore!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Jump("loc_4E62")

    label("loc_4C1A")

    Sleep(400)

    ChrTalk(
        0x101,
        "#005F#3S...you, Duke Dunan!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_9E(0xA, 0xF, 0x0, 0x12C, 0xFA0)
    OP_62(0xA, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(
        0xA,
        "#484FWh-What?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#721FY-You must be mistaken!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#018FEstelle...I'm seriously beginning\x01",
            "to worry about having you as my\x01",
            "partner...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(
        0x105,
        "#045FEstelle...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008FHee hee...\x01",
            "Okay, maybe I'm wrong!\x02\x03",
            "#502FAnyway, the real culprit is...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4D7D():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4D7D)

    def lambda_4D8B():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4D8B)
    OP_20(0x3E8)
    Sleep(1000)
    OP_1D(0x51)

    ChrTalk(
        0x101,
        "#005F#3S...you, Mayor Dalmore!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Jump("loc_4E62")

    label("loc_4DD7")


    ChrTalk(
        0x101,
        (
            "#002F...the mayor's steward, Gilbert!\x02\x03",
            "Acting on the orders of...\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x3E8)
    Sleep(1000)
    OP_1D(0x51)

    ChrTalk(
        0x101,
        "#005F#3S...you, Mayor Dalmore!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Jump("loc_4E62")

    label("loc_4E62")


    ChrTalk(
        0x8,
        "#663F!!!\x02",
    )

    OP_9E(0x8, 0xF, 0x0, 0x12C, 0xFA0)
    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012FWe already have Gilbert in custody,\x01",
            "and we know everything.\x02\x03",
            "We also have proof that you stole\x01",
            "the money donated to restore the\x01",
            "orphanage YOUR lackey set on fire.\x02\x03",
            "Can you deny that charge?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#665FN-Nonsense!\x02\x03",
            "Do you think I know those\x01",
            "people in the black clothes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006FWell, now...that's a little strange.\x02\x03",
            "We didn't say anything about\x01",
            "black clothes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#666F*gulp*\x02\x03",
            "This is absolutely ridiculous!\x01",
            "Gilbert was acting alone!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007FYou don't know when to\x01",
            "give up, do you, old man?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012FWe know that you were plotting\x01",
            "to build vacation homes on the\x01",
            "land the orphanage occupied.\x02\x03",
            "Do you still deny the charges\x01",
            "laid against you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#665FPersistent little brats!\x02\x03",
            "But I've had those development\x01",
            "plans in place for ages!\x02\x03",
            "They're just part of Ruan's\x01",
            "city planning!\x02\x03",
            "What reason would I have to be so\x01",
            "impatient that I'd resort to\x01",
            "criminal acts?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004FW-Well...\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 11020, 0, 36640, 270)

    NpcTalk(
        0x9,
        "Man's Voice",
        (
            "#1P...How about a mountain of\x01",
            "debts to pay off?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_52CB():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_52CB)

    def lambda_52D9():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_52D9)

    def lambda_52E7():

        label("loc_52E7")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_52E7")

    QueueWorkItem2(0x102, 1, lambda_52E7)

    def lambda_52F8():

        label("loc_52F8")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_52F8")

    QueueWorkItem2(0x105, 1, lambda_52F8)
    Sleep(200)

    def lambda_530E():

        label("loc_530E")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_530E")

    QueueWorkItem2(0x101, 1, lambda_530E)
    SetChrFlags(0x9, 0x4)
    OP_8E(0x9, 0xC26, 0x0, 0x8FB6, 0xBB8, 0x0)
    ClearChrFlags(0x9, 0x4)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x105, 0xFF)

    ChrTalk(
        0x101,
        "#004FNial?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014FWhat are you doing here...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#141FI figured I'd come to the mayor's\x01",
            "place to do some investigating...\x01",
            "when I see you two going in.\x02\x03",
            "The whole thing smelled fishy,\x01",
            "so I decided to sneak in.\x02\x03",
            "#147FThat's it in a nutshell. 噴\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#663FJ-Just who the hell are you?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#140FOh, I'm a reporter with the\x01",
            "Liberl News. The name's\x01",
            "Nial Burns.\x02\x03",
            "Actually, I've been checking\x01",
            "into the city's financial\x01",
            "affairs recently.\x02\x03",
            "And what do I see, but that Mayor\x01",
            "Dalmore here has been diverting\x01",
            "funds from the city budget lately...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_5587():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_5587)

    def lambda_5595():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5595)

    def lambda_55A3():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_55A3)

    def lambda_55B1():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_55B1)
    SetChrSubChip(0xA, 0)

    ChrTalk(
        0x8,
        (
            "#663FI... That's...\x02\x03",
            "They're funds for the\x01",
            "expansion project...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#142FI'm not buying it. You haven't\x01",
            "even started construction.\x02\x03",
            "I thought it was kind of strange,\x01",
            "so I dug deeper, and found links\x01",
            "to the airship company's services.\x02\x03",
            "Now, that was quite the\x01",
            "little surprise.\x02\x03",
            "One year ago, you took more than a\x01",
            "few trips to the Calvard Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#663FI... I was just sightseeing...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#145FA reasonable claim.\x02\x03",
            "But the truth is that you've\x01",
            "amassed a nice, big debt\x01",
            "over there, am I right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#666F!!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505FUmm... You're losing me. How?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#043FBy using town funds to speculate\x01",
            "in risky commodities, in the\x01",
            "hopes of cashing in.\x02\x03",
            "Buying goods when they're cheap,\x01",
            "selling them when they're high.\x01",
            "That kind of thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501FOh, I get it.\x02\x03",
            "So, how much did he lose?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#140FFrom what my fellow reporters\x01",
            "over there told me...\x02\x03",
            "Something to the tune of\x01",
            "100,000,000 mira.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#005F#3SOne h-h-hundred million mira?!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015FThat's a hundred times the\x01",
            "amount donated to the\x01",
            "orphanage's rebuilding...\x02\x03",
            "I can certainly see why one\x01",
            "might turn to crime over an\x01",
            "amount that high.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#481F*hic* A hundred million...\x02\x03",
            "#483FI'm pretty free with my spending,\x01",
            "but I've got nothing on you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#666F*gulp*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007FThis isn't a competition,\x01",
            "you know...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#145FNow that you mention it...\x02\x03",
            "He took funds from the city\x01",
            "budget to pay off his debts\x01",
            "and stave off any questions.\x02\x03",
            "But I can't understand why he\x01",
            "would turn to arson and theft to\x01",
            "build his vacation homes.\x02\x03",
            "#141FIt just all seems so...random.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#664F...\x02\x03",
            "Hmph. Where is your proof?\x02\x03",
            "#665FGo ahead and run your story, with\x01",
            "all its wild speculations. I'll sue\x01",
            "you and the newspaper for libel!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#143FSuddenly confident, are we?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#665FAnd you all!\x02\x03",
            "The Bracer Guild does NOT have\x01",
            "the authority to arrest me!\x01",
            "I'm the mayor!!\x02\x03",
            "I want you out of here, NOW!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#009FHmm, I guess he's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012FHe knows his rights.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#049F...\x02\x03",
            "Mayor...may I ask you one\x01",
            "question?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#665FWhat now?!\x02\x03",
            "What is a student of the Royal\x01",
            "Academy doing, associating with\x01",
            "such people...? Disgraceful!\x02\x03",
            "Return to campus at once!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#042F...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Kloe looked Mayor Dalmore directly in the eyes, her expression cold and\x01",
            "stern.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x8,
        "#663F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#043FWhy did you not use your own\x01",
            "assets to pay off your debt?\x02\x03",
            "One hundred million mira is\x01",
            "certainly a lot of money...\x02\x03",
            "But I think that House Dalmore\x01",
            "surely has enough assets to\x01",
            "settle the matter.\x02\x03",
            "This estate, for instance? It\x01",
            "would easily sell for at least\x01",
            "a hundred million mira.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#665FD-Don't be ridiculous!\x02\x03",
            "This estate has been handed\x01",
            "down in the Dalmore family\x01",
            "for generations!\x02\x03",
            "How could I ever simply\x01",
            "let it go?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#049FThe orphanage was no different.\x02\x03",
            "For many it was a place\x01",
            "fondly remembered.\x02\x03",
            "No one has the right to destroy\x01",
            "something like that.\x02\x03",
            "#042FHow could you do such a thing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#668FH-How dare you liken this estate\x01",
            "to that dilapidated old hovel?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#047FYou care for no one but yourself...\x02\x03",
            "More than being the mayor, or\x01",
            "being the head of House Dalmore...\x02\x03",
            "#049FYou pitiful man...\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0x8, 0xF, 0x0, 0x12C, 0xFA0)

    ChrTalk(
        0x8,
        "#668F...\x02",
    )

    CloseMessageWindow()
    OP_9E(0x8, 0xF, 0x0, 0x190, 0x1388)

    ChrTalk(
        0x8,
        (
            "#667FHa ha... Ha ha ha ha ha...\x02\x03",
            "You have quite a way with\x01",
            "words, young lady...\x02\x03",
            "...but let's see if you'll\x01",
            "change your tune in a few\x01",
            "minutes!\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrPos(0x8, -2230, 0, 39700, 90)
    SetChrSubChip(0xA, 2)
    OP_0D()
    OP_8C(0x8, 270, 400)

    def lambda_62FF():
        OP_6D(-2940, 0, 40120, 2000)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_62FF)
    OP_8E(0x8, 0xFFFFE2F0, 0x0, 0x9EB6, 0xBB8, 0x0)
    Sleep(500)
    OP_20(0x5DC)
    OP_72(0x10, 0x800)
    OP_22(0x70, 0x0, 0x64)
    OP_72(0x10, 0x10)
    OP_70(0x10, 0x12C)
    Sleep(1500)

    ChrTalk(
        0x8,
        (
            "#667F#3SFango! Bronco!\x02\x03",
            "#3SCome! It's dinner time!\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x8, 0xFFFFE2D2, 0x0, 0x98DA, 0xBB8, 0x0)
    TurnDirection(0x8, 0x101, 400)
    OP_73(0x10)

    ChrTalk(
        0x101,
        "#580F#2PWh-What the...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#016F#2PThat smell...!\x02",
    )

    CloseMessageWindow()

    def lambda_63DF():
        OP_6D(-500, 0, 39570, 3000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_63DF)

    def lambda_63F7():
        OP_6C(291000, 4000)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_63F7)

    def lambda_6407():
        OP_6B(3100, 2000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6407)
    OP_1D(0x56)
    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xE, 6)
    SetChrPos(0xE, -9610, 0, 41180, 0)
    OP_8E(0xE, 0xFFFFE4B2, 0x0, 0x9F4C, 0xFA0, 0x0)
    OP_8E(0xE, 0xFFFFEFB6, 0x0, 0xA276, 0xFA0, 0x0)
    TurnDirection(0xE, 0x101, 400)
    SetChrChipByIndex(0xE, 5)
    OP_43(0xE, 0x1, 0x0, 0x2)
    ClearChrFlags(0xF, 0x80)
    SetChrChipByIndex(0xF, 21)
    SetChrPos(0xF, -9610, 0, 41180, 0)
    OP_8E(0xF, 0xFFFFE4B2, 0x0, 0x9F4C, 0x1388, 0x0)
    OP_8E(0xF, 0xFFFFEE26, 0x0, 0x9844, 0x1388, 0x0)
    TurnDirection(0xF, 0x101, 400)
    SetChrChipByIndex(0xF, 20)
    OP_43(0xF, 0x1, 0x0, 0x2)

    ChrTalk(
        0x9,
        (
            "#144F#1PWh-What the hell are\x01",
            "those things?!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(
        0xA,
        (
            "#484F#4PM-Monsterrrs?!\x02\x03",
            "#228FUrrrggh...*gurgle gurgle*...\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x20C, 0x0, 0x64)
    SetChrSubChip(0xA, 3)
    Sleep(500)
    TurnDirection(0xB, 0xA, 0)

    ChrTalk(
        0xB,
        "#721FM-My Lord!\x02",
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0xB, 0x30C, 0x0, 0x9F06, 0xBB8, 0x0)
    TurnDirection(0xB, 0xA, 0)

    ChrTalk(
        0x105,
        (
            "#042FUnbelievable... You actually\x01",
            "keep monsters as pets...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#667F#6PHeh heh heh...\x02\x03",
            "Everything you think you know\x01",
            "will die with you here...\x02\x03",
            "Don't worry. If there's anything\x01",
            "left of you I'll dump it in the\x01",
            "river.\x02\x03",
            "HAAA HA HA HA!\x02",
        )
    )

    CloseMessageWindow()
    OP_94(0x1, 0x9, 0xB4, 0x3E8, 0xBB8, 0x0)

    ChrTalk(
        0x9,
        "#142F#1PH-He's crazy...\x02",
    )

    CloseMessageWindow()

    def lambda_66BA():
        OP_6D(1064, 0, 38330, 1000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_66BA)

    def lambda_66D2():
        OP_6C(315000, 1000)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_66D2)

    def lambda_66E2():
        OP_6B(2800, 800)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_66E2)
    SetChrChipByIndex(0xE, 6)
    OP_96(0xE, 0x226, 0x5DC, 0x9646, 0x7D0, 0x1770)
    OP_22(0xEC, 0x0, 0x64)
    Fade(500)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x19, 0x100)
    ClearChrFlags(0x17, 0x100)
    ClearChrFlags(0x18, 0x100)
    SetChrPos(0x17, 320, 1000, 39500, 0)
    SetChrPos(0x18, -100, 1500, 38100, 0)
    SetChrPos(0x19, 700, 1450, 38140, 0)
    OP_51(0x19, 0x2A, (scpexpr(EXPR_PUSH_LONG, 0x7530), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x2B, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x2C, (scpexpr(EXPR_PUSH_LONG, 0xFFFDF0A8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x2A, (scpexpr(EXPR_PUSH_LONG, 0x7530), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x2B, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x2C, (scpexpr(EXPR_PUSH_LONG, 0xFFFEA070), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x18, 0x2A, (scpexpr(EXPR_PUSH_LONG, 0x7530), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x18, 0x2B, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x18, 0x2C, (scpexpr(EXPR_PUSH_LONG, 0xFFFD40E0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x18, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x18, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x18, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_7C(0x0, 0x1F4, 0xBB8, 0x64)
    SetChrChipByIndex(0xE, 5)
    OP_43(0xE, 0x1, 0x0, 0x2)
    OP_0D()
    OP_22(0x195, 0x0, 0x64)

    ChrTalk(
        0xE,
        "#3PGrrrrrrrrrrrr...\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xF, 21)
    OP_96(0xF, 0x1B8, 0x5DC, 0x8C82, 0x7D0, 0x1770)
    OP_22(0xEC, 0x0, 0x64)
    OP_7C(0x0, 0x1F4, 0xBB8, 0x64)
    SetChrChipByIndex(0xF, 20)
    OP_43(0xF, 0x1, 0x0, 0x2)
    Sleep(500)
    OP_22(0x195, 0x0, 0x64)

    ChrTalk(
        0xF,
        "#3PRrrrrrrrrrrrr...\x02",
    )

    CloseMessageWindow()

    def lambda_68DB():
        OP_94(0x1, 0xFE, 0xB4, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_68DB)
    Sleep(100)

    def lambda_68F6():
        OP_94(0x1, 0xFE, 0xB4, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_68F6)
    Sleep(100)

    def lambda_6911():
        OP_94(0x1, 0xFE, 0xB4, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6911)
    WaitChrThread(0x101, 0x1)
    SetChrFlags(0x101, 0x1000)
    SetChrChipByIndex(0x101, 8)
    WaitChrThread(0x102, 0x1)
    SetChrFlags(0x102, 0x1000)
    SetChrChipByIndex(0x102, 9)
    WaitChrThread(0x105, 0x1)
    SetChrFlags(0x105, 0x1000)
    SetChrChipByIndex(0x105, 10)

    ChrTalk(
        0x101,
        (
            "#002FSo...is fighting freaky monsters\x01",
            "part of the 'stalling' plan now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012FWell, at least now we can arrest him for\x01",
            "trying to kill us. I'm sure the other\x01",
            "stuff will stick, too, after this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#047FI bear you both no ill will...\x02\x03",
            "#046FBut I will not allow you to\x01",
            "harm anyone!\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xE, 7)
    SetChrFlags(0xE, 0x20)
    OP_51(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_6A89():
        OP_96(0xFE, 0x132E, 0x0, 0x9632, 0xBB8, 0x1770)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_6A89)
    Sleep(150)
    SetChrChipByIndex(0xF, 22)
    SetChrFlags(0xF, 0x20)
    OP_51(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_6AC1():
        OP_96(0xFE, 0x132E, 0x0, 0x8A7A, 0x9C4, 0x1770)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_6AC1)
    Sleep(400)
    Battle(0x394, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_6AF7"),
        (SWITCH_DEFAULT, "loc_6AFA"),
    )


    label("loc_6AF7")

    OP_B4(0x0)
    Return()

    label("loc_6AFA")

    OP_A2(0x3FB)
    NewScene("ED6_DT01/T2210   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_12_3ED8 end

    def Function_13_6B07(): pass

    label("Function_13_6B07")

    EventBegin(0x0)
    OP_1D(0x51)
    OP_4A(0x8, 255)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0xA, -50, 200, 40550, 180)
    SetChrSubChip(0xA, 3)
    SetChrPos(0xB, 780, 0, 40710, 225)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x19, 0x100)
    ClearChrFlags(0x17, 0x100)
    ClearChrFlags(0x18, 0x100)
    SetChrPos(0x17, 320, 1000, 39500, 0)
    SetChrPos(0x18, -100, 1500, 38100, 0)
    SetChrPos(0x19, 700, 1450, 38140, 0)
    OP_51(0x19, 0x2A, (scpexpr(EXPR_PUSH_LONG, 0x7530), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x2B, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x2C, (scpexpr(EXPR_PUSH_LONG, 0xFFFDF0A8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x2A, (scpexpr(EXPR_PUSH_LONG, 0x7530), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x2B, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x2C, (scpexpr(EXPR_PUSH_LONG, 0xFFFEA070), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x18, 0x2A, (scpexpr(EXPR_PUSH_LONG, 0x7530), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x18, 0x2B, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x18, 0x2C, (scpexpr(EXPR_PUSH_LONG, 0xFFFD40E0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x18, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x18, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x18, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6F(0x10, 300)
    OP_72(0x10, 0x10)
    OP_44(0xF, 0xFF)
    OP_44(0xE, 0xFF)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0xE, 0x80)
    OP_6D(-5830, 0, 39000, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(346000, 0)
    OP_6E(280, 0)
    SetChrPos(0x8, -5850, 0, 40270, 180)
    SetChrPos(0x101, -5500, 0, 35010, 0)
    SetChrPos(0x102, -6750, 0, 35300, 0)
    SetChrPos(0x105, -4320, 0, 35440, 0)
    SetChrPos(0x9, -2140, 0, 42020, 270)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#668FI-It can't be...\x01",
            "My sweet babies...\x02\x03",
            "How could you do this?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#005F*huff* *huff*... \x01",
            "You're one to talk!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012FIn accordance with Bracer Guild protocol,\x01",
            "and this time with authority, we're\x01",
            "placing you under arrest.\x02\x03",
            "Surrender and you will\x01",
            "not be harmed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#667FHeh heh heh...\x02\x03",
            "You leave me no choice...but\x01",
            "to use my trump card!\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_22(0x8F, 0x0, 0x64)
    SetChrChipByIndex(0x8, 18)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x101,
        "#580FHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012FA wand...?\x02",
    )

    CloseMessageWindow()

    def lambda_6EB7():
        OP_91(0xFE, 0x0, 0x0, 0x3E8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_6EB7)
    Sleep(100)

    def lambda_6ED7():
        OP_6C(315000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_6ED7)

    def lambda_6EE7():
        OP_6D(-6640, 0, 41150, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6EE7)

    def lambda_6EFF():
        OP_90(0xFE, 0x0, 0x0, 0x170C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6EFF)

    def lambda_6F1A():
        OP_90(0xFE, 0x0, 0x0, 0x170C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6F1A)

    def lambda_6F35():
        OP_90(0xFE, 0x0, 0x0, 0x170C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6F35)
    Sleep(600)
    OP_22(0xC5, 0x0, 0x64)
    OP_44(0x8, 0xFF)
    LoadEffect(0x0, "map\\\\mp006_00.eff")
    PlayEffect(0x0, 0x0, 0x8, -350, 1100, 200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    ChrTalk(
        0x8,
        "#665FTime-stop!\x05\x02",
    )

    FadeToDark(1, 16777215, -1)
    OP_44(0x9, 0xFF)
    OP_44(0x101, 0x1)
    OP_44(0x102, 0x1)
    OP_44(0x105, 0x1)
    OP_0D()
    OP_43(0x101, 0x1, 0x0, 0x15)
    FadeToBright(400, 16777215)
    Sleep(500)
    OP_9E(0x101, 0xF, 0x0, 0x12C, 0xFA0)
    Sleep(700)
    OP_9E(0x101, 0xF, 0x0, 0x12C, 0xFA0)

    ChrTalk(
        0x101,
        "#581FI... I can't move!\x02",
    )

    CloseMessageWindow()
    OP_9E(0x102, 0xF, 0x0, 0x12C, 0xFA0)

    ChrTalk(
        0x102,
        "#513FD-Did he use...an orbal art?\x02",
    )

    CloseMessageWindow()
    OP_9E(0x105, 0xF, 0x0, 0x12C, 0xFA0)

    ChrTalk(
        0x105,
        (
            "#541FN-No...\x02\x03",
            "This has to be...an artifact!\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0x9, 0xF, 0x0, 0x12C, 0xFA0)

    ChrTalk(
        0x9,
        "#144FSo what the hell is that?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#667F#4PWell, well. Your knowledge is\x01",
            "impressive, Miss Rinz.\x02\x03",
            "This is the Chronos Rod,\x01",
            "an artifact which happens to\x01",
            "be a family heirloom.\x02\x03",
            "It can completely paralyze\x01",
            "anyone within range in the\x01",
            "blink of an eye.\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0x101, 0xF, 0x0, 0x12C, 0xFA0)

    ChrTalk(
        0x101,
        "#581FTh-That's crazy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#513FHow does the church not know\x01",
            "about such a powerful artifact...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#667F#4PHa ha... With a tool crafted by\x01",
            "the wise ancients themselves,\x01",
            "what else would one expect?\x02\x03",
            "Tactical orbments can't even\x01",
            "begin to compare to this.\x02\x03",
            "Sadly, it only has that one\x01",
            "function.\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x8, 19)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#667F#4PWhich means I'll have to sully\x01",
            "my hands and dispose of you\x01",
            "myself.\x02\x03",
            "Heh heh... You should consider\x01",
            "this an honor.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_738F():
        OP_6D(-6640, 0, 40150, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_738F)
    OP_92(0x8, 0x101, 0x76C, 0x3E8, 0x0)

    ChrTalk(
        0x8,
        (
            "#667F#4PLet's see... I think I'll start\x01",
            "with the smart-mouthed little\x01",
            "brat first...\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0x101, 0xF, 0x0, 0x12C, 0xFA0)

    ChrTalk(
        0x101,
        (
            "#009FWho are you calling\x01",
            "'smart-mouthed'?!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x105, 200)

    ChrTalk(
        0x8,
        (
            "#667F#4PPerhaps I'll save the intelligent\x01",
            "girl for last...?\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0x105, 0xF, 0x0, 0x12C, 0xFA0)

    ChrTalk(
        0x105,
        "#042F...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 200)

    ChrTalk(
        0x8,
        (
            "#667F#4PHeh heh... Now, what was that you\x01",
            "were saying about 'authority'?\x02\x03",
            "You could plead for your lives.\x01",
            "It might help, but I doubt it...\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0x101, 0xF, 0x0, 0x12C, 0xFA0)

    ChrTalk(
        0x101,
        "#005FTo you? Yeah, right!\x02",
    )

    CloseMessageWindow()
    OP_9E(0x102, 0xF, 0x0, 0x12C, 0xFA0)

    ChrTalk(
        0x102,
        "#013FKeep your filthy hands...off...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#663F#4PWhat's that?\x02",
    )

    CloseMessageWindow()

    def lambda_75DA():
        OP_9E(0x102, 0xF, 0x0, 0x7D0, 0xFA0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_75DA)

    ChrTalk(
        0x102,
        (
            "#510FKeep your filthy hands off\x01",
            "of Estelle...\x02\x03",
            "Don't you...harm a single hair\x01",
            "on her head...\x02\x03",
            "...or I'll use every technique\x01",
            "I know...to cut your miserable\x01",
            "carcass to pieces...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(
        0x8,
        "#668F#4PWha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#580FJ-Joshua...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#044FJoshua...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#666F#4PY-You certainly talk big for\x01",
            "someone who can't even wiggle\x01",
            "his fingers...\x02\x03",
            "#666FFine! I'll start with you!\x02",
        )
    )

    CloseMessageWindow()
    OP_92(0x8, 0x102, 0x4B0, 0x3E8, 0x0)
    TurnDirection(0x8, 0x102, 400)
    Sleep(400)
    OP_9E(0x101, 0xF, 0x0, 0x12C, 0xFA0)

    ChrTalk(
        0x101,
        (
            "#005FS-Stop!!\x02\x03",
            "I'll never let you get away\x01",
            "with hurting him!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#510F...\x02",
    )

    CloseMessageWindow()
    OP_9E(0x105, 0xF, 0x0, 0x12C, 0xFA0)

    ChrTalk(
        0x105,
        "#043FJoshua!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#667F#4PDie.\x02",
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    OP_44(0x101, 0xFF)

    def lambda_7830():
        OP_9E(0x101, 0xF, 0x0, 0x7D0, 0xFA0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7830)

    ChrTalk(
        0x101,
        "#504FNOOOOOOOOOOO!!!!\x02",
    )

    CloseMessageWindow()
    OP_22(0x90, 0x0, 0x64)
    LoadEffect(0x1, "map\\\\mp007_01.eff")
    PlayEffect(0x1, 0x2, 0x101, 350, 800, 200, 0, 0, 0, 100, 100, 100, 0xFF, 0, 0, 0, 0)
    OP_77(0xBE, 0xBE, 0xBE, 0x7D000, 0x0)
    OP_0D()
    Sleep(1600)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(
        0x8,
        "#668F#4PWha...?!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 180, 400)
    OP_8F(0x8, 0xFFFFE87C, 0x0, 0xA1B8, 0xBB8, 0x0)
    OP_77(0xA0, 0xA0, 0xA0, 0x3E800, 0x0)

    ChrTalk(
        0x105,
        "#044FThat light...\x02",
    )

    CloseMessageWindow()
    OP_77(0x82, 0x82, 0x82, 0x3E800, 0x0)

    ChrTalk(
        0x9,
        (
            "#142F#4PDamn it... If I could just\x01",
            "reach my camera...\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x91, 0x0, 0x64)
    LoadEffect(0x1, "map\\\\mp015_00.eff")
    PlayEffect(0x1, 0x3, 0x101, 350, 800, 200, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_77(0x64, 0x64, 0x64, 0x1F400, 0x0)
    Sleep(500)
    OP_23(0x90)
    OP_82(0x2, 0x2)
    OP_82(0x0, 0x2)
    OP_77(0xFF, 0xFF, 0xFF, 0x3E800, 0x0)
    Sleep(1500)

    ChrTalk(
        0x8,
        "#668FWha... What's going on?!\x02",
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_51(0x101, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    Sleep(50)
    OP_44(0x102, 0xFF)
    OP_51(0x102, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x102, 65535)
    SetChrSubChip(0x102, 0)
    Sleep(50)
    OP_44(0x105, 0xFF)
    OP_51(0x105, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x105, 65535)
    SetChrSubChip(0x105, 0)
    Sleep(500)

    ChrTalk(
        0x105,
        "#044FI... I can move again...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#014FEstelle...what was that\x01",
            "black light?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004FI don't know...\x02\x03",
            "But I think...\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x101, 25)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x1A, -5500, 500, 38500, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#505F...it came from that orbment\x01",
            "Dad sent us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#668FI-Impossible...\x02\x03",
            "#668FMy family heirloom...\x01",
            "My artifact...\x01",
            "It's broken!!\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x1A, 0x80)
    SetChrChipByIndex(0x101, 65535)

    def lambda_7B94():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7B94)

    def lambda_7BA2():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7BA2)

    def lambda_7BB0():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7BB0)

    ChrTalk(
        0x102,
        (
            "#015FIt hardly matters...since you've\x01",
            "played your last hand.\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0x1F5, 0x0, 0x64)
    SetChrChipByIndex(0x102, 9)
    OP_0D()

    ChrTalk(
        0x102,
        "#012FIt's time to face reality. \x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#009FY-Yeah!\x02",
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0x1F4, 0x0, 0x64)
    SetChrChipByIndex(0x101, 8)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#005FI can't believe you'd really\x01",
            "stoop this low!\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0x1F8, 0x0, 0x64)
    SetChrChipByIndex(0x105, 10)
    OP_0D()

    ChrTalk(
        0x105,
        "#042FIt's disgusting...\x02",
    )

    CloseMessageWindow()
    OP_9E(0x8, 0xF, 0x0, 0x12C, 0xFA0)

    ChrTalk(
        0x8,
        (
            "#666FGrrrr...\x02\x03",
            "...I will NOT be taken in!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7CFE():

        label("loc_7CFE")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_7CFE")

    QueueWorkItem2(0x101, 1, lambda_7CFE)

    def lambda_7D0F():

        label("loc_7D0F")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_7D0F")

    QueueWorkItem2(0x102, 1, lambda_7D0F)

    def lambda_7D20():

        label("loc_7D20")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_7D20")

    QueueWorkItem2(0x105, 1, lambda_7D20)
    SetChrChipByIndex(0x8, 0)
    OP_8C(0x8, 270, 800)
    OP_8E(0x8, 0xFFFFDDB4, 0x0, 0x9FBA, 0x1770, 0x0)
    SetChrFlags(0x8, 0x80)

    ChrTalk(
        0x101,
        "#005FAah!\x02",
    )

    CloseMessageWindow()
    OP_1D(0x52)

    ChrTalk(
        0x102,
        "#016FAfter him!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#046FOkay!\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 65535)
    OP_43(0x101, 0x1, 0x0, 0x11)
    Sleep(400)
    SetChrChipByIndex(0x102, 65535)
    OP_43(0x102, 0x1, 0x0, 0x11)
    Sleep(300)
    SetChrChipByIndex(0x105, 65535)
    OP_43(0x105, 0x1, 0x0, 0x11)
    WaitChrThread(0x105, 0x1)

    ChrTalk(
        0x9,
        (
            "#144F#4PHey, wait up!\x02\x03",
            "I can't let a story like this\x01",
            "get away!\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x9, 0x1, 0x0, 0x11)
    Sleep(2000)
    OP_6D(-1160, 0, 41000, 2000)

    ChrTalk(
        0xB,
        (
            "#722F#4POh, my... I believe I've lost\x01",
            "a few years off of what little\x01",
            "remains to me.\x02\x03",
            "My Lord...\x01",
            "Are you all right, my Lord?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#228F#3PNnnngh... Monsters... The monsters...\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x105, 0x80)
    SetChrFlags(0x9, 0x80)
    Fade(1000)
    OP_6D(-61080, 0, 54230, 0)
    SetChrPos(0x8, -59900, 0, 51220, 0)

    def lambda_7F14():
        OP_8E(0xFE, 0xFFFF0B8C, 0x0, 0xC634, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_7F14)
    OP_43(0x101, 0x1, 0x0, 0x12)
    Sleep(700)

    def lambda_7F3B():
        OP_96(0xFE, 0xFFFF0696, 0xFFFFEC78, 0xC724, 0x3E8, 0x1770)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_7F3B)
    OP_43(0x102, 0x1, 0x0, 0x12)
    Sleep(700)
    OP_43(0x105, 0x1, 0x0, 0x12)
    WaitChrThread(0x101, 0x1)
    OP_72(0xF, 0x10)
    OP_6F(0xF, 29)
    Fade(1000)
    OP_6D(-61320, 0, -38840, 0)
    OP_43(0x101, 0x1, 0x0, 0x13)
    Sleep(700)
    OP_43(0x102, 0x1, 0x0, 0x13)
    Sleep(700)
    OP_43(0x105, 0x1, 0x0, 0x13)
    Sleep(2200)
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_43(0x9, 0x1, 0x0, 0x14)
    Sleep(500)
    WaitChrThread(0x101, 0x1)
    Sleep(1000)
    SetMapFlags(0x2000000)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T2200   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_13_6B07 end

    def Function_14_7FEB(): pass

    label("Function_14_7FEB")

    ClearChrFlags(0xFE, 0x80)
    OP_8F(0xFE, 0x1D4C, 0x0, 0x92C2, 0xFA0, 0x0)
    OP_8F(0xFE, 0xA6E, 0x0, 0x9A1A, 0xFA0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_14_7FEB end

    def Function_15_8020(): pass

    label("Function_15_8020")

    Sleep(500)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x1D38, 0x0, 0x909C, 0xFA0, 0x0)
    OP_8E(0xFE, 0xD02, 0x0, 0x9416, 0xFA0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_15_8020 end

    def Function_16_805A(): pass

    label("Function_16_805A")

    Sleep(1000)
    ClearChrFlags(0xFE, 0x80)
    OP_8F(0xFE, 0x1D38, 0x0, 0x909C, 0xFA0, 0x0)
    OP_8F(0xFE, 0xFFA, 0x0, 0x968C, 0xFA0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_16_805A end

    def Function_17_8094(): pass

    label("Function_17_8094")

    OP_8E(0xFE, 0xFFFFE264, 0x0, 0x9F92, 0x1770, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0xFFFFCED2, 0x0, 0xA032, 0x1770, 0x0)
    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_17_8094 end

    def Function_18_80CC(): pass

    label("Function_18_80CC")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -55480, 0, 54970, 0)
    OP_8E(0xFE, 0xFFFF1DB6, 0x0, 0xD692, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFF18D4, 0x0, 0xCB66, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFF05F6, 0x0, 0xCBFC, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x4)

    def lambda_8129():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_8129)
    OP_96(0xFE, 0xFFFF04CA, 0xFFFFFE0C, 0xC6D4, 0x3E8, 0x1770)
    Sleep(100)
    OP_8F(0xFE, 0xFFFF04CA, 0xFFFFE0C0, 0xC6D4, 0xFA0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_18_80CC end

    def Function_19_8167(): pass

    label("Function_19_8167")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -62450, 2310, -43030, 270)
    OP_8F(0xFE, 0xFFFF0C0E, 0x3E8, 0xFFFF57EA, 0xFA0, 0x0)
    ClearChrFlags(0xFE, 0x4)
    OP_96(0xFE, 0xFFFF0F9C, 0x0, 0xFFFF57B8, 0xC8, 0xFA0)
    OP_8E(0xFE, 0xFFFF0D8A, 0x0, 0xFFFF6B54, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFF04E8, 0x0, 0xFFFF6CD0, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_19_8167 end

    def Function_20_81DB(): pass

    label("Function_20_81DB")

    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x4)
    SetChrPos(0xFE, -62450, 2310, -43030, 270)
    OP_96(0xFE, 0xFFFF0E02, 0x0, 0xFFFF57EA, 0xC8, 0x1770)
    OP_96(0xFE, 0xFFFF0F9C, 0x0, 0xFFFF57B8, 0x12C, 0x1770)
    Sleep(500)
    OP_8E(0xFE, 0xFFFF0D8A, 0x0, 0xFFFF6B54, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFF04E8, 0x0, 0xFFFF6CD0, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_20_81DB end

    def Function_21_8257(): pass

    label("Function_21_8257")

    OP_77(0xCD, 0xED, 0xF0, 0x0, 0x0)

    label("loc_8260")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8288")
    OP_77(0xCD, 0xED, 0xF0, 0x1F400, 0x0)
    Sleep(1000)
    OP_77(0x8C, 0xCE, 0xFF, 0x1F400, 0x0)
    Sleep(1000)
    Jump("loc_8260")

    label("loc_8288")

    Return()

    # Function_21_8257 end

    def Function_22_8289(): pass

    label("Function_22_8289")

    NewScene("ED6_DT01/T2210   ._SN", 123, 1, 0)
    IdleLoop()
    Return()

    # Function_22_8289 end

    def Function_23_8293(): pass

    label("Function_23_8293")

    NewScene("ED6_DT01/T2210   ._SN", 121, 1, 0)
    IdleLoop()
    Return()

    # Function_23_8293 end

    def Function_24_829D(): pass

    label("Function_24_829D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There's a drawbridge control unit here.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_24_829D end

    SaveToFile()

Try(main)
