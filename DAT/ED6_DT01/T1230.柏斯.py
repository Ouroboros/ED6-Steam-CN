from ED6ScenarioHelper import *

def main():
    # 柏斯

    CreateScenaFile(
        FileName            = 'T1230   ._SN',
        MapName             = 'Bose',
        Location            = 'T1230.x',
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
        'Apple',                                # 9
        'Limon',                                # 10
        'Lore',                                 # 11
        'Pesca',                                # 12
        'Melony',                               # 13
        'Anelace',                              # 14
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
        'ED6_DT07/CH01150 ._CH',             # 00
        'ED6_DT07/CH01050 ._CH',             # 01
        'ED6_DT07/CH01123 ._CH',             # 02
        'ED6_DT07/CH01023 ._CH',             # 03
        'ED6_DT07/CH01143 ._CH',             # 04
        'ED6_DT07/CH01033 ._CH',             # 05
        'ED6_DT07/CH01630 ._CH',             # 06
    )

    AddCharChipPat(
        'ED6_DT07/CH01150P._CP',             # 00
        'ED6_DT07/CH01050P._CP',             # 01
        'ED6_DT07/CH01123P._CP',             # 02
        'ED6_DT07/CH01023P._CP',             # 03
        'ED6_DT07/CH01143P._CP',             # 04
        'ED6_DT07/CH01033P._CP',             # 05
        'ED6_DT07/CH01630P._CP',             # 06
    )

    DeclNpc(
        X                   = -730,
        Z                   = 0,
        Y                   = 5300,
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
        X                   = 440,
        Z                   = 0,
        Y                   = 32439,
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
        X                   = -960,
        Z                   = 270,
        Y                   = 34690,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -1680,
        Z                   = 270,
        Y                   = 32310,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -1660,
        Z                   = 300,
        Y                   = 31080,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -700,
        Z                   = 0,
        Y                   = 35300,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )


    DeclActor(
        TriggerX            = -780,
        TriggerZ            = 0,
        TriggerY            = 4190,
        TriggerRange        = 400,
        ActorX              = -700,
        ActorZ              = 1500,
        ActorY              = 5300,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -1500,
        TriggerZ            = 0,
        TriggerY            = 31600,
        TriggerRange        = 400,
        ActorX              = 440,
        ActorZ              = 1500,
        ActorY              = 32439,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1EA",          # 00, 0
        "Function_1_248",          # 01, 1
        "Function_2_280",          # 02, 2
        "Function_3_296",          # 03, 3
        "Function_4_313",          # 04, 4
        "Function_5_ABD",          # 05, 5
        "Function_6_AC2",          # 06, 6
        "Function_7_137C",         # 07, 7
        "Function_8_147E",         # 08, 8
        "Function_9_164F",         # 09, 9
        "Function_10_16E7",        # 0A, 10
    )


    def Function_0_1EA(): pass

    label("Function_0_1EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_1F4")
    Jump("loc_247")

    label("loc_1F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_212")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0x9, 0x10)
    Jump("loc_247")

    label("loc_212")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 5)), scpexpr(EXPR_END)), "loc_221")
    ClearChrFlags(0xD, 0x80)
    Jump("loc_247")

    label("loc_221")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 4)), scpexpr(EXPR_END)), "loc_22B")
    Jump("loc_247")

    label("loc_22B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_247")
    SetChrPos(0x9, 1360, 0, 38700, 45)
    Jump("loc_247")

    label("loc_247")

    Return()

    # Function_0_1EA end

    def Function_1_248(): pass

    label("Function_1_248")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_252")
    Jump("loc_27F")

    label("loc_252")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_25C")
    Jump("loc_27F")

    label("loc_25C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 5)), scpexpr(EXPR_END)), "loc_266")
    Jump("loc_27F")

    label("loc_266")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 4)), scpexpr(EXPR_END)), "loc_270")
    Jump("loc_27F")

    label("loc_270")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27F")
    OP_64(0x1, 0x1)
    Jump("loc_27F")

    label("loc_27F")

    Return()

    # Function_1_248 end

    def Function_2_280(): pass

    label("Function_2_280")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_295")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_280")

    label("loc_295")

    Return()

    # Function_2_280 end

    def Function_3_296(): pass

    label("Function_3_296")

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
            "Rest\x01",       # 1
            "Leave\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F6")
    OP_0D()
    OP_A9(0xF)
    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_2F6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_307")
    TalkEnd(0x8)
    Return()

    label("loc_307")

    Call(0, 4)
    OP_8C(0x8, 180, 0)
    Return()

    # Function_3_296 end

    def Function_4_313(): pass

    label("Function_4_313")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_390")

    ChrTalk(
        0x8,
        (
            "I'm glad I started this place\x01",
            "with Limon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Now I've got to work harder to\x01",
            "make this place a success...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AB9")

    label("loc_390")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_434")

    ChrTalk(
        0x8,
        (
            "Limon will come and help me to\x01",
            "do the cleaning in the morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "And I'll come to help Limon in\x01",
            "the bar when it gets crowded\x01",
            "during the evenings.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AB9")

    label("loc_434")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_4C4")

    ChrTalk(
        0x8,
        (
            "Sometimes I wonder if Limon is\x01",
            "okay by herself running the bar...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If it looks like she's busy,\x01",
            "I want to help her out, too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AB9")

    label("loc_4C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 5)), scpexpr(EXPR_END)), "loc_627")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5EE")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "I know I'm a bit shy, but I love\x01",
            "doing this job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We get people from all over with\x01",
            "interesting stories about the world...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "And it makes me feel all warm and\x01",
            "tingly inside just hearing them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm so happy when someone who\x01",
            "stayed here before comes back\x01",
            "again...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_624")

    label("loc_5EE")


    ChrTalk(
        0x8,
        (
            "I know I'm a bit shy, but I love\x01",
            "doing this job.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_624")

    Jump("loc_AB9")

    label("loc_627")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 4)), scpexpr(EXPR_END)), "loc_9DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_972")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "When it becomes the right season,\x01",
            "people can come and experience\x01",
            "picking fresh fruit from the trees.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 0)

    ChrTalk(
        0x101,
        (
            "#0508FDid you hear that Joshua?\x01",
            "We can come here and pick fruit!\x02\x03",
            "#001FCan we come here again sometime\x01",
            "so we can gorge ourselves on all\x01",
            "the good stuff around here?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 0)

    ChrTalk(
        0x102,
        (
            "#018FI should've figured you'd say\x01",
            "something like that, Estelle...\x02\x03",
            "#010FAnyway, I think it's a little\x01",
            "early for that.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x102, 0)

    ChrTalk(
        0x8,
        (
            "Yeah, that's right. It'll still be another\x01",
            "several months before the fruit is ripe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007FWhy do you have to go and\x01",
            "say something like that? I\x01",
            "got all excited for nothing...\x02\x03",
            "#001FWell, let's at least come back\x01",
            "again when it's picking season,\x01",
            "okay?\x02\x03",
            "And when we don't have a job\x01",
            "to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FWhatever you say, Estelle.\x02\x03",
            "Didn't you say the same thing\x01",
            "about shopping in Bose?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Ha ha ha.\x02",
    )

    CloseMessageWindow()
    Jump("loc_9DC")

    label("loc_972")


    ChrTalk(
        0x8,
        (
            "When it becomes the right season,\x01",
            "people can come and experience\x01",
            "picking fresh fruit from the trees.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9DC")

    Jump("loc_AB9")

    label("loc_9DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_A79")

    ChrTalk(
        0x8,
        "U-Um...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'd like to recommend the\x01",
            "squeezed juice in the bar on\x01",
            "the second floor, if I could.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Please give it a try if you'd like.\x02",
    )

    CloseMessageWindow()
    Jump("loc_AB9")

    label("loc_A79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_AB9")

    ChrTalk(
        0x8,
        "W-Welcome...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Are you...here to stay the night?\x02",
    )

    CloseMessageWindow()

    label("loc_AB9")

    TalkEnd(0x8)
    Return()

    # Function_4_313 end

    def Function_5_ABD(): pass

    label("Function_5_ABD")

    Call(0, 6)
    Return()

    # Function_5_ABD end

    def Function_6_AC2(): pass

    label("Function_6_AC2")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_B3A")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B29")
    OP_0D()
    OP_A9(0x16)
    OP_56(0x0)
    TalkEnd(0x9)
    Return()

    label("loc_B29")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B3A")
    TalkEnd(0x9)
    Return()

    label("loc_B3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_BF0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BB6")
    OP_A2(0x1)

    ChrTalk(
        0x9,
        "Welcome, everyone!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I've just finished making\x01",
            "some fresh fruit juice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "How about a glass?\x02",
    )

    CloseMessageWindow()
    Jump("loc_BED")

    label("loc_BB6")


    ChrTalk(
        0x9,
        (
            "I've just finished making\x01",
            "some fresh fruit juice.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BED")

    Jump("loc_1378")

    label("loc_BF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_CE2")

    ChrTalk(
        0x9,
        (
            "If I remember right, there's a\x01",
            "village meeting going on today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The village elder came by this\x01",
            "morning, and he seemed to\x01",
            "have a lot on his mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I hope he doesn't worry\x01",
            "too much because it'll\x01",
            "start eroding his health.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1378")

    label("loc_CE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_D49")

    ChrTalk(
        0x9,
        (
            "Today is a little bit more\x01",
            "crowded than I expected...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Apple! A little help please!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1378")

    label("loc_D49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 5)), scpexpr(EXPR_END)), "loc_E4F")

    ChrTalk(
        0x9,
        (
            "I started this place with my\x01",
            "childhood friend, Apple.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Of course, I was the one who\x01",
            "invited her to join me in this\x01",
            "venture.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "She's a bit of an introvert so I wasn't\x01",
            "sure she was up for it, but she was\x01",
            "surprisingly eager to give it a shot.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1378")

    label("loc_E4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 4)), scpexpr(EXPR_END)), "loc_EE1")

    ChrTalk(
        0x9,
        (
            "Hmm, I wonder if I should increase\x01",
            "the number of dishes that use fruit\x01",
            "in them...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'll have to discuss this with Apple\x01",
            "later.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1378")

    label("loc_EE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_1301")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1297")
    OP_A2(0x1)

    ChrTalk(
        0x9,
        "Welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If you're here for a drink, I recommend\x01",
            "that you try our various types of fruit\x01",
            "wines.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Our ingredients are the freshest\x01",
            "and finest in all of Liberl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020FThat sounds great. But if you don't\x01",
            "mind me asking, this place wasn't\x01",
            "around before, was it?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x103, 0)

    ChrTalk(
        0x9,
        (
            "Yes, that's right. We just opened\x01",
            "the place recently. I hope you'll\x01",
            "come visit us often.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020FSo what's the recommended\x01",
            "item on your menu right now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Let's see, the pomegranate wine and\x01",
            "the apricot tart set is delightful.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 0)

    ChrTalk(
        0x101,
        (
            "#509FSchera, shouldn't we be investigating\x01",
            "things first?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 0)

    ChrTalk(
        0x103,
        (
            "#020FAnd that's exactly what we're doing.\x02\x03",
            "Speaking with local residents can\x01",
            "net us some information as well.\x02\x03",
            "#020FYou don't need to be in such\x01",
            "a hurry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505FI wonder if she's really serious\x01",
            "about what she says.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x103, 0)

    ChrTalk(
        0x102,
        (
            "#019FHa ha. Who knows? But whenever\x01",
            "it comes to her and alcohol, her\x01",
            "credibility isn't that great.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12FE")

    label("loc_1297")


    ChrTalk(
        0x9,
        (
            "Have a bite to eat, something to\x01",
            "drink and when you get tired,\x01",
            "take a rest downstairs at the inn.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12FE")

    Jump("loc_1378")

    label("loc_1301")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_1378")

    ChrTalk(
        0x9,
        "Are you guests?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I apologize, but I'm in the middle\x01",
            "of getting everything ready for the\x01",
            "day right now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1378")

    TalkEnd(0x9)
    Return()

    # Function_6_AC2 end

    def Function_7_137C(): pass

    label("Function_7_137C")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_142A")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "We're going to have the village elder\x01",
            "open a meeting to discuss policy\x01",
            "regarding orchard cultivation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope there'll be some sort\x01",
            "of development.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_147A")

    label("loc_142A")


    ChrTalk(
        0xFE,
        "I wonder what Pomme is up to.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope he's getting along well\x01",
            "in Bose.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_147A")

    TalkEnd(0xA)
    Return()

    # Function_7_137C end

    def Function_8_147E(): pass

    label("Function_8_147E")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1615")
    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "I don't think we should just continue\x01",
            "on in the old ways.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think we need to find a more inventive\x01",
            "approach where we can achieve a\x01",
            "constant output of products.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You can see how all of the fruit\x01",
            "producing trees are short, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "That was something I suggested.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I figured that if we didn't have to deal\x01",
            "with high places, we wouldn't need\x01",
            "so many hands to do the work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_164B")

    label("loc_1615")


    ChrTalk(
        0xFE,
        (
            "Man, I wish I could just\x01",
            "get Gray to understand.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_164B")

    TalkEnd(0xB)
    Return()

    # Function_8_147E end

    def Function_9_164F(): pass

    label("Function_9_164F")

    TalkBegin(0xC)

    ChrTalk(
        0xFE,
        (
            "I really want people to somehow\x01",
            "be able to understand my\x01",
            "husband's ideas.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think in the end it's in the best\x01",
            "interest of the village.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xC)
    Return()

    # Function_9_164F end

    def Function_10_16E7(): pass

    label("Function_10_16E7")

    TalkBegin(0xD)
    TurnDirection(0xFE, 0x103, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A0C")
    OP_A2(0x360)
    OP_A2(0x6)
    TurnDirection(0xFE, 0x103, 0)

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
            "this area.\x02",
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

    ChrTalk(
        0xFE,
        (
            "#819FAh ha ha... Uh...let's avoid that subject\x01",
            "right now. I'm still working on it.\x02\x03",
            "#810FBy the way, Scherazard, are you\x01",
            "here on a job for the guild?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020FYeah, something like that. Although\x01",
            "the job's a little different from the\x01",
            "one you're handling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#810FIs that so... Well, this region\x01",
            "has been becoming more\x01",
            "dangerous recently.\x02\x03",
            "Make sure to be careful.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B6F")

    label("loc_1A0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AF7")
    OP_A2(0x6)

    ChrTalk(
        0x103,
        "#020FWell, if it isn't Anelace...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 0)

    ChrTalk(
        0xFE,
        (
            "#814FOh hi, Scherazard...\x02\x03",
            "Don't tell me you're here on\x01",
            "a job with the guild too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#020FActually, yeah.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#810FIt seems like we're all bogged\x01",
            "down with work, huh?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B6F")

    label("loc_1AF7")

    TurnDirection(0xFE, 0x103, 0)

    ChrTalk(
        0xFE,
        (
            "#810FOne more thing, Scherazard.\x01",
            "The region has become really\x01",
            "dangerous recently.\x02\x03",
            "Make sure to be careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B6F")

    TalkEnd(0xD)
    Return()

    # Function_10_16E7 end

    SaveToFile()

Try(main)
