from ED6ScenarioHelper import *

def main():
    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4135   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4135.x',
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
        'Museum Director',                      # 9
        'Santos',                               # 10
        'Licia',                                # 11
        'Professor Alba',                       # 12
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
        'ED6_DT07/CH01490 ._CH',             # 00
        'ED6_DT07/CH01660 ._CH',             # 01
        'ED6_DT07/CH01540 ._CH',             # 02
        'ED6_DT07/CH02050 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT07/CH01490P._CP',             # 00
        'ED6_DT07/CH01660P._CP',             # 01
        'ED6_DT07/CH01540P._CP',             # 02
        'ED6_DT07/CH02050P._CP',             # 03
    )

    DeclNpc(
        X                   = 1890,
        Z                   = 0,
        Y                   = 77500,
        Direction           = 171,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -69000,
        Z                   = 0,
        Y                   = -2520,
        Direction           = 79,
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
        X                   = 4400,
        Z                   = 0,
        Y                   = -5910,
        Direction           = 255,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 470,
        Z                   = 0,
        Y                   = -3730,
        Direction           = 282,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )


    DeclActor(
        TriggerX            = 2580,
        TriggerZ            = 0,
        TriggerY            = -5970,
        TriggerRange        = 800,
        ActorX              = 4400,
        ActorZ              = 1700,
        ActorY              = -5910,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 5090,
        TriggerZ            = 0,
        TriggerY            = 2190,
        TriggerRange        = 800,
        ActorX              = 5090,
        ActorZ              = 800,
        ActorY              = 2190,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 7840,
        TriggerZ            = 4000,
        TriggerY            = 6700,
        TriggerRange        = 800,
        ActorX              = 7840,
        ActorZ              = 5700,
        ActorY              = 6700,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 75860,
        TriggerZ            = 0,
        TriggerY            = -2000,
        TriggerRange        = 800,
        ActorX              = 75860,
        ActorZ              = 1500,
        ActorY              = -2000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 73200,
        TriggerZ            = 0,
        TriggerY            = 710,
        TriggerRange        = 800,
        ActorX              = 73200,
        ActorZ              = 800,
        ActorY              = 710,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 68740,
        TriggerZ            = 0,
        TriggerY            = 7310,
        TriggerRange        = 800,
        ActorX              = 68740,
        ActorZ              = 800,
        ActorY              = 7310,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 73480,
        TriggerZ            = 0,
        TriggerY            = 6420,
        TriggerRange        = 800,
        ActorX              = 73480,
        ActorZ              = 800,
        ActorY              = 6420,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 75820,
        TriggerZ            = 4000,
        TriggerY            = 8010,
        TriggerRange        = 800,
        ActorX              = 75820,
        ActorZ              = 5700,
        ActorY              = 8010,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 71960,
        TriggerZ            = 4000,
        TriggerY            = 9290,
        TriggerRange        = 800,
        ActorX              = 71960,
        ActorZ              = 4800,
        ActorY              = 9290,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 15,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -20,
        TriggerZ            = 0,
        TriggerY            = 77880,
        TriggerRange        = 800,
        ActorX              = -20,
        ActorZ              = 1700,
        ActorY              = 77880,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 16,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -770,
        TriggerZ            = 0,
        TriggerY            = 72650,
        TriggerRange        = 800,
        ActorX              = -770,
        ActorZ              = 800,
        ActorY              = 72650,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 17,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 7000,
        TriggerZ            = 0,
        TriggerY            = 66550,
        TriggerRange        = 1200,
        ActorX              = 7000,
        ActorZ              = 800,
        ActorY              = 66550,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 18,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 1770,
        TriggerZ            = 0,
        TriggerY            = 66890,
        TriggerRange        = 800,
        ActorX              = 1770,
        ActorZ              = 800,
        ActorY              = 66890,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 19,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -3790,
        TriggerZ            = 0,
        TriggerY            = 64959,
        TriggerRange        = 800,
        ActorX              = -3790,
        ActorZ              = 800,
        ActorY              = 64959,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 20,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_342",          # 00, 0
        "Function_1_514",          # 01, 1
        "Function_2_561",          # 02, 2
        "Function_3_577",          # 03, 3
        "Function_4_1A6B",         # 04, 4
        "Function_5_1A70",         # 05, 5
        "Function_6_2285",         # 06, 6
        "Function_7_2FE0",         # 07, 7
        "Function_8_3AD7",         # 08, 8
        "Function_9_3C78",         # 09, 9
        "Function_10_3E20",        # 0A, 10
        "Function_11_3FCD",        # 0B, 11
        "Function_12_40BC",        # 0C, 12
        "Function_13_41A9",        # 0D, 13
        "Function_14_4299",        # 0E, 14
        "Function_15_4378",        # 0F, 15
        "Function_16_4458",        # 10, 16
        "Function_17_45F1",        # 11, 17
        "Function_18_477F",        # 12, 18
        "Function_19_48B0",        # 13, 19
        "Function_20_4977",        # 14, 20
    )


    def Function_0_342(): pass

    label("Function_0_342")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_362")
    SetChrPos(0x9, -69600, 0, 3910, 71)
    SetChrFlags(0xB, 0x80)
    Jump("loc_513")

    label("loc_362")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_393")
    SetChrFlags(0x8, 0x80)
    SetChrPos(0x9, -72260, 0, -3090, 183)
    SetChrPos(0xB, -73180, 0, 58630, 225)
    Jump("loc_513")

    label("loc_393")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_3C4")
    SetChrFlags(0x8, 0x80)
    SetChrPos(0x9, -75330, 0, 2770, 173)
    SetChrPos(0xB, -73180, 0, 58630, 225)
    Jump("loc_513")

    label("loc_3C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_3F5")
    SetChrFlags(0x8, 0x80)
    SetChrPos(0x9, -69770, 0, 6640, 341)
    SetChrPos(0xB, -73180, 0, 58630, 225)
    Jump("loc_513")

    label("loc_3F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_415")
    SetChrPos(0xB, -73180, 0, 58630, 225)
    SetChrFlags(0xB, 0x80)
    Jump("loc_513")

    label("loc_415")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_441")
    SetChrPos(0x9, -69200, 0, 0, 111)
    SetChrPos(0xB, -73180, 0, 58630, 225)
    Jump("loc_513")

    label("loc_441")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_46D")
    SetChrPos(0x9, 70400, 0, 3610, 0)
    SetChrPos(0xB, -72380, 0, -1410, 254)
    Jump("loc_513")

    label("loc_46D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_499")
    SetChrPos(0x9, -72260, 0, -3090, 183)
    SetChrPos(0xB, 69350, 0, 6420, 315)
    Jump("loc_513")

    label("loc_499")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_4C5")
    SetChrPos(0x9, -75330, 0, 2770, 173)
    SetChrPos(0xB, 72040, 0, 2370, 109)
    Jump("loc_513")

    label("loc_4C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_4F1")
    SetChrPos(0x9, -69770, 0, 6640, 341)
    SetChrPos(0xB, 3520, 0, 1550, 57)
    Jump("loc_513")

    label("loc_4F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_513")
    SetChrPos(0x8, -1010, 0, -3780, 75)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0xB, 0x10)

    label("loc_513")

    Return()

    # Function_0_342 end

    def Function_1_514(): pass

    label("Function_1_514")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_547")
    OP_B1("t4135_y")
    Jump("loc_550")

    label("loc_547")

    OP_B1("t4135_n")

    label("loc_550")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 2)), scpexpr(EXPR_END)), "loc_560")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x4B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_560")

    Return()

    # Function_1_514 end

    def Function_2_561(): pass

    label("Function_2_561")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_576")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_561")

    label("loc_576")

    Return()

    # Function_2_561 end

    def Function_3_577(): pass

    label("Function_3_577")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_584")
    Jump("loc_1A67")

    label("loc_584")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_7C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_68C")
    TurnDirection(0xB, 0x102, 400)

    ChrTalk(
        0xB,
        (
            "#130FYou know, I've always said the harder the\x01",
            "job, the better off you are just taking it\x01",
            "easy. That's the key to true success.\x02\x03",
            "#132FHahaha... Maybe that means I have\x01",
            "the world's hardest job, because\x01",
            "let me tell you, I take it EA-SY!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7C3")

    label("loc_68C")

    OP_A2(0x3)
    TurnDirection(0xB, 0x102, 400)

    ChrTalk(
        0xB,
        (
            "#130FHello, Joshua.\x02\x03",
            "You seem stressed. Is something\x01",
            "the matter?\x02\x03",
            "You know, I've always said the harder the\x01",
            "job, the better off you are just taking it\x01",
            "easy. That's the key to true success.\x02\x03",
            "#132FHahaha... Maybe that means I have\x01",
            "the world's hardest job, because\x01",
            "let me tell you, I take it EA-SY!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7C3")

    Jump("loc_1A67")

    label("loc_7C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_BDF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_87B")

    ChrTalk(
        0xB,
        (
            "#132FI'm very curious as to what it's\x01",
            "like inside the castle...\x02\x03",
            "...but I'm afraid I'll have to wait\x01",
            "until it's reopened to find out, just\x01",
            "like everyone else.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BDC")

    label("loc_87B")

    OP_A2(0x3)

    ChrTalk(
        0xB,
        (
            "#130FLiberl's history is quite long--\x01",
            "and more than a little sordid!\x02\x03",
            "Its roots go back more than a\x01",
            "thousand years, as I understand\x01",
            "it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004FWait... Liberl's only been Liberl as long as\x01",
            "the royal family's been around, so are you\x01",
            "telling me the royal family is THAT old?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#132FThey are. And I, for one, would love\x01",
            "to tour the inside of that castle...\x01",
            "see what ghosts I could dig up.\x02\x03",
            "You two got to see the inside\x01",
            "of it yesterday, did you not?\x02\x03",
            "Tell me, what was it like?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505FWell, uh...\x02\x03",
            "It felt pretty old and historic,\x01",
            "I guess...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FThere was definitely a lot to\x01",
            "see in there.\x02\x03",
            "But we weren't really given much\x01",
            "of a chance to see it.\x02\x03",
            "I'm afraid there's nothing we can\x01",
            "really tell you that you wouldn't\x01",
            "already know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#131FI see, I see...\x02\x03",
            "That's too bad. I suppose I'll\x01",
            "have to wait until the castle\x01",
            "is reopened to the public.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BDC")

    Jump("loc_1A67")

    label("loc_BDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_11A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_C6A")

    ChrTalk(
        0xFE,
        (
            "#132FThanks to your help, my research\x01",
            "is progressing quite nicely.\x02\x03",
            "I may even be able to publish\x01",
            "some results soon!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11A6")

    label("loc_C6A")

    OP_A2(0x3)

    ChrTalk(
        0xB,
        (
            "#130FAh, Estelle! Joshua!\x02\x03",
            "#132FThat was an incredible match.\x01",
            "Congratulations on your victory!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001FAwww, shucks. Tweren't nothin'!\x02\x03",
            "...How have you been, Professor\x01",
            "Alba?\x02\x03",
            "Found the meaning of life yet?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#130FNot quite. Though that old text the\x01",
            "museum asked me to decipher IS coming\x01",
            "along rather nicely.\x02\x03",
            "I also stumbled upon quite a few books I've\x01",
            "been meaning to reference in my research.\x01",
            "So overall, it's been a successful day!\x02\x03",
            "Still...I have more work than I\x01",
            "have time to do it. But, isn't\x01",
            "that always the way?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004FWow. I'm impressed, I must admit!\x02\x03",
            "#007FI guess that's the kind of dedication\x01",
            "it takes to be a professor.\x02\x03",
            "I sure couldn't do it, that's\x01",
            "for sure!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FHeh. You could never stay in your seat\x01",
            "for more than a minute at a time-- never\x01",
            "mind actually doing research!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007FYeah, like I keep saying, sitting still\x01",
            "always makes me sleepy. I have to move\x01",
            "around just to stay awake!\x02\x03",
            "#001FI'm like those fish. You know, \x01",
            "the ones that die if they don't\x01",
            "keep swimming?\x02\x03",
            "I gotta keep on swimming, forever\x01",
            "and always, right through this\x01",
            "aquarium called life! You know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#018F...Uh, sure...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#509FStop looking at me like that!\x01",
            "That was poetic, man!\x02\x03",
            "#506F...Anyway, I'm glad to hear\x01",
            "your research is going well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#132FI owe it all to you.\x02\x03",
            "I may even be able to publish\x01",
            "some results soon!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11A6")

    Jump("loc_1A67")

    label("loc_11A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_129D")

    ChrTalk(
        0xB,
        (
            "#130FI've been buried in records for\x01",
            "three straight days. Haven't even\x01",
            "laid eyes on the sun!\x02\x03",
            "The life of a professor is an\x01",
            "exhausting one sometimes. Perhaps\x01",
            "I'll step out for a bit...\x02\x03",
            "Treat myself to an ice cream\x01",
            "or something!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A67")

    label("loc_129D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_1369")

    ChrTalk(
        0xB,
        (
            "#130FI finally stumbled upon quite a few books I've\x01",
            "been meaning to reference in my research. It's\x01",
            "been a very successful day!\x02\x03",
            "I've just got to get to cracking\x01",
            "these old languages, now...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A67")

    label("loc_1369")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_14D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_13F0")

    ChrTalk(
        0xB,
        (
            "#130FHo ho, an artifact untainted by \x01",
            "public display?\x02\x03",
            "How exquisite! How remarkable!\x01",
            "How positively energizing!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14D4")

    label("loc_13F0")

    OP_A2(0x3)

    ChrTalk(
        0xB,
        (
            "#130FHo ho, an artifact untainted by \x01",
            "public display?\x02\x03",
            "What treasures lie within its depths?\x01",
            "Be they riches of money or mind, their\x01",
            "secrets I shall surely find!\x02\x03",
            "How exquisite! How remarkable!\x01",
            "How positively energizing!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14D4")

    Jump("loc_1A67")

    label("loc_14D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1715")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1581")

    ChrTalk(
        0xB,
        (
            "#130FImagination is a key part of an archaeologist's\x01",
            "work. After finding an artifact, the real trick\x01",
            "is learning what it is and why it's important!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1712")

    label("loc_1581")

    OP_A2(0x3)

    ChrTalk(
        0xB,
        (
            "#130FMy, my... Everything is just so\x01",
            "very, very fascinating!\x02\x03",
            "That relief over there is from\x01",
            "before the Great Collapse-- if\x01",
            "you can believe it!\x02\x03",
            "Has the same sort of feel to it\x01",
            "as something you'd find inside the\x01",
            "Tetracyclic Towers, don't you think?\x02\x03",
            "Imagination is a key part of an archaeologist's\x01",
            "work. After finding an artifact, the real trick\x01",
            "is learning what it is and why it's important!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1712")

    Jump("loc_1A67")

    label("loc_1715")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_18D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_17DB")

    ChrTalk(
        0xFE,
        (
            "#132FThere's a good chance that the\x01",
            "ruins dotting Liberl are from\x01",
            "the ancient Zemurians.\x02\x03",
            "I have the actual testing done;\x01",
            "now all I need is some time to\x01",
            "translate and collate.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18D5")

    label("loc_17DB")

    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "#130FAir-Letten in Ruan...\x02\x03",
            "Ahnenburg in Grancel...\x02\x03",
            "The Tetracyclic Towers...\x02\x03",
            "#132F...It's a real possibility that\x01",
            "these are all ancient Zemurian\x01",
            "ruins.\x02\x03",
            "I have the actual testing done;\x01",
            "now all I need is some time to\x01",
            "translate and collate.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18D5")

    Jump("loc_1A67")

    label("loc_18D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_1A48")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_195E")

    ChrTalk(
        0xB,
        (
            "#130FI'd like to start my research,\x01",
            "but I also really want to go see\x01",
            "the sights...\x02\x03",
            "Ahhh, decisions, decisions!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A45")

    label("loc_195E")

    OP_A2(0x3)

    ChrTalk(
        0xB,
        (
            "#130FGrancel is an amazing city.\x02\x03",
            "Even with a high terror alert,\x01",
            "all these people have come out\x01",
            "just to celebrate!\x02\x03",
            "I'd like to start my research,\x01",
            "but I also really want to go see\x01",
            "the sights...\x02\x03",
            "Ahhh, decisions, decisions!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A45")

    Jump("loc_1A67")

    label("loc_1A48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1A67")

    ChrTalk(
        0xB,
        "#130FMuch obliged.\x02",
    )

    CloseMessageWindow()

    label("loc_1A67")

    TalkEnd(0xFE)
    Return()

    # Function_3_577 end

    def Function_4_1A6B(): pass

    label("Function_4_1A6B")

    Call(0, 5)
    Return()

    # Function_4_1A6B end

    def Function_5_1A70(): pass

    label("Function_5_1A70")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_1AEB")

    ChrTalk(
        0xA,
        (
            "Now where did Professor Alba\x01",
            "get off to?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I had a question for him about\x01",
            "his special study course...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2281")

    label("loc_1AEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_1BC4")

    ChrTalk(
        0xA,
        (
            "Something doesn't seem right\x01",
            "out there today. Can't put my\x01",
            "finger on what it is...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It's quiet...TOO quiet...and it's been\x01",
            "so raucous lately, this silence is all\x01",
            "the more deafening by comparison...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2281")

    label("loc_1BC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_1DE1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1CAF")

    ChrTalk(
        0xA,
        (
            "What do you think will happen with\x01",
            "the Queen's Birthday Celebration?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It's going to be canceled for sure, don't you\x01",
            "think? I mean, they wouldn't celebrate if the\x01",
            "queen's still sick. They couldn't! Could they?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DDE")

    label("loc_1CAF")

    OP_A2(0x2)

    ChrTalk(
        0xA,
        (
            "Now that the competition's wrapped up,\x01",
            "the streets should get a bit quieter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "What do you think will happen with\x01",
            "the Queen's Birthday Celebration?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It's going to be canceled for sure, don't you\x01",
            "think? I mean, they wouldn't celebrate if the\x01",
            "queen's still sick. They couldn't! Could they?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DDE")

    Jump("loc_2281")

    label("loc_1DE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_1E95")

    ChrTalk(
        0xA,
        (
            "The tournament's done, and nobody\x01",
            "lost any limbs. I'd call that a\x01",
            "win overall!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'm a little jealous of Professor Alba, who\x01",
            "actually got to see the final match.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2281")

    label("loc_1E95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1EFA")

    ChrTalk(
        0xA,
        "The final bout is today, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I really wish I could go watch\x01",
            "the fight. *sigh*\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2281")

    label("loc_1EFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_1F99")

    ChrTalk(
        0xA,
        (
            "A package postmarked from Bose\x01",
            "arrived for the director just\x01",
            "a moment ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If you'll excuse me, I need to\x01",
            "make sure he gets it right away!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2281")

    label("loc_1F99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_206D")

    ChrTalk(
        0xA,
        (
            "Smoking and photography are prohibited in\x01",
            "the museum. If you're a shutterbug or a\x01",
            "nicotine fiend, please take it outside!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "We pride ourselves on our sense of\x01",
            "mystique and...lack of smoke odor.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2281")

    label("loc_206D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2104")

    ChrTalk(
        0xA,
        (
            "There are a lot of...strange\x01",
            "people amongst the scholars\x01",
            "I deal with on a daily basis.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "But Professor Alba? He's just...\x01",
            "a mystery.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2281")

    label("loc_2104")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_214D")

    ChrTalk(
        0xA,
        (
            "I doubt we'll have many visitors\x01",
            "during the tournament...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2281")

    label("loc_214D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_21E9")

    ChrTalk(
        0xA,
        (
            "I've seen a lot of Royal Army\x01",
            "soldiers in the town lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I wonder if it's because their\x01",
            "airship is grounded and they're\x01",
            "just bored...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2281")

    label("loc_21E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_2281")

    ChrTalk(
        0xA,
        (
            "Welcome to the Grancel Museum\x01",
            "of History!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Our newest exhibit, 'Liberl &\x01",
            "the Modernist Wave,' is now open\x01",
            "to the public. It's gripping!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2281")

    TalkEnd(0xA)
    Return()

    # Function_5_1A70 end

    def Function_6_2285(): pass

    label("Function_6_2285")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_2303")

    ChrTalk(
        0xFE,
        "It sure is lively outside!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After I finish work, I might\x01",
            "go out there and get a bit...\x01",
            "lively...myself.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FDC")

    label("loc_2303")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_246E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_23AB")

    ChrTalk(
        0xFE,
        (
            "We had some Royal Army soldiers\x01",
            "in here earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They were asking around if we'd\x01",
            "seen any troops from the Royal\x01",
            "Guard. Kind of alarming, no?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_246B")

    label("loc_23AB")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "We had some Royal Army soldiers\x01",
            "in here yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They were asking around if we'd\x01",
            "seen any troops from the Royal\x01",
            "Guard. Kind of alarming, no?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "They looked really frustrated.\x02",
    )

    CloseMessageWindow()

    label("loc_246B")

    Jump("loc_2FDC")

    label("loc_246E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_2595")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2501")

    ChrTalk(
        0xFE,
        (
            "I got a letter from the museum\x01",
            "director in Bose...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Apparently, he's stuck there,\x01",
            "thanks to the airships being\x01",
            "grounded.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2592")

    label("loc_2501")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "I got a letter from the museum\x01",
            "director in Bose...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Apparently, he's stuck there,\x01",
            "thanks to the airships being\x01",
            "grounded.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*sigh*\x02",
    )

    CloseMessageWindow()

    label("loc_2592")

    Jump("loc_2FDC")

    label("loc_2595")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_25FD")

    ChrTalk(
        0xFE,
        (
            "The Museum Director's been\x01",
            "called out on another project.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I think he's in Bose now.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2FDC")

    label("loc_25FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_26DE")

    ChrTalk(
        0xFE,
        (
            "Professor Alba got a ticket from\x01",
            "the director for the final match\x01",
            "of the competition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Wish I were so lucky!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Guess it doesn't matter. It's not\x01",
            "like I have any time for that, with\x01",
            "my workload as it is!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FDC")

    label("loc_26DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_28F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_27A1")

    ChrTalk(
        0xFE,
        (
            "Did you know that long ago, at the height\x01",
            "of ancient civilization, humans lived side-\x01",
            "by-side with other intelligent beings?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We refer to them as the 'ancient\x01",
            "dragons.'\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28ED")

    label("loc_27A1")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "Did you know that long ago, at the height\x01",
            "of ancient civilization, humans lived side-\x01",
            "by-side with other intelligent beings?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We refer to them as the 'ancient\x01",
            "dragons.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Their descendants were known to be living in the\x01",
            "Bose region as recently as a few decades ago, but\x01",
            "we haven't had any sightings of them recently.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28ED")

    Jump("loc_2FDC")

    label("loc_28F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_2A5A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2991")

    ChrTalk(
        0xFE,
        (
            "This was found sunken in the\x01",
            "depths of Lake Valleria.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Seems there's an entire set of\x01",
            "ruins at the bottom of Lake\x01",
            "Valleria, amazingly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A57")

    label("loc_2991")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "This was found sunken in the\x01",
            "depths of Lake Valleria.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It was caught by chance in a\x01",
            "fisherman's net.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Seems there's an entire set of\x01",
            "ruins at the bottom of Lake\x01",
            "Valleria, amazingly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A57")

    Jump("loc_2FDC")

    label("loc_2A5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2C25")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2B36")

    ChrTalk(
        0xFE,
        (
            "Those who survived the Great\x01",
            "Collapse had quite a harrowing\x01",
            "road ahead of them!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's thanks to the Orbal Revolution,\x01",
            "though, that our lives are as convenient\x01",
            "and comfortable as they are today.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C22")

    label("loc_2B36")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "Those who survived the Great\x01",
            "Collapse had quite a harrowing\x01",
            "road ahead of them!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Wars, poverty, famine...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's thanks to the Orbal Revolution,\x01",
            "though, that our lives are as convenient\x01",
            "and comfortable as they are today.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C22")

    Jump("loc_2FDC")

    label("loc_2C25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_2CCA")

    ChrTalk(
        0xFE,
        (
            "We have almost no records of\x01",
            "anything prior to the Great\x01",
            "Collapse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "All we know is that society\x01",
            "as a whole was much more\x01",
            "advanced than it is now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FDC")

    label("loc_2CCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_2EC8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2D93")

    ChrTalk(
        0xFE,
        (
            "We usually offer a special\x01",
            "assembly for visitors...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...but with all the bustle of the Martial\x01",
            "Arts Competition and the Birthday Celebration,\x01",
            "I'm afraid it's been called off.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EC5")

    label("loc_2D93")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "We usually offer a special\x01",
            "assembly for visitors...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...but with all the bustle of the Martial\x01",
            "Arts Competition and the Birthday Celebration,\x01",
            "I'm afraid it's been called off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Why, you ask?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Do you even HAVE to ask? I mean...\x01",
            "who would actually show up to something\x01",
            "like that TODAY?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EC5")

    Jump("loc_2FDC")

    label("loc_2EC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_2FDC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2F12")

    ChrTalk(
        0xFE,
        (
            "The museum's job isn't just\x01",
            "to show off old relics.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FDC")

    label("loc_2F12")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "The museum's job isn't just\x01",
            "to show off old relics.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We're also responsible for collecting,\x01",
            "cataloging and storing all of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And we work with researchers\x01",
            "like Professor Alba, as well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FDC")

    TalkEnd(0xFE)
    Return()

    # Function_6_2285 end

    def Function_7_2FE0(): pass

    label("Function_7_2FE0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_3094")

    ChrTalk(
        0xFE,
        (
            "Imagine my surprise when I found\x01",
            "myself stuck in Bose with no way\x01",
            "home!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A lot of things happened in my\x01",
            "absence, but the museum is,\x01",
            "thankfully, still intact.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AD3")

    label("loc_3094")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_309E")
    Jump("loc_3AD3")

    label("loc_309E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_30A8")
    Jump("loc_3AD3")

    label("loc_30A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_30B2")
    Jump("loc_3AD3")

    label("loc_30B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_3301")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3196")

    ChrTalk(
        0xFE,
        (
            "I'm going to Bose, you see. I have\x01",
            "a meeting with a scholar who's a\x01",
            "specialist in ancient studies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've got to catch an afternoon flight,\x01",
            "so regrettably, I won't be able to go\x01",
            "to the tournament today.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32FE")

    label("loc_3196")

    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "I was so looking forward to the\x01",
            "final match, too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm going to Bose, you see. I have\x01",
            "a meeting with a scholar who's a\x01",
            "specialist in ancient studies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've got to catch an afternoon flight,\x01",
            "so regrettably, I won't be able to go\x01",
            "to the tournament today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I didn't particularly want to\x01",
            "part with it, but I gave my\x01",
            "ticket to Professor Alba.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32FE")

    Jump("loc_3AD3")

    label("loc_3301")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_33AD")

    ChrTalk(
        0xFE,
        (
            "Tomorrow, I was thinking of taking\x01",
            "in the tournament's final match.\x01",
            "It should be an exciting one!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My ticket has already been secured,\x01",
            "so now...we wait!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AD3")

    label("loc_33AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_3585")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3471")

    ChrTalk(
        0xFE,
        (
            "I would be delighted if this museum\x01",
            "were to double as an academic repository\x01",
            "for ancient artifacts...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But the church refuses to even\x01",
            "acknowledge receipt of my requests!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3582")

    label("loc_3471")

    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "It's said these artifacts have\x01",
            "some kind of tie to the ancient\x01",
            "Zemurian civilization.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I would be delighted if this museum\x01",
            "were to double as an academic repository\x01",
            "for ancient artifacts...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But the church refuses to even\x01",
            "acknowledge receipt of my requests!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3582")

    Jump("loc_3AD3")

    label("loc_3585")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_36D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_361F")

    ChrTalk(
        0xFE,
        (
            "Professor Alba has kindly agreed\x01",
            "to study some of our undisplayed\x01",
            "archaeological finds.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They may hold some historical\x01",
            "insight.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36CD")

    label("loc_361F")

    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "Professor Alba is truly a great\x01",
            "man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He has kindly agreed to study some\x01",
            "of our undisplayed archaeological\x01",
            "finds.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They may bear untold historical\x01",
            "insight...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36CD")

    Jump("loc_3AD3")

    label("loc_36D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_3997")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_37CE")

    ChrTalk(
        0xFE,
        (
            "There are those who dismiss the Sept-Terrions\x01",
            "as the things of myth and fairytale...\x01",
            "but I'm not convinced!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We've found numerous relics within the\x01",
            "ruins throughout this land that seem to\x01",
            "suggest a Zemurian origin, after all...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3994")

    label("loc_37CE")

    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "The ancients spoke of the Sept-Terrions--\x01",
            "seven powerful items dropped from heaven\x01",
            "above, concealing a mystical power within them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But we've no sources to identify\x01",
            "just what these powers actually\x01",
            "were...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There are those who dismiss the Sept-Terrions\x01",
            "as the things of myth and fairytale...\x01",
            "but I'm not convinced!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We've found numerous relics within the\x01",
            "ruins throughout this land that seem to\x01",
            "suggest a Zemurian origin, after all...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3994")

    Jump("loc_3AD3")

    label("loc_3997")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_3A71")

    ChrTalk(
        0xFE,
        (
            "I find myself utterly fascinated\x01",
            "by Professor Alba's studies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He has this theory that states that one of the\x01",
            "Sept-Terrions is called 'the Aureole', and\x01",
            "is lost somewhere in Liberl. Can you imagine?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AD3")

    label("loc_3A71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_3AD3")

    ChrTalk(
        0xFE,
        (
            "Well, if it isn't my favorite\x01",
            "professor!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I suspected I might see you here\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AD3")

    TalkEnd(0xFE)
    Return()

    # Function_7_2FE0 end

    def Function_8_3AD7(): pass

    label("Function_8_3AD7")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "[Tetracyclic Tower Outer Wall Segment]         Age: Pre-Septian?\x01",
            "This wall segment was cut and carried from a Tetracyclic Tower--\x01",
            "a structure built shortly after the Great Collapse.\x02\x03",
            "Depicted upon it are a staff-wielding priest and a winged god-\x01",
            "like being, typical of period frescas. Scholars continue to\x01",
            "examine the figures depicted for any connection with Aidios.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_8_3AD7 end

    def Function_9_3C78(): pass

    label("Function_9_3C78")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "[Septian 1150-1200  ~The Orbal Post-Revolutionary World~]\x01",
            "It's been only 50 years since Prof. C. Epstein discovered Orbal\x01",
            "energy, and world technology has advanced at lightning speed.\x02\x03",
            "The most notable representative of these advances is, without a\x01",
            "doubt, the modern Orbal-powered airship. Used extensively in\x01",
            "Liberl, airships are the #1 choice for civilian transportation.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_9_3C78 end

    def Function_10_3E20(): pass

    label("Function_10_3E20")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "[Pre-Septian Calendar  ~The Ancient Civilization of Zemuria~]\x01",
            "Around 1200 years ago, the advanced civilization of Zemuria was\x01",
            "at its peak. Then, suddenly and inexplicably, it disappeared.\x02\x03",
            "A 'Great Collapse' occurred, destroying the Zemurian culture and\x01",
            "plunging its people into a dark age of ruin. The items exhibited\x01",
            "on the first floor are from the very beginning of this era.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_10_3E20 end

    def Function_11_3FCD(): pass

    label("Function_11_3FCD")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "[Ancient Lantern]                              Age: Pre-Septian?\x01",
            "A device built to hold fire. Most often found near towers and\x01",
            "other ceremonial structures. May have religious significance.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_11_3FCD end

    def Function_12_40BC(): pass

    label("Function_12_40BC")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "[Stone Pillar with Relief]                     Age: Pre-Septian?\x01",
            "Found at the bottom of Lake Valleria. Adorned with reliefs\x01",
            "similar to those found on the walls of the Tetracyclic Towers.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_12_40BC end

    def Function_13_41A9(): pass

    label("Function_13_41A9")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "[Floor Tile]                                   Age: Pre-Septian?\x01",
            "A piece of tiled floor from inside a ruined building. Broken\x01",
            "stones fit together to create beautiful and intricate patterns.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_13_41A9 end

    def Function_14_4299(): pass

    label("Function_14_4299")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "[Septian Calendar 1-500  ~The Dark Age of Ruin~]\x01",
            "Immediately following the Great Collapse, this era is notable\x01",
            "for the constant formation and usurpation of small countries.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_14_4299 end

    def Function_15_4378(): pass

    label("Function_15_4378")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "[Knights' Weaponry]                    Age: Septian Calendar 500\x01",
            "In an era defined by conflict, war became a way of life, and the\x01",
            "need for warriors spawned the knight class.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_15_4378 end

    def Function_16_4458(): pass

    label("Function_16_4458")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "[Septian Calendar 500-1100  ~The Septian Era~]\x01",
            "The first appearance of the Septian Church occured around the\x01",
            "year 500, and marked the end of the Dark Age of Ruin.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Forming a religion based around the 'Goddess of the Sky' Aidios,\x01",
            "the church permeated social consciousness through humanitarian\x01",
            "aid and social unity, attracting even the knights' attentions.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_16_4458 end

    def Function_17_45F1(): pass

    label("Function_17_45F1")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "[Ancient Artifacts]                                 Age: Unknown\x01",
            "'Artifact' (noun) - A relic of any shape or size found in an\x01",
            "ancient ruin, generally of unknown or uncertain purpose.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The church believes these artifacts have some connection with\x01",
            "the Sept-Terrions-- gifts from Aidios-- and their recovery is regarded\x01",
            "as a priority one mission.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_17_45F1 end

    def Function_18_477F(): pass

    label("Function_18_477F")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "[Church Sacrament]            Age: Septian Calendar 900 (approx)\x01",
            "The church has long been a source of art, and this has been true\x01",
            "since the dawn of the Septian Era. It was around the year 900,\x01",
            "however, that the first known likeness of Aidios was created.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_18_477F end

    def Function_19_48B0(): pass

    label("Function_19_48B0")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "[Church Testaments, Manuscript]        Age: Septian Calendar 500\x01",
            "A handwritten copy of the scriptures used by the church at the\x01",
            "end of the Dark Age.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_19_48B0 end

    def Function_20_4977(): pass

    label("Function_20_4977")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "[Medieval Loom]                        Age: Septian Calendar 900\x01",
            "A man-powered machine used to spin thread. As the Septian Era\x01",
            "continued, cotton and other crops became more widely cultivated.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_20_4977 end

    SaveToFile()

Try(main)
