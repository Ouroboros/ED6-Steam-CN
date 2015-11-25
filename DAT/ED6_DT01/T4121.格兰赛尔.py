from ED6ScenarioHelper import *

def main():
    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4121   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4121.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60014",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/T4121   ._SN',
            'ED6_DT01/T4121_1 ._SN',
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
        'Elnan',                                # 9
        'Carna',                                # 10
        'Anelace',                              # 11
        'Grant',                                # 12
        'Kurt',                                 # 13
        '1st Lieutenant Schwarz',               # 14
        'Agate',                                # 15
        'Scherazard',                           # 16
        'Zane',                                 # 17
        'Cassius',                              # 18
        'Fisher',                               # 19
        'Lloyd',                                # 20
        'Percy',                                # 21
        'Helmuth',                              # 22
        'Factory Chief Murdock',                # 23
        'Mayor Klaus',                          # 24
        'Olivier',                              # 25
        'Mueller',                              # 26
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
        'ED6_DT07/CH02580 ._CH',             # 00
        'ED6_DT07/CH01240 ._CH',             # 01
        'ED6_DT07/CH01630 ._CH',             # 02
        'ED6_DT07/CH01260 ._CH',             # 03
        'ED6_DT07/CH01620 ._CH',             # 04
        'ED6_DT06/CH20112 ._CH',             # 05
        'ED6_DT07/CH01410 ._CH',             # 06
        'ED6_DT07/CH00050 ._CH',             # 07
        'ED6_DT07/CH00020 ._CH',             # 08
        'ED6_DT07/CH00070 ._CH',             # 09
        'ED6_DT07/CH02000 ._CH',             # 0A
        'ED6_DT07/CH01200 ._CH',             # 0B
        'ED6_DT07/CH01020 ._CH',             # 0C
        'ED6_DT07/CH01460 ._CH',             # 0D
        'ED6_DT07/CH01220 ._CH',             # 0E
        'ED6_DT07/CH01633 ._CH',             # 0F
        'ED6_DT07/CH02620 ._CH',             # 10
        'ED6_DT07/CH02350 ._CH',             # 11
        'ED6_DT07/CH00030 ._CH',             # 12
        'ED6_DT07/CH02190 ._CH',             # 13
        'ED6_DT06/CH20038 ._CH',             # 14
    )

    AddCharChipPat(
        'ED6_DT07/CH02580P._CP',             # 00
        'ED6_DT07/CH01240P._CP',             # 01
        'ED6_DT07/CH01630P._CP',             # 02
        'ED6_DT07/CH01260P._CP',             # 03
        'ED6_DT07/CH01620P._CP',             # 04
        'ED6_DT06/CH20112P._CP',             # 05
        'ED6_DT07/CH01410P._CP',             # 06
        'ED6_DT07/CH00050P._CP',             # 07
        'ED6_DT07/CH00020P._CP',             # 08
        'ED6_DT07/CH00070P._CP',             # 09
        'ED6_DT07/CH02000P._CP',             # 0A
        'ED6_DT07/CH01200P._CP',             # 0B
        'ED6_DT07/CH01020P._CP',             # 0C
        'ED6_DT07/CH01460P._CP',             # 0D
        'ED6_DT07/CH01220P._CP',             # 0E
        'ED6_DT07/CH01633P._CP',             # 0F
        'ED6_DT07/CH02620P._CP',             # 10
        'ED6_DT07/CH02350P._CP',             # 11
        'ED6_DT07/CH00030P._CP',             # 12
        'ED6_DT07/CH02190P._CP',             # 13
        'ED6_DT06/CH20038P._CP',             # 14
    )

    DeclNpc(
        X                   = -4460,
        Z                   = 0,
        Y                   = 960,
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
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 3,
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
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 2,
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
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 4,
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
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 5,
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
        Unknown3            = 7,
        ChipIndex           = 0x7,
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
        Unknown3            = 8,
        ChipIndex           = 0x8,
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
        Unknown3            = 9,
        ChipIndex           = 0x9,
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
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 27820,
        Z                   = 0,
        Y                   = 62520,
        Direction           = 191,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 84510,
        Z                   = 0,
        Y                   = 56870,
        Direction           = 274,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 90050,
        Z                   = 0,
        Y                   = 63770,
        Direction           = 15,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 25740,
        Z                   = 0,
        Y                   = 58130,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 25470,
        Z                   = 0,
        Y                   = 58140,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 31740,
        Z                   = 0,
        Y                   = 63030,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
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
        Unknown3            = 18,
        ChipIndex           = 0x12,
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
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = -2600,
        TriggerZ            = 0,
        TriggerY            = 820,
        TriggerRange        = 800,
        ActorX              = -4460,
        ActorZ              = 1500,
        ActorY              = 960,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 27820,
        TriggerZ            = 0,
        TriggerY            = 60600,
        TriggerRange        = 800,
        ActorX              = 27820,
        ActorZ              = 1500,
        ActorY              = 62520,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 4970,
        TriggerZ            = 0,
        TriggerY            = -1040,
        TriggerRange        = 1400,
        ActorX              = 4970,
        ActorZ              = 2000,
        ActorY              = -1040,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 21,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_3FE",          # 00, 0
        "Function_1_665",          # 01, 1
        "Function_2_6F5",          # 02, 2
        "Function_3_70B",          # 03, 3
        "Function_4_72F",          # 04, 4
        "Function_5_7BB",          # 05, 5
        "Function_6_1015",         # 06, 6
        "Function_7_1ADA",         # 07, 7
        "Function_8_1BA3",         # 08, 8
        "Function_9_1C21",         # 09, 9
        "Function_10_1C26",        # 0A, 10
        "Function_11_2E04",        # 0B, 11
        "Function_12_2E09",        # 0C, 12
        "Function_13_941A",        # 0D, 13
        "Function_14_B2F8",        # 0E, 14
        "Function_15_B351",        # 0F, 15
        "Function_16_BB74",        # 10, 16
        "Function_17_D66F",        # 11, 17
        "Function_18_EA57",        # 12, 18
        "Function_19_F8AF",        # 13, 19
        "Function_20_F8F9",        # 14, 20
        "Function_21_F943",        # 15, 21
    )


    def Function_0_3FE(): pass

    label("Function_0_3FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_40C")
    OP_A3(0x3FA)
    Event(0, 15)

    label("loc_40C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_41A")
    OP_A3(0x3FB)
    Event(0, 16)

    label("loc_41A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 4)), scpexpr(EXPR_END)), "loc_428")
    OP_A3(0x3FC)
    Event(0, 17)

    label("loc_428")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 5)), scpexpr(EXPR_END)), "loc_436")
    OP_A3(0x3FD)
    Event(0, 18)

    label("loc_436")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_442"),
        (SWITCH_DEFAULT, "loc_458"),
    )


    label("loc_442")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_455")
    OP_A2(0x609)
    Event(0, 13)

    label("loc_455")

    Jump("loc_458")

    label("loc_458")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_46C")
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    Jump("loc_664")

    label("loc_46C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_476")
    Jump("loc_664")

    label("loc_476")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_4F4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 3)), scpexpr(EXPR_END)), "loc_49A")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 120230, 0, -2360, 90)

    label("loc_49A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 5)), scpexpr(EXPR_END)), "loc_4B7")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 122900, 0, -2350, 270)

    label("loc_4B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 2)), scpexpr(EXPR_END)), "loc_4D4")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 121650, 0, -3900, 0)

    label("loc_4D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 4)), scpexpr(EXPR_END)), "loc_4F1")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 121680, 0, -830, 180)

    label("loc_4F1")

    Jump("loc_664")

    label("loc_4F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_538")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 62290, 0, -3770, 108)
    OP_43(0xC, 0x0, 0x0, 0x2)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 58990, 0, 2730, 7)
    OP_43(0x9, 0x0, 0x0, 0x2)
    Jump("loc_664")

    label("loc_538")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_547")
    SetChrFlags(0x14, 0x80)
    Jump("loc_664")

    label("loc_547")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_584")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 54920, 0, -3370, 95)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 58990, 0, 2730, 7)
    OP_43(0x9, 0x0, 0x0, 0x2)
    Jump("loc_664")

    label("loc_584")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_5DE")
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 58990, 0, 2730, 7)
    OP_43(0x9, 0x0, 0x0, 0x2)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 15)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xA, 0x4)
    OP_44(0xA, 0xFF)
    SetChrPos(0xA, 58500, 200, -3440, 90)
    Jump("loc_664")

    label("loc_5DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_61B")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 54920, 0, -3370, 95)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 58990, 0, 2730, 7)
    OP_43(0x9, 0x0, 0x0, 0x2)
    Jump("loc_664")

    label("loc_61B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_62A")
    ClearChrFlags(0x15, 0x80)
    Jump("loc_664")

    label("loc_62A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_65D")
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 15)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xA, 0x4)
    OP_44(0xA, 0xFF)
    SetChrPos(0xA, 58500, 200, -3440, 90)
    Jump("loc_664")

    label("loc_65D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_664")

    label("loc_664")

    Return()

    # Function_0_3FE end

    def Function_1_665(): pass

    label("Function_1_665")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6C), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_695")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_695")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_6A8")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x4B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6B8")

    label("loc_6A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 2)), scpexpr(EXPR_END)), "loc_6B8")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x58), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6EB")
    OP_B1("t4121_y")
    Jump("loc_6F4")

    label("loc_6EB")

    OP_B1("t4121_n")

    label("loc_6F4")

    Return()

    # Function_1_665 end

    def Function_2_6F5(): pass

    label("Function_2_6F5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_70A")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_6F5")

    label("loc_70A")

    Return()

    # Function_2_6F5 end

    def Function_3_70B(): pass

    label("Function_3_70B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_72E")
    OP_8D(0xFE, 84890, 62930, 95170, 65019, 2000)
    Jump("Function_3_70B")

    label("loc_72E")

    Return()

    # Function_3_70B end

    def Function_4_72F(): pass

    label("Function_4_72F")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Oh ho ho...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll be honest; I never imagined this\x01",
            "simple, passionate club would balloon\x01",
            "out into something so spectacular!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_4_72F end

    def Function_5_7BB(): pass

    label("Function_5_7BB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_86D")

    ChrTalk(
        0xFE,
        (
            "The Martial Arts Competition,\x01",
            "the Queen's Birthday Celebration...\x01",
            "All well and good...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...But there are lots of us who'd \x01",
            "rather be out fishing right now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1011")

    label("loc_86D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_9AA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_90B")

    ChrTalk(
        0xFE,
        (
            "It's kind of tough for us\x01",
            "outdoorsy types to be forced\x01",
            "into places like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I just hope the airships\x01",
            "get back into service soon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9A7")

    label("loc_90B")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        "*sigh*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's kind of tough for us\x01",
            "outdoorsy types to be forced\x01",
            "into places like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I just hope the airships\x01",
            "get back into service soon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9A7")

    Jump("loc_1011")

    label("loc_9AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_A73")

    ChrTalk(
        0xFE,
        (
            "I went to the platform to see if there\x01",
            "were any flights to Ruan, but the soldiers\x01",
            "there told me the airships are grounded.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was really looking forward\x01",
            "to doing some ocean fishing!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1011")

    label("loc_A73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_B37")

    ChrTalk(
        0xFE,
        (
            "Today I ran across this girl\x01",
            "at practice who might be a\x01",
            "great fit for our group.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After practice, though, she said\x01",
            "she was going to stay behind at\x01",
            "the lake and catch some fish.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1011")

    label("loc_B37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_B41")
    Jump("loc_1011")

    label("loc_B41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_C83")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_BE6")

    ChrTalk(
        0xFE,
        (
            "Tomorrow is our introductory\x01",
            "course for novice anglers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope by the end of the day\x01",
            "you'll have an understanding\x01",
            "of the joys of fishing!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C80")

    label("loc_BE6")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "Tomorrow is our introductory\x01",
            "course for novice anglers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Anyone is welcome to join.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope we can convey to you the\x01",
            "true joy of fishing!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C80")

    Jump("loc_1011")

    label("loc_C83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_C8D")
    Jump("loc_1011")

    label("loc_C8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_D3A")

    ChrTalk(
        0xFE,
        (
            "Preparing to fish can be just as\x01",
            "fun as actually casting your lures.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The secret is to envision yourself\x01",
            "catching the big one, and just...\x01",
            "go from there!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1011")

    label("loc_D3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_DDF")

    ChrTalk(
        0xFE,
        (
            "You might be surprised what\x01",
            "you can end up catching with\x01",
            "a hand-crafted lure!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's a special joy in catching\x01",
            "a fish with your own creation...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1011")

    label("loc_DDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_E64")

    ChrTalk(
        0xFE,
        (
            "No masters of the sea were\x01",
            "caught in Ruan...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...No kings of the abyss were\x01",
            "hooked in Zeiss...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm no pro...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1011")

    label("loc_E64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1011")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_F17")

    ChrTalk(
        0xFE,
        (
            "You ought to see our leader, the appropriately-\x01",
            "named Mr. Fisher. He's the real pro. I mean,\x01",
            "hell, it's in his name!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "We call him 'The Duke of Angling.'\x02",
    )

    CloseMessageWindow()
    Jump("loc_1011")

    label("loc_F17")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "Our president, Mr. Fisher, is a consummate\x01",
            "professional...and the rest of us would KILL\x01",
            "for that last name!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He's the one who founded our\x01",
            "organization, to preserve our\x01",
            "methods for future fishermen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "We call him 'The Duke of Angling.'\x02",
    )

    CloseMessageWindow()

    label("loc_1011")

    TalkEnd(0xFE)
    Return()

    # Function_5_7BB end

    def Function_6_1015(): pass

    label("Function_6_1015")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_10B4")

    ChrTalk(
        0xFE,
        (
            "I'll never forgive Colonel Richard! He's grounded\x01",
            "the airships and stolen our fishing from us!\x01",
            "...Uh, and there was also that coup d'etat...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AD6")

    label("loc_10B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_1150")

    ChrTalk(
        0xFE,
        (
            "They're calling me... The Lenhardt River...\x01",
            "The Valleria Shore... Even Azelia Bay...\x01",
            "All calling my name...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Please...give me...a rod...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1AD6")

    label("loc_1150")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_12A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_11E1")

    ChrTalk(
        0xFE,
        (
            "A life without fishing is a life\x01",
            "better spent dead. If you can even\x01",
            "call it a life at all!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm going to lose my mind!\x02",
    )

    CloseMessageWindow()
    Jump("loc_129E")

    label("loc_11E1")

    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "How long do they plan to keep\x01",
            "us hostage like this?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A life without fishing is a life\x01",
            "better spent dead. If you can even\x01",
            "call it a life at all!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm going to lose my mind!\x02",
    )

    CloseMessageWindow()

    label("loc_129E")

    Jump("loc_1AD6")

    label("loc_12A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_1344")

    ChrTalk(
        0xFE,
        (
            "If they don't hurry and catch\x01",
            "those terrorists, we'll never\x01",
            "go fishing again...this season!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For Goddess' sake, Colonel!\x01",
            "You must DO SOMETHING!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AD6")

    label("loc_1344")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_13EB")

    ChrTalk(
        0xFE,
        (
            "Percy's out at the fishing\x01",
            "class, I suppose?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That class serves an important function\x01",
            "for us: to boost our membership and\x01",
            "spread angling awareness!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AD6")

    label("loc_13EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_147D")

    ChrTalk(
        0xFE,
        (
            "Yesterday's entrance exam had\x01",
            "some great weather for fishing!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was supposed to be proctor, but\x01",
            "I couldn't resist casting in!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AD6")

    label("loc_147D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_1487")
    Jump("loc_1AD6")

    label("loc_1487")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1502")

    ChrTalk(
        0xFE,
        (
            "I'm proctor for tomorrow's\x01",
            "entrance exam, so I need to\x01",
            "go out on the lake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Gotta get everything ready!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1AD6")

    label("loc_1502")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_16B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_15C6")

    ChrTalk(
        0xFE,
        (
            "Liberl is a small country, but\x01",
            "we have lots of lakes, rivers\x01",
            "and oceans to fish in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Of course, finding new spots for\x01",
            "fishing is just as important as\x01",
            "the fishing itself!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16B2")

    label("loc_15C6")

    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "Liberl's small, but it's a paradise\x01",
            "for us fishermen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There are lakes, rivers and oceans \x01",
            "all within a stone's throw of one\x01",
            "another.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Of course, finding new spots for\x01",
            "fishing is just as important as\x01",
            "the fishing itself!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16B2")

    Jump("loc_1AD6")

    label("loc_16B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_178D")

    ChrTalk(
        0xFE,
        (
            "The Kings of Valleria Shore-- those\x01",
            "are fish, not actual monarchs-- go\x01",
            "into the deep when it gets cold out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "One of these days, I'm gonna catch\x01",
            "'em before that time comes... Just\x01",
            "you wait and see!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AD6")

    label("loc_178D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1AD6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_187E")

    ChrTalk(
        0xFE,
        (
            "I've been chasin' the Kings of Valleria\x01",
            "Shore-- the biggest fish you ever done\x01",
            "see-- for roundabouts five years now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Next hook is number 23. Come on,\x01",
            "lucky 23! Factor of nothin', but\x01",
            "to me, you're my everythin'!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AD6")

    label("loc_187E")

    OP_A2(0x3)

    ChrTalk(
        0xFE,
        "Welcome to the Fisherman's Guild!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014FWhoa, hey...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F...What's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I know you two!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You're those bracers I met\x01",
            "at the lake in Bose, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#004FOh yeah! You were the one who\x01",
            "told us about the Sky Bandits!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So you DO remember! Welcome, welcome!\x01",
            "Welcome to the Fisherman's Guild!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FNow that I think about it, you\x01",
            "DID mention the Fisherman's Guild\x01",
            "when we spoke with you before...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "This is our main headquarters.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Come on in, and take a load off!\x01",
            "Sit back, relax, and enjoy the\x01",
            "opulence of fish and brine!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AD6")

    TalkEnd(0xFE)
    Return()

    # Function_6_1015 end

    def Function_7_1ADA(): pass

    label("Function_7_1ADA")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "#800FThe best fishing gear is that\x01",
            "which represents engineering\x01",
            "efficiency and elegance.\x02\x03",
            "#801F...The sort of gear I'd want to\x01",
            "own even if I never fished at\x01",
            "all, just for its sheer beauty.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_7_1ADA end

    def Function_8_1BA3(): pass

    label("Function_8_1BA3")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "#600FThe world is going by too fast\x01",
            "for me nowadays.\x02\x03",
            "I just want to slow it all down\x01",
            "and fish at Valleria Shore.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_1BA3 end

    def Function_9_1C21(): pass

    label("Function_9_1C21")

    Call(0, 10)
    Return()

    # Function_9_1C21 end

    def Function_10_1C26(): pass

    label("Function_10_1C26")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_224C")
    OP_A2(0x67C)

    ChrTalk(
        0x12,
        (
            "Welcome, friends, to the \x01",
            "Fisherman's Guild!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505FOh, wow, there's a guild for\x01",
            "you guys?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "Indeed there is!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "There be giant fish in the waters 'round these\x01",
            "parts. We call them Kings, an' they wriggle an'\x01",
            "they dive all through the waters of Liberl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "It is our job-- nay, our sacred duty!-- to find\x01",
            "these elusive piscine giants and best them in a\x01",
            "battle of lures, reels and wits. LRW, for short.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501FSo...you guys like fishing, then,\x01",
            "I take it!\x02\x03",
            "For me...fishing's all right,\x01",
            "I guess...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014FYou all seem very, um...\x01",
            "dedicated to your hobby.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "We fulfill our existence by traveling the\x01",
            "width and breadth of Liberl, and snatching\x01",
            "marine life from every corner of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "We spread the joys of fishing,\x01",
            "hold introductory seminars and\x01",
            "sell our handmade gear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "We've even begun lobbying the\x01",
            "queen to create a fund to help\x01",
            "protect our fishing locations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004FWow. You guys clearly are REALLY\x01",
            "into this. Like, SCARY into it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019FA true society for fishermen.\x01",
            "You guys are actually pretty\x01",
            "impressive!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "Would you like to join us?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "There is a small examination, but otherwise,\x01",
            "it's just a matter of adding your names to\x01",
            "our roster...in PERMANENT INK...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506FUh, thanks, and it really does sound fun,\x01",
            "but we've...kind of got...things to do\x01",
            "right now. Just...things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "A shame. You have the eyes of master\x01",
            "anglers. I guess you could say, I can\x01",
            "see it in the ANGLES of your retinas!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "If you have a change of heart,\x01",
            "please come back anytime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "We are always ready and eager\x01",
            "for new recruits!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E00")

    label("loc_224C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_239C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_22D0")

    ChrTalk(
        0x12,
        (
            "Yesterday I met a rather charming\x01",
            "woman.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "We happily inducted her into our\x01",
            "growing cul-- I mean, society.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2399")

    label("loc_22D0")

    OP_A2(0x2)

    ChrTalk(
        0x12,
        (
            "Yesterday I met a rather charming\x01",
            "woman.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "We happily inducted her into our\x01",
            "growing cul-- I mean, society.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "I swear, I've never seen a newbie\x01",
            "handle a fishing pole quite so well\x01",
            "before!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2399")

    Jump("loc_2E00")

    label("loc_239C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_2425")

    ChrTalk(
        0x12,
        (
            "There was quite a fuss outside\x01",
            "a short while ago...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "You know what fusses do?\x01",
            "They scare fish! And\x01",
            "THAT CANNOT STAND!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E00")

    label("loc_2425")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_257B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2495")

    ChrTalk(
        0x12,
        (
            "No going out at night, no\x01",
            "travel...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "This is truly a dark time\x01",
            "for our beloved guild.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2578")

    label("loc_2495")

    OP_A2(0x2)

    ChrTalk(
        0x12,
        (
            "Thanks to the curfew, we can\x01",
            "no longer do night fishing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "But more dire is our inability to travel,\x01",
            "cutting us off from all but the most local\x01",
            "of fishing holes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "This is truly a dark time\x01",
            "for our beloved guild.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2578")

    Jump("loc_2E00")

    label("loc_257B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_263F")

    ChrTalk(
        0x12,
        (
            "The weather and water today are \x01",
            "absolutely perfect for fishing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "After work, I intend to meet my compatriots\x01",
            "at the lake. We're sure to catch more than\x01",
            "our fair share of fish!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E00")

    label("loc_263F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_26EC")

    ChrTalk(
        0x12,
        (
            "Yesterday I met a truly passionate\x01",
            "neophyte angler.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "I was moved by her love of the sport,\x01",
            "and asked Percy to extend her an\x01",
            "invitation to join our ranks.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E00")

    label("loc_26EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_28F4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_27C8")

    ChrTalk(
        0x12,
        (
            "If you truly love fishing,\x01",
            "and have even a modicum of\x01",
            "skill, we will welcome you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "Today's applicants have skill, no doubt...\x01",
            "but they lack a true, burning passion for\x01",
            "this holiest of pastimes.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28F1")

    label("loc_27C8")

    OP_A2(0x2)

    ChrTalk(
        0x12,
        (
            "If you truly love fishing,\x01",
            "and have even a modicum of\x01",
            "skill, we will welcome you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "Today's applicants have skill, no doubt...\x01",
            "but they lack a true, burning passion for\x01",
            "this holiest of pastimes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "What's become of the world, that\x01",
            "fishing should be relegated as a\x01",
            "mere weekend hobby?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28F1")

    Jump("loc_2E00")

    label("loc_28F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_299D")

    ChrTalk(
        0x12,
        (
            "Today is our entrance exam at\x01",
            "Valleria Shore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "We require proctors, so all members\x01",
            "are expected to attend. And those\x01",
            "who don't...shall be punished...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E00")

    label("loc_299D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2B56")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2A48")

    ChrTalk(
        0x12,
        (
            "To truly love fishing is to\x01",
            "respect its rules and customs!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "Pollution of our grounds and\x01",
            "waters is basis for immediate\x01",
            "expulsion from the guild.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B53")

    label("loc_2A48")

    OP_A2(0x2)

    ChrTalk(
        0x12,
        (
            "To truly love fishing is to\x01",
            "respect its rules and customs!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "Pollution of our grounds and\x01",
            "waters is basis for immediate\x01",
            "expulsion from the guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "I trust none of you are foolish enough\x01",
            "to cross us. You wouldn't want to wind\x01",
            "up like Curly Jefferson...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B53")

    Jump("loc_2E00")

    label("loc_2B56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_2CAD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2BF7")

    ChrTalk(
        0x12,
        (
            "Our handmade fishing gear is\x01",
            "in high demand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "We have customers who fly in\x01",
            "from the remotest areas of the\x01",
            "world to purchase our wares.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CAA")

    label("loc_2BF7")

    OP_A2(0x2)

    ChrTalk(
        0x12,
        (
            "Our handmade fishing gear is\x01",
            "in high demand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "We have customers who fly in\x01",
            "from the remotest areas of the\x01",
            "world to purchase our wares.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "It's immensely gratifying!\x02",
    )

    CloseMessageWindow()

    label("loc_2CAA")

    Jump("loc_2E00")

    label("loc_2CAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_2D86")

    ChrTalk(
        0x12,
        (
            "Like the Martial Arts Competition, one day we\x01",
            "would love to hold a Grand Fishing Tournament.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "I would love to personally participate,\x01",
            "in fact. I have a competitive streak like\x01",
            "you wouldn't believe!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E00")

    label("loc_2D86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_2E00")

    ChrTalk(
        0x12,
        (
            "If you have a change of heart,\x01",
            "please come back anytime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "We are always ready and eager\x01",
            "for new recruits!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E00")

    TalkEnd(0x12)
    Return()

    # Function_10_1C26 end

    def Function_11_2E04(): pass

    label("Function_11_2E04")

    Call(0, 12)
    Return()

    # Function_11_2E04 end

    def Function_12_2E09(): pass

    label("Function_12_2E09")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_315E")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_314D")
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4B, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x4B, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3011")

    ChrTalk(
        0x8,
        (
            "#760FJob well done, everyone.\x02\x03",
            "#760FThe operation at the Erbe Royal\x01",
            "Villa was a complete success.\x02\x03",
            "We'll take a moment now to\x01",
            "pass out the bounties.\x02\x03",
            "Please use this money to prepare\x01",
            "yourselves for any upcoming battles.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_AF(0x63, 0x4B)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_28(0x4C, 0x4, 0x10)
    OP_28(0x4C, 0x4, 0x20)

    ChrTalk(
        0x8,
        (
            "#760FWe sincerely hope you'll continue to\x01",
            "uphold your vigilance and dedication.\x02\x03",
            "And we will continue to support\x01",
            "you in any way that we can.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3144")

    label("loc_3011")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_A9(0x63)"), scpexpr(EXPR_END)), "loc_30AA")
    Sleep(200)

    ChrTalk(
        0x8,
        (
            "#760FCongratulations on an assignment\x01",
            "well done.\x02\x03",
            "If you finish any other posted tasks,\x01",
            "please be sure to come back and let\x01",
            "us know.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3144")

    label("loc_30AA")

    Sleep(200)

    ChrTalk(
        0x8,
        (
            "#760FDoesn't look like you have anything\x01",
            "new to report right now.\x02\x03",
            "If you finish any posted tasks, please\x01",
            "be sure to come back and let us know.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3144")

    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_314D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_315E")
    TalkEnd(0x8)
    Return()

    label("loc_315E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3397")
    EventBegin(0x0)

    ChrTalk(
        0x8,
        (
            "#760FAh, you're here. Good.\x02\x03",
            "Once the operation begins, you\x01",
            "won't have any opportunity to\x01",
            "return to the city.\x02\x03",
            "So if you still have loose ends\x01",
            "to tie up, speak now...or forever\x01",
            "hold your peace.\x02",
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
            "[It's okay, we're ready]\x01",      # 0
            "[We're not ready yet]\x01",         # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_32B3"),
        (1, "loc_333E"),
        (SWITCH_DEFAULT, "loc_3394"),
    )


    label("loc_32B3")

    OP_A2(0x650)
    OP_28(0x4C, 0x4, 0x2)
    OP_28(0x4C, 0x4, 0x4)
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)

    ChrTalk(
        0x8,
        (
            "#764FUnderstood.\x02\x03",
            "#762FLet's review the operation.\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_21()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/C4111   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    label("loc_333E")


    ChrTalk(
        0x8,
        (
            "#760FUnderstood.\x02\x03",
            "When you're ready to begin,\x01",
            "please report to me.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 90, 0)
    OP_4B(0x8, 255)
    EventEnd(0x1)
    Return()

    label("loc_3394")

    Jump("loc_9416")

    label("loc_3397")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5925")
    EventBegin(0x0)
    OP_A2(0x650)
    OP_28(0x4B, 0x1, 0x800)
    OP_28(0x4B, 0x1, 0x1000)
    Fade(1000)
    OP_4A(0x8, 255)
    OP_6D(-3330, 0, 750, 0)
    SetChrPos(0x101, -2590, 0, 280, 270)
    SetChrPos(0x102, -2590, 0, 1220, 270)
    SetChrPos(0x108, -1500, 0, 750, 270)
    OP_8C(0x8, 90, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#760FThe other bracers are already\x01",
            "assembled.\x02\x03",
            "Have you heard from the Royal\x01",
            "Guardsmen or the reporter?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007FSorry, sir. No contact.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FBut we believe we've gathered\x01",
            "the intelligence we need.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Joshua explained everything they learned from the cathedral and the\x01",
            "Liberl News HQ.\x02",
        )
    )

    CloseMessageWindow()
    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(
        0x8,
        (
            "#764FI see. We can conclude with fair\x01",
            "certainty, then, that Princess\x01",
            "Klaudia is inside the Villa.\x02\x03",
            "#762FIt's unfortunate that you were unable to make\x01",
            "contact with the Royal Guardsmen, but at least\x01",
            "we now know they haven't been captured.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#4P#070FShall we get started, then?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#760FYes.\x02\x03",
            "We need to start working out the details of the\x01",
            "rescue operation.\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_6D(122020, 0, -2070, 0)
    OP_67(0, 6320, -10000, 0)
    OP_6B(1200, 0)
    OP_6C(315000, 0)
    OP_6E(678, 0)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xC, 123360, 0, -2490, 1)
    SetChrPos(0x9, 123640, 0, -1210, 350)
    SetChrPos(0xB, 125100, 0, -1960, 320)
    SetChrPos(0xA, 124920, 0, -560, 315)
    SetChrPos(0x101, 120480, 0, 820, 90)
    SetChrPos(0x102, 120560, 0, -380, 45)
    SetChrPos(0x108, 121320, 0, -1960, 0)
    SetChrPos(0x8, 122790, 0, 1800, 180)
    OP_4A(0xC, 255)
    OP_4A(0x9, 255)
    OP_4A(0xB, 255)
    OP_4A(0xA, 255)
    OP_1D(0x65)
    FadeToBright(2000, 0)
    OP_6D(122020, 0, 1070, 2500)

    ChrTalk(
        0x8,
        (
            "#764F...Are we all up-to-date on the pertinent\x01",
            "details of the Intelligence Division's\x01",
            "planned coup d'etat, then?\x02\x03",
            "#762FGiven this information, we should\x01",
            "consider ourselves under contractual\x01",
            "obligation to Queen Alicia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#844FI can barely believe what I'm hearing...\x02\x03",
            "I'm ashamed of myself for not noticing\x01",
            "something was amiss sooner...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#813FI was suspicious of those Special\x01",
            "Ops troops from the very beginning...\x02\x03",
            "...But I really trusted Colonel\x01",
            "Richard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#833FAnd he was behind the Sky Bandits\x01",
            "AND Mayor Dalmore...\x02\x03",
            "#832FWe got completely snowed!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#822FAnd we can't let them get away with it,\x01",
            "that's for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#760FCan you all be counted on to\x01",
            "cooperate in this assignment?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#820FDamn straight!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#830FJust lead the way.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#840FI owe these guys some black eyes.\x01",
            "Rhyme unintended.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#816FCount me in, for sure!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 400)

    ChrTalk(
        0x101,
        "#008FThis is gonna be good!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x9, 400)

    ChrTalk(
        0x102,
        (
            "#010FWe've got strong allies. We'll\x01",
            "prevail, without a doubt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#764FNow, let me explain the details\x01",
            "of this mission.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3BF8():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3BF8)

    def lambda_3C06():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3C06)
    Sleep(400)

    ChrTalk(
        0x8,
        (
            "#762FWe have to move fast, as there\x01",
            "are lives at stake here.\x02\x03",
            "It's not the most elegant approach, but\x01",
            "I believe taking control of the villa through\x01",
            "a frontal assault is our best option.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#824FWe don't have time to try and find some\x01",
            "route to infiltrate, so I guess that's the\x01",
            "only option we got.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#832FHow will we be divided?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#840FWe'll split into two groups: a\x01",
            "decoy team and a rescue team.\x02\x03",
            "The decoy team will draw the attention\x01",
            "of the main forces, while the rescue\x01",
            "team makes its way into the villa.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F#6PRemember, though, we're dealing with the\x01",
            "Intelligence Division's Special Ops here.\x02\x03",
            "If I may, I'd like to suggest we also add an\x01",
            "ambush team to aid the decoy team, and a second\x01",
            "decoy team to assist the rescue team.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 135, 400)

    ChrTalk(
        0x101,
        (
            "#004F#6PMan, we're really teeming with teams here! But\x01",
            "why do we need those?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010FThe ambush team would lie in wait until the\x01",
            "decoy team draws out the enemy forces, and then\x01",
            "both teams could attack at once.\x02\x03",
            "Meanwhile, the second decoy team would attempt\x01",
            "to break the enemy's ranks, allowing the rescue\x01",
            "team to enter the villa more easily.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F#6PAh, yeah, I guess that's a good\x01",
            "point. Evens the odds a little\x01",
            "bit.\x02\x03",
            "#505FBut do we have enough members\x01",
            "to spread among four squads?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#765FNo, we don't.\x02\x03",
            "We've contacted other guild branches,\x01",
            "but with the airships grounded, we're\x01",
            "pretty much on our own.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4181():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4181)
    OP_8C(0x101, 90, 400)

    ChrTalk(
        0x101,
        (
            "#007FWell...crap...\x02\x03",
            "#003FIf only we had Schera and Agate!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#764FHowever, I agree with Zane that trying to\x01",
            "carry out this operation with only two squads\x01",
            "is risky.\x02\x03",
            "We may need to re-examine this\x01",
            "strategy.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0xD, 123420, -2000, 4570, 270)

    NpcTalk(
        0xD,
        "Woman's Voice",
        (
            "#1PIf numbers are all you lack,\x01",
            "maybe we can be of assistance!\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xD, 0x80)
    SetChrChipByIndex(0xD, 6)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x108, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_4396():

        label("loc_4396")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_4396")

    QueueWorkItem2(0x101, 1, lambda_4396)

    def lambda_43A7():

        label("loc_43A7")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_43A7")

    QueueWorkItem2(0x102, 1, lambda_43A7)

    def lambda_43B8():

        label("loc_43B8")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_43B8")

    QueueWorkItem2(0x108, 1, lambda_43B8)

    def lambda_43C9():

        label("loc_43C9")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_43C9")

    QueueWorkItem2(0xB, 1, lambda_43C9)

    def lambda_43DA():

        label("loc_43DA")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_43DA")

    QueueWorkItem2(0x9, 1, lambda_43DA)

    def lambda_43EB():

        label("loc_43EB")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_43EB")

    QueueWorkItem2(0xC, 1, lambda_43EB)

    def lambda_43FC():

        label("loc_43FC")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_43FC")

    QueueWorkItem2(0xA, 1, lambda_43FC)

    def lambda_440D():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_440D)
    SetChrFlags(0x8, 0x4)

    def lambda_4420():
        OP_8F(0xFE, 0x1DCE0, 0x0, 0x73A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_4420)

    def lambda_443B():
        OP_8E(0xFE, 0x1D57E, 0x0, 0x132E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_443B)
    OP_6D(120550, 0, 3300, 2000)
    WaitChrThread(0xD, 0x1)
    TurnDirection(0xD, 0x8, 400)

    ChrTalk(
        0x101,
        "#004F#5PHey!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F#5PLieutenant Schwarz!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#073F#5PWell, now, if it isn't Sister\x01",
            "Military!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_44DB():

        label("loc_44DB")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_44DB")

    QueueWorkItem2(0x8, 1, lambda_44DB)

    def lambda_44EC():
        OP_8E(0xFE, 0x1D47A, 0x0, 0xBF4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_44EC)
    OP_6D(121320, 0, 1770, 2000)
    WaitChrThread(0xD, 0x1)
    Fade(1000)
    SetChrChipByIndex(0xD, 5)
    TurnDirection(0xD, 0x8, 400)
    OP_0D()

    ChrTalk(
        0xD,
        (
            "#465FIt's a pleasure to meet you all.\x02\x03",
            "#460FI am Royal Guardsman sub-commander, \x01",
            "Lieutenant Julia Schwarz.\x02\x03",
            "The Royal Guardsman are here at\x01",
            "your disposal for this operation.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(122540, 0, 820, 0)
    OP_67(0, 6320, -10000, 0)
    OP_6B(1200, 0)
    OP_6C(315000, 0)
    OP_6E(678, 0)
    OP_44(0xB, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xC, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x108, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0xD, 0xFF)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xC, 124600, 0, -2300, 340)
    SetChrPos(0x9, 124530, 0, -1010, 319)
    SetChrPos(0xB, 125530, 0, -570, 294)
    SetChrPos(0xA, 125290, 0, 750, 284)
    SetChrPos(0x101, 120540, 0, 1210, 75)
    SetChrPos(0x102, 120520, 0, 190, 45)
    SetChrPos(0x108, 120880, 0, -1300, 64)
    SetChrPos(0x8, 122790, 0, 1800, 180)
    SetChrPos(0xD, 122810, 0, -1980, 7)
    TurnDirection(0xC, 0xD, 0)
    TurnDirection(0x9, 0xD, 0)
    TurnDirection(0xB, 0xD, 0)
    TurnDirection(0xA, 0xD, 0)
    TurnDirection(0x101, 0xD, 0)
    TurnDirection(0x102, 0xD, 0)
    TurnDirection(0x108, 0xD, 0)
    TurnDirection(0x8, 0xD, 0)
    TurnDirection(0xD, 0x8, 0)
    Sleep(500)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#760FUnderstood. Your participation\x01",
            "will be most invaluable.\x02\x03",
            "I count nine soldiers in your\x01",
            "squad, including yourself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#460FMy remaining troops are incognito,\x01",
            "stationed all throughout the city.\x02\x03",
            "I can assemble them within\x01",
            "the hour.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F#6PThat's great, but Lieutenant Schwarz...\x02\x03",
            "How did you know we were going\x01",
            "to try to save the hostages?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FWe tried to find you at the\x01",
            "cathedral and tell you, but\x01",
            "you had already disappeared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#465FDid you? My apologies.\x02\x03",
            "#460FAll I knew was that you had\x01",
            "accepted the queen's mission.\x02\x03",
            "I found out last night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F#6PLast night?!\x02\x03",
            "We'd only just met with the\x01",
            "queen last night ourselves!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#461FYes, I'm aware of that.\x02\x03",
            "We have sources for...military\x01",
            "intelligence of this sort.\x02\x03",
            "All that matters now is that Her Highness\x01",
            "gave us the order to assist. And we are\x01",
            "happy to do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F#6PSources? I want sources! Can\x01",
            "I share some of yours?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#464FUmm...I...I don't...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F#6PLet's leave it at no, Estelle.\x02\x03",
            "More importantly, the Guardsmen's assistance\x01",
            "will give us the extra forces we need to fill\x01",
            "the ambush and support teams.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#761FIndeed. With this additional manpower,\x01",
            "I believe our chances of success have\x01",
            "increased exponentially.\x02\x03",
            "And with extra manpower secured, we should\x01",
            "start deciding on the teams immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#465FRoger that.\x02\x03",
            "#462FYou need two decoy teams, right? \x01",
            "I believe five of my troops should\x01",
            "be sufficient for one of them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#820FYeah, I'd say those Royal Guard\x01",
            "uniforms should definitely catch\x01",
            "their attention!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#460FMy thoughts exactly.\x02\x03",
            "We'll target the Intelligence Division's\x01",
            "aerial squadron, stationed just on the\x01",
            "outskirts of the Erbe Scenic Route.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#580F#6PWait a sec... Aerial squadron?!\x01",
            "You don't mean...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012FI'm afraid she does. It's on\x01",
            "the Scenic Route's outskirts?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#072F#6PNow that you mention it, there is\x01",
            "a stretch of land out there that's\x01",
            "been completely blockaded...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#460FAccording to my intelligence,\x01",
            "there is only a skeleton crew\x01",
            "of guards stationed there.\x02\x03",
            "If we attack, they will have\x01",
            "no alternative but to call\x01",
            "the villa for reinforcements.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#814FOoh, I get it! That's some\x01",
            "good decoying, right there!\x02\x03",
            "#850FAnd then when the reinforcements show up,\x01",
            "the ambush team pops in and takes 'em all\x01",
            "out, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#840F#2PWe should form that ambush team, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#821FI knew all those years of\x01",
            "hunting down monsters in the\x01",
            "bush'd pay off one day!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2P#830FAnd we've got a gunner, too. We'll be able to\x01",
            "handle this, no problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#764FAll right. Two teams locked\x01",
            "down.\x02\x03",
            "#760FNow for rescue and decoy 2...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#460FI think the second decoy team\x01",
            "should also be comprised of my\x01",
            "Royal Guardsmen.\x02\x03",
            "The Special Ops will definitely\x01",
            "drop their guards more readily\x01",
            "to apprehend them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F#6PSo that leaves us...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F...for the rescue team.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x108, 0x101, 400)

    ChrTalk(
        0x108,
        (
            "#070F#6PAll of the other teams will be acting to provide\x01",
            "cover for us. Ours will be the most important\x01",
            "assignment on the field, by far.\x02\x03",
            "This is no game. You're playing an actual\x01",
            "role in a crucial turning point for our\x01",
            "history. Make sure you're up to the task!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007F#6PSheesh... No pressure...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 400)

    def lambda_5384():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_5384)
    TurnDirection(0x9, 0x101, 400)

    def lambda_5399():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_5399)
    TurnDirection(0xD, 0x101, 400)

    ChrTalk(
        0xD,
        (
            "#461FHeh. There's no need to worry.\x01",
            "We will persevere. History\x01",
            "favors the just.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2P#831FBesides... You guys are the Grancel\x01",
            "Martial Arts Competition Champions!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#841F#2PAnd we'll be the ones keeping the\x01",
            "majority of the enemy force busy.\x02\x03",
            "#2PHopefully, all you'll need to worry\x01",
            "about are the hostages!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F#6PJulia...Elnan...Zane...I...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#019F'We,' Estelle. The word you're\x01",
            "looking for is 'we.'\x02\x03",
            "We CAN do this. And we will.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F#6P...You're right.\x02\x03",
            "You are so, SO right! We're\x01",
            "gonna kick some Special Ops'\x01",
            "special ASSES!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#071F#6PThat's the spirit!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#764FAnd that's the plan.\x02",
    )

    CloseMessageWindow()

    def lambda_561B():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_561B)

    def lambda_5629():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_5629)

    def lambda_5637():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_5637)

    def lambda_5645():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_5645)

    def lambda_5653():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_5653)

    def lambda_5661():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5661)

    def lambda_566F():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_566F)
    TurnDirection(0x101, 0x8, 400)
    Sleep(400)

    ChrTalk(
        0x8,
        (
            "#760FThe operation will begin at\x01",
            "nightfall. We'll use the dark\x01",
            "for cover.\x02\x03",
            "Once the operation begins, you\x01",
            "won't have any opportunity to\x01",
            "return to the city.\x02\x03",
            "So if you still have loose ends\x01",
            "to tie up, speak now...or forever\x01",
            "hold your peace.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006FMan. This is getting pretty\x01",
            "real...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#465FI will ensure that Her Highness\x01",
            "is made aware of the plan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FAll right, everyone. Tonight.\x01",
            "Here. Got it?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x101, 119650, 0, 1610, 0)
    SetChrPos(0x102, 119650, 0, 1610, 0)
    SetChrPos(0x108, 119650, 0, 1610, 0)
    SetChrPos(0x8, -4460, 0, 960, 90)
    SetChrPos(0x9, 120230, 0, -2360, 90)
    SetChrPos(0xC, 122900, 0, -2350, 270)
    SetChrPos(0xB, 121650, 0, -3900, 0)
    SetChrPos(0xA, 121680, 0, -830, 180)
    OP_43(0x9, 0x0, 0x0, 0x2)
    OP_43(0xC, 0x0, 0x0, 0x2)
    OP_43(0xB, 0x0, 0x0, 0x2)
    OP_43(0xA, 0x0, 0x0, 0x2)
    SetChrFlags(0xD, 0x80)
    OP_6D(119650, 0, 1610, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Jump("loc_9416")

    label("loc_5925")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6A75")
    EventBegin(0x0)
    OP_A2(0x628)
    OP_28(0x48, 0x1, 0x80)
    Fade(1000)
    OP_6D(-4030, 0, 1100, 0)
    SetChrPos(0x101, -2590, 0, 280, 270)
    SetChrPos(0x102, -2590, 0, 1220, 270)
    SetChrSubChip(0x8, 0)
    OP_8C(0x8, 90, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDF, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5BE8")

    ChrTalk(
        0x8,
        (
            "#761FEstelle. Joshua. I offer my\x01",
            "congratulations on advancing\x01",
            "to the championship bout.\x02\x03",
            "It is a shame to hear of Kurt's\x01",
            "loss, but I hear it was a very\x01",
            "good match.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006FYeah, it was pretty intense.\x02\x03",
            "#007FI wouldn't go patting us on the\x01",
            "back just yet, though. We weren't\x01",
            "better than Kurt. Not by a selge!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FTrue. We just got lucky.\x02\x03",
            "We had Zane, along with Olivier's\x01",
            "guns and magic to cover for our\x01",
            "mistakes.\x02\x03",
            "They're the only reason we've made\x01",
            "it as far as we have.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#761FYou two are very humble. A rare\x01",
            "quality, these days.\x02\x03",
            "#760FBy the way, have you learned any\x01",
            "more information?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C73")

    label("loc_5BE8")


    ChrTalk(
        0x8,
        (
            "#760FEstelle. Joshua. How did your\x01",
            "meeting go with the reporter\x01",
            "from the Liberl News?\x02\x03",
            "Did you get any valuable leads\x01",
            "or information?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C73")


    ChrTalk(
        0x102,
        "#012FWell...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Joshua explained the details of Nial's findings to Elnan.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(
        0x8,
        (
            "#763FSo...2nd Lieutenant Lorence is\x01",
            "part of a jaeger corps...\x02\x03",
            "#764FOr more specifically, the\x01",
            "jaeger corps known as Jester.\x02\x03",
            "First I've heard of that name,\x01",
            "definitely. I'd best look it up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014FDo the guild and jaeger corps\x01",
            "ever work together?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#762FNot at all. If anything, we consider\x01",
            "one another to be business rivals.\x02\x03",
            "We make it our business not to interfere in\x01",
            "matters of state, you see...whereas the jaegers\x01",
            "largely revel in such matters.\x02\x03",
            "They're often employed in border disputes, and\x01",
            "have some quite...opposing viewpoints with us\x01",
            "regarding the safety of the common man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007FThey don't sound very nice.\x02\x03",
            "#505FSo I take it there's no chance\x01",
            "of getting any information on\x01",
            "this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#760FI...wouldn't say no chance. With a bit\x01",
            "of cloak and dagger, I might be able to\x01",
            "find the information you seek.\x02\x03",
            "It would take several days to gather the\x01",
            "necessary intel, however, so you wouldn't\x01",
            "have it before the championship...\x02\x03",
            "Is that...all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006FChampionship, shmampionship. This has\x01",
            "nothing to do with the competition.\x01",
            "So yeah, if you'd please...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#015FThank you, Elnan.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#764FAlso, regarding the colonel's hunt for\x01",
            "Princess Klaudia's future husband...\x02\x03",
            "We've uncovered a few morsels of\x01",
            "information which may have some\x01",
            "connection.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004FUh, okay...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#760FA member of the Imperial royal family will be\x01",
            "arriving in Grancel during the Queen's Birthday\x01",
            "Celebration.\x02\x03",
            "We don't know their name...but we do know this is the\x01",
            "first time someone from the family has come to Liberl\x01",
            "since the war ten years ago, so this is fairly significant news.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FI see. You're right that it does\x01",
            "seem connected with talk of\x01",
            "Princess Klaudia's marriage...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505FI don't actually know a thing\x01",
            "about the Imperial royal family.\x02\x03",
            "I mean, the only Imperial I've ever\x01",
            "even met is Olivier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#765FThe princess has just celebrated \x01",
            "her sixteenth birthday.\x02\x03",
            "It seems much too early for her\x01",
            "to be married. I suspect there\x01",
            "may be politics at work here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004FWhoa, sixteen?! Geez, we're only\x01",
            "sixteen ourselves!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015FIt is the appropriate age for\x01",
            "a young lady to make her 'debut'\x01",
            "in high society.\x02\x03",
            "#013FBut unless we've reverted to a\x01",
            "more repressed time, it is much,\x01",
            "MUCH too soon for marriage...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#762FIndeed. As I said, I suspect\x01",
            "there is a political motive to\x01",
            "this push for wedlock...\x02\x03",
            "And finding that motive will\x01",
            "no doubt prove to be a most\x01",
            "valuable endeavor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006FGotcha.\x02\x03",
            "If we can earn that invite to\x01",
            "the castle, we'd be able to\x01",
            "investigate much more easily.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FThen we need to secure a win\x01",
            "in tomorrow's championship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#764FHmmm... As dangerous as this\x01",
            "may be...\x02\x03",
            "...I've got something for you.\x01",
            "Here.\x02",
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
            "Grancel Sewer Key B\x07\x00",
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3E(0x36E, 1)

    ChrTalk(
        0x101,
        "#004FWh-What the heck is THIS to?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#760FThe sewers. We always keep a few on\x01",
            "hand at the capital branch. Never know\x01",
            "when they might come in handy.\x02\x03",
            "This one should open one of the access\x01",
            "grates near the Grand Arena.\x02\x03",
            "There are some pretty strong monsters\x01",
            "living down there, so I figured it might\x01",
            "make for a suitable training ground.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001FBring it!\x02\x03",
            "We could totally use the warm-up!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FThank you, Elnan.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#760FI'm just doing my job.\x02\x03",
            "Make sure you don't head down there\x01",
            "without some backup, though. If it's\x01",
            "just the two of you, you're toast.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006FNo problem there!\x02\x03",
            "We'll head on down with Zane and\x01",
            "*sigh* Olivier after we meet up\x01",
            "with them tomorrow.\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_21()
    NewScene("ED6_DT01/T4150   ._SN", 103, 0, 0)
    IdleLoop()
    Jump("loc_9416")

    label("loc_6A75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_743F")
    EventBegin(0x0)
    OP_A2(0x61F)
    OP_28(0x47, 0x1, 0x200)
    Fade(1000)
    OP_6D(-4030, 0, 1100, 0)
    SetChrPos(0x101, -2590, 0, 280, 270)
    SetChrPos(0x102, -2590, 0, 1220, 270)
    SetChrSubChip(0x8, 0)
    OP_8C(0x8, 90, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#761FEstelle! Joshua!\x02\x03",
            "Congratulations on your victory!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506FThank you, thank you.\x02\x03",
            "#501FWait... How'd you know already?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#760FGrant already reported in.\x02\x03",
            "So, how was it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FHonestly...\x02\x03",
            "It felt more like surviving\x01",
            "than actually winning.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Joshua explained that there were Sky Bandit and Special Op teams.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(
        0x8,
        (
            "#762FI see... I'd heard that the\x01",
            "Sky Bandits were given special\x01",
            "permission to participate...\x02\x03",
            "But I must admit, I'm surprised to hear\x01",
            "about the Special Ops. Particularly\x01",
            "that their leader is so powerful!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007FThe team was pretty tough, but\x01",
            "that commander was, like...on a\x01",
            "different level altogether.\x02\x03",
            "#002FHe moved like a cat, and was\x01",
            "swinging that huge sword around\x01",
            "like it was a toy.\x02\x03",
            "I could barely believe he was\x01",
            "human, the way he was fighting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013FYeah... What she said.\x02\x03",
            "#012FElnan...\x02\x03",
            "What do you know about 2nd Lieutenant\x01",
            "Lorence's personal history?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#765FNothing, I'm afraid.\x02\x03",
            "The Intelligence Division is new, and Colonel\x01",
            "Richard suppressed all information regarding\x01",
            "them since their official inception.\x02\x03",
            "That includes information on\x01",
            "the lieutenant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#013FDrat...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#505F#1P...Joshua?\x02\x03",
            "You seem pretty caught up with\x01",
            "that guy in red.\x02\x03",
            "Is there something we should be\x01",
            "watching out for?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F#2PNo... We just need to know who\x01",
            "we're facing. That's all.\x02\x03",
            "...Anything that can give us\x01",
            "an edge in the tournament.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F#1PAh. Good point! Knowing your\x01",
            "enemy is the best way to beat\x01",
            "him, after all!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#760FAh, actually... This doesn't concern\x01",
            "the lieutenant, exactly...\x02\x03",
            "Today at noon, a military patrol\x01",
            "vessel arrived at the landing\x01",
            "port.\x02\x03",
            "Its passenger was the colonel's\x01",
            "right-hand woman, Captain Amalthea.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)
    OP_8C(0x102, 270, 400)

    ChrTalk(
        0x102,
        "#014FThat IS news...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009FCaptain Amalthea... Is that that\x01",
            "sneaky, fox-faced woman?\x02\x03",
            "That witch who used Tita to\x01",
            "threaten the professor?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#760FShe's traveling through all\x01",
            "of the major cities.\x02\x03",
            "Her arrival was unexpected, and\x01",
            "caused all civilian airship lines\x01",
            "to run late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#509FYeah, that doesn't bode well...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015FA tour of the major cities?\x02\x03",
            "Sounds like a cover for her to\x01",
            "hunt down the professor...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#760FWe've got all branches investigating\x01",
            "her trip very carefully.\x02\x03",
            "We'll let you know as soon as\x01",
            "we learn anything.\x02\x03",
            "You two just focus on the tournament\x01",
            "for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006FYou bet.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FThanks so much for all your help.\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Jump("loc_9416")

    label("loc_743F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7778")
    OP_A2(0x60A)

    ChrTalk(
        0x101,
        "#004FWait... Joshua...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#501FWasn't Kloe coming to the \x01",
            "capital right about now?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010FNow that you mention it, she did\x01",
            "say she'd meet us before the\x01",
            "Birthday Celebration started.\x02\x03",
            "She should definitely be here\x01",
            "by now.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_754F():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_754F)
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(
        0x101,
        (
            "#006FElnan...\x02\x03",
            "There wasn't a girl about our\x01",
            "age named Kloe who came around\x01",
            "asking for us, was there?\x02\x03",
            "We'd promised to meet up here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#763FKloe, you say?\x02\x03",
            "No, I'm afraid no one by that\x01",
            "name has been here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007FAww, raspberries.\x02\x03",
            "#505FMaybe we should've asked where\x01",
            "she was staying...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FShe mentioned some rich relatives.\x02\x03",
            "Though that's not much of a\x01",
            "lead, I suppose...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#760FI'm sure she's simply running\x01",
            "late, and will try to contact\x01",
            "you shortly.\x02\x03",
            "If she comes by, I'll be sure\x01",
            "to let you know immediately.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9416")

    label("loc_7778")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_8092")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDF, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDF, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7EBF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDF, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E0A")
    OP_A2(0x6FD)

    ChrTalk(
        0x8,
        (
            "#762FOh, and not to dampen the mood\x01",
            "of this joyous festival, but\x01",
            "I have further news...\x02\x03",
            "Specifically, I've learned a few\x01",
            "things about Jester.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004FOh... That!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012FThat's the corps 2nd Lieutenant Lorence\x01",
            "belonged to before joining the Intelligence\x01",
            "Division, correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#762FIndeed.\x02\x03",
            "They were a small team that primarily\x01",
            "operated from a small, autonomous state\x01",
            "on the outskirts of Erebonia.\x02\x03",
            "They were quite skilled--as they'd\x01",
            "have to be, to call themselves a jaeger corps.\x02\x03",
            "But about six months ago, the\x01",
            "entire group vanished.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#580FThe...entire group? You mean...\x01",
            "everyone?\x02\x03",
            "Were they, like, wiped out\x01",
            "in some border skirmish?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#765FNo. There are no records of them\x01",
            "being in battle at the time.\x02\x03",
            "In total, over one hundred people\x01",
            "disappeared, and not a soul knows\x01",
            "what happened to them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505F...Yeowza. That's creepy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F...\x02\x03",
            "#015FThat timetable overlaps with\x01",
            "Lorence joining the Intelligence\x01",
            "Division.\x02\x03",
            "#012FAre the two events related?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#764FWe're investigating that.\x02\x03",
            "We might find out more from\x01",
            "the Royal Army, actually.\x02\x03",
            "#760FAnd there's one more thing...\x02\x03",
            "It sounds like the plans for a member of the\x01",
            "Imperial family to attend the Birthday Celebration\x01",
            "were canceled.\x02\x03",
            "The only Erebonian representative at the ceremony\x01",
            "will be a simple ambassador, much like in previous\x01",
            "years.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501FOkay...\x02\x03",
            "Weren't they supposed to be a marriage\x01",
            "candidate for Kloe or something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FYeah. An arranged marriage to help\x01",
            "cement Duke Dunan's ascendancy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#760FThe queen herself put a stop to the\x01",
            "marriage talks, from what I've heard.\x02\x03",
            "I suppose that's why the royal family\x01",
            "canceled their visit altogether.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7EBC")

    label("loc_7E0A")


    ChrTalk(
        0x8,
        (
            "#760FThe Royal Army will be out in force\x01",
            "during the festivities-- but the other\x01",
            "bracers should be around as well.\x02\x03",
            "Check the bars, shops and inns.\x01",
            "You're sure to find them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7EBC")

    Jump("loc_808F")

    label("loc_7EBF")

    OP_A2(0x6FC)

    ChrTalk(
        0x8,
        (
            "#760FWell, if it isn't Estelle and\x01",
            "Joshua...\x02\x03",
            "We don't have any new assignments\x01",
            "today.\x02\x03",
            "#761FYou two may feel free to go on out\x01",
            "and enjoy your date.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#503FD-D-D-DATE?! Who's on a date?!\x02\x03",
            "We are SO not dating yet!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014FUhh... 'yet'?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#506F...At all! I meant AT ALL!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#760FThe Royal Army will be out in force\x01",
            "during the festivities-- but the other\x01",
            "bracers should be around as well.\x02\x03",
            "Check the bars, shops and inns.\x01",
            "You're sure to find them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_808F")

    Jump("loc_9416")

    label("loc_8092")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_827F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_8172")

    ChrTalk(
        0x8,
        (
            "#762FI heard about Princess Klaudia's\x01",
            "request from a member of the Royal\x01",
            "Guard.\x02\x03",
            "#760FDon't worry about us. Even if the Royal\x01",
            "Army were to get in, I'll have no trouble\x01",
            "pleading ignorance. Convincingly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_827C")

    label("loc_8172")

    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "#762FJoshua! Zane! I'm glad to see\x01",
            "the two of you are safe!\x02\x03",
            "I heard about Princess Klaudia's\x01",
            "request from a member of the Royal\x01",
            "Guard.\x02\x03",
            "#760FDon't worry about us. Even if the Royal\x01",
            "Army were to get in, I'll have no trouble\x01",
            "pleading ignorance. Convincingly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_827C")

    Jump("loc_9416")

    label("loc_827F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_8481")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8345")

    ChrTalk(
        0x8,
        (
            "#760FIt looks like all of the bracers\x01",
            "have been assembled.\x02\x03",
            "Now, if we should hear from the Royal\x01",
            "Guardsman or your reporter, things would\x01",
            "go much more smoothly...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_847E")

    label("loc_8345")


    ChrTalk(
        0x8,
        (
            "#760FThere are four other bracers in\x01",
            "the capital at present: Grant,\x01",
            "Kurt, Carna and Anelace.\x02\x03",
            "Check the bars, shops and inns.\x01",
            "You're sure to find them.\x02\x03",
            "When you do, tell them they\x01",
            "need to convene here.\x02\x03",
            "Now, if we should hear from the Royal\x01",
            "Guardsman or your reporter, things would\x01",
            "go much more smoothly...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_847E")

    Jump("loc_9416")

    label("loc_8481")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_87CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_84EA")

    ChrTalk(
        0x8,
        (
            "#760FWell done in the arena, and good\x01",
            "luck tonight at the victory banquet\x01",
            "as well.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_87CC")

    label("loc_84EA")

    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "#761FI've already heard. Congratulations\x01",
            "on your victory!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001FThanks, Elnan!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#760FKurt tells me it was quite\x01",
            "a sight to behold!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505FIt...sure was, I guess!\x02\x03",
            "I don't think we'd be able to take\x01",
            "them in another fight, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#015FNot easily, at any rate.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#761FSome say victory is equal parts effort and\x01",
            "luck, but it seems that the two of you have\x01",
            "discovered some secret third influence.\x02\x03",
            "With each passing day, one's skills are further\x01",
            "honed. As time passes, you'll grow into that\x01",
            "victory, and realize you truly did earn it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006FYou think so? Yay! I really\x01",
            "like your pep talks!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#760FWell done in the arena, and good\x01",
            "luck tonight at the victory banquet\x01",
            "as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006FThanks. We'll need it!\x02",
    )

    CloseMessageWindow()

    label("loc_87CC")

    Jump("loc_9416")

    label("loc_87CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_8983")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_889C")

    ChrTalk(
        0x8,
        (
            "#760FDid you get a chance to go\x01",
            "into the sewers yesterday?\x01",
            "...Egads, what a question!\x02\x03",
            "It sounds strange, I know, but it\x01",
            "really is a fine place for you to\x01",
            "brush up on your technique.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8980")

    label("loc_889C")

    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "#760FGood morning. Today is the big\x01",
            "day!\x02\x03",
            "Did you get a chance to go\x01",
            "into the sewers yesterday?\x01",
            "...Egads, what a question!\x02\x03",
            "It sounds strange, I know, but it\x01",
            "really is a fine place for you to\x01",
            "brush up on your technique.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8980")

    Jump("loc_9416")

    label("loc_8983")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 0)), scpexpr(EXPR_END)), "loc_8ABE")

    ChrTalk(
        0x8,
        (
            "#760FThat key I gave you will open\x01",
            "the access grate near the Grand\x01",
            "Arena.\x02\x03",
            "There are some pretty strong monsters\x01",
            "living down there, so I figured it might\x01",
            "make for a suitable training ground.\x02\x03",
            "Make sure you don't head down there\x01",
            "without some backup, though. If it's\x01",
            "just the two of you, you're toast.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9416")

    label("loc_8ABE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_8F0B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDF, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8E8B")
    OP_A2(0x6FA)

    ChrTalk(
        0x8,
        (
            "#761FEstelle. Joshua. I offer my\x01",
            "congratulations on advancing\x01",
            "to the championship bout.\x02\x03",
            "It is a shame to hear of Kurt's\x01",
            "loss, but I hear it was a very\x01",
            "good match.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006FYeah, it was pretty intense.\x02\x03",
            "#007FI wouldn't go patting us on the\x01",
            "back just yet, though. We weren't\x01",
            "better than Kurt. Not by a selge!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FTrue. We just got lucky.\x02\x03",
            "We had Zane, along with Olivier's\x01",
            "guns and magic to cover for our\x01",
            "mistakes.\x02\x03",
            "They're the only reason we've made\x01",
            "it as far as we have.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#761FYou two are very humble. A rare\x01",
            "quality, these days.\x02\x03",
            "#760FBy the way, have you learned any\x01",
            "more information?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006FWell, we talked a reporter from the Liberl News\x01",
            "into collecting some intel on our behalf...er...\x01",
            "behalves? On my behalf and his be--... For us.\x02\x03",
            "We were just about to check\x01",
            "in with him, and see what he\x01",
            "found out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#763FThe Liberl News... You have friends\x01",
            "in relatively high places, it would\x01",
            "seem!\x02\x03",
            "#761FI look forward to your report.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8F08")

    label("loc_8E8B")


    ChrTalk(
        0x8,
        (
            "#763FThe Liberl News... You have friends\x01",
            "in relatively high places, it would\x01",
            "seem!\x02\x03",
            "#761FI look forward to your report.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8F08")

    Jump("loc_9416")

    label("loc_8F0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_9047")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_8F8B")

    ChrTalk(
        0x8,
        (
            "#760FTextbook tactics won't work,\x01",
            "from here on out. You'll need\x01",
            "to be inventive.\x02\x03",
            "Best of luck out there!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9044")

    label("loc_8F8B")

    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "#760FGood morning, everyone.\x02\x03",
            "Are you ready for the trials\x01",
            "that await you?\x02\x03",
            "Textbook tactics won't work,\x01",
            "from here on out. You'll need\x01",
            "to be inventive.\x02\x03",
            "Best of luck out there!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9044")

    Jump("loc_9416")

    label("loc_9047")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_90E1")

    ChrTalk(
        0x8,
        (
            "#760FWe're keeping an eye on Captain\x01",
            "Amalthea's movements-- with some\x01",
            "help from the other branches.\x02\x03",
            "You two just focus on the\x01",
            "tournament.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9416")

    label("loc_90E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_92B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_9179")

    ChrTalk(
        0x8,
        (
            "#760FThe match isn't until this afternoon,\x01",
            "so you have a bit of free time.\x02\x03",
            "You might want to go out and\x01",
            "stretch your legs a bit.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_92B3")

    label("loc_9179")

    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "#760FGood morning! Today, it begins.\x01",
            "Are you ready?\x02\x03",
            "Right now, there are a large\x01",
            "number of soldiers about, and\x01",
            "very few requests on the board.\x02\x03",
            "So stay focused on the tournament!\x02\x03",
            "The match isn't until this afternoon,\x01",
            "so you have a bit of free time.\x02\x03",
            "You might want to go out and\x01",
            "stretch your legs a bit.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_92B3")

    Jump("loc_9416")

    label("loc_92B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_93B6")

    ChrTalk(
        0x8,
        (
            "#760FZane is currently staying at\x01",
            "the Calvardian embassy, located\x01",
            "in the East Block.\x02\x03",
            "He IS a renowned bar-hopper, however, so\x01",
            "make sure to check anyplace that offers\x01",
            "spirits...as well as all the gutters.\x02\x03",
            "The bar's along the northern road.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9416")

    label("loc_93B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_9416")

    ChrTalk(
        0x8,
        (
            "#760FGrancel Castle is directly\x01",
            "north of the main road.\x02\x03",
            "Good luck in your pursuit!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9416")

    TalkEnd(0x8)
    Return()

    # Function_12_2E09 end

    def Function_13_941A(): pass

    label("Function_13_941A")

    EventBegin(0x0)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xC, -2590, 0, 1600, 270)
    SetChrPos(0x9, -1500, 0, 770, 270)
    SetChrPos(0xB, -1770, 0, -310, 270)
    SetChrPos(0xA, -2590, 0, -610, 270)
    OP_4A(0xC, 255)
    OP_4A(0x9, 255)
    OP_4A(0xB, 255)
    OP_4A(0xA, 255)
    OP_4A(0x8, 255)
    OP_6D(-4030, 0, 1100, 0)
    OP_6B(2800, 0)
    SetChrPos(0x101, 30, -250, -4920, 315)
    SetChrPos(0x102, 1120, -250, -4920, 315)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#760FMay fortune smile upon you.\x02\x03",
            "With everyone together, I think\x01",
            "we may just succeed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#821FHeh heh...\x01",
            "Now you've got it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#830FIf you're participating, I expect\x01",
            "nothing less than everything\x01",
            "you've got.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#2P#850FRight! We can't let those\x01",
            "army goons beat us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#840FNow, then...\x01",
            "We ought to get going soon.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xC,
        "#840F...Hm?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 400)

    def lambda_964A():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_964A)

    def lambda_9658():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_9658)

    def lambda_9666():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_9666)

    def lambda_9674():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_9674)

    def lambda_9682():

        label("loc_9682")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_9682")

    QueueWorkItem2(0x101, 1, lambda_9682)

    def lambda_9693():

        label("loc_9693")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_9693")

    QueueWorkItem2(0x102, 1, lambda_9693)

    def lambda_96A4():
        OP_8E(0xFE, 0xFFFFF97A, 0x0, 0xFFFFF7FE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_96A4)

    def lambda_96BF():
        OP_8E(0xFE, 0xFFFFFDC6, 0x0, 0xFFFFF8E4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_96BF)
    OP_6D(-2770, 0, 100, 2000)
    WaitChrThread(0x101, 0x2)

    ChrTalk(
        0x101,
        "#008FUmm...\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 0x2)

    ChrTalk(
        0x102,
        "#010FPardon the intrusion...\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8E(0x9, 0xFFFFFEE8, 0x0, 0xFFFFFE3E, 0xBB8, 0x0)
    TurnDirection(0x9, 0x102, 400)

    ChrTalk(
        0x9,
        (
            "#831F#2PWell, if it isn't Estelle\x01",
            "and Joshua!\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)

    def lambda_979A():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_979A)
    TurnDirection(0x101, 0x9, 400)

    ChrTalk(
        0x101,
        (
            "#501FOh...Carna!\x01",
            "Wow, fancy meeting you here!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 0)), scpexpr(EXPR_END)), "loc_9868")

    ChrTalk(
        0xB,
        (
            "#820F#2PAh, yes. And we met once during\x01",
            "the whole Sky Bandit incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#850F#1PYou were the rookies with\x01",
            "Schera, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_98E5")

    label("loc_9868")


    ChrTalk(
        0xB,
        (
            "#820F#2PAh, yes. And we met once during\x01",
            "the whole Sky Bandit incident.\x02\x03",
            "#2PYou were the rookies with\x01",
            "Scherazard, right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_98E5")


    ChrTalk(
        0x102,
        (
            "#010FLong time no see.\x02\x03",
            "What brings you all to\x01",
            "Grancel?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#760FI'll field that one.\x02\x03",
            "They have to hurry,\x01",
            "or else they'll be late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#830F#2PWhoops...\x01",
            "You're right.\x02\x03",
            "Sorry, you two.\x01",
            "We'll talk later!\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x9, 0x1, 0x0, 0xE)

    ChrTalk(
        0xB,
        "#820F#2PWe've got to be going.\x02",
    )

    CloseMessageWindow()
    OP_43(0xB, 0x1, 0x0, 0xE)

    ChrTalk(
        0xA,
        "#811F#3PSeeya later, rookies!\x02",
    )

    CloseMessageWindow()
    OP_43(0xA, 0x1, 0x0, 0xE)

    ChrTalk(
        0xC,
        "#840FPardon me...\x02",
    )

    CloseMessageWindow()
    OP_43(0xC, 0x1, 0x0, 0xE)

    def lambda_9A37():

        label("loc_9A37")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_9A37")

    QueueWorkItem2(0x101, 1, lambda_9A37)

    def lambda_9A48():

        label("loc_9A48")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_9A48")

    QueueWorkItem2(0x102, 1, lambda_9A48)

    def lambda_9A59():

        label("loc_9A59")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_9A59")

    QueueWorkItem2(0x8, 1, lambda_9A59)
    WaitChrThread(0xC, 0x1)
    Sleep(300)
    OP_22(0x7, 0x0, 0x64)
    Sleep(700)

    ChrTalk(
        0x101,
        (
            "#004F*sigh*... It must be so awesome\x01",
            "to be a full-fledged bracer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FIndeed...\x01",
            "They all look pretty tough.\x02\x03",
            "But you were talking about something\x01",
            "when we came in... Was that what I\x01",
            "think it was?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#761FIndeed so.\x02\x03",
            "They're all leaving to participate\x01",
            "in the big fighting tournament,\x01",
            "the Martial Arts Competition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001FWhoa...\x02",
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x101, 0x8, 400)

    def lambda_9BF6():
        OP_6D(-4030, 0, 1100, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_9BF6)

    def lambda_9C0E():
        OP_8E(0xFE, 0xFFFFF5E2, 0x0, 0x118, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9C0E)

    def lambda_9C29():

        label("loc_9C29")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_9C29")

    QueueWorkItem2(0x101, 1, lambda_9C29)
    TurnDirection(0x102, 0x8, 400)
    OP_8E(0x102, 0xFFFFF95C, 0x0, 0x474, 0xBB8, 0x0)

    def lambda_9C55():
        OP_8E(0xFE, 0xFFFFF5E2, 0x0, 0x4C4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9C55)

    def lambda_9C70():

        label("loc_9C70")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_9C70")

    QueueWorkItem2(0x102, 1, lambda_9C70)
    WaitChrThread(0x101, 0x3)

    ChrTalk(
        0x101,
        (
            "#008FErr, sorry!\x02\x03",
            "I'm Estelle Bright, currently\x01",
            "of the Zeiss branch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FAnd I'm Joshua Bright,\x01",
            "of the same affiliation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#760FI'm Elnan.\x01",
            "I'm with the Grancel branch.\x02\x03",
            "Miss Kilika got in touch with\x01",
            "me and informed me that you\x01",
            "two would be coming soon.\x02\x03",
            "Could I get you to go ahead and\x01",
            "change your affiliation now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FCertainly.\x02",
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
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
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(
        0x8,
        (
            "#761FExcellent.\x02\x03",
            "I bid you welcome to the Grancel\x01",
            "branch of the Bracer Guild.\x02\x03",
            "#760FPersonally, I've been looking\x01",
            "quite forward to your arrival.\x02\x03",
            "You are the children of Cassius,\x01",
            "are you not?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004FUh, yes...\x02\x03",
            "I suppose you know him?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#760FOh, yes, I'm ever in his debt.\x02\x03",
            "Is it true that he set out on\x01",
            "a journey from which he has not\x01",
            "yet returned?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007FYeah...\x02\x03",
            "He hasn't been home in quite some\x01",
            "time. He did write us a letter...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F...but he failed to mention\x01",
            "where he was, or what he was\x01",
            "doing.\x02\x03",
            "We've traveled everywhere from\x01",
            "Rolent to Zeiss, but we've heard\x01",
            "no news of his whereabouts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#762FHmm... Which, I suppose, makes\x01",
            "it unlikely that he's still in\x01",
            "the country.\x02\x03",
            "#764FThat's a pity...\x02\x03",
            "The army's current counter-terrorism\x01",
            "activities have made it difficult for\x01",
            "us to do our jobs.\x02\x03",
            "With a former soldier like Cassius\x01",
            "among us, I'd hoped it might smooth\x01",
            "things over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#509F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#013F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#763FIs... Is something wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007FWell, actually...\x02\x03",
            "We know what's going on behind\x01",
            "the scenes with all of that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#763FEh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012FLet us tell you everything that\x01",
            "happened with the incident in\x01",
            "Zeiss...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Estelle and Joshua explained what they'd learned in Leiston Fortress, as well\x01",
            "as Professor Russell's request.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        "#763F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004FWhat... What's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#762FN-Nothing...\x01",
            "It's all just a lot to take in.\x02\x03",
            "So Colonel Richard is actually\x01",
            "in control of the Royal Army...\x02\x03",
            "And the counter-terrorism is just a\x01",
            "big farce put on by the Intelligence\x01",
            "Division's special forces?\x02\x03",
            "That's a little difficult to believe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#580FBut it's true!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012FTalk with Kilika at the Zeiss branch,\x01",
            "and she'll confirm our story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#764FIt's all right. It's not that\x01",
            "I don't believe you...\x02\x03",
            "On the contrary, a few pieces of\x01",
            "the puzzle have just fallen into\x01",
            "place, as it were.\x02\x03",
            "#762FHowever, Colonel Richard is\x01",
            "an extremely popular man in\x01",
            "this city...\x02\x03",
            "Though it pains me to say so,\x01",
            "I've been sympathetic to him\x01",
            "all this time.\x02\x03",
            "And the citizens...would never dream\x01",
            "that the colonel could be involved in\x01",
            "any sort of conspiracy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007FI figured as much...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012FThe Intelligence Division has\x01",
            "played everyone for fools.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#762FThe Bracer Guild cannot directly interfere\x01",
            "with military matters...but neither can\x01",
            "we simply stand back and watch.\x02\x03",
            "First of all, did you accept\x01",
            "the professor's request?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006FAbsolutely.\x02\x03",
            "The question is, how do we get\x01",
            "an audience with Her Majesty?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#764FThat is an issue...\x02\x03",
            "Ordinarily, a guild letter alone\x01",
            "would be enough to get you in...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004FWha... Really?!\x02\x03",
            "#001FOh, no waaaay! 侓\x01",
            "No need to worry, then!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#017F#2PEstelle... I really don't think it's\x01",
            "going to be quite that simple.\x02\x03",
            "No matter how you look at it, the Royal\x01",
            "Guards that are supposed to be protecting\x01",
            "the castle are being treated as terrorists.\x02\x03",
            "#012FDo you understand what that means?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#505F#1PWell...\x01",
            "I think it means that...\x02",
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
            "[The castle security won't be as tight?]\x01",       # 0
            "[The queen is in danger?]\x01",                      # 1
            "[That letter would just get crumpled up?]\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_AA8A"),
        (1, "loc_AC4C"),
        (2, "loc_AE16"),
        (SWITCH_DEFAULT, "loc_AFBE"),
    )


    label("loc_AA8A")


    ChrTalk(
        0x102,
        (
            "#015F#2PNo...rather the opposite.\x02\x03",
            "#012FBasically, odds are that the colonel\x01",
            "has a hold on Grancel Castle, just\x01",
            "like he did at Leiston Fortress.\x02\x03",
            "And if we presented that letter,\x01",
            "it'd likely get crumpled up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#005F#1PWha...WHAT?\x02\x03",
            "Then how are we supposed to\x01",
            "get in to talk to the queen?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F#2PWe could possibly sneak in, like\x01",
            "we did at Leiston Fortress...\x02\x03",
            "...but I doubt they'd be so\x01",
            "foolish as to fall for the\x01",
            "same trick twice.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AFBE")

    label("loc_AC4C")


    ChrTalk(
        0x102,
        (
            "#012F#2PIt seems likely...\x02\x03",
            "But what I was getting at is that the colonel\x01",
            "probably has as strong a hold on Grancel\x01",
            "Castle as he did on Leiston Fortress.\x02\x03",
            "And if we presented that letter,\x01",
            "it'd likely get crumpled up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#005F#1PWha...WHAT?\x02\x03",
            "Then how are we supposed to\x01",
            "get in to talk to the queen?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F#2PWe could possibly sneak in, like\x01",
            "we did at Leiston Fortress...\x02\x03",
            "...but I doubt they'd be so\x01",
            "foolish as to fall for the\x01",
            "same trick twice.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AFBE")

    label("loc_AE16")


    ChrTalk(
        0x102,
        (
            "#012F#2PThat's the most likely outcome, yes.\x02\x03",
            "Odds are that the colonel has as\x01",
            "strong a hold on Grancel Castle\x01",
            "as he did on Leiston Fortress.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F#1PUgh... I guess so...\x02\x03",
            "In other words, there's no simple\x01",
            "way we're going to get in touch\x01",
            "with Her Majesty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F#2PWe could possibly sneak in, like\x01",
            "we did at Leiston Fortress...\x02\x03",
            "...but I doubt they'd be so\x01",
            "foolish as to fall for the\x01",
            "same trick twice.\x02",
        )
    )

    CloseMessageWindow()
    OP_2B(0x45, 0x1)
    Jump("loc_AFBE")

    label("loc_AFBE")


    ChrTalk(
        0x101,
        (
            "#007F#1PHmmm...\x02\x03",
            "#006FWell, in that case, why don't\x01",
            "we just try going like normal\x01",
            "and see what happens?\x02\x03",
            "If we play our cards right, we\x01",
            "might get some useful info out\x01",
            "of the gatekeeper.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F#2PFine by me...but just one\x01",
            "piece of advice...\x02\x03",
            "Keep the fact that we want to\x01",
            "see the queen to yourself.\x02\x03",
            "If Colonel Richard gets wind\x01",
            "of it, he'll likely cause us\x01",
            "no end of trouble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F#1POh, okay.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#760FAnd I believe it would be a good idea to\x01",
            "keep this whole matter under wraps for the\x01",
            "time being. We must gather more intel.\x02\x03",
            "Just so you know, the royal castle\x01",
            "is just off the main street,\x01",
            "directly to the north.\x02\x03",
            "Go ahead and get what information \x01",
            "you can, but use the utmost caution.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B282():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B282)
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(
        0x101,
        "#006FYou bet, Mr. Elnan.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FWe'll let you know if we\x01",
            "find anything.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x45, 0x1, 0x80)
    OP_28(0x45, 0x1, 0x100)
    OP_44(0x8, 0x1)
    OP_4B(0x8, 255)
    EventEnd(0x0)
    Return()

    # Function_13_941A end

    def Function_14_B2F8(): pass

    label("Function_14_B2F8")

    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0x42E, 0x0, 0xFFFFFAE2, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFFF4C, 0xFFFFFF06, 0xFFFFE8C2, 0xBB8, 0x0)

    def lambda_B32B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_B32B)
    OP_8E(0xFE, 0xFFFFFF92, 0xFFFFFF06, 0xFFFFE43A, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_14_B2F8 end

    def Function_15_B351(): pass

    label("Function_15_B351")

    EventBegin(0x0)
    OP_6D(-4030, 0, 1100, 0)
    SetChrPos(0x101, -2590, 0, 280, 270)
    SetChrPos(0x102, -2590, 0, 1220, 270)
    OP_4A(0x8, 255)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#760FI see. Yes, Zane requested the\x01",
            "bracers send him some helping\x01",
            "hands...\x02\x03",
            "I hadn't said anything to you guys,\x01",
            "since you're working on that request\x01",
            "from the professor, but...\x02\x03",
            "#761F...thanks to the whim of His\x01",
            "Excellency, we can handle\x01",
            "both tasks at once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506FHeh heh... Nice to see his selfishness\x01",
            "work in our favor for once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FWhat do you think about participating\x01",
            "in the Martial Arts Competition?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#760FWell... I think there is merit in\x01",
            "allowing a skill which is practiced\x01",
            "to be used without restraint.\x02\x03",
            "And with two bracer teams participating,\x01",
            "our chances of gaining access to the castle\x01",
            "are doubled.\x02\x03",
            "You needn't even get the others involved\x01",
            "until and unless you lose. Personally,\x01",
            "I think it's a splendid idea!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001FWoohoo! That's my kind\x01",
            "of encouragement!\x02\x03",
            "#006FSo...any clue where we might\x01",
            "be able to find Zane?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#760FMore often than not, he's in\x01",
            "the bar down the street.\x02\x03",
            "Failing that, he stays at the\x01",
            "Calvard Republic's embassy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FGotcha. Makes sense, since\x01",
            "that's where he's from.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F#2PThe embassy is in the same\x01",
            "block as the arena.\x02\x03",
            "We can stick our heads in the\x01",
            "door at the bar along the way.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#006F#1POkay!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#763FOh, by the way...\x02\x03",
            "Where are you two planning to\x01",
            "stay while you're here?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B890():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B890)
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(
        0x101,
        (
            "#505FHmmm... Well, we could stay\x01",
            "in a hotel...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FIf I'm not mistaken, the northern\x01",
            "block holds the largest hotel in\x01",
            "the entire kingdom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#760FYes, the Hotel Roenbaum.\x02\x03",
            "If I may, allow us to cover the\x01",
            "cost of your room.\x02\x03",
            "The Grancel branch can afford it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004FWhoa, really?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014FThat's too much, honestly.\x01",
            "We couldn't possibly...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#760FI consider it a necessary expense\x01",
            "in the course of completing the\x01",
            "professor's request.\x02\x03",
            "I wish I could provide more...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001FNah, just a room's good by me!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FVery well, then.\x01",
            "We accept your offer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#761FI'll book your room, then.\x02\x03",
            "Just give your name at the\x01",
            "front desk this evening,\x01",
            "and someone will help you.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x611)
    OP_28(0x46, 0x4, 0x2)
    OP_28(0x46, 0x4, 0x4)
    OP_28(0x46, 0x1, 0x1)
    OP_28(0x46, 0x1, 0x2)
    OP_4B(0x8, 255)
    EventEnd(0x0)
    Return()

    # Function_15_B351 end

    def Function_16_BB74(): pass

    label("Function_16_BB74")

    EventBegin(0x0)
    OP_4A(0x8, 255)
    OP_6D(-1330, 0, 750, 0)
    SetChrPos(0x101, -2590, 0, 280, 270)
    SetChrPos(0x102, -2590, 0, 1220, 270)
    SetChrPos(0x108, -1500, 0, 750, 270)
    SetChrSubChip(0x8, 0)
    OP_8C(0x8, 90, 0)
    OP_A2(0x649)
    OP_28(0x4B, 0x4, 0x2)
    OP_28(0x4B, 0x4, 0x4)
    OP_28(0x4B, 0x1, 0x1)
    OP_28(0x4B, 0x1, 0x2)
    OP_28(0x4B, 0x1, 0x4)
    OP_28(0x4B, 0x1, 0x8)
    FadeToBright(2000, 0)
    OP_6D(-3330, 0, 750, 2000)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#764FI understand the situation...\x02\x03",
            "#760FYou've both performed admirably.\x02\x03",
            "I'm amazed that you were able to\x01",
            "deliver the professor's message\x01",
            "to Her Majesty, in person...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008FHa ha ha...\x01",
            "We just got lucky, is all.\x02\x03",
            "#007FThe real question is, how much\x01",
            "longer is luck going to be on\x01",
            "our side...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015FYes... We're really going\x01",
            "to have to stay focused.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#761FIf you understand that already,\x01",
            "then there's nothing more that\x01",
            "I need to tell you.\x02\x03",
            "In any case, we can consider\x01",
            "Professor Russell's request\x01",
            "to be fulfilled.\x02\x03",
            "Please, accept this as compensation\x01",
            "for a job well done.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x45, 0x4, 0x10)
    Sleep(100)
    OP_AF(0x63, 0x45)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_28(0x46, 0x4, 0x10)
    OP_28(0x47, 0x4, 0x10)
    OP_28(0x48, 0x4, 0x10)
    OP_28(0x49, 0x4, 0x10)
    OP_28(0x4A, 0x4, 0x10)
    OP_28(0x46, 0x4, 0x20)
    OP_28(0x47, 0x4, 0x20)
    OP_28(0x48, 0x4, 0x20)
    OP_28(0x49, 0x4, 0x20)
    OP_28(0x4A, 0x4, 0x20)

    ChrTalk(
        0x8,
        (
            "#760FNow, then...Zane.\x02\x03",
            "It was pure providence that\x01",
            "Cassius invited you here.\x02\x03",
            "We need the help of an A-ranked\x01",
            "bracer like yourself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#4P#070FNo need to even ask.\x02\x03",
            "Even if I didn't have a debt to repay to\x01",
            "Cassius, I couldn't possibly stand by idly in\x01",
            "a situation like this.\x02\x03",
            "I'm with you until the end.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_BFE4():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BFE4)
    OP_8C(0x101, 90, 400)

    ChrTalk(
        0x101,
        (
            "#001F#6PI knew we could count\x01",
            "on you, Zane!\x02\x03",
            "#501FBy the way...\x01",
            "What's this A-rank business?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F#4PIt's a rank that signifies a full-\x01",
            "fledged bracer's full power.\x02\x03",
            "There are seven ranks, ranging from\x01",
            "G on the bottom, up to A at the top.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F#6PS-So he's the highest rank\x01",
            "you can get?\x02\x03",
            "Wow... I never knew you were\x01",
            "such a badass, Zane!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#4P#070FHa ha... Well, I may be A-ranked,\x01",
            "but I'm still an underling, so to\x01",
            "speak.\x02\x03",
            "#074FThere are twenty A-rankers\x01",
            "across the continent.\x02\x03",
            "But above that, there's an\x01",
            "informal S-rank.\x02\x03",
            "That one's only granted to bracers\x01",
            "who successfully resolve issues on\x01",
            "a national scale.\x02\x03",
            "#070FAnd there are only four of\x01",
            "those on the entire continent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#509F#6PWhoa... I'm not sure I even want\x01",
            "to think about what they can do...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#4P#075F*sigh*... You really don't know\x01",
            "any of this stuff, do you...?\x02\x03",
            "#070FOne of those four is Master Cassius.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#005F#6P#3SWHAT?!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#009FOkay, Joshua, you're not going\x01",
            "to tell me you knew about this\x01",
            "already, right? Right...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F#4PSorry...but yes, I did.\x02\x03",
            "#010FHe solved a major case for the\x01",
            "Republic about five years ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F*sigh* I swear... It's hardly worth\x01",
            "even getting upset about anymore.\x02\x03",
            "Royal Army soldier, 'hidden' hero,\x01",
            "Divine Blade, S-rank bracer...\x02\x03",
            "#509FIf he's really so damned awesome, then\x01",
            "it sure would be nice if he'd come back\x01",
            "and take care of THIS case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#4P#070FHa ha...\x01",
            "You may be right.\x02\x03",
            "If he were with us, perhaps this would\x01",
            "never have escalated to the point where\x01",
            "a coup d'etat was even possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#013F#4P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004FJoshua? What's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F#4P...Just thinking about how\x01",
            "strange this is.\x02\x03",
            "This whole chain of events apparently\x01",
            "started with Dad going off on his trip.\x02\x03",
            "#012FIt's as if whoever planned the coup\x01",
            "was waiting for him to be gone...\x02\x03",
            "At least, it's just the impression\x01",
            "I have.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#580FOh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#4P#072FSo what you're saying is that\x01",
            "the coup was planned around\x01",
            "his departure for the Empire?\x02\x03",
            "Am I correct?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x108, 400)

    ChrTalk(
        0x102,
        (
            "#010F#4P...No, I'm sure that would be overthinking\x01",
            "things.\x02\x03",
            "I can't think of anyone who could possibly\x01",
            "manipulate Dad like that without him\x01",
            "noticing he was being used.\x02\x03",
            "#013FThey'd have to know him and his behavior\x01",
            "patterns exceptionally well to be able to\x01",
            "pull it off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506FHmm... Well, yeah.\x02\x03",
            "I never knew what he was up to,\x01",
            "even though he was so close...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#4P#070FI don't think that Colonel Richard\x01",
            "could have ever managed to pull\x01",
            "the wool over his eyes.\x02\x03",
            "More likely, it's just that two\x01",
            "major events happened to overlap\x01",
            "with each other.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#764FRegardless of the circumstances,\x01",
            "we cannot currently rely on\x01",
            "Cassius to help.\x02\x03",
            "#762FTherefore, I am resolved to\x01",
            "prepare for the worst.\x02\x03",
            "I believe an emergency conference\x01",
            "of the Grancel branch of the Bracer\x01",
            "Guild is called for.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_CB16():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_CB16)

    def lambda_CB24():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_CB24)
    TurnDirection(0x108, 0x8, 400)

    ChrTalk(
        0x101,
        "#004F...Huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#760FAll other things being equal, we\x01",
            "have a request that comes directly\x01",
            "from Her Majesty the Queen.\x02\x03",
            "The third article of the bracer code states\x01",
            "that we shall never act in a fashion that\x01",
            "interferes with the government.\x02\x03",
            "We cannot ignore Her Majesty's request,\x01",
            "however, so we must act. But we're no\x01",
            "match for the Royal Army as we are.\x02\x03",
            "I ask the cooperation of all\x01",
            "bracers in Grancel, including\x01",
            "Zane, of course.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006FOh, okay...\x02\x03",
            "If we come in conflict with the\x01",
            "Intelligence Division, we'll\x01",
            "need all the help we can get.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#765FIdeally, we should have the\x01",
            "cooperation of other branches...\x02\x03",
            "...but the checkpoints have been\x01",
            "completely sealed off, as of today.\x02\x03",
            "Ostensibly to foil any potential\x01",
            "terrorist activity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#580FWHAT?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012FSo basically, it amounts\x01",
            "to martial law...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#4P#074FSo the enemy is finally moving\x01",
            "at full tilt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#762FThis may be to stifle any activity\x01",
            "on the part of any Royal Guardsmen\x01",
            "in hiding, as well as ourselves.\x02\x03",
            "If we're going to conduct a rescue\x01",
            "operation, we'll have to do it with\x01",
            "the resources on hand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006FOh, fun.\x01",
            "But...we're up to it!\x02\x03",
            "So, do we have a solid idea\x01",
            "of where the prisoners are\x01",
            "being held?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#764FThat's been on my mind for a\x01",
            "while now, actually...\x02\x03",
            "#762FI believe the most likely place\x01",
            "to be the Erbe Royal Villa.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505FThat's the building in the\x01",
            "forest, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FIt would make sense.\x02\x03",
            "If the soldiers are using it under\x01",
            "the pretense of counter-terrorism,\x01",
            "few would question it.\x02\x03",
            "And I can't imagine they'd want to lock a lady\x01",
            "of the royal family in a cell in Leiston\x01",
            "Fortress...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#4P#072FConsidering it's the army we're going to be\x01",
            "going against here, I'd like a more solid\x01",
            "confirmation, however.\x02\x03",
            "If we assaulted the wrong place, we'd have hell\x01",
            "to pay for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#764FYes...precisely.\x02\x03",
            "#760FBut in either case, we must\x01",
            "assemble any bracers currently\x01",
            "in the royal city.\x02\x03",
            "Could I ask you to assemble them here for me?\x01",
            "Any information you could gather while doing so\x01",
            "would be much appreciated.\x02\x03",
            "If I'm not mistaken, Estelle, you\x01",
            "and your friends are acquainted\x01",
            "with a reporter, correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501FOh, you mean Nial?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010FYeah, we should see if he's picked\x01",
            "up anything significant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#762FAlso, we must attempt to enlist\x01",
            "the aid of the Guardsmen who\x01",
            "are in hiding.\x02\x03",
            "If you can get them to contact me,\x01",
            "it would be greatly appreciated.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#505FSo, in other words...\x02\x03",
            "We need to get in touch with\x01",
            "'Sister' Julia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FShe helped us with the invitation\x01",
            "before, so we should let her know\x01",
            "what's going on.\x02\x03",
            "So, off to the cathedral, then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#760FThere are four other bracers in\x01",
            "the city: Kurt, Grant, Carna\x01",
            "and Anelace.\x02\x03",
            "Check the bars and their usual\x01",
            "hangouts. They may also be in\x01",
            "the hotel.\x02\x03",
            "If you see them, please instruct\x01",
            "them to come back here.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)

    ChrTalk(
        0x101,
        "#006FSure thing!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x102, 270, 400)

    ChrTalk(
        0x102,
        "#010FAll right, then off we go.\x02",
    )

    CloseMessageWindow()
    OP_4B(0x8, 255)
    EventEnd(0x0)
    Return()

    # Function_16_BB74 end

    def Function_17_D66F(): pass

    label("Function_17_D66F")

    OP_28(0x4F, 0x1, 0x20)
    OP_28(0x4F, 0x1, 0x40)
    OP_28(0x4F, 0x1, 0x80)
    OP_28(0x4F, 0x1, 0x100)
    OP_28(0x4F, 0x1, 0x200)
    OP_28(0x4F, 0x1, 0x400)
    OP_28(0x4F, 0x1, 0x800)
    OP_28(0x4F, 0x4, 0x10)
    EventBegin(0x0)
    OP_6D(115240, 250, 4410, 0)
    OP_67(0, 5950, -10000, 0)
    OP_6B(1550, 0)
    OP_6C(315000, 0)
    OP_6E(519, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x8, 122730, 0, -1280, 180)
    SetChrPos(0xA, 120000, 0, -2600, 90)
    SetChrPos(0x9, 118530, 0, -3290, 90)
    SetChrPos(0xB, 119790, 0, -3880, 90)
    SetChrPos(0xC, 118310, 0, -1930, 90)
    SetChrPos(0xE, 120540, 0, 450, 135)
    SetChrPos(0xF, 120230, 0, -800, 135)
    SetChrPos(0x10, 118670, 0, -680, 135)
    SetChrPos(0x11, 123780, 0, -740, 180)
    SetChrPos(0x101, 122440, 0, -3200, 0)
    SetChrPos(0x102, 123620, 0, -3200, 0)
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    OP_4A(0xA, 255)
    OP_4A(0xB, 255)
    OP_4A(0xC, 255)
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    FadeToBright(2000, 0)
    OP_6D(121410, 0, -1310, 4000)

    ChrTalk(
        0x8,
        (
            "#760F#2PEstelle and Joshua Bright.\x02\x03",
            "In honor of your recent work, the Grancel\x01",
            "branch of the Bracer Guild has prepared\x01",
            "you a letter of recommendation.\x02\x03",
            "Take it with our blessing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1P#006FYes, sir!\x02",
    )

    CloseMessageWindow()
    OP_8E(0x8, 0x1DFD8, 0x0, 0xFFFFF6AA, 0x7D0, 0x0)
    Sleep(100)
    OP_AF(0x63, 0x4F)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
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
    OP_3E(0x33B, 1)
    OP_8F(0x8, 0x1DF6A, 0x0, 0xFFFFFB00, 0x7D0, 0x0)

    ChrTalk(
        0x8,
        (
            "#761F#2PWith this, you now have five\x01",
            "such letters, I believe.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 90, 400)

    ChrTalk(
        0x8,
        (
            "#760F#5PSir Cassius...\x01",
            "If you will do the honors?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#085F#2PI will.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 180, 400)
    OP_8F(0x8, 0x1DE8E, 0x0, 0xFFFFFE66, 0x7D0, 0x0)
    OP_8F(0x11, 0x1E01E, 0x0, 0xFFFFF916, 0x7D0, 0x0)
    Sleep(500)

    ChrTalk(
        0x11,
        (
            "#082F#2PEstelle and Joshua Bright.\x02\x03",
            "In accordance with the rules of the \x01",
            "guild, this will qualify you both\x01",
            "to become full-fledged bracers.\x02\x03",
            "Present your letters of recommendation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1P#004FY-Yes, sir...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1P#015FBy all means, please verify\x01",
            "their authenticity.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Handed over \x07\x02",
            "letters of recommendation\x07\x00",
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3F(0x330, 1)
    OP_3F(0x333, 1)
    OP_3F(0x339, 1)
    OP_3F(0x33A, 1)
    OP_3F(0x33B, 1)
    OP_3F(0x36D, 1)
    OP_3F(0x36E, 1)

    ChrTalk(
        0x11,
        (
            "#085F#2PThe Rolent, Bose, Ruan, Zeiss\x01",
            "and Grancel branches...\x02\x03",
            "I've now confirmed the authenticity\x01",
            "of all five signatures.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DCEE")

    ChrTalk(
        0x11,
        (
            "#080F#2PThe final rank, Junior Bracer Rank 1.\x02\x03",
            "#081FI never thought you'd come so far.\x01",
            "Honestly, it's a little frightening.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DF94")

    label("loc_DCEE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DD69")

    ChrTalk(
        0x11,
        (
            "#080F#2PThe final rank, Junior Bracer Rank 2.\x02\x03",
            "I can truly say that your\x01",
            "apprenticeship was a success.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DF94")

    label("loc_DD69")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DDE4")

    ChrTalk(
        0x11,
        (
            "#080F#2PThe final rank, Junior Bracer Rank 3.\x02\x03",
            "I can truly say that your\x01",
            "apprenticeship was a success.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DF94")

    label("loc_DDE4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DE7B")

    ChrTalk(
        0x11,
        (
            "#080F#2PThe final rank, Junior Bracer Rank 4.\x02\x03",
            "#083FYou just barely scraped by.\x01",
            "You'll have to work especially\x01",
            "hard in the future.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DF94")

    label("loc_DE7B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DF12")

    ChrTalk(
        0x11,
        (
            "#080F#2PThe final rank, Junior Bracer Rank 5.\x02\x03",
            "#083FYou just barely scraped by.\x01",
            "You'll have to work especially\x01",
            "hard in the future.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DF94")

    label("loc_DF12")


    ChrTalk(
        0x11,
        (
            "#080F#2PThe final rank, Junior Bracer.\x02\x03",
            "#083FFrankly, I'm amazed that you\x01",
            "qualified for advancement with\x01",
            "results this low...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DF94")

    Sleep(400)

    ChrTalk(
        0x11,
        (
            "#080F#2PIn Aidios' name and by the Seal of\x01",
            "the Bracer Guild, both of you are\x01",
            "promoted to full-fledged bracers.\x02\x03",
            "Take your emblems, you two.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1P#508FYes, sir!\x02",
    )

    CloseMessageWindow()
    OP_8F(0x11, 0x1DFD8, 0x0, 0xFFFFF6AA, 0x7D0, 0x0)
    OP_AD(0x40023, 0xBE, 0x64, 0x1F4)
    Sleep(1500)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 280, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received \x07\x02",
            "Bracer Emblem\x07\x00",
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3E(0x35D, 1)
    OP_AE(0x1F4)
    Sleep(1000)
    OP_8F(0x11, 0x1E01E, 0x0, 0xFFFFF916, 0x7D0, 0x0)
    OP_22(0xE9, 0x0, 0x64)
    Sleep(500)

    def lambda_E0E9():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E0E9)

    def lambda_E0F7():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E0F7)
    OP_6D(119780, 0, -1210, 1500)
    Sleep(500)

    ChrTalk(
        0xF,
        "#021FCongratulations, guys!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#071FHeeeey, those emblems look\x01",
            "good on you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#051FI have to admit, you two did\x01",
            "good. But just this once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F#2PHee hee...\x01",
            "Thanks, everyone!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019FWe never would have reached this\x01",
            "point without everyone's help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#080F#2PYour true careers as bracers\x01",
            "start now.\x02\x03",
            "Bear that in mind.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_E26C():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E26C)
    Sleep(100)
    OP_8C(0x101, 0, 400)

    ChrTalk(
        0x101,
        "#006F#1PI understand...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1P#010FWe'll be even more dedicated.\x02",
    )

    CloseMessageWindow()
    OP_6D(119780, 0, -210, 1000)
    OP_8C(0x8, 225, 400)

    ChrTalk(
        0x8,
        (
            "#760F#2PNow, I hate to break up such\x01",
            "a happy occasion...\x02\x03",
            "...but I'm afraid I do have\x01",
            "some unfortunate news that\x01",
            "I must tell all of you.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_E374():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_E374)

    def lambda_E382():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_E382)

    def lambda_E390():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_E390)

    def lambda_E39E():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_E39E)

    def lambda_E3AC():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_E3AC)

    def lambda_E3BA():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_E3BA)

    def lambda_E3C8():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_E3C8)

    def lambda_E3D6():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_E3D6)

    def lambda_E3E4():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E3E4)

    def lambda_E3F2():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E3F2)

    ChrTalk(
        0xC,
        "#842FWhat's that...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#762F#2PToday marks the final day of\x01",
            "Cassius Bright's membership\x01",
            "with the Bracer Guild.\x02\x03",
            "He is going to be returning to\x01",
            "active duty within the Royal Army.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_E516():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_E516)

    def lambda_E524():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_E524)

    def lambda_E532():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_E532)

    def lambda_E540():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E540)

    def lambda_E54E():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E54E)
    Sleep(1000)

    def lambda_E561():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_E561)

    def lambda_E56F():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_E56F)

    def lambda_E57D():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_E57D)

    def lambda_E58B():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_E58B)

    ChrTalk(
        0x9,
        "#832F#6PWha...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#822F#5PReally?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#085F#2PSince I've been away for so long,\x01",
            "I feel bad bringing this up so\x01",
            "suddenly.\x02\x03",
            "#080FBut the chaos that has resulted from\x01",
            "the attempted coup must be quelled.\x02\x03",
            "The military needs major reorganization to\x01",
            "deal with the damage that the Intelligence\x01",
            "Division caused.\x02\x03",
            "I plan to help out with that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#818F#5POh, I get it. Since bracers\x01",
            "can't be soldiers...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xF, 400)

    ChrTalk(
        0xA,
        (
            "#814F#6PHey, did you higher ranks\x01",
            "already know about this?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0xA, 400)

    ChrTalk(
        0xF,
        (
            "#020F#4PYes, he already discussed\x01",
            "it with us.\x02\x03",
            "It is discouraging, but we can never\x01",
            "truly become independent if we always\x01",
            "lean on those more experienced.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0xA, 400)

    ChrTalk(
        0xE,
        (
            "#051FAnd hey, think of it as less competition.\x01",
            "Now that Cassius is out, maybe you can\x01",
            "take the top spot...eventually.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#841F#6PI suppose that's true...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#835F#6PThis means that we're going to\x01",
            "be really busy, though...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_E90B():
        OP_6D(119780, 0, -1210, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E90B)
    OP_8C(0x11, 180, 400)

    def lambda_E92A():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_E92A)

    def lambda_E938():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_E938)

    def lambda_E946():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_E946)

    def lambda_E954():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_E954)
    WaitChrThread(0x101, 0x1)

    ChrTalk(
        0x11,
        (
            "#080F#2PWell, you do have two new full-\x01",
            "fledged bracers on hand now.\x02\x03",
            "You can work them like dogs\x01",
            "instead of me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#509F#1PDad...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F#2PHa ha... I guess our lives are\x01",
            "about to get pretty hectic, eh?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_A2(0x66B)
    ClearMapFlags(0x2000000)
    OP_A2(0x3FC)
    NewScene("ED6_DT01/T4200   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_17_D66F end

    def Function_18_EA57(): pass

    label("Function_18_EA57")

    EventBegin(0x0)
    OP_6D(-3270, 0, 730, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, -2600, 0, 100, 90)
    SetChrPos(0x101, -860, 0, -670, 270)
    SetChrPos(0x102, -950, 0, 482, 270)
    OP_4A(0x8, 255)
    SetChrPos(0x8, -5700, 0, -130, 270)
    LoadEffect(0x0, "map\\\\mp001_01.eff")
    PlayEffect(0x0, 0x0, 0xFF, -6030, 2000, -270, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(
        0x18,
        (
            "#033F#5P???\x02\x03",
            "Why are we back at the\x01",
            "Bracer Guild?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#507FOh, don't get your neckerchief\x01",
            "in a knot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FElnan's calling over our guest,\x01",
            "you see.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_EBDA():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_EBDA)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#760F#6PYes, yes.\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_22(0x83, 0x0, 0x64)
    OP_82(0x0, 0x0)
    Sleep(300)
    OP_8C(0x8, 90, 400)
    OP_8E(0x8, 0xFFFFEE80, 0x0, 0x3C0, 0x7D0, 0x0)
    TurnDirection(0x8, 0x102, 400)

    ChrTalk(
        0x8,
        (
            "#761FThe interested party has been\x01",
            "successfully contacted...\x02\x03",
            "...and should be arriving here\x01",
            "shortly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#6P#035FHeh, I imagine she simply\x01",
            "can't bear waiting for the\x01",
            "opportunity to meet me!\x02\x03",
            "#030FTell me, have I made this kitten's\x01",
            "acquaintance before, or is this to\x01",
            "be our first meowing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001FOh, I believe the 'kitten' knows\x01",
            "you and REALLY wants to see you.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x18, 90, 400)

    ChrTalk(
        0x18,
        (
            "#037F#5PHa ha...\x01",
            "Kittens in Grancel...\x02\x03",
            "Perhaps it's Schera...or perhaps\x01",
            "even Carna or Anelace...\x02\x03",
            "#035FNo, no... I must not discount the possibility\x01",
            "that it might be Mayor Maybelle, or maybe\x01",
            "even dear sweet Lila...\x02\x03",
            "#033FSurely, it's not Princess\x01",
            "Klaudia or Tita...?!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#019FThat's...well, let's just say\x01",
            "that you've got one hell of\x01",
            "an imagination.\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x71, 0x0, 0x64)
    Sleep(700)
    SetChrPos(0x19, -200, -250, -7270, 152)

    def lambda_EF66():
        TurnDirection(0xFE, 0x19, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_EF66)

    def lambda_EF74():
        TurnDirection(0xFE, 0x19, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_EF74)

    def lambda_EF82():
        TurnDirection(0xFE, 0x19, 400)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_EF82)

    def lambda_EF90():
        TurnDirection(0xFE, 0x19, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_EF90)
    OP_9F(0x19, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6D(-1570, 0, -2670, 2000)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#760F#6PAh, it seems that our guest\x01",
            "is already here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#031FIs she now?\x02\x03",
            "My dearest, come in! Come in!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x19,
        "Man's Voice",
        (
            "#2P...With that kind of welcome,\x01",
            "who am I to refuse?\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x6, 0x0, 0x64)
    ClearChrFlags(0x19, 0x80)

    def lambda_F07E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_F07E)

    def lambda_F090():
        OP_8E(0x19, 0xFFFFF8F8, 0x0, 0xFFFFF7F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_F090)

    def lambda_F0AB():

        label("loc_F0AB")

        TurnDirection(0x19, 0x18, 0)
        OP_48()
        Jump("loc_F0AB")

    QueueWorkItem2(0x19, 0, lambda_F0AB)

    def lambda_F0BC():
        OP_6D(-2220, 0, -370, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_F0BC)

    def lambda_F0D4():

        label("loc_F0D4")

        TurnDirection(0xFE, 0x19, 0)
        OP_48()
        Jump("loc_F0D4")

    QueueWorkItem2(0x101, 1, lambda_F0D4)

    def lambda_F0E5():

        label("loc_F0E5")

        TurnDirection(0xFE, 0x19, 0)
        OP_48()
        Jump("loc_F0E5")

    QueueWorkItem2(0x102, 1, lambda_F0E5)

    def lambda_F0F6():

        label("loc_F0F6")

        TurnDirection(0xFE, 0x19, 0)
        OP_48()
        Jump("loc_F0F6")

    QueueWorkItem2(0x18, 1, lambda_F0F6)
    WaitChrThread(0x101, 0x3)

    ChrTalk(
        0x18,
        "#4P#033FWha...\x02",
    )

    CloseMessageWindow()
    OP_44(0x19, 0xFF)
    TurnDirection(0x19, 0x101, 400)

    ChrTalk(
        0x19,
        (
            "#3P#270FLooks like you've done what\x01",
            "I asked, then.\x02\x03",
            "#272FI appreciate it. On behalf of the\x01",
            "Erebonian embassy, I thank you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001FThat's not necessary.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019FIt was Olivier who was really\x01",
            "eager to oblige you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#4P#033FI don't remember being present\x01",
            "at that discussion...\x02\x03",
            "But does this mean that you're the\x01",
            "kitten who wished to see me...?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x19, 0x18, 400)

    ChrTalk(
        0x19,
        (
            "#3P#270FWhat are you smoking?\x02\x03",
            "Her Royal Majesty the Queen directly\x01",
            "invited you to tonight's banquet, so I'm\x01",
            "not about to tell you you can't go.\x02\x03",
            "BUT...I know you. And I know you're going\x01",
            "to get into trouble if you're not properly\x01",
            "chaperoned.\x02\x03",
            "So I'm keeping a close eye on you until\x01",
            "dinnertime. And you're going to LIKE it.\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x18, 0xFF)
    OP_62(0x18, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x18, 90, 400)

    ChrTalk(
        0x18,
        (
            "#036FE-Estelle! Joshua!\x02\x03",
            "You tricked me?!\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_8C(0x101, 270, 400)

    ChrTalk(
        0x101,
        (
            "#509FDon't blame your bad hearing\x01",
            "on us...\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x102, 0xFF)
    OP_8C(0x102, 270, 400)

    ChrTalk(
        0x102,
        (
            "#019FYou were the one who decided\x01",
            "it was a woman. We never said\x01",
            "a word.\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x19, 0x40)
    OP_8E(0x19, 0xFFFFF5D8, 0x0, 0xFFFFFCE0, 0xBB8, 0x0)
    TurnDirection(0x19, 0x18, 400)
    TurnDirection(0x18, 0x19, 0)

    ChrTalk(
        0x19,
        (
            "#272F#3PNow, then...\x01",
            "Evening swiftly approaches.\x02\x03",
            "There's a lot of paperwork to fill out,\x01",
            "and YOU'RE going to do it. So let's\x01",
            "get back to the embassy, shall we?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_F58B():

        label("loc_F58B")

        TurnDirection(0xFE, 0x19, 0)
        OP_48()
        Jump("loc_F58B")

    QueueWorkItem2(0x101, 1, lambda_F58B)

    def lambda_F59C():

        label("loc_F59C")

        TurnDirection(0xFE, 0x19, 0)
        OP_48()
        Jump("loc_F59C")

    QueueWorkItem2(0x102, 1, lambda_F59C)
    OP_8E(0x19, 0xFFFFF5D8, 0x0, 0xFFFFFD44, 0xBB8, 0x0)
    OP_8C(0x19, 90, 400)
    SetChrFlags(0x18, 0x4)
    SetChrPos(0x18, -2600, 400, 100, 0)
    OP_62(0x18, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_F5F0():
        OP_97(0x18, 0xFFFFF5D8, 0xFFFFFD44, 0x16760, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_F5F0)
    SetChrChipByIndex(0x18, 20)
    SetChrSubChip(0x18, 0)
    SetChrFlags(0x18, 0x20)
    OP_8C(0x19, 180, 400)

    ChrTalk(
        0x18,
        "#5P#20A#036FOh, nooooo!\x05\x02",
    )

    OP_43(0x18, 0x1, 0x0, 0x13)
    OP_43(0x19, 0x1, 0x0, 0x14)
    WaitChrThread(0x18, 0x1)
    OP_22(0x7, 0x0, 0x64)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x18, 0xFF)
    OP_44(0x8, 0x1)
    OP_6D(-2240, 0, 670, 1000)
    TurnDirection(0x8, 0x102, 400)
    TurnDirection(0x101, 0x8, 400)
    TurnDirection(0x102, 0x8, 400)

    ChrTalk(
        0x8,
        (
            "#760FHmm...\x01",
            "Well, case closed, I guess.\x02\x03",
            "Since that concludes your investigation,\x01",
            "allow me to give you your rightful reward.\x02\x03",
            "Your proper Bracer Notebooks are not\x01",
            "yet ready, so I'd like for you to\x01",
            "note this in your junior one.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x55, 0x4, 0x10)
    OP_28(0x55, 0x1, 0x1)
    OP_28(0x55, 0x1, 0x2)
    Sleep(100)
    OP_AF(0x63, 0x55)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#506F#1PHmmm... I feel a little guilty\x01",
            "about this request, but okay.\x02\x03",
            "#006FNow, why don't we get back\x01",
            "to the Birthday Celebration?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F#4PSounds good.\x02\x03",
            "And once we've checked everything\x01",
            "out, we can go to the rest area\x01",
            "in the eastern block.\x02",
        )
    )

    CloseMessageWindow()
    SetMapFlags(0x800)
    OP_4B(0x8, 255)
    OP_A2(0x6FB)
    EventEnd(0x0)
    Return()

    # Function_18_EA57 end

    def Function_19_F8AF(): pass

    label("Function_19_F8AF")

    SetChrFlags(0xFE, 0x40)
    SetChrFlags(0xFE, 0x4)
    OP_8F(0xFE, 0x21C, 0xFA, 0xFFFFEA02, 0x7D0, 0x0)

    def lambda_F8D3():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_F8D3)
    OP_8F(0xFE, 0x21C, 0xFA, 0xFFFFE192, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_19_F8AF end

    def Function_20_F8F9(): pass

    label("Function_20_F8F9")

    SetChrFlags(0xFE, 0x40)
    SetChrFlags(0xFE, 0x4)
    OP_8F(0xFE, 0xFFFFFEAC, 0xFFFFFF06, 0xFFFFEA02, 0x834, 0x0)

    def lambda_F91D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_F91D)
    OP_8F(0xFE, 0xFFFFFEAC, 0xFFFFFF06, 0xFFFFE192, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_20_F8F9 end

    def Function_21_F943(): pass

    label("Function_21_F943")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDD, 5)), scpexpr(EXPR_END)), "loc_F956")
    OP_2A(0x50, 0x51, 0x55, 0xFFFF)
    Jump("loc_F9F8")

    label("loc_F956")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_F99C")
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There are no requests.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Jump("loc_F9F8")

    label("loc_F99C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_F9AD")
    OP_2A(0x50, 0x51, 0xFFFF)
    Jump("loc_F9F8")

    label("loc_F9AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_F9BC")
    OP_2A(0x50, 0xFFFF)
    Jump("loc_F9F8")

    label("loc_F9BC")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There are no requests.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_F9F8")

    TalkEnd(0xFF)
    Return()

    # Function_21_F943 end

    SaveToFile()

Try(main)
