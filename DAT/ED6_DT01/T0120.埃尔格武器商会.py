from ED6ScenarioHelper import *

def main():
    # 埃尔格武器商会

    CreateScenaFile(
        FileName            = 'T0120   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0120.x',
        MapIndex            = 4,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/T0120   ._SN',
            'ED6_DT01/T0120_1 ._SN',
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
        'Freddy',                               # 9
        'Melders',                              # 10
        'Elger',                                # 11
        'Stella',                               # 12
        'Scherazard',                           # 13
        'Dorothy',                              # 14
        'Target Camera',                        # 15
    )

    DeclEntryPoint(
        Unknown_00              = -39000,
        Unknown_04              = 0,
        Unknown_08              = -4000,
        Unknown_0C              = 4,
        Unknown_0E              = 270,
        Unknown_10              = 0,
        Unknown_14              = 8000,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2600,
        Unknown_2C              = 262,
        Unknown_30              = 315,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 4,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = -39000,
        Unknown_04              = 0,
        Unknown_08              = -5000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 8000,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2600,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 6,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = -43000,
        Unknown_04              = 0,
        Unknown_08              = 2000,
        Unknown_0C              = 4,
        Unknown_0E              = 180,
        Unknown_10              = 0,
        Unknown_14              = 8000,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2600,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 6,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = -37000,
        Unknown_04              = 0,
        Unknown_08              = 66000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 8000,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2600,
        Unknown_2C              = 262,
        Unknown_30              = 315,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 4,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH01040 ._CH',             # 00
        'ED6_DT07/CH01000 ._CH',             # 01
        'ED6_DT07/CH01680 ._CH',             # 02
        'ED6_DT07/CH01690 ._CH',             # 03
        'ED6_DT07/CH00020 ._CH',             # 04
        'ED6_DT07/CH02070 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT07/CH01040P._CP',             # 00
        'ED6_DT07/CH01000P._CP',             # 01
        'ED6_DT07/CH01680P._CP',             # 02
        'ED6_DT07/CH01690P._CP',             # 03
        'ED6_DT07/CH00020P._CP',             # 04
        'ED6_DT07/CH02070P._CP',             # 05
    )

    DeclNpc(
        X                   = -38180,
        Z                   = 0,
        Y                   = -497,
        Direction           = 180,
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
        X                   = -39499,
        Z                   = 0,
        Y                   = 678,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -36678,
        Z                   = 0,
        Y                   = 73751,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -86132,
        Z                   = 0,
        Y                   = 71210,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 200,
        Z                   = 0,
        Y                   = 74200,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -44500,
        Z                   = 0,
        Y                   = -360,
        Direction           = 279,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -41900,
        Y                   = 0,
        Z                   = 1877,
        Range               = -44000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x10A4,
        Unknown_18          = 0x0,
        Unknown_1C          = 13,
    )

    DeclEvent(
        X                   = -37700,
        Y                   = 0,
        Z                   = -5500,
        Range               = -40500,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0xFFFFDF76,
        Unknown_18          = 0x0,
        Unknown_1C          = 14,
    )


    DeclActor(
        TriggerX            = -38537,
        TriggerZ            = 0,
        TriggerY            = -1845,
        TriggerRange        = 400,
        ActorX              = -38180,
        ActorZ              = 1500,
        ActorY              = -497,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -41599,
        TriggerZ            = 0,
        TriggerY            = 299,
        TriggerRange        = 1000,
        ActorX              = -39499,
        ActorZ              = 1500,
        ActorY              = 678,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -36170,
        TriggerZ            = 0,
        TriggerY            = 71651,
        TriggerRange        = 1000,
        ActorX              = -36678,
        ActorZ              = 1500,
        ActorY              = 73751,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_332",          # 00, 0
        "Function_1_39E",          # 01, 1
        "Function_2_3C0",          # 02, 2
        "Function_3_3D6",          # 03, 3
        "Function_4_3DB",          # 04, 4
        "Function_5_1A51",         # 05, 5
        "Function_6_1A56",         # 06, 6
        "Function_7_2BC0",         # 07, 7
        "Function_8_2BC5",         # 08, 8
        "Function_9_4C17",         # 09, 9
        "Function_10_6771",        # 0A, 10
        "Function_11_7BAA",        # 0B, 11
        "Function_12_7BE8",        # 0C, 12
        "Function_13_7C18",        # 0D, 13
        "Function_14_7CC4",        # 0E, 14
        "Function_15_7D70",        # 0F, 15
        "Function_16_91D4",        # 10, 16
        "Function_17_A0C1",        # 11, 17
        "Function_18_A0F3",        # 12, 18
        "Function_19_A15B",        # 13, 19
        "Function_20_A177",        # 14, 20
    )


    def Function_0_332(): pass

    label("Function_0_332")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_340")
    OP_8C(0x9, 90, 0)

    label("loc_340")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (101, "loc_350"),
        (102, "loc_363"),
        (SWITCH_DEFAULT, "loc_376"),
    )


    label("loc_350")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0xA, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_363")
    Event(0, 15)

    label("loc_363")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_373")
    Event(0, 16)

    label("loc_373")

    Jump("loc_376")

    label("loc_376")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_39D")
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xD, 0x8)
    SetChrPos(0xD, -44500, 0, -320, 283)

    label("loc_39D")

    Return()

    # Function_0_332 end

    def Function_1_39E(): pass

    label("Function_1_39E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3B6")
    OP_B1("t0120_y")
    Jump("loc_3BF")

    label("loc_3B6")

    OP_B1("t0120_n")

    label("loc_3BF")

    Return()

    # Function_1_39E end

    def Function_2_3C0(): pass

    label("Function_2_3C0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3D5")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_3C0")

    label("loc_3D5")

    Return()

    # Function_2_3C0 end

    def Function_3_3D6(): pass

    label("Function_3_3D6")

    Call(0, 4)
    Return()

    # Function_3_3D6 end

    def Function_4_3DB(): pass

    label("Function_4_3DB")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_478")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",              # 0
            "Modify/Trade\x01",      # 1
            "Leave\x01",             # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_467")
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_44F")
    OP_A9(0x0)
    Jump("loc_45E")

    label("loc_44F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45C")
    OP_A9(0x9)
    Jump("loc_45E")

    label("loc_45C")

    OP_A9(0x70)

    label("loc_45E")

    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_467")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_478")
    TalkEnd(0x8)
    Return()

    label("loc_478")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_5CA")
    OP_A2(0x228)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_56A")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "The piece of septium that my dad\x01",
            "was asked to engrave for the mayor\x01",
            "finally arrived.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "This is the first time I've ever\x01",
            "seen such a splendid piece\x01",
            "of esmelas.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "My dad's doing the etchings\x01",
            "on it, right now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C7")

    label("loc_56A")


    ChrTalk(
        0x8,
        (
            "I just can't compare when it comes\x01",
            "to the kind of detail work my dad\x01",
            "can do on septium.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C7")

    Jump("loc_1A46")

    label("loc_5CA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x6, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x6, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5EF")
    OP_A2(0x228)
    Call(1, 3)
    Jump("loc_1A46")

    label("loc_5EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_END)), "loc_71F")
    OP_A2(0x228)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6A4")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "The mayor came by to ask about\x01",
            "some septium engraving earlier...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "But the key piece of esmelas\x01",
            "hasn't arrived.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I wonder if something happened.\x02",
    )

    CloseMessageWindow()
    Jump("loc_71C")

    label("loc_6A4")


    ChrTalk(
        0x8,
        (
            "The mayor came by to ask about\x01",
            "some septium engraving earlier...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "But the key piece of esmelas\x01",
            "hasn't arrived.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_71C")

    Jump("loc_1A46")

    label("loc_71F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_8A7")
    OP_A2(0x228)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_809")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "The mayor came by to ask about\x01",
            "some septium engraving a bit ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Although the esmelas hasn't arrived,\x01",
            "I hear it's quite the magnificent\x01",
            "crystal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm looking forward to seeing\x01",
            "what it looks like.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A4")

    label("loc_809")


    ChrTalk(
        0x8,
        (
            "The mayor came by to ask about\x01",
            "some septium engraving a bit ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Although the esmelas hasn't arrived,\x01",
            "I hear it's quite the magnificent\x01",
            "crystal.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8A4")

    Jump("loc_1A46")

    label("loc_8A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_C4E")
    OP_A2(0x228)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 3)), scpexpr(EXPR_END)), "loc_AA6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A47")
    OP_A2(0x0)
    TurnDirection(0x8, 0x110, 400)

    ChrTalk(
        0x8,
        (
            "Your camera is one of the\x01",
            "really nice, new models,\x01",
            "Dorothy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "This is for professionals, so I think\x01",
            "it may be a bit difficult to use...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x110,
        (
            "#150FTee hee hee.\x01",
            "Are you talking about Poochie?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "P-Poochie?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x110,
        (
            "#151FHe's so cute and does whatever\x01",
            "I tell him to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "H-Huh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10F,
        (
            "#145FIf you listen to everything she\x01",
            "says, you're just going to end\x01",
            "up with a headache.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AA3")

    label("loc_A47")


    ChrTalk(
        0x8,
        (
            "Ha ha. If you're in this business\x01",
            "long enough, you'll run into all\x01",
            "types of customers.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AA3")

    Jump("loc_C4B")

    label("loc_AA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B8E")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "It seems that there was a large\x01",
            "piece of septium discovered in\x01",
            "a new lode at the mine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Something like that is going to\x01",
            "be rather pricey, but it seems\x01",
            "like it already has a buyer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I wonder who bought it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_C4B")

    label("loc_B8E")


    ChrTalk(
        0x8,
        (
            "It seems that there was a large\x01",
            "piece of septium discovered in\x01",
            "a new lode at the mine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Something like that is going to\x01",
            "be rather pricey, but it seems\x01",
            "like it already has a buyer.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C4B")

    Jump("loc_1A46")

    label("loc_C4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_E84")
    OP_A2(0x228)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_D2F")

    ChrTalk(
        0x8,
        (
            "Thank you to the both of\x01",
            "you for replacing that light.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you need to discuss anything\x01",
            "about orbments then stop by\x01",
            "anytime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Don't forget to swing by if you\x01",
            "have any other business needs.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E81")

    label("loc_D2F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x6, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D4C")
    OP_A2(0x228)
    Call(1, 0)
    Jump("loc_E81")

    label("loc_D4C")

    OP_A2(0x228)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E07")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "How are your orbments working\x01",
            "out for you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you want to use new arts you'll\x01",
            "need to modify your orbments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please bring them here if you\x01",
            "want to do that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E81")

    label("loc_E07")


    ChrTalk(
        0x8,
        (
            "If you want to use new arts you'll\x01",
            "need to modify your orbments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please bring them here if you\x01",
            "want to do that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E81")

    Jump("loc_1A46")

    label("loc_E84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_F3A")
    OP_A2(0x228)

    ChrTalk(
        0x8,
        (
            "It looks like the airliner bound for\x01",
            "the Royal City from Bose arrived.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "But since we've got nothing coming\x01",
            "in, we'll be able to focus on work\x01",
            "here in the shop.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A46")

    label("loc_F3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_10AD")
    OP_A2(0x228)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1032")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "If you're aiming to become a first-\x01",
            "class bracer, mastering orbal arts\x01",
            "will probably be essential.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We get a number of bracers\x01",
            "stopping by the shop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "They always modify their orbments\x01",
            "after checking them first.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10AA")

    label("loc_1032")


    ChrTalk(
        0x8,
        (
            "We get a number of bracers\x01",
            "stopping by the shop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "They always modify their orbments\x01",
            "after checking them first.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10AA")

    Jump("loc_1A46")

    label("loc_10AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_143D")
    OP_A2(0x228)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x54, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13C7")
    OP_A2(0x2A2)

    ChrTalk(
        0x8,
        "Hey. You're doing good work so far.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ah! What's that emblem\x01",
            "on your chests?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Congratulations, you two!\x01",
            "So you've finally become\x01",
            "bracers, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001FTee hee, thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#018FEstelle, you are way too proud\x01",
            "of yourself.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        (
            "#001FWhy do you always have to ruin\x01",
            "the moment, Joshua? I should be\x01",
            "this happy because I earned it.\x02\x03",
            "#502FYou should at least let me bask\x01",
            "in the glory for a minute.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#017FSometimes, you can just be so...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "But, Estelle.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 500)

    ChrTalk(
        0x8,
        (
            "Now that you've become a bracer,\x01",
            "you're going to have to get over your\x01",
            "little...uh, problem, with orbal arts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004FMan...you, too? Why do you have\x01",
            "to go and spoil my day by saying\x01",
            "things like that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ha ha ha. If you have any other\x01",
            "business needs, don't forget to\x01",
            "stop by.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_143A")

    label("loc_13C7")


    ChrTalk(
        0x8,
        "All right, Rolent's two newest bracers.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you have any other business\x01",
            "needs, don't forget to stop by.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_143A")

    Jump("loc_1A46")

    label("loc_143D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_14E5")

    ChrTalk(
        0x8,
        (
            "Hi there. It looks like you two\x01",
            "are doing well in your training.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you would like to modify your\x01",
            "orbments, please select the\x01",
            "Modify/Trade service.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A46")

    label("loc_14E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_198D")
    OP_A2(0x0)
    OP_A2(0x20D)
    OP_A2(0x228)

    ChrTalk(
        0x8,
        "Hey, if it isn't Joshua and Estelle?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "How are those orbments working\x01",
            "out for you that we tuned the\x01",
            "other time you were here?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        (
            "#017FIn your case, Estelle, it's not whether\x01",
            "the orbment is good or bad, the\x01",
            "problem lies in the way you use it.\x02\x03",
            "#017FYou're always jumping into things\x01",
            "without a second thought, so you\x01",
            "end up being slow to learn.\x02\x03",
            "#010FIf you'd just start thinking before\x01",
            "you start swinging, then you'd\x01",
            "learn twice as much.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(800)
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        "#002FWell, excuse me for sucking.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "There, there. No need to get upset.\x01",
            "Everyone has these problems when\x01",
            "they first start out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you can get the hang of things,\x01",
            "you'll gradually be able to handle\x01",
            "them better.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FThat's right!\x02\x03",
            "#001FI'm going to master using this\x01",
            "as quick as I can and surpass\x01",
            "even Joshua!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FYeah, yeah, whatever.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "When I first entered the Zeiss Central\x01",
            "Factory, I pretty much couldn't use\x01",
            "one of these things either.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 500)

    ChrTalk(
        0x101,
        "#004FEven you couldn't use one, Freddy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yeah, but I can still become an\x01",
            "engineer even if I can't use one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "But since you're aiming to become\x01",
            "a bracer, you'll have to learn how.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007FArgh...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A46")

    label("loc_198D")


    ChrTalk(
        0x8,
        (
            "Everyone has a bit of trouble getting\x01",
            "the hang of battle orbments from the\x01",
            "start.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you can get the hang of things,\x01",
            "eventually you'll be able to handle\x01",
            "them better, Estelle.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A46")

    OP_56(0x0)
    TalkEnd(0x8)
    Sleep(300)
    Return()

    # Function_4_3DB end

    def Function_5_1A51(): pass

    label("Function_5_1A51")

    Call(0, 6)
    Return()

    # Function_5_1A51 end

    def Function_6_1A56(): pass

    label("Function_6_1A56")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_1BB5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B6D")
    OP_A2(0x1)

    ChrTalk(
        0x9,
        (
            "That septium from the mayor\x01",
            "finally arrived...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Now this is one fine crystal,\x01",
            "I tell you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "And I hear it's even going to be\x01",
            "a present to Her Majesty the\x01",
            "Queen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It's been a while since I've been\x01",
            "this excited to do a job, that's\x01",
            "for sure.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BB2")

    label("loc_1B6D")


    ChrTalk(
        0x9,
        (
            "This is something that I dare not\x01",
            "leave up to Freddy to handle.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BB2")

    Jump("loc_2BBC")

    label("loc_1BB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_END)), "loc_1CEE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C81")
    OP_A2(0x1)

    ChrTalk(
        0x9,
        "I accepted the job from the mayor...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "But he hasn't shown up even\x01",
            "though he promised to come by.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It's not like him, since he's always\x01",
            "been a stickler about punctuality.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CEB")

    label("loc_1C81")


    ChrTalk(
        0x9,
        (
            "I accepted the job from\x01",
            "the mayor...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "But he hasn't shown up even\x01",
            "though he promised to come by.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CEB")

    Jump("loc_2BBC")

    label("loc_1CEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_1E3C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DB1")
    OP_A2(0x1)

    ChrTalk(
        0x9,
        (
            "I've heard that orbments were\x01",
            "based on ancient tools.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It's not the people of today who are\x01",
            "amazing, it's those people of old.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Somehow it's a bit mortifying...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E39")

    label("loc_1DB1")


    ChrTalk(
        0x9,
        (
            "I've heard that orbments were\x01",
            "based on ancient tools.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It's not the people of today who are\x01",
            "amazing, it's those people of old.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E39")

    Jump("loc_2BBC")

    label("loc_1E3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_2007")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 3)), scpexpr(EXPR_END)), "loc_1EB2")

    ChrTalk(
        0x9,
        "Glad that unpleasantness is behind us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It was...unsightly, the way Freddy\x01",
            "behaved himself.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2004")

    label("loc_1EB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F8B")
    OP_A2(0x1)

    ChrTalk(
        0x9,
        (
            "I just saw the mayor, but he \x01",
            "was all fidgety.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "He's always been like that, even\x01",
            "before he was elected mayor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "A mayor is a type of person who\x01",
            "really needs to sink their teeth\x01",
            "into the job.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2004")

    label("loc_1F8B")

    OP_A2(0x1)

    ChrTalk(
        0x9,
        (
            "I just saw the mayor, but he\x01",
            "was all fidgety.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "He's always been like that, even\x01",
            "before he was elected mayor.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2004")

    Jump("loc_2BBC")

    label("loc_2007")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_21CC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2133")
    OP_A2(0x1)

    ChrTalk(
        0x9,
        (
            "I hear that the airliners are equipped\x01",
            "with huge machines called orbal\x01",
            "engines or some such thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "They're said to use an orbment\x01",
            "structure as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It seems that some big-wig professor\x01",
            "was the one who developed them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Heh, now that's something to\x01",
            "talk about.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21C9")

    label("loc_2133")


    ChrTalk(
        0x9,
        (
            "I hear that the airliners are equipped\x01",
            "with huge machines called orbal\x01",
            "engines or some such thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Heh, now that's something to\x01",
            "talk about.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21C9")

    Jump("loc_2BBC")

    label("loc_21CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_234C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22DF")
    OP_A2(0x1)

    ChrTalk(
        0x9,
        (
            "Is that you, Estelle and Joshua?\x01",
            "Could you not bother me while\x01",
            "I'm working?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...But I guess you're old enough that\x01",
            "I don't have to tell you that, huh?\x01",
            "And you're bracers, too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Now that's something else.\x01",
            "I've changed my mind about you kids.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2349")

    label("loc_22DF")


    ChrTalk(
        0x9,
        "So you're bracers now, are you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Now that's something else.\x01",
            "I've changed my mind about you kids.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2349")

    Jump("loc_2BBC")

    label("loc_234C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_23EA")

    ChrTalk(
        0x9,
        (
            "Oh, it's this late already?\x01",
            "I guess it's time to close up shop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "You kids quit loitering around\x01",
            "here and get yourselves home,\x01",
            "you hear me?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BBC")

    label("loc_23EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_2608")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2553")
    OP_A2(0x1)

    ChrTalk(
        0x9,
        (
            "The orbments we see today are built\x01",
            "using the structure of a clock.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Therefore, even old technicians such\x01",
            "as myself can tinker with some of\x01",
            "their parts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "When it comes to these quartz\x01",
            "circuits, however, I'm a bit out\x01",
            "of my league.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I don't know who invented these\x01",
            "things, but they're extremely\x01",
            "complicated little machines.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2605")

    label("loc_2553")


    ChrTalk(
        0x9,
        (
            "When it comes to these quartz\x01",
            "circuits, however, I'm a bit out\x01",
            "of my league.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I don't know who invented these\x01",
            "things, but they're extremely\x01",
            "complicated little machines.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2605")

    Jump("loc_2BBC")

    label("loc_2608")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2679")

    ChrTalk(
        0x9,
        "Oh, good work so far.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If you need to use the orbal factory,\x01",
            "give Freddy a holler over there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BBC")

    label("loc_2679")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AE8")
    OP_A2(0x1)

    ChrTalk(
        0x9,
        "Hey, I'm still setting up shop.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Ah, Estelle and Joshua.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "You seem to be here rather early.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000FGood morning, Mr. Melders.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x9, 500)

    ChrTalk(
        0x102,
        (
            "#010FGood morning, sir.\x02\x03",
            "#010FWe appreciate you fixing that\x01",
            "orbment light the other day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FSpeaking of orbment lights, isn't the\x01",
            "one outside our house burned out?\x01",
            "We should get that replaced ASAP!\x02\x03",
            "#001FOrbments sure are a daily life\x01",
            "necessity, aren't they?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "When I was a lad, there weren't\x01",
            "any of these orbment thingies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Now we can get fire and light\x01",
            "with the mere flip of a switch\x01",
            "and even ships fly in the skies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I don't like it. Don't you kids think\x01",
            "things are way too convenient these\x01",
            "days?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#007F(Oh crap... There he goes again\x01",
            "about 'the old days'...)\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#017F(Yeah, well if you'd just learn\x01",
            "to shut your big trap...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "When I was young, I made things a\x01",
            "reality through hard work and sweat.\x01",
            "Sweat, I tell ya!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It would be nice if the young kids\x01",
            "these days knew the meaning of\x01",
            "the phrase 'hard work'.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#008FAh ha ha ha.\x01",
            "You're probably right.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BBC")

    label("loc_2AE8")


    ChrTalk(
        0x9,
        (
            "Orbments are convenient all right,\x01",
            "but I get worried that young kids don't\x01",
            "understand what it means to work hard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "You hear me, Estelle? Joshua?\x01",
            "Don't forget what it means to\x01",
            "stand on your own two feet.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BBC")

    TalkEnd(0x9)
    Return()

    # Function_6_1A56 end

    def Function_7_2BC0(): pass

    label("Function_7_2BC0")

    Call(0, 8)
    Return()

    # Function_7_2BC0 end

    def Function_8_2BC5(): pass

    label("Function_8_2BC5")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x44, 6)), scpexpr(EXPR_END)), "loc_2C3D")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C2C")
    OP_0D()
    OP_A9(0x1)
    OP_56(0x0)
    TalkEnd(0xA)
    Return()

    label("loc_2C2C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C3D")
    TalkEnd(0xA)
    Return()

    label("loc_2C3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_2F76")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EF0")
    OP_A2(0x2)
    OP_A2(0x226)

    ChrTalk(
        0xA,
        (
            "Oh hey, Joshua and Estelle.\x01",
            "What's with the baggage?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012FUm, actually...we're...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Estelle and Joshua filled Elger\x01",
            "in on the details.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0xA,
        (
            "Cassius has what...?! And that's\x01",
            "why you're headed to Bose?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Of all people, I can't imagine that\x01",
            "anything has happened to him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FYes. I'm under the same impression.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006FWhich is why we're off to Bose\x01",
            "to check on things.\x02\x03",
            "Just sitting around would hardly\x01",
            "make us feel better.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Understandable.\x01",
            "That's just like you kids, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Well, with Scherazard tagging along,\x01",
            "I guess there's nothing to be worried\x01",
            "about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Good luck and be careful\x01",
            "out there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001FWe will!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F73")

    label("loc_2EF0")


    ChrTalk(
        0xA,
        (
            "Oh right, I'll make sure to let\x01",
            "Stella know about this myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I imagine she'll probably be a\x01",
            "bit flustered at the news.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F73")

    Jump("loc_4C0C")

    label("loc_2F76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_END)), "loc_31FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_316E")
    OP_A2(0x2)
    OP_A2(0x226)

    ChrTalk(
        0xA,
        (
            "Oh, Estelle and Joshua. And is that\x01",
            "Scherazard I see with you, too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#020FYeah, our work overlapped a bit.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I see. I had a new whip scheduled\x01",
            "to come in, but unfortunately it\x01",
            "won't get here 'til much later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FCome to think of it, Schera, you\x01",
            "used a sword for training, so why\x01",
            "take a whip for the job?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020FWell, if you must know...it was an\x01",
            "accessible weapon for me at a\x01",
            "young age, so I'm familiar with it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#018F(A whip? Do I even want to know...?)\x02",
    )

    CloseMessageWindow()
    Jump("loc_31FB")

    label("loc_316E")


    ChrTalk(
        0xA,
        (
            "Make sure to check your equipment\x01",
            "before you head out on any job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Although, I think it's needless\x01",
            "for me to tell that to a bracer.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31FB")

    Jump("loc_4C0C")

    label("loc_31FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_334D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32ED")
    OP_A2(0x2)
    OP_A2(0x226)

    ChrTalk(
        0xA,
        (
            "Hey there! I've been hearing great\x01",
            "things about you kids.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I hear that you've been knocking\x01",
            "out jobs one after another.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "You've made some successful\x01",
            "strides from your part-time job\x01",
            "working here for me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_334A")

    label("loc_32ED")


    ChrTalk(
        0xA,
        (
            "Cassius...Scherazard...and now\x01",
            "the two of you. Rolent bracers\x01",
            "are the best, hands down!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_334A")

    Jump("loc_4C0C")

    label("loc_334D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_3493")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3413")
    OP_A2(0x2)
    OP_A2(0x226)

    ChrTalk(
        0xA,
        (
            "Hey there. The two of you look\x01",
            "rather busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Stop by and show your faces to\x01",
            "Stella every once in a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "No matter what she tells you,\x01",
            "she's a real worrywart.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3490")

    label("loc_3413")


    ChrTalk(
        0xA,
        (
            "Stop by and show your faces to\x01",
            "Stella every once in a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "No matter what she tells you,\x01",
            "she's a real worrywart.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3490")

    Jump("loc_4C0C")

    label("loc_3493")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_36EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3663")
    OP_A2(0x2)
    OP_A2(0x226)

    ChrTalk(
        0xA,
        (
            "Hey there. So I've heard the news\x01",
            "that you've started work as bracers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "How's everything coming along?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FWe're surviving so far.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#502FAnd we managed to deal with\x01",
            "the monster problem at the\x01",
            "Perzel Farm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I see... It seems you have what it\x01",
            "takes, after all, to become adequate\x01",
            "fill-ins for Cassius in his absence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "But Estelle, don't be a handful\x01",
            "for Joshua.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007FWhy am I the one who always\x01",
            "gets lectured?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36EB")

    label("loc_3663")


    ChrTalk(
        0xA,
        (
            "I see. It looks like you've already\x01",
            "managed to become capable\x01",
            "bracers yourselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "And Estelle, don't be a handful\x01",
            "for Joshua.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36EB")

    Jump("loc_4C0C")

    label("loc_36EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_3ADE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x54, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A0C")
    OP_A2(0x2A1)
    OP_A2(0x226)

    ChrTalk(
        0xA,
        (
            "Hey there, how are our 1st-year\x01",
            "bracers doing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "So Cassius is going to be out\x01",
            "for a while, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FYes. We just saw him off at\x01",
            "the landing port.\x02\x03",
            "You sure managed to hear about\x01",
            "it rather quickly, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Ha ha, well...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x102, 400)

    ChrTalk(
        0xA,
        (
            "Back in the day, Cassius used to\x01",
            "leave Estelle with us while he was away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "But after you came here,\x01",
            "he started having you keep an eye\x01",
            "on things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FI didn't know that...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Estelle gets surprisingly lonely\x01",
            "when no one is around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Whenever we had her over, she was\x01",
            "as quiet as a cat among strangers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008FAhh! Don't say stuff like that!\x01",
            "I am not!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "After about two or three days here,\x01",
            "though, she'd eat, sleep, and play like\x01",
            "it was her own house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FHa ha, I can imagine that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#009F...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3ADB")

    label("loc_3A0C")


    ChrTalk(
        0xA,
        (
            "You're both pretty lonely without\x01",
            "Cassius around, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "The two of you are always welcome\x01",
            "to come visit and spend the night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "There's no need to hesitate either.\x01",
            "Stella would love to see you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3ADB")

    Jump("loc_4C0C")

    label("loc_3ADE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_404D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x44, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3C3A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BD3")
    OP_A2(0x2)
    OP_A2(0x226)

    ChrTalk(
        0xA,
        (
            "Whew, it's already that time again?\x01",
            "I put in a good day's work today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "I guess it's about time I closed up shop.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Estelle, Joshua. I'm looking forward\x01",
            "to hearing about other great things\x01",
            "from you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C37")

    label("loc_3BD3")


    ChrTalk(
        0xA,
        (
            "Estelle, Joshua. I'm looking forward\x01",
            "to hearing about other great things\x01",
            "from the both of you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C37")

    Jump("loc_404A")

    label("loc_3C3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x54, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FD2")
    OP_A2(0x2A0)
    OP_A2(0x226)

    ChrTalk(
        0xA,
        "Hey there, Estelle and Joshua.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001FGood evening, Mr. Elger.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FGood evening, sir.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Today was your last day of\x01",
            "training, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I seem to remember you saying\x01",
            "something about it the last time\x01",
            "I had you run the store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FYes, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "So how'd your training go?\x02",
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xA,
        "That emblem on your chest means...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I shouldn't have expected anything\x01",
            "less from Cassius' kids...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FBut, we're still bracers-in-training.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "I see, but, well...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I knew you were going to have to\x01",
            "give up your part-time job here\x01",
            "sooner or later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FYes, I'm really sorry about that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Don't sweat it. I knew it'd happen\x01",
            "eventually when I hired you on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It's a shame, though. There's hardly\x01",
            "anyone out there with as good an eye\x01",
            "for weapons as you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "But that's the path you've chosen.\x01",
            "So get out there and show us what\x01",
            "you're made of.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_404A")

    label("loc_3FD2")


    ChrTalk(
        0xA,
        "Joshua, I'm sad to see you go.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "But I knew this was going to happen\x01",
            "someday, so there's no use crying\x01",
            "over it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_404A")

    Jump("loc_4C0C")

    label("loc_404D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_47D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_439D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x54, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4322")
    OP_A2(0x2A0)
    OP_A2(0x226)

    ChrTalk(
        0x101,
        "#001FGood afternoon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Hey there, Estelle and Joshua.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "So how'd your training go?\x02",
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xA,
        "That emblem on your chest means...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I shouldn't have expected anything\x01",
            "less from Cassius' kids...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FBut, we're still bracers-in-training.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "I see, but, well...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I knew you were going to have to\x01",
            "give up your part-time job here\x01",
            "sooner or later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FYes, I'm really sorry about that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Don't sweat it. I knew it'd happen\x01",
            "eventually when I hired you on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It's a shame, though. There's hardly\x01",
            "anyone out there with as good an eye\x01",
            "for weapons as you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "But that's the path you've chosen.\x01",
            "So get out there and show us what\x01",
            "you're made of.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_439A")

    label("loc_4322")


    ChrTalk(
        0xA,
        "Joshua, I'm sad to see you go.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "But I knew this was going to happen\x01",
            "someday, so there's no use crying\x01",
            "over it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_439A")

    Jump("loc_47D0")

    label("loc_439D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x44, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4758")
    OP_A2(0x225)
    OP_A2(0x226)

    ChrTalk(
        0xA,
        "Hey there, Estelle and Joshua.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001FGood afternoon, Mr. Elger.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FGood afternoon, sir.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Correct me if I'm wrong, but today\x01",
            "is your last day of training, isn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I seem to remember you saying\x01",
            "something about it the last time\x01",
            "I had you run the store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FYes, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "So how'd your training go?\x02",
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xA,
        "That emblem on your chest means...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I shouldn't have expected anything\x01",
            "less from Cassius' kids...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FBut, we're still bracers-in-training.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "I see, but, well...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I knew you were going to have to\x01",
            "give up your part-time job here\x01",
            "sooner or later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FYes, I'm really sorry about that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Don't sweat it. I knew it'd happen\x01",
            "eventually when I hired you on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It's a shame, though. There's hardly\x01",
            "anyone out there with as good an eye\x01",
            "for weapons as you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "But that's the path you've chosen.\x01",
            "So get out there and show us what\x01",
            "you're made of.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47D0")

    label("loc_4758")


    ChrTalk(
        0xA,
        "Joshua, I'm sad to see you go.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "But I knew this was going to happen\x01",
            "someday, so there's no use crying\x01",
            "over it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47D0")

    Jump("loc_4C0C")

    label("loc_47D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x44, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B83")
    OP_A2(0x20E)
    OP_A2(0x226)

    ChrTalk(
        0xA,
        "Top of the morning to you kids.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001FGood morning, Mr. Elger.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FGood morning, sir.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Well, you're up rather early,\x01",
            "aren't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Correct me if I'm wrong, but today\x01",
            "is your last day of training, isn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I seem to remember you saying\x01",
            "something about it the last time\x01",
            "I had you run the store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FYes, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I see. Well, I'm sure you'll do\x01",
            "just fine, Joshua.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Now Estelle on the other hand...\x01",
            "I've got good reason to worry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "She's always been a bit scatterbrained ever\x01",
            "since she was a child. Probably all the knocks\x01",
            "she took to the head playing with the boys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#018FReally...\x02\x03",
            "So I guess that scatterbrained trait\x01",
            "isn't something new, huh?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#009FI'll give YOU a head injury\x01",
            "if you don't shut up!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        "#009FAnd don't call me scatterbrained!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Okay, you two, let's not fight now.\x01",
            "And shouldn't you be getting over\x01",
            "to the guild?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C0C")

    label("loc_4B83")


    ChrTalk(
        0xA,
        (
            "It seems like just yesterday that Estelle\x01",
            "was clinging all over Cassius and now\x01",
            "she's a bracer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "It looks like I'm getting old.\x02",
    )

    CloseMessageWindow()

    label("loc_4C0C")

    OP_56(0x0)
    TalkEnd(0xA)
    Sleep(300)
    Return()

    # Function_8_2BC5 end

    def Function_9_4C17(): pass

    label("Function_9_4C17")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_4D80")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D29")
    OP_A2(0x3)

    ChrTalk(
        0xFE,
        "Hello there, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm-hmm-hmm...\x01",
            "Are you working hard at your job?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F(I don't know if I have the heart to\x01",
            "tell her what's going on this time...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F(Same here...)\x02\x03",
            "#007F(She'd probably cry herself\x01",
            "to sleep if we did...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D7D")

    label("loc_4D29")


    ChrTalk(
        0xFE,
        "Are you all working hard as bracers?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Just try not to overdo things, okay?\x02",
    )

    CloseMessageWindow()

    label("loc_4D7D")

    Jump("loc_676D")

    label("loc_4D80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_END)), "loc_5080")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5026")
    OP_A2(0x2B0)
    TurnDirection(0xFE, 0x103, 0)

    ChrTalk(
        0xFE,
        (
            "Oh my, are you with them today\x01",
            "too, Schera?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020FYes, that's right.\x02\x03",
            "It turns out that I'm going to be\x01",
            "working with the two of them\x01",
            "this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm happy to see that you can work\x01",
            "alongside each other like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "But, Schera...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You shouldn't teach Estelle or Joshua\x01",
            "any bad things, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#025FThat's awfully rude. You don't need\x01",
            "to make me out to be some sort of\x01",
            "evil woman like that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, usually you're a good girl,\x01",
            "but you've got some bad habits,\x01",
            "if you know what I mean.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Understand? If you dare teach them\x01",
            "anything bad...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I-I...I'll just cry!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#025FAll right, all right, I get what\x01",
            "you're saying.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_507D")

    label("loc_5026")


    ChrTalk(
        0xFE,
        (
            "And, you two, don't you dare try\x01",
            "copying any of Schera's bad\x01",
            "habits either, okay?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_507D")

    Jump("loc_676D")

    label("loc_5080")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_5204")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5180")
    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "Well, how are you, Estelle and\x01",
            "Joshua?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The two of you have really grown\x01",
            "up, haven't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although, I'd like you to try and\x01",
            "act a bit more lady-like, Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008FAh ha ha... I'll try to pay more\x01",
            "attention to that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5201")

    label("loc_5180")


    ChrTalk(
        0xFE,
        (
            "The two of you have really grown up,\x01",
            "haven't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although, I'd like you to try and\x01",
            "act a bit more lady-like, Estelle.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5201")

    Jump("loc_676D")

    label("loc_5204")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_53FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x55, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_53B8")
    OP_A2(0x2AF)
    TurnDirection(0xB, 0x101, 400)
    OP_62(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "Huh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Are my eyes deceiving me...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501FWhat's wrong, Stella?\x02\x03",
            "I washed my face this morning\x01",
            "like you've always told me to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Estelle, you...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Your eyes have really begun to\x01",
            "look like your mother's, haven't\x01",
            "they?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004FWhat...\x02\x03",
            "R-Really?\x02\x03",
            "#008FHearing that really makes me\x01",
            "feel happy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My goodness, this has brought\x01",
            "back so many memories.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F...\x02",
    )

    CloseMessageWindow()
    Jump("loc_53FC")

    label("loc_53B8")


    ChrTalk(
        0xFE,
        (
            "Well, please make the most of\x01",
            "each day and work hard together.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_53FC")

    Jump("loc_676D")

    label("loc_53FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_576B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x55, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_56D6")
    OP_A2(0x2AE)

    ChrTalk(
        0xFE,
        (
            "You'll need to work hard so you\x01",
            "can give your father a good report.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just don't overdo it. Moderation is\x01",
            "the key in everything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001FOkay, we know already.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You're still young and inexperienced,\x01",
            "so there's no shame in asking those\x01",
            "around you for help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Especially you, Joshua. You're the\x01",
            "type to keep all your feelings pent\x01",
            "up inside, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's been a source of concern\x01",
            "for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#011FI'm sorry if I've caused you\x01",
            "any undue worry...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm not worried about Estelle being\x01",
            "unable to share her feelings with\x01",
            "the world, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#502FTee hee!\x02\x03",
            "#009F...Wait a sec...\x01",
            "That doesn't sound like a compliment...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, well, nobody said your outspokenness\x01",
            "was a bad thing.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5768")

    label("loc_56D6")


    ChrTalk(
        0xFE,
        (
            "You're still young and inexperienced,\x01",
            "so there's no shame in asking those\x01",
            "around you for help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you need any advice,\x01",
            "I'm always here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5768")

    Jump("loc_676D")

    label("loc_576B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_59BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x55, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_58F1")
    OP_A2(0x2AD)

    ChrTalk(
        0xFE,
        (
            "Well, how are you two doing\x01",
            "today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Cassius is going to be gone\x01",
            "for a while, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000FYeah, that's right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you need anything, please know\x01",
            "you're welcome to come ask for help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We're not strangers or new\x01",
            "acquaintances, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Don't hesitate if you need anything\x01",
            "or I'll be really angry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001FAh ha ha. Thanks for the reminder.\x02",
    )

    CloseMessageWindow()
    Jump("loc_59B8")

    label("loc_58F1")


    ChrTalk(
        0xFE,
        (
            "If you need anything, please know\x01",
            "you're welcome to come ask for help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We're not strangers or new\x01",
            "acquaintances, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Don't hesitate if you need anything\x01",
            "or I'll be really angry.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_59B8")

    Jump("loc_676D")

    label("loc_59BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_5D70")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_59FF")

    ChrTalk(
        0xFE,
        (
            "If you'd like, you can come\x01",
            "eat over anytime.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D6D")

    label("loc_59FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x55, 4)), scpexpr(EXPR_END)), "loc_5ABB")
    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "If you'd like, you can come\x01",
            "eat over anytime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You need energy to function, so\x01",
            "you'll need to get some nutrition\x01",
            "from somewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Schera is also welcome anytime.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5D6D")

    label("loc_5ABB")

    OP_A2(0x2AC)
    OP_62(0xFE, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "Well, I'd better get dinner ready.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Estelle, Joshua, would you like\x01",
            "to join us for dinner?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'll whip you up something delicious.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501FAh, today's not a good day...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Are you trying to say that...my\x01",
            "cooking isn't good any more?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004FHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You used to tell me how delicious\x01",
            "my cooking was when you were a\x01",
            "little girl, but now... *sniff*\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#004FI-It's not like that at all!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FI'm really sorry if we've upset you\x01",
            "in any way, but our dad's waiting\x01",
            "at home for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I see. I'm sure your father wants\x01",
            "you home for dinner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Poor Cassius would be all alone\x01",
            "in that house by himself.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D6D")

    Jump("loc_676D")

    label("loc_5D70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_60DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x55, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6032")
    OP_A2(0x2AB)

    ChrTalk(
        0xFE,
        "Hello there, Joshua and Estelle.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001FStella, listen to this!\x02\x03",
            "I finally became a bracer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My goodness, it that true?\x01",
            "And Joshua, too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FYes, ma'am. That's right.\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(500)

    ChrTalk(
        0xFE,
        (
            "Congratulations to the both of you!\x01",
            "You did wonderfully!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001FTee hee.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "But one thing, Estelle.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You shouldn't be proud just because\x01",
            "you became a bracer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "This is just the starting point.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002FI-I understand that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The two of you will experience a\x01",
            "lot of new things as bracers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And I hope that I can be proud of\x01",
            "the fact that this is the path you\x01",
            "chose in the coming years.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But enough about my feelings.\x01",
            "Please work hard and good luck!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_60DB")

    label("loc_6032")


    ChrTalk(
        0xFE,
        (
            "The two of you will experience a\x01",
            "lot of new things as bracers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And I hope that I can be proud of\x01",
            "the fact that this is the path you\x01",
            "chose in the coming years.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_60DB")

    Jump("loc_676D")

    label("loc_60DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_66C0")
    OP_A2(0x3)
    OP_A2(0x20F)

    ChrTalk(
        0x101,
        "#000FGood morning, Stella.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Oh my, well if it isn't Estelle\x01",
            "and Joshua?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Are you on your way to bracer\x01",
            "training?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 400)

    ChrTalk(
        0x101,
        (
            "#000FYeah, and just you watch.\x02\x03",
            "#502FI'm going to pass this exam and be\x01",
            "as good of a bracer as Schera, too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Hmm-hmm-hmm.\x01",
            "I'm looking forward to that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "By the way, Estelle...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008FWh-What? Why are you looking\x01",
            "at me like that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Did you wash your face?\x01",
            "How about your teeth?\x01",
            "Did you brush them, too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Joshua's so fastidious, but you always\x01",
            "forget to take care of yourself.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#008FCome on!\x01",
            "That was a long time ago.\x02\x03",
            "I don't do that anymore,\x01",
            "right, Joshua?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015FUmm, now that you mention it...\x02\x03",
            "#017FYou did take off from home the\x01",
            "other day with your hair all in\x01",
            "a mess, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#008FUgh...\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)
    TurnDirection(0x101, 0x102, 1000)

    ChrTalk(
        0x101,
        (
            "#008FThat was only because it was\x01",
            "an emergency!\x02\x03",
            "#008FMr. Rinon got the newest Strega-brand\x01",
            "sneakers in on that day...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#4SESTELLE!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#008FY-Yes!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xB, 800)

    ChrTalk(
        0xB,
        "You listen to me carefully!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "For a girl your age, you need\x01",
            "to take care of these things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If your appearance is messy, you\x01",
            "won't look like someone that people\x01",
            "can trust even if you are a bracer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Your appearance is a reflection\x01",
            "of what is on the inside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007FA-All right, I'll be more careful\x01",
            "from now on.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xB,
        (
            "Well, that's that. Now how about the\x01",
            "both of you get on over to the guild?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007F(Man, you just can't argue with her.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_676D")

    label("loc_66C0")


    ChrTalk(
        0xB,
        (
            "If your appearance is messy, you\x01",
            "won't look like someone that people\x01",
            "can trust even if you are a bracer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Your appearance is a reflection\x01",
            "of what is on the inside.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_676D")

    TalkEnd(0xB)
    Return()

    # Function_9_4C17 end

    def Function_10_6771(): pass

    label("Function_10_6771")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_69B8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_BB(0x0, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_BB(0x0, 0x5)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6852")
    OP_A2(0x29F)

    ChrTalk(
        0xC,
        (
            "#020FI see you've managed to open one\x01",
            "of your orbment slots, Estelle.\x02\x03",
            "Since your central slot is not limited\x01",
            "to a particular elemental, you are free\x01",
            "to install any type of quartz you like.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_69B8")

    label("loc_6852")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_BB(0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_BB(0x1, 0x5)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_691E")
    OP_A2(0x29F)

    ChrTalk(
        0xC,
        (
            "#020FGood work on opening up a slot,\x01",
            "Joshua.\x02\x03",
            "Since your central slot is limited to a certain\x01",
            "elemental, it would be best to increase your\x01",
            "orbment's number of open slots early on.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_69B8")

    label("loc_691E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53, 6)), scpexpr(EXPR_END)), "loc_69B8")

    ChrTalk(
        0xC,
        (
            "#020FIf you choose 'Slot' from the orbal factory\x01",
            "menu, you can open a new slot.\x02\x03",
            "Now decide which one of your\x01",
            "slots you're going to open.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xC)
    Return()

    label("loc_69B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_790F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_BA(0x0, 0x6E)"), scpexpr(EXPR_EXEC_OP, "OP_BA(0x1, 0xA)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_69D5")
    OP_A2(0x6)
    Jump("loc_6AA4")

    label("loc_69D5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_BA(0x0, 0x6E)"), scpexpr(EXPR_EXEC_OP, "OP_BA(0x1, 0x14)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_69EA")
    OP_A2(0x6)
    Jump("loc_6AA4")

    label("loc_69EA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_BA(0x0, 0x6E)"), scpexpr(EXPR_EXEC_OP, "OP_BA(0x1, 0x1E)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_69FF")
    OP_A2(0x6)
    Jump("loc_6AA4")

    label("loc_69FF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_BA(0x0, 0x6E)"), scpexpr(EXPR_EXEC_OP, "OP_BA(0x1, 0x32)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6A14")
    OP_A2(0x6)
    Jump("loc_6AA4")

    label("loc_6A14")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_BA(0x0, 0x6E)"), scpexpr(EXPR_EXEC_OP, "OP_BA(0x1, 0x41)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6A29")
    OP_A2(0x6)
    Jump("loc_6AA4")

    label("loc_6A29")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_BA(0x0, 0x6E)"), scpexpr(EXPR_EXEC_OP, "OP_BA(0x1, 0x6E)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6A3E")
    OP_A2(0x6)
    Jump("loc_6AA4")

    label("loc_6A3E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_BA(0x1, 0x6E)"), scpexpr(EXPR_EXEC_OP, "OP_BA(0x0, 0xA)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6A53")
    OP_A2(0x6)
    Jump("loc_6AA4")

    label("loc_6A53")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_BA(0x1, 0x6E)"), scpexpr(EXPR_EXEC_OP, "OP_BA(0x0, 0x14)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6A68")
    OP_A2(0x6)
    Jump("loc_6AA4")

    label("loc_6A68")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_BA(0x1, 0x6E)"), scpexpr(EXPR_EXEC_OP, "OP_BA(0x0, 0x1E)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6A7D")
    OP_A2(0x6)
    Jump("loc_6AA4")

    label("loc_6A7D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_BA(0x1, 0x6E)"), scpexpr(EXPR_EXEC_OP, "OP_BA(0x0, 0x32)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6A92")
    OP_A2(0x6)
    Jump("loc_6AA4")

    label("loc_6A92")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_BA(0x1, 0x6E)"), scpexpr(EXPR_EXEC_OP, "OP_BA(0x0, 0x41)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6AA4")
    OP_A2(0x6)

    label("loc_6AA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_774C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7146")
    OP_A2(0x29E)
    OP_A2(0x29D)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_6D0E")

    ChrTalk(
        0xC,
        (
            "#023FOh, so you've finished installing\x01",
            "your quartz, have you?\x02\x03",
            "#020FSince you have both recovery and attack arts\x01",
            "set up, it appears that you don't need any more\x01",
            "instruction from me about how to do this task.\x02\x03",
            "If you balance your arts out between each\x01",
            "other like you've done here, it should make\x01",
            "dealing with monsters much easier.\x02\x03",
            "Additionally, your Bracer Notebooks\x01",
            "contain information about which\x01",
            "quartz allow you to use which arts.\x02\x03",
            "If you'd like to use more powerful arts, check\x01",
            "out the arts and quartz charts in your Bracer\x01",
            "Notebooks and find something that works for you.\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 20)
    Jump("loc_7143")

    label("loc_6D0E")


    ChrTalk(
        0xC,
        (
            "#023FOh, so you've finished installing\x01",
            "your quartz, have you?\x02\x03",
            "#020FSince you have both recovery and attack arts\x01",
            "set up, it appears that you don't need any more\x01",
            "instruction from me about how to do this task.\x02\x03",
            "If you balance your arts out between each\x01",
            "other like you've done here, it should make\x01",
            "dealing with monsters much easier.\x02\x03",
            "Additionally, your Bracer Notebooks\x01",
            "contain information about which\x01",
            "quartz allow you to use which arts.\x02\x03",
            "If you'd like to use more powerful arts, check\x01",
            "out the arts and quartz charts in your Bracer\x01",
            "Notebooks and find something that works for you.\x02\x03",
            "All right, our training here is\x01",
            "almost finished.\x02\x03",
            "Last of all, I'm going to have\x01",
            "one of you open a new slot in\x01",
            "your orbments.\x02\x03",
            "The more slots you have available\x01",
            "to you, the broader range of choices\x01",
            "you'll have.\x02\x03",
            "Since EP, which is consumed by using arts, can\x01",
            "have its max value increased by opening up slots,\x01",
            "it would be a good idea to open them all early on.\x02\x03",
            "Now, I want you to use this sepith\x01",
            "and open a slot on each of your\x01",
            "orbments.\x02\x03",
            "Go ahead and decide which\x01",
            "slots you're going to open.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7143")

    Jump("loc_76D1")

    label("loc_7146")

    OP_A2(0x29E)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_731D")

    ChrTalk(
        0xC,
        (
            "#020FAll right, it looks like you've got both\x01",
            "recovery and attack arts set up.\x02\x03",
            "If you balance your arts out between each\x01",
            "other like you've done here, it should make\x01",
            "dealing with monsters much easier.\x02\x03",
            "Additionally, your Bracer Notebooks\x01",
            "contain information about which\x01",
            "quartz allow you to use which arts.\x02\x03",
            "If you'd like to use more powerful arts, check\x01",
            "out the arts and quartz charts in your Bracer\x01",
            "Notebooks and find something that works for you.\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 20)
    Jump("loc_76D1")

    label("loc_731D")


    ChrTalk(
        0xC,
        (
            "#020FAll right, it looks like you've got both\x01",
            "recovery and attack arts set up.\x02\x03",
            "If you balance your arts out between each\x01",
            "other like you've done here, it should make\x01",
            "dealing with monsters much easier.\x02\x03",
            "Additionally, your Bracer Notebooks\x01",
            "contain information about which\x01",
            "quartz allow you to use which arts.\x02\x03",
            "If you'd like to use more powerful arts, check\x01",
            "out the arts and quartz charts in your Bracer\x01",
            "Notebooks and find something that works for you.\x02\x03",
            "All right, our training here is\x01",
            "almost finished.\x02\x03",
            "Last of all, I'm going to have\x01",
            "one of you open a new slot in\x01",
            "your orbments.\x02\x03",
            "The more slots you have available\x01",
            "to you, the broader range of choices\x01",
            "you'll have.\x02\x03",
            "Since EP, which is consumed by using arts, can\x01",
            "have its max value increased by opening up slots,\x01",
            "it would be a good idea to open them all early on.\x02\x03",
            "Now, I want you to use this sepith\x01",
            "and open a slot on each of your\x01",
            "orbments.\x02\x03",
            "Go ahead and decide which\x01",
            "slots you're going to open.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_76D1")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Received several of each type\x01",
            "of elemental sepith.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_56(0x0)
    FadeToBright(300, 0)
    AddSepith(0x0, 0x1E)
    AddSepith(0x1, 0x1E)
    AddSepith(0x2, 0x1E)
    AddSepith(0x3, 0x1E)
    TalkEnd(0xC)
    Return()

    label("loc_774C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7757")
    Jump("loc_790F")

    label("loc_7757")


    ChrTalk(
        0xC,
        (
            "#020FNow install a quartz into your\x01",
            "orbments so that you can use\x01",
            "both recovery and attack arts.\x02\x03",
            "Look at your orbments and make\x01",
            "sure that recovery and attack arts\x01",
            "are divided up between them.\x02\x03",
            "You can figure this out by looking at the arts and\x01",
            "quartz charts in your Bracer Notebooks in order\x01",
            "to figure out which quartz you need to install.\x02\x03",
            "If you're lacking the necessary quartz,\x01",
            "then you can synthesize them at an\x01",
            "orbal factory.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xC)
    Return()

    label("loc_790F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7BA5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x273)"), scpexpr(EXPR_EXEC_OP, "OP_40(0x258)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x25E)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x261)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x26D)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7AB4")
    OP_A2(0x29D)

    ChrTalk(
        0xC,
        (
            "#020FAll right, it looks like you were\x01",
            "able to synthesize one.\x02\x03",
            "Next, I want you to increase the\x01",
            "arts you can use.\x02\x03",
            "Now install a quartz into your\x01",
            "orbments so that you can use\x01",
            "both recovery and attack arts.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "仸Quartz can be installed in the 'Orbment' screen. The 'Orbment' screen can\x01",
            "be utilized by selecting the 'Orbment' tab in the main menu.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xC)
    Return()

    label("loc_7AB4")


    ChrTalk(
        0xC,
        (
            "#020FNow, I want you to begin by first making\x01",
            "an elemental quartz that will work with\x01",
            "each of your particular orbments.\x02\x03",
            "In your case, Estelle, any elemental\x01",
            "quartz is okay but for you Joshua, it\x01",
            "has to be a time elemental quartz. \x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xC)
    Return()

    label("loc_7BA5")

    Call(0, 20)
    Return()

    # Function_10_6771 end

    def Function_11_7BAA(): pass

    label("Function_11_7BAA")

    TalkBegin(0xD)

    NpcTalk(
        0xD,
        "Girl With Glasses",
        "#0151FW-Wow! How cute is this?!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xD)
    Return()

    # Function_11_7BAA end

    def Function_12_7BE8(): pass

    label("Function_12_7BE8")

    OP_8F(0x101, 0xFFFF63D3, 0x0, 0xFFFFED2B, 0xBB8, 0x0)
    OP_8C(0x101, 0, 0)
    OP_8F(0x101, 0xFFFF66E7, 0x0, 0xFFFFE49E, 0xBB8, 0x0)
    Return()

    # Function_12_7BE8 end

    def Function_13_7C18(): pass

    label("Function_13_7C18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7CC3")
    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_69(0xC, 0x320)

    def lambda_7C38():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_7C38)

    def lambda_7C46():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_7C46)

    ChrTalk(
        0xC,
        (
            "#024FAnd just where do you think you're\x01",
            "going? We aren't finished with\x01",
            "training yet.\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_7CC3")

    Return()

    # Function_13_7C18 end

    def Function_14_7CC4(): pass

    label("Function_14_7CC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7D6F")
    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_69(0xC, 0x320)

    def lambda_7CE4():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_7CE4)

    def lambda_7CF2():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_7CF2)

    ChrTalk(
        0xC,
        (
            "#024FAnd just where do you think you're\x01",
            "going? We aren't finished with\x01",
            "training yet.\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_7D6F")

    Return()

    # Function_14_7CC4 end

    def Function_15_7D70(): pass

    label("Function_15_7D70")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xC, 0x8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_BB(0x0, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_BB(0x0, 0x5)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7D97")
    OP_A2(0x29F)
    OP_A2(0x7)
    Jump("loc_7DAA")

    label("loc_7D97")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_BB(0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_BB(0x1, 0x5)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7DAA")
    OP_A2(0x29F)
    OP_A2(0x7)

    label("loc_7DAA")

    SetChrPos(0xC, -41600, 0, -1337, 270)
    SetChrPos(0x101, -43651, 0, -651, 90)
    SetChrPos(0x102, -43651, 0, -2165, 90)
    OP_6D(-43106, 0, -929, 0)
    OP_0D()
    Sleep(2000)

    ChrTalk(
        0xC,
        (
            "#020FHere is where you will learn how\x01",
            "to use an orbal factory's services.\x02\x03",
            "#020FAt an orbal factory, you can modify\x01",
            "your orbments and synthesize support\x01",
            "quartz in order to use orbal arts.\x02\x03",
            "#020FArts have a wide range of effects and\x01",
            "if mastered, can be extremely helpful.\x02\x03",
            "#020FThe bracer business is a pretty risky occupation,\x01",
            "so the guild has had a long-standing relationship\x01",
            "with these orbal factories.\x02\x03",
            "#020FAnyway, this is about as much as\x01",
            "I can explain.\x02\x03",
            "#020FI'll leave the technical details to\x01",
            "the expert.\x02\x03",
            "#020F...So, Mr. Melders, if you wouldn't\x01",
            "mind taking over from here?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8046():

        label("loc_8046")

        TurnDirection(0xC, 0x0, 0)
        OP_48()
        Jump("loc_8046")

    QueueWorkItem2(0xC, 1, lambda_8046)
    OP_4A(0x9, 0)
    OP_6D(-41136, 0, -889, 800)

    ChrTalk(
        0x9,
        (
            "No problem.\x01",
            "Leave everything to me.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8095():
        OP_69(0x9, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_8095)

    def lambda_80A3():
        OP_8E(0x102, 0xFFFF5D77, 0x0, 0xFFFFFE70, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_80A3)
    OP_8E(0x101, 0xFFFF5D77, 0x0, 0x1A7, 0xBB8, 0x0)
    OP_8C(0x101, 90, 400)
    OP_8C(0x102, 90, 400)

    label("loc_80DA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8DE6")

    ChrTalk(
        0x9,
        (
            "So, what is it that you would\x01",
            "like to know about?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_8176")

    Menu(
        0,
        10,
        100,
        0,
        (
            "[Orbments]\x01",        # 0
            "[Orbal Arts]\x01",      # 1
            "[Quartz]\x01",          # 2
            "[Sepith]\x01",          # 3
            "[Leave]\x01",           # 4
        )
    )

    Jump("loc_81A9")

    label("loc_8176")


    Menu(
        0,
        10,
        100,
        0,
        (
            "[Orbments]\x01",        # 0
            "[Orbal Arts]\x01",      # 1
            "[Quartz]\x01",          # 2
            "[Sepith]\x01",          # 3
        )
    )


    label("loc_81A9")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_A2(0x5)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_81E3"),
        (1, "loc_85EC"),
        (2, "loc_8A02"),
        (3, "loc_8C34"),
        (4, "loc_8DD1"),
        (SWITCH_DEFAULT, "loc_8DE1"),
    )


    label("loc_81E3")


    ChrTalk(
        0x9,
        (
            "Orbments are mechanical devices which\x01",
            "exhibit an array of effects through the\x01",
            "installation of various types of quartz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "By definition, that means that\x01",
            "lights, airship engines and so\x01",
            "on, are also types of orbments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "However, the ones we will be discussing today are\x01",
            "battle orbments, which \x07\x04",
            "enhance the user's physical\x01",
            "abilities and make it possible to use magic\x07\x00",
            ".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Since each orbment is adjusted to match the\x01",
            "owner's personal aptitude, the structures for\x01",
            "these devices also \x07\x04",
            "differ for each owner\x07\x00",
            ".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Simply put, the shape of the fixed elemental\x01",
            "slots and lines which connect them vary.\x01",
            "At any rate, that's the layman's explanation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "In order to install quartz,\x01",
            "you must first have an open slot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "By default, the central slot is open, but the\x01",
            "other slots must be opened at an orbal factory\x01",
            "like this. It'll take a fair amount of sepith too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "EP, which is needed for magic, will also see a \x07\x04",
            "max\x01",
            "increase according to the number of open slots\x07\x00",
            ".\x01",
            "I recommend opening them all as soon as possible.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8DE1")

    label("loc_85EC")


    ChrTalk(
        0x9,
        (
            "Simply put, orbal arts are magic which\x01",
            "can be discharged exclusively through\x01",
            "the use of battle orbments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "In other words, a number of peculiar effects\x01",
            "can be produced by using the orbal energy\x01",
            "stored within these mechanical devices.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Since 'orbal arts' can be a mouthful, they are\x01",
            "almost universally referred to as 'arts'. Probably\x01",
            "ought to have been called that from the get-go...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "There are several types of arts, but in order to be\x01",
            "able to use them, their corresponding quartz must\x01",
            "first be synthesized at an orbal factory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Orbments are also set up so that once a\x01",
            "particular quartz is installed into a slot,\x01",
            "the owner will be able to use those arts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The type of arts one can use also changes\x01",
            "depending on \x07\x04",
            "the elemental value and the\x01",
            "combination of installed quartz\x07\x00",
            ".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Basically, if you want to use water arts,\x01",
            "all you have to do is install quartz with\x01",
            "a water elemental value.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "In reality, orbments are much more complex\x01",
            "than what I have described, but I think this\x01",
            "information should suffice for now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8DE1")

    label("loc_8A02")


    ChrTalk(
        0x9,
        (
            "Quartz are circuits made\x01",
            "from sepith.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Quartz have a vast number of effects and \x07\x04",
            "raise\x01",
            "the owner's abilities\x07\x00",
            " while simultaneously\x01",
            "making it \x07\x04",
            "possible for them to use arts\x07\x00",
            ".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "However, you will not be able to harness\x01",
            "any of these effects until quartz has\x01",
            "been installed into a slot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "However, \x07\x04",
            "there are also fixed slots\x01",
            "in which only a certain type of\x01",
            "elemental quartz can be installed\x07\x00",
            ".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "This being the case, when you synthesize a new\x01",
            "quartz, be sure to check your orbment and decide\x01",
            "where you will be installing it ahead of time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8DE1")

    label("loc_8C34")


    ChrTalk(
        0x9,
        (
            "Sepith are fragments of septium\x01",
            "which are dropped by monsters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "They are divided into 7 types: Earth (brown),\x01",
            "Water (blue), Fire (red), Wind (green),\x01",
            "Time (black), Space (gold), and Mirage (silver).\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x4),
            "Sepith can be exchanged\x01",
            "for mira\x07\x00",
            " almost anywhere,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...at the orbal factory, it can be used to\x01",
            "synthesize quartz and to open orbment slots\x01",
            "in which to install the synthesized quartz.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8DE1")

    label("loc_8DD1")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jump("loc_8DE1")

    label("loc_8DE1")

    OP_56(0x0)
    Jump("loc_80DA")

    label("loc_8DE6")


    def lambda_8DEC():
        TurnDirection(0x0, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_8DEC)

    def lambda_8DFA():
        TurnDirection(0x1, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_8DFA)
    OP_69(0xC, 0x3E8)

    ChrTalk(
        0xC,
        (
            "#020FIt looks like Mr. Melders has\x01",
            "answered all your questions.\x02\x03",
            "If there's nothing else, then\x01",
            "let's have you both try and\x01",
            "use the services here.\x02\x03",
            "For that, you're going to need\x01",
            "some sepith.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Received several of each type\x01",
            "of elemental sepith.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_56(0x0)
    FadeToBright(300, 0)
    AddSepith(0x0, 0x14)
    AddSepith(0x1, 0x14)
    AddSepith(0x2, 0x14)
    AddSepith(0x3, 0x14)
    AddSepith(0x4, 0x14)
    AddSepith(0x5, 0x14)
    AddSepith(0x6, 0x14)

    ChrTalk(
        0xC,
        (
            "#020FWith that amount, you two should be\x01",
            "able to synthesize a few quartz.\x02\x03",
            "Now, I want you to begin by first making\x01",
            "an elemental quartz that will work with\x01",
            "each of your particular orbments.\x02\x03",
            "In your case, Estelle, any elemental\x01",
            "quartz is okay, but for you Joshua, it\x01",
            "has to be a time elemental quartz.\x02\x03",
            "Normally at a shop you would be able to exchange\x01",
            "sepith for mira, but for this training you will\x01",
            "not be able to use this service.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "仸Upon approaching the counter, a TALK mark will appear. Pressing the OK\x01",
            "button will display a list of options. Select 'Modify' or 'Trade' to use the\x01",
            "orbal factory's services.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    EventEnd(0x0)
    OP_4B(0x9, 0)
    Return()

    # Function_15_7D70 end

    def Function_16_91D4(): pass

    label("Function_16_91D4")

    OP_A2(0x253)
    OP_28(0x19, 0x1, 0x40)
    EventBegin(0x0)
    AddParty(0xF, 0xFF)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9224")
    SetChrPos(0x101, -42590, 0, 1660, 135)
    SetChrPos(0x102, -43440, 0, 1640, 135)
    SetChrPos(0x2, -42910, 0, 520, 135)
    Jump("loc_9257")

    label("loc_9224")

    SetChrPos(0x101, -38220, 0, -5030, 0)
    SetChrPos(0x102, -39380, 0, -5260, 0)
    SetChrPos(0x2, -38890, 0, -4019, 0)

    label("loc_9257")

    SetChrPos(0x3, -38530, 0, -2400, 0)
    OP_4A(0x8, 0)
    TurnDirection(0x8, 0x3, 0)
    ClearMapFlags(0x1)
    OP_51(0xE, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x3, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x3, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x3, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(2000, 0)
    OP_69(0xE, 0x7D0)
    OP_0D()
    OP_62(0x3, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    NpcTalk(
        0x3,
        "Girl With Glasses",
        (
            "#152FWait, anything but that!\x02\x03",
            "#152FI'll do anything you ask, just\x01",
            "please give me back my camera!\x02\x03",
            "#152FIt's worth more to me than my life!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "This is a problem...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 400)

    ChrTalk(
        0x8,
        "What should I do about this, Dad?\x02",
    )

    CloseMessageWindow()
    OP_4A(0x9, 0)
    TurnDirection(0x9, 0x8, 400)

    ChrTalk(
        0x9,
        (
            "You're the one who took the job,\x01",
            "so you're the one who has to deal\x01",
            "with it.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x9, 270, 400)
    OP_4B(0x9, 0)
    TurnDirection(0x8, 0x3, 400)
    OP_51(0xE, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x3, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x3, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x3, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0xE, 0x320)

    ChrTalk(
        0x101,
        "#004FHmm? What's all the fuss about?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F#6PCould this person be...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2,
        "#145FThat's her, all right...\x02",
    )

    CloseMessageWindow()
    OP_43(0xE, 0x1, 0x0, 0x11)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_952A")
    OP_8E(0x2, 0xFFFF5CF9, 0x0, 0xFFFFF6A0, 0xBB8, 0x0)
    OP_8E(0x2, 0xFFFF6582, 0x0, 0xFFFFF6A0, 0xBB8, 0x0)
    Jump("loc_953E")

    label("loc_952A")

    OP_8E(0x2, 0xFFFF6582, 0x0, 0xFFFFF6A0, 0x7D0, 0x0)

    label("loc_953E")

    TurnDirection(0x2, 0x3, 400)

    ChrTalk(
        0x2,
        (
            "#144F#3PHey, Dorothy!\x01",
            "How long are you going\x01",
            "to keep me waiting?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x3, 0x2, 400)
    TurnDirection(0x8, 0x2, 400)

    ChrTalk(
        0x3,
        (
            "#153F#4PNial!\x01",
            "You came just at the right time!\x02\x03",
            "#152FPlease help me out here!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2,
        (
            "#142F#3PWhat did you do this time?\x02\x03",
            "#142FYou didn't waste all your money\x01",
            "so now you don't have enough for\x01",
            "repairs, did you?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x3,
        (
            "#153F#4PThat's amazing!\x01",
            "How did you guess?\x02\x03",
            "#153FAre you like a clairvoyant or\x01",
            "something?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2,
        (
            "#144F#3PWhen you do the same thing that\x01",
            "many times, even an idiot would\x01",
            "know what's going on!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Do you know this person?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm sorry to ask this, but can\x01",
            "I get you to pay the repair\x01",
            "costs?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x2, 0x8, 400)

    ChrTalk(
        0x2,
        (
            "#145F#3PFine...but I'll need you to write\x01",
            "it off as a business expense.\x02\x03",
            "#145FHow much?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Let's see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The decorative clock and the\x01",
            "repairs together are 2000 mira.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x2, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x2,
        (
            "#144F#3PHold on!\x02\x03",
            "#144FI can understand the repairs,\x01",
            "but what's the deal with the\x01",
            "decorative clock?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x3,
        (
            "#151F#4PWell, I was looking around the\x01",
            "store while he was doing the\x01",
            "repairs and...\x02\x03",
            "#151FI saw a pretty clock and when\x01",
            "I picked it up, it broke...\x02\x03",
            "#151FBut I'm glad we can write it\x01",
            "off as a business expense.\x01",
            "How wonderful is that?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x2, 0x3, 400)

    ChrTalk(
        0x2,
        (
            "#144F#3PThat kind of amount is not going\x01",
            "to be covered!\x02\x03",
            "#145FCrap... It looks like I'm going to\x01",
            "have to pay out of my own pocket\x01",
            "and get my money back later.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x2, 0x8, 400)

    ChrTalk(
        0x2,
        "#142F#3PHere's your 2000 mira.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "And this is your receipt.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9B0C")
    OP_6D(-42770, 0, 1380, 1500)
    Jump("loc_9B1D")

    label("loc_9B0C")

    OP_6D(-38130, 0, -4670, 1500)

    label("loc_9B1D")


    ChrTalk(
        0x101,
        (
            "#008F(This is an unbelievably awkward\x01",
            "combination if I've ever seen one.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#6P(No doubt about that...)\x02\x03",
            "#010F(But the fact that he'll pay out of\x01",
            "his pocket for someone means he's\x01",
            "probably pretty nice to work under.)\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x3, 0xFF)
    OP_43(0x2, 0x1, 0x0, 0x12)
    Sleep(500)
    OP_8C(0x8, 180, 400)
    OP_4B(0x8, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9C5C")
    OP_8E(0x3, 0xFFFF5D62, 0x0, 0xFFFFF66E, 0xBB8, 0x0)
    OP_8E(0x3, 0xFFFF58F8, 0x0, 0xFFFFFD26, 0xBB8, 0x0)
    OP_8C(0x3, 0, 400)
    Jump("loc_9C77")

    label("loc_9C5C")

    OP_8C(0x3, 180, 400)
    OP_8E(0x3, 0xFFFF699C, 0x0, 0xFFFFF164, 0x7D0, 0x0)

    label("loc_9C77")


    ChrTalk(
        0x2,
        (
            "#145F#6PSorry to keep you waiting, kids.\x01",
            "Had to take care of a little trouble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x3,
        "#150F#6PWho are these kids, Nial?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2,
        (
            "#140F#6PThey're the bracers who will be\x01",
            "acting as our escorts and guides.\x02\x03",
            "#140FThey'll be taking the place of\x01",
            "Cassius Bright, with whom we'd\x01",
            "originally made arrangements.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x3,
        "#153F#6PThese young kids are...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FI'm Estelle.\x01",
            "It's nice to meet you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F#6PAnd I'm Joshua.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x3,
        (
            "#151F#6PSo it's Estelle and Joshua, is it?\x01",
            "You may be young, but you seem\x01",
            "reliable.\x02\x03",
            "#151FI'm Dorothy Hyatt.\x02\x03",
            "#151FI'm the new camerawoman\x01",
            "for the Liberl News.\x02\x03",
            "#151FAt the moment, I'm training\x01",
            "under Nial.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2,
        (
            "#145F#6PWhy'd I get stuck babysitting\x01",
            "this blockhead of a girl...\x02\x03",
            "#145FThat damn Editor-in-Chief...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x3,
        (
            "#151F#6PRelax, relax. Something good will\x01",
            "come out of all of this soon enough.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x2, 0x3, 400)

    ChrTalk(
        0x2,
        (
            "#144F#6PYou're one to talk!\x02\x03",
            "#145FNever mind, just forget it...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x2, 0x102, 400)

    ChrTalk(
        0x2,
        (
            "#140F#6PNow that we've got everyone\x01",
            "together, how about we go and\x01",
            "get our story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#6POur destination is the Esmelas\x01",
            "Tower, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001FAll right, let's go!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x3,
        "#151F#6PRight on!\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_16_91D4 end

    def Function_17_A0C1(): pass

    label("Function_17_A0C1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A0E1")
    OP_6D(-39730, 0, -1830, 2000)
    Jump("loc_A0F2")

    label("loc_A0E1")

    OP_6D(-37205, 0, -2234, 2000)

    label("loc_A0F2")

    Return()

    # Function_17_A0C1 end

    def Function_18_A0F3(): pass

    label("Function_18_A0F3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A13F")
    OP_8E(0x2, 0xFFFF5D62, 0x0, 0xFFFFF66E, 0xBB8, 0x0)
    OP_8E(0x2, 0xFFFF55D8, 0x0, 0x1E, 0xBB8, 0x0)
    OP_8C(0x2, 0, 400)
    OP_8C(0x101, 180, 400)
    OP_8C(0x102, 180, 400)
    Jump("loc_A15A")

    label("loc_A13F")

    OP_8C(0x2, 180, 400)
    OP_8E(0x2, 0xFFFF65F0, 0x0, 0xFFFFF092, 0x7D0, 0x0)

    label("loc_A15A")

    Return()

    # Function_18_A0F3 end

    def Function_19_A15B(): pass

    label("Function_19_A15B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A176")
    TurnDirection(0x3, 0x2, 0)
    TurnDirection(0x8, 0x2, 0)
    OP_48()
    Jump("Function_19_A15B")

    label("loc_A176")

    Return()

    # Function_19_A15B end

    def Function_20_A177(): pass

    label("Function_20_A177")

    Sleep(100)
    Fade(1000)
    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_44(0xC, 0x1)
    OP_8C(0xC, 270, 0)
    SetChrPos(0x101, -42760, 0, -2149, 45)
    SetChrPos(0x102, -42760, 0, -936, 135)
    OP_6D(-42964, 0, -712, 0)
    OP_0D()

    ChrTalk(
        0xC,
        (
            "#020FThis concludes your training here\x01",
            "at the orbal factory.\x02\x03",
            "Now it's time to move on to what\x01",
            "you've both been waiting for:\x01",
            "the qualification test.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#004F...Pardon?\x02\x03",
            "#004FD-Did you just say, 'test'?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 400)

    def lambda_A2C1():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A2C1)

    ChrTalk(
        0x102,
        (
            "#018FYou can't honestly tell me that\x01",
            "you forgot about the test...again,\x01",
            "can you?\x02\x03",
            "Didn't I remind you just this\x01",
            "morning?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008FAh...ha...ha...\x02\x03",
            "Now that you mention it, I vaguely\x01",
            "remember some sort of talk along\x01",
            "those lines at the breakfast table...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A3D2():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A3D2)

    ChrTalk(
        0xC,
        (
            "#025F...Sometimes I fear for the future of\x01",
            "the Bracer Guild...and humanity...\x02\x03",
            "#020FOh well, no sense in worrying\x01",
            "about that now. Let's head over\x01",
            "to the testing area.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(
        0x101,
        (
            "#004FY-You mean like...now?!\x02\x03",
            "#004FI don't know if I'm ready for...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#024FHow about a little less yapping\x01",
            "and a little more walking?\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0xC, 0xFF)
    OP_8E(0xC, 0xFFFF5AF3, 0x0, 0xFFFFF60B, 0xBB8, 0x0)
    TurnDirection(0x102, 0x101, 0)
    OP_8C(0xC, 315, 400)
    OP_8C(0x101, 315, 1000)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_43(0x101, 0x1, 0x0, 0xC)
    OP_8E(0xC, 0xFFFF63D3, 0x0, 0xFFFFED2B, 0xBB8, 0x0)
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_8E(0xC, 0xFFFF66E7, 0x0, 0xFFFFE49E, 0xBB8, 0x0)
    Sleep(200)
    OP_9F(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0xBE)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0xC8)
    Sleep(300)

    ChrTalk(
        0x101,
        "#003FJoshuuua, heeelp meeee...\x02",
    )

    CloseMessageWindow()
    Sleep(800)
    OP_63(0x102)
    Sleep(100)
    TurnDirection(0x102, 0x8, 400)

    ChrTalk(
        0x102,
        (
            "#010FMr. Melders, Freddy, thank you\x01",
            "for all your help.\x02",
        )
    )

    CloseMessageWindow()
    OP_4A(0x9, 0)
    TurnDirection(0x9, 0x102, 400)

    ChrTalk(
        0x9,
        (
            "Don't mention it. And good luck\x01",
            "with that test of yours.\x02",
        )
    )

    CloseMessageWindow()
    OP_4A(0x8, 0)
    TurnDirection(0x8, 0x102, 400)

    ChrTalk(
        0x8,
        "We'll be rooting for you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009FI'm going to remember that you\x01",
            "left me high and dry like this,\x01",
            "Joshuaaa!\x02",
        )
    )

    CloseMessageWindow()
    NewScene("ED6_DT01/T0100   ._SN", 2, 0, 0)
    IdleLoop()
    Return()

    # Function_20_A177 end

    SaveToFile()

Try(main)
