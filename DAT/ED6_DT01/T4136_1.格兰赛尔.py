from ED6ScenarioHelper import *

def main():
    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4136_1 ._SN',
        MapName             = 'Grancel',
        Location            = 'T4136.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60018",
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
    )

    ScpFunction(
        "Function_0_66",           # 00, 0
        "Function_1_67",           # 01, 1
        "Function_2_68",           # 02, 2
        "Function_3_134",          # 03, 3
        "Function_4_22F",          # 04, 4
        "Function_5_30A",          # 05, 5
        "Function_6_45B",          # 06, 6
        "Function_7_53B",          # 07, 7
        "Function_8_64A",          # 08, 8
        "Function_9_6D1",          # 09, 9
    )


    def Function_0_66(): pass

    label("Function_0_66")

    Return()

    # Function_0_66 end

    def Function_1_67(): pass

    label("Function_1_67")

    Return()

    # Function_1_67 end

    def Function_2_68(): pass

    label("Function_2_68")

    TalkBegin(0xFE)
    OP_A2(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_F0")

    ChrTalk(
        0xFE,
        (
            "I didn't think the assault cavalry would\x01",
            "go down so fast. Not bad at all... I have\x01",
            "a newfound respect for bracers.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12C")

    label("loc_F0")


    ChrTalk(
        0xFE,
        (
            "We can't afford to hold back.\x01",
            "Not against any of them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12C")

    Call(0, 23)
    TalkEnd(0xFE)
    Return()

    # Function_2_68 end

    def Function_3_134(): pass

    label("Function_3_134")

    TalkBegin(0xFE)
    OP_A2(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_1A3")

    ChrTalk(
        0xFE,
        (
            "There are two bracer teams still\x01",
            "in the running this year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...May the best team win.\x02",
    )

    CloseMessageWindow()
    Jump("loc_227")

    label("loc_1A3")


    ChrTalk(
        0xFE,
        (
            "All we can do is our best, and\x01",
            "our best is all we can do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Here's where we show whether or\x01",
            "not all that practice paid off!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_227")

    Call(0, 23)
    TalkEnd(0xFE)
    Return()

    # Function_3_134 end

    def Function_4_22F(): pass

    label("Function_4_22F")

    TalkBegin(0xFE)
    OP_A2(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_2CB")

    ChrTalk(
        0xFE,
        "Those Raven guys are tough customers!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's quite unusual to have non-\x01",
            "bracer civilian teams in the\x01",
            "competition. May be a first...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_302")

    label("loc_2CB")


    ChrTalk(
        0xFE,
        (
            "Is it our turn yet? I'm dyin'\x01",
            "to do some killin'!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_302")

    Call(0, 23)
    TalkEnd(0xFE)
    Return()

    # Function_4_22F end

    def Function_5_30A(): pass

    label("Function_5_30A")

    TalkBegin(0xFE)
    OP_A2(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_3C5")

    ChrTalk(
        0xFE,
        (
            "Even the Royal Army acknowledges\x01",
            "your skill. I've heard a lot\x01",
            "about you, in fact.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...I'll be watching you guys,\x01",
            "so be sure to live up to the\x01",
            "rumors, you got it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_453")

    label("loc_3C5")


    ChrTalk(
        0xFE,
        (
            "Without General Morgan here, we all need to give\x01",
            "110 percent. And we absolutely will. So you'd\x01",
            "better believe you'll be seeing us again!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_453")

    Call(0, 23)
    TalkEnd(0xFE)
    Return()

    # Function_5_30A end

    def Function_6_45B(): pass

    label("Function_6_45B")

    TalkBegin(0xFE)
    OP_A2(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_4D8")

    ChrTalk(
        0xFE,
        (
            "Hmm... The pool of competitors narrows.\x01",
            "We may find ourselves facing our most\x01",
            "feared opponents today...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_533")

    label("loc_4D8")


    ChrTalk(
        0xFE,
        (
            "Border garrison... Not to be\x01",
            "messed with, for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "But we're not about to lose!\x02",
    )

    CloseMessageWindow()

    label("loc_533")

    Call(0, 23)
    TalkEnd(0xFE)
    Return()

    # Function_6_45B end

    def Function_7_53B(): pass

    label("Function_7_53B")

    TalkBegin(0xFE)
    OP_A2(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_57B")

    ChrTalk(
        0xFE,
        (
            "Looks like you're next. Have a\x01",
            "good match!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_642")

    label("loc_57B")


    ChrTalk(
        0xFE,
        (
            "This tournament is where we military\x01",
            "and you bracers alike get to shame-\x01",
            "lessly display some prowess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Shake what you've got up there,\x01",
            "and don't lose an eye-- 'cause\x01",
            "that would really hurt!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_642")

    Call(0, 23)
    TalkEnd(0xFE)
    Return()

    # Function_7_53B end

    def Function_8_64A(): pass

    label("Function_8_64A")

    TalkBegin(0xFE)
    OP_A2(0x7)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_68E")

    ChrTalk(
        0xFE,
        (
            "I'm feeling good! Confident!\x01",
            "Tough, and alive!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C9")

    label("loc_68E")


    ChrTalk(
        0xFE,
        (
            "So don't you DARE break my focus,\x01",
            "or I will KICK you!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6C9")

    Call(0, 23)
    TalkEnd(0xFE)
    Return()

    # Function_8_64A end

    def Function_9_6D1(): pass

    label("Function_9_6D1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_726")

    ChrTalk(
        0xFE,
        (
            "I'm going out there and giving it\x01",
            "everything I've got. No regrets!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7EE")

    label("loc_726")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_77F")

    ChrTalk(
        0xFE,
        (
            "You guys are pretty good...for\x01",
            "your age. Heh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "May the best team win!\x02",
    )

    CloseMessageWindow()
    Jump("loc_7EE")

    label("loc_77F")

    OP_A2(0x6)

    ChrTalk(
        0xFE,
        "So you're bracers, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You guys are pretty good...for\x01",
            "your age. Heh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "May the best team win!\x02",
    )

    CloseMessageWindow()

    label("loc_7EE")

    Call(0, 23)
    TalkEnd(0xFE)
    Return()

    # Function_9_6D1 end

    SaveToFile()

Try(main)
