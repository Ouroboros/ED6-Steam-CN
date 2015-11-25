from ED6ScenarioHelper import *

def main():
    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4121_1 ._SN',
        MapName             = 'Grancel',
        Location            = 'T4121.x',
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
    )

    ScpFunction(
        "Function_0_66",           # 00, 0
        "Function_1_67",           # 01, 1
        "Function_2_68",           # 02, 2
        "Function_3_307",          # 03, 3
        "Function_4_A89",          # 04, 4
        "Function_5_DFE",          # 05, 5
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_75")
    Jump("loc_303")

    label("loc_75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_7F")
    Jump("loc_303")

    label("loc_7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_1CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 0)), scpexpr(EXPR_END)), "loc_113")

    ChrTalk(
        0xFE,
        (
            "#812FLooks like you haven't had a\x01",
            "moment's rest since everything\x01",
            "started.\x02\x03",
            "Take a minute now and get\x01",
            "everything squared away.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CC")

    label("loc_113")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 4)), scpexpr(EXPR_END)), "loc_1CC")

    ChrTalk(
        0xFE,
        (
            "#854FUp until now things haven't\x01",
            "made much sense, but I think \x01",
            "I'm starting to get it...\x02\x03",
            "When this much is on the line,\x01",
            "you can't help but get a bit\x01",
            "nervous, right? Heh...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CC")

    Jump("loc_303")

    label("loc_1CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_1D9")
    Jump("loc_303")

    label("loc_1D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1E3")
    Jump("loc_303")

    label("loc_1E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_1ED")
    Jump("loc_303")

    label("loc_1ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_239")

    ChrTalk(
        0xFE,
        (
            "#850FLet's do what it is we need\x01",
            "to do, the best way we can!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_303")

    label("loc_239")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_243")
    Jump("loc_303")

    label("loc_243")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_24D")
    Jump("loc_303")

    label("loc_24D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_2FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_290")

    ChrTalk(
        0xFE,
        (
            "#850FHey, new guys! Have you found\x01",
            "Zane yet?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F9")

    label("loc_290")


    ChrTalk(
        0xFE,
        (
            "#850FHey, new guys! Have you found\x01",
            "Zane yet?\x02\x03",
            "#811FI can't wait for a chance\x01",
            "to spar with you guys!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F9")

    Jump("loc_303")

    label("loc_2FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_303")

    label("loc_303")

    TalkEnd(0xFE)
    Return()

    # Function_2_68 end

    def Function_3_307(): pass

    label("Function_3_307")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_314")
    Jump("loc_A85")

    label("loc_314")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_31E")
    Jump("loc_A85")

    label("loc_31E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_3FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 0)), scpexpr(EXPR_END)), "loc_393")

    ChrTalk(
        0xFE,
        (
            "#830FI'll leave the breaking and\x01",
            "entering to you guys.\x02\x03",
            "...What? You guys can totally\x01",
            "do this!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FA")

    label("loc_393")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 3)), scpexpr(EXPR_END)), "loc_3FA")

    ChrTalk(
        0xFE,
        (
            "#832FThis is the first time I've\x01",
            "had to handle a job this big.\x02\x03",
            "We have no room for error!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FA")

    Jump("loc_A85")

    label("loc_3FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_542")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_49C")

    ChrTalk(
        0xFE,
        (
            "#831FA big match like that is going\x01",
            "to be burned into my brain for\x01",
            "a long time to come!\x02\x03",
            "I hope I can work alongside\x01",
            "you guys one day...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_53F")

    label("loc_49C")

    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "#831FCongratulations!\x02\x03",
            "A big match like that is going\x01",
            "to be burned into my brain for\x01",
            "a long time to come!\x02\x03",
            "I hope I can work alongside\x01",
            "you guys one day...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_53F")

    Jump("loc_A85")

    label("loc_542")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_54C")
    Jump("loc_A85")

    label("loc_54C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_658")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_5BF")

    ChrTalk(
        0xFE,
        (
            "#830FTomorrow's the big match.\x02\x03",
            "Don't go out there and embarrass\x01",
            "the bracers, now, you hear?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_655")

    label("loc_5BF")

    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "#830FTomorrow's the big match.\x02\x03",
            "Don't go out there and embarrass\x01",
            "the bracers, now, you hear?\x02\x03",
            "#835FNot that I think you guys will,\x01",
            "of course!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_655")

    Jump("loc_A85")

    label("loc_658")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_692")

    ChrTalk(
        0xFE,
        (
            "#831FAll righty, then.\x02\x03",
            "Let's do it to it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A85")

    label("loc_692")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_9E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_701")

    ChrTalk(
        0xFE,
        (
            "#830FLooking forward to pitting my\x01",
            "own skills against you two in\x01",
            "the very near future...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9E4")

    label("loc_701")

    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "#831FHey, you. Congratulations on\x01",
            "finishing round one.\x02\x03",
            "Bet you weren't expecting to\x01",
            "meet up with the Ravens there,\x01",
            "were you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505FIt was definitely a bit of a\x01",
            "surprise!\x02\x03",
            "#006FBut I think THEY were even MORE\x01",
            "surprised. Heh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019FIf we keep this up, we might\x01",
            "even become bracers like Agate!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#009FEw. No, one of him is plenty!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#833FHeh heh. They fought pretty\x01",
            "hard, but honestly, I was \x01",
            "surprised how well you did.\x02\x03",
            "#830FI heard all the stories about you at the\x01",
            "Ruan Branch, but you exceed your reputations\x01",
            "quite thoroughly!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008FReally?\x02\x03",
            "That's so sweet of you to say!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#831FHeh heh. I can't wait to cross\x01",
            "swords with you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001FIt's a date!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FWe're looking forward to the\x01",
            "chance ourselves.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9E4")

    Jump("loc_A85")

    label("loc_9E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_A74")

    ChrTalk(
        0xFE,
        "All righty, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Before the match, you guys should\x01",
            "warm up against a couple of monsters.\x01",
            "Get the ol' muscles stretched.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A85")

    label("loc_A74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_A7E")
    Jump("loc_A85")

    label("loc_A7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_A85")

    label("loc_A85")

    TalkEnd(0xFE)
    Return()

    # Function_3_307 end

    def Function_4_A89(): pass

    label("Function_4_A89")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_A96")
    Jump("loc_DFA")

    label("loc_A96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_AA0")
    Jump("loc_DFA")

    label("loc_AA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_BB4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 0)), scpexpr(EXPR_END)), "loc_B25")

    ChrTalk(
        0xFE,
        (
            "#824FIntelligence is resorting to\x01",
            "using hostages? That's just\x01",
            "disgusting...\x02\x03",
            "#822FLet's go save us a princess!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BB1")

    label("loc_B25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 2)), scpexpr(EXPR_END)), "loc_BB1")

    ChrTalk(
        0xFE,
        (
            "#822FColonel Richard, staging a\x01",
            "coup d'etat? I'd've never\x01",
            "believed it before today.\x02\x03",
            "He's a pretty smooth liar, I\x01",
            "must admit...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BB1")

    Jump("loc_DFA")

    label("loc_BB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_BBE")
    Jump("loc_DFA")

    label("loc_BBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_BC8")
    Jump("loc_DFA")

    label("loc_BC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_CA8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_C35")

    ChrTalk(
        0xFE,
        (
            "#820FWe lost, but we lost in a good\x01",
            "fight. No regrets.\x02\x03",
            "Go win the championship, guys!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CA5")

    label("loc_C35")

    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "#820FHey, everybody!\x02\x03",
            "We lost, but we lost in a good\x01",
            "fight. No regrets.\x02\x03",
            "Go win the championship, guys!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CA5")

    Jump("loc_DFA")

    label("loc_CA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_CB2")
    Jump("loc_DFA")

    label("loc_CB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_DDF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_D40")

    ChrTalk(
        0xFE,
        (
            "#821FTomorrow, it's all about fighting\x01",
            "the big boys... Makin' a big noise\x01",
            "with some big toys...\x02\x03",
            "You'd better bring it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DDC")

    label("loc_D40")

    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "#821FGood work out there today.\x02\x03",
            "Tomorrow, it's all about fighting\x01",
            "the big boys... Makin' a big noise\x01",
            "with some big toys...\x02\x03",
            "You'd better bring it!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DDC")

    Jump("loc_DFA")

    label("loc_DDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_DE9")
    Jump("loc_DFA")

    label("loc_DE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_DF3")
    Jump("loc_DFA")

    label("loc_DF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_DFA")

    label("loc_DFA")

    TalkEnd(0xFE)
    Return()

    # Function_4_A89 end

    def Function_5_DFE(): pass

    label("Function_5_DFE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_E0B")
    Jump("loc_10C5")

    label("loc_E0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_E15")
    Jump("loc_10C5")

    label("loc_E15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_F18")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 0)), scpexpr(EXPR_END)), "loc_E7B")

    ChrTalk(
        0xFE,
        (
            "#840FWe're the only ones who can\x01",
            "possibly pull this off.\x02\x03",
            "So let's get pulling!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F15")

    label("loc_E7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 5)), scpexpr(EXPR_END)), "loc_F15")

    ChrTalk(
        0xFE,
        (
            "#845FWell, that was certainly embarrassing.\x02\x03",
            "I am bothered by my missing memories,\x01",
            "but right now, the queen's orders are\x01",
            "foremost on my mind.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F15")

    Jump("loc_10C5")

    label("loc_F18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_1082")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_FB8")

    ChrTalk(
        0xFE,
        (
            "#840FSeeing you young bracers in\x01",
            "action is a pretty big motivator\x01",
            "for the rest of us.\x02\x03",
            "I can't just let myself get\x01",
            "left behind, you know?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_107F")

    label("loc_FB8")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "#840FHey, congratulations. That\x01",
            "was an impressive match.\x02\x03",
            "Seeing you young bracers in\x01",
            "action is a pretty big motivator\x01",
            "for the rest of us.\x02\x03",
            "I can't just let myself get\x01",
            "left behind, you know?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_107F")

    Jump("loc_10C5")

    label("loc_1082")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_108C")
    Jump("loc_10C5")

    label("loc_108C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_1096")
    Jump("loc_10C5")

    label("loc_1096")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_10A0")
    Jump("loc_10C5")

    label("loc_10A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_10AA")
    Jump("loc_10C5")

    label("loc_10AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_10B4")
    Jump("loc_10C5")

    label("loc_10B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_10BE")
    Jump("loc_10C5")

    label("loc_10BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_10C5")

    label("loc_10C5")

    TalkEnd(0xFE)
    Return()

    # Function_5_DFE end

    SaveToFile()

Try(main)
