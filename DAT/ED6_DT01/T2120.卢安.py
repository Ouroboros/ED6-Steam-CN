from ED6ScenarioHelper import *

def main():
    # 卢安

    CreateScenaFile(
        FileName            = 'T2120   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2120.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60012",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/T2120   ._SN',
            'ED6_DT01/T2120_1 ._SN',
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
        'Jean',                                 # 9
        'Carna',                                # 10
        'Agate',                                # 11
        'Tobias',                               # 12
        'Karl',                                 # 13
        'Zack',                                 # 14
        'Eva',                                  # 15
        'Nikita',                               # 16
        'Melvin',                               # 17
        "O'Neil",                               # 18
        'Seagaro',                              # 19
        'Edel',                                 # 20
        'Targeting Camera',                     # 21
        'Orbment',                              # 22
        'Jimmy',                                # 23
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
        'ED6_DT07/CH01240 ._CH',             # 00
        'ED6_DT07/CH02400 ._CH',             # 01
        'ED6_DT06/CH20053 ._CH',             # 02
        'ED6_DT07/CH01020 ._CH',             # 03
        'ED6_DT07/CH01190 ._CH',             # 04
        'ED6_DT07/CH01460 ._CH',             # 05
        'ED6_DT07/CH01210 ._CH',             # 06
        'ED6_DT07/CH01590 ._CH',             # 07
        'ED6_DT07/CH01760 ._CH',             # 08
        'ED6_DT07/CH01100 ._CH',             # 09
        'ED6_DT07/CH01040 ._CH',             # 0A
        'ED6_DT07/CH01210 ._CH',             # 0B
        'ED6_DT06/CH20021 ._CH',             # 0C
        'ED6_DT06/CH20034 ._CH',             # 0D
        'ED6_DT07/CH01040 ._CH',             # 0E
    )

    AddCharChipPat(
        'ED6_DT07/CH01240P._CP',             # 00
        'ED6_DT07/CH02400P._CP',             # 01
        'ED6_DT06/CH20053P._CP',             # 02
        'ED6_DT07/CH01020P._CP',             # 03
        'ED6_DT07/CH01190P._CP',             # 04
        'ED6_DT07/CH01460P._CP',             # 05
        'ED6_DT07/CH01210P._CP',             # 06
        'ED6_DT07/CH01590P._CP',             # 07
        'ED6_DT07/CH01760P._CP',             # 08
        'ED6_DT07/CH01100P._CP',             # 09
        'ED6_DT07/CH01040P._CP',             # 0A
        'ED6_DT07/CH01210P._CP',             # 0B
        'ED6_DT06/CH20021P._CP',             # 0C
        'ED6_DT06/CH20034P._CP',             # 0D
        'ED6_DT07/CH01040P._CP',             # 0E
    )

    DeclNpc(
        X                   = -5700,
        Z                   = 0,
        Y                   = 45100,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x105,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = -400,
        Z                   = 0,
        Y                   = 45400,
        Direction           = 90,
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
        Y                   = 33500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -30000,
        Z                   = 0,
        Y                   = 4910,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 3100,
        Z                   = 4000,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -3700,
        Z                   = 0,
        Y                   = 42600,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 1200,
        Z                   = 0,
        Y                   = 5000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 5360,
        Z                   = 4000,
        Y                   = 5510,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -38000,
        Z                   = 0,
        Y                   = 47490,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 29900,
        Z                   = 0,
        Y                   = 4500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 31800,
        Z                   = 0,
        Y                   = 2500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 28500,
        Z                   = 0,
        Y                   = 700,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x81,
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
        Unknown3            = 917516,
        ChipIndex           = 0xC,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 28570,
        Z                   = 0,
        Y                   = 1980,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )


    DeclActor(
        TriggerX            = 1070,
        TriggerZ            = 0,
        TriggerY            = 43260,
        TriggerRange        = 1400,
        ActorX              = 1070,
        ActorZ              = 2000,
        ActorY              = 43260,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 0,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -30020,
        TriggerZ            = 0,
        TriggerY            = 3590,
        TriggerRange        = 400,
        ActorX              = -30000,
        ActorZ              = 1500,
        ActorY              = 4910,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 1020,
        TriggerZ            = 0,
        TriggerY            = 3000,
        TriggerRange        = 400,
        ActorX              = 1200,
        ActorZ              = 1500,
        ActorY              = 5000,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 29980,
        TriggerZ            = 0,
        TriggerY            = 3310,
        TriggerRange        = 400,
        ActorX              = 29900,
        ActorZ              = 1500,
        ActorY              = 4500,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -4420,
        TriggerZ            = 0,
        TriggerY            = 45090,
        TriggerRange        = 600,
        ActorX              = -5700,
        ActorZ              = 1500,
        ActorY              = 45100,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_3B6",          # 00, 0
        "Function_1_5AE",          # 01, 1
        "Function_2_60F",          # 02, 2
        "Function_3_625",          # 03, 3
        "Function_4_631",          # 04, 4
        "Function_5_FEA",          # 05, 5
        "Function_6_1C75",         # 06, 6
        "Function_7_1D12",         # 07, 7
        "Function_8_1D17",         # 08, 8
        "Function_9_27E6",         # 09, 9
        "Function_10_2A78",        # 0A, 10
        "Function_11_2C3C",        # 0B, 11
        "Function_12_3D4D",        # 0C, 12
        "Function_13_43E7",        # 0D, 13
        "Function_14_4763",        # 0E, 14
        "Function_15_4768",        # 0F, 15
        "Function_16_5685",        # 10, 16
        "Function_17_5777",        # 11, 17
        "Function_18_57E0",        # 12, 18
        "Function_19_5888",        # 13, 19
        "Function_20_60C5",        # 14, 20
        "Function_21_732D",        # 15, 21
        "Function_22_79A7",        # 16, 22
        "Function_23_998D",        # 17, 23
        "Function_24_A1AC",        # 18, 24
        "Function_25_B831",        # 19, 25
    )


    def Function_0_3B6(): pass

    label("Function_0_3B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3F1")
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8)
    ClearChrFlags(0x10, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1E, 0x0, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E4")
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x10)
    Jump("loc_3EE")

    label("loc_3E4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1E, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3EE")

    label("loc_3EE")

    Jump("loc_523")

    label("loc_3F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_436")
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8)
    ClearChrFlags(0x10, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1E, 0x0, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_429")
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x10)
    Jump("loc_433")

    label("loc_429")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1E, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_433")

    label("loc_433")

    Jump("loc_523")

    label("loc_436")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_47B")
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1E, 0x0, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46E")
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x10)
    Jump("loc_478")

    label("loc_46E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1E, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_478")

    label("loc_478")

    Jump("loc_523")

    label("loc_47B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_4A5")
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8)
    SetChrPos(0x9, -36210, 0, 41450, 270)
    ClearChrFlags(0x10, 0x80)
    Jump("loc_523")

    label("loc_4A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_4CD")
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    Jump("loc_523")

    label("loc_4CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_4F2")
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8)
    SetChrPos(0x9, -36210, 0, 41450, 270)
    Jump("loc_523")

    label("loc_4F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 7)), scpexpr(EXPR_END)), "loc_512")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x9, -36400, 0, 41270, 270)
    Jump("loc_523")

    label("loc_512")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_523")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8)

    label("loc_523")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_532")
    SetChrFlags(0xC, 0x80)
    Jump("loc_53F")

    label("loc_532")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_53F")
    SetChrFlags(0xC, 0x80)

    label("loc_53F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_54D")
    OP_A3(0x3FA)
    Event(0, 23)

    label("loc_54D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_55B")
    OP_A3(0x3FB)
    Event(0, 24)

    label("loc_55B")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (105, "loc_567"),
        (SWITCH_DEFAULT, "loc_5AD"),
    )


    label("loc_567")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_576")
    OP_A2(0x414)
    Event(0, 19)

    label("loc_576")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_597")
    OP_A2(0x418)
    Event(0, 20)
    SetMapFlags(0x10000000)
    OP_B1("t2120_n")

    label("loc_597")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5AA")
    OP_A2(0x42D)
    Event(0, 22)

    label("loc_5AA")

    Jump("loc_5AD")

    label("loc_5AD")

    Return()

    # Function_0_3B6 end

    def Function_1_5AE(): pass

    label("Function_1_5AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x89, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x89, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5C3")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5E4")
    OP_B1("t2120_y")
    Jump("loc_5ED")

    label("loc_5E4")

    OP_B1("t2120_n")

    label("loc_5ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5FE")
    OP_1B(0x6, 0x0, 0x19)
    OP_64(0x4, 0x1)

    label("loc_5FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_60E")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x56), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_60E")

    Return()

    # Function_1_5AE end

    def Function_2_60F(): pass

    label("Function_2_60F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_624")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_60F")

    label("loc_624")

    Return()

    # Function_2_60F end

    def Function_3_625(): pass

    label("Function_3_625")

    Call(0, 4)
    OP_8C(0xB, 180, 0)
    Return()

    # Function_3_625 end

    def Function_4_631(): pass

    label("Function_4_631")

    TalkBegin(0xB)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",                 # 0
            "Modify/Exchange\x01",      # 1
            "Leave\x01",                # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_69C")
    OP_0D()
    OP_A9(0x1E)
    OP_56(0x0)
    TalkEnd(0xB)
    Return()

    label("loc_69C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6AD")
    TalkEnd(0xB)
    Return()

    label("loc_6AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_6F4")

    ChrTalk(
        0xB,
        "Thank you very much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Feel free to stop by anytime.\x02",
    )

    CloseMessageWindow()
    Jump("loc_FE6")

    label("loc_6F4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x1, 0x8000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_716")
    Call(1, 1)
    Jump("loc_FE6")

    label("loc_716")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_7B1")

    ChrTalk(
        0xB,
        (
            "I'm relieved to know that the\x01",
            "mayor's been arrested.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Since House Dalmore has no\x01",
            "more heirs, we'll have to elect\x01",
            "a new mayor, won't we?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FE6")

    label("loc_7B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_90C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_874")
    OP_A2(0x0)

    ChrTalk(
        0xB,
        (
            "Rumor has it that a duke is\x01",
            "here to inspect the area.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "But if he is, I haven't seen\x01",
            "him at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I have seen an old man in nice\x01",
            "clothes who talks funny, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_909")

    label("loc_874")


    ChrTalk(
        0xB,
        (
            "Rumor has it that a duke is\x01",
            "here to inspect the area.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I haven't seen the duke, but I\x01",
            "have seen an old man in nice\x01",
            "clothes who talks funny.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_909")

    Jump("loc_FE6")

    label("loc_90C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_ACB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A4D")
    OP_A2(0x0)

    ChrTalk(
        0xB,
        (
            "It's good that Mayor Dalmore\x01",
            "has expanded tourism...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "He's had to resort to coercing\x01",
            "the ones against it, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I just hope everyone can\x01",
            "come to an agreement.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Here's hoping that the tourism\x01",
            "drives off the Ravens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Don't you think a gang like that\x01",
            "is bad for a place's image?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AC8")

    label("loc_A4D")


    ChrTalk(
        0xB,
        (
            "I just hope that the tourism\x01",
            "drives off the Ravens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Don't you think a gang like that\x01",
            "is bad for a place's image?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AC8")

    Jump("loc_FE6")

    label("loc_ACB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_B70")

    ChrTalk(
        0xB,
        (
            "I've had a lot of Royal Academy\x01",
            "students in here, buying up all\x01",
            "kinds of colored lights.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Come to think of it, the campus\x01",
            "festival isn't far off.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FE6")

    label("loc_B70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_C46")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C20")
    OP_A2(0x0)

    ChrTalk(
        0xB,
        "Ahhh...it's almost lunchtime.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I just can't work on an\x01",
            "empty stomach.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "One of the staples of Ruanian\x01",
            "cuisine is paella with plenty\x01",
            "of shrimp.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C43")

    label("loc_C20")


    ChrTalk(
        0xB,
        "Ahhh...it's almost lunchtime.\x02",
    )

    CloseMessageWindow()

    label("loc_C43")

    Jump("loc_FE6")

    label("loc_C46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_DFA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D5A")
    OP_A2(0x0)

    ChrTalk(
        0xB,
        "I heard about it from Jean...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Someone from the royal\x01",
            "family is apparently\x01",
            "here, in Ruan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If he shares the same bloodline\x01",
            "as Queen Alicia, I'll bet he's\x01",
            "really refined and dignified.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I guess he's coming to just\x01",
            "make his presence known.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DF7")

    label("loc_D5A")


    ChrTalk(
        0xB,
        (
            "Someone from the royal family\x01",
            "came to Ruan yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If he shares the same bloodline\x01",
            "as Queen Alicia, I'll bet he's\x01",
            "really refined and dignified.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DF7")

    Jump("loc_FE6")

    label("loc_DFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_END)), "loc_E7B")

    ChrTalk(
        0xB,
        (
            "Have you seen the Langland\x01",
            "Bridge yet? It's definitely\x01",
            "worth checking out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "It's the real symbol of the city.\x02",
    )

    CloseMessageWindow()
    Jump("loc_FE6")

    label("loc_E7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_FE6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F5D")
    OP_A2(0x0)

    ChrTalk(
        0xB,
        "We've got a lot of tourists today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "They don't have reservations\x01",
            "for the hotel, though, I hear.\x01",
            "And that place is booked solid!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I think the Bracer Guild office\x01",
            "is opening up to take them in.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FE6")

    label("loc_F5D")


    ChrTalk(
        0xB,
        "We've got a lot of tourists today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "They don't have reservations\x01",
            "for the hotel, though, I hear.\x01",
            "And that place is booked solid!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FE6")

    TalkEnd(0xB)
    Return()

    # Function_4_631 end

    def Function_5_FEA(): pass

    label("Function_5_FEA")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x67)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x22, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FFF")
    EventBegin(0x0)

    label("loc_FFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1064")

    ChrTalk(
        0xFE,
        "Thanks for all you've done today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope I can count on you if\x01",
            "I need you again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C5D")

    label("loc_1064")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_148A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x22, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1116")

    ChrTalk(
        0xFE,
        "You were a great help.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I should be able to handle\x01",
            "things from here on out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I need to get back to Zeiss soon,\x01",
            "so I've got to finish up my work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1487")

    label("loc_1116")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x22, 0x0, 0x4)"), scpexpr(EXPR_END)), "loc_11FF")

    ChrTalk(
        0xFE,
        (
            "If you find any orbal-powered guns\x01",
            "around the Aurian Causeway,\x01",
            "bring them back to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've lost a prototype, and you\x01",
            "might run across it there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm planning to go back to Zeiss\x01",
            "very soon. Please, hurry...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1487")

    label("loc_11FF")


    ChrTalk(
        0xFE,
        (
            "I came here from Zeiss to\x01",
            "do market research into\x01",
            "orbal-powered firearms.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The Aurian Causeway is crawling with\x01",
            "some extremely aggressive monsters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And along the way, I lost an extremely\x01",
            "important prototype model while fleeing\x01",
            "from some of them.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x22, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_13C7")
    OP_28(0x22, 0x4, 0x8)
    OP_28(0x22, 0x4, 0x4)
    OP_28(0x22, 0x1, 0x1)
    OP_28(0x22, 0x1, 0x2)

    ChrTalk(
        0x101,
        (
            "#000FOh, I saw the bulletin board.\x02\x03",
            "So what you lost is this orbal\x01",
            "gun thingy?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        "Yes, that's correct.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you should find it,\x01",
            "I beg of you...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1487")

    label("loc_13C7")

    OP_28(0x22, 0x4, 0x8)
    OP_28(0x22, 0x4, 0x4)
    OP_28(0x22, 0x4, 0x2)
    OP_28(0x22, 0x1, 0x1)
    OP_28(0x22, 0x1, 0x2)

    ChrTalk(
        0x101,
        "#002FDid you contact the Bracer Guild?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        "Yes, they performed a search.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I put the notice up on the board,\x01",
            "in hopes that it might be found\x01",
            "sooner.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1487")

    Jump("loc_1C5D")

    label("loc_148A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_189D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x22, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_151F")

    ChrTalk(
        0xFE,
        "You were a great help.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I should be able to handle\x01",
            "things from here on out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now, then...I simply must get\x01",
            "to work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_189A")

    label("loc_151F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x22, 0x0, 0x4)"), scpexpr(EXPR_END)), "loc_1612")

    ChrTalk(
        0xFE,
        (
            "If you find any orbal-powered guns\x01",
            "around the Aurian Causeway,\x01",
            "bring them back to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've lost a prototype, and you\x01",
            "might run across it there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now, then...returning to the\x01",
            "topic at hand, I simply must\x01",
            "get to work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_189A")

    label("loc_1612")


    ChrTalk(
        0xFE,
        (
            "I came here from Zeiss to\x01",
            "do market research into\x01",
            "orbal-powered firearms.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The Aurian Causeway is crawling with\x01",
            "some extremely aggressive monsters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And along the way, I lost an extremely\x01",
            "important prototype model while fleeing\x01",
            "from some of them.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x22, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_17DA")
    OP_28(0x22, 0x4, 0x8)
    OP_28(0x22, 0x4, 0x4)
    OP_28(0x22, 0x1, 0x1)
    OP_28(0x22, 0x1, 0x2)

    ChrTalk(
        0x101,
        (
            "#000FOh, I saw the bulletin board.\x02\x03",
            "So what you lost is this orbal\x01",
            "gun thingy?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        "Yes, that's correct.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you should find it,\x01",
            "I beg of you...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_189A")

    label("loc_17DA")

    OP_28(0x22, 0x4, 0x8)
    OP_28(0x22, 0x4, 0x4)
    OP_28(0x22, 0x4, 0x2)
    OP_28(0x22, 0x1, 0x1)
    OP_28(0x22, 0x1, 0x2)

    ChrTalk(
        0x101,
        "#002FDid you contact the Bracer Guild?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        "Yes, they performed a search.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I put the notice up on the board,\x01",
            "in hopes that it might be found\x01",
            "sooner.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_189A")

    Jump("loc_1C5D")

    label("loc_189D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 6)), scpexpr(EXPR_END)), "loc_1C5D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x22, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1937")

    ChrTalk(
        0xFE,
        "You were a great help.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I should be able to handle\x01",
            "things from here on out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please let me know of any\x01",
            "new developments.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C5D")

    label("loc_1937")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x22, 0x0, 0x4)"), scpexpr(EXPR_END)), "loc_19DE")

    ChrTalk(
        0xFE,
        (
            "If you find any orbal-powered guns\x01",
            "around the Aurian Causeway,\x01",
            "bring them back to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've lost a prototype, and you\x01",
            "might run across it there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C5D")

    label("loc_19DE")


    ChrTalk(
        0xFE,
        (
            "I came here from Zeiss to\x01",
            "do market research into\x01",
            "orbal-powered firearms.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The Aurian Causeway is crawling with\x01",
            "some extremely aggressive monsters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I have an extremely important\x01",
            "prototype model that I was\x01",
            "trying to work the bugs out of.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x22, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_1B9D")
    OP_28(0x22, 0x4, 0x8)
    OP_28(0x22, 0x4, 0x4)
    OP_28(0x22, 0x1, 0x1)
    OP_28(0x22, 0x1, 0x2)

    ChrTalk(
        0x101,
        (
            "#000FOh, I saw the bulletin board.\x02\x03",
            "So what you lost is this orbal\x01",
            "gun thingy?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        "Yes, that's correct.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you should find it,\x01",
            "I beg of you...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C5D")

    label("loc_1B9D")

    OP_28(0x22, 0x4, 0x8)
    OP_28(0x22, 0x4, 0x4)
    OP_28(0x22, 0x4, 0x2)
    OP_28(0x22, 0x1, 0x1)
    OP_28(0x22, 0x1, 0x2)

    ChrTalk(
        0x101,
        "#002FDid you contact the Bracer Guild?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        "Yes, they performed a search.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I put the notice up on the board,\x01",
            "in hopes that it might be found\x01",
            "sooner.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C5D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x67)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x22, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C71")
    Call(1, 4)

    label("loc_1C71")

    TalkEnd(0xC)
    Return()

    # Function_5_FEA end

    def Function_6_1C75(): pass

    label("Function_6_1C75")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_1D0E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CF5")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        "*huff...* *puff...*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "T-Trying to run all the way\x01",
            "from Manoria without a break\x01",
            "is exhausting...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D0E")

    label("loc_1CF5")


    ChrTalk(
        0xFE,
        "*huff...* *puff...*\x02",
    )

    CloseMessageWindow()

    label("loc_1D0E")

    TalkEnd(0xD)
    Return()

    # Function_6_1C75 end

    def Function_7_1D12(): pass

    label("Function_7_1D12")

    Call(0, 8)
    Return()

    # Function_7_1D12 end

    def Function_8_1D17(): pass

    label("Function_8_1D17")

    TalkBegin(0xE)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",       # 0
            "Shop\x01",       # 1
            "Leave\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D83")
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 4)), scpexpr(EXPR_END)), "loc_1D78")
    OP_A9(0x32)
    Jump("loc_1D7A")

    label("loc_1D78")

    OP_A9(0x1F)

    label("loc_1D7A")

    OP_56(0x0)
    TalkEnd(0xE)
    Return()

    label("loc_1D83")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D94")
    TalkEnd(0xE)
    Return()

    label("loc_1D94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1E29")

    ChrTalk(
        0xE,
        "Hmmm...Mayor Dalmore...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "He always was one to put on airs,\x01",
            "but never in a million years did\x01",
            "I think he'd put 'em on that THICK...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27E2")

    label("loc_1E29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_1FE5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F3B")
    OP_A2(0x3)

    ChrTalk(
        0xE,
        (
            "I heard someone talking,\x01",
            "and it was some weird guy\x01",
            "with really strange hair.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "He looked like he had plenty\x01",
            "of mira, but he was really\x01",
            "self-important and rude.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Definitely didn't measure up\x01",
            "to your average Ruanian man.\x01",
            "He MUST be a tourist.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FE2")

    label("loc_1F3B")


    ChrTalk(
        0xE,
        (
            "I heard someone talking,\x01",
            "and it was some weird guy\x01",
            "with really strange hair.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Definitely didn't measure up\x01",
            "to your average Ruanian man.\x01",
            "He MUST be a tourist.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FE2")

    Jump("loc_27E2")

    label("loc_1FE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_2186")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2145")
    OP_A2(0x3)

    ChrTalk(
        0xE,
        (
            "I had a good time at my little\x01",
            "sister's campus festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I don't think she really wanted me\x01",
            "to come checking on her, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Ha ha...what kind of big sister\x01",
            "would I be if I didn't look out\x01",
            "for her, now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "*phew* I really cleaned up at the game\x01",
            "stalls. Just what am I going to do with\x01",
            "all these Pom plushies I won?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2183")

    label("loc_2145")


    ChrTalk(
        0xE,
        (
            "I had a good time at my little\x01",
            "sister's campus festival.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2183")

    Jump("loc_27E2")

    label("loc_2186")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_2219")

    ChrTalk(
        0xE,
        (
            "Ha ha...it's almost time for\x01",
            "the campus festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "My little sister is in the play,\x01",
            "but I have no idea what role\x01",
            "she's playing.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27E2")

    label("loc_2219")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_248B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_239B")
    OP_A2(0x3)

    ChrTalk(
        0xE,
        (
            "I've been told that the Royal\x01",
            "Army performed admirably in\x01",
            "the Hundred Days War...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "...but it was one particular colonel\x01",
            "who really made the difference in\x01",
            "driving off the Imperial forces.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Still, I haven't heard a peep about where\x01",
            "he is or what he's done since the war ended.\x01",
            "People just stopped talking about him!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Ha ha...I wonder what he's like.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2488")

    label("loc_239B")


    ChrTalk(
        0xE,
        (
            "It was supposedly one particular\x01",
            "colonel who made the difference in\x01",
            "driving off the Imperial forces.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Still, I haven't heard a peep about where\x01",
            "he is or what he's done since the war ended.\x01",
            "People just stopped talking about him!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2488")

    Jump("loc_27E2")

    label("loc_248B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_2509")

    ChrTalk(
        0xE,
        (
            "Ha ha... Can you believe I've been\x01",
            "here for ten years already?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "The years certainly do creep\x01",
            "up on you...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27E2")

    label("loc_2509")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_END)), "loc_26D6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2634")
    OP_A2(0x3)

    ChrTalk(
        0xE,
        (
            "Ha ha...the bracers certainly\x01",
            "are impressive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Having that level of authority\x01",
            "must be a heavy burden\x01",
            "to bear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I'm sure one has to be trustworthy\x01",
            "to be a bracer...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "...but at the same time, I imagine\x01",
            "that someone like that has to be\x01",
            "pretty critical of oneself.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26D3")

    label("loc_2634")


    ChrTalk(
        0xE,
        (
            "I'm sure one has to be trustworthy\x01",
            "to be a bracer...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "...but at the same time, I imagine\x01",
            "that someone like that has to be\x01",
            "pretty critical of oneself.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26D3")

    Jump("loc_27E2")

    label("loc_26D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_27E2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27B0")
    OP_A2(0x3)

    ChrTalk(
        0xE,
        (
            "Oh, hello.\x01",
            "What a cute little bracer!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "...or rather, a bracer-in-training,\x01",
            "if I recognize that crest correctly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000FWow! You sure know your stuff.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Ha ha... I know a few things.\x02",
    )

    CloseMessageWindow()
    Jump("loc_27E2")

    label("loc_27B0")


    ChrTalk(
        0xE,
        (
            "Welcome, my cute little bracer-\x01",
            "in-training.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27E2")

    TalkEnd(0xE)
    Return()

    # Function_8_1D17 end

    def Function_9_27E6(): pass

    label("Function_9_27E6")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_END)), "loc_284A")

    ChrTalk(
        0xFE,
        "The break from classes ends today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I have to get ready for\x01",
            "lessons tomorrow.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A74")

    label("loc_284A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_2A74")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A17")
    OP_A2(0x4)
    TurnDirection(0xFE, 0x136, 0)

    ChrTalk(
        0xFE,
        (
            "Oh hi, Kloe. What brings you\x01",
            "to town?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        "#040FI'm just showing my friends around.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F(Hey, she's got the same school\x01",
            "uniform as Kloe...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F(So she does.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        "#040FI guess you're on your way home?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yeah, there's no club practice\x01",
            "today, so...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, by the way...did you ever\x01",
            "make up your mind about\x01",
            "you-know-what?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        "#045FUm, not yet.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Okay...I hope you do soon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F(What's 'you-know-what'?)\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A74")

    label("loc_2A17")

    TurnDirection(0xFE, 0x136, 0)

    ChrTalk(
        0xFE,
        (
            "Since you took the trouble to\x01",
            "come here, I hope you'll relax\x01",
            "and enjoy yourself.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A74")

    TalkEnd(0xF)
    Return()

    # Function_9_27E6 end

    def Function_10_2A78(): pass

    label("Function_10_2A78")

    TalkBegin(0x8)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",        # 0
            "Report\x01",      # 1
            "Leave\x01",       # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C26")
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_A9(0x22)"), scpexpr(EXPR_END)), "loc_2B77")
    Sleep(200)

    ChrTalk(
        0x8,
        (
            "#650FMuch obliged. You appear to have\x01",
            "achieved your goal without injury.\x02\x03",
            "If you complete any other jobs,\x01",
            "be sure to give me all the juicy\x01",
            "details!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C1D")

    label("loc_2B77")

    Sleep(200)

    ChrTalk(
        0x8,
        (
            "#650FIt doesn't seem that you have\x01",
            "anything noteworthy to report,\x01",
            "at the moment.\x02\x03",
            "If you complete any other jobs,\x01",
            "be sure to give me all the juicy\x01",
            "details!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C1D")

    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_2C26")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C37")
    TalkEnd(0x8)
    Return()

    label("loc_2C37")

    Call(0, 11)
    Return()

    # Function_10_2A78 end

    def Function_11_2C3C(): pass

    label("Function_11_2C3C")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2D63")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D13")
    OP_A2(0x5)

    ChrTalk(
        0x8,
        (
            "#650FAre you planning to go to Zeiss next?\x02\x03",
            "There may be clues about the\x01",
            "Black Orbment there.\x02\x03",
            "#651FIt'll be a real load off our minds\x01",
            "when you two get promoted to\x01",
            "full-fledged bracers.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D60")

    label("loc_2D13")


    ChrTalk(
        0x8,
        (
            "#654FBy the looks of things,\x01",
            "Ruan will be in quite a\x01",
            "state for a while.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D60")

    Jump("loc_3D49")

    label("loc_2D63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_2DF7")

    ChrTalk(
        0x8,
        (
            "#652FDo you understand? You need\x01",
            "to buy some time.\x02\x03",
            "Until the Royal Army shows up,\x01",
            "you are to keep Mayor Dalmore\x01",
            "under house arrest.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D49")

    label("loc_2DF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_304C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F7C")
    OP_A2(0x5)

    ChrTalk(
        0x8,
        (
            "#653FAhh, hello...the director has\x01",
            "already filled me in.\x02\x03",
            "#652FMelvin has left on assignment,\x01",
            "but unfortunately, Agate hasn't\x01",
            "reported in yet.\x02\x03",
            "I know you just finished up your business\x01",
            "at the Academy, but I need you to go\x01",
            "to Manoria as quickly as possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002FSure thing! You don't have to\x01",
            "persuade us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012FWe should hurry.\x01",
            "I'm worried about Carna.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3049")

    label("loc_2F7C")


    ChrTalk(
        0x8,
        (
            "#652FMelvin has left on assignment,\x01",
            "but unfortunately, Agate hasn't\x01",
            "reported in yet.\x02\x03",
            "I know you just finished up your business\x01",
            "at the Academy, but I need you to go\x01",
            "to Manoria as quickly as possible.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3049")

    Jump("loc_3D49")

    label("loc_304C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_3221")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3156")
    OP_A2(0x5)

    ChrTalk(
        0x8,
        (
            "#650FYou're to be commended for your \x01",
            "assistance to the civilians and\x01",
            "general contributions to the area.\x02\x03",
            "I can honestly say, this is the\x01",
            "first time someone's been sent\x01",
            "to participate in a play.\x02\x03",
            "#651FWell, I'll be waiting for your report.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_321E")

    label("loc_3156")


    ChrTalk(
        0x8,
        (
            "#650FYou're to be commended for your \x01",
            "assistance to the civilians and\x01",
            "general contributions to the area.\x02\x03",
            "I can honestly say, this is the\x01",
            "first time someone's been sent\x01",
            "to participate in a play.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_321E")

    Jump("loc_3D49")

    label("loc_3221")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_33BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3359")
    OP_A2(0x5)

    ChrTalk(
        0x8,
        (
            "#653FHello, you two. How is everyone\x01",
            "at the orphanage?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002FOh...uh...well, we finished\x01",
            "our investigation...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012FThere has been some trouble,\x01",
            "though.\x02\x03",
            "#010FWe'll have more information\x01",
            "for you later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#652FYou look like you're in a hurry.\x01",
            "Go. I'll take your report later.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33BA")

    label("loc_3359")


    ChrTalk(
        0x8,
        (
            "#652FIf anything major happens,\x01",
            "please report in.\x02\x03",
            "In the meantime, shouldn't\x01",
            "you be going?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33BA")

    Jump("loc_3D49")

    label("loc_33BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 6)), scpexpr(EXPR_END)), "loc_3481")

    ChrTalk(
        0x8,
        (
            "#652FI can't confirm the whereabouts, nor\x01",
            "the safety of the matron or the\x01",
            "children, I'm afraid.\x02\x03",
            "I'd like for you to make a full\x01",
            "investigation, including finding\x01",
            "out those details.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D49")

    label("loc_3481")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_3C4E")
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, -3490, 0, 45210, 270)
    SetChrPos(0x102, -3520, 0, 44250, 270)
    OP_6D(-5640, 0, 45060, 0)
    OP_8C(0x8, 90, 0)
    OP_4A(0x8, 255)
    OP_0D()

    ChrTalk(
        0x101,
        "#001FGood morning, Jean!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FGood morning.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#650FGood morning.\x01",
            "You're certainly here early.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006FYep, just like we promised.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FI know it's early, but do you\x01",
            "have any assignments for us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#651FAh, music to my ears!\x02\x03",
            "Let's see...\x01",
            "There are so many options...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#008FG-Go easy on us...\x02",
    )

    CloseMessageWindow()
    LoadEffect(0x0, "map\\\\mp001_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, -6670, 1900, 46840, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xC3, 0x0, 0x64)
    Sleep(500)
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#653FOh...hold on just a moment,\x01",
            "please.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 0, 400)

    def lambda_36B1():

        label("loc_36B1")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_36B1")

    QueueWorkItem2(0x101, 2, lambda_36B1)

    def lambda_36C2():

        label("loc_36C2")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_36C2")

    QueueWorkItem2(0x102, 2, lambda_36C2)

    def lambda_36D3():
        OP_6D(-5530, 0, 45850, 1200)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_36D3)
    OP_8E(0x8, 0xFFFFE8A4, 0x0, 0xB6B2, 0xBB8, 0x0)
    OP_8C(0x8, 270, 400)
    Sleep(500)
    LoadEffect(0x1, "map\\\\mp001_01.eff")
    PlayEffect(0x1, 0x0, 0xFF, -6670, 1900, 46840, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x83, 0x0, 0x64)
    OP_23(0xC3)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#650FHello, you've reached the\x01",
            "Bracer Guild.\x02\x03",
            "Oh, it's an incoming communication\x01",
            "from The White Magnolia...\x01",
            "How unusual.\x02\x03",
            "I'm impressed you were able to\x01",
            "reach us with that old comm\x01",
            "equipment...\x02\x03",
            "#653F...\x02\x03",
            "#652F...What did you say?\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1500)

    ChrTalk(
        0x8,
        (
            "#652FI see... That's definitely a\x01",
            "major issue.\x02\x03",
            "Yes, I understand. I'll send\x01",
            "someone over shortly.\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x83, 0x0, 0x64)
    OP_82(0x0, 0x0)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#002FWhat's wrong?\x01",
            "Another case?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0x8,
        (
            "#652FIt could be a case, or just an\x01",
            "accident. I'm not sure...\x02\x03",
            "Last night, the orphanage on\x01",
            "the coastal road caught fire\x01",
            "and burned down.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_1D(0x56)

    ChrTalk(
        0x101,
        "#004FN-No way...!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012FAny idea who might have\x01",
            "done it?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3A2E():
        OP_6D(-5640, 0, 45060, 1200)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_3A2E)
    OP_8E(0x8, 0xFFFFE9BC, 0x0, 0xB02C, 0xBB8, 0x0)
    OP_8C(0x8, 90, 400)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)

    ChrTalk(
        0x8,
        (
            "#652FThat was the proprietor of the\x01",
            "Manoria Inn who called.\x02\x03",
            "Are you two familiar with the\x01",
            "Mercia Orphanage?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#003FFamiliar...? We were there just\x01",
            "yesterday afternoon!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012FAre the kids and the matron\x01",
            "okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#652FThat I don't know.\x02\x03",
            "We have to conduct a full\x01",
            "investigation, and it has to\x01",
            "be as thorough as possible.\x02\x03",
            "Would you be willing...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#005FOf course we would!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012FLet's head over there now,\x01",
            "then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#652FGood, good. Take care!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x9)
    OP_A2(0x41E)
    OP_28(0x3B, 0x4, 0x2)
    OP_28(0x3B, 0x4, 0x4)
    EventEnd(0x0)
    OP_4B(0x8, 255)
    Jump("loc_3D49")

    label("loc_3C4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_END)), "loc_3D49")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CF3")
    OP_A2(0x5)

    ChrTalk(
        0x8,
        (
            "#650FWow...am I ever relieved to\x01",
            "see you at a time like this.\x02\x03",
            "Your work tomorrow is going\x01",
            "to require extreme dedication.\x02\x03",
            "#651FThank you!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D49")

    label("loc_3CF3")


    ChrTalk(
        0x8,
        (
            "#650FYour work tomorrow is going\x01",
            "to require extreme dedication.\x02\x03",
            "#651FThank you!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D49")

    TalkEnd(0x8)
    Return()

    # Function_11_2C3C end

    def Function_12_3D4D(): pass

    label("Function_12_3D4D")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3F4F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EBB")
    OP_A2(0x6)

    ChrTalk(
        0xFE,
        "#831FOh, hey, you guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001FCarna...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FAre you feeling better?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#830FFit as a fiddle. I'm back at work,\x01",
            "as of today.\x02\x03",
            "#835FI wish I had some way to pay\x01",
            "you back for all the trouble\x01",
            "I put you through.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#008FOh, come on...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#830FOnce you become full-fledged\x01",
            "bracers, come back to Ruan.\x02\x03",
            "I'll be waiting for you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F4C")

    label("loc_3EBB")


    ChrTalk(
        0xFE,
        (
            "#830FI wish I had some way to pay\x01",
            "you back for all the trouble\x01",
            "I put you through.\x02\x03",
            "Once you become full-fledged\x01",
            "bracers, come back to Ruan.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F4C")

    Jump("loc_43E3")

    label("loc_3F4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_404F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FE8")
    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "#830FI heard what you said to Jean.\x02\x03",
            "I'm going to be working as\x01",
            "security for the campus\x01",
            "festival, myself.\x02\x03",
            "I'll see you there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_404C")

    label("loc_3FE8")


    ChrTalk(
        0xFE,
        (
            "#830FI'm going to be working as\x01",
            "security for the campus\x01",
            "festival, myself.\x02\x03",
            "I'll see you there.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_404C")

    Jump("loc_43E3")

    label("loc_404F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_41DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4139")
    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "#835FRuan's seen a lot of tourists\x01",
            "coming through, lately.\x02\x03",
            "It's been keeping me super-busy with\x01",
            "guard jobs, not to mention searching\x01",
            "for lost property.\x02\x03",
            "I could really use your help\x01",
            "dealing with this stuff.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41D7")

    label("loc_4139")


    ChrTalk(
        0xFE,
        (
            "#835FRuan's seen a lot of tourists\x01",
            "coming through, lately.\x02\x03",
            "It's been keeping me super-busy with\x01",
            "guard jobs, not to mention searching\x01",
            "for lost property.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41D7")

    Jump("loc_43E3")

    label("loc_41DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_END)), "loc_435E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42E3")
    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "#831FYou done changing assignments?\x01",
            "Guess that makes us partners\x01",
            "for a while.\x02\x03",
            "We've only got one other bracer-\x01",
            "in-training at this branch.\x02\x03",
            "#833FAnd now you guys are here\x01",
            "for a little while...\x02\x03",
            "...\x02\x03",
            "#830F...I appreciate the help. Really.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_435B")

    label("loc_42E3")


    ChrTalk(
        0xFE,
        (
            "#830FWe've only got one other bracer-\x01",
            "in-training at this branch.\x02\x03",
            "And now you guys are here\x01",
            "for a little while...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_435B")

    Jump("loc_43E3")

    label("loc_435E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_43E3")

    ChrTalk(
        0xFE,
        (
            "#830FYou won't be able to switch\x01",
            "assignments until Jean\x01",
            "gets back.\x02\x03",
            "Why not go sightseeing to\x01",
            "kill some time until then?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43E3")

    TalkEnd(0x9)
    Return()

    # Function_12_3D4D end

    def Function_13_43E7(): pass

    label("Function_13_43E7")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_443F")

    ChrTalk(
        0xFE,
        (
            "The mayor's been arrested...\x01",
            "I just don't...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "What's going on...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_475F")

    label("loc_443F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_44CF")

    ChrTalk(
        0xFE,
        (
            "Carna was on assignment as\x01",
            "security for that festival, but\x01",
            "she hasn't come back yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe she's still busy\x01",
            "with something?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_475F")

    label("loc_44CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_45B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_457E")
    OP_A2(0x7)

    ChrTalk(
        0xFE,
        (
            "I'll just have to hold out until\x01",
            "she gets back!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Ah...AH-CHOO!\x02",
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "And hopefully I'll shake this\x01",
            "cold in the meantime...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45B3")

    label("loc_457E")


    ChrTalk(
        0xFE,
        (
            "I'll just have to hold out\x01",
            "until she gets back!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45B3")

    Jump("loc_475F")

    label("loc_45B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_END)), "loc_475F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46B4")
    OP_A2(0x7)

    ChrTalk(
        0xFE,
        (
            "So, you're the newbies that\x01",
            "Jean was talking about, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I failed the exam several times\x01",
            "before, but was able to eventually\x01",
            "get bumped up to Junior Bracer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you really want something,\x01",
            "you've just got to keep trying!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_475F")

    label("loc_46B4")


    ChrTalk(
        0xFE,
        (
            "I failed the exam several times\x01",
            "before, but was able to eventually\x01",
            "get bumped up to Junior Bracer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you really want something,\x01",
            "you've just got to keep trying!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_475F")

    TalkEnd(0x10)
    Return()

    # Function_13_43E7 end

    def Function_14_4763(): pass

    label("Function_14_4763")

    Call(0, 15)
    Return()

    # Function_14_4763 end

    def Function_15_4768(): pass

    label("Function_15_4768")

    TalkBegin(0x11)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",       # 0
            "Shop\x01",       # 1
            "Leave\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_47E0")
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x88, 2)), scpexpr(EXPR_END)), "loc_47C9")
    OP_A9(0x2B)
    Jump("loc_47D7")

    label("loc_47C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_47D5")
    OP_A9(0x26)
    Jump("loc_47D7")

    label("loc_47D5")

    OP_A9(0x20)

    label("loc_47D7")

    OP_56(0x0)
    TalkEnd(0x11)
    Return()

    label("loc_47E0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_47F1")
    TalkEnd(0x11)
    Return()

    label("loc_47F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4997")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4925")
    OP_A2(0x8)

    ChrTalk(
        0x11,
        (
            "I'd never have suspected Mayor\x01",
            "Dalmore of such crimes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "The position of mayor in Ruan\x01",
            "has been held by the Dalmores\x01",
            "for generations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "I suspect that one of them\x01",
            "being arrested will be the\x01",
            "end of that little tradition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "For an old man like me, it's\x01",
            "been a genuine shock.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4994")

    label("loc_4925")


    ChrTalk(
        0x11,
        (
            "Goodness me...life certainly\x01",
            "goes through its changes in\x01",
            "the course of one man's life.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "Hah ha ha ha!\x02",
    )

    CloseMessageWindow()

    label("loc_4994")

    Jump("loc_5681")

    label("loc_4997")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_4B83")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4AE7")
    OP_A2(0x8)

    ChrTalk(
        0x11,
        (
            "This continent is a big place...\x01",
            "with a lot of different countries\x01",
            "and people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Perhaps you lot will get\x01",
            "the chance to travel the\x01",
            "land someday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "It's important to spend time\x01",
            "with different cultures and\x01",
            "learn about them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "That is, if you want to be a\x01",
            "well-rounded adult, like me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "Hah ha ha ha!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4B80")

    label("loc_4AE7")


    ChrTalk(
        0x11,
        (
            "This continent is a big place...\x01",
            "with a lot of different countries\x01",
            "and people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Perhaps you lot will get\x01",
            "the chance to travel the\x01",
            "land someday.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B80")

    Jump("loc_5681")

    label("loc_4B83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_4D3E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CA4")
    OP_A2(0x8)

    ChrTalk(
        0x11,
        (
            "Even now, my sailor's blood\x01",
            "still stirs whenever I get a\x01",
            "look at the ocean.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "But nowadays, all the ships\x01",
            "seem to be orbment-powered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "I'm sure it makes everything\x01",
            "easier, but where's the effort...?\x01",
            "Where's the passion?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "Hmph...maybe I'm just too old.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4D3B")

    label("loc_4CA4")


    ChrTalk(
        0x11,
        (
            "But nowadays, all the ships\x01",
            "seem to be orbment-powered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "I'm sure it makes everything\x01",
            "easier, but where's the effort...?\x01",
            "Where's the passion?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D3B")

    Jump("loc_5681")

    label("loc_4D3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_4F04")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4EC3")
    OP_A2(0x8)

    ChrTalk(
        0x11,
        (
            "The Erebonian Empire used to be a much\x01",
            "smaller country than it is today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "After all the repeated attacks, the\x01",
            "different nations and peoples basically\x01",
            "merged into one large nation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Still, the Imperial family has\x01",
            "absolute control internally,\x01",
            "just as they always have.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "I passed through that area before,\x01",
            "and things got pretty tense.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "Hah ha ha ha!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4F01")

    label("loc_4EC3")


    ChrTalk(
        0x11,
        (
            "What, you want to hear more of\x01",
            "my old adventure stories?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F01")

    Jump("loc_5681")

    label("loc_4F04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_5199")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5158")
    OP_A2(0x8)

    ChrTalk(
        0x11,
        (
            "How about the time when\x01",
            "I was sailing through\x01",
            "Republican waters?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "This was before their political\x01",
            "climate had settled down, so\x01",
            "there was no real public order.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Anyway, we were suddenly attacked\x01",
            "by some pirates in a passenger ship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "But since I was a man of the sea,\x01",
            "it was the pirates that were in trouble!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "With them getting closer,\x01",
            "I knew that hesitating\x01",
            "would spell disaster...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "And after a scuffle, I eventually bested them and\x01",
            "spent my victory bathing in the adoration of some\x01",
            "exotic Eastern women...my, but they were lovely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "Hah ha ha ha!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5196")

    label("loc_5158")


    ChrTalk(
        0x11,
        (
            "What, you want to hear more\x01",
            "of my old adventure stories?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5196")

    Jump("loc_5681")

    label("loc_5199")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_5398")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5301")
    OP_A2(0x8)

    ChrTalk(
        0x11,
        (
            "There are quite a few other countries, both\x01",
            "large and small, on this continent, aside\x01",
            "from Liberl, Erebonia, and Calvard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Far to the east of these nations\x01",
            "the entire culture is very different.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "That's why the Republic is made\x01",
            "up of so many different cultures.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Back when I was younger, I\x01",
            "sailed all over those countries.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5395")

    label("loc_5301")


    ChrTalk(
        0x11,
        (
            "Far to the east of these nations,\x01",
            "the entire culture is very different.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "That's why the Republic is made\x01",
            "up of so many different cultures.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5395")

    Jump("loc_5681")

    label("loc_5398")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_END)), "loc_5566")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_54DE")
    OP_A2(0x8)

    ChrTalk(
        0x11,
        (
            "As you can probably see,\x01",
            "I was quite the sailor in\x01",
            "my younger days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "I've sailed from one corner of\x01",
            "the continent to another, in\x01",
            "search of rare and exotic things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Long ago, I was fairly well known\x01",
            "as Captain O'Neil.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Well, sit right back and you'll hear\x01",
            "a tale. A tale of my adventures.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5563")

    label("loc_54DE")


    ChrTalk(
        0x11,
        (
            "Long ago, I was fairly well known\x01",
            "as Captain O'Neil.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Well, sit right back and you'll hear\x01",
            "a tale. A tale of my adventures.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5563")

    Jump("loc_5681")

    label("loc_5566")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_5681")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5625")
    OP_A2(0x8)

    ChrTalk(
        0x11,
        "*ahem*!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "When I was young, nary a mira\x01",
            "to my name, I sailed around\x01",
            "the world on a trading ship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Once upon a time, Ruan was\x01",
            "full of men with the same drive.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5681")

    label("loc_5625")


    ChrTalk(
        0x11,
        (
            "When I was young, nary a mira\x01",
            "to my name, I sailed around\x01",
            "the world on a trading ship.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5681")

    TalkEnd(0x11)
    Return()

    # Function_15_4768 end

    def Function_16_5685(): pass

    label("Function_16_5685")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5707")
    OP_A2(0xA)

    ChrTalk(
        0xFE,
        (
            "He's been like this since\x01",
            "I stepped in here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'd like to eventually get some\x01",
            "actual shopping done...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5773")

    label("loc_5707")


    ChrTalk(
        0xFE,
        (
            "The shopkeeper's been chattering\x01",
            "on constantly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He's been at it ever since we\x01",
            "walked in the door.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5773")

    TalkEnd(0x12)
    Return()

    # Function_16_5685 end

    def Function_17_5777(): pass

    label("Function_17_5777")

    TalkBegin(0x13)

    ChrTalk(
        0xFE,
        (
            "We came all the way here...and I\x01",
            "wasn't planning on just browsing.\x01",
            "I'm here to shop, dammit!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x13)
    Return()

    # Function_17_5777 end

    def Function_18_57E0(): pass

    label("Function_18_57E0")

    TalkBegin(0x16)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_5850")

    ChrTalk(
        0xFE,
        (
            "Hmm...I can't find a really\x01",
            "high-quality map.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe I should ask old\x01",
            "Mr. O'Neil again...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5884")

    label("loc_5850")


    ChrTalk(
        0xFE,
        (
            "Hmmm...maybe there are\x01",
            "just no good maps here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5884")

    TalkEnd(0x16)
    Return()

    # Function_18_57E0 end

    def Function_19_5888(): pass

    label("Function_19_5888")

    EventBegin(0x0)
    OP_6D(-20, 0, 40420, 0)
    OP_6B(2800, 0)
    SetChrFlags(0x8, 0x80)
    SetChrPos(0x101, -170, 0, 40420, 0)
    SetChrPos(0x102, 790, 0, 39400, 0)
    SetChrPos(0x136, -610, 0, 39400, 0)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#000FGood afternoon.\x02",
    )

    CloseMessageWindow()
    OP_6D(-2850, 0, 44550, 1000)

    def lambda_5917():
        OP_8E(0xFE, 0xFFFFF3B2, 0x0, 0xACB2, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5917)

    def lambda_5932():

        label("loc_5932")

        OP_8C(0xFE, 270, 0)
        OP_48()
        Jump("loc_5932")

    QueueWorkItem2(0x101, 1, lambda_5932)
    Sleep(400)

    def lambda_5948():
        OP_8E(0xFE, 0xFFFFF47A, 0x0, 0xA7A8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x136, 2, lambda_5948)

    def lambda_5963():

        label("loc_5963")

        OP_8C(0xFE, 270, 0)
        OP_48()
        Jump("loc_5963")

    QueueWorkItem2(0x136, 1, lambda_5963)
    Sleep(300)

    def lambda_5979():
        OP_8E(0xFE, 0xFFFFF8D0, 0x0, 0xAA78, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5979)

    def lambda_5994():

        label("loc_5994")

        OP_8C(0xFE, 270, 0)
        OP_48()
        Jump("loc_5994")

    QueueWorkItem2(0x102, 1, lambda_5994)
    WaitChrThread(0x102, 0x2)

    ChrTalk(
        0x101,
        "#004FHuh? Where's the receptionist?\x02",
    )

    CloseMessageWindow()
    OP_4A(0x9, 255)
    OP_62(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_8C(0x9, 225, 400)

    ChrTalk(
        0x9,
        (
            "#831FOh, hello there!\x01",
            "Can I help you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501FUm...\x02",
    )

    CloseMessageWindow()
    OP_44(0x101, 0x1)
    OP_44(0x102, 0x1)
    OP_44(0x136, 0x1)

    def lambda_5A3C():

        label("loc_5A3C")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_5A3C")

    QueueWorkItem2(0x101, 1, lambda_5A3C)

    def lambda_5A4D():

        label("loc_5A4D")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_5A4D")

    QueueWorkItem2(0x102, 1, lambda_5A4D)

    def lambda_5A5E():

        label("loc_5A5E")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_5A5E")

    QueueWorkItem2(0x136, 1, lambda_5A5E)
    OP_8E(0x9, 0xFFFFF5EC, 0x0, 0xB0CC, 0x7D0, 0x0)
    OP_8C(0x9, 180, 400)
    OP_44(0x101, 0x1)
    OP_44(0x102, 0x1)
    OP_44(0x136, 0x1)

    ChrTalk(
        0x9,
        (
            "#830FJean is currently in a meeting\x01",
            "with a guest on the second floor.\x02\x03",
            "I'm sorry for the inconvenience,\x01",
            "but is there something I can\x01",
            "help you with?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FUh...well, we're not here as\x01",
            "customers or anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#835FOh, the emblems... I see. So\x01",
            "we're in the same business,\x01",
            "then?\x02\x03",
            "#830FMy name is Carna. I work\x01",
            "here at the Ruan branch.\x02\x03",
            "Are you new in town?\x01",
            "I don't recognize you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006FYep. I'm Estelle, Junior Bracer.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FSame goes for me. I'm Joshua.\x01",
            "It's a pleasure to meet you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#830FEstelle and Joshua...\x02\x03",
            "That's right... You're the new\x01",
            "kids from Rolent, then.\x02\x03",
            "#831FYou two were involved in some\x01",
            "big to-do with Scherazard in\x01",
            "Bose, weren't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008FUm...ha ha... Well, I don't know\x01",
            "if I'd put it quite like that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014FWere you expecting us?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#831FYes, Jean told me about some\x01",
            "promising up-and-comers.\x02\x03",
            "#830FBut I'm afraid you can't change\x01",
            "assignments until he's available.\x02\x03",
            "Why not go sightseeing to\x01",
            "kill some time until then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015FI suppose so. It beats sitting\x01",
            "around and waiting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001FTotally with you!\x02\x03",
            "#501FOh, yeah...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5ECD():
        TurnDirection(0xFE, 0x136, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5ECD)
    Sleep(200)

    def lambda_5EE0():
        TurnDirection(0xFE, 0x136, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5EE0)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#008F#4PUm, would you want to hang\x01",
            "out with us a little longer?\x02\x03",
            "We only just met, and I'd hate\x01",
            "to just part so suddenly...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x136, 0x101, 400)

    ChrTalk(
        0x136,
        (
            "#041FAh...certainly.\x02\x03",
            "#041FSo long as I won't be a bother\x01",
            "or get in your way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F#4PWoohoo!侓\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FThat settles it, then.\x02",
    )

    CloseMessageWindow()

    def lambda_6006():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6006)
    Sleep(200)
    TurnDirection(0x101, 0x9, 400)

    ChrTalk(
        0x102,
        (
            "#010FWe can all go take in the\x01",
            "sights of Ruan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FAnd then we'll come back\x01",
            "in a little bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#831FSure. Have fun!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x9, 90, 400)
    OP_8E(0x9, 0xFFFFFE70, 0x0, 0xB158, 0x7D0, 0x0)
    OP_8C(0x9, 90, 400)
    OP_4B(0x9, 255)
    EventEnd(0x0)
    Return()

    # Function_19_5888 end

    def Function_20_60C5(): pass

    label("Function_20_60C5")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(-3330, 0, 43680, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2830, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x101, -160, 0, 39670, 315)
    SetChrPos(0x102, -100, 0, 40880, 315)
    SetChrPos(0x136, -1250, 0, 39900, 315)
    OP_4A(0x8, 255)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x8, 135, 0)

    ChrTalk(
        0x8,
        (
            "#650FCome on in. Welcome to the\x01",
            "Bracer Guild.\x02\x03",
            "#653FHm? Oh, Miss Rinz!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        "#040FGood afternoon, Jean.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#650FAre you here for another\x01",
            "extermination request?\x02\x03",
            "#651FAhh, I know! Security's being\x01",
            "tightened for the campus festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#045FNo, but I'm sure we'll be here\x01",
            "for that, at some point.\x02\x03",
            "#040FToday, I'm just visiting with\x01",
            "Estelle and Joshua.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#653FOh, I see... So they're civilians, are\x01",
            "they? I suppose I should've known by\x01",
            "the lack of student attire!\x02\x03",
            "Wait... Those emblems...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6361():
        OP_8E(0xFE, 0xFFFFF222, 0x0, 0xB0FE, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6361)

    def lambda_637C():

        label("loc_637C")

        OP_8C(0xFE, 270, 0)
        OP_48()
        Jump("loc_637C")

    QueueWorkItem2(0x102, 1, lambda_637C)
    Sleep(200)

    def lambda_6392():
        OP_8E(0xFE, 0xFFFFF222, 0x0, 0xACBC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6392)

    def lambda_63AD():

        label("loc_63AD")

        OP_8C(0xFE, 270, 0)
        OP_48()
        Jump("loc_63AD")

    QueueWorkItem2(0x101, 1, lambda_63AD)
    Sleep(800)

    def lambda_63C3():
        OP_6D(-4540, 0, 45010, 2000)
        ExitThread()

    QueueWorkItem(0x136, 3, lambda_63C3)

    def lambda_63DB():
        OP_8E(0xFE, 0xFFFFF1AA, 0x0, 0xA8C0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x136, 2, lambda_63DB)
    Sleep(500)
    OP_8C(0x8, 90, 0)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x136, 0x2)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)

    ChrTalk(
        0x101,
        (
            "#000F#4PPleased to meet you.\x01",
            "I'm Estelle, Junior Bracer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FAnd I'm Joshua.\x01",
            "Also a Junior Bracer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#650FOh, so YOU'RE Estelle and Joshua!\x02\x03",
            "#651FWow... It's so good that\x01",
            "you're here!\x02\x03",
            "We've been waiting for you,\x01",
            "ever since we got word from\x01",
            "the Bose branch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F#4PAh... Old man Lugran must have\x01",
            "sent word of us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FWe'll have to thank him.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#650FMy name is Jean.\x01",
            "I'm the receptionist for the\x01",
            "Ruan branch.\x02\x03",
            "I'll be supervising you two,\x01",
            "as well as providing various\x01",
            "types of support.\x02\x03",
            "It's a pleasure to meet both\x01",
            "of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F#4PThe pleasure's all ours.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FIndeed. It's good to meet you,\x01",
            "sir.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#651FHa ha. I have high hopes for\x01",
            "you two.\x02\x03",
            "After all, you were the ones\x01",
            "who so magnificently handled\x01",
            "the Sky Bandit incident.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x136, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x136, 0x101, 400)

    ChrTalk(
        0x136,
        (
            "#044FSky Bandits? You mean that\x01",
            "incident in Bose?\x02\x03",
            "#041FI read about it in the latest\x01",
            "Liberl News.\x02\x03",
            "Did you guys really sort that\x01",
            "whole mess out?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x136, 400)
    TurnDirection(0x102, 0x136, 400)

    ChrTalk(
        0x101,
        (
            "#008F#4PAh ha ha... Well, we just helped\x01",
            "a little.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FIt was the Royal Army that really\x01",
            "did the work of apprehending them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#650FDon't be so modest. Lugran had\x01",
            "nothing but praise for you.\x02\x03",
            "Now, to change your assignment,\x01",
            "I'll need you to sign the\x01",
            "appropriate forms.\x02\x03",
            "Let's go ahead and take\x01",
            "care of that now.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)
    OP_8C(0x102, 270, 400)
    OP_8C(0x136, 315, 400)

    ChrTalk(
        0x101,
        "#004F#4PUm, okay...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FMight as well get it out of\x01",
            "the way...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Estelle and Joshua signed the assignment-change forms.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x8,
        (
            "#651FAll right, the two of you are\x01",
            "now part of the Ruan branch.\x01",
            "Welcome aboard!\x02\x03",
            "We've been so busy...you couldn't\x01",
            "have picked a better time to come.\x02\x03",
            "Ha ha... Now you can't get away.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#007F#4PWhy do I feel like I just signed\x01",
            "my life away...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FIt looks like you're as short-\x01",
            "handed as we heard some time\x01",
            "ago.\x02\x03",
            "Is something in particular\x01",
            "going on?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#654FI wouldn't say that, exactly.\x02\x03",
            "We are expecting a member of\x01",
            "the royal family to visit, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F#4PA member of the royal family...\x01",
            "Hmm...\x02\x03",
            "#001FWhoa. You aren't talking about\x01",
            "the queen, are you?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#650FHa ha, no. Of course not.\x02\x03",
            "I just know that it's someone\x01",
            "of royal blood.\x02\x03",
            "I've heard that he or she will\x01",
            "be giving Ruan a thorough\x01",
            "inspection, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F#4PHuh. That's kinda cool.\x02\x03",
            "But why would that cause\x01",
            "you to be short-staffed?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#650FBecause it's a member of the\x01",
            "royal family.\x02\x03",
            "If even one thing is out of place,\x01",
            "Mayor Dalmore will be worried\x01",
            "sick.\x02\x03",
            "So, most of our staff was\x01",
            "requisitioned to help strengthen\x01",
            "security.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FI get it. That's what was being\x01",
            "discussed upstairs earlier.\x02\x03",
            "Policing the streets, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#654FYes. I feel certain that the\x01",
            "crew at the harbor will be\x01",
            "back in action pretty quickly.\x02\x03",
            "I want this city to be hooligan\x01",
            "free during the royal visit!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009F#4PCrew at the harbor...? You mean\x01",
            "the guys we dealt with earlier?\x02\x03",
            "Hmmm... I had the feeling\x01",
            "they were up to something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#653FWhat? Do you know something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012FActually...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Estelle and Joshua described what had transpired outside the warehouse\x01",
            "district.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x8,
        (
            "#652FAh, yes...the warehouse district.\x02\x03",
            "That's the turf of a rather unsavory\x01",
            "group calling themselves the Ravens.\x02\x03",
            "I imagine you encountered some\x01",
            "young men and their leader there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009F#4PHuh... I wonder what those\x01",
            "'Raven' characters are up to...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#654FThey've been fine until recently.\x01",
            "Whoever's in charge needs to\x01",
            "tighten the leash.\x02\x03",
            "The mayor's main concern, though,\x01",
            "is that we cover the whole area.\x02\x03",
            "#650FAnd that's why we're so\x01",
            "short-staffed right now.\x02\x03",
            "Thank goodness you two\x01",
            "are here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F#4PHa ha... Well, it's nice to\x01",
            "feel wanted.\x02\x03",
            "I guess that means we've got\x01",
            "a lot of helping out to do\x01",
            "tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FIf anything happens, just say\x01",
            "the word and we'll help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#651FI will. Thank you!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T2100   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_20_60C5 end

    def Function_21_732D(): pass

    label("Function_21_732D")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(-1640, 0, 43790, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x102, -690, 0, 39780, 315)
    SetChrPos(0x101, 790, 0, 39400, 315)

    def lambda_7372():

        label("loc_7372")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_7372")

    QueueWorkItem2(0x101, 1, lambda_7372)

    def lambda_7383():

        label("loc_7383")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_7383")

    QueueWorkItem2(0x102, 1, lambda_7383)

    def lambda_7394():
        OP_6D(-5410, 0, 45570, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_7394)

    def lambda_73AC():
        OP_8E(0xFE, 0xFFFFF380, 0x0, 0xB036, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_73AC)
    Sleep(500)

    def lambda_73CC():
        OP_8E(0xFE, 0xFFFFF380, 0x0, 0xABB8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_73CC)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x102, 0x2)

    ChrTalk(
        0x101,
        "#000F#2PGood morning, Jean!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FGood morning.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#650FGood morning.\x01",
            "You're certainly here early.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000FNaturally!仚\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FI know it's early, but do you\x01",
            "have any assignments for us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#650FAh, music to my ears!\x02\x03",
            "Let's see...\x01",
            "There are so many options...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000FG-Go easy on us...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#650FOh...hold on just a moment,\x01",
            "please.\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x8, 0xFFFFE8A4, 0x0, 0xB6B2, 0x7D0, 0x0)
    OP_8C(0x8, 270, 400)

    ChrTalk(
        0x8,
        (
            "#650FHello, you've reached the\x01",
            "Bracer Guild.\x02\x03",
            "Oh, it's an incoming communication\x01",
            "from The White Magnolia...\x01",
            "How unusual.\x02\x03",
            "I'm impressed you were able to\x01",
            "reach us with that old comm\x01",
            "equipment...\x02\x03",
            "...\x02\x03",
            "...What did you say?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#650FI see... That's definitely a\x01",
            "major issue.\x02\x03",
            "Yes, I understand. I'll send\x01",
            "someone over shortly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FWhat's wrong?\x01",
            "Another case?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0x8,
        (
            "#650FIt could be a case, or just an\x01",
            "accident. I'm not sure...\x02\x03",
            "Last night, the orphanage on\x01",
            "the coastal road caught fire\x01",
            "and burned down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000FN-No way...!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FAny idea who might have\x01",
            "done it?\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x8, 0xFFFFE9BC, 0x0, 0xB02C, 0xBB8, 0x0)
    OP_8C(0x8, 90, 800)

    ChrTalk(
        0x8,
        (
            "#650FThat was the proprietor of the\x01",
            "Manoria Inn who called.\x02\x03",
            "Are you two familiar with the\x01",
            "Mercia Orphanage?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FFamiliar...? We were there just\x01",
            "yesterday afternoon!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FAre the kids and the matron\x01",
            "okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#650FThat I don't know.\x02\x03",
            "We have to conduct a full\x01",
            "investigation, and it has to\x01",
            "be as thorough as possible.\x02\x03",
            "Would you be willing...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000FOf course we would!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FLet's head over there now,\x01",
            "then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#650FGood, good. Take care!\x02",
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    EventEnd(0x0)
    Return()

    # Function_21_732D end

    def Function_22_79A7(): pass

    label("Function_22_79A7")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(-4700, 0, 45110, 0)
    OP_6B(2800, 0)
    ClearChrFlags(0x8, 0x80)
    OP_4A(0x8, 255)
    SetChrPos(0x101, -170, 0, 40420, 0)
    SetChrPos(0x102, -610, 0, 39400, 0)
    SetChrPos(0x105, 790, 0, 39400, 0)

    def lambda_7A0A():

        label("loc_7A0A")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_7A0A")

    QueueWorkItem2(0x8, 1, lambda_7A0A)

    def lambda_7A1B():

        label("loc_7A1B")

        OP_8C(0xFE, 270, 0)
        OP_48()
        Jump("loc_7A1B")

    QueueWorkItem2(0x101, 1, lambda_7A1B)

    def lambda_7A2C():

        label("loc_7A2C")

        OP_8C(0xFE, 270, 0)
        OP_48()
        Jump("loc_7A2C")

    QueueWorkItem2(0x102, 1, lambda_7A2C)

    def lambda_7A3D():

        label("loc_7A3D")

        OP_8C(0xFE, 270, 0)
        OP_48()
        Jump("loc_7A3D")

    QueueWorkItem2(0x105, 1, lambda_7A3D)
    FadeToBright(1000, 0)

    def lambda_7A57():
        OP_8E(0xFE, 0xFFFFF2E0, 0x0, 0xB036, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7A57)
    Sleep(400)

    def lambda_7A77():
        OP_8E(0xFE, 0xFFFFF236, 0x0, 0xAAFA, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7A77)
    Sleep(100)

    def lambda_7A97():
        OP_8E(0xFE, 0xFFFFF588, 0x0, 0xACB2, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_7A97)
    WaitChrThread(0x105, 0x2)

    ChrTalk(
        0x8,
        (
            "#651FWelcome back and good work!\x02\x03",
            "I'm told that you were able\x01",
            "to save a young boy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006FYeah...somehow or another.\x02\x03",
            "I'm still kind of in shock from\x01",
            "when that redhead showed up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#650FHa ha, you must mean Agate.\x02\x03",
            "He's working another case\x01",
            "in Ruan.\x02\x03",
            "He used to be the leader of the\x01",
            "Ravens, if you can believe it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F#2PI suspected as much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007FGuess that explains his\x01",
            "terrible disposition...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#655FWell, that was a long time ago.\x02\x03",
            "He drifted into town, right around\x01",
            "when he was your age.\x02\x03",
            "He hung out with a rough crowd and\x01",
            "got into some serious trouble.\x02\x03",
            "#650FCompared to back then, the tough\x01",
            "types nowadays are puppy dogs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004FA-And a guy like that was allowed\x01",
            "to become a bracer?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#651FWell, I've gotten to know\x01",
            "him a little bit...\x02\x03",
            "And it turns out that he wanted\x01",
            "to become a bracer, ever since\x01",
            "he was little.\x02\x03",
            "Sometimes, people just change.\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x6, 0x0, 0x64)
    SetChrPos(0xA, 0, 0, 39060, 0)
    ClearChrFlags(0xA, 0x80)
    Sleep(500)

    ChrTalk(
        0xA,
        (
            "...I think that's probably enough\x01",
            "of the idle chatter.\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x105, 0xFF)

    def lambda_7E94():

        label("loc_7E94")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_7E94")

    QueueWorkItem2(0x8, 1, lambda_7E94)

    def lambda_7EA5():

        label("loc_7EA5")

        TurnDirection(0xFE, 0xA, 400)
        OP_48()
        Jump("loc_7EA5")

    QueueWorkItem2(0x101, 2, lambda_7EA5)

    def lambda_7EB6():

        label("loc_7EB6")

        TurnDirection(0xFE, 0xA, 400)
        OP_48()
        Jump("loc_7EB6")

    QueueWorkItem2(0x102, 2, lambda_7EB6)

    def lambda_7EC7():

        label("loc_7EC7")

        TurnDirection(0xFE, 0xA, 400)
        OP_48()
        Jump("loc_7EC7")

    QueueWorkItem2(0x105, 2, lambda_7EC7)

    def lambda_7ED8():
        OP_6D(-4100, 0, 44500, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7ED8)
    OP_8E(0xA, 0xFFFFF57E, 0x0, 0xA62C, 0xBB8, 0x0)

    ChrTalk(
        0x101,
        "#004FOh, you're back.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#057FDidn't your mama ever tell you\x01",
            "it ain't nice to talk about\x01",
            "someone behind his back?\x02\x03",
            "Always with the gossip...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#651FHa ha. But is it really gossip\x01",
            "if it's positive?\x02\x03",
            "#650FAnyway, are you done with\x01",
            "your investigation?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#053FYep, over and done with.\x02\x03",
            "I can't say for sure...but\x01",
            "I think they're clean.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009FReally...?\x02\x03",
            "You're not just trying to protect\x01",
            "your old buddies?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)

    ChrTalk(
        0xA,
        (
            "#050FYou wanna watch that mouth\x01",
            "of yours?\x02\x03",
            "From what I saw last night\x01",
            "at the sailors' tavern...\x02\x03",
            "They couldn't be the arsonists... Hell,\x01",
            "I doubt they could've even walked a\x01",
            "straight line if they wanted to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#003FHmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#6PWell, if that's true, we can\x01",
            "hold off on them.\x02\x03",
            "#015FThey didn't strike me as the\x01",
            "types with the guts to try\x01",
            "arson, anyway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007FI guess not... Just full of\x01",
            "themselves, mostly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#053FAll you need is to give 'em a\x01",
            "nasty look, and believe me,\x01",
            "they'll cave.\x02\x03",
            "Anyway, I'll see if I can find\x01",
            "the arsonists while I'm out\x01",
            "in the field.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004FHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#050FI'm taking over the case...\x02\x03",
            "...and you're off it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#005FWhoa, say what?!\x02\x03",
            "You've got to be kidding me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F#6PCan you at least give us an\x01",
            "explanation?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#057FOh, don't get your panties in\x01",
            "a wad. You two are too close\x01",
            "to this case and you know it.\x02\x03",
            "And if you let your feelings run\x01",
            "away with you, it screws with your\x01",
            "judgment.\x02\x03",
            "Plus you let a civie get involved...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#043FOh...\x02\x03",
            "#049FPardon me, but I...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#051FYou ain't gotta apologize. It's \x01",
            "these two I'm worried about.\x02\x03",
            "The point is, you gotta be professional\x01",
            "about it. And these two ain't.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#005FJust where do YOU get off,\x01",
            "calling US unprofessional?!\x02\x03",
            "And no matter what you say, we\x01",
            "made a promise to the mayor!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x8, 400)

    ChrTalk(
        0xA,
        (
            "#051FHey, Jean.\x02\x03",
            "What do the rules say about when\x01",
            "junior and senior bracers want\x01",
            "the same case?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#654FOh, come on. You know as\x01",
            "well as I do...\x02\x03",
            "Of course it rules in favor of\x01",
            "the senior bracer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#009F*gulp*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F#6PWe're not bad in a fight...\x02\x03",
            "Perhaps we could provide\x01",
            "backup...?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)

    ChrTalk(
        0xA,
        (
            "#050FIt's just an investigation.\x01",
            "I don't need more people.\x02\x03",
            "I think we're done here. Try\x01",
            "not to hold this against me.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xA, 135, 400)
    OP_8E(0xA, 0x0, 0x0, 0x9894, 0xBB8, 0x0)
    OP_22(0x7, 0x0, 0x64)
    SetChrFlags(0xA, 0x80)

    def lambda_8797():
        OP_6D(-4700, 0, 45110, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8797)
    WaitChrThread(0x101, 0x1)

    ChrTalk(
        0x101,
        (
            "#009F#4PWhat... He... I...\x02\x03",
            "#005FJust who the hell does he\x01",
            "think he is?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F#5PIt's frustrating, sure,\x01",
            "but he has a point.\x02\x03",
            "It just irritates me that we really\x01",
            "don't have a counter-argument.\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x105, 0xFF)
    TurnDirection(0x105, 0x8, 400)

    ChrTalk(
        0x105,
        (
            "#043FI'm sorry...\x01",
            "If I had not drawn my sword...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009F#4PThat's not what's bothering me.\x02\x03",
            "He doesn't have to just blow us\x01",
            "off like that.\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x8, 0x1)
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0x8,
        (
            "#655FPlease, he means no harm.\x01",
            "Don't be upset.\x02\x03",
            "#655FTact is not his strong suit.\x01",
            "He just doesn't know any\x01",
            "other way to communicate.\x02\x03",
            "#652FParticularly in light of the\x01",
            "current situation...\x02\x03",
            "#652FI think it may have something to do\x01",
            "with an earlier case of his. He was\x01",
            "pursuing someone, and well...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8A56():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8A56)

    def lambda_8A64():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8A64)

    def lambda_8A72():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_8A72)
    Sleep(400)

    ChrTalk(
        0x101,
        "#004FHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014FPursuing someone?\x01",
            "Like a criminal?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#652FAh, never mind about that. I really\x01",
            "can't go into detail. Just let him\x01",
            "handle these criminals.\x02\x03",
            "Consider it a personal favor\x01",
            "for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#003FI guess we have no choice...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013FI see...\x02\x03",
            "#015FWell, we'll hand over our report\x01",
            "from our investigation, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#655FPlease, go ahead.\x02",
    )

    CloseMessageWindow()
    OP_28(0x3B, 0x4, 0x10)
    OP_28(0x3C, 0x4, 0x10)
    OP_28(0x3C, 0x4, 0x20)
    Sleep(100)
    OP_AF(0x22, 0x3B)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)

    ChrTalk(
        0x8,
        (
            "#655FIt seems that you were\x01",
            "quite thorough.\x02\x03",
            "#652FBut as I mentioned, the circumstances\x01",
            "of this case are special.\x02\x03",
            "I'm terribly sorry, but you'll have\x01",
            "to end your investigation here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#003FB-But...\x02\x03",
            "We just wanted to do something\x01",
            "for the matron and the kids...\x02\x03",
            "This isn't right...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 0)
    Sleep(300)

    ChrTalk(
        0x102,
        "#013F#1P...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 0)

    ChrTalk(
        0x105,
        (
            "#043FEstelle...\x02\x03",
            "#047F...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x8, 0)
    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#042FUm, Mr. Jean?\x02\x03",
            "It's possible to enlist the help of the Bracer\x01",
            "Guild for civilian events, isn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#650FYes, though it would depend on what kind of\x01",
            "event you're talking about.\x02\x03",
            "Because of the number of people who attend,\x01",
            "we'll be handling security at the royal academy\x01",
            "festival, for example.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040FWell, then...Estelle, Joshua...\x02\x03",
            "Would you mind helping out with\x01",
            "our play, in the meantime?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8F1F():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8F1F)

    def lambda_8F2D():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8F2D)

    ChrTalk(
        0x101,
        "#004F#4PHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F#1PWhat do you mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040FEvery year when the festival\x01",
            "ends, there's a play held in\x01",
            "the auditorium.\x02\x03",
            "I know the children always look\x01",
            "forward to it.\x02\x03",
            "#045FAnd there are still two major\x01",
            "roles that haven't been filled...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F#4PYou don't mean...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F#1P...you want us to take\x01",
            "the parts?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#047FYes...otherwise, we may have\x01",
            "to cancel the play entirely.\x02\x03",
            "I can't bear to think of how\x01",
            "disappointed the children\x01",
            "would be...\x02\x03",
            "#040FSo, I mentioned you two to the\x01",
            "Student Council last night...\x02\x03",
            "They seemed quite eager\x01",
            "to have you.\x02\x03",
            "#041FIt wouldn't be much, but you'd be\x01",
            "reimbursed from the admin budget.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F#4PWh-Why do you want us?\x02\x03",
            "I don't think I'd be any good,\x01",
            "and isn't the play a really big\x01",
            "deal?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040FWell, for the girl part, we need\x01",
            "someone who's been trained for\x01",
            "combat...\x02\x03",
            "I think you'd fit the role perfectly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F#4PI-I see...\x02\x03",
            "Hmm...well, I can definitely do\x01",
            "combat stuff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F#1PSounds like it would work.\x02\x03",
            "#010FAnd what about the other part?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#044FOh...yes, well...\x02\x03",
            "#049FTalking about it is kind of...um...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F#1P'Kind of'...what?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#045F...Embarrassing.\x02",
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#018F#1PA-And what does that mean, exactly?\x01",
            "What kind of play IS this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F#4POh, come on, Joshua. You're not\x01",
            "going to make her say it, are you?\x02\x03",
            "If we can do something for\x01",
            "the kids, where's the harm?\x02\x03",
            "Plus, if we do some work, they'll\x01",
            "probably let us have some of that\x01",
            "awesome festival food!\x02\x03",
            "#001FWe can't let that opportunity\x01",
            "slip by! 噴\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F#1PHey, hold on a second.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x8, 400)
    OP_62(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(
        0x102,
        (
            "#014F#5PJean, is this really a legit\x01",
            "bracer assignment?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_95B1():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_95B1)

    ChrTalk(
        0x8,
        (
            "#651FIt certainly is.\x02\x03",
            "Citizen outreach and regional\x01",
            "services comprise plenty of the\x01",
            "general work that bracers do.\x02\x03",
            "#650FAnd since Agate showed up,\x01",
            "you do have some extra time...\x02\x03",
            "I certainly have no problem\x01",
            "with it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F#4PAll right! 噴\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 0)
    Sleep(400)

    ChrTalk(
        0x102,
        (
            "#017F#1P*sigh* I have a bad feeling\x01",
            "about this.\x02\x03",
            "#017FBut if it's for the kids,\x01",
            "what choice do I have?\x02\x03",
            "#010FStill, if we have anything else\x01",
            "to do, we should take care of\x01",
            "it beforehand.\x02\x03",
            "I doubt working on the play\x01",
            "will leave us free time for\x01",
            "anything else.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#006F#4PHmm...\x01",
            "Yeah, you're probably right.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9803():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9803)

    def lambda_9811():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9811)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#501F#4PHey, Kloe?\x02\x03",
            "Would it be okay with you if we\x01",
            "looked around here some more?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#045FSure. You don't need to worry\x01",
            "about me.\x02\x03",
            "#040FTo get to the Royal Academy...\x02\x03",
            "You leave by the Gull Seaside Way,\x01",
            "go east at the first fork, and then\x01",
            "follow the woodland path.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F#4POkay, got it.\x02\x03",
            "#001FWell then, let's go!\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x3C, 0x1, 0x40)
    OP_28(0x3C, 0x1, 0x80)
    OP_28(0x3D, 0x4, 0x2)
    OP_28(0x3D, 0x4, 0x4)
    OP_28(0x3D, 0x1, 0x1)
    OP_28(0x3D, 0x1, 0x2)
    EventEnd(0x0)
    OP_4B(0x8, 255)
    Return()

    # Function_22_79A7 end

    def Function_23_998D(): pass

    label("Function_23_998D")

    EventBegin(0x0)
    OP_6D(-4840, 0, 45450, 0)
    SetChrPos(0x101, -3350, 0, 45440, 270)
    SetChrPos(0x102, -3440, 0, 44470, 270)
    SetChrPos(0x105, 0, 0, 39060, 0)
    SetChrFlags(0x105, 0x80)
    OP_4A(0x8, 255)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#652F...I understand.\x02\x03",
            "It's just hard to believe that\x01",
            "Mayor Dalmore is behind\x01",
            "these recent events.\x02\x03",
            "Hmm... This is certainly a\x01",
            "major incident...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002FSo, Jean...do you think the\x01",
            "mayor can be caught?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#654FWell... I'm afraid it's going\x01",
            "to be rather difficult.\x02\x03",
            "The only way it'll really happen is\x01",
            "if he can be caught in the act.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#013F#2PI figured as much...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#005FYou can't be serious!\x02\x03",
            "So we just have to allow a corrupt\x01",
            "mayor to stay in power?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#650FNow, now.\x01",
            "There's no need to panic.\x02\x03",
            "The Bracer Guild's hands may\x01",
            "be tied, but the Royal Army\x01",
            "can get him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004FOh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#652FEstelle, Joshua.\x02\x03",
            "I'd like for you to go to the\x01",
            "mayor's estate and question\x01",
            "him.\x02\x03",
            "It doesn't matter if he gets\x01",
            "angry. I just want you to buy\x01",
            "us some time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#2PAnd you'll contact the Royal\x01",
            "Army in the meantime?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#650FHa ha... Precisely.\x02\x03",
            "I'll contact Leiston Fortress HQ\x01",
            "with the orbal communications\x01",
            "system to request assistance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007FI don't like having to rely on\x01",
            "the army, but I don't see any\x01",
            "other option...\x02\x03",
            "#006FOkay, once Kloe catches up to us,\x01",
            "we'll go see the mayor at once.\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_9E7E():
        OP_6D(-4770, 0, 44400, 1000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9E7E)

    def lambda_9E96():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_9E96)

    def lambda_9EA4():

        label("loc_9EA4")

        TurnDirection(0xFE, 0x105, 400)
        OP_48()
        Jump("loc_9EA4")

    QueueWorkItem2(0x101, 1, lambda_9EA4)

    def lambda_9EB5():

        label("loc_9EB5")

        TurnDirection(0xFE, 0x105, 400)
        OP_48()
        Jump("loc_9EB5")

    QueueWorkItem2(0x102, 1, lambda_9EB5)
    ClearChrFlags(0x105, 0x80)
    OP_8E(0x105, 0xFFFFF434, 0x0, 0xA866, 0xBB8, 0x0)
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(
        0x105,
        (
            "#049F#1P...*huff* *huff* I made it!\x02\x03",
            "Sorry for the delay...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F#4PNot at all! Perfect timing,\x01",
            "in fact.侓\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#4PThat was pretty quick for a\x01",
            "run to the campus.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#045F#1PUm, well...\x01",
            "I'm pretty fast on my feet.\x02\x03",
            "#042FSo...what's the plan?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F#4PWe were just talking about\x01",
            "going to the mayor's estate.\x02\x03",
            "We have to stall him with an\x01",
            "interview while the Royal Army\x01",
            "is contacted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#044F#1PAh... I see.\x02\x03",
            "#049FMaybe that wasn't so necessary,\x01",
            "after all...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F#4P???\x02\x03",
            "Um, so will you be coming\x01",
            "with us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#045F#1POh, yes. Please allow me to\x01",
            "accompany you.\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    TurnDirection(0x102, 0x8, 400)

    ChrTalk(
        0x102,
        (
            "#012FWe'll be counting on you to\x01",
            "contact the army, Jean.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x102, 400)

    ChrTalk(
        0x8,
        "#652FJust leave it to me!\x02",
    )

    CloseMessageWindow()
    OP_28(0x3E, 0x1, 0x400)
    EventEnd(0x0)
    OP_4B(0x8, 255)
    Return()

    # Function_23_998D end

    def Function_24_A1AC(): pass

    label("Function_24_A1AC")

    EventBegin(0x0)
    OP_6D(-4700, 0, 45110, 0)
    OP_6B(2800, 0)
    ClearChrFlags(0x8, 0x80)
    OP_4A(0x8, 255)
    SetChrPos(0x101, -3360, 0, 45110, 270)
    SetChrPos(0x102, -3530, 0, 43770, 315)
    SetChrPos(0x105, -2350, 0, 44220, 270)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#650FOh, don't tell me the Royal\x01",
            "Guardsmen showed up.\x02\x03",
            "And the Arseille was there,\x01",
            "too? She's supposed to be\x01",
            "cutting-edge.\x02\x03",
            "#654FIt's too bad I just work the\x01",
            "info desk. I'd have liked to\x01",
            "see that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506FI never figured you for the\x01",
            "military enthusiast.\x02\x03",
            "#000FStill, didn't you end up speaking\x01",
            "to Colonel Richard?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#650FYes, he was on duty at Leiston HQ.\x02\x03",
            "I don't know how the Royal Guardsmen\x01",
            "got there so quickly, though...\x02\x03",
            "I guess there's a lot more cross-\x01",
            "communication in the military\x01",
            "than I thought.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FAmazing that they manage to communicate at all\x01",
            "given how many agencies there are. Regular army,\x01",
            "Border Patrol, Intelligence, the Royal Guard...\x02\x03",
            "It must be pretty complicated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#043FCleaning up after an incident like\x01",
            "this will be a major undertaking...\x02\x03",
            "What will happen to the administration\x01",
            "of Ruan from now on?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004FYeah...since the mayor's\x01",
            "been arrested.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#652FI'd imagine they'll be sending\x01",
            "in someone as acting mayor.\x02\x03",
            "And if Dalmore is found guilty,\x01",
            "elections will have to be held.\x02\x03",
            "#651FPlus, reparations will probably\x01",
            "be made toward the orphanage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#047FReally? Thank goodness...\x02\x03",
            "#048FAll of this is thanks to Estelle\x01",
            "and Joshua.\x02\x03",
            "Thank you so much...truly.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_A6E2():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A6E2)
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(
        0x101,
        (
            "#008F#2PCome on...you don't have\x01",
            "to be so formal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#1PWe just did what was right.\x02\x03",
            "Plus, it wasn't just us.\x01",
            "Agate played a big part.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#004F#2PSpeaking of...!\x02",
    )

    CloseMessageWindow()

    def lambda_A7C3():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A7C3)
    TurnDirection(0x102, 0x8, 400)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#005FJean, have you received any\x01",
            "word from him?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#652FYes, but unfortunately...\x02\x03",
            "I'm afraid he wasn't able to\x01",
            "capture the men in the black\x01",
            "uniforms.\x02\x03",
            "They were not alone, apparently.\x01",
            "Agate was ambushed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#580FWhat?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012FIs he all right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#655FYes, he managed to defeat\x01",
            "them.\x02\x03",
            "I believe he gave chase, and\x01",
            "they're on their way to Zeiss.\x02\x03",
            "By now, he's probably well\x01",
            "outside of Ruan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007FW-Wow.\x01",
            "Talk about hardcore...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#650FWell, he's got plenty of experience,\x01",
            "after all.\x02\x03",
            "He'd been chasing those black-\x01",
            "clad characters for a while.\x02\x03",
            "I think they're related to a job\x01",
            "your father asked him to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004FDad asked him?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014FAnd Agate just...did what\x01",
            "he asked?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#651FHa ha... Well, the one to put Agate\x01",
            "of the Ravens in his place was\x01",
            "none other than Cassius himself.\x02\x03",
            "And whatever he might like to claim,\x01",
            "Agate stood no chance against him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004FWhoa, seriously?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#650FCassius really beat some sense into him,\x01",
            "and Agate's too stubborn to simply say\x01",
            "thanks and leave it at that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FAh, I get it...\x02\x03",
            "Maybe that's why he's so abrasive\x01",
            "when it comes to us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F'Abrasive' barely covers that\x01",
            "guy's attitude...\x02\x03",
            "#005FHmph! Guess he's not so high and\x01",
            "mighty where Dad's involved, huh!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#045FHa ha...\x02\x03",
            "#044FOh, speaking of your father...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_ACEF():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_ACEF)
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(
        0x101,
        "#004F#2PSomething wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#043FUm, what about that black orbment\x01",
            "that lit up and saved our lives at\x01",
            "the mayor's estate...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F#2POh, yeah, that's right!\x02",
    )

    CloseMessageWindow()

    def lambda_ADAD():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_ADAD)
    OP_8C(0x101, 180, 200)
    Fade(500)
    OP_22(0x8F, 0x0, 0x64)
    SetChrChipByIndex(0x101, 13)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, -3600, 550, 44750, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#009F#2PSo much has been going on\x01",
            "that I forgot all about it.\x02\x03",
            "I wonder what that was\x01",
            "all about...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013FThat orbment may have saved\x01",
            "our skins, but it was still weird...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#653FAn unusually-colored orbment,\x01",
            "huh?\x02\x03",
            "What can you tell me about it?\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x15, 0x80)
    SetChrChipByIndex(0x101, 65535)

    def lambda_AEF7():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AEF7)
    TurnDirection(0x101, 0x8, 400)
    Sleep(400)

    ChrTalk(
        0x101,
        "#003FWell...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Estelle explained that it, along with a memo, had been in a package addressed\x01",
            "to Cassius.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x105,
        "#044FOh, my... That's quite a story.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#655FHmmm... From 'K' asking\x01",
            "about a 'Professor R'...\x02\x03",
            "Could it be...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004FYou know what it means?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#652FNot...specifically. I've got a\x01",
            "hunch, but nothing to back it\x01",
            "up.\x02\x03",
            "But if you want to know more\x01",
            "about its origin, I'd suggest\x01",
            "going to Zeiss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505FWhy Zeiss?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#652FAs you should know, Zeiss is\x01",
            "famous for the manufacture of\x01",
            "orbments.\x02\x03",
            "There must be someone there\x01",
            "who might know something\x01",
            "about your orbment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FMakes sense...\x02\x03",
            "We may never learn more about\x01",
            "the Black Orbment without\x01",
            "consulting an expert.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007FBut we still have more training\x01",
            "here to finish...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#651FHa ha... Well, about that...you\x01",
            "may want to prepare yourselves.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received \x07\x02",
            "Recommendation\x07\x00",
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3E(0x339, 1)

    ChrTalk(
        0x101,
        "#004FWhat...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014FReally?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#650FHa ha. You had to have seen this coming!\x01",
            "I mean, you got a recommendation from\x01",
            "Bose after the Sky Bandit incident...\x02\x03",
            "Given your crucial roles in all\x01",
            "the cases recently, I see no\x01",
            "reason not to award it.\x02\x03",
            "Your assessment and reward\x01",
            "have been prepared.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x3D, 0x4, 0x10)
    OP_28(0x3E, 0x4, 0x10)
    Sleep(100)
    OP_AF(0x22, 0x3D)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    Sleep(100)
    OP_AF(0x22, 0x3E)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)

    ChrTalk(
        0x101,
        (
            "#008FWow... All this on top of the pay\x01",
            "for performing in the campus\x01",
            "festival?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019FThank you for everything you've\x01",
            "done for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#651FCome, now...you've earned it.\x02\x03",
            "I confess, I'd also like to see you\x01",
            "advance as quickly as possible.\x02\x03",
            "I believe we'll be able to make\x01",
            "the best use of your talents\x01",
            "this way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#008FHa ha... Thank you, Jean.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FWe'll do our best to live up\x01",
            "to your expectations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#048FCongratulations, both of you!\x02\x03",
            "#045FIt'll be kind of lonely here\x01",
            "without you, though...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B628():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B628)
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(
        0x101,
        "#003F#2PKloe...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F#1PYou're right... It'll be tough\x01",
            "to say goodbye.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#045FOh...please don't mind me.\x01",
            "I'm just being selfish.\x02\x03",
            "#542FWill you please tell me when\x01",
            "you find out what day you're\x01",
            "leaving?\x02\x03",
            "I'd like to see you off, at\x01",
            "least as far as the Air-Letten\x01",
            "checkpoint.\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x9C4)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_21()
    Sleep(1000)
    OP_AD(0x40043, 0x0, 0x0, 0x64)
    Sleep(4000)
    OP_56(0x2)
    OP_83(0x13, 0x0)
    OP_A2(0x44B)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0xF2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(100000, -100000, 100000, 0)
    FadeToBright(0, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        240,
        180,
        0,
        (
            "[Save]\x01",                          # 0
            "[Continue to next chapter]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B7F1")
    ShowSaveMenu()

    label("loc_B7F1")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_AE(0xC8)
    Sleep(2000)
    OP_A2(0x44C)
    OP_A2(0x442)
    OP_28(0x3E, 0x1, 0x800)
    OP_28(0x53, 0x4, 0x2)
    OP_28(0x53, 0x4, 0x4)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/R2412   ._SN", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_24_A1AC end

    def Function_25_B831(): pass

    label("Function_25_B831")

    EventBegin(0x1)
    TurnDirection(0x9, 0x0, 0)
    OP_4A(0x9, 0)
    OP_51(0x14, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x14, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x14, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0x14, 0x3E8)

    ChrTalk(
        0x9,
        (
            "#830FI'm sorry, but there's a meeting\x01",
            "upstairs.\x02\x03",
            "Why don't you take in the sights\x01",
            "until it's done?\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    OP_4B(0x9, 0)
    OP_8C(0x9, 90, 0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_25_B831 end

    SaveToFile()

Try(main)
