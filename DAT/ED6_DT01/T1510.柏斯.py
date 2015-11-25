from ED6ScenarioHelper import *

def main():
    # 柏斯

    CreateScenaFile(
        FileName            = 'T1510   ._SN',
        MapName             = 'Bose',
        Location            = 'T1510.x',
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
        'Lenard',                               # 9
        'Sophina',                              # 10
        'Lloyd',                                # 11
        'Elke',                                 # 12
        'Anette',                               # 13
        'Sting',                                # 14
        'Anelace',                              # 15
        'Scherazard',                           # 16
        'Olivier',                              # 17
        'Dish',                                 # 18
        'Dish',                                 # 19
        'Dish',                                 # 20
        'Coffee',                               # 21
        'Coffee',                               # 22
        'Coffee',                               # 23
        'Coffee',                               # 24
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
        Unknown_30              = 225,
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
        'ED6_DT07/CH01270 ._CH',             # 00
        'ED6_DT07/CH01690 ._CH',             # 01
        'ED6_DT07/CH01020 ._CH',             # 02
        'ED6_DT07/CH01183 ._CH',             # 03
        'ED6_DT07/CH01213 ._CH',             # 04
        'ED6_DT07/CH01623 ._CH',             # 05
        'ED6_DT07/CH01630 ._CH',             # 06
        'ED6_DT07/CH00023 ._CH',             # 07
        'ED6_DT07/CH00033 ._CH',             # 08
        'ED6_DT06/CH20020 ._CH',             # 09
        'ED6_DT06/CH20021 ._CH',             # 0A
        'ED6_DT06/CH20049 ._CH',             # 0B
        'ED6_DT07/CH01180 ._CH',             # 0C
        'ED6_DT07/CH01210 ._CH',             # 0D
    )

    AddCharChipPat(
        'ED6_DT07/CH01270P._CP',             # 00
        'ED6_DT07/CH01690P._CP',             # 01
        'ED6_DT07/CH01020P._CP',             # 02
        'ED6_DT07/CH01183P._CP',             # 03
        'ED6_DT07/CH01213P._CP',             # 04
        'ED6_DT07/CH01623P._CP',             # 05
        'ED6_DT07/CH01630P._CP',             # 06
        'ED6_DT07/CH00023P._CP',             # 07
        'ED6_DT07/CH00033P._CP',             # 08
        'ED6_DT06/CH20020P._CP',             # 09
        'ED6_DT06/CH20021P._CP',             # 0A
        'ED6_DT06/CH20049P._CP',             # 0B
        'ED6_DT07/CH01180P._CP',             # 0C
        'ED6_DT07/CH01210P._CP',             # 0D
    )

    DeclNpc(
        X                   = 26500,
        Z                   = 0,
        Y                   = 12600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 24500,
        Z                   = 0,
        Y                   = 6100,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 13000,
        Z                   = 0,
        Y                   = 7500,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 13700,
        Z                   = 150,
        Y                   = 6400,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x155,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 15930,
        Z                   = 250,
        Y                   = 6290,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x155,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 23980,
        Z                   = 300,
        Y                   = 9640,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 17080,
        Z                   = 0,
        Y                   = 13470,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 16100,
        Z                   = 200,
        Y                   = 6240,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 13450,
        Z                   = 200,
        Y                   = 6320,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 15250,
        Z                   = 700,
        Y                   = 6400,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 327690,
        ChipIndex           = 0xA,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 14160,
        Z                   = 700,
        Y                   = 6050,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 327690,
        ChipIndex           = 0xA,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 14790,
        Z                   = 800,
        Y                   = 6500,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1835017,
        ChipIndex           = 0x9,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 14450,
        Z                   = 800,
        Y                   = 6650,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1835017,
        ChipIndex           = 0x9,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 15000,
        Z                   = 0,
        Y                   = 5500,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1835017,
        ChipIndex           = 0x9,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 14600,
        Z                   = 0,
        Y                   = 5500,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1835017,
        ChipIndex           = 0x9,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 14200,
        Z                   = 0,
        Y                   = 5500,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1835017,
        ChipIndex           = 0x9,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 23100,
        TriggerZ            = 0,
        TriggerY            = 6000,
        TriggerRange        = 700,
        ActorX              = 24500,
        ActorZ              = 1500,
        ActorY              = 6100,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 80610,
        TriggerZ            = 0,
        TriggerY            = 9100,
        TriggerRange        = 1400,
        ActorX              = 80610,
        ActorZ              = 1500,
        ActorY              = 9100,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 20,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_362",          # 00, 0
        "Function_1_58D",          # 01, 1
        "Function_2_5AF",          # 02, 2
        "Function_3_5C5",          # 03, 3
        "Function_4_5C6",          # 04, 4
        "Function_5_5EA",          # 05, 5
        "Function_6_12A9",         # 06, 6
        "Function_7_12AE",         # 07, 7
        "Function_8_251D",         # 08, 8
        "Function_9_25B6",         # 09, 9
        "Function_10_2B81",        # 0A, 10
        "Function_11_3053",        # 0B, 11
        "Function_12_3632",        # 0C, 12
        "Function_13_39EC",        # 0D, 13
        "Function_14_449A",        # 0E, 14
        "Function_15_4F97",        # 0F, 15
        "Function_16_67A8",        # 10, 16
        "Function_17_6832",        # 11, 17
        "Function_18_6F68",        # 12, 18
        "Function_19_6FC2",        # 13, 19
        "Function_20_7017",        # 14, 20
    )


    def Function_0_362(): pass

    label("Function_0_362")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_380")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8)
    Jump("loc_4B4")

    label("loc_380")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 6)), scpexpr(EXPR_END)), "loc_38A")
    Jump("loc_4B4")

    label("loc_38A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 5)), scpexpr(EXPR_END)), "loc_3E2")
    SetChrChipByIndex(0xB, 12)
    SetChrChipByIndex(0xC, 13)
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0xB, 0x40)
    ClearChrFlags(0xC, 0x40)
    SetChrPos(0xB, 54800, 0, 3410, 180)
    SetChrPos(0xC, 51130, 0, 5960, 270)
    OP_43(0xB, 0x0, 0x0, 0x2)
    OP_43(0xC, 0x0, 0x0, 0x4)
    Jump("loc_4B4")

    label("loc_3E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 6)), scpexpr(EXPR_END)), "loc_43A")
    SetChrChipByIndex(0xB, 12)
    SetChrChipByIndex(0xC, 13)
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0xB, 0x40)
    ClearChrFlags(0xC, 0x40)
    SetChrPos(0xB, 54800, 0, 3410, 180)
    SetChrPos(0xC, 51130, 0, 5960, 270)
    OP_43(0xB, 0x0, 0x0, 0x2)
    OP_43(0xC, 0x0, 0x0, 0x4)
    Jump("loc_4B4")

    label("loc_43A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 5)), scpexpr(EXPR_END)), "loc_444")
    Jump("loc_4B4")

    label("loc_444")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_44E")
    Jump("loc_4B4")

    label("loc_44E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_46C")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x10)
    Jump("loc_4B4")

    label("loc_46C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_476")
    Jump("loc_4B4")

    label("loc_476")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_494")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8)
    Jump("loc_4B4")

    label("loc_494")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_4B4")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8)
    ClearChrFlags(0xE, 0x80)

    label("loc_4B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_567")
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 4)), scpexpr(EXPR_END)), "loc_517")
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x10, 13450, 200, 6240, 0)
    SetChrFlags(0x10, 0x2)
    SetChrChipByIndex(0x10, 11)
    SetChrSubChip(0x12, 1)
    Jump("loc_567")

    label("loc_517")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 2)), scpexpr(EXPR_END)), "loc_535")
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    Jump("loc_567")

    label("loc_535")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 5)), scpexpr(EXPR_END)), "loc_558")
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrSubChip(0x12, 1)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    Jump("loc_567")

    label("loc_558")

    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)

    label("loc_567")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_575")
    OP_A3(0x3FA)
    Event(0, 15)

    label("loc_575")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_58C")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x46), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3FB)
    Event(0, 16)

    label("loc_58C")

    Return()

    # Function_0_362 end

    def Function_1_58D(): pass

    label("Function_1_58D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5A5")
    OP_B1("t1510_y")
    Jump("loc_5AE")

    label("loc_5A5")

    OP_B1("t1510_n")

    label("loc_5AE")

    Return()

    # Function_1_58D end

    def Function_2_5AF(): pass

    label("Function_2_5AF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5C4")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_5AF")

    label("loc_5C4")

    Return()

    # Function_2_5AF end

    def Function_3_5C5(): pass

    label("Function_3_5C5")

    Return()

    # Function_3_5C5 end

    def Function_4_5C6(): pass

    label("Function_4_5C6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5E9")
    OP_8D(0xFE, 50200, 5000, 54800, 6300, 2000)
    Jump("Function_4_5C6")

    label("loc_5E9")

    Return()

    # Function_4_5C6 end

    def Function_5_5EA(): pass

    label("Function_5_5EA")

    TalkBegin(0x8)
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_64A")
    FadeToBright(300, 0)
    OP_0D()
    OP_A9(0x15)
    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_64A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_664")
    FadeToBright(300, 0)
    TalkEnd(0x8)
    Return()

    label("loc_664")

    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_6D4")

    ChrTalk(
        0x8,
        "Oh, welcome, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You came here to fish again?\x01",
            "Well, make yourselves at home.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12A5")

    label("loc_6D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 4)), scpexpr(EXPR_END)), "loc_764")

    ChrTalk(
        0x8,
        (
            "The two of them certainly\x01",
            "drank a lot...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm going to have to put in another\x01",
            "order to Ravennue Village for some\x01",
            "fruit wine.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12A5")

    label("loc_764")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 5)), scpexpr(EXPR_END)), "loc_7EA")

    ChrTalk(
        0x8,
        "So how did your fishing go?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you happen to catch anything\x01",
            "good, I'll cook it up for you as\x01",
            "part of the service.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12A5")

    label("loc_7EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 6)), scpexpr(EXPR_END)), "loc_84D")

    ChrTalk(
        0x8,
        "Hmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I've got some good fish in today,\x01",
            "so please look forward to your\x01",
            "meals.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12A5")

    label("loc_84D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 5)), scpexpr(EXPR_END)), "loc_8FF")

    ChrTalk(
        0x8,
        "Were you able to meet Lloyd?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you like what you see here\x01",
            "at the inn, then please stay\x01",
            "for the night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I just had a cancellation so\x01",
            "I have an open room.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12A5")

    label("loc_8FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_E5C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DCB")
    OP_A2(0x33C)
    OP_28(0x38, 0x1, 0x2)
    EventBegin(0x0)
    OP_69(0x8, 0x3E8)
    SetChrSubChip(0x8, 0)

    ChrTalk(
        0x8,
        (
            "Welcome to the Kingfisher Inn.\x01",
            "Are you all here to stay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501FLet's see, yes and no.\x01",
            "How should I put it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FWe're here looking for a certain\x01",
            "someone.\x02\x03",
            "Is there a guest staying here\x01",
            "who loves to fish?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, pretty much everybody\x01",
            "who stays here loves to fish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020FWe heard he was a friend of\x01",
            "the old man who stayed here\x01",
            "yesterday.\x02\x03",
            "Do you have a clue who that\x01",
            "might be?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Oh, are you talking about old\x01",
            "man Kuwano?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you're talking about his fishing\x01",
            "buddy, then I think you must mean\x01",
            "Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505FLloyd?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I've heard he's a professional angler\x01",
            "who came all the way here from the\x01",
            "Royal City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It seems as though he's a member\x01",
            "of the Fisherman's Guild there.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CCC")

    ChrTalk(
        0x101,
        (
            "#506FHe sounds like a pretty amazing\x01",
            "guy.\x02\x03",
            "#000FDo you know where we might\x01",
            "be able to find him?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ha ha. He's out dropping a line\x01",
            "somewhere, of course.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If I remember right, he should\x01",
            "be out on the back pier.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DC6")

    label("loc_CCC")


    ChrTalk(
        0x101,
        (
            "#506FHe sounds like a pretty amazing\x01",
            "guy.\x02\x03",
            "#000FSo you're saying he's that old man\x01",
            "fishing out back?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yeah, I'm pretty sure he's the\x01",
            "one you're talking about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You might be able to get his\x01",
            "attention if you call his name\x01",
            "out really loud.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DC6")

    EventEnd(0x1)
    Jump("loc_E59")

    label("loc_DCB")


    ChrTalk(
        0x8,
        (
            "If you're looking for Lloyd, he's\x01",
            "out dropping a line somewhere,\x01",
            "of course.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If I remember right, he should\x01",
            "be out on the back pier.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E59")

    Jump("loc_12A5")

    label("loc_E5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_FE3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F5E")
    OP_A2(0x2)

    ChrTalk(
        0x8,
        "That reminds me...,\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The Royal Army also came to\x01",
            "investigate about a missing\x01",
            "airliner here, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "But there's nothing here but\x01",
            "placid waters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "And nobody's seen any suspicious\x01",
            "individuals or an airliner for that\x01",
            "matter.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FE0")

    label("loc_F5E")


    ChrTalk(
        0x8,
        (
            "The Royal Army also came to\x01",
            "investigate about a missing\x01",
            "airliner here, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "But there's nothing here but\x01",
            "placid waters.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FE0")

    Jump("loc_12A5")

    label("loc_FE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_1140")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10B6")
    OP_A2(0x2)

    ChrTalk(
        0x8,
        "That reminds me...,\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "There's an old tower standing to\x01",
            "the northwest of here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It seems as though it's called\x01",
            "the Amberl Tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I wonder what in the world it was\x01",
            "built for.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_113D")

    label("loc_10B6")


    ChrTalk(
        0x8,
        (
            "There's an old tower called the\x01",
            "Amberl Tower standing to the\x01",
            "northwest of here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I wonder what in the world\x01",
            "it was built for.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_113D")

    Jump("loc_12A5")

    label("loc_1140")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_12A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_120D")
    OP_A2(0x2)

    ChrTalk(
        0x8,
        "Welcome to our lovely inn.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "My little sister and I run this place\x01",
            "here on the Valleria Lakeshore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you don't have any pressing\x01",
            "errands, why don't you stay\x01",
            "for a while?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12A5")

    label("loc_120D")


    ChrTalk(
        0x8,
        (
            "My little sister and I run this place\x01",
            "here on the Valleria Lakeshore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you don't have any pressing\x01",
            "errands, why don't you stay\x01",
            "for a while?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12A5")

    TalkEnd(0x8)
    Return()

    # Function_5_5EA end

    def Function_6_12A9(): pass

    label("Function_6_12A9")

    Call(0, 7)
    Return()

    # Function_6_12A9 end

    def Function_7_12AE(): pass

    label("Function_7_12AE")

    TalkBegin(0x9)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",       # 0
            "Rest\x01",       # 1
            "Leave\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_130E")
    OP_0D()
    OP_A9(0x14)
    OP_56(0x0)
    TalkEnd(0x9)
    Return()

    label("loc_130E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_131F")
    TalkEnd(0x9)
    Return()

    label("loc_131F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_1393")

    ChrTalk(
        0x9,
        (
            "The weather is absolutely\x01",
            "wonderful today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Hmm-hmm. It looks like the sheets\x01",
            "will dry well too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2519")

    label("loc_1393")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 4)), scpexpr(EXPR_END)), "loc_145A")
    OP_A2(0x1)

    ChrTalk(
        0x9,
        (
            "I don't know if you'll believe me, seeing as\x01",
            "I'm family, but my brother's dishes made\x01",
            "with fish are something to be reckoned with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Please look forward to a meal\x01",
            "like no other.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2519")

    label("loc_145A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 5)), scpexpr(EXPR_END)), "loc_1537")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14F7")
    OP_A2(0x1)

    ChrTalk(
        0x9,
        (
            "Our dishes use fish purchased\x01",
            "straight from the fishermen\x01",
            "themselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "So you can always look forward\x01",
            "to the freshest of fish.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1534")

    label("loc_14F7")


    ChrTalk(
        0x9,
        "The boy who came with you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "He hasn't come in here.\x02",
    )

    CloseMessageWindow()

    label("loc_1534")

    Jump("loc_2519")

    label("loc_1537")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 6)), scpexpr(EXPR_END)), "loc_19CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15D5")

    ChrTalk(
        0x9,
        "People come here to enjoy fishing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If you would like to borrow a fishing\x01",
            "pole, we can loan you one, so all\x01",
            "you need to do is ask.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19C8")

    label("loc_15D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_178D")
    EventBegin(0x0)
    OP_69(0x9, 0x3E8)
    OP_A2(0x344)

    ChrTalk(
        0x101,
        (
            "#000FUm...\x02\x03",
            "Do you have a fishing pole I could\x01",
            "borrow?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Yes, of course we do.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "They're right over here, and they're\x01",
            "free to use for anyone lodging here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001FWow, really? Score!\x02",
    )

    CloseMessageWindow()
    OP_3E(0x332, 1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Borrowed \x07\x02",
            "Progressive Rod\x07\x00",
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x101,
        (
            "#501FHmm, this is a pretty nice rod\x01",
            "to be loaning out to everyone.\x02\x03",
            "All right then, I'll put it to\x01",
            "good use.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Please enjoy yourself.\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Jump("loc_19C8")

    label("loc_178D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_190B")
    OP_A2(0x1)

    ChrTalk(
        0x101,
        (
            "#501FLet's see, are there any particular\x01",
            "fishing spots I should be aware of?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Well...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "There is a small island close by\x01",
            "where you can catch a lot of fish...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "But I'd say that around the pier\x01",
            "is the most highly recommended\x01",
            "spot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The lake bed has quite a few hidey-spots\x01",
            "there for the fish, so there are a lot of\x01",
            "them swimming around in that area.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19C8")

    label("loc_190B")


    ChrTalk(
        0x9,
        (
            "I'd say around the pier is the most\x01",
            "highly recommended spot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The lake bed has quite a few hidey-spots\x01",
            "there for the fish, so there are a lot of\x01",
            "them swimming around in that area.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19C8")

    Jump("loc_2519")

    label("loc_19CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 5)), scpexpr(EXPR_END)), "loc_208B")
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 22480, 0, 5710, 90)
    SetChrPos(0x102, 22370, 0, 6610, 90)
    SetChrPos(0x103, 21380, 0, 5470, 90)
    SetChrPos(0x104, 22060, 0, 4510, 45)
    TurnDirection(0x9, 0x101, 0)
    OP_69(0x9, 0x0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B6C")
    OP_A2(0x1)

    ChrTalk(
        0x9,
        (
            "Will you be staying here with us\x01",
            "tonight?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501FYeah, that's the plan...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010FHold on, Estelle.\x02\x03",
            "If there's anything that we haven't\x01",
            "taken care of we'd better do it now.\x02\x03",
            "I don't want to head back to Bose\x01",
            "after we've gotten a room.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#000F#2PUm, I guess you're right.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 400)
    Jump("loc_1B94")

    label("loc_1B6C")


    ChrTalk(
        0x9,
        "Would you like to get a room here?\x02",
    )

    CloseMessageWindow()

    label("loc_1B94")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[Not just yet]\x01",      # 0
            "[Get a room]\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1C01"),
        (1, "loc_1C7D"),
        (SWITCH_DEFAULT, "loc_2088"),
    )


    label("loc_1C01")


    ChrTalk(
        0x9,
        "I understand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'll reserve your room, so please\x01",
            "come back after you've finished\x01",
            "with your other errands.\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    OP_4B(0x9, 255)
    Jump("loc_2088")

    label("loc_1C7D")


    ChrTalk(
        0x9,
        "All right then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Please come with me.\x01",
            "I'll show you to your room.\x02",
        )
    )

    CloseMessageWindow()
    ClearMapFlags(0x1)
    OP_A2(0x33E)
    OP_28(0x38, 0x1, 0x40)
    OP_28(0x16, 0x4, 0x40)
    OP_28(0x18, 0x4, 0x40)
    FadeToDark(1500, 0, -1)
    OP_0D()
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrPos(0x9, 104400, 0, 13140, 180)
    SetChrPos(0x101, 106160, 0, 11480, 180)
    SetChrPos(0x102, 105150, 0, 10900, 180)
    SetChrPos(0x104, 104580, 0, 11870, 180)
    SetChrPos(0x103, 105850, 0, 12550, 180)
    OP_6D(107290, 0, 4690, 0)
    OP_6B(2800, 0)
    Sleep(1000)
    FadeToBright(1500, 0)
    OP_6D(107690, 0, 12420, 3000)
    OP_0D()

    ChrTalk(
        0x9,
        "This is where you will be staying.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I will leave you here, so please\x01",
            "relax until dinner is served.\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x9, 0x4)
    OP_8C(0x9, 225, 300)
    OP_8E(0x9, 0x19604, 0x0, 0x3282, 0x7D0, 0x0)

    def lambda_1E16():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1E16)
    OP_8E(0x9, 0x18F7E, 0x0, 0x3282, 0x7D0, 0x0)
    SetChrFlags(0x9, 0x80)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010FThis is quite a nice room. It has\x01",
            "a certain atmosphere that you just\x01",
            "don't find back in the city.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#006F#2PYeah, it's great, huh?\x02\x03",
            "It wasn't that expensive either.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x103, 225, 400)

    ChrTalk(
        0x103,
        (
            "#020F#1PHmm-hmm-hmm.\x01",
            "What to do now...?\x02\x03",
            "How about we relax until it gets\x01",
            "dark?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x104, 90, 400)

    ChrTalk(
        0x104,
        "#031FWhat a nice idea.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(
        0x101,
        (
            "#004F#2PI'd be more than happy to do just\x01",
            "that, but is it really okay to take\x01",
            "it easy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#021F#1PRest when you can. That's\x01",
            "part of a bracer's job too.\x02\x03",
            "This is our free time, so let's\x01",
            "enjoy a meal, take a stroll,\x01",
            "or something else.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T1500   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2088")

    Jump("loc_2519")

    label("loc_208B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_20EC")

    ChrTalk(
        0x9,
        "Welcome to the Kingfisher Inn.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Please let me know if you would\x01",
            "like to stay.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2519")

    label("loc_20EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_21AD")

    ChrTalk(
        0x9,
        (
            "It seems the Royal Army was investigating\x01",
            "around the Amberl Tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I also heard some suspicious individual\x01",
            "was found at the tower, but he turned\x01",
            "out to be an archaeologist.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2519")

    label("loc_21AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_22F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_226E")
    OP_A2(0x1)

    ChrTalk(
        0x9,
        (
            "My older brother Lenard started\x01",
            "this inn.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I grew fond of the atmosphere\x01",
            "here when I came to visit him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "And so I decided to stay, and\x01",
            "he let me work for him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22F2")

    label("loc_226E")


    ChrTalk(
        0x9,
        (
            "I grew fond of the atmosphere here\x01",
            "when I came to visit my brother.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "And so I decided to stay, and\x01",
            "he let me work for him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22F2")

    Jump("loc_2519")

    label("loc_22F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_2519")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2451")
    OP_A2(0x1)

    ChrTalk(
        0x9,
        (
            "Welcome to the Kingfisher Inn.\x01",
            "Are you all here to stay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501FLet's see, not exactly...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Well, that's too bad...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The scenery of this place is beautiful,\x01",
            "and a refreshing breeze blows\x01",
            "through here all day long.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I guarantee that you'll find it\x01",
            "relaxing here. Please visit us\x01",
            "again when you have a chance.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2519")

    label("loc_2451")


    ChrTalk(
        0x9,
        (
            "The scenery of this place is beautiful,\x01",
            "and a refreshing breeze blows\x01",
            "through here all day long.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I guarantee that you'll find it\x01",
            "relaxing here. Please visit us\x01",
            "again when you have a chance.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2519")

    TalkEnd(0x9)
    Return()

    # Function_7_12AE end

    def Function_8_251D(): pass

    label("Function_8_251D")

    TalkBegin(0xA)

    ChrTalk(
        0xFE,
        (
            "The master has already gotten\x01",
            "away from me once today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I guess I'll try searching for\x01",
            "another prime fishing spot\x01",
            "and try my luck again.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xA)
    Return()

    # Function_8_251D end

    def Function_9_25B6(): pass

    label("Function_9_25B6")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 4)), scpexpr(EXPR_END)), "loc_261F")

    ChrTalk(
        0xFE,
        (
            "During the evening, the entire\x01",
            "surrounding area is bathed in\x01",
            "a beautiful orange color.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B7D")

    label("loc_261F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 5)), scpexpr(EXPR_END)), "loc_27C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2718")
    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "I was able to spend another\x01",
            "day relaxing here today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's important to get away from\x01",
            "your daily routine when you're\x01",
            "worn out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When I return home, reality is\x01",
            "waiting for me, so I'd better\x01",
            "enjoy myself while I can.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27C2")

    label("loc_2718")


    ChrTalk(
        0xFE,
        (
            "It's important to get away from\x01",
            "your daily routine when you're\x01",
            "worn out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When I return home, reality is\x01",
            "waiting for me, so I'd better\x01",
            "enjoy myself while I can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27C2")

    Jump("loc_2B7D")

    label("loc_27C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 6)), scpexpr(EXPR_END)), "loc_2822")

    ChrTalk(
        0xFE,
        "Oh, are you staying here too?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Let's enjoy this wonderful place\x01",
            "together.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B7D")

    label("loc_2822")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 5)), scpexpr(EXPR_END)), "loc_29C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2925")
    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "I wonder if I should bring my\x01",
            "husband here next year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He always stays at home to watch\x01",
            "the house while I'm gone, so I feel\x01",
            "kind of sorry for him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But my daughter and I bonding,\x01",
            "just the two of us, isn't a bad\x01",
            "thing either.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29C3")

    label("loc_2925")


    ChrTalk(
        0xFE,
        (
            "I wonder if I should bring my\x01",
            "husband here next year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He always stays at home to watch\x01",
            "the house while we're gone, so I feel\x01",
            "kind of sorry for him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29C3")

    Jump("loc_2B7D")

    label("loc_29C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_2A30")

    ChrTalk(
        0xFE,
        (
            "The Kingfisher Inn in Bose and\x01",
            "the Maple Leaf Inn in Zeiss are\x01",
            "my favorite places to stay.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B7D")

    label("loc_2A30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_2AC5")

    ChrTalk(
        0xFE,
        (
            "Although I like traveling around\x01",
            "and seeing the sights, too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I love being able to take a vacation\x01",
            "like this where I can relax.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B7D")

    label("loc_2AC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_2B76")

    ChrTalk(
        0xFE,
        "The weather is just wonderful today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe I'll just take a book and\x01",
            "read by the water's edge this\x01",
            "afternoon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Or maybe I could give fishing\x01",
            "a try, too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B7D")

    label("loc_2B76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_2B7D")

    label("loc_2B7D")

    TalkEnd(0xB)
    Return()

    # Function_9_25B6 end

    def Function_10_2B81(): pass

    label("Function_10_2B81")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 4)), scpexpr(EXPR_END)), "loc_2C0F")

    ChrTalk(
        0xFE,
        (
            "It's almost meal time. I wonder\x01",
            "what's on the menu today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The food here is the one thing\x01",
            "I can always look forward to.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_304F")

    label("loc_2C0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 5)), scpexpr(EXPR_END)), "loc_2CF0")

    ChrTalk(
        0xFE,
        (
            "There are a lot of people who\x01",
            "come to this inn to fish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just a little while ago, an old man\x01",
            "came here from Bose and spent\x01",
            "all day fishing before going home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm thinking about giving it\x01",
            "a try myself.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_304F")

    label("loc_2CF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 6)), scpexpr(EXPR_END)), "loc_2D48")

    ChrTalk(
        0xFE,
        "I wonder what's for dinner today?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm so excited I can hardly wait.\x02",
    )

    CloseMessageWindow()
    Jump("loc_304F")

    label("loc_2D48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 5)), scpexpr(EXPR_END)), "loc_2E3C")

    ChrTalk(
        0xFE,
        (
            "That Lloyd fellow who came from\x01",
            "the Royal City is an odd apple.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems that if you try to talk to him\x01",
            "while he's fishing, he completely tunes\x01",
            "you out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He's a rather friendly gent if you\x01",
            "meet him during dinner though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_304F")

    label("loc_2E3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_2FB4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F44")
    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "My mother and I come here every\x01",
            "year on vacation around this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It's a tradition in our family.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My mother seems to look forward\x01",
            "to it, every time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I kind of feel bad for my father,\x01",
            "though, as he always gets left\x01",
            "behind.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FB1")

    label("loc_2F44")


    ChrTalk(
        0xFE,
        (
            "My mother and I come here every\x01",
            "year on vacation around this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It's a tradition in our family.\x02",
    )

    CloseMessageWindow()

    label("loc_2FB1")

    Jump("loc_304F")

    label("loc_2FB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_304F")

    ChrTalk(
        0xFE,
        (
            "And the food is great.\x01",
            "This place is relaxing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And I couldn't ask for anything\x01",
            "more, but I have to be careful\x01",
            "not to put on any weight.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_304F")

    TalkEnd(0xC)
    Return()

    # Function_10_2B81 end

    def Function_11_3053(): pass

    label("Function_11_3053")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33DD")
    OP_A2(0x35F)
    OP_A2(0x5)

    ChrTalk(
        0x101,
        "#006F(Huh, who's this guy...?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F(Um, he looks like a bracer if\x01",
            "you ask me.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000FUm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002FHello? Is anybody there?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#023FHoney water with soda...\x02\x03",
            "#020FIt's been a while, hasn't it,\x01",
            "Sting?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "Weren't you...that bracer in training\x01",
            "from some time ago?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020FYou got it.\x02\x03",
            "And thanks to you I can call\x01",
            "myself a senior bracer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm...I almost didn't recognize you.\x01",
            "Do you have some work here at the\x01",
            "Bose branch?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#020FAt the moment, yeah.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Right now we are dealing with a\x01",
            "number of incidents, so we're a\x01",
            "little shorthanded...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Any help you could give us would\x01",
            "be useful.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFE, 0, 0)

    ChrTalk(
        0x101,
        (
            "#002F(So he was one of Schera's acquaintances,\x01",
            "huh? He does seem like a bit of a scary\x01",
            "guy if you ask me.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F(That may be so, but with the way he\x01",
            "carries himself...he looks pretty\x01",
            "capable as a bracer.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_362E")

    label("loc_33DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35F6")
    OP_A2(0x5)

    ChrTalk(
        0x101,
        "#000FIt was...um...Sting, wasn't it?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FWas there some kind of incident\x01",
            "here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No, just a monster extermination.\x01",
            "No big incident or anything like\x01",
            "that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "But never mind that...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard from Lugran that you're\x01",
            "Cassius' kids. Is that true?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000FY-Yeah, that's right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FWhy? Do you know our father?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yeah, in a sense...and he's helped\x01",
            "me out a number of times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505FHmm...\x02\x03",
            "So, Dad is well known in Bose\x01",
            "too, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FYeah, it sure looks that way.\x02",
    )

    CloseMessageWindow()
    OP_8C(0xFE, 0, 0)
    Jump("loc_362E")

    label("loc_35F6")

    TurnDirection(0xFE, 0x0, 0)

    ChrTalk(
        0xFE,
        (
            "I hope that you can find him\x01",
            "soon...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFE, 0, 0)

    label("loc_362E")

    TalkEnd(0xD)
    Return()

    # Function_11_3053 end

    def Function_12_3632(): pass

    label("Function_12_3632")

    TalkBegin(0xE)
    TurnDirection(0xFE, 0x103, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3967")
    OP_A2(0x360)

    ChrTalk(
        0xFE,
        (
            "#814FIsn't that you, Scherazard?\x02\x03",
            "#850FIt's nice to see you again. I haven't\x01",
            "seen you since the last time you\x01",
            "were here during your training.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020FIf it isn't Anelace. What\x01",
            "are you doing here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#810FWell, we had a request to\x01",
            "exterminate a monster in\x01",
            "this area.\x02\x03",
            "And that's just what we did!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020FOh really...?\x02\x03",
            "So how has your swordsmanship been\x01",
            "coming along? Have you started\x01",
            "mastering the use of that weapon?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "#819FPlease don't even ask.\x01",
            "I'm still working on that.\x02\x03",
            "#810FBy the way, Scherazard, are you\x01",
            "here on a job with the guild?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020FYeah, something like that. Although\x01",
            "the job's a little different from the one\x01",
            "you're handling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#810FIs that so...\x02\x03",
            "This region has been plagued with\x01",
            "a number of incidents.\x02\x03",
            "Please be careful yourself.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39E8")

    label("loc_3967")


    ChrTalk(
        0xFE,
        (
            "#810FOne more thing, Scherazard, the\x01",
            "region has been plagued with a\x01",
            "number of incidents recently.\x02\x03",
            "Make sure to be careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39E8")

    TalkEnd(0xE)
    Return()

    # Function_12_3632 end

    def Function_13_39EC(): pass

    label("Function_13_39EC")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3A05")
    TalkEnd(0x10)
    Call(0, 17)
    Jump("loc_4496")

    label("loc_3A05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 5)), scpexpr(EXPR_END)), "loc_3FDA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D8C")
    EventBegin(0x0)
    OP_A2(0x34A)
    OP_6D(14850, 0, 6330, 1000)

    ChrTalk(
        0xF,
        (
            "#028FHmm, so you can hold your\x01",
            "liquor, can't you?\x02\x03",
            "Hmm-hmm-hmm... I think I've changed\x01",
            "my mind about you.\x02\x03",
            "Come on now, drink up!\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0xF9, 0x0, 0x64)
    Fade(1000)
    SetChrSubChip(0x12, 5)
    OP_0D()
    OP_62(0x10, 0x0, 1700, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x10,
        (
            "#037FH-Hold on, Schera! Don't you think\x01",
            "we're getting a little ahead of\x01",
            "ourselves with this pace?\x02\x03",
            "It could interfere with tonight's...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#029FWhat are you whining about\x01",
            "now...?\x02",
        )
    )

    CloseMessageWindow()
    OP_7C(0x0, 0xC8, 0x7D0, 0xC8)

    ChrTalk(
        0xF,
        (
            "#029FCome on and drink, you third-rate\x01",
            "musician! Or are you saying that\x01",
            "you can't keep up with me?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#038FYikes...!\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x10, 0x10)
    TurnDirection(0x10, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3C47")
    SetChrSubChip(0x10, 1)
    Jump("loc_3C78")

    label("loc_3C47")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3C5D")
    SetChrSubChip(0x10, 0)
    Jump("loc_3C78")

    label("loc_3C5D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x10E), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3C73")
    SetChrSubChip(0x10, 2)
    Jump("loc_3C78")

    label("loc_3C73")

    SetChrSubChip(0x10, 1)

    label("loc_3C78")

    OP_8C(0x10, 90, 0)
    SetChrFlags(0x10, 0x10)
    Sleep(500)

    ChrTalk(
        0x10,
        (
            "#038FEstelle...don't just sit there\x01",
            "and watch! Do something!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007FSorry, bud. Once she gets started\x01",
            "there's no stopping her.\x02\x03",
            "#006FBut you don't have to worry,\x01",
            "Schera never gets plastered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#037FUm...shouldn't you be worried\x01",
            "about me?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 0)
    EventEnd(0x0)
    Jump("loc_3FD7")

    label("loc_3D8C")

    ClearChrFlags(0x10, 0x10)
    TurnDirection(0x10, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3DAE")
    SetChrSubChip(0x10, 1)
    Jump("loc_3DC9")

    label("loc_3DAE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x10E), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3DC4")
    SetChrSubChip(0x10, 1)
    Jump("loc_3DC9")

    label("loc_3DC4")

    SetChrSubChip(0x10, 2)

    label("loc_3DC9")

    OP_8C(0x10, 90, 0)
    SetChrFlags(0x10, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F43")
    OP_A2(0x7)

    ChrTalk(
        0x10,
        "#037FI-Is she always like this?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007FWhenever she's on the job, she\x01",
            "manages to behave herself.\x02\x03",
            "But when it comes to having a\x01",
            "drink, even my dad can't keep\x01",
            "up with her.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 1700, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x10,
        (
            "#037FI-Is that the case...?\x02\x03",
            "At any rate, I'm kind of interested in\x01",
            "seeing her go wild, or am I going to\x01",
            "pass out from the drinks first...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FD2")

    label("loc_3F43")


    ChrTalk(
        0x10,
        (
            "#037FSo, am I going to get to see Schera\x01",
            "go wild or am I going to pass out\x01",
            "from the drinks first...?\x02\x03",
            "Hmm, that's one big question there.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FD2")

    SetChrSubChip(0x10, 0)

    label("loc_3FD7")

    Jump("loc_4496")

    label("loc_3FDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42E2")
    EventBegin(0x0)
    OP_A2(0x343)
    OP_6D(14850, 0, 6330, 1000)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Scherazard and Olivier are having a\x01",
            "drink of chilled fruit wine together.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    TurnDirection(0x101, 0xF, 400)

    ChrTalk(
        0x101,
        (
            "#000FSchera...should you start drinking\x01",
            "again when it's only noon?\x02\x03",
            "No matter how light the liquor is,\x01",
            "drinking too much is bad for your\x01",
            "health, right?\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xF, 0x10)
    TurnDirection(0xF, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_412D")
    SetChrSubChip(0xF, 2)
    Jump("loc_415E")

    label("loc_412D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4143")
    SetChrSubChip(0xF, 1)
    Jump("loc_415E")

    label("loc_4143")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4159")
    SetChrSubChip(0xF, 0)
    Jump("loc_415E")

    label("loc_4159")

    SetChrSubChip(0xF, 2)

    label("loc_415E")

    OP_8C(0xF, 270, 0)
    SetChrFlags(0xF, 0x10)

    ChrTalk(
        0xF,
        (
            "#021FDon't worry, this stuff is just\x01",
            "like water.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x10, 0x10)
    TurnDirection(0x10, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_41C2")
    SetChrSubChip(0x10, 1)
    Jump("loc_41F3")

    label("loc_41C2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_41D8")
    SetChrSubChip(0x10, 0)
    Jump("loc_41F3")

    label("loc_41D8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x10E), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_41EE")
    SetChrSubChip(0x10, 2)
    Jump("loc_41F3")

    label("loc_41EE")

    SetChrSubChip(0x10, 1)

    label("loc_41F3")

    OP_8C(0x10, 90, 0)
    SetChrFlags(0x10, 0x10)

    ChrTalk(
        0x10,
        (
            "#035FEstelle, sometimes we all need\x01",
            "to take a breather.\x02\x03",
            "I understand your concern for\x01",
            "Schera, but you can leave her\x01",
            "to me.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x10, 400)

    ChrTalk(
        0x101,
        (
            "#007FActually, Schera's not the one I'm\x01",
            "concerned about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#033F???\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 0)
    SetChrSubChip(0xF, 0)
    EventEnd(0x0)
    Jump("loc_4496")

    label("loc_42E2")

    ClearChrFlags(0x10, 0x10)
    TurnDirection(0x10, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4304")
    SetChrSubChip(0x10, 1)
    Jump("loc_431F")

    label("loc_4304")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x10E), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_431A")
    SetChrSubChip(0x10, 1)
    Jump("loc_431F")

    label("loc_431A")

    SetChrSubChip(0x10, 2)

    label("loc_431F")

    OP_8C(0x10, 90, 0)
    SetChrFlags(0x10, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4400")
    OP_A2(0x7)

    ChrTalk(
        0x10,
        (
            "#035FI invited Schera for a friendly\x01",
            "drink, and she readily agreed.\x02\x03",
            "It seems as though she's finally\x01",
            "been taken in by my charm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F(That brash self-confidence may\x01",
            "cost you your life...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4491")

    label("loc_4400")


    ChrTalk(
        0x10,
        (
            "#031FHeh heh heh...\x02\x03",
            "And after she gets wasted I'll be\x01",
            "the one to take good care of her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F(It's scary how much he doesn't\x01",
            "know...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4491")

    SetChrSubChip(0x10, 0)

    label("loc_4496")

    TalkEnd(0x10)
    Return()

    # Function_13_39EC end

    def Function_14_449A(): pass

    label("Function_14_449A")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_44B3")
    TalkEnd(0xF)
    Call(0, 17)
    Jump("loc_4F93")

    label("loc_44B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 5)), scpexpr(EXPR_END)), "loc_49FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4841")
    EventBegin(0x0)
    OP_A2(0x34A)
    OP_6D(14850, 0, 6330, 1000)

    ChrTalk(
        0xF,
        (
            "#028FHmm, so you can hold your\x01",
            "liquor, can't you?\x02\x03",
            "Hmm-hmm-hmm... I think I've changed\x01",
            "my mind about you.\x02\x03",
            "Come on now, drink up!\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0xF9, 0x0, 0x64)
    Fade(1000)
    SetChrSubChip(0x12, 5)
    OP_0D()
    OP_62(0x10, 0x0, 1700, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x10,
        (
            "#037FH-Hold on, Schera! Don't you think\x01",
            "we're getting a little ahead of\x01",
            "ourselves with this pace?\x02\x03",
            "It could interfere with tonight's...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#029FWhat are you whining about\x01",
            "now...?\x02",
        )
    )

    CloseMessageWindow()
    OP_7C(0x0, 0xC8, 0x7D0, 0xC8)

    ChrTalk(
        0xF,
        (
            "#029FCome on and drink, you third-rate\x01",
            "musician! Or are you saying that\x01",
            "you can't keep up with me?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#038FYikes...!\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x10, 0x10)
    TurnDirection(0x10, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_46F5")
    SetChrSubChip(0x10, 1)
    Jump("loc_4726")

    label("loc_46F5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_470B")
    SetChrSubChip(0x10, 0)
    Jump("loc_4726")

    label("loc_470B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x10E), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4721")
    SetChrSubChip(0x10, 2)
    Jump("loc_4726")

    label("loc_4721")

    SetChrSubChip(0x10, 1)

    label("loc_4726")

    OP_8C(0x10, 90, 0)
    SetChrFlags(0x10, 0x10)
    Sleep(500)

    ChrTalk(
        0x10,
        (
            "#038FEstelle...don't just sit there\x01",
            "and watch! Do something!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x10, 400)

    ChrTalk(
        0x101,
        (
            "#007FSorry, bud. Once she gets started\x01",
            "there's no stopping her.\x02\x03",
            "#006FBut you don't have to worry,\x01",
            "Schera never gets plastered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#037FUm...shouldn't you be worried\x01",
            "about me?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 0)
    EventEnd(0x0)
    Jump("loc_49F8")

    label("loc_4841")

    ClearChrFlags(0xF, 0x10)
    TurnDirection(0xF, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4863")
    SetChrSubChip(0xF, 2)
    Jump("loc_487E")

    label("loc_4863")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x10E), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4879")
    SetChrSubChip(0xF, 2)
    Jump("loc_487E")

    label("loc_4879")

    SetChrSubChip(0xF, 1)

    label("loc_487E")

    OP_8C(0xF, 270, 0)
    SetChrFlags(0xF, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4955")
    OP_A2(0x6)

    ChrTalk(
        0xF,
        (
            "#028FThings are starting to heat\x01",
            "up in here!\x02\x03",
            "Maybe I should just strip\x01",
            "down naked.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#004FIf you take off anything else we're\x01",
            "really going to be in trouble.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49F3")

    label("loc_4955")

    OP_62(0xF, 0x0, 1700, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xF,
        (
            "#028FEstelle, you know you're so cute\x01",
            "when you talk like that.\x02\x03",
            "How about giving me a kiss?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002FI'll do no such thing!\x02",
    )

    CloseMessageWindow()

    label("loc_49F3")

    SetChrSubChip(0xF, 0)

    label("loc_49F8")

    Jump("loc_4F93")

    label("loc_49FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CFC")
    EventBegin(0x0)
    OP_A2(0x343)
    OP_6D(14850, 0, 6330, 1000)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Scherazard and Olivier are having a\x01",
            "drink of chilled fruit wine together.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x101,
        (
            "#000FSchera...should you start drinking\x01",
            "again when it's only noon?\x02\x03",
            "No matter how light the liquor is,\x01",
            "drinking too much is bad for your\x01",
            "health, right?\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xF, 0x10)
    TurnDirection(0xF, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4B47")
    SetChrSubChip(0xF, 2)
    Jump("loc_4B78")

    label("loc_4B47")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4B5D")
    SetChrSubChip(0xF, 1)
    Jump("loc_4B78")

    label("loc_4B5D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4B73")
    SetChrSubChip(0xF, 0)
    Jump("loc_4B78")

    label("loc_4B73")

    SetChrSubChip(0xF, 2)

    label("loc_4B78")

    OP_8C(0xF, 270, 0)
    SetChrFlags(0xF, 0x10)

    ChrTalk(
        0xF,
        (
            "#021FDon't worry, this stuff is just\x01",
            "like water.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x10, 0x10)
    TurnDirection(0x10, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4BDC")
    SetChrSubChip(0x10, 1)
    Jump("loc_4C0D")

    label("loc_4BDC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4BF2")
    SetChrSubChip(0x10, 0)
    Jump("loc_4C0D")

    label("loc_4BF2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x10E), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4C08")
    SetChrSubChip(0x10, 2)
    Jump("loc_4C0D")

    label("loc_4C08")

    SetChrSubChip(0x10, 1)

    label("loc_4C0D")

    OP_8C(0x10, 90, 0)
    SetChrFlags(0x10, 0x10)

    ChrTalk(
        0x10,
        (
            "#035FEstelle, sometimes we all need\x01",
            "to take a breather.\x02\x03",
            "I understand your concern for\x01",
            "Schera, but you can leave her\x01",
            "to me.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x10, 400)

    ChrTalk(
        0x101,
        (
            "#007FActually, Schera's not the one I'm\x01",
            "concerned about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#033F???\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xF, 0)
    SetChrSubChip(0x10, 0)
    EventEnd(0x0)
    Jump("loc_4F93")

    label("loc_4CFC")

    ClearChrFlags(0xF, 0x10)
    TurnDirection(0xF, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4D1E")
    SetChrSubChip(0xF, 2)
    Jump("loc_4D39")

    label("loc_4D1E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x10E), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4D34")
    SetChrSubChip(0xF, 2)
    Jump("loc_4D39")

    label("loc_4D34")

    SetChrSubChip(0xF, 1)

    label("loc_4D39")

    OP_8C(0xF, 270, 0)
    SetChrFlags(0xF, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4EBD")
    OP_A2(0x6)

    ChrTalk(
        0xF,
        (
            "#020FBy the way Estelle, what\x01",
            "happened to Joshua?\x02\x03",
            "Did he dump you or something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007FYeah, actually he did.\x02",
    )

    CloseMessageWindow()
    OP_62(0xF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xF,
        "#023FReally?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009FI invited him to come fishing\x01",
            "with me, but he brushed me\x01",
            "off for a book.\x02\x03",
            "Don't you think that's a little\x01",
            "cold-hearted?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#025FWhat, that's it? You had me\x01",
            "going there for a minute...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F8E")

    label("loc_4EBD")


    ChrTalk(
        0xF,
        (
            "#020FI guess you've liked fishing ever\x01",
            "since you were a kid, haven't\x01",
            "you, Estelle?\x02\x03",
            "Even though it's usually a hobby\x01",
            "for boys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001FIt shouldn't matter if I'm a boy\x01",
            "or not. I like the things I like.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F8E")

    SetChrSubChip(0xF, 0)

    label("loc_4F93")

    TalkEnd(0xF)
    Return()

    # Function_14_449A end

    def Function_15_4F97(): pass

    label("Function_15_4F97")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(17490, 0, 11000, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0xA, 17247, 0, 11528, 180)
    SetChrPos(0x101, 18088, 0, 10277, 270)
    SetChrPos(0x102, 18100, 0, 9000, 270)
    SetChrPos(0x103, 15700, 0, 10682, 90)
    SetChrPos(0x104, 15500, 0, 9000, 90)

    ChrTalk(
        0xA,
        (
            "I see...so you heard from\x01",
            "Mr. Kuwano, did you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Yeah, I saw that strange pair\x01",
            "about two nights ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FI knew it...\x02\x03",
            "Could we get you to fill us in\x01",
            "a little more on the details?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Before that, are you all bracers\x01",
            "or something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Is this somehow related to some\x01",
            "sorta crime?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012FWe can't say for sure, but there\x01",
            "does appear to be a possibility.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Gotcha... In that case, I'll\x01",
            "do what I can to help you out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It was the other night when\x01",
            "I was out fishing on my boat...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I was returning to the inn, dead\x01",
            "tired after a day of battling it out\x01",
            "with the master of this lake...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It had gotten late into the night, and\x01",
            "it was about the time when everyone at\x01",
            "the inn was asleep in their beds...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#022FNow hold on a minute.\x01",
            "What do you mean by\x01",
            "'the master of this lake'?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "I'm glad you asked!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "The 'master' is a giant salmon\x01",
            "that swims the murky depths of\x01",
            "Valleria Lake!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It has been the feared king of\x01",
            "the waters among fishing-lovers\x01",
            "for over a decade!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x103,
        "#023F(Crap...I shouldn't have asked...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#017F(It looks like you've thrown a\x01",
            "log onto the maniac's fire...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004FIs-is it really that huge of a fish\x01",
            "like you say?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "You bet your last mira it is!\x01",
            "And I've been chasing the darn thing\x01",
            "for the last five years of my life...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It comes and goes in different parts\x01",
            "of Valleria Lake and changes its\x01",
            "feeding spots on a whim.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I heard from a buddy of mine that it\x01",
            "had appeared in these parts, so I\x01",
            "came a runnin' from the Royal City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#035FHa, now that's what I call passion.\x01",
            "I can completely understand where\x01",
            "you're coming from.\x02\x03",
            "Whenever I find something I like,\x01",
            "I stop at nothing until I get ahold\x01",
            "of it.\x02\x03",
            "For example, a bottle of Grand\x01",
            "Chardonnay and such.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007FIn your case 'steal it' is more\x01",
            "accurate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#026F*cough* How about we get back\x01",
            "to our story?\x02\x03",
            "So Lloyd, what happened when you\x01",
            "came back from fishing that night?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Oh, right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I had returned the boat and was\x01",
            "on my way into the inn...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "When I saw an odd couple head\x01",
            "out onto the road from the grounds\x01",
            "behind the building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012FOnto the road...in the middle of\x01",
            "the night?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Yep, no doubt about it.\x01",
            "They headed out on the\x01",
            "New Ansel Path.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "At first I thought they were a group\x01",
            "of people visiting from the city,\x01",
            "heading back home...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "But it was way too late for something like\x01",
            "that and when I asked at the inn the next\x01",
            "day, nobody knew a thing about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Thought maybe I'd seen a coupla\x01",
            "ghosts or something then!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#004FGh-ghosts?!\x02\x03",
            "Th-There are ghosts that come\x01",
            "out here?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Ha ha, just so you know, the two\x01",
            "I saw were a young couple.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "They mighta been two lost souls who committed\x01",
            "a double suicide after not being accepted by\x01",
            "those around them...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#003FAwww, d-don't tell me any more!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#025FOh brother...a bracer that's afraid\x01",
            "of ghosts? The guild is doomed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FNot to mention, her habit of always\x01",
            "wanting to hear more ghost stories\x01",
            "and other bizarre stuff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#031FHmm-hmm-hmm. Well, isn't your being scared\x01",
            "attractive in its own right, Estelle? Not\x01",
            "sexy, but cute nonetheless.\x02\x03",
            "Like a little kitten shivering\x01",
            "in the cold.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#009F...You'd better watch out because\x01",
            "this little kitten bites!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Ha ha ha. Well, I was just kidding\x01",
            "about the ghost part.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "But the couple did, in fact, seem to\x01",
            "be one with a purpose and reason.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I say this, because the girl was\x01",
            "wearing some rather odd clothing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FWhat do you mean by that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I only saw her from behind,\x01",
            "so I couldn't say for sure...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "But it looked to me like she was\x01",
            "wearing some kinda school\x01",
            "uniform.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(500)
    OP_62(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#004FA school uniform...\x01",
            "It couldn't be...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014FIt wasn't one from the Jenis\x01",
            "Royal Academy, was it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Wow, you really know your\x01",
            "stuff, kid!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "You betcha. My niece goes there\x01",
            "as well, and it looked exactly the\x01",
            "same as the one she wears.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#022FI see... This whole event just\x01",
            "got a lot more interesting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009FIt's her! I know it's that lying\x01",
            "tomboy for sure!\x02\x03",
            "We're finally onto her trail!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "What...so she's an acquaintance\x01",
            "of yours?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Then while you're at it, tell the two\x01",
            "of them not to fret and rush into\x01",
            "anything they'll regret later on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If my mind isn't failing me, I coulda\x01",
            "sworn they said something about\x01",
            "coming again tonight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014FIs that true?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Yep. 'We'll meet back here in two\x01",
            "days,' is what the young man said.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "His tone seemed rather serious,\x01",
            "so I couldn't help but think on it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020FWell, that's understandable...\x02\x03",
            "We appreciate the valuable information.\x01",
            "Just leave the rest up to us.\x02\x03",
            "We won't let them get into any more\x01",
            "trouble than they already are.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Oh, I see...that's a relief to hear.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I feel like a weight's been lifted\x01",
            "off my shoulders now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Now that that is off my chest\x01",
            "I feel like taking a boat out\x01",
            "and fishing again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Well, there's no time to lose!\x01",
            "I'll leave you youngins to your\x01",
            "work!\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0xA, 0x5F17, 0x0, 0x37A7, 0x3A98, 0x0)
    SetChrFlags(0xA, 0x80)
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#000FMan...I don't even measure up when\x01",
            "it comes to that fishing nut.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FHe mentioned something about a\x01",
            "'Fisherman's Guild' too. I wonder\x01",
            "what kind of group that is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#030FSo how is this couple involved with\x01",
            "the missing airliner incident exactly?\x02\x03",
            "If you don't mind telling me,\x01",
            "that is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#020FWell, in a nutshell...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Schera explained that they encountered\x01",
            "Josette in Rolent.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x104,
        (
            "#033FI see... That seems to be the\x01",
            "person in question, all right.\x02\x03",
            "Which means that tonight is\x01",
            "the night, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020FYeah...\x02\x03",
            "It looks like we should probably\x01",
            "get a room just in case.\x02\x03",
            "We're going to be in for a late\x01",
            "night tonight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FAll right, let's go ask the receptionist\x01",
            "about a room.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x103, 0x4)
    ClearChrFlags(0x104, 0x4)
    Fade(1000)
    SetChrPos(0x0, 17154, 0, 12588, 0)
    SetChrPos(0x1, 17154, 0, 12588, 0)
    SetChrPos(0x2, 17154, 0, 12588, 0)
    SetChrPos(0x3, 17154, 0, 12588, 0)
    EventEnd(0x0)
    Return()

    # Function_15_4F97 end

    def Function_16_67A8(): pass

    label("Function_16_67A8")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(23550, 0, 12290, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3030, 0)
    OP_6C(45000, 0)
    OP_6E(261, 0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrSubChip(0xF, 2)
    SetChrSubChip(0x10, 1)
    OP_4A(0x9, 255)
    OP_4A(0x8, 255)
    OP_8C(0x9, 0, 0)
    OP_6D(17310, 0, 5790, 6000)
    OP_A2(0x3FB)
    SetMapFlags(0x2000000)
    NewScene("ED6_DT01/T1500   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_16_67A8 end

    def Function_17_6832(): pass

    label("Function_17_6832")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    Fade(1000)
    OP_6D(15740, 0, 7650, 0)
    SetChrPos(0x101, 15500, 0, 7820, 225)
    SetChrPos(0x102, 16400, 0, 7540, 225)
    OP_0D()

    ChrTalk(
        0x10,
        (
            "#038FHelp a fellow out...\x01",
            "I'm begging you...\x02\x03",
            "I-I can't...take another...drink...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004FWow, I think I've just reconsidered\x01",
            "my opinion of you, Olivier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FIt's pretty rare for anyone to still\x01",
            "be conscious after a night of wine\x01",
            "with Schera.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xF, 2)
    Sleep(300)
    OP_62(0xF, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xF,
        (
            "#028FHmm-hmm-hmm... Well, didn't the\x01",
            "two of you come at a good time?侓\x02\x03",
            "How about having a drink\x01",
            "together?\x02\x03",
            "You're both good for that, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)

    ChrTalk(
        0x101,
        (
            "#009FW-We're going to eat dinner now,\x01",
            "so the answer is no!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#029FCome on, you two. When I say,\x01",
            "'Let's drink,' we drink!\x02\x03",
            "You're going to make me veeeeery\x01",
            "angry if you don't sit down for a\x01",
            "glass with me!\x02",
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
            "#007FOh, great, she's already reached\x01",
            "Stage 2: Rage Mode...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019FDon't worry, Schera. Olivier said he's\x01",
            "good for another couple rounds.\x02\x03",
            "How about having him keep you\x01",
            "company?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xF, 0)
    Sleep(300)
    OP_8C(0x101, 225, 0)

    ChrTalk(
        0xF,
        (
            "#028F#4P...Tsk.\x02\x03",
            "#021FWhat? So you can still drink\x01",
            "more, can you?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 1700, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x10,
        (
            "#036FEeek...\x02\x03",
            "J-Joshua...how could you just\x01",
            "give me to her like that?\x01",
            "I can't... I can't...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008FD-Don't you feel sorry for the\x01",
            "poor guy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FI don't know, should I?\x02",
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 1700, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x10,
        (
            "#035FYou're...like a little...demon...\x01",
            "and cute at the...same time\x01",
            "too...\x02\x03",
            "Hee hee hee...\x01",
            "At least the fish are polite\x01",
            "here...*hic*\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007FAh, I guess he'll be just fine.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#019FHow about we sit at the\x01",
            "counter?\x02\x03",
            "I'd hate to bother the two\x01",
            "of them.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#001FRight, good idea.\x02",
    )

    CloseMessageWindow()
    OP_43(0x101, 0x1, 0x0, 0x12)
    OP_43(0x102, 0x1, 0x0, 0x13)
    Sleep(1000)
    OP_6D(14770, 0, 6250, 2000)
    Sleep(1000)

    ChrTalk(
        0x10,
        (
            "#036FPlease, Schera...I'm pleading\x01",
            "with you...you and the fish...\x01",
            "Don't pour me another glass...\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0xF9, 0x0, 0x64)
    Fade(1000)
    SetChrSubChip(0x12, 5)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x10,
        "#038FAhhhhhh...\x02",
    )

    CloseMessageWindow()
    OP_3F(0x332, 1)
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    OP_20(0x7D0)
    FadeToDark(2000, 0, -1)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T1501   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_17_6832 end

    def Function_18_6F68(): pass

    label("Function_18_6F68")

    Sleep(700)
    SetChrFlags(0xFE, 0x4)
    OP_8C(0xFE, 90, 400)
    OP_8E(0xFE, 0x4808, 0x0, 0x1D4C, 0x7D0, 0x0)
    OP_8E(0xFE, 0x4CAE, 0x0, 0x2206, 0x7D0, 0x0)
    OP_8E(0xFE, 0x6176, 0x0, 0x224C, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_18_6F68 end

    def Function_19_6FC2(): pass

    label("Function_19_6FC2")

    OP_8C(0xFE, 90, 400)
    SetChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0x4808, 0x0, 0x1D4C, 0x7D0, 0x0)
    OP_8E(0xFE, 0x4CAE, 0x0, 0x2206, 0x7D0, 0x0)
    OP_8E(0xFE, 0x6176, 0x0, 0x224C, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_19_6FC2 end

    def Function_20_7017(): pass

    label("Function_20_7017")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There are some fishing rods propped against the rack.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_20_7017 end

    SaveToFile()

Try(main)
