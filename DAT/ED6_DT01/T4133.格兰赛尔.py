from ED6ScenarioHelper import *

def main():
    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4133   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4133.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60084",
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
        'Soldier',                              # 9
        'Soldier',                              # 10
        'Fritz',                                # 11
        'Jill',                                 # 12
        'Hans',                                 # 13
        'Kloe',                                 # 14
        'Dean Collins',                         # 15
        'Kurt',                                 # 16
        'Carla',                                # 17
        'Lucia',                                # 18
        'Miele',                                # 19
        'Phoebe',                               # 20
        'Nana',                                 # 21
        'Armand',                               # 22
        'Ellie',                                # 23
        'Sophina',                              # 24
        'Anelace',                              # 25
        'Letter',                               # 26
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
        'ED6_DT07/CH01540 ._CH',             # 00
        'ED6_DT07/CH01640 ._CH',             # 01
        'ED6_DT07/CH00100 ._CH',             # 02
        'ED6_DT07/CH00110 ._CH',             # 03
        'ED6_DT07/CH01220 ._CH',             # 04
        'ED6_DT07/CH02390 ._CH',             # 05
        'ED6_DT07/CH02550 ._CH',             # 06
        'ED6_DT07/CH00040 ._CH',             # 07
        'ED6_DT07/CH01040 ._CH',             # 08
        'ED6_DT07/CH02600 ._CH',             # 09
        'ED6_DT07/CH01620 ._CH',             # 0A
        'ED6_DT06/CH20021 ._CH',             # 0B
        'ED6_DT07/CH00015 ._CH',             # 0C
        'ED6_DT07/CH01030 ._CH',             # 0D
        'ED6_DT07/CH01070 ._CH',             # 0E
        'ED6_DT07/CH01043 ._CH',             # 0F
        'ED6_DT07/CH02480 ._CH',             # 10
        'ED6_DT07/CH02490 ._CH',             # 11
        'ED6_DT07/CH01140 ._CH',             # 12
        'ED6_DT07/CH01150 ._CH',             # 13
        'ED6_DT07/CH01690 ._CH',             # 14
        'ED6_DT07/CH01630 ._CH',             # 15
    )

    AddCharChipPat(
        'ED6_DT07/CH01540P._CP',             # 00
        'ED6_DT07/CH01640P._CP',             # 01
        'ED6_DT07/CH00100P._CP',             # 02
        'ED6_DT07/CH00110P._CP',             # 03
        'ED6_DT07/CH01220P._CP',             # 04
        'ED6_DT07/CH02390P._CP',             # 05
        'ED6_DT07/CH02550P._CP',             # 06
        'ED6_DT07/CH00040P._CP',             # 07
        'ED6_DT07/CH01040P._CP',             # 08
        'ED6_DT07/CH02600P._CP',             # 09
        'ED6_DT07/CH01620P._CP',             # 0A
        'ED6_DT06/CH20021P._CP',             # 0B
        'ED6_DT07/CH00015P._CP',             # 0C
        'ED6_DT07/CH01030P._CP',             # 0D
        'ED6_DT07/CH01070P._CP',             # 0E
        'ED6_DT07/CH01043P._CP',             # 0F
        'ED6_DT07/CH02480P._CP',             # 10
        'ED6_DT07/CH02490P._CP',             # 11
        'ED6_DT07/CH01140P._CP',             # 12
        'ED6_DT07/CH01150P._CP',             # 13
        'ED6_DT07/CH01690P._CP',             # 14
        'ED6_DT07/CH01630P._CP',             # 15
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
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 7410,
        Z                   = 0,
        Y                   = 3300,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 3020,
        Z                   = 0,
        Y                   = 1290,
        Direction           = 119,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 3390,
        Z                   = 0,
        Y                   = -390,
        Direction           = 36,
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
        X                   = 4740,
        Z                   = 0,
        Y                   = 960,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 4970,
        Z                   = 0,
        Y                   = -600,
        Direction           = 309,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 36400,
        Z                   = 0,
        Y                   = 111030,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 100960,
        Z                   = 0,
        Y                   = 113420,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 97040,
        Z                   = 0,
        Y                   = 114630,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 157590,
        Z                   = 250,
        Y                   = 55130,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = -26610,
        Z                   = 0,
        Y                   = 55500,
        Direction           = 290,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = -27940,
        Z                   = 0,
        Y                   = 55480,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 155000,
        Z                   = 0,
        Y                   = 114600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 158680,
        Z                   = 0,
        Y                   = 110910,
        Direction           = 190,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 35100,
        Z                   = 0,
        Y                   = 53750,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 93210,
        Z                   = 0,
        Y                   = 53470,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = -24660,
        Z                   = -200,
        Y                   = 175270,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1114123,
        ChipIndex           = 0xB,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 57010,
        TriggerZ            = 0,
        TriggerY            = 3770,
        TriggerRange        = 800,
        ActorX              = 57010,
        ActorZ              = 1000,
        ActorY              = 3770,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 22,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 7200,
        TriggerZ            = 0,
        TriggerY            = 1690,
        TriggerRange        = 800,
        ActorX              = 7410,
        ActorZ              = 1500,
        ActorY              = 3300,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 7000,
        TriggerZ            = 0,
        TriggerY            = 4890,
        TriggerRange        = 800,
        ActorX              = 7000,
        ActorZ              = 1000,
        ActorY              = 4890,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 26,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_406",          # 00, 0
        "Function_1_5A8",          # 01, 1
        "Function_2_5EB",          # 02, 2
        "Function_3_601",          # 03, 3
        "Function_4_625",          # 04, 4
        "Function_5_678",          # 05, 5
        "Function_6_99A",          # 06, 6
        "Function_7_C97",          # 07, 7
        "Function_8_DE8",          # 08, 8
        "Function_9_DED",          # 09, 9
        "Function_10_1979",        # 0A, 10
        "Function_11_1E85",        # 0B, 11
        "Function_12_1EC0",        # 0C, 12
        "Function_13_1EEE",        # 0D, 13
        "Function_14_2027",        # 0E, 14
        "Function_15_20DA",        # 0F, 15
        "Function_16_2197",        # 10, 16
        "Function_17_2287",        # 11, 17
        "Function_18_2368",        # 12, 18
        "Function_19_24B2",        # 13, 19
        "Function_20_2534",        # 14, 20
        "Function_21_293F",        # 15, 21
        "Function_22_2FCD",        # 16, 22
        "Function_23_3D43",        # 17, 23
        "Function_24_4954",        # 18, 24
        "Function_25_55AC",        # 19, 25
        "Function_26_58C4",        # 1A, 26
    )


    def Function_0_406(): pass

    label("Function_0_406")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_414")
    OP_A3(0x3FA)
    Event(0, 20)

    label("loc_414")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_427")
    SetMapFlags(0x10000000)
    OP_A3(0x3FB)
    Event(0, 21)

    label("loc_427")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 4)), scpexpr(EXPR_END)), "loc_43A")
    SetMapFlags(0x10000000)
    OP_A3(0x3FC)
    Event(0, 24)

    label("loc_43A")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (122, "loc_446"),
        (SWITCH_DEFAULT, "loc_459"),
    )


    label("loc_446")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_456")
    Event(0, 23)

    label("loc_456")

    Jump("loc_459")

    label("loc_459")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_477")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    Jump("loc_5A7")

    label("loc_477")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_486")
    ClearChrFlags(0x12, 0x80)
    Jump("loc_5A7")

    label("loc_486")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_490")
    Jump("loc_5A7")

    label("loc_490")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_49A")
    Jump("loc_5A7")

    label("loc_49A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_4A4")
    Jump("loc_5A7")

    label("loc_4A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 1)), scpexpr(EXPR_END)), "loc_502")
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 34910, 0, 113190, 0)
    OP_43(0xF, 0x0, 0x0, 0x2)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x10)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x10)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    Jump("loc_5A7")

    label("loc_502")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_529")
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 154870, 0, 51420, 339)
    OP_43(0xF, 0x0, 0x0, 0x3)
    Jump("loc_5A7")

    label("loc_529")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_533")
    Jump("loc_5A7")

    label("loc_533")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_55A")
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 154870, 0, 51420, 339)
    OP_43(0xF, 0x0, 0x0, 0x3)
    Jump("loc_5A7")

    label("loc_55A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_END)), "loc_58C")
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x10)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x10)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x12, 0x80)
    Jump("loc_5A7")

    label("loc_58C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_596")
    Jump("loc_5A7")

    label("loc_596")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_5A0")
    Jump("loc_5A7")

    label("loc_5A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_5A7")

    label("loc_5A7")

    Return()

    # Function_0_406 end

    def Function_1_5A8(): pass

    label("Function_1_5A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5BC")
    OP_1B(0x0, 0x0, 0x19)
    Jump("loc_5CD")

    label("loc_5BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5CD")
    OP_1B(0x0, 0x0, 0x19)

    label("loc_5CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5E6")
    OP_72(0x12, 0x10)
    Jump("loc_5EA")

    label("loc_5E6")

    OP_64(0x0, 0x1)

    label("loc_5EA")

    Return()

    # Function_1_5A8 end

    def Function_2_5EB(): pass

    label("Function_2_5EB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_600")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_5EB")

    label("loc_600")

    Return()

    # Function_2_5EB end

    def Function_3_601(): pass

    label("Function_3_601")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_624")
    OP_8D(0xFE, 153520, 48510, 156020, 53700, 3000)
    Jump("Function_3_601")

    label("loc_624")

    Return()

    # Function_3_601 end

    def Function_4_625(): pass

    label("Function_4_625")

    TalkBegin(0xFE)

    ChrTalk(
        0xE,
        (
            "#780FJill and Hans have come to the capital\x01",
            "as school representatives.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_4_625 end

    def Function_5_678(): pass

    label("Function_5_678")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_6BF")

    ChrTalk(
        0x105,
        (
            "#040FEstelle! Joshua!\x02\x03",
            "I'm so glad to see you again!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_996")

    label("loc_6BF")

    OP_A2(0x5)

    ChrTalk(
        0xFE,
        "#040FEstelle! Joshua!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000FOh, Kloe! There you are!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#040FYeah, I'd heard that Jill and\x01",
            "Hans were here...\x02\x03",
            "So I sneaked out of the castle\x01",
            "and came to see them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FHa ha ha, you sure do know how\x01",
            "to act un-princess-ey!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#040FBut of course! Heh heh. And I\x01",
            "wanted to thank you, too.\x02\x03",
            "You've been nothing but helpful\x01",
            "at every turn.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FUs? Nah, it's totally all you!\x01",
            "We've learned a whole bunch just\x01",
            "from being around you!\x02\x03",
            "You've taught us all about kindness,\x01",
            "and courtesy, and strength of spirit,\x01",
            "and all that other junk!\x02\x03",
            "...Not that it's actually junk...\x01",
            "Ahhh, I'm so bad at this!\x02\x03",
            "What I'm trying to say is, that's\x01",
            "what friends do. So believe me,\x01",
            "no thanks are necessary!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#040FEstelle...\x02",
    )

    CloseMessageWindow()

    label("loc_996")

    TalkEnd(0xFE)
    Return()

    # Function_5_678 end

    def Function_6_99A(): pass

    label("Function_6_99A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_A4C")

    ChrTalk(
        0xFE,
        (
            "#730FLooks like you've been through\x01",
            "a lot...but you seem as full of\x01",
            "energy as ever, thankfully!\x02\x03",
            "Next time you're in Ruan, be sure\x01",
            "to stop by the school, okay?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C93")

    label("loc_A4C")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        "#730FHey, Joshua!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FHans! What brings you here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#730FWhat brings me here? What brings me\x01",
            "here?! All this time, and that's the\x01",
            "first question out of your mouth?!\x02\x03",
            "Do you know how lonely all my\x01",
            "nights have been? Do you?!\x02\x03",
            "I never forgot you, Joshua! I came running\x01",
            "all this way to the capital to see you!\x01",
            "But...where's the princess outfit?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F...Still the same as ever, I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#730FDamn straight. Looks like you've been\x01",
            "through a lot...but you seem as full\x01",
            "of energy as ever, thankfully!\x02\x03",
            "Next time you're in Ruan, be sure\x01",
            "to stop by the school, okay?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C93")

    TalkEnd(0xFE)
    Return()

    # Function_6_99A end

    def Function_7_C97(): pass

    label("Function_7_C97")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_D19")

    ChrTalk(
        0xFE,
        (
            "#640FI heard about your adventures from\x01",
            "Kloe. Sounds like you guys have\x01",
            "been busy.\x02\x03",
            "Ruby Knight Julius, indeed!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DE4")

    label("loc_D19")

    OP_A2(0x3)

    ChrTalk(
        0xFE,
        "#640FEstelle! Joshua!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000FJill?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#640FLong time no see!\x02\x03",
            "I heard about your adventures from\x01",
            "Kloe. Sounds like you guys have\x01",
            "been busy.\x02\x03",
            "Ruby Knight Julius, indeed!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000FHa ha ha!\x02",
    )

    CloseMessageWindow()

    label("loc_DE4")

    TalkEnd(0xFE)
    Return()

    # Function_7_C97 end

    def Function_8_DE8(): pass

    label("Function_8_DE8")

    Call(0, 9)
    Return()

    # Function_8_DE8 end

    def Function_9_DED(): pass

    label("Function_9_DED")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_ECD")

    ChrTalk(
        0xA,
        (
            "Only the Birthday Celebration\x01",
            "could match the excitement of\x01",
            "the Martial Arts Competition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "We've got more foreign visitors than\x01",
            "we've ever had before. Seems like it's\x01",
            "gonna get pretty busy around here!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1975")

    label("loc_ECD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_F37")

    ChrTalk(
        0xA,
        (
            "That's strange... Seems the\x01",
            "castle gates are already closed\x01",
            "for the day. But it's...early!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1975")

    label("loc_F37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_101C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_FA1")

    ChrTalk(
        0xA,
        "Kurt, the bracer, has returned...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "...but he looked a bit on the\x01",
            "pallid side...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1019")

    label("loc_FA1")

    OP_A2(0x2)

    ChrTalk(
        0xA,
        "Kurt, the bracer, has returned...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "...but he looked a bit on the\x01",
            "pallid side...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "I hope he's all right!\x02",
    )

    CloseMessageWindow()

    label("loc_1019")

    Jump("loc_1975")

    label("loc_101C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_1247")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_10AB")

    ChrTalk(
        0xA,
        (
            "Congratulations to you on your\x01",
            "championship victory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Please, enjoy your excursion. Put\x01",
            "all your worries behind you!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1244")

    label("loc_10AB")

    OP_A2(0x2)

    ChrTalk(
        0x101,
        "#000FOh, hey, Fritz.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Madam Estelle. How may I be\x01",
            "of service to you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FUh, actually, we were planning to\x01",
            "stay somewhere else tonight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Yes, I've already been informed\x01",
            "by Monsieur Elnan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Congratulations to you on your\x01",
            "championship victory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Please, enjoy your excursion. Put\x01",
            "all your worries behind you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FWow, leave it to Elnan. Everything\x01",
            "seems really nicely set-up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1244")

    Jump("loc_1975")

    label("loc_1247")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1311")

    ChrTalk(
        0xA,
        (
            "Madam Estelle, Master Joshua...\x01",
            "Today is the day of the tournament\x01",
            "championship, is it not?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Please do take care out there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "You may rest assured that I will\x01",
            "be cheering for you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1975")

    label("loc_1311")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 1)), scpexpr(EXPR_END)), "loc_13B4")

    ChrTalk(
        0xA,
        (
            "Quite a number of soldiers seem\x01",
            "to be patrolling out there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "And all our other guests who have\x01",
            "gone out have invariably been led\x01",
            "right back in.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1975")

    label("loc_13B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_153B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1463")

    ChrTalk(
        0xA,
        (
            "It seems the soldiers are ramping\x01",
            "up their patrol activities as of\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Please take care out there, and\x01",
            "try to come back as soon as you\x01",
            "are able.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1538")

    label("loc_1463")

    OP_A2(0x2)

    ChrTalk(
        0xA,
        (
            "We've received a notice from the\x01",
            "Royal Army...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It seems the soldiers are ramping\x01",
            "up their patrol activities as of\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Please take care out there, and\x01",
            "try to come back as soon as you\x01",
            "are able.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1538")

    Jump("loc_1975")

    label("loc_153B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_157F")

    ChrTalk(
        0xA,
        (
            "We do not wish to see any of\x01",
            "our guests get injured.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1975")

    label("loc_157F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_16B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1603")

    ChrTalk(
        0xA,
        (
            "Come to think of it, there are\x01",
            "two other bracers staying at this\x01",
            "hotel as well...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Have you met them yet?\x02",
    )

    CloseMessageWindow()
    Jump("loc_16AD")

    label("loc_1603")

    OP_A2(0x2)

    ChrTalk(
        0xA,
        (
            "Welcome back, Master Joshua\x01",
            "and Madam Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Come to think of it, there are\x01",
            "two other bracers staying at this\x01",
            "hotel as well...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Have you met them yet?\x02",
    )

    CloseMessageWindow()

    label("loc_16AD")

    Jump("loc_1975")

    label("loc_16B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_16DB")

    ChrTalk(
        0xA,
        "Going out? Very good, then.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1975")

    label("loc_16DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_18CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_END)), "loc_1770")

    ChrTalk(
        0xA,
        (
            "Your room is up the stairs, at the\x01",
            "far end of the hall. Room 202.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If you have need of anything,\x01",
            "please contact the front.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18C8")

    label("loc_1770")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_17E4")

    ChrTalk(
        0xA,
        (
            "I'm terribly sorry, but your room\x01",
            "is not yet ready, I'm afraid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Check-in time is three o'clock.\x02",
    )

    CloseMessageWindow()
    Jump("loc_18C8")

    label("loc_17E4")

    OP_A2(0x2)

    ChrTalk(
        0xA,
        (
            "I'm terribly sorry, but your room\x01",
            "is not yet ready, I'm afraid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Check-in time is three o'clock.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FWe can leave the checking in\x01",
            "for later, then. For now, we\x01",
            "should go find Zane.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000FSounds like a plan!\x02",
    )

    CloseMessageWindow()

    label("loc_18C8")

    Jump("loc_1975")

    label("loc_18CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1975")

    ChrTalk(
        0xA,
        (
            "We have a large number of guests who\x01",
            "have come to see the tournament.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "There are also other participants\x01",
            "in the tournament who are staying\x01",
            "at this hotel.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1975")

    TalkEnd(0xA)
    Return()

    # Function_9_DED end

    def Function_10_1979(): pass

    label("Function_10_1979")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_1986")
    Jump("loc_1E81")

    label("loc_1986")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_1990")
    Jump("loc_1E81")

    label("loc_1990")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_199A")
    Jump("loc_1E81")

    label("loc_199A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_19A4")
    Jump("loc_1E81")

    label("loc_19A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_19AE")
    Jump("loc_1E81")

    label("loc_19AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 3)), scpexpr(EXPR_END)), "loc_1A0E")

    ChrTalk(
        0xFE,
        (
            "#842F...Was I seeing things...?\x02\x03",
            "...or did something just flash\x01",
            "past the window?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E81")

    label("loc_1A0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 1)), scpexpr(EXPR_END)), "loc_1AA8")

    ChrTalk(
        0xFE,
        (
            "#840FYou should get some rest for\x01",
            "tomorrow's match.\x02\x03",
            "Keeping yourselves fit and ready\x01",
            "for anything is an important part\x01",
            "of being a bracer.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E81")

    label("loc_1AA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_1C39")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1B40")

    ChrTalk(
        0xFE,
        (
            "'Zane the Immovable' may have stolen the spot-\x01",
            "light, but you're the ones I really noticed.\x01",
            "You guys fought amazingly well today.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C36")

    label("loc_1B40")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        "Hey.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "'Zane the Immovable' may have stolen the spot-\x01",
            "light, but you're the ones I really noticed.\x01",
            "You guys fought amazingly well today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You showed a lot of skill and\x01",
            "teamwork out there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You've got a bright future, for\x01",
            "sure!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C36")

    Jump("loc_1E81")

    label("loc_1C39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_1C43")
    Jump("loc_1E81")

    label("loc_1C43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1E66")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1D2D")

    ChrTalk(
        0xFE,
        (
            "We both fought, and we both advanced.\x01",
            "It was an excellent day for us all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I am more convinced than ever that when we\x01",
            "ultimately face off against one another, we'll\x01",
            "be ready for it...and it will be glorious!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E63")

    label("loc_1D2D")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        "Hey, Estelle and Joshua!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We both fought, and we both advanced.\x01",
            "It was an excellent day for us all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I spoke with Carna. She seems to think\x01",
            "you have quite a lot of skill.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I am convinced that when we ultimately\x01",
            "face off against one another, we'll be\x01",
            "ready for it...and it will be glorious!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E63")

    Jump("loc_1E81")

    label("loc_1E66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_1E70")
    Jump("loc_1E81")

    label("loc_1E70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_1E7A")
    Jump("loc_1E81")

    label("loc_1E7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1E81")

    label("loc_1E81")

    TalkEnd(0xFE)
    Return()

    # Function_10_1979 end

    def Function_11_1E85(): pass

    label("Function_11_1E85")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "What a hotel. I wish I'd come\x01",
            "with my husband!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_1E85 end

    def Function_12_1EC0(): pass

    label("Function_12_1EC0")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "This sofa's soooo soft and comfy!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_1EC0 end

    def Function_13_1EEE(): pass

    label("Function_13_1EEE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 1)), scpexpr(EXPR_END)), "loc_1F8E")

    ChrTalk(
        0xFE,
        (
            "Maybe I'll go to bed early so\x01",
            "I can feel well-rested for\x01",
            "tomorrow's match...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I need a nice, warm soak to lift\x01",
            "the weary from my bones...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2023")

    label("loc_1F8E")


    ChrTalk(
        0xFE,
        (
            "Preliminaries or no, it was\x01",
            "pretty wild today. I can't\x01",
            "wait for tomorrow!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I screamed myself hoarse, I did!\x01",
            "Bet you can't even hear this...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2023")

    TalkEnd(0xFE)
    Return()

    # Function_13_1EEE end

    def Function_14_2027(): pass

    label("Function_14_2027")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 1)), scpexpr(EXPR_END)), "loc_2089")

    ChrTalk(
        0xFE,
        (
            "Going out with a guy from the\x01",
            "same block, huh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Doesn't breaking up suck?\x02",
    )

    CloseMessageWindow()
    Jump("loc_20D6")

    label("loc_2089")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "You know my sister? She broke\x01",
            "up with her boyfriend, or some\x01",
            "junk...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20D6")

    TalkEnd(0xFE)
    Return()

    # Function_14_2027 end

    def Function_15_20DA(): pass

    label("Function_15_20DA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 1)), scpexpr(EXPR_END)), "loc_2127")
    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "It does suck. So bad.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I would be so embarrassed...\x02",
    )

    CloseMessageWindow()
    Jump("loc_2193")

    label("loc_2127")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Seriously?! No way!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, isn't it better like that\x01",
            "or something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "He WAS kind of a jerk...\x02",
    )

    CloseMessageWindow()

    label("loc_2193")

    TalkEnd(0xFE)
    Return()

    # Function_15_20DA end

    def Function_16_2197(): pass

    label("Function_16_2197")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 1)), scpexpr(EXPR_END)), "loc_2238")

    ChrTalk(
        0xFE,
        (
            "I really wanted to spend a night\x01",
            "on the town with my girlfriend...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...but wouldn't you know it,\x01",
            "there's a new curfew that starts\x01",
            "TONIGHT!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2283")

    label("loc_2238")


    ChrTalk(
        0xFE,
        (
            "We're going out to look at the\x01",
            "city skyline.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "The night is young!\x02",
    )

    CloseMessageWindow()

    label("loc_2283")

    TalkEnd(0xFE)
    Return()

    # Function_16_2197 end

    def Function_17_2287(): pass

    label("Function_17_2287")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 1)), scpexpr(EXPR_END)), "loc_2303")

    ChrTalk(
        0xFE,
        (
            "Sometimes taking it easy is...\x01",
            "not so bad, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As long as my sweetie pie is\x01",
            "here next to me...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2364")

    label("loc_2303")


    ChrTalk(
        0xFE,
        (
            "*giggle* I'm so looking forward\x01",
            "to seeing the city tonight with\x01",
            "him. It sounds so romantic!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2364")

    TalkEnd(0xFE)
    Return()

    # Function_17_2287 end

    def Function_18_2368(): pass

    label("Function_18_2368")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 1)), scpexpr(EXPR_END)), "loc_23F5")

    ChrTalk(
        0xFE,
        (
            "The streets were really quiet\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With the championship tomorrow,\x01",
            "I thought things'd be more...\x01",
            "you know...lively.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24AE")

    label("loc_23F5")


    ChrTalk(
        0xFE,
        (
            "This is my first time here.\x01",
            "Aren't these rooms amazing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But I have to say I prefer my\x01",
            "brother's hotel to this one...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's just so hard to relax amidst\x01",
            "all this luxury...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24AE")

    TalkEnd(0xFE)
    Return()

    # Function_18_2368 end

    def Function_19_24B2(): pass

    label("Function_19_24B2")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "#811FHey-hey, newbies!\x02\x03",
            "I'm just about to go take a shower.\x02\x03",
            "#851FI'm drenched in sweat, and I\x01",
            "don't like it one bit!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_24B2 end

    def Function_20_2534(): pass

    label("Function_20_2534")

    EventBegin(0x0)
    OP_6D(7350, 0, -5650, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 6930, 0, 1460, 0)
    SetChrPos(0x102, 7840, 0, 1460, 0)
    OP_4A(0xA, 255)
    FadeToBright(1500, 0)
    OP_6D(7010, 0, 2460, 4000)

    ChrTalk(
        0xA,
        (
            "Good evening. Welcome to the\x01",
            "Hotel Roenbaum.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Were you looking to stay\x01",
            "for the night?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006FYes. We're with the Bracer Guild...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FWe were told that a room would\x01",
            "be ready for us. Can you please\x01",
            "confirm that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Ahh, so that was for you two.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Yes, we do have a reservation\x01",
            "for the both of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#506FWhew... That's a relief.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019FWe'll have to say thanks\x01",
            "to Elnan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Estelle and Joshua, correct?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'm sorry to ask, but may I\x01",
            "please see your identification\x01",
            "as bracers?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501FOh, just a second...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Estelle showed the clerk her Bracer Notebook.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(
        0xA,
        "Yes, that will be fine.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "And this is for you.\x02",
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
            "Room 202 Key\x07\x00",
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3E(0x375, 1)

    ChrTalk(
        0xA,
        (
            "Just take the stairs up, and\x01",
            "it'll be on your left.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If you have need of anything,\x01",
            "please contact the front.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x616)
    OP_A2(0x617)
    OP_1B(0x0, 0x0, 0x19)
    OP_4B(0xA, 255)
    EventEnd(0x0)
    Return()

    # Function_20_2534 end

    def Function_21_293F(): pass

    label("Function_21_293F")

    ClearMapFlags(0x10000000)
    EventBegin(0x0)
    OP_6D(6980, 0, -3210, 0)
    OP_67(0, 8310, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(337000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 6760, 0, -3090, 180)
    SetChrPos(0x102, 7760, 0, -3080, 180)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x8, 6510, -250, -4770, 0)
    SetChrPos(0x9, 7820, -250, -4970, 0)
    FadeToBright(1500, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#4P#008FUm... Thanks for escorting us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FWe appreciate it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1PYou've got to be kidding.\x01",
            "We're big fans of yours.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1PWe're all in the same army,\x01",
            "but I don't know...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1PThose Special Ops types just rub\x01",
            "me the wrong way, for some reason.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1PNo kidding. I just don't get\x01",
            "what goes through their heads.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1PDon't you think talking like\x01",
            "this is a little disrespectful\x01",
            "of Colonel Richard, though?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1PWell, that's why we're putting so\x01",
            "much faith in your participation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#1PGood luck with tomorrow's match!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4P#506FHa ha ha... Thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FWe'll do everything we can.\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x40)
    SetChrFlags(0x9, 0x40)
    OP_8C(0x8, 180, 400)

    def lambda_2C5C():
        OP_8E(0xFE, 0x196E, 0xFFFFFE0C, 0xFFFFE2D2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2C5C)
    OP_8C(0x9, 180, 400)

    def lambda_2C7E():
        OP_8E(0xFE, 0x1E8C, 0xFFFFFE0C, 0xFFFFE2D2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2C7E)
    WaitChrThread(0x8, 0x1)
    SetChrFlags(0x8, 0x4)

    def lambda_2CA3():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_2CA3)

    def lambda_2CB5():
        OP_8E(0xFE, 0x196E, 0xFFFFFF06, 0xFFFFDCD8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2CB5)
    WaitChrThread(0x9, 0x1)
    SetChrFlags(0x9, 0x4)

    def lambda_2CDA():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_2CDA)

    def lambda_2CEC():
        OP_8E(0xFE, 0x1E8C, 0xFFFFFF06, 0xFFFFDCD8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_2CEC)
    Sleep(1000)
    OP_22(0x7, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#007FWhew... This is all kind of\x01",
            "complicated, huh?\x02\x03",
            "I don't think those guys know a\x01",
            "thing about the colonel's plot.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#012FThey seem to think the Intelligence\x01",
            "Division are just regular soldiers.\x02\x03",
            "Whatever info comes down the\x01",
            "chain of command, they accept\x01",
            "as the truth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505FHmmm...\x02\x03",
            "Well, I'd hate to make enemies\x01",
            "of them, since they're rooting\x01",
            "for us, and all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FRegardless of anything else, it'd\x01",
            "be wisest not to stir up trouble\x01",
            "with the rank and file soldiers.\x02\x03",
            "What do you say we stay in our\x01",
            "room tonight and just rest up?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006FOkay...\x02",
    )

    CloseMessageWindow()
    Fade(1000)
    SetChrPos(0x101, 7090, 0, -2590, 0)
    SetChrPos(0x102, 7090, 0, -2590, 0)
    OP_6D(7090, 0, -2590, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_A2(0x629)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    OP_1B(0x0, 0x0, 0x19)
    EventEnd(0x0)
    Return()

    # Function_21_293F end

    def Function_22_2FCD(): pass

    label("Function_22_2FCD")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3A7D")
    OP_A2(0x618)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3015")

    ChrTalk(
        0x101,
        (
            "#006F202...\x01",
            "Yep, this is our room.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3043")

    label("loc_3015")


    ChrTalk(
        0x102,
        (
            "#010F202...\x01",
            "Looks like this is our room.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3043")

    Sleep(100)
    Fade(1000)
    SetChrPos(0x101, 34420, 0, 108910, 0)
    SetChrPos(0x102, 35770, 0, 108690, 0)
    OP_6D(34410, 0, 115500, 0)
    OP_67(0, 5930, -10000, 0)
    OP_6B(1890, 0)
    OP_6C(315000, 0)
    OP_6E(437, 0)
    OP_22(0x6, 0x0, 0x64)
    OP_6D(35020, 0, 111190, 2000)

    ChrTalk(
        0x101,
        "#004FHeeeey, nice room.\x02",
    )

    CloseMessageWindow()

    def lambda_30E5():
        OP_6D(31860, 0, 115500, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_30E5)

    def lambda_30FD():
        OP_8E(0xFE, 0x8674, 0x0, 0x1B972, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_30FD)
    Sleep(600)

    def lambda_311D():
        OP_8E(0xFE, 0x8BBA, 0x0, 0x1B9C2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_311D)
    WaitChrThread(0x101, 0x1)
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_3154():
        OP_8E(0xFE, 0x7B8E, 0x0, 0x1C32C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3154)
    WaitChrThread(0x102, 0x1)
    TurnDirection(0x102, 0x101, 400)
    WaitChrThread(0x101, 0x1)
    OP_8C(0x101, 0, 400)

    ChrTalk(
        0x101,
        (
            "#001FLook! You can see the Grand\x01",
            "Arena from here!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_31BE():
        OP_6D(31160, 0, 115440, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_31BE)

    def lambda_31D6():
        OP_6B(1700, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_31D6)

    def lambda_31E6():
        OP_6C(306000, 2000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_31E6)

    def lambda_31F6():

        label("loc_31F6")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_31F6")

    QueueWorkItem2(0x101, 1, lambda_31F6)
    OP_8E(0x102, 0x7EF4, 0x0, 0x1C32C, 0xFA0, 0x0)
    OP_8C(0x102, 0, 400)

    def lambda_3222():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3222)
    WaitChrThread(0x102, 0x2)

    ChrTalk(
        0x102,
        (
            "#014F#6PWow... No kidding.\x02\x03",
            "#019FThey really didn't skimp\x01",
            "on anything here.\x02\x03",
            "I guess we can use this as our base\x01",
            "of operations, so to speak...at\x01",
            "least until the competition's over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#503F#6P(So...Joshua and I have to share\x01",
            "this room for a while...?)\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x101)

    ChrTalk(
        0x101,
        (
            "#504F#3S#6P(GAH! What am I thinking?!\x01",
            "Bad thoughts! Bad thoughts!)\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)
    Sleep(400)

    ChrTalk(
        0x102,
        "#013FUh, Estelle...?\x02",
    )

    CloseMessageWindow()
    OP_9E(0x101, 0xF, 0x0, 0x12C, 0xFA0)
    Sleep(200)
    TurnDirection(0x101, 0x102, 800)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_94(0x1, 0x101, 0xB4, 0x1F4, 0xFA0, 0x0)

    ChrTalk(
        0x101,
        "#008F#3P#3SYES! Uh, I mean, yes?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#017FIt just occurred to me that this\x01",
            "might be a little weird...\x02\x03",
            "#010FBut, uh...I mean, we're family\x01",
            "...right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F#3P...Huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015FI might not be as dependable as Dad is...\x02\x03",
            "And I'm not as good a listener as Schera...\x02\x03",
            "#010FBut still, I'm your brother, and I want you\x01",
            "to know that I'm there if you need support.\x02\x03",
            "If there's ever anything bothering you,\x01",
            "I just want you to know that you can\x01",
            "always come to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F#3P...Oh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#017FI've been getting kind of a weird\x01",
            "feeling from you lately...\x02\x03",
            "#013FIf I've got this all wrong,\x01",
            "I'm sorry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F#3P*sigh*\x01",
            "You're just so...you.\x02\x03",
            "As smart as you are, sometimes\x01",
            "you can be so clueless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014FWhat...?\x02",
    )

    CloseMessageWindow()
    OP_94(0x1, 0x101, 0x0, 0x1F4, 0x3E8, 0x0)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#008F#3PThank you...but you don't\x01",
            "need to worry.\x02\x03",
            "#007FI know I've probably been acting\x01",
            "kinda strange lately...\x02\x03",
            "It's not all that serious or painful...\x02\x03",
            "I'm just trying to sort my\x01",
            "feelings out.\x02\x03",
            "#006FSo...I'll be okay.\x02\x03",
            "Just as long as you watch\x01",
            "out for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015FI see...\x02\x03",
            "#010FOkay, then. I'll keep my\x01",
            "worry in check.\x02\x03",
            "And in return, you let me know\x01",
            "when you've taken care of\x01",
            "whatever's bothering you.\x02\x03",
            "#014FI won't ask you to tell me\x01",
            "anything you're not ready\x01",
            "to yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#503F#3PU-Umm...\x02\x03",
            "Okay... Once I have everything\x01",
            "straight, I'll be glad to tell you\x01",
            "what's on my heart...er, mind!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014FHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F#3PErr, noting! Norhinf!\x02\x03",
            "#006FIt's still kind of early...but\x01",
            "do you want to turn in?\x02\x03",
            "Everything that's been going\x01",
            "on has worn me out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FYeah... We do have that match\x01",
            "tomorrow...\x02\x03",
            "Let's get our stuff put away\x01",
            "and get some shut-eye.\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_22(0xD, 0x0, 0x64)
    Sleep(3000)
    SetMapFlags(0x100000)
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T4103   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    label("loc_3A7D")

    OP_20(0x5DC)
    Fade(1000)
    SetChrPos(0x102, 56580, 0, 2320, 0)
    SetChrPos(0x101, 57920, 0, 2070, 0)
    OP_6D(56650, 0, 3000, 0)
    OP_0D()
    OP_22(0x82, 0x0, 0x64)
    OP_22(0x8C, 0x0, 0x32)
    Sleep(1000)
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#2P#505FHuh...?\x02\x03",
            "Did you just hear something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#510F...\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_1D(0x51)
    Sleep(500)

    ChrTalk(
        0x102,
        (
            "#015F(Be on alert when we go inside,\x01",
            "and be ready for a fight if things\x01",
            "don't look right.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2P#004F(Huh...?!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F(I think we've got a trespasser.)\x02\x03",
            "(There might be explosives set,\x01",
            "so be careful.)\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(
        0x101,
        "#2P#580F(W-Wait... You're kidding, right?)\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#015F(I need you to do exactly as\x01",
            "I tell you, no questions.)\x02\x03",
            "(If you'd rather stay out\x01",
            "here, that's fine with me.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2P#005F(N-No way!)\x02\x03",
            "(I'm fine. Let's go inside!)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#013F(...All right.)\x02",
    )

    CloseMessageWindow()
    OP_A2(0x62A)
    OP_64(0x0, 0x1)
    OP_71(0x12, 0x10)
    OP_1C(0x12, 0x0, 0xFFFF)
    FadeToDark(500, 0, -1)
    OP_0D()
    Call(0, 23)
    Return()

    # Function_22_2FCD end

    def Function_23_3D43(): pass

    label("Function_23_3D43")

    EventBegin(0x0)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, -24300, -200, 175600, 0)
    OP_6D(-25590, 0, 170160, 0)
    OP_67(0, 7400, -10000, 0)
    OP_6B(1500, 0)
    OP_6C(325000, 0)
    OP_6E(478, 0)
    SetChrPos(0x101, -23950, 0, 168970, 0)
    SetChrPos(0x102, -25320, 0, 168830, 0)
    SetChrChipByIndex(0x101, 2)
    SetChrChipByIndex(0x102, 3)
    FadeToDark(0, 0, -1)
    OP_22(0x6, 0x0, 0x64)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_6D(-25590, 0, 172760, 1000)

    ChrTalk(
        0x101,
        "#004F#5POh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F#5PLooks like he got away.\x02",
    )

    CloseMessageWindow()
    OP_51(0x102, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x102, 65535)
    Sleep(400)

    ChrTalk(
        0x102,
        (
            "#013F#5PBut that's strange... I don't\x01",
            "get the sense that anyone's\x01",
            "been in here.\x02\x03",
            "Nor does it feel like there\x01",
            "are any traps set.\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x101, 65535)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#004F#2PY-You can seriously tell\x01",
            "that kind of thing?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3F1B():

        label("loc_3F1B")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_3F1B")

    QueueWorkItem2(0x101, 2, lambda_3F1B)

    def lambda_3F2C():
        OP_6D(-24940, 0, 175710, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3F2C)

    def lambda_3F44():
        OP_8E(0xFE, 0xFFFFA088, 0x0, 0x2AB66, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3F44)
    Sleep(800)

    def lambda_3F64():
        OP_8E(0xFE, 0xFFFF9FA2, 0x0, 0x2A634, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3F64)
    WaitChrThread(0x102, 0x2)

    def lambda_3F84():

        label("loc_3F84")

        OP_8C(0xFE, 0, 0)
        OP_48()
        Jump("loc_3F84")

    QueueWorkItem2(0x102, 1, lambda_3F84)
    WaitChrThread(0x102, 0x2)
    OP_44(0x102, 0xFF)
    Fade(500)
    SetChrChipByIndex(0x102, 12)
    OP_0D()

    ChrTalk(
        0x102,
        (
            "#015F#5PI guess this is all that\x01",
            "was left behind.\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 0x2)

    ChrTalk(
        0x101,
        "#505FWhat...a letter?\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x19, 0x80)
    Fade(500)
    SetChrChipByIndex(0x102, 65535)
    OP_0D()
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Joshua broke the seal on the letter.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Sleep(400)

    ChrTalk(
        0x102,
        (
            "#012F#6P'Tonight, at the stroke of ten,\x01",
            "come to the cathedral.'\x02\x03",
            "'Please, tell no one of this.'\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#004F...And that's it?\x02\x03",
            "#505FAnd what cathedral? That huge church\x01",
            "over in the West Block?\x02\x03",
            "It's already almost ten o'clock now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#015F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007FHmmm... Well, it sure sounds\x01",
            "suspicious, but nothing ventured,\x01",
            "nothing gained.\x02\x03",
            "#006FWhat do you think?\x01",
            "Should we go for it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#510F#3S#6P...Absolutely NOT!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#580FWh-What was that for?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#013F#4PI'm sorry. I didn't mean to yell.\x02\x03",
            "#010FLook, didn't those soldiers\x01",
            "just say that they were going\x01",
            "to reinforce tonight's patrols?\x02\x03",
            "You can bet they'll be keeping\x01",
            "a close watch on the West\x01",
            "Block, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004FOh, right.\x02\x03",
            "#007FStill, I hate to just pretend\x01",
            "we never got it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F#4PI'll go by myself, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004FHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F#4PIt's easier for one person\x01",
            "to stay hidden than two.\x02\x03",
            "I shouldn't have any real trouble\x01",
            "getting to the cathedral unnoticed.\x02",
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
            "#010F#4PListen, if all I'm doing is\x01",
            "scoping out the situation, I\x01",
            "can handle it on my own.\x02\x03",
            "I just need you to stay here--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#509F#3SHey.\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F#4PHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009FI'm no less a bracer than you are.\x02\x03",
            "I can handle myself, and\x01",
            "I won't slow you down.\x02\x03",
            "Your silver tongue's not going to work on me\x01",
            "this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F#4PEstelle...\x01",
            "That's not what I meant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#500FI know it's not that you\x01",
            "don't trust me.\x02\x03",
            "I can tell you're worried about me...\x01",
            "or more that you're worried FOR me.\x02\x03",
            "#006FWhat are you not telling me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F#4P...\x02\x03",
            "How can you tell that I'm\x01",
            "keeping something from you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006FI'm closer to you than just\x01",
            "about anyone, Joshua.\x02\x03",
            "There's nothing you can keep from\x01",
            "me...not for very long, anyway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F#4P...\x02\x03",
            "#015F(...I'm impressed.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004FHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#4PAll right. If you want to come\x01",
            "with me, I won't try to stop you.\x02\x03",
            "It's almost ten now, though,\x01",
            "so we have to hurry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#008FOh...okay!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F#4PBut I want you to promise\x01",
            "me something.\x02\x03",
            "If anything goes wrong, you\x01",
            "do exactly as I tell you.\x02\x03",
            "One wrong move could be fatal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004FOkay...\x01",
            "I promise.\x02\x03",
            "#006FLet's get a move on, then.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_20(0x5DC)
    Fade(1500)
    SetChrPos(0x101, -24630, 0, 173630, 180)
    SetChrPos(0x102, -24630, 0, 173630, 180)
    OP_6D(-24630, 0, 173630, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_28(0x48, 0x1, 0x100)
    OP_1B(0x0, 0x0, 0xFFFF)
    OP_A2(0x62B)
    Sleep(500)
    EventEnd(0x0)
    OP_1D(0x54)
    Return()

    # Function_23_3D43 end

    def Function_24_4954(): pass

    label("Function_24_4954")

    ClearMapFlags(0x10000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F14")
    EventBegin(0x0)
    OP_6D(6980, 0, -3210, 0)
    OP_67(0, 8310, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(337000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 6760, 0, -3090, 180)
    SetChrPos(0x102, 7760, 0, -3080, 180)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x8, 6510, -250, -4770, 0)
    SetChrPos(0x9, 7820, -250, -4970, 0)
    FadeToBright(1500, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x48, 0x1, 0x800)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A0D")
    OP_28(0x48, 0x1, 0x800)
    Jump("loc_4A5E")

    label("loc_4A0D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x48, 0x1, 0x1000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A22")
    OP_28(0x48, 0x1, 0x1000)
    Jump("loc_4A5E")

    label("loc_4A22")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x48, 0x1, 0x2000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A37")
    OP_28(0x48, 0x1, 0x2000)
    Jump("loc_4A5E")

    label("loc_4A37")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x48, 0x1, 0x4000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A4C")
    OP_28(0x48, 0x1, 0x4000)
    Jump("loc_4A5E")

    label("loc_4A4C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x48, 0x1, 0x8000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A5E")
    OP_28(0x48, 0x1, 0x8000)

    label("loc_4A5E")


    ChrTalk(
        0x8,
        "#1PDamn troublemakers...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1PYou need to stay indoors while\x01",
            "we're trying to keep an eye out\x01",
            "for terrorist activity.\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x40)
    SetChrFlags(0x9, 0x40)
    OP_8C(0x8, 180, 400)

    def lambda_4AF2():
        OP_8E(0xFE, 0x196E, 0xFFFFFE0C, 0xFFFFE2D2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4AF2)
    OP_8C(0x9, 180, 400)

    def lambda_4B14():
        OP_8E(0xFE, 0x1E8C, 0xFFFFFE0C, 0xFFFFE2D2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4B14)
    WaitChrThread(0x8, 0x1)
    SetChrFlags(0x8, 0x4)

    def lambda_4B39():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_4B39)

    def lambda_4B4B():
        OP_8E(0xFE, 0x196E, 0xFFFFFF06, 0xFFFFDCD8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_4B4B)
    WaitChrThread(0x9, 0x1)
    SetChrFlags(0x9, 0x4)

    def lambda_4B70():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_4B70)

    def lambda_4B82():
        OP_8E(0xFE, 0x1E8C, 0xFFFFFF06, 0xFFFFDCD8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_4B82)
    Sleep(2000)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#007FAwww, man...\x01",
            "Back to square one.\x02\x03",
            "We'll just have to try it again.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#012FThat was educational, though.\x02\x03",
            "Some of the soldiers seem to have\x01",
            "stationary posts, while others patrol\x01",
            "on a fixed route.\x02\x03",
            "First things first, we need to keep our distance\x01",
            "from the soldiers. Easy enough, but it may\x01",
            "require us to go well out of our way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505FGot it... So, in other words,\x01",
            "we can't take the direct route\x01",
            "to the west.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FNow, as for the ones who are\x01",
            "actively patrolling...\x02\x03",
            "They can't see nearly as well at night, so\x01",
            "as long as we don't approach them from the\x01",
            "front, we should be able to get by them.\x02\x03",
            "The main thing will be to learn\x01",
            "their patrol routes and stay out\x01",
            "of their direct line of sight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006FOkay. Let's give this a shot, then.\x02",
    )

    CloseMessageWindow()
    Fade(1000)
    SetChrPos(0x101, 7090, 0, -2590, 0)
    SetChrPos(0x102, 7090, 0, -2590, 0)
    OP_6D(7090, 0, -2590, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_A2(0x62D)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    EventEnd(0x0)
    Jump("loc_55AB")

    label("loc_4F14")

    EventBegin(0x0)
    OP_6D(7010, 0, -2900, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 6760, 0, -3090, 180)
    SetChrPos(0x102, 7760, 0, -3080, 180)
    TurnDirection(0x101, 0x102, 0)
    TurnDirection(0x102, 0x101, 0)
    FadeToBright(1500, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x48, 0x1, 0x800)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_517F")
    OP_28(0x48, 0x1, 0x800)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5095")

    ChrTalk(
        0x102,
        (
            "#012FSome of the soldiers seem to have\x01",
            "stationary posts, while others patrol\x01",
            "on a fixed route.\x02\x03",
            "First things first, we need to keep our distance\x01",
            "from the soldiers. Easy enough, but it may\x01",
            "require us to go well out of our way.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_517C")

    label("loc_5095")


    ChrTalk(
        0x102,
        (
            "#012FAs for the patrolmen, they can't see well\x01",
            "at night, so as long as we don't approach\x01",
            "them from the front, we should be okay.\x02\x03",
            "The main thing will be to learn\x01",
            "their patrol routes and stay out\x01",
            "of their direct line of sight.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_517C")

    Jump("loc_55A9")

    label("loc_517F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x48, 0x1, 0x1000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5371")
    OP_28(0x48, 0x1, 0x1000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5287")

    ChrTalk(
        0x102,
        (
            "#012FSome of the soldiers seem to have\x01",
            "stationary posts, while others patrol\x01",
            "on a fixed route.\x02\x03",
            "First things first, we need to keep our distance\x01",
            "from the soldiers. Easy enough, but it may\x01",
            "require us to go well out of our way.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_536E")

    label("loc_5287")


    ChrTalk(
        0x102,
        (
            "#012FAs for the patrolmen, they can't see well\x01",
            "at night, so as long as we don't approach\x01",
            "them from the front, we should be okay.\x02\x03",
            "The main thing will be to learn\x01",
            "their patrol routes and stay out\x01",
            "of their direct line of sight.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_536E")

    Jump("loc_55A9")

    label("loc_5371")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x48, 0x1, 0x2000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_53E8")
    OP_28(0x48, 0x1, 0x2000)

    ChrTalk(
        0x102,
        (
            "#015FIt looks like there aren't as\x01",
            "many soldiers on patrol, but\x01",
            "we still have to be careful.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55A9")

    label("loc_53E8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x48, 0x1, 0x4000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5480")
    OP_28(0x48, 0x1, 0x4000)

    ChrTalk(
        0x102,
        (
            "#010FThey've seriously lowered the\x01",
            "count of patrolling soldiers.\x02\x03",
            "Maybe it's almost time for the\x01",
            "night patrol to go off duty.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55A9")

    label("loc_5480")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x48, 0x1, 0x8000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_54F8")
    OP_28(0x48, 0x1, 0x8000)

    ChrTalk(
        0x102,
        (
            "#010FWith no soldiers in front of the\x01",
            "hotel, getting to the South\x01",
            "Block should be no problem.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55A9")

    label("loc_54F8")


    ChrTalk(
        0x102,
        (
            "#010FIt looks like the soldiers have\x01",
            "almost all withdrawn.\x02\x03",
            "We can just take the main street out\x01",
            "of the South Block, and it'll take us\x01",
            "to the West Block and the cathedral.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_55A9")

    EventEnd(0x0)

    label("loc_55AB")

    Return()

    # Function_24_4954 end

    def Function_25_55AC(): pass

    label("Function_25_55AC")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 0)), scpexpr(EXPR_END)), "loc_574A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_569C")
    OP_A2(0x0)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010FLet's call it quits for tonight.\x01",
            "We can go back to our room and\x01",
            "get some rest.\x02\x03",
            "There's no way we'll be able\x01",
            "to go out without bumping into\x01",
            "the soldiers.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#000FYeah, you're probably right.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5747")

    label("loc_569C")

    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010FLet's call it quits for tonight.\x01",
            "We can go back to our room and\x01",
            "get some rest.\x02\x03",
            "There's no way we'll be able\x01",
            "to go out without bumping into\x01",
            "the soldiers.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5747")

    Jump("loc_58A8")

    label("loc_574A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5817")
    OP_A2(0x0)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010FIt's really too late to go outside now.\x02\x03",
            "We have the match tomorrow, so\x01",
            "why don't we just take advantage\x01",
            "of the chance to rest?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#000FYeah, you're probably right.\x02",
    )

    CloseMessageWindow()
    Jump("loc_58A8")

    label("loc_5817")

    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010FIt's really too late to go outside now.\x02\x03",
            "We have the match tomorrow, so\x01",
            "why don't we just take advantage\x01",
            "of the chance to rest?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_58A8")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_25_55AC end

    def Function_26_58C4(): pass

    label("Function_26_58C4")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Office\x01",
            "仸Authorized Personnel Only\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_26_58C4 end

    SaveToFile()

Try(main)
