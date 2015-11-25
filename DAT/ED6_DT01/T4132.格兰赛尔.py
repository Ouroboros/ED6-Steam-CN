from ED6ScenarioHelper import *

def main():
    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4132   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4132.x',
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
        'Nial',                                 # 9
        'Kurt',                                 # 10
        'Fritz',                                # 11
        'Jill',                                 # 12
        'Hans',                                 # 13
        'Kloe',                                 # 14
        'Miele',                                # 15
        'Dean Collins',                         # 16
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
        'ED6_DT07/CH02060 ._CH',             # 00
        'ED6_DT07/CH01620 ._CH',             # 01
        'ED6_DT07/CH00175 ._CH',             # 02
        'ED6_DT07/CH00176 ._CH',             # 03
        'ED6_DT06/CH20041 ._CH',             # 04
        'ED6_DT06/CH20047 ._CH',             # 05
        'ED6_DT07/CH01220 ._CH',             # 06
        'ED6_DT07/CH02390 ._CH',             # 07
        'ED6_DT07/CH02550 ._CH',             # 08
        'ED6_DT07/CH00040 ._CH',             # 09
        'ED6_DT07/CH01040 ._CH',             # 0A
        'ED6_DT07/CH02600 ._CH',             # 0B
    )

    AddCharChipPat(
        'ED6_DT07/CH02060P._CP',             # 00
        'ED6_DT07/CH01620P._CP',             # 01
        'ED6_DT07/CH00175P._CP',             # 02
        'ED6_DT07/CH00176P._CP',             # 03
        'ED6_DT06/CH20041P._CP',             # 04
        'ED6_DT06/CH20047P._CP',             # 05
        'ED6_DT07/CH01220P._CP',             # 06
        'ED6_DT07/CH02390P._CP',             # 07
        'ED6_DT07/CH02550P._CP',             # 08
        'ED6_DT07/CH00040P._CP',             # 09
        'ED6_DT07/CH01040P._CP',             # 0A
        'ED6_DT07/CH02600P._CP',             # 0B
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 6940,
        Z                   = 0,
        Y                   = 3300,
        Direction           = 166,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 6140,
        Z                   = 0,
        Y                   = -1760,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 7770,
        Z                   = 0,
        Y                   = -1720,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 6920,
        Z                   = 0,
        Y                   = -260,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 36400,
        Z                   = 0,
        Y                   = 50700,
        Direction           = 106,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 4320,
        Z                   = 0,
        Y                   = 1060,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )


    DeclActor(
        TriggerX            = 7060,
        TriggerZ            = 0,
        TriggerY            = 1700,
        TriggerRange        = 800,
        ActorX              = 6940,
        ActorZ              = 1500,
        ActorY              = 3300,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
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
        TalkFunctionIndex   = 17,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_252",          # 00, 0
        "Function_1_3A0",          # 01, 1
        "Function_2_3ED",          # 02, 2
        "Function_3_403",          # 03, 3
        "Function_4_427",          # 04, 4
        "Function_5_4E5",          # 05, 5
        "Function_6_838",          # 06, 6
        "Function_7_B47",          # 07, 7
        "Function_8_CA2",          # 08, 8
        "Function_9_D23",          # 09, 9
        "Function_10_D28",         # 0A, 10
        "Function_11_19BE",        # 0B, 11
        "Function_12_1E23",        # 0C, 12
        "Function_13_25F5",        # 0D, 13
        "Function_14_2CD6",        # 0E, 14
        "Function_15_314C",        # 0F, 15
        "Function_16_35E1",        # 10, 16
        "Function_17_4BF4",        # 11, 17
    )


    def Function_0_252(): pass

    label("Function_0_252")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_269")
    OP_A3(0x3FA)
    Event(0, 12)
    OP_B1("t4132_n")

    label("loc_269")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_280")
    OP_A3(0x3FB)
    Event(0, 14)
    OP_B1("t4132_n")

    label("loc_280")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 4)), scpexpr(EXPR_END)), "loc_2A0")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3FC)
    Event(0, 15)
    OP_B1("t4132_n")

    label("loc_2A0")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_2B0"),
        (120, "loc_2CB"),
        (SWITCH_DEFAULT, "loc_2E1"),
    )


    label("loc_2B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2C8")
    SetMapFlags(0x10000000)
    OP_A2(0x620)
    Event(0, 13)

    label("loc_2C8")

    Jump("loc_2E1")

    label("loc_2CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2DE")
    OP_A2(0x64D)
    Event(0, 16)

    label("loc_2DE")

    Jump("loc_2E1")

    label("loc_2E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_2FF")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xF, 0x80)
    Jump("loc_39F")

    label("loc_2FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_30E")
    ClearChrFlags(0xE, 0x80)
    Jump("loc_39F")

    label("loc_30E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_318")
    Jump("loc_39F")

    label("loc_318")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_322")
    Jump("loc_39F")

    label("loc_322")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_32C")
    Jump("loc_39F")

    label("loc_32C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_353")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 32009, 0, 115490, 0)
    OP_43(0x9, 0x0, 0x0, 0x2)
    Jump("loc_39F")

    label("loc_353")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_35D")
    Jump("loc_39F")

    label("loc_35D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_384")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 32009, 0, 115490, 0)
    OP_43(0x9, 0x0, 0x0, 0x2)
    Jump("loc_39F")

    label("loc_384")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_38E")
    Jump("loc_39F")

    label("loc_38E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_398")
    Jump("loc_39F")

    label("loc_398")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_39F")

    label("loc_39F")

    Return()

    # Function_0_252 end

    def Function_1_3A0(): pass

    label("Function_1_3A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3D3")
    OP_B1("t4132_y")
    Jump("loc_3DC")

    label("loc_3D3")

    OP_B1("t4132_n")

    label("loc_3DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 2)), scpexpr(EXPR_END)), "loc_3EC")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x4B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3EC")

    Return()

    # Function_1_3A0 end

    def Function_2_3ED(): pass

    label("Function_2_3ED")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_402")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_3ED")

    label("loc_402")

    Return()

    # Function_2_3ED end

    def Function_3_403(): pass

    label("Function_3_403")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_426")
    OP_8D(0xFE, 153520, 48510, 156020, 53700, 3000)
    Jump("Function_3_403")

    label("loc_426")

    Return()

    # Function_3_403 end

    def Function_4_427(): pass

    label("Function_4_427")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I decided to splurge a little, and\x01",
            "spend the Birthday Celebration in\x01",
            "style at a nice hotel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And what a hotel! This place\x01",
            "is just incredible. Biggest\x01",
            "in the kingdom, indeed!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_4_427 end

    def Function_5_4E5(): pass

    label("Function_5_4E5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_52C")

    ChrTalk(
        0xD,
        (
            "#040FEstelle! Joshua!\x02\x03",
            "I'm so glad to see you again!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_834")

    label("loc_52C")

    OP_A2(0x4)
    OP_A2(0x6F2)

    ChrTalk(
        0xD,
        "#040FEstelle! Joshua!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000FOh, Kloe! There you are!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#045FYeah, I'd heard that Jill and\x01",
            "Hans were here...\x02\x03",
            "So I sneaked out of the castle\x01",
            "and came to see them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001FHa ha ha, you sure do know how\x01",
            "to act un-princess-ey!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#041FBut of course! Heh heh. And I\x01",
            "wanted to thank you, too.\x02\x03",
            "You've been nothing but helpful\x01",
            "at every turn.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505FUs? Nah, it's totally all you!\x01",
            "We've learned a whole bunch just\x01",
            "from being around you!\x02\x03",
            "You've taught us all about kindness,\x01",
            "and courtesy, and strength of spirit,\x01",
            "and all that other junk!\x02\x03",
            "#008F...Not that it's actually junk...\x01",
            "Ahhh, I'm so bad at this!\x02\x03",
            "#006FWhat I'm trying to say is, that's\x01",
            "what friends do. So believe me,\x01",
            "no thanks are necessary!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#044FEstelle...\x02\x03",
            "#048FI'm so glad to see you again!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_834")

    TalkEnd(0xFE)
    Return()

    # Function_5_4E5 end

    def Function_6_838(): pass

    label("Function_6_838")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_8EA")

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
    Jump("loc_B43")

    label("loc_8EA")

    OP_A2(0x3)
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(
        0xFE,
        "#730FHey, Joshua!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014FHans!\x02\x03",
            "What brings you here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#734FWhat brings me here? What brings me\x01",
            "here?! All this time, and that's the\x01",
            "first question out of your mouth?!\x02\x03",
            "#730FDo you know how lonely all my\x01",
            "nights have been? Do you?!\x02\x03",
            "#731FI never forgot you, Joshua! I came running\x01",
            "all this way to the capital to see you!\x01",
            "But...where's the princess outfit?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#019F...Still the same as ever, I see.\x02",
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

    label("loc_B43")

    TalkEnd(0xFE)
    Return()

    # Function_6_838 end

    def Function_7_B47(): pass

    label("Function_7_B47")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_BCE")

    ChrTalk(
        0xFE,
        (
            "#640FI heard about your adventures from\x01",
            "Kloe. Sounds like you guys have\x01",
            "been busy.\x02\x03",
            "#648FRuby Knight Julius, indeed!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C9E")

    label("loc_BCE")

    OP_A2(0x2)

    ChrTalk(
        0xFE,
        "#640FEstelle! Joshua!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004FJill?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#641FLong time no see!\x02\x03",
            "I heard about your adventures from\x01",
            "Kloe. Sounds like you guys have\x01",
            "been busy.\x02\x03",
            "#648FRuby Knight Julius, indeed!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#008FHa ha ha!\x02",
    )

    CloseMessageWindow()

    label("loc_C9E")

    TalkEnd(0xFE)
    Return()

    # Function_7_B47 end

    def Function_8_CA2(): pass

    label("Function_8_CA2")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "#780FOho! Nice to see you. It's been\x01",
            "a long time!\x02\x03",
            "Jill and Hans have come to the capital\x01",
            "as school representatives.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_CA2 end

    def Function_9_D23(): pass

    label("Function_9_D23")

    Call(0, 10)
    Return()

    # Function_9_D23 end

    def Function_10_D28(): pass

    label("Function_10_D28")

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
            "Rest\x01",       # 1
            "Leave\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D88")
    OP_0D()
    OP_A9(0x5F)
    OP_56(0x0)
    TalkEnd(0xA)
    Return()

    label("loc_D88")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D99")
    TalkEnd(0xA)
    Return()

    label("loc_D99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_E76")

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
    Jump("loc_19BA")

    label("loc_E76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_F50")

    ChrTalk(
        0xA,
        (
            "It would seem that the regular\x01",
            "guards have been replaced by\x01",
            "those soldiers in black.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Considering how close it is to the time\x01",
            "of the Birthday Celebration, there seems\x01",
            "to be an awful lot of unrest...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19BA")

    label("loc_F50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 5)), scpexpr(EXPR_END)), "loc_FA1")

    ChrTalk(
        0xA,
        "Seems Kurt's gone out...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Does that mean he's feeling better?\x02",
    )

    CloseMessageWindow()
    Jump("loc_19BA")

    label("loc_FA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_1086")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_100B")

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
    Jump("loc_1083")

    label("loc_100B")

    OP_A2(0x1)

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

    label("loc_1083")

    Jump("loc_19BA")

    label("loc_1086")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_12B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1115")

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
    Jump("loc_12AE")

    label("loc_1115")

    OP_A2(0x1)

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

    label("loc_12AE")

    Jump("loc_19BA")

    label("loc_12B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1376")

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
        (
            "Please do take care out there.\x01",
            "You may rest assured that I will\x01",
            "be cheering for you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19BA")

    label("loc_1376")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_14FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1425")

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
    Jump("loc_14FA")

    label("loc_1425")

    OP_A2(0x1)

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

    label("loc_14FA")

    Jump("loc_19BA")

    label("loc_14FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_1577")

    ChrTalk(
        0xA,
        "How was the room? Did you sleep well?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Today's the second day, right?\x01",
            "Best of luck out there, bracers!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19BA")

    label("loc_1577")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_16AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_15FE")

    ChrTalk(
        0xA,
        (
            "...Come to think of it, there are\x01",
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
    Jump("loc_16AB")

    label("loc_15FE")

    OP_A2(0x1)

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
            "...Come to think of it, there are\x01",
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

    label("loc_16AB")

    Jump("loc_19BA")

    label("loc_16AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_1715")

    ChrTalk(
        0xA,
        (
            "You are all participants in the\x01",
            "tournament, then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "My, my! Best of luck to you all!\x02",
    )

    CloseMessageWindow()
    Jump("loc_19BA")

    label("loc_1715")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_1910")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_END)), "loc_17A7")

    ChrTalk(
        0xA,
        (
            "Your room is on the corner at\x01",
            "the top of the stairs. Room 205.\x02",
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
    Jump("loc_190D")

    label("loc_17A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_181B")

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
    Jump("loc_190D")

    label("loc_181B")

    OP_A2(0x1)

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
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010FWe can leave the checking in\x01",
            "for later, then. For now, we\x01",
            "should go find Zane.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#001FSounds like a plan!\x02",
    )

    CloseMessageWindow()

    label("loc_190D")

    Jump("loc_19BA")

    label("loc_1910")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_19BA")

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

    label("loc_19BA")

    TalkEnd(0xA)
    Return()

    # Function_10_D28 end

    def Function_11_19BE(): pass

    label("Function_11_19BE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_19CB")
    Jump("loc_1E1F")

    label("loc_19CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_19D5")
    Jump("loc_1E1F")

    label("loc_19D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_19DF")
    Jump("loc_1E1F")

    label("loc_19DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_19E9")
    Jump("loc_1E1F")

    label("loc_19E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_19F3")
    Jump("loc_1E1F")

    label("loc_19F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_1B5B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1A90")

    ChrTalk(
        0xFE,
        (
            "#840F'Zane the Immovable' may have stolen the spot-\x01",
            "light, but you're the ones I really noticed.\x01",
            "You guys fought amazingly well today.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B58")

    label("loc_1A90")

    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "#840FHey.\x02\x03",
            "'Zane the Immovable' may have stolen the spot-\x01",
            "light, but you're the ones I really noticed.\x01",
            "You guys fought amazingly well today.\x02\x03",
            "You showed a lot of skill and\x01",
            "teamwork out there.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B58")

    Jump("loc_1E1F")

    label("loc_1B5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_1B65")
    Jump("loc_1E1F")

    label("loc_1B65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1E04")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1C50")

    ChrTalk(
        0xFE,
        (
            "#840FWe both fought, and we both advanced.\x01",
            "It was an excellent day for us all.\x02\x03",
            "I am more convinced than ever that when we\x01",
            "ultimately face off against one another, we'll\x01",
            "be ready for it...and it will be glorious!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E01")

    label("loc_1C50")

    OP_A2(0x0)

    ChrTalk(
        0xFE,
        "#840FHey, Estelle and Joshua!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000FHey, Kurt.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#840FWe both fought, and we both advanced.\x01",
            "It was an excellent day for us all.\x02\x03",
            "I spoke with Carna. She seems to think\x01",
            "you have quite a lot of skill.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FThat's very kind, but we're really\x01",
            "still just novices.\x02\x03",
            "Hopefully we'll learn a few new\x01",
            "techniques as we go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#841FHa, ha, ha! Well, I'm hoping I get\x01",
            "a chance to fight you out there,\x01",
            "so don't let me down!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E01")

    Jump("loc_1E1F")

    label("loc_1E04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_1E0E")
    Jump("loc_1E1F")

    label("loc_1E0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_1E18")
    Jump("loc_1E1F")

    label("loc_1E18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1E1F")

    label("loc_1E1F")

    TalkEnd(0xFE)
    Return()

    # Function_11_19BE end

    def Function_12_1E23(): pass

    label("Function_12_1E23")

    ClearMapFlags(0x10000000)
    EventBegin(0x0)
    OP_31(0x3, 0x0, 0x1E)
    OP_B5(0x3, 0x0)
    OP_B5(0x3, 0x1)
    OP_B5(0x3, 0x2)
    OP_B5(0x3, 0x3)
    OP_B5(0x3, 0x4)
    OP_B5(0x3, 0x5)
    OP_41(0x3, 0x5E)
    OP_41(0x3, 0xF5)
    OP_41(0x3, 0x113)
    OP_41(0x3, 0x25C, 0x0)
    OP_41(0x3, 0x26B, 0x1)
    OP_41(0x3, 0x25F, 0x2)
    OP_41(0x3, 0x262, 0x2)
    OP_35(0x3, 0xB4)
    OP_35(0x3, 0xB5)
    OP_36(0x3, 0xF5)
    OP_6D(12040, 2000, 7430, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6E(262, 0)
    AddParty(0x3, 0xFF)
    AddParty(0x7, 0xFF)
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    SetChrPos(0x101, 11710, 2000, 7600, 0)
    SetChrPos(0x102, 12480, 2000, 8230, 0)
    SetChrPos(0x108, 8480, 0, -1270, 135)
    SetChrPos(0x104, 7240, -250, -7700, 135)
    SetChrFlags(0x104, 0x80)

    def lambda_1F24():

        label("loc_1F24")

        TurnDirection(0xFE, 0x108, 0)
        OP_48()
        Jump("loc_1F24")

    QueueWorkItem2(0x101, 1, lambda_1F24)

    def lambda_1F35():

        label("loc_1F35")

        TurnDirection(0xFE, 0x108, 0)
        OP_48()
        Jump("loc_1F35")

    QueueWorkItem2(0x102, 1, lambda_1F35)

    def lambda_1F46():
        OP_8E(0xFE, 0x2DB4, 0x0, 0x122, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1F46)

    def lambda_1F61():
        OP_8E(0xFE, 0x30D4, 0x0, 0x3B6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1F61)

    def lambda_1F7C():

        label("loc_1F7C")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_1F7C")

    QueueWorkItem2(0x108, 1, lambda_1F7C)
    OP_6D(10650, 0, 1690, 3000)

    ChrTalk(
        0x108,
        "#070F#6PGood morning, young ones.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F#2PGood morning, Zane!\x02",
    )

    CloseMessageWindow()

    def lambda_1FE6():
        OP_8E(0xFE, 0x25EE, 0x0, 0xFFFFF7CC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1FE6)

    def lambda_2001():
        OP_8E(0xFE, 0x2508, 0x0, 0xFFFFFC90, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2001)
    OP_6D(8570, 0, -1520, 2000)
    WaitChrThread(0x102, 0x2)

    ChrTalk(
        0x102,
        "#010FThank you for coming to meet us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070FHey, it's no problem.\x02\x03",
            "I've been up anyway, preparing\x01",
            "for the match today.\x02\x03",
            "Between checking out the weapon\x01",
            "smith and visiting all the stores,\x01",
            "I've had a busy morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006FBeing prepared means no\x01",
            "regrets for you, huh?\x02\x03",
            "#505FBy the way...where's Olivier?\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x6, 0x0, 0x64)
    Sleep(200)

    ChrTalk(
        0x104,
        "#2PGood morrow, my dear companions!\x02",
    )

    CloseMessageWindow()

    def lambda_219E():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_219E)

    def lambda_21AC():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_21AC)

    def lambda_21BA():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_21BA)
    ClearChrFlags(0x104, 0x80)
    OP_9F(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_21D8():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_21D8)
    OP_8E(0x104, 0x1C0C, 0xFFFFFF06, 0xFFFFE732, 0x7D0, 0x0)

    def lambda_21FE():

        label("loc_21FE")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_21FE")

    QueueWorkItem2(0x108, 1, lambda_21FE)

    def lambda_220F():

        label("loc_220F")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_220F")

    QueueWorkItem2(0x101, 1, lambda_220F)

    def lambda_2220():

        label("loc_2220")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_2220")

    QueueWorkItem2(0x102, 1, lambda_2220)

    def lambda_2231():
        OP_8E(0xFE, 0x20EE, 0x0, 0xFFFFF65A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2231)
    WaitChrThread(0x104, 0x1)

    ChrTalk(
        0x104,
        (
            "#031F*sniff* What is that aroma? Battle?\x01",
            "Conflict? No. Victory! Oh, what an \x01",
            "enchanting perfume this time of day!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#509F#4PDo you just deliberately time\x01",
            "your entrances like this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FGood morning, Olivier.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F#4PMorning... Looks like we're\x01",
            "all here, then.\x02\x03",
            "What say we go ahead\x01",
            "and get moving?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F#4PThe tournament doesn't start\x01",
            "up again until noon.\x02\x03",
            "It's still early, so what are\x01",
            "we going to do to kill time?\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x108, 0xFF)
    OP_8C(0x108, 135, 400)

    ChrTalk(
        0x108,
        (
            "#070FFor starters, I think we should\x01",
            "go to the equipment shop and\x01",
            "get all of our gear in order.\x02\x03",
            "Then, perhaps do a bit of monster-\x01",
            "hunting to keep us focused.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x104, 0, 400)

    ChrTalk(
        0x104,
        "#030FI see. A little warm-up, then?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FSome practice at working as a\x01",
            "team might do us some good.\x02\x03",
            "After all, we've never all fought\x01",
            "at each others' sides before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F#4PI'm up for it! Let's go!\x02\x03",
            "And once we're ready, we can head\x01",
            "straight to the Grand Arena!\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x108, 0xFF)
    OP_A2(0x619)
    OP_28(0x47, 0x4, 0x2)
    OP_28(0x47, 0x4, 0x4)
    OP_28(0x47, 0x1, 0x1)
    OP_28(0x47, 0x1, 0x2)
    EventEnd(0x0)
    Return()

    # Function_12_1E23 end

    def Function_13_25F5(): pass

    label("Function_13_25F5")

    ClearMapFlags(0x10000000)
    EventBegin(0x0)
    OP_6D(7340, -250, -5730, 0)
    OP_67(0, 5960, -10000, 0)
    OP_6B(3010, 0)
    SetChrPos(0x8, 4320, 0, 1700, 180)
    TurnDirection(0x8, 0x101, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x101, 6490, -250, -5810, 0)
    SetChrPos(0x102, 7740, -250, -5800, 0)
    FadeToBright(1000, 0)
    OP_0D()

    NpcTalk(
        0x8,
        "Man's Voice",
        "#6PSo, you're FINALLY back...\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Man's Voice",
        (
            "#6PYou sure know how to keep\x01",
            "a fellow waiting...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_271A():

        label("loc_271A")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_271A")

    QueueWorkItem2(0x101, 1, lambda_271A)

    ChrTalk(
        0x101,
        "#501FHey, I know that voice...\x02",
    )

    CloseMessageWindow()

    def lambda_274F():
        OP_6D(4450, 0, 1130, 2000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_274F)

    def lambda_2767():
        OP_8E(0xFE, 0xFFA, 0x0, 0xFFFFFF74, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2767)
    Sleep(300)

    def lambda_2787():
        OP_8E(0xFE, 0x145A, 0x0, 0xFFFFFEA2, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2787)
    WaitChrThread(0x102, 0x1)

    ChrTalk(
        0x102,
        "#010F#6PGood to see you, Nial.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008FHow've you been?\x02\x03",
            "Don't tell me you came here\x01",
            "just to see little old us...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#141F#4POkay, then. I won't tell you.\x02\x03",
            "I'm doing interviews with the \x01",
            "tourney contestants for my article.\x02\x03",
            "I figured you folks would be\x01",
            "my best bet for getting the\x01",
            "inside story.\x02\x03",
            "I was hoping I'd get a chance\x01",
            "to ambush you into an interview\x01",
            "at the hotel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F*sigh*... You're way too good\x01",
            "at your job, you know that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#6PWell, it's not that we're not\x01",
            "glad to see you...\x02\x03",
            "...but this is you we're talking\x01",
            "about. What's your angle?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006FHunting for the next big\x01",
            "story, I'll bet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#145F#4PHa! You wound me to the quick, kid.\x02\x03",
            "I've been like a big brother to you... You\x01",
            "scratch my back, I scratch yours. And now\x01",
            "you think of me as nothing but a newshound?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#509FWe KNOW you're nothing\x01",
            "but a newshound.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F#6PNot to mention, the age difference\x01",
            "is a little much for us to think\x01",
            "of you as a brother.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#144F#4POh, shut it.\x02\x03",
            "If that's how you're going to\x01",
            "be, then I'm leaving. And you're\x01",
            "coming with me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F#6PUhhh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001FI wouldn't mind a little\x01",
            "night air before bed!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#145F#4PGood. We're halfway there, then.\x02\x03",
            "#141FThere's this quaint little eatery\x01",
            "right next door to where I work.\x02\x03",
            "It's the perfect place to\x01",
            "sit and talk.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x47, 0x1, 0x400)
    OP_20(0x5DC)
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T4152   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_13_25F5 end

    def Function_14_2CD6(): pass

    label("Function_14_2CD6")

    EventBegin(0x0)
    OP_6D(6960, 0, 4490, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(287, 0)
    AddParty(0x3, 0xFF)
    AddParty(0x7, 0xFF)
    SetChrPos(0x108, 8480, 0, -1270, 90)
    SetChrPos(0x104, 8430, 0, -2470, 45)
    SetChrPos(0x101, 9710, 0, -2100, 270)
    SetChrPos(0x102, 9480, 0, -880, 270)
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    FadeToBright(2000, 0)
    OP_6D(8570, 0, -1520, 3000)

    ChrTalk(
        0x104,
        (
            "#031FWell, we all seem accounted for.\x02\x03",
            "Shall we be off?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070FOur match is in the afternoon, just\x01",
            "like yesterday, so we're free to do\x01",
            "as we please in the meantime.\x02\x03",
            "We can stop by and get our equipment\x01",
            "set up, and maybe even work in a\x01",
            "little monster killing on the way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F#4POh, if that's what you're after,\x01",
            "I know exactly where to go.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Estelle told them about the key to the sewers that the Ravens had given her\x01",
            "and Joshua.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(
        0x108,
        (
            "#073FYou don't say?\x01",
            "That's mighty interesting.\x02\x03",
            "I hear there are some tough monsters\x01",
            "down there, so maybe they'll prove\x01",
            "to be worthy opponents.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#035FA byzantine labyrinth, snaking\x01",
            "out beneath this jeweled city.\x02\x03",
            "My adventurer's bosom\x01",
            "strains its corset-strings!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FI have no problem with that,\x01",
            "provided that we have time.\x02\x03",
            "I think the entrance is just at\x01",
            "the edge of western block's\x01",
            "residential district.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x621)
    OP_28(0x48, 0x4, 0x2)
    OP_28(0x48, 0x4, 0x4)
    OP_28(0x48, 0x1, 0x1)
    OP_28(0x48, 0x1, 0x2)
    EventEnd(0x0)
    Return()

    # Function_14_2CD6 end

    def Function_15_314C(): pass

    label("Function_15_314C")

    EventBegin(0x0)
    OP_6D(6960, 0, 4490, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(287, 0)
    AddParty(0x3, 0xFF)
    AddParty(0x7, 0xFF)
    SetChrPos(0x108, 8480, 0, -1270, 90)
    SetChrPos(0x104, 8430, 0, -2470, 45)
    SetChrPos(0x101, 9710, 0, -2100, 270)
    SetChrPos(0x102, 9480, 0, -880, 270)
    FadeToDark(0, 0, -1)
    OP_20(0x0)
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_1E()
    FadeToBright(2000, 0)
    OP_6D(8570, 0, -1520, 3000)

    ChrTalk(
        0x104,
        (
            "#034FYesterday was genuinely awful.\x02\x03",
            "I returned to the embassy, overfull of spirit,\x01",
            "when those tiresome guards saw fit to stop and\x01",
            "cast flaming, stinking disparagements at me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070FThey've tightened security at\x01",
            "night, supposedly for anti-\x01",
            "terrorist purposes.\x02\x03",
            "Were you two okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019FYes... We went to bed rather early,\x01",
            "so we didn't have any problems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506FAnd Elnan lent us something\x01",
            "that might really give us\x01",
            "an edge!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Estelle explained that Elnan had loaned them the spare key to the Grancel\x01",
            "Sewers.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(
        0x108,
        (
            "#071FNow THAT should come in handy...\x02\x03",
            "He's a young one, but he's got a real\x01",
            "spark to him. He always seems to know\x01",
            "what you need, and when you need it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006FSo, what do you say we check\x01",
            "out the sewers this morning?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FThe gate is just north of\x01",
            "the arena.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#035FWell, if it's for the banquet, we\x01",
            "could muster up one more huzzah.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x62F)
    OP_28(0x49, 0x4, 0x2)
    OP_28(0x49, 0x4, 0x4)
    OP_28(0x49, 0x1, 0x1)
    OP_28(0x49, 0x1, 0x2)
    EventEnd(0x0)
    Return()

    # Function_15_314C end

    def Function_16_35E1(): pass

    label("Function_16_35E1")

    EventBegin(0x0)
    SetChrPos(0x9, 35140, 0, 114000, 0)
    OP_6D(35210, 0, 115000, 0)
    OP_67(0, 4890, -10000, 0)
    OP_6B(1680, 0)
    OP_6C(320000, 0)
    OP_6E(509, 0)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x108, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x101, 35130, 0, 107040, 180)
    SetChrPos(0x102, 35130, 0, 107040, 180)
    SetChrPos(0x108, 35130, 0, 107040, 180)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x9,
        (
            "#843F#6P...\x02\x03",
            "#6PI wish I could remember that\x01",
            "time a little better...\x02\x03",
            "#844F#6PIt's like there's a thick fog\x01",
            "blanketing the whole thing...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3729():
        OP_6D(35210, 0, 113750, 2000)
        ExitThread()

    QueueWorkItem(0x108, 3, lambda_3729)

    def lambda_3741():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3741)

    def lambda_3753():
        OP_8E(0xFE, 0x87BE, 0x0, 0x1B6C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3753)
    Sleep(600)

    def lambda_3773():
        OP_8E(0xFE, 0x8BA6, 0x0, 0x1B652, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3773)

    def lambda_378E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_378E)
    Sleep(600)

    def lambda_37A5():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_37A5)

    def lambda_37B7():
        OP_8E(0xFE, 0x8958, 0x0, 0x1B1E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_37B7)
    WaitChrThread(0x101, 0x1)

    ChrTalk(
        0x101,
        "#501FOh...hi, Kurt!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 0x1)

    ChrTalk(
        0x102,
        "#010FIt's good to see you here.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x108, 400)

    ChrTalk(
        0x9,
        (
            "#840F#4PHi, Estelle... Hi, Joshua.\x02\x03",
            "Oh, Zane's with you, too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F#3PDidn't you know that we were\x01",
            "going to that dinner party at\x01",
            "the castle yesterday?\x02\x03",
            "That was when these two rookies\x01",
            "took on a pretty major assignment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#4P#842FWhat 'major assignment'?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FI think it's best if we tell you\x01",
            "more or less the whole story.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Joshua explained all the circumstances that had led to their request from\x01",
            "the queen.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x9,
        (
            "#4P#842F...\x02\x03",
            "#844F...You're serious?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006FOf course we are.\x02\x03",
            "That's why we really need your help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#4P#842FNo... That's not it.\x02\x03",
            "I admit, I'm shocked at Her\x01",
            "Majesty's request of you...\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x5DC)

    ChrTalk(
        0x9,
        (
            "#4P#844FBut the Black Orbment that the\x01",
            "colonel has... It's real...?\x02",
        )
    )

    CloseMessageWindow()
    OP_21()
    OP_1D(0x51)

    ChrTalk(
        0x101,
        (
            "#505FKurt...?\x02\x03",
            "Wh-What's wrong?\x01",
            "You look awfully pale...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#4P#847F#10AUuggghhh...\x05\x02",
    )

    OP_9E(0x9, 0x1E, 0x0, 0x3E8, 0xBB8)
    SetChrFlags(0x9, 0x20)
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x9, 4)

    def lambda_3B7F():
        OP_99(0xFE, 0x0, 0x3, 0x3E8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_3B7F)
    Sleep(500)

    ChrTalk(
        0x9,
        "#4P#847F#10A#3SAaaaaahhhh...!\x05\x02",
    )

    OP_9E(0x9, 0x1E, 0x0, 0x3E8, 0xFA0)

    def lambda_3BCA():

        label("loc_3BCA")

        OP_9E(0xFE, 0x14, 0x0, 0x3E8, 0x1770)
        OP_48()
        Jump("loc_3BCA")

    QueueWorkItem2(0x9, 1, lambda_3BCA)
    Sleep(800)

    ChrTalk(
        0x9,
        "#4P#847F#5SAAAAAAAAAGGGGHHHH!!!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#580FWhoa!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012FWhat in the world...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#3P#072FHrm... Step away from him.\x02",
    )

    CloseMessageWindow()

    def lambda_3C7A():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3C7A)
    TurnDirection(0x101, 0x108, 400)

    ChrTalk(
        0x101,
        "#004FHuh...?\x02",
    )

    CloseMessageWindow()

    def lambda_3CA1():

        label("loc_3CA1")

        TurnDirection(0xFE, 0x108, 0)
        OP_48()
        Jump("loc_3CA1")

    QueueWorkItem2(0x102, 1, lambda_3CA1)

    def lambda_3CB2():

        label("loc_3CB2")

        TurnDirection(0xFE, 0x108, 0)
        OP_48()
        Jump("loc_3CB2")

    QueueWorkItem2(0x101, 1, lambda_3CB2)

    def lambda_3CC3():
        OP_8F(0xFE, 0x8412, 0x0, 0x1B3A0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3CC3)

    def lambda_3CDE():
        OP_8F(0xFE, 0x8DF4, 0x0, 0x1B314, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3CDE)
    Sleep(300)
    OP_8E(0x108, 0x88CC, 0x0, 0x1B7D8, 0x7D0, 0x0)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    Sleep(500)

    ChrTalk(
        0x108,
        "#074FHaaaaahhhh...\x02",
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x108, 2)
    OP_0D()

    ChrTalk(
        0x108,
        "#076F#20A#3SShade...\x05\x02",
    )


    def lambda_3D5C():

        label("loc_3D5C")

        OP_99(0xFE, 0x0, 0x3, 0x3E8)
        OP_48()
        Jump("loc_3D5C")

    QueueWorkItem2(0x108, 1, lambda_3D5C)
    OP_6B(1600, 3000)
    OP_44(0x108, 0xFF)
    OP_51(0x108, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x108, 3)
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x9, 5)
    OP_44(0x9, 0xFF)
    SetChrFlags(0x9, 0x800)

    def lambda_3DA5():
        OP_6D(35130, 0, 115000, 500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3DA5)

    def lambda_3DBD():
        OP_8F(0xFE, 0x893A, 0x0, 0x1C32C, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3DBD)

    def lambda_3DD8():
        OP_94(0x1, 0xFE, 0xB4, 0x258, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3DD8)

    def lambda_3DEE():
        OP_94(0x1, 0xFE, 0xB4, 0x258, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3DEE)

    ChrTalk(
        0x108,
        "#077F#3P#10A#5SLIFT!\x05\x02",
    )

    OP_22(0x1FB, 0x0, 0x64)
    OP_22(0x217, 0x0, 0x64)
    WaitChrThread(0x9, 0x1)
    OP_22(0x22A, 0x0, 0x64)

    ChrTalk(
        0x9,
        "#847F#4P#10A#3SAgh!\x05\x02",
    )

    OP_6B(1700, 0)
    OP_6B(1670, 100)
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x9, 4)

    def lambda_3E6D():
        OP_99(0xFE, 0x0, 0x3, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_3E6D)
    Sleep(2000)
    SetChrFlags(0x9, 0x800)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(
        0x101,
        (
            "#004F#3PWh-What was THAT?!\x02\x03",
            "You didn't even touch him, and he\x01",
            "acted like he got electrocuted!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012FIt's a special spirit-channeling\x01",
            "breath technique.\x02\x03",
            "It allows the user to directly\x01",
            "affect the target's body without\x01",
            "direct physical contact.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#074F#6PI don't normally like to be so\x01",
            "rough, but time isn't exactly\x01",
            "on our side.\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_51(0x108, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x108, 65535)
    OP_0D()

    def lambda_4000():
        OP_8F(0xFE, 0x8552, 0x0, 0x1C020, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_4000)
    Sleep(300)

    def lambda_4020():
        OP_6D(35130, 0, 115500, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4020)
    Sleep(300)
    SetChrFlags(0x101, 0x4)

    def lambda_4042():
        OP_8E(0xFE, 0x88A4, 0x0, 0x1BB2A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4042)
    Sleep(200)

    def lambda_4062():
        OP_8E(0xFE, 0x8C00, 0x0, 0x1BBAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4062)
    WaitChrThread(0x108, 0x1)
    OP_8C(0x108, 90, 400)
    WaitChrThread(0x101, 0x1)
    OP_8C(0x101, 0, 400)
    ClearChrFlags(0x101, 0x4)

    ChrTalk(
        0x108,
        "#070FHow are you feeling?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#4P#843FAhh...wow.\x01",
            "Actually, a lot better.\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x9, 0x3, 0x0, 0x3E8)
    Sleep(200)
    SetChrChipByIndex(0x9, 1)

    ChrTalk(
        0x9,
        (
            "#4P#844FI can't remember every detail...but\x01",
            "a good bit of it's coming back.\x02\x03",
            "I'm a little unsteady from the shock,\x01",
            "but I think I'll be all right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505FSo what do you remember?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#4P#845FDidn't I say so before? There was an\x01",
            "accident, around three months ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#012FYou lost your memories while\x01",
            "you were working, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#4P#844FYes... Someone had asked me to\x01",
            "check up on those men in the\x01",
            "black outfits...\x02\x03",
            "#843FAnd then I took something\x01",
            "suspicious from them...\x02\x03",
            "#842FIt was...the Black Orbment...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#005F!!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#012FSo the person who gave\x01",
            "you the assignment...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#4P#842FYes, it was your father, Cassius.\x02\x03",
            "I wasted no time in packaging\x01",
            "it up and sending it to him...\x02\x03",
            "#845FBut that's really as far back\x01",
            "as I can remember...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#580FSo...the 'K' on that package\x01",
            "was you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#4P#843FYes...\x02\x03",
            "I think I also remember there\x01",
            "being a note that said to have\x01",
            "Professor Russell analyze it...\x02\x03",
            "#840FI get it... The package was\x01",
            "delivered to you two...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#012FDo you remember anything\x01",
            "after that?\x02\x03",
            "Anything that happened after\x01",
            "you sent off the package?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#4P#844FYes... After I left the port,\x01",
            "someone called out to me...\x02\x03",
            "And then...\x02\x03",
            "#843F...\x02\x03",
            "#847FIt's no good.\x01",
            "It's all still one big blur.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#072FYou're probably best off not\x01",
            "pressing your luck.\x02\x03",
            "It's likely to just cause strain\x01",
            "that you can't handle yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#4P#845FYes, all right...\x02\x03",
            "I'm really just amazed that\x01",
            "I was able to remember anything\x01",
            "at all...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#003FWhich brings us to a bigger\x01",
            "question... Who would have\x01",
            "done this?\x02\x03",
            "Maybe those Special Ops guys?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#015FIt's possible...\x02\x03",
            "#013FThey did use that nasty poison\x01",
            "on Agate, after all...\x02\x03",
            "It's as if they're manufacturing\x01",
            "and testing new drugs.\x02\x03",
            "#012FMaybe they've made something\x01",
            "to cause memory loss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007FUgh...\x01",
            "Now there's a cheerful thought.\x02\x03",
            "#002FPlus, there's the Sky Bandits' boss,\x01",
            "and Mayor Dalmore to consider...\x02\x03",
            "We have to be really careful...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#4P#840FI'm sorry... I don't have anything\x01",
            "really useful to tell you.\x02\x03",
            "I know what Her Majesty asked you to\x01",
            "do. I want to help, if you'll let me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505FB-But...\x01",
            "Are you sure you'll be okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#4P#841FSure. My memory may be like a\x01",
            "sieve, but physically, I'm fine.\x02\x03",
            "I owe you for your help...so please,\x01",
            "allow me to make it up to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070FIf you're feeling up to it, sure.\x02\x03",
            "We need to work out a strategy. For\x01",
            "now, let's meet back at the guild.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x20)

    def lambda_4A4B():

        label("loc_4A4B")

        TurnDirection(0xFE, 0x108, 0)
        OP_48()
        Jump("loc_4A4B")

    QueueWorkItem2(0x9, 1, lambda_4A4B)

    ChrTalk(
        0x9,
        (
            "#4P#840FAll right...\x01",
            "You have my thanks!\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x9, 0xFF)

    def lambda_4A8E():

        label("loc_4A8E")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_4A8E")

    QueueWorkItem2(0x101, 1, lambda_4A8E)

    def lambda_4A9F():

        label("loc_4A9F")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_4A9F")

    QueueWorkItem2(0x102, 1, lambda_4A9F)

    def lambda_4AB0():

        label("loc_4AB0")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_4AB0")

    QueueWorkItem2(0x108, 1, lambda_4AB0)

    def lambda_4AC1():
        OP_6D(34710, 0, 112900, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4AC1)
    OP_8E(0x9, 0x8606, 0x0, 0x1BB2A, 0xBB8, 0x0)
    OP_8E(0x9, 0x8912, 0x0, 0x1A298, 0xBB8, 0x0)

    def lambda_4B01():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4B01)
    SetChrFlags(0x9, 0x4)
    OP_8E(0x9, 0x88C2, 0x0, 0x19B36, 0xBB8, 0x0)
    SetChrFlags(0x9, 0x80)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x108, 0xFF)
    OP_28(0x4B, 0x1, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4B, 0x1, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x4B, 0x1, 0x20)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x4B, 0x1, 0x40)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x4B, 0x1, 0x80)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4B66")
    OP_28(0x4B, 0x1, 0x100)

    label("loc_4B66")

    OP_20(0x3E8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(34980, 0, 113450, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, 34980, 0, 113450, 180)
    SetChrPos(0x102, 34980, 0, 113450, 180)
    SetChrPos(0x108, 34980, 0, 113450, 180)
    FadeToBright(1000, 0)
    OP_1D(0xE)
    EventEnd(0x0)
    Return()

    # Function_16_35E1 end

    def Function_17_4BF4(): pass

    label("Function_17_4BF4")

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

    # Function_17_4BF4 end

    SaveToFile()

Try(main)
