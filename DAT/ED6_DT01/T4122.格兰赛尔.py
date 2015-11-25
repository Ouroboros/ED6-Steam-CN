from ED6ScenarioHelper import *

def main():
    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4122   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4122.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60014",
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
        'Anelace',                              # 9
        'Carna',                                # 10
        'Lily',                                 # 11
        'Danton',                               # 12
        'Kitty',                                # 13
        'Sienna',                               # 14
        'Terell',                               # 15
        'Sophina',                              # 16
        'Carla',                                # 17
        'Lucia',                                # 18
        'Dorothy',                              # 19
        'Edel',                                 # 20
        'Filder',                               # 21
        'Sasha',                                # 22
        'Rutherford',                           # 23
        'Scherazard',                           # 24
        'Butler Phillip',                       # 25
        'Midee',                                # 26
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
        'ED6_DT07/CH01630 ._CH',             # 00
        'ED6_DT07/CH01240 ._CH',             # 01
        'ED6_DT07/CH01150 ._CH',             # 02
        'ED6_DT07/CH01020 ._CH',             # 03
        'ED6_DT07/CH01770 ._CH',             # 04
        'ED6_DT07/CH01130 ._CH',             # 05
        'ED6_DT07/CH01120 ._CH',             # 06
        'ED6_DT07/CH01690 ._CH',             # 07
        'ED6_DT07/CH01030 ._CH',             # 08
        'ED6_DT07/CH01070 ._CH',             # 09
        'ED6_DT07/CH02070 ._CH',             # 0A
        'ED6_DT07/CH01210 ._CH',             # 0B
        'ED6_DT07/CH01290 ._CH',             # 0C
        'ED6_DT07/CH01540 ._CH',             # 0D
        'ED6_DT07/CH01020 ._CH',             # 0E
        'ED6_DT07/CH00020 ._CH',             # 0F
        'ED6_DT07/CH02470 ._CH',             # 10
    )

    AddCharChipPat(
        'ED6_DT07/CH01630P._CP',             # 00
        'ED6_DT07/CH01240P._CP',             # 01
        'ED6_DT07/CH01150P._CP',             # 02
        'ED6_DT07/CH01020P._CP',             # 03
        'ED6_DT07/CH01770P._CP',             # 04
        'ED6_DT07/CH01130P._CP',             # 05
        'ED6_DT07/CH01120P._CP',             # 06
        'ED6_DT07/CH01690P._CP',             # 07
        'ED6_DT07/CH01030P._CP',             # 08
        'ED6_DT07/CH01070P._CP',             # 09
        'ED6_DT07/CH02070P._CP',             # 0A
        'ED6_DT07/CH01210P._CP',             # 0B
        'ED6_DT07/CH01290P._CP',             # 0C
        'ED6_DT07/CH01540P._CP',             # 0D
        'ED6_DT07/CH01020P._CP',             # 0E
        'ED6_DT07/CH00020P._CP',             # 0F
        'ED6_DT07/CH02470P._CP',             # 10
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
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 27,
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
        TalkScenaIndex      = 26,
    )

    DeclNpc(
        X                   = 8790,
        Z                   = 0,
        Y                   = 10500,
        Direction           = 196,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 25,
    )

    DeclNpc(
        X                   = 12170,
        Z                   = 0,
        Y                   = -4050,
        Direction           = 163,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 23,
    )

    DeclNpc(
        X                   = -13610,
        Z                   = 250,
        Y                   = 11140,
        Direction           = 182,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
    )

    DeclNpc(
        X                   = -12600,
        Z                   = 0,
        Y                   = 6400,
        Direction           = 9,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 13600,
        Z                   = 0,
        Y                   = -8480,
        Direction           = 91,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = -8770,
        Z                   = 0,
        Y                   = -8610,
        Direction           = 21,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 410,
        Z                   = 0,
        Y                   = 3810,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 2650,
        Z                   = 0,
        Y                   = 3210,
        Direction           = 106,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 9980,
        Z                   = 0,
        Y                   = 6170,
        Direction           = 87,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = -50,
        Z                   = 0,
        Y                   = 10,
        Direction           = 204,
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
        X                   = -1440,
        Z                   = 0,
        Y                   = 65550,
        Direction           = 179,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 1970,
        Z                   = 0,
        Y                   = 65550,
        Direction           = 175,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -950,
        Z                   = 0,
        Y                   = 60990,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 8850,
        Z                   = 0,
        Y                   = -10950,
        Direction           = 282,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -10430,
        Z                   = 0,
        Y                   = 9410,
        Direction           = 178,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -4540,
        Z                   = 0,
        Y                   = 9850,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )


    DeclActor(
        TriggerX            = 8450,
        TriggerZ            = 0,
        TriggerY            = 8650,
        TriggerRange        = 800,
        ActorX              = 8790,
        ActorZ              = 1500,
        ActorY              = 10500,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 24,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 11970,
        TriggerZ            = 0,
        TriggerY            = -5950,
        TriggerRange        = 800,
        ActorX              = 12170,
        ActorZ              = 1500,
        ActorY              = -4050,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 22,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -6400,
        TriggerZ            = 0,
        TriggerY            = 9620,
        TriggerRange        = 800,
        ActorX              = -4540,
        ActorZ              = 1500,
        ActorY              = 9850,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 19,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -1370,
        TriggerZ            = 0,
        TriggerY            = 63610,
        TriggerRange        = 800,
        ActorX              = -1440,
        ActorZ              = 1500,
        ActorY              = 65550,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 1850,
        TriggerZ            = 0,
        TriggerY            = 63640,
        TriggerRange        = 800,
        ActorX              = 1970,
        ActorZ              = 1500,
        ActorY              = 65550,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_426",          # 00, 0
        "Function_1_6CE",          # 01, 1
        "Function_2_727",          # 02, 2
        "Function_3_73D",          # 03, 3
        "Function_4_761",          # 04, 4
        "Function_5_785",          # 05, 5
        "Function_6_B5F",          # 06, 6
        "Function_7_E4C",          # 07, 7
        "Function_8_FB8",          # 08, 8
        "Function_9_FBD",          # 09, 9
        "Function_10_166B",        # 0A, 10
        "Function_11_1670",        # 0B, 11
        "Function_12_22E3",        # 0C, 12
        "Function_13_28DE",        # 0D, 13
        "Function_14_2A18",        # 0E, 14
        "Function_15_2D25",        # 0F, 15
        "Function_16_341F",        # 10, 16
        "Function_17_3790",        # 11, 17
        "Function_18_3CB9",        # 12, 18
        "Function_19_421F",        # 13, 19
        "Function_20_4224",        # 14, 20
        "Function_21_48E9",        # 15, 21
        "Function_22_5A57",        # 16, 22
        "Function_23_5A5C",        # 17, 23
        "Function_24_666E",        # 18, 24
        "Function_25_6673",        # 19, 25
        "Function_26_6EA5",        # 1A, 26
        "Function_27_6FAE",        # 1B, 27
    )


    def Function_0_426(): pass

    label("Function_0_426")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_448")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 10500, 0, 5390, 90)

    label("loc_448")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_4AF")
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 8850, 0, -10160, 259)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 4100, 0, -10830, 100)
    OP_43(0x8, 0x0, 0x0, 0x2)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0xE, 2470, 0, -3790, 78)
    Jump("loc_6CD")

    label("loc_4AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_4EA")
    SetChrPos(0xD, -11310, 0, 6390, 355)
    SetChrPos(0xE, 13600, 0, -11620, 107)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    ClearChrFlags(0x13, 0x80)
    Jump("loc_6CD")

    label("loc_4EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_520")
    SetChrPos(0xD, -13220, 0, 9430, 198)
    SetChrPos(0xE, 13600, 0, -7380, 82)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    Jump("loc_6CD")

    label("loc_520")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_578")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 2890, 0, 3290, 87)
    OP_43(0x8, 0x0, 0x0, 0x2)
    SetChrPos(0xD, -8740, 0, 9410, 165)
    SetChrPos(0xE, 5870, 0, -10820, 272)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    Jump("loc_6CD")

    label("loc_578")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_5B8")
    SetChrPos(0xD, -10560, 0, 9490, 200)
    SetChrPos(0xE, 4480, 0, -6130, 340)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    ClearChrFlags(0x13, 0x80)
    Jump("loc_6CD")

    label("loc_5B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_60B")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 5000, 0, 1510, 0)
    OP_43(0x8, 0x0, 0x0, 0x2)
    SetChrPos(0xD, -8890, 0, 6200, 349)
    SetChrPos(0xE, 13580, 0, -11020, 70)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x12, 0x80)
    Jump("loc_6CD")

    label("loc_60B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_641")
    SetChrPos(0xD, -7480, 0, 4300, 104)
    SetChrPos(0xE, 4480, 0, -6130, 340)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x13, 0x80)
    Jump("loc_6CD")

    label("loc_641")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_661")
    SetChrPos(0xD, -7480, 0, 4300, 104)
    ClearChrFlags(0xF, 0x80)
    Jump("loc_6CD")

    label("loc_661")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_686")
    SetChrPos(0xD, -12210, 250, 11380, 355)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x13, 0x80)
    Jump("loc_6CD")

    label("loc_686")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_6BC")
    SetChrPos(0xD, -11310, 0, 6390, 355)
    SetChrPos(0xE, 13580, 0, -11020, 70)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x16, 0x80)
    Jump("loc_6CD")

    label("loc_6BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_6CD")
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x16, 0x80)

    label("loc_6CD")

    Return()

    # Function_0_426 end

    def Function_1_6CE(): pass

    label("Function_1_6CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_701")
    OP_B1("t4122_y")
    Jump("loc_70A")

    label("loc_701")

    OP_B1("t4122_n")

    label("loc_70A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 2)), scpexpr(EXPR_END)), "loc_71A")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x4B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_71A")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_6CE end

    def Function_2_727(): pass

    label("Function_2_727")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_73C")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_727")

    label("loc_73C")

    Return()

    # Function_2_727 end

    def Function_3_73D(): pass

    label("Function_3_73D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_760")
    OP_8D(0xFE, -12460, -5460, -5830, -11220, 3000)
    Jump("Function_3_73D")

    label("loc_760")

    Return()

    # Function_3_73D end

    def Function_4_761(): pass

    label("Function_4_761")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_784")
    OP_8D(0xFE, 2190, 5370, 2900, 2580, 3000)
    Jump("Function_4_761")

    label("loc_784")

    Return()

    # Function_4_761 end

    def Function_5_785(): pass

    label("Function_5_785")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_83B")

    ChrTalk(
        0x18,
        (
            "#720FHis Excellency has sequestered\x01",
            "himself to consider the claims\x01",
            "made by the queen.\x02\x03",
            "He is spending his days\x01",
            "at the Erbe Royal Villa,\x01",
            "isolated with his thoughts.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B5B")

    label("loc_83B")

    OP_A2(0x10)

    ChrTalk(
        0x101,
        "#004FOh, hi, Phillip!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#720FMistress Estelle. Master\x01",
            "Joshua. Please, forgive my\x01",
            "lack of decorum.\x02\x03",
            "#722FThrough my actions yesterday, \x01",
            "I have caused His Excellency\x01",
            "much trouble...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505FOn that subject...do you know\x01",
            "where we might find Duke Dunan?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#720FHis Excellency has sequestered\x01",
            "himself to consider the claims\x01",
            "made by the queen.\x02\x03",
            "He is spending his days\x01",
            "at the Erbe Royal Villa,\x01",
            "isolated with his thoughts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000FOh, is he now...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014FThen...what brings you here,\x01",
            "Phillip?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#722FWell, I...I've been sent here\x01",
            "on an errand. To buy doughnuts\x01",
            "for His Excellency, you see!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506FOh, I see...\x02\x03",
            "(I get the feeling he's not\x01",
            "being completely honest about\x01",
            "that...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F(Yeah, he's pretty clearly here\x01",
            "for his OWN doughnuts...but,\x01",
            "whatever floats his airship!)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B5B")

    TalkEnd(0xFE)
    Return()

    # Function_5_785 end

    def Function_6_B5F(): pass

    label("Function_6_B5F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_BED")

    ChrTalk(
        0x17,
        (
            "#020FOnce we get back, let's go\x01",
            "shopping together, for old\x01",
            "times' sake.\x02\x03",
            "I can buy you an outfit, as a\x01",
            "congratulatory gift!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E48")

    label("loc_BED")

    OP_A2(0xF)
    OP_A2(0x6EC)

    ChrTalk(
        0x17,
        "#023FWell, hello there!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000FWhatcha doing, Schera?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#020FShopping with colleagues. Been\x01",
            "long overdue for a nice shopping\x01",
            "trip, after all.\x02\x03",
            "I don't get much of a chance\x01",
            "these days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505FWhen I was little, I remember\x01",
            "you used to take us shopping\x01",
            "all the time. It was fun!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#021FThat's right... When your dad \x01",
            "was gone, the three of us used\x01",
            "to go out all the time.\x02\x03",
            "#020FYou know, once we get back to Rolent,\x01",
            "what say we do a little shopping together,\x01",
            "for old times' sake?\x02\x03",
            "I can buy you an outfit, as a\x01",
            "congratulatory gift!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001FReally? I'd love to!\x02\x03",
            "It's a date, then!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E48")

    TalkEnd(0xFE)
    Return()

    # Function_6_B5F end

    def Function_7_E4C(): pass

    label("Function_7_E4C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_E59")
    Jump("loc_FB4")

    label("loc_E59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_E63")
    Jump("loc_FB4")

    label("loc_E63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_E6D")
    Jump("loc_FB4")

    label("loc_E6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_E77")
    Jump("loc_FB4")

    label("loc_E77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_E81")
    Jump("loc_FB4")

    label("loc_E81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_E8B")
    Jump("loc_FB4")

    label("loc_E8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_E95")
    Jump("loc_FB4")

    label("loc_E95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_E9F")
    Jump("loc_FB4")

    label("loc_E9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_EA9")
    Jump("loc_FB4")

    label("loc_EA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_F57")

    ChrTalk(
        0xFE,
        (
            "With the world going to hell in a\x01",
            "handbasket, it's no wonder the airship\x01",
            "business is in such dire straits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Selling them's been next to\x01",
            "impossible lately.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FB4")

    label("loc_F57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_FB4")

    ChrTalk(
        0xFE,
        "I finally made it to Grancel!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Our arrival was delayed for\x01",
            "army inspections.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FB4")

    TalkEnd(0xFE)
    Return()

    # Function_7_E4C end

    def Function_8_FB8(): pass

    label("Function_8_FB8")

    Call(0, 9)
    Return()

    # Function_8_FB8 end

    def Function_9_FBD(): pass

    label("Function_9_FBD")

    TalkBegin(0x15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_1007")

    ChrTalk(
        0x15,
        (
            "I hope our passengers have a\x01",
            "safe and enjoyable flight!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1667")

    label("loc_1007")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_105E")

    ChrTalk(
        0x15,
        "This sucks...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "We've got an open holiday\x01",
            "schedule, but no business!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1667")

    label("loc_105E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_110D")

    ChrTalk(
        0x15,
        (
            "Tickets and reservations have\x01",
            "been getting canceled left and\x01",
            "right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Shouldn't be any surprise, though,\x01",
            "you know? The airships are all\x01",
            "grounded, after all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1667")

    label("loc_110D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_1154")

    ChrTalk(
        0x15,
        (
            "I'm so glad the Martial Arts\x01",
            "Competition went smoothly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1667")

    label("loc_1154")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1202")

    ChrTalk(
        0x15,
        (
            "Today's the last day of the\x01",
            "competition, no?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "It's all astoundingly lively around\x01",
            "here, especially considering we just\x01",
            "had ourselves a terrorist incident!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1667")

    label("loc_1202")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_13C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_12BD")

    ChrTalk(
        0x15,
        (
            "Payton's a special maintenance\x01",
            "engineer who used to work on\x01",
            "the Arseille.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "The army seized the ship after\x01",
            "the coup, and he's been depressed\x01",
            "about it ever since.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13BD")

    label("loc_12BD")

    OP_A2(0xD)

    ChrTalk(
        0x15,
        (
            "Payton's a special maintenance\x01",
            "engineer who used to work on\x01",
            "the Arseille.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "The army seized the ship after\x01",
            "the coup, and he's been depressed\x01",
            "about it ever since.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "The Royal Guardsmen used it,\x01",
            "but it was originally made\x01",
            "for the royal family.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13BD")

    Jump("loc_1667")

    label("loc_13C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_147B")

    ChrTalk(
        0x15,
        (
            "I was able to talk with some\x01",
            "of the Royal Guardsmen connected\x01",
            "to the Arseille.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "They were a little old-fashioned,\x01",
            "but overall they seemed like good,\x01",
            "upstanding people.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1667")

    label("loc_147B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_14DF")

    ChrTalk(
        0x15,
        (
            "I didn't think the army could\x01",
            "commandeer the airways except\x01",
            "in times of emergency...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1667")

    label("loc_14DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_157D")

    ChrTalk(
        0x15,
        (
            "This time of year there are so many travelers \x01",
            "coming to see the Martial Arts Competition and\x01",
            "take part in the Queen's Birthday Celebration...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1667")

    label("loc_157D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_163E")

    ChrTalk(
        0x15,
        (
            "We had some crazy special offers\x01",
            "planned for this season, let me\x01",
            "tell you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "But with everything that's \x01",
            "happened, we had to cancel\x01",
            "every one of our plans.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "What a waste!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1667")

    label("loc_163E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1667")

    ChrTalk(
        0x15,
        "Welcome to Liberl Orbalship!\x02",
    )

    CloseMessageWindow()

    label("loc_1667")

    TalkEnd(0x15)
    Return()

    # Function_9_FBD end

    def Function_10_166B(): pass

    label("Function_10_166B")

    Call(0, 11)
    Return()

    # Function_10_166B end

    def Function_11_1670(): pass

    label("Function_11_1670")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_188B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_1756")

    ChrTalk(
        0x14,
        (
            "All the landing port closings have\x01",
            "been on account of this coup\x01",
            "d'etat, I suppose?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Makes sense, but if the general populace\x01",
            "had known that was the cause, I'm sure\x01",
            "there would've been mass hysteria...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1888")

    label("loc_1756")

    OP_A2(0xC)

    ChrTalk(
        0x14,
        (
            "All the landing port closings have\x01",
            "been on account of this coup\x01",
            "d'etat, I suppose?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Makes sense, but if the general populace\x01",
            "had known that was the cause, I'm sure\x01",
            "there would've been mass hysteria...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "I'm just glad that despite it\x01",
            "all, we were still able to hold\x01",
            "the Birthday Celebration!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1888")

    Jump("loc_22DF")

    label("loc_188B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_192D")

    ChrTalk(
        0x14,
        (
            "Saw a nun heading over to Payton's\x01",
            "house a little while ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "I wonder if she's helping him\x01",
            "through the shock of the \x01",
            "Arseille being seized...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22DF")

    label("loc_192D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_199B")

    ChrTalk(
        0x14,
        "*sigh*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "The Royal Army's closed the\x01",
            "landing platforms again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "Give me a break already!\x02",
    )

    CloseMessageWindow()
    Jump("loc_22DF")

    label("loc_199B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_1A4A")

    ChrTalk(
        0x14,
        (
            "The duke's assembled a group of very\x01",
            "powerful statesmen to serve as honored\x01",
            "guests during tonight's banquet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "I hope they'll be safe from\x01",
            "the terrorists...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22DF")

    label("loc_1A4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1AE2")

    ChrTalk(
        0x14,
        (
            "Thanks to the army and those\x01",
            "Sky Bandits in Bose, airship \x01",
            "business is in the red.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "All news is bad news these days.\x01",
            "I'm sick of it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22DF")

    label("loc_1AE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_1C89")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_1B9B")

    ChrTalk(
        0x14,
        (
            "The army told us they needed\x01",
            "our cooperation in protecting\x01",
            "the Arseille.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Of course, I don't see how \x01",
            "helping the army is going to\x01",
            "benefit my business at all!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C86")

    label("loc_1B9B")

    OP_A2(0xC)

    ChrTalk(
        0x14,
        (
            "The army has stepped up their\x01",
            "police presence in the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "The army told us they needed\x01",
            "our cooperation in protecting\x01",
            "the Arseille.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Of course, I don't see how \x01",
            "helping the army is going to\x01",
            "benefit my business at all!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C86")

    Jump("loc_22DF")

    label("loc_1C89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_1E2B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_1D44")

    ChrTalk(
        0x14,
        (
            "News of the queen's illness\x01",
            "hasn't spread to the rest\x01",
            "of the country yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "And quite a lot of people have \x01",
            "come for the Birthday Celebration,\x01",
            "totally unaware...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E28")

    label("loc_1D44")

    OP_A2(0xC)

    ChrTalk(
        0x14,
        (
            "News of the queen's illness\x01",
            "hasn't spread to the rest\x01",
            "of the country yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "And quite a lot of people have \x01",
            "come for the Birthday Celebration,\x01",
            "totally unaware...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "But what good will it do me\x01",
            "to start complaining?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E28")

    Jump("loc_22DF")

    label("loc_1E2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1F06")

    ChrTalk(
        0x14,
        (
            "The army is commandeering so many landing ports for\x01",
            "their own vessels that our business timetables\x01",
            "are in complete and total disarray.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "It was the army that completely\x01",
            "destroyed our flight schedules.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22DF")

    label("loc_1F06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_2004")

    ChrTalk(
        0x14,
        (
            "Thanks to the Martial Arts Competition and the\x01",
            "Birthday Celebration, there are more people dis-\x01",
            "embarking here than getting on. I'm seeing red!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "We have to be very careful in\x01",
            "handling issues like customer\x01",
            "complaints and lost children.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22DF")

    label("loc_2004")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_20C2")

    ChrTalk(
        0x14,
        (
            "We have both passenger liners\x01",
            "and the royal orbalship Arseille\x01",
            "in port here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "The Royal Guardsmen have been\x01",
            "using it, though, so it was seized\x01",
            "by the army after the coup.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22DF")

    label("loc_20C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_22DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_21AA")

    ChrTalk(
        0x14,
        (
            "Thanks to all these Royal Army\x01",
            "inspections, our flight schedules\x01",
            "are in shambles.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "I've been taking a lot of complaints from\x01",
            "customers...but I'm at a total loss as to\x01",
            "where I can go to file some of my own!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22DF")

    label("loc_21AA")

    OP_A2(0xC)

    ChrTalk(
        0x14,
        (
            "Thanks to all these Royal Army\x01",
            "inspections, our flight schedules\x01",
            "are in shambles.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "I've been taking a lot of complaints from\x01",
            "customers...but I'm at a total loss as to\x01",
            "where I can go to file some of my own!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "...It's not even our fault, yet\x01",
            "we're the ones who end up having\x01",
            "to apologize for it!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22DF")

    TalkEnd(0x14)
    Return()

    # Function_11_1670 end

    def Function_12_22E3(): pass

    label("Function_12_22E3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_23D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_235C")

    ChrTalk(
        0xFE,
        (
            "Take advantage of our Birthday\x01",
            "Celebration Memorial Sale now!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Want to know more? Just ask!\x02",
    )

    CloseMessageWindow()
    Jump("loc_23D2")

    label("loc_235C")

    OP_A2(0xB)

    ChrTalk(
        0xFE,
        "Welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Take advantage of our Birthday\x01",
            "Celebration Memorial Sale now!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Want to know more? Just ask!\x02",
    )

    CloseMessageWindow()

    label("loc_23D2")

    Jump("loc_28DA")

    label("loc_23D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_2485")

    ChrTalk(
        0xFE,
        (
            "We have a big campaign for the\x01",
            "start of the Birthday Celebration.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Things may be rough, but we don't\x01",
            "have time to mope-- there's much\x01",
            "too much to get ready!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28DA")

    label("loc_2485")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_248F")
    Jump("loc_28DA")

    label("loc_248F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_2499")
    Jump("loc_28DA")

    label("loc_2499")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_25C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_2506")

    ChrTalk(
        0xFE,
        (
            "Our shop only carries the finest\x01",
            "quality goods, hand-picked and\x01",
            "arranged just for you!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25BF")

    label("loc_2506")

    OP_A2(0xB)

    ChrTalk(
        0xFE,
        (
            "The Bose Market is a very crowded,\x01",
            "extremely high-energy place to work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You have to constantly revise,\x01",
            "maximize and improve your business\x01",
            "and sales sense, or you're toast!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25BF")

    Jump("loc_28DA")

    label("loc_25C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_25CC")
    Jump("loc_28DA")

    label("loc_25CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_27B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_268D")

    ChrTalk(
        0xFE,
        (
            "At this rate, we won't even\x01",
            "break into the top sellers in\x01",
            "Grancel, let alone Liberl!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Once the Birthday Celebration's\x01",
            "over, we're going on a business\x01",
            "retreat to Bose.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27B4")

    label("loc_268D")

    OP_A2(0xB)

    ChrTalk(
        0xFE,
        (
            "At this rate, we won't even \x01",
            "break into the top sellers in\x01",
            "Grancel, let alone Liberl!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...That tears it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Once the Birthday Celebration's\x01",
            "over, we're going on a business\x01",
            "retreat to Bose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Know your enemy like the back\x01",
            "of your hand, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm gonna shop 'til I drop!\x02",
    )

    CloseMessageWindow()

    label("loc_27B4")

    Jump("loc_28DA")

    label("loc_27B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_27C1")
    Jump("loc_28DA")

    label("loc_27C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_28C9")

    ChrTalk(
        0xFE,
        (
            "Okay, time to get to work!\x01",
            "Our goal? To destroy the\x01",
            "Bose Market share!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I joined my husband on his pilgrimage\x01",
            "and studied all the different stores...\x01",
            "and now, I'm ready to CRUSH them!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've got to re-energize this store,\x01",
            "and myself as well!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28DA")

    label("loc_28C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_28D3")
    Jump("loc_28DA")

    label("loc_28D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_28DA")

    label("loc_28DA")

    TalkEnd(0xFE)
    Return()

    # Function_12_22E3 end

    def Function_13_28DE(): pass

    label("Function_13_28DE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_295C")

    ChrTalk(
        0x12,
        (
            "#151FOoh yeah! I'll be back tomorrow...\x01",
            "and I'm gonna STEAL YOUR SOULS with\x01",
            "my camera obscura! Yeeah, baby!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A14")

    label("loc_295C")

    OP_A2(0xA)

    ChrTalk(
        0x12,
        (
            "#151FHey, guys! I got some of the BEST\x01",
            "shots of you in that last match!\x02\x03",
            "You'll see them in the tournament\x01",
            "special edition. Coming soon to a\x01",
            "newsstand near you! Don't miss it!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A14")

    TalkEnd(0xFE)
    Return()

    # Function_13_28DE end

    def Function_14_2A18(): pass

    label("Function_14_2A18")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_2A25")
    Jump("loc_2D21")

    label("loc_2A25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_2A2F")
    Jump("loc_2D21")

    label("loc_2A2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_2A39")
    Jump("loc_2D21")

    label("loc_2A39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_2A43")
    Jump("loc_2D21")

    label("loc_2A43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_2A4D")
    Jump("loc_2D21")

    label("loc_2A4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_2BA2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_2ABD")

    ChrTalk(
        0xFE,
        "I'm gonna cheer for Bigfoot Man!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mommy's going to cheer for the\x01",
            "man in the red mask.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B9F")

    label("loc_2ABD")

    OP_A2(0x9)

    ChrTalk(
        0xFE,
        "I'm gonna cheer for Bigfoot Man!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mommy's going to cheer for the\x01",
            "man in the red mask.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F(Bigfoot Man? Is she talking\x01",
            "about Zane...?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F(It'd break his heart if someone\x01",
            "called him that to his face.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B9F")

    Jump("loc_2D21")

    label("loc_2BA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_2BE3")

    ChrTalk(
        0xFE,
        "When is the match starting?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm so excited!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D21")

    label("loc_2BE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2C46")

    ChrTalk(
        0xFE,
        (
            "The man in the red bandana\x01",
            "lost his match, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I was cheering for him, too...\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D21")

    label("loc_2C46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_2CAC")

    ChrTalk(
        0xFE,
        "You know what?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm gonna cheer for the man in\x01",
            "the red bandana, with all my\x01",
            "might!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D21")

    label("loc_2CAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_2CEF")

    ChrTalk(
        0xFE,
        (
            "I'm gonna buy presents for\x01",
            "all of my friends today!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D21")

    label("loc_2CEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_2D21")

    ChrTalk(
        0xFE,
        (
            "Heh heh, I'm on a trip with\x01",
            "my mommy!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D21")

    TalkEnd(0xFE)
    Return()

    # Function_14_2A18 end

    def Function_15_2D25(): pass

    label("Function_15_2D25")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_2D32")
    Jump("loc_341B")

    label("loc_2D32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_2D3C")
    Jump("loc_341B")

    label("loc_2D3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_2D46")
    Jump("loc_341B")

    label("loc_2D46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_2D50")
    Jump("loc_341B")

    label("loc_2D50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_2D5A")
    Jump("loc_341B")

    label("loc_2D5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_2E2F")

    ChrTalk(
        0xFE,
        (
            "The clash of two tirelessly\x01",
            "honed fighting styles is such\x01",
            "a turn-o-- I-I mean, spectacle!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You can almost feel the two fighters'\x01",
            "pent-up energy swelling forth and\x01",
            "bursting all over one another!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_341B")

    label("loc_2E2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_2ECB")

    ChrTalk(
        0xFE,
        (
            "My daughter and I have become\x01",
            "completely addicted to the\x01",
            "Martial Arts Competition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We're gonna watch every match,\x01",
            "from start to finish!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_341B")

    label("loc_2ECB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2FFF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_2F5C")

    ChrTalk(
        0xFE,
        (
            "The Ravens lost, to the surprise\x01",
            "of pretty much no one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They seemed remarkably upbeat,\x01",
            "though, all things considered!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FFC")

    label("loc_2F5C")

    OP_A2(0x8)

    ChrTalk(
        0xFE,
        (
            "The Ravens lost, to the surprise\x01",
            "of pretty much no one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Now, it might just be me...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But they seemed remarkably upbeat,\x01",
            "all things considered!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FFC")

    Jump("loc_341B")

    label("loc_2FFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_3164")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_3093")

    ChrTalk(
        0xFE,
        (
            "The Ravens are that gang in\x01",
            "Ruan, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I just hope they don't bring\x01",
            "shame to Ruan's good name...\x01",
            "rhyme not intended...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3161")

    label("loc_3093")

    OP_A2(0x8)

    ChrTalk(
        0xFE,
        (
            "The Ravens are that gang that\x01",
            "got used by the Mayor, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Why would anyone let them into\x01",
            "the tournament?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I just hope they don't bring\x01",
            "shame to Ruan's good name...\x01",
            "rhyme not intended...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3161")

    Jump("loc_341B")

    label("loc_3164")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_33B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_3232")

    ChrTalk(
        0xFE,
        (
            "The Ruan Orphanage is using\x01",
            "donations and indemnities to\x01",
            "fund a new building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The children are all staying at my\x01",
            "inn right now. And they're rowdy\x01",
            "little buggers, let me tell you!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33B4")

    label("loc_3232")

    OP_A2(0x8)

    ChrTalk(
        0xFE,
        (
            "The orphanage in Ruan has had it rough. I mean,\x01",
            "the mayor gets arrested, then the main building\x01",
            "burns to the ground...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But they're using donations \x01",
            "and indemnities to fund the\x01",
            "construction of a new building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The children are all staying at my\x01",
            "inn right now. And they're rowdy\x01",
            "little buggers, let me tell you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope they finish building the\x01",
            "new orphanage soon...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33B4")

    Jump("loc_341B")

    label("loc_33B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_341B")

    ChrTalk(
        0xFE,
        (
            "My daughter and I came from \x01",
            "a small village in Ruan called\x01",
            "Manoria to see the capital.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_341B")

    TalkEnd(0xFE)
    Return()

    # Function_15_2D25 end

    def Function_16_341F(): pass

    label("Function_16_341F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_342C")
    Jump("loc_378C")

    label("loc_342C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_3436")
    Jump("loc_378C")

    label("loc_3436")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_3440")
    Jump("loc_378C")

    label("loc_3440")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_34E1")

    ChrTalk(
        0xFE,
        (
            "Tomorrow we're taking an \x01",
            "airship back home to Bose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm looking for a souvenir to \x01",
            "take back for my brother...\x01",
            "I wonder what would be good?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_378C")

    label("loc_34E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_3554")

    ChrTalk(
        0xFE,
        (
            "I'm going to go to the \x01",
            "cathedral in the West Block\x01",
            "sometime this afternoon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It should be fun!\x02",
    )

    CloseMessageWindow()
    Jump("loc_378C")

    label("loc_3554")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_3580")

    ChrTalk(
        0xFE,
        "Hmmm... Where to go today...\x02",
    )

    CloseMessageWindow()
    Jump("loc_378C")

    label("loc_3580")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_3607")

    ChrTalk(
        0xFE,
        (
            "That's right! My brother asked\x01",
            "me to buy him some fishing gear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll need to swing by the\x01",
            "Fisherman's Guild later.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_378C")

    label("loc_3607")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_367D")

    ChrTalk(
        0xFE,
        (
            "This was my first time\x01",
            "seeing the tournament.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It was intense! And...kind \x01",
            "of scary, to be honest!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_378C")

    label("loc_367D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_36E5")

    ChrTalk(
        0xFE,
        "What should I do today?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I came all this way. I might\x01",
            "as well go see the tournament!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_378C")

    label("loc_36E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_374B")

    ChrTalk(
        0xFE,
        (
            "It's been a long time since I\x01",
            "last came to the capital. I\x01",
            "want to soak it in slowly...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_378C")

    label("loc_374B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_378C")

    ChrTalk(
        0xFE,
        (
            "I flew in from Bose to sell\x01",
            "some of my merchandise. \x02",
        )
    )

    CloseMessageWindow()

    label("loc_378C")

    TalkEnd(0xFE)
    Return()

    # Function_16_341F end

    def Function_17_3790(): pass

    label("Function_17_3790")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_38A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_3805")

    ChrTalk(
        0xFE,
        (
            "You know, I don't think Duke\x01",
            "Dunan is that bad a person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Annoying, though? You betcha!\x02",
    )

    CloseMessageWindow()
    Jump("loc_38A3")

    label("loc_3805")

    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "But such horrible, horrible\x01",
            "things are said about him...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't think Duke Dunan is\x01",
            "an inherently bad person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I dunno, maybe it's just me!\x02",
    )

    CloseMessageWindow()

    label("loc_38A3")

    Jump("loc_3CB5")

    label("loc_38A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_3953")

    ChrTalk(
        0xFE,
        (
            "Nothing can happen with all\x01",
            "of these soldiers on guard...\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I might go home early today.\x01",
            "It...seems like a good day to\x01",
            "hole up in safety somewhere!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CB5")

    label("loc_3953")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_39CC")

    ChrTalk(
        0xFE,
        (
            "All the shopkeepers seemed to\x01",
            "be in an uproar over something\x01",
            "just now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...What the heck happened?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3CB5")

    label("loc_39CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_3A10")

    ChrTalk(
        0xFE,
        (
            "Gotta try to find something\x01",
            "nice to give to my wife.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CB5")

    label("loc_3A10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_3A96")

    ChrTalk(
        0xFE,
        (
            "At first I thought, I'll just\x01",
            "get her a plate or something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But you know, she deserves\x01",
            "a little better than that!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CB5")

    label("loc_3A96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_3B21")

    ChrTalk(
        0xFE,
        (
            "When are they going to hunt down\x01",
            "and arrest these terrorists?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I mean, that attack on the\x01",
            "Central Factory was horrible!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CB5")

    label("loc_3B21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_3B9A")

    ChrTalk(
        0xFE,
        (
            "I'm not really interested in\x01",
            "the Martial Arts Competition...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So for me, it's just business\x01",
            "as usual!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CB5")

    label("loc_3B9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3C2B")

    ChrTalk(
        0xFE,
        (
            "*sigh* But it's all the same\x01",
            "old stuff, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I came in here hoping they'd\x01",
            "have something new today...\x01",
            "but no such luck!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CB5")

    label("loc_3C2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_3C51")

    ChrTalk(
        0xFE,
        "Hmm... I don't know...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3CB5")

    label("loc_3C51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_3C72")

    ChrTalk(
        0xFE,
        "Oh, this is nice!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3CB5")

    label("loc_3C72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_3CB5")

    ChrTalk(
        0xFE,
        (
            "It would make for a really\x01",
            "nice gift, don't you think?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CB5")

    TalkEnd(0xFE)
    Return()

    # Function_17_3790 end

    def Function_18_3CB9(): pass

    label("Function_18_3CB9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_3D43")

    ChrTalk(
        0xFE,
        (
            "Now what should I do about lunch\x01",
            "today...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Housewives never get a day off,\x01",
            "even during the Birthday Cele-\x01",
            "bration.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_421B")

    label("loc_3D43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_3DBB")

    ChrTalk(
        0xFE,
        (
            "Those soldiers in black\x01",
            "are all over the place!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It really makes this city\x01",
            "look like a police state.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_421B")

    label("loc_3DBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_3E18")

    ChrTalk(
        0xFE,
        (
            "Is it my imagination, or are\x01",
            "there fewer things on the\x01",
            "shelves than usual...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_421B")

    label("loc_3E18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_3EB9")

    ChrTalk(
        0xFE,
        (
            "With all the hubbub, there are bound\x01",
            "to be some great limited time sales...\x01",
            "and I'm gonna find 'em!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope the price on this one\x01",
            "drops soon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_421B")

    label("loc_3EB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_3F3B")

    ChrTalk(
        0xFE,
        (
            "Maybe I should just stop shopping\x01",
            "and go eat something!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But everywhere I go it's just\x01",
            "crowds, crowds, crowds!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_421B")

    label("loc_3F3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_3F94")

    ChrTalk(
        0xFE,
        (
            "So, what should I make for\x01",
            "dinner tonight? Gotta stock\x01",
            "up, don'tcha know!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_421B")

    label("loc_3F94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_4022")

    ChrTalk(
        0xFE,
        "There! That should be everything!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Seems like every time I write\x01",
            "a shopping list, there's always\x01",
            "that ONE ITEM I forget...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_421B")

    label("loc_4022")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_405B")

    ChrTalk(
        0xFE,
        (
            "Let's see... Ooh, oil, gotta\x01",
            "have that...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_421B")

    label("loc_405B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_40F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_4083")

    ChrTalk(
        0xFE,
        "Mmmm... Scones...\x02",
    )

    CloseMessageWindow()
    Jump("loc_40F0")

    label("loc_4083")

    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "Coffee's nice, but I'm a tea\x01",
            "drinker, myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This is probably the best\x01",
            "store in all of Liberl.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40F0")

    Jump("loc_421B")

    label("loc_40F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_418E")

    ChrTalk(
        0xFE,
        (
            "After the tournament starts,\x01",
            "the streets get so crowded!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Should I just buy everything\x01",
            "I need in bulk now, or come\x01",
            "back again later...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_421B")

    label("loc_418E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_421B")

    ChrTalk(
        0xFE,
        (
            "Ooh! They have stuff from\x01",
            "Ravennue! SCORE!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But why is it you can only\x01",
            "ever find the things you want\x01",
            "when you have no money?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_421B")

    TalkEnd(0xFE)
    Return()

    # Function_18_3CB9 end

    def Function_19_421F(): pass

    label("Function_19_421F")

    Call(0, 20)
    Return()

    # Function_19_421F end

    def Function_20_4224(): pass

    label("Function_20_4224")

    TalkBegin(0x19)
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4284")
    OP_0D()
    OP_A9(0x5E)
    OP_56(0x0)
    TalkEnd(0x19)
    Return()

    label("loc_4284")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4295")
    TalkEnd(0x19)
    Return()

    label("loc_4295")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_43EB")

    ChrTalk(
        0x19,
        (
            "If I can't get my wicked tongue under control,\x01",
            "I'll never be allowed to sell tea. So I need to\x01",
            "just...bite it, and be nice!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "I'm going to teach myself everything I can\x01",
            "about teas, and try to talk the owner into\x01",
            "letting me sell them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "That'll show that smug sister\x01",
            "of mine who's the REAL exotic\x01",
            "tea girl in this family!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_48E5")

    label("loc_43EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_44AD")

    ChrTalk(
        0x19,
        (
            "...My insults toward my sister haven't been\x01",
            "very good, have they? Gimme a sec, and I'll\x01",
            "come up with something much meaner to say!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "Like, I'm the better tea seller,\x01",
            "so NYEAH!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_48E5")

    label("loc_44AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_46DC")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (0, "loc_44D5"),
        (1, "loc_44F5"),
        (2, "loc_4513"),
        (3, "loc_453A"),
        (4, "loc_45F5"),
        (5, "loc_4641"),
        (SWITCH_DEFAULT, "loc_4697"),
    )


    label("loc_44D5")


    ChrTalk(
        0x19,
        "My sister's feet stink!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4697")

    label("loc_44F5")


    ChrTalk(
        0x19,
        "My sister can't sing!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4697")

    label("loc_4513")


    ChrTalk(
        0x19,
        "My sister's scared of roaches!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4697")

    label("loc_453A")


    ChrTalk(
        0x19,
        "My sister's...uh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "My sister's ignoring me, and\x01",
            "I kind of miss her...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "Er, I mean...Miss, Little Miss,\x01",
            "Little Miss Know-it-all! YEAH!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "She's cold, man! Cold as ICE!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4697")

    label("loc_45F5")


    ChrTalk(
        0x19,
        (
            "My sister can't gain weight\x01",
            "no matter how much junk \x01",
            "food she eats!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4697")

    label("loc_4641")


    ChrTalk(
        0x19,
        (
            "My sister has low blood \x01",
            "pressure and has trouble \x01",
            "getting up in the morning!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4697")

    label("loc_4697")


    ChrTalk(
        0x19,
        (
            "So that means she has to suck\x01",
            "at selling tea, right? RIGHT?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_48E5")

    label("loc_46DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_48E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_47A3")

    ChrTalk(
        0x19,
        (
            "She stole the tea-selling position from me\x01",
            "and said it was okay because she's older...\x01",
            "and WISER! She actually said wiser!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "I'll show her! I'll be the\x01",
            "best tea seller EVER!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_48E5")

    label("loc_47A3")

    OP_A2(0x11)

    ChrTalk(
        0x19,
        (
            "The girl over there giving out\x01",
            "free tea samples? That's my twin\x01",
            "sister, Kitty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "She's the most popular waitress\x01",
            "here right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "She stole the tea-selling position from me\x01",
            "and said it was okay because she's older...\x01",
            "and WISER! She actually said wiser!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "I'll show her! I'll be the\x01",
            "best tea seller EVER!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48E5")

    TalkEnd(0x19)
    Return()

    # Function_20_4224 end

    def Function_21_48E9(): pass

    label("Function_21_48E9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_49C3")

    ChrTalk(
        0xFE,
        (
            "I keep forgetting to ask Danton\x01",
            "to order some teapots from the\x01",
            "Republic next time he has a chance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Tea goods have gotten really popular\x01",
            "with womenfolk lately, and I think\x01",
            "they'd totally love it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A53")

    label("loc_49C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_4A7A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_4A2B")

    ChrTalk(
        0xFE,
        (
            "If you like tea with lemon, I\x01",
            "recommend you try the norgil\x01",
            "tea from North Ambria.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A77")

    label("loc_4A2B")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        "Hello!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you like milk tea, why not\x01",
            "try our Calvardian blend?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A77")

    Jump("loc_5A53")

    label("loc_4A7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_4BFA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_4B0B")

    ChrTalk(
        0xFE,
        "It's Queen Alicia's favorite!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I take some small measure of\x01",
            "pride in selling the same teas\x01",
            "the queen loves oh so much.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BF7")

    label("loc_4B0B")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        "You heard it here first...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Queen Alicia? Loves tea! Like,\x01",
            "ADORES it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sometimes some of her royal\x01",
            "aides come to buy our teas.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I take some small measure of\x01",
            "pride in selling the same teas\x01",
            "the queen loves oh so much.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BF7")

    Jump("loc_5A53")

    label("loc_4BFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_4EC9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_4CE1")

    ChrTalk(
        0xFE,
        (
            "Drink every last drop when you\x01",
            "can, because you never know how\x01",
            "long the tea'll keep flowin'!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Don't ever forget that when you're brewing\x01",
            "a good cup. If it's not delicious from top\x01",
            "to bottom, it's GARBAGE!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4EC6")

    label("loc_4CE1")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "Kitty's Guide to Savoring Delicious\x01",
            "Tea, Rule Number Six!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Drink every last drop when you\x01",
            "can, because you never know how\x01",
            "long the tea'll keep flowin'!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They call the last mouthful of tea 'the\x01",
            "teardrop,' because you'll be crying when\x01",
            "you realize there's no more in your cup!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Another important tip is to\x01",
            "keep stirring your tea while\x01",
            "it brews in your cup.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That concludes my Guide to\x01",
            "Savoring Delicious Tea.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What do you think? Bestseller\x01",
            "material, or what?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4EC6")

    Jump("loc_5A53")

    label("loc_4EC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_50DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_4F45")

    ChrTalk(
        0xFE,
        "Steep the leaves!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's very important you not\x01",
            "forget that when making your\x01",
            "cup of delicious tea.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_50DA")

    label("loc_4F45")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "Kitty's Guide to Savoring Delicious\x01",
            "Tea, Rule Number Five!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Steep the leaves!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Tea leaves release all their\x01",
            "bitterness before the real\x01",
            "flavor starts a-flowin'.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Thus, patience is key!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But if you wait too long, it'll get\x01",
            "bitter again. You need to find the\x01",
            "'butter zone,' so to speak.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For long leaves, you'll want to\x01",
            "wait just over 3 minutes; and for\x01",
            "short leaves, just under.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_50DA")

    Jump("loc_5A53")

    label("loc_50DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_5314")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_5166")

    ChrTalk(
        0xFE,
        "Measure your tea!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Be exacting-- as if your life\x01",
            "depended on it! (Because if I'm\x01",
            "around, IT WILL, believe me!)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5311")

    label("loc_5166")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "Kitty's Guide to Savoring Delicious\x01",
            "Tea, Rule Number Four!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Measure your tea!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It varies based on the leaves you're\x01",
            "using, but a general rule of thumb is\x01",
            "that one cup gets one teaspoon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you have too many leaves, the\x01",
            "tea is bitter. And if there are\x01",
            "too few, it's bland city!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you use a large number of leaves over\x01",
            "too short a time, you'll end up with the \x01",
            "flavor suppressed by all the bitterness.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5311")

    Jump("loc_5A53")

    label("loc_5314")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_553B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_5395")

    ChrTalk(
        0xFE,
        "Keep your teapot warm!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's very important you not\x01",
            "forget that when making your\x01",
            "cup of delicious tea.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5538")

    label("loc_5395")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "Kitty's Guide to Savoring Delicious\x01",
            "Tea, Rule Number Three!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Keep your teapot warm!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The phenomenon of tea leaves\x01",
            "rising and swirling as they\x01",
            "steep is called 'jumping.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Jumping is key to a properly\x01",
            "made cup of delicious tea.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But jumping leaves are caused\x01",
            "by hot water, and if your\x01",
            "teapot is cold...well...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's also said that a round-\x01",
            "bottomed teapot will help\x01",
            "jumping occur more easily.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5538")

    Jump("loc_5A53")

    label("loc_553B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_5700")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_55E3")

    ChrTalk(
        0xFE,
        "Always use freshly boiled water!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Don't ever forget that, or I\x01",
            "WILL find you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Equally important is not to\x01",
            "overboil your water, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_56FD")

    label("loc_55E3")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "Kitty's Guide to Savoring Delicious\x01",
            "Tea, Rule Number Two!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Always use freshly boiled water!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There has to be enough oxygen\x01",
            "dissolved into the water to \x01",
            "bring out the tea's flavor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's why you use freshly\x01",
            "drawn and boiled water, poured\x01",
            "directly from the pot.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_56FD")

    Jump("loc_5A53")

    label("loc_5700")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_5890")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_574A")

    ChrTalk(
        0xFE,
        (
            "First, use fresh, quality tea\x01",
            "leaves. A no-brainer.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_588D")

    label("loc_574A")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "Kitty's Guide to Savoring Delicious\x01",
            "Tea, Rule Number One!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Use good tea leaves. This\x01",
            "is patently obvious, but\x01",
            "also patently important! \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Of course, you CAN use old \x01",
            "ones, as long as they don't\x01",
            "smell and aren't moldy.  \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But really...tea is more than\x01",
            "the taste of dried leaves boiled\x01",
            "in water, you know?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_588D")

    Jump("loc_5A53")

    label("loc_5890")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_5957")

    ChrTalk(
        0xFE,
        (
            "You know the golden rules of\x01",
            "making tea, don't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They vary by region, but I've got six of\x01",
            "them I've taken to heart, and they're the\x01",
            "reason the teas I sell are so deeeelicious!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A53")

    label("loc_5957")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_5A53")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_59D5")

    ChrTalk(
        0xFE,
        (
            "Would you like to try a free\x01",
            "sample of our tea?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can even teach you how to\x01",
            "prepare your own cup! \x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A53")

    label("loc_59D5")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        "Welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Would you like to try a free\x01",
            "sample of our tea?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can even teach you how to\x01",
            "prepare your own cup! \x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A53")

    TalkEnd(0xFE)
    Return()

    # Function_21_48E9 end

    def Function_22_5A57(): pass

    label("Function_22_5A57")

    Call(0, 23)
    Return()

    # Function_22_5A57 end

    def Function_23_5A5C(): pass

    label("Function_23_5A5C")

    TalkBegin(0xB)
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5ABC")
    OP_0D()
    OP_A9(0x5D)
    OP_56(0x0)
    TalkEnd(0xB)
    Return()

    label("loc_5ABC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5ACD")
    TalkEnd(0xB)
    Return()

    label("loc_5ACD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_5BE3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_5B62")

    ChrTalk(
        0xB,
        (
            "Well, the important thing is that\x01",
            "the queen is safe and able to\x01",
            "celebrate her birthday properly!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Thank goodness for that!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5BE0")

    label("loc_5B62")

    OP_A2(0x3)

    ChrTalk(
        0xB,
        "Praise the Goddess!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "The queen is safe and able to\x01",
            "celebrate her birthday properly!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Thank goodness for that!\x02",
    )

    CloseMessageWindow()

    label("loc_5BE0")

    Jump("loc_666A")

    label("loc_5BE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_5D2C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_5C89")

    ChrTalk(
        0xB,
        (
            "If one of the Royal Guardsmen\x01",
            "came running in here, I would \x01",
            "hide him, no questions asked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "There's no way that Lt.\x01",
            "Schwarz is a terrorist.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D29")

    label("loc_5C89")

    OP_A2(0x3)

    ChrTalk(
        0xB,
        (
            "If one of the Royal Guardsmen\x01",
            "came running in here, I would \x01",
            "hide him, no questions asked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "There's no way that Lt. Schwarz\x01",
            "is a terrorist. No way!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D29")

    Jump("loc_666A")

    label("loc_5D2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_5E92")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_5DCF")

    ChrTalk(
        0xB,
        (
            "The army's completely shut \x01",
            "down the airship platforms.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "What are they thinking? How\x01",
            "are we supposed to get any\x01",
            "new stock at this rate?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E8F")

    label("loc_5DCF")

    OP_A2(0x3)

    ChrTalk(
        0xB,
        (
            "The army's completely shut \x01",
            "down the airship platforms.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "What are they thinking? How\x01",
            "are we supposed to get any\x01",
            "new stock at this rate?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "A bunch of smeg-heads, if you\x01",
            "ask me!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E8F")

    Jump("loc_666A")

    label("loc_5E92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_5F1F")

    ChrTalk(
        0xB,
        "So the finals are over, then?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "A royal banquet in the castle\x01",
            "for the winners... Surprised\x01",
            "the duke came up with that one.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_666A")

    label("loc_5F1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_6082")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_5FC3")

    ChrTalk(
        0xB,
        (
            "All these crazy things happening\x01",
            "around Bose, Ruan and Zeiss...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "The only places free of craziness\x01",
            "right now are Rolent and...well,\x01",
            "here!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_607F")

    label("loc_5FC3")

    OP_A2(0x3)

    ChrTalk(
        0xB,
        (
            "All these crazy things happening\x01",
            "around Bose, Ruan and Zeiss...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "The only places free of craziness\x01",
            "right now are Rolent and...well,\x01",
            "here!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "...Hope I didn't just jinx us...\x02",
    )

    CloseMessageWindow()

    label("loc_607F")

    Jump("loc_666A")

    label("loc_6082")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_62A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_616E")

    ChrTalk(
        0xB,
        (
            "After the Birthday Celebration, the\x01",
            "manager suggested we take a trip to\x01",
            "Bose for *cough* store research.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Usually she'll just spout out trendy\x01",
            "marketing ploys, but this time I\x01",
            "think she may be on to something!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62A6")

    label("loc_616E")

    OP_A2(0x3)

    ChrTalk(
        0xB,
        (
            "After the Birthday Celebration, the\x01",
            "manager suggested we take a trip to\x01",
            "Bose for *cough* store research.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I'd love to go, personally, and\x01",
            "see the infamous Bose Market with\x01",
            "my own two eyes...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Usually she'll just spout out trendy\x01",
            "marketing ploys, but this time I\x01",
            "think she may be on to something!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_62A6")

    Jump("loc_666A")

    label("loc_62A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_6419")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_633E")

    ChrTalk(
        0xB,
        (
            "I heard Ruan City just held\x01",
            "itself a new mayoral election.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Looks like the Dalmore family's\x01",
            "finally going to get the boot!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6416")

    label("loc_633E")

    OP_A2(0x3)

    ChrTalk(
        0xB,
        (
            "So I was reading the\x01",
            "Liberl News...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Seems Ruan city just held itself\x01",
            "a new mayoral election.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Looks like the Dalmore family's\x01",
            "finally going to get the boot!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "It's about damn time, if you ask me.\x02",
    )

    CloseMessageWindow()

    label("loc_6416")

    Jump("loc_666A")

    label("loc_6419")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_64E1")

    ChrTalk(
        0xB,
        (
            "The mayor of Ruan got himself arrested,\x01",
            "which-- as you might imagine-- resulted\x01",
            "in MASS HYSTERIA.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "We haven't gotten any fresh\x01",
            "fish in a while now. And I\x01",
            "love fresh fish... So sad!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_666A")

    label("loc_64E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_6584")

    ChrTalk(
        0xB,
        (
            "Our store manager just got\x01",
            "back from a trip.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "This job feels much more relaxing\x01",
            "with her gone. Can't she, like, go\x01",
            "on another trip...right now?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_666A")

    label("loc_6584")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_662B")

    ChrTalk(
        0xB,
        (
            "This is where we sell some of\x01",
            "the hottest, most fashionable\x01",
            "accessories and items around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If you see something you'd \x01",
            "like, just give me a holler!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_666A")

    label("loc_662B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_666A")

    ChrTalk(
        0xB,
        (
            "Hello. Looking for a little\x01",
            "memento of your visit?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_666A")

    TalkEnd(0xB)
    Return()

    # Function_23_5A5C end

    def Function_24_666E(): pass

    label("Function_24_666E")

    Call(0, 25)
    Return()

    # Function_24_666E end

    def Function_25_6673(): pass

    label("Function_25_6673")

    TalkBegin(0xA)
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_66EB")
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_66D4")
    OP_A9(0x69)
    Jump("loc_66E2")

    label("loc_66D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_66E0")
    OP_A9(0x68)
    Jump("loc_66E2")

    label("loc_66E0")

    OP_A9(0x5C)

    label("loc_66E2")

    OP_56(0x0)
    TalkEnd(0xA)
    Return()

    label("loc_66EB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_66FC")
    TalkEnd(0xA)
    Return()

    label("loc_66FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_67AC")

    ChrTalk(
        0xA,
        (
            "Thanks to that coup d'etat\x01",
            "special, the Liberl News has \x01",
            "been flying off the shelves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "We can't keep them for even an\x01",
            "hour at a time, they sell out\x01",
            "so fast!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6EA1")

    label("loc_67AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_6848")

    ChrTalk(
        0xA,
        (
            "I've been catching some of\x01",
            "the gossip from the soldiers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Seems they're trying their\x01",
            "damnedest to catch the head\x01",
            "of the Royal Guardsmen.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6EA1")

    label("loc_6848")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_68D7")

    ChrTalk(
        0xA,
        (
            "Hey. Want a copy of the Liberl\x01",
            "News' Martial Arts Competition\x01",
            "Special Edition?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Good for spectators and\x01",
            "participants alike!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6EA1")

    label("loc_68D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_6948")

    ChrTalk(
        0xA,
        "Jeez, why are we so busy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I haven't even been able to\x01",
            "keep up with news from the\x01",
            "tournament!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6EA1")

    label("loc_6948")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_698E")

    ChrTalk(
        0xA,
        (
            "The weather's nice today. \x01",
            "Should sell me some drinks.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6EA1")

    label("loc_698E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_6A0C")

    ChrTalk(
        0xA,
        (
            "There's always so many people\x01",
            "out around tournament time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "The store manager's happy\x01",
            "about that, I'm sure!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6EA1")

    label("loc_6A0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_6AB8")

    ChrTalk(
        0xA,
        (
            "With the queen sick, I don't know\x01",
            "whether or not the festivities will\x01",
            "actually happen this year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Still, doesn't seem to be affecting\x01",
            "tourism very much!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6EA1")

    label("loc_6AB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_6B14")

    ChrTalk(
        0xA,
        (
            "Would you like a sightseeing\x01",
            "map of the city to help \x01",
            "commemorate your trip?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6EA1")

    label("loc_6B14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_6CD2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_6BE9")

    ChrTalk(
        0xA,
        (
            "The articles in the Liberl News\x01",
            "have gotten a bit...dull lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "As uninteresting as the articles themselves\x01",
            "are, though, they're always accompanied by\x01",
            "absolutely breathtaking pictures.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6CCF")

    label("loc_6BE9")

    OP_A2(0x2)

    ChrTalk(
        0xA,
        (
            "The articles in the Liberl News\x01",
            "have gotten a bit...dull lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Why do you think that is?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "As uninteresting as the articles themselves\x01",
            "are, though, they're always accompanied by\x01",
            "absolutely breathtaking pictures.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6CCF")

    Jump("loc_6EA1")

    label("loc_6CD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_6E38")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_6D4C")

    ChrTalk(
        0xA,
        (
            "We carry everything in this store,\x01",
            "from souvenirs to essentials to...\x01",
            "near-unmentionables, perhaps?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6E35")

    label("loc_6D4C")

    OP_A2(0x2)

    ChrTalk(
        0xA,
        (
            "We carry everything in this store,\x01",
            "from souvenirs to essentials to...\x01",
            "near-unmentionables, perhaps?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "We're no Bose Marketplace...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "...but we're also no slouch\x01",
            "when it comes to stocking our\x01",
            "shelves with only the best!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6E35")

    Jump("loc_6EA1")

    label("loc_6E38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_6EA1")

    ChrTalk(
        0xA,
        (
            "Welcome to the Edel Department \x01",
            "Store, where your money goes\x01",
            "far and REALLY wants to play...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6EA1")

    TalkEnd(0xA)
    Return()

    # Function_25_6673 end

    def Function_26_6EA5(): pass

    label("Function_26_6EA5")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_6F49")

    ChrTalk(
        0xFE,
        (
            "#835FI usually don't shop in \x01",
            "places like this.\x02\x03",
            "Scherazard and Anelace wouldn't\x01",
            "stop going on and on about it,\x01",
            "though, so I had to check it out.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6FAA")

    label("loc_6F49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_6F53")
    Jump("loc_6FAA")

    label("loc_6F53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_6F5D")
    Jump("loc_6FAA")

    label("loc_6F5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_6F67")
    Jump("loc_6FAA")

    label("loc_6F67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_6F71")
    Jump("loc_6FAA")

    label("loc_6F71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_6F7B")
    Jump("loc_6FAA")

    label("loc_6F7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_6F85")
    Jump("loc_6FAA")

    label("loc_6F85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_6F8F")
    Jump("loc_6FAA")

    label("loc_6F8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_6F99")
    Jump("loc_6FAA")

    label("loc_6F99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_6FA3")
    Jump("loc_6FAA")

    label("loc_6FA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_6FAA")

    label("loc_6FAA")

    TalkEnd(0x9)
    Return()

    # Function_26_6EA5 end

    def Function_27_6FAE(): pass

    label("Function_27_6FAE")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_725A")
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 9240, 0, 5790, 90)
    SetChrPos(0x102, 9180, 0, 4760, 90)
    SetChrPos(0x108, 8280, 0, 5410, 90)
    TurnDirection(0x8, 0x108, 0)
    SetChrSubChip(0x8, 0)
    OP_A2(0x64C)
    OP_28(0x4B, 0x1, 0x40)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4B, 0x1, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x4B, 0x1, 0x20)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x4B, 0x1, 0x40)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x4B, 0x1, 0x80)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7035")
    OP_28(0x4B, 0x1, 0x100)

    label("loc_7035")

    OP_6D(10020, 0, 5390, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#850FWell, if it isn't Zane \x01",
            "and the new recruits!\x02\x03",
            "Back from the castle already?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505FWell, yeah, I guess we are...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012FAnelace, could we have a moment\x01",
            "of your time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#811FHmm? You hear something juicy\x01",
            "you're looking to share with\x01",
            "me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007FWell...if by 'juicy' you mean\x01",
            "'spit your juice all over in\x01",
            "shock,' then yeah...\x02\x03",
            "...it's a real juice-bomb.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#810FOoooh! You have my undivided\x01",
            "attention!\x02\x03",
            "#850FShould we be talking about \x01",
            "this here, or should I be\x01",
            "sitting down for it?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x3FF)
    NewScene("ED6_DT01/T4101   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_7851")

    label("loc_725A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_7674")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_7307")

    ChrTalk(
        0xFE,
        (
            "#810FThis is the first time I've \x01",
            "had a chance to work with you.\x02\x03",
            "But you two really do a nice\x01",
            "job of covering one another...\x01",
            "if you know what I mean!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7671")

    label("loc_7307")

    OP_A2(0x1)

    ChrTalk(
        0x101,
        "#001FAnelace!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#812FHmmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#008FHey. Why so serious?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#810FIt's just...this is the first\x01",
            "time I've had a chance to work\x01",
            "with you like this.\x02\x03",
            "But you two really do a nice\x01",
            "job of covering one another...\x01",
            "if you know what I mean!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505FUh... Well, we're around each other\x01",
            "all the time, so we've gotten pretty\x01",
            "used to each others' styles, I guess.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7671")

    ChrTalk(
        0xFE,
        (
            "#818F...Hello, anybody home up there? Read\x01",
            "between the lines, you doofus! Guess\x01",
            "I just gotta come out and say it...\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Anelace leaned in close and\x01",
            "whispered into Estelle's ear.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(
        0xFE,
        (
            "#816F(I think you two make a very\x01",
            "cute couple! *giggle*)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#008FWhaaaa?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#811F(Don't be embarrassed! It's\x01",
            "plain to see, with the way\x01",
            "you look at each other.)\x02\x03",
            "#851F(I'm jealous! I mean, I'd kill\x01",
            "for a cute boyfriend like him!)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#503F*blush*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F...Something wrong, ladies?\x02",
    )

    CloseMessageWindow()

    label("loc_7671")

    Jump("loc_7851")

    label("loc_7674")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_767E")
    Jump("loc_7851")

    label("loc_767E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_7688")
    Jump("loc_7851")

    label("loc_7688")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_7754")

    ChrTalk(
        0xFE,
        (
            "#818FHmm...which one to choose...?\x02\x03",
            "#851FAhhh, when they're this cute,\x01",
            "I just can't make up my mind!\x02\x03",
            "#811FI came all this way to the\x01",
            "capital. I might as well enjoy\x01",
            "my time here, you know?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7851")

    label("loc_7754")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_775E")
    Jump("loc_7851")

    label("loc_775E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_7822")

    ChrTalk(
        0xFE,
        (
            "#810FWell, hello, new recruits!\x02\x03",
            "#856FI've got to say you put up\x01",
            "one great fight. You really\x01",
            "deserved that win today.\x02\x03",
            "#816FLet's try it again sometime,\x01",
            "and see if your luck holds!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7851")

    label("loc_7822")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_782C")
    Jump("loc_7851")

    label("loc_782C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_7836")
    Jump("loc_7851")

    label("loc_7836")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_7840")
    Jump("loc_7851")

    label("loc_7840")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_784A")
    Jump("loc_7851")

    label("loc_784A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_7851")

    label("loc_7851")

    TalkEnd(0x8)
    Return()

    # Function_27_6FAE end

    SaveToFile()

Try(main)
