from ED6ScenarioHelper import *

def main():
    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4120   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4120.x',
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
        'Carna',                                # 9
        'Shepard',                              # 10
        'Chaeli',                               # 11
        'Zacharias',                            # 12
        'Tom',                                  # 13
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
        'ED6_DT07/CH01680 ._CH',             # 01
        'ED6_DT07/CH01690 ._CH',             # 02
        'ED6_DT07/CH01140 ._CH',             # 03
        'ED6_DT07/CH01040 ._CH',             # 04
    )

    AddCharChipPat(
        'ED6_DT07/CH01240P._CP',             # 00
        'ED6_DT07/CH01680P._CP',             # 01
        'ED6_DT07/CH01690P._CP',             # 02
        'ED6_DT07/CH01140P._CP',             # 03
        'ED6_DT07/CH01040P._CP',             # 04
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
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -1540,
        Z                   = 0,
        Y                   = 69240,
        Direction           = 0,
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
        X                   = 1260,
        Z                   = 0,
        Y                   = -240,
        Direction           = 236,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 58580,
        Z                   = 0,
        Y                   = 360,
        Direction           = 102,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 120030,
        Z                   = 0,
        Y                   = -1260,
        Direction           = 10,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )


    DeclActor(
        TriggerX            = -10,
        TriggerZ            = 0,
        TriggerY            = -1600,
        TriggerRange        = 800,
        ActorX              = 1260,
        ActorZ              = 1500,
        ActorY              = -240,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 60410,
        TriggerZ            = 0,
        TriggerY            = 390,
        TriggerRange        = 800,
        ActorX              = 58580,
        ActorZ              = 1500,
        ActorY              = 360,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 119960,
        TriggerZ            = 0,
        TriggerY            = 650,
        TriggerRange        = 800,
        ActorX              = 120030,
        ActorZ              = 1500,
        ActorY              = -1260,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1DE",          # 00, 0
        "Function_1_27D",          # 01, 1
        "Function_2_2CA",          # 02, 2
        "Function_3_2E0",          # 03, 3
        "Function_4_2E5",          # 04, 4
        "Function_5_E87",          # 05, 5
        "Function_6_E8C",          # 06, 6
        "Function_7_1C0A",         # 07, 7
        "Function_8_22F4",         # 08, 8
        "Function_9_22F9",         # 09, 9
        "Function_10_3534",        # 0A, 10
    )


    def Function_0_1DE(): pass

    label("Function_0_1DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_200")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 5480, 4000, -2590, 90)

    label("loc_200")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_20A")
    Jump("loc_27C")

    label("loc_20A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_214")
    Jump("loc_27C")

    label("loc_214")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_21E")
    Jump("loc_27C")

    label("loc_21E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_228")
    Jump("loc_27C")

    label("loc_228")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_232")
    Jump("loc_27C")

    label("loc_232")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_23C")
    Jump("loc_27C")

    label("loc_23C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_246")
    Jump("loc_27C")

    label("loc_246")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_250")
    Jump("loc_27C")

    label("loc_250")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_26B")
    SetChrPos(0x9, 3310, 0, 129900, 0)
    Jump("loc_27C")

    label("loc_26B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_275")
    Jump("loc_27C")

    label("loc_275")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_27C")

    label("loc_27C")

    Return()

    # Function_0_1DE end

    def Function_1_27D(): pass

    label("Function_1_27D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2B0")
    OP_B1("t4120_y")
    Jump("loc_2B9")

    label("loc_2B0")

    OP_B1("t4120_n")

    label("loc_2B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 2)), scpexpr(EXPR_END)), "loc_2C9")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x4B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2C9")

    Return()

    # Function_1_27D end

    def Function_2_2CA(): pass

    label("Function_2_2CA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2DF")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_2CA")

    label("loc_2DF")

    Return()

    # Function_2_2CA end

    def Function_3_2E0(): pass

    label("Function_3_2E0")

    Call(0, 4)
    Return()

    # Function_3_2E0 end

    def Function_4_2E5(): pass

    label("Function_4_2E5")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_381")

    ChrTalk(
        0xC,
        (
            "What a beautiful day. Perfect\x01",
            "weather for celebrating Her\x01",
            "Majesty's birthday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Aaaanyway, time to get to work.\x01",
            "Got a lot to do today!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E83")

    label("loc_381")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_3C3")

    ChrTalk(
        0xC,
        "Not many customers today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Something going on?\x02",
    )

    CloseMessageWindow()
    Jump("loc_E83")

    label("loc_3C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_520")

    ChrTalk(
        0xC,
        (
            "It's important to listen to one's\x01",
            "customers. I mean, they pay the\x01",
            "bills, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I've always felt that if a customer needs help\x01",
            "after hours-- I mean REALLY needs help-- then\x01",
            "I'll gladly stay late and do what I can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Gotta make sure Zacharias signs off\x01",
            "on it, though. And if I do it too\x01",
            "often, he'll tell me to take a hike!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E83")

    label("loc_520")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_5AE")

    ChrTalk(
        0xC,
        "We'll be closing soon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "But I've still got to hurry up and\x01",
            "try to get these rush-jobs finished.\x01",
            "I owe it to our customers!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E83")

    label("loc_5AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_651")

    ChrTalk(
        0xC,
        (
            "Today's the final match of the\x01",
            "Martial Arts Competition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I'll be finishing up repairs while\x01",
            "my customers are enjoying themselves\x01",
            "at the match.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E83")

    label("loc_651")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_7E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_6BB")

    ChrTalk(
        0xC,
        (
            "I don't know how good an idea it was\x01",
            "to let the Sky Bandits into the\x01",
            "competition...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7E3")

    label("loc_6BB")

    OP_A2(0x3)

    ChrTalk(
        0xC,
        (
            "The Martial Arts Competition seems\x01",
            "livelier than ever this year. You\x01",
            "can FEEL the energy in the air!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "All the customers who come to\x01",
            "pick up their orders just can't\x01",
            "stop talking about it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I don't know how good an idea it was\x01",
            "to let the Sky Bandits into the\x01",
            "competition, though...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7E3")

    Jump("loc_E83")

    label("loc_7E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_974")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_84B")

    ChrTalk(
        0xC,
        (
            "I like feeling that I've helped\x01",
            "people using my brains and my\x01",
            "own two hands...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_971")

    label("loc_84B")

    OP_A2(0x3)

    ChrTalk(
        0xC,
        (
            "I like feeling that I've helped\x01",
            "people using my brains and my\x01",
            "own two hands...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "From a grandfather's treasured\x01",
            "watch, to a child's favorite\x01",
            "toy...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I love seeing the smiles on their faces when\x01",
            "they get back their precious keepsakes, working\x01",
            "just as they did when they were new.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_971")

    Jump("loc_E83")

    label("loc_974")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_AE7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_A15")

    ChrTalk(
        0xC,
        (
            "I feel like I have a responsibility\x01",
            "to fix anything I've sold to a\x01",
            "customer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "But I'll repair things even\x01",
            "if they weren't bought here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AE4")

    label("loc_A15")

    OP_A2(0x3)

    ChrTalk(
        0xC,
        (
            "I always listen to my customers.\x01",
            "I make a point of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I feel like I have a responsibility\x01",
            "to fix anything I've sold to a\x01",
            "customer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "But I'll repair things even\x01",
            "if they weren't bought here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AE4")

    Jump("loc_E83")

    label("loc_AE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_CA8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_B9C")

    ChrTalk(
        0xC,
        (
            "Do I want to see the tournament? Absolutely!\x01",
            "But I have work to do here, and it would be\x01",
            "remiss of me to put all of that aside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "The customer comes first!\x02",
    )

    CloseMessageWindow()
    Jump("loc_CA5")

    label("loc_B9C")

    OP_A2(0x3)

    ChrTalk(
        0xC,
        (
            "Today marks the beginning of what\x01",
            "promises to be another spectacular\x01",
            "Martial Arts Competition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I'd love to go see the fighters in action,\x01",
            "but I have work to do here, and it would be\x01",
            "remiss of me to put all of that aside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "The customer comes first!\x02",
    )

    CloseMessageWindow()

    label("loc_CA5")

    Jump("loc_E83")

    label("loc_CA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_DB2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_D11")

    ChrTalk(
        0xC,
        (
            "I was beginning to think the\x01",
            "Martial Arts Competition would\x01",
            "be canceled this year.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DAF")

    label("loc_D11")

    OP_A2(0x3)

    ChrTalk(
        0xC,
        (
            "With the queen bedridden and all\x01",
            "this coup d'etat nonsense...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I was beginning to think the\x01",
            "Martial Arts Competition would\x01",
            "be canceled this year.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DAF")

    Jump("loc_E83")

    label("loc_DB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_E83")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_E0C")

    ChrTalk(
        0xC,
        (
            "The 3rd floor is where we handle\x01",
            "all repair and maintenance orders.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E83")

    label("loc_E0C")

    OP_A2(0x3)

    ChrTalk(
        0xC,
        "Welcome to the Wingard Orbal Factory!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "The 3rd floor is where we handle\x01",
            "all repair and maintenance orders.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E83")

    TalkEnd(0xC)
    Return()

    # Function_4_2E5 end

    def Function_5_E87(): pass

    label("Function_5_E87")

    Call(0, 6)
    Return()

    # Function_5_E87 end

    def Function_6_E8C(): pass

    label("Function_6_E8C")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EF7")
    OP_0D()
    OP_A9(0x5A)
    OP_56(0x0)
    TalkEnd(0xB)
    Return()

    label("loc_EF7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F08")
    TalkEnd(0xB)
    Return()

    label("loc_F08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_1027")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_F56")

    ChrTalk(
        0xB,
        (
            "I'm so glad Her Majesty has\x01",
            "recovered from her illness.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1024")

    label("loc_F56")

    OP_A2(0x2)

    ChrTalk(
        0xB,
        (
            "With the town's spirits up, so\x01",
            "too are my customer numbers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "During the Birthday Celebration,\x01",
            "my sales increase by a factor of\x01",
            "five.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I'm so glad Her Majesty has\x01",
            "recovered from her illness.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1024")

    Jump("loc_1C06")

    label("loc_1027")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_10AF")

    ChrTalk(
        0xB,
        (
            "These 'anti-terror' patrols are\x01",
            "really restricting my customers'\x01",
            "freedoms.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "What a fine mess this coup has\x01",
            "made, no?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C06")

    label("loc_10AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_123F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_114E")

    ChrTalk(
        0xB,
        (
            "We depend on the festivities this time of year\x01",
            "to make ends meet. If we're in the red, we're\x01",
            "dead; if we're in the black, we'll be back!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_123C")

    label("loc_114E")

    OP_A2(0x2)

    ChrTalk(
        0xB,
        (
            "It's positively amazing how much\x01",
            "money I've made off of the Martial\x01",
            "Arts Competition...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "We depend on the festivities this time of year\x01",
            "to make ends meet. If we're in the red, we're\x01",
            "dead; in we're in the black, we'll be back!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_123C")

    Jump("loc_1C06")

    label("loc_123F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_12BF")

    ChrTalk(
        0xB,
        "Okay, it's about closing time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I look forward to tallying the\x01",
            "day's sales whenever I close up\x01",
            "the register.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C06")

    label("loc_12BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1499")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1391")

    ChrTalk(
        0xB,
        (
            "I'd be ecstatic if you used Wingard-\x01",
            "branded Quartz to win it all in the\x01",
            "Martial Arts Competition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "And of course, if that WERE to\x01",
            "happen, an endorsement would be\x01",
            "appreciated as well!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1496")

    label("loc_1391")

    OP_A2(0x2)

    ChrTalk(
        0xB,
        (
            "Hey, aren't you guys the bracers\x01",
            "who made it to the finals?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I'd be ecstatic if you used Wingard-\x01",
            "branded Quartz to win it all in the\x01",
            "Martial Arts Competition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "And of course, if that WERE to\x01",
            "happen, an endorsement would be\x01",
            "appreciated as well!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1496")

    Jump("loc_1C06")

    label("loc_1499")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_15AD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1502")

    ChrTalk(
        0xB,
        (
            "I'm really looking forward to seeing\x01",
            "how much money I'll be able to make\x01",
            "tomorrow.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15AA")

    label("loc_1502")

    OP_A2(0x2)

    ChrTalk(
        0xB,
        (
            "I'm eager to see who'll win the\x01",
            "tournament, of course...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "...but what I'm really looking forward\x01",
            "to is seeing how much money I'll be able\x01",
            "to make tomorrow!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15AA")

    Jump("loc_1C06")

    label("loc_15AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_16B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1622")

    ChrTalk(
        0xB,
        (
            "I run this store with my buddy Tom,\x01",
            "but the two of us never seem to agree\x01",
            "on much of anything.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16AF")

    label("loc_1622")

    OP_A2(0x2)

    ChrTalk(
        0xB,
        (
            "I run this store with my old\x01",
            "childhood buddy Tom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "He's a real hard-worker.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "But we don't see eye-to-eye\x01",
            "on a lot of things.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16AF")

    Jump("loc_1C06")

    label("loc_16B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_183B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1756")

    ChrTalk(
        0xB,
        (
            "We get a lot of orders to repair\x01",
            "and customize during the Martial\x01",
            "Arts Competition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "See, we make our real money selling\x01",
            "new merchandise.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1838")

    label("loc_1756")

    OP_A2(0x2)

    ChrTalk(
        0xB,
        (
            "And it's nice we have so many new\x01",
            "customers this time of year...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "But we're spending all of our\x01",
            "time fixing or rebuilding items,\x01",
            "which translates into fewer sales.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "And sales are where we make our\x01",
            "REAL profit.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1838")

    Jump("loc_1C06")

    label("loc_183B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_19EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_18E3")

    ChrTalk(
        0xB,
        (
            "I'd be ecstatic if you used Wingard-\x01",
            "branded Quartz to win it all in the\x01",
            "Martial Arts Competition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It'd make for good advertising,\x01",
            "you know?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19EC")

    label("loc_18E3")

    OP_A2(0x2)

    ChrTalk(
        0xB,
        (
            "Hey, are you guys taking part\x01",
            "in the tournament?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I'm going to be closing up shop\x01",
            "soon, so I'll probably see you\x01",
            "there. I can't wait!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I'd be ecstatic if you used Wingard-\x01",
            "branded Quartz to win it all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It'd make for good advertising,\x01",
            "you know?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19EC")

    Jump("loc_1C06")

    label("loc_19EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_1A8F")

    ChrTalk(
        0xB,
        (
            "After the Royal Guardsmen stopped\x01",
            "coming in here, we lost a decent\x01",
            "chunk of our sales.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Coup d'etats aren't always so\x01",
            "good for business, eh?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C06")

    label("loc_1A8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1C06")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1B59")

    ChrTalk(
        0xB,
        (
            "Got some orbments that just won't work right?\x01",
            "Bring 'em on down! Here at the Wingard Orbal\x01",
            "Factory, no job is too big or small!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "We're professionals here. You\x01",
            "can count on us!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C06")

    label("loc_1B59")

    OP_A2(0x2)

    ChrTalk(
        0xB,
        "You guys bracers?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If so, then come on in and let\x01",
            "Wingard Orbal Factory take care\x01",
            "of all your orbment needs!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "We're professionals here. You\x01",
            "can count on us!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C06")

    TalkEnd(0xB)
    Return()

    # Function_6_E8C end

    def Function_7_1C0A(): pass

    label("Function_7_1C0A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_1C37")

    ChrTalk(
        0xFE,
        "It's pretty hopping today.\x02",
    )

    CloseMessageWindow()
    Jump("loc_22F0")

    label("loc_1C37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_1CA2")

    ChrTalk(
        0xFE,
        (
            "Did you see them too? Those royal\x01",
            "soldiers in black armor?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "They're really unnerving...\x02",
    )

    CloseMessageWindow()
    Jump("loc_22F0")

    label("loc_1CA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_1CFE")

    ChrTalk(
        0xFE,
        (
            "Don't you think it's a bit TOO\x01",
            "quiet, considering the tournament\x01",
            "just ended?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22F0")

    label("loc_1CFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_1D6D")

    ChrTalk(
        0xFE,
        (
            "The shop's calmed down a bit\x01",
            "since the tournament ended.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Seems like I can finally relax...\x02",
    )

    CloseMessageWindow()
    Jump("loc_22F0")

    label("loc_1D6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1E25")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1DAD")

    ChrTalk(
        0xFE,
        (
            "If only I were a bit better with\x01",
            "words...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E22")

    label("loc_1DAD")

    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "*sigh* If only I were a bit better\x01",
            "with words...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When I'm around people, I just\x01",
            "don't know what to say.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E22")

    Jump("loc_22F0")

    label("loc_1E25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_1E94")

    ChrTalk(
        0xFE,
        "I'm going out with my wife tomorrow.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So that means I have to get all\x01",
            "this work done today.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22F0")

    label("loc_1E94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_2003")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1F49")

    ChrTalk(
        0xFE,
        (
            "Hmm. It looks like we have enough\x01",
            "merchandise for now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With this much in stock, we should\x01",
            "be totally okay until after the\x01",
            "Queen's Birthday Celebration.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2000")

    label("loc_1F49")

    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "So the people who were in here in\x01",
            "handcuffs the other day apparently\x01",
            "participated in the tournament.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Who lets criminals take part\x01",
            "in sporting events?! I mean,\x01",
            "seriously!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2000")

    Jump("loc_22F0")

    label("loc_2003")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_20D1")

    ChrTalk(
        0xFE,
        (
            "When the tournament starts, a\x01",
            "lot of the participants usually\x01",
            "come through here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's always highly unnerving ordering\x01",
            "the parts and items I'll need before\x01",
            "the flood of people arrive...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22F0")

    label("loc_20D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_2193")

    ChrTalk(
        0xFE,
        (
            "Orbal guns and rifles and such--\x01",
            "that sort of thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yesterday alone, practically the\x01",
            "whole store was bought out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Our selection is pretty limited\x01",
            "right now as a result.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22F0")

    label("loc_2193")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_21F6")

    ChrTalk(
        0xFE,
        (
            "Welcome! Please take your time,\x01",
            "and let me know if you need any\x01",
            "help with anything.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22F0")

    label("loc_21F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_22F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2273")

    ChrTalk(
        0xFE,
        (
            "I'm not very good at talking\x01",
            "with customers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I generally let my wife handle\x01",
            "that part of the job.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22F0")

    label("loc_2273")

    OP_A2(0x0)

    ChrTalk(
        0xFE,
        "Welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm not very good at talking\x01",
            "with customers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I generally let my wife handle\x01",
            "that part of the job.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22F0")

    TalkEnd(0xFE)
    Return()

    # Function_7_1C0A end

    def Function_8_22F4(): pass

    label("Function_8_22F4")

    Call(0, 9)
    Return()

    # Function_8_22F4 end

    def Function_9_22F9(): pass

    label("Function_9_22F9")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2365")
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_235A")
    OP_A9(0x60)
    Jump("loc_235C")

    label("loc_235A")

    OP_A9(0x5B)

    label("loc_235C")

    OP_56(0x0)
    TalkEnd(0xA)
    Return()

    label("loc_2365")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2376")
    TalkEnd(0xA)
    Return()

    label("loc_2376")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_2464")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 2)), scpexpr(EXPR_END)), "loc_23D8")

    ChrTalk(
        0xA,
        (
            "I'm glad Her Majesty has gotten\x01",
            "better.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "The kingdom can rest easy now.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2461")

    label("loc_23D8")


    ChrTalk(
        0xA,
        (
            "Queen Alicia and Princess Klaudia\x01",
            "were so radiant!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'm glad Her Majesty has gotten\x01",
            "better.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "The kingdom can rest easy now.\x02",
    )

    CloseMessageWindow()

    label("loc_2461")

    Jump("loc_3530")

    label("loc_2464")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_24CF")

    ChrTalk(
        0xA,
        (
            "We haven't had many customers\x01",
            "today, and it's rather odd, since\x01",
            "the weather's quite nice...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3530")

    label("loc_24CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_260D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 2)), scpexpr(EXPR_END)), "loc_2544")

    ChrTalk(
        0xA,
        (
            "With Her Majesty still sick, I just\x01",
            "have no idea what will become of her\x01",
            "Birthday Celebration.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_260A")

    label("loc_2544")


    ChrTalk(
        0xA,
        (
            "Those black-armored soldiers\x01",
            "have been all over the town\x01",
            "lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "...Such a commotion...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "With Her Majesty still sick, I just\x01",
            "have no idea what will become of her\x01",
            "Birthday Celebration.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_260A")

    Jump("loc_3530")

    label("loc_260D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_2890")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 2)), scpexpr(EXPR_END)), "loc_278E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_26A1")

    ChrTalk(
        0xA,
        (
            "That was the fiercest fight\x01",
            "I've seen in many years.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I was extremely impressed. You\x01",
            "may count me among your fans.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_278B")

    label("loc_26A1")

    OP_A2(0x1)

    ChrTalk(
        0xA,
        "You did wonderful out there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Congratulations on your victory.\x01",
            "That was some incredible match!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It was the fiercest fight I've\x01",
            "seen in many years.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "I was extremely impressed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "You may count me among your fans.\x02",
    )

    CloseMessageWindow()

    label("loc_278B")

    Jump("loc_288D")

    label("loc_278E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_27F4")

    ChrTalk(
        0xA,
        (
            "Today's final match was simply\x01",
            "amazing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'm so glad I took off work to\x01",
            "go see it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_288D")

    label("loc_27F4")

    OP_A2(0x1)

    ChrTalk(
        0xA,
        (
            "Today's final match was simply\x01",
            "amazing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "That was the fiercest fight\x01",
            "I've seen in many years.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'm so glad I took off work to\x01",
            "go see it!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_288D")

    Jump("loc_3530")

    label("loc_2890")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_29B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 2)), scpexpr(EXPR_END)), "loc_2941")

    ChrTalk(
        0xA,
        (
            "Oh, it's you guys. So, today's\x01",
            "the final match, no?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'm just about to close shop, and then\x01",
            "I'll be heading out to cheer for you--\x01",
            "louder than anyone!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29B3")

    label("loc_2941")


    ChrTalk(
        0xA,
        (
            "The final day of the tournament\x01",
            "already? My, how time flies...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I hope I can go see some of the\x01",
            "matches!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29B3")

    Jump("loc_3530")

    label("loc_29B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_2D1A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2A25")

    ChrTalk(
        0xA,
        (
            "If you want my advice, you should\x01",
            "turn in early tonight. Rest up real\x01",
            "good for tomorrow!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D17")

    label("loc_2A25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2C93")
    OP_A2(0x1)
    OP_A2(0x67B)

    ChrTalk(
        0xA,
        "Oh, hey, it's you guys...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I hear you made it to the finals.\x01",
            "Congratulations!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001FThanks!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FThank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Apparently, you were quite the\x01",
            "showstoppers, too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "And I was cheering for you, of course, so\x01",
            "I can hold my nose up high for a while.\x01",
            "Chaeli's team's gonna take it all!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006FHeh heh! Now it's just a hop, skip\x01",
            "and a jump to full-on victory!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#018F(Yeah, like it's really that\x01",
            "easy...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Well, you've gotten this far... Don't see\x01",
            "why you WOULDN'T win the championship.\x01",
            "I mean, you guys got the GOODS, yo!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Best of luck to you-- not that\x01",
            "you'll need it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D17")

    label("loc_2C93")

    OP_A2(0x1)

    ChrTalk(
        0xA,
        (
            "Everyone is saying that today's\x01",
            "match was a real keeper.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "You can FEEL their excitement\x01",
            "as they recount every detail...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D17")

    Jump("loc_3530")

    label("loc_2D1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_30E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 2)), scpexpr(EXPR_END)), "loc_2D9B")

    ChrTalk(
        0xA,
        (
            "We're going to close the shop\x01",
            "and go watch the finals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Best of luck to you-- not that\x01",
            "you'll need it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30E0")

    label("loc_2D9B")

    OP_A2(0x67A)

    ChrTalk(
        0xA,
        "Hmmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Are you participants in the Martial\x01",
            "Arts Competition, by any chance?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#073FActually, yes we are.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "I knew it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'd heard about a team with one\x01",
            "big dude, one little dude and\x01",
            "a rough-and-tumble little lady.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "You guys totally have my support.\x01",
            "I'll be cheering for you louder\x01",
            "than anyone!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008FReally? Wow, thanks! I'll be sure\x01",
            "to listen for you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Yaaay! So, can I get your autographs?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004FOur a-autographs? Seriously?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019FI...don't even know what to say.\x01",
            "No one's ever asked me for my\x01",
            "autograph before...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Usually I'm working, so I can't\x01",
            "get to the arena.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "But we're going to close up shop\x01",
            "to go see the final match.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I sure hope it turns out you'll\x01",
            "be in it, so we can see you guys\x01",
            "in action!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001FYou bet! It doesn't matter who we\x01",
            "face, we'll be there, for sure!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30E0")

    Jump("loc_3530")

    label("loc_30E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_31BA")

    ChrTalk(
        0xA,
        (
            "Usually the military leaves everyone else\x01",
            "in the dust, but this year...it's hard to\x01",
            "say, with so many entrants!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I can't wait to find out who\x01",
            "wins. It's going to be the best\x01",
            "tournament year EVER!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3530")

    label("loc_31BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_334E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_326F")

    ChrTalk(
        0xA,
        (
            "Yesterday, some people in handcuffs\x01",
            "were escorted into the shop by\x01",
            "soldiers...to buy weapons!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Don't you usually try to take\x01",
            "weapons AWAY from criminals?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_334B")

    label("loc_326F")

    OP_A2(0x1)

    ChrTalk(
        0xA,
        (
            "Yesterday, some people in handcuffs\x01",
            "were escorted into the shop by\x01",
            "soldiers...to buy weapons!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Don't you usually try to take\x01",
            "weapons AWAY from criminals?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'd really love to know who\x01",
            "the heck they were!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_334B")

    Jump("loc_3530")

    label("loc_334E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_34E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_33F4")

    ChrTalk(
        0xA,
        (
            "The sub-commander of the Royal\x01",
            "Guardsman used to come in here\x01",
            "all the time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "He was always concerned about Her\x01",
            "Majesty. Such a nice person!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34DD")

    label("loc_33F4")

    OP_A2(0x1)

    ChrTalk(
        0xA,
        (
            "Still can't believe the Royal\x01",
            "Guardsman were behind the terro-\x01",
            "rist attack.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "The sub-commander of the Royal\x01",
            "Guardsman used to come in here\x01",
            "all the time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "He was always concerned about Her\x01",
            "Majesty. Such a nice person!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34DD")

    Jump("loc_3530")

    label("loc_34E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_3530")

    ChrTalk(
        0xA,
        "Braaaaaacers! Welcome to the shop!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Please, have a look around!\x02",
    )

    CloseMessageWindow()

    label("loc_3530")

    TalkEnd(0xA)
    Return()

    # Function_9_22F9 end

    def Function_10_3534(): pass

    label("Function_10_3534")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_38CC")
    EventBegin(0x0)
    Fade(1000)
    OP_6D(4690, 4000, -2480, 0)
    SetChrPos(0x101, 4350, 4000, -2160, 90)
    SetChrPos(0x102, 4390, 4000, -3250, 90)
    SetChrPos(0x108, 3200, 4000, -2630, 90)
    TurnDirection(0x8, 0x108, 0)
    OP_A2(0x64B)
    OP_28(0x4B, 0x1, 0x20)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4B, 0x1, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x4B, 0x1, 0x20)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x4B, 0x1, 0x40)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x4B, 0x1, 0x80)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_35C7")
    OP_28(0x4B, 0x1, 0x100)

    label("loc_35C7")

    OP_0D()
    SetChrSubChip(0xFE, 0)

    ChrTalk(
        0x101,
        "#004FHi, Carna!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#830FHey, look who it is!\x02\x03",
            "Ooh, you've got old man Zane\x01",
            "with you. What's going on?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#074FWell, it's a long story...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#832FUh-oh. Sounds serious.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Explained the situation and the queen's request to Carna.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x8,
        (
            "#832F...Uhh...\x02\x03",
            "...You're not just pulling my\x01",
            "leg, are you?\x02\x03",
            "#833FI must admit, I did find it a bit\x01",
            "odd that all the gates and ports\x01",
            "and such have been shut down...\x02\x03",
            "#832FSooo, what did you want with me,\x01",
            "exactly?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012FWell, we need to get everyone\x01",
            "together and formulate a plan.\x02\x03",
            "So if you would, please meet us\x01",
            "at the guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#832FGotcha.\x02\x03",
            "I'm already there!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3850():

        label("loc_3850")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_3850")

    QueueWorkItem2(0x101, 1, lambda_3850)

    def lambda_3861():

        label("loc_3861")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_3861")

    QueueWorkItem2(0x102, 1, lambda_3861)

    def lambda_3872():

        label("loc_3872")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_3872")

    QueueWorkItem2(0x108, 1, lambda_3872)
    OP_8E(0x8, 0x1522, 0xFA0, 0x276, 0xFA0, 0x0)
    OP_8E(0x8, 0xC58, 0xFA0, 0x9F6, 0xFA0, 0x0)
    OP_8E(0x8, 0xFFFFF254, 0x0, 0x9F6, 0xFA0, 0x0)
    SetChrFlags(0x8, 0x80)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x108, 0xFF)
    EventEnd(0x0)

    label("loc_38CC")

    TalkEnd(0x8)
    Return()

    # Function_10_3534 end

    SaveToFile()

Try(main)
